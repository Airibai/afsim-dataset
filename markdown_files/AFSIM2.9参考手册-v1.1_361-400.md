# 阶段变化命令格式

next_phase <phase-name> [if | when] <event>   
next_phase <phase-name> [if | when] <variable> [<operator> <reference-value>]

用于检测特定事件的发生。

可用事件：

▫ end_of_route：移动器指示已通过路线中的最后一个点（如果移动器正在跟随航路点）。  
▫ boost_complete：移动器指示不再推进。这通常意味着所有产生推力的阶段已被使用。  
□ stage_ignition：移动器指示当前阶段已点火。  
□ stage_burnout：移动器指示当前阶段已燃尽。  
□ stage_separation：移动器指示当前阶段已分离。  
□ on_commanded_flight_path_angle：武器的飞行路径角已达到发射计算机命令的俯仰角（如果提供）。  
□ sensor_track_initiated：本地车载传感器已建立对目标的自主跟踪。

# 变量检测格式

next_phase <phase-name> [if | when] <variable> [<operator> <reference-value>]

用于检测何时 <variable> 达到与 <reference-value> 的某种关系。

<reference-value> 格式：

□ 常量值格式：<real-value> <units>   
▫ 变量值格式：

/variable <variable-name>   
variable <variable-name> <units>

注意：

变量必须在 script_variables 块中定义，该块出现在引用变量的命令之前，并且不能出现在“阶段”块中。  
如果变量是有量纲的，则变量的值必须使用正确的单位：

□ 如果使用 /variable，则使用标准 WSF 单位。  
□ 如果使用 variable，则使用指定的 <units>。

有效运算符： $< , < = , = = , ! = , > = , >$

有效变量：

变量必须是一个双精度脚本变量，且 <variable-name> 必须在计算机的 script_variables

块中定义。

<table><tr><td>Variable</td><td>Ref-Variable-Type</td><td>Description</td></tr><tr><td>phase_time</td><td>&lt;time-value&gt;</td><td>The time (seconds) that has elapsed since the start of the phase.</td></tr><tr><td>flight_time</td><td>&lt;time-value&gt;</td><td>The time (seconds) that has elapsed since the platform was launched.</td></tr><tr><td>altitude</td><td>&lt;length-value&gt;</td><td>The current altitude (meters) of the weapon.</td></tr><tr><td>speed</td><td>&lt;speed-value&gt;</td><td>The current speed (meters/second) of the weapon.</td></tr><tr><td>vertical_speed</td><td>&lt;speed-value&gt;</td><td>The current vertical speed (meters/second) of the weapon.</td></tr><tr><td>flight_path_angle</td><td>&lt;angle-value&gt;</td><td>The current flight path angle (radians) of the weapon.</td></tr><tr><td>dynamic_pressure</td><td>&lt;pressure-value&gt;</td><td>The current dynamic pressure (Newtons/meter2) on the weapon.</td></tr><tr><td>target_altitude</td><td>&lt;length-value&gt;</td><td>The current altitude (meters) of the target.</td></tr><tr><td>target_speed</td><td>&lt;speed-value&gt;</td><td>The current speed (meters/second) of the target.</td></tr><tr><td>target_flight_path_angle</td><td>&lt;angle-value&gt;</td><td>The current flight path angle (radians) of the target.</td></tr><tr><td>closing_speed</td><td>&lt;speed-value&gt;</td><td>The closing speed (meters/second) between the weapon and the target. Positive values are closing.</td></tr><tr><td>time_to_intercept</td><td>&lt;time-value&gt;</td><td>The approximated predicted time (seconds) until the weapon and target intercept.</td></tr><tr><td>range_to_intercept</td><td>&lt;length-value&gt;</td><td>The approximate distance (meters) to the predicted point of intercept between weapon and the target.</td></tr><tr><td>target_slant_range</td><td>&lt;length-value&gt;</td><td>The slant range (meters) between the weapon and the target.</td></tr><tr><td>target-ground_range</td><td>&lt;length-value&gt;</td><td>The approximate ground range (meters) between the weapon and the target.</td></tr><tr><td>target_elevation</td><td>&lt;angle-value&gt;</td><td>The angle (radians) above or below the local horizontal plane (tangent to the Earth's surface) and the line-of-sight vector from the weapon to the target. A positive value means the target is above the local horizontal plane while a negative value indicates it is below.</td></tr><tr><td>target_azimuth</td><td>&lt;angle-value&gt;</td><td>The angle (radians) in the local horizontal plane (tangent to the Earth's surface) between the horizontal components of the weapon velocity vector and line-of-sight vector from the weapon to the target. This value is always positive.</td></tr><tr><td>los_target_elevation</td><td>&lt;angle-value&gt;</td><td>The elevation angle (radians) of the target with respect to the current orientation of the weapon.</td></tr><tr><td>los_target_azimuth</td><td>&lt;angle-value&gt;</td><td>The azimuth angle (radians) of the target with</td></tr><tr><td></td><td></td><td>respect to the current orientation of the weapon. This value is always positive.</td></tr><tr><td>los_target_angle</td><td>&lt;angle-value&gt;</td><td>The 3D angle (radians) of the target with respect to the current orientation of the weapon.</td></tr></table>

事件使用示例：

```txt
next_phase PHASE2 if end_of rout   
next_phase PHASE2 if boostcomplete   
next_phase PHASE2 if stageIgnition   
next_phase PHASE2 if stage_burnout   
next_phase PHASE2 if stage_separation   
next_phase PHASE2 when on commanded_airight_path_angle   
next_phase PHASE2 when sensor_track_initiated 
```

使用常量做引用值：

```txt
next_phase PHASE2 when phase_time > 200 sec  
next_phase PHASE2 when flight_time > 25 sec  
next_phase PHASE2 when altitude > 10000 m  
next_phase PHASE2 when speed > 500 m/s  
next_phase PHASE2 when vertical_speed > 100 m/s  
next_phase PHASE2 when target_altitude > 10000 m  
next_phase PHASE2 when target_speed > 500 m/s  
next_phase PHASE2 when closing_speed > 1000 m/s  
next_phase PHASE2 when time_to_intercept < 1 sec  
next_phase PHASE2 when range_to_intercept < 1 m  
next_phase PHASE2 when target_slant_range < 1 m  
next_phase PHASE2 when target-ground_range < 1 m  
next_phase PHASE2 when target_azimuth > 179 deg  
next_phase PHASE2 when target_elevation > 89 deg  
next_phase PHASE2 when los_target_azimuth > 179 deg  
next_phase PHASE2 when los_target_elevation > 89 deg  
next_phase PHASE2 when los_target_angle > 179 deg  
next_phase PHASE2 when altitude > 10 km 
```

使用脚本变量做引用值

In this form the value of TARGET_ALTITUDE should be in meters.   
next_phase PHASE2 when altitude $>$ /variable TARGET_ALTITUDE   
# In this form the value of TARGET_ALTITUDE should be in kilometers (km).   
next_phase PHASE2 when altitude $>$ variable TARGET_ALTITUDE km

脚本变量 TARGET_ALTITUDE 应在‘script_variables’块中定义，并在此处理器公开的脚本块之一中赋值。

WSF_P6DOF_GUIDANCE_COMPUTER 利用通用脚本接口和 WSF_SCRIPT_PROCESSOR 的功能，并支持在 WsfP6DOF_GuidanceComputer 中定义的附加脚本方法。然而，有一些从WSF_GUIDANCE_COMPUTER 继承的方法目前不被支持。

# 不支持的方法

commanded_altitude <length-value> [ msl | agl ]

指定命令的高度。通常用于爬升或下降到巡航高度并保持高度。高度参考标签（‘msl’ 或‘agl’）可以省略，省略时假定为 ‘msl’。

指定‘agl’作为高度参考是一种粗略的地形跟随实现机制。当指定‘agl’时，移动器将强制执行一个额外的约束，即始终保持在地面以上。然而，不进行前瞻性检查（仅检查平台正下方的地形高度），因此如果地形迅速上升，飞行器可能会做出非常突然的变化。

默认值：无命令高度

脚 本 命 令 ： WsfGuidanceComputer.SetCommandedAltitude 和WsfGuidanceComputer.SetCommandedAltitudeAGL

commanded_flight_path_angle <angle-value>

指定命令的飞行路径角。如果指定 from_launch_computer，则使用发射计算机产生的值（如果存在）。

通常用于产生抛物线弹道轨迹。

默认值：无命令飞行路径角

脚本命令：WsfGuidanceComputer.SetCommandedFlightPathAngle

commanded_mach <real-value> / commanded_speed <speed-value>

指定在此阶段使用的命令速度/马赫数。通常用于巡航。

默认值：无命令速度或马赫数

脚 本 命 令 ： WsfGuidanceComputer.SetCommandedSpeed 和WsfGuidanceComputer.SetCommandedMach

注意：并非所有移动器都支持此功能。使用此命令时，燃料利用可能无法正确建模。

commanded_throttle <real-value>

指定一个范围在 [0..1] 的油门因子，覆盖移动器中的油门规格。

这通常不作为命令使用。它主要存在以允许脚本调用来改变油门。

默认值：无命令油门

脚本命令：WsfGuidanceComputer.SetCommandedThrottle

allow_route_following <boolean-value>

如果为 true，计算机将在提供给相关移动器的情况下遵循路线。如果移动器没有路线，则此命令无效。常规目标点选择将在路线结束时恢复。

命令 next_phase <phase-name> at_end_of_route 可用于在遇到路线结束时切换到不同的阶段。

默认值：false

脚本命令：WsfGuidanceComputer.SetAllowRouteFollowing

这些方法和命令提供了对武器引导行为的详细控制，尽管某些功能在当前实现中不被支持。

# 3.3.31. 六自由度制导处理器 WSF_SIX_DOF_GUIDANCE_COMPUTER

```txt
processor <name> WSF SIX DOF GUIDANCE COMPUTER ... WSF GUIDANCE Computer Commands ... end Processor 
```

概述

WSF_SIX_DOF_GUIDANCE_COMPUTER 是一个通常安装在武器上的处理器，为使用WSF_SIX_DOF_MOVER 的武器提供制导。它通过 CurrentTargetTrack 提供的轨迹来表示要追踪的目标。移动器调用此处理器以请求制导更新。处理器计算所需的制导并将命令反馈给移动器。

这 是 针 对 WSF_SIX_DOF_MOVER 对 象 的 WSF_GUIDED_MOVER 专 用WSF_GUIDANCE_COMPUTER 的重新实现，预期会有类似的行为和功能。代码维护者应定期更新此类，以便在简单继承不可行的情况下与 WSF_GUIDANCE_COMPUTER 保持一致。

不支持的方法

以下方法（从 WSF_GUIDANCE_COMPUTER 继承）目前不支持：

