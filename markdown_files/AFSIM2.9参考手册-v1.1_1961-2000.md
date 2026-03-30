# 基础设施

想定管理

时间管理

地理空间

数据管理

工具

推演管理

事件管理

插件管理

![](images/0e89f91f62a00238ede86587f76e9f7f83562d948dabec74699d5063077e1fef.jpg)

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQQD.

# UNCLASSIFIED

# 一些仿真结构

![](images/bba11a58cc8f58bb35821ce37c2a8b75fed4a9b8a1fdcdd63d05bc979829af98.jpg)

WsfScenario对象包含一个扩展列表、一个地形接口以及所有类型的列表。

WsfApplication对象包含一个扩展列表和一个插件管理器。

WsfSimulation对象依赖于WsfScenario对象，而WsfScenario对象依赖于WsfApplication对象。

![](images/56457e63eacaff639e27e9a544497322c87a17602f212bcc64eff30cdd3a4cb1.jpg)

WsfSimulation对象包含许多与管理和执行仿真相关的对象。

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19.

Other requests for this document shall be referred to AFRL/RQQD.

- 仿真对象负责仿真：

- 通过从框架提供的基类派生进行自定义。

- 支持事件步进或伪帧步进模式。

- 提供添加和移除平台的通用机制。  
- 以协调的方式初始化和更新平台及其平台系统。

![](images/861b624f0f3100d6e9778ffcc49f6c213b934dff1089aa07f7d5b694d6152f52.jpg)

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQQD.

15

![](images/981e47fff5b9420feee39c16ca208e08349e82eb5b9847a13a4c089342b1dedd.jpg)

# UNCLASSIFIED

# 仿真管理

![](images/68b45f05ba5d0cffc88e0b2a1cc2384339bc0fafc1aadc45c6347128e234389b.jpg)

- 场景类型列表提供用户输入的内部表示，包括：

- 平台  
- 平台部件  
特征签名   
- 路径  
跟踪过滤器  
- 电子战（EW）效果  
- 行为树节点  
- ......仅列举部分内容......

- 使用工厂（Factory）软件设计模式：  
- 用户输入中的“子类型”以相同 C++ 类的不同配置形式存储。

Replay File has a .aer file extension

- 每个仿真对象类型都聚合了一个时钟源：

- WsfClockSource 提供启动、停止（暂停）和重置时钟的方法。  
实时仿真使用

WsfRealTimeClockSource 的实例化：

包含一个挂钟对象，用于维护经过的“真实”时间。  
基于计算机的实时时钟检索系统时间。

![](images/0fa2aeedb1f945fab99fca8ad7af5796cf51ed54503f9a62b9c541dd40ce5b2c.jpg)

![](images/52725be593a5d4ed2f031480baaa96a29697efc8cc415b2bb887cd30d1172b1e.jpg)

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQQD.

# UNCLASSIFIED

# 事件管理

![](images/e8fd7697cafcc404e866443f082565052ccf02c28c0834de2b85bfe519c63ae3.jpg)

![](images/f06c01030678d40aa367a2d2b1d0b6dec1c4c6b0449721cad8eb9d0738e0346c.jpg)

![](images/88a0aa4faef87b85ba65fcf6cd35c25f0cbcd4858423e4f4f1c3a54c5b607d99.jpg)

- 一个模拟对象（WsfSimulation）在构造时会创建一个事件管理器。事件管理器（WsfEventManager）维护一个按时间排序的事件队列。这个事件队列是一个标准模板库（STL）中的priority_queue，其中每个元素按照时间递增的顺序排列。时间表示事件（WsfEvent）需要被调度的时刻。  
- 事件管理器提供了一些方法，用于将事件添加到队列中、查看但不移除下一个要调度的事件、从队列中弹出下一个事件，以及将队列重置为空状态。添加事件的接口是通过模拟对象的 AddEvent 方法来使用的。

- 事件步进仿真通过查看事件队列的队首来等待下一个事件。事件步进和帧步进仿真对象都会在调用 AdvanceTime 方法时分派事件。事件会从队列中弹出，并调用它们的 Execute 方法。

![](images/0b81a70623cb921568c07e6a61cc395463b5d597fd7a85153ef9805ea140e93e.jpg)

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQDD.

- WsfTerrain 类实现了地形数据库和查询操作功能：

- 维护表示地形数据库的静态数据。  
- 查询方法会引用该数据库以获取地形数据。  
- 注意，地形切片（tiles）通过引用计数机制在多个 WsfTerrain 对象之间共享。因此，内存中实际上只会存在某个特定切片的一个实例。

- 数字地形高程数据（Digital Terrain Elevation Data，DTED）是通过该类缓存并可访问的一种地形数据集形式。

- 支持DTED Level 0、1和2。

- 美国地质调查局（United States Geological Survey, USGS）的数字高程模型（Digital Elevation Model, DEM）数据经过重新处理，转换为与ESRI ArcGIS®产品兼容的格式（http://www.esri.com）。

