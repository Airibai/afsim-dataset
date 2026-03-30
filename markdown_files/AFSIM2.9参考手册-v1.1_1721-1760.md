- 查看任务分配器（Task Assigner）中的任务块（Task blocks）：  
- 每种之前讨论过的任务类型都有一个对应的块。  
- 复选框的含义是什么？

- 它们表示基于受任务者资源的可用任务类型。  
例如：如果受任务者是一个发射器（launcher），那么“Fire”和“Custom”将是可选项。

![](images/0fd63f5ac8ca66ffc737e683b7eee87a3e18b94423ea047cb3307706b0c39459.jpg)

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

23

![](images/c9fed18e02d8f31be4b34d2ddee951cdf555dfa614e43314473cb8f791dbfb83.jpg)

# 实践：任务分配（Task Assigner）/任务状态浏览（Task Status Browser）

![](images/5f3eb9473c1666102c9fee176bf06e083de774e28a9d6fb0e894836824aa4cd1.jpg)

- 在此示例中，您只能分配一个自定义任务（Custom task）：  
  - 受任务者没有武器、传感器或干扰能力。  
- 展开自定义任务块（Custom task block）。  
- 处理器（Processor）下拉菜单允许您选择受任务者的处理器以发送任务。

- 选择“taskMgr: LARGESAM_BATTALION_TASK_MGR”。

- 点击“Assign”（分配）。

![](images/4bd815fd56e2acaaed7712532469934fd17a86a30421b344776c876cf68649b2.jpg)

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

- 在仍然选择10_iads_cmdr的情况下，查看任务状态浏览器（Task Status Browser）：

注意，任务位于Assigned（已分配）部分。

现在，选择3500_large_sam_battalion。

注意，任务位于Received（已接收）部分。

- 完成此幻灯片后，关闭 Warlock 窗口，但保持 Wizard 打开。

![](images/e71658305d0d1b2402b056afae3544db41839ae580030443767675263e35348d.jpg)

![](images/3adc450155e063f8c1255806f453f84f62f2bb913447fe999551a72e74bd9ecf.jpg)

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

25

![](images/61b7bd930a7590f3be5e31f4b7f354753be9ca3e685f2b06fab951d5d58e4f48.jpg)

# 任务实践: 最后一点

![](images/dcdc08ccac48d0ae47fc042491239394da1637da3ad86216533d7b984a2318f8.jpg)

- 我们只扮演了 IADS 指挥官的角色：  
- 我们没有修改营级单位的脚本化行为和任务处理器。  
- 平台中同时存在具有脚本化行为和没有脚本化行为的混合情况是可以的。

![](images/36f3acf898af75446ec048fb9eae6ce69fdc5845de6ff838a5c8ddff572e0dae.jpg)

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

- 允许用户执行包含在 .txt 文件中的 AFSIM 脚本:  
- 显示包含“WARLOCK_”前缀的全局和平台级脚本。

![](images/29155f529203c1ff51298985f74a3aa7e5be45ff62afdd6742abd37cf6952b16.jpg)  
If included in platforms/bomber.txt:

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

27

![](images/c0bd610c0b483bcb5e4dd44dd84cf4988e515060644a449e38ea8df20903a798.jpg)

# UNCLASSIFIED

# 对话框构建

![](images/83086cbbed1df3d2a707eb6eca9ad6ba08195c7058ebad2ac0a4c3a3e52c3733.jpg)

If included in platforms/bomber.txt:

- 允许用户创建、编辑和删除自定义对话框以执行AFSIM脚本：  
- 在创建用户友好的方式来执行非内置功能/应用程序的脚本时特别有用。

script void GoToPlatform (WsfPlatform aPlatform) double targetLat $=$ aPlatform Latitude(); double targetLong $=$ aPlatform.Longitude(); PLATFORM.GoToLocation(targetLat, targetLong, PLATFORM.Altitude()); end_script

![](images/cefb499ed43887c98672f80757acb5d432d40e440ad0c2fb2c7b261d42d6f765.jpg)

![](images/05ded85038dc20c06eb738cea6e95888464d8452acd121d957f2ed534abef39f.jpg)

- 在 Wizard 中打开文件 platforms/bomber.txt:  
- 在 platform_type BOMBER 块中输入下图所示的脚本。

platforms/bomber.txt

30 processor fire-em BOMBER WEAPON RELEASE   
32 end Processor   
33   
34 script void GoToPlatform (WsfPlatform aPlatform) double targetLat $=$ aPlatform.Latitude(); double targetLong $=$ aPlatform.Longitude(); PLATFORM.GoToLocation(targetLat, targetLong, PLATFORM.Altitude());   
38 endScript   
39   
40 # execute at_time 100 sec absolute   
41 # Weapon("red_gps_bomb_1").FireSalvo(MasterTrackList().TrackEntry(0),2);   
42 # Weapon("red Glide_bomb_1").FireSalvo(MasterTrackList().TrackEntry(1),2);   
43 # end_execute   
44

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

29

![](images/3f47f6c90d6ff5d876cc18970d418b85f08d923d16f3637f838a032bc0612524.jpg)

UNCLASSIFIED

# 实践：对话框构建（继续）

![](images/4208217de7ef03672068a648a07c5802a2a71eb75e5c1fe05e40a00df62016fc.jpg)

- Run with Warlock!!!   
- 打开Options -> Preferences -> Dialog Builder   
- 选择New

![](images/6c7105d665d503f99da7232461672dd675f47964d30c775b99d9b0b1aff2d6d4.jpg)

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

- 将对话框名称设置为“Go To Platform”：  
- 将 Max Rows 和 Max Columns 都设置为 1。

- 注意，这会更改底部部分的框数量。

- 将按钮大小（Button Size）更改为“square (large)”。

- 注意，这会更改底部部分框的形状。

- 点击带有加号的框。

![](images/f8dd08c27a10c6ea0b2e3ba32bb60354d577ae3cb6aa409d07d0e7d4acde4998.jpg)

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

UNCLASSIFIED

# 实践：对话框构建（继续）

31

![](images/53aab00dc1681345fefc199d9c83e010368e859b1dba85149862d20b23c93bb5.jpg)

![](images/c5a847126f6a22fc4c0c748b06edd6dbb61d3240ca7337d6f571aef89d24bfb6.jpg)

- 将Display Name改为“Go to Platform”

![](images/f1f3e4d25ecc266873615fdf4b6ee3aa8fe263776dab42522edc49e724759439.jpg)

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

- 此幻灯片中的字段必须与您在 Wizard 中为其构建对话框的脚本相匹配：  
- 将脚本名称更改为“GoToPlatform”。  
- 将上下文（Context）更改为platform。  
- 将平台类型（Platform Type）更改为“BOMBER”。  
- 将参数数量（Number of Arguments）更改为1。  
- 勾选“Prompt User to Input Values”（提示用户输入值）。  
- 在脚本构建器（Script Builder）和对话框定义（Dialog Definition）弹出窗口中点击OK。  
- 在首选项（Preferences）弹出窗口中点击 OK。

![](images/b45d2a86619bc7520fbeede7cee586be18a6e9313b99d883c3c5be88f2436dff.jpg)  
platforms/bomber.txt

