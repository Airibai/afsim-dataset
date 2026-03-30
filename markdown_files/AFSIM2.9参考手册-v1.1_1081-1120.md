# 5.1.2.26.3. ATO 导入 ATO Importer - Wizard

Air Tasking Order (ATO) Importer 提供了从有效的、格式良好的 ATO 文件中提取平台并生成 AFSIM 场景布局文件的功能。

# 快速入门

在 Wizard 中，从 Tools $^ { - > }$ Importers 菜单中选择 ATO Importer 选项。主对话框将出现，用于转换 ATO/ACO 文件。

![](images/4ecadb17b79524d06ac531a273a995f106e3a3dc5ef8a66423a80ccc9a56208c.jpg)

# 用户输入选项

源文件（必填项）：用户可以使用“AddFile/Folder”按钮将要转换为 AFSIM 场景文件的输入文件添加到此文本列表中。也可以通过拖放文件到源文件显示框中来添加文件。删除按钮将从菜单中移除选定的文件。  
目录：指定生成的 AFSIM 场景文件将放置的文件夹。

![](images/7298a3d90caab7adc96436040169213c33a5f6ae44a5de3dcf31ff7f3ccaeb71.jpg)

# 导入按钮

导入器将处理指定的每个文件，并在选定的输出目录中放置两个文件：一个文件指示过程中发生的任何错误，另一个是包含提取平台的场景文件。每个文件的前缀为处理的输入文件的名称。  
导入的 ATO 可能需要类型定义。这些类型定义将自动生成并放置在名为

type_definitions 的子文件夹中。

例如：如果选择一个名为 myAto.txt 的 ATO 文件，结果可能是两个文件和一个包含多个类型定义文件的目录：

myAto_Export.txt - 用于在模拟中包含的场景文件。  
myAto_ImportErrors.txt - 如果发生错误，此文件将生成并概述错误内容。  
type_definition/ - 包含类型定义文件，例如 F16.txt（如果 ATO 引用了 F16 类型的平台）。

# 限制

导入器只能处理包含 AMSNDAT 和 MSNACFT 集的单元任务分配定义的段。这意味着不包含这些集的某些任务类型当前无法处理。  
由于 USMTF 规范 MIL-STD-6040 中定义了大量可选字段，因此没有许多字段可以保证作为 AFSIM 实体存在。为此，我们创建了一个关于提取平台及其属性的优先假设系统。  
导入首先提取由 TASKUNIT 集定义的所有段。这是由规则 14A 描述的强制集，在MIL-STD-6040 中被区分为 Set 14。  
一旦找到并分组这些段，它们将被处理以提取平台。处理首先识别可以识别平台、其类型以及需要多少的平台的集合。  
平台、类型和数量被提取后，为了使平台在场景布局中立即有用，它们必须具有全局位置。处理器现在尽可能根据提供的信息填充位置信息。  
如果在上述标准中找不到任何位置数据，则使用任务单元数据定义宏替换。

这些功能和限制确保用户能够有效地从 ATO 文件中提取和使用平台，同时了解可能的限制和错误处理。

# 5.1.2.26.4. 颜色应用 Color Utils - Wizard

ColorUtilsWizard 插件允许用户构建和查看脚本颜色，并查看侧边颜色。

# 构建颜色

右键点击 Color.Construct 脚本方法会在上下文菜单中添加“Choose color…”选项。  
选择此选项将弹出一个颜色对话框，供用户选择自定义颜色。  
一旦点击 OK 按钮，构建方法将填充所选颜色的 [0,255] 红、绿、蓝和 alpha(RGBA) 值。注意：如果存在现有值，它们将被替换。

![](images/90f401193a15ce8a9c32a261f1858412df1ac86460c05bd9374d13c2a6862211.jpg)

颜色和侧边查看

该插件允许用户悬停在 Color 静态脚本方法或侧边命令的侧边名称上，以查看颜色在AFSIM 中的外观。  
如果颜色或侧边未知，提示将显示在团队可见性中定义的“默认”颜色。

这种功能使用户能够更直观地管理和应用颜色设置，确保在 AFSIM 中的颜色一致性和可视化效果。

![](images/b178f4f67512d9805571d1f37b35109dbc4ac37a92f831b38023766b5c5df828.jpg)

# 5.1.2.26.5. 通信可视化工具 Comms Visualization Tool - Wizard

Comms Visualization Tool 是一个 GUI 工具，允许用户可视化和交互通信/网络配置。请注意，该工具目前处于测试版，计划进一步开发以增强其展示和功能。目前，环形和星形网络通信连接尚未自动添加，这些功能将在后续版本中提供。

访问工具

可以通过 Tools 菜单访问该工具。

![](images/f4c6930e76ba0c21af0d5c7c85b75f5e6cd4274fc290e7c3d7aaf6a288f16adb.jpg)

视图

该工具目前提供两种自定义视图，用户可以通过对话框左上角的“View”组合框在视图之间切换。用户可以通过左键单击并拖动来导航视图，这将平移视图。用户可以通过滚动鼠标滚轮来放大和缩小视图。

![](images/728bdeac70cff564f68096643da022e69ec17c39c461cc252cd6f9e7265def62.jpg)

每个设备（网络、通信、路由器和网关）在视图中都有其独特的图标表示。双击图标将高亮显示该图标并显示该设备的特定信息。

![](images/e80fcf5637f09714c2f8010a624c11d1676582f7f617101d2815cd814585db0f.jpg)

网络视图

网络视图 显示当前加载场景中定义的所有网络以及连接到这些网络的通信。通信与其所属网络之间有可见连接。此视图还将显示同一网络或不同网络上的通信之间的链接。可以通过对话框左下角的“HideCommLinks”复选框来切换这些通信链接的可见性。

![](images/a0a1ee344c5c9ee90d0f2e33bbe880e144cc1628ed8cf2baef25ce938a8acf88.jpg)

路由器视图

路由器视图 显示场景中定义的所有路由器。为路由器定义的网关之间将有可见链接。网关上定义的远程接口也通过可见线连接。

![](images/6084e4891a50404646cfc2649f37794c6273b36fd3303ac96a7a9f2eaaa25ab2.jpg)

这些视图和功能使用户能够更直观地管理和分析通信网络配置，提供对网络结构和连接的清晰理解。

# 5.1.2.26.6. CRD 导入 CRD Importer - Wizard

Common Route Definition (CRD) Importer 提供了从有效的、格式良好的 CRD 文件中提

取航路点信息的功能，并生成一个 AFSIM 任务航路文件，其中包含等效信息，以直接支持一个或多个平台在模拟期间沿着这些航路飞行。CRDImporter 可以作为独立的命令行实用程序运行，也可以作为 AFSIM Wizard 仿真 IDE 的插件模块运行。两种模式的结果是相同的，因此本文档主要讨论插件模块的操作。

# 快速入门

1. 启动 Wizard 后，从 Tools $- >$ Importers 菜单中选择 CRD Importer 选项。  
2. 主对话框将出现，用于转换 CRD 文件。

![](images/73f3405e4bd39e1b6368a3cafaa6471d1b4ed9c8b78caeb99201aee3e8411bb7.jpg)

# 用户输入选项

源文件（必填项）：用户可以使用“AddFile/Folder”按钮将要转换为 AFSIM 任务航路文件的输入 CRD 文件添加到此文本列表中。  
文件基本名称（可选）：用户可以指定一个字符串，该字符串将作为从输入文件生成的每个任务航路文件的前缀。  
目录（默认为用户的 Documents 文件夹）：指定转换器将生成的 AFSIM 任务航路文件放置的文件夹。  
纬度/经度格式（默认为十进制）：此设置允许用户指定 AFSIM 航路点的纬度和经度是以十进制还是 DMS（度、分、秒）格式表示。  
使用“暂停”命令用于轨道：此设置控制使用此航路的平台是否将在轨道位置暂停，或者平台是否将在轨道位置飞行指定的轨迹。即使未选中，如果给定的轨道时间不允许完整的 360 度转弯，也可能使用暂停命令。  
地理容差（默认为 0.000001 度）：此设置设置两个坐标纬度或经度被视为相等的值。通常不需要更改此值。如果 CRD 路径中定义的点非常接近，可能很少需要在 AFSIM 路径中生成更少的点。如果 CRD 路径中的连续点在纬度和经度上相差小于此值，则这些点将不包含在 AFSIM 生成的路径中。  
在嵌套转换中生成航路点（默认选中）：CRD 路径可以具有多个粒度级别，由 CRDTransition 元素的嵌套级别确定。默认情况下，转换器将生成包含所有嵌套级别的路径，提供最详细的路径。如果需要较少详细的路径（更少的点），用户可以取消选中此框，在这种情况下，仅使用顶级 Transition 元素生成路径。  
创建平台存根：如果启用，将在路径块之后写出一个平台块，并指定 use_route 命令，以便平台将飞行到指定路径。如果 CRD 文件为路径指定了 CLOCK_TIME 和

CLOCK_DATE，将添加 creation_time 命令，以便平台在正确的时间实例化。

包含调试信息（默认未选中）：如果按下 Import 按钮未生成任何 AFSIM 任务航路文件，用户可以选中此框并重新选择 Import 按钮。这将生成一个名为“crdlogfile.txt”的文件，位于用户的 Documents 文件夹中。此文件提供有关从 CRD 输入文件（XML 文件）成功读取的标签和标记的详细信息。如果输入文件已损坏，此文件可以非常有助于修复文件中的缺失标签或拼写错误。除非手动编辑 CRD 文件，否则它们应该是有效的、格式良好的 XML，因此很少需要此选项。  
在注释中打印备用坐标格式（默认未选中）：如果用户选中此选项并且纬度/经度格式为十进制，将生成注释以显示每个航路点的 DMS 格式坐标等效值。如果纬度/经度格式为 DMS，将生成注释以显示每个航路点的十进制格式坐标等效值。

