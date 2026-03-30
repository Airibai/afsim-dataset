7) 根据前面步骤确定的状态，调用 CyberAttackSucceeded 或 CyberAttackFailed 观察者回调。  
8) 如果攻击被标记为“失败”，则停止网络生命周期的进一步执行。

# 效果阶段

“利用”步骤已声明受害者易受攻击。对于代表传入攻击的 cyber_attack对象中的每个效果，调用 Attack方法以引发模拟效果（例如：禁用传感器等）。

# 反应阶段

确定受害者是否能够检测和反应攻击。使用在“利用阶段”确定的攻击响应。

1) 通过执行“attack_detection”的概率评估来确定受害者是否能够检测到攻击（参见下面的概率评估）。

□ 如果抽签小于或等于阈值，则攻击被认为是可被受害者检测到的。  
▫ 通过执行“attack_attribution”的概率评估来确定受害者是否能够归因于攻击。  
▫ 如果抽签大于阈值，则攻击被认为是不可检测的，受害者无法注意到或从攻击中恢复。

2) 发出 WsfDraw 命令以记录可视化数据。  
3) 调用 CyberAttackSucceeded 观察者回调。

如果攻击被认为是可被受害者检测到的，将发生以下步骤：

模拟受害者识别自己正在被攻击所需的时间（即：为当前模拟时间加上攻击响应中的attack_detection_delay_time 安排一个事件）。  
在 attack_detection_delay_time 完成时：

□ 调用攻击响应中定义的任何 OnAttackDetection 脚本。这将允许受害者执行诸如通知他人攻击等操作。  
□ 模拟受害者从攻击中恢复所需的时间（即：为当前模拟时间加上攻击响应中的attack_recovery_delay_time 安排一个事件）。  
□ 发出 WsfDraw 命令以记录可视化数据。  
□ 调用 CyberAttackDetected 观察者回调。  
如果攻击被认为是归因的，调用 CyberAttackAttributed 观察者回调。

在 attack_recovery_delay_time 完成时：

□ 调用攻击响应中定义的任何 OnAttackRecovery 脚本。这让受害者采取任何无法在后续步骤中执行的自定义操作。  
□ 如果攻击响应中存在“restore”命令，则遍历攻击中每个 cyber_effect 并调用其Recover()方法。  
□ 通过执行“future_immunity”的概率评估来确定受害者是否对未来同类型的攻击免疫（参见下面的概率评估）。

如果抽签小于或等于阈值，受害者将对未来同类型的攻击免疫。  
如果抽签大于阈值，受害者将继续对未来同类型的攻击易受攻击。

□ 发出 WsfDraw 命令以记录可视化数据。  
□ 调用 CyberAttackRecovery 观察者回调。

# 嵌入式攻击

嵌入式攻击是指那些在主机系统的硬件或软件中处于休眠状态并通过内部触发的攻击（即：它们不是从外部来源传递的）。这种攻击可以通过使用 cyber_trigger 来建模，该触发

器定期检查会引发此类攻击的条件。任何可以用 AFSIM 脚本语言编写的逻辑都可以用来描述通过 cyber_trigger启动潜在嵌入式攻击的有利条件，当这些条件满足时，可以针对目标发起定义的攻击，以模拟嵌入式攻击的特征。

# 平台响应选择

平台对网络扫描或攻击的响应由其 cyber_protect 对象定义。当尝试进行扫描或攻击时，AFSIM必须确定在 cyber_protect 对象中应使用哪种响应。假设以下定义：

```txt
cyber_attack AT_1 WSF_CYBER_attack  
...  
end.cyber_attack  
cyber_attack AT_2 WSF_CYBERAttack  
...  
end.cyber_attack  
cyber_attack AT_3 WSF_CYBERAttack  
...  
end.cyber_attack  
# 从另一种攻击类型继承的攻击类型。  
cyber_attack AT_4 AT_2  
...  
end.cyber_attack  
cyber_protect PT_1 WSF_CYBER_PROTECTattack_response AT_1...end_attack_responseattack_response AT_2...end_attack_response  
end.cyber_protect  
cyber_protect PT_2 WSF_CYBER_PROTECTattack_response AT_2...end_attack_responsedefault_attack...end_default_attack  
end.cyber_protect 
```

如果使用 cyber_attack类型‘<T>’尝试进行网络攻击或扫描，针对目标平台执行的算法以确定

响应为：

1) 尝试找到名称为‘<T>’的 attack_response。  
2) 如果步骤 1 失败，对于‘<T>’继承的每个 cyber_attack 类型，尝试找到名称与继承类型匹配的 attack_response。  
3) 如果步骤 1 和 2 失败，尝试找到名为‘default’的 attack_response 条目。  
4) 如果步骤 1、2 和 3 都失败，则使用从 cyber_attack 类型 $' { < } \mathsf { T } { > } ^ { \prime }$ 中的默认响应值动态创建的内部响应。

以下表格定义了每种保护类型对每种攻击的选定响应。cyber_attack 类型在顶行，cyber_protect 类型在左列。交叉点是选定的攻击响应以及选择响应的规则编号（括号内）：

<table><tr><td></td><td>AT_1</td><td>AT_2</td><td>AT_3</td><td>AT_4</td></tr><tr><td>PT_1</td><td>AT_1 (1)</td><td>AT_2 (1)</td><td>internal (4)</td><td>AT_2 (2)</td></tr><tr><td>PT_2</td><td>default (3)</td><td>AT_2 (1)</td><td>default (3)</td><td>AT_2 (2)</td></tr></table>

使用规则 1 选择的响应是显而易见的，因为它们是精确匹配的，但其他的可能需要进一步解释：

对于使用规则 2 选择的：PT_1 或 PT_2 都没有针对 AT_4 的响应，但它们确实有针对 AT_2的响应。因为 AT_4 继承自 AT_2，所以将选择 AT_2 的响应。  
对于使用规则 3 选择的：PT_2 没有针对 AT_1 或 AT_3 的响应，但它确实有一个默认响应将被使用。  
对于使用规则 4 选择的：PT_1 没有针对 AT_3 的响应，也没有默认响应，因此将使用从AT_3 的默认响应值动态创建的响应。

概率评估

在网络交战期间，可以进行五种不同的概率评估。与每个评估相关的是一个概率阈值和一个用于抽取随机数的频率。以下表格显示了每种评估类型的阈值来源和抽取频率命令：

<table><tr><td>Evaluation Type</td><td>Threshold Command</td><td>Draw Frequency Command</td></tr><tr><td>scan misdetection</td><td>probability_of_scan misdetection</td><td>scan misdetection_draw_freqency</td></tr><tr><td>scan Attribution</td><td>probability_of_scan Attribution</td><td>scan AttributionDRAW_freqency</td></tr><tr><td>attack_success</td><td>probability_of_attack_success</td><td>attack_success_DRAW_freqency</td></tr><tr><td>status_report</td><td>probability_of_status_report</td><td>status_report_DRAW_freqency</td></tr><tr><td>attack misdetection</td><td>probability_of_attack misdetection</td><td>attack misdetectiondraw_freqency</td></tr><tr><td>attack Attribution</td><td>probability_of_attack Attribution</td><td>attack AttributionDRAW_freqency</td></tr><tr><td>future-immunity</td><td>probability_of_future-immunity</td><td>future-immunity.draw_freqency</td></tr></table>

在 AFSIM网络交战模型中，所有概率评估都使用相同的算法。以下是以‘attack_success’（攻击成功）的评估为例的详细说明：

1) 确定‘attack_success’阈值：

使用受害者 cyber_protect 对象中当前攻击响应的 probability_of_attack_success 值。  
如果前一个值未定义，则使用当前 cyber_attack 对象中的 probability_of_attack_success值（或其默认值）。

2) 根据 attack_success_draw_frequency 命令确定随机抽取：

如果频率是‘always’，则执行抽取并返回。

如果频率是‘once_per_simulation’：

□ 如果这是第一次使用攻击，则执行抽取并存储。  
□ 返回与此攻击类型相关的存储抽取。

如果频率是‘once_per_target’：

□ 如果这是第一次对当前目标使用此攻击类型，则执行抽取并存储。  
▫ 返回与此攻击类型相关的存储抽取。

如果频率是‘interval_per_simulation’：

如果这是第一次使用此攻击类型，或者自上次使用以来的时间超过指定的时间间隔，则执行抽取并存储。  
□ 返回与此攻击类型相关的存储抽取。

如果频率是‘interval_per_target’：

▫ 如果这是第一次对该目标使用此攻击类型，或者自上次对该目标使用以来的时间超过指定的时间间隔，则执行抽取并存储。  
▫ 返回与此目标和攻击类型相关的存储抽取。

# 4.16.2. 网络攻击 cyber_attack

```txt
cyber_attack <type> <base_type> # Define the effect(s) of the attack on the victim effect ... duration ... scan_delay_time ... delivery_delay_time ... # Define default probability thresholds. probability_of_scan misdetection ... probability_of_scan_attribute ... probability_of_attack_success ... probability_of_status_report ... probability_of_attack misdetection ... probability_of_attack_attribute ... probability_of_future-immunity ... # Random draw frequencies. scan misdetection_draw_freqency ... scan_attribute Draws_freqency ... attack_successdraw_freqency ... status_reportdraw_freqency ... attack misdetectiondraw_freqency ... attack_attributedraw_freqency ... 
```

```txt
future-immunity_draw_freqency ... end_cyber_attack 
```

