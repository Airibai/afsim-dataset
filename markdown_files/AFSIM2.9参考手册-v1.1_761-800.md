# 3.8.1.1. 箔条武器 WSF_CHAFF_WEAPON

```txt
weapon <name> WSF_CHAFFWEAPON
... Platform Part Commands ...
... Articulated Part Commands ...
... WSF_EXPLICIT_WEAPON Commands ...
ejector <name>
    ... Chaff Ejector Commands ...
end_ejector
... additional ejector definitions
cloud_update_interval ...
draw 
```

WSF_CHAFF_WEAPON 代表一种释放箔条包（WSF_CHAFF_PARCEL）的武器，这些包由大量短路调谐的偶极天线组成，切割成特定长度以在感兴趣的频率范围内产生所需的雷达截面积（RCS）响应。一个或多个释放的箔条包组合形成一个箔条云，通常用作雷达对抗措施，可以用于走廊铺设或自我保护模式。

# 主要特性

箔条云：不是模拟实体，而是用于计算与交互的发射器和接收器的双基地呈现面积的包的聚合。

箔条武器：作为 WSF_EXPLICIT_WEAPON，创建包（每个包建模为单独的平台），由一个或多个弹射器系统释放。每个弹射器都有一个唯一名称，可以独立配置以指定包的数量和类型、平台上的位置以及弹射速度。

# 命令

cloud_update_interval <time-value>

如果非零，指定模拟将更新释放的箔条包状态（位置、速度、大小等）的周期时间间隔。如果为零，则仅在需要确定其状态时更新包。

默认值： 0.0

draw_cloud_approximations <boolean-value>

如果为 true，将使用 WsfDraw 绘制一个椭球体，表示用于调试目的的云近似。可用于

可视化用于 RCS 计算的云的呈现面积。

默认值： false

launched_platform_type <string-reference>

虽然在 WSF_EXPLICIT_WEAPON 中是必需的，但对于 WSF_CHAFF_WEAPON 是可选的。可以指定以向释放的包添加用户定义的脚本或其他自定义平台命令。

默认值： 如果未指定，将使用虚拟 WSF_PLATFORM 类型。

# 箔条弹射器命令

quantity <integer-value>

指定弹射器中最初可用的包数量。

默认值： 10

parcel_type <string-reference>

指定此弹射器释放的箔条包类型。指定的值必须代表一个有效的包类型，必须在模拟中初始化此弹射器时定义。

默认值： 无默认值。必须指定。

1 location <x length-value> <y length-value> <z length-value> <length-units>

指定弹射器在释放平台的实体坐标系中的位置。

默认值： 000 米

ejection_velocity <speed-value>   
ejection_elevation <angle-value>   
ejection_azimuth <angle-value>

指定相对于释放平台的发射机制提供的附加速度的大小、方位和仰角。类似于launch_delta_v，但以球面坐标而非笛卡尔坐标指定。

默认值： 15.0 m/s, 0.0 deg, 0.0 deg

# 其他信息

箔条的组成：通常由铝涂层的材料制成，如铝化的 Mylar 薄膜或铝涂层的晶体硅芯，切割成特定长度以优化雷达反射。

使用策略：箔条的主要使用策略包括力量屏蔽和自我保护，不同的释放技术用于每种策略。

这种武器系统通过创建干扰云来迷惑敌方雷达，提供有效的电子对抗能力。

# 3.8.1.1.1. 箔条包 WSF_CHAFF_PARCEL

```txt
chaff_parcel <name> WSF_CHAFF_PARCEL
# Geometric inputs
bloom_diameter ...
expansion_time_constant | bloom_time_constant ...
# Kinematic inputs
terminal Velocity ...
deceleration_rate ... 
```

```txt
Lifetime and debugging inputs expiration_time ... debug ... # Signal return (RCS) inputs RCS Related Commands end_chaff_parcel 
```

概述

WSF_CHAFF_PARCEL 代表从 WSF_CHAFF_WEAPON 系统的弹射器中释放的箔条包或束。它们被建模为球体，其平均径向尺寸根据膨胀方程计算为指数增长：

$$
R _ {p a r c e l} = 0. 5 D _ {m a x} (1 - e ^ {- t _ {f a l l} / \tau D})
$$

其中， $D _ { m a x }$ 是膨胀直径（bloom_diameter）， $t _ { f a l l }$ 是包被弹射后的时间，??是膨胀时间常数（expansion_time_constant）。

通过调用脚本方法 WsfChaffWeapon.DropChaffCloud 投放的一组一个或多个包共同形成一个箔条云。当被射频能量照射时，每个包产生一个雷达截面（RCS）定义的返回信号：

$$
\sigma_ {p a r c e l} = \frac {A _ {p}}{N} \big [ 1 - e ^ {- (N \sigma_ {m a x} / A _ {p})} \big ]
$$

其中， $A _ { p }$ 是云的双站呈现面积，N 是云中的包数量， $\sigma _ { m a x }$ 是分散包的最大理论 RCS，当其偶极子间距较大时（即无屏蔽效应）。

云的双站呈现面积考虑了包的膨胀和视角依赖性。它是发射器和接收器所呈现面积的平均值，每个面积使用视角计算云从正面和侧面观察的截面积的加权均方根值。

$\sigma _ { \mathrm { m a x } }$ 可以是频率的函数，并通过 frequency_maximum_rcs_table 命令指定。如果未指定此表， $\sigma _ { \mathrm { m a x } }$ 假设为半波偶极子（所有偶极子切割为相同长度 $\mathrm { L } = \lambda / 2$ ）的点箔条计算如下：

$$
\sigma_ {m a x} = 0. 1 5 N _ {d} \lambda^ {2}
$$

其中， $N _ { d }$ 是通过 number_dipoles 命令指定的箔条偶极子数量，λ是雷达的波长。

注意：当箔条包落地或达到由 expiration_time 指定的最大时间时，将从模拟中移除。

命令说明

bloom_diameter <length-value>

指定包膨胀到的直径，随着时间趋于无穷大。

默认值：10.0 米

expansion_time_constant <time-value>

指定膨胀时间常数（ ）。

默认值：0.75 秒

terminal_velocity <speed-value>

包的自由落体速度。假设包在弹射时瞬间达到终端速度。

默认值： $1 . 0 \ : \mathrm { m } / s$

deceleration_rate <acceleration-value>

包弹射时的减速率。应指定一个正值，表示与初速度矢量相反的加速度矢量的大小。

默认值： $1 0 0 . 0 \ : \mathrm { m } / s ^ { 2 }$

expiration_time <time-value>

包将在弹射后从模拟中移除的时间，除非它先落地。

默认值：60.0 秒

debug <boolean-value>

如果为 true，将在控制台打印关于包状态的调试信息。

默认值：false

# RCS 相关命令

▪ frequency_maximum_rcs_table … end_frequency_maximum_rcs_table

定义包的最大 RCS 响应作为频率的函数。此表用于在包 RCS 方程中查找 $\sigma _ { m a x }$ 的值。预期格式：

```txt
frequency_maximum_rcs_table [independent_variable [units <frequency-unit>] [precision <double | float>] [extrapolate]] [dependent_variable [units <area-db-unit>] [precision <double | float>]] <frequency-1> <max-rcs-1> <frequency-2> <max-rcs-2> ... end_frequency_maximum_rcs_table 
```

如果未指定单位，频率假定为 Hz，RCS 为 dBsm。

number_dipoles <integer-value>

如果未定义 frequency_maximum_rcs_table， $\sigma _ { m a x }$ 可以根据箔条偶极子数量和雷达波长计算，假设为随机定向的半波偶极子。

默认值：1e6

# 3.8.1.2. 六自由度显式武器 WSF_P6DOF_EXPLICIT_WEAPON

```txt
weapon <name> WSF_P6DOF_EXPLICIT_WEapon ... Platform Part Commands ... ... Articulated Part Commands ... ... WSF_EXPLICIT_WEapon Commands ... add_subobject ... endweapon 
```

WSF_P6DOF_EXPLICIT_WEAPON 是从 WSF_EXPLICIT_WEAPON 派生的，代表一种在发射时被建模为独立平台的武器。该武器允许装备有 WSF_P6DOF_MOVER 的平台发射或抛弃其P6DOF 子对象作为武器。这意味着在发射之前，移动器将模拟子对象的任何空气动力学、

推进和/或质量效应（如重量和阻力），并在子对象发射/发射后停止这样做。这种方式可以通过 WSF_P6DOF_MOVER 适当地建模由于携带武器而导致的性能下降。此外，武器相对于母体飞行器的相对位置和方向在 p6dof_object_type 的定义中自动指定。由于子对象在发射时将拥有自己的独立平台，因此它是显式武器。任何分离速度和/或角速度都在父 P6DOF 对象中指定。

命令

add_subobject <string>

指定将在 WSF_P6DOF_MOVER 上发射/发射的子对象的基本名称。武器（发射器）支持的每个单独子对象都需要自己的 add_subobject 命令行。每个子对象必须有一个唯一名称。子对象武器将按照列出的顺序发射。与子对象关联的发射平台类型使用 P6DOF 平台映射中包含的定义指定。

默认值： 无默认值。必须指定。

# 忽略的命令

以下命令将被忽略，如果使用，将导致警告：

```yaml
- launchedplatform_type
- quantity
- maximumquantity
- reload_increment
- reload_inventory
- reload_time
- inhibit_while_reloading
- launch_dalta_v
- ignore_launchplatform_velocity 
```

# 使用注意事项

□ 独立平台建模：每个子对象在发射时被建模为独立的平台，允许更精确的物理模拟。  
▫ 子对象管理：通过 add_subobject 命令管理子对象的发射顺序和属性。  
□ 性能影响：在发射前，母体平台的性能会受到子对象的影响（如重量和阻力），发射后这些影响将被移除。

这种武器系统适用于需要精确建模和控制的场景，尤其是在涉及复杂空气动力学和推进系统的情况下。

# 3.8.1.3. 六自由度显式武器 WSF_SIX_DOF_EXPLICIT_WEAPON

同上节的 3.8.1.2 六自由度显式武器 WSF_P6DOF_EXPLICIT_WEAPON。

# 3.8.2. 隐式武器 WSF_IMPLICIT_WEAPON

```txt
weapon <name> WSF_IMPLICITWEAPON ... Platform Part Commands ... ... Articulated Part Commands ... 
```

```txt
...Weapon Commands ..   
launchedPLATFORM_type ...   
quantity ...   
endweapon 
```

WSF_IMPLICIT_WEAPON 代表一种不需要独立飞行的武器。对于隐式武器，没有创建武器平台。通常，这些武器直接对准特定目标发射，而不是使用轨迹提供其他信息（如目标坐标）。隐式武器通常与发射计算机一起使用（例如，建模为隐式的间接火力武器）。在这种情况下，交战在发射计算机的拦截时间计算时进行评估。默认情况下，如果未使用发射计算机，交战将在武器的 update_interval（如果指定）上进行评估。然而，派生的武器模型（如WSF_LASER_WEAPON）可能会在指定的间隔内提供自己的实现。

命令

launched_platform_type <string-reference>

如 WSF_EXPLICIT_WEAPON 中所述，此命令指定发射此类武器时要创建的平台类型。虽然隐式武器不会创建新平台，但如果隐式武器使用发射计算机，则可能需要此命令。发射计算机文档将列出此要求（如果适用）。

默认值： 无默认值。如果需要，必须指定。