![](images/8054c8f3da14800c65c8f0697aef5b1e06434b410d345f9e6abadb8c4d6e1f2d.jpg)

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

# UNCLASSIFIED

# 实践：对话框构建（继续）

33

![](images/4eece3d41c80054be8dba53c5ccc1d74ea2545fde384061741a464ef938f7c52.jpg)

![](images/f88915330f1e4e0dc376035fe4485653e347b7ac9bfd43de841671f69a87e497.jpg)

- 在“视图”（View）菜单中，找到并启用“Go To Platform”：  
- 选择bomber_2。  
- 点击对话框。   
- 在“脚本输入”（Script Inputs）弹出窗口中，使用十字准线在地图显示中选择200_ew_radar。点击OK。

![](images/90d8401de13b9ce44689216ffe5caf00dcfc4745a72b4c2479ee8afda872e19c.jpg)

![](images/f5704e0b34dc603c353ea7664e08c078cd5f534186b1728ba71cff910330a2e8.jpg)

![](images/8c0183e595ac59e45b16951e40e06c8652636c04498de789d607e49b350096e3.jpg)

![](images/79c29a6fe92017da854e2fe5a2060c32d9b3abafa783c15765996a1ecd1f2f7e.jpg)

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

- 轰炸机转向所选的雷达目标：

![](images/eacf5f2b7ed878b214568ac744a469fceee9fa8b1c9e8e6790b5a57847bccd9d.jpg)

- 完成此幻灯片后，关闭 Warlock 窗口，但保持 Wizard 窗口打开。

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

35

![](images/30bbca483aabdec97ad09bb2ab63d8a10e07b4eeff147518e1807498e16f2aef.jpg)

UNCLASSIFIED

# WsfPrompt

![](images/e719ffa9861b70d459689106fb592726f93e8040e1f6483dbdcc35e99a81053f.jpg)

- 脚本可用于在 Warlock 中创建对话框：

- “弹出窗口”用于向用户显示信息。  
- 您可以选择在提示时通过对话框执行脚本。

![](images/1a6b842e87d0d7cd9024f7f13cbd94be84c6d15e74d7b1faecfa0e679f9333b1.jpg)

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

- 这些 WsfPrompt 方法将显示一个提示：

```txt
static void Display(string aTitle, string aMessage, Array<string>aScripts, Array<string>aButtons) 
```

```txt
Scripts are executable from the dialog 
```

```txt
static void Display(string aTitle, string aMessage) 
```

```txt
No scripts are executable from the dialog 
```

- 您还可以在提示弹出时暂停模拟。

- 一旦用户在提示中做出选择，模拟将重新开始运行。  
- 使用以下其中一种 WsfPrompt 方法:

```txt
static void DisplayAndPause(string aTitle, string aMessage, Array<string>aScripts, Array<string>aButtons) 
```

```txt
Scripts are executable from the dialog 
```

```txt
static void DisplayAndPause(string aTitle, string aMessage) 
```

```txt
No scripts are executable from the dialog 
```

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQDD.

37

![](images/91cecad10c1d3a24c7a3cff0f42085368f9a3beff9027e27509bfc9c6f3292ec.jpg)

# 实践：WsfPrompt

![](images/6b50b072af16b2d55913c86c1c3167a243e3d8f57ba8f2b1e9f562045c069587.jpg)

- 在 Wizard 中打开文件 scenarios/blue_laydown.txt:  
- 将下方显示的脚本和执行块添加到汽车平台定义中。
- 保存您的更改。  
- 使用 Warlock 运行！

```txt
scenarios/blue_laydown.txt 
```

```txt
script void turnAround()
    PLATFORMTURNToRelativeHeading(180);
end_script
execute at_time 5 s absolute
WsfPrompt.DisplayAndPause("WARNING", "I forgot to turn off the oven!", {"turnAround"}, {"Turn the car around!"});
end_execute 
```

- 在模拟时间 5 秒时,下方的对话框会出现：

- 对话框会暂停模拟。

- 点击“Turn the car around!”（让汽车掉头！）。

- 结果：汽车开始向相反方向行驶。

完成此幻灯片后，关闭 Warlock。

![](images/15d94f4ca2e993ec0bf69d723f697a299fe48254699e7de05378a1e16346476e.jpg)

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

39

![](images/361b679159707e9795c6fdf3387c063f6cb9e071bf2950262968b7b993e77877.jpg)

# 杂项 Warlock 功能

![](images/3a0aab6e2ac5f4592e3d9f52c69c2da32ccd725743ac249cc5913c16eb86228d.jpg)

- 演示模式（Demo Mode）

- 允许您在场景完成后自动重新启动场景。

- 记分板（Scoreboard）

- 显示武器性能的统计数据。

P6DOF

允许用户手动控制模拟。

- P6DOF是一种高保真运动类型。

- 下视显示（Heads Down Display）

- 类似玻璃驾驶舱的显示，用于选定的平台。

- 网络交战浏览器（Cyber Engagement Browser）

- 总结当前网络交战情况的表格。

![](images/5311da8d534016aa2ff3718609b80eeef5ebf291bc38071590669c01d68e73ad.jpg)

![](images/3b8b84407ebe4c0bafb84cc9c99a1928891a1c7c7a3d96083dcabfe5c233c2a3.jpg)

![](images/6b3ca1c33035f92ba155c53659f6cd63e072308066e1851d05448688f39eb6de.jpg)  
Heads Down Display

Cyber Engagement Browser   

<table><tr><td>Attack Type</td><td>Attacker</td><td>Attacker Team</td><td>Victim</td><td>Result</td></tr><tr><td>TEST_attack</td><td>attack2</td><td>blue</td><td>target1</td><td>Attack Failed</td></tr><tr><td>TEST ATTACK</td><td>attack1</td><td>red</td><td>target1</td><td>Attack Failed</td></tr><tr><td>TEST_attack2</td><td>attack1</td><td>red</td><td>target1</td><td>Attack Failed</td></tr><tr><td>TEST_attack2</td><td>attack2</td><td>blue</td><td>target1</td><td>Attack Failed</td></tr></table>

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19.

Other requests for this document shall be referred to AFRL/RQQD.

- 包含以下内容:

- Warlock中独特的特性  
如何使用这些特性

![](images/c2c079a113a66f068dd9a740c53546819bd9af50f5a10e429bc8bb72b87b6098.jpg)

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

UNCLASSIFIED

![](images/f098af5d1bd7c6d0310406830137cda84f404d5febf7253a5a45dcc9bf2b0500.jpg)

问题？

![](images/670f4835f6ae2ce89c029b06644cf181e17f0f23156bcc91aac613795e7ff110.jpg)

![](images/500634cc6f9094aaa475e8703d045ebd91dfbe29e9a55d6feadc08c37035c1d4.jpg)

A. 武器浏览和最大请求计数（Weapon Browser and Maximum Request Count）  
B. 任务分配器/任务浏览详情（Task Assigner/Task Browser Details）  
C. 使用脚本浏览的步骤（Steps to Using Script Browser）

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

43

![](images/1b62d5805c2317154c574eaac149ecdf505b9d03e41102fdd2d9a337a0c4f891.jpg)

# A) 武器浏览和最大请求计数

![](images/f860f85e7c75835135424c42c6b4c8b27a1196671c90fcbb8309c8fafcc4e363.jpg)

