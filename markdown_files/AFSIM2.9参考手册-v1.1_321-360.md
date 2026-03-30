# 轨迹状态控制器命令

evaluate_candidate_tracks <boolean>: 指示是否评估“候选轨迹”。候选轨迹是已接收但尚未确定为“稳定”的轨迹（由过滤器定义）。

默认值: false

evaluation_interval <state-name> <random-time-reference>: 指定在指示状态下轨迹应（重新）评估的频率。  
number_of_servers <integer>: 指示可以同时进行的最大轨迹评估数。评估所需的时间通过 time_to_evaluate 命令设置。

默认值:1

show_state_evaluations: 指示应将有关状态评估的信息写入标准输出。这基本上显示了每个 next_state 块评估的真或假状态。

show_state_transitions: 指示应将有关状态转换的信息写入标准输出。  
state <state-name>: 定义状态机中的一个状态，名称为 <state-name>。

▫ on_entry … end_on_entry: 进入此状态时执行这些脚本命令。这是一个可选的子命令。  
□ on_exit … end_on_exit: 离开此状态时执行这些脚本命令。这是一个可选的子命令。  
▫ next_state <next-state-name> … end_next_state: 这是一个可选的脚本块，必须返回一个真/假值。评估时，返回值决定是否转换到由 <next-state-name> 定义的命名状态。如果未定义 next_state，则将在此状态中“死胡同”。多个 next_state 子命令是允许的，但只有在所有先前的转换评估为假时才会被评估（第一个“真”会短路进一步的评估）。因此，建议在进行更复杂的 next_state 评估之前，先执行最简单的评估以节省 CPU 周期。

状态命令定义结构:  
```txt
state <state-name>
    on_entry
        ... <script-command> ...
    end_on_entry
    on_exit
        ... <script-command> ...
    end_on_exit
    next_state <next-state-name-1>
        ... <script-command> ...
    end_next_state
    next_state <next-state-name-2>
        ... <script-command> ...
    end_next_state
end_state 
```

time_to_evaluate <state-name> <random-time-reference>: 指定在指示状态下执行轨迹评估所需的时间。这模拟了在逻辑上“思考”或执行评估所需的时间。默认值: 0.01 秒  
track_processor <track-proc-name>: 指定一个 WSF_TRACK_PROCESSOR 的名称（通常作为非主轨迹处理器运行），其轨迹列表将用于评估过程。默认值: 使用平台的主轨迹列表。  
comm_retry_attempts <integer>: 指示重试失败通信的尝试次数。  
comm_retry_interval <time-value>: 指示重试失败通信的尝试之间的时间。  
operating_level <name> <level>: 指示操作条件或状态及其相关级别。

示例:   
```txt
operating_level Engage 0 
```

time_to_recognize_messages <time-value>: 指示识别消息所需的时间。

track_update_interval <time-value>: 指示向受让人发送轨迹更新的时间间隔。  
track_update_strategy [ default | suppressor ]: 指示如何发送轨迹更新。

□ default: 如果任务已被接受，则定期向受让人发送轨迹更新。  
□ suppressor: 仅当轨迹管理器指示轨迹已更新时，才向受让人发送轨迹更新。

weapon_uplink_path <sensor-name> <comm-name>: 指示支持武器上行链路时使用的传感器和通信设备。  
uplink_source <sensor-name>: 指示上行链路时轨迹的来源。

默认值: track-manager

uplink_comm <comm-name>: 指示用于传输上行链路的通信系统。  
uplink_delay<time-value>: 指示在接收到上行链路任务后启动上行链路之前的延迟。默认值: 0.0 秒  
auto_weapon_uplink <boolean-value>: 指示任务管理器在调用 FireAt() 脚本时是否自动为每个发射的武器分配上行链路任务。

默认值: off

auto_weapon_uplink_platform <platform-name>: 指示使用 auto_weapon_uplink 启动的上行链路任务的受让人。

默认值: 此平台

uplink_send_interval <time-value>: 发送上行链路轨迹之间的最小间隔（仅用于基于任务的上行链路）。

默认值: 0.0 秒

show_task_messages: 指示与任务分配、取消和完成相关的信息应写入标准输出。  
show_uncompleted_tasks: 这是一个调试工具，指示在任务处理器销毁期间未完成任务的信息应写入标准输出。

# 脚本接口

WSF_TASK_PROCESSOR 利用通用脚本接口和 WSF_SCRIPT_PROCESSOR 的功能，并提供以下附加脚本：

on_task_assign: 当接收到任务分配时调用。

```txt
script void on_task_assign(WsfTask aTask, WsfTrack aTrack)  
...  
end_script 
```

on_task_cancel: 当接收到任务取消时调用。

```txt
script void on_task Cancel(WsfTask aTask)  
...  
end_script 
```

on_task_complete: 当任务的分配者收到受让人完成指定任务的通知时调用。

```txt
script void on_taskcomplete(WsfTask aTask) 
```

```rst
... endScript 
```

on_task_assign_sent: 当发送任务分配时调用。

```txt
script void on_task_assign_sent(WsfTask aTask, WsfTrack aTrack)  
...  
end_script 
```

on_task_cancel_sent: 当发送任务取消时调用。

```txt
script void on_task Cancel_sent(WsfTask aTask)  
...  
end_script 
```

on_task_complete_sent: 当任务的受让人发送任务完成消息时调用。

```txt
script void on_taskcomplete_sent(WsfTask aTask)  
...  
end_script 
```

on_operating_level_change: 每当检测到“操作级别”变化时调用。

```txt
script void on-operating_level_change(string aLevel)  
...  
end_script 
```

on_track_drop: 每当处理器被轨迹管理器告知轨迹丢失时调用。

```txt
script void on_track_drop()
...
end_script 
```

# 操作方法

每个轨迹在首次被发现时，最初会在 time_to_evaluate 间隔过后进入输入文件中定义的第一个状态。从那时起，它将继续评估当前状态的转换规则，并根据规则允许的情况转换到新状态。当发生转换时，将执行当前状态的 on_exit 脚本（如果已定义），并执行新状态的 on_entry 脚本（如果已定义）。首次进入状态时，应用 time_to_evaluate 间隔。这作为状态进入时的思考延迟。

每个轨迹在其当前存在的状态定义的间隔内被（重新）评估。执行评估所需的逻辑时间由该状态的 time_to_evaluate 定义。控制器可以一次执行多达 number_of_servers 个评估。当需要评估给定轨迹的状态时，将确定是否有服务器可用于执行评估。如果有服务器可用，则标记为忙，并将在间隔完成时执行实际的规则评估（从而模拟思考过程）并安排下一次评估。如果没有可用的服务器，则将其放入待处理队列，以便下一个可用的服务器进行评估。

# 3.3.22. 相干传感器处理器 WSF_COHERENT_SENSOR_PROCESSOR

```tcl
processor <name> WSF_COHERENT_SENSORPROCESSOR  
processor Commands ...  
Platform Part Commands ...  
sensors ... end Sensors  
detection_threshold ...  
use_target_result ...  
coast_time ...  
result_PROCESSing_type ...  
fusion_method ...  
message_length ...  
message_priority ...  
end Processor 
```

WSF_COHERENT_SENSOR_PROCESSOR 提供了相干传感器的功能，包括将多个传感器的WsfEM_Interaction 结果（即非本地结果）处理为单个交互结果（本地结果）以进行检测和轨迹报告的能力。该处理器基于 result_processing_type 从非本地结果计算本地结果，并使用融合技术从非本地结果计算本地结果位置（即测量值）。

# 操作方法

更新间隔: 如果指定了 update_interval，则传感器或目标结果将在下一个更新间隔之前排队并批量处理。如果未指定 update_interval，则传感器或目标结果将在每个传感器更新每个目标时进行处理。

# 典型使用结构:

```txt
platform_type ...
sensor sensor-1 WSF_RADAR_SENSOR
...
# 将轨迹转发到 'track_proc'
processor track_proc
end_sensor
sensor sensor-2 WSF_RADAR_SENSOR
...
# 将轨迹转发到 'track_proc'
processor track_proc
end SENSOR 
```

```txt
processor cs_proc WSF_COHERENT_SENSORPROCESSOR  
...  
#将提取的'tracks'转发到'track_proc'  
processor track_proc  
#连接到传感器以收集'interaction'数据进行处理  
sensors  
sensor sensor-1  
sensor sensor-2  
end Sensors  
end Processor  
processor track_proc WSF Track PROCESSOR  
...  
#隐式地从'cs_proc'获取轨迹并更新trackmanager  
end Processor  
end platform_type 
```

# 关键功能

传 感 器 融 合 : 通 过 将 多 个 传 感 器 的 结 果 融 合 为 一 个 本 地 结 果 ，WSF_COHERENT_SENSOR_PROCESSOR 提高了检测和跟踪的准确性和可靠性。这种融合技术在智能飞行器目标检测和高级驾驶辅助系统（ADAS）中得到了应用。

批处理能力: 通过指定 update_interval，可以实现结果的批量处理，从而提高处理效率。

灵活的传感器连接: 允许连接多个传感器以收集交互数据，并将处理后的结果转发到轨迹处理器进行进一步的管理和更新。

WSF_COHERENT_SENSOR_PROCESSOR 提供了一系列命令，用于配置和管理相干传感器的功能。以下是这些命令的详细说明：

sensors … end_sensors: 定义传感器列表。

□ sensor <sensor-name>: 指定与处理器在同一平台上的传感器名称。  
platform_sensor <platform-name> <sensor-name>: 指定外部平台上的传感器名称。

detection_threshold <dbratio-value>: 定义接收器的检测阈值。

默认值: 3.0 dB

use_target_result <boolean-value>: 指定是否使用每个传感器的目标结果。如果为 false，则使用每个传感器结果，这取决于传感器的能力。

默认值: false

coast_time<time-value>: 指定更新之间可能经过的最大时间，超过此时间轨迹将被丢弃。  
result_processing_type [ SNR_BASED | RSS_BASED ]: 指定用于计算结果信噪比（SNR）的结果处理类型。

□ SNR_BASED: 使用最佳非本地结果基于 SNR 形成本地结果。  
□ RSS_BASED: 使用信号功率的平方和的平方根与噪声功率的均方根计算本地结果。

