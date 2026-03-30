# UNCLASSIFIED

23

![](images/56305b43c4bbc912f9f164bf4b0d543f54f679680cf6a123ea4c2e5d9d569d75.jpg)

# Platform Movement(平台运动)

![](images/07e2452cd2a56b341db9255090486dbc9eacfdaa4d873ad3c172a37f61273cf5.jpg)

选择在运动中的bomber(轰炸机)  
选择Turn to Heading   
给个180度  
Click‘Turn'

![](images/60c80151bd8b126e12438965db9ebc2cffba98727aa2e4b3164206a3385a7a47.jpg)

![](images/8abfe99e5ffea20d2753b229a9e756d6bf5c3d0e6556a5766742ecf39f5671b7.jpg)

DISTRIBUTioNC.Distributionauthorized to U.S.Government Agenciesand theircontractors,9-Aug-19. Otherrequestsforthisdocument shallbereferredtoAFRL/RQQD.

·在其中做的设置不会改变原本想定的任何东西.

![](images/dc9d593ac79af26bb994887547bc2619150d3be325256cb342ee10ca577be28a.jpg)

DISTRIBUTioNC.Distributionauthorized to U.S.Government Agenciesandtheircontractors,9-Aug-19. Otherrequestsforthisdocument shallbereferredtoAFRL/RQQD.

25

![](images/9db725a753252d4df63ac3d0a625e05879233fadb71086b405f9299566d9765f.jpg)

UNCLASSIFIED

# 返回到路线

![](images/c17f8107660f6fe4d8c5e9e5c188b4fbfe8af79a12209ba2aa21d4c154d40f2d.jpg)

·在Platform Movement,下选择‘Return to Route' -点击Go'

![](images/61537d05727461aa45b43ae767a4f716c23657585988935191aabd7202ce280a.jpg)

![](images/4235c952289ac1b5afd50fac9f35878a90aa524e31fb769dbb99820c2f5e91bc.jpg)

DISTRIBUTloNC.Distributionauthorized to U.S.Government Agenciesand their contractors,9-Aug-19. Otherrequestsforthisdocument shallbereferredtoAFRL/RQQD.

·尝试命令一个Tank到一个指定的海拔高度(AItitude)

－能行吗？  
－为什么？  
－因为它有个WSF_GROUND_MOVER

·对应的movers都有其运动上的限制(其自身合理的限制)

DISTRIBUTioNC.Distributionauthorized toU.S.Government Agenciesand theircontractors,9-Aug-19. Otherrequestsforthisdocument shallbereferredtoAFRL/RQQD.

![](images/1d0aa80ff5e3c3ac217976088167a4153aafececd9a5b6cf8fda0fb7d4887ca5.jpg)

# UNCLASSIFIED

# 学习目标

27

![](images/c81c68c8b3ff544f9637ef0163b2281534f0f5485806de2d7891cedd2d41c38e.jpg)

·包括

－学习AFSIM中不同的运动  
－在平台类型和平台实例中添加和编辑运动  
－给平台添加路线  
－在Warlock中对平台的运动进行导调

![](images/297a702398816fbb130c0b3e10b3bb14cab4569e855a82439fd676816f6bd738.jpg)

DISTRIBUTloNC.Distributionauthorized to U.S.Government Agenciesand their contractors,9-Aug-19. Otherrequestsforthisdocument shallbereferredtoAFRL/RQQD.

28

# 6.1.3. 武器 3_Weapons

本节给了一个给飞机上加装导弹的示例，通过学习这个示例可以掌握定义武器的基本方法。同时介绍了使用 warlock 做导调的方法，对导弹要打击的目标做实时的编辑，建立了从

定义导弹、定义目标、跟踪打击做了闭环。

# 6.1.3.1. 本节想定解析

本节想定源码在：afsim2.9_src\training\user\3_Weapons\scenarios\ solutions\5_Weapons_And_Execute\floridistan

# 想定沙盘图

![](images/afe6ae4a19ba3bc17a95845fe43b0d0bb841cb53822a971bc7874557f19114dd.jpg)

如上图所示，红方的轰炸机 bomber_1，向蓝方的 tank_1，tank_2 各投了一个制导导弹。

# 红方兵力

一艘航母 ship_1

□ 定义了一个循环的路线

一架轰炸机 bomber_1

□ 定义了一个路线，先到陆地，再回到海上  
□ 设置了固定跟踪 tank_1,tank_2，只有跟踪了才能投弹  
挂了 4 枚 GPS 制导炸弹，最大允许同时齐射 2 枚

炸弹开火时间为 510s 时开火  
打击 tank_1,tank_2 的炸弹同时开火，针对每个目标又齐射 2 枚，相当于四枚一次打完

■ GPS 制导炸弹

□ 本例中被挂在了 bomber_1 上  
▫ 弹的雷达特征 RCS 被设置为了常数 1 $\cdot$ ，换算为 dbsm则是 0

□

# 蓝方兵力

一个在天上的卫星 satellite_1

□ 定义了一个 700km 的轨道

两辆坦克 tank_1, tank_2

一个车辆

▫ 定义了一个向北行进的路线

# 6.1.3.2. 官方 PPT 资料

# 6.1.3.2.1. 武器与执行 5_AFSIM_User_Training_Weapons_Execute

本文为 afsim2.9_src\training\user\3_Weapons\slides\5_AFSIM_User_Training_Weapons_Execute.pptx 的翻译。

![](images/87f124df479d91c4d75186fcf64025b2c866c5ca79378a629511d60390c18e57.jpg)

UNCLASSIFIED

![](images/984e7db2f436c01c57d5bf2605b45da2a154241f1c33a7561be8bd144fb7a150.jpg)

![](images/86ac95056bf5ba57b012841bfc2e934bee87d85ead5d9075b7cf2f570c75a38b.jpg)

Integrity★Service★ Excellence

# AFSIM用户地道战5-武器与执行

13324598743

# AFRL/RQQD美国空军研究实验室

DISTRIBUTioNc.DistributionauthorizedtoU.S.GovernmentAgenciesand theircontractors,9-Aug-19. Otherrequestsforthisdocument shallbereferredtoAFRL/RQQD.

# ·包括：

－构建一个武器  
－将武器添加到平台  
－使用跟踪命令  
－使用执行命令

![](images/ba2c5766f6434c64f1a2f7a6336e09dfbb0c0ea578034151e040be4b1b415491.jpg)

DISTRIBUTioNc.Distributionauthorized toU.S.Government Agenciesand theircontractors,9-Aug-19. Otherrequestsforthisdocument shallbereferredtoAFRL/RQQD.

2

![](images/3b1ab2c6179722ff337f94f9dd18428456a54475f81282e1e8fe0923a0af700c.jpg)

# UNCLASSIFIED

# 武器类型

![](images/eb140f87d9c308c12941c39189256fd71d00effadfa9d01158398d1242043903.jpg)

·显式武器是有个物理的离开发射平台的过程  
·隐式武器不需要离开发射平台

－激光和对子战武器就属于隐式武器

# Predefined Weapon Types

·WSF EXPLICITWEAPON   
·WSF_IMPLICITWEAPON   
·WSF_LASER_WEAPON   
·WSFRFJAMMER

![](images/bb61807d31636e1b4d7d4c880094971d1a984be89a0e31acd51271b7d5f4fedf.jpg)

DISTRIBUTioNc.DistributionauthorizedtoU.S.GovernmentAgenciesand theircontractors,9-Aug-19. Otherrequestsforthisdocument shallbereferredtoAFRL/RQQD.

4

![](images/0eb801bc9e9049b21f0921334aad7dd046c4d22548f5bd03a1a5f42a272c6b56.jpg)

# UNCLASSIFIED示例：Step1-创建发射平台类型"platform_type”

![](images/cc463f2751627b6a5f36b103b34c4820b7db5153443f8ac33f80156753c2e86a.jpg)

·武器示例：发射平台  
·创建platform_type描述一个运动武器

脚本一般在单独的武器文件夹下

·包含一些必须的平台部分

特性和图标  
运动和弹出特性  
跟踪处理器用来管理跟踪  
引信处理器用来触发引爆

控制武器的装配、引爆、中止

![](images/43b3231c79cba0bca6ce1b57e4db999e768756358c5725d6baf8e0c3621f8c18.jpg)

