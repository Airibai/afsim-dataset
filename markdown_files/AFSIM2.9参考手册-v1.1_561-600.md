# 3.5.14. 超视距反射散射天波雷达 WSF_OTH_RADAR_SENSOR

```txt
sensor <name> WSF_OTH_RADAR_SENSOR
... Platform Part Commands ...
... Articulated Part Commands ...
... sensor Commands ...
show Calibration_data
mode <name>
... sensor Common Mode Commands ...
... WSF_RADAR_SENSOR Mode Commands ...
beam 1
Antenna Commands ...
transmitter
... transmitter commands ...
end_transmitter
receiver
... receiver commands ...
end_receive
... WSF_RADAR_SENSOR Beam Commands ...
... OTH Beam Commands ...
end_beam
beam <n>
Antenna Commands ...
transmitter
... transmitter commands ... 
end_transmitter   
receiver ... receiver commands ...   
end Receiver .. WSF_RADAR_SENSOR Beam Commands ... . OTH Beam Commands ... end_beam   
end_mode   
end_sensor 
```

WSF_OTH_RADAR_SENSOR 实现了一个基础的超视距反向散射（OTH-B）天波雷达。该雷达利用电离层反射能量，以检测超出视觉地平线的目标。此实现基于 Chapman 电离层模型，专注于电离层的 F 区域，特别是 F2 层，该区域具有最高的电子密度。

# OTH-B 雷达特性

单次反射：此实现仅支持单次反射。  
电离层反射：使用电离层反射来检测目标，特别是在 F2 层。

与 WSF_RADAR_SENSOR 类似：OTH 模式命令与 WSF_RADAR_SENSOR 的模式命令相同。

# OTH Beam 命令

noise environment <noise-environment-type>控制银河噪声、大气噪声和人为噪声的计算。仅在使用此命令时计算和应用噪声。

默认值： quiet_rural

solar_characteristics … end_solar_characteristics初始化一天中的时间和一年中的日期，以控制太阳赤纬角和太阳天顶角。

```txt
solar-characteristics  
hour_of_day <int>  
day_of_year <int>  
end_solar-characteristics 
```

默认值： 如果未指定，hour_of_day 和 day_of_year 分别默认为 12 和 1，即 1 月 1日 12:00。

ionosphere_characteristics … end_ionosphere_characteristics

初始化控制电离层反射发生的条件。

```c
ionosphere-characteristics  
electron_temperature <double>  
electron_density_at_max <double>  
electron_height_at_max <length>  
reflection_height <length>  
ionosphere_constrains_minimum_range <bool>  
end_ionosphere-characteristics 
```

□ electron_temperature: 电子温度，单位为开尔文。默认值为 1540 K。

▫ electron_density_at_max: 最大电子密度，单位为电子每立方米。默认值为 4.0e11。  
□ electron_height_at_max: 最大电子密度发生的高度。默认值为 $2 5 0 ~ \mathsf { k m }$ 。  
□ reflection_height: 用于计算电离层反射几何的高度。默认值为 $3 0 0 ~ { \mathsf { k m } }$ 。  
□ ionosphere_constrains_minimum_range: 是否使用计算的最小和最大范围。默认值为 false。

# OTH 反射点

可以通过传感器提供的轨迹上的 AuxDataDouble 方法访问电离层的估计反射点。示例：

```txt
double lat = track.AuxDataDouble("oth_reflection_point_lat");
double lon = track.AuxDataDouble("oth_reflection_point_lon");
double alt = track.AuxDataDouble("oth_reflection_point_alt"); 
```

# 其他信息

工作频率：通常使用高频（HF）无线电信号，频率在 2 到 30MHz 之间，以便在开放海洋区域超越地平线进行探测。

检测范围：OTH-B 雷达能够检测远超视觉或无线电地平线的大型物体，如大型飞机或小型飞机编队。

这种雷达技术利用电离层的反射特性，使其能够在极远距离上检测目标，适用于军事和远程监视应用。

# 3.5.15. 合成孔径雷达传感器 WSF_SAR_SENSOR

```txt
sensor <name> WSF_SAR_SENSOR Platform Part Commands ... ... sensor Commands ... WSF_SAR_SENSOR Common Commands ... mode <name> ... Antenna Commands ... transmitter Commands ... receiver Commands ... WSF_SAR_SENSOR Mode Commands end_mode end_sensor 
```

WSF_SAR_SENSOR 实现了一个基础的合成孔径雷达（SAR）传感器，支持“点”模式和“条”模式。SAR 是一种主动雷达传感器，能够在白天和夜晚以及大多数天气条件下观察地球表面。

# 输出

点模式：生成 WsfImage，包含在 WSF_IMAGE_MESSAGE 中。

条模式：生成 WSF_VIDEO_MESSAGE。  
输出通常发送到 WSF_IMAGE_PROCESSOR，该处理器将图像转换为轨迹，然后发送到WSF_TRACK_PROCESSOR 以纳入本地主轨迹列表。

# 传感器功能

光学特征：使用平台的 optical_signature 确定对象在图像中占据的像素数。  
雷达特征：使用 radar_signature 确定像素强度。  
使用注意事项  
视场命令：使用 azimuth_field_of_view 和 elevation_field_of_view 命令排除 3 dB 波束宽度之外的目标。  
最大范围：在条模式下，maximum_range 非常重要，可以通过限制传感器在采样间隔内查看的对象数量来显著提高性能。  
驻留时间或分辨率：必须定义 dwell_time 或 resolution。  
脉冲重复频率：如果未定义，将根据传感器开启或模式更改时的提示信息计算。

# 常见命令

▪ intensity_limits <db-power-value> min-db-power <db-power-value> max-db-power

指定用于将信号强度映射到归一化像素强度的范围。

intensity_range <db-power-value>

指定用于将信号强度映射到归一化像素强度的范围。

rescale_substandard_image <boolean-value>

仅用于“点”模式。指定是否应重新缩放“次标准图像”以使其像素的纵横比与“标准图像”相同。

默认值： true

show_calibration_data

如果指定，模型将在创建传感器时显示一般传感器性能数据。

show_status

如果指定，模型将在传感器状态更改时显示某些关键计算参数。

call_sensor_track_observers <boolean-value>

指定是否调用“传感器跟踪观察者”。如果为 true，将调用传感器跟踪观察者事件。

默认值： false

sar_constraint_plotting <boolean-value>

如果为 true，模型将内部移除某些内部限制，以允许使用 sensor_plot 的horizontal_map 函数正确创建“SAR 约束图”。

SAR 传感器通过使用合成孔径技术来提高分辨率，能够在各种环境条件下提供高质量的地面成像。

# 模式命令

WSF_SAR_SENSOR 支持两种操作模式：点模式和条模式。这些模式通过 operating_mode命令指定。

operating_mode [ spot | strip ]

点模式：传感器开启时，将对当前提示位置进行训练，并形成图像。图像将在传感器关闭时交付，可能是由于 automatic_turn_off 或显式外部请求（WsfSensor.TurnOff）导致的。

条模式：传感器将连续更新“图像”，仅包括自上次采样以来检测到的对象。

默认值： spot.

automatic_turn_off

仅用于点模式。如果指定，传感器将在 dwell_time 或形成分辨率至少为 resolution 的图像所需的时间后自动关闭。

默认值： 传感器必须由应用程序关闭。

resolution <length-value>

指定图像单元/像素的期望横向分辨率。用于计算形成指定横向分辨率图像所需的驻留时间。

注意： 地面分辨率由发射器的 pulse_width 和 pulse_compression_ratio 决定。如果未定义脉冲宽度，则将其计算为接收器带宽的倒数。

默认值： 无默认值。必须指定 dwell_time 或 resolution。

dwell_time <time-value>

指定“采集时间”，即传感器将在位置上驻留以形成图像的时间。这也用于预测横向分辨率。

默认值： 无默认值。必须指定 dwell_time 或 resolution。

maximum_dwell_time <time-value>

仅用于点模式。如果指定，计算出的驻留时间将限制为此值。

默认值： 999 秒

minimum_clutter_to_noise_ratio <ratio>

仅用于点模式。指定低于此值的杂波与噪声比，图像将被声明为“次标准”。

inhibit_substandard_collection <boolean-value>

仅用于点模式。如果为 true，则如果所需分辨率的内部计算杂波与噪声比低于minimum_clutter_to_noise_ratio，则抑制图像采集请求。

默认值： 图像采集不会被抑制。

# 其他命令

maximum_detectable_speed <speed-value>

指定对象可以移动的最大速度，并且仍然存在于图像中。

默认值： $2 \mathsf { m } / \mathsf { s }$

doppler_filter_broadening_factor <unitless-value>

考虑到多普勒滤波器没有矩形加权，略微加宽滤波器以控制能量“渗入”相邻滤波器。默认值： 1.0

image_width <length-value> / image_height <length-value>

分别指定 SAR 图像区域在地面上的宽度和高度。

默认值： 0m（使用方位和仰角视场）

sar_error_model_parameters … end_sar_error_model_parameters

调用范围和多普勒误差计算以生成 SAR 目标位置误差（TLEs）。

这些命令和参数帮助配置 WSF_SAR_SENSOR 的性能，以便在不同的环境条件下进行有效的目标检测和成像。

# 3.5.16. 超视距地波雷达 WSF_SURFACE_WAVE_RADAR_SENSOR

```txt
sensor <name> WSF_SURFACE_WAVE_RADAR_SENSOR
... Platform Part Commands ...
... Articulated Part Commands ...
... sensor Commands ...
mode <name>
... Sensor Mode Commands ...
... WSR_RADAR_SENSOR Beam Commands ...
... WSF_SURFACE_WAVE_RADAR_SENSOR Commands ...
end_mode
end SENSOR 
```

WSF_SURFACE_WAVE_RADAR_SENSOR 实现了一种超视距雷达，依赖于沿地球表面传播的射频能量（即，不依赖于电离层反向散射）。这种雷达系统能够检测远距离目标，通常用于监测海洋和沿海地区的船只和飞机。

# 检测能力

外部噪声驱动：这些雷达的检测能力主要受外部噪声影响，包括银河噪声、大气噪声和人为噪声。

□ 银河噪声：与雷达的工作频率有关。  
□ 大气噪声：与雷达的工作位置、季节和时间有关。  
□ 人为噪声：与雷达位置附近的人为环境有关。

噪声计算：传感器使用模拟的日期和时间（由模拟控制命令指定）来确定适当的大气噪声。

# 地面波传播

GRWAVE 程序：地面波传播是 GRWAVE FORTRAN 代码的 ${ \mathsf { C } } { + } { + }$ 移植，来自国际电信联盟（ITU）无线电通信部门第 3 研究组（无线电波传播）。GRWAVE 程序和文档可以从ITU 网站获取。

# 命令

transmitter … end_transmitter定义发射器属性的块。地面波雷达传感器有一个独特的传播模型。  
propagation_model groundwave_propagation … end_propagation_model定义地面波传播模型的参数。

□ relative_permittivity <number>地球表面的相对介电常数。

默认值： 70.0（海洋）

□ conductivity <number>地球表面的电导率（西门子/米）。

默认值： 5.0

□ troposphere_refractivity <number>

地球表面对流层的折射率（N 单位）。

默认值： 315.0

▫ troposphere_height_scale <length-value>

对流层的尺度高度。

默认值： $7 . 3 5 ~ \mathsf { k m }$

□ minimum_computation_distance <length-value>

传播计算的最小距离。

默认值： $1 0 . 0 \mathrm { k m }$

□ computation_distance_interval <length-value>

传播计算的距离间隔。

默认值： $1 0 . 0 \mathrm { k m }$

noise_environment [ business | residential | rural | quiet_rural ]

定义传感器操作的人为噪声环境。

默认值： quiet_rural

# 其他信息

工作频率：地面波雷达通常在高频（HF）范围内工作，频率可达 $5 0 ~ \mathsf { M H z }$ 。  
应用：这种雷达技术适用于监测海洋和沿海地区的船只和飞机，提供远距离目标检测能力。

这种雷达系统通过利用地面波传播特性，能够在不依赖电离层反射的情况下实现超视距目标检测，适用于海洋监测和国土安全应用。

# 3.5.17. 多传感器模型 WSF_MULTIRESOLUTION_SENSOR

```txt
multiresolution_sensor WSF MultiresOLUTION SENSOR ... multiresolution_sensor ... endMULTIRESOLUTION_sensor 
```

multiresolution_sensor 定义了一个容器，用于在平台上保存一个或多个传感器（sensor）对象，并将选择使用哪个 sensor 推迟到运行时。选择 sensor 是通过与组件关联的 fidelity 参数来完成的。容器中定义的每个 sensor 模型都分配了一个 fidelity_range，在初始化期间根据匹配的 fidelity 设置平台上的 sensor。

# 使用方法

定义新类型: 可以在 platform 或 platform_type 命令之外使用 multiresolution_sensor 来定义新类型。

```c
multiresolution_sensor <derived> WSFMULTIRESOLUTION_SENSOR 
```

```txt
fidelity <real-value>   
[add | edit] model <string-value> fidelity_range <real-value> <real-value> [default] sensor [<sensor-type>] ... sensor-specific commands ... 
```

