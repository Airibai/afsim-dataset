# 衰减的概念

衰减是指信号强度的损失，通常以分贝（dB）为单位进行测量。这种损失可能由于多种因素而发生，例如信号在长距离传输过程中变得失真或难以辨认。在工程中，衰减通常是介质路径长度的指数函数，并且在光学和化学光谱学中被称为 Beer-Lambert 定律。

# 应用场景

在 ALARM 模型中，衰减模型主要用于模拟雷达信号在大气中的传播损失。这对于在地球表面操作的雷达系统尤为重要，因为大气条件会显著影响信号的传播和检测能力。通过选择合适的衰减模型，可以更准确地预测和补偿这些损失，从而提高雷达系统的性能。

# 3.5.5.1.2. ALARM 杂波模型 Clutter Model

选择 ALARM 杂波模型的方法

ALARM 杂波模型可以通过以下两种机制之一进行选择：

在 WSF_RADAR_SENSOR 中包含一个 clutter_model 块，选择‘alarm’模型。

定义一个选择‘alarm’模型的 clutter_model 类型，然后在 WSF_RADAR_SENSOR 中使用clutter_model 命令引用该模型。

# 第一种情况的示例

在雷达传感器定义中直接选择‘alarm’模型：

```txt
sensor EX_RADAR WsF_RADAR_SENSOR transmitter  
...  
end_transmitter  
receiver  
...  
end receiver  
clutter_model alarm  
... parameters ...  
end_clutter_model  
end SENSOR 
```

# 第二种情况的示例

首先定义一个杂波模型，然后在雷达传感器中引用它：

```txt
clutter_model EX_RADAR_CLAMPTER alarm
... parameters ...
end_clutter_model
sensor EX_RADAR WSF_RADAR_SENSOR
transmitter
...
end_transmitter
receiver
...
end Receiver 
```

```txt
clutter_model EX_RADAR_CLAMPTER end_sensor 
```

# 灵活性和应用

这种功能非常有用，因为它允许在不修改雷达定义的情况下更改杂波模型。这对于需要在不同环境条件下测试雷达性能的场景尤其重要。通过这种机制，可以轻松地在不同的杂波模型之间切换，以评估其对雷达性能的影响。

# 杂波模型的背景

杂波是雷达信号处理中一个重要的因素，它包括地面反射、海面反射、天气、建筑物、鸟类和昆虫等的回波。选择合适的杂波模型对于提高雷达的目标检测能力至关重要。

# ALARM 杂波模型命令

在默认情况下，WSF-ALARM 接口将使用 4.11.1 全局环境定义 global_environment 来确定杂波反射率。ALARM 杂波模型通常只需要以下命令：

azimuth_angle_limit 和 azimuth_angle_increment：用于包括旁瓣杂波。  
maximum_range：用于提高运行时性能。

如果指定了 reflectivity、reflectivity_delta 或 statistic，则反射率将由输入值定义。

# 命令详解

azimuth_angle_limit <angle-value>

计算杂波返回的最大偏轴角。

与 ALARM 输入 CLUT_AZ_WIDTH 相同。

如果未指定或设置为 0，模型将仅使用一个主波束样本进行计算。

默认值：0.0（使用一个主波束样本）。

azimuth_angle_increment <angle-value>

用于计算杂波返回的方位角增量。

与 ALARM 输入 CLUT_ANGLE_INCR 相同。

如果未指定或设置为 0，模型将使用方位波束宽度进行计算。

默认值：0.0（使用完整的方位波束宽度）。

maximum_range <length-value>

计算杂波的最大范围。较短的范围减少执行时间，特别是对于使用地形高程数据（如DTED）的模拟。

与 ALARM 输入 CLUT_MAX_RANGE 相同。

默认值：两倍的计算杂波地平线范围。

reflectivity <db-ratio-value>

当 statistic 设置为 numerical 时使用的反射率值。

与 ALARM 输入 CLUT_REFLECTIVITY 相同。

默认值：0.0

reflectivity_delta <db-ratio-value>

关于 reflectivity 的增量杂波反射率值，仅在 statistic 设置为 numerical 时使用。杂波反射

率在范围 reflectivity ± reflectivity_delta 内均匀随机分布。

与 ALARM 输入 CLUT_DELTA_REFLECT 相同。

默认值：0.0

statistic [ mean | statistical | maximum | minimum | numerical ]

与 ALARM 输入 CLUT_STATISTIC 相同。

默认值：mean

random_seed <integer>

仅在 statistic 设置为 statistical 或 numerical 且 reflectivity_delta 设置时使用的随机数种子。必须是大于 1000 的数。

与 ALARM 输入 CLUT_SEED 相同。

默认值：1234567

sigmac <frequency-value>

杂波功率谱密度（PSD）中高斯部分的标准偏差。通常称为均方根杂波频率扩展。建议值为陆地 $1 0 \mathsf { H z }$ ，海洋 $5 0 \mathsf { H z }$ 。

与 ALARM 输入 SIGMAC 相同。

注意：当前未使用此输入。

decay_constant <frequency-value>^2

杂波功率谱密度（PSD）中反平方部分的二次衰减常数。建议值为 $1 0 ^ { \wedge . } 6 \mathsf { H z } ^ { 2 }$ 。

与 ALARM 输入 CLUT_DECAY 相同。

注意：当前未使用此输入。

use_legacy_data <boolean-value>

指定是否使用旧版杂波强度表。此旧表在 WSF1.7.5 发布之前使用。

默认值：禁用

use_native_terrain_masking <boolean-value>

指定是否使用本地 AFSIM地形遮蔽计算，而不是 ALARM 的。

此命令也可以在 ALARM 传播块中指定；对 ALARM 杂波和传播遮蔽计算均有效。

默认值：禁用

这些命令提供了灵活性和控制，以便在不同的雷达操作环境中优化杂波模型的性能。

# 3.5.5.1.3. ALARM 传播模型 Propagation Model

选择 ALARM 传播模型的方法

ALARM 传播模型可以通过以下两种机制之一进行选择：

在 WSF_RADAR_SENSOR 的发射器块中包含一个 propagation_model 块，选择‘alarm’模型。定义一个选择‘alarm’模型的 propagation_model 类型，然后在 WSF_RADAR_SENSOR 的发射器块中使用 propagation_model 命令引用该模型。

第一种情况的示例

在雷达传感器定义中直接选择‘alarm’模型：

```txt
sensor EX_RADAR WSF_RADAR_SENSOR transmitter propagation_model alarm 
```

```txt
... parameters ... end_propagation_model end_transmitter receiver ... end Receiver end_sensor 
```

# 第二种情况的示例

首先定义一个传播模型，然后在雷达传感器中引用它：

```txt
propagation_model EX_RADAR_propAGATION alarm
...
parameters ...
end_propagation_model
sensor EX_RADAR_WSF_RADAR_SENSOR
transmitter
...
propagation_model EX_RADAR_propAGATION
end_transmitter
receiver
...
end_receiver
end SENSOR 
```

# 命令详解

```txt
- propagation <boolean-value>
  指定是否使用多路径传播模型。
  默认值：true
  与ALARM输入PROPAGATION_SW相同。
```

```txt
- diffraction <boolean-value>
  指示是否使用球形地球/刀刃衍射模型。
  默认值：true
  与ALARM输入DIFFRACTION_SW相同。
```

```txt
- soil_moisture <real-value>
土壤中的湿度百分比[0..100]。
与ALARM输入SOIL_MOISTURE相同。
```

```txt
- soil_moisture_fraction <real-value>
土壤中的湿度分数[0..1]。
```

```txt
stddev_SURFACE_height <length-value>与ALARM输入STDDEV_SURFACE_HEIGHT相同。
```

```txt
- terrain_dielectric_constant <real-value>
地形介电常数。 
```

epsilon_one <real-value>与 ALARM 输入 EPSILON_ONE 相同。  
terrain_conductivity <real-value>地形导电率。  
sigma_zero <real-value>与 ALARM 输入 SIGMA_ZERO 相同。  
terrain_scattering_coefficient <real-value>地形散射系数。  
roughness_factor <real-value>与 ALARM 输入 ROUGHNESS_FACTOR 相同。  
sea_relaxation <real-value>与 ALARM 输入 SEA_RELAXATION 相同。  
sea_wind_speed <speed-value>与 ALARM 输入 SEA_WIND_SPEED 相同。  
water_temperature <temperature-value>与 ALARM 输入 WATER_TEMP 相同。  
water_type [ sea | lake ] 默认值：sea

与 ALARM 输入 WATER_TYPE 相同。

这些命令提供了对传播模型的详细控制，以便在不同的环境条件下优化雷达系统的性能。通过调整这些参数，可以更准确地模拟信号在不同地形和气象条件下的传播特性。

# 3.5.5.2. 杂波模型 clutter_model

```txt
clutter_model <derived-name> <base-name> ... Input for the clutter model ... end_clutter_model 
```

# Clutter Model 的使用

clutter_model 可以用于创建配置好的杂波模型，这些模型可以在 WSF_RADAR_SENSOR的定义中引用。<derived-name>是用户希望用来引用配置好的杂波模型的名称。<base-name>是可用的杂波模型之一：

```tcl
none   
surface_clutter_table alarm   
surface_clutter 
```

根据 Skolnik 的《Introduction to Radar》（第三版），“杂波强度被定义为 $\sigma ^ { 0 } F ^ { 4 }$ ，其中 $\sigma ^ { 0 }$ 是每单位面积的杂波截面， $F$ 是传播因子，有时在雷达方程中出现以考虑传播效应，如多路径反射、衍射和衰减。”默认的杂波强度表，如 Billingsley 的《Low Altitude Land Clutter》一书中所述，是地面覆盖和地形构造的函数，以及频率和极化的函数。

有效使用杂波模型杂波模型定义可以直接嵌入到雷达的定义中。例如，假设你有一个名为‘ex_radar.txt’的文件：

```txt
sensor EX_RADAR WSF_RADAR_SENSOR 
```

```txt
transmitter ... transmitter commands ... end_transmitter receiver ... receiver commands ... end Receiver clutter_model surface_clutter ... surface_clutter commands ... end_clutter_model end_sensor 
```

这种方法的问题在于，必须修改雷达定义才能更改或消除杂波模型。在许多生产使用中，这是不理想或不可行的。更理想的是提供一个可以被覆盖的“默认”杂波模型定义。

新的‘ex_radar.txt’文件将包含：

```txt
Define the default' clutter model   
clutter_model EX_RADAR_CLAMPER surface_clutter ...surface_clutter commands ...   
end_clutter_model   
sensor EX_RADAR WSF_RADAR_SENSOR transmitter ... transmitter commands ... end_transmitter receiver ...receiver commands ... end_receiver clutter_model EX_RADAR_CLAMPER #References the clutter model symbolically   
end_sensor 
```

