```txt
processor Commands ... Platform Part Commands ... sensors ... end Sensors minimum detections message_length ... messagepriority .. end Processor 
```

WSF_TRIMSIM_PROCESSOR 提供了从战区范围参考信息管理模拟（TRIMSIM）和SUPPRESSOR 实现中派生的到达时间差（TDOA）算法。它模拟了参考系统误差对空对地目标数据融合的影响。TDOA算法基于来自各种来源的误差生成目标点在三维空间中的测量误差。这些误差应用于主传感器（传感器块中的第一个传感器）的检测信息。

# Key Points

Primary and Secondary Sensors: 列表中的第一个传感器最初被设置为主传感器，其余的被视为次级传感器。次级传感器由处理器更新，而主传感器自行更新并触发处理器更新给定目标的次级传感器。如果检测目标的传感器数量满足 minimum_detections 标准，则宣布检测并将误差应用于结果轨迹，传感器结果可能不会显示当前的误差，仅轨迹显示。  
SensorRemoval: 如果第一个传感器被移除（无论是通过模拟还是用户），则列表中的下一个传感器将成为主传感器，前提是有足够的传感器可满足 minimum_detections 标准。如果由于可用传感器数量不足而未满足 minimum_detections 标准，则所有传感器将以正常方式运行。  
Passive Sensors: 传感器必须是被动类型。   
Update Interval: update_interval 目前对这种处理器类型不起作用。

# Typical Usage

在典型的构造中，处理器和传感器的设置如下：

```shell
platform_type ...
sensor sensor-1 WSF_ESM_SENSOR
...
# Forward the tracks to 'track_proc'
processor track_proc
end_sensor
sensor sensor-2 WSF_ESM_SENSOR
...
# Forward the tracks to 'track_proc'
processor track_proc
end SENSOR 
```

```txt
processor trimsim_proc WSF_TRIMSIMPROCESSOR   
...   
#Connect to sensors to collect 'interaction' data for processing   
sensors sensor sensor-1 sensor sensor-2   
end Sensors   
end Processor   
#minimum detections required   
minimum detections 2   
endplatform_type 
```

# Commands

sensors … end_sensors: 定义传感器列表。  
sensor <sensor-name>: 指定与处理器在同一平台上的传感器名称。  
platform_sensor <platform-name> <sensor-name>: 指定外部平台上的传感器名称。  
minimum_detections <integer>: 指定传感器列表中传感器所需的最小检测次数，以便主传感器宣布检测。  
message_length <data-size-value>: 指定从图像创建的轨迹消息的逻辑长度。默认值: 0（使用从 message_table 派生的值）  
message_priority <integer-priority>: 指定从图像创建的轨迹消息的优先级。默认值: 0（使用从 message_table 派生的值）

# Script Interface

扩展了 WsfProcessor 脚本类，添加了以下方法：

AddSensor(string aSensorName): 将传感器按名称添加到 WSF_TRIMSIM_PROCESSOR 的传感器列表中。如果省略 aPlatformName，则假定传感器与处理器在同一平台上。  
RemoveSensor(string aSensorName): 从 WSF_TRIMSIM_PROCESSOR 的传感器列表中按名称移除传感器。如果省略 aPlatformName，则假定传感器与处理器在同一平台上。

这些功能和命令帮助在模拟中有效地管理和处理传感器数据，特别是在涉及到达时间差（TDOA）算法的情况下。

# 3.3.46. 未分配消息处理器 WSF_UNCLASS_DISSEMINATE_C2

```txt
processor <name> WSF_UNCLASS_DISSEMINATE_C2 ... WSF_DISSEMINATE_C2 Commands ... end Processor 
```

# 概述

WSF_UNCLASS_DISSEMINATE_C2 是基于 HELIOS 的 GTIQBDisseminateC2Table 算法端口的脚本类。此处理器根据用户指定的标准，将分配、状态、位置和轨迹消息传播到连接的

单元。它旨在与其他 HELIOS 处理器配合使用，以便从这些处理器发送消息。

脚本接口

WSF_UNCLASS_DISSEMINATE_C2 利用了通用脚本接口和 WSF_SCRIPT_PROCESSOR 的功能。

非密级 C2 传播命令

非密级 C^2 传播模型没有增加任何超出 WSF_DISSEMINATE_C2 基类所提供的功能。

说明

该处理器的主要功能是将信息传播到连接的单元，确保信息的分配和状态更新符合用户的要求。它不增加新的功能，而是依赖于其基类 WSF_DISSEMINATE_C2 的现有功能。

# 3.3.47. 上行链路处理器 WSF_UPLINK_PROCESSOR

```txt
processor <name> WSF_UPLINKPROCESSOR  
WSFScriptPROCESSOR Commands ...  
maxweapon_uplinks <integer-value>  
weapon_uplink_path <sensor-name> <comm-name>  
end Processor 
```

概述

WSF_UPLINK_PROCESSOR 是 上 行 链 路 访 问 和 控 制 的 默 认 方 法 。 如 果WSF_TASK_PROCESSOR 或 RIPR 处理器指定了上行链路设置，这些设置实际上会被传递到其平台上的默认上行链路处理器。未来，我们设想会有其他上行链路处理器可用，以不同的方式服务这些上行链路。目前，WSF_UPLINK_PROCESSOR 的唯一操作与 WSF_TASK_PROCESSOR和 RIPR 处理器相匹配。有关各种查询方法和控制方法，请参阅 WsfUplinkProcessor。如果您没有指定上行链路路径（使用 weapon_uplink_path 命令），则所有启动的上行链路将由目标的本地轨迹更新服务。

# 参数说明

max_weapon_uplinks <integer>: 指定 RIPR 代理能够处理的最大活动上行链路数量。

默认值:0，无最大值限制

weapon_uplink_path <sensor-name> <comm-name>: 如果指定了武器上行链路路径，则处理器将通过指定的通信路径使用指定传感器的轨迹更新来支持上行链路，发送到发射武器平台。上行链路可以通过脚本启动和停止，详见 WsfUplinkProcessor。

默认值: 未定义路径

说明

WSF_UPLINK_PROCESSOR 主要用于管理和控制上行链路的访问。它允许用户通过指定路径和最大上行链路数量来配置上行链路的行为。如果没有指定路径，系统将默认使用本地轨迹更新来服务所有上行链路。

# 3.3.48. 多处理器模型 WSF_MULTIRESOLUTION_PROCESSOR

```batch
multiresolution Processor WSF MultiresOLUTION PROCESSOR ... multiresolution processor ...   
end multiresolution processor 
```

概述

multiresolution_processor 定义了一个容器，用于在平台上保存一个或多个处理器（processor）对象，并将选择使用哪个 processor 推迟到运行时。选择 processor 是通过与组件关联的 fidelity 参数来完成的。容器中定义的每个 processor 模型都分配了一个 fidelity_range，在初始化期间根据匹配的 fidelity 设置平台上的 processor。

使用方法

定义新类型: 可以在 platform 或 platform_type 命令之外使用 multiresolution_processor 来定义新类型。

```txt
multiresolution Processor <derived> WSF Multiresolution Processor 
```

```txt
fidelity <real-value>   
[add | edit] model <string-value> fidelity_range <real-value> <real-value> [default] processor [<processor-type>] ... processor-specific commands ... end Processor end_model   
[add | edit] model <string-value> ... Any number of models may be specified ... end_model   
common ... processor-specific commands ... end_common   
endMULTIRESOLUTIONPROCESSOR 
```

实例化对象: 可以在 platform_type 或 platform 实例上实例化一个 multiresolution_processor对象。实例化时需要提供一个名称。

```txt
platform_type ...
multiresolution Processor <name> <type>
    ... multiresolution Processor commands ...
endMULTIRESOLUTIONPROCESSOR
endPLATFORM_TYPE 
```

```txt
platform ... 
```

```txt
add multiresolution Processor <name> <type> ... multiresolution Processor commands ... endMULTIRESOLUTONPROCESSER   
endplatform 
```

修改现有对象: 可以在 platform 实例上修改现有的 multiresolution_processor 对象。

```txt
platform ...
    edit multiresolution Processor <name> <type>
        ... multiresolution Processor commands ...
    endMULTIRESOLUTIONPROCESSOR
endplatform 
```

# 命令

fidelity <real-value>: 定义组件的 fidelity 值，决定在运行时使用哪个 processor。必须在0 到 1 之间（包括 0 和 1）。此值直接映射到模型命令中定义的 fidelity_range。默认值: 1.0  
model <string-value> ... end_model: 定义或编辑包含的 processor 模型，名称由字符串给出。支持隐式添加（或编辑如果命名模型存在）以及使用 add 和 edit 命令的显式添加和编辑。  
注意: 必须至少指定一个模型块。  
fidelity_range <real-value> <real-value>: 定义此模型应使用的 fidelity 值范围。必须在 0到 1 之间（包括 0 和 1），按递增顺序排列，并且不得与此组件上的另一个模型的fidelity_range 重叠。默认值: 0.0 1.0  
default: 如果没有匹配的 fidelity，则使用此模型作为默认选择。  
processor <processor-type> ... end_processor: 定义 processor 模型的类型和特定于此模型实例化的参数。在首次定义新模型时需要 processor，在编辑现有模型时不得指定。  
common ... end_common: 定义要转发到所有当前指定的 processor 模型的通用参数。这些参数必须对所有当前定义的 processor 模型有效。

# 说明

多分辨率分析: 这种方法允许在不同的分辨率下分析和选择合适的 processor 模型，以便在不同的场景中优化处理性能。  
未来改进: 计划在场景文件的其他位置提供 fidelity 选择，以提高此组件的实用性。

# 3.4. 路由器组件 router

# 3.4.1. 公共命令

```rst
router <name-or-type> <base-type-name>
... Platform Part Commands ...
... router_protocol Commands ...
... medium Commands ...
gateway_address <address>
gateway <comm-name> 
```

```txt
hop_limit <integer-value>  
automated_Interface_linking <boolean-value>  
use_default_protocol <boolean-value>  
useMULTicast_protocol <boolean-value>  
end router 
```

注意：medium Commands 在 3.2.1.2 媒介命令 medium Commands。

在 AFSIM 中，路由器对象表示一种设备，它能够确定消息是否可以发送到其目的地，以及消息应该采取哪条路径到达目的地。路由器与同一平台上的通信接口唯一关联，当消息发送和接收时使用该路由器实例。

# 路由器的默认行为

默认情况下，AFSIM 中的每个平台都有一个路由器，除非另有指定，否则所有通信接口将分配给此默认路由器。默认路由器的名称为“default”。如果用户想要覆盖默认路由器设置，只需使用相同的名称“default”定义并分配一个路由器。

# 注意事项

路由器在模拟实例化时必须开启并运行，以支持传统通信行为。

当前不支持最初禁用路由器的命令，但使用 WsfPlatformPart 脚本方法禁用或关闭路由器仍然有效。

所有分配给路由器的通信接口之间的连接被视为桥接，这意味着通信可以在它们之间传递，无论通信模型类型和接收/传输限制如何。

# 3.4.1.1. 路由器协议 router_protocol

