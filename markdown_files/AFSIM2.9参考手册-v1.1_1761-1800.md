- 让我们分析武器交战结果，以评估蓝方的武器交战表现：  
- 转到工具 $\rightarrow$ 显示交战统计。  
- 在攻击者下拉菜单中，选择Side: blue（蓝方）。  
- 在目标下拉菜单中，选择Side:red（红方）。

![](images/bc98eb1862a86415927a0994ef7e666550849eb6c768b85b11e8cb742f3d600a.jpg)

![](images/ebae382580f99fee0da34673355419de32a4d619fc7d713eb317bf612294575d.jpg)

![](images/f2b6673a323beef36494f335ca1520240d4421e854a4a3c2691f59ea7704bc62.jpg)

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

# UNCLASSIFIED

# 实践：交战统计

41

![](images/1dd665fba639443e36b945cb43cb82cdfdc1a6e89a4d22108770d96c46e07028.jpg)

![](images/4c13c2b7d12e7139d210bd691841c53124a72f8816e02fbf1165f9b7b14c157c.jpg)

- 右键单击结果列第1行中的单元格。  
- 点击“Plot: Result”。  
- 这将生成一个显示每次交战事件结果的饼图。  
- Ext. result 列提供了每次交战事件结果的更具体描述。

![](images/71093c31705ac74129ba0db4ab254136d4a409b0d703e7a51cd39e477e36982a.jpg)

![](images/4c530ef94403e104fe43cbfc95f2afaf97bfd91041e86c4042fe413e1baa2f9e.jpg)

<table><tr><td>Result</td><td>Ext. result</td></tr><tr><td>far away in air</td><td>Maximum time...</td></tr><tr><td>far away in air</td><td>Maximum time...</td></tr><tr><td>target prox. air ...</td><td>Target proximity</td></tr><tr><td>far away in air</td><td>Coast time exce...</td></tr></table>

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

- 追踪功能允许你查看导致交战事件或轨迹的相关事件。  
- 要追踪交战事件：

- 右键单击交战统计表中任意单元格。  
- 选择“Trace Event”。

- 要追踪轨迹：

- 右键单击平台详情中主轨迹列表的条目。  
- 选择“Trace Track”。

![](images/362e3631a19dc6bbc37ec25afd180443efd43b5b5ca13ce514014d29cddbbe21.jpg)

![](images/3d3542cceffe3ced49c625d30b6f07614118874e6b4241ee29ed0ad0ae8db48d.jpg)

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

43

![](images/64f834b856bed1cb2e628fb8f87acafacb5dfda1bc52a5d43bd277a6fc03d3f0.jpg)

# UNCLASSIFIED

# 实践：事件与轨迹追踪

![](images/1fe7b6e87bfa2d32314e9b41723af782c0c200d1c0de3151c9ab565c461ab95d.jpg)

- 将模拟时间推进到840秒。  
- 选择3540_large_sam launcher。   
- 在平台详情中，右键单击主轨迹列表中的轨迹1。
- 选择“Trace Track”。

![](images/960ee3069880b9138351e939c7518c7067d268dd76abe3ef35f44414cdc0ca43.jpg)

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

- 工具 -> 显示结果统计  
- 按事件类型显示已加载文件的内容。

- 显示每种事件的频率和内存使用情况。  
- 显示内存使用情况的饼图。

![](images/e68fe325224868c2c64d73da34b05966c522bb1d41b97d45638d9b59183f94f7.jpg)

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

45

![](images/19d250e1d7592d2785be661b64d5e484b4522cfe23638f8fcc3db6a56c53bcf6.jpg)

UNCLASSIFIED

# 学习目标

![](images/b361fc57936eeca4f8f8569b3006e89ee4ab0a3ba778383e0548e820cbe079a5.jpg)

- 包括:

- Mystic独一无二的特性  
- 怎么使用这些特性

![](images/13a3c9890e99d18d37b54deb4af280d21c3bbadef78d14e86cc218d5d159c0cc.jpg)

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

![](images/6d6702db1e15692faf239935fae4f83e7b636268462d7ed1efb69a90a69dc394.jpg)

# 6.1.9. 太空9_Space

# 6.1.9.1. 卫星星座与覆盖分析 1_ConstellationCoverage.pptx

# 6.1.9.1.1. 本节想定解析

本节想定为：

afsim2.9_src\training\user\9SPACE\scenesarios\solution\1_constellation\constellation.txt

# 蓝方兵力（本节只有蓝方）

- argus 星座

共72颗星  
每颗星携带一个几何传感器用于进行地面覆盖计算

地面网格检测点

布点范围：纬度范围[0.0s 60.0n]，经度范围[180.0w, 180.0e]  
布点间隔：经纬度都是15度一个点

输出覆盖数据

指定输出相关网格点的平均间隙持续时间。

下图为卫星在 Wizard 中的分布图：

![](images/53a6ff7caf9fcb97b886c87a112e85116376d00803289017ce377c4949730ad8.jpg)

下图为在Mystic中的卫星覆盖图（按PPT步骤就可以做出来，下图是重访时间MOE的图）：

![](images/b9cec58a1277e967352a005b823726d0d3b61bf89819126a45cee6e81d2ee136.jpg)

# 6.1.9.1.2. 本节PPT资料

本文为afsim2.9_src\training\user\9SPACE\slides\1_ConstellationCoverage.pptx的翻译。

![](images/abddc6ab36e535be3e5b6c21719d3c45396b9c1b240fd709c24b0c370aa8d6e4.jpg)

Integrity $\star$ Service $\star$ Excellence

# AFSIM用户培训

# 1-卫星星座和覆盖分析

本文档由杨石兴翻译，该资料做为《AFSIM2.9参考手册》的一部分。没有《AFSIM2.9参考手册》的加杨石兴微信领取：13324598743

![](images/41e6e99b24eb4a5c4f751a9bccfbf623e7ee427e50ac9d9b20d424c32c43bd3b.jpg)

# AFRL/RQQD

# 美国空军研究实验室

Distribution C. Distribution authorized to U.S. Government Agencies and their contractors, 11-Feb-2020. Copyright © 2020 InfoScriX, a DCS company. All rights reserved. Other requests for this document shall be referred to AFRL/RQQD.

![](images/7c56be377045c4c3f2e7e4f3b47ae089e998985ac5bfcaf3401f8138e1b9891b.jpg)

# UNCLASSIFIED

# 学习目标

1

![](images/10b63791b12c54a12a143d3d2fc33e34ffa323c5ceb87110e65b9598a2658ab8.jpg)

# - 主要包括：

定义一个简单的航天器及其轨道  
- 使用Mystic可视化轨道  
- 使用 Constellation Maker 定义和编辑卫星星座  
AFSIM覆盖范围

![](images/4e544b194ed2bc01b47e6112290b29b31962182c0be2c5dea92259c82e0c0b31.jpg)

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 11-Feb-2020.

Copyright © 2020 Infoscitex, a DCS company. All rights reserved. Other requests for this document shall be referred to AFRL/RQQD.

- 我们将创建“Argus”ISR卫星星座，并测量其覆盖范围。

![](images/6d78482a969bd7ab2d06f62d2bb425db370ae0fbc67eac8d4e3b37d68374d92d.jpg)

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 11-Feb-2020.

Copyright © 2020 Infositex, a DCS company. All rights reserved. Other requests for this document shall be referred to AFRL/RQQD.

![](images/9aaa1d3b25b3fdfe72336d0ebcb369b07abb2415f6660fa8c8c63f0490901fe0.jpg)

# UNCLASSIFIED

# 开始

3

![](images/51dd8ceac856aeaf8616d14496982059f80910eb0f92f6ab43937002f21dd0f1.jpg)

- 您需要安装以下应用程序：

- AFSIM 版本 2.7（译者注：2.9也行）  
- Wizard 版本 2.7，并启用 SpaceTools 插件  
Mystic版本2.7

![](images/ec7a68b979dcfb54159cee7c3aedeea7f40313798abac9fbd31329db8af7050c.jpg)

步骤：

1. 打开 Wizard。

2. 创建一个名为 constellation 的新项目：

- 关闭 Wizard 启动窗口。  
- 点击文件 -> 新建项目。  
- 导航到 scenarios/inwork/1_constellation。  
- 输入新项目名称。

3. 右键单击 constellation.txt 文件。  
- 选择“Set as Startup File”（设置为启动文件）。

4. 打开 constellation.txt 文件。

- 快捷方法：将 constellation.txt 文件拖放到 Wizard 图标或快捷方式上，或者直接拖放到启动对话框中（更快的方法）。

- Argus 将有 6 个轨道平面, 每个平面包含 12 颗卫星。

- 每个轨道平面的升交点赤经 (RAAN) 将均匀分布在 180 度范围内。  
- 每个平面的卫星将在360度范围内均匀分布。  
- 低地球轨道 (LEO) 将是高倾角且圆形的轨道。

- 倾角为 85 度。

偏心率为0.0。

- 重点：这里的重点是创建星座并测量覆盖范围；我们使用一个简单的传感器定义来实现目标。

- 如何定义一个空间领域的平台？

为其分配一个空间移动器(space mover)，例如：WSF_SPACE_MOVER。

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 11-Feb-2020.

Copyright © 2020 Infoscitex, a DCS company. All rights reserved. Other requests for this document shall be referred to AFRL/RQQD.

5

![](images/41c5566e675cd80b3f0488568972ddcac70a30317ae420eb3726fc187255ae21.jpg)

# UNCLASSIFIED

# 添加一个卫星: 根数

![](images/7cbea2330e3868aa32579b2facd4df75070ff7d99f8bf6f391b0c80456071a01.jpg)

- 指定经典轨道要素（Classical Orbital Elements, COEs）

需要6个要素来完全指定初始状态。  
输入选项中存在一些冗余，例如：半长轴(semi major axis)和每日公转次数(revs_per_day)。

练习：使用轨道要素添加一颗卫星。  
- 有关所有可用选项，请参阅WSF_SPACE_MOVER的文档。

![](images/9f4b2387053320a54143688c42d10b9fd28926af9b3ac767edf6ced124312386.jpg)

