![](images/c4074fdf68363bc5ccb13bb6ad25344444d24e03a247f73eb127324baba270c1.jpg)

概述

显示器由中心的 HUD 和其下方的简单前置控制（UFC）显示组成。

HUD 的顶部提供了一个水平航向带，当前航向（度）显示在带的中心框中。

HUD 的左侧显示地速（节）、校准空速（节）、迎角（alpha，度）、马赫数、当前过载和可用过载。它还包括 HUD 模式（如 NAV）以及箔条和照明弹消耗对策的计数。

HUD 的右侧显示垂直速度（英尺/分钟）、气压高度（英尺）、雷达高度（英尺），以及航路点信息，包括航路点编号、航向、航路点距离（海里）和到达航路点的时间（小时:分钟:秒）。它还包括导航模式和飞行员控制信息。

HUD 的底部显示滚动指示器。

中心显示俯仰/滚动梯和速度矢量。

UFC包括左侧的标准化推力指示器。绿色区域表示军用功率（干推力），红色区域表示加力/再热（湿推力）。中心显示质量摘要（所有值以千磅为单位），显示总重、总燃料、内部燃料和外部燃料。

注意：并非所有数据都可能显示，因为某些移动类型不提供所有显示的数据，但所有可用数据将被显示。

偏好设置

从偏好设置中可以设置抬头视图的分辨率。

![](images/2574d5fc6dda775f912e2ddb2cd0ccc75fed6d3500079f508c96c4065235e405.jpg)

![](images/a165da3d1f09563e5bd651c77b6a6883799689717b74bdb1c025eb136fbe92fe.jpg)

![](images/9d77978300e9d2a049237753d933465bb2bd31c987a2f205d9b9e38455fd87ef.jpg)

![](images/abefbd879323378a8b1d2281527b207a161d8207cabe9882e62168d18e2ef2fc.jpg)

# 5.3.2.2.3.6. 场景内消息 Comment - Mystic

Comments 是通过 AFSIM 脚本使用 WsfPlatform.Comment 脚本方法生成的消息。

评论将出现在评论窗口中，并带有指向原始平台的链接。可以从“View”菜单中显示评论窗口。

评论气泡会显示评论消息，并出现在调用脚本方法的平台上方的地图显示上。

![](images/871d137d04ef1f50f9d9352a24a243f1adc6eb6719a78e8c2b0afa4ab24953de.jpg)

![](images/80e8d5a8a83556a387c789ee65b46cac47de4a05b746e5a9b51121a95a22028e.jpg)

# 偏好设置

可以通过“EnableComments”复选框启用/禁用评论。默认情况下，评论是启用的。

“IncludeTimestamp”复选框允许用户控制评论开头是否包含时间戳。默认情况下，时间戳是关闭的。

超时决定评论在地图显示上显示的时间长度（以模拟时间计）。默认时间为 5 秒。

![](images/cf5535ff97c3d8153f68a09f9135b16b80434fd0cce2126b68282dee5a43e8aa.jpg)

# 5.3.2.2.3.7. 平台浏览 Platform Browser - Mystic

平台浏览器对话框显示当前场景中存在的平台列表。浏览器中的项目按团队进行颜色编码。可以通过“View”菜单访问平台浏览器。它可以停靠在主窗口的左侧或右侧停靠区域。浏览器也可以作为一个单独的窗口弹出。

![](images/60a0bfb4e02b4872ad530ef321c5c47984eb2216d6ff50221c6be2db27b3dbae.jpg)

右键单击一个平台将显示平台上下文菜单，用户可以从中执行各种操作，例如添加范围

环、使用测量工具从平台测量到另一个位置、添加装饰以及将屏幕居中于平台。

![](images/df1ab7faeb768d0e0a9b68696689bce64d7f12bf8a8f2d6c88e829da11985d68.jpg)

平台浏览器标题栏在括号中显示当前模拟中存在的平台数量，后跟场景包含的平台总数。默认情况下，浏览器只显示活动平台。在偏好设置中，可以更改为也显示非活动（死亡、移除或尚未初始化）平台。

浏览器顶部的过滤器可用于仅显示特定名称、类型或团队的平台。浏览器中的项目按团队进行颜色编码。

# 偏好设置

![](images/8ee7e3fca34005dceff796c778f1df91dce176787f81df3be310a156d8ed1b7a.jpg)  
ShowInactiveEntities- 如果选中，非活动实体（尚未创建或已销毁的实体）将在浏览器中显示为淡出状态，否则将被隐藏。

# 5.3.2.2.3.8. 录像 Video Capture - Mystic

视频和屏幕捕获功能可以在“Tools”菜单中找到，或者可以随时使用其快捷键序列执行

（默认情况下，视频是 Ctrl-Shift-V，屏幕截图是 Ctrl-Shift-S）。

![](images/d0a7cc99ef79f4b20ca31485793e6b19305be1fbb46f34f61313df203c77c66e.jpg)

偏好设置

偏好设置包括在捕获活动窗口或主窗口之间切换的选项，以及设置输出目录、文件名模板和视频质量的选项。

# 5.3.2.2.3.9. 时间控制 Time Controller - Mystic

![](images/4d91269df6069ada39fcc091cf0c9abaaca02e0f27e289b524ab5d0792d1c33d.jpg)

时间控制器允许用户浏览场景的历史数据。

灰色区域显示当前在内存中的内容。为了保持性能，场景中只有一部分可能被加载。

时间控制器左侧的图标依次为：

time：跳转到指定时间  
rate：设置播放速度  
restart：跳转到场景开始  
reverse：倒放   
play：正向播放  
pause：在正向或倒放时，图标将替换为暂停图标。

时间控制器还提供了一种可视化书签的机制，书签是一种特殊类型的评论，与定义的时间相关联。它们可以通过脚本添加到 AER 文件中。每个书签可以有一个定义的类型和与之关联的消息。书签在时间控制器上用彩色刻度线表示。在适用的情况下，将鼠标悬停在书签上会显示其类型和消息。

时间控制器右侧的图标与书签相关：

next：转到下一个书签。如果没有可用书签，则跳转到结束时间。  
prev：转到上一个书签。如果没有可用书签，则跳转到开始时间。

