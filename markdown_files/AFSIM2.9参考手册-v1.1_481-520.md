发射机的峰值功率输出。

默认值：无。必须指定 power 或 powers 之一。如果指定了多个，则使用最后一个指定的。

powers … end_powers

允许定义发射机的频率依赖峰值功率输出。

格式：

```txt
powers  
frequency <frequency-value-1> <power-value-1>  
frequency <frequency-value-2> <power-value-2>  
...  
frequency <frequency-value-n> <power-value-n>  
endpowers 
```

算法：

频率大于或等于 frequency-value-m 且小于 frequency-value- $m { + 1 }$ 时使用 power-value-m。

频率小于 frequency-value-1 时使用 power-value-1。

频率大于或等于 frequency-value-n 时使用 power-value-n。

默认值：无。必须指定 power 或 powers 之一。如果指定了多个，则使用最后一个指定的。

注意：条目将按频率递增顺序排序。

propagation_model <derived-name>   
propagation_model <base-name> …commands… end_propagation_model

指定传播模型。有关可用传播模型及其配置的信息，请参见全局命令 3.5.5.6 传播模型propagation_model。

默认值：无（无传播效果）

pulse_compression_ratio <db-ratio-value>

指定由于脉冲压缩/编码技术带来的增益。

默认值：0dB（无脉冲压缩）

注意：这不会改变发射信号的有效辐射功率。脉冲压缩的效果在信号接收时应用。它在发射机上定义，因为压缩/编码实际上发生在那里。

pulse_repetition_frequency <frequency-value>   
pulse_repetition_interval <time-value>

指定脉冲发射机的脉冲速率或脉冲间隔，可以使用以下方法之一：

每秒的平均脉冲数（pulse_repetition_frequency）。

脉冲前沿之间的平均时间（pulse_repetition_interval）。

默认值：pulse_repetition_frequency 0 Hz

注意：如果指定了非零值，则必须指定非零 pulse_width。

pulse_repetition_frequencies … end_pulse_repetition_frequencies   
pulse_repetition_intervals … end_pulse_repetition_intervals

指定脉冲发射机的脉冲速率或脉冲间隔列表，可以使用以下方法之一：

每秒的平均脉冲数（pulse_repetition_frequencies … end_pulse_repetition_frequencies）。

脉冲前沿之间的平均时间（pulse_repetition_intervals … end_pulse_repetition_intervals）。

```txt
pulse_repetition_frequencies prf_id <id><frequency-value> 
```

```txt
...   
end_pulse_repetition_frequencies   
pulse_repetition_intervals pri_id <id> <time-value> ...   
end_pulse_repetition_intervals 
```

□ <id>：用于添加多个脉冲重复频率的有序输入 ID，范围为[1,N]。  
□ <frequency-value>：给定<id>的脉冲重复频率值。   
□ <time-value>：给定<id>的脉冲重复间隔值。

默认值： $0 H z$ ，未定义

注意：如果指定了非零值，则必须指定非零 pulse_width。

pulse_width <time-value>

指定脉冲发射机的平均脉冲宽度（以时间单位）。

默认值：0 秒

注 意 ： 如 果 指 定 了 非 零 值 ， 则 必 须 指 定 非 零 pulse_repetition_frequency 或pulse_repetition_interval。

use_peak_power <boolean-value>

当设置为 true 时，切换此发射机以在所有适用的内部计算中使用峰值功率，并通过扩展，所有由此发射机预测的结果交互。当设置为 false 时，使用平均功率。

默认值：False（使用平均功率）

alternate_frequency <id> <frequency-value>

指定备用频率，当检测到干扰时，通信设备与 jamming_perception_timeout 和jamming_perception_threshold 结 合 使 用 ， 或 WSF_RADAR_SENSOR 与jamming_perception_timeout 、 jamming_perception_threshold 和 electronic_protectWSF_AGILITY_EFFECT 技 术 结 合 使 用 。 对 于 WSF_RADAR_SENSOR 类 型 ， 可 以 通 过randomize_radar_frequencies 命令在模拟初始化期间随机选择频率。可以输入多个具有连续递增<id>的条目。

□ <id>：用于添加多个备用频率的有序输入 ID，范围为[1,N]。  
□ <frequency-value>：给定<id>的备用频率值。

electronic_attack … end_electronic_attack

定义发射机的电子攻击能力。有关详细信息，请参见 3.5.5.8.1 电子攻击模型electronic_attack。

默认值：无电子攻击能力。

# 3.5.5.8.1. 电子攻击模型 electronic_attack

参见 3.5.5.10 电子战模型

# 3.5.5.9. 接收机 receiver

```txt
receiver
... Antenna Commands ...
antenna_ohmic_loss <db-ratio-value>
antenna_pattern <pattern-name>
antenna_pattern_table ... end_antenna_pattern_table 
```

```tcl
attenuation_model <derived-name>   
attenuation .... (attenuation is a synonym for attenuation_model)   
aux_data ... end(aux_data   
bandwidth <frequency-value>   
beam_tilt <angle-value>   
check_terrain_masking <boolean-value>   
check_transmitter_masking <boolean-value>   
terrain_masking_mode [ terrain_andHorizon | terrain_only | horizon_only ]   
detection_threshold <db-ratio-value>   
earth_radiusmultiplier <value>   
effective-earth_radius <length-value>   
frequency <frequency-value>   
wavelength <length-value>   
instantaneous-bandwidth <frequency-value>   
internal_loss <db-ratio-value>   
noise_figure <db-ratio-value>   
noise_power <power-value>   
polarization [ horizontal | vertical | slant_45 | slant_135 | left_circular | right_circular | default ]   
polarization Effect [ horizontal | vertical | slant_45 | slant_135 | left_circular | right_circular ]   
<fraction>   
propagation_model <derived-name>   
receive_line_loss <db-ratio-value>   
electronic_protect ... end_electronic_protect   
end Receiver 
```

接收机模块定义了电磁接收机的属性，广泛应用于各种传感器和通信设备。

antenna_ohmic_loss <db-ratio-value>

指定天线的欧姆电阻损耗，这与噪声系数和接收线损耗一起用于确定接收机的噪声功率。

默认值：0dB（无损耗）

注意：指定 antenna_ohmic_loss 或 receive_line_loss 会触发使用替代方法来计算噪声功率。对于许多应用，应该使用 internal_loss 来考虑损耗。

天线增益模式

antenna_pattern <pattern-name>

指定接收机使用的天线增益模式的名称。模式必须使用3.5.5.5天线模式antenna_pattern命令定义。

默认值：如果省略 antenna_pattern 和 antenna_pattern_table，它们将从隐式关联的发射机中复制（如果已定义）。否则，天线增益将假定为常数 1（0dB）。

注意：如果同时指定了 antenna_pattern 和 antenna_pattern_table，则使用最后一个指定的。

antenna_pattern_table … end_antenna_pattern_table

允许定义频率依赖或极化和频率依赖的天线增益模式。每个命名的天线模式必须使用antenna_pattern 命令定义。

频率依赖表格式：

```txt
antenna_pattern_table frequency <frequency-value-1> <pattern-name-1> frequency <frequency-value-2> <pattern-name-2> ... frequency <frequency-value-n> <pattern-name-n> end_antenapattern_table 
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
end_antenna_pattern_table 
```

规则：

▫ 任何在第一个 polarization 条目之前出现的 frequency 条目假定适用于 default 极化。  
□ 未定义的极化将使用 default 极化的定义。  
▫ 必须定义 default 极化。

算法：

□ 如果使用极化依赖表，接收信号的极化用于定位适当的极化特定频率条目集。如果没有对应的条目，则使用 default 条目。  
□ 频 率 大 于 或 等 于 frequency-value-m 且 小 于 frequency-value-m+1 时 使 用pattern-name-m。  
□ 频率小于 frequency-value-1 时使用 pattern-name-1。  
□ 频率大于或等于 frequency-value-n 时使用 pattern-name-n。

attenuation_model <derived-name>   
attenuation_model <base-name> …commands… end_attenuation_model

指定衰减模型。有关可用衰减模型及其配置的信息，请参见全局命令 3.5.5.7 衰减模型attenuation_model。

默认值：无（无衰减效果）

注意：此命令仅对接收来自非发射机信号的接收机有效。

aux_data … end_aux_data

定义应用程序特定的“辅助数据”。

默认值：未定义辅助数据。

bandwidth <frequency-value>

指定接收机的带宽。接收机将接受频率在以下范围内的信号： [ frequency - 1/2bandwidth, frequency $+ ~ 1 / 2$ bandwidth ]

对于频率跳变系统，频率应设置为频率跳变范围的中心，带宽应设置为涵盖频率范围。

需要注意的是，WSF 目前不模拟实际的瞬时频率跳变。

默认值：如果省略此值，将使用 instantaneous_bandwidth 的值（如果非零）。否则假定为零。

注意：此命令不应与 WSF_PASSIVE_SENSOR 一起使用，因为它会从 WSF_PASSIVE_SENSOR命令中隐式生成所需数据。

beam_tilt <angle-value>

仅在定义使用多个波束的系统时使用（例如，在 WSF_RADAR_SENSOR 中使用多个波束）。

指定波束中心在水平面上的仰角。

默认值：如果有隐式关联的发射机（例如在 WSF_RADAR_SENSOR 中），则默认值为关联发射机的 beam_tilt 值。如果没有关联发射机或未在关联发射机中指定 beam_tilt，则假定为 0 度。

注意：不应与 antenna_tilt 或:command_.articulated_part.pitch 命令一起使用。

check_terrain_masking <boolean-value>

切换地形和地平线视线的计算。可以设置为“off”以减少计算或模拟没有视线限制的传感器和通信设备。默认情况下，首先检查地平线遮蔽，然后在加载地形时进行单独的地形遮蔽检查。简单的地平线遮蔽检查假设地球是光滑的球形，任何低于海平面的物体都被遮挡。对于地下传感器，可以通过将 terrain_masking_mode 设置为 terrain_only 来禁用地平线检查。

默认值：on

check_transmitter_masking <boolean-value>

切换发射机检查的地形和地平线视线的计算。可以设置为“off”以减少计算或模拟没有视线限制的传感器和通信设备，例如双基地传感器。

默认值：on

terrain_masking_mode [ terrain_and_horizon | terrain_only | horizon_only ]

设置要执行的遮蔽检查模式或类型。默认情况下，启用地平线和地形遮蔽检查。

默认值：terrain_and_horizon

detection_threshold <db-ratio-value>

指定信号被声明为可检测的信噪比。

默认值：3dB

注意：某些系统（特别是 WSF_PASSIVE_SENSOR 和 WSF_RADAR_SENSOR）使用其他标准来确定接收到的信号是否足以检测。在这些情况下，此命令无效，不应使用。

earth_radius_multiplier <value>   
effective_earth_radius <length-value>

指定用于计算无线电频率信号大气折射效应的地球半径乘数或有效地球半径。

默认值：earth_radius_multiplier 1.0

注意：此命令仅对接收来自非发射机信号的接收机有效。对于涉及发射机的命令（如RF 传感器或通信），应在发射机块中指定此命令。

frequency <frequency-value>   
wavelength <length-value>

指定接收机调谐的中心频率。接收机将接受频率在以下范围内的信号：[frequency-1/2bandwidth, frequency $+ ~ 1 / 2$ bandwidth ]

波长是输入频率的替代机制。结果频率计算为： frequency $=$ speed-of-light / wavelength

默认值：如果接收机与发射机隐式关联（如单基地雷达系统），则默认值与关联发射机的频率相同。对于独立接收机，必须指定一个值。

注意：此命令不应与 WSF_PASSIVE_SENSOR 一起使用，因为它会从 WSF_PASSIVE_SENSOR

命令中隐式生成所需数据。

