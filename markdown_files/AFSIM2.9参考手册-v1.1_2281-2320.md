- 对于每个仿真扩展，仿真会调用 Initialize 方法。  
- 完成 UDP_Observer::Initialize 的实现:

- 创建一个新的 GenUDP_Connection:

- 使用 new 操作符创建一个指向新 GenUDP_Connection 的指针。  
- 将 GenUDP_Connection 指针分配给类成员变量 mConnectionPtr。  
- 使用 GenUDP_Connection 的 Init() 方法初始化连接（传入成员变量 mAddress 和 mPort）。  
- 请参考 Visual Studio 解决方案中 genio 项目的头文件 GenUDP_Connection.hpp 以确保语法正确。

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

58

![](images/8f7898667d472541468533e3766b73d3e47d9593120b29c65dbe5cdb90105ab3.jpg)

# Observer 练习—任务5 解决方案

# UDP_Observer.cpp

![](images/b273b3222c7ca8d1a05f0c709655cf4e5e8784cf2a0845308593b73c47b4fa7a.jpg)

```cpp
bool UDP_Observer::Initialize()
{
    if (mAddress.empty())
    {
        Disconnect();
        return true;
    }
    bool connected = false;
    // EXERCISE 1 TASK 5
    // Create a new connection and initialize
    // Create a new GenUDP_Connection and assign it to class member mConnectionPtr.
    // Initialize the GenUDP_Connection using the Init() method.
    // Refer to the header file GenUDP_Connection.hpp in the
    // genio project of the Visual Studio solution for correct syntax.
    // Ensure local variable 'connected' is set to true if connection is successfully initialized
    mConnectionPtr = new GenUDP_Connection();
    connected = mConnectionPtr->Init(mAddress, mPort); 
```

}

- 对于每个仿真扩展，仿真会调用 Initialize 方法。

- 检查对额外 WsfObserver 事件的订阅：

- SensorTrackUpdated 和 SensorTrackInitiated。

- 我们最终将编写这些 UDP_Observer 函数，以响应任何已订阅的回调。  
- 本地成员变量 mCallbacks 用于保存为 WsfObserver 回调添加的订阅。

- 注意：如果 GenUDP_Connection 类成功初始化，Initialize 方法返回 true，否则返回 false。

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

60

![](images/ea50be3fa0123c156a7af5a45258916d9019b8ee65d170b775b11ffc69676921.jpg)

# UNCLASSIFIED Observer 练习一 检视 2

UDP_Observer.cpp

![](images/e0a29e73149444efc90c3df1a4506aaa9adb049da6386cb8139a10e4f152f128.jpg)

```cpp
bool UDP_Observer::Initialize()
{
    // On successful connection subscribe to additional events
    // See WsfObserver.hpp for all typedefs of all AFSIM-provided available events if (connected)
    {
        mCallbacks.Add(WsfObserver::SensorTrackUpdated(&GetSimulation().Connect (&UDP_Observer::SensorTrackUpdated, this));
        mCallbacks.Add(WsfObserver::SensorTrackInitiated(&GetSimulation().Connect (&UDP_Observer::SensorTrackUpdated, this));
        return connected;
    }
} 
```

在文件 UDP_Observer.cpp 中:

- 任务 6a: 类似于 SensorTrackUpdated 和 SensorTrackInitiated 方法如何作为回调连接到同名的 WsfObserver 事件, 编写一条语句以同样的方式将 PlatformAdded 方法连接为回调。  
- 任务 6b: 类似于 SensorTrackUpdated 和 SensorTrackInitiated 方法如何作为回调连接到同名的 WsfObserver 事件, 编写一条语句以同样的方式将 PlatformDeleted 方法连接为回调。

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

62

![](images/390b56dfcc4067a0bed7ffb65a6224b7d6b916472f699ae09a9da7424921a4e8.jpg)

# Observer 练习—任务6 解决方案

UDP_Observer.cpp

![](images/fa724d1406e080b0545a61f9e80279d040e8ea4b0207c1777541b63c97630c37.jpg)

```cpp
bool UDP_Observer::Initialize()
{
    // On successful connection subscribe to additional events
    // See WsFObserver.hpp for all typedefs of all AFSIM-provided available events
    if (connected)
        mCallbacks.Add(WsFObserver::SensorTrackUpdated(&GetSimulation().Connect &
            &UDP_Observer::SensorTrackUpdated, this));
        mCallbacks.Add(WsFObserver::SensorTrackInitiated(&GetSimulation().Connect &
            &UDP_Observer::SensorTrackUpdated, this));
    // EXERCISE 1 TASK 6a
    // connect PlatformAdded to the WsFObserver event of the same name
    mCallbacks.Add(WsFObserver::PlatformAdded(&GetSimulation().Connect &
            &UDP_Observer::PlatformAdded, this));
    // EXERCISE 1 TASK 6b
    // connect PlatformDeleted to the WsFObserver event of the same name
    mCallbacks.Add(WsFObserver::PlatformDeleted(&GetSimulation().Connect &
            &UDP_Observer::PlatformDeleted, this));
} else
{ return connected; } 
```

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

- 在本练习中，我们选择将场景输入的处理推迟到仿真扩展类 UDP_Observer 中进行。

- 因此，我们在 UDP_Observer 中声明并定义了一个非虚的、非重写的 ProcessInput 方法，并让场景扩展调用此方法来处理输入命令。

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

# UNCLASSIFIED

![](images/90a5dc81212c98b95f03fc1a5339b848ab3bb8aa7db9118ce9441022afd1ef29.jpg)

# Observer 练习—任务7

![](images/31fcb8fefc5e483bedb86ffca74416c0e1503704445b3c4b956baf510ad71836.jpg)

- 在文件 UDP_Observer.hpp 中，处理场景输入文件中 UDP_Observer 的关键字，并将值分配给 UDP_Observer 类的适当成员变量：

- 任务 7：需要处理以下代码块：udp observer 和 endudpobserver。

- 完成用于查找初始udpobserver块标识符的if语句。

可以通过在源代码中搜索对“ReadCommand”的引用来找到AFSIM的示例。

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

11

//! Process input from the AESIM input file.

bool UDP_Observer::ProcessInput(UtInput& aInput)

{

bool myCommand = false;

// EXERCISE 1 TASK 7

if (aInput.GetCommand() == "udpobserver")

myCommand $\equiv$ true;

// UtInputBlock automatically stops when end_udp observer is found  
UtInputBlock block(aInput);

std::string command;

while (block.ReadCommand commanded))

1

}

return myCommand;

![](images/a1fa14d64917ecbd8efda71897a1c93e5ab4bae269ba147d36314875bc28afbb.jpg)

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19.

Other requests for this document shall be referred to AFRL/RQQD.

# UNCLASSIFIED

# Observer 练习—任务8

![](images/c9305dd04969457f55ba51b6ba7b2781a52d94d6df3ee91c9607a016b64be3fe.jpg)

- 在文件 UDP_Observer.hpp 中，处理场景输入文件中 UDP_Observer 的关键字，并将值分配给 UDP_Observer 类的适当成员变量：

- 任务8a：需要处理命令port的输入值。

- 调用alInput.ReadValue方法，并传入成员变量mPort。

- 任务8b：需要处理命令address的输入值。

- 调用 alInput.ReadValue 方法，并传入成员变量 mAddress。

可以通过在源代码中搜索对“ReadCommand”的引用来找到AFSIM的示例。

bool UDP_Observer::ProcessInput(UtInput& aInput)