a - defines the size of the orbit   
e - defines the shape of the orbit   
i - defines the orientation of the orbit with respect to the Earth's equator.   
(1) - defines where the low point, perigoe, of the orbit is with respect to the Earth's surface.   
$\Omega$ - defines the location of the ascending and descending orbit locations with respect to the Earth's equatorial plane.   
V - defines where the satellite is within the orbit with respect to perigee.

scenarios/basic.txt   
```txt
14 platform elset_sat wSF_PLATFORM   
15 icon satellite   
16 side red   
17   
18 add mover WSF_SPACE_MOVER   
19 eccentricity 0.3   
20 semimajor_axis 10000 km   
21 raan 270 deg   
22 inclination 45 deg   
23 argument_of_periapsis 90 deg   
24 true_anomaly 180 deg   
25 end_mover   
26 endPlatform 
```

![](images/c6bfa7c38f4d202fce6f4bea9066a8f431f09e07e2c04b61ca60d690b0b5940c.jpg)

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 11-Feb-2020.

Copyright © 2020 Infoscitex, a DCS company. All rights reserved. Other requests for this document shall be referred to AFRL/RQQD.

![](images/eacf6922434e927ce8f990c30c0542e57969a723c515ee440d73886d959e65a1.jpg)

# UNCLASSIFIED

# 轨道可视化

7

![](images/b83dab775b85b9fc5e52de1bcfea271babeb9efd43aece0d3c00d754bdd6781f.jpg)

# - 运行场景。

- 打开output/constellation.aer文件。  
- 您可以看到卫星围绕地球运行。

# - 查看轨道的方法：

1. 选择卫星。  
2. 在平台选项(Platform Options)面板中，勾选标记为Orbit的复选框。  
3.您应该能够看到偏心的倾斜轨道。

![](images/200df877b1f2177cdb6f983ba417e877835bf338593ecbe9100ffb04417c2b27.jpg)

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 11-Feb-2020.

Copyright © 2020 Infoscitex, a DCS company. All rights reserved. Other requests for this document shall be referred to AFRL/RQQD.

- Argus 星座将包含 72 个成员。

- 使用之前的方法会导致大量的重复。

- DRY 原则（Don't Repeat Yourself）：

- 重复会导致错误。  
修改时会更加耗时。

- 可能的解决方案：

- 为Argus星座的每个轨道平面定义平台类型。  
- 这样可以将尽可能多的通用细节集中在一个地方。

·问题：

- 即便如此，仍然需要手动添加72个平台，并为每个平台手动设置轨道参数（如近地点角距）。

- 我们能做得更好吗？

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 11-Feb-2020.

Copyright © 2020 InfoRx, a DC5 company. All rights reserved. Other requests for this document shall be referred to AFRL/RQQD.

9

![](images/6f906f4353729a18ff99f70f4b9b0cf36311868b789553f90f9968f4e06b7934.jpg)

# UNCLASSIFIED

# 定义一个星座

![](images/0b250bd5499124eeac23dc8317d6a056579abce196a4f72c87bc6769aef4d9e0.jpg)

- 改进的DRY原则：

- DRY $\rightarrow$ DRYBIYMRYRyA   
- Don't Repeat Yourself, But, If You Must Repeat Yourself, Repeat Yourself Automatically.   
（不要重复自己，但如果必须重复自己，请自动化地重复。）

# - 星座创建器（Constellation Maker）

- AFSIM Wizard SpaceTools 插件中的一个工具。  
- 可快速创建并轻松修改星座。  
- 可通过工具菜单（Tools Menu）访问。  
- 我们将介绍星座创建器的基本用法。

- 有关高级用法，请参阅卫星通信模块#2。

![](images/6d0221bc0e01e502faeb90c90a071472e78f7830779b64a240720f4cb0b97275.jpg)

![](images/1fd2c88985c185a1c27236e924ba0715381ac9c5559f7616ab8ddced6b88c385.jpg)

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 11-Feb-2020.

Copyright © 2020 Infoctex, a DCS company. All rights reserved.

Other requests for this document shall be referred to AFRL/RQQD.

11

![](images/f248dcb5eaf8c97dd2c6aa69726a2c9aff2d5991af85b8e4d38545f7e88eafb1.jpg)

# 平台类型(Platform Type)

![](images/8137f23c96e66a317373a382064a54e49defd5569ea931f24f452302e199952a.jpg)

- 星座创建器 (Constellation Maker)constellation.txt

- 用于创建给定类型的平台。

- 编辑 constellation.txt 文件：  
- 删除对 scenarios/basic.txt 的引用  
- 包含 platforms/argus.txt 中定义的 ARGUS。

![](images/c62da873121fe6599b2841e6ce51fdbb9b0e0124073baf54ed82716f49789662.jpg)

platforms/nearidium.txt

![](images/6d2859f5059b97078246ff43f420c1ce07bddd6008dec174bbd2f0864455b1c6.jpg)

- 打开星座创建器（Constellation Maker）。

- 在 Platform Type（平台类型）字段中输入 ARGUS。

- 保持星座创建器窗口打开。

![](images/462e5ddfa740a28afa4873ea7514e0ec1ac74411c5b9f702f905ce8c518a0529.jpg)

Distribution C. Distribution authorized to U.S. Government Agencies and their contractors, 11-Feb-2020. Copyright © 2020 InfoSitectex, a DCS company. All rights reserved. Other requests for this document shall be referred to AFRL/RQQD.

![](images/041e0866e1572509cd54524acf77aaf1bb6fb9acfa2487fd2350a68fb390de9c.jpg)

# UNCLASSIFIED

# 星座名称

![](images/75abb92a0e76df453b6064a1fbe80b4c14eba8a9156a8e610b436081a04aed1a.jpg)

- 星座名称（Constellation Name）

设置生成平台的名称格式：

- <name>_<plane>_<sat>

设置生成文件的名称格式：

$\cdot$ <name $\rightharpoonup$ autogen.txt

- 在星座创建器（Constellation Maker）中：

- 输入一个名称。

注意将要生成的文件名称。

![](images/df0293cfe42c0915a96f1cf398db9f73527c996d75a0f8c5f9af3e4141476e12.jpg)

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 11-Feb-2020.

Copyright © 2020 Infoctex, a DC5 company. All rights reserved. Other requests for this document shall be referred to AFRL/RQQD.

# ·实践：

完成轨道细节的输入：

每日公转次数（Revs.Per Day）：15  
- 倾角（Inclination）：85度  
- 轨道平面数量（Number of Planes）：6  
每个平面的卫星数量（Satellites Per Plane）：12  
- 升交点赤经范围（RAAN Range）：180度  
初始轨道参数（InitialAnomaly）：5度

- 完成后，点击“Constellation”。

![](images/82144e32ebce9e79cb66acbee6fe14b9382b286ac52d146572e0db27bfc1cfa5.jpg)

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 11-Feb-2020.

Copyright © 2020 InfoRx, a DC5 company. All rights reserved. Other requests for this document shall be referred to AFRL/RQQD.

15

![](images/f54f422e09c671a5d4f33349422d9fb88ba472df2b6b88eb180d1000b5b122b9.jpg)

# UNCLASSIFIED

# 实践：轨道细节定义

![](images/b0abf4de943ceeca73e015ca03157dfd05debb0b2c82baa2b04ed96fc4c04f13.jpg)

![](images/012a6842350b9cb2e4f07261dfc724018c17a20d3c1c16ad77b1de04d399116d.jpg)

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 11-Feb-2020.

Copyright © 2020 Infoscitex, a DCS company. All rights reserved. Other requests for this document shall be referred to AFRL/RQQD.

- 生成 argus_autogen.txt 文件后，关闭星座创建器（Constellation Maker）。  
- 在 Constellation.txt 文件中包含生成的文件。  
- 运行模拟程序（sim）并检查输出结果。

constellation.txt   
```txt
5 define_path_variable CASE constellation   
6 #load in scenarios   
8 #include_once scenarios/basic.txt   
9 include_once platforms/argus.txt   
10 include_once argus_autogen.txt 
```

argus autogen.txt   
```txt
18 platform argus_0_0 ARGUS
19 mover
20 inclination 85 degrees
21 revs_per_day 15
22 raan 0 degrees
23 true_anomaly 5 degrees
24 end mover
25 endPlatform
26
27 platform argus_0_1 ARGUS
28 mover
29 inclination 85 degrees
30 revs_per_day 15
31 raan 0 degrees
32 true_anomaly 35 degrees
33 end mover
34 endPlatform
35
36 platform argus_0_2 ARGUS
37 mover
38 inclination 85 degrees 
```

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 11-Feb-2020.

Copyright © 2020 Infoctex, a DCS company. All rights reserved. Other requests for this document shall be referred to AFRL/RQQD.

17

![](images/6da7f1add4175d59350277d0a9281a88cb29b61e6472d4edb8be1d407107a2d4.jpg)

# UNCLASSIFIED

# AFSIM覆盖分析

![](images/81fbdb97a488ecd108641f502f5f422a5886a5c30383c1fdbe37d23292b1bb5e.jpg)

收集网格点与其他平台之间交互的时间历史数据，并将这些信息后处理为有效性度量（MOE, Measures of Effectiveness）。

WSF_SENSOR_COVERAGE 监控资产对之间的传感器交互。   
- 支持多种网格类型和 MOE。  
- 提供多种输出格式，包括集成的可视化覆盖图。  
- 领域无关性：

- 尽管它特别适用于卫星覆盖分析，但也可以用于其他领域。

![](images/57387a4634236ac0649e2d7df1ffd4440772ddcfb2ca9e0f2f20f1de7a77ebed.jpg)

![](images/d28537088543764358e5aa18efe3935cef23b0e4a0bf481fdda1899dcfd4a7e7.jpg)

- 覆盖（Coverage）捕捉成对资产之间的交互：一个是网格资产（grid asset），另一个是自由资产（free asset）。

资产（Assets）是平台-设备对（platform-device pairs）。  
- 对于WSF_SENSOR_COVERAGE，设备将是传感器（sensor）或“无”（none）。

- 网格资产（Grid Assets）：

- 指定为平台类型-设备对（platform_type-devicepair）。  
- 给定平台类型的实例将在每个网格点上创建。

