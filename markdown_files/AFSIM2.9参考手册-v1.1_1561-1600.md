- 平台可以有组件，类似传感器、处理器、运动  
- 平台可以有属性，类似图标和阵  
- 平台特性是平台对象的一个属性

- 可以在平台内部定义  
- 也可以外部定义平台引用

- 特性定义可以包含以下内容：

空间属性：

- 方位角（水平面内的角度）  
- 仰角（垂直面内的角度）

- 电子属性：

频率   
极化（电波方向）

状态

![](images/12f35c4d9888b1bcfa9749bfe1fabcbde6ebf0bd151d162cbf9649eea6362b06.jpg)

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQQD.

# UNCLASSIFIED

# 平台坐标系统

3

![](images/a5dd21ad03efbf1325e9baaddae397bcf3564cc11d4744ddf1cbf8a56a4f41ff.jpg)

![](images/272dfbd4913bab1d538d1c31dadb4c8f8c10cf4614e133719d6f5efde81e8e21.jpg)

- AFSIM有一个和平台相关的坐标系统

水平角度范围[-180，180]  
垂直角度范围[-90,90]   
- 两者都取0时是平台的正前方朝向

![](images/aacbca5da1b0538d4aad69333b02454c052f3d3f523de52628c161b1b5b822b7.jpg)

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19.

Other requests for this document shall be referred to AFRL/RQQD.

# - 返回单个截面

- 块以 radar signature 开始  
- 块以 end_radar_signature 结束   
- 为特征命名  
- 这定义了一个恒定的10平方米的雷达截面积  
- 大致相当于一个6英尺的球  
- 对于所有方位角、频率和极化，返回恒定值。

radar_signature CUEBALL_10DB constant 10 dbsm end_radar_signature

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQQD.

5

![](images/15e635f39d99aea396efaad85286c02454a3c9c63801bec40045a720834217a3.jpg)

# 2维内联表格的概念

![](images/98c37cb316192958f3fc41164d4bf9bb0b8625ae0f1bdcd7bef76523f4a9beeb.jpg)

- 允许定义复杂特征  
- 数据点在方位/俯仰坐标中定义  
- 在数据点之间插值求值  
- 表格定义需要以下信息：

- 单位  
- 每个维度的大小（方位和俯仰）  
- 方位和俯仰坐标  
- 每个方位/俯仰坐标的数据值

# 内联表定义

- 维度由方位角和俯仰角（度）定义  
定义表格时：

提供单位  
- 提供每个维度的大小  
- 方位坐标沿表格纵向排列   
俯仰坐标沿表格横向排列   
- 将方位和俯仰坐标按升序排列

![](images/18b1f5fc5721e987f91f9a18718267c9c74e06dccb863e9552e902ecb45b593f.jpg)

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQQD.

# UNCLASSIFIED

# 建立一个2维内联表格

7

![](images/6de4e414fab3735ca609c73c50a1767c22d061a376850b32341aeaa16f1bd5ca.jpg)

![](images/808a6212c3d5676de637ed852d3bfb873c71efc88d8da4eb7eceee6fde22a350.jpg)

- 内联表数据

- 每个俯仰的值垂直排列  
- 每个方位的值水平排列  
- 每个方位和俯仰对有一个单一数据值

<table><tr><td colspan="2">inline table</td><td>dbsm 17</td><td>5</td><td></td><td></td></tr><tr><td></td><td>-90</td><td>-10</td><td>0</td><td>10</td><td>90</td></tr><tr><td>-180</td><td>30</td><td>20</td><td>0</td><td>20</td><td>30</td></tr><tr><td>-150</td><td>30</td><td>20</td><td>5</td><td>20</td><td>30</td></tr><tr><td>-135</td><td>30</td><td>20</td><td>20</td><td>20</td><td>30</td></tr><tr><td>-120</td><td>30</td><td>20</td><td>5</td><td>20</td><td>30</td></tr><tr><td>-90</td><td>30</td><td>20</td><td>0</td><td>20</td><td>30</td></tr><tr><td>-60</td><td>30</td><td>20</td><td>5</td><td>20</td><td>30</td></tr><tr><td>-45</td><td>30</td><td>20</td><td>20</td><td>20</td><td>30</td></tr><tr><td>-30</td><td>30</td><td>20</td><td>5</td><td>20</td><td>30</td></tr><tr><td>0</td><td>30</td><td>20</td><td>0</td><td>20</td><td>30</td></tr><tr><td>30</td><td>30</td><td>20</td><td>5</td><td>20</td><td>30</td></tr><tr><td>45</td><td>30</td><td>20</td><td>20</td><td>20</td><td>30</td></tr><tr><td>60</td><td>30</td><td>20</td><td>5</td><td>20</td><td>30</td></tr><tr><td>90</td><td>30</td><td>20</td><td>0</td><td>20</td><td>30</td></tr><tr><td>120</td><td>30</td><td>20</td><td>5</td><td>20</td><td>30</td></tr><tr><td>135</td><td>30</td><td>20</td><td>20</td><td>20</td><td>30</td></tr><tr><td>150</td><td>30</td><td>20</td><td>5</td><td>20</td><td>30</td></tr><tr><td>180</td><td>30</td><td>20</td><td>0</td><td>20</td><td>30</td></tr></table>

end inline table

# 在方位角和俯仰角返回雷达截面积

- 使用一个表或一组表  
- 每个表定义一个特征  
- 以 radar signature 开始; 以 end_radar_signature 结束  
为雷达特征命名  
- 添加内联表  
- 请参阅文档以获取有关使用多表为多频率和极化定义特征的更多信息。

![](images/140003ff8c0010cede599a0eb32083b8331f0a3a45e403dc4bd221b9b4dc1e9c.jpg)

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQQD.

9

![](images/28016f65611db711548f767fcec421acfb2418db59fe29177f00ca783d1231c2.jpg)

# UNCLASSIFIED

# 定义特性状态和波段

![](images/8e95f119ace2d828272ae41c13af089f1b014955d4f664ee08417491cbf88c63.jpg)

# - 可以为特征定义多个状态

- 使用脚本更改状态  
- 还可以定义频率特性  
- 红外（IR）波段  
- 声学和射频（RF）的频率

![](images/d19864e9835bb72861ab0a2a3c161478247f1a553a9c6560196f9d6e3218aa36.jpg)

- 把这一行添加到setup.txt当中  
- 可以在我们的模型库中找到  
- 打开common.txt查看其内容

# setup.txt

```txt
2 include_ once platforms/common.txt   
3 include_ once platforms/bomber.txt   
4 include_ once platforms/car.txt   
5 include_ once platforms/satellite.txt   
6 include_ once platforms/ship.txt   
7 include_ once platforms/tank.txt   
8 include_ once platforms/ship.txt   
9 include_ once platforms/tank.txt   
10 
```

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQQD.

11

![](images/1369919bca57de5052336d81616ffe597467089086d352b49451c607514eb37c.jpg)

# UNCLASSIFIED

# 特性在此定义

![](images/f1b8655c46422f732ae847e19aadf45f19d6a9932a8739ab64bf8d7ee3e467aa.jpg)

# common.txt