- 格式为带有头文件的“grid(float”或“float-grid”二进制格式。

![](images/96053c468861e2d8bb57a5755528fb8e0154ea4633c7a4b01a98969098056eed.jpg)

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQQD.

19

![](images/180178849a8d363562ad6e34eefd519b5143f6a629d542bb4bc9772edded1d54.jpg)

# UNCLASSIFIED

# 插件管理

![](images/afcde561e1defe3f5725330058ff9b62622f1e698363dcdd98940c48c7683c8d.jpg)

- 支持通过动态加载的插件进行自定义：

- 提供与源代码修改类似的灵活性。  
- 支持通过主版本号和次版本号进行版本管理。

- 类 WsfPluginManager 的功能:

- 在以下路径中搜索插件：

- WSF_PLUGIN_PATH 环境变量定义的路径。  
../<application_name>_plugins目录。  
- 应用程序的当前目录。

- 注册并加载在搜索过程中找到的插件。  
- 在注册插件之前执行编译器检查。  
- 能够注册几乎任何类型的插件。

- 实用程序例程（Utility routines）用于多种目的，帮助管理和简化其他AFSIM类的数据操作。AFSIM的实用程序例程通常支持以下领域：

实体表示：位置、方向、速度/加速度。  
- 专用数据类型和行为（例如，向量、数组、列表、表格或字符串）。  
- 数学操作（例如，表格查找、向量/矩阵运算或几何计算）。  
- 输入、输出和文件管理例程（例如，加密以及从各种来源交换数据）。  
- 时间管理。  
- 地球坐标参考框架和大气数据。  
仿真控制机制（例如，UtCallback对象、列表以及UtCallback对象的管理）。  
单位（角度、经纬度、长度、地球计算、输入、数学、随机数、速度、间）。

![](images/442ce26a1f1afadb9b5ae738ca6447113adc44f130ac0ce48ef2f5fc829bdbdb.jpg)

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQQD.

# UNCLASSIFIED

# 单位

21

![](images/b3ef0d38935b46703f2d826e4166ee8596cf47a60e71b391b621b7e1e3607759.jpg)

![](images/e685326184df4c06895b2e02ff9b4eaf3254d0d51eb1f046931831625d7a74aa.jpg)

- 除非文档中另有说明，AFSIM将对所有参数和成员变量使用米/千克/秒（meter/kilogram/second, MKS）单位系统。

- 以下是支持单位的部分列表：

- 长度：米（m）  
- 质量：千克（kg）  
时间：秒（s）  
- 速度：米每秒（m/s）  
加速度：米每二次方秒（ $\mathfrak{m} / \mathfrak{s}^2$ ）  
频率：赫兹（Hz）=1/s   
力：牛顿（Nt）=kg·m/s²  
功率：瓦特（W）=Nt·m/s  
- 角度：弧度  
纬度：十进制度数，范围为[-90, 90]   
经度：十进制度数，范围为[-180, 180]   
数据单位：比特（bits）  
数据传输速率：比特每秒（bits/second）

- 仿真加载器和输入系统为用户提供了以多种形式指定输入值的机制，但在将这些值存储到内存之前，它们始终会被转换为首选单位。

“世界坐标系”（World Coordinate System, WCS）  
- 该坐标系被定义为NIMATR8350.2中描述的WGS-84坐标系，并被DIS使用。它是一个右手坐标系，具体定义如下：

原点位于地球的中心。  
+X轴穿过 $0^{\circ}\mathrm{N},0^{\circ}\mathrm{E}$ （赤道与本初子午线的交点）。  
+Y轴穿过 $0^{\circ}\mathrm{N},90^{\circ}\mathrm{E}$ （赤道与东经 $90^{\circ}$ 的交点）。  
+Z轴穿过 $90^{\circ}\mathrm{N}$ （北极）。

“实体坐标系”（Entity Coordinate System, ECS）  
- 该坐标系有时被称为“机体坐标系”（Body Coordinate System）。它是一个右手坐标系，具体定义如下：

原点位于实体（机体）的中心。  
+X轴指向机体的前方   
+Y轴指向飞行员的右侧。  
+Z轴指向机体的底部。  
- 正偏航（Yaw）为飞行员向右转动。  
- 正俯仰（Pitch）为机头上仰。  
- 正滚转（Roll）为右侧机翼向下。

“本地北东下坐标系”（North-East-Down, NED）  
- 该坐标系类似于 ECS，但未经过实体的方向角旋转。具体定义如下：

原点位于实体的中心。  
+X轴指向北方。  
+Y轴指向东方。  
+Z轴指向地面（向下）。

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19.

Other requests for this document shall be referred to AFRL/RQQD.

# UNCLASSIFIED

# 坐标系统 (2/2)

![](images/481c50844a3b698320fe764a1d70fb363d77d2cf4e7312333990c7d49e809aac.jpg)

![](images/4b10b63ce1c38fa9d9631160a1621eefcc7a06977f737ad90b7888f3c4d2b9b5.jpg)

“地心惯性坐标系”（Earth Centered Inertial, ECI）

该坐标系类似于WCS，但它是相对于背景恒星固定的，而不是相对于地球固定的。

在较好的近似下，其定义如下：

原点位于地球的中心。  
- +X轴指向春分点（即太阳从南向北穿过地球赤道的点，发生在春分日[3月20日-21日]）。  
- +Z轴垂直于2000年1月1日12:00 UT的平均赤道平面（大致在该历元时通过北极 $[90^{\circ}\mathrm{N}]$ ）。  
- $+\mathsf{Y}$ 轴垂直于X和Z轴，形成一个右手坐标系。

“部件坐标系”（Part Coordinate System, PCS）

PCS表示附加到实体（例如天线）的部件的局部坐标系：

它表示该子部件的位置和方向。  
- PCS 的原点位置和方向是相对于附加部件的实体（平台）的 ECS 定义的（在 UtEntityPart 中有更详细的描述）。  
PCS的轴和角度约定与ECS类似。

UEntity类

UttEntity 类提供了多种方法，用于在不同坐标系之间进行转换。

- AFSIM 提供了处理和支持仿真执行、其他常规计算以及基本功能的能力：

- 扩展（Extensions）：提供了一种通用方法，用于添加新的服务和组件。  
- 观察者（Observer）：提供了一种通用的发布-订阅服务，用于从仿真中提取数据。  
- 脚本（Script）：提供了实现和扩展AFSIM脚本语言的基础设施。  
- 分布式仿真接口（Distributed Simulation Interfaces）：应用了仿真互操作性的接口标准（IEEE 1278 和 1516；DIS 和 HLA）。

![](images/6901d46dab908d2698d62953b30c0b6fa1862c3d7f01f9db921d4174bd634cb0.jpg)

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQQD.

# UNCLASSIFIED

![](images/877c59f47b49f2cab1769f538c79739d31af08f4d26290230a46a39ef1f26692.jpg)

# AFSIM脚本

![](images/7a010ad008f898a14e073b9fd016c9053a4fdcadd4a4ace494e51e6aa05e93f0.jpg)

- 脚本方法的声明和定义

- #define UT.DeclareScriptMethod( ... )展开为方法参数的类声明：

继承自类UtScriptClass::InterfaceMethod。  
- 为类的方法声明构造函数和 operator() 运算符。

define UT DEFINEScriptMETHOD(..)

- 为使用 UT.DeclareSCRIPTMETHOD 宏定义的相同“方法”创建类定义。  
- 同时展开为一系列 $\mathsf{C} + +$ 语句，这些语句创建了一个函数，其函数体是为宏定义的代码。  
- 该函数由为类声明的 operator() 调用。  
- 一旦定义，该脚本方法即可从场景文件中的脚本接口调用。

AFSIM核心中为任务预定义了许多脚本方法，使用这些宏可以实现。

您也可以在自己的代码中使用这些宏创建新的脚本方法。

- 实现了软件设计中的观察者模式（Observer Pattern），在该模式中，观察者可以订阅对象的状态变化，并通过调用其方法之一来接收通知。  
- 许多不同类型的框架对象会“发布”仿真事件。

# List of Published Events v2.5

# COMMENT

COMM_ADDED_TO managerial

COMM REMOVED FROM MANAGER COMM DETOE

COMM_ADDED TO_LOCAL COMMADDED LOCAL

COMM_REMOVED FROM_LOCAL COMM_REPOUNDED CHANGED

COMM FREQUENCY CH COMM TURNEOFF

COMM_TURNEED_OFF COMM_TURNEED_ON

COMM.COM

EXCHANGEEVEN

EXCHANGE_EVENT EXECUTI CAL I RACK

EUELEVENT

FOLL EVENTLINK_ADDDED_TO.'<MANAGER>

LINK_ABDED_TO_MANAGER

LINK ENABLED ON MANAGER

LINK DISABLED ON MANAGER

LINK_ADDDED_TO_LOCAL

LINK_REMOVE_FROM_LOCAL

LINK_ENABLED_ON_LOCAL

LINK DISABLED_ON_LOCAL

LOCAL Track CORRELATION

LOCAL Track DECORRELATION

LOCALTRACK DROPPED

LOCAL TRACK INITIATED
LOCAL TRACK UPDATED

LOCAL Track Updated
MESSAGE DELIVERY ATTEMPT

MESSAGE DELIVERYMESSAGE DISCARDED

MESSAGE_DISCARDED
MESSAGE failed ROUTING

MESSAGE-IFIEDEN-MESSAGE-LIBDATED

MESSAGE OF DATED

MESSAGE_QUCLED  
MESSAGE_RECEIVED

MESSAGE TRANSMITTED

MESSAGE_TRANSMITTED_HEARTBEAT

MESSAGE TRANSMIT ENDED

# MOVER_UPDATE

NETWORK_ADDDED

NETWORK_REMOVE

OPERATING_LEVEL_CHANGED

PLATFORM_ADDED

PLATFORM APPEARANCE_CHANGED

PLATFORMDELETED

PLATFORM INITIALIZ

PLATFORM BROKENPLATTONOUTED

PLATFOMMOTITED PROESECOOCHUDINE

PROCESSOR TURNED ON PROCESSOR TURNED OFF

PROCESSOR_TURNOED_ON
SENSOR DETECTION ATTEMPT

SENSOR DETECTION ATTEMPT SENSOR DETECTION CHANGED

SENSOR_DETECTION_CHANGED SENSOR FREQUENCY CHANGED

SENSOR_MODE_ACTIVATED

SENSOR_MODE_ACTIVATE SENSOR_MODE_DEACT

SENSOR_MODE_SENSIVATED SENSOR_REQUEST_CANCELED

SENSOR_REQUEST_CANCELLED SENSOR_REQUEST_INIATED

SENSOR_REQUEST_UPDATE

SENSOR TRACK COASTED

SENSOR Track DROPPED

SENSOR Track INITIATED

SENSOR Track Updated

SENSOR-TURNED_OFF

SENSOR_TURNED_ON

SIMULATION_COMPLETE

SIMULATION�始ING

SIMULATION_STARTING

STATE_ENTRY

STATE_EX1

TANKING_EVENT

TASK Assigned

TASK_CANCELED TASK_CANCELED

TASK_COMPLETED
TITLE NAME DEP#

TEAM_NAMEDEFINITION

# ECLIPSE_ENTRY

ECLIPSE_EXIT   
ORBITAL_MANEUVER_INITIATED   
ORBITAL_MANEUVER_UPDATE   
ORBITAL_MANEUVER_CANCELED   
ORBITAL_MANEUVER_COMPLETED   
ORBITDETERMINATION INITIATED   
ORBIT_DETERMINATION_US

# CYBER ATTACK INITIATED

CYBER_attack_SUCCEEDED   
CYBER_attack_FAILED   
CYBER_attack_DETECTD  
CYBER_attack_RECOVER  
CYBER_SCANNITATED   
CYBER_SCAN_SUCCEEDED   
CYBER_SCAN_FAILED CYBERSCAN DETECTED   
CYBER_SCAN_DETECTED

DIRECTED ENERGY WEAPON BEGIN SHOT   
DIRECTED ENERGY WEAPON UPDATE SHOT   
DIRECTED_ENERGY_WEapon_ABORT SHOT   
DIRECTED_ENERGY_WEapon_COOLDOWN_C

DIRECTED_ENERGY_WEapon_END_SHOT   
IMPLICITWEAPON_BEGIN_ENGAGEMENT  
IMPLICIT_WEapon_END_ENGAGEMENT   
JAMMING_ATTEMPT   
JAMMING_REQUEST_CANCELED   
JAMMING_REQUEST_INITIATED   
JAMMING_REQUEST_UPDATE   
WEAPON FIRE.AI   
WEAPON FIRE REQUESTED   
WEAPON_FIRED   
WEAPON_HIT   
WEAPON_MISSED   
WEAPON_MODE_ACTIVATED   
WEAPON MODE DEACTIVATED WEAION-DETECTED   
WEAPOIN-RELOAD-STARTE WEALON-GEOLD-ENDED   
WEAPOINRELOAD ENLC WEAONTERMINATED   
WEAPOWN TERMINATED WEAPON TURNED OFF   
WEAPON_TURNEED_ON

27

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19.

Other requests for this document shall be referred to AFRL/RQQD.

# UNCLASSIFIED

# 分布式仿真接口

![](images/877aeef444030d015998c539a97ed827bfa032c5b348844071b58d855d2cd35a.jpg)

- AFSIM 支持多种分布式仿真接口标准：

- 分布式交互仿真（Distributed Interactive Simulation, DIS）

基于IEEE标准1278。  
- 经过广泛测试，具有许多用户功能。  
支持大多数“标准”协议数据单元（PDUs）。  
- 完全支持DIS5。  
- 部分支DIS6。

注意：DIS标准并未完全实现

- 高层体系结构（High Level Architecture, HLA）

- HLA插件扩展了AFSIM的功能，能够创建一个时间管理的分布式仿真，通过网络发送和接

收仿真数据（例如实体数据）

- 开放任务系统（Open Mission Systems, OMS）和通用指挥与控制接口（Universal

Command and Control Interface, UCI)