AFSIM 中的 cyber_attack 对象

在 AFSIM 中，cyber_attack 对象用于定义攻击对受害者的影响类型，并在受害者的cyber_protect 对象中没有定义响应时，提供默认响应。

关键字段解释

<type>: 定义的 cyber_attack 类型的名称。

<base_type>: 一个现有的 cyber_attack 类型或 WSF_CYBER_EFFECT 的名称，其定义将用作新类型的初始定义。

功能概述

效果定义: cyber_attack 对象定义了攻击对受害者的影响类型，例如禁用传感器或其他系统功能。

概率阈值: 这些是用于评估攻击成功、检测和归因等事件的默认概率值。

随机抽取频率: 定义了在模拟过程中随机数抽取的频率，以确定事件的发生。

概述

cyber_attack对象定义了攻击对受害者的影响类型，并在受害者的 cyber_protect 对象中没有定义响应时，提供默认响应。

命令

effect <effect_type>: 一个 cyber_effect 类型，用于模拟攻击对受害者的影响。此命令可以重复以指定多个效果。如果与此攻击相关联的效果有多个，则效果将按照列出的顺序解决。

默认值: 无。必须至少提供一个效果。

警告: 特定效果类型可能需要在通过 CyberAttack 方法调用发起攻击时由用户输入，如每个效果文档中所述。用户通过这些调用仅限于单个变量输入。当前不支持在单次攻击中使用不同变量类型的多个效果，可以通过单独的攻击类型定义来解决这一问题。

duration <time-value>: 指定效果持续的时间。当未设置 duration 但存在与 cyber_attack效 果 相 关 联 的 cyber_protect 块 时 ， duration 将 是 attack_detection_delay_time 和attack_recovery_delay_time 的总和。

默认值:0 秒

注意: 如果 duration 小于 attack_detection_delay_time，则受害者将无法为攻击抽取网络免疫。

scan_delay_time <random-time-value>: 指 定 执 行 扫 描 所 需 的 时 间 。 这 是 从 调 用WsfPlatform.CyberScan 到 WsfPlatform.CyberScanStatus 返回非负值之间的时间。在此时间之前发生的任何对 WsfPlatform.CyberScanStatus 的调用将返回负值，表示扫描正在进行中。

默认值:0 秒

delivery_delay_time <random-time-value>: 指定传递漏洞利用所需的时间。这是从调用WsfPlatform.CyberAttack 到 WsfPlatform.CyberAttackStatus 返回非负值之间的时间。在此

时间之前发生的任何对 WsfPlatform.CyberAttackStatus 的调用将返回负值，表示传递正在进行中。

默认值:0 秒

# 概率阈值命令

这些命令指定如果在 cyber_protect 中的 attack_response 中未提供相应值时使用的默认概率阈值。

probability_of_scan_detection [ 0 .. 1 ]: 指 定 cyber_protect 中 相 应 attack_response 的probability_of_scan_detection 的默认值。

默认值:0

probability_of_scan_attribution [ 0 .. 1 ]: 指定 cyber_protect 中相应 attack_response 的probability_of_scan_attribution 的默认值。

默认值:0

probability_of_attack_success [ 0 .. 1 ]: 指 定 cyber_protect 中 相 应 attack_response 的probability_of_attack_success 的默认值。

默认值:1

probability_of_status_report [ 0 .. 1 ]: 指 定 cyber_protect 中 相 应 attack_response 的probability_of_status_report 的默认值。

默认值:1

probability_of_attack_detection [ 0 .. 1 ]: 指定 cyber_protect 中相应 attack_response 的probability_of_attack_detection 的默认值。

默认值:0

probability_of_attack_attribution [ 0 .. 1 ]: 指定 cyber_protect 中相应 attack_response 的probability_of_attack_attribution 的默认值。

默认值:0

probability_of_future_immunity [ 0 .. 1 ]: 指定 cyber_protect 中相应 attack_response 的probability_of_future_immunity 的默认值。

默认值:0

# 随机抽取频率命令

以下命令定义了执行均匀随机抽取的频率。攻击类型中随机数的每个类别使用单独的命令控制。

在以下每个命令中，<draw_frequency>可以有以下值：

always: 每次评估时抽取一个新的随机值。

once_per_simulation: 在模拟中的第一次评估时抽取一个随机值，并用于所有后续评估。

once_per_target: 在涉及特定目标的第一次评估时抽取一个随机值，并用于所有后续涉及相同目标的评估。

interval_per_simulation <random-time-value>: 如果自上次抽取以来的模拟时间超过阈值，则抽取一个随机值。

interval_per_target <random-time-value>: 如果自上次涉及相同目标的抽取以来的模拟时间超过阈值，则抽取一个随机值。

scan_detection_draw_frequency <draw_frequency_>: 确定扫描是否被检测到的随机抽取 频率。

默认值: always

scan_attribution_draw_frequency <draw_frequency_>: 确定扫描是否被归因的随机抽取 频率。

默认值: always

attack_success_draw_frequency <draw_frequency_>: 确定攻击是否成功的随机抽取频率。 默认值: always   
status_report_draw_frequency <draw_frequency_>: 确定是否进行状态报告的随机抽取频率。

默认值: always

attack_detection_draw_frequency <draw_frequency_>: 确定攻击是否可被受害者检测到 的随机抽取频率。

默认值: always

attack_attribution_draw_frequency <draw_frequency_>: 确定攻击是否被受害者归因的 随机抽取频率。

默认值: always

future_immunity_draw_frequency <draw_frequency_>: 确定受害者是否对未来同类型攻 击免疫的随机抽取频率。

默认值: always

# 4.16.2.1.脚本攻击效果 WSF_CYBER_SCRIPT_EFFECT

```txt
cyber Effect <effect_name> WSF_CYBERScriptEffect
platform_type <type>
    ... effectScripts definitions
    script void Attack ... end_script
    script void Restore ... end.script
    end-platform_type
platform <name>
    ... effectScripts definitions
    script void Attack ... end.script
    script void Restore ... end.script
    end-platform
default
    ... effectScripts definitions
    script void Attack ... end.script
    script void Restore ... end.script
    end_default
end.cyber-effect 
```

# 概述

WSF_CYBER_SCRIPT_EFFECT 是一种 cyber_effect，允许用户使用脚本语言定义效果。

注意：此效果在 CyberAttack 启动调用期间不需要用户提供数据。

platform_type <type> ... end_platform_type: 为平台类型定义效果脚本。此命令可以根据需要重复使用。  
platform <name> ... end_platform: 为特定平台定义效果脚本。此命令可以根据需要重复使用。  
default ... end_default: 为未通过 platform 或 platform_type 指定的任何受害者定义效果脚本。此命令仅有效一次，多个此块的实例将仅使用最后声明的实例。

效果脚本

要实现一个效果，必须定义两个脚本：

```txt
script void Attack(WsfCyberEngagement aEngagement)  
end_script 
```

```txt
script void Restore(WsfCyberEngagement aEngagement)  
end_script 
```

‘Attack’脚本：当确定攻击将发生时调用。该方法应采取必要的行动以实现效果。

‘Restore’脚本：当确定受害者已从攻击中恢复时调用。该方法应采取必要的行动以撤销‘Attack’脚本所采取的行动（本质上是将平台恢复到攻击前的状态）。

这种结构允许用户在 AFSIM 中灵活地使用脚本语言来定义和管理网络攻击的效果，从而更好地模拟和应对潜在的网络威胁。

# 4.16.2.2.加强脚本攻击效果 WSF_CYBER_SCRIPT_EFFECT_ENHANCED

```txt
cyber Effect WsF_CYBERScript_EFFECT_ENHANCED   
platform_type <type> script void Attack(WsfCyberEngagement aEngagement, WsfCyberAttackParameters   
aParameters) ... end Script script void Restore(WsfCyberEngagement aEngagement, WsfCyberAttackParameters   
aParameters) ... end Script   
end platform_type   
platform <name> script void Attack(WsfCyberEngagement aEngagement, WsfCyberAttackParameters   
aParameters) ... end Script script void Restore(WsfCyberEngagement aEngagement, WsfCyberAttackParameters   
aParameters) ... end Script   
end platform   
default script void Attack(WsfCyberEngagement aEngagement, WsfCyberAttackParameters   
aParameters) ... end Script script void Restore(WsfCyberEngagement aEngagement, WsfCyberAttackParameters 
```

```txt
aParameters) ... endScript end_default   
end_cyber Effect 
```

WSF_CYBER_SCRIPT_EFFECT_ENHANCED 是一种 cyber_effect，可以使用脚本语言定义。此效果在功能上等同于 WSF_CYBER_SCRIPT_EFFECT，但支持在攻击调用期间提供的用户参数在脚本上下文中的使用。因此，为此效果的脚本方法重载提供了这些附加参数。

注意：此脚本效果的功能预计将在 AFSIM3.0 中取代标准脚本效果。此效果在CyberAttack启动调用期间不需要用户提供数据。然而，如果提供了此类数据，此类型支持其使用。

命令

platform_type <type> ... end_platform_type: 为平台类型定义效果脚本。此命令可以根据需要重复使用。  
platform <name> ... end_platform: 为特定平台定义效果脚本。此命令可以根据需要重复使用。  
default ... end_default: 为未通过 platform 或 platform_type 指定的任何受害者定义效果脚本。此命令仅有效一次，多个此块的实例将仅使用最后声明的实例。

