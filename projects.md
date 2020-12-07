---
title: Projects
layout: page
header-img: "./img/projects.jpg"
description: Where my time goes? Get a hint from below.
---

This website is for presentation of samples on some of the cool side-projects I've been working on
Last update: *Dec. 2020*

<!-- Prepare a container for your calendar. -->
<script
  src="https://cdn.rawgit.com/IonicaBizau/github-calendar/gh-pages/dist/github-calendar.min.js"
>
</script>

<!-- Optionally, include the theme (if you don't want to struggle to write the CSS) -->
<link
  rel="stylesheet"
  href="https://cdn.rawgit.com/IonicaBizau/github-calendar/gh-pages/dist/github-calendar.css"
/>

<!-- Prepare a container for your calendar. -->
<div class="calendar">
    <!-- Loading stuff -->
    Loading the data just for you.
</div>

<script>
    new GitHubCalendar(".calendar", "shanjiang21");
</script>


### Projects

Below is an incomplete list of projects I have been working on and contributed to.

* [Pending PhD Program](#pending-phd-program)
* [Data science jobs outlook](#data-science-jobs-outlook-(NLP-using-R-))
* [Bangledesh Migrants Study](#bangledesh-migrants-study)
* [Media Bias on Protest Events](#social-protest-analysis)
* [Social network Analysis visualization](#social-network-analysis-visualization)
* [Energy Insecurity Instrument Scaling](#Energy-Insecurity-Instrument-scaling)


#### Pending-phd-program

The year of 2020 marks a critical turning point in my life, and I believe it also applies to many grad school students. Last year around late Nov., I was struggling hard in the Butler library, relying heavily on coffee beans to stay until late night. This year I witnessed how an individual's fate can be tweaked and the unintended consequences changed my life. Thus, I made this dashboard to update stakeholders up-to-date suspending social science PhD programs in the US, stay tuned, spring will come. 

<iframe src="https://shanj21.shinyapps.io/Pending_PhD_program_2021/" width=1000 height=800></iframe>


#### Data science jobs outlook (NLP using R)

<tr>
   <td> <img src="../img/job_outlook.png" alt="Drawing" style="width: 500px;"/> </td>
   </tr>


[Click Here](https://shanjiang21.github.io/P8105_final_website.io/) for a the full introduction for the project.

Data Scientist Job Posts in the U.S on Indeed Website in 2018 August. This Indeed dataset originates from Indeed website, containing 7,000 data scientist jobs around the U.S. by August 3rd, 2018. Main variables include Company Name, Position Name,  Location, Job Description, and Number of Reviews of the Company. We mainly squared at the job description column that contains information such as a short description of company and position, requirement and route of application.

Based on the ranking of total revenues of each company’s retrospective fiscal year, Fortune magazine’s annual report of top 500 largest companies in the U.S has always been regarded as a reliable measurement for the value of a company. Many of the Fortune 500 companies now have a job title of Chief Data Scientist or Head of Analytics, and some Internet magnets have invested much on data mining, Artificial Intelligence or related areas.

Comparison of top-500 companies and non-top 500 companies are based on Data from The 500 Largest Industrial Corporations in the U.S., Published by Fortune magazine (updated by October 5, 2018)
Given that differences of preference of these big-names and small companies may have for employees, we will combine the Fortune 500 company list and our Indeed dataset by company name. Through creating a new logical variable named flag to indicate whether each company falls into Fortune 500 companies category or not, this full dataset will be adopted for our Exploratory analysis.


#### Social Protest Analysis

How can you map news media Bias on Protest Events in China? Among the goals of demonstrators, media coverage is always treated as the priority and embedded as one of the most crucial objectives. It is not uncommon to see that protests usually involve an enduring contest on the control of media between the challengers and authorities, which precedingly shapes the public opinion along political process (Tarrow 1998; Oliver & Maney 2000). However, news is not fixed, the dynamic flow of information in an ordinary day have become a mix of multi-level sources in recent decade. Increasingly polarized political environments and declining social trust level have also transformed the public perceptions of news, in particular, protests, online activisms and also the diffusion patterns of events (Scheufele & Krause 2019).
Which protest is Newsworthy? Will the continuing coverage or tracking of long-lasting protests more frequent in local-circulated print-news than national-circulated papers?

I am trying to answer these questions by applying an examination of WiseNews data, a Hong Kong based newspaper database, which covers around 1,500 newspapers from mainland China, Hong Kong and Taiwan (Chu et al. 2009), and social media data with the application of CASM algorithm (Zhang & Pan 2019).


#### Bangladesh Migrants Study

The project is aiming at evaluate the living conditions of Bangladesh Domestic Migrants for offering financial-aid policy consultation for USAID evaluation.

<td> <img src="../img/dhs_t6_1.png" alt="Drawing" style="width: 800px;"/> </td>
Our analysis shows that, in general, migrant households are poorer on average than urban non-migrant households. Specifically, as measured by wealth index, migrant households are more likely to be in the two poorest wealth quintiles and less likely to be in the richer quintiles (Table 1). But at the same time, it is worth noting that the economic well-being of rural-urban migrants follow a bi-modal distribution: while many of them are in the poor quintiles, a large fraction of these migrants are in the two richest groups. Hence, it is important to examine migrants of different socioeconomic groups separately.

<tr>
   <td> <img src="../img/dhs_t1.png" alt="Drawing" style="width: 560px;"/> </td>
   </tr>


Several findings have beyond my expectation:

* The minor marriage happens for more than half of the girls before 18 years old.
* 22% girls needs to get their marriage before 15 years old.
* The work-abuse are mainly focus on the verbal abuse.

 <td> <img src="../img/dhs_t6_2.png" alt="Drawing" style="width: 690px;"/> </td>

#### Social network Analysis visualization

I've started doing computational social network analysis for a while, recently I helped with one project on the flow of officials from different positions in China with policy reform.

Here is one visualization result conducted in Gephi.

<td> <img src="../img/proj-100city.png" alt="Drawing" style="width: 670px;"/> </td>

Here is the micro-scope plot:

<td> <img src="../img/proj-2.png" alt="Drawing" style="width: 590px;"/> </td>

The visualization result clearly presents the significant difference of policy attitudes among different geolocations.

####  Energy Insecurity Instrument Scaling

For the past year I’ve also worked with Professor Hernandéz on developing a robust scale for quantifying Energy Insecurity (EI) based on the original 54-item instrument. By applying the dimension reduction techniques, I successfully applied the PCA analysis and multidimensional Rasch model to successfully validate the 29-item structure, which not only provides the measurement tool for EI, but also complements a data-driven conceptual framework for the 3-dimensions scheme.

<td> <img src="../img/wright.jpg" alt="Drawing" style="width: 570px;"/> </td>

For assessing Energy Insecurity, a shorter-version 29-item instrument from the original 54-item HEII is developed, and validated its multidimensionality in clinical settings using Classical Test Theory and Rasch model analysis. Items are screened before using the psychometrical statistics, then filtered 32 items respectively enter the three models: unidimensional, 3-dimension and 7-dimension Rasch models, together with a contrast of 7-dimension consecutive analysis. Final scale is established on item statistics and conceptual fit. Consistency and reliability of scale are validated.

<img src= "/img/Data_science.jpg" style="width:245px; height:89px;">

### Statistics & Quantative Methods

#### Top R packages

* [Rcpp](http://adv-r.had.co.nz/Rcpp.html), provides a combination of R and C++.
* [stringr](https://cran.r-project.org/web/packages/stringr/vignettes/stringr.html), extremely useful for text mining.
* [ggplot](https://www.mailman.columbia.edu/sites/default/files/media/fdawg_ggplot2.html), a well-known package for data visualization.
* [Table 1](https://cran.r-project.org/web/packages/table1/vignettes/table1-examples.html), extremely useful for organizing tables for publish on journals.
* [TAM](https://www.edmeasurementsurveys.com/TAM/Tutorials/), written by authors of ConQuest, which is a popular software for fitting Rasch model, partial credit model and its extended multidimensional models.

#### Computational resources

* [Five Thirty Eight](https://fivethirtyeight.com/) for political data visualization hosted by ABC news.
* [Introduction to Educational and Psychological Measurement Using R](https://www.thetaminusb.com/intro-measurement-r/) a hands-on book introducing SEM, factor analysis techniques by using R.
* [Working Group on Computational Social Science @Columbia](http://css.iserp.columbia.edu/)
* [Generalized Linear models](https://data.princeton.edu/wws509/sets)Statistical Models: Most popular model in sociology, log-linear model.
* [2019 Summer Institutes for Computational Social Science](https://compsocialscience.github.io/summer-institute/2019/) Cool workshop held multi-centered by scholars and researchers from political science, sociology, psychology and other social science departments. Great resources for fans of computational methods.

#### Blogs and online books

* [Matthew Salganik](http://www.princeton.edu/~mjs3/)
* [Yihui Xie's Blog](https://yihui.name/)
* [Text Mining](https://github.com/dgrtwo/tidy-text-mining)
* [R Markdown Fixes](https://docs.google.com/document/d/1P7IyZ4On9OlrCOhygFxjC7XhQqyw8OludwChz-uFd_o/edit)
* [Word count add-in](https://github.com/benmarwick/wordcountaddin)
* [Quantative Economics Notes](https://notes.quantecon.org/)


#### Sociology Journal

* [The American Sociological Review](https://journals.sagepub.com/home/asr)
* [The American Journal of Sociology](https://www.journals.uchicago.edu/toc/ajs/current)
* [Social Forces](https://academic.oup.com/sf/issue)
* [Social Networks](https://www.journals.elsevier.com/social-networks)
* [Peers at work](https://eml.berkeley.edu/~moretti/text20.pdf)

A regular review of popular journals is a nice inspiration and refreshment.

#### Editing and writing Templates

* [LaTeX Templates and Styles](https://github.com/kjhealy/latex-custom-kjh)
* [Resume Format](http://kjhealy.github.io/kjh-vita/)
* [Pandoc Templates](https://github.com/kjhealy/pandoc-templates)
* [Beamer](http://web.mit.edu/rsi/www/pdfs/beamer-tutorial.pdf) is a powerful and flexible $LaTeX$ class to create great looking presentations.
