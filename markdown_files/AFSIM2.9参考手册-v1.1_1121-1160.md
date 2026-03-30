# Session Notes

MissingPlatforms：通知用户场景中每个在运行 Checks 时未在模拟中激活的平台。如果平台的创建时间晚于运行 Checks 的时间，通知用户平台可能缺失，因为它尚未创建。如果平台的创建时间早于运行 Checks 的时间，通知用户平台可能缺失，因为它已被删除。如果此 Session Note 认为模拟中缺少任何平台，Scenario Analyzer 将为用户提供调整运行 Checks 时间的选项。有关更多信息，请参阅高级功能：修改 Check 执行时间。

# 5.1.2.26.20.3. 脚本实用工具描述 Descriptions of Script Utilities

# 用于传达结果的实用工具

正如添加新 Scenario Analyzer Checks 的教程中所述，Checks 通过记录由表示 Check 信息（套件、严重性和名称）的字符串组成的消息以及描述任何 Check 失败的详细消息来传达其结果，这些结果可以显示在 Scenario Analyzer Results 窗格中。在编写新 Check 时，每次识别到失败时都应调用 SendResultMessage 或 SendResultMessageWithLinks。如果 Check在模拟级别评估条件，最好每次 Check 运行时仅记录一个结果消息。另一方面，如果 Check在平台级别评估条件，则可能会为每个未通过 Check 的平台记录一个结果，这可能导致Scenario Analyzer Results 窗格中单个 Check 的详细消息有很多行。

请记住，除非 Check 调用这些实用工具之一，否则 Check 将不会出现在 Results 窗格中 —— 即 使 它 已 被 选 择 并 运 行 。 例 如 ， 如 果 Check 每 次 识 别 到 失 败 时 调 用SendResultMessage，但在场景通过 Check（即没有失败）时未发送消息，则每当 Check 通过时，它将从 Results 窗格中消失。有关在 AFSIM 脚本中完全定义 Check 的建议方法的示例，请参阅教程中处理 Check 定义的部分。

void SendResultMessage(string suite, string severity, string check, string detail)

使结果添加到 Scenario Analyzer Results 窗格中的 Check Results 树。

□ suite 应类似于定义 Check 的文件名，因为 Scenario Analyzer Checks 窗格使用文件名来确定套件名称。

□ severity 在失败的情况下应为 ‘WARNING’ 或 ‘ERROR’，如果整个场景通过了 Check，则为 ‘PASS’。（SendPassMessage 也可用于报告通过。）  
▫ check 表示 Check 的名称，将显示在 Results 窗格中。它应与套件文件中的 Check脚本名称匹配，但用空格替换下划线。  
□ detail 应包括帮助分析人员识别和修复导致 Check 失败的问题的任何信息。

下面是此实用工具的示例调用及相应的 Check 结果：

```javascript
ScenarioAnalyzerUtilssendResultMessage( "Core", "Declared commander should be in that command chain", "WARNING", "Platform e identifies b as its commander in command chain THIRD, but b is not in that command chain.)); 
```

```txt
- All results
- Check Results
- Core
- WARNING (1)
- Declared commander should be in that command chain
- Platform e identifies b as its commander in command chain THIRD, but b is not in that command chain. 
```

void SendResultMessageWithLinks(string suite, string severity, string check, string detail, Array<string> linkedLocationTypes, Array<string> linkedLocationNames)

使结果添加到 Scenario Analyzer Results 窗格中的 Check Results 树中，并在详细消息中添加指向场景文件中相关位置的超链接。

此实用工具利用 Wizard 的功能来导航 AFSIM 项目文件，以允许定义新 Checks 的人员将 Check 结果与场景文件中的相关“位置”关联。右键点击结果的详细消息将弹出一个包含超链接位置的上下文菜单。

位置由“类型”和“名称”标识。Check 作者希望添加链接的所有位置的类型必须出现在linkedLocationTypes 数组中，而所有位置的名称必须出现在并行的 linkedLocationNames 数组中。以下类型将生成有效链接：'platform'（不是 'platforms'）、'sensors'、'processors'、'weapons' 和 'comms'。位置的名称必须是 AFSIM 脚本中调用 Name() 或 ${ \mathsf { C } } { + } { + }$ 中调用GetName() 的结果。

下面是此实用工具的示例调用及相应的 Check 结果：

```txt
// sensor fails the Check if it is not linked to any WsfTrackProcessor  
if (linkedTrackProcs.Size() <= 0 && linkedTrackMgrs.Size() <= 0)  
{  
    checkPassed = false;  
    Array<string> fileLocationTypes = Array<string>();  
    Array<string> fileLocationNames = Array<string>();  
    fileLocationTypes.PushBack("platform");  
    fileLocationNames.PushBack平台上。);  
    fileLocationTypes.PushBack("sensors");  
    fileLocationNames.PushBack(sensor.Name()); 
```

```javascript
string message = "Sensor " + sensor.Name() + " on platform " + platform.Name() + " is not linked directly or indirectly to a track processor"; ScenarioAnalyzerUtilities.SendResultMessageWithLinks-suite, check, severity, message, fileLocationTypes, fileLocationNames); 
```

```txt
Scenario Analyzer Results  
Results Generated Scenario File wsf_exec Output  
All results Check Results demo WARNING (1) Sensors should be linked to track processors Sensor unlinkedsensor on platform sensorplatform_2 is not linked directly or indirectly to a track processor  
Session Notes Go to platform sensorplatform_2 Go to sensor unlinked SENSOR 
```

void SendPassMessage(string suite, string check)

调用 SendPassMessage 等效于调用 SendResultMessage，其严重性值为 ‘PASS’，详细值为 ‘Scenario passed this check.’（对于通过的检查，不显示详细消息。）

# 用于传达结果的实用工具

void SendSessionNoteMessage(string sessionNote, string detail)

在 Scenario Analyzer Results 窗格中 Check Results 树下方生成一个名称为 sessionNote且详细消息为 detail 的 Session Note 结果。

# 用于导航指挥链的实用工具

除了 GetTopCommander 之外，用于导航指挥链的实用工具以原始平台为起点，递归地向上或向下搜索一个或所有原始平台的指挥链，寻找通过 checkName 参数指定的脚本定义检查的任何平台。如果遇到任何通过检查的平台，这些实用工具将返回 true。checkName 必须是一个在全局脚本上下文中可访问的 AFSIM 脚本名称（在模拟级别），该脚本以一个WsfPlatform 作为参数并返回一个布尔值。

WsfPlatform GetTopCommander(string commandChain, WsfPlatform origin)

返回在指定指挥链上位于 origin 之上的顶级指挥官（指挥官 $\mathsf { \Lambda } = = { \mathsf { S E L F } }$ 的平台）。

bool CheckDownOneCommandChain(WsfPlatform origin, string checkName, string commandChain)

如果 checkName 指定的脚本对 origin 或在名为 commandChain 的指挥链上从属于origin 的任何平台返回 true，则返回 true。

▪ bool CheckDownAllCommandChains(WsfPlatform origin, string checkName)

如果 checkName 指定的脚本对 origin 或在任何指挥链上从属于 origin 的任何平台返回 true，则返回 true。

此实用工具通过在 origin 上调用名为 checkName 的脚本，然后在 origin 所属的每个指挥链上的每个下属上调用该脚本，依此类推递归地工作。即使与 origin 没有共同指挥链的平台通过检查，此实用工具也可能返回 true。例如，使用下图中的指挥链结构，以平台 a作为起点调用 CheckDownAllCommandChains 将在 a 上调用指定的检查，并在 a 的下属 b和 c 上调用检查。它还将在 b 的下属 d 和 e 上调用检查。因此，如果平台 e 是唯一一个 checkName 指定的脚本返回 true 的平台，即使平台 e 与起始平台 a 没有共同的指挥链，实用工具也将返回 true。

![](images/a228721d67dd98a4a4dcccf447e8aeb4eebf91b28589d60962e2b349a5f2e37f.jpg)

bool CheckUpOneCommandChain(WsfPlatform origin, string checkName, string commandChain)