然后要覆盖杂波模型：

```txt
include ex_radar.txt   
#Provide a new definition that overrides the existing definition. #This example disables clutter calculations.   
clutter_model EX_RADAR_CLAMPTER none   
end_clutter_model 
```

雷达模型将在最终创建雷达实例时使用 EX_RADAR_CLUTTER 的最后定义。

# 3.5.5.2.1. 不指定杂波模型 none

```txt
clutter_model <derived-name> none end_clutter_model 
```

3.5.5.2.2. 使用表格指定 surface_clutter_table  
```txt
clutter_model <derived-name> WSF_SURFACECLAUTTER_TABLE  
clutters  
altitude <length-value>  
range <length-value> clutter <power-value>  
...  
range <length-value> clutter <power-value>  
altitude <length-value>  
range <length-value> clutter <power-value>  
...  
range <length-value> clutter <power-value>  
...  
altitude <length-value>  
range <length-value> clutter <power-value>  
...  
range <length-value> clutter <power-value>  
...  
end_clutters  
end_clutter_model 
```

surface_clutter_table 通过一个表格来表示杂波，这个表格通常由 sensor_plot 生成。表格包含了杂波数据，作为目标高度和目标距离的函数。此外，如果表格是特定于某个地点的，它还会包含作为目标方位角函数的数据。

注意事项

每个高度块中的距离数量是独立的。每个高度块至少需要一个距离。

地点特定的表格

一个特定于地点的表格形式类似，但包括了方位角数据，适用于一组距离，如下所示：

```txt
clutter_model <derived-name> WSF_SURFACECLAUTTER_TABLE  
clutters  
altitude <length-value>  
bearing <angle-value>  
range <length-value> clutter <power-value>  
...  
range <length-value> clutter <power-value>  
...  
bearing <angle-value>  
// Full set of ranges:  
range <length-value> clutter <power-value>  
...  
range <length-value> clutter <power-value> 
```

```txt
...   
altitude <length-value> bearing <angle-value> range <length-value> clutter <power-value> ... range <length-value> clutter <power-value> ... end_clutters end_clutter_model 
```

# 3.5.5.2.3. ALARM 杂波 alarm

参见 3.5.5.1.2ALARM 杂波模型 Clutter Model。

# 3.5.5.2.4. 面杂波 surface_clutter

模型概述

surface_clutter 是一个算法模型，用于计算杂波功率。它使用 4.11.1 全局环境定义global_environment 中的参数来确定地形、地面覆盖和海况。

重要注意事项

对于地面平台，该杂波模型适用于天线高度相对于波高（由 sea_state指定）显著的船只。如果天线高度较低，可能会出现其他几何冲突，导致不期望的结果。

模型定义示例

```txt
clutter_model <derived-name> surface_clutter end_clutter_model 
```

使用旧数据

use_legacy_data <boolean-value>

指定是否使用旧版杂波强度表。

默认值：禁用

背景信息

在海面杂波建模中，天线高度对杂波响应有显著影响。靠近观察船只的倾斜波前比远处的波前更有利于雷达能量的反射，因为在大俯角时，波束向下看向附近的波前，导致一些能量可能垂直于波前的表面。此外，海况、频率、极化和掠射角等因素也会影响海面杂波的反射率。

对于地面或海面返回的典型表面杂波，地理地块的返回通常是静止的，但风对树木等的影响可能会引入多普勒频移，这在雷达系统的信号处理部分中是去除不需要信号的重要方法。

# 3.5.5.3. 雷达信号处理器 Radar Signal Processors

```txt
signal Processor <type-name> ...commands ... end_signal Processor 
```

# 3.5.5.3.1. 移动目标指示 mti_adjustment

```txt
signal Processor [mti_adjustment | gmti_adjustment]  
mti_adjustment_table ...  
gmti_adjustment_file <file-name>  
mti_adjustment_compound_file ...  
mti_maximum_range <length-value>  
end_signal处理器 
```

MTI（移动目标指示）调整用于处理慢速移动目标比同等大小的快速移动目标更难被MTI 传感器检测到的现象。该调整通过定义一个函数来捕捉这种非线性效应，函数定义了接收信号的衰减因子与闭合速度或多普勒频率之间的关系。

mti_adjustment_table

gmti_adjustment_table

调整 vs. 闭合速度

```txt
mti_adjustment_table //(or gmti_adjustment) closing_speed <speed-value> speed-1 adjustment <db-ratio-value> adjustment-1 closing_speed <speed-value> speed-2 adjustment <db-ratio-value> adjustment-2 ... closing_speed <speed-value> speed-n adjustment <db-ratio-value> adjustment-n end_mti_adjustment 
```

# 调整 vs. 多普勒频率

```txt
mti_adjustment_table //(or gmti_adjustment)  
doppler Frequency adjustment-1 <frequency-value> frequency-1 adjustment <db-ratio-value>  
doppler Frequency adjustment-2 <frequency-value> frequency-2 adjustment <db-ratio-value>  
...  
doppler Frequency adjustment-n <frequency-value> frequency-n adjustment <db-ratio-value>  
end_mti_adjustment 
```

# 表格要求

□ 至少需要两个条目，且 closing_speed 或 doppler_frequency 值必须单调递增。  
□ 如果提供负值，则表格被认为是非对称的；正值表示接近目标，负值表示远离目标。  
▫ 超出表格限制的速度或频率将被限制在适当的端点。

□ <adjustment-n>值通常是负的 dB 值，表示应用的调整。

mti_adjustment_file <file-name>

指定一个外部 MTI 表格，格式为 CSV 文件。文件应有一个标题行和两列：第一列是独立速度值，第二列是相关的衰减值。

mti_adjustment_compound_file <file-name>

指定一个外部 MTI 表格，格式为 CSV 文件。文件应有一个标题行和多于两列：最后一列是相关的衰减值，前面的列是独立速度值，表示不同频率。

# MTI 最大范围

mti_maximum_range <length-value>

指定仅用于 MTI“表格”的最大范围。如果目标距离更远，则不会应用任何 MTI 表格。

默认值：无限

这些配置和调整允许雷达系统更精确地检测和处理移动目标，特别是在复杂的环境中。通过调整这些参数，可以优化 MTI 雷达的性能，以适应不同的操作条件和目标特性。

# 3.5.5.3.2. MTI 处理器 mti_processor

```txt
signal Processor mti Processor  
maximum_range <length-value>  
number_of_stages <integer-value>  
interpulse_period_1 <time-value>  
interpulse_period_2 <time-value>  
clutter_lock <boolean-value>  
upwind <boolean-value>  
filtered_doppler_speed  
unfiltered_doppler_speed  
end_signal_PROCESSor 
```

