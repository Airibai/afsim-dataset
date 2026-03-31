# 内置规则

内置规则在 WSF 语法中提供了一些常用的匹配模式，以下是一些关键的内置规则：

<string>：匹配以空格分隔的字符字符串，例如 MY_PLATFORM 或 banana's-apple。  
<quotable-string>：匹配空格分隔的字符串或带引号的字符串，例如 MY_PLATFORM 或 "C:\Program Files\MyPath"。   
<string-except>：匹配任何字符串，但排除指定的例外词。例如：

```txt
(string-except invalid_word1 invalid_word2) 
```

<integer>：匹配整数，例如 0 或 -123。  
<real>：匹配实数，例如 -2、-2.0 或 -2.0e-7。  
(error {})：定义一个匹配时触发错误的序列。例如：

```txt
{ (error {<integer>}） | <string>   
}
```

(delimited…)：定义一个非空格分隔的词，允许在空格分隔输入的情况下匹配不带空格的词。

例如：

```txt
{ (delimited <real> n) | (delimited <real> s) } 
```

(name name-kind)：与 <string> 匹配相同，但将词标识为某种名称，name-kind 指定名称的种类。  
(typeref type-prefix)：与 <string> 匹配相同，但指示匹配的词应为现有类型，type-prefix指定类型在符号表中的键前缀。  
(nocase{…})：使任何序列不区分大小写。例如：

```javascript
(nocase{true|false}）
```

(file-reference file-type) 和 (output-file-reference file-type)：与 <quotable-string> 相同，但标记文本为指定类型的输入或输出文件的位置。  
<TypeCommand>：使用与当前符号关联的规则。  
<ScriptBlock>、<ScriptVariables>、<ScriptFunctionBlock>：用于递归匹配任何字符串，但将文本块标记为属于脚本。

命名规则

命名规则使用以下语法创建：

```txt
rule \*rule-name\*{ \*rules\*   
} 
```

例如：

定义新规则：

```txt
rule my-rule{ end_time<Time> } 
```

使用新规则：

```txt
rule my-rule-2 {
    <my-rule>
    | not <my-rule>
} 
```

命名规则可以重新打开以支持扩展性。例如：

```txt
rule root-command { apple{core|peel}   
}}   
(rule root-command{ banana{seed|peel}   
} 
```

等同于：

```txt
rule root-command { apple{core|peel} | banana{seed|peel} } 
```

结构体

结构体是一种特殊类型的命名规则，表示 WSF 理解的对象。结构体可以包含规则定义和变量。例如：

```txt
(Struct MY_SENSOR :base_type Sensor :symbol (type sensorType MY_SENSOR) 
```

```txt
(var String my_settings)  
{  
    my_command<String> [my_settings=$1]  
| <Sensor>  
}) 
```

结构体可以像规则一样使用 <struct-name> 语法引用。

符号表

在解析使用类型的文件时，需要一个符号表。符号表允许文件引用先前定义的类型。符号表是从键到结构类型的映射，键是字符串的元组。

示例输入文件

```txt
platform_type newtype WSFPLATFORM
    processor y WSFScriptPROCESSOR endprocessor
    weapon z WSF_EXPLICIT_WEAPON endweapon
end-platform_type
platform x newtype
    delete weapon z
end-platform 
```

生成的符号表

<table><tr><td>符号</td><td>类型</td></tr><tr><td>platformType.newtype</td><td>struct Platform</td></tr><tr><td>platformType.newtype processors.y</td><td>struct WSFScriptPROCESSOR</td></tr><tr><td>platformType.newtype.weapons.z</td><td>struct WSFEXPLICITWEapon</td></tr><tr><td>platform.x</td><td>struct Platform</td></tr><tr><td>platform.xprocessors.y</td><td>struct WSFScriptPROCESSOR</td></tr></table>

符号表包含了解析文件所需的信息。例如，如果接下来出现 editplatformx 块，我们可以 确 定 platform.x 存 在 ， 并 且 它 有 一 个 名 为 y 的 处 理 器 ， 其 类 型 为WSF_SCRIPT_PROCESSOR。

符号表维护

符号表的维护通过 new、new_replace、load 和 delete 规则完成。符号表中的位置（键）通过 type 和 subtype 命令引用。

(type…)：指定符号表中的位置。可以有任意数量的参数，每个参数可以是字符串或序列规则引用。

```txt
(type platform x) # -> platform.x  
(type platformType newtype processors y) # -> platformType.newtypeprocessors.y 
```

(subtype…)：与 type 相同，但将参数附加到当前类型。当前类型最初是一个空元组，但可以通过 new、new_replace 或 load 规则更改。  
(new storage-address load-address [:backup load-address])：定义一个尝试创建新符号的规

则。load-address 的符号被复制到 storage-address。如果 storage-address 尚未使用，并且 load-address 指向有效符号，则规则成功。

(new_replace storage-address load-address [:option…])：与 (new …) 相同，但会替换任何现有符号。  
(loadload-address)：从符号表加载现有符号并将其设置为当前符号。如果符号不存在，则规则匹配失败。  
(delete address)：删除现有符号。如果该地址没有符号，则规则匹配失败。

代理（Proxy）

代理提供了语法的语义，构建了输入文件含义的表示。代理与符号表结构相似，但存储关于对象的信息，而不是解析对象的关联规则。

变量

变量是结构体的成员，存储关于对象的数据。变量由类型和名称组成。可用变量类型的完整列表可以在核心语法文件中找到。还有两种容器类型：List 和 ObjectMap。

List：有序对象列表，例如路线的航点。  
ObjectMap：将字符串映射到值类型的关联数组。

在结构体中，变量定义语法如下：

```txt
(var *type* *name* [:default <value>]) 
```

例如：

```txt
(var Real earthRadiusMultiplier :default 1.0)  
(var String myName :default "a name") 
```

动作

动作可以放在序列规则中的条目之前或之后，用于在代理中存储数据。动作放在 [] 字符之间，可以使用 ; 字符指定多个动作。

赋值：将新值分配给属性。

```txt
side=blue  
icon="F-18"  
width="24 inches"  
height=$1 
```

push(attribute-name)：更新当前值为指定属性。  
new(attribute-name, key-name)：向 ObjectMap 属性添加新条目，并将当前对象设置为新值。  
apply($$)：将先前的 (new …) 或 (load …) 规则应用于代理数据结构。  
skip()：进入没有当前代理对象的模式，允许执行规则而不应用任何代理更改。

这些构造共同帮助解析和理解输入文件的结构和内容。

# 5.2. 推演导调工具 Warlock

![](images/2841d31d9df684f71ed34eb86939eb125cc309cd6ef46a7268799f2c296bfa5b.jpg)