如果 checkName 指定的脚本对 origin 或在名为 commandChain 的指挥链上优于origin 的任何平台返回 true，则返回 true。

bool CheckUpAllCommandChains(WsfPlatform origin, string checkName)

如果 checkName 指定的脚本对 origin 或在任何指挥链上优于 origin 的任何平台返回true，则返回 true。有关实用工具如何检查平台的所有指挥链的说明，请参阅CheckDownAllCommandChains。

bool CheckFullCommandChain(WsfPlatform origin, string checkName)

如果 checkName 指定的脚本对 origin 所属的任何指挥链中的任何平台返回 true，则返回 true。此实 用工具通过 识别 origin 所属的每个指挥链中的顶级指挥（使用GetTopCommander），然后对每个顶级指挥调用 CheckDownOneCommandChain 的等效方法，使用指挥官和 origin 共享的指挥链名称作为 commandChain 参数。

用于识别连接平台部件的实用工具

此类别中的每个实用工具返回一个与原始平台或平台部件以特定方式连接的WsfPlatformParts 数组。每个实用工具还接受一个字符串参数 partType：只有当平台部件的类型与 partType 匹配时，连接的平台部件才会包含在返回的数组中。平台部件的类型是否匹配是通过调用 WsfObject::IsA_TypeOf(partType) 确定的，该方法期望部件的基类名称而不是其脚本类名称。例如，如果对 LinkedAndReachablePlatformParts 的调用应返回所有链接到WsfPlatformPart origin 的 WsfTrackProcessors ， 则 partType 必 须 是'WSF_TRACK_PROCESSOR'，而不是 'WsfTrackProcessor'。

Array<WsfPlatformPart> GetPlatformPartsDownOneCommandChain(WsfPlatform origin, string partType, string commandChain)

返回一个数组，其中包含位于 origin 或在指定指挥链上从属于 origin 的平台上的所有类型为 partType 的平台部件。

用于识别连接平台部件的实用工具

Array<WsfPlatformPart> GetPlatformPartsDownAllCommandChains(WsfPlatform origin, string partType)

返回一个数组，其中包含位于 origin 或在任何指挥链上从属于 origin 的平台上的所有类型为 partType 的平台部件。此实用工具通过在 origin 上寻找匹配的平台部件，然后在origin 所属的每个指挥链上的每个下属上寻找匹配的平台部件，依此类推递归地工作。因此，返回的平台部件中的一些或全部可能位于 origin 不属于的平台上。有关实用工具如何检查平台的所有指挥链的说明，请参阅 CheckDownAllCommandChains。

Array<WsfPlatformPart> InternallyLinkedPlatformParts(WsfPlatformPart origin, string partType)

返回一个数组，其中包含与 origin 直接（通过从 origin 到其他平台部件的 internal_link）或间接连接的所有类型为 partType 的平台部件。如果 origin 具有到中间平台部件的internal_link，而中间平台部件又具有到其他部件的 internal_link，则平台部件 otherPart 间接链接到 origin。在 origin 和 otherPart 之间可能有任意数量的中间平台部件。请记住，内部链接是有方向的：只有当两个部件之间的所有链接都指向 origin->otherPart 方向时，otherPart 才链接到 origin。

Array<WsfPlatformPart> LinkedAndReachablePlatformParts(WsfPlatformPart origin, string partType)

返 回 一 个 数 组 ， 其 中 包 含 通 过 同 一 平 台 上 的 内 部 链 接 （ 即 那 些 由InternallyLinkedPlatformParts 返回的部件）或通过内部链接、外部链接和兼容通信设备网络连接到 origin 的所有类型为 partType 的平台部件。实用工具通过查找所有脚本处理器（包括派生类型如跟踪处理器）和通过内部链接连接到 origin 的链接处理器来发现外部链接。然后，实用工具跟随这些外部链接以找到处理器报告的平台。单独的外部链接不足以使一个平台上的部件可由另一个平台上的部件访问。外部链接必须与类型为 WsfCommXmtrRcvr 或派生类型的通信设备相关联，这些设备 (1) 在同一网络上，(2) 能够适当地传输和接收外部链接的方向，并且 (3) 通过正确方向的内部链接连接到目标平台部件。

下面的代码块包含一个示例，其中 cmdr 平台上的 WsfTrackProcessor 从 sub 平台上的 WsfGeometricSensor 链接且可达。如果 report_to 语句或任何一个内部链接丢失，track_proc 将不再从 sensor1 链接且可达。同样，如果 comm1 和 comm2 不在同一网络上，如果 comm1 缺乏传输能力，或者 comm2 缺乏接收能力，track_proc 将不再从传感器链接且可达。

```fortran
platform sub WSF_PLATFORM
commander cmdr
add comm comm1 WSFCOMM XMTR
    network_name local_net
end_comm
add Processor linkedProc WSFLINKEDPROCESSOR
    report_to commander via comm1
end Processor
add sensor sensor1 WSFGEOMETRIC_SENSOR
    on
    frame_time 1s
    reports_range
    internal_link linked Proc 
```

```txt
end_sensor   
endplatform   
platform cmdr WSF PLATFORM   
commander SELF   
add comm comm2 WSFCOMM_RCVR network_name local_net internal_link track_proc   
end_comm   
add processor track_proc WSFTRACKPROCESSOR purge_interval 60 s   
endprocessor   
endplatform 
```

在跟随外部链接时，实用工具递归搜索每个新发现平台上的脚本处理器和链接处理器，并跟随这些链接（只要通信设备配置正确）。这意味着在 origin 和其链接且可达的部件之间可能出现任意数量的中间平台。

Array<WsfPlatformPart> LinkedAndReachablePlatformPartsChooseProcs(WsfPlatformPart origin, string partType, Array<string> processorTypes, bool followSpecifiedProcs)

此实用工具与 LinkedAndReachablePlatformParts 几乎相同，但有一个重要例外。虽然LinkedAndReachablePlatformParts 跟随其遇到的所有外部链接（只要通信设备配置正确），但 LinkedAndReachablePlatformPartsChooseProcs 允许调用者指定一个处理器类型列表，表示 (1) 在搜索链接且可达的平台部件时应跟随其外部链接的处理器类型，或 (2) 应忽略其外部链接的处理器类型。布尔参数 followSpecifiedProcs 确定是否应跟随或忽略属于processorTypes 列 表 中 类 型 的 外 部 链 接 。 如 果 followSpecifiedProcs $= =$ true ，则只有processorTypes 中包含的类型的处理器才会评估其外部链接。如果 followSpecifiedProcs $= =$ false，则除 processorTypes 中列出的类型外，所有脚本或链接处理器都会评估其外部链接。对于确定将跟随哪些外部链接的一般规则有一个重要例外：如果最初作为 origin 传入的平台部件具有外部链接，则即使 origin 的类型通常会被忽略，这些链接也会被跟随。

例如，Core 套件中的一个 Check 警告成对的跟踪处理器相互报告融合跟踪。Check 旨在捕获通过任何中间链接处理器或脚本处理器（除中间跟踪处理器外）相互报告的两个跟踪处理器。为了此 Check 的目的，图中所示的 WsfTrackProcessor B 从 A 是“链接且可达”的，但 WsfTrackProcessor C 不是。

```txt
WsfTrackProcessor A -> WsfLinkedProcessor -> WsfTrackProcessor B  
WsfTrackProcessor C 
```

想要在 AFSIM 脚本中重新实现此 Check 的人可以通过传递一个包含一个项目的Array<string> - 'WSF_TRACK_PROCESSOR' - 作为 processorTypes 参数，并传递 false 作为最后一个参数，来根据 Check 的“链接且可达”定义发现所有从 WsfTrackProcessorA 链接且可达的跟踪处理器。以 WsfTrackProcessor A 为起点，其外部链接将被跟随，WsfLinkedProcessor的外部链接也将被跟随。然而，WsfTrackProcessorB 的外部链接将不被跟随，因此实用工具将正确识别 B，而不是 C，从 A 是“链接且可达”的。有关使用此实用工具在 AFSIM 脚本中完整实现 Check 的教程，请参阅教程。