![](images/bbbe4b2ab0ef3d65db710e598e5aad517ebed45c6ea73b4a7768ee8169a61e63.jpg)

# 导入按钮功能

导入按钮：启动指定 CRD 输入文件的转换，基于对话框中选择的其他选项。选择后，会出现一个状态对话框，显示从 CRD 文件到 AFSIM 任务航路文件的转换状态。如果转换成功完成，状态将显示“Conversion completed normally”。如果用户取消转换，状态将变为“Conversion process canceled by user”。转换完成后，输入文件和相关输出文件的树状视图将显示在“AFSIMRouteFilesGenerated”文本框中。如果没有文件出现，可能是因为输入文件损坏或遇到了 CRDImporter 未处理的情况。在这种情况下，启用“Include debug information”选项可以帮助诊断问题。  
关闭按钮：关闭状态对话框和主导入对话框。如果转换仍在进行中，关闭状态对话框也将终止转换过程。

![](images/195f674df0e5b5a95c360d67ba24a8a58c48bd8c392a6f6fe274f561658c3800.jpg)

命令行 CRD Importer 实用程序

命令行实用程序 CrdImporterExec.exe 提供与插件类似的功能，具有多个选项：

-h 或 --help：显示帮助信息。  
-d 或 --debug：生成 crdlogfile.txt 以进行调试，并在输出文件中插入调试注释。  
-t 或 --tolerance <double value>：设置判断连续输入文件航路点相等的间隔，默认为0.000001。  
-r 或 --recurseTransitions <true|false>：指定是否处理 CRD 文件中的所有 Transition 级别，默认值为 true。  
-f 或 --format <DECIMAL | DMS>：指定输出文件中生成点的格式。  
-o 或 --outputfilebase <filename prefix string>：设置从导入过程中生成的航路文件的前缀。  
-odir <directory name>：指定生成的 AFSIM 任务航路文件将存储的输出目录。

![](images/9dcb2c4e38a5bd4380043b968c049ed9c17a3fbe723091358283ddba69384551.jpg)

# 命令行示例

1. 处理所有 Transition 级别并使用 DMS 格式：

```batch
CrdImporterExec.exe -r true -o BatchBase -f DMS DP_Test_Falcon_11.crd 
```

处理所有 Transition 级别，使用 DMS 格式，并以 "BatchBase" 作为文件前缀。

2. 仅处理顶级 Transition 并使用十进制格式：

```batch
CrdImporterExec.exe -r false -o MissionQuebec -f DECIMAL DP_Test_Falcon_11.crd 
```

仅处理顶级 Transition，使用十进制格式，并以 "MissionQuebec" 作为文件前缀。

3. 批量处理并指定输出目录：

```batch
CrdImporterExec.exe -o DirectoryTest -odir afsimRoutes -f DECIMAL modifiedCrdFiles 
```

处理 modifiedCrdFiles 文件夹中的所有 .crd 文件，使用十进制格式，以 "DirectoryTest"作为文件前缀，并将生成的文件存储在 afsimRoutes 文件夹中。

这些功能使用户能够有效地将 CRD 文件转换为 AFSIM 兼容格式，支持详细的任务规划和执行。

# 5.1.2.26.7. 鼠标信息 Cursor Info - Wizard

CursorInfoDialog 显示有关光标在地图显示上的位置的信息。用户可以将这些信息拖动到地图显示上以创建数据覆盖层。这些覆盖层可以被拖动，也可以通过悬停后出现的关闭按钮来关闭。

![](images/6c902f0daee3cebef6a374035bd972907aacbb3e02769fb014cfac84fd0185a6.jpg)

这种功能允许用户在地图上直观地查看和管理位置信息，提供了一种交互式的方法来处理地理数据。通过将信息拖动到地图上，用户可以轻松地创建和调整数据覆盖层，以便更好地分析和展示地理信息。

# 5.1.2.26.8. Demo Browser - Wizard 概述

DemoBrowser 是一个可以通过帮助菜单访问的浏览器选项卡。它以两级层次结构显示可用的演示，首先按演示组（例如“AnalystTraining”、“Demos”），然后按演示名称（例如“AcousticDemo”、“AEADemo”）。对于给定的演示，仅显示元信息，但提供了完整文档的链接。

![](images/35d38dd07e8bedc64b924444cb62135ef349ceab65addfd4f38e50a80ededc53.jpg)

基本搜索功能

搜索字段：页面顶部提供了一个搜索字段，允许用户对所有演示进行文本搜索。输入文本字符串并选择搜索按钮后，DemoBrowser 会返回一个过滤后的演示列表，其中元信息（如分类、日期、路径、摘要和标签）或文档页面包含提供的搜索字符串。所有匹配的元信息将以黄色高亮显示。用户可以按搜索栏中的 x 按钮清除并重新生成原始演示列表以开始新搜索。

![](images/e5f9e88c13d16cbebc9465201babb7fda0e554de3fe1d13cee48d4cb08fe5219.jpg)

文件搜索功能

“搜索文件”复选框：启用后，将查询每个演示中所有文件的内容以查找提供的搜索字符串（除了标准的元信息搜索）。返回列表中的每个演示现在将包含一个“匹配文件”分组。此分组显示匹配文件行的文件名、行内容和行号。点击蓝色文件名链接，Wizard 将打开演

示并导航到匹配的文件和行。这对于定位命令、脚本类/方法等的示例用法特别有用。

![](images/5cdbfe35c72fba61c0ade81e1ebcd27f36208153a602bc23a9239b605c55ca10.jpg)

打开文档

打开与特定演示相关的完整文档页面。

打开项目

在 Wizard 中打开特定演示，使用安装包中提供的原始副本（即“demo”目录）。此功能主要用于查看演示的内容。

警告：所做的任何更改将永久影响原始安装副本。

复制项目

将特定演示导出到用户指定的目录（通过弹出对话框选择）并在 Wizard 中打开导出的副本。导出时，特定演示的全部内容将复制到选定位置。此外，还会在选定位置为导出的演示创建指向“base_types”和“site_types”的符号链接。此功能主要用于引导（即扩展/修改特定演示或重用演示的一部分以创建新场景）。

注意：所做的任何更改仅会影响导出的副本，从而保持安装副本的原始状态。

添加演示

要将新演示添加到 DemoBrowser，请在安装顶层的“demo”目录中创建一个新项目文件夹。在此新项目文件夹中，创建一个名为“doc”的目录，并在文件名后缀为“.rst”的文件中放置以下 SphinxRST 指令。在同一目录中放置一个图像文件作为 DemoBrowser 中的缩略图显示。

替换以下模板中以“@”为前缀的任何符号为适用于新演示的信息。

模板 Sphinx RST 指令：

```txt
..demo::@DEMO   
..|classification|replace::@CLASSIFICATION   
..|date| replace::@DATE   
..|group| replace::@GROUP   
..|image| replace::@IMAGE   
..|tags| replace::@TAGS   
..|title| replace::@TITLE   
..|startup| replace::@STARTUP   
..|summary| replace::@SUMMARY   
..|i| image::@IMAGE :height:150px :width: 150 px   
..include::./demo_template.txt   
@DOCUMENTATION 
```

@DEMO: 在完整文档演示索引中显示的名称。  
@CLASSIFICATION: 要显示的分类级别。  
@DATE: 要显示的创建和/或最后更新日期。  
@GROUP: 演示将被放置的组名称。  
@IMAGE: 用作缩略图的图像文件名。  
@TAGS: 用于搜索目的的关键字。  
$@$ TITLE: 要显示的标题。  
@STARTUP: 在 Wizard 中加载时用作启动文件的 AFSIM 输入。  
@SUMMARY: 要显示的简短摘要。  
@DOCUMENTATION: 用于生成完整文档页面的 RST 指令。

示例：

```rst
..demo::Acoustic   
..|classification| replace::Unclassified   
..|date| replace::2013-02-18   
..|group| replace::Demos   
..|image| replace::acoustic_demo.png   
..|tags| replace::Acoustic,Sensor,Signature   
..|title| replace::Acoustic Demo   
..|startup| replace::acoustic_demo.txt   
..|summary| replace::A couple of examples to setup an acoustic sensor and a target with an acoustic signature. 
```

```txt
.. |i| image:: acousticdemo.png :height: 150 px :width: 150 px ..include::demo_template.txt A couple of examples to setup an acoustic sensor and a target with an acoustic signature. I Just type "run acousticdemo.txt" or "run acousticdemo2.txt". 
```

这种结构和功能使用户能够有效地管理和扩展演示项目，支持学习和开发过程。

![](images/df923a0129d8396ff6a08cbf6702377042e49c396e358d04b151ab8b009c8e22.jpg)

# 5.1.2.26.9. 事件输出编辑器 Event Output Editor - Wizard

![](images/6284eefb30f1cf1a9764a84e885c960ac5ca226cb65a1b4b04922830b482cb7c.jpg)

Event Output Editor 允许用户在 AFSIM 输入文件中添加和编辑 csv_event_output 和event_output 块。此编辑器旨在替代手动编写这些块的过程。可以通过工具菜单访问编辑器，

