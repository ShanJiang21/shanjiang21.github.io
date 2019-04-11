---
layout: page
title: "About"
author: "Shan J."
description: "Me, myself."
header-img: "img/about-bg-walle.jpg"
multilingual: true
---

<!-- Language Selector -->
<select class="sel-lang" onchange= "onLanChange(this.options[this.options.selectedIndex].value)">
    <option value="0" selected> 中文 Chinese </option>
    <option value="1"> 英文 English </option>
</select>

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


<img src= "assets/images/index.jpg" alt="">

<blockquote class="full-width"><p>A student, runner and Enthusiast for statistics.</p></blockquote>


I am Shan Jiang(<span lang="zh">姜珊</span>), a master student at the Department of biostatistics, from [Columbia University](https://www.mailman.columbia.edu/become-student/departments/biostatistics), my research interests fall into computational social science and network analysis, health sociology. Prior to my graduate school studies, I received my B.A. at [Central University of Finance and Economics](http://en.cufe.edu.cn/), China.

This website contains several main sections including my projects, my comments on classical sociological papers, statistical resources, and some tutorials for data visualization in R.

### Education

* B.A. Sociology(Minor Economics), Central University of Finance and Economics, China, 2014 – 2018
* Exchange, Johns Hopkins University, US, 2016
* M.S. Biostatistics(Theory and Methods), Columbia University, US, 2018 – Now

###  My Projects

Below is an incomplete list of packages and projects I have worked on.

* [Data science jobs outlook](https://shanjiang21.github.io/P8105_final_website.io/)
* [Shiny](https://github.com/ShanJiang21/Shiny_lec)

<img src= "assets/images/Data_science.jpg" style="width:28%">

### Preferred links  

#### Academic resources

* [Data Science](https://p8105.com/)
* [Introduction to Data Science 2018 Spring](https://beanumber.github.io/sds192/index.html)
* [Introduction to Data Science 2018 Fall](https://rudeboybert.github.io/SDS192/)
* [R for data science](http://r4ds.had.co.nz/), Garrett Grolemund and Hadley Wickham, O’Reilly, 2017. Available free online.
* [Datacamp](https://www.datacamp.com/groups/8702c0fa3e62145fd1a543715dddc3a3645cd03c/invite), online programming courses for data science. Available for free using links on Moodle.
* [Generalized Linear models](https://data.princeton.edu/wws509/sets)


### Statistics resources

#### Top R packages

* [Rcpp](http://adv-r.had.co.nz/Rcpp.html), provides a combination of R and C++.
* [stringr](https://cran.r-project.org/web/packages/stringr/vignettes/stringr.html), extremely useful for text mining.
* [ggplot](https://www.mailman.columbia.edu/sites/default/files/media/fdawg_ggplot2.html), a well-known pakage for data visualization.
* [Table 1](https://cran.r-project.org/web/packages/table1/vignettes/table1-examples.html), extremely usefu for organizing tables for publish on journals.

#### Blogs and online books

* [Yihui Xie's Blog](https://yihui.name/)
* [Text Mining](https://github.com/dgrtwo/tidy-text-mining)
* [R Markdown Fixes](https://docs.google.com/document/d/1P7IyZ4On9OlrCOhygFxjC7XhQqyw8OludwChz-uFd_o/edit)
* [Word Count add-in](https://github.com/benmarwick/wordcountaddin)
* [soft-ware tutorial](http://www.smart-stats.org/content/software-tutorials)

### Computational Sociology resource

* [Five Thirty Eight](https://fivethirtyeight.com/) for political data visualization;
* [Introduction to Educational and Psychological Measurement Using R](https://www.thetaminusb.com/intro-measurement-r/) for factor analysis and scaling, scoring.
* [Working Group on Computational Social Science @Columbia](http://css.iserp.columbia.edu/),



{% if site.disqus_username %}
<!-- disqus 评论框 start -->
<div class="comment">
    <div id="disqus_thread" class="disqus-thread">

    </div>
</div>
<!-- disqus 评论框 end -->

<!-- disqus 公共JS代码 start (一个网页只需插入一次) -->
<script type="text/javascript">
    /* * * CONFIGURATION VARIABLES * * */
    var disqus_shortname = "{{site.disqus_username}}";
    var disqus_identifier = "{{site.disqus_username}}/{{page.url}}";
    var disqus_url = "{{site.url}}{{page.url}}";

    (function() {
        var dsq = document.createElement('script'); dsq.type = 'text/javascript'; dsq.async = true;
        dsq.src = '//' + disqus_shortname + '.disqus.com/embed.js';
        (document.getElementsByTagName('head')[0] || document.getElementsByTagName('body')[0]).appendChild(dsq);
    })();
</script>
<!-- disqus 公共JS代码 end -->
{% endif %}