instantaneous_bandwidth <frequency-value>

指定接收机的瞬时带宽。对于频率跳变或扫描系统，这将是单个跳变或扫描点期间处理的带宽。

如果未显式提供噪声功率，则此值用作计算接收机噪声功率的带宽。

默认值：如果省略此值，将使用 bandwidth 的值（如果非零）。否则假定为零。

internal_loss <db-ratio-value>

用于考虑各种杂项损耗的单一数值。此值出现在分母中，用于调整信号强度： $S ^ { ' } =$ ?????????_????

默认值：0dB（无内部损耗）

noise_figure <db-ratio-value>

与天线欧姆损耗和接收线损耗一起提供一种指定接收机噪声功率的方法。

默认值：0dB

noise_power <power-value>

指定显式噪声功率。这是指定接收机噪声的一种机制。

polarization [ horizontal | vertical | slant_45 | slant_135 | left_circular | right_circular | default ]

指定接收天线将接收的信号的主要极化。

默认值：default

polarization_effect [ horizontal | vertical | slant_45 | slant_135 | left_circular | right_circular ] <fraction>

定义接收信号的指定极化将被处理的比例。这允许在接收机尝试接收与其主要极化不同的信号时覆盖默认行为。

注意：如果声明了一个作为极化函数的 antenna_pattern_table，则对于接收到的信号，其极化在 antenna_pattern_table 中有对应条目且不是默认条目的，polarization_effects 条目将被忽略。在这种情况下，假定 antenna_pattern_table 条目包含任何极化失配的影响。

<table><tr><td>rcvr/xmtr</td><td>horizontal</td><td>vertical</td><td>slant_45</td><td>slant_135</td><td>left_circular</td><td>right_circular</td><td>default</td></tr><tr><td>horizontal</td><td>1.0</td><td>0.0</td><td>0.5</td><td>0.5</td><td>0.5</td><td>0.5</td><td>1.0</td></tr><tr><td>vertical</td><td>0.0</td><td>1.0</td><td>0.5</td><td>0.5</td><td>0.5</td><td>0.5</td><td>1.0</td></tr><tr><td>slant_45</td><td>0.5</td><td>0.5</td><td>1.0</td><td>0.0</td><td>0.5</td><td>0.5</td><td>1.0</td></tr><tr><td>slant_135</td><td>0.5</td><td>0.5</td><td>0.0</td><td>1.0</td><td>0.5</td><td>0.5</td><td>1.0</td></tr><tr><td>left_circular</td><td>0.5</td><td>0.5</td><td>0.5</td><td>0.5</td><td>1.0</td><td>0.0</td><td>1.0</td></tr><tr><td>right_circular</td><td>0.5</td><td>0.5</td><td>0.5</td><td>0.5</td><td>0.0</td><td>1.0</td><td>1.0</td></tr><tr><td>default</td><td>1.0</td><td>1.0</td><td>1.0</td><td>1.0</td><td>1.0</td><td>1.0</td><td>1.0</td></tr></table>

propagation_model <derived-name>   
propagation_model <base-name> …commands… end_propagation_model

指定传播模型。有关可用传播模型及其配置的信息，请参见全局命令 3.5.5.6 传播模型propagation_model。

默认值：无（无传播效果）

注意：此命令仅对接收来自非发射机信号的接收机有效。

receive_line_loss <db-ratio-value>

指定天线与接收机之间的射频组件线损耗。与天线欧姆损耗和噪声系数一起提供一种指定接收机噪声功率的方法。

默认值：0dB（无损耗）

注意：指定 antenna_ohmic_loss 或 receive_line_loss 会触发使用替代方法来计算噪声功率。对于许多应用，应该使用 internal_loss 来考虑损耗。

# 带宽重叠比率 Bandwidth Overlap Ratio

在涉及发射机和接收机的单向交互过程中（例如通信尝试或被动传感器检测尝试），使用两者的频率和带宽来确定频率重叠的量。这产生了一个“带宽重叠比率”，即发射频谱中位于接收机带宽内的频谱量。

计算步骤

设定：

$f _ { x }$ ：发射机频率。

$B _ { x }$ ：发射机带宽。

$f _ { r }$ ：接收机频率。

$B _ { r }$ ：接收机带宽。

$f _ { x l }$ ：发射机频谱下限。

$f _ { x u }$ ：发射机频谱上限。

$f _ { r l }$ ：接收机频谱下限。

$f _ { r u }$ ：接收机频谱上限。

$B _ { r } ^ { ' }$ ：有效接收机带宽。

$F _ { B W }$ ：有效接收机带宽重叠比率。

1、发射机频谱范围计算：

一 下限：??? = ?? − ?? $\begin{array} { r } { f _ { x l } = f _ { x } - \frac { B _ { x } } { 2 } } \end{array}$

□ 上限： $\begin{array} { r } { f _ { x u } = f _ { x } + \frac { B _ { x } } { 2 } } \end{array}$

2、确定有效接收机带宽

$$
B _ {r} ^ {\prime} = \left\{ \begin{array}{l l} B _ {r} & i f B _ {r} \neq 0 \\ B _ {t} i f f _ {x l} \leq f _ {r} \leq f _ {x u} \end{array} \right.
$$

第二种情况处理未指定接收机带宽的情况。这是一种简化，表示只要指定的接收机频率在发射频谱内，接收机和发射机就被认为是“匹配的”。

3、接收机频谱范围计算：

下限：??? = ?? − ??' $\begin{array} { r } { f _ { r l } = f _ { r } - \frac { B _ { r } ^ { ' } } { 2 } } \end{array}$   
上限： $\begin{array} { r } { f _ { r u } = f _ { r } + \frac { \dot { B _ { r } } } { 2 } } \end{array}$

4、确定带宽重叠比率

□ 如果 $f _ { x u } \leq f _ { r l }$ 或 $f _ { x l } \geq f _ { r u }$ 则 $F _ { B W } = 0$   
□ 否则： $\begin{array} { r } { F _ { B W } = m i n \left( \frac { m i n \left( f _ { x u } , f _ { r u } \right) - m a x \left( f _ { x l } , f _ { r l } \right) } { f _ { x u } - f _ { x l } } , 1 . 0 \right) } \end{array}$ ???(???,???)−???(??? ,???)

# 接收机噪声的计算 Receiver Noise

接收机噪声可以通过以下几种方式确定。以下是方程中使用的定义：

k:玻尔兹曼常数 (1.3806505E-23 J/deg-K)

$\mathrm { { T _ { 0 } } }$ :标称环境温度 (290 deg-K)

B:接收机的（瞬时）带宽。

# 计算接收机噪声功率的过程

计算接收机噪声功率的过程如下。将使用满足条件的第一步的值。

# 1、如果指定了 WSF_RADAR_SENSOR

计算噪声功率。在这些情况下，接收机噪声被视为需要确定的变量。使用来自发射机的相关功率和频率以及提供的其他数据（无论是显式的还是默认的），使用雷达距离方程计算接收到的信号功率。然后使用以下公式计算噪声功率：

$$
N = \frac {\text {r e c e i v e d} _ {\text {p o w e r}}}{\text {d e t e c t i o n} _ {\text {t h r e s h o l d}}}
$$

# 2、如果指定了 noise_power

使用定义的值。

# 3、如果无法确定带宽

使用-160 dBW 的值。

# 4、接收机的带宽

将定义为从 instantaneous_bandwidth 或 bandwidth 中显式指定的值。如果没有定义这些值，则无法确定带宽。

# 5、如果指定了 noise_figure 且省略了 antenna_ohmic_loss 和 receive_line_loss

使用以下公式计算噪声功率：

$$
N = k \times T _ {0} \times B \times n o i s e \_ f i g u r e
$$

# 6、使用“Radar Range Performance”中定义的算法计算噪声功率

Lamont V. Blake, 1986, Artech House, Inc., 第 4 章。

# 天空噪声温度的贡献

由于天线的天空温度贡献 (Tant $=$ 天线指向角度引起的天空温度):

$$
T _ {a} = T _ {0} + \frac {0 . 8 7 6 \times \text {T a n t} - 2 5 4 . 0}{\text {a n t e n n a o h m i c l o s s)}}
$$

由于接收线损失的噪声温度贡献:

$$
T _ {l} = T _ {0} \times (r e c e i v e \_ l i n e \_ l o s s - 1. 0)
$$

由于接收机的噪声温度贡献:

$$
T _ {r} = T _ {0} \times (n o i s e \_ f i g u r e - 1. 0)
$$

总系统温度:

$$
T _ {s} = T _ {a} + T _ {l} + \left(\text {r e c e i v e \_ l i n e \_ l o s s} \times T _ {r}\right)
$$

然后计算噪声功率为:

$$
N = k \times T _ {s} \times B
$$

这些步骤和公式帮助确定接收机噪声功率，以便在不同条件下进行准确的计算。

# 3.5.5.9.1. 电子保护模型 electronic_protect

参见 3.5.5.10 电子战模型

# 3.5.5.10.电子战模型 electronic_warfare

本节介绍电子战模型（EW），也即涉及电子攻击（EA），电子防护（EP）。配置时往往在 3.5.5.8 发射机 transmitter 中配置 EA，在 3.5.5.9 接收机 receiver 中配置 EP。

```txt
electronicWARFAre<name> <type-name> debug technique <technique-name> <technique-type> ... Electronic Warfare Technique Commands ... end_technique   
end_electronicWARFAre 
```

<name>: 要创建的新电子战类型的名称。  
<type-name>: 一 个 现 有 电 子 战 类 型 的 名 称 ， 或 WSF_ELECTRONIC_ATTACK 或WSF_ELECTRONIC_PROTECT，其定义将用作新类型的初始定义。

electronic_warfare 提供了为发射器和接收器中的电子攻击和电子保护定义电子战类型的能力。电子攻击（EA） - 电子保护（EP）架构提供了定义 EA和 EP 技术并评估这些技术相互作用的能力。EA 和 EP 能力块均允许多种技术。接收器处的效果如 EA技术块中定义，除非 EP 技术块定义了一种具有关联效果的缓解技术来应对特定 EA技术。

debug

指定使用调试模式将调试数据输出到标准输出。

默认值为 false 或 off

technique <technique-name> [<technique-type-name>] … end_technique

定义唯一命名的技术及其派生类型（如果需要）。可以输入多个技术块。

<technique-name>*: 技术唯一名称的字符串输入。  
<technique-type-name>*: 技术类型的字符串输入。如果编辑已经定义的实例名称，则不需要此输入。

给个示例吧：

```txt
electronic_warfare EW_RADAR_EP WSF_ELECTRONIC_PROTECT technique sidelobe Canceling WSF_EP_TECHNIQUE #debug mitigated技术和e classes noise_jamming end_mitigated和技术e classes effect slc-effect WSF_SLC_EFFECT #debug 
```

```txt
number_canceller_channels 2  
cancellation_lock_ratio 3 dB  
antenna_pattern AUX ANTENNA  
cancellation_ratios  
jammer_to_noise 0.0 db 0.0 db  
jammer_to_noise 15.0 db 10.0 db  
jammer_to_noise 30.0 db 20.0 db  
saturation_ratio 10.0 dB  
end_cancellation_ratios  
end-effect  
end技术和 technique  
end_electronic_warfare 
```

整体电子战模型概述：