增强效果脚本

要实现一个效果，必须定义两个脚本：

attack

```txt
script void Attack(WsfCyberEngagement aEngagement, WsfCyberAttackParameters aParameters)  
end_script 
```

‘Attack’脚本：当确定攻击将发生时调用。该方法应采取必要的行动以实现效果。

restore

```txt
script void Restore(WsfCyberEngagement aEngagement, WsfCyberAttackParameters aParameters) end_script 
```

‘Restore’脚本：当确定受害者已从攻击中恢复时调用。该方法应采取必要的行动以撤销‘Attack’脚本所采取的行动（本质上是将平台恢复到攻击前的状态）。

在攻击实例化期间传递的用户提供参数可在这些脚本方法重载的上下文中使用。

这种增强的脚本效果允许用户在 AFSIM 中更灵活地使用用户提供的数据来定义和管理网络攻击的效果，从而更好地模拟和应对潜在的网络威胁。

# 4.16.2.3.禁用传感器攻击效果 WSF_CYBER_TOGGLE_SENSORS_EFFECT

```txt
cyber Effect <effect_name> WSF_CYBER_TOGGLE_SENSORS_EFFECT platform_type <type> ... sensor-effect_targeting definitions target_list <sensor-name> ... <sensor-name> ... end_target_list 
```

```sql
select_all endplatform_type platform <name> ...sensor-effect_targetingdefinitions endplatform default ...sensor-effect_targetingdefinitions end_default end_cyber effected 
```

WSF_CYBER_TOGGLE_SENSORS_EFFECT 是一种 cyber_effect，允许在受影响的受害者平台上禁用一个或多个传感器。

注意：此效果在 CyberAttack 启动调用期间不需要用户提供数据。

# 命令

platform_type <type> ... end_platform_type: 为平台类型定义效果目标。此命令可以根据需要重复使用。  
platform <name> ... end_platform: 为特定平台定义效果目标。此命令可以根据需要重复使用。  
default ... end_default: 为所有不属于提供的平台或平台类型定义的所有平台定义效果目标参数。

注意：此效果尝试匹配最具体的情况以确定哪个块适用于受害者平台。匹配首先尝试通过平台名称，然后通过受害者派生的所有平台类型（从最具体到最不具体），最后使用默认块（如果定义）。如果由于未定义默认块且之前的匹配尝试失败而未找到匹配，则此效果将对受害者平台没有影响。

# 传感器效果目标

对于受此效果影响并匹配定义的平台、平台类型或默认块的平台，提供以下选项以确定受害者上哪些传感器将被关闭：

target_list <sensor-name> ... <sensor-name> ... end_target_list: target_list 定义了应由此效果禁用的传感器名称。任何与提供的名称匹配的传感器将被关闭。所有其他传感器将不受影响。  
select_all: 代替 target_list 指定此命令将禁用受害者平台上的所有传感器。在定义select_all 和 target_list 块命令时，将导致加载场景输入时出现错误。

这种结构允许用户在 AFSIM 中灵活地定义和管理网络攻击对传感器的影响，从而更好地模拟和应对潜在的网络威胁。

# 4.16.2.4.禁用武器攻击效果 WSF_CYBER_TOGGLE_WEAPONS_EFFECT

```txt
cyber Effect <effect_name> WSF_CYBER_TOGGLE_WEAPONS_EFFECT platform_type <type> 
```

```txt
... weapon Effect targeting definitions   
target_list <weapon-name> ... <weapon-name> ... end_target_list   
select_all   
endplatform_type   
platform <name>   
... weapon effect targeting definitions   
endplatform   
default   
... weapon effect targeting definitions   
end_default   
end_cyber-effect 
```

概述

WSF_CYBER_TOGGLE_WEAPONS_EFFECT 是一种 cyber_effect，允许在受影响的受害者平台上禁用一个或多个武器。

注意：此效果在 CyberAttack 启动调用期间不需要用户提供数据。

命令

platform_type <type> ... end_platform_type: 为平台类型定义效果目标。此命令可以根据需要重复使用。  
platform <name> ... end_platform: 为特定平台定义效果目标。此命令可以根据需要重复使用。  
default ... end_default: 为所有不属于提供的平台或平台类型定义的所有平台定义效果目标参数。

注意：此效果尝试匹配最具体的情况以确定哪个块适用于受害者平台。匹配首先尝试通过平台名称，然后通过受害者派生的所有平台类型（从最具体到最不具体），最后使用默认块（如果定义）。如果由于未定义默认块且之前的匹配尝试失败而未找到匹配，则此效果将对受害者平台没有影响。

# 武器效果目标

对于受此效果影响并匹配定义的平台、平台类型或默认块的平台，提供以下选项以确定受害者上哪些武器将被关闭：

target_list <weapon-name> ... <weapon-name> ... end_target_list: target_list 定义了应由此效果禁用的武器名称。任何与提供的名称匹配的武器将被关闭。所有其他武器将不受影响。  
select_all: 代替 target_list 指定此命令将禁用受害者平台上的所有武器。在定义 select_all和 target_list 块命令时，将导致加载场景输入时出现错误。

这种结构允许用户在 AFSIM 中灵活地定义和管理网络攻击对武器系统的影响，从而更好地模拟和应对潜在的网络威胁。

4.16.2.5.禁用通信设备攻击效果 WSF_CYBER_TOGGLE_COMMS_EFFECT  
```txt
cyber Effect <effect_name> WSF_CYBER_TOGGLE_COMMS_EFFECT
platform_type <type>
    ... comm Effect_targeting definitions
    target_list <comm-name> ... <comm-name> ... end_target_list
    select_all
end-platform_type
platform <name>
    ... comm Effect_targeting definitions
end-platform
default
    ... comm Effect_targeting definitions
end_default
end.cyber-effect 
```

WSF_CYBER_TOGGLE_COMMS_EFFECT 是一种 cyber_effect，允许在受影响的受害者平台上禁用一个或多个通信设备。

注意：此效果在 CyberAttack 启动调用期间不需要用户提供数据。

# 命令

platform_type <type> ... end_platform_type: 为平台类型定义效果目标。此命令可以根据需要重复使用。  
platform <name> ... end_platform: 为特定平台定义效果目标。此命令可以根据需要重复使用。  
default ... end_default: 为所有不属于提供的平台或平台类型定义的所有平台定义效果目标参数。

注意：此效果尝试匹配最具体的情况以确定哪个块适用于受害者平台。匹配首先尝试通过平台名称，然后通过受害者派生的所有平台类型（从最具体到最不具体），最后使用默认块（如果定义）。如果由于未定义默认块且之前的匹配尝试失败而未找到匹配，则此效果将对受害者平台没有影响。

# 通信效果目标

对于受此效果影响并匹配定义的平台、平台类型或默认块的平台，提供以下选项以确定受害者上哪些通信设备将被关闭：

target_list <comm-name> ... <comm-name> ... end_target_list: target_list 定义了应由此效果禁用的通信设备名称。任何与提供的名称匹配的通信设备将被关闭。所有其他通信设备将不受影响。  
select_all: 代替 target_list 指定此命令将禁用受害者平台上的所有通信设备。在定义select_all 和 target_list 块命令时，将导致加载场景输入时出现错误。

4.16.2.6.禁用处理器攻击效果 WSF_CYBER_TOGGLE_PROCESSORS_EFFECT  
```txt
cyber Effect <effect_name> WSF_CYBER_TOGGLE_PROCESSORS_EFFECT
platform_type <type>
    ... processor Effect_targeting definitions
    target_list <processor-name> ... <processor-name> ... end_target_list
    end-platform_type
platform <name>
    ... processor Effect_targeting definitions
end-platform
default
    ... processor Effect_targeting definitions
end_default
end.cyber-effect 
```

WSF_CYBER_TOGGLE_PROCESSORS_EFFECT 是一种 cyber_effect，允许在受影响的受害者平台上禁用一个或多个处理器。

注意：此效果在 CyberAttack 启动调用期间不需要用户提供数据。

# 命令

platform_type <type> ... end_platform_type: 为平台类型定义效果目标。此命令可以根据需要重复使用。  
platform <name> ... end_platform: 为特定平台定义效果目标。此命令可以根据需要重复使用。  
default ... end_default: 为所有不属于提供的平台或平台类型定义的所有平台定义效果目标参数。

注意：此效果尝试匹配最具体的情况以确定哪个块适用于受害者平台。匹配首先尝试通过平台名称，然后通过受害者派生的所有平台类型（从最具体到最不具体），最后使用默认块（如果定义）。如果由于未定义默认块且之前的匹配尝试失败而未找到匹配，则此效果将对受害者平台没有影响。

# 处理器效果目标

对于受此效果影响并匹配定义的平台、平台类型或默认块的平台，提供以下选项以确定受害者上哪些处理器将被关闭：

target_list <processor-name> ... <processor-name> ... end_target_list: target_list 定义了应由此效果禁用的处理器名称。任何与提供的名称匹配的处理器将被关闭。所有其他处理器将不受影响。  
select_all: 代替 target_list 指定此命令将禁用受害者平台上的所有处理器。在定义select_all 和 target_list 块命令时，将导致加载场景输入时出现错误。

这种结构允许用户在 AFSIM 中灵活地定义和管理网络攻击对处理器系统的影响，从而更好地模拟和应对潜在的网络威胁。