commanded_throttle <real-value>:

指定一个范围为 [0..1] 的油门因子，覆盖移动器中的油门规范。

建议通过脚本命令飞行器的油门，而不是使用此命令。

默认值: 无命令油门。

脚本命令: WsfGuidanceComputer.SetCommandedThrottle

此处理器的设计旨在为复杂的六自由度运动提供精确的制导控制，确保武器能够有效地追踪和接近目标。

# 3.3.32. 旧的武器制导处理器 WSF_OLD_GUIDANCE_COMPUTER（弃用）

```txt
processor <name> WSF_OLD GUIDANCE Computer ... base processor commands ... ... WSF_OLD GUIDANCE Computer Commands ... end Processor 
```

WSF_OLD_GUIDANCE_COMPUTER 是 一 种 处 理 器 ， 用 于 模 拟 自 导 引 导 。 它 从track_manager 获取平台的当前目标轨迹（track），并计算出期望的垂直和横向力，以引导平台拦截目标轨迹。期望的侧向力（可能受 max_commanded_g 限制）被设置到WSF_OLD_GUIDED_MOVER 中，后者最终决定了结果轨迹。

引导模式

速度追踪（Velocity Pursuit）：

通过将速度矢量沿目标的视线方向转动来实现。由于这种引导模式不补偿目标速度，因此在对抗高速目标的空对空交战中，导弹往往会从后方追逐目标。

比例导航（Proportional Navigation）：

通过转动来使惯性视线速率为零。由于这种引导模式实时补偿目标机动，因此对于空对空机动交战来说，它几乎是理想的拦截方案。

# 默认轨迹

默认情况下，飞行轨迹将是短时间的速度追踪引导。在速度矢量大致指向目标后，将切换到比例导航。如果引导平台的速度高于目标速度，并且没有其他限制干扰，将会发生目标拦截。

# 不确定性模型

处理器包含一个简单的漂移模型来考虑自我位置的不确定性。目标位置的不确定性取决于平台当前目标轨迹的准确性。默认行为是完美的自我位置感知。可以通过time_between_GPS_fixes 和 IMU_drift_rate 关键字进行调整。

# 应用场景

这种引导处理器在现代空对空导弹中广泛应用，利用反馈机制来纠正目标机动的不准确预测和其他未建模的动态因素。通过结合速度追踪和比例导航，系统能够在不同的飞行阶段优化拦截路径，尽可能提高命中率。

WSF_OLD_GUIDANCE_COMPUTER 是一个用于模拟自导引导的处理器，提供了多种配置选项来调整导引行为。以下是各个命令的详细说明：

# 基本配置命令

guide_to_truth <boolean-value>

指定在引导计算中是使用感知的目标位置（由当前目标轨迹定义）还是实际目标位置。默认值：false

proportional_navigation_gain <float-value>

指定应用于感知惯性视线速率的增益，以将速率归零。增益值通常需要通过实验确定。默认值：1.0

velocity_pursuit_gain <float-value>

指定应用于感知偏轴目标角度的增益，以将速度矢量重新对准目标。

默认值：1.0

g_bias <float-value>

指定轨迹应如何补偿重力引起的垂直加速度。默认值为 1.0，表示沿视线的平坦轨迹。默认值：1.0

continuous_g_bias

请求在整个飞行过程中使用 g 偏置。默认行为是在水平目标距离相对于垂直下降到目标较大时才开启 g 偏置补偿。

max_commanded_g <acceleration-value>

设置引导计算机请求的最大横向转弯加速度，以模拟结构限制。

默认值： $2 5 . 0 { \mathrm { g } }$

guidance_delay <time-interval-value>

指定发射后引导请求被限制为零的时间间隔。

默认值：0.0

aspect_angle_for_pro_nav_switch <angle-value>

当速度矢量到目标视线角度低于此值时，引导算法将从速度追踪切换到比例导航。

默认值：30.0 度

omit_velocity_pursuit

强制轨迹引导仅包括纯比例导航，从飞行开始就没有速度追踪段。

omit_proportional_navigation

强制轨迹引导仅包括速度追踪，没有切换到比例导航。

# 漂移模型配置

time_between_GPS_fixes <time-duration>

指定位置更新的频率，仅在漂移率非零时使用。

默认值：5.0 分钟

IMU_drift_rate <speed-value>

指定位置感知的漂移率。

默认值：0.0（无漂移）

# 特殊引导配置

pitchover_guidance

指定武器将使用仅为执行俯仰机动而修改的比例导航引导方案。

maximum_loft_time

指定导弹使用指定的俯仰角爬升的时间。

默认值：0.0

loft_angle

指定导弹在指定的最大爬升时间内最初爬升的角度。

默认值：0.0

frequency_cutoff

指定用于计算俯仰增益的方法的多普勒频率。

默认值： $0 . 0 \mathsf { H z }$

min_nav_gain

当多普勒频移小于零时使用的最小俯仰增益。

默认值：0.0

max_nav_gain

当多普勒频移等于或大于频率截止时使用的最大俯仰增益。

默认值：0.0

nav_gain_factor

应用于计算的俯仰增益的因子。

默认值：0.0

nav_gain_slope_1

用于计算多普勒频移小于指定频率截止时的俯仰增益。

计算公式：Pitchover_gain $=$ nav_gain_slope_1 * doppler_shift $^ +$ min_nav_gain

nav_gain_slope_2

用于计算多普勒频移大于或等于指定频率截止时的俯仰增益。

计算公式：Pitchover_gain $=$ nav_gain_slope_2 * (doppler_shift - frequency_cutoff) $+ 0 . 5$

3.3.33. 消息处理器 WSF_MESSAGE_PROCESSOR  
```txt
processor <name> WSF_MESSAGEPROCESSOR   
processor Commands ...   
Platform Part Commands ...   
... WSFScript PROCESSOR Commands ...   
# Specify the parameters for handling messages to be delayed.   
queuing_method ...   
number_of_servers ...   
# Specify message selection and processing rules.   
# (May be repeated as necessary...)   
process   
# Specify the messages to be selected for this process. # (May be repeated as necessary...) select .. Message Selection Commands .. end_select   
# Specify how the selected messages are to be processed Message Processing Commands ignore_message delay_time ... 'script ... <script commands> ... end.script' ... External Link Commands ... ... Internal Link Commands ...   
end_process   
# Define the processing for messages not selected by a process block.   
default_process ignore_message delay_time ... 'script ... <script commands> ... end.script' ... External Link Commands ... 
```

```txt
... Internal Link Commands ... end_default_process   
# Define the routing to be used when the selected process (or default_process) # block does not include any routing commands.   
defaultrouting ... External Link Commands ... ... Internal Link Commands ...   
end_defaultRouting   
# NOTE: Message Processing Commands that occur outside of process and # default_process are assumed to be part of the default_process.. delay_time ... ... External Link Commands ... ... Internal Link Commands ... ignore_message   
end Processor 
```

WSF_MESSAGE_PROCESSOR 旨在通过应用用户定义的时间延迟和路由策略来管理接收到的消息流。用户可以定义处理块，指定哪些消息将应用特定的延迟和路由。

# 输入要求

处理器的输入包括：

处理块：这些块包含一个或多个选择块，用于定义要处理的消息。它们还包括指定操作的命令，例如时间延迟、路由或忽略消息。  
默认处理块：这是一个可选块，用于定义未被任何处理块选择的消息的操作。  
默认路由块：这是一个可选块，指定没有任何路由命令的消息的路由。  
队列管理器配置：用于配置队列管理器的命令，该管理器负责处理具有非零延迟时间的消息。

# 处理流程

处理接收到的消息的一般流程如下：

搜索处理块：寻找第一个适用的处理块。如果未找到，则使用 default_process 块定义的默认处理。  
忽略消息：如果消息处理指定 ignore_message，则忽略消息并停止处理。  
队列消息：如果指定了非零 delay_time，则根据 queuing_method 和 number_of_servers将消息放入处理队列。  
路由消息：一旦完成任何必要的延迟（如果未选择延迟则立即），根据需要路由消息：使用选定的处理或 default_process 块中的内部和外部链接命令（如果定义）。

▫ 如果未定义，则使用 default_routing 块中的内部和外部链接命令。

这种结构化的方法允许灵活和高效的消息处理，确保消息根据用户定义的标准和条件进行处理。

# 消息排队命令

这些命令定义了当消息需要 time_delay 时如何进行排队。

queuing_method [ first_in_first_out | last_in_first_out | none ]

指定当所有服务器都忙时，传入消息的排队方式。值为 none 表示如果没有可用的服务器，消息将被丢弃。

默认值：first_in_first_out

number_of_servers [ <integer-reference> | infinite ]

指定在任何给定时刻可以“处理中”的最大消息数量。如果接收到新消息且所有服务器都忙，则消息将根据 queuing_method 进行排队。

如果指定为 infinite（默认值），接收到的消息将在所需的时间延迟后直接转发。

默认值：infinite

# 消息选择命令

消息选择命令出现在 select 块中，指定要由它们所在的处理块中的消息处理命令处理的消息。如果处理块中的任何 select 块中指定的所有选择条件都为真，则消息将被选中进行处理。

需要注意的是，除了 sender 命令外，每个选择条件命令在给定的 select 块中最多只能出现一次。例如，如果需要选择两种不同类型的消息，则必须提供两个 select 块，每个块具有不同的类型选择器。

type <message-type>

如果提供的消息类型与消息中的类型匹配，则返回 true。标准消息类型如下：

<table><tr><td>Type String</td><td>Script Class</td></tr><tr><td>WSF_ASSOCIATION_MESSAGE</td><td>WsfAssociationMessage</td></tr><tr><td>WSF_CONTROL_MESSAGE</td><td>WsfControlMessage</td></tr><tr><td>WSF_IMAGE_MESSAGE</td><td>WsfImageMessage</td></tr><tr><td>WSF_STATUS_MESSAGE</td><td>WsfStatusMessage</td></tr><tr><td>WSF_TASK_ASSIGN_MESSAGE</td><td>WsfTaskAssignMessage</td></tr><tr><td>WSF_TASKiates_TESTMESSAGE</td><td>WsfTaskCancelMessage</td></tr><tr><td>WSF_TASK_CONTROL_MESSAGE</td><td>WsfTaskControlMessage</td></tr><tr><td>WSF_TASK_STATUS_MESSAGE</td><td>WsfTaskStatusMessage</td></tr><tr><td>WSF DropsTracks_MESSAGE</td><td rowspan="2">WsfTrackDropMessage</td></tr><tr><td>WSF DropsTracks Drops.Message(See note below)</td></tr><tr><td>WSF Tracks_MESSAGE</td><td>WsfTrackMessage</td></tr><tr><td>WSF Tracks_NOTIFY_MESSAGE</td><td>WsfTrackNotifyMessage</td></tr><tr><td>WSF Video_MESSAGE</td><td>WsfVideoMessage</td></tr></table>

