发射功率 $P _ { t }$

发射功率 $P _ { t }$ 是发射器的（峰值）功率。如果定义了平均功率 $P _ { a v e . }$ ,则发射功率设置为：

$$
P _ {t} = \frac {P _ {a v e}}{C}
$$

其中 $P _ { a v e }$ 是平均功率， $C$ 是从调制类型获得的占空比。

发射天线增益 $G _ { t }$

发射天线增益 $G _ { t }$ 表示由于发射器处的平面波引起的理想近场强度：

$$
G _ {t} \equiv \left(\frac {\pi D _ {t}}{\lambda}\right) ^ {2} = \frac {4 \pi A _ {t}}{\lambda^ {2}}
$$

其中 $D _ { t }$ 是（圆形）发射器孔径直径， $A _ { t }$ 是发射器孔径面积，?是激光波长。

发射器损耗 $L _ { t }$

发射器损耗 $L _ { t }$ 由于光学传输损耗、遮挡和截断，以及波前和指向损耗而发生：

$$
L _ {t} = L _ {r, o p t i c s} L _ {w a v e f r o n t} L _ {p o i n t i n g}
$$

其中 $L _ { o p t i c s }$ 是光学传输因子，??????????是波前传输因子， $L _ { p o i n t i n g }$ 是指向传输因子。

如果指定了波前误差，则波前传输因子计算如下：

$$
e x p \left(- (2 \pi W) ^ {2}\right)
$$

其中?是以波长分数表示的波前误差。

自由空间范围损耗 $L _ { R }$

自由空间范围损耗 $L _ { R }$ 定义为：

$$
L _ {R} \equiv \left(\frac {\lambda}{4 \pi R}\right) ^ {2}
$$

其中 $R$ 是从发射器到接收器的距离。

大气损耗 $L _ { a t m }$

大气损耗 $L _ { a t m }$ 表示大气衰减（消光），以及由于湍流和空气光学效应引起的损耗：

$$
L _ {a t m} = L _ {a t t e n} L _ {t u r b} L _ {a o}
$$

其中 $L _ { a t t e n }$ 是衰减传输因子， $L _ { t u r b }$ 是湍流传输因子， $L _ { a o }$ 是空气光学传输因子。

接收天线增益 $G _ { r }$

接收天线增益 $G _ { r }$ 形式与发射天线增益相同：

$$
G _ {r} \equiv \left(\frac {\pi D _ {r}}{\lambda}\right) ^ {2} = \frac {4 \pi A _ {r}}{\lambda^ {2}}
$$

其中 $D _ { r }$ 是接收器的（圆形）孔径直径， $A _ { r }$ 是相关面积。

接收器损耗 $L _ { r }$

接收器损耗 $L _ { r }$ 由于光学传输损耗、遮挡和截断（光学传输因子）而发生：

$$
L _ {r} = L _ {r, o p t i c s}
$$

# 信号计算

接收器处的平均信号电子数从接收到的功率计算如下：

$$
N _ {s i g n a l} = \frac {G _ {\eta} P _ {r} t _ {s l o t}}{E _ {\lambda}}
$$

其中：

$G$ :是探测器增益（detector_gain）。  
$\eta$ :是探测器的原子效率（quantum_efficiency）。  
$t _ { s l o t }$ :是时隙宽度（slot_width）。  
$\begin{array} { r } { E _ { \lambda } \equiv \frac { h c } { \lambda } } \end{array}$ ?? ≡ :是激光波长?处的特征光子能量。

# 噪声计算

接收器噪声是由于电流的统计波动引起的。这些噪声源包括：

1) 由于转换光子引起的电流变化：

a. 背景解析源（例如，恒星），使用背景辐照度（background_irradiance）输入计算。  
b. 背景未解析源（例如，散射的太阳辐射），使用背景辐射度（background_radiance）输入计算。  
c. 发射器（信号光子）。

2) 热噪声（Johnson 噪声），使用电路温度（circuit_temperature）和电路电阻（circuit_resistance）或电路电容（circuit_capacitance）输入计算。  
3) 放大（“体”）暗电流（散粒噪声），使用暗计数率（dark_count_rate）或暗电流（dark_current）输入计算。  
4) 未放大（“表面”）暗电流（散粒噪声），使用表面暗计数率（surface_dark_count_rate）或表面暗电流（surface_dark_current）输入计算。

除了热噪声，这些波动遵循泊松统计：假设噪声电流源的方差等于其平均值来计算。

# 背景光子

背景光子入射到探测器上并转换为光电子，与信号光子相同。因此，来自背景源的平均光子数为：

$$
N _ {b a c k} = \eta L _ {r, o p t i c s} \left(L _ {e, \Omega , \lambda} \Omega_ {f o v} + E _ {e, \lambda}\right) t _ {s l o t} \Delta \lambda / E _ {\lambda}
$$

其中：

$L _ { e , \varOmega , \lambda }$ ：是背景光谱辐射度（background_radiance）。  
$E _ { e , \lambda }$ ：是背景光谱辐照度（background_irradiance）。  
$\Omega _ { f o v }$ ：是由探测器视场定义的立体角。  
：是光学滤波器带宽。

# 立体角计算

立体角计算为：

$$
\Omega_ {f o v} \equiv \frac {\pi}{4} \theta_ {f o v}
$$

其中θ 是全视场角（假设为圆形；此计算使用小角度近似）。

# 散粒噪声方差

由于信号和背景光电流引起的散粒噪声方差等于最初产生的电子数，受探测器增益和过量噪声因子的影响：

$$
\begin{array}{l} \sigma_ {s i g n a l} ^ {2} = N _ {s i g n a l} G F \\ \sigma_ {b a c k} ^ {2} = N _ {b a c k} G F \\ \end{array}
$$

其中?是过量噪声因子。

# 暗电流引起的散粒噪声方差

暗电流引起的散粒噪声方差包括放大和未放大的贡献：

$$
\sigma_ {d a r k} ^ {2} = \left(I _ {d a r k, s u r f a c e} + I _ {d a r k, b u l k} \cdot G \cdot F\right) t _ {s l o t} / q
$$

其中 $I _ { d a r k , b u l k }$ 是由暗电流（dark_current）输入提供的放大暗电流，?????,???????是由表面暗电流（surface_dark_current）输入提供的未放大暗电流。

# 热噪声方差

热噪声是由于电阻中电子的热运动引起的。热噪声方差如下：

$$
\sigma_ {t h e r m a l} ^ {2} = \frac {2 k T}{R _ {L} q ^ {2}} t _ {s l o t}
$$

其中 是电路温度， $R _ { L }$ 是电路电阻， $k$ 是玻尔兹曼常数。

或者，基于电容计算的噪声方差为：

$$
\sigma_ {t h e r m a l} ^ {2} = \frac {K T C}{e ^ {2}}
$$

其中?是电路电容值， $e$ 是基本电荷（电子电荷）。

# 信噪比 SNR 的计算

定义总噪声贡献为噪声方差之和的平方根：

$$
N _ {n o i s e} = \sqrt {\sigma_ {s i g n a l} ^ {2} + \sigma_ {b a c k} ^ {2} + \sigma_ {d a r k} ^ {2} + \sigma_ {t h e r m a l} ^ {2}}
$$

信噪比（SNR）为：

$$
S N R = \frac {N _ {s i g n a l}}{N _ {n o i s e}}
$$

# 背景光谱辐射度和辐照度的参考值

以下表格列出了一些特征激光波长下的背景辐射度和辐照度的可能值：

辐照度（ $\mathrm { \Delta } W / \mathrm { m } ^ { 2 } / \mu \mathrm { m }$ ）

<table><tr><td>波长(μm)</td><td>太阳</td><td>月亮</td><td>水星</td><td>金星</td><td>火星/木星</td><td>土星</td></tr><tr><td>0.53</td><td>1842</td><td>0.0027</td><td>1.8E-7</td><td>1.8E-6</td><td>2.8E-7</td><td>8.4E-8</td></tr><tr><td>0.85</td><td>940</td><td>0.0015</td><td>9.5E-8</td><td>9.0E-7</td><td>1.5E-7</td><td>4.6E-8</td></tr><tr><td>1.06</td><td>748</td><td>0.01</td><td>7.2E-8</td><td>7.1E-7</td><td>1.1E-7</td><td>3.2E-8</td></tr><tr><td>1.3</td><td>411</td><td>0.00054</td><td>3.7E-8</td><td>3.6E-7</td><td>5.6E-8</td><td>1.7E-8</td></tr><tr><td>1.5</td><td>204</td><td>0.00024</td><td>1.7E-8</td><td>1.6E-7</td><td>2.5E-8</td><td>7.5E-9</td></tr></table>

辐射度（ $\mathrm { \Delta W / m ^ { 2 } / s r / \mu m }$ ）

<table><tr><td>波长(μm)</td><td>阳光照射的云</td><td>阳光照射的雪/冰</td><td>星场</td></tr><tr><td>0.53</td><td>245</td><td>330</td><td>3.0E-6</td></tr><tr><td>0.85</td><td>180</td><td>220</td><td>1.4E-6</td></tr><tr><td>1.06</td><td>120</td><td>190</td><td>1.1E-6</td></tr><tr><td>1.3</td><td>50</td><td>140</td><td>6.0E-7</td></tr><tr><td>1.5</td><td>40</td><td>100</td><td>4.0E-7</td></tr></table>

# 3.2.7. 多通信模型 WSF_MULTIRESOLUTION_COMM

```txt
multiresolution_comm WSF MultiresOLUTION COMM ... multiresolution_comm ... endMULTIRESOLUTION COMM 
```

概述

multiresolution_comm 定义了一个容器，用于在平台上保存一个或多个通信（comm）对象，并将选择使用哪个 comm 推迟到运行时。选择 comm 是通过与组件关联的 fidelity 参数来完成的。容器中定义的每个 comm 模型都分配了一个 fidelity_range，在初始化期间根据匹配的 fidelity 设置平台上的 comm。

使用方法

定义新类型: 可以在 platform 或 platform_type 命令之外使用 multiresolution_comm 来定义新类型。

```txt
multiresolution_comm <derived> WSF Multiresolution COMM  
fidelity <real-value>  
[add | edit] model <string-value>  
fidelity_range <real-value> <real-value>  
[default]  
comm [<comm-type>]  
... comm-specific commands ...  
end_comm  
end_model  
[add | edit] model <string-value>  
... Any number of models may be specified ...  
end_model  
common  
... comm-specific commands ...  
end_common  
endMULTIRESOLUTIONCOMM 
```