4.16.2.7.修改消息攻击效果 WSF_CYBER_MAN_IN_THE_MIDDLE_EFFECT  
```txt
cyber Effect <effect_name> WSF_CYBER_MAN_INTHE.Middle_EFFECT
platform_type <type>
    ... comm-effect commands
target_list
    <comm1>
        <comm2>
            ...
        <commN>
    end_target_list
all
exfiltrate <boolean>
    script WsfCyberMitmMessage OnSend ...
    script WsfCyberMitmMessage OnReceive ...
end-platform_type
platform <name>
    ... comm-effect commands
end-platform
default
    ... comm-effect commands
end_default
end.cyber Effect 
```

WSF_CYBER_MAN_IN_THE_MIDDLE_EFFECT 是一种 cyber_effect，允许在受害者上注入中间人攻击（Man-in-the-MiddleAttack）。这种效果允许用户丢弃、延迟和修改来自受害者平台的任何传入或传出消息。

注意：此效果在 CyberAttack 启动调用期间不需要用户提供数据。

# 命令

platform_type <type> ... end_platform_type: 为平台类型定义受影响的通信设备和效果行为。此命令可以根据需要重复使用。  
platform <name> ... end_platform: 为特定平台定义受影响的通信设备和效果行为。此命令可以根据需要重复使用。  
default...end_default: 如果受害者不属于任何先前指定的平台或平台类型，则定义攻击

的默认通信设备和行为。

# 常见受害者命令

target_list ... end_target_list: 指定受此效果影响的受害者平台上的通信设备名称。如果列出的通信设备在应用效果时不存在于受害者平台上，则将被忽略。  
all: 指定受害者平台上的所有通信设备将受到此效果的影响。  
exfiltrate<boolean>: 指定此通信设备应尝试将其接收到的每条消息转发回攻击者。这将尝试将消息发送到攻击者上从受害者通信设备可达的第一个通信设备。以这种方式外传的任何消息都将标记为 EXFILTRATED_MESSAGE 辅助数据字段。转发的消息将标记为EXFILTRATION_MESSAGE 辅助数据字段。

默认值: false

脚本

OnSend(script): 当指定的通信设备尝试发送消息时，将调用提供的脚本。此脚本允许更改、延迟或丢弃 WsfMessage。

丢弃消息的示例如下：

```txt
script WsfCyberMitmMessage OnSend(WsfMessage aMessage) # 设置 drop 为 true 以丢弃消息 return WsfCyberMitmMessage.Construct(aMessage, 0, true); endScript
```

OnReceive(script): 当指定的通信设备尝试接收消息时，将调用提供的脚本。此脚本允许更改、延迟或丢弃 WsfMessage。

延迟消息的示例如下：

```txt
script WsfCyberMitmMessage OnReceive(WsfMessage aMessage) #将消息延迟10秒 return WsfCyberMitmMessage.Construct(aMessage,10,false); endScript 
```

这种结构允许用户在 AFSIM 中灵活地定义和管理中间人攻击的效果，从而更好地模拟和应对潜在的网络威胁。

# 4.16.2.8.更改目标武器攻击效果 WSF_CYBER_WEAPONS_RETARGET_EFFECT

```txt
cyber Effect <effect_name> WSF_CYBER_WEAPONS_RETARGET_EFFECT end_cyber-effect 
```

WSF_CYBER_WEAPONS_RETARGET_EFFECT 是一种 cyber_effect，允许攻击者通过提供新的目标轨迹来重新定义受害者的当前目标。在效果完成后，受害者的原始目标将被恢复。此效果不阻止在效果进行期间更改当前目标。该效果不仅限于武器平台，可以针对模拟中的任何平台。

此效果不会改变受害者的轨迹更新机制。因此，如果此攻击提供了轨迹上的更改数据，

任何未来对该轨迹的更新都不会被阻止。请注意，如果提供了虚假轨迹，则不应有任何传入的轨迹更新需要处理。未来的开发迭代中预计会有操纵受害者轨迹数据的功能。

此效果需要在攻击调用时通过 WsfCyberAttackParameters 对象传递用户提供的数据。此效果仅允许一个类型为 WsfTrack 的用户提供参数。此类数据的字符串标识符必须与此特定效果实例化的名称完全匹配，以便效果能够识别哪个参数是为其准备的（因为这可能不是唯一需要用户提供参数的效果）。

警告：此效果在 CyberAttack 启动调用期间需要用户提供数据。任何超出单个轨迹的传递都是错误的。

注意：除非目标具有主动引导，否则此效果可能用途有限。

命令

注意：此效果没有额外的输入。它只需要在场景中实例化，以便稍后由 cyber_attack对象使用。此效果需要在攻击时通过提供重新定位轨迹来对 cyber_attack 调用进行额外输入。这种效果允许用户在 AFSIM 中灵活地重新定位目标，从而更好地模拟和应对潜在的网络威胁。

# 4.16.2.9.远程引爆攻击效果 WSF_CYBER_DETONATE_EFFECT

```txt
cyber Effect WsF_CYBER_DETONATE_EFFECT weapon_name ... weapon_type ...   
end_cyber-effect 
```

WSF_CYBER_DETONATE_EFFECT 是一种 cyber_effect，允许攻击平台远程引爆受害者平台上指定的武器。当攻击成功时，此效果将继续引爆效果中定义名称或类型的武器，直到所有武器被引爆或目标被摧毁。

目前，仅具有基本类型 WSF_EXPLICIT_WEAPON 的武器可以被指定为引爆目标。

注意：此效果在 CyberAttack 启动调用期间不需要用户提供数据。

命令

weapon_type <string>: 所有继承自指定武器类型的武器（只要它们是基本类型WSF_EXPLICIT_WEAPON）将在攻击成功时被引爆。  
weapon_name<string>: 受害者平台上所有具有指定武器名称（由用户在场景中定义）的武器将被引爆。

对于给定的 detonation_effect，可以指定多个 weapon_types 和 weapon_names。只要平台上的武器具有相同的名称、继承自该类型或两者兼有，并且受害者尚未被摧毁，该武器就可以被引爆。

示例

在 目 标 平 台 上 ， “test_weapon” 是 weapon_name ， 而 “TEST_WEAPON” （ 以 及WSF_EXPLICIT_WEAPON）是 weapon_type。

```txt
platform target WSFPLATFORM 
```

```txt
add weapon testweapon TEST_WEAPON quantity 2 end weaponry   
endplatform   
platform attacker WsF PLATFORM add processor CYBERPROCESSOR WsFScript PROCESSOR execute at_time 5 sec absolute PLATFORM.CyberAttack(WsfSimulation.FindPlatform("target","DETO"); end_execute endprocessor   
endplatform   
cyber_attack DETO WSF_CYBER_attack effect Deto_Effect   
end_cyber_attack   
cybereffect Deto_Effect WSF_CYBER_DETONATE_EFFECT weapon_type TEST_WEAPON   
end_cyber-effect 
```

注意事项

weapon TEST_WEAPON WSF_EXPLICIT_WEAPON: 定 义 了 一 个 武 器 类 型 为WSF_EXPLICIT_WEAPON 的武器。

这种效果允许用户在 AFSIM 中灵活地管理和模拟远程引爆武器的网络攻击，从而更好地应对潜在的威胁。

# 4.16.2.10. 丢失目标攻击效果 WSF_CYBER_WEAPONS_UNTARGETED_EFFECT

```txt
cyber Effect <effect_name> WSF_CYBER_WEAPONSUntARGETED_EFFECT end_cyber-effect 
```

WSF_CYBER_WEAPONS_UNTARGETED_EFFECT 是一种 cyber_effect，允许攻击者清除受害者的当前目标。激活后，受害者平台的当前目标将被移除。在恢复后，原始目标将被恢复到受害者平台。请注意，此效果不会阻止在效果进行期间（包括任何传感器更新、任务分配等）更改当前目标（无论是由受害者还是其他原因）。该效果不仅限于武器平台，可以针对模拟中的任何平台。

注意：此效果在 CyberAttack 启动调用期间不需要用户提供数据。

注意：除非目标具有主动引导，否则此效果可能用途有限。

命令

注意：此效果没有额外的输入。它只需要在场景中实例化，以便稍后由 cyber_attack对象使用。

这种效果允许用户在 AFSIM 中灵活地管理和模拟清除目标的网络攻击，从而更好地应对潜在的威胁。

4.16.2.11. 跟踪干扰攻击效果 WSF_CYBER_TRACK_MANAGER_EFFECT  
```tcl
cyber Effect <effect_name> WSF_CYBERTRACKMANAGER_EFFECT   
targetplatform <platform-name>   
targetplatform <platform-type>   
remove_targetplatform <platform-name>   
remove_targetplatform <platform-type>   
inactive_track_purging <boolean-value>   
inactive_raw_track_purging <boolean-value>   
local_track_history_purging <boolean-value>   
# Effect Event Scripts   
script void OnEntry ... endScript   
script void OnExit ... endScript   
script bool OnTrack ... endScript   
script bool OnRawTrack ... endScript   
script bool OnTrackDrop ... endScript   
end_cyber-effect 
```

WSF_CYBER_TRACK_MANAGER_EFFECT 是一种 cyber_effect，允许在受害者处理其主轨迹管理器的轨迹时注入用户自定义行为。此效果旨在影响与用户指定的 target_platform 输入参数匹配的任何平台或平台类型，并且仅影响平台的主轨迹管理器及任何利用主轨迹管理器的其他对象（如处理器）。

