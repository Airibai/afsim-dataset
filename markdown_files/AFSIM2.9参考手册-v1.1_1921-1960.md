scenarios/red_air_support.txt   
DISTRIBUON C. Distribution authorized to U.S. Government Agencies and their contractors, 9 Aug 19. Other requests for this document shall be referred to AFRL/RQQD 15   
```txt
74 platform escort_south RED_STRIKER   
76 side red   
77 icon weasel   
78 command_chain red_chain ship_lead   
79 route   
81 position 29:33:57.54n 80:08:06.19w altitude 35000 ft msl   
82 speed 450 kts   
83 position 29:46:00.17n 80:36:37.58w altitude 35000 ft msl   
84 end-route   
85 NOTE: added north AND south escorts!!!   
86 heading 250 deg   
87 edit processor task_mgr   
89 edit behavior escort   
90 script_variables   
91 mDrawEscortData = true;   
92 mEscortNames[0] = "soj_south";   
93 mFormationPositionX = 0; // meters in front of of package   
94 mFormationPositionY = -5*1852; // meters off right wing of package   
95 mEscortProtectDistance = 60 * MATH.M_PER_NM();   
96 mWeaponRangeToInclude = 0;   
97 mEscortChaseDistance = 5 * MATH.M_PER_NM();   
98 end scripted_variables   
99 end_behavior   
100 end Processor   
101 endplatform 
```

![](images/aead2459af7e8f03b85d5b5753c62ba16a9bd2d62abc86286a02fc5c2d8f2bac.jpg)

# UNCLASSIFIED

# 红色控制器

![](images/72c65383968df90bbc9ee588f44216ce05267ef51c78a4039231054e97b9e623.jpg)

platforms/ship.txt   
```txt
platforms/ship.txt
1
2 include_ once processors/quantum_agenta/aif1/f1_quantum_tasker_verysimple.txt
3
4 # note: this JAMMER_LEAD_TASKER processor is only useful when on a
5 # commander platform that commands over SOJ type platforms
6 
```

DISTRIBUON C. Distribution authorized to U.S. Government Agencies and their contractors, 9 Aug 19. Other requests for this document shall be referred to AFRL/RQQD   
```txt
109 comm red_comm TEAM_DATALINK   
111 network_name red_net   
112 internal_link data_mgr   
113 internal_link task_mgr   
114 internal_link perception   
115 internal_link jammer_tasker   
116 end_comm   
117   
118 processor task_mgr FL_QUANTUM_TASKER   
119 end Processor   
120 
```

RUN IT!!!

现在红色干扰机有护航了

DISTRIBUION C. Distribution authorized to U.S. Government Agencies and their contractors, 9 Aug 19. Other requests for this document shall be referred to AFRL/RQQD

![](images/a1ebd63307f93087160dc84d1f584ea49d0d20215d4ecb1b92b79e6e55a7af39.jpg)

# UNCLASSIFIED

# 红方护航机

![](images/c46b716c5003c4c87852f203df6aa0fb8956fa4156aed8b95cf548b94f51d35f.jpg)

![](images/7f9e7c4aad034686660bac54f526f83c130cecbf09f03ea6c2ee1f5de48ad0d4.jpg)

DISTRIBUON C. Distribution authorized to U.S. Government Agencies and their contractors, 9 Aug 19. Other requests for this document shall be referred to AFRL/RQQD 18

![](images/58956fdc7cd5ded4620c90dc7b7b1b355bc64de6d7921f4268b4fb36f9312e78.jpg)

DISTRIBUON C. Distribution authorized to U.S. Government Agencies and their contractors, 9 Aug 19. Other requests for this document shall be referred to AFRL/RQDD

# 6.1.10.6.威胁处理器和规避行为26_AFSIM_BAM_Trng,ThreatProcessor

# 6.1.10.6.1. 本节想定解析

本节想定资源在以下目录下：

afsim2.9_src\training\user\10_Other_Topics\bam\scenes\floridistan\26_FLORIDIAN_evade\run_coarse.txt,

行为与智能体建模培训的每一节都是在上一节的基础上的，而且想定较为复杂，因此要先了解上一节的内容。本节是在上一节的基础上给红方新增了两架战机，其感知威胁后会做规避动作，但是其实没有什么用，导弹的速度很快，一旦锁定通过机动来逃生的概率不大：

![](images/233ee9cf239f2c72096f99396921976b59c9261a900b5e1226eabf16455ba7f6.jpg)

# 6.1.10.6.2. 本节PPT资料

本文为afsim2.9_src\training\user\10_Other_Topics\bam\slides\26_AFSIM_BAM_Trng_ThreatProcessor.pptx的翻译。

![](images/92a0f59c06beaa2ef9aa05db61c02eedc953df9d39247e64019356b5cead82bf.jpg)

UNCLASSIFIED

![](images/d427b0b744542569ede45b06e359d37612562d7706e0e29e0f9e202ec7d60c51.jpg)

![](images/46d2b8504e2d2468fae3290cfefdee58c9d825b14ad35fd619f54e962d83e816.jpg)

# AFSIM用户培训26-威胁处理器&规避行为

本文档由杨石兴翻译，该资料做为《AFSIM2.9参考手册》的一部分。没有《AFSIM2.9参考手册》的加杨石兴微信领取：13324598743

Integrity ★ Service ★ Excellence

AFRL/RQQD

美国空军研究实验室

DISTRUBION C. Distribution authorized to U.S. Government Agencies and their contractors, 9 Aug 19. Other requests for this document shall be referred to AFRL/RQQD

![](images/0d8f87217e12d12e223e3386504ed552f52b9fa780009be122e32277ae82b995.jpg)

UNCLASSIFIED

规避行为

![](images/884eb212867cf62e9e873cb788afc01761c5f155eda33993306afd9128980090.jpg)

![](images/5affdff53119ea47713434e71153f7b1e0ee4e2bcf552afee5f1ec8e2f0712e9.jpg)

DISTRIBUON C. Distribution authorized to U.S. Government Agencies and their contractors, 9 Aug 19. Other requests for this document shall be referred to AFRL/RQDD

# - 理论

规避的考虑因素  
- 累积向量数学逃逸   
- 考虑僚机的情况  
- 永远不要帮助威胁引导你

# - 应用

- 为攻击者（striker）添加WSF-threatPROCESSOR  
- 为攻击者添加规避行为

![](images/02780281536b073f376a94cb5911d520ba6dfd916e6cbd904ec9d88a90293dd3.jpg)

DISTRUBION C. Distribution authorized to U.S. Government Agencies and their contractors, 9 Aug 19. Other requests for this document shall be referred to AFRL/RQDD

3

![](images/a95a5be322fd87585eeb73c1d6b2155009753100b95ee7456ffe7c0ffb319749.jpg)

# UNCLASSIFIED

# 威胁处理器

![](images/ee89c454f424ceba43b2e31151657ac7d565ca4b77c8c74bad21de6e645ebbf0.jpg)

- 规避行为查找威胁处理器 WSF-threatPROCESSOR

- 威胁分类依据：

![](images/8f759308d1b316574c1c135e8a035e232385a9dedfdd261dc0b729937a05750b.jpg)