```txt
router_protocol <name-or-type> <base-type-name>  
...  
end_ROUTeriaprotocol 
```

路由协议在 AFSIM 中通常在消息的发送和接收过程中被引用。当消息被发送时，查询路由器以确定消息是否可以发送到其目的地，以及消息应该转发（传输）到的路径（特别是下一跳或通信接口）。在接收过程中，路由器的使用有限，但有助于根据消息的目的地确定如何处理消息，以及该目的地是否是接收到消息的通信接口。

路由协议在所有这些操作期间被查询，以便它们可以改变路由器的正常消息处理，并收集特定于所使用协议的内部数据。

例如，多播协议允许正确识别具有多播地址目的地的消息，并允许路由器正确识别应使用哪些可用接口将多播消息转发给其他接收者。因此，这种特定协议可能导致从单个消息接收传输单个或多个消息，这不是典型的路由器行为。

在任何给定的路由器实例上，只应存在任何类型的路由协议的一个实例。

AFSIM默认使用几种路由协议来启用消息路由和多播功能。有关更多详细信息，请参阅预定义的路由协议类型。

# 示例配置

以下是一个示例路由协议配置：

```txt
router_protocol myProtocol BaseProtocol #在这里添加特定于协议的命令 end_ROUTer_protocol
```

添加路由协议到路由器

```txt
add router_protocol myProtocol BaseProtocol #在这里添加特定于协议的命令 end router_protocol 
```

编辑现有路由协议

```txt
edit router_protocol myProtocol
# 在这里编辑特定于协议的命令
end router_protocol
```

删除路由协议

```txt
delete router_protocol myProtocol end router_protocol 
```

已经实现的几种路由器协议如下：

3.4.1.1.1. 通用路由协议模型 WSF_COMM_ROUTER_PROTOCOL_AD_HOC  
```perl
router_protocol <name> WSFCOMM_ROUTER_PROTOCOL_AD_HOC comm-added_delay_time <random-time-reference> comm Removed_delay_time <random-time-reference> connection-added_delay_time <random-time-reference> connection Removed_delay_time <random-time-reference> script bool OnCommAdded ... script bool OnCommRemoved ... script bool OnConnectionAdded ... script bool OnConnectionRemoved ... script WsfAddress OnMessageRouting ...   
end_ROUTer_protocol 
```

WSF_COMM_ROUTER_PROTOCOL_AD_HOC 是一个通用的路由协议，提供用户定义的脚本方法来定义路由协议的行为。该协议允许用户定义在网络状态变化时反映在路由器中维护的网络知识的行为。尽管设计初衷是为了实现临时（ad-hoc）网络功能，但它也可以用于任何用户希望通过脚本界面定义自己的路由调用实现的场景。

限制 出于实际和性能原因，该协议仅考虑分配给路由器的通信接口的网络成员变化。外部网络的变化不在此协议的考虑范围内。

运行时变化 在协议感兴趣的网络之一发生变化时，将调用相应的脚本方法以允许用户定义的逻辑执行，并返回相应的值以指示对该事件的操作。

时间延迟 该协议为其监控的大多数事件提供时间延迟，以允许状态更新中的常数或基

于分布的延迟。这是为了模拟由于典型网络延迟效应、特定协议分发数据的延迟等导致路由器获取这些事件通知的潜在延迟。

注意 如果该协议监控的网络包含许多成员，或同时在模拟中存在许多具有此协议的路由器，则该协议可能会对性能产生影响。

<table><tr><td>命令</td><td>comm-added_delay_time &lt;random-time-reference&gt;</td></tr><tr><td>解释</td><td>定义了在监控网络添加通信接口和协议执行OnCommAdded脚本方法（可能将接口添加到网络状态图）之间的延迟。默认值：无延迟（常数0秒）</td></tr><tr><td>命令</td><td>comm_Removed_delay_time &lt;random-time-reference&gt;</td></tr><tr><td>解释</td><td>定义了在监控网络移除通信接口和协议执行OnCommRemoved脚本方法（可能将接口从网络状态图中移除）之间的延迟。默认值：无延迟（常数0秒）</td></tr><tr><td>命令</td><td>connection-added_delay_time &lt;random-time-reference&gt;</td></tr><tr><td>解释</td><td>定义了在监控网络添加连接和协议执行OnConnectionAdded脚本方法（可能将连接添加到网络状态图）之间的延迟。默认值：无延迟（常数0秒）</td></tr><tr><td>命令</td><td>connection_Removed_delay_time &lt;random-time-reference&gt;</td></tr><tr><td>解释</td><td>定义了在监控网络移除连接和协议执行OnConnectionRemoved脚本方法（可能将连接从网络状态图中移除）之间的延迟。默认值：无延迟（常数0秒）</td></tr></table>

以下是相关脚本：  

<table><tr><td>脚本</td><td>script bool OnCommAdded(WsfAddress aAddedComm, WsfCommGraph aNetworkState, WsfCommRouter aRouter) 
... 
end_script</td></tr><tr><td>功能</td><td>定义了在添加通信接口时（延迟后）调用的可选脚本。只有当被添加的接口与该协议所属路由器的某个接口共享网络或直接与某个路由器接口相关时才会调用此脚本。脚本必须返回一个布尔值，指示协议是否应将该接口添加到其网络状态图（true）或不采取任何操作（false）。</td></tr><tr><td>脚本</td><td>script bool OnCommRemoved(WsfAddress aAddedComm, WsfCommGraph aNetworkState, WsfCommRouter aRouter) 
... 
end_script</td></tr><tr><td>功能</td><td>定义了在移除通信接口时（延迟后）调用的可选脚本。只有当被移除的接口与该协议所属路由器的某个接口共享网络或直接与某个路由器接口相关时才会调用此脚本。脚本必须返回一个布尔值，指示协议是否应将该接口从其网络状态图中移除（true）或不采取任何操作（false）。</td></tr><tr><td>脚本</td><td>script bool OnConnectionAdded(WsfAddress aSourceComm, WsfAddress aDestinationComm, WsfCommGraph aNetworkState, WsfCommRouter aRouter) 
... 
end_script</td></tr><tr><td>功能</td><td>定义了在添加连接时（延迟后）调用的可选脚本。只有当涉及的接口（源或目的地之一）与该协议所属路由器的某个接口共享网络时才会调用此脚本。脚本必须返回一个布尔值，指示协议是否应将该连接添加到其网络状态图（true）或不采取任何操作（false）。</td></tr><tr><td>脚本</td><td>script bool OnConnectionRemoved(WsfAddress aSourceComm, WsfAddress aDestinationComm, WsfCommGraph aNetworkState, WsfCommRouter aRouter) 
... 
end_script</td></tr><tr><td></td><td></td></tr><tr><td>功能</td><td>定义了在移除连接时（延迟后）调用的可选脚本。只有当涉及的接口（源或目的地之一）与该协议所属路由器的某个接口共享网络时才会调用此脚本。脚本必须返回一个布尔值，指示协议是否应将该连接从其网络状态图中移除（true）或不采取任何操作（false）。</td></tr><tr><td>脚本</td><td>script WsfAddress OnMessageRouting(WsfCommMessage aMessage, WsfAddress alInterface, WsfCommGraph aNetworkState, WsfCommRouter aRouter)…end_script</td></tr><tr><td>功能</td><td>定义了在消息需要在属于该协议的路由器接口上进行路由时立即调用的可选脚本。脚本必须返回一个 WsfAddress，指示转发此消息的下一跳地址。如果提供了空地址（未设置返回对象的地址），则表示此协议应丢弃消息而不尝试转发消息。任何其他地址将用作指示的转发地址，并且必须直接连接到接收消息的接口（通过 alInterface 参数提供）。注意 脚本提供了许多详细信息以进行大多数路由决策，包括直接从消息本身提供的信息（如traceroute、目的地址等）、当前图状态（路径）和路由器本身。</td></tr></table>

# 3.4.1.1.2. 基本路由协议 WSF_COMM_ROUTER_PROTOCOL_LEGACY

```c
router_protocol <name> WSFCOMM_ROUTER_PROTOCOL_LEGACY end routers_protocol 
```

介绍 WSF_COMM_ROUTER_PROTOCOL_LEGACY 提供了在以前版本的 AFSIM 中存在的通用路由功能。默认情况下，它会被添加到 AFSIM 中的每个路由器实例中。默认情况下，该路由协议基于模拟提供的真实数据工作，因此路由器可以使用到达目的地的任何实际路径，或者在电磁通信（如无线电）情况下，目的地是已知的以便发送消息。

输入 目前，该协议没有额外的输入。

建议 强烈建议如果使用更强大的路由协议，应从任何通信中移除此协议，因为任何复杂且有限的路由协议的路由失败仍会成功，因为如果所有其他协议都失败，将查询旧版协议进行路由。

注意 如果使用更复杂的路由协议，建议移除此协议，以避免在其他协议失败时旧版协议仍然被查询，从而导致路由成功。

# 主要功能和特点

默认添加：WSF_COMM_ROUTER_PROTOCOL_LEGACY 默认添加到每个 AFSIM 路由器实例中。

基于真实数据：该协议基于模拟提供的真实数据工作，确保任何实际路径都可以被路由器使用。

无额外输入：目前，该协议没有额外的输入要求。

兼容性建议：建议在使用更复杂的路由协议时移除此协议，以避免在其他协议失败时旧版协议仍然被查询。

通过这种方式，WSF_COMM_ROUTER_PROTOCOL_LEGACY 提供了一种简单且可靠的路由机制，确保在没有其他复杂路由协议的情况下，路由器仍然能够有效地进行数据传输。

# 3.4.1.1.3. RIPv2 路由协议 WSF_COMM_ROUTER_PROTOCOL_RIPv2

```txt
router_protocol <name> WSFCOMM_ROUTER_PROTOCOL_RIPv2 update_interval <time-value> invalidation_timeout <time-value> 
```

```txt
garbage.collection_timeout <time-value>  
poisoned_reverse <boolean-value>  
end router_protocol 
```

WSF_COMM_ROUTER_PROTOCOL_RIPv2 是一种基于 Bellman-Ford 算法的路由协议，用于通信对象路由器确定何时向其他路由器提供更新，并确定通过 AFSIM 通信框架发送的消息的路由路径。RIPv2 设计用于直径不超过 15 的网络。

与所有路由协议一样，使用此对象仅与感知/动态路由相关。

注意：此协议处于测试版状态。此版本可能存在错误或其他问题。

<table><tr><td>命令</td><td>update_interval &lt;time-value&gt;</td></tr><tr><td>解释</td><td>指定路由器向其他路由器发送更新的频率。根据RIPv2规范（RFC 2543）的规定，这是基准时间。每次安排更新时，时间可以变化±5秒。默认值：30秒</td></tr><tr><td>命令</td><td>invalidation_timeout &lt;time-value&gt;</td></tr><tr><td>解释</td><td>路由被标记为不活动之前必须经过的时间。一旦路由器在此时间内没有收到消息，从该路由器学到的路由将被标记为不活动。默认值：180秒</td></tr><tr><td>命令</td><td>garbageCollection_timeout &lt;time-value&gt;</td></tr><tr><td>解释</td><td>一旦路由被标记为不活动，它将从路由表中清除的时间。默认值：120秒</td></tr><tr><td>命令</td><td>poisoned_reverse &lt;boolean-value&gt;</td></tr><tr><td>解释</td><td>指定是否使用分割水平或带有毒性反转的分割水平。分割水平是一种避免向从中学到路由的路由器发送更新的方案。毒性反转将这些路由包含在更新中，但将其度量设置为不可用。默认值：开启</td></tr></table>