多个此类型的效果同时作用于同一受害者时，将按照效果应用的顺序进行处理。这包括在单个网络攻击定义中使用多个此类型的效果，用户应按所需行为的优先顺序排列命名效果。

注意：此效果在 WsfPlatform.CyberAttack 启动调用期间不需要用户提供数据。

# 命令

target_platform <platform-name> / target_platform <platform-type>: 指定此效果有效的明确平台名称或平台类型。  
remove_target_platform <platform-name> / remove_target_platform <platform-type>: 对于派生效果类型，这些命令移除此效果有效的明确平台名称或平台类型。  
inactive_track_purging <boolean-value>: 定义此效果是否允许在效果生命周期内进行非活动轨迹清除。默认值为 true。  
inactive_raw_track_purging <boolean-value>: 定义此效果是否允许在效果生命周期内进行非活动原始轨迹清除。默认值为 true。  
local_track_history_purging <boolean-value>: 定义此效果是否允许在效果生命周期内进行本地轨迹历史清除。默认值为 true。

效果事件脚本

可以为此效果定义以下脚本：

OnEntry: 当效果在受害者上开始时调用一次。

```batch
script void OnEntry(WsfTrackManager aTrackManager) end_script 
```

OnExit: 当效果在受害者上结束时调用一次（如果效果结束）。

```vba
script void OnExit(WsfTrackManager aTrackManager) endScript 
```

OnTrack: 每当轨迹引入轨迹管理器时运行。用户必须返回 true 或 false，true 表示允许轨迹由主轨迹管理器处理，false表示不允许主轨迹管理器接收此轨迹。

```txt
script bool OnTrack(WsfTrack aTrack, WsfTrackManager aTrackManager)  
end_script 
```

OnRawTrack: 每当原始轨迹引入轨迹管理器时运行。用户必须返回 true 或 false，true 表示允许原始轨迹由主轨迹管理器处理，false表示不允许主轨迹管理器接收此原始轨迹。

```txt
script bool OnRawTrack(WsfTrack aTrack, WsfTrackManager aTrackManager)  
end_script 
```

OnTrackDrop: 每当预计从主轨迹管理器中删除轨迹时运行。用户必须返回 true 或 false，true表示允许轨迹由主轨迹管理器删除，false表示不允许主轨迹管理器删除此轨迹。

```txt
script bool OnTrackDrop(WsfTrackId aTrack, WsfTrackManager aTrackManager) endScript 
```

这种效果允许用户在 AFSIM 中灵活地管理和操控轨迹管理器的行为，从而更好地模拟和应对潜在的网络威胁。

4.16.2.12. 轨迹处理攻击效果 WSF_CYBER_TRACK_PROCESSOR_EFFECT  
```txt
cyber Effect WsF_CYBERTRACKPROCESSOR_EFFECT ... WSF_CYBERTRACKMANAGER_EFFECT commands ... target Processor <processor-name> target processor <processor-type> remove_target Processor <processor-name> remove_target Processor <processor-type> end_cyber-effect 
```

WSF_CYBER_TRACK_PROCESSOR_EFFECT 是 一 种 cyber_effect ， 允 许 在 受 害 者 通 过WSF_TRACK_PROCESSOR 处理轨迹时注入用户自定义行为。此效果旨在影响与用户指定的target_platform 输入参数匹配的任何平台或平台类型，以及与用户提供的 target_processor实例名称或类型匹配的任何轨迹处理器。符合条件的受害者平台上的所有轨迹处理器都将受到影响。此效果将针对轨迹处理器指定的轨迹管理器，无论它是主轨迹管理器还是处理器本地的。

多个此类型的效果同时作用于同一受害者时，将按照效果应用的顺序进行处理。这包括

在单个网络攻击定义中使用多个此类型的效果，用户应按所需行为的优先顺序排列命名效果。除 了 用 于 指 定 轨 迹 处 理 器 的 额 外 输 入 外 ， 此 效 果 在 输 入 方 面 与 其 派 生 的WSF_CYBER_TRACK_MANAGER_EFFECT 相同。

注意：此效果在 WsfPlatform.CyberAttack 启动调用期间不需要用户提供数据。

# 命令

target_processor <processor-name> / target_processor <processor-type>: 指定此效果有效的明确处理器名称或处理器类型。  
remove_target_processor <processor-name> / remove_target_processor <processor-type>:对于派生效果类型，这些命令移除此效果有效的明确处理器名称或处理器类型。

这种效果允许用户在 AFSIM 中灵活地管理和操控轨迹处理器的行为，从而更好地模拟和应对潜在的网络威胁。

# 4.16.3. 网络保护 cyber_protect

```txt
cyber_protect <type> <base_type>   
# Defines the response to the attack <attack_type>.   
# Repeat as necessary to handle additional attack types   
attack_response <attack_type> probability_of_scan misdetection ... probability_of_scan_attribute ... probability_of_attack_success ... probability_of_status_report ... probability_of_attack misdetection ... probability_of_attack Attribution ... probability_of_future-immunity ... attack misdetection_delay_time ... attack_recovery_delay_time ... script bool IsVulnerable ... script bool OnScanDetection ... script bool OnAttackDetection ... script bool OnAttackRecovery ... end_attack_response   
# Define the default attack response should an attack occur # for an attack type that does not have an accompanying response. attack_response default end_attack_response 
```

cyber_protect 对象定义了平台对网络攻击的响应能力，包括阻止、检测和从攻击中恢复

的能力。每个在模拟中活跃的平台都会显式或隐式地定义一个 cyber_protect 对象。

该对象包含零个或多个 attack_response 块，每个块定义了对特定类型攻击的响应。当尝试攻击时，将根据以下算法选择响应：

1) 尝试找到名称为<T>的 attack_response。  
2) 如果步骤 1 失败，对于<T>继承的每个 cyber_attack 类型，尝试找到名称与继承类型匹配的 attack_response。  
3) 如果步骤 1 和 2 失败，尝试找到名为 default 的 attack_response 条目。  
4) 如果步骤 1、2 和 3 都失败，则使用从 cyber_attack 类型<T>中的默认响应值动态创建的内部响应。

# 实例化和编辑

platform_type <type> <base_type> ... end_platform_type: 在平台类型上实例化 cyber_protect。

```txt
platform_type <type> <base_type>
    cyber_protect <type>
    ...
    end_cyber_protect
end-platform_type 
```

platform <name> <type> ... end_platform: 在平台上添加或编辑 cyber_protect。

```txt
platform <name> <type> # or edit platform <name>
    add cyber_protect <type>
    ...
    end_cyber_protect
end-platform 
```

cyber_protect 对象定义了平台对网络攻击的响应能力，包括阻止、检测和从攻击中恢复的能力。每个在模拟中活跃的平台都会显式或隐式地定义一个 cyber_protect 对象。

# 命令

attack_response [ <attack_type> | default ] ... end_attack_response: 定义对特定攻击类型的响应。<attack_type>必须是已定义的 cyber_attack 类型或单词“default”，用于在没有定义响应的攻击类型时使用。

attack_response 子命令

probability_of_scan_detection [ 0 .. 1 ]: 扫描功能被检测到的概率阈值。默认值来自适用的 cyber_attack 中的 probability_of_scan_detection。  
□ probability_of_scan_attribution [ 0 .. 1 ]: 扫描功能被归因的概率阈值。默认值来自适用的 cyber_attack 中的 probability_of_scan_attribution。  
□ probability_of_attack_success [ 0 .. 1 ]: 攻击被宣布成功的概率阈值。默认值来自适用的 cyber_attack 中的 probability_of_attack_success。  
□ probability_of_status_report [ 0 .. 1 ]: 攻击者立即收到攻击成功或失败通知的概率阈值。默认值来自适用的 cyber_attack 中的 probability_of_status_report。  
□ probability_of_attack_detection [ 0 .. 1 ]: 攻击被受害者检测到的概率阈值。默认值来自适用的 cyber_attack 中的 probability_of_attack_detection。  
▫ probability_of_attack_attribution [ 0 .. 1 ]: 攻击被受害者归因的概率阈值。默认值来

自适用的 cyber_attack 中的 probability_of_attack_attribution。

□ probability_of_future_immunity [ 0 .. 1 ]: 受害者对未来同类攻击免疫的概率阈值。默认值来自适用的 cyber_attack 中的 probability_of_future_immunity。  
□ attack_detection_delay_time <random_time_value>: 受害者意识到攻击所需的时间。默认值为无限。  
□ attack_recovery_delay_time <random_time_value>: 受害者在意识到攻击后从攻击中恢复所需的时间。默认值为无限。

脚本

IsVulnerable (script): 定义一个可选脚本，当对平台进行扫描或攻击时调用。返回 true表示平台易受攻击，返回 false 表示不易受攻击。如果返回 false，则当前进行的扫描或攻击将被中止，而不会向攻击者提供任何通知。

```txt
script bool IsVulnerable(WsfCyberEngagement aEngagement)  
end_script 
```

OnScanDetection(script): 定义一个可选脚本，当对平台进行扫描时调用。可以用于模拟通知其他人有可疑活动发生。

```txt
script void OnScanDetection(WsfCyberEngagement aEngagement) endScript 
```

OnAttackDetection (script): 定 义 一 个 可 选 脚 本 ， 在 攻 击 发 生 并 超 过attack_detection_delay_time 后调用。可以用于模拟通知其他人攻击的发生。

```vba
script void OnAttackDetection(WsfCyberEngagement aEngagement)  
end_script 
```

