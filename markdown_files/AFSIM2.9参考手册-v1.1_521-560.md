# 3.5.5.10.4.19. 随机脉冲干扰 WSF_RPJ_EFFECT

```txt
effect <effect-name> WSF_RPJ_EFFECT  
electronic_warfare-effect Commands  
WSF_PULSE_EFFECT Commands  
WSF_REPEATER_EFFECT Commands  
WSF_POWER_EFFECT Commands  
WSF_RADIUS_EFFECT Commands  
jamming_pulse_density <value>  
samples_per_detector <value>  
minimum_jammer_to_noise_threshold <db-ratio-value>  
jammer_gain_table  
jammer_to_noise_ratio <ratio>  
pulse_density_to_jammer_gain <ratio> <db-ratio-value> 
```

```txt
... end_jammer_gain_table end-effect 
```

这种基础效应类型可以作为给定技术的众多可用效应之一，包含在 electronic_attack技术块中。下面列出的命令是该效应类型的基本命令，可以在效应块中指定。

命令

coherency_ratio <value>

指定受害者接收器中相干处理的脉冲比例。通过此比例将功率在相干和噪声干扰功率之间进行分配。

默认值：0.0

jamming_pulse_density <value>

指定用于此雷达类型的干扰信号的脉冲密度，范围为[0,1]。

默认值：0.1

samples_per_detection <value>

指定在单次检测尝试中用于目标的脉冲样本数量（例如，雷达使用的快速傅里叶变换、积分箱的数量）。必须大于 1。

默认值：对于 WSF_RADAR_SENSOR 类型为 number_of_pulses_integrated，其他类型为 1

minimum_jammer_to_noise_threshold <db-ratio-value>

指定此效应能够影响此雷达类型接收器的最小干扰与噪声比。

默认值：0.0 dB

jammer_gain_table … end_jammer_gain_table

此块定义了此效应在受害者接收器中作为干扰与噪声比和存在的脉冲密度（即从输入干扰脉冲密度获得）函数的干扰增益。

jammer_to_noise_ratio <db-ratio-value>

指定以下一组 pulse_density_to_jamming_gain 有效的干扰与噪声比。根据需要，可以为多个干扰与信号输入值重复此输入。

默认值：0.0 dB

pulse_density_to_jamming_gain <ratio> <db-ratio-value>

指定在受害者接收器中实现的脉冲密度下的干扰功率增益因子。根据需要，可以为给定的 jammer_to_noise_ratio 重复多个 pulse_density_to_jamming_gain 输入值。脉冲密度输入范围为[0.0,…1.0]。对于在表中两个值之间的脉冲密度，增益查找值将进行插值。表中的脉冲密度 0.0 自动映射到-300.0dB的干扰增益，但可以通过输入覆盖。

默认值：0.1 0.0 dB

system_type_data <system-type-name> … end_system_type_data

这是一个输入块，用于提供特定系统类型（例如，SENSOR-TYPE,JAMMER-TYPE）所需的数据，以实现给定系统类型的技术。可以为未定义的系统类型设置默认数据，使用“default”字符串作为系统类型。

```txt
system_type_data <system-type-name> 
```

```txt
WSF_PULSE_EFFECT Commands 
```

```txt
WSF_POWER_EFFECT Commands 
```

```txt
WSF_REPEATER_EFFECT Commands  
WSF_RADIUS_EFFECT Commands  
jamming_pulse_density <value>  
samples_per_detector <value>  
minimum_jammer_to_noise_threshold <db-ratio-value>  
jammer_gain_table  
jammer_to_noise_ratio <ratio>  
pulse_density_to_jammer_gain <ratio> <db-ratio-value>  
...  
...  
...  
end_jammer_gain_table  
end_system_type_data 
```

```txt
system-type-name> 
```

这是一个字符串输入，表示以下数据适用的系统类型，有效值为[system-type-name |“default”]。默认数据用于未指定的系统类型，如果未定义，则不会对给定的系统类型应用任何效应。

注意：此输入通常由 electronic_attack 定义使用，以指定不同的传感器类型数据。它可能由 electronic_protect 定义使用，以指定干扰器类型数据输入，但通常数据仅在此输入块外输入，并应用于所有干扰器类型的 electronic_protect 效应。

# 3.5.5.10.4.20. 简单假目标干扰模型 WSF_SIMPLE_FT_EFFECT

```c
effect <effect-name> WSF_SIMPLE_FT_EFFECT  
electronic_warfare-effect Commands  
WSF_PULSE_EFFECT Commands  
WSF_REPEATER_EFFECT Commands  
WSF_POWER_EFFECT Commands  
WSF_RADIUS_EFFECT Commands  
apply_electronic_protect_effects <boolean-value>  
combine-multi_beam_counts <boolean-value>  
jamming_pulse_density <value>  
maximum,false_target_capacity <value>  
number_of=false_targets <value>  
percent_of.beamwidth_for_detector <ratio-value>  
update_once_per_frame <boolean-value>  
use_random Calculation_draw <boolean-value>  
end Effect 
```

这种基础效应类型可以作为给定技术的众多可用效应之一，包含在 electronic_attack技术块中。此技术动态计算在当前几何条件下雷达扫描范围内可能创建的虚假目标数量，然后将其与雷达的虚假目标容量进行比较，以确定是否被淹没。如果被淹没，则检测被阻止。如果虚假目标数量是硬性设置的，则使用该数量而不是动态计算的虚假目标数量。根据需要应用基本的电子保护技术。

命令

apply_electronic_protect_effects <boolean-value>

指定是否应将 electronic_protect 效应应用于计算出的虚假目标数量。

默认值：true

combine_multi_beam_counts <boolean-value>

指定具有多个波束的雷达是否应合并其虚假目标计数以进行总比较。一旦虚假目标数量超过 maximum_false_target_capacity，则后续波束将不再计算。

默认值：true

jamming_pulse_density <value>

指定用于此雷达类型的干扰信号的脉冲密度，范围为[0,1]。与 number_of_false_targets互斥。

默认值：0.1

maximum_false_target_capacity <value>

指定此雷达类型在被淹没之前能够处理的最大虚假目标数量。

默认值：1000，除非雷达传感器上存在 false_target_screener，则使用其 track_capacity。

number_of_false_targets <value>

指定将为此雷达类型创建的虚假目标数量。与 jamming_pulse_density 互斥。

默认值：1000

percent_of_beamwidth_for_detection <ratio-value>

指定在此雷达类型中发生检测的雷达波束宽度的百分比，范围为[0,1]。例如，值为 0.5表示需要半个波束宽度的连续脉冲来声明检测，而值为 1.0 表示需要整个波束宽度。

默认值：1.0

update_once_per_frame <boolean-value>

指定雷达传感器模式的虚假目标计数是否应在每帧时间内更新多次。

默认值：false

use_random_calculation_draw <boolean-value>

指定是否使用随机计算抽签来确定检测是否被阻止，依据以下公式：

阻止 $=$ UniformRandomDraw(0.0, 1.0) $>$ TrackCapacity / NumberFalseTargets

默认值：false

system_type_data <system-type-name> … end_system_type_data

这是一个输入块，用于提供特定系统类型（例如，SENSOR-TYPE,JAMMER-TYPE）所需的数据，以实现给定系统类型的技术。可以为未定义的系统类型设置默认数据，使用“default”字符串作为系统类型。

```txt
system_type_data <system-type-name>  
WSF_PULSE_EFFECT Commands  
WSF_POWER_EFFECT Commands  
WSF_REPEATER_EFFECT Commands  
WSF_RADIUS_EFFECT Commands  
apply_electronic_protect_effects <boolean-value>  
combine-multi_beam_counts <boolean-value>  
jamming_pulse_density <value>  
maximumfalse_target_capacity <value>  
number_of,false_targets <value> 
```

```txt
percent_of_beamwidth_for_detector <ratio-value> update_once_per_frame <boolean-value> end_system_type_data 
```

```txt
system-type-name> 
```

这是一个字符串输入，表示以下数据适用的系统类型，有效值为[system-type-name |“default”]。默认数据用于未指定的系统类型，如果未定义，则不会对给定的系统类型应用任何效应。

注意：此输入通常由 electronic_attack 定义使用，以指定不同的传感器类型数据。它可能由 electronic_protect 定义使用，以指定干扰器类型数据输入，但通常数据仅在此输入块外输入，并应用于所有干扰器类型的 electronic_protect 效应。

# 3.5.5.10.4.21. 抑制旁瓣相消模型 WSF_SLC_DEGRADE_EFFECT

```txt
effect <effect-name> wsf_slc_degrade-effect
... base effect commands ...
... wsf_radius-effect commands ...
... wsf_repeater-effect commands ...
... wsf_power-effect commands ...
... wsf_radius-effect commands ...
number_slc_channels_saturated <integer-value>
signal_modulation <modulation-type>
slc_degradation_factor <db-ratio-value>
system_type_data <system-type-name> ... end_system_type_data
end Effect 
```

这种基础效应类型可以作为给定技术的众多可用效应之一，包含在 electronic_attack技术块中。下面列出的命令是该效应类型的基本命令，可以在效应块中指定。

命令

```txt
number_slc_channels_saturated <integer-value>指定此技术将饱和（占用）的旁瓣消除器（SLC）通道数量。
```

默认值：1

```txt
- signal_modulation <modulation-type>指定此技术使用的信号调制类型。
```

默认值：none

```txt
- slc_degradation_factor <db-ratio-value>
  指定应用于由WSF_SLC_EFFECT定义的SLC消除比的降级因子。
```

```txt
- system_type_data <system-type-name> ... end_system_type_data  
这是一个输入块，用于提供特定系统类型（例如，SENSOR-TYPE, JAMMER-TYPE）所需的数据，以实现给定系统类型的技术。可以为未定义的系统类型设置默认数据，使用“default”字符串作为系统类型。
```

```txt
system_type_data <system-type-name> WSF_RADIUS_EFFECT Commands WSF_REPEATER_EFFECT Commands WSF_POWER_EFFECT Commands 
```

```txt
WSF_RADIUS_EFFECT Commands  
number_slc_channels_saturated <integer-value>  
signal_modulation <modulation-type>  
slc_degradation_factor <db-ratio-value>  
end_system_type_data 
```

<system-type-name>

这是一个字符串输入，表示以下数据适用的系统类型，有效值为[system-type-name |“default”]。默认数据用于未指定的系统类型，如果未定义，则不会对给定的系统类型应用任何效应。