![](images/25bf0fd252d64f6c825a0b068e446434241330381ea20ba0682581b4833acbce.jpg)

# ·武器示例：Weapon Effects

-定义武器使平台失效或中和的有效性  
－对目标的效果可以是概率性的、基于物理的，或两者的结合  
最终的武器属性（不是一个对象类）

可以重写！

-在weapon_effects/end_weapon_effects块中定义

独一无二的名称  
查看文档看看哪个武器效能应被选择  
定义杀伤半径.

# PredefinedWeapon EffectTypes

·WSF SPHERICALLETHALITY

![](images/f721c594e46fa724a4ea6cefdd3c2d4afbb647114476120c8416fae8741144b7.jpg)

DISTRIBUTioNC.Distributionauthorized to U.S.Government Agenciesand their contractors,9-Aug-19.

Otherrequestsforthisdocument shallbereferredtoAFRL/RQQD.

6

![](images/212447c537329ff5731c6ed2e4d7d7ac008d2700f41a9efba47d9bd8d306b604.jpg)

# UNCLASSIFIED

# 距离杀伤模型

![](images/5522d3c055d492921b29a1ff2557f9ac89039769c0edd224d110351b27313864.jpg)

![](images/79582724aa24a4ee0370b166d845694235fd272b2a4242133a69a3bd7f25d783.jpg)  
  
离minimum_radius的距离(m)

![](images/739aa81e03f4a314fa1816ee7a0ac980a2ad7c006700eb9a4c4c8b61a5232fbb.jpg)

DISTRIBUTioNC.Distributionauthorized to U.S.Government Agenciesand their contractors,9-Aug-19.

OtherrequestsforthisdocumentshallbereferredtoAFRL/RQQD.

![](images/62573c5e996b8f473a540b1d8fc1b4f9169fed0a4d14a7c6a44669aabdb4b146.jpg)

<table><tr><td>31</td><td>// The Weapon Effect component</td></tr><tr><td>32</td><td>weapon_effects ATA-MISSILE-EFFECTS WSF_SPHERICAL_LETHALITY</td></tr><tr><td>33</td><td>minimum_radius 1000 m</td></tr><tr><td>34</td><td>maximum_radius 1200 m</td></tr><tr><td>35</td><td>endweapon_effects</td></tr><tr><td>36</td><td></td></tr><tr><td>37</td><td></td></tr></table>

DISTRIBUTioNC.Distributionauthorized to U.S.Government Agenciesand their contractors,9-Aug-19. Otherrequestsforthisdocument shallbereferredtoAFRL/RQQD.

8

# UNCLASSIFIED

# 渐进式杀伤(离散的)

![](images/32bfee88a5edd2f4e0ab99fcbe6d7ec54015fcad371631c7355c89e322c0fc4d.jpg)

![](images/75a271a44e437a5872c232f501ea0c97b71ed0bbee3a72200beaf7a03143f84b.jpg)

DISTRIBUTioNC.Distributionauthorized to U.S.Government Agenciesand their contractors,9-Aug-19. Otherrequestsforthisdocument shallbereferredtoAFRL/RQQD.

![](images/eeea60d1a86bbadef603db7e6dc494a856874bceb274a53992d544756aa7c387.jpg)  
  
Graduated Lethality (interpolated)

![](images/426ca2d5088d9fd3738dd091a5e8cb21ec703355cdb50219caceb0799d3666eb.jpg)  
和目标的距离

![](images/64f5b6c2f41aa966630d547703d236182cc72d57cc3723c129cacaed0c7fce7e.jpg)  
DISTRIBUTioNC.Distributionauthorized to U.S.Government Agenciesand their contractors,9-Aug-19. Otherrequestsforthisdocument shallbereferredtoAFRL/RQQD.

10

# UNCLASSIFIED

![](images/c3aa6da6df55b2a88882805bfd27b30ead63f200fa7f9be9441a53c1b7634af0.jpg)

# 示例：Step3:创建"weapon"代码块

![](images/4b330bb3eee3e75ff164c5f04d6e622f81000aeb59723ef0c365122832f3539d.jpg)

·武器示例：显式武器

创建唯一的武器对象类

需要绑定在一个平台上做为平台的一部分  
多个武器可以绑定在一个平台上

weapon类是从其它类派生来的

如果发射的平台类型从发射平台上释放，则使用WSF_EXPLICIT_WEAPON  
WSFEXPLICITWEAPON

－一个武器对象包含

发射平台类型  
武器效能  
数量（可选）

![](images/3d53ab11f28e6334ad633360293bfe2ee03f1aae32f772cfcf47bcc590596178.jpg)

![](images/f4e1c3bab7212fd225b06e296da6c6d14c4701ffcc9bbc3597df8ea3c93216c4.jpg)

·武器示例：安装在平台上

－武器是平台的一部分

·Weapon代码块向平台添加武器  
·可以向platform_type或者platform对象来添加武器

：Quantity是一个属性，可以在实例化之后修改

![](images/c1d063d4091364b68a81ca3280bbcfd61c129a264986cf6c55277420509b8b7f.jpg)

```txt
include_once ata_missile.txt   
platform type jet_fighter WSF_PLATFORM icon F-15   
mover WSF_AIR_MOVER end mover   
weapon ata ATA-MISSILE-LAUNCHER end weapon   
weapon ata_more ATA-MISSILE-LAUNCHER quantity 10   
end platform type 
```

DISTRIBUTioNc.DistributionauthorizedtoU.S.GovernmentAgenciesand theircontractors,9-Aug-19. Otherrequestsforthisdocument shallbereferredtoAFRL/RQQD.

![](images/72a5eb0c7d0cdf21862479ea55d895a395832e72f33ceda411aef061ee1b0870.jpg)

# UNCLASSIFIED

# 示例：干扰武器

![](images/e7169c86c6d473de95c2bf2f4ec16e7f0089fc34f806c92523e498a808a1bbe1.jpg)

·武器示例：干扰器

weapon代码块定义了一个武器对象  
和显式武器类似

可以被添加到平台上做为平台的一部分  
可以被添加到platform_type和platform对象中

-没有“quantity"这个属性

![](images/7baf55200aff204dfe73032c678b327314775d7a367785479924e69678fb06b8.jpg)

```txt
2   
3 antenna_pattern SOJ_VHF_ANENNA   
4 constant 0 db   
5 end.antenna_pattern   
6   
7 weapon SOJ_VHF_JAMMER WSF_RF_JAMMER   
8 maximum_number_of_spots 2   
9 spot_power_distribution average   
10 slew_mode fixed   
11 maximum_range 200 km   
12 transmitter   
13 antenna_pattern SOJ_VHF_ANENNA   
14 frequency_band 30 mhz 300 mhz   
15 power 100.0 w   
16 internal_loss 0.0 db   
17   
18 endweapon   
19 
```

DISTRIBUTioNC.Distributionauthorized to U.S.Government Agenciesand their contractors,9-Aug-19.

Otherrequestsforthisdocument shallbereferredtoAFRL/RQQD.

·包含一个新的武器文件:

－在"bomber.txt"的最顶部加上  
"include_once weapons/agm/red_gps_bomb_1.txt"   
-在我们的模型库中定义了red_gps_bomb_1.txt

# platforms/bomber.txt

![](images/31c4eef0c47b81c12deeabcf992029c8157b5df785863c9db1f70d800709e62f.jpg)

![](images/1107d394114047bea31dd08ad67b246d02bc004ac1c9250f64f563ccb89a9fa0.jpg)

DISTRIBUTioNC.Distributionauthorized to U.S.Government Agenciesand their contractors,9-Aug-19. Otherrequestsforthisdocument shallbereferredtoAFRL/RQQD.

![](images/51200869013d2149b6f010582e342d32896a5c23d0b51b9b9225ceb12f78230c.jpg)

# UNCLASSIFIED

# 文件路径

![](images/7ee4fe6ca26a3151d8249ac5826ff5efc612bc9add0c9cd05fa70de808b688b2.jpg)

在floridistan.txt中添加一个文件路径  
可以让Wizard找到我们包含的相对路径的文件

# floridistan.txt

![](images/3dbe77cc8aa67ba003a269e49a77562153290911c228424999333a611d8c11a3.jpg)

