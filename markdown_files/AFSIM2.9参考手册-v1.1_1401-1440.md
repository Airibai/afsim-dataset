![](images/e76438927970668e57b55896d83232134d94dcfe4f386ab475f22148d6adc8df.jpg)

# 5.3.2.17.瀑布图 Waterfall Plots - Mystic

![](images/0c7ca9e9099e2735c76931f6a9bda047e18d36f8329af076845a3d749c15e5b1.jpg)

瀑布图显示了针对选定平台、交互类型和交互者过滤器的交互活动时间。

可以通过右键单击平台访问瀑布图。显示对话框后，用户可以选择事件类型：

Detected- 显示目标平台被交互者检测到的时间段。  
Detecting- 显示目标平台检测交互者的时间段。  
SensorTracked- 显示交互者对目标平台进行传感器跟踪的时间段。  
SensorTracking- 显示目标平台对交互者进行传感器跟踪的时间段。  
LocalTracked- 显示交互者对目标平台进行本地跟踪的时间段。  
LocalTracking- 显示目标平台对交互者进行本地跟踪的时间段。  
Jammed- 显示交互者尝试干扰目标平台的时间段。  
Jamming - 显示目标平台尝试干扰交互者的时间段。

用户还可以选择对交互者应用过滤器。交互者可以按阵营、平台类型、类别或个人名称进行过滤。右键单击图表提供导出为 CSV 的选项。使用鼠标中键滚动可以在光标位置放大或缩小。

图表仅能识别在调用时已加载的数据。如果需要不同的时间段，可以调整时间控制器以捕捉感兴趣的区域，或更改内存偏好设置。

# 5.3.3. python 工具 PyMystic

PyMystic 是一个用于读取 AER 文件的 Python 模块。它完全用 Python 3 编写，无需额外的依赖。PyMystic 主要用于实验设计分析和 AFSIM 蒙特卡洛运行的批处理，也可以帮助 Mystic 功能的原型设计和自定义数据提取。

# 功能和兼容性

跨版本兼容性：PyMystic 使用嵌入在读取的 AER 文件中的模式（schema），这使得它可以与任何版本的 AFSIM 兼容，只要模式本身的规则没有改变。然而，由于不同版本的内容会有所变化，使用 PyMystic 编写的脚本不一定能跨版本兼容。

事件管道消息：事件管道消息的内容由创建文件的 AFSIM 版本的 event_pipe 页面记录。

# 使用方法

PyMystic 定义了一个 Reader 类，可以从事件管道文件中读取消息。一般来说，pymystic脚本的结构如下：

```txt
import mystic   
with mysticReader('somefilename.aer')as reader:#创建一个读取器 formsg in reader:#遍历AER文件中的每条消息 #在这里处理消息 pass
```

消息表示：消息以 Python 字典的形式表示，其中每个键都与一个值相关联。有些键的关联值本身可能是一个字典。

# API 文档

Reader 类：用于打开 AER 文件，生成模式，并允许读取消息。可以作为迭代器使用，按顺序生成加载文件中的消息。

方法：

_init__(filename, debug=False): 加载指定文件名的文件。

□ close(): 关闭加载的重放文件。  
□ process(msgdata): 将 MessageData 转换为消息。  
□ read(): 读取并返回加载文件中的下一条消息。  
□ scan(): 仅读取文件中下一条消息的头数据。  
▫ scan_iter(): 迭代器，遍历 AER 文件中的消息。

Schema 类：使用模式字符串生成本地模式定义。

# 示例脚本

example_message_list.py：输出时间和消息类型列表，当遇到实体状态消息时，还会写出相关平台的名称。

```txt
28797.0 MsgEntityState platformA  
28798.0 MsgEntityState platformB  
28798.0 MsgEntityState platformA  
28799.0 MsgEntityState platformB  
28800.001953125: MsgPlatformStatus 
```

example_graph.py：需要 graphviz 和 graphviz Python 模块，查询 MsgPlatformInfo 消息中的命令链关系，并将其渲染为 PDF。

![](images/ed049f220e3e15e2972b9e86404f9362eaedd4dd7f7e6e04b612bdbf45b1ec48.jpg)

example_bigreport.py：从包含 AER 文件名列表的本地 aerlist.txt 文件中读取，报告AFSIM 执行的版本和时间戳。

```txt
TESTING /AFSIM/test scenarios/scen1/scen1.aer  
***unversioned***  
TESTING /AFSIM/training/developer/labs/solution/comm/data/comm exercise.aer  
version: mission 2.4.0.190626  
executed: 2019-06-28 09:09:48  
TESTING /AFSIM/training/developer/labs/solution/comm/data/comm exercise2.aer  
version: mission 2.4.0.190626  
executed: 2019-06-28 09:09:52  
TESTING  
/AFSIM/training/user/basic/scenarios/solutions/11/Floridistan/output/jacksonabad.aer  
version: Warlock 2.5.0.191029  
executed: 2019-10-31 11:50:59 
```

example_print_message_data.py：演示递归处理由嵌套字典表示的消息。

```yaml
id: 1  
msgtype: MsgEntityState  
simTime: 0.0  
simIndex: 0  
state:  
    platformIndex: 38  
    damageFactor: 0.0  
    locationWCS: 
```

<table><tr><td>x:</td><td>-2356075.8866955335</td></tr><tr><td>y:</td><td>-3743698.25337908</td></tr><tr><td>z:</td><td>4579620.857159804</td></tr><tr><td>velocityWCSValid:</td><td>False</td></tr><tr><td>accelerationWCSValid:</td><td>False</td></tr><tr><td>orientationWCSValid:</td><td>True</td></tr><tr><td>orientationWCS:</td><td></td></tr><tr><td>x:</td><td>1.0090789794921875</td></tr><tr><td>y:</td><td>-0.7646905779838562</td></tr><tr><td>z:</td><td>3.1415927410125732</td></tr><tr><td>fuelCurrentValid:</td><td>True</td></tr><tr><td>fuelCurrent:</td><td>0.0</td></tr></table>

这些功能和示例展示了 PyMystic 在处理 AER 文件和进行数据分析方面的强大能力。

# 5.4. 事件读取工具 EVT Reader

概述

EVTReader 是一个应用程序，用于读取和显示 AFSIM 的 EVT 文件。EVT 文件包含以人类可读格式记录的带时间戳的事件。该工具将事件格式化为表格，并允许用户进行过滤和导出到新文件。

主显示

<table><tr><td colspan="8">AFSIM-EVT-Reader</td></tr><tr><td colspan="8">File</td></tr><tr><td rowspan="2">00:07:43.4</td><td>type</td><td>platform</td><td>interactor</td><td>thirdParty</td><td>5</td><td>6</td><td>^</td></tr><tr><td>SENSOR_REQUEST UPDATED</td><td>sr_sam_telar-1</td><td>target4</td><td></td><td>sr_sam_trr_rada...</td><td>TRACK</td><td>sr_sar</td></tr><tr><td>00:07:43.4</td><td>SENSOR_MODE_DEACTIVAT...</td><td>sr_sam_telar-1</td><td></td><td></td><td>sr_sam_trr_rada...</td><td>ACQUIRE</td><td>48:47:</td></tr><tr><td>00:07:43.4</td><td>SENSOR_MODE_ACTIVATED</td><td>sr_sam_telar-1</td><td></td><td></td><td>sr_sam_trr_rada...</td><td>TRACK</td><td>48:47:</td></tr><tr><td>00:07:43.4</td><td>OPERATING_LEVEL_CHANG...</td><td>sr_sam_telar-1</td><td>taskmgr</td><td></td><td>ENGAGE</td><td>1</td><td></td></tr><tr><td>00:07:45.4</td><td>OPERATING_LEVEL_CHANG...</td><td>sr_sam_telar-1</td><td>taskmgr</td><td></td><td>ENGAGE</td><td>1</td><td></td></tr><tr><td>00:07:45.4</td><td>OPERATING_LEVEL_CHANG...</td><td>sr_sam_telar-1</td><td>taskmgr</td><td></td><td>ENGAGE</td><td>1</td><td></td></tr><tr><td>00:07:45.4</td><td>TASK_ASSIGNMENT</td><td>type</td><td>sr_sam_telar-1</td><td>target4</td><td>sr_sam_telar-1</td><td>Shoot</td><td>sr_sar</td></tr><tr><td>00:07:45.4</td><td>WEAPON_FIRE_REQUESTED</td><td>sr_sam_telar-1</td><td>target4</td><td></td><td>sam</td><td>sr_sam_telar-1.2</td><td>2</td></tr><tr><td>00:07:47.4</td><td>LOCAL Track INITIATED</td><td>sr_sam_telar-1...</td><td>target4</td><td></td><td>sr_sam_telar-1...</td><td>00:07:47.4</td><td>00:07:</td></tr><tr><td>00:07:47.4</td><td>WEAPON_Fired</td><td>sr_sam_telar-1</td><td>target4</td><td>sr_sam_telar-1...</td><td>1</td><td>00:07:47.4</td><td>Laun</td></tr><tr><td>00:07:47.4</td><td>WEAPON_FIRE_REQUESTED</td><td>sr_sam_telar-1</td><td>target4</td><td></td><td>sam</td><td>sr_sam_telar-1.2</td><td>1</td></tr><tr><td>00:07:51.0</td><td>LOCAL Track INITIATED</td><td>sr_sam_telar-1...</td><td>target4</td><td></td><td>sr_sam_telar-1...</td><td>00:07:51.0</td><td>00:07:</td></tr><tr><td>00:07:51.0</td><td>WEAPON_Fired</td><td>sr_sam_telar-1</td><td>target4</td><td>sr_sam_telar-1</td><td>2</td><td>00:07:51.0</td><td>Laun</td></tr></table>

应用程序的主显示界面展示了一个表格，每行代表一个事件，事件的数据在列中显示。事件的时间显示在垂直标题中。前四列分别是事件类型、所有者或源平台、目标平台和第三方平台。并非所有事件都会填充所有这些列。更右边的列由事件的数据填充。当鼠标悬停在表格单元格上时，可以通过工具提示查看数据类型。当显示许多事件类型时，单个列可能代表许多不同的数据字段。即使对于单个事件类型，在 AFSIM 输出不同数量的值时，列也可能代表不同的数据字段。

