# Go To Line

GoToLine 功能提供了一种将光标跳转到指定行的方法。此功能也可以在编辑菜单中找到或通过快捷键使用。

# Auto Complete

AutoComplete 功能为用户在完成命令时提供指导。它会在可能的情况下自动建议已知的值和类型。此功能可以通过编辑菜单或使用快捷键组合 Ctrl+Space 来使用。

# Comment/Uncomment Selection

Comment and Uncomment Selection 功能允许用户将当前选定的文本行放入或移出注释。第一个示例图显示了一些选定的行，而第二个示例图显示了注释选定内容后的结果。此功能可以在编辑菜单中找到或通过快捷键使用。

![](images/af69b2a4a78efe77579f6b5290c437b7be8941c41ba988ee82db60e3a8ad75d3.jpg)

上面是注释前

![](images/300774108e2ef5905c27ea8e604783ecac4b50c7fb62d6d03e24556a04316119.jpg)

上面是注释后。

# 5.1.2.3.3.9. 扩展工具 External Tools - Wizard

External Tools 选项可以通过 Options 菜单中的首选项对话框访问，用于管理 Wizard 已知的所有外部工具。

添加新工具：点击“+”按钮，然后浏览到工具的位置。工具将被添加到顶部列表中，工具的相关信息会在底部填充。

移除工具：只需点击“-”按钮即可。

对话框底部的字段包含以下信息：

Path：工具的绝对路径。  
Alias：给这个工具指定的名称，用于在菜单中引用此工具。  
CommandLineArguments：执行工具时传递的命令行文本。可以配置为固定文本，或包含在工具启动时扩展的变量的文本。点击“Variables”可以获取可用变量的列表。  
Working Directory：工具所见的“当前目录”。  
AssociatedFileTypes：一个以空格分隔的文件扩展名列表，这些扩展名可以用此工具打开。这些扩展名用于在项目浏览器中右键单击文件项时填充上下文菜单。  
Configure CME Tools：可以通过将 VESPA 可执行文件添加为外部工具来快速配置 VESPA、Timeview、GRIT 和 Plotview。

![](images/4c8f5ee4c1ffc9df12e6ef5874d103a923d1c2aca52860e87413696063522a21.jpg)

# 5.1.2.3.3.10. 视频捕捉 Video Capture - Wizard

视频和屏幕捕获功能可以在 Tools 菜单中找到，或者可以随时使用它们的快捷键序列执行（默认情况下，视频捕获是 Ctrl-Shift-V，屏幕截图是 Ctrl-Shift-S）。

![](images/b6d9a58ed57103bc35a4077df8ffad07e0b4786ee4e0c98206d1c361ebcb35b8.jpg)

视频和屏幕捕获功能可以在 Tools 菜单中找到，或者可以随时使用它们的快捷键序列执行（默认情况下，视频捕获是 Ctrl-Shift-V，屏幕截图是 Ctrl-Shift-S）。

# 5.1.2.3.3.11. 推演管理 Simulation Manager - Wizard

SimulationManager 可以通过 Options 菜单中的首选项对话框或运行工具栏上的模拟名称访问。这个工具允许你监控多个模拟的进程，无论是串行还是并行运行。你可以查看每次

运行的详细信息，例如参数、已用时间和诊断信息。SimulationManager 还提供了分析和比较记录信号结果的选项。

![](images/ff10dd4d8964bf1aa3f9b1bc867801a14a9a53473c57e26b04a6a58feffbbf2a.jpg)

# Sim Execution

Wizard 会自动填充其发布中的模拟，如果需要其他模拟，必须首先在此处添加。添加模拟应用程序可以让你从 Wizard运行它们，并利用该应用程序和版本允许的输入语法。

添加新应用程序：点击“Add”按钮，然后浏览到可执行文件（在 Windows 上为.exe）。应用程序的信息将被生成，并添加到列表中。  
移除应用程序：只需点击“Remove”按钮即可。

将鼠标悬停在应用程序上会显示其路径。选定的应用程序将用于在 Wizard中执行。

如上所述，Simulation Manager 也可以通过点击运行工具栏上的 WIZARD_EXE_TOOLBAR访问。

新项目将使用选定的默认应用程序。  
现有项目将覆盖此设置，并使用.afproj文件中保存的设置。

如果应用程序支持分析，通过设置“ProfilingOutputPath”可以启用性能分析。如果与调试结合使用，分析结果将不准确。默认应用程序配置禁用了分析。用户可以手动添加这些应用程序的其他实例以使用分析。

可以在“Extra arguments”设置中添加特定于应用程序的额外命令行参数。

# Output Window

当模拟正在执行时，结果会显示在主窗口底部的 Output Window 中。可以通过 Options菜单中的首选项对话框更改 OutputWindow 中显示文本的字体大小。

![](images/a90b5d0fdea8ef60f3996a7d0de97b6ef898d21801bb3364f8edf42f0815efb8.jpg)

# 5.1.2.3.3.12. 地图悬停信息 Map Hover Information - Wizard

在向导中，地图悬停信息插件负责在使用光标悬停在地图显示中的平台和轨迹上时显示工具提示。这个功能通过在地图上提供额外的信息来增强用户交互，而不会使显示变得杂乱。工具提示是一种常见的方法，用于以用户友好的方式提供额外的细节，因为它们只在需要时出现，例如当悬停在特定区域或项目上时。

这一功能类似于其他工具提示实现，当悬停在某个特征上时，会触发工具提示以显示相关信息。根据上下文和应用程序的具体需求，工具提示可以配置为显示各种类型的数据。

![](images/ccb1521e16cf4f1c0d75ad8746d35958b9aae3302a27340fe33e4b46f361b429.jpg)

地图悬停信息首选项

地图悬停信息首选项提供了一个界面，用于自定义地图悬停工具提示显示的数据。用户可以根据自己的需求选择和配置要在工具提示中显示的信息类型。这种自定义功能允许用户在悬停时查看更相关和有用的信息，从而提高用户体验。

通过调整这些首选项，用户可以决定哪些数据字段在悬停时可见，例如平台名称、轨迹细节或其他相关信息。这种灵活性使得工具提示不仅仅是一个简单的显示工具，而是一个可以根据用户需求进行调整的动态信息窗口。

![](images/9ac3b04634627047da80aa086c96f0a2f0bb27b866d22abfbab57c38ba4f5310.jpg)

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

# 5.1.2.3.3.13. 路由浏览 Route Browser - Wizard

RouteBrowser 显示所选平台的路线以及场景中定义的所有全局路线。

应用更改：一旦点击 Apply 或 OK，对路线的更改将立即应用到它们所在的 AFSIM 脚本文件中。  
启用方法：可以从 ‘View’ 菜单启用 RouteBrowser。选择一个平台后，如果该平台有路线，其路线将显示在 RouteBrowser 中。  
选择路线：如果在 PlatformOptions 中启用了路线，可以通过在地图显示中点击其一个航点来选择路线。选择路线后，RouteBrowser 将填充该路线的信息。

![](images/68c65fbd02e3a02d436cb94066aa59ae86e46e25e2400bb3b6fa337213d052f8.jpg)

![](images/372ac78ae108dc38cb9afde6aa8b334cd066525a48418d5d3719543115e827a2.jpg)

用户可以通过以下方式编辑或创建路线：

编辑路线：用户可以通过选择一条路线，然后点击浏览器顶部的 “EditRoute” 按钮，或者右键点击路线并从菜单中选择编辑选项来编辑路线。这将显示一个对话框，用户可以在其中修改每个航点的属性。航点也可以被添加到路线中或从路线中移除。  
添加航点：要添加航点，可以在对话框左侧右键点击所需的相邻航点，并从菜单中选择“Insert Waypoint Prior” 或 “Insert Waypoint After”。航点也可以使用对话框顶部的locationselectorbutton 添加。这样用户可以在地图显示上选择一个位置，并将具有该纬度/经度的航点附加到路线中。新航点的高度默认为前一个航点的高度，如果没有可用的前一个高度，则默认为 25000 英尺。  
删除航点：要删除航点，从同一菜单中选择 “RemoveWaypoint”。

