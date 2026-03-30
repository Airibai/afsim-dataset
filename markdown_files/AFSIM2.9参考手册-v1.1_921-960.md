central_body … end_central_body：指定用于模拟平台的中心体及相关椭球模型。

<central-body-type>的选项包括：

▫ earth_wgs72（地球世界大地测量系统 1972）  
□ earth_wgs84（地球世界大地测量系统 1984）  
□ earth_egm96（地球重力模型 1996）  
□ moon（月球）  
□ sun（太阳）  
□ jupiter（木星）

默认值：earth_wgs84

polar_offset_angles <angle-value> <angle-value>：指定中心体的极偏移角（分别为 x_p 和y_p），相对于 WCS（ITRS）坐标系的天体中间极（CIP）。提供这些值（约为十分之一角秒）可以实现 ECI 和 WCS 坐标之间的非常高精度转换。默认值：0.0rad0.0rad

注意：WCS 到 LLA 的转换受中心体选择的影响，以及在惯性（ECI）坐标转换中计算的恒星运动变换。

# 4.11.2. 大气湍流模型 Turbulence model

在红外和光学波长中考虑大气湍流对 AFSIM 激光传播非常重要，因为它会产生平均光束扩展效应。这种效应独立于衍射和波前误差等其他因素，减少了影响高能激光目标或激光通信接收器的平均光束功率。

# 湍流模型方程

AFSIM实现了湍流光束扩展角的等斑关系：

$$
\theta_ {0} = \left[ 2. 9 1 k ^ {2} \int_ {0} ^ {L} C _ {n} ^ {2} (z) z ^ {\frac {5}{3}} d z \right] ^ {\frac {3}{5}}
$$

其中 $\mathbf { z } ( \mathrm { h } )$ 是一个函数，将高度 h 与从接收器到发射器的路径距离 L 相关联。 $\begin{array} { r } { \mathbf { k } = \frac { 2 \pi } { \lambda } } \end{array}$ = 2π是 特征激光波长 的波数， $C _ { n } ^ { 2 }$ 是大气结构参数，单位为 $m ^ { - 2 / 3 }$ 。

注意：在评估此积分时，通常理解为实际的 $C _ { n } ^ { 2 }$ 表达式通常是 h 的函数，而不是 z。

$C _ { n } ^ { 2 }$ 模型

有多种记录的 $C _ { n } ^ { 2 }$ 模型。目前在 AFSIM 中实现的是 Hufnagel-Valley (5/7) (“hv57”) 大气结构函数，其形式为：

$$
C _ {n} ^ {2} (h) = 8. 2 \times 1 0 ^ {- 2 6} W ^ {2} \left(\frac {h}{1 0 0 0}\right) ^ {1 0} e ^ {- h / 1 0 0 0} + 2. 7 \times 1 0 ^ {- 1 6} e ^ {- h / 1 5 0 0} + A e ^ {- h / 1 0 0}
$$

其中，h 是计算函数的地表以上高度（米）， $\mathrm { A } = 1 . 7 \times 1 0 ^ { - 1 4 }$ 和 $\mathsf { W } = 2 1$ 。

参考

该模型的理论基础可以在未发表的论文《The Effect of Atmospheric Optical Turbulence onLaser Communication Systems: Part 1, Theory》中找到，该论文由 Thomas C Farrell 撰写，隶属于美国空军研究实验室空间飞行器主任。

# 4.11.3. 大气模型 Atmosphere Model

```txt
atmosphere_model <model-name> <atmosphere-model-type> ... end_atmosphere_model 
```

<model-name>: 您为特定大气模型实例指定的名称。  
<atmosphere-model-type>: 您所使用的大气模型的类型。

可用的大气模型类型

WSF_PIECEWISE_EXPONENTIAL_ATMOSPHERE: 这种模型类型使用分段指数函数来近似大气特性。适用于需要对大气层进行分段建模的应用。

WSF_JACCHIA_ROBERTS_ATMOSPHERE: 这种模型基于 Jacchia-Roberts 模型，常用于高层大气模拟，特别是在航空航天应用中。它提供了在传统模型可能不够准确的高度下的大气条件的详细建模。

通过定义大气模型，您可以在模拟中使用这些模型来更准确地反映大气条件对系统的影响。

# 4.11.3.1. 内联大气模型 atmosphere

# 大气模型

在 AFSIM中，大气模型用于模拟模拟平台移动时所经过的空气。默认的大气定义是 1976年标准大气。然而，MIL-STD-210A 定义了几种非标准大气类型，分别为热带、热、冷和极地大气。此外，还允许另一种大气类型，该类型在 100,000 英尺以下的所有高度上升高或降低标准大气温度，以匹配特定地势高度下的期望密度高度。

```txt
default_atmosphere_type [standard_day | hot_day | tropical_day | cold_day | polar_day | custom | simple_dt <temperature value>] 
```

可用的大气模型类型

□ standard_day: 默认提供的标准大气。  
□ hot_day: 热大气。  
□ tropical_day: 热带大气。  
□ cold_day: 冷大气。  
□ polar_day: 极地大气。  
□ custom: 自定义大气。  
□ simple_dt <temperature value>: 简单温度偏差大气，默认值为 $+ 1 0$ 度 K。

# 关键字和输入块

□ default_atmosphere_type: 这是一个全局命令，应该在使用大气的任何类型定义之前指定。每个“simple_dt”类型的大气实例必须使用与“standard_day”大气相同的（静态）温度偏差。  
□ atmosphere_type: 用于在传感器或移动器定义中调用特定大气类型。此命令的上下文是局部的，将覆盖全局默认大气类型。  
□ print_mks_atmosphere_tables | print_sae_atmosphere_tables: 该命令在当前目录中创建一个名为“UtAtmosphereTables.lis”的输出文件，按 500 米或 5000 英尺的增量列出高度、温度、压力、密度、声速和水密度。

▫ atmosphere_table … end_atmosphere_table: 该块将 default_atmosphere_type 设置为‘custom’，并根据表输入从头开始构建大气。最多可以定义 512 个高度，必须按升序定义。

```txt
atmosphere_table  
<height-m> <temperature-K> <pressure-Pa>  
<height-m> <temperature-K> <pressure-Pa> <density-kg-per-m3>  
<height-m> <temperature-K> <pressure-Pa> <density-kg-per-m3> <sonic-speed-mps>  
end_atmosphere_table 
```

□ contrailing_altitude_floor <length-value> 和 contrailing_altitude_ceiling<length-value>: 调整大气中可能形成凝结尾迹的带。默认情况下，该带位于椭球体上方 26,000 英尺至 35,000 英尺之间。  
□ atmosphere_calibration … end_atmosphere_calibration: 该 块 将default_atmosphere_type 设置为‘simple_dt’，并选择一个温度偏差，以提供指定地势高度下所需的空气密度或温度。

```txt
atmosphere Calibration altitude <length-value> density <mass-density-value> temperature <temperature-value> end_atmosphere_calibration 
```

```txt
atmosphere_CALibration
# This block will set the default Atmosphere_type_ to simple_dt, and choose the delta temperature
# needed to match the given air density or temperature at a specified altitude. A printed block
# in the output stream will indicate the delta temperature (from standard) value selected.
# "altitude" is required, and one only of either "density" or "temperature" is required.
altitude 11000 ft
density 0.85896 kg/m3
#temperature 20 F
end_atmosphere_CALibration 
```

# 注意事项

MIL-STD-210A 非标准大气仅延伸到 100,000 英尺，标准大气模型继续向上延伸到大约200,000 英尺（61 公里），在此高度以上返回的空气密度为零。

一旦个别大气被声明为特定类型，default_atmosphere_type 将不再使用，模拟可能会出现大气属性冲突。

# 4.11.3.2. Jacchia-Roberts 大气模型 WSF_JACCHIA_ROBERTS_ATMOSPHERE

```txt
atmosphere_model <name> WSF_JACCHIA_ROBERTS_ATMOSPHERE ... Common Atmosphere Commands ... solar Flux ... average_solar Flux ... geomagnetic_index ... 
```

WSF_JACCHIA_ROBERTS_ATMOSPHERE 提供了一种大气模型，该模型模拟了外大气层的温度剖面，并依赖于太阳和地磁活动。然后根据不同的高度区域获得密度。详细信息请参见Vallado 的《Fundamentals of Astrodynamics and Application》第四版附录 B。

常用大气命令

□ central_body … end_central_body   
□ central_body <central-body-type>   
▫ polar_offset_angles   
▫ end_central_body

指定模拟平台使用的中心体及相关椭球模型。<centralbodytype> 的选项如下：

▫ earth_wgs72 (地球世界大地测量系统 1972)：中心体椭球根据 WGS-72 标准定义。  
□ earth_wgs84 (地球世界大地测量系统 1984)：中心体椭球根据 WGS-84 标准定义。  
□ earth_egm96 (地球重力模型 1996)：中心体椭球根据 EGM-96 标准定义。  
□ moon (月球)：中心体椭球根据已发布的月球参数定义。  
□ sun (太阳)：中心体椭球根据已发布的太阳参数定义。  
□ jupiter(木星)：中心体椭球根据已发布的木星参数定义。

默认值：earth_wgs84

polar_offset_angles <angle-value> <angle-value> 指定中心体的极偏移角（分别为 x_p 和y_p），相对于 WCS(ITRS) 坐标系的天体中间极 (CIP)。提供这些值（数量级为十分之一角秒）可以实现 ECI 和 WCS 坐标之间的高精度转换。

默认值：0.0 rad 0.0 rad

注意：WCS->LLA 转换受中心体选择的影响，以及在惯性 (ECI) 坐标转换中计算的恒星运动变换。

# 命令

solar_flux <real-value> 设置该大气模型使用的 $\pm 0 . 7 ~ \mathsf { c m }$ 太阳通量，单位为 $1 0 ^ { - 2 2 } \mathrm { { W / m } } ^ { 2 } / $ Hz。合理的值范围为 [50,400]。此值是感兴趣日期的通量平均值。

默认值：150

average_solar_flux <real-value> 设置该大气模型使用的 10.7 cm 太阳通量的平均值，单位为 $1 0 ^ { - 2 2 } \mathrm { W / m } ^ { 2 } / \mathrm { H z }$ 。合理的值范围为 [50,400]。此值是以感兴趣日期为中心的 81 天运行平均通量。

默认值：150

geomagnetic_index <real-value> 设置地磁活动指数 $\mathrm { K _ { p } }$ 。提供的值必须在 [0,9] 范围内。默认值：0

# 4.11.3.3. 指数剖面大气模型 WSF_PIECEWISE_EXPONENTIAL_ATMOSPHERE

```txt
atmosphere_model <name> WSF Piecewise_EXPONENTIAL_ATMOSPHERE ... Common Atmosphere Commands ... end_atmosphere_model 
```

WSF_PIECEWISE_EXPONENTIAL_ATMOSPHERE 使用一系列不同高度范围的指数剖面来模拟大气密度。在每个范围内，剖面形式为： $\begin{array} { r } { \rho ( h ) = \rho _ { 0 } e x p \left[ - \frac { h - h _ { 0 } } { H } \right] } \end{array}$ ，其中，H 是尺度高度， $h _ { 0 }$ 是该段开始的高度， $\rho _ { 0 }$ 是模型在该高度的密度。这些常数的值可以在 Vallado 的《Fundamentals of Astrodynamics and Application》第四版第 567 页的表 8-4 中找到，并在下方列出。这些值的选择确保了在段边界处的密度是连续的。

常数值表  