DISTRIBUTioNC.Distributionauthorized to U.S.Government Agenciesand their contractors,9-Aug-19.

OtherrequestsforthisdocumentshallbereferredtoAFRL/RQQD.

·雷达特性  
·空气动力学特性

![](images/f0d54ef293a00ff5239cec492e299cf6b6b3994ef3c275f6fb6802cdb8d0b8ad.jpg)

weapons/agm/red_gps_bomb_1.txt   
```txt
13 radar_signature RED_GPS_BOMB_1_RADAR_SIGNATURE constant 1 m^2   
16 end_radar_signature   
17   
18 aero RED_GPS_BOMB_1_AERO WSF_AERO   
19 //Note: Values for Mk-82-like slick bomb.   
20 cd_zero_subsonic 0.100   
21 cd_zero_supersonic 0.40   
22 mach_begin_cd_rise 0.800   
23 mach_end_cd_rise 1.200   
24 mach_max_supersonic 2.000   
25 reference_area 0.059 m2   
26 cl_max 10.400   
27 aspect_ratio 4.000   
28 end_aero 
```

DISTRIBUTioNc.DistributionauthorizedtoU.S.GovernmentAgenciesand theircontractors,9-Aug-19. Otherrequestsforthisdocument shallbereferredtoAFRL/RQQD.

16

![](images/77b6393b17bcc097afcc830e10bc8ba1062befa7ac5490fbf5fb8b870ac3e256.jpg)

# UNCLASSIFIED

# 数据单位举例

![](images/218cfd2184aafac1106d9909c933a123f34c41cf7d0cd3975f0d43a75bad167c.jpg)

# 在帮助文档中搜“Argument Types”

mass-value<real><mass-units> mass-units

<table><tr><td>Unit of Measure</td><td>Allowable Input Values</td></tr><tr><td>kilograms</td><td>kilograms kg kilo kilogram</td></tr><tr><td>grams</td><td>grams gram g</td></tr><tr><td>pounds</td><td>pounds pound lbs lbm lb</td></tr><tr><td>kilopounds</td><td>klb</td></tr><tr><td>tons</td><td>tons ton</td></tr><tr><td>tonnes</td><td>tonnes tonne</td></tr><tr><td>slugs</td><td>slugs slug</td></tr></table>

length-value<real><length-units> length-units

<table><tr><td>Unit of Measure</td><td>Allowable Input Values</td></tr><tr><td>meters</td><td>meters meter m</td></tr><tr><td>kilometers</td><td>kilometers km</td></tr><tr><td>megameters</td><td>megameters megameter</td></tr><tr><td>feet</td><td>feet ft</td></tr><tr><td>kilofeet</td><td>kfeet kft</td></tr><tr><td>miles</td><td>miles mile mi</td></tr><tr><td>nautical miles</td><td>nm nmi</td></tr><tr><td>centimeters</td><td>centimeters centimeter cm</td></tr><tr><td>millimeters</td><td>millimeters millimeter mm</td></tr><tr><td>micrometers</td><td>micrometers micrometer um microns micron</td></tr><tr><td>nanometers</td><td>nanometers nanometer</td></tr><tr><td>angstroms</td><td>angstroms angstrom</td></tr><tr><td>inches</td><td>inches inch in</td></tr><tr><td>astronomical unit</td><td>au ua</td></tr></table>

DISTRIBUTioNC.Distributionauthorized to U.S.Government Agenciesand their contractors,9-Aug-19. Otherrequestsforthisdocument shallbereferredtoAFRL/RQQD.

# 制导MOVER需要一个制导计算处理器

weapons/agm/red_gps_bomb_1.txt   
```txt
33 platform_type RED_GPS_BOMB_1 WSF_PLATFORM   
35 icon jdam   
36 radar_signature RED_GPS_BOMB_1_RARAD_SIGNATURE   
37 mover WSF GUIDED_MOVER   
39 aero RED_GPS_BOMB_1_AERO   
40 mass 500 lbs   
41 update_interval 0.5 s   
42 end_mover   
43   
44 processor guidance_computer WSF GUIDANCECOMPUTER   
45 proportionaljahation_gain 10.0   
46 velocity_pursuit_gain 10.0   
47 g.bias 1.0   
48 maximum commanded_g 25.0 g   
49 guidance_delay 0.0 sec   
50 end Processor   
51   
52 processor fuse WSFGROUND_TARGET Fuse   
53 maximum_time_of_flight 900 seconds   
54 end Processor   
55 endplatform_type 
```

![](images/50fb95f0b9a5d706cc663ed18d0f8d6137199e7cc865a94cb6f5f89b82be1349.jpg)

DISTRIBUTioNC.Distributionauthorized to U.S.Government Agenciesand their contractors,9-Aug-19. Otherrequestsforthisdocument shallbereferredtoAFRL/RQQD.

18

![](images/18a176b624d539f254ccbaa166e15ca551f550955dd04cc894e78b81a9357292.jpg)

# RED_GPS_BOMB_1武器效能

![](images/c0f1291968868c846fb654ee2de2404156a2aa19c827efdf1178388de28e2a28.jpg)

# ·使用距离杀伤模型WSF_SPHERICAL_LETHALITY－其方程在文档中有提供

UNCLASSIFIED   
weapons/agm/red_gps_bomb_1.txt   
60 weapon_effects RED_GPS_BOMB_1_EFFECTS WSF_SPHERICAL_LETHALITY   
62 allow_incidental DAMAGE   
63 minimum_radius 25.0 m // largest blast radius at which damage inflicted is maximum.   
64 maximum_radius 30.0 m // blast radius beyond which the damage inflicted is Zero.   
65 minimum_radius 0.1 // damage level achieved at the minimum radius.   
66 maximum_radius 1.0 // maximum damage level achievable upon the target.   
67 threshold_radius 0.2 // initial damage level which must be achieved   
68 // before effects begin to accumulate upon the target   
69 exponent 1.0 // exponent of proportionality of damage with radius.   
70 // ( $\mathrm{e} = 1.0\equiv \equiv$ linear damage within blast region,   
71 // e > 1.0 => more damaging within the blast region,   
72 // 0.0 < e < 1.0 => less damaging within blast region.)   
73 endweapon_effects   
74

![](images/a832193132e4094d0d6b433f971582a7df1492b8cb2daed8b69acb6bca0678fa.jpg)

DISTRIBUTioNC.Distributionauthorized to U.S.Government Agenciesand their contractors,9-Aug-19. Otherrequestsforthisdocument shallbereferredtoAFRL/RQQD.

·也可以在这里定义数量"Quantity”

weapons/agm/red_gps_bomb_1.txt

```txt
82
83.1 weapon RED_GPS_BOMB_1 WSF_EXPLICIT_WEapon
84 launchedplatform_type RED_GPS_BOMB_1
85 weapon_effects RED_GPS_BOMB_1_EFFECTS
86 aux_data
87 double lar_meters = 18520
88 end_aux_data
89 endweapon
90 
```

![](images/74311940f4c6f91b92782fd878ffce8f6d338637320bde81d427be0763185a97.jpg)

DISTRIBUTioNc.DistributionauthorizedtoU.S.GovernmentAgenciesand theircontractors,9-Aug-19. Otherrequestsforthisdocument shallbereferredtoAFRL/RQQD.

20

![](images/eb9bf7e07a09ab8c883b9d84ff35edae92aca1bdbe8a5e21ef13e9426240d5f4.jpg)

# UNCLASSIFIED

# 整合到发射平台

![](images/e74167c01a7213b42a0c208574629b90bb17308243272aa6b4442a24048c6e2c.jpg)

# platforms/bomber.txt

·添加weapon到BOMBER平台模版中  
·可以运行！可以切回使用‘Mission运行，假如设置的还是使用Warlock'的话  
·我们需要跟踪！

```txt
platform/bomber.txt
1 # File generated by Wizard 2.7.0 on Sep 20, 2020.
2 include_ once weapons/ agm/red_gps_bomb_1.txt
3 platform_type BOMBER WSF PLATFORM
4 icon bomber
5 mover WSF_AIR_MOVER
6 end_mover
7 mover WSF_AIR_MOVER
8 weapon red_gps_bomb_1 RED_GPS_BOMB_1
9 quantity 4
10 end_mover
11 endPlatform_type
12 endPlatform_type 
```