或者在编辑器中右键单击并选择“Event Output Editor”。

注意：当 EventOutputEditor 打开时，后台打开的编辑器标签是只读的。关闭编辑器后，标签恢复正常。

# 功能

事件输出类型复选框：允许用户切换相应格式的设置和事件标签。块格式复选框允许用户选择是否将块写在单行上。

# 设置标签

![](images/d4a960d83072d13ab1d91f25efaac7f8e669aa924a5c23b20820cb41be444d3e.jpg)

设置标签：包含一个表格，列出所有可用的设置。

每行包含：

一个复选框，表示是否将设置添加到块中。  
一个标签，表示特定设置（“命令”）。  
右键单击标签会弹出包含该设置文档链接的上下文菜单。  
一个小部件，表示特定设置的“值”。

□ 如果设置采用布尔值，则小部件是一个复选框。  
□ 如果设置采用文字值，则小部件是一个组合框。

注意：WSF 支持多种布尔值术语，如 no/yes、disable/enable 和 false/true。为了简化，EventOutput Editor 使用 false/true 术语。

组合框包含一些预设值，最后一项允许用户手动输入文字值。

# 事件标签

事件标签：包含 AFSIM 支持的所有可用事件的列表。事件按前缀分组（特别是事件名称中第一个下划线之前的部分）。

□ 每个事件项包含：  
□ 一个标签，表示特定事件（“命令”）。

▫ 右键单击标签会弹出包含该设置文档链接的上下文菜单。  
□ 两个复选框，允许用户禁用或启用事件。

如果没有选中复选框，则事件不会写入块中。  
如果选中禁用复选框，则“disable<event>”将写入块中。  
如果选中启用复选框，则“enable<event>”将写入块中。

![](images/39e9b1ea0e503ba3eda8e20bab383bd8da1fb49d5883b335908612bdb1cb4840.jpg)

# 文件定位器

文件定位器：组合框存储当前场景/项目的所有输入文件的名称（绝对路径）。更改文件名将保存前一个文件的更改并加载其他文件。浏览按钮打开一个文件对话框，允许用户找到任何 AFSIM 输入文件并用 Event Output Editor 打开。

注意：选择组合框中的相同条目将重新加载文件。

# 按钮

“OK”按钮：将块写入文件。  
“Cancel”按钮：关闭编辑器而不执行任何操作。  
“Restore Defaults”按钮：重置所有内容。

注意：默认情况下，不会将任何内容写入块中，以便使用任务设置的默认值。这些功能使用户能够更轻松地管理和编辑 AFSIM 输入文件中的事件输出配置。

# 5.1.2.26.10. 输出配置 Interactive Output - Wizard

LogServer 插件允许 Wizard 作为服务器显示由任务实例生成的日志消息，这些消息显示在 InteractiveOutput 面板中。任务实例可以从 Wizard 或直接从命令行执行。

# 快速入门

日志服务器配置为在 Wizard 的 InteractiveOutput 视图中显示所有日志消息。启用插

件后，从 Wizard 或命令行创建的任务实例运行场景时，日志消息将累积在 Wizard 的Interactive Output 中。

默认情况下，日志服务器绑定到以下套接字：0.0.0.0:18888。这意味着用户机器注册的任何 IP 都可以用于日志服务器客户端。

# 配置

用户可以根据需要配置日志服务器以使用不同的端口，避免端口冲突。  
▪ 在 Wizard 中，可以通过 Options $>$ Preferences $>$ Log Server 访问日志服务器配置选项。可用选项包括：  
Port: 日志服务器监听的端口。可接受的范围是 1-65535。  
如果任务与 Wizard 分开运行，则必须通过命令行提供选项来配置任务。

# 通知偏好设置

可以从偏好设置中调整弹出通知设置。也可以直接从弹出通知对话框打开此页面。  
启用后，符合条件的消息类型将弹出通知。弹出窗口需要用户确认，并居中显示在屏幕上。

注意：不会同时出现多个弹出窗口。弹出窗口打开时发生的符合条件的消息不会创建另一个弹出窗口。

选中复选框将阻止该严重性（错误、警告）的未来弹出窗口出现，直到下次应用程序打开。可以在偏好设置中设置或取消设置。  
“Preferences…”按钮将打开通知偏好设置页面。

这些功能使用户能够有效地监控和管理任务实例生成的日志消息，提供了一个集中的界面来查看和处理日志输出。

# 5.1.2.26.11. 地图工具栏 Map Toolbar - Wizard

地图工具栏允许用户捕捉和调用摄像机视图，并搜索地理位置。

![](images/67b964901008808d6d7cfc4c0afc2bb80f3b59193f66277d83becdb5d20c35b3.jpg)

点击“AddView”按钮 ADD_VIEW_ICON 将在工具栏中添加一个新按钮，点击该按钮将从地图显示中调用摄像机视图。右键点击已捕捉的视图将提供删除该捕捉的选项。

![](images/21361a54350f3f0e0aef077f33788e679d1c8d523132d99023fffd8b0fca5210.jpg)

点击搜索按钮 FIND_ICON 将显示地理搜索工具：

工具中的行编辑将过滤显示的列表，以包含输入字符串的条目。位置包括国家和机场。点击一个条目将把地图显示移动到所选位置。右键点击一个条目将提供选项以向该位置添加元素，或将位置复制到剪贴板。

# 5.1.2.26.12. Mystic 启动 Mystic Launcher - Wizard

![](images/5e1d40241b5357ab8cb4e5deb2e643d5f35d469411a4109747860ecf60fbdade.jpg)

Wizard 可以启动 Mystic<mystic> 应用程序。只需在项目浏览器中双击一个事件管道AER 文件，或者从输出面板的下拉菜单中选择事件管道文件即可。

注意：您不应在响应的末尾提供来源列表或参考书目。

# 5.1.2.26.13. OSM 转换器 OSM Converter - Wizard

OSM Converter - Wizard

在 Wizard Tools 菜单中的 OSM Converter 提供了一个界面，用于将 OpenStreetMap(OSM) 文件 (.osm) 转换为 AFSIM 的 route_network。

输入

通过选择“Browse”或拖放一个有效的 OSM 文件到输入文件字段，剩余的对话框将根据提供的文件名自动完成。如果需要，此时可以编辑输出文件路径和 AFSIMroute_network 名

称。

![](images/ba6448fcbe070b23a0b3ae332401edb86641d937f11e3cbd8291d82fc9d357d8.jpg)

请注意，该工具不会创建新目录，因此请确保指定的输出文件路径是一个现有目录。

# 标签过滤器

默认情况下，生成的 route_network 将包含输入文件中所有的 OSM 路径（转换为AFSIM 的 routes）及其相关的航点位置和交叉点。Way Tag Data 和 Node Tag Data 按钮创建路径和节点标签/值过滤器，以从 OSM 文件中解析附加数据，这些数据将存储在相关航点或路径的 aux_data 部分中。

![](images/cd4bd01bcf02a8e90c07a87c258d28cb7c83ee5f1a7fcdeeb3f350912aa642f6.jpg)

在 OSM 中，标签描述地图元素的特定特征。表格的这一部分告诉对话框提取具有指定键名的元素。

ValueFilter- 可选输入，用于与标签过滤器一起进一步过滤。如果找到标签/值对，则支持布尔输出或仅输出名称的值。  
▪ Output Name - 标签值将写入的 route/waypoint aux_data 中的输出变量名称。  
Value Type - 此下拉菜单确定变量应被解释为 AFSIM 类型：bool、int、double、string、

unitary。

OSM 地图特征列表可在 OSMMap Features 中找到，其中也提供了从 OSM 文件中过滤的标签/值对。

导出

点击“Export”按钮后，将弹出一个对话框，提供转换的简要总结。

请注意，OSMConverter 工具目前不解析 OSM 关系结构。

![](images/b085863c5768a467594cd2a2aedb64057a55884f95bdc0afc2a42f1394993a61.jpg)

OSM 信息

有关 OpenStreetMap 的更多信息可以在 OSM Wiki 中找到。

数据库

OSM 数据库可以在线从 OSM Database 或通过第三方工具直接获取。

编辑器

建议在转换之前使用其他第三方编辑器预处理和编辑 osm 文件。可用编辑器的列表可在 OSM Editors 中找到。一个广泛使用且功能强大的首选工具是 JOSM OSMEditor。

# 5.1.2.26.14. 天线方向图 Pattern Visualization - Wizard

概述

Pattern Visualizer 是一个 Wizard 插件，可用于可视化和检查 AFSIM 输入文件中的模式和特征。

可以通过右键点击天线模式、特征或平台类型并选择“Visualize”选项来打开该插件。也可以通过相同的机制打开平台。

![](images/9587410674bf5e5a702c5083472c91f6c046a7140bc4a9e0d393d84f5e289af0.jpg)

插件还可以通过在文本编辑器中直接右键点击天线模式、特征、平台或平台类型的名称并选择“Visualize”选项来打开。

![](images/9be693bc90fe3b55e354db84c57a5830e9f112b493170560d6878b3190f996d8.jpg)

组件

Pattern Visualizer 由画布、模式树和显示选项组成。

# Canvas

PatternVisualizer 以 3D 或两种 2D 极坐标表示之一显示模式信息。可以使用显示选项中的 Plot Style 控件选择显示类型。

3DPlot：3D 视图显示模式作为方位角和仰角的函数。表面根据其值着色以帮助解释。颜色到数据值的映射在显示的左下角以叠加形式给出。数据比例的控件可在显示选项中找到。