Warlock 是一个应用程序，提供图形用户界面（GUI）环境，用于查看和控制高级仿真、集成和建模框架（AFSIM）场景。Warlock 的主要目标是支持 AFSIM 框架内的操作员在环（OITL）战争游戏和实验。Warlock 提供的功能涵盖交战、任务、操作和战略级别的仿真和分析领域。Warlock 提供了一个可扩展的架构和相应的接口，以支持自定义控制和显示。

Warlock 的可配置中央视图默认为一个地图窗口，显示 AFSIM 仿真的状态，周围是可自定义的显示，以支持交战、任务、操作和战略级别的仿真。这些显示包括控制平台、传感器、武器、通信、后勤等的对话框。Warlock 可以在整个仿真环境中提供不受限制的视图，用于白色单元，并提供限制视图以提供团队感知视图，用于红色或蓝色单元。存在一个AFSIM 脚本接口，使操作员可以轻松执行 AFSIM 脚本。此外，Warlock 支持使用通用驾驶舱功能控制单个 AFSIM 实体，并使用操纵杆飞行实体。这允许操作员控制实体并执行可能无法通过其他方式获得的特定操作。

# 用户体验

Warlock 的用户体验专注于简单直观的显示和控制，使用时需要的 AFSIM 知识量最少。用户无需参加 AFSIM 分析师培训课程即可有效使用 Warlock。Warlock 为用户提供了一个现代化的用户界面，其中数据显示可以根据用户的个人偏好进行配置。Warlock 支持保存当前的显示配置、键盘快捷键、偏好设置等。这些保存的配置可以随时加载并在不同用户之间共享。这允许在实验中为不同角色存在不同的配置，例如白色单元操作员的一个配置和蓝色单元驾驶舱控制站的另一个配置。

# 可扩展性

Warlock 设计为可以扩展以满足不断增长的 AFSIM 社区的需求。Warlock 提供了一个定义良好的 API，使开发人员能够快速创建自定义扩展。这类似于 AFSIM 支持扩展的方式。例如，作为 P6DOF 增强功能，Warlock 可以扩展以提供 P6DOF 模型独有的附加数据，并提供对话框以帮助用户调整 P6DOF 模型。Warlock 还可以扩展以提供有关网络漏洞、条件和影响的附加数据，以便操作员了解网络对仿真的影响。Warlock 还可以扩展以提供专用驾

驶舱显示，除了通用驾驶舱显示之外。

# 5.2.1. Warlock 用户指南 Warlock User’s Guide

Warlock 是一个与 AFSIM 集成的操作员在环（OITL）应用程序。

如何运行 Warlock

Warlock 应用程序类似于任务应用程序，支持相同的 AFSIM 场景、命令行参数和插件。以下是 Warlock 与任务应用程序之间的区别：

实时运行：Warlock 旨在实时运行。虽然可以构建性地运行，但某些接口可能无法按预期执行，例如控制实体的能力。  
无命令行参数启动：Warlock 支持在没有命令行参数的情况下启动。如果不使用命令行参数，Warlock 将打开一个启动对话框，用户可以在其中选择要运行的场景文件。  
支持插件：Warlock 不仅支持 AFSIM 插件，还支持 Warlock 插件。Warlock 插件可以具有图形显示和接口。  
多线程应用程序：Warlock 是一个多线程应用程序，其中 AFSIM 在其自己的线程上运行，而图形部分在不同的线程上运行。

从 Wizard 启动 Warlock

Warlock 可以在 Wizard 中注册，以便在 Wizard 中按下运行按钮时执行 Warlock。有关更多信息，请阅读从 Wizard 运行的文档。

存储用户数据

Warlock 的许多部分将存储应用程序的状态，以便下次启动 Warlock 时状态保持不变。

这些信息存储在一个称为配置文件的用户设置文件中。

在 Windows 上，默认配置文件存储在 C:\Users\<user_name>\AppData 目录中。

# Warlock 配置文件管理

Warlock 会在用户更改偏好设置或关闭应用程序时，将应用程序的状态、窗口和偏好设置存储在一个配置文件中。用户可以通过文件菜单中的“保存配置”选项保存 Warlock 的配置。配置也可以通过文件菜单中的“加载配置”选项加载。

此外，配置文件可以被导入，这允许用户选择性地导入配置文件的某些部分。这与“加载配置”不同，因为“加载配置”会加载文件中的所有配置选项。

可以通过命令行使用 -cf 或 -icf 选项加载或导入配置文件，类似于以下命令：

```batch
start warlock.exe -cf StrikeConfig.ini 
```

保存多个配置的好处在于可以轻松地在 Warlock 的不同角色之间切换。用户可以为执行白色单元保存一个配置，为红色单元保存另一个，为单架飞机的操纵杆控制保存另一个，为调整 P6DOF 模型保存另一个。这四种用例将使用不同的窗口和可能不同的偏好设置。保存和加载配置允许用户设置一次配置，然后轻松地在配置之间切换。

# 5.2.2. 参考手册 Warlock Reference Guide

# 5.2.2.1. 启动 Start-up

# 5.2.2.1.1. 命令行启动 Command Line - Warlock

Warlock 支持与任务可执行文件大多数相同的命令行选项。Warlock 始终以实时方式运行，因此不应使用帧步进选项（-fs）。

Warlock 支持在没有命令行参数的情况下启动，并提供一个启动对话框，用户可以在其中选择要运行的场景文件。

# 命令行选项

-?,-h,-help：显示命令行选项并退出。  
-cf<filename>：使用指定的配置文件，修改将保存到指定文件。  
-icf<filename>：导入指定的配置文件，修改不会保存到指定文件。  
-permission_file <filename>：使用指定的权限文件，防止用户编辑权限。  
-console：启用控制台窗口。  
-ups：使用上一个场景，如果没有指定场景。  
-minimized：应用程序将以最小化方式启动。

# 5.2.2.1.2. 启动对话框 Start Dialog - Warlock

![](images/9980f2622a803683fd3890161fbd9b760d9d63d179c6102aa6407c544bc55d0b.jpg)

启动应用程序时会出现启动对话框。

左侧：对话框左侧包含最近使用该应用程序打开的文件列表。将鼠标悬停在文件名上会显示文件的完整路径。用户还可以右键单击文件名以获取选项菜单，其中包括从最近列表中移除场景的功能。要打开不在最近列表中的文件，请使用“浏览”按钮导航到所需文件。当选择场景文件时，它们会被添加到“浏览”按钮旁边的编辑框中。文档块包含各种链接到 AFSIM 提供的文档的链接，这些链接与 Warlock 帮助中的文档对话框中出现的链接相同。

