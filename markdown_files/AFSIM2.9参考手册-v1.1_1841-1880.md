# 6.1.10.1.1.4. 仿真过程

阶段零：四架无人机照着设置的四个目标和路径就奔过去投弹了

阶段一（下图）：蓝方早期预警雷达 200_ew_radar 和 300_ew_radar 探测并建对红方目标建立跟踪，建立跟踪后上报给它的最高级指挥官 10_iads_cmdr

![](images/c5688764ea74a8fcabbfb5c57f582314b92b6a3c8e867aaa61b96bc1acb8ba4d.jpg)

因为 ew 雷达的最大作用距离并没有设置，可以认为距离非常远，可以覆盖当前场景的所有目标，因此演示刚开始就陆续建立了所有目标的探测和跟踪。在过程中也不断的失跟，又重新跟踪。

拿 300_ew_radar 举例通过查看事件列表(Mystic->Tools->Show EventList)可以得知：  

<table><tr><td>时间(秒)</td><td>平台</td><td>目标</td><td>交互</td></tr><tr><td>0</td><td>300_ew_radar</td><td>uav-4</td><td>探测到</td></tr><tr><td>5.71</td><td>300_ew_radar</td><td>soj_south</td><td>探测到</td></tr><tr><td>8.57</td><td>300_ew_radar</td><td>soj_north</td><td>探测到</td></tr><tr><td>11.42</td><td>300_ew_radar</td><td>uav-3</td><td>探测到</td></tr><tr><td>14.285</td><td>300_ew_radar</td><td>uav-2</td><td>探测到</td></tr><tr><td>17.14</td><td>300_ew_radar</td><td>uav-1</td><td>探测到</td></tr><tr><td>40</td><td>300_ew_radar</td><td>uav-4</td><td>建立跟踪</td></tr><tr><td>45.71</td><td>300_ew_radar</td><td>soj_south</td><td>建立跟踪</td></tr><tr><td>51.42</td><td>300_ew_radar</td><td>uav-3</td><td>建立跟踪</td></tr><tr><td>68.57</td><td>300_ew_radar</td><td>soj_north</td><td>建立跟踪</td></tr><tr><td>77.1429</td><td>300_ew_radar</td><td>uav_1</td><td>建立跟踪</td></tr><tr><td>154.286</td><td>300_ew_radar</td><td>uav_2</td><td>建立跟踪</td></tr></table>