1 # \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*  
2 #\* \* \* \* \* \* \* \* \* \* \* \* \* \* \* \* \* \* \* \* \* \* \* \* \* \* \* \* \* \* \* \* \* \* \* \* \* \* \* \* \* \* \* \* \* \* \* \* \*  
3 #\* UNCLASSIFIED \* \* \*  
4 #\* \* \* \* \* \* \* \*  
5  
6 #  
7 # Vehicle Signatures  
8  
9 infarred_signature VEHICLE_INFRARED_SIGNATURE constant 10 watts/steradian end_infrared_signature optical_signature VEHICLE_OPTICAL_SIGNATURE constant $10\mathrm{m}^2$ end_optical_signature radar_signature VEHICLE_RARAD_SIGNATURE constant $1\mathrm{m}^2$ end_radar_signature  
10  
11  
12  
13  
14  
15  
16  
17  
18  
19  
20  
21 # Red datalink  
22 # comm TEAM_DATALINK WSFCOMM_TRANSEIVER transfer_rate 100 mbits/sec end_comm  
23  
24  
25  
26  
27  
28  
29  
30 # Filter tactics  
31 #  
32  
33 filter_FILTER Tactics WSF_KALMAN_FILTER rangemeasurement_sigma 50.m bearingMeasurement_sigma 0.1 deg elevationMeasurement_sigma 0.1 deg  
34  
35  
36  
37  
38  
39  
40  
41 end_filter

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19.

Other requests for this document shall be referred to AFRL/RQQD.

# NOTE: 在平台的TYPE BROWSER当中查看

- 在Wizard中，菜单：View -> Type Browser  
- 展开WSFPLATFORM   
- 对CAR点右键, 选择Manage Platform Parts

![](images/3099c95042b3841228fd2056c939a63954b1486fc12467dcb4721f6c31bad025.jpg)

![](images/e9cd39ccd180aed1880dac99cb807d08dd0310d1027fc0e5fa3df09b2dee9d24.jpg)

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQQD.

13

![](images/c3bde2a52eea0b244ba392201d1d07b9832ce01b0251597add7bb5a7cc11b84f.jpg)

# UNCLASSIFIED

# 平台组件管理

![](images/3a3cb5608c470c0bc9a9193256029070595e630b2d0cb130dd377a04661810f3.jpg)

![](images/9a82c6fe1fdb1b08e0886a0fc71909cb951cde6eda2aadc5b574447888867ece.jpg)

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

- 使用右侧下拉框选择和为平台添加目标特性  
- 红外特性  
光学特性  
-雷达特性

![](images/94fbf61b75a91209667917979b144c847ea2276d1946bd70eefec8525b8ab288.jpg)

- 关闭Platform Parts Manager保存所有文件

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQQD.

UNCLASSIFIED

![](images/d56f5ceebd5b87acd46755ad63cc0eb912727284bb34d74d9951bc40ef05e124.jpg)

# 新的CAR定义

![](images/ceef13cfd74a758b8cb64c89ccc74e3e853333f25efb5621b810a9e4f82e22ac.jpg)

- 特性当前被加到platform_type当中

- 这种方法添加特性都会被加入在platform_type的末尾当中  
- 这也不是不行，但是一般来说特性都是在图标和阵营下面定义，也就是定义的比较靠上  
- 可以自己手动改改

![](images/29fa298c955d6dc930349aa460de7b88304516f8817e090c8e7ef12ae7c03518.jpg)

![](images/d904aeed8cc22585a8832bb35cc8117c0b31e7ecdf912544953cd74cf63ac0db.jpg)

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19.

Other requests for this document shall be referred to AFRL/RQQD.

- 在“bomber.txt”中, 添加以下代码

- "include_once signatures/bomberoptical_sig.txt"   
- "include_once signatures/bomber_infrared_sig.txt"   
- "include_once signatures/bomber_radar_sig.txt"

这些代码可以在我们的模型库中找到

platforms/bomber.txt   
```cmake
include_once weapons/agm/red_gps_bomb_1.txt include_once signatures/bomber_infrared_sig.txt include_once signatures/bomberoptical_sig.txt include_once signatures/bomber_radar_sig.txt platform_type BOMBER WSFPLATFORM icon bomber 
```

UNCLASSIFIED   
```txt
DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQQD. 
```

17

![](images/627df71d651904bb0477829c44931c45bccdbb3252ed57f52b671b2d3fbb5cb3.jpg)

# 将特性添加到平台当中Platform

![](images/ea287d7d63f6d35524d0c8ef6a13a144995098015b5e0481a43a47b7764d363a.jpg)

在BOMBER中添加这些特性  
- 添加时会自动补全   
- 运行时选择“Mission”然后运行。

platforms/bomber.txt   
```txt
include_once signatures/bomber_radar_sig.txt   
9 platform_type BOMBER WSF PLATFORM icon bomber infrared_signature BOMBER_INFRAREDSIG optical_signature BOMBER_OPTICALSIG radar_signature BOMBER_RADARSIG mover WSF_AIR_MOVER end_mover weapon red_gps_bomb_1 RED_GPS_BOMB_1 maximum_request_count 2 quantity 4 endweapon 
```

右键BOMBER_RADARSIG-选择“VisualizeSignature”

![](images/491721753183e0af8498c983bc4a23fe5c633795e5f61b6ffefb1d9908d0add5.jpg)  
platforms/bomber.txt

![](images/e3a46d87f0557373e9b5e21f07e022b0b0200edd91a6625abfb6b1eb994d4875.jpg)  
DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQQD.

19

![](images/33887830bab624ed5eeba2d75403a342fd6ecf483546969bc369ce004ea678dc.jpg)  
UNCLASSIFIED

# 天线模式可视化工具

![](images/a986e05024cdd609446be437615bb0d850e1e3eb3cb7aabf01fcf3a5340a264c.jpg)

# 控制：

- 点击并拖动以改变视角  
滚动鼠标中键进行缩放  
定位平面提供数值

- Shift+点击并拖动移动平面

![](images/4a61bfa4c178502d760ed3ca5a63b522a553785e586c9253252040e0d9e6849b.jpg)  
DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQQD.

20

# - 每个平台都有以下默认值:

# - 特性

- 声 100 dB-20uPa at 1kHz  
- 红外 1000 w/sr  
Inherent Contrast 0.5 (Used by IR sensors)   
- 光学 1000 m^2  
- 雷达 1000 m^2

使用默认值时，命令窗口会有相关输出

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQDD.

UNCLASSIFIED

![](images/2f46a93c520958ce640453c8bb57de3d83940996e5de68ac7f1890b09e8ef86a.jpg)

# 重温学习目标

![](images/b25fc34f16072481383a778339b1bff5e6411410c09df5b9b97d8a063de9e241.jpg)

# - 包括:

- 定义平台的特性  
- 添加一个特性到平台  
- 使用平台组件管理  
- 使用天线模式可视化工具

![](images/417cc588b145d7a2ed9430782b8dec7f781445022bc352c5710a0fc19257e7be.jpg)

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

![](images/a145ec4f32233cff0be9b94c7fe51f5e52d4dd4d579500c56487143a84fb2944.jpg)

23

# 6.1.4.2.3.传感器跟踪7_AFSIM_User_Training_Sensors_Tracks

本文为afsim2.9_src\training\user\4_Sensors\

slides\7_AFSIM_User_Training_Sensors_Tracks.pptx的翻译。

![](images/812ec8bcde4b17a00b4d1cbf134371c60f24cf4db46e6831e6ef74d5337bd83c.jpg)

UNCLASSIFIED

![](images/c3d51ab0d35530ec00032bfec859b8c6a547ea33972e3037b0756b8538f40264.jpg)

![](images/ca87c4139744df7d1aeb4b9e0d2b7fea1cca8da7798e204e19d392314b33d300.jpg)

Integrity $\star$ Service $\star$ Excellence

# AFSIM用户培训

# 7-传感器跟踪

本文档由杨石兴翻译，该资料做为《AFSIM2.9参考手册》的一部分。没有《AFSIM2.9参考手册》的加杨石兴微信领取：13324598743

AFRL/RQQD

美国空军研究实验室

# ·包括

- 定义传感器  
- 向平台中添加传感器  
- 向平台中添加任务处理器和跟踪处理器  
- 创建事件输出文件

![](images/9154f935488cc924c16b8494dc43de8d463c0f9e07cc413dac376a0fc0a5efe3.jpg)

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

2