# 注意事项

在 on_message 和 WSF_MESSAGE_PROCESSOR 中，可以接受 WSF_DROP_TRACK_MESSAGE

或 WSF_TRACK_DROP_MESSAGE 作为 WsfTrackDropMessage 的有效处理程序。当 WSF 创建 时 ， 与 WsfTrackDropMessage 关 联 的 字 符 串 类 型 被 混 淆 地 称 为WSF_DROP_TRACK_MESSAGE 而不是 WSF_TRACK_DROP_MESSAGE。在某个时候，字符串类型将被更改以保持一致，但在此期间，在指定的上下文中可以接受这两种形式。

subtype <message-subtype>

如果提供的消息子类型与消息中的类型匹配，则返回 true。这用于精确匹配消息的特定子类型。

sensor_name <sensor-name>

如果消息是 WSF_TRACK_MESSAGE、WSF_IMAGE_MESSAGE 或 WSF_VIDEO_MESSAGE，并且提供的传感器名称与消息中的传感器名称匹配，则返回 true。这用于识别来自特定传感器的消息。

sensor_type <sensor-type>

如果消息是 WSF_TRACK_MESSAGE、WSF_IMAGE_MESSAGE 或 WSF_VIDEO_MESSAGE，并且提供的传感器类型与消息中的传感器类型匹配，则返回 true。这用于识别特定类型的传感器消息。

sensor_mode <sensor-mode>

如果消息是 WSF_TRACK_MESSAGE、WSF_IMAGE_MESSAGE 或 WSF_VIDEO_MESSAGE，并且提供的传感器模式与消息中的传感器模式匹配，则返回 true。这用于识别传感器的工作模式。

system_name <system-name>

如果消息是 WSF_STATUS_MESSAGE，并且提供的系统名称与消息中的系统名称匹配，则返回 true。这用于识别来自特定系统的状态消息。

sender commander | peer | subordinate | self

如果消息的发送者是指定的平台之一（如指挥官、同级、下属或自身），则返回 true。此命令可以重复使用，以构建可接受的发送者集合。如果任何一个 sender 命令返回 true，则返回值为 true。

script … script commands … end_script

定义一个脚本，如果消息被选中，则返回 true。脚本变量 MESSAGE 指代当前消息。这允许用户编写自定义逻辑来选择消息。

# 消息处理命令

在消息处理系统中，以下命令用于定义如何处理消息：

delay_time <random-time-reference>

指定消息在处理前应延迟的时间。这个参数是一个 <random-time-reference>，因此可以为每个接收到的消息指定一个延迟的分布。

默认值：delay_time 0 sec（无延迟）

例如，在一些消息队列系统中，如 AmazonSQS，可以使用延迟队列来推迟新消息的传递，具体延迟时间可以根据需要配置。

ignore_message

指示消息应被忽略。

默认值：false（消息将被处理）

script … script commands … end_script

定义一个脚本，将被调用来“处理”消息。脚本变量 MESSAGE 指代当前消息。这类似于

WSF_SCRIPT_PROCESSOR 中 on_message 块内的脚本块。

注意：这种形式的脚本命令（无返回类型、名称和参数列表）仅允许在 process 或default_process 块内。出现在这些块之外的脚本命令被视为正常的脚本定义，必须包括返回类型、名称和参数列表。

# 外部链接命令

这些命令用于指定消息的路由到外部接收者（即其他平台）。这部分内容没有具体的细节提供，但通常涉及到如何将消息从一个系统传递到另一个系统，可能涉及网络配置和协议设置。

外部链接命令适用于选择使用 WSF 外部链接功能的平台部件。外部链接功能提供了将消息路由到离板目的地的设施。这些可以通过使用指挥官/下属/同级关系、定义和加入通信组或直接寻址来实现。

report_to [ commander | peers | subordinates ] via <xmtr-name> [ to <rcvr-name> ]   
■ external_link [ commander | peers | subordinates ] via <xmtr-name> [ to <rcvr-name> ]

指定消息在默认指挥链上的预期接收者。此命令可以多次指定，以便将消息路由到多个接收者集。

▫ <xmtr-name> 是平台上具有传输能力的通信设备的名称。此参数是必需的，因为通信必须存在且不能含糊不清。  
▫ <rcvr-name> 是接收平台上具有接收能力的通信设备的名称。如果未指定，则假定目标接收通信设备的名称与 <xmtr-name> 提供的名称相同。

report_to command_chain <cmd-chain-name> [ commander | peers | subordinates ] via <xmtr-name> [ to <rcvr-name> ]   
external_link command_chain <cmd-chain-name> [ commander | peers | subordinates ] via <xmtr-name> [ to <rcvr-name> ]

与前面的版本类似，但适用于指定的指挥链而不是默认指挥链。

report_to platform <platform-name> comm <comm-name> via <xmtr-name>   
external_link platform <platform-name> comm <comm-name> via <xmtr-name>

使用其各自的名称指定唯一的平台和通信对象作为接收者。像所有外部链接命令一样，此命令可以多次使用。

report_to address <address> via <xmtr-name>   
external_link address <address> via <xmtr-name>

通过指定的地址指定接收者。AFSIM 中的每个通信对象都被分配了一个地址，可以是动态的或由用户输入的。如果用户输入指定了这样的地址，则可以在此上下文中使用它来识别外部链接的接收者。

除了上述常规用例外，提供的地址可以是广播或多播地址。假设传输和接收通信具有这些能力，任何通过外部链接发送的消息将使用这些传输方法而不是标准单播传输。这也允许支持和使用具有外部链接的特殊寻址方案。任何正确定义的 AFSIM 通信框架扩展（通过协议使用和保留寻址）都可以以这种方式使用。

report_to_group <group-name> via <xmtr-name>

指定给定组名的通信对象成员是该设备发送的消息的预期接收者。此命令可以多次指定，以便将消息路由到多个组。

▫ <xmtr-name> 是平台上具有传输能力的通信设备的名称。此参数是必需的，因为通

信必须存在且不能含糊不清。在当前实现中，接收设备的通信名称必须与此相同。

注意：平台和非通信平台部件可以是组的成员，但是，report_to_group 命令将默默忽略任何不是通信的成员。

clear_external_links

移除由 external_link 或 report_to 命令定义的所有当前定义的外部链接。如果想要在某些修改的情况下重用现有平台定义，这很有用。

debug_external_links

启用与外部链接的内部处理相关的各种消息。此命令应在任何其他外部链接命令之前，以确保所有调试输出都为解析的输入命令发出。

这些命令提供了灵活的机制来管理消息的外部路由，确保系统能够根据特定的通信需求和网络配置有效地传递消息。

# 内部链接命令概述

内部链接命令用于指定消息路由到“车载”接收者（即同一平台上的处理器）。

clear_internal_links

移除由 internal_link 或 processor 命令定义的所有当前定义的内部链接。如果想要在某些修改的情况下重用现有平台定义，这很有用。

internal_link <platform-part-name>   
processor <platform-part-name>

指定从该对象发出的消息将被路由到同一平台上的指定平台部件对象。此命令可以多次指定，以便将消息路由到多个接收者。

<platform-part-name> 可以是以下之一：

□ 平台上的处理器名称。  
□ 平台上的通信设备名称。  
□ 平台上的传感器设备名称。  
□ 字符串 mover，表示接收者是平台上的移动对象。

字符串 fuel，表示接收者是平台上的燃料对象。

当前，接收者是处理器的第一种形式是唯一使用的形式。目前，由未分类的 WSF 核心实现的平台部件不支持接收消息，因此链接到它们不会执行任何有用的功能。

这些命令提供了一种机制来管理消息在平台内部的路由，确保消息能够在同一平台的不同部件之间有效传递。

# 3.3.34. 图像处理器 WSF_IMAGE_PROCESSOR

```txt
processor <name> WSF_IMAGEPROCESSOR processor Commands ... Platform Part Commands ... ... External Link Commands ... ... WSF_MESSAGEPROCESSOR Commands ... ... WSFScriptPROCESSORCommands ... coast_time ... filter...end_filter reports_velocity 
```

```txt
reports_side  
reports_type  
reports_bearing_elevation  
message_length...  
messagepriority...  
include_unstable_covariance...  
include_unstable_residual_covariance...  
target_recognition...  
...Target Recognition Commands...  
#Script Interface  
on_initiage ...end_on_initiage  
on_initiage2..end_on_initiage2  
on_update ...end_on_update  
script_variables ...end Script_variables  
scripts...end.script  
...Other Script Commands...  
end Processor 
```

WSF_IMAGE_PROCESSOR 概述

WSF_IMAGE_PROCESSOR 从成像传感器（如 WSF_EOIR_SENSOR 或 WSF_SAR_SENSOR）接收图像数据并生成轨迹。这提供了一种简单的能力来模拟分析员查看图像并生成可操作的信息。可以使用 WSF_MESSAGE_PROCESSOR 的功能通过延迟接收传入的图像消息来模拟处理延迟。

典型使用结构

在平台定义中，WSF_IMAGE_PROCESSOR 通常用于以下结构：

```txt
platform_type ...
sensor eoir WSF_EOIR_SENSOR
...
# 将图像转发到 'imageproc'
internal_link image_proc
endSENSOR
processor image_proc WSF_IMAGEPROCESSOR
...
# 将提取的 'tracks' 转发到 'track procure'
internal_link track_mgr
end Processor 
```

```txt
processor track_proc WSFTRACKPROCESSOR  
...  
#隐式地从' image_proc'获取轨迹并更新trackmanager  
end Processor  
end platform_type 
```

# 接受的消息类型

▫ WSF_IMAGE_MESSAGE：来自 WSF_SAR_SENSOR 在“spot”模式下操作的静态图像。  
□ WSF_VIDEO_MESSAGE：来自 WSF_EOIR_SENSOR 或 WSF_SAR_SENSOR 在“strip”模式下操作的视频流的单帧。

每个上述消息都包含一个 WsfImage 对象，反映了图像中可见的对象。处理器然后为图像中的每个对象创建或更新轨迹。

# 静态图像处理

对于静态图像，处理过程如下：

1. 为图像中的每个对象创建一个新的临时轨迹，并分配新的轨迹 ID。  
2. 将轨迹中的报告位置设置为图像中的“测量”位置。  
3. 将轨迹中的报告速度设置为零。  
4. 如果需要，设置报告的类型和阵营。  
5. 发送包含新轨迹的 WSF_TRACK_MESSAGE。

注意，每个静态图像中的每个对象都会获得一个唯一的轨迹 ID，不会保留关于以前处理的静态图像的记忆。

# 视频流处理

对于视频流，以下过程针对图像中的每个对象重复：

