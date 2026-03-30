<table><tr><td></td><td></td><td rowspan="4">esm_rwr</td><td>definitions.</td></tr><tr><td></td><td></td><td>Electronic Support Measures &amp; Radar Warning Receiver sensor definitions.</td></tr><tr><td></td><td></td><td>Radar sensor definitions</td></tr><tr><td></td><td></td><td>Other sensor types</td></tr><tr><td></td><td>signatures</td><td></td><td></td></tr><tr><td></td><td>weapons</td><td></td><td></td></tr><tr><td></td><td></td><td>aam</td><td>Air-to-Air Missiles Definitions.</td></tr><tr><td></td><td></td><td>agm</td><td>Air-to-Ground Missiles Definitions.</td></tr><tr><td></td><td></td><td>jaam</td><td>Joint Air-to-Air Missiles Definitions.</td></tr><tr><td></td><td></td><td>jammer</td><td>Examples of intentional emission of radio frequency signals:</td></tr><tr><td></td><td></td><td>other</td><td>e.g., Theater Ballistic Missile.</td></tr><tr><td></td><td></td><td>sam</td><td>Surface-to-Air Missile Definitions</td></tr><tr><td></td><td></td><td>sims</td><td>Standard Interface for Missile Simulation.</td></tr></table>

# 5.6.8. 提高构建模拟运行速度的方法 Making Constructive Sims Run Faster

以下项目通常可以调整而不会对模拟产生不利影响。然而，请记住您正在调整的内容以及它对单个平台的影响。严重调整帧率可能会影响模拟。调整事件或重放输出不会影响模拟结果。

# 调整建议

movers 的 update_interval

将 movers 的 update_interval 设置为小于 5 到 10 秒通常会导致运行时问题。然而，如果作为武器使用，制导的 movers 绝对需要较低的更新间隔。

脚本中的 update_interval

▪ 在平台上每秒调用一次脚本是昂贵的。考虑将其延长到 10 秒或更长时间。

传感器中的 frame_time

将 frame_time 设置为低于 1 秒会占用大量资源。此外，考虑形成轨迹所需的时间。例如：如果传感器在正面传感器检测发生后通常需要 10 秒来形成轨迹，则将frame_time 设置为 3.3 秒以实现 3 次命中中的 5 次 hits_to_establish_track。

dis_interface

可以更改以下输入以显著减少重放文件的大小（使其更小，从而减少运行时间）：

suppress_comm_data- 您是否真的需要在可视化工具中查看蓝色通信线？  
heartbeat_timer - 将其设置为 100（默认值为 5）。  
entity_position_threshold - 将其设置为 10 米（默认值为 1）。  
entity_orientation_threshold - 将其设置为 10 度（默认值为 3）。

请记住，设置这些值不会影响模拟。

event_output

您是否真的需要记录传感器的每次检测尝试？  
您是否真的需要记录每次轨迹更新？  
选择的任何事件都需要 I/O，这很昂贵。再次强调，选择要保留的事件项不会影响模拟。

csv_event_output

您是否真的需要记录传感器的每次检测尝试？  
您是否真的需要记录每次轨迹更新？  
选择的任何事件都需要 I/O，这很昂贵。再次强调，选择要保留的事件项不会影响模拟。

observer

如果用于写入输出或日志文件，可能会很昂贵。请小心使用，因为这些可能也用于模拟运行时。

write_ln 或 debug 语句

注释掉每个 writeln 并关闭调试语句。写入屏幕需要 I/O。

替换通信中的默认网状网络

通信中的默认网络类型是网状网络，当网络中有很多成员时，扩展性很差： $[ ( \mathsf { n } ^ { \ast } \left( \mathsf { n } - 1 \right) )$ /2] 条边，其中 n 是网络中的通信数量。如果需要更大的网络，请尝试切换到更具扩展性的网络类型（例如星型），或者完全通过使用通用网络类型来定义网络，以避免使用网状网络的过度性能损失。

# 5.6.9. 构建型转实时运行 Constructive to Virtual

要将构建型 WSF 模拟转换为实时（虚拟）运行，需要在 WSF 输入文件中进行以下更改：

# 步骤

1. 添加命令 “realtime”

使用 realtime 命令使模拟以墙钟速度运行。

2. 配置 dis_interface 块以设置 TCP/IP 参数

使用 dis_interface... end_dis_interface 块设置在 DIS 上运行 WSF 所需的参数。以下是一个多播接口的示例：

dis_interface

exercise

```txt
site 25  
application 44  
multicast 224.2.25.55 192.168.10.32 # 多播地址 / 我的 PC 上使用的以太网设备  
#broadcast 192.168.10.255 # 广播示例  
port 3225  
end_dis_INTERFACE
```

# 3. 配置 dis_interface 块以设置 sides

将 force side 映射到场景文件中使用的 side 子命令。例如：

```txt
dis_INTERFACE
#force <side> <dis-force-id>
force blue 1 #如果未指定 side，则为默认值
force red 2 #如果未指定 side，则为默认值
force green 3 #如果未指定 side，则为默认值
## 或 ###
force united_states 1
force canada 2
end_dis/interface
```

# 4. 在 dis_interface 块中将 platform_types 映射到 DIS 枚举

如果 platform_type 未映射，将发送 00:00:00:00:00:00:00 的实体类型枚举。例如：

```txt
dis_INTERFACE #entity_type <platform_type><dis-entity-type> #munition_type <platform_type><dis-entity-type>#与entity_type相同 entity_type F-15E 1:2:225:1:5:5:0 entity_type F-18E 1:2:225:1:9:10:0 end_dis-interface 
```

# 5. 在 dis_interface 块中手动或自动映射 entity_id

自动示例：

```txt
dis_INTERFACE  
start_entity 10#dis实体id从10开始{25:44:10及以上用于  
site:application:entity_id}  
end_dis-interface 
```

手动示例：

```txt
dis_INTERFACE #entity_id <platform_name> <entity-number> entity_id hornet-1 101#示例：生成{25:44:101}的dis实体id entity_id raptor-1 102 entity_id tank-1 103 end_dis-interface 
```

# 6. 仅在需要映射 dis 发射 PDU 时执行此步骤

在大多数情况下，只需映射 emitter_type。

```txt
dis/interface #emitter_type <sensor/jammer-type><dis-emitter-name-enum> #emitter_function <sensor/jammer-type><dis-emitter-function-enum> #beam_type <sensor/jammer-type> <sensor/jammer-mode-name> <sensor/jammer-beam-number><dis-beam-parameter-index-value> #beam_function <sensor/jammer-type> <sensor/jammer-mode-name> <sensor/jammer-beam-number><dis-beam-function-enum-value> emitter_type EW_RADAR_TYPE 11 emitter_type TTR_RADAR_TYPE 12 emitter_type ACQ_RADAR_TYPE 13 emitter_function EW_RADAR_TYPE 2 #将EW_RADAR发射器功能的功能设置为"2"(请参阅dis规范以获取正确值) beam_type EW_RADAR_TYPE \*11 #将所有未定义模式和未定义波束编号的波束参数索引默认为11。 beam_type EW_RADAR_TYPE \*212 #将所有未定义模式名称的波束参数索引设置为12，除了当波束编号为2时。 beam_type EW_RADAR_TYPE \*313 #将所有未定义模式名称的波束参数索引设置为13，除了当波束编号为3时。 beam_function EW_RADAR_TYPE \*222 #将波束编号2的波束枚举功能设置为22（请参阅dis规范以获取值） beam_type TTR_RADAR_TYPE TRACK\*30002 #在TRACK模式下将波束参数索引设置为30002，适用于所有波束编号 beam_function TTR_RADAR_TYPE TRACK\*7 #如果在TRACK模式下，将功能设置为7，适用于所有波束。（请参阅dis规范以获 取值） end_dis_interface
```

# 7. 确保通信设备使用静态地址

在构建型模拟中，通信设备通常使用动态地址（即未明确为通信设备提供地址）。如果其他模拟使用的网络也被本地通信设备使用（包括在默认网络情况下省略任何输入，或通过使用 local:master 或 local:slave 等共享公共网络），则必须为这些通信设备分配静态地址，以确保在所有模拟中正确且一致地应用通信地址。

构建型用例中的通信定义示例（在必要更改之前）

案例 1- 字符串网络名称使用：

```txt
commdatalinkWSFCOMM_TRANSEIVER network_nameblue_net   
end_comm   
commdatalink_2WSFCOMM_TRANSEIVER network_name blue_net   
end_comm 
```

案例 2- 命令链使用：

```txt
comm blue_comm WSFCOMM_TRANSEIVER network_name <local:master> end_comm 
```

案例 3- 默认网络使用：

```txt
comm generic_comm WSFCOMM_TRANSEIVER #uses the 'default' network end_comm 
```

案例 4- 网络地址使用：

```txt
comm red_comm WSFCOMM_TRANSEIVER network_address 192.168.1.1/24  
end_comm 
```