注意：此输入通常由 electronic_attack 定义使用，以指定不同的传感器类型数据。它可能由 electronic_protect 定义使用，以指定干扰器类型数据输入，但通常数据仅在此输入块外输入，并应用于所有干扰器类型的 electronic_protect 效应。

# 3.5.5.11.雷达传感器其它命令

# 传感器级别命令 Sensor Level Commands

show_calibration_data

将雷达特性的相关信息写入标准输出。这将包括一平方米的探测范围以及可能需要推导的其他值。

# 模式命令 Mode Commands

transmit_only   
receive_only

表示仅使用发射器或接收器。

注意：对于发射器屏蔽不重要的双基地交互，请将 check_transmitter_masking 设置为“off”或“false”。

compute_measurement_errors [ true | false ]

如果为 true，将使用标准雷达误差模型方程计算测量误差。如果为 false，将使用通用传感器误差模型计算测量误差。

默认值：false

override_measurement_with_truth [ true | false ]

此命令将计算测量误差并在轨迹中报告误差，但将在轨迹中报告真实位置，而不是使用应用了测量误差的位置。这通常用于测试跟踪器。

默认值：false

frequency_select_delay <time-value>

指定在发射机定义的不同频率之间选择时的延迟。

注意：此输入仅对 WSF_AGILITY_EFFECT 频率变化功能有效。

默认值：0.0 秒

maintain_track_measurement_history <boolean-value>

如果为 true，该模式将维护由成功检测产生的测量的轨迹历史。

默认值：false

# 波束命令 Beam Commands

doppler_resolution <speed-value>

定义雷达的目标多普勒速度分辨率（即开合速度）能力。

默认值：0.0

注 意 ： 此 输 入 目 前 仅 用 于 计 算 与 该 传 感 器 相 关 的 距 离 速 率 测 量 误 差 。compute_measurement_errors 必须设置为 true，并且必须指定 reports_range_rate 以启用距离速率误差计算。

adjustment_factor <dbratio-value>

调整波束检测能力的方法。正值增加传感器的检测能力。

默认值：0.0 dB

operating_loss <dbratio-value>

定义波束的操作损耗。

默认值：0.0 dB

注意：损耗应输入为正值。

integration_gain <dbratio-value>

定义使用二进制检测器（detection_threshold）时的积分增益。当使用 Swerling 检测器（swerling_case）或检测概率时不适用。

默认值：0.0 dB

detection_threshold <dbratio-value>

定义接收器检测阈值的替代方法。可以在此输入值以提高输入文件的可读性。

默认值：3.0 dB

swerling_case [ 0 | 1 | 2 | 3 | 4 ]

指示使用 Marcum-Swerling 检测器模型并指定要使用的“案例”。

默认值：默认使用二进制检测器，检测阈值由 detection_threshold 定义。

number_of_pulses_integrated <integer-value>

指定 Marcum-Swerling 检测器集成的脉冲数量。

默认值：1

probability_of_false_alarm <pfa>

指定虚警概率。

默认值：1.0e-6

detector_law [ linear | square | log ]

指定 Marcum-Swerling 检测器的类型。

默认值：linear

no_swerling_case

指定不使用 Marcum-Swerling 检测器。检测将基于 detection_threshold。这是默认配置。

detection_probability

定义检测概率（Pd）与接收信号噪声比的函数（更具体地说，实际上是信号干扰比，包括接收器噪声、干扰和未抑制杂波的影响）。这是使用 Swerling 检测器（swerling_case）或二进制检测器（detection_threshold）的替代方法。表格定义如下：

```perl
detection(probability signal_to_noise <db-ratio-1> pd <pd-value-1> signal_to_noise <db-ratio-2> pd <pd-value-2> ... signal_to_noise <db-ratio-n> pd <pd-value-n> endDetectionprobability 
```

□ <db-ratio-n>：接收信号的信噪比。  
▫ <pd-value-n>：与比率相关的检测概率。

必须至少有两个条目，并且比率必须单调递增。超过表格限制的信号将被夹到适当的端点。中间值将使用“dB”值之间的线性插值确定。

默认值：默认使用二进制检测器，检测阈值由 detection_threshold 定义。

post_lockon_detection_threshold_adjustment <dbratio-value>

定义在传感器达到“锁定”状态后，检测阈值将调整的值。这通常用于跟踪传感器，以指示在达到锁定状态后检测阈值较低。该值通常为负的“dB”值，尽管如果需要，也可以为 0dB或更大。

默认值：0dB

post_lockon_adjustment_delay_time <time-value>

定义从传感器宣布达到“锁定”状态到应用 post_lockon_detection_threshold_adjustment之间必须经过的时间。

默认值：0.0 秒

one_m2_detect_range <length-value>   
range_product <area-value>   
loop_gain <dbratio-value>

指定雷达波束检测能力的替代方法。如果指定，接收器的噪声值将被校准以产生指定的检测范围。

look_down_factor <dbratio-value>

定义波束的俯视损耗。该比率将调整位于波束天线下方目标的接收信号功率。

默认值：1.0

prf_factor <dbratio-value>

定义一个因子，表示使用交错 HPRF 和 MPRF 波形的波束的检测差异。如果目标闭合速度的绝对值小于自船速度，则 prf_factor应用于接收信号功率。

默认值：1.0

clutter_model <derived-name>

指定杂波模型。有关可用杂波效果及如何配置模型的更多信息，请参见 3.5.5.2 杂波模型 clutter_model。

默认值：none（无杂波）

clutter_attenuation_factor <dbratio-value>

指定一个范围为[0..1]的常数值，通过该值将杂波返回乘以以创建“衰减的杂波返回”。如果提供了信号处理器类型 mti_processor且未提供此值，则将计算杂波衰减值。

默认值：1.0 绝对值（即无杂波衰减）

signal_processor <type-name> …commands… end_signal_processor

指定由<type-name>标识的信号处理器，参见 3.5.5.3 雷达信号处理器 Radar SignalProcessors，以下列表中的信号处理器特定于 WSF_RADAR_SENSOR 类型定义。

simple_doppler：模拟具有最小/最大多普勒速度截止的简单多普勒效果。

mti_adjustment：模拟 MTI 调整作为闭合速度或多普勒频率的函数。

mti_processor：模拟双延迟线消除器移动目标指示器。

sensitivity_time_control：模拟灵敏度时间控制（STC）效果，基于 ALARM 的实现。

pulse_doppler：模拟脉冲多普勒（PD）效果，基于 ALARM 的实现。

moving_target_indicator：模拟移动目标指示器（MTI）效果，基于 ALARM 的实现。

moving_target_detector：模拟移动目标检测器（MTD）效果，基于 ALARM 的实现。

error_model_parameters … end_error_model_parameters

参见 3.5.1.7.3 雷达探测错误模型 radar_sensor_errorr

用于由 radar_sensor_error 计算误差的误差模型参数覆盖，以代替使用默认接收器/发射器数据。

azimuth_beamwidth <angle-value>：指定误差模型使用的方位波束宽度。

默认值：接收器方位波束宽度。

elevation_beamwidth <angle-value>：指定误差模型使用的仰角波束宽度。

默认值：接收器仰角波束宽度。

pulse_width <time-value>：指定误差模型使用的脉冲宽度。

默认值：发射器脉冲宽度，经过脉冲压缩比校正。

receiver_bandwidth <frequency-value>：指定误差模型使用的接收器带宽。

默认值：接收器带宽。

doppler_resolution <speed-value>：指定误差模型使用的多普勒分辨率。

默认值：波束多普勒分辨率。

# 干扰检测命令 Jam Strobe Detector

Jam Strobe Detector 是一个用于 WSF_RADAR_SENSOR 模式的功能，允许雷达传感器检测和报告其接收到的干扰信号的方位角和/或仰角。通过指示器或频闪轨迹记录的干扰信号可以与其他雷达的仅角度测量结合，使用 JamStrobeEstimator(JSE) 算法生成传递给跟踪算法的伪测量。由于误差计算的不同，报告信息及误差被指定在通用传感器误差模型之外。

该功能支持高斯分布或均匀分布的误差，可以按照接收器波束宽度的比例来指定误差，并包括干扰感知阈值。

注意：该功能尚未完全实现，需要进一步的使用和测试案例来使其完全符合用户规格。目前，轨迹融合不允许仅方位角的轨迹，这可能是使用该功能的一个不足之处。

gaussian_azimuth_error_sigma [ <angle-value> | <real-value> fraction_of_beamwidth ]和gaussian_elevation_error_sigma [ <angle-value> | <real-value> fraction_of_beamwidth ]：指定方位角和仰角误差的标准差，可以直接指定为角度值或接收器波束宽度的比例。  
uniform_azimuth_error_sigma [ <angle-value> | <real-value> fraction_of_beamwidth ]和uniform_elevation_error_sigma [ <angle-value> | <real-value> fraction_of_beamwidth ]：均匀分布误差的标准差，类似地可以指定为角度值或接收器波束宽度的比例。  
uniform_azimuth_error_bound [ <angle-value> | <real-value> fraction_of_beamwidth ]和 uniform_elevation_error_bound [ <angle-value> | <real-value> fraction_of_beamwidth ]： 均匀分布误差的边界值?，标准差为σ = B。 $\sigma = \frac { \mathsf { B } } { \sqrt { 3 } } \circ$

这些命令决定了在给定传感器的轨迹报告中，JamStrobeDetector 报告的目标信息。

Note If a filter (e.g., WSF_KALMAN_FILTER, WSF_ALPHA_BETA_FILTER) is being used, the reported tracks are marked as being filtered, and reported position information (bearing/elevation) will be the filtered position.

报告选项

reports_bearing：报告从传感器到目标的方位角。这个角度从传感器的北方方向测量，范围在 $[ - \pi , \pi ]$ 。  
reports_elevation：报告从传感器到目标的仰角。  
reports_nothing：取消任何之前的 reports 命令，这在想要重用包含 reports 命令的现有传感器定义但需要更改报告内容时很有用。  
▪ track_quality [0 .. 1]：指定由这个 Jam Strobe Detector 生成的轨迹的“质量”。

默认值为：1.0

使用这些选项，你可以精细控制雷达传感器的干扰信号检测和报告能力。

# 干扰感知命令 Jamming Perception Commands

Jamming Perception Commands 是用于雷达传感器的命令，主要用于检测和管理干扰信号的感知。这些命令通常在波束级别操作，但在 jam_strobe_detector 中使用时除外。

jamming_perception_timeout <time-value>：指定感知到的干扰信号在多长时间后不再被感知，从而将干扰感知状态恢复为“false”。如果在此时间内再次感知到干扰信号，则干扰感知状态将保持或变为“true”。默认值为传感器的 frame_time。