·常见问题：我尝试通过多个命令同时发射同一武器，但武器无法发射

- 查看武器的 maximum_request_count（在 Wizard 的武器定义中）。  
- 如果请求计数过低，可能会限制该武器的发射请求数量。

- AFSIM会忽略该命令，导致发射失败。

- 最大请求计数应至少足够大，以处理您同时发出的请求数量。

![](images/41a16f79edf5b445c1f5110e09e9e368a5b675e5288aa21f5939a066b01cc34f.jpg)

maximum_request_count <integer-value>

specifies the maximum number of salvo firing requests (WsfWeaponFireSalvo or WsfTaskManagerFireAt) that may be active simultaneously.

- 任务状态浏览器和任务分配器处理相同的四种任务类型

<table><tr><td>任务类型</td><td>描述</td></tr><tr><td>Fire</td><td>被分配者（拥有一个或多个武器）将对目标轨迹（track）发射武器。</td></tr><tr><td>Jam</td><td>被分配者（必须具备干扰能力）将开始对目标轨迹进行干扰。</td></tr><tr><td>Track</td><td>被分配者（至少拥有一个传感器）将开始对目标轨迹进行跟踪。</td></tr><tr><td>Custom</td><td>其他任务：允许您编写自己的任务类型。</td></tr></table>

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

# UNCLASSIFIED

![](images/853dc0ea7d7ec90d08cebccfb42c9031310c7ad956d2d5e2be2139f93f6a28a1.jpg)

# B) 任务状态浏览器中的任务类型

![](images/b9cf2a79aac8c1023263c0ee5592d09cfc6c83495e67bec174e55d6341f4d93e.jpg)

- 每种任务类型在任务状态浏览器中显示不同的信息：

<table><tr><td>任务类型</td><td>Info in Column 1</td><td>Info in Column 2</td><td>Info in Column 3</td><td>Info in Column 4</td><td>Info in Column 5</td><td>Info in Column 6</td></tr><tr><td>Fire</td><td>Assignee</td><td>Weapon Name</td><td>Task Type</td><td>N/A</td><td>N/A</td><td>N/A</td></tr><tr><td>Jam</td><td>Assignee</td><td>Jammer Name</td><td>Task Type</td><td>Frequency</td><td>Bandwidth</td><td>Beam #</td></tr><tr><td>Track</td><td>Assignee</td><td>Sensor Name</td><td>Task Type</td><td>N/A</td><td>N/A</td><td>N/A</td></tr><tr><td>Custom</td><td>Assignee</td><td>Processor Name</td><td>Task Type</td><td>N/A</td><td>N/A</td><td>N/A</td></tr></table>

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

- 在 Wizard 中，编写一个以“WARLOCK_”开头命名的全局或平台级脚本。

- 这里显示的脚本包含在轰炸机平台类型中。

- 在 Warlock 中运行场景后，在“视图”菜单中启用脚本浏览器。

![](images/7e3aab8e798878b46b2ecead38927329c6f3fed7c7e8bf8261b252822ea74bde.jpg)

![](images/da044a2c8c803e974c07b549c92adbf6773b01765b9d92ad8f7311a1466a372c.jpg)

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

47

# UNCLASSIFIED

![](images/e26f9d33c2e3e077d6f0bd4422d982c53a3e0b21986bb0aae9235e847df6c5f5.jpg)

# C) 使用脚本浏览器的步骤（继续）

![](images/e0a65aee2e00e91c6ce8845e3c0a0361246514998db18d2faea8d7d16c842992.jpg)

- 选择脚本适用的平台。

-您将在脚本浏览器中看到该脚本出现。

![](images/91774a875629cd8be54009c1e132cb8163dcd0c423124349802b151f19a29254.jpg)

- 在浏览器中选择脚本名称。

- 填写您的输入参数。

![](images/d59360a1f328d1e48febf11f9de87aa596dc8353ae0cfa0ba27c1e707b4dd671.jpg)

- 选择“执行”。

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQQD.

48

# 6.1.8. 回放工具Mystic特性8_Mystic_Features

# 6.1.8.1. Mystic 概览 12-Mystic_Overview

本节不涉及想定，只有PPT资料，下面为afsim2.9_src\training\user\8_Mystic_Features\slides\12-Mystic_Overview.pptx的翻译。

![](images/bbe3066238a2e3170907ec9380ef09f061a488360cf4d598412ff243aef63e02.jpg)

Integrity $\star$ Service $\star$ Excellence

# AFSIM用户培训

# 12-Mystic概览

本文档由杨石兴翻译，该资料做为《AFSIM2.9参考手册》的一部分。没有《AFSIM2.9参考手册》的加杨石兴微信领取：13324598743

AFRL/RQQD

# 美国空军研究实验室

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQQD.

1

![](images/683548f1e8bdced1f73344c19becac58933f70cf930eda80da4f64a60e6a5b81.jpg)

UNCLASSIFIED

# 学习目标

![](images/a29b0784b24d9c1598019bf7ec6b11733b83e0dbafe5e27b3e93ea86f4ae2561.jpg)

- 包括以下内容

- Mystic是什么  
- Mystic的基础特性

![](images/807b19004bf23a320185e41bbd0508954239430e4caefdbadc274e7500c4eb7a.jpg)

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

- 复盘回放工具  
- 在地图中回放  
- 后处理和分析的工具

![](images/42c59e57f93628ba7af5d9733c1a5dd6d27a6c2f3dccebf6a7b751c051019046.jpg)

![](images/e5e8d806982b5c704ddb991bc0d1e597bcb57647c66646817e9a991148762139.jpg)  
DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

3

![](images/e6caa263415be92581163233d4d44bebb0412122431f8ead6ab6a28efd53ffff.jpg)  
UNCLASSIFIED

# Mystic的主要应用

![](images/89df179c5cdddcde2ad2cbdbe4b96dcefaf460f4e05d1900be36e605020b3e9a.jpg)

- 展示平台, 平台历史, 传感器包络, 平台交互, .....

![](images/02270f21025f56804ffe7c51ffd4caa0e462ec2f894986f59456d81d3a8dd720.jpg)

![](images/628587f5d00382d2ac3c7acb9ea33bcf03f16201730e7ecdf34470a92a82acbc.jpg)

![](images/58dad178036cf05905405670d3d6b0aec2d7586320b1c7eba39f4a83df8d202c.jpg)

![](images/f52fbdfcd3449b452a8edcc55982360d873c9dba16d8bdf6594b99069b42b880.jpg)  
DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19.   
Other requests for this document shall be referred to AFRL/RQQD.

- Mystic包含针对如下数据进行分析的工具:

- 平台数据  
一 传感器数据  
- 武器交战数据

- Mystic可以用图和表的方式来展示数据

- 也可以导出成.csv文件

![](images/25e7faa10aa9bc3257feabdb433a677ad9c88a941172f61527a7df08e3420f74.jpg)  
DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19.   
Other requests for this document shall be referred to AFRL/RQQD.

# UNCLASSIFIED

# 事件输出文件Event Pipe/.aer

5

![](images/6efe44479906232084619717b1f5ceaab536223fc991c07bb94a9cb8df315e9e.jpg)