- 自由资产（Free Assets）：

- 可以指定为任何平台、平台类型、类别或组。

![](images/a82522b79c5f288ab2f779654589bdaa9e0b5d0ec3c4c1ff039c7b5ca9ef7ea7.jpg)  
Example: Interactions between free assets (in space) and grid assets (on the ground) visualized with Mystic.

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 11-Feb-2020.

Copyright © 2020 Infoscitex, a DCS company. All rights reserved. Other requests for this document shall be referred to AFRL/RQQD.

![](images/f27140d3037f294fef922d63912e75895443b2b0e2eb9bc574c11c121a23b2e3.jpg)

# UNCLASSIFIED

# 覆盖网格

19

![](images/2ae6b6f94c7409284f45e772cccddcda31bd597dcf0ac0074bcf0d9f168c5e77.jpg)

- 网格（Grids）提供了创建网格资产（grid assets）的位置集合。

如果需要，创建的资产可以遵循地形（terrain）。  
- 网格可以被多个覆盖计算（coverage computations）使用。

- 将覆盖（Coverage）添加到场景：

1. 在启动文件中包含 coverage/global.txt。  
2. 添加一个网格（grid）。  
3. WSF_LAT_LON_grid 是一个规则的矩形网格，由网格点组成。

# constellation.txt

<table><tr><td>10</td><td>include_once platforms/argus.txt</td></tr><tr><td>11</td><td>include_once argus_autogen.txt</td></tr><tr><td>12</td><td></td></tr><tr><td>13</td><td>include_once coverage/global.txt</td></tr></table>

# coverage/global.txt

<table><tr><td>5</td><td>grid global_grid WSF_LAT_LONGRID</td></tr><tr><td>6</td><td>latitude spans 60.0s 60.0n</td></tr><tr><td>7</td><td>longitude span 180.0w 180.0e</td></tr><tr><td>8</td><td>altitude 0 km agl</td></tr><tr><td>9</td><td>origin 0n 0w</td></tr><tr><td>10</td><td>latitude_spacing 15 deg</td></tr><tr><td>11</td><td>longitude-spacing 15 deg</td></tr><tr><td>12</td><td>asset WSF PLATFORM none</td></tr><tr><td>13</td><td>grid_data_file output/global_grid_data.csv</td></tr><tr><td>14</td><td>end_grid</td></tr></table>

# - 覆盖块（Coverage Block）

- 典型的AFSIM表达方式包括对象名称（如global_coverage）和对象类型（如WSF_SENSORYCOVERAGE）。  
- 选择刚刚定义的网格。  
- 使用ARGUS平台类型，并将eye sensor作为自由资产（free assets）。

coverage/global.txt   
```txt
16 coverage global_coverage WsF_SENSOR_COVERAGE   
17 grid global_grid   
18 assets   
19 platform_type ARGUS eye   
20 end assets   
21   
22   
23   
24 output_dir ./output   
25 raw_data_file raw_intervals_global.csv   
26   
27 moe simple_global WSF_SIMPLE_COVERAGE_MOE   
28 output data end_output   
29 output grid.stats end_output   
30 output lat_lon/stats end_output   
31 end_moe   
32   
33 moe revisit_global WSF_REVISIT_TIME_MOE   
34 subtype mean   
35 output data end_output   
36 end_moe   
37   
38 overlay_file overlay_global   
39 end_coverage 
```

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 11-Feb-2020.

Copyright © 2020 Infoscitex, a DC5 company. All rights reserved. Other requests for this document shall be referred to AFRL/RQQD.

21

![](images/dd2798e5008b0b2c47d6e37171c9bb0644e41e686586586eb96d2c860cced2a2.jpg)

# UNCLASSIFIED

# 覆盖定义

![](images/cec602ab4ea07da3f8452f5198f929222a181fbeb592a5ad29ff8974c05b4960.jpg)

# - 覆盖块：输出（Coverage Block:）

# Output)

指定输出目录。  
- 在覆盖计算期间，可以生成所有资产之间原始访问间隔的 CSV 记录。  
- MOE数据输出也将出现在指定的目录中。

<table><tr><td colspan="8">Grid Name, grid position</td></tr><tr><td>1</td><td colspan="7">Grid Asset ID, Grid Asset Device, Free Asset Name, Free Asset Device, Start Epoch, End Epoch, Start</td></tr><tr><td>2</td><td>115,</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>3</td><td>119,</td><td>none,</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>4</td><td>107,</td><td>none,</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>5</td><td>183,</td><td>none,</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>6</td><td>111,</td><td>none,</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>7</td><td>117,</td><td>none,</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>8</td><td>173,</td><td>none,</td><td></td><td></td><td></td><td></td><td></td></tr></table>

coverage/global.txt   
```txt
16 coverage global_coverage WsF_SENSOR_COVERAGE   
17 grid global_grid   
18 assets   
21 platform_type ARGUS eye   
22 end_assets   
23 output_dir ./output   
25 raw_data_file raw_intervals_global.csv   
26 moe simple_global WsF_SIMPLE_COVERAGE_MOE output data end_output output grid stats end_output output lat_lon.stats end_output end_moe   
23 moe revisit_global WsF_REVISIT_TIME_MOE subtype mean output data end_output   
34 end_moe   
35 overlay_file overlay_global   
39 end_coverage 
```

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 11-Feb-2020.

Copyright © 2020 InfoSctex, a DCS company. All rights reserved. Other requests for this document shall be referred to AFRL/RQQD.

# - 覆盖块：MOE（Coverage Block: MOE）

- 用户可以收集任意数量的MOE（有效性度量）。  
提供多种输出选项：

- data：每个网格点的MOE值。  
- grid.stats：在整个网格上计算的统计数据。  
- lat_lon/stats：投影到纬度或经度上的统计数据。

- 可以指定输出格式和文件名。  
提供合理的默认值。  
- 某些 MOE 具有子类型。  
- 有关可用MOE的详细信息，请参阅AFSIM文档。

coverage/global.txt   
```txt
16 coverage global_coverage WsF_SENSOR_COVERAGE   
17 grid global_grid   
18 assets platform_type ARGUS eye   
19 end_assets   
20 output_dir ./output   
21 raw_data_file raw_intervals_global.csv   
22 moe simple_global WSF_SIMPLE_COVERAGE_MOE   
23 output data end_output   
24 output grid.stats end_output   
25 output lat_lon/stats end_output   
26 end_moe   
27 moe revisit_global WSF_REVISIT_TIME_MOE   
28 subtype mean   
29 output data end_output   
30 end_moe   
31   
32   
33 overlay_file overlay_global   
34   
35   
36   
37   
38   
39 
```

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 11-Feb-2020.

Copyright © 2020 InfoRx, a DC5 company. All rights reserved. Other requests for this document shall be referred to AFRL/RQQD.

![](images/94a7306d9e8f5e6dd739b7db84091918ee05b9ce5b4610625e812efc8ec6efeb.jpg)

# UNCLASSIFIED

# 覆盖定义

23

![](images/55e4333411b55c59b6948fc498de273829f6122076b3c7f0e7a53e48d29ec6b0.jpg)

# - 覆盖块

- 覆盖文件生成的数据可以被 Wizard、Mystic 和 Warlock 中的覆盖面板使用。

# - 定义覆盖后，运行仿真。

由于我们在仿真中添加了大量交互，这将需要一些时间。

coverage/global.txt   
```txt
16 coverage global_coverage WsF_SENSOR_COVERAGE   
17 grid global_grid   
18 assets platform_type ARGUS eye   
19 end_assets   
20 output_dir ./output   
21 raw_data_file raw_intervals_global.csv   
22 moe simple_global WSF_SIMPLE_COVERAGE_MOE   
23 output data end_output   
24 output grid.stats end_output   
25 output lat_lon/stats end_output   
26 end_moe   
27 moe revisit_global WSF_REVISIT_TIME_MOE   
28 subtype mean   
35 output data end_output   
36 end_moe   
37 overlay file overlay_global   
38 end_coverage 
```

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 11-Feb-2020.

Copyright © 2020 Infoscitex, a DCS company. All rights reserved. Other requests for this document shall be referred to AFRL/RQQD.

# - 已创建一个覆盖叠加文件

- 通过覆盖叠加面板查看  
- 在“视图”菜单中启用面板  
面板将显示并停靠

![](images/7a843bb24ccef4215292dd31091087772a57214c6ee1179ef40cc811069c495b.jpg)

# - 加载 output/overlay_global.csv 文件

- 点击“加载覆盖文件”  
导航到输出文件夹

# - MOE数据将在地图窗口中以可视化形式呈现

![](images/f2810cb175b424f68ca4818d94375e9c545cb031e1b6efc93ace627630acf5b7.jpg)

Distribution C. Distribution authorized to U.S. Government Agencies and their contractors, 11-Feb-2020. Copyright © 2020 InfoScriRx, a DCS company. All rights reserved. Other requests for this document shall be referred to AFRL/RQQD.

![](images/b0f934c4986d88e27454e87c860520a405b98a799cdcd133980d71d0000ff53e.jpg)

# UNCLASSIFIED 覆盖叠加

![](images/35d500dfcd66596b45456988070fa2c46d3dab5ac4d1bbf8b27d415623346947.jpg)

# 控制

- 可以加载多个.cvg文件  
- 可以启用/禁用每个文件的显示  
- 可以选择要显示的 MOE（效能指标）  
可以设置映射到颜色渐变的MOE值范围  
- 可以选择叠加层的透明度  
- 可以选择渐变样式

![](images/3fc755911d2d0033c7336f4d1068edacacebe14127ae0f82890873e69d2fce4b.jpg)

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 11-Feb-2020.

Copyright © 2020 InfoSctex, a DCS company. All rights reserved. Other requests for this document shall be referred to AFRL/RQQD.

# - 平均间隙时间不均匀

即使使用更长的仿真时间和更长的覆盖间隔，这种情况仍然存在。

# - 我们能改进结果吗？

结果受多种因素影响  
- 完整的方法需要检查许多参数

例如，轨道平面的数量，每个平面上的卫星数量