必要转换示例（假设外部定义的通信使用相同网络）

案例 1- 字符串网络名称使用：

```txt
commdatalinkWSFCOMM_TRANSEIVER address192.168.1.1/24   
end_comm   
commdatalink_2WSF COMM TRANSEIVER address192.168.1.2/24   
end_comm 
```

案例 2- 命令链使用：

```txt
network master:<commander-platform-name> WSFCOMM_NETWORK_MESH  
network_address 192.168.1.0/24  
end_network  
comm blue_comm WSFCOMM_TRANSEIVER 
```

```txt
address 192.168.1.123/24  
end_comm 
```

案例 3 - 默认网络使用（注意默认网络始终为 0.1.0.0/16）：

```txt
comm generic_comm WSFCOMM_TRANSEIVER address 0.1.22.127/16   
end_comm 
```

案例 4- 网络地址使用：

```txt
comm red_comm WSFCOMM_TRANSEIVER address 192.168.1.1/24  
end_comm 
```

通过为通信设备分配静态地址，可以确保在所有模拟中通信地址的正确性和一致性。这对于使用共享网络的多个模拟尤其重要。有关更多详细信息，请参阅通信入门指南。

# DIS 特定问题和解答

如何保持在 DIS 规范内？

要确保符合 DIS 规范，可以在 dis_interface 块中添加以下子命令：

```txt
dis_INTERFACE maximum_beam_entries 10 #限制波束数量 maximum_track_jam_entries 10 #限制跟踪/干扰条目数量以符合DIS规范 suppress_non_STANDARD_data true end_dis-interface
```

如何轻松查看映射内容？

在 dis_interface 块中添加 log_created_entities。在运行时，平台类型和 DIS 枚举的列表将显示在控制台窗口中。

```txt
dis_INTERFACE log_createdentities end_dis-interface 
```

如何使某个平台在接收到外部武器时成为优先目标？

使用 target_priority 命令可以在接收到 DIS 引爆 PDU 时为优先目标增加偏向。以下是将所有 SAM_FC_RADAR 平台设为最高优先级目标的示例：

```txt
dis_INTERFACE  
targetpriority SAM_FC_RADAR 1000 # 这使得 SAM_FC_RADAR 类型具有很大的被击中偏向。  
end_dis/interface
```

如何使平台不向其他模拟发送任何 DIS 信息？

使用 private 命令：

```txt
dis_INTERFACE
#private [name <name> | type <type> | all ]
private type SITE_COMMANDER
private name target-52
end_dis-interface 
```

WSF 是否可以忽略正在运行的应用程序？

是的，使用子命令 filter_out_by_site_and_app：

```txt
dis_INTERFACE  
filter_out_by_site_and_app  
ignore_site 25  
ignore.application 55  
end_filter_out_by_site_and_app  
end_dis_INTERFACE 
```

模拟在输入运行 WSF 的命令后没有启动，怎么办？

这意味着没有其他模拟发送“start” PDU。要在没有“start” PDU 的情况下启动 WSF：

```txt
dis-interface  
autostart # 如果有人发送 start PDU，请注释掉此行。  
end_dis-interface
```

我不断收到未知平台警告。这是怎么回事？

WSF 接收到的每个外部平台都必须定义一个 platform_type 和一个 DIS 枚举值。当WSF 通过 DIS 接收到一个平台时，它会自动在内部创建（实例化）该平台并对其进行操作。通过 DIS 接收到的未知（未映射）平台将在内部创建，但将为其定义默认值（例如，极端特征值）。首先，创建一个 platform_type 并为其分配一个特征。其次，添加 entity_type 和枚举映射，就像它是一个内部实体一样。

如果 WSF 接收到一个具有 00:00:00:00:00:00:00 或任何其他未映射枚举的实体，可以将其映射到特定内容吗？

可以，使用子命令 unknown_platform_type：

```txt
dis_INTERFACE unknownplatform_type <platform_type> end_dis-interface 
```

我在 dis_interface 块中更改了设置，但 WSF 模拟没有变化！出了什么问题？

很可能在您编辑的 dis_interface 块之后读取了另一个 dis_interface 块。请记住，最后读取的命令将覆盖您的设置。要查看哪些文件已被读取（以及它们的读取顺序），请查看日志文件（通常位于名为“output”的子目录下）。

如何轻松添加上述实时命令？

在此示例中，构建型运行模拟的命令是“run mysim.txt”。首先，创建一个 realtime.txt 文件（文件名可以自行选择）。realtime.txt 文件的示例内容：

```txt
realtime 
```

```txt
dis_INTERFACE  
exercise 1  
site 25  
application 44  
multicast 224.2.25.55 192.168.10.32  
port 3225  
suppress_comm_data  
maximum_track_jam_entries 10  
autostart  
force united_states 1  
force canada 2  
log_created Entities  
end_dis-interface  
include dis_map.txt # 此文件将包含所有 DIS 枚举映射... 
```

现在，输入命令“run mysim.txt realtime.txt”，构建型 WSF 模拟将实时运行。

# 5.6.10. WSF 参考手册 WSF Reference Guide

核心应用

Core Applications: 核心应用

Post Processing & Report Generation: 后处理与报告生成

post_processor: 后处理器

传感器覆盖与天线增益图创建

Sensor Coverage & Antenna Gain Plot Creation: 传感器覆盖与天线增益图创建

sensor_plot: 传感器图

武器交战分析支持

Weapon Engagement Analysis Support: 武器交战分析支持

engage: 交战

武器模型开发支持

Weapon Model Development Support: 武器模型开发支持

weapon_tools: 武器工具

任务分析/基线仿真应用

Mission Analysis / Baseline Simulation Application: 任务分析/基线仿真应用

mission: 任务

# 仿真运行时

Simulation Runtime: 仿真运行时

Simulation Control Commands: 仿真控制命令  
File Commands: 文件命令  
Monte Carlo Commands: 蒙特卡罗命令

▫ clock_rate: 指定仿真时间与实际时间的比率  
□ conditional_section: 有条件地包含或排除输入

□ end_time: 指定仿真运行的结束时间  
□ generate_random_seeds: 生成蒙特卡罗迭代集的随机种子  
□ initial_run_number: 指定蒙特卡罗迭代集的初始运行编号  
□ final_run_number: 指定蒙特卡罗迭代集的最终运行编号  
□ frame_rate: 定义逐帧仿真的时间步长  
□ frame_time: 定义逐帧仿真的时间步长  
□ line_of_sight_manager: 视线管理器配置  
□ multi_threading or multi_thread: 定义是否启用多线程   
□ non-realtime: 指示仿真以非实时模式运行  
□ number_of_threads: 定义线程数量  
▫ platform_availability: 定义平台在运行时存在的概率  
□ random_seed: 指定随机数生成器的种子  
□ realtime: 指示仿真以实时模式运行  
□ run_number_increment: 指定蒙特卡罗迭代集运行之间的增量  
□ simulation_name: 指定仿真在 Warlock 和 Mystic 中的标识名称  
□ start_date, start_epoch, start_time: 定义仿真的基准或参考时间

文件、输入和输出

□ WSF User Input Format: WSF 用户输入格式  
□ Argument Types: 参数类型

File and Input: 文件和输入

□ classification_levels: 定义场景中可用的分类级别及其颜色  
□ classification: 指定输入文件的分类级别、注意事项和三字代码  
□ define_path_variable: 定义可替换到文件名中的变量  
□ file_path: 指定包含文件的路径  
□ include and include_once: 将文件插入输入流   
□ log: 写入日志文件  
□ log_file: 打开日志文件  
□ reset_file_path: 移除所有‘文件路径’条目  
□ undefine_path_variable: 取消定义‘路径’变量

输出

□ console_output: 配置控制台输出内容和格式  
□ csv_event_output: 配置‘逗号分隔值（CSV）’事件输出记录器  
□ draw: 绘制路线和路线网络   
▫ draw_file: 指定 WsfDraw 的输出  
□ enumerate: 枚举（列出）对象类型到文件  
□ event_output: 配置事件输出记录器  
observer: 捕获平台间特定交互的结果  
□ event_pipe: 配置二进制 AFSIM 事件记录文件

地形和环境

▫ atmosphere: 修改仿真中的大气特性（如温度、密度）  
□ global_environment: 定义全球环境的属性  
▫ terrain: 控制地形管理接口

定义系统、子系统、模型和数据

Defining Systems (Platforms): 定义系统（平台）  
platform and platform_type: 定义平台类型和实例

▫ osm_traffic: 生成使用 Open Street Maps（OSM）转换路线的背景车辆交通  
□ road_traffic: 生成背景车辆交通  
□ sea_traffic: 生成背景船舶平台  
▫ air_traffic: 生成背景空中交通

定义子系统

Defining Subsystems (comm, sensors, processors, etc.): 定义子系统（通信、传感器、处理器等）