DISTRUBION C. Distribution authorized to U.S. Government Agencies and their contractors, 9 Aug 19. Other requests for this document shall be referred to AFRL/RQQD

- 更近的威胁权重更高  
- 可以选择为盟友赋予权重  
- 向量之和决定方向  
- 优先原则：

- 永远不要帮助最近的威胁引导你

![](images/4c4145a5c2c6ea62f8a7c153e6dc0776919d5b43ce27d3518aa5ccac01e36b53.jpg)

DISTRIBUON C. Distribution authorized to U.S. Government Agencies and their contractors, 9 Aug 19. Other requests for this document shall be referred to AFRL/RQDD 5

5

![](images/e5c424c244b29f6880e86d2b01fed9014931c8e44f85fef8ec8a6086b2f07026.jpg)

# UNCLASSIFIED

# 添加规避行为

![](images/5fdfc3faef265895ab53c9f7b4be3277a23abfb764bed5500908a04b6cf03a0d.jpg)

# platforms/striker.txt

```txt
4 include_once processors/quantum_agenta/aiai/behavior_agengage weaponry_task_target.txt 5 include_once processors/quantum_agenta/aiai/behaviorEscort.txt 6 include_once processors/quantum_agenta/aiai/behavior Escort.txt 7 include_once processors/quantum_agenta/aiai/behavior_evade.txt 8 include_once processors/quantum_agenta/aiai/behavior_go_home.txt 9 include_once processors/quantum_agenta/aiai/behavior_planned-route.txt 10 include_once processors/quantum_agenta/aiai/behavior_pursue-target-routefinder.txt 11 include_once processors/quantum_agenta/aiai/behavior_pursue weaponry_task_target.txt 12 
```

```txt
67 processor task_mgr WSF_QUANTUM_TASKERPROCESSOR  
68 scriptDebugWrites off  
69 update_interval 5 sec  
70 behavior_tree  
71 selector  
72 behavior_node evade  
73 behavior_node go_home  
74 behavior_node escort 
```

DISTRIBUON C. Distribution authorized to U.S. Government Agencies and their contractors, 9 Aug 19. Other requests for this document shall be referred to AFRL/RQQD

# 规避行为参数举例

- 所有参数都与确定威胁和执行规避机动有关。

# -- debug parameters

- bool mDrawNearestThreat = false;   
- bool mDrawEvasionVector = true;

# - control parameters

double weightPeersForEvade = 0.25;   
- bool mWobbleLeftRight = true;   
- bool mWobbleUpDown = true;

# - flying parameters

double mAltitudeMin = 1000.0;   
double mAltitudeMax = 20000.0;   
double mBankAngleForEvading = 45.0;

# off-limit variables (not for user editing)

- double mLastTime;   
.   
- bool mDiveDownFlag;   
- bool mBankLeftFlag;

DISTRUBION C. Distribution authorized to U.S. Government Agencies and their contractors, 9 Aug 19. Other requests for this document shall be referred to AFRL/RQQD

![](images/4a3859fd2ad9c3c539d542d19c71abe6d8e252d06757bf5f76e3a0e79acd8f7e.jpg)

# UNCLASSIFIED

# 规避行为

![](images/4361bc0f27db60c5f7de66457f15e3cae22403cd0bf60eee0f29688c5070c5af.jpg)

processors/quantum_agentaiai/behavior_evade.txt   
behavior evade   
script-debugWrites off   
script_variables   
double cDEFAULT_ALTITUDE = 9144; // ~30,000 feet   
double mEngagementAggressiveness $= 0.4$ ; // value in range [0, 1]. 1 i // used by behavior_in Danger,   
//**********   
bool mDrawNearestThreat = false;   
bool mDrawEvasionVector = false;   
//**********   
double weightPeersForEvade $= 0.25$ ; //percentage to scale peers influ   
bool mWobbleLeftRight = true;   
bool mWobbleUpDown = true;   
double cFAST_UPDATE_intervalVAL $= 0.25$ .   
double cSLOW_UPDATE_intervalVAL $= 2.0$ .   
//**********   
//** flying parameters, for for evasive maneuvering   
//**********   
double cNORMAL SPEED $= 200.0$ ; // m/s

DISTRIBUON C. Distribution authorized to U.S. Government Agencies and their contractors, 9 Aug 19. Other requests for this document shall be referred to AFRL/RQQD

platforms/stiker.txt

```txt
82 processor incoming-threats WSF-threatPROCESSOR   
84 update_interval 1 sec   
85 threat_velocity 1300 knots   
86 threat_anglepread 20.0 deg   
87 threat_time_to_intercept 30 sec //60 sec   
88 end Processor   
89 
```

DISTRIBUON C. Distribution authorized to U.S. Government Agencies and their contractors, 9 Aug 19. Other requests for this document shall be referred to AFRL/RQQD

![](images/076682928a2f4ad8cc9993e1f5bd8fac8619119b288528fa98a96ab31ba2013d.jpg)

# UNCLASSIFIED

# 新的飞机

![](images/0b747aeecf28fc839947bdb63c4cc926425842ef894b0ac3f13a2b70fdad41d1.jpg)

Scenarios/red_air_support.txt

```txt
115   
116 #   
117 # Fighter Support   
118 #   
119   
120 platfornleft_flanker_1 STRIKER   
121 side red   
122 icon weasel   
123 commander ship_lead   
124 route   
125 position 29:39n 79:49w altitude 35000 ft msl speed 450 kts   
126 position 30:20n 81:32w altitude 35000 ft msl speed 450 kts   
127 end route   
128 heading 292 deg   
129 end platform   
130   
131 platfornleft_flanker_2 STRIKER   
132 side red   
133 icon weasel   
134 commander ship_lead   
135 route   
136 position 29:43n 79:48w altitude 35000.00 ft msl speed 450 kts   
137 position 30:23n 81:31w altitude 35000.00 ft msl speed 450 kts   
138 end route   
139 heading 292 deg   
140 end platform NOTE: also moved other platforms   
141 
```

DISTRIBUON C. Distribution authorized to U.S. Government Agencies and their contractors, 9 Aug 19. Other requests for this document shall be referred to AFRL/RQQD 10

RUN IT!!!

新的战机规避

DISTRIBUION C. Distribution authorized to U.S. Government Agencies and their contractors, 9 Aug 19. Other requests for this document shall be referred to AFRL/RQQD

![](images/1b9322320ce187b75a1d6c6ccd0721f4ae9384e915bb85df09ba32112e3d2501.jpg)

# UNCLASSIFIED

# 红的战机躲避导弹

![](images/5b8f443882318a948d0b11d0f8a225bede9216d507513066c61ff418902b8fa4.jpg)

![](images/3ce2e932a96d94d270b452a2ab5cf82b89a7030b6a2e6079978d0ee39aeb9ca9.jpg)

DISTRIBUON C. Distribution authorized to U.S. Government Agencies and their contractors, 9 Aug 19. Other requests for this document shall be referred to AFRL/RQQD

编辑参数以更改平台的动作。

- 可以修改威胁处理器或规避行为中的数值。  
针对平台的特定情况进行更改。

- 运行场景以确认更改是否生效。

具体尝试：