# 3.4.1.1.4. OSPF 路由协议 WSF_COMM_ROUTER_PROTOCOL_OSPF

```perl
router_protocol <name> WSFCOMM_ROUTER_PROTOCOL OSPF ospf_area <address> remove ospf_area <address> backbone <address> remove backbone ospf_br_priority <integer-value> hello_interval <random-time-reference> hold_timer <random-time-reference>   
end_ROUTer_protocol 
```

WSF_COMM_ROUTER_PROTOCOL_OSPF 提供了类似于 OSPF 协议的通用任务级路由功能。此协议支持将路由器分配到“区域”，在这些区域中保持详细的路由信息，同时在其他区域中仅携带潜在接收者数据的摘要级别的详细信息。

该协议通过周期性发送由此协议的其他成员接收的多播消息来工作。这用于动态检测新成员，并检测其他成员的丢失。数据在区域内分发，并且以这种格式传输到外部。此消息传递过程在其实现中是抽象的。

在路由消息时，如果接收者在本地区域，消息将使用区域网络状态图直接路由到该成员。如果接收者已知但在区域外，则此协议始终尝试将消息发送到定义的“骨干”区域。骨干区域将消息转发到任何区域，所有区域必须连接到骨干区域。

区域连接通过将某些通信定义为“边界路由器”来处理。用户必须通过在协议输入中提供多个区域定义来指定这些路由器。

每个连接的 OSPF 自治系统（AS）只能存在一个骨干。所有区域必须连接到该区域。

对于发送到 OSPF 启用路由器外部的消息，必须有一个或多个路由器共享与所需外部接口的连接，并且必须具有可用的替代路由协议以正确处理这些消息的外部路由。因此，任何具有非 OSPF 路由协议的 OSPF 启用路由器都被指定为 ASBR（自治系统边界路由器），可以将消息发送到 OSPFAS 外部。发送到 OSPF 外部的消息使用 ASBR 的最佳外部路径选择最佳的 ASBR，然后使用标准 OSPF 路由策略内部路由到该 ASBR。

并非所有网络拓扑都兼容 OSPF。所有区域成员必须连接。边界路由器的丢失将导致传输能力的丧失，这是此协议的预期。此外，尽管可能存在外部于 OSPF 提供定义的连接，但此协议不会使用这些连接来“绕过”任何丢失的边界路由器，这是其意图。

最后，OSPF 通常使用基于发送消息时可用的多个接口的传输能力的度量来做出路由决策。此度量由任何给定路由的传输速率除以 100Mbps 定义，最小值为 1.0。唯一小于 1.0的度量值是瞬时传输速率，在确定成本时使用度量值 0.0。

注意：此协议处于测试版状态。此版本可能存在错误或其他问题。 注意：此协议对模拟性能的要求极高。强烈建议将 hello_interval 时间增加到可接受的最高值，以避免在每个间隔发送大量多播消息，并避免将大量通信分配给任何特定区域。

<table><tr><td>命令</td><td>ospf_area &lt;address&gt;</td></tr><tr><td>解释</td><td>定义此通信/路由器在 OSPF AS 中所属的区域。如果此成员具有与该区域中另一个成员的直接连接,可以分配多个区域,将此成员定义为“边界路由器”。</td></tr><tr><td>命令</td><td>remove ospf area &lt;address&gt;</td></tr><tr><td>解释</td><td>从此协议中移除定义的区域。专门用于编辑输入中的派生对象。</td></tr><tr><td>命令</td><td>backbone &lt;address&gt;</td></tr><tr><td>解释</td><td>定义指定的区域为骨干区域。此设置只需要在一个协议实例上完成,即可应用于整个 OSPF 连接的 AS。每个连接的 OSPF AS 只能定义一个骨干。所有其他区域必须通过边界路由器连接到此区域。</td></tr><tr><td>命令</td><td>remove backbone</td></tr><tr><td>解释</td><td>此命令移除此协议类型或实例的骨干指定。在从继承的协议类型中不需要指定的骨干设置时使用。</td></tr><tr><td>命令</td><td>ospf drpriority &lt;integer-value&gt;</td></tr><tr><td>解释</td><td>设置此路由器成为其网络中“指定路由器”或“备份指定路由器”(DR,BDR)的优先级。这些路由器持有特定区域的所有详细路由数据,作为同一网络中所有其他路由器的公共通信点。此值必须为正数,较低的值表示较高的优先级。此值还会影响这些路由器在运行时的动态重新选择。任何进入网络和区域的路由器不会抢占任何已经建立的 DR 或 BDR,即使它具有更高的优先级。默认最大整数值。</td></tr><tr><td>命令</td><td>hello_interval &lt;random-time-reference&gt;</td></tr><tr><td>解释</td><td>定义发送 OSPF 心跳(“hello” 数据包)之间的时间。如果在定义的保持时间内未收到这些数据包,则路由器将被视为未连接或不可用,并从路由状态数据中移除。此外,这还定义了检测新成员的时间,因为这是检测新成员的方法。此值将增加一个小值,以确保这些时间在模拟中不完全相同,并确保当此值为常量时的可重复性。默认常量 10 秒。</td></tr><tr><td>命令</td><td>hold_timer &lt;random-time-reference&gt;</td></tr><tr><td>解释</td><td>定义在未收到 hello 数据包之前的时间。请注意,默认值允许在实际上由于保持时间而被删除之前传输多个 hello 数据包窗口。确保此值大于 hello_interval 以避免从网络状态知识中删除所有成员。此值将增加一个小值,以确保这些时间在模拟中不完全相同,并确保当此值为常量时的可重复性。</td></tr></table>

# 3.4.1.1.5. 多播路由协议 WSF_COMM_ROUTER_PROTOCOL_MULTICAST

```batch
router_protocol <name> WSFCOMM_ROUTER_PROTOCOL Multicast end routers_protocol 
```

WSF_COMM_ROUTER_PROTOCOL_MULTICAST 提供了用于多播消息的通用路由功能。具体来说，该协议允许解析多播消息到预期的接收者，并确保消息仅在必要时转发和/或复制，以到达所有潜在接收者。

此协议是一个路由器协议，但不是传统意义上的路由协议。该协议不提供针对预期多播组成员的路由逻辑，而是依赖于路由器上存在的其他协议来提供消息的路由。因此，仅此协议本身必须在路由器上存在另一个协议，否则多播消息传输将不会成功。

还需要注意的是，此协议允许发送多播消息，但不提供接收功能。任何希望接收多播消息 的 接 口 也 必 须 具 有 识 别 和 接 受 多 播 消 息 的 方 法 ， 例 如 通 过 通 信 协 议WSF_COMM_PROTOCOL_IGMP 提供的那些方法。

此协议目前没有其他输入。

注意事项

依赖性：此协议本身不提供路由逻辑，必须依赖其他协议来实现多播消息的路由。

发送功能：此协议允许发送多播消息，但不提供接收功能。接收多播消息需要额外的协议支持，如 WSF_COMM_PROTOCOL_IGMP。

性能影响：多播消息的处理可能会对网络性能产生影响，特别是在大量多播消息的情况下。

# 3.4.1.2. 公共命令参数

所有的路由器设备都有的公共参数：

<table><tr><td>命令</td><td>gateway_address &lt;address&gt;</td></tr><tr><td>解释</td><td>如果提供,定义与此路由器关联的特定接口,当路由器无法找到消息的目的地时,应使用该接口转发消息。所选通信网关的目的地在通信接口本身上定义。此命令提供了静态地址替代方案给 gateway 命令,并且在任何给定的路由器上只能使用这两个命令之一。默认值:无网关地址指定或使用。</td></tr><tr><td>命令</td><td>gateway &lt;comm-name&gt;</td></tr><tr><td>解释</td><td>如果提供,定义与此路由器关联的特定接口,当路由器无法找到消息的目的地时,应使用该接口转发消息。所选通信网关的目的地在通信接口本身上定义。此命令提供了动态地址替代方案给 gateway address 命令,并且在任何给定的路由器上只能使用这两个命令之一。默认值:无网关指定或使用。</td></tr><tr><td>命令</td><td>hop_limit &lt;integer&gt;</td></tr><tr><td>解释</td><td>指定消息在到达目的地之前可以访问的节点/通信接口的数量,然后消息将被丢弃。通常称为生存时间(TTL)。hop_limit 适用于从此路由器的接口发起的任何消息。此值确保进入循环路由的消息最终会被丢弃。默认值:64</td></tr><tr><td>命令</td><td>automated-interface_linking &lt;boolean-value&gt;</td></tr><tr><td>解释</td><td>如果设置为 true,所有为此路由器指定的接口之间将创建连接。这确保路由器接口通过路由器硬件接口直接连接。如果设置为 false,则不会在成员之间自动创建连接,并且从路由器上的任何特定接口发送或接收的消息可能无法到达同一路由器上的另一个接口。</td></tr><tr><td></td><td>警告:某些网络类型与automated/interface_linking不兼容,如果网络拓扑会被违反,用户不应启用此设置。默认值:false</td></tr><tr><td>命令</td><td>use_default_protocolboolean-value&gt;</td></tr><tr><td>解释</td><td>一个方便的设置,用于确定路由器是否应使用默认的传统路由协议。true表示使用此routing_protocol,false表示移除它。默认值:true</td></tr><tr><td>命令</td><td>useMULTicast_protocolboolean-value&gt;</td></tr><tr><td>解释</td><td>一个方便的设置,用于确定路由器是否应使用默认的多播路由协议。true表示使用此routing_protocol,false表示移除它。默认值:true</td></tr></table>

# 3.4.2. 基础路由模型 WSF_COMM_ROUTER

WSF_COMM_ROUTER 提供了核心 AFSIM 的基础路由器模型。除了通过路由器输入提供的命令外，它没有其他附加命令。

有关 AFSIM 中通信框架的更多详细信息，请参阅《Communications Primer》。

# 3.5. 传感器组件 sensor

```tcl
sensor <name> <base-type-name>
... Platform Part Commands ...
... Articulated Part Commands ...
... Common Script Interface ...
ignore <category-name>
ignore_domain [land | air | surface | subsurface | space ]
ignore_side <side>
ignore_same_side
ignore Nothing
message_length <data-size-value>
messagepriority <integer-priority>
modifier_category <category-name>
mode_template ... end_mode_template
mode <mode-name> ... end_mode
selection_mode [single | multiple ]
initial_mode <mode-name>
mode_select_delay <time-value>
script bool OnSensorDetectionAttempt ...
Filter Commands ...
Common Mode Commands ...
Detection Scheduling Commands ...
Track Formation Commands ...
Track Information Reporting Commands ...
...
sensor-specific mode commands ...
end_sensor 
```