![](images/69d852cd6352a2e2a14b573b9d052679dbc1d66541a8b9f101689502022951e2.jpg)

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 11-Feb-2020.

Copyright © 2020 InfoScriTex, a DC5 company. All rights reserved. Other requests for this document shall be referred to AFRL/RQQD.

27

![](images/8c57dcde64652e2d2764af438627d9dfc8fd46e66a7df86c69fbdb567712634b.jpg)

# UNCLASSIFIED

# 编辑一个星座

![](images/a50d8e2de6b62a720c3350569bf413ffd3867804c25722378c2da63f53cf0bb0.jpg)

# - 我们能改进结果吗？

- 这里我们尝试一种更改，向星座添加一个异常别名。

# - 可以轻松编辑星座：

- 打开 argus_autogen.txt 文件。  
- 在编辑器中任意位置右键单击。  
- 选择“使用星座生成器编辑”（Edit Using Constellation Maker）。  
- 这将打开星座生成器，并加载生成星座的详细信息。

![](images/1ffec3aac42632cfdb68763533cc0ff06103e277e2e2586dc3bafb1a01471227.jpg)

![](images/027cc083a64aa2643f88aafe160e896fc37b22db7263d1c55d5e92b4377dbf42.jpg)  
argus autogen.txt

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 11-Feb-2020.

Copyright © 2020 InfoSctex, a DCS company. All rights reserved. Other requests for this document shall be referred to AFRL/RQQD.

# - 异常偏移

- 相对于前一轨道平面中对应卫星的异常偏移量。

# - 做以下动作：

- 将异常偏移量（AnomalyAlias）更改为15度。  
- 点击“星座”按钮以重新生成星座。  
- 关闭星座生成器。  
- 重新运行仿真并检查输出结果。  
想象一下，如果逐个平台进行编辑，这将花费多长时间。

![](images/a4dd4477eeb56a6cd5bd3486776c91ec60d412ae30dc104790e03c410df6bacf.jpg)

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 11-Feb-2020.

Copyright © 2020 InfoRx, a DC5 company. All rights reserved. Other requests for this document shall be referred to AFRL/RQQD.

29

![](images/3d887d0b75ebe4b3aeda244d66a4dfc2499857b63c560bf57758c89eb4686e8a.jpg)

# UNCLASSIFIED

# 覆盖比较

![](images/eca6b7393c9ce2d121051dca74fb606a67119d2af246b4541d6ea9a2a921714b.jpg)

![](images/a95178b90a7fb7557bc130c12526831427d25bcd9722258d34ef00ed4e4cf96a.jpg)  
Anomaly Alias: 0 deg

![](images/fff98dc15a83d2385516907c5ae682b3b2f3ca58aa20bdf2724eaa101dce8688.jpg)  
Anomaly Alias: 15 deg

- 这只是一个参数，还有许多其他参数可能会影响结果。

- 我们能让参数空间的探索变得更简单吗？

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 11-Feb-2020.

Copyright © 2020 InfoSctex, a DCS company. All rights reserved. Other requests for this document shall be referred to AFRL/RQQD.

# - 脚本化星座生成器

- WsfConstellationMaker 脚本类  
- 在运行时创建星座  
- 然后由外部驱动脚本设置参数并运行 mission.exe

例如，AFSIM中包含的基于Python的工具chugger  
- 更多信息请参阅AFSIM文档

Distribution C. Distribution authorized to U.S. Government Agencies and their contractors, 11-Feb-2020. Copyright © 2020 InfoSitex, a DCS company. All rights reserved. Other requests for this document shall be referred to AFRL/RQQD.

![](images/acd5c901b9371141cbe81834e7303f2225a54e5e70d12062a1671844ebcdaeab.jpg)

# UNCLASSIFIED

# WsfConstellationMaker

![](images/db79df41bfc86311c1032cc4264011bbc5c8fd41610aaba79bab46c6856579e2.jpg)

# - WsfConstellationMaker 示例

- 查看 scripts/argus.Scripted.txt 文件  
- 将scripts/argus.Scripted.txt替换为argus_autogen.txt使用

scripts/arguscripted.txt   
5 script void GenerateConstellation()   
6 WsfConstellationMaker maker   
7 $\equiv$ WsfConstellationMaker.CreateGeneral(6,12,15,180);   
8 maker.SetRevolutionsPerDay(15);   
9 maker.SetInclination(85);   
10 maker.SetInitialAnomaly(5);   
11 maker.SetPlatformType("ARGUS");   
12   
13 maker.Create();   
14 end_script   
15   
16 observer   
17 enable SIMULATION_INITIALIZING GenerateConstellation   
18 end observer

![](images/92fee5cd868d14bb0d24300f161c31f77fa119b464fca30833c99394ae02b007.jpg)

# 6.1.9.2. 卫星通信 2_Comm_Sats

# 6.1.9.2.1. 本节想定解析

本节想定资源在以下目录下：

afsim2.9_src\training\user\9SPACE\scenes\solution\2_comm_sats照着PPT做到第29页为想定一，剩余为想定二

# 想定一（星间通信）可以看到下图两颗卫星中间通信用了5跳

![](images/3aa9929c250b98d3032f421427ceabb7519d6a9e7aea499f4e486c456c5a9320.jpg)

# 蓝方兵力（本节只有蓝方）

Nearidium星座

定义了 72 颗卫星, 分 6 个轨道面

星间链路建链规则如下：

- 和同一轨道平面的前、后星建链  
- 非最后一个轨道面（ $0 \sim 5$ 也即第 5 个轨道面）则和下一轨道面的同序号星、下一轨道面的前序号星建链  
- 非第 0 个轨道面则上一轨道面的同序号星、上一轨道面的下一序号星建链

- 在 test_network.txt 中随机选择两颗星来做通信（需要修改默认的代码 22、23 行修改成两颗星），在想定 2 中才是星地通信。

# 想定二（星地通信）可以看到图像卫星0借助星座经历了3跳到达地面站

![](images/2f13d1ba2b379d11b69b4158315a8fefb16853476c2b436814e3c20f1b1c8aa6.jpg)

afsim2.9_src\training\user\9SPACE\scenario\solution\2_comm_sats\comm_sats.txt

本节功能是图像卫星与地面站借助星座的通信。如上图经历了3跳。运行的过程中因为卫星的位置一直在变化也可能无法通信。

# 蓝方兵力（本节只有蓝方）

Nearidium星座

定义了72颗卫星，分6个轨道面  
星间链路建链规则如下：

- 和同一轨道平面的前、后星建链  
- 非最后一个轨道面（ $0 \sim 5$ 也即第 5 个轨道面）则和下一轨道面的同序号星、下一轨道面的前序号星建链  
- 非第0个轨道面则上一轨道面的同序号星、上一轨道面的下一序号星建链

图像卫星

一个名为 imaging_sat 的图像卫星  
建立和Nearidium星座的通信

地面站

一个名为 jacksonabad 的地面站  
建立和Nearidium星座的通信

# 6.1.9.2.2. 本节PPT资料

本文为afsim2.9_src\training\user\9SPACE\slides\2_Comm_Sats.pptx的翻译。

![](images/cc5daabbed80b888e866a86596737a5e68c501c8c23d99d6253641dcb432ace5.jpg)

Integrity $\star$ Service $\star$ Excellence

# AFSIM空间培训

# 2-卫星通信

![](images/55f23957768471eefc05d07a78fd28e46e2e0e72edf41b81412f7bc072b5fe23.jpg)

# AFRL/RQQD

# 美国空军研究实验室

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 11-Feb-2020.

Copyright © 2020 Infoseek, a DCS company. All rights reserved.

Other requests for this document shall be referred to AFRL/RQQD.

1

![](images/e0dd306752a31000ab1750ab07782993a89e0533dfbaf0a574883b1abfec351e.jpg)

# UNCLASSIFIED

# 学习目标

![](images/4e6892372ab61ece9c5d22ea3d154dc29226875af960d7ab9ee77c3e0e01163c.jpg)

# ·包括：

创建一个通信卫星星座。  
- 高级使用星座生成器。  
- 在星座内设置一个静态的星间链路网络。  
设置一个临时或动态网络，将星座连接到地面站和其他空间资产。

![](images/afa568584ab1ac767c072bd9cc5282c8d447c2c0ec8a99e9b619ec1409e9faae.jpg)

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 11-Feb-2020.

Copyright © 2020 InfoScitek, a DCS company. All rights reserved.

Other requests for this document shall be referred to AFRL/RQQD.

·佛罗里迪斯坦利用Nearidium卫星星座传输由ISR卫星收集的关于奥瓦卡的监视数据。

![](images/1a0d41fd802855e94999a623801ca21deb1e710feee8a6baf8a6b69be0de7b06.jpg)

- 您将为一个不完整的场景添加行为。

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 11-Feb-2020.

Copyright © 2020 Infoctex, a DCS company. All rights reserved.

Other requests for this document shall be referred to AFRL/RQQD.

3

![](images/2ec15ba145ac8294d24e83eda644b4380ef9435365ee503ce6350a8ee0346f05.jpg)

# UNCLASSIFIED

# 开始

![](images/0e2d70123b5fdcb011728f932313deb1644a4d101d04a2873ac8f687dd3f3e9f.jpg)

- 您需要安装以下应用程序：

- AFSIM 版本 2.7  
- 启用了SpaceTools插件的Wizard版本2.7  
Mystic版本2.7

# 操作步骤：

1. 打开 Wizard。  
2. 创建一个名为 comm_sats 的新项目。  
3. 关闭 Wizard 启动窗口。  
4. 依次点击 File -> New Project。  
5. 导航到 scenarios/inwork/2_comm_sats 目录。  
6. 输入新项目名称。  
7. 右键单击 comm_sats.txt 文件。  
8. 选择“Set as Startup File”（设置为启动文件）。  
9. 打开 comm_sats.txt 文件。

- 快捷方法：将 comm_sats.txt 文件直接拖放到 Wizard 图标或快捷方式上（更快的方法）。

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 11-Feb-2020.

Copyright © 2020 InfoScitek, a DCS company. All rights reserved.

Other requests for this document shall be referred to AFRL/RQQD.

NEARIDIUM卫星将配备两种射频通信设备：