![](images/bbb8f229d7d20be661f99e9701e7d0a1783534fbea0a149aefc7ab7e4ac67b9c.jpg)

Event Pipe: AFSIM创建一个文件，包含了仿真过程中所有的关键事件，

用此进行完整回放

- Mystic可以读取该事件文件(AER文件)  
- 下面是基本的事件输出定义：

```txt
event_pipe file output/warlock_rvscenario.aer use_preset full disable DRAW end_event_pipe 
```

- 其它关于事件输出的命令Event Pipe Commands

- use_preset [default | low | high | full]   
- 配置输出消息  
- enable/disable   
- 指定启用/禁止某一具体事件输出到 aer 文件中

- Default & low 相同  
High 添加了：

- TRACK_UPDATE   
-MESSAGE_received   
MESSAGE_TRANSMITTED   
-MESSAGE_HOP

- full 添加了：

- DETECTION_ATTEMPT   
- USER_ACTION

default & low:

BASE_DATA   
- ENTITY STATE   
DRAW   
- DETECTION CHANGE   
COMMENT   
- TRACK

high:

BASEDATA   
-ENTITY STATE   
DRAW   
- DETECTION CHANGE   
COMMENT   
- TRACK   
XIO   
- TRACK UPDATE   
MESSAGE RECEIVED   
MESSAGE RECEIVED:MESSAGE TRANSMITTED   
MESSAGE_HOP

full:

BASE DATA   
- ENTITY STATE   
DRAW   
- DETECTION CHANGE   
COMMENT   
- TRACK   
XIO   
- TRACK UPDATE   
MESSAGE RECEIVED   
MESSAGE RECEIVED: ·MESSAGE TRANSMITTED   
MESSAGE HOP   
- DETECTION ATTEMPT   
- DETECTION_A
- USER ACTION

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

# UNCLASSIFIED

# Event Pipe Preset 命令

7

![](images/016593bf5435460cd2b29e7c9f4a8ac682549fc50cc421abe38b12d2201337bf.jpg)

- 打开以下文件夹

AFSIM-2.8.0-win64 > training > user > 8_Mystic_Features > scenarios > floridistan

- 在Wizard中打开warlock_mystic/startup.txt,  
- 如下添加该命令“use_preset_full”在event_pipe块中  
- 运行！！！

warlock_mystic/startup.txt

![](images/41f5e32e6ce6b938fad51939885b0894266a0b58473e22a8dc0d9198de575bee.jpg)

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19.

Other requests for this document shall be referred to AFRL/RQQD.

# 方法1: 从Wizard的Output窗口中

在使用Mission运行完后，Output窗口中选择“Results”

![](images/4978ae3e23efbc2771151e8df82d4400b39e2607f666d0fbe3acdd0c729d2c01.jpg)

在下拉框中选择.aer文件

![](images/ba28ad92d2f6eb1aa3426b8e97d4aafef931d70e50efaead3a84534fcf4d300b.jpg)

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

UNCLASSIFIED

# 打开一个.aer文件

9

![](images/e18e8c7f65aa7040052af9b48f4bcb718b4d65bd955a95728a653295bd03b218.jpg)

![](images/9f1476179816da61ff595e72bd503d3a38b6c7fc0ac2663b7a4abf76a413bb0a.jpg)

# 方法3: 从Mystic中

打开mystic.exe

在弹出窗口中可以看到最近打开（Recent Recording）或者点击Browse来浏览到具体的aer文件

![](images/f6420390f79ca9364af1268c985efc6538492ac98c013ac51f0df8ebdbe51955.jpg)

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

![](images/b6eda7fe694ce01721c7dd1d6cb70bcc4d3f8df37dc0fa11a7f4a8d24e262f40.jpg)

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

Simulation Clock

11

![](images/d211f1ef65d518a4300e278b024c3db83bc18acbf5db330de35597aeb02b5b40.jpg)

# UNCLASSIFIED

# 时间控制

![](images/7239a5f3597d6d04ce835e5313323782e3f75e14163046f7949d798267390f9f.jpg)

![](images/df1ae8593ef1f6d981ede8cbd72f1b37029c23fd65e182b280756e976c2998e7.jpg)

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

- 包括以下内容

- Mystic是什么  
- Mystic的基础特性

![](images/8ff781a05b37bb735afa392a03dd56f49aaba496f197439474e22adb72e6c6f2.jpg)

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

UNCLASSIFIED

![](images/6db593be2e6311e851fa8dbcc87ae8d66cc55793fd2a592b06855c34747b14bf.jpg)

# 问题

![](images/bd99184d319a538464893da729ddd5fa9c027a61a0b47c3c7dec8e7783c094cc.jpg)

![](images/26b79beeed12e9f7de893b184e602f33fea31df09a00971a4953801cbfaa4cda.jpg)

6.1.8.2. Mystic 和 Warlock 共同特性 14-Mystic_and_Warlock/Common_Features

参见：6.1.7.2Mystic 和 Warlock 共同特性 14-Mystic_and_Warlock/Common_Features

# 6.1.8.3. Mystic 特性 15-Mystic_Features

本节不涉及想定，只有PPT资料，下面为afsim2.9_src\training\user\8_Mystic_Features\slides\15-Mystic_Features.pptx的翻译。

![](images/9a55cceefe7c9babf1bbf744287804c5f20ec7ba01636c00226c787d42a70aad.jpg)

UNCLASSIFIED

![](images/7f71d322692f4f199e6251f5324f9964a40cabac4616947dd9779a463897b03a.jpg)

![](images/b8447e1f43b1eb7bdf37e5fbe90cbe04e3a04da8fc10a276c11ec209a361bd43.jpg)

Integrity $\star$ Service $\star$ Excellence

# AFSIM用户培训15-Mystic特性

本文档由杨石兴翻译，该资料做为《AFSIM2.9参考手册》的一部分。没有《AFSIM2.9参考手册》的加杨石兴微信领取：13324598743

AFRL/RQQD

美国空军研究实验室

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

1

![](images/740c18bf5546318676ead8db13782c36456214bfa4e560dbed23597b072aaba5.jpg)

UNCLASSIFIED

学习目标

![](images/3d8b0aa233e0299cd4e665029a969abdf6cc44945b323bdfe208846934de1d40.jpg)

- 包括:

- Mystic独一无二的特性  
- 怎么使用这些特性

![](images/6a196e9cfa524b698661fd5e59b9c501bd112bb704dfc08e10ea0a6b3468ba1b.jpg)

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

- Mystic是实现以下功能的工具：  
- 可视化回放仿真记录  
- 提供事后分析功能  
- 其独一无二的特性见右表

<table><tr><td>范畴</td><td>特性</td></tr><tr><td>调整可视化结果</td><td>首选项Preferences</td></tr><tr><td>事后处理分析</td><td>*Platform Details Plot</td></tr><tr><td></td><td>Script Data</td></tr><tr><td></td><td>Bookmark Browser</td></tr><tr><td></td><td>Waterfall Plot</td></tr><tr><td></td><td>*Sensor Detection Report</td></tr><tr><td></td><td>Event List</td></tr><tr><td></td><td>*Engagement Statistics</td></tr><tr><td></td><td>*Event and Track Tracing</td></tr><tr><td></td><td>Result Statistics</td></tr></table>