# 过滤和导出

通过右键单击单元格，可以提供多种过滤选项：

Show when column ${ \sf X } = { \sf Y }$ - 应用过滤器以仅显示与当前列值匹配的事件。  
Hide when column ${ \sf X } = { \sf Y }$ - 应用过滤器以隐藏所有与当前列值匹配的事件。  
Create Filter - 对当前列应用自定义过滤器。  
Export - 将过滤后的数据导出到新的 EVT 文件。

![](images/c12dc70164f7b6ea65653aec6db72cf277cd06c7699f0587c60aad42552f549e.jpg)

显示界面的顶部部分显示当前应用的过滤器。右键单击这些过滤器可以：

RemoveRule- 移除光标所在的过滤规则。  
EditRule- 更改悬停的过滤规则。  
Clear Rules - 移除所有过滤规则。  
Save Filter - 将过滤规则写入文件。  
LoadFilter- 从文件读取一组过滤规则。

# 命令行

evt_reader 的命令行用法如下：

```txt
evt_reader [input.evt] [--filter filter.evt_filter] [--out output.evt] 
```

如果提供了输入文件，它将在启动时加载。  
如果提供了过滤器，它将在启动时应用。  
如果提供了输出文件，应用程序将对输入文件应用过滤器并将其写入输出文件。在这种情况下，应用程序不会显示。这可以与脚本语言一起使用，以快速对多个数据文件按顺序应用事件过滤器。

通过这些功能，EVTReader 工具可以有效地管理和分析 AFSIM 的 EVT 文件，提供灵活的过滤和导出选项以满足不同的分析需求。

# 5.5. 运动创建工具 Mover Creator

MoverCreator 是一个 AFSIM 软件工具，提供了一个方便易用的基于 GUI 的应用程序，帮助用户为空域移动物体创建 AFSIM 输入文件。通过自定义定义的基于图形的飞行器定义，用户能够为 AFSIM 模拟建模飞机、武器和引擎。MoverCreator 界面允许用户从现有的模板模型（由 MoverCreator 提供）创建新的自定义模型，或者编辑他们之前创建的模型。

# 功能模块

MoverCreator 包含多个模块，协助完成各种功能，包括：

修改飞行器几何/配置：调整飞行器的形状和结构。  
调整控制配置：设置和修改控制系统的配置。  
调节/修改自动驾驶仪参数：优化自动驾驶仪的性能。   
调整空气动力学：修改空气动力学特性以提高性能。  
分析飞行器性能：评估飞行器在不同条件下的表现。  
比较不同移动物体类型的性能：对比不同类型的移动物体的性能差异。  
▪ 在 AFSIM 环境中进行飞行测试：在模拟环境中测试飞行器的飞行性能。

# 支持的移动物体类型

MoverCreator 当前支持以下移动物体类型：

WSF_RIGID_BODY_SIX_DOF_MOVER：六自由度刚体移动物体。  
WSF_P6DOF_MOVER：六自由度移动物体。  
WSF_GUIDED_MOVER：制导移动物体。

这些模型可以单独生成，也可以同时生成。此外，对 WSF_BRAWLER_MOVER 感兴趣的用户可能会发现 Brawler 转换工具对于研究 WSF_RIGID_BODY_SIX_DOF_MOVER 功能非常有用。

MoverCreator 提供了一个强大的平台，帮助用户在 AFSIM 中创建和优化空域移动物体的模型，从而支持复杂的模拟和分析任务。

![](images/bf1af4fc46e6b4ab78f8ea56794e4872b0f2ae3b8fca774b94cdc3b5507c59e1.jpg)

![](images/d7f9b4ebb678ffd9da0d6ec2033eb0e4be8d974cded8cde3480e5008efc61895.jpg)

![](images/42de2fdc1bb2bf9ceea7b6c89c531461a3a3723162929c2a5247eef0e2e2e867.jpg)

![](images/879e3fe0edbc2589dd1035ceda160d5f73974fc4752f0e644a602ec92d8079d7.jpg)

# 5.5.1. 用户指南 Mover Creator User’s Guide

概述

MoverCreator 是一个 AFSIM 软件工具，提供了一个方便易用的 GUI 应用程序，帮助用户创建空域移动物体的 AFSIM 输入文件。用户可以通过自定义的图形化飞行器定义来建模飞机、武器和引擎，以便在 AFSIM 中使用。

核心功能

MoverCreator 引导用户通过线性、逐步的过程设计他们的飞行器或引擎。以下是该过程的描述：

启动对话框

![](images/581f1b20f085cb0df09217348f2ff9231e433f0fa4aa247954502cbeb60786e5.jpg)

初始选择：当 MoverCreator 首次打开时，用户可以选择开始设计飞机、武器或引擎。用户可以创建新模型或编辑现有模型。

创建新模型：选择“创建新飞机”会打开一个对话框，提示用户选择一个类型来派生他们的模型，并为新模型命名。用户可以对新模型进行更改，而不会影响原始模型。

![](images/ba4f66a341c2f23a5b2e1b0ce05e5c66edb80e4d9fbe53e8ab1d8d5004d14f4c.jpg)

![](images/ba704a100a0aeb3a130151bb199bc25df89a2bc2ae4d73a0b680280094b3d69c.jpg)

![](images/fd30b16362dce4e344ffc1aa6760036b8fb2e7c7c66e0af92790be1838a6448e.jpg)

编辑现有模型：选择“编辑现有飞机”会请求用户选择要编辑的飞机类型。更改将应用于所选的飞机模型。

WSF_BRAWLER_MOVER 转换对话框

在 Mover Creator 中，WSF_BRAWLER_MOVER 飞机的转换对话框与其他不同。与其逐个组件构建完整模型并通过典型的 MoverCreator 流程发送，MoverCreator 将飞机转换为WSF_POINT_MASS_SIX_DOF_MOVER，并允许用户进行进一步的调整。随着对六自由度（SixDOF）飞行器的支持扩展到点质量移动模型，这一流程可能在未来版本中更好地集成到Mover Creator 中。

启动对话框中的选项按钮

选项按钮：位于退出按钮左侧，允许用户指定输出 3D 模型以用于 AFSIM 场景的目录。用户还可以指定主题。

![](images/c0173b97c6b7f32bfb9d5bbbd8c3e8e4791e5489dc3624e05175392986e19031.jpg)

![](images/6b46e1f69dc82bda12b7576f3707aef1825df4031ad299ddd808f2f6ec4d9a69.jpg)

目录设置：

SiteDirectory：指定 .obj 模型文件的输出目录。包含模型定义块的 AFSIM 输入文件也将输出到此目录。  
OSGConvert 文件：用于将模型文件转换为 OSGB 或 IVE 格式，具体取决于在“首选 3D模型文件类型”下选择的格式。此格式通常是首选，但需要用户下载 OSG 并选择

osgconv 可执行文件。

主题设置：可以设置为浅色或深色。  
重置设置：将对话框中的所有设置恢复为默认值。  
关于/信息按钮：位于退出按钮右侧，点击后会打开一个对话框，显示版本信息和文档链接。

这些功能使得 MoverCreator 更加灵活和用户友好，允许用户根据需要自定义输出和界面设置。

# 应用程序流程

在使用 Mover Creator 进行设计时，建议用户先设计引擎，然后再进行飞行器设计。以下是详细的流程说明：

# 引擎设计

选择引擎：从启动对话框中选择要创建或修改的引擎，MoverCreator 将打开包含引擎设计器的“引擎”页面。  
引擎设计器：在此页面中，用户可以定义引擎的各个参数和特性。有关引擎定义过程的详细信息，请参阅引擎设计器页面。  
完成引擎设计：当用户对引擎设计满意后，可以开始飞行器的设计。

# 飞行器设计

<table><tr><td>Start/Setup</td><td>Engine</td><td>Geometry</td><td>Aerodynamics</td><td>Performance</td><td>Pilots/Controls</td><td>Autopilot</td><td>Flight Test</td></tr></table>

选择飞行器：从启动对话框中选择要编辑或创建的飞行器，MoverCreator 将打开所选飞行器的几何页面。  
几何页面：在此页面中，用户可以指定飞行器的几何形状。  
空气动力学页面：完成几何设计后，用户可以通过点击应用程序窗口底部的“空气动力学”选项卡或右下角的“下一步”按钮进入空气动力学页面。  
设计步骤顺序：飞行器设计步骤必须按特定顺序完成，因此用户只能导航到当前页面的前一页或后一页。每个页面在飞行器设计器和引擎设计器中都有详细说明。

# 输出

生成 AFSIM 输入文件：一旦完成所有步骤，Mover Creator 将输出 AFSIM 库可识别的飞行器定义。生成的 AFSIM 输入文件包含定义所需飞行器设计的块。  
定义块内容：这些定义块包括但不限于 P6DOF Mover、RB6DOF Mover、PM6DOF Mover和 GuidedMover 的平台类型、空气动力学、质量、推进和控制等数据。  
通过遵循这些步骤，用户可以有效地使用 MoverCreator 设计和优化飞行器和引擎，以便在 AFSIM 环境中进行模拟和分析。

<table><tr><td></td><td>P6DOF Mover</td><td>RB6DOF Mover</td><td>PM6DOF Mover</td><td>Guided Mover</td></tr><tr><td>Platform Type</td><td>platform_type</td><td>platform_type</td><td>platform_type</td><td>platform_type</td></tr><tr><td>Mover</td><td>mover</td><td>mover</td><td>mover</td><td>mover</td></tr><tr><td>Aerodynamics</td><td>aero_data</td><td>aero_data</td><td>aero_data</td><td>aero (aspect_ratio, cl_max, mach_and_cd)</td></tr><tr><td>Mass</td><td>mass_property</td><td>mass_property</td><td>mass_property</td><td>total_mass, fuel_mass</td></tr><tr><td>Propulsion</td><td>propulsion_data</td><td>propulsion_data</td><td>propulsion_data</td><td>sea_levelSpecific_impulse</td></tr><tr><td></td><td></td><td></td><td></td><td>, vacuumSpecific_impulse, sea_level_thrust_table, t hrottle.</td></tr><tr><td>Controls</td><td>flight Controls, co ntrl_entries</td><td>flight Controls, co ntrl_entries</td><td>flight Controls</td><td></td></tr></table>

