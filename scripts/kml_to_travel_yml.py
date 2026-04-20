#!/usr/bin/env python3
# /// script
# requires-python = ">=3.9"
# dependencies = ["pyyaml"]
# ///
"""
kml_to_travel_yml.py — Convert a Google My Maps KML/KMZ export into
_data/travel.yml format for the travel page.

Usage:
    uv run scripts/kml_to_travel_yml.py path/to/footprints.kml
    uv run scripts/kml_to_travel_yml.py path/to/footprints.kmz

Writes to _data/travel.yml (merging with existing entries, de-duped by
place+country). Existing entries keep their `date`, `note`, `photos`,
etc. — the script only fills lat/lon/place/country for new pins.

Fields filled from KML:
    place    — <name> of the Placemark
    country  — last comma-segment of <address>, or folder name, or ""
    lat, lon — parsed from <coordinates>lon,lat,alt</coordinates>

Fields you still need to fill by hand after running:
    date     — "YYYY-MM"
    slug     — url-friendly folder name under img/travel/<slug>/
    note     — 1-3 sentences of prose
    photos   — list of filenames (optional)

Run again after you edit _data/travel.yml — new pins get appended, your
hand-written notes/dates are preserved.
"""

import argparse
import re
import sys
import xml.etree.ElementTree as ET
import zipfile
from pathlib import Path

import yaml

NS = {"kml": "http://www.opengis.net/kml/2.2"}


def load_kml(path: Path) -> str:
    """Load KML text from a .kml or .kmz file."""
    if path.suffix.lower() == ".kmz":
        with zipfile.ZipFile(path) as z:
            # Google's KMZ puts the KML at doc.kml
            candidates = [n for n in z.namelist() if n.lower().endswith(".kml")]
            if not candidates:
                sys.exit(f"No .kml found inside {path}")
            return z.read(candidates[0]).decode("utf-8")
    return path.read_text(encoding="utf-8")


def slugify(s: str) -> str:
    s = s.lower().strip()
    s = re.sub(r"[^a-z0-9]+", "-", s)
    return s.strip("-")


def country_from_address(addr: str) -> str:
    if not addr:
        return ""
    # Last comma-separated segment, stripped of postal codes.
    segs = [seg.strip() for seg in addr.split(",") if seg.strip()]
    if not segs:
        return ""
    last = segs[-1]
    # Strip a trailing ZIP-like token (e.g. "New York, NY 10001, USA")
    last = re.sub(r"\b\d{3,6}(-\d+)?\b", "", last).strip()
    return last


def parse_placemarks(kml_text: str):
    root = ET.fromstring(kml_text)
    out = []

    # Walk folders so we can inherit a folder name as a country fallback.
    def walk(node, folder_name=""):
        # Folders may contain their own <name> before nested Placemarks.
        for child in node:
            tag = child.tag.split("}", 1)[-1]
            if tag == "Folder":
                inner = child.find("kml:name", NS)
                inner_name = inner.text.strip() if inner is not None and inner.text else folder_name
                walk(child, inner_name)
            elif tag == "Placemark":
                name_el = child.find("kml:name", NS)
                addr_el = child.find("kml:address", NS)
                point_el = child.find("kml:Point", NS)
                if point_el is None:
                    # Skip lines/polygons — we only want point pins.
                    continue
                coords_el = point_el.find("kml:coordinates", NS)
                if coords_el is None or not coords_el.text:
                    continue
                coord_txt = coords_el.text.strip().split()[0]  # first coord triple
                parts = coord_txt.split(",")
                if len(parts) < 2:
                    continue
                try:
                    lon = float(parts[0])
                    lat = float(parts[1])
                except ValueError:
                    continue
                place = (name_el.text or "").strip() if name_el is not None else ""
                address = (addr_el.text or "").strip() if addr_el is not None else ""
                country = country_from_address(address) or folder_name
                out.append({
                    "place": place,
                    "country": country,
                    "lat": round(lat, 4),
                    "lon": round(lon, 4),
                    "date": "",          # fill by hand
                    "slug": slugify(place) if place else "",
                    "note": "",          # fill by hand
                })
            else:
                walk(child, folder_name)

    walk(root)
    return out


def merge_with_existing(new_items, existing_path: Path):
    """Preserve any hand-written date/note/photos on existing entries."""
    if not existing_path.exists():
        return new_items
    try:
        existing = yaml.safe_load(existing_path.read_text(encoding="utf-8")) or []
    except yaml.YAMLError as e:
        sys.exit(f"Couldn't parse existing {existing_path}: {e}")
    if not isinstance(existing, list):
        existing = []

    def key(item):
        return (item.get("place", "").lower(), item.get("country", "").lower())

    existing_by_key = {key(e): e for e in existing if isinstance(e, dict)}
    merged = []
    for item in new_items:
        k = key(item)
        if k in existing_by_key:
            prev = existing_by_key.pop(k)
            # Keep existing date/note/photos/cover/slug; refresh lat/lon.
            prev["lat"] = item["lat"]
            prev["lon"] = item["lon"]
            merged.append(prev)
        else:
            merged.append(item)
    # Append any existing items that weren't matched (KML doesn't know about them).
    for leftover in existing_by_key.values():
        merged.append(leftover)
    return merged


def dump_yaml(items, out_path: Path):
    header = out_path.read_text(encoding="utf-8").split("\n\n", 1)[0] if out_path.exists() else ""
    # Keep any leading comment header if it exists; else write a minimal one.
    if not header.lstrip().startswith("#"):
        header = (
            "# Travel log — one block per trip. Generated from Google My Maps KML.\n"
            "# To add a trip by hand, append a block below. To refresh from KML, re-run\n"
            "#   uv run scripts/kml_to_travel_yml.py <path/to/export.kml>\n"
        )
    body = yaml.safe_dump(items, allow_unicode=True, sort_keys=False, default_flow_style=False)
    out_path.write_text(header.rstrip() + "\n\n" + body, encoding="utf-8")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("kml_path", help="Path to the .kml or .kmz file from Google My Maps → Export")
    ap.add_argument("--out", default="_data/travel.yml", help="Where to write YAML (default: _data/travel.yml)")
    ap.add_argument("--dry-run", action="store_true", help="Print to stdout instead of writing")
    args = ap.parse_args()

    path = Path(args.kml_path).expanduser()
    if not path.exists():
        sys.exit(f"File not found: {path}")

    kml_text = load_kml(path)
    items = parse_placemarks(kml_text)
    if not items:
        sys.exit("No point Placemarks found in the KML. Check the export.")

    out_path = Path(args.out)
    merged = merge_with_existing(items, out_path)

    if args.dry_run:
        yaml.safe_dump(merged, sys.stdout, allow_unicode=True, sort_keys=False, default_flow_style=False)
    else:
        out_path.parent.mkdir(parents=True, exist_ok=True)
        dump_yaml(merged, out_path)
        print(f"Wrote {len(merged)} entries to {out_path} ({len(items)} from KML).")
        missing_date = sum(1 for m in merged if not m.get("date"))
        if missing_date:
            print(f"→ {missing_date} entries still need a date (YYYY-MM) — edit {out_path} and fill them in.")


if __name__ == "__main__":
    main()