- 星间链路（crosslink），用于连接 NEARIDIUM 星座内的卫星；  
- 下行链路（downlink），用于连接地面平台和ISR卫星imaging_sat。

- 星间链路将连接每颗 NEARIDIUM 卫星至：

同一轨道平面中前后相邻的卫星；  
- 最多四颗相邻轨道平面中的卫星。

- 星间链路不会跨越第1平面和第6平面之间的“接缝”，因为这两个平面中的卫星相对彼此运动方向相反。

![](images/85f8ab24a27ef8bf8c6b9ce2d78562399a14320c22f3250878f29c940b45d416.jpg)

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 11-Feb-2020.

Copyright © 2020 Infoctex, a DCS company. All rights reserved.

Other requests for this document shall be referred to AFRL/RQQD.

5

![](images/1639d5b458f52fd127cc7ba41555ec2fe52a2582107dd2750a75a8fbe700b6ef.jpg)

# UNCLASSIFIED

# NEARIDIUM通信

![](images/95605ea59e913cad83aac1246dd560b8b99d7f66fe0d7d95c52360d6e7cd579f.jpg)

检查射频通信定义：

comm/crosslink.txt   
comm/handheld.txt

将这些实例添加到 NEARIDIUM 平台类型中。  
下一步：

需要设置网络，以控制哪些平台可以通过特定的通信设备相互连接。  
需要一个路由器来实现星间链路（crosslink）和下行链路（downlink）通信设备之间的接口连接。

技术说明：

路由器是平台的一部分。如果未明确定义路由器和路由协议（router_protocol(s)），路由器将默认使用网络真实数据（network truth data）来处理链路连接。

# platforms/nearidium.txt

![](images/d12937ce63b4f41d621520326163cad1903e40906673bd6b1b0fdc7b48a96516.jpg)

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 11-Feb-2020.

Copyright © 2020 Infoctex, a DCS company. All rights reserved. Other requests for this document shall be referred to AFRL/RQQD.

媒介：

- 表示通信设备传播数据的方式。  
- NEARIDIUM_CROSSLINK和NEARIDIUM_HANDHELD都指定了一个媒介。

```txt
comm/simple_delay_medium.txt   
5 medium SIMPLE_DELAY_MEDIUM WSFCOMM MEDIUM UngUIDED   
6 default_mode_name simple Alignment_delay   
7   
8 mode simple Alignment_delay   
9 packet_loss_time constant 5 sec   
10 end_mode   
11 end_medium 
```

检查：

comm/simple_delay_medium.txt   
- 有许多选项可以为通信仿真添加效果。

• 请阅读文档以了解更多信息。

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 11-Feb-2020.

Copyright © 2020 Infoctex, a DCS company. All rights reserved.

Other requests for this document shall be referred to AFRL/RQQD.

7

![](images/5c71e1fb1e97e218b4e05cc21eaed1afa4278370a619e46ed3551ba1645c9da2.jpg)

# UNCLASSIFIED

# Nearidium通信网络

![](images/4774609d57b69c31fcc5b008a6956363f87ef0d0deec056e182a120ebdb25156.jpg)

仅需包含一次并检查网络定义：

comm/networks.txt

- UL_DL_NETWORK 是一种临时（ad hoc）网络类型，它会以指定的更新速率（update_rate）更新网络连接。

这种网络类型非常适合用于建模具有动态视距（LOS）访问的移动平台网络，例如卫星到地面网络或混合卫星星座网络。

CROSSLINK_NETWORK 是一种通用网络类型，默认情况下可以支持多达 255 个命名通信设备。

- 稍后我们将使用星间链路通信设备（crosslink comm device）为 NEARIDIUM 卫星指定静态链路。

为每个通信设备设置网络名称（network_name）：

在星间链路通信设备上设置为CROSSLINK_NETWORK  
- 在下行链路通信设备上设置为UL_DL_NETWORK

# platforms/nearidium.txt

```txt
include_once comm/crosslink.txt   
include_once comm/handheld.txt   
include_once comm/networks.txt   
platform_type NEARIDIUM WSFPLATFORM   
icon satellite   
side green   
mover WSF_SPACE_MOVER   
eccentricity 0.0   
argument_of_periapsis 0.0 deg   
end_mover   
comm crosslink NEARIDIUM_CROSSLINK   
end_comm   
comm downlink NEARIDIUM_HANDHeld   
end_comm   
endplatform_type 
```

仅需包含一次并检查网络定义：

comm/networks.txt

- UL_DL_NETWORK 是一种临时（ad hoc）网络类型，它会以指定的更新速率（update_rate）更新网络连接。

这种网络类型非常适合用于建模具有动态视距（LOS）访问的移动平台网络，例如卫星到地面网络或混合卫星星座网络。

CROSSLINK_NETWORK 是一种通用网络类型，默认情况下可以支持多达 255 个命名通信设备。

- 稍后我们将使用星间链路通信设备（crosslink comm device）为 NEARIDIUM 卫星指定静态链路。

为每个通信设备设置网络名称（network_name）：

在星间链路通信设备上设置为CROSSLINK_NETWORK

- 在下行链路通信设备上设置为UL_DL_NETWORK

comm/networks.txt

```txt
5 # Network 1: U/L and D/L data streams between  
6 # - jasksonabad GS and any satellite  
7 # (so ground to satellite comms)  
8 # - imaging_sat and NEARIDIUM constellation  
9 # (so mixed constellation comms)  
10 # - dynamic links that update automatically  
11 # @update_rate  
12 network UL_DI_NETWORK WSFCOMM_NETWORK_AD_HOC  
13 update_rate 5 sec  
14 end_network  
15  
16 # Network 2: NEARIDIUM constellation crosslinks  
17 # - these links will be specified per NEARIDIUM  
18 # platform/satellite in a future exercise using  
19 # the Advanced Constellation Maker option  
20 network CROSSLINK_NETWORK WSFCOMM_NETWORKGENERIC  
21 end_network 
```

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 11-Feb-2020.

Copyright © 2020 Infoctex, a DCS company. All rights reserved.

Other requests for this document shall be referred to AFRL/RQQD.

9

![](images/94f6c259b09f0fd5257e15ddddbb80fee600bea435e697260ee60b3b254f25b8.jpg)

# UNCLASSIFIED

# Nearidium通信网络

![](images/45ae8db399a20d16858fb00c83e8446705a668b0388fe2aadd8448501da8416e.jpg)

仅需包含一次并检查网络定义：

comm/networks.txt

- UL_DL_NETWORK 是一种临时（ad hoc）网络类型，它会以指定的更新速率（update_rate）更新网络连接。

这种网络类型非常适合用于建模具有动态视距（LOS）访问的移动平台网络，例如卫星到地面网络或混合卫星星座网络。

CROSSLINK_NETWORK是一种通用网络类型，默认情况下可以支持多达255个命名通信设备。

稍后我们将使用星间链路通信设备（crosslink comm device）为 NEARIDIUM 卫星指定静态链路。

为每个通信设备设置网络名称（network_name）：

在星间链路通信设备上设置为CROSSLINK_NETWORK

- 在下行链路通信设备上设置为UL_DL_NETWORK

# platforms/nearidium.txt

```txt
4 include_once comm/crosslink.txt   
5 include_once comm/handheld.txt   
6 include_once comm/networks.txt   
7   
8 platform_type NEARIDIUM WSFPLATFORM   
9 icon satellite   
10 side green   
11   
12 mover WSF_SPACE_MOVER   
13 eccentricity 0.0   
14 argument_of_periapsis 0.0 deg   
15 end_mover   
16   
17 comm crosslink NEARIDIUM CROSSLINK   
18 network_name CROSSLINK_NETWORK   
19 end_comm   
20   
21 comm downlink NEARIDIUM HANDHELD   
22 network_name UL_DL_NETWORK   
23 end_comm   
24 endplatform_type 
```

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 11-Feb-2020.

Copyright © 2020 Infoctex, a DCS company. All rights reserved.

Other requests for this document shall be referred to AFRL/RQQD.

1. 为 NEARIDIUM 平台类型添加一个路由器块，并将其命名为 default。  
2. 将路由器设置为不使用默认协议（default protocol），稍后我们将通过router_protocol更改协议。  
3. 将路由器设置为自动接口链接（automatically interface links），这将使消息能够在星间链路（crosslink）和下行链路（downlink）通信设备之间传递（类似于桥接功能）。  
4. 在文件顶部附近包含文件 comm/nearidium_protocol.txt（仅需包含一次）。

platforms/nearidium.txt   
```txt
include_once comm/crosslink.txt   
include_once comm/handheld.txt   
include_once comm/networks.txt   
platform_type NEARIDIUM WSFPLATFORM   
icon satellite   
side green   
mover WSF_SPACE_MOVER   
eccentricity 0.0   
argument_of_periapsis 0.0 deg   
end_mover   
router default WSFCOMM_ROUTER   
end routers   
comm crosslink NEARIDIUM_CROSSLINK   
network_name CROSSLINK_NETWORK   
end_comm   
comm downlink NEARIDIUM_HANDHELD   
network_name UL_DL_NETWORK   
end_comm   
endplatform_type 
```

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 11-Feb-2020.

Copyright © 2020 Infoscitex, a DCS company. All rights reserved.

Other requests for this document shall be referred to AFRL/RQQD.

11

![](images/e92ecfa2ba1a4ab694d72f9354bfa5a01df6077dbc718d27f8afd5daac44db5b.jpg)

# Nearidium的路由和协议

(part 1/3)

![](images/9b8a109bf826af222d35f9a385829087d45dccbeef56571eb31d53e63d5f4cdd.jpg)

1. 为 NEARIDIUM 平台类型添加一个路由器块，并将其命名为 default。  
2. 将路由器设置为不使用默认协议（defaultprotocol），稍后我们将通过router_protocol更改协议。  
3. 将路由器设置为自动接口链接（automatically interface links），这将使消息能够在星间链路（crosslink）和下行链路（downlink）通信设备之间传递（类似于桥接功能）。  
4. 在文件顶部附近包含文件 comm/nearidium_protocol.txt（仅需包含一次）。