1. 如果对象没有现有轨迹，则创建轨迹，并在需要时启动过滤器。  
2. 如果定义了过滤器：

□ 使用图像中对象的“测量”位置更新过滤器。  
使用过滤器的位置信息和速度估计更新轨迹。  
□ 更新轨迹的状态和残差协方差（在过滤器未“成熟”时可能会抑制）。

3. 如果未定义过滤器：

□ 使用图像中对象的“测量”位置更新轨迹。  
如果指定了 reports_velocity，则使用与对象关联的平台的真实速度更新轨迹。

4. 如果需要，设置报告的类型和阵营。

5. 发送包含新或更新轨迹的 WSF_TRACK_MESSAGE。

在处理完图像中的所有对象后，旧轨迹将被清除。任何自上次更新以来超过 coast_time的轨迹将被清除，并发送 WSF_DROP_TRACK_MESSAGE。

# 目标识别

如果启用了 target_recognition 标志，WSF_IMAGE_PROCESSOR 将尝试基于评估图像中的像素数量和相关的 Johnson 标准方程进行目标检测、识别和分类。

# 注意事项

仅 WSF_IMAGE_MESSAGE 和 WSF_VIDEO_MESSAGE 消息类型由 WSF_IMAGE_PROCESSOR处理。所有其他类型的传入消息将被丢弃。

# 轨迹管理命令

coast_time <time-value>

指定在更新之间可能经过的最大时间，超过此时间轨迹将被丢弃。轨迹仅在接收到包含对象的消息时进行评估。

默认值：0 秒（无漂移时间）

# 过滤器命令

filter <filter_type> <filter_parameters> end_filter

过滤器用于从传入的视频流中生成平滑的位置和速度估计。<filter-type> 可以是预定义的过滤器类型之一或从这些类型派生的过滤器，参见：4.5.4 滤波器 filter 。

默认值：无过滤器

注意：过滤器不应用于静态图像。

报告选项

reports_velocity

指示是否在生成的轨迹中报告速度。此命令仅适用于输入为视频流且未定义过滤器的情况。在以下情况下将始终报告速度：

如果定义了过滤器，并且接收到足够的更新以生成可靠的速度。

对于静态图像，将报告速度为零。

reports_type

指示是否在生成的轨迹中报告“类型”。

默认值：不报告“类型”。

reports_side

指示是否在生成的轨迹中报告“阵营”。

默认值：不报告“阵营”。

reports_bearing_elevation

指示轨迹是否应填充方位角和仰角而不是位置信息。

注意：此功能不应与过滤器一起使用。

默认值：报告位置而不是方位角和仰角。

# 消息配置

message_length <data-size-value>

指定从图像创建的轨迹消息的逻辑长度。

默认值：0（使用从 message_table 派生的值，参见：4.14 消息表 message_table ）

message_priority <integer-priority>

指定从图像创建的轨迹消息的优先级。

默认值：0（使用从 message_table 派生的值，参见：4.14 消息表 message_table ）

# 其他选项

include_unstable_covariance <boolean-value>

include_unstable_residual_covariance <boolean-value>

当使用过滤器时，状态协方差和残差协方差在初始创建期间以及可能在一两个更新中不

可靠。当这些值为 false（默认值）时，这些不可靠的值不会传递到输出轨迹。

默认值：false

target_recognition <boolean-value>

启用此处理器的目标识别功能，用于目标检测、分类和识别。参见：3.3.34.1 目标识别命令 Target Recognition Commands。

脚本接口

WSF_IMAGE_PROCESSOR 利 用 通 用 脚 本 接 口 、 WSF_MESSAGE_PROCESSOR 和WSF_SCRIPT_PROCESSOR 的功能。这些接口允许用户编写自定义脚本来处理和分析图像数据。

# 3.3.34.1.目标识别命令 Target Recognition Commands

```txt
average Aspect_ratio ...   
detectionscene_analysis_factor ...   
classificationscene_analysis_factor ...   
identificationscene_analysis_factor ...   
minimumDetectionpixel_count ...   
minimum_classificationpixel_count ...   
minimum_identificationpixel_count ...   
detection_delay_time ...   
classification_delay_time ...   
identification_delay_time ...   
transition_coast_time ...   
detection_coast_time ...   
classification_coast_time ...   
identification_coast_time ... 
```

# 目标识别概述

在 WSF_IMAGE_PROCESSOR 中，当 target_recognition 标志设置为 true 时，启用目标识别功能。在此模式下，处理器尝试检测、分类和/或识别当前评估图像中的所有“对象”（平台）。这些决策基于对象平台占据的像素数量，使用以下 Johnson 标准方程：

# 检测标准

对象被声明为“检测到”，当满足以下条件时：

对象占据的像素数量达到 minimum_detection_pixel_count 指定的数量。  
对象通过 Johnson 标准的“检测”标准。  
▪ 对象满足这两个条件的时间至少达到 detection_delay_time 指定的最短时间。

# 分类标准

对象被声明为“已分类”，当满足以下条件时：

对象已经通过“检测到”状态。  
对象占据的像素数量达到 minimum_classification_pixel_count 指定的数量。  
对象通过 Johnson 标准的“分类”标准。

对象满足后两个条件的时间至少达到 classification_delay_time 指定的最短时间。

# 识别标准

对象被声明为“已识别”，当满足以下条件时：

对象已经通过“已分类”状态。  
对象占据的像素数量达到 minimum_identification_pixel_count 指定的数量。  
对象通过 Johnson 标准的“识别”标准。  
对象满足后两个条件的时间至少达到 identification_delay_time 指定的最短时间。

# 轨迹更新

当一个对象被声明为“检测到”时，会通过内部链接发出代表该对象的轨迹。只要从成像传感器接收到更新，轨迹将继续被更新和发出。以下附加信息将包含在轨迹中以指示当前状态：

检测状态：指示对象当前已达到的识别状态（检测到、已分类、已识别）。

像素占用信息：对象在图像中占据的像素数量。  
延迟时间信息：对象在特定状态下所需的最短时间。

<table><tr><td>State</td><td>AuxDataDouble(&quot;CLASSIFIED&quot;)</td><td>AuxDataDouble(&quot;IDENTIFIED&quot;)</td><td>Type()</td></tr><tr><td>DETECTED</td><td>-1</td><td>-1</td><td>&quot;UNKNOWN&quot;</td></tr><tr><td>CLASSIFIED</td><td></td><td>-1</td><td></td></tr><tr><td>IDENTIFIED</td><td></td><td></td><td></td></tr></table>

在 WSF_IMAGE_PROCESSOR 中，aux_data 变量 CLASSIFIED 和 IDENTIFIED 表示对象最近一次被分类为该状态的时间。如果对象不在该状态，则其值为 -1。

# 实施注意事项

状态不可逆：在当前实现中，一旦对象达到某个状态（如检测到、已分类或已识别），它将不会被重置为较低的状态。这意味着一旦对象被标记为“已分类”或“已识别”，即使条件不再满足，它也不会自动降级到“检测到”或“未检测到”状态。

用户责任：用户需要检查数据并确定信息是否可用。这意味着在使用这些状态信息时，用户应根据具体应用场景和需求来判断数据的有效性和可靠性。

# 识别参数

average_aspect_ratio <real-reference>

定义在将伪图像中的原始像素计数转换为线对数时使用的平均纵横比。如果 AR 是此命令定义的平均纵横比，而 PC 是伪图像中对象的原始像素计数，则线对数 LP 定义为：

$$
L P = \frac {\sqrt {P C / A R}}{2}
$$

默认值：4.0

# 场景分析因子

detection_scene_analysis_factor <real-reference>   
classification_scene_analysis_factor <real-reference>   
identification_scene_analysis_factor <real-reference>

定义 Johnson 标准方程中用于检测、分类或识别的“场景分析因子”（SAF）。方程为：

$$
P (L P) = \frac {(L P / S A F) ^ {2 . 7 + 0 . 7 (L P / S A F)}}{1 + (L P / S A F) ^ {2 . 7 + 0 . 7 (L P / S A F)}}
$$

其中 LP 是线对数，SAF 是适当的场景分析函数。

默认值：检测：1.0，分类：4.0，识别：6.4

# 最小像素计数

minimum_detection_pixel_count <real-reference>   
minimum_classification_pixel_count <real-reference>   
minimum_identification_pixel_count <real-reference>

定义对象在图像中必须占据的最小像素数量，以便可能被检测、分类或识别。对象必须通过像素计数测试和 Johnson 标准测试才能达到给定状态。

默认值：0

# 延迟时间

detection_delay_time <time-reference>

定义对象必须满足“检测”标准的时间量，直到其被声明为“检测到”。在延迟时间内，不满足“检测”标准的检测将导致状态重置为“未检测到”，除非定义了 transition_coast_time。

默认值：0 秒

classification_delay_time <time-reference>

定义对象必须满足“分类”标准的时间量，直到其被声明为“已分类”。在延迟时间内，不满足“分类”标准的检测将导致状态重置为“检测到”或“未检测到”（取决于失败检测的质量），除非定义了 transition_coast_time。

默认值：0 秒

identification_delay_time <time-reference>

定义对象必须满足“识别”标准的时间量，直到其被声明为“已识别”。在延迟时间内，不满足“识别”标准的检测将导致状态重置为“已分类”、“检测到”或“未检测到”（取决于失败检测的质量），除非定义了 transition_coast_time。

默认值：0 秒

# 漂移时间

1 transition_coast_time <time-reference>

定义对象在状态之间的过渡期间（由 detection_delay_time、classification_delay_time 和identification_delay_time 定义）可以“漂移”而不接收到“可接受检测”的时间量。“可接受检测”是至少满足目标状态检测标准的检测。

默认值：0 秒

detection_coast_time <time-reference>   
classification_coast_time <time-reference>   
identification_coast_time <time-reference>

定义对象在没有接收到不满足该状态 Johnson 标准的检测的情况下可以保持在状态中的时间量。

默认值：0 秒

注意：这目前是一种调查能力，不影响生成的轨迹。

这些命令提供了详细的配置选项，以便在图像处理中实现精确的目标识别和状态管理。

# 3.3.35. 相交处理器 WSF_INTERSECT_PROCESSOR

```txt
processor <name> WSF_INTERSECTPROCESSOR processor Commands .. Platform Part Commands .. define_offset ... intersect_shell ...   
end Processor 
```

WSF_INTERSECT_PROCESSOR 允许在模拟过程中查询称为交叉网格的三维表示，以确定几何信息。这些查询完全在模拟中进行，因此无需使用单独的可视化系统。

目前，交叉处理器用于确定高能激光与目标交互时的交叉几何、遮挡和材料代码（参见3.8.3 激光武器 WSF_LASER_WEAPON）。未来，这种能力可能会扩展，以纳入其他功能，如LADAR 图像形成。为了启用这些计算，处理器必须放置在目标的 platform_type（或平台实例）定义中。例如：