```txt
Multiple mode sensor definition   
sensor<name><base-type-name> ... Platform Part Commands ... ... Articulated Part Commands ... Commands ... mode_template Common Mode Commands ... Filter Commands ... sensor-specific mode commands ... end_mode_template mode<mode-name-1> Common Mode Commands ... Filter Commands ... sensor-specific mode commands ... end_mode additional mode definitions end_sensor 
```

# 传感器概述

传感器是一种设备，能够让一个平台检测其他平台或其组成部分。它们在现代技术中扮演着重要角色，广泛应用于各种系统中，如报警系统、自动门和玩具等。

# 多模式考虑

大多数传感器支持“模式”的概念。模式是传感器的一组命名操作特性。虽然不必使用多种模式，但如果传感器实现支持模式且未定义明确的模式，则任何与模式相关的命令都假定属于隐式定义的名为“default”的模式。

模式模板（mode_template）：如果要使用多种模式，可以定义一个“模式模板”，指定所有模式之间的共同特性。虽然不必定义“模式模板”，但如果使用它，必须在第一个“mode”命令之前定义。如果使用“模式模板”，每个模式的初始配置将从“模式模板”复制，然后任何添加或修改应出现在相关的“mode”和“end_mode”命令之间。

当前支持的传感器有：

WSF_COMPOSITE_SENSOR

由其他传感器组成的复合传感器。

WSF_GEOMETRIC_SENSOR

纯粹基于几何学的基础传感器。

WSF_PASSIVE_SENSOR

基础的被动射频（RF）检测传感器。

WSF_RADAR_SENSOR

基础雷达模型。

WSF_SOSM_SENSOR

用于光谱光学（红外）传感模型（SOSM）的接口。

WSF_ACOUSTIC_SENSOR

基础声学传感器模型。

WSF_BEAM_DIRECTOR

用于获取非常精细的跟踪的传感器，能够进行发射。

WSF_EOIR_SENSOR

电光/红外（EOIR）传感器模型。

WSF_ESM_SENSOR

基础的被动射频（RF）检测传感器。

WSF_IRST_SENSOR

基础红外搜索与跟踪传感器。

WSF_LADAR_SENSOR

基础激光雷达（LADAR）传感器。

WSF_OPTICAL_SENSOR

基础光学传感器模型。

WSF_OTH_RADAR_SENSOR

基础的超视距反向散射（OTH-B）天波雷达模型。

WSF_SAR_SENSOR

基础合成孔径雷达（SAR）模型。

WSF_SURFACE_WAVE_RADAR_SENSOR

超视距雷达表面波传感器模型。

# 3.5.1. 公共命令 sensor commands

大多数传感器都会使用到的公共命令。

# 3.5.1.1. 基础命令 Commands

忽略命令

ignore <category-name>

指示传感器忽略对属于指定类别的对象的检测尝试。可以多次指定此命令以忽略多个类别。

ignore_domain [ land | air | surface | subsurface | space ]

指示传感器忽略对属于指定空间域的平台或平台上对象的检测尝试。可以多次指定此命令以忽略多个域。

ignore_side <side>

指示传感器忽略对属于指定侧的平台或平台上对象的检测尝试。可以多次指定此命令以忽略多个侧。

ignore_same_side

指示传感器忽略对与传感器附着的平台在同一侧的平台或平台上对象的检测尝试。

ignore_nothing

取消任何先前的 ignore、ignore_domain、ignore_side 和 ignore_same_side 命令的效果。

这对于希望重用带有嵌入式“忽略”命令的传感器定义但希望消除或更改忽略内容的情况非常有用。

消息命令

message_length <data-size-value>

指定从传感器创建的跟踪消息的逻辑长度。此命令可在传感器级别和传感器模式级别使用。

message_priority <integer-priority>

指定从传感器创建的跟踪消息的优先级。此命令可在传感器级别和传感器模式级别使用。

模式相关命令

modifier_category <category-name>

映射到 zone_set 中定义的基于区域的衰减值的类别。设置此值告诉传感器评估区域的衰减。

mode_template … end_mode_template

定义传感器模式的默认值。当定义新模式时，首先用模式模板中的值填充。这在传感器有多个模式且每个模式的参数相同但只有少数值不同的情况下非常有用。

mode <mode-name> … end_mode

定义一个模式，即一组选定的参数。模式的初始或默认值由 mode_template（如果提供）定义。

selection_mode [ single | multiple ]

指示传感器是否支持多模式的同时操作。默认值为 single。

initial_mode <mode-name>

此命令的操作取决于 selection_mode 是 single 还是 multiple。

如果 selection_mode 是 single，则定义传感器首次打开时选择的模式。

如果 selection_mode 是 multiple，则定义传感器从“关闭”状态变为“打开”状态时选择的模式。

mode_select_delay <time-value>

指定选择模式时的延迟。此输入仅对 WSF_AGILITY_EFFECT 模式更改功能有效。默认值为 0.0 秒。

脚本命令

OnSensorDetectionAttempt

定义一个可选脚本，为传感器模型施加额外的检测约束。此脚本在检测尝试发生后立即调用，但在观察者中的任何 SENSOR_DETECTION_ATTEMPT 事件之前调用。脚本必须返回一个布尔值，指示传感器检测是否应被接受或拒绝。

# 3.5.1.2. 模式特定命令 Common Mode Commands

required_pd (0..1)

指定常数“required_pd”值，如果全局模拟命令 use_constant_required_pd 被指定为 true，则使用此值。适用于实现概率检测器的传感器（例如，WSF_RADAR_SENSOR 中的可选

Marcum-Swerling 检测器）。默认值为 0.5。

cue_mode [ fixed | azimuth | elevation | both | azimuth_and_elevation]

此命令与 azimuth_cue_limits 和 elevation_cue_limits 一起使用，可以限制特定模式的提示能力，使其小于由关节部件定义的能力。

fixed- 传感器不能被提示。

azimuth- 传感器只能在方位角上被提示。

elevation- 传感器只能在仰角上被提示。

both 或 azimuth_and_elevation - 系统可以在方位角和仰角上被提示。

默认值由关节部件中的 slew_mode 命令定义。

azimuth_cue_limits <angle-value> <angle-value>

指定传感器在方位角上可以被提示的最小和最大角度。这些值仅在 cue_mode 为azimuth 或 both 时适用。默认值由关节部件中的 azimuth_slew_limits 命令定义。

elevation_cue_limits <angle-value> <angle-value>

指定传感器在仰角上可以被提示的最小和最大角度。这些值仅在 cue_mode 为elevation 或 both 时适用。默认值由关节部件中的 elevation_slew_limits 命令定义。

azimuth_cue_rate <angle-rate-value>   
elevation_cue_rate <angle-rate-value>

指定在满足提示请求时使用的角速度。主要用于建模跟踪单个目标的系统，不用于扫描系统，也不应用于多目标跟踪系统。值必须大于零，且大于或等于 $1 . 0 5 { \div } 1 2 ~ { \mathsf { d e g } } / { \mathsf { s e c } }$ 的值将被视为“无限”。默认值由关节部件中的 azimuth_slew_rate 和 elevation_slew_rate 命令定义。error_model <derived-name>

error_model <base-name> …commands… end_error_model

指定错误模型。有关可用错误效果和如何配置模型的更多信息，请参见 error_model。

solar_exclusion_angle <angle-value>

如果传感器的视线与太阳边缘和目标之间的角度小于此值，则传感器不会检测目标。默认无太阳排除。

lunar_exclusion_angle <angle-value>

如果传感器的视线与月亮边缘和目标之间的角度小于此值，则传感器不会检测目标。默认无月亮排除。

target_solar_illumination_angle <angle-value> <angle-value>

定义目标被检测所需的太阳照明角度范围。仅适用于被动红外传感器和被动视觉传感器，以及 WSF_GEOMETRIC_SENSOR。

solar_elevation_at_target <angle-value> <angle-value>

定义目标位置所需的太阳仰角范围，以便目标被检测。仅适用于被动红外传感器和被动视觉传感器，以及 WSF_GEOMETRIC_SENSOR。

enable_moon_los_block <boolean-value>

如果设置为 true，则传感器不会检测视线被月亮阻挡的目标。默认值为 false。

# 3.5.1.3. 调度相关命令 Detection Scheduling Commands

update_interval <time-value>

当调度器被分配为 physical_scan 或 sector_scan 类型时，此值是必需的。它与传感器输入文件中读取的最终模式中定义的 frame_time 值结合使用，以计算并物理扫描雷达检测的扇区。例如，如果最终 frame_time 值设置为 20 秒，而 update_interval 设置为 2 秒，则需要 10 个扇区在 20 秒的帧内扫描 360 度。每个扇区将在每个 2 秒的 update_interval 内覆

盖 36 度的方位角。

注意：此关键字应放置在 sensor-end_sensor 块内，而不是模式块内。

frame_time <time-value>

指定传感器执行一次搜索体积扫描所需的时间。此参数的实际使用取决于传感器的具体实现，也表示传感器检测报告的频率。

maximum_request_count <integer>

如果此值大于零，则此模式仅响应由 WsfTaskManager::StartTracking 发起的显式请求。

revisit_time <time-value>

如果 maximum_request_count 非零，则指定请求应重新访问的频率。

dwell_time <time-value>

如果 maximum_request_count 非零，则指定传感器将停留或执行与请求相关的检测尝试的时间。

search_while_track

如果 maximum_request_count 非零，则表示搜索模式请求可以继续处理。

disables_search

如果 maximum_request_count 非零，则表示如果选择此模式，则任何搜索模式的检测尝试将被阻止。

scheduler <scheduler-type> end_scheduler

定义调度器类型。可用的调度器类型包括：

default   
physical_scan   
sector_scan   
spin   
debug_scheduler：启用调度器数据的控制台窗口输出。注意：此关键字在WSF_COMPOSITE_SENSOR 定义块中不起作用，但在用于 WSF_COMPOSITE_SENSOR的组成传感器中，当组件传感器相同时可以工作。

# 3.5.1.3.1. 默认调度器 default

```txt
schedule default  
    scan_scheduling ...  
end_schedule 
```

在 AFSIM 中，默认传感器调度器用于均匀分配检测机会，基于目标的总数在帧时间内进行分配。以下是与默认调度器相关的命令及其功能：

scheduler default

使用默认传感器调度器。检测机会在帧时间内根据目标总数均匀分布。

scan_scheduling [random | input_order | reverse_input_order]

指定在使用默认传感器调度器时，新平台如何被添加到扫描调度队列中：

random- 新平台随机添加到列表中。

input_order- 新平台添加到队列的末尾。这意味着传感器将按照平台在输入文件中出现的顺序对其进行检测尝试。

reverse_input_order- 新平台添加到队列的前面。这意味着传感器将按照平台在输入文件中出现的逆序对其进行检测尝试。

默认值为 random。

# 3.5.1.3.2. 物理扫描调度器 physical_scan

```txt
schedule physical_scan initial Heading ... end_scheduler 
```