<table><tr><td>* Denotes an associated hands-on activity</td></tr></table>

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

UNCLASSIFIED

# Mystic相关首选项(PReferences)

3

![](images/d61b3dd524cc3103829b7fd3477b8840a0c5bffab0a9d9629803ab4dc0d48259.jpg)

![](images/ea338b6a9fa7ec9655bef55708f1ec8926b0368b0891796e326f11fb5217c7e8.jpg)

<table><tr><td>首选项(Preference)</td><td>具体功能</td></tr><tr><td>Map -&gt; Interpolation</td><td>决定平台出生点/位置的具体方法</td></tr><tr><td>Application -&gt; Memory Usage</td><td>出于内存性能考虑，一次加载多少数据</td></tr><tr><td>Time Controller</td><td>·调整当前仿真时间
·编辑显示的时间格式
·选择事件文件结束时发生的操作</td></tr></table>

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

- 可以使用Plot tool（绘图工具）来对platform details中的数值信息进行绘制和分析

![](images/ad275496f4e209dfe40102d5435f7b7810f4deed63e649bcbe7db8a76651bd7a.jpg)  
实践：平台详情绘制

5

![](images/dd3daa09d64c78aa3008dc2408dda4114f41a3b7feb15bff3336c6d15d39f346.jpg)

- 如果没有在Mystic中打开warlock_mysticscenario则跟随以下步骤打开  
- 打开下面的文件夹

AFSIM-2.8.0-win64 > training > user > 8_Mystic_Features > scenarios > floridistan

- 在Wizard中打开warlock_mystic/startup.txt,并设置为启动文件  
- 使用Mission运行warlock_mystic/startup.txt 然后使用Mystic打开aer文件

![](images/a5b3c8e3ca1dcfa65ee672997fc868c8172961b989941ad5e2b3cfea0a749837.jpg)

![](images/e9355700f99c4e4e7cbe18ee0e1fe82f6cf1632af759814bef47c3d2f75edf8c.jpg)

- 进行到675s, 然后暂停  
- 选择平台

"bomber_new_red_glide_bomb_1_3"

- 在Platform Details中右键Speed  
- 选择

"Plot

bomber_new_red_glide_bomb_1_3”

- 也可以在Tools menu中打开绘图工具(Plot Tool)

![](images/9d4d6e8aa707571353474126d688494cc236b57122dc6be0e9a3c1b1befd9b00.jpg)

![](images/313af40bdaa221622d2f4f0c33dfd70b1804fed13add1c8269349db422ecdbe9.jpg)

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

# UNCLASSIFIED

# 实践：平台详情绘制

7

![](images/9aa57c7bec9dd8812f7a5b23652ce885fc93a25906a62d22aa1dc8d72d88d40b.jpg)

![](images/6b463fbd64a6a6e1b8867d0d9eb2ba6c6580a7ed45e066685dabfa42fd9e2e8a.jpg)

![](images/740b1184a7d254e1f1bc86730dc68588556332bfda745eb022308bdfaa9d52ce.jpg)

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

播放仿真  
- 竖线代表当前的仿真时间  
- 暂停仿真

![](images/6b00abd4ff3bdde39fac89e4fe71318d6db4199e7a676bd0d8d9f49f9c322b57.jpg)  
DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

- 在筛选框中输入“glide”  
- Ctrl + 单击多选第1个3个最后一个如下图 - 第3个结果是最初绘制在里的

![](images/15ac77ea10e9d80ad7c21951d1a68ade6d13dc988c58dd9fdf01c6d6e9afb2ad.jpg)

- 现在多个记录都在绘制工具中进行绘制

![](images/127d6faafe72d40289eb2a0aefe1154dc4240b5ed46cbd44962477f6ab0a4cc1.jpg)

9

![](images/1c30621c12a700ccd1b3e308bceeb7b143f9e1bf64088c856482595679226d98.jpg)

# UNCLASSIFIED

# 实践: 平台详情绘制

![](images/3b9a0978a01a687fb06824c26292bbe76b0ce607773c84c47816678bec076bce.jpg)

# 在X Axis下拉菜单选项中选择“Lifetime”

绘制会基于平台的寿命而非仿真时间

![](images/d89cc66ce71a24690e36e4ed64f7dcfc97e2823200299f11ee0d6fd0102d42f5.jpg)

![](images/55ccbeaaa2a5cdbdc36098eaa269956b5d193be54b6dd2b6961c6866f19ed24d.jpg)

- 轴下拉菜单内容的意义是什么？

每个选项代表一个不同的平台细节数值条目。  
- 意思是：你可以通过绘图窗口切换你正在绘制的平台细节。

将Y轴更改为加速度

(Acceleration)。将 X 轴改回时间 (Time)。

![](images/644f50ef0b59defa7f63dcfe3edd5f2c7aa34c757488f5a776109f24927faece.jpg)  
DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

- 当你右键单击绘图时，会出现各种选项：  
- 导出数据（Export Data）

- 你可以将此绘图（以及Mystic中的许多其他绘图）的数据导出为CSV文件。

- 显示图例（ShowLegend）  
- 系列颜色（Series Color(s))

- 你可以更改每个单独绘制系列的颜色。

![](images/a1be63881a3e7f6e02141785699bf0f50f7223fced8b0d53da2f67d1732c1d0a.jpg)

![](images/2da9cafb84cfd1558ba2bed21bf33aeffc997a8e735224cb6b79e96ff63d3926.jpg)

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

11

![](images/3f22beb1801cd7b8afc9fb7cb9bf5258419c816688edee6972aaecce9ccd0460.jpg)

# 平台详情绘制：设置采样率(Sample Rate)

![](images/9d45c5519d383b0de461f21b0317963367e1a4ddc3715c3f30ad6c8ac485c200.jpg)

- 设置绘图数据的期望采样率（以秒为单位）。

- 默认值 $= 0$ 秒（显示所有可能的数据）。

![](images/de3949d228f4dd7a4ac35c00ae0d9900ab25f4010154347f34a8de7319d6f92c.jpg)  
Sample Rate $= 0$ s

![](images/6ff52f9a3ead7297cee67eeb8105f9ce132103aa093ab7faa48bc46ce97a5840.jpg)  
Sample Rate $= 30$ s

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

- 右键单击绘图主体部分  
- 选择数据视图（Select Data View）  
- 显示绘图中所有点的数值。  
与绘图中不同颜色的系列一样，数据按平台分隔。  
- 你可以像在绘图视图（Plot View）中一样使用过滤器和轴功能。  
- 你还可以从数据视图中导出数据。  
- 关闭绘图。

![](images/a258dfc7334c5d6655ae4420bd73ee29bfbe949adab093df94132f37f1f92d1c.jpg)

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

UNCLASSIFIED

# 实践: 平台详情绘制

13

![](images/81807700f856b531feffc9fd7799cfedf7d5610f8d41994c5004ae738131044d.jpg)

- 在平台浏览器（Platform Browser）中找到并选择轰炸机（bomber）。  
- 在平台详情（Platform Details）中，右键单击纬度（Latitude）。  
- 点击“绘制平台类型 = BOMBER”（Plot Platform Type = BOMBER）。  
- 生成一个单一的纬度与时间的绘图（latitude vs. time plot）。

