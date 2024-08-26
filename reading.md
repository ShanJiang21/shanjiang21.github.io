---
layout: page
title: "Reading"
description: “You are what you read"
header-img: "img/bg-walle.jpg"
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