quantity <real-reference>

此命令与 quantity 相同，但隐式武器的默认值不同。

默认值： maximum_quantity 的值

# 使用注意事项

直接发射：隐式武器通常直接对准目标发射，不依赖于轨迹信息。

与发射计算机的集成：如果使用发射计算机，可能需要指定 launched_platform_type。

评估时间：如果没有发射计算机，交战评估将在 update_interval 上进行。

这种武器系统适用于需要快速响应和直接打击的场景，尤其是在不需要复杂轨迹计算的情况下。

# 3.8.3. 激光武器 WSF_LASER_WEAPON

```txt
weapon <name> WSF_LASER_WEAPON ... Platform Part Commands ... ... Articulated Part Commands ... ... Weapon Commands ... thermal_system ... Thermal System Commands ... end_thermal_system fluence_model <type> ... Fluence Model Commands ... 
```

```txt
end_fluence_model  
firing_time ...  
firing_update_interval ...  
Non-Thermal System Related Commands  
number_of_shots ...  
cooling_time ...  
Thermal System Related Commands  
cooling_update_interval ...  
efficiency...  
high_temperature_limit ...  
low_temperature_limit ...  
minimum_total_firing_time ...  
end weaponry 
```

WSF_LASER_WEAPON 代表一种高能激光（HEL）武器。大多数输入参数用于fluence_model（参见：3.8.3.1 影响模型 Fluence_model），该模型确定激光能量的传播和在目标上的沉积，以及与热相关的输入，这些输入限制了激光在必须散发多余热能之前的发射时间。

# 不兼容的命令

以下命令与 WSF_LASER_WEAPON 不兼容，使用这些命令将导致警告或错误：

```txt
quantity maximum�数量 maximum_number reload incremment reload_inventory reload_threshold reload_time inhibit while reloading 
```

# 命令

firing_time <time-value>

指定每次射击的发射时间。

注意：如果用户未设置 firing_time，激光将继续发射，直到用户通过调用 CeaseFire 终止交战，或热系统阻止激光发射。

firing_update_interval <time-value>

指定更新交战和在目标上积分能量的间隔。

默认值： 如果设置了 firing_time，则为 $0 . 1 ~ ^ { * }$ firing_time，否则为 0.1 秒。

# 非热系统相关命令

这些命令在未指定 thermal_system 时有效。

number_of_shots <integer-value>

指定激光在必须冷却之前可以发射的次数。

默认值： 1000000（无限制）

cooling_time <time-value>

指定冷却时间，从指定的 number_of_shots 用尽后开始。

默认值： 30 秒

热系统相关命令

这些命令在指定 thermal_system 时有效。

cooling_update_interval <time-value>

指定检查冷却周期是否完成的间隔。

默认值： 10.0 秒

efficiency <real-value>

指定 HEL 系统将输入功率转换为输出激光功率的效率。

默认值： 0.3

high_temperature_limit <temperature-value>

这是发射停止并开始冷却的温度（热系统不接受高于此温度的热量）。

默认值： 100 摄氏度

low_temperature_limit <temperature-value>

这是最大发射时间可用的温度（热系统不会冷却到低于此温度）。

默认值： -20 摄氏度

minimum_total_firing_time <time-value>

在冷却周期中，武器在恢复到此发射时间之前不可用。

默认值： 5 秒

这些命令和参数帮助配置 WSF_LASER_WEAPON 的性能，以便在不同的操作条件下进行有效的目标打击和热管理。

# 3.8.3.1. 影响模型 Fluence_model

```txt
fluence_model <fluence-model-type-name>  
aperture_diameter ...  
atmospheric_structure ...  
beam_quality ...  
calculate_incidence ...  
jitter ...  
laser_type ...  
power ...  
wavelength ...  
... derived model type commands  
endfluence_model 
```

fluence model 被 WSF_LASER_WEAPON 和 WSF_CUED_LASER_WEAPON 用于计算由于抖动、衍射、大气湍流、消光和目标效应引起的光束扩散和光束损失。

默认几何计算方法

默认情况下，目标几何的计算假设为正面、最大有效的角度。这可以通过使用calculate_incidence 输入进行余弦衰减来修改。然而，模拟目标几何的最佳方法是使用WSF_INTERSECT_PROCESSOR 和表示目标几何的交叉网格。

<fluence-model-type-name>指定影响模型，当前影响模型支持默认影响模型 default，参见：3.8.3.2 默认影响模型 default fluence_model。

# 命令说明

aperture_diameter <length-value>

定义高能激光系统的孔径直径。改变此参数会控制衍射引起的光束扩散，影响目标上的光束大小。孔径直径越大，目标上的光束越小，能量密度越大（能量密度 ~(孔径直径^2)）。

atmospheric_structure <hv57>

指定用于计算大气湍流的气象结构模型或 $C _ { n } ^ { 2 }$ 函数。单位为 $m ^ { - 2 / 3 }$ 。

默认值：hv57

注意：目前仅提供 HV5/7 模型（hv57）。未来可能会提供更多选择。

beam_quality <real-value>

指定光学系统的光束质量。光束质量是光束轮廓与完美高斯光束的接近程度的度量。具体来说，它是衍射极限半径的乘数因子。其值从 1（衍射极限）到大于 1 的值。

默认值：1.1

calculate_incidence <boolean-value>

指定是否根据目标的角度计算入射角，正面角度代表最小（0 度）入射。任何大于 90 度的入射角将被视为无效。

默认值：禁用

注意：此功能已被交叉网格和 WSF_INTERSECT_PROCESSOR 的使用取代。

jitter <angle-value>

指定系统的抖动（通常在微弧度范围内）。抖动越大，高能激光束在目标上的“扩散”越大。

默认值：6.6e-7

laser_type carbon_dioxide | nd_yag | coil | deuterium_fluoride

指定高能激光类型。这反过来指定了波长，模型需要此波长来计算光束的衍射和消光。

注意：目前优先使用此命令而不是 wavelength。

注意：波长、haze_model 和 atmosphere_model 的值被用来查询由 MODTRAN 生成的大气系数表 atmospheric_coefficients（参见：3.8.3.2.1 大气系数表 atmospheric_coefficients），以便在模拟中进行精确的光束传播计算。

power <power-value>

这是从孔径发射的实际激光功率。

wavelength <length-value>

激光操作的波长（例如，Nd-YAG 激光器为 1.064 微米）。当前支持的波长（以纳米为单位）包括：

□ 1000（碳酸气体）  
□ 1064（Nd:YAG）  
□ 1315（COIL- 碘激光）  
3800（氟化氘）

注意：波长、haze_model 和 atmosphere_model 的值被用来查询由 MODTRAN 生成的

大气系数表 atmospheric_coefficients（参见：3.8.3.2.1 大气系数表 atmospheric_coefficients），以便在模拟中进行精确的光束传播计算。

这些命令提供了详细的配置选项，以便在模拟中精确地计算激光与目标的交互效果。

# 3.8.3.2. 默认影响模型 default fluence_model

```txt
fluence_model default  
base fluence model commands  
atmosphere_model ...  
haze_model ...  
end Fluence_model 
```

默认 fluence_model 提供了对光束抖动、衍射、大气湍流和大气消光的表示。它基于论文《高功率激光传播》（F. Gebhardt，应用光学，vol.15(6)，1479-1493）。此模型需要针对 给 定 波 长 或 激 光 类 型 、 atmosphere_model 和 haze_model 的 有 效atmospheric_coefficients。目前，这些可以在任何 WSF 版本（1.7.5 或更高版本）中找到，位于目录 hel_demo/atmosphere 中。

atmosphere_model <integer-value>

指定要使用的大气模型。有效值为 1-6，并对应以下内容：

1. 热带大气  
2. 中纬度夏季（默认）  
3. 中纬度冬季  
4. 亚北极夏季  
5. 亚北极冬季  
6. 1976 美国标准

注意：目前，所有模型仅支持 1064 纳米波长；否则，仅支持模型 2（中纬度夏季）。

haze_model <integer-value>

指定要使用的雾霾模型。有效值为 1-5，并对应以下内容：

1. 农村消光，能见度 $= 2 3$ 公里（晴朗）（默认）  
2. 农村消光，能见度 $= 5$ 公里（雾霾）  
3. 海军海洋消光  
4. 海洋消光，能见度 $= 2 3$ 公里  
5. 城市消光，能见度 $= 5$ 公里

注意：目前，所有模型仅支持 1064 纳米波长（激光类型 nd_yag）；否则，仅支持模型 1（晴朗）。

# 3.8.3.2.1. 大气系数表 atmospheric_coefficients

```txt
atmospheric_coefficients altitude ... end_altitude attenuation ... end_attenuation scattering ... end_scattering wavelength <length-value> haze_model <integer-value> atmosphere_model <integer-value> 
```

在使用 fluence_model 与 WSF_LASER_WEAPON 或 WSF_CUED_LASER_WEAPON 时，需要大气系数。这些通常是通过 ModTran 为给定波长、雾霾模型和大气模型生成的。目前，在 WSF 标 准 发 布 版 本 WSF 1.7.5 （ 2013 年 3 月 28 日 及 以 上 版 本 ） 的hel_demo/atmosphere 文件夹中，有以下标准激光类型的数据：

```txt
二氧化碳 1000 nm  
ND-YAG 1064 nm  
COIL 1315 nm  
氟化氘 3800 nm
```

支持的大气模型

从 ModTran 支持以下大气模型，模型 2、3 和 6 支持 1064nm 波长的 WSF；否则，其他波长仅支持模型 2：

1. 热带大气  
2. 中纬度夏季（默认）  
3. 中纬度冬季  
4. 亚北极夏季  
5. 亚北极冬季  
6. 1976 美国标准

# 支持的雾霾值

目前，所有模型仅适用于 1000 和 $\mathsf { 1 0 6 4 } \mathsf { n m }$ 波长（CO2 和 Nd-YAG）；否则，仅支持模型 1（请参阅下面的模型提取程序，以访问其他波长的其他模型）：

1. 农村消光，能见度 $= 2 3$ 公里（晴朗）（默认）  
2. 农村消光，能见度 $= 5$ 公里（雾霾）  
3. 海军海洋消光  
4. 海洋消光，能见度 $= 2 3$ 公里  
5. 城市消光，能见度 $= 5$ 公里

# 其他字段说明

altitude … end_altitude：提供相应衰减和散射系数块的海拔列表。  
attenuation … end_attenuation：以 $1 / \mathsf { m }$ 为单位的衰减系数列表。此块中的每个条目与 altitude 块中的条目对应。  
scattering … end_scattering：以 $1 / \mathsf { m }$ 为单位的散射系数列表。此块中的每个条目与altitude 块中的条目对应。  
wavelength <length-value>：表格有效的波长。  
haze_model <integer-value>：使用的雾霾模型，对应上述值之一（1-5）。这应该是用于ModTran 运行的输入值。  
atmosphere_model <integer-value>：使用的大气模型，对应上述值之一（1-6）。这应该是用于 ModTran 运行的输入值。

# 3.8.4. 导引激光武器 WSF_CUED_LASER_WEAPON

```txt
weapon <name> WSF_CUED_LASER_WEAPON beamdirector <string> 
```

```txt
use_default_beamdirector ... Platform Part Commands ... ... Articulated Part Commands ... ... Laser Weapon Commands ... ... Weapon Commands ... endweapon 
```