- 显示关于两种BOMBER类型平台的信息。

![](images/4c193186d17fb3375640b35b9d9e4abde348ac2b9e0ee0b5026abdb23058164f.jpg)

![](images/7afbd11da9de0bbc9c118b7b4c00a9e30ce7a0595507a018d98b27fa8fdd8281.jpg)

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19.

Other requests for this document shall be referred to AFRL/RQQD.

·问题：黑线的终点代表什么？  
·问题：红线的突然上升代表什么？  
- 答案:

- 黑线的终点代表平台“bomber”被击落。  
- 红线的突然上升代表平台“bomber_2”正在转向。

完成此幻灯片后，关闭Mystic，但保持Wizard打开。

![](images/8616cfd0c8162138acd8c4aaf575d2dccab83bb6bb07d37fb9b5d701ed29aa3a.jpg)

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

UNCLASSIFIED

# 平台详情：脚本数据

15

![](images/37ef5ede751f95cce74330adc927fcd2b128253f12a9535f56d47a3bb6201edf.jpg)

![](images/d73a3acb2b989ee8ad63566c31a8da1b23e915607a2dd729b4a39a34a8f65456.jpg)

- WsfEventPipe.Record() 可以通过脚本将信息推送到平台详情（Platform Details）。  
- 这些信息会被更新，并且可以像默认的平台详情信息一样进行绘图。

![](images/4071f07b2510c7893b3ef8ccc92a4330540540ff693fe8e8a89e77d7cd846cf8.jpg)

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

- WsfEventPipe.AddBookmark() 可以通过脚本向 AER 文件添加书签。  
- 书签浏览器（Bookmark Browser）显示按时间排序的书签列表。

- 它允许你将模拟推进到书签对应的时间点。

![](images/76c912e75557c3474873418bf68ed7d1a48acdc4e3819ea101bbf76a0dfd262a.jpg)

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

17

![](images/d75195756aafb28343fc8a8f5f3160d5ab03004422bdc501a6d78b4e3458ca0d.jpg)

UNCLASSIFIED

# 瀑布图(Waterfall Plot)

![](images/17129c5f35b62c26e6e937bb677d7bc45a58fb6a9b40c32c6912de9a20892264.jpg)

- 对于选定的平台、交互类型和交互对象过滤器：  
- 显示交互活动的时间点。  
- 事件类型：

被探测/探测中  
- 传感器跟踪/传感器正在跟踪  
- 本地跟踪/本地正在跟踪  
被干扰/正在干扰

- 交互对象过滤器（一次使用一个过滤器）

- 阵营（Side）  
- 平台类型（Platform Type）  
- 类别（Category）  
- 平台（Platform）

![](images/271fda6d4852f4121df9bfa229635a5ded2a93fa55376b3a0721726188538d1c.jpg)

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

- 提供传感器探测数据的表格和图形视图。  
回答以下问题:

- 我的探测交互线发生了什么？  
- 为什么干扰不起作用？

![](images/7bd932441de8404e46d2711fd89809e4111994489580c86216861c0be633d8cf.jpg)

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

19

![](images/41a4c535b4b61860104b7d5c9d6c657dca4cd3334fb7952b1a19d3640e1575c1.jpg)

# 实践：瀑布图（Waterfall Plot）和传感器探测报告（Sensor Detection Report）

![](images/722563c98977777250c0c5617e078184895b04e98597a452672fc1bd57c2fd17.jpg)

- 在 Wizard 中，打开文件 scenarios/red_laydown.txt。  
- 找到bomber_2的平台定义。  
- 将其当前的路线注释掉。  
- 按照示例输入新的路线块。

scenarios/red_laydown.txt

![](images/62507ee2dc4c3d8e272f129fdc67a865c564d528852fe716132c454faef010dd.jpg)

- 在Mission中运行模拟并打开.aer文件。  
- 在 Platform Browser中右键单击

300_ew_radar。

- 选择 Waterfall Plot（瀑布图）。

![](images/203233541f8148de0a28cb3c2c7869ccee61979901b590bc17111ab9a2d54208.jpg)

![](images/8d5c7a12eeebf9ec4820b29509abcbf1c09afffc36377a8a74d9fae5d15f0713.jpg)

![](images/5bce96868ad874919e3bf6fadb5bb6fdd20fa79b75e75430ea4165782c2d0f94.jpg)

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

21

![](images/ca676c07980dcf3df8f14fd9a6ea6d5daa68317cfbb52b7b32e0ce572c77da93.jpg)

实践：瀑布图（Waterfall Plot）和传感器探测报告（Sensor Detection Report）

![](images/afdbbeca47d04c685132672b33062a3579acfb5427f2359852fb85878d03635b.jpg)

- 在图表窗口中，选择“Detecting”作为交互类型，并选择“Platform: bomber_2”作为交互对象过滤器（Interactor Filter）。  
- 注意到其中的间隙。

- 这些间隙显示了雷达停止探测到bomber_2的时间段。

![](images/2be74281922bf0a9c86b14a9c0324dfb4da8248866bae2e8433042b0c7490eba.jpg)

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

- 传感器探测报告（Sensor Detection Report）提供了对传感器行为的进一步洞察。  
- 在 Platform Browser 中右键单击 300_ew_radar。
- 选择 Sensor Detection Report。

![](images/00a6471b6f50bacac675fd976d3c3af74792e9ac07fb94f1707febbaad6e3708.jpg)

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

23

![](images/5fd522dcfe1877e9873a9795581f0b17a84c60df8c10b8c4da53cea6cc9f6e6d.jpg)

实践：瀑布图（Waterfall Plot）和传感器探测报告（Sensor Detection Report）

![](images/8d732b53daf5b90e4e370d2b4adedbce78383902cfb16cb5eba437be0b204b69.jpg)

- 在窗口顶部的 Target 下拉菜单中，选择 bomber_2。

![](images/02ba8612ca7dae0e119d176e8a41a6f62d12feb54547d99929a5a15b002636b6.jpg)

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

- “Plot:” 选项允许你仅绘制所选列的数据。

- 右键单击 req. pd 列的标题。

- req. pd 代表 Required Probability of Detection（所需探测概率）。  
- 选择“Plot: req. pd”。  
绘图将仅显示 req. pd 与模拟时间的关系。

<table><tr><td>req. pd</td><td>status</td><td>r to taz /dec</td></tr><tr><td rowspan="2">0.663302</td><td colspan="2">Choose columns</td></tr><tr><td colspan="2">Plot: req. pd</td></tr><tr><td>0.535232</td><td colspan="2">Add to plot: req. pd</td></tr><tr><td>0.782479</td><td colspan="2">Hide column</td></tr><tr><td rowspan="2">0.788221</td><td colspan="2">Export visible columns</td></tr><tr><td colspan="2">Export all columns</td></tr><tr><td>0.866075</td><td>OK</td><td>0</td></tr><tr><td>0.00542345</td><td>OK</td><td>5.6112e-15</td></tr><tr><td>0.729037</td><td>OK</td><td>-3.60633e-15</td></tr></table>

![](images/1bb48548c11388f449d2c6897091931bfb6e6783042ac2a923993006bf2551c7.jpg)

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