# 5.1.2.26.20.4. 添加新的想定检查 Adding New Scenario Analyzer Checks

添加新 Scenario Analyzer Checks

本 节 将 以 教 程 的 形 式 解 释 如 何 向 Scenario Analyzer 添 加 自 定 义 Checks 和SessionNotes。用户可以选择仅使用 AFSIM 脚本语言，也可以结合使用 AFSIM 脚本和 ${ \mathsf { C } } { + } { + }$ 来定义检查。教程将从两种方法通用的步骤开始。然后，我们将仅使用 AFSIM 脚本添加两个新 Checks。接下来，教程将演示如何结合使用 AFSIM 脚本和 ${ \mathsf { C } } { + } { + }$ 添加 Check。最后，我们将介绍添加 SessionNote 与 Check 过程中的细微差异。由于过程几乎相同，除非另有说明，否则可以安全地假设 Check 文件的说明也适用于 SessionNote 文件。

通用说明

创建新套件文件：

要 为 Scenario Analyzer 添 加 新 的 检 查 套 件 ， 请 在wsf_install/bin/scenario_analyzer/check_suites 中 创 建 一 个 新 文 本 文 件 。 文 件 名 将 用 作Scenario Analyzer Checks 窗格中相应套件的名称。例如，文件名为 demo.txt 的所有 Checks将显示为 demo 套件的成员。

![](images/acd9228d4e4ef222dd98520fc9dc9a15d1d9876be6b7af3930561e69548ba766.jpg)

Check 文件结构：

Check 文件如 demo.txt 可以包含 AFSIM 场景文件中允许的小子集。以下元素是有效的：

注释：与普通 AFSIM 场景文件中接受的注释格式相同。以 # 或 // 开头的行以及被$/ ^ { * } . . . ^ { * } /$ 包围的所有文本将被忽略。  
Include 语句：如果出现 Include 或 Include_once 语句，必须放在文件顶部的任何脚本块之前。任何不打算作为 Scenario AnalyzerChecks 解析、加载和运行的脚本必须在单独的文本文件中定义，这些文件可以包含在 Check 文件中。  
依赖脚本块：在 ScenarioAnalyzer 从套件加载检查之前，工具首先会验证 Check 文件中指定的任何依赖项是否存在。  
Scenario Analyzer Check 脚本块：所有 Checks 必须在 script...end_script 块中定义，不带参数且返回类型为 void。Check 定义为脚本时给出的名称用于在 Scenario AnalyzerChecks 窗格中显示该 Check，但用空格替换下划线。

定义依赖项：

当创建新的检查套件时，可以添加一个名为 ScenarioAnalyzerDependencies[Suite] 的脚本，该脚本不带参数并返回 void。任何字符串字面值都将被解析为依赖项的名称。依赖项适用于整个检查套件。

```txt
script void ScenarioAnalyzerDependenciesDemo() string dependency1 = "wsf_iads_c2"; Array<string> dependencies = Array<string>(); dependencies.PushBack(dependency1); 
```

```txt
dependencies.PushBack("wsf_mil"); endScript 
```

定义新 Check：

以 script...end_script 块中定义 Check，名称中不能包含空格。

通过调用 ScenarioAnalyzerUtils.SendResultMessage() 生成结果，该方法接受四个字符串参数：套件名称、检查名称、严重性级别和描述 Check 未通过原因的详细消息。

script void Sensors.should_be_linked_to_track_processors() string suite $=$ "demo"; string check $=$ "Sensors should be linked to track processors"; string severity $=$ "WARNING"; string message $=$ "This is just a test"; ScenarioAnalyzerUtilities.SendResultMessagesuite,severity,check, message);   
endScript

加载和运行新 Check：

保存 demo.txt 并点击 Load Checks，您的 Check 应该会出现在名为 demo 的新套件下的 Scenario Analyzer Checks 窗格中。

![](images/baad99a5a0970bc2e32d8912c6a2e33f4ef77c3f234ab6831dfa1f558467bc2b.jpg)

选择并运行此 Check，您将在 Check Results 中看到结果。

![](images/0c503eb9dc2d1706f98262115b8f73e7134c0c650e2d4df55922be2c5296c8d2.jpg)

# 使用 AFSIM 脚本语言添加 Checks

1. 遍历场景中的每个平台和传感器

我们需要遍历场景中的每个平台，然后遍历每个平台上的每个传感器。定义一个布尔变量 checkPassed 并将其初始化为 true，用于跟踪整个场景是否通过了 Check：

```txt
bool checkPassed = true; 
```

```txt
for (int i = 0; i != WsfSimulation platfomCount(); i += 1)  
{  
    WsfPlatform platform = WsfSimulationplatfomEntry(i);  
    for (int j = 0; j != platformSensorCount(); j += 1)  
{  
        WsfSensor sensor = platformSensorEntry(j);  
        // 在每个传感器上进行进一步检查...  
    }  
} 
```

# 2. 检查传感器是否连接到跟踪处理器

Check 要求每个传感器要么具有一个或多个内部链接连接到平台上的跟踪处理器，要么链 接 到 报 告 到 其 他 平 台 的 处 理 器 。 我 们 使 用ScenarioAnalyzerUtils.LinkedAndReachablePlatformPartsChooseProcs 实用工具来寻找与传感器“链接且可达”的跟踪处理器。

```txt
Array<string> ignoreExternalLinks = Array<string>(); ignoreExternalLinks.PushBack("WSFTRACKPROCESSOR"); ignoreExternalLinks.PushBack("WSFTRACKMANAGER");   
Array<WsfPlatformPart> linkedTrackProcs =   
ScenarioAnalyzerUtilities-linkedAndReachablePlatformPartsChooseProcs( sensor, "WSFTRACKPROCESSOR", ignoreExternalLinks, false);   
Array<WsfPlatformPart> linkedTrackMgrs =   
ScenarioAnalyzerUtilities-linkedAndReachablePlatformPartsChooseProcs( sensor, "WSFTRACK_MANAGER", ignoreExternalLinks, false); 
```

# 3. 处理 Check 失败情况

如果两个调用 LinkedAndReachablePlatformPartsChooseProcs 都返回空数组，则传感器未通过 Check。使用 ScenarioAnalyzerUtils.SendResultMessageWithLinks 发送结果消息，描述失败情况，并嵌入指向相关位置的链接。

```txt
if (linkedTrackProcs.Size() <= 0 && linkedTrackMgrs.Size() <= 0)  
{  
    checkPassed = false;  
    Array<string> linkedLocationTypes = Array<string>();  
    Array<string> linkedLocationNames = Array<string>();  
    linkedLocationTypes.PushBack("platform");  
    linkedLocationNames.PushBack platform.Name());  
    linkedLocationTypes.PushBack("sensors"); 
```

linkedLocationNames.PushBack(sensor.Name());   
string message $=$ "Sensor $" +$ sensor.Name() $^+$ "on platform $" +$ platform.Name() $^+$ "is not linked directly or indirectly to a track processor"; ScenarioAnalyzerUtilities.SendResultMessageWithLinkssuite,check,severity, message, linkedLocationTypes, linkedLocationNames);   
}

4. 记录场景通过 Check 的消息

如果所有传感器都通过了 Check，我们记录一个“pass”消息。

if(checkPassed)   
{ string message $=$ "Scenario passed this check."; ScenarioAnalyzerUtilities.SendResultMessagesuite,check,"PASS",message);   
}

5. 运行并查看 Check 结果

保存 Check 的套件文件并点击 Load Checks 按钮刷新可用的 Checks。运行新的 Check后，若场景中有一个传感器未链接到跟踪处理器，您将看到如下结果：

```txt
Scenario Analyzer Results  
Results Generated Scenario File wsf_exec Output  
All results Check Results demo WARNING (1) Sensors should be linked to track processors Sensor unlinked SENSOR on platform sensorplatform_2 is not linked directly or indirectly to a track processor  
Session Notes Go to platform sensorplatform_2 Go to sensor unlinked SENSOR 
```