WSF_CUED_LASER_WEAPON 是 WSF_LASER_WEAPON 的一种实现，它由一个独立的光束指挥器（beamdirector）引导。这个光束指挥器模型是一个传感器，用于获取高能激光（HEL）目标，并确保 HEL 能够对其进行射击。一旦武器发射，光束指挥器会尝试对准目标感兴趣的区域。只有当光束指挥器的提示在约束范围内（包括图像大小、云台速率和目标遮挡）时，武器才会开始高能激光发射。如果提示因任何原因丢失，HEL 发射将停止，目标提示必须由光束指挥器重新获取。

# 关键特性

自动链接：在同一平台上定义 WSF_CUED_LASER_WEAPON 和 WSF_BEAM_DIRECTOR即可，武器会自动找到并链接到光束指挥器。  
光束指挥器的选择：可以通过 beam_director 命令指定光束指挥器，也可以使用use_default_beam_director 命令禁用指定功能，自动链接到遇到的第一个光束指挥器。

命令

beam_director <string>

指定要附加到此引导激光武器的 WSF_BEAM_DIRECTOR 对象。当指定时，引导激光武器将在同一平台上搜索具有指定名称的光束指挥器。如果找到，武器将链接到它。如果在平台上找不到光束指挥器，初始化将失败。

use_default_beam_director

禁用指定 WSF_BEAM_DIRECTOR 的能力，而是链接到遇到的第一个光束指挥器。

# 使用注意事项

光束指挥器的作用：光束指挥器负责获取目标并确保激光武器能够对准目标进行有效打击。  
目标提示丢失：如果目标提示丢失，激光发射将停止，必须重新获取目标提示以继续操作。

这种武器系统通过结合光束指挥器的精确引导和高能激光的强大打击能力，提供了一种有效的远程打击解决方案，适用于需要精确目标获取和打击的军事应用。

# 3.8.5. 射频干扰武器 WSF_RF_JAMMER

```txt
Single mode jammer definition weapon <name> WSF_RF_JAMMER ... Platform Part Commands ... 
```

```txt
...Articulated Part Commands ...   
...Weapon Commands ...   
...Antenna Commands ...   
...transmitter Commands ...   
...Commands ...   
...Mode Commands ...   
...Group Commands ...   
...Spot Commands ...   
endweapon   
#Multiple mode jammer definition   
weapon<name>WSF_RF_JAMMER   
...Platform Part Commands ...   
...Articulated Part Commands ...   
...Weapon Commands ...   
mode_template   
...Antenna Commands ...   
transmitter Commands ...   
...Commands ...   
...Mode Commands ...   
...Group Commands ...   
...Spot Commands ...   
end_mode_template   
mode <mode-name-1>   
...Antenna Commands ...   
transmitter Commands ...   
...Commands ...   
...Mode Commands ...   
...Group Commands ...   
...Spot Commands ...   
end_mode   
...additional mode definitions ...   
endweapon 
```

WSF_RF_JAMMER 是一种射频干扰器，可用于干扰雷达、电子支援措施（ESM）和无线电通信系统。干扰器可以由多个波束和多个点组成，分别代表干扰器的空间和频率元素。多个干扰器还可以组合在一起形成一个“功率”组。

多模式考虑

干扰器支持类似于传感器的“模式”概念。模式是干扰器的一组命名操作特性。可以不使用多个模式。如果干扰器实现支持模式且未定义显式模式，则任何与模式相关的命令都假定属于隐式定义的名为“default”的模式。

如果将使用多个模式，可以定义一个 mode_template 来指定所有模式之间的共同特性。mode_template 不必定义，但如果定义，则必须在第一个 mode 命令之前定义。如果使用mode_template，则每个模式的初始配置从 mode_template 复制，然后任何对模式的添加或修改应出现在适用的 mode 和 end_mode 命令之间。

命令

以下命令阻止干扰器发射机与模拟中的指定标准进行交互。这些命令适用于WSF_RF_JAMMER 发射机，可以位于顶层或发射机 … end_transmitter 输入块和/或模式命令块中。发射机的相关命令参数参见：3.5.5.8 发射机 transmitter。

ignore <category-name>

指示干扰器应拒绝与属于指定类别的对象进行交互。此命令可以多次指定以拒绝与多个类别的交互。

ignore_domain [ land | air | surface | subsurface | space ]

指示干扰器应拒绝与属于指定空间域的平台或平台上的对象进行交互。此命令可以多次指定以拒绝与多个域的交互。

ignore_side <side>

指示干扰器应拒绝与属于指定侧的平台或平台上的对象进行交互。此命令可以多次指定以拒绝与多个侧的交互。

ignore_same_side

指示干扰器应拒绝与附加干扰器的平台上同一侧的平台或平台上的对象进行交互。组命令

jammer_group <string>

干扰器组名称，此干扰器将成为该组的成员。此输入还将此组名称添加为类别，从而启用 WsfPlatformPart 中定义的脚本类别检查。然而，反之则不成立。类别不会将干扰器组名称添加到干扰器中。

group_power_distribution [ average | constant ]

干扰器组的组功率分布。如果选择 average，则总功率在活动组成员之间平均分配。

默认值：constant

# 模式命令

frequency_band <lower-frequency> <upper-frequency>

指定频带。此输入可以代替发射机频率和带宽输入，使用最后一个输入定义。

repeater … end_repeater

定义使用 ESM 系统启动、停止和维护干扰分配（即闭环[自动化]）所需的逻辑。此外，如果从发射机（例如雷达/通信）到 ESM 的当前几何形状不允许检测，则重复器逻辑当前实现为阻止干扰功率。此阻止逻辑可能过于强大，超出了预期效果。重复器需要 ESM 传感器具有 internal_link 才能在手动以外的任何模式下运行。

定义重复器逻辑：

```txt
repeater debug <boolean-value> operating_mode <operating-mode-string> signal_followering <boolean-value>   
end_repeater 
```

debug

如果在 repeater … end_repeater 输入块中指定，则为重复器设置调试模式。

▫ operating_mode <operating-mode-string>

指定重复器的操作模式，如下所述：

manual：通过用户输入（即脚本）方法或其他手动类型方法启动和停止干扰分配。  
semi-auto：通过用户输入方法手动启动干扰分配，并根据内部链接的 ESM 传感器轨迹自动停止。  
auto：根据内部链接的 ESM 传感器轨迹启动和停止干扰分配。

注意：ESM 传感器必须报告频率。

默认值：manual

□ signal_following <boolean-value>

指定重复器（即 ESM）是否将跟随轨迹的信号变化进行更新，允许重复器监视 ESM传感器轨迹更新以进行信号变化。

注意：ESM 传感器必须报告频率。

默认值：false

debug_repeater

仅在此模式下将重复器的调试模式设置为 true。

默认值：false

# 波束命令

maximum_number_of_beams <integer>

干扰器上的最大波束数量。

默认值：1

beam_power_distribution [ average | constant ]

干扰器波束上的波束功率分布。如果选择 average，则总功率在活动波束之间平均分配。

默认值：average

# 点命令

maximum_spots_per_beam <integer>

干扰器每个波束上的最大点数。

默认值：1

maximum_number_of_spots <integer>

模拟干扰器时的最大点数。如果在此输入之后输入 maximum_number_of_beams 和/或maximum_spots_per_beam ， 则 此 输 入 等 于 这 两 个 输 入 的 乘 积 。 如 果 在maximum_number_of_beams 和/或 maximum_spots_per_beam 之后输入此输入，则这将限制此干扰器可用的活动点的总数。

默认值：1 或 maximum_number_of_beams * maximum_spots_per_beam（如果在输入中提供了任一项）

spot_power_distribution [ average | constant ]

干扰器所有波束上的点功率分布。如果选择 average，则总功率在每个波束上的活动点之间平均分配。

默认值：average

# 3.8.6. 武器效能模型 weapon effects

# 3.8.6.1. 显式武器效果 WSF_EXPLICIT_WEAPON_EFFECT

```txt
weapon_effects <name> WSF_EXPLICIT_WEAPON_EFFECT ... weapon_effects Commands ... ... WSF_EXPLICIT_WEAPON_EFFECT Commands ... end weapon_effects 
```

WSF_EXPLICIT_WEAPON_EFFECT 是一种武器效果的基类，可以在某个有效爆炸半径内对任何平台造成伤害。这种效果通常用于模拟武器的爆炸或冲击波对周围环境的影响。

命令

maximum_radius <length-value>

指定武器在其有效爆炸半径内产生效果的最大半径。这意味着在这个半径范围内的任何平台都可能受到武器效果的影响。

使用注意事项

爆炸半径：确保设置的 maximum_radius 适合模拟所需的武器效果范围。过大的半径可能导致不必要的性能开销，而过小的半径可能无法有效模拟武器的实际影响。  
平台影响：在指定的半径内，所有平台都可能受到影响，因此在设计武器效果时需要考虑到友军和敌军平台的相对位置。

这种武器效果系统适用于需要模拟爆炸或冲击波影响的场景，尤其是在需要精确控制影响范围和强度的情况下。

# 3.8.6.2. 显式武器效果 WSF_EXPLICIT_WEAPON_EFFECTS

```txt
weapon_effects <name> <base-type>
... weapon_effects Commands ...
... WSF_EXPLICIT_WEAPON_EFFECTS Commands ...
end weapon_effects 
```

WSF_EXPLICIT_WEAPON_EFFECTS 定义了显式建模武器的所有武器效果类的通用命令。这些效果用于模拟武器在爆炸或撞击点附近对目标的影响。

maximum_radius <length-value>

定义武器可能产生效果的最大斜距（从爆炸/撞击点到目标的距离）。这个值用于限制必须检查可能损坏的平台数量，有效地排除“远处”对象的考虑。

默认值： $0 \mathsf { m }$ （未提供 - 无限制，或由派生类限制）

注意：如果未提供此值，派生类可能会提供一个值。例如，WSF_GRADUATED_LETHALITY将其设置为略大于其表中最大半径的值。

限制派生类值：如果提供此值，它也可能限制派生类定义的任何值。例如，如果表中的最大半径为 200 米，而此命令指定的值为 100 米，则仅考虑爆炸/撞击点 100 米内的平台。这允许快速临时限制武器效果。

使用注意事项

范围限制：通过设置 maximum_radius，可以有效地减少需要考虑的目标数量，从而提高模拟效率。

派生类的影响：派生类可能会根据其特定需求调整或覆盖此值，因此在使用时应考虑到这一点。

这种武器效果系统适用于需要精确控制影响范围的场景，尤其是在复杂的战场环境中。

# 3.8.6.3. 卡尔顿杀伤模型 WSF_CARLTON_LETHALITY

```txt
weapon_effects <name> WSF_CARLTON_LETHALITY ... weapon_effects Commands ... ... WSF_EXPLICIT_WEapon_EFFECTS Commands ... ... WSF_CARLTON_LETHALITY Commands ... end weapon_effects 
```

WSF_CARLTON_LETHALITY 使用卡尔顿损伤方程，通常用于对固定地面目标的间接火力炮击。该模型假设下射程和横射程的偏差距离发生在包含目标的水平面内，武器的速度矢量用于将这些值定向为近-远、右-左方向。任何 Z 轴偏移都被忽略，武器或目标的方向无关紧要。

卡尔顿致命性模型方程

$$
P _ {k} = D _ {0} \times e ^ {(\frac {- \pi D _ {0}}{L A} \times (x ^ {2} \times R D R + y ^ {2} \times \frac {1}{R D R}))}
$$