<table><tr><td>模型名称</td><td>用于</td><td>说明</td></tr><tr><td>频率捷变模型WSF_AGILITY_EFFECTWSF_RADAR_AGILITY_EFFECT</td><td>EP</td><td>通过改变频率和切换雷达的工作模式来对抗干扰,实施EP。</td></tr><tr><td>通信模型WSFCOMM_EFFECT</td><td>EA、EP</td><td>通过丢弃、扭曲、误码等手段来干扰对方实施EA,以及通过设定这些指标来保护已方实施EP。模拟各种通信干扰和保护措施。</td></tr><tr><td>功率模型WSF_POWER_EFFECTWSF_JAMMER_POWER_EFFECT</td><td>EA、EP</td><td>通过调整信号增益、噪声增益等来实施EA、EP。</td></tr><tr><td>脉冲密度模型WSF_PULSE_EFFECT</td><td>EA、EP</td><td>通过调整脉冲的密度来实施EA、EP。</td></tr><tr><td>脉冲抑制模型WSF_PULSESuppress_EFFECT</td><td>EP</td><td>模拟对雷达信号的脉冲参数进行抑制或允许来实施EP。</td></tr><tr><td>旁瓣消隐模型WSF_SLB_EFFECT</td><td>EP</td><td>通过识别旁瓣进入的干扰信号实施EP。</td></tr><tr><td>旁瓣相消模型WSF_SLC_EFFECT</td><td>EP</td><td>通过抵消来自旁瓣的信号来实施EP。</td></tr><tr><td>跟踪模型WSF Track_EFFECT</td><td>EA、EP</td><td>通过引入距离、方位角等误差来针对对方的跟踪系统来实施EA,设置不同的跟踪行为来实施EP。</td></tr><tr><td>扩展旁瓣消隐模型WSF_NX_SLB_EFFECT</td><td>EP</td><td>增强的旁瓣消隐模型,更灵活的消隐算法支持,主要用于实施EP。</td></tr><tr><td>脉冲覆盖模型WSF_COVER_PULSE_EFFECT</td><td>EA</td><td>通过增加目标的回波概率来实现特定的信噪比来对目标施加EA。</td></tr><tr><td>假目标模型WSFFalse_TARGET_EFFE</td><td>EA</td><td>通过生成假目标来实施EA。</td></tr><tr><td>CT
WSF_FT_EFFECT</td><td></td><td></td></tr><tr><td>极化调制模型
WSF_POL_MOD_EFFECT</td><td>EA</td><td>通过控制极化调制速率来实施 EA。</td></tr><tr><td>半径因子调制模型
WSF_RADIUS_EFFECT
WSF_JAMMER_RADIUS_EFFECT</td><td>EA</td><td>根据距离目标的距离和半径来调整干扰功率实现 EA。往往与其它手段相结合。</td></tr><tr><td>随机脉冲干扰
WSF_RPJ_EFFECT</td><td>EA</td><td>随机脉冲干扰 EA。</td></tr><tr><td>重复脉冲干扰模型
WSF_REPEATER_EFFECT</td><td>EA</td><td>动态调整重复发送的脉冲信号强度来实施 EA。</td></tr><tr><td>简单假目标干扰模型
WSF_SIMPLEFT_EFFECT</td><td>EA</td><td>动态控制生成虚假目标，迷惑对方雷达实施 EA。</td></tr><tr><td>抑制旁瓣相消模型
WSF_SLC_DEGRADE_EFFECT</td><td>EA</td><td>通过干扰旁瓣相消器的频道，干扰敌方雷达或通信信号的处理能力，从而降低其精确度和可靠性。</td></tr></table>

![](images/9169f73f5320ccde3f66291b55c58fc08e9cac66429dc63f37f85261cc702dec.jpg)  
EA/EP 模型继承关系

![](images/57a9168e43058e73e303673115b72193e88b5f0bb3ed11d306bf621d45ebf8ab.jpg)

# 3.5.5.10.1. 电子战效果聚合 Electronic Warfare Effect Aggregation

# 概述

在WS（F 战争模拟框架）中，电子战（EW）效果包括电子攻击效果（Electronic_Attack_Effects）和电子保护效果（Electronic_Protect_Effects），这些效果在发射器-接收器或发射器-目标-接收器的交互过程中应用。这些效果的行为由软件和用户可修改的输入定义。在这种交互中，首先应用未缓解的电子攻击（EA）效果，然后应用任何缓解的电子保护（EP）效果到电子攻击效果上。这个过程会重复，直到所有技术上的 EA 效果和缓解的 EP 效果都被应用并聚合成一个数据集，用于修改发射器-接收器或发射器-目标-接收器之间的交互。

# 电子攻击效果一致性

在交互计算中，干扰功率使用通用的 WSF 电磁计算进行计算。每个 EA效果都具有一个或多个一致性类型。在应用效果时，遇到的效果一致性类型会被汇总，所有 EW 效果计算结束时，干扰功率会根据应用效果时遇到的 EA效果一致性类型分为三种类型：非相干、非相干脉冲和相干。

效果一致性类型 Effect Coherency Types  

<table><tr><td>效果一致性类型</td><td>描述</td><td>干扰功率类型</td></tr><tr><td>无（None）</td><td>对于给定效果未指定一致性。假设为非相干。</td><td>噪声</td></tr><tr><td>噪声（Noise）</td><td>波形与发射和/或预期接收波形不相干。假设为连续噪声类型波形。</td><td>非相干</td></tr><tr><td>非相干脉冲（Non-Coherent Pulse）</td><td>波形是脉冲的，与发射和/或预期接收波形不相干。假设为脉冲噪声类型波形。</td><td>脉冲噪声</td></tr><tr><td>相干（Coherent）</td><td>波形与发射和/或预期接收波形相干。假设在最基本的意义上紧密代表信号。</td><td>相干</td></tr><tr><td>相干脉冲（Coherent-Pulse）</td><td>波形是脉冲的，与发射和/或预期接收波形相干。假设在最基本的意义上紧密代表脉冲信号。</td><td>相干</td></tr></table>

# 干扰功率类型 Jamming Power Types

<table><tr><td>干扰功率类型</td><td>描述</td><td>一致性类型</td></tr><tr><td>噪声（Noise）</td><td>干扰引发的功率对接收器表现为噪声功率。</td><td>无（None）和非相干（Non-Coherent）</td></tr><tr><td>脉冲噪声（Pulsed-Noise）</td><td>脉冲干扰功率对接收器表现为噪声。</td><td>非相干脉冲（Non-Coherent Pulse）</td></tr><tr><td>相干（Coherent）</td><td>相干（连续和/或脉冲）干扰功率对接收器表现为信号。</td><td>相干（Coherent）和相干脉冲（Coherent Pulse）</td></tr></table>

在大多数交互中，信号与干扰比（S/I）通过信号功率除以噪声功率、杂波功率和干扰机功率之和来计算。用于干扰的干扰机功率是噪声和脉冲（非相干）干扰机功率之和。

# 电子战效果交互变量 EW Effects Interaction Variables

在电子战效果中，为每种类型的干扰功率定义了特定的变量结构，以及单独的信号、跟踪和消息效果结构。以下表格总结了这两种结构及其相关变量：

干扰效果变量结构 Jamming Effects Variable Structure  

<table><tr><td>功率效果变量</td><td>描述</td><td>聚合</td><td>默认</td><td>修改效果</td></tr><tr><td>空白因子
Blanking Factor</td><td>干扰空白因子（例如，旁瓣空白器）。</td><td>乘法</td><td>1.0</td><td>WSF_SLB_EFFECT</td></tr><tr><td>取消因子
Cancellation Factor</td><td>干扰取消因子（例如，旁瓣取消器）。</td><td>最小值</td><td>1.0</td><td>WSF_SLC_EFFECT
WSF_SLC_DEGRADE_EFFECT</td></tr><tr><td>调制因子
Modulation Factor</td><td>干扰处理/调制类型因子，不是物理干扰功率因子。</td><td>乘法</td><td>1.0</td><td>WSF_POWER_EFFECT</td></tr><tr><td>干扰功率因子
Jamming Power Factor</td><td>物理干扰功率因子。</td><td>乘法</td><td>1.0</td><td>WSF_POWER_EFFECT
WSF_COVER_PULSE_EFFECT</td></tr><tr><td>J/X 因子
J/X Factor</td><td>具有干扰到信号/噪声依赖性的替代干扰处理/调制类型。</td><td>乘法</td><td>1.0</td><td>WSF_POWER_EFFECT</td></tr><tr><td>目标保护标志
Target Protection Flag</td><td>标志指定是否允许干扰功率与给定目标的接收器交互。</td><td>未定义布尔</td><td>未定义</td><td>electronic Warfare Effect</td></tr><tr><td>脉冲抑制因子
Pulse Suppression Factor</td><td>脉冲类型干扰抑制因子。</td><td>乘法</td><td>1.0</td><td>WSF_PULSESuppressPRESS_EFFECT</td></tr><tr><td>半径因子 Radius Factor</td><td>评估目标相对于干扰机位置的因子以应用用户输入因子。</td><td>乘法</td><td>1.0</td><td>WSF_RADIUS_EFFECT</td></tr><tr><td>重复器干扰因子
Repeater Jamming Factor</td><td>依赖于定义的重复器行为的物理干扰功率因子。</td><td>乘法</td><td>1.0</td><td>WSF_REPEATER_EFFECT</td></tr><tr><td>RPJ 因子
RPJ Factor</td><td>随机脉冲干扰因子。</td><td>乘法</td><td>1.0</td><td>WSF_RPJ_EFFECT</td></tr></table>

信号效果变量结构 Signal Effects Variable Structure  

<table><tr><td>信号效果变量</td><td>聚合</td><td>默认</td><td>修改效果</td></tr><tr><td>信号功率因子（Signal Power Factor）</td><td>乘法</td><td>1.0</td><td>WSF_POWER_EFFECT</td></tr><tr><td>接收器噪声功率因子（Receiver Noise Power Factor）</td><td>乘法</td><td>1.0</td><td>WSF_POWER_EFFECT</td></tr></table>

跟踪效果变量结构 Track Effects Variable Structure  

<table><tr><td>跟踪效果变量</td><td>描述</td><td>聚合</td><td>默认</td><td>修改效果</td></tr><tr><td>方位误差Azimuth Error</td><td>跟踪方位误差。</td><td>最大值(EA)/最小值(EP)</td><td>0.0</td><td>WSFTRACK_EFFECT</td></tr><tr><td>仰角误差Elevation Error</td><td>跟踪仰角误差。</td><td>最大值(EA)/最小值(EP)</td><td>0.0</td><td>WSFTRACK_EFFECT</td></tr><tr><td>距离误差Range Error</td><td>跟踪距离误差。</td><td>最大值(EA)/最小值(EP)</td><td>0.0</td><td>WSFTRACK_EFFECT</td></tr><tr><td>速度误差Velocity Error</td><td>跟踪速度误差。</td><td>最大值(EA)/最小值(EP)</td><td>0.0</td><td>WSFTRACK_EFFECT</td></tr><tr><td>跟踪丢失/保持标志 TrackDrop/MaintainFlag</td><td>跟踪丢失/保持标志。</td><td>未定义布尔</td><td>未定义</td><td>WSFTRACK_EFFECTWSF_SLB_EFFECT</td></tr></table>

消息效果变量结构 Message Effects Variable Structure  

<table><tr><td>消息效果变量</td><td>描述</td><td>聚合</td><td>默认</td><td>修改效果</td></tr><tr><td>比特错误率 Bit Error Rate, BER</td><td>通信设备使用的比特错误率。</td><td>最大值（EA）/最小值（EP）</td><td>0.0</td><td>WSFCOMM_EFFECT</td></tr><tr><td>消息丢失/保持标志Message Drop/Maintain Flag</td><td>消息丢失/保持标志。</td><td>BOOL</td><td>0.0</td><td>WSFCOMM_EFFECT</td></tr></table>

# 聚合类型 Aggregation Types

在电子战效果中，聚合类型用于将各个电子战效果值汇总为一个交互值，以便在目标检测、跟踪过程和/或消息中应用任何相关的电子战效果。所有聚合都在标准单位中进行（例如，在 dB 空间中，乘法等同于加法）。