- 让南部的红方战斗机继续前进，而南部的SOJ护航机逃离。  
- 改变蓝方和红方战斗机之间的相对攻击性。

提示：

- 将更改限制在特定平台实例上。

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9 Aug 19. Other requests for this document shall be referred to AFRL/RQQD 13

![](images/4b55c3338c9b5254de89f89fa2066417a0790b398eb5744f48efd90fcb1ec13e.jpg)

DISTRIBUON C. Distribution authorized to U.S. Government Agencies and their contractors, 9 Aug 19. Other requests for this document shall be referred to AFRL/RQQD

# 6.1.10.7. 聚类、C2 和任务分解 27_AFSIM_BAM_Trng_ClusteringC3

# 6.1.10.7.1. 本节想定解析

本节想定资源在以下目录下：

afsim2.9_src\training\user\10_Other_Topics\bam\scenes\floridistan\27_FLORIDIAN_cluster_gci\run_course.txt,

行为与智能体建模培训的每一节都是在上一节的基础上的，而且想定较为复杂，因此要先了解上一节的内容。本节给蓝方的两架飞机指挥所上新增了个指挥所名为地面拦截控制中心（GCI）10_gci_cmdr，其负责对来犯的红方飞机按距离关系进行聚类，聚类完成后将任务进行下发。以下为具体效果：

![](images/651be93fe553f3c6587aa858843e5634665beb2634a206a80b89d503bc38ea2e.jpg)

可以看到紫粉红色的圈就是将其聚类的飞机形成一个任务进行下发。右侧两架是一个聚类，中间四架是一个任务聚类，左边两架是一个任务聚类。

# 6.1.10.7.2. 本节PPT资料

本文为afsim2.9_src\training\user\10_Other_Topics\bam\slides\27_floridistan_cluster_gci.pptx的翻译。

![](images/099ce287e64e96ee9ede1c4d1484f92658d8409295f0cbf2149094a1dd5f5bf9.jpg)

Integrity $\star$ Service $\star$ Excellence

# AFSIM用户培训

# 27- 聚类、C2 和任务分解

本文档由杨石兴翻译，该资料做为《AFSIM2.9参考手册》的一部分。没有《AFSIM2.9参考手册》的加杨石兴微信领取：13324598743

# AFRL/RQQD

# 美国空军研究实验室

DISTRIBUON C. Distribution authorized to U.S. Government Agencies and their contractors, 9 Aug 19. Other requests for this document shall be referred to AFRL/RQQD

1

![](images/ed4138c2787125c62d037cb175e8aa3632f3d31cef5584be5c4694b3bf276b7b.jpg)

# UNCLASSIFIED

# 聚类 & 指挥/控制 (C2)

![](images/c27db5c02c2e8e4443a651f7cc58417680ff499f3e7b7568bc71b5c65e4da343.jpg)

- 理论

- 聚类   
- 代理的层级结构

·应用

- 添加地面控制拦截（GCI）代理

- 用于聚类任务  
- 使用不同的飞行队长原子任务分配器  
- 将聚类任务解释为目标（武器）任务

- 改进指挥官的能力

DISTRIBUON C. Distribution authorized to U.S. Government Agencies and their contractors, 9 Aug 19. Other requests for this document shall be referred to AFRL/RQQD

- GCI 代理处理态势感知（SA）以管理战斗

需要更多关于一组威胁的信息  
- 能够对列表的子集进行推理和决策

- 我们是自动完成的——通过视觉方式（你能看到多少组？）

![](images/3db25f71b9c7ffcbfaab00529dab15649073baaaaf17887d3d2a39dd36cd4f03.jpg)  
DISTRIBUON C. Distribution authorized to U.S. Government Agencies and their contractors, 9 Aug 19. Other requests for this document shall be referred to AFRL/RQQD 3

![](images/3fd71f534a899cce94f4a0e394723f9129ace71976293c0bfd8036aa6e8f9f0c.jpg)

# UNCLASSIFIED

# 平台分组

![](images/724ac960c0d4e7cb72d6493a4b5c62dcbb97777958c821caa345f611e872cf40.jpg)

- 我们是自动完成的——通过视觉方式（你能看到多少组？）

![](images/dfaf8ba0e8fa0093dcb174d56fb02ca295d077fbcb49d7412495721ead314b99.jpg)  
DISTRUBION C. Distribution authorized to U.S. Government Agencies and their contractors, 9 Aug 19. Other requests for this document shall be referred to AFRL/RQQD

- 现有的威胁表示  
- WsfTrackList：传感器能够检测到的所有内容  
- MasterTrackList =

[ blue01,

blue02,

blue03,

blue04,

blue05,

blue06]

没有特定的顺序  
- 整个组的数据？

![](images/4574e7a3bed0254d82c78e7cf1ef41b950cf0385c111d150e906bb5e12112bb1.jpg)

DISTRIBUON C. Distribution authorized to U.S. Government Agencies and their contractors, 9 Aug 19. Other requests for this document shall be referred to AFRL/RQQD 5

![](images/ac50b6b384b53e30ea326577ac39e2ce81401ecb395d927852431aa26dd05e08.jpg)

# UNCLASSIFIED

# 聚类威胁

![](images/281e02b06b87d088caf802cf12cad6f807996ffba5cf666638d2b9439fd30e35.jpg)

- 我们希望看到：  
- 分组“有意义”   
- 对任务分配有用  
- Cluster01=[blue01, blue03, blue04]   
- Cluster02 = [blue02, blue05, blue06]

![](images/eda4e582abd6f732c6d233ec2f071de79ee165ef86aac4bd66e99a6d04f58ba4.jpg)

DISTRIBUON C. Distribution authorized to U.S. Government Agencies and their contractors, 9 Aug 19. Other requests for this document shall be referred to AFRL/RQQD

- 创建聚类对象非常简单:

```txt
WsfClusterManager cManager = WsfClusterManager.Create();  
cManager.setClusterMethod("H.Tree_MAX");  
WsfLocalTrackList MTL = PLATFORM MasterTrackList();  
Array<Array<WsfLocalTrack>> clusters = cManager.GetClusters(MTL);
```

控制它们的创建：

- 设置聚类方法、阈值、聚类数量等……  
- 参阅 WsfClusterManager 的文档

- 使用聚类：

- 访问其成员：Wsftrack Entry(index)  
- 访问其聚合属性：位置、凸包和方位

DISTRIBUON C. Distribution authorized to U.S. Government Agencies and their contractors, 9 Aug 19. Other requests for this document shall be referred to AFRL/RQQD

![](images/d920f2c11391e3e6c0eda1e38ff0df594648f6403a0c89b1295e27bf0561bfa2.jpg)

# UNCLASSIFIED

# K-Means 聚类 (K 均值聚类)

![](images/17e1777a590649011247ff8124e7ed61b4b896101c0b73f8b0c3fbec79e3e8f5.jpg)

# K均值聚类处理方法:

![](images/989c6374b154f030aed6f3f5cc8933be56bd35ead471c0975795936b3ef67d9a.jpg)

- 易于理解；简单的迭代过程；总是能够终止

- 缺点