实例化对象: 可以在 platform_type 或 platform 实例上实例化一个 multiresolution_comm 对象。实例化时需要提供一个名称。

```txt
platform_type ...
multiresolution_comm <name> <type>
... multiresolution_comm commands ...
endMULTIRESOLUTIONCOMM
endPLATFORM_TYPE 
```

```txt
platform ... 
```

```perl
add multiresolution_comm <name> <type> ... multiresolution_comm commands ... endMULTIRESOLUTONcomm endplatform 
```

修改现有对象: 可以在 platform 实例上修改现有的 multiresolution_comm 对象。

```txt
platform ...
edit multiresolution_comm <name> <type>
... multiresolution_comm commands ...
endMULTIRESOLUTION_comm
endplatform 
```

命令

fidelity <real-value>: 定义组件的 fidelity 值，决定在运行时使用哪个 comm。必须在 0 到1 之间（包括 0 和 1）。此值直接映射到模型命令中定义的 fidelity_range。

默认值: 1.0

model <string-value> ... end_model: 定义或编辑包含的 comm 模型，名称由字符串给出。支持隐式添加（或编辑如果命名模型存在）以及使用 add 和 edit 命令的显式添加和编辑。

注意: 必须至少指定一个模型块。

fidelity_range <real-value> <real-value>: 定义此模型应使用的 fidelity 值范围。必须在 0到 1 之间（包括 0 和 1），按递增顺序排列，并且不得与此组件上的另一个模型的fidelity_range 重叠。

默认值: 0.0 1.0

default: 如果没有匹配的 fidelity，则使用此模型作为默认选择。  
comm <comm-type> ... end_comm: 定义 comm 模型的类型和特定于此模型实例化的参数。在首次定义新模型时需要 comm，在编辑现有模型时不得指定。  
common ... end_common: 定义要转发到所有当前指定的 comm 模型的通用参数。这些参数必须对所有当前定义的 comm 模型有效。

说明

多分辨率分析: 这种方法允许在不同的分辨率下分析和选择合适的 comm模型，以便在不同的场景中优化通信性能。  
未来改进: 计划在场景文件的其他位置提供 fidelity 选择，以提高此组件的实用性。

# 3.3. 处理器 processor

```txt
processor <name> <base-type> ... Platform Part Commands ... update_interval ... end Processor 
```

在 WSF 框架中，processor 是一种用于处理特定任务或功能的组件。它可以被配置为在模拟中以特定的时间间隔更新，或者仅在接收到显式消息时响应。

update_interval <time-reference>

如果非零，则指定模拟将调用处理器的周期性时间间隔。如果为零，则处理器仅响应显式消息。

默认值：0.0

注意：并非所有处理器都支持周期性更新。

# 3.3.1. 脚本处理器 WSF_SCRIPT_PROCESSOR

```tcl
processor <name> WsF-script PROCESSOR  
... processor Commands ...  
... Platform Part Commands ...  
... External Link Commands ...  
behavior_tree ...  
... Finite State Machine Commands ...  
update_interval <time-value>  
on_initiize  
...script definition...  
end_on_initiize  
on_initiize2  
...script definition...  
end_on_initiize2  
on_update  
...script definition...  
end_on_update  
on_message  
...script definition...  
end_on_message  
script void on_message_create(WsfMessage aMessage)  
...script definition...  
end.script  
end Processor 
```

WSF_SCRIPT_PROCESSOR 是一个处理器，允许用户提供脚本，这些脚本可以在处理器接收到消息或被调用进行周期性更新时执行。此外，它允许定义外部链接以将消息路由到其他

平台。除了处理器上的常规“on_update”脚本块，用户还可以在脚本处理器上使用行为树（behavior_tree）和有限状态机命令（Finite State Machine Commands）来帮助组织他们的脚本。脚本处理器每次更新的操作顺序是：

1. on_update 脚本块  
2. 处理器上的 behavior_tree（参见：4.13.1 行为树 behavior_tree）  
3. 有限状态机评估当前状态

命令

on_initialize

```txt
on_initi z e  
...script definition...  
end_on_initi z 
```

此块定义了在处理器的“阶段 1”初始化期间执行的脚本。在阶段 1 初始化期间，处理器不能假设平台或其任何组成部分的状态。

预定义的脚本变量如下：

double TIME_NOW; // 当前模拟时间

WsfMessage MESSAGE; // 接收到的消息

WsfPlatform PLATFORM; // 包含此处理器的平台

WsfProcessor PROCESSOR; // 此处理器（不推荐使用“this”）

on_initialize2

```txt
on_initize2 ..script definition...   
end_on_initize2 
```

此块定义了在处理器的“阶段 2”初始化期间执行的脚本。在阶段 2 初始化期间，处理器可以假设平台及其组成部分已完成阶段 1 初始化。

预定义的脚本变量如下：

double TIME_NOW; // 当前模拟时间

WsfMessage MESSAGE; // 接收到的消息

WsfPlatform PLATFORM; // 包含此处理器的平台

WsfProcessor PROCESSOR; // 此处理器（不推荐使用“this”）

update_interval <time-value>

指定执行 on_update 脚本的间隔。如果未指定此值，则 on_update 脚本将不会执行（即使已定义）。

默认值：0.0 秒

on_update

```txt
on_update ..script definition... end_on_update 
```

此块定义了响应处理器周期性更新（由 update_interval 定义）而执行的脚本。如果未定义 update_interval 或其值为零，则此块将不会执行。

预定义的脚本变量如下：

double TIME_NOW; // 当前模拟时间

WsfPlatform PLATFORM; // 包含此处理器的平台

WsfProcessor PROCESSOR; // 此处理器（不推荐使用“this”）

```txt
on_message 
```

```txt
on_message  
[ type <message-type> [subtype <message-subtype>] ]  
[ default]  
script  
...script definition...  
end_script  
...  
end_on_message 
```

此命令块定义了一个脚本，该脚本在处理器接收到消息时执行。如果脚本块前有 type/subtype 命令，则脚本将处理任何与类型/子类型匹配的消息。如果脚本块前有 default，则它将处理此块中尚未处理的任何消息类型。

<table><tr><td>Type String</td><td>Script Class</td></tr><tr><td>WSF_ASSOCIATION_MESSAGE</td><td>WsfAssociationMessage</td></tr><tr><td>WSF_CONTROL_MESSAGE</td><td>WsfControlMessage</td></tr><tr><td>WSF_IMAGE_MESSAGE</td><td>WsfImageMessage</td></tr><tr><td>WSF_STATUS_MESSAGE</td><td>WsfStatusMessage</td></tr><tr><td>WSF_TASK_ASSIGN_MESSAGE</td><td>WsfTaskAssignMessage</td></tr><tr><td>WSF_TASKiates_TESTMESSAGE</td><td>WsfTaskCancelMessage</td></tr><tr><td>WSF_TASK_CONTROL_MESSAGE</td><td>WsfTaskControlMessage</td></tr><tr><td>WSF_TASK_STATUS_MESSAGE</td><td>WsfTaskStatusMessage</td></tr><tr><td>WSF DropsTracks.Message</td><td rowspan="2">WsfTrackDropMessage</td></tr><tr><td>WSF DropsTracks Drops_message(See note below)</td></tr><tr><td>WSF Tracks.Message</td><td>WsfTrackMessage</td></tr><tr><td>WSF Tracks_NOTIFY_message</td><td>WsfTrackNotifyMessage</td></tr><tr><td>WSF Video_message</td><td>WsfVideoMessage</td></tr></table>

注意：on_message 和 WSF_MESSAGE_PROCESSOR 将接受 WSF_DROP_TRACK_MESSAGE或 WSF_TRACK_DROP_MESSAGE 作为 WsfTrackDropMessage 的有效处理程序。创建 WSF时，与 WsfTrackDropMessage 关联的字符串类型被混淆地称为 WSF_DROP_TRACK_MESSAGE而不是 WSF_TRACK_DROP_MESSAGE。在某个时候，字符串类型将被更改以保持一致，但在此期间，任何一种形式都将在指定的上下文中被接受。

预定义的脚本变量如下：

double TIME_NOW; // 当前模拟时间

WsfMessage MESSAGE; // 接收到的消息

WsfPlatform PLATFORM; // 包含此处理器的平台

WsfProcessor PROCESSOR; // 此处理器（不推荐使用“this”）

示例

on_message   
type WsFTRACKMESSAGE   
script WsfTrackMessage trackMsg $=$ (WsfTrackMessage)MESSAGE;   
writeln("T=",TIME NOW,"Received track:"，trackMsg Track().TrackId().ToString());   
end_script   
default script writeln("T=",TIME NOW,"Received other message");   
end.script   
end_on_message

注意：WSF_SCRIPT_PROCESSOR 将在 on_message 执行后将消息转发到任何链接。使用WsfProcessor.SuppressMessage() 可以防止这种行为。

# 有限状态机命令

show_state_evaluations：指示应将有关状态评估的信息写入标准输出。这基本上显示了每个 next_state 块评估的真或假状态。  
show_state_transitions：指示应将有关状态转换的信息写入标准输出。  
state <state-name>：在状态机中定义一个名为 <state-name> 的状态。每个状态可以使用不同的 behavior_tree。每个状态可以在其中定义子状态。

```txt
state <state-name>
    on_entry
        ... <script-command> ...
    end_on_entry
    on_exit
        ... <script-command> ...
    end_on_exit 
```

```txt
next_state <next-state-name-1> ... <script Commands> ... end_next_state  
next_state <next-state-name-n> ... <script commands> ... end_next_state  
behavior_tree ... behavior_tree Commands ... end_behavior_tree  
state <child-state-name-1> ... end_state  
state <child-state-name-N> ... end_state  
end_state 
```

脚本接口

WsfProcessor 中定义的所有方法（以及由此派生的 WsfPlatformPart 和 WsfObject 中的方法）都可以在此处理器中定义的任何脚本中使用。

on_message_create

script void on_message_create(WsfMessage aMessage) ... end_script

这是一个可选脚本，可以定义它以允许在处理器内部创建消息并在发送之前对其进行修改。这通常用于使用 WsfMessage.SetPriority 覆盖消息的默认优先级。

注 意 ： 此 脚 本 目 前 仅 由 WSF_TRACK_PROCESSOR 在 将 WsfTrackMessage 或WsfTrackDropMessage 发送给外部接收者之前调用。如果定义了此脚本，其他处理器将在未来进行修改以调用此脚本。

