# 5.3.2.2.6. 帮助菜单 Help - Mystic

帮助 - Mystic

帮助菜单包含指向“关于”对话框和“文档”对话框的链接。

![](images/f0a6b3a263ce346ad023579a59271167852207c010200c79f12bbb229ce35b70.jpg)

![](images/8c33cca56440c83770ff7a323ab878b1217d4304cd229cd31d1f1f342afdd1ab.jpg)

![](images/4bd20ec4e9a68fdeff8f0221c770b211bfdde20aeeb1826b9eb213b4753f0fb2.jpg)

功能

关于对话框：提供有关版本、第三方许可证、艺术作品归属以及系统高级信息的信息。  
文档对话框：包含指向 AFSIM 文档重要部分的链接。

命令行

当执行时提供 -?、-h 或 -help 命令行参数时，Mystic 将显示命令行使用情况。这将显示一个对话框，显示 Mystic 的正确命令行用法。

![](images/25298f150c480160506195cc71984211eae5a51107954a764f7a1aebfd94b62a.jpg)

# 5.3.2.3. 主显示 Central Display - Mystic

![](images/3d79a56d25415a749738cd03764b6d0180bda219844b3519cd631e579c5e58fd.jpg)

![](images/8e64b3e261747b27ef1e834ccef593d5d69a051a1925f61033dc18d3878fb982.jpg)

![](images/24d76355f9345caa090c2cba54b01ea46096c9aebe2df2d1d3693c594fc6a4ce.jpg)

![](images/c3dd6467617214f3f20cfa00f7b993086d25e0153a42ccfb9469fe195feb5d7b.jpg)

功能

Mystic 的中央显示不仅仅可以包含地图视图。停靠小部件可以移动到中央显示中，并且可以同时显示多个。要将显示移动到中心，请将它们拖动到中央显示的边缘。一旦停靠，右键单击将提供以下选项：

![](images/17a199f7cdbb9b744adff403e3939289da28ee1058bb068cde15c0ee4037f016.jpg)

MoveToNew Window：这将把一个停靠小部件移出中央显示并使其成为一个窗口。此菜单选项仅在停靠小部件位于中央显示中时出现。  
Hide：隐藏一个停靠小部件。要取消隐藏停靠小部件，请使用视图工具栏启用停靠小部件。此选项仅在停靠小部件位于中央显示中时出现。  
Close：关闭停靠小部件。  
FullScreen(F11)：切换停靠小部件是否应全屏显示。

可放置在中央显示的窗口

ACESDisplay：显示当前平台的空战数据。  
Situation Awareness Display：显示当前平台的态势感知（感知）信息。

# 5.3.2.3.1. 空中交战综合显示 ACES Display - Mystic

![](images/f1a7de2345f907f6070efce89ae972f2182b87e2446171803af6050bbe72fbc8.jpg)

Air Combat Engagement Summary (ACES) Display 是一个集成显示工具，旨在为包含WSF_SA_PROCESSOR 的平台提供多组空战数据。它通过一个可重新配置的显示界面，整合了多种空战信息。

# 功能概述

数据要求：要显示所有可用数据，需要一个具有态势感知处理器的平台。  
插件状态：ACESDisplay 插件是一个原型功能，尚未完成。因此，它默认是禁用的，必须通过插件管理器启用。  
打开显示：在地图显示或平台浏览器中为平台打开上下文菜单（右键单击），然后选择“ACES View”以打开显示。

ACESDisplay 提供了一个强大的工具，用于分析和可视化空战数据，尽管它仍处于开发阶段，但它为用户提供了丰富的战术信息和灵活的显示选项。

# 显示同步

在 Warlock 中，战术态势显示（TSD）和态势感知显示（SAD）的缩放和居中可以通过点击中央的“DisplaySync”按钮来同步。当启用时，左侧区域的缩放和居中将作为同步显示的参考。

# 显示切换

在 Warlock 中，四个圆形显示区域可以通过点击顶部或底部显示的左侧或右侧来进行切换。这一功能允许用户根据需要重新排列显示内容，以便更好地组织和查看不同的数据集。

![](images/09418dd08f4ffdf8e966c830b6a92e9d2af664d3b55e1c2dc590a2c1b4030534.jpg)

# 设置中心点

在 Warlock 的战术态势显示（TSD）或态势感知显示（SAD）中，用户可以设置一个中心点，以便放大并获取有关特定区域的更多信息。此选项可以通过右键单击打开的上下文菜单中找到。重置中心点将使自有平台返回到中心位置。

![](images/63c42b9a688dae8c59013123404d483aaedf0b510326562e335eb8f68ef67e8e.jpg)

新的中心点被设置。

![](images/0c014919d06d83746f718bda170d063d93d747a1075e200a5a8cd77a72e71cd3.jpg)

# 设置

![](images/a193179bd7e0570548b6715b81d677c476e563ff9e39b1a33cc897b30139f025.jpg)

在 Warlock 的 ACES Display 中，战术态势显示（TSD）、态势感知显示（SAD）和交战区域都有设置选项卡，可以打开以切换各种设置。这些设置允许用户根据需要自定义显示，以便更好地适应不同的战术需求和分析场景。

# 显示区域

ACESDisplay 包含多个显示区域，每个区域提供特定类型的数据。以下是这些区域的详细说明：

# 平台数据

![](images/c813ea6dc505dbadd842da663adbf7b90ea4cfb6420086c9d21ca12339db31cf.jpg)

在 Warlock 的 ACESDisplay 中，显示的左上角提供了一般平台数据。这些数据从左到右依次包括：

发动机推力和油门：显示标准化的推力和油门设置，包括加力燃烧器的使用情况。  
重量/质量：显示总重量、总燃料重量、内部燃料重量和外部燃料重量（单位为千磅）。  
武器：显示武器的数量和类型，选定的武器以白色显示。  
燃料：显示当前燃料流量（磅/小时）、joker/bingo 燃料状态（磅）和过载（G-load）。  
高度和速度：显示高度（英尺）、校准空速（节）、真空速（节）和马赫数。

# 态势感知显示 Situation Awareness Display

![](images/4282486a80b89e37811ddcadb9e345f030cfe6cc0c0e1a1fa0fac17107c3bfad.jpg)