```txt
end_sensor  
end_model  
[add | edit] model <string-value>  
... Any number of models may be specified ...  
end_model  
common  
... sensor-specific commands ...  
end_common  
endMULTIRESOLUTION_sensor 
```

实例化对象: 可以在 platform_type 或 platform 实例上实例化一个 multiresolution_sensor 对象。实例化时需要提供一个名称。

```txt
platform_type ...
multiresolution_sensor <name> <type>
... multiresolution_sensor commands ...
endMULTIRESOLUTION SENSOR
endPLATFORM_TYPE 
```

```txt
platform ...
    add multiresolution_sensor <name> <type>
        ... multiresolution_sensor commands ...
    endMULTIRESOLUTION_SENSOR
endplatform 
```

修改现有对象: 可以在 platform 实例上修改现有的 multiresolution_sensor 对象。

```matlab
platform ...
    edit multiresolution_sensor <name> <type>
        ... multiresolution_sensor commands ...
    endMULTIRESOLUTION_sensor
endplatform 
```

# 命令

fidelity <real-value>: 定义组件的 fidelity 值，决定在运行时使用哪个 sensor。必须在 0到 1 之间（包括 0 和 1）。此值直接映射到模型命令中定义的 fidelity_range。

默认值: 1.0

model <string-value> ... end_model: 定义或编辑包含的 sensor 模型，名称由字符串给出。支持隐式添加（或编辑如果命名模型存在）以及使用 add 和 edit 命令的显式添加和编辑。

注意: 必须至少指定一个模型块。

fidelity_range <real-value> <real-value>: 定义此模型应使用的 fidelity 值范围。必须在 0到 1 之间（包括 0 和 1），按递增顺序排列，并且不得与此组件上的另一个模型的fidelity_range 重叠。

默认值: 0.0 1.0

default: 如果没有匹配的 fidelity，则使用此模型作为默认选择。  
sensor <sensor-type> ... end_sensor: 定义 sensor 模型的类型和特定于此模型实例化的参数。在首次定义新模型时需要 sensor，在编辑现有模型时不得指定。  
common ... end_common: 定义要转发到所有当前指定的 sensor 模型的通用参数。这些参数必须对所有当前定义的 sensor 模型有效。

# 说明

多分辨率分析: 这种方法允许在不同的分辨率下分析和选择合适的 sensor 模型，以便在不同的场景中优化传感器性能。  
未来改进: 计划在场景文件的其他位置提供 fidelity 选择，以提高此组件的实用性。

# 3.6. 运动组件 Mover

```txt
mover Mover Types ...  
... Platform Part Commands ...  
update_interval <time-reference>  
update_time_tolerance <time-reference>  
end_mover 
```

Mover 是一个组件，它定义了平台可以移动的域以及平台在该域内如何移动。换句话说，每种 Mover 类型定义了平台在模拟运行期间的移动行为。WSF 中存在几种预定义的Mover 类型，可以放置在平台上。一个平台只能定义一种 Mover 类型。可以在平台外部定义基础 Mover 以供多个 platform_types 使用。

Mover 的公共命令仅有两个如下：

<table><tr><td>命令</td><td>update_interval &lt;time-reference&gt;</td></tr><tr><td>解释</td><td>如果非零，指定模拟将调用Mover的周期时间间隔。如果为零，则仅在需要确定包含平台的位置时调用Mover。默认值：0秒，除非特定Mover实现覆盖。</td></tr><tr><td>命令</td><td>update_time_tolerance &lt;time-reference&gt;</td></tr><tr><td>解释</td><td>当模拟请求位置更新时，如果自上次更新以来的时间小于或等于此值，则Mover将忽略更新。默认值：大多数Mover实现将其定义为以某个适当的名义速度行驶1米所需的时间。注意：Mover实现可能会选择忽略此命令。</td></tr></table>

Mover 官方的分类也是五花八门，有时候自相矛盾，以下是对各类 Mover 的简要介绍，在本节的分小节针对每个 Mover 的更详细的介绍有助于全面的掌握每个 Mover。

# 路线类型 Mover

这些 Mover 是简化的 Mover，可以定义带有航点的路线，以便它们在模拟期间从一个位置移动到另一个位置。平台上的限制定义了它们的移动。平台移动基于数学计算，而不一定是平台的空气动力学或质量属性。

```txt
WSF_SUBSURFACE_MOVER  
WSF_P6DOF_MOVER 
```

# 跟随类型 Mover

这些 Mover 附加到路线类型 Mover 上，用于使平台实例“跟随”其他平台。

```txt
WSFFormation_FLYER  
WSF_TOWED_MOVER 
```

# 轨迹类型 Mover

这些 Mover 引导到轨迹，移动基于平台的空气动力学和质量属性。此类型的 Mover 通常用于在模拟中定义武器的移动。除了 WSF_STRAIGHT_LINE_MOVER 外，平台必须知道质量属性、空气动力学、推力和推力持续时间。即使轨迹的范围或速度值有轻微变化，运行结果的轨迹也可能显著不同。三种 Mover 类型是外部定义的。

```txt
WSF GUIDED_MOVER  
WSF Unguided MOVER  
WSF STRAIGHT_LINE_MOVER 
```

# 简化弹道类型 Mover

这些 Mover 提供了一种定义平台的抛物线或弹道轨迹的方法。

```txt
WSF_FIRESMOVER  
WSF_PARABOLIC_MOVER  
WSF_TB_MOVER 
```

# 高保真类型 Mover

这些 Mover 是详细的 Mover，支持基于物理的运动学，包括姿态（航向、俯仰和滚动）以及高度效应。平台移动完全基于数学计算，包括平台的详细空气动力学、推进和质量属性。这些 Mover 通常可以跟随航点路线，但也提供其他控制选项。

```txt
WSF_P6DOF_MOVER 
```

以下是对所有的系统预置的 Mover 的更全面的分类：

# 路线类型

这些 Mover 是简化的 Mover，可以定义带有航点的路线，以便它们在模拟期间从一个位置移动到另一个位置。平台上的限制定义了它们的移动。平台移动基于数学计算，而不一定是平台的空气动力学或质量属性。

```txt
WSF_AIR_MOV  
WSFGROUND_MOV  
WSF_KINEMATIC_MOV  
WSFROAD_MOV  
WSF_ROTORCRAFT_MOV  
WSF_SURFACE_MOV 
```

WSF_TSPI_MOVER

# 跟随类型

这些 Mover 附加到路线类型 Mover 上，用于使平台实例“跟随”其他平台。

WSF_HYBRID_MOVER

WSF_OFFSET_MOVER

# 六自由度类型

WSF_RIGID_BODY_SIX_DOF_MOVER

WSF_POINT_MASS_SIX_DOF_MOVER

# P-6DOF 类型

WSF_P6DOF_MOVER

# ARGO8 类型

WSF_ARGO8_MOVER

# 卫星/轨道类型

这些 Mover 使用分析模型传播其附加的平台。

WSF_NORAD_SPACE_MOVER

WSF_SPACE_MOVER

此 Mover 使用数值模型传播其附加的平台。

WSF_INTEGRATING_SPACE_MOVER

# Brawler 类型

WSF_BRAWLER_MOVER

# 军事类型

WSF_FIRES_MOVER

WSF_FORMATION_FLYER

WSF_GUIDED_MOVER

WSF_PARABOLIC_MOVER

WSF_STRAIGHT_LINE_MOVER

WSF_SUBSURFACE_MOVER

WSF_TBM_MOVER

WSF_TOWED_MOVER

WSF_UNGUIDED_MOVER

# 3.6.1. 路线类型 RouteTypes

这些 Mover 是简化的 Mover，可以定义带有航点的路线，以便它们在模拟期间从一个位置移动到另一个位置。平台上的限制定义了它们的移动。平台移动基于数学计算，而不一定是平台的空气动力学或质量属性。

# 3.6.1.1. 空中运动模型 WSF_AIR_MOVER

```txt
mover WSF_AIR_MOVER Platform Part Commands //Mover Commands update_interval update_time_tolerance //Route Mover Commands altitude_offset at_end_of_path draw-route on_turn FAILURE pathfinder print-route start_at start_time switch_onapproach switch_on_passing turn FAILURE_threshold useROUTE //Waypoint Mover Commands angle_of_attack_table altitude speed angle bank_angle_limit body_g_limit heading_pursuit_gain maximum_climb_rate maximum_airight_path_angle maximum_LINEARacceleration maximum_radialacceleration maximum_altitude minimum_altitude maximum_speed minimum_speed path_variance_radius roll_rate_limit 
```

```txt
speed-variance_percent   
turn_rate_limit   
pitch_disable   
no_pitch   
on_road   
off_road   
path_compute_timestep   
//Air Mover Commands   
maximum_impact_speed   
end_mover 
```

WSF_AIR_MOVER 是 一 种 为简 化 空 中 载 具运 动 而 设 计 的路 线 Mover。 使 用WSF_AIR_MOVER 的优点在于，无需了解平台的质量属性、空气动力学或推进系统即可模拟空体运动。运动基于为各种参数（如线性加速度、速度、G 力、径向加速度）设置的最大限制，但仅适用于水平面的连续运动。WSF_AIR_MOVER 的限制在于平台的垂直过渡（高度变化）。这些过渡是不连续的，因为不对过渡的垂直俯仰率和垂直加速度进行建模。如果希望平台具有连续和平滑的垂直和水平过渡，请使用 WSF_KINEMATIC_MOVER（如果不需要空气动力学、质量属性、推进或高度效应）或 WSF_P6DOF_MOVER（如果需要真实的基于物理的建模）。

# Mover 全局命令

<table><tr><td>命令</td><td>update_interval &lt;time-value&gt;</td></tr><tr><td>解释</td><td>如果非零，指定模拟调用Mover的周期时间间隔。如果为零，则仅在需要确定包含平台的位置时调用Mover。
默认值：0秒，除非特定Mover实现覆盖。</td></tr><tr><td>命令</td><td>update_time_tolerance &lt;time-value&gt;</td></tr><tr><td>解释</td><td>当模拟请求位置更新时，如果自上次更新以来的时间小于或等于此值，则Mover将忽略更新。
默认值：大多数Mover实现将其定义为以某个适当的名义速度行驶1米所需的时间。
注意：Mover实现可能会选择忽略此命令。</td></tr></table>

# 路线 Mover 命令

<table><tr><td>命令</td><td>altitude_offset &lt;length-value&gt;</td></tr><tr><td>解释</td><td>设置时,此偏移量将使父平台的位置偏移当前航点高度的指定量。</td></tr><tr><td>命令</td><td>at_end_of_path [extrapolate | stop | remove]</td></tr><tr><td>解释</td><td>指定当 Mover 到达其定义路径的末端时要采取的操作。extrapolate: 继续以最后已知的航向、速度和高度移动。stop: 停止移动,但将平台保留在模拟中。remove: 从模拟中移除平台。默认值: extrapolate</td></tr><tr><td>命令</td><td>draw-route &lt;boolean-value&gt;</td></tr><tr><td>解释</td><td>此命令与 print_route 相同,只是路线文本不打印,仅通过 WsfDraw 绘制。</td></tr><tr><td>命令</td><td>on_turnfailure [best_effort | reverse_turn | ignore_point]</td></tr><tr><td>解释</td><td>定义当由于转弯半径无法准确到达路径上的某个点时Mover的行为。best_effort:转弯直到平台到达最接近该点的位置。ignore_point:Mover实际上忽略该点。当跳过该点时,任何与该点相关的脚本都会执行。reverse_turn:Mover将向相反方向转弯,使其能够准确到达该点。注意:如果Mover给出的路径在其约束范围内,此命令无效。默认值:best_effort</td></tr><tr><td>命令</td><td>pathfinder</td></tr><tr><td>解释</td><td>要使用的路径查找器对象的名称。</td></tr><tr><td>命令</td><td>print-route</td></tr><tr><td>解释</td><td>启用时,每当路径被修改时,路线将打印到屏幕上。此外,WsfDraw将用于输出路线的可视化,可以通过许多可视化工具查看。</td></tr><tr><td>命令</td><td>start_at</td></tr><tr><td>解释</td><td>标识路径中航点的标签,用作起始位置。</td></tr><tr><td>命令</td><td>start_time</td></tr><tr><td>解释</td><td>指示平台在指定时间开始移动。当前速度设置为零,一旦达到模拟时间,平台将以第一个航点指定的速度开始移动。如果希望在航点处有一个延迟时间,请使用子命令pause_time。</td></tr><tr><td>命令</td><td>switch_onapproach</td></tr><tr><td>解释</td><td>当接近当前目标航点的一个转弯半径范围内时切换到下一个航点。</td></tr><tr><td>命令</td><td>switch_on_passing</td></tr><tr><td>解释</td><td>仅当通过当前目标航点时切换到下一个航点。注意:这是默认设置。</td></tr><tr><td>命令</td><td>turn_failure_threshold</td></tr><tr><td>解释</td><td>定义触发on_turn_failure行为的阈值,作为转弯半径的比率。例如,转弯半径为1000米,turn_failure_threshold为0.01,则如果错过该点超过10米,将触发on_turn_failure 逻辑。默认值:0.01</td></tr><tr><td>命令</td><td>use-route</td></tr><tr><td>解释</td><td>提供要遵循的路径的名称。假定路径是预定义的绝对路径。参见:4.8.1路由route</td></tr></table>