- 需要提供一种方法来初始化均值（随机初始化？）  
- 最接近某个均值的集合可能为空  
- 不一定能找到最优的聚类配置  
- 我们应该使用多少个均值？“K”应该是多少？

DISTRIBUON C. Distribution authorized to U.S. Government Agencies and their contractors, 9 Aug 19. Other requests for this document shall be referred to AFRL/RQDD

H-Tree 聚类方法的凝聚过程:  
![](images/5a7079d257ae0a64aff7c3cd1a827389895e8d933aa0723d9ca5024d840deeb1.jpg)  
- 优点  
- 容易定义相似性阈值；相似性是相对计算的  
如果需要“K”个聚类，更有可能找到最优配置  
- 缺点  
扩展性较差：时间复杂度为 $O(n^2)$   
DISTRIBUON C. Distribution authorized to U.S. Government Agencies and their contractors, 9 Aug 19. Other requests for this document shall be referred to AFRL/RQQD

![](images/79618a6a6200c1d463916003c3de580f9ae301772421218d7d73d845f50b283d.jpg)  
UNCLASSIFIED

# H-Tree方法

![](images/e6dbcd34e760b494abd2db5c3941500a2171ef799ff85cba435029b2d75b79e5.jpg)

问题：什么与“a”聚类在一起？

![](images/6056107082ab3782e3b90436166d0bf22751ea715d56120dbf1637c069766b27.jpg)  
观察“a”，有哪些其他平台在距离阈值范围内？到此为止！

![](images/d67a9aff65e42f6396afef9aa31457f5c6bbcd4fc4a038c4c648b3ca84c25b96.jpg)  
观察“a”，有哪些其他平台在距离阈值范围内？对这些平台也重复相同的操作！  
DISTRIBUON C. Distribution authorized to U.S. Government Agencies and their contractors, 9 Aug 19. Other requests for this document shall be referred to AFRL/RQQD

![](images/b378efa997a4225883285f7a9666bbcb8f1607fe1c01218033084d026a74009d.jpg)  
H.Tree_MAX

![](images/c73750611331e7235400f3508329fc761a3df9461cca6c5e96cbc7dd835aebcc.jpg)  
H.Tree_MIN

DISTRIBUON C. Distribution authorized to U.S. Government Agencies and their contractors, 9 Aug 19. Other requests for this document shall be referred to AFRL/RQQD 11

![](images/68437ce533948f362544bb19f7f381909bb6fdad95c363b4fe1d4d410550d96c.jpg)

# UNCLASSIFIED

# Interactions

![](images/93861fcf0f274d252e4d319649fcdd5b078d3db250f105a49501cfbf9ec295be.jpg)

用于代理交互的聚类：

- 轨迹（Tracks）会被传递，可能GCI没有本地传感器  
- 资产感知（Asset Perceptions）会被传递  
- GCI 代理创建并分配聚类任务  
- 它使用 WsfClusterManager  
- 在评估时，它使用其下属的下属信息  
- FL 代理将聚类任务解释为武器任务

- 每个聚类成员对应一个武器任务

- 它使用下属信息进行评估

- AI 代理被分配一个武器任务

![](images/65f6378ad76e9fe660f7e06eb0234b6129f078176c1852e6b5b65c714783d321.jpg)

DISTRIBUION C. Distribution authorized to U.S. Government Agencies and their contractors, 9 Aug 19. Other requests for this document shall be referred to AFRL/RQQD

# setup.txt

```c
7 //redcommander   
8 9 include_once platforms/ship.txt   
10 //redSOJ   
11 include_once platforms/soj.txt   
12 //bluecommander   
13 include_once platforms/flight Lead.txt   
14 include_once platforms/gci_cmdr.txt   
15 //air platform (used by blue and red)   
16 include_once platforms/striker.txt   
17 
```

DISTRIBUON C. Distribution authorized to U.S. Government Agencies and their contractors, 9 Aug 19. Other requests for this document shall be referred to AFRL/RQQD 13

13

![](images/dd8bb54446903ef4b15de4efc752daf21d1e603e28da768a538440e7f89868b6.jpg)

# UNCLASSIFIED

# 实例化GCI

![](images/1a82d0602b662369ab31f241973dc55821a8bc32b9c2aff8e3d01491335c5320.jpg)

# scenarios/blue_air_cap.txt

14   
15.1E platform 10_gci_cmdr GCI_CMDR side blue icon runway command_chain blue_chain SELF position 30:15n 82:00w altitude 0 ft agl heading 105 deg   
22.2 edit processor data_mgr report_to_command_chain blue_chain commander via blue_comm report_interval 20 sec fused_track_reporting on raw_track_reporting off endprocessor   
29.6 edit processor task_mgr script_variables mKnownTargetTypes["RED_STRIKER"] $= 1$ .   
31 end.script_variables   
33 end Processor   
34 endplatform

```txt
79   
80 platform flight_lead_north BLUE_FLIGHT_LEAD   
81 side blue   
82 icon Command_Truck   
83 position 30:38:12.770n 81:42:59.042w   
84 heading 100 deg   
85 command_chain blue_chain 10_gci_cmdr   
86 endPlatform   
87 
```

DISTRIBUION C. Distribution authorized to U.S. Government Agencies and their contractors, 9 Aug 19. Other requests for this document shall be referred to AFRL/RQQD 14

# platforms/flight_lead.txt

![](images/326059c42a7a67454a4d7d12d146490d835eb52d1b35e5d37393a0c5dfc1ecf2.jpg)

![](images/90507e311ec922a74374b6fb95bbf270659162e3b39fe0c88a322ad0567adcdb.jpg)

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9 Aug 19. Other requests for this document shall be referred to AFRL/RQQD

15

# UNCLASSIFIED

![](images/f513d56ed6b72e2acaf9f04fe6753ce269b26f9bab47902ba11afbb7036fb865.jpg)

# 船

![](images/88d6431975feb8c26bf0a9a885419473e8d761cbc150c39f3d620f812f3a8640.jpg)

# platforms/ship.txt

![](images/82a618f792da1ecde5859a59828f8154225628909b9a33c4d55a2df2814f0ddb.jpg)

![](images/6fd064534ab80ee95d03f1f7531d6c50c6c8f55e68192d52731efc257b098487.jpg)

突击测试：我可以通过什么方法增强 FL_QUANTUM_TASKER，从而不需要使用“mSelfCreateTasks”变量？

DISTRIBUION C. Distribution authorized to U.S. Government Agencies and their contractors, 9 Aug 19. Other requests for this document shall be referred to AFRL/RQQD

运行！！！

现在蓝方GCI正在对威胁进行聚类

DISTRIBUION C. Distribution authorized to U.S. Government Agencies and their contractors, 9 Aug 19. Other requests for this document shall be referred to AFRL/RQQD

![](images/3d4a9c024cccd03966a59d1f35da6860091a564f656e4cb7a0f9002a8d16ec84.jpg)

# UNCLASSIFIED

# 围绕集群的边界

![](images/f097ed2e3707477e74d808d6106a8f34c1bd47e78017d76da02662bff274790a.jpg)

![](images/256f0b1bd4f2449c71c61d71904f59f998c4872e3af72633ac237d976af01eb8.jpg)