▫ comm: 定义通信对象类型和实例。（预定义通信类型）  
□ processor: 定义处理器类型和实例。（预定义处理器类型）  
▫ mover: 定义移动对象类型和实例。（预定义移动类型）  
□ router: 定义通信路由器类型和实例。（预定义路由器类型）  
□ sensor: 定义传感器对象类型和实例。（预定义传感器类型）  
▫ track_manager: 配置平台的主跟踪列表或备用跟踪列表的跟踪维护和融合。  
□ visual_part: 定义未与定义的子系统关联的关节部件。

定义模型和数据

□ aero: 定义通过空气移动的平台的空气动力学阻力和升力特性。  
□ antenna_pattern: 定义发射机或接收机的天线增益模式。  
□ attenuation_model: 定义或引用大气衰减模型。  
□ clutter_model: 定义或引用杂波模型。  
error_model: 定义或引用传感器误差模型。   
□ filter: 为传感器或 track_manager 定义过滤器对象。（预定义过滤器类型）  
□ group: 定义可以包含平台和/或平台部件的组。  
□ fuel: 定义燃料对象类型和实例。（预定义燃料类型）  
□ iff_mapping: 定义全球 IFF 映射。  
□ medium: 定义通信介质，由各种通信对象使用。（预定义介质类型）  
□ message_table: 定义消息表。  
□ network: 定义通信网络。（预定义网络类型）  
□ noise_cloud: 定义用于传感器和通信衰减的云层。  
□ propagation_model: 定义或引用传播模型。  
□ protocol: 定义通信协议，供通信对象后续使用。（预定义协议类型）  
□ radar_signature: 定义平台的雷达特征。  
□ route: 定义路线移动器的移动路径。  
□ route_network: 定义路线网络。  
router_protocol: 定义路由协议，供路由器对象后续使用。（预定义路由协议类型）  
□ track: 定义“预先简报”轨迹。

□ zone and zone_set: 定义区域或区域集合。

# 脚本

Scripting Language: 脚本概述、脚本命令、通用脚本接口、脚本对象类型

□ callback: 定义触发脚本的回调。  
□ execute: 在指定时间执行脚本。  
□ observer: 捕获平台间特定交互的结果。

# 接口

□ dis_interface: 分布式交互仿真（DIS）配置。  
▫ xio_interface: 控制“外部 I/O”接口。

# 多分辨率

▫ Multiresolution: 每个多分辨率模型定义一个容器，用于在平台上容纳一个或多个模型。选择使用哪个模型推迟到仿真时间，并取决于选择的保真度值。  
▫ multiresolution_comm: 通信模型的多分辨率容器。  
▫ multiresolution_fuel: 燃料模型的多分辨率容器。   
□ multiresolution_mover: 移动器的多分辨率容器。   
□ multiresolution_processor: 处理器的多分辨率容器。   
□ multiresolution_sensor: 传感器的多分辨率容器。   
□ multiresolution_acoustic_signature: 声学特征的多分辨率容器。   
□ multiresolution_infrared_signature: 红外特征的多分辨率容器。   
□ multiresolution_optical_signature: 光学特征的多分辨率容器。   
□ multiresolution_radar_signature: 雷达特征的多分辨率容器。   
□ multiresolution_multirun_table: 定义保真度值的多运行表。这些保真度值可以为场景中的任何平台/模型组合指定。多运行功能与 final_run_number 命令一起使用。

# 空间

propagator: 指定用于跟踪卫星的传播器类型（轨道确定融合；轨道确定过滤器）。

# 覆盖

Coverage Overview: AFSIM 覆盖能力概述。

□ grid: 定义可以计算覆盖的网格（预定义覆盖网格类型）。  
□ coverage: 定义覆盖计算（预定义覆盖类型）。

# SIMDIS

□ simdis_interface: 定义 SIMDIS ASI 文件输出配置。

# OMS_UCI

OMS_UCI: 开放任务系统通用指挥和控制接口，或 OMS/UCI，是一种允许平台及其组件相互通信的消息系统。

□ uci_component: 使组件能够发送 UCI 消息的基本组件。

# 注释

□ visual_elements: 定义将在视觉应用中显示的注释。

# 军事

□ acoustic_signature: 定义平台的声学特征。  
□ infrared_signature: 定义平台的红外特征。  
▫ inherent_contrast: 定义平台的固有对比度。  
□ optical_reflectivity: 定义平台的光学反射率。  
□ optical_signature: 定义平台的光学特征（投影面积）。

# 电子战

Electronic Warfare Effect Aggregation: 理解电子战在传感器和通信接收器中的聚合和使用。

▫ electronic_warfare: 定义电子战对象类型。（预定义电子战类型）  
▫ electronic_warfare_effect: 定义电子战效果对象类型。（预定义电子战效果类型）  
▫ electronic_warfare_technique: 定义电子战技术对象类型。（预定义电子战技术类型）  
□ false_target: 定义电子攻击的假目标技术。  
▫ false_target_screener: 定义接收器对假目标的响应。

# 武器

□ weapon: 定义武器对象类型和实例。（预定义武器类型）  
□ weapon_effects: 定义武器效果对象类型。（预定义武器效果类型）  
□ launch_computer: 定义武器发射计算机。（预定义发射计算机类型）  
□ wsf_weapon_server: 定义武器服务器接口。

# P6DOF

□ p6dof_object_types: P6DOF（伪 6DOF）类型定义/配置。

# 网络战

□ Cyber Overview: 网络战模型概述。  
□ cyber_attack: 定义网络战攻击类型。  
□ cyber_effect: 定义网络战效果类型。（预定义网络效果类型）  
□ cyber_protect: 定义网络战保护类型和实例。  
▫ cyber_trigger: 定义单次或重复的脚本条件检查，主要用于嵌入式攻击的脚本执行器。（预定义网络触发器类型）  
□ cyber_constraint: 定义网络攻击的资源限制概念。  
□ enable_cyber_wsfdraw: 启用网络战的 WsfDraw 输出。  
□ disable_cyber_wsfdraw: 禁用网络战的 WsfDraw 输出（默认）。

# RIPR

□ RIPR: 反应集成规划架构

# SIXDOF

six_dof_object_types: 点质量和刚体 6DOF 类型定义/配置。

# 6. 官方培训资料

AFSIM 官方提供培训资料和丰富的 demo，官方培训资料在本章中介绍。本章主要是对官方培训资料 PPT 的翻译以及对所涉及的想定的分析，以协助用户来理解和自己独立完成官方培训。

其中官方培训资料在该目录下：afsim2.9_src\training。其下分为 developer 和 user 两部分，每部分都包含了完整的 PPT和示例的代码，所以并不需要担心按着 PPT 敲不出来代码。其中 user 部分主要介绍如何使用 AFSIM 这款软件，可以理解为面向用户的。而 developer主要介绍如何使用其提供的扩展接口进行扩展的开发，可以理解为面向开发者的。

以下对其各部分做更加详细的介绍。

# 6.1. 用户培训教程 user

该部分培训资料均在 afsim2.9_src\training\user 下，其下包含了丰富的 PPT 与示例代码，拿第 1 课来说，其中 afsim2.9_src\training\user\1_AFSIM_Intro\slides 下包含了 2 个 PPT：

![](images/2d6f4617910647ec05e43893d2b5ed37d0ec0e452572c2daa6ef9273017d56c1.jpg)

而\afsim2.9_src\training\user\1_AFSIM_Intro\scenarios 下则包含了该小节对应的代码：

![](images/144e891c51f899b66d9bb0072a3dad656790dbf34391c3681545cd27bf7c6f47.jpg)

以下来介绍 2.9 版本的 user 培训资料的全部内容。

# 6.1.1. AFSIM 介绍 1_AFSIM_Intro

本节全面的介绍 AFSIM，以及做了一个输出打印的想定示例。

# 6.1.1.1. 本节想定解析

本节想定在：afsim2.9_src\training\user\1_AFSIM_Intro\scenarios

本节想定的功能较为简单，只是在输出窗口中输出了一个”HelloWorld”打印。

# 6.1.1.2. 官方 PPT 资料

# 6.1.1.2.1. 1_AFSIM 用户培训介绍 1_AFSIM_User_Training_Overview

本

文

为

afsim2.9_src\training\user\1_AFSIM_Intro\slides\1_AFSIM_User_Training_Overview.pptx 的翻译。

![](images/13232be0972605ebe4c8050b3592bc88598cf820877d895011d42186019d3227.jpg)

Integrity★Service★ Excellence

# AFSIM用户培训1-介绍

13324598743

# AFRL/RQQD美国空军研究实验室

DISTRIBUTioNC.DistributionauthorizedtoU.S.Government Agenciesand theircontractors,9-Aug-19. Otherrequestsforthisdocument shallbereferredto AFRL/RQQD.

1

![](images/17d61e09879aa354e44dd41279edfbb50072a5f8a6af18a418e460d7426720ec.jpg)

UNCLASSIFIED

目的