![](images/ac12889ea99d8fda60e77aa53d2a119756024da6d80ca9b40cdb974880bac5c8.jpg)

DISTRIBUTioNC.Distributionauthorized to U.S.Government Agenciesand their contractors,9-Aug-19. OtherrequestsforthisdocumentshallbereferredtoAFRL/RQQD.

# track

track...end track

```txt
track   
position ...   
altitude ...   
range ...   
bearing ...   
elevation ...   
speed ...   
heading ...   
type ...   
side ...   
spatial_domain ...   
frequency ...   
platform ...   
aux_data...end_ux_c   
endtrack 
```

# Overview

trackblocksmaybespecifiedinagivenplatformCommandsshouldbespecifiedforonlythoseatributesthatare

NoteEitheosgeonsteseiediutualyieiean

# Commands

position<latitude-value><longitude-value>

altitude<length-value>[aglmsl]

forthealtitudespecification.If thereference specification isomitted thenmsl isassumed.

DISTRIBUTioNC.Distributionauthorized to U.S.Government Agenciesand their contractors,9-Aug-19.

Otherrequestsforthisdocument shallbereferredtoAFRL/RQQD.

# UNCLASSIFIED

# 在平台中初始化跟踪

22

·在"red_laydown.txt"中给bomber_1添加跟踪

scenarios/red_laydown.txt

```txt
18   
191 platformbomber_1BOMBER   
20   
21 track platform tank_1 end_track   
22 track platform tank_2 end_track   
23 side red   
25 heading 270 degrees   
26 route   
28 position 30:09:55.440n 80:20:43.800w altitude 30000.00 ft   
29 speed 500 mph   
30 position 30:08:41.000n 81:34:36.000w   
31 position 30:12:50.000n 81:40:31.000w   
32 position 30:18:50n 81:40:25w   
33 position 30:24:51.751n 81:20:41.535w   
34 position 30:26:37.139n 80:18:19.578w   
35 end-route   
36   
37 endplatform 
```

DISTRIBUTioNC.Distributionauthorized to U.S.Government Agenciesand their contractors,9-Aug-19.

Otherrequestsforthisdocument shallbereferredtoAFRL/RQQD.

# execute

# execute...end execute

```txt
execute at_time <time-reference> [absolute | relative]  
...script commands...  
end_execute  
execute at_interval_of <time-reference>  
...script commands...  
end_execute 
```

# Overview

# Example

```txt
platform radar-site-1.Radar_SITE sensor radar...endSensor execute at time 10 minutes absolute PLATFORM.TurnSensorOn("radar"); end_execute execute at time 20 minutes absolute PLATFORM.TurnSensorOff("radar"); end_execute endplatform 
```

DISTRIBUTioNc.Distributionauthorized toU.S.Government Agenciesand theircontractors,9-Aug-19. Otherrequestsforthisdocument shallbereferredtoAFRL/RQQD.

# UNCLASSIFIED

![](images/adf0cb40aa8498e8bb6d419f5a08bafb1a6a476bda220802ebb0ae0823eca792.jpg)

# 在BOMBER中的Execute Block代码块

![](images/1f8dab849cb5efd97acbb00429a067d18920a7e1d36ba4aeffaa1acea9cea2c4.jpg)

·在平台类型中添加执行代码块   
·确保使用Mission在执行  
·运行！!！  
·我们开火了吗？  
·哪里出问题了呢？

# platforms/bomber.txt

```matlab
10 weapon red_gps_bomb_1 RED_GPS_BOMB_1 quantity 4 endweapon execute at_time 510 sec absolute Weapon("red_gps_bomb_1").FireSalvo(MasterTrackList().TrackEntry(0),2); Weapon("red_gps_bomb_1").FireSalvo(MasterTrackList().TrackEntry(1),2); end_execute   
endplatform_type 
```

DISTRIBUTioNc.Distributionauthorized to U.S.Government Agenciesand their contractors,9-Aug-19.

Otherrequestsforthisdocument shallbereferredtoAFRL/RQQD.

MaximumRequestCount（最大齐射武器数量）默认值是 1.   
也许你需要调整武器的发射时间，坦克的位置和弹的路径以来让武器命中目标

![](images/befa7543c984516350b0ce8501d6fa2a4a34fa6a10f7cf47804dae61fa787b4b.jpg)  
DISTRIBUTioNc.DistributionauthorizedtoU.S.GovernmentAgenciesand theircontractors,9-Aug-19. Otherrequestsforthisdocument shallbereferredtoAFRL/RQQD.

26

![](images/23dfc9945ca8f57691513fc2091c7f9be0806f65fbbf0cc8c03c72b55f38afaf.jpg)

# UNCLASSIFIEDMaximum Request Count武器齐射数量

![](images/7eb2ef86a9fec9a1cd4054b532ace7628dcd412e676770c81903f1a488420a94.jpg)

将武器最大齐射数量改为2  
运行！!！

```txt
4   
5 platform_type BOMBER WSFPLATFORM   
6 icon bomber   
7   
8 mover WSF_AIR_MOVER   
9 end_mover   
10   
11 weapon.red_gps_bomb_1 RED_GPS_BOMB_1   
12 maximum_request_count 2   
13 quantity 4   
14 endweapon   
15   
16 execute at_time 510 sec absolute   
17 Weapon("red_gps_bomb_1").FireSalvo(MasterTrackList().TrackEntry(0), 2);   
18 Weapon("red_gps_bomb_1").FireSalvo(MasterTrackList().TrackEntry(1), 2);   
19 end_execute   
20   
21 endPlatform_type   
22 
```

DISTRIBUTioNC.Distributionauthorized to U.S.Government Agenciesand their contractors,9-Aug-19. Otherrequestsforthisdocument shallbereferredtoAFRL/RQQD.

![](images/978ea92ad2dd177b130a2417f7aa4423e08ca84bf065bfcd4b0c044b465dae98.jpg)

DISTRIBUTioNc.DistributionauthorizedtoU.S.GovernmentAgenciesand theircontractors,9-Aug-19. Otherrequestsforthisdocument shallbereferredtoAFRL/RQQD.

# UNCLASSIFIED

![](images/25d986e875fb93e3d32435a897023482debb2bc3fe5be40a0859e489a95e903d.jpg)

# Warlock

28

![](images/126e8824e4616493b723745c669d11ccd73b6a36f3732a612e52a79c9e8a6a1f.jpg)

·切换到Warlock执行!!!   
·如果我们什么也不做，同样会在某时刻发射导弹进行打击

![](images/0211510eb4dd726b9c8cb82e991d05cc582be7d9b5987ca93b5c696625588b58.jpg)

DISTRIBUTioNC.Distributionauthorized to U.S.Government Agenciesand their contractors,9-Aug-19. Otherrequestsforthisdocument shallbereferredtoAFRL/RQQD.

－打开武器浏览器View→WeaponBrowser

·选择bomber_1

会弹出可用的武器列表

![](images/f6c842b0eacc58538c9257a0504642b2f38a8639e70f8d1e4b8011d1a955fff3.jpg)

![](images/5f4f5b757160c40767d45692d35d30cc960af5b1136dbaf24f1aca8835fa3f5f.jpg)

DISTRIBUTioNc.DistributionauthorizedtoU.S.GovernmentAgenciesand theircontractors,9-Aug-19. Otherrequestsforthisdocument shallbereferredtoAFRL/RQQD.

# UNCLASSIFIED

# 武器浏览器

30

![](images/3656f96267e0a1a84cbfa4c638b268ee486e3ad30146afd2706de4712d95150b.jpg)

![](images/e2ec585e54f93077fa85ab60d628adbb244f4607bc57e6804dfdabbdf9a6158f.jpg)

·选择'New Target’   
·选择Track

－点击十字图标  
-点击tank_2   
-可以看到‘2'在track编辑框内

![](images/10d02d3aa8e41549a1b16742005b33616faa30872f10a042c6a6142214f7a1d7.jpg)

![](images/90414d2c67b3e3545fb310c4cf3f6df490bc23207544329fafc4ec66d0edf6ac.jpg)