$$
S N R _ {R S S} = \frac {\sqrt {\sum_ {i = 1} ^ {N} P _ {s i g n a l \_ i} ^ {2}}}{\sqrt {\sum_ {i = 1} ^ {N} P _ {n o i s e \_ i} ^ {2} / N}}
$$

默认值: SNR_BASED

fusion_method [ replacement | weighted_average | MTT ]: 指定结果处理使用的融合算法。

□ replacement: 使用标准算法融合相关测量。  
□ weighted_average: 使用协方差矩阵融合本地和非本地测量。  
□ MTT: 使用多目标跟踪器（MTT）融合相关测量和轨迹。

默认值: replacement

message_length <data-size-value>: 指定从图像创建的轨迹消息的逻辑长度。

默认值: 0（使用从 message_table 派生的值）

message_priority <integer-priority>: 指定从图像创建的轨迹消息的优先级。

默认值: 0（使用从 message_table 派生的值）

# 脚本接口

WSF_COHERENT_SENSOR_PROCESSOR 扩展了 WsfProcessor 脚本类，添加了以下方法：

AddSensor(string aSensorName): 将 传 感 器 按 名 称 添 加 到WSF_COHERENT_SENSOR_PROCESSOR 的传感器列表中。如果省略 aPlatformName，则假定传感器与处理器在同一平台上。  
AddSensor(string aPlatformName, string aSensorName): 将外部平台上的传感器按名称添加到传感器列表中。  
RemoveSensor(string aSensorName): 从 WSF_COHERENT_SENSOR_PROCESSOR 的传感器列表中按名称移除传感器。如果省略 aPlatformName，则假定传感器与处理器在同一平台上。  
RemoveSensor(string aPlatformName, string aSensorName): 从外部平台的传感器列表中按名称移除传感器。

这些命令和方法使 WSF_COHERENT_SENSOR_PROCESSOR 能够在复杂的传感器网络环境中有效地管理和处理传感器数据，支持更精确的目标检测和跟踪。

# 3.3.23. 延迟模拟器 WSF_DELAY_PROCESSOR

```txt
processor <name> WSF_DELAYPROCESSOR  
... processor Commands ...  
... Platform Part Commands ...  
... External Link Commands ...  
... WSFScriptPROCESSOR Commands ...  
queuing_method ...  
number_of_servers ...  
time_distribution ...  
end Processor 
```

WSF_DELAY_PROCESSOR 用于模拟处理信息所需的有限时间。当处理器接收到消息（例如，图像、轨迹）时，它将保留消息以模拟处理时间，然后通过其内部和外部链接转发消息。

通常，消息的初始生产者（如传感器）会将自己链接到此处理器，而此处理器会将自己链接到消费者。

# 命令

queuing_method [ first_in_first_out | last_in_first_out | none ]: 指定如果所有服务器都忙时，传入消息的排队方式。none 表示消息将被丢弃。默认值: first_in_first_out  
number_of_servers [ <integer> | infinite ]: 指定在任何给定时间可以“处理中”的最大消息数。如果接收到新消息且所有服务器都忙，则消息将根据 queuing_method 排队。默认值: infinite  
time_distribution constant time <time-value>: 定义模拟处理时间为指定时间的常量值。默认值: constant time 0 seconds  
time_distribution uniform minimum_time <min-time-value> maximum_time<max-time-value>: 定义消息的模拟处理时间将从指定范围的均匀分布中抽取。  
time_distribution gaussian mean_time <mean-time-value> sigma_time <sigma-time-value>:定义消息的模拟时间将从具有指定均值和标准差的高斯分布中抽取。  
time_distribution log_normal mean_time <mean-time-value> sigma_time<sigma-time-value>: 定义消息的模拟时间将从具有指定均值和标准差的对数正态分布中抽取。

# 3.3.24. 方位查找处理器 WSF_DIRECTION_FINDER_PROCESSOR

```txt
processor <name> WSF_DIRECTION_FINDERPROCESSOR  
... WSFLINKEDPROCESSOR Commands ...  
fuse_all_MEASUREMENTS | fuse_all_collects  
measurement_replacement_interval | collect_replacement_interval  
maximumEXPECTED_error  
use_truth_altitude  
filter  
filter_bypass  
maximum_time_diffERENCE  
minimum_baseLine_distance  
test  
end Processor 
```

WSF_DIRECTION_FINDER_PROCESSOR 是一种专用处理器，用于融合多个仅方位轨迹（例如，来自一个或多个被动系统）。这种功能与标准的 WSF“默认”融合略有不同。通常，轨迹数据会先被过滤，然后再融合。在这种情况下，必须融合原始方位轨迹数据以形成位置和位置误差数据，然后进行过滤。方向查找器处理器的产品是具有有效三角测量目标位置的融合过滤轨迹。

这种过滤是必要的，以便将三角测量误差减少到可操作的值。当报告对通过三角测量算法运行时，位置误差随着累积对数的平方根而下降。

# 典型使用结构

通常，此处理器将是仅方位传感器轨迹报告的消费者。因此，传感器将与方向查找器处理器链接，如下所示：

```txt
processor direction-finder WSF_DIRECTION_FINDERPROCESSOR end Processor   
sensor passive_sensor WSF_PASSIVE_SENSOR internal_link direction-finder   
end SENSOR 
```

方 向 查 找 器 处 理 器 的 输 出 是 包 含 有 效目标位置数据的轨迹。通常，它会与WSF_TRACK_PROCESSOR 或与外部融合节点的通信链接连接。例如：

```fortran
processor direction-finder WSF_DIRECTION_FINDERPROCESSOR processor track processor share   
end Processor   
processor track WSFTRACKPROCESSOR   
end Processor   
processor share WSFLINKEDPROCESSOR report_to commander via datalink   
end Processor   
comm datalink WSFCOMM_TRANSEIVER   
end comm 
```

# 关键功能

多 传 感 器 融 合 : 通 过 融 合 多 个 仅 方 位 传 感 器 的 轨 迹 数 据 ，WSF_DIRECTION_FINDER_PROCESSOR 能够提供更准确的目标位置估计。这种方法在军事和航空应用中尤为重要，因为它可以通过被动传感器网络提供精确的目标定位。

误差减少: 通过使用三角测量算法，随着累积报告对的增加，位置误差显著减少。这使得处理器能够提供更可靠的目标位置数据。

灵活的集成: 处理器可以与其他处理器（如 WSF_TRACK_PROCESSOR）和通信系统集成，以便在更大的系统中使用。

WSF_DIRECTION_FINDER_PROCESSOR 提供了一系列命令，用于配置和管理仅方位轨迹的融合和处理。以下是这些命令的详细说明：

fuse_all_measurements   
fuse_all_collects <boolean-value>: 如果启用，将使用给定目标的所有测量进行方向查找。否则，如果使用后的预期位置误差大于当前值，则不会融合该对。

默认值: 禁用

measurement_replacement_interval   
collect_replacement_interval <time-value>: 指定一个时间间隔，在此之后未用于方向查找的现有测量将被更新为更近期的测量。

默认值: $1 . 0 \mathsf { e } + 1 2$ （无限）

maximum_expected_error <length-value>: 指定单一维度中预期方向查找误差值不应超过的最大值。

默认值: 100000 m

use_truth_altitude <boolean-value>: 指定在报告空中目标位置时应使用实际高度。

默认值: 禁用

filter…end_filter: 将过滤器类型与此处理器关联。所有没有过滤器的传入轨迹将被分配此类型。如果未指明此命令，将使用 WsfKalmanFilter 类型。

默认值: WsfKalmanFilter，零过程噪声

filter_bypass <flag>: 允许绕过过滤器，使输出为“测量”，即成功三角测量的交点。

默认值: 过滤器启用

minimum_baseline_distance <length-value>: 指定正在融合的测量对的原点位置之间的最小距离。

默认值: $1 0 \ k \mathsf { m }$

maximum_time_difference <time-value>: 指定测量之间允许的最大时间差。超过此时间差的测量将不被融合。这有助于减少目标移动时的误差。如果未包含此字段，则没有最大时间差——假设其他条件相同，所有对将被融合。

默认值: $1 . 0 \mathsf { e } + 1 2$ （无限）

test <boolean-value>: 启用诊断消息输出和基于 WsfDraw 的每个方向查找解决方案的表示。当候选方向查找解决方案由于以下原因失败时，输出诊断消息：

□ 角度阈值测试失败：两个候选目标向量形成的内角小于两次测量的最大预期方位误差的五倍。  
□ 基 线 距 离 测 试 失 败 ： 两 个 测 量 位 置 的 原 点 之 间 的 距 离 小 于minimum_baseline_distance 命令指定的距离。  
□ 方位线发散失败：两个测量的方位线在目标方向上发散（即，它们在目标的相反方向相交）。  
□ 最大预期范围误差失败：计算的预期范围误差超过 maximum_expected_error 输入指定的值。

WsfDraw 基于解决方案的可视化显示沿轨迹方向的绿色线条，表示预期方位误差范围的红色线条，显示计算的 3D 解决方案误差范围的蓝色线条和点，以及指示计算的目标位置的点。

这些命令和设置使 WSF_DIRECTION_FINDER_PROCESSOR 能够在复杂的传感器网络环境中有效地管理和处理方位数据，支持更精确的目标检测和跟踪。

# 3.3.25. 信息传播处理器 WSF_DISSEMINATE_C2

```txt
processor <name> WSF_DISSEMINATE_C2  
WSFScriptPROCESSOR Commands ...  
routing_style [next_unit|next_c2|direct]  
routing_table 
```

```ini
track Updates [peer|commander|dynamic|none]
assign_trackUpdates [peer|commander|dynamic|none]
assignments [peer|commander|dynamic|none]
assignment_status [peer|commander|dynamic|none]
assignment Cancel [peer|commander|dynamic|none]
sensor_cue [peer|commander|dynamic|none]
status [peer|commander|dynamic|none]
end=routing_table
end Processor 
```

WSF_DISSEMINATE_C2 是一个脚本基类，专为基于 HELIOS 的 C^2（Command andControl）传播模型继承而设计。它并不作为一个独立的处理器使用，而是为传播 C^2 模型提供所有传播处理器中常见的脚本功能。

脚本接口

WSF_DISSEMINATE_C2 利用 Common Script Interface 和 WSF_SCRIPT_PROCESSOR 的功能，提供了一系列命令来管理信息传播。

# Disseminate C2 命令

