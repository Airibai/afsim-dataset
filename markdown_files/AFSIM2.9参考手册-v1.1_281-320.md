最终武器分数使用以下公式计算：

```txt
Weapons Score = Weapons Score / (1 + Sum of Scoring Factors) 
```

因此，累积武器分数基于加权的武器类型、武器子类型、拦截范围、拦截时间、工作负载和击杀概率。您可以设置评分因素以模拟特定的目标/武器配对逻辑。例如，如果威胁系统仅基于拦截时间进行目标/武器配对，以便始终希望将目标与能够最先交战的武器系统配对，则将拦截时间设置为 1，所有其他评分因素设置为 0。

3.3.14. BRAWLER 空空对抗处理器 WSF_BRAWLER_PROCESSOR  
```matlab
platform <platform-name> WFS_BRAWLERPLATFORM
    mind_file ...
    mover ...
    debug ...
    draw_alternatives ...
    draw_nominal_states ...
    time Allowed_per sector_search ...
    consciousness_event_update_time ...
    ... [[platform|Platform Commands]] ...
end-platform 
```

WSF_BRAWLER_PROCESSOR 是用于 BRAWLER 视距内空对空战斗机动的处理器类型。可以在“brawler_demo”中查看其使用的多个示例。该处理器使用 WSF_BRAWLER_MOVER、WSF_PERCEPTION_PROCESSOR 和 WSF_QUANTUM_TASKER_PROCESSOR，并通过脚本行为利用 WsfBrawlerProcessor 的 评 估 和 控 制 功 能 。 WSF_BRAWLER_PROCESSOR 依 赖 于 接 收“WEAPON”任务来确定其在 1v1 空战机动中的目标，这在演示中有示例。

# 命令

mind_file <file-name>: 指定用于建模思维和意识事件更新的 BRAWLER 思维文件。

BRAWLER 未分类版本中的 MIND 文件 $100 \%$ 兼容。

默认值: 无文件 - 使用默认值

mover WSF_BRAWLER_MOVER mover-commands … end_mover: 定义 BRAWLER 平台使用的 BRAWLER 移动器。

□ debug: 如果指定，将为每个替代评估打印调试信息到标准输出。  
▫ draw_alternatives: 如果指定，将在 DIS 重放文件中渲染每个前向投影替代的彩色编码点。绿色表示替代评估接近目前看到的最大值，红色表示相反，黄色/橙色介于两者之间。  
▫ draw_nominal_states: 如果指定，将在 DIS 重放文件中渲染我的目标的前向投影名义状态的彩色编码点。蓝点是我的，紫点是我的目标。BRAWLER 名义状态投影只是一个基于物理的前向投影，其中忽略加速度，速度在投影中保持恒定。名义状态通常用于评估函数中。

time_allowed_per_sector_search <time-value>: 表示允许搜索天空某个扇区的时间。影响意识事件的时间安排。

默认值:10 秒

consciousness_event_update_time <time-value>: 覆盖 BRAWLER 意识事件的时间安排。如果指定，所有意识事件将在此间隔发生。否则，将定期进行动态时间计算以确定适当的意识事件更新时间。

默认值: 未指定

这些命令和设置允许 WSF_BRAWLER_PROCESSOR 在空对空战斗中进行复杂的机动和评估，以优化战斗性能和决策。

3.3.15. 态势感知处理器 WSF_PERCEPTION_PROCESSOR  
```tcl
processor <name> WSF_PERCEPTIONPROCESSOR  
... processor Commands ...  
... Platform Part Commands ...  
... External Link Commands ...  
... WSFScriptPROCESSORCommands ...  
report_interval ...  
reporting_self ...  
reporting_others ...  
asset_perception ...  
perceive_self ...  
threat_update_interval ...  
max-threat_load ...  
threat Importance_function ...  
asset_update_interval ...  
max_asset_load ...  
asset Importance_function ...  
Heat Map Commands ... end_heat_map  
end Processor 
```

WSF_PERCEPTION_PROCESSOR 执行三个主要功能：

状态报告: 作为指挥官、下属和/或同级的资产进行状态报告。  
□ 资产感知建模: 以给定的速率更新，并在给定的最大负载下进行限制。  
▫ 威胁（轨迹）感知建模: 以给定的速率更新，并在给定的最大负载下进行限制。

感知建模的目的是模拟平台代理更新其对这些实体的心理知识。可以将其视为代理在给定的速率下查看雷达屏幕或状态显示，而其心理能力允许他们在脑海中保留有限的信息量。

示例

以下是一个简单的示例，展示了一个下属向指挥官报告资产状态，指挥官基于接收到的消息对该下属有了感知：

```fortran
platform cmd WSFPLATFORM
comm comm1 WSFCOMM_TRANSEIVER
internal_link brain
end_comm
processor brain WSF_PERCEPTIONPROCESSOR
asset_perception statusmessages
asset_update_interval 25 sec
max_asset_load 10
end Processor
end platform
platform sub WSFPLATFORM
commander cmd
comm comm1 WSFCOMM_TRANSEIVER
end_comm
processor brain WSF_PERCEPTIONPROCESSOR
report_interval 10 sec
report_to commander via comm1
end Processor
end platform 
```

# 状态报告命令

report_interval <time-value>: 指定资产状态消息发送给友方的间隔。默认值:0 秒（不进行报告）  
reports_self <boolean-value> / reporting_self <boolean-value>: 指定是否报告关于该平台的资产状态消息。默认值: true  
reports_others <boolean-value> / reporting_others <boolean-value>: 指定是否报告所有接收到的和已知的其他平台的资产状态消息。默认值: false

# 资产感知命令

asset_perception [ status_messages; truth <members> ]: 指定资产感知将利用的消息类型。status_messages 使用接收到的 WSF_ASSET_MESSAGE 消息，truth <members> 使用真实数据。

默认值:truth（但没有成员，因此感知为空）

perceive_self: 将此平台包括在感知资产列表中。默认值: false  
asset_update_interval <time-value>: 指定处理器更新其资产感知的间隔。默认值:0 秒（不延迟间隔，使用当前真实或接收到的资产消息）  
max_asset_load <integer>: 指定资产感知中持有的最大条目数。默认值:0（无最大限制）  
asset_importance_function <string>: 指定用于测量资产重要性的脚本函数名称。脚本函数必须匹配签名 double FunctionName(WsfAssetPerception)。

# 威胁感知命令

threat_update_interval <time-value>: 指定处理器更新其威胁感知的间隔。

默认值:0 秒（不延迟间隔，使用当前主轨迹列表）

max_threat_load <integer>: 指定威胁感知中持有的最大条目数。

默认值:0（无最大限制）

threat_importance_function <string>: 指定用于测量威胁重要性的脚本函数名称。脚本函数必须匹配签名 double FunctionName(WsfLocalTrack)。

# 热图命令

热图用于对感知到的威胁提供一个感知层，显示丢失轨迹的近似位置（“热”）和传感器覆盖的区域（“冷”）。

position <latitude-value> <longitude-value>: 指定热图网格中心点的纬度和经度。

默认值: 0n 0e

altitude <length-value>: 指定热图网格中心点的高度。

默认值: 0 m msl

grid_extent <length-value>: 指定热图网格从中心点延伸的距离。

默认值: $0 \mathsf { m }$

cell_size <length-value>: 指定热图网格中一个单元的边长。

默认值: $0 \mathsf { m }$

heat_decay [0.05 .. 0.9]: 指定热单元随着时间变旧时其值的变化量。

默认值: 0.1

decay_interval <time-value>: 指定热图单元值更新之间的时间。

默认值:30 秒

expansion_timeout <time-value>: 指定热源将继续扩展的时间。

默认值: 240 秒

use_asset_perception <boolean-value>: 指示感知处理器是否应使用资产的传感器覆盖来生成热图的“冷”覆盖。

默认值: false

sensor_range <length-value>: 传感器被认为“清除”热图的距离。

默认值: 0 m

draw_grid <boolean-value> / draw_heat <boolean-value> / draw_sensor_outline<boolean-value>: 指示是否应为热图网格线、热/冷值或传感器覆盖轮廓发出 WsfDraw命令。

默认值: false

# 3.3.16. 综合态势感知处理器 WSF_SA_PROCESSOR

```txt
processor <name> WSF_SAPROCESSOR // Update Interval Commands report_interval ... engagement_data_update_interval ... flight_data_update_interval ... fuel_data_update_interval ... nav_data_update_interval ... flight Controls_data_update_interval ... 
```

```txt
weapons_data_update_interval ...   
asset_data_update_interval ...   
asset_purge_lifetime ...   
perceived_item_data_update_interval ...   
prioritized_item_data_update_interval ...   
perceived_item Calculation update interval ...   
prioritized item calculation update interval ..   
behavior Calculation update interval ... 
```

```txt
// Update Interval Group Commands  
cognitive_update_interval ...  
platform_update_interval ...  
universal_update_interval ... 
```

```txt
// Enemy/Friendly Types  
enemy_side ...  
friendly_side ...  
neutral_side ...  
enemy_type ...  
friendly_type ...  
neutral_type ...  
missile_type ...  
asset Ignore ...  
filter_assets_from_track  
use_iff_id ...  
usesimple_id_by_type 
```

```c
// Missile Identification Filters  
missile_speed_any_alt <speed-value>  
missile_alt_any_speed <length-value>  
missile_speed_with_alt <speed-value>  
missile_alt_with_speed <length-value>  
missile_nose_angle <angle-value>  
missile_time_to_intercept <time-value>  
missile_distance <length-value> 
```

```txt
// Range Settings  
max_range_for_perceived_assets ...  
max_range_for_perceived_bogies_and_bandits ...  
max_range_for_engagement_data ...  
assumed_range_for_angle_only_targets ... 
```

```rust
// Filter Settings for Engagement Assessment filterrequires_same_side ... 
```

```txt
filterrequires.not_same_side ...   
filterrequires_air_domain ...   
filterrequires.not_air_domain ...   
filterrequires_land_or(surface_domain ...   
filterrequires.not_subsurface_domain ...   
filterrequires.not_space_domain ...   
filterrequires.sa Processor ...   
// Optional Track Processors   
esm_track Processor ...   
mws_track Processor ...   
radar_track Processor ...   
irst_track Processor ...   
das_track Processor ...   
flir_track Processor ...   
eyes_track Processor ...   
perception/master_track Processor ... 
```