![](images/3c08636ba2940b2e1e6b816eec842eb01afe15eb04f741e77188889ae8d68bc0.jpg)

UNCLASSIFIED

# 相关坐标变换

![](images/f1f7a0091270f832c13c0efb7ebdb2f66f06e680e9ec9eba764346a9cbd53293.jpg)

- AFSIM使用'IEEE Std. 1278.1-1995; Standard for Distributed Simulation - Application Protocols'标准中规定的相关坐标系统。

世界坐标系(WCS)

- 标准的WGS-84椭球体，使用右手系

实体坐标系(ECS)

以平台为中心的局部坐标系. 也是一个右手系

- 部件坐标系(PCS)

- 实体上的部件为中心的局部坐标系(比如传感器，武器等). 也是一个右手系。

原点在地心

$+x$ 轴穿过ON，OE   
+Y轴穿过ON,90E   
+Z轴穿过90N（北极）

原点在平台中心

$+x$ 轴穿过平台前方

+轴穿过右侧

(向下看×铀)

+2轴穿越底部

Yaw是绕Z轴旋转. 正的yaw是向右侧

Pitch是绕Y轴旋转.正的pitch是沿 $+\mathbf{X}$ 轴方向变大

Roll是绕X轴旋转.正的roll沿+Y轴方向下降

![](images/881286b14fbdd4c10153b2e72229fac9fade4e31fe833551097c13b99c0a523f.jpg)

$+X$ 向前  
$+Y$ 向右  
+Z各下.   
- Yaw绕Z轴转. 正的yaw沿'nose'向右   
Pitch绕Y轴转. 正的pitch沿'nose'向上   
- Roll是绕X轴转. 正的roll沿'rightwing'降低

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

4

![](images/9771bbea7bb108b7afcfd03ae766ac57db60b1be5d065474a72b24c7bfd4178b.jpg)

# UNCLASSIFIED

# 传感器相关约定

![](images/848824885a2082c71d44e1ef9e73396d9c49a4819bdc03739e484c3debb9e44e.jpg)

![](images/bbe72d634a995b51e0dcd277326ecbcb9d756b3b767c8bbe65e6e17f5de8a22a.jpg)  
有几个参数会影响传感器的方位角和仰角覆盖范围。

- 旋转极限(SlewLimit)，有时称为万向节极限或视场，定义铰接部件相对于 ECS 的旋转范围。  
波束宽度(BeamWidth)天线波束宽度的中心受旋转极限限制半波束宽度可以超过旋转极限。  
- 扫瞄极限(Scan Limits)定义传感器模式的搜索区覆盖范围，包括模式中心的左侧和右侧。  
- 机动极限(Cue Limits)经常小于旋转极限   
视场极限(Field of View Limit)大于等于扫描极限覆盖模型中心的左侧和右侧可以被用于一个过滤器，不在视场中的目标会被忽略优化不必要的检测，使模型运行速度更快

- 在setup.txt中添加

"include_once platforms/single_largeSAM.txt"

- 可以在模型文件夹中找到  
- 做一个本地的拷贝

- 从模型文件夹中将其拷入到我们的工程想定当中

- 打开这个文件

# setup.txt

```txt
include_once platforms/common.txt   
include_once platforms/ship.txt   
include_once platforms/car.txt   
include_once platforms/tank.txt   
include_once platforms/bomber.txt   
include_once platforms/satellite.txt   
include_once platforms/single_large_sam.txt   
12   
13 
```

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19.

Other requests for this document shall be referred to AFRL/RQQD.

6

![](images/73811470c2e4d067d463a4979fd4367620eca07223cf29dc04239d88a62a9054.jpg)

# UNCLASSIFIED

# 单枚大型地空导弹(SAM)1

![](images/ccb77766b14ffb73c8b55f0b34e485cf350b0c34929cb0ffe356b16794f72f0e.jpg)

```txt
platforms/single_largeSAM.txt
1 # New file created by AFSIM-Wizard
2
3 # * * *** Demonstrations input file *** * 
4 # * *** UNCLASSIFIED * 
5 # * * *** *** * 
6 # * * *** *** * 
7 include_onceWeapons/sam/largeSAM.txt
8 platform_type SINGLE LARGE SAM WSF PLATFORM
9 icon TWIN_BOX
10 platform_type SINGLE LARGE SAM WSF PLATFORM
11 category ENGAGEMENT
12 infrared signature VEHICLE_INFRARED_SIGNATURE
13 optical signature VEHICLE_OPTICAL_SIGNATURE
14 radar signature VEHICLE_RADAR_SIGNATURE
15 trackmanager
16 filter FILTER Tactics end_filter
17 end_trackmanager
18 comm cmdr_net TEAM_DATALINK
19 network_name <local:slave>
20 internal_link data_mgr
21 internal_link task_mgr
22 end_comm
23 comm sub_net TEAM_DATALINK
24 network_name <local:master>
25 internal_link data_mgr
26 internal_link task_mgr
27 end_comm
28 comm sub_net TEAM_DATALINK
29 network_name <local:master>
30 internal_link data_mgr
31 internal_link task_mgr
32 end_comm 
```

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19.

Other requests for this document shall be referred to AFRL/RQQD.

platforms/single_largeSAM.txt   
```txt
34   
35 zone full_kinematic   
36 circular   
37 maximum_altitude 30 km   
38 maximum_radius 25 nm   
39 end-zone   
40   
41 sensor acq ACQ_RADAR   
42 on   
43 internal_link data_mgr   
44 end SENSOR   
45   
46 sensor ttr TTR_RADAR   
47 end SENSOR   
48   
49 weapon sam LARGE_SAM   
50 quantity 16   
51 endweapon   
52   
53 processor data_mgr WSFTRACKPROCESSOR   
54 purge_interval 60 seconds   
55 end Processor   
56   
57 processor task_mgr WSF_TASK_PROCESSOR   
58 end Processor   
59   
60 endPLATFORM_type   
61 
```

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

8

![](images/3a8564b748236a6d2cfb038ac06f6574a99007b808818e07267d7975affb42d8.jpg)

# UNCLASSIFIED

# 包含传感器文件

![](images/356f3f7b21e840523b61a35b2ff4ded4e00da3f03b0346e62d2d2c5412a56561.jpg)

- ttr_radar.txt在models文件夹中可以找到  
- 创建并打开acq_radar.txt文件

- 确保创建在了floridistan目录下，而不是创建在了models目录下

platforms/single_largeSAM.txt   
```txt
2 # \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*   
3 #\* \* \* \* \* \* \* \* \* \* \* \* \* \* \* \* \* \* \* \* \* \* \* \* \* \* \* \* \* \* \* \* \* \* \* \* \* \* \* \* \* \* \* \* \* \* \* \* \* \* \*  
4 #\* \* \* \* \* \* \* \* \* \* \* \* \* \* \* \* \*  
5 #\* \* \* \* \* \* \* \* \* \* \*  
6 #\* \* \* \* \* \* \* \* \* \*  
7 include_onceWeapons/sam/large_sam.txt  
8 include_once sensors/radar/acq_radar.txt  
9 include_once sensors/radar/ttr_radar.txt  
10 include_once sensors/radar/ttr_radar.txt  
11 platform_type SINGLE LARGE SAM WSF PLATFORM  
12 icon TWIN_BOX  
13 category ENGAGEMENT  
14 
```

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19.

Other requests this document shall be referred to AFRL/RQQD.