platforms/nearidium.txt   
```txt
include_once comm/crosslink.txt   
include_once comm/handheld.txt   
include_once comm/networks.txt   
platform_type NEARIDIUM WSF PLATFORM   
icon satellite   
side green   
mover WSF_SPACE_MOVER   
eccentricity 0.0   
argument_of_periapsis 0.0 deg   
end_mover   
router default WSF COMM ROUTER use_default_protocol false   
end_ROUTer   
comm crosslink NEARIDIUM_CROSSLINK   
network_name CROSSLINK_NETWORK   
end_comm   
comm downlink NEARIDIUM_HANDHELD   
network_name UL_DL_NETWORK   
end_comm   
endPLATFORM_type 
```

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 11-Feb-2020.

Copyright © 2020 InfoSite, a DCS company. All rights reserved.

Other requests for this document shall be referred to AFRL/RQQD.

1. 为 NEARIDIUM 平台类型添加一个路由器块，并将其命名为 default。  
2. 将路由器设置为不使用默认协议（default protocol），稍后我们将通过router_protocol更改协议。  
3. 将路由器设置为自动接口链接（automatically interface links），这将使消息能够在星间链路（crosslink）和下行链路（downlink）通信设备之间传递（类似于桥接功能）。  
4. 在文件顶部附近包含文件 comm/nearidium_protocol.txt（仅需包含一次）。

platforms/nearidium.txt   
```txt
include_once comm/crosslink.txt   
include_once comm/handheld.txt   
include_once comm/networks.txt   
platform_type NEARIDIUM WSFPLATFORM   
icon satellite   
side green   
mover WSF_SPACE_MOVER   
eccentricity 0.0   
argument_of_periapsis 0.0 deg   
end_mover   
router default WSFCOMM_ROUTER   
use default protocol false   
automated_Interface_linking true   
end routers   
comm crosslink NEARIDIUM_CROSSLINK   
network_name CROSSLINK_NETWORK   
end_comm   
comm downlink NEARIDIUM_HANDHELD   
network_name UL_DL_NETWORK   
end_comm   
end-platform_type 
```

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 11-Feb-2020.

Copyright © 2020 Infoscitex, a DCS company. All rights reserved.

Other requests for this document shall be referred to AFRL/RQQD.

13

![](images/b81857740a262e9253c693a3652fa3dd09d53c6baba21cdf5b1925bf51b56187.jpg)

# Nearidium的路由和协议

(part 1/3)

![](images/182e12639664d6cfa304e2701530601428ed6f44187677b262ed7420eca9d26d.jpg)

1. 为 NEARIDIUM 平台类型添加一个路由器块，并将其命名为 default。  
2. 将路由器设置为不使用默认协议（default protocol），稍后我们将通过router_protocol更改协议。  
3. 将路由器设置为自动接口链接（automatically interface links），这将使消息能够在星间链路（crosslink）和下行链路（downlink）通信设备之间传递（类似于桥接功能）。  
4. 在文件顶部附近包含文件 comm/nearidium_protocol.txt（仅需包含一次）。

platforms/nearidium.txt   
```txt
include_once comm/crosslink.txt   
include_once comm/handheld.txt   
include_once comm/networks.txt   
include_once comm/nearidium_protocol.txt   
9 platform_type NEARIDIUM WSF PLATFORM   
10 icon satellite side green   
11   
12   
13 mover WSF_SPACE_MOVER eccentricity 0.0 argument_of_periapsis 0.0 deg   
14 end_mover   
15   
16 router default WSFCOMM_ROUTER use_default_protocol false automated_Interface_linking true   
17   
18   
19   
20   
21   
22   
23   
24   
25   
26 comm crosslink NEARIDIUM_CROSSLINK network_name CROSSLINK_NETWORK   
27   
28 end_comm   
29   
30 comm downlink NEARIDIUM_HANDHELD network_name UL_DL_NETWORK   
31   
32 end_comm   
33 endplatform_type 
```

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 11-Feb-2020.

Copyright © 2020 InfoSite, a DCS company. All rights reserved.

Other requests for this document shall be referred to AFRL/RQQD.

# 5. 打开文件

# comm/nearidium_protocol.txt。

6. 此 router_protocol 允许在临时（ad hoc）网络尝试通过

OnConnectionAdded 本地通信事件连接通信设备时进行链路控制，并通过返回布尔值决定是否连接：

true $=$ 连接

false $=$ 不连接

7.补充缺失的router_protocol代码，以允许下行链路通信设备与任何非NEARIDIUM平台类型进行临时连接（请记住：NEARIDIUM平台之间将仅通过星间链路通信设备进行通信）。

comm/nearidium protocol.txt   
```txt
4 router_protocol NEARIDIUM_PROTOCOL WsFCOMM_ROUTER_PROTOCOL_ADD_HOC  
0 script bool OnConnectionAdded(wsFAddress aSourceComm,  
6 WsFAddress aDestinationComm,  
7 WsFCommGraph aNetworkState,  
8 WsFCommRouter aRouter)  
9  
10 WsFComm srcComm = WsFComm.GetComm(aSourceComm);  
11 string srcCommName = srcComm.Name();  
12 WsFPlatform srcPlat = srcComm Platforms();  
13 string srcPlatType = srcPlat.Type();  
14 WsFComm destComm = WsFComm.GetComm(aDestinationComm);  
15 string destCommName = destComm.Name();  
16 WsFPlatform destPlat = destComm.PlatForm();  
17 string destPlatType = destPlat.Type();  
18 WsFComm to imaging_sat or jacksonabad via downlink  
20 # Check 1: NEARIDIUM to NEARIDIUM via crosslink  
21 if (srcCommName == "crosslink" && destCommName == "crosslink" &&  
22 srcPlatType == "NEARIDIUM" && destPlatType == "NEARIDIUM")  
23 { return true;  
24 }  
25  
26 # Check 2: NEARIUM to imaging_sat or jacksonabad via downlink  
27 (so NEARIDIUM will not connect to NEARIDIUM via downlink)  
28 // add code here  
30  
31  
32  
33  
34  
35  
36 return false;  
37 endScript  
38 end_ROUTer_protocol 
```

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 11-Feb-2020.

Copyright © 2020 Infoscitex, a DCS company. All rights reserved.

Other requests for this document shall be referred to AFRL/RQQD.

# UNCLASSIFIED

![](images/b5d0fcbdde587131ffef35e12d4ec9bb8b7662d82d43ee09b4f5d234791bd318.jpg)

# Nearidium的路由和协议

(part 2/3)

15

![](images/5e8bc76a6a13b033369a8a224c3d899e1b965dfcb3113e27cdef17e8e7fd6645.jpg)

5. 打开文件

comm/nearidium_protocol.txt.

6. 此 router_protocol 允许在临时（ad hoc）网络尝试通过

OnConnectionAdded 本地通信事件连接通信设备时进行链路控制，并通过返回布尔值决定是否连接：

true = 连接

false $=$ 不连接

7. 补充缺失的router_protocol代码，以允许下行链路通信设备与任何非

NEARIDIUM平台类型进行临时连接

（请记住：NEARIDIUM平台之间将仅通过星间链路通信设备进行通信）。

comm/nearidium protocol.txt   
4 routerprotocol NEARTIDIUM PROTOCOL WsF COMM ROUTER PROTOCOL AD HQC   
5 script bool OnConnectionAdded(wsfAddress aSourceComm,   
6 WsfAddress aDestinationComm,   
7 WsfCommGraph aNetworkState,   
8 WsfCommRouter aRouter)   
9   
10 WsfComm srcComm = WsfComm.GetComm(aSourceComm);   
11 string srcCommName $\equiv$ srcComm.Name();   
12 WsfPlatform srcPlat $\equiv$ srcComm Platform();   
13 string srcPlatType $\equiv$ srcPlat.Type();   
14   
15 WsfComm destComm $=$ WsfComm.GetComm(aDestinationComm);   
16 string destCommName $\equiv$ destComm.Name();   
17 WsfPlatform destPlat $\equiv$ destComm.PlatForm();   
18 string destPlatType $\equiv$ destPlat.Type();   
19   
20 # Check 1: NEARIDIUM to NEARIDIUM via crosslink   
21 if(srcCommName $\equiv$ "crosslink" && destCommName $\equiv$ "crosslink"&&   
22 srcPlatType $\equiv$ "NEARIDIUM" && destPlatType $\equiv$ "NEARIDIUM")   
23 { return true;   
24 }   
25   
26   
27 # Check 2: NEARIUM to imaging_sat or jacksonabad via downlink   
28 # (so NEARDIUM will not connect to NEARIDIUM via downlink)   
29 // add code here   
30   
31   
32   
33   
34   
35 return false;   
36 endScript   
37 end_ROUTer_protocol

5. 打开文件

comm/nearidium_protocol.txt.

6. 此 router_protocol 允许在临时（ad hoc）网络尝试通过

OnConnectionAdded 本地通信事件连接通信设备时进行链路控制，并通过返回布尔值决定是否连接：

true $=$ 连接

false = 不连接

7. 补充缺失的router_protocol代码，以允许下行链路通信设备与任何非NEARIDIUM平台类型进行临时连接

（请记住：NEARIDIUM平台之间将仅通过星间链路通信设备进行通信）。

comm/nearidium protocol.txt   
```cpp
4 router_protocol NEARIDIUM_PROTOCOL WsFCOMM_ROUTER_PROTOCOL_AD_HOC  
5 script bool OnConnectionAdded(WsFAddress aSourceComm,  
6 WsFAddress aDestinationComm,  
7 WsFCommGraph aNetworkState,  
8 WsFCommRouter aRouter)  
9  
10 WsFComm srcComm = WsFComm.GetComm(aSourceComm);  
11 string srcCommName = srcComm.Name();  
12 WsFPlatform srcPlat = srcComm.PlatForm();  
13 string srcPlatType = srcPlat.Type();  
14 WsFComm destComm = WsFComm.GetComm(aDestinationComm);  
15 string destCommName = destComm.Name();  
16 WsFPlatform destPlat = destComm.PlatForm();  
17 string destPlatType = destPlat.Type();  
18 # Check 1: NEARIDIUM to NEARIDIUM via crosslink  
19 if (srcCommName == "crosslink" && destCommName == "crosslink" &&  
20 { return true;  
21 }  
22 # Check 2: NEARIUM to imaging_sat or jacksonabad via downlink  
23 # (so NEARIDIUM will not connect to NEARIDIUM via downlink)  
24 // add code here  
25 return false;  
26 endScript  
27 endROUTer_protocol 
```

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 11-Feb-2020.