<table><tr><td>h0[km]</td><td>H[km]</td><td>ρ0[kg·m3]</td></tr><tr><td>0.0</td><td>7.294</td><td>1.225e0</td></tr><tr><td>25.0</td><td>6.349</td><td>3.899e-2</td></tr><tr><td>30.0</td><td>6.682</td><td>1.774e-2</td></tr><tr><td>40.0</td><td>7.554</td><td>3.972e-3</td></tr><tr><td>50.0</td><td>8.382</td><td>1.057e-3</td></tr><tr><td>60.0</td><td>7.714</td><td>3.206e-4</td></tr><tr><td>70.0</td><td>6.549</td><td>8.770e-5</td></tr><tr><td>80.0</td><td>5.799</td><td>1.905e-5</td></tr><tr><td>90.0</td><td>5.382</td><td>3.396e-6</td></tr><tr><td>100.0</td><td>5.877</td><td>5.297e-7</td></tr><tr><td>110.0</td><td>7.263</td><td>9.661e-8</td></tr><tr><td>120.0</td><td>9.473</td><td>2.438e-8</td></tr><tr><td>130.0</td><td>12.636</td><td>8.484e-9</td></tr><tr><td>140.0</td><td>16.149</td><td>3.845e-9</td></tr><tr><td>150.0</td><td>22.523</td><td>2.070e-9</td></tr><tr><td>180.0</td><td>29.740</td><td>5.464e-10</td></tr><tr><td>200.0</td><td>37.105</td><td>2.789e-10</td></tr><tr><td>250.0</td><td>45.546</td><td>7.248e-11</td></tr><tr><td>300.0</td><td>53.628</td><td>2.418e-11</td></tr><tr><td>350.0</td><td>53.298</td><td>9.518e-12</td></tr><tr><td>400.0</td><td>58.515</td><td>3.725e-12</td></tr><tr><td>450.0</td><td>60.828</td><td>1.585e-12</td></tr><tr><td>500.0</td><td>63.822</td><td>6.967e-13</td></tr><tr><td>600.0</td><td>71.835</td><td>1.454e-13</td></tr><tr><td>700.0</td><td>88.667</td><td>3.614e-14</td></tr><tr><td>800.0</td><td>124.64</td><td>1.170e-14</td></tr><tr><td>900.0</td><td>181.05</td><td>5.245e-15</td></tr><tr><td>1000.0</td><td>268.00</td><td>3.019e-15</td></tr></table>

常用大气命令

central_body … end_central_body

central_body <central-body-type>

polar_offset_angles

指定模拟平台使用的中心体及相关椭球模型。<central bodytype> 的选项如下：

□ earth_wgs72 (地球世界大地测量系统 1972)：中心体椭球根据 WGS-72 标准定义。  
□ earth_wgs84(地球世界大地测量系统 1984)：中心体椭球根据 WGS-84 标准定义。  
□ earth_egm96 (地球重力模型 1996)：中心体椭球根据 EGM-96 标准定义。  
□ moon(月球)：中心体椭球根据已发布的月球参数定义。  
□ sun(太阳)：中心体椭球根据已发布的太阳参数定义。  
□ jupiter (木星)：中心体椭球根据已发布的木星参数定义。

默认值：earth_wgs84

polar_offset_angles <angle-value> <angle-value> 指定中心体的极偏移角（分别为 x_p 和y_p），相对于 WCS(ITRS) 坐标系的天体中间极 (CIP)。提供这些值（数量级为十分之一角秒）可以实现 ECI 和 WCS 坐标之间的高精度转换。

默认值：0.0 rad 0.0 rad

注意：WCS->LLA 转换受中心体选择的影响，以及在惯性 (ECI) 坐标转换中计算的恒星运动变换。

# 4.12. 空气动力学 WSF_AERO

```perl
aero <new-type-name> <base-type-name> debug reference_area <area-value> aspect_ratio <float-value> oswalds_factor <float-value> cl_max <float-value> mach_and_cd <float-value> <float-value> cd_zero_subsonic <float-value> mach_begin_cd_rise <float-value> cd_zero_supersonic <float-value> mach_end_cd_rise <float-value> subsonic_cd_slope <float-value> supersonic_cd_slope <float-value> mach_max_supersonic <float-value> end_aero 
```

# Aero Block 概述

AeroBlock 允许用户指定简单的空气动力学阻力和升力属性，以近似作用于通过空气移动的物体上的力。它用于移动物体，以确定施加在飞行器上的侧向力和向下力的量，从而提供必要的横向加速度以引导拦截目标轨迹。然而，在低动态压力下，所需的力可能会物理上超过空气动力学体的能力。该类将把所需的力限制在指定的 Clmax能够产生的范围内，成比例地减少侧向力和垂直力。结果力将提供给动力学引擎，该引擎汇总施加的力，计算加速度，并整合这些加速度以确定飞行器的运动状态。

空气动力学阻力和升力

空气动力学阻力和升力力大致遵循关系式 $\mathsf { F } { = } { \mathsf { q S } } { \mathsf { C } }$ ，即力 F 等于动态压力 q 乘以参考面积 S再乘以系数 C，其中动态压力等于空气密度的一半乘以空气速度的平方。升力系数 Cl 值通常随迎角线性变化，直到达到最大值。阻力系数 Cd 值遵循抛物线趋势，从零升力时的最小值开始，随着升力系数的平方增加而增加。流线型物体的零升力阻力系数通常不会显著变化，直到速度超过阻力发散马赫数，在此情况下，阻力系数随着马赫数的增加而增加。

指定零升力阻力系数 (Cdo)

用户首先需要估算考虑中的物体的零升力阻力系数 Cdo。零升力阻力系数反映了寄生阻力，这使得它在某种程度上与空气动力体的“清洁”或流线型程度同义。以下是指定 Cdo 的三种方法：

1) 单一常数值：对于远低于音速的低速使用，空气流动的可压缩性不会成为问题，可以接受一个单一的常数值。可以参考实验阻力估算资源（如 Hoerner 的《流体动力阻力》）来估算 Cdo 值，并使用 zero_lift_cd 关键字将其提供给此类实例。  
2) 已知的零升力阻力系数表：如果已经知道空气动力体的零升力阻力系数表（相对于马赫数），则可以使用 mach_and_cd 关键字按递增的马赫数顺序提供给类。运行时将根据马赫数插值阻力系数值。  
3) 两个关键阻力系数值：如果用户可以提供两个关键阻力系数值，类将尝试填充其余部分。所需的关键值是跨音速阻力上升开始的亚音速马赫数，以及阻力上升平稳后略微下降的超音速马赫数。用户提供的关键字是：mach_begin_cd_rise 与 cd_zero_subsonic 配对，以及 mach_end_cd_rise 与 cd_zero_supersonic配对。类将推断出跨音速区域（约马赫 ${ \mathrm { : = } } 1 . 0$ ）之间的典型阻力上升形状。

![](images/e1dde73eaa5b5fe37d12080f03aa11222d45d8825c0cf3e18295842afb55beb4.jpg)

这三种指定 Cdo 的方法是互斥的，不能混合使用。

诱导阻力的计算

用户接下来需要指定如何计算由于升力引起的阻力（诱导阻力）。这取决于 aspect_ratio、oswalds_factor 和升力系数（受 cl_max 限制）。

详细过程描述

Update()方法确定与当前飞行条件相对应的平台施加的空气动力。大气密度和音速从当前高度获得，动态压力与空气密度和当前速度的平方成正比。计算马赫数，因为阻力值可以作为马赫数的函数指定。最大横向力（所需力的俯仰和偏航分量的向量和）限制在当前空气动力极限；Fmax=DynamicPressure $\times$ ReferenceArea $\times$ Clmax。如果其向量和超过 Fmax，则所需的俯仰和偏航力将按比例减少，直到等于 Fmax。然后，给定由施加的横向力产生的当前升力系数，计算阻力值作为依赖值。结果空气动力是（阻力、偏航力、俯仰力）的向量和。

![](images/bda1614fbb681a757e48cd8e5adf0450d79bd663690d75253e6c302a7a188ba3.jpg)

Three Options for Specifying Cdo of a Vehicle

![](images/c07a9c197012bbad31fd6ffb72f320c56bde465b3b5977db6a5a3c4f395a2740.jpg)  
Typical Relationship Between Lift and Drag Coefficients

命令

debug：在运行时启用调试输出。  
reference_area <area-value>：空气动力学参考面积。通常是飞机的机翼面积（从顶部视图看）。参考面积用于将无量纲的力系数转换为实际力（力等于系数乘以动态压力乘以参考面积）.  
aspect_ratio <float-value>：机翼的展弦比（AR）是翼展的平方除以其面积，是一个无量纲量。较高的值通常能更有效地产生升力，并减少由于升力引起的诱导阻力。滑翔机设计有非常长而细的机翼以最小化诱导阻力。对于亚音速飞机，通常可以接受使用理想化的抛物线阻力极来近似现实： $\operatorname { C d } = \operatorname { C d o } + \mathbf { k } \times \mathbf { C l } ^ { 2 }$ ，其中 $\begin{array} { r } { \mathbf { k } = \frac { 1 . 0 } { \pi \times \mu \mathrm { R } \times \mathrm { e } } \mathrm { ~ } } \end{array}$ π×AR×e  
oswalds_factor <float-value>：奥斯瓦尔德效率因子（通常表示为 e）是一个经验确定的值，用于计算与升力产生不可避免相关的诱导阻力，近似公式为： $\operatorname { C d } = \operatorname { C d o } + \mathbf { k } \times \mathbf { C l } ^ { 2 }$ ，其中 $\begin{array} { r } { \mathbf { k } = \frac { 1 . 0 } { \pi \times \ A \mathrm { R } \times \mathrm { e } } , } \end{array}$ 。默认值：0.95  
cl_max<float-value>：最大升力系数。此值指定飞行器空气动力学上可获得的最大升力。完整飞机的 $\mathrm { C l } _ { \mathrm { m a x } }$ 通常为 1.4 左右。  
zero_lift_cd<float-value>：零升力阻力系数。仅在低速空气动力学中给出单一值，当流动不可压缩时使用。  
mach_and_cd <float-value> <float-value>：马赫数及其对应的 Cdo。通过多次提供此关键字以递增的马赫数顺序指定阻力表。  
cd_zero_subsonic <float-value>：跨音速阻力上升区域之前的零升力阻力系数。使用mach_begin_cd_rise 指定此阻力上升开始的对应马赫数。  
mach_begin_cd_rise <float-value>：跨音速阻力上升开始的马赫数。此值必须小于 1.0，

通常约为 0.78 到 0.86。使用 cd_zero_subsonic 指定此阻力上升开始的对应阻力系数。

cd_zero_supersonic <float-value>：跨音速阻力上升结束时的零升力阻力系数。使用mach_end_cd_rise 指定此阻力上升结束的对应马赫数。  
mach_end_cd_rise <float-value>：跨音速阻力上升结束的马赫数。此值必须大于 1.0，通常在 1.05 到 1.2 区域。在马赫数大于此值时，Cdo 值通常开始减少，但由于速度的平方关系，总阻力仍然增加。使用 cd_zero_supersonic 指定此阻力上升结束的对应阻力系数。  
subsonic_cd_slope <float-value>：在跨音速阻力上升区域以下，随着马赫数增加，零升力阻力系数的变化。默认值：1.0  
supersonic_cd_slope <float-value>：在跨音速阻力上升区域以上，随着马赫数增加，零升力阻力系数的变化。此值可以是正的或负的。默认值：1.0  
mach_max_supersonic <float-value>：指定此值以阻止在跨音速阻力上升区域以上，随着马赫数增加，阻力系数的连续上升或下降。如果马赫数高于此指定值，则零升力阻力系数将保持不变。

# 4.13. AI 相关

# 4.13.1. 行为树 behavior_tree

```txt
behavior_tree <one or more nodes> end_behavior_tree 
```

# Behavior Tree 概述

BehaviorTree是一种人工智能技术，允许场景开发人员快速创建具有各种战术模块（称为行为或行为节点）的灵活代理。这些节点可以通过连接节点以有趣且相互关联的方式组合在一起。

# 基本节点类型

行为节点（BehaviorNodes）：树的叶节点，包含用户定义的脚本，用于执行特定行为或动作。