- OMS/UCI插件扩展了AFSIM的功能，使平台能够通过网络发送和接收OMS/UCI消息，以指挥和控制AFSIM组件（如传感器、武器等）。

- XIO（自定义的AFSIM专用网络接口）

仅用于连接AFSIM实体与其他AFSIM实体。  
- 与此不同的是，Comms接口可以连接非AFSIM的网络实体。  
XIO的用途包括：

- 在多个进程中模拟平台部件（如传感器、通信等）。  
- 对AFSIM平台进行分布式控制。

- 应用程序、场景和仿真都可以被“扩展”

- 应用程序扩展（Application Extensions）

由应用程序拥有。  
- 表示可以添加到应用程序的可选功能。  
- 当需要新的脚本类型（如传感器、武器、组件、移动器）时使用。  
- 这是在AFSIM中注册所有扩展的入口点。  
- 如果要创建场景扩展或仿真扩展，则需要一个应用程序扩展。

场景扩展（Scenario Extensions）

由场景拥有。  
- 用于注册新的组件类型。  
- 提供对ProcessInput链（组件、观察者、通信）的访问。  
- 如果要使用默认的应用程序扩展，则需要一个场景扩展。

仿真扩展（Simulation Extensions）

由仿真拥有。  
- 如果需要访问或使用仿真的任何部分，则必须使用仿真扩展。  
- 提供特定于仿真的可选功能，例如DIS接口、WsfDraw、事件输出、脚本观察者等。

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQDD.

29

![](images/ae9d4fd01c0762bb87f0c954c81727d1b856835bbe583247216e243d98465963.jpg)

# 应用程序扩展（Application Extensions）和插件（Plugins）

![](images/db35f642aaf26a35ab81d7178455be7080f5fbbcdd45d06836026f107a7e68e5.jpg)

- 插件在 AFSIM 中的目的是什么？  
- 插件是一个可以在运行时加载到内存中的外部库。  
- 插件的主要目的是支持创建AFSIM扩展，包括：

- 应用程序扩展（继承自 WsfApplicationExtension）  
- 场景扩展（继承自 WsfScenarioExtension）  
仿真扩展（继承自 WsfSimulationExtension）

- 应用程序扩展的位置在哪里？  
- 应用程序扩展几乎可以位于任何地方。  
- cmake 会在一组预定义的位置中搜索“标准”应用程序扩展。  
- cmake 也可以通过配置来指定其他路径以查找应用程序扩展，

例如：EX，cmake ... -DWSF_ADD Extensions_PATH=<path to extension> ...

- AFSIM 扩展被编译为外部动态链接库（DLL）或插件  
- 应用程序扩展如何注册到标准应用程序中？

- 每个插件都必须包含一个名为 WsfPluginSetup 的函数。  
- 该函数会在插件加载到内存并与AFSIM链接后立即执行。  
- WsfPluginSetup 的函数原型如下：  
    void WsfPluginSetup(WsfApplication& aApplicationPtr);

- 每个 WsfPluginSetup 的定义应完成以下操作：

- 为该库插件创建应用程序扩展对象。  
- 调用以下方法注册扩展：：

aApplicationPtr->RegisterExtension( ... )

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQQD.

31

![](images/c9b843244f6ac023d6ac0206478e0d241eee497345b8c86815abe42130292bbd.jpg)

# 应用程序扩展（Application Extensions）和插件（Plugins）

![](images/721290dac81784d820bf9e616889c88a5147141dfaa11f1acfd0a20450628b3d.jpg)

- AFSIM 如何定位插件并加载扩展？  
- 通过使用插件管理器（WsfPluginManager 或 UtPluginManager），AFSIM 执行以下操作：

1. 搜索动态库文件的位置（在 Windows 中为 .lib DLL 文件，在 Linux 中为 .so 文件）。  
2. 对于每个找到的库文件，AFSIM插件管理器会：

- 将库加载到内存中。  
- 一旦加载完成，AFSIM会调用该库中的WsfPluginSetup函数。

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQDD.

- AFSIM 提供了处理和支持仿真执行、常规计算以及基本功能的能力

Movers

提供运动相关功能。

- Sensors

提供仿真加载器和对象支持。

- Weapons

提供时钟源功能。

Communications

提供发布/订阅功能，允许仿真观察者注册仿真事件。

- Processors

提供地形和视线（Line-of-Sight）数据支持。

- 其他平台组件

提供地球模型、坐标系、数学运算等功能。

非平台组件

- 允许AFSIM在运行时查找插件并将其加载到内存中。

![](images/73208887531c1e868e290a29725db520b95219a23acdc0c93bf92994e83badd6.jpg)

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQQD.

UNCLASSIFIED

# AFSIM平台

![](images/b9cf484046c07338c01917c01691ae70011638850dacc35f03b2c6ebe71d5a65.jpg)

33

![](images/871ff1eb3b8673b7bb06fc0905ae892069ef6bc73a6f1f2e5712ba1bd0b9400d.jpg)  
平台（Platform）是其组成组件的“容器”

# 平台（Platform）是AFSIM中表示实体的主要方式

- 平台由以下部分组成

物理组件  
心理/计算组件  
信息  
属性  
链接

![](images/0066d50e917ca7813a1b4f4bc8967ee3c4884b34164293201be6765364060947.jpg)

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19.

Other requests for this document shall be referred to AFRL/RQQD.

- AFSIM 允许在平台上放置任意组件

- “基于组件的架构”（Component-Based Architecture, CBA）  
- AFSIM 采用了基于组件的架构，允许用户根据需求添加或移除组件。  
组件的灵活性

- 可以根据需要添加或移除组件。  
- 用户可以创建新的组件以满足特定需求。

组件本身也可以是平台（例如，想象一枚从战斗机上发射的导弹——导弹本身就是一个独立的平台）。

- 组件创建与加载

- AFSIM 依赖于组件（对象）工厂来创建并加载平台上的组件。  
- “PreInitialize”方法会自动加载组件，从而简化了组件的初始化过程。

- 这种架构使得AFSIM在仿真中具有高度的灵活性和可扩展性，能够适应复杂的场景和任务需求。

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQQD.

35

![](images/3a54fad796d1d38ddbc9c5d2cc5a6a6b945217243cdbb4d93b965c37afb1e249.jpg)

# 通用组件层次结构（General Component Hierarchy）

![](images/a1842fa67bb8c678f03cc39c31c73795ecebea06c950c1b435d6c22531062484.jpg)

![](images/3b400ee8c6c8f038b8e328baeb6a78cd7ab6aa0ff50958ce19bde7b41ca0ac06.jpg)

以下代码片段定义了一些有用的标识符：

using WsfPlatformComponent = WsfComponentT<WsPlatform>定义了一个类型别名WsfPlatformComponent，它是WsfComponentT模板类的一个特化，基于WsfPlatform。  
using WsfPlatformComponentList = WsfComponentListT <WsPlatformComponent> 定义了一个类型别名 WsfPlatformComponentList，它是 WsfComponentListT 模板类的一个特化，基于 WsfPlatformComponent。  
- class WsfProcessorComponent : public WsfComponentT<WsfProcessor> ...
- 定义了一个类 WsfProcessorComponent，它继承自 WsfComponentT 模板类，基于 WsfProcessor。  
using ComponentList = WsfComponentListT<WsfProcessorComponent> 定义了一个类型别名 ComponentList，它是 WsfComponentListT 模板类的一个特化，基于 WsfProcessorComponent。

注意：这只是 AFSIM 中组件层次结构的一部分

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQQD.

- WsfPlatform 表示仿真中的一个实体（UtEntity）  
- WsfPlatform 的作用

WsfPlatform 在仿真中表示一个实体（UtEntity），并作为“系统”（即组件——如移动器、通信、传感器、武器等）的容器，这些组件定义了平台的运行方式和行为。

- WsfPlatform 的继承关系

类 WsfPlatform 派生自以下类：

- WsfObject: 一个基础类, 用于表示具有名称和类型的对象。  
- WsfUniqueld: 维护对象的唯一标识符。  
- UtEntity：表示实体的位置、方向、速度和加速度。

通过这种设计，WsftPlatform能够在仿真中灵活地表示复杂的实体及其行为。

![](images/b63d02c8c5d9c2adaff854dff4a34093dc355174605a0106c6aa924a2df731a8.jpg)

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQQD.

37

![](images/a8a68bec042369c0ed4becccb2b95b681873133359e7c0ee7edff0110bcb4269.jpg)

# 平台和平台索引（Platforms and Platform Indices）

![](images/5b0fa3573da5d7f73c2add9fa4f9f516c4963c876d876687bce28b4fa2cd6f9a.jpg)