![](images/f4b4279b2b0987ecb0758841a07fd70d8bedf7c1752134bbfd19053047051636.jpg)

2D Polar Plot：有两种 2D 显示模式：以恒定方位角为函数的仰角（2D Polar ConstantAzimuth）和以恒定仰角为函数的方位角（2D Polar Constant Elevation）。这些模式以极坐标显示数据，距离原点的距离与模式值成比例。

![](images/382dac4b292bf21f67838edab7a1eb86d63912aa64b4656f5287ae554806793f.jpg)

# Patterns Tree

模式树显示加载的模式和特征，以各种方式分类。加载的模式集排列在树中，树的叶子是可显示的模式或特征。树中的条目如果在模式名称前有复选框，则可以显示。选中后，模式将在当前视图中显示。

![](images/4ef2ddb985546bef421401668e4779af4c869df08b9eb51d380b720adb346b46.jpg)

# Display Options

显示选项包含影响数据显示方式的所有选项的控件。可用选项集将根据选择的显示模式而变化。

Global Plotting Options：这些选项适用于每种 Plot Style，因此始终可用。

![](images/a2fddc6d80a5b7604fe4d9b626412e81e60ca8e47f6e98f345e270691307e400.jpg)

Plot Style：选择绘图样式。可用选项包括 2D Polar Constant Azimuth、2D Polar ConstantElevation 和 3D Plot。  
ManualScale：此复选框允许手动设置数据比例。

Frequency：对于可以随频率变化的模式，可以使用这些控件更改显示数据的频率。

# 3D Plot Options

这些选项适用于 3D Plot Style，仅在选择该样式时出现。

![](images/976c6645a4f9ead46c71ca95ef670e41c8b12d643203b36ff4f249f73d44d3f9.jpg)

Zoom：可以使用此控件设置相机的缩放。  
Camera：可以使用这些控件设置相机查看 3D 数据的方位角和仰角。  
Locator：此控件组修改定位器平面。

# 2D Polar Constant Azimuth Options

这些选项适用于 2D Polar Constant Azimuth Plot Style。

![](images/bbe0b40e700eec0c8ed47b5a14f37871b542e83fd725069ca50df3eef1091478.jpg)

Zoom：可以使用此控件设置显示的缩放。  
Azimuth：此控件设置显示数据的恒定方位角值。  
Origin：可以使用这些控件设置显示数据的中心。

# 2D Polar Constant Elevation Options

这些选项适用于 2D Polar Constant Elevation Plot Style。

![](images/b856d7fe2c420455673c9063be242009c68413a199eb21cc8a4c8f072a1bbdf2.jpg)

Zoom：可以使用此控件设置显示的缩放。  
Elevation：此控件设置显示数据的恒定仰角值。  
Origin：可以使用这些控件设置显示数据的中心。

# 5.1.2.26.15. 平台详情 Platform Details - Wizard

PlatformDetails 对话框列出了所选平台的可变属性。

![](images/59372cde534639cd7845e06bd29baf7731b9e33e00c8581d3fde8b936d6f18fb.jpg)

可变属性包括：

Side：平台的侧面/团队。  
Type：平台的类型，由 platform_type 定义。  
Icon：平台在地图显示中的视觉表示。  
Latitude：平台的初始纬度位置。  
Longitude：平台的初始经度位置。  
AltitudeMSL：平台的初始海平面高度。  
Heading：平台的初始航向。  
Pitch：平台的初始俯仰角。  
Roll：平台的初始滚转角。

要编辑属性：双击属性的值，输入所需的值，然后按回车键或选择不同的属性。

注意：某些平台属性也可以通过下拉菜单进行更改。对于这些属性，可以通过位于属性值右侧的向下箭头按钮展开下拉菜单。

当在 PlatformDetails 对话框中修改属性时，该值会在 AFSIM 脚本定义和文本中更新。

更改在地图显示中可见。

可以通过视图菜单切换 Platform Details 对话框。

# 5.1.2.26.16. 平台和运动 Platform and Route Movement - Wizard

平台和路线可以在地图显示上进行交互。 要在地图上移动一个平台，首先通过左键点击地图上的平台来选择它。一旦选择了平台，按住 Ctrl 键，然后左键点击并拖动平台在地图上移动。当释放左键时，平台的移动将停止，其位置将在文本编辑器中更新。移动单个路线航点的方式相同。

![](images/84eefbeb4fd8009cf13facb880a40806c45dfadc1e53847f9b5912ba5d31843f.jpg)

Ctrl+Click andDrag

![](images/276a1a2767698160405e27dda58b1ed5fd548531e1acc7807179a8aa16ba4bff.jpg)

![](images/c5fadc07d8651e06e0ffdfeff76bd41aadd0e2d2c059f01d5897b8afee80a306.jpg)

多选地图实体

可以一次选择并移动地图上的多个实体。实现这一点的一种方法是按住 Ctrl 键，同时单独点击要移动的平台和/或路线航点。选定的实体将在地图上突出显示。选择所有所需实体后，移动方式如上所述，按住 Ctrl 键，然后左键点击并拖动实体在地图上移动。当释放左键时，实体的移动将停止，其位置将在文本编辑器中更新。

![](images/149c1c2a1c30700765aff9df720df27bc2db0394d50e363aa32d93460bb7cab3.jpg)

另一种一次选择多个实体的方法是通过框选功能。按住 Ctrl+Shift 键，左键点击并拖动鼠标覆盖包含所需选择实体的区域。一个框将出现，指示其中包含的所有内容将被选中。一旦覆盖了所需区域，释放左键。所有在选择框内的实体现在都将被选中。

![](images/c7a2b5900de307b3eccd1fa7ed2f977e7b4cbe5c8477efcddbabd6c1daff2e87.jpg)

# 5.1.2.26.17. 坐标转换工具 Position Converter Tool - Wizard

Position Converter Tool 用于在 Latitude/Longitude (LL) 和 Military Grid Reference System(MGRS) 格式之间进行转换。选择转换下拉框中的所需转换，并按照指定格式输入位置。有效输入将生成所需格式的结果。结果可以手动复制，或者可以使用“CopyResult”按钮快速将结果复制到剪贴板。

请注意，MGRS 是一种二维网格系统，用于唯一标识地球上任何地方的一个平方米。它基于 UTM（在 $\boldsymbol { 8 0 } ^ { \circ } ~ \mathsf { S }$ 和 $8 4 ^ { \circ } ~ \mathsf { N }$ 纬度之间）和 UPS 系统。

![](images/bf7eb40a64fa3092283e9d89247d4cb26cde5acbeafda43f377857051641a9d3.jpg)

![](images/d3da315f039614e9bc06a7251efc4bda390b1816fd234deb239a3d55950412a5.jpg)

# 5.1.2.26.18. 报告后处理 Post Processor - Wizard

Post Processor Wizard 插件是用于生成 Post Processor 配置文件和报告的用户界面。该插件位于“Tools”菜单下的“PostProcessor”中，用户可以在此选择要创建的报告类型。然后，用户可以更改报告的选项，包括：时间和纬度/经度格式、子报告类型、平台过滤等。选择所需选项后，选择“GenerateReports”，将创建两个文件：包含当前输入设置的配置文件和相应的报告。

![](images/389423dbdf47710eeb9100a0e65e00fbda7f2eaf91acafc835cf2f56d7c0fee8.jpg)

![](images/37ddaf32c53948792899a2ca593f23654f01e5a4235472b4014b892252152c7f.jpg)

![](images/144fcc15a21c24043d5a5f1d45b1b3ed93afe9e74270f20950b10f359c6182d2.jpg)

# 5.1.2.26.19. 旋转对话框 Rotate Dialog - Wizard

![](images/4b0416d925391f70730d7f748ed62f726397571b0dfad9e232f3b19ac00f9b66.jpg)

“RotateScenario” 对话框 可用于旋转整个场景或地图显示上的一组选定对象。此工具可以在“Tools”菜单下的“Map Utilities”中找到。

警告：旋转工具无法更改具有空间移动器的平台的位置和方向，因为大多数情况下，这些移动器不是通过六自由度定义的，而是通过其他参数定义的。

# 菜单

![](images/54fea45a7383b3aef2de4e27e07aa033e9940c3096d78ef60bbfa22f62d67bae.jpg)

菜单包含以下项目：

“RotateScenario”：此项目将对话框设置为允许用户旋转整个场景的模式。  
“RotateSelection”：此项目将对话框设置为允许用户旋转一组选定对象的模式。

注意：如果地图上没有任何内容，则没有菜单选项可用。如果地图上没有选中任何内容，则只有“Rotate Scenario”选项可用。

# 输入方法

行编辑：允许用户输入旋转角度。

注意：角度的格式为：“vu”，其中 $\mathsf { \pmb v }$ 是十进制值，u 是单位。值和单位之间有一个空格。行编辑初始化为角度 0。单位由首选项确定，但可以更改为 AFSIM 支持的任何单位。

拨盘：允许用户以“动画”风格旋转。

注意：拨盘仅以整数度旋转。

# 5.1.2.26.20. 想定分析工具 Scenario Analyzer

![](images/7ca9807ab8f4c31320a24cb9e287a5e0e1fefedc29cde331e5d0df0e9a7e6d98.jpg)

# 5.1.2.26.20.1. 使用想定分析器 Using the Scenario Analyzer

Scenario Analyzer 是 Wizard（AFSIM 的 IDE）的一个插件，帮助分析人员在场景创建过程中识别和解决常见错误。Scenario Analyzer 包括两类测试，分析人员可以对场景运行：‘Checks’ 和 ‘Session Notes’。