```txt
//su-37平台类型示例  
//一旦定义了交叉处理器，  
//可以对目标座舱盖和/或IRST进行几何查询。  
platform_type su-37 WSF_PLATFORM  
...  
processor intersect WSF_INTERSECTPROCESSOR  
define_offset CANOPY  
3.461642 m  
0.000184 m  
-0.943480 m  
define_offset IRST  
5.138014 m  
0.000005 m  
-0.629733 m  
intersect_grid../meshes/su37.imesh  
end Processor  
...  
endplatform_type
```

# 命令说明

define_offset <string-value> <length-value> <length-value> <length-value>

定义与目标感兴趣区域相关的交叉网格上的偏移名称和位置（参见上面的示例）。这允许用户指定特定的目标区域，以便在模拟中进行几何查询。

intersect_mesh <string-value>

定义与此处理器关联的交叉网格文件。该文件包含目标的三维几何信息，用于模拟中的交叉查询。

# 应用场景

WSF_INTERSECT_PROCESSOR 的主要应用是模拟高能激光与目标的交互，通过精确的几何查询来确定激光的影响点和路径。这种处理器的设计使其能够在复杂的三维环境中进行精确的物理模拟，支持更复杂的武器系统和传感器的开发。

3.3.36. LINK16 处理器 WSF_LINK16_COMPUTER  
Link 16 和 Tadil-J 简介  
```txt
processor <name>WSF_LINK16_COMPUTER  
... processor Commands ...  
... Platform Part Commands ...  
... External Link Commands ...  
c2 ...  
callsign ...  
comm ...  
ignore_surveillance ...  
output_dis ...  
output_wsf ...  
decimal_track_number ...  
track_number ...  
octal_track_number ...  
iff_colormapped ...  
end_iff_colormapped  
# Message Processors  
message Processor <name> <type>  
...  
end_message Processor  
edit message Processor <name>  
...  
end_message Processor  
delete <name>  
end Processor 
```

WSF_LINK16_COMPUTER 是一个处理器，用于处理发送和接收 Link16 - Tadil-J 消息。Tadil-J 消息可以发送到模拟中的另一个平台，或者通过 DIS 发送到另一个应用程序。默认情 况 下 ， 该 处 理 器 仅 接 收 消 息 。 要 发 送 消 息 ， 必 须 将 消 息 处 理 器 添 加 到WSF_LINK16_COMPUTER 中。

要使 Link-16 计算机正常工作，必须与 WSF_JTIDS_TERMINAL 一起使用。

Link16，也称为 TADIL-J，是一种基于 TDMA 的安全、抗干扰、高速数字数据链路，工

作在 960-1215 MHz 频段内。

它支持战场中的战术和作战数据、语音通信、图像和导航信息的实时传输。

Link16 是一个集成的通信、导航和识别（ICNI）系统，旨在交换监视和指挥控制信息。

TADIL-J 是由美国军事标准（MIL-STD）6016 定义的标准化 J 系列消息系统，北约称之为 Link 16。

通过这些功能，Link16 在现代军事通信中扮演着关键角色，确保信息的安全和高效传输。

以下是用于配置和操作 WSF_LINK16_COMPUTER 的命令及其功能：

c2 <boolean-value>

指定平台是否为 C-2 平台。这用于填充一些 Tadil-J 字段。

callsign <callsign>

指定平台的呼号，用于填充一些 Tadil-J 字段。

comm <comm-name>

指定用于通信的 WSF_JTIDS_TERMINAL 的名称。

ignore_surveillance <boolean-value>

指定此处理器是否应将 J3 系列消息处理为 WsfTrack，以填充轨迹管理器。

默认值：true

output_dis <boolean-value>

确定使用此处理器发送的消息是否也通过 DIS 发送。

默认值：no

output_wsf <boolean-value>

确定使用此处理器发送的消息是否发送到其他 WSF 平台。如果 DIS 输出是主要目标，将其设置为 no 可以减少 Link-16 的开销。

默认值：yes

decimal_track_number <integer-value>   
指定使用此处理器发送消息的源轨迹编号。必须在范围 (0, 32767) 内。  
track_number <octal-integer-value>   
octal_track_number <octal-integer-value>

使用八进制整数指定使用此处理器发送消息的源轨迹编号。必须在范围 (00, 077777)内。

iff_color_mapping … end_iff_color_mapping

定 义 身 份 类 型 到 颜 色 的 映 射 。 身 份 类 型 必 须 是 以 下 之 一 ： pending, unknown,assumed_friend, friend, neutral, suspect, hostile, undefined。

```python
iff_mapping hostile red end_iff.mapping 
```

message_processor <name> <type>

向 Link-16 计算机添加消息处理器。

```txt
(type> 
```

类 型 可 以 是 以 下 之 一 ： PPLI, SURVEILLANCE, WEAPONS_COORDINATION,NETWORK_ENABLED_WEAPON, SYSTEM_STATUS, SCRIPTED

# 消息处理器 Message Processors

为了配置 Link-16 计算机以发送消息，必须添加消息处理器。消息处理器类似于包含在Link-16 计算机内的 WSF 处理器。可以使用 message_processor 命令的变体来添加、删除或修改消息处理器。正如之前提到的，必须在平台上设置一个 WSF_JTIDS_TERMINAL 才能使用 Link-16 计算机。对于每个消息处理器，必须配置一个独特的 SlotGroupCommands。

```txt
message Processor .. command_chain .. send_interval ... script void on_send_X_Y(WsfTadilJX_YI aMessage) ..script commands .. endScript # Slot Parameters network .. npg .. slot_number .. msec .. tsec ..   
end_message处理器 
```

command_chain <command-chain-name>

使用 JTIDS Terminal 时：

该命令指定用于接收和发送消息的命令链。每个消息处理器必须指定一个命令链。

每个命令链必须链接到 WSF_JTIDS_TERMINAL 上的一个独特的 Slot Group Commands。这定义了槽组与通过槽组发送和接收的消息之间的映射。

注意：此命令是每个消息处理器所必需的。

使用其他通信设备时：

该命令指定用于接收和发送消息的命令链。

如果 DIS 输出是主要关注点，可以安全地忽略此命令。

send_interval <time-value> / send_interval rrn <rrn-number>

□ <time-value>：

指定每条发送消息之间的时间间隔。

□ rrn <rrn-number>：

可以使用标准复发率编号设置发送间隔。以下是标准复发率编号及其对应的时间间隔：

<table><tr><td>rrn</td><td>interval</td></tr><tr><td>1</td><td>384 seconds</td></tr><tr><td>2</td><td>192 seconds</td></tr><tr><td>3</td><td>96 seconds</td></tr><tr><td>4</td><td>48 seconds</td></tr><tr><td>5</td><td>24 seconds</td></tr><tr><td>6</td><td>12 seconds</td></tr><tr><td>7</td><td>6 seconds</td></tr><tr><td>8</td><td>3 seconds</td></tr><tr><td>9</td><td>1.5 seconds</td></tr><tr><td>10</td><td>0.75 seconds</td></tr><tr><td>11</td><td>0.375 seconds</td></tr></table>

script void on_send_X_Y(WsfTadilJX_YI aMessage) … end_script

如果定义了这种格式的脚本，则每当此消息处理器发送消息时，都会执行该脚本。主要用途是通过更改字段值在发送前自定义消息。

示例：设置每条发送消息中的 flight-leader 字段：

```c
script void on_send_2_2(WsfTadilJ2_21 aMessage)  
aMessage.IsFlightLeader(true);  
end_script 
```

Slot 参数（仅在不使用 WSF_JTIDS_TERMINAL 时使用）

这些参数用于填充传出 JTIDS DIS PDU 的头信息，仅在不使用 WSF_JTIDS_TERMINAL 时参考。

network <integer-value>JTIDS 网络编号，范围 [0, 127]。

默认值：0

npg <integer-value>网络参与，范围 [0,512]。

默认值：0

slot_number <integer-value>打包到 JTIDS 标头中的槽号。通常可以忽略此值。

默认值：0

msec <integer-value>JTIDS MSEC 值，范围 [0, 127]。

默认值：0

tsec <integer-value>JTIDS TSEC 值，范围 [0, 127]。

默认值：0

PPLI (Precise Participant Location and Identification) 消息处理器PPLI 消息处理器类型增加了为本地平台发送 PPLI 消息的能力。

```txt
message Processor <name> PPLI ... Message Processors ... environment ... 
```

```txt
land_or_point... end_message Processor 
```

environment [air | surface | subsurface | land]

用于明确指定要发送的 PPLI 类型。如果未指定，将使用平台的移动类型来确定要发送的消息类型。

<table><tr><td>Category</td><td>Message type to send</td><td>Default value when using</td></tr><tr><td>air</td><td>J2.2 - WsfTadiIJ2_2I</td><td>WSF_AIR_MOVER</td></tr><tr><td>surface</td><td>J2.3 - WsfTadiIJ2_3I</td><td>WSF_SURFACE_MOVER</td></tr><tr><td>subsurface</td><td>J2.4 - WsfTadiIJ2_4I</td><td>WSF_SUBSURFACE_MOVER</td></tr><tr><td>land</td><td>J2.5 - WsfTadiIJ2_5I</td><td>WSFGROUND_MOVER</td></tr></table>

land_or_point [point | land]

用于在未设置 environment 命令且使用平台的移动类型来确定要发送的消息类型时，明确指定要发送的陆地 PPLI 类型。

<table><tr><td>Category</td><td>Message type to send</td><td>Default value when using</td></tr><tr><td>point</td><td>J2.5 - WsfTadiIJ2_5I</td><td>WSFGROUND_MOVER</td></tr><tr><td>land</td><td>J2.6 - WsfTadiIJ2_6I</td><td></td></tr></table>

SURVEILLANCE 消息处理器

SURVEILLANCE 消息处理器增加了为监视轨迹发送 J.3 系列消息的能力。具体的消息类型由轨迹的空间域决定。

```txt
message Processor <name> SURVEILLANCE ... Message Processors ... environment ... ignore_reporting_responsibility ... maximum_send_interval ... send_non SENSORreports... suppressdead_targets... suppress_domain .. suppresssensor... track_number_range...   
end_message_processors 
```

send_interval 默认值：0.25 秒  
environment [air | surface | subsurface | land | space]

指定在选择要发送的轨迹消息类型时使用的空间域。此值仅在轨迹的空间域未知时使用。