态势感知显示（SAD）为用户提供了一个战术感知的图形化总结，利用平台的WSF_SA_PROCESSOR 数据。这种显示方式帮助用户理解环境中的实体及其动态变化，从而在空战环境中做出更有效的决策。

感知

在态势感知显示（SAD）中，感知到的实体根据其识别信息进行绘制。实体可能还包括其他信息，例如实体图标右侧的高度（以千英尺为单位），图标左上角的优先威胁编号，以及图标左下角的优先目标编号。实体的方向与其航向一致。被态势感知处理器（SAP）标记为重要的实体会显示为白色轮廓。漂移中的实体显示为透明，因此看起来较暗。如果设置了eyes_track_processor，则在实体图标的左侧会出现一个眼睛形状的图标。

符号和识别

bogie：未知/不明，黄色方块

![](images/27bb1a23e8d5701818bbd8868049094218af3b7f868b3ed26b2b2d362f0c85f1.jpg)

neutral：中立，白色方块

![](images/bcbfe420a81b08fba925aa330cfdb58e7bf88062b094d10a1d8dace6d3ffd7f7.jpg)

bandit：敌机/威胁，红色三角形

![](images/ce4119e1ab090174d0fca250d873204794ef732f0ffbf0ebb4d0d1850637201c.jpg)

friendly：友机，绿色圆圈（可选 ID）

![](images/d226974e425df72829ec318ee09242cab02cbcc453adb12e2f0d2499b95c7607.jpg)

flight：飞行，蓝色圆圈（带飞行 ID）

![](images/15d968481e874cdc27dab9aa8ea3c87eb80d89112dff2c5d9f4becd775ac3f42.jpg)

missile：导弹，带圆圈/方块/三角形的箭头

![](images/53ce93714f0b5837378748de9b5288fd15f2d609ffe3d1387062656b0206ee17.jpg)

例如，下面的感知显示一个威胁，其相对方位为 0 度，飞行高度为 35,000 英尺。它

被评估为第二高优先级的威胁和最高优先级的目标。该实体被标记为重要，并且对飞行员可见。

![](images/e69657c5df01433c7fe5e37e246f5d2db694a5477c41656cd6b72e1f0f8e0936.jpg)

# 群组

![](images/810d06e786f793a1ca9dd54d34af1f2e7076c41d94210d50c661a3259e8d355d.jpg)

在态势感知显示（SAD）中，群组通过足够大的圆圈来显示，以包含群组的所有成员。可以在 WSF_SA_PROCESSOR 中指定最小群组半径，这对于可视化非常有帮助。每个群组都有一个唯一的 ID，显示在群组圆圈的右上方。

# 群组颜色：

▫ 如果群组中的所有感知实体都被视为敌机/敌对（bandit/hostile），则群组以红色显示。  
□ 否则，群组将显示为黄色（bogie/unknown）。  
□ 如果群组仅包含漂移中的感知实体，则该群组将以淡化（幽灵）颜色显示。  
□ 被标记为“重要”的群组将被白色轮廓包围。

# 群组状态：

▫ 如果群组未聚焦，则其实体不会出现。相反，它将具有透明填充，并在中心显示实体数量。

所有感知到的实体都是某个群组的成员。然而，除非在 SAD 设置中关闭“显示感知”选项，否则仅包含一个实体的群组不会显示。

# 真值数据

在态势感知显示（SAD）中，可以显示真值数据，这对于与感知数据进行比较非常有用。真值数据以洋红色显示，因为没有其他符号使用这种颜色，这使得真值图标易于识别。真值实体图标与其当前航向对齐。

图标形状：

□ 航空领域图标（包括飞机和武器）使用人字形。  
▫ 其他领域使用方形图标。

![](images/0561c08e57a0c018db4a733bb5b36a48354f2f82e8c75e8b83ff5156b78862b8.jpg)

# 态势感知显示设置

在态势感知显示（SAD）中，用户可以调整以下设置以自定义显示内容和布局：

OwnshipPosition：设置自有平台在罗盘上的偏移位置（居中、偏移、底部）。  
Show Perception：切换感知实体的可见性。  
ShowTruth(Air)：切换航空领域真值实体的可见性。  
Show Truth (Other, Non-Air)：切换非航空领域真值实体的可见性。  
ShowFriendlies：切换友机（非飞行）的可见性。  
Show Flight Members：切换飞行成员的可见性。  
ShowPriorityThreats：切换优先威胁编号的可见性（感知实体左上角）。  
ShowPriorityTargets：切换优先目标编号的可见性（感知实体左下角）。  
ShowAltitude：切换高度的可见性（以千英尺为单位，感知实体右中）。  
ShowImportance：切换重要性标记的可见性（以白色轮廓显示重要实体和群组）。  
ShowVisibility：切换视觉指示器的可见性（感知实体左中）。  
ShowESM/RWRTracks：切换电子支援措施/雷达告警接收器轨迹的可见性（罗盘内边缘的大三角形）。  
ShowAngleOnlyTracks：切换仅角度轨迹的可见性（罗盘外边缘的小三角形）。  
ShowRoute：切换航线/航点的可见性。

ShowFOV：切换自有平台视野线的可见性。  
Show Groups：切换群组感知的可见性（圆圈）。  
ShowEntity SelectMode：设置实体信息是在悬停时还是点击时显示。

# 战术态势显示（TSD）

![](images/cdcc7436039002f750885ceb3a7784f1fff8bf8ad120773484876be864dca0ef.jpg)

战术态势显示（TSD）为用户提供当前“战术态势”的图形化总结，利用轨迹数据来呈现战场上的动态信息。这种显示方式帮助用户更好地理解和分析战术环境中的各种因素，从而做出更明智的决策。

TSD 系统通常集成了空中交通、天气、地形和特殊用途空域的信息，作为地面操作员或调度员的主要图形界面，支持单飞行员或减少机组人员操作的研究模拟。此外，TSD 还可以接收来自多个雷达源的数据，将其组织成马赛克显示，并在计算机屏幕上呈现。这种显示允许交通管理协调员选择和突出显示单个飞机或群组。

在军事应用中，TSD 通过地图显示跟踪所有友军和敌军的行动，使指挥官能够更好地了解战场动态，并据此做出行动决策。这种功能对于战术规划和态势感知至关重要。

