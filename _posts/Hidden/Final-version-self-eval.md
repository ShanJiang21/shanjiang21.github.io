#### 内容分级项目（合作者: Tracy Elizabeth & Steve Pin & Sitong Yang & many people I owe credit to）

1. 脏话标签模型侧落地，本土化和产品化：协助脏话标签策略在产品侧与feature policy的沟通，在模型侧后端落地脏话标签策略，推动数据结构的改造，提升策略有效性。（合作者: Tracy Elizabeth & Steve Pin）
2. 协助A/B实验设计，数据指标确定，产品影响面分析和沟通：进行了四个阶段的A/B实验设计，帮助观察核心指标变化，历时5个月, 完成了四轮A/B测试和影响面验证。（**合作者:** Sitong Yang)
3. 沟通各部门诉求和项目执行推动：项目上线的过程中及时高效地保障了需求上线；在TikTok主模式，在欧盟和东南亚地区，美国，澳大利亚，爱尔兰，英国共计31个市场，实现了脏话标签过滤策略的全量上线；收益：策略上线后，生产侧每天 6.08%的视频被标签识别，用户消费侧7.98%的内容被策略过滤，同时，此策略对于用户的留存和活跃指标未造成显著负向影响。（合作者: Tracy Elizabeth & Steve Pin &sitong Yang）
4. 在模型侧，完成Brand Safety CV 模型的调研，主动探索饮酒/吸烟模型单独部署FYF的可能性，完成模型抽样case数据准备和SOP整合。
5. 协助Push侧对于脏话标签策略的早期调研，数据提取，产品策略设计和验证。


#### SDS平台建设 （合作者: Xinchen Zhao, Kunlun Cao and Zichao Wang and Eddie Wang)

1. 【平台建设】制定高危消重产品愿景，规划产品分阶段路线图，设定项目里程碑，把控平台开发节奏。
2. 【平台横向业务能力拓展】收集用户需求，进行业务线拓展：梳理用户资料、短视频、直播和音频审核流程各业务线，抽象跨业务线的平台基础通用能力。
3. 【平台纵向功能设计】主导SDS平台的产品原型和功能设计：
   1. 新增舆情发掘-回扫能力，整合线上高危消重视频模型和embedding模型能力，支持对于线上舆情的应对。
   2. 新增哈希库存储能力和匹配能力支持：NCMEC NGO和行业数据库接入和匹配，KCC项目视频侧进审沟通和产品方案落地。
4. 【业务导向落地和运营】站内工具能力集成, 丰富并优化高危内容来源，建立**高危库梯度分类体系**和标签策略应用体系，建立**高危库种子回查和检索功能**，增加特定种子引起的队列增量**报警通知功能**


#### 高危消重视频全流程优化 (合作者：AI-Lab 北京消重同学，yangyu Chen & ruiqi lu）

1. 【高危消重短视频业务线模型能力优化】与AI-Lab合作，进行高危消重视频模型的优化，在海外TikTok短视频业务线，推动深度学习新模型7月份全量上线，队列审出率从24%提升到最高45%，目前稳定在36.71%左右。
2. 【海外高危消重视频模型训练流程建设】主导发起高危消重视频模型训练集建设，建立了贴合业务的模型标注标准和稳定的标注流程，提高了模型对于badcase的召回能力。
3. 【二次标注全流程重构】二次标注policy的4.0对齐，重新梳理和确认二次标注来源，沟通剪辑标注模板需求和PMS新版、
4. 【局部消重模型建设】从零到一建设单帧全局，单帧局部消重模型和消重库，完成模型上线的法务评估流程和运营工作，有效支持线上色情问题的画中画内容风险。


#### 视觉模型和文本模型优化

1. 探索公司内舆情处理能力，与AI- Lab共同完成搜索词文本模型聚类需求（合作者：Chen Zhu 同学）
2. 提需AI-lab新加坡团队，为应对美国Mass shooting舆情进行紧急法务评估，进行3D打印枪支模型的训练和上线。（合作者：Hu Jie & Logan Zuo 同学）
3. 及时发现线上舆情风险，发起饮食失调视觉模型(Eating_disorder model) 训练需求，在德国上线。
4. 识别VGC领域中电影，动画和电子游戏中血腥暴力画面，发起Animated violence模型需求，模型在8月底已上线。（合作者：Siyao Zhang & Logan Zuo）


#### 音频模型优化