<table><tr><td>聚合类型</td><td>描述</td></tr><tr><td>最大值（Maximum）</td><td>取交互值和当前效果值中的最大值作为交互值。</td></tr><tr><td>最小值（Minimum）</td><td>取交互值和当前效果值中的最小值作为交互值。</td></tr><tr><td>加法（Additive）</td><td>将交互值和当前效果值相加作为交互值。</td></tr><tr><td>乘法（Multiplicative）</td><td>将交互值和当前效果值相乘作为交互值。</td></tr><tr><td>布尔值（Boolean）</td><td>一个可以根据当前值和效果逻辑切换的真/假（即，两态）标志。</td></tr><tr><td>未定义布尔值</td><td>类似于布尔聚合类型，但除了真/假之外，还提供未定义状态（即，</td></tr><tr><td>(Undefined Boolean)</td><td>三态)。这种类型可以从未定义(其最常见的默认状态)切换到真/假(即,已定义),并根据当前值和效果逻辑在三种状态之间切换。</td></tr></table>

![](images/678e1a457ef53c539a6236a67c5102101cfef22c9b1b7a8e89ecee0403aec603.jpg)  
电子战交互流程图 EW Interaction Flowchart

# 3.5.5.10.2. 电子攻击 WSF_ELECTRONIC_ATTACK

```txt
electronic_warfare <type-name> WSF_ELECTRONIC_attack ... Electronic Warfare Commands ... ... Electronic Attack Technique Commands ... end_electronic_attack 
```

WSF_ELECTRONIC_ATTACK 类型定义

WSF_ELECTRONIC_ATTACK 类型为发射器定义了一种电子攻击（对抗措施）能力。电子攻击（EA） - 电子保护（EP）架构提供了定义 EA 和 EP 技术并评估这些技术相互作用的能力。允许定义多种 EA技术。

3.5.5.10.2.1. 电子攻击技术 WSF_EA_TECHNIQUE  
```txt
Defining a new type:  
electronic_warfare技术和name>WSF_EA_TECHNIQUE  
default_on  
mitigation_class_name <string-value>  
... Electronic Warfare Technique Commands ...  
end_electronic_warfare和技术 
```

```txt
Adding an instance of the base type inside an 'electronic_attack' block:  
    technique <name> [WSF_EA_TECHNIQUE]  
    default_on  
    mitigation_class_name <string-value>  
    ... Electronic Warfare Technique Commands ...  
    end_technique 
```

电子战技术（electronic_warfare_technique）提供了定义电子战技术及其相关电子战效果的能力。允许定义多种效果。

default_on

设置技术的行为为激活状态。否则，技术将保持不活跃状态，直到被命令激活。

mitigation_class <string-value>   
mitigation_class_name <string-value>

设 置 技 术 的 缓 解 类 别 名 称 。 用 于 将 电 子 攻 击 技 术 映 射 到 可 以 通 过mitigated_technique_classes 命令缓解它们的电子保护技术。

注意：当仅使用 mitigated_techniques 输入命令时，此输入是可选的。

3.5.5.10.3. 电子保护 WSF_ELECTRONIC_PROTECT  
```txt
electronic_warfare <name> WSF_ELECTRONIC_PROTECT ... Electronic Warfare Commands ... ... Electronic Protect Technique Commands ... end_electronic_attack 
```

WSF_ELECTRONIC_PROTECT 类型为接收器定义了一种电子保护（反对抗措施）能力。电子攻击（EA） - 电子保护（EP）架构提供了定义 EA和 EP 技术并评估这些技术相互作用的能力。允许定义多种技术。

3.5.5.10.3.1. 电子保护技术 WSF_EP_TECHNIQUE  
```txt
Defining a new type:  
electronic_warfare技术和technique <name> WSF_EP_TECHNIQUE  
default_on  
externally-controlled 
```

```txt
internally-controlled   
mitigated Techniques <ea-technique-name>   
<ea-technique-name>   
end_mitigatedTechniques   
mitigated_technique_classes> <ea-technique-class-name>   
... <ea-technique-class-name>   
end_mitigated_technique_classes>   
... Electronic Warfare Technique Commands ...   
end_electronic_warfare_technique   
# Adding an instance of the base type inside an 'electronic_protect' block:   
...   
techniqueWSF_EP_TECHNIQUE default_on mitigated Techniques <ea-technique-name>   
... <ea-technique-name>   
end_mitigated_techniques mitigated_technique_classes> <ea-technique-class-name>   
... <ea-technique-class-name>   
end_mitigated_technique_classes>   
... Electronic Warfare Technique Commands ...   
end_technique 
```

电子战技术（electronic_warfare_technique）提供了定义电子战技术及其相关电子战效果的能力。允许定义多种效果。

default_on

设置技术的行为为激活状态。否则，技术将保持不活跃状态，直到被命令激活。

externally_controlled

指定禁止技术的自动内部使用，仅允许外部（即脚本或命令）控制。这一操作不是应用EP 技术的默认方式，并且会被 default_on 覆盖。

internally_controlled

指定允许技术的自动内部使用，任何外部控制可能会被覆盖。如果需要使用该技术，此操作会将 default_on 值修改为开启状态，这是应用 EP 技术的默认方法。

mitigated_techniques <ea-technique-name> … <ea-technique-name> …

end_mitigated_techniques

定义此 EP 技术可以尝试缓解的 EA技术。

▫ <ea-technique-name>: 要尝试缓解的 EA 技术名称的字符串输入。可以输入多个技术名称以对应多种技术。

注意：此输入是 mitigated_technique_classes 的替代或补充。

mitigated_technique_classes <ea-technique-class-name> … <ea-technique-class-name> … end_mitigated_technique_classes

定义此 EP 技术可以尝试缓解的 EA技术类别。

□ <ea-technique-class-name>: 要尝试缓解的 EA 技术的 mitigation_class_name 的字符串输入。可以输入多个类别名称以对应多种类别。

注意：此输入是 mitigated_techniques 的替代或补充。

# 3.5.5.10.4. 电子战效应模型 electronic_warfare_effect

```txt
#Defining a new type:   
electronic Warfare Effect <name> <type-name> debug target_protection_type ... allowed_target_set ... rejected_target_set end_electronic Warfare-effect   
#Adding or editing an instance inside an 'electronic Warfare_technique' or 'technique' block:   
effect [<type-name>] debug target_protection_type ... allowed_target_set ... rejected_target_set end-effect 
```

□ <name>: 要创建的电子战效果类型或实例的名称。  
□ <type-name>: 现有或预定义的电子战效果类型的名称，其定义将用作新类型或实例的初始定义。

电子战效果（electronic_warfare_effect）提供了定义与特定电子战技术相关的效果的能力。允许定义多种效果。

debug

指定使用调试模式将调试数据输出到标准输出。

默认值为 false 或 off

target_protection_type <target-protection-type>

指定用于 EA效果的目标保护类型。根据指定的目标保护类型设置干扰功率。

□ <target-protection-type>: 定义要应用的目标保护类型的字符串输入，有效值如下：

“all_targets”: 默认值。所有目标都将被允许并受到保护。如果定义了此项，则

会同时检查 rejected_target_list 和 allowed_target_set（如果设置）。

“self_protect”: 只有拥有发射器的干扰目标将受到此效果的保护。  
“non_self_protect”: 只有干扰平台以外的其他目标将受到此效果的保护。

注意：目标允许/拒绝的优先顺序如下：target_protection_type $- >$ rejected_target_list->allowed_target_list。第一个失败（即拒绝目标并不允许效果）的将导致下一个不被评估。

allowed_target_set … end_allowed_target_set

指定 EA效果将应用的允许目标集，所有其他目标的干扰功率将设置为 0.0 瓦。

rejected_target_set … end_rejected_target_set

指定 EA效果不应用的拒绝目标集，其干扰功率将设置为 0.0 瓦。所有其他目标将被允许

# 3.5.5.10.4.1. 频率捷变模型 WSF_AGILITY_EFFECT

# 3.5.5.10.4.2. 雷达频率捷变模型 WSF_RADAR_AGILITY_EFFECT

```txt
effect <effect-name> WSF_AGILITY_EFFECT Base Effect Commands agility_type ... end_agiltiy_type end-effect 
```

WSF_AGILITY_EFFECT 是一种基础效果类型，可以包含在电子保护技术块中，作为给定技术的多种可用效果之一。此效果类型的基本命令可以在效果块中指定，以增强电子战系统的灵活性和适应性。

debug

设置此效果的调试模式。

agility_type <agility-type> … end_agility_type

输入块，用于提供此效果的灵活性类型及其相关输入命令。当通信系统或雷达传感器感知到干扰时，应用指定的灵活性类型。为了使此效果正常工作，雷达传感器的jamming_perception_threshold 和 jamming_perception_timeout 或 通 信 的jamming_perception_threshold 和 jamming_perception_timeout 应该被正确定义。

可用的灵活性类型

frequency_changing

提供在雷达传感器的 mode_select_delay 或通信的 frequency_select_delay 约束内更改到不同备用频率的能力。

注意：如果此效果在 WSF_RADAR_SENSOR 类型上作为电子保护定义，则传感器将被视为频率灵活（脉冲到脉冲），前提是此效果被定义为 frequency_changing 且发射器上定义了备用频率，并且设置了干扰感知阈值。

mode_changing

提供在 mode_select_delay 约束内更改到不同雷达模式的能力。

```txt
agility_type mode-changing mode_name 1 <mode-name-1> 
```

```txt
mode_name 2 <mode-name-2>  
...  
mode_name N <mode-name-N>  
end_agility_type 
```

□ <mode-name-n> 指定将按顺序应用的模式名称。

频率灵活性在电子战中的应用

频率灵活性是一种有效的技术，用于对抗来自干扰源的信号，并支持这些系统的有效操作。例如，主动电子扫描阵列（AESA）系统可以通过频率灵活性来支持雷达、电子战和通信功能。通过采用频率灵活性，雷达系统可以在复杂的射频环境中对抗干扰效果。

这种灵活性允许系统在检测到干扰时快速切换频率或模式，从而提高系统的生存能力和操作效率。这在现代电子战中尤为重要，因为敌方可能使用多种干扰技术来削弱或破坏通信和探测能力。

3.5.5.10.4.3. 通信模型 WSF_COMM_EFFECT  
```txt
effect <effect-name> WSFCOMM_EFFECT ... Base Effect Commands ... bit_error_rate <real-value> message_behavior ... end-effect 
```

WSF_COMM_EFFECT 是一种基础效果类型，可以包含在电子攻击和/或电子保护技术块中，作为给定技术的多种可用效果之一。此效果类型的基本命令可以在效果块中指定，以影响通信系统的性能。

# 基本命令

bit_error_rate <real-value>

指定要应用的比特错误率（BER）。可以用于引入或缓解错误。自动将 message_behavior设置为失真。

默认值：0.0

message_behavior <behavior-type> … end_message_behavior

输入块，用于提供此通信效果表现的行为类型。

# 可用的行为类型

```txt
- maintain
- 保持消息完整。
- drop
- 丢弃消息。
- distort
```

通过比特错误率失真消息。此行为类型由 bit_error_rate 自动设置。

应用场景

在电子战中，通信系统可能会受到干扰，导致信息传输的完整性和有效性受到影响。通过使用 WSF_COMM_EFFECT，可以模拟或对抗这些干扰效果。例如：

引入干扰：通过设置较高的比特错误率，可以模拟敌方干扰对通信系统的影响，导致消息失真或丢失。

缓解干扰：通过调整比特错误率和消息行为，可以优化通信系统的抗干扰能力，确保在复杂电磁环境中的可靠通信。