由于平台可能在仿真过程中被销毁，因此不能保留指向其他平台的指针

- 推荐的做法  
应保留的是“平台名称”或“平台索引”。  
- 平台索引的分配  
当一个平台被添加到仿真中时，它会被分配一个唯一的平台索引，该索引在整个仿真过程中不会被重新分配。

平台索引的分配是在 WsfSimulation::Initialize 方法内部调用

WsfSimulation::AddPlatform 时完成的。

- 获取平台索引

对于一个活动平台，可以通过以下方式获取其平台索引：

size_t platformIndex = platformPtr->GetIndex();   
通过平台索引获取关联平台的地址  
- 给定一个平台索引，可以通过以下方式获取与之关联的平台地址：：

- WsfPlatform* WsfSimulation::GetPlatformByIndex(size_t aIndex)   
- 返回值将是指向该平台的指针（如果平台仍然存在），或者是 nullptr（如果平台已从仿真中移除）。因此，在使用返回的指针访问平台之前，必须检查该指针是否为 nullptr。

- WsfMover 是一个平台组件，负责维护其附属平台的运动学状态（位置、方向、速度、加速度等）。  
- WsfMover 的功能

- WsfMover由仿真对象调用，用于实现仿真中平台的移动。它是平台运动的核心组件，确保平台的运动状态能够被准确模拟和更新。

一些示例Mover

- Air Mover：用于飞机的航路点移动器。  
GroundMover：用于地面车辆的航路点移动器。  
- Guided Mover: 一种特殊的移动器，使用牛顿动力学模型，结合指定的质量属性、施加的空气动力以及由制导计算机发出的转向指令。  
- NORAD Space Mover：用于地球轨道卫星的专用移动器。  
- Road Mover：一种地面移动器，沿着道路网络（WsfRouteNetwork）移动。  
- Surface Mover：用于海上车辆的航路点移动器。  
- Time-Space-Position-Information (TSPI) Mover：基于TSPI文件中的数据更新位置的移动器。

通过这些不同类型的Mover，AFSIM能够模拟各种平台的运动行为，从而满足复杂仿真场景的需求。

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQQD.

39

![](images/ac93a14dcfdd0f7a23245c9276ffa428cf4daa5df74346ef8c11cf6f9a61950c.jpg)

# WsfMover的继承关系（WsfMoverDerivation）

![](images/bd56fede9f822092c2de26c58a2d9bbb2f83d4ebfe31cb8baa7284d5188cd0a4.jpg)

![](images/1a62e8ca68a52dfdf26d59b13666c69213f62c822f42f71f323e83e62bc39ba5.jpg)

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQDD.

![](images/f284994323edbfbe98daa33d7e5e936599a5af7cb5610cb0c049cc610eed3820.jpg)  
DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQQD.

![](images/8943109b4d4ac03375e4c718cf8e9e3576fd897a7412f5d9c2cfa2c88bd0a928.jpg)

# UNCLASSIFIED 电磁系统建模（Modeling of Electromagnetic Systems）

![](images/57c2d72a311e9726dd60a44c11e32e6a69ac21f74a938723ba43a694ebb65578.jpg)

41

通信、传感器和武器系统使用一组通用的类来建模电磁交互  
![](images/3052a1e0824d3aa22be1aa22c768053e302417b98601389f072b126bec333e3c.jpg)  
DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQDD.

- WsfSensor 表示附加到平台上的传感系统

- 它是一个可动部件（WsfArticulatedPart），而可动部件是平台部件

（WsfPlatformPart），平台部件又是**平台组件（WsfComponent）**的一部分。

- WsfSensor 通常使用发射器、接收器和天线来完成其传感功能。

![](images/18613876eb96a6f998c424e3ae2204a3bd7f626d8717f634db91117d45249de0.jpg)

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQQD.

43

![](images/740b626591f5ab07093fce5f56e5941a17de96ea46563c4337788b0d7d0c4fe4.jpg)

# WsfSensor 专门化

![](images/af280dcd679e30bf7b6e8f02c327f8315845761ee0dc1dcdea3b8018cf0c9361.jpg)

# - 预定义传感器（Predefined Sensors）

- Acoustic（声学传感器）：一种简单的被动声学传感器，模拟人类听觉功能，用于检测和处理声波或声学信号。  
- Composite（复合传感器）：由多个传感器组成的复合型传感器，能够结合不同传感器的功能以实现更复杂的感知能力。  
- EOIR（电光/红外传感器）：一种基础的电光或红外传感器，能够检测从红外到紫外波段的电磁辐射，用于多种工业和军事应用。  
- ESM（电子支援措施传感器）：一种基础的被动雷达频率检测传感器，用于检测和识别雷达频率信号。  
- Geometric（几何传感器）：基于几何原理的基础传感器，用于通过几何关系进行目标检测和定位。  
- IRST（红外搜索与跟踪传感器）：一种基础的红外搜索与跟踪传感器，能够被动检测和跟踪目标的红外辐射信号。  
- Optical（光学传感器）：一种简单的电光传感器，用于检测可见光或近红外波段的信号。  
- OTH（超视距雷达传感器）：一种基础的超视距回波散射天波雷达传感器，利用电离层反射实现远距离目标探测。  
- RADAR（雷达传感器）：一种基础的雷达传感器，用于主动发射和接收电磁波以检测目标位置和速度。  
- SAR（合成孔径雷达传感器）：一种基础的合成孔径雷达传感器，通过移动天线合成大孔径以实现高分辨率成像。  
- Surface Wave RADAR（表面波雷达传感器）：一种表面波雷达传感器，利用地表波传播特性进行目标探测，适用于海洋监测等场景。

![](images/8032676016760fc0cb71e3b9f8a54af6b9778151802ddea4490de9d8cb99235c.jpg)

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19.

Other requests for this document shall be referred to AFRL/RQQD.

- WsfWeapon 是一种旨在阻止其他物体运行的工具（无论是永久性还是暂时性）。

- 大多数武器是“显式”武器：

- 当武器被发射时，会为该武器显式创建一个平台。

- 隐式武器则不会被表示为平台（例如，干扰器、定向能武器）。  
- 这种分类区分了武器在仿真系统中的表现形式，显式武器通过平台进行建模，而隐式武器则直接通过其功能进行建模。

![](images/9983a373b722e17c74c9e294413953404012875f1d3383f3991ee04b707f2c01.jpg)

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQQD.

45

![](images/05c7656204e1e52ffb832e26dfefc0f844a0a29322880ad3e50d281d4a145710.jpg)  
UNCLASSIFIED

# 通信(Communications)

![](images/c99c3b04a2da02f76bd63b268ed19733f99cbe18b53db1bb6cbdc2b1144c1788.jpg)

- WsfComm 对象提供了平台之间以及平台内部部件之间通信的机制。  
- 支持有线或无线通信，使用发射器、接收器和天线进行数据传输。  
- WsfComm 是所有通信实现的基类。  
这种设计允许平台通过多种通信方式进行交互，无论是通过物理连接（有线）还是无线技术（如射频或其他无线协议）。

![](images/33ff9f52ce5b509211b9fe04f869e060d15b05ef2bc0ac7ee3ae78f5988ab8f2.jpg)

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQDD.

- WsfMessage 是 AFSIM 中通信的“单位”。

- 包含许多派生类型。  
- 在平台内部，消息通过“内部链接”传递：

- 平台组件彼此解耦，便于在组件之间轻松设置通信。

- 在平台之间，消息通过“外部链接”传递：  
- 这完全依赖于 Comm 对象来实现。

- 这种设计使得AFSIM能够高效地管理平台内部和平台之间的通信，同时保持模块化和灵活性。

![](images/07212ff38cdc82d46ecf0a4e02264c229bae62ad9dc37ffb60d9276f7140ac7c.jpg)

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQQD.

47

![](images/c6f8a54cfc1769462c6da99b1276764fa888a0ba34933dc26a8c81aa89703c31.jpg)

UNCLASSIFIED

# Processors

![](images/1974fc6c7a62d458c2e4d0580dab5e12838bf1f5a993e571ec7cd4517d666db1.jpg)

- WsfProcessor 实现了平台的“行为”。  
- 处理器通过以下方式被调用：

- 从另一个“系统”接收消息。  
定期调用更新函数。  
- 调用脚本化的函数方法。

- 现在，大多数自定义处理都可以通过使用 WsfScriptProcessor 的脚本来完成。  
- AFSIM 核心中仍然包含一些自定义处理器，包括：

- WsfTaskProcessor   
- WsfTrackProcessor   
- WsfImageProcessor

Processors

![](images/27f6ccaec97f7ae87509026aaeb2e95e72ea0d394f8e51f6577e09567704e286.jpg)  
Component Based allows for Addition and Removal of Whole Types

- 平台/仿真组件类型通过名称或角色进行访问

- 允许在仿真和平台中添加或移除组件类型。  
例如：在EAR（出口管理条例）版本中移除武器和电子战（EW）组件，而在ITAR（国际武器贸易条例）版本中添加这些组件。

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQQD.

49

![](images/e09e79ce12a03aec47068ab943d660d1efca61d41abde833b2fba6477b53745b.jpg)