右侧：对话框右侧包含“你知道吗”部分，显示应用程序的提示。

注意事项：

如果指定了多个文件，则第一个文件名后会列出“ $+ { \sf X }$ 更多…”。

如果从命令行执行 Warlock 并提供场景文件作为参数，则启动对话框不会出现。

# 5.2.2.2. 程序布局 Application Layout

![](images/b4e7d794b55c5bdba9697af5e64a2881a23be37bc3eadc43e622a2ad0ad22605.jpg)

# 5.2.2.2.1. 菜单 Menus

# 5.2.2.2.1.1. 文件菜单 File Menu - Warlock

![](images/9de3711764bb6623e1802b2331d6c171eb22ab334e07e0c87d0fea7112117c31.jpg)

Load Scenario…：浏览以加载 AFSIM 场景。  
Recent Scenario：选择从最近执行的 AFSIM 场景中加载。  
Save Configuration：将当前应用程序设置保存到文件。  
Load Configuration：加载已保存的应用程序设置文件。  
Import Configuration Options…：从应用程序设置文件中导入某些功能。  
Recent Configurations：从最近使用的应用程序设置文件中选择。  
Clear Platform Options：清除所有平台选项。  
Exit：退出应用程序。

Annotations：允许保存和加载地图注释文件。

# 5.2.2.2.1.2. 视图菜单 View Menu - Warlock

![](images/c7df2676499fc3f55121f000f9d29cc1fe6868a25f2558498d6af7088d4782d1.jpg)

应用程序中的各种窗口可以通过此菜单打开和关闭。

# 5.2.2.2.1.3. 选项-偏好菜单 Preferences - Warlock

偏好设置对话框允许用户以多种方式自定义应用程序的显示。它位于 Options 菜单下。

共享偏好设置：某些偏好设置，如 Units 和 Mil-Std 2525D Symbology，在所有 AFSIM 的可视化应用程序中共享。“SaveConfiguration”选项会将所有偏好设置合并到一个文件中。  
保存和加载：偏好设置在应用程序关闭时保存。如果打开了多个应用程序，最后关闭的应用程序将覆盖共享偏好设置文件，并成为唯一保留的设置。  
即时生效：如果打开了多个应用程序，更改共享偏好设置不会立即在所有应用程序中生效。需要重启应用程序以重新加载偏好设置。  
插件偏好设置：每个插件可以在偏好设置对话框的其页面中提供自己的偏好设置。

# 偏好设置选项

DeveloperTools：提供启用或禁用开发者工具菜单的选项，通常仅在测试时需要。  
General：提供隐藏/显示主窗口底部状态栏、改变最近使用的配置/场景数量和主题的选项。  
KeyboardShortcuts：允许用户重新绑定快捷键。各种插件的快捷键也会出现在此页面。  
MapDefinitions：允许用户定义所需的地图配置文件，并查看所有地图的资源位置。  
Mil-Std 2525D Symbology：允许用户用 Mil-Std 2525D 符号替换通常显示的平台和轨迹模型。  
Team Visibility：允许用户控制应用程序中可见的团队颜色。  
Units：允许用户更改各种值类型的默认显示单位。  
Simulation：允许用户设置 DIS 偏好和基本仿真设置。  
Network：允许用户为 Warlock 插件设置网络设置。

![](images/f15ba12c777076d8f68284ac11f687b6683014da1665b65e4cda50e0698d9317.jpg)

# 其他功能包括：

Video Capture   
WsfDraw   
Orbits   
Sensor Controller   
Interactions   
Cyber Engagement Browser   
Event Marker   
Map Hover Info   
Platform History   
Sensor Volumes

P6DOF Controller   
Simulation Controller   
Air Combat Visualization   
Head Up View   
Map Display   
Zone Browser   
Visual Effects   
Track Visibility   
Comment Bubbles   
Dialog Builder   
Demo Mode   
Chat

# 5.2.2.2.1.3.1. 偏好-一般 Preferences - General

![](images/493a9e5753211b6801c005067c9cc5f9fa017faddb7f9b9d3cf8653113045fb9.jpg)

# General Preferences 页面

GeneralPreferences 页面包含不属于其他偏好设置类别的用户选项集合。

ShowStatusBar：切换是否在主窗口底部显示状态栏。  
Recent Configuration Length：指示在最近配置列表中应存储多少个配置。  
Theme：允许用户在浅色和深色主题之间切换。  
ApplicationBanner：允许用户指定将在应用程序顶部显示的横幅。用户可以指定文本、文本颜色、字体大小和背景颜色。

如果设置了“Use Simulation Name”，文本将设置为 simulation_name。否则，使用提供的文本。

Map Overlay Classification Banner：允许用户启用显示场景中指定的分类、警告和三字代码。

# 5.2.2.2.1.3.2. 偏好-快捷键 Preferences - Keyboard Shortcuts

![](images/fe5c4853d81bccb9b9b646517a3b463e782666442bc3eec105be27696b5bd42a.jpg)

Keyboard Shortcuts Preferences 页面允许用户更改分配给不同操作的键盘快捷键。这些操作可能是标准快捷键，例如“Assign Groups”和“Selecting Groups”平台，或者是由插件提供的快捷键。

# 5.2.2.2.1.3.3. 地图定义 Map Definitions

![](images/d75b3ef2ec23650edf01fcc68960e0833de77b9fd7576f5c5058ad6175b7568d.jpg)

MapDefinitionPreferences 提供了一个界面，用于向应用程序添加新的地形数据库。点击“AddNewMap”可以添加新地图。新地图需要一个文件和一个名称。右键点击地图可以选择删除或重命名地图。应用程序支持 osgEarth 地球文件，这些文件可以用于结合影像和高程数据来创建背景地图。斜体显示的地图是内置的，不能在偏好设置中更改或删除。

使用 osgEarth 构建的地图示例：

osgEarth 文件允许用户将影像和高程数据结合起来，以创建复杂的背景地图。这种功能使用户能够在应用程序中使用详细的地形信息进行模拟和分析。

这些功能使用户能够灵活地管理和定制地图资源，以满足不同的应用需求。

![](images/98c5f7a34d754458828163a264abb63a1c31a7b25a333b69feee593d15b1acea.jpg)

![](images/c8407736802a832f3172f68374b4ab60d92b81bfc1a9d200f926ba3617b1e303.jpg)

![](images/3729c332902cbf19f39045e42d146686ab9fc05622f459c139eaa6c6d39e5964.jpg)

MapProfilesSection 允许为沉浸式显示（如系留显示或驾驶舱视图）和导航显示选择地