连接节点（ConnectorNodes）：用于构建和组织树。这些节点指定行为节点之间的关系。

# 连接节点

连接节点用于构建行为树的结构和语法：

```txt
<connector-node-type> [run_selection ...] [make_selection ...] <two or more nodes> end_<connector-node-type> 
```

目 前 支 持 五 种 连 接 节 点 类 型 ： sequence 、 parallel 、 selector 、 priority_selector 和weighted_random。

sequence…end_sequence：顺序节点是行为树中第二常用的连接节点。当到达顺序节点时，它按顺序执行其所有子节点，直到其中一个子节点未通过其前置条件。如果第一个子节点失败，则不执行任何子节点。如果所有子节点通过其前置条件，则全部执行。

parallel…end_parallel：并行节点用于行为树中，以执行每个通过前置条件的子节点，而不考虑顺序。  
selector…end_selector：选择器节点是行为树中最常用的连接节点。选择器节点指示树仅选择其一个子节点执行。树将执行选择器节点的第一个通过其前置条件的子节点。  
priority_selector … end_priority_selector：优先选择器节点用于行为树中，以选择并执行价值最高的子节点。子节点的价值由其前置条件脚本块确定。优先选择器节点始终（且仅）执行其价值最高的子节点。  
weighted_random … end_weighted_random：加权随机节点用于行为树中，以随机选择并执行一个子节点。执行均匀加权随机选择，每个子节点的权重由其前置条件脚本块确定。

# 连接节点子命令

这些子命令仅对 selector、priority_selector 和 weighted_random 类型有用：

run_selection [ until_done | for <time> | repeat <int> ]：指定选定子节点将执行多长时间，而不是默认的：一次（重复 1 次）。如果声明“until_done”，则子节点将执行直到其前置条件返回 0.0 或 false。  
make_selection [ continuous | count <int> ]：指定将进行多少次选择，而不是默认的：连续。这不会影响或改变 make_selection 定义的内容，而是可以限制选择器类型节点将执行的次数。

#

以下行为树示例展示了如何使用 weighted_random 节点在行为“cat”和“dog”之间随机选择，选择概率分别为 $67 \%$ 和 $33 \%$ （根据其前置条件返回值）。每次选择时，节点将在每次更新时自动运行 30 秒，而不是每次更新时进行新选择（因为 run_selection 命令）。weighted_random 节点将仅进行十次选择，然后不再执行任何操作（因为 make_selection 命令）。因此，此树仅在大约 300 秒内（30 秒乘以 10）执行操作。

```txt
behavior cat precondition return 2.0 end_precondition execute writeln("cat"); end_execute   
end_behavior   
behavior dog precondition return 1.0 end_precondition execute writeln("dog"); end_execute   
end_behavior 
```

```txt
behavior_tree  
weighted_random  
run_selection for 30 sec  
make_selection count 10  
behavior_node cat  
behavior_node dog  
end_weighted_random  
end_behavior_tree 
```

这种行为树结构提供了一种简单而灵活的方式来建模 AI 行为，减少了开发复杂行为所需的时间和精力。

# 定义行为树

行为树默认有一个不可见的根节点，该节点是一个并行节点。所有在根级别存在的行为和节点都会被检查其前置条件，并在前置条件通过时执行。

```txt
behavior_tree <one or more nodes> end_behiorize_tree 
```

行为树可以包含理论上无限深度的嵌套连接节点和行为。以下是一个不使用任何连接节点的行为树示例，只有一层深度，通过仅将行为节点附加到树的[不可见]根节点。

示例浅层行为树

```txt
假设所有这些命名的行为都是预定义的  
behavior_tree  
behavior_node check_fuel  
behavior_node check_instruments  
behavior_node drink_coffee  
end_behavior_tree
```

# 示例简单行为树

```txt
每次更新时对"check_fuel"和"check_instruments"行为进行排序  
behavior_tree  
sequence  
behavior_node check_fuel  
behavior_node check_instruments  
end_sequence  
end_behavior_tree 
```

# 示例嵌套行为树

```txt
假设所有这些命名的行为都是预定义的behavior_treesequence
```

```txt
behavior_node drink_coffee selector behavior_node check_fuel behavior_node check_instruments end_selector end_sequence end_behavior_tree 
```

行为树设计考虑

树构建者的两个主要考虑因素是行为节点的前置条件和节点在树中的位置。这两个因素共同决定了行为树的哪些节点会被执行。前置条件是节点内部的检查，用于确定它是否可以运行。节点在行为树中的位置充当“外部检查”，以确定它是否会运行。例如，如果一个节点是选择器节点的子节点，而其他子节点经常被选择，那么这个节点可能永远不会被调用。

以下是一个示例，展示了这两个决定因素的作用：