注意：每个工具栏选项也可以通过可修改的键盘快捷键触发。 注意：书签遍历也可以通过书签浏览器控制。

时间控制器将显示速率、日历时间和模拟时间添加到状态栏中。

# 偏好设置

![](images/55bc1468570e061273acab5231af04e4cc9b9d2c8e67a15d9f9aadf09bcc2dba.jpg)

从时间控制器偏好设置中，用户可以设置以下时间：

Pause：在事件文件结束时暂停。  
Looped to start：选中时，显示将返回到时间 0 并在事件文件结束时继续播放。  
Extrapolate：选中时，显示将在事件文件结束时以实时进行推算。这对于实时模拟很有用。

时间控制器偏好设置还允许用户设置最大可设置播放速度（播放速度通过速率按钮设置）。两个选项是 1000 倍和 10,000 倍的实时速度。

注意：无论选择哪个最大可设置播放速度，播放速度的渐变数目是相同的。因此，选择更高的值将导致较小播放速度的可用播放速度选择较少。 警告：在事件密集的场景中使用高播放速度可能会导致体验下降。

# 5.3.2.2.3.10. 探测区域 Sensor Volumes - Mystic

传感器体积可以显示在地图显示上，以可视化传感器和干扰机的几何信息（视场形状、范围、方向）。

可视化的体积将被地球的球体遮挡，但不会被较小的特征（如山脉、建筑物或平台）遮挡。这些遮挡作为一种视觉效果实现，以防止光束穿过地球；它们不应被用于预测组件性能。

注意：体积不会绘制超过 600,000 公里。

![](images/03b2cb7f40acd27669c459d1b2ffc6ba529a9535beca831ca40a05a55fbb9782.jpg)

平台选项

可以从平台选项中启用/禁用体积。它们可以在单个传感器/干扰机级别进行控制。

偏好设置

![](images/1253ffdeea6212fffa9bc461c989a86776fe6d5677d74551efb53bff92155543.jpg)

体积类型将改变显示的体积类型，这些类型包括：

SlewLimits：绘制由关节部件的偏转限制定义的体积。  
CueLimits：绘制由组件的提示限制定义的体积。  
ScanLimits：绘制由组件天线的扫描限制定义的体积。  
Field-of-view：绘制由组件天线的视场定义的体积。

BeamWidth：绘制由组件的扫描限制和波束宽度定义的体积。  
Calculated：绘制一个计算出的体积，以显示上述类型的组合体积。

每个配置的传感器/干扰机模式都有以下控制：

Faces：此控制将启用并为体积的表面着色。

![](images/5782207d1410e467c65df4d5624e6e3a51502dfe1c6273b63c5f8c04c5bfe499.jpg)

Edges：此控制将启用并为体积的边缘着色。

![](images/cb8bff2904fe5854b7b008c5af8acae25cf5fce411feb255374857c7966f374f.jpg)

Proj.：此控制将启用并为体积的投影着色。

![](images/040b66d3faa2cb51ade0bb7b8538d466722efb4549be626bc2b6119e07e0e7ae.jpg)

用户可以通过点击“Add”并输入所需模式的名称来定义新的模式配色方案。

未设置传感器模式的传感器体积将以默认模式颜色显示。

# 5.3.2.2.3.11. 低头显 Head Down View - Mystic（弃用）

警告：HeadDownView 插件已被弃用且不再支持。用户应避免使用它，因为它将在不久的将来从 AFSIM 中移除。应使用 ACES Display 代替，它提供了许多相同的功能以及其他能力。

HeadDownView 显示所选平台的类似玻璃座舱的下视显示。该工具可通过在平台上右键单击的上下文菜单中使用。如果需要，可以同时打开多个下视视图。

注意：要显示所有可用数据，需要一个具有态势感知处理器的平台。

注意：HeadDownView 是一个原型功能，尚未完成。因此，它默认是禁用的，必须通过插件管理器启用。

![](images/0e5ca91d9d0496ab0ccef96ae80d602785f12f42e0800d9110c85a6c1d4ad3e4.jpg)

# 显示概述

显示器分为 12 个默认页面。可以通过点击底部的箭头来扩展或收缩页面。页面通过以下编号标识（默认页面可以在偏好设置中选择）：

![](images/b81fe37787e7072915e3394f99112cc7d61d8cc5cbd662e713bea75d7c753467.jpg)  
页面功能

![](images/1b70602be7152f72f90f5601e1e31f28fe2c11205b4dfeb29d409b7faa285a99.jpg)

ASR：未实现   
CKLST：未实现   
CNI：未实现   
DAS：未实现   
DIM：未实现   
EFI：显示俯仰和滚动  
ENG：显示油门、推力和燃油流量值   
FCS：未实现（视觉占位符）  
FTA：未实现   
FTI：未实现   
FUEL：显示燃油信息，如油箱水平、燃油流量和耗尽时间  
HUD：显示航向、速度（KTAS）和高度（视觉占位符）  
ICAWS：未实现（在标题中实现）  
NAV：显示飞机的俯视地图视图（目前不在菜单中）  
PWM：未实现   
SMS：显示武器、主武器和外部油箱的信息  
SACH：未实现   
TFLIR：未实现（视觉占位符）  
TSD-1/2/3：使用跟踪信息显示战术情况  
TWD：显示 RWR/ESM 威胁  
WPN-A/S：未实现

标题栏（顶部栏）

标题栏显示十二个不同的信息区域。从左到右：

![](images/c5e6c26ea88acbee7f604372940a7e61fb2e531c7a3cd63f8ff6f24149a91cc0.jpg)

Engine：显示推力和油门值

Fuel：显示总重以及总、内部和外部燃油值  
Weapons：显示武器及其数量。选定的武器将显示为白色  
LandingGear：显示起落架位置。空绿色表示起落架收起，红色表示起落架移动，实心绿色表示起落架放下  
ICAWS：显示三个警告：主警告、主警告和失速警告  
Blank：无（空白）  
COM/NAV/ADF/XPDR/Menu：无（仅视觉）  
PlatformInfo：显示平台高度（英尺）、航向（度）和速度（KTAS）  
Sim Time：显示自模拟开始以来的时间