其中：

□ $\mathrm { D } _ { 0 }$ ：武器/目标对的输入参数（定义为输入值）。  
□ LA：武器/目标对的致命区域（定义为输入值）。  
RDR：计算公式为 $\frac { 1 } { 1 { - } 0 . 8 { \times } \cos { \mathrm { A } } 0 \mathrm { F } }$ 其中 为武器相对于水平面的落角。  
□ :下射偏离距离。  
□ :横射偏离距离。

命令

d_zero <real-value>

指定 $\mathrm { D } _ { 0 }$ 的值，范围为 [0..1]。

默认值： 0.5

lethal_area <target-type> <area-value>

指定指定类型目标的致命区域（LA）。此命令应针对该致命性对象适用的所有目标类型重复。

注意： 如果未为目标类型定义致命区域，则假定弹药对目标没有影响。

# 不兼容的命令

以下 weapon_effects 命令与 WSF_CARLTON_LETHALITY 不兼容，使用这些命令将导致输入处理错误：

▫ intercept_pk   
▫ launch_pk   
▫ use_launch_pk

# 使用注意事项

□ 间接火力：卡尔顿模型特别适用于间接火力场景，其中不依赖于武器和目标之间的直接视线。  
□ 目标类型：确保为所有相关目标类型定义致命区域，以确保模型的有效性。

# 3.8.6.4. 匹配杀伤模型 WSF_ENGAGE_LAUNCH_PK_TABLE_LETHALITY

```txt
weapon_effects <name> WSF_ENGAGE-LaUNCH_PK_TABLE_LETHALITY  
weapon_effects Commands ...  
pk_tables_path <directory>  
default_pk <pk-value>  
file_filter <string>  
endweapon_effects 
```

WSF_ENGAGE_LAUNCH_PK_TABLE_LETHALITY 使用在 Pk 表文件中定义的击杀概率（Pk）表查找来计算致命性。Pk 表文件指定发射平台类型和目标平台类型。对于每个发射/目标平台类型对，Pk 查找是目标高度和速度的函数，以及武器发射时的目标横向和纵向距离。

# Pk 表文件格式

每个文件必须具有预定义格式，包含以下内容：

□ 发射平台类型（launcher）  
□ 目标平台类型  
□ 长度测量单位  
□ 速度测量单位  
□ 目标高度

□ 目标速度  
▫ Pk 表：目标横向距离在 X 轴（列）上指定，目标纵向距离在 Y 轴（行）上指定

重要提示：每个武器/目标配对至少需要 2 个 Pk 表文件，至少在两个文件中定义 1 个高度和 2 个速度。尝试使用单个 Pk 表文件或使用无效表输入的 Pk 表文件时，将发出警告。

命令

pk_tables_path <directory>

指定 Pk 表文件的路径。可以是相对路径或绝对路径。

default_pk <pk-value>

当给定的发射器和目标平台类型没有 Pk 表查找时，在武器交战中使用的默认常数 Pk值。

默认值： 0.0

file_filter <string>

在递归扫描 pk_tables_path 目录以查找 Pk 表文件时使用的过滤器。任何名称与过滤器匹配的文件将被加载。建议使用通配符 ‘*’（例如 *.* 或 *.pk*），如果过滤器包含空格字符，可以用引号括起来。

默认值： *（通配符匹配所有文件）

使用注意事项

表文件生成：可以使用 AFSIM 交战工具通过 Pk 表生成命令创建 Pk 表文件。

默认 Pk 值：在没有可用的 Pk 表查找时，使用 default_pk 指定的值。

不兼容的命令：以下命令与 WSF_ENGAGE_LAUNCH_PK_TABLE_LETHALITY 不兼容，使用这些命令将导致输入处理错误：

```txt
intercept_pk launch_pk use_intercept_pk 
```

这种致命性模型适用于需要精确计算武器对目标影响的场景，尤其是在复杂的战场环境中。

# 3.8.6.5. 大气层外杀伤模型 WSF_EXOATMOSPHERIC_LETHALITY

```txt
weapon_effects <name> WSF_EXOATMOSPHERIC_LETHALITY ... weapon_effects Commands ... ... WSF_EXPLICIT_WEapon_EFFECTS Commands ... ... WSF_EXOATMOSPHERIC_LETHALITY Commands ... endweapon_effects 
```

WSF_EXOATMOSPHERIC_LETHALITY 使用击杀概率（Pk）与撞击速度和/或撞击角度的关系来计算致命性。如果缺少撞击速度或撞击角度的 Pk 表，则假定该特定贡献为 1.0，剩余的贡献是唯一的效果。表格进行插值，但不超出指定端点进行外推。

命令

impact_angle_and_pk <angle-value> <pk-value>

在 Pk 与撞击角度插值表中指定一个条目。可以输入任意数量的条目。约束范围为 0 到180 度。

impact_velocity_and_pk <speed-value> <pk-value>

在 Pk 与撞击速度插值表中指定一个条目。可以输入任意数量的条目。撞击速度必须大于零。

不兼容的命令

以下 weapon_effects 命令与 WSF_EXOATMOSPHERIC_LETHALITY 不兼容，使用这些命令将导致输入处理错误：

□ intercept_pk   
▫ launch_pk   
□ use_launch_pk

使用注意事项

插值而非外推：Pk 表进行插值计算，但不超出表格的端点进行外推，因此确保表格覆盖所需的撞击速度和角度范围。

独立变量缺失处理：如果缺少某个独立变量的 Pk 表，则假定该变量的贡献为 1.0，确保至少一个变量有有效的 Pk 表。

这种致命性模型适用于需要考虑撞击速度和角度对目标影响的场景，尤其是在大气层外的交战环境中。

# 3.8.6.6. 渐进式杀伤模型 WSF_GRADUATED_LETHALITY

```txt
weapon_effects <name> WSF_GRADUATED_LETHALITY ... weapon_effects Commands ... ... WSF_EXPLICIT_WEapon_EFFECTS Commands ... discrete | interpolated use_3d_radius | use_2d_radius # Single table format (a single table for all target types) radius_and_PK | pk_and_radius ... ... repeat as necessary ... radius_and_PK | pk_and_radius ... # Multiple tables (target-type specific tables) target_type <target-type-1> radius_and_PK | pk_and_radius ... 
```

```txt
...repeat as necessary ... radius_and(pk|pk_and_radius... [end_target_type]   
...   
target_type <target-type-n> radius_and(pk|pk_and_radius... ...repeat as necessary ... radius_and(pk|pk_and_radius... [end_target_type]   
endweapon_effects 
```

WSF_GRADUATED_LETHALITY 使用击杀概率（Pk）与偏差距离的表查找来计算致命性。表查找可以是插值的或非插值的，并且可以使用二维（仅考虑水平偏差距离）或三维偏差距离。

# 功能特性

目标类型特定表：可以定义特定目标类型的表，以反映对某些类型目标的有效性。当发生交战时，模型将选择第一个与目标平台继承层次结构中的任何平台类型匹配的<target-type> 表。例如，如果平台类型 F-18E 和 F-18F 派生自一个共同的 F-18 平台类型，则会考虑 F-18 的 target_type 表。如果找不到特定目标类型的表，则使用默认表（见target_type）。即使默认表首先定义，它也总是最后一个被考虑的。

命令

discrete / interpolated

指定一个标志，表示 Pk 是在两个同心环之间插值还是从一个边界到另一个边界保持不变。

默认值： discrete

use_3d_radius / use_2d_radius

偏差距离计算为武器和目标之间的斜距或水平距离。

默认值： use_3d_radius

target_type <target_type>

引入一组与指定目标类型相关的半径和 Pk 值。所有后续的 radius_and_pk 和pk_and_radius 命令，直到下一个不定义半径/Pk 对的命令为止，都是表的一部分。可以使用可选的 end_target_type 命令显式终止块。

注意： 对于平台类型没有匹配 target_type 块的目标，应使用 DEFAULT、default 或WSF_PLATFORM 作为 <target_type>。

radius_and_pk <length-value> <pk-value>   
pk_and_radius <pk-value> <length-value>

在当前 Pk 与偏差距离表中指定一个条目。

不兼容的命令

以下 weapon_effects 命令与 WSF_GRADUATED_LETHALITY 不兼容，使用这些命令将导致输入处理错误：

```txt
intercept_pk launch_pk use_intercept_pk use_launch_pk 
```

使用注意事项

表查找：确保表格覆盖所需的偏差距离范围，以便在交战中准确计算 Pk。

目标类型匹配：定义特定目标类型的表，以提高模型的准确性和有效性。

这种致命性模型适用于需要根据偏差距离精确计算武器对目标影响的场景，尤其是在复杂的战场环境中。

# 3.8.6.7. 高能激光武器杀伤模型 WSF_HEL_LETHALITY

```txt
weapon_effects <name> WSF_HEL_LETHALITY  
weapon_effects Commands ...  
WSF_EXPLICIT_WEAPON_EFFECTS Commands ...  
region <platform_type> <region_name>  
Commands  
end_region  
target_type <platform type >  
Commands  
end_target_type  
category <category name>  
Commands  
end_category  
manage_kills ...  
end weapon_effects 
```

WSF_HEL_LETHALITY 是一种专门的致命性模型，基于高能激光（HEL）武器（如WSF_LASER_WEAPON 或 WSF_CUED_LASER_WEAPON）的能量沉积来施加伤害。致命性可以根据区域、目标类型或类别指定。区域是平台上的特定区域，目前仅在引用目标上的交叉网格中定义的致命区域时有意义。platform_type 定义适用于给定类型的所有目标。类别定义适用于所有标记有给定类别的目标。

命令

region <platform_type> <region_name>

定义特定平台类型和区域名称的命令块。

target_type <platform_type>

定义特定目标类型的命令块。

category <category_name>

定义特定类别的命令块。

damage_radius <length-value>

指定光束有效的半径。如果小于光束尺寸，则仅使用圆形区域内的光束部分进行致命性计算。如果大于光束尺寸，则使用整个光束。如果指定，损伤半径表示的区域将用于能量密度计算。如果未指定，则在能量密度计算中使用整个光束尺寸。

默认值： 未指定（使用光束尺寸）

minimum_energy <energy-value>

指定对目标施加致命性所需的最小能量沉积。

minimum_energy_density <fluence-value>

指定对目标施加致命性所需的最小能量密度（以 $\mathsf { j } / \mathsf { c } \mathsf { m } ^ { 2 }$ 或等效单位）。

pk_energy_table table

定义击杀概率与阈值能量的表。表格格式如下：

```txt
*number-of-rows*
* p-k_1 energy-threshold_1*
* p-k_2 energy-threshold_2*
...
* p-k_n energy-threshold_n* 
```

示例：

```txt
pk_energy_table 5 0.1 1 kj 0.3 2 kj 0.5 3 kj 0.7 4 kj 0.9 5 kj end(pk_energy_table 
```

能量阈值应按递增顺序列出。在交战期间，每个 firing_update_interval 后进行一次 Pk抽取。参考 Pk 值将根据当前累积能量沉积在目标上的情况从表中插值。如果抽取值小于参考值，则处理致命性效果。

manage_kills <boolean-value>

指示模拟是否可以杀死和移除平台。对于基于 API 的模拟，应禁用此功能，否则应启用。

默认值： true

# 不兼容的命令

以下 weapon_effects 命令与 WSF_HEL_LETHALITY 不兼容，使用这些命令将导致输入处理错误：