![](images/65891ec9164c6173f85392211e2f94392d55ac515e5cc1ba70fe2b80ed7ae8a1.jpg)

DISTRIBUTioNC.Distributionauthorized to U.S.Government Agenciesand their contractors,9-Aug-19. Otherrequestsforthisdocument shallbereferredtoAFRL/RQQD.

·武器数量给4   
·FIRE!!!   
·平台浏览器中会增加4个武器  
·武器浏览器中没有武器剩余了

![](images/893b97753b8a89d537db6978f2f8b083ee8c814b2b15f185fe9d0e53c1d884c0.jpg)

![](images/4e7c36964edeed56e6620a3b470738cdd390da82d6d6a2ab4e14bf505258ebe1.jpg)

![](images/2bb80e378122200073afc8417094c958a294b149b936b6a951784b5752eccc23.jpg)

DISTRIBUTioNc.DistributionauthorizedtoU.S.GovernmentAgenciesand theircontractors,9-Aug-19. Otherrequestsforthisdocument shallbereferredtoAFRL/RQQD.

32

![](images/98449dfbbb978cff4bd7a706bbbb1071739378dcdfd2a0b93a985574e0e94432.jpg)

# UNCLASSIFIED

# 武器开火？

![](images/0f2b88666c877f1cfae698ce0c0b39a64216cdf2535591c9f1c407518fe23f07.jpg)

·重新启动Warlock试图向car开火.

－可以完成吗？  
－为什么不行呢？  
-缺少Track

·包括：

-构建一个武器  
-将武器添加到平台  
－使用跟踪命令  
－使用执行命令

![](images/5ccfabab885659380403fb171b256d4cd35dbc4bf44912a195a7688035545aad.jpg)

DISTRIBUTloNC.Distributionauthorized to U.S.Goverment Agenciesandtheircontractors,9-Aug-19. Otherrequestsforthisdocument shallbereferredtoAFRL/RQQD.

# 6.1.4. 传感器 4_Sensors

# 6.1.4.1. 本节想定解析

本节想定为：

afsim2.9_src\training\user\4_Sensors\scenarios\solutions\7_Sensors_And_Tracks\floridista n\floridistan.txt

![](images/3c4ae16782e7bec1bbcbefa8600fea80632c6286532c921137bb035474725eac.jpg)

# 红方兵力

一艘航母 ship_1

□ 定义了一个循环的路线

一架轰炸机 bomber_1

□ 定义了一个路线，先到陆地，再回到海上  
□ 设置了固定跟踪 tank_1, tank_2，只有跟踪了才能投弹  
□ 挂了 4 枚 GPS 制导炸弹，最大允许同时齐射 2 枚

炸弹开火时间为 510s 时开火  
打击 tank_1,tank_2 的炸弹同时开火，针对每个目标又齐射 2 枚，相当于四枚一次打完

GPS 制导炸弹

□ 本例中被挂在了 bomber_1 上  
□ 弹的雷达特征 RCS 被设置为了常数 1 $m ^ { 2 }$ ，换算为 dbsm 则是 0

# 蓝方兵力

一个在天上的卫星 satellite_1

□ 定义了一个 700km 的轨道

两辆坦克 tank_1, tank_2

一个车辆

□ 定义了一个向北行进的路线

■ 一个地空导弹阵地 sam_1

▫ 下挂 16 枚地空导弹（但未设置发射条件）  
□ 下挂 2 部雷达，一部 150 海里（acq，开启），一部是 100 海里（ttr，默认关），在想定开始后，acq 雷达陆续会探测到红方的战斗机以及其发射的 4 枚 GPS 制导炸弹  
□ 其它定义包括通信、区域等在推演时均未有动作

# 6.1.4.2. 官方 PPT 资料

# 6.1.4.2.1. 雷达传感器 Radar_Sensors

本文为 afsim2.9_src\training\user\4_Sensors\slides\Radar_Sensors.pptx 的翻译。

![](images/021cc31dd37a9b9a67aa5d92ffae955b6d2e702c6ee45c679a1758f4e3fef03a.jpg)

# AFSIM地基雷达传感器

13324598743

Integrity $\star$ Service★ Excellence

# AFRL/RQQD美国空军研究实验室

DISTRIBUTioNC.Distributionauthorized to U.S.Government Agenciesand their contractors,9-Aug-19. Otherreguestsforthisdocument shall bereferred to AFRL/RQQD

1

![](images/b4b84eac610622fe28f122990e394ea69e0b96beb876b302d8fd38ef723f4bbd.jpg)

UNCLASSIFIED

# 学习目标

![](images/49309aa537103763465055a46c1f512a651ac0fb921b2a6cd96e80e2fb7e622f.jpg)

·内容

－了解不同的雷达类型  
-了解雷达在AFSIM当中的表达  
－对雷达建模需要的数据  
－天线模式&波束

![](images/b944cfd9722aa654907fb5515ef47e79fab679f17f9d2381796146e5150e0de7.jpg)

DISTRIBUTIoNC.Distributionauthorizedto U.S.GovernmentAgenciesand their contractors,9-Aug-19. Otherrequestsforthisdocument shall bereferredto AFRL/RQQD.

![](images/117127b60b60f07dd6b099547bf93a63f97bdceac747ba3f15c03e2d5c137a44.jpg)

![](images/3458f5bed4adf2f5ed537a9f0386948e6e5edd8831d2d1171fe008ddbe7579c2.jpg)

![](images/85e3596eb07d2e011b79124eb51ace9b4d5288fac148a531d93161f407a5b791.jpg)

![](images/40f723c68e95cf8fe5e3b1486e6994cda99cc89f7daef1556c5808e5c8e2f8ed.jpg)

![](images/d4b50a777cbec6128e0194881338ae1656432f3ecaa7084d1752708228f0848a.jpg)

![](images/8219b7953c3b951e6f3187459c6bfef3a52f64de621a414a0d8715f1fe7e4aff.jpg)

DISTRIBUTIoNC.Distribution authorized toU.S.Government Agenciesand their contractors,9-Aug-19. Otherreguestsforthisdocumentshall bereferred to AFRL/RQQD

3

![](images/824b10c048da695a331e3ddce9233fb99e50acc10c5e8c19b2bc098d69750f79.jpg)

# UNCLASSIFIED

# 早期预警雷达

![](images/11b57823a91ed1f2e27dc7f1963f5f4ab1ac3a11a7af8494a62bf1cd80e7330b.jpg)

·早期预警雷达是指任何主要用于远程探测目标的雷达系统。这种雷达系统的目的是在入侵者到达目标之前尽早发出警报，从而为防空系统提供最大限度的反应时间，以便进行防御操作。  
·通常，早期预警雷达在方位角上以360°旋转，而在仰角和高度上是固定的。  
·通常发射宽波束以实现最大的方位角和仰角覆盖。

![](images/1822cb3380b7f092ea09326598044448097c4de9a3c87e7966fc29e404552c88.jpg)

DISTRIBUTIoNC.Distributionauthorizedto U.S.GovernmentAgenciesand their contractors,9-Aug-19. Otherrequestsforthisdocument shall bereferredto AFRL/RQQD.

·高度测量雷达是一种用于测量目标高度的二维雷达。  
·它发射的波束在方位角上非常窄，但在仰角上非常宽。  
·需要来自其他系统的方位角提示。  
·新的地对空导弹系统使用三维早期预警或目标获取雷达，使得高度测量雷达逐渐被淘汰。

![](images/708f534cedebe124f4faa292c3aaf09ea2cd5f2967200f51015efc4dcf5ea432.jpg)

DISTRIBUTioNC.Distributionauthorized to U.S.Government Agenciesand their contractors,9-Aug-19. Otherrequestsforthisdocument shallbereferredto AFRL/RQQD.

5

![](images/b1d71c2bb11e423d71770e0cb0d8537a9292d60d6c39925c0790e0dfc322afa0.jpg)

# UNCLASSIFIED

# 目标识别雷达(TAR)

![](images/a38f9458721afd77da673c47fb8d386b66725f36a287b9be7b40f0ce678cb82a.jpg)

·较新的SAM系统采用目标捕获雷达，而非高度探测器。  
·通常，预警雷达将提供二维解决方案，而TAR用于在火控雷达启动之前确定三维解决方案。