1. 在TikTok音频审核业务上，推动了高危消重音频模型全量上线，增加了静音检测功能，日均减少无效进审量8700+，审出率从 0.56%提高至3.42%（with Zhu Bilei & Mingyu Liu)
2. 语种分流模型能力调研和文档总结，向AI-Lab进行语种分流模型(LID模型)的提需和训练数据准备。
3. 在全球上线ASR-EN 模型匹配色情敏感词自动下架策略，建立模型和敏感词效果评估。（合作者：Wenchao Zheng ）
4. 协同OPS确定音频/视频侧拆分队列计划，解决重点国家音频队列的审核人力错配问题。（合作者：Leason Shi ）
5. 新建涉恐/仇恨言论歌曲库入库流程，上线命中高危消重音频模型自动下架策略, 月级别自动下架音频数量为3,350。（合作者：Darwn  Rahim & Zhongqiang Liu）
6. 统筹短视频和直播业务的ASR模型的上线规划，为AI-Lab模型训练和机器资源部署提供支持（合作者：Wenchao Zheng ）
7. 协助音频初审召回Gandalf模型的上线，ASR模型在俄罗斯和孟加拉国的迭代（合作者：Wenchao Zheng ）。


#### 流程建设和知识沉淀

1. 【流程建设】搭建了一套完整的与Issue PNP/policy，Feature policy，Lab合作的机制，建立了Model PNP日常提需的流程；
2. 【为新入职同学提供支持和指导】帮助新入职两位同学熟悉模型侧沟通方法，数据分析手段，模型效果评估和提需流程；并完成了组织架构、业务知识、基础方法和文档写作等技能的培训。

------------------------------------------------------------<EN Shown Below>---------------------------------------------------------



#### CONTENT CLASSIFICATION and PROFANITY Filter Models（Thanks to Tracy Elizabeth & Steve Pin & Sitong Yang & Many people I owe credit to）

1. 【POLICY LANDING IN MODEL】 Profanity Policy model landing and localization: Build strategic relationships with global and cross-functional Policy partners to drive improvements to the content classification framework; provided robust evaluation AND model landing strategy design on back-end, re-structured the data stroage and promoted the successful integration of the strategy with current moderation pipeline.（w/: Tracy Elizabeth）

2. 【DATA-DRIVEN PRODUCTIZATION】 Coordinated the set-up of A/B experiment design, confirmed the core performance metrics for the strategy and impact of the whole product：In total, we conducted 4 phases of A/B testing on FYF page for validating the potential effect on user engagement and retention over more than 5 months。（w/: Sitong Yang)

3. 【COORDINATION XFN TEAMS】Cementing the connections of recommendation-side engineers, PMs and TNS-side PMs, identified the launch criteria and road-blockers. 

4. 【SOFT LAUNCH IN EU/SEA/EN-MAIN COUNTRIES】 Finally promoted the successful launch of profanity filter on TikTok For You Feed Page(Main mode) in 31 markets that cover European, South East Asia, United States, Australia, Ireland and United Kingdom. It is monitored on production end  6.08% videos are labelled by this strategy and around 7.98% videos are filtered on consumption end. Luckily there is no significant negative impact observed on engagemnt and retention metrics meanwhile.（w/: Tracy Elizabeth & Steve Pin & Sitong Yang ）

5. 【CV MODEL due diligence check】 On Model side, carried out the due diligence check of existing CV models and proactively explored the drinking, smoking and drugging models for mitigating susbstance abuse risks, prepared the model performance metrics, sampled cases and labelling policy for a realignment that can cater to Content Classification design on For You Feed page. 

6. 【USR  STORIES COLLECTION 】Consulted with UR team to develop a questionnaire for informing the decision-making process on whether to make the maturity tagging mandate or optional for users and evalute the expectation of users on the product strategy. 

7. Helped the early research and validation form Push-side PMs for profanity strategy. 

  

#### SDS PLATFORM Construction （Thanks to Xinchen Zhao, Kunlun Cao and Zichao Wang and Eddie Wang）