# 3.3.2. 武器管理器 WSF_WEAPONS_MANAGER

```txt
processor <name> WSF_WEAPONSMANAGER  
WSFScriptPROCESSORCommands...  
haveco_reporting_strategy [on_launch|on_detonate|on_kill]  
engagement_settings  
ew_targets <boolean-value>  
tar_targets <boolean-value>  
ttr_targets <boolean-value>  
engage_local_ttr_targets_only <boolean-value>  
track_quality <real-value> 
```

```txt
end_engagement_settings  
delays time_between_engagements <time-value> expected SENSOR_acquisition <time-value> end_delays  
wez library <string> tactical_range [aero|max1|max2] end_wez  
end Processor 
```

WSF_WEAPONS_MANAGER 是一个脚本基类，供基于 HELIOS 的武器管理器模型继承。它本身并不作为处理器使用，而是为所有武器管理器处理器提供通用的脚本功能。

脚本接口

WSF_WEAPONS_MANAGER 利用了通用脚本接口和 WSF_SCRIPT_PROCESSOR 的功能。

# 武器管理器命令

haveco_reporting_strategy [on_launch | on_detonate | on_kill]: 指定何时评估交战以报告HAVCO 的成功或失败。on_launch 行为会在导弹仍在飞行时将分配视为完成，因此可能导致对目标的多次不必要分配和射击。

默认值: on_kill

# 交战设置命令

ew_targets <boolean-value>: 如果为真，武器管理器将对来自电子战雷达的目标轨迹进行交战。  
默认值: False   
tar_targets <boolean-value>: 如果为真，武器管理器将对来自 TAR 的目标轨迹进行交战。默认值: False  
ttr_targets <boolean-value>: 如果为真，武器管理器将对来自 TTR 的目标轨迹进行交战。默认值: True  
engage_local_ttr_targets_only <boolean-value>: 如果为真，武器管理器将仅对来自本地TTR 的目标进行交战。  
默认值: True   
track_quality <real-value>: 武器管理器将仅对质量达到或超过指定值的轨迹进行交战。默认值: 0.0

# 延迟命令

time_between_engagements <time-value>: 分配交战之间的延迟。例如，如果武器管理器有两个不同的分配并且都需要在当前时间进行交战，当一个交战时，将发生此延迟，

然后下一个交战。旨在防止同时分配交战。

默认值:0 秒

expected_sensor_acquisition <time-value>: 与预期传感器获取时间相关的延迟。此延迟允许战斗管理器调整分配时间以优化交战射击时间线。分配将提前评估和创建，时间等于此延迟，这允许 IADS 获取足够质量的轨迹以根据优化的时间线交战目标。

默认值:0 秒

# WEZ 命令

library <string>: 设置 WEZ 库名称。

默认值: “”

tactical_range [aero | max1 | max2]: 指定时，武器管理器将使用伴随原则指定的范围。

□ Aero: 表示给定目标航向和速度的拦截范围。  
▫ Max1: 表示给定目标高度下导弹的最大运动范围。  
▫ Max2: 表示给定高度下的最大原则交战范围或导弹的最大范围，以较小者为准。

默认值: aero

# 自卫命令

自卫模块用于定义武器管理器的自卫行为。目前，自卫尚未实现。

enable: 启用自卫。自卫尚未实现。  
disable: 禁用自卫。  
range <length-value>:

默认值:0 米

shot_doctrine [Shoot-1 | Shoot-2 | Shoot-Look-Shoot]

默认值: Shoot-1

shot_expiry <time-value>

默认值:10 秒

Weapons Manager Example   
```txt
engagement_settings ew_targets false tar_targets false ttr_targets true engage_local_ttr_targets_only true end_engagement_settings delays time_between_engagements 0 seconds expected_sensor_acquisition 0 seconds delays wez library none tactical_range aero end_wez 
```

haveco_reporting_strategy on_detonate

self_defense

disable

end_self_defense

# 3.3.3. AI 武器管理器 WSF_WEAPONS_MANAGER_AI

```tcl
processor <name> WSF_WEAPONS managerial_AI  
WSF_WEAPONS managerial Commands ...  
take_action  
enable  
disable  
action_distance <length-value>  
ai_action_1 [Straight|Break-Left|Break-Right]  
duration_1 <time-value>  
ai_action_2 [Straight|Break-Left|Break-Right]  
duration_2 <time-value>  
ai_action_3 [Straight|Break-Left|Break-Right]  
duration_3 <time-value>  
ai_action_4 [Straight|Break-Left|Break-Right]  
duration_4 <time-value>  
end.take_action  
rwr_response  
enable  
disable  
beam_duration <time-value>  
sam_response_range <length-value>  
ai_response_range <length-value>  
restore_after_break_lock <time-value>  
priority [Choose-Closest-Threat | Default]  
end_rwr_response  
alert_time <time-value>  
assess_engage VIA  
[Collision-Intercept-PT-Inside-Zone|Munition-Intercept-PT-Inside-Zone|Munition-Intercept-PT-Ig  
nore-Zone]  
home_base_position <latitude-value, longitude-value>  
intercept_speed <speed-value>  
my_place_inFormation [1|2|3|4]  
pursuit_range <length-value>  
end Processor 
```

WSF_WEAPONS_MANAGER_AI 是基于 HELIOS 的 GTIQBWeaponsManagerAI 端口的脚本类。它是一个用于 AI 武器单元的武器管理器，负责管理 AI 武器单元对指定目标的所有交战方面。这些方面包括：

□ 验证目标是否能够被选定的武器交战  
□ 验证目标是否位于或接近单元的交战区（如果存在）  
□ 验证目标轨迹的质量是否可接受（例如 TTR）

武器管理器 AI 负责监控当前活动的任何分配并与目标交战。此过程包括：

□ 通过拦截或追击来交战目标  
□ 决定是否向正在拦截或追击的目标发射导弹  
□ 接收任何已发射导弹的交战结果  
▫ 如果分配认为有必要，向目标发射额外的第二枚导弹  
□ 一旦分配完成处理，设置分配的最终状态（例如 HAVCO）

武器管理器 AI 还负责感知和规避威胁。这些过程包括：

▫ 确定是否有任何威胁在单元的规避响应范围内（用户可以为 SAM 和 AI 指定不同的响应范围）  
▫ 根据用户指定的标准选择最高优先级的范围内威胁进行规避  
▫ 选择适当的规避行为（如果有）。例如，如果 AI 当前正在与该单元交战，则不会规避另一个单元。

重要提示: 所有 IADSC2 空中拦截器需要此子系统才能正常工作，以交战分配的目标并感知和规避威胁。

# 操作方法

武器管理器 AI(WMAI) 首先检查用户是否启用了规避行为。如果启用了规避行为并且平台具有 RWR，WMAI 选择 RWR 感知到的最高优先级威胁，该威胁在响应范围内，并评估是否规避，使用相对于该威胁的波束响应或拖曳响应。如果 AI 当前正在执行波束响应（试图将威胁置于平台“波束”上的机动），WMAI 检查波束时间是否已过。如果是，WMAI 开始相对于最高优先级威胁的拖曳响应（以最高可能速度远离威胁飞行）。如果不是，则根据需要调整当前波束响应，使其相对于最高优先级威胁。如果 AI 当前正在执行拖曳响应，则根据需要调整拖曳响应，使其相对于高优先级威胁。如果 AI 当前没有规避，WMAI 开始对最高优先级威胁进行波束响应，除非 AI 正在与该单元交战或该单元被认为已死亡。

如果 WMAI 没有继续或开始规避行为，并且用户启用了“采取行动”行为，WMAI 接下来考虑是否采取行动。“采取行动”涉及向左转、向右转或继续直飞特定时间。用户可以为四个可用动作中的每一个指定方向和持续时间。将采取哪一个动作取决于 AI 在编队中的位置，用户也可以设置。WMAI 只有在 AI 当前正在追击或拦截分配时才会采取行动。此外，在 AI 拦截然后追击分配的时间内，它只能采取一次行动。（如果 WMAI 后来收到针对同一目标的另一个分配并以新的拦截或追击行为与之交战，它可能会再次相对于同一目标采取行动。）因此，WMAI 将决定相对于当前分配采取行动，如果：（1）AI 当前正在拦截或追击分配，（2）拦截-追击行为链尚未生成“采取行动”，并且（3）AI 当前没有与分配交战。

如果 WMAI 没有继续或开始规避或采取行动，它会对已分配的目标采取以下步骤：如果当前分配已完成，WMAI 报告 HAVCO 并考虑下一个分配。如果资产未战备就绪或没有有效的主轨迹用于分配，WMAI 报告 CANTCO 并考虑下一个分配。如果 WMAI 发射的齐射少于分配请求的数量，算法确保为交战分配的武器可以定位，弹药充足，并且分配引用有效

的武器记录。（如果这些条件中的任何一个失败，WMAI 报告 CANTCO 并考虑下一个分配。）如果 AI 尚未向目标开火或是时候进行第二次射击，WMAI 报告 WILCO。否则，WMAI 转到下一个分配。

在报告 WILCO 后，WMAI 决定如何处理分配。WMAI 的响应取决于其当前执行的行为：如果 WMAI 没有执行任何行为，它将在目标处于追击范围内时通过追击目标进行交战，如果不在，则通过拦截（飞到预期目标将在未来时间到达的点）进行交战。如果 WMAI 正在执行“采取行动”行为，它将继续评估下一个分配。如果 WMAI 正在拦截指定目标并且已缩短距离使目标现在处于追击范围内，它将停止拦截并开始追击。如果 WMAI 正在通过执行波束响应或拖曳响应进行规避，它将继续下一个分配而不向目标开火。

WMAI 只有在交战目标时才会向指定目标开火，无论是通过拦截还是追击。如果它当前正在拦截或追击与分配对应的目标，WMAI 将决定是否应该开火。首先，WMAI 确保轨迹质量足够高，即轨迹的报告传感器是用户指定应交战的类型。如果用户要求仅交战“本地”TTR 目标，WMAI 检查轨迹是否包含至少一个来自 AI、同级平台或 AI 直接指挥官的 TTR的原始轨迹。其次，WMAI 验证目标是否在武器的射程内。如果这些检查中的任何一个失败，WMAI 将转到下一个分配而不向目标开火。最后，WMAI 验证它是否可以拦截轨迹。如果可以，WMAI 尝试使用分配的射击原则向目标发射齐射。如果不能，它报告 CANTCO 并继续下一个分配。WMAI 向目标发射齐射的尝试将失败，如果：（1）武器没有剩余弹药，（2）武器的最大齐射数量已经激活，或（3）武器正在重新装填且无法在重新装填时射击。否则，发射尝试将成功，这意味着向目标开火的请求将被添加到武器的齐射请求列表中。