# 人工地平线（EFI）

![](images/f037086b205178348445d1648fdd7736643b7e435b94711e43455ec1f7d2ba04.jpg)

人工地平线将显示平台的方向。

# 发动机显示（ENG）

![](images/9e7b942b3ea62adeeeac3fe245011fb7fd8a2e317e0952fd091e970c5aa31443.jpg)

发动机显示将显示平台的推力、油门和燃油流量（磅/小时）值。

燃油显示（FUEL）

![](images/b1ceeb30b3d102768e43b8b6cf520fb8ea8c5117bbd935a9b453d0e4c7abf98d.jpg)

燃油显示将显示总、内部和外部燃油水平的信息，以及燃油流量、耗尽时间和距离，以及 joker 和 bingo 水平。单位为磅。

HUD 重复器（HUD）

![](images/f1bcc262b22506f5e0f9fe1444a7041809210e2fd2bd88cde3ada6dbff14e90e.jpg)

HUD 重复器显示平台的航向（度）、高度（英尺）和真实空速（节）。

移动地图显示（NAV）

![](images/2fba9e820d44f553f4d02db00adb206941aa9b457ffc4f74700fdc4bbc5cd899.jpg)

移动地图显示将显示平台在地图上的位置。地图由地图定义偏好设置中的导航地图配置文件

确定。可以使用鼠标滚轮放大和缩小地图。

储存管理系统（SMS）

![](images/160f4dc6cbf0eefc894bcb1e2c5e34c59c98123b9bebec23ffdeff62edabea66.jpg)

SMS 显示显示平台当前的武器和外部油箱配置。

武器绘制

如果存在超过 8 种武器，武器将以两行 16 种武器布局显示，否则以一行 8 种武器布局显示。武器将根据每种武器的绘制类型从中间向外加载。当前支持的绘制类型是炸弹、SRM和 MRM。它们按此顺序加载到显示中。当前选定的武器将显示为白色。

注意：武器名称必须包含列出的字符串（不区分大小写），否则将默认绘制为 MRM。

主武器和选定武器

如果主武器关闭，将显示一个带有青色轮廓的 SAFE 框。当主武器打开时，框将变为绿色。如果然后选择了武器，它将在主武器框下方显示。如果武器弹药耗尽，其框将变为红色。

对抗措施和门

显示箔条、诱饵和照明弹的对抗措施计数。一个门标签指示武器舱门的状态（打开/关闭）。

战术情况显示（TSD）

注意：如果偏好设置中的页面 1 设置为 TSD，它将默认扩展到最大尺寸。

TSD 使用跟踪数据显示当前平台的“战术情况”。实体根据跟踪数据中提供的识别信息进行着色。将鼠标悬停在实体上会在 TSD 的右下角显示有关该项目的附加信息。单击该项目将保持窗口显示，直到单击实体以外的某个位置或跟踪丢失。

![](images/e1f73cd2342915eb1f49c6c588fd7b7c3451c60cdadccf163c66c292b8257f64.jpg)

符号

实体根据其识别绘制为以下之一：

：黄色方块  
Neutral:自色方块当  
BandtThreat：红色三角形  
Friendly：绿色圆圈   
Flight：蓝色圆圈

按钮

TSD 包括以下按钮，可以用鼠标左键单击：

Range Up/Down：更改当前范围（海里）。范围包括：5、10、20、40、80、160、320和 640 海里。  
Air：切换空域实体的可见性  
Gnd：切换地面域实体的可见性  
Waypt：切换航路点/路线的可见性

威胁警告显示（TWD）

TWD 显示 ESM/RWR 跟踪以及可能的识别 ID（ID 尚未实现，因此使用“U”表示未知）。要将

数据输入此显示，必须使用名称为“esm”或“rwr”（不区分大小写）的跟踪处理器。威胁将在显示的外环中显示为带有中间 ID 字符串的白色方块。

![](images/45e412b2c7487212d03984a3c07a5b4433fae44526e3cfa45c34148a171d21e6.jpg)

对抗措施

显示箔条、诱饵和照明弹的对抗措施计数。

# 偏好设置

![](images/73670a6634eb1ad8980e929fc9a7056b825fbab9c7b102c11a87b8ef8a961e85.jpg)

![](images/8946cd677fa387486659b740dccd991aa037fa3513dc8ea229e2d00d61509080.jpg)

![](images/42fa711e26bf682791381789ae131ed144a65206c3981274b2284556b722adeb.jpg)

![](images/211a27d48d89891804612feb173d19999e3ece402ba6a219bee04715f13dc91e.jpg)

在偏好设置中，可以设置分辨率以及每个插槽的默认页面。

注意：如果页面 1 设置为 TSD，它将默认扩展到最大尺寸。

# 5.3.2.2.3.12. 空间浏览 Zone Browser - Mystic

区域浏览器为在地图显示上可视化区域和区域集提供了一个界面。以下是其功能和使用方法的详细介绍：

![](images/214ce9e979cc9018b3c9f8ecf5389cc7fcec256c0a50f95ba840293f3cdbfb29.jpg)

# 功能概述

平台下拉菜单：对话框为场景中定义至少一个区域或区域集的每个平台提供一个下拉部分。如果适用，还会在对话框顶部提供一个全局定义的区域和区域集部分。  
显示所有区域：通过“显示所有区域”复选框，可以启用或禁用所有现有的区域和区域集。

![](images/516639c7583d656311f618f82dc7906b38654adbc66ce4583672ca6ca4fe6bce.jpg)

# 自定义选项

颜色和透明度：浏览器提供了修改线条颜色、填充颜色和填充不透明度（通过颜色选择器中的 alpha 值）的选项。这些颜色可以通过场景中的区域颜色命令和相应的区域集命令进行设置。默认情况下，所有区域/集将被分配一个可从 Warlock 偏好菜单中修改的单一颜色组合。也可以选择随机为每个区域/集分配颜色组合。

注意事项：重启场景将撤销通过浏览器对区域颜色所做的所有更改。

使用提示