```txt
intercept_pk launch_pk use_intercept_pk use_launch_pk 
```

# 使用注意事项

自定义效果：要在目标区域上定义自定义脚本效果，可以实现 on_target_damaged 或on_target_killed。  
能量密度计算：确保正确设置 damage_radius 和 minimum_energy_density 以准确计算致命性。

这种致命性模型适用于需要精确控制能量沉积和目标影响的场景，尤其是在使用高能激光武器的情况下。

# 3.8.6.8. 飞行武器杀伤模型 WSF_MOBILITY_AND_FIREPOWER_LETHALITY

```txt
weapon_effects <name> WSFMobility_AND_FIREPOWER_LETHALITY  
weapon_effects Commands ...  
WSF_EXPLICIT_WEapon_EFFECTS Commands ...  
... WSF Mobility AND FIREPOWER LETHALITY Commands ...  
table <table_name>  
...  
end_table  
target_type <target_type>  
...  
vulnerability <cm_type>  
...  
end_vulnerability  
end_target_type  
endweapon_effects 
```

WSF_MOBILITY_AND_FIREPOWER_LETHALITY 在武器飞行过程中被显式使用，并对目标以及可能的其他临近附带目标造成离散的伤害，具体分类如下：<NoDamage>（无伤害）、Mobility Kill（机动杀伤）、Firepower Kill（火力杀伤）、Combined Mobility and Firepower Kill（综合机动和火力杀伤）、以及 CatastrophicKill（灾难性杀伤）（分别为 MK、FK、MFK 和KK）。模型允许在交战过程中考虑相对目标的硬度，并允许考虑目标为自我保护而使用的对抗措施（CM），这些措施可能部分或完全抵消交战效果。

如上所述，某些目标类型本质上比其他目标更难以损坏。模型允许通过表格块定义零个或多个命名概率表。当没有其他表格被明确应用时，总是使用一个名为“default”的表格。用户可以提供这个“default”表格，如果没有提供，系统将创建一个（具有其内部默认值）。

模型允许将不同的致命性表格应用于特定的<target-type>，使用零个或多个 target_type块。特定目标类型的概率集合通过 table_name 命令集体分配给该目标类型。如果定义的弹药没有明确提供适用于<target-type>的致命性，则使用“default”目标类型。与表格规范一样，有一个特殊的“default” target_type 块，如果用户没有提供，系统将提供。至少，每个target_type 块通常会包含一个 table_name 规范，否则将使用“default”表格。

在 WSF_WEAPON_FUSE 明确武器弹药飞行终止时，检查与目标平台的失误距离。如果失误距离小于定义的最大致命半径，则进行随机均匀抽取。如果抽取值超过 Pmk_damage 阈值，则弹药对目标造成了一定的伤害。根据超过阈值的抽取部分，与“kill-thermometer”进行比较，较大的抽取值会对威胁造成更大的伤害，如上所述。请注意，只有在最近通过失误距离小于 WSF_EXPLICIT_WEAPON_EFFECTS 的‘maximum_radius’设置时才进行抽取。

还要注意，在第一次武器撞击之后，对同一目标的多次武器撞击可能会对目标造成累加伤害，但不保证如此。每次武器撞击都是单独考虑的，不考虑现有的目标损伤。

Mobility Kill (MK) 对移动者施加完全伤害（平台部件 DamageFactor $= 1 . 0$ ，或总伤害），并且根据实现，可能导致运动瘫痪。目前，并非所有 WSF 移动类型都响应此伤害设置。瘫痪效果已对属于“Land”域的航点移动者实现。  
Firepower Kill (FK) 对平台上的每个武器施加完全伤害（平台部件 DamageFactor $= 1 . 0$ ，或总伤害）。目前，并非所有 WSF 武器类型都响应此伤害设置。如果受到此类伤害，则不允许任何 WSF_EXPLICIT_WEAPON 类型发射武器。  
CatastrophicKill(KK) 对平台的所有方面及其所有附加部件施加完全伤害，即平台死亡，通常是移除死亡平台。

```txt
Probability Definitions (either of two keywords below are accepted):  
probability_of_damage GIVEN_proximity_hit = Pd_hit = Probability of damage, given a  
proximity hit (default = 0.50)  
probability_of_mk GIVEN DAMAGE = Pmk DAMAGE = Probability of receiving  
only a Mobility Kill, given damage (default = 0.15)  
probability_of_fk GIVEN DAMAGE = Pfk DAMAGE = Probability of receiving only  
a Firepower Kill, given damage (default = 0.15)  
probability_of_kke GIVEN DAMAGE = Pkk DAMAGE = Probability of receiving a  
Catastrophic Kill, given damage (default = 0.50)  
<probability_of_mfk GIVEN DAMAGE> = <Pmfk DAMAGE> = Probability of simultaneous  
M and F Kills, given damage (calculated = 0.20) 
```

概率阈值：上面提到的前四个概率阈值被限定在[0,1]的范围内，默认值如所示。用户可以指定任意或全部值以覆盖默认设置。最后一个概率值不能由用户直接指定，而是通过计算以填充一个均匀概率（MK、FK、MFK 和 KK 的总和将恰好为 1.0）。如果最后四个概率的总和超过 1.0，模型将无法初始化。

武器脆弱性：目前，尚未考虑部署显式对抗措施（CM，作为自我防御机制的显式武器）的目标。例如，干扰弹、箔条，甚至是烟雾弹等遮蔽物。为应对此情况，对于攻击性武器易受影响的每个 CM，可以通过 vulnerability 块指定致命性的降级。此块可以通过以下三种方式之一来降低致命性：a）通过调用一个替代的 alternate_table_name 来替换 table_name 表格，或 b）对 table_name 表格应用一个 pk_factor 降级，或 c）一个 probability_of_weapon_defeat值，移除攻击性武器。虽然选项 a 允许用户更具体地定义，但它仅允许一个 CM 类型对最终致命性产生影响。如果多种 CM 类型同时针对攻击性武器使用，选项 b 的 Pk 降级效果仅在

每个 vulnerability 块中使用 Pk_factor 时才是累积的。对于选项 c，当 CM 被判定为“有效”（详见下段）时，攻击性武器立即从模拟中移除。（原因——CM 通常部署以误导入侵武器偏离其预定目标。此致命性模型从不改变武器的引导方向，但移除入侵武器近似该效果。射手和目标都可以将武器平台的提前消失视作 CM 有效的视觉提示。）

对于 CM 类型定义的每个 vulnerability 块，必须满足最低约束条件才能被认为“有效”并将其效果注入致命性模型。这些约束条件是：a）视场半锥角，b）最小和最大距离限制，以及 c）视场内的最小持续时间。这三个约束条件默认设置为立即通过各自检查的值（ $\mathsf { F O V } = \mathsf { 1 } 8 0$ 度，min $\scriptstyle 1 = 0$ ，max $\left. \right.$ <极大值>，duration ${ \tt = } 0$ 秒）。因此，在 CM 可以注入其效果之前，必须同时满足提供的每个约束条件。例如：“vulnerability FLARE probability_of_weapon_defeat 1.0end_vulnerability”将保证如果在飞行出发时存在一个 FLARE 类型，目标将立即看到发射的入侵武器消失。若在块中添加“minimum_duration $3 . 5 ~ 5 \mathsf { e c } ^ { \prime \prime }$ ，则需要 FLARE 类型在 3.5 秒内持续存在后才变为有效。

模拟中的 CM 会定期评估，以确定它们在前一个时间间隔内是否变得有效。它们只会变得有效一次，并永久保持该状态。模型中的 update_interval 用于确定此评估的计算频率。较小的间隔提供更大的时间粒度，但会增加计算开销。

# 示例输入

```txt
weapon_effects ANTIARMOR_EFFECT WSF Mobility_AND FIREPOWER_LETHALITY
#debug
maximum_radius 30 m # No damage will occur to any platform unless detonation is within this radius.
update_interval 1.0 sec
table default # MUST be the first lethality Table specified.
probability_of_damage GIVEN_proximity_hit 0.50
probability_of_mk GIVEN_damage 0.20
probability_of_fk GIVEN_damage 0.20
probability_of_kke GIVEN_damage 0.80
end_table
table TARGET_TABLE
probability_of_damage GIVEN_proximity_hit 0.55
probability_of_mk GIVEN_damage 0.22
probability_of_fk GIVEN_damage 0.15
probability_of_kke GIVEN_damage 0.60
end_table
table FLARE_DEGRADE_TABLE
probability_of_damage GIVEN_proximity_hit 0.35
probability_of_mk GIVEN_damage 0.20
probability_of_fk GIVEN_damage 0.20
probability_of_kke GIVEN_damage 0.80
end_table
table SMOKE_DEGRADE_TABLE
probability_of_damage GIVEN_proximity_hit 0.30
probability_of_mk GIVEN_damage 0.25 
```

```tcl
probability_of_fk GIVEN DAMAGE 0.25  
probability_of_kk GIVEN DAMAGE 0.50  
end_table  
target_type default #MUST be the first lethality specified,  
#for all target types _not _specified below.  
table_name default #By default, this is "default", if not specified otherwise!  
vulnerability FLARE  
minimum_duration 0.5 sec  
maximum-half_cone_angle 15 deg  
minimum_distance 20 m  
maximum_distance 5000 m  
distance_value missile_to_target  
#alternate_table_name FLARE_DEGRADE_TABLE #Table or Pk_Factor mutually exclusive.  
pk_factor 0.8 #Table or Pk_Factor mutually exclusive.  
probability_ofweapon_defeat 0.15 #This value will short-circuit the two above, and remove the weapon  
end_vulnerability  
vulnerability SMOKE  
minimum_duration 5.0 sec  
minimum_distance 20 m  
maximum_distance 5000 m  
alternate_table_name SMOKE_DEGRADE_TABLE  
end_vulnerability  
end_target_type  
target_type TARGET  
table_name TARGET_TABLE  
vulnerability FLARE  
minimum_duration 1.5 sec  
maximum-half_cone_angle 15 deg  
minimum_distance 50 m  
maximum_distance 5000 m  
alternate_table_name FLARE_DEGRADE_TABLE #Table or Pk_Factor mutually exclusive.  
#pk_factor 0.8 #Table or Pk_Factor mutually exclusive.  
end_vulnerability  
vulnerability SMOKE  
minimum_duration 10.0 sec  
alternate_table_name SMOKE_DEGRADE_TABLE  
minimum_distance 50 m  
maximum_distance 5000 m  
end_vulnerability  
end_target_type 
```

# 表格定义

table <table_name> … end_table：一个命名的‘table’块提供一组四个概率，在给定条件下作为一个集合考虑，并将在其他地方通过名称引用。它计算第五个概率，并确保总概率为 1。

# 表格命令

probability_of_damage_given_proximity_hit <floating-point-value>：指定对目标平台造成伤害的概率阈值。（也允许使用“Pd_hit”作为简写。）例如，值为 0.90 表示有 $90 \%$ 的可能性造成某种伤害，或 10%的可能性不造成伤害。只有当达到伤害阈值时，才会考虑进一步的伤害概率。  
probability_of_mk_given_damage <floating-point-value>：指定平台（如果受损）仅遭受机动杀伤的概率。（也允许使用“Pmk_damage”作为简写。）  
probability_of_fk_given_damage <floating-point-value>：指定平台（如果受损）仅遭受火力杀伤的概率。（也允许使用“Pfk_damage”作为简写。）  
probability_of_kk_given_damage <floating-point-value>：指定目标平台（如果受损）遭受灾难性杀伤的概率。（也允许使用“Pkk_damage”作为简写。）