<table><tr><td>antenna_pattern</td></tr><tr><td>antenna_pattern ... end_antenna_pattern</td></tr><tr><td>antenna_pattern &lt;pattern-name&gt; &lt;pattern-type-name&gt; Common commands ... Available Antenna Patterns Commands ... end_antenna_pattern</td></tr><tr><td>Overview</td></tr><tr><td>antenna_pattern is used in transmitter and receiver commands to define the gain of an antenna for communication and sensor devices. &lt;pattern-name&gt; Specifies the name of the antenna pattern. &lt;pattern-type-name&gt; Specifies one of the Available Antenna Patterns: · Azimuth/Elevation Table · Uniform or Constant Pattern · Circular sine(x)\\(x Pattern · Rectangular sine(x)\\)x Pattern · Cosecant Pattern · Electronic Steered/Scanned Array (ESA) Pattern · ALARM Antenna Pattern File · GENAP Pattern · Complex Electronic Steered/Scanned Array Pattern · Shaped Electronic Steered/Scanned Array (ESA) Pattern</td></tr><tr><td>Common Commands</td></tr><tr><td>The following commands can be used in any of the antenna pattern definitions: minimum_gain &lt;db-ratio-value&gt; The minimum gain that will be returned. Default: -300 db</td></tr></table>

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQDD.

10

![](images/d6e2b5d412136ad9a1f924ccfcfcb29f437fd26df538ddea9b22f71a8fbfc90a.jpg)

# UNCLASSIFIED

# 定义雷达传感器

![](images/1f1aebc52d5823c7553da1009fa0831690ed5c41b33228476e3b3dd521767186.jpg)

# - 先从天线模式开始(antenna pattern)

```txt
sensors/radar/acq_radar.txt   
3 antenna_pattern ACQ_RADARAntENNA   
4 rectangular_pattern   
5 peak_gain 35 dB   
6 minimum_gain -10 db   
7 azimuth_beamwidth 10 deg   
8 elevation_beamwidth 10 deg   
9 end_rectangular_pattern   
10 end.antenna_pattern   
11 
```

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQDD.

- 名称: ACQ_RADAR, 继承自 WSF_RADAR_SENSOR  
- 指定参数：

-one_m2detect_range探测范围优先于其它参数  
- frame_time帧时间决定报告时间

![](images/726bc6af9ca676f136a31a69d03e1ce3785ff3fb3edd1a01c00ffb14c2da17cf.jpg)

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQDD.

12

![](images/2ebcbb55e17aa3f36e8307ab95f6ed77d3b820f7916147bef90ae2ec37fdfc86.jpg)

UNCLASSIFIED

# 实践：发射机(Transmitter)/接收机(Receiver)

![](images/68b837e12d3520dd8fc27b689e05690ff5bd63036de4ed6b82644a69ec5cb382.jpg)

sensors/radar/acq_radar.txt

- 给传感器添加发射机与接收机

- 都需要使用到天线模式(antenna pattern)  
- 噪声将被调整以匹配指定的探测范围。

# Transmitter

Antenna Pattern   
Transmit Power: 1000 kilowatts   
- Operating Frequency: - 3000 megahertz   
- Internal Loss
- 2 decibels

# Receiver

Antenna Pattern   
- Operating Bandwidth: - 2 megahertz   
- Noise Power: -160 decibel watts   
- Internal Loss
- 7 decibels

- 发射机和接收机使用同一个天线模式(antenna pattern)  
- 噪声将被调整以匹配指定的探测范围。

sensors/radar/acq_radar.txt   
```txt
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
end SENSOR 
```

```txt
DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD. 
```

14

![](images/f858f508f37c51e28ece5cbffe5453caae67fde16deeccca05c591b74c93b062.jpg)

# UNCLASSIFIED

# 天线模式可视化

![](images/63e4be516b28060fd8741d7bb374a53152ece0b5d607637f4cc59f99f7bf5f87.jpg)

保存所有的文件，对着ACQ_RADARAntENNA点右键选择visualize

![](images/bcc79c99fd228b9cf531de4dd809033e654536d6795f475be8223df4e5128ca1.jpg)  
DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

- 定义跟踪请求  
- 定义雷达对外报告哪些属性  
- 使用end SENSOR结束定义

sensors/radar/acq_radar.txt   
```c
38 probability_ofFalse alarm 1.0e-6   
39   
40 required_pd 0.5   
41 swerling(case 1   
42   
43 hits_to_establish_track 3 5   
44 hits_to Maintain_track 1 5   
45   
46 track_quality 0.6 // used in tactics   
47   
48 reports_range   
49 reports_bearing   
50 reports_elevation   
51 reports_iff   
52   
53 end SENSOR   
54 
```

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQDD.

16

![](images/86b39a07e24d9dcea7f260e5ee1f9104479f1b7815cccc40a0660a2af194eaff.jpg)

![](images/8eb5147407113b458b9576ff844378c3f6dcc4b580f59735b24c97aa70c8d876.jpg)

DISTRiBtion C. Distribution authorized to U.S. Government Agencies and the contractors, 9-Aug-19.

Other requests this document shall be referred to AFRL/RQQD.

sensors/radar/acq_radar.txt   
11   
12 sensor ACO_RADAR WSF_RADAR_SENSOR   
13 one_m2detect_range 50 nm   
15 maximum_range 150 nm   
16   
17 antenna_height 5 m   
18   
19 frame_time 10 sec   
20   
21 scan_mode azimuth_and_elevation   
22 azimuth_scanlimits -180 deg 180 deg   
23 elevation_scanlimits 0 deg 50 deg   
24   
25 transmitter   
26 antenna_pattern ACO_RADAR AntENNA   
27 power 1000 kw   
28 frequency 3000 mhz   
29 internal_loss 2 db   
30   
31   
32 receiver   
33 antenna_pattern ACO_RADAR ANTENNA   
34 bandwidth 2 mhz   
35 noise_power -160 dbw // will be calibrated for $1\mathrm{m}^2$ 36 internal_loss 7 dB   
37 end_transmitter   
38   
39 probability_ofFalse alarm 1.0e-6   
40 required_pd 0.5   
41 swerling(case) 1   
42   
43 hits_to_establish_track 3 5   
44 hits_to Maintain_track 1 5   
45   
46 track_quality 0.6 // used in tactics   
47   
48 reports_range   
49 reports_bearing   
50 reports_elevation   
51 reports iff   
52   
53   
54   
end SENSOR

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

18

![](images/f661db520ab70dafd6d0c1e8d9c5356804140563f35cb52bb43130761f472465.jpg)

# UNCLASSIFIED

# 传感器上报

![](images/c4b729e21582c485a52ec638ef235144ce723a2a55fa9db8f11523f7efbbd360.jpg)

- 必须非常明确的定义传感器要将数据上报到哪里默认情况下是不上报  
- 跟踪处理器(Track processor)维护着一个主跟踪列表(Master Track List)  
- 任务处理器(Task Processor)监视主跟踪列表(Master Track List)后面会讨论

internal_link（或processor）是用于连接平台内部的组件此链接是单向的！

platforms/single_largeSAM.txt   
```txt
41   
42 sensor acq ACQ_RADAR on   
43 internal_link data_mgr   
44   
45 end SENSOR   
46   
47 sensor ttr TTR_RADAR   
48 end SENSOR   
49   
50 weapon sam LARGE_SAM   
51 quantity 16   
52 endweapon   
53   
54 processor data_mgr WSFTRACKPROCESSOR   
55 purge_interval 60 seconds   
56 end Processor   
57   
58 processor task_mgr WSF_TASK_PROCESSOR   
59 end Processor   
60   
61 endPLATFORM_type 
```

# 在平台上，轨迹的表示形式实际上是一个

# WsfLocalTrack

# - 它是由一个或多个WsfTrack对象组合而成的，这些对象被称为“原始轨迹”

# - 这些原始轨迹是可以访问的

![](images/c353dc03a83a6ebc05fbc6c557ee1a5312ae93d371851da987217e162e1a8ef7.jpg)

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

20

![](images/cfd9f804ada5d6598fc49b9011ef6f4e0bc590cf34a0ee49d0fa6dc1dfe2dfbf.jpg)

# UNCLASSIFIED

# 关于跟踪的很好的资源