工具提示：将鼠标光标悬停在地图显示的可见区域上时，会出现一个小工具提示，指示区域的名称。  
注意：浏览器仅填充在场景执行之前定义的区域。通过脚本或其他方法程序化添加的区域将不会显示。此外，不支持 reference_zone 和 negative zone 命令。

![](images/d4f1b81a3a585fad4549365519c08efb43080ff0b7da474b9dea70c3271d1313.jpg)

# 5.3.2.2.3.13. 地图鼠标悬停信息 Map Hover Information - Mystic

地图悬停信息插件负责在使用光标悬停在地图显示中的平台和轨迹上时显示工具提示。

![](images/6f41e3357b60b4b6bce24eaefd7fda2898338ad0e6318d34e5e60d0a90f84070.jpg)

地图悬停信息偏好设置

地图悬停信息偏好设置提供了一个界面，用于自定义地图悬停工具提示显示的数据。

![](images/04f5af86dcaffc86dbe07a48989a1ddc201e032046b83772959aec5fcc5156a2.jpg)

Enable Hover Info：完全打开/关闭悬停信息显示。  
ShowNames：悬停信息显示将列出平台或轨迹的名称。  
ShowItemLabels：每个显示的数据字段将在值前显示数据字段的名称。

平台和轨迹悬停信息部分控制当光标移动到平台或轨迹上时显示哪些数据。

要修改显示的数据，请选择一个标签：

左/右箭头将项目移入和移出“待显示项目”类别。  
上/下箭头控制信息在工具提示中显示的顺序。

注意：某些数据值是相对于 Bullseye 显示的。这些项目用“(Bullseye)”文本表示。如果未指定 Bullseye，则显示为字符串“no bullseye”。

注意：当为平台启用 Mach 时，它只会出现在空中和太空平台上。

# 5.3.2.2.3.14. 地图显示 Map Display - Mystic

地图显示对话框显示世界以及用户选择在地图上显示的平台、轨迹和其他元素。

导航地图的方法：

左键单击并拖动：随鼠标光标“拉动”地图。  
鼠标滚轮：向鼠标光标方向放大和缩小。  
双击左键：将地图放大到鼠标光标。  
中键单击并拖动：倾斜和旋转视图。  
箭头键：移动地图。  
Home 键：重置地图以居中于场景。

可以通过左键单击选择平台。

当鼠标光标悬停在许多屏幕元素上时，会弹出附加信息。

右键单击地图将打开地图的上下文菜单。您也可以右键单击平台以打开平台的上下文菜单。

# 平台标签选项

可以从平台选项对话框应用显示平台名称的标签。

![](images/34d4e3be494fb83c88e05738943a5a89030a20487dac0e319e56b4da283f385a.jpg)

# 测量工具

![](images/0b8c3278ccc8231effedda7c7808662e3040e0820c4ffc77ebddc3f4e9397f8c.jpg)

可以通过右键单击平台或位置并从菜单中选择测量选项，然后单击另一个平台或位置来进行测量。选择标尺将显示选项对话框，取消选择将隐藏它。

draw_compass：沿大圆进行测量。  
icon_ruler：沿直线进行测量。  
icon_compass：显示相对航向。  
distance：显示距离。  
speed：显示闭合速度。  
hourglass：显示预计到达时间。

选择字体大小。

dest：显示目的地端的指标。  
source：显示源端的指标。

居中

右键单击将提供一个选项以将相机居中于当前选择或整个场景。

跟随

右键单击平台将提供一个选项以让相机跟随平台。用鼠标移动相机将结束跟随。

# 偏好设置

![](images/fbbafcb64e45f1a892973ab0f1dd93c836af29a6f47bc6ab4eec49df502d42c5.jpg)

Map：选择要显示的地图。可以在地图定义中添加地图。  
Brightness, Contrast, Saturation：影响地图的色彩平衡。  
Lighting：启用太阳光照。  
ECICamera：在地心地固视图和地心惯性视图之间切换。  
CenteronStart：在启动时将相机居中于场景。  
Show Terrain Altitude At Cursor：在状态栏中显示鼠标光标下的地形高度（如果可用）。  
ZoomonMouseCursor：启用时，缩放操作将以鼠标光标为中心；禁用时，将以视图中心为中心。

Display Team Color：平台图标要么用团队颜色着色，要么抑制颜色。  
Truescale：按比例绘制平台图标。  
Modelscale：在屏幕空间中缩放模型。  
Label font：设置应用于平台标签的字体（例如，平台标签）。  
GridLines：启用/禁用纬度和经度线，并选择其颜色。密度子选项更改网格线的密度。  
Elevation Lines：与 TMS 高程数据库关联时，启用地形等高线。  
CoastLines：启用/禁用并选择海岸线的颜色。  
CountryBorders：启用/禁用并选择国家边界的颜色。  
US Internal Borders：启用/禁用并选择美国州边界的颜色。  
LakesandRivers：启用/禁用并选择主要湖泊和河流的颜色。  
Screen-Centered Range Rings：启用/禁用并选择屏幕中心范围环的颜色。  
Terminator：启用/禁用昼夜分界线的可视化。  
Sub-Solar Point：启用/禁用太阳直射点的可视化。  
Sub-Lunar Point：启用/禁用月球直射点的可视化。  
Solar Path：启用/禁用表示太阳直射点路径的线条。  
Scale：启用/禁用比例工具。  
Compass：启用/禁用指南针工具。  
Tooltips：启用/禁用当鼠标悬停在地图元素上时的工具提示。

# 地形等高线

当与 TMS 高程数据库关联时，启用地形等高线。要选择高程数据库，请在“Source”下浏览所需的 TMS 文件。

![](images/fc51ee68fb20848c2e0c0d7734b89ee48138c66aee8653e9f84e2549db003a45.jpg)

![](images/8f277d51df18d50c607f99cfbbf3f41403c6214d06cee5e29fa5c04cbac30046.jpg)

# 屏幕中心范围环

启用/禁用并选择屏幕中心范围环的颜色。

![](images/836311243c34584538bf82722c321907e35f6a038d6d3623f498dfb788c4dd3d.jpg)

昼夜分界线