6. 定义辅助脚本

首先，我们需要在 check_suites/includes/helpers.txt 中定义一个辅助脚本。这个脚本将检查一个平台是否具有具有提交权限的战斗管理器。

script bool PlatformHasBMWithCommitAuthority(WsfPlatform p)   
{ for (int i = 0,PROCCount $=$ p.ProcessorCount();i $! =$ procCount; $\mathrm{i} + = 1$ ） { WsfProcessor proc $=$ p.ProcessorEntry(i); if (proc.IsA_TYPEOf("WSF_UNCLASS_BM")) { WsfUnclassBM bm $=$ (WsfUnclassBM)proc; return bm.HasCommitAuthority(); } } return false;   
}   
endScript

# 7. 包含辅助脚本

在我们的套件文件顶部包含这个辅助脚本文件：

include includes/helpers.txt   
script void ScenarioAnalyzerDependenciesDemo()   
{ string dependency1 $=$ "wsf_iads_c2"; Array<string> dependencies $=$ Array<string>(); dependencies.PushBack(dependency1); dependencies.PushBack("wsf_mil");   
}   
end_script

# 8. 实现 Check

接下来，我们实现 Check，检查每个平台是否具有传感器管理器。如果有，则使用CheckUpOneCommandChain 检查该平台是否在默认指挥链上从属于具有提交权限的战斗管理器的平台。

script void SensorsmanagerPlatforms.must_beConnected_to_battle管理水平with_commit_authoritycript()   
{ string suite $=$ "demo"; string checkName $=$ "Sensors manager platforms must be connected to battle manager with commit authority"; string severity $=$ "ERROR"; bool passedCheck $=$ true; int platCount $=$ WsfSimulationplatFormCount(); for (int i = 0; i != platCount; i += 1) { WsfPlatform platform $=$ WsfSimulationplatFormEntry(i); for (int j = 0,PROCount $=$ platform.ProcessorCount();j $! =$ progCount;j $+ = 1$ ） { WsfProcessor proc $=$ platform.ProcessorEntry(j); if (proc.IsA_TYPEOf("WSF_SENSORS管理系统")) { string scriptName $=$ "PlatformHasBMWithCommitAuthority"; if (!ScenarioAnalyzerUtilities.CheckedUpDownCommandChain平台上，scriptName, "default")) {

passedCheck $=$ false; string detail $=$ "Platform $" +$ platform.Name(） $^+$ " deploys a sensors manager, but neither this platform nor any platform above it in the default command chain deploys a. battle manager with commit authority."; ScenarioAnalyzerUtilities.SendResultMessagesuite, checkName, severity, detail); } } } } if (passedCheck) { string message $=$ "Scenario passed this check."; ScenarioAnalyzerUtilities.SendResultMessagesuite, checkName, "PASS", message); } } end_script

# 9. 运行 Check

保存套件文件并点击 LoadChecks 按钮刷新可用的 Checks。运行新的 Check 后，您将看到结果。如果场景中有一个传感器管理器平台未连接到具有提交权限的战斗管理器，您将收到相应的错误消息。

# 使用 $\mathbf { c } { + + }$ 添加 Checks

在 ${ \mathsf { C } } { \mathsf { + } } { \mathsf { + } }$ 中实现 Check 可以访问一些 AFSIM 脚本语言未公开的功能，但过程比仅使用脚本定义 Check 更复杂。以下是通过创建新的 Mission 插件来重新实现 "Sensors must beinternally linked" Check 的步骤。

# 1. 设置 CMakeLists.txt

在插件的 CMakeLists.txt 文件中，您必须将 ScenarioAnalyzerUtilities.hpp 的路径列为包含目录之一，并链接 scenario_analyzer 库。

# 2. 定义 Check 在套件文件中

Check 仍然需要在 check_suites 目录中的套件文件内的 Scenario Analyzer Check 块中定义。我们将在 check_suites/add_on.txt 中添加我们的 Check。脚本调用另一个脚本方法CheckSensorInternallyLinkedAddOn，该方法属于 ScenarioAnalyzerAddOn 脚本类。

# 3. 注册插件

在 ScenarioAnalyzerAddOn.cpp 中处理插件注册：

```txt
class ScenarioAnalyzerAddOnExtension : public WsfApplicationExtension {   
public: 
```

```cpp
void AddedToApplication(WsfApplication& app) override
{
    UtScriptTypes* scriptedTypes = app.ScriptTypes();
    scriptTypes->Register(new ScenarioAnalyzerAddOnScriptClass.scriptTypes);
}
};
void Registerscenario_analyzer_add_on(WsfApplication& aApplication)
{
    if (!aApplication.ExtensionIsRegistered("scenario_analyzer_add_on"))
    {
        aApplication.RegisterFeature("scenario_analyzer_add_on Plugin",
        "scenario_analyzer_add_on");
        aApplication.RegisterExtension("scenario_analyzer_add_on",
        ut::make_unique<ScenarioAnalyzerAddOnExtension>());
    }
}
extern "C"
{
    UT_PLUGIN exporting void WsfPluginVersion(UtPluginVersion& version)
    {
        version = UtPluginVersion(WSF_PLUGIN_APIMajor_VERSION,
WSF_PLUGIN_APIMinor_VERSION, WSF_PLUGIN_API_COMPILER_STRING);
    }
    UT_PLUGIN exporting void WsfPluginSetup(WsfApplication& application)
    {
        WSFREGISTER_EXTERNAL(application, scenario_analyzer_add_on);
    }
} 
```

# 4. 定义新脚本类

定义一个新的脚本类，并在其中声明 CheckSensorInternallyLinked() 脚本方法：

```txt
class ScenarioAnalyzerAddOnScriptClass : public UtScriptClass   
public: UT.Declare-scriptMethod(CheckSensorInternallyLinkedAddOn); explicit ScenarioAnalyzerAddOnScriptClass(UtScriptTypes\* types) :UtScriptClass("ScenarioAnalyzerAddOn",types) { SetClassName("ScenarioAnalyzerAddOn"); 
```

```cpp
this->AddStaticMethod(new CheckSensorInternallyLinkedAddOn);   
}   
virtual \~ScenarioAnalyzerAddOnScriptClass() {}   
}; 
```

# 5. 定义脚本方法

定义脚本方法并将其连接到实现 Check 的函数：

UT DEFINEScriptMETMethod(ScenarioAnalyzerAddOnScriptClass, ScenarioAnalyzerAddOn, CheckSensorInternallyLinkedAddOn,0,"void",""))   
{ WsfSimulation\*sim $=$ WsfScriptContext::GetSIMULATION(aContext); checkSensorInternallyLinkedAddOn(\*sim);   
}

# 6. 实现 Check

实现 Check 的功能，类似于在 AFSIM 脚本中编写 Checks 的过程：