![](images/1dbdc082c1900f61994ce3819b81bb927bab162ba748ae727c54239a3ca498bb.jpg)

![](images/4ca95fbef99664bd62e63c6b011c1cc3486966931f993821a8b1c102136055b8.jpg)

![](images/eb15fe17235cfd24b36d000adf9bf252806895511132695726a18caa6713d124.jpg)

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

sensors/radar/ttr_radar.txt   
```txt
14   
15 sensor TTR_RADAR_WSF_RADAR_SENSOR   
16 selection_mode multiple   
17   
18 slew_mode azimuth_and_elevation   
19 azimuth_slewlimits -180 deg 180 deg   
20 elevation_slew限度 0.0 deg 80.0 deg   
21   
22 mode_template one_m2detect_range 35.0 nm   
23 maximum_range 100.0 nm   
25 antenna_height 4.0 m   
27   
28 transmitter antenna_pattern TTR_RADAR_ANTENNNA   
30 power 1000.0 kw   
31 frequency 9500 mhz   
32 internal_loss 2 db   
33   
34   
35 receiver antenna_pattern TTR_RADAR_ANTENNNA   
37 bandwidth 500.0 khz   
38 noise_power -160 dBw   
39 internal_loss 7 dB   
40 end_receive   
41   
42 probability_of,false alarm 1.0e-6   
43 required_pd 0.5   
44 swerling(case 1   
45   
46 reports_range   
47 reports_bearing   
48 reports_elevation   
49 reports_velocity   
50 end_mode_template   
51 
```

sensors/radar/ttr_radar.txt   
```txt
51 mode ACQUIRE maximum_request_count 1   
52 scan_mode azimuth_and_elevation azimuth_scanLimits -5 deg 5 deg elevation_scanlimits -5 deg 5 deg   
53 frame_time 2.0 sec   
54   
60   
61 hits_to EstablishTrack 35 hits_tomaintainTrack 13   
62   
63   
64 track_quality 0.8 // used in tactics   
65   
66 end_mode   
67   
68 mode TRACK maximum_request_count 6   
69   
70 scan_mode azimuth_and_elevation azimuth_scanlimits -1 deg 1 deg elevation_scanlimits -1 deg 1 deg frame_time 1.0 sec   
71   
72   
73   
74   
75   
76 hits_to-establishTrack 35 hits_tomaintainTrack 13   
77   
78   
79 track_quality 1.0 // used in tactics   
80 end_mode   
81   
82 end SENSOR 
```

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19.

Other requests for this document shall be referred to AFRL/RQQD.

22

![](images/0dc0e76597a0016486666ce795bfc7914696862931bb636ef12b5708439348f0.jpg)

# UNCLASSIFIED

# 新的想定文件

![](images/e6afcab833fe72a30407ecd52fa867676fe01bf2f143d5dbdcdb61bb6391e52a.jpg)

# - 在floridistan.txt文件中加入新的想定文件

# floridistan.txt

```ruby
1 # New file created by AFSIM Wizard  
2 log_file output/jacksonabad.log  
3 include_ once setup.txt  
4 include_ once scenarios/blue_laydown.txt  
5 include_ once scenarios/red_laydown.txt  
6 include_ once scenarios/blue_sams.txt  
7 include_ once scenarios/red_sams.txt  
8 include_ once scenarios/blue_sams.txt  
9 event_output file output/jacksonabad.evt end_event_output  
10 event_pipe file output/jacksonabad.aer end_event_pipe  
11 end_time 1 hour 
```

- 在地图中将sam_1加进去

- 将SINGLE_largeSAM放在塔克旁边

- 创建新的平台

- 选择类型，名字叫“sam_1”  
- 平台类型选择'SINGLE_largeSAM'  
- 想定文件选择scenarios\blue_sams.txt文件  
- 点击OK

![](images/71fbf8f971b12e0b6c43f50c908b3b73b2d0a7af564fd1c9fc53443ae21c7d1e.jpg)

![](images/853c1af3e381e0880ad4d88aa4416de0337aaded328ad6b0ede62490580da91e.jpg)

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

24

![](images/a8a97fd942848ff09c0e3897d923a84b7fcdba528f0785642b5071922739b524.jpg)

UNCLASSIFIED

# 改变SAM的阵营

![](images/30cf186fbbf808c05cbcc85613580928ab8f93a02dbb0e930c8ec5bbe5820cd6.jpg)

- 将阵营改为 blue  
- 朝向改为朝向90deg方向

![](images/4d07d8a5aadbbadbb7686f0087608ebf7047f1e5949b040afce3b52d2f00f9bf.jpg)

![](images/2c0fe1b7d83848cdf6a620bbe28d48b7f1b999a657c0d2544c832083ff433942.jpg)

·运行！！！

![](images/7d6f5346c27ae6e76f19213f2f7920e2a83a21e90d72572444b99356f19ac027.jpg)

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

26

![](images/bb8d0b451e1267c1ff82b4295b32b06ff7394dc5d4ab07359d4ed59cec185045.jpg)

# UNCLASSIFIED

# 传感器和通信流程

![](images/a9ddad1f76d37fe28a147c2a97c863e25042c0cbd5bc7168f337aabc69187567.jpg)

- 从几何角度来看，传感器或通信尝试的一般流程，不包括系统特定的处理。

- 计算到目标的距离，并与模式特定的minimum_range和maximum_range进行比较。如果不在限制范围内，则抑制其余的检测处理。  
- 计算目标的高度，并与模式特定的minimum_altitude和maximum_altitude进行比较。如果不在限制范围内，则抑制其余的检测处理。  
- 更新子系统的方向以反映任何潜在的提示（计算部件坐标系和指示坐标系）。  
- 计算目标相对于扫描坐标系的方向，并与azimuth field of view和elevation_field_of_view进行比较。如果不在限制范围内，则抑制其余的检测处理。  
- 设置发射器/接收器的波束位置（即：计算波束的波束坐标系和天线坐标系）。  
- 在此之后，处理传感器特定参数。对于雷达之类的东西，将使用目标相对于发射机和接收机BCS（以及可能的电子扫描系统的ACS）的方向来推导天线增益。

- 在“setup.txt”文件中，添加如下：

- "include_once event_output.txt"并创建 event_output.txt

setup.txt   
UNCLASSIFIED   
```txt
include_once platforms/bomber.txt   
include_once platforms/satellite.txt   
include_once platforms/single_large_sam.txt   
include_once event_output.txt   
13 
```

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQDD.

28

![](images/24d2862a4f5e6b6dce99848bf31caac0d7200b07262029332270ad1a827ce97d.jpg)

实践：启用事件输出

![](images/12e1296905b944d50302786297bc48a1887474311884e8f9b42b47008334f13b.jpg)

- 启用以下事件输出：

- 传感器失跟   
- 传感器初始化  
发送/收到消息

event output.txt   
```txt
2   
3 event_output   
4   
5   
6   
7   
8   
9   
10 end_event_output   
11 
```

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19.

Other requests this document shall be referred to AFRL/RQQD.

·注意：在有两个事件输出块的情况下  
- 同一个设置如果有冲突，则以最新的设置为准  
- 启用某项输出时要很谨慎！  
- Run!!!

event_output.txt   
```txt
2 event_output   
3 enable LOCAL Track DROPPED   
4 enable LOCAL Track INITIATED   
5 enableMESSAGE RECEIVED   
6 enableMESSAGE_TRANSMITTED   
7 enable SENSOR Track DROPPED   
8 enable SENSOR Track INITIATED   
9 end_event_output   
10 
```

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

30

![](images/137c360a7824d3515d79e6c63a9013f6c8a92df58f428ca4ebc219c3c0c62cdc.jpg)

# 事件输出到文件示例

![](images/af8735c70cdaf8d9780ba39651e8ff55a6a118c8c267d3361e3fc0b02d2f2305.jpg)