```txt
// Optional IDs  
flight_id ...  
id_flag ... 
```

```tcl
// Fuel Data  
bingo_fuel ...  
joker_fuel ... 
```

```txt
// Perception Commands  
reports_self ... | reporting_self ...  
reports_others ... | reporting_others ...  
asset_perception ...  
perceive_self ...  
max-threat_load ...  
max_asset_load ...  
asset_coast_time ...  
bandit_coast_time ...  
bogey_coast_time ...  
usesimplecountermeasures...  
num_chaff ...  
num_flares ...  
num_decoys ...  
filter_assets_from_bogies ...  
consideration_score_randomness ...  
display_perception_delay ...  
visual_perception_delay ... 
```

```txt
// Assessment Commands  
bogie-threat_score-multiplier ...  
bogie_target_score-multiplier ...  
ignore_bogies_when_grouping ...  
mission_task ...  
max_prioritized_threats ...  
max_prioritized_targets ...  
max_grouping_distance_centroid ...  
max_grouping_distancebles neighbor ...  
max_grouping_speed_diffrence ...  
max_grouping Heading_diffrence ...  
min_group_radius ...  
use_centroid_grouping ...  
use_neighbors_grouping ...  
use_speed_grouping ...  
use Heading_grouping ...  
use_type_grouping ...  
ignore_missiles_as_threats ...  
ignore_bogies_as_threats ...  
ignore_missiles_as_targets ...  
ignore_bogies_as_targets ...  
missile_wez_parameters ...  
aircraft_signature_parameters ... 
```

// Custom Scripts   
```txt
script double AssetConsiderationScoring ...   
script double BogieBanditConsiderationScoring ...   
script double MissileConsiderationScoring ...   
script double UnfocusedGroupConsiderationScoring ...   
script Array<WsfSA_PerceivedItem> CreatePerceivedItemPruningArray ...   
script double CalculateRisk ...   
script double CalculateSelfRisk ...   
script double CalculateFlightRisk ...   
script double CalculatePackageRisk ...   
script double CalculateMissionRisk ...   
script double CalculateDefensiveness ...   
script double CalculateUrgency ...   
script bool CalculateWeaponSupport ...   
script double CalculateThreatLevel ...   
script double CalculateMissileThreatLevel ...   
script double CalculateGroupThreatLevel ...   
script double CalculateTargetValue ... 
```

```txt
script double CalculateMissileTargetValue ...  
script double CalculateGroupTargetValue ...  
script double CalculateRiskPosedByEntity ...  
script double CalculateDefensivenessInducedByEntity ...  
script double CalculateUrgencyInducedByEntity ...  
script WsfGeoPoint ProjectPositionInTime ...  
script WsfGeoPoint ProjectPositionForward ...  
script WsfGeoPoint ProjectPositionLevelTurnLeft ...  
script WsfGeoPoint ProjectPositionLevelTurnRight ...  
script WsfGeoPoint ProjectPositionTurnToHeading ...  
script WsfGeoPoint ProjectPositionGoToPoint ...  
script WsfGeoPoint ProjectPositionSlice ...  
script WsfGeoPoint ProjectPositionSliceToHeading ...  
script WsfGeoPoint ProjectPositionSplitS ...  
end Processor 
```

情境感知 (SA) 处理器 是 AFSIM 认知模型的关键组件，提供感知、评估/理解和预测/投射功能。SA 处理器基于 Endsley 的情境感知模型，提供执行 OODA 循环中的观察和定向（OO）组件的方法，而高级行为树（ABTs）则提供执行决策和行动（DA）组件的方法。

# 感知项目

感知项目是 SA 处理器中用于建模认知负荷和限制的主要方法。感知项目包括群组和实体感知。飞行员利用威胁/目标的群组或集群来减少感知项目的数量。在某些情况下，飞行员可能不会感知和记住群组中的每个项目，而是感知和记住整个群组。因此，与其感知四架飞机的集合，飞行员更倾向于感知为一个群组，将感知项目的数量从 4 减少到 1。我们称之为非聚焦群组感知，这是一种在保持一定 SA 的同时减少感知项目数量的方法。然而，在其他情况下，飞行员可能希望对群组中的每个项目有详细的感知，此时飞行员可能会感知这些项目形成一个“概念”群组，仅作为一种组织手段。我们称之为聚焦或详细群组感知，因为它保持了群组成员的完整细节，飞行员专注于群组的成员。这种类型的群组不会影响感知项目的数量。

# 群组感知的视角

实体中心视角：详细群组既不增加也不减少感知项目的数量，其包含的每个实体增加一个感知项目。  
群组中心视角：详细群组增加的感知项目数量等于其包含的实体数量。

# 注意事项

群组和认知限制旨在用于人类飞行员——自主飞行器上的合成飞行员通常不使用群组来减少认知负荷，因为它们通常具有相当大的限制，不需要以这种方式减少认知负荷。

群组可以由 SA 处理器自动形成、解散、聚焦或非聚焦。然而，其许多自动功能可以通过自定义脚本覆盖。

SA 处理器替代了一些以前由 WSF_PERCEPTION_PROCESSOR 执行的功能。虽然允许在

具有 SA 处理器的平台上使用感知处理器，但这不是预期的配置，应尽可能避免。

# 认知模型

在认知模型中，底部用红色表示的是 Boyd 的 OODA（观察、定向、决策和行动）模型。在 AFSIM 中，OODA 循环被分为两个模块，显示在 OODA 块的上方。SA 处理器（蓝色）处理观察和定向，而高级行为树（绿色）执行决策和行动。

这种结构使得 SA 处理器能够有效地支持飞行员在复杂环境中的感知和决策过程，从而提高任务的成功率和安全性。

![](images/6b8f9d3fbd7e120355834994785213167a3097cdcde840307b2aaf48bcb8d504.jpg)  
上图：AFSIM 认知模型，包括 SA处理器和高级行为树（ABTs）

下图展示了 Endsley 的情境感知模型。SA 处理器与感知、理解和预测的概念密切相关。

![](images/db9226e8dbfeb8c867180d67f73d3e03d71a1e0fb3a8555ea6751c7a39ae5472.jpg)

Above: Endsley’s Model of Situational Awareness, Endsley et al (2000), drawn by Dr. Peter

以下表格定义了文档中使用的空对空作战相关概念的常用技术术语。

<table><tr><td>bogie</td><td>A perceived entity (unknown) that has yet to be identified as a bandit, friendly, or neutral</td></tr><tr><td>bandit</td><td>A perceived entity that is known to be an enemy</td></tr><tr><td>friendly</td><td>A perceived entity that is known to be friendly</td></tr><tr><td>neutral</td><td>A perceived entity that is known to be neutral (often a non-combatant)</td></tr><tr><td>asset</td><td>Another term for “friendly”. This term is typically used to denote friendly forces that could provide support</td></tr><tr><td>threat</td><td>A bandit/bogie that has been prioritized by threat scoring and maintained in a prioritized/ordered list</td></tr><tr><td>target</td><td>A bandit/bogie that has been prioritized by target scoring and maintained in a prioritized/ordered list</td></tr></table>

# 可视化工具 Visualization Tools

有几种可视化工具可以支持 WSF_SA_PROCESSOR，其中包括 Air Combat EngagementSummary(ACES)Display（参见：错误！未定义书签。错误！未定义书签。）。这些工具通过提供空战交战的视觉总结，帮助用户评估和解释空战场景的各个方面。ACESDisplay 旨在通过可视化关键数据和指标来增强态势感知。

![](images/437354a0bc2592f3404f16ba791e11e13488c5c8fe6e9648101bea34f39e4bb7.jpg)

Air Combat Engagement Summary (ACES) Display 旨在提供一个集成显示界面，为包含WSF_SA_PROCESSOR 的平台提供多组空战数据。这个显示界面是可重新配置的，包含以下内容：

Tactical Situation Display（战术态势显示）

Stores Management System（储存管理系统）  
Tactical Warning System（战术警告系统）  
Engine Systems（引擎系统）  
Fuel Systems（燃料系统）

此外，Situation Awareness Display（态势感知显示）展示了多种数据，包括：

感知到的友军（Assets）、未知机（Bogies）和敌机（Bandits）  
优先排序的威胁（Prioritized Threats）  
优先排序的目标（Prioritized Targets）  
感知到的群体（Perceived Groups）

模拟中平台的“真实”位置

该显示器允许用户快速在感知的“图景”和世界的真实状态之间切换。

这些功能使得 ACESDisplay成为一个强大的工具，帮助用户在复杂的空战环境中保持高效的态势感知和决策能力。如果你有更多问题或需要进一步的信息，请随时告诉我！

# 头上显 Head Up View

![](images/5920ad2087b89b738a6fc9f15b9af0fea957a33c0ddd2e4702c12c3e6d67a4e6.jpg)

这是一个带有通用平视显示器（HUD）的窗口外（OTW）视图。

# 空战可视化-地图显示 Air Combat Visualization - Map Display

![](images/79cf651db091e2e01ed6827915967e2b2462f5eb1b7a82d6cc512ae443884eea.jpg)

这是一个用于 Map Display（地图显示）的可视化项目集合，包括：

DataRings（数据环）：提供了一种以简洁方式显示标准化数据的方法。  
DataAccents（数据强调）：提供了另一种以简洁方式显示离散、基于状态的数据的方法。  
StateData（状态数据）：顶级状态数据的摘要。

□ 显示方式类似于空中交通管制屏幕。

□ 一目了然地提供高度、垂直速度、空速、马赫数、过载（g-load）和攻角（angleof attack）。

Engagement Lines（交战线）：提供了典型 AFSIM 轨迹线的替代方案。

□ 显示两个（或更多）平台之间的探测和武器有效区（WEZ）数据。

这些可视化项目旨在通过简洁和直观的方式展示复杂的数据，帮助用户更好地理解和分析地图上的信息。如果你有更多问题或需要进一步的信息，请随时告诉我！