所有其他航点属性设置为 MoverDefault 或保持未设置状态，视情况而定。

![](images/42baa979e1695c3bd4f69e28fad1234dfa66843d60ef0c97698e957d05e15d0c.jpg)

![](images/28af1cdb28f40f49a41a517c0b8e5c86295a2eb9a02975719becc417e9f4d0d0.jpg)

Waypoint Properties 在 Route Browser 中与以下属性相关：

Label：在地图显示中出现在航点旁边的标签。这也用作 goto 命令的目标。  
Latitude：航点的纬度位置。  
Longitude：航点的经度位置。  
Altitude：航点的高度。如果未指定高度，将使用前一个航点的高度。  
Altitude Reference：高度的参考。此属性的选项包括 MSL、AGL 和 Mover Default。  
GoTo：下一步要去的航点的标签。此属性的选项包括为当前路线定义的所有航点标签。  
Speed：航点的速度。如果未指定速度，将使用前一个航点的速度。  
ClimbRate：航点的爬升率。如果未指定爬升率，将使用前一个航点的爬升率。  
LinearAcceleration：航点的线性加速度。如果未指定线性加速度，将使用前一个航点的线性加速度。  
RadialAcceleration：航点的径向加速度。如果未指定径向加速度，将使用前一个航点的径向加速度。径向加速度可以通过三种方式之一指定：径向加速度、倾斜角或最大 g 值。可以从下拉列表中选择所需的径向加速度规格。  
Turn Direction：航点的转向方向。此属性的选项包括 Left、Right 和 Shortest。  
Switch Type：航点的切换类型。此属性的选项包括 On Passing、On Approach 和 MoverDefault。  
EndOfPathOption：指定平台到达其路线的最后一个航点时会发生什么的属性。选项包括 Extrapolate、Stop、Remove 和 Mover Default。

在编辑路线时，对航点的任何更改将立即反映在地图显示中（如果启用了路线）。然而，要在模拟中生效，必须通过点击 “Apply” 或 “OK” 来应用更改。

Note：路线更改在点击 “Apply” 或 “OK” 之前不会应用于模拟。

该路线被认为是“全局的”，直到它被分配给一个平台。

可以通过点击 “New Route” 按钮在 RouteBrowser 中创建新路线。将出现一个与编辑对话框非常相似的对话框，此外还有一个 “RouteName” 字段和一个下拉列表，用于在需要时将路线分配给平台。要添加航点，请使用位置选择器在地图显示上选择位置。一旦添加了至少一个航点，可以通过右键点击航点，然后选择 “InsertWaypointPrior” 或 “InsertWaypointAfter” 来添加其他航点。可以通过选择 “Remove Waypoint” 选项来移除航点。

一旦创建了全局路线，可以从平台移动窗口的 “FollowRoute” 部分的下拉列表中选

择它。

![](images/0adc0133f637a3190a2a28a3b73cc9d42c015a3f4f8c4c2e09d81ed9058b1d34.jpg)

这样可以轻松管理和清理不再需要的路线。

# Platform Options

通过平台选项，可以在地图显示中显示或隐藏路线。

在这段话中，“PlatformOptions”指的是一个设置选项，用户可以通过这个选项来控制地图上路线的显示状态。具体来说，用户可以选择让路线在地图上可见或不可见。这种功能通常用于简化地图视图，帮助用户专注于其他重要信息。

![](images/48df7d758934a4dad65e306b5826409c1513cb9153c1c4b3163ff621777c2af5.jpg)

# Preferences

偏好设置中有选项可以设置和切换使用默认路线名称，设置和切换使用默认航点标签，

以及一个切换选项来在地图上显示或隐藏全局路线。

在这段话中，“Preferences”指的是用户可以自定义的一组设置。用户可以通过这些设置来控制以下功能：

默认路线名称：用户可以选择是否使用系统提供的默认名称来命名路线。  
默认航点标签：用户可以选择是否使用默认标签来标记航点。  
全局路线显示：用户可以选择在地图上显示或隐藏所有的全局路线。

# 5.1.2.3.3.14. 地图展示 Map Display - Wizard

地图显示对话框展示了世界地图以及用户选择在地图上显示的平台、轨迹和其他元素。

# 地图导航方法

左键单击并拖动：用鼠标光标“拉动”地图。  
鼠标滚轮：以鼠标光标为中心放大或缩小地图。  
双击左键：将地图放大到鼠标光标处。  
中键单击并拖动：倾斜和旋转视图。  
方向键：移动地图。  
Home 键：将地图重置到以场景为中心。

# 平台选择

可以通过左键单击选择平台。

# 信息提示

当鼠标光标悬停在许多屏幕元素上时，会弹出额外的信息。

# 右键菜单

右键单击地图将打开地图的上下文菜单。您还可以右键单击平台以打开平台的上下文菜单。

# 平台标签选项 Platform Label Option

可以通过平台选项对话框应用显示平台名称的标签。

![](images/4756313d649f099cc7df34bd7fdc4679716ba4db29b4028c2fe5e394c17fa56a.jpg)  
测量工具 Measure tool

![](images/f3337485b94addefc41ff5739f5841671c8a5b3a8883716b9ee96b7434c78e13.jpg)

可以通过右键单击平台或位置并从菜单中选择测量选项，然后单击另一个平台或位置来进行测量。选择标尺图标将显示选项对话框，取消选择将隐藏它。

draw_compass：沿大圆进行测量。  
icon_ruler：沿直线进行测量。  
icon_compass：显示相对航向。  
distance：显示距离。  
speed：显示接近速度。  
hourglass：显示预计到达时间。  
选择字体大小。  
dest：显示目的地端的指标。  
source：显示源端的指标。

居中功能 Center on

右键单击将提供一个选项，可以将摄像机居中于当前选择的对象或整个场景。

跟随功能 Follow

右键单击平台将提供一个选项，使摄像机跟随该平台。使用鼠标移动摄像机将结束跟随。

偏好设置 Preferences

这些功能允许用户更好地控制视图和摄像机的行为，以便在场景中进行更有效的导航和观察。

![](images/1b3e0bf8b3d62d83ed4743ad23eb463c8a78534d00366722e3ffd3524084be45.jpg)

Map：选择要显示的地图。可以在地图定义中添加地图。  
Brightness, Contrast, Saturation：影响地图的色彩平衡。  
Lighting：启用太阳光照效果。  
ECICamera：在地心地固视图和地心惯性视图之间切换。  
CenteronStart：在启动时将摄像机居中于场景。   
Show Terrain Altitude At Cursor：在状态栏中显示鼠标光标下的地形高度（如果可用）。  
ZoomonMouseCursor：启用时，缩放操作将以鼠标光标为中心；禁用时，将以视图中心为中心。  
DisplayTeamColor：平台图标要么用团队颜色着色，要么抑制颜色。  
Truescale：按比例绘制平台图标。  
Modelscale：在屏幕空间中缩放模型。  
Labelfont：设置应用于平台标签的字体（例如，平台标签）。  
GridLines：启用/禁用纬度和经度线，并选择其颜色。密度子选项更改网格线的密度。  
ElevationLines：当与 TMS 高程数据库关联时，启用地形等高线。  
CoastLines：启用/禁用并选择海岸线的颜色。  
CountryBorders：启用/禁用并选择国家边界的颜色。  
US Internal Borders：启用/禁用并选择美国州边界的颜色。  
LakesandRivers：启用/禁用并选择主要湖泊和河流的颜色。  
Screen-Centered Range Rings：启用/禁用并选择屏幕中心的范围环的颜色。  
Terminator：启用/禁用昼夜分界线的可视化。  
Sub-Solar Point：启用/禁用太阳下点的可视化。   
Sub-Lunar Point：启用/禁用月下点的可视化。  
SolarPath：启用/禁用表示太阳下点在场景中路径的线。  
Scale：启用/禁用比例尺工具。  
Compass：启用/禁用指南针工具。