图。这一功能使用户能够根据不同的显示需求选择合适的地图配置文件，以增强模拟体验。注意：Units 偏好设置在所有 AFSIM可视化应用程序中是共享的。这意味着一旦设置了单位偏好，它将在所有相关应用程序中保持一致。

这种设置的灵活性和共享性有助于在不同的应用场景中保持一致性和便利性。

# 5.2.2.2.1.3.4. 偏好-Mil-Std 2525D 符号 Mil-Std 2525D Symbology

Mil-Std 2525D Symbology Preferences 提供了一种在地图显示中查看平台和轨迹的替代方式。通过勾选“Use Symbology”复选框，可以控制是否用 Mil-Std 符号替换通常显示的模型。这些符号与显示对齐。

Show Velocity Vector 选项是一个附加设置，当使用 Mil-Std 符号时会在地图上显示。这些矢量作为平台的图形放大器，显示其运动方向，并以其标准身份相关的颜色表示（友方=青色，敌方 $\mathbf { \bar { \Pi } } = \mathbf { \bar { \Pi } }$ 红色，中立 $\mathbf { \Psi } _ { \cdot } = \mathbf { \Psi }$ 绿色，未知 $\equiv$ 黄色）。

这种符号化的显示方式有助于在复杂的军事模拟中更直观地理解平台的状态和运动方向。

![](images/c334c4c0cd4f3936efb74dfb51a5d1faff2c783b729b2cbc887156c4e14efa7b.jpg)

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

![](images/cc92d63c1c55913fad1466e1aedf7644601fd472d637edaa31346f86cc7277f6.jpg)

在 non white-cell 场景中，可能更好地通过 Team Visibility 偏好设置隐藏敌对团队，并依赖于轨迹信息。这将防止 Mil-Std 符号被重复显示（一次用于平台，一次用于轨迹）。通过这种方式，可以避免信息的冗余显示，从而保持地图显示的清晰和简洁。

这种设置对于需要精确和简洁信息显示的场景尤其重要，确保用户能够专注于关键的轨迹信息而不被重复的符号干扰。

# 5.2.2.2.1.3.5. 偏好-团队可见性 Preferences - Team Visibility

TeamVisibility Preferences 提供了一种控制平台团队可见性的替代方式。用户可以使用复选框来显示或隐藏团队，并点击“Apply”应用更改。

这种设置允许用户根据需要调整哪些团队在应用程序中可见，从而帮助用户专注于当前任务或场景中最相关的信息。这在处理复杂的模拟或需要简化显示的情况下尤其有用。

![](images/0d23c98327415115dd0efce676d1d5f19c945940dd6aa28eaf73bdcc166af133.jpg)

Team Visibility Preferences 页面控制哪些团队是可见的以及它们的分配颜色。

可见性和颜色：用户可以通过在行编辑中输入团队名称并按下“AddTeam”按钮来添加团队。Visible 复选框控制团队是否对用户可见，而颜色选项控制分配给团队的颜色。可以通过选择团队并按下删除键来移除团队。

默认团队：

us   
united_states   
europe   
1 china   
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

# 5.2.2.2.1.3.6. 偏好-单位 Preferences - Units

![](images/bb37bae77678f12a13d16b6ab05102ecbc16948d9dab0d580c1f07c6f8f9e68e.jpg)

UnitsPreferences 页面控制应用程序中不同类型的值应显示的单位和精度（小数位数）。由于处理方式不同，纬度/经度和时间值还有额外的格式选项。

单位和精度：用户可以选择不同的单位（如米、英尺、公里等）以及设置显示数值的小数位数，以满足特定的需求和标准。

纬度/经度和时间格式：这些值有额外的格式选项，以确保在地图和时间相关的显示中提供准确和一致的信息。

注意：Units 偏好设置在所有 AFSIM 可视化应用程序中是共享的。这意味着一旦设置了单位偏好，它将在所有相关应用程序中保持一致。

这种设置的共享性确保了在不同的应用场景中保持一致性和便利性，特别是在涉及多个应用程序的复杂模拟中。

# 5.2.2.2.1.3.7. 仿真偏好 Simulation Preferences - Warlock

![](images/3c078df86a1d029074bc9f5fb86bc6ad8d8a73ab163bc0aefd6cee1d3db1af72.jpg)

Simulation Preferences 页面包含一组用户选项，用于修改仿真的行为。

Start Simulations Paused：加载和初始化后，仿真将暂停，而不是自动开始。这与no_autostart 选项相关。  
Allow Dragging of Platforms to Set New Position：允许用户在地图上拖动平台到新位置，以向仿真发出命令更改平台位置。  
SimulationClockRate：控制从仿真中读取数据的频率。较高的频率意味着平台更新更频繁，但仿真可能无法支持实时运行。如果场景无法实时运行，考虑降低此频率。  
DISSettings：允许用户覆盖加载的场景文件中设置的 DIS 设置。对该对话框的更改在仿真重新加载之前不会生效。这与 dis_interface 选项相关。  
DeferredStartTime：仿真将在指定时间经过后才连接到网络。在此之前，仿真将以构建模式（尽可能快）运行。这与 deferred_connection_time 选项相关。

# 5.2.2.2.1.3.8. 网络偏好 Network Preferences - Warlock

NetworkPreferences 页面包含用于多播网络的设置，Warlock 插件可以使用这些设置来共享不由 DIS 或 XIO 处理的信息。

Address：这是多播地址。所有连接的仿真都应使用相同的地址。多播是一种通过单次传输将数据报发送给一组感兴趣的接收者的方法，通常用于流媒体和其他网络应用。  
Interface：这是本地端口的地址。此列表通过扫描网络接口设置。点击 $^ \prime { + }$ 按钮可以添加未自动检测到的新接口。  
Port：这是用于发送和接收数据的端口。所有连接的仿真都应使用相同的端口。  
受影响的功能

该页面的设置影响 Warlock 插件如何在多播网络上共享信息。

![](images/59a1de1dc0191ed039fcf3fb545c44cc80fd806ddb0b187c9f8b04e912cbde54.jpg)

# 5.2.2.2.1.3.9. 视频捕捉 Video Capture - Warlock

视频和屏幕捕获功能可以在 Tools 菜单中找到，或者可以随时使用它们的快捷键序列执行（默认情况下，视频捕获是 Ctrl-Shift-V，屏幕截图是 Ctrl-Shift-S）。

![](images/bef62ba0d533c96715acbb16c7f0232b8ba0f2d317c084149108a7af2cf74b1f.jpg)

视频和屏幕捕获功能可以在 Tools菜单中找到，或者可以随时使用它们的快捷键序列执行（默认情况下，视频捕获是 Ctrl-Shift-V，屏幕截图是 Ctrl-Shift-S）。