OnAttackRecovery (script): 定义一个可选脚本，在攻击发生并超过 attack_recovery_delay_time后调用。可以用于模拟通知其他人系统再次正常运行。

```vba
script void OnAttackRecovery(WsfCyberEngagement aEngagement) end_script 
```

这种结构允许用户在 AFSIM 中灵活地定义和管理平台的网络防护能力，从而更好地模拟和应对潜在的网络威胁。

# 5. 工具链

# 5.1. 想定编辑工具 Wizard

# 5.1.1. Wizard 用户指南 Wizard User’s Guide

Wizard 用户指南提供了逐步执行各种任务的说明，回答了“我该如何……”的问题。

# 创建新项目

有两种方法可以创建新项目：

将根场景文件（您将传递给 WSF 应用程序的初始文件）拖放到主窗口 -Wizard。  
选择“文件” -> “新建”菜单选项并创建一个新的 .afproj 文件。

记得通过选择“文件” -> “保存项目”来保存项目。如果项目是通过将场景文件拖放到主窗口创建的，第一次选择“保存项目”选项时，系统会提示您输入项目名称。

下次运行 Wizard 时，您可以通过将之前保存的 .afproj 文件拖放到项目浏览器 -Wizard 或通过“文件” -> “打开”菜单选项来简单地打开项目。

# 编辑场景

加载项目后，您可以开始编辑场景。使用文本编辑器读取、导航和修改场景文件。如果您有使用 Microsoft Notepad、Textpad 或 Notepad $^ { + + }$ 等工具的经验，场景文本编辑器应该会让您感到熟悉，并支持复制、剪切、粘贴、撤销和重做等标准功能。

# 使用自动完成功能

自动完成是一个非常有用的功能，通常在许多软件集成开发环境（如 Visual Studio 和Eclipse）中找到。它根据您正在处理的上下文提供命令建议。例如，如果您正在定义一个平台，您只对平台可用的命令感兴趣。通过命令自动完成，Wizard 可以为您提供适合的命令列表。要使用此功能，请将光标放在您感兴趣的上下文中（这可以是全局的、平台块内的、传感器块内的等），然后使用 Ctrl+Space 键序列。这将弹出一个窗口，显示当前上下文中可用的命令列表。

例如：

要创建新类型的平台，按 Ctrl+Space 并输入“pla”…这将列表过滤到 platform、platform_availability、platform_type 等。  
接下来，使用箭头键突出显示“platform_type”。  
按“Tab”或“Enter”键接受“platform_type”命令。  
注意语法提示功能指示需要为新类型提供名称，例如 type MY_PLATFORM_TYPE。  
再次按 Ctrl+Space，自动完成工具将提供所有可用的 platform_types 列表，选择WSF_PLATFORM。

通过使用自动完成工具，您可以轻松浏览每个 WSF 命令，甚至可以让工具建议已知值（即可用的平台类型）。

# 查找 Wizard 文档

Wizard 附带此用户指南和参考指南，可以在 Wizard 的帮助菜单中访问这些指南。

# 查找 WSF 命令的文档

Wizard 的一个很好的功能是可以快速在文档中找到 WSF 命令。只需在文本编辑器中点击命令并按下“F1”键。或者，选择命令，然后右键单击并从上下文菜单中选择“命令文档”。文档将显示在主窗口底部的上下文帮助选项卡中。

# 查找类型声明的位置

Wizard 提供了一项功能，允许您快速跳转到 WSF 类型声明的文件位置。要使用此功能，只需选择您感兴趣的类型（在文本编辑器中）并右键单击。这将启动右键菜单，其中有一个名为“转到定义”的菜单项…选择此项。文本编辑器中将立即打开一个选项卡，光标将跳转到类型所在的行。

# 查找类型引用的位置

与“转到定义”功能互补，Wizard 提供了“查找引用”功能，提供指定 WSF 类型被引用的文件位置列表。要使用此工具，只需选择您感兴趣的类型（在文本编辑器中）并右键单击。这将启动右键菜单，其中有一个名为“查找引用”的菜单项…选择此项。将出现一个弹出窗口，列出找到类型引用的位置（如果只有一个引用，它将立即跳转到此位置）。

# 查看场景中的平台

Wizard 提供了一个名为平台浏览器的功能，提供当前加载项目中所有平台的树状视图列表。显示可以展开以显示平台的部件。

双击平台或平台部件将打开文本编辑器并导航到相应的定义。

# 查看场景中的平台类型

类型浏览器提供当前加载项目中所有类型的树状视图列表。显示可以展开以显示派生类型。

双击浏览器中的项目将打开文本编辑器选项卡并导航到相应的定义。

# 从 Wizard 运行

Wizard 提供运行 WSF 应用程序的能力。为此，您必须首先使用工具菜单中的仿真管理器（这是一次性配置）在 Wizard 中注册您的应用程序。

接下来，您需要使用场景的设置对话框将应用程序与要运行的场景关联。场景设置可以在项目菜单中访问。

现在，您只需按“F5”或从项目菜单中选择“运行”。WSF 的控制台输出将显示在输出面板的输出选项卡中。

# 在 Mystic 中查看仿真结果

Wizard 提供运行 Mystic 应用程序的能力。

您只需右键单击项目浏览器中列出的任何 .aer 文件，然后选择“用 Mystic 打开”。双击文件或从输出列表中选择它也可以。

# 5.1.2. 参考手册 Reference Guide

# 5.1.2.1. 启动 Start-up

# 5.1.2.1.1. 命令行参数 Command Line Arguments - Wizard

用法

```txt
wizard.exe [<file_name.txt>] 
[<project_file.afproj>] 
{-console} 
<file_name1.txt> <file_name2.txt> </dots> 
```

指定要加载为场景的输入文件。可以指定多个文件，每个文件都会被添加到场景中。

```txt
<project_file.afproj> 
```

指定要打开的现有项目文件的路径。

```txt
-console 
```

指示向导在启动时显示控制台窗口。此窗口显示附加的状态和调试信息。

示例

启动向导并加载 strike.txt 和 dis_interface.txt：

在 Windows 上：

```batch
>> wizard.exe strike.txt dis/interface.txt  
或  
>> wizard.exe c:\project1\scenario1.afproj 
```

在 Linux 上：

```txt
>> wizard strike.txt dis/interface.txt
或
>> wizard /home/user/project1/scenario1.afproj 
```

注意：>> 表示命令行。

# 5.1.2.1.2. 启动对话框 Start Dialog - Wizard

![](images/58e1d886ebb4ae761c4327ab9a0eed5aee4870f324936f2daf82f3ce2f81d6dc.jpg)

启动对话框在应用程序启动时出现。

左侧：对话框的左侧包含一个最近打开文件的列表。将鼠标悬停在文件名上会显示文件的完整路径。用户还可以右键单击文件名以获取选项菜单，其中包括从“最近”列表中移除场景的功能。要打开不在“最近”列表中的文件，可以使用“浏览”按钮导航到所需文件。当选择场景文件时，它们会被添加到“浏览”按钮旁边的编辑框中。

文档块：包含各种链接，指向 AFSIM 提供的文档。这些链接与向导帮助中的文档对话框中出现的链接相同。

右侧：对话框的右侧包含一个“你知道吗”部分，显示应用程序的使用技巧。

这种设计使用户能够快速访问最近使用的文件，并提供了便捷的文档参考和使用提示。

# 5.1.2.2. 应用布局 Application Layout

![](images/b33f47b528850caa0b0618d973ec27546666509b5b15b3e084ccbcb707a2c4df.jpg)

上图显示了向导应用程序的布局，主要组件已标注。

可停靠组件：这些组件中的许多是可停靠的，可以移动到窗口的其他位置，或移到它们自己的“浮动”窗口中。这种设计允许用户根据自己的工作流程和偏好自定义界面布局。

这种灵活的布局设计使用户能够更有效地组织和访问应用程序的功能，从而提高工作效率和用户体验。

# 5.1.2.3. 菜单 Menus

# 5.1.2.3.1. 文件菜单 File Menu - Wizard

![](images/3ef1a410d941ab7befc145562f2640432f48d1a54e26635ff9bb33d1a8c02ecf.jpg)

Open Project… - 浏览以打开一个项目。

这意味着您需要浏览文件系统来选择并打开一个现有的项目。

Open Recent - 打开最近使用的项目。

这功能允许您快速访问最近使用过的项目文件。

New Project - 创建一个新项目。

用于从头开始创建一个新的项目文件夹或工作空间。

NewFile- 在文本编辑器中创建一个新文件。

这将打开一个新的编辑器窗口，供您创建和编辑新文件。

OpenFile- 在文本编辑器中打开一个文件。

选择并打开一个现有的文件进行查看或编辑。

Close Project - 关闭项目。

关闭当前打开的项目，但不退出应用程序。

Save Project… - 保存项目。

将当前项目的更改保存到磁盘。

Export Project… - 将项目保存到一个新目录中。

这通常用于备份或在不同位置存储项目副本。

SaveFile… - 保存当前活动编辑器窗口中的文件。

将当前正在编辑的文件保存到磁盘。

Save File As… - 以不同的名称保存当前活动编辑器窗口中的文件。

这允许您创建文件的副本并以新名称保存。

SaveAll- 保存编辑器窗口中的所有文件。

一次性保存所有打开的文件，确保所有更改都被记录。

PrintFile… - 打印当前活动编辑器窗口中的文件。