routing_style [next_unit | next_c2 | direct]: 指定在 IADS 网络中确定下一跳的消息路由风格。

□ next_unit: 消息将发送到通往目的地的下一个单元。  
next_c2: 消息将发送到通往目的地的下一个被指定为 C^2 能力的单元。  
□ direct: 消息将直接发送到消息目的地。

默认值: next_c2

# 路由表命令

用于定义 HELIOS C^2 传播消息路由表的块。所有值可以是以下之一：[peer |commander | dynamic | none]。

track_updates [peer | commander | dynamic | none]: 设置轨迹消息的路由。

默认值: none

assign_track_updates [peer | commander | dynamic | none]: 设置分配轨迹的路由。

默认值: dynamic

assignments [peer | commander | dynamic | none]: 设置分配的路由。

默认值: dynamic

assignment_status [peer | commander | dynamic | none]: 设置分配状态的路由。

默认值: dynamic

assignment_cancel [peer | commander | dynamic | none]: 设置分配取消的路由。

默认值: dynamic

sensor_cue [peer | commander | dynamic | none]: 设置传感器提示的路由。

默认值: none

这些命令和设置使 WSF_DISSEMINATE_C2 能够在复杂的 C^2 网络环境中有效地管理信息传播，确保指挥和控制信息的准确传递和处理。

示例

```txt
routing_table
# Routing values allowed are subordinate, peer, commander, dynamic, none. multiple entries can exist
# for a given type of message.
track Updates none
assign_trackUpdates dynamic
assignments dynamic
assignment_status dynamic
assignment Cancel dynamic
sensor_cue dynamic
status commander
endRouting_table 
```

# 3.3.26. 消息处理器 WSF_DUMP_MESSAGE_PROCESSOR(弃用)

```txt
processor <name> WSF_DUMP_MESSAGEPROCESSOR Platform Part Commands ... External Link Commands ... verbose end Processor 
```

WSF_DUMP_MESSAGE_PROCESSOR 是一个非常简单的处理器，主要用于调试。它的功能是接收消息，打印出有关消息的信息，然后通过其内部和外部链接转发数据。该处理器在版本 1.7.4 中已被弃用。

输出格式

输出的格式如下：

```txt
s.ffff platform-nameprocessor-name Number: message-number Type: message-type Size: size-in-bits 
```

如果启用了详细输出，还会包含指定的详细信息。

命令

verbose: 生成关于某些已知消息的详细输出。目前，这仅限于 WsfTrackMessage 和WsfTrackDropMessage。

默认值: 不包括详细信息

使用注意事项

调试用途: 由于其简单性和直接性，WSF_DUMP_MESSAGE_PROCESSOR 非常适合用于调试目的，帮助开发人员快速查看和分析消息流。

弃用状态: 请注意，该处理器在版本 1.7.4 中已被弃用，因此在新项目中可能需要寻找替代方案。

# 3.3.27. 信息交换处理器 WSF_EXCHANGE_PROCESSOR

```txt
processor <name> WSF_EXCHANGEPROCESSOR  
... processor commands ...  
... Platform Part Commands ...  
... Exchange Processor Commands ...  
... Exchange Processor Script Interface ...  
container <name>  
...  
end(transactor  
transactor <name>  
...  
end(transactor  
end Processor 
```

WSF_EXCHANGE_PROCESSOR 是一个处理器，用于管理与其他模拟平台之间的商品或服务交换。它可以用于多种场景，例如油轮与接收器之间的燃料交换、仓库向需要零件的机械师提供备件，或机械师前往故障飞行器进行维修并使其恢复服务。

# 交换过程

交换通过一系列的“乒乓”协商事件进行，结果是双方共同决定的交换数量，以及可选的交换速率。如果没有指定速率，交换速率默认为零，因此被视为瞬时。如果协商了非零速率，则双方理解交换正在进行中，直到根据经过的时间完成全部交易。在此情况下，任何一方都可以提前取消交易，已交易的部分将被保留。

# 关键组件

数量: 交换的数量可以是任何实现定义的方便单位。如果交换的商品与 WSF 平台的有效载荷或燃料相关联以影响运动动力学，则单位必须在内部指定为千克。否则，单位可以是任意浮点值，如“供应托盘”、“备用引擎”或“机翼维修次数”。

Tender（投标）: 封装商品或服务的请求或报价。它指定商品或服务的名称、最大需求或可提供的数量、最大传输速率，以及一个标志指示该项目是商品还是服务。

Container（容器）: 放置在 WSF_EXCHANGE_PROCESSOR 上，指定可以存储以供以后提供的项目的最大数量，或平台上可以一次积累的最大数量。

Transactor（交易者）: 是商品或服务可以进入或离开指定容器的通道。流动方向（‘is_offeror’ 或 ‘is_requestor’）在创建交易者时指定，之后不能更改。

# 交换过程

预留: 一个‘is_offeror’交易者预留或设置某些商品或服务的投标。

请求: 另一个平台上的‘is_requestor’交易者可以请求投标。

协商: 如果预留和请求在名称和服务/商品类型上兼容，并且足够接近，则开始协商实际数量和交易速率。

交易: 事件 REQUEST, OFFER, ACCEPT, SUPPLY, RECEIVE 依次发生，协商交换的数量和服务速率。

取消: 任何一方可以通过 CANCEL 事件提前终止交易，已交易的部分将被保留。

事件和脚本接口

事件: 交换过程会生成 WSF 可观察事件：EXCHANGE_QUERIED, EXCHANGE_NEGOTIATED,和 EXCHANGE_COMPLETED。

脚本接口: 用户可以通过脚本接口控制交易的收件人、时间、数量和速率。

# 质量影响

WSF_EXCHANGE_PROCESSOR 允许其容器可选地连接到有效载荷或燃料，以便交换的商品立即影响平台的总质量。这通过 hook_to_payload 和 hook_to_fuel 关键字选项实现。通过这些功能，WSF_EXCHANGE_PROCESSOR 提供了一个灵活的框架，用于模拟复杂的商品和服务交换场景，支持更真实的模拟环境。

# 商品交易状态机如下：

_Transactor_Role_ Begin_State_ End_State_Generated_Event_ Offeror -disabled- READY -none- Receiver READY REQUESTING REQUESTED Offeror READY OFFERING OFFERED Receiver REQUESTING ACCEPTING ACCEPTED Offeror OFFERING SUPPLYING SUPPLIED $\Rightarrow$ <Begin transfer in progress timer> Receiver ACCEPTING READY RECEIVED $\Rightarrow$ <Begin transfer in progress timer> <For the offeror and receiver, when the timer elapses, the transaction is fully completed >

# 服务交易状态机如下：

_Transactor_Role_ Begin State End State_Generated_Event_Offeror -disabled- READY _none- Receiver READY REQUESTING REQUESTED Offeror READY OFFERING OFFERED Receiver REQUESTING ACCEPTING ACCEPTED Offeror OFFERING SUPPLYING SUPPLIED $\equiv$ <Begin repair in progress timer> <repair in progress timer expires> Offeror SUPPLYING READY OFFEROR_COMPLETED Receiver ACCEPTING READY REQUESTOR_RESPONSEED Offeror READY READY <confirmation received, but no action needed>

# 取消交易

任何交易者都可以取消正在进行的交易，这将生成事件 CANCEL 以通知另一方，因此CANCEL 可能是内部或外部生成的事件。如果在交换过程中另一方没有响应，取消会自动在内部排队作为超时机制。假设后续交易协商成功，时间排队的取消将被忽略。

# 商品交换示例

一个典型的商品交换示例是空中加油机类型的平台从其有效载荷数量中卸载燃料，并将其供应给附近的飞机以补充其燃料数量。以下是具有供应燃料能力的加油机平台类型的声明

```txt
platform_type TANKER WSFPLATFORM processor exchange_proc WSF_EXCHANGEPROCESSOR update_interval 5 sec 
```

```txt
commodity_and_capacity_pairing JP8_FUEL SUPPLY_FUEL   
container fuel_supply-tank commodity JP8_FUEL maximum_mass的数量 8000 kg mass_rate 50 kg/sec end_commodity initial_mass的数量 7000 kg   
end-container   
transactor fuelprovider container_name fuel supply_tank is Offeror hook_to_fuel false hook_toPGA payload true exclusive-hook_toPGA true response_time_out_interval 10 sec proximity_limit 500 m   
end_transactor   
end Processor   
endPLATFORM_type 
```

# DIS 网络中的远程交换

如果 DIS 网络配置正确，商品或服务的交换可以与外部 DIS 实体进行。在这种情况下，必须在 DIS 环境中声明要交换的商品或服务类型，如下所示：

```txt
dis_INTERFACE entity_type JP8_FUEL 6:0:0:0:1:4 dis_exchange debug end_dis_exchange end_dis-interface 
```

在通过 DIS 进行的所有远程交换中，上述序列中划定的每个状态机转换触发事件必须在本地模拟和远程模拟中各发生一次。本地事件触发一个回调机制，该机制将适当的 DISPDU 类型发送到外部。在远程目的地接收到该 PDU 将触发与本地模拟中先前事件相同的事件。

# Tender 定义

在输入流中，用户可以通过两种方式构建 Tender：作为商品或服务。

# 商品 Tender

commodity <commodity-name> … #Tender Commands <tender_body> … end_commodity

商品 Tender 用于提议交换一些命名的有形商品，注明计划请求或提供交换的种类、数量和速率。它不指定流动方向，流动方向由交易者的 is_offeror 或 is_requestor 设置决定。

# 服务 Tender

service <service-name> … #Tender Commands <tender_body> … end_service

服务 Tender 用于提议交换一些命名的无形服务，注明计划请求或提供交换的种类、数量和速率。它不指定流动方向，流动方向由交易者的 is_offeror 或 is_requestor 设置决定。

# Tender 命令

quantity <real-value>: 指定当前可用或所需的服务数量。  
maximum_quantity <real-value>: 指定可用或所需服务的限制数量。用于指示容器的最大尺寸的语法便利。  
mass_quantity <mass-value>: 指定当前可用或所需商品的质量。  
maximum_mass_quantity <mass-value>: 指定可用或所需商品的限制数量。用于指示容器的最大尺寸的语法便利。

# Container 定义