output/jacksonabad.evt   
```txt
1 0.00000 LOCAL Track Initialized bomber tank_1 TrackId: bomber.1\  
2 Start_Time: 0.00000 Update_Time: 0.00000 Update Counts: 0 Quality: 0!  
3 Originator: LLA: 30:17:16.62n 81:04:35.31w 9144 m  
4 Source_TrackId: bomber.1 Update_Time: 0.00000 Update Count: 0 Quality  
5 0.00000 LOCAL Track Initialized bomber tank_2 TrackId: bomber.2\  
6 Start_Time: 0.00000 Update_Time: 0.00000 Update Count: 0 Quality: 0!  
7 Originator: LLA: 30:17:16.62n 81:04:35.31w 9144 m  
8 Source_TrackId: bomber.2 Update_Time: 0.00000 Update Counts: 0 Quality  
9 20.00000 SENSOR Track Initialized sam-1 bomber Sensor: acq TrackId: sam-1  
10 Start_Time: 20.00000 Update_Time: 20.00000 Update Counts: 0 Quality: 0!  
11 Target Truth: Name: bomber Type: BOMBER Side: red \  
12 Originator: LLA: 30:20:00.00n 81:40:00.00w 5 m  
13 Track: LLA: 30:17:23.56n 81:07:55.79w 9144 m Flags: 3RBE \  
14 Truth: LLA: 30:17:23.56n 81:07:55.79w 9144 m Difference: 1.17916e-14  
15 Track: Range: 52474.2 m Bearing: 95.2183 deg Elevation: 9.79806 deg  
16 Truth: Range: 52474.2 m Bearing: 95.2183 deg Elevation: 9.79806 deg  
17 20.00000 LOCAL Track Initialized sam-1 bomber TrackId: sam-1.2 \  
18 Start_Time: 20.00000 Update_Time: 20.00000 Update Counts: 0 Quality: 0!  
19 Target Truth: Name: bomber Type: BOMBER Side: red \  
20 Originator: LLA: 30:20:00.00n 81:40:00.00w 5 m \  
21 Track: LLA: 30:17:23.56n 81:07:55.79w 9144 m Flags: L3RBE \ 
```

"track"命令为平台“预定义”轨迹，这些轨迹在模拟开始时初始化于主轨迹列表中。

# output/jacksonabad.evt

```yaml
8 Source_TrackId: bomber.2 Update_Time: 0.0000 Update_Count: 0 Quality: 0.5   
9 20.0000 SENSORTracks Initiated sam-1 bomber Sensor: acq TrackId: sam-1.1   
10 Start_Time: 20.0000 Update_Time: 20.0000 Update_Count: 0 Quality: 0.8 Domain: air Type: M   
11 Target Truth: Name: bomber Type: BOMBER Side: red \   
12 Originator: LLA: 30:20:00.00n 81:40:00.00w 5 m \   
13 Track: LLA: 30:17:23.56n 81:07:55.79w 9144 m Flags: 3RBE \   
14 Truth: LLA: 30:17:23.56n 81:07:55.79w 9144 m Difference: 1.17916e-10 m \   
15 Track: Range: 52474.2 m Bearing: 95.2183 deg Elevation: 9.79806 deg \   
16 Truth: Range: 52474.2 m Bearing: 95.2183 deg Elevation: 9.79806 deg   
17 20.0000 LOCAL TRACK INITIATED sam-1 bomber TrackId: sam-1.2   
18 Start_Time: 20.0000 Update_Time: 20.0000 Update_Count: 0 Quality: 0.8 Domain: air Type: PC   
19 Target Truth: Name: bomber Type: BOMBER Side: red \   
20 Originator: LLA: 30:20:00.00n 81:40:00.00w 5 m \   
21 Track: LLA: 30:17:23.56n 81:07:55.79w 9144 m Flags: L3RBE \   
22 Truth: LLA: 30:17:23.56n 81:07:55.79w 9144 m Difference: 0 m \   
23 Track: Range: 52474.2 m Bearing: 95.2183 deg Elevation: 9.79806 deg \   
24 Truth: Range: 52474.2 m Bearing: 95.2183 deg Elevation: 9.79806 deg \   
25 Source_TrackId: sam-1.1 Sensor: acq Type: ACO_RARAD Mode: default Update_Time: 20.0000 Update_Cou   
26 100.0000 LOCAL TRACK INITIATED bomber_gbu-38_1 tank_1 TrackId: bomber_gbu-38_1.1 \   
27 Start_Time: 0.0000 Update_Time: 0.0000 Update_Count: 0 Quality: 0.5 Domain: unknown Type: P \   
28 Target Truth: Name: tank_1 Type: TANK Side: blue \ 
```

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

32

![](images/7583c9850be08be30f522a0bdccb31064a2893d62eca57f2315b4b70304be8d3.jpg)

# UNCLASSIFIED

# 主轨迹列表Master Track List

![](images/b035ae67fd51a80430572f52b740e879fb3f33759c01747d33d4cc8e9b7ab338.jpg)

- 每个平台有一个唯一的主轨迹列表Master Track List

可以从多个平台中的传感器输入数据  
- 使用track processor创建并维护

![](images/3b2632129044f09e0343465cbffad170ae659216a8b349da314e981cb05c3719.jpg)

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19.

Other requests for this document shall be referred to AFRL/RQQD.

- 一个平台可以有多个轨迹列表multiple track lists

- 一个是主轨迹列表Master Track List  
- 每个任务处理器(task processor)只能关联一个轨迹列表

![](images/5caaade8b25a222bd45ae7d1c45c894305c51c7c5584653613acb2a3d3f83235.jpg)  
DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

34

UNCLASSIFIED

![](images/90b495b38b4a278f47e5ff98e6b11c5733ccab9e49613a1cf8d600bfaa9945ff.jpg)

# 处理器可以过滤消息(Filter Messages)

![](images/54b4211174a483b42b5dd6e5357737f2f78dd5f883ee6b6890be1839a203f85f.jpg)

- 传感器产生轨迹消息   
通信设备从外部传感器收到的轨迹消息  
- 都传到处理器当中  
这些消息在到时达最终的目的地之前都可以被送往其它的处理器onmessage块可以响应这些消息  
- 消息可以被改变、延时、挂起

![](images/7ec71abd2ed4bf24db0a7a70cdc4caf237ce506f68bb743022a253783542ee05.jpg)  
DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

- 当收到消息时触发该处理器  
- 通过“internal_link”在通信组件 (comm), 传感器(sensor), 和其它处理器 processor) 之间通信.  
- 可以根据消息类型在内部响应进入不同处理流程

从帮助文档中的

"WSFScriptPROCESSOR"

<table><tr><td>Type String</td><td>Script Class</td></tr><tr><td>WSF_ASSOCIATION_MESSAGE</td><td>WsfAssociationMessage</td></tr><tr><td>WSF_CONTROL_MESSAGE</td><td>WsfControlMessage</td></tr><tr><td>WSF_IMAGE_MESSAGE</td><td>WsfImageMessage</td></tr><tr><td>WSF_STATUS_MESSAGE</td><td>WsfStatusMessage</td></tr><tr><td>WSF.droptrack_message</td><td>WsfTrackDropMessage</td></tr><tr><td>WSFtrack_drop_message
(See note below)</td><td></td></tr><tr><td>WSFtrack_message</td><td>WsfTrackMessage</td></tr><tr><td>WSFtrack_NOTIFY_message</td><td>WsfTrackNotifyMessage</td></tr><tr><td>WSF Video Message</td><td>WsfVideoMessage</td></tr></table>