启用/禁用昼夜分界线的可视化。可以更改线条的宽度和颜色。

![](images/55433349d493509ddb53434b433ae1d45ecc20e4cd1fcd206c92a67c38a7c96f.jpg)

太阳直射点

启用/禁用太阳直射点的可视化。可以更改点的大小、颜色和图标。

![](images/d7c29c1c1da8aa96ab147c79174aea601b7717fb820b894d2fc6b58f9af0a4c3.jpg)

![](images/1261a39e12444969842142a40d4ceafd1ca7ce73647e4f6c233b72f59594cc37.jpg)

![](images/90ae5cf09ded3c0539d09e57f289651ad06cbf04299252230f724fb68d56e1da.jpg)  
月球直射点

启用/禁用月球直射点的可视化。可以更改点的大小、颜色和图标。

太阳路径

![](images/01090755a679bc8892f78aa4c63ba6e77a85139b166f292f7754bfb30aa81fd5.jpg)

启用/禁用表示太阳直射点路径的线条。可以更改线条的宽度和颜色。

比例工具

![](images/4206afb77433ce06255a56392e1b92827953a4bf7432ec68cf21e7421a5883a9.jpg)

启用/禁用比例工具。

指南针工具

![](images/a73d0b8399d3d0b18db4acf1fa1b45ab0871ffcdb5c85ee12aaded6f934aa308.jpg)

启用/禁用指南针工具。

以下是其它要素要在地图中显示的：

# 5.3.2.2.3.14.1.空战可视化 Air Combat Visualization - Mystic

Warlock 中的空战可视化插件提供了多种可视化空战数据的方法，增强了态势感知和分析能力。以下是其功能的详细介绍：

![](images/9453be8c89aeecf7ba7b5a6a6b5bd3cea2f8b2e896d5c4e45b80f8d22e06bfd0.jpg)

# 可视化组件

数据环：这些环帮助可视化空战数据，如防御性、燃料水平和过载（GLoad）。

□ 防御性：测量范围从 -1 到 1，-1 为全红圈， $+ 1$ 为全绿圈。正值顺时针填充，负值逆时针填充。  
□ 燃料水平：测量范围从 0 到 1，正值顺时针以绿色填充。  
□ 过载（GLoad）：黑色条代表 1G（水平飞行），正向范围最高可达 9G，负向最高可达 -3G。值在 0 到 1G 之间时变为黄色。

![](images/36785efe6690887cef8f96514e1cd9af02acdce2079f87a86d0052b991d55454.jpg)

数据强调：提供快速的信息概览：

▫ 武器状态：显示“W”并根据弹药水平改变颜色（ $50 \%$ 为绿色， $1 5 0 \%$ 为蓝色，无弹药为红色）。  
▫ 发射状态：当雷达发射时显示 $\prime \langle { \sf R } ^ { \prime \prime }$ ，干扰器发射时显示“J”，通讯时显示 $^ { \prime \prime } \mathsf { C } ^ { \prime \prime }$ ，雷达和干扰器同时发射时显示“X”，无发射时显示“–”。  
燃料状态：显示“F”，并根据燃料水平改变颜色（ $. > 5 0 \%$ 为绿色， $1 5 0 \%$ 为黄色， $10 \%$ 或到达“bingo”状态时为红色，“joker”状态为蓝色）。  
□ 特征：从低到高显示重要性：无适用时为“–”，产生尾迹时为 $" { \mathsf { C } } ^ { \prime \prime }$ ，使用加力燃烧时为“A”，武器舱门打开时为 $" \boldsymbol { \mathsf { W } } ^ { \prime \prime }$ ，最重要的状态会被显示。

![](images/548e60c7de948ac8613a89b2b3fda8907ddea6c9b233b20f362909cb76fd2996.jpg)

状态数据：提供数值数据，如平台名称、海拔高度、垂直速度、速度、马赫数、过载（GLoad）和迎角。

![](images/149760c093e725f8512110cbc829805e841f4fbcd76ea313f81b383cd9ed84cd.jpg)

交战线：可视化平台之间的交互：

武器交战区（WEZ）线：表示与武器交战区的接近程度，平台在范围内时线条连接。

□ 检测线：显示检测范围，平台在范围内时线条连接。  
线条可能会闪烁以指示目标被跟踪或在最大射程（Rmax）范围内。

![](images/809aac8c9b2873c6dbabad7c53420b1b55c09d569b1e6bf3fe60afcd31f1cc51.jpg)

空战覆盖层：可以添加到 Tether 视图中，以进行详细数据可视化，包括：

□ 状态数据块：显示运动和燃料状态数据。  
□ 战术数据总结块：显示战术和武器数据。  
□ 交战数据块：显示源平台和目标平台之间的交战数据，并根据平台方标颜色。

![](images/0ed7c7e6e87dd36cb701c01dde873ba5416a42f50967f0b8da8cb1bf2d0850ea.jpg)

# 偏好设置

用户可以调整数据环所测量的数据，并切换状态数据和数据强调的显示。

![](images/ec86b47581d411299f46c8c44ccfc5ea5c19913bf4d71450193357c8f082807d.jpg)

# 5.3.2.2.3.14.2.平台历史 Platform History - Mystic

平台历史功能以轨迹线或翼带的形式显示平台的几何历史。

![](images/8b467da41694ad9c09c90c129a73f40d3017401ed61940b03d70ff586543a57b.jpg)  
翼带

![](images/f19933b13f14a49922a220dd6f14330538760e8bd926597a2e975a4bbc5ea565.jpg)

平台选项

可以在平台选项中启用/禁用平台历史。

# 偏好设置

Preferences-AFSIM-Mystic

7 ×

![](images/d596a8f84b7c1718c94fcc7501bc9d0de3f0fa6876e6a9d8462f97fba758b3e3.jpg)

平台历史可以在偏好设置中配置。

平台历史插件的偏好设置位于“Map”下。

# 轨迹线

宽度选项：确定线条宽度（以像素为单位）。  
长度选项：确定从当前位置到轨迹线末端显示的时间长度。

轨迹线可以按以下方式着色：