container <container-name> … #Container Commands <container_body> … end_container<container-name>: 指定对象的名称，用于 WSF_EXCHANGE_PROCESSOR 区分可能由处理器拥有的多个容器。容器块量化一个容器；其名称、所持有的内容、商品或服务的最大和当前数量。虽然服务（如发动机维修）不是可以放在容器中的有形物品，但为了模拟记账的目的，它被视为这样的物品。交易总是“管道”进出一个命名的容器。任何交易都不允许转移超过容器最大容量和当前数量所允许的商品或服务。约束操作将始终限制/夹住交易以遵守容器的约束。可以根据需要定义任意数量的容器，并且一个容器可以有多个交易“管道”进入，例如加油机可以同时从另一个加油机装载燃料并向接收器卸载燃料，两个都链接到同一个容器。

# Container 命令

service …end_service: 指定服务类型、数量和交换速率，如上面的 Tender 定义中所述。只能提供一个“服务”或“商品”。  
commodity …end_commodity: 指定商品类型、数量和交换速率，如上面的 Tender 定义中所述。只能提供一个“服务”或“商品”。  
initial_quantity <real-value>: 指定容器中可用服务的初始数量，必须小于或等于上述投标规格中的最大容器大小。  
initial_mass_quantity <mass-value>: 指定容器中可用商品的初始质量，必须小于或等于上述投标规格中的最大容器大小。

# Transactor 定义

transactor <transactor-name> … #Transactor Commands <transactor_body> … end_transactor

<transactor-name>: 指定对象的名称，用于 WSF_EXCHANGE_PROCESSOR 区分可能由处理器拥有的多个交易者。交易者块量化一个交易；其名称、商品或服务的流动方向，以及正在进行的交易的当前数量。无论方向如何，数量随着交易的进行趋向于零（is_offeror 从可用数量开始，当耗尽时达到零，is_requestor 从所需数量开始，当完全满足时达到零）。交易总是“管道”进出一个命名的容器。无论 Reserve() 或 Request() 的初始数量如何，交易仅在被限制为可以从命名容器中获取或适合命名容器后开始。

# Transactor 命令

is_offeror: 将交易者配置为商品或服务的提供者。

is_requestor: 将交易者配置为商品或服务的请求者。  
hook_to_fuel <boolean-value>: 在每次成功交易后，交易者将增加或减少其平台上的燃料数量。不会减少到零以下。  
hook_to_payload <boolean-value>: 在每次成功交易后，交易者将增加或减少其平台上的有效载荷数量。不会减少到零以下。  
exclusive_hook_to_payload / exclusive_hook_to_fuel: 交易者将直接控制有效载荷或燃料的数量，强制其与当前命名容器中的数量匹配。它将被允许忽略并覆盖任何其他设置燃料或有效载荷数量的过程，包括输入文件规范。不会减少到零以下。  
proximity_limit <length-value>: 指定两个平台之间允许的最大距离以进行交换。默认值为零，或忽略距离。  
time_out_clock_interval <time-value>: 指定等待对报价或请求的响应的最大间隔。如果收到请求，并发出相应的报价，然后没有收到响应，则在此时间段后取消报价，以便释放交易者以向另一个请求者提供服务。

# Exchange Processor 命令

commodity_and_capability_pairing <commodity-name> <capability-type>: 该关键字在商品名称和平台能力之间创建关联，如在 DIS 实体状态 PDU 中提供的那样。如果交换处理器有一个交易者当前提供燃料商品，那么该处理器将确保平台能力“SUPPLY_FUEL”被标记为存在。其他位可能指示燃料或有效载荷可以提供，但只有在使用上述关键字正确指示时才会如此。可以提供多个配对。  
service_and_capability_pairing <service-name> <capability-type>: 该关键字在服务类型名称和平台能力之间创建关联，如在 DIS 实体状态 PDU 中提供的那样。如果交换处理器有一个交易者当前提供维修服务，那么该处理器将确保平台能力“VEHICLE_REPAIR”被标记为存在。其他位可能指示飞行器维修或飞行器恢复可用，但只有在使用上述关键字正确指示时才会如此。可以提供多个配对。（能力自动化数据服务 - 广播（ADS_B）目前不支持。）  
ignore_all_proximity_checks <boolean-value>: 如果设置为 true，命令将忽略并覆盖所有交易者的‘proximity_limit’值，将其强制为零。没有交易会因接近限制检查而失败。默认值为‘false’。  
force_transactions_instantaneous <boolean-value>: 如果设置为 true，命令将忽略所有投标‘rate’、‘service_interval’或‘mass_rate’的规范。一旦成功协商，结果交易将占用零模拟时间。  
debug <boolean-value>: 命令提示控制台输出以协助调试处理器操作。  
edit <object_type> <object_name> … end_<object_type>: 命令允许编辑先前命名的交易者或容器。此命令将开始一个块，必须以正常的 end_block 语法结束。在块内，可以使用任何适合所选 object_type 的命令。

# Exchange Processor 脚本接口

WSF_EXCHANGE_PROCESSOR（脚本对象名称为 WsfExchangeProcessor）利用了 CommonScript Interface 和 WSF_SCRIPT_PROCESSOR 的功能，并提供以下功能：

Transactor FindContainer(string): 如果命名的容器（第一个参数）存在，将返回与之交互的交易者的引用。使用前应检查返回的对象是否有效（IsValid()）。  
Transactor FindTransactor(string): 如果命名的交易者（第一个参数）存在，将返回与之交互的交易者的引用。使用前应检查返回的对象是否有效（IsValid()）。

Array<int> PayloadProviders(): 返回当前已知提供有效载荷的模拟实体的平台索引数组，无论其接近程度如何。  
Array<int> FuelProviders(): 返回当前已知提供燃料的模拟实体的平台索引数组，无论其接近程度如何。  
Array<int> VehicleRepairers(): 返回当前已知提供飞行器维修服务的模拟实体的平台索引数组，无论其接近程度如何。  
Array<int> VehicleRecoverers(): 返回当前已知提供飞行器恢复服务的模拟实体的平台索引数组，无论其接近程度如何。  
WsfPlatform ClosestPossibleProvider(string): 返回代表所提供商品项目名称的能力的最近已知提供者的平台的引用。使用前应检查返回的对象是否有效（IsValid()）。

一般来说，上述每种子组件类型都是可脚本化的对象，包括：‘tender’ 作为 “Tender”、‘container’ 作为 “Container”、‘transactor’ 作为 “Transactor”，以及一个新提到的可脚本化类型 “Query”。Query 类型的目的是在脚本中提供细节，以便能够辨别两个 Tenders 是否兼容。

# 3.3.28. 轨迹融合处理器 WSF_FUSION_CENTER

```txt
processor <name> WSF_FUSION_CENTER  
... Platform Part Commands ...  
... processor Commands ...  
... WSFScriptPROCESSORCommands ...  
plot_capacity <value>  
frame_time <time-value>  
track_capacity <value>  
random_to_multiple_radars  
consistent_to_multiple_radars <boolean-value>  
radar_site  
consistency_constrained <boolean-value>  
end Processor 
```

WSF_FUSION_CENTER 是一个处理器，用于关联来自不同和多个雷达站点的轨迹。必须定义以处理来自虚假目标干扰效应的虚假目标。

# 命令

plot_capacity <value>: 定义可以在雷达范围内绘制的目标数量。

默认值: 2000

frame_time <time-value>: 定义融合中心的更新速率，以秒为单位。

默认值: 5.0 秒

track_capacity <value>: 定义融合中心可以维护的轨迹数量。

默认值: 500

random_to_multiple_radars: 定义将在任何雷达上出现的虚假目标被拒绝的比例。

默认值: 0.0

consistent_to_multiple_radars <boolean-value>: 定义将在多个雷达上出现的虚假目标被拒绝的比例。

默认值: 0.0

radar_site: 指定要融合的雷达站点的名称。对于每个雷达站点重复此命令。名称指的是雷达平台的玩家名称。  
consistency_constrained <boolean-value>: 定义轨迹是否必须由所有雷达站点检测到才能被融合中心融合。False 表示轨迹只需出现在一个雷达站点上即可。

默认值: true

# 3.3.29. 武器制导处理器 WSF_GUIDANCE_COMPUTER

```shell
processor <name> WSF GUIDANCE COMPUTER   
... WSFScriptPROCESSORCommands ...   
# Global Commands   
show_status   
show_diagnostics   
show Commands   
showvaluations   
guide_to_truth ...   
program ... end program   
phase <phase-name-1>   
# General Subcommands   
guidance_delay ...   
on_entry ... end_on_entry   
on_exit ... end_on_exit   
on_update ... end_on_update   
#AimpointSelectionSubcommands   
guidance_target... | guide_to_truth   
allow-routefollowing...   
aimpoint_altitude_offset...   
aimpoint_azimuth_offset...   
aimpoint_range_offset...   
aimpoint.evaluation_interval...   
#ProgramSelectionCommands   
use_program ..   
program ... end PROGRAM 
```

# Navigation Subcommands

proportional_navigation_gain ...

proportional_navigation_limit_angle ...

proportional_navigation_method ...

velocity_pursuit_gain ...

# Trajectory Shaping Subcommands

g_bias ...

lateral_g_bias ...

commanded_altitude ...

commanded_azimuth_offset ...

commanded_flight_path_angle ...

commanded_mach ...

commanded_speed ...

commanded_throttle ...

# Limiting Subcommands

maximum_commanded_g ...

maximum_ascent_rate ...

maximum_descent_rate ...

maximum_pitch_angle ...

pitch_change_gain ...

# Phase Changing Subcommands

next_phase ...

end_phase

phase <phase-name-n>

end_phase

# Script Interface

script_variables ... end_script_variables

script ... end_script

on_initialize ... end_on_initialize

on_initialize2 ... end_on_initialize2

on_update ... end_on_update

... Other Script Commands ...

WSF_GUIDANCE_COMPUTER 是一个通常位于武器上的处理器，为通常类型为WSF_GUIDED_MOVER 的武器提供制导。它使用通过 CurrentTargetTrack 提供的轨迹来表示要追踪的目标。移动器调用此处理器以请求制导更新。处理器计算所需的制导并将其提供回移动器。

制导程序

从 AFSIM2.2 开始，通过使用“程序”提供了一种额外的制导形式。与现有的制导方法相比，程序具有几个优势：