jamming_perception_threshold <ratio-value>   
continuous_jamming_perception_threshold <ratio-value>   
pulsed_jamming_perception_threshold <ratio-value>   
coherent_jamming_perception_threshold <ratio-value>

指 定 操 作 员 感 知 干 扰 信 号 的 最 小 阈 值 。 通 常 与 jamming_perception_timeout 、JammingPerceived 脚本方法和电子保护技术（参见 3.5.5.9.1 电子保护模型 electronic_protect）结合使用。默认值为 380dB。

近目标检测命令 Close Target Detection Commands  
```txt
...   
beam ...   
...   
close_target_detector   
debug acquire_deltas.. end_acquire_deltas   
reacquire_deltas... end_reacquire_deltas   
end_close_target_detector   
...   
end_beam 
```

close_target_detection … end_close_target_detection

近目标检测（CloseTargetDetection，CTD）模型允许检测紧密排列的目标和其他平台类型，并使用其结果进行位置测量和轨迹创建。

这种能力主要用于跟踪雷达。当前的实现利用 acquire_deltas 来初步获取附近的目标，并在所有获取条件都满足的情况下选择其结果测量。

reacquire_deltas 用于防止目标跟踪雷达类型在任何指定条件超出重新获取请求（即跟踪）

目标的限制时重新获取目标。如果不允许重新获取，轨迹将被丢弃，并且需要实施传感器的适当行为来处理这种情况，例如使用状态机或脚本方法监控传感器轨迹丢失。

debug

如果指定，调试消息将输出到标准输出。

acquire_deltas … end_acquire_deltas

定义相对于当前目标提示或请求的方位角、仰角和距离的增量，用于获取目标。

▫ azimuth_delta <angle-value>：指定相对于当前目标提示或请求的方位角增量，考虑其他目标。值必须大于等于 0.0。默认：如果未设置，则不考虑该参数。  
□ elevation_delta <angle-value>：指定相对于当前目标提示或请求的仰角增量，考虑其他目标。值必须大于等于 0.0。默认：如果未设置，则不考虑该参数。  
□ range_delta <length-value>：指定相对于当前目标提示或请求的距离增量，考虑其他目标。值必须大于等于 0.0。默认：如果未设置，则不考虑该参数。

reacquire_deltas … end_reacquire_deltas

定义相对于当前目标提示或请求的方位角、仰角和距离的增量，用于目标不能再被重新获取的情况。

▫ azimuth_delta <angle-value>：指定相对于当前目标提示或请求的方位角增量，目标可能被重新获取。值必须大于等于 0.0。默认：如果未设置，则不考虑该参数。  
□ elevation_delta <angle-value>：指定相对于当前目标提示或请求的仰角增量，目标可能被重新获取。值必须大于等于 0.0。默认：如果未设置，则不考虑该参数。  
▫ range_delta <length-value>：指定相对于当前目标提示或请求的距离增量，目标可能被重新获取。值必须大于等于 0.0。默认：如果未设置，则不考虑该参数。

# 3.5.6. 光谱光学传感器 WSF_SOSM_SENSOR

```txt
sosm-interface show.status <boolean-value> # Cache control commands cache_directory <directory-name> ignore_cache_files <boolean-value> write_cache_files <boolean-value> # Load SOSM definitions and associate with WSF types load_atmosphere <s osm-atmosphere-type> from <file-name> load_sensor <s osm-sensor-type> from <file-name> load_target <s osm-target-type> from <file-name> map SENSOR_type <wsf-sensor-type> <s osm-sensor-type> map_target_type <wsf-platform-type> <s osm-target-type> default Atmosphere <type-name> # Use of fast detection mode 
```

```txt
fastdetecton_mode <boolean-value>
# Debugging commands
debug_level <integer>
spectral_print_format ...
show_riipp_data
end_sosm-interface 
```

```txt
sensor <sensor-type> WSF_SOSM_SENSOR
... Platform Part Commands ...
... Articulated Part Commands ...
sensor Commands ...
mode <mode-name>
    sensor_mode commands ...
    ... Antenna Commands ...
    sosm SENSOR_type <sosm-sensor-type>
    ranging_time ...
    ranging_time_track_quality ...
end_mode
end SENSOR 
```

sosm_interface 中的命令用于控制 WSF 和光谱光学传感模型（SOSM）之间的接口。SOSM是一个相对高保真的模型，适用于在任务级模拟环境中分析红外系统。SOSM 使用传感器、目标和大气的光谱表示，使其能够更真实地模拟传感器和目标之间的相互作用。

传感器、目标和大气的特性保存在特定于 SOSM 的独立文件中。sosm_interface包含命令以将定义加载到 SOSM 中，并控制 WSF 传感器和目标类型到相关 SOSM 类型的映射。有关更多信息，请参见：3.5.6.1SOSM 概述 SOSM Overview。

```txt
sosm_INTERFACE 命令
```

show_status <boolean-value>

指示在加载文件时是否应显示进度消息。

默认值： false

cache_directory <directory-name>

指定缓存二进制文件（由于启用 write_cache_files 命令而生成）要写入的目录名称。

默认值： ./sosm_cache

ignore_cache_files <boolean-value>

指示是否应使用由于 write_cache_files 或 fast_detection_mode 命令创建的二进制缓存文件。如果为 true，则将忽略任何缓存文件，所有数据将从原始文本文件中读取。

默认值： false（如果存在，将使用缓存的二进制文件）

注意： 如果指定了 ignore_cache_files true，则将假定 write_cache_files false，除非随后设置为 true。如果要抑制读取现有缓存文件并创建新文件，必须首先指定 ignore_cache_filestrue，然后是 write_cache_files true。如果模型确定文本文件比缓存的二进制文件更新，它将忽略缓存的二进制文件并使用相应的文本文件。

write_cache_files <boolean-value>

指示是否应将从文本文件读取的表或由于启用 fast_detection_mode 而生成的表写入缓存目录。使用相同数据的后续运行将从缓存目录读取数据，而不是读取原始文本数据或重新生成快速检测模式表。

强烈建议使用缓存文件。 例如，从缓存读取大型大气表比从文本文件读取快约两个数量级。

默认值： true

load_atmosphere <sosm-atmosphere-type> from <file-name>

从指定文件加载 SOSM 大气定义，并将其与由<sosm-atmosphere-type>指定的名称关联。

有 关 如 何 创 建 大 气 定 义 的 说 明 ， 请 参 见 ： 3.5.6.1.1SOSM 大 气 模 型SOSM_atmosphere_model。

标准 WSF 发行版包括使用 MODTRAN 生成的几种大气，波长范围为 6680 cm-1（约 1.5微米）到 240 cm-1（约 41.67 微米），采样间隔为 20 cm-1：

□ sosm/modtran/us_std_day.txt 美国标准 - 白天  
□ sosm/modtran/us_std_night.txt 美国标准 - 夜晚  
□ sosm/modtran/mid_lat_summer_day.txt 中纬度夏季 - 白天  
▫ sosm/modtran/mid_lat_summer_night.txt 中纬度夏季 - 夜晚   
□ sosm/modtran/mid_lat_winter_day.txt 中纬度冬季 - 白天  
□ sosm/modtran/mid_lat_winter_night.txt 中纬度冬季 - 夜晚

所有包含在标准发行版中的大气都是使用以下非默认 MODTRAN 选项生成的：

□ 多重散射（卡片 1，IMULT=1）  
□ 光谱朗伯表面（卡片 1，SURREF $= ^ { \prime }$ 'LAMBER', 'farm'）  
□ CO2 混合比为 365.0 ppmv（卡片 1A， $\mathsf { C O } 2 \mathsf { M } \mathsf { X } = 3 6 5 . 0$ ）  
□ 乡村消光， ${ \mathsf { V } } | { \mathsf { S } } = 2 3 { \mathsf { k m } }$ （卡片 2， $\mathsf { I H A Z E } = 1$ ）

注意： 第一个加载的大气被定义为“默认”大气，除非提供了 default_atmosphere。

load_sensor <sosm-sensor-type> from <file-name>

从指定文件加载 SOSM 传感器定义，并将其与由<sosm-sensor-type>指定的名称关联。有关创建传感器模型定义的说明，请参见：3.5.6.1.2SOSM 传感器模型 SOSM sensor model。

注意： 该命令应为模拟所需的每个定义重复。

load_target <sosm-target-type> from <file-name>

从指定文件加载 SOSM 目标模型定义，并将其与由<sosm-target-type>指定的名称关联。有关创建目标模型定义的说明，请参见：3.5.6.1.3SOSM 目标模型表 SOSM target model table和 3.5.6.1.4SOSM 简单目标模型 SOSM target model simple。

注意： 该命令应为模拟所需的每个定义重复。

映射命令

map_sensor_type <wsf-sensor-type> <sosm-sensor-type>

指示当 WSF 想要创建类型为<wsf-sensor-type>的 WSF_SOSM_SENSOR 实例时，应使用的SOSM 传感器类型<sosm-sensor-type>。

创建 WSF_SOSM_SENSOR 实例时，WSF 必须确定要使用的相应 SOSM 传感器定义。具体

步骤如下：

如果提供了，在传感器模式定义中使用 sosm_sensor_type 的值。

对于传感器层次结构中的每个级别：

□ 检查 map_sensor_type 列表中是否有条目，其中<sensor-type>:<sensor-mode>与条目中的<wsf-sensor-type>值匹配。  
检 查 map_sensor_type 列 表 中 是 否 有 条 目 ， 其 中 <sensor-type> 与 条 目 中 的<wsf-sensor-type>值匹配。  
检查 load_sensor 列表中是否有条目，其中<sensor-type:sensor-mode>与条目中的<sosm-sensor-type>值匹配。  
检 查 load_sensor 列 表 中 是 否 有 条 目 ， 其 中 <sensor-type> 与 条 目 中 的<sosm-sensor-type>值匹配。

注意： 除了非常简单的测试案例，建议用户始终包括如下默认映射，以便每个 WSFWSF_SOSM_SENSOR 都有相应的 SOSM 传感器类型：

map_target_type <wsf-platform-type> <sosm-target-type>

指示当 WSF 想要对类型为<wsf-platform-type>的 WSF 平台进行检测尝试时，应使用的SOSM 目标类型<sosm-target-type>。

当 WSF 要对目标进行检测尝试时，必须确定要使用的 SOSM 目标类型。对于 WSF 目标平台的继承层次结构中的每个级别，平台类型的使用如下：

检 查 map_target_type 列 表 中 是 否 有 条 目 ， 其 中 <platform-type> 与 条 目 中 的<wsf-target-type>值匹配。