![](images/d951885c65bc96101791806ce408692b40fded715e8d7c2b29ca1676e464e4b3.jpg)

# 实践：瀑布图（Waterfall Plot）和传感器探测报告（Sensor Detection Report）

25

![](images/2b8e9934fa6b6a9a9cad51a94b7bbcf5ad04f5ec1d465ac5966ef1532b6dab13.jpg)

- “Add to Plot:” 选项允许将所选列的数据与已绘制的数据一起显示。

- 右键单击“pd”列的标题。

- “pd”代表Probability of Detection（探测概率）。

- 选择“Add to plot: pd”。  
- 结果：图表中同时显示 req. pd 和 pd 的数据。

<table><tr><td>pd</td><td rowspan="2">Choose columns
Plot: pd</td></tr><tr><td>0.90114</td></tr><tr><td>0.913156</td><td>Add to plot: pd</td></tr><tr><td>0.924064</td><td>Hide column
Export visible columns</td></tr><tr><td>0.933917</td><td>Export all columns</td></tr><tr><td>0.942275</td><td>0.00542245 OK</td></tr></table>

![](images/51bd663cb6d339d4959b7587686a462960f7d1770f6eedc52c15a70955f06cb7.jpg)

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

- 让我们将瀑布图（Waterfall Plot）与传感器探测报告图表（Sensor Detection Report Graph）进行比较：在传感器探测报告图表中，pd（探测概率）低于req. pd（所需探测概率）的点，与瀑布图中的间隙相吻合。

- 在模拟中发生了什么导致了这些变化？

![](images/3f31780011070179e707e0930896245f4c982de84a5fc68a4db5112ccd243b8d.jpg)

![](images/fb8ba454bde485149ac392caceab30e098be0c614fdcb4d9662cc98118715239.jpg)  
DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

27

![](images/3f4abd2b59ab23ed8de9110fac38ced91f65c6f9290ccdbd20b0cc14ec360044.jpg)

实践：瀑布图（Waterfall Plot）和传感器探测报告（Sensor Detection Report）

![](images/fcc6268b1cc2077cbe8b9ca769bfd94ec8ac4ca5f4f4f6e765308b142971dae5.jpg)

- 传感器探测报告（Sensor Detection Report）的“status”列解释了探测失败的原因。  
- 在这里，我们由于信号弱（Low Signal）和地平线遮挡（Masked Horizon）而未能成功探测到目标。

![](images/72b3cd722baa8a772f3c83205d5becd9632d09719da10727f57be138877d99a4.jpg)  
DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQQD.

- 关闭两个图表。  
- 将时间推进到 350 秒。  
- 选择bomber_2。  
- 播放模拟。  
- 在 Platform Options 中为 bomber_2 打开传入探测线（Incoming Detection Lines）。  
- 注意在 Platform Details 中轰炸机的下降高度。  
- 当轰炸机下降到足够低的高度时，探测线会消失。

- 在这种情况下，探测失败是由于目标被地平线遮挡（Masked by Horizon）所导致的。

![](images/54c37c8f7c662d5686c58cb74443b3ed1bf31e84f8b0c326a30e09aff00d00e5.jpg)  
Scenario Time = 367 seconds

![](images/51d140c10c1c69871d840c289063803b551db0bc0b1b35d6f7badd5ae5cbd548.jpg)

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

29

![](images/01b1413f8b61421790f1d46a4113a3c8cf6d43c5ce4fff779593ad7a71b88b48.jpg)

# 实践：瀑布图（Waterfall Plot）和传感器探测报告（Sensor Detection Report）

![](images/0b1b397b94bbe3604c31e534f96fa956395c560d0e3d6edb2b4f241774479320.jpg)

- 关闭Mystic。  
- 在 Wizard 中，打开文件 scenarios/red_laydown.txt。  
- 删除你在bomber_2平台定义中写的新路线。  
- 取消注释原始路线。

- 平台上的路线应与图片中的路线一致。

- 在Mission中运行该场景并打开.aer文件。

![](images/6db53d87710de6895820c22f9d04da7dba3dc0380446d1c4891399171a318833.jpg)  
scenarios/red_laydown.txt

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

- 工具（Tools） $\rightarrow$ 显示事件列表（Show Event List）  
- 显示所有当前加载的模拟事件，呈现在一个可筛选、可导出的表格中。

![](images/5f9436734fa31345756fea95a608f11ea18d5dd5cf8d9c37163589b308f67333.jpg)  
DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

![](images/0d03d9c95a742294b84f2b2d87cc8b07984f4d9075998687a0de1af6b5aa9043.jpg)  
UNCLASSIFIED

# 事件列表：编号列

31

![](images/15138b392b13ba2d0a4c42fd8d9970489ba981de7201bbbdc82f713e2613d5d7.jpg)

- 问：为什么有些列是用数字表示，而不是标签？

答：所有事件都有一些通用的信息类别（例如：类型、时间、平台）。但是，不同的事件也有独特的信息，这些信息没有专门的列来表示。

- 如果将鼠标悬停在编号列中的某个单元格上，字段名称将会显示出来。  
- 如果将筛选条件设置为单一事件类型，任何编号列都会变成带有名称的列。

<table><tr><td colspan="2">time</td><td>simulation</td><td>type</td><td>platform</td><td>interactor</td><td>track id</td><td>component</td><td>8</td><td>9</td></tr><tr><td>1</td><td>0</td><td>1:1</td><td>MsgExecData</td><td></td><td></td><td></td><td></td><td>C:/Users/clyon/...</td><td>C:\AFSIM-2.5.0....</td></tr><tr><td>2</td><td>0</td><td>1:1</td><td>MsgScenarioData</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>3</td><td>0</td><td>1:1</td><td>MsgPlatformInfo</td><td>car</td><td></td><td></td><td></td><td>1</td><td>CAR|WSF_PLAT...</td></tr><tr><td>4</td><td>0</td><td>1:1</td><td>MsgPartStatus</td><td>car</td><td></td><td></td><td>mover</td><td>mover</td><td>false</td></tr><tr><td>5</td><td>0</td><td>1:1</td><td>MsgPlatformInfo</td><td>satellite</td><td></td><td></td><td></td><td>2</td><td>SATELLITE|WSF_...</td></tr><tr><td>6</td><td>0</td><td>1:1</td><td>MsgOrbitalEle...</td><td>satellite</td><td></td><td></td><td></td><td>7.07262e+06</td><td>2.00106e-05</td></tr><tr><td>7</td><td>0</td><td>1:1</td><td>MsgPartStatus</td><td>satellite</td><td></td><td></td><td>mover</td><td>mover</td><td>false</td></tr><tr><td>8</td><td>0</td><td>1:1</td><td>MsgPlatformInfo</td><td>tank_1</td><td></td><td></td><td></td><td>3</td><td>TANK|WSF_PLA...</td></tr><tr><td>9</td><td>0</td><td>1:1</td><td>MsgPartStatus</td><td>tank_1</td><td></td><td></td><td>mover</td><td>mover</td><td>false</td></tr><tr><td>10</td><td>0</td><td>1:1</td><td>MsgPlatformInfo</td><td>tank_2</td><td></td><td></td><td></td><td>4</td><td>TANK|WSF_PLA...</td></tr><tr><td>11</td><td>0</td><td>1:1</td><td>MsgPartStatus</td><td>tank_2</td><td></td><td></td><td>mover</td><td>mover</td><td>false</td></tr><tr><td>12</td><td>0</td><td>1:1</td><td>MsgPlatformInfo</td><td>ship</td><td></td><td></td><td></td><td>5</td><td>SHIP|WSF_PLAT...</td></tr><tr><td>13</td><td>0</td><td>1:1</td><td>MsgPartStatus</td><td>ship</td><td></td><td></td><td>mover</td><td>mover</td><td>false</td></tr><tr><td>14</td><td>0</td><td>1:1</td><td>MsgPlatformInfo</td><td>bomber</td><td></td><td></td><td></td><td>6</td><td>BOMBER|WSF_...</td></tr></table>

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