▫ 无隐藏行为: 在旧系统中，如果不需要比例和追踪制导以及重力偏差，必须显式禁用它们。使用新系统，除非请求，否则不会获得这些功能。  
□ 跨阶段的程序: 可以定义一个程序并使用它，以便在阶段变化时保留其状态。  
□ 多程序执行: 可以在一个阶段中执行多个程序以获得组合效果。  
▫ 可扩展的程序架构: 可以轻松添加新的程序类型。如果特定应用需要新的制导模型，可以像其他模型一样编译并包含。

AFSIM 2.2 中提供的初始程序集主要用于实现发射到轨道的能力和一些先进的弹道导弹需求。因此，最初不会满足所有需求。

制导程序或传统制导的使用是按阶段选择的。如果在一个阶段中使用或定义程序，则只会使用程序。如果在一个阶段中不使用或定义程序，则会获得传统行为。每个阶段可以不同一个可以使用程序，另一个可以使用传统制导。

这种灵活性和可扩展性使得 WSF_GUIDANCE_COMPUTER 能够适应不同的制导需求和应用场景。

WSF_GUIDANCE_COMPUTER 提供了一系列全局命令，用于控制制导计算机的行为和输出。

show_status: 指定在阶段或阶段转换发生时信息应写入标准输出。  
show_diagnostics: 指定来自制导程序的诊断信息应写入标准输出。通常在尝试调整制导计算机以生成轨道发射计算机时使用。

注意: 这会引入一些额外的开销，应仅在调整期间使用。

show_commands: 指定来自脚本命令的调用应写入标准输出。  
show_evaluations: 指定阶段更改规则评估应写入标准输出。  
guide_to_truth <boolean-value>: 指定制导目标是否应为当前目标轨迹中指定的位置（false），或应为当前目标轨迹中指定的平台的真实位置（true）。

注意: 此命令在此处和‘phase’块中都存在。如果在阶段块中未指定命令，则此形式指定阶段的默认值。

默认值: false

phase <phase-name> phase-commands end_phase: ‘phase’块用于定义飞行各阶段的制导以及阶段之间转换的规则。

格式:

```txt
phase <phase-name>
    ... phase commands ...
end_phase 
```

每个所需的唯一阶段都应定义‘phase’块。第一个‘phase’块定义武器发射时要使用的阶段。

edit phase <phase-name> phase-commands end_phase: 通常在通过从另一种制导计算机类型派生来创建新的制导计算机类型时使用。

```txt
processor DEMO GUIDANCE WSF GUIDANCE COMPUTER guide_to_truth true phase TERMINAL end_phase end Processor DEMO GUIDANCE_MOD DEMO GUIDANCE edit phase TERMINAL guide_to_truth false #覆盖基类值 end_phase end Processor 
```

program <name> <type> … end_program: 使用指定的<name>和预定义的制导程序<type>定义制导程序。然后可以通过指定 use_program<name> 在阶段中选择使用该程序。

注意: 程序必须在引用该程序的 use_program 之前出现在输入中。

示例:

```txt
program RESETAttITUDE ATTITUDE PROGRAM reset yaw_rate 5 deg/sec pitch_rate 5 deg/sec roll_rate 5 deg/sec   
endProgram   
...   
phase BEGIN DESCENT use_program RESET ATTITUDE next_phase DESCENT when program RESET ATTITUDE complete   
end_phase   
...   
phase DESCENT   
...   
end_phase 
```

阶段命令

阶段块中的子命令可以分为以下广泛类别：

▫ General Subcommands: 一般子命令。  
□ Aimpoint Selection Subcommands: 指定如何确定目标点。  
□ Program Selection Subcommands: 选择或定义要执行的制导程序。  
□ Navigation Subcommands: 指定如何导航到目标点。  
□ Trajectory Shaping Subcommands: 指定在导航时如何修改轨迹。  
▫ Limiting Subcommands: 指定计算的限制。  
□ Phase Changing Subcommands: 根据多个条件转换到其他阶段。

这些命令和结构使得 WSF_GUIDANCE_COMPUTER 能够灵活地适应不同的制导需求和应用场景。

WSF_GUIDANCE_COMPUTER 一般子命令 General Subcommands

WSF_GUIDANCE_COMPUTER 提供了一些一般子命令，用于控制制导计算机在不同阶段的行为。

guidance_delay <time-value>: 指定自阶段开始以来经过的时间，在此时间后开始计算制导命令。这在起飞和其他不希望追踪目标的阶段中很有用。

默认值: 0 秒（进入阶段时开始计算制导命令）

脚本命令: WsfGuidanceComputer.SetGuidanceDelay

on_entry … end_on_entry 和 on_exit … end_on_exit: 定义在进入和退出阶段时执行的脚本。

```txt
on_entry
    ... script commands ...
end_on_entry
on_exit
    ... script commands ...
end_on_exit 
```

on_update … end_on_update: 定义在每次阶段更新时执行的脚本。

```txt
on_update ...script commands... end_on_update 
```

通常仅在以下情况下使用：

1. 在一个阶段中需要改变制导命令的值。  
2. 需要评估无法通过 next_phase 命令完成的阶段更改条件。

注意: 不要随意使用，因为它在移动器的每个集成时间步执行。尽量保持脚本简单。

瞄准点选择子命令 Aimpoint Selection Subcommands

guidance_target [ predicted_intercept | perception | truth ]: 为 当 前 阶 段 覆 盖 顶 级guide_to_truth 命令。选项包括：

□ predicted_intercept: 基于发射计算机提供的预测拦截位置进行制导计算。  
□ perception: 基于当前目标轨迹提供的目标感知进行制导计算。  
□ truth: 基于目标的实际位置进行制导计算。  
□ default: 使用全局 guide_to_truth 命令的值。

默认值: default

脚本命令: WsfGuidanceComputer.SetGuidanceTarget

aimpoint_altitude_offset <length-value>: 修改瞄准点以位于感知目标位置的上方或下方，通常用于制造空中爆炸。

默认值:0 米（无高度偏移）

脚本命令: WsfGuidanceComputer.SetAimpointAltitudeOffset

aimpoint_azimuth_offset <angle-value> [ left | right | either ] 和 aimpoint_range_offset<length-value>: 提供一种方法来生成相对于感知目标位置的横向偏移瞄准点，通常用于满足某些战术要求。  
aimpoint_azimuth_offset: 当地面距离等于 aimpoint_range_offset 指定的值时，目标的相对方位角。left,right,either: 指示目标相对于武器的位置。

示例

```txt
phase PHASE_X  
...  
aimpoint_altitude_offset 10000 m  
aimpoint_azimuth_offset 45 deg either  
aimpoint_range_offset 10 nm  
next_phase PHASE_Y when target_azimuth > 45 deg  
end_phase 
```

默认值: 无瞄准点偏移

脚 本 命 令 · WsfGuidanceComputer.SetAimpointAzimuthOffset 和WsfGuidanceComputer.SetAimpointRangeOffset

注意: 如果 aimpoint_azimuth_offset 或 aimpoint_range_offset 非零，则两者都必须非零。瞄准点偏移在跟随路线时不会应用。通常仅用于静止或缓慢移动的地面目标，未针对空中目标进行测试。

aimpoint_evaluation_interval <time-value>: 控 制 使 用 aimpoint_azimuth_offset 和aimpoint_range_offset 时计算新瞄准点的频率。

默认值:5 秒

脚本命令: WsfGuidanceComputer.SetAimpointEvaluationInterval

allow_route_following <boolean-value>: 如果为 true，计算机将在提供给关联移动器的情况下跟随路线。如果移动器没有路线，则此命令无效。常规目标点选择将在路线结束

时恢复。

命令: next_phase <phase-name> at_end_of_route 可用于在遇到路线结束时切换到不同阶段。

默认值: false

脚本命令: WsfGuidanceComputer.SetAllowRouteFollowing

# Program Selection Subcommands

在阶段内指定将使用的制导程序。可以选择或定义一个或多个程序，并按出现顺序调用。

use_program<name>: 指定在阶段外的程序块中定义的命名程序将被使用。如果一个程序将在多个阶段中使用，定义一个程序是有用的。  
program <type> end_program: 定义指定类型的程序并在当前阶段使用。<type> 必须是预定义的制导程序类型之一（参见：3.3.29.1 导航程序类型 Guidance Program Types）。

# Navigation Subcommands

proportional_navigation_gain <real-value>: 指定比例导航的增益。值为零表示不执行比例导航。

默认值: 3.0

脚本命令: WsfGuidanceComputer.SetProportionalNavigationGain

proportional_navigation_limit_angle <angle-value>: 指定目标相对于武器的 3D 视角角度，在此角度下导航方法将在比例和速度追踪之间切换。如果目标视角角度小于或等于此值，则使用比例导航，否则使用速度追踪。

默认值: 30.0 度

脚本命令: WsfGuidanceComputer.SetProportionalNavigationLimitAngle

proportional_navigation_method [ pure | augmented ]: 指定是否由于当前目标加速度而应命令额外加速度。

默认值: pure（忽略目标加速度）

脚本命令: WsfGuidanceComputer.SetProportionalNavigationMethod

velocity_pursuit_gain <real-value>: 指定速度追踪导航的增益。值为零表示不执行速度追踪导航。

默认值: 10.0

脚本命令: WsfGuidanceComputer.SetVelocityPursuitGain

轨迹塑形子命令 Trajectory Shaping Subcommands

轨迹塑形子命令用于修改计算出的导航命令以塑造轨迹。

g_bias <real-value>

指定用于克服重力的偏置因子。通常在中途使用以防止轨迹下垂。如果指定为零，则不会应用重力偏置。

默认值：1.0

脚本命令： WsfGuidanceComputer.SetGeeBias

lateral_g_bias <real-value>

指定用于在特定方向上倾斜轨迹水平分量的偏置因子。如果指定为零，则不会应用重力偏置。

默认值：0.0

脚本命令： WsfGuidanceComputer.SetLateralGeeBias

commanded_altitude <length-value> [ msl | agl ]

指定命令的高度。通常用于爬升或下降到巡航高度并保持高度。高度参考标签（‘msl’，或‘平均海平面以上’；‘agl’，或‘地面以上’）可以省略，在这种情况下，假定为‘msl’。

指定‘agl’的高度参考是实现地形跟随的一种粗略机制。当指定‘agl’时，移动物体将强制执行一个额外的约束，即始终保持在地面以上。然而，不会进行前瞻性检查（它只检查平台正下方的地形高度），因此如果地形迅速上升，飞行器可能会做出非常突然的变化。