检查 load_target 列表中是否有条目，其中<platform-type>与条目中的<sosm-target-type>值匹配。

注意： 除了非常简单的测试案例，建议用户始终包括如下默认映射，以便每个 WSF 平台类型都有相应的 SOSM 目标类型：

default_atmosphere <sosm-type-name>

指定当 SOSM 传感器定义未明确引用特定大气类型时要使用的 SOSM 大气类型。

默认值： 第一个 load_atmosphere 命令中的<sosm-type-name>。

fast_detection_mode <boolean-value>

指示是否应使用“fast_detection_mode”。“fast_detection_mode”是一种特殊的操作模式，用于在牺牲少量保真度的情况下减少计算开销。通常在运行实时时使用此模式。

当“fast_detection_mode”未激活时，检测模型必须计算并累加传感器光谱响应内每个波数箱的效果。根据传感器的不同，这可能是 10 到 100 个箱。当启用“fast_detection_mode”时，检测模型将预先计算传感器与大气和传感器与目标之间的光谱交互，然后在检测机会期间使用这些数据以消除对波数箱的迭代。

如果 write_cache_files 为 true，预计算的表将写入缓存目录，可以在将来的运行中重用。

默认值： false

debug_level <integer>

指定要打印的调试信息级别。

debug_level $= 0$ ; 不会生成调试信息。

debug_level $= 1$ ; 显示集成信息。

debug_level $> 1$ ; 显示集成和光谱信息。

spectral_print_format [ wavenumber | wavelength]

指定当 debug_level 大于 1 时光谱数据的输出格式。

默认值： wavenumber

show_iripp_data

如果指定，将以类似于 IRIPP“spec”数据的格式生成光谱检测数据。

sosm_sensor_type <sosm-sensor-type>

一个可选命令，指定要使用的 SOSM 传感器类型。有关如何使用此命令的信息，请参见map_sensor_type。

默认值： 传感器的类型名称。

ranging_time <time-value>

在指定时间过去后，为该传感器生成的任何轨迹添加范围信息。这基本上模拟了系统在足够长的时间后可以进行三角测量并获得范围。

ranging_time_track_quality <quality-value>

如果使用测距时间生成具有范围信息的轨迹，此参数控制范围有效后轨迹的质量。quality-value 必须是非负的。

示例：

```txt
sosm-interface load_atmosphere_type DEFAULT from us_std_day.txt load_sensor_type IRST from demo_irst.txt load_target_type TARGET from demo_target.txt   
end_sosm-interface   
platform_type TARGET WSFPLATFORM # Platforms of this type will use the SOSM target definition loaded from #demo_target.txt (a result of the \*\*load_target_type TARGET from demo_target.txt\*\# command in the \*\*sosm_interface\*\* block defined above). end-platform_type   
sensor IRST WSF_SOSM_SENSOR # This sensor will use the SOSM sensor definition loaded from demo_irst.txt # (a result of the \*\*load sensor_type IRST from demo_irst.txt\*\* command in #the \*\*sosm_interface\*\* block defined above. ...   
end SENSOR   
platform_type SENSOR WSFPLATFORM .. sensor irst IRST on end SENSOR   
end-platform_type 
```

# 3.5.6.1. SOSM 概述 SOSM Overview

光谱光学传感模型（Spectral Optical Sensing Model，SOSM）是一个高保真的红外检测模型，适用于建设性和实时任务模拟环境。目标和大气模型通常由使用离线工具（如 MODTRAN

和 IRIMAGE）生成的表格表示。

使用该模型通常涉及以下步骤：

▪ 创建大气模型（参见：3.5.6.1.1SOSM 大气模型 SOSM_atmosphere_model）  
创建传感器模型（参见：3.5.6.1.2SOSM 传感器模型 SOSM sensor model）  
创 建 目 标 模 型 （ 参 见 ： 3.5.6.1.3SOSM 目 标 模 型 表 SOSM target model table 和3.5.6.1.4SOSM 简单目标模型 SOSM target model simple）  
将模型加载到模拟中并控制操作（参见：3.5.6 光谱光学传感器 WSF_SOSM_SENSOR）

# 光谱表示

该模型使用大气、传感器和目标的离散光谱表示。每个组件都有三个值来定义光谱的限制和分辨率：

▫ O - 起点，定义光谱中第一个波数（cm-1）。  
□ R- 分辨率，定义光谱中采样点之间的波数数量。  
▫ N- 光谱中的采样数量。

因此，组件的光谱范围为：

$$
O, O + (N - 1) \times R
$$

模型对交互的组件施加以下限制：

▫ 所有组件必须具有相同的分辨率（R）。  
□ 在组件相交的地方，它们的采样点必须在相同的波数上。确保这一点的最佳方法是创建起点（O）可以被分辨率（R）整除的模型。

对于大多数应用，使用 $2 0 \ c m { - 1 }$ 的分辨率。标准 WSF 发行版中提供的大气是使用这种分辨率生成的，传感器模型的默认分辨率是 $2 0 \thinspace { \mathsf { c m } } { - 1 }$ ，IRIMAGE 到 SOSM 的转换工具默认生成分辨率为 $2 0 \mathsf { c m } { \cdot } 1$ 的输出。

通常，大气模型是以足够的光谱范围生成的，以覆盖可能与模拟一起使用的任何传感器或目标。目标模型通常仅为感兴趣的光谱窗口创建。

# 3.5.6.1.1. SOSM 大气模型 SOSM_atmosphere_model

创建 SOSM 大气定义包括以下三个步骤：

获取原始光谱大气数据：通常通过执行 MODTRAN 来完成（参见执行 MODTRAN）。  
将第一步的原始光谱大气数据转换为 SOSM 可读取的格式（参见转换 MODTRAN 输出）。  
创建引用第二步中创建的文件的 SOSM 大气模型文件（参见创建大气定义文件）。

WSF 发行版附带了一对 Perl 脚本，帮助使用 MODTRAN 准备模型所需的大气表。这些脚本位于 sosm/modtran 目录中，操作如下：

# 执行 MODTRAN

标准 WSF 发行版中包含一个 Perl 脚本 modtran_execute.pl，位于 sosm/modtran 目录中。此脚本有助于使用 MODTRAN 在所需的高度、仰角和范围值上创建原始光谱大气数据。执行脚本的命令如下：

```txt
<path-to-wsf>/sosm/modtran/modtran_execute.pl <basename> 
```

文件 <basename>.def 指定观察者的高度、视线仰角和范围值以及 MODTRAN 输入卡片。准备 .def 文件需要一些 MODTRAN 的知识。sosm/modtran 目录中有几个 .def 文件的示例。此脚本的输出文件包括：

<basename>_bgr.plt - 背景辐射   
<basename>_bgt.plt - 背景透射率（当前未使用）  
<basename>_fgr.plt - 前景辐射  
<basename>_fgt.plt - 前景透射率

注意： 执行此过程可能需要几个小时。

创建 MODTRAN 输入时应注意以下几点：

卡片 4，FLAGS(1:1) 应为空或‘W’（波数输入）  
卡片 4，XFLAG 必须设置为‘W’（波数输出）。  
▪ 卡片 4，DV 应设置为 20（cm-1），除非您也准备更新传感器和目标模型。  
卡片 4，V1 和 V2 应为 DV 的倍数。  
输出文件的大小将与光谱样本的数量成正比，即： $\left( \left( \mathsf { V } 2 - \mathsf { V } 1 \right) / \mathsf { D } \mathsf { V } \right) + 1$ 。

转换 MODTRAN 输出

一旦运行 MODTRAN 创建了必要的文件，这些文件必须转换为 SOSM 可用的格式。这可以通过使用标准 WSF 发行版中提供的 Perl 脚本 modtran_convert.pl 来完成，该脚本位于 sosm/modtran 目录中。执行脚本的命令如下：

```txt
modtran.convert.pl <pathname> 
```

该脚本将前一步生成的文件转换为 SOSM 所需的表：

<basename>.bgr   
<basename>.bgt（当前未使用）  
<basename>.fgr   
<basename>.fgt

创建大气定义文件

在运行前面的步骤后，应创建文件 <basename>.txt，其内容如下：

```txt
atmosphere_model table background_radiance <basename>.bgr foreground_radiance <basename>.fgr foreground_transmittance <basename>.fgt end_atmosphere 
```

示例

假设您希望创建一个基于标准 WSF 发行版中提供的美国标准白天大气的新大气类型。

复制 sosm/modtran/us_std_day.def 到 us_std_day_mod.def 并根据需要进行编辑。然后执行MODTRAN：

```txt
<path-to-wsf>/sosm/modtran/modtran_execute.pl us_std_day_mod
```

转换文件：

```txt
<path-to-wsf>/sosm/modtran/modtranConvert.pl us_std_day_mod
```

创建文件 us_std_day_mod.txt，内容如下：

```txt
atmosphere_model table background_radiance us_std_day_mod.bgr foreground_radiance us_std_day_mod.fgr foreground_transmittanceus_std_day_mod.fgt   
end_atmosphere 
```

要在模拟中使用新模型，在所有其他 sosm_interface 命令之后，将以下命令添加到模拟输入流中：

```txt
sospm-interface  
sospm-interface.load_atmosphere US_STD_DAY_MOD from us_std_day_mod.txt  
sospm-interface.default Atmosphere US_STD_DAY_MOD  
end_sospm-interface 
```

# 3.5.6.1.2. SOSM 传感器模型 SOSM sensor model

sensor_model default   
responselimits $<  <$ lower-wavelength $>$ <upper-wavelength>   
responsecurve wavelength $\langle$ wavelength-value $\rangle$ <response> end_responsecurve   
noise_equivalent_irradiance $\langle$ power/area-value $\rangle$ detection_threshold $\langle$ real-value $\rangle$ detection_threshold_above Horizon $\langle$ real-value $\rangle$ detection_thresholdbelow horizon $\langle$ real-value $\rangle$ installation_adjustment_table $\langle$ file-name $\rangle$ atmosphere <atmosphere-type> resolution <wavenumber-increment>   
end_sensor_model

创建传感器定义

要为光谱光学传感模型（SOSM）创建传感器定义，每个传感器定义必须包含在其自己的文件中。通过使用 sosm_interface load_sensor 命令，可以将传感器定义提供给模拟。

命令说明

response_limits <lower-wavelength> <upper-wavelength>

定义传感器可以检测信号的区域。

默认值： 无 - 必须提供。

示例：

```txt
responseLimits3um5um 
```

response_curve … end_response_curve