<table><tr><td>Type String</td><td>Script Class</td></tr><tr><td>WSF_TASK_ASSIGN_MESSAGE</td><td>WsfTaskAssignMessage</td></tr><tr><td>WSF_TASKiatesMESSAGE</td><td>WsfTaskCancelMessage</td></tr><tr><td>WSF_TASK_CONTROLMESSAGE</td><td>WsfTaskControlMessage</td></tr><tr><td>WSF_TASK_STATUSMESSAGE</td><td>WsfTaskStatusMessage</td></tr><tr><td>WSF_TASK_ASSIGNMESSAGE</td><td>WsfTaskAssignMessage</td></tr><tr><td>WSF DROPTRACK_MESSAGE</td><td>WsfTrackDropMessage</td></tr><tr><td>WSFTRACK DropsMESSAGE</td><td></td></tr></table>

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

36

![](images/b8a1e37d617fbe691e411958a314545361911e71d2e10862198fa43ab0e34807.jpg)

# UNCLASSIFIED

# 脚本处理器 - on_message

![](images/7f2848909c36b17504683fc59c4c3e5dd64fbc53ddd79e85d4f09e9ef9b67cf8.jpg)

- 可以处理很多类型消息，每个有自己的流程  
- "default"用来响应没有处理的消息类型

- 这个类似switch和case.  
- 以下内容是一个响应和使用MESSAGE的示例。

```txt
on_message
type WsFTRACKMESSAGE
script
WsfTrackMessage trackMsg = (WsfTrackMessage)MESSAGE;
writeln(TIME NOW, " -- Received message: ", trackMsg Track().TrackId().ToString());
end script
default
script
writeln(TIME NOW, " -- Received message of type: ",MESSAGE.Type));
end script
end_on_message 
```

- 注意我们可以将MESSAGE转换到我们响应的类型，因为type已经确保了是该消息类型
- 这样我们就可以在脚本中处理各消息类型

- 传感器探测到目标则就会创建一个轨迹

- 探测到目标在什么时刻会转化成轨迹呢？

- 接着轨迹就被送往轨迹处理器(Track Processor)

- 轨迹是如何到达处理器的？  
- 主轨迹列表在哪儿维护？

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

38

![](images/3eebcce551b11417c9fe0cbdb8f5b806e634dc931c5ee02c51a70687037774cb.jpg)

UNCLASSIFIED

# 学习目标回顾

![](images/e5cd1f4071be0f355078d891897d2004cd354f65085d3975638e7d85d24e0cf1.jpg)

·包括

- 定义传感器  
- 向平台中添加传感器  
- 向平台中添加任务处理器和跟踪处理器  
- 创建事件输出文件

![](images/be614207faf0de34782251dae0791cccfe9c327f73460a2b37e3a00c7d003297.jpg)

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

# 6.1.5. 脚本 5_Scripting

# 6.1.5.1. 脚本语言与脚本处理器

8_AFSIM_USER_Training_ScriptingLanguage_ScriptProcessors

# 6.1.5.1.1. 本节想定解析

本节想定为：

afsim2.9_src\training\user\5_Scripting\scenes\scenarios\solutions\8_Scripting_Proceessors\floridistan\floridistan.txt

![](images/883e3cc28c10c519d25ff618ae71631bd88231d6d821d879d54979c1f1d780f1.jpg)

# 红方兵力

一艘航母 ship_1

定义了一个循环的路线

- 一架轰炸机 bomber_1（另一架bomber_2与bomber_1配置相同）

定义了一个路线，先到陆地，再回到海上  
。 设置了固定跟踪 tank_1, tank_2，只有跟踪了才能投弹  
挂了4枚GPS制导炸弹，最大允许同时齐射2枚

设置当在gps制导炸弹的打击范围内时才开火(doublelarmeters=18520)   
- 打击 tank_1, tank_2 的炸弹同时开火，针对每个目标又齐射 2 枚，相当于四枚一次打完

GPS制导炸弹

本例中被挂在了bomber_1上  
。 弹的雷达特征 RCS 被设置为了常数 $1 m^{2}$ , 换算为 dbsm 则是 0

# 蓝方兵力

- 一个在天上的卫星 satellite_1

定义了一个700km的轨道

- 两辆坦克 tank_1, tank_2  
一个车辆

定义了一个向北行进的路线

一个地空导弹阵地sam_1

下挂16枚地空导弹（但未设置发射条件）  
。下挂 2 部雷达, 一部 150 海里 (acq, 开启), 一部是 100 海里 (ttr, 默认关), 在想定开始后, acq 雷达陆续会探测到红方的战斗机以及其发射的 4 枚 GPS 制导炸弹  
。 其它定义包括通信、区域等在推演时均未有动作

# 6.1.5.1.2. 本节PPT资料

本文为afsim2.9_src\training\user\5_Scripting\slide\

8_AFSIM_USER_Training_ScriptingLanguage_ScriptProcessors.pptx 的翻译。

![](images/3a67bd2cd39c2fa115b551f519a5fa87e38be3167cfda79bd12a4829382c6e9f.jpg)

UNCLASSIFIED

![](images/020e0fb8fc4fbea77fe44d5b1e79df28f4183a400dbae35744af14e8b0336889.jpg)

![](images/58b3e02b73178114eb6b1633ace57cc60b0b6a6c68b6b4778921b165cb058cd2.jpg)

# AFSIM用户培训8-脚本语言与脚本处理器

本文档由杨石兴翻译，该资料做为《AFSIM2.9参考手册》的一部分。没有《AFSIM2.9参考手册》的加杨石兴微信领取：13324598743

Integrity $\star$ Service $\star$ Excellence

AFRL/RQQD美国空军研究实验室

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQQD.

- 将学习到以下内容:

- AFSIM脚本语言  
- 使用脚本处理器processor

![](images/9e58932cc24c4f17e840c9ad7c9382df376990f743527704583bdf92e90ffa7a.jpg)

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQQD.

UNCLASSIFIED

![](images/9d0b97a23bb6e14e5630aceea273d38fe626d28fe5e1cae19944f61e0995c344.jpg)

# 概览

2

![](images/c9c278f32f912a7578e2b5394e5cd238db352ec760346fb7991c4a0aabc7be86.jpg)

# AFSIM提供用户自定义脚本语言

- 用户可以基于仿真事件来使用复杂的指令集  
- 语法上与C#和Java类似   
- 需要基本的编程技能

- 块结构化

- 没有关于缩进、换行等的规则。  
- 每行以分号结尾。  
- 变量在使用前必须声明。  
- 注释行以井号（#）或 $\mathbb{C} + +$ 风格的注释（//或I...I）开头。

·作用域

- 级别：全局(Global)、平台(Platform)、处理器(Processor)或行为(Behavior)。  
- 脚本块的有效插入点可分布在模拟输入的许多位置。

# - 基本类型

- int - 一个32位整数（例如：int prime5 = 11;）  
- bool - 一个布尔值（true 或 false）  
- double - 一个双精度浮点数  
string - 一个字符组成的字符串

# 运算符

- 方法调用：., ->  
一元运算符：！，+，-  
- 算术运算符：\*, /, +, -   
- 关系与相等运算符：<，<=，>，>=，==，!=  
逻辑运算符：&&，||  
- 赋值运算符：=，+=，-=，\*=，/=

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQQD.

4

![](images/5d0f213fba01bf13fee5f59147c49753ab66b38379074ee2090fa5325e62e89d.jpg)

# UNCLASSIFIED

# 静态复杂类型

![](images/276e37fbe38755cd6bce2eeff9007a9ab787b6504f37f316cdbaad38df1d3622.jpg)

-BUILDIN_   
Calendar   
- Earth   
Math   
- Moon   
Sun   
- System

![](images/b46f8a4e6ff8bb8b8b5b0c3cace26afb28963d4d06674324757041e29d1e256d.jpg)

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQQD.

6

![](images/4920edfbba5a564b0f70ef35edb57ac811bd670d641dcf7a9604337306fb09a1.jpg)