默认值：无命令高度

脚 本 命 令 ： WsfGuidanceComputer.SetCommandedAltitude 和WsfGuidanceComputer.SetCommandedAltitudeAGLcommanded_azimuth_offset <angle-value>

指定应保持的目标方位角。该角度定义为武器速度矢量与从武器到目标的视线矢量之间的局部水平面内的角度。（这与 next_phase 命令中的‘target_azimuth’条件测试一致。）

默认值：无命令方位偏移角

脚本命令： WsfGuidanceComputer.SetCommandedAzimuthOffset

commanded_flight_path_angle <angle-value>   
commanded_flight_path_angle from_launch_computer

指定命令的飞行路径角。如果指定了 from_launch_computer，则将使用发射计算机产生的值（如果存在）。

通常用于产生抛物线弹道轨迹。

默认值：无命令飞行路径角

脚本命令： WsfGuidanceComputer.SetCommandedFlightPathAngle

commanded_mach <real-value>   
commanded_speed <speed-value>

指定在此阶段使用的命令速度/马赫数。通常用于巡航。

默认值：无命令速度或马赫数

脚 本 命 令 ： WsfGuidanceComputer.SetCommandedSpeed 和WsfGuidanceComputer.SetCommandedMach

注意： 并非所有移动物体都支持此功能。使用此命令时，燃料利用可能无法正确建模。

commanded_throttle <real-value>

指定一个范围为[0..1]的油门因子，覆盖移动物体中的油门规格。

这通常不作为命令使用。它主要存在以允许脚本调用改变油门。

默认值：无命令油门

脚本命令： WsfGuidanceComputer.SetCommandedThrottle

限制子命令 Limiting Subcommands

maximum_commanded_g <acceleration-value>

指定可以命令的最大加速度的大小。

默认值： $2 5 . 0 { \mathrm { g } }$

脚本命令： WsfGuidanceComputer.SetMaximumCommandedGees

maximum_ascent_rate <speed-value>   
maximum_descent_rate <speed-value>

指定用于达到命令高度的最大上升或下降速度。

注意： 值为 0 表示对上升/下降速度没有限制。

脚 本 命 令 ： WsfGuidanceComputer.SetMaximumAscentRate 和WsfGuidanceComputer.SetMaximumDescentRate

默认值：0，无限制

maximum_pitch_angle <angle-value>

指定用于上升或下降到命令高度的最大飞行路径角的绝对值。

默认值：70.0 度

脚本命令： WsfGuidanceComputer.SetMaximumPitchAngle

pitch_change_gain <real-value>

指定在尝试达到命令高度时改变俯仰角的增益因子。

默认值：1.0

脚本命令： WsfGuidanceComputer.SetPitchChangeGain

阶段转换子命令 Phase Changing Subcommands

next_phase <phase-name> [if | when] <event> next_phase <phase-name> [if | when] <variable> [<operator> <reference-value>]

next_phase 命令用于定义阶段转换发生的条件。一个阶段块可以有多个 next_phase 命令，以定义可能触发阶段变化的多个条件。next_phase 命令在每次导航更新时进行评估，并按指定顺序进行评估。

第一种形式的命令用于检测事件：

▫ end_of_route：移动器指示已通过路线中的最后一个点（如果移动器在跟随航路点）。  
□ boost_complete：移动器指示不再推进。这通常意味着所有的推力产生阶段已被使用。  
□ stage_ignition：移动器指示当前阶段已点火。  
□ stage_burnout：移动器指示当前阶段已燃尽。  
□ stage_separation：移动器指示当前阶段已分离。  
□ on_commanded_flight_path_angle：武器的飞行路径角已达到发射计算机命令的抛物角（如果提供）。  
□ sensor_track_initiated：本地车载传感器已对目标建立自主跟踪。  
□ program <program-name> complete：指定的程序已完成。并非所有程序都有定义完成的条件。这些程序是连续的，将运行到阶段结束。

第二种形式的命令用于检测当 <variable> 达到与 <reference-value> 的某种关系时：

<reference-value> 可以是以下形式的常量值：

```txt
<real-value> <units> 
```

或者是以下形式的变量值：

```txt
/variable *<variable-name>  
variable *<variable-name>* *<units> 
```

后两种形式表示 <reference-value> 是从一个双脚本变量中获取的。变量必须在引用变量的命令之前的 script_variables 块中定义，并且不能出现在“阶段”块中。

如果变量是一个有量纲的量，则变量的值必须使用正确的单位：

如果指定了 /variable，则使用标准 WSF 单位。标准单位在下表的“描述”列中指示。

如果指定了 variable，则使用指定的 <units> 单位。

使用变量形式时，<variable-name> 必须是一个双脚本变量的名称，<units> 表示存储在变量中的数据的单位。变量必须在计算机中出现在引用之前的 script_variables 块中定义。

有效的 <operators> 是 $< , < = , = = , \ : ! = , > = ,$ 或 >。有效的 <variables> 包括：

□ phase_time：自阶段开始以来经过的时间（秒）。  
□ flight_time：自平台发射以来经过的时间（秒）。  
□ altitude：武器的当前高度（米）。  
□ speed：武器的当前速度（米/秒）。  
□ vertical_speed：武器的当前垂直速度（米/秒）。  
□ flight_path_angle：武器的当前飞行路径角（弧度）。  
□ dynamic_pressure：武器上的当前动态压力（牛顿/米²）。  
□ target_altitude：目标的当前高度（米）。  
□ target_speed：目标的当前速度（米/秒）。  
▫ target_flight_path_angle：目标的当前飞行路径角（弧度）。  
□ closing_speed：武器与目标之间的闭合速度（米/秒）。正值表示闭合。  
▫ time_to_intercept：预计武器与目标拦截的时间（秒）。  
□ range_to_intercept：武器与目标之间预计拦截点的距离（米）。  
□ target_slant_range：武器与目标之间的斜距（米）。  
□ target_ground_range：武器与目标之间的地面距离（米）。  
□ target_elevation：从武器到目标的视线矢量与当地水平面（地球表面的切线）之间的角度（弧度）。正值表示目标在当地水平面之上，负值表示在其下。  
□ target_azimuth：武器速度矢量的水平分量与从武器到目标的视线矢量之间的角度（弧度）。此值始终为正。  
□ los_target_elevation：目标相对于武器当前方向的仰角（弧度）。  
□ los_target_azimuth：目标相对于武器当前方向的方位角（弧度）。此值始终为正。  
□ los_target_angle：目标相对于武器当前方向的三维角度（弧度）。

使用事件的示例：

```txt
next_phase PHASE2 if end_of-route  
next_phase PHASE2 if boost_COMPLETE  
next_phase PHASE2 if stageIgnition  
next_phase PHASE2 if stage_burnout  
next_phase PHASE2 if stage_separation  
next_phase PHASE2 when on commanded_flow_path_angle  
next_phase PHASE2 when sensor_track_initiated  
next_phase PHASE2 when FLIGHT_PATH_ANGLE_PROGRAM complete 
```

使用常量作为参考值的示例：

```perl
next_phase PHASE2 when phase_time > 200 sec  
next_phase PHASE2 when flight_time > 25 sec  
next_phase PHASE2 when altitude > 10000 m  
next_phase PHASE2 when speed > 500 m/s  
next_phase PHASE2 when vertical_speed > 100 m/s  
next_phase PHASE2 when target_altitude > 10000 m  
next_phase PHASE2 when target_speed > 500 m/s 
```

```txt
next_phase PHASE2 when closing_speed > 1000 m/s  
next_phase PHASE2 when time_to_intercept < 1 sec  
next_phase PHASE2 when range_to_intercept < 1 m  
next_phase PHASE2 when target_slant_range < 1 m  
next_phase PHASE2 when targetGround_range < 1 m  
next_phase PHASE2 when target_azimuth > 179 deg  
next_phase PHASE2 when target_elevation > 89 deg  
next_phase PHASE2 when los_target_azimuth > 179 deg  
next_phase PHASE2 when los_target_elevation > 89 deg  
next_phase PHASE2 when los_target_angle > 179 deg  
next_phase PHASE2 when altitude > 10 km 
```

使用脚本变量作为参考值的示例：

在这种形式中，TARGET_ALTITUDE的值应以米为单位。  
next_phase PHASE2 when altitude $>$ /variable TARGET_ALTITUDE  
#在这种形式中，TARGET_ALTITUDE的值应以千米（km）为单位。  
next_phase PHASE2 when altitude $>$ variable TARGET_ALTITUDE km

脚本变量 TARGET_ALTITUDE 应在 script_variables 块中定义，并在此处理器公开的脚本块之一中分配值。

脚本接口

WSF_GUIDANCE_COMPUTER 利用通用脚本接口和 WSF_SCRIPT_PROCESSOR 的功能，并支持 WsfGuidanceComputer 中定义的附加脚本方法。

# 3.3.29.1.导航程序类型 Guidance Program Types

以下部分定义了可以由 WSF_GUIDANCE_COMPUTER 引用的预定义导航程序类型。导航程序通过命令 program 和 use_program 定义和使用。

# 3.3.29.1.1. 无操作 NULL_PROGRAM

NULL_PROGRAM 是一个不执行任何操作的程序。它通常用作在某个阶段不需要导航时的占位符。

示例：

phase LIFTOFF program NULLPROGRAM endprogram next_phase PITCH_OVER when speed $>100~\mathrm{m / s}$ end_phase

# 3.3.29.1.2. 高度程序 ALTITUDE_PROGRAM

ALTITUDE_PROGRAM 用于指挥飞行器爬升或下降到指定高度并保持该高度。这与使用传统导航的 commanded_altitude 提供相同的功能。

最 大 爬 升 和 下 降 速 率 分 别 由 阶 段 命 令 maximum_ascent_rate 和maximum_descent_rate 定义。

altitude <length-value> [ msl | agl ]

指定一个命令的高度。通常用于爬升或下降到巡航高度并保持该高度。高度参考标签（‘msl’，或‘海平面以上’；‘agl’，或‘地面以上’）可以省略，在这种情况下，假定为‘msl’。

指定‘agl’作为高度参考是实现地形跟随的一种粗略机制。当指定‘agl’时，移动器将强制执行一个额外的约束，即它始终保持在地面以上。然而，不会进行前瞻性检查（它只检查平台正下方的地形高度），因此如果地形迅速上升，飞行器可能会做出非常突然的变化。