![](images/2398a31adfeb2081dc5b1cf3d4328ce322ec334eaa959dd6e7f74cbf1ddd45a2.jpg)

DISTRIBUTloNC.Distributionauthorized to U.S.Government Agenciesand their contractors,9-Aug-19. Otherrequests forthisdocument shallbereferred to AFRL/RQQD.

·火控雷达（FCR)是一种专门设计用于向火控系统提供信息（主要是目标方位角、仰角、距离和射程率）以引导武器击中目标的雷达。它们有时被称为瞄准雷达，或在英国被称为炮瞄雷达。如果雷达用于引导导弹，则通常被称为照明器或照明器雷达。  
·通常具有多种模式（例如搜索、捕获、跟踪）  
·通常发射狭窄而强大的光束。

![](images/c8a682c6ad6b2eb81b045a2266847a0601d163c9c5e4d56cdd8b5dedb298abbf.jpg)

DISTRIBUTioNC.Distributionauthorized to U.S.Government Agenciesand their contractors,9-Aug-19. Otherreguestsforthisdocumentshall bereferred to AFRL/RQQD

![](images/64d040c323ade6c53612a43d4ccdb00e9e5b1464ca27b80ab714120c3a015fce.jpg)

# UNCLASSIFIED

# 海军雷达

![](images/d319354795d0b0b458d96d21defd14c076c9b43d11d0b7a3c57c7279dc4c20d2.jpg)

·海军舰艇通常配备多种类型的雷达，可提供不同的功能。  
·水面搜索：用于探测其他水面舰艇、导航设备等。通常具有方位角宽、仰角窄的波束。通常安装在高处以尽量减少海面杂波的影响  
·空中搜索：功能与地面预警雷达非常相似。  
·多功能：通常是船上有多个阵列的AESA雷达。提供预警、目标捕获和目标交战能力。

![](images/45a5de7dc29b670cd82c565554d1132f165cd84d6bd8e9cbbeaaee1d7f821f28.jpg)

DISTRIBUTloNC.Distributionauthorized toU.S.Government Agenciesand their contractors,9-Aug-19. Otherrequests forthisdocument shallbereferred to AFRL/RQQD.

![](images/043a12a05c1fe72ccc58eac02272e963887d6dc20e275a8c1e1733e5a3a5a663.jpg)  
DISTRIBUTioNC.Distributionauthorized to U.S.Government Agenciesand theircontractors,9-Aug-19. Otherrequestsfor thisdocument shallbe referred to AFRL/RQQD.

9

![](images/ff6757c3c268783fbaaa8491cc7ac0b99e38d33966c8e7504616e8cf5e7ea7ec.jpg)

# UNCLASSIFIED

# 弹道导弹早期预警雷达

![](images/b82116b2bc0e023d19ddffb7c5185ad52f2025c2345003607182e06d43f78b71.jpg)

·一种专门的早期预警雷达变体。  
·其目的是检测来袭的弹道导弹。  
·设计用于极远距离的检测能力（因此具有大阵列和高峰值功率）。

![](images/db41853d3398a8f1ac19675f820373ee15702f4c079e02b5a30dcb07bf5497b6.jpg)  
DISTRIBUTIoNC.Distribution authorized toU.S.Government Agenciesand their contractors,9-Aug-19. Otherrequestsforthisdocument shall bereferredto AFRL/RQQD.

·一种雷达系统，能够探测非常远距离的目标，通常距离数百至数千公里，超出雷达视距，这是普通雷达的距离极限。  
·两种信号传播模式：

一天波：信号从电离层反射  
一表面/地面波：信号从海面反射。

·非常大的阵列

![](images/92e4125b7d4eb5d3d2ff7533bedc4d416daa7825fdf0736c4623c664efb244b5.jpg)

![](images/f5d361f08b4d0b33dd18704507eb50d582ec6a82049e65a49ccf52c28848752f.jpg)

DISTRIBUTioNC.Distributionauthorized to U.S.Government Agenciesand their contractors,9-Aug-19. Otherreguestsforthisdocument shall be referred to AFRL/RQQD

11

![](images/9f3a654b2df892d4c893b2679d19280b14c09e76a7b0f37e85801f895d7f84e9.jpg)

# UNCLASSIFIED

# 雷达频段

![](images/6fddf4faacf735b2d9a130e76ac122dae2365c11c7772dde622da7d3e4fed199.jpg)

·HF波段(3-30MHz)：超视距雷达，结合了超长距离和低空间分辨率及精度。  
·VHF和UHF波段(30-1000MHz)：长距离、视距监视 $( 2 0 0 - 5 0 0 k m$ )，分辨率和精度为低至中等。  
·L波段(1-2GHz):远程监视，分辨率为中等。  
·S波段(2-4GHz)：近距离监视 $( 1 0 0 - 2 0 0 k m$ )，远程跟踪 $( 5 0 - 1 5 0 k m$ )，精度为中等，但易受天气影响。  
·C波段(4-8GHz)：近距离监视、远程跟踪和制导，精度高，但易受天气影响。  
·X波段(8-12GHz)：近距离监视、远程跟踪和制导，精度高。下雨时，距离缩短至近距离 $( 2 5 - 5 0 k m$ ）。  
·Ku波段和Ka波段（12-40GHz）：短距离跟踪和制导（10-25公里），用于天线尺寸非常有限且不需要全天候操作的情况。更广泛地用于高于天气高度的机载系统。

DISTRIBUTIoNC.Distribution authorized toU.S.Government Agenciesand their contractors,9-Aug-19. Otherrequestsforthisdocument shall bereferredto AFRL/RQQD.

![](images/f1aed68cab650b85ebc6c0edb20754273168a911363c1e10c47711adc0c94ec0.jpg)

Integrity $\star$ Service★ Excellence

切换至AFSIM...

DISTRIBUTioNC.Distributionauthorized to U.S.Government Agenciesand their contractors,9-Aug-19. Otherreguestsforthisdocumentshall bereferred to AFRL/RQQD

13

![](images/3b989d3c2b5b4a067c628cfa5e82bf7d637a6bc9e8af880a578a267d3b0f8af6.jpg)

在AFSIM中雷达传感器WSF_RADAR_SENSOR

![](images/3a63539fdf408dccdc1f2a277bafab9beb21aa78b5eb5a504c7b23d27d2be9d4.jpg)

SenSOrWSF RADAR SENSOR

·提供基础雷达实现。它能够代表各种各样的雷达系统，包括简单的单模式预警雷达，以及用于目标探测的复杂多模式雷达。

![](images/0bfdd94d2e54997991914c7963664955d849afa73cf9d14aead82a3bf2979f83.jpg)

DISTRIBUTIoNC.Distributionauthorizedto U.S.GovernmentAgenciesand their contractors,9-Aug-19. Otherrequestsforthisdocument shall bereferredto AFRL/RQQD.

1)天线模式

必须

2)发射机(频率、功率)

可选

3b)接收机(带宽，噪声指数)

可选

3a)探测能力(最远距离，1平方米物体的探测距离)

DISTRIBUTioNC.Distributionauthorized to U.S.Government Agenciesand their contractors,9-Aug-19. Otherreguestsforthisdocument shall bereferred to AFRL/RQQD

15

![](images/45b92f6096cbac9ea9cae28aa9f1c5a139f04f16b81416b01d738fe973a5d126.jpg)

# UNCLASSIFIED

# 雷达方程

![](images/2a21a853ff92173b1b874cf46b22541c371d2e42b31cca32c1f447bba1ceaa4c.jpg)

<table><tr><td colspan="5">Table 1. Typical Minimum SN Required</td></tr><tr><td>Skilled Operator</td><td>Auto-Detection</td><td>Auto-detection with Amplitude, TOA, and Frequency Measurements</td><td>AGA Phase Interferometer</td><td>AGA Amplitude Comparison</td></tr><tr><td>3 to 8 dB</td><td>10 to 14 dB</td><td>14 to 18 dB</td><td>14 to 18 dB</td><td>16 to 24 dB</td></tr></table>

$$
R _ {\max } = \sqrt [ 4 ]{\frac {P _ {t} G ^ {2} \lambda^ {2} \sigma}{(4 \pi) ^ {3} P _ {\min }}} = \sqrt [ 4 ]{\frac {P _ {t} G ^ {2} c ^ {2} \sigma}{f _ {o} ^ {2} (4 \pi) ^ {3} \left| P _ {\min } \right.}}
$$

