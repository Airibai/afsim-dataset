<table><tr><td></td><td>注意:参见 DIS Articulation 以了解如何使用 articulation 功能。警告:根据 DIS 标准(IEEE Std 1278.1-1995 补充 SISO-REF-010-2006),afterburner 仅对空中平台类型有效。configuration 目前仅对空中平台类型实现。</td></tr><tr><td>命令</td><td>articulated_part &lt;platform-type&gt; &lt;part-name&gt; ... end-articulated_part</td></tr><tr><td>解释</td><td>关节部件块指示平台类型应向 DIS 发布关节部件。部件可以是通信、传感器或视觉部件。块中可以包含以下命令:parent &lt;parent-id&gt;:如果存在,这表示该部件应从属于另一个关节部件。部件将继续其父部件的运动。publish &lt;degree-of-freedom&gt;:发布命令指示哪些自由度将在 DIS 实体状态 PDU 中发布。可能的自由度包括:x:部件位置的 x 分量.y:部件位置的 y 分量.z:部件位置的 z 分量.x_rate:部件位置 x 分量的变化率.y_rate:部件位置 y 分量的变化率.z_rate:部件位置 z 分量的变化率。azimuth:部件 z 轴的旋转.elevation:部件 y 轴的旋转.rotation:部件 x 轴的旋转.azimuth_rate:部件 z 轴的运动速率.elevation_rate:部件 y 轴的运动速率.rotation_rate:部件 x 轴的运动速率。&lt;platform-type&gt;:将在其 DIS PDU 中包含关节的平类型名称。&lt;part-name&gt;:将在实体状态 PDU 中包含的关节部件的名称。&lt;part-id&gt;:将在实体状态 PDU 中通过 DIS 传输的部件的 ID。</td></tr><tr><td>命令</td><td>emitter_type &lt;sensor-type&gt;&lt;dis-emitter-name-enum&gt;</td></tr><tr><td>解释</td><td>指定与指定 WSF 系统(如传感器)相关联的 DIS “发射器名称”枚举。对于出站电磁发射 PDU,这定义了 PDU 中给定 WSF 发射器的“发射器名称”字段的值。对于入站 PDU,执行反向查找以确定需要提供额外特性以正确建模与外部建模发射器交互的 WSF 传感器类型。</td></tr><tr><td>命令</td><td>emitter_function &lt;sensor-type&gt;&lt;dis-emitter-function-enum&gt;</td></tr><tr><td>解释</td><td>指定与指定 WSF 系统(如传感器)相关联的 DIS “发射器功能”枚举。这仅适用于出站电磁发射 PDU。</td></tr><tr><td>命令</td><td>beam_type &lt;sensor-type&gt;&lt;sensor-mode-name&gt;&lt;sensor-beam-number&gt;&lt;dis-beam-parameter-index-value&gt;</td></tr><tr><td>解释</td><td>指定与指定 WSF 系统(如传感器)相关联的 DIS Emissions PDU “波束参数索引”值。对于出站电磁发射 PDU,这定义了 PDU 中给定 WSF 发射器波束的“波束参数索引”字段的值。对于入站 PDU,此字段目前未在 WSF 中使用。&lt;sensor-type&gt;:传感器的类型名称。&lt;sensor-mode-name&gt;:给定传感器类型的模式名称。使用“*”表示任何模式。&lt;sensor-beam-number&gt;:感兴趣的模式上的波束编号,范围为 [1, 255]。使用“*”表示任何波束。&lt;dis-beam-parameter-index-value&gt;:范围为 [1, 65534] 的“波束参数索引”字段在DIS 发射 PDU 中由 WSF 输出的分配值。</td></tr><tr><td>命令</td><td>beam_function &lt;sensor-type&gt;&lt;sensor-mode-name&gt;&lt;sensor-beam-number&gt;&lt;dis-beam-function-enum-value&gt;</td></tr><tr><td>解释</td><td>指定与指定 WSF 系统(如传感器)相关联的 DIS Emissions PDU “波束功能”值。这仅适用于出站电磁发射 PDU。&lt;sensor-type&gt;:传感器的类型名称。&lt;sensor-mode-name&gt;:给定传感器类型的模式名称。使用“*”表示任何模式。&lt;sensor-beam-number&gt;:感兴趣的模式上的波束编号,范围为 [1, 255]。使用“*”表示任何波束。&lt;dis-beam-parameter-index-value&gt;:范围为 [1, 255] 的“波束功能”字段在 DIS 发射</td></tr><tr><td></td><td>PDU中由WSF输出的值。如果用户未指定beam_function,则WSF实现允许将索引值设置为5。</td></tr><tr><td>命令</td><td>entity_id&lt;platform_name&gt;&lt;entity-number&gt;</td></tr><tr><td rowspan="2">解释</td><td>为WSF平台实例分配特定的DIS实体编号。如果未为给定平台实例指定DIS实体编号,仿真将按创建顺序自动顺序分配一个编号(参见start_entity)。平台的唯一DIS实体ID是通过组合站点、应用和实体编号的值来形成的。示例</td></tr><tr><td>site      79application      22entity_id      737-1     101entity_id      787-1     102此输入将DIS实体ID{79:22:101}分配给名为737-1的WSF平台实例,并将{79:22:102}分配给名为787-1的WSF平台实例。</td></tr><tr><td>命令</td><td>start-entity&lt;dis-entity&gt;</td></tr><tr><td rowspan="2">解释</td><td>指定起始DIS实体,范围为[0,65534]。仿真将按创建顺序依次为DIS平台表示分配DIS实体ID,从此值开始。示例</td></tr><tr><td>site      79application      22start-entity      10第一个分配了{79:22:10},后面的是{79:22:11},{79:22:12}以此类推。</td></tr></table>

# 过滤命令

这些命令用于在 DIS 环境中过滤特定的 PDU（协议数据单元）或实体。

解释

这些过滤命令允许用户在仿真中排除特定的 DIS 数据包或实体，从而减少不必要的数据处理和网络流量。这对于大型仿真尤其重要，因为它可以显著提高仿真性能和效率。

filter_out_by_site_and_app：通过指定站点和应用程序对来过滤数据包。这对于排除特定来源的数据非常有用。

ignore_kind_and_domain：通过指定实体类型的种类和域来过滤数据包。这对于排除特定类型的实体（如陆基平台）非常有用。

ignore_type：通过指定实体类型来过滤数据包。这对于排除特定型号或类型的实体（如特定型号的飞机）非常有用。

ignore_pdu_type：通过指定 PDU 类型来过滤数据包。这对于排除特定类型的操作（如停止或信号操作）非常有用。

filter_out_by_range：通过指定与平台的距离来过滤数据包。这对于排除超出特定范围的实体非常有用。

<table><tr><td>命令</td><td>filter_out_by_site_and_app</td></tr><tr><td>解释</td><td>过滤在 DIS 环境中运行时的站点和应用程序对。站点和应用程序必须成对设置。对于多个站点/应用程序对，重复整个块。示例
filter_out_by_site_and_app
ignore_site 80
ignore.application 200</td></tr><tr><td></td><td>end_filter_out_by_site_and_app</td></tr><tr><td>命令</td><td>ignore-kind_and_domain</td></tr><tr><td>解释</td><td>过滤具有给定DIS实体类型种类和域值的DIS实体状态PDU。使用此滤波器将防止在仿真中创建相应的外部平台。例如,要过滤所有来自陆基平台(种类=1;域=1)的实体状态PDU:示例ignore-kind_and_domain 1 1</td></tr><tr><td>命令</td><td>ignore_type</td></tr><tr><td>解释</td><td>过滤具有给定DIS实体类型的DIS实体状态PDU。使用此滤波器将防止在仿真中创建相应的外部平台。例如,要过滤仿真中的所有F-15E:示例ignore_type 1:2:225:1:5:5:0//参见DIS枚举文档以获取DIS实体类型列表</td></tr><tr><td>命令</td><td>ignore_pdu_type</td></tr><tr><td>解释</td><td>过滤具有给定类型的DIS PDU。例如,要过滤 Stop/Freeze 和 Signal PDU:示例ignore_pdu_type Stop/Freezeignore_pdu_type signal</td></tr><tr><td>命令</td><td>filter_out_by_range</td></tr><tr><td>解释</td><td>基于与平台的给定范围过滤DIS实体状态PDU。超出给定范围的实体将不会被添加到仿真中。可以指定多个平台。例如,要过滤所有在两个名为737_1A和737_1B的737平台60公里半径之外的所有平台:示例filter_out_by_range 737_1A 60 kmfilter_out_by_range 737_1B 60 km</td></tr></table>

# 其他命令

这些命令用于控制和调试 DIS 仿真中的各种行为和输出。

<table><tr><td>命令</td><td>debug_emission_pdu&lt;level&gt;</td></tr><tr><td>解释</td><td>指定电磁发射 PDU 的调试信息级别。默认值: 0</td></tr><tr><td>命令</td><td>enterprise entity_types to &lt;target-name&gt;enterprise emitter_types to &lt;target-name&gt;</td></tr><tr><td>解释</td><td>entity_types: 输出平台类型及其映射的实体类型列表。emitter_types: 输出传感器发射器类型及其映射的发射器类型列表。&lt;target-name&gt;: 定义输出列表的位置。如果 &lt;target-name&gt; 是 STDOUT, 则列表打印到控制台。否则,&lt;target-name&gt; 被解释为文件名并写入文件。警告: 此命令应在所有平台类型和 entity_type 命令处理之后使用。</td></tr><tr><td>命令</td><td>log_created Entities</td></tr><tr><td>解释</td><td>指定将有关 DIS 实体创建的信息写入标准输出。这对于调试非常有用。它还用于与make-entity_id_map.pl Perl 脚本(位于工具子目录下)一起创建 DIS 实体 ID 表。</td></tr><tr><td>命令</td><td>no-periodic pdus_whilepaused</td></tr><tr><td>解释</td><td>在仿真暂停时, 不发送实体状态和发射 PDU。这是默认行为。默认值: 关闭 (不发送)</td></tr><tr><td>命令</td><td>multi_thread</td></tr><tr><td>解释</td><td>创建一个独立于主线程的工作线程, 用于发送/接收 DIS PDU。在多线程帧步仿真中</td></tr><tr><td></td><td>使用此功能。此功能不适用于基于事件的仿真。</td></tr><tr><td>命令</td><td>multi_thread_sleep_time &lt;time-value&gt;</td></tr><tr><td>解释</td><td>允许用户显式设置 DIS 工作线程在不工作时的休眠时间(秒)。默认值: 0.001 秒或一毫秒</td></tr><tr><td>命令</td><td>max Allowed bad entity states &lt;integer-value&gt;</td></tr><tr><td>解释</td><td>指定在抑制来自实体的未来 PDU 之前允许的“坏” DIS 实体状态 PDU 的数量。一个坏的实体状态 PDU 包括以下一种或多种错误数据:位置低于海洋最低点速度 &gt;45 km/s加速度 &gt;10000 g默认值: 5</td></tr><tr><td>命令</td><td>send periodic pdus while paused</td></tr><tr><td>解释</td><td>在仿真暂停时,发送实体状态和发射 PDU。此更改是因为如果在指定时间内未收到状态 PDU,外部仿真允许超时并移除远程实体。默认值: 关闭(不发送)</td></tr><tr><td>命令</td><td>suppress non standard data &lt;boolean-value&gt; (deprecated)</td></tr><tr><td>解释</td><td>如果设置为 true, WSF 将仅输出标准 DIS 数据。</td></tr><tr><td>命令</td><td>suppress comm data &lt;boolean-value&gt;</td></tr><tr><td>解释</td><td>指定是否应为通信事件写入发射机、信号和接收机 PDU。如果通信 PDU 不重要,应将其设置为 true。默认值: false</td></tr><tr><td>命令</td><td>suppress emissions data &lt;boolean-value&gt;</td></tr><tr><td>解释</td><td>指定是否应为传感器事件写入发射 PDU。如果发射 PDU 不重要,应将其设置为 true。默认值: false</td></tr><tr><td>命令</td><td>use simple accelerations</td></tr><tr><td>解释</td><td>如果存在,使用简单的速率变化计算方程设置 DIS 实体状态 PDU 中的加速度字段。相关关键字可以用来设置方向速率,包括 use simple orientation rates、use body angular velocities 和 zero body angular velocities。默认情况下,如果不存在相关关键字,方向速率值将使用 use simple orientation rates 计算。要覆盖此行为,请使用相关关键字之一。v1 - v0a = -----t1 - t0此条目必须存在,以便计算并输入加速度和方向速率数据到 DIS 实体状态 PDU 中。如果省略,加速度和方向速率字段将设置为 0 。如果存在,默认行为是使用use simple orientation rates 计算方向速率。默认值: 条目省略</td></tr><tr><td>命令</td><td>use simple orientation rates</td></tr><tr><td>解释</td><td>如果存在,使用简单的速率计算设置 DIS 实体状态 PDU 中的方向速率字段。这是默认行为。如果省略条目,字段仍将使用此简单速率计算设置。要覆盖此行为,请使用关键字 use body angular velocities 或 zero body angular velocities。psi1 - psi0apsi = -----,etc...t1 - t0默认值: 条目省略</td></tr><tr><td>命令</td><td>use body angular velocities</td></tr><tr><td>解释</td><td>如果存在,使用 DIS 标准的世界到体轴计算设置 DIS 实体状态的方向速率字段。如果省略,将在 DIS 实体状态的方向速率字段中使用简单的方向速率计算。然而,如果存在,此关键字将覆盖 use simple orientation rates 和 zero body angular velocities 关键字的行为。//将世界(欧拉)角速度转换为体轴角速度(根据标准)w1 = (delta phi/dt) - ((delta yaw/dt) * sin(theta))w2 = (delta theta/dt)*cos(theta) + ((delta psi/dt)*sin(theta)*cos(theta))</td></tr><tr><td></td><td>w3 = -((delta theta/dt)*sin(phi) + ((delta psi/dt)*cos phi)*cos(theta))默认值:条目省略</td></tr><tr><td>命令</td><td>zero_body_angular_ Velocities</td></tr><tr><td>解释</td><td>如果存在,将 DIS 实体状态的方向速率字段清零。将覆盖use SIMPLE_orientationRates 计算。如果同时存在,将不会覆盖use_body_angular_ Velocities 行为。默认值:条目省略</td></tr></table>