team-color：平台的团队颜色。  
platform name：每个平台的独特颜色。  
state：根据平台的状态选择颜色，状态可以是正常、被检测、被跟踪、被攻击或被击毁。   
behavior：根据每个平台的高级行为树上执行的节点选择颜色。默认情况下，插件会自动为每个行为树叶节点选择颜色。或者，可以在 AFSIM 输入中为行为节点分配颜色。在偏好设置中，可以更改颜色，并可以隐藏或显示行为。对于没有行为树的平台，将使用默认颜色。

![](images/d83e4d82be54384ce2ecac8419b85128e5d8449eef9168de46b8e9e4fa1e0160.jpg)

![](images/30cdb8be59694833b09bbd6ddd4d344531570e9b9b0c42eb492e3133d64056d4.jpg)

# 翼带

长度选项：确定从当前位置到翼带末端显示的时间长度。  
宽度比例：允许夸大翼带。  
颜色方案：可以是团队颜色、绿色或灰色。  
死亡时的透明度：当平台被击毁时，翼带的透明度将改变。

# 5.3.2.2.3.14.3.轨道 Orbits - Mystic

轨道插件显示空间移动物体和月球的轨道。

![](images/cdcb2f48e0376826ba570ea5714a1aa8dd89835af57263eab7a7c4c7b103727e.jpg)

轨道将在适当的参考系中显示。这可以通过在地图显示的 Mystic 偏好设置中切换 ECI

相机来更改。

以下是同一轨道在 ECI 框架、ECEF 框架和平面地图上的三个图像。

![](images/630810c8949b0e704ec63b390b0276036ddb6270e11687de50813dabc24d140c.jpg)

![](images/d1ecfa69432931a53a4f1c0d6c56532cbca2cf95a20a5f758b2a9c54104f644d.jpg)

![](images/30086174e41cbf0e0f5175dba0bb3d6bc8d471e90d19caf6013a90fe4d8aa86b.jpg)

![](images/ef83dcdcdaca8c038b1656003b2eb55c94ad651c22e8e5c5413161fec9f9095f.jpg)  
偏好设置

Fadeout(sec)：当平台改变轨道时，这将决定旧轨道淡出的时间。  
Color：颜色可以设置为白色、团队颜色、按名称随机颜色或按场景。场景选项使用WSF_SPACE_MOVER 或 WSF_NORAD_SPACE_MOVER 中的 orbit_color 命令来定义轨道颜色。如果移动物体没有定义颜色，轨道颜色将与团队颜色相同。  
Linewidth：设置轨道的线宽（以像素为单位）。  
Periods：在平面地图上查看轨道或没有 ECI 相机时（参见地图显示 -Mystic 偏好设置），周期值将决定显示轨道的周期数。

# 5.3.2.2.3.14.4.路线 Routes - Mystic

平台的路线可以选择通过 AFSIM 在 event_pipe 中进行通信。全局路线将不会写入文件。

![](images/f1bd579cdfd2ec33d86f3ab90f490b9f7a510a788ef3893f16b334d82783a865.jpg)

在平台选项中启用路线将显示当前路线。在播放过程中，路线可能会动态变化。右键单击平台将提供一个选项“显示路线信息”，这将显示平台路线的航路点摘要。

![](images/f6daf066cb6e544142b9af88cfa0bb1e1fdcb31db17d0cba8308f145210058f5.jpg)

# 5.3.2.2.3.14.5.轨迹 Tracks - Mystic

Tracks 功能负责在地图显示上显示轨迹，并显示在平台详细信息显示中的相关信息。场景中的本地轨迹会在地图显示上显示轨迹图标。

![](images/ceba37d184a4a4c860f35aee59437bcd6b0919a3f0e51998113e801e42c0b3ed.jpg)  
平台详细信息

![](images/6a80b5d8529e93e7b6c4a4024b87aee0ad98b952764616960ae124b7b85afede.jpg)

当选择一个平台时，其主轨迹和传感器轨迹列表将添加到平台详细信息显示中。点击列表中的一个本地轨迹将会在地图显示中突出显示该轨迹。

右键单击轨迹将提供选项以追踪或绘制轨迹。

Trace：追踪将显示轨迹的历史。

![](images/0c908b4e7717c4ad4a76813c79fcf557d1fc0e3074d6733c14c0e7f38da03d27.jpg)

# Engagement Events-AFSIM-Mystic

?

```csv
510.0000: vhf_ew_radar-1's vhf_ew_radar_sensor has a new sensor track vhf_ew_radar-1:2  
510.0002: 100_radar_company has a new local track 100_radar_company:4  
510.0002: 100_radar_company correlates 100_radar_company:4 with vhf_ew_radar-1:2  
1311.6666: uhf_ew_radar-1's uhf_ew_radar SENSOR has a new sensor track uhf_ew_radar-1:3  
1311.6670: 100_radar_company correlates 100_radar_company:4 with uhf_ew_radar-1:3  
1761.6666: s-band_ew_radar-1's s-band_ew_radar SENSOR has a new sensor track s-band_ew_radar-1:1  
1761.6675: 100_radar_company correlates 100_radar_company:4 with s-band_ew_radar-1:1  
1841.6675: 100_radar_company decorrelates 100_radar_company:4 from s-band_ew_radar-1:1  
1911.6666: s-band_ew_radar-1's s-band_ew_radar SENSOR has a new sensor track s-band_ew_radar-1:2  
1911.6675: 100_radar_company correlates 100_radar_company:4 with s-band_ew_radar-1:2  
2290.0002: 100_radar_company decorrelates 100_radar_company:4 from vhf_ew_radar-1:2  
2591.6670: 100_radar_company decorrelates 100_radar_company:4 from uhf_ew_radar-1:3 
```

Plot：绘制轨迹指标将显示指标随时间的历史。真值也可以在图上显示，对于本地轨迹，可以绘制贡献的传感器轨迹。

![](images/e20c1022682bc4993be5b25d4247c1401815a77498005d9b81769b165b7abb54.jpg)

# 偏好设置

轨迹可见性偏好页面控制何时在地图显示上向用户显示轨迹。