Pt $\equiv$ Transmit power(power dimensions)

Pmin=minimum detectable signal（power）

$\equiv$ transmitwavelength(length)）

0=Target radar cross section(area)

Pmin=k TBF(S/N)min

f。=Frequency （Hz)

G=Antenna Gain （ratio）

C=speed of light

k=波尔兹曼常数（1.38×10-23w·sec/Kelvin）

T=温度（开尔文）（典型的290°）

B=接收带宽（Hz）

F=噪声指数（dB）

S/N $\mathrm { \Delta } _ { \mathrm { M I N } } =$ 信噪比（minimum）

DISTRIBUTIoNC.Distributionauthorizedto U.S.GovernmentAgenciesand their contractors,9-Aug-19. Otherrequestsforthisdocument shall bereferredto AFRL/RQQD.

![](images/4223f46f91263f1051ddc2685bfd1bb55d40cf36ec033a91d7615da9e36e5f7b.jpg)  
DISTRIBUTioNC.Distributionauthorized to U.S.Government Agenciesand their contractors,9-Aug-19.   
Otherrequestsforthisdocument shallbereferredto AFRL/RQQD

17

![](images/a0142083e1e795c8ace3f0d4e1510426cde57067f13f305756ef7ff80501dc82.jpg)

# UNCLASSIFIED

# 发射修正因子

![](images/4516e0f937a383467bbf62dd6f7b84cc88b955040fc006de3d23b594e53c5181.jpg)

·脉冲宽度PW(距离因子)

![](images/f6897378ff3e54032b1fb814e1b87ffef1294dfc3c4918a649cd008e82875e13.jpg)

·脉冲重复间隔PRI/脉冲重复频率PRF(距离模糊)

-PRI $=$ 1/PRF

·(-)损耗   
－线路损耗，天线损耗  
·(+）脉冲压缩比   
·（-)占空比： $\%$ 信号发送与不发送的时间的比率

![](images/9637525fad5d71502bfa6975e6a4b784de79e2e96ae69e57fa68f4abd09f5708.jpg)  
DISTRIBUTloNC.Distributionauthorized to U.S.Government Agenciesand their contractors,9-Aug-19.   
OtherreguestsforthisdocumentshallbereferredtoAFRL/ROOD

·为了使雷达正常工作，您必须包括一个接收器。然而，您不一定需要定义其任何参...

```txt
receiver   
antenna_ohmic_loss <db-ratio-value>   
antenna_pattern <pattern-name>   
antenna_pattern_table ... end_antenna_pattern_table   
attenuation_model <derived-name>   
attenuation .... (attenuation is a synonym for attenuation_model)   
aux_data ... end_aux_data   
bandwidth <frequency-value>   
beam_tilt <angle-value>   
check_ferrain_masking <boolean-value>   
check_transmitter_masking <boolean-value>   
detection_threshold <db-ratio-value>   
earth_radiusmultiplier <value>   
effective_earth_radius <length-value>   
frequency <frequency-value>   
wavelength <length-value>   
instantaneous_b-bandwidth <frequency-value>   
internal_loss <db-ratio-value>   
noise_figure <db-ratio-value>   
noise_power <power-value>   
polarization [horizontal | vertical | slant_45 | slant_135 | left_circular | right_circular | default ]   
polarization Effect [horizontal | vertical | slant_45 | slant_135 | left_circular | right_circular ] <fraction>   
propagation_model <derived-name>   
receive_line_loss <db-ratio-value>   
end Receiver 
```

DISTRIBUTioNC.Distributionauthorized to U.S.Government Agenciesand their contractors,9-Aug-19. Otherreguestsforthisdocumentshall bereferred to AFRL/RQQD

19

![](images/182fea1570f5cf9c8af739e19b3226a54d57560dfd1f48c874017ff8d10c20d7.jpg)

# UNCLASSIFIED

# AFSIM中接收机相关

# (Receiver-情况1&2)

![](images/6b297d39963467e372aaf266f71e398e6359a25b47ac1e3a0aafeb880176875e.jpg)

·情况1：如果在接收机模块啥也没有指定，一切默认..

-接收噪声是必须计算的，...AFSIM中默认值是-160 dBW

·情况2：如果只指定了带宽：

理想接收机

$$
N = k * T _ {0} * B
$$

k

$T _ { 0 }$ Nominalambient temperature (290deg-K)

B The(instantaneous)bandwidth of thereceiver.

DISTRIBUTIoNC.Distributionauthorizedto U.S.GovernmentAgenciesand their contractors,9-Aug-19. Otherrequestsforthisdocument shall bereferredto AFRL/RQQD.

·情况3：如果指定了带宽噪声指数

真实接收机

$$
N = k * T _ {0} * B * n o i s e \_ f i g u r e
$$

·情况4：如果您指定带宽、噪声系数、天线欧姆损耗和接收线路损耗

Noise temperature contribution due toreceive line loss

DISTRIBUTioNC.Distributionauthorized to U.S.Government Agenciesand their contractors,9-Aug-19.

Otherrequestsforthisdocument shallbereferredto AFRL/RQQD

21

![](images/09b2ed72fefe62b5ab4c9a70c5bffbbd1ba9e456540ba330f618ff7861434607.jpg)

# UNCLASSIFIED

# 指定噪声功率/调整为1平方米范围

![](images/db261c39c858b1b59aa3a71cddd5ad23e189c29f385149cff4cba0a8eaf4efac.jpg)

·如果您不知道具体的接收器数据，但知道雷达的探测范围，您可以为该范围指定噪声功率。  
·使用one_m2_detection_range命令来确定所需的噪声功率。  
·或者使用adjustment_factor命令来微调1平方米的探测范围（推荐的方法）。  
·将雷达规格设定为最大1平方米的探测范围。  
·不要使用one_m2_detection_range来硬性设置探测范围（这会导致雷达在干扰情况下工作不正常）。

```txt
SENSOR.sensor; mode default   
Peak power output : 50 dBW (100000 W)   
Pulse repetition frequency : 0 Hz   
Pulse width : 0 seconds   
Duty cycle (input:PW/PRI) : 1:0   
Pulse compression ratio : 0 dB (1)   
Average power output : 50 dBW (100000 W)   
Frequency : 2e+08 Hertz   
Wavelength : 1.49896 meters   
Transmitter Antenna Gain : 30 dB (1000)   
Receiver Antenna Gain : 30 dB (1000)   
Transmitter Internal Loss : 0 dB (1)   
Receiver Internal Loss : 0 dB (1)   
Receiver Noise Power : -131.985 dBW (6.3307e-14 W)   
Minimum Detectable Signal : -128.985 dBW (1.26314e-13 W)   
Minimum Detectable S/N : 3 dB (1.99526)   
1 m2 Detection Range : 173031 meters (calibrated - free space)   
Loop Gain : 212.525 dB (calibrated) 
```

DISTRIBUTloNC.Distributionauthorized toU.S.Government Agenciesand their contractors,9-Aug-19.

OtherreguestsforthisdocumentshallbereferredtoAERL/ROOD.

·AFSIM具有生成多种天线模式类型的能力。

一 方位/俯仰表  
-均匀模式  
一正弦（圆形）模式  
-正弦（矩形）模式  
余割模式  
-ESA模式  
-GENAP模式

·也可以使用ALARM模式。

DISTRIBUTioNC.Distributionauthorized to U.S.Government Agenciesand their contractors,9-Aug-19. Otherrequestsforthisdocument shallbereferredto AFRL/RQQD.

23

![](images/a3f0f65b2468ea58c77943478fd56e7e7e9be053ccc74a492608cb68c4de97bf.jpg)

# UNCLASSIFIED

# 天线模式-它们重要吗？

![](images/601d85da7ebf5774a3e07dcac62c4f52abd762666b348b1f4e26f6c532013dca.jpg)

![](images/2d9e780ea73c24deb419212687e6dde54332511fd33b6a170a9ba669280a6f60.jpg)

![](images/58209976716f6db2e5b741ea67c68a7b93b20496a26d1d6ed6895a5d39854c8d.jpg)