# 外部 DIS 移动器命令

这些命令用于将外部 DIS 实体映射到 WSF 平台类型，以便在仿真中控制和监视这些外部实体。

解释

map_external_entity：此命令用于将特定的 DIS 实体 ID 映射到 WSF 平台类型。这样，外部实体可以在 WSF 仿真中作为本地平台进行控制和监视。

map_external_type：此命令用于将特定的 DIS 实体类型映射到 WSF 平台类型。这样，所有具有该 DIS 实体类型的外部实体都可以在 WSF 仿真中作为本地平台进行控制和监视。

这些命令允许用户在仿真中集成和管理外部 DIS 实体，从而增强仿真的互操作性和灵活性。

<table><tr><td>命令</td><td>map_external_entity &lt;dis-entity-id&gt;</td></tr><tr><td>解释</td><td>将传入的 DIS 实体 ID 与 DIS 实体类型到平台类型的映射进行检查。如果存在相应的平台类型,则该类型定义的所有组件将可用于外部平台。外部平台将在 WSF 内被视为本地平台,其组件可以像任何 WSF 平台一样被控制或监视。任何能够从 WSF发送 DIS PDU 的组件将发送 DIS PDU,但不发送 DIS 实体状态 PDU。PDU 将在其dis-entity-id字段中包含外部平台的实体 ID。</td></tr><tr><td>命令</td><td>map_external_type &lt;dis-entity-type&gt;</td></tr><tr><td>解释</td><td>与 map_external_entity 命令相同,但它将映射给定 DIS 实体类型的所有实体,而不是特定的 DIS 实体 ID。示例假设你有一个 DIS 实体 ID 为 1234 的外部实体,并且你希望将其映射到 WSF 平台类型 Tank,可以这样定义:map_external-entity 1234entity_type Tankend_map_external-entity如果你希望将所有类型为 1:2:225:1:5:5:0 的 DIS 实体映射到 WSF 平台类型FighterJet,可以这样定义:map_external_type 1:2:225:1:5:5:0entity_type FighterJetend_map_external_type</td></tr></table>

# 武器和电子战映射命令

这些命令用于指定在发送 PDU 时使用的 DIS 实体类型和电子战技术类型。

解释

munition_type：此命令用于指定在发送 PDU 时使用的 DIS 实体类型。它确保 WSF 平

台类型与 DIS 实体类型正确映射，以便在仿真中进行交互。

ew_technique_type：此命令用于指定与 WSF 电子战技术相关联的 DIS 干扰模式序列枚举。它确保 EW 技术在发送和接收 PDU 时正确映射。

warhead：此命令用于指定在火力和爆炸 PDU 中使用的 DIS 弹头枚举。它确保 WSF 武器类别与 DIS 弹头类型正确映射。

这些命令允许用户在仿真中准确地映射和管理武器和电子战技术，从而增强仿真的互操作性和准确性。

<table><tr><td>命令</td><td>munition_type &lt;platform_type&gt;&lt;dis-entity-type&gt;</td></tr><tr><td>解释</td><td>指定在为具有指定WSF平台类型的平台或弹药发送PDU时使用的DIS实体类型。此命令应为场景中存在的每个WSF平台类型指定。如果平台的类型没有对应的DIS实体类型,则将使用0:0:0:0:0:0。为了正确地与其他网络仿真接收到的DIS实体进行交互,必须创建一个具有定义签名的对应简单平台类型。示例entity_type F-15E 1:2:225:1:5:5:0entity_type F-18E 1:2:225:1:9:10:0注意:entity_type和munition_type是同义词。</td></tr><tr><td>命令</td><td>ew技术和technique_type&lt;ew-technique-type&gt;&lt;dis-jamming-mode-sequence-enum&gt;</td></tr><tr><td>解释</td><td>指定与指定WSF电子战(EW)技术相关联的DIS干扰模式序列枚举。对于出站电磁发射PDU,这定义了PDU中给定WSF定义的传感器/干扰器的EW技术的“干扰模式序列”字段的值。对于入站PDU,执行反向查找以确定需要由传感器/干扰器使用的WSFEW技术类型,以提供正确建模与外部建模EW技术交互所需的附加特性。如果在一个波束上使用了多种EW技术,则只会发送其中一种。目前,这仅对(电子攻击)技术有效。</td></tr><tr><td>命令</td><td>warhead &lt;category&gt;&lt;dis-warhead-enum&gt;</td></tr><tr><td>解释</td><td>指定在DIS火力和爆炸PDU的爆炸描述符字段中使用的DIS弹头枚举。此枚举映射到WSF类别。示例warhead HEL 3000 # 将武器类别HEL 映射到DIS弹头枚举3000(照明)。</td></tr></table>

# 其他武器和电子战命令

这些命令用于控制和调试武器和电子战相关的 PDU（协议数据单元）。

<table><tr><td>命令</td><td>debug_warfare_pdu&lt;level&gt;</td></tr><tr><td>解释</td><td>指定战争PDU的调试信息级别。这是一个位掩码。如果设置了位0，将在控制台上打印有关接收到的Fire和Detonate PDU的详细信息。如果设置了位1，将在控制台上打印有关武器转移的详细信息。默认值：3（Fire和武器转移信息都打印到控制台）</td></tr><tr><td>命令</td><td>simple_detonations&lt;boolean-value&gt;</td></tr><tr><td>解释</td><td>指示在接收到的Fire PDU中确定爆炸事件效果时将应用更简单的规则。如果启用此功能且simple_detonations Exclude不排除武器的简单爆炸处理，将应用以下规则：如果PDU指定了特定目标实体，并且该实体是本地控制的且未标记为不可摧毁，则如果PDU表示目标被击中（DIS结果代码为1），它将被击毁。如果未明确指定目标实体，并且PDU表示发生了击中或某种爆炸，将选择一个目标</td></tr><tr><td></td><td>(参见 targetpriority 算法),如果它与爆炸点之间的距离小于或等于simple_kill_range 的值,则将其击毁。如果 DIS 结果代码表示未发生任何爆炸(例如,代码 0、6 和 31-33),则不会击毁任何实体。默认值:开启</td></tr><tr><td>命令</td><td>simple_detonations Exclude platform_type &lt;type-name&gt;simple_detonations Exclude weapon_effects &lt;type-name&gt;</td></tr><tr><td>解释</td><td>如果启用了 simple_detonations,此命令将防止对特定武器平台类型或武器效果类型进行简单爆炸处理。如果:武器的平台类型出现在 simple_detonations Exclude platform_type 命令中。与武器平台相关联的武器效果出现在 simple_detonations Exclude weapon_effects命令中。此命令可以多次重复以构建排除列表。注意:如果相关的武器效果具有必须执行的 onweapon_target_engagement 脚本以实现所需效果(通常用于对抗措施或非致命效果建模),应使用此命令。</td></tr><tr><td>命令</td><td>simple_kill_range &lt;length-value&gt;</td></tr><tr><td>解释</td><td>如果启用了 simple_detonations 并且在接收到的 Fire PDU 中未指定目标,将选择一个目标(参见 target_priority 算法)。如果它与爆炸点之间的距离小于或等于此命令指定的值,则将其击毁。默认值:100 米</td></tr><tr><td>命令</td><td>simple_miss_reporting &lt;boolean-value&gt;</td></tr><tr><td>解释</td><td>如果为 true ,则任何未导致目标被击毁的报告爆炸将报告为 6(NoneOrNoDetonationDud)。只有当目标被击毁时,报告的爆炸结果才为 1(EntityImpact)。当某些接收应用程序对爆炸结果的处理有限时使用此功能。默认值: false</td></tr><tr><td>命令</td><td>suppress_directed_energy_data &lt;boolean-value&gt;</td></tr><tr><td>解释</td><td>定向能量数据包括新扩展 DIS 标准的一部分 PDU;这些包括定向能量火力和实体部件损坏状态 PDU。如果设置了此标志,则仅发送符合 IEEE 1278.1 DIS 标准的基本Fire 和 Detonate PDU,用于定向能量武器。默认值:启用</td></tr><tr><td>命令</td><td>suppress_cmedetect报告显示 [ &lt;boolean-value&gt;] (deprecated)</td></tr><tr><td>解释</td><td>指定电磁发射 PDU 是否不会包含指示传感器检测但尚未跟踪的目标的补充波束。CME 应用程序 VESPA 和 Clouseau 使用此功能绘制传感器和目标之间的白色检测线。默认值: true注意:补充波束指定极低功率(约 1 毫瓦),以减少对那些正在跟踪接收功率的应用程序的干扰潜力。</td></tr><tr><td>命令</td><td>suppress_cme-entity_data [&lt;boolean-value&gt;] (deprecated)</td></tr><tr><td>解释</td><td>指定是否不会发送 CME 应用程序 VESPA 和 Clouseau 的补充 DIS “其他” PDU,包含额外的实体数据。默认值:true</td></tr><tr><td>命令</td><td>suppress_cme_draw报告显示 [&lt;boolean-value&gt;] (deprecated)</td></tr><tr><td>解释</td><td>指定是否不会发送 WsfDraw DIS “其他” PDU,包含绘图命令。默认值:true</td></tr><tr><td>命令</td><td>suppress_cme Passive sensor [&lt;boolean-value&gt;] (deprecated)</td></tr><tr><td>解释</td><td>指定是否不会发送被动传感器的发射 PDU。默认值:true</td></tr><tr><td>命令</td><td>use_deprecated_cme_draw报告显示 [&lt;boolean-value] (deprecated)</td></tr><tr><td>解释</td><td>如果设置为 true,则使用已弃用的格式发送 WsfDraw DIS “其他” PDU,包含绘图命令。</td></tr><tr><td></td><td>默认值: false
注意: VESPA v5.3.2 及更早版本需要已弃用的格式。</td></tr><tr><td>命令</td><td>targetpriority &lt;platform_type&gt; &lt;real-value&gt;</td></tr><tr><td>解释</td><td>当接收到 Fire PDU 并且 PDU 中未指定目标实体时使用此命令。当 Fire PDU 中未指定目标实体时, 仿真将根据以下公式为每个本地控制的敌对实体 (那些与爆炸武器不同侧的实体) 分配优先级, 然后选择优先级最高的实体:
Priority = targetpriority - distance_from_target_location
其中 targetpriority 是相关实体的 targetpriority 值。
注意: 如果没有任何 targetpriority 命令, 此算法将简单地选择离目标位置最近的本地控制敌对实体。这通常可以正常工作, 但许多政府提供的数据库包含共址实体 (例如, SAM 站点的所有元素都共址), 选择目标可能会导致歧义, 从而导致选择错误的目标。targetpriority 命令可用于创建偏差, 以便选择高价值目标。
示例
targetpriority SAM_FC_RADAR 1000
这将导致选择类型为 SAM_FC_RADAR 的平台, 如果它们与另一个平台共址。</td></tr><tr><td>命令</td><td>use_track_jam_for_tracking_requestson&lt;boolean-value&gt;</td></tr><tr><td>解释</td><td>如果为 true, 这为接收器提供了一种近似方法来确定 AESA 波束可能指向的所有位置。由于单个 ESA 波束可以跟踪许多目标, 并且其移动速度比电磁发射 PDU 的任何合理更新速率都快, 使用标准 DIS 协议接收器无法确定波束的指向位置, 从而使高保真 ESM 模型无法确定是否可以检测到波束。
此更改修改了此类传感器的跟踪干扰列表, 使其包含传感器希望跟踪的实体 ID, 而不是实际跟踪的实体 ID。因此, 即使传感器无法检测到目标, 接收应用程序也可以确定波束的大致指向位置。
默认值: false</td></tr></table>