- 事件列表数据可以导出为 .csv 文件  
- 导出步骤:

- 右键单击任意单元格。  
- 选择“Export to CSV”（导出为CSV）。

<table><tr><td colspan="2">time</td><td>simulation</td><td>type</td><td>platform</td><td>interactor</td><td>track id</td><td>component</td></tr><tr><td>1</td><td>0</td><td>1:1</td><td>MsgExecData</td><td></td><td></td><td></td><td></td></tr><tr><td>2</td><td>0</td><td>1:1</td><td>MsgScenarioData</td><td></td><td></td><td></td><td></td></tr><tr><td>3</td><td>0</td><td>1:1</td><td>MsgPlatf</td><td colspan="2">Make filter for [type] == MsgPlatformInfo</td><td></td><td></td></tr><tr><td>4</td><td>0</td><td>1:1</td><td>MsgPartS</td><td colspan="2">Export to CSV</td><td></td><td>mover</td></tr><tr><td>5</td><td>0</td><td>1:1</td><td>MsgPlatformInfo</td><td>satellite</td><td></td><td></td><td></td></tr></table>

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

33

![](images/4a81f6ed7b4d0d89179b477b8f0d70adea135e4269a2e5f244b3efb876feff2d.jpg)

# UNCLASSIFIED

# 事件列表：绘制类型

![](images/bcc051f4711275af7ef6931910632f258fda5a497d364d7fc4b58aeff93a959f.jpg)

- 对事件列表想绘制的列点右键弹出plot进行绘制

<table><tr><td>platform</td><td>interactor</td><td>track id</td><td>component</td><td>Pd</td><td>9</td><td>10</td></tr><tr><td rowspan="2">300_ew_radar</td><td rowspan="2">bomber_new-g...</td><td rowspan="2"></td><td rowspan="2">ew_radar</td><td rowspan="2">0.99923</td><td colspan="2">Make filter for [Pd] == 0.9992305040359497</td></tr><tr><td colspan="2">Export to CSV</td></tr><tr><td>3520_large_sam...</td><td>bomber_new-g...</td><td></td><td>ttr</td><td>0.97244</td><td colspan="2">Plot Pd</td></tr><tr><td>3520_large_sam...</td><td>bomber_new-g...</td><td></td><td>ttr</td><td>0.972543</td><td></td><td></td></tr></table>

- 允许你将列与时间进行绘图，同时调整图中显示的系列数据

![](images/5c2ec89b333490a7f459b79d3a8470a3e3cda45b7b88e96ec12950c46aeafdfd.jpg)

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

- 方法1: 点击右上角的加号

![](images/cf6c18c770e0c21dcef38470731cde60175b46f38a6b31d3224359e1aa08351f.jpg)

- 然后在以下框中根据需求选择填入信息

![](images/a93828e44bda65bc6c37ba0bb35384167b353bed98bdc4472ddd2fa4c97b9350.jpg)

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

35

![](images/db13f187a75a02384e247ab1ed849188cb89bf51fea20b3bf59f529cc348176b.jpg)

UNCLASSIFIED

# 事件列表：添加筛选器

![](images/9a63995fd385be99d29a75acd4bf883e91792e120212658f867b56fa7c97c39c.jpg)

·方法2：右键单击某个单元格即可按列值进行筛选。

<table><tr><td colspan="2">time</td><td>simulation</td><td>type</td><td>platform</td><td>interactor</td><td>track id</td><td>component</td></tr><tr><td>583</td><td>90.7137</td><td>1:1</td><td>MsgEntityState</td><td>100_radar</td><td colspan="3">Make filter for [platform] == 100_radar_company</td></tr><tr><td rowspan="2">584</td><td rowspan="2">90.7887</td><td rowspan="2">1:1</td><td rowspan="2">MsgEntityState</td><td rowspan="2">10_iads_c</td><td colspan="3">Export to CSV</td></tr><tr><td colspan="3">Plot platform</td></tr></table>

- 结果：筛选器会显示在事件列表的顶部。

- 你也可以在这里编辑筛选器。

![](images/41ae97af1c4032d5b28b61ef65a9c214dbaa945dec6f28ae015a85f0daf63c0a.jpg)

- 点击这个减号删除筛选器

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

- 启用（Enabled）：

顶部：

未选中时，将显示所有行。  
选中时，仅显示符合所有列出条件的行。

单个筛选器：

未选中时，将忽略该条件。  
选中时，仅显示符合该条件的行。

- 反转（Invert）：

逻辑：

所有原本会显示的内容现在不显示，反之亦然。

顶部：

选中时，会反转所有逻辑。

单个筛选器：

选中时，仅反转该筛选器的逻辑。

![](images/8c52712e6e344da0e513dcbf5b0c9bbb105021f3f91f37f05e8e8e65a4038f6d.jpg)

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

# UNCLASSIFIED

# 交战统计

37

![](images/92e4a8cd9e84586e3ccbd3e73f9fcaceef877f3c8e2bd30116716126449c9c80.jpg)

![](images/c0a39b6100d74e4d7228ee618daefba1ed5ea72af2cb56f5ec50a69a0e2c47dc.jpg)

- 允许你使用以下工具分析场景中所有武器交战的数据：

- 绘图  
数据表  
- 事件追踪

![](images/2b13a918671a6acfebd40b3c8e8d5efebccf6d7f51c4cdab3e1d371ebc83cef6.jpg)

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

- 你可以通过右键单击列中任意单元格并选择“Plot”来绘制该列的数据：  
- 绘制包含分类（非数值）数据的列时，会生成饼图。

![](images/a4c083b88fe61fa1cb93bbee12e51acd7e8cb2569790919051facfea7fab15fc.jpg)

- 绘制包含数值数据的列时，会生成折线图。

![](images/4677be0b59cd8d394106a38bfe017d12930dd9ba22d53f83052455ba75762911.jpg)

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

39

![](images/aa570b7b52131af4e80c1425a10e1ef794e45eefe879a7caaa3a9f89cd56d5ac.jpg)

# 交战统计：访问平台上下文菜单

![](images/40df0ea9c198b2809810b5a3efd1e2d10c19a452cb2f17a7a1e21f6dcc18edd3.jpg)

- 你可以右键单击以下任意列中的单元格，以访问平台上下文菜单：

- 攻击者  
目标  
- 预定目标  
- 武器

![](images/f246c8128d44e8d422e1b9b5fa594482300e4cf96c28c587a78e815953eb46f6.jpg)

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.