Tooltips：启用/禁用当鼠标悬停在地图元素上时显示的工具提示。

# 等高线

当与 TMS 高程数据库关联时，可以启用地形等高线。要选择高程数据库，请在“Source”下浏览所需的 TMS 文件。

等高线是地图上用于表示地形高度变化的线条。它们通常用于地形分析和导航，帮助用户理解地形的起伏和特征。通过选择合适的 TMS 文件，用户可以在地图上显示详细的地形等高线，从而更好地进行地形分析和决策。

![](images/13da8cf28228751c462b55967d0efa04177778f2ff8a1b74789afd9a915fe503.jpg)

# 屏幕中心的范围环

启用/禁用屏幕中心的范围环，并选择其颜色。范围环通常用于雷达图像，但也可以用于任何数据。它们在地图投影上居中显示，并可以通过重置纬度-经度或站点来移动。

范围环是地图上的同心圆，用于表示从某个中心点的固定距离。这些环可以帮助用户在地图上直观地理解距离和范围，特别是在分析雷达数据或其他地理信息时。通过自定义颜色和启用/禁用选项，用户可以根据需要调整范围环的显示。

![](images/b29854d38dd041dc97b21fdd904e31ddff5c0156db2fa503db1ed3bd9db412f3.jpg)

Terminator：启用/禁用昼夜分界线的可视化。昼夜分界线是地球上白天和黑夜的分界线。

用户可以更改分界线的线宽和颜色，以便更好地适应地图的显示需求。这一功能有助于用户直观地了解地球上光照条件的变化，特别是在分析与时间相关的地理信息时。

![](images/4ccc735e9e340182a618d703a04f5696e22ab1f51d683eb149bf2e9d07ef3422.jpg)

![](images/0f2ced15f1f6526682b20cafa645c10f4553ce9ecf57694f5ec231453d401231.jpg)

# Sub-Solar Point

Sub-SolarPoint：启用/禁用太阳下点的可视化。太阳下点是地球上太阳正好位于头顶（天顶）的位置，即太阳光线垂直于地球表面的位置。

用户可以更改该点的大小、颜色和图标，以便更好地适应地图的显示需求。这个功能帮助用户直观地了解太阳在地球上的位置变化，特别是在分析与太阳位置相关的地理信息时。

![](images/abb1334253568df4f7e65042c938f07ef8e1a70842d81e0255f24e851ee03a01.jpg)

![](images/83ca75173dc0c85f2905eccfe394b08f68bbcfac08f3e89facd236bb044fb89b.jpg)

# Sub-Solar Point

Sub-SolarPoint：启用/禁用太阳下点的可视化。太阳下点是地球上太阳正好位于头顶（天顶）的位置，即太阳光线垂直于地球表面的位置。

用户可以更改该点的大小、颜色和图标，以便更好地适应地图的显示需求。这个功能帮助用户直观地了解太阳在地球上的位置变化，特别是在分析与太阳位置相关的地理信息时。

![](images/6c5d24c1be0a13b8684ac0caa538c3558081ec48d02a2ddb3fe27e101b567c62.jpg)

SolarPath：启用/禁用表示太阳下点在场景中路径的线。太阳路径线显示了太阳下点在整个场景过程中的移动轨迹。

用户可以更改该线的宽度和颜色，以便更好地适应地图的显示需求。这一功能帮助用户直观地了解太阳在地球上的移动路径，特别是在分析与太阳位置变化相关的地理信息时。

![](images/115d3f7581ffdd01edca31a16d9c41b99a47e8b3aa4c3d6eab6c431c9fd8b699.jpg)

Scale：启用/禁用比例尺工具。

比例尺工具用于在地图上显示距离的比例关系，帮助用户理解地图上的距离与实际距离之间的关系。通过启用比例尺工具，用户可以更准确地进行测量和分析地理信息。

![](images/6c2c03c4db3bbaa40bf82e23a85c209dc1d81f7a79917202f8c04e9ea6fbbce0.jpg)

Compass：启用/禁用指南针工具。

指南针工具在地图上显示方向，帮助用户确定方位和导航。启用指南针工具可以为用户提供地理方向的参考，特别是在需要精确定位或导航时非常有用。

![](images/eebe5b09d8f5931821ec17b5d1ec5eba79866abd3bdf0f62734a351f20d0cea3.jpg)

# 5.1.2.3.3.15. 地形工具 Terrain Tools - Wizard

Line-of-Sight（通视分析）：该工具允许在两个实体之间绘制一条线，以显示何时视线被地形阻挡。应用程序将使用您场景中定义的地形来进行计算。

要创建视线，请右键单击源实体，并从上下文菜单中选择“Line-of-sight”，然后将线绘制到第二个实体。实体可以是平台、轨迹或注释兴趣点。一旦线条完成，它将从源实体开始为绿色，并在与地形相交的点变为红色。视线的计算可能不会立即完成。

这种分析在地理信息系统（GIS）中非常常见，用于确定两个点之间的可见性，揭示沿线哪些部分对观察者是可见的或隐藏的

![](images/2524bd777d49810cd1c91f341a6fbdb01580c86d202ef6f436a62a0160462b41.jpg)

HoveringtheMouse Cursor：将鼠标光标悬停在视线上时，会显示源实体和目标实体之间的地形剖面。地形剖面始终以源实体在左侧，目标实体在右侧绘制。需要注意的是，垂直比例不会与水平比例匹配。

这种功能允许用户直观地查看两个点之间的地形变化，帮助分析视线是否被地形阻挡，以及在哪些位置发生阻挡。这对于规划和分析地形相关的任务非常有用，例如军事应用、通信塔选址等。

![](images/bb4f5ee01cfe6d61447d8bab4075a50220bfa61c0db6d8d650af960ada69e9f8.jpg)

# Line-of-Sight Options

Right-ClickOptions: 通过右键单击视线，可以设置源实体的桅杆高度。这将为计算增加提供的长度到源实体的高度。此外，还有一个选项可以绘制视线相对于地形的高度。  
Mast-HeightAdjustment: 通过设置桅杆高度，用户可以模拟源实体的高度增加，这在需要考虑天线或其他设备安装高度时非常有用。调整桅杆高度可以帮助用户更准确地分析视线是否会被地形阻挡。  
Height Above Terrain Plotting: 这个选项允许用户查看视线在地形之上的高度变化。这对于理解视线在不同地形条件下的表现非常有帮助，特别是在复杂地形中进行通信或监测时。

这些功能增强了视线工具的实用性，使其能够更好地适应不同的应用场景，如通信网络规划和地形分析。

![](images/cae628a391f61112410dfeb51ad8f98bb7fa2f1869e44d424c17e3d24771b9b6.jpg)

Update Button Functionality: 在地形高度图上，更新按钮用于将图更新为视线的最新状态。

Real-TimeUpdates: 通过点击更新按钮，用户可以确保地形高度图反映视线的最新变化。这对于动态调整视线或地形时非常有用，确保用户始终查看的是最新的地形剖面数据。这种功能增强了用户在分析地形和视线时的灵活性和准确性，特别是在需要频繁调整和查看不同视线条件的场景中。

# 5.1.2.3.4. 工具菜单 Tools Menu - Wizard

![](images/5a66e7f97391fb0837e5a6564cbd591614514269b869c8b5642aa8ff4c068ee2.jpg)

# 5.1.2.3.4.1. 星座生成器 Constellation Maker - Wizard

星座生成器 - 向导

星座生成器是一个工具，用于自动生成卫星星座的输入。它能帮助将卫星组织成一系列轨道平面，每个平面包含一定数量的卫星，这些卫星具有相同的轨道，但位于不同的位置（不同的异常值）。

操作模式：