# 空战可视化-空战 Overlays（跟踪视图）Air Combat Visualization - Air Combat Overlays (TetherView)

![](images/d2c7ab56713a1c591a5b455a9abfba7adaaa03315bd67218e15d2c4025da3b29.jpg)

这是使用系绳显示覆盖的交战数据摘要，提供以下信息：

焦点飞机与目标/威胁飞机的交战数据（左下角）  
焦点目标/威胁与焦点飞机的交战数据（右下角）  
焦点飞机的运动状态数据（左上角）  
焦点飞机的燃料状态数据（左上角）  
焦点飞机的战术数据摘要，包括武器状态（右上角）

这些信息通过直观的界面展示，帮助用户快速理解和分析交战情况。

# 更新间隔命令 Update Interval Commands

SAProcessor 具有多项职责，可以以不同的速率执行。这些速率可以设置初始值，并且可以通过脚本在模拟过程中进行更改。

某些速率仅决定数据通过事件管道发送的频率，这些速率以后缀 data_update_interval

表示。

其他速率决定信息在内部处理的频率，这些速率以后缀 calculation_update_interval 表示。

更新只能在处理器本身更新时发生（其更新速率由 update_interval 设置）。因此，最佳实践是确保以下更新间隔都是 update_interval 的倍数。

警告：本节中的所有更新间隔设置将四舍五入到 update_interval 值的最近倍数。为了防止四舍五入为零，小于 update_interval/2 的正设置将四舍五入为 asset_perception；然而，值为零可以用于禁用特定的更新类型。

report_interval <time-value>：指定报告资产状态数据的更新间隔。

默认值：0 秒（不发送数据）

engagement_data_update_interval <time-value> ： 指 定 报 告 交 战 数 据 的 更 新 间 隔（MsgSA_EngagementSummaryData 消息）。

默认值：0 秒（不发送数据）

flight_data_update_interval <time-value> ： 指 定 报 告 飞 行 数 据 的 更 新 间 隔（MsgSA_FlightKinematicsData 消息）。

默认值：0 秒（不发送数据）

fuel_data_update_interval <time-value>：指定报告燃料数据的更新间隔（MsgSA_FuelData消息）。

默认值：0 秒（不发送数据）

nav_data_update_interval <time-value>：指定报告导航数据的更新间隔（MsgSA_NavData消息）。

默认值：0 秒（不发送数据）

flight_controls_data_update_interval <time-value> ： 指 定 报 告 控 制 数 据 的 更 新 间 隔（MsgSA_FlightControlsData 消息）。

默认值：0 秒（不发送数据）

weapons_data_update_interval <time-value> ： 指 定 报 告 武 器 数 据 的 更 新 间 隔（MsgSA_WeaponsData 消息）。

默认值：0 秒（不发送数据）

track_data_update_interval <time-value> ： 指 定 报 告 轨 迹 数 据 的 更 新 间 隔（MsgSA_TrackData 消息）。

默认值：0 秒（不发送数据）

asset_data_update_interval <time-value> ： 指 定 报 告 资 产 数 据 的 更 新 间 隔（MsgSA_PerceivedAssetsData 消息）。

默认值：0 秒（无延迟间隔，使用当前真实或接收到的资产消息；参见 asset_perception）

asset_purge_lifetime <time-value>：指定缺乏更新的资产的最大生命周期。如果资产在指定的生命周期限制内没有更新，将自动清除。

默认值：默认值取决于是否指定了 asset_update_interval。如果指定，默认清除生命周期为asset_update_interval 的 2.5 倍。如果未指定，默认值为 5 秒。

perceived_item_data_update_interval <time-value>：指定报告未知机、敌机和群体数据的更新间隔（MsgSA_PerceivedBogiesAndBanditsData 和 MsgSA_GroupsData 消息）。

默认值：0 秒（不发送数据）

prioritized_item_data_update_interval <time-value>：指定报告优先威胁数据的更新间隔（MsgSA_PrioritizedThreatsAndTargetsData 消息）。

默认值：0 秒（不发送数据）

perceived_item_calculation_update_interval <time-value>：指定计算未知机、敌机和群体数据的更新间隔。

默认值：0 秒（不计算数据）

prioritized_item_calculation_update_interval <time-value>：指定计算优先威胁数据的更新间隔。

默认值：0 秒（不计算数据）

behavior_calculation_update_interval <time-value> ： SA Processor 的 独 特 之 处 在 于WsfAdvancedBehaviorTrees 和 WsfStateMachines 的更新速率可以选择性地与处理器的更新速率分开设置。因此，默认值为 0 意味着它将以与处理器相同的速率更新，而不是从不更新。

默认值：0 秒（每当处理器本身更新时更新）

# 更新间隔组命令 Update Interval Group Commands

某些更新间隔命令可以在预定义的组内设置为一个通用值：cognitive_update_interval、platform_update_interval 和 universal_update_interval。

注意：只有数据更新间隔可以这样设置。计算更新间隔必须单独设置。

cognitive_update_interval <time-value>：通过此命令将以下更新间隔命令组设置为一个通用值：

▫ asset_data_update_interval   
□ perceived_item_data_update_interval   
□ engagement_data_update_interval   
□ prioritized_item_data_update_interval

platform_update_interval <time-value>：通过此命令将以下更新间隔命令组设置为一个通用值：

□ flight_controls_data_update_interval   
□ flight_data_update_interval   
fuel_data_update_interval   
□ nav_data_update_interval   
□ report_interval   
▫ track_data_update_interval   
□ weapons_data_update_interval

universal_update_interval <time-value>：通过此命令将所有更新间隔命令设置为一个通用值（不包括 asset_purge_lifetime 和所有计算更新间隔命令）。

# 敌友类型 Enemy/Friendly Types

WSF_SA_PROCESSOR 支持使用多种技术来确定 WsfSA_EntityPerception 是否被感知为友方、敌方、中立或未知。以下命令允许基于平台的阵营、平台类型以及是否应使用 IFF 进行感知。此外，可以指定导弹类型，如果平台类型用于感知，它也可能被感知为导弹，而不是默认的飞机。如果平台是导弹类别，WsfSA_EntityPerception 也可能被感知为导弹。

enemy_side <string>：指定敌方的阵营名称。如果轨迹具有与 enemy_side 相同的阵营标识，则该轨迹被视为敌机。注意，多个条目允许多个阵营为敌方。  
friendly_side <string>：指定友方的阵营名称。如果轨迹具有与 friendly_side 相同的阵营标识，则该轨迹被视为友机。注意，多个条目允许多个阵营为友方。此外，包含 SA

Processor 的平台的同一侧始终被视为友方，即使没有以这种方式指定。

neutral_side <string>：指定中立方的阵营名称。如果轨迹具有与 neutral_side 相同的阵营标识，则该轨迹被视为中立。注意，多个条目允许多个阵营为中立。  
enemy_type <string>：将敌方类型添加到已知敌方类型列表中。如果轨迹具有与enemy_type 相同的类型标识，则该轨迹被视为敌机。注意，类型不一定必须是平台类型，它也可能是传感器类型，因为某些传感器将报告传感器类型而不是平台类型。  
friendly_type <string>：将友方类型添加到已知友方类型列表中。如果轨迹具有与friendly_type 相同的类型标识，则该轨迹被视为友机。注意，类型不一定必须是平台类型，它也可能是传感器类型，因为某些传感器将报告传感器类型而不是平台类型。  
neutral_type <string>：将中立类型添加到已知中立类型列表中。如果轨迹具有与neutral_type 相同的类型标识，则该轨迹被视为中立。注意，类型不一定必须是平台类型，它也可能是传感器类型，因为某些传感器将报告传感器类型而不是平台类型。  
missile_type <string>：将导弹类型添加到已知导弹类型列表中。如果轨迹具有与missile_type 相同的类型标识，则该轨迹被视为导弹。注意，类型不一定必须是平台类型，它也可能是传感器类型，因为某些传感器将报告传感器类型而不是平台类型。  
asset_ignore <category-name>：将平台类别添加到将在 ACES Display 上忽略的资产列表中。  
filter_assets_from_tracks <boolean-value>：如果为真，资产/友方将从轨迹列表中过滤。 默认值：true   
use_iff_id <boolean-value>：如果为真，则在确定识别时包括使用 IFF。使用时，必须定义 iff_mapping（参见：3.3.16.13.3.16.1 敌我映射 iff_mapping）。

默认值：false

use_simple_id_by_type <boolean-value>：如果为真，将使用简单的按类型识别方法。在这种情况下，不必使用 enemy_side、friendly_side 和 neutral_side 指定敌方、友方和中立类型列表，而是使用更简单的方法，仅在轨迹支持类型 ID 时执行按类型识别。

默认值：false

# 导弹识别过滤器 Missile Identification Filters

这些命令提供了一种识别/分类轨迹为导弹的方法。任何符合这些条件的轨迹将被视为导弹。

此外，使用在敌友类型中定义的导弹类型允许实体被感知为导弹，而不是默认的飞机。如果平台是导弹类别，WsfSA_EntityPerception 也可能被感知为导弹。

missile_speed_any_alt <speed-value>：如果轨迹的速度大于指定速度且在任何高度，它将被视为导弹/武器（而不是飞机）。  
missile_alt_any_speed <length-value>：如果轨迹的高度大于指定高度且在任何速度，它将被视为导弹/武器（而不是飞机）。  
missile_speed_with_alt <speed-value>：如果轨迹的速度大于指定速度且在（或高于）missile_alt_with_speed 中指定的高度，它将被视为导弹/武器（而不是飞机）。  
missile_alt_with_speed <length-value>：如果轨迹的高度大于指定高度且在（或高于）missile_speed_with_alt 中指定的速度，它将被视为导弹/武器（而不是飞机）。  
这些命令提供了一种从导弹考虑中过滤掉轨迹的方法。任何符合这些条件的轨迹将不被视为导弹（它们将被过滤掉）。  
missile_nose_angle <angle-value>：如果自机位于轨迹的机头角度之外，它将不被视为导弹/武器（而不是飞机）。这允许过滤掉不朝向自机的轨迹。

