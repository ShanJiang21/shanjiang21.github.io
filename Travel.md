---
layout: page
title: "Travel"
description: “Adventures fill my soul"
header-img: "img/"
header-mask: 0.3
multilingual: true
---

{% include multilingual-sel.html %}

<!-- Chinese Version -->
<div class="zh post-container">
    {% capture about_zh %}{% include about/zh.md %}{% endcapture %}
    {{ about_zh | markdownify }}
</div>

<!-- English Version -->
<div class="en post-container">
    {% capture about_en %}{% include about/en.md %}{% endcapture %}
    {{ about_en | markdownify }}
</div>

<div class="quote-container">
    <div class="quote-author">Krystle Wright</div>
    <div class="quote-location">Imperial, Nebraska</div>
    <div class="quote-content">
      It’s a tough thing to see because you feel this contradiction. On one hand it’s just like, Oh my God, I can’t believe I’m witnessing this absolute phenomenon. But then at the same time, particularly when it’s going through a town, you realize, Well, this is absolutely destroying lives.
    </div>
    <div class="quote-divider"></div>
    <div class="additional-text">
      Photographer Krystle Wright and fellow storm chasers arrived on the scene just as a supercell storm spitting lightning threatened a farm with a UFO-like “mother ship” formation in May 2019. The team’s timing that day was “sheer luck,” Wright recalls. After retreating from a storm in Colorado that pounded their SUV with hail, they crossed into Nebraska and caught up to this system at the apex of its power.
    </div>
  </div>