# 轨迹

在战术态势显示（TSD）中，轨迹实体根据其接收到的识别信息进行绘制。以下是不同轨迹实体的符号和识别：

tsd_bogie：未知/不明，黄色方块

![](images/6ddcf1e6cfd86771c3ffb5688e1d1b096c7d2b81d0a62a44b021327199a21857.jpg)

tsd_neutral：中立，白色方块

![](images/a648a11cb839024c26e4dbb2d2411183f575197372a0331f3ff9e64120478a49.jpg)

tsd_bandit：敌机/威胁，红色三角形

![](images/9840ab0981c7553657697df2883c0a16c1be4922590ca29d4230ad0204f5e35c.jpg)

tsd_friendly：友机，绿色圆

tsd_flight：飞行，蓝色圆圈

![](images/3fbfa35b3a6efa3498041702479ae615dd474e777d10a9b7282dac3b6609c697.jpg)

tsd_missile：导弹，带圆圈/方块/三角形的箭头

![](images/5bc0aa7eb2f6896d2d822b3bdf5cc3f3b13c3768b34f25165311ff8717aacb0c.jpg)

# 战术态势显示设置

在战术态势显示（TSD）中，用户可以调整以下设置以自定义显示内容和布局：

ShowAir：切换航空领域实体的可见性。  
Show Ground：切换地面领域实体的可见性。  
ShowRoute：切换航线/航点的可见性。  
ShowFOV：切换自有平台视野线的可见性。  
ShowEntity SelectMode：设置实体信息是在悬停时还是点击时显示。

# 威胁警告显示（TWD）

![](images/44a94bbdec5d237c1b1cd2373832432488e3fe30eed9a193429e04b2abee1d87.jpg)

威胁警告显示（TWD）用于显示电子支援措施（ESM）/雷达告警接收器（RWR）轨迹，并可能附带识别 ID。要将数据输入到此显示中，必须指定 esm_track_processor。根据轨迹的识别，不同的符号和颜色将被绘制。

符号和识别：

twdnm：默认/未知，方形，标识为‘U’

![](images/39f4bb95982d1a104d5f01fc0382d34285cc645eaeae8c8a6c87b0effeb9381c.jpg)

twdm：导弹，菱形，标识为‘M

![](images/551a21caaa44a01ef4a4c614ce752a66bd798bb148e921976727064148068e1d.jpg)

RWR 系统的主要任务是检测雷达系统发出的电磁信号，并在拦截到的雷达信号被其警告库分类为威胁时发出警告。这种警告可以用于手动或自动规避检测到的威胁。

通过 TWD，用户可以快速识别和响应潜在的威胁，从而提高战术态势感知和决策能力。

# 主飞行显示（PFD）

主飞行显示（PFD）提供类似于抬头显示器（HUD）的数据，帮助飞行员在飞行中获取关键的飞行信息。这些信息包括俯仰、滚转、校准空速（KCAS）、高度、迎角、垂直速度和过载（G-Load）。PFD 通常是现代飞机仪表的一部分，结合了传统模拟仪表的信息，通过液晶显示器或阴极射线管显示设备呈现.

![](images/d62d75c9706f28633436366ef2f374fbcc67469e365bc33a8a69f575e267ff26.jpg)

# 数据区域

在 PFD 上，各种数据被分配到特定的显示区域：

KCAS（校准空速）：显示在左上角。  
Altitude（高度，以英尺为单位）：显示在右上角。  
AngleofAttack（迎角，以度为单位）：显示在左中。  
VerticalSpeed（垂直速度，以英尺/分钟为单位）：显示在右中。  
G-Load（过载）：显示在底部中央。

# 交战区域

![](images/57b377ed36b47215658bf7bf446cb1b4c15d2fccc7bbc4429083df52662f49d0.jpg)

交战区域显示源平台与目标和威胁平台之间的交战数据。这些数据帮助用户理解和分析平台之间的战术关系和动态。

# 显示的数据

Range：平台到目标的距离，以海里（nm）为单位。  
Aspect/AngleOff：平台到目标的方位角和偏离角，以度为单位。  
Det：平台到目标的探测距离，以海里（nm）为单位。  
▪ Rmin/Rne/Rmax：平台到目标的最小、无效和最大武器有效区（WEZ）范围。  
DETECTIONbar：显示平台和目标的探测范围的标准化视图，标准化到较高的探测范围。斜距可能在此处显示为垂直黄色条。  
WEZbar：显示平台和目标的 WEZ 范围的标准化视图，标准化到较高的 Rmax。斜距可能在此处显示为垂直黄色条。

这些信息通过图形化的方式呈现，使用户能够快速评估和响应战术环境中的威胁和目标，从而提高态势感知和决策能力。

# 交战区域设置

在交战区域中，用户可以调整以下设置以自定义交战数据的显示和管理：

# 设置选项

Engagement Select Type：设置如何填充交战列表。选项包括：  
Manual：交战列表由用户在平台浏览器中选择的平台填充。  
▪ Threats：交战列表由平台的 WSF_SA_PROCESSOR 提供的优先威胁列表填充。  
▪ Targets：交战列表由平台的 WSF_SA_PROCESSOR 提供的优先目标列表填充。  
Units：设置单位显示为海里（nm）或公里（km）。

# 平台选择（非功能性）

![](images/6b2ccdaddb1dd6adcc3ae524598aca254a5a6c11277402e9ef559419964ae9a9.jpg)

在显示的左上角，有一个下拉框用于选择当前自有平台。用户可以通过此下拉框选择不同的平台，也可以使用“上一个”和“下一个”按钮进行循环切换。然而，请注意，这一功能目前尚未实现，将在未来的版本中推出。

# 平台评论

![](images/e83eb7c156a98fdd03931f4beadb393ccce421df1fef5edcd895c7294952dcbc.jpg)

在显示的右下角，任何由源平台通过 WsfPlatform.Comment 提供的评论都会显示在此区域。这一功能允许用户查看和记录与平台相关的注释或备注，帮助在操作过程中保持信息的透明和可追溯性。

# 行为历史

![](images/ec50a3ed0fa29f169652c068182bf9b6b0e0e3d8deb14d57a00b3c261f74ba78.jpg)