# 航点 Mover 命令

<table><tr><td>命令</td><td>angle_of_attack_table...end_angle_of_attack_table</td></tr><tr><td>解释</td><td>定义攻角表。altitude:指定后续数据有效的高度。高度块必须按递增数值顺序排列。使用高度块的线性插值。speed:指定列出的攻角有效的速度。速度条目必须按递增数值顺序排列。攻角将使用速度数据的线性插值计算。angle:攻角。攻角条目必须按递增数值顺序排列。</td></tr><tr><td>命令</td><td>bank_angle_limit&lt;angle-value&gt;</td></tr><tr><td>解释</td><td>滚转角度限制。值必须在0度到85度之间。用于计算最大径向加速度。默认值:0</td></tr><tr><td>命令</td><td>body_g_limit&lt;acceleration-value&gt;</td></tr><tr><td>解释</td><td>体g限制。值必须大于地球重力加速度。</td></tr><tr><td>命令</td><td>heading_pursuit_gain&lt;double-value&gt;</td></tr><tr><td>解释</td><td>航向追踪增益。默认值:5</td></tr><tr><td>命令</td><td>maximum_climb_rate&lt;speed-value&gt;</td></tr><tr><td>解释</td><td>指定更改高度时使用的最大爬升率和俯冲率。航点或脚本指定的其他爬升率受此值约束。注意:Mover的实际爬升率也会受到‘maximum_attack_path_angle'的影响。</td></tr><tr><td>命令</td><td>maximum_attack_path_angle&lt;angle-value&gt;</td></tr><tr><td>解释</td><td>指定最大飞行路径角(爬升/俯冲角)。值必须大于或等于0。</td></tr><tr><td></td><td>注意：Mover的实际爬升率也会受到‘maximum_climb_rate'的影响。默认值：0</td></tr><tr><td>命令</td><td>maximum_linearacceleration&lt;acceleration-value&gt;</td></tr><tr><td>解释</td><td>指定加速时使用的最大线性加速度。如果航点不包括线性加速度规范，则使用此值。默认值：6g's</td></tr><tr><td>命令</td><td>maximum_radialacceleration&lt;acceleration-value&gt;</td></tr><tr><td>解释</td><td>指定转弯时使用的最大径向加速度。如果航点不包括径向加速度规范，则使用此值。默认值：6g's注意：径向加速度不是飞机的负载因子。例如，如果希望最大负载因子为n=2对于2g转弯，则希望的2g转弯限制的径向加速度需要设置为=g*√n²-1=1.732g</td></tr><tr><td>命令</td><td>maximum_altitude&lt;altitude-value&gt;</td></tr><tr><td>解释</td><td>最大高度限制。</td></tr><tr><td>命令</td><td>minimum_altitude&lt;altitude-value&gt;</td></tr><tr><td>解释</td><td>最小高度限制。</td></tr><tr><td>命令</td><td>maximum_speed&lt;speed-value&gt;</td></tr><tr><td>解释</td><td>最大速度限制。值必须大于0。</td></tr><tr><td>命令</td><td>minimum_speed&lt;speed-value&gt;</td></tr><tr><td>解释</td><td>最小速度限制。值必须大于或等于0。默认值：0.0</td></tr><tr><td>命令</td><td>path_variance_radius&lt;length-value&gt;</td></tr><tr><td>解释</td><td>此值将在给定半径范围内随机变化航点的位置。计算路径时选择并应用随机方位和距离到下一个航点。</td></tr><tr><td>命令</td><td>roll_rate_limit&lt;angle-rate-value&gt;</td></tr><tr><td>解释</td><td>滚转率限制。值必须大于0。注意：当应用于WSF_AIR_MOVER或其他航点Mover类型时，滚转率不会影响平台沿路线的移动。要影响路线跟随行为，请使用maximum_radialacceleration。</td></tr><tr><td>命令</td><td>speed_variance_percent&lt;percent-value&gt;</td></tr><tr><td>解释</td><td>此值将在给定的百分比范围内随机变化每个航点的速度。值必须大于0。</td></tr><tr><td>命令</td><td>turn_rate_limit&lt;angle-rate-value&gt;</td></tr><tr><td>解释</td><td>转弯率限制。值必须大于0。</td></tr></table>

# 其它命令

<table><tr><td>命令</td><td>pitch_disable</td></tr><tr><td>解释</td><td>no_pitch 限制 Mover 使平台俯仰。这对运动学没有影响。</td></tr><tr><td>命令</td><td>on_road</td></tr><tr><td>解释</td><td>限制 Mover 使平台滚转。这对运动学没有影响。</td></tr><tr><td>命令</td><td>off_road</td></tr><tr><td>解释</td><td>关闭&#x27;on_road&#x27;选项。这允许平台滚转。</td></tr><tr><td>命令</td><td>path_compute timestep &lt;time-value&gt;</td></tr><tr><td>解释</td><td>航点 Mover 预先计算沿路径的移动。此行为强制转弯具有恒定半径。如果 path_compute timestep 指定为正值,则如果速度发生任何变化,转弯率将在该间隔内更新。默认值:0.0</td></tr></table>

# 最大值和默认命令的注意事项

Movers 有各种命令指定最大值，如 maximum_linear_acceleration。这些命令指定在整个模拟过程中不会超过的总体限制。有一些默认命令，如 default_linear_acceleration。这些命令指定除非在路线或脚本中另有规定，否则使用的速率。这些参数可以省略，使 Mover 默认使用最大速率。速率可以在模拟期间通过路线（如 linear_acceleration 命令）或脚本（如GoToSpeed() 方法）进行修改。速率保持不变，直到被另一个脚本或路线更改。路线提供了一种返回默认速率的机制，如使用 linear_acceleration 默认命令。

空中 Mover 命令  

<table><tr><td>命令</td><td>maximum_impact_speed &lt;speed-value&gt;</td></tr><tr><td>解释</td><td>在模拟平台的背景下，平台被认为是“撞向地面”而不是“着陆”的最大速度并未在提供的信息中明确说明。然而，模拟中的一般原则是，平台与地面的交互取决于其速度和撞击角度。从现有信息中，我们可以推断：高速撞击：如果平台以高速与地形相交，它将被认为是碰撞。这与极端的地面碰撞会产生显著的力，导致碰撞情景的概念相一致。低速撞击：如果撞击速度低于某个阈值，平台将被认为是着陆。这与所提到的默认行为一致，即平台总是着陆而非碰撞，除非速度过大。通知和移除当平台撞向地面时，它会通过 WsfSimulationObserver::CrashedIntoGround() 方法通知观察者，并随后将自己从模拟中移除。这确保了模拟准确反映平台的状态，并防止已碰撞实体的进一步交互。默认行为模拟的默认行为是总是着陆而非碰撞，除非撞击速度超过安全着陆的最大阈值。这种方法优先考虑模拟环境的连续性和稳定性。</td></tr></table>

# 3.6.1.2. 低保真空中运动模型 WSF_MATH_3D_MOVER

```batch
mover WSF_MATH_3D_MOVER Platform Part Commands ... .. WSF_MATH_3D_MOVER Commands .. // Route Mover Commands use-route ...   
end_mover 
```

WSF_MATH_3D_MOVER 是一种低保真度的空中移动器，类似于 WSF_AIR_MOVER。然而，WSF_AIR_MOVER 在结合横向和垂直机动时发现运动不平滑，因此需要这种替代方案。其底层动力学模型本质上是一个四元数方向，仅允许在惯性空间中以受限的角速度旋转，速度矢量则指向该四元数的“前方”方向。没有建模空气动力学或推进力，这允许在横向和垂直方向上进行平滑转弯。加速度的大小由内部追踪和比例导航增益决定，三维空间中的目标点由路线移动器的航路点切换逻辑确定。

# 特点

平滑运动: 通过使用四元数方向和受限的角速度旋转，实现横向和垂直方向的平滑转弯。  
无空气动力学或推进力建模: 仅依赖于内部追踪和比例导航增益来确定加速度。  
航路点响应: 响应纬度、经度和海平面高度（MSL）的航路点，并遵循速度命令。  
忽略其他命令: 忽略航向、距离、时间、爬升率、飞行路径角和加速度命令。

# 速度矢量转弯率

转弯率受以下因素的限制：

maximum_lateral_acceleration: 最大横向加速度。  
maximum_axial_body_roll_rate: 最大轴向机体滚转率。  
maximum_axial_body_turn_rate: 最大轴向机体转弯率。

随着平台速度的增加，如果保持最大横向加速度不变，平台运动将趋向于直线。

# 增益设置

velocity_pursuit_gain (VP) 和 proportional_navigation_gain (PN): 这两个增益可能会相互冲突，找到合适的值可能需要反复试验。  
VP: 开始时将 PN 设置为零，VP 设置为小值，然后逐渐增加 VP，直到转弯的积极性足以拦截目标点。  
PN: 对于移动或加速的目标运动，纯 VP 将导致从后方接近目标的扫掠转弯。此时，开始增加 PN，直到平台“预判”撞击点，并以直线飞行拦截（假设目标也在直线移动）。

# 使用说明

use_route: 使用航路命令来定义移动路径。

以下是 WSF_MATH_3D_MOVER 的命令列表及其功能：

detailed_debug <boolean-value>: 启用或禁用标准输出的调试输出。布尔值可以是 true或 false，表示是否启用调试。  
prefer_canopy_up <boolean-value>: 使 平 台 始 终 滚 转 到 局 部 垂 直 方 向 。 此 选 项 与bank_to_turn 互斥。  
bank_to_turn <boolean-value>: 使平台滚转到加速度矢量中，但在不加速转弯时仍偏向垂直。此选项与 prefer_canopy_up 互斥。  
broach_at_sea_level <boolean-value>: 确保一旦进入水下，运动必须保持在当地海平面以下。  
target_speed <speed-value>: 一 旦 提 供 ， 平 台 将 加 速 或 减 速 以 匹 配 目 标 速 度 ， 受maximum_linear_acceleration 约束。  
initial_speed <speed-value>: 初始线速度。初始化后，速度会变化以保持 target_speed。  
initial_flight_path_angle <angle-value>: 初始飞行路径角。初始化后，飞行路径角将变化以引导到所需的航路点。  
maximum_linear_acceleration <acceleration-value>: 定义线性（速度方向）加速度限制约束。默认值为 $_ { 0 . 2 5 \ : 6 }$ 。  
maximum_lateral_acceleration <acceleration-value>: 定义横向（垂直于速度方向）加速度限制约束。此约束与 maximum_axial_body_turn_rate 同时施加，使用最严格的限制。默认值为 $8 . 0 \ G$ 。  
maximum_axial_body_roll_rate <angular-rate-value>: 定义平台尝试捕获目标滚转角的最大速率。默认值为 180 度/秒。  
maximum_axial_body_turn_rate <angular-rate-value>: 定义速度矢量在三维空间中旋转的最大速率。此约束与 maximum_lateral_acceleration 同时施加，使用最严格的限制。默认值为 45 度/秒。  
velocity_pursuit_gain <non-negative-value>: 定义目标方位角和仰角（以弧度为单位）与施加的横向或垂直加速度（以米/秒²为单位）之间的比例因子，以使速度矢量指向目标。

默认值为 4.0。

proportional_navigation_gain <non-negative-value>: 定义目标视线速率（以弧度/秒为单位）与施加的横向或垂直加速度（以米/秒²为单位）之间的比例因子，以使速度矢量拦截目标在拦截时的未来位置。默认值为 40.0。  
use_route<route-name>: 提供要遵循的航路名称。假定航路是预定义的绝对航路。

这些命令允许用户在 AFSIM 中灵活地配置和管理平台的运动特性，从而更好地模拟和分析空中移动器的行为。

# 3.6.1.3. 地面运动模型 WSF_GROUND_MOVER

```txt
mover WSFGROUND_MOVER Platform Part Commands //Mover Commands update_interval update_time_tolerance //Route Mover Commands altitude_offset at_end_of_path draw-route on_turn FAILURE pathfinder print-route start_at start_time switch_onapproach switch_on_passing turn FAILURE_threshold useROUTE //Waypoint Mover Commands angle_of_attack_table altitude speed angle bank_angle_limit body_g_limit heading_pursuit_gain maximum_climb_rate maximum_airight_path_angle maximum_LINEARacceleration maximum_radialacceleration maximum_altitude minimum_altitude 
```

```txt
maximum_speed minimum_speed path_variance_radius roll_rate_limit speed_variance_percent turn_rate_limit pitch_disable no_pitch on_road off_road path_compute_timestep end_mover 
```

概述

实现一个用于地形跟踪地面 vehicle 的移动器。WSF_GROUND_MOVER 是一个路线移动器。

# Mover 全局命令