文件在此目录下： \resources\data\mover_creator\AFSIM_Scripts\.

飞行器设计器

MoverCreator 中的飞行器设计器是一个全面的工具，允许用户定义飞行器的各个方面，如控制、几何和空气动力学。它还提供了进行性能和飞行测试的功能。以下是关键组件的详细说明：

# 关键组件

几何：定义飞行器的物理形状和结构。这包括影响飞行器性能和能力的尺寸和配置。  
空气动力学：调整空气动力学特性，这是了解飞行器与空气相互作用的关键。这涉及研究飞行器周围的空气运动，并优化升力和阻力等因素。  
性能：分析飞行器在各种条件下的性能。这包括速度、机动性和效率的评估。  
飞行员/控制：设置飞行员用于操作飞行器的控制系统和界面。这包括配置控制面和输入设备。  
自动驾驶仪：设计和调整自动驾驶仪系统，以确保飞行器可以自主操作或在最少的飞行员干预下运行。  
飞行测试：在模拟环境中进行虚拟飞行测试，以验证飞行器的设计和性能。

# 文件管理

.amc 文件：飞行器的配置存储在 .amc 文件中，这些文件采用 JSON 格式。它们位于\resources\data\mover_creator\Vehicles\ 目录中。虽然 GUI 提供了一个用户友好的飞行器设计界面，但高级用户可以直接修改这些文件以实现更细致的控制。

# 引擎设计器

引擎设计器是 MoverCreator 的另一个关键组件，允许用户创建或修改引擎设计。支持的引擎类型包括喷气发动机、冲压发动机、液体推进剂火箭和固体推进剂火箭。与飞行器文件类似，引擎配置存储在 \resources\data\mover_creator\Engines\ 目录中的 .amc 文件中。

▪ 自定义：用户可以通过 GUI 定义引擎参数，或直接编辑 .amc 文件以进行高级自定义。注意  
飞行器和引擎的 .amc 文件具有特定的格式结构，只有熟悉 JSON 和 AFSIM 输入文件特定要求的用户才应修改这些文件。这确保了修改不会破坏 MoverCreator 的功能或其支持的模拟。

# 5.5.2. 参考手册 Mover Creator Reference Guide

# 5.5.2.1. 标准模版 Standard Templates

# 5.5.2.1.1. 标准飞行器模板 Mover Creator Standard Vehicle Templates

MoverCreator 提供了一套预定义的标准模板，用户可以从中派生他们的飞行器。这些

模板遵循一种命名约定，建立了一种命名未分类、半通用飞行器的通用方法。命名分为两个组：飞机和武器。命名设计尽可能简短，同时传达飞行器的功能或任务信息。以下部分将详细介绍命名约定的结构。

# 命名约定结构

飞机模板：这些模板的命名通常包括飞机的类型和其主要功能或任务。例如，战斗机、运输机等。

<table><tr><td>Fighter</td><td>Attack</td><td>Bomber</td><td>ISR</td><td>AEW</td><td>Tanker</td><td>Cargo and Transport</td><td>Maritime Patrol</td><td>Drone</td></tr><tr><td>F-H4-21C-1</td><td>A-M4-22A-1</td><td>B-H3-81A-1</td><td>R-MJ-11A-1</td><td>E-HJ-41A-1</td><td>K-MJ-21A-1</td><td>C-HJ-41A-1</td><td>P-MJ-21A-1</td><td>D-L4-11V-1</td></tr><tr><td>F-H4-22A-1</td><td></td><td>B-H1-80W-1</td><td></td><td></td><td></td><td></td><td></td><td>D-L4-11Z-1</td></tr><tr><td>F-H4-22B-1</td><td></td><td>B-H4-40W-1</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>F-L4-11A-1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>F-L4-11C-1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

武器模板：这些模板的命名通常反映武器的类型和用途，例如导弹、炸弹等。

<table><tr><td>Air-to-air</td><td>Surface-to-air</td><td>Air-to-ground</td><td>Air-launched decoy</td><td>Air-launched drone</td><td>Ground-launched drone</td><td>Guided bomb units</td><td>Munitio ns</td><td>Fuel Tanks</td></tr><tr><td>AIM-MR-1</td><td>MIM-MR-1</td><td>AGM-CM-1</td><td>ADM-MR-1</td><td>AQM-MR-1</td><td>BQM-MR-1</td><td>GBU-S-1</td><td>MUN-B-1</td><td>TNK-370-1</td></tr><tr><td>AIM-SR-1</td><td>RIM-MR-1</td><td>AGM-SR-1</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td>FIM-SR-1</td><td>BGM-CM-1</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td>RGM-CM-1</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td>UGM-CM-1</td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

这种命名约定的设计旨在帮助用户快速识别和选择适合其需求的模板，同时保持命名的一致性和简洁性。这种方法不仅提高了模板的可用性，还确保了在使用 MoverCreator 时的效率和准确性。

# Mover Creator 标准飞机模板命名规则

在 MoverCreator 中，飞机的命名由四个部分组成，用短横线分隔。以下是每个部分的详细说明：

# 部分 1：主要功能定义

第一个部分是一个字母，用于定义飞机的主要功能或任务：

A: 攻击（Attack）  
B: 轰炸机（Bomber）  
C: 货运（Cargo）  
D: 无人机（Drone）  
E: 预警机（AEW）  
F: 战斗机（Fighter）  
K: 加油机（Tanker）

P: 海事（Maritime）  
R: 侦察/情报、监视和侦察（ISR）

部分 2：重量级别和类型

第二部分根据飞机类型而变化，由两个字母或数字组成。第一个字母定义重量级别：

L: 轻型（Light）  
M: 中型（Medium）  
H: 重型（Heavy）

对于攻击机、战斗机和轰炸机，使用一个数字表示代际：

3: 第三代  
4: 第四代  
5: 第五代  
6: 第六代

对于侦察/ISR、预警机、加油机、货运/运输机和巡逻机，使用一个字母定义推进类型：

J: 涡轮喷气/涡轮风扇（Turbojet/Turbofan）  
P: 螺旋桨（Propeller）

部分 3：发动机、垂直尾翼和俯仰控制

第三部分由两个数字和一个字母组成：  
第一个数字表示发动机数量。  
第二个数字表示垂直尾翼数量。

最后一个字母表示俯仰控制方式：

□ A: 后置稳定器（常规稳定器/升降舵控制）  
B: 双稳定器/鸭翼  
□ C: 鸭翼控制  
□ V: V 型尾翼  
□ W: 机翼  
Z: 倒 V 型尾翼

部分 4：变体编号

最后一个部分是一个数字，表示变体。它从 1 开始，每定义一个新类型的飞机就递增。这种命名规则旨在通过简洁的方式传达飞机的功能和特性，帮助用户快速识别和选择合适的模板。

# 标准飞机模版

战斗机 Fighter

<table><tr><td colspan="2">F-H4-21C-1
第四代双引擎鸭翼战斗机,类似于欧洲战斗机台风(Eurofighter Typhoon).</td></tr><tr><td colspan="2">F-H4-22A-1
描述:第四代双引擎重型战斗机,类似于苏-27(Su-27).</td></tr><tr><td colspan="2">F-H4-22B-1
描述:第四代战斗机,带有稳定器和鸭翼,类似于苏-30系列(Su-30+).</td></tr><tr><td colspan="2">F-L4-11A-1
描述:第四代单引擎轻型战斗机,类似于F-16.</td></tr></table>

![](images/f10c8222eafc0414bd0ad1c466d300ca8812282a97367b75ffa4c3d0dc1ab234.jpg)  
F-L4-11C-1

描述: 第四代单引擎鸭翼战斗机，类似于鹰狮（Gripen）.

![](images/f97c9e155cd8ad96535b9a6cdbb9fe6ed218c072473fcb8a0630dc05fbc30f65.jpg)  
F-M5-12A-1

描述: 第五代单引擎中型战斗机，类似于F-35.

![](images/e3e15a327091f17a4aea4ac96bcada3f29f683f20883424911137eaa14a97b8b.jpg)  
攻击机 Attack  
A-M4-22A-1

描述: 第四代双引擎中型攻击机，类似于A-10.

![](images/96f9ca599116ac73284c0cd0b7eac5806776425ef3537bfc336e98ea15d174ce.jpg)  
轰炸机 Bomber  
B-H3-81A-1

描述: 第三代八引擎重型轰炸机，类似于B-52.

![](images/8c761b2409a2db87796160a976158d76e7f490f826ec2d698ac39bd405dac9f8.jpg)  
B-H1-80W-1

描述: 第一代八引擎重型轰炸机，类似于YB-49.

![](images/5df94e62749809e3b4f1395a6db8004a67f52b28e40f0a0e8ce0e065ec6e03e1.jpg)  
B-H4-40W-1

描述: 第四代四引擎重型轰炸机，类似于B-2.

![](images/c8cd2d6d3c9c27ac344c48ec8655f1e4803ff73b677ca78eeb1bf8be4707c273.jpg)  
侦察机 ISR  
R-MJ-11A-1

描述: 喷气动力中型侦察机，类似于 U-2.

![](images/38634ea1e48ccd6c2511944d6e354b81567b826863fc115117bad170fa0ed31a.jpg)  
预警机 AEW  
E-HJ-41A-1

描述: 四引擎重型预警机，类似于 E-3.

# 加油机 Tanker

![](images/1d75bd0a27a6d9780c042ae887e46590e40765a8587b1a27b59fdff08b2a6352.jpg)

K-MJ-21A-1

描述: 双引擎中型喷气加油机，类似于KC-46.

# 货运和运输 Cargo and Transport

![](images/457d763bc2eda4fa7a0b9c82a15d1aa3a8d692e7b519083e21765e71c09db84c.jpg)

C-HJ-41A-1

描述: 四引擎重型喷气运输机，类似于C-17.

# 海事巡逻 Maritime Patrol

![](images/592dcb42cd40722dfb9d8a18faea2ad1b0a644f5a640943344db1d3b43b495e3.jpg)

D-L4-11V-1