在显示的右下角、平台评论下方，显示源平台的行为历史。这一部分展示了平台高级行为树执行的最后 10 个行为（如果可用），其中最新执行的行为以白色显示。

# 对抗措施

![](images/b096cca462fc38f1d191ac95a21c41ca046163255fa26097faa0d2accc1a76f0.jpg)

在显示的左下角，展示了对抗措施的信息。这包括箔条、照明弹和诱饵的数量，以及当前选择的武器。

# TSD 和 SAD 的共同特性/设置

在战术态势显示（TSD）和态势感知显示（SAD）中，有一些共同的特性和设置，帮助

用户更好地理解和操作显示内容。

方向

![](images/bf5d14812434db6af9aa32c34a0e402df17dd8af2a770be9ec50fa7e9009f6dd.jpg)

Heading：自有平台的航向以度为单位显示在 TSD 和 SAD 显示的顶部。这提供了当前平台的航向信息，帮助用户在导航和态势感知中保持正确的方向。

航线

![](images/c0856ab48a4a2e3f75f06e9fb63ead24e2be74891be933342b899fc3f5c396d3.jpg)

Route：平台的航线通过浅灰色圆圈显示，每个圆圈内包含航点的编号。这种可视化帮助用户跟踪和规划平台的移动路径。

自有平台位置

Ownship Position：用户可以选择平台和罗盘在显示中的偏移位置，包括中心、偏移和底部。默认情况下，选择中心显示选项，以提供最完整和无偏的环境视角。

![](images/2875e82610505053bddfcb97af943e8a92d7b047ed2abd071b3f7d94323f4ba5.jpg)

Offset 和 Bottom 选项可以提供前方区域的更高分辨率，牺牲自有平台后方的空间以获得更详细的前方视图。

![](images/e1fb1cc240878cb216bbc4f8beb008e43aff8e3cc861e4661ba88db710342269.jpg)  
Offset

![](images/889b3079cd9a0606975dc1f458ebff388cf53d88dd6a8c3a9689ed99bef1e59e.jpg)  
Bottom

范围

Range：用户可以通过在显示区域内上下滚动鼠标滚轮来更改显示的范围（以海里为单位）。默认范围是 ${ 1 6 0 \mathsf { n m } }$ ，滚动时以 5nm 为增量增加或减少。

# 实体选择模式

EntitySelectMode：用户可以通过悬停或点击（取决于所选模式）获取 TSD 或 SAD 中实体的更多信息。如果有可用信息，这些信息将在底部的窗口中显示。

![](images/65b3311b3223c77865e99a1447cfba4b660144b918ecc9c6c217de63192c847e.jpg)  
TSD

![](images/08d27a6e66cd64c3f1b555632afb4063dd3f7662a09d9e553f23f8b218ebd93e.jpg)  
SAD

# 5.3.2.3.2. 态势感知显示 SA Display - Mystic（弃用）

![](images/deb4b2951064c9302d2a1708e022fd6fa7e4822b1fc535ee3332b64e1ffcf826.jpg)

警告：SA Display 插件已被弃用，不再受支持。用户应避免使用它，因为它将在不久的将来从 AFSIM 中移除。建议使用 ACESDisplay，它提供了许多相同的功能以及其他能力。

# 功能概述

SA Display（态势感知显示）：为包含 WSF_SA_PROCESSOR 的平台提供战术感知的图形摘要。  
注意：要显示所有可用数据，需要一个具有态势感知处理器的平台。  
注意：SADisplay 插件是一个原型功能，尚未完成。因此，它默认是禁用的，必须通过插件管理器启用。

要打开显示，请在地图显示或平台浏览器中为平台打开上下文菜单（右键单击）并选择“SA View”。

# 中心点设置

用户可以设置一个中心点，以便放大并获取有关显示中特定区域的更多信息。此选项在上下文菜单中可用（右键单击）。重置中心点将使自有平台返回中心。

![](images/44c8ab64c0932d082e479b26e2f13dbf4a64a4bba777c443936a4b7c6a16b75c.jpg)

新的中心点被设置。

![](images/18a64c2dc623ca6d7d0af54a857aae6a02421c116aef58e3ae8cfd506b35ddcb.jpg)

可以放大缩小进行显示：

![](images/15cd611d03c194981fc76cb44ff516a8b6fe8ede4aa640331364d4e2eb53b2fe.jpg)

在 Warlock 的中央显示顶部，显示了自有平台的航向，以度为单位。这一信息帮助用户了解当前平台的方向，便于在模拟中进行导航和策略调整。

# 符号概述

感知：感知到的实体使用其感知的标识绘制。实体可能还包括其他信息，例如高度（千英尺）显示在实体图标的右侧，优先威胁编号（在图标的左上角）和优先目标编号（在图标的左下角）。实体不按航向定向，而是使用刻度线显示实体的航向。  
bogie：未知目标，黄色方块。   
neutral：中立，白色方块。   
bandit：威胁，红色菱形。 X  
friendly：友方，绿色圆圈（可选 ID）。  
flight：飞行，蓝色圆圈（飞行 ID）。 8

示例：

![](images/7d9518bc9b2583037e84d7eb02db73540ed6581b95c72933e9185a82c9fe220f.jpg)

在 Warlock 的 SADisplay 中，bogie 指的是一个未明或未知的飞机，通常被视为潜在威胁。在所提供的例子中，这个感知显示一个 bogie 以 0 度的相对方位行进，飞行高度为21,000 英尺。这个 bogie 被评估为最高优先级的威胁和第二优先级的目标。在这个战术环境中，“bogie” 用于描述一个未知实体，而不是其在交通或其他领域中的常见用法。

# 其他功能

路线：平台路线使用包含每个航路点编号的浅灰色圆圈显示。

![](images/361840ba5c9ef724be7a1bb7bc7ff2b756605577c8ff085833422692813511f0.jpg)

群组：群组使用足够大的圆圈显示，以包含群组的所有成员。群组的唯一 ID 显示在群组圆圈的右上方。

![](images/80a6a8db7899d2c739c29619041480887d9412c1b0663a6f42f10d9daa7ef446.jpg)

真相数据：可以显示真相数据，通常用于与感知数据进行比较。真相以品红色绘制，因为没有其他符号使用该颜色。