<table><tr><td>命令</td><td>update_interval &lt;time-value&gt;</td></tr><tr><td>解释</td><td>如果非零，指定模拟调用Mover的周期时间间隔。如果为零，则仅在需要确定包含平台的位置时调用Mover。
默认值：0秒，除非特定Mover实现覆盖。</td></tr><tr><td>命令</td><td>update_time_tolerance &lt;time-value&gt;</td></tr><tr><td>解释</td><td>当模拟请求位置更新时，如果自上次更新以来的时间小于或等于此值，则Mover将忽略更新。
默认值：大多数Mover实现将其定义为以某个适当的名义速度行驶1米所需的时间。
注意：Mover实现可能会选择忽略此命令。</td></tr></table>

# 路线 Mover 命令

<table><tr><td>命令</td><td>altitude_offset &lt;length-value&gt;</td></tr><tr><td>解释</td><td>设置时,此偏移量将使父平台的位置偏移当前航点高度的指定量。</td></tr><tr><td>命令</td><td>at_end_of_path [extrapolate | stop | remove]</td></tr><tr><td>解释</td><td>指定当 Mover 到达其定义路径的末端时要采取的操作。 extrapolate: 继续以最后已知的航向、速度和高度移动。 stop: 停止移动,但将平台保留在模拟中。 remove: 从模拟中移除平台。 默认值: extrapolate</td></tr><tr><td>命令</td><td>draw-route &lt;boolean-value&gt;</td></tr><tr><td>解释</td><td>此命令与 print-route 相同,只是路线文本不打印,仅通过 WsfDraw 绘制。</td></tr><tr><td>命令</td><td>on_turn_failure [best_effort | reverse_turn | ignore_point]</td></tr><tr><td>解释</td><td>定义当由于转弯半径无法准确到达路径上的某个点时 Mover 的行为。 best_effort: 转弯直到平台到达最接近该点的位置。 ignore_point: Mover 实际上忽略该点。当跳过该点时,任何与该点相关的脚本都会执行。 reverse_turn: Mover 将向相反方向转弯,使其能够准确到达该点。 注意:如果 Mover 给出的路径在其约束范围内,此命令无效。默认值: best_effort</td></tr><tr><td>命令</td><td>pathfinder</td></tr><tr><td>解释</td><td>要使用的路径查找器对象的名称。</td></tr><tr><td>命令</td><td>print-route</td></tr><tr><td>解释</td><td>启用时,每当路径被修改时,路线将打印到屏幕上。此外,WsfDraw 将用于输出路线的可视化,可以通过许多可视化工具查看。</td></tr><tr><td>命令</td><td>start_at</td></tr><tr><td>解释</td><td>标识路径中航点的标签,用作起始位置。</td></tr><tr><td>命令</td><td>start_time</td></tr><tr><td>解释</td><td>指示平台在指定时间开始移动。当前速度设置为零,一旦达到模拟时间,平台将以第一个航点指定的速度开始移动。如果希望在航点处有一个延迟时间,请使用子命令 pause_time。</td></tr><tr><td>命令</td><td>switch_onTONapprox</td></tr><tr><td>解释</td><td>当接近当前目标航点的一个转弯半径范围内时切换到下一个航点。</td></tr><tr><td>命令</td><td>switch_on Passing</td></tr><tr><td>解释</td><td>仅当通过当前目标航点时切换到下一个航点。注意:这是默认设置。</td></tr><tr><td>命令</td><td>turnfailure_threshold</td></tr><tr><td>解释</td><td>定义触发 on_turngilru行为的阈值,作为转弯半径的比率。例如,转弯半径为1000米,turn_failure_threshold 为0.01,则如果错过该点超过10米,将触发on_turn_failure 逻辑。默认值:0.01</td></tr><tr><td>命令</td><td>use-route</td></tr><tr><td>解释</td><td>提供要遵循的路径的名称。假定路径是预定义的绝对路径。参见:4.8.1 路由 route</td></tr></table>

# 航点移动器命令

<table><tr><td>命令</td><td>angle_of_attack_table ... end_angle_of_attack_table</td></tr><tr><td>解释</td><td>altitude &lt;altitude-value&gt;: 指定后续数据有效的高度。高度块必须按数值升序排列。使用线性插值计算高度块。speed &lt;speed-value&gt;: 指定有效的攻角速度。速度条目必须按数值升序排列。攻角将使用速度数据的线性插值计算。angle &lt;angle-value&gt;: 攻角。攻角条目必须按数值升序排列。end_angle_of_attack_table</td></tr><tr><td>命令</td><td>bank_angle_limit &lt;angle-value&gt;</td></tr><tr><td>解释</td><td>滚转角度限制。值必须在0度到85度之间。用于计算最大径向加速度。默认值: 0</td></tr><tr><td>命令</td><td>body_g_limit &lt;acceleration-value&gt;</td></tr><tr><td>解释</td><td>机体g极限。值必须大于地球重力加速度。</td></tr><tr><td>命令</td><td>heading_pursuit_gain &lt;double-value&gt;</td></tr><tr><td>解释</td><td>航向追踪增益。默认值: 5</td></tr><tr><td>命令</td><td>maximum_climb_rate &lt;speed-value&gt;</td></tr><tr><td>解释</td><td>指定更改高度时使用的最大爬升率和俯冲率。航点或脚本指定的其他爬升率受此值限制。注意: 移动器的实际爬升率也会受到 maximum_airight_path_angle 的影响。</td></tr><tr><td>命令</td><td>maximum_airight_path_angle &lt;angle-value&gt;</td></tr><tr><td>解释</td><td>指定最大飞行轨迹角度(爬升/俯冲角度)。值必须大于或等于0。注意: 移动器的实际爬升率也会受到 maximum_airight_rate 的影响。默认值: 0</td></tr><tr><td>命令</td><td>maximum_LINEAR acceleration &lt;acceleration-value&gt;</td></tr><tr><td>解释</td><td>指定加速时使用的最大线性加速度。如果航点不包含线性加速度规范,则使用此值。默认值: 6g</td></tr><tr><td>命令</td><td>maximum_radian acceleration &lt;acceleration-value&gt;</td></tr><tr><td>解释</td><td>指定转弯时使用的最大径向加速度。如果航点不包含径向加速度规范,则使用此值。</td></tr><tr><td></td><td>默认值:6g注意:径向加速度不是飞机的载荷因子。例如,如果希望n=2的最大载荷因子为2g转弯,则所需的2g转弯极限径向加速度应设置为=g*√n2-1=1.732g</td></tr><tr><td>命令</td><td>maximum_altitude&lt;altitude-value&gt;</td></tr><tr><td>解释</td><td>最大高度限制。</td></tr><tr><td>命令</td><td>minimum_altitude&lt;altitude-value&gt;</td></tr><tr><td>解释</td><td>最小高度限制。</td></tr><tr><td>命令</td><td>maximum_speed&lt;speed-value&gt;</td></tr><tr><td>解释</td><td>最大速度限制。值必须大于0。</td></tr><tr><td>命令</td><td>minimum_speed&lt;speed-value&gt;</td></tr><tr><td>解释</td><td>最小速度限制。值必须大于或等于0。默认值:0.0</td></tr><tr><td>命令</td><td>path_variance_radius&lt;length-value&gt;</td></tr><tr><td>解释</td><td>此值将在给定半径内随机变化航点的位置。选择随机方位和距离,并在计算路径时应用到下一个航点。</td></tr><tr><td>命令</td><td>roll_rate_limit&lt;angle-rate-value&gt;</td></tr><tr><td>解释</td><td>滚转速率限制。值必须大于0。注意:当应用于WSF_AIR_MOVER或其他航点移动器类型时,滚转速率不会影响平台沿路线的移动。要影响路线跟踪行为,请使用maximum_radial acceleration。</td></tr><tr><td>命令</td><td>speed_variance_percent&lt;percent-value&gt;</td></tr><tr><td>解释</td><td>此值将在每个航点随机变化速度,范围为给定百分比的正负。值必须大于0。</td></tr><tr><td>命令</td><td>turn_rate_limit&lt;angle-rate-value&gt;</td></tr><tr><td>解释</td><td>转弯速率限制。值必须大于0。</td></tr><tr><td>命令</td><td>pitch_disable 或 no_pitch</td></tr><tr><td>解释</td><td>限制移动器俯仰平台。对运动学没有影响。</td></tr><tr><td>命令</td><td>on_road</td></tr><tr><td>解释</td><td>限制移动器滚转平台。对运动学没有影响。</td></tr><tr><td>命令</td><td>off_road</td></tr><tr><td>解释</td><td>关闭on_road选项。这允许平台滚转。</td></tr><tr><td>命令</td><td>path_compute timestep&lt;time-value&gt;</td></tr><tr><td>解释</td><td>航点移动器预计算沿路径的移动。此行为强制转弯具有恒定半径。如果path_compute timestep指定为正值,则如果发生速度变化,转弯速率将在该间隔内更新。默认值:0.0</td></tr></table>

# 关于最大和默认命令的注意事项

移动器有各种命令指定最大值，例如 maximum_linear_acceleration。这些命令指定了在模拟过程中不会超过的总体移动限制。有一些默认命令，例如 default_linear_acceleration。这些命令指定了除非在路线或脚本中另有规定的速率。这些参数可能会被省略，让移动器默认使用最大速率。速率可以通过路线（如 linear_acceleration 命令）或脚本（如 GoToSpeed()方法）在模拟过程中修改。速率保持不变，直到被另一个脚本或路线改变。路线提供了一种机制来恢复默认速率，例如使用 linear_acceleration 默认命令。

# 3.6.1.4. 运动学模型 WSF_KINEMATIC_MOVER

```batch
mover WSF_KINEMATIC_MOVER Platform Part Commands ... .. WSF_KINEMATIC_MOVER Commands .. // Route Mover Commands use-route ...   
end_mover 
```

当放置在平台上时，WSF_KINEMATIC_MOVER 提供水平和垂直方向的平稳运动。与WSF_AIR_MOVER 不同，模型化了垂直加速度；高度和方向的过渡是动态且同时进行的。类似于 WSF_AIR_MOVER，不需要已知任何空气动力学、质量属性或推进力特性即可使用此移动器。此外，平台的飞行特性不受使用此移动器定义的飞行高度变化的影响（无空气密度变化效应）。

这种移动器接受两种不同的增益值（速度追踪增益和比例导航增益），并需要一些澄清的说明。对于您的特定场景，“正确”的增益值是实现定义的，没有特定的默认值适用于所有场景。较高的值会导致更激进的拦截机动，具有更大的角度和不连续的轨迹转弯，而较低的值则趋向于缓慢的徘徊机动进入目标点。移动器算法被编写为足够通用，可以拦截动态机动的目标点，在这种情况下，最好使用比例导航增益，以更有效地使用能量进行拦截。然而，此移动器类型始终应至少给予少量的速度追踪增益，因为在某些情况下，比例导航的转向方向变得模糊，可能导致飞行方向与目标点相反；此时一些速度追踪增益会介入以提供转向方向。如果观察到“翼摇”，则应减少增益值。

请注意，与所有移动器类型一样，在途径点接近时的微小时间差异会导致多个平台遵循相同途径点集时的路径变化。缩短更新间隔将减轻此问题，但会增加运行时间。例如，测试表明将更新间隔从 1.0 秒减少到 0.01 秒大大减少了这种倾向。

还要注意，没有逻辑专门用于保持恒定高度。考虑一个两点往返路径：当到达途径点 A时，有无限多的 180 度转弯选项（在 3D 中）返回到途径点 B；这可能包括一架伊梅尔曼翻转、一个左右横向转弯、一个滚动的分裂 S，或介于两者之间的任何动作。此时的最佳做法是确保所分配的路径中有足够的点，并且间隔足够近，以告知移动器要飞行的高度。

请注意，WSF_KINEMATIC_MOVER 不能完全取代 WSF_AIR_MOVER。WSF_AIR_MOVER 可用的几种脚本和路径方法不适用于 WSF_KINEMATIC_MOVER。WSF_KINEMATIC_MOVER 应被视为初始能力，绝非完整。它并未实现切换路径点时的所有引导命令 ..end_route定义。然而，它确实遵循纬度、经度、高度（仅 MSL）和速度命令的路径命令。然而，它目前忽略了距离、时间、爬升率和飞行路径角。

WSF_KINEMATIC_MOVER 的基本动力学模型本质上是一个四元数方向数学模型，该模型允许在惯性空间内在受限的角速度范围内旋转，同时速度矢量指向“前进”方向。加速度的大小由内部的追踪和比例导航增益决定，三维目标点（途径点）由路径移动器的路径点切换逻辑确定。当平台在当前途径点的一个转弯半径内时，当前飞行到点将前进到路线中的下一个（L，L，A）。waypoint_switch_on_ground_turning_radius 标志影响被认为是一个“转弯半径”的值。

速度矢量转弯速率受到最大横向加速度、最大机体滚转速率和最大机体转弯速率中最严格的限制，并且如果保持最大横向加速度，随着当前平台速度的增加，平台运动将趋向于直线。