# 武器转移命令

这些命令用于控制武器在仿真中的转移和管理。

解释

incoming_weapon_transfer：此命令用于将外部实体发射的武器转移到本地控制。它确保 FirePDU 中指定的武器在本地进行建模和控制。

outgoing_weapon_transfer：此命令用于将本地发射的武器转移到外部控制。它确保某些外部应用程序接管发射武器的控制。

这些命令允许用户在仿真中准确地管理和转移武器，从而增强仿真的互操作性和灵活性。

<table><tr><td>命令</td><td>incomingweapon_transfer &lt;dis-entity-type&gt; [ from &lt;dis-entity-id&gt; ] using &lt;weapon-system-type&gt;</td></tr><tr><td>解释</td><td>Fire PDU 可用于表示由外部实体发射的武器将在本地进行建模(“飞行”)。如果 Fire PDU 中的 Burst Descriptor 中的 Munition 字段(以及可选的 Firing Entity ID)与 &lt;dis-entity-type&gt; 和 &lt;dis-entity-id&gt; 值分别匹配,则武器实体将在 Fire PDU 中被转移到本地控制。如果匹配,将从类型为 &lt;weapon-system-type&gt; 的武器系统发射武器,以建模武器的飞行。如果提供了 &lt;dis-entity-id&gt;,则指定为 0 的组件将被视为“通配符”,并将匹配该组件的任何传入值。注意: &lt;weapon-system-type&gt; 应为使用 weapon 命令定义的武器系统类型的名称,而不是发射平台类型的名称。</td></tr><tr><td>命令</td><td>outgoingweapon_transfer &lt;weapon-system-type&gt;</td></tr><tr><td>解释</td><td>指定从指示的武器系统发射的武器将被转移到外部控制。某些外部应用程序预计会</td></tr><tr><td></td><td>响应 Fire PDU 并接管发射武器的控制。
注意: &lt;weapon-system-type&gt; 应为使用 weapon 命令定义的武器系统类型的名称,而不是发射平台类型的名称。
示例
假设你有一个外部实体类型为 1:2:225:1:5:5:0 的武器,并且希望将其转移到本地控制,可以这样定义:
incoming weaponry_transfer 1:2:225:1:5:5:0 using MissileSystem
如果你希望将从类型为 MissileSystem 的武器系统发射的武器转移到外部控制,可以这样定义:
outgoing weaponry_transfer MissileSystem</td></tr></table>

# 4.3. 全局仿真控制命令 Simulation Control Commands

# 4.4. 装备目标特性 signature

# 4.4.1. 声学特性 acoustic_signature

```txt
acoustic_signature <signature-name> data_reference_range <length-value> state <state-name> | default spectrum_data freq <frequency-value> noise_pressure <noise-pressure-value> freq <frequency-value> noise_pressure <noise-pressure-value> ... end_spectrum_data state ... end_acoustic_signature 
```

acoustic_signature 用于定义一个平台类型的声学特征。当声学传感器尝试检测一个平台时会使用这个特征。声学特征由一个或多个表组成，每个表定义平台处于特定“状态”时的特征。“状态”表示一种条件，比如“起落架放下”。

解释

这个描述定义了如何在 AFSIM 中为一个平台创建声学特征。每个特征都有一个唯一的名字，可以包含多个状态，每个状态都有一系列频率和相应的噪声压力值。通过这些定义，可以模拟在不同状态下的平台声学特征，比如飞行时、起落架放下时等。

这种细化的声学建模对于在仿真中准确检测和识别平台非常重要，因为不同状态下的平台可能会发出不同的声学信号。

<table><tr><td>命令</td><td>data_reference_range &lt;length-value&gt;</td></tr><tr><td>解释</td><td>计算或测量以下声学数据时使用的参考范围值。此值用于将以下声学数据调整到零斜距值。</td></tr><tr><td>命令</td><td>state [ &lt;state-name&gt; | default ]</td></tr><tr><td>解释</td><td>指示当平台处于签名状态 &lt;state-name&gt;时，以下表定义将被使用。如果指定为 default，那么如果平台处于未匹配任何定义状态的签名状态时，将使用后续表。
如果未指定 state 命令，则签名将有一个适用于所有签名状态的签名表。</td></tr><tr><td>命令</td><td>freq &lt;frequency-value&gt;</td></tr><tr><td>解释</td><td>签名值的 1/3 倍频程中心频率。
注意：在单个状态内，这些频率值必须按递增顺序出现。</td></tr><tr><td>命令</td><td>noise_pressure &lt;noise-pressure-value&gt;</td></tr><tr><td>解释</td><td>在指定的 1/3 倍频程中心频率下的声噪声压力（dB/20 uPa）。</td></tr></table>

# 4.4.1.1. 多声学特性 WSF_MULTIRESOLUTION_ACOUSTIC_SIGNATURE

```txt
multiresolution_acoustic_signature WSF MultiresOLUTION_ACOUTIC_SIGNATURE ... multiresolution_acoustic_signature ... endMULTIRESOLUTION_acoustic_signature 
```

概述

multiresolution_acoustic_signature 定义了一个容器，用于在平台上保存一个或多个acoustic_signature 对 象 ， 并 将 选 择 使 用 哪 个 acoustic_signature 推 迟 到 运 行 时 。 选 择acoustic_signature 是 通 过 与 组 件 关 联 的 fidelity 参 数 来 完 成 的 。 容 器 中 定 义 的 每 个acoustic_signature 模型都分配了一个 fidelity_range，在初始化期间根据匹配的 fidelity 设置平台上的 acoustic_signature。

使用方法

定 义 新 类 型 : 可 以 在 platform 或 platform_type 命 令 之 外 使 用multiresolution_acoustic_signature 来定义新类型。

```txt
multiresolution_acoustic_signature <derived> WSF MultiresOLUTION_ACOUSTIC_SIGNATURE 
```

```txt
fidelity <real-value>   
[add | edit] model <string-value> fidelity_range <real-value> <real-value> [default] acoustic_signature [<acoustic_signature-type>] ... acoustic_signature ... end_acoustic_signature end_model   
[add | edit] model <string-value> ... Any number of models may be specified ... end_model   
common ... acoustic_signature ... end_common   
endMULTIRESOLUTION_acoustic_signature 
```

实 例 化 对 象 : 可 以 在 platform_type 或 platform 实 例 上 实 例 化 一 个multiresolution_acoustic_signature 对象。

```txt
platform_type ...
multiresolution_acoustic_signature <type>
    ... multiresolution_acoustic_signature commands ...
endMULTIRESOLUTION_ACQUISCSignatures 
```

```txt
platform ...
    add multiresolution_acoustic_signature <type>
        ... multiresolution_acoustic_signature commands ...
    endMULTIRESOLUTION_ACQUSTIC_SIGNATURE
endplatform 
```

修改现有对象: 可以在 platform 实例上修改现有的 multiresolution_acoustic_signature 对象。

命令

fidelity <real-value>: 定义组件的 fidelity 值，决定在运行时使用哪个 acoustic_signature。必须在 0 到 1 之间（包括 0 和 1）。此值直接映射到模型命令中定义的 fidelity_range。默认值: 1.0  
model <string-value> ... end_model: 定义或编辑包含的 acoustic_signature 模型，名称由字符串给出。支持隐式添加（或编辑如果命名模型存在）以及使用 add 和 edit 命令的显式添加和编辑。

注意: 必须至少指定一个模型块。

fidelity_range <real-value> <real-value>: 定义此模型应使用的 fidelity 值范围。必须在 0到 1 之间（包括 0 和 1），按递增顺序排列，并且不得与此组件上的另一个模型的fidelity_range 重叠。

默认值: 0.0 1.0

default: 如果没有匹配的 fidelity，则使用此模型作为默认选择。  
acoustic_signature <acoustic_signature-type> ... end_acoustic_signature: 定 义acoustic_signature模型的类型和特定于此模型实例化的参数。在首次定义新模型时需要acoustic_signature，在编辑现有模型时不得指定。  
common ... end_common: 定义要转发到所有当前指定的 acoustic_signature 模型的通用参数。这些参数必须对所有当前定义的 acoustic_signature模型有效。

说明

多分辨率分析: 这种方法允许在不同的分辨率下分析和选择合适的 acoustic_signature模型，以便在不同的场景中优化性能。  
未来改进: 计划在场景文件的其他位置提供 fidelity 选择，以提高此组件的实用性。

这种结构允许用户在 AFSIM 中灵活地定义和管理平台的声学特征，从而更好地模拟和分析不同条件下的声学响应。

# 4.4.2. 红外特性 infrared_signature

```txt
infrared_signature <signature-name> (model-name) 
```

```txt
... model specific commands ... end_infrared_signature 
```

在 AFSIM （ Advanced Framework for Simulation, Integration, and Modeling ） 中 ，infrared_signature用于定义一个平台类型的红外特征。当红外传感器试图检测某个平台时，这个红外特征会被使用。

以下是 infrared_signature 的定义格式：

```txt
infrared signature <特征名称>(模型名称)
```

... 模型特定的命令 ...

```txt
end_infrared_signature 
```

目前红外特征模型当前仅有一个 WSF_INFRARED_SIGNATURE，其模型特定的命令也都是它的命令。

# 4.4.2.1. 红外特性模型 WSF_INFRARED_SIGNATURE

```txt
infrared signature <signature-name> (WSF_INFRARED_SIGNATURE) interpolate_tables <boolean-value> interpolation_type [linear | logarithmic] state <state-name> | default band [short | medium | long | very_long | default] ... Azimuth-Elevation Table Definition ... band ... ... Azimuth-Elevation Table Definition ... state ... end_infrared_signature 
```

WSF_INFRARED_SIGNATURE 提供了 infrared_signature 的标准实现，如果用户没有指定不同的实现模型，则使用此模型。该模型将特征实现为一个或多个表集，这些表集在平台处于特定“状态”时适用。“状态”表示一种条件，例如“舱门打开”。

表中的因变量单位应为辐射强度单位（W/sr）。

<table><tr><td>命令</td><td>interpolate_tables&lt;boolean-value&gt;</td></tr><tr><td>解释</td><td>指定是否对定义的方位角-仰角表进行插值。插值类型可以是线性或对数（参见 interpolation_type）。默认值：true</td></tr><tr><td>命令</td><td>interpolation_type&lt;linear | logarithmic&gt;</td></tr><tr><td>解释</td><td>指定在方位角-仰角表中插值数据时使用线性或对数插值。默认值：linear</td></tr><tr><td>命令</td><td>state&lt;state-name&gt;</td></tr><tr><td>解释</td><td>表示当平台处于特征状态&lt;state-name&gt;时，将使用以下表定义。如果&lt;state-name&gt;是默认值，则在平台处于未匹配任何定义状态时使用后续表。如果未指定状态命令，则特征具有一个适用于所有特征状态的特征表。</td></tr><tr><td>命令</td><td>band [short | medium | long | very_long | default]</td></tr><tr><td>解释</td><td>表示当感应红外传感器在指定波段操作时，将使用以下表。波段定义如下：short:1到3微米medium:3到8微米（通常为3到5微米）long:8到14微米very_long:14微米及以上每个状态必须定义每个波段或定义一个默认波段。</td></tr></table>

# 示例

使用一个名为 cueball 的常量特征，适用于所有状态和波段：

```txt
infrared_signature cueball constant 10 w/sr end_infrared_signature 
```

使用默认情况下依赖波段的特征，并在舱门打开时使用固定特征：

```tcl
infrared signature dummy  
state default  
band medium  
constant 10 w/sr  
band default  
constant 20 w/sr  
state bays_open  
constant 30 w/sr  
end_infrared_signature 
```

# 4.4.2.2. 多红外特性模型 WSF_MULTIRESOLUTION_INFRARED_SIGNATURE

```txt
multiresolution_infrared_signature WSF MultiresOLUTION_INFRARED_SIGNATURE ... multiresolution_infrared_signature ...   
endMULTIRESOLUTION_INFRARED_SIGNATURE 
```

multiresolution_infrared_signature 是 一 个 容 器 ， 用 于 在 平 台 上 保 存 一 个 或 多 个infrared_signature 对 象 ， 并 将 选 择 使 用 哪 个 infrared_signature 推 迟 到 运 行 时 。 选 择infrared_signature 是 通 过 与 组 件 关 联 的 fidelity 参 数 来 完 成 的 。 容 器 中 定 义 的 每 个infrared_signature 模型都分配了一个 fidelity_range，在初始化期间根据匹配的 fidelity 设置平台上的 infrared_signature。

# 使用方法