基于对话框的输入生成：

在这种模式下，用户可以直接在星座生成器对话框中输入选项。配置完成后，使用对话框底部的 Constellation 按钮生成包含每个星座成员平台的输入文件。这使得部署预定义的卫星网络变得简单。

基于脚本的输入生成：

通过选择 Advanced 选项，用户可以生成一个脚本文件而不是直接的输入文件。这个脚本可以在执行前进一步自定义，允许更个性化的星座配置。脚本包含注释，提供安全修改的说明，为高级用户提供了调整星座设置的灵活性。

文件管理：

星座生成器生成的文件包含一个注释块，详细说明了用于生成文件的选项。这些注释对于保持一致性非常重要，且不应被修改，因为如果重新运行工具，它们可能会被覆盖。当选择星座生成器时，它会扫描编辑器中的活动文件以查找这个注释块，并将选项加载到对话框中，方便修改现有的星座或生成器。如果活动文件中没有找到这样的注释块，工具将使用最近输入的一组选项。

该工具对于有效设计和管理卫星星座至关重要，特别是在需要在多个轨道平面上协调多个卫星的场景中。

![](images/765d0a5ea547384c8eea9d0a53dafdd7e9b8507271dcef53504a0ea3d610e039.jpg)

星座生成器提供了一套详尽的选项，用于定义卫星星座的细节。以下是主要选项和控件的详细介绍：

选项：

Constellation Name（星座名称）：

指定星座的名称。生成的平台命名遵循格式 <name>_<plane>_<satellite>。例如，名为‘sample’星座的第二平面的第四颗卫星将被命名为‘sample_1_3’。平面和卫星编号从 0 开始。星座名称还会影响生成文件的名称，当您修改此字段时，生成文件的名称会动态更新。

Platform Type（平台类型）：

设置生成卫星的平台类型。平台类型必须包含 WSF_SPACE_MOVER 才能使生成的输入文件正常工作。

Orbit Size（轨道大小）：

使用四种选项之一定义：Altitude（高度）、Semi-major Axis（半长轴）、Period（周期）或 RevolutionsperDay（每日公转次数）。更改输入方法时，会自动将先前的值转换为新方法的等效值。轨道的等效高度必须至少为 100 公里。

Altitude（高度）：设置圆形轨道的近地点和远地点高度。  
□ Semi-majorAxis（半长轴）：设置轨道的半长轴。  
▫ Period（周期）：设置轨道的周期。  
□ Revs.PerDay（每日公转次数）：设置每日公转次数。

Inclination（倾角）：

设置轨道倾角，范围为 0.0 到 180.0 度。

Number of Planes（轨道平面数）：

指定轨道平面的数量，范围为 1 到 360。

Satellites Per Plane（每个平面的卫星数）：

设置每个平面的卫星数量，范围为 1 到 360。

Initial RAAN（初始升交点赤经）：

设置第一个平面的升交点赤经，范围为 0.0 到 360.0 度。

RAANRange（升交点赤经范围）：

定义其余平面分布的范围，从初始升交点赤经值开始测量。必须在 0.0 到 360.0 度之间。

Initial Anomaly（初始近地点角距）：

设置平面上第一颗卫星的近地点角距，范围为 0.0 到 360.0 度。

Anomaly Alias（近地点角距偏移）：

设置一个平面上第一颗卫星相对于前一平面第一颗卫星的偏移，范围为 0.0 到 360.0 度。

File Generation Path（文件生成路径）：

指定生成文件的路径。该路径会随着更改在‘Constellation’和‘Generator’按钮上方动态更新。

控件：

Constellation（生成星座）：

生成星座。生成的输入文件名称显示在此按钮上方。执行此操作不会关闭星座生成器。

Close（关闭）：

关闭星座生成器。

Advanced（高级）：

切换其他选项和控件以进行更多自定义。

Generator（生成器）：

生成一个包含生成星座脚本的输入文件，允许进一步定制。文件名显示在此按钮上方。执行此操作不会关闭星座生成器。

Input Conjunction（输入冲突）：

如果所选参数可能导致星座成员之间发生冲突，界面中将显示警告。

这些选项和控件提供了设计和管理卫星星座的强大框架，确保卫星部署的灵活性和精确性。

![](images/5c41746f41bb5ee624e52142156804e72dd62a89fc7d821c29baee2a2ff65fe6.jpg)

# 5.1.2.3.4.2. 卫星插入工具 Satellite Inserter - Wizard

Satellite Inserter 是 Space Tools 插件的一部分，允许用户将卫星定义插入到场景中，更新卫星的 TwoLineElements(TLEs)，并根据现有的空间平台管理开始时间/日期/纪元。用户可以通过 Tools 菜单中的 SatelliteInserter 访问该工具，或者通过右键单击编辑器并选择“Insert Satellites”来访问。

这个工具对于需要管理复杂卫星场景的用户来说非常重要，提供了一个用户友好的界面来处理卫星数据，并确保场景模拟的准确性。

# Insert Satellites Tab

在 “Insert Satellites” 选项卡中，您可以将可用的卫星插入到场景中。可用的卫星列表位于对话框的下部。点击列的标题可以按升序排序，再次点击则按降序排序。要选择多个项目，可以按住 Ctrl 键并点击所需的行，或者按住 Shift 键并选择最后一个文件以选择一组卫星。按下 $\mathsf { C t r l } + \mathsf { A }$ 将选择所有符合当前筛选条件的卫星。一旦选择了所需的卫星，点击“Insert” 按钮。卫星定义以及任何必要的包含文件将被插入到插入位置的末尾（显示在工具的左下角）。可以通过点击 “…” 按钮更改插入位置。点击插入按钮后，该按钮将被禁用，直到选择新的卫星进行插入。插入位置的文件也将在点击此按钮后打开并显示。您还可以通过右键单击所需的编辑器并选择“InsertSatellites”来更改位置。

注意：只有具有唯一名称的卫星才会被插入。如果场景中已经存在具有相同名称的平台，则该卫星将不会被插入。如果选择插入多个具有相同名称的卫星，则只有第一个卫星会被插入。允许插入具有相同标识符的卫星。如果发生这些情况，将显示警告。

上部包含筛选器列表。要添加筛选器，右键单击表格单元格以对该列应用筛选器。右键

单击筛选器允许用户删除筛选规则或删除所有筛选规则。用户还可以从这里保存或加载筛选器。保存的筛选器将存储在用户偏好中，以便以后应用。

![](images/be2919562d17c7146958c6914224c096fd28dacb99de7c48f06989129b6bab3f.jpg)

# Databases

可用的卫星定义被组织成 JSON 数据库。这些数据库描述了卫星的属性，并用于填充工具。用户可以通过 Options->Preferences 中的 Space Tools 偏好设置，或者点击工具上的“Manage Databases” 按钮来管理自己的 JSON 卫星数据库。

这些数据库提供了一个结构化的方式来存储和访问卫星信息，使用户能够轻松地在场景中插入和管理卫星数据。通过管理这些数据库，用户可以确保他们使用的是最新和最相关的卫星信息，从而提高场景模拟的准确性和有效性。

![](images/e009df67cc363c99574a853d7a3175867a3e824aa98f9c83e253c1831a3cd3ef.jpg)

默认的数据库 satellite.json 和 satcat.json 位于 demos/satellite_demos 目录中。这些数据库指向 demos/satellite_demos/satellites 目录中的定义。数据库 satcat.json 是使用 CelesTrak 的 SATCAT 数据创建的。

数据库格式：

数据库中必须至少包含一个名为 “platforms” 的 JSON 数组。此数组中的每个平台必须至少包括一个平台 “name” 和一个定义所在的 “file” 路径。

其他可以输入的数据包括：

platform_type   
designator   
country   
definition_type   
orbit_type   
constellation   
classification   
norad_catalog_number   
launch_date   
launch_site   
radar_cross_section   
operational_status