1. 【[Platform Productization】Setting the product vision and initiate the roadmap for similarity matching model services and banks. Navigating the milestones for projects and carry out the project management for an agile development.

2. 【Integrating business needs with Platform development】Collecting user stories, and expanding lines of business, Realizing an efficient and flexible configuration of different business lines, including user profile, short-videos, livestream and audio moderation process.

3. 【Fundamental Services design】Played a dominant role for prototype and feature design:
   3.1. Build a retracing and retroaction tab for providing an enhanced capability of identifying risks in historical posts, which is a strong booster for reacting to incidents/crisis management.
   3.2. Compiled a general cross-functional support for hashing value storage and matching: including NCMEC NGO and Industry database construction, KCC illegal recordings matching and so on. 

4. 【Operational functions landing】New feature release: Catalogued content management, seed content search and tracking, early earning and data monitoring, seed content life cycle management, permission control and clipping tools development. 



#### High-risk Deduplication VIDEO MODEL and workflow Optimization （Thanks to AI-Lab Deduplication Team, Ruiqi Lu & Yangyu Chen)

1. 【Enhance high-risk deduplication ML video model】Keeping a close coorpertion with AI-Lab, carried out the optimization of video models in short-video business line. Promoted the full-launch of novel high-risk deduplication video model in July, enabling the violation rate lifted from 24% to around 36.71%.

2. 【Buidling up the training dataset for video high-risk deduplication ML video model】Leading the build-up for building the training dataset for high-risk deduplication ML video model, and constructed a stable labelling workflow, increased the recall for commonly-seen badcases. 

3. 【Revamping for incident labelling workflow】Mapping the incident labelling policy with 4.0 video moderation policy, and signed it off globally. RE-Defining the sources of incident labelling cases, revamping the labelling and clipping template, and configuring a new PMS template.

4. 【Localized deduplication model build-up】Completed the compliance review and set-up of localized dedeplication model and banks, setting the clipping SOP and launched the model in 4 countries. Provided effective support for tackling frame in frame issues in video moderation pipeline.  

   

#### PAKISTAN PROJECT

1. Added a shunting button for moderation template for round-2 video moderation queues, reduced the leakages induced by language challenges, the precision of the strategy is 92%.
2. Brought the Pakistan Urdu model for audio moderation pipeline with full traffic, uplifting the violation rate from 2% to 15%.(With Wenchao Zheng)
3. Conducted due diligence check on a text-based model for language shunting via characters identified in video frames with AI-Lab : we examined the alphabet table and researched the local linguistic environment. (With Chen Zhu & Jie Wang)



#### AUDIO MODEL OPTIMIZATION

1. Promoted the high-risk deduplication audio model to launch with 100% traffic. Added voice activity detection strategy for this model, which reduced the inefficient 8,700 enqueued cases and increased the violation rate from 0.56% to 3.42%.(with Zhu Bilei & Mingyu Liu)

2. Researched the available language shunting models across ByteDance and documented the conclusion for knowleage transfer for Issue-PNPs. 

3. Raised the Lanuage Identification Model(LID) model training request to AI-Lab acoustic team and prepared the training dataset in the format of audio clips, making it a great support for Pakistan and Turkish by the end of August. 

4. Launched the ASR-EN model globally for removing ANSA-spam related audios, build up the whole word corpus and evaluated the impact of sensitive keywords. (With Wenchao Zheng）

5. Established an auto-removal strategy for VE and Hate-speech songs stocked in high-risk library, it is observed that 3,350 audio cases are taken down on average monthly (Up to date)

6. Made a planner for ASR models to be launched for short video and LiveStream Business lines, replaced Google ASR services with Inhouse ASR models in Russia, Pakistan and Bangladesh.

7. Assisted in the launch of audio-Gandalf model in US and RU, with US enqueue volume will be decreased by 60%, violation rate will be increased by 140%.


#### Embedding VISUAL MODELS in Video moderation pipeline 

1. Analyzing typical characteristics and providing solutions for common features of badcases feedback by Issue PNP; ( with GPIOs)
2. Raised Animated Model training request to productize Visual models for moderation (with AI-Lab Singapore-Computer vision Team Logan Zuo) 
3. Identify loopholes in moderation pipeline, applied Machine-learning-powered productization on TikTok Short Video Business Lines via building Eating Disorder models and the regular iteration of visual models. (With Bingni Zhang and her team)
4. Offered Immediate response to US Safety team by localized iteration of weapon model for dealing with the 3D-printed guns and bullets issues. (With Logan Zuo)
5. Coordinating with Video Level Model Compliance review and model precision/recall evaluation 


#### Knowledge Management and Skills Transfer 

1. 【Oversee various issue verticals, product lines, and ML processes】Established a comprehensive workflow for more efficient communication and cooperation with Issue PNP/policy, Feature policy and established a daily request  process for Model PNP; (With Bingni Zhang and her team)

2. 【Mentorship for new onboarders】Familiarize new fellows with ByteDance Feature-PNP domain knowledge.That includes machine learning concepts, basic AI concepts, and data science fundamentals. Help them to gain more understanding to evaluate data, ask the right questions about said data, and more.