这种效果类型在电子战模拟和训练中非常有用，帮助操作人员理解和应对不同的干扰情境。通过调整这些参数，电子战系统可以优化其对抗干扰的能力，确保在复杂的电磁环境中维持通信的完整性和有效性。

# 3.5.5.10.4.4. 功率模型 WSF_POWER_EFFECT

# 3.5.5.10.4.5. 干扰功率模型 WSF_JAMMER_POWER_EFFECT

```txt
effect <effect-name> WSF_POWER_EFFECT  
    electronic Warfare-effect Commands  
    WSF_REPEATER_EFFECT Commands  
    WSF_RADIUS_EFFECT Commands  
    jamming_modulation_gain <db-ratio-value>  
    jamming_power_gain <db-ratio-value>  
    jamming_to_signal_gain_table ... end_jamming_to_signal_gain_table  
    signal_power_gain <db-ratio-value>  
    receiver_noise_power_gain <db-ratio-value>  
    system_type_data <system-type-name> ... end_system_type_data  
    end-effect 
```

WSF_POWER_EFFECT 是一种基础效果类型，可以包含在电子保护或电子攻击技术块中，作为给定技术的多种可用效果之一。此效果类型的基本命令可以在效果块中指定，以调整干扰和信号功率的水平。

# 基本命令

jamming_modulation_gain <db-ratio-value>

指定对由此技术创建的有效干扰增益水平的调整。此调整修改通常确定的处理干扰功率。如果此输入在 system_type_data 输入块中指定，则它特定于系统类型，否则此输入被定义为未定义系统类型的“默认”数据。

默认值：0.0 dB

jamming_power_gain <db-ratio-value>

指定对由此技术创建的有效干扰功率水平的调整。此调整修改通常确定的物理干扰功率。

默认值：0.0 dB

jamming_to_signal_gain_table … end_jamming_to_signal_gain_table

定义一个依赖于 J/S 比率的增益因子，其中 J 是干扰功率，S 是接收器中的信号功率。使用线性插值来推导中间 J/S 比率的值。J/S 值超出表的范围时，使用适当端点的值（即，不进行外推）。

```html
jamming_to_signal_gain_table jamming_to_signal<j_to_s-value-1><gain-value-1> jamming_to_signal<j_to_s-value-2><gain-value-2> ... jamming_to_signal<j_to_s-value-n><gain-value-n> end_jamming_to_signal_gain_table 
```

规则：

□ 条目必须按 J/S 值单调递增排序。  
▫ 必须至少有两个条目。

signal_power_gain <db-ratio-value>

指定对由此技术创建的有效信号水平的调整。此调整修改通常确定的接收信号功率。

默认值：0.0 dB

receiver_noise_power_gain <db-ratio-value>

指定对由此技术创建的有效接收器噪声功率水平的调整。此调整通过乘数应用于信噪比计算。

默认值：0.0 dB

system_type_data <system-type-name> … end_system_type_data

输入块，用于提供实现此技术所需的系统类型（例如，SENSOR-TYPE,JAMMER-TYPE）特定数据。可以为未定义的系统类型设置默认数据，使用“default”字符串作为系统类型。

示例：

```c
system_type_data <system-type-name> WSF_REPEATER_EFFECT Commands WSF_RADIUS_EFFECT Commands jamming_modulation_gain <db-ratio> jamming_power_gain <db-ratio> signal_power_gain <db-ratio> receiver_noise_power_gain <db-ratio> end_system_type_data 
```

# 应用场景

在 电 子 战 中 ， 调 整 干 扰 和 信 号 功 率 是 优 化 系 统 性 能 的 关 键 。 通 过 使 用WSF_POWER_EFFECT，可以模拟或对抗干扰效果。例如：

干扰增强：通过增加干扰功率增益，可以提高干扰信号的有效性，从而更有效地阻止敌方通信或雷达。

信号增强：通过调整信号功率增益，可以提高接收信号的强度，增强系统在干扰环境中的生存能力。

这些调整在电子战模拟和训练中非常有用，帮助操作人员理解和应对不同的干扰情境。通过调整这些参数，电子战系统可以优化其对抗干扰的能力，确保在复杂的电磁环境中维持通信和探测的完整性和有效性。

# 3.5.5.10.4.6. 脉冲密度模型 WSF_PULSE_EFFECT

```txt
effect <effect-name> WSF_PULSE_EFFECT electronic_warfare-effect Commands WSF_POWER_EFFECT Commands WSF_REPEATER_EFFECT Commands WSF_RADIUS_EFFECT Commands jamming_pulse_density <value> end-effect 
```

WSF_PULSE_EFFECT 是一种基础效果类型，可以包含在电子保护或电子攻击技术块中，作为给定技术的多种可用效果之一。此效果类型的基本命令可以在效果块中指定，以调整干扰信号的脉冲密度。

# 基本命令

jamming_pulse_density <value>

指定用于此雷达类型的干扰信号的脉冲密度，范围为 [0,1]。此输入仅用于电子攻击（Electronic Attack）效果。

默认值：0.1

# 应用场景

在电子战中，脉冲密度是一个关键参数，影响干扰信号的有效性。通过调整脉冲密度，可以控制干扰信号的强度和覆盖范围，从而优化对敌方雷达和通信系统的干扰效果。例如：

高脉冲密度：可以用于集中干扰特定频率或目标，增加干扰信号的强度。

低脉冲密度：可以用于广泛覆盖多个频率或目标，减少被检测的可能性。

这种效果类型在电子战模拟和训练中非常有用，帮助操作人员理解和应对不同的干扰情境。通过调整这些参数，电子战系统可以优化其对抗干扰的能力，确保在复杂的电磁环境中维持通信和探测的完整性和有效性。

# 相关技术

根据搜索结果，电子战系统通常结合多种技术来增强其干扰能力。例如，BAESystems 的数字电子战系统（DEWS）集成了雷达警告、干扰响应和先进的电子对抗措施，以在复杂的电磁战场中占据优势。此外，干扰技术包括噪声技术和重复技术，后者通过操纵接收到的雷达能量并重新传输来改变雷达的检测结果。这些技术的结合使得电子战系统能够有效地对抗和中和敌方的雷达和通信威胁。

# 3.5.5.10.4.7. 脉冲抑制模型 WSF_PULSE_SUPPRESS_EFFECT

```txt
… 
```

```txt
effect <effect-name> WSF_PULSEsuppressRESS_EFFECT  
    electronic Warfare-effect Commands  
    WSF_PULSE_EFFECT Commands  
    reject <sup> suppression-type-value> <sup> suppression-type> <lower-suppression-value>  
    allow <sup> suppression-type-value> <sup> suppression-type> <lower-suppression-value>  
    <upper-suppression-value>  
end Effect 
```

WSF_PULSE_SUPPRESS_EFFECT 是一种基础效果类型，可以包含在电子保护或电子攻击技术块中，作为给定技术的多种可用效果之一。此效果类型的基本命令可以在效果块中指定，以控制干扰信号的脉冲特性。

# 基本命令

reject <suppression-type> <lower-suppression-value> <upper-suppression-value>

指定要拒绝的抑制类型及其所需的输入变量，这些变量依赖于指定的抑制类型。

allow <suppression-type> <lower-suppression-value> <upper-suppression-value>

指定要允许的抑制类型及其所需的输入变量，这些变量依赖于指定的抑制类型。

可用的抑制类型  

<table><tr><td>&lt;suppression-type&gt;</td><td>描述</td><td>&lt;lower-suppression-value&gt;</td><td>&lt;upper-suppression-value&gt;</td></tr><tr><td>frequency</td><td>应用脉冲频率抑制,允许或拒绝在限制范围内的频率。</td><td>下限频率: &lt;frequency-value&gt;</td><td>上限频率: &lt;frequency-value&gt;</td></tr><tr><td>pulse_width</td><td>应用脉冲宽度(PW)抑制,允许或拒绝在限制范围内的脉冲宽度。</td><td>下限 PW : &lt;time-value&gt;</td><td>上限 PW : &lt;time-value&gt;</td></tr><tr><td>pulse_repetition-frequency</td><td>应用脉冲重复频率(PRF)抑制,允许或拒绝在限制范围内的 PRF。</td><td>下限 PRF : &lt;frequency-value&gt;</td><td>上限 PRF : &lt;frequency-value&gt;</td></tr><tr><td>modulation</td><td>应用脉冲调制抑制,允许或拒绝指定调制类型,并将指定比例应用于功率。</td><td>Modulation type :指定调制类型(详见下方调制类型)。</td><td>Rejection ratio [0,1]:拒绝比例,范围为0到1。</td></tr><tr><td>coherent</td><td>应用相干脉冲抑制,允许或拒绝指定比例的相干脉冲功率。</td><td>Power rejection ratio [0,1]:功率拒绝比例,范围为0到1。</td><td>N/A</td></tr><tr><td>noncoherent</td><td>应用非相干脉冲抑制,允许或拒绝指定比例的非相干脉冲功率。</td><td>Power rejection ratio [0,1]:功率拒绝比例,范</td><td>N/A</td></tr><tr><td></td><td></td><td>围为0到1。</td><td></td></tr><tr><td>percent_of_pulses</td><td>应用脉冲百分比抑制，允许或拒绝指定比例的脉冲，对于WSFFalse_TARGET_EFFECT，这是假目标的比例而不是脉冲。</td><td>Pulse rejection ratio &lt;value&gt; [0,1]:脉冲拒绝比例，范围为0到1。</td><td>N/A</td></tr></table>

```txt
<modulation-type> 
```

指定调制类型。可用的调制类型如下：

□ continuous_wave / cw - 连续波   
□ coherent_pulse - 相干脉冲  
□ non_coherent_pulse - 非相干脉冲   
□ linear_fm - 线性频率   
□ non_linear_fm - 非线性频率   
□ phase_key - 相位键（通用键）  
□ phase_modulation - 相位调制（通用调制）  
□ phase_coding - 相位编码（通用编码）  
▫ ask - 振幅键控   
▫ fsk - 频率键控   
□ psk - 相位键控  
□ bpsk- 二进制相位键控  
□ dpsk- 差分相位键控   
□ qpsk- 正交相位键控  
□ qam- 正交振幅调制

# 3.5.5.10.4.8. 旁瓣消隐 WSF_SLB_EFFECT

```txt
effect <effect-name> WSF_SLB_EFFECT  
electronic_warfare-effect Commands  
WSF_POWER_EFFECT Commands  
auxiliary.antenna_pattern <pattern-name>  
auxiliary_beam_tilt <angle-value>  
blanking_threshold <dbratio-value>  
main_jnr_thresholds <min-db-ratio> <max-db-ratio>  
auxiliary_jnr_thresholds <min-db-ratio> <max-db-ratio>  
saturation Effect ... end_saturation-effect  
target_blanking-effect ... end_target_blanking-effect  
# Optional Inputs - uses main channel antenna and/or receiver parameters if not specified. Antenna Commands ...  
receiver  
... receiver commands ...  
end_receiver  
end-effect 
```

auxiliary_antenna_pattern <pattern-name>

功能：指定要使用的天线模式名称。

注意：此天线模式将成为唯一和默认的天线模式，并会覆盖接收器的天线模式。

auxiliary_beam_tilt <angle-value>

功能：指定辅助接收器的波束倾斜角度。

默认值：如果未定义，默认使用附加效果的接收器的波束倾斜。

blanking_threshold <dbratio-value>

功能：指定信号将被屏蔽的阈值水平。当（辅助接收器通道）/（主通道功率） $> =$ blanking_threshold 时，信号将被屏蔽。

默认值：0.0 dB

main_jnr_thresholds <min-db-ratio> <max-db-ratio>

功能：指定主通道 JNR 阈值的下限和上限，SLB 将在这些水平下操作输入的干扰信号。