![](images/1022d72a6e05460a9c6c63e057f530c2ff32a8ce89cffb6b9a626c335ac8eff5.jpg)

·该课程对AFSIM进行以下介绍

－辅助人员快速的熟悉AFSIM  
－介绍AFSIM中的相关应用和程序  
－构建一个基本的想定

![](images/fcd627168664c94b5140748a964aaea1df55fee958bfb2b563cb4297b8d0faf3.jpg)

DISTRIBUTioNC.Distributionauthorizedto U.S.Government Agenciesand their contractors,9-Aug-19. Otherrequests forthisdocumentshallbereferredtoAFRL/RQQD.

# ·包括

－描述课程内容  
－介绍什么是AFSIM  
－介绍AFSIM的脚本由哪些部分组成  
－描述AFSIM有哪些基本输出

![](images/faed77c322d3d3fa3a8e570107f1bae11692b0f658bdf3461f5d2a1ee6365b7f.jpg)

DISTRIBUTioNC.Distributionauthorized to U.S.Government Agenciesand their contractors,9-Aug-19. OtherrequestsforthisdocumentshallbereferredtoAFRL/RQQD

![](images/3bdecc8b3b34bd1a1ed276129ecb575d5de1743083bdc17b9f38ce33408ddc34.jpg)

# UNCLASSIFIED

# AFSIM是什么？

![](images/ded21423a8a479508e1654e22ffb0b3888b3e1a5688887d2d4c0d6ef4996d312.jpg)

·AFSIM是如下英文的缩写"Advanced Framework forSimulation, IntegrationandModeling"翻译成中文就是“高级仿真、集成与建 模框架”

－是一个面向军事和商业领域的分析需求的通用仿真框架

·AFIM不仅仅只是一个综合防空（IADS）仿真系统  
·AFSIM面向以下应用领域进行分析：

－综合防空(IADS)  
－导弹防御任务  
-边防   
－人在环(OITL)的战争游戏  
-航空公司运营与空中交通管制  
......甚至一个银行排队模型

![](images/ece637d4601b11737b99370932281cc8a3191af7867d640fd6a56e83e917373a.jpg)

DISTRIBUTioNC.Distributionauthorizedto U.S.Government Agenciesand their contractors,9-Aug-19. Otherrequests forthisdocument shallbereferredto AFRL/RQQD.

·AFSIM聚焦于任务级/交战级仿真   
·AFSIM提供了一个灵的跨域、多精度的仿环境。  
译者注：右侧是强调AFSIM关构建、交战、任务/战斗这三个由下至上，最终组成一个战役

![](images/9fb87cd1ae04c8b7fd8b71ec835bc83f162b8d36d7059a7a1f191e466648618b.jpg)

DISTRIBUTioNC.DistributionauthorizedtoU.S.Government Agenciesand theircontractors,9-Aug-19. OtherrequestsforthisdocumentshallbereferredtoAFRL/RQQD.

5

![](images/4ba613d2195f8824f41848bda19e2d2f16082125d78812f83ea724a3072172f9.jpg)

# UNCLASSIFIED

# AFSIM主要用于

![](images/3c8043a5329a5aa221825953b39bf165a15ba5c1f763dee3a058ec77fddccd67.jpg)

·多对多的仿真任务建模环境。  
·可应用于多个领域：

-空  
-天  
－陆、海  
-水下  
-网络

![](images/f2cf5443a5946d3ef974fa8d80fffbc351980b16a5cb9652dce906e50203da68.jpg)

DISTRIBUTioNC.Distributionauthorizedto U.S.Government Agenciesand their contractors,9-Aug-19. Otherrequests forthisdocument shallbereferredto AFRL/RQQD.

# ·模型

－对系统、实体、现象或过程的物理、数学或其他逻辑表示。

# ·仿真

－一种随时间实现模型的方法。

![](images/77d80ade13b62247d325fbf4b746ae790f29f7718bd5075e67d6c30a4b82cbe2.jpg)

DISTRIBUTioNC.DistributionauthorizedtoU.S.Government Agenciesand theircontractors,9-Aug-19. Otherrequestsforthisdocument shallbereferredto AFRL/RQQD.

7

![](images/d0653cc9644b3cd7feca4baf144cdc4f2c78670c2b929439da3c2cdcd698df9f.jpg)

# UNCLASSIFIED

# AFSIM的发展过程1

![](images/5da812e1ae4867b4c3380411d8943935f2503f32d9cebdbe4071924261b3009f.jpg)

2000年-SUPPRESSOR为应用新的需求进行了大量的改进

对复杂结果的可视化  
支持虚拟实验的DIS协  
高级追踪器和自动路  
先进的雷达、红外（IR

“波音SUPPRESSOR”非常不完善，体现在以下

难以与新的SUPPRES  
难以维持其实时性  
难应对多种坐标系  
圆球和平球  
仍然不是网络中心化

![](images/9afffd3d8e0376d79d24cb83460ea1b43e5e5e98f82bfea33996301c8bc30d44.jpg)

DISTRIBUTioNC.Distributionauthorizedto U.S.Government Agenciesand their contractors,9-Aug-19. Otherrequests forthisdocument shallbereferredto AFRL/RQQD.

2005－波音公司创建了基线版本

开发了AFNES脚本语言  
需要支持IADS战术的灵活定义  
SUPPRESSOR“obruty”场景的转换

2006-聚焦传感器

根据需要将SUPPRESSOR传感器算法迁移到AFNES  
开始转换MCO-1/MCO-2SUPPRESSORTDB文件

平台、传感器、资源分配（战术和条令

开发了SUPPRESSORSDB到AFNES的转换器  
除了交战以外的传感器和跟踪的其它能力

2006到2008-海军IWARS模型转换到AFNES

2007-聚焦交战

将SIMS模型从FORTRAN转换为C   
AENES的初步发布，包含MCO-2和交战功能  
2008年-正式发布AFNES1.0，包含MCO-1和MCO-2

2008－波音幻影工厂副总裁达里尔·戴维斯指示波音研究与技术部门（BR&T）将AFNES提供给空军，以促进其作为标准工具的采用。  
2013-交付给政府，拥有完整的使用权—空军研究实验室（AFRL）将其重命名为“AFSIM”。  
2016-空军研究实验室（AFRL）全面接管了AFSIM的支持（包括C++和模型）。

DISTRIBUTioNC.Distributionauthorized to U.S.Government Agenciesand theircontractors,9-Aug-19.

Otherrequestsforthisdocument shallbereferredto AFRL/RQQD.

9

![](images/f489b78fac812c4bf47496656a1f4f08b53dfd1902f42f3ce5c73c4845e5a7c6.jpg)

# UNCLASSIFIED

# 框架定义

![](images/af3f49ea2a375d59d786a429702a5fdd3f7a5b27a49361e7a5b1883e35bbd129.jpg)

·软件框架定义：

软件框架是一个软件系统（或子系统）的可重用设计。软件框架可能包括支持程序、代码库、脚本语言或其他软件，以帮助开发并将软件项目的不同组件粘合在一起。框架的各个部分可以通过API公开。（来源：维基百科）

·AFSIM是一个用于创建模拟的C++框架

一模块化可扩展架构。  
－类似于Java/VB/C#的脚本语言用于外部定制。

·多层次的精确度。  
·高精度的基于物理的模型。  
·简单的基于几何的模型。  
·概率模型。

框架不是应用程序，而是用于创建应用程序的工具。

DISTRIBUTioNC.Distributionauthorizedto U.S.Government Agenciesand their contractors,9-Aug-19.

Otherrequestsfor thisdocument shallbereferredto AFRL/RQQD.

# AFSIM提供标准接口和通用基础设施以支持模拟开发。

![](images/8c626d59bd883fd8bb28af42f555298fb99ec287e1bb97611ea2675a1eff1010.jpg)

DISTRIBUTioNC.DistributionauthorizedtoU.S.GovernmentAgenciesand theircontractors,9-Aug-19. Otherrequestsforthisdocument shallbereferredto AFRL/RQQD.

11

![](images/71d1dde4629e7221aa613d71f48f2fbb8cde4fd2886cc7fb5d7697aba5f30b26.jpg)

# UNCLASSIFIED

# 应用程序：想定编辑工具Wizard

![](images/08db35ab891223189fdcf2608e8aa46efaae31e00eb4dab9d6fe6017110dcdee.jpg)

·Wizard是AFSIM的集成开发环 境   
·用于布置平台的想定编辑器  
·支持基于AFSIM的应用程序的场景开发和模拟执行。

![](images/2d0e0c3e3e2ba39529334becfdf02c7270fed44260b618acff653dd0cf81fff8.jpg)

![](images/409f1fe92ec7ac9173682ef32cdd9d23df3fe191d413533b7280f1a9fceaf140.jpg)

![](images/cfcc48e51d408e2c22a7026f5e0f2eb67e06b04d70ffe106a2645642b2cfa63c.jpg)