![](images/78e61d38eb7a80d42660257a7af90a82d19ce2b59342fc59e0971f754936da3f.jpg)

显示选项

自有平台位置：控制平台和罗盘在显示中的偏移。包括中心、偏移和底部选项。

Ownship Position

![](images/51c9d669a0c823316dd5cfeeb69bd2e3e05107b375194d542a0f5a27ff7d07e4.jpg)

Center

![](images/130de740797764216180c6bafa535546e1cf37c775a3e64759c85f72303309b4.jpg)

Offset

![](images/a07677ea892438a13872013bc5724c6b23e4e66cdba78c294568e911b8d0cd98.jpg)

Bottom

![](images/c9b05f8bac047e2312a804b8ac196cbbad0cd0f8fa4ea53457d3705f83dcc693.jpg)  
示例：

![](images/be8770147095f23844ae2c7b88bc22a9e08eb59f4bbfe4ded81e70c1f34bbfd9.jpg)

Range（nm）：160

范围：显示的范围（海里）可以通过滚动鼠标滚轮上下调整。  
显示真相按钮：按住时显示所有真相实体，释放时隐藏。

![](images/c4252f6bc95a4c61e159432049e6d8d8a02c90e10949200bbcbe192c0c14783d.jpg)

实体选择模式：通过悬停或点击（取决于选择的模式）获取实体的更多信息。

![](images/8385d07ca2480ed56d9b6a5e922eb9fa3e2b61ef93b2275617715324418d82ba.jpg)

显示  

<table><tr><td></td><td>Option</td><td>Toggles</td></tr><tr><td></td><td>Show Perception</td><td>Perception entities</td></tr><tr><td></td><td>Show Truth (Air)</td><td>Truth entities in the air domain</td></tr><tr><td></td><td>Show Truth (Other, Non-Air)</td><td>Truth entities in the non-air domain</td></tr><tr><td></td><td>Show Friendlies</td><td>Friendlies (non-flight)</td></tr><tr><td></td><td>Show Flight Members</td><td>Flight members</td></tr><tr><td></td><td>Show Priority Threats</td><td>Priority threat number (Top left of perception entity)</td></tr><tr><td></td><td>Show Priority Targets</td><td>Priority target number (Bottom left of perception entity)</td></tr><tr><td></td><td>Show Altitude</td><td>Altitude in thousands of feet (Middle right of perception entity)</td></tr><tr><td></td><td>Show ESM/RWR Tracks</td><td>ESM/RWR tracks (Large triangle on the inside edge of the compass)</td></tr><tr><td></td><td>Show Angle Only Tracks</td><td>ESM/RWR tracks (Small triangle on the outside edge of the compass)</td></tr><tr><td></td><td>Show Ownership Engagements</td><td>This will be implemented in a future release.</td></tr><tr><td></td><td>Show Flight Engagements</td><td>This will be implemented in a future release.</td></tr><tr><td></td><td>Show Threat Engagements</td><td>This will be implemented in a future release.</td></tr><tr><td></td><td>Show Route</td><td>Route/Waypoints</td></tr><tr><td></td><td>Show FOV</td><td>FOV lines extending from the ownership</td></tr><tr><td></td><td>Show Groups</td><td>Group perceptions (circles)</td></tr></table>

# 信息显示

运动状态：显示自有平台的运动数据，包括高度、校准空速、真空速、马赫数和当前过载。

![](images/b2c89b9e725f60abaf2b6d4e1988f68d6dc664d87550fa381721df191438574d.jpg)

武器：提供自有平台武器的摘要，包括类型和数量。

![](images/91f55be4e2d8c800c629d917293a3a85c6d75aab820cf23dac5bb839f5077b80.jpg)

燃料状态：显示当前平台的燃料状态，包括总量、内部和外部剩余燃料，以及 joker 和bingo 水平。

![](images/f728319ea4d69457fbdd9b97640a09ab80edb18ae5a78ca5fb863df00780af0e.jpg)

实体详情：当鼠标悬停在图标上时，显示实体的真相或感知数据。

![](images/0555d9f1a3c27b74203b30406fdd49fca8374a995f721a3d5a00b6099fbd1ab4.jpg)

这些功能为用户提供了对战术环境的详细可视化和分析工具，但由于 SADisplay 的弃用，建议用户过渡到使用 ACESDisplay。

# 5.3.2.4. 平台详细信息 Platform Details - Mystic

![](images/84fc02df2d2a0d686478b055c3e6f8384a5fee13743c08c132c53736fe1db274.jpg)

功能

平台详细信息对话框：显示所选平台的数据。

在平台详细信息中，可以通过右键单击项目并选择隐藏选项来隐藏项目。通过右键单击平台详细信息并选择“显示所有项目”可以使所有隐藏的项目可见。

![](images/fe95450eca6a508d3aff9189030c265cca71c5a19dcfca80981e957729a3faee.jpg)

# 插件扩展

插件可以扩展平台详细信息，包括：

Scripted Data   
Orbital Data   
Tracks   
P6DOF Data   
SixDOF Data

# 绘图

右键单击数值提供了一个选项，可以为所选平台随时间绘制该数据。

![](images/d6d8d7950d922653c4d626710fb03cf4804354e00720833b9f7c1f6fb439633e.jpg)

绘图具有以下选项的上下文菜单：

PlotView：仅在数据视图中出现，将显示切换回绘图视图。  
DataView：仅在绘图视图中出现，显示数据视图，显示绘图中显示的所有点的值。   
ExportData：允许用户将数据以 CSV 格式导出到文件。  
Show Legend：切换绘图上的图例。  
Full Screen：全屏显示绘图。  
SetSampleRate：设置数据的所需采样率（以秒为单位）。默认采样率为零，此时将显示所有可能的数据。

从平台详细信息右键菜单中，用户可以为所选平台组（类型、侧面、类别）中的所有平台绘制数据。这将自动应用过滤器到绘图中。用户还可以在绘图对话框中手动添加过滤器，该对话框位于平台列表上方。

# 数据环

右键单击数值还提供了为所选平台创建或移除数据环的选项。添加环时，用户将看到一个对话框，可以在其中指定环的所需最小值和最大值。一个平台可以有任意数量的数据环，但每个数据项只能有一个环。