使用物理扫描调度器。检测机会沿着扫描角度进行。这种选项适用于使用单一模式的360 度监视雷达。基础方法将 360 度扇区划分为更小的扇区。这些更小的扇区基于update_interval 关键字以及从传感器输入文件中读取的最终模式中定义的 frame_time 值。扇区在初始化时设置，并且不会因模式更改而修改。移动的扇区仅用于地理筛选目标集以进行检测事件。扇区从随机方向开始顺时针扫描，除非提供了 initial_heading。

initial_heading <angle-value>

指定传感器开始扫描的初始方向。如果未指定，则选择一个随机值。

默认值为无（随机化）。

# 3.5.1.3.3. 扇区扫描调度器 sector_scan

```txt
schedule sector_scan frame_based_scheduler <boolean-value> sector ... end sector end_scheduler 
```

在 AFSIM 中，扇区扫描调度器用于提供比默认调度器更符合时间要求的检测目标选择功能。它适用于机械扫描传感器（如抛物面天线雷达、望远镜等）的表示。以下是与扇区扫描调度器相关的命令及其功能：

使用扇区扫描调度器。允许在方位角、仰角或同时在方位角和仰角中定义扫描“扇区”。这使得可以定义多条雷达扫描或光学传感器的扫描模式。

frame_based_scheduling <boolean-value>

非成像传感器默认执行基于帧的扇区扫描调度。此默认行为仅为所有扇区中的每个目标提供一次检测机会（或每帧一次检测机会）。要覆盖非成像传感器的基于帧的调度，请将此命令设置为 false。此命令不适用于成像传感器。

默认值为 true（适用于非成像传感器）。

sector … end_sector

定义扫描扇区的命令块。可以指定多个扇区，每个扇区可以有不同的扫描参数。

```txt
sector  
type ...  
start_azimuth ...  
end_azimuth ...  
start_elevation ...  
end_elevation ...  
azimuth ...  
elevation ...  
azimuth_rate ...  
elevation_rate ...  
azimuth_scan_direction ...  
end sector 
```

扇区命令 Sector Commands

type [azimuth | elevation | azimuth_and_elevation]指定扇区的类型。

azimuth- 扇区仅在方位角上实现扫描，仰角固定。  
elevation - 扇区仅在仰角上实现扫描，方位角固定。  
azimuth_and_elevation - 扇区在方位角和仰角上提供扫描。

start_azimuth <angle-value>

定义方位角或方位角和仰角扫描扇区的起始方位角。允许的值范围为-180.0度到180度。

end_azimuth <angle-value>

```txt
sector type azimuth_and_elevation start_azimuth 0 deg end_azimuth 90 deg start_elevation 0 deg end_elevation 80 deg   
end sector 
```

定义方位角或方位角和仰角扫描扇区的结束方位角。允许的值范围为-180.0度到180度。

start_elevation <angle-value>

定义仰角或方位角和仰角扫描扇区的起始仰角。允许的值范围为-90.0 度到 90 度。

end_elevation <angle-value>

定义仰角或方位角和仰角扫描扇区的结束仰角。允许的值范围为-90.0 度到 90 度。

azimuth <angle-value>

在仰角扫描中指定固定方位角。

```txt
sector type elevation azimuth 40 deg start_elevation 0 deg end_elevation 40 deg end sector 
```

elevation <angle-value> 在方位角扫描中指定固

```txt
sector type azimuth start_azimuth 0 deg end_azimuth 40 deg elevation 0 deg   
end sector 
```

azimuth_rate <angular-speed-units>

指定用于方位角或方位角和仰角扫描扇区的方位角速率值。必须为每个扇区定义azimuth_rate，或者定义传感器的回转速率，否则会发生初始化错误。

elevation_rate <angular-speed-units>

指定用于仰角或方位角和仰角扫描扇区的仰角速率值。必须为每个扇区定义elevation_rate，或者定义传感器的回转速率，否则会发生初始化错误。

azimuth_scan_direction [positive | negative]

定义方位角和方位角和仰角扇区类型的方位角扫描方向，可以是正方向（顺时针）或负方向（逆时针）。

默认方向由 start_azimuth 和 end_azimuth 角度决定，从起始角度向结束角度前进。

# 3.5.1.3.4. 旋转调度器 spin

```matlab
schedule spin  
    scan_period ...  
    clockwise ...  
    starting_beam_azimuth ...  
    starting_azimuth_randomized ...  
end_schedule 
```

SpinScheduler 提供了一种传感器扫描功能，旨在以时间上准确的方式模拟旋转雷达系统的行为。在 Mystic 中没有明显的传感器波束扫描或移动，因为 spinscheduler 假定它所调度的传感器具有 360 度的视野。调度器会尝试将对移动目标的探测安排在传感器波束将与目标未来位置相交的时间点。前提是可以准确预测目标的未来位置，最多可以提前一个scan_period 的时间。

scan_period <time-value>

指定传感器完成一次完整旋转所需的时间。

默认值： 10 秒

1 clockwise <boolean-value>

指定传感器是顺时针扫描还是逆时针扫描。值为 true 表示顺时针扫描，值为 false 表示逆时针扫描。

默认值： true

starting_beam_azimuth <angle-value>

指定传感器扫描的起始角度。此角度相对于传感器部件坐标系的 $+ { \sf X }$ 轴。

默认值： 0 度

starting_azimuth_randomized <boolean-value>

指定传感器扫描的起始角度是否随机确定。与大多数 AFSIM 命令不同，如果此参数被starting_beam_azimuth 命令随后覆盖，将警告用户。

默认值： false

性能考虑

预测平台的未来位置可能是一项耗费资源的操作。因此，在有很多移动平台的情况下，spinscheduler 的运行时间将超过默认调度器。通常，这种行为与场景中移动平台的数量大约呈二次关系。更具体地说，在一个有 10000 个移动平台的场景中，如果使用 spinscheduler而不是默认调度器，场景的运行时间会增加 18 倍。

# 3.5.1.4. 跟踪相关命令 Track Formation Commands

这些命令定义了建立跟踪的标准，以及该传感器生成的跟踪中报告的信息类型和质量。

注意： 对于不生成跟踪的传感器，这些命令将被忽略。

```txt
azimuth_error_sigma [ <angle-value> | <real-value> percent_of_true_range ] 
```

```xml
elevation_error_sigma [<angle-value> | <real-value> percent_of_true_range] range_error_sigma [<length-value> | <real-value> percent_of_true_range] range_rate_error_sigma <speed-value> 
```

这些命令指定了应用于传感器位置测量误差的高斯分布的标准差。标准差可以指定为角度、长度或速度值（视情况而定），或者可以指定为某些误差类型的“percent_of_true_range”的函数。在后一种情况下，使用以下公式：

sigma(angle) $=$ atan2(0.01 * value * Rtrue, Rtrue)

sigma(range) = 0.01 * value * Rtrue

其中，value 是命令中指定的 <real-value>（范围为 [0..100]），Rtrue 是目标的真实距离。

默认值： 所有误差的默认值为 0（无误差）。

hits_to_establish_track <M> <N> 指定在最近的 <N> 次尝试检测对象中，必须有 <M>次成功才能建立跟踪。

默认值： <M> 和 <N> 都为 1。

hits_to_maintain_track <M> <N> 一旦建立了跟踪，在最近的 <N> 次尝试检测对象中，必须有 <M> 次成功才能维持跟踪。

默认值： <M> 和 <N> 都为 1。

establish_track_probability [0 .. 1] 当 满 足 M/N 建 立 跟 踪 标 准 时 （ 参 见hits_to_establish_track），这是建立跟踪的概率。

默认值： 1.0

maintain_track_probability [0 .. 1] 只 要 满 足 M/N 维 持 跟 踪 标 准 （ 参 见hits_to_maintain_track），这是维持跟踪的概率。

默认值： 1.0

# 3.5.1.5. 跟踪信息报告命令 Track Information Reporting Commands

这些命令决定了在给定传感器的跟踪报告中报告的目标信息。

注意： 如果使用了滤波器（例如，WSF_KALMAN_FILTER、WSF_ALPHA_BETA_FILTER），则报告的跟踪将被标记为已滤波，报告的位置和速度信息（距离、方位、仰角、位置和速度）将是滤波后的结果。如果使用了卡尔曼滤波器，还可以获得状态协方差矩阵（参见reports_state_covariance）。

message_length <data-size-value>

指定此传感器模式下报告消息的逻辑长度。消息长度按以下顺序分配，使用第一个产生非零值的值：

传感器模式 message_length 命令的值（此命令）。

传感器 message_length 命令的值。

适用的 message_table 条目的值。

默认值： 0

message_priority <integer-priority>

指定从此模式发出的报告消息的优先级。消息优先级按以下顺序分配，使用第一个产生非零值的值：

传感器模式 message_priority 命令的值（此命令）。

传感器 message_priority 命令的值。

适用的 message_table 条目的值。

# 报告内容

reports_range   
报告从传感器到目标的斜距。  
reports_bearing

报告从传感器到目标的方位角。此角度以弧度为单位，从传感器的北方向测量，范围为{ -pi, pi }。

reports_elevation

报告从传感器到目标的仰角。

reports_location

报告目标的位置（纬度、经度、高度）。

reports_velocity

报告目标的速度。

reports_range_rate

报告目标的距离变化率。

reports_iff

报告敌我识别（IFF）状态。

reports_side

报告目标的阵营。

reports_type

报告目标的类型。

reports_signal_to_noise

报告信噪比。

reports_frequency

报告检测到的信号的频率。

reports_pulsewidth | reports_pw

报告信号的脉冲宽度。

注意： 也设置 reports_frequency。

reports_pulse_repetition_interval | reports_pri

报告信号的脉冲重复间隔。

注意： 也设置 reports_frequency。

reports_other

指定从此传感器的跟踪中将报告哪些数据元素。

reports_nothing

不报告任何内容。如果未指定任何报告标志，这是默认行为，并且还会取消任何先前的reports_ 命令。这在需要重用具有嵌入 reports_ 命令的现有传感器定义但需要更改报告内容的情况下，或在仅需要生成跟踪中的检测平台的情况下很有用。

track_quality [0 .. 1]

指定从此模式生成的跟踪的“质量”。

默认值： 0.5

send_track_drop_on_turn_off <boolean-value>

指示当传感器关闭时，是否应为每个活动跟踪发送“跟踪丢失”消息。

默认值： off

注意： 如果删除了拥有传感器的平台，则不会发送“跟踪丢失”消息。

# 3.5.1.6. 滤波器命令 Filter Commands

参见 4.5.4 滤波器 filter

# 3.5.1.7. 错误模型 error_model

```txt
error_model <derived-name> <base-name> ... Input for the error model ... end_error_model 
```

error_model <derived-name> <base-name>用于创建配置的错误模型，可以在预定义传感器类型的定义中引用。<derived-name>是用户希望用来引用配置错误模型的名称。<base-name>是可用的错误模型之一：

```txt
none   
standard_sensor_error   
radar SENSOR_error   
absolute_sensor_error   
bistatic_error   
trimsim_error 
```

错误模型的有效使用

错误模型定义可以直接嵌入到雷达的定义中。例如，假设你有一个名为‘ex_radar.txt的文件：