默认值：感知接收器定义的主接收器 SNR 阈值为下限，较大的值为上限。

auxiliary_jnr_thresholds <min-db-ratio> <max-db-ratio>

功能：指定辅助通道 JNR 阈值的下限和上限，SLB 将在这些水平下操作输入的干扰信号。

默认值：与主通道相同。

# 饱和效果

saturation_effect <saturation-type> … end_saturation_effect

功能：提供饱和效果及其相关输入命令的输入块。

□ <saturation-type>

可用类型：

□ no_saturation_effect：不应用饱和效果。  
□ duty_cycle_limit_effect：应用占空比饱和效果。

duty_cycle_limit <value>

功能：指定输入干扰信号的最大占空比，超过此值的信号将不被屏蔽。

有效值范围：0 到 1

默认值：1.0

# 目标屏蔽效果

target_blanking_effect <target-blanking-type> … end_target_blanking_effect

功能：提供目标屏蔽效果及其相关输入命令的输入块。

□ <target-blanking-type>可用类型：  
□ no_target_blanking_effect：不应用目标屏蔽效果。  
▫ duty_cycle_probability_effect：使用概率抽取和比较输入信号的占空比进行目标屏蔽。

probabilities … end_probabilities

功能：提供目标屏蔽概率表效果及其相关输入命令的输入块。

pulse_density <pulse-density> <probability-value>   
duty_cycle <duty-cycle> <probability-value>

功能：指定接收到的脉冲密度或干扰信号的占空比的目标屏蔽概率。多个条目创建一个

查找表。

3.5.5.10.4.9. 旁瓣相消 WSF_SLC_EFFECT   
```txt
effect <effect-name> WSF_SLC_EFFECT  
electronic_warfare-effect Commands  
WSF_POWER_EFFECT Commands  
auxiliary.antenna_pattern <pattern-name>  
auxiliary_beam_tilt <angle-value>  
number_of_cancellation_channels <integer-value>  
cancellation_lock_ratio <bratio-value>  
main_jnr_thresholds <min-db-ratio-value> <max-db-ratio-value>  
auxiliary_jnr_thresholds <min-db-ratio-value> <max-db-ratio-value>  
cancellation_ratio <bratio-value>  
saturation_ratio <bratio-value>  
cancellation RATios ... end_cancellation RATios  
# Optional Inputs - uses main channel antenna and/or receiver parameters if not specified. Antenna Commands ...  
receiver  
... receiver commands ...  
end_receiver  
end Effect 
```

auxiliary_antenna_pattern <pattern-name>

功能：指定要使用的天线模式名称。

注意：此天线模式将成为唯一和默认的天线模式，并会覆盖接收器的天线模式。

auxiliary_beam_tilt <angle-value>

功能：指定辅助接收器的波束倾斜角度。

默认值：如果未定义，默认使用附加效果的接收器的波束倾斜。

number_of_canceler_channels <integer>

功能：指定取消器通道（即取消环路或取消器）的数量。

cancellation_lock_ratio <dbratio-value>

功能：指定信号将被取消的阈值水平。当（辅助接收器通道）/（主通道功率） $> =$ cancellation_lock_ratio 时，信号将被取消。

默认值：0.0 dB

minimum_pulsewidth <time-value>

功能：指定取消器能够操作的最小脉冲宽度。

minimum_cancelled_pulsewidth <time-value>

功能：指定取消器能够操作的最小被取消脉冲宽度。

默认值：0.0 秒

canceller_settling_time <time-value>

功能：指定取消器环路的稳定时间。

注 意 ： 如 果 (1 / pol_mod_switch) < canceller_settling_time ， 则number_slc_channels_saturated 设置为 1，slc_degradation_factor 设置为 1.0，因为取消器

环路可以锁定在极化调制效果上。

默认值：0.0 秒

main_jnr_thresholds <min-db-ratio-value> <max-db-ratio-value>

功能：指定主通道 JNR 阈值的下限和上限，SLC 将在这些水平下操作输入的干扰信号。

默认值：0.0 dB

auxiliary_jnr_thresholds <min-db-ratio-value> <max-db-ratio-value>

功能：指定辅助通道 JNR 阈值的下限和上限，SLC 将在这些水平下操作输入的干扰信号。

默认值：0.0 dB

cancellation_ratio <dbratio-value>

功能：指定当干扰器数量小于或等于 number_of_canceler_channels 时，应用于干扰信号的稳态取消比。

saturation_ratio <dbratio-value>

功能：指定当干扰器数量大于 number_of_canceler_channels 时，应用于干扰信号的稳态取消比。

默认值：如果单独输入 cancellation_ratio，则为其值；如果输入表格，则为 0.0dB。

cancellation_ratios … end_cancellation_ratios

在 WSF_SLC_EFFECT 中，cancellation_ratios 命令允许定义不同依赖关系的取消比率。以下是如何定义这些比率的详细说明：

□ Nondependent (非依赖)

定义：取消比率不依赖于任何其他参数。

示例：

```txt
cancellation_ratio cancellation_ratio saturation_ratio | saturation end_cancellation_ratio 
```

□ Jammer-to-Noise-Dependent (干扰信号与噪声比依赖)

定义：取消比率依赖于干扰信号与噪声比（JNR）。

示例：

```txt
cancellation_ratios jammer_to_noise <db-ratio-value-1> <db-cancellation-ratio-1> jammer_to_noise <db-ratio-value-2> <db-cancellation-ratio-2> ... jammer_to_noise <db-ratio-n> <db-cancellation-ratio-3> saturation_ratio | saturation end_cancellation_ratios 
```

□ Number-Jammers-Canceled-Dependent (被取消干扰器数量依赖)

定义：取消比率依赖于被取消的干扰器数量。

示例：

```txt
cancellation_ratio  
number_canceled_jammers <integer-1>  
cancellation_ratio <db-ratio-value>  
number_canceled_jammers <integer-2>  
cancellation_ratio <db-ratio-value> 
```

```txt
...  
number_canceled_jammers <integer-n>  
cancellation_ratio <db-ratio-value>  
saturation_ratio | saturation  
end_cancellation_ratios 
```

□ Number-Canceled-Jammers and Jammer-to-Noise-Dependent (被取消干扰器数量与 干扰信号与噪声比依赖)

定义：取消比率同时依赖于被取消的干扰器数量和干扰信号与噪声比。

示例：

```txt
cancellation_ratioss   
number_canceled_jammers integer-1> jammer_to_noise <db-ratio-value-1> <db-cancellation-ratio-1> jammer_to_noise <db-ratio-value-2> <db-cancellation-ratio-2> ... jammer_to_noise <db-ratio-n> <db-cancellation-ratio-3>   
number_canceled_jammers integer-2> jammer_to_noise <db-ratio-value-1> <db-cancellation-ratio-1> jammer_to_noise <db-ratio-value-2> <db-cancellation-ratio-2> ... jammer_to_noise <db-ratio-value-n> <db-cancellation-ratio-3> ... saturation_ratio | saturation   
end_cancellation_ratioss 
```

□ Jammer-Canceled-Dependent (干扰器被取消依赖)

定义：取消比率依赖于特定的干扰器被取消。

示例：

```txt
cancellation_ratio  
jammer_canceled <integer-1>  
cancellation_ratio <db-ratio-value>  
jammer_canceled <integer-2>  
cancellation_ratio <db-ratio-value>  
...  
saturation_ratio | saturation  
end_cancellation_ratio 
```

□ Jammer-Canceled and Jammer-to-Noise-Dependent (干扰器被取消与干扰信号与噪 声比依赖)

定义：取消比率同时依赖于特定的干扰器被取消和干扰信号与噪声比。

示例：

```txt
cancellation_ratios  
jammer_canceled <integer-1>  
jammer_to_noise <db-ratio-value-1> <db-cancellation-ratio-1>  
jammer_to_noise <db-ratio-value-2> <db-cancellation-ratio-2>  
...  
jammer_to_noise <db-ratio-value-n> <db-cancellation-ratio-3> 
```

```txt
jammer_canceled <integer-2>  
jammer_to_noise <db-ratio-value-1> <db-cancellation-ratio-1>  
jammer_to_noise <db-ratio-value-2> <db-cancellation-ratio-2>  
...  
jammer_to_noise <db-ratio-value-n> <db-cancellation-ratio-3>  
...  
saturation_ratio | saturation  
end_cancellation_ratios 
```

饱和比率

□ saturation <db-ratio>

功能：定义非依赖或干扰信号与噪声比依赖的饱和取消比率。

非依赖示例：

```txt
saturation saturation_ratio | cancellation_ratio <db-ratio> 
```

干扰信号与噪声比依赖示例：

```txt
saturation jammer_to_noise <db-ratio-value-1> <db-cancellation-ratio-1> jammer_to_noise <db-ratio-value-2> <db-cancellation-ratio-2> ... jammer_to_noise <db-ratio-value-n> <db-cancellation-ratio-3> 
```

# 3.5.5.10.4.10. 跟踪模型 WSF_TRACK_EFFECT

```txt
effect <effect-name> WSFTRACK_EFFECT electronic Warfare-effect Commands WSF_PULSE_EFFECT Commands WSF_REPEATER_EFFECT Commands WSF_POWER_EFFECT Commands WSF_RADIUS_EFFECT Commands track_behavior <behavior-type> required_j_to_s <dbratio-value> range_error <length-value> azimuth_error <angle-value> elevation_error <angle-value> velocity_error <speed-value> range_walkoff_rate <speed-value> azimuth_walkoff_rate <angular-rate> elevation_walkoff_rate <angular-rate> velocity_walkoff_rate <acceleration-value> range_holdout <length-value> range_holdout_time <time-value> azimuth_holdout <angle-value> 
```

```txt
azimuth_holdout_time <time-value> elevation_holdout <angle-value> elevation_holdout_time <time-value> velocity_holdout <speed-value> velocity_holdout_time <time-value> range_recycle <boolean-value> azimuth_recycle <boolean-value> elevation_recycle <boolean-value> velocity_recycle <boolean-value> delay_table ... end_delay_table holdout_table ... end_holdout_table recycle_table ... end_recycle_table system_type_data <system-type-name> ... end_system_type_data end-effect 
```

track_behavior <behavior-type> 设置技术的缓解跟踪行为。

▫ maintain- 如果当前未丢失，则对跟踪没有影响。如果当前已丢失，将更改为有效。  
□ drop - 导致跟踪丢失（可能与 EP 技术无关）。  
▫ distort- 引入跟踪误差（如果需要缓解 EA技术引入的误差）。

required_j_to_s <dbratio-value> 指定有效性所需的最小 J/S 比率。

默认值：3dB

range_error <length-value> 指定此技术引入的距离误差或缓解误差。

默认值：0.0

azimuth_error <angle-value> 指定此技术引入的方位误差或缓解误差。

默认值：0.0

elevation_error <angle-value> 指定此技术引入的仰角误差或缓解误差。

默认值：0.0

velocity_error <speed-value> 指定此技术引入的速度误差或缓解误差。

默认值：0.0

range_walkoff_rate <speed-value> 指定此技术引入的距离误差的线性变化率。

默认值：0.0

azimuth_walkoff_rate <angular-rate> 指定此技术引入的方位误差的线性变化率。

默认值：0.0

elevation_walkoff_rate <angular-rate> 指定此技术引入的仰角误差的线性变化率。

默认值：0.0

velocity_walkoff_rate <acceleration-value> 指定此技术引入的速度误差的线性变化率。

默认值：0.0

range_holdout <length-value> 指定此技 术引入的距离 误差偏移的上限 。可以作为range_holdout_time 的替代，并将覆盖之前指定的任何 range_holdout_time。

默认值：无

range_holdout_time <time-value> 指 定 每 个 距 离 偏 移 周 期 的 时 间 。 可 以 作 为range_holdout 的替代，并将覆盖之前指定的任何 range_holdout。