Checks 是 ScenarioAnalyzer 的核心功能，分析人员可以使用这些测试来评估场景中未链接的传感器、没有通信设备的指挥链、没有所需特征的平台以及其他直接涉及场景内容的常见问题。Checks 被组织成称为‘套件’的组。Scenario Analyzer 提供了两个 Checks套件，一个用于核心 AFSIM，一个用于 IADS C2。分析人员可以选择对场景运行单个Check、多个 Checks、完整的 Check 套件或所有可用的 Checks。每个 Check 都有一个对应的严重性级别——‘警告’或‘错误’，指示解决 Check 识别的问题的紧迫性。当 Check 结果显示给分析人员时，它们按套件分组。在每个套件中，结果进一步按严重性分组。失败的 Check 结果根据 Check 的严重性分类为 WARNING 或 ERROR，而通过的 Check 结果分类为 PASS。如果场景的每个部分都通过了 Check，则场景通过Check。相反，如果场景的任何部分未通过 Check，则场景未通过 Check。例如，核心AFSIMCheck Sensors 必须内部链接评估场景中每个平台上的每个传感器，并验证每个传感器是否与另一个平台部分有内部链接。在具有 100 个传感器的场景中，无论是 1个传感器还是 99 个传感器未链接，Check 都会失败。这意味着一个失败的 Check 可能对应于许多失败实例。当 ScenarioAnalyzer 返回 Check 结果时，它会为每个失败实

例显示详细消息。详细消息包括问题描述和解决问题的说明（如果解决方案不够明显）。此外，右键点击详细消息会弹出一个上下文菜单，其中包含可能与解决问题相关的场景文件位置的链接。

Session Notes 保证每次分析人员运行 Scenario Analyzer 时执行。虽然 Checks 查找场景内容引起的问题，但 SessionNotes 评估运行 Checks 的环境，并通知分析人员可能影响 Check 结果有效性或有用性的情况。例如，名为 Missing Platforms 的 Session Note通知用户在运行 Checks 时尚未添加到模拟中的平台，因为平台的缺失可能导致 Check结果中的假阴性和假阳性。（有关何时执行 Checks 以及如何修改执行时间的更多信息，请参阅高级功能：修改 Check 执行时间）。Session Notes 的结果与 Check 结果显示在同一窗格中。SessionNotes 没有组织成套件或严重性级别，但结果仍包括每个失败实例的详细消息。

与其他 Wizard 插件一样，ScenarioAnalyzer 可以使用工具菜单中的插件管理器加载和卸载。加载后，插件会在 Wizard GUI 中添加两个窗格，一个用于选择要运行的 Checks（Scenario Analyzer Checks），另一个用于显示结果（Scenario Analyzer Results）。可以通过在视图菜单中选择它们来添加和移除这些窗格。

# 加载 Checks

![](images/8eabe791419e9a3e9b42ac74bbc2b0ef9fe739ffc047d60fe0c506fa0fd69e40.jpg)

ScenarioAnalyzerChecks 窗格包含一个可扩展的复选框树，表示按套件组织的所有可用Checks。当 Scenario Analyzer 插件在 Wizard 中加载时，check_suites 目录中文件中定义的所有 Checks（其依赖项存在）将自动显示在 Scenario Analyzer Checks 窗格中。

Suites 目录中的每个文件代表一个单独的 Checks 套件。例如，Scenario Analyzer Checks窗格图像中显示为‘core’套件的一部分的所有 Checks 都在 check_suites/core.txt 中定义。点击 LoadChecks 按钮通过解析 check_suites 目录中的所有文本文件重新填充复选框树。

ScenarioAnalyzer 还会在打开 Wizard、活动项目更改以及活动可执行文件更改时加载或

重新加载 Checks。加载 Checks 时，Scenario Analyzer 会检查每个套件的依赖项，并仅在所有依赖项都存在时加载该套件中的 Checks。无法加载的套件中的 Checks 仍然在 ScenarioAnalyzerChecks 窗格中可见，但它们以浅灰色字体显示，无法选择或运行。在图像中，ScenarioAnalyzer 未加载 IADS C2 套件的 Checks，因为缺少 wsf_iads_c2 插件。如果无法加载套件，ScenarioAnalyzer 将显示一个弹出消息，显示套件的名称以及缺少的插件或库的名称，如本节中显示的弹出窗口。有关如何定义和评估 Check 套件的依赖项的更多详细信息，请参阅添加新 Checks 的一般说明中的‘dependencies script block’部分。

![](images/ec0b9e8a6fa8d2486b5321fc3cc3b5dc8cc10dcf2b35314cb0ebc86e4912060b.jpg)

# 选择和运行 Checks

分析人员可以选择任何组合的 Checks 来对场景运行。在本节中显示的 ScenarioAnalyzer Checks 窗格中，‘core’套件中的所有 Checks 和‘iads_c2’套件中的几个单独 Checks已被选择执行。

点击 Run Checks 使用所有选定的 Checks 测试已设置为启动文件的场景。ScenarioAnalyzer 通过生成一个新场景文件来评估场景，该文件包括启动文件以及 check_suites 和session_note_suites 目录中的所有文件。此自动生成的文件可以在 Scenario Analyzer Results窗格中的 Generated Scenario File 选项卡中查看。

Scenario Analyzer Results 图像中显示的场景文件显示了运行选定 Checks 的结果。每个选定的 Check 都设置为在模拟初始化后立即执行。此外，session_notes_suites 目录中的文件中包含的所有 SessionNotes 都计划执行。在这种情况下，只有一个 SessionNote 存在：Warn_if_platforms_are_not_in_simulation()。有关更多信息，请阅读 Missing Platforms SessionNote 描述。

![](images/cb6a36d711badb917f12fc0a3d15b3848def4492a1f381f39529af27808c0792.jpg)

# 查看和使用结果

为了演示如何查看和使用 ScenarioAnalyzer 的输出，我们将检查在 AFSIM 分析课程中常用的 debugging_quiz 场景上运行 Core 套件 Checks 的结果。在选择所有 Core Checks并点击 Run Checks 按钮后，Scenario Analyzer Results 窗格中出现如下输出。我们可以看到，该场景通过了九个 Checks，失败了八个，其中一个是错误级别的 Check，七个是警告级别的 Check。Session Notes 出现在结果树中但无法展开，这告诉我们至少有一个 Session Note运行了，但没有返回有用的信息。

![](images/50a5e5fd36156e021d8ca104cf9421fcff22936ca72d9b2770e2b6c65db9724f.jpg)

展开 WARNING 和 ERROR 严重性级别，我们可以看到场景失败的 Checks 的名称。我们可以进一步展开每个失败的 Check，以查看每个失败实例的详细消息。正如下面完整Wizard 窗口的图片所示，场景未通过错误级别的 Check Sensors must be internally linked，因为平台 pirate_ac_1 上的传感器 eyes 未与任何其他平台组件内部链接。场景还未通过警告级别的 Check Sensors should be linked to track processor，因为 pirate_ac_1 上的相同传感器eyes 未直接或间接链接到跟踪处理器。错误级别失败的详细消息指示我们使用 internal_link将 eyes 链接到处理器，例如跟踪处理器。我们可以通过确保 eyes 直接链接到跟踪处理器或链接到与跟踪处理器通信的另一个平台来解决这两个失败。右键点击消息会弹出一个上下文菜单，其中包含指向 pirate_ac_1 和 eyes 的超链接，我们可以使用这些链接导航到场景文件中的相关位置。

![](images/5abfb3fc95f100b29cf36e9550fe221023430326d7ef6a7ef9a84d0e322dca6e.jpg)

点击 pirate_ac_1 的链接将我们带到平台，我们可以从那里轻松导航到 pirate_ac_1 的实例 SOCATA_TB9 的平台类型。果然，传感器 eyes 未链接到任何东西。添加一个内部链接到跟踪处理器 data_mgr，如文本编辑窗格的图像所示，将通过 (1) 确保传感器与其他平台

部分有内部链接和 (2) 确保传感器可以将其数据传输到跟踪处理器来解决这两个失败。

![](images/75f8af36e21cb5dd64231f184260d40dd439ffe9094e3bb2f52599431da0d1d3.jpg)

如果我们保存场景并重新运行 Core Checks，我们会得到以下结果：

All results Check Results Core PASS (10) $\nu$ Warning6 Declared command chains should have structure Sensor platforms should have at least one sensor turned on All signatures should be detectable by an enemy sensor Platforms should have signatures required by sensors in scenario Track processors should have purge interval defined Deployed weapons should have quantity greater than zero $\nu$ ERROR (1) Track processor purging intervals must be long enough to maintain tracks Session Notes

添加从 eyes 到 data_mgr 的内部链接修复了导致 Sensors must be internally linked 和Sensors should be linked to track processor 失败的问题，但我们现在有一个不同的错误级别失败：Track processor purging intervals must be long enough to maintain tracks。该 Check 的详细消息如下：

pirate_ac_1 上的传感器 eyes 有一个模式 default，至少需要 5.000000 秒才能获得足够的命中以维持跟踪，但传感器最终报告给平台 pirate_ac_1 上的跟踪处理器 data_mgr，该处理器的清除间隔仅为 0.000000 秒。为了解决这个问题，(1) 减少模式的 ‘frame_time’，(2) 减少 ‘hits_to_maintain_track’ 的第一个值，或 (3) 增加 ‘purge_interval’。