调整默认的速度追踪增益（VP）和比例导航增益（PN）值并非易事。这两个增益彼此直接冲突，实现正确的值可能成为一个反复试验的过程。如果速度矢量约束（见上段）如此严格，以至于请求的 VP 或 PN 请求的加速度不可实现，则可能发生“饱和”。将 VP 和 PN 设置为零值将导致平台完全不转向以拦截途径点。要调整 VP 和 PN 增益值，请从将 PN 设置为零，VP 设置为小值开始。不断增加 VP，直到向途径点的转弯激进程度足以拦截。如果目标点是静止的（例如固定途径点），则校准完成。但是，对于移动或加速目标，纯 VP 会导致一个扫过的转弯从后面接近目标。增加 PN 直到平台“预见”撞击点，并沿直线飞行以拦截（前提是目标也沿直线移动）。如果不带 VP 设置 PN，则当目标点开始在速度矢量后面（方位角或仰角大于 90 度）时，会导致飞离目标。通常，首先飞行一个简短的 VP 阶段以使平台向

目标移动，然后逐渐减少 VP，同时逐渐增加 PN，以便终端拦截是纯 PN。默认值为 VP 为 4，PN 为 40，大多数情况下应足够。

（ 仅 供 软 件 开 发 人 员 参 考 ， WSF_KINEMATIC_MOVER 的 底 层 运 动 动 力 学 由UtMath3D_Motion 实用程序实现，该实用程序处理以下输入流命令。）

<table><tr><td>命令</td><td>detailedDebug</td></tr><tr><td>解释</td><td>启用调试输出到标准输出。</td></tr><tr><td>命令</td><td>prefer是可以的</td></tr><tr><td>解释</td><td>使平台始终滚转到局部垂直。与bank_to_turn互斥。</td></tr><tr><td>命令</td><td>bank_to_turn</td></tr><tr><td>解释</td><td>使平台滚转到加速度矢量,但在不转弯加速时仍然偏好垂直。与prefer是可以的互斥。</td></tr><tr><td>命令</td><td>broach_at_sea_level</td></tr><tr><td>解释</td><td>此移动器最初是为定义鱼雷移动器而开发的。然而,模型的能力使其可以在海平面以上使用。此标志确保运动必须保持在局部海平面以下,一旦潜入水下。</td></tr><tr><td>命令</td><td>target_speed</td></tr><tr><td>解释</td><td>一旦提供,平台将加速或减速以达到目标(期望)速度,受最大线性加速度约束。</td></tr><tr><td>命令</td><td>initial_speed</td></tr><tr><td>解释</td><td>初始线速度。初始化后,速度会变化以维持目标速度。</td></tr><tr><td>命令</td><td>initial_go_path_angle</td></tr><tr><td>解释</td><td>初始飞行路径角。初始化后,飞行路径角将变化以引导到定义路径中的期望途径点。</td></tr><tr><td>命令</td><td>maximum_LINEARacceleration</td></tr><tr><td>解释</td><td>定义线性(速度方向)加速度限制约束。默认:0.25 G</td></tr><tr><td>命令</td><td>maximum_radialacceleration</td></tr><tr><td>解释</td><td>定义径向(垂直于速度方向)加速度限制约束。此约束与maximum_body_turn_rate同时施加,使用最严格的限制。默认:8.0 G</td></tr><tr><td>命令</td><td>maximum_body_turn_rate</td></tr><tr><td>解释</td><td>定义平台捕获期望目标滚转角的最大速率。默认:180度/秒</td></tr><tr><td>命令</td><td>maximum_body_turn_rate</td></tr><tr><td>解释</td><td>定义速度矢量在三维空间中旋转的最大速率。此约束与maximum_radialacceleration同时施加,使用最严格的限制。默认:45度/秒</td></tr><tr><td>命令</td><td>velocity_pursuit_gain</td></tr><tr><td>解释</td><td>定义目标方位角和仰角(以弧度为单位)与应用的横向或垂直加速度(以米/秒^2)之间的比例因子,以使速度矢量指向目标。请参阅上面的注释。默认:4.0</td></tr><tr><td>命令</td><td>waypoint_SWITCH_on-ground_turning_radius</td></tr><tr><td>解释</td><td>如果此输入值设置为true,则在决定是否前进到路径中的下一个途径点时,仅考虑水平偏移;垂直偏移被忽略。如果设置为false,则在决定途径点是否足够接近被视为“命中”时,考虑三维斜距偏移。默认:true</td></tr><tr><td>命令</td><td>proportionaljahging gain</td></tr><tr><td>解释</td><td>定义目标视线速率(以弧度/秒为单位)与施加的横向或垂直加速度(以米/秒^2为单位)之间的比例因子,以使速度矢量在拦截时刻拦截目标的未来位置。详见上方注释。默认值:40.0</td></tr><tr><td>命令</td><td>use-route</td></tr><tr><td>解释</td><td>提供要遵循的路线名称。假定该路线是预定义的绝对路线。</td></tr></table>

# 3.6.1.5. 道路运动模型 WSF_ROAD_MOVER

```txt
mover <name> WSF_ROAD_MOVER Platform Part Commands ... ... WSFGROUND_MOVER commands road_network ... start_position ... end_position ... speed ... off_road_speed ... linear acceleraion ... pause_time ... useclosest_waypoint consider_off_road_shortcut ... end_mover 
```

WSF_ROAD_MOVER 是 WSF_GROUND_MOVER 的一种专门化，它在道路网络上移动。它计算起点和终点之间的最短路径，并将其用作路径点路径。可以设置暂停时间来偏移移动器的开始时间。此外，可以设置一个标志（use_closest_waypoint），使移动器根据用户指定的起点和终点位置的最近路径点来绘制最短路径。

最简单的情况下，移动器计算的路径包括：

一个可选的段，从 start_position 到道路网络上的最近点。如果起始位置在道路上，则不会生成此段。

在道路上最接近 end_position 的最短路径。

一个可选的段，从道路上的最后一点到 end_position。如果终点位置在道路上，则不会生成此段。

您还可以指定一条路线，表示各种中间点（如果省略了 start_position 和 end_position，可能包括它们）。例如，您可能希望从家出发，然后去杂货店、邮局和五金店，最后按顺序返回家。路线将简单地定义这些点的位置，移动器将找到在道路上最短的路径，将您按指定顺序带到这些点之间。

<table><tr><td>命令</td><td>road_network</td></tr><tr><td>解释</td><td>跟随的路网的名称。默认值:无(必须指定)路网的定义参考:4.8.2路网route_network。</td></tr><tr><td>命令</td><td>start_position</td></tr><tr><td>解释</td><td>定义起始位置和结束位置。结果路径将是从道路网络中定义的最短路径点。默认值:无注意:路线也可以用来指定中间位置。警告:如果指定了 start_position 或 end_position,则必须同时指定。如果两者都未指定,则可以使用路线来定义起点、终点和可能的中间位置。</td></tr><tr><td>命令</td><td>speed</td></tr><tr><td>解释</td><td>定义平台在道路网络上行驶时的速度。默认值:无(必须指定)</td></tr><tr><td>命令</td><td>off_road_speed</td></tr><tr><td>解释</td><td>定义平台在道路网络外行驶时的速度。默认值:与speed相同。</td></tr><tr><td>命令</td><td>linear acceleration</td></tr><tr><td>解释</td><td>用于加速平台的线性加速度。默认值:12m/s2</td></tr><tr><td>命令</td><td>pause_time &lt;time-value&gt;</td></tr><tr><td>解释</td><td>移动器在用户指定的起始位置暂停的时间。默认值:0秒</td></tr><tr><td>命令</td><td>useclosest_waypoint</td></tr><tr><td>解释</td><td>移动器在计算沿道路网络的最短路径时,将使用用户指定的起点和终点位置的最近路径点。不会生成起点或终点的非道路段。</td></tr><tr><td>命令</td><td>consider_off_road_shortcut &lt;boolean-value&gt;</td></tr><tr><td>解释</td><td>如果此命令的值为 true,则将考虑第二条路径,即从起点到终点的非道路“捷径”路径。如果使用 off_road_speed 行驶捷径路径所需的时间比正常路径少,则将其用作路线。这类似于穿过后院到达后面的房子,而不是绕过街道或人行道。默认值: false</td></tr></table>

# 3.6.1.6. 旋翼机动模型 WSF_ROTORCRAFT_MOVE

```txt
mover<name>WSF_ROTORCRAFT_MOVER Platform Part Commands .. // Rotorcraft Mover Commands update_interval ... update_time_tolerance ... // Rotorcraft Mover Commands weathercock_speed maximum_attitude_rate maximum_totalacceleration minimum_upwardacceleration bodyRates_gain maximum-ground_speed maximum_rate_of_climb maximum_rate_of_descent maximum_impact_speed ... mode <name> // Mode Commands ... end_mode vertical acceleraion_rate.pid...end_vertical acceleraion_rate.pid vertical acceleraion_value.pid...end_vertical acceleraion_value.pid lateral acceleraion_rate.pid...end_lateral acceleraion_rate.pid lateral acceleraion_value.pid...end_lateral acceleraion_value.pid end_mover 
```

WSF_ROTORCRAFT_MOVER 是一种用于模拟旋翼机运动特性的路线移动器。它允许将期望的平台航向（机身指向方向）与速度矢量解耦。在低速时，平台可以假设任何期望的航向，

而不管移动方向，但在高速时，航向将假设为飞行方向。脚本命令假设期望的方向或航向（机身指向方向）作为请求，但可能不会立即被执行。移动器将保持期望的航向角，并在减速到低于风标速度时再次假设期望的航向。在横向加速或转弯时，平台旋翼平面的方向在北东下框架中倾斜到加速度矢量的方向，但在巡航条件下是水平的。

这里需要讨论一些术语（参见 WsfPlatformSetHeading 命令的注释）。许多 WSF 基础设施错误地将航向角（速度矢量的罗盘方向）称为航向。因此，脚本请求 GoToHeading 实际上被视为请求 GoToCourse。即使在这个 WSF_ROTORCRAFT_MOVER 类型中也是如此，但由于这种情况，在命令这个移动器时会产生歧义。有两种方法可以将期望的机身指向方向插入此移动器类型：平台命令 SetHeading() 和 SetOrientationNED()。这两者中的任何一个都将插入 WSF_ROTORCRAFT_MOVER 一个期望的真实罗盘指向角，当低于风标速度时将被执行。所有其他与“航向”相关的功能将与其他 WSF 移动器中的实现匹配，并作为 Course 命令执行。

WSF_ROTORCRAFT_MOVER 是第一个实现移动器“模式”的 WSF 移动器类型，参见下面的模式命令。当移动器模式在脚本中或由于穿越路径点而改变时，所有运动属性将更改为该运动模式定义的属性。例如，脚本命令 'PLATFORM.Mover().SetMode("CRUISE")' 将立即采用预定义的运动模式“CRUISE”中的速度、爬升率和加速度值。可以为旋翼机移动器定义适合“悬停”、“盘旋”、“冲刺”或任何其他期望的移动器模式的模式。如果移动器未定义模式，则忽略命令。

# 旋翼机移动器命令

<table><tr><td>命令</td><td>desired Heading &lt;angle-value&gt;</td></tr><tr><td>解释</td><td>设置移动器的期望航向,该航向将在低于“风标速度”时生效。</td></tr><tr><td>命令</td><td>position_hold Capture Radius &lt;length-value&gt;</td></tr><tr><td>解释</td><td>旋翼机移动器在从一个位置过渡到另一个位置时使用速率引导机制。当接近目标点时,引导会根本性地改变以捕获位置值,因此必须减速以预期捕获和保持目标位置。此值确定从一种引导类型到另一种引导类型的过渡点。默认值设置为200米,这对于绝大多数旋翼机模型来说应该足够。</td></tr><tr><td>命令</td><td>start_mode &lt;mode-name&gt;</td></tr><tr><td>解释</td><td>指定平台的初始移动器模式。移动器模式可以通过脚本设置或在路径点转换时外部更改。移动器模式将在单独讨论。</td></tr><tr><td>命令</td><td>ned_filter_time_constant &lt;time-value&gt;</td></tr><tr><td>解释</td><td>指定应用于命令加速度值的滤波时间常数,以平滑瞬态响应。较大的值将对命令应用更大的平滑量。值必须大于零。默认值为1秒,适用于大多数用途。</td></tr><tr><td>命令</td><td>altitude_error_to_rate_of_climb_gain &lt;floating-point-value&gt;</td></tr><tr><td>解释</td><td>指定应用于高度误差的增益,以得出垂直加速度值。默认值为1,适用于大多数用途。</td></tr><tr><td>命令</td><td>vertical accelera tion_rate pid ... end vertical accelera tion_rate pid
vertical accelera tion_value pid ... end vertical accelera tion_value pid
lateral accelera tion_rate pid ... end lateral accelera tion_rate pid
lateral accelera tion_value pid ... end lateral accelera tion_value pid</td></tr><tr><td>解释</td><td>上述四个输入块中的每一个都可以包含应用于比例积分微分(PID)控制器的调谐参数,这些控制器确定驱动平台运动状态的加速度值。除非需要特定的动态响应,否则最终用户不需要修改默认增益。调谐PID控制器超出了本文档的范围,但有许多单独的资源可以提供帮助。PID控制器响应应适用于大多数用途。参见PID控制器命令以获取有效命令。</td></tr></table>