定 义 新 类 型 : 可 以 在 platform 或 platform_type 命 令 之 外 使 用multiresolution_infrared_signature 来定义新类型。

```txt
multiresolution_infrared_signature <derived> WSF MultiresOLUTION_INFRARED_SIGNATURE 
```

```txt
fidelity <real-value>   
[add | edit] model string-value> fidelity_range <real-value> <real-value> [default] infrared_signature [<infrared_signature-type>] ... infrared_signature ... end_infrared_signature   
end_model   
[add | edit] model string-value> ... Any number of models may be specified ... 
```

```txt
end_model   
common ...infrared_signature... end_common   
endMULTIRESOLUTION_INFRAD_signature 
```

实 例 化 对 象 : 可 以 在 platform_type 或 platform 实 例 上 实 例 化 一 个multiresolution_infrared_signature 对象。

```fortran
platform_type ...
multiresolution_infrared_signature <type>
    ... multiresolution_infrared_signature commands ...
endMULTIRESOLUTION_INFRADED_SIGNA
endPLATFORM_TYPE 
```

```txt
platform ...
    add multiresolution_infrared_signature <type>
        ... multiresolution_infrared_signature commands ...
    endMULTIRESOLUTION_INFRARED_SIGNATURE
endplatform 
```

修改现有对象: 可以在 platform 实例上修改现有的 multiresolution_infrared_signature 对象。

```matlab
platform ...
    edit multiresolution_infrared_signature <type>
        ... multiresolution_infrared_signature commands ...
    endMULTIRESOLUTION_INFRAD_signature
endplatform 
```

# 命令

fidelity <real-value>: 定义组件的 fidelity 值，决定在运行时使用哪个 infrared_signature。必须在 0 到 1 之间（包括 0 和 1）。此值直接映射到模型命令中定义的 fidelity_range。默认值: 1.0  
model <string-value> ... end_model: 定义或编辑包含的 infrared_signature 模型，名称由字符串给出。支持隐式添加（或编辑如果命名模型存在）以及使用 add 和 edit 命令的显式添加和编辑。

注意: 必须至少指定一个模型块。

fidelity_range <real-value> <real-value>: 定义此模型应使用的 fidelity 值范围。必须在 0到 1 之间（包括 0 和 1），按递增顺序排列，并且不得与此组件上的另一个模型的fidelity_range 重叠。

默认值: 0.0 1.0

default: 如果没有匹配的 fidelity，则使用此模型作为默认选择。  
infrared_signature <infrared_signature-type> ... end_infrared_signature: 定 义infrared_signature模型的类型和特定于此模型实例化的参数。在首次定义新模型时需要

infrared_signature，在编辑现有模型时不得指定。

common ... end_common: 定义要转发到所有当前指定的 infrared_signature 模型的通用参数。这些参数必须对所有当前定义的 infrared_signature模型有效。

# 说明

多分辨率分析: 这种方法允许在不同的分辨率下分析和选择合适的infrared_signature模型，以便在不同的场景中优化性能。  
未来改进: 计划在场景文件的其他位置提供 fidelity 选择，以提高此组件的实用性。

这种结构允许用户在 AFSIM 中灵活地定义和管理平台的红外特征，从而更好地模拟和分析不同条件下的红外响应。

# 4.4.3. 光学反射率 optical_reflectivity

```txt
optical_reflectivity <signature-name> (model-name) ... model specific commands ... end_optical_reflectivity 
```

# 概述

optical_reflectivity 定义了给定平台类型反射光学信号的程度。当光学传感器试图检测平台时，会使用该反射率。

<signature-name> 是给这个特征指定的名称。如果名称指定了一个已存在的定义，那么新的定义将取代当前的定义（即最后一次出现的定义将被用于模拟中）。

(model-name) 是一个可选参数，指定用于定义特征的实现模型。可用的模型有：

WSF_OPTICAL_REFLECTIVITY - 使用方位角/仰角表格来定义特征。如果没有显式选择模型，这是默认模型。

# 4.4.3.1. 光学反射率模型 WSF_OPTICAL_REFLECTIVITY

```txt
optical_reflectivity <signature-name> (WSF_OPTICAL_REFLECTIVITY) interpolate_tables <boolean-value> interpolation_type [linear | logarithmic] state <state-name> | default ... Azimuth-Elevation Table Definition ... state ... end_optical_reflectivity 
```

WSF_OPTICAL_REFLECTIVITY 提供了 optical_reflectivity 的标准实现，如果用户没有指定不同的实现模型，则使用此模型。方位角-仰角表中的因变量是无单位的反射率。

<signature-name> 是给这个特征指定的名称。如果名称指定了一个已存在的定义，那么新的定义将取代当前的定义（即最后一次出现的定义将被用于模拟中）。

<table><tr><td>命令</td><td>interpolate_tables &lt;boolean-value&gt;</td></tr><tr><td>解释</td><td>指定是否对定义的方位角-仰角表进行插值。插值类型可以是线性或对数（参见 interpolation_type）。默认值：true</td></tr><tr><td>命令</td><td>interpolation_type &lt;linear | logarithmic&gt;</td></tr><tr><td>解释</td><td>指定在方位角-仰角表中插值数据时使用线性或对数插值。默认值：linear</td></tr><tr><td>命令</td><td>state &lt;state-name&gt;</td></tr><tr><td>解释</td><td>表示当平台处于特征状态 &lt;state-name&gt;时，将使用以下表定义。如果指定为 default，则在平台处于未匹配任何定义状态时使用后续表。
如果未指定状态命令，则特征具有一个适用于所有特征状态的特征表。</td></tr></table>

# 4.4.4. 光学特性 optical_signature

```txt
optical_signature <signature-name> (model-name) ... model specific commands ... end_optical_signature 
```

概述

optical_signature 定义了一个平台类型的光学特征。当传感器试图检测平台并需要平台在传感器方向上的投影面积时，会使用光学特征。

<signature-name> 是给这个特征指定的名称。如果名称指定了一个已存在的定义，那么新的定义将取代当前的定义（即最后一次出现的定义将被用于模拟中）。

(model-name) 是一个可选参数，指定用于定义特征的实现模型。可用的模型有：

• WSF_OPTICAL_SIGNATURE- 使用方位角/仰角表格来定义特征。如果没有显式选择模型，这是默认模型。  
• WSF_SPACE_OPTICAL_SIGNATURE - 为空间平台计算动态特征。  
• WSF_COMPOSITE_OPTICAL_SIGNATURE - 一个简单的动态光学和红外特征。

# 4.4.4.1. 标准光学特性模型 WSF_OPTICAL_SIGNATURE

```txt
optical_signature <signature-name> (WSF_OPTICAL_SIGNATURE) interpolate_tables <boolean-value> interpolation_type [linear | logarithmic] state <state-name> | default ... Azimuth-Elevation Table Definition ... state ... end_optical_signature 
```

WSF_OPTICAL_SIGNATURE 提供了 optical_signature 的标准实现，如果用户没有指定不同的实现模型，则使用此模型。该模型将特征实现为一个或多个表集，这些表集在平台处于特定“状态”时适用。“状态”表示一种条件，例如“舱门打开”。

表中的因变量单位应为面积单位（平方米）。

<signature-name> 是给这个特征指定的名称。如果名称指定了一个已存在的定义，那么新的定义将取代当前的定义（即最后一次出现的定义将被用于模拟中）。

<table><tr><td>命令</td><td>interpolate_tables &lt;boolean-value&gt;</td></tr><tr><td>解释</td><td>指定是否对定义的方位角-仰角表进行插值。插值类型可以是线性或对数（参见 interpolation_type）。默认值：true</td></tr><tr><td>命令</td><td>interpolation_type &lt;linear | logarithmic&gt;</td></tr><tr><td>解释</td><td>指定在方位角-仰角表中插值数据时使用线性或对数插值。默认值：linear</td></tr><tr><td>命令</td><td>state &lt;state-name&gt;</td></tr><tr><td>解释</td><td>表示当平台处于特征状态 &lt;state-name&gt;时，将使用以下表定义。如果指定为 default，则在平台处于未匹配任何定义状态时使用后续表。如果未指定状态命令，则特征具有一个适用于所有特征状态的特征表。</td></tr></table>

# 4.4.4.2. 空间平台光学特性 WSF_SPACE_OPTICAL_SIGNATURE

```txt
optical_signature <signature-name> WSF_SPACE_OPTICAL_SIGNATURE state <state-name> | default ... Surface Commands state ... high_resolution_eclipse ... end_optical_signature 
```

WSF_SPACE_OPTICAL_SIGNATURE 是 4.4.4 光学特性 optical_signature 的一种实现，它根据请求时平台、太阳和地球的位置动态计算特征。特别地，计算特征是以下三个组件的结果：

• 太阳反射 - 平台将太阳的辐射反射到传感器方向。只有当平台能看到太阳时才会发生这种反射。  
• 地球反射 - 平台将地球的辐射反射到传感器方向，包括：

太阳在地球表面的反射  
地球本身的辐射

• 平台热辐射 - 平台在暴露于太阳时会升温，在不暴露于太阳时会降温。

注意：此模型提供了光学和视觉检测模式 WSF_EOIR_SENSOR 和 WSF_IRST_SENSOR 所需的所有组件，以及 WSF_OPTICAL_SENSOR 的视觉检测所需的组件。如果使用此模型，任何由 infrared_signature 和 inherent_contrast 提供的特征将被忽略。

注意：目前所有反射假设为朗伯漫反射。由于太阳能电池板的镜面反射引起的耀斑不会发生。

# 命令

<table><tr><td>命令</td><td>state [&lt;state-name&gt;| default]</td></tr><tr><td>解释</td><td>表示当平台处于特征状态 &lt;state-name&gt;时，将使用以下表定义。如果指定为 default，则在平台处于未匹配任何定义状态时使用后续表。
如果未指定状态命令，则特征具有一个适用于所有特征状态的特征表。
注意：在此模型中使用多个状态是实验性的，应自行承担风险。</td></tr><tr><td>命令</td><td>high_resolution_eclipse&lt;boolean-value&gt;</td></tr><tr><td>解释</td><td>此命令启用更精确的日食状态计算。这会影响组成特征的表面温度建模以及入射太阳辐射的量。
当禁用此选项时，具有空间移动器的签名平台将使用近似的日食时间计算，以确定表面何时开始从未照射（最低温度）变为照射（最高温度）的值。当启用此选项时，它将检查每次交互的日食状态。
当禁用此选项时，入射太阳辐射在处于本影阴影时为零，而不处于本影阴影时为全值。当启用此选项时，当表面处于半影阴影区域时，入射太阳照明也会取中间值。远离地球时，这两种模式的差异最为明显。
注意：启用此功能将影响运行时间，因为每次交互将进行更多计算。然而，对于非椭圆轨道或远离地球的平台，此模式将提供更准确的结果。
默认值：禁用</td></tr></table>

# 表面命令

这些命令提供了一种定义近似平台表面的简单三维形状的方法。辐射从每个表面反射或

发射到观察者。每个表面独立考虑，并且不考虑一个表面对另一个表面的遮挡（因此不需要定义表面的位置）。另一个关键点是表面的实际尺寸并不重要，而是表面的面积及其法向矢量。这在聚合表面时尤为重要。

应尽量减少定义平台的形状数量。例如，国际空间站有八个大型太阳能电池板，总表面积为 2500 平方米。假设所有的近似相同，定义一个面积为 2500 平方米的表面（使用“盒子”或“平面”表面）就足够了。

除“球体”外，所有表面都是可定向的。

# 公共表面命令 Common Surface Commands

所有表面共享以下命令：

<table><tr><td>命令</td><td>reflectance</td></tr><tr><td>解释</td><td>原帮助文档中也是没有任何解释，只有下面的默认值。默认值：1.0</td></tr><tr><td>命令</td><td>temperature_change_rate</td></tr><tr><td>解释</td><td>指定表面的时间变化率。当太阳不再可见时，表面温度开始下降，直到达到最低温度。当太阳随后可见时，表面温度开始上升，直到达到最高温度。默认值：0.1 k/sec</td></tr><tr><td>命令</td><td>minimum_temperature</td></tr><tr><td>解释</td><td>指定表面在未照射太阳时将降低到的最低温度。默认值：173.15 k</td></tr><tr><td>命令</td><td>maximum_temperature</td></tr><tr><td>解释</td><td>指定表面在照射太阳时将升高到的最高温度。默认值：373.15 k</td></tr></table>

# 可定向表面命令 Orientable Surface Commands

除“球体”外，大多数表面都是可定向的。每个表面都有自己的坐标系，与零件坐标系（PCS）完全平行。表面的尺寸或面积最初在实体坐标系中定义，定向命令指定表面的定向。旋转后的框架是零件坐标系，所有提示（如果请求）都是相对于该系统进行的。