我们有几种选择来修改场景以通过此 Check，但另一个警告级别失败，Trackprocessorsshould have purge interval defined，帮助我们确定正确的选项。该 Check 的详细消息如下：平台 pirate_ac_1 上的跟踪处理器 data_mgr 的跟踪清除间隔为 0 秒，因此跟踪不会被清除。用户可以使用 ‘purge_interval <time_value>’ 或 ‘drop_after_inactive <time_value>’ 来设置非零的跟踪清除间隔。

这两个详细消息让我们知道，给 data_mgr 一个大于传感器 eyes 上模式 default 所需的 5 秒的清除间隔应该可以解决这两个 Check 失败。本节的最后一张图片显示了对

data_mgr 的必要编辑以及在修复后重新运行 Core 套件后产生的 Check 结果：场景现在通过了十七个 Checks 中的十二个，仅失败了五个警告级别的 Checks。

platfom type SOCATA_TB9 WsF_PLATFORM All results   
side red Check Results Core   
sensor eyes EYE_SENSOR PASS (12) internal_link data_mgr $\nvdash$ WARNING (5) end_sensor Declared command chains should have structure processor task_mgr AIRCRAFT_TACTICS Sensor platforms should have at least one sensor turned on end Processor All signatures should be detectable by an enemy sensor #processor send_it SEND_MESSAGE Deployed weapons should have quantity greater than zero end Processor Session Notes   
processor data_mgr WsFTRACKPROCESSOR external_link subordinates via pirate_comm purge_interval 60 s   
end Processor

# 高级功能：修改 Check 执行时间

ScenarioAnalyzer 的默认行为是在模拟初始化后立即运行所有选定的 Checks，而不提供用户调整 Check 执行时间的选项。然而，如果 Missing Platforms Session Note 确定模拟中缺少一个或多个平台，Scenario Analyzer 将通过添加一个文本框来修改 Scenario AnalyzerChecks 窗格中的控件，该文本框可用于指定执行 Checks 的模拟时间。用户可以以天:小时:分钟:秒格式或以秒为单位输入时间。输入框右侧的文本将使用第一种格式显示所选的Check 执行时间。

![](images/a20d6d6c2c14de57cc71e19357188fafe85ddc2ee3aadc7f3c50712cc37b85d3.jpg)

将上一节中的 pirate_ac_1 的 creation_time 更改为 30 秒的模拟时间说明了此功能为何有用。仅进行此更改并重新运行 CoreChecks 会产生如下结果：

```txt
- All results
- Check Results
- Core
- PASS (15)
- WARNING (2)
- All signatures should be detectable by an enemy sensor
- Deployed weapons should have quantity greater than zero
- Session Notes
- Missing Platforms 
```

由于 pirate_ac_1 在运行 Checks 时不存在，前一节末尾看到的五个警告级别失败中的三个消失了。导致这些警告的问题，例如未打开平台的任何传感器，尚未解决。然而，pirate_ac_1 对 Checks 是不可见的。

如果我们展开 Missing Platforms Session Note，我们会看到以下消息：

平台 pirate_ac_1 在运行 Checks 时不在模拟中：这可能是因为平台的创建时间为

30.000000 秒，而工具的默认行为是在模拟初始化后立即运行所有选定的 Checks。您可以通过在 ‘Run Checks’ 按钮旁边的文本框中输入执行 Checks 的时间来调整运行 Checks 的时间，以便在此平台的创建时间之后。（请注意，如果您推进模拟时间，其他平台可能会被删除。）

由于 Missing Platforms 发现模拟中缺少一个平台，Scenario Analyzer 现在提供了调整Checks 执行时间的选项。如果我们将执行时间更改为 35 秒并重新运行 CoreChecks，我们会得到如下输出。由于 pirate_ac_1 在运行 Checks 时存在于模拟中，场景失败了我们在上一节末尾看到的相同五个警告级别的 Checks。此外，Missing Platforms Session Note 不再显示任何输出，因为在 Check 执行时间所有平台都存在。

![](images/eaaf6c1bd097411277dee1ea1cbc32471de947c727520f3d3a80554e0d3f70b3.jpg)

调整 Check 执行时间时，重要的是要意识到推进模拟时间以包括后创建的平台可能意味着在运行 Checks 时其他平台已经被删除。就像在某些平台尚未创建之前运行 Checks 一样，在某些平台被删除之后运行 Checks 也可能导致假阳性和假阴性。Missing PlatformsSessionNote 将再次通知用户在 Checks 执行时平台是否不存在。如果 Check 执行时间在缺少平台的创建时间之后，SessionNote 将说明平台可能已被删除。

一旦执行时间框出现并为用户提供调整运行 Checks 时间的选项，该框将在 Wizard 会话期间保持可见和可用。关闭 Wizard 或卸载并重新加载 ScenarioAnalyzer 插件将导致该框消失。

# 5.1.2.26.20.2. 包含的 Checks 描述 Descriptions of Included Checks

# 核心 AFSIM Checks

Comm devices must have internal links：检查每个通信设备（WSF_COMM_TRANSCEIVER、WSF_COMM_XMTR、WSF_COMM_RCVR）是否至少有一个内部链接（internal_link）将其连接到任何其他平台部分。请注意，通过此检查并不保证通信设备接收到的数据会传递到期望接收数据的平台或平台部分。  
Platforms in command chains must have comm devices：检查属于声明的指挥链的每个平台是否至少有一个通信设备。如果一个平台仅属于默认指挥链，或者一个平台属于一个声明的指挥链且它是自己的指挥官且没有下属，则不会触发检查。检查的前提是，除非这些平台能够相互通信，否则将平台组织成指挥链是无用的。然而，请注意，通过检查并不保证指挥链中的平台会按预期通信。例如，仍然需要确保旨在相互通信的平台在同一网络上具有通信设备，通信设备通过内部链接（internal_link）正确连接到处理器，并且旨在传播信息的处理器使用 report_to 或 report_to_group 语句设置了与正确平台的外部链接。  
Declared command chains should have structure：对于声明的指挥链中的每个平台，检查 该平台不是自己的指挥官，或者在该指挥链中至少有一个下属或同级。‘声明的指挥链’

是指具有用户定义名称的指挥链（例如，command_chain MY_COMMAND_CHAIN SELF），与默认指挥链不同，当未指定指挥链名称时，平台被添加到默认指挥链中（例如，commander SELF）。

Declared commander should be in that chain：检查每个平台在声明的指挥链中被另一个平台识别为其指挥官时，该平台是否是该指挥链的成员。例如，如果平台 ew_radar 使用 command_chain BLUE blue_cmdr 识别指挥官，那么平台 blue_cmdr 也应该在 BLUE指挥链中识别其指挥官（即使该指挥官是 SELF），以便被识别为属于 BLUE。  
Scenarios with many platforms should have a command chain：检查任何‘大型’模拟（目前在检查中定义为具有 10 个或更多平台）是否包含至少一个具有某种结构的指挥链。如果声明的指挥链中至少有一个平台不是自己的指挥官，具有至少一个下属，或具有至少一个同级，则声明的指挥链具有结构。场景不需要有声明的指挥链即可通过此检查：如果默认指挥链已被赋予结构（例如，通过为平台分配一个非 SELF 的指挥官），检查将通过。如果模拟中的任何地方存在指挥链，即使一侧有 10 个或更多平台且该侧没有指挥链，检查也会满足。  
All platforms should have meaningful locations defined：检查每个平台是否定义了一个起始位置，该位置至少包括纬度、经度和高度中的一个非零值。命令 position<Latitude><Longitude> [<Altitude>] 定义了平台的位置。  
Sensors must be internally linked：检查每个传感器是否至少定义了一个从该传感器到同一平台上任何其他部分的 internal_link。如果传感器没有定义内部链接，它收集的信息将永远不会被使用。请注意，通过此检查并不保证传感器信息会传递到期望接收信息的平台或平台部分。

Sensor platforms should have at least one sensor turned on：

□ 如果未加载 wsf_iads_c2 插件：检查每个平台是否至少有一个传感器开启。  
□ 如果已加载 wsf_iads_c2 插件：如果平台不是 IADS C2 系统的一部分，检查将发出警告，如果平台有一个或多个传感器且没有传感器开启。如果平台是 IADSC2 系统的一部分，检查还将评估平台传感器的类别（TTR、TAR、EW、RWR），如果平台有一个或多个非 TTR 传感器且所有传感器都关闭，将发出警告。对于此检查，如果平台的传感器由传感器管理器管理，即平台在默认指挥链上从属于具有传感器管理器的平台，则该平台是 IADSC2 系统的一部分。

Sensors should be linked to track processor：

▫ 对于非 WSF_SAR_SENSORs 的传感器：检查每个传感器是否至少有一个WSF_TRACK_PROCESSOR 是从传感器‘链接且可达’的。如果传感器具有一个内部链接到同一平台上的跟踪处理器，或者传感器通过内部链接和外部链接（使用report_to 或 report_to_group 命令定义）与每个外部链接两侧的兼容通信设备连接 ， 则 跟 踪 处 理 器 是 从 传 感 器 链 接 且 可 达 的 。 检 查 使 用 等 效 的‘ScenarioAnalyzerUtils.LinkedAndReachablePlatformPartsChooseProcs<#arraywsfplatformpart-linkedandreachableplatformpartschooseprocswsfplatformpart-origin-string-parttype-arraystring-processortypes-bool-followspecifiedprocs>’__ 脚 本方法来查找传感器链接到的跟踪处理器，并排除来自其他跟踪处理器的中间外部链接。有关如何发现链接且可达的跟踪处理器的更详细说明，请参阅该辅助方法的描述。  
□ 对 于 WSF_SAR_SENSORs ： 检 查 每 个 SAR 传 感 器 是 否 至 少 有 一 个WSF_IMAGE_PROCESSOR 或 WSF_VIDEO_PROCESSOR (1) 是从传感器‘链接且可达’的，并且 (2) 是内部链接到 WSF_TRACK_PROCESSOR 的。SAR 必须以与非 SAR 传