missile_time_to_intercept <time-value>：如果轨迹的拦截时间大于指定时间，它将不被视为导弹/武器（而不是飞机）。这允许过滤掉在指定时间内不会拦截自机的轨迹。  
missile_distance <length-value>：如果到轨迹的距离大于指定距离，它将不被视为导弹/武器（而不是飞机）。这允许过滤掉远距离的轨迹不被视为导弹。

# 范围设置 Range Settings

max_range_for_perceived_assets <length-value>：将资产包含在感知资产列表中的范围限制。如果未指定，将不使用资产的范围过滤器。  
max_range_for_perceived_bogies_and_bandits <length-value>：将未知机/敌机包含在感知未知机/敌机列表中的范围限制。如果未指定，将不使用未知机或敌机的范围过滤器。  
max_range_for_engagement_data <length-value>：报告交战数据的范围限制。如果未指定，将不对交战数据的报告使用范围过滤器。  
assumed_range_for_angle_only_targets <length-value>：仅角度轨迹的假定范围。如果未指定，仅角度轨迹的范围将假定为 $2 . 0 \mathsf { E } + 1 3$ 米，这大于地球到太阳距离的 100 倍。

默认值： $2 . 0 \mathsf { E } + 1 3$ 米

# 交战评估的过滤设置 Filter Settings for Engagement Assessment

filter_requires_same_side <boolean-value>：如果为真，过滤掉不在同一侧的平台。 默认值：false   
filter_requires_not_same_side <boolean-value>：如果为真，过滤掉在同一侧的平台。 默认值：false   
filter_requires_air_domain <boolean-value>：如果为真，过滤掉不在空域中的平台。默认值：false  
filter_requires_not_air_domain <boolean-value>：如果为真，过滤掉在空域中的平台。默认值：false  
filter_requires_land_or_surface_domain <boolean-value>：如果为真，过滤掉不在陆地或表面域中的平台。默认值：false  
filter_requires_not_subsurface_domain <boolean-value>：如果为真，过滤掉在水下域中的平台。默认值：false  
filter_requires_not_space_domain <boolean-value>：如果为真，过滤掉在太空域中的平台。

默认值：false

filter_requires_sa_processor <boolean-value>：如果为真，过滤掉缺乏 WSF_SA_PROCESSOR的平台。

这些设置和命令允许用户灵活地配置导弹识别和交战评估过程，以适应不同的战术和战略需求。

# 可选轨迹处理器 Optional Track Processors

这些可选定义用于定义轨迹处理器，以支持各种传感器系统功能。这些处理器帮助可视化工具确定哪些轨迹与特定传感器系统（如 ESM/RWR）相关联。

esm_track_processor <string>：用于 ESM/RWR 轨迹的可选轨迹处理器名称。这允许感知

与 ESM 和/或 RWR 传感器系统相关的轨迹。

mws_track_processor <string>：用于导弹警告系统（MWS）轨迹的可选轨迹处理器名称。这允许感知与 MWS 传感器系统相关的轨迹。  
radar_track_processor <string>：用于雷达轨迹的可选轨迹处理器名称。这允许感知与雷达传感器系统相关的轨迹。  
irst_track_processor <string>：用于 IRST 轨迹的可选轨迹处理器名称。这允许感知与 IRST和/或其他用于检测空中平台的红外传感器相关的轨迹。  
das_track_processor <string>：用于 DAS（分布式孔径系统）轨迹的可选轨迹处理器名称。这允许感知与 DAS 和/或其他多孔径红外/光电传感器系统相关的轨迹。  
flir_track_processor <string>：用于 FLIR 轨迹的可选轨迹处理器名称。这允许感知与 FLIR和/或其他主要用于检测地面平台的成像红外传感器系统相关的轨迹。  
eyes_track_processor <string>：用于目视（视觉）轨迹的可选轨迹处理器名称。这允许感知与任何机组人员目视（眼睛）观测相关的轨迹。  
perception_master_track_processor <string>：用于收集/协调感知轨迹的可选轨迹处理器名称。如果定义了此项，SAProcessor 在感知和评估轨迹时将使用指定的轨迹处理器。如果未指定，则使用主轨迹处理器（默认）。

# 可选 IDOptional IDs

flight_id<integer>：可选的飞行 ID（用于表示特定飞行中的飞机）。值为零表示飞机不属于任何飞行。

默认值：0

id_flag <string>：提供飞行中的 ID 的可选字符串。

默认值：null

# 燃料数据 Fuel Data

bingo_fuel <mass-value>：可选的最低燃料水平。如果未指定，则使用移动值（如果可用），否则使用零。

默认值：0

joker_fuel<mass-value>：可选的次最低燃料水平。如果未指定，则使用移动值（如果可用），否则使用零。

默认值：0

# 感知命令 Perception Commands

reports_self <boolean-value> / reporting_self <boolean-value>

指定是否报告关于该平台的资产状态消息。

默认值：true

reports_others <boolean-value> / reporting_others <boolean-value>

指定是否报告所有接收和已知的其他平台的资产状态消息。

默认值：false

asset_perception [ status_messages; truth <members> ]

□ status_messages：资产感知将利用任何接收到的 WsfSA_EntityMessage 消息。  
□ truth<members>：资产感知将遍历指挥链并使用真实数据。  
<members> 是一个以冒号分隔的列表，包括‘commander’、‘subordinates’、peers’、‘all_commanders’和/或‘all_subordinates’。

示例：

```txt
使用该平台指挥官和整个指挥链下所有下属的真实数据 asset_perception truth all_subordinates:commander
```

默认值：truth（但没有成员，因此感知为空）。

警告：目前，SAProcessor 处于“beta”版本，建议使用 truth 选项。在某些情况下，使用 status_messages 可能会导致由于清除问题而丢失一些资产。这将在未来解决。

perceive_self

将该平台包含在感知资产列表中。

默认值：false

max_threat_load <integer>

指定可以感知的未知机/敌机实体和未聚焦群体（即感知项目）的最大数量。

默认值：-1（无最大限制）

max_asset_load <integer>

指定可以感知的资产的最大数量。

默认值：-1（无最大限制）

asset_coast_time <time-value>

指定在失去轨迹后资产感知应持续的时间。

默认值：0 秒

bandit_coast_time <time-value>

指定在失去轨迹后敌机感知应持续的时间。

默认值：0 秒

bogey_coast_time <time-value>

指定在失去轨迹后未知机感知应持续的时间。

默认值：0 秒

use_simple_countermeasures <boolean-value>

如果为真，处理器将使用 num_chaff、num_flares 和 num_decoys 作为初始对抗措施数 量 。 当 调 用 WsfSA_Processor.DispenseChaff 、 WsfSA_Processor.DispenseFlare 和WsfSA_Processor.DispenseDecoy 时，这些数量将简单地递减（没有实际发射）。如果为假，处 理 器 将 使 用 在 父 平 台 上 定 义 的 WSF_CHAFF_WEAPON 、 WSF_FLARE_WEAPON 和WSF_DECOY_WEAPON 实例来建模对抗措施。

默认值：false

num_chaff <integer>

与 use_simple_countermeasures 一起使用时，指定初始箔条数量。

默认值：0

num_flares <integer>

与 use_simple_countermeasures 一起使用时，指定初始照明弹数量。

默认值：0

num_decoys <integer>

与 use_simple_countermeasures 一起使用时，指定初始诱饵数量。

默认值：0

filter_assets_from_bogies <boolean-value>

如果为真，已知资产将自动从未知机中过滤。

默认值：true

consideration_score_randomness <real>

如果设置，感知项目的考虑分数将随机增加或减少不超过该值的数量。

默认值：0.0

display_perception_delay <time-value>

指定在将新非视觉轨迹识别为可用于处理和分类的感知实体之前等待的时间。

默认值：0.0 秒

visual_perception_delay <time-value>

指定在将新视觉轨迹（即 eyes_track_processor）识别为可用于处理和分类的感知实体之前等待的时间。

默认值：0.0 秒

# 评估命令 Assessment Commands

bogie_threat_score_multiplier <real>

用于在优先威胁列表中对未知机进行评分的乘数。

默认值：1.0

bogie_target_score_multiplier <real>

用于在优先目标列表中对未知机进行评分的乘数。

默认值：1.0

ignore_bogies_when_grouping <boolean-value>

如果为真，形成群体时将不考虑未知机。

默认值：false

mission_task <string>

指定主要任务。这用于空战事件管道数据和空战可视化插件的空战覆盖显示。

默认值：[空]

max_prioritized_threats <integer>

指定优先威胁列表的数量限制。

默认值：0（无限制）

max_prioritized_targets <integer>

指定优先目标列表的数量限制。

默认值：0（无限制）

max_grouping_distance_centroid <length-value>

如果 use_centroid_grouping 为真，实体可以离群体中心的最大距离，以被视为群体的一部分。

默认值：8 海里

max_grouping_distance_neighbor <length-value>

如果 use_neighbor_grouping 为真，实体可以离群体中另一个实体的最大距离，以被视为同一群体的一部分。

默认值：4 海里

max_grouping_speed_difference <length-value>

如果 use_speed_grouping 为真，实体可以离群体中心的最大速度差异，以被视为群体的一部分。

默认值：100 节

max_grouping_heading_difference <angle-value>

如果 use_neighbor_grouping 为真，实体可以离群体中心的最大航向差异，以被视为群体的一部分。

默认值：10 度

min_group_radius <length-value>

群体的最小半径。群体半径是 min_group_radius 和群体成员与群体中心之间最大距离的最大值。

默认值：1 海里

use_centroid_grouping

指定实体是否必须在 max_grouping_distance_centroid 范围内才能被视为群体的一部分。

默认值：true

use_neighbor_grouping

指定实体是否必须在 max_grouping_distance_neighbor 范围内才能被视为群体的一部分。

默认值：true

use_speed_grouping

指定实体是否必须在 max_grouping_speed_difference 范围内才能被视为群体的一部分。仅在考虑实体加入群体时适用，而不是继续留在群体中。

默认值：true

use_heading_grouping

指定实体是否必须在 max_grouping_heading_difference 范围内才能被视为群体的一部分。仅在考虑实体加入群体时适用，而不是继续留在群体中。