阶段二（下图）：四架无人机到达了要攻击的目标(四个 Target）的无人机挂弹的可攻击范围，则发弹进行打击

![](images/e1c164af0f65409d1951ee0dbb0b3ba26aa5b4a2e360cd15df954398c4fc13c1.jpg)

阶段三（下图）：无人机投弹后，弹也在往过飞，无人机也在往过飞，飞到蓝方指挥所10_iads_cmdr 指定的区域(battalion_sector，以 3500_large_sam_battalion 为圆心，30海里)时,下图白圈。则 10_iads_cmdr 给 3500_large_sam_battalion 下任务，如下图中紫色线。

![](images/75c8b46b1e8d0fa7891557c0e4b94d56e0fad95c8816027cad5ecdc35bddff4f.jpg)

阶段四（下图）：3500_large_sam_battalion 则指示目标捕获雷达进行进一步探测，

下图是目标捕获雷达 3510_acq_radar 雷达对所有来袭目标进行捕获并建立跟踪

![](images/3d492866b8604673551a322167590b83eb920e49588e5933ee2ff7dfa589a34e.jpg)

阶段五：目标捕获雷达捕获目标后，待其到达可打击区域后，由目标跟踪雷达导引 3辆导弹发射车进行拦截。敌弹有些打中了目标，有些也被拦截了。

# 6.1.10.1.2. 本节 PPT 资料

本文为 afsim2.9_src\training\user\10_Other_Topics\bam

\slides\21_AFSIM_BAM_Trng_Review.pptx 的翻译。

![](images/cab0602e3cb6c157fea71dd13140050cfa11c60201d24025ebe6b03e8c279d1e.jpg)

UNCLASSIFIED

![](images/4bf63b01e66f8ae3f2ae63cfe400a23ce6e1f69e395c839cddf95d3285cb9d88.jpg)

![](images/f27b6d08900d2fc36c6a796e3c027be543be5f71b008919eb75547886897155b.jpg)

Integrity★Service★ Excellence

# AFSIM用户培训

# 21－行为与智能体建模

AFRL/RQQD

美国空军研究实验室

DISTRIBUTIoistrtitdtUeetencndthotractsugtheestftumesaet

AFRL/RQQD

·目标(Targets)   
·红方

搭载武器的无人机(UAV)   
-远程干扰机(SOJ's)

·蓝方

地空导弹系统(BAM)

目标捕获雷达(AR)   
目标跟踪雷达(TTR)   
导弹发射装备(ML)  
地空导弹指挥部

－空中拦截机  
早期预警雷达(EWR)  
指挥控制结点

![](images/53adcce243e80201efdee90b8b637aa4c0a859bf509780492b482f89a415bbf5.jpg)

DISTRIBUTIostritiuttUeetecedtetractosrestftcumetld AFRL/RQQD 2

![](images/7bbd06edab59753e5d82c68c129226a43ef3d58cd5686e75a71bf87737b9022a.jpg)

# UNCLASSIFIED

# 事项

![](images/94b271db1d560db183b9607fcb36c86aa750aa9dfe1ab2426fbe1fbb69a9d271.jpg)

·感知处理器和细粒度任务处理器  
·行为树/追踪行为/武器/交战行为   
·路径规划器  
·返回基地/护送行为   
·威胁处理器/规避行为  
·聚类/CC2/任务分解   
·AIR与IADS的集成

DISTRIBUTIOstrtiuthedtUoventAcdeotractsuOtreestftcumetsld AFRL/ROOD 3 3

![](images/0878e26f9b70fb9ec9b2bc3c1c96c259e40e85d770b87483b1bc7f9bb79d6e07.jpg)  
DISTRIBUTIostrtittUeetecedetractorestftcumtl AFRL/RQQD 4

![](images/5358c795cd6223383b67f1b2fe091e280359ffaf5309b056f727c298de08dea3.jpg)

# UNCLASSIFIED

# 基础

![](images/05dcd74902dcddf09cdf102a6cd294190d4757868173bc076619e07619fc834f.jpg)

·理论部分

－平台和组件作为AFSIM对象的概述

·处理器示例

-AGENT功能与流程概述

·应用部分

－添加SOJ平台及其指挥舰  
－展示AFSIM人工智能代理的初步实现

·平台和组件由AFSIM输入定义定义   
·AFSIM示例：

-输入定义:WSF_SCRIPT_PROCESSOR   
－脚本对象：WsfProcessor

·用户可以定义更多类型，并从已有类型派生

－示例：

```txt
processor MY_TYPE WSFScriptPTPROCESSOR //do special stuff inside end Processor 
```

·WsfScriptProcessor是关键类型，很多类型都是继承于它:

-WsfTaskManager   
-WsfQuantumTaskerProcessor   
-WsfPerceptionProcessor   
一 etc...

DISTRIBUIONistititordtUverentencendthtractorstherqestfotcumtd AFRL/RQQD 6 6

![](images/72f0910516ec162a007f1117ed8b52210d232f0ecffcb55f09617780b12d8607.jpg)

# UNCLASSIFIED

# 脚本处理器(Script Processor)

![](images/f1033adf2a3398ad3bc37af136dfc64330cdb604e6c371823abbeeb62de2e438.jpg)

# WSF_SCRIPT_PROCESSOR

Navigation:Predefined Processor Types

Script Class:WsfProcessor

# WsfProcessor

Navigation:Script Types

Derivesfrom:WsfPlatformPart,WsfObject

InheritedbyWsfaunchComputerWsfsknagerWsfWeaponFuseWsfPerceptionrocsso

# Overview

WSF_SCRlPT_PRoCEssOR isaprocessor that allows the user to provide scripts that can be executed whenever theprocessor receives amessage oriscalled for aperiodic update Inaddition itallws the definitionofexternalinkstoroutemessagestootherplatformsBesidestheregularonupdate"scriptblock ontheprocessor.userscanusebehaviortreesandfinitestatemachinesonthescriptprocessortohelpthem organize theirscrint The order of operationof ascrintprocessoreachupdate is

1.on update script block   
2.behaviortree ontheprocessor   
3.finitestatemachineevaluatesthecurrent state

# WSF_TASK_PROCESSOR

Navigation:Predefined Processor Types

DerivesFrom:WSFSCRIPT PROCESSOR

ScriptClasses:WsfTaskProcessor

# WSF_QUANTUM_TASKER_PROCESSOR

Navigation:Predefined ProcessorTypes

DerivesFrom:WSF_SCRIPT_PROCESSOR

BrotherTo:WSF_TASK_PROCESSOR

ScriptClasses:WsfQuantumTaskerProcessor

DISTRIBUTIostrtittUeetesdtetractstfcumetl AFRL/RQQD 7

·从所有这些派生类型中可以得出的结论是什么？

－任何从某个类型派生的类型，都继承了父类型的所有功能和脚本方法。  
-例如，WSF_QUANTUM_TASKER_PROCESSOR具有WSF_SCRIPT_PROCESSOR的所有功能，包括：

·on_update脚本块   
·行为树（behavior_tree）  
·状态块（有限状态机，stateblocks）

DISTRIBUIOstrtithdtUoeentecisdtetractosteeestftmntal AFRL/RQQD 8

![](images/715c957b34030063dd74206a0c6c44ca0a664eee97bb9a898d497de4eac931bb.jpg)

# UNCLASSIFIED

# 代理

![](images/86cc25c971194ea620ae29d731abcc61d714b493ba655074f247e286c5cc55d3.jpg)

# 什么是人工智能代理？

![](images/a722bbe8d2bcfe36b529fb059b3e5e7d61c70a89055b206f57cdb9160c2b6b73.jpg)

DISTRIBUTIOstrtiuthedtUoventAcdeotractsuOtreestftcumetsld AFRL/ROOD 9 9

在具有AFSIM组件的AFSIM平台上，代理的流程是什么样的？

![](images/57b58332eb31c2a80c0a2cb112b2ae64fb61489290b1427356e72d4a0beccf4c.jpg)

![](images/e977ada439945465f92b9e36d38796a55b9bf7bec39903777fc4d3d0f5175b18.jpg)  
DISTRIBUTIOstrtitdtUoeenteciesdtetractostereqesftmntal AFRL/RQQD 10

![](images/8c51cd0498f3a16634a7b06d74bd11214f5b5c1ea8afcd1aebedcdea8cbd646f.jpg)

# UNCLASSIFIED

# 代理工作流程

![](images/753632a20892b2905b3112e69dbaaacebf5d31d51a92ac8310a63d24f2de5257.jpg)

在具有AFSIM组件的AFSIM平台上，代理的流程是什么样的？

![](images/4f4372935f7dc7d367abfc2ecb371165b916790ab3feca00a07c17f40810d4aa.jpg)

![](images/1aa36ebcb46f9c738694bbf505d14f5c59ecab16943ff9a53565cf854df50366.jpg)  
DISTRIBUTIOstrtiuthedtUoventAcdeotractsuOtreestftcumetsld AFRL/RQQD 11 11

# setup.txt

```c
2 include_once platforms/common.txt   
3   
4 include_once platforms/target.txt   
5 include_once platforms/ucav.txt   
6 include_once platforms/ucav.txt   
7   
8 //red commander include_once platforms/ship.txt   
9 include_once platforms/soj.txt   
10 //red SOJ include_once platforms/soj.txt   
11   
12   
13 include_once event_output.txt   
14   
15 include_once observers.txt   
16 
```

DISTRIBUTIostritiuttUeetecedtetractosrestftcumetl AFRL/RQQD 12 12

![](images/d91d6c968ce48c103918de8f4c6263ce4863c4f10180a7c31e5b4b14b5d0fcf3.jpg)

# UNCLASSIFIED

# 新的想定

![](images/cd45f6ad6a13bb14b9ee571af490bdaceeb0f328174973fc594460ff88cd0442.jpg)

# run_course.txt

```c
run_course.txt\*   
1 define_path_variable CASE jacksonabad   
2 log_file output/\\(CASE).log   
3   
4 // setup file containing type definitions   
5 include_once_setup.txt   
6   
7 // include the scenario files   
8 include_once scenarios/targets.txt   
9 include_once scenarios/red_air_strike.txt   
10 include_once scenarios/small_red_iads.txt   
11 include_once scenarios/red_air_support.txt   
12   
13 event_output file output/\\)CASE).evt end_event_output   
14 event_pipe file output/\\)CASE).aer end_event_pipe   
15   
16 end_time 60 minutes   
17 
```

DISTRIBUTIOstrtiuthedtUoventAcdeotractsuOtreestftcumetsld AFRL/RQQD 13 13

red_air_support.txt   
DISTRIBUTIostritiuttUeetecedtetractosrestftcumetl AFRL/RQQD 14   
UNCLASSIFIED   
```txt
15 platform ship_lead SHIP   
16 side red   
17 icon Carrier   
18 command_chain blue_chain SELF   
19 heading 0 deg   
20 route   
21 position 30:30n 79:00w speed 30 knots   
22 insert-route ship.patrol reference Heading 0 deg   
23 end-route   
24 endplatform   
25   
26 route soj_orbit   
27 label start   
28 offset 20 0 km speed 450 kts altitude 35000 ft msl   
29 radialacceleration 2 g   
30 offset 20 5 km speed 450 kts altitude 35000 ft msl   
31 radialacceleration 2 g   
32 offset 0 5 km speed 450 kts altitude 35000 ft msl   
33 radialacceleration 2 g   
34 offset 0 0 km speed 450 kts altitude 35000 ft msl   
35 radialacceleration 2 g   
36 goto start   
37 endRoute 
```

![](images/948ef3b488ec65f5ecea75da12df9848285b8b798a14ce95e17e8c859e410396.jpg)

# 远距离干扰机

![](images/05358b930eea36262d28f1d24f50d8f239bbc05819d36addf52ae4b5b1b66ad6.jpg)

red_air_support.txt   
DISTRIBUTIostritiuttUeetecedtetractretftcumtl AFRL/RQQD 15 15   
```txt
43 platform soj_south SOJ  
44 side red  
45 icon weasel  
46 commander ship_lead  
47 route  
48 position 29:33:57.54n 80:08:06.19w altitude 35000 ft msl  
49 speed 450 kts  
50 position 29:46:00.17n 80:36:37.58w altitude 35000 ft msl  
51 insert-route soj_orbit reference Heading 300.0 deg  
52 end-route  
53 heading 246.4 deg  
54 endPLATFORM  
55  
56 platform soj_north SOJ  
57 side red  
58 icon weasel  
59 commander ship_lead  
60 route  
61 position 31:16:00.17n 80:08:06.19w altitude 35000 ft  
62 ms1 speed 450 kts  
63 position 31:03:57.54n 80:36:37.58w altitude 35000 ft msl  
64 insert-route soj_orbit referenceHeading 240.0 deg  
65 end-route  
66 heading 276.5 deg  
67 endPLATFORM 
```

RUN IT!!!

DISTRIBUTIostritiuttUeetecedtetractosrestftcumetl AFRL/RQQD 16

![](images/33ad3a731f8ee0e5989b98a49dadda092f8a8074b54845922a86de62da298911.jpg)

# UNCLASSIFIED

# 练习

![](images/78bb9c86cd80dbcc848bd12c9397bd1ae3de653130681dc3447b95b07f62f433.jpg)

在蓝方IADS指挥官上，定期执行以下操作：

打印平台主轨迹列表中每个轨迹的轨迹ID和目标名称。

提示：

定期间隔可以通过execute或on_update脚本块实现。  
访问主轨迹列表（MasterTrack List）是一个PLATFORM脚本方法。

建议：

为了提高输出的清晰度，可以在输出中显示当前的模拟时间。

DISTRIBUTIOstrtitdtUoeenteciesdtetractostereqesftmntal AFRL/ROOD 17 17

![](images/7508f006cceff44520a0f6ac4be56204a7dffb91f6edf13c3b10033ac766e540.jpg)

DISTRIBUIONistititordtUverentencendthtractorstherqestfotcumtd AFRL/RQQD

# 6.1.10.2.感知与原子任务处理器 22_AFSIM_BAM_Trng_PerceptionQuantumTasker

# 6.1.10.2.1. 本节想定解析

行为与智能体建模培训的每一节都是在上一节的基础上的，而且想定较为复杂，因此要先了解上一节的内容。本节想定也是在上一节的基础上来更改的，重复的地方不再描述。因此要想掌握本节想定请先阅读上一节的内容：6.1.10.1 行为与智能体建模培训概览21_AFSIM_BAM_Trng_Review。

本节较之上一节，对红方船只和干扰机增加了干扰行为如下：

# 1) 一艘指挥船(SHIP) ship_lead

指挥船首先针对每个探测到的敌方雷达建立任务，根据每个任务中敌方雷达的频率来选择其下属中不同的干扰武器进行干扰。

其自己不包含雷达为什么会能够获取敌方的雷达信息呢？其有两个下属无人机soj_north 和 soj_south，在本节这两个无人干扰机加装了雷达 sensor esm UCAV_ESM。

# 2) 两架远距离干扰机(soj) soj_north, soj_south

无人干扰机加装了雷达 sensor esm UCAV_ESM，以及 5 个干扰武器，分别为：weaponvhf_jammer SOJ_VHF_JAMMER、weapon fwd_sband_jammer SOJ_SBAND_JAMMER、weaponaft_sband_jammer SOJ_SBAND_JAMMER、weapon fwd_xband_jammer SOJ_XBAND_JAMMER、weapon aft_xband_jammer SOJ_XBAND_JAMMER。其接收指挥船的指示对敌雷达进行干扰。

# 6.1.10.2.2. 仿真过程

在本节中可以看到加装了干扰措施后，蓝方的远程预警雷达已经在远距离无法探测到红

方的来袭无人机。下图左图是上一节未加装干扰措施的（一出港就被探测到了），右图是加装了干扰措施的（都快跑跟前了还没有看到）。

![](images/6480ed9a3b0b6cff6ee21e7bb5bed66d3105d8f05852625db653b0adf24894cd.jpg)

![](images/8946e76b4d44ac4ce26bf591fdaab6c50c5f1f1f7d0ae153a4b8d096622bb1c4.jpg)

# 6.1.10.2.3. 本节 PPT 资料

本文为 afsim2.9_src\training\user\10_Other_Topics\bam

\slides\22_AFSIM_BAM_Trng_PerceptionQuantumTasker.pptx 的翻译。

UNCLASSIFIED

![](images/dbc3927b473239fe5cab1c9e0bae3ce919f4600d00a1b371f86d1ad78d275ae3.jpg)

![](images/003cc823a7c50e67b2e8479858bcc015a5e03622d11b05787f9da027f2c2c7df.jpg)

![](images/f86ac86527b0949fd031932d035652208bcf525c17ede13e8da51f54f60ecf8f.jpg)

# AFSIM User Training

# 22－感知与原子任务处理器

Integrity ★Service ★

Excellence

AFRL/RQQD

美国空军研究实验室

DISTRIBUTIOistrtitdtUteidtetractsteestftimntal

AFRL/RQQD

·包括：

－感知处理器  
－原子任务处理器

![](images/bd866cba8b37475ac88f3a3e05ee2a6ba1d4d742254508ae030440357b495837.jpg)

DISTRIBUIONCistititodtUvetAencdthotractorsg9tereqstsfotscumtld AFRL/RQQD 2

![](images/fe3a7bcfd3e11461975ff91b52edafcf7d215a3c4a14043d2846efd1b3b32a29.jpg)

# UNCLASSIFIED

# 感知/原子任务处理器

![](images/36594c354dbdebe8944359d00a8d3fb103e120f0e5cda584e4611b43e836f5ac.jpg)

·感知处理器

－源自脚本处理器  
－用于表示操作者感知的机制  
－功能：

·状态报告  
资产感知建模   
跟踪感知建模

·原子任务处理器

－源自脚本处理器  
－基于威胁感知生成任务  
－功能：

任务/资产对的评估  
任务分配  
利用威胁感知和资产感知

DISTRIBUTIOstrittdvetAgecdtheotractsgOthreqstsfortumtal AFRL/ROOD 3 3

·表示代理对环境的感知

－与系统感知（如雷达/通信缓冲区）不同  
－表示大脑对威胁、同伴等的感知  
－专家级代理能够在脑中处理更多信息，并能定期更新这些信息，而不会产生过多的认知负担  
－感知处理器可调节(以表示不同的认知能力)

·带宽：能够容纳的信息量  
·频率：信息更新的速率

DISTRIBUTIOstrtiuttUeetesdtetractosrstfotcumtsld AFRL/RQQD 4

![](images/1908c9d207aac7cfe504a50a483416831a4ca2cf3c53155007b05fc2f622166b.jpg)

# UNCLASSIFIED

# 感知处理器

![](images/3fc6a9a20b03914fb8ba9195077a029dd9b443d38376a966a538d2eea0fe6e95.jpg)

# WSF_PERCEPTION_PROCESSOR

Navigation: Predefined Processor Types

DerivesFrom:WSF_SCRIPT_PROCESSOR

Script Object:WsfPerceptionProcessor

proCesSOr <name>WSF PERCEPTION PROCESSOR

d processor

DISTRIBUIOstrtitdtUteisdtetractsteesftmntal

AERL/ROOD

<table><tr><td>参数</td><td>描述</td><td>默认值</td></tr><tr><td>threat_update_interval</td><td>查看雷达屏幕的时间间隔</td><td>0 sec(无延迟)</td></tr><tr><td>max-threat_load</td><td>给定的时间可以保存多少感胁</td><td>0(不限制)</td></tr><tr><td>asset_update_interval</td><td>查看资产/同伴状态信息的时间间隔</td><td>0 sec(无延迟)</td></tr><tr><td>max_asset_load</td><td>给定的时间可以保存多少资产</td><td>0(不限制)</td></tr></table>

DISTRIBUTIOstrtiuttUeetsdetractrstftumtld AFRL/RQQD 6

![](images/b424c1b7493ce0abbb2ad36db046b2794c1f6f9619c83a0f35f8c359aff0bad9.jpg)

# UNCLASSIFIED

# 感知处理器参数

![](images/4d2b6e93e068582464ff39b077cbc22049fcd3c4c1260411af2050e8240a8c46.jpg)

<table><tr><td>参数</td><td>完美 (default)</td><td>专家</td><td>平均</td><td>新手</td></tr><tr><td>threat_update_interval</td><td>0 sec</td><td>5</td><td>7.5</td><td>10</td></tr><tr><td>max-threat_load</td><td>Unlimited</td><td>16</td><td>8</td><td>4</td></tr><tr><td>asset_update_interval</td><td>0 sec</td><td>5</td><td>7.5</td><td>10</td></tr><tr><td>max_asset_load</td><td>Unlimited</td><td>16</td><td>8</td><td>4</td></tr></table>

DISTRIBUIONCistibtitodtUvetAgencndthotractors9thereqstfotcumtld AFRL/ROOD 7

# WsfPerceptionProcessor

Navigation:WSF_PERCEPTION_PROCESSOR,ScriptTypes

# Script Methods

Arry<WsfAssetPerception>PerceivedAssets()

Returnsanrfssetperceptioobectssiilartoacksutfd)

Array<WsfTrack>PerceivedThreats()

Returnsanarrayof threat perceptionobjects(tracks).

WsfAssetPerception NearestAsset()

Returnstheassetperceptionobjectthatisclosesttotheplatform'spositionUselsValid)toverifyvaluereturned

WsfTrack NearestThreat()

Retursthethreatperception object(track)thatisclosesttotheplatform'sposition.Tobeconsidered atrackmusth

voidAddExtraCognitiveLoading(double timeDelaySeconds)

Addatimedelay toperceptionupdatingoranyothercognitivetask.Thisisprovidedtorepresentaconditionwhere perceptionupdatingshouldbedelavedBecarefulusingthisifitiscalledfromaregularlyupdatingscriptandadela intervalthannoperceptionupdatingwilleveroccur.Payattentiontothetime valuesyoudelay with.

voidSetAssetimportant(WsfPlatform)

void SetAssetimportant(WsfAssetPerception)

voidSetAssetTypelmportant(string)

Marksthegivenasset(orgiventype)asimportantsothattheassetperceptionwillalways includethatassetThed canperceiveevenifyouvemarkedmorethanthatasimportant

DISTRIBUIOstrtitdtUenteidtractostetftmntal AFRL/RQQD 8

![](images/77f12649388f6a726f97a9b2151ef49288ac4b79aad2a1c74b54662762bf2cf6.jpg)

# UNCLASSIFIED

# WsfAssetPerception

![](images/a1ac134e2783656ef5eb5dd5c37d445d366e182993870a21de4f84aa7c1150ae.jpg)

# WsfAssetPerception

Navigation:Script Types

Derives from:None

# GeneralMethods

int Index()

Thesimulationindexoftheplatformthatthisperceptionrepresents.Thisisusefulwith WsfSimulation.FindPlatform()

double Time()

The simulation time at which this perception was captured

WsfGeoPoint Location()

Perceived location

Vec3Velocity

Perceived wCS velocity vector:inmeterspersecond

Vec3VelocityNED()

Perceived NED velocity vectorinmetersper second

double Speed()

Perceived speed,units: meters/seconds.

Vec3OrientationNED()

Perceived NEDorientationangles (heading.pitchroll:indegrees.

Vec3 OrientationWCS()

Perceived WCSorientationangles(psi,theta,phi)；indegrees

DISTRIBUTIostrittdveetecedthtractsgtheqstfotumntal AFRL/ROOD 9

·指挥官任务分解为逻辑部分：

－任务生成  
－任务与资产配对评估  
－任务分配

·每个组件均为预定义或自定义脚本化

－与任务管理器兼容（双向兼容）  
－提供多种重新分配策略

DISTRIBUTIOstrtiuthdtoUoventAecisdtetractos,g9thereqstfortoumntald AFRL/RQQD 10

![](images/9f17ec64547f72af8a89e42fdb5d20ada0e544dd92768c08838e2dc57b368f48.jpg)

# UNCLASSIFIED

# 帮助文档页面

![](images/f9d5980260caa0062372b3e2aad7f32ef5e3224b98e635f06bb52263ea4d26cf.jpg)

# WSF_QUANTUM_TASKER_PROCESSOR

Navigation: Predefined Processor Types

DerivesErom:WSESCRIPT PROCESSOR

BrotherTo:WSF_TASK_PROCESSOR

ScriptClasses:WsfQuantumTaskerProcessor

proCeSSOr <name>WSF QUANTUM TASKER PROCESSOR

DISTRIBUIOstrtitdtUteisdtetractsteesftmntal

AERL/ROOD

![](images/b3b098855306da226cc8c9a7fea594eb20f17e9411e9b628ffc2a5eaa7a11030.jpg)

# ·分配：

“贪心"算法是否对计算时间敏感？

单次遍历：  
Joe 洗车，Bob 刷围栏，Tim 割草   
总成本 $= \$ 13$

－多次遍历（最小成本，最优利润）：

Joe 刷围栏，Bob割草，Tim洗车  
总成本 $\ l = \$ 10$

DISTRIBUTIOstrtithodtoU.oventAcdotrsugOtrststisumetsld AFRL/RQQD 12

![](images/4ff43d000810b53b3d076ea7b093da7d4959a6e4e0fb0084ed6b48da80793e43.jpg)

# UNCLASSIFIED

# 可用组件

![](images/3dd93bfd8e81c7d89dd96e7e679119c728ed790af1eb2168d8d15c20c0b6c888.jpg)

# 产生器

simple_weapon

simple_jammer

simple_sensor

custom (script)

# 评估器

simple

distance

intercept_time

custom (script)

# 分配器

greedy_isolated

greedy_value

greedy_priority

greedy_profit

optimal_profit**

custom (script)

**Assignment problem, Hungarian Algorithm, $\mathsf { O } ( \mathsf { n } ^ { \wedge } 3 )$

DISTRIBUTIOstritiuttUetisdtetractsrstftumtld AERL/ROOD 13 13

![](images/08d6e4a518095258c79ce7dba1cefc965bddf9cf92868b5d029316c1690cd1bf.jpg)

操作方法：

-感知处理器提供感知信息  
－生成器创建任务  
－评估器考虑任务与资产的配对  
－分配器 为每个任务找到最佳资产  
－重新分配策略的影响：

·先前分配的任务  
·被拒绝的任务  
·新任务

-通过通信进行任务分配/握手

<table><tr><td></td><td>Asset 1</td><td>Asset 2</td><td>Asset M</td></tr><tr><td>Task 1</td><td>value</td><td>value</td><td>value</td></tr><tr><td>Task 2</td><td>value</td><td>value</td><td>value</td></tr><tr><td>Task 3</td><td>value</td><td>value</td><td>value</td></tr><tr><td>Task N</td><td>value</td><td>value</td><td>value</td></tr></table>

DISTRIBUTIOstrtiuttUeetsdetractrstftumtld AFRL/RQQD 14

![](images/959e5fb3d3f6bc77b7b96b1c70f09d1bb65c58f837bd301eca9fa98385b44c0d.jpg)

# UNCLASSIFIED

# 重新分配策略

![](images/06360536f3221b865411c3e1105eaf0e98e426a80981075d00da8e43521d8b10.jpg)

<table><tr><td>策略</td><td>描述</td></tr><tr><td>Dynamic</td><td>理论上，所有资产在每次更新时都可以被重新分配任务，因为评估器和分配器会找到最优的任务分配方案。</td></tr><tr><td>Static</td><td>一旦任务被分配，它将永远不会被重新分配。</td></tr><tr><td>Response</td><td>只有被下属拒绝或取消的任务才会被重新分配给其他人。</td></tr><tr><td>Event</td><td>根据以下三种动因之一重新计算最佳分配：
1. 出现新任务
2. 资产消失
3. 任务被拒绝</td></tr></table>

DISTRIBUTIOstrittdvetAgecdtheotractsgOthreqstsfortumtal AFRL/ROOD 15 15

生成器必须在每次查询时生成所有任务。  
，如果某个任务不再被生成，则会向所有被分配者发送任务取消消息。  
·如果任务分配发生变化：

会向之前的分配者发送任务取消消息。  
会向新的分配者发送任务分配消息。

·如果收到任务完成消息，则该任务不会被重新分配，除非其创建所依据的感知信息比完成消息更新。  
如果从某个特定资产收到任务拒绝消息，则该任务永远不会再分配给该资产。如果可能，会将其分配给其他资产。  
如果资产感知为"系统"，则每个资产系统会接收单独的任务。

例如：missile_type_1可以接收任务4，而missile_type_2可以接收任务7。

WsfQuantumTasks 是根据资源类型（如"武器”、“传感器"等）构建的。  
自定义类型的任务需要使用 SetTaskType()和 SetUniqueld()。  
所有持久性任务（不仅仅是一次性事件）在构建时都需要一个跟踪器。

DISTRIBUTIOstrtiuthdtoUoventAecisdtetractos,g9thereqstfortoumntald AFRL/RQQD 16

![](images/6673a852a73e9e1a69ee4d50ddad6d59201cf1e8dc19ceb639455b5dd194f833.jpg)

# UNCLASSIFIED

# "Extras"

![](images/f6c0a37075b9373a4d2ba2498fa70691400730ca4b25687677c10aa6d6998f67.jpg)

·如果任务多于资产会发生什么？

－默认操作：将任务保持未分配状态，直到资产空闲。  
－如果某个任务未被任何资产正面评估，则不会被分配。

-allocator_extra_tasks <allocator_type>:

对剩余任务和所有资产执行一次分配遍历。  
只要每次迭代找到新的分配，就会继续执行更多迭代。  
一些资产可能会被分配多个任务。

·如果资产多于任务会发生什么？

－默认操作：将资产保持空闲状态（不分配任务）。  
－如果某个资产未正面评估任何任务，则不会被分配任务。

-allocator_extra_assets <allocator_type>:

对剩余资产和所有任务执行一次分配遍历。  
，只要每次迭代找到新的分配，就会继续执行更多迭代。  
一些任务可能会被分配给多个资产。

allocate extra

new allocation found

DISTRIBUTIOstrittdvetAgecdtheotractsgOthreqstsfortumtal AFRL/ROOD T17 17

·干扰器代理的功能：

－在适当的频率上向目标发射电磁辐射。

·独立设计（可独立运行）。

1．机载电子支援措施（ESM）触发WSF_TASK_MANAGER。  
2．任务管理器的TRACK状态控制脚本 找到第一个可用且兼容的机载干扰武器，并分配干扰任务。

![](images/9cddae23df948ed609facc755302f1b943edbe008f7f69d7bc41ac66b05276bd.jpg)

![](images/f475bb7482b74c4be00e92b3157743c9b58e075c8de72a7949c6d0512f8e48e8.jpg)

![](images/bf605a44a6d52a5160facc9b656c35e550e80c6d3c9231561d2d6b02f1ef1d7e.jpg)

![](images/7720a82aa09a2f9eb9aba274194fe72357f6059a4543beb08c175f3248467f09.jpg)

什么条件会导致问题？

DISTRIBUTItrttdvetAgecdthotractsgthqstfortumtal AFRL/RQQD 18 18

# UNCLASSIFIED

![](images/63ccd420d58b4f49dd0028a1a6aa12726b3e8ef247a1752c61006c063ce69c60.jpg)

# 干扰器和电子支援措施(ESMs)

![](images/fca69731c9fa6f5958810cda163282eeefbd9b4bae97b60256ab391e504e72e9.jpg)

·问题：

－需要干扰的系统过多/干扰资源不足  
－协调干扰/避免冲突  
－时间/功率分配

![](images/ac797660255ec64003b8b448125dc3fae4522b58b926815f361984b4b4a90388.jpg)

DISTRIBUTIOstritiuttUetisdtetractsrstftumtld AFRL/ROOD 19

·分配干扰任务存在哪些问题？

－如何在两个或更多资产之间进行协调  
－如何应对意外事件

·突发威胁   
·设备故障   
·失去受保护的实体

·独立设计的难点：

－每个平台（脚本）都必须考虑所有这些情况。  
－每个平台都需要完整的信息。

DISTRIBUTIOstrtiuthdtUontecisdtetractosg9thereqstfortmntal AFRL/RQQD 20

![](images/1ac7a27767188150f1c3b339c6320b27e00c1de12e442aaea9a4993d16c187fc.jpg)

# UNCLASSIFIED

# 解决方案

![](images/4aff045b179784a7fc42caaa948b93a586d2d71b73c5073f80f913f50b714e96.jpg)

·Quantum Tasker提供了一种工具来解决类似的问题：

－通用工具，可用于多种方式，处理多种任务类型。  
－用户只需提供一个脚本，描述干扰器对目标的干扰波束：

·价值可以是：1/距离  
·价值可以是：所需功率  
·其他修改：如果我们已经对多个目标进行干扰，则价值会降低。

－Quantum Tasker分配波束到目标上。

DISTRIBUTIOstritiuttUetisdtetractsrstftumtld AERL/ROOD 21 21

![](images/1997b8b231ec9f5e5bdc35805eea7b2dfcfb7f187d448394257991303c4ad709.jpg)

操作方法，干扰示例：

感知处理器提供感知数据。  
·电子支援措施（ESM）跟踪敌方雷达。  
·生成器创建任务：为每个目标生成干扰任务。  
·动态重新分配策略是最佳选择：评估器考虑任务与资产的配对情况。  
用户脚本用于对每个波束-目标进行评分。  
分配器为每个任务找到最佳资产。  
通常，最优收益分配器（OptimalProfitAllocator）是最佳选择。

·任务分配/握手通过通信完成：  
任务分配或取消消息会自动发送。  
：SOJ（干扰）代理仅执行其任务列表中的干扰任务。

DISTRIBUTIOtrttdvetAgecdthotractsgtheqstfortiumtal AFRL/RQQD 22

![](images/66465b210dfeac4d3f22da0405d6424cf73fbb645963d2edc1f069494382c622.jpg)

# UNCLASSIFIED

# 更新远距离干扰机(SOJ)

![](images/77bab2aa52138bdcbfa2702353bf72b82f1945e37a447d48c71ec8c40ab728da.jpg)

platforms/soj.txt   
```shell
5 include_once signatures/fighter_sig.sigs.txt
7 include_once sensors/esm_rwr/ucav_esigns.txt
8 include_once weapons/jammer/soj_vhf_jammer.txt
9 include_once weapons/jammer/soj_sband_jammer.txt
10 include_once weapons/jammer/soj_xband_jammer.txt
11 include_once processors/soj_quantum_tasker.txt
12 include_once processors/soj_quantum_tasker.txt
13 platform_type SOJ WSF_PLATFORM
14 icon weasel
15 infrared_signed signature FIGHTER_INFRAREDSIG
16 optical_signed signature FIGHTER_OPTICALSIG
17 radar_signed signature FIGHTER_RADARSIG
18 mover WSF_AIR_MOVER
20 default_radial acceleration 2.0 g
21 at_end_of_path remove
22 end mover 
```

DISTRIBUTIOstrittdvetAgecdtheotractsgOthreqstsfortumtal AFRL/ROOD 23 23

platforms/soj.txt   
UNCLASSIFIED   
```txt
25   
260 sensor esm UCAV ESM on   
27 internal link data mgr ignore_same_side ignore_domain air   
30 end_sensor   
32   
33 weapon vhf_jammer SOJ_VHF_JAMMER off   
34 ignore_same_side   
36 end weaponry   
37   
38 weapon fwd_sband_jammer SOJ_SBAND_JAMMER off   
40 yaw 0.0 deg   
41 ignore_same_side   
42 end weaponry   
43 
```

DISTRIBUTIOstrtithdtUoeentecisdtetractostereqestftcmntal AFRL/RQQD 24

![](images/9fa1d8acd5a7b4f010ca932a8fdc94ac405472907ce245b7c9f3d82ee1b1b993.jpg)

# 新的处理器

![](images/372aa8f2a84a887570db966ee36a9bc0b403fb26ccd1d5e6865a7e1fca1acd01.jpg)

platforms/soj.txt   
```txt
72 comm red_comm TEAM_DATALINK network_name red_net internal link data mgr internal_link taskmgr internal_link perception   
78 end_comm   
79   
80 processor taskmgr SOJ_QUANTUM_TASKER   
81 end Processor   
82   
83 processor perception WSF_PERCEPTIONPROCESSOR on scriptDebugWrites off report_interval 10 sec reporting_self true report_to command_chain red_chain commander via red_comm   
89 report_to command_chain red_chain peers via red_comm asset_perception status/messages   
91   
92   
94 
```

DISTRIBUTIostritittUeeedtetractsestftcumtl AFRL/RQQD 25 25

processors/soj_quantum_tasker.txt   
```txt
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
44   
45   
46   
47 
```

![](images/a0001ea27a8110bfd18c63cd43b5a62c3d9b253d63122bb07d12eff071200b15.jpg)

# UNCLASSIFIED

# 处理器实例化

![](images/9bd89d317bc62cb81fc8ca2c23aa356ebf4168d2930575c7df53d27579691377.jpg)

# platforms/ship.txt

```txt
108 comm red_comm TEAM_DATALINK   
109 110 network_name red_net   
111 internal_link data_mgr   
112 internal_link perception   
113 internal_link jammer_tasker   
114 end_comm   
115   
116 processor jammer_tasker JAMMER_LEAD_TASKER   
117 end Processor   
118 
```

DISTRIBUTIostritittUeeedtetractsestftcumtl AFRL/ROOD 27 27

platforms/ship.txt   
UNCLASSIFIED   
118   
119 processor perception WsF_PERCEPTIONPROCESSOR   
120 on   
121 scriptDebugWrites off   
122 reporting_self true   
123 reporting_others true   
124 report_interval 10 sec   
125 report_to command_chain red_chain commander via red_comm   
126 asset_perception status/messages   
127 update_interval 10 sec   
128 on_update writeIn_d("T="，TIME NOW，"，"，PLAfromName()，"assets:");   
130 Array<WsfAssetPerception> assets $=$ PROCESSOR.PerceivedAssets();   
131 foreach(WsrfAssetPerception a in assets)   
132 { writeln_d(" Asset:"，a.Name()，"at T="，a.Time());   
134 for(int i $\equiv$ 0; i < a_SystemCount(); i += 1)   
135 { writeln_d(" ",a.SystemKind(i)，":",a.SystemType(i));   
137 writeln_d(" ready:"，a.SystemReadyAssignment(i));   
138 }   
139 }   
140 end_on_update   
141 end Processor   
142

28

![](images/77872e4a573c5bd6b3ab1db8bfda7dfd13aaee1003de7e35300fc9dc52faa5d0.jpg)

# Quantum Tasker Processor

![](images/ff75dea347c0a9d48508047739305f2708dcac436593f6bb5ce27c93bb3b8e2a.jpg)

platforms/ship.txt   
7 processor JAMMER_LEAD_TASKER WSF_QUANTUM_TASKER_PROCESSOR   
9   
10 // Script to determine the appropriate jammer type based on frequency   
11 script string JammerType(double aFrequency) string jammerType $= \mathrm{""}$ . if (aFrequency < 500.e6) { jammerType $=$ "SOJ_VHF_JAMMER"; } if ((aFrequency > 2000.e6) && (aFrequency < 4000.e6)) { jammerType $=$ "SOJ_SBAND_JAMMER"; } else if (aFrequency > 8000.e6) { jammerType $=$ "SOJ_XBAND_JAMMER"; } return jammerType;   
27 end_script   
28

# platforms/ship.txt

```txt
return 0;   
endScript   
update_interval 15.0 sec   
assetRepresentation resources // [platform, systems, resources]   
reallocation_strategy dynamic   
generator custom JammerTaskGeneration   
evaluator custom JammerTaskEvaluation   
Allocator optimal_profit   
show_taskmessages   
#scriptDebugWrites off   
end Processor 
```

# 将会分配对应的干扰资源

DISTRIBUIOstrtitdtUenteidtractostetftmntal AFRL/RQQD 30

![](images/706e547bcaadc8689d1e084b42a723fef1d009170ed795d4d648c2f02faf1f9d.jpg)

# UNCLASSIFIED

# Generator

![](images/5a60e7191a9f40903533b51c068b12a8521a4aef1486feca1f2badd28c106408.jpg)

# platforms/ship.txt

```txt
28 script ArrayWsfQuantumTask> JammerTaskGeneration (ArrayWsfLocalTrack> TRACKS, ArrayWsfAssetPerception> ASSETS)   
30 ArrayWsfQuantumTask> tasks = ArrayWsfQuantumTask();   
31 //create jammer tasks for enemy tracks   
32 for (int i=0; i<TRACKS.Size(); i=i+1)   
33 { WsfLocalTrack lt = TRACKS.Get(i); if (lt.IsValid() && (!lt.SideValid() || lt.Side() != PLATFORM.Side())) && ltSignalCount() > 0) { WsfQuantumTask task = WsfQuantumTask.Construct(1.0, "JAMMER", lt); task.SetTaskType("JAMMER"); task.SetAuxData("freq", ltSignalFrequency(@)); tasks.PushBack(task); writein_d("jammer task generated for: ", lt.TargetName(), "", updated time: ", lt.UpdateTime()); }   
40   
41   
42   
43   
44   
45   
46   
47   
48 
```

<table><tr><td></td><td>Asset 1</td><td>Asset 2</td><td>Asset M</td></tr><tr><td>Task 1</td><td>value</td><td>value</td><td>value</td></tr><tr><td>Task 2</td><td>value</td><td>value</td><td>value</td></tr><tr><td>Task 3</td><td>value</td><td>value</td><td>value</td></tr><tr><td>Task N</td><td>value</td><td>value</td><td>value</td></tr></table>

DISTRIBUTIotrititdveetencdthtractostqtfortumnthal

AERL/ROOD

platforms/ship.txt   
UNCLASSIFIED   
47 script double JammerTaskEvaluation ( WsfQuantumTask aTask, WsfAssetPerception ASSET) //TOOD -include missile capability in evaluation // for now:just base value on range & whether or not asset as domain capable weapon WsfTrack track $=$ PLATFORM.MasterTrackList().FindTrack(aTask.TrackId());   
50   
51   
52 if(aTask.TaskType $) = =$ "JAMMER" &&aTask.ResourceIsJammer(）&&track.IsValid())   
53 { //TOOD -select one of the systems? or let quantum tasker do it? expect asset rep type: resources ? yes for(int i=0;i<ASSET_SystemCount();i+=1) { if(ASSET_SystemKind(i) $\equiv =$ "jammer") { double freq $=$ aTask.AuxDataDouble("freq"); string requireType $=$ JammerType(freq); #writeIn("track",track.TargetName(),,"frequency ",freq，"required type:"，requiredType); if(requiredType $\equiv =$ ASSET_SystemType(i)) { //its possible that this jammer asset can jam this task's target if(train.LocationValid()） { return(1.0/track.SlantRangeTo(ASSET.Location)); } else if(track.Target().IsValid()) { return(1.0/track.Target().SlantRangeTo(ASSET.Location)); } } Task1 valuevalue 77 } Task2 valuevalue 78 return 0; end-script Task3 valuevalue 80

<table><tr><td></td><td>Asset
1</td><td>Asset
2</td><td>Asset
M</td></tr><tr><td>Task 1</td><td>value</td><td>value</td><td>value</td></tr><tr><td>Task 2</td><td>value</td><td>value</td><td>value</td></tr><tr><td>Task 3</td><td>value</td><td>value</td><td>value</td></tr><tr><td>Task N</td><td>value</td><td>value</td><td>value</td></tr></table>

DISTRIBUIOstrtitdtUenteidtractosteftmntal AFRL/RQQD 32

![](images/4299755bea59e7450f92870a09803f95fbbc9bb237d346d9394d6c3131376127.jpg)

执行

![](images/ba64eb91d72addba9e7ad3a97ce582cbcf26ad75c1b03976717f132d3d922591.jpg)

RUN !!!

现在我们有了电子支援侦测和干扰。

DISTRIBUTIOstritiuttUetisdtetractsrstftumtld AERL/ROOD 33 33

![](images/051c8d2eb2c1a8a270194ed87087d2ae5125ad2ad8be99ca3c18aaa65df0761a.jpg)

SOJ有ESM信号探测

信号指示线（strobes）从SOJ（ESM）延伸到发射器

DISTRIBUTIOstrtithdtUoeentecisdtetractostereqestftcmntal AFRL/RQQD 34

![](images/05eb257e6171be2f6a009a327af451f98ef1886e1c69eeba19dd64ded73b651a.jpg)

# UNCLASSIFIED

# 干扰指示线

![](images/cc34a5a48112eb0ea76d5203fabeb93cf02660d1a11e8c4277f333adfe0028e1.jpg)

![](images/48b6c2a05dac1d8a182c63e9fda9ad4bf9c2f942cebf522ad6b4913b77afc3af.jpg)

DISTRIBUTIOstrtitdtUoventAdeotrasuOtrestftcumetsld AFRL/RQQD 35 35

打印SOJ上接收到的任务信息

一打印任务类型、资源、分配者、被分配者等信息

添加更多电子战（EW）雷达，观察任务分配的变化

提示：

接收到的任务是一个PROCESSOR脚本方法  
一任务有它们自己的方法  
将新雷达分开，以便在Mystic中看到干扰信号指示线（jammingstrobes)

DISTRIBUTIOstrtiuthdtUontecisdtetractosg9thereqstfortmntal AFRL/RQQD 36

![](images/a7b113e2c8b4300edb17f0e870e6f97a2529a40b3b02fdc2e12b26b3986d230d.jpg)

# UNCLASSIFIED

# 不同的任务类型

![](images/4537560fbc2bbd48845172867e4e5440755e98989bfe0be24631b011a58b7adf.jpg)

# ·我需要在不同任务类型之间调整评估吗？

－不需要：你可以为不同的任务类型使用独立的分配器（allocators）。

```txt
415 asset Representation platform   
416 reallocation_strategy dynamic   
417 generator custom FlightLeadTaskGeneration   
418 evaluator custom FlightLeadEvaluation   
419 allocator optimal_profit type PINCER   
420 allocator optimal_profit type WEAPON   
421 #Allocator-extra_tasks optimal_profit   
422 AllocatorExtra_assets optimal_profit 
```

# -或者使用不同的原子任务(QUANTUM_TASKER)

157 processor jammer_task JAMMER_LEAD_TASKER   
159 end Processor   
160   
161 processor taskmgr FL_QUANTUM_TASKER   
162 script_variables   
163 mSelfCreateTasks $=$ true;   
164 #mCreatePincerTasks $=$ true;   
165 endScript_variables

DISTRIBUTIOstrtithdtUoventAcdeotractsuOtrestftcumetsld AFRL/RQQD 37 37

·包括：

－感知处理器  
－原子任务处理器

![](images/9ac9edd2944f84e2626da7d8c07472c7d1848cf9687709b6de327d45d5607a2e.jpg)

DISTRIBUTIOtrttdvetAgecdthotractsgtheqstfortiumtal AFRL/RQQD 38 38

![](images/d7ff118b79e9f33e4bd5cc0f5c96c685f138f818af428e35d31fe1d40a916793.jpg)

DISTRIBUTIostrittdveetecedthtractsgtheqstfoumntal AFRL/ROOD

# 6.1.10.3.行为树与追踪行为 23_AFSIM_BAM_Trng_BehaviorTreesPursue

# 6.1.10.3.1. 本节想定解析

本节想定资源在以下目录下：

afsim2.9_src\training\user\10_Other_Topics\bam\scenarios\floridistan\23_floridistan_behavior_tree s\run_course.txt

行为与智能体建模培训的每一节都是在上一节的基础上的，而且想定较为复杂，因此要先了解上一节的内容。本节是在上一节的基础上给蓝方小队新增了一个空中打击分队打击来犯的无人机和远距离干扰机。下面来对其兵力做详细的分析。

# 6.1.10.3.1.1. 蓝方新增兵力

# 1) 两个飞机指挥所(FLIGHT_LEAD)flight_lead_north、flight_lead_south

每个都有两个战斗机下属如下图：

![](images/e8ebd97ad5a972f7fcaa81317018ce4a235b7ae1bdae38852f35e2ecb002ce9f.jpg)

其核心的任务分配逻辑是在 FL_QUANTUM_TASKER 处理器中如下：

□ 判断目标和我方管辖的下属的战机的距离，谁离的近谁去打

# 2) 四架战斗机(STRIKER)cap_north_1~2,cap_south_1~2

▪ 其核心逻辑是在 task_mgr 当中，其是个 WSF_QUANTUM_TASKER_PROCESSOR

□ 若要打击的目标传感器跟踪质量符合要求，又在武器的打击范围之内，则进行发射打击

# 6.1.10.3.2. 仿真过程

第一阶段：蓝方远程预警雷达探测到了红方干扰机与无人机，图中白线。

![](images/be2569f78ae2b459c5c44793883105c8f3f4127be8206a3c1cb86425208b86f5.jpg)

第二阶段：由于红方干扰机 soj_north 与 soj_south 对蓝方远程预警雷达实施干扰，对远方的无人机失跟了，近处的干扰机还跟踪着，红线是干扰线，白线消失了。

![](images/ccbb01bb3d76c634f2fa0685d914bc46750751cdd4b71180440fc1ccabd9e8c4.jpg)

第三阶段：四架战机 cap_north_ $\displaystyle 1 ^ { \sim _ { 2 } }$ 和 cap_south $\cdot ^ { 1 \sim 2 }$ 上的几何传感器探测到了这两架干扰机，开始升空打击。打击完了再把四架无人机也打下来，战斗结束。

# 6.1.10.3.3. 本节 PPT 资料

本文为 afsim2.9_src\training\user\10_Other_Topics\bam\slides\23_AFSIM_BAM_Trng_BehaviorTreesPursue.pptx 的翻译。

![](images/b5c3c1906b516b70eada3713b1572bde057062c649836c3de999450040382960.jpg)

![](images/119e477a590213b9f9dc7d19c1c956310d6df0e8a32cd213c9709991e12b776a.jpg)

![](images/ba8fae0743016c93ac259b96c2b32b25a88c6c1902edcf49fad3e1463cd03c62.jpg)

Integrity ★Service ★ Excellence

# AFSIM用户培训

# 23－行为树与追踪行为

AFRL/RQQD美国空军研究实验室

DISTRIBUTIOstrtithdtUteiesdtetractsteresftimntal AFRL/RQQD 1

·包括：

－描述AFSIM中的行为树  
－构建行为节点  
－修改行为树

![](images/335451c4c50d3d89be3a63f0187461c0c8e467fb4c78c0e73281634ef605e1b0.jpg)

DISTRIBUTIOstrtiuttUeetesdtetractosrstfotcumtsld AFRL/RQQD 2

![](images/7e33d673fca96bc7233c6fb6e112694ac333a03eba0166d2b2e0c30444c086e0.jpg)

# UNCLASSIFIED

# 行为树

![](images/b6a6cabb66d529d7e1460e17919f8de6823ef54acfee66b434e77b9dc626071c.jpg)

·理论

－行为树

·应用

－添加蓝方的CAP（战斗空中巡逻）单位（打击者）。

·使用行为树实现预定航线及追踪目标的行为。

－添加蓝方的飞行领队。

·使用与舰艇相同的Quantum Tasker（原子任务管理器）。

·添加简单的 武器任务（WEAPON tasks）。

DISTRIBUTIOstritiuttUetisdtetractsrstftumtld AFRL/ROOD 3 3

# ·行为树

－ 将行为定义为小型的、可操作的单元。  
－定义了将行为连接在一起的分支，并描述它们之间的关系。  
－ 定义了决定执行哪些行为的过程。  
－ 在行为树的顶部有一个不可见的"根"节点。

# ·行为 (Behaviors)

－ 定义了某些具体的动作或操作。  
－ 自我感知，即知道执行其动作所需的条件。  
－在RIPR（某种实现框架）中表现为脚本定义。

# ·分支（或中间节点）翻译

－每个节点可以通过某种类型的分支拥有子节点。  
－ 分支的类型包括：

·并行(parallel)：允许多个子节点同时执行。  
·顺序(sequence)：按照从上到下的顺序依次执行子节点，直到某个节点失败或全部完成。  
·选择器(selector)：从上到下依次检查子节点，执行第一个成功的节点，若失败则继续检查下一个节点。

DISTRIBUTIOstrtiuthdtUontecisdtetractosg9thereqstfortmntal AFRL/RQQD 4

![](images/f549defae58754cd57e63ccd37d05e6f8cafbff377d7d7368f14af2343977db6.jpg)

# UNCLASSIFIED

# 行为树概念

![](images/1b6a32044645dd9e279a49549852391148f7fde6bf62aae3df645986dbd87fe3.jpg)

![](images/496487dd986f1f245c8c1e9d10118d6b3d3f37decb31500c32198b9cfb904a6a.jpg)  
行为树

目标是决定哪些叶子节点需要被执行。  
·逻辑从根节点开始。  
·每个节点会依次评估其子节点。  
·中间节点可能不会评估其所有子节点。

DISTRIBUTIOstrtiuthodtoUovetAecisadtetractos,g9tereqstfrtmntald AFRL/ROOD 5 5

·每个节点需要具备两个必要的部分：

-前置条件 (precondition):

·一个脚本块，返回一个布尔值（true 或false）。

－执行逻辑 (execute):

·一个脚本块，仅当前置条件返回true 时才会运行。

·节点的执行条件：

－节点必须被行为树访问到。  
－节点的前置条件必须通过（即返回true）。

·对于行为节点（叶子节点）：

－它们有唯一的名称，可以通过名称引用。  
－它们的前置条件是显式的，由用户通过脚本定义。  
－它们的执行逻辑/动作是显式的，由用户通过脚本定义。

DISTRIBUIONCistititodtUvetAencdthotractorsg9tereqstsfotscumtld AFRL/RQQD 6 6

![](images/4b99de47c38ce41e23961a80346df58561c94e0854e12a2ee43d54a19622d6bb.jpg)

# UNCLASSIFIED

# 行为树操作

![](images/bd9449e7e2606cd13b931b2d31d4cdf9137a5a1ad0b28ddd1282fc6669028cf7.jpg)

·对于中间节点：

－它们的前置条件默认通过。  
－它们的"执行"方式是简单地运行其子节点（可以是没有子节点、部分子节点或全部子节点）。

_中间节点有三种类型：

·并行节点(Parallel Node)：尝试运行所有子节点。  
·选择器节点(Selector Node)：依次尝试运行其子节点，直到有一个成功运行。  
·顺序节点(Sequence Node)：依次尝试运行其子节点，直到有一个失败。

－为了嵌套的目的，如果中间节点的任何一个子节点被运行（即前置条件返回"true"），那么该中间节点会返回true。

·行为树的执行：

一行为树的执行从不可见的根节点开始。  
－这个根节点是一个并行节点类型。

DISTRIBUIONCistibtitodtUvetAgencndthotractors9thereqstfotcumtld AFRL/ROOD 7

![](images/de054ca0cab19c3e3a2a7da67c3d1f69a3b3ac358d199c633909dc50486803a9.jpg)

选择器节点 (Selector Nodes)

选择器节点只尝试运行一个子节点。  
每次评估一个子节点的前置条件。  
在第一个成功的子节点处停止。  
如果任何子节点的前置条件通过（返回true），选择器节点返回true。  
非常适合在多个动作中选择一个动作。  
将最重要的选择放在最前面！

# 顺序节点 (Sequence Nodes)

顺序节点尝试运行所有子节点。  
每次评估一个子节点的前置条件。  
在第一个失败的子节点处停止。  
如果任何子节点的前置条件通过（返回true），顺序节点返回true。

非常适合用于指定依赖行为（即一个行为依赖于另一个行为的成功）。

![](images/5cd60deb16c3cafcf0b9e7f16ed46e616df90a73a0d6f4a836784c4874f8e35d.jpg)

DISTRIBUTIOstrtiuttUeetsdetractrstftumtld AFRL/RQQD 8 8

# UNCLASSIFIED

![](images/1015d1fc6d7ebdd6018d480ea9ed1427df8894eb590307ac1b03ccf60bcbcc88.jpg)

# 中间节点示例

![](images/0a7e979c090eb0dd7567b9fd0f467d67e882269ccc88f5f09418770f473a1613.jpg)

并行节点 (Parallel Nodes)

·并行节点尝试运行所有子节点。  
·每个子节点的前置条件都会被独立评估，且不依赖其他子节点的返回值。  
·如果任何子节点的前置条件通过（返回true），并行节点返回true。  
·非常适合用于将多个行为组合在一起。

![](images/ebad3a38f55f0d24c513dec625114450f9b2f9d1af542a602e0ba40147884850.jpg)

DISTRIBUTIOstrtiuthodtoUovetAecisadtetractos,g9tereqstfrtmntald AFRL/ROOD 9 9

![](images/e54321c50ef484a4a5dbfc4de0e77877e669daacc3cb3f053d11707e41ec7f26.jpg)

加权随机节点(weighted_random nodes)

加权随机节点会随机选择一个子节点，选择的概率由子节点的前置条件返回值决定。  
适用于当任何动作都可以执行时的场景。  
，与“run_selection”一起使用效果很好。  
·与“make_selection"一起使用效果很好。

![](images/1947474f354db511d88145df52e3a0ae9a35669cedf29956c30357682d4122f9.jpg)

优先级选择器节点(priority_selector nodes)

优先级选择器节点会选择前置条件返回值最高的子节点。  
适用于当执行顺序未知时的场景。  
·与“run_selection”一起使用效果很好。  
·与“make selection"一起使用效果很好。

DISTRIBUTIOtrttdvetAgecdthotractsgtheqstfortiumtal AFRL/RQQD 10

![](images/46d742e288511a60862c7a1e06810e021d43696d73de94f93cbfe6b22dff1327.jpg)

# UNCLASSIFIED

# 行为树事件

![](images/0d94a818f96f54622ba7e6d8c90dc0baac036fe0cc84dd5707865d5aca8f2c77.jpg)

事件日志输出:

```ruby
1 event_output  
2 file replay.evt  
3 time_format h:m:s.1  
4 enable BTREE_NODE_CHILDREN  
5 enable BTREE_NODE_EXEC  
6 end_event_output  
7 
```

DISTRIBUTIostritittUeeedtetractsestftcumtl AERL/ROOD e11 e11

# BTREE_NODE_CHILDREN

# 在初始化时输出一次

Example:

```txt
00:00:00.0 BTREE Node CHILDREN red_3 324 selector 2 325 326 "d:/CoDev/projects/fuel_mgmt_test/redfighter.txt" 1326920272 
```

# BTREE_NODE_EXEC

# 在状态发生变化时以及以固定的时间间隔输出结果

Example:

```txt
00:04:02.0 BTREE Node_EXEC agent 4 395 engage-target 0 "no acceptable target to shoot at!" 
```

DISTRIBUTIOstrtithodtoU.oventAcdotrsugOtrststisumetsld AFRL/RQQD 12

![](images/3c43f1fb7b7406128f4075742bd4be53e611e6cc7f14be406528c02f4434e2ee.jpg)

# UNCLASSIFIED

# 行为树－测试1

![](images/ec58661b4a5b646224c40c407613a418796f4efd89c38f1195a2bdbcf0555d2f.jpg)

![](images/0be9ff91f72a5158e72bf00db97bf160a0b32fd218cbfbc1bf5b0e4cde6a2ff9.jpg)

假设性（如果被访问）。

哪些节点会被执行？

DISTRIBUTIOstritiuttUetisdtetractsrstftumtld AERL/ROOD 13 13
![](images/eaa03ac2bb9c7aa2f218b3a3d9c6fd17bcf3df53f07b68cfe491831702dc213d.jpg)

![](images/b760e387e7272c4829b931964c957ccbc7cc48d2851edb91c257377aaaac84a6.jpg)

![](images/04cca1dbaa07ce739c04ebf4b42d783e7f183025ddb340ce9438778a19ac3894.jpg)

DISTRIBUTIOstrtithdtUoeentecisdtetractostereqestftcmntal AFRL/RQQD 14

![](images/a1a398e6572957f19e662bce25d98d29da7e2866509054711a77e34419d5c3ac.jpg)