DISTRIBUTioNC.Distributionauthorizedto U.S.Government Agenciesand their contractors,9-Aug-19. Otherrequests forthisdocument shallbereferredto AFRL/RQQD.

·控制AFSIM的实时推演  
·可用于战争游戏  
·提供人在环(OITL)的操作  
·提供用户关于控制和展示等方面的自定义扩展

![](images/fed47373dbcc364abe8144e54a82d72d3530b27cd365bc6d16a7fcae4d37f9ef.jpg)

![](images/192067a72586b2e1e681463a9520d4cb069d73bf236a6832a80630669bc085cc.jpg)

DISTRIBUTioNC.DistributionauthorizedtoU.S.Government Agenciesand theircontractors,9-Aug-19. Otherrequestsforthisdocument shallbereferredto AFRL/RQQD.

13

![](images/c3d8d9557e8816910e2d6f0d74892048c03dd5b81fc64e256c70a29940a978d7.jpg)

# UNCLASSIFIED

# 应用程序:回放评估工具Mystic

![](images/262433619e7a4a0d641d435b21e036570292d0f7b8fb384d4186a14fb25ce7e3.jpg)

![](images/5d5002df57dbd968c8797ad58a7a3f2fbbeb41d9ecda57130c9b8f7d9f57fea0.jpg)  
可视化关系和传感器范围

![](images/0dfac0545ffd721b1d642452340643d052904a3bb3b6deb299e044f44f852cc3.jpg)  
跟踪交战事件

![](images/4757001b62e28c4db0c45692d77839bd898275b75070060fecf314b820352b8a.jpg)  
记录传感器的侦察尝试

![](images/8cc5ba6ea30e7cf42993a3c4d2ea81ce9326ae245e02b7f247075c5be987a58c.jpg)  
绘制平台路径

DISTRIBUTioNC.DistributionauthorizedtoU.S.Government Agenciesand their contractors,9-Aug-19. Otherrequests forthisdocument shallbereferredto AFRL/RQQD.

·任务工具Mission

－根据想定推演计算生成推演结果，该结果可以被Mystic直接回放.

·交战工具Engage

－一对一的交战计算工具

·传感器绘制Sensor_plot

－用于产生数据用于绘制：

·传感器的垂直覆盖   
·传感器的水平覆盖   
·传感器的防区集合

·武器工具Weapon_tools

产生武器的发射计算数据（比如：发射可接受区域、武器交战区、飞行扇形区域）

DISTRIBUTioNC.DistributionauthorizedtoU.S.Government Agenciesand theircontractors,9-Aug-19. OtherrequestsforthisdocumentshallbereferredtoAFRL/RQQD.

15

![](images/6dc344a87baf11a9e71f36aa16af1bfb0fd7b62859035c538fa532fde013a17d.jpg)

# UNCLASSIFIED

# 命令，脚本和方法

![](images/05115616986aa1953a4bbe989ef59c835f1b2c8b94514d171dd5c1c79528fb2c.jpg)

·AFSIM模型是由命令、脚本和方法构成的

-命令：

·定义对象特征   
·实例化对象

－脚本：

·控制对象  
·检索模拟数据   
·方法：

－访问对象信息  
－改变对象状态

![](images/ee1114f8ed08b4c3d9f4a15006fdb0b48aec0e82dbde2883ac3011ddf41cf87a.jpg)

DISTRIBUTioNC.Distributionauthorizedto U.S.Government Agenciesand their contractors,9-Aug-19. Otherrequests forthisdocument shallbereferredto AFRL/RQQD.

定义了一个叫做

# FIGHTER的平台类型

－继承自

# WSF_PLATFORM

仅仅包含了一个运动组件mover

创建了一个FIGHTER

# 的实例叫做platform-1

给定了platform-1的图 标

－给定了它的路线

```txt
14 platform_type FIGHTER WSFPLATFORM
2 mover WSF_AIR_MOVER
3 end mover
4 endplatform_type
5
6 platform platform-1 FIGHTER
7 icon F-15
8 route
9
10
11 position 38:44:50n 90:21:41w
12 speed 480 kts
13 position 38:44:42n 89:59:48w altitude 30000.00 ft
14 position 38:21:14n 85:40:20w
15 position 38:13:41N 85:39:49W altitude 0.0 ft
16 end-route
17 heading 90 deg
18 endplatform 
```

DISTRIBUTioNC.Distributionauthorizedto U.S.Government Agenciesand their contractors,9-Aug-19.

Otherrequestsforthisdocument shallbereferredto AFRL/RQQD.

![](images/0443678145878d9e4e0b50532ef007af6817ecd8d527cb61ab790546e5110359.jpg)

# UNCLASSIFIED

# 脚本例子

![](images/32e437842b81576c1cb0e55256ab9247de93eeca9d08f7b7b95659b5c28a526a.jpg)

```txt
42   
43 execute at_time 1.0 sec absolute   
44 WsfPlatform p = WsfSimulation.CreatePlatform("FIGHTER");   
45 p.ProcessInput("icon F-15");   
46 WsfPlatform pa = WsfSimulation.AddPlatform(p, "platform-2");   
47 if (pa.IsValid())   
48 {   
49 WsfGeoPoint tempPoint = WsfGeoPoint();   
50 WsfRoute newRoute = WsfRoute();   
51 tempPoint.Construct("38:44:50n 90:21:41w");   
52 newRoute.Add(tempPoint, 0.0);   
53 tempPoint.Set(WsfGeoPoint.Construct(38.74, -89.99, 9144.));   
54 newRoute.Add(tempPoint, 246.9);   
55 tempPoint.Set(WsfGeoPoint.Construct(38.35, -85.7, 9144.));   
56 newRoute.Add(tempPoint, 246.9);   
57 tempPoint.Set(WsfGeoPoint.Construct(38.21, -85.65, 0.0));   
58 newRoute.Add(tempPoint, 0.0);   
59 pa.FollowRoute(newRoute);   
60 }   
61 else   
62 {   
63 writeIn("****** ERROR T=", TIME NOW, "Could not add platform of type ", p.Type());   
64 }   
65 end_execute   
66 
```

DISTRIBUTioNC.Distributionauthorizedto U.S.Government Agenciesand their contractors,9-Aug-19.

Otherrequestsfor thisdocument shallbereferredto AFRL/RQQD.

冒泡排序-一个典型的小例子  
定义一个全局的脚本可以在任何地方使用  
包括典型的代码结构：

-while和for循环   
－if条件判断  
－变量声明  
－分配内存

adapted from http://www.aldolist.net/Algorithms/Sorting/Buscript ArrayInt> bubbleSort(Array int arr)   
Array output $=$ Arrayint(); for (int $\mathrm{i} = 0$ .i $<$ arr.Size); $\mathrm{i} = \mathrm{i} + \mathrm{i})$ {output[i] $=$ arr[i]; }#all in one line bool swapped $=$ true; int j $= 0$ . int tmp; while swapped { swapped $=$ false; $\mathrm{j} = \mathrm{j} + \mathrm{i}$ . for (int i $= 0$ ; i $<$ output.Size() -j; i=i+i){ if(output[i] $>$ output[i+1]) { tmp $=$ output[i]; output[i] $=$ output[i+1]; output[i+1] $=$ tmp; swapped $=$ true; } #if check } #for loop } #while loop return output;   
endScript

adapted from http://www.algolist.net/Algorithms/Sorting/Bubble_sort

DISTRIBUTioNC.Distributionauthorizedto U.S.Government Agenciesand their contractors,9-Aug-19.

OtherrequestsforthisdocumentshallbereferredtoAFRL/RQQD

19

![](images/29eceb576ae2f21ab5cdda6232c74d85cb327ae7479443ee889afd35af96ea76.jpg)

# UNCLASSIFIED

# “Big Power”示例

![](images/66496724ff10f118e8ef869c204857932fd5e3a3ef7c1bebac33ef6ef011048c.jpg)

创建1000个随机位置的在飞行中的飞机

```c
1+ platform_type COMMERCIAL_JET WSF PLATFORM
2 mover WSF_AIR_MOVER end_mover
3endPlatform_type
4
5 execute at_time 0.1 sec absolute
6 double lat; double lon; double head;
7 double dist = 600. * MATH.M_PER_NM();
8 string rte;
9 WsfGeoPoint startPt = WsfGeoPoint();
10 WsfGeoPoint endPt = WsfGeoPoint();
11 for (int i = 1; i <= 1000; i = i + 1)
12 {
13 { WsfPlatform p = WsfSimulation.CreatePlatform("COMMERCIAL_JET");
14 p.ProcessInput("icon B-747");
15 }
16     lat = RANDOM.Uniform(30., 50);
17     lon = RANDOM.Uniform(70., 130);
18     head = RANDOM.Uniform(-180., 180);
19     string loc = write_str("position", lat, "n", lon, "w altitude 30000 ft msl");
20     p.ProcessInput(loc);
21     string temp = (string)i;
22     if (i < 10) temp = write_str("θ", temp);
23     if (i < 100) temp = write_str("θ", temp);
24     if (i < 1000) temp = write_str("θ", temp);
25     string name = write_str("commercial-", temp);
26     WsfPlatform pa = WsfSimulation.AddPlatform(p, name);
27     if (pa.IsValid())
28     { paTURNToHeading(RANDOM.Uniform(-180., 180));
29     pa.GoToSpeed(480. * MATH.MPS_PER_NMPH());
30 } else
31 break;
32 }
33 }
34 } end_execute
35 end_execute
36 }
dis_interface
37 record commercial.rep
38 end_dis_interface
39 end_time 1 hour 
```