UNCLASSIFIED

# 复杂变量类型

![](images/1e4ded4f38bbe3b094655904217c28e1f79f7df4d5cf11043d252c8e9820c3a9.jpg)

# - 容器

- Array   
- Map   
- Set   
- Vec3

# - 其它

- QuadTree   
Calendar   
- Signal   
-Struct   
- FileIO   
- string

- Array $< \mathrm{T} >$

- 和C++ STL库中的array类似  
- T是模版，使用时需要换成数组中实际存储的类型

```txt
Array < int > myIntArray = Array < int >();  
myIntArray.PushBack(42);  
writeln("Array size="，myIntArray.Size()，" and the first value="，myIntArray_FRONT());  
// Array size= 1 and the first value= 42 
```

Map < T1, T2 >

和C++ STL库中的map类似  
- T1是key类型，T2是data类型。

- Set<T>

- 和 $\mathrm{C} + +$ STL库中的set类似  
- 存储唯一的值，插入其中就会进行排序。

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQQD.

8

![](images/be89bba3ffa5fc04f3830ace4062e340935c7fc6f54f2918ee5636526824663b.jpg)

# UNCLASSIFIED

# 其它脚本类型…

![](images/c54cd137e2016bf1e1916be6cce02ebefa3e9e25f2e33d007b9bdf2ae3f50793.jpg)

string

string sValue;   
int iValue $= 42$ .   
iValue $=$ iValue $+4$ .   
sValue $=$ (string)iValue;//sValue now contains the string "46"   
iValue $=$ (int)sValue; //iValue now contains the integer 46   
dValue $= 12.345$ .   
dValue $=$ dValue-2.0;   
sValue $=$ (string)dValue;//sValue now contains the string "10.345"   
dValue $=$ (double)sValue; //dValue now contains the double 10.345

FileO

script_variables FileIO gOut $=$ FileIO();   
endScript_variables   
script void RecordPlatformName(string aFileName, WsfPlatform aPlatform) gOut.Open(aFileName, "append"); gOut.Writeln(aPlatform.Name()); gOut.Close();   
endcript

# Methods

int Length()

The current number of characters in the string.

bool Contains(string aSubString)

Returns true if the string contains the provided sub-string

bool StartsWith(string aSubString)

Returns true if the string starts with the provided sub-string.

bool EndsWith(string aSubString)

Returns true if the string ends with the provided sub-string.

string Substring(int aStart)

string Substring(int aStart, int aEnd)

Returns a substring of the string. aStart and aEnd define the index range of the

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19.

Other requests for this document shall be referred to AFRL/RQQD.

# UNCLASSIFIED

# 脚本结构体

10

![](images/851cdb9940f4a996eae3dfe18d8fc51f3ffc3d157bea1f92e3edd2d1dee1bc46.jpg)

![](images/6f0a6d79438754e6f97aae9afb654a915830805372cd36bb2b32097a9ff9206a.jpg)

# - 定义可以用于其它脚本中的对象类型

# - 必须是全局的

# script_struct example

script_struct Car   
script_variables   
WsfGeoPoint position $=$ {}; Vec3 velocity $=$ {}; string color $=$ "red"; end.script_variables   
script void Honk() written(color, "car honks"); endcript   
end.Script_struct   
on_initlize   
# Create a new instance of the struct Car car $=$ Car(); # Assign some values. car.color $=$ "blue"; car.position.Set(39,-90,125.0); car.speed.Set(20,0,0); #Call a script car.Honk(); #Print the contents of the struct written(car); end_on_initlize

output:

```txt
blue car honks  
struct({"position": 39:00:00.0n 90:00:00.0w 125, "velocity": (20, 0, 0), "color": blue}) 
```

# - extern允许变量先使用后定义

1 script variables   
2 int global1 $= 2$ 3 end script variables   
4 platform p WsF PLATFORM   
5 execute at_time 1 s absolute   
6 extern int global2;   
7 writeln(MATH.Max(global1, global2));   
8 end execute   
9 end platform   
10 script variables   
11 int global2 $= 3$ 12 end script variables

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQQD.

UNCLASSIFIED

# 箭头 $(->)$ 操作符

12

![](images/edf5c5c0f1236f4509f4ff0881aa0ad8d599418f8ad7f978b83f8acb07de23f7.jpg)

![](images/c38064581ba60e462007d9b01c74572083b74e9afe7ef0514e9163c8f6bdd554.jpg)

# - 用户访问对象成员

```matlab
1 = platform p WSFPLATFORM
2 = script_variables
3 = double x = 1.75;
4 = endScript_variables
5 = endplatform
6 =
7 = platform q WSFPLATFORM
8 = execute at_time 1 s absolute
9 = WsfPlatform p = WsfSimulation.FindPlatform("p");
10 = writeln(p->x);
11 = writeln(p->y);
12 = end_execute
13 = endplatform 
```

```txt
Output: 1.75  
ERROR: Attribute does not exist (y).  
0 -> void execute_1() File: demo3.txt Line: 11 Col: 19 
```

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQQD.

- if, else if, else   
- while, do while   
for, foreach   
- break, continue

string name $=$ "platform-1";   
if (name $\equiv$ "platform-2") { print("Found platform-2"); } else if (name $\equiv$ "platform-1") { print("Found platform-1"); } else { print("Couldn't find platform 1 or 2"); }

```txt
Map<string, double> myMap = Map<string, double>();  
myMap["a"] = 1.1;  
myMap["b"] = 2.2; 
```

```txt
// If two loop variables are declared  
// (separated by a colon), the first must be  
// the key and the second must be the data.  
foreach (string aKey : double aData in myMap)  
{  
    print("key, data ", aKey, "", aData);  
} 
```

```txt
// If one loop variable is declared // it must be the data. 
```

```txt
foreach (double aData in myMap) { print("data", aData); if (aData > 2.0) break; } 
```

```txt
for (int i = 0; i < 10; i = i + 1) { if (i == 5) { continue; } } 
```

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQQD.

14

![](images/5e1e6f3cc96c9bf355f20d558a0c8aaf1b61f53e89b805befeae2a62cccac4c6.jpg)

# UNCLASSIFIED

# script块

![](images/d8ebffb042121b5d025bf73d70bd8efebcc7e5a476c31c1f33b7817c129274d0.jpg)

上下文很重要... 你在哪个位置放这些块很重要！

- Script 方法

```txt
script <type> <script-name> [(variable-declaration-list)]
<script-command...>
end_script
script bool IsScriptingFun()
return true;
end.script 
```

- Script 变量

script_variables double $\mathbf{x} = 1.0$ end.script_variables

- Execute 执行

```txt
execute at_time <time-reference> [ absolute | relative ]
...script commands ...
end_execute
execute at_interval_of <time-reference>
...script commands ...
end_execute 
```

- AFSIM的组件都实现了公共的脚本接口

- Simulation, platforms, processors, weapons

- 接口元素

- Script变量块   
- Script方法块  
- Script控制命令  
公共脚本块

execute   
on_initlize   
on_init2   
on_update   
on_message

- 预定义变量

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQQD.

UNCLASSIFIED

![](images/22c218b4eec600339809650970181b7b8765f3ce2967552e3d6da87c40e24a77.jpg)

# 预定义变量

![](images/0ea1ecfe854b663d5b7480c5db232392846474e6efca33c1b25af90bd20b83bf.jpg)

- WsfSimulation - 获取仿真级别的方法(查看帮助文档)  
- TIME NOW - 当前仿真时间  
- MATH - 访问数学库(查看帮助文档)

- 以下是在上下文中起作用的！

- PLATFORM - 当前平台  
- WEAPON - 当前武器(与PLATFORM类似)  
- PROCESSOR - 当前处理器  
- TRACK - 状态机中处理的当前跟踪  
-MESSAGE-on_message块处理的当前消息