```txt
sensor EX_RADAR WSF_RADAR_SENSOR transmitter ... transmitter commands ... end_transmitter receiver ... receiver commands ... end_receive error_model <base-name> ... error model commands ... end_error_model end_sensor 
```

这种方法的问题在于，必须修改雷达定义才能更改或消除错误模型。在许多生产使用中，这是不理想或不可行的。更理想的是提供一个可以被覆盖的“默认”错误模型定义。

新的‘ex_radar.txt’文件将包含：

```txt
定义“默认”错误模型  
error_model EX_RADAR_ERROR<base-name> ... error model commands ...  
end_error_model
```

```txt
sensor EX_RADAR WSF_RADAR_SENSOR  
transmitter  
... transmitter commands ...  
end_transmitter  
receiver  
... receiver commands ...  
end_receiver  
error_model EX_RADAR_ERROR #符号引用错误模型  
end SENSOR 
```

然后要覆盖错误模型：

```txt
include ex_radar.txt  
# 提供一个新的定义来覆盖现有定义。  
# 此示例禁用错误计算。  
error_model EX_RARAR_ERROR none  
end_error_model
```

雷达模型将在最终创建雷达实例时使用 EX_RADAR_ERROR 的最后定义。

# 3.5.1.7.1. 不指定错误模型 none

```txt
error_model <derived-name> none end_error_model 
```

没有任何错误模型。

# 3.5.1.7.2. 标准探测错误模型 standard_sensor_error

```txt
error_model <derived-name> standard SENSOR_error end_error_model 
```

在 AFSIM 中 ， 标 准 错 误 模 型 使 用 azimuth_error_sigma 、 elevation_error_sigma 、range_error_sigma 和 range_rate_error_sigma 来计算误差值。可以通过以下方式定义：

# 3.5.1.7.3. 雷达探测错误模型 radar_sensor_error

```txt
error_model <derived-name> radar_sensor_error end_error_model 
```

radar_sensor_error是一个用于雷达传感器的错误模型，它使用接收器/发射器数据中指定的波束误差，例如波束宽度和带宽，或者通过 error_model_parameters 块进行覆盖。请注意，传感器类型必须是 WSF_RADAR_SENSOR。

# 3.5.1.7.4. 绝对探测错误模型 absolute_sensor_error

```txt
error_model <derived-name> absolute_sensor_error 
```

absolute_sensor_error是一个“绝对”错误模型，用于定义传感器检测目标的二维或三维绝对位置误差的一个标准差。

该模型用于模拟传感器检测目标位置的绝对误差，提供了两种误差标准：

2D 位置误差标准差 (2d_position_error_sigma)：指定一个标准差位置误差，应用于传感器检测目标的北向和东向轨迹位置。应用此误差将导致 $68 \%$ 的轨迹位置测量值位于以目标真实位置为中心的半径为<length-value>的圆内。目标的高度将不带误差地报告。  
3D 位置误差标准差 (3d_position_error_sigma)：指定一个标准差位置误差，应用于传感器检测目标的北、东和下方向的轨迹。应用此误差将导致 $68 \%$ 的轨迹位置测量值位于以目标真实位置为中心的半径为<length-value>的球体内。

使用示例

```txt
定义绝对错误模型  
error_model EX_SENSORS_ERROR absolute_sensor_error  
2d_position_error_sigma 10.0 #10米的2D位置误差标准差  
3d_position_error_sigma 15.0 #15米的3D位置误差标准差  
end_error_model  
sensor EX_SENSORS  
transmitter  
... transmitter commands ...  
end_transmitter  
receiver  
... receiver commands ...  
end_receiver  
error_model EX_SENSORS_ERROR #符号引用错误模型  
end SENSOR 
```

在这个例子中，EX_SENSOR_ERROR 被定义为一个绝对错误模型，并在传感器中引用。通过调整这些误差标准差参数，可以模拟不同的传感器测量误差情境。这种模型对于需要精确模拟传感器位置测量误差的应用场景非常有用。

# 3.5.1.7.5. 双基地错误 bistatic_error

```txt
error_model <derived-name> bistatic_error realistic_blurring time_reflected_sigma <time-value> time_direct_sigma <time-value> transmitter_position_sigmas <length-value> end_transmitter_position_sigmas end_error_model 
```

bistatic_error 是 一 个 用 于 双 基 地 雷 达 的 错 误 模 型 ， 它 使 用 传 感 器 模 式 的azimuth_error_sigma 和 elevation_error_sigma。其功能是利用瞬时测量来计算动态范围的标准差。此命令与 range_sigma、transmit_only 和 compute_measurement_errors 互斥，后者会导致此模型被绕过。该模型要求对发射器（直接信号）和目标（反射信号）都有直接视线，以获得成功的检测。

该错误模型基于论文《A Three-dimensional Bistatic Radar Target Position MeasurementError Model》，作者为 R. K. Lynn。

realistic_blurring：指定是否基于计算的动态范围误差标准差应用高斯分布到范围误差。默认情况下，此功能是禁用的。  
time_reflected_sigma <time-value>：指定反射时间测量的标准差。反射时间或散射时间（ts）是信号从发射器到目标再到接收器的接收时间。  
time_direct_sigma <time-value>：指定直接时间测量的标准差。直接时间（tx）是信号从发射器直接到接收器的接收时间。  
transmitter_position_sigmas <length-value> … end_transmitter_position_sigmas：指定一个双键表，用于发射器平台与其位置测量标准差相关联的标准差。注意，在双基地事务中，发射器可以在红方/对方团队。键是阵营和领域的配对。

# 3.5.1.7.6. TRIMSIM 错误 trimsim_error

```c
error_model <derived-name> trimsim_error  
north_position_error_sigma <length-value>  
east_position_error_sigma <length-value>  
down_position_error_sigma <length-value>  
reference_time_error <time-value>  
inter_system_time_delay <time-value>  
sensor_timing_error <time-value>  
atmospheric_refraction_residual <unitless>  
ground_target_altitude_error <length-value>  
end_error_model 
```

trimsim_error 是一个与 WSF_TRIMSIM_PROCESSOR 配合使用的错误模型，用于提供误差计算的参数。该模型定义了 TDOA（到达时间差）算法中使用的各种误差来源。需要为主 TDOA和从 TDOAESM 传感器建立 TDOA参数（如果适用）。

请注意，当定义这些参数时，传感器模式误差将被忽略。

north_position_error_sigma <length-value>：定义传感平台的北向目标位置误差。默认值为 0 米。  
east_position_error_sigma <length-value>：定义传感平台的东向目标位置误差。默认值为 0 米。  
down_position_error_sigma <length-value>：定义传感平台的下向目标位置误差。默认值为 0 米。  
reference_time_error <time-value>：需要描述。默认值为 0 秒。  
inter_system_time_delay <time-value>：定义目标传感器与参考系统（例如 INS/GPS）之间的相对时间误差。默认值为 0 秒。  
sensor_timing_error <time-value>：定义目标传感器的内部时间测量误差。默认值为 0 秒。  
atmospheric_refraction_residual <unitless>：定义大气折射补偿误差的残余部分。默认值为 0.0。  
ground_target_altitude_error <length-value>：定义用于检测“陆地”或“表面”目标的三平台特殊情况的高度误差。对于所有其他类型的目标（例如，空中，未知）或如果未定义此

值，算法仍然需要一个主节点和至少三个从节点检测目标。

# 3.5.2. 复合传感器 WSF_COMPOSITE_SENSOR

```python
sensor <name> WSF_COMPOSITE_SENSOR
    ... Platform Part Commands ...
    ... Common sensor Commands ... (See Note in Commands)
    operating_mode ...
    sensor ...
    filter ... end_filter
    track_quality ...
end SENSOR 
```

WSF_COMPOSITE_SENSOR 提供了一种创建“复合”传感器的方法，该传感器由一个或多个“组成”传感器构成。

在 WSF 中，有时很难用单一传感器定义来建模复杂的传感器。例如，包含多个孔径的真实系统通常在 WSF 中使用多个传感器进行建模。这会导致以下问题：

每个传感器独立报告其跟踪。  
在传感器之间进行跟踪变得困难。

WSF_COMPOSITE_SENSOR 的动机是解决这些问题。最终结果是，对于给定的目标，可能的多个报告将合并为一个单一的跟踪。

# 操作模式

复合传感器可以在两种 operating_mode 中之一运行：独立模式 或 同步模式。以下部分将分别描述这些模式。

# 独立操作模式

当 operating_mode 设置为独立模式时，组成传感器完全独立地运行。也就是说，每个组成传感器必须通过其各自的接口开启或关闭、提示或请求跟踪，而不是通过复合传感器。然而，复合传感器必须处于“开启”状态才能有效工作。它必须“开启”以接收来自组成传感器的跟踪报告。此模式通常用于组成传感器的帧率不同、模式不同，或用户希望对组成传感器有更多控制的情况。

在操作过程中，每个组成传感器将其跟踪报告发送到复合传感器，复合传感器将这些报告“合并”成一个单一的报告流进行报告。复合跟踪报告是使用组成传感器生成的跟踪报告形成的。当复合传感器从其组成传感器之一接收到“可接受”的跟踪报告时，它将报告一个跟踪。如果一个跟踪报告的质量（由生成传感器的 track_quality 属性定义）等于或高于任何其他正在积极检测该对象的组成传感器，则该报告是可接受的。注意，“漂移”的传感器（在最后一次检测机会中失败但仍未丢失跟踪）不被视为正在积极检测对象。复合跟踪也可以被“滤波”（参见下面的 filter），以产生目标位置和速度的更平滑估计，并生成协方差。注意，如果使用滤波器，则必须在每个组成传感器上定义测量误差。

当以下任一情况为真时，复合传感器将为目标发送“跟踪丢失”消息：

从所有报告目标的组成传感器接收到“跟踪丢失”消息。

所有报告目标的组成传感器都被关闭。

这种独立模式提供了对组成传感器的更大控制，同时允许复合传感器整合和优化跟踪报告。

# 同步操作模式

当 operating_mode 设置为同步模式时，组成传感器完全由复合传感器控制。也就是说，所有开启或关闭、提示或跟踪的请求必须直接指向复合传感器，而不是组成传感器。此外，通过复合传感器在同步模式下控制的任何被动传感器，将不会立即收到交互发射器（例如通信、传感器或干扰器）中任何间歇性信号变化（如频率或模式选择）的通知，这与作为独立传感器或作为独立模式下操作的复合传感器的一部分时不同。为了减轻这种影响，可以减少被动传感器的 frame_time 以允许更频繁地报告检测结果。

这种操作模式提供了最为一致的视图，但使用此模式时必须遵循以下条件：组成传感器必须出现在平台上的复合传感器之后。

所有组成传感器必须具有相同的模式集合。它们必须具有相同的名称，并且在各自的定义中以相同的顺序出现。然而，模式的属性可以不同。

复合传感器的模式特定调度和跟踪参数从第一个组成传感器复制（即，在传感器命令中提到的第一个传感器）。例如：

```tcl
frame_time  
maximum_request_count  
revisit_time  
dwell_time  
search_while_track  
disables_search  
hits_to_establish_track  
hits_to Maintain Tracks  
reports_<x> 命令  
track_quality  
filter 
```