DISTRIBUTioNC.Distributionauthorized to U.S.Government Agenciesand their contractors,9-Aug-19.

Otherrequestsforthisdocument shallbereferredtoAFRL/RQQD

![](images/54940f0ddc72df679460e6000dc952ed717740cb36d66342ab2f792c79110c9c.jpg)

DISTRIBUTioNC.DistributionauthorizedtoU.S.Government Agenciesand theircontractors,9-Aug-19. Otherrequestsforthisdocument shallbereferredto AFRL/RQQD.

21

![](images/2451e0d304e02352347c5eb617b5692db378af2ec18c6e35f55872ba28616df8.jpg)

# UNCLASSIFIED

# 脚本文档页面

![](images/0b77b3a894ebcdab8e1038acd12ff0e209b5e1ecc6a931b1e70270c19768b24d.jpg)

![](images/18597ac8afaf7b7604243234bdf1c5ba12fdd4189019657e240bc92477d33a15.jpg)

DISTRIBUTioNC.DistributionauthorizedtoU.S.Government Agenciesand their contractors,9-Aug-19. Otherrequestsforthisdocumentshallbereferredto AFRL/RQQD

·HTML格式  
·可以使用浏览器看  
·可打印

![](images/139ce1a4da53057d447449721d19c1712a14ef130be913b88c2d4f63a8c201e0.jpg)

DISTRIBUTioNC.DistributionauthorizedtoU.S.Government Agenciesand theircontractors,9-Aug-19. Otherrequestsforthisdocument shallbereferredto AFRL/RQQD.

23

![](images/118791a1d158c28d7daada1fbcb5c858ce735bae9d6b35d996f88c5d92d3cd56.jpg)

# UNCLASSIFIED

# 快速查询

![](images/5a37d1748ad00385886bd280b6f9f48586d16f66b7c60c050e75575b433fdd9b.jpg)

·输入time就会返回所有的包含time的页面  
·当你要知道你要搜索的关键字时，非常有用.

![](images/7afa056e51797b7037351af2a1983915688c0c1ff798d8974ac1961214110a20.jpg)

DISTRIBUTioNC.Distributionauthorized to U.S.Government Agenciesand their contractors,9-Aug-19. Otherrequestsfor thisdocument shallbereferredto AFRL/RQQD.

·包含每个页面  
·按字母排序

![](images/defa48cff8247dda29f7efe4d748b31d59d074d506721077b8ff9ac3f4536308.jpg)

# WSFReference Guide

·Simulation Runtime

.Silelaputandoutput

Defining Models&Data

Electronic Warfare

:Intera

![](images/61d5ab3fa13006510b28126bd46a8f28764d3e87e2d396af638fefe6ccdb075f.jpg)

DISTRIBUTioNC.DistributionauthorizedtoU.S.Government Agenciesand theircontractors,9-Aug-19. OtherrequestsforthisdocumentshallbereferredtoAFRL/RQQD.

![](images/b13c8ca745df461055d9c46799b7ee72f35381d9b88f05241f58428602b63b52.jpg)

# UNCLASSIFIED

# 免责声明

![](images/1ff3a3fa83cc8fc3c3882c0bf9800e96c3b1db91b2a083d388dcd5ab8a39ef9b.jpg)

·AFSIM培训模块中对作战系统的所有表示均使用虚构的数值构建，旨在保持通用性。  
·作战系统的表示仅用于教授AFSIM软件的操作。  
·培训部分中的平台、传感器和武器不代表任何真实或拟议的战术系统。  
·用户应自行收集和验证数据，以便使用AFSIM进行分析。

·想定发生在北部的佛罗里达斯坦

－靠近城市杰克逊纳巴德

·“红色"帝国正在攻击目标

－他们使用轰炸机进行打击

·“蓝色"防御部队将尝试阻止这些打击

－使用地对空导弹（SAM）系统

DISTRIBUTioNC.Distributionauthorized to U.S.Government Agenciesand their contractors,9-Aug-19. Otherrequests forthisdocumentshallbereferredtoAFRL/RQQD.

27

![](images/a1655c5967540132957cf33de4d88e277f8272cffa743f18fd76369fcbcdf26e.jpg)

# UNCLASSIFIED

# 佛罗里达斯坦

![](images/af63cfdaa1cbe3f9693e9b46917cfe8bdf05abb6ce7c550af0a178405715b59c.jpg)

![](images/c03d00991cce8e80ccefa3e8b65fbe7c2d5a564343980197768b96d6c98bced3.jpg)

DISTRIBUTioNC.Distributionauthorized to U.S.Government Agenciesand their contractors,9-Aug-19. Otherrequests forthisdocument shallbereferredto AFRL/RQQD.

![](images/40e9e033f5e031841500c5dad10186ac4181dfb65893cdc3ce0ff2770ad99bb5.jpg)  
DISTRIBUTioNC.DistributionauthorizedtoU.S.Government Agenciesand theircontractors,9-Aug-19. Otherrequestsforthisdocument shallbereferredto AFRL/RQQD.

29

![](images/47e1a77602c5f9dd0fc49050d1bde8ce3cf9c04c3f467054988255001f6f7e0c.jpg)

# UNCLASSIFIED

# 重温学习内容

![](images/ed45b2d73e32e3b9195e5f3b8601df051db7a8b900a8f6915e7a692902704053.jpg)

# ·包括

-描述课程内容  
－介绍什么是AFSIM  
－介绍AFSIM的脚本由哪些部分组成  
－描述AFSIM有哪些基本输出

![](images/9733cb74c59153c370e649d9e9ae0678875822fc826aedcc377ef74dc40988b1.jpg)

DISTRIBUTioNC.Distributionauthorized to U.S.Government Agenciesand their contractors,9-Aug-19. Otherrequestsfor thisdocument shallbereferredto AFRL/RQQD.

30

# 6.1.1.2.2. 2_AFSIM 应用程序工具 2_AFSIM_User_Training_Applications_Tools

本文为 afsim2.9_src\training\user\1_AFSIM_Intro\slides\2_AFSIM_User_Training_Applications_Tools.pptx 的翻译。

![](images/a9a384f43ef7b993422024f20885fe7d2a37b3b3e94d51a98c16e12919bb7623.jpg)  
DISTRIBUTioNC.Distributionauthorized to U.S.Government Agenciesand their contractors,9-Aug-19. Otherrequestsforthisdocument shallbereferred toAFRL/RQQD.

41

![](images/03f70a08c933b25dd320f1c78d2e6217a948b0267a86cb0abaf35308824f8de1.jpg)

# UNCLASSIFIED

# 回顾学习内容

![](images/5d3b77de8b7d7f5870158a95cb2eedf7e549784f4e1490770d48a5c27431b497.jpg)

# ·你将会掌握：

－查找应用程序和工具  
－使用文档检索  
－使用Wizard运行不同的示例Demo  
－使用Mystic来运行仿真结果文件.aer  
－创建一个"Hello World"想定

![](images/a2a3117d9d0080ccf7c2e9d9db24e025ca558697c9f35a0ee1b90bac6390389f.jpg)  
DISTRIBUTioNC.DistributionauthorizedtoU.S.Government Agenciesand their contractors,9-Aug-19. Otherrequestsforthisdocument shallbereferredtoAFRL/RQQD.

![](images/b6a22e19a2025b4c7c4b637b618007ee77d10d314cc5a260ccfa78f9047c4995.jpg)

Integrity★Service★ Excellence

# AFSIM用户培训

# 2－应用程序和工具

13324598743

# AFRL/RQQD美国空军研究实验室

DISTRIBUTioNC.Distributionauthorized to U.S.Government Agenciesand their contractors,9-Aug-19. Otherrequestsforthisdocument shallbereferred toAFRL/RQQD.

1

![](images/43019e1a3f3d26e2bf181d51a4262221b47e31ff8146b421e9cf57c290a07c34.jpg)

UNCLASSIFIED

# 学习内容

![](images/b40e3373341c0062d98f8d4bbb390697426726be13d9002991f4f22f1f6922b6.jpg)

·你将会掌握：

－查找应用程序和工具  
－使用文档检索  
－使用Wizard运行不同的示例Demo  
－使用Mystic来运行仿真结果文件.aer  
－创建一个"Hello World"想定