# 规避行为的要求

武器管理器 AI 依赖 RWR 来检测和规避威胁。要激活规避行为，用户必须（1）在“rwr_response”块中启用行为（参见命令部分），并且（2）在平台上放置一个WSF_ESM_SENSOR ， 其 类 别 设 置 为 “ RWR ” 。 RWR 必 须 通 过 internal_link 连 接 到track_manager。RWR 检测在其频带内传输的其他传感器，可以使用传感器的“frequency_band”命令更改。因此，RWR 不会检测到 - 并且武器管理器 AI 不会规避 - 没有在 RWR 频带内传输的传感器的威胁。

# 中文翻译与解释

脚本接口

WSF_WEAPONS_MANAGER_AI 利用了通用脚本接口和 WSF_SCRIPT_PROCESSOR 的功能。

# 武器管理器 AI 命令

alert_time <time-value>: 对于停放的 AI，警戒时间表示 AI 准备起飞所需的时间。

默认值:60 秒

assess_engage_via [Collision-Intercept-PT-Inside-Zone | Munition-Intercept-PT-Inside-Zone | Munition-Intercept-PT-Ignore-Zone]:

Collision-Intercept-PT-Inside-Zone 通过评估 AI 是否可以在 FEZ 内拦截目标来评估交战。Munition-Intercept-PT 通过评估 AI 的武器当前是否可以拦截目标来评估交战；Inside-Zone要求目标在 FEZ 内，而 Ignore-Zone 不使用区域。

默认值: Munition-Intercept-PT-Ignore-Zone

debug: 设置时，记录调试信息。

默认值: 关闭

home_base_position <latitude-value, longitude-value>: 确定 AI 的基地的纬度和经度，如果 AI 撤退可能会使用。

默认值: (0,0)

▪ intercept_speed <speed-value>: 拦截速度是 AI 试图拦截轨迹时的移动速度。

默认值: 500 节（257.222 米/秒）

my_place_in_formation [1 | 2 | 3 | 4]: 在采取行动时，AI 在编队中的位置决定执行哪个动作以及持续时间。有关详细信息，请参阅上面的 take_action 文档。

默认值:1

pursuit_range <length-value>: 如果 AI 开始交战轨迹，并且轨迹在 AI 的追击范围内，AI 将追击轨迹而不是拦截它。如果 AI 当前正在拦截轨迹并接近到轨迹落入追击范围内，AI 将停止拦截并开始追击。

默认值: 60,000 米

# 采取行动命令

enable/disable: 启用时，武器管理器 AI 将评估是否在拦截或追击轨迹时相对于目标“采取行动”。

默认值: 禁用

action_distance <length-value>: 在评估是否采取行动时，武器管理器 AI 只有在威胁的action_distance 范围内才会执行行动行为。

默认值: 45,000 米

当武器管理器 AI 执行“采取行动”行为时，平台移动的方向和动作的持续时间取决于单元在编队中的位置，该位置通过 my_place_in_formation 命令设置。位置为 1 的单元将执行 ai_action_1 持续 duration_1，等等。

ai_action_1 [Straight | Break-Left | Break-Right]

默认值: Break-Left

duration_1 <time-value>

默认值:3 秒

ai_action_2 [Straight | Break-Left | Break-Right]

默认值: Break-Right

duration_2 <time-value>

默认值:3 秒

ai_action_3 [Straight | Break-Left | Break-Right]

默认值: Straight

duration_3 <time-value>

默认值:0 秒

ai_action_4 [Straight | Break-Left | Break-Right]

默认值: Straight

duration_4 <time-value>

默认值:10 秒

# RWR 响应命令

此模块用于定义基于 HELIOS 的武器管理器 AI 规避行为参数。

enable/disable: 启用时，武器管理器 AI 将尝试检测和规避威胁。

默认值: 禁用

beam_duration <time-value>: 武器管理器 AI 开始以“波束响应”规避威胁（沿着与威胁速度成 90 度的水平面向左或向右移动）。如果武器管理器 AI 确定在波束时间结束后威胁尚未规避，它可能决定继续使用“拖曳响应”规避（以最高可能速度远离威胁飞行）。beam_duration 确定武器管理器 AI 执行波束响应的时间长度，然后考虑拖曳响应。

默认值:3 秒

sam_response_range <length-value>: 如果威胁的空间域为陆地或地面，武器管理器 AI仅在威胁在 SAM 响应范围内时考虑相对于威胁的规避响应。如果威胁的空间域为水下，武器管理器 AI 也将默认使用 SAM 响应范围，并记录一条错误消息，指出尚未正确实现该域的规避行为。

默认值: 150,000 米

ai_response_range <length-value>: 如果威胁的空间域为空中，武器管理器 AI 仅在威胁在 AI 响应范围内时考虑相对于威胁的规避响应。对于空间域为太空或未知的威胁，武器管理器 AI 也将默认使用 AI 响应范围，并记录一条错误消息，指出尚未正确实现该域的规避行为。

默认值: 40,000 米

restore_after_break_lock <time-value>: 如果 RWR 在一定时间内没有收到与威胁对应的更新，武器管理器 AI 将认为平台已成功打破威胁的锁定。restore_after_break_lock设置在最近一次更新后必须经过的时间，然后才会认为锁定已被打破。

默认值:3 秒

priority [Choose-Closest-Threat | Default]: 即使 RWR 感知到多个威胁在范围内，武器管理器 AI 也只会评估是否相对于每个时间步的一个威胁执行规避行为。priority 命令允许用户选择在决定是否规避时优先考虑哪个威胁的标准。“Default” 仅选择 RWR 活动轨迹列表中首先出现的威胁；这种方法最类似于 HELIOS，但可能导致意外结果，例如 试 图 规 避 一 个 刚 好 在 响 应 范 围 内 的 威 胁 ， 而 忽 略 一 个 更 近 的 威 胁 。

“Choose-Closest-Threat” 相对于离平台最近的威胁评估规避行为。

默认值: Default

# 注意事项

在当前版本中，自卫功能尚未实现。

确保在平台上放置一个类别为“RWR”的 WSF_ESM_SENSOR，以便激活规避行为。

Weapons Manager AI Example   
```txt
take_action enable action_distance 50000 meters ai_action_1 Break-Right duration_1 10 seconds ai_action_2 Break-Right duration_2 10 seconds ai_action_3 Break-Left duration_3 10 seconds 
```

```txt
ai_action_4 Break-Left  
duration_4 10 seconds  
end.take_action  
rwr_response  
enable  
beam_duration 4 seconds  
sam_response_range 120000 meters  
ai_response_range 45000 meters  
restore_after_break_lock 5 seconds  
priority Choose-Closest-Threat  
end_rwr_response  
engagement_settings  
ew_targets false  
tar_targets false  
ttr_targets true  
engage_local_ttr_targets_only true  
end_engagement_settings  
alert_time 90 seconds  
assess_engage_via Collision-Intercept-PT-Inside-Zone  
home_base_position 38:27:24.00n 117:32:40.00w  
intercept_speed 600 kts  
my_place_inFormation 2  
pursuit_range 60000 meters  
salvo_delay 1.5 seconds  
haveco_reporting_strategy on_detonate 
```

# 3.3.4. 地空导弹(SAM）武器管理器 WSF_WEAPONS_MANAGER_SAM

```txt
processor <name> WSF_WEAPONS managerialSAM WSF_WEAPONS MANAGER Commands ... end Processor 
```

中文翻译与解释

概述

WSF_WEAPONS_MANAGER_SAM 是基于 HELIOS 的 GTIQBWeaponsManagerSAM 端口的脚本类。它是一个用于 SAM（地对空导弹）武器单元的武器管理器，负责管理 SAM 武器单元对指定目标的所有交战方面。这些方面包括：

□ 验证目标是否能够被选定的武器交战  
□ 验证目标是否位于或接近单元的交战区（如果存在）  
验证目标轨迹的质量是否可接受（例如 TTR）

武器管理器 SAM 还负责监控当前活动的任何分配并与目标交战。此过程包括：

□ 向发射的导弹发送目标位置更新，以便其可以相应调整飞行路径  
□ 接收任何已发射导弹的交战结果

□ 如果分配认为有必要，向目标发射额外的第二枚导弹  
□ 一旦分配在 SAM 单元完成处理，设置分配的最终状态（例如 HAVCO）

重要提示: 所有 SAM 发射器需要此子系统才能正常工作并能够交战分配的目标。

# 操作方法

武器管理器 SAM 对位于导弹交战区（MEZ）内的目标采取以下行动。算法遍历分配数组。如果当前分配已完成、失败、目标已被摧毁或不活动，或分配已被取消，算法考虑下一个分配。如果 SAM 系统不可用，或导弹不可用，算法退出循环。算法评估是否是齐射中下一枚导弹发射的时间。如果是，则发射下一枚导弹，并在用户设置弹药递减时递减弹药。算法通过预测轨迹是否会进入 MEZ，以及是否满足弹药的最小和最大范围、合理的拦截时间、拦截范围、击杀概率和在接下来的 60 秒内发射的发射时间来评估交战是否仍然可行。如果这些测试失败，交战不再可行，武器管理器报告 CANTCO。

武器管理器 SAM 通过进行轨迹源测试来结束。如果轨迹源对应于用户设置的不交战类型，则目标不交战。对于剩余的交战，评估是否是发射的时间。如果是发射时间，则发送发射命令，并在用户设置弹药递减时递减可用弹药。最后一步是计算齐射中下一枚导弹的发射时间。在每次后续通过中评估此发射，直到发射下一枚导弹。

# 脚本接口

WSF_WEAPONS_MANAGER_SAM 利用了通用脚本接口和 WSF_SCRIPT_PROCESSOR 的功能。

# 武器管理器 SAM 命令

武器管理器 SAM 模型没有增加任何超出 WSF_WEAPONS_MANAGER 基类所提供的命令。

# 3.3.5. 武器服务处理器 WSF_WEAPON_SERVER_PROCESSOR