定义传感器作为波长函数的响应曲线。传感器模型将使用此曲线来确定波数箱的响应。默认值： 均匀响应为 1.0

示例：

```txt
response_curve wavelength 3.0 0.8 wavelength 4.0 1.0 wavelength 5.0 0.9 end_responsecurve 
```

noise_equivalent_irradiance <power/area-value>

定义传感器的噪声等效辐照度。

默认值： 无 - 必须提供。

detection_threshold <real-value>

定义传感器的检测阈值。

默认值： 无 - 必须提供此命令或下面定义的 detection_threshold_above/below_horizon命令之一。

detection_threshold_above_horizon <real-value>   
detection_threshold_below_horizon <real-value>

定义传感器在地平线上方或下方的检测阈值。

默认值： 无 - 必须提供此命令或上面定义的 detection_threshold 命令之一。

installation_adjustment_table <file-name>

指定包含一个表的文件名，该表定义了一个函数，其自变量是目标相对于传感平台的方位角和仰角，因变量是用于缩放目标辐照度的 0 到 1 之间的因子。通常用于考虑结构遮挡或可变窗口透射率。

默认值： 无安装调整。

atmosphere <atmosphere-type>

指定传感器使用的大气类型。

默认值： DEFAULT

resolution <wavenumber-value>

定义传感器模型的分辨率。

默认值： 20 cm-1

示例：

```txt
resolution 20 cm-1 
```

# 3.5.6.1.3. SOSM 目标模型表 SOSM target model table

创建目标模型

创建目标模型是一个三步过程：

▫ 获取原始光谱红外特征数据：通常通过使用红外预测模型如 IRIMAGE 来完成（参见执行 IRIMAGE）。  
□ 将第一步创建的原始光谱红外特征数据转换为 SOSM 可读取的格式（参见转换IRIMAGE ‘kio3’ 文件）。  
□ 创建 SOSM 目标定义文件，指定在模拟中如何使用第二步创建的特征文件（参见创建目标定义文件）。

标准 WSF 发行版附带了一对 Perl 脚本，帮助使用 IRIMAGE 完成前两步。

执行 IRIMAGE

IRIMAGE 通常由红外特征分析师运行。这个过程可能需要很长时间（根据所需案例的数量，可能需要几天到几周）。如果您需要自己完成此步骤，请继续阅读。

标准 WSF 发行版中包含一个 Perl 脚本 execute_irimage.pl，位于 sosm/irimage 目录中。此脚本有助于在一系列条件下执行 IRIMAGE。执行脚本的命令如下：

```txt
<path-to-wsf>/sosm/irimage/execute_irimage.pl <basename> 
```

其中 <basename> 是目标类型的基本名称，可能包括马赫数。例如，su-35_m12 可能用于马赫数为 1.2 的 SU-35。

此脚本需要两个文件：

□ <basename>.def：包含定义马赫数、高度和波段的命令，用于生成数据。  
<basename>.iri：包含运行指定马赫数所需的 IRIMAGE 输入模板。

脚本然后为给定的马赫数的每个高度和波段调用 IRIMAGE，并为每种情况生成一个 .kio3 文件。

在 sosm/irimage 目录中提供了文件 su-35_m12.def 和 su-35_m12.iri 作为示例。

转换 IRIMAGE ‘kio3’ 文件

一旦运行 IRIMAGE 创建了必要的 .kio3 文件，这些文件必须转换为 SOSM 可用的格式。这可以通过使用每个 WSF 发行版中提供的 kio3_to_sosm.pl 脚本来完成，该脚本位于sosm/irimage 目录中。

首先需要在包含 .kio3 文件的目录中创建一个名为 kio3_to_sosm.txt 的文件。每个

WSF 发行版中都提供了此文件的模板，位于 sosm/irimage 目录中。复制文件后，编辑副本并根据文件末尾的注释更新信息。在大多数情况下，只需在第三行提供安全分类信息。完成后，执行以下命令：

```txt
<path-to-wsf>/sosm/irimage/kio3_to_sosm.pl *.kio3 
```

这将处理每个形式为 <basename>.kio3 的文件，并生成四个文件：

□ <basename>.bda - 机体的投影面积  
□ <basename>.bdi - 机体的辐射强度  
□ <basename>.pla - 尾流的投影面积  
▫ <basename>.pli - 尾流的辐射强度

这些文件应复制到将创建 SOSM 目标定义的目录中。

# 创建目标定义文件

目标定义文件定义在何种模拟条件下应使用哪些特征文件。以下是命令的说明：

```perl
target_model table
state <state-name-1>
# ---- State selection control
altitude_range <lower-length-value> <upper-length-value>
mach_range <lower-mach> <upper-mach>
speed_range <lower-speed-value> <upper-speed-value>
throttle_range <lower-value> <upper-value>
# ---- Band Definitions
band <band-name-1>
# ---- Body and plume definition using implied file extensions
body_and_plume <file-base> # reads .bda, .bdi, .pla and .pli
body <file-base> # reads .bda and .bdi
plume <file-base> # reads .pla and .pli
# ---- Body and plume definition using explicit files
body_area <file-name>
body_intensity <file-name>
plume_area <file-name>
plume_intensity <file-name>
end_band 
```

```txt
band <band-name-n> ... band-definition ... end_band end_state state <state-name-n> ... state-definition ... end_state end_target_model 
```

# 目标定义命令

target_model table … end_target_model

引入一个使用表格的目标模型定义。table 是必需的。

state <state-name> … end_state

一个状态标识了一组目标条件，与之相关的特征适用。altitude_range、mach_range、speed_range 和 throttle_range 定义了状态适用的目标条件。包含的波段块定义了相关的特征文件。

<state-name> 是状态的用户定义名称。它的唯一作用是唯一标识目标定义中的状态。

注意： 每个目标定义必须至少有一个状态。状态定义的顺序很重要。对于每次检测机会，目标条件用于选择适当的状态。按定义顺序搜索状态列表，使用第一个匹配目标条件的状态。如果没有状态匹配当前目标条件，则使用最后定义的状态。

altitude_range <lower-length-value> <upper-length-value>

定义适用状态的高度范围。

默认值： 无限制 - 高度不是标准。

mach_range <lower-mach> <upper-mach>   
speed_range <lower-speed-value> <upper-speed-value>

定义适用状态的速度范围。范围可以用马赫数或绝对速度来定义。

throttle_range <lower-value> <upper-value>

定义适用状态的油门范围。

band <band-name> … end_band

每个状态必须有一个或多个波段块，定义适用于特定波段的特征文件。<band-name> 是标识波段的用户定义字符串。实际适用的波长范围由文件内容决定。

必须指定机体面积/强度。如果没有尾流，则不需要尾流面积/强度。

可以通过以下命令加载要使用的特征文件：

□ body_and_plume <base-name>读取机体和尾流的特征文件（<base-name>.bda、<base-name>.bdi、<base-name>.pla和 <base-name>.pli）。  
□ body <base-name>仅读取机体的特征文件（<base-name>.bda 和 <base-name>.bdi）。  
plume <base-name>仅读取尾流的特征文件（<base-name>.pla 和 <base-name>.pli）。  
□ body_area <file-name>

▫ body_intensity <file-name>   
▫ plume_area <file-name>   
▫ plume_intensity <file-name>

不使用假定后缀加载特征文件。

# 示例

F-XX 战斗机目标定义

假设我们正在为一个新的战斗机 F-XX 创建定义，并且已经为以下条件执行了前两个步骤：

两个马赫数：0.8 和 1.2  
三个高度：30000 英尺、35000 英尺和 40000 英尺  
两个传感器波段：中波红外（MWIR，3-5 微米）和长波红外（LWIR，8-12 微米）

这将导致生成 12 组文件，假设命名如下：

```c
f-xx_30k_m08_lwir.*  
f-xx_30k_m08_mwir.*  
f-xx_30k_m12_lwir.*  
f-xx_30k_m12_mwir.*  
f-xx_35k_m08_lwir.*  
f-xx_35k_m08_mwir.*  
f-xx_35k_m12_lwir.*  
f-xx_35k_m12_mwir.*  
f-xx_40k_m08_lwir.*  
f-xx_40k_m08_mwir.*  
f-xx_40k_m12_lwir.*  
f-xx_40k_m12_mwir.* 
```

假设已创建目录 f-xx，目标定义文件 f-xx.txt 将如下所示：

```txt
target_model table  
state 30k_m08  
altitude_range 0 ft 32500 ft  
mach_range 0.0 1.0  
band lwir body_and_plume f-xx_30k_m08_lwir end_band  
band mwir body_and_plume f-xx_30k_m08_mwir end_band  
end_state  
state 30k_m12  
altitude_range 0 ft 32500 ft  
mach_range 1.0 10.0  
band lwir body_and_plume f-xx_30k_m12_lwir end_band  
band mwir body_and_plume f-xx_30k_m12_mwir end_band  
end_state 
```

```txt
state 35k_m08 altitude_range 32500 ft 37500 ft mach_range 0.0 1.0 band lwir body_and_plume f-xx_35k_m08lwir end_band band mwir body_and_plume f-xx_35k_m08_mwir end_band end_state   
state 35k_m12 altitude_range 32500 ft 37500 ft mach_range 1.0 10.0 band lwir body_and_plume f-xx_35k_m12lwir end_band band mwir body_and_plume f-xx_35k_m12_mwir end_band end_state   
state 40k_m08 altitude_range 37500 ft 42500 ft mach_range 0.0 1.0 band lwir body_and_plume f-xx_40k_m08lwir end_band band mwir body_and_plume f-xx_40k_m08_mwir end_band end_state   
state 40k_m12 altitude_range 37500 ft 42500 ft mach_range 1.0 10.0 band lwir body_and_plume f-xx_40k_m12lwir end_band band mwir body_and_plume f-xx_40k_m12_mwir end_band end_state   
end_target_model 
```

# 3.5.6.1.4. SOSM 简单目标模型 SOSM target model simple

SOSM 的“简单”目标模型提供了一种方法，可以轻松创建适用于不需要高度细节的应用的目标模型。这种模型适合在需要快速设置和较低复杂度的情况下使用。

特点

简化设计：简单目标模型不需要详细的光谱数据或复杂的状态定义，适合快速模拟和测试。

易于实现：通过减少对详细输入数据的需求，用户可以更快地创建和调整目标模型。

适用场景：适用于需要快速响应或资源有限的模拟环境。

使用场景

简单目标模型特别适合以下情况：

初步概念验证：在早期阶段进行概念验证时，简单模型可以帮助快速评估系统性能。

资源受限的模拟：当计算资源有限或时间紧迫时，简单模型提供了一种有效的替代方案。