忽略某些类型对象的检测机会的命令（即，ignore、ignore_domain、ignore_side、ignore_same_side）必须在复合传感器中指定。

这种同步模式确保了组成传感器的协调和一致性，适用于需要统一控制和报告的复杂传感器系统。

注意： 尽管该传感器被记录为接受通用传感器命令，但这些命令将被忽略，并且不应指定以确保未来的兼容性。复合传感器的属性来自其组成传感器。

operating_mode independent

定义组成传感器的管理方式。

independent：组成传感器独立运行。

synchronous：组成传感器与复合传感器同步运行。

默认值： 无 - 必须提供此值。

sensor <sensor-name>

定义组成传感器的名称。此命令必须重复一次或多次，以指定构成“复合”传感器的“组成”传感器的名称。通常，所有组成传感器应为相同的一般类型。目前，传感器应为报告跟踪的类型（如 WSF_RADAR_SENSOR、WSF_IRST_SENSOR、WSF_PASSIVE_SENSOR）。

注意： 复合传感器的传感器定义不应包含 internal_link 命令。组成传感器将根据需要

自动链接到复合传感器。

filter <filter-type> … end_filter

定义在 operating_mode 为独立时应用于目标跟踪流的滤波器。

默认值： 无

注意： 如果使用滤波器，则必须在每个组成传感器上定义测量误差。此命令必须出现在 operating_mode 命令之后。

track_quality [ 0 .. 1 ]

指定当 operating_mode 为独立时，由该传感器生成的复合跟踪的跟踪质量。仅当该值大于零时才使用。如果值为零，则使用组成跟踪的跟踪质量。

默认值： 0.0（使用组成跟踪的跟踪质量。）

示例：

```txt
sensor SENSOR-TYPE-1 ...  
...  
end_sensor  
sensor SENSOR-TYPE-2 ...  
...  
end_sensor  
platform_type ...  
processor track_proc WSFTRACKPROCESSOR  
end Processor  
sensor composite WSF_COMPOSITE_SENSOR  
operating_mode independent  
sensor sensor-1  
sensor sensor-2  
internal_link track_proc  
on  
end SENSOR  
sensor sensor-1 SENSOR-TYPE-1  
on  
end SENSOR  
sensor sensor-2 SENSOR-TYPE-2  
on  
end SENSOR  
endPLATFORM_type 
```

# 3.5.3. 几何学传感器 WSF_GEOMETRIC_SENSOR

```txt
sensor<name>WSFGEOMETRIC_SENSOR 
```

```txt
... Platform Part Commands ...
... Articulated Part Commands ...
// Sensor Commands
sensor Commands ...
mode ...
... common sensor mode commands ...
... receiver ...
... Antenna Commands ...
platform_type [ <platform-type> | default ]
check_terrain_masking <boolean-value>
terrain_masking_mode [ terrain_andHorizon | terrain_only | horizon_only ]
earth_radius-multiplier <value>
effective-earth_radius <length-value>
minimum_range_rate <speed-value>
maximum_range_rate <speed-value>
end_mode
end SENSOR 
```

WSF_GEOMETRIC_SENSOR 是一种严格基于几何学的简单传感器。根据下面模式命令中施加的附加约束，如果目标位于由天线命令形成的视锥体内，则将被检测到：

azimuth_field_of_view（方位视场）  
elevation_field_of_view（仰角视场）  
maximum_range 和 minimum_range（最大和最小范围）

注意： 传感器模式接受接收器命令，但这仅用于访问 check_terrain_masking、terrain_masking_mode 和 earth_radius_multiplier / effective_earth_radius 命令。其他记录在接收器中的命令不被使用。

platform_type [ <platform-type> | default ]

定义具有 <platform-type> 平台类型的目标的最大检测范围。如果提供了关键字 default，则该范围将适用于所有没有自己检测范围或 pd-range 表条目的平台类型。

detection_range <length-value>

定义具有 <platform-type> 平台类型的目标的最大检测范围。

pd_range_table … end_pd_range_table

定义具有 <platform-type> 平台类型的目标的检测概率与范围表。例如：

```txt
platform_type WSF_PLATFORM pd_range_table 
```

```txt
1.0 0 km  
0.8 0.5 k  
0.2 2.0 k 
```

```txt
end_pd_range_table 
```

注意： 定义少于两个条目的表是输入错误。范围必须是递增的，中间值是线性插值的。一个 platform_type 可以同时拥有 pd_range_table 和 detection_range。

check_terrain_masking <boolean-value>

确定传感器是否对目标执行地形和地平线遮蔽检查。默认情况下，首先检查地平线遮蔽，

然后在加载地形时进行单独的地形遮蔽检查。简单的地平线遮蔽检查假设地球是光滑的球形，任何低于海平面的物体都被遮蔽。对于水下传感器，可以通过将 terrain_masking_mode 设置为 terrain_only 来禁用地平线检查。

默认值： true（执行地形和地平线遮蔽检查）

terrain_masking_mode [ terrain_and_horizon | terrain_only | horizon_only ]

设置要执行的遮蔽检查的模式或类型。默认情况下，启用地平线和地形遮蔽检查。

默认值： terrain_and_horizon

earth_radius_multiplier <value> / effective_earth_radius <length-value>

指定用于计算电磁辐射大气折射效应的地球半径乘数或有效地球半径。

默认值： earth_radius_multiplier 1.0

注意： 地球半径被认为是 6366707.019 米。

minimum_range_rate <speed-value>

传感器不会检测到范围速率低于此值的目标。

默认值： 无最小值

maximum_range_rate <speed-value>

传感器不会检测到范围速率高于此值的目标。

默认值： 无最大值

# 3.5.4. 被动射频检测传感器 WSF_PASSIVE_SENSOR

```txt
sensor <name> WSF_PASSIVE_SENSOR
... Platform Part Commands ...
... Common sensor Commands ...
reported_target_type .. end_reported_target_type
reported_emitter_type .. end_reported_emitter_type
unframed misdetection_optimization ...
unframed misdetection_coast_time ...
mode <name>
... Common Mode Commands ...
... Detection Scheduling Commands ...
... Track Formation Commands ...
... Track Information Reporting Commands ...
... Antenna Commands ...
... receiver ... end_receiver
frequency_band ...
dwell_time ...
revisit_time ...
detection_sensitivity ...
continuous misdetection_sensitivity ...
pulsed misdetection_sensitivity ... 
```

```txt
detection_sensitivities ... endDetection_sensitivities   
detection_threshold ...   
continuousDetection_threshold ...   
pulsedDetection_threshold ...   
detection_thresholds ... end_detection_thresholds   
detection(probability ... end_detection(probability   
scan_on_scan_model ...   
azimuth_error_sigma_table ... end_azimuth_error_sigma_table elevation_error_sigma_table ... end_elevation_error_sigma_table range_error_sigma_table ... end_range_error_sigma_table ranging_time ... ranging_time_track_quality ...   
end_mode   
end SENSOR 
```

WSF_PASSIVE_SENSOR 实现了一种基本的被动射频（RF）检测传感器，可用于建模雷达告警接收器（RWR）、信号情报（SIGINT）和电子情报（ELINT）传感器。

该传感器使用两种不同的检测方法来收集数据以进行报告：

# 框架或采样检测：

传感器检测其频带内发射模式规则的所有发射器。这是传感器检测搜索雷达的方式。传感器的采样间隔由 frame_time 模式命令指定。

# 非框架检测：

传感器使用此方法检测其频带内发射模式不规则的发射器。这包括使用电子波束控制跟踪多个目标的跟踪雷达，以及仅在发送消息时才发射的通信设备。

传感器结合这两种检测方法的结果，为其检测到的每个目标生成检测报告（WsfTrack）。给定目标的检测报告按照 frame_time 定义的间隔生成。在框架采样之间发生的非框架检测将在下一个框架采样时报告。

对于瞬时通信信号的非框架检测，在信号存在的每个框架采样中都会报告。这意味着长消息的传输将在传输期间被检测到。然而，来自第一次采样的检测结果将在同一传输的后续采样中报告（假设在传输期间变化很小）。

# 相关信息

被动 RF 传感器：被动 RF 传感器通过被动监听无线电频谱来检测信号，而不主动发射信号，因此不会干扰其他通信设备。

应用领域：被动 RF 传感器广泛用于检测和分类雷达信号，尤其是在军事应用中，如雷达告警接收器（RWR）和电子情报（ELINT）系统。

这种传感器模型适用于需要检测和分析射频信号的各种应用场景，尤其是在需要隐蔽操作的情况下。

reported_target_type … end_reported_target_type

```txt
reported_target_type
default_time_toDeclare...
default_time_to_reevaluate...
type <target_type>
    ... type sub Commands ...
type <target_type>
    ... type sub commands ...
...
default_type
    ... type sub commands ...
end_reported_target_type 
```

定义被动传感器如何在跟踪中报告目标类型信息。

▫ default_time_to_declare <time-value>

定义从初始检测到确定目标类型所需的时间。

默认值： 0 秒

□ default_time_to_reevaluate <time-value>

定义用于重新评估目标识别的时间间隔。0 秒表示不会进行重新评估。

默认值： 0 秒

▫ type <target_type>

指定以下子命令适用的真实目标类型。

□ default_type

指定以下类型子命令适用于未用 type 命令定义的任何类型。

类型子命令

time_to_declare <time-value>定义从初始检测到确定目标类型所需的时间。默认值： 由 default_time_to_declare 命令设置  
time_to_reevaluate <time-value>定义用于重新评估目标识别的时间间隔。默认值： 使用 default_time_to_reevaluate 命令设置  
report_type <type-name> emitter <emitter-name> report_type <type-name1> emitter <emitter-type-1> emitter <emitter-type- $^ { 2 > }$ ... emitter <emitter-name-N> report_type <type-type-2

定义报告的类型名称为目标类型，基于发射器列表中报告的发射器类型。目前，必须在发射器列表中完全匹配才能报告给定的 report_type。如果有差异，将报告另一个 report_type 或 default_type。

report_type <type-name> <probability>

定义报告类型名称为目标类型的概率。概率参数是 0.0 到 1.0 之间的值。可以指定任意数量的 report_type 命令，只要概率参数加起来为 1.0。为了更方便使用，可以使用 remainder 作为概率参数来指定所需的值以加到 1.0。

report_truth

指定传感器将报告真实类型。这仅在 default_type 命令下有效。

reported_emitter_type … end_reported_emitter_type   
unframed_detection_optimization <boolean-value>   
```txt
reported_emitter_type
default_time_toDeclare...
default_time_to_reevaluate...
type <emitter_type>
    ... type sub Commands ...
type <emitter_type>
    ... type sub commands ...
...
default_type
    ... type sub commands ...
end_reported_emitter_type 
```

定义被动传感器如何在跟踪中报告发射器类型信息。

□ default_time_to_declare <time-value>

定义从初始检测到确定发射器类型所需的时间。

默认值： 0 秒

□ default_time_to_reevaluate <time-value>

定义用于重新评估发射器识别的时间间隔。0 秒表示不会进行重新评估。

默认值： 0 秒