ShowNoTracks：地图显示上不会显示任何轨迹。  
Show Local Tracks Only：仅显示所选平台的本地轨迹。  
Show All Visible Teams’ Tracks：显示所有标记为可见的团队的所有平台的本地轨迹。  
Show Selected Team’s Tracks：显示组合框指示的团队的所有轨迹。  
Show Tracks From Network Simulations：显示从通过 XIO 连接的 AFSIM 应用程序接收到的轨迹。

![](images/b3f201e77d46358513c532e1ed76263390ca3485e62ccd6df3b38c458b4a536d.jpg)

还有一些自定义选项用于控制轨迹如何显示给用户。

ShowTeamColor：轨迹将根据报告的团队颜色着色。  
Show Track ID Label：轨迹将根据报告的团队用轨迹 ID 标记。  
ShowTrackOrientation：控制轨迹图标是广告牌式的还是根据报告的方向倾斜。  
LabelFont：设置应用于轨迹标签的字体。  
Track Scale：缩放轨迹图标。  
WedgeIcon：在地图显示上显示默认轨迹图标。  
CustomTrackIcon：在地图显示上显示指定的轨迹图标。要选择图标，可以拖放支持的图像或使用浏览器手动选择一个。  
Rules-BasedIcon：如果选中“使用目标平台图标”框，则显示被跟踪平台的模型。否则，使用基于轨迹报告的空间域的自定义模型。未指定的图标使用楔形图标。

在地图显示上悬停在轨迹图标上会提供以下信息：轨迹 ID、侧面、类型、空间域和航向。

# 5.3.2.2.3.15. 插件管理 Plugin Manager - Mystic

![](images/19b54c622927709fdbebe2798bcfa0fd35fc15ae19f8ea441290b38f9324e673.jpg)

插件管理器对话框显示有关插件的信息，并允许用户控制是否加载特定插件。可以在“选项”菜单下找到插件管理器的链接。

插件

插件可以提供图形用户界面（GUI）与模拟进行交互和/或显示信息。显示的许多小部件实际上是插件，可以选择性地加载。请注意，某些插件可能仅限于特定应用程序。例如，Mystic 或 Wizard 插件可能与 Warlock 可执行文件不兼容，反之亦然。因此，插件可能具有指示其为哪个应用程序编写的角色。应用程序只会加载与其兼容的插件。因此，您可能会在插件管理器中看到一些无法加载的插件。

插件管理器

插件管理器左侧有一个列表，列出了应用程序尝试加载的所有插件。

只有选中“自动启动”复选框的插件才会被加载。要阻止插件加载，请取消选中此选项。应用程序必须重新启动才能使此更改生效。

插件名称左侧的符号指示插件的状态。将鼠标悬停在插件名称上会显示一条消息，指示插件未加载的原因。

位于左下角的“自动启动所有插件”复选框将切换所有插件的自动启动。

当选择一个插件时，所选插件的简短描述将出现在插件右侧。

“打开插件文件夹”按钮将打开插件 DLL 的文件夹位置。

# 5.3.2.2.4. 工具菜单 Tools Menu - Mystic

![](images/f517332355a7fc95988a855b57c2830c1cecbaea322967190e027f644c12bc31.jpg)

Show Quantum Tasker Matrix：显示原子任务供应商和接收者的矩阵。  
Record Video：切换视频录制功能。   
Screenshot：捕获屏幕截图。  
Model Viewer：一个窗口，用于查看应用程序中可用的模型。  
Show Engagement Statistics：显示模拟中发生的武器交战信息。  
Show AFSIM Information：显示 AFSIM 应用程序中模拟执行的信息。  
ShowEventList：以可过滤和可导出的格式显示模拟中发生的事件。  
Show Result Statistics：显示模拟中事件的统计信息。  
Battle Management：用于管理平台的工具。  
CommVis…：显示通信可视化工具。  
Plotting：绘制平台数据。

# 5.3.2.2.4.1. 交战分析 Engagement Analysis - Mystic

交战分析工具查看场景中的所有武器交战。

![](images/eab6bdf9064906acd1ed7d6462618ea9d6cbe6cfd8db62a5e98e50bec2168f81.jpg)

功能

顶部的过滤器允许用户选择攻击者和目标平台/组。

右键单击列将提供选项以显示/隐藏列、绘制该列中的数据、将数据导出为 CSV 文件或追踪事件。

```csv
88.0000: uhf_ew_radar-1 has a new sensor track uhf_ew_radar-1:2  
88.0004: 100_radar_company has a new local track 100_radar_company:2  
88.0004: 100_radar_company correlates 100_radar_company:2 with uhf_ew_radar-1:2  
88.0007: 10_iads_cmdr has a new local track 10_iads_cmdr:2  
88.0007: 10_iads_cmdr correlates 10_iads_cmdr:2 with 100_radar_company:2  
90.0007: 10_iads_cmdr tasks lr_sam_battalion_1 to ENGAGE against 10_iads_cmdr:2  
90.0007: 10_iads_cmdr tasks mr_sam_battalion_4 to ENGAGE against 10_iads_cmdr:2  
90.0016: mr_sam_battalion_4 has a new local track mr_sam_battalion_4:1  
90.0016: mr_sam_battalion_4 correlates mr_sam_battalion_4:1 with 10_iads_cmdr:2  
106.6740: mr_sam_acq_radar_4 has a new sensor track mr_sam_acq_radar_4:1  
106.6740: mr_sam_battalion_4 correlates mr_sam_battalion_4:1 with mr_sam_acq_radar_4:1  
108.1116: mr_sam_battalion_4 tasks mr_sam_ttr_radar_4 to Track against mr_sam_battalion_4:1  
112.1116: mr_sam_ttr_radar_4 has a new sensor track mr_sam_ttr_radar_4:2  
112.1116: mr_sam_battalion_4 correlates mr_sam_battalion_4:1 with mr_sam_ttr_radar_4:2  
116.1616: mr_sam_battalion_4 tasks mr_sam-Launcher_4-1 to Shoot against mr_sam_battalion_4:1  
124.6703: mr_sam-Launcher_4-1 completes task from mr_sam_battalion_4 to Shoot against mr_sam_battalion_4:1  
184.9903: mr_sam_battalion_4 tasks mr_sam-Launcher_4-1 to Shoot against mr_sam_battalion_4:1  
186.9903: mr_sam-Launcher_4-1 fires on mr_sam_battalion_4:1  
239.3903: Weapon Terminates: target_impact 
```