{ bool myCommand $=$ false; //EXERCISE 1 TASK 6 if(aInput.GetCommand() $= =$ "udpobserver") { myCommand $=$ true; //UtInputBlock automatically stops when endudpobserver is found UtInputBlock block(aInput); std::string command; while(block.ReadCommand commanded) { //EXERCISE 1 TASK 8a if command $= =$ "port) { aInput.ReadValue(mPort); } //EXERCISE 1 TASK 8b else if (command $= =$ "address") { aInput.ReadValue(mAddress); } else { throw UtInput::UnknownCommand(aInput); } } return myCommand;

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19.

Other requests for this document shall be referred to AFRL/RQQD.

68

![](images/70f86f69bb800bcdca31f814528564ab76a44fa0db0c3fdcb4b121de2fce5ac5.jpg)

# UNCLASSIFIED

# Observer 练习— 任务 9

![](images/a6de44af4d6a6a0f58fcbead319ee704ec98eb43118f6731b2895d1b7892cd94.jpg)

- 任务9a：完成UDP_Observer::PlatformAdded的实现

1. 检查 WsfPlatform.hpp 和基类 WsfObject.hpp。  
2. 注意其中的方法GetName和类型的。  
3. 创建一个字符串，格式为：

"PlatformAdded, <time>, <name>, <type>"

1. <time>是仿真时间参数。  
2. <name>是平台的名称（通过GetName获取）。

3. <type>是平台的类型（通过GetType 获取）。

4. 使用 aPlatformPtr 参数访问所选方法，获取数据（如平台的名称和类型），并将其写入字符串中。  
5. 将包含所选数据的字符串发送到 UDP_Observer::SendPacket 函数（该函数是 UDP_Observer 类的一部分）。

- 任务9b：以类似方式完成UDP_Observer::PlatformDeleted方法的实现。  
- 任务9c：以类似方式完成SensorTrackUpdated方法的实现：

1. 还需要打印 aTrackPtr 的 TargetIndex（通过 GetTargetIndex 获取）。  
2. 还需要打印平台的纬度、经度和高度：

- 通过调用 aTrackPtr->GetLocationLLA(lat, lon, alt) 获取这些值。注意：如果使用 std::stringstream 来保存数据，则调用 SendPacket 的语法如下：: SendPacket(ss.str());

此任务可以通过多种方式解决。一个类似任务的常见方法可以在文件 WsfScriptPlatformClass.cpp 中找到，其中方法 WsfScriptPlatformClass::ToString 使用了一个名为 ss 的局部变量，其类型为 std::stringstream。

```cpp
void UDP_Observer::PlatformAdded(double aSimTime, WsfPlatform* aPlatformPtr) 
```

{

// EXERCISE 1 TASK 9a   
```cpp
stringstream ss;
ss << "PlatformAdded," << aSimTime
<< ', ' << aPlatformPtr->GetName()
<< ', ' << aPlatformPtr->GetType());
SendPacket(ss.str());
}
void UDP_Observer::PlatformDeleted(double double aSimTime, WsfPlatform* aPlatformPtr)
{
// EXERCISE 1 TASK 9b
stringstream ss;
ss << "PlatformDeleted," << aSimTime
<< ', ' << aPlatformPtr->GetName()
<< ', ' << aPlatformPtr->GetType();
SendPacket(ss.str());
} 
```

```cpp
void UDP_Observer::SensorTrackUpdated(double aSimTime, WsfSensor* aSensorPtr, const WsfTrack* aTrackPtr) 
```

{

// EXERCISE 1 TASK 9c   
```erlang
stringstream ss;
double lat, lon, alt;
aTrackPtr->GetLocationLLA(lat, lon, alt);
ss << "SensorTrackUpdated," << aSimTime
<< ', ' << aSensorPtr->GetName()
<< ', ' << aSensorPtr->GetPlatform() -> GetIndex()
<< ', ' << aTrackPtr->GetTargetIndex()
<< ', ' << lat
<< ', ' << lon
<< ', ' << alt;
SendPacket(ss.str()); 
```

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

70

# - 检视和理解：

//   
///!Destroy the socket,and disconnect from all callbacks.   
void UDP_Observer::Disconnect()   
{ delete mConnectionPtr; mConnectionPtr $\equiv$ nullptr; //It is good practice to disconnect from callbacks you don't need to //reduce overhead. mCallbacks.Clear();   
}   
//   
///!Send a UDP packet given a packet type ID and a buffer of data   
void UDP_Observer::SendPacket(const std::string& aMessage)   
{ int bytesWritten $=$ mConnectionPtr->SendBuffer(aMessage.c_str(),aMessage.length(）+1); if(bytesWritten<0) { ut::log::error()<<"Socket error:" << GenSocketManager::GetLastError(); Disconnect(); }   
}

![](images/08cd25ab9b645e260b293b6048ae64fa57ce5475fb44c130780c6de76a55bb74.jpg)

- UDP_Observer 和 WsfObserver 存在于 AFSIM 应用程序中。

- UDP_Observer 订阅了 WsfObserver 发布者的 4 个事件。  
- 当事件发生时，发布者会通知 UDP_Observer。  
- UDP_Observer 的回调方法会创建一条消息，并调用 SendPacket 方法。  
- UDP数据包通过网络流向一个独立的应用程序（receiver.exe）。

- receiver.exe（或receiver.py）是一个独立于AFSIM的应用程序：

- 它接收数据包，提取消息，并将其发送到屏幕进行显示。

![](images/885577e37b89be21039a7c95a6d066be195d49bb9a1a292290d38d8a3492a67d.jpg)

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

# UNCLASSIFIED

![](images/02abad7d022354f35737b367de32c5b8331e265c06f5aabfa3397b79627dafe6.jpg)

# 测试(1/3)

![](images/396b72023aa262e7087fff6069deae3653d5a3b8f7dc63ed05c401e39a276642.jpg)

72

- 从 Visual Studio 中执行以下步骤：

1. 在 Release 模式下构建解决方案。  
2. 构建 INSTALL 项目。

Linux: from the build directory, run:
$ cmake --build . --target all -- -j11
$ cmake --build . --target install -- -j11

- 加载测试场景到 WIZARD 中:

1. 打开 WIZARD（位于 /bin/ 文件夹中）。  
2. 找到名为 observerscenario.txt 的顶级场景文件，该文件位于路径：training\developer\core\Labs\inwork\observer\Data。这是我们用来测试程序的输入文件。

3. 将 observerscenario.txt 拖放到 WIZARD 中。

![](images/70277510e62695073b5b1e50e29ef062f4c28600b2b77499a74022be0eea4582.jpg)  
DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

# UNCLASSIFIED

# 测试(3/3)

74

![](images/28dce45d9cc70e03809d341aa2b4a896dc98a050260b2f462b4bf281b49748fc.jpg)

![](images/396015db8af23191070f277f5c487b2b25774e28837e24f0826d8a8506c81e8d.jpg)

- 设置并运行 Receiver 应用程序

- Receiver 应用程序接收从 UDP_Observer 发送的数据，并将消息显示在 STDOUT 上。

- 有两种选项：

- 执行一个名为 receiver.py 的 Python 脚本。：

Command line window (.observer)

>pythonreceiver.py

- 运行提供的“receiver”应用程序，该应用程序是基于WSF core library和genio构建的：

Command line window (.observer)

receiver/bin/receiver.exe

- 从 WIZARD 中运行所选的应用程序

- (点击 Play)

![](images/b0cd9c38efbda112bbeb24ee1c469ff81454a0c145fb603eaa2e4ce981b2108a.jpg)

![](images/2d5fd10289d8d8561fd8a1a22a999a306840b33ccf58396c46764dabb8029a45.jpg)

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQDD.

UNCLASSIFIED

![](images/5b2626f387f471b191bfe610732480936b87fba2bcfa3a8ddb7468a61f1183f8.jpg)

76

![](images/71611504b5e1307216c695ed916b63fabf07d8e0c3b6795dc56db317390fddd6.jpg)

![](images/7171ae168bc9bc09a64e11b12a6935c0ad0d3eaa6b36d03c8c47f0db1aed979b.jpg)

77

# 6.2.1.10. 通信 9_AFSIMDev_Trng_Communications

本文为afsim2.9_src\training\developer\core\slides\

9_AFSIM_Dev_Trng_Communications.pptx 的翻译，主要是介绍如何扩展自定义通信，并做了许多小练习。

![](images/5df25d6f71d1b4790cc5bd739acbb7707b10819614047e6ba0783a17f22fffe8.jpg)

Integrity $\star$ Service $\star$ Excellence

# AFSIM开发培训

# 9-通信

本文档由杨石兴翻译，该资料做为《AFSIM2.9参考手册》的一部分。没有《AFSIM2.9参考手册》的加杨石兴微信领取：13324598743

# AFRL/RQQD美国空军研究实验室

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

# UNCLASSIFIED

![](images/5eee80d8cf2e8fbf50c0b90d212467679b7a28f3013fbb14581395e9760c26b3.jpg)

# 缩写和术语

![](images/da3820d2ea075b4d9458ab65c46f355f34e9e6124a5b7b24b5e915aed0e11d2e.jpg)

AFSIM - Advanced Framework for Simulation, Integration, and Modeling

AGL – Above Ground Level

DIS - Distributed Interactive Simulation

DTED - Digital Terrain Elevation Data

EO/IR - Electro-Optical/Infra-Red

ESM - Electronic Support Measure

FOV - Field Of View

GUI - Graphical User Interface

HLA-High Level Architecture

IEEE - Institute of Electrical & Electronics Engineers, Inc.

JTIDS - Joint Tactical Information Distribution System

MSL - Mean Sea Level

PDU - Protocol Data Unit

RCS - Radar Cross Section

SAM-Surface-to-Air Missile

SAR - Synthetic Aperture Radar

VESPA - Visual Environment for Scenario Preparation and Analysis

WKF-Warlock Framework

WSF - World Simulation Framework

dB - decibels

dBsm - decibel square meters

deg-degrees

ft-feet

GHz-GigaHertz

kts-knots

m - meters

m^2-square meters

mw-megawatts

nm - nautical miles

s - seconds

- 本实验演示了如何创建一个新的AFSIM通信设备和一个新的AFSIM消息。  
- 此外，将使用分布式交互式仿真（DIS）接口，通过DIS Signal Protocol Data Unit (PDU)发送新消息。  
- AFSIM 通信设备 是一个平台组件，它提供了在平台之间发送消息（WsfMessage）的手段。  
- 以下练习提供了操作AFSIM通信的实践机会：

- 练习1：注册一个默认的应用程序扩展、新的场景扩展和新的仿真扩展。  
- 练习2：  
- 为通信场景实现ProcessInput方法。  
- 创建一个自定义的AFSIM通信设备和消息。

- 练习3：创建一个自定义的AFSIM通信脚本接口。

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

# UNCLASSIFIED

# 问题陈述

![](images/8868c8f5ac9b933d5218392950f318d3d97abd4828b9f15b7e009cd87b812afd.jpg)

3

![](images/073d7953a97e11085b137cbf24d1ae5108d37eb5b7890c94ed1ee574ee1e0574.jpg)

- 创建一个新的通信设备类型，称为 SIGNALCOMM，以及一个新的消息类，称为 LocationMessage。  
- SIGNALCOMM 应具备以下功能:

- 能够发送所有核心消息类型，包括新的 LocationMessage。  
- 每当 SIGNALCOMM 设备发送新的 LocationMessage 时，该消息还将通过 DIS 接口使用 Signal PDU（协议数据单元）发送，包含 LocationMessage 的内容。

- 其他支持 DIS 的仿真系统可以读取 LocationMessage。

参考资料：

- AFSIM 开发者基于 Web 的数据。  
- AFSIM 源代码和 Visual Studio 搜索功能。  
- AFSIM文档。

![](images/3b4cd4cd9f31cb192bab1a953fc9c29957d5f7fa8379414e49b5523397861af9.jpg)

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19.

Other requests for this document shall be referred to AFRL/RQQD.

- 您将获得以下实践知识：

- 创建新的通信设备类型和消息类型。  
- 为新的通信设备实现发送和接收方法。  
- 使用自定义数据打包和解包 DIS Signal PDU。  
- 强化创建默认应用程序扩展和插件的技能。

- 新的脚本类型由场景扩展注册。

- 强化创建仿真扩展和场景扩展的技能。  
- 理解如何扩展现有脚本类以包含新方法，而无需修改核心代码。

![](images/4dca4f76296b0c76e56ab093a7f6ab8cc2a5bde176fb047c99131cd9ee5adc89.jpg)

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

# UNCLASSIFIED

![](images/6c37b3ba052d506b0533af484fe7c2a2bcf37b1903c1689ff5683c876f94375e.jpg)

# 先决条件

![](images/f763f8288c7f58355268aebb2e5f143f8d83b1d4304e93fa34e0194f50e507f7.jpg)

- 在开始本实验之前，您应该：

- 熟悉 Wizard 和 AFSIM 脚本语言。  
- 建议参加过AFSIM分析课程或具有同等经验。  
- 能够使用 Microsoft® Visual Studio 2017® 或更新版本来编译应用程序，并对此工具熟悉。  
- 熟悉使用 Microsoft Windows® Explorer。  
- 安装并熟悉使用最新版本的Mystic。

Mystic is an interactive software environment for analyzing AFSIM results.

- AFSIM在其基础框架中包含了一套强大的通信和消息选项。  
- 通过使用 $\mathrm{C} + +$ 架构，开发人员可以扩展类以创建新的通信设备和消息类型。

# AFSIM应用程序

# AFSIM框架

# 基础设施

想定管理

时间管理

地理空间数据管理

插件管理

# 接口

脚本语言

分布式接口

观察者

扩展

# 组件

# 平台组件

运动

传感器

传感器

组件

武器

武器组件

通信

通信组件

处理器

处理器组件

.

$\frac{1 + u}{1} - \frac{u}{1} = \frac{\left( {1 + u}\right) u}{1} < \frac{u}{1} = u$

其它

平台组件

非平台组件

![](images/f833e9236ff172c1043ff4f20c14076e8e79588c946d87aa4f06273c1ec2438d.jpg)

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

7

# UNCLASSIFIED Comm 练习扩展 WsfComm 类

![](images/ee1205cc57438dbc43a93082e20ed6b5c63fa4d7e9c3c648233c7bca08d82ffa.jpg)

- 在AFSIM中添加一个新的SignalComm类。

![](images/b19f388558b5df3327ff1ccf99f73ae861669e633d8e9ad8aff913019b4ae1f6.jpg)

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19.

Other requests for this document shall be referred to AFRL/RQQD.

![](images/25bfb4bde241074af07b9f21bfab0d3f8fecd38b1559e54390f7b7bff53c7f41.jpg)

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

9

![](images/d5d43de00506bc662d7bbddef59e9cb39142e4822acc0817ca8feffe62383bc6.jpg)

# AFSIM中通信类(Comm)详情

![](images/54a0c36d1acb4e6e4e551f602a7c5756a564f712941aca96f5b4024b4c9237c6.jpg)

![](images/4f7dcdd35287fd494db27d3d2b58f0422fb11563abc31252b2fde2d98afc0896.jpg)

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQQD.

在 AFSIM 中添加一个新的

LocationMessage 类。

![](images/772fd343dd25f98d25eee9f97d86a0ecfff6f8a97589dc56210a9cc1d64bf04e.jpg)

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

# UNCLASSIFIED

![](images/347686863971ed55f773d4c21c8277211000d8db5a19dc2f44a27c4c5bf9dc87.jpg)

# AFSIM插件&扩展

![](images/4dfc504fff064a1c7674c237719749461ee92ce5917b962fd3b2ec29baf159ef.jpg)

![](images/539a0b7529055cc942229772360ee18805b2a134c0ae7b724912d15c16da5d1b.jpg)

- AFSIM 扩展必须继承自 WsfExtension:

- WsfScenarioExtension - 提供新场景命令的扩展（需要为这些命令实现新的ProcessInput方法）需要继承此类。  
- WsfSimulationExtension - 访问仿真的扩展需要继承此类。  
- WsfApplicationExtension - 创建新脚本类型或利用仿真扩展或场景扩展的扩展需要继承此类。

- 代码修改需要接受:

- 关键字 source_track_number_offset 及其输入值。

- 将使用现有的AFSIM方法来设置其他通信输入值。

示例输入：：

```txt
comm comm-net SIGNALCOMM source_track_number 100 end_comm 
```

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

UNCLASSIFIED

![](images/7c7319a626a68f7d03940c680a3b6d17593cfbfa8f764c8914d6891f9ca3de7f.jpg)

# Comm想定

![](images/80c09fb800096f8d0f2ef19c00afb8b4ce6829d03da3da7a4339d292779b61d1.jpg)

- 检查 comm_types.txt 文件并观察以下内容：

名为COMMPLATFORM的平台类型携带SIGNALCOMM(BLUECOMM)通信设备。

COMMPLATFORM SIGNALCOMM BLUECOMM

```txt
comm BLUECOMM SIGNALCOMM debug end_comm 
```

```txt
platform_type COMMPLATFORM WSFPLATFORM 
```

```txt
comm comm-net BLUECOMM internal_link msg Processor end_comm 
```

```txt
processor msg Processor WSFScriptPTPROCESSOR   
endprocessor   
mplatform_type 
```

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

- 检查 commscenario1.txt 文件并观察以下内容：

- blue-commander 平台每 5 秒向所有下属发送一次 WsfControlMessage。

# File: commscenario1.txt

```txt
platform blue-commander CMDR
    side blue
    commander SELF
    position 39:39:12n 123:08:00w altitude 0 ft agl 
```

```txt
execute at_interval_of 5 s WsfControlMessage cntrlMsg = WsfControlMessage(); cntrlMsg.SetFunction("I COMMAND YOU"); PLATFORM.Comm("comm-net").SendMessageToSubordinates("", cntrlMsg); end_execute 
```

```txt
endplatform 
```

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

# UNCLASSIFIED

# Comm想定

![](images/8687db0348d2b65d900259c74db4f2550157707a23ad2e66ee223714e56551a9.jpg)

![](images/7235b8cfeb2c4a8008943da9e7b5fba682f481bf7df73f1161e98144608b0173.jpg)

- 检查 commscenario1.txt 文件并观察以下内容：

- blue-commander 平台有一个 on_message 块，当从其下属接收到 LOCATION_MESSAGE 时，会写入一条消息。

# File: commscenario1.txt

```txt
platform blue-commander CMDR
side blue
commander SELF
position 39:39:12n 123:08:00
execute at_interval_of 5s
WsfControlMessage cntrlMsg
cntrlMsg.SetFunction("I COMM")
PLATFORM.Comm("comm-net").S
end_execute
end-platform
end-platform
on_message type LOCATION_MESSAGE
script
ProcessMessage((LocationMessage)MESSAGE);
end_script
end_on_message 
```

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19.

Other requests for this document shall be referred to AFRL/RQQD.

- 检查 commscenario1.txt 文件并观察以下内容：

- blue-1、blue-2 和 blue-3 平台每 5 秒向指挥官发送一次 LocationMessage。

File: commscenario1.txt   
```txt
platform blue-1 AIRCRAFT
    side blue
    commander blue-commander
    route
    end-platform
    platform blue-2 AIRCRAFT
    side blue
    commander blue-commander
    route
    end-platform
    platform blue-3 AIRCRAFT
    side blue
    position 38:28:47.764n 122:50:13.166w altit
    end-platform 
```

```txt
DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQDD. 
```

17

![](images/3f63314a0bd50c6ae0ef59271fb14ce7becd049c71247254234348b1bd3f10b0.jpg)

UNCLASSIFIED

# Comm想定

![](images/edd397fa5ea9872969fc110e7f2cc51ee915d7a96f72fadc0747bb9b4929c88c.jpg)

- 检查 commscenario1.txt 文件并观察以下内容：

- 这些平台有一个on_message块，用于响应WsfControlMessage。

File: commscenario1.txt   
```txt
platform blue-1 AIRCRAFT
side blue
commander blue-commander
route
end-platform
platform blue-2 AIRCRAFT
side blue
commander blue-commander
route
end-platform
platform blue-3 AIRCRAFT
side blue
position 38:28:47.764n 122:50:13.166w al
end-platform 
```

- “我命令你”控制消息  
- 每5秒发送一次。  
- 仅发送给下属。

- 平台包括指挥官 blue-commander（blue-1 和 blue-2）。

- “OK”控制消息会立即发送回指挥官。

![](images/083d6ae7da8011fced0f4c24166a65ba9b079b910671d6fd8fde661e4fb1827d.jpg)

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

UNCLASSIFIED

![](images/9739396e6a0c0d2e6b3c4e2e500634dc946c2c0115b61b5197afa44394aac890.jpg)

# Comm想定

![](images/ebd1c5ed0eb9e5f50b81c98d6a6299097cd8c85c1406005d12a6c7b65b644352.jpg)

- 检查 commscenario2.txt 文件：

- 平台ISR-1接收来自commscenario1中平台的SIGNALCOMM消息，并使用WsfDraw在Mystic中将这些位置显示为图标。

- 尽管我们在AFSIM仿真中演示了这一点，但其他仿真也可以接收、解码并显示这些位置。

# File: commscenario2.txt

```txt
platform isr-1 COMM PLATFORM
add processor internal_generation msg Processor
update_interval 5.0 seconds
internal_link msg Processor
on_update
// Send location
LocationMessage msg = LocationMessage();
SendMessage(msg);
end_on_update
end处理器 
```

- 检查 commscenario2.txt 文件：

-ISR-1还演示了通过内部链接发送位置消息，以便使用WsfDraw显示这些位置。

File: comm scenario2.txt   
edit processor msg Processor on_message type LOCATION_MESSAGE script LocationMessage msg $=$ (LocationMessage)MESSAGE; WsfDraw draw $=$ WsFDraw(); draw.Erase(msg.SourceTrackNumber()); draw.SetId(msg.SourceTrackNumber()); draw.SetDuration(20.0); : draw.End(); end.script end_on_message end Processor

：

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

# UNCLASSIFIED

# Messages 产生

21

![](images/2c8a8c77abfa4b8a54e0c0cbc84ce762fb8de01f59c5dd24760e5e8f267484af.jpg)

![](images/bd59e32fafd5bf1bfb1994f55b8ec0faa21621c71b27530ed3355c9621d0755e.jpg)

- 每5秒发送一次。

- 仅发送给平台的指挥官。  
- blue-1 发送给 blue-commander。  
- blue-2 发送给 blue-commander。  
- blue-3 发送消息，但没有接收者（没有指挥官）。  
- ISR-1 发送消息，但没有接收者（没有指挥官）。

- ISR-1 扫描通信网络以获取所有位置消息。

对于每个接收到的位置消息，它在该位置绘制平台。

![](images/f88b91c7639357ae0b82a342bf56ef55d11e1aa32b7f60ed63fe4514a365b029.jpg)

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19.

Other requests for this document shall be referred to AFRL/RQQD.

![](images/d8e304f94247de4769644b26442d6d2d640060138abc4934bc7e60490890432e.jpg)

![](images/7baffe0851ca8a1ca8b5346fcb5f953db410e704484241c6da4c6398f44f6333.jpg)

T=0

Queued message for transmission. T = 2.96422

Comm: blue-commander.comm-net

Message: 35 (dest 0.1.0.2; size 0)

Scheduled transmission event.

T=2.96422

Comm: blue-commander.comm-net

Message: 35 (dest 0.1.0.2; size 0)

Queued message for transmission.

T=2.96422

Comm: blue-commander.comm-net

Message: 35 (dest 0.1.0.3; size 0)

Scheduled transmission event.

T=2.96422

Comm: blue-commander.comm-net

Message: 35 (dest 0.1.0.3; size 0)

Comm has started transmission of message.

T=2.96422

Comm: blue-commander.comm-net

Message: 35 (dest 0.1.0.2; size 0)

Message transmission completed.

T=2.96422

Comm: blue-commander.comm-net

Message: 35 (dest 0.1.0.2; size 0)

Comm has started transmission of message.

T=2.96422

Comm: blue-commander.comm-net

Message: 35 (dest 0.1.0.3; size 0)

Message transmission completed.

T=2.96422

Comm: blue-commander.comm-net

Message: 35 (dest 0.1.0.3; size 0)

Comm receiving message.

T=2.96464

Comm: blue-1.comm-net

Message: 35 (dest 0.1.0.2; size 0)

23

![](images/0b3cc33ba7522c7635b7195eb1985ea97567ad5e8aa65f2cb8f68005f886d66e.jpg)

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

# UNCLASSIFIED

# 开始(1/3)

![](images/185eed511193897574b9a3323ea9c192ec1f00ebe6830d5228c39fd80d2240a2.jpg)

- 打开 CMake GUI:  
- 检查BUILD_WITH_comm exercis   
- 点击“Configure”。

- （如果出现提示，请选择编译器）。

- 点击“Generate”。

- 如果 Visual Studio 已经打开：

- 导航到它并在提示时选择Reload All。

![](images/b8b73a5eb2544f7ad435c790ed8f7b5ad95e32a175463ccff83e84c190af952e.jpg)

- 或者，通过以下方式打开解决方案文件afsim.sln:

- 从 swdev\build 打开。  
- 从 CMake 中点击“Open Project”

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

# UNCLASSIFIED

# 开始 (3/3)

25

![](images/243819787dffc83c84b5f06d5c507a000499e60826147b1534a07695a5702e1d.jpg)

![](images/05c687e11bc2412e5baf0e35830bb0a1fd36e494e8987e945ff517ef52dbb97a.jpg)

- 工程包含以下文件:

CommPluginRegistration.cpp   
- DataLinkMessage.hpp   
- DataLinkMessage.cpp   
- DataLinkLocationMessage.hpp   
- DataLinkLocationMessage.cpp   
- Interface.hpp   
- Interface.cpp   
- LocationMessage.hpp   
- LocationMessage.cpp   
- SignalComm.hpp   
- SignalComm.cpp   
- SignalCommRegistration.hpp

![](images/c8a3f2f16100784069ae2f7f2e8fdc3ca373ef4b86bcd9dd3b14c624e0019eba.jpg)

Note that many solutions are possible; we have provided a solution in order to complete our training exercise in a short time period.

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQQD.

- 本练习使用以下类：

-class DataLink::Message

定义了一个“链路层”消息头。  
位于命名空间 DataLink 中。

-class DataLink::LocationMessage : public DataLink::Message

- 定义了一个“链路层”消息，用于编码 LocationMessage 的元素（见下文）。  
- 继承的 DataLink::Message 将头部纳入消息中。  
位于命名空间 DataLink 中。

-class WsfControlMessage : public WsfMessage

被我们的场景脚本使用。  
- 允许指挥官（有下属的）发送“我控制你”消息。  
- 已在核心脚本接口中定义。

-class WsfStatusMessage : public WsfMessage

被我们的场景脚本使用。  
- 允许下属（有指挥官的平台）以“OK”消息进行响应。  
- 已在核心脚本接口中定义。

-class LocationMessage:public WsfMessage

- 创建一种新的高级消息类型，用于编码平台的位置数据。

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

# UNCLASSIFIED

# 本练习所使用的类

![](images/677d2ba1ddd581c1895abb6e9a96e491afcaddea8e2663e519f9b6df606f9154.jpg)

27

![](images/f7194282c9727667ac91cc4ab4e76249e7408e984dc3efda82cc7743bbc1ef8a.jpg)

- 本练习使用以下类：

-class ScriptLocationMessageClass:public WsfScriptMessageClass   
- 声明并定义了新的脚本方法，这些方法将可用于场景定义，以发送和接收新的 LocationMessage。

class SignalComm : public wsf::comm::Comm

定义了一个通信设备，用于触发发送/接收编码消息的DIS信号PDU。

-class CommLab::Interface : public WsfSimulationExtension

主要作为DIS通信协议的接口，用于发送和接收消息。  
位于命名空间CommLab中。

class SignalCommRegistration : public WsfScenarioExtension

定义了三个方法：

- AddedToScenario：将新的SignalComm通信类型添加到场景中。将新的ScriptLocationMessageClass添加到应用程序的脚本类型中。  
- ProcessInput: 简单地调用 CommLab::Interface::ProcessInput 来处理场景命令。  
- SimulationCreated: 将 CommLab::Interface 仿真扩展注册到仿真中。

-class WsfDefaultApplicationExtension : public WsfApplicationExtension

- 一个简单的应用程序扩展，具有 ScenarioCreated 方法。  
以场景扩展为模板。  
- 当 ScenarioCreated 被调用时，它将场景扩展注册到场景中。

- 练习 1

- 完成默认应用程序扩展的注册，并与场景扩展结合。

·练习2

- 完成场景扩展的ProcessInput和Interface::ProcessInput。

·练习3

- 理解并完成处理发送、接收和处理消息的类方法的实现。

·练习4

- 理解并完成新的脚本方法的代码。

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

# UNCLASSIFIED

# 练习1

![](images/3f30f559fd2ab4f6ff9d761dc8252a7ccfacee9a9e08ac6a754b1a02f41cff05.jpg)

29

![](images/f9a706833f74b3d40888ad10d007b1cbad97514ce7e975decc02028b4be72734.jpg)

- 完成默认应用程序扩展的注册，该扩展以场景扩展为模板。

![](images/cdc6002de182942791a9385d31dc74538676ba45a6469b70cb189326c3a27751.jpg)

- 所有AFSIM扩展必须继承自WsfExtension:

- 已经存在三个预定义的扩展类（可以继承）：

- WsfScenarioExtension - 提供新场景命令的扩展（需要为这些命令实现新的ProcessInput）需要继承此类。  
- WsfSimulationExtension - 访问仿真的扩展需要继承此类。  
- WsfApplicationExtension - 创建新脚本类型或利用仿真扩展或场景扩展的扩展需要继承此类。

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

31

![](images/6875794a0bace0dc13a72203a2f8ce946a9465c48a5457dc434545faeecf0f55.jpg)

# AFSIM插件&扩展

![](images/c4e9394cc3ce9f12baf0c246843371bda348b378ea84c23bab4f4cfacd78b4ed.jpg)

![](images/a75dc40ded97b0da943d6f62d56dcb3e6f7419e11d4295f690421fc563953a81.jpg)

- 所有 AFSIM 扩展都必须继承自 WsfExtension:

- 已经存在三个预定义的扩展类（可以继承）：

- WsfScenarioExtension 提供新场景命令的扩展（需要为这些命令实现新的 ProcessInput）需要继承此类。  
- WsfSimulationExtension 访问仿真的扩展需要继承此类。  
- WsfApplicationExtension 创建新脚本类型，或使用仿真扩展或场景扩展的扩展需要继承此类。

- 应用程序、场景和仿真都可以被“扩展”。

- 应用程序扩展由应用程序拥有。

- 代表可以添加到应用程序的可选功能。  
- 如果需要新的脚本类型（传感器、武器、组件、移动器），则使用此功能。  
- 这是在AFSIM中注册所有扩展的入口点。  
- 如果要创建场景扩展或仿真扩展，则需要应用程序扩展。

- 我们需要一个新的插件，因为我们需要注册默认的应用程序扩展。

- 请参见文件 CommPluginRegistration.cpp。

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

33

![](images/27a1dc81080b957ff6e887248ecee9a9737e59c20f21826d32244b5f121d1586.jpg)

# Comm 练习1—检视1

# CommPluginRegistration.cpp

![](images/c291a694b097bb9bc4e7c5702650b05bbe288e45e571ae30f9c7e69084e7da3a.jpg)

- 在CommPluginRegistration.cpp中, 检视 WsfPluginVersion

extern "C"   
COMM_EXERCISE exporting void WsfPluginVersion(UtPluginVersion& aVersion) { aVersion $=$ UtPluginVersion(WSF Plugin_APIMajor_VERSION, WSF Plugin_APIMinor_VERSION, WSF Plugin_API_COMPILER_STRING); }

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQDD.

- 完成 WsfPluginSetup:

- 调用 aApplication.RegisterExtension。  
- 第一个参数应为应用程序扩展的名称，即“signal_commregistration”。  
- 第二个参数应为一个新创建的 unique_ptr，指向以我们的场景扩展 SignalCommRegistration 为模板的 WsfDefaultApplicationExtension。

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

35

![](images/2a95445cf1ba3e85285360d153e407b2524e507cfa32a0f542f319cdaded0bb3.jpg)

# Comm 练习1—任务1 解决方案

# CommPluginRegistration.cpp

![](images/3f7807559c705f13b13542eed1de178839df466f917446672c9c7f78bb506e60.jpg)

extern "C"   
{ COMM_EXERCISE exporting void WsfPluginVersion(UtPluginVersion& aVersion) { aVersion $=$ UtPluginVersion(WSF Plugin_APIMajor_VERSION, WSF Plugin_APIMinor_VERSION, WSF Plugin_API_COMPILER_STRING); } COMM_EXERCISE exporting void WsfPluginSetup(WsfApplication& aApplication) { // EXERCISE 1 TASK 1 //Invoke aApplication's RegiserExtension method // The first argument is the name of the application extension //The second argument is a newly created unique_ptr to a default application extension //that is templated upon a scenario extension (the SignalCommRegistration class) aApplication.RegisterExtension("signal_commregistration", ut::make_unique<WsfDefaultApplicationExtension<SignalCommRegistration>>();   
}

注意：当我们注册应用程序扩展 WsfDefaultApplicationExtension 时，我们也在注册 SignalCommRegistration 场景扩展。

- 要扩展应用程序，您必须创建一个继承自 WsfApplicationExtension 的类

# class myAppExtension: public WsfApplicationExtension { ... }

- 您应该重写以下成员：

- AddedToApplication: 接收扩展被添加到应用程序的通知，通常用于注册额外的脚本类和方法等.  
- ScenarioCreated: 在场景构造函数结束时调用，以接收来自应用程序的场景创建通知，如果需要，可以用于注册场景扩展  
- SimulationCreated: 在仿真的初始化方法中调用，以接收来自应用程序的仿真创建通知，如果需要，可以用于注册仿真扩展  
- ProcessCommandLine: 从 WsfApplication::ProcessCommandLine 方法调用，以检查当前参数并在必要时处理它  
- PrintGrammar: 打印扩展识别的扩展语法  
- ProcessCommandLineCommands: 由 WsfApplication 的 ProcessCommandLineCommands 调用，以允许扩展处理/处理其需要识别的任何命令

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

UNCLASSIFIED

![](images/70141df54638c1cc4711c9ff42e5f99485acf3e34c853ba12a7be70ea544a485.jpg)

# Application Extensions

![](images/8124d23113462513610413026d8c274906f8ecdd18a22446864ed77d84a02545.jpg)

- 要扩展一个 Application，必须创建一个继承自 WsfApplicationExtension 的类。
- 我们将使用 WsfDefaultApplicationExtension，它会注册场景扩展：

class WsfDefaultApplicationExtension: public WsfApplicationExtension { }

- 此类为 ApplicationExtension 重写了以下成员：  
- ScenarioCreated 在场景构造函数结束时调用，用于接收应用程序通知场景已创建的消息。  
- 如果需要，可以在此处注册场景扩展。  
- 此类是基于 ScenarioExtension 的模板类，因此在实例化时，必须为模板提供一个从 ScenarioExtension 派生的类。  
- 当 WsfDefaultApplicationExtension::ScenarioCreated 方法由 WsfScenario 构造函数执行时，它会将 SignalCommRegistration 场景扩展注册到场景中。

- 场景也可以被“扩展”。

- 场景扩展由场景拥有。

- 代表可以添加到场景的可选类型。  
- 如果需要新的类型（组件、观察者、通信），则使用此功能。

- 如果要创建场景扩展（或仿真扩展——稍后讨论），则需要应用程序扩展。

- 如果我们正在创建仿真级命令，我们也需要场景扩展。

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

UNCLASSIFIED

![](images/739f08b1eb27da473a96c0cf2311651786dcc3d2e45fdaf60218017bb8b1e3f2.jpg)

# 想定扩展

![](images/388e143dd1965f7e1921c7f579a866ae7d6ae849f72a969eb332f29d56639f03.jpg)

- 要扩展一个场景（Scenario），必须创建一个继承自 WsfScenarioExtension 的类：

class myScenarioExtension: public WsfScenarioExtension

- 可以重写以下方法:

- AddedToScenario: 用于接收扩展被添加到场景的通知。  
- 通常用于注册额外的组件类型对象和工厂。  
- ProcessInput: 处理扩展必须识别的任何场景输入命令  
- FileLoaded: 通知扩展文件已加载到场景中  
- Complete: 从 WsfScenario::LoadComplete 调用，通知扩展所有场景输入已处理完成  
- Complete2: 在所有扩展的 Complete 方法被调用后调用  
- SimulationCreated: 从 WsfSimulation::Initialize 调用。如果场景扩展需要关联的仿真扩展，此方法可以注册仿真扩展。  
AlwaysCreate: 确定扩展是可选的还是必需的

- 要扩展一个场景，您必须创建一个继承自 WsfScenarioExtension 类的类

# class SignalCommRegistration: public WsfScenarioExtension

- 我们将重写以下方法:

- AddedToScenario: 接收扩展被添加到场景的通知——通常用于注册额外的组件类型对象和工厂  
- SimulationCreated: 从 WsfSimulation::Initialize 调用——如果场景扩展需要一个关联的仿真扩展，这个方法可以注册该仿真扩展  
- ProcessInput: 处理必须被扩展识别的任何场景输入命令

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

UNCLASSIFIED

# Comm 练习1—检视2

41

![](images/633bb7e94d36e7362a7f34a58e7a54990900781a6fab7a3e65e99d542c32cb60.jpg)

![](images/1a5fae1a9ebaa8946a9dadba3e95274b72a5372b8d80c922711c64c7d83c8f6c.jpg)

- 查看 SignalCommRegistration::AddedToScenario 的定义。

- 请注意，AddedToScenario 是由

WsfScenarioExtension::RegisterExtension 执行的，用于通知扩展现在可以进行需要场景存在的操作，例如注册新类型等。

- AddedToScenario 执行以下操作：

- 将新的 SignalComm 通信类型注册到场景中。  
- 将新的脚本类型 ScriptLocationMessageClass 注册到场景中。

```txt
class SignalCommRegistration : public WsfScenarioExtension { public: 
```

```cpp
void AddedToScenario() override
{
    // Add the new comm type.
    auto signalCommPtr = ut::make_unique<wsf::comm::SignalComm>(GetScenario());
    GetScenario().GetCommTypes().Add(wsf::comm::SignalComm::GetSignalCommClassId(), std::move(signalCommPtr));
    // Add the script classes to the script manager
    GetScenario().GetApplication().GetScriptTypes()->Register(ut::make_unique<ScriptLocationMessageClass>
("LocationMessage", GetScenario().GetApplication().GetScriptTypes));
} 
```

```txt
1 
```

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

UNCLASSIFIED

![](images/6c56194d750367eb766e2a29a64e4765445ffb924f5818ae5698dceaf324a65c.jpg)

# Comm 练习1—检视3

43

![](images/17ef1f72875dedf885d6451688b60f6bcb1810456a7e82b3016d0a9b169d6e3d.jpg)

- 请注意，成员变量 mPrototypicalInterface 是一个 CommLab::Interface 仿真扩展对象。

- mPrototypical 是一个原型仿真扩展，在场景读取输入文件时使用。

- 在场景调用 ProcessInput 时，该对象存在，而在 SimulationCreated 中创建的新仿真扩展的 unique_ptr 尚不存在。

- 当仿真被创建时，会创建一个指向新实例化的

CommLab::Interface 的唯一指针，并将 mPrototypeInterface 的成员复制到该指针中。

class SignalCommRegistration : public WsfScenarioExtension { public:

···

void SimulationCreated(WsfSimulation& aSim) override

// create a new CommLab::Interface simulation extension

auto InterfacePtr = ut::make_unique<CommLab::Interface>();

// use the prototype to initialize member variables in the new Interface

// have to copy members, since ProcessInput was already called on mPrototypeInterface

// only have to copy two members, since the others are not yet changed from default

InterfacePtr->SetDebugEnabled(mPrototypeInterface.GetDebugEnabled());

InterfacePtr->SetPrintMessages(mPrototypeInterface.GetPrintMessages());

// register the new extension

aSim.RegisterExtension("comm_lab-interface", std::move(InterfacePtr));

1

private:

CommLab::Interface mPrototypeInterface;

}；

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19.

Other requests for this document shall be referred to AFRL/RQQD.

# UNCLASSIFIED

# 扩展

- 仿真也可以被“扩展”。

仿真扩展由仿真拥有。  
- 允许访问仿真功能。  
- 如果需要访问仿真本身（观察者、通信、XIO），则使用此功能。  
- 如果要创建仿真扩展（您可能还需要场景扩展），则需要应用程序扩展。  
- 如果我们需要知道平台何时被添加或删除，以及传感器跟踪何时被初始化或更新，我们需要一个仿真扩展。

- 要扩展一个仿真（Simulation），必须创建一个继承自

WsfSimulationExtension 的类

# class mySimulationExtension: public WsfSimulationExtension

- 必须重写以下方法:

- AddedToSimulation: 从 WsfSimulation::RegisterExtension 调用  
- Initialize: 从 WsfSimulation::Initialize 调用，用于执行扩展的初始化操作  
- PrepareExtension: 从 WsfSimulation::Initialize 调用（当仿真被初始化时调用）。也会从 WsfSimulation::PrepareSimulation 调用（当仿真被重新加载时调用）。  
- PendingStart: 仿真刚刚进入待启动状态时调用，允许扩展添加额外的平台或其他实体。  
- Start: 从 WsfSimulation::Start 调用，这是另一个机会可以添加额外的平台或其他实体  
- Complete: 从 WsfSimulation::Complete 调用，允许扩展释放由 Initialize 或 PrepareExtension 分配的资源（如文件、套接字等）

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

UNCLASSIFIED

![](images/c0bd4fe02c25e4ebdf3f5e0d2b48f9cc38041775606886202d52ef21b683abf4.jpg)

# 仿真扩展

![](images/6cdbe9785f450d58db5c1f87465733f392febb56682bb47930763cdc0e09de5f.jpg)

47

- 要扩展一个仿真，您必须创建一个继承自 WsfSimulationExtension 类的类：

class Interface: public WsfSimulationExtension

- 您必须重写以下方法：

- Initialize: 从 WsfSimulation::Initialize 调用——用于执行扩展初始化  
- Start: 从 WsfSimulation::Initialize 调用——用于通知扩展仿真即将开始

![](images/23bc652a4a998866948c26cb81675c6c8badaceb92ee6fd14a783b0153f6a612.jpg)

# UNCLASSIFIED

# AFSIM插件与扩展

# AFSIM 任务启动序列

![](images/4ad2c6a1cdaa46313615624186fdc9f953e64b62cb46878775c8181c4bafd7eb.jpg)

注意：SignalCommRegistration包含一个成员变量mPrototypicalInterface，它是一个Comm::Interface。

![](images/6c38489d9780f48e73f23f4b72c5c13f0b18ba893cb15f8428a9cd0e10b77e74.jpg)

- WsfStandardApplication 构造函数利用插件管理器查找并加载所有插件（包括训练文件夹中的插件——因为使用了 cmake 选项 WSF_ADD Extensions_PATH）。

- 对于找到的每个插件，执行 WsfPluginSetup（注意：这会导致我们的通信练习插件的 WsfPluginSetup 函数被执行）。  
- 这导致我们的通信练习的 WsfDefaultApplicationExtension 被创建并注册到 app 中。  
- RegisterExtension 然后调用 WsfApplicationExtension::AddedToApplication().

- 注意：WsfDefaultApplicationExtension并没有重写 AddedToApplication，因此这个通知实际上被忽略了。

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

49

![](images/a27284139795c25944cbac7c2b1ca406e5d03ab6e6bafc4b5ee5f8a2df3b9d0a.jpg)

# UNCLASSIFIED AFSIM插件与扩展

# AFSIM 任务启动序列

![](images/8a3542cb81ebecec7173126382946019d1bb0987b204b239c27e31ec0b2ab5df.jpg)

![](images/14e65b955309a86d0c472ba3ce6e92ef904db17c5e64bb46e424cacc3aa17038.jpg)

任务随后将所有必要的预定义扩展注册到 app 中。

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19.

Other requests for this document shall be referred to AFRL/RQQD.

![](images/e2a9b2d5ac9eb089b85b9f1fed2b065fad6c0a8ad2bfc857903c4e5b7895276b.jpg)

Mission 随后创建场景并调用 WsfScenario 构造函数: WsfScenario

scenario(app);

- 该构造函数调用 WsfApplication::ScenarioCreated 方法。  
- 这又会调用所有注册的应用程序扩展的 ScenarioCreated（包括  
WsfDefaultApplicationExtension::ScenarioCreated）。  
- 这进一步创建了 SignalCommRegistration，并将其注册到 scenario 中。  
- RegisterExtension 然后调用 SignalCommRegistration::AddedToScenario。  
- SignalCommRegistration::AddedToScenario 将 ScriptLocationMessageClass 类注册到脚本类型管理器中。

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19.

Other requests for this document shall be referred to AFRL/RQQD.

51

![](images/7c06f1d131b47255b4973223de55c8a0f7293bb32273354e73e93e11295dd5db.jpg)

# AFSIM插件与扩展

# AFSIM 任务启动序列

![](images/639a7c9a77755d1dfacd565792e8a950cd1ba5ed6135125349e5b082e0d13628.jpg)

![](images/e50c5a52363d05a50e35a122d63ba011f0d98fcbd97e8a6f052e1d1fa89c1400.jpg)

# Mission调用app.WsfStandardApplication::ProcessInputFiles()

- 任务调用 app.WsfStandardApplication::ProcessInputFiles(), 这会调用 WsfScenario::LoadFromFile().

- 对于输入中的每个命令：

- 调用每个核心类的ProcessInput()方法  
- 调用每个注册的场景扩展的ProcessInput()

调用SignalCommRegistration::ProcessInput()   
调用CommLab::Interface::ProcessInput()

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19.

Other requests for this document shall be referred to AFRL/RQQD.

![](images/33abd6d618c19d49f597cd5958ea7425e08d2dec504980416ca49f27a0acaf34.jpg)

任务调用app.WsfStandardApplication::ProcessInputFiles()，这会调用WsfScenario::LoadFromFile()，然后调用WsfScenario::CompleteLoad()。

- 调用每个场景扩展的 Complete() 方法。  
- 然后调用每个场景扩展的 Complete2() 方法。

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

53

![](images/1e2f71b01549dbc27e8ded47c3c559e448fb267f3d68161494b0cc0772ba33e7.jpg)

# UNCLASSIFIED AFSIM插件与扩展 AFSIM任务启动序列

![](images/a536863acecd7094ed25c180ed64f672dd1f980189a82efce0b5b78a4d111963.jpg)

![](images/d142236a07bbf7125f586d98b03c761c3dc41ad4810e0a2f0099f7f87675cb92.jpg)

Mission通过执行以下代码创建仿真:

std::unique_ptr<WsfSimulation> simPtr =

app.CreateSimulation(scenario, ...);

- CreateSimulation 调用 WsfSimulation 对象的构造函数（以 scenario 作为参数）

![](images/5d7b291047af10a556899c7288c8f42984042548d290dde64395d93ca7dc975d.jpg)

Mission通过执行以下代码创建仿真：

app.InitializeSimulation(simPtr.get())

- InitializeSimulation 调用: aSimPtr->Initialize()

(where aSimPtr $\equiv$ simPtr.get())

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

55

![](images/8275314217fd43324d80fafdfbba95aad4fbfeaf8581aa6705f9a2eba8a50c03.jpg)

# UNCLASSIFIED AFSIM插件与扩展

# AFSIM 任务启动序列

![](images/22d29b3cbbcba91120b450421f49b3fc611e59e99a5fcf8d4b10fb3920627811.jpg)

![](images/4941979c1a53a561a698a4fa738cba1650a807448737ebe63d9de17652a86738.jpg)

Mission通过执行以下代码创建仿真:

app.InitializeSimulation(simPtr.get())

- InitializeSimulation 调用: aSimPtr->Initialize()   
- WsfSimulation::Initialize 调用: mScenario.SimulationCreated(*this)

(where mScenario $\equiv$ scenario and \*this $\equiv$ *simPtr.get()

![](images/c5a18b9f1634d3d80e1d3d267b2c11ed55300c4910f86e018208cd8cfff30b8e.jpg)

Mission 通过执行以下代码创建仿真：

app.InitializeSimulation(simPtr.get())

- InitializeSimulation 调用: aSimPtr->Initialize()   
- WsfSimulation::Initialize 调用: mScenario.SimulationCreated(*this)   
- SimulationCreated 调用: GetApplication().SimulationCreated(aSimulation)

(where GetApplication() ≡ app and aSimulation ≡ *simPtr.get())

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19.

Other requests for this document shall be referred to AFRL/RQQD.

57

![](images/5b4eef4f12dc1ecb2a02d18345d24a3c0e1ceb76758c496b0b1c4fc2a89b73d2.jpg)

# AFSIM插件与扩展

# AFSIM 任务启动序列

![](images/1fac2825cb2778a08c80e0b95b3e1079f33d79e7882f664e015ee49c6bba5836.jpg)

![](images/376d948f701a16e63e9bb1a270df6a013a34c660f23ece1642814defc8cd5270.jpg)

Mission通过执行以下代码创建仿真:

app.InitializeSimulation(simPtr.get())

- InitializeSimulation 调用: aSimPtr->Initialize()   
- WsfSimulation::Initialize 调用: mScenario.SimulationCreated(*this)   
- SimulationCreated 调用: GetApplication().SimulationCreated(aSimulation)

- 对于每个应用扩展调用：SimulationCreated(aSimulation)

(where aSimulation $\equiv^{*}\mathrm{simPtr.get()}$

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19.

Other requests for this document shall be referred to AFRL/RQQD.

![](images/12a5f8a527650589882294de0ba206ce78fca83adcd0f0df922f191d0c8c7ec8.jpg)

Mission通过执行以下代码创建仿真:

app.InitializeSimulation(simPtr.get())

：

- SimulationCreated 调用: GetApplication().SimulationCreated(aSimulation)

- 对于每个应用扩展调用 SimulationCreated(aSimulation)  
- 这会调用 SignalCommRegistration::SimulationCreated(aSimulation)

(where aSimulation $\equiv^{*}\mathrm{simPtr.get()}$

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19.

Other requests for this document shall be referred to AFRL/RQQD.

59

![](images/a24c38ea2b1822dbd5a98e096c0b20d7760e827bc748281ac17c1b7f7c750ab3.jpg)

# UNCLASSIFIED AFSIM插件与扩展

# AFSIM 任务启动序列

![](images/c871614e4958390af66ecc4ef9288fc64a6095e7d00f056abaa6fb27579cc70e.jpg)

![](images/c94129bd1a4dee3e82ad47c5c29b78fd478c554d8872dabac415c83ae6b06d38.jpg)

Mission通过执行以下代码创建仿真：

app.InitializeSimulation(simPtr.get())

：

- SimulationCreated 调用: GetApplication().SimulationCreated(aSimulation)

- 对每个应用扩展调用 SimulationCreated(aSimulation)  
- 这会调用 SignalCommRegistration::SimulationCreated(aSimulation)  
接着调用aSimulation.RegisterExtension(ut::make_unqiue<CommLab::Interface>))

(where aSimulation $\equiv^{*}\mathrm{simPtr.get()}$