# 模式命令

命令 mode … end_mode

<table><tr><td>解释</td><td>weathercock_speed &lt;speed_value&gt; 地面速度高于此值时,平台将假设与航向角匹配的航向。低于此速度时,平台将假设由脚本命令设置的期望航向角。maximum_attitude_rate &lt;angular_rate_value&gt; 机身姿态变化的最大角速度。这主要与weathercock_speed 配合使用,以确定平台在进入和退出风标模式时的转换速度。maximum_total acceleraion &lt;acceleration_value&gt; 线性加速度的最大幅度。在剧烈的横向加速期间设置上限。minimum_upward acceleraion &lt;acceleration_value&gt; 最小向上加速度值。当飞机上升时,如果给出快速下降的命令,此值设置最小垂直加速度约束。请注意,许多具有摇摆旋翼头的旋翼机设计上不允许产生负g。bodyRates_gain &lt;floating_point_value&gt; 应用于角航向误差的增益,以获得消除航向误差的速率。主要用于在快速前飞时消除航向误差,高于风标速度。maximum-ground_speed &lt;speed_value&gt; 此运动模式下允许的最大地面速度。典型用途是为&lt;mode&gt;速度约束设置。maximum_rate_of_climb &lt;speed_value&gt; 此运动模式下允许的最大爬升率。典型用途是为&lt;mode&gt;设置现实的爬升率。maximum_rate_of_descent &lt;speed_value&gt; 此运动模式下允许的最大下降率的幅度。值必须大于零,但应用时将被取负。典型用途是为&lt;mode&gt;设置现实的下降率。</td></tr></table>

# PID 控制命令

<table><tr><td>命令</td><td>proportional_gain floating_point_value&gt;</td></tr><tr><td>解释</td><td>应用于当前误差的增益,试图将误差归零。较大的值将更强力地试图将误差归零,但容易在输出中引起振荡。</td></tr><tr><td>命令</td><td>derivative_gain floating_point_value&gt;</td></tr><tr><td>解释</td><td>应用于当前误差变化率的增益,试图防止误差超过期望目标值。较大的值将反对任何输出变化,导致漂移。</td></tr><tr><td>命令</td><td>integral_gain floating_point_value&gt;</td></tr><tr><td>解释</td><td>反对稳态偏差的增益,试图将偏差归零。</td></tr><tr><td>命令</td><td>input_threshold floating_point_value&gt;</td></tr><tr><td>解释</td><td>比较值,用于确定是否对输入误差样本进行积分求和。当输入值与目标值的差异超过 input_threshold时,不进行输入积分。一旦输入阈值接近目标值,将进行连续积分以识别和反应输入偏差。如果是这样,将对偏差应用 integral_gain 以随时间消除它。</td></tr></table>

# 3.6.1.7. 海上移动模型 WSF_SURFACE_MOVER

```txt
mover WSF_SURFACEMOVED Platform Part Commands .. update_interval ... update_time_tolerance .. // Route Mover Commands at_end_of_path... 
```

```txt
pathfinder ...   
start_at ...   
start_time ...   
switch_onapproach   
switch_on_passing   
altitude_offset   
route ... Route Commands ...   
end-route   
useRoute...   
//Waypoint Mover Commands   
angle_of_attack_table ...   
bank_angle_limit ...   
body_g_limit ...   
heading_pursuit_gain ...   
maximum_climb_rate ...   
maximum_airight_path_angle ...   
maximum_linearacceleration ...   
maximum_radialacceleration ...   
maximum_altitude ...   
minimum_altitude ...   
maximum_speed ...   
minimum_speed ...   
path_variance_radius ...   
roll_rate_limit ...   
speed_variance_percent ...   
turn_rate_limit ...   
end_mover 
```

WSF_SURFACE_MOVER 实现了一个移动器，用于在水面上移动的平台（例如，船只）。这个移动器类似于 WSF_GROUND_MOVER；然而，俯仰和横滚默认设置为零。未来可能会增加一个可选的海况选项，以修改相关平台的俯仰、横滚和高度。

# Mover 全局命令

<table><tr><td>命令</td><td>update_interval &lt;time-value&gt;</td></tr><tr><td>解释</td><td>如果非零，指定模拟调用Mover的周期时间间隔。如果为零，则仅在需要确定包含平台的位置时调用Mover。
默认值：0秒，除非特定Mover实现覆盖。</td></tr><tr><td>命令</td><td>update_time_tolerance &lt;time-value&gt;</td></tr><tr><td>解释</td><td>当模拟请求位置更新时，如果自上次更新以来的时间小于或等于此值，则Mover将忽略更新。
默认值：大多数Mover实现将其定义为以某个适当的名义速度行驶1米所需的时</td></tr><tr><td colspan="2">间。
注意：Mover 实现可能会选择忽略此命令。</td></tr></table>

路线 Mover 命令  

<table><tr><td>命令</td><td>altitude_offset &lt;length-value&gt;</td></tr><tr><td>解释</td><td>设置时,此偏移量将使父平台的位置偏移当前航点高度的指定量。</td></tr><tr><td>命令</td><td>at_end_of_path [extrapolate | stop | remove]</td></tr><tr><td>解释</td><td>指定当 Mover 到达其定义路径的末端时要采取的操作。extrapolate: 继续以最后已知的航向、速度和高度移动。stop: 停止移动,但将平台保留在模拟中。remove: 从模拟中移除平台。默认值: extrapolate</td></tr><tr><td>命令</td><td>draw-route &lt;boolean-value&gt;</td></tr><tr><td>解释</td><td>此命令与 print-route 相同,只是路线文本不打印,仅通过 WsfDraw 绘制。</td></tr><tr><td>命令</td><td>on_turn_failure [best_effort | reverse_turn | ignore_point]</td></tr><tr><td>解释</td><td>定义当由于转弯半径无法准确到达路径上的某个点时 Mover 的行为。best_effort: 转弯直到平台到达最接近该点的位置。ignore_point: Mover 实际上忽略该点。当跳过该点时,任何与该点相关的脚本都会执行。reverse_turn: Mover 将向相反方向转弯,使其能够准确到达该点。注意:如果 Mover 给出的路径在其约束范围内,此命令无效。默认值: best_effort</td></tr><tr><td>命令</td><td>pathfinder &lt;path-name&gt;</td></tr><tr><td>解释</td><td>要使用的路径查找器对象的名称。</td></tr><tr><td>命令</td><td>printRoute &lt;boolean-value&gt;</td></tr><tr><td>解释</td><td>启用时,每当路径被修改时,路线将打印到屏幕上。此外,WsfDraw 将用于输出路线的可视化,可以通过许多可视化工具查看。</td></tr><tr><td>命令</td><td>start_at &lt;label-name&gt;</td></tr><tr><td>解释</td><td>标识路径中航点的标签,用作起始位置。</td></tr><tr><td>命令</td><td>start_time &lt;random-time-reference&gt;</td></tr><tr><td>解释</td><td>指示平台在指定时间开始移动。当前速度设置为零,一旦达到模拟时间,平台将以第一个航点指定的速度开始移动。如果希望在航点处有一个延迟时间,请使用子命令 pause_time。</td></tr><tr><td>命令</td><td>switch_onapproach</td></tr><tr><td>解释</td><td>当接近当前目标航点的一个转弯半径范围内时切换到下一个航点。</td></tr><tr><td>命令</td><td>switch_on_passing</td></tr><tr><td>解释</td><td>仅当通过当前目标航点时切换到下一个航点。注意:这是默认设置。</td></tr><tr><td>命令</td><td>turn Failure_threshold &lt;ratio-value&gt;</td></tr><tr><td>解释</td><td>定义触发 on_turn_failure 行为的阈值,作为转弯半径的比率。例如,转弯半径为1000米, turn Failure_threshold 为 0.01 ,则如果错过该点超过 10 米,将触发on_turn_failure 逻辑。默认值: 0.01</td></tr><tr><td>命令</td><td>use-route &lt;route-name&gt;</td></tr><tr><td>解释</td><td>提供要遵循的路径的名称。假定路径是预定义的绝对路径。参见:4.8.1 路由 route</td></tr></table>

航点移动器命令  

<table><tr><td>命令</td><td>angle_of_attack_table ... end_angle_of_attack_table</td></tr><tr><td>解释</td><td>altitude &lt;altitude-value&gt;: 指定后续数据有效的高度。高度块必须按数值升序排列。使用线性插值计算高度块。
speed &lt;speed-value&gt;: 指定有效的攻角速度。速度条目必须按数值升序排列。攻角将使用速度数据的线性插值计算。</td></tr><tr><td></td><td>angle:攻角。攻角条目必须按数值升序排列。end_angle_of_attack_table</td></tr><tr><td>命令</td><td>bank_angle_limit&lt;angle-value&gt;</td></tr><tr><td>解释</td><td>滚转角度限制。值必须在0度到85度之间。用于计算最大径向加速度。默认值:0</td></tr><tr><td>命令</td><td>body_g_limit&lt;acceleration-value&gt;</td></tr><tr><td>解释</td><td>机体g极限。值必须大于地球重力加速度。</td></tr><tr><td>命令</td><td>heading_pursuit_gain&lt;double-value&gt;</td></tr><tr><td>解释</td><td>航向追踪增益。默认值:5</td></tr><tr><td>命令</td><td>maximum_climb_rate&lt;speed-value&gt;</td></tr><tr><td>解释</td><td>指定更改高度时使用的最大爬升率和俯冲率。航点或脚本指定的其他爬升率受此值限制。注意:移动器的实际爬升率也会受到 maximum_aircraft_path_angle 的影响。</td></tr><tr><td>命令</td><td>maximum_aircraft_path_angle&lt;acceleration-value&gt;</td></tr><tr><td>解释</td><td>指定最大飞行轨迹角度(爬升/俯冲角度)。值必须大于或等于0。注意:移动器的实际爬升率也会受到 maximum_aircraft_path_angle 的影响。默认值:0</td></tr><tr><td>命令</td><td>maximum-linear acceleration&lt;acceleration-value&gt;</td></tr><tr><td>解释</td><td>指定加速时使用的最大线性加速度。如果航点不包含线性加速度规范,则使用此值。默认值:6g</td></tr><tr><td>命令</td><td>maximum_radial acceleration&lt;acceleration-value&gt;</td></tr><tr><td>解释</td><td>指定转弯时使用的最大径向加速度。如果航点不包含径向加速度规范,则使用此值。默认值:6g注意:径向加速度不是飞机的载荷因子。例如,如果希望n=2的最大载荷因子为2g转弯,则所需的2g转弯极限径向加速度应设置为=g*√n²-1=1.732g</td></tr><tr><td>命令</td><td>maximum_altitude&lt;altitude-value&gt;</td></tr><tr><td>解释</td><td>最大高度限制。</td></tr><tr><td>命令</td><td>minimum_altitude&lt;altitude-value&gt;</td></tr><tr><td>解释</td><td>最小高度限制。</td></tr><tr><td>命令</td><td>maximum_speed&lt;speed-value&gt;</td></tr><tr><td>解释</td><td>最大速度限制。值必须大于0。</td></tr><tr><td>命令</td><td>minimum_speed&lt;speed-value&gt;</td></tr><tr><td>解释</td><td>最小速度限制。值必须大于或等于0。默认值:0.0</td></tr><tr><td>命令</td><td>path_variance_radius&lt;length-value&gt;</td></tr><tr><td>解释</td><td>此值将在给定半径内随机变化航点的位置。选择随机方位和距离,并在计算路径时应用到下一个航点。</td></tr><tr><td>命令</td><td>roll_rate_limit&lt;angle-rate-value&gt;</td></tr><tr><td>解释</td><td>滚转速率限制。值必须大于0。注意:当应用于WSF_AIR_MOVER或其他航点移动器类型时,滚转速率不会影响平台沿路线的移动。要影响路线跟踪行为,请使用 maximum_radial accelera tion。</td></tr><tr><td>命令</td><td>speed_variance_percent&lt;percent-value&gt;</td></tr><tr><td>解释</td><td>此值将在每个航点随机变化速度,范围为给定百分比的正负。值必须大于0。</td></tr><tr><td>命令</td><td>turn_rate_limit&lt;angle-rate-value&gt;</td></tr><tr><td>解释</td><td>转弯速率限制。值必须大于0。</td></tr><tr><td>命令</td><td>pitch_disable 或 no_pitch</td></tr><tr><td>解释</td><td>限制移动器俯仰平台。对运动学没有影响。</td></tr><tr><td>命令</td><td>on_road</td></tr><tr><td>解释</td><td>限制移动器滚转平台。对运动学没有影响。</td></tr><tr><td>命令</td><td>off_road</td></tr><tr><td>解释</td><td>关闭on_road 选项。这允许平台滚转。</td></tr><tr><td>命令</td><td>path_compute timestep&lt;time-value&gt;</td></tr><tr><td>解释</td><td>航点移动器预计算沿路径的移动。此行为强制转弯具有恒定半径。如果path_compute timestep 指定为正值,则如果发生速度变化,转弯速率将在该间隔内更新。</td></tr></table>