在 AFSIM 中，mti_processor 是用于定义双延迟线消除器移动目标指示器（DDLC-MTI）信号处理器的模块。这个处理器计算目标响应，从而在进行最终的信号/噪声 $^ +$ 杂波 $+$ 干扰$( S / ( N { + } C { + } 1 )$ ）计算之前影响衰减的杂波功率。

如果只需要一个简单的 MTI 处理器，可以定义一个空的 mti_processor 块。

maximum_range <length-value>: 指定从传感器到目标的最大地面范围，只有在目标位于此范围内时才会进行 MTI 处理。默认值为 0 米。  
interpulse_period_1 <time-value> 和 interpulse_period_2 <time-value>: 可选值，表示脉冲间隔期。如果省略，则创建一个非交错的 MTI 系统，两个值均为脉冲重复频率（PRF）的倒数。  
number_of_stages <integer-value>: 指定 MTI 处理器中的阶段数。默认值为 1。  
clutter_lock <boolean-value>: 为与 SALRAM 模型兼容而提供。默认值为 true。注意，如果 clutter_lock 和 upwind 都为 true，则 clutter_lock 优先。  
upwind <boolean-value>: 也为与 SALRAM 模型兼容而提供。默认值为 true。注意，如果 clutter_lock 和 upwind 都为 true，则 clutter_lock 优先。  
filtered_doppler_speed 和 unfiltered_doppler_speed: 指定是否从多普勒速度计算中移

除 自 身 速 度 。 MTI 传 感 器 通 常 使 用 filtered_doppler_speed 。 默 认 值 为filtered_doppler_speed。

这些字段和参数帮助定义和调整 MTI 处理器的行为，以便在模拟中准确地反映目标检测和杂波处理的效果。

# 3.5.5.3.3. 简单多普勒信号处理器 simple_doppler

```txt
signal Processor simple_doppler minimum_doppler_speed maximum_doppler_speed filtered_doppler_speed unfiltered_doppler_speed debug   
end_signal Processor 
```

在 AFSIM 中，simple_doppler 是用于定义简单多普勒信号处理器的模块。这个处理器用于检测目标的多普勒速度（即开合速度）。

# 字段解释

minimum_doppler_speed <speed-value> 和 maximum_doppler_speed <speed-value>: 定义能够被检测到的目标多普勒速度的最小和最大值。默认范围是从 0 到无穷大。注意: 下面记录的 mti_adjustment 表提供了更高的精度来模拟移动目标的检测。  
filtered_doppler_speed 和 unfiltered_doppler_speed: 指定是否从多普勒速度计算中移除 自 身 速 度 。 MTI 传 感 器 通 常 使 用 filtered_doppler_speed 。 默 认 值 为filtered_doppler_speed。  
debug: 如果存在此标志，表示 MTI 信号处理器将输出额外的操作信息到系统控制台。

这些字段和参数帮助定义和调整 SimpleDoppler 处理器的行为，以便在模拟中准确地反映目标检测和多普勒速度处理的效果。

# 3.5.5.3.4. 移动目标检测 moving_target_detector

```txt
signal Processor moving_target_detector | moving_target_detector  
MTI Signal Processor Commands  
PD Signal Processor Commands  
zvf_SWITCH  
zvf_filter_bandwidth  
zvf_num_filter_poles  
zvf_filter_slr  
filtered_doppler_speed  
unfiltered_doppler_speed  
debug  
end_signalPROCESSOR 
```

在 AFSIM 中，moving_target_detector 或 moving_target_detection 是用于实现移动目

标检测器（MTD）的模块。MTD 是在 WSF_RADAR_SENSOR 中定义的一部分，其实现基于ALARM 的现有实现。MTD 是移动目标指示器（MTI）和脉冲多普勒（PD）的组合，并增加了零速度滤波器（ZVF）输入。

# MTD 系统概述

MTD 系统由两个信号通道组成：

第一通道: 包含串联连接到检测器的 MTI 和 PD 滤波。

第二通道: 包含 ZVF，用于零速度检测。在零速度通道中，目标仍需与存在的杂波信号竞争。

# MTD 响应

MTI 响应: MTD 响应中的 MTI 部分被强制大于“mti_min_response”，默认值为 0.0 dB。

传感器交互应用: 如果传感器检测结果包含发射器和 MTI 信号处理器，则会计算 MTD 响应。MTD 响应应用于结果的接收功率、杂波功率和噪声干扰功率。

# MTD 命令

zvf_switch <boolean-value>: 控制是否应用零速度滤波器效果。默认开启。  
zvf_filter_bandwidth <integer> <frequency-value>: 指定与 PRF(I) 对应的零速度滤波器带宽。对于匹配滤波器，输入 0.0。

注意: 对于匹配滤波器，多普勒滤波器带宽等于积分时间的倒数。如果 ZVF_BANDWIDTH(I)=0.0，它将重置为 PRF(I)/ZVF_FILTERS。

zvf_num_filter_poles <integer>: 指定切比雪夫滤波器的极点数（阶数），范围为 1 到 7。  
zvf_filter_slr <dbration-value>: 指定切比雪夫滤波器的主瓣与峰值旁瓣的差异，必须大于0.0 dB。  
filtered_doppler_speed 和 unfiltered_doppler_speed: 指定是否从多普勒速度计算中移除 自 身 速 度 。 MTI 传 感 器 通 常 使 用 filtered_doppler_speed 。 默 认 值 为filtered_doppler_speed。  
debug: 如果存在此标志，表示 MTI 信号处理器将输出额外的操作信息到系统控制台。

这些字段和参数帮助定义和调整 MTD 处理器的行为，以便在模拟中准确地反映目标检测和多普勒速度处理的效果。

# 3.5.5.3.5. 移动目标指示 moving_target_indicator

```txt
signal Processor moving_targetindicator mti_SWITCH mti_num_delays mti_min_response mti_num_gates mti_rangelimits mti_anglelimits filtered_doppler_speed unfiltered_doppler_speed debug 
```

在 AFSIM 中，moving_target_indication 是用于实现移动目标指示（MTI）的模块。MTI的实现基于 ALARM 的现有实现，并且可以作为 WSF_RADAR_SENSOR 的一部分进行定义。需要注意的是，雷达必须指定脉冲重复频率（PRF）或脉冲重复间隔（PRI）。

# MTI 响应

MTI 响应: MTI 响应被强制大于“mti_min_response”，默认值为 $0 . 0 { \mathsf { d B } }$ 。

传感器交互应用: 如果传感器检测结果包含发射器和 MTI 信号处理器，则会计算 MTI响应。MTI 响应应用于结果的接收功率、杂波功率和噪声干扰功率：

结果接收功率 $=$ 结果接收功率 *MTI 目标响应

结果杂波功率 $=$ 结果杂波功率 *MTI 杂波响应

结果噪声干扰功率 $=$ 结果噪声干扰功率 *MTI 噪声干扰响应

结果脉冲干扰功率 $=$ 结果脉冲干扰功率 *MTI 噪声干扰响应

结果相干干扰功率 $=$ 结果相干干扰功率 *MTI 相干干扰响应

# MTI 命令

mti_switch <boolean-value>: 控制是否应用移动目标指示器（MTI）效果。默认开启。  
mti_num_delays <integer-value>: 指定 MTI 延迟线的数量，必须大于 0。  
mti_min_response <power-value>: 指定 MTI 系统的最小功率响应，即 MTI 功率响应的底线值。默认值为 0.0dB。  
mti_num_gates <integer-value>: 指定 MTI 门的数量，范围为 1 到 4。如果为 0，则 MTI关闭。  
mti_range_limits <integer-value> <length-value> <length-value>: 指定第 I 个 MTI 门的最小和最大范围。

注意:MTI 处理在最小和最大门范围之间进行。在 MTI 门之外不进行 MTI 处理。

mti_angle_limits <integer-value> <angle-value> <angle-value>: 指定第 I 个 MTI 门的最小和最大方位角。  
注意:MTI 处理在最小和最大门角度之间进行。在 MTI 门之外不进行 MTI 处理。  
filtered_doppler_speed 和 unfiltered_doppler_speed: 指定是否从多普勒速度计算中移除 自 身 速 度 。 MTI 传 感 器 通 常 使 用 filtered_doppler_speed 。 默 认 值 为filtered_doppler_speed。  
debug: 如果存在此标志，表示 MTI 信号处理器将输出额外的操作信息到系统控制台。

这些字段和参数帮助定义和调整 MTI 处理器的行为，以便在模拟中准确地反映目标检测和多普勒速度处理的效果。

# 3.5.5.3.6. 脉冲多普勒 pulse_doppler

```txt
signal Processor pulse_doppler  
pd_num_filters  
pd_filter_bandwidth  
pd_num_filter_poles  
pd_filter_slr  
filtered_doppler_speed 
```

```txt
unfiltered_doppler_speed debug end_signal Processor 
```

在 AFSIM 中，pulse_doppler 是用于实现脉冲多普勒信号处理器的模块。脉冲多普勒雷达通过多普勒频移来检测和区分移动目标与静止杂波信号。这种处理策略在脉冲多普勒雷达和多模式雷达中使用，适合在包含大量慢速移动反射体的区域中操作。

# PD 响应

传感器交互应用: 如果传感器检测结果包含发射器和 PD 信号处理器，则会计算 PD 响应。

PD 响应应用于结果的接收功率、杂波功率和噪声/脉冲/相干干扰功率：

结果接收功率 $=$ 结果接收功率 *PD 目标响应

结果杂波功率 $=$ 结果杂波功率 *PD 杂波响应

结果噪声干扰功率 $=$ 结果噪声干扰功率 *PD 噪声干扰响应

结果脉冲干扰功率 $=$ 结果脉冲干扰功率 *PD 噪声干扰响应

结果相干干扰功率 $=$ 结果相干干扰功率 *PD 相干干扰响应

# PD 命令

pd_num_filters <integer-value>: 指定滤波器组中的多普勒滤波器数量。  
pd_filter_bandwidth <integer-value> <frequency-value>: 指定与 PRF(I) 对应的雷达多普勒滤波器带宽。对于匹配滤波器，输入 0.0。

注意: 对于匹配滤波器，多普勒滤波器带宽等于积分时间的倒数。如果PD_BANDWIDTH $( | ) = 0 . 0$ ，它将重置为 PRF(I)/PD_FILTERS。

pd_num_filter_poles <integer-value>: 指定切比雪夫滤波器的极点数（阶数），范围为 1到 7。  
pd_filter_slr <dbratio-value>: 指定切比雪夫滤波器的主瓣与峰值旁瓣的差异，必须大于0.0 dB。  
filtered_doppler_speed 和 unfiltered_doppler_speed: 指定是否从多普勒速度计算中移除 自 身 速 度 。 MTI 传 感 器 通 常 使 用 filtered_doppler_speed 。 默 认 值 为filtered_doppler_speed。  
debug: 如果存在此标志，表示 MTI 信号处理器将输出额外的操作信息到系统控制台。

这些字段和参数帮助定义和调整 Pulse Doppler 处理器的行为，以便在模拟中准确地反映目标检测和多普勒速度处理的效果。

# 3.5.5.3.7. 灵敏度时间控制 sensitivity_time_control

```tcl
signal Processor sensitivity_time_control  
stc_type ...  
stc_min_response ...  
stc_min_range ...  
stc_max_range ...  
stc_order ...  
stc_data_table ... 
```

```txt
[Independent_variable units <length-units>]  
[dependent_variable units <ratio-units>]  
end_stc_data_table  
end_signal Processor 
```

在 AFSIM 中，sensitivity_time_control 是用于实现灵敏度时间控制（STC）的模块。STC是一种用于雷达接收机的增益控制方法，旨在调节接收机的灵敏度，从而控制返回信号的强度。STC 的实现基于 SUPPRESSOR 的现有实现。

# STC 系统概述

STC 类型: STC 可以定义为 WSF_RADAR_SENSOR 的一部分。雷达必须指定脉冲重复频率（PRF）或脉冲重复间隔（PRI），因为模型使用 PRF 来计算最大无歧义范围，这在输入描述中用作最大范围。

# STC 响应

MIN, MAX, MIN/MAX RANGE STC 响应: 这些响应通过改变 STC 最小响应、最小/最大范围和 STC 阶数来修改。无歧义范围的计算如下：

最大无歧义范围 $= 0 . 5 ~ ^ { * }$ (光速 / PRF)

无歧义范围 $=$ 斜距 - TRUNC(斜距 / 最大无歧义范围) * 最大无歧义范围

最小无歧义范围 $=$ STC_Min_Range - floor(STC_Min_Range / 最大无歧义范围) * 最大无歧义范围

最大无歧义范围 $=$ STC_Max_Range - floor(STC_Max_Range / 最大无歧义范围) * 最大无歧义范围

# STC 类型为 MIN RANGE:

如果无歧义范围大于最小无歧义范围，STC 响应 $=$ stc_min_response * (无歧义范围 /最小无歧义范围)^STC_Order

否则，STC 响应 $=$ stc_min_response

# STC 类型为 MAX RANGE:

如果无歧义范围小于最大无歧义范围，STC 响应 $=$ (无歧义范围 / 最大无歧义范围)^STC_Order

否则，STC 响应 $= 0 . 0$ dB

# STC 类型为 MIN MAX RANGE:

如果无歧义范围小于最小无歧义范围，STC 响应 $=$ stc_min_response

如果无歧义范围大于最大无歧义范围，STC 响应 $= 0 . 0$ dB

否则，STC 响应 $=$ (无歧义范围 / 最大无歧义范围)^STC_Order

数据表 STC 响应: 当 STC 传感器信号处理器作为数据表类型操作时，STC 响应通过查找从目标到传感器接收机的斜距来确定。数据表中的 STC 响应被强制在 stc_min_response和 1.0 之间。

# STC 命令

stc_type <string-value>: 指 定 将 使 用 的 STC 信 号 处 理 类 型 。 有 效 值 为 min_range,max_range, min_max_range 或 data_table。默认值为 min_range。  
stc_min_response <db-ratio-value>: 指定 STC 响应的最小水平。输入为比率，值为 0 dB或更小（0.0 到 1.0 绝对值）。所有 STC 类型都需要此值。默认值为 1.0 绝对值 /0dB。  
stc_min_range <length-value>: 指定在 min_range 和 min_max_range STC 类型中 STC响应开始的最小斜距。在小于最小范围的范围内，STC 响应为 stc_min_response 值。默认值为 0.0。  
stc_max_range <length-value>: 指定在 max_range 和 min_max_range STC 类型中应用STC 响应的最大斜距。在大于最大范围的范围内，STC 响应为 0dB。默认值为 0.0。  
stc_order <real-value>: 用于 min_range, max_range 和 min_max_range STC 类型的 STC响应曲线的阶数。有效值为大于或等于零的实数。默认值为 4.0。  
stc_data_table … end_stc_data_table: 定义 STC 响应作为斜距的函数。如果 stc_type 为data_table，则需要此表。表值为长度值和比率对。独立和依赖变量单位命令是可选的，但如果未指定，则假定单位为米和 dB。  
debug: 如果存在此标志，表示 STC 信号处理器将输出额外的操作信息到系统控制台。

这些字段和参数帮助定义和调整 STC 处理器的行为，以便在模拟中准确地反映目标检测和信号处理的效果。

# 3.5.5.4. 天线命令 Antenna Commands

# 概述

注意 本节仅作为各种命令的参考。

注意 天线命令适用于任何使用电磁天线的设备，包括发射机、接收机和雷达波束。

注意 当范围和高度限制在多个地方使用时，例如在发射机和接收机上，优先考虑最后读取的条目。

# 命令

antenna_height <length-value> 定义子系统相对于其附着平台的高度。  
antenna_pitch <angle-value>   
antenna_tilt<angle-value> 定义子系统在俯仰平面内相对于平台的方向。这主要用于指定简单旋转系统天线的倾斜角度。

注意 此命令不得用于多波束雷达（例如，定义了多个波束的 WSF_RADAR_SENSOR）。在这些情况下，应使用 beam_tilt 命令在 beam_tilt 和 beam_tilt 块中。

注意 pitch 命令应用于指定固定安装系统的倾斜，但如果战斗机 AESA 系统要使用扫描稳定，则应使用此命令。

注意 如果使用了 :command_.articulated_part.pitch，则不得使用此命令。

minimum_altitude <length-value> 定义子系统能够观察目标的最小相对高度。默认值为负无穷大

注意 此值仅用于初步筛选，以确定子系统是否可能与其他对象交互。

注意 如果高度限制打算低于天线，则应将限制输入为负数。

maximum_altitude <length-value> 定义子系统能够观察目标的最大相对高度。

默认值为无穷大

注意 此值仅用于初步筛选，以确定子系统是否可能与其他对象交互。

注意 如果高度限制打算低于天线，则应将限制输入为负数。

minimum_range <length-value> 指定系统可以与其他对象交互的最小范围。

默认值为 0.0

注意 此值仅用于初步筛选，以确定子系统是否可能与其他对象交互。

maximum_range <length-value> 指定子系统可以与其他对象交互的最大范围。

默认值为无穷大

注意 此值仅用于初步筛选，以确定子系统是否可能与其他对象交互。

electronic_beam_steering_loss_exponent <value> 指定用于波束控制损耗计算的指数。

electronic_beam_steering_limit <angle-value> 指 定 应 用 于electronic_beam_steering_loss_exponent 的角度限制。

scan_mode [ fixed | azimuth | elevation | both | azimuth_and_elevation] 指示子系统相对 于当前提示的扫描方式：

▫ fixed- 子系统不移动。这是默认值。  
□ azimuth- 子系统仅在方位角上扫描。  
▫ elevation- 子系统仅在仰角上扫描。  
▫ both 或 azimuth_and_elevation - 子系统在方位角和仰角上都扫描。

默认值为 fixed。

scan_stabilization [ none | pitch | roll | pitch_and_roll ] 指 定 扫 描 体 积 （ 由azimuth_scan_limits 和 elevation_scan_limits 定义）是否“稳定”以抵消平台俯仰和滚动的影响。

默认值为 none。

azimuth_scan_limits <angle-value> <angle-value> 指定子系统在方位角上可以扫描的最小和最大角度。这些值仅在 scan_mode 为 azimuth 或 both 时适用。限制是相对于当前提示的。

默认值为 -180.0 度到 180 度。

elevation_scan_limits <angle-value> <angle-value> 指定子系统在仰角上可以扫描的最小和最大角度。这些值仅在 scan_mode为 elevation 或 both 时适用。限制是相对于当前提示的。

默认值为 -90.0 度到 90 度。

azimuth_field_of_view <angle-value> <angle-value> 指定子系统在方位角上可以看到的最小和最大角度。限制是相对于当前提示的。通常这些值应大于或等于azimuth_scan_limits（可能考虑到子系统定位到其扫描限制时波束的宽度）。

默认值为 -180.0 度到 180 度。

注意 如果启用了 scan_stabilization，则“视野”体积将以与扫描体积相同的方式稳定。

注意 这些值仅用于初步筛选，以确定对象是否可能与其他对象交互。

elevation_field_of_view <angle-value> <angle-value> 指定子系统在仰角上可以看到的最小 和 最 大 角 度 。 限 制 是 相 对 于 当 前 提 示 的 。 通 常 这 些 值 应 大 于 或 等 于elevation_scan_limits（可能考虑到子系统定位到其扫描限制时波束的宽度）。

默认值为 -90.0 度到 90 度。

注意 如果启用了 scan_stabilization，则“视野”体积将以与扫描体积相同的方式稳定。

注意 这些值仅用于初步筛选，以确定子系统是否可能与其他对象交互。

field_of_view … end_field_of_view 指定几何限制以确定子系统是否可能与其他对象交互。视野适用于任何使用电磁天线的设备，包括发射机、接收机和雷达波束。

```txt
field_of_view <field-of-view-type>
... Type Commands ...
end_field_of_view 
```

<field-of-view-type> 指定定义的视野类型及其相关命令。可用类型包括：

□ 矩形  
▫ 圆形  
□ 多边形  
▫ 赤道

注意 如果启用了 scan_stabilization，则“视野”体积将以与扫描体积相同的方式稳定。

注 意 默 认 提 供 矩 形 视 野 。 然 后 可 以 直 接 使 用 azimuth_field_of_view 和elevation_field_of_view 关键字进行配置。

接着专门介绍 field_of_view 中的矩形、圆形、多边形、赤道的配置。

# 3.5.5.4.1. 矩形 rectangular

```txt
field_of_view rectangular azimuth_field_of_view <angle-value> <angle-value> elevation_field_of_view <angle-value> <angle-value> end_field_of_view 
```

azimuth_field_of_view <angle-value> <angle-value> 指定子系统在方位角上可以看到的最小和最大角度。限制是相对于当前提示的。通常这些值应大于或等于azimuth_scan_limits（可能考虑到子系统定位到其扫描限制时波束的宽度）。

默认值为 -180.0 度到 180 度。

注意 这些值仅用于初步筛选，以确定对象是否可能与其他对象交互。

elevation_field_of_view <angle-value> <angle-value> 指定子系统在仰角上可以看到的最小 和 最 大 角 度 。 限 制 是 相 对 于 当 前 提 示 的 。 通 常 这 些 值 应 大 于 或 等 于elevation_scan_limits（可能考虑到子系统定位到其扫描限制时波束的宽度）。

默认值为 -90.0 度到 90 度。

注意 这是默认的视野类型。

# 3.5.5.4.2. 圆形 circular

```txt
field_of_view circular half_angle <angle-value> end_field_of_view 
```

定义：圆形视野定义了一个圆锥形的实心角。

half_angle <angle-value> 指定子系统从中心到圆边缘的半角度。

# 3.5.5.4.3. 多边形 polygonal

```txt
field_of_view polygonal azimuth_elevation <angle-value> <angle_value> # 1st point 
```

```txt
azimuth_elevation <angle-value> <angle_value> # 2nd point  
azimuth_elevation <angle-value> <angle_value> # 3rd point  
...  
azimuth_elevation <angle-value> <angle_value> # nth point  
end_field_of_view 
```

定义：多边形视野由从观察点出发的一系列方位角和仰角值定义。至少需要三个值。

azimuth_elevation <angle-value> <angle-value> 指定定义多边形视野的点的方位角和仰角值。

# 3.5.5.4.4. 赤道 equatorial

```txt
field_of_view equatorial  
equatorial_field_of_view <angle-value> <angle-value>  
polar_field_of_view <angle-value> <angle-value>  
end_field_of_view 
```

赤道视野定义了一个矩形视野，但与矩形视野不同的是，它的方向球体是一个天球，其赤道与地球的投影瞬时赤道相匹配，而不是与当地地平线（即当地东北下坐标系中的东北平面）相匹配的天球。赤道视野与类似定义的矩形视野之间的区别在于围绕传感器指向方向的视差角旋转。

equatorial_field_of_view <angle-value> <angle-value> 指定子系统在赤道坐标（赤道天球的方位角）上可以看到的最小和最大角度。限制是相对于当前提示的。

默认值为 -180.0 度到 180 度。

注意 这些值仅用于初步筛选，以确定对象是否可能与其他对象交互。

polar_field_of_view <angle-value> <angle-value> 指定子系统在极坐标（赤道天球的极角）上可以看到的最小和最大角度。限制是相对于当前提示的。

默认值为 -90.0 度到 90 度。

注意事项

赤道视野：这种视野类型适用于需要考虑地球旋转影响的系统，特别是在天文观测或需要精确地球定位的应用中。

# 3.5.5.5. 天线模式 antenna_pattern

```txt
antenna_pattern <pattern-name>
<pattern-type-name>
Common Commands
... Available Antenna Patterns Commands ...
end_antenna_pattern 
```

天线模式用于发射机和接收机命令中，以定义通信和传感设备的天线增益。

<pattern-name> 指定天线模式的名称。  
<pattern-type-name> 指定可用的天线模式之一，包括：

□ 方位/仰角表  
□ 均匀或恒定模式

□ 圆形 sine(x)/x 模式  
□ 矩形 sine(x)/x 模式  
▫ 余割模式  
□ ALARM 天线模式文件  
□ GENAP 模式  
□ 复杂电子控制/扫描阵列模式  
□ 元件电子控制/扫描阵列 (ESA) 模式  
□ 电子控制/扫描阵列 (ESA) 模式

# 通用命令

minimum_gain <db-ratio-value> 返回的最小增益。

默认值：-300 dB

gain_adjustment <db-ratio-value> 应用于原始增益的调整因子。这在希望重用由文件（如方位/仰角表）定义的模式并简单缩放定义时特别有用。

默认值：1.0（无调整）

注意 gain_adjustment 和 gain_adjustment_table 可以一起使用。结果在对数空间中是相加的（在线性空间中是相乘的）。

gain_adjustment_table … end_gain_adjustment_table 该命令提供了定义增益的频率相关调整的方法。点定义了一个曲线，其 x 轴是频率的对数，y 轴是 dB 中的调整因子。

线性插值用于推导中间频率的值。频率超出表范围的信号使用适当端点的值（即，不进行外推）。

表格格式为：

```txt
gain_adjustment_table frequency <frequency-value> <db-ratio-1> frequency <frequency-value> <db-ratio-2> ... frequency <frequency-value> <db-ratio-n> end_gain_adjustment_table 
```

规则：

条目必须按频率单调递增顺序排列。

必须至少有两个条目，除非没有提供条目，则视为未提供表。

注意 gain_adjustment 和 gain_adjustment_table 可以一起使用。结果在对数空间中是相加的（在线性空间中是相乘的）。

# 3.5.5.5.1. 方位/仰角表模式 Azimuth/Elevation Table

```txt
pattern_table #方位-仰角表定义 azimuth_beamwidth <angle-value> elevation_beamwidth <angle-value> #通用命令
```

```txt
minimum_gain <db-ratio-value> gain_adjustment <db-ratio-value> gain_adjustment_table ... end_gain_adjustment_table end ANTenna_pattern 
```

定义：使用标准的方位-仰角表定义格式来定义天线模式。

azimuth_beamwidth <angle-value> 定义方位角上的波束宽度。

默认值：无 - 必须提供

elevation_beamwidth <angle-value> 定义仰角上的波束宽度。

默认值：无 - 必须提供

# 3.5.5.5.2. 均匀或恒定模式 Uniform or Constant Pattern

```txt
antenna_pattern <pattern-name>
uniform_pattern
    peak_gain <db-ratio-value>
azimuth_beamwidth <angle-value>
elevation_beamwidth <angle-value>
# Common Commands
minimum_gain <db-ratio-value>
gain_adjustment <db-ratio-value>
gain_adjustment_table ... end_gain_adjustment_table
end_antenna_pattern 
```

定义：定义一个模式，其增益在指定的波束宽度限制内为 peak_gain，在其他地方为minimum_gain。

peak_gain <db-ratio-value> 定义相对于理想各向同性天线的天线峰值增益。

默认值：1dB

azimuth_beamwidth <angle-value> 定义方位角上的波束宽度。

默认值：180 度

elevation_beamwidth <angle-value> 定义仰角上的波束宽度。

默认值：90 度

# 3.5.5.5.3. 圆形 sine(x)/x 模式 Circular sine(x)/x Pattern

```perl
antenna_pattern <pattern-name>   
circular_pattern   
peak_gain <db-ratio-value>   
beamwidth <angle-value>   
#Common Commands   
minimum_gain <db-ratio-value>   
gain_adjustment <db-ratio-value>   
gain_adjustment_table ... end_gain_adjustment_table 
```

定义：定义一个具有圆形对称性的 sine(x)/x 模式。

peak_gain <db-ratio-value> 定义相对于理想各向同性天线的天线峰值增益。

默认值：1dB

beamwidth <angle-value> 定义半功率波束宽度（增益达到峰值增益一半的点所夹的角度）。

# 3.5.5.5.4. 矩形 sine(x)/x 模式 Rectangular sine(x)/x Pattern

```txt
antenna_pattern <pattern-name>
rectangular_pattern
    peak_gain <db-ratio-value>
azimuth_beamwidth <angle-value>
elevation_beamwidth <angle-value>
# Common Commands
minimum_gain <db-ratio-value>
gain_adjustment <db-ratio-value>
gain_adjustment_table ... end_gain_adjustment_table
end_antenna_pattern 
```

定义：定义一个 sine(x)/x 模式，其中方位角和仰角的波束宽度可以不同。

peak_gain <db-ratio-value> 定义相对于理想各向同性天线的天线峰值增益。

默认值：1dB

azimuth_beamwidth <angle-value> 定义方位角上的半功率波束宽度（增益达到峰值增益一半的点所夹的角度）。  
elevation_beamwidth <angle-value> 定义仰角上的半功率波束宽度（增益达到峰值增益一半的点所夹的角度）。

# 3.5.5.5.5. 余割平方模式 Cosecant Pattern

```txt
antenna_pattern <pattern-name>   
cosecant_squared_pattern peak_gain <db-ratio-value> azimuth_beamwidth <angle-value> elevation_beamwidth <angle-value> minimum_elevation_for_peak_gain <angle-value> elevation_of_peak/csc2 Boundary <angle-value> maximum_elevation_for_csc2 <angle-value> #Common Commands minimum_gain <db-ratio-value> gain_adjustment <db-ratio-value> 
```

```txt
gain_adjustment_table ... end_gain_adjustment_table end_antenna_pattern 
```

余割平方模式用于定义一种天线模式，该模式在不同的仰角范围内使用不同的增益模式：

□ 在小于 minimum_elevation_for_peak_gain 的仰角下使用 $\mathsf { s i n e } ( \mathsf { x } ) / \mathsf { x }$ 模式。  
▫ 在 [minimum_elevation_for_peak_gain, elevation_of_peak/csc2_boundary] 范 围 内使用峰值增益。  
▫ 在 [elevation_of_peak/csc2_boundary, maximum_elevation_for_csc2] 范围内使用余割平方模式。  
□ 在大于 maximum_elevation_for_csc2 的角度上使用 sine(x)/x 模式。

peak_gain <db-ratio-value> 定义相对于理想各向同性天线的天线峰值增益。

默认值：1.0 dB

azimuth_beamwidth <angle-value> 定义方位角上的半功率波束宽度（增益达到峰值增益一半的点所夹的角度）。用于确定与方位角相关的增益部分。  
elevation_beamwidth <angle-value> 定义仰角上的半功率波束宽度（增益达到峰值增益一半的点所夹的角度）。用于确定仰角在余割平方区域以上或以下时的增益部分。  
minimum_elevation_for_peak_gain <angle-value> 定义峰值增益值的最小仰角。

注意 非零值可能导致雷达在 0 度时使用非峰值增益进行转动或扫描时出现问题。

elevation_of_peak/csc2_boundary <angle-value> 定义峰值余割平方边界值的仰角。  
maximum_elevation_for_csc2 <angle-value> 定义峰值增益值的最大仰角。

# 3.5.5.5.6. 电子控制/扫描阵列 (ESA) 模式 Electronic Steered/Scanned Array (ESA) Pattern

```txt
antenna_pattern <pattern-name>
esa_pattern
    debug
    element-spacing_x <length-value>
    element-spacing_y <length-value>
    length_x <length-value>
    length_y <length-value>
    number_elements_x <integer-value>
    number_elements_y <integer-value>
    amplitude_quantization_bits <integer-value>
    phase_quantization_bits <integer-value>
failed_elements_ratio [0.0 .. 1.0]
element_pattern <pattern-name>
back_baffled <boolean-value>
lattice <lattice-type>
distribution_type <distribution-type>
# Common Commands 
```

```txt
minimum_gain <db-ratio-value> gain_adjustment <db-ratio-value> gain_adjustment_table ... end_gain_adjustment_table end ANTenna_pattern 
```

电子控制/扫描阵列天线模式生成器是一个在 x-y 平面上定义的 MxN 阵列（x 为方位方向，y为仰角方向）。这种模式通过遍历所有元素来获取每个元素的贡献和相位信息，然后进行求和，因此计算时间为 $\mathsf { N } ^ { \wedge } 2$ ，可能不适合时间关键的应用（例如，实时模拟应用/演习）。

debug 启用调试。  
默认值：false   
element_spacing_x <length-value> 阵列的水平元素间距。需要定义 number_elements_x或 length_x。  
element_spacing_y <length-value> 阵列的垂直元素间距。需要定义 number_elements_y或 length_y。  
length_x <length-value> 总 水 平 阵 列 长 度 。 需 要 定 义 number_elements_x 或element_spacing_x。  
length_y <length-value> 总 垂 直 阵 列 长 度 。 需 要 定 义 number_elements_y 或element_spacing_y。  
number_elements_x <integer-value> 阵列水平方向的单个元素数量。需要定义 length_x或 element_spacing_x。  
number_elements_y <integer-value> 阵列垂直方向的单个元素数量。需要定义 length_y或 element_spacing_y。  
amplitude_quantization_bits <integer-value> 用于量化阵列中每个元素的幅度响应的位数。参考值设置为幅度 1。  
phase_quantization_bits <integer-value> 用于量化阵列中每个元素的相位响应的位数。参考值设置为 2π弧度（360 度）。  
failed_elements_ratio <real-value> 阵列中失效元素的比例。

注意 实际失效元素在每个模式实例的模拟初始化期间随机选择，并在整个模拟过程中使用。

默认值：0.0

element_pattern <pattern-name> 通过天线模式名称指定阵列中所有元素的元素模式。注意 元素模式应相对于各向同性元素（即，dBi- 归一化为 1.0（0.0dB））。

默认值：假定为各向同性元素

back_baffled <boolean-value> 指定天线元素是否在方位角[-90, 90]度之外进行背面遮挡。默认值：true  
lattice <lattice-type> 用于定义元素位置的晶格类型。类型包括：  
rectangular 使用矩形晶格，所有元素在行/列中对齐。  
triangular 使用三角形晶格，其中相应的行偏移一个 element_spacing_x 的一半。默认值：rectangular  
distribution_type <distribution-type> 应用的加权分布，可用分布包括：

□ uniform 在阵列元素之间应用均匀分布。

□ taylor 在阵列元素之间应用泰勒分布。

额外所需输入：

sidelobe_level_x <db-ratio-value> 阵列 x 方向的旁瓣电平，范围为 15 dB 到 55 dB。  
sidelobe_level_y <db-ratio-value> 阵列 y 方向的旁瓣电平，范围为 15 dB 到 55 dB。  
n_bar_x <integer-value> 阵列 x 方向的条数，范围为[1, 2, …]。  
n_bar_y <integer-value> 阵列 y 方向的条数，范围为[1, 2, …]。

默认值：uniform

# 3.5.5.5.7. ALARM 天线模式文件 ALARM Antenna Pattern File

```txt
antenna_pattern <pattern-name>
    alarm_pattern
        file <file-name>
            gain-correction <db-ratio-value>
        # Common Commands
            minimum_gain <db-ratio-value>
            polarization [horizontal|vertical|default]
            gain_adjustment <db-ratio-value>
            gain_adjustment_table ... end_antenna_pattern_gain_adjustment_table
            end_alarmpattern
end_antenna_pattern 
```

ALARM 天线模式使用一个定义文件来指定天线模式。

▪ file<file-name> 包含天线模式定义的文件名。将对该值应用文件路径处理。  
gain_correction <db-ratio-value> 是 gain_adjustment 命令的同义词。  
polarization [horizontal|vertical|default] 提供一个极化以匹配天线模式文件中指定的一个或多个极化。仅当天线模式文件中指定了极化时才需要此输入；否则应省略。

# 3.5.5.5.8. GENAP 天线模式 GENAP Pattern

```tcl
antenna_pattern <pattern-name>  
genap_pattern  
peak_gain <db-ratio-value>  
aperture_shape [rectangular | elliptical | circular]  
azimuth_distribution [uniform | cosine | bw/sll]  
azimuth_beamwidth <angle-value>  
azimuth_exponent [1..4]  
azimuth_side_lobe_level <db-ratio of 15 db to 55 db>  
elevation_distribution [uniform | cosine | bw/sll | cosecant]  
elevation_beamwidth <angle-value>  
elevation_exponent [1..4]  
elevation_side_lobe_level <db-ratio of 15 db to 55 db>  
elevation_cosecant_limit <angle-value>  
elevation_beamwidth <angle-value>  
# Common Commands 
```

```txt
minimum_gain <db-ratio-value> gain_adjustment <db-ratio-value> gain_adjustment_table ... end_gain_adjustment`table end ANTenna_pattern 
```

GENAP 天线模式源自技术雷达分析和建模（TRAMS）雷达分析系统，允许使用多种方法定义天线模式。

peak_gain <db-ratio-value> 定义相对于理想各向同性天线的天线峰值增益。  
aperture_shape [ rectangular | elliptical | circular ] 指定天线孔径的形状。  
azimuth_distribution [ uniform | cosine | bw/sll ] 指定方位角方向的分布类型。  
azimuth_beamwidth <angle-value> 定义方位角上的波束宽度。  
azimuth_exponent [ 1 .. 4 ] 指定方位角方向的指数。  
azimuth_side_lobe_level <db-ratio of 15 db to 55 db> 指定方位角方向的旁瓣电平。  
elevation_distribution [ uniform | cosine | bw/sll | cosecant ] 指定仰角方向的分布类型。  
elevation_beamwidth <angle-value> 定义仰角上的波束宽度。  
elevation_exponent [ 1 .. 4 ] 指定仰角方向的指数。  
elevation_side_lobe_level <db-ratio of 15 db to 55 db> 指定仰角方向的旁瓣电平。  
elevation_cosecant_limit <angle-value> 指定仰角方向的余割限制。

# 3.5.5.5.9. 复 杂 电 子 控 制 / 扫 描 阵 列 模 式 Element Electronic Steered/Scanned Array (ESA)

# Pattern

```txt
antenna_pattern <pattern-name>  
element_esa_pattern  
... Base ESA Commands ...  
... Common Commands ...  
aperture_efficiencies <efficiency-value-x real-value> <efficiency-value-y real-value>  
aperture_efficiency <real-value>  
average_element_spacing_x <length-value>  
average_element_spacing_y <length-value>  
elementLocations ... end_element Locations  
end_antenapattern 
```

复杂电子控制/扫描阵列天线模式是对基础电子控制/扫描阵列 (ESA) 模式的扩展，包含边缘角度修改和阵列细分，以支持需要阵列细分的多波束成形应用。

# 详细说明

edge_angle_x <angle-value> 关于 Z 轴相对于 x 轴的元素旋转偏移。默认值为 0 度。  
edge_angle_y <angle-value> 关于 Z 轴相对于 y 轴的元素旋转偏移，角度从 x 轴开始计算。默认值为 90 度。  
array_subdivision_table … end_array_subdivision_table 该块定义了 X 和 Y 细分比率作为波束数量的函数。当系统定义了多个波束时，阵列根据表中的比率进行细分。格式如下：

```txt
array_subdivision_table
```

```txt
beam_count 1 <x-ratio> <y-ratio> beam_count 2 <x-ratio> <y-ratio> ... beam_count N <x-ratio> <y-ratio> end_array_subdivision_table 
```

beam_count <beam-count-integer-value> <x-ratio> <y-ratio> 指定波束数量以及在 x 和 y方 向 上 应 用 的 比 率 。 阵 列 长 度 和 / 或 元 素 数 量 将 按 此 比 率 划 分 。<beam-count-integer-value> 应在范围 [1, 2, .., N] 内按递增顺序排列。比率必须大于 0.0且小于或等于 1.0。

注意 目前此功能仅在定义了多个波束的 WSF_RF_JAMMER 系统中可用。系统可以创建的每个波束数量的值都应在 beam_count表中考虑。

默认值：无阵列细分

# 其他注意事项

计算复杂性：该天线模式通过遍历所有元素来求和每个元素的贡献和相位信息，因此具有 N^2 的计算复杂性，可能不适合性能要求较高的应用，例如具有实时约束的应用。

波束控制：电子控制的阵列天线可以快速改变波束方向和形状，以适应不同的应用需求，如雷达、通信和干扰抑制等。

# 3.5.5.6. 传播模型 propagation_model

```txt
propagation_model <derived-name> <base-name> ... Input for the propagation model ... end_propagation_model 
```

propagation_model 用于创建配置的传播模型，这些模型可以在发射机定义中的propagation_model 块中引用。

□ <derived-name> 是您希望分配给配置传播模型的名称。用户希望通过此名称引用配置的传播模型。  
□ <base-name> 是可用的传播模型之一：

none：一个“虚拟”传播模型，不产生任何效果。  
fast_multipath：实现了在《Radar Range Performance Analysis》中定义的方法，计算由于信号在圆形、粗糙地球表面反射而导致的干涉效应。  
ground_wave_propagation：仅应与 WSF_SURFACE_WAVE_RADAR_SENSOR 一起使用的特殊模型。  
alarm：来自 ALARM 雷达模型的高保真模型，仅在不可导出版本中可用。

# 传播模型的有效使用

传播模型定义可以直接嵌入雷达的定义中。例如，假设您有一个名为 ex_radar.txt 的文件：

```txt
sensor EX_RADAR WSF_RADAR_SENSOR transmitter ... transmitter commands ... 
```

```txt
propagation_model fast_multipath
    ... fast_multipath model commands ...
    end_propagation_model
    end_transmitter
    receiver
    ... receiver commands ...
    end_receiver
end SENSOR 
```

这种方法的问题在于，必须修改雷达定义才能更改或消除传播模型。在许多生产使用中，这是不可取或不可行的。更理想的是提供一个可以被覆盖的“默认”传播模型定义。

新的 ex_radar.txt 将包含：

```txt
Define the 'default' propagation model   
propagation_model EX_RADAR_propAGATION fast multipath ... fastmultipath model commands ...   
end_propagation_model   
sensor EX_RADAR WSF_RADAR_SENSOR transmitter ... transmitter commands ... propagation_model EX_RADAR_propAGATION # References the propagation model symbolically end_transmitter receiver ... receiver commands ... end_receiver   
end_sensor 
```

然后要覆盖传播模型：

```txt
include ex_radar.txt   
#Provide a new definition that overrides the existing definition. #This example now uses the none propagation model.   
propagation_model EX_RADAR_propAGATION none   
end_propagation_model 
```

雷达模型将在最终创建雷达实例时使用 EX_RADAR_PROPAGATION 的最后定义。

# 3.5.5.6.1. 空的传播模型 none

```txt
propagation_model <derived-name> none end_propagation_model 
```

none：一个“虚拟”传播模型，不产生任何效果。

# 3.5.5.6.2. 快速多路径 fast_multipath

```txt
propagation_model <derived-name> fast Multipath soil_moisture_fraction ... surface_roughness ... end_propagation_model 
```

实现了在《Radar Range Performance Analysis》中定义的方法，计算由于信号在圆形、粗糙地球表面反射而导致的干涉效应。可以提供两个因素来定义反射点表面的属性。

soil_moisture_fraction [0.0 .. 1.0]：定义土壤的湿度含量。默认值为 0.15。  
surface_roughness <length-value>：定义表面高度变化的标准偏差。默认值为 3.0 米。

# 3.5.5.6.3. alarm 传播模型 alarm

参见：3.5.5.1.3ALARM 传播模型 Propagation Model。

# 3.5.5.6.4. 地波传播模型 ground_wave_propagation

仅应与 WSF_SURFACE_WAVE_RADAR_SENSOR 一起使用的特殊模型。

# 3.5.5.7. 衰减模型 attenuation_model

```txt
attenuation_model <derived-name> <base-name> ... Input for the attenuation model ... end Attenuation_model 
```

attenuation_model 用于创建配置的衰减模型，这些模型可以在发射机定义中的attenuation_model 块中引用。

□ <derived-name> 是您希望分配给配置衰减模型的名称。用户希望通过此名称引用配置的衰减模型。  
□ <base-name> 是可用的衰减模型之一：

none：一个“虚拟”衰减模型，不产生任何效果。  
simple：简单的衰减模型。  
itu：国际电信联盟（ITU）定义的衰减模型。  
blake：Blake 模型。  
WSF_OPTICAL_ATTENUATION：光学衰减模型。  
WSF_TABULAR_ATTENUATION：表格式衰减模型。

衰减模型的有效使用

衰减模型定义可以直接嵌入雷达的定义中。例如，假设您有一个名为 ex_radar.txt 的文件：

```txt
sensor EX_RADAR WsF_RADAR_SENSOR transmitter ... transmitter commands ... attenuation_model itu 
```

```txt
...itu model commands ... end_attenuation_model end_transmitter receiver ... receiver commands ... end_receiver end SENSOR 
```

这种方法的问题在于，必须修改雷达定义才能更改或消除衰减模型。在许多生产使用中，这是不可取或不可行的。更理想的是提供一个可以被覆盖的“默认”衰减模型定义。

```txt
Define the default' attenuation model   
attenuation_model EX_RADARAttENUATION itu ...itu model commands...   
end Attenuation_model   
sensor EX_RADAR WSF_RADAR_SENSOR transmitter ... transmitter commands ... attenuation_model EX_RADARAttENUATION # References the attenuation model symbolically end_transmitter receiver ...receiver commands ... end_receiver   
end SENSOR 
```

然后要覆盖衰减模型：

```txt
include ex_radar.txt   
#Provide a new definition that overrides the existing definition. #This example now uses the blake attenuation model. attenuation_model EX_RADARAttENUATION blake end Attenuation_model 
```

雷达模型将在最终创建雷达实例时使用 EX_RADAR_ATTENUATION 的最后定义。

衰减的基本概念

衰减是指信号在传播过程中强度的减少。它可以由传输损耗、反射或吸收引起。在电气系统中，衰减是信号电压沿着导线或其他传输线流动时的减少。衰减通常以分贝（dB）为单位表示，表示信号在传输过程中功率的损失。

# 3.5.5.7.1. 空的衰减模型 none

```txt
attenuation_model <derived-name> none end Attenuation_model 
```

一个“虚拟”衰减模型，不产生任何效果。

# 3.5.5.7.2. 简单衰减模型 simple

描述：此模型提供了一种机制，可以指定恒定的特定衰减（每单位长度的信号损失）或恒定因子（衰减始终相同）。适用于几何条件相对独立且不需要计算更复杂模型的情况，也适用于某些简单情况。

specific_attenuation <value> <db-ration-unit>/<length-unit>：指定每单位长度的信号损失，适用于路径几乎平行于地球表面的情况。

示例：specific_attenuation 0.001 db/km

attenuation_factor <db-ratio-value>：指定信号值的恒定乘数（增益因子），适用于几何形状固定的情况。

示例：attenuation_factor -3.0 db

# 3.5.5.7.3. itu

此模型使用国际电信联盟（ITU）定义的方法来确定 1-1000 GHz 频率的 RF 信号的衰减因子。

使用 ITU 的推荐标准，如“ITU-R P.676-8”、“ITU-R P.838-3”和“ITU-R P.840-4”。

如果在 4.11.1 全局环境定义 global_environment 中定义了 rain_rate，则计算雨水引起的衰减。

如果定义了 cloud_altitude_limits 和 cloud_water_density，则计算云或雾引起的衰减。

# 3.5.5.7.4. blake

描述：使用 L.V.Blake编写的大气吸收模型来确定衰减因子，适用于频率在 100MHz 到10GHz 之间的情况。

注意：此选择仅在发射机或目标在（或非常接近）地表时有效。

# 3.5.5.7.5. erace

描述：使用来自 ESAMS/ALARM/RADGUNS 公共环境（EARCE）的大气吸收模型来确定衰减因子。

注意：此选择仅在发射机或目标在（或非常接近）地表时有效。

# 3.5.5.7.6. 光学衰减 WSF_OPTICAL_ATTENUATION

```txt
attenuation_model <name-or-type> WSF_OPTICAL AttENUATION # Explicit Table Selection Commands internal_table ... external_table ... # Implicit Table Selection Commands 
```

```txt
atmosphere_model ...  
haze_model ...  
# Miscellaneous Commands  
adjustment_factor ...  
# Conversion Commands  
spectral_data_conversion ...  
optical_path_conversion ..  
end_attenuation_model 
```

用于视觉和红外系统，如 WSF_EOIR_SENSOR 和 WSF_IRST_SENSOR。这些模型提供了不同的机制来处理信号在传播过程中的衰减，适用于不同的应用场景和条件。

WSF_OPTICAL_ATTENUATION 是一种用于视觉和红外系统（如 WSF_EOIR_SENSOR 和WSF_IRST_SENSOR）的衰减模型。该模型计算给定交互的衰减，具体过程如下：

# 大气层模型

大气被视为包围地球的一系列同心层。

对于路径经过的每一层，计算其透射率：

$$
\tau_ {i} = e ^ {- \alpha_ {i} R _ {i}}
$$

其中，

$a _ { i }$ 是该层的衰减系数， $R _ { i }$ 是通过该层的斜距。

整个路径的透射率为：

$$
\tau = \prod_ {i} \tau_ {i}
$$

衰减系数的确定

模型使用一个表格来定义层边界的高度以及确定这些高度处衰减系数的机制。

对于特定高度，系数可能是常数，也可能更复杂。对于特定层的系数，将是路径通过该层的端点高度的系数的平均值（如果路径在层内开始或结束，可能需要插值）。

# 表格构建 Table Construction

spectral_data_conversion 命令：用于将高保真大气模型（如 MODTRAN）的光谱透射率数据转换为可用于此模型的数据。

高保真程序在选定的高度和多个范围内运行。对于每个点（高度/范围对），程序生成作为波长函数的透射率。

首先在该点积分透射率，得到该点光谱的平均透射率。

对于每个高度，得到一组定义透射率与范围关系的点。然后通过以下公式导出衰减系数：

$$
a _ {i} = l n (\tau_ {i}) / R _ {i}
$$

对于单色光，衰减系数几乎是常数，验证了使用 Beer-Lambert 定律的假设。

对于更复杂的情况，表格包含直线的系数，以便通过已知层的范围恢复系数。

# 复杂情况处理

在某些情况下，线性拟合误差过大，因此允许每个高度有多个段。转换过程尝试找到尽可能长的范围段，使直线产生可接受的误差。

由于不同波长与大气的相互作用方式不同，导致衰减系数在不同范围内可能以非线性方式变化。

这种模型通过考虑大气层的复杂性和不同波长的相互作用，提供了对视觉和红外系统的精确衰减计算。

# 显式表选择命令 Explicit Table Selection Commands

这些命令用于显式选择特定的内部或外部表，以用于计算衰减。

```txt
- internal_table <table_name> 
```

功能：指定使用具有指定名称的内部表来计算衰减。

```txt
表名构造：<spectrum>_a<atm>_h<Haze>
```

□ <spectrum> 是光谱域名称：

mono_1000nm：单色（激光）1000nm   
mono_1064nm：单色（激光）1064nm   
mono_1550nm：单色（激光）1550nm   
mono_1572nm：单色（激光）1572nm   
mwir：中波红外，3um-5um  
lwir：长波红外，8um-12um  
visual：可见光，380nm-760nm

```txt
<atm> 是 MODTRAN 大气模型:
```

1：热带（北纬 15 度）  
• 2：中纬度夏季（北纬 45 度）  
3：中纬度冬季（北纬 45 度）  
• 4：亚北极夏季（北纬 60 度）  
5：亚北极冬季（北纬 60 度）  
6：1976 年美国标准日

```txt
-haze> 是 MODTRAN 大气模型:
```

1：农村消光，默认能见度 23 公里  
2：农村消光，默认能见度 5 公里  
3：海军海洋消光，基于风速和相对湿度设置能见度  
4：海洋消光，默认能见度 23 公里（LOWTRAN 模型）  
5：城市消光，默认能见度 5 公里  
6：对流层消光，默认能见度 50 公里  
8：雾 1（平流雾）消光，0.2 公里能见度  
9：雾 2（辐射雾）消光，0.5 公里能见度  
10：沙漠消光，基于风速设置能见度

示例：internal_table mono_1000nm_a2_h1 选择单色 1000nm 光谱、中纬度夏季、农村消光、默认能见度 23 公里的表。

external_table <filename>

功 能 ： 指 定 使 用 从 指 定 文 件 加 载 的 表 来 计 算 衰 减 。 该 文 件 通 常 是 使 用spectral_data_conversion 或 optical_table_conversion 命令创建的，但也可以是手动创建的简单表格式文件。

默认：无 - 必须指定 internal_table 或 external_table。

这些命令允许用户根据特定的光谱和大气条件选择适当的衰减表，以便在视觉和红外系统中进行精确的衰减计算。

# 隐式表选择命令 Implicit Table Selection Commands

如果没有通过显式表选择命令选择表，将尝试根据与此实例关联的发射机或接收机的波长和带宽选择表。以下命令也将用于辅助选择：

atmosphere_model <integer>

功能：指定 MODTRAN 大气模型编号。

允许值：请参阅 internal_table 命令的描述。

默认值：2（中纬度夏季）

haze_model <integer>

功能：指定 MODTRAN 雾霾模型编号。

允许值：请参阅 internal_table 命令的描述。

默认值：1（23 公里农村消光）

这些命令帮助在没有显式选择表的情况下，根据环境条件自动选择适当的内部或外部表，以便进行衰减计算。

# 杂项命令 Miscellaneous Commands

adjustment_factor <value>

功能：指定一个乘数应用于返回值。这通常用于考虑到在宽带（如长波红外、中波红外、可见光）上积分的值可能包括许多传感器可能排除的“死区”。因此，有效透射率可能更高。注意：返回值是透射率，因此要增加透射率，请指定大于 1 的因子。

默认值：1.0（无调整）

# 转换命令 Conversion Commands

这些命令用于将其他数据形式转换为可用于此模型的形式。注意，转换命令通常在使用生成的表进行的任何实际模拟运行之前单独运行。

spectral_data_conversion … end_spectral_data_conversion

功能：用于将 MODTRAN 的光谱结果转换为可用于 external_table 的形式或可编译为可执行文件的代码。

spectral_data<filename>：指定要从中创建表的光谱透射率文件的名称。运行时使用“恒定压力高度”几何规范在透射模式下运行 MODTRAN 生成此文件。

默认值：无 - 必须提供。

table_output <filename>：指定将包含转换结果的文件名，以可用作 external_table 命令的参数。

默认值：无 - 必须提供 table_output 或 code_output。

code_output <filename>：指定将包含转换结果的文件名，以便编译为 internal_table 可

用的嵌入模型之一。

默认值：无 - 必须提供 table_output 或 code_output。

maximum_segment_count <integer>：每个高度允许的最大线性段数。

默认值：5

maximum_absolute_error <real_value>：输入透射率与段内建模透射率之间允许的最大绝对误差。

默认值：0.0001

maximum_relative_error <real_value>：输入透射率与段内建模透射率之间允许的最大相对误差。

默认值：0.005

optical_path_conversion … end_optical_path_conversion

功能：用于将 WSF_LASER_WEAPON 和 WSF_CUED_LASER_WEAPON 使用的遗留大气系数表转换为可用于 external_table 命令的形式。

wavelength <Length>：指定要选择的系数表的波长。

默认值：无，必须提供

atmosphere_model <integer>：指定要选择的系数表的 MODTRAN 大气模型编号。

默认值：无，必须提供

haze_model <integer>：指定要选择的系数表的 MODTRAN 雾霾模型编号。

默认值：无，必须提供

table_output <filename>：指定将包含转换结果的文件名，以可用作 external_table 命令的参数。

默认值：无 - 必须提供 table_output 或 code_output。

code_output <filename>：指定将包含转换结果的文件名，以便编译为 internal_table 可用的嵌入模型之一。

默认值：无 - 必须提供 table_output 或 code_output。

# 简单表格式 Simple Table Format

external_table命令接受包含每个高度使用的衰减系数规范的文件，格式如下：

```txt
compact_table altitude <alt_1 length-value> range_limit 10000000.0 meters <alpha_1> 0.0 end_altitude altitude <alt_2 length-value> range_limit 10000000.0 meters <alpha_2> 0.0 end_altitude altitude <alt_n length-value> range_limit 10000000.0 meters <alpha_n> 0.0 end_altitude end_compact_table 
```

注意：高度必须包含单位并单调递增。<alpha>是以 $1 / \mathsf { m }$ 为单位的衰减系数。

# 3.5.5.7.7. 表格衰减模型 WSF_TABULAR_ATTENUATION

```txt
attenuation_model <name-or-type> WSF_TABULAR AttENUATION  
attenuation ...  
adjustment_factor ...  
sort_end_points ...  
two_wayAttenuation ...  
spectral_data_conversion ...  
endAttenuation_model 
```

概述

WSF_TABULAR_ATTENUATION 是一种衰减模型，允许用户使用表格定义衰减。

# 命令说明

attenuation <table-value>

指定定义衰减值的表格。该表格必须至少是三个自变量的函数：

altitude, elevation_angle 和 slant_range

altitude_1, altitude_2 和 ground_range

还可以包括“frequency”作为附加自变量。

默认值：无（必须指定）

adjustment_factor <value>

指定应用于返回值的乘数。通常用于考虑在宽带（例如：可见光）上积分的值可能包括许多传感器可能排除的“死区”，因此有效透射率可能更高。

注意：返回值是透射率，因此要增加透射率，请指定大于 1 的因子。

默认值：1.0（无调整）

sort_end_points <boolean-value>

指定给定交互的端点（源点和目标点）是否可以逻辑互换，以便路径从最高对象到最低对象。这适用于衰减值与方向无关的情况。这允许为空对地目的计算的表格也用于地对空目的。

默认值：false

two_way_attenuation <boolean-value>

指定表格值是否表示双向衰减（发射器到目标再到接收器）。

默认值：false（表格值表示单向衰减）

# 光谱数据转换命令

spectral_data_conversion … end_spectral_data_conversion

此命令用于将由 MODTRAN 等程序生成的光谱数据转换为可用作衰减命令输入的形式。

此命令与使用模型的实际模拟运行分开使用。例如，可以在任务中执行以下输入来首先转换文件：

```batch
attenuation_model CONVERT WSF_TABULAR AttENUATION spectral_data_conversion sensor_to_target_transmittance example_stt.plt output example.txt end_spectral_data_conversion 
```

```txt
end_attenuation_model 
```

转换后的数据将用作传感器中的衰减模型：

```batch
attenuation_model EXAMPLE WSF_TABULAR AttENUATION attenuation file example.txt   
endAttenuation_model 
```

sensor_to_target_transmittance <filename>

指定包含原始光谱传感器到目标透射率的文件名，该透射率是观察者高度、仰角和到目标的斜距的函数。根据当前流程，此文件名的格式为 <filename>_stt.plt。

默认值：无 - 必须提供。

target_to_background_radiance <filename>

指定包含原始光谱目标到背景辐射的文件名，该辐射是观察者高度、仰角和到目标的斜距的函数。根据当前流程，此文件名的格式为 <filename>_tbr.plt。

如果未提供此文件，输出将仅包含每个点的积分透射率。如果提供了文件，则输出将包含某些传感器模型所需的“视线大气透射率”或“对比透射率”。

默认值：无 - 输出包含积分透射率。

spectral_response_curve … end_spectral_response_curve

定义传感器的响应作为波长的函数。曲线定义为一系列点，每个点定义为：

```txt
wavelength response 
```

其中第一个项目是波长（带单位），第二个项目是该波长的响应。响应必须在 [0..1] 范围内。必须至少指定两个点，并且点必须按波长单调递增。

默认值：输入文件中所有波长的均匀响应为 1.0

output <filename>

指定要写入转换结果的文件名。该文件可以用作衰减命令的参数（参见本节开头的示例）。

默认值：无 - 必须提供

# 3.5.5.8. 发射机 transmitter

```txt
transmitter   
... Antenna Commands ...   
alternate_freqency <id> <frequency-value>   
antenna_pattern <pattern-name>   
antenna_pattern_table ... end_antenna_pattern_table   
attenuation_model <derived-name>   
attenuation ... (attenuation is a synonym for attenuation_model)   
aux_data ... end_aux_data   
bandwidth <frequency-value>   
beam_tilt <angle-value>   
check Terrain_masking <boolean-value>   
terrain_masking_mode [ terrain_and_horizon | terrain_only | horizon_only ]   
duty_cycle <real-value> 
```

```shell
earth_radius-multiplier <value>  
effective-earth_radius <length-value>  
frequency <frequency-value>  
wavelength <length-value>  
frequency_channels <lower-frequency-value> <step-frequency-value>  
<upper-frequency-value>  
frequency_list ... end_frequency_list  
internal_loss <db-ratio-value>  
polarization [horizontal | vertical | slant_45 | slant_135 | left_circular | right_circular | default]  
power <power-value>  
powers ... endpowers  
propagation_model <derived-name>  
pulse_compression_ratio <db-ratio-value>  
pulse_repetition_freqency <frequency-value>  
pulse_repetition_interval <time-value>  
pulse_repetition_freqency ... end_pulse_repetition_freqency  
pulse_repetition_interval ... end_pulse_repetition_interval  
pulse_repetition_freqencies ... end_pulse_repetition_freqencies  
pulse_repetition_intervals ... end_pulse_repetition_intervals  
pulse_width <time-value>  
use_peak_power <boolean-value>  
electronic_attack ... end_electronic_attack  
end_transmitter 
```

发射机模块定义了电磁发射机的属性，广泛应用于各种传感器和通信设备。

alternate_frequency <id> <frequency-value>

指定备用频率。对于 WSF_RADAR_SENSOR 类型，可以通过 randomize_radar_frequencies命令在模拟初始化期间随机选择频率。可以输入多个具有连续递增<id>的条目。

□ <id>：用于添加多个备用频率的有序输入 ID，范围为[1,N]。

▫ <frequency-value>：给定<id>的备用频率值。

注意：频率值是必需的，<id>为 0。频率条目必须在所有备用频率条目之前，因为在解析频率值时备用频率列表会被清除。

antenna_pattern <pattern-name>

指定发射机使用的天线增益模式的名称。模式必须使用 antenna_pattern 命令定义。

默认值：如果未指定 antenna_pattern 或 antenna_pattern_table，则假定天线增益为常数1（0 dB）。

antenna_pattern_table … end_antenna_pattern_table

允许定义频率依赖或极化和频率依赖的天线增益模式。每个命名的天线模式必须使用antenna_pattern 命令定义。

频率依赖表格式：

```txt
antenna_pattern_table frequency <frequency-value-1> <pattern-name-1> frequency <frequency-value-2> <pattern-name-2> 
```

```txt
... frequency <frequency-value-n> <pattern-name-n> end ANTenna_pattern_table 
```

极化和频率依赖表格式：

```txt
antenna_pattern_table
polarization default
    frequency <frequency-value-1> <pattern-name-1>
    ...
    polarization <polarization-type>
    frequency <frequency-value-1> <pattern-name-1>
    ...
end ANTenna_pattern_table 
```

规则：

▫ 任何在第一个 polarization 条目之前出现的 frequency 条目假定适用于 default 极化。  
□ 未定义的极化将使用 default 极化的定义。  
□ 必须定义 default 极化。

attenuation_model <derived-name>

指定衰减模型。有关可用衰减模型及其配置的信息，请参见全局命令attenuation_model。

默认值：无（无衰减效果）

aux_data … end_aux_data

定义应用程序特定的“辅助数据”。

默认值：未定义辅助数据。

bandwidth <frequency-value>

指定发射机的频谱带宽。发射信号的频率在： [ frequency - 1/2 bandwidth, frequency + 1/2 bandwidth ]

默认值：0Hz

beam_tilt <angle-value>

仅在定义使用多个波束的系统时使用（例如，在 WSF_RADAR_SENSOR 中使用多个波束）。

指定波束中心在水平面上的仰角。

默认值：如果有隐式关联的接收器（例如在 WSF_RADAR_SENSOR 中），则默认值为关联接收器的 beam_tilt 值。如果没有关联接收器或未在关联接收器中指定 beam_tilt，则假定为 0 度。

check_terrain_masking <boolean-value>

切换地形和地平线视线的计算。可以设置为“off”以减少计算或模拟没有视线限制的传感器和通信设备。

默认值：on

terrain_masking_mode [ terrain_and_horizon | terrain_only | horizon_only ]

设置要执行的遮蔽检查模式或类型。

默认值：terrain_and_horizon

duty_cycle <real-value>

指定脉冲发射机的传输占空比。如果输入，则此值乘以输入的峰值功率，并用作任何未特别调用峰值功率的计算中的平均功率。

默认值：1.0

earth_radius_multiplier <value>

指定用于计算无线电频率信号大气折射效应的地球半径乘数。

默认值：1.33333（4/3），这意味着有效地球半径约为实际地球半径的 4/3.

effective_earth_radius <length-value>

指定有效地球半径的长度值，用于大气折射计算。

默认值：8488942.693 米（基于地球半径 6366707.019 米和默认乘数 4/3）.

frequency <frequency-value>

发射机发射的辐射的中心频率。发射频率范围为：[ frequency - 1/2 bandwidth, frequency$+ 1 / 2$ bandwidth ]

默认值：无。必须指定 frequency、frequency_channels 或 frequency_list 之一。如果指定了多个，则使用最后一个指定的。

wavelength <length-value>

作为输入频率的替代机制。结果频率计算为： frequency $=$ speed-of-light / wavelength

frequency_channels <lower-frequency-value> <step-frequency-value>

<upper-frequency-value>

指定备用频率通道。基于通道限制和步长创建备用频率列表。

默认值：无。必须指定 frequency、frequency_channels 或 frequency_list 之一。如果指定了多个，则使用最后一个指定的。

frequency_list … end_frequency_list

指 定 备 用 频 率 列 表 。 对 于 WSF_RADAR_SENSOR 类 型 ， 可 以 通 过randomize_radar_frequencies 命令在模拟初始化期间随机选择频率。可以输入多个具有连续递增<id>的条目。

```txt
frequency_list frequency_id <id> <frequency-value> ... frequency_id <id> <frequency-value> end_frequency_list 
```

□ <id>：用于添加多个备用频率的有序输入 ID，范围为[1,N]。

□ <frequency-value>：给定<id>的备用频率值。

默认值：无。必须指定 frequency、frequency_channels 或 frequency_list 之一。如果指定了多个，则使用最后一个指定的。

注意：在具有多个波束的 WSF_RADAR_SENSOR 类型中，每个波束必须具有相同数量的frequency_id 输入。

internal_loss <db-ratio-value>

用于模拟发射机和天线之间的各种损耗的单一数值。

默认值：0dB

注意：这是一个“损耗因子”，通常具有正的“dB”值或大于 1 的线性值。

polarization [ horizontal | vertical | slant_45 | slant_135 | left_circular | right_circular | default ]

指定发射信号的极化。这是一个可选条目，可用于模拟极化失配的影响。

默认值：default

power <power-value>