将文件内容发送到打印机进行打印。

Save Configuration - 将当前应用程序设置保存到文件。

保存当前的配置设置，以便以后可以恢复。

Load Configuration - 加载已保存的应用程序设置文件。

从文件中恢复之前保存的设置。

Import Configuration Options… - 从应用程序设置文件中导入某些功能。

选择性地导入配置选项，而不是加载整个配置。

Recent Configurations - 从最近使用的应用程序设置文件中选择。

快速访问最近使用的配置文件。

Clear Platform Options - 清除所有平台选项。

重置平台相关的设置到默认状态。

Exit- 退出应用程序。

关闭应用程序并退出。

Annotations- 允许保存和加载地图注释文件。

管理地图注释的功能，便于标记和注释地图内容。

# 5.1.2.3.2. 视图菜单 View Menu - Wizard

![](images/798441890d30f6c0500f40b30c2b683b6ad039cb8363c5f77a5be785c5cc44c5.jpg)

可以通过此菜单打开和关闭应用程序中的各种窗口。

此菜单还包含管理编辑器的选项。

Closeallbutstartup- 关闭除场景启动文件以外的所有文本编辑器。

这意味着您可以关闭所有打开的编辑器窗口，但保留与场景启动文件相关的编辑器。

Close all but included - 关闭所有与场景无关的文本编辑器。

这将关闭所有不属于当前场景的编辑器窗口。

Close inactive - 关闭所有不可见的文本编辑器。

关闭当前未显示在屏幕上的编辑器窗口。

Closeall- 关闭所有文本编辑器。

关闭所有打开的编辑器窗口，无论其状态如何。

# 5.1.2.3.3. 选项菜单 Options Menu - Wizard

![](images/bb3a6289fc9be92934df31579364a071af113bf89a71c6f94ac40a3acfadab33.jpg)

# 5.1.2.3.3.1. 偏好设置 Preferences - Wizard

![](images/df174006f188f325ec443325085ec2577aa907494227ccd8b288b597f142b62e.jpg)

# 偏好设置 - 向导

偏好设置对话框允许用户以多种方式自定义应用程序的显示。它位于“选项”菜单下。

注意：某些偏好设置，例如 Units 和 Mil-Std 2525D Symbology，在 AFSIM 的所有可视化应用程序中共享。 从“文件”菜单中的“SaveConfiguration”将所有偏好设置合并为一个文件。

偏好设置会在应用程序关闭时保存。如果有多个应用程序打开，最后关闭的那个将覆盖共享的偏好设置文件，并且只有它会被保留。

如果有多个应用程序打开，改变共享偏好设置不会立即在所有应用程序中生效。需要重启应用程序以重新加载偏好设置。

每个插件可能会在偏好设置对话框的自己的页面中提供偏好设置。

DeveloperTools- 提供启用或禁用开发者工具菜单的选项，除非用于测试目的，否则不需要这些工具。  
General- 提供隐藏/显示主窗口底部状态栏的选项，改变存储的最近使用配置/场景的数量，以及主题。  
KeyboardShortcuts- 允许用户重新绑定快捷键。来自各种插件的快捷键也会出现在此页面中。  
MapDefinitions- 允许用户定义所需的地图配置文件，并查看所有地图的资源位置。  
Mil-Std 2525D Symbology - 允许用户用 Mil-Std 2525D 符号替换通常显示的平台和轨迹模

型。

Team Visibility - 允许用户控制应用程序中可见的团队颜色。  
Units- 允许用户更改各种值类型的默认显示单位。  
Back-ups - 提供启用或禁用场景自动备份（更改历史记录）的选项。  
TextEditor- 允许用户配置文本编辑器的外观和行为。  
ToolLauncher- 提供设置由向导启动的外部工具的能力。  
Video Capture   
Simulation Manager   
Map Hover Info   
Route Browser   
Map Display

# 5.1.2.3.3.2. 偏好设置-一般性设置 Preferences - General

![](images/92ee158a5fac6b224ec7a671bc604125530efdba5e4010ab98b01d21d5fd58a1.jpg)

GeneralPreferences 页面包含了一些不属于其他偏好设置类别的用户选项。

ShowStatusBar- 切换是否在主窗口底部显示状态栏。状态栏通常用于显示窗口的当前状态信息。  
Recent Configuration Length - 指定在“最近配置”列表中应存储多少个配置。  
Theme- 允许用户在浅色和深色主题之间切换。  
ApplicationBanner- 允许用户指定一个横幅，该横幅将显示在应用程序顶部。用户可以指定文本、文本颜色、字体大小和背景颜色。如果设置了“UseSimulationName”，文本将设置为 simulation_name，否则使用提供的文本。  
Map Overlay Classification Banner - 允许用户启用显示场景中指定的分类、警告和三字代码的功能。

# 5.1.2.3.3.3. 偏好设置-快捷键设置 Preferences - Keyboard Shortcuts

![](images/7d86e889b3a56c3836bbc866c4635e47043c9858439d38129853514e09467a69.jpg)

Keyboard Shortcuts Preferences 页面允许用户更改分配给不同操作的键盘快捷键。这些操作可能是标准快捷键，例如“Assign Groups”和“Selecting Groups”用于平台，或者是插件提供的快捷键。

用户可以通过此页面自定义和管理快捷键，以便更好地适应个人的使用习惯和提高操作效率。

# 5.1.2.3.3.4. 地图定义 Map Definitions

![](images/208193b3a48a055ccb4adb058e2c2b7d02061b161b9c62275171be6dd77df112.jpg)

MapDefinitionPreferences 提供了一个界面，用于向应用程序添加新的地形数据库。点击“AddNewMap”可以添加新地图。新地图需要一个文件和一个名称。右键点击地图可以选择删除或重命名地图。应用程序支持 osgEarth 地球文件，这些文件可以用于结合影像和高程数据来创建背景地图。斜体显示的地图是内置的，不能在偏好设置中更改或删除。

使用 osgEarth 构建的地图示例：

osgEarth 文件允许用户将影像和高程数据结合起来，以创建复杂的背景地图。这种功能使用户能够在应用程序中使用详细的地形信息进行模拟和分析。

这些功能使用户能够灵活地管理和定制地图资源，以满足不同的应用需求。

![](images/4c9739df0da15e85bf2a5ee0b7fa3cbdc5227ddc58cd981e4b50e14f677b44db.jpg)

![](images/cf62b78c7178d161984811e8157d6ab13befb53601724840c9759519b1264505.jpg)

![](images/e71dfa3631655a4bd95d9ef1a68824880321ff2e3b08c2a27e707c0c2670724d.jpg)

MapProfilesSection 允许为沉浸式显示（如系留显示或驾驶舱视图）和导航显示选择地

图。这一功能使用户能够根据不同的显示需求选择合适的地图配置文件，以增强模拟体验。注意：Units 偏好设置在所有 AFSIM可视化应用程序中是共享的。这意味着一旦设置了单位

偏好，它将在所有相关应用程序中保持一致。

这种设置的灵活性和共享性有助于在不同的应用场景中保持一致性和便利性。

# 5.1.2.3.3.5. 偏好-Mil-Std 2525D 符号 Mil-Std 2525D Symbology

Mil-Std 2525D Symbology Preferences 提供了一种在地图显示中查看平台和轨迹的替代方式。通过勾选“Use Symbology”复选框，可以控制是否用 Mil-Std 符号替换通常显示的模型。这些符号与显示对齐。

Show Velocity Vector 选项是一个附加设置，当使用 Mil-Std 符号时会在地图上显示。这些矢量作为平台的图形放大器，显示其运动方向，并以其标准身份相关的颜色表示（友方=青色，敌方 $\mathbf { \bar { \Pi } } = \mathbf { \bar { \Pi } }$ 红色，中立 $\mathbf { \Psi } _ { \cdot } = \mathbf { \Psi }$ 绿色，未知 $\equiv$ 黄色）。

这种符号化的显示方式有助于在复杂的军事模拟中更直观地理解平台的状态和运动方向。

![](images/5a0037d98bb69a2770f02ba81e76998072f516ad6c9d3d868d5ee92ced3749f3.jpg)

# Teams Assignment

团队通过提供的树视图分配给各个身份。默认情况下，蓝队被分配为“友方”，红队被分配为“敌方”，但可以根据需要在树视图中添加或移除团队。为了简化操作，还可以在不同部分之间拖动现有的团队分配。任何未分配给身份的团队都被视为“未知”。

注意：Mil-Std2525D 偏好设置在所有 AFSIM可视化应用程序中是共享的。

# Mil-Std 2525D Icons

在这个上下文中，图标指的是显示符号的最内层部分，并提供平台或轨迹的图形或字母数字表示。类似于平台的模型名称和定义，图标映射可以通过外部文件进行修改或添加。

要添加自定义映射或重新映射现有映射，请将目录“your_install_directory/resources/site”添加到 AFSIM 安装中。在 site 目录中，创建一个 milStdIconMappings.csv 文件以及一个额外的“mil-std2525d”目录。该.csv 文件应有两列：第一列是图标名称，第二列是描述将显示

符号的 20 位 Mil-Std 代码。mil-std2525d 目录是存储附加图像的地方。确保这些图像的名称与.csv 文件中写的 20 位代码相对应（例如“10030100001101040000.png”）。

AFSIM 发布中包含的 mil-std2525d 图标是使用位于 https://www.spatialillusions.com/的Unit Symbol Generate 工具创建的。