# 关于最大值和默认命令的注意事项

移动器有各种命令用于指定最大值，例如 maximum_linear_acceleration。这些命令指定了一个整体的移动限制，在模拟过程中不会超过这个限制。有一些默认命令，例如default_linear_acceleration。这些命令指定了一个速率，除非在路径或脚本中另有规定，否则将使用这个速率。这些参数可以省略，使移动器默认使用最大速率。速率可以在模拟过程中通过路径（例如使用 linear_acceleration 命令）或脚本（例如使用 GoToSpeed() 方法）进行修改。速率在被另一个脚本或路径改变之前保持不变。路径提供了一种返回默认速率的机制，例如使用 linear_acceleration default 命令。

# 3.6.1.8. TSPI 运动模型 WSF_TSPI_MOVER

```txt
mover WSF_TSPI_MOVER   
... Platform Part Commands ...   
filename or TSPIFilename ..   
start_time ..   
at_end_of_path ..   
# Data Format Commands   
time_in ...   
altitude_in ...   
heading_in ...   
pitch_in ...   
roll_in ...   
relocate_and Rotate ...   
heading_inverted   
pitch_inverted   
roll_inverted   
end_mover 
```

WSF_TSPI_MOVER 实现了一个移动器，该移动器基于从文本文件读取的时间空间位置信息（TSPI）数据更新位置。

TSPI 数据文件中包含的数据格式如下：

<time> <latitude> <longitude> <altitude> <speed> <heading> <pitch> <roll>

这些 TSPI 值的默认单位是秒、米、米/秒和弧度。然而，用户可以指定数据格式命令来覆盖默认值。

<table><tr><td>命令</td><td>filename &lt;filename&gt;TSPIFilename &lt;filename&gt;</td></tr><tr><td>解释</td><td>指定包含TSPI数据的文件名。（请注意，这也是一个可单独脚本化的命令。详见</td></tr><tr><td></td><td>WsfMover SetTSPI_FileName(   )。)</td></tr><tr><td>命令</td><td>start_time &lt;time-value&gt;</td></tr><tr><td>解释</td><td>指定与第一个 TSPI 数据值对应的模拟时间。这是关联平台开始移动的模拟时间。默认值: 0.0</td></tr><tr><td>命令</td><td>at_end_of_path [ extrapolate | stop | remove ]</td></tr><tr><td>解释</td><td>指定在遇到 TSPI 文件末尾时的操作。 extrapolate: 沿大圆路径从最后一个点继续。stop: 在最后一个点停止。remove: 从模拟中移除平台。默认值: extrapolate</td></tr><tr><td>命令</td><td>extrapolation &lt;boolean-value&gt;</td></tr><tr><td>解释</td><td>为了兼容旧输入文件保留此命令。值为 'true' 等同于 'at_end_of_path extrapolate', 值为 'false' 等同于 'at_end_of_path stop'。</td></tr></table>

# 数据格式命令

这些命令定义了 TSPI 文件中数据的格式。例如，当使用与 BLUEMAX 兼容的 TSPI 文件时，应指定以下命令：

altitude in feet   
roll inverted   
time_in <time-unit> 指定 TSPI 数据文件中 <time> 值的单位为 <time-units>。 默认值：秒  
altitude_in <length-units> 指 定 TSPI 数 据 文 件 中 <altitude> 值 的 单 位 为<length-units>。 默认值：米  
speed_in <speed-units> 指定 TSPI 数据文件中 <speed> 值的单位为 <speed-units>。默认值：米/秒  
heading_in <angle-unit>   
pitch_in <angle-unit>   
roll_in <angle-unit> 指定 TSPI 数据文件中 <heading>、<pitch> 或 <roll> 值的单位为 <angular-units>。 默认值：弧度  
heading_inverted   
pitch_inverted   
roll_inverted 指定 TSPI 数据文件中的给定值名称是否需要反转（即，值取反）。默认值：不反转  
relocate_and_rotate relocate_and_rotate … end_relocate_and_rotate 块是一种将轨迹从一个位置移动到另一个位置的方法，包括改变方向。两个关键字将 TSPI 轨迹从一个（纬度，经度）移动到另一个（纬度，经度），分别是：A)initial_endpoint_anchor<lat> <lon>，或 B) terminal_endpoint_anchor <lat> <lon>。路径重新定位后，可以重新定向。为此，使用 A) great_circle_heading_at_anchor_point <angle-value>，或 B)align_to_great_circle_through <lat> <lon>。在后一种情况下，<lat> <lon> 值必须与锚点不同。请注意，由于使用的球面几何计算和椭球地球，路径平移过程将是近似的。还请注意，初始或终端航向值是沿初始和最终轨迹点之间的大圆弧，而不一定是轨迹开始或结束时的真实航向。

# 3.6.1.9. 水下运动模型 WSF_SUBSURFACE_MOVER

```batch
mover WSF_SURFACE_MOVER 
```

```txt
Platform_Part_Commands...   
//`MoverCommands`_   
update_interval...   
update_time_tolerance...   
WSF_SUBSURFACE_MOV_Route_Mover_Commands   
angle_of_attack_table   
bank_angle_limit   
body_g_limit   
heading_pursuit_gain   
maximum_climb_rate   
maximum_airight_path_angle   
maximum_linearacceleration   
maximum_radialacceleration   
maximum_altitude   
minimum_altitude   
maximum_speed   
minimum_speed   
path_variance_radius   
roll_rate_limit   
speed_variance_percent   
turn_rate_limit   
end_mover 
```

WSF_SUBSURFACE_MOVER 实现了用于潜水器的移动器。WSF_SUBSURFACE_MOVER 是一种路径移动器，能够根据指定的路径和参数进行移动。

# Mover 全局命令

<table><tr><td>命令</td><td>update_interval &lt;time-value&gt;</td></tr><tr><td>解释</td><td>如果非零，指定模拟调用Mover的周期时间间隔。如果为零，则仅在需要确定包含平台的位置时调用Mover。
默认值：0秒，除非特定Mover实现覆盖。</td></tr><tr><td>命令</td><td>update_time_tolerance &lt;time-value&gt;</td></tr><tr><td>解释</td><td>当模拟请求位置更新时，如果自上次更新以来的时间小于或等于此值，则Mover将忽略更新。
默认值：大多数Mover实现将其定义为以某个适当的名义速度行驶1米所需的时间。
注意：Mover实现可能会选择忽略此命令。</td></tr></table>

# 路线 Mover 命令

命令 altitude_offset <length-value>

<table><tr><td>解释</td><td>设置时,此偏移量将使父平台的位置偏移当前航点高度的指定量。</td></tr><tr><td>命令</td><td>at_end_of_path [extrapolate | stop | remove]</td></tr><tr><td>解释</td><td>指定当Mover到达其定义路径的末端时要采取的操作。extrapolate:继续以最后已知的航向、速度和高度移动。stop:停止移动,但将平台保留在模拟中。remove:从模拟中移除平台。默认值:extrapolate</td></tr><tr><td>命令</td><td>draw-route&lt;boolean-value&gt;</td></tr><tr><td>解释</td><td>此命令与print-route相同,只是路线文本不打印,仅通过WsfDraw绘制。</td></tr><tr><td>命令</td><td>on_turn_failure [best_effort | reverse_turn | ignore_point]</td></tr><tr><td>解释</td><td>定义当由于转弯半径无法准确到达路径上的某个点时Mover的行为。best_effort:转弯直到平台到达最接近该点的位置。ignore_point:Mover实际上忽略该点。当跳过该点时,任何与该点相关的脚本都会执行。reverse_turn:Mover将向相反方向转弯,使其能够准确到达该点。注意:如果Mover给出的路径在其约束范围内,此命令无效。默认值:best_effort</td></tr><tr><td>命令</td><td>pathfinder&lt;path-name&gt;</td></tr><tr><td>解释</td><td>要使用的路径查找器对象的名称。</td></tr><tr><td>命令</td><td>printRoute&lt;boolean-value&gt;</td></tr><tr><td>解释</td><td>启用时,每当路径被修改时,路线将打印到屏幕上。此外,WsfDraw将用于输出路线的可视化,可以通过许多可视化工具查看。</td></tr><tr><td>命令</td><td>start_at&lt;label-name&gt;</td></tr><tr><td>解释</td><td>标识路径中航点的标签,用作起始位置。</td></tr><tr><td>命令</td><td>start_time&lt;random-time-reference&gt;</td></tr><tr><td>解释</td><td>指示平台在指定时间开始移动。当前速度设置为零,一旦达到模拟时间,平台将以第一个航点指定的速度开始移动。如果希望在航点处有一个延迟时间,请使用子命令pause_time。</td></tr><tr><td>命令</td><td>switch_onapproach</td></tr><tr><td>解释</td><td>当接近当前目标航点的一个转弯半径范围内时切换到下一个航点。</td></tr><tr><td>命令</td><td>switch_on_passing</td></tr><tr><td>解释</td><td>仅当通过当前目标航点时切换到下一个航点。注意:这是默认设置。</td></tr><tr><td>命令</td><td>turn Failure_threshold&lt;ratio-value&gt;</td></tr><tr><td>解释</td><td>定义触发on_turn_failure行为的阈值,作为转弯半径的比率。例如,转弯半径为1000米,turn Failure_threshold为0.01,则如果错过该点超过10米,将触发on_turn_failure逻辑。默认值:0.01</td></tr><tr><td>命令</td><td>use-route&lt;route-name&gt;</td></tr><tr><td>解释</td><td>提供要遵循的路径的名称。假定路径是预定义的绝对路径。参见:4.8.1路由route</td></tr></table>

航点 Mover 命令  

<table><tr><td>命令</td><td>angle_of_attack_table...end_angle_of_attack_table</td></tr><tr><td>解释</td><td>定义攻角表。altitude:指定后续数据有效的高度。高度块必须按递增数值顺序排列。使用高度块的线性插值。speed:指定列出的攻角有效的速度。速度条目必须按递增数值顺序排列。攻角将使用速度数据的线性插值计算。angle:攻角。攻角条目必须按递增数值顺序排列。</td></tr><tr><td>命令</td><td>bank_angle_limit&lt;angle-value&gt;</td></tr><tr><td>解释</td><td>滚转角度限制。值必须在0度到85度之间。用于计算最大径向加速度。默认值:0</td></tr><tr><td>命令</td><td>body_g_limit&lt;acceleration-value&gt;</td></tr><tr><td>解释</td><td>体g限制。值必须大于地球重力加速度。</td></tr><tr><td>命令</td><td>heading_pursuit_gain &lt;double-value&gt;</td></tr><tr><td>解释</td><td>航向追踪增益。默认值:5</td></tr><tr><td>命令</td><td>maximum_climb_rate &lt;speed-value&gt;</td></tr><tr><td>解释</td><td>指定更改高度时使用的最大爬升率和俯冲率。航点或脚本指定的其他爬升率受此值约束。注意:Mover的实际爬升率也会受到‘maximum_going_path_angle'的影响。</td></tr><tr><td>命令</td><td>maximum_climb_path_angle &lt;angle-value&gt;</td></tr><tr><td>解释</td><td>指定最大飞行路径角(爬升/俯冲角)。值必须大于或等于0。注意:Mover的实际爬升率也会受到‘maximum_climb_rate'的影响。默认值:0</td></tr><tr><td>命令</td><td>maximum_LINEARacceleration &lt;acceleration-value&gt;</td></tr><tr><td>解释</td><td>指定加速时使用的最大线性加速度。如果航点不包括线性加速度规范,则使用此值。默认值:6g's</td></tr><tr><td>命令</td><td>maximum_radialacceleration &lt;acceleration-value&gt;</td></tr><tr><td>解释</td><td>指定转弯时使用的最大径向加速度。如果航点不包括径向加速度规范,则使用此值。默认值:6g's注意:径向加速度不是飞机的负载因子。例如,如果希望最大负载因子为n=2对于2g转弯,则希望的2g转弯限制的径向加速度需要设置为=g*√n2-1=1.732g</td></tr><tr><td>命令</td><td>maximum_altitude &lt;altitude-value&gt;</td></tr><tr><td>解释</td><td>最大高度限制。</td></tr><tr><td>命令</td><td>minimum_altitude &lt;altitude-value&gt;</td></tr><tr><td>解释</td><td>最小高度限制。</td></tr><tr><td>命令</td><td>maximum_speed &lt;speed-value&gt;</td></tr><tr><td>解释</td><td>最大速度限制。值必须大于0。</td></tr><tr><td>命令</td><td>minimum_speed &lt;speed-value&gt;</td></tr><tr><td>解释</td><td>最小速度限制。值必须大于或等于0。默认值:0.0</td></tr><tr><td>命令</td><td>path_variance_radius &lt;length-value&gt;</td></tr><tr><td>解释</td><td>此值将在给定半径范围内随机变化航点的位置。计算路径时选择并应用随机方位和距离到下一个航点。</td></tr><tr><td>命令</td><td>roll_rate_limit &lt;angle-rate-value&gt;</td></tr><tr><td>解释</td><td>滚转率限制。值必须大于0。注意:当应用于WSF_AIR_MOVER或其他航点Mover类型时,滚转率不会影响平台沿路线的移动。要影响路线跟随行为,请使用maximum_radial acceleration。</td></tr><tr><td>命令</td><td>speed_variance_percent &lt;percent-value&gt;</td></tr><tr><td>解释</td><td>此值将在给定的百分比范围内随机变化每个航点的速度。值必须大于0。</td></tr><tr><td>命令</td><td>turn_rate_limit &lt;angle-rate-value&gt;</td></tr><tr><td>解释</td><td>转弯率限制。值必须大于0。</td></tr></table>