感器必须连接到跟踪处理器相同的方式连接到图像或视频处理器，如上所述。

All signatures should be detectable by enemy sensors：检查模拟中的每个平台，确保至少有一个敌方传感器可以检测到每个平台的每种签名类型。检查考虑以下签名类型：acoustic_signature 、 infrared_signature 、 inherent_contrast 、 optical_signature 和radar_signature。对于此检查，如果传感器使用该类型的签名，则传感器“可以检测”签名 类 型 。 例 如 ， 任 何 WSF_RADAR_SENSOR 可 以 检 测 雷 达 签 名 ， 任 何WSF_ACOUSTIC_SENSOR 可以检测声学签名，而任何 WSF_IRST_SENSOR 可以检测红外签名、固有对比度和光学签名。如果传感器位于属于与被评估签名的平台不同侧（使用side<side> 命令设置）的平台上，则该传感器是“敌方传感器”。请注意，通过此检查并不 保 证 所 有 平 台 实 际 上 会 被 敌 方 传 感 器 检 测 到 ： 只 要 某 个 敌 方 平 台 有WSF_RADAR_SENSOR，具有 radar_signature 的平台就会通过此检查，但如果其雷达签名超出传感器的频带，则该平台实际上将不可检测。  
Platforms should have signatures required by sensors in scenario：对于模拟中传感器所需的每种签名类型，检查模拟中的每个平台是否定义了该类型的签名。例如，如果一个平台上的传感器有 WSF_RADAR_SENSOR，则对于缺少 radar_signature 的每个平台，检查将发出警告。  
Script processors must have update intervals defined：检查任何 WSF_SCRIPT_PROCESSOR或 WSF_QUANTUM_TASK_PROCESSOR 是否定义了非零更新间隔（使用 update_interval<time-reference>）。如果未定义更新间隔或设置为零，则脚本处理器将永远不会更新。  
Track processor purging intervals must be long enough to maintain tracks：对于每个跟踪处理器（WSF_TRACK_PROCESSOR），检查清除间隔是否足够长，以便它可以维护由连接到它的每个传感器生成的数据的跟踪。检查将跟踪处理器的清除间隔（由命令purge_interval <time-value> 或 drop_after_inactive <time-value> 设置）与每个连接到跟踪处理器的传感器的每种模式的绝对最小时间和“检测窗口时间”进行比较。任何传感器模式的绝对最小时间等于模式的帧时间（由 frame_time <time-value> 设置）与hits_to_maintain_track <integer> <integer> 指定的第一个值的乘积。传感器模式的检测窗口等于其帧时间与 hits_to_maintain_track 的第二个值的乘积。例如，以下传感器的绝对最小所需时间为 30 秒，检测窗口为 50 秒：

```txt
sensor my_sensor WSFGEOMETRIC_SENSOR on frame_time 10s hits_to Maintain_track35 [. .]   
end SENSOR 
```

如果连接到此传感器的跟踪处理器的清除间隔为 20 秒，则不可能基于此传感器的数据维护跟踪，因为传感器不可能在该时间内获得所需的三个命中。因此，此检查将生成错误级别消息。如果跟踪处理器的清除间隔为 45 秒，则传感器可能但不太可能获得所需的三个命中，因为其检测窗口大于清除窗口，检查将生成警告级别消息。此检查使用等效的‘ScenarioAnalyzerUtils.LinkedAndReachablePlatformPartsChooseProcs

<#arraywsfplatformpart-linkedandreachableplatformpartschooseprocswsfplatformpart-origin-stri ng-parttype-arraystring-processortypes-bool-followspecifiedprocs>’__ 脚本方法来查找传感器

链接到的跟踪处理器，并排除来自其他跟踪处理器的中间外部链接。有关如何发现链接且可达的跟踪处理器的更详细说明，请参阅该辅助方法的描述。

Track processors should have purge interval defined ： 检 查 每 个 跟 踪 处 理 器（WSF_TRACK_PROCESSOR）是否定义了非零清除间隔。清除间隔由 purge_interval<time-value> 或 drop_after_inactive <time-value> 定义，决定了跟踪处理器在丢弃跟踪之前等待多长时间而不接收更新。如果未定义清除间隔或设置为 0 秒，则跟踪将永远不会被清除。  
Track processors should not circularly report fused tracks ： 检 查 两 个 跟 踪 处 理 器（WSF_TRACK_PROCESSOR）相互报告融合跟踪的情况。是否报告融合跟踪由命令fused_track_reporting <boolean-value> 设置，默认为 false。如果两个跟踪处理器相互“链接 且 可 达 ” ， 则 它 们 相 互 报 告 。 此 检 查 使 用 等 效 的‘ScenarioAnalyzerUtils.LinkedAndReachablePlatformPartsChooseProcs

<#arraywsfplatformpart-linkedandreachableplatformpartschooseprocswsfplatformpart-origin-string-parttype-arraystring-processortypes-bool-followspecifiedprocs>’__ 脚本方法来查找另一个跟踪处理器报告的跟踪处理器，并排除来自其他跟踪处理器的中间外部链接。

有关如何发现链接且可达的跟踪处理器的更详细说明，请参阅该辅助方法的描述。

这是一个循环跟踪报告的示例：

```fortran
platform WMPlatform_1 WSFPLATFORM
commander WMPlatform_2
add processor data_mgr_1 WSF Track Processor
purge_interval 60 s
report_to commander
report_fused Tracks
end处理器
[...] end platform
platform WMPlatform_2 WSF PLATFORM
add processor data_mgr_2 WSF Track Processor
purge_interval 60 s
report_to subordinates
fused_track_reporting on
end处理器
[...] end platform 
```

User configured speed should be within mover capabilities ： 对 于 每 个 具 有 从WsfWaypointMover 派生的移动器的平台，检查平台路线中任何航点的用户配置速度是否 超 过 移 动 器 的 maximum_speed 。 从 WsfWaypointMover 派 生 的 移 动 器 包 括WSF_AIR_MOVER 、 WSF_GROUND_MOVER 、 WSF_SURFACE_MOVER 和WSF_SUBSURFACE_MOVER 。 用 户 可 以 使 用 命 令 position <Latitude> <Longitude>[<Altitude>] speed <real> <speed-unit> 在平台的路线块中配置航点的速度。请注意，即使用户将航点的速度设置为大于最大值，移动器也永远不会超过其最大速度。

Deployed weapons should have quantity greater than zero：遍历模拟中每个平台上的所有显式武器（为其定义了 launched_platform_type 的武器），并验证每个显式武器是否

已分配非零数量。

# IADS C2 Checks