教育和培训：在教学或培训环境中，简单模型可以帮助学员快速理解和应用基本概念。

通过使用 SOSM 的简单目标模型，用户可以在不牺牲基本功能的情况下，简化目标模型的创建和管理过程。这种方法特别适合需要快速迭代和调整的应用场景。

```txt
target_model simple state <state-name-1> # ---- State selection control altitude_range <lower-length-value><upper-length-value> mach_range <lower-mach><upper-mach> speed_range <lower-speed-value><upper-speed-value> throttle_range <lower-value><upper-value> # ---- Used to specify nominal conditions for 'fast_detection_mode'. sample_altitude <length-value> sample_speed <speed-value> sample_mach <mach-value> sample_throttle [0..1] # ---- Cold part definition cold_part_area [<file-name>|constant<area-value>] # Parameters to determine temperature for the blackbody model using adiabatic wall assumption recovery_factor (0..1] # default 0.85 gamma <real-value> # default 1.4 # Use a specific temperature for the blackbody model. cold_part_temperature <temperature-value> # Use a specific radiant intensity (no blackbody model). cold_part_radiant_intensity <power/solid-angle-value> # ---- Hot part definition (optional) hot_part_area [<file-name>| constant<area-value>] hot_part_area_fraction <file-name> # Use a specific temperature for the blackbody model. hot_part_temperature <temperature-value> 
```

```txt
# Use a specific radiant intensity (no blackbody model). hot_part_radiant_intensity <power/solid-angle-value>   
# ---- Plume definition (optional)   
plume_area [<file-name> | constant <area-value>]   
# Use a specific temperature for the blackbody model. plume_temperature <temperature-value>   
# Use a specific radiant intensity (no blackbody model). plume_radiant_intensity <power/solid-angle-value>   
end_state   
state <state-name-n> ... state-definition ... end_state   
end_target_model 
```

target_model simple … end_target_model

引入一个使用简单目标模型的目标模型定义。simple 是必需的。

state <state-name> … end_state

一个状态标识了一组目标条件，与之相关的特征适用。altitude_range、mach_range、speed_range 和 throttle_range 定义了状态适用的目标条件。包含的波段块定义了相关的特征文件。

<state-name> 是状态的用户定义名称。它的唯一作用是唯一标识目标定义中的状态。

注意： 每个目标定义必须至少有一个状态。状态定义的顺序很重要。对于每次检测机会，目标条件用于选择适当的状态。按定义顺序搜索状态列表，使用第一个匹配目标条件的状态。如果没有状态匹配当前目标条件，则使用最后定义的状态。

altitude_range <lower-length-value> <upper-length-value>

定义适用状态的高度范围。

默认值： 无限制 - 高度不是标准。

mach_range <lower-mach> <upper-mach>   
speed_range <lower-speed-value> <upper-speed-value>

定义适用状态的速度范围。范围可以用马赫数或绝对速度来定义。

throttle_range <lower-value> <upper-value>

定义适用状态的油门范围。

通过这些命令，您可以为简单目标模型定义不同的状态和条件，以便在 SOSM 中进行模拟。这种方法适合不需要高度细节的应用场景，提供了一种快速设置和调整目标模型的方式。

# 3.5.7. 声学传感器 WSF_ACOUSTIC_SENSOR

```txt
sensor <name> WSF_ACOUSTIC_SENSOR 
```

```txt
... Platform Part Commands ...  
... sensor Commands ...  
mode <name>  
    ... Antenna Commands ...  
    ... receiver ... endreceiver  
    ... WSF_ACOUSTIC_SENSOR Mode Commands ...  
end_mode  
end_sensor 
```

WSF_ACOUSTIC_SENSOR 实现了一个简单的声学传感器模型。这个模型是对人类听觉的简单表示，使用 1/3 倍频程的光谱声源数据构建。多个来源的数据被用于创建这个模型。

声传播、大气衰减和地面反射的建模依据是工程科学数据单元（Engineering SciencesDataUnit）#78002，“均匀大气中声衰减的评估”和#94035，“测量噪声频谱的地面反射效应校正”。

该模型定义了几种背景噪声水平，这些数据摘自“户外环境声学背景噪声综述”，CharlesP. Wright，波音文件#D6-38671，1991 年 5 月 18 日。背景噪声水平的频率为 1/3 倍频程。

人类听觉阈值和 1/3 倍频程滤波数据分别定义在“声学 - 校准听力计设备的参考零点 -第 7 部分：自由场和漫射场听音条件下的听觉阈值”，ISO389-7:2005 和“技术备忘录 3-85：陆军物资的建议听觉不可检测性限值”，Georges R. Garinther, Joel T. Kalb 和 David C. Hodge，1995 年 3 月。

Background Noise Levels   
![](images/a00c2972c774acb3b5c59dc71a9ef5fa0793b1aa53ce407a422a399847993942.jpg)  
注意： 空军发布了他们接受的噪声模型的数据，可以从以下网址获取：http://www.afcee.brooks.af.mil/ec/noise/noisemodels/noisemodels.asp

# 模式命令

detection_threshold <value>

定义相对于人类听觉阈值的声学检测阈值。

默认值： 0.0

acoustic_type [ human ]

定义声学传感器的类型。

默认值： human

background_noise [ jungle_day | jungle_night | industrial | rural | residential ] 定义声学背景的类型。

默认值： residential

# 1/3 倍频程

1/3 倍频程是一种将可听频谱分割为更小段的滤波方法，常用于声学应用的建模和分析。这种方法通过一系列带通滤波器计算每个 1/3 倍频程带的幅度。在声学测量系统中，1/3 倍频程提供了一种灵活的方式来表示模拟结果，这对于声学应用的建模至关重要。

# 3.5.8. 激光光束传感器 WSF_BEAM_DIRECTOR

```txt
sensor<name>WSF_BEAM_DIRECTORY   
... Platform Part Commands ...   
... sensor Commands ..   
mode<name> angular_resolution ... perfect_corrlation ... type ... minPixels_for_cue ...   
end_mode   
end SENSOR 
```

WSF_BEAM_DIRECTOR 是一个用于高能激光（HEL）的光束导向器（目标跟踪器）的传感器。该传感器专为与 WSF_CUED_LASER_WEAPON 配合使用而设计。

模式

该传感器有三种模式：扫描、锁定成像和提示成像。

扫描模式：激光传感器被提示到一个位置或轨迹，并使用此位置作为其视场的中心，扫描其扫描视场内的目标。  
□ 锁定模式：如果检测到目标，传感器将“锁定”该目标并开始成像序列。  
提示模式：一旦获取图像，如果图像达到给定的临界大小（min_pixels_for_cue），传感器将“提示成像”，模拟锁定图像的子部分，此时可以发射共指的 HEL。

模式转换消息

```txt
LOCKED->CUED: CUED_TO_IMAGE  
CUED->LOCKED: LOST_IMAGE_CUE  
LOCKED->SCANNING: BREAKLOCK 
```

当 WSF_CUED_LASER_WEAPON 接收到 CUED_TO_IMAGE 消息时，高能激光开始发射，这在模拟中由 DIRECTED_ENERGY_WEAPON_BEGIN_SHOT 事件指示。如果在激光发射时接收到 LOST_IMAGE_CUE，则高能激光发射中止，并发出 DIRECTED_ENERGY_WEAPON_END_SHOT事件。

模式命令

angular_resolution <angle-value>

指定传感器的角分辨率。

默认值： 3.0E-5 弧度

perfect_correlation <boolean-value>

指定传感器在从初始提示进行跟踪时是否完美相关。

默认值： false（它将选择视场中心最近的对象进行跟踪。）

type scanning | locked | cued

确定模式的类型。使用类型输入简化了将光束导向器建模为一组越来越精细的跟踪模式的任务。通常指定一个扫描模式，一个或多个锁定模式，最后是一个提示模式。一旦进入提示模式，消息将发送到相关的 WSF_CUED_LASER_WEAPON，并开始 HEL 激光发射。

默认值： cued

min_pixels_for_cue <integer-value>

指定成功过渡到提示模式所需的最小像素数。

默认值： 0

通过这些命令，您可以配置 WSF_BEAM_DIRECTOR 的不同模式和参数，以便在高能激光应用中进行有效的目标跟踪和锁定。

# 3.5.9. 光学红外成像传感器 WSF_EOIR_SENSOR

```c
sensorWSF_EOIR_SENSOR ... Articulated Part Commands ... ... sensor Commands .. // Miscellaneous Commands call_sensor_track_observers ... mode Antenna Commands ... ... Receiver Commands ... ... Mode Commands ... end_mode end SENSOR 
```

WSF_EOIR_SENSOR 实现了一个简单的光学或红外成像传感器。该传感器生成一个包含在 WSF_IMAGE_MESSAGE（WsfImageMessage）中的伪图像（类型为 WsfImage）。通过将传感器链接到 WSF_IMAGE_PROCESSOR，可以模拟图像分析过程并创建跟踪。

# 杂项命令

call_sensor_track_observers <boolean-value>

指定是否调用“传感器跟踪观察者”。如果为 true，将调用传感器跟踪观察者事件，这使得可视化工具能够在图像形成过程中显示检测线。然而，这些额外的事件可能会对某些未修改以忽略这些事件的观察者造成问题，因此默认值为 false。

默认值： false

模式命令

angular_resolution <angle-value>

指定每个像素所覆盖的角度。

注意： 必须提供 angular_resolution 或 pixel_count 之一。

pixel_count <horizontal-count> <vertical-count>

指定传感器生成的图像的宽度和高度（以像素为单位）。如果指定此命令，则忽略angular_resolution。相反，角分辨率通过（方位视场）/（水平像素数）和（仰角视场）/（垂直像素数）计算。

注意： 必须提供 angular_resolution 或 pixel_count 之一。

band [ visual | short | medium | long | very_long ]

定义传感器将检测的辐射波段。波段的波长定义如下：

▫ visual: 380-760 nm   
▫ short: $1 { - } 3 \mu \mathrm { m }$   
▫ medium: $3 - 5 \mu \mathsf { m }$   
▫ long: $8 \mathrm { - } 1 2 \mu \mathrm { m }$   
▫ very_long: $1 5 { - } 3 0 ~ { \mu \mathrm { m } }$

默认值： visual

atmospheric_attenuation <value> per <length-value>

有时称为消光系数，这是每单位距离传播时被衰减的信号分数（在 0 到 1 的闭区间内）。该值根据高度变化调整以考虑空气密度。

默认值： 0.0 每米（无衰减）

▪ background_radiance <value> <power-units>/<angle-units>/<area-units>