behavior evade-threat precondition ArrayWsfPlatform> mlIncoming $\equiv$ ArrayWsfPlatform $\rightharpoondown$ ); if(PROCESSOR.WeaponsIncoming(mlIncoming) $>0$ 1 return true; return false; end_precondition execute extern void Evade(void); Evade(); end_execute   
end_behavior   
behavior chase_target precondition if(!PROCESSOR.Target().IsValid()) return false; return true; end_precondition execute extern void Chase(WsfTrack); Chase( PROCESSOR.Target()); end_execute   
end_behavior   
behavior_tree selector behavior_node evade-threat behavior_node chase_target

```txt
end_selector end_behavior_tree 
```

在这个例子中，“evade_threat”行为的前置条件只有在有威胁来临时才会让该行为执行。而“chase_target”行为的前置条件只有在有有效目标可追踪时才会让该行为执行。观察它们在行为树中的排列方式，我们可以看到“evade_threat”行为被设置为其选择器节点父节点的第一个子节点。每当“evade_threat”行为的前置条件通过时，该行为被“选择”并执行，其他子节点则不被考虑。换句话说，“chase_target”行为只有在没有东西需要规避时才会被选择。如果树构建者希望这两个行为都被执行，他可能会使用一个顺序节点作为父节点。

# 4.13.2. 高级行为树 advanced_behavior_tree

```txt
advanced_behior_tree <one or more nodes> end.advanced_behior_tree 
```

# Advanced Behavior Tree 概述

AdvancedBehaviorTrees 是在行为树的基础上构建的，允许三种状态（运行、成功、失败），而不是两种（成功、失败）。第三种状态的添加使得 AI 可以更加复杂和具有反应性。

# 基本节点类型

高级行为节点（AdvancedBehaviorNodes）：树的叶节点，包含用户定义的脚本，用于执行特定行为或动作。  
复合节点（CompositeNodes）：用于构建和组织树。这些节点指定行为节点之间的关系。

复合节点

复合节点的结构和语法如下：

```txt
<composite-node-type> name <string> <one or more nodes> end_<composite-node-type> 
```

目 前 支 持 七 种 复 合 节 点 类 型 ： sequence 、 sequence_with_memory 、 selector 、selector_with_memory、parallel、priority_selector 和 weighted_random。

此外，还有四种装饰器节点：repeater、inverter、succeeder 和 negator。

selector…end_selector：选择器节点按顺序执行所有子节点（脚本中从上到下，行为树工具中从左到右）。如果任何子节点成功，选择器将成功，之后的所有子节点将被跳过。如果所有子节点失败，选择器将失败。  
selector_with_memory … end_selector_with_memory：带记忆的选择器节点与普通选择器节点的工作方式相同，但有一个例外：如果一个节点失败，选择器将向前移动记忆，并且在记忆重置之前不会检查该子节点。记忆在一个节点成功或所有子节点失败时重置。  
sequence…end_sequence：顺序节点按顺序执行所有子节点。如果任何子节点的前置条件或执行脚本失败，顺序将失败，之后的所有子节点将被跳过。如果所有子节点成功，顺序将成功。  
sequence_with_memory … end_sequence_with_memory：带记忆的顺序节点与普通顺序节点的工作方式相同，但有一个例外：如果一个节点成功，顺序将向前移动记忆，并且

在记忆重置之前不会检查该子节点。记忆在一个节点失败或所有子节点成功时重置。

parallel…end_parallel：并行节点将同时执行所有子节点，而不考虑顺序。并行节点使用成功策略来确定成功/失败（参见下面的 success_policy 命令）。如果所有子节点都已完成执行且策略未命中，并行节点将失败。默认情况下，并行节点使用 succeed_on_one，这意味着只有一个子节点需要成功，并行节点就会成功。  
priority_selector … end_priority_selector：优先选择器节点选择并执行价值最高的子节点。子节点的价值由其前置条件脚本块确定。优先选择器节点始终执行其价值最高的子节点。  
weighted_random … end_weighted_random：加权随机节点用于行为树中，以随机选择并执行一个子节点。执行均匀加权随机选择，每个子节点的权重由其前置条件脚本块确定。

# 装饰器节点

装饰器节点类似于复合节点，但只有一个子节点。装饰器修改其下方子节点的行为。

decorator inverter … end_decorator：反转器节点将反转其子节点的返回状态。如果子节点返回成功，反转器将返回失败；如果子节点返回失败，反转器将返回成功。  
decorator negator … end_decorator：否定器节点将返回失败，无论子节点的返回状态如何。  
decorator succeeder … end_decorator：成功器节点将返回成功，无论子节点的返回状态如何。  
decorator repeater [ repeat <int> | for <time> | until_done ] … end_decorator：重复器节点将重复执行其子节点，直到满足设定的条件。重复器节点在达到此条件后返回成功。repeat <int>将使子节点执行<int>次后成功。for <time>将使子节点执行直到经过<time>时间。until_done 将重复子节点，直到其返回成功或失败。

这些高级行为树结构提供了一种更复杂和灵活的方式来建模 AI 行为，使得 AI 能够更好地响应动态环境。

# 定义 Advanced Behavior Tree

高级行为树的声明非常简单。与普通行为树类似，每个树都有一个不可见的根节点，该节点是一个并行节点。所有直接位于根节点下的节点将并行执行。

```txt
advanced_behior_tree <one or more nodes> end.advanced_behior_tree 
```

行为树可以包含理论上无限深度的嵌套连接节点和行为。以下是一些示例：

示例浅层行为树

# 假设所有这些命名的行为都是预定义的

```txt
advanced_behior_tree behavior_node check_fuel behavior_node check_instruments behavior_node drink_coffee end.advanced_behior_tree 
```

示例简单行为树

```txt
每次更新时对"check_fuel"和"check_instruments"行为进行排序  
advanced_behavior_tree  
sequence  
behavior_node check_fuel  
behavior_node check_instruments  
end_sequence  
end.advanced_behavior_tree 
```

示例嵌套行为树

```txt
假设所有这些命名的行为都是预定义的  
advanced_behavior_tree  
sequence  
behavior_node drink_coffee  
selector  
behavior_node check_fuel  
behavior_node check_instruments  
end_selector  
end_sequence  
end.advanced_behavior_tree 
```

子树

树也可以在其他树中定义。这对于在视觉上分隔树的部分以及重用树非常有用。示例带子树的行为树

```txt
假设所有这些命名的行为都是预定义的  
advanced_behavior_tree  
sequence  
behavior_node wake_up  
advanced_behavior_tree  
sequence  
behavior_node eat  
behavior_node exercise  
end_sequence  
end.advanced_behavior_tree  
end_sequence  
end.advanced_behavior_tree 
```

其他命令

name<string>：为树命名。这将在根节点上显示，并在 Mystic 的行为树视图中的树选择组合框中显示。

desc<string>：为树定义描述。当在 Mystic 的行为树视图中悬停在根节点上时，将显示此描述。  
▪ btt<boolean>：定义树是否发送所需数据以在 Mystic 的行为树视图中显示树。  
root_node_type [parallel | priority_selector | selector | selector_with_memory | sequence | sequence_with_memory | weighted_random ]：设置此树的根节点的复合节点类型。   
success_policy [threshold <int> | succeed_on_one | succeed_on_all ]：为并行节点或使用root_node_type parallel 的 advanced_behavior_tree 设置成功策略。三种策略可用于处理并行节点上的成功：threshold 将采用必须成功的节点数量以使并行节点成功。succeed_on_one 将使并行节点在任何子节点成功时成功。succeed_on_all 将使并行节点仅在所有子节点成功时成功。

这些高级行为树结构提供了一种更复杂和灵活的方式来建模 AI 行为，使得 AI 能够更好地响应动态环境。

# 4.13.3. RIPR

Reactive Integrated Planning aRchitecture (RIPR) 是一个人工智能框架，允许场景开发人员快速创建具有复杂行为的灵活代理。RIPR 代理脚本通常使用行为树技术构建（现在在WSF 的所有脚本处理器上可用）；有关更多信息，请参阅行为树页面。许多指挥官/下属代理对使用工作板技术。工作板是一个任务分配系统，通过 WsfRiprProcessor 和 WsfRIPRJob类向场景开发人员开放。

RIPR 是 WSF 基线发布的一部分，由以下类组成：

▫ WSF_RIPR_PROCESSOR / WsfRiprProcessor   
▫ behavior_tree（现在在 WSF_SCRIPT_PROCESSOR 上）  
□ WsfRIPRJob

入门指南

大多数 RIPR 功能通过在 WSF 脚本语言中编写脚本来使用。有关可用脚本功能的详细信息，请参阅 WSF 参考指南。

行为树技术 是使您的行为脚本模块化、可重用且易于编辑的最佳方式。

工作板任务分配系统 可通过 WSF_RIPR_PROCESSOR 类及其派生类型访问。工作板可用于为智能代理的层次结构提供动态、适应性强的指挥和控制。

示例和解释

RIPR 资源分配器：关于如何使用 RIPR 进行协调干扰的示例。

RIPR 场景：关于具有 RIPR 代理的指挥层次结构场景的更多解释。

故障排除

请参考 RIPR 故障排除指南以获取调试代理的步骤。

对象类型

WSF_RIPR_PROCESSOR

WSF_RIPR_PROCESSOR 是包含工作板技术的处理器。如果您希望平台或代理使用自下而上的工作板竞标系统，则应使用 WSF_RIPR_PROCESSOR。有关其他选项，请参阅WSF_QUANTUM_TASKER_PROCESSOR。

RIPR 提供了一种强大的框架，用于在复杂的模拟环境中管理和协调智能代理的行为和任务分配。

# 4.14. 消息表 message_table

```txt
message_table comm_type<comm-type-1> #...Message Size Commands for<comm-type-1>,formatted as follows: type ... subtype ... subtype ... type ... subtype ... subtype ... default ... comm_type<comm-type-2> ... Message Size Commands for<comm-type-2> comm_type<comm-type-n> ... Message Size Commands for<comm-type-n> default_comm_type ... Message Size Commands for other comm types end_message_table 
```

message_table 块用于为消息分配大小，当消息在最初传输时未定义大小时使用（可以通过使用 WsfMessage.SetSizeInBits 或 WsfMessage.SetSizeInBytes 脚本方法来提供此功能）。如果未定义消息大小，将使用以下算法查询 message_table。将使用定义值的第一个步骤来确定消息大小：

1. 使用与匹配的 comm_type 块中具有匹配 type 和 subtype 的条目。  
2. 使用与匹配的 comm_type 块中具有匹配 type 的条目。  
3. 使用与匹配的 comm_type 块中的 default 条目。  
4. 使用 default_comm_type 块中具有匹配 type 和 subtype 的条目。  
5. 使用 default_comm_type 块中具有匹配 type 的条目。  
6. 使用 default_comm_type 块中的 default 条目。

注意：消息大小仅在首次传输时分配。如果消息随后被转发，大小不会更改。

# 设备命令

comm_type <comm-type>

引入一个类型、子类型和默认命令块，这些命令定义了来自指定 <comm-type> 的通信设备的消息的大小和可选优先级。

default_comm_type

引入一个类型、子类型和默认命令块，这些命令定义了来自没有相应 comm_type 条目

的通信设备的消息的大小和可选优先级。

消息大小命令

type <message-type> <data-size-value> [priority <integer-priority-value>]

指定指定类型的消息的大小和可选优先级。

注意：type 命令可以根据需要重复。

default <message-type> <data-size-value> [priority <integer-priority-value>]

指定没有适用类型命令的消息的默认大小和可选优先级。

subtype <message-sub-type> <data-size-value> [priority <integer-priority-value>]

指定指定子类型的消息的大小和可选优先级，以及最近指定的类型（或默认）。

注意：此命令可以根据需要重复。

这些命令允许用户灵活地定义消息的大小和优先级，确保在不同通信设备和消息类型之间的一致性和可控性。

# 4.15. 传感器覆盖 WSF_SENSOR_COVERAGE

```batch
coverage <name> WSF_SENSOR_COVERAGE
grid ...
assets ...
moe ...
start_time ...
end_time ...
start_epoch ...
end_epoch ...
output_dir ...
raw_data_file ...
overlay_file ...
interval Constraint ...
end_coverage 
```

# 概述

传感器覆盖监控指定网格和自由资产之间的传感器交互。与传感器覆盖相关的设备是任何传感器。此外，在每个网格资产-自由资产对中，只需一个资产指定设备；另一个资产应使用“none”作为设备名称。

# 网格资产规范

grid <grid-name>

使用具有给定名称的覆盖网格作为计算此覆盖的网格。参考：4.15.3 覆盖网格定义Coverage Grid。

# 自由资产规范

assets … end_assets

指定用于此覆盖的自由资产。

platform <platform-name> <device-name>

指定具有给定名称的平台将包含在此覆盖的自由资产中。除非设备名称为“none”否则给定平台必须具有相关设备。

platform_type <platform-type> <device-name>

指定具有给定类型的所有平台将包含在此覆盖的自由资产中。除非设备名称为“none”，否则给定平台类型必须具有相关设备。  
category <category-name> <device-name>

指定给定类别中具有相关设备的任何平台将包含在此覆盖的自由资产中。如果设备名称为“none”，则此类别中的所有平台将添加到此覆盖的自由资产集中。

group <group-name> <device-name>

指定给定组中具有相关设备的任何平台将包含在此覆盖的自由资产中。如果设备名称为“none”，则此组中的所有平台将添加到此覆盖的自由资产集中。

# 有效性度量

```txt
moe <name> <measure-type> ... end_moe 
```

moe … end_moe

指定由覆盖计算的有效性度量（MOE）。有关可用 MOE 的列表，参见：4.15.1 有效性度量 MOE。

# 覆盖时间间隔命令

start_time <time-value>

将覆盖时间间隔的开始设置为给定的模拟时间。此命令或 start_epoch 可用于指定覆盖时间间隔的开始时间。如果未指定开始时间，则覆盖时间间隔的开始设置为模拟的开始时间。

end_time <time-value>

将覆盖时间间隔的结束时间设置为给定的模拟时间。此命令或 end_epoch 可用于指定覆盖时间间隔的结束时间。如果未指定结束时间，则覆盖时间间隔的结束设置为模拟的结束时间。

start_epoch <month> <day-of-month> <year> hh:mm:ss

将覆盖时间间隔的开始设置为给定的日期和时间。此命令或 start_time 可用于指定覆盖时间间隔的开始时间。如果未指定开始时间，则覆盖时间间隔的开始设置为模拟的开始时间。

end_epoch <month> <day-of-month> <year> hh:mm:ss

将覆盖时间间隔的结束设置为给定的日期和时间。此命令或 end_time 可用于指定覆盖时间间隔的结束时间。如果未指定结束时间，则覆盖时间间隔的结束时间设置为模拟的结束时间。

# 数据输出命令

output_dir <path-value>

设置此覆盖生成的所有文件的目录。默认输出目录是工作目录。

raw_data_file <file-name>

如果设置了此文件名，覆盖计算将存储原始访问间隔，并在覆盖计算结束时将这些间隔写入指定文件。

overlay_file <file-name>

如果设置了此文件名，覆盖计算将生成一个数据文件，该文件可以由 CoverageOverlay插件显示。此命令将为这些文件附加规范扩展名“.cvg”到指定的文件名。

时间间隔约束命令

interval_constraint … end_interval_constraint

为覆盖计算指定时间间隔约束，允许排除持续时间过短或过长的间隔。可以通过多种方式指定这些约束适用于哪些资产。可以在单个时间间隔约束块中包含多个规范，并且可以为单个覆盖计算指定多个时间间隔约束块。

output_file <file-name>

指定将从覆盖计算中过滤出的间隔写入的文件的名称。这些文件的格式将与raw_data_file 生成的文件的输出匹配。

platform <platform-name> <constraint-type> <time-value> [<time-value>]

指定涉及指定平台的访问间隔将根据给定的 <constraint-type> 进行过滤，可能的值包括：

▫ minimum- 移除持续时间短于给定值的访问间隔。  
□ maximum - 移除持续时间长于给定值的访问间隔。  
□ interval- 移除短于第一个给定时间或长于第二个给定时间的访问间隔。

platform_type <platform-type> <constraint-type> <time-value> [<time-value>]

指定涉及给定 <platform-type> 的平台的访问间隔将根据给定的 <constraint-type> 进行过滤。

device <device-name> <constraint-type> <time-value> [<time-value>]

指定涉及指定设备的访问间隔将根据给定的 <constraint-type> 进行过滤。

device_type <device-type> <constraint-type> <time-value> [<time-value>]

指定涉及给定 <device-type> 的设备的访问间隔将根据给定的 <constraint-type> 进行过滤。

# 4.15.1. 有效性度量 MOE

# 4.15.1.1.访问间隔有效性度量 WSF_ACCESS_DURATION_MOE

```txt
moe <name> WSF_ACCESS_DURATION_MOE  
subtype ...  
output ...  
end_moe 
```

# 概述

WSF_ACCESS_DURATION_MOE 计算与单个自由资产的访问间隔持续时间相关的量。此度量针对的是单个自由资产的覆盖间隔，而不是任何自由资产的覆盖。因此，两个不同自由资产的访问间隔在时间上重叠的覆盖不会被计为一个长访问间隔，而是两个独立的间隔，每个自由资产一个。如果这样的间隔跨越了覆盖间隔的边界，则该间隔会被截断，以便在覆盖间隔开始（或结束）时开始（或结束）。

# 计算子类型

subtype <sub-type> [<parameter>]

指定计算子类型。

WSF_ACCESS_DURATION_MOE 具有以下不需要参数的子类型：

□ minimum- 测量值将是相关网格点的最小访问间隔持续时间。

□ maximum - 测量值将是相关网格点的最大访问间隔持续时间。  
□ mean- 测量值将是相关网格点的平均访问间隔持续时间。  
□ standard_deviation- 测量值将是相关网格点的访问间隔持续时间的标准差。  
▫ sum- 测量值将是相关网格点的访问间隔持续时间的总和。注意，如果访问间隔重叠，则这可能比整个覆盖间隔的持续时间更长。

WSF_ACCESS_DURATION_MOE 支持以下需要输入参数的子类型，该参数指定一个百分比值，必须大于 0 且小于 100。

▫ percent_above - 在覆盖间隔的 <parameter> 百分比时间内，相关网格点经历的访问间隔持续时间大于或等于计算值。

测量输出命令（参见：4.15.2 有效性度量输出 Measure Output Commands）

output <output-type> … end_output

□ 指定要为有效性度量生成的输出形式。<output_type> 的允许值为：

data - 生成一个文本文件，其中包含每个网格点的 MOE 值。  
grid_stats - 生成一个文本文件，计算网格上 MOE 的汇总统计数据。  
lat_lon_stats- 生成一个文本文件，计算作为纬度或经度函数的汇总统计数据。

# 4.15.1.2.覆盖时间有效性度量 WSF_COVERAGE_TIME_MOE

```txt
moe <name> WSF_COVERAGE_TIME_MOE  
subtype ...  
output ...  
end_moe 
```

# 概述

WSF_COVERAGE_TIME_MOE 计算与网格点覆盖时间相关的量。此度量针对的是覆盖间隔内网格点至少可以访问一个自由资产的访问间隔。

# 计算子类型

subtype <sub-type> [<parameter>]

指定计算子类型。

WSF_COVERAGE_TIME_MOE 具有以下不需要参数的子类型：

□ total- 测量值将是相关网格点的总访问持续时间。  
□ percent- 测量值将是相关网格点的访问持续时间，占整个覆盖间隔的百分比。  
□ 每个带有“per”后缀的子类型，除非另有说明，以秒为单位或样本的百分比测量值。这些需要一个参数来定义这些八个子类型的样本持续时间。  
□ maximum_per- 测量值将是相关网格点的单个日历样本的最大总访问持续时间。  
□ maximum_percent_per - 测量值将是相关网格点的单个日历样本的最大访问持续时间，占样本的百分比。  
▫ minimum_per- 测量值将是相关网格点的单个日历样本的最小总访问持续时间。  
□ minimum_percent_per- 测量值将是相关网格点的单个日历样本的最小访问持续时间，占样本的百分比。  
▫ mean_per- 测量值将是相关网格点每个样本的平均访问持续时间。这不使用日历样本的数量，而是使用覆盖间隔的样本持续时间来计算平均值。  
▫ mean_percent_per- 测量值将是相关网格点单个样本的平均访问持续时间，占整个覆盖间隔持续时间的百分比。这不使用日历样本的数量，而是使用覆盖间隔的样本

持续时间来计算平均值。

□ standard_deviation_per - 测量值将是相关网格点每个日历样本的访问持续时间的标准差。  
□ standard_deviation_percent_per - 测量值将是相关网格点每个日历样本的访问持续时间的标准差，占样本的百分比。

注 意 ： 这 些 子 类 型 在 实 际 使 用 此 参 数 时 存 在 细 微 差 异 。 minimum_per 、minimum_percent_per、maximum_per 和 maximum_percent_per 将此持续时间与 UTC 的午夜绑定，例如，如果给定值为 1 天，则每个样本将从午夜到连续的午夜，UTC。如果<sample-span> 的值为 6 小时，则样本将从午夜到 0600，0600 到 1200，1200 到 1800，或 1800 到午夜。其结果之一是，对于这两个子类型，<sample-span> 的唯一有效值是可以表示为 1/n 天的值，其中 n 是正整数。这是为了使样本始终与每个日历日（午夜到连续午夜，UTC）对齐。最小可接受值为 1 秒。这些将被称为“日历样本”。然而，mean_per、mean_percent_per、standard_deviation_per 和 standard_deviation_percent_per 子类型不将<sample-span> 绑定到日历，因此将接受任何正持续时间作为值。例如，假设 <sample-span>的值为 1 天。如果覆盖间隔从 1 月 1 日 1200 开始，并持续到 1 月 2 日 1200，最小值和最大值将计算为 2 天 -1 月 1 日和 1 月 2 日 - 但平均值将仅计算为 1，因为间隔实际上只有 24 小时长。

WSF_COVERAGE_TIME_MOE 支持以下需要输入参数的子类型，该参数指定网格点必须能够访问的最少自由资产数量才能计入间隔：  
total_time_above - 测量值将是相关网格点至少可以访问 <parameter> 个自由资产的总持续时间。  
percent_time_above - 测量值将是相关网格点至少可以访问 <parameter> 个自由资产的访问持续时间，占整个覆盖间隔的百分比。

测量输出命令（参见：4.15.2 有效性度量输出 Measure Output Commands）

output <output-type> … end_output

指定要为有效性度量生成的输出形式。<output_type> 的允许值为：

□ data - 生成一个文本文件，其中包含每个网格点的 MOE 值。  
□ grid_stats - 生成一个文本文件，计算网格上 MOE 的汇总统计数据。  
□ lat_lon_stats - 生成一个文本文件，计算作为纬度或经度函数的汇总统计数据。

# 4.15.1.3.同一时间可访问资产有效性度量 WSF_N_ASSET_COVERAGE_MOE

```batch
moe <name> WSF_N_ASSET_COVERAGE_MOE  
subtype ...  
output ...  
end_moe 
```

概述

WSF_N_ASSET_COVERAGE_MOE 计算与网格点在某一时刻可以访问的自由资产数量相关的量。

计算子类型

subtype <sub-type> [<parameter>]

指定计算子类型。

WSF_N_ASSET_COVERAGE_MOE 具有以下不需要参数的子类型：

□ minimum- 测量值将是相关网格点同时访问的最小自由资产数量。  
▫ maximum- 测量值将是相关网格点同时访问的最大自由资产数量。  
□ mean- 测量值将是相关网格点同时访问的平均自由资产数量。  
▫ unique- 测量值将是整个覆盖间隔内相关网格点可访问的唯一自由资产总数。  
□ WSF_N_ASSET_COVERAGE_MOE 支持以下需要输入参数的子类型，该参数指定一个百分比值，必须大于 0 且小于 100。  
▫ percent_above - 在覆盖间隔的 <parameter> 百分比时间内，相关网格点访问的自由资产数量多于计算值。

测量输出命令（参见：4.15.2 有效性度量输出 Measure Output Commands）

output <output-type> … end_output

指定要为有效性度量生成的输出形式。<output_type> 的允许值为：

□ data - 生成一个文本文件，其中包含每个网格点的 MOE 值。  
□ grid_stats- 生成一个文本文件，计算网格上 MOE 的汇总统计数据。  
□ lat_lon_stats - 生成一个文本文件，计算作为纬度或经度函数的汇总统计数据。

4.15.1.4.访问次数有效性度量 WSF_NUMBER_OF_ACCESSES_MOE  
```batch
moe <name> WSF_NUMBER_OF_ACCESSES_MOE  
subtype ...  
output ...  
end_moe 
```

概述

WSF_NUMBER_OF_ACCESSES_MOE 计算与网格点访问自由资产次数相关的量。访问间隔是针对每个自由资产的，因此如果一个网格点同时访问两个自由资产，则计为两个独立的访问。此 MOE 的某些子类型在其定义中使用从午夜到午夜的 UTC 日历天。

计算子类型

subtype <sub-type> [[<min-parameter> <max-parameter>] <sample-span>]指定计算子类型。

WSF_NUMBER_OF_ACCESSES_MOE 具有以下不需要参数的子类型：

▫ total- 测量值将是相关网格点的总访问次数。

WSF_NUMBER_OF_ACCESSES_MOE 具有三个仅接受 <sample-span> 参数的子类型：

▫ minimum_per- 测量值将是相关网格点在一个样本内的最小访问次数。如果覆盖间隔完全适合一个样本内，则这与总间隔数相同。  
▫ maximum_per- 测量值将是相关网格点在一个样本内的最大访问次数。如果覆盖间隔完全适合一个样本内，则这与总间隔数相同。  
□ mean_per - 测量值将是 总访问次数 -对于相关网格点。覆盖间隔持续时间|样本跨度

<sample-span> 参数定义了这些三个子类型的样本持续时间。

注意：这些子类型在实际使用此参数时存在细微差异。minimum_per 和 maximum_per将此持续时间与 UTC 的午夜绑定，例如，如果 <sample-span> 的值为 1 天，则每个样本将从午夜到连续的午夜，UTC。如果 <sample-span> 的值为 6 小时，则样本将从午夜到 0600，0600 到 1200，1200 到 1800，或 1800 到午夜。其结果之一是，对于这两个子类型，<sample-span> 的唯一有效值是可以表示为 1/n 天的值，其中 n 是正整数。这是为了使样本始终与每个日历日（午夜到连续午夜，UTC）对齐。最小可接受值为 1 秒。然而，mean_per不将 <sample-span> 绑定到日历，因此将接受任何正持续时间作为值。例如，假设<sample-span> 的值为 1 天。如果覆盖间隔从 1 月 1 日 1200 开始，并持续到 1 月 2 日1200，minimum_per 和 maximum_per 子类型将计算为 2 天（1 月 1 日和 1 月 2 日），但 mean_per 子类型将仅计算为 1 天，因为间隔实际上只有 24 小时长。

WSF_NUMBER_OF_ACCESSES_MOE 支持以下需要两个输入参数的子类型，这些参数指定最小和最大时间跨度。这些子类型将仅计算持续时间至少与最小跨度一样长但不超过最大跨度的访问间隔：

in_span- 测量值将是相关网格点的访问次数，其持续时间至少与 <min-parameter> 一样长，但不超过 <max-parameter>。

WSF_NUMBER_OF_GAPS_MOE 支持以下需要三个输入参数的子类型，按此顺序指定应计数的间隔的最小和最大持续时间，然后是上述描述的样本跨度：

in_span_per- 测量值将是 in_span 的值，除以整个覆盖间隔的天数。

测量输出命令（参见：4.15.2 有效性度量输出 Measure Output Commands）

output <output-type> … end_output

指定要为有效性度量生成的输出形式。<output_type> 的允许值为：

□ data - 生成一个文本文件，其中包含每个网格点的 MOE 值。  
□ grid_stats- 生成一个文本文件，计算网格上 MOE 的汇总统计数据。  
□ lat_lon_stats- 生成一个文本文件，计算作为纬度或经度函数的汇总统计数据。

# 4.15.1.5.覆盖间隔有效性度量 WSF_NUMBER_OF_GAPS_MOE

```txt
moe <name> WSF_NUMBER_OF_GAPS_MOE  
subtype ...  
output ...  
end_moe 
```

概述

WSF_NUMBER_OF_GAPS_MOE 计算与网格点经历的覆盖间隙数量相关的量。此度量针对的是间隙，即网格点无法访问任何自由资产的时间间隔。

计算子类型

subtype <sub-type> [[<minimum-duration> <maximum-duration>] <sample-span>]指定计算子类型。

WSF_NUMBER_OF_GAPS_MOE 具有以下不需要参数的子类型：

total- 测量值将是整个覆盖间隔内相关网格点的总间隙数量。

▫ WSF_NUMBER_OF_GAPS_MOE 具有三个仅接受 <sample-span> 参数的子类型：  
□ minimum_per- 测量值将是相关网格点在一个样本内的最小间隙数量。如果覆盖间隔完全适合一个样本内，则这与总间隙数相同。  
□ maximum_per- 测量值将是相关网格点在一个样本内的最大间隙数量。如果覆盖间隔完全适合一个样本内，则这与总间隙数相同。  
总间隙数□ mean_per - 测量值将是 对于相关网格点。覆盖间隔持续时间 样本跨度

<sample-span> 参数定义了这些三个子类型的样本持续时间。

注意：这些子类型在实际使用此参数时存在细微差异。minimum_per 和 maximum_per将此持续时间与 UTC 的午夜绑定，例如，如果 <sample-span> 的值为 1 天，则每个样本将从午夜到连续的午夜，UTC。如果 <sample-span> 的值为 6 小时，则样本将从午夜到 0600，0600 到 1200，1200 到 1800，或 1800 到午夜。其结果之一是，对于这两个子类型，<sample-span> 的唯一有效值是可以表示为 1/n 天的值，其中 n 是正整数。这是为了使样本始终与每个日历日（午夜到连续午夜，UTC）对齐。最小可接受值为 1 秒。然而，mean_per不将 <sample-span> 绑定到日历，因此将接受任何正持续时间作为值。例如，假设<sample-span> 的值为 1 天。如果覆盖间隔从 1 月 1 日 1200 开始，并持续到 1 月 2 日1200，minimum_per 和 maximum_per 子类型将计算为 2 天（1 月 1 日和 1 月 2 日），但 mean_per 子类型将仅计算为 1 天，因为间隔实际上只有 24 小时长。

WSF_NUMBER_OF_GAPS_MOE 支持以下需要两个输入参数的子类型，这些参数分别指定应计数的间隙的最小和最大持续时间：

in_span - 测量值将是整个覆盖间隔内相关网格点的总间隙数量，其持续时间至少为<minimum-duration> 且最多为 <maximum-duration>。

WSF_NUMBER_OF_GAPS_MOE 支持以下需要三个输入参数的子类型，按此顺序指定应计数的间隙的最小和最大持续时间，然后是上述描述的样本跨度：

in_span_per - 测量值将是 覆盖间隔持续时间/样本跨度 总间隙数 其中仅在间隙的持续时间至少为<minimum-duration> 且最多为 <maximum-duration> 时才计数。

测量输出命令（参见：4.15.2 有效性度量输出 Measure Output Commands）

output <output-type> … end_output

指定要为有效性度量生成的输出形式。<output_type> 的允许值为：

□ data - 生成一个文本文件，其中包含每个网格点的 MOE 值。  
□ grid_stats- 生成一个文本文件，计算网格上 MOE 的汇总统计数据。  
□ lat_lon_stats- 生成一个文本文件，计算作为纬度或经度函数的汇总统计数据。

# 4.15.1.6.简单交互性有效性度量 WSF_SIMPLE_COVERAGE_MOE

```txt
moe <name> WSF_SIMPLE_COVERAGE_MOE output ...  
end_moe 
```

概述

WSF_SIMPLE_COVERAGE_MOE 用于测量网格资产是否与覆盖中指定的自由资产之一有任何交互。如果有交互，则此度量的值设置为 1.0；否则，值为 0.0。

测量输出命令（参见：4.15.2 有效性度量输出 Measure Output Commands）

output <output-type> … end_output

指定要为有效性度量生成的输出形式。<output_type> 的允许值为：

□ data - 生成一个文本文件，其中包含每个网格点的 MOE 值。  
□ grid_stats- 生成一个文本文件，计算网格上 MOE 的汇总统计数据。  
□ lat_lon_stats - 生成一个文本文件，计算作为纬度或经度函数的汇总统计数据。

# 4.15.1.7.重访时间有效性度量 WSF_REVISIT_TIME_MOE

```batch
moe <name> WSF_REVISIT_TIME_MOE  
subtype ...  
output ...  
end_moe 
```

概述

WSF_REVISIT_TIME_MOE 计算与网格点重访时间相关的量。此度量针对的是间隙，即网格点无法访问任何自由资产的时间间隔。如果这样的间隙跨越了覆盖间隔的边界，则该间隙会被截断，以便在覆盖间隔开始（或结束）时开始（或结束）。

# 计算子类型

subtype <sub-type> [<parameter>]

指定计算子类型。WSF_REVISIT_TIME_MOE 具有以下不需要参数的子类型：

□ minimum- 测量值将是相关网格点的最小间隙持续时间。  
□ maximum- 测量值将是相关网格点的最大间隙持续时间。  
□ mean- 测量值将是相关网格点的平均间隙持续时间。  
□ standard_deviation- 测量值将是相关网格点的间隙持续时间的标准差。

WSF_REVISIT_TIME_MOE 支持以下需要输入参数的子类型，该参数指定一个百分比值，必须大于 0 且小于 100。

□ number_percent_below - 对于相关网格点，<parameter> 百分比的间隙持续时间短于计算值。  
□ percent_below - 在覆盖间隔的 <parameter> 百分比时间内，相关网格点的重访时间小于计算值。  
□ percent_below_gaps_only - 在覆盖间隙的 <parameter> 百分比时间内，相关网格点的重访时间小于计算值。

测量输出命令（参见：4.15.2 有效性度量输出 Measure Output Commands）

output <output-type> … end_output

指定要为有效性度量生成的输出形式。<output_type> 的允许值为：

□ data - 生成一个文本文件，其中包含每个网格点的 MOE 值。  
□ grid_stats- 生成一个文本文件，计算网格上 MOE 的汇总统计数据。  
□ lat_lon_stats- 生成一个文本文件，计算作为纬度或经度函数的汇总统计数据。

# 4.15.1.8.时间间隙覆盖有效性度量 WSF_TIME_AVERAGE_GAP_MOE

```batch
moe <name> WSF_TIME_AVERAGE_GAP_MOE output ...  
end_moe 
```

概述

WSF_TIME_AVERAGE_GAP_MOE 计算在随机采样覆盖间隔时，覆盖间隙的平均长度（以秒为单位）。此度量针对的是间隙，即网格点无法访问任何自由资产的时间间隔。结果等于（CoverageGapDuration  2）CoverageIntervalDuration

测量输出命令（参见：4.15.2 有效性度量输出 Measure Output Commands）

output <output-type> … end_output

指定要为有效性度量生成的输出形式。<output_type> 的允许值为：

□ data - 生成一个文本文件，其中包含每个网格点的 MOE 值。  
□ grid_stats- 生成一个文本文件，计算网格上 MOE 的汇总统计数据。  
□ lat_lon_stats- 生成一个文本文件，计算作为纬度或经度函数的汇总统计数据。

# 4.15.2. 有效性度量输出 Measure Output Commands

# 4.15.2.1.测量有效性网格数据输出 Measure of Effectiveness Grid Data Output

```batch
output data file <file-name> width <integer> precision <integer> format ... justify ...   
end_output 
```

测量有效性网格数据输出

output data … end_output

生成一个文件，其中包含覆盖网格中每个网格点的有效性度量最终值。请参见各个有效性度量以了解所测量值的含义。

文本测量输出命令

file <file-name>

指定将生成的文件的名称。文件将被创建到从定义有效性度量的覆盖对象继承的目录中。如果未指定文件名，将从覆盖名称、度量名称和输出类型特定后缀的组合生成一个名称。

width <integer>

设置输出字段的宽度。适当设置此值将使输出文件更易于人类阅读。

precision <integer>

设置在将数值数据写入生成文件时使用的精度位数。

format <format-specifier>

设置数值数据的格式。有效的格式说明符包括：

▫ fixed- 小数点后的位数是固定的。

▫ scientific- 数字以科学计数法表示，并且数字中的位数是固定的。  
▫ justify <justify-specifier>

设置输出在列宽中的位置。允许的值为：left 和 right，它们分别将字段内容放置在列的左侧或右侧。

4.15.2.2.测量有效性网格统计输出 Measure of Effectiveness Grid Stats Output  
```batch
output grid stats file <file-name> width <integer> precision <integer> format ... justify ... end_output 
```

# 测量有效性网格统计输出

output grid_stats … end_output

生成一个文件，其中包含覆盖网格上度量的最小值、最大值和平均值。

# 文本测量输出命令

1 file <file-name>

指定将生成的文件的名称。文件将被创建到从定义有效性度量的覆盖对象继承的目录中。如果未指定文件名，将从覆盖名称、度量名称和输出类型特定后缀的组合生成一个名称。

width <integer>

设置输出字段的宽度。适当设置此值将使输出文件更易于人类阅读。

precision <integer>

设置在将数值数据写入生成文件时使用的精度位数。

format <format-specifier>

设置数值数据的格式。有效的格式说明符包括：

▫ fixed- 小数点后的位数是固定的。  
□ scientific- 数字以科学计数法表示，并且数字中的位数是固定的。  
□ justify <justify-specifier>

设置输出在列宽中的位置。允许的值为：left 和 right，它们分别将字段内容放置在列的左侧或右侧。

4.15.2.3.测量有效性纬度/经度统计输出 Measure of Effectiveness Lat/Lon Stats Output  
```txt
output lat_lon.stats latitude longitude bin_size <angle-value> file <file-name> width <integer> precision <integer> format ... justify ... end_output 
```

测量有效性纬度/经度统计输出

output lat_lon_stats … end_output

生成一个文件，其中包含每个纬度或经度的测量值统计数据。通过投影出纬度或经度，将结果点进行分箱，并计算每个箱的度量最小值、最大值和平均值。仅当箱不为空时，才会将一行写入文件。

# 投影命令

■ latitude

生成作为纬度函数的汇总统计数据。

longitude

生成作为经度函数的汇总统计数据。

bin_size <angle-value>

指定网格点投影到的箱的大小。

# 文本测量输出命令

file <file-name>

指定将生成的文件的名称。文件将被创建到从定义有效性度量的覆盖对象继承的目录中。如果未指定文件名，将从覆盖名称、度量名称和输出类型特定后缀的组合生成一个名称。

width <integer>

设置输出字段的宽度。适当设置此值将使输出文件更易于人类阅读。

precision <integer>

设置在将数值数据写入生成文件时使用的精度位数。

format <format-specifier>

设置数值数据的格式。有效的格式说明符包括：

一 fixed- 小数点后的位数是固定的。  
□ scientific- 数字以科学计数法表示，并且数字中的位数是固定的。  
□ justify <justify-specifier>

设置输出在列宽中的位置。允许的值为：left 和 right，它们分别将字段内容放置在列的左侧或右侧。

# 4.15.3. 覆盖网格定义 Coverage Grid

```txt
grid <name> <grid-type> central_body ... grid_data_file ... suppress_gridPlatforms ... end_grid 
```

在模拟中，覆盖网格用于在一组固定位置上计算覆盖范围。每个覆盖计算都需要指定要进行计算的网格，并且多个覆盖计算可以使用相同的网格。

# 覆盖网格命令

grid <name> <grid-type> ... end_grid: 指定一个覆盖网格。可用的预定义覆盖网格类型包括：

□ WSF_LAT_LON_GRID: 在纬度和经度上形成的规则矩形网格。

▫ WSF_ZONE_BASED_GRID: 在纬度和经度上形成的规则网格，但点被过滤到指定区域内。  
□ WSF_DISTANCE_STEPPED_GRID: 具有给定距离分隔的规则矩形网格。  
□ WSF_EXISTING_PLATFORM_GRID: 由现有模拟平台形成的网格。  
□ WSF_COMPOSITE_GRID: 通过组合子网格形成的网格。

# 常见网格命令

grid_data_file <file-name>: 指定将在模拟结束时创建的输出文件的名称，该文件包含此网格中点的详细信息。  
central_body ... end_central_body: 指定模拟平台使用的中心体及相关椭球模型。可选的中心体类型包括：

□ earth_wgs72: 根据 WGS-72 标准定义的地球椭球。  
▫ earth_wgs84: 根据 WGS-84 标准定义的地球椭球。  
□ earth_egm96: 根据 EGM-96 标准定义的地球椭球。  
□ moon: 根据已发布的月球参数定义的月球椭球。   
▫ sun: 根据已发布的太阳参数定义的太阳椭球。  
▫ jupiter: 根据已发布的木星参数定义的木星椭球。

默认值为 earth_wgs84。

polar_offset_angles <angle-value> <angle-value>: 指定中心体的极偏移角（分别为 x_p 和y_p），用于相对于 WCS（ITRS）坐标系的天体中间极（CIP）。这些值通常为十分之一角秒的量级，用于在 ECI 和 WCS 坐标之间进行非常高精度的转换。默认值为 0.0rad0.0rad。  
suppress_grid_platforms <boolean-value>: 允许在 DIS 输出和分布式模拟中抑制网格资产平台。此抑制仅适用于由网格创建的平台，默认情况下启用。

这种结构允许用户在 AFSIM 中灵活地定义和管理覆盖网格，从而更好地模拟和分析地理覆盖范围。

# 4.15.3.1.经纬度网格 WSF_LAT_LON_GRID

```txt
grid <name> WSF_LAT_LON_grid ... Common Grid Commands ... latitudeSpan ... longitudeSpan ... spacing ... latitude_spacing ... longitudespacing ... altitude... origin .. asset ...   
end_grid 
```

# 概述

WSF_LAT_LON_GRID 是一种覆盖网格，跨越纬度和经度的矩形区域。网格中点之间的间隔以纬度或经度的角度指定。网格的高度是固定的，可以指定。

# 常见网格命令

grid_data_file <file-name>: 指定将在模拟结束时创建的输出文件的名称，该文件包含此网格中点的详细信息。  
central_body ... end_central_body: 指定模拟平台使用的中心体及相关椭球模型。可选的中心体类型包括：

□ earth_wgs72: 根据 WGS-72 标准定义的地球椭球。  
□ earth_wgs84: 根据 WGS-84 标准定义的地球椭球。  
□ earth_egm96: 根据 EGM-96 标准定义的地球椭球。  
□ moon: 根据已发布的月球参数定义的月球椭球。   
□ sun: 根据已发布的太阳参数定义的太阳椭球。  
▫ jupiter: 根据已发布的木星参数定义的木星椭球。

默认值为 earth_wgs84。

polar_offset_angles <angle-value> <angle-value>: 指定中心体的极偏移角（分别为 x_p 和y_p），用于相对于 WCS（ITRS）坐标系的天体中间极（CIP）。这些值通常为十分之一角秒的量级，用于在 ECI 和 WCS 坐标之间进行非常高精度的转换。默认值为 0.0rad0.0rad。  
suppress_grid_platforms <boolean-value>: 允许在 DIS 输出和分布式模拟中抑制网格资产平台。此抑制仅适用于由网格创建的平台，默认情况下启用。

# 特定命令

latitude_span <latitude-value> <latitude-value>: 设置此网格的纬度范围。  
▪ longitude_span <longitude-value> <longitude-value>: 设置此网格的经度范围。   
spacing<angle-value>: 设置网格点在纬度和经度上的间隔，但仅在这些间隔未以其他方式设置（如 latitude_spacing 或 longitude_spacing）时使用。  
latitude_spacing <angle-value>: 设置此网格相邻纬度之间的间隔。如果同时定义了latitude_spacing 和 spacing，则使用 latitude_spacing 提供的值。  
longitude_spacing <angle-value>: 设置此网格相邻经度之间的间隔。如果同时定义了longitude_spacing 和 spacing，则使用 longitude_spacing 提供的值。  
origin <latitude-value> <longitude-value>: 设置网格的原点。原点是其他点在纬度和经度上间隔的起点。原点必须在给定的 latitude_span 和 longitude_span 内。默认值为最小纬度和最小经度的点。  
altitude <length-value> <altitude-reference>: 设置网格点的高度。<altitude-reference>可以是 msl（指高度在平均海平面之上）或 agl（指高度在场景中任何地形之上）。  
asset <platform-type> <device-name>: 指定与此网格关联的资产将是<platform-type>的实例，并将使用名称为<device-name>的设备。如果网格点是被动目标，则给定的<device-name>也可以是 none。

这种结构允许用户在 AFSIM 中灵活地定义和管理覆盖网格，从而更好地模拟和分析地理覆盖范围。

# 4.15.3.2.区域网格 WSF_ZONE_BASED_GRID

```batch
grid <name> WSFZone_BASEDGRID ...Common Grid Commands... zone... spacing... 
```

```txt
latitude_spacing ...  
longitude-spacing ...  
origin ...  
altitude ...  
asset ...  
end_grid 
```

WSF_ZONE_BASED_GRID 是一种覆盖网格，具有在纬度和经度上规则排列的点，但其边界由用户可指定的区域定义。网格中点之间的间隔由纬度和经度的角度指定。南北和东西方向的间隔可以独立设置。网格的高度是固定的，可以指定。

# 常见网格命令

grid_data_file <file-name>: 指定将在模拟结束时创建的输出文件的名称，该文件包含此网格中点的详细信息。  
central_body ... end_central_body: 指定模拟平台使用的中心体及相关椭球模型。可选的中心体类型包括：

□ earth_wgs72: 根据 WGS-72 标准定义的地球椭球。  
□ earth_wgs84: 根据 WGS-84 标准定义的地球椭球。  
□ earth_egm96: 根据 EGM-96 标准定义的地球椭球。  
□ moon: 根据已发布的月球参数定义的月球椭球。   
□ sun: 根据已发布的太阳参数定义的太阳椭球。  
□ jupiter: 根据已发布的木星参数定义的木星椭球。

默认值为 earth_wgs84。

polar_offset_angles <angle-value> <angle-value>: 指定中心体的极偏移角（分别为 x_p 和y_p），用于相对于 WCS（ITRS）坐标系的天体中间极（CIP）。这些值通常为十分之一角秒的量级，用于在 ECI 和 WCS 坐标之间进行非常高精度的转换。默认值为 0.0rad0.0rad。  
suppress_grid_platforms <boolean-value>: 允许在 DIS 输出和分布式模拟中抑制网格资产平台。此抑制仅适用于由网格创建的平台，默认情况下启用。

# 特定命令

zone <global-zone-name>: 指定网格的边界应与名称为<global-zone-name>的全局区域的边界匹配。  
spacing<angle-value>: 设置网格点在纬度和经度上的间隔，但仅在这些间隔未以其他方式设置（如 latitude_spacing 或 longitude_spacing）时使用。  
latitude_spacing <angle-value>: 设置此网格相邻纬度之间的间隔。如果同时定义了latitude_spacing 和 spacing，则使用 latitude_spacing 提供的值。  
longitude_spacing <angle-value>: 设置此网格相邻经度之间的间隔。如果同时定义了longitude_spacing 和 spacing，则使用 longitude_spacing 提供的值。  
origin <latitude-value> <longitude-value>: 设置网格的原点。原点是其他点在纬度和经度上间隔的起点。原点必须在为此网格指定的区域所包围的纬度和经度矩形内。默认值为区域的质心。  
altitude <length-value> <altitude-reference>: 设置网格点的高度。<altitude-reference>可以是 msl（指高度在平均海平面之上）或 agl（指高度在场景中任何地形之上）。

asset <platform-type> <device-name>: 指定与此网格关联的资产将是<platform-type>的实例，并将使用名称为<device-name>的设备。如果网格点是被动目标，则给定的<device-name>也可以是 none。

这种结构允许用户在 AFSIM 中灵活地定义和管理覆盖网格，从而更好地模拟和分析地理覆盖范围。

# 4.15.3.3.距离网格 WSF_DISTANCE_STEPPED_GRID

```txt
grid <name> WSF_distance_STEPPED_grid ... Common Grid Commands ... size ... step_distance ... origin_index ... altitude ... origin ... asset ... end_grid 
```

WSF_DISTANCE_STEPPED_GRID 是一种覆盖网格，其中的点按给定距离分隔。网格将形成用户指定数量的行，每行位于某个纬度，并与相邻行保持用户指定的距离。每行将包含用户指定数量的点，每个点与其行中的邻居保持用户指定的距离。所有网格点将位于相同的用户指定高度。

# 常见网格命令

grid_data_file <file-name>: 指定将在模拟结束时创建的输出文件的名称，该文件包含此网格中点的详细信息。  
central_body ... end_central_body: 指定模拟平台使用的中心体及相关椭球模型。可选的中心体类型包括：

□ earth_wgs72: 根据 WGS-72 标准定义的地球椭球。  
□ earth_wgs84: 根据 WGS-84 标准定义的地球椭球。  
□ earth_egm96: 根据 EGM-96 标准定义的地球椭球。  
moon: 根据已发布的月球参数定义的月球椭球。  
□ sun: 根据已发布的太阳参数定义的太阳椭球。  
□ jupiter: 根据已发布的木星参数定义的木星椭球。

默认值为 earth_wgs84。

polar_offset_angles <angle-value> <angle-value>: 指定中心体的极偏移角（分别为 x_p 和y_p），用于相对于 WCS（ITRS）坐标系的天体中间极（CIP）。这些值通常为十分之一角秒的量级，用于在 ECI 和 WCS 坐标之间进行非常高精度的转换。默认值为 0.0rad0.0rad。  
suppress_grid_platforms <boolean-value>: 允许在 DIS 输出和分布式模拟中抑制网格资产平台。此抑制仅适用于由网格创建的平台，默认情况下启用。

# 特定命令

size<integer><integer>: 设置网格的大小。第一个值给出网格中的行数，第二个值给出每行中的点数。网格点的总数将是这两个值的乘积。  
step_distance <length-value> <length-value>: 指定相邻网格点之间的距离。第一个值给出

一行与下一行之间的分隔距离，第二个值给出同一行中点之间的分隔距离。

origin_index <integer> <integer>: 指定网格中位于 origin 命令给定位置的点。这些值从 0开始，从西南角开始计数。例如：

□ origin_index 0 0 表示西南角。  
□ 对于一个有 4 行和每行 5 个点的网格，origin_index 3 4 表示东北角。

origin <latitude-value> <longitude-value>: 设置网格的原点，即其他行和每行成员间隔的起点。网格中将在给定纬度处有一行，并且在网格的每行中将在给定经度处有一个点。  
altitude <length-value> <altitude-reference>: 设置网格点的高度。<altitude-reference>可以是 msl（指高度在平均海平面之上）或 agl（指高度在场景中任何地形之上）。  
asset <platform-type> <device-name>: 指定与此网格关联的资产将是<platform-type>的实例，并将使用名称为<device-name>的设备。如果网格点是被动目标，则给定的<device-name>也可以是 none。

这种结构允许用户在 AFSIM 中灵活地定义和管理覆盖网格，从而更好地模拟和分析地理覆盖范围。

4.15.3.4.批定平台网格 WSF_EXISTING_PLATFORM_GRID  
```txt
grid <name> WSF-existingPLATFORM_grid ... Common Grid Commands ... platform ... end_grid 
```

WSF_EXISTING_PLATFORM_GRID 是一种覆盖网格，由若干用户指定的平台组成。这种网格不会以任何方式修改指定的平台。这些平台不需要是静止的，也不需要在其位置上形成某种模式。

# 常见网格命令

grid_data_file <file-name>: 指定将在模拟结束时创建的输出文件的名称，该文件包含此网格中点的详细信息。  
central_body ... end_central_body: 指定模拟平台使用的中心体及相关椭球模型。可选的中心体类型包括：

□ earth_wgs72: 根据 WGS-72 标准定义的地球椭球。  
□ earth_wgs84: 根据 WGS-84 标准定义的地球椭球。  
earth_egm96: 根据 EGM-96 标准定义的地球椭球。  
□ moon: 根据已发布的月球参数定义的月球椭球。   
□ sun: 根据已发布的太阳参数定义的太阳椭球。  
□ jupiter: 根据已发布的木星参数定义的木星椭球。

默认值为 earth_wgs84。

polar_offset_angles <angle-value> <angle-value>: 指定中心体的极偏移角（分别为 x_p 和y_p），用于相对于 WCS（ITRS）坐标系的天体中间极（CIP）。这些值通常为十分之一角秒的量级，用于在 ECI 和 WCS 坐标之间进行非常高精度的转换。默认值为 0.0rad0.0rad。  
suppress_grid_platforms <boolean-value>: 允许在 DIS 输出和分布式模拟中抑制网格资产平台。此抑制仅适用于由网格创建的平台，默认情况下启用。

# 特定命令

platform <platform-name> <device-name>: 指定具有给定<platform-name>的平台应添加

到网格中，并使用给定<device-name>的设备进行覆盖计算。此命令可以用于任意数量的平台。

这种结构允许用户在 AFSIM 中灵活地定义和管理覆盖网格，从而更好地模拟和分析地理覆盖范围。

4.15.3.5.组合网格 WSF_COMPOSITE_GRID  
```txt
grid <name> WSF_COMPOSITEGRID ... Common Grid Commands ... subgrid ... end_subgrid end_grid 
```

WSF_COMPOSITE_GRID 是一种覆盖网格，通过组合子网格来定义。这对于计算地理上分离区域的覆盖非常有用。这些子网格可以是任何可用的网格类型（参见预定义覆盖网格类型），并且它们会创建自己的平台。每个定义的子网格在此网格的子网格中必须具有唯一的名称。子网格将继承此网格的 central_body 和 suppress_grid_platforms 设置。grid_data_file 将在此网格的子网格中被忽略。

# 常见网格命令

grid_data_file <file-name>: 指定将在模拟结束时创建的输出文件的名称，该文件包含此网格中点的详细信息。  
central_body ... end_central_body: 指定模拟平台使用的中心体及相关椭球模型。可选的中心体类型包括：

□ earth_wgs72: 根据 WGS-72 标准定义的地球椭球。  
□ earth_wgs84: 根据 WGS-84 标准定义的地球椭球。  
□ earth_egm96: 根据 EGM-96 标准定义的地球椭球。  
□ moon: 根据已发布的月球参数定义的月球椭球。   
□ sun: 根据已发布的太阳参数定义的太阳椭球。  
□ jupiter: 根据已发布的木星参数定义的木星椭球。

默认值为 earth_wgs84。

polar_offset_angles <angle-value> <angle-value>: 指定中心体的极偏移角（分别为 x_p 和y_p），用于相对于 WCS（ITRS）坐标系的天体中间极（CIP）。这些值通常为十分之一角秒的量级，用于在 ECI 和 WCS 坐标之间进行非常高精度的转换。默认值为 0.0rad0.0rad。  
suppress_grid_platforms <boolean-value>: 允许在 DIS 输出和分布式模拟中抑制网格资产平台。此抑制仅适用于由网格创建的平台，默认情况下启用。

# 特定命令

subgrid <name> <grid-type> ... end_subgrid: 添加具有给定<name>的子网格，并指定其类型为<grid-type>。子网格根据所选类型进行配置，并支持所选网格类型支持的任何命令。支持的子网格类型是那些创建自己平台的类型。

这种结构允许用户在 AFSIM 中灵活地定义和管理覆盖网格，从而更好地模拟和分析地理覆盖范围。

# 4.16. 网络战

# 4.16.1. 概述 Cyber Overview

# 网络战概述

网络战被定义为“国家行为体为了造成损害或破坏而渗透另一个国家的计算机或网络的行动”。AFSIM 通过提供一种平台（称为攻击者）来破坏另一种平台（称为受害者）的功能来实现网络战。

# 网络交战生命周期

抽象地说，网络交战有一个由六个阶段定义的生命周期。以下是每个阶段的描述，包括在现实生活中可能发生的情况以及在模拟模型环境中可能发生的情况。

# 1 目标阶段

现实世界：通过 OPE（作战准备环境）和情报确定目标。

任何有合理“进入方式”或可利用弱点的人。这可以是以下的组合：

□ 平台类别

□ 单个平台（按名称）

# 2 扫描阶段

现实世界：类似于 Nessus 或‘nmap’扫描，以列出或确认受害者的漏洞。

此阶段是可选的，伴随模拟中的视觉/声音效果和扫描的效果（例如，双向 RF 通信）。

可选概率：受害者会检测到询问并阻止漏洞利用。

可选响应：受害者指示是否存在漏洞。

# 3 传递阶段

现实世界：空中的 RF 信号或线上传输的数据。

传递漏洞和有效载荷……或触发预先植入的东西（远程、定时或逻辑炸弹）。

模拟中伴随的可视化和/或声音。

# 4 利用阶段

现实世界：权限提升、缓冲区溢出、使用意外输入/格式——使系统按照攻击者的利益行事。

概率应用成功：高保真工程细节被抽象为概率……与真实数据包/格式无关。

可选概率：攻击者立即对应用成功或失败有信心。

可选概率：目标立即知道攻击（通过 IDS、敏锐的操作员等）。

# 5 效果阶段

现实世界：有效载荷。

在受害者上注入并执行攻击者的恶意逻辑，并向攻击者报告应用的成功或失败（如果适用）。

效果包括预期的、非预期的、直接的和间接的（第二、第三、n 阶效果）。

分析师可以提供一系列非预期/间接效果及其相关概率。

# 6 反应阶段

现实世界：攻击者和受害者根据他们的感知采取的响应行动。

攻击者对应用和非预期副作用的响应。

受害者对攻击的反应。

可选概率：受害者在未来对这种能力免疫。

# AFSIM网络交战模型

在现实生活中，网络战争涉及利用软件和硬件中的漏洞来破坏系统的运行。AFSIM 并不明确模拟实际需要如何利用漏洞或由此产生的破坏细节，而是使用三种主要对象类型和脚本支持来模拟攻击的效果：

# cyber_effect

cyber_effect 对象提供 AFSIM 功能，用于模拟某些现实攻击的效果。例如，对传感器的某种现实攻击可以通过简单地将传感器标记为不可操作来模拟，从而阻止其检测目标和报告轨迹。

AFSIM包括许多预定义的效果（例如禁用通信、传感器和武器系统），但它也允许用户使用 WSF_CYBER_SCRIPT_EFFECT 创建效果。通过 WSF_CYBER_SCRIPT_EFFECT，用户定义脚本方法 Attack()和 Recover()，以实现攻击的模拟模型及其恢复。

# cyber_attack

cyber_attack对象提供一个或多个 cyber_effect 类型的列表，这些类型定义了攻击对受害者的影响。此外，它还包含：

如果受害者没有定义的响应，默认的受害者响应。  
一组用于控制交战过程中使用的随机数的值。

# cyber_protect

cyber_protect 对象定义受害平台对网络攻击的响应。模拟中的每个平台都有一个显式或隐式定义的 cyber_protect 对象，因为每个平台都可能受到网络攻击的威胁。

一个 cyber_protect 对象包含一组攻击响应。每个攻击响应提供：

适用的 cyber_attack 类型的名称。

定义网络生命周期中事件发生可能性的概率。  
受害者检测到扫描的概率。

▫ 攻击成功的概率。  
□ 攻击者立即知道攻击是否成功或失败的概率。  
□ 受害者检测到攻击发生的概率。  
□ 受害者能够将攻击源归因于攻击者的概率。  
□ 受害者将来对这种攻击类型免疫的概率。

随时间发生的事件的延迟时间：

□ 检测到已被攻击所需的时间。  
□ 检测到攻击后从攻击中恢复所需的时间。

分析师可以提供的可选脚本定义，以实现更多细节。

# 脚本命令和类

在 WsfPlatform 中提供了脚本方法，用于启动和查询攻击和扫描。

一个 WsfCyberEngagement 类的对象作为参数提供给网络脚本观察者、cyber_protect 中的脚本方法和 WSF_CYBER_SCRIPT_EFFECT。它为脚本方法提供有关交战的信息。

事件输出和可视化

除了实际模型外，AFSIM还提供：

event_output、csv_event_output 和观察者扩展，允许捕获有关网络交战事件的信息。

事 件 类 型 包 括 CYBER_ATTACK_INITIATED 、 CYBER_ATTACK_SUCCEEDEDCYBER_ATTACK_FAILED 、 CYBER_ATTACK_DETECTED 、 CYBER_ATTACK_ATTRIBUTEDCYBER_SCAN_INITIATED 1 CYBER_SCAN_SUCCEEDED 、 CYBER_SCAN_FAILEDCYBER_SCAN_DETECTED 、 CYBER_SCAN_ATTRIBUTED 、 CYBER_TRIGGER_EVALUATIONCYBER_TRIGGER_EXECUTION。

能够将附加信息写入 dis_interface 记录或 event_pipe 文件，以便通过可视化应用程序进行网络交战的可视化。

这种结构化的方法允许 AFSIM 在不需要复制现实世界网络攻击技术细节的情况下，模拟网络战争的战略和操作影响。

# AFSIM 网络交战模型的详细说明

目标阶段

在 目 标 阶 段 ， 攻 击 节 点 将 利 用 WSF_TASK_PROCESSORWSF_QUANTUM_TASKER_PROCESSOR 或其他处理器来选择受害者和攻击类型。

扫描阶段

这是一个可选步骤。在前一步选择目标后，攻击者将调用 WsfPlatform.CyberScan 脚本。受害者的逻辑如下：

1) 安排一个事件在 cyber_attack 类型的 scan_delay_time 完成时发生。  
2) 调用 CyberScanInitiated 观察者回调。  
3) 发出 WsfDraw 命令以记录可视化数据。