# 5.2.2.2.1.3.10.绘制 WSF Draw - Warlock

WSF Draw 图层在 Warlock 的 Map Display 中显示，可用于可视化自定义对象。要启用或禁用图层，可以从“View”菜单中的“WsfDraw”浏览器中选择它们。默认情况下，所有对象都会显示。

![](images/049a53855555b3d307c5fc7e61a368cb7d15fccadb4652d330b56f82b2d0e47c.jpg)

使用 WSF Draw

显示/隐藏图层：在 WsfDraw 浏览器中，可以通过勾选或取消勾选单个图层或选择“ShowAll”来显示或隐藏图层。通过勾选顶部的复选框，还可以从其他连接的仿真中接收绘制。  
扩展模式：浏览器可以通过开发者菜单中的“ExtendedDraw Browser”选项进入“扩展模式”。在扩展模式下，可以查看给定图层的内容。  
调试目的：切换绘制图层内容仅用于调试目的。在正常的 WsfDraw 操作中，绘制命令的状态会发生变化。

![](images/590338072a8d0eba2536be89a466b411a8df9e740746f1198275422d6994befd.jpg)

# 5.2.2.2.1.3.11.轨道 Orbits - Warlock

Warlock 中的 Orbits 插件用于显示空间物体和月球的轨道。该可视化可以根据所使用的参考系进行调整，如 ECI（地心惯性）或 ECEF（地心地固），也可以在平面地图上查看。

![](images/a10029daa410f11ec2f7f5c5b1af1af745175d368374955e0f276bab3c4f2027.jpg)

参考系

ECICamera：轨道显示在适当的参考系中，可以通过在 Warlock 的地图显示偏好设置中切换 ECICamera 设置来更改。这允许用户在不同的参考系中查看相同的轨道，例如 ECI、ECEF 或平面地图上。

![](images/1836c80c3fe71d9397c8d38e2e4c542855748f79414133665caf74c8314eb6cd.jpg)

![](images/4a381d5f6787aedfb5c8d1cecd0ad1940717586375ee2266243d8ed6169bd29f.jpg)

![](images/bdd1040122628165b4c6cbbf6601fb098e58df33f4d4699359fb757b12774d17.jpg)

偏好设置

![](images/81d59dec92377d65579c515b1b9dafb1f60714123742a664be00ec06057b910d.jpg)

Fadeout（秒）：确定平台改变轨道时旧轨道淡出的持续时间。  
Color：轨道的颜色可以设置为白色、团队颜色、按名称随机颜色或按场景颜色。“场景”选项使用 WSF_SPACE_MOVER 或 WSF_NORAD_SPACE_MOVER 中的 orbit_color 命令定义轨道颜色。如果未为移动物体定义颜色，则轨道颜色默认为团队颜色。  
LineWidth：设置轨道线的像素宽度。  
Periods：当在平面地图上或不使用 ECI 摄像机查看轨道时，周期值决定将显示轨道的几个周期。

此插件为 Warlock 应用程序内的各种空间实体的轨道提供了全面的可视化和管理方式，增强了仿真和分析能力。

# 5.2.2.2.1.3.12.传感器控制 Sensor Controller - Warlock

![](images/9e2c9ef427e1c77e33228920aa24f26b939ed6d6f4a81e446427b3be233cd721.jpg)

SensorController 插件为用户提供对所选平台上传感器的基本控制。这包括打开/关闭传感器以及指向给定的方位/仰角（AzEl）或轨迹。传感器只有在满足以下条件时才能被指向：

传感器的 slew_mode 和 cue_mode 未设置为“fixed”。  
传感器的平台未被外部控制。  
传感器已开启并处于工作状态。

# AzEl 控制

使用 AzEl 时，角度是相对于平台的水平面（无俯仰或滚动）的。将鼠标悬停在 AzEl 编辑区域上会显示给定传感器的可接受转动限制。  
▪ 方位角限制由 azimuth_slew_limits 和 azimuth_cue_limits 的最小值定义。  
仰角限制由 elevation_slew_limits 和 elevation_cue_limits 定义。

# 5.2.2.2.1.3.13.交互可视化 Interactions - Warlock

在 AFSIM 中，平台之间可以通过多种方式进行交互。为了可视化这些交互，在地图显示上会在平台之间绘制不同颜色的线条。交互类型包括检测、跟踪、干扰请求、通信、任务分配和武器交战。

# 交互类型

干扰请求：由 JAMMING_REQUEST_INITIATED 和 JAMMING_REQUEST_CANCELED 事件触发。这些事件表明一个平台是否正在积极尝试干扰目标，但不表示干扰是否有效。对于未针对目标或基于位置的干扰以及偶然干扰的平台，不会显示线条。

![](images/544107dc09ef0f324efb93f9a611845953d4401cbe9ec5ae2a850a0cafc3e12c.jpg)

平台选项

在平台选项对话框中可以启用或禁用交互。

# 偏好设置

![](images/bf3892e3ae3c291266b8d2fda197fc16ca91a64d02293126d888e76f6e3555c2.jpg)

颜色和线宽：偏好设置提供选项来设置每种交互类型的颜色和线条宽度。  
工具提示：控制鼠标悬停在交互上时显示的信息量。  
超时（秒）：设置星标事件显示的时间长度（以秒为单位）。

允许堆叠：启用后，每对平台之间的每个星标事件都会显示线条。否则，一次只显示一条线。

通过这些设置，用户可以更好地管理和可视化 AFSIM 中平台之间的复杂交互。

# 5.2.2.2.1.3.14.网络战浏览 Cyber Engagement Browser - Warlock

![](images/fd9b621f6016ff783558448cbfb1bc898acd38ab9d08c7ca8c8cb65a81905220.jpg)

CyberEngagementBrowser 提供了一个表格，用于显示当前感知到的网络交战情况。对于每个交战，表格中会显示攻击类型、攻击者、攻击团队、受害者以及交战结果。

功能

删除过期事件：用户可以通过右键单击表格中的事件，然后点击“Delete”来删除或清除过期事件。

# 偏好设置

清除时间：用户可以在 CyberEngagementBrowser 的偏好设置对话框中更改清除时间。默认情况下，表格不会自动清除过期事件。

![](images/d4bd0181adc9fc155c2d32779ab903d9a06bc551951b07149bfac9a3e3d2c426.jpg)

# 5.2.2.2.1.3.15.事件标记 Event Marker - Warlock

Eventmarkers 是显示在地图显示上发生事件位置的图标。当您将鼠标悬停在标记上时，会出现一个工具提示，提供有关该事件的信息。

![](images/f0f3f46d42277b7016414e8713e7858a32186e4dfe9915d66f51e98b0b59e280.jpg)