<table><tr><td>命令</td><td>yaw &lt;angle-value&gt;</td></tr><tr><td>解释</td><td>指定表面相对于其附加实体的偏航角。默认值: 0.0 度</td></tr><tr><td>命令</td><td>pitch &lt;angle-value&gt;</td></tr><tr><td>解释</td><td>指定表面相对于其附加实体的俯仰角。默认值: 0.0 度</td></tr><tr><td>命令</td><td>roll &lt;angle-value&gt;</td></tr><tr><td>解释</td><td>指定表面相对于其附加实体的滚转角。默认值: 0.0 度</td></tr><tr><td>命令</td><td>cue_to &lt;cue-target&gt;</td></tr><tr><td>解释</td><td>指定 PCS X 轴将对齐的矢量, 受以下定义的方位角限制和仰角限制约束。目前唯一有效的值是: 太阳默认值: 无注意: 必须指定方位角限制和/或仰角限制才能进行提示。注意: 提示最常用于定位太阳能电池板, 但请注意, 实际上, 定位是通过定向面板和平台来完成的。根据平台的姿态控制, 可能需要允许两个方向的提示以模拟平台姿态变化。</td></tr><tr><td>命令</td><td>azimuth_cuelimits &lt;min-angle-value angle-value&gt; &lt;max-angle-value angle-value&gt;</td></tr><tr><td>解释</td><td>指定在执行 cue_to 操作时, 表面在方位角 (PCS Z 轴旋转) 上可提示的绝对最小和最大角度。</td></tr><tr><td></td><td>限制在零件坐标系（PCS）中指定，必须在范围[-180度..180度]内。
默认值：0度0度（不执行方位角提示）</td></tr><tr><td>命令</td><td>elevation_cuelimits &lt;min-angle-value angle-value&gt; &lt;max-angle-value angle-value&gt;</td></tr><tr><td>解释</td><td>指定在执行 cue_to 操作时，表面在仰角（PCS Y轴旋转）上可提示的绝对最小和最大角度。
限制在零件坐标系（PCS）中指定，必须在范围[-180度..180度]内。
默认值：0度0度（不执行仰角提示）</td></tr></table>

# 盒子形状 surface box

```txt
surface box size ... Orientable Surface Commands ... Common Surface Commands end_SURFACE 
```

<table><tr><td>命令</td><td>size &lt;length-value&gt;&lt;length-value&gt;&lt;length-value&gt;</td></tr><tr><td>解释</td><td>定义盒子的尺寸。第一个值是沿零件坐标系（PCS）X轴的尺寸，第二个是沿PCS Y轴的尺寸，第三个是沿PCS Z轴的尺寸。
注意：其中一个尺寸可以为零。这是为了定义双面物体，如太阳能电池板或SAR天线。
默认值：1米（每个方向）</td></tr></table>

# 平面形状 surface plane

```txt
surface plane area ... Orientable Surface Commands ... Common Surface Commands end_SURFACE 
```

<table><tr><td>命令</td><td>area &lt;area-value&gt;</td></tr><tr><td>解释</td><td>定义平面的面积。
默认值：1平方米</td></tr></table>

# 球形形状 surface sphere

```txt
surface sphere radius ... Common Surface Commands end_SURFACE 
```

<table><tr><td>命令</td><td>radius &lt;length-value&gt;</td></tr><tr><td>解释</td><td>定义球体的半径。
默认值：1米</td></tr></table>

# 4.4.4.3. 组合光学特性 WSF_COMPOSITE_OPTICAL_SIGNATURE

```txt
optical_signature <signature-name> WSF_COMPOSITE_OPTICAL_SIGNATURE state <state-name> | default ... Surface Commands state ... end_optical_signature 
```

WSF_COMPOSITE_OPTICAL_SIGNATURE 是 optical_signature 的一种实现，它扩展了标准的光学特征模型，同时提供红外特征。用户定义一个或多个大致定义平台表面的表面。每个表面都有一个与方向相关的投影面积，并且具有静态或动态定义的温度。表面的温度用于使用黑体模型确定其辐射强度。

请注意，此模型的结果假设观察者与由此特征表示的物体之间的距离远大于物体的大小（即：远场假设）。

注意：此模型提供了光学和视觉检测模式 WSF_EOIR_SENSOR 和 WSF_IRST_SENSOR 所需的所有特征组件，以及 WSF_OPTICAL_SENSOR 的视觉检测所需的组件。特别是，此模型还提供了任何由 infrared_signature 和 inherent_contrast 提供的特征。如果使用此模型，任何由这些命令提供的特征将被忽略。

# 未来发展

这个模型代表了一种开发能力。特别地：

• 尾焰表面将自动附加到前一个表面，但它仅在圆锥、圆柱和半球形状中进行了测试。  
• 尾焰目前需要显式指定尾焰温度、长度和半径。未来，这些值可能会根据当前条件在运行时确定。  
• 偏航、俯仰和滚转命令被接受并处理，但尚未彻底测试。鉴于可用的形状，大多数应用不需要方向。如果使用，应使用 90 度的倍数，否则自动面邻接检查可能无法正确工作。

<table><tr><td>命令</td><td>state [ &lt;state-name&gt; | default ]</td></tr><tr><td>解释</td><td>表示当平台处于特征状态 &lt;state-name&gt;时，将使用以下表定义。如果指定为 default，则在平台处于未匹配任何定义状态时使用后续表。
如果未指定状态命令，则特征具有一个适用于所有特征状态的特征表。</td></tr></table>

# 表面命令

这些命令提供了一种定义近似平台表面的简单三维形状的方法。辐射从每个表面反射或发射到观察者。每个表面独立考虑，并且不考虑一个表面对另一个表面的遮挡（因此不需要定义表面的位置）。另一个关键点是表面的实际尺寸并不重要，而是表面的面积及其法向矢量。这在聚合表面时尤为重要。

应尽量减少定义平台的形状数量。例如，国际空间站有八个大型太阳能电池板，总表面积为 2500 平方米。假设所有的近似相同，定义一个面积为 2500 平方米的表面（使用“盒子”或“平面”表面）就足够了。

# 公共表面命令 Common Surface Commands

所有表面共享以下命令：

<table><tr><td>命令</td><td>location &lt;x-size&gt;&lt;y-size&gt;&lt;z-size&gt;&lt;length-units&gt;</td></tr><tr><td>解释</td><td>指定表面相对于实体坐标系原点的位置。除非排除相邻面,否则每个表面的投影面积是独立计算的。默认:如果未指定位置,则位置将使定义的表面直接紧邻前一个表面的最末端位置。</td></tr><tr><td>命令</td><td>temperature &lt;temperature-value&gt;</td></tr><tr><td>解释</td><td>指定用于计算黑体模型温度的表面固有温度。这表示由于自生产(发动机、加热器等)或皮肤摩擦而产生的温度,不包括由于太阳加热的温度。第一种形式指定一个恒定温度。第二种形式根据高度、速度或马赫数等独立变量的表定义温度。ambient 表示温度是环境温度加上 temperature_offset 的值。adiabatic_WALL 表示温度将使用绝热壁假设计算。默认:无,必须指定。</td></tr><tr><td>命令</td><td>temperature_offset &lt;temperature-value&gt;</td></tr><tr><td>解释</td><td>指定在 temperature Ambient 被指定时添加到环境温度的温度偏移量。可以指定为负值。默认:0.0 K。</td></tr><tr><td>命令</td><td>recovery_factor (0..1]</td></tr><tr><td>解释</td><td>为绝热壁温度模型指定恢复因子。默认:0.85。</td></tr><tr><td>命令</td><td>gamma &lt;real-value&gt;</td></tr><tr><td>解释</td><td>为绝热壁温度模型指定比热比。默认:1.4。</td></tr></table>

# 绝热壁温度模型

如果温度命令指定 adiabatic_wall，则用于黑体模型的温度将根据绝热壁假设确定。计算公式如下：

$$
\mathrm {T} = \mathrm {T} _ {\mathrm {a m b}} \left(1 + \mathrm {F} \left(\frac {\gamma - 1}{2} \mathrm {r M} ^ {2}\right)\right)
$$

其中：

• $\mathrm { T _ { a m b } }$ ：当前高度的环境（静态）温度。  
• ：当前马赫数。  
• γ：比热比。  
• r：恢复因子。  
• ：绝热修正因子。

绝热修正因子 尝试解决绝热壁模型在高海拔时不太适用的问题（即使大气密度接近为零时，该模型在高马赫数情况下会导致高温）。对于海拔低于 30 公里的高度，绝热修正因子的值为 1.0。对于海拔高于 30 公里的高度，修正因子计算如下：

$$
\mathrm {F} = 1. 0 - \frac {\rho_ {3 0} - \rho}{\rho_ {3 0}}
$$

其中：

• ρ ：30 公里高度的大气密度。  
• ：当前高度的大气密度。

随着密度减少，该表达式趋近于零。

# 可定向表面命令 Orientable Surface Commands

大多数表面（除了“球形”和“表形”）可以定向。每个表面都有自己的坐标系，完全平行于零件坐标系（PCS）。表面的尺寸或面积最初在 PCS 框架中定义，定向命令指定表面的方向。

<table><tr><td>命令</td><td>yaw &lt;angle-value&gt;</td></tr><tr><td>解释</td><td>指定表面相对于附加实体的偏航角。
默认：0.0度。</td></tr><tr><td>命令</td><td>pitch &lt;angle-value&gt;</td></tr><tr><td>解释</td><td>指定表面相对于附加实体的俯仰角。
默认：0.0度。</td></tr><tr><td>命令</td><td>roll &lt;angle-value&gt;</td></tr><tr><td>解释</td><td>指定表面相对于附加实体的滚转角。
默认：0.0度。</td></tr></table>

# 形状定义

# 盒形 Box Shape

```txt
surface box size ... .. Orientable Surface Commands ... ... Common Surface Commands ...   
end_SURFACE 
```

<table><tr><td>命令</td><td>size &lt;length-value&gt; &lt;length-value&gt; &lt;length-value&gt;</td></tr><tr><td>解释</td><td>指定表面相对于附加实体的滚转角。
默认：0.0度。</td></tr></table>

# 圆锥形 Cone Shape

```txt
surface cone length ... radius ... Orientable Surface Commands ... Common Surface Commands ... end_SURFACE 
```

圆锥形可用于定义平台的尖锐（或流线型）鼻部。圆锥的轴沿零件坐标系（PCS）X 轴，圆锥的底面在 PCSY-Z 平面内。

<table><tr><td>命令</td><td>length</td></tr><tr><td>解释</td><td>定义圆锥的长度。
默认：必须提供。</td></tr><tr><td>命令</td><td>radius</td></tr><tr><td>解释</td><td>定义圆锥的底面半径。
默认：必须提供。</td></tr></table>

# 圆柱形 Cylinder Shape

```txt
surface cylinder 
```

```txt
length ...  
radius ...  
... Orientable Surface Commands ...  
... Common Surface Commands ...  
end_SURFACE 
```

圆柱形可用于定义平台的主体。圆柱的轴沿零件坐标系（PCS）X 轴，圆柱的端盖在 PCSY-Z 平面内。

<table><tr><td>命令</td><td>length</td></tr><tr><td>解释</td><td>定义圆柱的长度。
默认：必须提供。</td></tr><tr><td>命令</td><td>radius</td></tr><tr><td>解释</td><td>定义圆柱的底面半径。
默认：必须提供。</td></tr></table>

# 半球形 Hemisphere Shape

```txt
surface hemisphere radius ... Orientable Surface Commands ... Common Surface Commands ... end_SURFACE 
```

半球形状可以用来定义钝体的鼻部。半球的轴沿着部件坐标系（PCS）的 X 轴。半球的底部位于 PCS 的 Y-Z 平面内。

<table><tr><td>命令</td><td>radius &lt;长度值&gt;</td></tr><tr><td>解释</td><td>定义半球的半径。
默认值：必须提供。</td></tr></table>

# 尾焰形 plume shape

```txt
surface plume length ... radius ... ... Common Surface Commands ... end_SURFACE 
```

尾焰形状表示火箭或喷气发动机的尾焰。此形状根据当前操作条件提供尾焰的大致尺寸和温度。假设尾焰与部件坐标系（PCS）的 X 轴对齐。

位置命令对尾焰无效。尾焰总是附着在紧接前面的表面上。它也不是一个可定向的表面（偏航、俯仰和滚动命令无效）。

<table><tr><td>命令</td><td>length&lt;长度值&gt;</td></tr><tr><td>解释</td><td>明确定义尾焰的长度。默认值：未指定，这表示长度将根据当前条件确定。如果提供了长度，则必须同时</td></tr><tr><td></td><td>指定半径。
注意：在当前版本中必须指定。自动调整大小尚未实现。</td></tr><tr><td>命令</td><td>radius&lt;长度值&gt;</td></tr><tr><td>解释</td><td>明确定义尾焰的半径。
默认值：未指定，这表示半径将根据当前条件确定。如果提供了半径，则必须同时指定长度。
注意：在当前版本中必须指定。自动调整大小尚未实现。</td></tr></table>