注意：“file” 路径必须相对于 JSON 文件的位置。

管理数据库：

要添加数据库，打开 Preferences 并点击 “Space Tools”，或者点击工具左下角的“Manage Databases” 按钮，然后点击 “Add Database”。这将打开一个文件对话框以选择 JSON

文件。选择所需的文件并点击 “Open” 以添加它。您可以勾选或取消勾选任何已添加的数据库以将其添加/移除出表格。点击 “CheckAll” 一次以勾选所有添加的数据库，再次点击以取消勾选所有数据库。勾选所需的数据库后，点击 “OK” 或 “Apply” 以更新表格。

如果在向导打开时更改或删除了数据库，请点击 “UpdateDatabases”。任何已删除的数据库将消失，现有数据库将更新。

要从偏好设置中删除数据库，选择要删除的数据库并点击数据库列表下的 “Delete”。所有选定的项目将被移除。

自动化数据库创建：

为了帮助自动化创建数据库的过程，可以使用位于 tools/misc 目录中的make_satcat_database 和 convert_platforms_to_json 工具。

Database Format   
```json
"platforms": [
    {
        "name": "Platform_Name_1",
        "platform_type": "PLATFORM_TYPE",
        "designator": "YYYYNNNAAA",
        "country": "Country_Name",
        "definition_type": ["nominal" | "tle'],
        "orbit_type": ["LEO" | "MEO" | "HEO" | "GEO'],
        "constellation": "Constellation_Name",
        "classification": "Classification_Level",
        "norad_catalog_number": "NNNN",
        "launch_date": "YYYY-MM-DD",
        "launch_site": "Launch_Site",
        "radar CROSS_section": "NNNN",
        "operational_status": "Operational_Status",
        "file": ".\relative\path\from\JSON\file\to\Platform_Name_1\definition.txt"
    }
] 
```

Update TLEs Tab

![](images/5e06fbdac0e38809158821175d9c910a0f001a76084d0d37afbb66c0e693a1ad.jpg)

要在场景中更新 TLEs，请选择 “UpdateTLEs” 选项卡。在此选项卡中，您可以添加或删除包含 TLE 更新的文件。

添加 TLE 集文件：

点击 “Add TLE Set”。  
选择包含更新 TLEs 的文件，然后点击 “Open” 以添加它们。  
勾选或取消勾选文件以确定哪些文件将用于更新 TLEs。只有勾选的文件会被搜索。  
点击 “Update TLEs” 按钮以更新 TLEs。

注意：TLEs 将根据所有输入文件中最新纪元的 TLE 进行更新。

移除 TLE 集文件：

选择需要移除的文件，然后点击 TLE 集列表下的 “Remove”。所有选定的文件将从列表中移除。

有关 TLEs 的更多信息，请参阅 Two Line Elements。

根据搜索结果，CelesTrak 提供了更新的 TLE 数据格式，用户可以通过查询格式获取最新的 TLE 数据。确保使用最新的 TLE 数据可以提高卫星轨道预测的准确性。

示例：

有平台定义为：

```txt
...   
platform Platform1 WSFPLATFORM   
...   
add mover WSF_SPACE_MOVER   
orbit 136287U 10001A 19093.96307495 -.00000292 00000-0 00000-0 0 9995 236287 1.4396 352.0597 0001920 174.4823 152.2071 1.00274485 33783 end_orbit   
end_mover 
```

```txt
endPLATFORM   
platform Platform2 WSF_PLATFORM   
...   
add mover WSF_SPACE_MOVER orbit 136287U 10001A 19093.96307495-.00000292 00000-0 00000-0 0 9996 236287 1.4396 352.0597 0001920 174.4823 152.2071 1.00274485 33783 end_orbit   
end_mover   
...   
endPLATFORM   
platform Platform3 WSF_PLATFORM   
...   
add mover WSF_SPACE_MOVER orbit 136828U 10036A 19093.49771867-.00000164 00000-0 10000-3 0 9994 236828 54.1489 187.1521 0078332 232.7902 69.4191 1.00287084 31827 end_orbit   
end_mover   
...   
endPLATFORM 
```

使用的更新文件为：

```proteindb
BEIDOU 3  
1 36287U 10001A 19093.96307495 -.00000292 00000-0 00000-0 0 9997  
2 36287 1.4396 352.0597 0001920 174.4823 152.2071 1.00274485 33783  
BEIDOU 3_2  
1 36287U 10001A 19092.96307495 -.00000292 00000-0 00000-0 0 9998  
2 00000 0.0000 000.0000 0000000 000.0000 000.0000 0.0000000 00000  
BEIDOU 4  
1 36590U 10024A 19093.44858549 -.00000148 00000-0 0000+0 0 9992  
2 36590 1.5727 36.5332 0002254 40.6874 355.7867 1.00272495 32399  
BEIDOU 5  
1 36828U 10036A 19093.49771867 -.00000164 00000-0 10000-3 0 9994  
2 36828 54.1489 187.1521 0078332 232.7902 69.4191 1.00287084 31827 
```

在这个示例中，Platform1 和 Platform2 将使用 BEIDOU 3 的 TLE 进行更新，而Platform3 将使用 BEIDOU 5 的 TLE 进行更新。这样做的结果是：

Platform1 和 Platform2 将反映 BEIDOU 3 的最新轨道数据。  
Platform3 将反映 BEIDOU 5 的最新轨道数据。

```txt
... platform Platform1 WSFPLATFORM 
```

```txt
...   
add mover WSF_SPACE_MOVER   
orbit BEIDOU 3 136287U 10001A 19093.96307495-.00000292 00000-0 00000-0 0 9997 236287 1.4396 352.0597 0001920 174.4823 152.2071 1.00274485 33783 end_orbit   
end_mover   
...   
endPLATFORM   
platform Platform2 WSF PLATFORM   
...   
add mover WSF_SPACE_MOVER   
orbit BEIDOU 3 136287U 10001A 19093.96307495-.00000292 00000-0 00000-0 0 9997 236287 1.4396 352.05 97 0001920 174.4823 152.2071 1.00274485 33783 end_orbit   
end_mover   
...   
endPLATFORM   
platform Platform3 WSF PLATFORM   
...   
add mover WSF_SPACE_MOVER   
orbit BEIDOU 5 136828U 10036A 19093.49771867-.00000164 00000-0 10000-3 0 9994 236828 54.1489 187.1521 0078332 232.7902 69.4191 1.00287084 31827 end_orbit   
end_mover   
...   
endPlatform 
```

Edit Start Time Tab

![](images/c7c030394af0e39e657e4ec0070e0f7860af3e07d823552afb2ed8372d7c9f7a.jpg)

编辑开始时间

“EditStartTime” 选项卡提供了根据现有空间平台更新场景开始时间的功能。您可以手动编辑时间、日期或纪元，或者从以下选项中选择：当前场景时间、最新纪元或当前时间（UTC时区）。更改时间或日期将更新纪元，反之亦然。选择“StartDate”编辑框的箭头会打开一个日历，供用户点击选择所需日期。

最新纪元选项：选择场景中定义的所有空间平台的最新纪元。空间平台的默认纪元是2003 年 6 月 1 日 12:00:00。如果场景中没有现有的空间平台，选择此选项将默认为当前世界时间（UTC）或当前场景时间，以较晚者为准。

更新开始时间：一旦设置了时间，点击 “Update Start Time” 将移除所有未注释的“start_time”、“start_date”、“start_epoch”和“start_time_now”实例。然后，新开始日期和时间将被添加到第一个启动文件的末尾。选择“SetAsEpoch”选项将添加开始纪元而不是日期和时间。工具还会添加一个注释，显示之前的开始日期和时间。

# 5.1.2.3.4.3. 表数据显示工具 Table Plotter - Wizard

TablePlotter 是一种用于可视化 TableValues 数据的工具。它通过将数据以表格形式展示，帮助用户更直观地理解和分析数据。