```txt
processor <name> WSF_WEAPON_SERVERPROCESSOR processor Commands ... Platform Part Commands ... External Link Commands ... wpn_server_type wpn_server_site wpn_server.application wpn_server_entity ack_time_tolerance reallocate_on_NACK debug   
end Processor 
```

# 概述

WSF_WEAPON_SERVER_PROCESSOR 实现了一个与外部武器服务器的处理器接口。它负责通过指定的网络连接处理向适当武器服务器的武器传输。

# 背景信息

武器 ID 的唯一性: 在武器分配阶段之前和设置期间，ID 被称为存储 ID。在武器实际分配后，ID 被称为武器 ID。存储 ID 被发送到武器服务器处理器。武器服务器处理器可 能 会 更 改 存 储 ID ， 这 取 决 于 WSF_EXPLICIT_WEAPON 块 中 是 否 为 特 定weapon_system_type 设置了 dis_entity_id_offset 值。

```txt
weapon USER_WEAPON_TYPE WSF_EXPLICIT_WEAPON  
.  
.  
.  
dis-entity_id_offset 5000  
endweapon 
```

武 器 ID 的 生 成 : 在 这 种 情 况 下 ， 武 器 服 务 器 处 理 器 将 存 储 ID 加 到dis_entity_id_offset（如果未提供，则 dis_entity_id_offset 为 0）以形成武器 ID。武器ID 将被视为武器的数据链或 JU 编号。此值也用于武器的 DisEntityState 实体 ID 字段，并在 SetDataPDU 中设置，该 PDU 被传递到 DREAMS 武器服务器。在武器分配时，SetDataPDU 被发送到 DREAMS 武器服务器应用程序。如果 DREAMS 武器服务器验证了分配 SetDataPDU，它会返回一个响应的 DataPDU，分配字段设置为 1，表示武器已分配，然后武器进入 ALLOCATE(1) 状态，之后武器服务器处理器将发送脐带数据。如果武器服务器应用程序确认了该数据，则过程完成，武器进入 READY(4) 状态。武器只能在 READY 状态下发射，否则 Fire 命令无效。  
发射过程: 如果过程成功，并且使用武器 ID 参数执行了 Fire 命令，WSF 应用程序发出的 DisFire PDU 将在 DisFire PDU 实体 ID 字段中插入武器 ID。如果在没有武器 ID参数的情况下执行发射命令，WSF 使用 WSF ID 方法来标识导弹。很可能在分配序列期间设置的 ID 不匹配，可能会导致发射序列出现问题。  
武器分配: 可以使用以下 WsfWeapon 脚本命令分配武器：AllocateTheWeapon()  
武器状态: 在发射前必须评估武器状态，并且必须处于 READY 状态（4）才能发射。返回状态为 1 表示武器已分配。返回状态为（3）表示武器从未分配。用户可以检查传出的 weapon_system_type 的 DIS 实体类型是否匹配。  
武器发射: 可以使用 WsfWeaponFire 脚本命令发射武器。  
初始设置: 可以使用 WsfWeaponServerProcessor 函数 SetStoreIdTrackPairing_() 设置初始 store_id 值。

# 注意事项

确保在武器分配和发射过程中正确设置和使用武器 ID，以避免发射序列中的问题。

在发射前，确保武器处于 READY 状态，以确保 Fire 命令的有效性。

# DIS 接口文件输入设置

在为 DREAMS 武器服务器设置 DIS 接口文件时，dis_interface 块应按照通常的方式设置，其中 site 和 application 字段应与 XML 输入文件中的 platform 块匹配。以下是设置的关键点：

# DIS 接口块设置

site: 这个字段应该与 XML 输入文件中 platform 块的 site 字段匹配。它指定了武器服

务器所在的站点。

application: 这个字段应该与 XML 输入文件中 platform 块的 application 字段匹配。它指定了武器服务器应用程序的标识。

# 注意事项

确保 site 和 application 字段的值在 dis_interface 块和 platform 块中是一致的，以确保正确的网络连接和数据传输。  
在配置 DIS 接口时，确保所有相关的网络参数和标识符都正确设置，以避免通信错误。  
通过正确配置这些字段，DREAMS 武器服务器能够通过指定的网络连接正确处理武器的传输和分配。

```xml
wsrc_userName.xml input file   
<platform> <entity-id> <site>79</site> <appv2000</app> . . . </entity-id> </platform>   
<munition-type-defn> <!-- Assign a unique identifier to the munition type --> <name>JDRADM_POD</name> <enable=true</enable> <entity-type> <kind>2</kind> <domain>1</domain> <country>225</country> <category>1</category> <subcategory>29</sub>  
<specific>0</specific> <extra>0</extra> </entity-type> . . . </munition-type-defn> 
```

end of wsrc_userName.xml file.

dis_interface   
```txt
site 79   
application 2000   
exercise 1   
port 3456 
```

//entity_type_keyword weapon_server_type kind do main country cat subcat specific extra   
```txt
//List both the weapon system type and the weapon platform type in the entity_type list //in the entity_type list. Note the entity type match in the munition-type-defn portion //of the DREAMS xml file. 
```

```asm
entity_type &nbsp  
; ATA_POD  
2122512900 // Must match  
// out_going weaponry_transfer  
// input line  
entity_type &nbsp  
; ATAPLATFORM &nbsp  
; 2122512900 // Must match the  
// out_going weaponry_transfer  
// input line 
```

This is the critical line that does the weapon transfer out and does the fire PDU and drops the weapon on the WSF

side. Add this line for all weapon_system_types that are going to be controlled by the weapon server.

```txt
outgoingweapon_transfer ATA_POD  
outgoingweapon_transfer mslweapon_jassm  
outgoingweapon_transfer mslweapon_sdb_new 
```

```txt
end_dis-interface 
```

WSF 输入文件更改以适应武器服务器接口

在为 DREAMS 武器服务器配置 WSF 输入文件时，需要进行以下更改：

目标的空间域

空间域设置: 对于每个 DREAMS 武器目标，必须指定 spatial_domain。这用于填充DREAMS 武器服务器期望的空对地或空对空字段。根据平台类型适当地添加 spatial_domain，例如：

```txt
spatial_domain <air | land> 
```

这确保了目标的空间域与武器服务器的期望相匹配。

导弹类型的范围设置

范围设置: 每种导弹类型都有其自己的范围，这通过在 WSF_EXPLICIT_WEAPON 块中使用 dis_entity_id_offset 来设置。例如：

```txt
weapon USER_WEapon_TYPE WSF_EXPLICIT_WEapon dis-entity_id_offset <range_value> endweapon 
```

这允许为每种导弹类型指定特定的范围值，以确保在武器服务器中正确配置。

注意事项

确保 spatial_domain 和 dis_entity_id_offset 的设置与武器服务器的需求一致，以避免通信和配置错误。

这些设置对于确保武器服务器能够正确识别和处理目标和导弹类型至关重要。

weapon msl weapon_jassm WSF_EXPLICIT_WEAPON   
quantity 12   
launchedplatform_type mslplatform_jassm   
weapon_effects msl_effects   
dis-entity_id_offset <DisUint16 Value>   
aux_data   
//available fields to set umbilical data   
// $1 =$ laser; $2 =$ sensor; $3 =$ coordinate (default 2) int attack_mode $= 2$ //To define one of the source target originator fields,use one of the two options   
//1) use initial_target_index_originator - track information coming from launching platform   
//2) use thirdParty_source_number to set a third party as the source of track information.   
//They are mutually exclusive

```asm
// Each option has a bool input that must be set to, true, in order for the field to be
// set with the assigned data.
// To use the initial target index originator/target index pair (and NOT the third party
// source number).
// Set the associated bool first
// bool use_initial_target_index_originator <true | yes | false | no>
// if omitted will be 0 or false and data field will not get set.
// 
// bool use_initial_target_index_originator = true
// 
// Then set data for the initial target index originator field,
// initial_target_index_originator <decimal-track-number>
// where decimal-track-number = decimal_track_number defined in the l16_computer block.
// 
// int initial_target_index_originator = 121
// 
// XOR
// 
// Set the bool to allow the thirdParty_source_field to be filled.
// useThirdParty_source_number <true | yes | false | no>
// If omitted or use_thirdParty_source_number set to <no | false > then the third-party
source number
// will not be used.
//bool use_thirdParty_source_number = true
// 
// Set the third-party source number field
// thirdParty_source_number <decimal-track-number>
// Where the decimal-track-number = decimal_track_number defined in the l16_computer
block.
int thirdParty_source_number = 121
// 
// can reassign the weapon site and application value, else will be site and
app found in dis text file
int weapon_site
int weapon_app
end(aux_data
endweapon
platform platform_name WSFPLATFORM
aux_data
int initial_target_index_originator = 120
// match decimal_track_number in l16_computer, else will use the platform's index
int decimal_track_number = 120 
```

```txt
aux_data endplatform 
```

For Each Platform that is to interact with the weapon server must have a weapon server processor.

```txt
processor <name> WSF_WPN_SERVERPROCESSOR  
available inputs  
<on | off>  
update_interval time  
wpn_server_type <DREAMS | WSF | VENDOR_R>  
wpn_server_site  
value  
// maps to site macrotag  
wpn_server.application value // maps to app macrotag  
wpn_server-entity  
value // maps to entity macrotag  
ack_tolerance_time  
time // time it takes before resend if weapon server does not respond  
end Processor 
```

Example shown below:

```txt
platform_type weapon_server_type WSFPLATFORM
.
.
.
.
.
// would have link16 comm set up here also
// launching platform or at least the one sending the initial
// allocation data (set data pdus) to the weapon server
processor wpn_server_proc WSF_WPN_SERVERPROCESSOR
on
update_interval 1 sec
wpn_server_type DREAMS
wpn_server_site 11
wpn_server.application 22
wpn_server-entity 33
ack_tolerance_time 3 s
end Processor
.
.
.
.
end platform 
```

3.3.6. 武器引导处理器 WSF_WEAPON_TRACK_PROCESSOR  
```txt
processor <name> WSF_WEAPONTRACKPROCESSOR processor Commands ... Platform Part Commands ... WSFScriptPROCESSORCommands... turn_on SENSOR ... coast_time ... switch_time ... switch_range ... ignore_uplink_target_change uplink_required ...   
end Processor 
```

概述