DISTRIBUON C. Distribution authorized to U.S. Government Agencies and their contractors, 9 Aug 19. Other requests for this document shall be referred to AFRL/RQQD 18

- 调试 AI 中队、FL（Flight Leads，飞行队长）和 GCI（Ground-Controlled Interception，地面控制拦截）问题的基础：

- 确认FL和GCI有可用的轨迹数据  
- 在指挥官的行为树中使用“debug_quantum_tasker”行为  
- 资产是否存在？（列）任务是否存在？（行）评估值是否为零？（主体）  
- 对于行为异常的代理，启用 script_DEBUG_writes  
- 检查事件文件或 GRIT 可视化工具，查看代理正在执行的行为

- 如果一个飞行队长赢得了所有目标，该怎么办？

- 只有一个集群吗？降低 GCI 的聚类距离阈值  
- 他是否赢得了多个集群任务？

- 确认评估脚本对其他飞行队长的任务生成了正值  
- 降低聚类阈值，以便生成更多可用任务

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9 Aug 19. Other requests for this document shall be referred to AFRL/RQDD

![](images/dc30ff9bf3ee898745e521e1cc0d08b61a8b3c06e749b5d91254a630d824a9a1.jpg)

# UNCLASSIFIED

# 调试任务问题

![](images/94aa84e52e310ef238429e1dc80e2808da51ea4519f4a2d02f6a617ac8a987f1.jpg)

- 一个目标集群被忽略了，该怎么办？

- 下属数量不足？有两个选项：

- 增加 GCI 的聚类距离阈值  
- 重新组织飞行队，将AI中队划分得更小

- 有些中队处于空闲状态？  
- 尝试在 GCI 上使用不同的任务分配模式

- 我不喜欢“轨迹 N”被聚类到“组 X”中

- 尝试使用不同的聚类方法、距离函数和/或距离阈值

DISTRIBUION C. Distribution authorized to U.S. Government Agencies and their contractors, 9 Aug 19. Other requests for this document shall be referred to AFRL/RQDD 20

# ·修改聚类参数

- 创建以下四个集群：南部战斗机、南部SOJ及护航、北部 SOJ及护航，以及UCAV（无人作战飞行器）  
- 创建一个单一集群  
- 使UCAV出现在两个或更多的集群中

# - 提示：

- 查看H树的最小值和最大值选项  
- 查看阈值

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9 Aug 19. Other requests for this document shall be referred to AFRL/RQQD

![](images/3f7e82be3ac7ce36d7d22a2fa46a0cb72c0a32214fb55d4fb54cca968d0d2eba.jpg)

DISTRIBUON C. Distribution authorized to U.S. Government Agencies and their contractors, 9 Aug 19. Other requests for this document shall be referred to AFRL/RQDD

# 6.1.10.8. 综合空地联合防空 28_AFSIM_BAM_Trng_Integration

# 6.1.10.8.1. 本节想定解析

本节想定资源在以下目录下：

afsim2.9_src\training\user\10_Other_Topics\bam\scenes\floridistan\28_floridistan_iads_integrated\run_course.txt,

行为与智能体建模培训的每一节都是在上一节的基础上的，而且想定较为复杂，因此要先了解上一节的内容。

本节是行为与智能体建模培训的最后一课，前面是空对空，地对空都有了，本节是在二者上面再建一级，统筹空地综合防空，其任务分析的原则也较为简单，凡在地对空的SAM的打击范围内的都分给地，其它的都分给空。其想定如下：

![](images/d617b74fb11a6a9060b28f2fef0fcfb39d22b4b9c5bc51244ff46707bc7346e5.jpg)  
图中天蓝色的线是分配给的任务线。

# 6.1.10.8.2. 本节PPT资料

本文为afsim2.9_src\training\user\10_Other_Topics\bam\slides\28_AFSIM_BAM_Trng_Integration.pptx的翻译。

![](images/509d1f966720d4927b3cea285f589630f3a0e2de039b43ea14be8666cad20ecf.jpg)

Integrity $\star$ Service $\star$ Excellence

# AFSIM用户培训

# 28- 综合空地防御

本文档由杨石兴翻译，该资料做为《AFSIM2.9参考手册》的一部分。没有《AFSIM2.9参考手册》的加杨石兴微信领取：13324598743

# AFRL/RQQD

# 美国空军研究实验室

DISTRIBUON C. Distribution authorized to U.S. Government Agencies and their contractors, 9 Aug 19. Other requests for this document shall be referred to AFRL/RQQD

![](images/b18ffa04cb2f73a5aac6909c95ebc9dcae13b5b834420ace3735c4dab740679a.jpg)

# UNCLASSIFIED

# 综合空地防御

![](images/07292317a935b54b11984b4c469ab241e7c4ed0e2f8c3bc0bed1b6177c522d78.jpg)

我们是一个Team，来一起干活。

![](images/d1f627b82b4e37275d878d0dbd8e71483529152fa2556912902828888bd9ef0c.jpg)

DISTRIBUON C. Distribution authorized to U.S. Government Agencies and their contractors, 9 Aug 19. Other requests for this document shall be referred to AFRL/RQQD

![](images/334a65b4f5cd20e25da0d0770a95b31a7f6e46f44d0c78366f87a1e4f8cd9e5b.jpg)  
Uses WSF_TASKPROCESSOR

DISTRIBUON C. Distribution authorized to U.S. Government Agencies and their contractors, 9 Aug 19. Other requests for this document shall be referred to AFRL/RQQD 3

![](images/f482417777fbd31b6ad87313340b03b1045e9f7f7cb5e8e41190229d32deefff.jpg)

# UNCLASSIFIED

# 空中防空

![](images/5985d6270e7f898bef1df2d968498894a4b1f32dc8b1f291774bc601f0cd87a0.jpg)

![](images/de7245785eb4e96338dc11e91ce97eb985fe9cc882c31061cffd87561d616c5d.jpg)  
Uses WSF_QUANTUM_TASKERPROCESSOR

DISTRIBUON C. Distribution authorized to U.S. Government Agencies and their contractors, 9 Aug 19. Other requests for this document shall be referred to AFRL/RQDD

![](images/c1eec8ae410fd143e81c2b272e4e823b78eaba04c639f3b2d549644918e88bf2.jpg)  
SOC uses WSF_QUANTUM_TASKERPROCESSOR

DISTRIBUON C. Distribution authorized to U.S. Government Agencies and their contractors, 9 Aug 19. Other requests for this document shall be referred to AFRL/RQQD

![](images/6a72aee95eeb37635c2e767ee9693c729e478d49ab5a9582b1ff834a0356a678.jpg)

# UNCLASSIFIED

# 区域作战指挥

![](images/fa538402bdc3e93a9db4f5754a8a1d94a85fd50ae04647081b507bef53d33655.jpg)

# setup.txt

```txt
7 // red commander  
8 include_once platforms/ship.txt  
9 include_once platforms/soj.txt  
10 // red SOJ  
11 include_once platforms/soj.txt  
12 // blue commander  
13 include_once platforms/flight_lead.txt  
14 include once platforms/gci cmdr.txt  
15 include_once platforms/soc_cmdr.txt  
16 // air platform (used by blue and red)  
17 include_once platforms/striker.txt  
18 
```