描述: 单引擎喷气动力无人机/UCAV，类似于 XQ-58 Valkyrie.

![](images/ab7b18ccfbc2c97cfd1ed97a7137af2f9b60c8b8dfc8c15be8b9505edb5dd4c7.jpg)

D-L4-11Z-1

描述: 单引擎远程操控飞机（RPA），类似于 MQ-1 Predator.

Mover Creator 标准武器模板命名规则

在 Mover Creator 中，武器的命名由三个部分组成，用短横线分隔。以下是每个部分的详细说明：

# 部分 1：三字母标识符

第一个部分使用三字母标识符。在大多数情况下，这是基于 1963 年美国三军导弹和无人机命名系统的三字母组合，表示发射环境、任务和类型。此外，第一部分还可能包括以下标识符：

AIM: 空射拦截空中导弹  
MIM: 地面发射拦截空中导弹  
RIM: 舰载发射拦截空中导弹  
FIM: 步兵发射拦截空中导弹  
AGM: 空射对地攻击导弹  
BGM: 地面发射对地攻击导弹  
RGM: 舰载发射对地攻击导弹  
UGM: 潜艇发射对地攻击导弹  
ADM: 空射诱饵导弹   
AQM: 空射无人机导弹  
BQM: 地面发射无人机导弹  
GBU: 制导炸弹单元  
MUN: 无制导弹药  
TNK: 外部燃料箱

# 部分 2：范围或类型

第二部分是可变的，取决于武器类型，由最多三个字母或数字组成。

大多数导弹: 使用两个字母表示射程类别：

▫ SR: 短程  
□ MR: 中程  
□ LR: 长程  
□ ER: 极远程

巡航导弹: 使用 CM 表示。  
制导炸弹单元 (GBUs): 使用一个字母表示鳍片类型：

□ F: 鳍片

▫ S: 侧翼   
▫ W: 机翼

弹药 (MUN): 使用一个字母表示弹药类型：

□ B: 炸弹  
□ R: 火箭

外部燃料箱 (TNK): 使用携带燃料的数量（以加仑为单位）。

部分 3：变体编号

最后一个部分是一个数字，表示变体。它从 1 开始，每定义一个新类型的武器或物品就递增。

标准武器模版 Standard Weapon Templates

AIM (空射拦截空中导弹)AIM (Air-Launched Intercept-Air Missiles)

![](images/29d4cef5d250fdcc940c69001914a045807348ccd72ec67881302e7018241cdc.jpg)

AIM-MR-1

描述: 中程空对空导弹，类似于 PL-12。

![](images/aee159c4ccbb01e4bbf6db1b52d3c4ccb1eee88ab98491c37804a40c1320be90.jpg)

AIM-SR-1

描述: 短程空对空导弹，类似 于 AA-11(R-73)。

MIM (地面发射拦截空中导弹)MIM (Ground-Launched Intercept-Air Missiles)

![](images/93b1fbb576ad99b38d4e502392d072d82433c9a66faf9f5c0f58f2dc5fe03571.jpg)  
MIM-MR-1

描述: 中程地面发射防空导弹 ， 类 似 于SA-11。

![](images/7eb938b99f0333f0dff1e1cb070963408e1e03097e25c19cd824fe48c1319c1e.jpg)  
RIM (舰载发射拦截空中导弹)RIM (Ship-Launched Intercept-Air Missiles)   
RIM-MR-1

描述: 中程舰载发射防空导弹 ， 类 似 于SA-N-7。

FIM (步兵发射拦截空中导弹)FIM (Infantry-Launched Intercept-Air Missiles)

![](images/d198e7aae850be839f589c34c32c879968744f6480c0fab965e4e0dc8c75c65e.jpg)  
AGM (空射对地攻击导弹)AGM (Air-Launched Surface Attack Missiles)

FIM-SR-1

描述: 短程便携式防空导弹系统（MANPADS），类 似 于 SA-14(9K34)。

![](images/db49f86a6a4ec1984fb18ba4c85bb41c7520d75eb4c6552dee106a79815d664b.jpg)  
AGM-CM-1

描述: 空射巡航导弹，类似于 AGM-109(Tomahawk)。

![](images/10b0061182b47cf295cea4bad3575d4b7f6e1e8c8065b3c68518d4f1d5024694.jpg)  
AGM-SR-1

描述: 短程空对地导弹，类似 于 AGM-65(Maverick)。

BGM (地面发射对地攻击导弹)BGM (Ground-Launched Surface Attack Missiles)

![](images/6893b5cbccf7c9ec627c09c1f1750c496350e9a7039c4ced5a4a2398db7dcd1a.jpg)  
RGM (舰载发射对地攻击导弹)RGM (Ship-Launched Surface Attack Missiles)

BGM-CM-1

描述: 地面发射巡航导弹，类 似 于BGM-109(Tomahawk)。

![](images/5337d2c5207730a95f87990cb40b608faa7f80f94c6c37321aa21f891d3753b5.jpg)  
RGM-CM-1

描述: 舰载发

射巡航导弹，

类 似 于

RGM-109

(Tomahawk)。

![](images/cd1c31c775cd023ad428d12d0c1c37dcf14f228434b32dc1a2ed02d3c4b40419.jpg)  
UGM (潜艇发射对地攻击导弹)UGM (Sub-Launched Surface Attack Missiles)   
UGM-CM-1

描述: 潜艇发

射巡航导弹，

类 似 于

UGM-109

(Tomahawk)。

![](images/76fc3738140d303e09bf77a2220e3a4c571fd70c559d648493266ad945e222e5.jpg)  
ADM (空射诱饵导弹)ADM (Air-Launched Decoy Missiles)   
ADM-MR-1

描述: 中程空

射诱饵导弹，

类 似 于

ADM-160B。

AQM (空射无人机导弹)AQM (Air-Launched Drone Missiles)

![](images/16eae729cd4896c10c9c3167c51720492d0173cfaafb0c7033cae9f027b3a756.jpg)  
AQM-MR-1

描述: 中程空射无人机，类似于 AQM-34(Firebee)。

![](images/4b2569d1bb9a15170279952c3a40c9def833f3914a4b3607c68cbd8b79122e33.jpg)  
BQM (地面发射无人机导弹)BQM (Ground-Launched Drone Missiles)   
BQM-MR-1

描述: 中程地面 发 射 无 人机 ， 类 似 于BQM-34(Firebee)。

GBU (制导炸弹单元)GBU (Guided Bomb Unit)

![](images/df7facbdae47445838893db89094a158ad668d30a153a61a9244cd2baaecb9b6.jpg)  
MUN (无制导弹药)

GBU-S-1

描述: 带有侧翼的制导炸弹单元，类似于2000 磅JDAM。

![](images/003ec58a8b0ac365994068b2d048d42b8451a485698ec3765e41a554a8641561.jpg)  
MUN-B-1

描 述 : 通 用500 磅炸弹，类 似 于 Mk82。

![](images/fa70612b3ed1919a4e32f313f4cf54b3749c42f0023f9a71b2854103f4e190f4.jpg)  
MUN-R-1

描述: 典型的无制导空对地火箭，类似于Hydra。

![](images/5cc21f05b092d0405768a36581ed48a026935c0b42ebf5ca6a52a21aa4a3e01a.jpg)  
TNK (外部燃料箱)TNK (External Fuel Tanks)   
TNK-370-1

描 述 : 通 用370 加仑外部燃料箱，类似于 F-16 使 用的燃料箱。

# 5.5.2.1.2. 标准翼型模板 Mover Creator Standard Airfoil Templates

# 5.6. 核心 APP WSF Core

World Simulation Framework (WSF) Core 提供了一个建模和仿真环境，供其核心应用程序用于分析目的。以下是 WSFCore 的一些关键应用和功能：

文档

参考指南：提供有关 WSF Core 的详细信息和使用说明。  
变更日志：记录了 WSFCore 的更新和修改历史。

# 应用程序

后处理和报告生成 (post_processor)：用于分析结果的后处理和生成报告。  
传感器覆盖和天线增益图创建 (sensor_plot)：用于创建传感器覆盖和天线增益图。  
武器交战分析支持 (engage)：支持武器交战的分析。  
武器模型开发支持 (weapon_tools)：用于开发和支持武器模型。  
任务分析/基线仿真应用 (mission)：用于任务分析和基线仿真。

# WSF 信息和示例

设置 Link-16：关于通过 DIS 设置 Link-16 的概述。  
数据结构约定：定义 WSF 输入文件内容和位置的约定概述。  
加速构建仿真运行：减少 WSF 运行时间的步骤。  
从构建到虚拟：修改构建仿真并实时运行的具体步骤。

# 5.6.1. 后处理生成报告工具 post_processor

PostProcessor 是一个用于从 AFSIM 输出的原始数据创建格式化报告的工具，基于给定的配置文件。报告类型包括：

▫ 通信报告  
□ 探测报告  
▫ 日食报告  
□ 交战报告  
▫ 轨迹报告  
□ DSV（分隔符分隔值）输出

每种报告在配置文件中都有可修改的选项，用于过滤和更改给定数据的格式。某些选项适用于所有报告（见下文的配置选项）。

# 配置选项

以下选项适用于所有报告，除非另有说明：

report [communication | detection | eclipse | engagement | dsv | trajectory]：指定要生成 的报告类型。   
report_name<string>：指定报告的名称。如果文件夹或文件已存在，则会被覆盖。运行编号会自动插入到文件名的末尾，但也可以使用 %d 标签手动插入。日期和时间标签 %D 和 %T 也可以用于文件管理。

□ 示例：report_name example_report   
▫ 注意：对于包含空格的值，需要使用引号。

data_file[<file_name>]：指定输入文件所在的文件名。要处理蒙特卡洛文件，请在文件名中插入运行编号标签 %d。

□ 示例：data_file ../input/example_%d.csv   
□ 注意：对于包含空格的值，需要使用引号。

output_directory [<folder_name>]：指定输出文件生成的文件夹名称。如果文件夹和文件已存在，则会被覆盖。运行编号会自动插入到文件名的末尾，但也可以使用 $\% 0$ 标签手动插入。日期和时间标签 %D 和 %T 也可以用于文件管理。