WSF_WEAPON_TRACK_PROCESSOR 继承自 WsfProcessor，用于提供一种简单的方法来发射武器并引导武器到达目标轨迹。它提供了一些子命令来处理滑行时间、打开终端传感器以及与脚本语言的接口。在大多数情况下，该处理器足以单独用于武器，以引导武器到达目标。WSF_WEAPON_TRACK_PROCESSOR 仅处理来自地面或机载传感器的原始轨迹。

如果武器平台需要额外的功能（例如，多个终端传感器、任务管理以控制当前目标），建 议 创 建 一 个 WSF_TRACK_PROCESSOR 来 创 建 轨 迹 管 理 器 ， 以 及 一 个WSF_TASK_PROCESSOR 来 响 应 来 自 轨 迹 管 理 器 的 WsfLocalTrack(s) ， 并 从 平 台 中 移 除WSF_WEAPON_TRACK_PROCESSOR。如果在一个平台上同时存在 WSF_TASK_PROCESSOR（以及 WSF_TRACK_PROCESSOR）和 WSF_WEAPON_TRACK_PROCESSOR 来控制武器平台的行为，可能会出现意外结果。

警告: 该处理器依赖于平台的当前目标轨迹是一个有效的三维轨迹，以便在计算拦截范围和时间时使用。

命令

turn_on_sensor <sensor-name> at_range <length-value> [before_intercept | to_target]   
turn_on_sensor <sensor-name> at_time <time-value> [before_intercept | after_launch]<sensor-name>: 平台上的传感器名称。

在以下四种条件之一下打开传感器：

□ (at_range / before_intercept): 当拦截距离低于指定值时。  
□ (at_range / to_target): 当到当前目标位置的距离低于指定值时。  
□ (at_time / before_intercept): 当拦截时间低于指定值时。  
▫ (at_time / after_launch): 当飞行时间达到指定值后。

coast_time<time-value>: 武器在不接收轨迹更新的情况下保持活动的时间。当达到滑行时间时，武器交战终止。

默认值: 无限制

switch_time<time-value>: 指定拦截时间，当达到该时间时，处理器切换到终端制导。默认值: 未使用  
switch_range <length-value>: 指定拦截范围，当达到该范围时，处理器切换到终端制导。

默认值: 未使用

ignore_uplink_target_change: 强制处理器忽略与当前目标无关的轨迹消息。  
uplink_required <boolean-value>: 指定是否需要上行链路（外部）轨迹更新。这与coast_time 结合使用，以决定哪些轨迹源用于决定滑行时间是否已超过。如果为 true，则仅使用最后接收到的上行链路的时间。如果为 false，则使用最后接收到的上行链路和最后接收到的本地传感器轨迹的最大时间。对于指令制导武器（无论是否有终端导引头），true 是合适的。对于通过导弹系统跟踪的系统，false 是合适的。

默认值: false

注意事项

确保在使用 WSF_WEAPON_TRACK_PROCESSOR 时，平台的当前目标轨迹是有效的三维轨迹，以便正确计算拦截参数。

根据具体需求配置传感器的开启条件和滑行时间，以优化武器的制导和交战性能。

# 3.3.7. 武器引信 WSF_WEAPON_FUSE

```txt
processor <name> WSF_WEAPONFuse Platform Part Commands .. processor Commands .. WSFScriptPROCESSORCommands ... update_interval ... fine_update_interval ... time_of_flight_to_arm ... // Detonation Based On Time, Altitude or Speed maximum_time_of_flight ... detonatebelow_height_agl ... detonatebelow_height_msl ... detonate_above_height_agl ... detonateabove_height_msl ... detonatebelow_speed ... detonatebelow_mach ... detonate_on_mach_decreasing_to ... // Detonation Based on Target Proximity gross_proximity_range ... hit_proximity_range ... use_current_target do.not_use_current_target exclusive_target_name ... fuse_function_range ... coast_time_on_loss_of_target... 
```

```txt
detonate_on_loss_of_target   
proximity Cancel_on_loss_of_target   
proximity_all_on_loss_of_target   
excluded_category ...   
air_to-ground_mode   
on_intercept ...   
// Script Interface   
on_initi... end_on_initi   
on_initi2 ... end_on_initi2   
on_update ... end_on_update   
script_variables ... endScript_variables   
script ... endScript   
..Other Script Commands ...   
script void onweapon_detonation() ..<script>..   
end.script   
end Processor 
```

WSF_WEAPON_FUSE 是 嵌 入 在 平 台 内 的 处 理 器 ， 用 于 控 制 飞 行 中 的WSF_EXPLICIT_WEAPON 的武装、引爆和终止。终止可能基于飞行时间、平均海平面（MSL）高度、地面以上（AGL）高度、与其他平台的接近程度，或显式的外部引爆命令。由于计算与其他平台的近距离引爆可能会非常耗费计算资源，因此一个重要的考虑因素是是否考虑模拟中的所有平台，还是仅考虑指定的特定平台。通常，空对空交战是针对特定目标进行的，要么该目标受损，要么没有目标受损。空对地交战可能希望仅攻击单一目标，但临近的附带损害通常是一个现实问题。在这种情况下，用户必须通过输入指定是否考虑附带损害。

WSF_AIR_TARGET_FUSE 和 WSF_GROUND_TARGET_FUSE 是此处理器的特殊实现，专为特定类别的目标配置。应在适当时使用它们。

update_interval <time-value>   
gross_update_interval <time-value>: 当不在任何感兴趣的平台附近时，保险处理器的更新间隔。（当接近目标平台时，更新间隔可能会在内部暂时减少。）

默认值: 1.0 秒

fine_update_interval <time-value>

保险处理器在被认为接近感兴趣的平台时的更新间隔。此值必须小于 update_interval，用于增加接近目标时的分辨率和精度。适当的值取决于武器的接近速度。粗略指南是，在武器穿越其致命半径的时间内应经过一个 fine_update_interval。

默认值: 0.05 秒

time_of_flight_to_arm <time-value>

在指定的飞行时间过去之前不考虑引爆。此值相对于武器首次离开“轨道”或“发射台”的时间。这将允许在武器武装引爆之前进行安全的发射分离。如果在武器武装之前通过各种方式命令引爆，武器将从模拟中移除，对任何平台没有破坏性影响。

默认值: 0 秒（武器将立即武装）

基于时间、高度或速度的引爆

maximum_time_of_flight <time-value>

当指定的飞行时间过去时自动引爆。此值相对于武器首次离开“轨道”或“发射台”的时间。这将防止未命中接近目标的武器永远飞行。

默认值: $1 . 0 \mathsf { E } + 1 0$ 秒（基本上是永远）

detonate_below_height_agl <length-value> / detonate_below_height_msl <length-value>

当武器下降并低于指定的 AGL 或 MSL 高度时引爆。

默认值: 下降高度不是标准

detonate_above_height_agl <length-value> / detonate_above_height_msl <length-value>

当武器上升并高于指定的 AGL 或 MSL 高度时引爆。

默认值: 上升高度不是标准

detonate_below_speed <speed-value> / detonate_below_mach <Mach-number>

当武器下降且速度降低时，如果速度或马赫数低于指定值则引爆。

默认值: $0 \ : \mathsf { m } / \mathsf { s }$ （最低速度/马赫数不是标准）

detonate_on_mach_decreasing_to <Mach-number>

当武器加速时，存储峰值马赫数。在燃料耗尽后，当减速时，如果马赫数低于指定值则引爆。引爆仅在达到大于指定值的峰值马赫数后触发。

默认值: $0 \ : \mathsf { m } / \mathsf { s }$ （最低速度/马赫数不是标准）

# 基于目标接近的引爆

gross_proximity_range <length-value>

必须指定此值以进行武器-目标接近检查。此输入指定武器被认为接近目标的最小分离距离。在武器处于目标的此范围内时，将使用更精细的时间步长（参见 fine_update_interval）以提高拦截确定的准确性。

注意: 合理的值是武器平均速度的 2 到 3 倍。

hit_proximity_range <length-value>

如果启用了接近检查（gross_proximity_range 非零）且指定了 do_not_use_current_target，则表示在武器和目标的最近接近点之间的最大范围内将触发引爆。如果武器和目标在其最近接近点未通过此距离，则平台将继续而不引爆。

默认值: 100 米

use_current_target / exclusive_target_name <target-name>

如果非零，则在此指定的待机范围内，最近接近点（PCA）计算将提前终止（保险动作）。默认值为零，这会导致在 PCA 处进行保险。使用 PkTable 时建议使用一些小的待机，因为未修改的 PCA 保险几乎总是会导致 PCA 处的方位角和仰角值大于 90 度。

do_not_use_current_target

如果启用了接近检查（gross_proximity_range 非零），则指定将对哪些平台进行接近检查。选项分别是：

□ 针对平台的当前目标。  
针对指定的目标。

□ 针对任何不是发射器或未被 excluded_category 排除的平台。

在前两种情况下，当武器和目标达到其最近接近点时将发生引爆。在最后一种情况下，当潜在目标和武器达到小于 hit_proximity_range 的最近接近点时将发生引爆。

默认值: use_current_target

注意: do_not_use_current_target 可能非常耗费计算资源。谨慎使用。

coast_time_on_loss_of_target <time-value>

如果启用了 use_current_target 或 exclusive_target_name，并且现有目标丢失，则每个输入指定要执行的操作。选项分别是：

□ 在引爆前漂移指定时间（以允许目标重新获取）。  
□ 立即引爆。  
▫ 停止考虑任何接近检查（恢复到时间、高度和速度检查）。  
□ 开始考虑所有平台的接近。参见 do_not_use_current_target。

默认值: coast_time_on_loss_of_target 2 秒

excluded_category <category-name>

仅在考虑所有平台的接近时使用。此输入将排除属于 <category-name> 的所有平台。可以多次指定此命令以排除多个类别。

air_to_ground_mode

此标志将通过指定目标类型（当前目标或指定的 exclusive_target_name）的高度来提高AGL 限制的拦截值。这是为了允许武器尽可能接近目标的重心引爆，而不因地面目标的垂直高度而人为增加偏差距离。

on_intercept [ detonate halt ]

此设置允许武器平台在保险计算出拦截条件后冻结并留在模拟中。通常，平台将在拦截时引爆并删除。如果设置为“halt”，则运动将在拦截位置冻结，并且保险控制的交战对象将被中断。将由脚本或其他机制来终止（Terminate()）交战，然后将武器平台从模拟中移除。

默认值: detonate

脚本接口

WSF_WEAPON_FUSE 利用通用脚本接口和 WSF_SCRIPT_PROCESSOR 的功能，以及以下内容：