<table><tr><td>Spatial domain</td><td>Message type to send</td></tr><tr><td>air</td><td>J3.2 - WsfTadilJ3_2I</td></tr><tr><td>surface</td><td>J3.3 - WsfTadilJ3_3I</td></tr><tr><td>subsurface</td><td>J3.4 - WsfTadilJ3_4I</td></tr><tr><td>land</td><td>J3.5 - WsfTadiJ3_5I</td></tr><tr><td>space</td><td>J3.6 - WsfTadiJ3_6I</td></tr></table>

ignore_reporting_responsibility <boolean-value>

如果为 true，则忽略轨迹的报告责任规则。

默认值：false

maximum_send_interval <time-value>

指定队列未修改轨迹以发送的间隔。修改后的轨迹会立即排队。

注意：实际发送速率受 send_interval 限制。

send_non_sensor_reports <boolean-value>

指定是否应发送主轨迹列表中的非传感器（融合）轨迹或原始传感器轨迹。

默认值：true（“原始”传感器轨迹将不被报告）

suppress_dead_targets <boolean-value>

如果为 true，则抑制为完全损坏或不再在模拟中的平台发送 J3 消息。

默认值：true

suppress_domain [air | surface | subsurface | land | space]

如果指定，则不会通过 Link-16 发送来自给定域的轨迹。

suppress_sensor <string-value>

如果指定，则不会通过 Link-16 发送来自指定传感器的报告。

注意：此输入仅在 send_non_sensor_reports 为 false 时有效。

track_number_range <first-track-number> <last-track-number>

指定发送监视轨迹时使用的轨迹编号范围。轨迹编号格式为 XXOOO，其中 X 是 0-7 或A-Z，O 是 0-7。

WEAPONS_COORDINATION 消息处理器

```txt
message Processor <name> WEAPONS_COORDINATION ... Message Processors ... end_message Processor 
```

该消息处理器用于 J9 接口，允许用户配置与武器协调相关的消息。

NETWORK_ENABLED_WEAPON 消息处理器

```txt
message Processor <name> NETWORK_ENABLED WEAPON ... Message Processors ... end_message Processor 
```

该消息处理器用于 J11 接口。J11 消息通过这些部分之一发送（如果存在），允许用户配置槽参数。

SYSTEM_STATUS 消息处理器

SYSTEM_STATUS 消息处理器类型增加了发送 J.13 系列消息的能力。

```txt
message Processor <name> SYSTEM_STATUS ... Message Processors ... reportweaponquantity_1... 
```

```txt
reportweaponquantity_2... reportweaponquantity_3... end_message Processor 
```

<table><tr><td>Category</td><td>Message type to send</td><td>Default value when using</td></tr><tr><td>air</td><td>J13.2 - WsfTadiJ13_2I</td><td>WSF_AIR_MOVER</td></tr><tr><td>surface</td><td>J13.3 - WsfTadiJ13_3I</td><td>WSF_SURFACE_MOVER</td></tr><tr><td>subsurface</td><td>J13.4 - WsfTadiJ13_4I</td><td>WSF_SUBSURFACE_MOVER</td></tr><tr><td>land</td><td>J13.5 - WsfTadiJ13_5I</td><td>WSFGROUND_MOVER</td></tr></table>

report_weapon_quantity_1 <weapon-name> <integer-value>   
report_weapon_quantity_2 <weapon-name> <integer-value>   
report_weapon_quantity_3 <weapon-name> <integer-value>

这些命令用于设置 J13.2 消息的 C2 字中的库存数量和库存类型字段。<weapon-name> 必须与平台上的武器匹配以找到当前数量。<integer-value> 表示库存类型。

# SCRIPTED 消息处理器

SCRIPTED 消息处理器默认不执行任何操作，但提供了一种处理 Tadil-J 消息的方法。可以通过脚本发送消息。

```txt
message Processor <name> SURVEILLANCE  
... Message Processors ...  
script void on_message_X_Y(WsfTadilJX_YI aMessage)  
... script commands ...  
end_script  
end_message Processor 
```

script void on_message_X_Y(WsfTadilJX_YI aMessage) … end_script

定义一个脚本，当接收到特定消息类型时执行。X 和 Y 被替换为要处理的 Tadil-J 消息编号。

示例：打印所有接收到的 air-PPLI 消息，并发送一条 PPLI 消息。

```txt
script void on_message_2_2(WsfTadilJ2_2I aMessage)  
aMessage.Print();  
WsfTadiJ2_2I msg = WsfTadiJ2_2I();  
msg.altitude(PLATFORM.altitude());  
WsfTadiJ2_2E1 ext1 = msg.AddExtension1();  
ext1Latitude(PLATFORMLatitude());  
ext1.Longitude(PLATFORM.Longitude());  
SendJMessage(msg);  
endScript 
```

# 3.3.37. 链接处理器 WSF_LINKED_PROCESSOR

```txt
processor <name> WSFLINKEDPROCESSOR 
```

```txt
...processor commands ... Platform Part Commands ... ...External Link Commands ... end Processor 
```

WSF_LINKED_PROCESSOR 是一种处理器，具有内部链接（连接到其他处理器）和外部链接（通过通信连接到其他平台）。虽然这种类型的处理器用途有限，但许多其他处理器类型都派生自它，并具有类似的链接功能。

使用示例

一个简单的应用场景是雷达站，其中雷达报告直接发送给指挥官。在这种情况下，配置可能如下：

```txt
platform_type RADAR_POST WSF PLATFORM  
comm datalink WSFCOMM_TRANSEIVER  
...  
end_comm  
sensor radar WSF_RADAR_SENSOR  
...  
internal_link router  
end SENSOR  
processor router WSFLINKEDPROCESSOR  
external_link commander via datalink  
end Processor  
endPLATFORM_type 
```

# 配置说明

platform_type RADAR_POST WSF_PLATFORM: 定义一个平台类型为雷达站。  
comm datalink WSF_COMM_TRANSCEIVER: 定 义 通 信 链 路 ， 使 用WSF_COMM_TRANSCEIVER 进行数据传输。  
sensor radar WSF_RADAR_SENSOR: 定义一个雷达传感器，使用 WSF_RADAR_SENSOR。  
internal_link router: 将雷达传感器内部链接到一个名为 router 的处理器。  
processor router WSF_LINKED_PROCESSOR: 定 义 一 个 处 理 器 router ， 类 型 为WSF_LINKED_PROCESSOR。  
external_link commander via datalink: 将处理器 router 外部链接到指挥官，通过数据链路进行通信。

这种配置允许雷达站的雷达报告通过内部和外部链接直接传递给指挥官，实现高效的指挥和控制通信。

# 3.3.38. 轨迹会合处理器 WSF_ORBITAL_CONJUNCTION_PROCESSOR

```txt
processor <name> WSF_ORBITAL_CONJUNCTIONPROCESSOR ... WSFScriptPROCESSORCommands ... 
```

```txt
search_interval <time-value>   
filter_cut_distance <length-value>   
search_step_size <angle-value>   
exclusion_factor <real-value>   
default_variance <length-value>   
default_object_size <length-value>   
prediction_model <string>   
primary <string> end_primary   
debug   
script void on_conjunction_predicted(Array<WsfOrbitalConjunctionReport> aReports)   
...   
end.script   
end Processor 
```

WSF_ORBITAL_CONJUNCTION_PROCESSOR 是一个处理器，用于监控包含的 WsfPlatform的主轨迹列表，并在 search_interval 内预测任何被跟踪的对象是否可能与指定的主要对象发生交会。该处理器继承了 WSF_SCRIPT_PROCESSOR 的所有功能，并在以下方面进行了扩展：

轨迹分类：在每次处理器更新结束时，检查所属平台的主轨迹列表，将每个轨迹分类为主要和次要对象。主要轨迹对应于处理器特别关注的航天器。次要轨迹是所属平台主轨迹列表中空间域的其他轨迹。  
交会预测：对于每个主要轨迹，检查每个其他主要和次要轨迹是否可能发生交会。预测从更新时刻开始，持续到 search_interval。  
快速过滤：使用快速过滤器快速移除不可能发生交会的轨迹对。通过检查两个轨道的近地点和远地点来执行过滤。如果最近可能的接近距离大于 filter_cut_distance，则忽略该对。  
接近预测：通过沿轨道采取一系列步骤并在步骤的开始和结束之间进行插值来预测接近。这允许采取相对较大的步骤，从而减少处理器的计算负担。步骤大小由 search_step_size设置。  
交会计算：对于每对轨迹，当预测到接近时，处理器将计算多个量，包括最大交会概率、最近接近点的时间和偏差距离，以及两个对象进入交会区域的时间，该区域定义为组合误差椭球体，按 exclusion_factor 缩放。  
脚本接口：在发现所有可能的交会后，处理器将调用名为 on_conjunction_predicted 的脚 本 （ 如 果 存 在 ） 。 此 函 数 的 参 数 将 是 包 含 可 能 交 会 详 细 信 息 的WsfOrbitalConjunctionReport 对象的集合。这些报告将被排序，以便较早的交会出现在Array<T> 的前面。

# 配置命令

search_interval <time-value>声明将被预测的时间，以搜索交会。  
filter_cut_distance <length-value>

声明快速过滤器中使用的距离。

默认值： $1 0 \ k \mathsf { m }$

search_step_size <angle-value>

声明预测中使用的步长。

默认值：3 度

exclusion_factor <real-value>

声明排除区的大小，作为组合协方差椭球体按此因子缩放。

默认值：8.0

default_variance <length-value>

声明在轨迹没有状态协方差数据时的默认位置方差。

默认值： $1 0 . 0 \mathsf { m }$

default_object_size <length-value>

声明在计算交会概率时使用的对象大小。

默认值： ${ \mathsf { 1 . 0 } } { \mathsf { m } }$

prediction_model <string>

声明处理器使用的预测模型，可以是 default 或 norad。

primary <string> … end_primary

声明要视为主要对象的对象列表。

debug

打开有关此处理器操作的附加输出。

# 脚本接口

on_conjunction_predicted

可选脚本，允许对可能交会的发现做出反应。仅在发现交会时调用此脚本，因此输入数组将始终至少有一个条目。

# 3.3.39. 完美跟踪器 WSF_PERFECT_TRACKER

processor <name> WSF_PERFECT_TRACKER

processor Commands ...

Platform Part Commands ...

update_interval <time-value>

end_processor

WSF_PERFECT_TRACKER 是一个处理器，用于模拟完美的寻的器或完美的指令引导。它简单地更新平台的“当前目标轨迹”，以对应于传递给主平台的真实目标平台。“当前目标轨迹”通常被引导计算机（如 WSF_GUIDANCE_COMPUTER 和 WSF_HARM_GUIDANCE）用于确定导航目的的拦截点。

# 命令

update_interval <time-value>

指定处理器应更新轨迹的频率。

默认值：无（必须提供）

WSF_PERFECT_TRACKER 的主要功能是确保目标轨迹与真实目标平台保持一致，从而为