偏好设置

在偏好设置中，用户可以调整与事件标记相关的以下设置：

![](images/e3b3c2f6cc09aeaabebd7015ed0367673c09ca5730bd2678fd4a0e97cbf31b7e.jpg)

Timeout：设置标记在地图上显示的持续时间。

Scale：调整事件标记相对于场景中显示的模型的大小。  
Visibility：通过勾选相关框来决定事件是否显示在显示屏上。取消勾选框将删除与该事件类型相关的任何现有事件标记。  
▪ Color：允许用户为点标记和 x 标记应用颜色。此设置不影响自定义图标。  
MarkerType：让用户选择标记的类型。如果使用自定义图标，会在图像浏览器旁边显示所选图像的预览。如果选择了无效图像路径的自定义图标，应用程序将默认显示点标记。

# 其他注意事项

Shared Preferences：事件标记偏好在 Warlock 和 Mystic 之间共享，以确保这些应用程序之间的一致性。

# 5.2.2.2.1.3.16.地图悬停信息 Map Hover Information - Warlock

在向导中，地图悬停信息插件负责在使用光标悬停在地图显示中的平台和轨迹上时显示工具提示。这个功能通过在地图上提供额外的信息来增强用户交互，而不会使显示变得杂乱。工具提示是一种常见的方法，用于以用户友好的方式提供额外的细节，因为它们只在需要时出现，例如当悬停在特定区域或项目上时。

这一功能类似于其他工具提示实现，当悬停在某个特征上时，会触发工具提示以显示相关信息。根据上下文和应用程序的具体需求，工具提示可以配置为显示各种类型的数据。

![](images/14b89625d74b489d7f83950b154a2c00b134ae16134b63909e06df81f7da943f.jpg)

# 地图悬停信息首选项

地图悬停信息首选项提供了一个界面，用于自定义地图悬停工具提示显示的数据。用户可以根据自己的需求选择和配置要在工具提示中显示的信息类型。这种自定义功能允许用户在悬停时查看更相关和有用的信息，从而提高用户体验。

通过调整这些首选项，用户可以决定哪些数据字段在悬停时可见，例如平台名称、轨迹细节或其他相关信息。这种灵活性使得工具提示不仅仅是一个简单的显示工具，而是一个可

以根据用户需求进行调整的动态信息窗口。

![](images/b6195bde14f2cb0f2f9a525eafbf3b6d94a9f32a70f7e69483cf00a8bb374743.jpg)

# Map Hover Info Preferences

EnableHoverInfo：此选项允许您完全打开或关闭悬停信息显示。禁用时，悬停在地图元素上将不会出现工具提示。  
ShowNames：启用后，悬停信息显示将包括平台或轨迹的名称，以便立即识别。  
ShowItemLabels：此选项确保工具提示中显示的每个数据字段前都有其标签，使每个值代表的内容清晰明了。  
Platform and Track Hover Info Sections：这些部分控制当光标悬停在平台或轨迹上时显示的具体数据字段。用户可以通过选择标签来自定义显示的数据。  
Modify Displayed Data：要更改工具提示中显示的数据，请选择一个标签并使用 Left/RightArrows 将项目移入和移出“Items To Be Displayed”类别。  
Order of Information：Up/Down Arrows 允许用户控制工具提示中信息的显示顺序，确保最重要的数据优先可见。  
Bullseye Reference：某些数据值是参照 Bullseye 显示的，用“(Bullseye)”文本标示。如果未指定 Bullseye，工具提示将显示“no bullseye”。  
MachDisplay：当为平台启用 Mach 时，它将仅在空中和太空平台上出现，提供相关的速度信息。

这些首选项提供了一种灵活的方式，可以根据用户的具体需求调整地图悬停工具提示，以显示最相关和有用的信息。

# 5.2.2.2.1.3.17.轨迹回放 Platform History - Warlock

在 Warlock 中，平台的位置历史可以通过轨迹线或翼带来显示。

![](images/d189cebecc6789846b5515970f216e310c78d11a52083b4e46d03bba1fce2566.jpg)

![](images/c9ec2aee74f362c78cdf54c1d8becf59b9357f54b5a95f4fa2c208689a7b70f9.jpg)

平台选项

可以通过平台选项来打开或关闭轨迹线和翼带的显示。

# 偏好设置

![](images/038a0768345551236482c40349b16bc91247998df96ad5bef6ebdae5e2f20e24.jpg)

# 轨迹线

LineWidth：设置轨迹线的像素宽度。  
Length：决定从当前位置到轨迹线末端显示的时间长度。  
Coloring：轨迹线可以根据团队颜色、平台名称或状态进行着色。当选择状态时，轨迹线将使用配置的颜色和状态（默认、检测、跟踪、攻击和被击毁）。

# 翼带

Length：决定从当前位置到翼带末端显示的时间长度。  
WidthScale：允许对翼带进行夸张显示。  
ColorScheme：可以选择团队颜色、绿色或灰色。   
Transparency on Death：当平台被击毁时，改变翼带的透明度。

# 5.2.2.2.1.3.18.传感器包络 Sensor Volumes - Warlock

Warlock 中的传感器体积

Sensor volumes 可以在地图显示上显示，以可视化传感器和干扰器的几何信息（视场形状、范围、方向）。

![](images/d382ac8380cf7d3ba3af424137d0bdf880ef0c716241b4a25ba4411e009da31d.jpg)

可视化特性

可视化的体积会被地球的球体遮挡，但不会被较小的特征（如山脉、建筑物或平台）遮挡。这些遮挡作为一种视觉效果实现，以防止光束穿过地球；它们不应被用于预测组件性能。

注意：体积不会绘制超过 600,000 公里的范围。

平台选项

可以通过平台选项启用或禁用体积显示。它们可以在单个传感器/干扰器级别进行控制。偏好设置

![](images/3e9f1e84c2f662c6440d58655183b7ef1405c88973f3aab09fca75f8f5cb8353.jpg)

VolumeType：更改显示的体积类型，包括：  
SlewLimits：绘制由关节部件的转动限制定义的体积。  
CueLimits：绘制由组件的指向限制定义的体积。  
ScanLimits：绘制由组件天线的扫描限制定义的体积。  
Field-of-view：绘制由组件天线的视场定义的体积。  
Beam Width：绘制由扫描限制和波束宽度定义的体积。  
Calculated：绘制一个计算出的体积，显示上述类型的组合体积。

# 控制选项

Faces：启用并为体积的表面着色。

![](images/6e9ddea644d44b7a0ccc1ed5f0a61e31d6a932d3e2967cc011b22ee03deb13a6.jpg)

Edges：启用并为体积的边缘着色。