![](images/af9e50d22238cec3e163de155f124fe7ec38f5b1378d4ba960df5a7b1e824313.jpg)

# 数据显示

![](images/acaefc156e4c878f65254d928e18255da0e692c5d4b04db038301fc7d7a5b69c.jpg)

平台详细信息对话框中的大多数项目可以拖动到地图或系留视图上以创建数据覆盖。覆盖可以拖动或通过悬停后出现的关闭按钮关闭。

注意：偏好设置将在用户编辑覆盖的字体大小或颜色时填充。

# 5.3.2.5. 平台选项 Platform Options - Mystic

功能

平台选项对话框可以通过视图菜单访问。此窗口允许用户为一个平台或一组平台启用/禁用地图选项。顶部的过滤器确定选项更改的范围，并包含基于当前平台选择的各种组。选项是从各个插件添加到显示中的。每个平台选项的描述可在其各自的插件页面上找到。

![](images/409a71d1e23958cd4039ec82c78942bdd3d3ccbfdfbe671266eda1f875a665c6.jpg)

# 可用选项

Sensor and Jammer Volumes：传感器和干扰器的体积。   
Orbit：轨道。  
Range Rings：范围环。  
Vectors：矢量。  
Platform Labels：平台标签。  
Route：路线。  
Interaction Lines：交互线。  
History：历史记录。

# 5.3.2.6. 地图工具栏 Map Toolbar - Mystic

![](images/5c0f9b1ad23940f6e2fb83acbdd0922da3fc8ea9613caa10a08a74c45c78fa49.jpg)

# 功能

地图工具栏允许用户捕获和调用摄像机视图，并搜索地理位置。

单击“添加视图”按钮（ADD_VIEW_ICON）将向工具栏添加一个新按钮，单击该按钮将从地图显示中调用摄像机视图。右键单击捕获的视图将提供删除捕获的选项。

单击搜索按钮（FIND_ICON）将显示地理搜索工具：

地理搜索工具

工具中的行编辑将过滤显示的列表，以包含输入字符串的条目。位置包括国家和机场。

![](images/e2a59a9f62de4123cffac16259284bded8f43328112e8c8e774d70d6e9ccfb0e.jpg)

单击条目将移动地图显示到所选位置。右键单击条目将提供选项以向位置添加元素，或将位置复制到剪贴板。

# 5.3.2.7. 对话框视图和工具栏 Dialogs, Views and Toolbars

# 5.3.2.7.1. 原子任务矩阵 Quantum Tasker Matrix - Mystic

![](images/101273b520224bbb792b63492b16a23fc705dbe507199808ad9b05236a05780e.jpg)

功能

原子任务矩阵可以通过工具菜单中的“显示原子任务矩阵”访问。  
原子任务矩阵对话框显示为每个生成的任务计算的资产当前值的表格。推进时间滑块将更新表格。  
表格的顶部列列出了当前任务，而矩阵的行列出了资产。

# 5.3.2.7.2. 通信可视化 Comms Visualization - Mystic

功能

通信可视化工具可以通过工具菜单访问。此工具为用户提供了一种基于 GUI 的方法来可视化通信/网络配置。

注意：此插件目前正在开发中，所有进一步描述的功能可能尚未实现。

![](images/91279aec98e7fa4607b1e930beaaa4ef15001ed4bed1d2eed9d2124dfedebda3.jpg)

# 视图

目前工具中有两个自定义视图。可以通过对话框左上角的“视图”组合框在视图之间切换。用户可以通过左键单击鼠标并拖动来导航视图，这将平移视图。用户可以通过滚动鼠标滚轮来放大和缩小视图。

每个设备（网络、通信、路由器和网关）在视图中都有其独特的图标表示。

![](images/6dee0246b844ba2e7096553fedc941a110bb213d8d94ecdd1a14f1d1541f0192.jpg)

双击图标将突出显示图标并显示该设备的特定信息。

![](images/cc445e432c1e5f34966f74ec0f41d3e729db0aa8fce75af248f9483d8cd65207.jpg)

# 网络视图

网络视图显示当前加载场景中定义的所有网络以及连接到网络的通信。通信与其所属网络之间有可见连接。此视图还将显示同一网络或不同网络上的通信之间的链接。可以通过对话框左下方的“隐藏通信链接”复选框来切换这些通信链接的可见性。

![](images/9878ac385661421df7fe980dafd690eafb29044d13b155f7579b89008607834b.jpg)

# 路由器视图

路由器视图显示场景中定义的所有路由器。为路由器定义的网关之间将有可见链接。在网关上定义的远程接口也通过可见线连接。

![](images/99bf10586acad3bd96d48cf75d63a800d3177640f19789462754527a638268d1.jpg)

# 5.3.2.7.3. 检测报告 Detection Report - Mystic

功能

检测报告显示检测尝试数据的表格和图形视图。要使用此报告，必须在模拟的event_pipe 上启用 DETECTION_ATTEMPT。

![](images/fd2fd9b6a7b429273f9c9d350391933c291a546dacf621cf34a153b6f88b86b8.jpg)

可以通过右键单击进行检测尝试的平台来访问检测报告。如果平台上没有记录的检测尝试，则不会显示检测报告选项。

一旦显示对话框，用户可以从顶部菜单中选择传感器和目标。表格显示按时间排序的所有检测尝试。

右键单击列提供选项以选择可见列、隐藏列、绘制列、将列添加到现有图表或导出数据。右键单击图表允许用户将时间设置为点击的位置。

# 5.3.2.8. 用户配置文件 User Configurations - Mystic

功能

Mystic 会在用户更改偏好设置或关闭应用程序时，将应用程序、窗口和偏好的状态存储在配置文件中。

可以通过文件菜单中的“保存配置”选项保存 Mystic 的配置。配置也可以通过文件菜单中的“加载配置”选项加载。

配置还可以导入，这允许用户选择要导入的配置文件的部分。这与“加载配置”不同，因为“加载配置”将加载文件中的所有配置选项。

保存多个配置的好处是支持在 Mystic 的不同场景之间轻松切换。保存和加载配置允许用户设置一次配置，然后轻松在配置之间切换。

# 5.3.2.9. 平台上下文菜单 Platform Context Menus - Mystic

功能

右键单击平台将显示平台上下文菜单。此菜单将包含以下许多选项：