# WsfComponent

![](images/e7a7dffa6e642a9574f7a5eb819956b04007ad502382f7b33d2b37cdab0375e7.jpg)

没有成员变量

大多数函数需要在派生类中实现。

框架方法：

- Clone（克隆）  
- ProcessInput（处理输入）  
Initialize（初始化）

其他方法：

Get/Set>Name（获取/设置名称）  
- <Get/Set>Role（获取/设置角色）  
- InitializationOrder（初始化顺序）  
角色定义了平台组件列表中的类型  
例如：传感器（sensors）、通信（comms）、移动器（movers）、处理器（processors）、武器（weapons）等。

![](images/f8525c342fe19c24706ec20cc35c9735d0d3cd6f5fb5b37192f4f2da58765af5.jpg)

WsfPlatformComponent

WsfProcessorComponent

WsfSensorComponent

Component (for Comm)

示例：

在 WsfComponent.hpp 中，我们为平台专门化组件：

using WsfPlatformComponent = WsfComponent<Wsflplatorm>

在 WsfProcessorComponent.hpp 中，我们为处理器专门化：

class WsfProcessorComponent : public WsfComponentT<WsfProcessor> ...

在 WsfSensorComponent.hpp 中，我们为传感器专门化：

class WsfSensorComponent : public WsfComponentT<WsfSensor> ...

在 WsfCommComponent.hpp 中，我们为通信专门化：

class Component : public WsfComponentT<Comm> ...

Other requests for this document shall be referred to AFRL/KUQU.

- 提供维护和管理组件的方法：

- 添加（Add）  
移除（Remove）  
迭代（Iterate）  
查找（Find）  
- 按角色查找（FindByRole）  
回调（Callbacks）

- 添加/删除时的回调

- 为每种组件类型定义组件“角色”枚举

支持查找和按角色查找功能。

WsfComponentList

Component and Part Type Enumerations

Part Type Enumerations

有许多组件列表，例如：

- WsfComponentList   
- ComponentList（用于 WsfProcessorComponent）  
- ComponentList（用于 WsfSensorComponent）  
- ComponentList（用于通信组件）  
- WsfXioComponentList（用于WsfXIO Component）

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQQD.

# UNCLASSIFIED

![](images/e9d16045ff94cdeaffb311318c43bd86f77c534249199bc69b067cad8ab82a54.jpg)

# WsfPlatform Class Diagram

![](images/482bed0385d3f2e82f3fc09b8d1b8a47ca5bb739ffd5f739c5089ec21551bcd8.jpg)

![](images/1493ea36e14661fcc576489bfe3745076268f1964dd860ae0ea9f0d796cd0129.jpg)

- 派生自：

- WsfComponent（模板类）  
- WsfComponentList（模板类）  
- WsfObject/WsfUniqueld

- 直接访问 WsfComponentList 函数

- 平台能够作为另一个平台的组件。  
- 组合设计模式（Composition design pattern）

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQDD.

在 WsfSensor.hpp 文件中，将预定义的整数值

# Declarations:

cWSF_COMPONENT_SENSOR与WsfSensor类关联起来。

WSF.Declare_component_TYPE(WsfSensor, cWSF Component Sensor) using ComponentList = WsfComponentListT<WsfSensorComponent>;

![](images/4018e49fb3ebcdaa92cb2ad065ce4db6ab63fa15dbef67322b8dd3c593c0e9ac.jpg)

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQQD.

53

![](images/ecb69a37ccbad0d6c909e0698b99ad0c6a0588465ca04e5b923fe4f3b0662e81.jpg)

# UNCLASSIFIED

# AFSIM 额外基础设施功能

![](images/58c02b1c12a687ba3fa06ec3e1cb2b5213708e5d2ac1ca6c77aa6a3d65be0e28.jpg)

- Multi-Threading   
Event Output   
- Task Management   
- Track Management   
- Signatures   
- Weapon Effects   
- Aux Data   
- Console Output

# - 多线程

- 在事件步进和帧步进模拟中均可用。  
- 创建了一个线程池，根据传入线程池中的对象类型更新对象。  
- 目前仅移动器和传感器对象的更新利用了此功能。  
- 视线管理器和DIS接口也可以在单独的线程中运行。  
- 在“某些”虚拟模拟环境中提高了性能。  
- 注意：如果运行多线程，模拟运行的可重复性无法保证。

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQQD.

55

![](images/efac5f0eff9d276dd04ab27231dfd5cc95cd079833ad8105700d15b24df25b4b.jpg)

# Event Output

![](images/b215a00f36d36284d569a0547a67e873648b98bcd2bd95cb0e6e5ced79ccd703.jpg)

- 事件输出是一个带时间戳的模拟事件文本文件

- 事件类型是用户启用的。  
- 可用事件的列表大致遵循由 WsfObserver 发布的事件。  
- 可由事件读取器读取。  
- 可以将新的自定义事件类型添加到事件输出中。

![](images/b67ad28fd726c56c5014914adf80850461359009121c5e4ab3f194d974186b8d.jpg)

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQDD.

- 专用处理器用于发送和接收与轨迹相关的“任务分配”

- 允许用户使用有限状态机的概念对轨迹进行分类。  
用户定义一组转换规则，定义从一个状态到另一个状态转换的条件。  
- 每个轨迹维护自己的状态。

![](images/7ebc8051f3e5603147aef86b508d8bccef1d640e9b20d57703b1351df590fd1c.jpg)  
next_state IMAGING return (TasksReceivedFor(TRACK.TrackId(), "ID") > 0); end_next_state   
next_state IN-route return ((TasksReceivedFor(TRACK.TrackId(), "BDA") > 0) || (TasksReceivedFor(TRACK.TrackId(), "STRIKE") > 0)); end_next_state

Task Management

end_state

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19.

Other requests for this document shall be referred to AFRL/RQQD.

57

![](images/ee2c46fbab8188e0d89f8f3b013471e1fe0aaa16c412c5867d6bc8f88c6be3b2.jpg)

# Task Management -状态机(State Machines)

![](images/ee432336092f0ae8e8938f900f1cd08fb8a63a41bd405398e4bf62be14f822a9.jpg)

# UNCLASSIFIED

# - 状态机有:

- States   
- Events   
- Transitions

![](images/623cb35f1e7e2d5b5fe43c13c1ce17a682fa9f55be5345d3171d227d8decb5ef.jpg)  
状态机示例 - 描述门的操作

# 状态机示例 - 自动售货机

![](images/44bb4b8fcbc25fcf7d790aa8a5d4b902251a2041d3b2e04a9b9849e18adb307d.jpg)  
DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19.   
Other requests for this document shall be referred to AFRL/RQQD.

- 轨迹管理器始终可在平台上使用，负责以下任务：

- 维护“本地”轨迹的轨迹列表（WsfLocalTrack）。  
- 维护贡献的“原始”轨迹的轨迹列表（WsfTrack）。  
控制轨迹之间的关联和融合。

- 关联和融合作为可互换的“策略”实现，以便于集成。

控制轨迹的清除。  
提供跟踪事件的通知。  
充当“过滤中心”。

![](images/762959a4e10fd49325618046457a537cd49f80c08f261a6fcaac372e02187ece.jpg)

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQQD.

# UNCLASSIFIED

59

![](images/c5865b5b46ec95744114dd27dd25f0770b8d87df5f31fe19a2b423293e6ba612.jpg)

# 跟踪处理器(Track Processor)功能

![](images/d9b0474469a81b242ae2c7d5eb906c284bad9e6864763ff01bb312369cbd0505.jpg)

- 填充轨迹管理器的轨迹列表

- 从其他平台导入离线轨迹。  
- 导入在板传感器轨迹。

- 清除轨迹

如果在指定时间间隔内没有更新，则“丢弃”轨迹。

- 报告轨迹

利用与轨迹管理器的发布/订阅服务。  
报告选项包括：

批量报告。  
循环报告。  
通信所有轨迹或仅更改的轨迹。

![](images/c15a5c590d54c932c8c35b7f722ac36bf3f3d5fb8dde235b01921c51ac12a3fb.jpg)

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19.

Other requests for this document shall be referred to AFRL/RQQD.

# 轨迹关联策略：

完美关联   
- 原始轨迹与真实目标关联。  
最近邻

如果两个位置之间的距离在协方差矩阵的标准差范围内“合理”接近，则原始轨迹与另一轨迹关联。

- 聚类

- 使用聚类算法建立轨迹关联，以协方差矩阵的标准差作为聚类成员资格的判别标准。

- 真实

- 在分布式场景中有用，该算法将轨迹位置与最近的真实位置匹配，如果“合理”接近。

轨迹融合策略：

本地/“默认”

- 替换或基于协方差的加权平均，专注于运动学融合。

- 多目标跟踪（MTT；来自抑制器）

- 请参阅抑制器文档以获取算法。

- 分类数据融合是常见的，并遵循简单规则（但可能很快会改变）

- 侧面、类型简单复制。   
- IFF 根据简单的硬编码规则进行合并。  
- 辅助数据被合并/替换。

![](images/b994acca9a0aa9951299c3e3adabcce0bdd70bbae27dba9f4089a508dd4e32fb.jpg)

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQQD.

61