引导系统提供精确的导航信息。这种模拟的完美跟踪器在仿真环境中非常有用，因为它消除了传感器误差和延迟的影响，使得测试和验证引导算法更加直接和可靠。

# 3.3.40. RIPR-AI 代理处理器 WSF_RIPR_PROCESSOR

```txt
processor <name>WSF_RIPRPROCESSOR   
... Script Processor Commands ...   
// job related inputs channel_job_type <channel-index> <job-type> job_board_comm <comm-name> job_pass_through job_stickiness <real-value> num_job_channels <integer-value> //windowing inputs auto_exclusive_mode <boolean-value> bid_window_open_length <time-value> job_window_open_length <time-value>   
// uplink related inputs maxweapon_uplinks <integer-value> use_remoteTracks_for_uplink <boolean-value> weapon_uplink_path <sensor-name> <comm-name>   
query_bid_type <job-type> end_query_bid_type   
end Processor 
```

WSF_RIPR_PROCESSOR 是 WSF 中所有 RIPR（关于什么是 RIPR 在：4.13.3RIPR 中介绍）代理的基础。大多数 RIPR 代理使用行为树（参见：4.13.1 行为树 behavior_tree）构建，现在 在 WSF_SCRIPT_PROCESSOR 上 定 义 。 任 何 新 的 RIPR 代 理 类 都 应 继 承 自WsfRIPRProcessor。RIPR 处理器的独特功能是工作板，任何希望利用自下而上工作竞标系统的代理都应使用此处理器。另一种选择是 WSF_QUANTUM_TASKER_PROCESSOR。

命令

channel_job_type <channel-index> <job-type>

指定此 RIPR 代理处理器上的指定通道将被允许竞标并赢得指定类型的工作。如果未为通道指定类型，则该通道允许所有类型。channel-index 是一个整数值，job-type 是一个等于工作名称（也称为工作类型）的字符串。

job_board_comm <comm-name>

指定所有工作交互将通过的通信设备的名称。这包括竞标、状态更新和赢得工作。

job_pass_through

如果指定，此 RIPR 处理器将仅作为工作的传递。它不会在自己的板上持有任何工作，所有来自其下属的竞标将上升到其指挥官，其下属将从其指挥官的工作板上赢得工作。

job_stickiness <real-value>

RIPR 处理器的工作粘性用于为当前工作分配提供额外的稳定性。当 RIPR 处理器赢得工作并执行该工作时，其所有对该工作的竞标都乘以 job_stickiness 值。

num_job_channels <integer-value>

RIPR 处理器的通道数量代表其同时执行工作的能力。例如，如果处理器正在竞标跟踪工作且其雷达可以同时跟踪四个目标，则它可能有四个工作通道。

auto_exclusive_mode <boolean-value>

如 果 设 置 为 true ， RIPR 处 理 器 工 作 板 将 使 用 “job_window_open_length” 和“bid_window_open_length”提供的时间值自动交替工作板的工作竞标和工作授予窗口。

bid_window_open_length <time-value>

指定每个周期竞标窗口将打开的时间。在竞标窗口关闭时，所有提交给工作板的竞标都将被忽略。

job_window_open_length <time-value>

指定每个周期工作窗口将打开的时间。在工作窗口关闭时，所有工作保持恒定分配（没有人更换工作）。

max_weapon_uplinks <integer-value>

指定 RIPR 代理能够支持的最大活动上行链路数量。

use_remote_tracks_for_uplink <boolean-value>

如果设置为 true，RIPR 处理器将从任何传感器和任何来源发送轨迹到其支持的武器。

weapon_uplink_path <sensor-name> <comm-name>

如果为 RIPR 处理器指定了武器上行链路路径，则处理器将支持所有发射武器的上行链路。

query_bid_type <job-type>

确定并返回代理对给定类型工作的竞标。此代理上不允许为同一工作类型定义其他query_bid_type 块。

这些命令和功能使 RIPR 处理器能够有效地管理和分配工作，支持复杂的任务竞标和执行系统。

# 3.3.41. 状态机处理器 WSF_STATE_MACHINE

```txt
processor <name> WSF_STATE_MACHINE  
WSFScriptPROCESSOR Commands ...  
show_statevaluations  
show_state_transitions  
state <state-name>  
... state definition ...  
end_state  
# Script Interface 
```

```ocaml
on_init... end_on_initi on_init2 ... end_on_init2 on_update ... end_on_update script_variables ... end.script_variables script ... end_script .. Other Script Commands ..   
end Processor 
```

# 概述

WSF_STATE_MACHINE 使用有限状态机的概念。用户定义一组转换规则，这些规则定义了从一个状态转换到另一个状态的条件。这些转换规则是使用 WSF 脚本语言定义的。与WSF_SCRIPT_PROCESSOR 类似，WSF_STATE_MACHINE 无法直接访问轨道数据，因此不能使用 TRACK 变量。

# 命令

show_state_evaluations: 指示应将状态评估的信息写入标准输出。这基本上显示了每个next_state 块评估的真或假状态。  
show_state_transitions: 指示应将状态转换的信息写入标准输出。  
state <state-name>: 在状态机中定义一个名为 <state-name> 的状态。除了转换条件外，注意一个状态可以包含自己的 behavior_tree。

on_entry: 定义进入状态时要执行的操作。  
□ on_exit: 定义退出状态时要执行的操作。  
□ next_state <next-state-name>: 指定状态机应在何种条件下转换到另一个状态。  
□ behavior_tree: 允许在状态中包含行为树（参见：4.13.1 行为树 behavior_tree），可以定义复杂的行为和决策过程。

# 注意事项

WSF_STATE_MACHINE 利用通用脚本接口（参见：4.1 公共脚本接口 Common ScriptInterface）和 WSF_SCRIPT_PROCESSOR 的功能，提供了增强的脚本灵活性。

# 3.3.42. 威胁处理器 WSF_THREAT_PROCESSOR

```c
processor <name> WSF-threatPROCESSOR processor Commands ...   
threat_velocity <speed>   
threat_anglepread <angle>   
threat_time_to_intercept <time>   
require_iff_foe <boolean>   
ignore_lower_altitude-threats <boolean> ignore Without_location <boolean> 
```

```txt
ignore_without_speed <boolean> end Processor 
```

WSF_THREAT_PROCESSOR 是一个处理器，它监控包含的 WsfPlatform 的主轨道列表，并根据指令约束从中创建一个威胁轨道列表。WSF_THREAT_PROCESSOR 旨在识别高速来袭的平台（例如导弹），但也可以适应其他用途。

命令

threat_velocity <speed-value>: 声明超过此速度的轨道将被分类为威胁。

默认值: $6 0 0 ~ \mathrm { m } / s$

threat_angle_spread <angle-value>: 声明平台前方的角度宽度，在此范围内它可能将轨道视为威胁。

默认值:30 度

threat_time_to_intercept <time-value>: 声明在此拦截时间限制内，轨道可能被视为威胁。基于速度和距离。

默认值:60 秒

require_iff_foe <boolean>: 如果设置为 true，此威胁处理器将忽略所有没有在其轨道中设置 IFF 为 FOE 的潜在威胁。

默认值: false

ignore_lower_altitude_threats <boolean>: 如果设置为 true，此威胁处理器将忽略所有处于较低高度并向下移动的潜在威胁。

注意: 在考虑 WSF_STRAIGHT_LINE_MOVER 时要小心；由于地球的曲率，它们可能较低并“向下”移动。

默认值: false

ignore_without_location <boolean>: 如果设置为 true，威胁处理器将忽略没有位置数据的轨道；此类轨道始终不构成威胁。

默认值: true

ignore_without_velocity <boolean>: 如果设置为 true，威胁处理器将忽略没有速度数据的轨道；此类轨道始终不构成威胁。

默认值: true

这些命令和默认设置帮助配置 WSF_THREAT_PROCESSOR，以便根据特定的威胁识别标准有效地筛选和识别潜在威胁。

# 3.3.43. 跟踪处理器 WSF_TRACK_PROCESSOR

```txt
processor <name> WSFTRACKPROCESSOR  
... processor Commands ...  
... WSFScript PROCESSOR Commands ...  
master_track Processor ...  
non/master_track Processor ...  
trackmanager...end_trackmanager  
# Track Purging Commands 
```

```tcl
purge_interval ...   
track_history_retention_interval   
# Reporting Commands   
external_link ...   
report_to ...   
report_interval ...   
report_method ...   
fused_track_reporting ...   
raw_track_reporting ...   
pass_through_reporting ...   
candidate_track_reporting ...   
unchanged_track_reporting ...   
update_on_report ...   
# Received Report Assimilation Commands   
circular_report_rejection ...   
inbound_filter   
# Script Interface   
on_initiage ... end_on_initiage   
on_initiage2 ... end_on_initiage2   
on_update ... end_on_update   
script_variables ... endScript_variables   
script ... endScript   
.. Other Script Commands ..   
script bool WsfTrackProcessor.is_track_reportable (WsfTrack aTrack)   
...   
end.script   
end Processor 
```

WSF_TRACK_PROCESSOR 实现了一个用于 track_manager 的处理器接口，负责以下两个主要功能：

接受报告：从本地和外部来源接收报告，并将其提供给轨道管理器进行关联和融合。发送更新的轨道：将更新后的轨道发送给感兴趣的各方。

作为一个 WSF_SCRIPT_PROCESSOR，它通过通信（comm）向连接的内部处理器和外部实体发送消息。

# 轨道管理器选项

主轨道处理器：可以是父平台的轨道管理器（即，维护平台主轨道列表的轨道管理器）。

非主轨道处理器：可以创建自己的轨道管理器，维护一个独立的轨道列表。

# 报告选项

可以选择向外部实体报告融合后的轨道或“原始”轨道（原始轨道定义为输入到轨道处理器的任何轨道）。外部实体将收到包含更新轨道的 WsfTrackMessage（类型为WSF_TRACK_MESSAGE）。同一平台上的连接处理器将收到 WSF_TRACK_NOTIFY_MESSAGE，指示融合轨道的状态发生了变化（创建、更新、丢弃、移除）。融合轨道通过平台的主轨道列表进行引用。

# 一般命令

master_track_processor: 指示此处理器应用作平台的主轨道处理器。它将直接访问平台的主轨道管理器对象和相关的主轨道列表。这是默认行为。  
non_master_track_processor: 指示此处理器不会用作平台的主轨道处理器。它将创建自己的轨道管理器对象，并维护一个独立于平台主轨道列表的轨道列表。

注意: 对于非主轨道处理器，此对象将在 track_manager … end_track_manager 块中处理 track_manager 子命令。

track_manager … end_track_manager: 这是用于处理非主轨道处理器的轨道管理器输入的块。在此块中放置轨道管理器子命令。

# 轨道清除命令