在模拟扫描持续时间的 scan_delay_time 完成时：

1) 在受害者的 cyber_protect 对象中找到适用的 attack_response。  
2) 如果用户在受害者的 cyber_protect 对象中定义了 IsVulnerable，则此时执行。如果受害者不易受攻击，则将扫描标记为“失败”，并继续到步骤 5。  
3) 如果受害者根据其对先前攻击的反应宣布自己对攻击免疫（参见“反应阶段”中的“future_immunity”评估处理），则将扫描标记为“失败”，并继续到步骤 5。  
4) 通过执行“scan_detection”的概率评估来确定受害者是否会检测到扫描（参见下面的概率评估）。  
5) 如果抽签小于或等于阈值，则扫描被受害者检测到，并且它将对未来同类型的攻击免疫。  
6) 将扫描标记为“失败”。  
7) 如果在攻击响应中提供了 OnScanDetection 脚本，则调用它。  
8) 调用 CyberScanDetected 观察者回调。

如果抽签大于阈值，则扫描未被受害者检测到，并且它可能对未来同类型的攻击易受攻击。

1) 将扫描标记为“成功”。  
2) 通过执行“scan_attribution”的概率评估来确定受害者是否会归因于扫描。  
3) 调用 CyberScanAttributed 观察者回调。  
4) 发出 WsfDraw 命令以记录可视化数据。  
5) 根据前面步骤确定的状态，调用 CyberScanSucceeded 或 CyberScanFailed 观察者回调。