```txt
script void onweapon_detonation() ... <script> ... end_script 
```

当保险即将引爆但在评估武器杀伤力之前执行此脚本。武器交战对象（可通过PLATFORM.WeaponEngagement() 获得）已填充引爆原因和位置。

# 3.3.8. 对空目标引信 WSF_AIR_TARGET_FUSE

```txt
processor <name> WSF_AIR_TARGETFuse Platform Part Commands processor Commands WSF_WEaponFuseCommands end Processor 
```

WSF_AIR_TARGET_FUSE 是一个特殊的 WSF_WEAPON_FUSE，其默认设置适用于攻击空中目标的武器。以下是其附加的默认值：

□ use_current_target: 默认使用当前目标进行接近检查。  
update_interval: 0.5 秒。这是保险处理器的更新间隔。  
▫ gross_proximity_range: 1500 米。这是进行武器-目标接近检查的最小分离距离。

这些默认设置旨在优化空对空交战的性能和准确性。

3.3.9. 对地目标引信 WSF_GROUND_TARGET_FUSE  
```txt
processor <name> WSFGROUND_TARGET Fuse ... Platform Part Commands ... processor Commands ... ... WSF_WEapon Fuse Commands ... end Processor 
```

WSF_GROUND_TARGET_FUSE 是一个特殊的 WSF_WEAPON_FUSE，其默认设置适用于攻击地面目标的武器。以下是其附加的默认值：

▫ air_to_ground_mode: 启用空对地模式，以便武器尽可能接近目标的重心引爆。  
□ use_current_target: 默认使用当前目标进行接近检查。  
□ detonate_below_height_agl: 0.0 米。当武器下降并低于指定的 AGL 高度时引爆。  
□ gross_proximity_range: 500 米。这是进行武器-目标接近检查的最小分离距离。

这些默认设置旨在优化空对地交战的性能和准确性。

3.3.10. 资产管理器 WSF_ASSET_MANAGER  
```txt
processor <name> WSF_ASSET.'<NAME>  
WSFScriptPROCESSORCommands...  
filterdeadTracks <boolean-value>  
max_track_grouping_distance <length-value>  
maxassignments <integer>  
assignment_delay <time-value>  
decision_update_delay <time-value>  
log_status <boolean-value>  
status_settings  
subordYELLOW_timeout <time-value>  
subord_red_timeout <time-value>  
report_positionEvery <length-value>  
orEvery <time-value>  
report.statusevery <time-value>  
aggregate_unit_status <boolean-value>  
stationary_opns_only <boolean-value>  
weapon_required <boolean-value>  
require_allweapons <boolean-value>  
ew_required <boolean-value>  
tar_required <boolean-value>  
ttr_required <boolean-value>  
end.status_settings 
```

WSF_ASSET_MANAGER 是一个脚本基类，供基于 HELIOS 的资产管理模型继承。它并不作为一个独立的处理器使用，而是为资产管理模型提供所有资产管理处理器中常见的脚本功能。

脚本接口

WSF_ASSET_MANAGER 利用通用脚本接口和 WSF_SCRIPT_PROCESSOR 的功能。

资产管理器命令

filter_dead_tracks <boolean-value>: 如果为真，则在将目标纳入威胁数组之前检查目标是否存活。

默认值: False

max_track_grouping_distance <length-value>: 设置轨迹强度确定的分组距离。注意，轨迹在分组时不会合并，只是增加强度计数。

默认值:50 米

max_assignments <integer>: 设置资产的最大活动分配数。

注意: 下属分配计入此总数。

默认值:0

assignment_delay <time-value>: 设置资产管理器的分配延迟。

注意: 分配延迟发生在为具有提交权限的处理器排队传出消息之前，以及为没有提交权限的处理器处理接收消息之前。

默认值:0 秒

decision_update_delay <time-value>: 设置分配的路由。

注意: 这是一个定向消息，因此通常设置为“动态”。

默认值:0 秒

log_status <boolean-value>: 设置资产管理器的状态日志记录开关。

默认值: True

# 状态设置命令

用于定义 HELIOS 资产管理器状态设置的块。

subord_yellow_timeout <time-value>: 指定在没有状态报告的情况下等待多长时间后将下属状态设置为黄色（不可用）。

默认值:15 秒

subord_red_timeout <time-value>: 指定在没有状态报告的情况下等待多长时间后将下属状态设置为红色（不可用）。

默认值:30 秒

report_position_every <length-value>: 指定如果平台在移动，位置消息应传输的频率。

默认值: 100 米

or_every <time-value>: 指定位置消息应传输的频率。

默认值: 300 秒

report_status_every <time-value>: 指定状态消息应传输的频率。

默认值:10 秒

aggregate_unit_status <boolean-value>: 在确定是否满足绿色状态要求时，包括绿色状态的下属。

默认值: False

stationary_opns_only <boolean-value>: 要求资产静止以达到绿色状态。

默认值: False

weapon_required <boolean-value>: 要求有弹药的武器以达到绿色状态。

默认值: False

require_all_weapons <boolean-value>: 要求平台上的所有武器都有弹药以达到绿色状态。默认值: False

ew_required <boolean-value>: 需要电子战雷达以达到绿色状态。

默认值: False

tar_required <boolean-value>: 需要 TAR 雷达以达到绿色状态。

默认值: False

ttr_required <boolean-value>: 需要 TTR 雷达以达到绿色状态。

默认值: False

示例

```txt
status_settings  
    subordYELLOW_timeout 120 secs  
    subord_red_timeout 180 secs  
    report_positionevery 100 meters  
    orEvery 300 secs  
    report_status EVERY 10 secs  
    aggregate_unit_status true  
    weapon_required true  
    require_all_weapons false  
    ew_required false  
    tar_required true  
    ttr_required true  
    stationary_opns_only false  
end.status_settings  
max_assignments 10  
assignment_delay 0 secs  
decision_update_delay 0 secs  
log_status true 
```

# 3.3.11. 未分类资产管理器 WSF_UNCLASS_ASSET_MANAGER

```txt
processor <name> WSF_UNCLASS_ASSETMANAGER  
WSF_ASSETMANAGER Commands ...  
WSFScriptPROCESSORCommands...  
end Processor 
```

WSF_UNCLASS_ASSET_MANAGER 是基于 HELIOS 的 IADS C^2 资产管理模型端口的脚本类。它旨在与战斗管理器一起使用，以提供通用的 IADS 状态、轨迹和分配接口。资产管理器负责报告其自身状态、接收其下属单位的状态，并报告汇总状态。此外，资产管理器（及其子系统）执行存储在单位中的轨迹的武器到目标分配，并监控和评估现有分配。

脚本接口

WSF_UNCLASS_ASSET_MANAGER 利 用 通 用 脚 本 接 口 、 WSF_SCRIPT_PROCESSOR 和WSF_ASSET_MANAGER 的功能。

未分类资产管理器命令

未分类资产管理器模型没有增加任何超出 WSF_ASSET_MANAGER 基类所提供的功能。这意味着它继承了所有 WSF_ASSET_MANAGER 的命令和功能，但没有额外的特定命令。

这种设计使得 WSF_UNCLASS_ASSET_MANAGER 可以在不增加复杂性的情况下，利用WSF_ASSET_MANAGER 提供的所有通用功能，适用于需要标准化资产管理功能的场景。

# 3.3.12. 战斗管理器 WSF_BATTLE_MANAGER

```txt
processor <name> WSF_BATTLEMANAGER ... WSFScriptPROCESSORCommands... commit_authority <boolean-value> project Tracks_by_delays <boolean-value> project_targets_forward <time-value> by <time-value> engage_iffpermissions unknowns <boolean-value> neutrals <boolean-value> friendlies <boolean-value> hostiles <boolean-value> end_engage_iffpermissions end Processor 
```

WSF_BATTLE_MANAGER 是所有基于 HELIOS 的战斗管理器继承的脚本基类。它本身并不作为一个独立的处理器使用，而是由其他战斗管理器使用，以提供所有战斗管理器中常见的脚本功能。

WSF_BATTLE_MANAGER 脚本接口

WSF_BATTLE_MANAGER 利用通用脚本接口和 WSF_SCRIPT_PROCESSOR 的功能，并提供以下命令：

战斗管理器命令

commit_authority <boolean-value>: 设置提交权限的开关。如果关联的资产管理器未设置为过滤死亡轨迹，可能会将过时或无效的轨迹分配给武器。此外，轨迹处理器上的异常高或低的清除间隔可能导致异常的分配行为。

默认值: False

project_tracks_by_delays <boolean-value>: 设置通过分配延迟进行轨迹预测的开关，用于创建分配。

默认值: True

project_targets_forward <time-value>: 允许配置目标的前向预测时间，用于武器评估目的。注意，HELIOS 根据模型默认设置这些，但可以通过此脚本设置覆盖。

默认值:60 秒

by <time-value>: 允许配置用于武器评估目的的前向预测时间增量。  
默认值: 10 秒

交战 IFF 权限命令

任何 IFF 类型设置为 true 的值将被战斗管理器允许交战。设置为 false 的值将不被授予交战许可。

unknowns <boolean-value>   
默认值: False   
neutrals <boolean-value>   
默认值: False   
friendlies <boolean-value>   
默认值: False   
hostiles <boolean-value>   
默认值: False

战斗管理器示例

以下是一个战斗管理器的示例配置：

```txt
commit_authority true  
project Tracks_by_delays false  
engage_iffpermissions unknowns false neutrals false friendlies false hostiles true  
end_engage_iffpermissions 
```

在这个示例中，战斗管理器被设置为具有提交权限，并且不通过延迟预测轨迹。它仅允许与敌对目标交战，而不与未知、中立或友方目标交战。

# 3.3.13. 未分类战场管理器 WSF_UNCLASS_BM

```txt
processor <name> WSF_UNCLASS_BM  
WSF_BATTLEMANAGER Commands ...  
stale_asset_time <time-value>  
shot_doctrine [Shoot-1|Shoot-2|Shoot-Look-Shoot] 
```