事件追踪

追踪事件尝试找到导致武器交战的场景中的所有事件。这些将包括传感器轨迹、本地轨迹、任务和武器事件。

# 5.3.2.2.4.2. 事件列表 Event List - Mystic

概述

事件列表可以通过工具菜单中的“事件列表”访问。

![](images/d059aa3f63b5e2830527a01331d60809dc27b56e9073ff829d03a422118b7807.jpg)

功能

例如，此过滤器将接受在前 120 秒内发生的所有事件，适用于“10_iads_cmdr”或

“100_radar_company”平台，并具有“MsgEntityState”类型。

事件列表对话框显示所有当前加载的事件。当此对话框打开时，应用程序的其他部分将无法访问。

对话框的上半部分是过滤器列表，下半部分是事件列表。只有加载并通过过滤器的事件才会显示。

# 过滤器类型

从下拉菜单中可以选择三种类型的过滤器：

Condition：允许用户测试给定列中的值如何与某个值进行比较。例如，测试列时间小于等于 120 的过滤器将允许在前 120 秒内发生的所有事件通过。  
And：此过滤器将其他过滤器分组。如果事件通过其所有子过滤器，则通过此过滤器。如果没有启用的子过滤器，则事件通过。  
Or：此过滤器将其他过滤器分组。如果事件通过至少一个子过滤器，则通过此过滤器。如果没有启用的子过滤器，则事件通过。

# 比较类型

以下比较始终可用：

$= =$ ：如果事件中的值等于给定值，则通过。  
!=：如果事件中的值不等于给定值，则通过。  
contains：如果事件中的值（作为文本处理）包含给定文本，则通过。此检查不区分大小写。

如果给定值是数字，则以下比较可用：

<：如果事件中的值小于给定值，则通过。  
$< =$ ：如果事件中的值小于或等于给定值，则通过。  
>：如果事件中的值大于给定值，则通过。  
$> =$ ：如果事件中的值大于或等于给定值，则通过。

如果指定的列是“平台”或“交互者”，则以下比较可用：

isonside：如果事件适用于给定侧的平台，则通过。  
isoftype：如果事件适用于给定类型的平台，则通过。  
isofcategory：如果事件适用于给定类别的平台，则通过。

# 添加过滤器

添加过滤器的两种主要方法：

对于 And/Or 过滤器，从其上下文菜单中选择“添加子项”或单击添加（+）按钮，为其提供用户可以填写的子过滤器。  
从事件列表的上下文菜单中选择“创建过滤器”。这将在顶层创建一个新过滤器。

# 重新排列过滤器

用户可能需要重新排列过滤器，因为逻辑发生了变化，或者过滤器在错误的位置创建。选择过滤器上下文菜单中的“剪切”将删除所选过滤器及其子项，以便可以将其粘贴到其他位置。剪切或复制的过滤器可以根据需要多次粘贴。  
要删除过滤器而不复制以备后用，请单击其行中的删除（-）按钮。要快速删除所有过

滤器，请右键单击根（顶部）过滤器并选择“清除子项”。

# 启用/禁用过滤器

启用复选框指示过滤器是否启用。未启用的过滤器在更新事件列表时不会被考虑。如果分组过滤器被禁用，但其子过滤器已启用，则不会考虑任何子过滤器。即，为了检查过滤器，所有祖先也必须启用。  
要禁用所有过滤器，只需禁用根项目。

# 反转过滤器

反转复选框允许用户反转过滤器的结果。例如，“包含”测试变为“不包含”。反转的 AND，即 NAND，具有“如果至少一个子过滤器不通过，则通过”的逻辑。反转的 OR，即 NOR，具有“如果所有子过滤器不通过，则通过”的逻辑。

# 导入和导出

在过滤器上下文菜单中有两个选项，称为“导入”和“导出”。

导出：将保存所选过滤器及其所有子项，以便以后导入。导出的过滤器被赋予名称，以便将来易于找到。  
导入：将在所选过滤器处粘贴导出的过滤器。粘贴后，修改导入的过滤器不会影响导出的过滤器。

导出的过滤器在关闭和重新打开应用程序后仍然可以导入。

# 隐藏列

在列标题上下文菜单中有两个选项，称为“隐藏 <列名>”和“显示所有隐藏列”。

隐藏的列仍将参与过滤，但不会显示。

导出为 CSV

从事件列表上下文菜单中选择“导出为 CSV”将保存过滤后的事件到 CSV 文件。

# 绘图

从事件列表上下文菜单中选择“绘图”允许用户绘制过滤事件中的数据。绘图允许用户为X 和 Y 轴指定列，以及用于表示不同数据系列的列。

只有包含数值数据的列可以用于轴，只有少数列可以用于系列。默认情况下，X 轴始终为“时间”。如果用户右键单击以打开菜单的列仅包含数值数据，则它将用作默认的 Y 轴列。通过在系列列表中选中和取消选中复选框，可以显示或隐藏单个系列。

![](images/d4b8f7bda50dc0ec78816227d7569ef9c10b636f805de2a93c1a851cdf7b2aff.jpg)

# 5.3.2.2.4.3. 统计 Statistics - Mystic

![](images/0c1aa36f6dc2f0f6a890f8be024fe8938b4e2aac091091c9ef7acde9b49713de.jpg)

# 功能

统计信息可以在工具菜单下的“结果统计”中找到。此对话框按事件类型显示加载文件的内容，显示频率和内存使用情况。

饼图提供了表格数据的可视化表示。它是基于内存使用情况绘制的。

# 5.3.2.2.5. 开发者菜单 Developer Menu - Mystic

开发者菜单可以在偏好设置中启用。

注意：除非您是开发人员，否则不建议使用开发者菜单。稳定性无法保证。

# 功能

Performance Analyzer…：显示应用程序使用的内存量。  
ShowMapWindow SceneGraph：显示地图显示的场景图。右键单击节点将提供详细信