默认值：当前阶段命令 commanded_altitude 的值。

注意：如果需要通过脚本设置或修改值，则不得使用此命令。

示例

# 在程序定义中指定所需的高度。

# 这可能更清晰，但它阻止使用脚本命令来改变高度。

```txt
phase CRUISE program INTERCEPT_PROGRAM endprogram program ALTITUDE PROGRAM altitude 10000 m endProgram   
end_phase 
```

# 这与上面相同，但所需的高度是作为阶段命令而不是程序命令指定的。

# 这种形式允许通过脚本命令改变高度。

```txt
phase CRUISE  
commanded_altitude 10000 m # ALTITUDE PROGRAM 的高度  
program INTERCEPTPROGRAM endProgram  
program ALTITUDE PROGRAM endProgram  
end_phase
```

# 3.3.29.1.3. 方向程序 ATTITUDE_PROGRAM

ATTITUDE_PROGRAM 用于将飞行器定向到某个期望的方向。它计算达到指定命令所需的命令角速度。

该程序还可以用于命令连续旋转，例如某些空间物体为了平衡太阳的加热而持续旋转。这是通过指定一个没有对应目标角度的速率来实现的。

程序将在所有命令角度都达到且未指定裸速率命令时发出完成信号。

注意：这不会影响性能，也不需要施加任何加速度。请参阅 WSF_GUIDED_MOVER 中的概述。

# 角度命令

yaw <angle-value>   
pitch <angle-value>   
roll <angle-value>

指定相对于风坐标系（与速度矢量对齐，无迎角或滚转）的目标方向角。相应的速率命令指定达到目标角度所需的角速度。

默认值：未指定

注意：目标角度是相对于未旋转的风坐标系，而不是当前方向！‘yaw’ 和 ‘yaw_fixed’ 不能同时指定，‘pitch’ 和 ‘pitch_fixed’ 也不能同时指定。如果同时指定，则使用最后一个指定的。

yaw_fixed <angle-value>   
pitch_fixed <angle-value>

指定相对于东北向下坐标系的目标方向角。相应的速率命令指定达到目标角度所需的角速度。

默认值：未指定

注意：‘yaw’ 和 ‘yaw_fixed’ 不能同时指定，‘pitch’ 和 ‘pitch_fixed’ 也不能同时指定。如果同时指定，则使用最后一个指定的。

# 角速度命令

yaw_rate <angle-rate-value>   
pitch_rate <angle-rate-value>   
roll_rate <angle-rate-value>

这些命令根据上下文有两种用途：

如果与相应的目标角度一起指定，则指定用于达到目标角度的速率。

如果没有相应的目标角度，则命令速率将简单地设置为该值（实现连续旋转）。

默认值：10 度/秒

# 重置命令

reset

这与将偏航、俯仰和滚转设置为零相同。速率命令可用于指定角度重置的速率。

# 示例

```txt
phase ROLL_RIGHT program ATTITUDE PROGRAM roll 50 deg roll_rate 5 deg/sec endProgram next_phase ROLL_LEFT when ATTITUDE PROGRAM complete end_phase   
phase ROLL_LEFT program ATTITUDE PROGRAM 
```

```txt
roll-50 deg roll_rate 5 deg/sec endProgram next_phase ROLL_RESET when ATTITUDE PROGRAM complete end_phase   
phase ROLL_RIGHT program ATTITUDE PROGRAM reset roll_rate 10 deg/sec endprogram next_phase COAST when ATTITUDE PROGRAM complete end_phase   
phase COAST ...   
end_phase 
```

# 3.3.29.1.4. 飞行路径角程序 FLIGHT_PATH_ANGLE_PROGRAM

FLIGHT_PATH_ANGLE_PROGRAM 通常用于轨道发射载具，以将飞行器调整到其上升轨迹。这一程序非常敏感，其终止条件决定了通常随后的动力弹道轨迹的初始条件。这里的微小变化可能会对轨道高度甚至轨道能力产生重大影响。

使用建议

早期调用：该程序应尽早在起飞后调用。在起飞阶段的 next_phase 命令中应指定一个足够的垂直速度测试，以便进行机动。如果速度过低，飞行器可能会坠毁或轨道高度过低；如果速度过高，燃料可能会在达到轨道速度之前在高空耗尽。合理的速度值是 $5 0 ~ \mathsf { m } / s$ ，但可以低至 $4 0 ~ \mathsf { m } / \mathsf { s }$ 。某些飞行器可能需要更高的值，但很少超过 $1 0 0 ~ \mathrm { m } / s$ 。

调优工具：大多数演示中的发射载具包括一个名为 tune.txt 的输入文件，帮助确定该程序中应使用的“最佳”俯仰速率，以及起飞阶段的垂直速度测试。

参数说明

flight_path_angle <angle-value>

指定俯仰完成时的目标飞行路径角，范围为 (0,90)。如果未指定，则使用以下第一个返回值：

当前阶段的 commanded_flight_path_angle 的值。

发射计算机的命令飞行路径角的值。

默认值：未指定。

pitch_rate <angle-rate-value>

指定俯仰机动进行的速率。实际俯仰速率将根据下面的 time_constant 逐步实现。

默认值：0.15 度/秒

time_constant <time-value>

指定用于逐步实现指定俯仰速率的指数时间常数。程序启动后约 4 个时间常数，俯仰速率将达到其全部值。

默认值：1 秒