![](images/b3575f2295f18a7e0484198031c2c4092fc38df78986c3cad408ec1ce5ff8631.jpg)

# UNCLASSIFIED

# 目特

![](images/1a89d5a5f4eabdd5711e7c1b9166d24082cf4a2eca5b3c2571862851d42f4214.jpg)

- 签名表示平台对位于某个角度的传感器（雷达、光学等）的可见性（可探测性）。

![](images/49ffb6bde440f318f22a6e40a963cb459192a1d417ced6868acc5a5ec2f4e03f.jpg)

- WsfSignature 对象是签名的容器。目前实现了几种签名：

- WsfOpticalSignature   
- WsfRadarSignature   
- WsfInfraredSignature

![](images/0fe1603eb5ec4a391fa1b9f632b1593e678ff48f4fdf3a5ec819e1fb1c343b74.jpg)

- 签名状态允许根据平台的配置使用不同的签名表。例如，一个签名状态可能表示武器舱门关闭，而另一个则表示武器舱门打开。

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19.

Other requests for this document shall be referred to AFRL/RQQD.

- 武器效果（致命性）对象用于确定武器对平台的影响。  
- WsfLethality 是所有致命性实现的基类。AFSIM 提供了几种实现，包括：

- WsfCarltonLethality ← uses Carlton Damage Equation   
- WsfSphericalLethality ← damage inversely proportional to miss distance   
- WsfTabulatedLethality $\leftarrow$ table lookups determine damage

- 我们将作为 AFSIM 武器模块的一部分实现一个简单的武器效果。

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQQD.

# UNCLASSIFIED

![](images/779c8308cb9171b9971d001c313c43652e41910ba16a8166cdc2153eaf6ecf09.jpg)

# 辅助数据

![](images/d35a8cc49cd4f31eecb90c3c517ac6fc5c221e7ea042fd6662009fb7f8c64c3c.jpg)

- 辅助数据允许在轨迹或其他组件上放置“额外”数据，包括：

-平台  
- 任何平台部件（通信、传感器、武器、移动器等）  
- 任务  
-组  
一 路线  
- 发射器/接收器

- 基本类型（int、bool、double、string）是预定义的。  
- 还可以注册任意类型或构建结构体。  
- 通过脚本语言也可以使用这些数据。

# Signatures

ut::log::info() << "Hello World";

Creates a stream (of type info) and generates message at same time  
This stream goes out of scope immediately, send() 'ing the message

- 基本用法：

- 创建并写入一个消息流（某种类型/分类）。  
- 该流将消息发送给发布者。  
- 当流被销毁时，Send()会被隐式调用。  
- 也可以显式调用 Send() 来刷新消息到流中。  
- 发布者将消息发送给所有感兴趣的订阅者，包括控制台。  
- 控制台将消息显示在屏幕/窗口上，并在后面添加换行符。

注意：虽然可以使用 std::cout 生成控制台输出，但您应该使用 ut::log 系统，因为其他感兴趣的实体（如观察者）也可以接收生成的输出。

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQQD.

![](images/7e07f7de3901227b556361f7809cb86f4303de6a29bf41ed589c7f75f9418988.jpg)

# UNCLASSIFIED 控制台消息生成 消息类型

65

![](images/fbab10b8cb867a4ba18a4958e80ee40b08ef69083a850813572819e420c73dc9.jpg)

- Fatal

- ut::log::fatal   
- 不可修复的错误.  
- 在AFSIM中当前没有使用.

- Error

- ut::log::error   
- 可修复的错误.  
- 标记为 ***ERROR

- Warning

- ut::log::warning   
一警告  
- 标记为 ***WARNING

Info

- ut::log::info   
一般消息  
没有应用星标标签

- Debug

- ut::log::debug  
用户级调试消息  
- 标记为 ***DEBUG

- Developer

- ut::log::developer   
- 开发者级调试消息  
- 在AFSIM中当前没有使用

- 备注可以通过 AddNote 添加到消息中  
- ut::log::info 的示例
  auto out = ut::log::info() << "input command 'foobar' is deprecated staring with AFSIM 2.6";
  out.AddNote() << aInputBlock.Input().GetFooBarValue();   
- ut::log::warning 的示例
  auto out = ut::log::warning() << "'subtype' definitions are not applicable for the 'default' type."; 
  out.AddNote() << aInputBlock.Input().GetLocation(); 
  out.send();   
- 什么是备注？  
- 备注是附加到消息上的附录，包含额外的信息。  
- 备注中应包含的项目：

与消息相关的变量值  
- 错误在代码或场景文件中的位置  
描述与消息相关命令的文档引用  
用户如何解决警告或错误的说明

- 备注在控制台中将显示在单独的一行，并缩进。  
- send() 方法将流刷新到输出。  
- 当变量超出作用域时，析构函数会调用 send() 方法（刷新流）。  
- 当直接调用 send() 方法时，流会被刷新。

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQDD.

67

![](images/74a0edf28fa9b5070c40eeff11bf50451127bc70f77b0122953f6195bcb1f182.jpg)

# 编码指南 - 风格

![](images/691adf0ff0e88910daaeca4a46bdfd3fd69a00a56f85aebe4af240544b30f396.jpg)

- 请参阅AFSIM文档以获取完整的编码指南  
·大括号

- 包含代码块的大括号应放在同一列，分别在代码块的前后单独一行。  
- 始终包括大括号，即使是单行的 if 语句或 for 循环。

- 缩进使用3个空格（不应使用制表符！）。

不多也不少。  
3 应该是你所计算的数字。  
- 计算的数字应为3。  
4 不应计算。  
- 也不应计算2，除非你接着计算到3。  
- 5是不允许的。

·续行

- 续行应缩进3个空格。

\*”和“&   
- 在指针和引用变量定义中，“*”和“&”操作符应紧挨类型名称，后面跟着空格。

- 命名约定

- 标识符应使用驼峰命名法（camelCase）（除非有其他规定）。  
- 变量的名称应以小写字母开头。  
- 函数、抽象数据类型（ADTs）、结构体、类型定义（typedefs）和枚举类型的名称应以大写字母开头。  
常量和枚举值应包含一个前导的小写字母“c”。  
- 类的数据成员变量应包含一个前导的小写字母“m”。  
- 函数参数名称（形式参数）应包含一个前导的小写字母“a”。  
- 不应使用以“_”或“_”开头的标识符。  
- 指针应以“Ptr”作为后缀命名。

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQQD.

69

![](images/24f08b4a20a229c7177d0037c8234133956ea8650629ce39284dd3ad4fbaf587.jpg)

UNCLASSIFIED

# 更多指南

![](images/860e71caf4cee19749aa94f9189681691e9cdf0dd43d19e2e6ffa3efa085ed12.jpg)

- 变量

- 每个变量应在单独的声明语句中声明。  
- 每个声明的变量在使用之前都应赋值。

- 指针初始化

- 指针在声明时应始终初始化为有效值或 nullptr。

- 编写简短的函数 生命、宇宙和一切的意义是“42”

- 如果函数体超过大约 42 行代码（LOC），考虑将其拆分。

- 注释

- 所有注释应以“//”开头，除非需要支持 Doxygen 注释。

- 请参阅 AFSIM 文档以获取完整的编码指南。

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQDD.

# - AFSIM 文档

位置：./BUILD/documentation/index.html  
- AFSIM 参考指南：AFSIM 输入定义和脚本语言参考的百科全书。  
- 用户/分析师资源：

- AFSIM 用户手册：AFSIM 用户的独立手册。  
- Doxygen：使用 Doxygen 从 AFSIM 源代码生成的软件参考文档。

# - 软件开发者资源：

位置：./BUILD/doxygen/index.html

Doxygen 是一个文档系统，支持 C++、C、Java、Objective-C、Python、IDL（包括 CORBA 和 Microsoft 版本）、Fortran、VHDL、PHP、C#，以及在某种程度上支持 D。Doxygen 根据 GNU 通用公共许可证发布，是免费软件。（www.doxygen.org）

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQQD.

# UNCLASSIFIED

# 免责声明

![](images/ba51320eae619cadc5b63f3731a2cc148bfa37730dd65744693a13393f76aea8.jpg)

71

![](images/bcaba098dd3c672932d37f94ffee10394c67c45f424718cf2498aaa2f6b0c689.jpg)

- 在AFSIM培训模块中，所有战斗系统的表现均采用虚构值构建，旨在具有通用性。  
- 战斗系统的表现仅用于教授AFSIM软件的操作。  
- 培训部分中的平台、传感器和武器并不代表任何真实或拟议的战术系统。  
- 用户应自行收集和验证用于 AFSIM 分析的数据。

![](images/ace5987b897670c8956b289a33265f60e0774c8d061965eef10cfc81a0972ef4.jpg)

73

![](images/4355b96f0115e2fc34a3e7573545be03534aee6e5311943718a2c59cf16a668b.jpg)

# UNCLASSIFIED

# 更多信息/分布

![](images/f22784fd13f7f295a3de7f7a7a832d635cab7755f4001c1ae09968b6c3ae1a52.jpg)

如需更多信息，请查阅AFSIM文档  
非机密分发