![](images/921c16a2bb38c3f99598cfde5d6d4ece8e7ea06eaccf4d2d2ef3a9e684c7aad8.jpg)

访问 Table Plotter

Table Plotter 可以通过两种方式访问：

右键菜单：在 TableCommands 或 “file” 命令上右键单击，会弹出一个上下文菜单，其

中包含绘制相关数据的选项。这种方法允许用户快速访问和可视化特定命令的数据。

工具菜单：通过 Tools 菜单打开一个空的 TablePlotter 对话框，用户可以在其中提供一个 AFSIM 表文件或 CSV 文件来绘制数据。这种方法适用于用户希望从外部文件导入数据进行可视化的情况。

# 功能和设置

基本数据显示设置：TablePlotter 提供了基本的数据显示设置，例如修改轴的限制和选择要显示的数据集。  
上下文菜单功能：在绘图视图中右键单击会打开一个上下文菜单，提供导出数据、切换视图（在绘图和表格数据之间）以及显示图例的选项。这些功能使用户能够更灵活地管理和展示数据。

通过这些功能，TablePlotter 为用户提供了一个强大的工具来可视化和分析数据，支持多种数据格式和交互方式。

# 5.1.2.3.4.4. 模型查看工具 Model Viewer - Wizard

模型查看器位于工具菜单下，允许用户操作模型列表。用户可以通过左上角的菜单查看现有模型，或者使用右上角的按钮加载新模型。

![](images/e8686dcc686d35576b2e2a5d2acdd9ce6abe99ca14a8f0d57b7044f6f3f00edb.jpg)

底部的 grid 选项允许用户调整 camera，以及 grid 的位置和方向。

定义编辑区域允许用户对用户添加的模型进行更改。通过按下预览按钮，可以确认更改的有效性并进行预览，然后通过应用按钮将更改写入 sitemodels.txt 文件。

模型定义在 Model Definitions 中描述。

模型图表选项卡允许用户探索模型文件的内容。

# 模型定义 Model Definitions

用户可以将自己的模型添加到应用程序提供的集合中。

要做到这一点：

1) 从 AFSIM 安装目录中，添加一个目录：install_dir/resources/site。  
2) 在 site 目录中创建一个 models.txt 文件。  
3) 在 models.txt 文件中创建对您模型的引用。

models.txt文件包含两种类型的条目：

alias：为模型定义关联一个附加名称。  
model：创建一个模型定义。

模型

模型在块中定义，如下所示：

```txt
model *model_name*  
filename *file*  
set *set*  
default_set  
pre_xform  
scale *s_value*  
translate *t_value*  
rotate *[x,y,z] * r_value*  
end_pre_xform  
screen_scale *ss_value*  
wing_tip *wx_value* *wy_value* *wz_value*  
engine  
position *wx_value* *wy_value* *wz_value*  
diameter *d_value*  
end ENGINE  
billboard  
articulation *visual_part_name* *node_name*  
end_model 
```

模型定义将被命名为 model_name，并且在应用程序中具有此图标名称的模型将与此模型一起显示。

模型文件通过 file 引用。此文件可以是 ive、osgb、openflight、obj 或任何 OpenSceneGraph本地支持的模型格式。该文件也可以是 OpenSceneGraph支持的图像文件。

其余输入是可选的。

set 命令将模型添加到一个集合中。如果模型集合是“immersive”，则模型将在沉浸式视图中代替默认模型使用。如果没有给出集合，模型将被添加到默认模型集合中。  
default_set 命令将模型添加到 default_set 中。default_set 用于地图视图，并在“immersive”集合中没有给定名称的模型时用于沉浸式视图。  
pre_xform 将在模型显示之前应用提供的变换。通常，最好在建模软件中将这些变换应

用于您的模型几何体，而不是使用 pre_xform 块。pre_xform 块可以根据需要以任何顺序采用三种变换中的任意数量。

screen_scale 的 ss_value 将使模型的缩放图标变大或变小。应用程序会自动缩放图标以尝试创建所有图标的统一性，ss_value会改变这种行为。  
wing_tip 命令允许用户定义翼尖的位置。应用程序假定另一个翼尖在 y 轴上反射。  
engine 命令允许用户定义引擎排气口的位置和直径。可以定义多个引擎。  
billboard将使模型成为广告牌，这意味着模型将始终朝向相机旋转。  
articulation 允许将模拟的 visual_part 运动映射到 3D 模型场景图中的一个节点。可以从模型查看器中查看模型的场景图。模型图中的任何节点都是可以接受的，但运动应用于节点的局部坐标系，如果没有正确变换，可能不会按预期移动。

别名

别名格式如下：

```txt
alias *alias_name* *model_name* 
```

其中 alias_name 是用户可以与 model_name 定义关联的新名称。

# 5.1.2.3.4.5. 交战向导 ENGAGE - Wizard

ENGAGE 向导是一个用于创建通用 ENGAGE 场景的工具。在向导中输入的各种字段的值将用于生成一个文件，该文件可以直接由与 AFSIM构建的 ENGAGE 可执行文件（参见：5.6.3交战工具 engage）使用，或者通过添加到模拟管理器中的 ENGAGE 可执行文件直接通过向导使用。在未来的版本中，生成的场景将自动加载到向导环境中以供进一步使用。

场景设置

文件路径设置

根目录：如果指定，向导将使用此位置在根目录位置查找预定义类型。当前支持的类型在其自己的目录结构中包括：

▫ 发射器（ROOTlaunchers）  
跟踪器（ROOTtrackers）  
□ 目标平台（ROOTtargets）  
武器（ROOTweapons）

# 模拟设置

线程数：请求在执行多次运行时使用的线程数。将此值设置为 1 时，串行执行运行。将值设置为 0 将根据处理器核心的数量利用线程数，以提供通常良好的性能。此值不能超过场景输入中所需的实际任务数，超过时将默认线程数为任务数。  
随机种子：用于初始化伪随机数生成器的整数值。  
帧时间：模拟中步骤之间的时间增量。  
结束时间：允许每个任务运行的时间量，然后终止。请注意，如果此值不够长，任务可能会在武器交战进行中终止，可能导致结果不正确。过长的运行时间可能导致在武器未交战的运行中性能不佳，因为不产生主动武器交战的任务将继续运行到指定的时间。

# 事件输出

时间格式：时间输出的格式。目前未使用。

纬度/经度格式：纬度/经度值输出的格式。目前未使用。  
在消息中打印轨迹：选择此值以在事件输出中包含目标轨迹数据。  
事件表：此表保存将在任务运行期间跟踪的事件。如果启用，这些值将被写入事件输出。当前支持以下事件：

▫ SENSOR_DETECTION_ATTEMPT   
▫ SENSOR_DETECTION_CHANGED   
▫ SENSOR_FREQUENCY_CHANGED   
▫ SENSOR_MODE_ACTIVATED   
□ SENSOR_MODE_DEACTIVATED   
▫ SENSOR_NON_OPERATIONAL  
▫ SENSOR_OPERATIONAL  
□ SENSOR_REQUEST_CANCELED   
▫ SENSOR_REQUEST_INITIATED   
▫ SENSOR_REQUEST_UPDATED   
▫ SENSOR_TRACK_COASTED   
▫ SENSOR_TRACK_DROPPED   
▫ SENSOR_TRACK_INITIATED   
▫ SENSOR_TRACK_UPDATED   
□ SENSOR_TURNED_OFF   
▫ SENSOR_TURNED_ON   
▫ SIMULATION COMPLETE   
□ WEAPON_FIRE_ABORTED   
□ WEAPON_FIRE_REQUESTED   
□ WEAPON_FIRED   
▫ WEAPON_HIT   
□ WEAPON_KILLED   
□ WEAPON_MISSED   
WEAPON_TERMINATED

输出率：此表定义用于生成事件输出的速率。表中的每个条目指的是单独的输出文件。点击添加将打开输出率对话框，在其中指定特定速率集的名称，并通过点击添加按钮输入值。