![](images/f1dc9f6451cdd9cd178daa89cb0411197d9a91b99f0fa46f9f3adb6183e8b69e.jpg)

DISTRIBUTioNC.Distributionauthorizedto U.S.Government Agenciesand their contractors,9-Aug-19. Otherrequestsforthisdocument shallbereferredtoAFRL/RQQD.

#

bin   
demos   
documentation   
resources   
swdev   
tools   
training

#

#

DISTRIBUTioNC.Distributionauthorized to U.S.Government Agenciesand their contractors,9-Aug-19. Otherrequestsforthisdocument shallbereferred toAFRL/RQQD.

![](images/181fc3b09b47a698437fbc95ea6e493d637b5939691b9617e0b39a3ccc8e73f0.jpg)

# UNCLASSIFIED

# 各文件夹下的主要内容

![](images/0463a1b408e9269bbe5cac9f8c25693013d6e0e29c00a04968125a89094dfae9.jpg)

#

grammar/

# demos

#

data/

#

#

#

html/

DISTRIBUTioNC.DistributionauthorizedtoU.S.Government Agenciesand theircontractors,9-Aug-19. Otherrequests forthisdocument shallbereferredtoAFRL/RQQD.

<table><tr><td>Name</td><td>Date modified</td><td>Type</td><td>Size</td></tr><tr><td>■ engagebéram</td><td>8/27/2020 12:23 AM</td><td>File folder</td><td></td></tr><tr><td>■ grammar</td><td>8/27/2020 12:23 AM</td><td>File folder</td><td></td></tr><tr><td>■ lib</td><td>8/27/2020 12:23 AM</td><td>File folder</td><td></td></tr><tr><td>■ missionbéram</td><td>8/27/2020 12:23 AM</td><td>File folder</td><td></td></tr><tr><td>■ missionPlugins</td><td>8/27/2020 12:23 AM</td><td>File folder</td><td></td></tr><tr><td>■ mystic plugins</td><td>8/27/2020 12:23 AM</td><td>File folder</td><td></td></tr><tr><td>■ osgPlugins-3.6.3</td><td>8/27/2020 12:23 AM</td><td>File folder</td><td></td></tr><tr><td>■ qt plugins</td><td>8/27/2020 12:23 AM</td><td>File folder</td><td></td></tr><tr><td>■ sensor.plotbéram</td><td>8/27/2020 12:23 AM</td><td>File folder</td><td></td></tr><tr><td>■ warlockbéram</td><td>8/27/2020 12:23 AM</td><td>File folder</td><td></td></tr><tr><td>■ warlockPlugins</td><td>8/27/2020 12:23 AM</td><td>File folder</td><td></td></tr><tr><td>■ weapon.toolsbéram</td><td>8/27/2020 12:23 AM</td><td>File folder</td><td></td></tr><tr><td>■ wizardPlugins</td><td>8/27/2020 12:23 AM</td><td>File folder</td><td></td></tr><tr><td>■ wkfPlugins</td><td>8/27/2020 12:23 AM</td><td>File folder</td><td></td></tr><tr><td>■ wsf plugins</td><td>8/27/2020 12:23 AM</td><td>File folder</td><td></td></tr><tr><td>■ crd importer_execexe</td><td>8/26/2020 11:41 PM</td><td>Application</td><td>30 KB</td></tr><tr><td>■ engageexe</td><td>8/26/2020 11:41 PM</td><td>Application</td><td>384 KB</td></tr><tr><td>■evtreader.exe</td><td>8/26/2020 11:41 PM</td><td>Application</td><td>110 KB</td></tr><tr><td>■ mission.exe</td><td>8/26/2020 11:42 PM</td><td>Application</td><td>142 KB</td></tr><tr><td>■ mover creator.exe</td><td>8/26/2020 11:42 PM</td><td>Application</td><td>3,725 KB</td></tr><tr><td>■ mystic.exe</td><td>8/26/2020 11:43 PM</td><td>Application</td><td>178 KB</td></tr><tr><td>■ post Processor.exe</td><td>8/26/2020 11:43 PM</td><td>Application</td><td>367 KB</td></tr><tr><td>■ sensorPlugins.exe</td><td>8/26/2020 11:43 PM</td><td>Application</td><td>177 KB</td></tr><tr><td>■ warlock.exe</td><td>8/26/2020 11:44 PM</td><td>Application</td><td>225 KB</td></tr><tr><td>■ weapon.tools.exe</td><td>8/26/2020 11:44 PM</td><td>Application</td><td>424 KB</td></tr><tr><td>■ wizard.exe</td><td>8/26/2020 11:44 PM</td><td>Application</td><td>142 KB</td></tr></table>

DISTRIBUTioNC.DistributionauthorizedtoU.S.Government Agenciesand theircontractors,9-Aug-19. Otherrequests forthisdocument shallbereferredtoAFRL/RQQD.

5

![](images/f399ce2003aedf030fa07ab7a1f8640c7536f031f96a254b9491c671ac78e0ee.jpg)

# UNCLASSIFIED

# 将Wizard程序创建桌面快捷方式

![](images/b23e89cf12aaa5c1059177d9dd05010ad6138d47cef88d4a758339381599246c.jpg)

如右图对着其点右键，发送到桌面快捷方式，桌面上就有了下图的图标

![](images/ded0aa65dc01b04d8bbb63118f62fade0f708b46f98931e1b7ab8f7f7f0f8358.jpg)

![](images/c3775fc14bee7059df288d631bb11dcc5e610208f41ed85ee0e714ea612e2a28.jpg)

DISTRIBUTioNC.DistributionauthorizedtoU.S.Government Agenciesand their contractors,9-Aug-19.

Otherrequestsforthisdocument shallbereferredtoAFRL/RQQD.

双击bin文件夹下的wizard.exe-或  
双击桌面的快捷方式  
小技巧

直接将一个想定顶级启动.txt脚本拖到wizard图标上也会在wizard中打开这个脚本。

![](images/7cc78bc403cd2c625b40dbc8c1dd95f53e260a9d3c58879c90cddb23be3965a0.jpg)

DISTRIBUTioNC.Distributionauthorized to U.S.Government Agenciesand their contractors,9-Aug-19. Otherrequestsforthisdocument shallbereferred toAFRL/RQQD.

7

![](images/b6310876f45099437b9a83b61fd21ab9ed4f59f04f9a020cb82da3e21356b7ad.jpg)

# UNCLASSIFIED

# 你将会看到

![](images/4876c14637e12af12b7169b3f5960d582822b783d9d964d3a21851b531d1f223.jpg)

![](images/e34f5f3a912558dbe3eba6478a0e9de04a53d631446217ef00deab77a165d8e3.jpg)

DISTRIBUTioNC.DistributionauthorizedtoU.S.Government Agenciesand theircontractors,9-Aug-19.

Otherrequestsforthisdocument shallbereferredtoAFRL/RQQD.

![](images/6006470e353507641b47534103e9b46894c588d41e99c97fc6c7a69610608408.jpg)  
DISTRIBUTioNC.Distributionauthorized to U.S.Government Agenciesand their contractors,9-Aug-19. Otherrequestsforthisdocument shallbereferred toAFRL/RQQD.

9

![](images/d0da0f715a23cd00f916c2f81fdae7f72fa415409e1d50f03c788468b32ccc13.jpg)

# UNCLASSIFIED

# 收藏该页面

![](images/303887c09c4d26d70371458a9fb61d98bc0b070e0d9fa46dba55c605c440e845.jpg)

![](images/e2aace2c06ce61ce1a8aa1877d8b4867c161ecd281a2880ce8c5089ea54f28a6.jpg)

# Wizard User's Guide

#

#

DISTRIBUTioNC.DistributionauthorizedtoU.S.Government Agenciesand their contractors,9-Aug-19.

OtherrequestsforthisdocumentshallbereferredtoAFRL/RQQD.

·HTML格式  
·也可以通过wizard的help->documentation打开  
·通过documentation文件夹下的index.html打开

－、帮助文档的启动页面

·从wizard打开

－帮助菜单

-对wizard中在编辑的

脚本的关键字点右键在弹出菜单中

![](images/1feb451303a24c20e62f53466856c9f5607d16e18ab5bc6c39512104d49fa5c0.jpg)

![](images/41f8bcef36d6ae522bb0f77578b4c5294c6826d8efc81b78b7d47aa419e865a8.jpg)

DISTRIBUTioNC.Distributionauthorized to U.S.Government Agenciesand their contractors,9-Aug-19. OtherreguestsforthisdocumentshallbereferredtoAFRL/RQQD.

11

![](images/15167376b64bd43379b920f9ff268767951a17fb487519d4bbb7b49beb7db1c6.jpg)

# UNCLASSIFIED

# 点击browse

![](images/a86c5557256c189baa260397320f960d38f71be58bfad22589f971f5d7b9c8d2.jpg)