默认值：true

use_type_grouping

指定实体是否必须与群体的其他成员类型相同才能被视为群体的一部分。仅在考虑实体加入群体时适用，而不是继续留在群体中。

默认值：false

ignore_missiles_as_threats <boolean>

指定在计算威胁值时是否应忽略感知的导弹实体。通常，感知的导弹被视为威胁，不会被忽略。

默认值：false

ignore_bogies_as_threats <boolean>

指定在计算威胁值时是否应忽略感知的未知机实体。通常，感知的未知机被视为威胁，不会被忽略。

默认值：false

ignore_missiles_as_targets <boolean>

指定在计算目标值时是否应忽略感知的导弹实体。通常，感知的导弹不被视为目标，会被忽略。

默认值：true

ignore_bogies_as_targets <boolean>

指定在计算目标值时是否应忽略感知的未知机实体

missile_wez_parameters … end_missile_wez_parameters

定义：用于定义武器有效区（WEZ）计算的参数。

说明：请参阅 missile_wez_parameters 以获取更多详细信息。

aircraft_signature_parameters … end_aircraft_signature_parameters

定义：用于定义飞机特征的参数。

说明：请参阅 aircraft_signature_parameters 以获取更多详细信息。

# 自定义脚本 Custom Scripts

用户可以选择通过使用“自定义脚本”来覆盖 WSF_SA_PROCESSOR 的默认行为和功能。这些脚本允许用户根据特定需求调整感知和评估过程。

可用的自定义脚本

```txt
- AssetConsiderationScoring (script)  
script double AssetConsiderationScoring(WsfSA_EntityPerception aAsset)  
end_script 
```

用于测量资产重要性的可选脚本，决定资产在感知中应被多强烈地考虑。

仅在定义了 max_asset_load 时有用，否则不需要重要性。

返回的值可以是正或负，负分的资产将被排除在考虑之外。

```txt
- BogieBanditConsiderationScoring (script)  
script double BogieBanditConsiderationScoring(WsfLocalTrack aTarget)  
end_script 
```

用于测量未知机/敌机重要性的可选脚本，决定它们在感知中应被多强烈地考虑。仅在定义了 max_threat_load 时有用。

返回的值可以是正或负，负分的未知机/敌机将被排除在考虑之外。

```txt
- MissileConsiderationScoring (script)  
script double MissileConsiderationScoring(WsfLocalTrack aTarget)  
end_script 
```

用于测量感知的导弹未知机/敌机重要性的可选脚本。

仅在定义了 max_threat_load 时有用。

返回的值可以是正或负，负分的导弹未知机/敌机将被排除在考虑之外。

```c
- UnfocusedGroupConsiderationScoring (script)  
script double UnfocusedGroupConsiderationScoring(WsfSA_Group aGroup)  
end_script 
```

用于测量感知的未聚焦群体重要性的可选脚本。

仅在定义了 max_threat_load 时有用。

返回的值可以是正或负，负分的群体将被排除在考虑之外。

```txt
CreatePerceivedItemPruningArray (script)  
script Array<WsfSA_PerceivedItem>  
CreatePerceivedItemPruningArray(Array<WsfSA_PerceivedItem> aThreatItems)  
end_script 
```

用于覆盖默认行为以保持感知项目数量在 max_threat_load 内的可选脚本。

返回需要删除的感知项目数组，以保持在感知项目限制内。

```txt
CalculateRisk (script) script double CalculateRisk() endScript 
```

用于计算 WSF_SA_PROCESSOR 评估的整体操作/战术风险的可选脚本。

应返回 0.0 到 1.0 之间的标准化值。

```txt
CalculateSelfRisk (script) script double CalculateSelfRisk() end_script 
```

用于计算仅考虑该平台面临的操作/战术“自我风险”的可选脚本。

应返回 0.0 到 1.0 之间的标准化值。

```txt
CalculateFlightRisk (script) 
```

```txt
script double CalculateFlightRisk() endScript 
```

这是一个可选脚本，用于计算由 WSF_SA_PROCESSOR 评估的操作/战术“飞行风险”，考虑到飞机（通常是两架或四架飞机）面临的风险。该脚本应返回一个在 0.0 到 1.0 之间的归一化值。此可选脚本将覆盖默认计算。

默认值：如果没有用户定义的脚本存在，飞行风险将被计算为在感知的 bogies 列表和bandits 列表中任何 bogie 或 bandit 所带来的最高风险。

```txt
CalculatePackageRisk (script)  
script double CalculatePackageRisk()  
end_script 
```

这是一个可选脚本，用于计算由 WSF_SA_PROCESSOR 评估的操作/战术“包风险”，考虑到飞机包（通常是多架飞机的飞行）面临的风险。该脚本应返回一个在 0.0 到 1.0 之间的归一化值。此可选脚本将覆盖默认计算。

默认值：如果没有用户定义的脚本存在，包风险将被计算为在感知的 bogies 列表和bandits 列表中任何 bogie 或 bandit 所带来的最高风险。

```txt
CalculateMissionRisk (script) script double CalculateMissionRisk() endScript 
```

这是一个可选脚本，用于计算由 WSF_SA_PROCESSOR 评估的操作/战术“任务风险”，考虑到可能阻碍当前任务成功的风险。该脚本应返回一个在 0.0 到 1.0 之间的归一化值。此可选脚本将覆盖默认计算。

默认值：如果没有用户定义的脚本存在，任务风险将被计算为在感知的 bogies 列表和bandits 列表中任何 bogie 或 bandit 所带来的最高风险。

```txt
CalculateDefensiveness (script)  
script double CalculateDefensiveness()  
end_script 
```

这是一个可选脚本，用于计算平台对当前操作/战术情况的防御程度，由

WSF_SA_PROCESSOR 评估。该脚本应返回一个在 0.0 到 1.0 之间的归一化值。此可选脚本将覆盖默认计算。

默认值：如果没有用户定义的脚本存在，防御性将被计算为任何 bogie或 bandit 所带来的最高防御性。

```txt
CalculateUrgency (script) script double CalculateUrgency() endScript 
```

这是一个可选脚本，用于计算由 WSF_SA_PROCESSOR 评估的操作/战术情况所施加的紧迫感。该脚本应返回一个在 0.0 到 1.0 之间的归一化值。此可选脚本将覆盖默认计算。

默认值：如果没有用户定义的脚本存在，紧迫性将被计算为任何 bogie或 bandit 所带来的最高紧迫性。

```txt
CalculateWeaponSupport (script) script bool CalculateWeaponSupport() endScript 
```

这是一个可选脚本，用于计算武器是否正在被支持（即，是否由母平台提供轨道更新信息）。如果武器正在被支持，应返回 true。对于武器支持没有默认实现，因此如果省略此函数，武器支持条件将始终为 false。

```txt
- CalculateThreatLevel (script)  
script double CalculateThreatLevel(WsfSA_EnityPerception aThreat, bool alsBogie)  
end_script 
```

这是一个可选脚本，用于计算指定的 bogie/bandit（aThreat）所呈现的威胁等级。如果威胁是 bogie，布尔值（aIsBogie）应为 true；如果是 bandit，则为 false。该脚本应返回一个在 0.0 到 1.0 之间的归一化值。此可选脚本将覆盖默认计算。

```txt
CalculateMissileThreatLevel (script)   
script double CalculateMissileThreatLevel(WsfSA_EntityPerception aThreat, bool alsBogie)   
end_script 
```

这是一个可选脚本，用于计算指定的导弹 bogie/bandit（aThreat）所呈现的威胁等级。如果威胁是 bogie，布尔值（aIsBogie）应为 true；如果是 bandit，则为 false。该脚本应返回一个在 0.0 到 1.0 之间的归一化值。此可选脚本将覆盖默认计算。此脚本与CalculateThreatLevel 一 起 使 用 ， 其 中 CalculateMissileThreatLevel 用 于 感 知 的 导 弹 ， 而CalculateThreatLevel用于飞机（甚至是尚未被感知为导弹的导弹）。

```txt
CalculateGroupThreatLevel (script)   
script double CalculateGroupThreatLevel(WsfSA_Group aThreat, bool alsBogie)   
end_script 
```

这是一个可选脚本，用于计算指定的未聚焦的 bogies/bandits 组（aThreat）所呈现的威胁等级。如果威胁是 bogie，布尔值（aIsBogie）应为 true；如果是 bandit，则为 false。该脚本应返回一个在 0.0 到 1.0 之间的归一化值。此可选脚本将覆盖默认计算。此脚本与CalculateThreatLevel 一起使用，其中 CalculateGroupThreatLevel 用于感知的未聚焦组，而CalculateThreatLevel用于飞机（甚至是尚未被感知为导弹的导弹）。

CalculateTargetValue (script)

script double CalculateTargetValue(WsfSA_EntityPerception aTarget, bool aIsBogie) end_script

这是一个可选脚本，用于计算指定的 bogie/bandit（aTarget）所提供的目标价值。如果目标是 bogie，布尔值（aIsBogie）应为 true；如果是 bandit，则为 false。该脚本应返回一个在 0.0 到 1.0 之间的归一化值。此可选脚本将覆盖默认计算。

CalculateMissileTargetValue (script)

script double CalculateMissileTargetValue(WsfSA_EntityPerception aTarget, bool aIsBogie) end_script

这是一个可选脚本，用于计算指定的导弹 bogie/bandit（aTarget）所提供的目标价值。如果目标是 bogie，布尔值（aIsBogie）应为 true；如果是 bandit，则为 false。该脚本应返回一 个 在 0.0 到 1.0 之 间 的 归 一 化 值 。 此 可选脚本将覆盖默认计算。此脚本与CalculateTargetValue 一 起 使 用 ， 其 中 CalculateMissileTargetValue 用 于 感 知 的 导 弹 ， 而CalculateTargetValue用于飞机（甚至是尚未被感知为导弹的导弹）。

CalculateGroupTargetValue (script)

script double CalculateGroupTargetValue(WsfSA_Group aTarget, bool aIsBogie) end_script