▫ type <emitter_type>

指定以下子命令适用的真实发射器类型。

□ default_type

指定以下类型子命令适用于未用 type 命令定义的任何类型。

类型子命令

time_to_declare <time-value>

定义从初始检测到确定发射器类型所需的时间。

默认值： 由 default_time_to_declare 命令设置

time_to_reevaluate <time-value>

定义用于重新评估发射器识别的时间间隔。

默认值： 使用 default_time_to_reevaluate 命令设置

report_type <type-name> <probability>

定义报告类型名称为发射器类型的概率。概率参数是 0.0 到 1.0 之间的值。可以指定任意数量的 report_type 命令，只要概率参数加起来为 1.0。为了更方便使用，可以使用 remainder 作为概率参数来指定所需的值以加到 1.0。

report_truth

指定传感器将报告真实类型。这仅在 default_type 命令下有效。

其他命令

指示是否使用非框架检测优化。如果启用，一旦传感器在一个帧内成功检测到给定发射

器，后续在同一帧内检测同一发射器的尝试将被抑制。

默认值： true

unframed_detection_coast_time <time-value>

如果被动传感器的帧时间比它试图检测的传感器快，它可能在一个帧内检测到发射器而在下一个帧内未检测到。这可能导致大量的跟踪创建和删除。此值指示从发射器成功检测后报告的时间长度。

默认值： 2 秒

# 被动传感器特定模式命令 Passive-Specific Mode Commands

frequency_band <lower-frequency> <upper-frequency>

定义传感器可以检测的频率范围。如果传感器可以检测多个频段，可以多次指定此命令。

dwell_time <time-value> 和 revisit_time <time-value>

这些命令与紧接在其前面的 frequency_band 相关，定义传感器在该频段停留的时间以及停留之间的间隔。这些命令仅在启用 scan_on_scan_model 时有效，用于确定传感器在检测机会发生时查看目标发射器频率的时间概率。

注意： 如果为传感器中的任何频段定义了这些命令，则必须为传感器中的所有频段定义它们。

continuous_detection_sensitivity <db-power>   
pulsed_detection_sensitivity <db-power>   
detection_sensitivity <db-power>

定义可以“可靠”检测到的最小信号强度。如果定义了 detection_probability，则这是会导致 Pd 为 0.5 的信号强度。如果未定义 detection_probability，则这定义了成功检测将被声明的信号强度。

前两种形式分别设置连续波和脉冲信号的检测灵敏度。

最后一种形式将两种灵敏度设置为相同的值。

如 果 使 用 continuous_detection_sensitivity ， 则 必 须 同 时 指 定pulsed_detection_sensitivity，反之亦然。

默认值： 请参见 detection_threshold。

detection_sensitivities … end_detection_sensitivities

允许定义频率依赖或信号类型和频率依赖的检测灵敏度。

仅频率依赖表：

```txt
detection_sensitivities frequency <frequency-value-1> <db-power-1> frequency <frequency-value-2> <db-power-2> frequency <frequency-value-n> <db-power-n> endDetection_sensitivities 
```

信号类型和频率依赖表：

```txt
detection_sensitivities signal_type <signal-type-1> frequency <frequency-value-1> <db-power-1> frequency <frequency-value-2> <db-power-2> frequency <frequency-value-n> <db-power-n> signal_type <signal-type-2> 
```

```txt
frequency <frequency-value-1> <db-power-1> frequency <frequency-value-2> <db-power-2> frequency <frequency-value-n> <db-power-n> endDetection_sensitivities 
```

▫ <signal-type> 信号类型的字符串输入，有效值为 ["continuous" | "pulsed" | "both"]。   
▫ <frequency> 频率值。   
□ <db-power>在指定频率下检测所需的接收信号强度。

注意：

在定义信号类型和频率依赖表时，任何在第一个 signal_type 条目之前出现的frequency 条目都假定适用于“both”（即连续和脉冲）信号类型。

如果随后输入 signal_type，则之前为该信号类型输入的相应数据将被清除，并输入新数据。

算法：

如果使用信号类型依赖表，则使用接收到的信号的信号类型来定位适当的信号类型特定频率条目集。

频率大于或等于 frequency-value-m 且小于 frequency-value- $\cdot \mathsf { m } { + 1 }$ 将使用 db-power-m。  
频率小于 frequency-value-1 将使用 db-power-1。  
频率大于或等于 frequency-value-n 将使用 db-power-n。  
detection_probability

定义检测概率（Pd）与接收信号强度的函数（表示为接收功率与检测灵敏度的比率）。表格定义如下：

```txt
detection(probability signal <db-ratio-1> pd <pd-value-1> signal <db-ratio-2> pd <pd-value-2> ... signal <db-ratio-n> pd <pd-value-n> endDetection probability 
```

▫ <db-ratio-n>：接收信号功率与检测灵敏度的比率。  
□ <pd-value-n>：与比率相关的检测概率。

超出表格限制的信号将被限制在适当的端点。中间值将使用线性插值确定。

默认值： 如果未定义此函数，则使用二进制检测器。如果信号水平等于或超过检测灵敏度，Pd 将为 1.0。

注意： 如果使用 detection_threshold 或 detection_thresholds，检测灵敏度将计算为检测阈值乘以噪声功率。

scan_on_scan_model <boolean-value>

指定是否应使用概率扫描-扫描（PSOS）模型。此模型尝试概率性地捕获被动传感器在频率上扫描且发射器可能在角度上扫描的时间效应。

默认值： 关闭

误差西格玛表

azimuth_error_sigma_table

elevation_error_sigma_table   
range_error_sigma_table

这些命令提供了定义误差西格玛的能力，这些误差西格玛是接收信号频率的函数，而不是由单值 azimuth_error_sigma、elevation_error_sigma 和 range_error_sigma 命令提供的固定西格玛。格式如下：

```txt
type_error_sigma_table frequency <frequency-1> <error-sigma-1> frequency <frequency-2> <error-sigma-2> ... frequency <frequency-n> <error-sigma-n> end_type_error_sigma_table 
```

type 是 方 位 、 仰 角 或 范 围 ， <error-sigma> 是 使 用 与 azimuth_error_sigma 、elevation_error_sigma 和 range_error_sigma 命令中值相同格式的西格玛。可以为每种类型提供独立的表。

注意： 条目必须按频率单调递增顺序排列。提供表将覆盖其单值对应项的任何规范。

ranging_time <time-value>

在指定时间过去后，将范围信息添加到该传感器生成的任何跟踪中。这基本上模拟了系统可以在足够长的时间后进行三角测量并获得范围。

ranging_time_track_quality <quality-value>

如果使用测距时间生成具有范围信息的跟踪，则此参数控制范围有效时的跟踪质量。quality-value 必须为非负值。

# 3.5.5. 雷达传感器 WSF_RADAR_SENSOR

```txt
sensor<name>WSF_RADAR_SENSOR ... Platform Part Commands ... ... Articulated Part Commands ... ... sensor Commands ... show Calibration_data mode<name> ... Sensor Mode Commands ... ... WSF_RADAR_SENSOR Mode Commands ... beam 1 Antenna Commands ... transmitter ... transmitter commands ... end_transmitter receiver ... receiver commands ... end_receiver ... Beam Commands ... end_beam beam <n> Antenna Commands ... 
```

```txt
transmitter ... transmitter commands ... end_transmitter receiver ... receiver commands ... endreceiver ... Beam Commands ... end_beam end_mode end SENSOR 
```

WSF_RADAR_SENSOR 提供了一个基础的雷达实现，能够表示各种雷达系统，从简单的单模式预警雷达到复杂的多模式雷达，用于目标检测机会。

一个雷达定义由一个或多个模式组成，每个模式由一个或多个波束组成。如果雷达只有一个模式，可以省略包围模式定义的 mode 和 end_mode 命令。如果一个模式只有一个波束，可以省略包围波束定义的 beam 和 end_beam 命令。

# 多波束考虑

如果传感器使用多个波束，应注意以下事项：

波束编号必须严格按数字顺序递增且无间隙。即，波束 2 必须跟在波束 1 之后，波束 3必须跟在波束 2 之后，依此类推。

第一个波束（波束 1）的定义为每个后续波束提供初始定义。出现在后续波束的beam/end_beam 块之间的命令可以对初始定义进行添加或修改。

如果传感器有多种模式，则每种模式的波束数量必须相同（这一限制可能在未来版本中被移除）。

# 传感器级别命令

雷达传感器的实现可以涵盖从简单的早期预警雷达到复杂的多模式雷达系统。根据不同的应用需求，雷达系统可以进行多种配置和调整，以适应特定的检测和跟踪任务。

# 相关信息

多模式雷达：现代雷达系统通常支持多种操作模式，以适应不同的任务需求，如目标检测、跟踪和识别。

波束管理：在多波束雷达中，波束管理是关键，确保每个波束的定义和操作符合系统的整体目标。

应用领域：雷达广泛应用于军事、航空、海事和气象等领域，用于目标检测、导航和监视。

通过灵活的模式和波束配置，WSF_RADAR_SENSOR 可以模拟各种复杂的雷达系统，满足不同的操作需求。

# 3.5.5.1. 高级低空雷达模型 ALARM Interface

ALARM 接口的功能

非出口版本的 WSF（Weapon System Framework）可选地包含了来自空军研究实验室（AFRL）的高级低空雷达模型（ALARM）5.2 版的许多功能。这些功能包括：

大气衰减模型  
杂波模型  
传播模型

注意事项

该模型仅适用于在地球表面（陆地或水面）操作的雷达，不适用于空中或太空中的雷达。

WSF 与 ALARM 的集成

WSF 会将某些值传递到 ALARM 环境中：

ALARM 的 REFRACTIVITY 值 被 设 置 为 发 射 器 的 WSF earth_radius_multiplier 值（WSF_RADAR_SENSOR 的默认值为 4/3）。  
如果感知玩家属于“地面”或“水下”空间域（通过使用 WSF_SURFACE_MOVER 或WSF_SUBSURFACE_MOVER，或在平台类型定义中使用 spatial_domain），则执行以下操作：

□ ALARM 的 LAND_COVER 值被设置为“水”。  
▫ ALARM 的 LAND_FORM 值从 WSF 的 global_environment 命令 sea_state 派生。

如果感知玩家不属于“地面”或“水下”空间域（如前所述），则执行以下操作：

▫ ALARM 的 LAND_COVER 值从 WSF 的 global_environment 命令 land_cover 派生。  
▫ ALARM 的 LAND_FORM 值从 WSF 的 global_environment 命令 land_formation 派生。

请注意，内部的 ALARM 环境没有 WSF 那么多的地面覆盖值，因此需要进行一些映射。

附加信息

根据搜索结果，ALARM 模型主要用于评估目标检测范围，考虑了环境因素如大气、地形遮蔽、杂波、多路径和电磁传播等。

# 3.5.5.1.1. ALARM 衰减模型 Attenuation Model

```txt
sensor ... transmitter attenuation earce end_transmitter end_sensor 
```

# ALARM 衰减模型的选择

在发射器块中通过包含一个attenuation命令来选择ALARM衰减模型，该命令选择‘earce’模型如上。