指定背景的辐射亮度。

默认值： 0.0

background_radiance_above_horizon <value> <power-units>/<angle-units>/<area-units>   
background_radiance_below_horizon <value> <power-units>/<angle-units>/<area-units>

提供固定背景辐射亮度的替代方案。这对于传感器可能向上看天空或向下看地面作为背景的空中传感器很有用。

background_transition_angle <lower-angle> <upper-angle>

与 background_radiance_above_horizon 和 background_radiance_below_horizon 一 起使用，以指定从使用地平线下方和上方背景辐射亮度值的过渡区域。指定的角度相对于地平线的局部角度，正值在地平线上方，负值在地平线下方。如果目标在这些角度定义的过渡区域内，结果背景辐射亮度将在上方和下方的值之间线性插值。

默认值： $0 . 0 \deg 0 . 0 \deg$ （即无过渡区域）

detection_threshold <value>

定义声明成功检测所需的信噪比。

默认值： 无（必须指定）

noise_equivalent_irradiance <value> <power-units>/<area-units>

接收器的“噪声等效辐照度”（NEI）。

默认值： 无（必须指定）

通过这些命令，您可以配置 WSF_EOIR_SENSOR 的不同模式和参数，以便在光学或红外成像应用中进行有效的目标检测和分析。

接收器命令

以下命令用于通用接收器设置：

antenna_pattern <pattern-name>

定义伪天线模式的名称（通过 antenna_pattern 命令定义），用于考虑传感器观察孔径引起的方向依赖效应。如果天线模式反映了通过固定孔径的损耗（例如，传感器安装在某种窗户后面），则相关的关节部分的 slew_mode 应为 slew_mode fixed（默认值）。否则，天线模式将随传感器提示移动。

默认值： 如果未指定天线模式，效果为 0dB（即无调整）。

internal_loss <db-ratio>

定义可以应用于计算的附加常数损耗。

默认值： 0dB（即无附加损耗）

注意： 这应该是一个正的 dB 值，因为它出现在分母中。

# 红外模式方程

1. 确定目标（点源）的红外辐射强度 [瓦特/球面度]

$$
I _ {s} = i n f r a r e d \_ s i g n a t u r e (a z, e l)
$$

2. 确定背景辐射强度 [瓦特/球面度]

$$
I _ {b} = \text {b a c k g r o u n d} \times \text {o p t i c a l} (a z, e l)
$$

3. 确定对比辐射强度[瓦特/球面度]

$$
I _ {c} = I _ {s} - I _ {b}
$$

4. 确定大气透过率