# 球形状 Spherical Shape

```txt
surface sphere radius ... Common Surface Commands ... end_SURFACE 
```

这定义了一个简单的球形状。

<table><tr><td>命令</td><td>radius&lt;长度值&gt;</td></tr><tr><td>解释</td><td>定义球的半径。
默认值：必须提供。</td></tr></table>

# 表格定义形状 tabular shape

```txt
surface tabular projected_area ... Common Surface Commands ... end_SURFACE 
```

表格形状是其投影面积由一个表定义的形状，该表是观察者的方位角和仰角的函数。此形状通常单独出现。它通常用于包含用于定义标准光学特征的现有表格。通过简单地向此形状添加温度定义，可以获得红外特征。

位置命令对这种形状无效。它也不是一个可定向的表面（偏航、俯仰和滚动命令无效）。

<table><tr><td>命令</td><td>projected_area_Azimuth-elevation_Table_Definition</td></tr><tr><td>解释</td><td>指定方位角-仰角表定义。
默认值：必须提供。</td></tr></table>

# 4.4.4.4. 多光学特性 WSF_MULTIRESOLUTION_OPTICAL_SIGNATURE

```batch
multiresolution_optical_signature WSF_MULTIRESOLUTION_OPTICAL_SIGNATURE ... multiresolution_optical_signature ...   
endMULTIRESOLUTION_optical_signature 
```

# 概述

multiresolution_optical_signature 定义了一个 容器，用于在平台上 保存一个或多个optical_signature 对 象 ， 并 将 选 择 使 用 哪 个 optical_signature 推 迟 到 运 行 时 。 选 择optical_signature 是 通 过 与 组 件 关 联 的 fidelity 参 数 来 完 成 的 。 容 器 中 定 义 的 每 个

optical_signature 模型都分配了一个 fidelity_range，在初始化期间根据匹配的 fidelity 设置平台上的 optical_signature。

使用方法

定义新类型: 可以在 platform 或 platform_type 命令之外使用 multiresolution_optical_signature来定义新类型。

```matlab
multiresolution_optical_signature<derived>WSF_MULTIRESOLUTION_OPTICAL_SIGNATURE  
fidelity <real-value>  
[add | edit] model <string-value>  
fidelity_range <real-value> <real-value>  
[default]  
optical_signature [<optical_signature-type>]  
... optical_signature ...  
end_optical_signature  
end_model  
[add | edit] model <string-value>  
... Any number of models may be specified ...  
end_model  
common  
... optical_signature ...  
end_common  
endMULTIRESOLUTION_OPTICAL_SIGNATURE 
```

实 例 化 对 象 : 可 以 在 platform_type 或 platform 实 例 上 实 例 化 一 个multiresolution_optical_signature 对象。

```txt
platform_type ...
multiresolution Optical Signature <type>
    ... multiresolution Optical signature commands ...
endMULTIRESOLUTION Optical signature
endplatform_type 
```

```txt
platform ...
    add multiresolution_optical_signature <type>
        ... multiresolution_optical_signature commands ...
    endMULTIRESOLUTION_OPTICAL_SIGNA
endplatform 
```

修改现有对象: 可以在 platform 实例上修改现有的 multiresolution_optical_signature 对象。

```txt
platform ... edit multiresolution_optical_signature <type> 
```

```txt
... multiresolution Optical signature commands ... endMULTRESOLUTONOptical signature endplatform 
```

# 命令

fidelity <real-value>: 定义组件的 fidelity 值，决定在运行时使用哪个 optical_signature。必须在 0 到 1 之间（包括 0 和 1）。此值直接映射到模型命令中定义的 fidelity_range。默认值: 1.0  
model <string-value> ... end_model: 定义或编辑包含的 optical_signature 模型，名称由字符串给出。支持隐式添加（或编辑如果命名模型存在）以及使用 add 和 edit 命令的显式添加和编辑。

注意: 必须至少指定一个模型块。

fidelity_range <real-value> <real-value>: 定义此模型应使用的 fidelity 值范围。必须在 0到 1 之间（包括 0 和 1），按递增顺序排列，并且不得与此组件上的另一个模型的fidelity_range 重叠。

默认值: 0.0 1.0

default: 如果没有匹配的 fidelity，则使用此模型作为默认选择。  
optical_signature <optical_signature-type> ... end_optical_signature: 定义 optical_signature模型的类型和特定于此模型实例化的参数。在首次定义新模型时需要 optical_signature，在编辑现有模型时不得指定。  
common ... end_common: 定义要转发到所有当前指定的 optical_signature 模型的通用参数。这些参数必须对所有当前定义的 optical_signature模型有效。

# 说明

多分辨率分析: 这种方法允许在不同的分辨率下分析和选择合适的 optical_signature 模型，以便在不同的场景中优化性能。

未来改进: 计划在场景文件的其他位置提供 fidelity 选择，以提高此组件的实用性。

# 4.4.5. 雷达特性 radar_signature

```txt
radar_signature <signature-name> use_bisector_for_bistatic <boolean-value> interpolate_tables <boolean-value> interpolation_type [linear | logarithmic] state <state-name> default polarization [horizontal | vertical | slant_45 | slant_135 | left_circular | right_circular | default] frequency_limit <frequency-value> ... Azimuth-Elevation Table Definition ... frequency_limit <frequency-value> ... Azimuth-Elevation Table Definition ... polarization ... plt_file <file-name> ... 
```

```txt
state ... end_radar_signature 
```

radar_signature 定义了平台类型的雷达特征。当雷达传感器尝试检测平台时，会使用雷达特征。雷达特征由一个或多个表集组成，每个表集定义了平台处于特定“状态”时的特征（作为极化和频率的函数）。一个“状态”表示一种条件，例如“舱门打开”。

<signature-name> 是要赋予特征的名称。如果名称指定了现有定义的名称，则新定义将替换当前定义（即，模拟中将使用最后一次出现的定义）。