DISTRIBUON C. Distribution authorized to U.S. Government Agencies and their contractors, 9 Aug 19. Other requests for this document shall be referred to AFRL/RQQD

# platforms/soc_cmdr.txt

```snap
70 platform_type SOC_CMDR WSF PLATFORM   
72 icon C4I   
73 infrared signature VEHICLE_INFRARED_SIGNATURE   
75 optical signature VEHICLE_OPTICAL_SIGNATURE   
76 radar signature VEHICLE_RARAD_SIGNATURE   
77 comm blue_comm TEAM_DATAALINK   
79 network_name blue_net   
80 internal_link data_mgr   
81 internal_link task_mgr   
82 end_com   
83   
84# processor data_mgr WSF TrackPROCESSOR   
85 purge_interval 60 sec   
86 # execute at interval of 30 sec   
87 # writeIn("----",PLATFORM.Name(),"tracks:---");   
88 # foreach(NsFTrack t in PLATFORMMASTERTrackList())   
89 {   
90 # writeIn("track:" ,t.TargetName());   
91 }   
92 # end_execute   
93 endprocessor   
94   
95# processor task_mgr SOC_CMDR_QUANTUM_TASKER   
96 endprocessor   
97   
98# processor perception WSF_PERCEPTION_PROCESSOR   
99 script debugWrites off   
100 reporting_self false   
101 reporting_others false   
102 asset_perception truth subordinates   
103 asset_update_interval 5 sec   
104 max_asset_load 100   
105 thread_update_interval 5 sec   
106 max-threat_load 100   
107 endprocessor   
108   
109 endplatform_type 
```

DISTRIBUON C. Distribution authorized to U.S. Government Agencies and their contractors, 9 Aug 19. Other requests for this document shall be referred to AFRL/RQQD

7

# UNCLASSIFIED

![](images/3c1fa2dfee00596368e4cee45a8c310ba3dcc06681b671b4f7cb6ac515d955d8.jpg)

# SOC Quantum Tasker

![](images/7704edd4e64d537b3c7169d38a027137f083cf2134cbc9b9d3585f58670c729a.jpg)

# platforms/soc_cmdr.txt

```txt
53 #show_task/messages   
54 script debugWrites off   
55 update_interval 5.0 sec   
56 reallocation_strategy dynamic   
58 generator custom SOC Generation   
59 evaluator custom SOC_Evaluation   
60 #Allocator optimal_profit   
61 allocator greedy_isolated   
62 allocatorextra_tasks greedy_isolated   
63 #Allocatorcustom EmptyAllocator   
64 #Allocatorextra_tasks optimal_profit   
65   
66 #behavior_tree   
67 #behavior_node debugquantum.Tasker   
68 #end_beharior_tree   
69 end Processor 
```

- The greedy allocator will only allocate the first two tasks   
- The extra task allocator will then allocate the remaining tasks   
- Because of the binary nature of the evaluator, every task will be allocated

DISTRIBUON C. Distribution authorized to U.S. Government Agencies and their contractors, 9 Aug 19. Other requests for this document shall be referred to AFRL/RQQD

platforms/soc_cmdr.txt   
32 script double SOC_Evaluation ( WsfQuantumTask TASK, WsfAssetPerception ASSET)   
33   
34 WsfTrack track $=$ PLATFORM.MasterTrackList().FindTrack(TASK.TrackId());   
35 if (track.IsValid())   
36 { bool InMez $=$ track.WithinZoneOf(PLATFORM, MEZ-zone_NAME);   
38 if (InMez $= =$ true && ASSET.Type() $= =$ "IADS_CMDR")   
39 { return 1.0;   
41 } else if (InMez $= =$ false && ASSET.Type() $= =$ "GCI_CMDR")   
43 { return 1.0;   
44 }   
47 return 0.0;   
48 end script

DISTRIBUON C. Distribution authorized to U.S. Government Agencies and their contractors, 9 Aug 19. Other requests for this document shall be referred to AFRL/RQDD

![](images/bca34df85faffc8f7f3985e5c78237a4ab26dd9772bda09bf558d9351bb1678f.jpg)

# IADS指挥官需要任务分配

![](images/cbea39042d5d5cea5ea86656f74c167881132403f1c494094c1f7d1a4a8159b5.jpg)

UNCLASSIFIED   
platforms/iads_cmdr.txt   
script_variables   
20 int MAX_SAMS_PER_TARGET $= 2$ 21 int MAX_ASSIGNMENTS_PER_SAM $= 4$ 22 string WEAPON_NAME $= \mathrm{"sam"}$ 23 bool REQUIRE_ASSIGNMENT $= \mathrm{false}$ 24 endScript_variables   
25   
26 // determine if TRACK is assignable   
27 script bool Assignable()   
28 if (REQUIRED_ASSIGNMENT $= =$ true && TasksReceivedFor(TRACK.TrackId()) <= 0)   
30 { return false; }   
33 if (!TRACK.IFF_Friend()) && (TRACK.TimeSinceUpdated() < 30.0))   
34 { return true; }   
36 return false;   
39 endScript

DISTRIBUION C. Distribution authorized to U.S. Government Agencies and their contractors, 9 Aug 19. Other requests for this document shall be referred to AFRL/RQDD

platforms/iads_cmdr.txt & platforms/gci_cmdr.txt   
DISTRIBUION C. Distribution authorized to U.S. Government Agencies and their contractors, 9 Aug 19. Other requests for this document shall be referred to AFRL/RQQD   
149 # script_variables
150 # WsfDraw mDraw = WsfDraw(   );
151 # endScript_variables
152 # Draws lines to all assigned tasks
153 # execute at_interval_of 10 sec
154 # mDraw.setColor(1.0, 0.0, 1.0);
155 # mDraw.setDuration(10.0);
156 # foreach(WsfTask task in PROCESSORReceivedTaskList(   ))
157 # \{ $\mathrm{{WsfTrack}\;{track} = {PLATFORM}.MasterTrackList().Find\left( {{task}.{LocalTrackId}\left( \right) }\right) }$ if (track.IsValid(   ))
			\{ $\mathrm{{WsfPlatform}\;{plat} = \;{WsfSimulation}\;{FindPlatform}\left( {{track}.{TargetIndex}\left( \right) }\right) }$ if (plat.IsValid(   ))
				\{
					mDraw.BeginLines(   );
					mDraw.Vortex(PLATFORM);
					mDraw.Vortex Plat);
					mDraw.End(   );
			\}
			\}
\}
170 #

![](images/206e0ef368e8641502c0ba6c655ff63cc928a98b9a17887bb83ff1907cb9162a.jpg)

# UNCLASSIFIED

# 实例化SOC Commander

![](images/650a75c2f0a49cdaae433f79553f8c5dba441a00a2e2e23d9061a788c4972735.jpg)

scenarios/small_blue_iads.txt

```txt
28
29 platform 10_soc_cmdr SOC_CMDR
30 side blue
31 use-zone 100 brigade_section as MEZ
32 position 30:21n 82:15w altitude 0.00 ft msl
33 commander SELF
34 endplatform 
```