# 脆弱性定义

vulnerability <cm-type> … end_vulnerability：一个‘vulnerability’块指定如果攻击性武器遇到目标为自我保护而使用的<cm-type>类型的对抗措施（CM），对其造成的降级效果。此块作为 target_type 块中的子命令接受。

# 脆弱性命令

minimum_duration <TimeValue>：指定 CM 必须存在的最短时间，以对入侵攻击性武器产生影响。默认值为 0.0，即立即生效。  
maximum_half_cone_angle <angle-value>：指定仍被视为潜在有效 CM 的最大视场角。这是从弹药到 CM 的视线与弹药到目标的视线之间的 3D 角度。默认值为 180 度，即始终可见。  
minimum_distance <length-value>：指定仍被视为潜在有效 CM 的最小距离。测量由distance_value 设置决定。默认值为 0。  
maximum_distance <length-value>：指定仍被视为潜在有效 CM 的最大距离。测量由distance_value 设置决定。默认值为<极大值>。  
distance_value <string>：指定用于距离约束的距离测量类型。可能的值包括：“missile_to_target”、“countermeasure_to_target”或“missile_to_countermeasure”。默认值为“missile_to_target”。  
alternate_table_name <string>：指定在此 CM 被认为“有效”时将替换 table_name 的表格名称。CM 在同时通过距离、半锥角和持续时间测试时被视为“有效”。  
probability_of_weapon_defeat <floating-point-value>：指定给定 CM 类型将诱导弹药的概率。CM 必须首先通过上述“有效”标准。如果此值非零，将对每个此类型 CM 实例进行一次随机抽取。如果随机抽取成功，攻击性弹药不会被偏转，而是立即从模拟中移除。限制在[0.0, 1.0]。默认值为 0.0。

# 目标类型定义

target_type <target_type> … end_target_type：一个‘target_type’块提供仅用于特定目标类型交战的概率。它应包含一个要使用的 table_name 和零个或多个 vulnerability 块。

# 目标类型命令

table_name<string>：指定针对给定目标类型的交战中要引用的概率表格名称。表格值将在 target_type 块范围之外定义。默认值为“default”。  
vulnerability <string> … end_vulnerability

# 命令

update_interval <TimeValue>：指定对抗措施状态评估之间的间隔，计算它们何时可以被视为“有效”。默认值为 1.0 秒。

# 3.8.6.9. 距离杀伤模型 WSF_SPHERICAL_LETHALITY

```txt
weapon_effects <name> WSF_SPHERICAL_LETHALITY  
weapon_effects Commands ...  
WSF_EXPLICIT_WEapon_EFFECTS Commands ...  
... WSF_SPHERICAL_LETHALITY Commands ...  
# Pk Table  
use_pk_table <string-value>  
pk_table ... end_pk_table  
endweapon_effects 
```

球形杀伤力指的是一种基于球形范围内的伤害计算模型，用于评估武器在爆炸或其他作用下对目标造成的伤害。基于以下算法：

$$
D = D _ {m a x} - \left[ (D _ {m a x} - D _ {m i n}) \times \left(\frac {R - R _ {m i n}}{R _ {m a x} - R _ {m i n}}\right) ^ {\frac {1}{X}} \right]
$$

其中：

：从爆炸位置到目标平台的斜距。  
$ \mathrm { { R } } _ { \mathrm { m i n } }$ ：施加伤害的最小距离。  
$\mathrm { R } _ { \mathrm { m a x } }$ ：施加伤害的最大距离。  
$ { \mathrm { D } } _ { \mathrm { m i n } }$ ：当 $\mathtt { R } = \mathtt { R } _ { \operatorname* { m a x } }$ 时施加的伤害。  
$\mathrm { D } _ { \mathrm { m a x } }$ ：当 $\mathtt { R } = \mathtt { R } _ { \operatorname* { m i n } }$ 时施加的伤害。  
X: 指定伤害衰减率的指数。

□ $\Chi = 1$ 线性衰减。  
$\Chi > 1$ 较慢的衰减。  
□ $\Chi < 1$ 较快的衰减。

伤害计算规则：

如果 $\mathrm { R } > \mathrm { R } _ { \operatorname* { m a x } }$ ，则不施加伤害。

□ 如果 $ { \mathrm { R } } <  { \mathrm { R } } _ { \mathrm { m i n } }$ ，则施加伤害最大伤害 $\mathrm { D } _ { \mathrm { m a x } }$   
如果在 $ \mathrm { { R } } _ { \mathrm { m i n } }$ 和 $\mathrm { R } _ { \mathrm { m a x } }$ 之间，伤害根据上述公式计算。

计算出的伤害因子将添加到目标平台的当前伤害因子中。如果更新后的值大于或等于1.0，则目标平台将被击毁。

# 半径和伤害参数

minimum_radius <length-value>：指定伤害方程中的 R min 值。注意：此值必须小于maximum_radius 的值。  
maximum_radius <length-value>：指定伤害方程中的 R max 值。注意：此值必须大于minimum_radius 的值。  
minimum_damage <value>：指定伤害方程中的 D min 值。注意：此值必须在 [0..1] 范围内，并且必须小于 maximum_damage 的值。默认值为 0.0。  
maximum_damage <value>：指定伤害方程中的 D max 值。注意：此值必须在 [0..1] 范围内，并且必须大于 minimum_damage 的值。默认值为 1.0。  
exponent<value>：指定上述方程中的 X 值。注意：值必须大于零。值为 1.0 表示线性衰减。默认值为 1.0。  
threshold_damage<value>：如果目标平台从未受损，则这是爆炸必须达到的伤害因子阈值，才能造成任何伤害。注意：此值必须在 [0..1] 范围内，并且必须小于maximum_damage 的值。值为 0.0 将立即施加伤害。默认值为 0.0。

# Pk 表格

use_pk_table <string-value>：设置在武器引信时评估的 Pk 表格名称，以计算拦截 Pk 的阈值。在平台初始化时，PkTable Manager 必须知道此表格名称以提供给武器。表格将覆盖为 intercept_pk 提供的任何值。  
pk_table … end_pk_table：以下是使用 use_pk_table 选项指定 PkTable 的示例输入。pk_table…end_pk_table 块 必 须 出 现 在 全 局 上 下 文 中 （ 因 为 所 有 表 格 都 由PkTableManager 读取，并通过引用提供给武器），或嵌套在 weapon_effects 块中。武器必须通过使用 use_pk_table 选项请求使用该表格。pk_table 块中列出的一个或多个表格与 target_type 相关联。表格查找的自变量（如果不是常数 Pk 值）将包括：目标方位角、目标仰角、武器速度和目标速度。第一个列出的 target_type 必须是 DEFAULT，如果没有更具体的匹配，则使用 DEFAULT 选项下提供的值。PkTables 可以指定为inline_tables，并且“inline_table”关键字后面总是跟着两个整数，分别是方位角的数量（从零开始，因为假设 Pk 关于武器的 XZ 平面对称）和仰角的数量（不假设对称）按递增顺序排列。然后，内联表格将包含 nXm 个 Pk 值，供武器作为 Pk 阈值进行插值。如果均匀随机抽取小于阈值，则判定为 1.0（完全击杀）。

```txt
pk_table PkTableName  
target_type DEFAULT  
constant 0.1  
end_target_type  
target_type FLANKER  
weapon_speed 21 m/s # lower_bound  
target_speed 22 m/s 
```

```txt
inline_table25 -90 -45 0 45 90 0 0.81 0.81 0.81 0.85 0.81 180 0.81 0.81 0.81 0.84 0.81   
end_target_speed   
target_speed33m/s   
inline_table33 -90 0 90 0 0.81 0.81 0.81 90 0.81 0.81 0.81 180 0.81 0.81 0.81   
end_target_speed   
endweapon_speed   
weapon_speed34m/s #upper_bound target_speed25m/s inline_table25 -90 -45 0 45 90 0 0.81 0.81 0.81 0.85 0.81 180 0.81 0.81 0.81 0.84 0.81   
end_target_speed   
target_speed36m/s inline_table25 -90 -45 0 45 90 0 0.81 0.81 0.81 0.85 0.81 180 0.81 0.81 0.81 0.84 0.81   
end_target_speed   
endweapon_speed   
end_target_type   
end_pk_table 
```

3.8.6.10.圆概率伤杀模型 WSF_TABULATED_LETHALITY  
```c
weapon_effects <name> WSF_TABLEATED_LETHALITY  
weapon_effects Commands ...  
WSF_EXPLICIT_WEapon_EFFECTS Commands ...  
circular_errorprobable <length-value>  
target_type  
pk_at_cep <pk-value> <length-value>  
endweapon_effects 
```

WSF_TABULATED_LETHALITY 是一种基于杀伤概率（Pk）与圆概率误差（CEP）之间的线性插值方法。对于每种目标平台类型，插值方法可能不同。

命令与参数

circular_error_probable <length-value>：此值指定武器在标准约束条件下使用时的 $50 \%$ 分位数固有名义精度。它可以用于确定最终目标偏移或失误距离。圆概率误差（CEP）是指以目标点为中心的圆的半径，预计 $50 \%$ 的弹着点会落在该圆内。  
target_type：指示以下 Pk 表格适用的目标平台类型。可以为不同的预期目标平台类型指定任意数量的表格。  
pk_at_cep <pk-value> <length-value>：在 Pk 与 CEP 表格中指定一个条目。可以为每种目标平台类型提供多个点。

# 注意事项

不兼容命令：以下命令与 WSF_TABULATED_LETHALITY 不兼容，使用这些命令将导致输入处理错误：

```txt
intercept(pk launch(pk use_launchPK 
```

WSF_TABULATED_LETHALITY 通过考虑不同目标平台类型的特定 Pk 与 CEP 关系，提供了一种灵活的方式来评估武器的致命性。通过为每种目标类型定义不同的表格，可以更准确地模拟武器在不同条件下的性能。

# 3.8.7. 发射计算模型 launch_computer

```txt
launch_computer <name> <base-type>
    debug
    noDebug
    ... WSF-LaUNCH_COMPUTER Commands ...
end_launch_computer 
```

launch_computer 命令用于定义一种发射计算机类型，该类型可以被武器用来决定特定武器与目标交战的条件是否有利，并在有利的情况下提供一些指导武器使用的信息。

在综合战斗中，当许多资源可能被用来打击同一目标时，一个关键考虑因素是估计给定资源可以多快打击目标。因此，每种类型的发射计算机必须提供的主要功能是估计拦截目标轨迹的时间。如果交战条件完全不利，则返回一个巨大的值，表明不建议进行交战。然后由战斗管理器智能地选择那些提供可接受的快速拦截时间和可接受成功概率的资源。

注意：这可能应该被称为“weapon_computer”或“weapon_engagement_computer”，因为“launch_computer”暗示了一个发射实体的存在。这对于定向能武器等情况并不适用。命令

launch_computer <name> <base-type>：定义一个新的发射计算机。

□ <name>：要创建的新发射计算机的名称。  
□ <base-type>：现有用户定义的发射计算机类型、WSF_LAUNCH_COMPUTER 或预定义发射计算机类型之一，其定义将构成新类型的初始定义。

debug：在运行时启用调试输出。  
no_debug：在运行时禁用调试输出。