注意：在修改 milStdIconMappings.csv 时，确保图标代码正好是 20 位，否则输入将被解释为无效。特别是，Excel 可能会自动截断条目中的前导 0，从而产生无效输入。

# Symbology On the Map Display

当用 Mil-Std 符号替换平台模型时，平台将以完全知识的假设显示。这意味着无论团队、身份或信息的预期可用性如何，只要提供了支持的 20 位代码，完整的符号就会显示。

当替换轨迹时，符号的部分会根据轨迹报告的信息被包含或省略。例如，如果平台的类型未报告但所有其他相关信息都已报告，则图标将被省略，但空间域和侧面等因素仍会影响显示中使用的符号集和标准身份。

![](images/8540c3b8769fd2ae298abc8077ad68b338fe042f5958dc7a29b7fce658d045a8.jpg)

在 non white-cell 场景中，可能更好地通过 Team Visibility 偏好设置隐藏敌对团队，并依赖于轨迹信息。这将防止 Mil-Std 符号被重复显示（一次用于平台，一次用于轨迹）。通过这种方式，可以避免信息的冗余显示，从而保持地图显示的清晰和简洁。

这种设置对于需要精确和简洁信息显示的场景尤其重要，确保用户能够专注于关键的轨迹信息而不被重复的符号干扰。

# 5.1.2.3.3.6. 偏好-团队可见性 Preferences - Team Visibility

TeamVisibility Preferences 提供了一种控制平台团队可见性的替代方式。用户可以使用复选框来显示或隐藏团队，并点击“Apply”应用更改。

这种设置允许用户根据需要调整哪些团队在应用程序中可见，从而帮助用户专注于当前任务或场景中最相关的信息。这在处理复杂的模拟或需要简化显示的情况下尤其有用。

![](images/fde7d331dfa0ecb9120347b34751bb8b36330aa0e649d97ddc787127a4f343c7.jpg)

Team Visibility Preferences 页面控制哪些团队是可见的以及它们的分配颜色。

可见性和颜色：用户可以通过在行编辑中输入团队名称并按下“AddTeam”按钮来添加团队。Visible 复选框控制团队是否对用户可见，而颜色选项控制分配给团队的颜色。可以通过选择团队并按下删除键来移除团队。

默认团队：

us   
united_states   
europe   
china   
russia   
iran   
iraq   
skorea   
nkorea   
neutral   
red   
blue

注意：可以通过命令行选项**-lock_side**使用户无法修改此页面上的选项。

这种设置允许用户灵活地管理团队的可见性和颜色，以便在模拟中更好地识别和区分不同的团队。

# 5.1.2.3.3.7. 偏好-单位 Preferences - Units

![](images/f7d89719ec60d57f27533e8d7a22479eadaa6e16477a4d6ef114c148cd241eba.jpg)

UnitsPreferences 页面控制应用程序中不同类型的值应显示的单位和精度（小数位数）。由于处理方式不同，纬度/经度和时间值还有额外的格式选项。

单位和精度：用户可以选择不同的单位（如米、英尺、公里等）以及设置显示数值的小数位数，以满足特定的需求和标准。

纬度/经度和时间格式：这些值有额外的格式选项，以确保在地图和时间相关的显示中提供准确和一致的信息。

注意：Units 偏好设置在所有 AFSIM 可视化应用程序中是共享的。这意味着一旦设置了单位偏好，它将在所有相关应用程序中保持一致。

这种设置的共享性确保了在不同的应用场景中保持一致性和便利性，特别是在涉及多个应用程序的复杂模拟中。

# 5.1.2.3.3.8. 文本编辑器 Text Editor - Wizard

文本编辑器提供了一个界面，用于显示、编辑、导航和理解你的场景文件。它提供了一套在现代软件集成开发环境（IDEs）中常见的工具（例如，MicrosoftVisual Studio）。这些工具包括：

语法高亮：根据代码的语法结构使用不同颜色来显示文本，以便于阅读和理解。

自动补全：在输入代码时，编辑器会根据上下文自动提供建议，帮助你快速输入完整的代码。

语法提示：当你书写代码时，编辑器会提供实时的语法建议和错误提示，帮助你避免语

法错误。

上下文敏感文档：根据当前光标所在位置，提供相关的文档和帮助信息。

文件导航：允许你在文件中快速跳转到不同部分，提高效率。

以下部分将详细描述每一种工具。

![](images/1cc8eb77aab3df8bfbc51ce9c004a90860575dda726d2a5bf7cb41b3a8db562b.jpg)

# 文本编辑器选项

文本编辑器的选项可以在 Preferences 对话框中找到。选项包括：

ShowLineNumbers：启用后，行号会显示在编辑器左侧边距。  
ShowSyntaxTips：启用后，语法建议会出现在活动编辑器中。  
Auto-complete after ‘.’：启用后，当在对象名称后输入‘.’字符时，Wizard 会提供有效成员函数和/或变量的列表。  
Enable Pop-ups on Undo for Multiple/Different Files：启用后，Wizard 在使用撤销功能进行更改之前，会生成一个确认对话框，尤其是在以下情况下：

□ 影响多个文件  
□ 影响当前在 Wizard Text Editor 中未激活/未聚焦的文件

TabSize：确定按下‘Tab’键时插入的空格数量。  
Font：编辑器文本将以所选字体显示。  
Size：编辑器文本将以所选大小显示。  
Styles：样式决定了 Wizard语法的文本颜色和标记。用户可以使用样式进一步自定义编辑器，并在保存前在示例视图中查看更改。

Note 用户可以通过DeveloperMenu中的首选项选项在编辑器状态栏上启用性能计时器。

用户还可以按住控制键并滚动鼠标滚轮来更改编辑器中的字体大小。

# Margins

编辑区域左侧的 margin 包含行号、与错误、警告、实例和类型相关的图标，以及行折叠框。行折叠功能允许将输入块折叠为单行。点击 $" + \prime$ 和“-”按钮可以展开和折叠部分。行号可以在 Preferences 对话框中禁用。

# Right-Click Menu

右键菜单提供了访问许多针对文本编辑器命令的便捷方式。只需在文本编辑器中的任意位置右键单击即可调出右键菜单。菜单内容会根据上下文（即光标位置和文本选择）而有所不同。

# Syntax Highlighting

Syntax highlighting 为场景文件中的 WSF commands 进行颜色编码，使阅读和理解内容更加容易。以下示例说明了默认的配色方案。

6 $\boxed{\begin{array}{rl}\end{array}}$ platform 10_iads_cmdr IADS_CMDR
7 side red
8 commander SELF
9 position 38:04:06n 117:14:00w altitude 0.0 m agl
10 endplatform
11
12 platform 10_iads_cmdr IADS_CMDR
13 side red
14 commander SELF
15 position 38:04:06n 117:14:00w altitude 0.0 m agl
16 endplatform
17
18 $\boxed{\begin{array}{rl}\end{array}}$ platform 11_iads_cmdr IADS_CMDR
19 side red
20 bad_command 999
21 endplatform
22
23 platform 12_iads_cmdr IADS_CMDR
24 side red
25 endplatform

# Unknown Commands

请注意，未知命令会用红色下划线标出。在这个例子中，第一个平台（10_iads_cmdr）没有错误。第二个平台命令实际上是第一个的编辑版本，因此，IADS_CMDR 不被识别为有效输入。第三个平台块包含一个无效命令。第四个平台块因大写的‘M’而无效。

# Reference Errors and Warnings

Referenceerror（引用错误）发生在需要一个不存在的对象或类型时。当引用对象或类型未找到，但不是模拟执行所必需的，这时会出现 referencewarning（引用警告）。通过右键单击带有引用错误或警告的文本，可以提供选项来纠正问题。当名称被重复使用时，也可能发生引用错误。

# Syntax Tips

SyntaxTips 功能为用户提供关于当前命令接下来期望的指导。在下面的示例中，我们开始输入平台命令，语法提示会自动建议。语法提示可以在首选项中禁用。

![](images/945a9ba06df210b46f77a2c728146fd0c9f6a8375df1ee881687c0869cb46c8a.jpg)

# Command Documentation

通过使用 context sensitive documentation（上下文敏感文档），用户可以快速跳转到任何选定命令的文档。只需右键单击并选择 Command Documentation（命令文档），信息将显示在输出面板的命令文档选项卡中。通过选择“Full Article”链接，可以显示命令来源的实际HTML 页面。

# Go To Include

GoToInclude功能提供了一种通过右键菜单快速导航到场景文件中包含的内容的方法。只需选择“Go To Include: <include-filename>”即可。

# Go To Definition

GoToDefinition 功能提供了一种快速跳转到当前选定 WSFtype（WSF 类型）文件位置的方法。要使用此功能，选择 WSF 类型并使用右键菜单访问“GoToDefinition”选项。此功能也可以在编辑菜单中找到或通过快捷键使用。

# Find References

FindReferences 功能提供了一种快速生成给定类型使用位置列表的方法。在下面的示例中，我们找到了所有对‘SR_SAM_TELAR’平台类型的引用。要使用此工具，选择 WSF 类型并使用右键菜单访问“FindReferences”选项。此功能也可以在编辑菜单中找到或通过快捷键使用。

![](images/498113c47206a85ff76b10af57c1d250ed9786d5477ca5a60e44843a09b43f3a.jpg)

FindInFile功能提供了一种在当前文件中搜索字符串的方法。下面的示例显示了搜索字