![](images/41a0ee660f6a2bfec36ef9792ef8a0cf4fe58db104de8dee0979b324215c1a83.jpg)

Proj.：启用并为体积的投影着色。

![](images/ca90fd453e7977ddc206f2db13040ea95035507288e5e158bf5e34ee9325e9ff.jpg)

# 5.2.2.2.1.3.19.六自由度控制 P6DOF Controller - Warlock

P6DOF Controller 已被弃用，推荐使用 Joystick 和 HeadUpView 插件。因此，P6DOF 控制器默认是禁用的，必须通过插件管理器启用。该工具允许用户通过伪六自由度（P6DOF）移动器手动控制 AFSIM 平台，并提供一个带有抬头显示（HUD）覆盖的窗外视图（OTW）。它还包括一些实验性功能，如多功能显示器（MFDs），这些功能可能在未来版本中得到增强或移除。可以通过在上下文菜单中右键单击具有 P6DOF 移动器的平台来访问该工具。

![](images/56184307725ecd5b66cdabbfbf6a24db135e1d6f05f496f5f30f85906cd6d820.jpg)

# 右键菜单选项

ShowHUD：显示抬头显示器。  
FirstPersonView：切换到/从第一人称视角。  
ActivateAutoPilot：激活伪六自由度自动驾驶。  
ActivateManualPilot：激活伪六自由度手动驾驶，允许用户控制。  
ActivateSyntheticPilot：激活伪六自由度合成驾驶。  
ActivateGuidance：激活伪六自由度引导控制。  
Controllers：选择已连接和定义的控制器。  
Full Screen：使窗口全屏显示。

这些操作可以在偏好设置中映射到键绑定。

偏好设置

![](images/eb365c218bb2c1d44b4f14c44b3c0bc0098d98e6bed57508db7715e188d6dbe7.jpg)

ShowHUD：设置新控制器中 HUD 的默认初始状态。  
1stPersonView：设置新控制器中的默认初始视图。  
LaunchHDD：设置启动控制器时是否自动启动下视显示器。  
PilotMode：设置新控制器中的默认初始驾驶模式。  
Resolution：设置控制器窗口的分辨率。

# 控制器映射

P6DOF Controller Warlock 插件的控制器映射在存储于资源/数据中的 XML 文件中定义。

Warlock 提供了以下控制器的映射：

Thrustmaster T-160000M Stick（首选控制器）  
HOTAS Warthog Stick and Throttle   
Logitech X3D Pro Stick   
Playstation 4 Gamepad   
Saitek x45 Stick   
Saitek x52 Stick   
XBox 360/One Gamepad

XML 文件包含一个 devicelist，其中包含一个或多个设备。每个设备为插件定义一个控制方案。虽然一个文件可以包含多个设备，但建议每个文件维护一个设备。

# 设备定义示例

```xml
<device name="My new controller">
    <id_string name="Controller*" />
    ...
</device>
<device name="My other controller">
    <id_string name="Stick*" subdevice="0"/>
    <id_string name="Throttle*" subdevice="1"/>
    ...
</device>
</device> 
```

# 控制机制

axis：设备上的一个轴，返回一个值范围，默认范围为 [-1,1]。  
button：一个按钮，返回二进制值，默认返回 0，按下时返回 1。  
toggle_button：一个切换按钮，循环通过状态，默认在 0 和 1 之间循环。  
hat：一个具有默认范围 [-1,1] 的双轴控制。  
state_key：将键盘输入视为按钮。  
toggle_key：将键盘输入视为切换按钮。

# 识别的值

当前在伪六自由度控制器中识别的值包括：

roll, pitch, rudder, throttle, afterburner, spd_brake_up, spd_brake_down, landing_gear_up,

landing_gear_down, trim_el, trim_az, trim_view_button, pinkie_paddle, view_az_accum,view_el_accum, view_az, view_el_accum

![](images/12070d17d0319745bb4d1e7509c3dea3c9c5baa86fd3d6748c20088023262b2d.jpg)

并非所有值在所有移动器上都能正常工作。此外，可以定义 script_values，当组件总和达到 0.5 或更多时，将在平台上执行命名脚本。

音频支持

该工具目前包括简单警告音的早期访问音频支持，但这是实验性的，目前不支持。

多功能显示器（MFDs）

该工具还包括实验性的 MFDs，尽管功能正常，但目前尚未记录和支持。

# 5.2.2.2.1.3.20.仿真控制 Simulation Controller - Warlock

Simulation Controller 工具栏

SimulationController 工具栏提供了控制模拟时间推进的选项。以下是支持的命令：

![](images/6b5bf14c4b1ddd1e9ec02ea00b60b94c1becf66441adea1d56a58bbde1b4b120.jpg)

Pause/ Resume：暂停或恢复模拟的执行。  
Terminate：终止模拟。  
Restart：重新启动当前模拟。  
ClockSpeed：更改模拟时钟的实时倍增器。  
Advance Time：在非实时模式下快进模拟，直到指定的时间。

# 注意事项

要禁用工具栏，可以直接修改相关配置或设置文件中的 enableToolbar 标志。  
工具栏的每个选项也可以通过可修改的键盘快捷键触发。

# 偏好设置

![](images/770b5a2378ebded1257819e237075771677cba1212b8cbc78029b56ca901c62e.jpg)

StatusBar：控制状态栏中显示的元素。  
Wall Time Specification：控制状态栏中墙上时间的显示方式。  
Networking：控制模拟控件如何与远程模拟交互。

# 5.2.2.2.1.3.21.空战可视化 Air Combat Visualization - Warlock

Warlock 中的空战可视化插件提供了多种可视化空战数据的方法，增强了态势感知和分析能力。以下是其功能的详细介绍：

![](images/55d0962b052b897599ca8b6c92cac047d95a96fc20372e9390fdaa4ba3d5866b.jpg)

# 可视化组件

数据环：这些环帮助可视化空战数据，如防御性、燃料水平和过载（GLoad）。

□ 防御性：测量范围从 -1 到 1，-1 为全红圈， $+ 1$ 为全绿圈。正值顺时针填充，负值逆时针填充。  
燃料水平：测量范围从 0 到 1，正值顺时针以绿色填充。  
□ 过载（GLoad）：黑色条代表 1G（水平飞行），正向范围最高可达 9G，负向最高可达 -3G。值在 0 到 1G 之间时变为黄色。

![](images/fb10317f17cbbe7346e8ddb3e740c7f61ffb4d0660bb0cacd582d19066dc363f.jpg)

数据强调：提供快速的信息概览：