这个工具通过提供时间估算和条件评估，帮助在复杂的战斗环境中优化资源分配和武器

使用策略。

# 3.8.7.1. 通用发射计算模型 WSF_LAUNCH_COMPUTER

```txt
launch_computer <name> WSF-LaUNCH COMPUTER
... launch_computer Commands ...
... WSF-LaUNCH_COMPUTER Commands ...
end_launch_computer 
```

WSF_LAUNCH_COMPUTER 用于确定是否可以有效地将 WSF 武器发射到目标轨迹上，并提供武器拦截目标轨迹位置的预计时间。这种类型是发射计算机的最通用实现，适用于早期概念研究。它接受多个交战约束，并在响应查询时，指示交战条件是否在约束范围内。如果无法实现拦截，基础类将返回一个巨大的时间值（表示永远）。在计算非巨大值的拦截时间之前，必须满足以下提供的每个约束值。

对于地对空导弹（SAM）系统，可以从推力持续时间、燃尽速度、滑行持续时间、最小终端速度中推导出估计的速度剖面，用于拦截时间计算。

# 命令

maximum_delta_altitude <altitude-value> / minimum_delta_altitude <altitude-value>：指定 目标与武器之间的最小和最大高度差。（目标高于发射高度为正差值。）   
maximum_closing_speed <speed-value> / minimum_closing_speed <speed-value>：指定武器可以交战的最小和最大接近速度。（发射器到目标距离减小为正接近速度。）  
maximum_opening_speed <speed-value> / minimum_opening_speed <speed-value>：指定武器可以交战的最小和最大远离速度。（发射器到目标距离增加为正远离速度。）  
注意：这些值不是目标的速度值，而是有效的“多普勒”速度。  
maximum_slant_range <range-value> / minimum_slant_range <range-value>：指定武器可以交战的最小和最大目标范围。  
maximum_time_of_flight <time-value>：指定武器的最大允许飞行时间。  
maximum_boresight_angle <angle-value>：指定武器的最大离轴角能力。  
thrust_duration <time-value>：SAM 系统导弹推力持续时间。  
coast_duration <time-value>：SAM 系统导弹滑行持续时间。  
burnout_speed <speed-value>：SAM 系统导弹燃尽速度。  
minimum_terminal_speed <speed-value>：SAM 在仍具有足够终端机动能力时的最低速度。

这些命令和参数帮助定义了武器在不同交战条件下的有效性和性能，确保在复杂的战斗环境中能够做出最佳决策。

# 3.8.7.2. 空空发射计算模型 WSF_AIR_TO_AIR_LAUNCH_COMPUTER

```txt
launch_computer <name> WSF_AIR_TO_AIR-LaUNCH COMPUTER ... launch_computer Commands ... ... WSF-LaUNCH_COMPUTER Commands ... load_table ... 
```

WSF_AIR_TO_AIR_LAUNCH_COMPUTER 实现了一种用于空对空导弹的发射计算机。该计算机接受目标轨迹，并评估哪个表格化的交战条件最接近轨迹参数。它提供预期的（范围和飞行时间），用于发射逻辑。

空对空导弹设计有优选的使用范围：短程、中程或远程。无论如何，所有导弹都有一个最小范围，低于此范围它们无法正确武装和引导拦截；一个最大范围，超出此范围它们无法成功拦截；以及一个最大致命性的“无逃逸”范围。最小和最大范围通常假设目标是水平且不机动的。“无逃逸”范围介于最小和最大之间，假设目标具有一定的代表性能力（如 G 负载）来转身并逃离导弹。在无逃逸范围内，目标逃脱的概率很低。

# 操作方法

交战结果是 6 个独立变量（IVs）的函数：射手高度和马赫数、目标高度和马赫数、目标方位角（正面 $\scriptstyle = 0$ 度）和目标引导角。以及 6个依赖变量（DVs）：最大范围和飞行时间、无逃逸范围和飞行时间、最小范围和飞行时间。

数据表可能非常大。为了让许多发射计算机实例共享公共数据表，输入处理主要用于读取交战结果表，所有此类计算机将共同引用该表。该表用于对目标 WsfTrack 发射WSF_EXPLICIT_WEAPON 的时机。轨迹必须具有有效的 WCS 位置和速度。

结果通过首先获取每个 IV并找到数据表中最近的条目来找到。然后，一旦确定了每个IV的索引，这组索引用于查找结果。换句话说，结果不是插值值。

□ 目标方位角：在水平面上从目标的速度矢量到射手视线矢量测量，值从 0 到 180度。这意味着正面 ${ \tt = } 0$ 度目标方位角！  
▫ 目标引导角：也在水平面上测量，从射手速度矢量到目标视线（类似于方位角），但如果目标横向收敛到射手速度矢量则为正，如果远离则为负。

weapon_tools 应用程序协助创建此类发射计算机。（参见：3.8.8.1 空空发射计算模型产生工具 AIR_TO_AIR_LAUNCH_COMPUTER_GENERATOR）。

# 命令

load_table <file-name> ： 指 定 要 包 含 的 单 独 文 件 。 此 包 含 文 件 必 须 包 含launch_computer_table 块。  
launch_computer_table … end_launch_computer_table：指定武器交战预期结果的数据表。此块可以内联包含在发射计算机块中，不需要像上面的 load_table 那样在单独的文件中。所有列出的子命令输入都要嵌入在此块中。

□ no_escape_manuever <acceleration-value>：用于定义目标“转身逃避导弹”规避战术能力的加速度。从导弹发射开始。  
□ independent_variables … end_independent_variables：此块包含定义交战每个独立变量有效范围的数据。每个 IV 必须按递增值给出。

shooter_altitudes <distances> end_shooter_altitudes：指定射手高度。可以不均匀，但必须按递增数值顺序。（最小增量 $= 1 0 0 . 0$ 米）  
shooter_machs <values> end_shooter_machs：指定射手马赫数。可以不均匀，

但必须按递增数值顺序。（最小增量 $= 0 . 0 5$ ）

target_altitudes <distances> end_target_altitudes：指定目标高度。可以不均匀，但必须按递增数值顺序。（最小增量 $= 1 0 0 . 0$ 米）  
target_machs <values> end_target_machs：指定目标马赫数。可以不均匀，但必须按递增数值顺序。（最小增量 $_ { = 0 . 0 5 }$ ）  
target_aspect_angles <angles> end_target_aspect_angles：指定目标方位角（正面 $\scriptstyle = 0$ 度）。可以不均匀，但必须按递增数值顺序。（最小增量 $\mathtt { \Omega } = 2 . 0$ 度）  
target_lead_angles <angles> end_target_lead_angles：指定目标引导角。可以不均匀，但必须按递增数值顺序。（最小增量 ${ \tt = } 2 . 0$ 度）  
target_lead_angle_limits from <angle-value> to <angle-value> by <angle-value>：使用简化符号指定目标引导角。这是前一个 target_lead_angles 命令的替代。（最小增量 ${ \bf \bar { \Lambda } } = 2 . 0$ 度）

▫ intercept_results … end_intercept_results：此块包含定义拦截包络的所有数据点。必须有与交战条件一样多的条目/行（参见 independent_variables）。任何值为-1.0表示不可实现。建议使用名为 weapon_tools 的 LAR 生成器工具生成此数据。

数据格式为：  
```txt
intercept_results  
Rmin <length-value> <time-value> Rne <length-value> <time-value> Rmax <length-value> <time-value>  
Rmin <length-value> <time-value> Rne <length-value> <time-value> Rmax <length-value> <time-value>  
...  
Rmin <length-value> <time-value> Rne <length-value> <time-value> Rmax <length-value> <time-value>  
end_intercept_results 
```

Rmin <length-value> <time-value>：此条件的最小范围和飞行时间，低于此范围拦截不成功。  
Rne <length-value> <time-value>：此条件的无逃逸范围和飞行时间。  
Rmax <length-value> <time-value>：此条件的最大范围和飞行时间，超出此范围拦截不成功。

这些命令和参数帮助定义了空对空导弹在不同交战条件下的有效性和性能，确保在复杂的空战环境中能够做出最佳决策。

示例  
```txt
launch_computer airToAirComputer WSF_AIR_TO_AIR_COMPUTER launch_computer_table noescape_mechanver 7 g independent_variables shooter_altitudes 10000 ft 20000 ft 30000 ft end_shooter_altitudes shooter_machs 0.8 1 1.2 1.4 1.6 1.8 2 end_shooter_machs target_altitudes 10000 ft 20000 ft 30000 ft end_target_altitudes 
```

```txt
target_machs 0.8 1 1.2 1.4 1.6 1.8 2 end_target_machs  
target Aspect angles 0 deg 60 deg 120 deg 180 deg end_target Aspect angles  
target Lead angles 0 deg 60 deg 90 deg 120 deg 180 deg end_target Lead angles  
end_independent_variables  
intercept_results  
# Shooter Alt=10000 ft, M=0.8, Tgt Alt=10000 ft, M=0.8, Aspect = 0 deg  
Rmin 1096.54 m 1.90483 s Rne 7237.79 m 17.35 s Rmax 15904 m 20.4 s # Lead = 0 deg  
Rmin 4829.64 m 12.7495 s Rne -1 m -1 s Rmax -1 m -1 s # Lead = 60 deg  
Rmin 5003.26 m 9.83513 s Rne -1 m -1 s Rmax -1 m -1 s # Lead = 90 deg  
Rmin 4208.14 m 7.21605 s Rne 5809.84 m 16.9783 s Rmax -1 m -1 s # Lead = 120 deg  
Rmin 1096.54 m 1.90482 s Rne 7284.14 m 17.4125 s Rmax 15904 m 20.4 s # Lead = 180 deg  
# INCOMPLETE EXAMPLE ... Total Conditions = 3 X 7 X 3 X 7 X 4 X 5 = 8820 lines needed.  
end_intercept_results  
end_launch_computer_table  
end_launch_computer 
```

示例 2 使用文件输入

```txt
launch_computer airToAirComputer2 WSF_AIR_TO_AIR COMPUTER
#Pointed to file must contain the launch_computer_table ... end_launch_computer_table
block.
load_table launch_computer_table_data.txt
end_launch_computer 
```

# 3.8.7.3. 空空发射计算模型 WSF_ATA_LAUNCH_COMPUTER（旧）

```txt
launch_computer <name> WSF_ATA-LaUNCH COMPUTER  
... launch_computer Commands ...  
... WSF-LaUNCH_COMPUTER Commands ...  
... WSF_ATA-LaUNCH_COMPUTER Commands ...  
end-Launch_computer 
```

概述

WSF_ATA_LAUNCH_COMPUTER 实现了一个用于空对空导弹的发射计算机。（此类型已被 弃 用 ， 建 议 使 用 WSF_AIR_TO_AIR_LAUNCH_COMPUTER 。 ） 导 弹 可 能 具 有 在 发 射WSF_EXPLICIT_WEAPON 之前必须满足的各种交战约束。

一 个 weapon_tool 已 被 开 发 用 于 协 助 创建此类 型的发 射计算 机。请 参阅AIR_TO_AIR_LAUNCH_COMPUTER_GENERATOR。

命令

intercept_results … end_intercept_results: 此块包含定义拦截包线的数据。建议使用 LAR

生成器武器工具生成此数据。

# 子命令:

number_of_aspect_angle_bins <number>: 指定拦截包线中的方位角角度区间数。方位角覆盖范围为 0 到 180 度。假设方位角对称。  
azimuth_bin_count_end_limit <number> <angle>: 类似于 number_of_aspect_angle_bins，但将方位角覆盖限制为指定值。  
elevation_bin_count_min_and_max_limits <number> <min-angle> <max-angle>: 指定拦截 包线中在指定最小和最大角度之间的仰角区间数。   
range_rate_bin_count_min_and_max_limits <number> <min-range-rate> <max-range-rate>:指定拦截包线中在指定最小和最大速率之间的距离速率（即闭合速度）区间数。  
firing_range_bin_count_and_values <number> <range1> <range2> … <rangen>: 指定发射范围区间数及其在拦截包线中的对应范围。  
time_of_flight_values … end_time_of_flight_values: 拦截包线（飞行时间值序列）用于上述指定的 $( \mathsf { m } \times \mathsf { n } \times \mathsf { p } \times \mathsf { q } \times \mathsf { r } )$ 矩形矩阵的交战参数。任何给定为 0.0 的飞行时间表示在这些条件下无法拦截。  
generate_rectangular_results … end_generate_rectangular_results: 此块由离线 LAR 生成器工具用于生成 intercept_results 块。称为“矩形”是因为 weapon_tool 系统地（即通过“蛮力”）为 $( \mathsf { m } \times \mathsf { n } \times \mathsf { p } \times \mathsf { q } \times \mathsf { r } )$ 矩形矩阵中的每组交战条件计算飞行时间结果。任何0.0 的飞行时间值表示无法拦截；表中可能有许多零值。

# 子命令:

aspect_angle_bin_count <number>: 指定用于生成拦截包线的方位角区间数。  
azimuth_bin_count <number>: 指定用于生成拦截包线的方位区间数。默认值:4  
azimuth_limit <angle>: 指定用于生成拦截包线的最大方位角。默认值: 90.0 度  
elevation_bin_count <number>: 指定用于生成拦截包线的仰角区间数。默认值:4  
elevation_lower_limit <angle>: 指定用于生成拦截包线的最小仰角。默认值: -45.0 度  
elevation_upper_limit <angle>: 指定用于生成拦截包线的最大仰角。默认值: 45.0 度  
range_rate_bin_count <number>: 指定用于生成拦截包线的距离速率区间数。默认值:4  
range_rate_lower_limit <range-rate>: 指定用于生成拦截包线的最小距离速率。默认值: -1000.0 英尺/秒  
range_rate_upper_limit <range-rate>: 指定用于生成拦截包线的最大距离速率。默认值: 1000.0 英尺/秒  
range_bin_count <number>: 指定用于生成拦截包线的范围区间数。默认值:4  
minimum_ground_range <range>: 指定用于生成拦截包线的最小范围。默认值: 0.0  
maximum_ground_range <range>: 指定用于生成拦截包线的最大范围。

说明

弃 用 警 告 : WSF_ATA_LAUNCH_COMPUTER 已 被 弃 用 ， 建 议 使 用 更 新 的WSF_AIR_TO_AIR_LAUNCH_COMPUTER。  
拦截包线生成: 使用 LAR 生成器工具来系统地生成拦截包线数据，以确保导弹在各种交战条件下的有效性。

# 3.8.7.4. 空地发射计算模型 WSF_ATG_LAUNCH_COMPUTER

```txt
launch_computer <name> WSF_ATG-LaUNCH COMPUTER  
... launch_computer Commands ...  
... WSF-LaUNCH_COMPUTER Commands ...  
... WSF_ATG-LaUNCH_COMPUTER Commands ...  
end_launch_computer 
```

WSF_ATG_LAUNCH_COMPUTER 实现了一种用于制导空对地武器的发射计算机，该武器在大致水平的飞行中巡航。该对象必须定义一个或多个发射可接受区域（LAR），这些区域是相对于发射飞机位置指定的移动区域形状，规定了武器预期能够击中目标的交战几何和飞行条件。当定义了多个 LAR 时，发射计算机将尝试选择最符合当前交战条件的 LAR。如果当前发射条件与指定的 LAR 交战值不完全匹配，则线性敏感性将尝试调整 LAR 中心以进行补偿。（例如，如果发射速度高于 LAR 定义的发射速度，LAR 将向前调整一定量，以考虑到更快的武器释放将允许武器飞得更远以击中目标。）补偿后，将检查当前跟踪的目标位置是否在调整后的 LAR 内。如果在 LAR 内，则目标位置可以用武器达到，因此可以尝试武器释放。

weapon_tools 应用程序协助创建此类发射计算机。（参见 ：3.8.8.2 空地发射计算模型产生工具 ATG_LAR_AND_LC_GENERATOR ）。

注意：如果定义了多个 LAR，则必须在父武器上指定 update_interval 并且不为零，以便发射计算机具有准确的内部状态。

命令

debug_lars

在运行时启用发射计算机中定义的所有 LAR 的调试输出。

launch_acceptable_region <name> … end_launch_acceptable_region

定义单个 LAR 的调试输出。

delta_altitude <length-value>

发射平台和目标平台之间的高度差。正值表示发射平台高于目标（如空对地交战所期望的）。

launch_speed <speed-value>

发射平台的速度。

sensitivity_range_per_10m_altitude <length-value>

为补偿比标称值高 10 米的高度而应用于 LAR 的额外前向偏移（以米为单位），由delta_altitude 指定。

sensitivity_range_per_10ms_velocity <length-value>

为补偿比标称值高 10 米/秒的发射速度而应用于 LAR 的额外前向偏移（以米为单位），由 launch_speed 指定。

sensitivity_range_per_percent_gradient <length-value>

为补偿高于水平的飞行路径角梯度而应用于 LAR 的额外前向偏移（以米为单位）。

use_zone <global-zone-name> as <zone-name>

指定定义 LAR 的区域。

# 3.8.7.5. 非制导弹道武器发射计算模型 WSF_BALLISTIC_LAUNCH_COMPUTER

```txt
launch_computer <name> WSF_BALLISTIC-LaUNCH COMPUTER  
... launch_computer Commands ...  
... WSF-LaUNCH_COMPUTER Commands ...  
... WSF_BALLISTIC-LaUNCH_COMPUTER Commands ...  
end-Launch_computer 
```

WSF_BALLISTIC_LAUNCH_COMPUTER 实现了一种用于无制导武器（如重力炸弹或无制导火 箭 ）的 发 射 计 算 机。 武 器 可 能具 有 各 种 交 战约 束 ， 这 些约 束 必 须 在 发射WSF_EXPLICIT_WEAPON 之前满足。

weapon_tools 应用程序协助创建此类发射计算机。（参见：3.8.8.3 非制导弹道武器发射计算模型产生工具 BALLISTIC_LAUNCH_COMPUTER_GENERATOR ）。生成的输出产品是一个表格，提供从特定高度和速度投放武器的下游行程和飞行时间，从而可以预测未来的武器释放以将撞击位置放置在所需位置。

命令

注意：以下命令的顺序很重要。必须在飞行时间和下游值之前定义发射高度、发射速度和目标高度。

launch_altitudes <minimum-altitude> <delta-altitude> <number-of-altitudes>

指定最小发射高度、高度增量和构成拦截包线的高度数量。假设高度是发射器在椭球地球上的高度。

注意：高度数量必须大于 1，高度增量必须大于 0.0。

launch_speeds <minimum-speed> <delta-speed> <number-of-speeds>

指定最小发射速度、速度增量和构成拦截包线的发射速度数量。

注意：速度数量必须大于 1，速度增量必须大于 0.0。

target_altitudes <minimum-altitude> <delta-altitude> <number-of-altitudes>

指定最小目标高度、高度增量和构成拦截包线的高度数量。假设高度是目标在椭球地球上的高度。

注意：高度数量必须大于 1，高度增量必须大于 0.0。

times_of_flight_values …

当武器在指定的发射高度、目标高度和发射速度下释放时的飞行时间值。给定的值数量必须等于发射高度数量 X 目标高度数量 X 发射速度数量，后者的索引循环速度比前者快（典型的“矩阵”顺序）。

注意：输入的值必须以秒为单位。

downrange_values …

当武器在指定的发射高度、目标高度和发射速度下释放时，从发射位置到撞击位置的下游距离。提供的值数量必须等于发射高度数量 X 目标高度数量 X 发射速度数量，后者的索引循环速度比前者快（典型的“矩阵”顺序）。

注意：输入的值必须以米为单位。

```txt
launch_computer example_lc WSF_BALLISTIC-LaUNCH_COMPUTER  
# Created by BallisticLaunchComputerGenerator on Fri Jan 13 15:02:49 2017  
launch_altitudes 3048 m 1524 m 2 # Min, Max, Number  
launch_speeds 128.611 m/s 25.7222 m/s 2 # Min, Max, Number  
target_altitudes 0.3048 m 3.048 m 2 # Min, Max, Number  
# target_altitudes (m) = 0, 3  
# target_altitudes (ft) = 1, 11  
times_of_flight_values # (seconds)  
# launch_alt = 3048 m, 10000 ft  
25.1523 25.1395 # launch_spd = 128 m/s, 421 ft/s, Mach=0.39  
25.179 25.1662 # launch_spd = 154 m/s, 506 ft/s, Mach=0.47  
# launch_alt = 4572 m, 15000 ft  
30.8852 30.8747 # launch_spd = 128 m/s, 421 ft/s, Mach=0.39  
30.9199 30.9094 # launch_spd = 154 m/s, 506 ft/s, Mach=0.47  
downrange_values # (meters)  
# launch_alt = 3048 m, 10000 ft  
3146.33 3140.31 # launch_spd = 128 m/s, 421 ft/s, Mach=0.39  
3763.21 3763.21 # launch_spd = 154 m/s, 506 ft/s, Mach=0.47  
# launch_alt = 4572 m, 15000 ft  
3841.33 3841.33 # launch_spd = 128 m/s, 421 ft/s, Mach=0.39  
4601.07 4601.07 # launch_spd = 154 m/s, 506 ft/s, Mach=0.47  
end_launch_computer 
```

# 3.8.7.6. 制 导 弹 道 导 弹 发 射 计 算 模 型

# WSF_BALLISTIC_MISSILE_LAUNCH_COMPUTER

```txt
launch_computer <name> WSF_BALLISTIC_MISSLERLAUNCH COMPUTER ... launch_computer Commands ... ... WSF-LaUNCH COMPUTER Commands ... ... WSF_BALLISTIC_MISSLERLAUNCH COMPUTER Commands ... ... target_data <target-type> ... end_target_data ... end-Launch_computer 
```

WSF_BALLISTIC_MISSILE_LAUNCH_COMPUTER 实现了一种用于弹道导弹的发射计算机。该导弹可以是地对地导弹或地对空导弹（包括空间目标）。对于地对地导弹，必须使用surface_to_surface_table 命令指定拦截表。对于地对空导弹，必须使用 surface_to_air_table命令指定拦截表。

对于地对地计算，计算机将使用目标轨迹中的位置。如果目标轨迹中未定义位置，则计算机将使用目标轨迹中的“真实平台”位置（如果平台存在）。假设目标是静止的。
对于地对空计算，计算机将始终使用目标轨迹中的“真实平台”。

此发射计算机的表格应使用 weapon_tools 实用程序生成。（参见：3.8.8.4 制导弹道导弹发射计算模型产生工具 BALLISTIC_MISSILE_LAUNCH_COMPUTER_GENERATOR ）。