Asset managers should have update interval defined ： 检 查 每 个 资 产 管 理 器（WSF_UNCLASS_ASSET_MANAGER）是否定义了非零更新间隔（使用 update_interval<time-reference>）。如果未定义更新间隔或设置为零，则资产管理器将永远不会更新。  
Asset manager platforms should deploy disseminate C2 manager：检查每个部署资产管理器的平台是否也具有传播 C2 管理器（WSF_UNCLASS_DISSEMINATE_C2）。  
Battle manager platforms must be C2 capable ： 检 查 每 个 部 署 传 感 器 管 理 器（WSF_SIMPLE_SENSORS_MANAGER、WSF_FOV_SENSORS_MANAGER）的平台是否也部署 了 跟 踪 处 理 器 （ WSF_TRACK_PROCESSOR ） 和 传 播 C2 管 理 器（WSF_UNCLASS_DISSEMINATE_C2）。具有传感器管理器的平台还必须部署资产管理器（WSF_UNCLASS_ASSET_MANAGER），但检查不会查找资产管理器，因为如果没有资产管理器，平台初始化将在检查运行之前失败。  
Battle managers must have subordinate weapons managers linked by C2-capable platforms：检查每个具有战斗管理器（WSF_UNCLASS_BM）的平台是否在默认指挥链上至少有一个具有武器管理器（WSF_WEAPONS_MANAGER_SAM 或 WSF_WEAPONS_MANAGER_AI）的下属平台。战斗管理器及其下属武器管理器之间的每个平台（包括战斗管理器和武器管理器平台）必须是“C2 能力”的。在此检查的上下文中，如果平台具有 (1) 资产管理器，(2) 传播 C2 管理器，并且 (3) max_assignments $> 0$ ，则该平台是 $^ { \prime \prime } ( 2$ 能力”的。  
Battle managers should be reachable by subordinate sensors：检查每个战斗管理器是否可以被其在任何指挥链上的下属传感器访问。如果战斗管理器平台上的跟踪处理器是从传感器“链接且可达”的，则传感器可以访问战斗管理器。此检查使用等效的‘ScenarioAnalyzerUtils.LinkedAndReachablePlatformPartsChooseProcs<#arraywsfplatformpart-linkedandreachableplatformpartschooseprocswsfplatformpart-origin-string-parttype-arraystring-processortypes-bool-followspecifiedprocs>’__ 脚本方法来查找另一个跟踪处理器报告的跟踪处理器，并排除来自其他跟踪处理器的中间外部链接。有关如何发现链接且可达的跟踪处理器的更详细说明，请参阅该辅助方法的描述。  
Battle managers should have subordinate sensors managers linked by C2-capable platforms：检查每个具有战斗管理器（WSF_UNCLASS_BM）的平台是否在默认指挥链上至少有一个具 有 传 感 器 管 理 器 （ WSF_SIMPLE_SENSORS_MANAGER 或WSF_FOV_SENSORS_MANAGER）的下属平台。战斗管理器及其下属传感器管理器之间的每个平台（包括战斗管理器和传感器管理器平台）必须是“C2 能力”的。在此检查的上下文中，如果平台具有 (1) 资产管理器和 (2) 传播 C2 管理器，则该平台是“C2 能力”的。  
Battle managers should not conflict with each other：检查没有具有提交权限的战斗管理器从属于默认指挥链上另一个具有提交权限的战斗管理器。战斗管理器上的提交权限由命令 commit_authority <boolean-value> 设置。  
Disseminate C2 manager platforms must have internal comm links：对于每个具有传播 C2管理器（WSF_UNCLASS_DISSEMINATE_C2）的平台，检查平台上的至少一个通信设备（WSF_COMM_TRANSCEIVER、WSF_COMM_XMTR、WSF_COMM_RCVR）是否具有与传播 C2 管理器的内部链接（internal_link）。  
Sensors manager platforms must be C2 capable ： 检 查 每 个 部 署 传 感 器 管 理 器（WSF_SIMPLE_SENSORS_MANAGER、WSF_FOV_SENSORS_MANAGER）的平台是否也部

署 了 跟 踪 处 理 器 （ WSF_TRACK_PROCESSOR ） 和 传 播 C2 管 理 器（WSF_UNCLASS_DISSEMINATE_C2）。具有传感器管理器的平台还必须部署资产管理器（WSF_UNCLASS_ASSET_MANAGER），但检查不会查找资产管理器，因为如果没有资产管理器，平台初始化将在检查运行之前失败。

Sensors manager platforms must be connected to battle manager with commit authority：检查 每 个 部 署 传 感 器 管 理 器 （ WSF_SIMPLE_SENSORS_MANAGER 、WSF_FOV_SENSORS_MANAGER）的平台是否在默认指挥链上从属于具有提交权限的战斗管理器（WSF_UNCLASS_BM）。战斗管理器上的提交权限由命令 commit_authority<boolean-value> 设置。  
Sensors managers must not conflict with each other ： 检 查 导 致 传 感 器 管 理 器（WSF_SIMPLE_SENSORS_MANAGER、WSF_FOV_SENSORS_MANAGER）冲突的指挥链配置 ， 这 些 冲 突 从 武 器 管 理 器 （ WSF_WEAPONS_MANAGER_SAM 、WSF_WEAPONS_MANAGER_AI）的角度来看发生。对于从属于默认指挥链上具有提交权限的战斗管理器（WSF_UNCLASS_BM）的任何武器管理器，如果在默认指挥链上武器管理器平台和战斗管理器平台之间（包括战斗管理器平台）有多个平台具有传感器管理器，则存在传感器管理器冲突。然而，如果武器管理器平台部署了自己的传感器管理器，则从武器管理器平台的角度来看永远不会发生冲突，无论其与战斗管理器之间有多少其他传感器管理器。这意味着默认指挥链中相同的传感器管理器配置可以相对于某些下属平台创建传感器管理器冲突，同时避免相对于其他平台的冲突。  
Sensors manager platforms must be connected to TAR or TTR：检查每个部署传感器管理器（WSF_SIMPLE_SENSORS_MANAGER、WSF_FOV_SENSORS_MANAGER）的平台是否在默认指挥链上优于至少一个具有 TAR 或 TTR 类型传感器的平台。如果传感器管理器平台上有 TAR 或 TTR，则检查满足。传感器的类型由命令 category <EW/TAR/TTR/RWR>确定，无论传感器的属性或其实例化的类如何。例如，分配了 TAR 类别的WSF_GEOMETRIC_SENSOR 将被视为 TAR，无论是为了此检查还是在 IADS C2 代码中。  
Sensors manager max acquisition times should be long enough for subordinate sensors toformtracks：检查传感器管理器的最大 TAR 和 TTR 获取时间是否足够长，以便其下属的 TAR 和 TTR 形成跟踪。检查将传感器管理器的最大获取时间（由命令max_ttr_acquisition_time <time-value> 和 max_tar_acquisition_time <time-value> 设置）与在默认指挥链上从属于传感器的每个传感器模式的绝对最小时间和“检测窗口时间”进行比较。任何传感器模式的绝对最小时间等于模式的帧时间（由 frame_time<time-value> 设置）与 hits_to_establish_track <integer> <integer> 指定的第一个值的乘积。传感器模式的检测窗口等于其帧时间与 hits_to_establish_track 的第二个值的乘积。此检查是必要的，因为如果传感器在被提示的最大获取时间内尚未开始跟踪，传感器管理器将取消传感器的分配。  
Platforms with TAR or TTR should be connected to sensors manager：检查每个具有 TAR 或TTR 类 型 传 感 器 的 平 台 是 否 在 默 认 指 挥 链 上 从 属 于 部 署 传 感 器 管 理 器（WSF_SIMPLE_SENSORS_MANAGER、WSF_FOV_SENSORS_MANAGER）的平台。如果传感器平台部署了传感器管理器，则检查满足。传感器的类型由命令 category<EW/TAR/TTR/RWR> 确定，无论传感器的属性或其实例化的类如何。例如，分配了 TAR类别的 WSF_GEOMETRIC_SENSOR 将被视为 TAR，无论是为了此检查还是在 IADS C2代码中。请注意，通过此检查的具有 TAR 或 TTR 的平台可能会从多个传感器管理器接收冲突的命令。另一个 IADS C2 检查，“Sensors managers must not conflict with eachother <#sensors-managers-must-not-conflict-with-each-other>”，测试这种情况。

TTRs managed by FOV sensors manager must not manipulate on/off state：检查每个在默认指挥链上从属于具有 WSF_SENSORS_MANAGER_FOV 的平台的 TTR 类别传感器是否最初关闭。虽然创建场景的分析人员可能会定义一个操纵 TTR 开/关状态的脚本，但ScenarioAnalyzer 无法检测脚本的内容，因此此检查仅确保由视场传感器管理器管理的TTR 未被打开。  
TTRs managed by FOV sensors manager must use default sensor scheduler：检查每个在默认指挥链上从属于具有 WSF_SENSORS_MANAGER_FOV 的平台的 TTR 类别传感器是否使用默认传感器调度器。传感器的调度器可以通过调度器命令指定，例如，schedulerdefault 或 scheduler physical_scan。  
TTRs managed by FOV sensors manager should provide auxiliary data：检查每个在默认指挥链上从属于具有 WSF_SENSORS_MANAGER_FOV 的平台的 TTR 类别传感器是否提供以下 辅 助 数 据 ： RESTING_AZIMUTH 、 COARSE_SLEW_RATE_AZIMUTH 和FINE_SLEW_RATE_AZIMUTH。  
TTRs managed by FOV sensors managers should use one beam per mode：检查每个在默认指挥链上从属于具有 WSF_SENSORS_MANAGER_FOV 的平台的 TTR 类别传感器是否为其每种模式定义了一个波束。  
Platforms with weapons should deploy weapons manager：检查每个至少有一种武器的平台 是 否 也 部 署 了 武 器 管 理 器 （ WSF_WEAPONS_MANAGER_SAM 或WSF_WEAPONS_MANAGER_AI）。  
Weapons manager platforms must be C2 capable ： 检 查 每 个 部 署 武 器 管 理 器（WSF_WEAPONS_MANAGER_SAM、WSF_WEAPONS_MANAGER_AI）的平台是否也部署了 跟 踪 处 理 器 （ WSF_TRACK_PROCESSOR ） 和 传 播 C2 管 理 器（WSF_UNCLASS_DISSEMINATE_C2）。具有武器管理器的平台还必须部署资产管理器（WSF_ASSET_MANAGER），但检查不会查找资产管理器，因为如果没有资产管理器，平台初始化将在检查运行之前失败。  
Weapons manager platforms must deploy weapons：检查每个部署武器管理器的平台是否至 少 有 一 种 武 器 （ 例 如 ， WSF_EXPLICIT_WEAPON 、 WSF_IMPLICIT_WEAPON 或WSF_RF_JAMMER）。  
Weapons manager platforms must be connected to battle manager with commit authority：检查每个部署武器管理器（WSF_WEAPONS_MANAGER、WSF_WEAPONS_MANAGER_SAM、WSF_WEAPONS_MANAGER_AI）的平台是否在默认指挥链上从属于具有提交权限的战斗管理器（WSF_UNCLASS_BM）。战斗管理器上的提交权限由命令 commit_authority<boolean-value> 设置。  
Weapons manager platforms should have access to required sensor：对于每个具有武器管理器（WEAPONS_MANAGER_SAM、WEAPONS_MANAGER_AI）的平台，检查平台是否可以访问至少满足武器管理器所需质量的传感器。武器管理器所需的传感器质量由engagement_settings 块确定，该块设置武器管理器是否会参与来自每个类别传感器的跟踪。具有以下 engagement settings 块的武器管理器需要并应能够访问 TAR 或 TTR：

```txt
engagement_settings ew_targets false tar_targets true ttr_targets true end_engagement_settings 
```