Copyright © 2020 Infoctex, a DCS company. All rights reserved.

Other requests for this document shall be referred to AFRL/RQQD.

17

![](images/7e15d090b8d4c5caef7962806dcb7d665244208bbccd36d27a76f8ac22c4b439.jpg)

# Nearidium的路由和协议

(part 2/3: solution)

![](images/591d87dc7d639db3ce7762ef6923d0bacd7e3ed2db72f641fd004a9258635cba.jpg)

5. 打开文件

comm/nearidium_protocol.txt.

6. 此 router_protocol 允许在临时（ad hoc）网络尝试通过

OnConnectionAdded 本地通信事件连接通信设备时进行链路控制，并通过返回布尔值决定是否连接：

true $=$ 连接

false = 不连接

7. 补充缺失的router_protocol代码，以允许下行链路通信设备与任何非

NEARIDIUM 平台类型进行临时连接

（请记住：NEARIDIUM平台之间将仅通过星间链路通信设备进行通信）。

comm/nearidium protocol.txt   
```cpp
4 router_protocol NEARIDIUM_PROTOCOL WsF COMM_ROUTER_PROTOCOL_AD_HOC  
5 script bool OnConnectionAdded(WsFAddress aSourceComm, WsFAddress aDestinationComm, WsFCommGraph aNetworkState, WsFCommRouter aRouter)  
6 WsFComm srcComm = WsFComm.GetComm(aSourceComm);  
7 string srcCommName = srcComm.Name();  
8 WsFPlatform srcPlat = srcComm Platforms();  
9 string srcPlatType = srcPlat.Type();  
10 WsFComm destComm = WsFComm.GetComm(aDestinationComm);  
11 string destCommName = destComm.Name();  
12 WsFPlatform destPlat = destComm Platforms();  
13 string destPlatType = destPlat.Type();  
14 WsFComm destComm = WsFComm.GetComm(aDestinationComm);  
15 WsFPlatform destPlat = destComm Platforms();  
16 string destPlatType = destPlat.Type();  
17 # Check 1: NEARIDIUM to NEARIDIUM via crosslink  
18 if (srcCommName == "crosslink" && destCommName == "crosslink" && srcPlatType == "NEARIDIUM" && destPlatType == "NEARIDIUM") { return true; }  
20 # Check 2: NEARIUM to imaging_sat or jacksonabad via downlink  
21 # (so NEARIDIUM will not connect to NEARIDIUM via downlink) // add code base  
22 if (srcCommName == "downlink" && destPlatType != "NEARIDIUM") { return true; }  
23 return false;  
24 endScript  
25 endROUTer_protocol 
```

# 8. 返回 platforms/nearidium.txt

9. 最后，将router_protocol添加到NEARIDIUM路由器块中。

platforms/nearidium.txt   
```txt
include_once comm/crosslink.txt   
include_once comm/handheld.txt   
include_once comm/networks.txt   
include_once comm/nearidium_protocol.txt   
9 platform_type NEARIDIUM WSF PLATFORM   
10 icon satellite side green   
11   
12   
13 mover WSF_SPACE_MOVER eccentricity 0.0   
14 argument_of_periapsis 0.0 deg   
15   
16 end_mover   
17   
18 router default WSFCOMM_ROUTER use_default_protocol false automated/interface linking true   
19   
20   
21   
22   
23   
24 end routers   
25   
26 comm crosslink NEARIDIUM_CROSSLINK network_name CROSSLINK_NETWORK   
27   
28 end_comm   
29   
30 comm downlink NEARIDIUM_HANDHELD network_name UL_DL_NETWORK   
31   
32   
33 end_comm   
33 endplatform_type 
```

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 11-Feb-2020.

Copyright © 2020 Infoctex, a DCS company. All rights reserved.

Other requests for this document shall be referred to AFRL/RQQD.

19

![](images/0fdc0402277c1f81baee955daff7c4bd38129c50002aaa47b4e0d7f8eca93de2.jpg)

# Nearidium的路由和协议

(part 3/3)

![](images/ebb2b3c56949c5934b46bf652aac7d3895a9bdabed7f9464dae1514f9092f2c0.jpg)

# 8. 返回 platforms/nearidium.txt

9. 最后，将 router_protocol 添加到 NEARIDIUM 路由器块中。

platforms/nearidium.txt   
```txt
include_once comm/crosslink.txt   
include_once comm/handheld.txt   
include_once comm/networks.txt   
include_once comm/nearidium_protocol.txt   
9 platform_type NEARIDIUM WSF PLATFORM   
10 icon satellite side green   
11   
12   
13 mover WSF_SPACE_MOVER eccentricity 0.0 argument_of_periapsis 0.0 deg   
16 end_mover   
17   
18 router default WSFCOMM_ROUTer use_default_protocol false automated_Interface_linking true   
19   
20 add router_protocol nearprot NEARIDIUM_PROTOCOL   
23 end routers   
24   
25   
26 comm crosslink NEARIDIUM_CROSSLINK   
27 network_name CROSSLINK_NETWORK   
28 end_comm   
29   
30 comm downlink NEARIDIUM_HANDHELD   
31 network_name UL_DL_NETWORK   
32 end_comm   
33 endplatform_type 
```

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 11-Feb-2020.

Copyright © 2020 InfoScitex, a DCS company. All rights reserved.

Other requests for this document shall be referred to AFRL/RQQD.

- 各个 NEARIDIUM 卫星的星间链路通信设备尚未连接。我们需要编辑星座

# 配置：

1. 打开nearidium_autogen.txt;  
2. 在编辑器中任意位置右键单击，选择Edit using Constellation Maker;  
3. 点击 Advanced。

- Advanced 模式会显示额外的控制选项:

设置生成文件的路径；  
以高级模式生成星座配置。

![](images/7c26cf6e2696c9a28868e389951c9f6fbdbef8914b6f887d972266d1bf6540cc.jpg)

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 11-Feb-2020.

Copyright © 2020 Infoctex, a DCS company. All rights reserved.

Other requests for this document shall be referred to AFRL/RQQD.

21

![](images/c7dbf4736d671d5eaa4f9cfb44bf5f6649205a8be4b899c3e7e24d75bdeeb996.jpg)

# UNCLASSIFIED

# 星座生成工具(Constellation Maker)

![](images/8de763071dfbcb83b0b83a8ae0f999ac66b13187e16239fb1856f150b298af01.jpg)

- Constellation Maker 有两种操作模式:  
- 直接模式（Direct Mode）

直接生成星座配置  
- 简单易用  
生成可立即使用的输入

- 高级模式（Advanced Mode）

生成一个启动文件，用于生成星座配置  
- 为星座生成过程增加额外步骤  
- 提供更大的灵活性，并可以根据需要调整单个成员

# - 直接模式（Direct Mode）：

- 启动 Constellation Maker  
填写参数值   
- 点击 Constellation 按钮生成 <name>_autogen.txt  
- <name>_autogen.txt 可直接用于您的场景

# - 高级模式（Advanced Mode）：

- 启动 Constellation Maker，如有需要显示高级选项  
填写参数值   
- 点击Generator按钮生成<name>_generator.txt   
- 将 `<name>`_generator.txt 设置为启动文件  
根据需要自定义<name>_generator.txt  
运行仿真以生成<name>_.autogen.txt   
- <name>_autogen.txt 可直接用于您的场景

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 11-Feb-2020.

Copyright © 2020 Infoseek, a DCS company. All rights reserved.

Other requests for this document shall be referred to AFRL/RQQD.

23

![](images/ac8d286fa56f4969dac65e80fabe1688309328a8fe9f99c42c45f73c00e9a4ac.jpg)

# UNCLASSIFIED

# 连接Nearidium

![](images/0ce2ec0648a3c7818ce08845910623084f2a45700e748dac1f4579444f9021ec.jpg)

# - 每个 NEARIDIUM 成员需要通过星间链路网络上的静态通信链路连接到一组唯一的其他成员。

- 这是 Constellation Maker 高级模式的完美应用场景。

# - 使用高级模式的 Constellation Maker:

![](images/19a11042143ade8291b49a64f6a57c027a08059b63a01f5d232977be5ee9b408.jpg)

- 检查 NEARIDIUM 星座的详细信息  
- 点击Generator按钮生成nearidiumgenerated.txt;   
- 关闭 Constellation Maker;   
- 将nearidiumgenerated.txt设置为启动文件（start-up file）。

# - 检查生成器场景：

- 有两个部分被标记为可自定义。  
- 在每个平台被写入时，会调用 SpecializeMember。

# - 我们将修改 SpecializeMember 以：

- 为通信设备设置网络名称；  
- 将卫星与星座中的邻居连接起来。

nearidium generator.txt   
```txt
62 // YOUR SCRIPTS HERE - content between these two markers will not be overwritten  
63 // by the Constellation Maker  
64 // YOUR SCRIPTS HERE - content between these two markers will not be overwritten  
65 // by the Constellation Maker  
66  
67 // YOUR MODIFICATIONS HERE  
68 // This script is called during constellation generation to allow customization of  
69 // the platforms that compose the constellation. Do not change the signature or the  
70 // name of this script, but the contents can be freely modified.  
71 script void SpecializeMember(FileIO aFile, int aPlane, int aSat)  
72 end_script 
```

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 11-Feb-2020.

Copyright © 2020 Infoctex, a DCS company. All rights reserved.

Other requests for this document shall be referred to AFRL/RQQD.

25

![](images/31f73ea2c053e215f10d725b554782c9a04c5b4a6a1820d3564cd3eaaeaa9d6b.jpg)

# 实践: SpecializeMember

![](images/43649721d3e81d438d1ac0a2b77d75f17f94075b34a0e26f1317686b80d67ff7.jpg)

# - SpecializeMember:

- 使用FileIO将详细信息写入生成的AFSIM文件中。  
- 使用以下函数：