phase LIFT_OFF program NULL PROGRAM end program next_phase when speed $>50~\mathrm{m / s}$ end_phase   
phase PITCH_OVER program FLIGHT_PATH_ANGLE PROGRAM flight_path_angle 86 deg pitch_rate 0.15 deg/sec end(program next_phase ASCENT when program FLIGHT_PATH_ANGLE PROGRAM complete   
end_phase   
phase ASCENT   
...   
end_phase

这个程序对于轨道发射载具的成功至关重要，确保在适当的条件下实现所需的上升轨迹。

# 3.3.29.1.5. 传统飞行路径角程序 LEGACY_FLIGHT_PATH_ANGLE_PROGRAM

LEGACY_FLIGHT_PATH_ANGLE_PROGRAM 实现了传统导航模型中的飞行路径角导航。

flight_path_angle <angle-value>

指定所需的飞行路径角，范围为 (-90,90)。

默认值：当前阶段命令 commanded_flight_path_angle 的值。

注意：如果需要通过脚本设置或修改值，或值来自发射计算机，则不得使用此命令。

# 3.3.29.1.6. 垂直加速度程序 GRAVITY_BIAS_PROGRAM

GRAVITY_BIAS_PROGRAM 修改（例如：增加）命令加速度的垂直分量。它通常用于防止由于重力的向下拉力导致的轨迹下沉。

示例

```txt
phase INTERCEPT program INTERCEPTprograms proportionaljahication_gain 5 endprogram program GRAVITY_BIAS_PROGRAM endprogram   
end_phase 
```

# 3.3.29.1.7. 垂直加速度清零程序 GRAVITY_TURN_PROGRAM

GRAVITY_TURN_PROGRAM 将命令的垂直加速度设置为零。任何由前一个程序（例如INTERCEPT_PROGRAM）设置的命令水平加速度将保持不变。

# 3.3.29.1.8. 拦截程序 INTERCEPT_PROGRAM

INTERCEPT_PROGRAM 提供使用比例和速度追踪导航的目标拦截指导。它使用与传统拦截导航相同的算法。

注意：通常在使用此程序后应跟随 GRAVITY_BIAS_PROGRAM、ALTITUDE_PROGRAM 或LEGACY_FLIGHT_PATH_ANGLE_PROGRAM 以实现所需的结果。

proportional_navigation_gain <real-value>

指定比例导航的增益。值为零表示不执行比例导航。

默认值：当前阶段命令 proportional_navigation_gain 的值（标称为 3.0）。

注意：如果需要通过脚本设置或修改值，则不得使用此命令。

proportional_navigation_limit_angle <angle-value>

指定目标相对于武器的 3D 目标角度，在该角度下导航方法将在比例和速度追踪之间切换。如果目标角度小于或等于此值，则使用比例导航，否则使用速度追踪。

默认值：当前阶段命令 proportional_navigation_limit_angle 的值（标称为 30 度）。

注意：如果需要通过脚本设置或修改值，则不得使用此命令。

proportional_navigation_method [ pure | augmented ]

指定是否由于当前目标加速度而命令额外加速度。

□ pure 表示忽略目标加速度。

▫ augmented 表示应考虑目标加速度。

默认值：当前阶段命令 proportional_navigation_method 的值（标称为 ‘pure’）。

注意：如果需要通过脚本设置或修改值，则不得使用此命令。

velocity_pursuit_gain <real-value>

指定速度追踪导航的增益。值为零表示不执行速度追踪导航。

默认值：当前阶段命令 velocity_pursuit_gain 的值（标称为 10.0）。

注意：如果需要通过脚本设置或修改值，则不得使用此命令。

示例

```txt
phase INTERCEPT program INTERCEPTprograms proportionaljahication_gain 5 endprogram program GRAVITY_BIAS_PROGRAM endprogram   
end_phase 
```

# 3.3.29.1.9. 轨道进入程序 ORBIT_INSERTION_PROGRAM

ORBIT_INSERTION_PROGRAM 用于引导轨道发射载具进入圆形轨道。当飞行器接近远地点（飞行路径角小于 fine_adjustment_threshold 定义的值）时，它将管理高度以便平台能够实现轨道。这意味着：

如果当前速度小于在当前高度维持轨道所需的速度，程序将尝试保持当前高度，以便平台可以继续加速到所需速度。

如果当前速度超过在当前高度维持轨道所需的速度，程序将尝试增加高度，直到速度达到轨道所需的水平。

当程序检测到速度和高度满足轨道条件时，它将宣布进入轨道并命令发动机停止。用户应在使用此程序的阶段中包含一个 next_phase 语句，并测试程序的完成情况。

# 参数说明

ascent_g_bias <real-value>

上 升 期 间 应 用 的 重 力 偏 置 因 子 。 上 升 定 义 为 飞 行 路 径 角 大 于coarse_adjustment_threshold（默认值为 0.5 度）时。

默认值：0

maximum_lateral_acceleration <acceleration-value>

在轨道插入期间用于调整轨迹的最大横向加速度。这不包括重力施加的任何加速度。

默认值： $_ { 0 . 1 \ \mathsf { g } }$

minimum_insertion_altitude <length-value>

当高度低于此值时，程序将不尝试轨道插入。

默认值： $1 0 0 ~ { \mathsf { k m } }$ （因为在此高度以下维持轨道是不可能的，因大气阻力）

coarse_adjustment_threshold <angle-value>

定义平台不再被视为上升的飞行路径角。当飞行路径角小于此值但大于fine_adjustment_threshold 时，所有重力偏置将被禁用。这允许上升平台自然趋向于零飞行路径角。

默认值：0.5 度

fine_adjustment_threshold <angle-value>

定义“精细调整”发生的飞行路径角。当飞行路径角的绝对值小于此值时，程序将积极管理高度以实现轨道。这可能意味着保持高度以允许速度达到维持轨道所需的水平，或者如果速度已经过大，则让高度增加。

默认值：0.05 度

show_orbit <boolean-value>

当轨道条件满足时，写入关于轨道条件的诊断信息。

默认值：false

on_injection { eject_stage | continue }

当程序宣布轨道条件满足时采取的附加操作。

□ eject_stage：导致当前阶段被弹出。

□ continue：仅标记程序完成。

默认值：eject_stage

注意：这通常不使用，可能在未来版本中被移除。

示例

```txt
phase ORBIT InsertION program ORBIT INSERTION PROGRAM # ... using default arguments... 
```

3.3.30. 六自由度制导处理器 WSF_P6DOF_GUIDANCE_COMPUTER  
```txt
endProgram next_phase IN_ORBIT when ORBIT_insertIONPROGRAM complete end_phase   
phase IN_ORBIT   
end_phase 
```

```txt
processor <name> WSF_P6DOF_GUIDANCE_COMPUTER   
... WSF GUIDANCE COMPUTER Commands ...   
# Global Commands   
show_status   
show Commands   
showvaluations   
guide_to_truth ...   
phase <phase-name-1>   
# General Subcommands   
guidance_delay ...   
on_entry ... end_on_entry   
on_exit ... end_on_exit   
on_update ... end_on_update   
maximum commanded_g ...   
# Proportional Navigation Subcommands   
proportionaljahication_gain ...   
proportionaljahication_limit_angle ...   
proportional_haigation_method ...   
# Velocity Pursuit Subcommands   
velocity_pursuit_gain ...   
# Trajectory Shaping Subcommands   
g.bias ...   
lateral_g.bias ...   
commanded_azimuth_offset ... 
```

```tcl
#AimpointSelectionSubcommands   
guidance_target...|guide_to_truth   
aimpoint_altitude_offset...   
aimpoint_azimuth_offset...   
aimpoint_range_offset...   
aimpoint_evaluation_interval...   
#Phase Changing Subcommands   
next_phase...   
end_phase   
phase<phase-name-n>   
end_phase   
#Script Interface   
script_variables...endcript_variables   
script...end Script   
on_initiage...end_on_initiage   
on_initiage2...end_on_initiage2   
on_update...end_on_update   
...Other Script Commands...   
end Processor 
```

# WSF_P6DOF_GUIDANCE_COMPUTER 概述

WSF_P6DOF_GUIDANCE_COMPUTER 是一种处理器，通常安装在武器上，为使用WSF_P6DOF_MOVER 的武器提供引导。它通过 CurrentTargetTrack 提供的轨迹来表示要追踪的目标。移动器调用此处理器以请求引导更新，处理器计算所需的引导并将命令反馈给移动器。

# 全局命令

show_status

指定在阶段或阶段转换发生时将信息写入标准输出。

show_commands

指定从脚本命令的调用应写入标准输出。

show_evaluations

指定阶段变化规则评估应写入标准输出。

guide_to_truth <boolean-value>

指定引导目标应为当前目标轨迹中指定的位置（false），还是应为当前目标轨迹中指定的平台的真实位置（true）。

此命令既存在于全局命令中，也存在于“阶段”块中。此形式指定如果在阶段块中未指定命令，则为阶段的默认值。

默认值：false

# 阶段定义

phase <phase-name> phase-commands end_phase

“阶段”块用于定义飞行各个阶段的引导以及阶段之间转换的规则。

阶段块的格式为：

```txt
phase <phase-name>
    ... phase commands ...
end_phase 
```

应为每个所需的独特阶段定义“阶段”块。第一个“阶段”块定义了武器发射时要使用的阶段。

edit phase <phase-name> phase-commands end_phase

通常用于通过从另一种引导计算机类型派生来创建新的引导计算机类型。

示例：

```txt
processor DEMO GUIDANCE WSF_P6DOF GUIDANCE COMPUTER  
guide_to_truth true  
phase TERMINAL  
...  
end_phase  
end Processor  
processor DEMO GUIDANCE_MOD DEMO GUIDANCE  
edit phase TERMINAL  
guide_to_truth false #覆盖基类值  
end_phase  
end处理器 
```

通过这些配置，您可以为使用 WSF_P6DOF_MOVER 的武器定义复杂的引导逻辑，适应不同的飞行阶段和目标追踪需求。

阶段命令包含如下：

# 一般子命令

guidance_delay <time-value>

指定从阶段开始到开始计算引导命令的经过时间。这在起飞和其他不希望追踪目标的阶段中很有用。

默认值：0 秒

脚本命令：WsfP6DOF_GuidanceComputer.SetGuidanceDelay

on_entry … end_on_entry

定义进入阶段时执行的脚本。

on_exit … end_on_exit

定义退出阶段时执行的脚本。

on_update … end_on_update

定义在每次阶段更新时执行的脚本。通常用于在阶段期间需要变化引导命令的情况，或需要评估无法通过 next_phase 命令完成的阶段变化条件。

注意：不要随意使用此命令，因为它在移动器的每个积分时间步长都会执行。尽量保持脚本简单。

maximum_commanded_g <acceleration-value>

指定可以命令的最大加速度的幅度。

默认值：25.0 g

脚本命令：WsfP6DOF_GuidanceComputer.SetMaximumCommandedGees

# 比例导航子命令

proportional_navigation_gain <real-value>

指定比例导航的增益。值为零表示不执行比例导航。

默认值：3.0

脚本命令：WsfP6DOF_GuidanceComputer.SetProportionalNavigationGain

proportional_navigation_limit_angle <angle-value>

指定目标相对于武器的 3D 视角角度，在此角度下导航方法将在比例导航和速度追踪之间切换。

默认值：30.0 度

脚本命令：WsfP6DOF_GuidanceComputer.SetProportionalNavigationLimitAngle

proportional_navigation_method [ pure | augmented ]

指定是否应因当前目标加速度而命令额外加速度。

默认值：pure

脚本命令：WsfP6DOF_GuidanceComputer.SetProportionalNavigationMethod

# 速度追踪子命令

velocity_pursuit_gain <real-value>

指定速度追踪导航的增益。值为零表示不执行速度追踪导航。

默认值：10.0

脚本命令：WsfP6DOF_GuidanceComputer.SetVelocityPursuitGain

# 轨迹塑形子命令

g_bias <real-value>

指定用于克服重力的偏置因子。通常在中途使用以防止轨迹下垂。

默认值：1.0

脚本命令：WsfP6DOF_GuidanceComputer.SetGeeBias

lateral_g_bias <real-value>

指定用于在特定方向上倾斜轨迹水平分量的偏置因子。

默认值：0.0

脚本命令：WsfP6DOF_GuidanceComputer.SetLateralGeeBias

commanded_azimuth_offset <angle-value>

指定应保持的目标方位角。定义为武器速度矢量与从武器到目标的视线矢量之间的局部水平面角度。

脚本命令：WsfP6DOF_GuidanceComputer.SetCommandedAzimuthOffset

目标点选择子命令

guidance_target [ predicted_intercept | perception | truth ]

指定引导目标的计算基础：

□ predicted_intercept：基于发射计算机提供的预测拦截位置进行引导计算，不考虑目标的实际位置。通常用于初始阶段，当基于当前条件的拦截点预测不可靠时。  
▫ perception：基于当前目标轨迹提供的目标感知进行引导计算。由于轨迹可能存在传感器误差，武器可能被引导到目标实际位置以外的地方。（等同于 guide_to_truthfalse）  
□ truth：基于目标的实际位置进行引导计算。（等同于 guide_to_truth true）  
□ default：使用全局 guide_to_truth 命令的值。

默认值：default

脚本命令：WsfP6DOF_GuidanceComputer.SetGuidanceTarget

aimpoint_altitude_offset <length-value>

修改目标点以位于感知目标位置的上方或下方。通常用于制造空中爆炸。

默认值：0 米（无高度偏移）

脚本命令：WsfP6DOF_GuidanceComputer.SetAimpointAltitudeOffset

aimpoint_azimuth_offset <angle-value> [ left | right | either ]   
aimpoint_range_offset <length-value>

提供一种方法来生成相对于感知目标位置的横向偏移目标点。通常用于满足某些战术要求。

□ aimpoint_azimuth_offset 是当地水平面中武器速度矢量与从武器到目标的视线矢量之间的相对方位角。  
aimpoint_range_offset 是到目标的地面距离。  
□ left,right,either 修饰符指示目标相对于武器的位置。either 将偏移放置在最小化武器航向变化的位置。

脚 本 命 令 ： WsfP6DOF_GuidanceComputer.SetAimpointAzimuthOffset 和WsfP6DOF_GuidanceComputer.SetAimpointRangeOffset

aimpoint_evaluation_interval <time-value>

控制使用 aimpoint_azimuth_offset 和 aimpoint_range_offset 时重新计算目标点的频率。这是一个相当耗时的操作，不需要在每次调用引导计算机时执行。

默认值：5 秒

脚本命令：WsfP6DOF_GuidanceComputer.SetAimpointEvaluationInterval

使用示例

```txt
phase PHASE_X ... aimpont_altitude_offset 10000 m 
aimpoint_azimuth_offset 45 deg either  
aimpoint_range_offset 10 nm  
next_phase PHASE_Y when target_azimuth > 45 deg  
end_phase 
```

在此示例中，目标点将被创建，使得当武器到达该点时，目标将位于相对方位角 45 度、距离 10 海里处，且武器将位于目标上方 10000 米的高度。next_phase 命令中的target_azimuth 比较值应与 aimpoint_azimuth_offset 的值相同。