输出率对话框中的条目由开始时间和速率输出的周期（频率）指定。除非在表中指定了其他时间，否则此速率将保持用于输出生成，在此时，新列出的速率将决定输出生成。没有指定周期或值小于或等于零的时间表条目将终止超出列出时间的任何额外输出。

# Run Information

# Center Location

默认情况下，站点或目标网格运行的起始位置是 $0 ^ { \circ }$ 纬度和 $0 ^ { \circ }$ 经度，即所谓的“NullIsland”。如果选择，可以为网格的中心选择一个替代位置。对于目标网格，此值将指定目标的初始位置。对于站点网格（目前不支持），此值将指定站点的初始位置。

# Site Laydown

站点特性可以在 sitelaydowntable中指定。通过设置根目录解析的预定义类型将自动填

充在此处。选择的那些将在生成场景文件时使用。

# Custom Laydown

可以在此处指定单个自定义站点位置。填充到各个字段中的值将用于场景中的单次运行。可以指定多个位置，每个位置都会在 ENGAGE 场景中产生一个新的单对单运行。

# Grid

根据用户设置的站点网格特性确定总体运行次数。站点被放置在中心位置，每个目标实例化导致该运行中单个站点和目标之间的单独交战。生成额外的运行，直到满足所有变量组合。可以使用 downrange、crossrange 和目标高度值，最后一个字段“by:”确定“from:”到“to”字段中两个值之间等距离步长的粒度。速度在所有运行中保持不变。支持负值的crossrange和 downrange值分别表示站点在目标后面或目标左侧的位置。请注意，使用站点网格布局时，目标高度和目标速度值显然是目标的设置，而不是站点的。因此，当定义站点网格时，其他形式的可能目标布局输入被禁用且无效（目前）。

# Target Laydown

目标特性可以在 targetlaydowntable中指定。通过设置根目录解析的预定义类型将自动填充在此处。选择的那些将在生成场景文件时使用。

# Target Behavior

允许选择目标在 ENGAGE 运行中的实例化方式。

# Grid

根据用户设置的目标网格特性确定总体运行次数。目标被放置在中心位置，每个站点实例化导致该运行中单个站点和目标之间的单独交战。生成额外的运行，直到满足所有变量组合。可以使用 downrange、crossrange 和高度值，最后一个字段“by:”确定“from:”到“to”字段中两个值之间等距离步长的粒度。速度在所有运行中保持不变。支持负值的 crossrange和 downrange值分别表示站点在目标后面或目标左侧的位置。

# Simple Path

允许用户定义目标将采取的简单路径。x、y和 z值是目标相对于中心点的起始位置。目标将从此位置以指定的速度和航向移动。

# Flight Path

可以通过为目标添加航路点来定义更具体的飞行路径，为表中指定的字段提供值。

# Flight Route

类似于飞行路径，但选项较少，复杂性较低。

# Use Target Path

使用目标类型定义的路径，而不是上述方法。

# Repetition Count

根据用户提供的 crossrange、downrange和高度值，需要特定数量的唯一运行来覆盖这些值的所有组合。如果需要，可以通过更改重复计数来多次运行这些唯一组合中的每一个。

Perform Flyouts

指定是否在运行中进行武器飞行。

Generate Record File

指定是否生成记录文件。

Generate Event File

指定是否创建事件文件。

# Output

此表定义可以从运行时条件创建的可变输出文件。点击添加输出时，会提示提供保存数据的文件名，以及变量名、输出变量的阶段、单位和格式。对于每个变量文件，如果需要，可以通过选择适当的复选框将事件和摘要输出附加到每个文件。当前支持的变量包括：

1 time   
target_x   
target_y   
target_z   
target_vx   
target_vy   
target_vz   
target_ax   
target_ay   
target_az   
weapon_flight_time   
weapon_x   
weapon_y   
weapon_z   
■ weapon_vx   
weapon_vy   
weapon_vz   
weapon_ax   
weapon_ay   
weapon_az   
weapon_speed   
weapon_mach   
weapon_gee_force   
weapon_to_target_range   
Pk Table Generation   
此表确定用于从站点网格运行生成 Pktables 的设置（如果需要）。请注意，必须定义站点网格才能生成 Pktable输出，否则输入将被禁用。  
Enable Pk Table Generation：选择是否从站点网格数据生成 Pk tables。  
Table Site Name：设置将在 Pk table 输出中用于标识站点的名称。  
Table Target Name：设置将在 Pk table 输出中用于标识目标的名称。

OutputPath：点击文件对话按钮将允许指示和选择一个目录，在所有模拟运行完成后将Pktable数据写入该目录。  
Enable Periodic Flush：启用在模拟运行期间写入 Pk table 数据，而不是默认的（在完成时）。  
Output Length Units：选择将在生成的 Pk table 值中使用的长度单位。  
Output Speed Units：选择将在生成的 Pk table 值中使用的速度单位。

# 5.1.2.3.5. 开发菜单 Developer Menu - Wizard

![](images/58f3eeb180dab90c8ed8ddda16ee7c19b03369d3900c213995f5236752bc2671.jpg)

在 developermenu 中，可以通过 preferences 启用此功能。然而，除非您是开发人员，否则不建议使用 developermenu，因为稳定性无法保证。

DocumentMemoryUsage：报告文档使用的内存量。这对于开发人员监控和优化内存使用非常有用。  
ObjectMode：切换到对象编辑模式，这将锁定文本编辑，直到用户返回到文本编辑模式。这有助于专注于对象操作而不受文本编辑的干扰。  
ParseTreeDump：将解析树的内容转储到对话框中。这对于调试和理解解析数据的结构非常有用。  
ProxyDump：类似于解析树转储，此功能将代理（对象）树的内容转储到对话框中。它有助于检查应用程序中代理对象的状态和结构。  
WatchProxy：允许用户设置对代理值的监视。这对于在应用程序运行时跟踪特定代理值的变化非常有用。

这些功能主要是为需要调试或优化其应用程序的开发人员设计的。如果您不是开发人员，建议避免使用 developer menu 以防止潜在的不稳定问题。

![](images/d8dcd2eebb4b6479f2e5e970fdfc529acddccad698d219ffbe8835828a538e6c.jpg)

Parser/Proxy Timers：显示解析器/代理过程的执行时间细分。

▫ Grammar T：WsfParseDefinitions 解析 WsfGrammar 所花费的时间。  
▫ Parse T：WsfParser 解析输入文件所花费的时间。  
□ Deserialize T：WsfPProxyDeserialize 反序列化解析树所花费的时间。  
□ Merge/GUI T：ProxyMerge 合并旧的和新的 WsfPProxys 以及 Wizard 更新其 GUI 所花费的时间。  
□ 注意：这些时间以秒为单位。

Reload Model Database：重新加载所有 models.txt 文件，有效捕获对文件所做的编辑。  
Show Map Window Scene Graph：显示地图显示的场景图。右键单击节点将提供详细信息选项。  
ReloadShaders：重新加载应用程序使用的所有 GLSLshaders。这将捕获对着色器源文件的实时更改。  
Toggle Graphics Stats：切换显示每秒帧数和其他诊断图形显示。  
Toggle Polygon Mode：在填充、线框和顶点之间切换多边形绘制模式。  
Performance Analyzer：显示应用程序使用的内存量。

![](images/499f3c09b6ff6208936a5a21f0f909ee32f0ef5bf41816ec5329fb597a1c5262.jpg)

这些功能主要用于开发人员进行调试和性能优化。如果您不是开发人员，建议避免使用这些功能以防止潜在的不稳定问题。

![](images/aa6b6ddcea8f08c296f0eda18b7b43f25ff258b16c717a03f46f0aef175e712e.jpg)

以下选项适用于当前活动的 text editor，除非另有说明：