DISTRIBUION C. Distribution authorized to U.S. Government Agencies and their contractors, 9 Aug 19. Other requests for this document shall be referred to AFRL/RQQD

scenarios/small_blue_iads.txt   
```txt
33 platform 10_iads_cmdr IADS_CMDR
35 side blue
36 command_chain blue_chain 10_soc_cmdr
37 position 30:22:32n 81:58:34w
38 altitude 0.00 ft agl
39
40 edit processor taskmgr
41 #show_task/messages
42 script_variables
43 REQUIRE_ASSIGNMENT = true;
44 endScript_variables
45 end Processor 
```

DISTRIBUION C. Distribution authorized to U.S. Government Agencies and their contractors, 9 Aug 19. Other requests for this document shall be referred to AFRL/RQQD 13

![](images/784d35f90dbdbe58a9a58cbfe81ce7c1400df5f80dcffbd07bdf7660c4e4240c.jpg)

# UNCLASSIFIED

# 修改GCI Commander

![](images/a96fec16f0447f36f87852d0b5e9cc69ad993f73211a168af30e4500dd1db3e5.jpg)

scenarios/blue_air_cap.txt   
```txt
14   
15   
16   
17   
18   
19   
20   
21   
22   
23   
24   
25   
26   
27   
28   
29   
30   
31   
32   
33   
34   
35   
36   
37   
38   
39   
40   
41   
42   
43 
```

DISTRIBUON C. Distribution authorized to U.S. Government Agencies and their contractors, 9 Aug 19. Other requests for this document shall be referred to AFRL/RQQD 14

RUN IT NOW!!!

DISTRIBUON C. Distribution authorized to U.S. Government Agencies and their contractors, 9 Aug 19. Other requests for this document shall be referred to AFRL/RQQD 15

![](images/7de3931a2ae551af356f3d157d88375d59fbd3cbda052e5a5c115a9fc4b564b2.jpg)

# UNCLASSIFIED

# 练习

![](images/42fb1b0a20725e3fadad6c798ff90c76efd21687fb77971ce40eff573f87548b.jpg)

- 当前场景实际上并未展示出这一点是有效的  
修改场景以证明它确实有效  
- 提示：有很多方法可以做到这一点。

培训问题：

Afrl.rq.afsim-training@infoscitex.com

其它问题？

联系AFSIM组：

afrl.rq.afsim-help@us.af.mil

![](images/02a4ead2adafb320778dd85d493f6d52b9948f68ef3583bfaff7e2afddd547f9.jpg)

评估

DISTRIBUION C. Distribution authorized to U.S. Government Agencies and their contractors, 9 Aug 19. Other requests for this document shall be referred to AFRL/RQQD

![](images/824fd3b29ac2911f9096b58a96ecfc4155c93ee25469162b6cb7f306c63515cc.jpg)

DISTRUBION C. Distribution authorized to U.S. Government Agencies and their contractors, 9 Aug 19. Other requests for this document shall be referred to AFRL/RQQD

# 6.2. 开发培训 developer

# 6.2.1. 核心core

# 6.2.1.1. 培训介绍0_AFSIMDev-Trng_Introduction

本文为afsim2.9_src\training\developer\core\slides\0_AFSIMDev_Trng_Introduction.pptx的翻译，主要是整体介绍一下开发课程的安排。

![](images/8c3cace943d06abf80368a79d4bd3c961f62332bee5d87fa4fcdbf1ba2824702.jpg)

UNCLASSIFIED

![](images/0d5f925bfb13c9e1f48530b3818a928a99cc6ace62cda2d61a9f55e2e8ec98a4.jpg)

![](images/8f6d3af5465c09c7dfc66e8442c6e424f74975a4de828db658b90e027b2a71e8.jpg)

# AFSIM开发培训0－课程介绍

本文档由杨兴翻译，该资料做为《AFSIM2.9参考手册》的一部分。没有《AFSIM2.9参考手册》的加杨兴微信领取：13324598743

integrity $\star$ Service $\star$ Excellence

# AFRL/RQQD 美国空军研究实验室

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

# 第1天

- 欢迎&介绍   
- Cmake&安装  
架构概览   
- Mission概览   
- 传感器Sensors - Part 1

# 第2天

- 传感器Sensors - Part 2   
- 武器Weapons - Part 1

# 第3天

- 武器Weapons - Part 2  
运动Movers

# 第4天

组件Components

# - 第5天

- 观察者Observers

# - 第6天

- 通信Communications

# - 第7天

XIO   
- 语法Grammar   
- Qt

# - 第8天

-WKF   
- Warlock

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19.

Other requests for this document shall be referred to AFRL/RQQD.

# 6.2.1.2. 架构概览 1_AFSIM_DeTrng_ArchitectureOverview

本文为afsim2.9_src\training\developer\core\slides\1_AFSIMDev_Trng_ArchitectureOverview.pptx的翻译，主要是整体介绍一下AFSIM的整体结构。

![](images/e65989c4c12bf880c5285d54266d14bec6b0ac22e66d261d8f97e616a5307d21.jpg)

Integrity $\star$ Service $\star$ Excellence

# AFSIM开发培训1-架构概览

本文档由杨石兴翻译，该资料做为《AFSIM2.9参考手册》的一部分。没有《AFSIM2.9参考手册》的加杨石兴微信领取：13324598743

# AFRL/RQQD 美国空军研究实验室

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQQD.

1

![](images/b5e667e97d0b1774bcffba5c36c46ca59faed1e3fd82a87e21fee45d00d24d4b.jpg)

UNCLASSIFIED

从这里开始…

![](images/20f50626e8bd4d89e7d83ad3f5d28bbec8984c9d2fcccfcdc3980cd63d65f793.jpg)

# 别害怕!

![](images/5cd269c1daf3ae217723ca47e686635d972093de209a77d631e9e4ceaeb25ee5.jpg)

事情只有在不可能之前才是不可能的

——让-吕克·皮卡尔（Jean-Luc Picard）

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQDD.

AFSIM - Advanced Framework for Simulation, Integration, and Modeling

AGL - Above Ground Level

DIS - Distributed Interactive Simulation

DTED - Digital Terrain Elevation Data

EO/IR - Electro-Optical/Infra-Red

ESM - Electronic Support Measure

FOV - Field Of View

GUI - Graphical User Interface

HLA-High Level Architecture

IEEE - Institute of Electrical & Electronics Engineers, Inc.

JTIDS - Joint Tactical Information Distribution System

MSL - Mean Sea Level

PDU - Protocol Data Unit

RCS - Radar Cross Section

SAM - Surface-to-Air Missile

SAR - Synthetic Aperture Radar

VESPA - Visual Environment for Scenario Preparation and Analysis

WKF - Warlock Framework

WSF - World Simulation Framework

dB - decibels

dBsm - decibel square meters

deg-degrees

ft-feet

GHz-GigaHertz

kts-knots

m - meters

m^2 - square meters

mw-megawatts

nm - nautical miles

s - seconds

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19.

Other requests for this document shall be referred to AFRL/RQQD.

# UNCLASSIFIED

# 介绍

![](images/e7d5dc71072a88af94c832129b77f99b0ef141f5afa4ee6509821a9d0ba17b6a.jpg)