-GenerateName   
- PrevSatInPlane   
NextSatInPlane

- 当前功能是添加跨轨道平面的链路。

# ·练习：

- 从scripts/specializehelper.txt中复制起始代码。  
- 在指定位置编辑脚本，添加两个同轨道平面的链路：

- 上一个卫星（Previous satellite）  
- 下一个卫星（Next satellite）

scripts/specializehelper.txt   
```txt
5 script void SpecializeMember(FileIO aFile, int aPlane, int aSot)  
6 string name = GenerateName(aPlane, aSot);  
7 aFile.WriteLn("");  
8 aFile.WriteLn(" comm crosslink");  
9 # YOUR SCRIPT HERE  
10 if (aPlane != cmNumPlanes - 1)  
11 {  
12 string aheadRight =GenerateName(aPlane + 1, aSot);  
13 aFile.WriteLn(" link " + aheadRight + " crosslink");  
14 string behindRight =GenerateName(aPlane + 1, PrevSatInPlane(aSot));  
15 aFile.WriteLn(" link " + behindRight + " crosslink");  
16 }  
17 }  
18  
19  
20 if (aPlane > 0)  
21 {  
22 string aheadLeft =GenerateName(aPlane - 1, NextSatInPlane(aSot));  
23 aFile.WriteLn(" link " + aheadLeft + " crosslink");  
24 string behindLeft =GenerateName(aPlane - 1, aSot);  
25 aFile.WriteLn(" link " + behindLeft + " crosslink");  
26 }  
27  
28  
29  
30 end.script 
```

# - 解决方案：

nearidium generator.txt

```cs
script void SpecializeMember(FileIO aFile, int aPlane, int aSat)  
string name = GenerateName(aPlane, aSat);  
aFile.WriteLn("");  
aFile.WriteLn(" comm crosslink");  
string aheadName =GenerateName(aPlane, NextSatInPlane(aSat));  
aFile.WriteLn(" link + aheadName + " crosslink");  
stringBehindName =GenerateName(aPlane, PrevSatInPlane(aSat));  
aFile.WriteLn(" link + behindName + " crosslink");  
if (aPlane != cmNumPlanes - 1)  
{  
    string aheadRight =GenerateName(aPlane + 1, aSat);  
    aFile.WriteLn(" link + aheadRight + " crosslink"); 
```

# - 生成自定义星座：

- 运行场景。  
- 将生成文件nearidium_autogen.txt。  
- 将 comm_sats.txt 设置为启动文件（start-up file）。  
- 打开nearidium_autogen.txt，查看脚本添加的链路。

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 11-Feb-2020.

Copyright © 2020 Infoctex, a DCS company. All rights reserved.

Other requests for this document shall be referred to AFRL/RQQD.

27

![](images/52e02ceed986afe1a7ed89cc5122ee2dd00aae0024ce06c187397fc6652f9d84.jpg)

# UNCLASSIFIED

# 测试Crosslink Network

![](images/7f2e9489b6e7535b4979b9e507ce326ed506d141b483243f3e0c2bdd6b8999f8.jpg)

# - 系统现在能够在卫星之间发送消息。

- 在启动文件中包含 scripts/test_network.txt:  
- 用于在随机卫星之间发送消息。  
- 在启动文件中包含 observers/draw/messages.txt:  
- 用于可视化网络中的消息路径。  
- 运行仿真，并在Mystic中查看输出结果。  
- 还可以检查 output/2_comm_sats.evt 文件，以查看每条消息的事件记录。

![](images/e134b594f9d9ba0aebeb5048c89b75a050379a46b4b916b1432a604d5a40ede1.jpg)

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 11-Feb-2020.

Copyright © 2020 Infoctex, a DCS company. All rights reserved. Other requests for this document shall be referred to AFRL/RQQD.

From:nearidium_4_10

To:nearidium_0_7

Comm: crosslink

Hops: 7

![](images/680d6ae6db47416640526f329e8117ad08d420ae8ff7cfb2f22a8ed59f351048.jpg)

DISTRUBION C. Distribution authorized to U.S. Government Agencies and their contractors, 11-Feb-2020.

Copyright © 2020 Infoseek, a DCS company. All rights reserved.

Other requests for this document shall be referred to AFRL/RQQD.

29

# UNCLASSIFIED

# 地面站

现在我们添加几个用户：

一个指挥官，用于接收监视数据；  
一颗监视卫星。  
打开comm_sats.txt

修改comm_sats.txt:

包含文件 scenarios/floridistan.txt。

修改floridistan.txt:

包含文件 sensors/handheld.txt 和 comm/handheld.txt。  
修改指挥官（jacksonabad）：

- 添加通信上行链路（comm uplink）：  
使用网络UL_DL_NETWORK;  
注意，这是一个动态网络，每5秒动态建立一次链路。

添加传感器hh：

该传感器对于在ResultsVis中可视化通信可见性窗口非常有用，因为它与上行链路具有相同的最大范围限制（3000公里）。

# comm sats.txt

9

load the scenario   
include_once nearidium_autogen.txt

12 43

include_once scripts/test_network.txt   
include_once observers/draw/messages.txt

现在我们添加几个用户：

一个指挥官，用于接收监视数据；  
一颗监视卫星。  
打开comm_sats.txt

# 修改comm_sats.txt:

# 包含文件 scenarios/floridistan.txt。

修改floridistan.txt:

包含文件 sensors/handheld.txt 和 comm/handheld.txt。  
修改指挥官（jacksonabad）：

- 添加通信上行链路（comm uplink）：  
使用网络UL_DL_NETWORK;

注意，这是一个动态网络，每5秒动态建立一次链路。

添加传感器hh:

该传感器对于在ResultsVis中可视化通信可见性窗口非常有用，因为它与上行链路具有相同的最大范围限制（3000公里）。

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 11-Feb-2020.

Copyright © 2020 Infoctex, a DCS company. All rights reserved.

Other requests for this document shall be referred to AFRL/RQQD.

![](images/bf7a0a358b6751199e18568174e2ed98dcb73300da57081445d5e79050049e1b.jpg)

# UNCLASSIFIED

# 地面站

![](images/b65bcf07bdbddea9480dec31f0bc0a1df5acb4dd0bcc6c814191c61832237215.jpg)

现在我们添加几个用户：

一个指挥官，用于接收监视数据；  
一颗监视卫星。  
打开comm_sats.txt

修改comm_sats.txt:

包含文件 scenarios/floridistan.txt。

# 修改floridistan.txt:

包含文件 sensors/handheld.txt 和 comm/handheld.txt。  
修改指挥官（jacksonabad）：

- 添加通信上行链路（comm uplink）：  
使用网络UL_DL_NETWORK;

注意，这是一个动态网络，每5秒动态建立一次链路。

添加传感器hh:   
该传感器对于在ResultsVis中可视化通信可见性窗口非常有用，因为它与上行链路具有相同的最大范围限制（3000公里）。

# comm sats.txt

```txt
9 #load the scenario   
10 include_once nearidium_autogen.txt   
11 include_once scenarios/floridistan.txt   
12 include_once scripts/test_network.txt   
13 include_once observers/draw/messages.txt   
14 include_once observers/drawmessages.txt 
```

# scenarios/floridistan.txt

include_once sensors/handheld.txt include_once comm/handheld.txt   
7 # The central command.   
8 platform jacksonabad WSFPLATFORM side blue icon tower position 30.3322n 81.6557w altitude $5\mathrm{m}$ 10   
11   
12   
13   
14   
15   
16   
17   
18   
19   
20 endplatform

现在我们添加几个用户：

一个指挥官，用于接收监视数据；  
一颗监视卫星。  
打开comm_sats.txt

修改comm_sats.txt:

包含文件 scenarios/floridistan.txt。

# 修改floridistan.txt:

包含文件 sensors/handheld.txt 和 comm/handheld.txt。  
修改指挥官（jacksonabad）：

- 添加通信上行链路（comm uplink）：

- 使用网络 UL_DL_NETWORK;  
注意，这是一个动态网络，每5秒动态建立一次链路。

添加传感器hh:

该传感器对于在ResultsVis中可视化通信可见性窗口非常有用，因为它与上行链路具有相同的最大范围限制（3000公里）。

comm sats.txt

![](images/ffb299849d6d2c5cffda59220dc194e16978f26e5b7eace3a542feb13323bc39.jpg)

scenarios/floridistan.txt

![](images/a9fcaedc56a1cc414395ed0cdf0035b4c3d83b5a61ba46b00fc6d5c1d7071bf5.jpg)

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 11-Feb-2020.

Copyright © 2020 Infoctex, a DCS company. All rights reserved.

Other requests for this document shall be referred to AFRL/RQQD.

33

![](images/be9de2a6eaf70106b63228ec0226d203202dfee2e7ce0cf461cc2fd8acb3f75f.jpg)

UNCLASSIFIED

# 地面站

![](images/b5658d0abc58033501019d63ee6eed4c7e3a47a35dd56c3f189eff48014e74f7.jpg)

现在我们添加几个用户：

一个指挥官，用于接收监视数据；  
一颗监视卫星。  
打开comm_sats.txt

修改comm_sats.txt:

包含文件 scenarios/floridistan.txt。

# 修改floridistan.txt:

包含文件 sensors/handheld.txt 和 comm/handheld.txt。  
修改指挥官（jacksonabad）：

- 添加通信上行链路（comm uplink）：  
使用网络UL_DL_NETWORK;  
注意，这是一个动态网络，每5秒动态建立一次链路。

- 添加传感器hh:

- 该传感器对于在 Results Vis 中可视化通信可见性窗口非常有用，因为它与上行链路具有相同的最大范围限制（3000 公里）。

comm sats.txt

![](images/863a928751804bc9b8cc1dde20bff37a7720fb81e5a07f70f1605ede98c68965.jpg)

scenarios/floridistan.txt

![](images/a1b13a53a6c16b62b836703d8cc8cfe5636a9082f3355cd85bae39c29037041e.jpg)

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 11-Feb-2020.

Copyright © 2020 Infoctex, a DCS company. All rights reserved.

Other requests for this document shall be referred to AFRL/RQQD.