![](images/72553b57c7d1586ea289be4b262280dfa3de93eba9be93258e3e07cfb90a2b9d.jpg)

DISTRIBUTioNC.Distributionauthorizedto U.S.Government Agenciesand theircontractors,9-Aug-19

Otherrequestsforthisdocument shallbereferredtoAFRL/RQQD.

![](images/f186748dfa9a5b4b9613c0eddfbabf62a941d2a48954c81d2f8094159be0a5ce.jpg)  
DISTRIBUTioNC.Distributionauthorized to U.S.Government Agenciesand their contractors,9-Aug-19. Otherrequestsforthisdocument shallbereferred toAFRL/RQQD.

13

![](images/b853e3b381df548c2ef92dfe7a166b83804111ad01b7574976fcb1ec6edb7c07.jpg)

# UNCLASSIFIED

# 浏览到demos文件夹

![](images/828d0346913d8fc7697cad675c87504961d342afde023142ebe2f7130f9c42da.jpg)

![](images/817f6c23211cd5c08461ab9cf1ff5dbfe19fc9ed705ffcb9e24847ac5a5c515d.jpg)

bin

demos

![](images/5d9a905307bcd898c5495bac37fb52a265c5e61686068a3809b6aaae5f89335a.jpg)

documentation

![](images/ece8d529faf76ba2115818957fa94a9b3d958ff5b8c739f7c5650beef41d3244.jpg)

resources

![](images/37225f265a6263f668e1e27ef0cdaa48c86cb6ffc74db9f1d7239bee2ef212ae.jpg)

swdev

![](images/4c6e92db67fee863c5436c728307fa800a7e693076c236d194ec449310603f47.jpg)

tools

![](images/0b50104ff3a443d69982f6be7e14102241c75da161c0b4a3dda078f003e58957.jpg)

training

DISTRIBUTioNC.Distributionauthorizedto U.S.Government Agenciesand their contractors,9-Aug-19. Otherrequestsforthisdocument shallbereferredtoAFRL/RQQD.

![](images/0058855a9e23674be70934e48e55fd458123d037ea3d1e1290e80010184a63b4.jpg)

DISTRIBUTioNC.Distributionauthorized to U.S.Government Agenciesand their contractors,9-Aug-19. Otherrequestsforthisdocument shallbereferred toAFRL/RQQD.

15

![](images/2c3a0fa5d73c2d438ab97c941570f597068032d13e887bce22b467b6559cb511.jpg)

# UNCLASSIFIED

# 双击“ballistic_shootdown.txt"

![](images/df3061a28bfb3af41c046ebb194171faa6c6347fa9a5cb1bbe31679db775e2b5.jpg)

![](images/ff254dbf34145cfcc6872f61c55638884d0d21e7cc984d46628fe2a2d5d9132c.jpg)

DISTRIBUTioNC.DistributionauthorizedtoU.S.Government Agenciesand their contractors,9-Aug-19.

OtherrequestsforthisdocumentshallbereferredtoAFRL/RQQD.

![](images/6dc481ea76e6b87518f96db49279df2b373a6c2ed5557c50e872a7fb71f187ea.jpg)  
DISTRIBUTioNC.Distributionauthorized to U.S.Government Agenciesand their contractors,9-Aug-19. Otherrequestsforthisdocument shallbereferred toAFRL/RQQD.

![](images/2a1fb0371baab52119c7452d80659798edf1148556b479044640e273f8e115fb.jpg)

# UNCLASSIFIED

# 你会看到

![](images/fbc6df167ea57c12e250bb54036472218a8811300b447fc4500fc00ac389d65f.jpg)

![](images/21457a41a8e63e9c025b00f905bdceb761453014f408130c26881b3d38a8b06b.jpg)  
DISTRIBUTioNC.Distributionauthorizedto U.S.Government Agenciesand their contractors,9-Aug-19.   
OtherrequestsforthisdocumentshallbereferredtoAFRL/RQQD.

·Output窗口默认在底部  
·你可以通过output窗口的内容查看demo在运行过程中发生了什么，以及事件发生的具体时间

![](images/6a5f9cd9a0f6f9f451b622d640b2962a8a5fb31ec874038f4e20210a427a226d.jpg)

DISTRIBUTioNC.Distributionauthorized to U.S.Government Agenciesand their contractors,9-Aug-19. OtherreguestsforthisdocumentshallbereferredtoAFRL/RQQD.

19

![](images/1e2164a01e4d02e26689cecb7cd4d394e928acfb9b1b80e58ade48667a60fead.jpg)

# UNCLASSIFIED

# 标准的想定输出

![](images/5e76e08ca6c29a7c463526437cfee67e44b477a47f507f7d0a22131e92a98978.jpg)

# ·双击Project Browser树中的log日志文件

![](images/1f3a13a8ba2a1a24d7c3fd613dbd847ff9d5ad2a948e6056f60aa2945157f9ab.jpg)

![](images/1a46affb042c184978fab5bc757621d2ae6cc6a030ba0c33602cddafa71a25eb.jpg)

DISTRIBUTioNC.Distributionauthorizedto U.S.Government Agenciesandtheircontractors,9-Aug-19

Otherrequestsforthisdocument shallbereferredtoAFRL/RQQD.

# ·日期，时间，包含的文件，以及相关版本

```txt
#shootdown.log
1 2020-09-20 20:27:50 version wsf 2.7.0
2 2020-09-20 20:27:50 file ballistic_shootdown.txt
3 2020-09-20 20:27:50 file event_output.txt
4 2020-09-20 20:27:50 file setup.txt
5 2020-09-20 20:27:51 file platforms/common.txt
6 2020-09-20 20:27:51 file platforms/df-21b launcher.txt
7 2020-09-20 20:27:51 file ./weapons/ssm/df-21b.txt
8 2020-09-20 20:27:51 file weapons\\ssm\show_spent_stages.txt
9 2020-09-20 20:27:51 file ./processors/launch_ssm Processor.txt
10 2020-09-20 20:27:51 file platforms/target.txt
11 2020-09-20 20:27:51 file platforms/rim-161 launcher.txt
12 2020-09-20 20:27:51 file ./weapons/sam/rim-161.txt
13 2020-09-20 20:27:51 file platforms/rim-161battery.txt
14 2020-09-20 20:27:51 file ./processors/anti_ballistic Missile处理器.txt
15 2020-09-20 20:27:51 file platforms/an_tpy-2.txt
16 2020-09-20 20:27:51 file ./sensors/radar/an_tpy-2.txt
17 2020-09-20 20:27:51 file scenarios/red Launcher.sgs.txt
18 2020-09-20 20:27:51 file scenarios/blueSide.txt
19 2020-09-20 20:27:51 file weapons\\ssm\df-21b-launch_data.txt
20 2020-09-20 20:27:51 file ./weapons/sam/rim-161 launch_data.txt
21 2020-09-20 20:27:51 AER output file: output/ballistic_shootdown.aer
22 2020-09-20 20:27:51 Event output file: output/ballistic_shootdown.evt
23 2020-09-20 20:27:51 start 1
24 2020-09-20 20:27:52 complete 1800.001 1.036 1.031
```
```
```bash
#shootdown.log
1 2020-09-20 20:27:50 version wsf 2.7.0
2 2020-09-20 20:27:50 file ballistic_shootdown.txt
3 2020-09-20 20:27:51 file event_output.txt
4 2020-09-20 20:27:51 file setup.txt
5 2020-09-20 20:27:51 file platforms/common.txt
6 2020-09-20 20:27:51 file platforms/df-21b launcher.txt
7 2020-09-20 20:27:51 file ./weapons/ssm/df-21b.txt
8 2
9 1
13 1
14 1
15 1
16 1
17 1
18 1
19 1
```
```
```bash
#shootdown.log
1 2033.3.33.33.33.33.33.33.33.33.33.33.33.33.33.33.33.33.33.33.33.33.33.33.33.33.33.33.33.33.33.33.33.33.33.3 
```

DISTRIBUTioNC.Distributionauthorized to U.S.Government Agenciesand theircontractors,9-Aug-19. Otherrequestsforthisdocument shallbereferred toAFRL/RQQD.

21

![](images/5f9a42b77f8aeae222f2cb06724316d981cc127ee1b44868d22290a92e20a208.jpg)

# UNCLASSIFIED

# 事件文件

![](images/712feb1cf074ec0e27038740e0156f1fe91cc323f402aae378edae644e3323b6.jpg)

# ·在Project Browser树中双击evt文件

![](images/cbfddaafdf36e1b6ebd1d98c1abd5f78ab2d406ac7f6a94c57155de5abae1a77.jpg)

![](images/c58ce15d7ca7cae247d60daa6e121189481b0388728ac751ad52ff5d3691f01a.jpg)

DISTRIBUTioNC.DistributionauthorizedtoU.S.Government Agenciesand theircontractors,9-Aug-19.

OtherrequestsforthisdocumentshallbereferredtoAFRL/RQQD.