void checkSensorInternallyLinkedAddOn(WsfSimulation& sim)   
{ bool passedCheck $=$ true; string suite $=$ "AddOn"; string checkName $=$ "Sensors must be internally linked"; string severity $=$ "ERROR"; for (unsigned i $= 0$ ; i $<$ sim.GetPlatformCount(); ++i) { WsfPlatform\* platform $=$ sim.GetPlatformEntry(i); unsigned sensorCount $=$ platform->GetComponentCount<WsfSensor>(); for (unsigned j $= 0$ ; j $<$ sensorCount; ++j) { WsfSensor\* sensor $=$ platform->GetComponentEntry<WsfSensor>(j); if (!sensor->HasInternalLinks()) { passedCheck $=$ false; vector<ScenarioFileLocation> locations; locations emplace_back(ScenarioFileLocation("platform", platform->GetName())); locations.emplace_back(ScenarioFileLocation("sensors", sensor->GetName())); string detailedMessage $=$ "Sensor " + sensor->GetName() + " on platform " + platform->GetName() + " is not internally linked to any other platform component."

+ "Link the sensor to a processor, such as a track processor, using the 'internal_link' command."; string message $=$ buildResultMessagesuite, checkName, severity, detailedMessage, locations); scenarioAnalyzerWriteMessage(message.length(), message.data()); } 1 if (passedCheck) { string message $=$ "Scenario passed this check."; scenarioAnalyzerWriteMessage(message.length(), message.data()); }

# 7. 编译和运行

重新编译并构建 INSTALL 目标，您的新 Check 将在下次加载 Checks 时可用。

# 添加 Session Notes

添加 Session Note 的步骤与添加新 Check 的步骤相同。Session Notes 可以在 AFSIM脚本或 ${ \mathsf { C } } { + } { + }$ 中定义。唯一的区别是定义新 Session Notes 的脚本块必须位于session_note_suites 目录中的文本文件中。

# 5.1.2.26.20.5. 附录：示例代码 Appendix: Sample Code from New Checks Tutorial

Demo 1: Sensors should be linked to track processors (simplified)   
script void Sensors.should_be Linked_to_track_processors() string suite $=$ "demo"; string check $=$ "Sensors should be linked to track processors"; string severity $=$ "WARNING"; string message $=$ "This is just a test"; bool checkPassed $=$ true;   
for (int $\mathrm{i} = 0$ ; i != WsfSimulation PLATFORMCount(); i += 1) { // For every sensor on each platform... WsfPlatform platform $=$ WsfSimulation PLATFORMEntry(i); for (int $\mathrm{j} = 0$ ; j! $\equiv$ platformSensorCount(); j+=1) { WsfSensor sensor $=$ platformSensorEntry(j); // ... find all track processors that it can reach. // Do NOT follow external links from WsfTrackprocessors

```txt
// (which may have a "type" of either WSFTRACKPROCESSOR or WSFTRACKMANAGER) Array<string> ignoreExternalLinks = Array<string>(); ignoreExternalLinks.PushBack("WSFTRACKPROCESSOR"); ignoreExternalLinks.PushBack("WSFTRACKMANAGER"); // Track processors may have a "type" of either WSFTRACKPROCESSOR or // WSFTRACK_MANAGER: Look for both, since a link to either is sufficient. Array<WsfPlatformPart> linkedTrackProcs = ScenarioAnalyzerUtilities.linkAndReachablePlatformPartsChooseProcs(sensor, "WSFTRACK_PROCESSOR", ignoreExternalLinks, false); Array<WsfPlatformPart> linkedTrackMgrs = ScenarioAnalyzerUtilities.linkAndReachablePlatformPartsChooseProcs(sensor, "WSFTRACK_MANAGER", ignoreExternalLinks, false); // sensor fails the Check if it is not linked to any WsfTrackProcessor if (linkedTrackProcs.Size() <= 0 && linkedTrackMgrs.Size() <= 0) { checkPassed = false; Array<string> fileLocationTypes = Array<string>(); Array<string> fileLocationNames = Array<string>(); fileLocationTypes.PushBack("platform"); fileLocationNames.PushBack平台上 name(); fileLocationTypes.PushBack("sensors"); fileLocationNames.PushBack(sensor.Name()); string message = "Sensor " + sensor.Name() + " on platform " + platform.Name() + " is not linked directly or indirectly to a track processor"; ScenarioAnalyzerUtilities.SendResultMessageWithLinkssuite, check, severity, message, fileLocationTypes, fileLocationNames); } } if (checkPassed) { ScenarioAnalyzerUtilities.SendPassMessage-suite, check); } endScript 
```

Demo 2: Sensors manager platforms must be linked to battle managers with commit authority check_suites/includes/helpers.txt (Must be included in demos.txt)   
```txt
//Helper script that will be passed to ScenarioAnalyzerUtilities.CheckedUpDownCommandChain()   
script bool PlatformHasBMWithCommitAuthority(WsfPlatform p) for (int i = 0, proc_count = p.ProcessorCount(); i < proc_count; i += 1) { WsfProcessor proc = p.ProcessorEntry(i); if (proc.IsA_TYPEOf("WSF_UNCLASS_BM")) { WsfUnclassBM bm = (WsfUnclassBM)proc; return bm.HasCommitAuthority(); } } return false;   
end_script   
check Suites/demos.txt 
```

include_once includes/helpers.txt   
script void SMPlatforms.must_be_connected_to_BM_with_commit_authority() string suite $=$ "demo"; string check $=$ "SM platforms must be connected to BM with commit authority"; string severity $=$ "ERROR"; bool check Passed $=$ true; int platform_count $=$ WsfSimulation PlatformsCount(); for (int $\mathrm{i} = 0$ .i $<$ platform_count; i $+ = 1$ ） { WsfPlatform platform $=$ WsfSimulation.EventArgs(i); for (int $\mathrm{j} = 0$ ,proc_count $=$ platform.ProcessorCount();j $<$ proc_count;j $+ = 1$ ） { // If processor is a sensors manager... WsfProcessor proc $=$ platform.ProcessorEntry(j); if (proc.IsA_TypeOf("WSF_SENSORS_MANAGER")) { // ... ensure that at least one platform superior to this platform on // default command chain has a battle manager with commit authority string script_name $=$ "PlatformHasBMWithCommitAuthority"; if (!ScenarioAnalyzerUtilities.CheckedOneCommandChainplatform, script_name,

"default")   
{ // If no BM with commit authority is found, send a result message // describing the check failure. check Passed $=$ false; Array<String> fileLocationTypes $=$ Array<string>(); Array<String> fileLocationNames $=$ Array<string>(); fileLocationTypes.PushBack("platform"); fileLocationNames.PushBack platform.Name()); fileLocationTypes.PushBack("processor"); fileLocationNames.PushBack(prog.Name()); string message $=$ "Platform $^+$ platform.Name() $^+$ " deploys a sensors manager, $^+$ "but neither this platform nor any platform above it in the default \)+\( "command chain deploys a battle manager with commit authority"; ScenarioAnalyzerUtilities.SendResultMessageWithLinkssuite, check, severity,   
message, fileLocationTypes, fileLocationNames); } 1 } } if(check Passed) { ScenarioAnalyzerUtilities.SendPassMessagesuite, check); } end Script

# 5.1.2.26.21. 想定导入 Scenario Importer

![](images/739898e371eda022117afda11bbf4995880fe74157fc9da66e429884c35bbbe9.jpg)

# 5.1.2.26.21.1. 想定导入概览 Scenario Importer Overview

![](images/90b97d140ac2d10c621930d4add8be89263a48ca85820a0287fdae22975a7088.jpg)

# 概述

Scenario Importer 是一个用于 Wizard（AFSIM IDE）的插件。该插件可以用于将现有的场景从未识别或过时的格式转换为包含正确 AFSIM 语法的格式，以便它们可以作为 AFSIM场景运行。插件还可以用于对所需平台参数进行更改，或者简单地对整个模拟进行快速的程序化编辑。从工作流程的角度来看，ScenarioImporter 通过以下五个阶段工作，其中一些是可选的：

预处理阶段：允许用户加载现有的预处理程序，以便将其场景转换为所需格式，通常是CSV 或其他逻辑分隔的场景表示。预处理是可选的，可能并不必要。  
过滤器：在下一阶段可以选择性地应用过滤器，以在格式化之前删除不需要的条目。  
解析阶段：允许分析师使用键对输入数据进行划分和标记。此步骤允许对数据类型进行检查；例如，如果用户将输入的一列标记为纬度值，它将被验证是否在合法范围内，以及检查简单的格式错误和拼写错误。

模板创建：在下一阶段中，用户可以生成格式正确的 AFSIM 平台。各种条件和函数允许用户构建具有不同类型和部件的平台文件，并对命令链、任何数值等进行编辑。  
预览阶段：虽然工作量不大，但允许分析师在继续之前查看他们创建的 Importer 的输出。如果需要，此阶段允许用户将输出保存到按平台类型或任何其他参数指定的文件中。

所有这些阶段的详细描述可以在阶段描述页面上找到，并且可以在演示页面上找到包含所有功能的演示。

文件处理

![](images/dd57ef814f4615d8e6ef8c9a69276613492a8010da5f78419217454024dd331f.jpg)

□ 打开文件 将打开一个文件浏览器，并要求提供包含未格式化内容的基础输入文件。这应该是在应用任何所需预处理之前的文件。  
▫ 选择输出目录 将打开另一个文件浏览器，允许用户选择一个目录，以便保存完成和格式化的文件。在保存任何输出之前，需要指定此目录。  
▫ 分析师可以使用 加载导入器 和 保存导入器 来加速他们的工作流程；一旦为特定类型的输入配置了导入器阶段，它们可以被保存并在以后重新使用。保存的配置只是文本文件，可以放置在任何方便的位置。  
□ 最后，当正确的输出在预览阶段可见且输出目录有效时，保存输出 将保存预览阶段中指定的任何输出文件。

阶段控制

![](images/2c4c87cb41a1b6fd43b4002a9efb8b466c56d8449e15e603ff5bb861e4ef6093.jpg)

在这里可以访问 Importer 处理输入数据的阶段。如果相应的复选框被设置，每个阶段会自动处理任何更改，并且处理从上到下进行。任何阶段中发生的错误将导致其导航按钮变红，在这种情况下，未来阶段所做的任何工作都应视为无效。任何时候一个阶段认为自己完成了处理数据而没有错误，它将变绿；尽管这并不一定意味着用户已经完成了阶段所需的所有工作。

关于阶段配置和输出的更多详细信息在此处描述，并且还有一个演示，逐步使用每个阶

段来格式化场景。

# 5.1.2.26.21.2. 想定导入阶段 Scenario Importer Stages

使用 Scenario Importer 主要包括通过各个阶段进行工作。除了预览阶段外，配置设置下方的输入和输出面板显示阶段处理前后的数据。如果用户指定某个阶段自动处理更改，则可以实时查看更改以检查工作。

# 预处理阶段

![](images/8d6cf92b2d37a56c228c4c66762ab88997106535044205a365569deb2be6009c.jpg)

预处理阶段为用户提供了使用预定义的外部处理程序将输入修改为 Scenario Importer可读状态的机会。这是一个可选步骤，但如果需要在运行后续阶段之前更改要读取的数据，则可能需要此步骤。

# 过滤阶段

![](images/81303630de5fe6599d62530292b3279a537322d31b79fd02c35618747b21d0a9.jpg)

过滤阶段允许用户从每行输入中删除不需要的数据。这些过滤器包括：

文本匹配过滤器：用于根据输入数据中的某些文本模式进行过滤。  
行号过滤器：用于根据特定的输入行进行过滤，可以是块状或单独的行。

# 解析阶段

![](images/f6e1ed31cc1b47f800ebba78b5aa75ed50df4974694d78c063aead62898fad3f.jpg)

![](images/b2b8de49e7ddfc24e4fd1b1fd147edd7bbff3048c375f21ff76429cd795ad1a0.jpg)

解析配置面板为输出面板中创建的每列数据设置了一组数据。有效输入的类型包括：

列名：用于在格式化时检索特定列捕获的数据的名称。  
分隔符：用于解析特定列数据的分隔符，默认为逗号。  
丢弃选项：设置是否在捕获的条目中保留分隔符。  
消耗选项：设置是否保留在当前列中，或推送到下一个列。  
多行输入：用于捕获字段跨多行的平台的全局设置。  
数据类型：可以设置为允许解析器验证列中找到的条目是否为预期类型，数值或其他。在演示中提供了一个组合解析表的示例。列直接在输出面板中创建，我们可以在表头中查看每列的名称、分隔符和数据类型的设置。选择表头条目以编辑任何列的配置。

# 模板阶段

![](images/32ff96d8f4733bcfdf7c7bad1e32283bb23e68ee2cb9ebb2bb5fc8a1069d4c54.jpg)

![](images/9d46290b69a549f922e8bd4350f3b5aad51d48754fccf8a374f8f4ac454db8e2.jpg)

模板阶段允许用户将解析器捕获并验证的数据格式化为 AFSIM 可读的场景文件。ScenarioImporter 将根据平台逐个解释任何用方括号括起来的输入标记，其中标记可以是存储在输入表中的字段或用于操作数据的函数。可用的函数如下所示，并在 ScenarioImporter演示中展示：

[token]：打印在每个条目中找到的名为“token”的列中的条目。  
if ([token]) { output }：仅当该条目为标记存储了内容时，打印格式化输出。  
if ([token] $= =$ value){}：根据标记和值的类型解释比较是否应为数值，并在比较为真时打印输出。  
random (start, end)：打印在开始和结束之间的随机值，截断为 6 位小数。  
translate (heading, distance, latitude, longitude)：给定有效的纬度/经度坐标对，打印在方向上距离为 heading 的坐标对，方向以北为度数。  
toUpper([token]) / toLower([token])：更改输入标记的大小写。当提供长度时，仅更改长度字符的大小写；负长度从右到左更改大小写。

所有上述函数都需要包含在方括号内才能被 ScenarioImporter 解释，否则函数将按原样传递，以便将 AFSIM 脚本写入导入器。此语法可以在演示中看到。

如果模板阶段设置为自动处理更改，可以实时检查格式化输出文件的更新。

![](images/2278455f3d188b451cc4883b1a0566f9e02f6616b5bf5a2bee92fb9788a0adee.jpg)

# 预览阶段

![](images/4e3afa1b82ca47cb42a533f191792e3c7a1f12ca0801e9ce0515c5391c397632.jpg)

预览阶段允许用户在保存之前查看他们创建的格式化输出。可以选择将输出保存到多个文件中，这些文件按用户指定的标记（如平台侧、类别或组）排序。

当所需的输出文件在预览阶段可见且没有错误时，用户现在可以保存输出，并可选择保存当前的导入器设置以加快将来使用导入器的速度。

# 5.1.2.26.21.3. 想定导入示例 Scenario Importer Demo

为了演示用户如何使用 ScenarioImporter，本节将通过一个用例，描述如何从外部提供的原始平台数据构建一个场景，并将其转换为可用于 AFSIM 的场景布局。

# 文件输入

![](images/397007ea5a40598bc1e2fcdac2e4948dddb3a1957143b5485c4dc78a19b09b46.jpg)

第一步是从外部文件加载场景数据。点击“打开文件”按钮将弹出一个新窗口，提示用

户选择感兴趣的输入文件。如果需要任何预处理，则将在下一步中应用。

# 预处理

![](images/ecb35b66c88d3452fc2124524319f1fda75eb88b73f63645cc7e39de8b9beff7.jpg)

用户编写的任何预处理程序都可以加载到预处理器中并应用于原始输入。在此示例中，我们编写了一个简单的可执行文件，仅删除包含不需要的头信息的第一行输入，以便进行后续的导入步骤。外部命令生成的任何错误或警告将写入 Importer 的错误面板，输出可在右下角的输出选项卡中查看，以检查预期的更改。

# 生成解析表

到目前为止，输入数据一直处于原始形式，没有捕获或标记所需的数据类型。用户可能需要生成一个解析表，以将数据组织成标记和命名的列。这对于编写生成所需场景文件的格式模板至关重要。

# 添加解析列

![](images/2f4118fae892f1267d38eef43fd9eb29fa6e126fed15c16a590ca8f87172095d.jpg)

可以通过点击左上角的 $^ { 6 6 } + { } ^ { , 5 }$ 列或右键单击直接设置列数，在输出面板的表格中添加列。也可以通过右键单击其标题条目删除列。

在此示例中，平台将具有最多 10 个唯一数据条目，因为标题包含 10 个条目。

读取多行数据输入

![](images/ec9e9985f32c6d329222550aad9443e8e9d459e286b23e4f088c96bf8ed40ca3.jpg)

我们可以看到，一些平台条目似乎有不在同一行的部件和字段。如果原始数据恰好是这种形式，用户可以勾选“多行输入”，这将强制数据条目填充到最后一列。请注意，在此示例中，没有传感器和图标的条目（即不是 ew_radar 平台的条目）具有额外的分隔符，这些分隔符告诉导入器为特定平台条目添加空白条目。

![](images/4d20c7425dfc9eb30dbd4bcf2d458c56b0e0159b02ef1d8a19266a557f317a28.jpg)

命名和标记数据条目

接下来，数据列应命名，以便可以在下一阶段以编程方式调用它们。点击每个列标题将加载其配置面板，可以在其中填写名称、非逗号分隔符和用于验证的数据类型。标记数据类型不是必需的，但这样做会指示导入器根据其类型检查数据的有效性。

过滤解析错误

![](images/1f34929dd5ae9c5fcbfd0c6af186600f04f8df53d1ae2f4b245143aff62b6944.jpg)

在命名和标记所有数据条目后，解析阶段出现了错误和警告。

错误：无效标记  
警告：找到 9 个空标记

![](images/34e9b3f5e9c11ade2c1e16971b46c99ade7e82392a5ed497b2affa46dad21e09.jpg)

在这种情况下可以忽略警告；它指的是没有传感器和图标的平台的空数据条目，这些条目被认为是正确的。点击错误会将我们引导到被发现无效的数据条目，在这种情况下，200_ew_radar 平台的定位值超出了合法范围或格式不正确。这可以通过保存导入器设置到此点，然后直接编辑输入数据中的条目并重新加载导入器来解决。或者，用户也可以使用过滤阶段删除该特定条目。

使用模板阶段进行格式化

在标记并准备好编写的场景数据后，剩下的就是以正确的格式聚合数据。在此阶段编写的模板将作为从解析器输出的每个数据条目的格式，可以方便地在右下角的模板输入面板上查看。用户可以使用多种函数，这些函数在模板阶段描述中有记录，并在下面演示。

使用标记编写平台部件

![](images/2b59fa4948a7ae34eb4f089206c3ca62def622553b20ec906ae3e27fe2c56c96.jpg)

用户可以使用输入数据中的列名，通过标记符号输入平台部件和字段，标记符号是用方括号括起来的名称：[]。如果我们调用一个不存在于特定记录中的平台部件，它将在格式化输出中显示为空白。用户还可以使用条件语句根据每个平台的情况改变格式，以解决这个问题。

条件格式化

![](images/069cddd6b2eea1ee49bd2007025e9afc3c68d43dd228a5a6e4161ecbce4d5e1a.jpg)

![](images/56d656b34883037908ddc8b21519d96e3fb755addcd451d6d58cd3e4f0fc906e.jpg)

在此示例中，期望仅打印 ew_radar 平台类型的图标。为此，请在模板中编写一个条件，该条件类似于 AFSIM 脚本格式的条件，并在上面链接的模板阶段描述中进行了描述。具体来说，用户可以测试平台类型是否为 EW_RADAR，并仅在这种情况下列出图标，请注意在下面的模板输出中，只有第一个可见的 300_ew_radar 平台被分配了一个图标。

![](images/060151baf91ea9b6fff7d2bfc42ab2c5e37cc438112b99e5ab59d42f2e9d6d4b.jpg)

随机化输出

![](images/5e24bdc8d556095a52fc9802521cede15a512f5f9baba269b1db6b5a2be3bdb6.jpg)

```fortran
platform 10_jads_cmdr IADS_CMDR
    side red
    position 38:04:06n 117:14:00w
    commander 10_jads_cmdr
endplatform
platform 100_radar_company RADAR_COMPANY
    side red
    position 38:41:35n 117:05:57w
    commander 10_jads_cmdr
endplatform
platform 300_ew_radar EW_RADAR
    side red
    position 39:22:34n 117:33:10w
    commander 100_radar_company
edit ew_radar
    transmitter
    frequency 176.083054 mhz
    end_transmitter
    end SENSOR
endplatform 
```

用户还可以选择使用随机标记随机化场景中的任何数值。在上面的示例中，将为包含发射器的任何平台设置 150-180MHz 范围内的随机发射器频率。

平台坐标转换

![](images/01a963f86fcaf5e764d4eb3ae4d7720331ce9da429733cf3ea781a2aeccc387c.jpg)

用户还可以选择在每个平台的基础上转换任何位置数据（纬度和经度）。给定 0-360 度的航向、距离和输入位置，translate 标记将输出一个转换后的纬度-经度对。

![](images/447e143f6f1468e8db6f4716f3a8a7f0b23b67209aca26865779b8af8a8159ba.jpg)

在上面的示例中，将所有平台在 100_radar_company 的指挥下向西移动 240 海里。请注意，如果没有为距离输入单位，导入器将默认使用公里。

更改标记大小写

![](images/b0e2f9e415c54fd1214bfd043502c0d8c531be51ca82e6d63390133c4aa9973a.jpg)

为了方便起见，如果出于任何原因输入场景数据的大小写不正确，还有 toCase 函数。更改可以应用于整个标记或特定长度的选择。

# 完成场景输出

![](images/af98a7b50d1ad0765af0b48a4e58a8905f85862c1edfbc42cc283ce5fa310db0.jpg)

最初，预览阶段将仅显示来自先前模板阶段的输出。从这里，用户可以将输出分成多个文件。如果场景包含多个侧面的平台，用户可以将它们分成每个侧面的文件，或者如示例中所示，用户可以按指挥官将平台分成文件。

![](images/bce719dd11717098f5595245970d1719b6a8b42b78e672b144cb5435228a27ea.jpg)

数据完成后，用户现在可以选择输出目录并保存格式化的输出文件。当前的 ScenarioImporter 配置也可以保存，以便快速处理将来的类似数据。保存配置以供将来使用可以加快将来数据集的处理速度，并减少可能繁琐的数据输入步骤。

成功将场景布局转换为 AFSIM 命令后，导入的文件现在可以由 AFSIM 使用。

![](images/868cffd9ed34c29b3beba9a5587b204a7430b2c885ce921a1cb8e70c266f3ab4.jpg)

# 5.1.2.26.22. SIMDIS

SIMDIS 是由美国海军研究实验室开发的软件工具集，提供实时和后处理模拟、测试和操作数据的二维和三维交互式图形和视频显示。在 Wizard 中集成使用 SIMDIS 可视化应用程序的插件，允许用户更好地可视化和分析数据。

# 配置 SIMDIS

要开始使用，请从工具菜单中选择“配置 SIMDIS…”选项。这将允许您导航到 SIMDIS 应用程序。配置将在未来的 Wizard 会话中被记住。

![](images/0791ccf7a80389522560fdb5a5f66abed23b819d0601d40d676ade73742e1552.jpg)

执行 SIMDIS

一旦配置完成，可以通过右键单击“用 SIMDIS 打开”选项来执行 SIMDIS。

![](images/5cfd0965a5fbbccd4044b03560f164cca4349713fa67eee74b745c3075bfa3d2.jpg)

更改平台图标

右键单击平台图标将提供一个选项，可以从“SIMDIS 模型”子菜单中将图标更改为SIMDIS 模型。这也适用于 simdis_interface 中的 hit_icon 和 kill_icon。

设置 SIMDIS 光束颜色

在 simdis_interface 中右键单击光束颜色将提供一个选项“设置 SIMDIS 光束颜色…”，这将启动一个颜色选择对话框以设置光束的颜色。

通过这些功能，用户可以在 Wizard 中更直观地使用 SIMDIS 进行数据可视化和分析。

![](images/e142f853908c493dc4e78aa6fa4eae8f6e594cb66a553e17eb351e1c505b7b08.jpg)

# Wizard 的任务列表功能

任务列表在 Wizard 中收集来自活动项目文件的任务，并以统一列表的形式呈现，帮助用户导航。任务可以作为提醒或未来工作目标的指示器。任务的分隔字符与注释相同：#、// 和 /**/。任务列表可以从视图菜单访问。

# 功能

任务表

任务在任务表中呈现，这是一个完全可自定义的项目任务视图。默认情况下可见的数据列包括：

文件：任务所在的文件。  
行：任务所在的行号。  
标签：任务的标签。  
描述：任务的描述。

默认隐藏的数据列，可以通过任务列表首选项启用：

列：任务所在的列。  
目录：任务所在的目录。

用户可以通过双击任务表中的任务来查看关联的项目文件中的任务。

# 任务过滤器

任务过滤器允许用户通过文件上下文控制任务的可见性。它包含以下过滤器：

所有场景文件：显示所有场景文件中的任务。  
打开的场景文件：仅显示当前打开的场景文件中的任务。  
当前场景文件：仅显示当前场景文件中的任务。

首选项

![](images/0b8f21157d57802bfb80ccd9730309daca03e7a5caef73e74aa93e1388b7f13d.jpg)

可以通过“选项 $>$ 首选项 $>$ 任务列表”配置任务列表。

# 任务标签

标签是任务列表用于在项目中定位任务的关键字。要添加自定义任务标签，请在“添加新标签”字段中输入标签名称并点击“添加（+）”。要删除标签，请在标签列表中选择它并点击“删除（-）”。

默认标签包括：

ATTENTION：需要注意的任务。  
BUG：存在错误的任务。  
DEBUG：需要调试的任务。  
HACK：临时解决方案的任务。  
TASK：一般任务。  
TODO：待办事项。  
UNDONE：未完成的任务。

# 列顺序和可见性

任务表数据列是完全可自定义的，可以使用位于列可见性列表之间的箭头按钮进行配置。

上箭头：将选定列与前一列交换。  
下箭头：将选定列与后一列交换。  
左箭头：隐藏选定的可见列。  
右箭头：显示选定的隐藏列。

示例

以下是一个包含几个任务的示例场景：

# 这是一条普通注释，不是任务。

#TASK 创建一个类型为 WSF_PLATFORM 的平台，并命名为您选择的名称。

```txt
/\* BUG 
```

以下平台的初始位置不正确。

更改为 1n 2e。

```txt
\*/ 
```

```txt
platform p WSFPLATFORM position 4n 3e end-platform 
```

// UNDONE 以下平台没有初始速度。

```txt
platform q WSF_PLATFORM
add mover WSF_AIR_MOVER
route
    position 0n 0e
    position 0n 1e
    position 1n 1e
    position 1n 0e
    end-route
    end Mover
end platform 
```

在任务列表中，您可以看到来自示例场景的任务：

TASK：创建平台任务。  
BUG：位置错误的任务。  
UNDONE：未完成的速度设置任务。

通过这些功能，用户可以更有效地管理和跟踪项目中的任务。

![](images/2f4becffcd4f056385b1c7f682fb0df60ae4068f68d926175bbfed72ca73936e.jpg)

# 5.1.2.26.24. 翻译功能 Translate Dialog - Wizard

“TranslateScenario” 对话框可以用于翻译整个场景或选择的对象。此工具可以在工具

菜单下的地图实用程序中找到。

警告

Translate 工具无法更改具有空间移动器的平台的位置和方向，因为大多数情况下，移动器不是通过六个自由度定义的，而是通过其他参数定义的。

菜单选项

![](images/97eca6c2fd1e5e4646d98475c61f7bd8d69615177fa4097176cb892a12510673.jpg)

菜单包含以下项目：

“Translate Scenario to…”：此选项将对话框设置为允许用户将整个场景翻译到另一个纬度/经度（绝对翻译）。

“TranslateSelectionto…”：此选项将对话框设置为允许用户将选择的对象翻译到另一个纬度/经度（绝对翻译）。

注意：如果地图上没有任何内容，菜单选项将被禁用。

# 输入方法

行编辑：有两个行编辑框，一个用于纬度，一个用于经度。  
注意：格式为 d:m:s.f(N/S) 表示纬度，d:m:s.f(E/W) 表示经度，“v u”表示距离，其中v 是十进制值，u 是单位。值和单位之间有一个空格。  
在绝对翻译模式下，行编辑框初始化为整个场景/对象选择的纬度和经度。  
滑块：有两个滑块，一个用于纬度，一个用于经度。这允许用户以“动画”风格进行翻译。  
注意：滑块仅按纬度/经度的度数进行翻译。

通过这些功能，用户可以更直观地调整场景或对象的位置。

# 5.1.2.26.25. 单位转换工具 Unit Converter Tool - Wizard

UnitConverterTool用于在常用的标准单位之间进行转换。从下拉框中选择一个UnitType，这将使 ConvertTo下拉框中填充该类型的常用单位。选择要转换到的单位，并在 Value 框中输入一个附加了适当单位的值。Result 框将填充指定 ConvertTo单位的转换值。结果可以手动复制，也可以使用 Copy Result 按钮快速将结果复制到剪贴板。

![](images/6b6d8c59cea39e775c9e59fd5e38b94a696d15b4022bf28c39398b991610f5a6.jpg)

# 5.1.2.26.26. 可视性 Visibility - Wizard

可见性 - 向导

可见性对话框允许用户快速选择在当前场景中哪些团队是可见的。可见性对话框和团队可见性偏好设置反映相同的可见性信息，并在更改时相互更新。在可见性对话框中所做的更改将在应用程序的未来会话中被记住。

团队可见性

团队可见性提供了场景中所有平台团队的可选列表。通过切换其关联的复选框来控制指定平台团队的可见性。

要显示对话框，请在视图菜单下的“可见性”中启用它。

![](images/568bcd8939699325fa9a6899f17eacaf86f251c38791e54a2c7abcde75774ac5.jpg)

启动时，团队可见性将根据团队可见性偏好设置加载。除非有先前定义的设置，否则默认情况下所有平台团队都是可见的。

团队可见性对话框实际上是偏好的扩展，因此每当其中一个被修改时，另一个也会随之更改。

视图上下文菜单

可见性还在视图右键单击上下文菜单中添加了三个操作：“过滤掉选定的平台”、“过滤掉未选定的平台”和“移除所有过滤器”。这些选项位于“可见性”子菜单中。

前两个操作将根据选择的平台隐藏任意数量的平台。这些操作仅在至少选择了一个平台时可用。

第三个操作能够使通过其他两个操作隐藏的任何平台再次可见。

![](images/2d487704e4462c647820171fb89bb7f8e69b25d2fd215670900eee681c9b3ac4.jpg)

# 5.1.3. 语法详解 Grammar Guide

看这篇没用，看例子照猫画虎是最快的。

WSF 语法格式定义了 WSF 命令的语法，并在许多工具和应用程序中用于解析 WSF 文件。许多 WSF 模块已经有现成的语法文件，这些文件可以在 WSF 安装目录的 bin 目录下的 grammar 子目录中找到，文件扩展名为 .ag。开发人员在添加新类型和命令时有责任维护这些语法文件，以确保工具和应用程序能够正确处理 WSF 文件。

语法文件定义

语法文件有两个主要特征：用于解析 WSF 输入的规则和用于创建表示输入文件数据的动作。

规则

序列：最基本的规则是序列，用 { 和 } 符号表示。序列定义了一系列子规则，每个子规则必须依次匹配。

```txt
{rule0 rule1...} 
```

序列中的每个规则都必须匹配，序列才能匹配。在序列中，规则从 0 开始计数，稍后可以使用 \$0 这样的符号引用规则。

字面量：字面量匹配特定的字符串，可以是带引号的字符串或纯文本。解析器假定以空格分隔的标记。

```txt
end_time
"the end time" 
```

规则引用：规则可以在定义后使用 <rule-name> 格式引用。

```twig
<my-rule> 
```

递归：递归是指规则引用可以重复 0 到多次或 0 到 1 次。* 表示 0 到多次， $^ +$ 表示1 到多次，? 表示 0 到 1 次。

{ string_list $\text{串}$ string $>$ \*end_string_list |ABCD{EFG}？
}

使用 * 或 $^ +$ 时，终止字面量的存在很重要。例如，在 stuff <string>* end_stuff 中，任何数量的字符串将被读取，直到找到 end_stuff。但在 stuff<int>* 中，将消耗每个匹配整数规则的标记，并在遇到非整数标记时停止。因此，尽可能提供一个终止字面量。