Go To Definition：查找光标下文本的定义。  
Find References：查找光标下文本的引用。  
Undo：撤销上一次更改。  
Redo：重做上一次撤销的更改。  
Cut：将高亮文本剪切到操作系统剪贴板。  
Copy：将高亮文本复制到操作系统剪贴板。  
Paste：从操作系统剪贴板粘贴到光标位置。  
SelectAll：选择文档的全部内容。  
Find…：输入并查找文本片段。  
FindNext：查找上次输入文本的下一个实例。  
FindPrevious：查找上次输入文本的上一个实例。  
FindinFiles：在每个项目文件中查找文本片段的所有实例。  
Replace…：用新文本片段替换旧文本片段。  
GoToLine…：将光标跳转到选定行。  
Back：将光标移回到先前的位置。  
Forward：将光标向前移动到从“Back”移动的先前位置。  
Auto-Complete：尝试完成光标下的文本片段。  
Comment Selection：注释选定的文本块。  
Uncomment Selection：取消注释选定的文本块。  
Toggle Selection Comment：根据当前状态注释或取消注释选定的文本块。  
Format Selection：尝试格式化当前选定的文本块。请注意，这是根据 preferences 中描述的缩进规则完成的。

# 5.1.2.3.7. 项目菜单 Project Menu - Wizard

![](images/45d1848bd8921a5cf91d22b18c548d5142aedc39d7c63811c0e54dc6194c1af6.jpg)

AddDirectorytoProject…：将新目录添加到项目中。这通常用于在项目中包含新的文件夹结构或资源。  
ChangeHistory：显示更改历史对话框。这可以帮助开发人员查看项目的更改记录，类似于版本控制系统中的提交历史。  
Reparse：强制重新解析场景。这对于确保项目中的所有更改都被正确解析和更新非常有用。  
Settings…：显示项目设置对话框。用户可以在此处调整项目的各种配置选项。

![](images/6523eb0d37f3de7ac4c3a70f81164789a856a3cb26ce7f58520b99e8b45763ef.jpg)

在项目管理中，一个项目通常由几个主要项目组成：project directory、working directory、application selection 和 command line options。项目会保存为.afproj 文件，以便以后加载。

# 项目设置

Root Directory: 这是在 Project Browser 中显示的顶级目录。它是项目的主要目录，包含所有相关文件和资源。

WorkingDirectory: 这是场景执行的目录，并且是引用包含路径的目录（如果与根目录不同）。它用于运行场景并处理相关文件。

Command Line: 执行场景时给出的命令行。$(SCENARIO_FILES)将被场景中的主文件集替换。选择“Configure Startup”可以配置启动选项。

# 项目保存注意事项

如果通过将根场景文件拖放到 WizardMain Window 上打开项目，则必须在 File 菜单中选择 SaveProject，否则在打开另一个项目或退出应用程序时，所有项目设置将丢失。

# 项目设置对话框

项目设置对话框可以从项目中访问。该对话框提供了更改以下设置的接口：

Root Directory: 项目浏览器中显示的顶级目录。

Working Directory: 场景执行的目录。

Command Line: 执行场景时使用的命令行。

这些设置帮助开发人员有效地组织和管理项目文件，确保项目的顺利运行和维护。

# 5.1.2.3.8. 运行菜单 Run Menu - Wizard

![](images/294aa495b6ac22055b17a9eab06977369e1404034a04e62eab19a13ca5356ec0.jpg)

Run：执行活动模拟中的场景。这是运行场景的标准模式。  
RunDebug：使用脚本调试器执行活动模拟中的场景。这允许开发人员在调试模式下运行场景，以便更好地分析和解决问题。  
ToggleBreakpoint：在当前活动的脚本行上添加或移除断点。断点是调试过程中用于暂停程序执行的标记。  
DeleteAllBreakpoints：从场景中移除所有断点。这可以快速清除所有设置的断点。  
DisableAllBreakpoints：禁用场景中的所有断点，而不删除它们。这允许暂时忽略断点而不丢失它们的位置。  
DebuggerSettings…：显示调试器设置对话框，用户可以在其中调整调试器的配置。

# 5.1.2.3.9. 脚本调试 Script Debugger - Wizard

WizardScript Debugger 是一个用于调试 WSF 脚本的工具，能够在执行 WSF 应用程序时提供调试功能。其主要功能包括：

SettingBreakpoints：可以在代码中设置断点，以便在特定行暂停脚本执行。这有助于检查应用程序在关键点的状态。  
SteppingExecution：调试器允许您逐步执行脚本，包括进入、跳过和退出脚本命令。这使您能够更好地理解执行流程。  
InspectingVariableValues：在脚本暂停时，可以检查变量的值，以了解数据如何被操作，并识别变量值的问题。

# 运行调试模式

如果项目关联了可执行文件，只需从 Run 菜单中点击 RunwithDebugging 即可。这将执行场景，并附加一个配置文件以连接到调试器。要从 Wizard 外部以调试模式启动可执行文件，可以从 Run 菜单中点击 DebuggingSettings。显示的文本可以复制并粘贴到场景文件中。要从其他主机运行，只需更新连接参数以指向运行 Wizard 的机器。

# 断点

断点是暂停脚本执行的代码行。可以通过左键或右键单击文本编辑器的左边距，或按 F9来设置断点。条件断点会在暂停执行前测试某个条件，只有当条件为真时才会暂停。

![](images/8846fc294442438464010d5cc21a09ceb12c78a61ad468856aa55562cd424a0a.jpg)

所 有 断 点 都 显 示 在 “Script Breakpoints” 控 制 中 。 可 以 通 过 点 击 复 选 框 或“Enable-all”/“Disable-all”按钮来暂时禁用或重新启用断点。可以通过选择断点并按下 if 按钮来更改断点条件。

# 执行控制

当 WSF 应用程序连接到 Wizard 时，会显示运行控制。此控制允许您暂停、播放（实时）和快进模拟。在调试模式下，提供了进入、跳过和退出按钮，以便对脚本执行进行原子控制。一旦命中断点，活动行将在文本编辑器中以黄色高亮显示。控制上提供以下按钮：

![](images/e56f800109626c1c021e2ee6f2fdced369dde83bebeba1afbdfce2d00dffe042.jpg)

Pause：暂停模拟（即 Break All）。  
Stop：停止模拟。  
Play：实时播放模拟。  
Fast Forward：快进模拟（非实时）。  
StepInto：运行脚本直到下一个脚本行处于活动状态。这允许进入调用的函数。  
Step Over：运行脚本直到下一个行处于活动状态。  
StepOut：运行脚本直到函数退出。

# 监视变量

![](images/9f9062308cc6727b5bdc5abde5c95382b324184d89cd4a3d53e362d09b5aa002.jpg)

Watch Control 允许检查脚本变量的值。顶级项目包括“Watches”、“Local”和“Global”。

Watches：显示所有用户定义的监视表达式。可以通过左侧的 New Watch 按钮添加新的监视表达式。可以通过双击文本更改每个监视的变量名或表达式。  
Global Variables：可以将任何全局变量名添加到监视中。例如：TIME_NOW  
LocalVariables：可以将活动行的局部变量添加到监视中。可以使用调用堆栈控制来更改哪个函数处于活动状态。例如：aValue

ScriptExpressions：可以使用任何结果为值的脚本表达式，包括对脚本和内置函数的调用。例如：TIME_NOW - aValue 或 PLATFORM.MasterTrackList()

此外，还有预填充的 Local 和 Global 条目：

Local：显示当前上下文中的所有局部脚本变量列表。  
Global：显示模拟中的平台列表。可以通过向场景添加脚本来向全局列表添加自定义子项。有关更多信息，请参阅随 Wizard 分发的 wsf_debug_scripts.txt。

调用堆栈

CallStack 提供在命中断点时查看脚本调用堆栈的功能。这有助于了解函数调用的顺序和上下文。

![](images/eb04ff162e3b90188dc36864fbdd670b2e84b4fcadd46faaded1be120a1e0805.jpg)