这种详细的过程描述了 AFSIM 如何模拟网络攻击的各个阶段，特别是在扫描阶段如何评估和记录攻击的效果和响应。

# 交付阶段

在交付阶段，模拟将漏洞利用程序传递给受害者。攻击者调用 WsfPlatform.CyberAttack脚本方法，指定在“目标阶段”确定的目标和攻击类型。

在现实生活中，交付通常涉及攻击者和受害者之间的某种通信（有线或无线），尽管有些攻击可能嵌入在电路中。AFSIM 的网络交战模型不使用 AFSIM通信模型，因为修改现有场景以利用显式通信会很困难，而且要求它也不会带来太多好处。  
安排一个事件在 cyber_attack 类型的 delivery_delay_time 完成时发生。  
调用 CyberAttackInitiated 观察者回调。  
发出 WsfDraw 命令以记录可视化数据。  
在 delivery_delay_time 完成时，控制权转移到“利用”阶段。

注意：在未来的版本中，将添加文档以描述由于操作条件（可能是概率性的，也可能是几何的等）导致交付失败的处理。目前，交付总是会发生，处理将立即恢复到“利用”阶段。

# 利用阶段

在利用阶段，确定受害者是否易受请求攻击的影响。

1) 在受害者的 cyber_protect 对象中找到适用的 attack_response。  
2) 如果用户在受害者的 cyber_protect 对象中定义了 IsVulnerable，则此时执行。如果受害者不易受攻击，则将攻击标记为“失败”，并继续到步骤 6。  
3) 如果受害者根据其对先前攻击的反应宣布自己对攻击免疫（参见“反应阶段”中的“future_immunity”评估处理），则将攻击标记为“失败”，并继续到步骤 6（不向攻击者报告状态）。  
4) 通过执行“attack_success”的概率评估来确定攻击是否成功（参见下面的概率评估）。

□ 如果抽签小于或等于阈值，则攻击被认为是成功的。  
□ 如果抽签大于阈值，则攻击不成功。

5) 通过执行“status_report”的概率评估来确定攻击者是否会立即收到攻击状态的通知（参见下面的概率评估）。

□ 如果抽签小于或等于阈值，则攻击的真实状态会报告给攻击者。将状态报告给调用者。  
如果抽签大于阈值，攻击者将不知道攻击的状态。

6) 发出 WsfDraw 命令以记录可视化数据。