▫ 武器状态：显示“W”并根据弹药水平改变颜色（ $50 \%$ 为绿色， $1 5 0 \%$ 为蓝色，无弹药为红色）。  
▫ 发射状态：当雷达发射时显示 $\prime \langle { \sf R } ^ { \prime \prime }$ ，干扰器发射时显示“J”，通讯时显示 $^ { \prime \prime } \mathsf { C } ^ { \prime \prime }$ ，雷达和干扰器同时发射时显示“X”，无发射时显示“–”。  
燃料状态：显示“F”，并根据燃料水平改变颜色（ $. > 5 0 \%$ 为绿色， $1 5 0 \%$ 为黄色， $10 \%$ 或到达“bingo”状态时为红色，“joker”状态为蓝色）。  
□ 特征：从低到高显示重要性：无适用时为“–”，产生尾迹时为 $" { \mathsf { C } } ^ { \prime \prime }$ ，使用加力燃烧时为“A”，武器舱门打开时为 $" \boldsymbol { \mathsf { W } } ^ { \prime \prime }$ ，最重要的状态会被显示。

![](images/9ca6601663173f267e1af4081eea86fa132f94392fc81e573a2c6f44f57e1552.jpg)

状态数据：提供数值数据，如平台名称、海拔高度、垂直速度、速度、马赫数、过载（GLoad）和迎角。

![](images/f88fcf7733eaadc9b1ed87882a200deb68151f86df9bd4a30763d506f6b091f5.jpg)

交战线：可视化平台之间的交互：

武器交战区（WEZ）线：表示与武器交战区的接近程度，平台在范围内时线条连接。

□ 检测线：显示检测范围，平台在范围内时线条连接。  
□ 线条可能会闪烁以指示目标被跟踪或在最大射程（Rmax）范围内。

![](images/a2ed14c3895bbbd575187e3e69098aab3ad77b6bb9319c715ff2457d6a3a6231.jpg)

空战覆盖层：可以添加到 Tether 视图中，以进行详细数据可视化，包括：

□ 状态数据块：显示运动和燃料状态数据。  
□ 战术数据总结块：显示战术和武器数据。  
□ 交战数据块：显示源平台和目标平台之间的交战数据，并根据平台方标颜色。

![](images/1df77263b57767aa14915aec49a0bfbbdd9595eb97f280121469abbdad1d98b9.jpg)

# 偏好设置

用户可以调整数据环所测量的数据，并切换状态数据和数据强调的显示。

![](images/7ce769719b52a5d842297a0165829cfdd72a132e20d59e6634003f25ab616054.jpg)

# 5.2.2.2.1.3.22.抬头视图 Head Up View - Warlock（弃用）

警告：抬头视图插件已被弃用且不再支持。用户应避免使用它，因为它将在不久的将来从 AFSIM 中移除。建议使用 ACES Display，它提供了许多相同的功能以及其他能力。

抬头视图显示一个窗外视图（OTW），其中包含一个通用的抬头显示（HUD）覆盖。可以通过在上下文菜单中右键单击平台来访问该工具。如果需要，可以同时打开多个抬头视图。

# 注意事项

为显示所有可用数据，平台需要具备态势感知处理器。  
抬头视图插件是一个原型功能，尚未完成。因此，它默认是禁用的，必须通过插件管理器启用。

![](images/77518ea35651173fd2cad1bab3351c47a60c4a01b4fbed88b3cf6933ac73a8b7.jpg)

概述

显示组成：HUD 位于中心，下方是一个简单的前置控制（UFC）显示。  
HUD 顶部：提供水平航向带，当前航向（度）显示在带的中心框中。  
HUD 左侧：显示地速（节）、校准空速（节）、迎角（度）、马赫数、当前过载和可用过载。还包括 HUD 模式（如导航）以及箔条和照明弹的消耗品计数。  
HUD 右侧：显示垂直速度（英尺/分钟）、气压高度（英尺）、雷达高度（英尺），以及航路点信息，包括航路点编号、航向、距离（海里）和时间（小时:分钟:秒）。还包括导航模式和飞行员控制信息。  
HUD 底部：显示滚转指示器。  
中心：显示俯仰/滚转梯和速度矢量。  
UFC：左侧包括一个标准化的推力指示器，绿色区域表示军用功率（干推力），红色区域表示加力燃烧（湿推力）。中心显示质量摘要（以千磅为单位），包括总重、总燃料、内部燃料和外部燃料。

# 偏好设置

用户可以在偏好设置中设置抬头视图的分辨率。

![](images/4ac5f8ca4577980d2e489d94f1e312c78aa331fc4d788fa7a970d526ac49fc32.jpg)

![](images/5132a7e2badd6bec9fe1c82c37c7ac968a092e484ed32d3473ad79d9809fb061.jpg)

![](images/c5dc76ae939e7f17a965dec714bf6c0d6d4c64c62f191908f45164efaded39c0.jpg)

![](images/893aa84bd23b8af2a3802152ba0dec635ded5370234d2163dcf50390b1ffa3be.jpg)

# 5.2.2.2.1.3.23.低头视图 Head Down View - Warlock（弃用）

警告：HeadDownView 插件已被弃用，并且不再受到支持。用户应避免使用它，因为它将在不久的将来从 AFSIM 中移除。建议使用 ACESDisplay，它提供了许多相同的功能以及其他能力。

HeadDownView 为所选平台显示类似玻璃座舱的下视显示。该工具可以通过右键单击平台时的上下文菜单获得。可以同时打开多个 HeadDownView。

注意：要显示所有可用数据，必须使用具有 Situation Awareness Processor 的平台。

注意：HeadDownView 是一个原型功能，尚未完成。因此，它默认是禁用的，必须通过 Plugin Manager 启用。

![](images/ab61dbb1ff99cfd062a2d88dfa3c35d269c9f846b0fcb465ee4796cd12ec195d.jpg)

显示界面被分为 12 个默认页面。用户可以通过点击底部的箭头来扩展或收缩这些页面。每个页面都有特定的编号，用户可以在 Preferences 中选择默认页面。

# 主要功能

页面导航：使用底部的箭头可以轻松导航页面，实现页面的扩展或收缩。  
自定义：用户可以在 Preferences 中自定义默认页面，以便根据需要调整显示。

![](images/c0e80d9e58bde32350f5dd463ddade6b1c616a24327aa57b455dddd69d31e64a.jpg)

# AFSIM 页面管理

页面可以通过打开主页面（1-4）左上角的菜单按钮进行更改。
![](images/b21896fcdb52d4544e49b80853fea9b3ce85a96c2ee3e1e05104b5d21a55de17.jpg)
![](images/b21896fcdb52d4544e49b80853fea9b3ce85a96c2ee3e1e05104b5d21a55de17.jpg)