![](images/f730b9bbd9fe2ec2a693b153a62fff4434018b15690a89d21c4e172cbcd36c94.jpg)

![](images/498947c672f3fcadb48fcae7c56ab1d963924b54188e7c7f3b56039c7ab6cf41.jpg)

![](images/ac899b1be8b131d8bf0a8a79fa38e172453f54910e13631e6d6f170ec8ce304c.jpg)

![](images/cd541eca768e3e7bea2dfcfaea81291486ff99498eb3c9753cbdcce1e274bb18.jpg)

DISTRIBUTloNC.Distributionauthorized toU.S.Government Agenciesand their contractors,9-Aug-19. Otherrequests forthisdocument shallbereferredto AFRL/RQQD.

![](images/d5dbea8793330a5565b3ecb8208250017c160b0f417da8da84d8d4a134fbf89c.jpg)

![](images/fce0c41676ae5e46749234ac2665a7c6dedd4c4bb0f555df7cb467944b850236.jpg)

![](images/c118bd39ef3c64516d982d892daa753c2d6424a11033b71080b0a2a4ae50b446.jpg)

![](images/1076aed1765888be6431a863cffbb1c23a03ef03884f6c3feb6f0b0edb913f6f.jpg)

![](images/63beee9a7cc5c5ff9d6bdbc48c445cafe409dad213aee2e8e366a9f5428db8ce.jpg)

![](images/81e1fd27044c68e05eb76dfc53544f7a26c2e8da1830320bba33893f675818d7.jpg)

DISTRIBUTioNC.Distributionauthorized to U.S.Government Agenciesand their contractors,9-Aug-19. Otherreguestsforthisdocumentshall bereferred to AFRL/RQQD

25

![](images/2869504ef533387c75c6109fa40490d94447c9e6862005915c9a120e66ffa475.jpg)

# UNCLASSIFIED

# 雷达孔径重要吗？

![](images/e077771b5d8e4ce2b124b12326484ddf6d1137fb5a3682f65dcbdc75f77c8a15.jpg)

![](images/3d23a541aa353eef1b261e592fddedc38eac46426db6ff19ffc77884d91843a7.jpg)

![](images/913742693d4b199707515b0c0fdc73cb94660c35cd4bff28d4f3802fc9006c1b.jpg)

![](images/19f36ad4b93b44bd50ea9e0b8691b9e5779762311f010d1231b26c2a3f43b841.jpg)

![](images/fea8285f00e93be0a577470f422580f05ff4587e73eda3c96deea1366e080a4a.jpg)

DISTRIBUTloNc.Distributionauthorized to U.S.Government Agenciesand their contractors,9-Aug-19. Otherrequests forthisdocument shallbereferred to AFRL/RQQD.

![](images/60847ed3b5df380b7f93d5f9452327a669083cf8f5273f75141ee89c3995349c.jpg)

![](images/b3e9ebe3dba51ac3562b875c15557e2fbb5346f771728b605caaa88134cd4c4f.jpg)

![](images/394cdd420076a80cf042d57c38c89d32bee868d03135dee25f80b2cf5af92957.jpg)

![](images/2cee669374d2c55514b436fe14305052691aa157d73dd6f2793509dc1569a7eb.jpg)

DISTRIBUTioNC.Distributionauthorized to U.S.Government Agenciesand their contractors,9-Aug-19. Otherreguestsforthisdocumentshall bereferred to AFRL/RQQD

27

![](images/4c4e381ed3061d52c762de52b10aea7163bf39a38831fca27d65e1fbb6b21cc8.jpg)

# UNCLASSIFIED

# 波束

![](images/461b5d51d5046b99ca68ea01800022e38685d0e1d4d6ce2e741bb0bac971fd04.jpg)

·许多雷达（尤其是电子战）都是多波束的。  
·这可以是仰角的函数，有时也可以是变化的电子特性（脉冲宽度、脉冲重复频率/间隔、频率）。  
·除非重新定义特性，否则波束1中定义的特性将延续到后续波束。

```txt
beam 1 Antenna Commands .. transmitter ... transmitter commands ... end_transmitter receiver ... receiver commands ... endreceiver ... BeamCommands...   
end_beam 
```

DISTRIBUTIoNC.Distributionauthorizedto U.S.GovernmentAgenciesand their contractors,9-Aug-19. Otherrequestsforthisdocument shall bereferredto AFRL/RQQD.

![](images/2ae7862c111e9ad50e1caefa032b074aea762dd9edf0b5e566e9df50d5f98c17.jpg)

![](images/ce3d8a435fbee5fee861c1c7eb16e5e6478427de74170aae2febb323497c5a54.jpg)

![](images/579d3055d4f3879a4716940b0a7116c1c889017ccc6dc2d2a4c95de9ea5d4737.jpg)

![](images/3faadae60560525e9b72aec7ca5651e93426f4c7f72d50650512aa03b3a9f48c.jpg)

![](images/208d98299a182abc7410d961a81996106308ef10e2ce9ae39d80e28ff41b0f45.jpg)

DISTRIBUTIoNC.Distribution authorized toU.S.Government Agenciesand their contractors,9-Aug-19. Otherrequestsforthisdocument shall bereferred to AFRL/RQQD.

29

![](images/abb272ac5f1d24a13371b6c1bc839906c40fe7388d059f4beaee543223c7442b.jpg)

# 波策示例占空比

![](images/846737400f8aa9865b528497ce1e5576523866cc405796d4c0e111495e61f9a7.jpg)

![](images/13bab0bccb922a6234b8757681b2a05bd616441189fde81e34eca930708f4a05.jpg)

![](images/988fc80893b50169a4c2599136f1d486a53f04c29bb4b4063f69804441e8544c.jpg)

DISTRIBUTIoNC.Distribution authorized toU.S.Government Agenciesand their contractors,9-Aug-19. Otherrequestsforthisdocument shall bereferredto AFRL/RQQD.

·通常，电子战雷达（包括HF/TAR）是无模式的。但它们可能有多个波束。  
·TTR/FCR通常有模式。但是，如果您使用模式，则必须有策略/脚本来控制其模式。

DISTRIBUTioNC.Distributionauthorized to U.S.Government Agenciesand their contractors,9-Aug-19. Otherreguestsforthisdocument shall bereferred to AFRL/RQQD

31

![](images/a237c97875a94fab028c4d103b62fbefedd0ef59ec924add6754ccd4b06434cc.jpg)

UNCLASSIFIED

![](images/a790da368d5d974da7708be4f5672dab9c99647d903d294dae078d43b19d5d92.jpg)

# 问题？

DISTRIBUTIoNC.Distribution authorized toU.S.Government Agenciesand their contractors,9-Aug-19. Otherrequestsforthisdocument shall bereferredto AFRL/RQQD.

32

# 6.1.4.2.2. 目标特性与组件管理 6_AFSIM_User_Training_Signatures_PartManager

本文为 afsim2.9_src\training\user\4_Sensors\slides\6_AFSIM_User_Training_Signatures_PartManager.pptx 的翻译。

![](images/36aa0628e5b5d9218d9e2aa56191c2e5405354cb4b41d93d93d4a09b8daa04ce.jpg)

Integrity★Service★ Excellence

# AFSIM用户培训6－特性和组件管理

# AFRL/RQQD美国空军研究实验室

DISTRIBUTioNC.Distributionauthorizedto U.S.Government Agenciesand their contractors,9-Aug-19. OtherrequestsforthisdocumentshallbereferredtoAFRL/RQQD

1

![](images/4543ecb7bc6d212ba94e2f89ab4af533e9e90cba56681db21df22c8830c11688.jpg)

# UNCLASSIFIED

# 学习目标

![](images/4a652d5354376930a72de82128111337432d55178cec4ee9e44e40404acb7d59.jpg)

·包括：

－定义平台的特性  
－添加一个特性到平台  
－使用平台组件管理  
－使用天线模式可视化工具

![](images/4974f6025b54384bc50dec76eeb727043ea8d117a4cdd12ac3f06a7ded511c5d.jpg)

DISTRIBUTioNC.Distributionauthorized to U.S.GovernmentAgenciesandtheircontractors,9-Aug-19. Otherrequestsforthisdocument shallbereferredtoAFRL/RQQD.
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