# 3.6.2. 跟随类型 FollowerTypes

这些移动器“附加”到路线类型移动器上，用于使平台实例“跟随”其他平台。

# 3.6.2.1. 混合跟踪运动模型 WSF_HYBRID_MOVER

```txt
mover WSF_HYBRID_MOVERS Platform Part Commands .. //Mover Commands 
```

```txt
update_interval ...   
update_time_tolerance ...   
// Hybrid Mover Commands   
follower_mover ...   
 waypoint_mover ...   
current_mover ...   
auto_SWITCH   
...WaypointMoverCommands...   
...FollowerMoverCommands...   
end_mover 
```

WSF_HYBRID_MOVER 是 一 种 专 门 的 移 动 器 ， 整 合 了 WsfFollower 移 动 器 和WsfWaypointMover 移动器的功能。

```txt
命令follower_mover<name-value>  
解释预定义的跟随者移动器的名称。  
命令 waypoint_mover<name-value>  
解释预定义的路径点移动器的名称（例如，WSF_AIR_MOVER、WSFGROUND_MOVER或WSF_SURFACE_MOVER）。  
命令current_mover[follower_mover| waypoint_mover]  
解释将当前移动器设置为跟随者移动器或路径点移动器。  
命令auto_SWITCH  
解释如果当前移动器是跟随者移动器且领航者不再存在，则切换回路径点移动器并返回到给定路线的最近点。
```

# 3.6.2.2. 保持偏移运动模型 WSF_OFFSET_MOVER

```txt
mover WSF_OFFSET_MOVER Platform Part Commands .. //Mover Commands update_interval ... update_time_tolerance .. // Offset Mover Commands attachment_type ... referenceplatform ... offset_from_reference ... orphan_action ... 
```

```txt
end mover 
```

WSF_OFFSET_MOVER 实现了一个移动器，使平台保持在指定的领航平台的预定偏移位置。平台可以“刚性”或“系绳”附加。

特别注意事项

参考平台应在跟随平台之前定义，以便跟随平台在初始化时可以确定其位置。如果不是这种情况，请确保跟随平台在其定义中有一个“位置”命令。

如果使用系绳模式，请确保领航平台的“更新间隔”不太大。否则，跟随者可能需要进行一些剧烈的移动以达到预定的空间关系。

<table><tr><td>命令</td><td>attachment_type [ tether | rigid ]</td></tr><tr><td>解释</td><td>指定跟随者如何附加到领航者。 tether: 跟随者移动时好像通过弹性系绳附加到领航者。 rigid: 跟随者移动时好像刚性附加到领航者。 默认值: tether 注意: 当前默认的 tether 不起作用。初始功能仅适用于 rigid。</td></tr><tr><td>命令</td><td>referenceplatform &lt;name&gt;</td></tr><tr><td>解释</td><td>指定参考或“领航”平台的名称(即要跟随的平台)。注意:一般来说,应在定义跟随平台之前定义领航平台。</td></tr><tr><td>命令</td><td>offset_from_reference &lt;x-length-units&gt;&lt;y-length-units&gt;&lt;z-length-units&gt;</td></tr><tr><td>解释</td><td>指定跟随平台相对于参考平台实体坐标系的偏移量。 默认值:0 m 0 m 0 m</td></tr><tr><td>命令</td><td>orphan_action [ stop | extrapolate | remove ]</td></tr><tr><td>解释</td><td>定义如果参考平台从模拟中移除时应执行的操作。值如下:stop: 在当前位置停止。extrapolate: 沿最后已知航向继续外推。remove: 从模拟中移除跟随平台。 默认值:stop</td></tr></table>

# 3.6.3. 六自由度类型 SixDof Types

# 3.6.3.1. 公共类型定义

# 3.6.3.1.1. 六自由度目标类型 six_dof_object_types

```c
six_dof_object_types   
// rigid_body(vehicle_type rigid_bodyvehicle_type ... end_rigid_bodyvehicle_type   
// point_mass(vehicle_type point_massvehicle_type ... end_point_massvehicle_type   
// SixDOF Thrust Producer Types rigid_body.engine_type ... end_rigid_body.engine_type point_mass.engine_type ... end_point_mass.engine_type   
// SixDOF Platform Mappings mapVehicle_toplatform ... end_mapvehicle_toplatform   
// SixDOF Integrators Support 
```

```c
integrators ..   
// SixDOF Environment Support terrain ...   
endsix_dof_object_types 
```

six_dof_object_types 块用于指定各种类型的 SixDOF 对象、子对象、组件（如引擎）和环境基础设施（如地形）。一旦定义完成，可以在定义 WSF_RIGID_BODY_SIX_DOF_MOVER 或WSF_POINT_MASS_SIX_DOF_MOVER 时使用 rigid_body_vehicle_type（参见：3.6.3.1.3 刚体载具类型 rigid_body_vehicle_type） 或 point_mass_vehicle_type（参见：3.6.3.1.2 点质量载具类型 point_mass_vehicle_type）。

可以使用多个 six_dof_object_types 块。six_dof_object_types 块中定义的类型必须具有唯一的名称。此外，类型必须在引用之前定义。因此，定义类型的顺序很重要。类型应按引用顺序定义。例如，如果一个 “F2H_Banshee” 刚体飞机使用 “Westinghouse_J34” 喷气发动机，则 应 先 定 义 引 擎 类 型 (rigid_body_engine_type ， 参 见 ： 3.6.3.2.2) ， 然 后 定 义 飞 机(rigid_body_vehicle_type，参见：3.6.3.1.3 刚体载具类型 rigid_body_vehicle_type)。

```txt
point_mass.engine_type J79-GE-7 BASE_TYPE ... Jet-or rocket-specific commands ... //Thrust Offset Location thrust_offset ... //Reference Area When Inoperative inop_ref_area ... //Fuel Source for Engine fuel_feed ...   
end_point_mass.engine_type 
```

# SixDOF 积分器支持

SixDOF 设计时考虑了使用不同的数值积分方法。这些不同的积分器通过使用integrators 命令来“加载”。

目前，只提供了一个默认的积分器，但软件开发人员可以从基类 WsfSixDOF_Integrator派生以引入其他积分器。

integrators <file-name>

这将通过读取/加载指定文件来加载一个或多个 SixDOF 积分器。

有关积分器文件格式的定义，如下：

```c
integrators create_integrator STANDARD_RIGID_BODY_INTEGRATOR end_integrators 
```

integrators 行可以独立定义，但通常与 SixDOF 环境支持项一起分组到另一个文件中（ 通 常 是 six_dof_environment.txt ） 。 通 常 应 包 括 默 认 积 分 器 （ 区 分 大 小 写 ，STANDARD_RIGID_BODY_INTEGRATOR 适 用 于 刚 体 6DOF ， 而STANDARD_POINT_MASS_INTEGRATOR 适用于点质量 6DOF），除非场景中的所有对象都使用其他积分器。

# SixDOF 环境支持

SixDOF 移动器依赖 AFSIM 场景局部信息来获取大多数环境组件。这些组件包括大气、风、地形和重力。AFSIM 地形可以进行增强，以指定如机场等区域，在这些区域中，其他地形数据中的噪声可能对起降或滑行操作产生不利影响。

```txt
terrain <file-name>
```

使用指定文件创建 SixDOF 地形对象。对于给定场景，只应定义一个地形对象。

有关地形文件格式的定义，如下：

```txt
region
location
lat 21.3178275
lon -157.92026310
alt_ft 13.0
minLat 21.27
maxLat 21.37
minLon -157.97
maxLon -157.87
end_location
...
location
lat 21.4814475
lon -158.0378379
alt_ft 843.0
end_location
end_region
end Terrain 
```

SixDOF 地形文件定义了一个或多个区域，每个区域包含一个或多个位置。文件的目的是定义地形的海拔高度（以海平面以上的英尺为单位）。其主要用途是定义机场区域以支持SixDOF 地面操作。

位置块有两种配置（如上所示）。

第一个位置显示了完全定义的方法，定义了纬度/经度（以度为单位）和海拔高度（以英尺为单位），以及最小/最大纬度和经度值。这定义了一个由最大/最小纬度和经度界定的位置。假设该位置内的所有地形都在指定的海拔高度。

第二个位置显示了部分定义的方法，仅定义了纬度/经度（以度为单位）和海拔高度（以英尺为单位）。在这种情况下，最小/最大纬度和经度值将通过调整值来计算，大约在指定纬度/经度的两侧各 3 海里（3 弧分）。假设该位置内的所有地形都在指定的海拔高度。

这允许在一个区域内定义各种机场，并且还允许定义多个区域。将机场分组到多个区域（而不是简单地使用单个区域）可以提高运行时性能。

为了方便，通常也会在文件中包含一个 integrators 命令。

在这里定义一个 atmosphere_table （参见：4.11.3.1 内联大气模型 atmosphere）块也可能很方便。如果未定义，将使用默认大气层。这将在 61 公里 MSL 以上导致不准确，因为默认的大气层在此高度结束。

# 3.6.3.1.2. 点质量载具类型 point_mass_vehicle_type

point_mass_vehicle_type F-86_Saber BASE_TYPE

// SixDOF Mass Properties Data mass_properties ... end_mass_properties

// SixDOF Aerodynamics Data aero_data ... end_aero_data

// SixDOF Pilot Manager and Control Inputs pilot_manager ... end_pilot_manager

// SixDOF Flight Control System Definition flight_controls ... end_flight_controls

// SixDOF Propulsion System Definition propulsion_data ... end_propulsion_data

// SixDOF Integrator integrator ...

// Fuel Transfers fuel_transfer ... end_fuel_transfer remove_fuel_transfer ...

// Fuel System Modification remove_fuel_tank ... modify_fuel_quantity ... end_modify_fuel_quantity
```txt
// SixDOF Subobjects   
subobject ... end_subobject   
// SixDOF Sequencers   
sequencer ... end_sequencer   
remove_sequencer ...   
// Parent-Relative Positioning and Separation   
parent.rel_x ...   
parent.rel_y ...   
parent.rel_z ...   
parent.rel_yaw ...   
parent.rel_pitch ...   
parent reli_roll ...   
separation_vx ...   
separation_vy ...   
separation_vz ...   
separation_omega_x ...   
separation_omega_y ...   
separation_omega_z ...   
// Size Factor Parameters   
size_factor_radius ...   
size_factor_min ...   
size_factor_max ...   
size_factor_volume_rate_m3_per_sec ...   
size_factor_area_rate_m2_per(sec ...   
size_factor_radius_rate_m_per(sec ...   
// Special Properties   
use_spherical-earth ...   
use_rotating-earth ...   
ignore_jettisoned Objects ...   
fixed_object ...   
// Object Creation Support   
nominal_max_mach ...   
nominal_max_alpha ...   
nominal_min_alpha ...   
nominal_max_beta ...   
end_point_massvehicle_type 
```

Point Mass Vehicle Type 是 WSF_POINT_MASS_SIX_DOF_MOVER 的一个关键组件。它定义了各种组件的特性（如质量属性、空气动力学、推进系统等），这些特性决定了WSF_POINT_MASS_SIX_DOF_MOVER 的性能。必须在 WSF_POINT_MASS_SIX_DOF_MOVER中引用之前定义一个 point_mass_vehicle_type。一个 point_mass_vehicle_type 可以从另一个 point_mass_vehicle_type 或 BASE_TYPE（PM6 对象类型的基类）派生。
```txt
// SixDOF Subobjects   
subobject ... end_subobject   
// SixDOF Sequencers   
sequencer ... end_sequencer   
remove_sequencer ...   
// Parent-Relative Positioning and Separation   
parent.rel_x ...   
parent.rel_y ...   
parent.rel_z ...   
parent.rel_yaw ...   
parent.rel_pitch ...   
parent reli_roll ...   
separation_vx ...   
separation_vy ...   
separation_vz ...   
separation_omega_x ...   
separation_omega_y ...   
separation_omega_z ...   
// Size Factor Parameters   
size_factor_radius ...   
size_factor_min ...   
size_factor_max ...   
size_factor_volume_rate_m3_per_sec ...   
size_factor_area_rate_m2_per(sec ...   
size_factor_radius_rate_m_per(sec ...   
// Special Properties   
use_spherical-earth ...   
use_rotating-earth ...   
ignore_jettisoned Objects ...   
fixed_object ...   
// Object Creation Support   
nominal_max_mach ...   
nominal_max_alpha ...   
nominal_min_alpha ...   
nominal_max_beta ...   
end_point_massvehicle_type 
```