```txt
max_firing_time <time-value>   
print_settings valid.units <boolean-value> valid_unit_details <boolean-value> invalid_unit_details <boolean-value>   
end_print_settings   
weapon_table speed_attributes <name> <speed-value> [< <= ] <speed-value> end_speed_attributes   
altitude_attributes <name> <length-value> [< <= ] <length-value> end_altitude_attributes   
weapon_rows target suf priority [<integer>] [<target type string>"Any"] [<target subtype string>"Any"] [speed attribute] [altitude attribute] [min pk] [<Al priority (integer)> <SAM priority (integer)> <Other priority (integer)>]   
endweapon_rows   
endweapon_table   
scoringFactors weapon_type <integer> weapon subtype <integer> intercept_range <integer> intercept_time <integer> pk <integer> workload <integer>   
end_scoring Factors   
end Processor 
```

WSF_UNCLASS_BM 是一个基于脚本的类，用于基于 HELIOS 的分配武器 WSPT 战斗管理器。所有针对这个战斗管理器的脚本都遵循 HELIOS 战斗管理器支持的精确脚本。

# Script Interface

WSF_UNCLASS_BM 利用通用脚本接口和 WSF_SCRIPT_PROCESSOR 的功能。它还派生自WSF_BATTLE_MANAGER，为 IADS C2 战斗管理器类提供通用功能。

# Unclass Battle Manager Commands

stale_asset_time <time-value>: 指定在多长时间后战斗管理器将认为一个友军信息过时，并且在更新之前将不再考虑进行评估。

默认值:60 秒

shot_doctrine [Shoot-1 | Shoot-2 | Shoot-Look-Shoot]: 指定在分配武器任务时使用的射击原则。

默认值: Shoot-Look-Shoot

max_firing_time <time-value>: 指定武器在战斗管理器认为其未完成并取消任务之前，参与目标的最大射击时间。

默认值: 360 秒

# Print Settings Commands

用于设置未分类战斗管理器日志记录的打印设置块：

valid_units <boolean-value>: 设置是否打印基本评估信息。

默认值: False

valid_unit_details <boolean-value>: 设置是否打印详细评估信息。

默认值: False

invalid_unit_details <boolean-value>: 设置是否打印失败的评估信息。

默认值: False

# Weapon Table Commands

用于定义 HELIOS 分配武器-WSPT 模型的武器表块：

speed_attributes … end_speed_attributes: 允许定义用户定义的速度属性助记符，以便在武器表定义中使用。

默认值: 无。需要明确声明以实现正确的武器表功能。

altitude_attributes … end_altitude_attributes: 允许定义用户定义的高度属性助记符，以便在武器表定义中使用。

默认值: 无。需要明确声明以实现正确的武器表功能。

weapon_rows … end_weapon_rows: 允许定义武器行。

□ priority: 设置目标优先级。  
□ type: 目标类型字符串。引用实现中使用了 AFSIM平台类型。字符串必须用引号（“”）括起来。匹配任何类型的通配符是关键字“Any”。  
□ subtype: 目标子类型字符串。引用实现中使用了名为 TARGET_SUBTYPE 的平台 AUX数据。字符串必须用引号（“”）括起来。匹配任何子类型的通配符是关键字“Any”。  
□ speed attribute: 此行适用的在 speed_attributes 块中定义的速度属性名称。  
▫ altitude attribute: 此行适用的在 altitude_attributes 块中定义的高度属性名称。  
□ minpk: 设置武器系统参与此目标的最低击杀概率。  
□ AIpriority: 为定义的空中拦截器（AI）设置的优先级。  
□ SAMpriority: 为定义的地对空导弹（SAM）设置的优先级。  
□ Otherpriority: 为其他类别的武器设置的优先级。

# Weapon Table Example

```txt
weapon_table
speed_attributes
    attrib slow 0 kts < 250 kts
    attrib med 250 kts < 600 kts
    attrib fast 600 kts < 2000 kts 
```

end_speed_attributes   
altitude_attributes attrib low 0 ft <1000 ft attrib med 1000 ft $<  30000$ ft attrib high 30000 ft $<  100000$ ft   
end_altitude_attributes   
weapon_rows target_ref priority 1 "UCAV""Any"med high 0.7 0 1 0 end weaponry_rows   
endweapon_table

评分因素命令

评分因素用于决定采用哪个武器系统与目标的配对。在决策过程中，优先考虑评分因素较高的配对。每个评分因素实际上是对该参数赋予的权重，可以调整以优化战斗管理器的性能。

# 参数

weapon_type <integer>:描述: 此因素影响评分计算中对武器类型的权重。

范围: 0 到 10

默认值:1

weapon_subtype <integer>:描述: 此因素影响评分计算中对武器子类型的考量。

范围: 0 到 10

默认值:1

intercept_range <integer>:描述: 此因素应用于武器拦截距离的评分过程。

范围: 0 到 10

默认值:1

intercept_time <integer>:描述: 此因素影响基于武器拦截目标所需时间的评分。

范围: 0 到 10

默认值:1

pk <integer>:描述: 此因素涉及击杀概率（Pk）在评分计算中的应用。

范围: 0 到 10

默认值:1

workload <integer>:描述: 此因素与武器的工作负荷有关，影响其在评分计算中的得分。

范围: 0 到 10

默认值:1

Scoring Factors Example   
```txt
scoring Factors weapon_type 1 weapon subtype 1 intercept_range 1 intercept_time 1 pk 1 workload 1 end_scoringFactors 
```

非密级战斗管理器处理

分配武器

非密级战斗管理器的武器分配从创建武器数组并填充武器数据开始。它为每个“Pass”构建不同的武器数组，以便仅包含满足通过标准的武器。它遍历资产数组以找到武器系统。对于找到的每个武器系统，该功能确定用户是否为武器系统设置了区域使用（如果此过程与武器系统及其直接下属相关）。它同样确定间接下属的情况。对于所有中间下属，它确定下属单位是否战备就绪（绿色）并确定中间下属是否使用区域。然后，该功能根据以下六个通过规则考虑将武器系统添加到其中一个武器数组中（如果在较早的通过中识别出有效武器，则后续通过是不必要的）：

□ Pass1：利用区域的直接下属武器（导弹交战区、战斗机交战区或干扰机交战区）。  
□ Pass2：不利用区域的直接下属武器。  
□ Pass3：所有下属武器在指挥链中有直接 C2 下属使用区域。  
□ Pass4：所有下属武器在指挥链中有任何 C2 下属（非直接）使用区域。  
▫ Pass5：所有下属武器在指挥链中没有 C2 下属（包括直接）使用区域，或武器使用区域。  
□ Pass 6：所有下属武器在指挥链中没有使用区域（在评估期间将进行武器运动学检查）。

对于每个 $\looparrowleft$ ，非密级战斗管理器将目标分配给下属系统。如果战斗管理器没有“Commit”权限，它自动具有“Delegate”权限。这意味着它可以从其指挥官接收分配并决定将轨迹分配给哪个下属单位。对于委派，它从创建轨迹/武器配对数组开始。然后遍历分配数组以找到有效的分配。分配数组由指挥权限的分配填充。如果分配过旧、不完整、已被拒绝或取消，或尚未传播，则跳过分配。对于剩余的（有效的）分配，该功能找到匹配的主轨迹。对于此主轨迹，该功能根据目标类型和子类型从 WSPT 中找到匹配的武器偏好。计算从系统到轨迹的距离和轨迹到达系统的时间（闭合时间）。闭合时间的计算假设轨迹以其速度直接向系统移动。然后，该功能遍历武器数组。它评估武器以排除没有弹药或“过时”武器的武器系统。它计算武器系统的工作负载，并通过发射时间加上分配延迟来预测轨迹。它遍历武器管理器。如果武器管理器是 SAM，如果预测轨迹在最小范围内、最大范围外或偏离首选 PK，则拒绝分配。如果武器系统是 SAM 或“其他”，如果轨迹不在武器系统的视线内，则拒绝分配。如果用户选择在 Assign Engagements Weapons Systems Preference Table 中使用区域，则如果预测轨迹在区域外，则拒绝分配。对于中间 C2 单位区域进行相同检查。如果武器管理器是 AI，则使用武器管理器 AI 过程评估交战。最后一步是更新配对记录。如果找到匹配，则进行分配。

如果处理器具有“Commit”权限，它遍历主轨迹并执行与武器委派相同的过程，结果是直接分配给武器系统的配对记录。

为了分配武器，战斗管理器遍历配对数组，计算各个武器分数并将结果存储在配对矩阵中。然后，它逐个轨迹遍历每个配对武器以找到最高的武器分数。如果过程具有“Commit”权限，它找到准备好的分配，设置分配数据，根据射击原则提交导弹数量，并更新导弹记录。如果过程仅具有“Delegate”权限，它执行与“Commit”权限相同的过程，但不提交导弹。

战斗管理器通过确保以下内容来管理现有分配：

活动分配已被分配。如果没有，CANTCO该分配。

下属在 MaxFiringTime 内向目标开火。如果没有，取消该分配。

# 计算武器分数

武器分数计算从将武器分数设置为 11 减去目标优先级开始。这意味着最高优先级目标将以 10 的分数开始，而最低优先级目标（可能有多个）将以零分开始。

然后为每个修改武器分数的评分因素运行计算。还计算一个累积变量，即因素权重之和加一。在武器类型和武器子类型的情况下，使用以下公式：

```txt
Weapon Score = Weapon Score + Scoring Factor * (11 - Factor Value) 
```

其中：

Factor Value：应用于特定因素的数值。例如，SAM 的武器类型可能有一个因素值为 1，而 AI 的武器类型可能有一个因素值为 2。

对于拦截范围评分因素，使用以下公式计算系数，范围为 0.0 到 1.0：

```txt
Intercept Range Coefficient = (Weapon Max Range - Target Slant Range) / Weapon Max Range; 
```

如果目标斜距大于武器最大范围，导致系数为负，则系数默认为 0.1。对于所有大于零的系数值，使用以下公式更新武器分数：

```c
Weapons Score = Weapons Score + Intercept Range Scoring Factor * Intercept Range Coefficient * 10 
```

对于拦截时间评分因素，使用与拦截范围评分因素相同的公式，替换闭合时间为武器最大范围，拦截时间为目标斜距，拦截时间评分因素为拦截范围评分因素。

对于工作负载评分因素，使用以下公式计算武器分数：

```txt
Weapons Score = Weapons Score + Workload Scoring Factor * Workload * 10 
```

其中工作负载由以下公式确定：

```txt
[ \text{Workload} = (\text{Max Assignments - Assignments Made}) / \text{Max Assignments} ] 
```

对于 PK 评分因素，使用以下公式计算武器分数：

```txt
Weapons Score = Weapons Score + PK Scoring Factor * PK * 10 
```