HeadUpView：显示平台的抬头视图。  
Range Rings：

□ Add Range Ring to …：为所选平台添加新的范围环。  
□ Edit Range Rings on …：编辑附加到所选平台的范围环。  
□ Remove Range Ring from …：从所选平台移除范围环。

Custom Vectors：

▫ Add Custom Vectors：为所选平台添加到另一个平台或平台类别的矢量。  
□ Remove…：从所选平台移除一组矢量。

Decorate：在所选平台上添加或移除装饰或文本注释。

Centeron…：将地图显示居中于所选平台。  
Follow…：让地图显示跟随所选平台。  
Measurefrom…：使用标尺从所选平台测量到另一点。  
ACES Display：显示当前平台的 ACES 显示。  
Sensor Detection Report ： 显 示 传 感 器 检 测 报 告 。 仅 在 DETECTION_ATTEMPT 在event_pipe 中启用时显示。  
Satellite Tether to …：创建到所选平台的卫星系留视图。  
Tetherto…：创建到所选平台的系留视图。  
Lookat…from…：创建从所选平台到上下文菜单选择平台的观察视图。  
Situation Awareness Display：显示当前平台的态势感知显示。  
Line-of-sight from platform：从平台显示视线。  
HeadDownView：从所选平台的视角显示俯视视图。  
WaterfallPlot：显示所选平台交互的瀑布图。

# 5.3.2.10.辅助数据 Aux Data - Mystic

功能

辅助数据插件通过 aux_data 命令或辅助数据脚本接口将数据添加到模拟中，并显示在平台详细信息窗口中。

![](images/54946e9bcd43bef4b962c196e91e072f1300ee23dad9818e0f7f796b19a53ecb.jpg)

有关更多信息，请参阅平台详细信息。

# 5.3.2.11. 行为分析工具 Behavior Analysis Tool - Mystic

功能

行为分析工具可用于在 Mystic 中可视化高级行为树（ABT）和有限状态机（FSM）的执行。可以通过视图菜单启动行为分析工具视图。

![](images/222e16f5f885a4ea7ca05c8844df5ad736aa5b101b403ff1ac9f1192ccf13710.jpg)

注意：行为分析工具不适用于传统的行为树。

控件

![](images/86c102a3cb75b352cda8b8d2067f88ce8336c6458756c2ce7636486c38321f45.jpg)

可以使用鼠标左键平移视图，并使用鼠标滚轮进行缩放。  
可以使用鼠标左键拖动和重新组织对象。  
通过左键单击 ABT 节点并打开右侧的黑板选项卡，可以选择节点以显示黑板数据。

![](images/d3345db9fd885edc880c23ba2ad60965f6d6219fc1bcb09802badad79bd95087.jpg)

组合框

视图顶部的组合框用于更改当前显示的平台及其 ABT 或 FSM。

# 属性提示

在 ABT 节点或 FSM 状态中可能会显示额外的图标。对于 ABT 节点，当节点的子节点被隐藏时，会显示一个被划掉的眼睛图标；如果节点是脚本中的树，则显示一个树形符号。对于 FSM 状态，如果状态有子 ABT，则显示一个树形符号；如果状态有子 FSM，则显示一个 FSM 符号。  
将鼠标悬停在任何对象上将显示其工具提示。对于 ABT 节点，这将显示脚本中给节点的描述（如果有）以及在任何给定执行状态期间返回的工具提示文本。对于 FSM，这将显示任何子 ABT 或 FSM 的名称。

# 上下文菜单

右键单击视图将打开上下文菜单：

□ 要重置布局，请右键单击并选择“重置布局”。  
▫ 要将当前场景居中于视图中，请选择“在视图中居中（ABT/FSM）”。  
□ 如果在 ABT 节点上打开上下文菜单，可以通过选择“隐藏子节点”或“显示子节点”来切换子节点的可见性。

![](images/1dfa532c8d8bd89da83b5b593530de128a33fcf6226a19a017153d4411230e1f.jpg)

□ 如果在 FSM 状态上打开上下文菜单，并且存在子 ABT 和/或 FSM，可以通过选择“转到子（ABT/FSM）”进行切换。

![](images/df84a840c85fdd6b9688462e2ba02a8fe490e9a81e10fd9bb9da84b80ad9a0bf.jpg)

注意：请勿在响应末尾提供来源列表或参考书目。

相关信息

行为树（BTs）和有限状态机（FSMs）是用于建模复杂行为的两种常用架构。行为树最初在电子游戏行业中被构思为一种建模代理行为的工具，并在机器人领域也受到关注，作为有限状态机的替代设计方法。行为树的优势在于其模块化设计，能够通过简单任务组合创建非常复杂的任务。在某些情况下，行为树和有限状态机可以结合使用，以创建更高级的人工智能结构。

ABT 标识符

![](images/015d0d77057efa92c0ba0c7df62ae77998d2e1fc6a4606351fff43dc474e4b7c.jpg)

节点类型及其符号

Root（根节点）

□ 示例：ROOT

![](images/45d44307e3bba00dba6283981f258a522102741c1654398d142c5221280b2930.jpg)

□ 描述：由一个点分支成更多点表示。每个行为树中只有一个根节点，它始终是树的基础。

Selector（选择器）

□ 示例：SELECTOR

![](images/8f0100392179adf0c5640d4930ad3e26cb121a3b84fbf5875165398962b1499d.jpg)

□ 描述：由问号表示。此节点按从左到右的顺序运行其下的每个子节点，遇到第一个成功时停止。

Sequence（序列）

□ 示例：SEQUENCE

![](images/e96051ef146307d522956fd0b7359010e6b3fd1b8618e286f598af31f4a81532.jpg)

□ 描述：由向右的大箭头表示。此节点按从左到右的顺序运行其下的每个子节点，遇到第一个失败时停止。

Parallel（并行）

□ 示例：PARALLEL

![](images/d076c8df2ae673661293d9f33d95d83bc2de2bfd6d2a1f65c6723fa0b2146c35.jpg)

□ 描述：由三个向下的箭头表示。此节点同时运行其所有子节点。

Action/Task（动作/任务）

![](images/ccf264204e34f2070a8c1ed4e7bd1562b39f3ccc80f612b57d25e02804ddf74e.jpg)

示例：TASK