这是一个可选脚本，用于计算指定的未聚焦的 bogies/bandits 组（aTarget）所提供的目标价值。如果目标是 bogie，布尔值（aIsBogie）应为 true；如果是 bandit，则为 false。该脚本应返回一个在 0.0 到 1.0 之间的归一化值。此可选脚本将覆盖默认计算。此脚本与CalculateTargetValue 一 起 使 用 ， 其 中 CalculateGroupTargetValue 用 于 未 聚 焦 组 ， 而CalculateTargetValue用于飞机（甚至是尚未被感知为导弹的导弹）。

CalculateRiskPosedByEntity (script)

script double CalculateRiskPosedByEntity(WsfSA_EntityPerception aEntity) end_script

这是一个可选脚本，用于计算指定的 bogie/bandit 实体所带来的风险。该脚本应返回一个在 0.0 到 1.0 之间的归一化值。此可选脚本将覆盖默认计算。

CalculateDefensivenessInducedByEntity (script)

script double CalculateDefensivenessInducedByEntity(WsfSA_EntityPerception aEntity) end_script

这是一个可选脚本，用于计算指定的 bogie/bandit 实体所引发的防御程度。该脚本应返回一个在 0.0 到 1.0 之间的归一化值。此可选脚本将覆盖默认计算。

CalculateUrgencyInducedByEntity (script)

script double CalculateUrgencyInducedByEntity(WsfSA_EntityPerception aEntity) end_script

这是一个可选脚本，用于计算指定的 bogie/bandit 实体所引发的紧迫感。该脚本应返回一个在 0.0 到 1.0 之间的归一化值。此可选脚本将覆盖默认计算。

```txt
- ProjectPositionInTime (script)  
script WsfGeoPoint ProjectPositionInTime(double aSimTime, WsfSA_EntityPerception aEntity) end_script 
```

这是一个可选脚本，用于估计实体的未来位置。该脚本应返回一个有效的 WsfGeoPoint。此脚本将覆盖默认计算。

```powershell
- ProjectPositionForward (script)  
script WsfGeoPoint ProjectPositionForward(double aSimTime, WsfSA_EntityPerception aEntity) end_script 
```

这是一个可选脚本，用于估计实体在假设前进运动下的未来位置。该脚本应返回一个有效的 WsfGeoPoint。此脚本将覆盖默认计算。

```txt
- ProjectPositionLevelTurnLeft (script)  
script WsfGeoPoint ProjectPositionLevelTurnLeft(double aSimTime, WsfSA_EntityPerception aEntity, double aGees)  
end_script 
```

这是一个可选脚本，用于估计实体在假设进行恒定 g 左转时的未来位置。该脚本应返回一个有效的 WsfGeoPoint。此脚本将覆盖默认计算。

```txt
- ProjectPositionLevelTurnRight (script)  
script WsfGeoPoint ProjectPositionLevelTurnRight(double aSimTime, WsfSA_EntityPerception aEntity, double aGees)  
end_script 
```

这是一个可选脚本，用于估计实体在假设进行 g 限制的右转时的未来位置。该脚本应返回一个有效的 WsfGeoPoint。此脚本将覆盖默认计算。

```txt
- ProjectPositionTurnToHeading (script)  
script WsfGeoPoint ProjectPositionTurnToHeading(double aSimTime, WsfSA_EntityPerception aEntity, double aHeading_deg, double aGees)  
end_script 
```

这是一个可选脚本，用于估计实体在假设进行 g 限制的转向到指定航向时的未来位置。该脚本应返回一个有效的 WsfGeoPoint。此可选脚本将覆盖默认计算。

```txt
- ProjectPositionGoToPoint (script)  
script WsfGeoPoint ProjectPositionGoToPoint(double aSimTime, WsfSA_EntityPerception aEntity, WsfGeoPoint aPointOfInterest, double aGees)  
end_script 
```

这是一个可选脚本，用于估计实体在假设进行 g 限制的转向到指定位置时的未来位置。该脚本应返回一个有效的 WsfGeoPoint。此可选脚本将覆盖默认计算。

```txt
- ProjectPositionSlice (script)  
script WsfGeoPoint ProjectPositionSlice(double aSimTime, WsfSA_EntityPerception aEntity, double aRollAngle, double aGees)  
end_script 
```

这是一个可选脚本，用于估计实体在假设进行 g 限制的滚转和拉动机动离开当前航向时的未来位置。该脚本应返回一个有效的 WsfGeoPoint。此可选脚本将覆盖默认计算。

```txt
- ProjectPositionSliceToHeading (script)  
script WsfGeoPoint ProjectPositionSliceToHeading(double aSimTime, WsfSA_EntityPerception aEntity, double aHeading_deg, double aRollAngle, double aGees)  
end_script 
```

这是一个可选脚本，用于估计实体在假设进行 g 限制的滚转和拉动机动到指定航向时的未来位置。该脚本应返回一个有效的 WsfGeoPoint。此可选脚本将覆盖默认计算。

```txt
- ProjectPositionSplitS (script)  
script WsfGeoPoint ProjectPositionSplitS(double aSimTime, WsfSA_EntityPerception aEntity, double aGees)  
end_script 
```

这是一个可选脚本，用于估计实体在假设进行 g 限制的 Split-S 机动时的未来位置。该脚本应返回一个有效的 WsfGeoPoint。此可选脚本将覆盖默认计算。

# 3.3.16.1.敌我映射 iff_mapping

iffmapped side <side-name $\rightharpoondown$ ...<side-name> | [default] reports...forSide... reports...for_category... reports...by_default endSide   
end_iffmapped

概述

提供为模拟中的所有实体定义 IFF（敌我识别）报告行为的能力。

命令

side <side-name> … <side-name> | [default]

为一个或多个阵营应用 IFF 映射规则。如果指定了默认值，则 IFF 映射规则适用于所有未明确定义的阵营。

side-name

IFF 映射适用的“阵营”（“团队”或“隶属”）。可以是蓝方、红方、国家或团队名称。

reports [friend | foe | neutral]

指定要为给定阵营、类别或默认情况下报告的 IFF 状态。

for_side <side-name>

指定阵营之间的 IFF 映射。

for_category <category-name>

指定来自给定阵营的平台与来自给定类别的平台之间的 IFF 映射。

by_default

指定来自给定阵营的平台与所有未明确映射的阵营和类别之间的 IFF 映射。

IFF 映射条目的示例

在模拟中，阵营“蓝”、“绿”和除“白”以外的所有其他阵营将阵营“红”报告为敌方，将“myCategory”中的任何平台报告为友方，将所有其他阵营和类别报告为中立。阵营“白”将阵营“红”报告为友方，并将所有其他阵营和类别报告为敌方：

```txt
iffmapped   
side blue green default reports foe forSide red reports friend for_category myCategory reports neutral by_default   
end_side   
side white reports friend for side red   
end_side   
end_iffmapped 
```

这种配置允许用户灵活地定义和管理模拟中的敌我识别规则，以适应不同的战术和战略需求。

# 3.3.17. 传感器管理器 WSF_SENSORS_MANAGER

```txt
processor <name> WSF_SENSORSMANAGER  
WSFScriptPROCESSORCommands...  
ttr_tracking_mode_name <string>  
max TAR_acquisition_time <time-value>  
max_ttr_acquisition_time <time-value>  
turn_off TAR_if_noTracks <boolean-value>  
turn_off_ttr_if_noTracks <boolean-value>  
end Processor 
```

概述

WSF_SENSORS_MANAGER 是一个基于 HELIOS 的传感器管理器模型的脚本基类。它不是作为一个独立的处理器使用，而是传感器管理器模型用来提供所有传感器管理器处理器中常见的脚本功能。

脚本接口

WSF_SENSORS_MANAGER 利用通用脚本接口和 WSF_SCRIPT_PROCESSOR 的功能。

传感器管理器命令

ttr_tracking_mode_name <string>

设置 TTR 跟踪模式的名称。

默认值: ""

max_tar_acquisition_time <time-value>

TAR被允许在未找到指定目标的情况下搜索的最长时间。

默认值:60 秒

max_ttr_acquisition_time <time-value>TTR 被允许在未找到指定目标的情况下搜索的最长时间。

默认值:60 秒

turn_off_tar_if_no_tracks <boolean-value>当为 true 时，如果雷达没有分配目标，TAR 将被关闭。

默认值: False

turn_off_ttr_if_no_tracks <boolean-value>当为 true 时，如果雷达没有分配目标，TTR 将被关闭。

默认值: True

这些命令和参数允许用户配置传感器管理器的行为，以适应特定的操作需求和策略。

# 3.3.18. 简单传感器管理 WSF_SIMPLE_SENSORS_MANAGER

```txt
processor <name> WSF_SIMPLE_SENSORS managerial  
WSF_SENSORS managerial Commands ...  
end Processor 
```

概述

WSF_SIMPLE_SENSORS_MANAGER 是基于 HELIOS 的 GTISimpleSensorManager 端口的脚本类。简单传感器管理器是一个资产管理子系统，负责管理位于该单元或下属单元的某些传感器。它负责在适当的时间打开/关闭传感器，为特定目标提示传感器，取消对特定目标的提示，以及在提示的传感器无法找到所需目标时取消分配。基本上，它控制所有必要的传感器处理和任务处理。

脚本接口

WSF_SIMPLE_SENSORS_MANAGER 利用通用脚本接口和 WSF_SCRIPT_PROCESSOR 的功能。

简单传感器管理器命令

简单传感器管理器模型没有增加任何超出 WSF_SENSORS_MANAGER 基类所提供的功能。

简单传感器管理器配置

设置简单传感器管理器在单元上的方法有多种正确方式。要正确利用附加的简单传感器管理器，单元必须满足一个核心要求：单元必须能够访问完整的空中图像（即，单元必须能够存储检测到的目标的主轨迹）。如果简单传感器管理器连接到不满足此要求的单元，例如一个仅向其指挥官传播图的 TTR，那么该传感器管理器将无用。需要注意的是，这种配置不会必然导致问题，而是该传感器管理器将不会为该单元提供额外功能。

这种设计确保了传感器管理器能够有效地管理和处理传感器任务，优化资源使用并提高

操作效率。

![](images/b05a00d93a792c4635da1b0ce70f1f3dd9f1dc1b03facc68ce46ba283802176a.jpg)