默认值：无

azimuth_holdout <angle-value> 指定此技术引入的方位误差偏移的上限。可以作为azimuth_holdout_time 的替代，并将覆盖之前指定的任何 azimuth_holdout_time。

默认值：无

azimuth_holdout_time <time-value> 指 定 每 个 方 位 偏 移 周 期 的 时 间 。 可 以 作 为azimuth_holdout 的替代，并将覆盖之前指定的任何 azimuth_holdout。

默认值：无

elevation_holdout <angle-value> 指定此技术引入的仰角误差偏移的上限。可以作为elevation_holdout_time 的替代，并将覆盖之前指定的任何 elevation_holdout_time。

默认值：无

elevation_holdout_time <time-value> 指 定 每 个 仰 角 偏 移 周 期 的 时 间 。 可 以 作 为elevation_holdout 的替代，并将覆盖之前指定的任何 elevation_holdout。

默认值：无

velocity_holdout <speed-value> 指定此技术引入的速度误差偏移的上限。可以作为velocity_holdout_time 的替代，并将覆盖之前指定的任何 velocity_holdout_time。

默认值：无

velocity_holdout_time <time-value> 指 定 每 个 速 度 偏 移 周 期 的 时 间 。 可 以 作 为velocity_holdout 的替代，并将覆盖之前指定的任何 velocity_holdout。

默认值：无

range_recycle <boolean-value> 指定偏移是否应循环回最小距离误差或保持在偏移。仅在给定 range_holdout 或 range_holdout_time 时使用。

默认值：False

azimuth_recycle <boolean-value> 指定偏移是否应循环回最小方位误差或保持在偏移。仅在给定 azimuth_holdout 或 azimuth_holdout_time 时使用。

默认值：False

elevation_recycle <boolean-value> 指定偏移是否应循环回最小仰角误差或保持在偏移。仅在给定 elevation_holdout 或 elevation_holdout_time 时使用。

默认值：False

velocity_recycle <boolean-value> 指定偏移是否应循环回最小速度误差或保持在偏移。仅在给定 velocity_holdout 或 velocity_holdout_time 时使用。

默认值：False

delay_table … end_delay_table holdout_table … end_holdout_table recycle_tableend_recycle_table 此命令提供定义延迟、偏移或回收时间因子的手段，这些因子依赖于J/S 比率，其中 J 是干扰功率，S 是接收器中的信号功率。如果输入的范围具有非零增量，则在指定范围内执行均匀随机数抽取。线性插值用于在随机抽取之前推导中间 J/S 比率的值。超出表格范围的 J/S 值使用适当端点的值（即不进行外推）。如果此输入在system_type_data输入块中指定，则它特定于系统类型，否则此输入被定义为未定义系统类型使用的“默认”数据。

表格格式为：

```txt
<type>_table
    jamming_to_signal <j_to_s-value-1> <min-time-value-1> <max-time-value-1>
    jamming_to_signal <j_to_s-value-2> <min-time-value-2> <max-time-value-2>
    ... 
```

```txt
jamming_to_signal <j_to_s-value-n> <min-time-value-n> <max-time-value-n> end_type>_table 
```

必须遵循以下规则：

条目必须按 J/S 值单调递增排序。

必须至少有两个条目。

system_type_data <system-type-name> … end_system_type_data 输入块提供特定于系统类型（例如，SENSOR-TYPE, JAMMER-TYPE）的数据，以便为给定系统类型实现此技术。可以为未定义的系统类型设置默认数据，使用“default”字符串作为系统类型。如果未定义，则对给定系统类型不应用任何效果。

<system-type-name> 一个字符串输入，表示以下数据适用的系统类型，有效值为[system-type-name | “default”]。默认数据用于未指定的系统类型，如果未定义，则对给定系统类型不应用任何效果。

# 3.5.5.10.4.11. 扩展旁瓣消隐 WSF_NX_SLB_EFFECT

```txt
effect <effect-name> WSF_SLB_EFFECT electronic Warfare-effect Commands WSF_POWER_EFFECT Commands ... WSF_SLB_EFFECT Commands ... target_blanking-effect ... end_target_blanking-effect end-effect 
```

WSF_NX_SLB_EFFECT 是一种电子战效果类型，可以在电子保护（electronic_protect）或电子攻击（electronic_attack）技术块中使用。它是预定义的电子战效果类型之一，提供了一种基于检测到的每个干扰脉冲的范围单元空白数量的算法计算效果。

功能与作用

目标空白效果（target_blanking_effect）：此效果类型扩展了基础的 WSF_SLB_EFFECT 的目标空白效果，增加了一个算法计算效果。该算法基于每个干扰脉冲检测到的范围单元空白数量进行计算。

target_blanking_effect <target-blanking-type> … end_target_blanking_effect：这是一个输入块，用于提供饱和效果及其相关的输入命令。可以使用的目标空白效果包括基础目标空白效果以及：

cell_blanking_probability_effect ： 概 率 是 使 用 在 系 统 中 指 定 的‘number_of_cells_blanked’ 的 N 个 单 元 的 累 积 概 率 计 算 的 。 公 式 如 下 ：???????????????= ?=1 ??????_?????_???????   ???????_????_?????×(1−???????????????(?−1))  
□ number_cells_blanked <integer-value>：指定每个触发空白的干扰脉冲空白的连续范围/速度单元数量，从[1,N]。默认值为 1。

# 3.5.5.10.4.12. 脉冲覆盖模型 WSF_COVER_PULSE_EFFECT

```txt
effect <effect-name> WSF_COVER_PULSE_EFFECT ... Base Effect Commands ... 
```

```c
... WSF_PULSE_EFFECT Commands ...
... WSF_POWER_EFFECT Commands ...
... WSF_REPEATER_EFFECT Commands ...
... WSF_RADIUS_EFFECT Commands ...
probability_of_coverage <value>
required_j_to_s <db-ratio-value>
system_type_data <system-type-name> ... end_system_type_data
end-effect 
```

WSF_COVER_PULSE_EFFECT 是 一 种 基 础 效 果 类 型 ， 可 以 包 含 在 电 子 保 护（electronic_protect）或电子攻击（electronic_attack）技术块中，作为给定技术的众多可用效果之一。该效果旨在增加覆盖目标回波的概率，并设定一个所需的干扰与信号（J/S）比率，以便该效果能够被应用。

# 主要功能

覆盖概率（probability_of_cover）：指定覆盖脉冲覆盖目标回波的概率，范围在 [0.0, 1.0]之间。进行概率抽取，如果抽取结果在此概率之外，则效果为 0.0。默认值为 1.0。

所需 J/S 比率（required_j_to_s）：指定效果生效所需的最小 J/S 比率。默认值为 3 dB。

# 使用场景

该效果可以与 WSF_PULSE_EFFECT 和 WSF_POWER_EFFECT 结合使用，以应用脉冲效果（例如，干扰脉冲密度）和功率增益效果。这种组合可以增强电子攻击或保护技术的有效性。

# 系统类型数据

通过 system_type_data <system-type-name> ... end_system_type_data 输入块，可以为特定系统类型（例如，传感器类型、干扰器类型）提供必要的数据，以实现该技术。对于未定义的系统类型，可以使用“default”字符串设置默认数据。

# 3.5.5.10.4.13. 假目标模型 WSF_FALSE_TARGET_EFFECT

```txt
effect <effect-name> WSFFalse_TARGET_EFFECT ... Base Effect Commands ... ... WSF_PULSE_EFFECT Commands ... ... WSF_REPEATER_EFFECT Commands ... ... WSF_POWER_EFFECT Commands ... ... WSF_RADIUS_EFFECT Commands ... ... false target definition ... 
```

```txt
false_target_name<string-value> jamming_pulse_density<real-value> number_of,false_targets<integer-value> scan_ratemultiplier<real-value> speeds<min-speed-value><max-speed-value> system_type_data<system-type-name>...end_system_type_data end-effect 
```

WSF_FALSE_TARGET_EFFECT 是 一 种 基 础 效 果 类 型 ， 可 以 包 含 在 电 子 保 护（electronic_protect）或电子攻击（electronic_attack）技术块中，作为给定技术的众多可用效果之一。该效果用于生成虚假目标，以迷惑或干扰敌方雷达系统。

# 主要功能

虚假目标名称（false_target_name）：指定用于此效果的虚假目标定义的名称。如果未指定，将自动生成虚假目标，并使用默认雷达参数结合 default_pulse_density 生成虚假目标。自动生成虚假目标时，雷达发射机需要定义脉冲宽度（pulse_width）和脉冲重复间隔（pulse_repetition_interval）。  
干扰脉冲密度（jamming_pulse_density）：指定用于生成虚假目标的干扰脉冲密度，范围为 [0,1]。此输入将覆盖指定数量（如果输入了虚假目标名称），并且与number_of_false_targets 互斥。用于根据公式计算虚假目标的数量。

默认值：0.1

虚假目标数量（number_of_false_targets）：指定为此雷达类型创建的虚假目标数量。此输入将覆盖指定数量（如果输入了虚假目标名称），并且与 jamming_pulse_density 互斥。用于根据公式计算干扰脉冲密度。

默认值：使用 jamming_pulse_density

扫描速率乘数（scan_rate_multiplier）：指定用于再生虚假目标的扫描速率乘数。如果输入了虚假目标名称，此输入将乘以指定的扫描速率，否则虚假目标的扫描速率等于frame_time 乘以 scan_rate_multiplier。

默认值：1.0

速度（speeds）：指定虚假目标闪烁移动的最小和最大速度值。如果最小和最大速度相等，则所有闪烁的速度相同；如果不相等，则在限制范围内随机抽取速度，并为每个虚假目标闪烁单独设置速度。

默认值： $0 . 0 \ : \mathrm { m } / s$ 到 $0 . 0 \ : \mathrm { m } / s$

# 系统类型数据

通过 system_type_data <system-type-name> ... end_system_type_data 输入块，可以为特定系统类型（例如，传感器类型、干扰器类型）提供必要的数据，以实现该技术。对于未定义的系统类型，可以使用“default”字符串设置默认数据。

# 3.5.5.10.4.14. 假目标模型 WSF_FT_EFFECT

```txt
effect <effect-name> WSF_FT_EFFECT
    ... WSF_PULSE_EFFECT Commands ...
    false_target_name <string-value>
    jamming_pulse_density <real-value>
    scan_rate-multiplier <real-value>
    system_type_data <system-type-name> ... end_system_type_data
    end-effect 
```

概述

WSF_FT_EFFECT 是一种基础效果类型，可以包含在电子保护或电子攻击技术块中，作为给定技术的众多可用效果之一。下面列出的命令是可以在此效果类型的效果块中指定的基础类型命令。

命令

false_target_name <string-value>: 指定此效果使用的虚假目标定义的名称。

注 意 : 如 果 未 指 定 ， 则 将 自 动 生 成 虚 假 目 标 ， 并 结 合 默 认 雷 达 参 数 和default_pulse_density 生 成 虚 假 目 标 。 雷 达 发 射 机 需 要 定 义 pulse_width 和pulse_repetition_interval 以自动生成虚假目标。

jamming_pulse_density <real-value>: 指定用于生成虚假目标的干扰脉冲密度，范围为[0,1]。如果输入了虚假目标名称，此输入将覆盖指定的数量。此输入用于根据以下公式计算虚假目标的数量：

```txt
NumberOfFalseTargets = (PRI/PW) * (ScanTime/PRI) * NumberPulsesIntegrated * jamming_pulse_density
NumberOfPulsesIntegrated = MaximumOf(number_of_pulses_integrated, (AzBeamWidth/ScanRate)/PRI) 
```

默认值: 0.1