□ 示例：output_directory output/run_%d/

□ 注意：对于包含空格的值，需要使用引号。

monte_carlo_start <integer-value>：指定起始运行编号。默认值为 1。  
monte_carlo_end <integer-value>：指定结束运行编号。默认值为所有连续运行，按升序排列。  
single_output_file <boolean-value>：指定是否将所有格式化的运行数据输出到单个文件。（目前未实现）

□ 注意：不适用于 DSV 输出。默认值为 true。

write_header_information <boolean-value>：指定是否将标题输出到报告中。  
□ 注意：不适用于 DSV 输出。默认值为 true。  
delimiter [comma | column | semicolon | space | tab]：指定分隔值的分隔符。默认值为逗号。  
length_units [feet | meters]：指定距离的测量单位。（目前未实现）

▫ 注意：不适用于 DSV 输出。默认值为米。

angle_units [radians | degrees]：指定角度的测量单位。（目前未实现）

□ 注意：不适用于 DSV 输出。默认值为度。

track_number_options [numerical | jtids]：指定轨道编号格式选项。（目前未实现）

□ 注意：不适用于 DSV 输出。默认值为数字。

start_time <real> <time-units>：指定所需数据的开始时间。默认值为 0。  
end_time <real> <time-units> ： 指 定 所 需 数 据 的 结 束 时 间 。 默 认 值 为std::numeric_limits<double>::max()。  
lat_lon_format d[:m[:s]][.#]：指定显示纬度和经度值的格式和小数位数。默认值为d:m:s.2。  
time_format [[h:]m:]s[.#]：指定显示时间值的格式和小数位数。默认值为 s.5。  
precision <double-value>：指定双精度值的精度。

□ 注意：不适用于 DSV 输出。默认值为 2。

# 通信报告

通信报告记录平台之间如何以及多频繁地进行通信。

重要提示：至少需要启用以下事件之一才能生成通信报告数据：

MESSAGE_DISCARDED   
MESSAGE_UPDATED   
MESSAGE_QUEUED   
MESSAGE_TRANSMITTED   
MESSAGE_RECEIVED   
report_type [traffic_counts | connectivity]：指定子报告类型。默认值为 traffic_counts。  
transmitters … end_transmitters：指定将收集数据的发射器。默认值为所有。  
receivers … end_receivers：指定将收集数据的接收器。默认值为所有。  
networks … end_networks：指定将收集数据的网络。默认值为所有。

# 通信报告子报告

TrafficCounts：输出每个平台或网络生成、传输、完成到接收者以及清除/删除的消息数量。

选项：

platforms | networks | time_interval

间隔：

interval <real> <time-units>：指定每个数据集所需的时间间隔。默认值为 1 秒。示例：interval 60 seconds：提供 0-60 秒之间的数据，然后是 60-120 秒，依此类推。  
Connectivity：目前未实现。

# 探测报告子报告

重要提示：至少需要启用以下事件之一才能生成探测报告数据：

SENSOR_DETECTION_ATTEMPT   
SENSOR_DETECTION_CHANGED   
report_type [total_detections | first_detections | access]：指定子报告类型。   
TotalDetections：输出每个平台的探测次数。此子报告没有其他选项。  
First Detections：输出一个平台对另一个平台的首次探测。

选项：

□ platform_type_of_detected_platform   
▫ side_indicator   
□ altitude_of_detected_platform   
□ azimuth_angle   
▫ elevation_angle

Access：提供平台之间可见性的开始时间、结束时间和持续时间。

# 日食报告

日食报告提供平台在地球阴影中的开始时间、结束时间和持续时间。

重要提示：至少需要启用以下事件之一才能生成日食报告数据：

ECLIPSE_ENTRY   
ECLIPSE_EXIT

注意：结果不考虑地球的扁平效应或平台单次轨道期间地球的运动。

platforms … end_platforms：指定将收集数据的平台。默认值为所有。

# 交战报告子报告

重要提示：至少需要启用以下事件之一才能生成交战报告数据：

PLATFORM_ADDED   
WEAPON_FIRED   
WEAPON_FIRE_ABORTED   
WEAPON_RELOAD_STARTED   
WEAPON_RELOAD_ENDED   
LOCAL_TRACK_DROPPED   
LOCAL_TRACK_INITIATED   
LOCAL_TRACK_UPDATED   
SENSOR_REQUEST_CANCELED   
SENSOR_REQUEST_INITIATED   
SENSOR_REQUEST_UPDATED   
SENSOR_TRACK_COASTED

SENSOR_TRACK_DROPPED   
SENSOR_TRACK_INITIATED   
report_type [total_detections | first_detections]：指定子报告类型。  
Track Event History：输出每个平台的探测次数。  
Weapon Expenditures：目前未实现。

轨迹报告

待办事项。

# DSV（分隔符分隔值）输出

此报告根据以下指定生成多个分隔符分隔值（DSV）输出文件。任何未列出的文件或未在 post_processor 中映射的文件将输出到与输入文件头中的事件名称匹配的文件中。

示例输入文件：  
```txt
report DSV  
report_name sample_demo_%D  
data_file sample_demo_%d.csv  
output_directory.  
delIMITER comma  
lat_lon_format d:m:s.2  
time_format s.5 
```

# 核心文件列表

BTREE_NODE_CHILDREN.csv：包含事件 BTREE_NODE_CHILDREN  
BTREE_NODE_EXEC.csv：包含事件 BTREE_NODE_EXEC  
COMMENT.csv：包含事件 COMMENT  
COMM_FREQUENCY_CHANGED.csv：包含事件 COMM_FREQUENCY_CHANGED  
COMM_STATUS.csv ： 包 含 事 件 COMM_BROKEN, COMM_TURNED_ON,COMM_TURNED_OFF, COMM_OPERATIONAL, COMM_NON_OPERATIONAL  
EXECUTE_CALLBACK.csv：包含事件 EXECUTE_CALLBACK  
FUEL_EVENT.csv：包含事件 FUEL_EVENT, RAN_OUT_OF_FUEL  
LOCAL_TRACK_CORRELATION.csv ： 包 含 事 件 LOCAL_TRACK_CORRELATION,LOCAL_TRACK_DECORRELATION  
LOCAL_TRACK_INITDROPUPDATE.csv ： 包 含 事 件 LOCAL_TRACK_DROPPED,LOCAL_TRACK_INITIATED, LOCAL_TRACK_UPDATED  
MESSAGE_DELIVERY_ATTEMPT.csv：包含事件 MESSAGE_DELIVERY_ATTEMPT  
MESSAGE_XMITD_RCVD_QUEUED_DISCARDED.csv ： 包 含 事 件 MESSAGE_RECEIVED,MESSAGE_TRANSMITTED, MESSAGE_QUEUED, MESSAGE_DISCARDED  
MESSAGE_UPDATED.csv：包含事件 MESSAGE_UPDATED  
MOVER_STATUS.csv ： 包 含 事 件 MOVER_TURNED_OFF, MOVER_TURNED_ON,MOVER_STAGED, MOVER_OPERATIONAL, MOVER_NON_OPERATIONAL, MOVER_BROKEN,MOVER_BURNED_OUT  
NAVIGATION_STATUS_CHANGED.csv：包含事件 NAVIGATION_STATUS_CHANGED  
OPERATING_LEVEL_CHANGED.csv ： 包 含 事 件 AUTONOMY_LEVEL_CHANGED,

OPERATING_LEVEL_CHANGED

PLATFORM_APPEARANCE_CHANGED.csv：包含事件 PLATFORM_APPEARANCE_CHANGED  
PLATFORM_BROKEN.csv：包含事件 PLATFORM_BROKEN  
PLATFORM_CAPABILITY_CHANGED.csv：包含事件 PLATFORM_CAPABILITY_CHANGED  
PLATFORM_STATUS.csv ： 包 含 事 件 PLATFORM_ADDED, PLATFORM_DELETED,PLATFORM_BROKEN, PLATFORM_INITIALIZED, PLATFORM_OMITTED  
PROCESSOR_BROKEN.csv：包含事件 PROCESSOR_BROKEN  
PROCESSOR_STATUS.csv：包含事件 PROCESSOR_TURNED_OFF, PROCESSOR_TURNED_ON,PROCESSOR_OPERATIONAL, PROCESSOR_NON_OPERATIONAL  
SENSOR_DETECTION.csv ： 包 含 事 件 SENSOR_DETECTION_ATTEMPT,SENSOR_DETECTION_CHANGED  
SENSOR_FREQUENCY_CHANGED.csv：包含事件 SENSOR_FREQUENCY_CHANGED  
SENSOR_BROKEN.csv：包含事件 SENSOR_BROKEN  
SENSOR_MODE_STATUS.csv ： 包 含 事 件 SENSOR_MODE_ACTIVATED,SENSOR_MODE_DEACTIVATED  
SENSOR_STATUS.csv ： 包 含 事 件 SENSOR_NON_OPERATIONAL, SENSOR_OPERATIONAL,SENSOR_TURNED_OFF, SENSOR_TURNED_ON  
SENSOR_REQUEST_STATUS.csv ： 包 含 事 件 SENSOR_REQUEST_CANCELED,SENSOR_REQUEST_INITIATED, SENSOR_REQUEST_UPDATED  
SENSOR_TRACK_STATUS.csv ： 包 含 事 件 SENSOR_TRACK_COASTED,SENSOR_TRACK_DROPPED, SENSOR_TRACK_INITIATED, SENSOR_TRACK_UPDATED  
STATE_STATUS.csv：包含事件 STATE_ENTRY, STATE_EXIT  
TANKING_EVENT.csv：包含事件 TANKING_EVENT  
TEAM_NAME_DEFINITION.csv：包含事件 TEAM_NAME_DEFINITION

# 武器文件列表

▪ DIRECTED_ENERGY_WEAPON_SHOT.csv ： 包 含 事 件 DIRECTED_ENERGY_WEAPON_BEGIN_SHOT, DIRECTED_ENERGY_WEAPON_UPDATE_SHOT, DIRECTED_ENERGY_WEAPON_ABORT_SHOT, DIRECTED_ENERGY_WEAPON_END_SHOT   
DIRECTED_ENERGY_WEAPON_COOLDOWN_COMPLETE.csv ： 包 含 事 件DIRECTED_ENERGY_WEAPON_COOLDOWN_COMPLETE  
IMAGE_CREATED.csv：包含事件 IMAGE_CREATED  
IMPLICIT_WEAPON_ENGAGEMENT.csv ： 包 含 事 件IMPLICIT_WEAPON_BEGIN_ENGAGEMENT, IMPLICIT_WEAPON_END_ENGAGEMENT  
JAMMING_ATTEMPT.csv：包含事件 JAMMING_ATTEMPT  
JAMMING_REQUEST.csv ： 包 含 事 件 JAMMING_REQUEST_CANCELED,JAMMING_REQUEST_INITIATED, JAMMING_REQUEST_UPDATED  
MOVER_GUIDANCE_PHASE_CHANGED.csv ： 包 含 事 件MOVER_GUIDANCE_PHASE_CHANGED  
PLATFORM_KILLED.csv：包含事件 PLATFORM_KILLED（已弃用）  
TASK_STATUS.csv：包含事件 TASK_ASSIGNED, TASK_CANCELED, TASK_COMPLETED   
WEAPON_FIRE_STATUS.csv ： 包 含 事 件 WEAPON_FIRE_ABORTED, WEAPON_FIRE_REQUESTED   
WEAPON_FIRED.csv：包含事件 WEAPON_FIRED, WEAPON_LAUNCHED

WEAPON_HITMISSKILL.csv：包含事件 WEAPON_HIT, WEAPON_KILLED, WEAPON_MISSED   
WEAPON_MODE_STATUS.csv ： 包 含 事 件 WEAPON_MODE_ACTIVATED,WEAPON_MODE_DEACTIVATED  
WEAPON_STATUS.csv：包含事件 WEAPON_NON_OPERATIONAL, WEAPON_OPERATIONAL,WEAPON_TURNED_OFF, WEAPON_TURNED_ON  
WEAPON_RELOAD_STATUS.csv ： 包 含 事 件 WEAPON_RELOAD_ENDED,WEAPON_RELOAD_STARTED  
WEAPON_SELECTED.csv：包含事件 WEAPON_SELECTED  
WEAPON_TERMINATED.csv：包含事件 WEAPON_TERMINATED

# 网络文件列表

CYBER_ATTACK_INITIATED.csv：包含事件 CYBER_ATTACK_INITIATED  
CYBER_ATTACK_SUCCEEDED.csv：包含事件 CYBER_ATTACK_SUCCEEDED  
CYBER_ATTACK_FAILED.csv：包含事件 CYBER_ATTACK_FAILED  
CYBER_ATTACK_DETECTED.csv：包含事件 CYBER_ATTACK_DETECTED  
CYBER_ATTACK_RECOVERY.csv：包含事件 CYBER_ATTACK_RECOVERY  
CYBER_SCAN_INITIATED.csv：包含事件 CYBER_SCAN_INITIATED  
CYBER_SCAN_SUCCEEDED.csv：包含事件 CYBER_SCAN_SUCCEEDED  
CYBER_SCAN_FAILED.csv：包含事件 CYBER_SCAN_FAILED  
CYBER_SCAN_DETECTED.csv：包含事件 CYBER_SCAN_DETECTED

# 5.6.2. 传感器评估工具 sensor_plot

sensor_plot 是一个 WSF 应用程序，用于评估传感器特性及其与用户指定几何形状的交互。它能够创建以下类型的图表文件：

传感器垂直覆盖   
传感器垂直地图  
传感器水平覆盖   
传感器水平地图  
传感器球形覆盖   
飞行路径分析  
杂波表  
传感器集合的防御区域  
天线模式

命令行使用

使用独立的 sensor_plot.exe：

```txt
sensor_plot file<sub>sub>1</sub>/sub> [file<sub>sub>2</sub>/sub> ... file<sub>sub>n</sub>/sub>] 
```

对于支持 sensor_plot 的其他 WSF 应用程序：

```txt
wsf.application.exe --sensor_plot file<sub>sub>1</sub>/sub> [file<sub>sub>2</sub>/sub> ... file<sub>sub>n</sub>/sub>] 
```

其中参数是包含以下内容的文件名：

定义要执行功能的 sensor_plot 输入块。  
执行功能所需的传感器和平台定义。

# 命令

antenna_plot：生成 2D 恒定方位角或仰角或 3D 极坐标图文件。

```txt
antenna_plot
... Antenna Plot Commands ...
... Stub Definition Commands ...
end_antenna_plot 
```

clutter_table：生成用于 WSF 仿真的雷达杂波表。

```txt
clutter_table ... Clutter Table Commands ... ... Stub Definition Commands ... end_clutter_table 
```

flight_path_analysis：生成沿飞行路径的变量图。

```txt
flight_path_analysis ... Flight Path Analysis Commands ... ... Stub Definition Commands ... end_flight_path_analysis 
```

horizontal_map：生成下游和横向值矩阵上的变量图。

```txt
horizontal_map ...HorizontalMapCommands... ...StubDefinitionCommands... end-horizontality_map 
```

horizontal_coverage：生成“水平覆盖图”（或“水平覆盖包络”）图文件。

```txt
horizontal_coverage ...Horizontal Coverage Commands ... ...Stub Definition Commands ...   
end-horizontal_coverage 
```

spherical_map：在指定范围内生成视角矩阵上的变量图。

```txt
spherical_map ...Spherical Map Commands ... ...Stub Definition Commands ... end_spherical_map 
```

vertical_map：生成高度和地面范围矩阵上的变量图。

```txt
vertical_map ... Vertical Map Commands ... ... Stub Definition Commands ... end_vertical_map 
```

vertical_coverage：生成“垂直覆盖图”（或“垂直覆盖包络”）图文件。

```txt
vertical_coverage ... Vertical Coverage Commands ... ... Stub Definition Commands ... end_vertical_coverage 
```

# Stub Definition Commands

现有场景通常用于创建 horizontal_map 图。这些场景可能包括使用 sensor_plot 可执行文件中未提供功能（例如武器模型）的平台或平台子系统类型定义。为了允许场景在不更改的情况下使用，提供了命令和虚拟类型定义来模拟未实现功能的可用性。

以下命令提供了忽略指定全局命令的机制：

ignore_block <word>：忽略从 <word> 开始到 end_<word> 的所有数据。  
ignore_line <word>：忽略 <word> 及同一行上的所有后续词。  
ignore_word <word>：忽略 <word>。

提供的虚拟类型包括：

WSF_DUMMY_COMM（虚拟通信定义）  
WSF_DUMMY_MOVER（虚拟移动器定义）  
WSF_DUMMY_PROCESSOR（虚拟处理器定义）  
WSF_DUMMY_SENSOR（虚拟传感器定义）  
WSF_DUMMY_WEAPON（虚拟武器定义）  
WSF_DUMMY_WEAPON_EFFECTS（虚拟武器效果定义）

# 5.6.3. 交战工具 engage

ENGAGE 是一个用于评估地面武器有效性（以及目标脆弱性）的 WSF 应用程序。

命令行

命令格式如下：

```txt
engage file<sub>sub>1</sub>/sub> [file<sub>sub>2</sub>/sub> … file<sub>sub>n</sub>/sub>] 
```

参数是包含以下内容的文件名：

定义配置和输出的 run 和 output_rate 输入块。  
执行功能所需的武器、目标、发射器和可选传感器的定义。

# 脚本方法

WsfSimulation 方法用于在输出到屏幕或文件时对不同的运行、目标、站点和蒙特卡洛重复次数进行排序（例如观察者输出文件）。

```javascript
write_In("Run Number: ", WsfSimulationRUNNumber(), "Target Number: ", WsfSimulation.TargetNumber(), "SiteNumber: ", WsfSimulation.SiteNumber(), "RepNumber: ", WsfSimulation.Repetition()); 
```

int RunNumber()：返回当前运行编号。   
int TargetNumber()：返回当前运行的目标编号。  
int SiteNumber()：返回当前运行的站点编号。  
int RepetitionNumber()：返回当前运行的蒙特卡洛重复次数。

# 命令

▪ thread_count <integer>：指定用于并行完成 SWEET 任务的线程池中的线程数。  
run … end_run：定义一个运行块，可以在单个可执行文件中输入多个运行块以串行处理每个运行块。  
output_rate <rate-table-name> … end_output_rate：指定一个按名称配置的 output_rate，用于运行输入块命令的输出块。  
output_template <template-name> … end_output_template：指定一个按名称配置的output_template，用于运行输入块命令的输出块。

# 运行命令

center_location <latitude-value> <longitude-value>：指定此运行的中心位置，默认值为0.0n 0.0e。  
event_output_file_base_name <string>：指定结果写入的文件名基础值，附加后缀 .evt。  
perform_flyouts <boolean-value>：指定是否执行飞行，默认值为 true。  
record_file_base_name <string>：指定结果写入的文件名基础值，附加后缀 .rep。  
repetition_count <integer>：指定此配置要运行的蒙特卡洛重复次数，默认值为 1。

# 站点配置命令

launcher_type <platform-type-name>：指定运行的发射器平台类型名称，默认值为LAUNCHER_TYPE。  
tracker_type <platform-type-name> ： 指 定 运 行 的 跟 踪 器 平 台 类 型 名 称 ， 默 认 值 为TRACKER_TYPE。  
sites … end_sites：指定站点列表，使用以下命令多次：  
xyz <length-value> <length-value> <length-value>：指定站点的 $\mathsf { x } , \mathsf { y } , \mathsf { z }$ 位置。  
heading <angles-value>：指定站点的航向，默认值为 90.0 degrees。  
speed <speed-value>：指定站点在航向方向上的速度，默认值为 $0 . 0 \ : \mathrm { m } / s$   
site_grid … end_site_grid：指定站点网格配置。

# 目标配置命令

target_type <platform-type-name> ： 指 定 运 行 的 目 标 平 台 类 型 名 称 ， 默 认 值 为TARGET_TYPE。  
use_target_path：指定使用定义的目标飞行路径。  
target_grid … end_target_grid：指定目标网格配置。

simple_path … end_simple_path：指定目标简单路径配置。  
flight_path … end_flight_path：指定飞行路径。  
flight_route … end_flight_route：指定飞行路线。

注意：use_target_path、target_grid、simple_path、flight_path 和 flight_route 是互斥的，输入处理堆栈中的最后一个将被使用。

# 输出命令

output … end_output：指定要输出的数据。可以在运行输入块中多次定义输出块，以根据用户需求定制输出。以下命令可用：  
file<file-name>：指定输出文件名以输出运行的数据。  
phase [<all | acquiring | tracking | flying>]：指定运行的阶段，以输出数据。  
event_output <boolean-value>：指定是否输出事件数据。  
summary_output <boolean-value>：指定是否输出运行摘要数据。  
rate_table_name <rate-table-name>：指定要使用的速率表名称，由 output_rate 命令指定。  
items .. end_items：指定要输出的项目及其格式，格式如下：

variable <variable-name> units <variable-units> format <formatting-value>

<variable-name>：指定要输出的变量名。有效值包括：  
时间相关：time, weapon_flight_time  
目标位置和速度：target_x, target_y, target_z, target_vx, target_vy, target_vz, target_ax, target_ay, target_az   
武器位置和速度：weapon_x, weapon_y, weapon_z, weapon_vx, weapon_vy, weapon_vz,weapon_ax, weapon_ay, weapon_az  
武器性能：weapon_speed, weapon_mach, weapon_gee_force, weapon_to_target_range   
<variable-units>：指定输出的变量单位。根据变量名检查有效单位。  
<formatting-value>：指定格式，遵循 ANSI C 标准的字符串语法。

示例：

# items

```txt
variable weapon_flight_time format "%.2f"  
variable target_x units km format "%7.3f"  
variable target_y units km format "%7.3f"  
variable target_z units m format "%7.1f"  
variable weapon_x units km format "%7.3f"  
variable weapon_y units km format "%7.3f"  
variable weapon_z units m format "%7.1f"  
variable weapon_to_target_range units m format "%7.1f"  
end_items 
```

events .. end_events：指定要启用或禁用的事件，使用以下命令：

# events

```txt
disable [<event-name> | all] enable [<event-name> | all] end_events 
```

disable [ <event-name> | all ] 和 enable [ <event-name> | all ]：指定要包含或排除在事件日志中的事件名称。默认情况下，所有事件都被禁用。命令按出现顺序处理，每个后续命令根据需要选择或取消选择事件。  
有效的事件名称包括：

传 感 器 相 关 ： SENSOR_DETECTION_ATTEMPT, SENSOR_DETECTION_CHANGED,SENSOR_FREQUENCY_CHANGED, SENSOR_MODE_ACTIVATED, SENSOR_MODE_DEACTIVATED,SENSOR_NON_OPERATIONAL, SENSOR_OPERATIONAL, SENSOR_REQUEST_CANCELED,SENSOR_REQUEST_INITIATED, SENSOR_REQUEST_UPDATED, SENSOR_TRACK_COASTED,SENSOR_TRACK_DROPPED, SENSOR_TRACK_INITIATED, SENSOR_TRACK_UPDATED,SENSOR_TURNED_OFF, SENSOR_TURNED_ON

仿 真 和 武 器 相 关 ： SIMULATION COMPLETE, WEAPON_FIRE_ABORTED,WEAPON_FIRE_REQUESTED, WEAPON_FIRED, WEAPON_HIT, WEAPON_KILLED,WEAPON_MISSED, WEAPON_TERMINATED

# 输出速率命令

time <time>：指定输出将被写入的时间。默认值为 0.0 sec。  
period <time>：指定输出数据的周期。默认值为 0.5 secs。

输出模板命令

待定（TBD）

Pk 表生成命令

enable_Pk_table_generation <boolean-value>：启用与运行相关的 Pk 表生成。注意，Pk表生成仅在站点网格中有效，对于目标网格将被禁用。默认值为 false。  
Pk_table_target_type <string>：设置生成 Pk 表目录层次结构和表头时的目标名称。默认值为 "DEFAULT"。  
Pk_table_site_type <string>：设置生成 Pk 表目录层次结构和表头时的站点名称。默认值为 "DEFAULT"。  
Pk_table_output_directory <string>：生成的 Pk 表数据层次结构的输出路径位置。默认值为 "."。  
Pk_output_length_units <length-value>：将所有输出值转换为此单位以用于 Pk 表生成和目录层次结构。默认值为 "m"。  
Pk_output_speed_units <speed-value>：将所有输出速度值转换为此单位以用于 Pk 表生成和目录层次结构。默认值为 "m/s"。  
enable_Pk_table_periodic_flush <boolean-value>：在生成完成时写入所有 Pk 表数据，而是在与目标高度相关的所有数据点完成处理时输出数据。这允许在非常长的生成过程中保留部分 Pk 数据，以防止中止或中断的过程。默认值为 false。

# 5.6.4. 武器工具 weapon_tools

weapon_tools 是一个可选的 WSF 模块，可以集成到 WSF 应用程序中，也可以作为独立的可执行文件分发。它通过在各种交战条件下反复发射预定义的 WSF_EXPLICIT_WEAPON，捕获命中/未命中的结果，以量化该武器类型的交战能力，从而实现对目标轨迹的成功武器

部署。该工具生成一个或多个文件，这些文件定义了未来模拟或场景中将使用的武器的运行时软件对象。weapon_tools 是可扩展的，目前允许创建/生成以下武器部署对象：

空对空发射计算机，通过 AIR_TO_AIR_LAUNCH_COMPUTER_GENERATOR。  
空对地（ATG）发射可接受区域（LARs）和发射计算机，通过 ATG_LAR_AND_LC_GENERATOR。  
弹道发射计算机，通过 BALLISTIC_LAUNCH_COMPUTER_GENERATOR。  
弹道导弹发射计算机，通过 BALLISTIC_MISSILE_LAUNCH_COMPUTER_GENERATOR。  
轨道发射计算机，通过 ORBITAL_LAUNCH_COMPUTER_GENERATOR。  
地对空导弹（SAM）发射计算机，通过 SAM_LAUNCH_COMPUTER_GENERATOR。

命令行使用

使用独立的 weapon_tools.exe：

```xml
weapon.tools.exe <input-files> 
```

对于支持 weapon_tools 的其他 WSF 应用程序：

```xml
wsf.application.exe --weapon-tools <input-files> 
```

命令

tool <tool-type-name> … end_tool：定义工具类型和相关命令。

```txt
tool <tool-type-name> ... Tool Commands ... end_tool 
```

其中 <tool-type-name> 是概述中列出的选项之一。

# 工具命令

tool_debug：启用运行时调试输出。默认：关闭。  
terminate_on_launch_failure <boolean-value>：如果为 true，当武器未能发射时工具将终 止 。 此 命 令 仅 适 用 于 AIR_TO_AIR_LAUNCH_COMPUTER_GENERATOR 、ATG_LAR_AND_LC_GENERATOR 和 BALLISTIC_LAUNCH_COMPUTER_GENERATOR。默认：true。  
position <latitude> <longitude>：指定发射平台的地理位置。默认： $0 . 0 \mathsf { n } , 0 . 0 \mathsf { e }$   
altitude <length-value>：指定武器发射的高度。默认： $_ { 0 . 0 \mathsf { m } }$ 。  
heading <angle-value>：指定发射平台的罗盘方向。默认： $0 . 0 { \mathsf { d e g } }$ 。  
frame_step <time-value>：工具更新之间的时间间隔。默认：0.5 秒。  
launch_platform_type <platform-type> ： 指 定 将 发 射 武 器 的 平 台 类 型 。 默 认 ：LAUNCH_PLATFORM_TYPE。  
target_platform_type <platform-type> ： 指 定 将 被 攻 击 的 平 台 类 型 。 默 认 ：TARGET_PLATFORM_TYPE。  
weapon_name <weapon-name>：指定在发射平台上使用的武器名称。默认：在发射平台类型上遇到的第一个武器。  
weapon_effects <effect-name>：指定发射武器平台将用于确定目标效果的武器效果（致

命性）模型。默认：WEAPON_TOOL_LETHALITY。

tool_produces <product-name>：指定武器工具的输出产品。此值用于自动命名输出文件。典 型 值 为 _LAUNCH_COMPUTER 或 _LAUNCH_ACCEPTABLE_REGION 等 。 默 认 ：_UNKNOWN_PRODUCT。  
output_object_name <output-name>：指定武器工具的输出产品。此值用于自动命名输出文件。默认：_UNKNOWN_PRODUCT。  
output_file_extension <extension-name>：指定武器工具输出产品的文件扩展名。默认：.txt。  
output_file_name <file-name>：指定工具生成的文件的名称。默认：output_object_name$^ +$ output_file_extension 的连接。

# 5.6.5. 任务 mission

mission 应用程序是 WSF 应用程序的基线可执行文件。它读取包含 WSF 参考指南的文本文件，并执行模拟，通过时间推进，移动平台，做出决策并在对象之间进行交互。

# 执行模式

事件步进或帧步进：模拟可以以事件为步进或以帧为步进的方式执行。  
实时或非实时：可以选择实时或非实时模式。  
纯构建，包括多次蒙特卡洛迭代：支持多次蒙特卡洛模拟。  
作为分布式交互式模拟（DIS）练习的一部分：可以与 DIS 接口集成。

# mission 的三种主要输出形式

事件日志：由输入命令 event_output 控制。生成的日志是人类可读的文本文件，可以通过 Timeview 程序可视化，或通过各种脚本程序（如 Perl、Python）进行后处理。还可以使用 csv_event_output 创建一组默认的逗号分隔（或用户指定分隔符）文件。通过 observer 命令，可以触发用户定义的脚本，将信息写入屏幕或文件。  
二进制事件报告文件：可以通过 Mystic 应用程序查看，由输入命令 event_pipe 控制。  
二进制“重放文件”（可能在未来被弃用）：可以通过 VESPA 可视化。通过在 dis_interface块中指定 record 命令生成。

# 命令行使用

```typescript
mission [ -es | -rt | -fs | -fio | -sm | -mi <interval> | -log-server-host <hostname> | -log-server-port <portNumber> | -profiling-output <output-location> | -profiling-library ] <file-1> [ <file-2> ... <file-n> ] 
```

# 参数说明

-es(默认)：运行事件步进模拟执行程序。默认情况下，事件步进模拟执行程序将在非实时模式下运行（即，它将尽可能快地调度事件）。要在实时 DIS 练习中运行事件步进，请确保在输入中包含 realtime 命令。  
-rt：以实时模式运行帧步进模拟执行程序（帧推进将与时钟同步进行）。目前不建议在复杂场景中使用此选项。  
-fs：以非实时模式运行帧步进模拟执行程序（帧推进将在完成所有帧工作时进行）。等同于指定 -rt 并在输入中包含 non-realtime 命令。

-fio：每次模拟推进时，确保所有字符从标准输出流写入其目的地，并清除缓冲区（刷新）。  
-sm：抑制指示模拟时间推进的周期性消息。  
-mi<interval>：以给定时间间隔（秒）输出指示模拟时间推进的周期性消息。  
-list-variables：输出场景文件中使用的预处理变量列表并退出。  
-log-server-host <host>：指定 mission 应连接日志服务器客户端的主机。  
-log-server-port <port>：指定 mission 应连接日志服务器客户端的端口。  
-profiling-output <output-location>：指定性能分析输出的写入位置。文件将在不存在时创建。仅在提供此选项时启用性能分析。  
-profiling-library <library-path>：指定性能分析钩子的非默认共享库路径。如果未提供且启用了分析，则使用默认分析库。  
<file-1> [ <file-2> … <file-n> ]：包含 WSF 参考指南中记录的命令的一个或多个文件。

# 5.6.6. 构建 Link-16 数据链

以下组件是通过 DIS 设置 Link-16 所需的：

link16_interface - 配置 Link-16 接口。如果没有此命令，Link-16 接口将被禁用。  
WSF_LINK16_COMPUTER - 这是一个处理发送和接收 Link16 - Tadil-J 消息的处理器。Tadil-J 消息可以发送到模拟中的另一个平台，或者通过 DIS 发送到另一个应用程序。默认情况下，该处理器仅接收消息。要发送消息，必须将消息处理器添加到WSF_LINK16_COMPUTER 中 。 为 了 使 其 功 能 正 常 ， Link16 计 算 机 必 须 与WSF_JTIDS_TERMINAL 或其他作为网络一部分运行的通信设备一起使用。  
WSF_JTIDS_TERMINAL - 这是 WSF 实现的 JTIDS 终端。此实现模拟了通过 JTIDS 网络的数据传输。它不模拟消息内容或脉冲级特性。注意：任何 WSF 通信设备都可以用于模拟数据传输。

上述 WSF_LINK16_COMPUTER 与 WSF_JTIDS_TERMINAL 均有对应章节描述。以下介绍link16_interface。

# 5.6.6.1. link16 接口 link16_interface

```txt
link16-interface ... Link16 interface subcommands ... j11 allow_any_comm network-enabledweapon_type ... use_time_of_target mesurement wift_interval ... print/messages end_j11   
end_link16-interface 
```

没有此命令将禁用 Link16 接口。

命令

tdl_header <header-type><header-type>：用于编写 DIS 信号消息的 TDL 头类型。可以是 6 或 100。

默认值：100

swap_tdl_header_100_method <swap-type>

我 们 支 持 两 种 不 同 的 TDL-100 传 输 方 式 。 <swap-type> 可 以 是 fields_only 或fields_then_word_boundary。

默认值：fields-only

print_script_usage

输出有关 WsfTadilJ 类用于脚本化 J 消息的信息。

ignore_inbound_messages <boolean-value>

指定是否忽略入站的 l16 DIS 消息。如果设置为 true，WSF 将不会尝试处理通过 DIS接收到的 j 消息。这不影响 J11 消息。

默认值：false

debug

启用 Link16 接口的调试输出。

fill_with_31.7 <boolean-value>

启用或禁用用 31.7 消息填充信号 PDU。如果启用，信号 PDU 将包含足够的 31.7 字以总计 3、6 或 12 字的整个消息。此选项可用于与某些仿真兼容。

默认值：no

include_dis_entity_id_in_j3x_tracks <boolean-value>

在将 WSF 轨迹转换为 J3.X 监视轨迹消息时使用。当为“true”时，将附加一个扩展字，其中包含由轨迹表示的真实对象的 DIS 实体 ID。

默认值：false

# J11 命令

allow_any_comm

允许任何通信设备发送/接收 J11 消息。换句话说，不需要 WSF_JTIDS_TERMINAL。

network_enabled_weapon_type <weapon-platform-type> <integer-value>

用于将武器的平台类型映射到 J11.0I 字中的“TypeofNEW”字段中使用的整数值。有效范围是 0 到 11。（请参阅 J11 规范定义以了解字段的使用）

注意：为每种用作武器的平台类型创建一个或多个。

默认值：0

use_time_of_target_measurement

在接收到 J11.1-5 飞行中目标更新 (IFTU) 指令时，将使用续行字 3 中的“目标测量时间”来推断 IFTU 数据到接收仿真的当前仿真时间。IFTU 时间值预计为发送仿真的仿真时间，并假设发送和接收应用程序之间正在进行时间同步。（这不符合 J11 规范定义的字段使用）

默认值：off

wift_interval <time-value>

发送 J11.0-4 武器飞行中轨迹 (WIFT) 报告的时间间隔。

print_messages

在发送或接收时打印 J11 消息的内容。

另请参阅

WSF_LINK16_COMPUTER

# 5.6.7. 数据结构约定 Data Structure Conventions

命名约定

AFSIM 的命名约定确保了一致性，并使用户能够识别名称是文件还是平台/传感器/模式。

<table><tr><td>模式</td><td>约定</td><td>示例</td></tr><tr><td>名称</td><td>使用连字符(hyphens)和下划线(underscores)替换空格或其他特殊字符</td><td>F18 radar 变为 f-18_radar</td></tr><tr><td>文件名</td><td>使用小写字母</td><td>generic_f-18_radar.txt</td></tr><tr><td>平台/传感器</td><td>大写并用下划线替换斜杠、空格或破折号</td><td>Tin Shield 变为 TIN_SHIELD</td></tr><tr><td>文件中定义的平台、传感器名称</td><td>与文件名相同(不带后缀),全部大写</td><td>文件 generic_f-18_radar.txt 定义 GENERIC_F-18_RAR</td></tr><tr><td>系统组件名称(例如,天线模式)</td><td>以系统名称开头</td><td>组件 radar antenna 为 GENERIC_F-18_RARANTENNA</td></tr><tr><td>雷达模式名称</td><td>全部大写</td><td>模式 ACQUIRE</td></tr></table>

目录结构

文件库目录树展示了用于 AFSIM 输入文件的目录结构。

输入文件被组织到 base_types 和 <other>_types 子目录下。深入细分为 patterns、platforms、sensors、signatures 和 weapons。

用户项目目录（例如，随 AFSIM 提供的 iads_demo）被划分为自己的目录结构，模仿输入文件示例子目录的结构。这些目录包含“覆盖”基础输入文件的文件。这种方法允许用户拥有一个稳定的、已知行为的基础案例，可以以简单、一致的方式进行修改。

注意：例如，如果用户想要修改特定武器的行为，可以将 base_types/weapons 子目录中的基础武器复制到本地项目 scenario/weapons 目录。然后可以对本地武器进行更改。同样，可以将其他模型复制到项目子目录中，这将覆盖 base_types 中的模型。

<table><tr><td>Directory</td><td>Subdirectory</td><td>Links</td><td>Content</td></tr><tr><td>base_types</td><td></td><td></td><td></td></tr><tr><td></td><td>patterns</td><td></td><td></td></tr><tr><td></td><td>platforms</td><td></td><td></td></tr><tr><td></td><td>sensors</td><td></td><td></td></tr><tr><td></td><td></td><td>eo_ir</td><td>Electro-Optical and Infrared sensor definitions.</td></tr><tr><td></td><td></td><td>esm_rwr</td><td>Electronic Support Measures &amp; Radar Warning Receiver sensor definitions.</td></tr><tr><td></td><td></td><td>radar</td><td>Radar sensor definitions</td></tr><tr><td></td><td></td><td>other</td><td>Other sensor types</td></tr><tr><td></td><td>signatures</td><td></td><td></td></tr><tr><td></td><td>weapons</td><td></td><td></td></tr><tr><td></td><td></td><td>aam</td><td>Air-to-Air Missiles Definitions.</td></tr><tr><td></td><td></td><td>agm</td><td>Air-to-Ground Missiles Definitions.</td></tr><tr><td></td><td></td><td>jaam</td><td>Joint Air-to-Air Missiles Definitions.</td></tr><tr><td></td><td></td><td>jammer</td><td>Examples of intentional emission of radio frequency signals:</td></tr><tr><td></td><td></td><td>other</td><td>e.g., Theater Ballistic Missile.</td></tr><tr><td></td><td></td><td>sam</td><td>Surface-to-Air Missile Definitions</td></tr><tr><td></td><td></td><td>sims</td><td>Standard Interface for Missile Simulation.</td></tr><tr><td>tools</td><td></td><td></td><td>Scripts that help users run their model(s) and parse output.</td></tr><tr><td></td><td></td><td></td><td>User scenario (iads_demo, sensor_demo, etc)</td></tr><tr><td></td><td>output</td><td></td><td>Model output (replay, log, and event files).</td></tr><tr><td></td><td>platforms</td><td></td><td>Only present if changes were made to platforms.</td></tr><tr><td></td><td>sensors</td><td></td><td>Only present if changes were made to sensors.</td></tr><tr><td></td><td>signatures</td><td></td><td>Only present if changes were made to signatures.</td></tr><tr><td></td><td>weapons</td><td></td><td>Only present if changes were made to weapons.</td></tr><tr><td></td><td></td><td></td><td>Override directory for base_types if applicable.</td></tr><tr><td></td><td>patterns</td><td></td><td></td></tr><tr><td></td><td>platforms</td><td></td><td></td></tr><tr><td></td><td>sensors</td><td></td><td></td></tr><tr><td></td><td></td><td>eo_ir</td><td>Electro-Optical and Infrared sensor</td></tr></table>