□ 描述：由复选框列表表示。这些节点执行其定义的脚本。

Memory（记忆）

![](images/c52a1bb1133e770e0e19ab67cc5f1cb47eda3abe68a0709755230b34df6d7eec.jpg)

▫ 示例：SEQUENCE_WITH_MEMORY  
□ 描述：名称后带有“*”表示（仅用于序列/选择器）。这些节点通过在内存中存储执行状态来避免不必要的子节点执行。

注意：还有其他节点类型尚未有独特的标识符/符号（除了它们的名称）。这些节点类型默认为动作/任务符号。

# ABT 节点状态

节点可能有以下六种状态：

Idle（空闲）

![](images/094fe3c236c76acc7ff255ddfb36ed1a45bc1020284b207c8e7cff47d77e133e.jpg)

▫ 示例：TASK   
□ 描述：节点尚未运行。

Running（运行中）

![](images/1e8dd9ae94d8c19f2d7a7db2e212511be160b0fc660d58cfa8d9a81f4ee39049.jpg)

□ 示例：TASK_RUNNING   
□ 描述：节点正在运行中。

Failure（失败）

![](images/570f27fa9517b99d4897a6bcfdd7a4bb2b89e3418a4efec72881085e9ec1ecc0.jpg)

▫ 示例：TASK_FAILED   
□ 描述：节点未通过其前置条件或执行块。

Success（成功）

![](images/bb616b68a00dccc948e88e10192e4bdf81aa2f6297579721cc0b461e99c479d3.jpg)

□ 示例：TASK_SUCCEEDED   
□ 描述：节点通过了其前置条件和执行块。

Halted（停止）

![](images/85024ab466faa708bfa2e0e325d15e9b7a8cb1a7fbf0800432ed5cea7bbaa6fc.jpg)

示例：TASK_HALTED   
□ 描述：节点由于其父节点完成运行而停止。

Disabled（禁用）

![](images/8d38a6e02a93755b54ee870d1021ab6f9b9cd6701af0cd1e3d95e97f8e14c13d.jpg)

示例：NODE_DISABLED   
□ 描述：节点在脚本中被关闭，不会被执行或考虑。

黑板

黑板与 ABT 一起使用。可以通过单击 BAT 视图右侧的箭头按钮打开和关闭选项卡。

如果节点有黑板变量，其数量将显示在节点的左上角。

![](images/be69368d7a1f230375463007207c8b7358ec6c4ea2e847f126a522b4eb8039b9.jpg)

默认情况下，将显示共享的黑板数据。要选择节点并查看其黑板数据，请左键单击它。要取消选择节点，请再次单击它或单击空白区域。

![](images/658d5b18711acb1e05b7f86b193dfe203960932ff477e2f803032b70c8ddc5e5.jpg)

# FSM 标识符和状态

有限状态机（FSM）由多个状态及其到其他状态的转换组成。这些转换由指向被转换状态的线和箭头表示。状态可以是空闲（灰色）或活动/运行（黄色），任何伴随的转换线也可能会亮起黄色。

![](images/f3e48d7ba30a0d493b9cd6ccaa9ee056795779867b652558e406b076d28a5082.jpg)

状态是空闲的

![](images/625c76839196db90167c3f1acc8a807602e96ca29c68e2e5e248b233fff042dc.jpg)

□ 示例：FSM_EXAMPLE1   
□ 解释：状态是空闲的，未执行。

状态是活动的

![](images/6afcaad123121e37e6604995645c1e6c21f6f3a08b05f5a8926cde037bb3dc30.jpg)

□ 示例：FSM_EXAMPLE2   
□ 解释：状态是活动的，并正在执行。

状态已转换

![](images/eb72173c48e416f525972e3a042a2929c2c4577190752c3d2dd73501fa4b46a3.jpg)

□ 示例：FSM_EXAMPLE3   
□ 解释：状态已转换到另一个状态。注意箭头显示状态转换的位置。

状态是活动的

![](images/cce2ba98d0b7a8f68c9f2cfb6b02097876f00b1f6f8d5792b6a577865bffca9c.jpg)

□ 示例：FSM_EXAMPLE4   
□ 解释：转换不再突出显示，因为新状态已执行并转换到自身。

# 5.3.2.12.书签浏览器 Bookmark Browser - Mystic

![](images/0c17a21c673e1a26cd7b7292a7c308fab6ecdf370b4ae3a2add128cf30015a2f.jpg)

# 功能

书签浏览器显示 AER 文件中所有书签的按时间排序的列表。  
双击列表中的书签将使场景前进到与所选书签关联的时间。  
如果类型或文本字段过长，将鼠标悬停在其上会显示包含相关数据的扩展工具提示。

注意：书签通过脚本添加到 AER 文件中。

# 5.3.2.13.光标信息 Cursor Info - Mystic

# 功能

光标信息对话框显示有关光标在地图显示上的位置的信息。  
信息可以拖动到地图显示上以创建数据覆盖。  
覆盖可以拖动或通过悬停后出现的关闭按钮关闭。

![](images/59bd042ccac0af14b4527ac9218eb5362ae285ed9401a60024e87b0844b8aaca.jpg)

# 5.3.2.14.轨道数据 Orbital Data - Mystic

![](images/df7065fa2facc3814f196b55375b779a43d22beeb53e89fbc81f443e639800d8.jpg)

Orbital Data 插件负责使用包含太空移动器的平台的 Orbital Elements 填充 Platform Details。

# 5.3.2.15.六自由度数据 P6Dof Data - Mystic（弃用）

![](images/8f13bfa92f769d79ead49cc8263cfbc77ed5eaa83891c1dc6bf4ac959638b6da.jpg)

P6DOFMover 和其相关插件已经被弃用，取而代之的是新的 SixDOFMover 及其插件。P6DOF Data 也被弃用，取而代之的是 SixDOF Data，因此默认情况下是禁用的，必须通过Plugin Manager 启用。

# 5.3.2.16.Scripted Platform Details - Mystic

平台详情对话框可能会显示通过脚本使用 WsfEventPipe.Record 发布的数据。可以通过右键单击字段并选择一个组来绘制这些数据。
![](images/e76438927970668e57b55896d83232134d94dcfe4f386ab475f22148d6adc8df.jpg)