![](images/4ae845b3f8411ea56c9594fceecb8ed78b14211feab993b6f2bf9c3b99909e27.jpg)

- 本演示文稿概述了AFSIM架构。  
- 本培训旨在教开发人员如何使用AFSIM仿真框架创建任务级别的仿真。

- 实验内容包括以下领域：：

使用CMAKE构建AFSIM

- 传感器

练习1：了解AFSIM插件和扩展  
练习2：创建自定义AFSIM传感器  
练习3：创建自定义AFSIM传感器脚本接口

武器

练习1：注册一个新的应用扩展  
练习2：创建自定义AFSIM武器

- 运动器（Mover）

练习1：注册一个新的应用扩展  
练习2：创建一个利用MATLAB DLL的自定义AFSIM运动器  
练习3[可选]：编译一个MATLAB DLL

组件

练习1：注册一个新的应用扩展、新的场景扩展和组件工厂  
练习2：创建自定义AFSIM组件  
练习3：创建组件工厂  
练习4：创建自定义AFSIM组件脚本接口

- 观察器（Observer）

使用默认应用扩展和新的场景扩展创建自定义AFSIM观察器

通信

练习1：注册默认应用扩展、新的场景扩展和新的仿真扩展  
练习2：为通信场景实现ProcessInput   
练习3：创建自定义AFSIM通信设备和消息

·练习4：创建自定义AFSIM通信脚本接口

外部输入输出（eXternalIO,XIO）

练习1：注册默认应用扩展、新的场景扩展和新的仿真扩展  
练习2：实现一个仿真扩展，用于读取和处理新的XIO消息以控制选定的平台  
练习3：创建一个与AFSIM仿真通信的外部应用程序

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19.

Other requests for this document shall be referred to AFRL/RQQD.

![](images/95646bf621a2ec9327d4bdadd666e69621d01d19613c98eb95187cca68b51cb0.jpg)

- 您将学习以下内容：

- 高级仿真、集成与建模框架（AFSIM）。

- 了解课程内容的总体概况。

![](images/eb19b1c52a9a8f4023b549b4deb93890203f409ddb16bd4cb9993d82ed2507f4.jpg)

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQQD.

5

![](images/e313ed79f874d79571d9b4b57a2a994999658c6c30e16b77dfe07ab04c8f27a0.jpg)

# UNCLASSIFIED

# 背景

![](images/c707fe3980c9718709b217aca57c14b3d36b54f108c5fab2a42b5bd9c6ec8047.jpg)

什么是AFSIM？

- AFSIM 是一个仿真框架，主要用于满足运筹学社区在任务级分析中的需求。

为什么开发AFSIM？

分析社区的需求未得到满足。  
- 传统的政府仿真工具（如 SUPPRESSOR）缺乏足够的灵活性，无法分析先进概念和技术。  
- 使用Excel和VB开发的低保真工具无法满足复杂需求。  
从头开发新的分析仿真工具成本过高。  
- AFSIM提供了一套软件构建模块，可以快速（以周或月为单位，而非年）开发复杂的分析仿真工具。

- AFSIM 的当前状态是什么？

- AFSIM 是一个成熟的仿真框架，已交付给政府，拥有无限制使用权，并且政府和工业界均可免费使用。  
包括所有源代码。  
- 包括经过验证和确认（V&V）的机密场景，这些场景基于SUPPRESSOR，但可以扩展以分析先进武器系统概念的作战效益。

- AFSIM 的特点：

约200万行代码（截至2021年1月15日）。  
- 使用 $\mathbb{C} + +$ 编写（当前版本使用 $\mathbb{C} + + 11$ ）。  
生成非常高效且性能优越的代码。  
- 使用 Qt 作为用户界面框架。  
大量使用面向对象的编程范式：

封装和抽象  
继承   
多态

- 结果：

- 高效。  
- 稳定、可靠且准确。  
提供大量的组件、服务和分析功能。  
- 易于添加或扩展行为。  
- 易于添加或扩展组件和服务。

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQQD.

7

![](images/718103ae086faeb6918e5dedbd2c1ae809cff87d93759cf77e1079b62dd475cf.jpg)

# UNCLASSIFIED

# 一些标准的AFSIM程序

![](images/17f3902832babd922e41e240ac2196696ad04678001049f0fa6c16452c4955c0.jpg)

- Mission 提供了一种执行 main 的方式。  
- Warlock 提供了另一种执行 main 的方式。  
- Wizard 是一个图形用户界面（GUI），用于构建要执行的场景。

- 这些场景会保存为 .txt 文件，并在执行时由 Mission 或 Warlock 加载。

- Mystic 提供了一个 GUI，用于通过生成的 .aer 回放文件重放仿真。

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQDD.

![](images/3d7815a25592a4a3d81eda647fa19277ff5e11c00403d74ff63730ebffa2ecb6.jpg)  
Workflow

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQQD.

# UNCLASSIFIED

# AFSIM架构概览

![](images/5867a299a82fc74ee14e11394736710ba07e3c8765c2b657104ac3c097a503dd.jpg)

![](images/6db09e5b952adbe8c5d63c3b541b20d5495297fa13e778f951740a66b40da3a0.jpg)

AFSIM 框架提供了一个通用的基础设施、接口和基于组件的架构，以支持仿真应用程序的开发。

# AFSIM应用程序

# AFSIM框架

基础设施

想定管理

推演管理

时间管理

事件管理

地理空间数据管理

插件管理

工具

接口

脚本语言

观察者

分布式接口

扩展

组件

平台组件

运动

传感器

传感器

组件

武器

武器组件

${12}/{12}$

件

$\therefore m = \frac{3}{11}$

处理器组件

···

$\frac{1 + u}{7} = {70}\frac{1}{9}$

其它平台组件

非平台组件

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19.

Other requests for this document shall be referred to AFRL/RQQD.

要在自定义仿真中利用AFSIM框架，您需要：

- 创建或利用现有的仿真主循环（通常利用AFSIM扩展）。  
- 构建新的功能作为AFSIM插件，以便与现有仿真一起使用。

- 通常会使用“Mission”（标准仿真应用程序）。

- 在本课程中，我们将同时研究和利用一个“最小化”的仿真主循环，通过扩展添加功能，并构建新的功能作为AFSIM插件。

# AFSIM Application

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQQD.

# UNCLASSIFIED

![](images/eb976a82ccd0818314e13a0c436eb3882c1e354410bbdef2afedc65e8a2956c6.jpg)

# 应用程序, 想定和推演仿真

![](images/b708c6f4bd134482ed8d80a2a782fe744922bf1d395961d8640c3c21b90f1aa8.jpg)

- 每个可执行文件中只有一个 AFSIM 应用程序。

- 负责维护脚本类型和插件管理器。

- 应用程序由一个或多个场景组成。

- 拥有类型工厂、输入和服务。

在实际应用中，每个应用程序仅包含一个场景。

- 场景用于实例化仿真。

- 拥有观察器接口和类型实例。

- 每个仿真仅包含一个场景。

通常，每个场景对应一个仿真。

- 应用程序、场景和仿真的扩展提供了添加功能的灵活性。

# AFSIM Application

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19.

Other requests for this document shall be referred to AFRL/RQQD.