---
layout: post
title: Sharing
author: Shan J.
subtitle:
mathjax: true
header-img: "img/head_1.jpg"
date: 2023-02-26 10:32:24.000000000 +09:00
tags:
    - PM side notes
    - Trust and Safety
---

Here are some of my pick-up from my past PM life in tech industry, as most of the time, I use Chinese and English simultaneously to cater the needs of such giant cross-border organizations. Thus, I would like to log down some useful tips.

### 1. Communication ｜ 跨文化交际
Coffee chats may seem easy for PM, however, I never think it is easy for approaching people from a totally different culture.


#### 1.1 Chinese Internet Industry Phrases 101 | 中文互联网PM职业环境表达101
How can I localize Transitioning words in Virtual meetings?
These frequently used phrases can help Chinese PMs to talk more smoothly.  

- 拎一下: Lead something/ take ownership of something
- 碰一下: touch base with sb on sth
- 做会议记录: take meeting minutes; I was jotting down some important highlights
- 插一嘴: Let me chime in here
- 点名同事回答下: Sorry to put you on the spotlight; Sorry to call you out
- 总结一下: Let's call it a day
- 不太难/很容易: it's a walk in the park
- 突然想到的: off the cuff thoughts 

### 2. Master Distraction | 项目时间管理术
Project management is being used and heard in so many places. I cannot remember how many times I saw the title `Scrum Master` on LinkedIn. Indeed, different organizations lean on their own methodologies to help grow their business. No matter what type of methodology you are using: Scrum, Kanban and Agile, always find the good fit should not be errant.

#### 2.0 Methods - Agile Framework

Agile represents an overarching philosophy for software development, emphasizing the value of iterating quickly and often to satisfy customers. An agile framework can be defined as a specific software-development approach based on the agile philosophy articulated in the [Agile Manifesto](https://agilemanifesto.org/).

I love what is defined in [Debian rules](https://www.debian.org/code_of_conduct.zh-cn.html).


#### 2.1 定期清理消息

公司内部沟通的时候，因为节奏快，喜欢DM类型的直接私信，而不是邮件沟通，因此我会时刻保持对于消息的alert，但是这样既耗时，也容易分散精力，之前和supervisor交流过这个问题，没有得到很好的解答，但是最近在一个研发小哥的working log中看到了一种可能的解法：
* 定下固定的时间窗口，清理Lark聊天软件上的记录；
* 定下focus mind专心画图/写文档的slot

#### 2.2 给出问题选项，少问开放性问题

开放性问题在庞大机构和组织里简直就是个灾难，作为底层打工人而言，直接给supervisor选项，并能阐明pros & cons, 会比直接问出开放性问题得到更加有效的反馈。

#### 2.3 黑白选项

Instead of giving the black/white options for a product solution, a bearable minimum product design is always a good start if you need to buy in multiple stakeholders.  

#### 2.4 降低预期
穷举选项给用户不一定是一件好事，因为设计者常常站在自己的角度在给使用者挖坑。
产品设计的精细化和精密仪器设计不一致，在bug常有的创业公司，不要给自己预设很多心理防线。


### 3. Writing | PM写作之术

### 3.1 How to write Roadmap?

#### Section 1: Mission Statement & Vision Statement

To write the roadmap for my work, I need some big visions, so here I collected some of the most well-known tech companies' mission statement for a better reference.

````SQL
1. Google’s corporate mission is “to organize the world’s information and make it universally accessible and useful.”
2. Google’s corporate vision is “to provide access to the world’s information in one click.”
3. Facebook mission statement is “to give people the power to share and make the world more open and connected.”
4. Facebook vision statement is “People use Facebook to stay connected with friends and family, to discover what’s going on in the world, and to share and express what matters to them.”
````
The purpose of this section is to make sure all are aligned to the same mission.

#### Section 2: Milestones in Each Phase

#### Section 3: Resource planning & Timeline
Engineering source planning
Prioritize the right features from the begining.

Kick off from the MVP version.

### 3.2 How to write a PRD?

### 3.2.1 Context(Business & Product)| 商业背景和产品上下文

### 3.2.3 Indicators/Metrics | 常用指标

##### E-commerce:
1. **Bounce rate** is calculated by the total number of one-page visits divided by the total number of entries to a website.
* As a good rule of thumb, the bounce rate rambles under 40%. Between 40% and 55% is usually okay.
2. **CTR*CR**: Click-through rate and order conversion rate, which is used for measuing how efficient the traffic can be turned into actual orders.

##### Content:
1. **Short-term Engagement Metrics**: Playtime/U, Play/U and DAU.


### 4. Product ROI validation

ROI高不高往往是决定产品feature是否能够上线的重要因素。但是如何衡量收益呢？在工业界的验证也是通过实验的方法，拿到真实世界的用户数据反馈，在不断的迭代中，往前推进。

#### Evaluation Methods

##### 1. `Canary Deployment`
A canary deployment, or canary release, is a deployment pattern that allows you to roll out new code/features to a subset of users as an initial test.

Fun fact: This technique is called `“canary” releasing` is because just like canaries that were once used in coal mining to alert miners when toxic gases reached dangerous levels, a small set of end users selected for testing act as the canaries and are used to provide an early warning

##### 2. `BlueGreen Deployment`
Blue-green release means keeping the old version, deploying the new version then testing for problems, then switching the traffic to the new version.

The process is generally as follows:
* Step 1: Deploy version 1 of the application (initial state). All external traffic requests will go to this version.
* Step 2: Deploy version 2 of the application. The code for version 2 is different from version 1 (new features, bug fixes, and so on).
* Step 3: Switch traffic from version 1 to version 2, that is, v1:v2 traffic goes from 100:0 to 0:100.
* Step 4: If there is a problem with version 2, you need to roll back to version 1, v1:v2 traffic is switched back to 100:0.

##### 3. `A/B Testing`
This is frequently used in search & recommendation feature validation. Traffic distribution, AA sanity check are always necessary to keep the experiment fair enough to be trusted.