purge_interval <time-value>: 指定如果轨道在指定时间内没有更新，则将其丢弃。如果报 告 了 融 合 轨 道 （ 参 见 report_fused_tracks ） ， 将 通 过 外 部 链 接 发 送WsfTrackDropMessage，并通知附加的本地观察者。

注意: 已分配或接收到任务分配的轨道在所有此类分配完成之前不会被丢弃。

注意: 对于非主轨道处理器，此命令无效。

默认值: 无限（不清除轨道）。

track_history_retention_interval <time-value>: 指定应保留轨道历史的时间间隔。此选项仅在关联的轨道管理器中设置了 retain_track_history 时有效。

注意: 此间隔是下限。随着模拟时间的推进，超过保留间隔的轨道将被保留，直到下次清除轨道历史。

注意: 当前轨道历史清除与输入的时间间隔相同。

默认值:1 小时

# 报告接收者

external_link 或 report_to: 这些命令指定轨道报告的接收者。

# 报告频率和方法

report_interval <time-value>: 设置报告轨道（原始或融合）的时间间隔。每个轨道将在相应的轨道列表中按照报告间隔向外部连接的实体发送一次。

默认值:10 秒（如果定义了外部链接）。

注意: 必须定义外部链接以进行报告。

report_method [batch | cyclic | on_update | on_update_fused]: 指定报告轨道的策略。

batch: 所有轨道在报告间隔开始时报告。新轨道将立即报告。  
cyclic: 轨道在整个报告间隔中报告。报告之间的时间为 T/(N-1)，其中 T 是报告间隔，N 是帧开始时的轨道数量。新轨道将立即报告。  
on_update: 轨道在更新时报告。这包括：

如果 raw_track_reporting 开启且自上次同一轨道 ID 报告以来的时间大于或等于report_interval，则报告接收到的轨道。

如果 fused_track_reporting 开启，则报告由于接收到的轨道报告而更新的“本地”或“融合”轨道。

隐式设置 circular_report_rejection 为开，unchanged_track_reporting 为关。

on_update_fused: 等同于 report_method on_update，同时开启 fused_track_reporting、 circular_report_rejection，关闭 unchanged_track_reporting。

默认值: batch

# 报告的数据类型

fused_track_reporting <boolean-value>: 指示是否通过通信设备向外部实体报告融合（本地）轨道。

默认值: 关闭（不报告融合轨道）。

注意: 仅应向不会将轨道发回发送者的实体报告融合轨道。

raw_track_reporting <boolean-value>: 指示是否通过通信设备向外部实体报告非本地（“原始”）轨道。

默认值: 开（报告原始轨道）。

pass_through_reporting <boolean-value>: 指示应立即以“直通”模式报告非本地（“原始”）轨道，而不是基于时间间隔。  
candidate_track_reporting <boolean-value>: 指示是否应向外部实体报告“候选轨道”（即，过滤器尚不稳定的传感器测量）。设置此选项允许数据在接收到时立即在主轨道列表中可用。  
unchanged_track_reporting <boolean-value>: 指示自上次报告间隔以来数据未更改的轨道是否应再次报告。

默认值: 开

update_on_report <boolean-value>: 指定是否在报告时更新轨道信息。如果启用，在发送 轨 道 报 告 之 前 会 更 新 轨 道 位 置 和 位 置 不 确 定 性 。 如 果 启 用 了quantitative_track_quality，则根据外推的位置不确定性重新计算报告的轨道质量。

默认值: 如果设置了 quantitative_track_quality，则为真；否则为假。

# 已弃用的命令形式

以下命令形式已弃用，不应在新应用中使用，因为它们可能在未来版本中被移除：

report_raw_tracks: 等同于 raw_track_reporting on。

report_fused_tracks: 等同于 fused_track_reporting on。

report_pass_through: 等同于 pass_through_reporting on。

report_candidate_tracks: 等同于 candidate_track_reporting on。

# 循环报告拒绝

circular_report_rejection <boolean-value>: 指示如何处理被确定为“循环”的接收轨道报告。如果以下条件之一为真，则接收的轨道报告被声明为“循环报告”：

接收的轨道报告是从接收节点发起的报告的简单反射。

接收的轨道报告是融合轨道报告，其最后一次更新是由于从接收节点发起的报告。

默认值: 关闭

# 入站过滤器

inbound_filter … end_inbound_filter: 默认情况下，处理器将尝试将所有接收的报告提交给轨道管理器进行关联和融合。然而，在某些情况下，特定的轨道处理器可能不希望进行此活动。此块允许控制同化的内容。  
reject non_sensor_reports: 指示应忽略不是直接传感器报告的报告。这通常用于“过滤节点”向“融合节点”报告原始轨道，后者从多个来源同化数据并生成融合报告。存在一种可能性，即融合节点可能会将其融合产品广播回过滤节点，如果同化会导致问题。

# 脚本接口

WsfTrackProcessor 利用通用脚本接口和 WSF_SCRIPT_PROCESSOR 的功能，并提供以下功能：

void is_track_reportable(WsfTrack aTrack): is_track_reportable 方法可以提供额外的控制层次，以决定哪些轨道被报告。对于创建自定义报告方法非常有用。如果定义了此方法，则每当轨道因标准融合或原始轨道报告而即将被报告时，都会调用它。如果未定义，则轨道将按正常方式报告。

方法必须定义如下：

script bool is_track_reportable(WsfTrack aTrack) //在此定义脚本主体，如果轨道应被报告则返回'true'，否则返回'false'。 // //例如，以下代码仅在轨道在最近60秒内更新时报告： bool isReportable $=$ true; if(aTrack.TimeSinceUpdated() $>60.0$ )isReportable $=$ false; return isReportable;   
end_script

注意：对于融合和原始轨道报告，都会调用相同的方法。对于融合轨道报告，输入对象实际上是 WsfLocalTrack，但参数类型仍为 WsfTrack。如果需要访问仅在 WsfLocalTrack 上定义的方法，必须“转换”参数。例如：

```txt
script bool is_track_reportable(WsfTrack aTrack)  
bool isReportable = true;  
WsfLocalTrack track = (WsfLocalTrack) aTrack;  
if (track.IsValid()) // 如果轨道是 :class:'WsfLocalTrack', 则为真  
{  
// 如果轨道“旧”或没有贡献者，则不报告  
if ((track.TimeSinceUpdated() > 60.0) || (track.RawTrackCount() == 0)) isReportable = false; 
```

```txt
} return isReportable; end_script 
```

3.3.44. 状态机轨迹处理器 WSF_TRACK_STATE_CONTROLLER  
```txt
processor <name> WSFTRACK_STATE_CONTROLER 
```

```txt
... WSFScriptPROCESSOR ...   
// State Machine Commands   
show_statevaluations   
show_state_transitions   
state<state-name> ... state definition ...   
end_state   
// Thinker Commands   
number_of_servers ...   
// Track State Controller Commands   
evaluate_candidateTracks ...   
evaluation_interval ...   
time_to Evaluate ...   
# Script Interface   
on_initiage ... end_on_initiage   
on_initiage2 ... end_on_initiage2   
on_update ... end_on_update   
script_variables ... endcript_variables   
script ... endcript   
... Other Script Commands ...   
on_track_drop   
...   
end_on_track_drop   
end Processor 
```

WSF_TRACK_STATE_CONTROLLER 是一个工具，允许用户使用有限状态机的概念对轨迹进行分类。用户可以定义一组转换规则，这些规则规定了从一个状态转换到另一个状态的条件。这些转换规则是使用 WSF 脚本语言定义的。每个轨迹在机器中维护其自身的状态。

# State Machine Commands

show_state_evaluations: 指示关于状态评估的信息应写入标准输出。这基本上显示了每个 next_state 块评估的真或假状态。  
show_state_transitions: 指示关于状态转换的信息应写入标准输出。  
state <state-name>: 在状态机中定义一个名为 <state-name> 的状态。

一 on_entry: 当进入状态时执行的脚本命令。  
□ on_exit: 当退出状态时执行的脚本命令。  
□ next_state <next-state-name>: 定义可能的下一个状态及其转换条件。

# Thinker Commands

number_of_servers: 指定可以同时进行的最大评估数量。

默认值:1

# Track State Controller Commands

evaluate_candidate_tracks <boolean>: 指示是否评估“候选轨迹”。候选轨迹是指已接收但尚未通过过滤器确定为“稳定”的轨迹。

默认值: false

evaluation_interval <state-name> <time-value>: 指定在指定状态下轨迹应（重新）评估的频率。  
time_to_evaluate <state-name> <time-value>: 指定在指定状态下执行轨迹评估所需的时间。这模拟了逻辑上“思考”或执行评估所需的时间。

默认值: 0.01 秒

# Script Interface

WSF_TRACK_STATE_CONTROLLER 利用通用脚本接口和 WSF_SCRIPT_PROCESSOR 的功能，并提供以下附加功能：

on_track_drop … end_on_track_drop: 当处理器被轨迹管理器告知轨迹丢失时调用。隐式定义的脚本变量 TRACK（类型为 WsfLocalTrack）表示被丢弃轨迹的最后已知状态。

# Method of Operation

每个轨迹在首次被发现时，最初会在 time_to_evaluate 间隔后被放入输入文件中定义的第一个状态。从那时起，它将继续评估当前状态的转换规则，并根据规则允许的情况转换到新状态。当发生转换时，将执行当前状态的 on_exit 脚本（如果已定义），并执行新状态的 on_entry 脚本（如果已定义）。首次进入状态时，应用 time_to_evaluate 间隔，这作为状态进入时的思考延迟。

每个轨迹在其当前存在的状态定义的间隔内被（重新）评估。执行评估所需的逻辑时间由该状态的 time_to_evaluate 定义。控制器可以同时执行多达 number_of_servers 次评估。当需要评估给定轨迹的状态时，确定是否有服务器可用来执行评估。如果有服务器可用，它将被标记为忙碌状态，并在间隔完成时执行实际的规则评估（从而模拟思考过程）并安排下一次评估。如果没有可用的服务器，则将其放入待评估的挂起队列中，等待下一个可用的服务器进行评估。

# 3.3.45. 区域多传感器融合处理器 WSF_TRIMSIM_PROCESSOR

```txt
processor <name> WSF_TRIMSIMPROCESSOR 
processor Commands ... Platform Part Commands ... sensors ... end Sensors minimum detections message_length ... messagepriority .. end Processor 
```

WSF_TRIMSIM_PROCESSOR 提供了从战区范围参考信息管理模拟（TRIMSIM）和SUPPRESSOR 实现中派生的到达时间差（TDOA）算法。它模拟了参考系统误差对空对地目标数据融合的影响。TDOA算法基于来自各种来源的误差生成目标点在三维空间中的测量误差。这些误差应用于主传感器（传感器块中的第一个传感器）的检测信息。