scan_rate_multiplier <real-value>: 指定用于再生虚假目标的扫描速率乘数。如果输入了虚假目标名称，此输入将乘以指定的扫描速率，否则虚假目标的扫描速率等于frame_time 乘以 scan_rate_multiplier。

默认值: 1.0

system_type_data <system-type-name> … end_system_type_data: 输入块，用于提供实现给定系统类型（例如，SENSOR-TYPE,JAMMER-TYPE）所需的系统类型特定数据。可以为未定义的系统类型设置默认数据，使用“default”字符串作为系统类型。

```txt
system_type_data <system-type-name> ... WSF_PULSE_EFFECT Commands ... false_target_name <string-value> jamming_pulse_density <real-value> scan_ratemultiplier <real-value> 
```

<system-type-name>: 系统类型的字符串输入，以下数据适用于该类型，有效值为[system-type-name | "default"]。默认数据用于未指定的系统类型，如果未定义，则不会对给定的系统类型应用任何效果。

# 说明

电子对抗（ECM）: 这种效果类型通常用于电子对抗技术中，通过发送无线电频率信号来干扰雷达的操作，达到欺骗或干扰的目的。  
虚假目标生成: 通过调整干扰脉冲密度和扫描速率乘数，可以控制生成虚假目标的数量和特性，以实现特定的电子攻击或保护效果。  
系统类型数据: 为不同的系统类型（如传感器或干扰器）提供特定的数据配置，以便在不同的操作环境中有效应用此效果。

# 3.5.5.10.4.15. 随机极化调制模型 WSF_POL_MOD_EFFECT

```txt
effect <effect-name> WSF_POL_MOD_EFFECT  
electronic_warfare-effect Commands  
... WSF_SLC_DEGRADE_EFFECT Commands ...  
WSF_REPEATER_EFFECT Commands  
WSF_POWER_EFFECT Commands  
WSF_RADIUS_EFFECT Commands  
polarization SWITCHING_rate <frequency-value>  
system_type_data <system-type-name> ... end_system_type_data  
end Effect 
```

WSF_POL_MOD_EFFECT 是一种基础效果类型，可以包含在电子保护（electronic_protect）或电子攻击（electronic_attack）技术块中，作为给定技术的众多可用效果之一。该效果涉及极化切换速率的设置，影响电子战系统的性能。

# 主要功能

极化切换速率（polarization_switching_rate）：指定极化切换的频率。极化是指电磁波的电场矢量的方向。在电子战中，极化切换可以用于干扰敌方雷达的探测能力。有关其使用和效果的更多信息，请参阅 WSF_SLC_EFFECT 及其 canceller_settling_time。

默认值：0.0 秒

# 系统类型数据

通过 system_type_data <system-type-name> ... end_system_type_data 输入块，可以为特定系统类型（例如，传感器类型、干扰器类型）提供必要的数据，以实现该技术。对于未定义的系统类型，可以使用“default”字符串设置默认数据。

# 3.5.5.10.4.16. 半径因子调制模型 WSF_RADIUS_EFFECT

# 3.5.5.10.4.17. 干扰半径因子调制模型 WSF_JAMMER_RADIUS_EFFECT

```txt
effect <effect-name> WSF_RADIUS_EFFECT  
    electronic Warfare-effect Commands  
    radius_factor <target-position-type> <value>  
    system_type_data <system-type-name> ... end_system_type_data  
end Effect 
```

WSF_RADIUS_EFFECT 是一种基础效果类型，可以包含在电子保护（electronic_protect）或电子攻击（electronic_attack）技术块中，作为给定技术的众多可用效果之一。该效果主要用于调整基于目标位置的有效干扰水平。

主要功能

半径因子（radius_factor/jamming_radius_factor <target-position-type> <value>）：指定基于目标相对于传感器接收器和干扰发射器的位置类型的有效干扰水平调整因子。此调整会修改通常确定的干扰功率。如果在 system_type_data 输入块中指定此输入，则它特定于某个系统类型，否则此输入被定义为未定义系统类型的“默认”数据。可以多次列出此输入以定义不同的 <target-position-type> 值。

□ 目标位置类型（<target-position-type>）：

inside：如果目标范围在干扰器范围（半径）内，则应用 <ratio-value>。  
inside_and_equal：如果目标范围在干扰器范围（半径）内或等于干扰器范围，则应用 <ratio-value>。  
outside：如果目标范围在干扰器范围（半径）外，则应用 <ratio-value>。  
outside_and_equal：如果目标范围在干扰器范围（半径）外或等于干扰器范围，则应用 <ratio-value>。  
outside_and_inside 或 inside_and_outside：如果目标范围在干扰器范围（半径）内或外，则应用 <ratio-value>。  
equal：如果目标范围等于干扰器范围（半径），则应用 <ratio-value>。  
inside_and_outside_and_equal 或 all：如果目标范围在干扰器范围（半径）内、外或等于干扰器范围，则应用 <ratio-value>。

□ 值（<value>）：指定应用于给定 <target-location-type> 的干扰功率水平的因子，必须大于或等于 0。

# 系统类型数据

通过 system_type_data <system-type-name> ... end_system_type_data 输入块，可以为特定系统类型（例如，传感器类型、干扰器类型）提供必要的数据，以实现该技术。对于未定义的系统类型，可以使用“default”字符串设置默认数据。

# 3.5.5.10.4.18. 重复脉冲干扰模型 WSF_REPEATER_EFFECT

```txt
effect <effect-name> WSF_REPEATER_EFFECT  
electronic_warfare-effect Commands  
WSF_RADIUS_EFFECT Commands  
repeater Effect_control_method <repeater-control-method>  
gain_control_method <gain-control-method>  
repeater_factorlimits <min-repeater-factor> <max-gain-factor> 
```

```perl
desired=false_target_rcs<area-value> desired_jammer_to_noise <dbratio-value> desired_jammer_to_signal <dbratio-value> minimumdetect_factor <dbratio-value> masking_factor <dbratio-value> system_type_data <system-type-name> ... end_system_type_data end-effect 
```

重复效应本质上是通过一个名为 repeaterfactor的效应变量，将某种自动增益控制方法应用于物理干扰功率的实现。此效应可以用来模拟许多重复干扰系统的逆增益和增益控制/调平方法。

这种基础效应类型可以作为给定技术的众多可用效应之一，包含在 electronic_attack技术块中。下面列出的命令是该效应类型的基本命令，可以在效应块中指定。

命令

repeater_effect_control_method <repeater-control-method>

指定一个重复器控制方法，如下表所述，用于设置将在计算应用于干扰功率的 repeaterfactor 时使用的数据类型。此调整会修改通常确定的干扰功率。如果此输入在system_type_data输入块中指定，则它特定于一种系统类型，否则，此输入被定义为用于未定义系统类型的“默认”数据。

□ <repeater-control-method>

这是一个字符串输入，定义了有效值，列表如下：

none：不会应用任何重复效应。此控制方法是默认值，因此只有当此命令设置为此方法以外的其他方法时才继承效应。  
actuals：使用实际接收器（例如传感器或通信）的数据来推导设置重复因子的最小、峰值和实际增益值。  
repeater：使用来自重复器的 ESM 系统检测更新的数据来获取设置重复因子的最小、峰值和实际增益值。如果数据未设置，则不计算重复因子。  
repeater_actuals：如果可用，尝试首先使用重复器数据。如果此数据不可用，则使用 actuals。这两者在上表中描述。  
默认值：none

gain_control_method <gain-control-method>

指定将用于确定用于计算 repeaterfactor的最小增益值的控制方法。此调整会修改通常确定的干扰功率。如果此输入在 system_type_data 输入块中指定，则它特定于一种系统类型，否则，此输入被定义为用于未定义系统类型的“默认”数据。如果要使用多种类型，则可以多次输入此输入。

□ <gain-control-method>

这是一个字符串输入，定义了有效值，列表如下：

□ none：不会应用任何重复器最小增益控制方法。此增益控制方法是默认值，因此只有当此命令设置为此方法以外的其他方法时才继承效应。  
□ minimum_detect：重复因子的最小值将基于接收器检测干扰的最小功率加上minimum_detect_factor 和即将到来的发射机的最大增益数据来设置。对于相干类型的干扰波形，最小重复因子将使用最小检测阈值作为基础进行计算，对于非相干（即噪声类型）则使用接收器噪声功率值作为基础计算此值。  
□ jammer_to_noise：重复因子的最小值将基于干扰达到所需 jammer_to_noise 值的最小功率，并在即将到来的发射机的最大增益数据内设置。对于相干和非相干类型的

干扰波形，最小重复因子将使用接收器噪声功率值作为基础进行计算。

▫ jammer_to_signal：重复因子的最小值将基于干扰达到所需 jammer_to_signal 值的最小功率，并在即将到来的发射机的最大增益数据内设置。对于相干和非相干类型的干扰波形，最小重复因子将使用接收器接收信号功率值作为基础进行计算。  
▫ masking：重复因子的最小值将基于干扰有效掩盖接收器中目标回波的最小功率加上 masking_factor 值，并在即将到来的发射机的最大增益数据内设置。对于相干类型的干扰波形，最小重复因子将使用当前计算的相互作用的目标回波功率，或使用虚假目标相互作用的 RCS 的期望回波功率，对于非相干（即噪声类型）则使用计算中需要掩盖即将计算的相互作用目标回波的功率。  
desired_rcs：重复因子的最小值将基于接收器在即将到来的发射机的最大增益数据下有效达到期望 desired_false_target_rcs 值的最小功率来设置。这仅适用于相干类型的干扰波形，最小重复因子将使用目标回波功率与期望与实际用于相互作用的RCS 比率进行计算。目前此方法仅影响虚假目标闪烁。

注意：对于上述多个方法，将使用最大重复因子，且在发射机增益数据的限制范围内。

默认值：none

repeater_factor_limits <min-repeater-factor> <max-gain-factor>

指定计算出的 repeater factor 将受限的最小和最大增益因子。如果此输入在system_type_data输入块中指定，则它特定于一种系统类型，否则，此输入被定义为用于未定义系统类型的“默认”数据。

默认值：0.0 dB

desired_false_target_rcs <area-value>

指定虚假目标闪烁的期望 RCS 值，当技术中启用虚假目标效应时，将为其计算 repeaterfactor 。 此 输 入 会 自 动 将 gain_control_method 设 置 为 desired_rcs 。 如 果 此 输 入 在system_type_data输入块中指定，则它特定于一种系统类型，否则，此输入被定义为用于未定义系统类型的“默认”数据。

默认值：0.0 dB

desired_jammer_to_noise <dbratio-value>

指定期望的 J/N 值，其中 J 是干扰功率，N 是接收器噪声功率，将为其计算repeaterfactor。此 输 入 会 自 动 将 gain_control_method 设 置 为 jammer_to_noise 。 如 果 此 输 入 在system_type_data输入块中指定，则它特定于一种系统类型，否则，此输入被定义为用于未定义系统类型的“默认”数据。

默认值：0.0 dB

desired_jammer_to_signal <dbratio-value>

指定期望的 J/S 值，其中 J 是干扰功率，S 是接收器中的信号功率，将为其计算 repeaterfactor。此输入会自动将 gain_control_method 设置为 jammer_to_signal。如果此输入在system_type_data输入块中指定，则它特定于一种系统类型，否则，此输入被定义为用于未定义系统类型的“默认”数据。

默认值：0.0 dB

minimum_detect_factor <dbratio-value>

指定当 gain_control_method 设置为 minimum_detect 时，将添加到计算出的最小检测repeater factor 的因子（以 dB 为单位，绝对值相乘）。如果此输入在 system_type_data 输入块中指定，则它特定于一种系统类型，否则，此输入被定义为用于未定义系统类型的“默认”数据。