- 请求DI2E账户(http://www.di2e.net)  
- 请求数字化AFSIM用户（https://dpam.di2e.net/myaccount）  
- 将 Confluence 添加到您的应用程序许可证中（注意：访问权限可能需要最多一个小时才能生效）  
- 下载所需版本 (https://confluence.di2e.net/display/AFSIM/Releases)

机密分发

联系 Brian Birkmire (brian.birkmire.1@us.af.mil, 937-255-2441)  
完成ITA，承包商需要识别适当的DD254  
- 获取 SIPR Intelink AFSIM 网站的访问权限，如果没有 SIPR 访问权限，将邮寄 DVD

![](images/2da92fc13c14c5196a6515c73e4fe93c77aef66d2480ba7688e0692d853d998d.jpg)

- 特定应用程序模型可以（并且已经）集成：

- 使用各种语言编写（C、C++、MATLAB®、Java、FORTRAN）  
- 不需要对核心框架进行更改

- 集成示例：

- 自定义代码编译为AFSIM应用程序的静态库，使用AFSIM基类并创建派生类或新类。  
- MATLAB® SIMULINK® 模型 - (“自动编码”为 C++)  
- 自定义代码编译为动态库，在运行时加载  
- AFSIM插件  
- MATLAB® 源代码和 SIMULINK® 模型（编译为 .dll）  
- 通过现有应用程序接口进行自定义通信

XIO   
MATLAB® 引擎 API  
- ExtendSim OLE/COM自动化接口

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQQD.

![](images/e7a0103b25ded8a4b52a5399ac5e13195c711d1865adbeaca011c3cbb05cac22.jpg)

# UNCLASSIFIED

# 额外问题

![](images/5722c6710394beed07ce68fb4f65a8470fb6473388fe29456e9e7a71bff01b0c.jpg)

afsim-help@vdl.afrl.af.mil

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

# 6.2.1.3. 使用 Cmake 构建 2_AFSIMDev_Trng_BuildingWithCMAKE

本文为afsim2.9_src\training\developer\core\slides\

2_AFSIM_Dev_Trng_BuildingWithCMAKE.pptx 的翻译，主要是整体介绍一下使用 CMAKE 对 AFSIM 进行构建。

![](images/25f6066bfa409eb69e309d25f2c1147219c3717c4c142890ee38aef4d423a959.jpg)

Integrity $\star$ Service $\star$ Excellence

# AFSIM开发培训

# 2- 使用CMAKE构建

本文档由杨石兴翻译，该资料做为《AFSIM2.9参考手册》的一部分。没有《AFSIM2.9参考手册》的加杨石兴微信领取：13324598743

# AFRL/RQQD 美国空军研究实验室

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

1

![](images/82cc01a6c9459047e8884a25eb0a825fce504f7854d14e0979ef2e5d950c2094.jpg)

UNCLASSIFIED

# 前提条件

![](images/d2e26f08bf9857626e653bb414c562dedc03543b0ab7effbdecc3994be6935e7.jpg)

- 在开始这个实验室之前，您应该：

熟练掌握 C++ 编程语言  
- 理解统一建模语言（UML）的基本概念  
- 熟悉 WIZARD 和 WSF 脚本语言

- 建议参加AFSIM分析师课程或具备同等经验

- 能够使用 Microsoft® Visual Studio 2017® 编译应用程序，并对此熟悉  
- 熟悉使用 Microsoft Windows® 资源管理器  
- 安装最新版本的 WIZARD 和 AFSIM 集成开发环境（IDE），并对此熟悉（已提供）

在参加本课程之前，您应该能够掌握以下内容：

C++基础知识

描述并使用以下 $\mathsf{C} + +$ 基础知识：

构造函数和析构函数  
- 虚函数  
函数重载  
运算符重载   
- 访问器和修改器  
单继承和多继承  
模板  
异常处理

统一建模语言（UML）基础知识

描述并使用以下UML基础知识：

类图  
时序图  
- 聚合关联   
- 组合关联   
- 访问器和修改器  
复合类

- 使用环境

- 使用 Microsoft Windows® 环境以及 Microsoft® Visual Studio 2017® 或

Microsoft® Visual Studio 2019® 集成开发环境（IDE）。

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19.

Other requests for this document shall be referred to AFRL/RQQD.

3

![](images/27eea58247e175fc4287f322d328d6e3ea2cdf6ca7d45f77c6c8b6811511134d.jpg)

# UNCLASSIFIED

# 环境搭建

![](images/f0353a1c2494d5f41b43f1dbfae3cb6c27a601319a6e19a18dd91b2ec0342c3f.jpg)

要完成本课程中的实验室，您需要以下内容：

基于 Microsoft Windows® 的计算机（Windows 7 或更高版本）  
- Microsoft® Visual Studio 2017®   
- MATLAB® 或 MATLAB® 编译器运行时（MCR）（已提供）  
- AFSIM 可执行文件（仿真运行时可执行文件 - 插件版本）

- 我们将在下一个模块中构建此内容

- AFSIM WIZARD（已提供）  
AFSIMMYSTIC（已提供）  
- Python（公共领域编程语言；可选）  
- CMake（VS 2017 需要 3.8 或更高版本，VS 2019 需要 3.14 或更高版本）

实验室起始点

- 每个实验室的起始点位于：  
- <afsim-install folder>\training\developer\core\Labs\inwork   
实验室解决方案  
- 每个实验室的解决方案位于：  
- <afsim-install folder>\training\developer\core\Labs\solution   
- 您将在inwork目录中进行工作。

在开始之前，请花几分钟时间设置您的环境：

1. 确保您拥有本地管理员权限。  
2. 工作目录的读/写权限。  
3. 验证已安装带有编译器的 Visual Studio 版本。

- 2017版本必须安装最新的服务包。

4. 您的讲师可能会提供额外的副本，仅用于本次培训。  
5. 获取AFSIM版本的副本，包含以下内容：

- AFSIM 软件分发，包括源代码  
- 开发者培训练习和幻灯片  
- AFSIM 和开发练习的文档

- 确保以上所有准备工作都已完成，以便顺利进行培训。

![](images/e597badf80af7af650b9f2c595100cc68e05cb25b6edc2b84fda22964bed1e57.jpg)

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

5

![](images/1fa6d4cc7ff8518504041e1e8b7f88b147fe43e54572487a131461f08f4096b3.jpg)

# UNCLASSIFIED

# 准备培训 (cont.)

![](images/2dfa9d5ac1ccbebd3724f933e9632719b32e7b36108cfa0df0c634e1bb3eeadd.jpg)

- 将AFSIM安装到您拥有完全读/写权限的目录中：

- 将其放置在桌面上通常是可行的。  
- 可选：将快捷方式放置到.../3rd_party/cmake/bin/cmakegui.exe 到您的桌面上。  
如果您已安装AFSIM的发布版本，请确保在swdev/dependencies文件夹中安装了3rd_Party资源和VTK资源。

- 好的！让我们开始吧！

![](images/d8ccb9c7b435cad04e48f092a74c90fdbbb83faef8205b61c9894591cce3fc14.jpg)

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

6

- AFSIM 使用 CMake 进行构建配置。本演示描述了在 AFSIM 中使用 CMake 的最佳实践。  
- 您可以从
http://www.cmake.org在线获取 CMake。CMake 提供了一个名为cmake-gui 的工具，如右侧所示。这个工具使得自定义 AFSIM 构建变得更加简单。

![](images/be99bccb97dba1bfce8855d7b9288d192ca9ec2f5f0ba20c97e1aa9420d971ba.jpg)

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

7

![](images/7ce27a087c6f3408ac7f3c597e2500955e258450ad844caa0da23ba1afc29c0c.jpg)

# UNCLASSIFIED

# 为什么使用CMake?

![](images/ee708abf5e09068c07dba0ad8b5019c74b3f5fedb7f3df7cbbc9cda192db44bd.jpg)

- 早期版本的框架使用了一组 Windows Visual Studio 项目文件和自定义的 Linux makefile 系统。这在新项目和文件不经常添加时是可以接受的。然而，对于现代的 AFSIM 来说，情况并非如此！  
- CMake 通过提供一套单一的配置文件，理论上解决了配置管理问题，使得可以构建任何 Windows、Linux（或其他）配置。请查看项目目录中的“CMakeLists.txt”文件和“misc”目录中的配置文件。  
- AFSIM 对 CMake 的使用已经成为管理大量新可选项目、可执行文件和插件的不可或缺的工具。

![](images/2d59369a9fff83157557e5f0dd423ab39922d0dd599747abd86477bd846b663c.jpg)

- 有时构建过程中会出现问题。这种布局允许我们安全地销毁构建目录而不会丢失数据。

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

UNCLASSIFIED

# 一般开发者文件夹层次结构

9

![](images/4426fad0335bc926f789f51fcc8bd1ca5e3ff213b9641bf654be21e6e0090271.jpg)

![](images/23fdae30f626be3df5ec1a28c867f583a6a4f3e8b20459752de20eef83235b7d.jpg)

<table><tr><td>文件夹</td><td>目的</td></tr><tr><td>../afsim</td><td>主要源代码文件夹，存储在 Git Lab 上的代码库。</td></tr><tr><td>../afsim_shared</td><td>额外的源代码，用于管理与 AFSIM 相关的模型、分析场景、生成报告以及管理某些类型的通信。</td></tr><tr><td>../build</td><td>构建文件夹，所有二进制文件在此创建。</td></tr><tr><td>../demos</td><td>主要场景文件夹。</td></tr><tr><td>../demos_shared</td><td>额外场景文件夹。</td></tr><tr><td>../devtools</td><td>用于拉取 AFSIM 代码库的 Git 工具。</td></tr><tr><td>../resources</td><td>地图和模型资源。</td></tr><tr><td>../tools</td><td>各种转换和分析的脚本。</td></tr><tr><td>../training</td><td>培训内容文件夹。</td></tr><tr><td>../bin</td><td>AFSIM 可执行文件的打包版本。</td></tr><tr><td>../demoos</td><td>主要场景文件夹。</td></tr><tr><td>../documentation</td><td>主要文档文件夹。</td></tr><tr><td>../resources</td><td>地图和模型资源。</td></tr><tr><td>../swdev/build</td><td>主要 AFSIM 构建文件夹。</td></tr><tr><td>../swdev/resources</td><td>存放 3rd_party 工具和 vtkResources 的文件夹，用于离线构建（无访问 git 代码库）。</td></tr><tr><td>../swdev/resources</td><td>存放生成的地图、模型和 vtk 资源的文件夹。</td></tr><tr><td>../swdev/src</td><td>主要 AFSIM 源代码文件夹。</td></tr><tr><td>../tools</td><td>各种转换和分析的脚本。</td></tr><tr><td>../training</td><td>培训内容文件夹。</td></tr></table>

注意：在../swdev/src中的所有内容都可以在从Git代码库中提取的开发者文件夹结构中的../afsim_dev/afsim文件夹中找到。

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19.

Other requests for this document shall be referred to AFRL/RQQD.

11

![](images/58833d3aa21980adc1910bce8264521261bbd6cff304daf3b10a0e68e498781d.jpg)

# AFSIM源代码库文件夹层次结构

Either: ..swdev/src or ..afsim_dev/afsim

![](images/74ce47db6cf7acedc8063b48d198bd16e8eb040367b52b4ba2d6a20f1d84c315.jpg)

<table><tr><td>文件夹</td><td>目的</td></tr><tr><td>../cmake</td><td>大多数CMake文件都在这里。</td></tr><tr><td>../core</td><td>任务的核心源代码文件。</td></tr><tr><td>../doc</td><td>用于构建文档的.rst文件。</td></tr><tr><td>../engage</td><td>用于分析武器有效性和目标脆弱性的工具。</td></tr><tr><td>../mission</td><td>任务的主要源代码文件。</td></tr><tr><td>../mystic</td><td>Mystic结果可视化工具的源代码文件。</td></tr><tr><td>../sensor_plot</td><td>用于构建传感器图的工具。</td></tr><tr><td>../tools</td><td>各种工具和实用程序。</td></tr><tr><td>../warlock</td><td>Warlock的源代码文件。</td></tr><tr><td>../weapon.tools</td><td>用于生成射击表、发射可接受区域和其他表格数据的工具。</td></tr><tr><td>../wizard</td><td>Wizard的源代码文件。</td></tr><tr><td>../wsfPlugins</td><td>插件，如Brawler、P6DOf等。</td></tr><tr><td>../tools</td><td>在: ../afsim/tools 或 ../swdev/src/tools</td></tr><tr><td>3rdParty-cmake</td><td>第三方工具的 CMake 文件。</td></tr><tr><td>dis</td><td>分布式交互式仿真（IEEE 标准 1278）。</td></tr><tr><td>genio</td><td>Genio 库，用于轻松设置 TCP、TCP 服务器和 UDP 连接。</td></tr><tr><td>misc</td><td>执行测试的杂项脚本。</td></tr><tr><td>packetio</td><td>各种数据包类型的序列化/反序列化。</td></tr><tr><td>tracking_filters</td><td>用于传感器/跟踪器的过滤器，以生成目标位置/速度估计。</td></tr><tr><td>util</td><td>单位、向量、表格、时钟、线程、输入等的实用工具。</td></tr><tr><td>util_script</td><td>脚本实用工具。</td></tr><tr><td>utilosg</td><td>OSG 图形模型。</td></tr><tr><td>utilqt</td><td>用于构建 GUI 的 Qt 相关工具。</td></tr><tr><td>vespatk</td><td>创建和管理地图显示的工具。</td></tr><tr><td>wkf</td><td>用于创建 Wizard/Warlock/Mystic GUI 的通用框架。</td></tr></table>

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

# UNCLASSIFIED

# AFSIM 源文件夹层次结构

13

![](images/39754cd62d3c8ea27d0bf5feb5e765db3007de337608c0693254f4a3737b7533.jpg)

![](images/0a501ab85eba6d9233b5cb1ce88508278345d1957e2308a645b46bbf6a118271.jpg)

<table><tr><td>文件</td><td>目的</td></tr><tr><td>.../core</td><td>在: ../afsim/core 或 ../swdev/src/core</td></tr><tr><td>sensor_plot_lib</td><td>用于评估传感器特性和交互的源代码。</td></tr><tr><td>wsf</td><td>核心建模和仿真环境的源代码。</td></tr><tr><td>wsf_cyber</td><td>实现网络战的源代码。</td></tr><tr><td>wsf_Cyber_check</td><td>检查语法是否正确解析的扩展源代码。</td></tr><tr><td>wsf_l16</td><td>实现 Link16 接口命令的源代码。</td></tr><tr><td>wsf_mil</td><td>实现武器的源代码。</td></tr><tr><td>wsf_mil_parser</td><td>解析 wsf_mil 语法的扩展源代码。</td></tr><tr><td>wsf_mtt</td><td>多目标跟踪器的源代码。</td></tr><tr><td>wsf_nx</td><td>非可导出代码的源代码。</td></tr><tr><td>wsf_parser</td><td>AFSIM 语法解析器的源代码。</td></tr><tr><td>wsf_ripr</td><td>反应式集成规划架构框架的源代码。</td></tr><tr><td>wsf_space</td><td>实现空间功能的源代码。</td></tr></table>

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19.   
Other requests for this document shall be referred to AFRL/RQQD.

<table><tr><td>文件夹</td><td>目的</td></tr><tr><td>../mystic</td><td>在: ../afsim/mystic 或 ../swdev/src/mystic</td></tr><tr><td>exec</td><td>Mystic 的主函数，在运行时执行。</td></tr><tr><td>lib</td><td>包含 Mystic 的布局、地图定义、插件管理器等代码。</td></tr><tr><td>plugins</td><td>Mystic 支持的所有插件。</td></tr><tr><td>python</td><td>用于运行各种示例的 Python 代码。</td></tr></table>

<table><tr><td>文件夹</td><td>目的</td></tr><tr><td>../warlock</td><td>在: ../afsim/warlock 或 ../swdev/src/warlock</td></tr><tr><td>data</td><td>用于某些 Warlock 测试的场景文件。</td></tr><tr><td>plugins</td><td>包含所有 Warlock 的插件。</td></tr><tr><td>warlock_core</td><td>Warlock 的核心代码。</td></tr><tr><td>warlock_exec</td><td>包含 Warlock 的主函数和 Warlock 应用扩展。</td></tr></table>

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

UNCLASSIFIED

# AFSIM 源文件夹层次结构

15

![](images/ddf4ae694b27ffb199e4fb484f815aaef253d421505485063e5d243ba7328d76.jpg)

![](images/54ce6294aa20533b848395a3f089f3073a9defa0c52038755d590d5cb9a9baaa.jpg)

<table><tr><td>Folder</td><td>Purpose</td></tr><tr><td>../wizard</td><td>在: ../afsim/wizard 或 ../swdev/src/wizard</td></tr><tr><td>exec</td><td>Mystic 的主函数，在运行时执行。</td></tr><tr><td>lib</td><td>包含 Mystic 的布局、地图定义、插件管理器等代码。</td></tr><tr><td>plugins</td><td>Mystic 支持的所有插件。</td></tr><tr><td>python</td><td>用于运行各种示例的 Python 代码。</td></tr></table>
CMake 生成构建文件的说明

- CMake生成的文件类型

CMake会根据操作系统生成不同的构建文件：

- 在Linux系统上，CMake生成Makefiles。

- 在Windows系统上，CMake生成Visual Studio项目文件。

选择构建目录

选择一个位于源代码目录之外的构建目录。这种做法有以下好处：

- 将构建文件和源代码文件分开，保持目录结构清晰。

-避免版本控制工具（如Git）提示将构建文件添加到源代码管理中。

- 标准目录结构

我们使用以下标准目录布局：

-“src”：顶级代码目录，存放源代码文件。

- "build": 构建目录, 存放生成的构建文件。

- "dependencies": 依赖目录，包含第三方工具和 vtk resources。

- 这种目录结构有助于保持项目的组织性和可维护性，同时避免构建文件污染源代码目录。

swdev/ /src/ - code directory /core/ /tools/ /wizard/ /dependencies/ /3rdParty - directory for $3^{\mathrm{rd}}$ Party tools /resources - directory for vtk-resources /build/ - build directory /build_mission/ /buildobserver exercice/

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19.

Other requests for this document shall be referred to AFRL/RQQD.