<table><tr><td>命令</td><td>use_bisector_for_bistaticboolean-value&gt;</td></tr><tr><td>解释</td><td>指定是否为双基地检测尝试近似双基地特征。如果为真,RCS(雷达截面)将使用目标到发射器和目标到接收器的角度平分线来确定。如果为假,RCS将使用目标到接收器的角度来确定。默认值:真</td></tr><tr><td>命令</td><td>interpolate_tablesboolean-value&gt;</td></tr><tr><td>解释</td><td>指定是否对定义的方位角-仰角表进行插值。插值类型可以是线性或对数(见 interpolation_type)。默认值:真</td></tr><tr><td>命令</td><td>interpolation_type&lt;linear | logarithmic&gt;</td></tr><tr><td>解释</td><td>指定在方位角-仰角表中插值时使用线性或对数插值。默认值:线性</td></tr><tr><td>命令</td><td>state [&lt;state-name] | default]</td></tr><tr><td>解释</td><td>表示当平台处于特征状态 &lt;state-name&gt;时将使用以下表定义。如果指定了 default,则在平台处于未匹配任何定义状态的特征状态时将使用后续表。如果未指定状态命令,则特征具有一个适用于所有特征状态的表集。</td></tr><tr><td>命令</td><td>polarization [horizontal | vertical | slant_45 | slant_135 | left_circular | right_circular | default]</td></tr><tr><td>解释</td><td>表示当感应雷达以指定极化操作时将使用以下表(直到下一个极化或状态)。如果省略极化,则以下表(直到下一个状态)适用于任何极化。</td></tr><tr><td>命令</td><td>frequency_limit[frequency-value&gt;</td></tr><tr><td>解释</td><td>表示以下表适用的频率上限。这些必须在单个状态/极化分组内按递增顺序出现。对于以特定极化和频率操作的雷达,将选择第一个具有适当状态和极化且频率小于 frequency_limit 的表。如果省略 frequency_limit,则以下表适用于所有频率。</td></tr><tr><td>命令</td><td>plt_file[defaulthorizontal | vertical]</td></tr><tr><td>解释</td><td>加载包含多个方位角/仰角表定义的 PLT 文件,这些表按极化和频率索引。由于极化和频率嵌入在文件中,任何先前的极化或 frequency_limit 命令将被忽略。可以选择指定一个默认极化(水平或垂直)。然而,由于每个状态必须有一个默认极化,如果省略此可选参数,则必须使用 polarization 命令显式定义一个。注意:当前版本中 PLT 文件仅接受水平和垂直极化。注意:PLT 文件中指定的频率是中心频率,而不是频率限制。对于特定频率的电磁相互作用,将基于中心频率周围的频带选择表,而不是基于频率限制。例如,考虑一个具有 0.1、1 和 10 GHz 频率索引表的 PLT 文件。在这种情况下,0 到 0.55 GHz之间的电磁相互作用将使用第一个表,0.55 到 5.5 GHz 之间的相互作用使用第二个表,5.5 GHz 及以上的相互作用使用第三个表。</td></tr></table>

示例

内联表  
```txt
radar_signature AIRPLANE_RADARSIG 
```

```txt
state default inline_table dbsm 20 2 -90.0 90.0 -180.0 0.0 0.0 -137.5 0.0 0.0 -135.0 20.0 20.0 -132.5 0.0 0.0 -92.5 0.0 0.0 -90.0 20.0 20.0 -87.5 0.0 0.0 -47.5 0.0 0.0 -45.0 20.0 20.0 -42.5 0.0 0.0 42.5 0.0 0.0 45.0 20.0 20.0 47.5 0.0 0.0 87.5 0.0 0.0 90.0 20.0 20.0 92.5 0.0 0.0 132.5 0.0 0.0 135.0 20.0 20.0 137.5 0.0 0.0 180.0 0.0 0.0 end在线line_table and_radar_signature 
```

双基地特征   
bistatic_signature interpolate_transmitterAnglesboolean-value> transmitterAngles_interpolation_type [linear | logarithmic] state<state-name $\rightharpoondown$ default polarization [horizontal | vertical | left_circular | right_circular | default] frequency_limit <frequency-value> azimuth <angle-value> elevation <angle-value> ...方位角-仰角表定义 ... elevation ... azimuth ... frequency_limit ...

```txt
polarization ... azimuth <angle-value> elevation <angle-value> plt_file <file-name> ... elevation ... azimuth <angle-value> ... state ... end_bistatic_signature 
```

定义平台类型的双基地雷达特征。此特征用于双基地相互作用（即，涉及非同地点的发射器和接收器的相互作用）。此输入块在 radar_signature 块内定义，并定义用于双基地相互作用 RCS 查找的单独表。

注意：如果定义了 bistatic_signature，则双基地特征将覆盖 use_bisector_for_bistatic 命令。

注意：如果未定义 radar_signature 而定义了 bistatic_signature，则双基地特征也将用于单基地相互作用，使用相同的接收和发射角度进行查找。

<table><tr><td>命令</td><td>interpolate_transmitterAnglesboolean-value&gt;</td></tr><tr><td>解释</td><td>指定是否在指定的目标到发射器角度表之间进行插值。如果为“假”,则使用给定目标到发射器方位/仰角对的下一个较低方位/仰角表。默认值:假</td></tr><tr><td>命令</td><td>transmitterAngles_interpolation_type&lt;linear | logarithmic&gt;</td></tr><tr><td>解释</td><td>指定在插值目标到发射器角度时使用线性或对数插值。默认值:线性</td></tr><tr><td>命令</td><td>azimuth</td></tr><tr><td>解释</td><td>指定输入表的最小目标到发射器方位角,范围在[-180.0,180.0]度之间。必须指定至少两个单调递增的角度和表。表是目标到接收器角度的函数。</td></tr><tr><td>命令</td><td>elevation</td></tr><tr><td>解释</td><td>指定输入表的最小目标到发射器仰角,范围在[-90.0,90.0]度之间。必须指定至少两个单调递增的角度。表是目标到接收器方位/仰角的函数。</td></tr></table>

# 4.4.5.1. 多雷达特性模型 WSF_MULTIRESOLUTION_RADAR_SIGNATURE

```batch
multiresolution_radar_signature WSF_MULTIRESOLUTION_RARAD_SIGNATURE ... multiresolution_radar_signature ...   
endMULTIRESOLUTION_radar_signature 
```

概述

multiresolution_radar_signature 定 义 了 一 个 容 器 ， 用 于 在 平 台 上 保 存 一 个 或 多 个radar_signature 对象，并将选择使用哪个 radar_signature 推迟到运行时。选择 radar_signature是通过与组件关联的 fidelity 参数来完成的。容器中定义的每个 radar_signature 模型都分配了一个 fidelity_range，在初始化期间根据匹配的 fidelity 设置平台上的 radar_signature。

使用方法

定义新类型: 可以在 platform 或 platform_type 命令之外使用 multiresolution_radar_signature

来定义新类型。

```txt
multiresolution_radar_signature<derived>WSF MultiresOLUTION_RARAD_SIGNATURE fidelity <real-value> [add | edit] model <string-value> fidelity_range <real-value> <real-value> [default] radar_signature [<radar_signature-type>] ... radar_signature ... end_radar_signature end_model [add | edit] model <string-value> ... Any number of models may be specified ... end_model common ... radar_signature ... end_common endMULTIRESOLUTION_radar_signature 
```

实 例 化 对 象 : 可 以 在 platform_type 或 platform 实 例 上 实 例 化 一 个multiresolution_radar_signature 对象。

```txt
platform_type ...
multiresolution_radar_signature <type>
    ... multiresolution_radar_signature commands ...
endMULTIRESOLUTION_RARAD_SIGNATURE
endPLATFORM_TYPE 
```

```txt
platform ...
    add multiresolution_radar_signature <type>
        ... multiresolution_radar_signature commands ...
    endMULTIRESOLUTION_RARAD_SIGNATURE
endplatform 
```

修改现有对象: 可以在 platform 实例上修改现有的 multiresolution_radar_signature 对象。

```txt
platform ...
edit multiresolution_radar_signature <type>
    ... multiresolution_radar_signature commands ...
endMULTIRESOLUTION_RARAD_SIGNATURE
endplatform 
```

命令

fidelity <real-value>: 定义组件的 fidelity 值，决定在运行时使用哪个 radar_signature。必须在 0 到 1 之间（包括 0 和 1）。此值直接映射到模型命令中定义的 fidelity_range。默认值: 1.0  
model <string-value> ... end_model: 定义或编辑包含的 radar_signature 模型，名称由字符串给出。支持隐式添加（或编辑如果命名模型存在）以及使用 add 和 edit 命令的显式添加和编辑。

注意: 必须至少指定一个模型块。

fidelity_range <real-value> <real-value>: 定义此模型应使用的 fidelity 值范围。必须在 0到 1 之间（包括 0 和 1），按递增顺序排列，并且不得与此组件上的另一个模型的fidelity_range 重叠。

默认值: 0.0 1.0

default: 如果没有匹配的 fidelity，则使用此模型作为默认选择。  
radar_signature <radar_signature-type> ... end_radar_signature: 定义 radar_signature 模型的类型和特定于此模型实例化的参数。在首次定义新模型时需要 radar_signature，在编辑现有模型时不得指定。  
common ... end_common: 定义要转发到所有当前指定的 radar_signature 模型的通用参数。这些参数必须对所有当前定义的 radar_signature模型有效。

# 说明

多分辨率分析: 这种方法允许在不同的分辨率下分析和选择合适的radar_signature模型，以便在不同的场景中优化性能。  
未来改进: 计划在场景文件的其他位置提供 fidelity 选择，以提高此组件的实用性。

# 4.5. 跟踪管理器 track_manager

```txt
trackmanager
    debug
    correlation_method ...
    fusion_method ...
    tracker_type ...
    uncorrelated_trackdrops ...
    retain_raw Tracks
    retain_track_history
    filter ... end_filter
    track ... end_track
    aux_data ... end(aux_data
    aux_data_fusion_rule ... end(aux_data_fusion_rule
    typeSpecifictracker_inputss
end_trackmanager 
```

track_manager 模块是平台的一个子命令，用于定义平台主跟踪管理器的子命令。一个跟 踪 管 理 器 维 护 平 台 的 主 跟 踪 列 表 。 它 还 可 以 用 于 通 过 标 准 WSF 处 理 器（WSF_TRACK_PROCESSOR）维护备用跟踪列表。

<table><tr><td>命令</td><td>debug</td></tr><tr><td>解释</td><td>启用将调试信息写入标准输出。</td></tr><tr><td>命令</td><td>correlation_method</td></tr><tr><td>解释</td><td>correlation_method&lt;correlation-method&gt;Correlation commands...end-correlation_method指定跟踪管理器使用的关联算法。关联算法确定新的跟踪和测量更新信息是否与现有跟踪匹配。如果是,则使用fusion_method将新信息融合到现有跟踪中;否则,创建新跟踪。&lt;correlation-method&gt;可以是: ·perfect ·nearest_neighbor ·truth ·mtt每种类型都有其独特的输入关键字。参考:4.5.1关联方法 correlation-method。</td></tr><tr><td>命令</td><td>fusion_method</td></tr><tr><td>解释</td><td>fusion_method&lt;Fusion-method&gt;Fusion Commands...end_fusion_method指定跟踪管理器使用的融合算法。融合算法将来自两个或多个来源的单一实体信息合并为一个连贯的信息集或跟踪。&lt;fusion-method&gt;可以是: ·replacement ·weighted_average ·mtt ·orbit_determination每种类型都有其独特的输入关键字。参考:4.5.2融合方法 fusion_method。</td></tr><tr><td>命令</td><td>tracker_type</td></tr><tr><td>解释</td><td>tracker_type&lt;type-name&gt;Correlation commands...Fusion commands...Other tracker commands...endtracker_type指定使用的标准跟踪器类型。使用此输入意味着不必指定 correlation_method或fusion_method。注意:目前唯一有效的跟踪器类型是“mtt”(多目标跟踪器;参考:4.5.3MTT跟踪器Multi-Target Tracker)。</td></tr><tr><td>命令</td><td>uncorrelated_trackdrops [on;off]</td></tr><tr><td>解释</td><td>指定是否丢弃无关联的本地跟踪(即不再有任何关联的原始跟踪)。如果在关联的WSFTRACKPROCESSOR中清除了跟踪,则自动设置为 off。默认值:on</td></tr><tr><td>命令</td><td>retain_raw Tracks</td></tr><tr><td>解释</td><td>指定跟踪管理器是否保留所有原始跟踪信息。如果设置,则用户需负责管理原始跟踪信息。默认:不保留原始跟踪信息。</td></tr><tr><td>命令</td><td>retain_track_history</td></tr><tr><td>解释</td><td>指定跟踪管理器是否保留跟踪历史信息。如果设置,则用户需负责管理跟踪历史。默认:不保留跟踪历史信息。</td></tr><tr><td>命令</td><td>filter &lt;type-name&gt; end_filter</td></tr><tr><td>解释</td><td>将滤波器类型与跟踪管理器关联。所有类型为“未过滤传感器”的传入跟踪将使用此滤波器类型进行过滤。
参见: 4.5.4 滤波器 filter</td></tr><tr><td>命令</td><td>track ... end_track</td></tr><tr><td>解释</td><td>track块中定义的目标会一直被跟踪,无论传感器有没有探测到,相当于定义了个初始跟踪物体,只要没有明确停止跟踪,则会一直跟踪和更新其信息。可以定义多个track。
参见: 4.5.5 跟踪器 track</td></tr><tr><td>命令</td><td>aux_data ... end(aux_data</td></tr><tr><td>解释</td><td>指定将添加到任何“本地”跟踪中的附加数据,这些数据由跟踪管理器创建和维护。这些数据将作为对跟踪和资源分配的额外辅助。</td></tr><tr><td>命令</td><td>aux_data_fusion_rule ... end(aux_data_fusion_rule</td></tr><tr><td>解释</td><td>定义在将原始跟踪中的 aux_data 变量融合到本地跟踪时应用的规则。通常,原始跟踪中的变量会覆盖本地跟踪中具有相同名称的变量。
variable &lt;name&gt; private
标记为“private”的变量在融合时永不会被覆盖。变量只能由各种本地脚本/任务处理器操作。
variable &lt;name&gt; only_local
标记为“only_local”的变量只能被来自本平台的传入原始跟踪覆盖。
variable &lt;name&gt; prefer_local
标记为“prefer_local”的变量可以被来自本地平台的传入跟踪或另一个平台的传入跟踪覆盖,但前提是本地跟踪没有包含相同变量的其他贡献跟踪。</td></tr><tr><td>命令</td><td>type Specific tracker_input</td></tr><tr><td>解释</td><td>根据选择的 tracker_type,会有各种有效的输入。特别是对于 MTT 跟踪器,请参见MTT 配置输入参考: 4.5.3MTT 跟踪器 Multi-Target Tracker。</td></tr></table>

# 4.5.1. 关联方法 correlation-method

```txt
correlation_method <correlation-type-name>
... commands ...
end-correlation_method 
```

在 AFSIM中，correlation_method 命令用于指定跟踪管理器使用的关联算法。每种关联方法都有其独特的输入关键字和配置选项。可用的 correlation-type-name有：

```txt
- perfect
- nearest neighbor
- truth
- mtt 
```

每个都有不同的配置，以下会详细说明。

# perfect

```txt
correlation_method perfect end_corrlation_method 
```

测量或跟踪（包括虚假目标）如果其对应的真实平台 ID 匹配，则被关联。这是最快且最简单的关联算法，但不适用于高保真跟踪应用，例如可能出现跟踪交换或丢失的情况。

```txt
nearest_neighbor 
```

```txt
correlation_method nearest_neighbor tracking_sigma <real> turning_sigma <real> coast_time <time-value> end-correlation_method 
```

测量或跟踪基于其各自的协方差矩阵的最近邻近性进行关联。计算出的距离表示两个跟踪的关联概率，如果该概率低于给定阈值，则创建新跟踪。

<table><tr><td>命令</td><td>tracking_sigma &lt;real&gt;</td></tr><tr><td>解释</td><td>指定跟踪最初关联的统计显著性。值为1表示关联跟踪位置之间的距离等于从跟踪的协方差矩阵中提取的一西格玛误差之和，沿着一个跟踪位置到另一个跟踪位置的方向。
注意：较高的值会导致较少的关联，但置信度更高。
默认值：1.0</td></tr><tr><td>命令</td><td>turning_sigma &lt;real&gt;</td></tr><tr><td>解释</td><td>指定如果未达到 tracking_sigma 关联阈值时的关联统计显著性。此值应小于或等于 tracking_sigma 值。值为1表示关联跟踪位置之间的距离等于从跟踪的协方差矩阵中提取的一西格玛误差之和，沿着一个跟踪位置到另一个跟踪位置的方向。
注意：较高的值会导致较少的关联，但置信度更高。
默认值：1.0</td></tr><tr><td>命令</td><td>coast_time &lt;time-value&gt;</td></tr><tr><td>解释</td><td>指定在跟踪不再关联后返回“无关联”结果的时间。此时间独立于任何传感器或跟踪处理器的报告时间。
默认值：1.0秒</td></tr></table>

# truth

```txt
correlation_method truth evaluation_interval <time-value> maximum_corrlation_distance <length-value> ignore_samede <boolean-value> ignore_track_target <boolean-value>   
end_corrlation_method 
```

默认情况下，当跟踪目标信息可用时（即，如果 WsfTrack.Target()返回有效结果），跟踪与 perfect 关联器相同地进行关联。然而，如果没有跟踪目标可用，或 ignore_track_target设置为“true”，则测量和跟踪基于与真实体的接近性进行关联。如果与任何真实体的距离小于给定半径，则跟踪与该体相关联的跟踪进行关联；否则，创建新跟踪。

<table><tr><td>命令</td><td>maximum_corrlation_distance &lt;length-value&gt;</td></tr><tr><td>解释</td><td>指定跟踪位置与真实位置之间的最大距离，在此距离内发生与现有跟踪的关联。如果距离超过此最大值，或没有与真实体相关联的现有跟踪，则创建新跟踪。默认值：1000米</td></tr><tr><td>命令</td><td>ignore_same_side &lt;boolean-value&gt;</td></tr><tr><td>解释</td><td>在执行关联时，忽略与跟踪报告的同一侧（如果有）的真实体。默认值：false</td></tr><tr><td>命令</td><td>evaluation_interval &lt;time-value&gt;</td></tr><tr><td>解释</td><td>指定在已经关联的跟踪上执行后续关联的时间。
默认值：0秒</td></tr><tr><td>命令</td><td>ignore_track_target &lt;boolean-value&gt;</td></tr><tr><td>解释</td><td>指定在进行关联时是否忽略与跟踪相关的真实数据。如果此值设置为 true，则在可能的情况下，关联与 perfect 关联器相同。
默认值：false</td></tr></table>

mtt

```txt
correlation_method mtt <MTT Commands...> end-correlation_method 
```

测量或跟踪与多目标跟踪器（MTT）进行关联。关联算法类似于最近邻。如果选择此方法，则 fusion_method 也必须是 mtt。

# 4.5.2. 融合方法 fusion_method

# 命令相关

```txt
fusion_method <fusion-type-name>
    ... commands ...
end_fusion_method 
```

在 AFSIM 中，fusion_method 命令用于指定跟踪管理器使用的融合算法。融合算法将来自两个或多个来源的单一实体信息合并为一个连贯的信息集或跟踪。以下是可用的融合方法及其详细说明：

```txt
- replacement
- weighted_average
- orbit_determination
- mtt 
```

replacement

```txt
fusion_method replacement end_fusion_method 
```

关联的测量和跟踪根据一组标准算法进行融合。本地跟踪位置被非本地跟踪位置替换。

weighted_average

```txt
fusion_method weighted_average end_fusion_method 
```

关联的测量和跟踪根据一组标准算法进行融合。本地跟踪位置与非本地跟踪位置结合，

使用本地和非本地跟踪的协方差矩阵。

注意：如果非本地跟踪没有关联的协方差矩阵，跟踪管理器将尝试使用从跟踪的测量误差（范围、仰角和方位）生成的测量协方差矩阵。

orbit_determination   
```txt
fusion_method orbit_determination  
number_of_anglemeasurements <int>  
angles_only_linear_tolerance <length-value>  
angles_only_maximum_iterations <int>  
lambert_convergence_tolerance <real>  
process_noise_sigmas_XYZ...  
debug  
debug_filter  
end_fusion_method 
```

轨道确定融合结合多传感器测量算法，提供卫星轨道的初始估计，然后继续融合后续测量以更新和完善初始估计。可以使用仅提供方位-仰角跟踪的角度传感器的目标测量，或也提供范围的测量。一旦轨道初步确定，将触发 ORBIT_DETERMINATION_INITIATED 事件。在后续的轨道确定更新中，将触发 ORBIT_DETERMINATION_UPDATED 事件。

<table><tr><td>命令</td><td>number_of_anglemeasurements integer&gt;</td></tr><tr><td>解释</td><td>指定在进行仅角度初始轨道确定尝试之前要收集的角度测量次数。注意:此值必须至少为5。默认值:5</td></tr><tr><td>命令</td><td>angles_only_LINEAR_tolerance length-value&gt;</td></tr><tr><td>解释</td><td>指定仅角度初始轨道确定算法达到解决方案所需的线性公差。注意:通常不需要设置此值。默认值:1000米</td></tr><tr><td>命令</td><td>angles_only_maximum_iterations integer&gt;</td></tr><tr><td>解释</td><td>指定仅角度初始轨道确定算法找到解决方案的最大迭代次数。注意:通常不需要设置此值。默认值:100</td></tr><tr><td>命令</td><td>lambert_convergence_tolerance real&gt;</td></tr><tr><td>解释</td><td>指定两个位置和时间的拉姆伯特通用变量算法的收敛公差(无单位)。默认值:1.0e-8</td></tr><tr><td>命令</td><td>process_noise_sigmas_XYZ realvalue realvalue realvalue</td></tr><tr><td>解释</td><td>定义嵌入滤波器使用的噪声标准差。值对应于跟踪平台的实体坐标系(ECS)中的加速度。默认值:000</td></tr><tr><td>命令</td><td>debug</td></tr><tr><td>解释</td><td>将调试信息打印到标准输出。</td></tr><tr><td>命令</td><td>debug_filter</td></tr><tr><td>解释</td><td>指定保存过滤历史信息(参见过滤调试)。</td></tr></table>

# 4.5.3. MTT 跟踪器 Multi-Target Tracker

多目标跟踪器 (MTT) 是由 Bogdon & Associates 的 Fred Keifer 生产的跟踪器。它包含在任务级模拟器 SUPPRESSOR 的 $^ { 7 + }$ 版本中，并已用 C 语言重新编码并集成到 AFSIM 中。配置

以下是 MTT 的有效输入摘要及其默认值。如果某个配置输入没有提供输入，则将使用默认值。由于目前没有详细的 MTT 参考文档，这些输入的文档将在可用时添加。这些块输入必须放置在 track_manager 的 tracker_type 块内，并且 tracker_type 必须设置为 mtt。

```txt
track_drop(times  
embryonic_track <time-value> (30.0 s)  
candidate_track <time-value> (30.0 s)  
active_track <time-value> (60.0 s)  
vertical_channel.active_track <time-value> (60.0 s)  
report_delay_for_active_track <time-value> (0.0 s)  
end_track_drop(times  
process_model_one_sigma Errors_candidate_track  
x_dir accel <accel-value> (9.0 m/s2)  
y_dir accel <accel-value> (9.0 m/s2)  
end_process_model_one_sigmaErrors_candidate_track 
```

```tcl
process_model_one_sigma Errors_and_parameters.active_track  
x_dir accel_straight_flight_model <accel-value> (0.09 m/s2)  
y_dir accel_straight rdright_track <accel-value> (0.09 m/s2)  
x_dir accel_turning).[flight_model <accel-value> (8.0 m/s2)  
y_dir accel_turning).[flight_model <accel-value> (8.0 m/s2)  
vertical).[velocity] (6.25 m/s)  
decorrelation_time).[vert).[velocity] (20.0 s)  
end_process_model_one_sigmaErrors_and_parameters.active_track 
```

```txt
one_sigma_state_error_thresholds  
velocity_limit_to_promote_embryonic_track <velocity-value> (700.0 m/s)  
velocity_error_to_promote_embryonic_track <velocity-value> (150.0 m/s)  
position_error_to_promote_candidate_track <distance-value> (500.0 m)  
velocity_error_to_promote_candidate_track <velocity-value> (40.0 m/s)  
position_error_to_promote_vertical_channel <distance-value> (500.0 m)  
velocity_error_to_promote_vertical_channel <velocity-value> (40.0 m/s)  
end_one_sigma_state_error_thresholds 
```

```txt
state_error_covariance_matrix_condition_number_thresholds  
promote_track_in-horizontal_channel <value> (2.0e+4)  
promote_track_in_vertical_channel <value> (1.0e+10)  
end_state_error_covariance_matrix_condition_number_thresholds 
```

state_variance_limit.active_track max_std_dev_straight_flight_model $<  <$ distance-value> (800.0 m) max_std_dev_turning rdright_model $<  <$ distance-value> (800.0 m) min_std_dev_straight rdright_model $<  <$ distance-value> (400.0 m)

```tcl
min_std_dev_turning_flow_model <distance-value> (400.0 m)  
end_state-variance_limit.active_track  
mode_transition(probability_matrix  
straight_to_straight_flow <value> (0.70)  
straight_to_turning_flow <value> (0.30)  
turning_to_turning_flow <value> (0.30)  
turning_to_straight_flow <value> (0.70)  
end_mode_transition(probability_matrix  
probability_of_falsely_rejecting_corrlation  
measurement_to_track <value> (1.0e-20)  
track_to_track <value> (1.0e-20)  
end(probability_of_falsely_rejecting_corrlation  
consecutive_single_source_hits_to_promote_track <value> (0)  
track_corrlation_cylinder  
cylinder_height <distance-value> (2000 m)  
cylinder_diameter <distance-value> (2000 m)  
end_track_corrlation_cylinder  
mttc_track_fusion "<all_sources" | "initial_source_only"> (all_sources) 
```

# 4.5.4. 滤波器 filter

Define a filter type (occurs outside a trackmanager or sensor block)   
filter $<$ name> <base-type> ...type-specific filter commands ..   
end_filter   
#Instantiate a filter object   
platform... (or platform_type) trackmanager filter $<$ filter-type> ...filter commands ... end_filter end_trackmanager   
endPLATFORM   
sensor .. filter $<$ filter-type> ...filter commands ... end_filter

滤波器是一个附加到 track_manager 或 sensor 的对象，用于实现轨迹过滤。它们可以用来筛选、处理或修改传感器数据或轨迹数据。以下是系统实现的各种滤波器。

# 4.5.4.1. ??滤波器 WSF_ALPHA_BETA_FILTER

```txt
filter <name> WSF ALPHA BETA FILTER ... Commands ... end_filter 
```

alpha-beta滤波器实现了以下数据模型：

$$
X _ {f} = X _ {p} ^ {\prime} + \alpha \times (X _ {m} - X _ {p} ^ {\prime})
$$

$$
V _ {f} = V _ {f} ^ {\prime} + \frac {\beta}{d T} \times (X _ {m} - X _ {p} ^ {\prime})
$$

$$
X _ {p} = X _ {f} + d T \times V _ {f}
$$

其中：

α：alpha 参数的值  
$\beta$ ：beta参数的值  
$\Chi _ { \mathrm { m } }$ ：测量位置  
$\mathrm { X } _ { \mathrm { f } }$ ：过滤后的位置  
$\mathrm { X _ { p } }$ ：预测位置  
$\mathrm { V _ { f } }$ ：过滤后的速度  
：自上次滤波更新以来的时间

带撇号的值是上次滤波更新的过滤值。

<table><tr><td>命令</td><td>alpha</td></tr><tr><td>解释</td><td>定义滤波器的 alpha（位置）参数。默认值 0。</td></tr><tr><td>命令</td><td>beta</td></tr><tr><td>解释</td><td>定义滤波器的 beta（速度）参数。默认值 0。</td></tr><tr><td>命令</td><td>debug</td></tr><tr><td>解释</td><td>输出调试信息。</td></tr></table>

# 4.5.4.2. 滤波器 WSF_ALPHA_BETA_GAMMA_FILTER

```txt
filter <name> WSF ALPHA BETA GAMMA FILTER ... Commands ... end_filter 
```

alpha-beta-gamma 滤波器实现了以下数据模型：

$$
X _ {f} = X _ {p} ^ {\prime} + \alpha \times (X _ {m} - X _ {p} ^ {\prime})
$$

$$
V _ {f} = V _ {f} ^ {\prime} + d T \times A _ {f} ^ {\prime} + \frac {\beta}{d T} \times \left(X _ {m} - X _ {p} ^ {\prime}\right)
$$

$$
A _ {f} = A _ {f} ^ {\prime} + \frac {\gamma}{d T ^ {2}} \times \left(X _ {m} - X _ {p} ^ {\prime}\right)
$$

$$
X _ {p} = X _ {f} + d T \times V _ {f} + \frac {d T ^ {2}}{2} \times A _ {f}
$$

其中：

α：alpha参数的值   
$\beta$ ：beta 参数的值  
γ：gamma参数的值   
$\Chi _ { \mathrm { m } }$ ：测量位置  
$\mathrm { X } _ { \mathrm { f } }$ ：过滤后的位置  
$\mathrm { X _ { p } }$ ：预测位置  
$\mathrm { V _ { f } }$ ：过滤后的速度  
$\mathrm { A } _ { \mathrm { f } }$ ：过滤后的加速度  
：自上次过滤更新以来的时间

带撇号的值是上次过滤更新的过滤值。

<table><tr><td>命令</td><td>alpha</td></tr><tr><td>解释</td><td>定义滤波器的 alpha（位置）参数。</td></tr><tr><td>命令</td><td>beta</td></tr><tr><td>解释</td><td>定义滤波器的 beta（速度）参数。</td></tr><tr><td>命令</td><td>gamma</td></tr><tr><td>解释</td><td>定义滤波器的 gamma（加速度）参数。</td></tr><tr><td>命令</td><td>debug</td></tr><tr><td>解释</td><td>输出调试信息。</td></tr></table>

# 4.5.4.3. 卡尔曼滤波器 WSF_KALMAN_FILTER

```txt
filter <name> WSF_KALMAN_FILTER ... Commands ... end_filter 
```

滤波器接受输入位置（来自距离、方位角、仰角或位置测量），并生成对跟踪目标位置和速度的估计，以及状态协方差矩阵。

<table><tr><td>命令</td><td>process_noise_sigmas_XYZ&lt;X-value&gt;&lt;Y-value&gt;&lt;Z-value&gt;</td></tr><tr><td>解释</td><td>定义滤波器在三个方向上的噪声标准差。值是被跟踪平台的实体坐标系(ECS)中的加速度,单位为米每二次方秒(m/s2)。请参阅下文中的“过程噪声推荐值”以获取示例输入。默认值:000</td></tr><tr><td>命令</td><td>process Noise_model [constant Velocity; constant acceleration]</td></tr><tr><td>解释</td><td>选择滤波器的过程噪声模型,可以是基于目标的恒定速度或恒定加速度。默认值:constant velocity</td></tr><tr><td>命令</td><td>debug</td></tr><tr><td>解释</td><td>将调试信息写入标准输出。</td></tr><tr><td>命令</td><td>range measurement sigma&lt;length-value&gt;</td></tr><tr><td>解释</td><td>定义在滤波前应用于测量范围的标准差。注意:通常不需要这个输入。仅在相关轨迹没有范围误差时使用。默认值:0m</td></tr><tr><td>命令</td><td>bearing measurement sigma&lt;长度值&gt;</td></tr><tr><td>解释</td><td>定义在滤波前应用于测量方位的标准差。注意:通常不需要这个输入。仅在相关轨迹没有方位误差时使用。默认值:0deg</td></tr><tr><td>命令</td><td>elevation measurement sigma&lt;长度值&gt;</td></tr><tr><td>解释</td><td>定义在滤波前应用于测量仰角的标准差。</td></tr></table>