$$
\tau = f (\text {a t m o p h e r i c}
$$

5. 确定有效目标辐照度 [瓦特/平方米]

$$
E _ {e f f} = \frac {\tau \times I _ {c}}{R ^ {2}}
$$

6. 调整目标辐照度以考虑结构遮挡

$$
E _ {e f f} = E _ {e f f} \times \text {m a s k i n g \_ p a t t e r n} (a z, e l)
$$

7. 确定信噪比

$$
S / N = \frac {E _ {e f f}}{N E I}
$$

可视模式方程

注意： 可视模式方程非常基础。实际上，如果目标在视场内且没有结构遮挡，则目标将被

检测到。

1. 确定目标的固有对比度 [无量纲]

$$
C _ {s} = \text {i n h e r e n t} (a z, e l)
$$

2. 确定大气透过率

$$
\tau = f (\text {a t m o s p h e r i c}
$$

3. 确定传感器处目标的固有对比度 [无量纲]

$$
C _ {s} = C _ {s} \times \tau
$$

4. 确定背景辐射亮度 [瓦特/平方米/球面度]

$$
L _ {b} = b a c k g r o u n d \_ r a d i a n c e
$$

5. 确定传感器处的背景辐射亮度 [瓦特/平方米/球面度]

$$
L _ {b s} = \left(L _ {b} \times \tau\right) + p a t h _ {-} r a d i a n c e
$$

6. 确定目标相对于背景的对比度 [无量纲]

$$
C _ {s} = C _ {s} \times \frac {L _ {b}}{L _ {b s}}
$$

7. 调整对比度以考虑结构遮挡

$$
C _ {s} = C _ {s} \times \text {m a s k i n g \_ p a t t e r n} (a z, e l)
$$

8. 确定信噪比

$S / N = 0$ 如果对比度为 0，否则为 1。

这些方程和命令帮助定义和调整传感器的接收器特性，以便在不同的环境和条件下进行有效的目标检测和分析。

# 3.5.10. 被动射频检测传感器 WSF_ESM_SENSOR

和 3.5.4 被动射频检测传感器 WSF_PASSIVE_SENSOR 一样。参见它的命令就好。

# 3.5.11. 红外搜索跟踪传感器 WSF_IRST_SENSOR

```txt
sensor <name> WSFIRST_SENSOR Platform Part Commands ... ... sensor Commands ... 
```

```txt
mode <name> ... WSFIRST_SENSOR Mode Commands ... end_mode end SENSOR 
```

WSF_IRST_SENSOR 实现了一个基本的红外搜索和跟踪（IRST）传感器，用于目标检测。该传感器通过被动检测红外辐射来识别和跟踪目标。

# 模式命令

atmospheric_attenuation <value> per <length-units>

指定信号在海平面每单位距离传播时的衰减分数（在 0 到 1 的闭区间内）。衰减根据高度变化调整以考虑空气密度。

默认值： 0.0 每米（无衰减）

background_radiance <value> <power-units>/<angle-units>/<area-units> background_radiance dynamic

指定背景的辐射亮度。如果指定为 dynamic，则使用实验动态背景模型，该模型目前仅对从传感器正仰角（例如：向上看卫星）有效。

默认值： 0.0

background_radiance_above_horizon <value> <power-units>/<angle-units>/<area-units> background_radiance_below_horizon <value> <power-units>/<angle-units>/<area-units>

提供固定背景辐射亮度的替代方案。这对于传感器可能向上看天空或向下看地面作为背景的空中传感器很有用。

background_transition_angle <lower-angle> <upper-angle>

与 background_radiance_above_horizon 和 background_radiance_below_horizon 一起使用，以指定从使用地平线下方和上方背景辐射亮度值的过渡区域。指定的角度相对于地平线的局部角度，正值在地平线上方，负值在地平线下方。

默认值： 0.0 度 0.0 度（即无过渡区域）

band [ short | medium | long | very_long ]

定义传感器将检测的辐射波段。波段的波长定义如下：

short: $1 - 3\mu m$ medium: $3 - 5\mu m$ long: $8 - 12\mu m$ very_long: $15 - 30\mu m$

默认值： 无（必须指定）

detect_negative_contrast <bool>

声明传感器是否会检测与背景对比为负的目标（即目标的辐射强度小于背景的辐射强度）。如果为 true，则负对比将被视为正对比，从而可能被检测到。

默认值： true

detection_threshold <value>

定义声明成功检测所需的信噪比。

默认值： 无（必须指定）

noise_equivalent_irradiance <value> <power-units>/<area-units>

接收器的“噪声等效辐照度”（NEI）。

默认值： 无（必须指定）

antenna_pattern <pattern-name>

定义伪天线模式的名称（通过 antenna_pattern 命令定义），用于考虑传感器观察孔径引起的方向依赖效应。

默认值： 如果未指定天线模式，效果为 0dB（即无调整）

internal_loss <db-ratio>

定义可以应用于计算的附加常数损耗。

默认值： 0dB（即无附加损耗）

传感器方程

1. 确定目标（源）的红外辐射强度

$$
I _ {s} = i n f r a r e d \_ s i g n a t u r e (a z, e l)
$$

2. 确定背景辐射强度

$$
I _ {b} = \text {b a c k g r o u n d} \cdot \text {r a d i a n c e} \times \text {o p t i c a l} \cdot \text {s i g n a t u r e} (a z, e l)
$$

3. 确定对比辐射强度

$$
I _ {c} = I _ {s} - I _ {b}
$$

4. 确定大气透过率

$$
\tau = f (\text {a t m o s p h e r i c}
$$

5. 确定有效目标辐照度

$$
E _ {e f f} = \frac {\tau \times I _ {c}}{R ^ {2}}
$$

6. 调整目标辐照度

$$
E _ {e f f} = \frac {E _ {e f f} \times a n t e n n a _ {\mathrm {p a t t e r n}} (a z , e l)}{i n t e r n a l _ {\mathrm {l o s s}}}
$$

7. 确定信噪比

$$
S / N = \frac {E _ {e f f}}{N E I}
$$

这些命令和方程帮助配置和模拟 WSF_IRST_SENSOR 的性能，以便在不同的环境条件下进行有效的目标检测和跟踪。

3.5.12. 激光雷达传感器 WSF_LADAR_SENSOR  
sensor $\text{一} _ { \text{一} }$ WSF_LADAR_SENSOR   
... Platform Part Commands ...   
... sensor Commands ..   
mode $\text{一} _ { \text{一} }$ Antenna Commands ...   
... Common Mode Commands ...   
# Mode Commands   
background_temperature or background_irradiance ...   
# Detection Processing Commands   
integration_gain ...   
detection_threshold ...   
detection(probability ...   
# Transmitter Commands   
transmitter   
... Common Transmitter Commands ...   
aperture_diameter ...   
optics_transmission_factor ...   
beam_divergence_angle ...   
end_transmitter   
# Receiver Commands   
receiver   
... Common Receiver Commands ...   
aperture_diameter..."   
optics_transmission_factor ...   
quantum_efficiency ...   
detector_gain ...   
circuit_temperature ...   
circuit_capacitance ...   
dark_current_rate or dark_current ...   
focal_length ...   
detector_size ...   
end RECEIVER   
end_mode   
end SENSOR

WSF_LADAR_SENSOR 实现了一个基础的直接检测激光雷达（LADAR）传感器。该模型提供了辐射测量和检测处理，而模拟框架则负责所有几何计算和目标属性的确定，如投影面积和反射率。它完全支持传感器中定义的多种模式。

# 主要功能

轨迹生成：传感器的主要输出是轨迹（WsfTrack）。轨迹根据常见传感器模式命令中定义的正常轨迹形成标准创建。传感器误差也可以包括在内。  
目标平台要求：目标平台应具有 optical_signature 和 optical_reflectivity 定义。  
检测模型：不考虑传感器的错误提示（与雷达不同，雷达具有天线模式，如果目标位于偏轴位置，增益会降低）。为了防止目标在偏轴过远时被看到，始终指定“视场”。例如，在模式定义中输入以下天线命令：

▫ azimuth_field_of_view -1 deg 1 deg   
▫ elevation_field_of_view -1 deg 1 deg

# 模式命令

background_temperature <temperature-value>

使用普朗克定律从指定温度的黑体计算背景辐照度。

默认值： 5778 K

background_irradiance <spectral-irradiance-value>

直接指定背景辐照度。

# 检测处理命令

integration_gain <value>

定义通过集成多个脉冲获得的增益。

默认值： 1.0

detection_threshold <value>

定义信噪比（SNR），其结果是检测概率（Pd）为 0.5。

默认值： 1.0（如果定义了 detection_probability 表，则不使用此命令）

detection_probability <sn1> <pd1> … <snn> <pdn> end_detection_probability

定义一个表，用于根据信噪比确定检测概率。用户必须提供成对的数字（信噪比和检测概率），以定义 Pd 与 SNR 的曲线。

# 发射器命令

wavelength

必须指定，无默认值。

pulse_width

必须指定，无默认值。

pulse_repetition_interval 或 pulse_repetition_frequency

必须指定，无默认值。

bandwidth

默认值为与 1 纳米波长等效的频率。

attenuation_model

指定用于计算大气衰减的模型（通常为 WSF_OPTICAL_ATTENUATION）。

aperture_diameter <length-value>

定义 LADAR 发射器的孔径直径。

optics_transmission_factor <value>

定义通过发射器光学系统的激光光的百分比。

默认值： 1.0

beamwidth <angle-value> / beam_divergence_angle <angle-value>

指定发射光束的“光束宽度”。

# 接收器命令

aperture_diameter <length-value>

定义 LADAR 接收器（探测器）孔径的直径。

optics_transmission_factor <value>

定义通过接收器光学系统的激光光的百分比。

默认值： 1.0

quantum_efficiency <value>

信号（光子数）转换为光电子的比例。

默认值： 1.0（ $100 \%$ 效率）

detector_gain <value>

探测器的增益。

默认值： 1.0

circuit_temperature <temperature-value> / circuit_capacitance <capacitance-value>

用于指定计算热噪声成分所需的数据。

dark_count_rate <frequency-value> / dark_current <current-value>

用于指定计算背景噪声成分中的暗计数项所需的数据。

视场计算命令

focal_length <length-value>

指定接收器光学系统的焦距。

detector_size <length-value>

指定物理探测器一侧的长度，假设探测器是方形的。

这些命令和参数帮助配置 WSF_LADAR_SENSOR 的性能，以便在不同的环境条件下进行有效的目标检测和跟踪。

# 计算从激光脉冲接收到的能量

激光雷达（LADAR）传感器接收到的光子数 $N _ { l a s e r }$ 可以通过以下公式计算：

$$
N _ {l a s e r} = E _ {t} \tau_ {t} \tau_ {a} \left(\frac {A _ {r e f} \rho}{\pi}\right) \tau_ {a} \left(\frac {\pi D _ {r} ^ {2}}{4 R ^ {2}}\right) \tau_ {r} \eta Q E \frac {\lambda}{h c}
$$

参数说明

□ $N _ { l a s e r }$ ：接收到的光子数。  
□ $E _ { t }$ ：发射能量，计算如下。  
□ $\tau _ { t }$ ：发射器的光学传输因子。  
□ $\tau _ { a }$ ：使用发射器的衰减模型计算的大气衰减。

□ $A _ { r e f }$ ：激光光反射的面积。  
□ $\rho$ ：目标的光学反射率。  
▫ $D _ { r }$ ：接收器块的孔径直径。  
□ R：传感器与目标之间的距离。  
□ $\tau _ { r }$ ：接收器块的光学传输因子。  
□ $\eta Q E$ ：接收器块的原子效率。  
□ ?：发射器块的波长。  
▫ ℎ?：普朗克常数、光速。

# 发射能量计算

发射能量 $E _ { t }$ 可以通过以下公式计算（取决于用户提供的输入）：

$$
E _ {t} = P _ {t} t _ {p} \text {或} E _ {t} = P _ {t} / f _ {p}
$$

▫ $P _ { t }$ ：发射器块的功率。  
□ $t _ { p }$ ：发射器块的脉冲重复间隔。  
$f _ { p }$ ：发射器块的脉冲重复频率。

# 反射面积计算

反射面积 $A _ { r e f }$ 取以下值的最小值：

□ $\mathrm { A _ { b e a m } }$ : 目标平面的激光光束面积。  
= $\mathsf { A } _ { \mathrm { p r o j } }$ : 由目标的光学特征定义的投影面积。  
▫ $\mathsf { A } _ { \mathrm { I F 0 V } }$ : 目标平面上接收器瞬时视场（IFOV）的面积（可选）。

激光光束在目标平面的面积计算如下：

$$
\mathrm {A _ {b e a m}} = \frac {\pi \theta^ {2} \mathrm {R ^ {2}}}{4}
$$

其中θ是发射器的光束宽度。

如果提供了必要的输入项，接收器在目标平面的 IFOV 面积计算如下：

$$
A _ {I F O V} = \left(\frac {R S}{f}\right) ^ {2}
$$

▫ R: 接收器到目标的距离。  
□ S: 接收器块的探测器尺寸。  
▫ f: 接收器块的焦距。

# 噪声计算

噪声的三个组成部分：

1. 背景噪声。  
2. 接收器中的热噪声。

背景噪声的光电子数由以下三个主要成分组成：

从目标反射回接收器的环境（太阳）光。  
□ 即使接收器孔径被覆盖时“检测到”的电子（“暗计数”）。  
□ $\mathrm { \Delta N _ { l a s e r } }$ 的统计变化。

环境光的辐射强度计算为：

$$
L _ {B} = S _ {B} B _ {r}
$$

接收器带宽内的背景辐照度（瓦特/平方米）

$$
P _ {r e f} = L _ {B} A _ {r e f} \rho
$$

从目标区域反射的功率（W/sr）

$$
E _ {s r} = P _ {r e f} \times \tau_ {p}
$$

每球面度的反射能量（J/sr）

然后使用前一节中的接收部分方程计算电子数：

$$
N _ {b a c k} = E _ {s r} \tau_ {a} \frac {\pi D _ {r} ^ {2}}{4 R ^ {2}} \tau_ {r} \eta_ {e} \frac {\lambda}{h c}
$$

第二个成分是脉冲接收时发生的暗电流光电子数：

$$
N _ {d a c k} = f _ {d c} \times \tau_ {p}
$$

其中： $f _ { d c }$ 为接收器块的暗计数率， $\tau _ { p }$ 接收器块的脉冲宽度。

复合背景噪声为：

$$
N _ {b a c k g r o u n d} = N _ {b a c k} + N _ {d a c k}
$$

信号光子的到达假设为泊松分布，产生的光电子的未放大方差等于平均值。这种方差也是噪声的来源：

$$
Q _ {n, s i g n a l} ^ {2} = N _ {l a s e r}
$$

电路中的热噪声光电子数计算为：

$$
Q _ {n, t h e r m a l} ^ {2} = \frac {k T C}{e ^ {2}} N _ {t h e r m a l} = \sqrt {Q _ {n , t h e r m a l} ^ {2}}
$$

□ ：玻尔兹曼常数。  
▫ ：接收器块的电路温度。  
?：接收器块的电路电容。  
□ e：基本电荷（电子电荷）。

信噪比计算

信噪比（SNR）计算为：

$$
\mathrm {S N R} = \frac {\mathrm {G} \times \mathrm {N} _ {\text {l a s e r}}}{\sqrt {\mathrm {Q} _ {\mathrm {n , t h e r m a l}} ^ {2} + \mathrm {G} (\mathrm {Q} _ {\mathrm {n , s i g n a l}} ^ {2} + \mathrm {N} _ {\text {b a c k g r o u n d}})}}
$$

其中 G是接收器块的探测器增益，其他值如前述部分所述计算。

# 3.5.13. 光学传感器 WSF_OPTICAL_SENSOR

```txt
sensor <name> WSF_OPTICAL_SENSOR Platform Part Commands ... ... sensor Commands ... mode <name> ... Antenna Commands ... receiver Commands ... ... WSF_OPTICAL_SENSOR Mode Commands ... end_mode end SENSOR 
```

WSF_OPTICAL_SENSOR 实现了一个简单的光学传感器模型。该模型通过假设恒定的背景对比度和线性大气衰减来计算目标对比度，以评估目标检测的可能性。其对比度阈值基于 地面观察者的视觉检测模型 ，由 ArthurC.PoeIII 于 1974 年在美国陆军导弹司令部发布。

# 模式命令

atmospheric_attenuation <value> per <length-units>

指定信号在海平面每单位距离传播时的衰减分数（在 0 到 1 的闭区间内）。衰减根据高度变化调整以考虑空气密度。

默认值： 0.0 每米（无衰减）

▪ background_radiance <value> <power-units>/<solid-angle-units>/<area-units>

指定背景的辐射亮度。

默认值： 0.0

path_radiance <value> <power-units>/<angle-units>/<area-units>

指定路径辐射亮度。

默认值： 0.0

reacquisition_time <value> <time-units>

指定当轨迹丢失时传感器的重新获取时间。

默认值： 3.0 秒

# Glimpse 数据命令

这些命令用于为每个光学检测序列计算一张概率表。

search_glimpse_data … end_search_glimpse_data定义搜索时的概率表数据。  
reacquire_glimpse_data … end_reacquire_glimpse_data定义重新获取时的概率表数据。  
track_glimpse_data … end_track_glimpse_data定义跟踪时的概率表数据。

# 搜索 Glimpse 数据命令

azimuth_fov <value> <angle-units>

指定传感器的方位视场。

默认值： 5.0 度

minimum_elevation <value> <angle-units>

指定传感器的最低仰角。

默认值： 0.0 度

maximum_elevation <value> <angle-units>

指定传感器的最高仰角。

默认值： 5.0 度

number_of_iterations <value>

指定将执行的蒙特卡罗迭代次数以创建概率表。

默认值： 1000
magnification <value>指定传感器的放大倍率。默认值： 1.0  
apparent_half_angle_FOV <value> <angle-units>指定传感器的视场半角。默认值： 45.0 度  
minimum_resolution <value> <angle-units>指定传感器的最小分辨率。默认值： 0.001 sr  
contrast_gain <value>指定传感器的对比增益。默认值： 1.0  
ocular_integration_level <value> <angle-units>指定传感器的眼部集成水平。默认值： 0.05 度

这些命令和参数帮助配置 WSF_OPTICAL_SENSOR 的性能，以便在不同的环境条件下进行有效的目标检测和跟踪。