当一个简单传感器管理器接收到一个任务时，会执行以下过程：

主轨迹确认：

单元确保它拥有一个引用该任务的主轨迹。传感器管理器必须有一个引用该任务的轨迹才能继续处理，因为它需要知道目标的位置。如果不知道目标的位置，传感器管理器无法通知提示的传感器在空中图像的哪个区域搜索该目标。

轨迹源/质量检查：

如果满足上述条件，引用该任务的主轨迹将被检查其轨迹源/质量。下一个为任务提示的传感器类型取决于当前的轨迹质量。轨迹质量的顺序如下：EW、TAR、TTR、TTR/A。因此，如果当前源是EW轨迹，传感器管理器尝试在目标上提示TAR。如果没有可用的TAR进行提示，则尝试TTR，依此类推。

提示传感器：

一旦确定了下一个期望的轨迹源，传感器管理器尝试为目标提示该源的传感器。某些传感器具有优先级。每当传感器被提示为目标时，如果当前关闭，它会自动打开。以下算法用于尝试定位所需类型的传感器：

优先级：首先优先考虑该任务的分配单元。如果分配单元有所需类型的传感器，则提示其定位目标。

下属检查：如果分配单元没有所需的传感器，则检查所有下属。任何拥有所需雷达且没有武器管理器的下属（或当前单元本身）被提示定位目标。在这种情况下，拥有武器管理器的下属被忽略，因为假定这些单元是武器单元，而不是严格的搜索传感器。唯一的例外是当这些单元之一实际上被分配了目标时（如上所述）。

责任管理：

如果传感器管理器能够提示雷达定位目标，该传感器管理器为该任务增加责任。因此，每当该任务再次处理时，传感器管理器检查任务的当前状态，以确定提示的传感器是否已定位目标。如果传感器已定位目标，则重复上述过程以确定是否可以提示更高质量的传感器定位目标。

监控与完成：

如果已提示最高可用质量的传感器，传感器管理器则简单地监控任务并等待任务完成。一旦任务完成，传感器管理器便移除其对该任务的责任。此时，传感器管理器确定是否是关闭最后一个为任务活动的传感器的时间。如果用户已配置传感器管理器关闭当前类型的传感器，并且传感器管理器确定没有其他活动任务当前使用该传感器，则该传感器将被关闭。

超时处理：

如果用户配置的“最大获取时间”已超过且传感器尚未定位目标，算法还会取消提示任务。如果发生这种情况，任务将被取消分配，雷达将放弃对目标的提示。

![](images/0757eec64cfd156aee895f8fa916c858fabb518fd014cb9785d4bfa814d7ef21.jpg)

如果分配任务的单元是“SAM”单元而不是“SAM2”，则将应用相同的过程，只是 SAM控制器将管理“SAM”上的 TAR和 TTR，并将独立的 TAR和 TTR 保持关闭。

注意：传感器管理器应放置在 TAR 和 TTR 之上的级别。TAR 和 TTR 雷达不应有传感器管理器。

# 3.3.19. 传感器偏转控制处理器 WSF_SENSORS_MANAGER_FOV

```txt
processor <name> WSF_SENSORS managerial FOV WSF_SIMPLE_SENSORS managerial Commands ... end Processor 
```

WSF_SENSORS_MANAGER_FOV 扩展了 WSF_SIMPLE_SENSORS_MANAGER，提供更复杂的偏转控制。在其他方面它是相同的。虽然简单的传感器管理器以未定义的顺序将 TTR 直接指向分配的目标，但传感器管理器 FOV 将 TTR 偏转到可以看到最多目标的空间区域。完整的传感器管理器 FOV 算法将在更新部分中给出。为了简洁起见，本页通常将WSF_SENSORS_MANAGER_FOV 简称为“传感器管理器”或“管理器”。

# TTR 辅助数据

传感器管理器查询从属 TTR 中定义的 aux_data 以发现额外的传感器参数。注意，这些参数不是在传感器管理器的 aux_data 中定义的，而是在 TTR 传感器中定义的。如果未指定辅助参数，则将设置为默认值。

unitary RESTING_AZIMUTH $=$ <angle-value>

当 TTR 没有更多任务时，将返回的方位角。此方位角在 TTR 的 PCS 框架中定义（因此，将此值设置为 0 度时，休息方位角直接指向传感器前方，90 度指向右侧，-90 度指向左侧，180 度指向正后方）。因为这是一个方位角，所以应在[-180,180]度范围内。

默认值:0 度

unitary COARSE_SLEW_RATE_AZIMUTH $=$ <angular-speed-value>

当 TTR 在其视野内没有目标时，TTR 在方位角上偏转的速度。

默认值: 无限大

unitary FINE_SLEW_RATE_AZIMUTH $=$ <angular-speed-value>

当 TTR 在其视野内有目标时，TTR 在方位角上偏转的速度。

默认值: 无限大

# TTR 限制

传感器管理器控制其下属 TTR 的一些方面。这包括开/关状态；方位偏转率和方位提示率；以及提示的位置/角度/目标。这些方面不应通过脚本进行修改。这样做会干扰管理器的操作，并产生奇怪的结果。管理器还要求 TTR 传感器使用默认的传感器调度程序。使用其他调度程序也会产生奇怪的结果。

传感器管理器只提示一个 TTR 传感器到一个位置，因此如果传感器有多个天线或波束，而天线/波束可以同时指向多个方向，它将无法正常工作。然而，如果多个传感器存在于同一平台上，它能够管理它们。

# 计算提示方位角

传感器管理器的主要职责是通过考虑当前的任务来计算 TTR 的指向方向。这部分将把分

配给 TTR 的任务称为目标。在计算提示方位角时，管理器考虑目标相对于传感器的方位，以及传感器当前是否正在跟踪目标。

![](images/84e2d9442ed4022a5c37711f6b8f2fe83614651cd282d0f75730238c3abb7f4d.jpg)

确定 TTR 的提示方位角涉及分析传感器周围目标的空间分布。以下是其工作原理：

楔形表示：

传感器的视野被表示为一个楔形，楔形的角度对应于传感器波束的宽度。对于雷达传感器，这通常是半功率波束宽度；对于几何传感器，它是方位视场。其他传感器类型可能会以不同的方式定义此宽度。

选择最佳楔形：

提示方位角通过识别包含最多已跟踪目标的楔形来确定。如果两个楔形包含相同数量的已跟踪目标，则选择包含更多总目标（无论是否已跟踪）的楔形。

如果两个楔形具有相同数量的目标，则选择目标组（在方位上）密集度更高的楔形。

提示 TTR：

在选定的楔形内，TTR 会被提示指向目标组的中间位置，该位置精确计算为该楔形内所有目标方位的平均值。

示例场景：

在一个场景中，目标 T3、T4 和 T5 形成了一个密集组，并在一个方位楔形内，传感器可能会优先考虑这些目标。然而，如果 TTR 已经在跟踪目标 T8 和 T9，它将保持对这些目标的关注，以避免放弃它们。

策略优势：

这种策略确保 TTR 不放弃其已经在跟踪的目标。

它优先考虑包含更多目标的组，并倾向于密集组而非稀疏组，从而优化传感器的跟踪能

力。

# 更新传感器管理器 Updating

传感器管理器由联合防空系统（IADS）指挥与控制（C2）系统定期更新。在每次更新中，除执行基础传感器管理器的常规职责外，视场（FOV）传感器管理器还对每个下属 TTR 执行额外任务。具体流程如下：

检查任务：

传感器管理器首先检查 TTR 是否有当前任务。

无任务时：

如果没有任务，管理器确保 TTR 处于关闭状态。

将 TTR 的偏转速率设置为粗略偏转速率。

然后将 TTR 提示到其休息方位。

有任务时：

如果有任务，管理器计算 TTR 的提示方位角。

将 TTR 提示到这个计算出的方位角。

视野检查：

如果提示方位角在传感器当前视野内：

管理器确保 TTR 处于开启状态。

将偏转速率设置为精细偏转速率。

如果提示方位角在当前视野外：

管理器确保 TTR 处于关闭状态。

将偏转速率设置为粗略偏转速率。

此更新过程确保 TTR 得到有效管理，通过在不需要时关闭来节约能量和资源，并在有任务时快速调整以跟踪目标。这种方法优化了传感器的操作准备和效率。

# 计算提示方位角 - 开发者指南

在 AFSIM端口中，计算提示方位角的算法与原始 HELIOS 实现有所不同。新版本更高效，并能产生更准确的结果，尽管仅从代码中可能难以理解。此部分旨在解释算法中令人困惑的部分。在此部分中，目标指的是分配给 TTR 的任务。

# 算法概述

方位窗口表示：

图像中展示了一条从-180 到 180 度的数轴，表示传感器周围的方位角。数轴上有一系列目标，用圆圈表示。中心有点的圆圈是已跟踪的目标。灰色框带有向右的箭头，表示方位视场（在前一节中称为方位楔形）；在本节余下部分中称为方位窗口，或简称为窗口。

![](images/bee1416b48e53adb73415d1daeeb5c0e874aee897d827cb66a405e1f66484b3d.jpg)

目标检测：

通过简单地遍历所有目标并检查每个目标是否在窗口的最小和最大限制内，可以轻松计算哪些目标在特定窗口内。然而，可能的窗口数量是无限的，因此检查所有窗口是不可能的。

HELIOS 通过尝试 360 个不同的窗口（每 1 度间隔）解决了这个问题。然而，这是一种昂贵的计算（除非目标数量非常大，这并不常见）。此外，考虑到 TTR 通常只有几度的视场，1 度的增量可能会引入一些显著的误差。

算法步骤：

目标按方位升序排序。

初始化窗口大小、最小索引和最大索引。

找出初始窗口中的目标。

计算窗口的左边缘和右边缘。

处理方位角的环绕（例如，超过 180 度时调整）。

计算目标进入或退出窗口的距离。

根据目标进入或退出窗口调整索引。

更新窗口位置。

计算目标数量。

```txt
// 按方位升序排序目标  
sort(target)  
windowSize = 窗口的视场  
minIndex = 0  
maxIndex = 0  
// 找出初始窗口中的目标  
WHILE maxIndex < length(target) AND targets[maxIndex].azimuth <= windowSize  
maxIndex += 1  
leftEdge = 0  
rightEdge = windowSize  
LOOP  
// 处理环绕 
```

```txt
wrappedMaxIndex = maxIndex mod length(target)  
wrappedRightEdge = rightEdge  
IF wrappedRightEdge > 180  
    wrappedRightEdge -= 360  
minTargetDistance = targets[minIndex].azimuth - leftEdge  
maxTargetDistance = targets[wrappedMaxIndex].azimuth - wrappedRightEdge  
IF maxTargetDistance >= minTargetDistance  
// 目标进入窗口  
maxIndex += 1  
slideDistance = maxTargetDistance  
ELSE  
// 目标退出窗口  
minIndex += 1  
slideDistance = minTargetDistance  
// 前进窗口  
leftEdge += slideDistance  
rightEdge = leftEdge + windowsSize  
IF leftEdge >= 180  
BREAK  
targetCount = maxIndex - minIndex 
```

算法的核心

该算法通过 minIndex（包含）和 maxIndex（不包含）变量跟踪窗口中的目标。它通过leftEdge 和 rightEdge 变量跟踪窗口的位置，分别标记窗口的最小和最大方位。目标存储在一个名为 targets 的顺序列表中。算法的主循环开始时计算窗口前进的距离，以便目标进入或退出窗口。这两个距离的最小值决定了目标计数图的下一个上升/下降边缘。如果目标进入窗口，需要增加 maxIndex；如果目标退出窗口，需要增加 minIndex。然后，窗口按最小距离前进。目标数量可以通过简单地从 maxIndex 中减去 minIndex 来计算。当窗口的左边缘超过最大可能方位时，循环结束；这意味着所有可能的方位都已检查。

完整计算旨在确定最大目标计数、最大跟踪计数和最小组稀疏性，因此实际代码中有一些额外的记录以确定这些值。然而，算法的核心内容包含在上述代码示例中。

# 3.3.20. 原子任务处理器 WSF_QUANTUM_TASKER_PROCESSOR

```txt
processor<name>WSF_QUANTUM_TASKERPROCESSOR  
WSFScriptProcessorCommands...  
processor Commands...  
Platform Part Commands...  
// Quantum Tasker Commands 
```

```txt
ignore_ally Tracks   
assetRepresentation ...   
generator ...   
evaluator ...   
allocation ...   
allocationextra.tasks ...   
allocationextra_assets ...   
reallocation_strategy ...   
updateassignments   
// Task Processor Commands   
comm_retry-seeking...   
comm_retry_interval ...   
operatings_level ...   
trackprocessor ...   
time_torecognizablemessages ...   
track_update_interval ...   
track_update_strategy ...   
show_task/messages   
show_uncompleted_tasks   
queuing_method ...   
number_of_servers ...   
end Processor 
```

WSF_QUANTUM_TASKER_PROCESSOR 提供了一种通用机制，用于发送和接收“任务分配”（可能与轨迹相关）。它提供了额外的脚本命令（例如，AssignTask 和 CancelTask，如WsfQuantumTaskerProcessor 中定义），允许任务的发送和接收。

# 操作方法

当 WSF_QUANTUM_TASKER_PROCESSOR 更新时，它执行以下基本步骤：

1. 使用资产感知: 从平台的 WSF_PERCEPTION_PROCESSOR 获取资产感知信息。  
2. 使用威胁感知: 从平台的 WSF_PERCEPTION_PROCESSOR 获取威胁感知信息。  
3. 调用生成器: 创建任务列表。  
4. 调用评估器: 为所有可能的资产-任务配对赋值。  
5. 调用分配器: 根据当前评估计算适当的分配（例如，最大利润分配）。  
6. 发送任务分配: 根据选定的重新分配策略发送任务分配（例如，静态策略不允许重新分配先前分配的任务）。

# 注意事项

如果处理器有多个 WSF_PERCEPTION_PROCESSOR，它将隐式链接到第一个附加到它的处理器。

该处理器通过与 WSF_PERCEPTION_PROCESSOR 的集成，利用平台的感知信息来优化任务分配和管理。

这种结构使得 WSF_QUANTUM_TASKER_PROCESSOR 能够在动态和复杂的环境中有效地管理任务分配，确保资源的最佳利用和任务的成功完成。

WSF_QUANTUM_TASKER_PROCESSOR 利 用 通 用 脚 本 接 口 和 WSF_SCRIPT_PROCESSOR的功能，提供了一系列命令来管理任务分配和处理。

# Quantum Tasker 命令

ignore_ally_tracks: 指示 Quantum Tasker 不应将盟友的轨迹传递给任务生成器，因此不应有与盟友轨迹相关的任务。  
asset_representation [ platform | systems | resources ]: 指示 Quantum Tasker 应如何表示资产感知对象。

□ platform: 整个平台作为一个资产。  
□ systems: 每个平台子系统作为一个独立资产。  
□ resources: 每个子系统的资源（如导弹、传感器/干扰器波束）作为可分配的独立资产。

generator [ simple_weapon | simple_jammer | simple_sensor | custom <script methodname> ]: 指定 Quantum Tasker 使用的任务生成器。

□ simple_weapon: 为每个轨迹创建武器任务。  
□ simple_jammer: 为每个轨迹创建干扰任务。  
□ simple_sensor: 为每个轨迹创建传感器任务。  
□ custom: 用户定义的脚本方法生成任务。

evaluator [ simple | distance | intercept_time | custom <script method name> ]: 指 定Quantum Tasker 使用的任务评估器。

simple: 每个配对的值为 1.0。  
□ distance: 根据资产与任务轨迹之间的反距离评估。  
□ intercept_time: 根据资产与任务轨迹的反拦截时间评估。  
□ custom: 用户定义的脚本方法评估可能的资产-任务配对。

allocator [ simple | greedy_isolated | greedy_priority | greedy_value | greedy_profit |optimal_profit | custom <script method name> ] [type <task_type>]: 指定 Quantum Tasker使用的分配算法。

□ simple: 将第一个任务分配给第一个资产，依此类推。  
□ greedy_isolated: 资产被分配其评估最佳的任务。  
□ greedy_priority: 分配剩余的最高优先级任务。  
□ greedy_value: 分配评估最高的资产-任务配对。  
□ greedy_profit: 分配利润最高的资产-任务配对。  
一 optimal_profit: 执行最大加权算法以确定最大累计利润的分配。  
□ custom: 用户定义的脚本方法分配任务。

allocator_extra_tasks: 指定用于未被主分配器分配的额外任务的分配器。

默认值: 无 - 额外任务未分配。

allocator_extra_assets: 指定用于未被主分配器分配的额外资产的分配器。

默认值: 无 - 额外资产未分配。

reallocation_strategy [ static | dynamic | response | event ]: 指示 Quantum Tasker 如何处理先前分配的任务和任务分配的变化。

□ static: 永不允许任务重新分配。  
□ dynamic: 始终允许任务重新分配。  
□ response: 仅在原始接收者拒绝或取消任务时允许重新分配。  
▫ event: 在新任务出现、资产状态改变或任务被拒绝/取消时执行完整分配。

默认值: static

update_assignments: 如果声明，每次更新时都会向所有分配的资产发送任务分配消息。默认值: 未声明

# 任务处理器命令

comm_retry_attempts <integer>: 指示重试失败通信的尝试次数。  
comm_retry_interval <time-value>: 指示重试失败通信的尝试之间的时间。  
operating_level <name> <level>: 指示操作条件或状态及其相关级别。  
track_processor <track-proc-name>: 指定 WSF_TRACK_PROCESSOR 的名称，其轨迹列表将用于评估过程。

默认值: 使用平台的主轨迹列表。

time_to_recognize_messages <time-value>: 指示识别消息所需的时间。  
track_update_interval <time-value>: 指示向受让人发送轨迹更新的时间间隔。  
track_update_strategy [ default | suppressor ]: 指示如何发送轨迹更新。  
show_task_messages: 指示与任务分配、取消和完成相关的信息应写入标准输出。  
show_uncompleted_tasks: 这是一个调试工具，指示在任务处理器销毁期间未完成任务的信息应写入标准输出。  
queuing_method [ first_in_first_out | last_in_first_out | none ]: 指定如果所有服务器都忙时如何排队传入消息。

默认值: first_in_first_out

number_of_servers [ <integer-reference> | infinite ]: 指定在任何给定时间可以“处理中”的最大消息数。

默认值: infinite

这些命令和设置使 WSF_QUANTUM_TASKER_PROCESSOR 能够在复杂的任务环境中有效地管理任务分配和处理，确保资源的最佳利用和任务的成功完成。

# 3.3.21. 任务处理器 WSF_TASK_PROCESSOR

```txt
processor <name> WSF_TASKPROCESSOR  
WSFScriptPROCESSOR Commands ...  
# Track State Controller Commands  
evaluate_candidate Tracks ...  
evaluation_interval ...  
number_of_servers ...  
show_statevaluations 
```

# Task Processor Commands   
```txt
show_state_transitions   
state<state-name> ...state definition ... on_entry ...end_on_entry on_exit ...end_on_exit next_state...end_next_state end_state time_to Evaluate ... 
```

# Script Interface   
```txt
track Processor ...  
comm Retry Attempts ...  
comm Retry_interval ...  
operating_level ...  
time_torecognize/messages ...  
track_update_interval ...  
track_update_strategy ...  
weapon_uplink_path ...  
uplink_source ...  
uplink_comm ...  
uplink_delay ...  
autoweapon_uplink ...  
autoweapon_uplinkplatform...  
uplink_send_interval ...  
show_task-messages  
show_uncompleted_tasks 
```

```txt
on_initiage ... end_on_initiage   
on_initiage2 ... end_on_initiage2   
on_update ... end_on_update   
script_variables ... endScript_variables   
script ... endScript   
... Other Script Commands ...   
script void on_task_assign(WsfTask aTask, WsfTrack aTrack) .. script commands ...   
end.Script   
script void on_task Cancel(WsfTask aTask) .. script commands ...   
end.Script 
```