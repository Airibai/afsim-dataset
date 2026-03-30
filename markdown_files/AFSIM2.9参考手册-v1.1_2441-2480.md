![](images/4d0ede67a5229c0cde79779d3079e40ac2ab149759edf5c92e196353453963e8.jpg)  
DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

![](images/9fe426f981355f8293b2da948f175c0b02c49e1bc8f6485ba66314ca6635dc31.jpg)

# UNCLASSIFIED 练习2-任务1 TrainingPlugin.cpp

42

![](images/b2f5e79e9842d8e91039c8729158ab3c7a1c74424dca1027ec77d6a7ac5affec.jpg)

- 创建一个连接，将 WkfEnvironment 的

PlatformSelectionChanged() 信号与 Training::Plugin 的 SelectionChanged() 函数连接起来。

- 这样，每当所选平台集合发生变化时，都会调用 Plugin::SelectionChanged()。  
- 使用以下 connect 的重载版本:

QObject::connect()

const QObject *sender,

PointerToMemberFunction signal,

const QObject *receiver,

PointerToMemberFunction method,

Qt::ConnectionType type = Qt::AutoConnection)

Should be: &wkfEnv   
Should be: &wkf::En   
Should be: this

Should be: &Training::Plugin::SelectionChanged

Should be left as using the default value

Qt's Signal and Slot documentation https://doc qt.io/qt-5/signalsandslots.html

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19.

Other requests for this document shall be referred to AFRL/RQQD.

WKF PluginrogenDEFINE_SYMBOLS(Training::Plugin, "WKF Training", "Plugin created for AFSIM Developer Course.", "all")

```cpp
Training::Plugin::Plugin(const QString& aPluginName, const size_t aUniqueId) : wkf::Plugin(aPluginName, aUniqueId)   
{ // EXERCISE 1 TASK 2a // Get wkf::MainWindow pointer from WkfEnvironment wkf::MainWindow\* mainWindowPtr = wkfEnv.GetMainWindow(); // EXERCISE 1 TASK 2b // Add mDockWidget to the Main Window, // this will also add the action to toggle the visibility of the DockWidget to the View menu mainWindowPtr->addDockWidget(Qt::RightDockWidgetArea, new DockWidget()); //EXERCISE 2 TASK 1 // Add a connect statement that connects RangeRing::Plugin::SelectionChanged / to the wkf::Environment::PlatformSelectionChanged signal   
connect(&wkfEnv, &wkf::Environment::PlatformSelectionChanged, this, &Training::Plugin::SelectionChanged);   
} 
```

![](images/abe79a22470cc52e9fbd9b41fb633f07bdfa2a82140343edb897c8ac6c313b6f.jpg)

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

44

![](images/ee70f84d3e8c9a295744e0aa0f5d40bffdb890e4aa2c09a145e02f87d5619e6c.jpg)

# UNCLASSIFIED

# 练习2- 任务2

# TrainingPlugin.cpp

![](images/3bd8a1cdf0ee2a88dbf26ad46ce98b2d4ea7936564f5ffc23d50c8869b9163ba.jpg)

- 在 Plugin::SelectionChanged() 中：  
- 任务2a:

- 为每个选定的平台添加一个 Range Ring 附件（Range Ring attachment）。  
- 使用vespa::make_attachment<>()（已在VaUtilities.hpp中定义，且已包含）来创建附件。  
- 该模板应基于wkf::AttachmentRangeRing。

构造函数需要以下三个参数：

1. Parent（父对象）：这是平台（platform）。  
2. Viewer（查看器）：这是标准查看器（Standard Viewer），通过调用 vaEnv::GetStandardViewer 获取。  
3. Unique Name（唯一名称）：将附件命名为"range_ring"。

```cpp
void Training::Plugin::SelectionChanged(const wkf::PlatformList& aSelected, const wkf::PlatformList& aUnselected)   
{ for (auto platform : aSelected) { //EXERCISE 2 TASK 2a // First check to see if an attachment named "range_ring" is on the platform // If the attachment does not exist, create an attachment using vesp::make_embedding // The attachment constructor takes three arguments: // 1. Parent: which the the platform // 2. Viewer: which is the Standard Viewer // 3. Unique Name: name the attachment "range_ring" if (platform->FindAttachment("range_ring") == nullptr) { vespa::make_embedding<wkf::AttachmentRangeRing> (*platform, vaEnv.GetStandardViewer(), "range_ring"); } for (auto platform : aUnselected) { //EXERCISE 2 TASK 2b // Find the attachment on the platform with the name "range_ring" // Remove the attachment from the platform using the attachment's GetUniqueId() } } 
```

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

46

![](images/3fc7a10b23a9ec7746f65fa28770010ed55eb8a51de5244bce100465a46c3fbc.jpg)

UNCLASSIFIED练习-任务2 TrainingPlugin.cpp

![](images/046e46aa7f895f16449ffbd22b6cc02d6e363205d218395369231a4f773810e8.jpg)

# - 任务2b:

- 从每个不再被选中的平台中移除 Range Ring 附件（Range Ring attachment）。  
- 使用平台的 FindAttachment 方法查找名称为 "range_ring" 的附件。  
- 如果返回的值不是 nullptr（即找到了附件），则使用平台的 RemoveAttachment 方法将其从平台中移除。

```cpp
void Training::Plugin::SelectionChanged(const wkf::PlatformList& aSelected, const wkf::PlatformList& aUnselected)   
{ for (auto platform : aSelected) { //EXERCISE 2 TASK 2a // First check to see if an attachment named "range_ring" is on the platform // If the attachment does not exist, create an attachment using vesp::make_embedding // The attachment constructor takes three arguments: // 1. Parent: which the the platform // 2. Viewer: which is the Standard Viewer // 3. Unique Name: name the attachment "range_ring" if (platform->FindAttachment("range_ring") == nullptr) { vespa::make_embedding<wkf::AttachmentRangeRing> (*platform, vaEnv.GetStandardViewer(), "range_ring"); } for (auto platform : aUnselected) { //EXERCISE 2 TASK 2b // Find the attachment on the platform with the name "range_ring" // Remove the attachment from the platform using the attachment's GetUniqueId() auto ring = platform->FindAttachment("range_ring"); if (ring != nullptr) { platform->RemoveAttachment(ring->GetUniqueId()); } } 
```

```txt
DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQQD. 
```

48

![](images/c41011e7784a69e278227cda2e7d56eeb76e76f45b552446446967e9a9a12715.jpg)

# UNCLASSIFIED

# 练习

![](images/e220b27b94b95ecb87d8c6405570bd4fcf7dd1c478198b044ec823979e3bb91d.jpg)

- 从 Windows 的 Visual Studio:

- 在“Release”模式下构建解决方案。  
- 构建“INSTALL”项目。

从Linux：

- 在构建目录中执行以下命令：：

$ cmake --build . --target all -- -j12

$ cmake --build . --target install -- -j12

加载 WIZARD 中的测试场景：

路径：training\developer\wkf\abs\data\wkf_trainingscenario.txt

- 更改选定的平台：

- 通过地图显示（Map Display）或平台浏览器（Platform Browser）更改选定的平台。  
- 在平台浏览器中，可以使用Ctrl或Shift键选择多个平台。

![](images/aceeaf4c0bab6b80da77e28974d32a80a83cde723c2993293a9591b3c521f35e.jpg)

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

UNCLASSIFIED

![](images/e545c9655753d5755550419bda13b3ca08ccf88b6a1a3aea8efef03e18b17b6f.jpg)

50

![](images/9afc5a3f8a75e85c0dcaff39feb2db2a356734e8a4628eb6544b6c468bc1538f.jpg)

![](images/b7b3feff693e82207cad03f9ae48fc2039350685850970e042e150ddd5207ff2.jpg)

51

# 6.2.2.3. Warlock 开发 3_AFSIM_Dev_Trng_Warlock

本文为afsim2.9_src\training\developer\wkf\slides\3_AFSIMDev_Trng_Warlock.pptx的翻译，主要是介绍如何扩展Warlock，并做了些小例子。

![](images/b81ab46bd827a2abcfe8c86b1e22f1eac0199e649a80ed28de791048c54990a9.jpg)

Integrity $\star$ Service $\star$ Excellence

# AFSIM开发培训

# 3 - Warlock开发

本文档由杨石兴翻译，该资料做为《AFSIM2.9参考手册》的一部分。没有《AFSIM2.9参考手册》的加杨石兴微信领取：13324598743

# AFRL/RQQD 美国空军研究实验室

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

UNCLASSIFIED

![](images/009671e417096c35bb09480232ee68877c980513882d257e3ee1293a9601b11c.jpg)

# 术语和定义

![](images/6754cd35e923f8a1fa559a1df94da77191d0ff1946de2deca8af8099e5a3b55c.jpg)

AFSIM - Advanced Framework for Simulation, Integration, and Modeling

AGL – Above Ground Level

DIS - Distributed Interactive Simulation

DTED-Digital Terrain Elevation Data

EO/IR - electro-optical/infra-red

ESM - electronic support measure

FOV - field of view

GUI - graphical user interface

HLA-High Level Architecture

ID - identification

IEEE - Institute of Electrical & Electronics Engineers, Inc.

JTIDS - Joint Tactical Information Distribution System

MSL - Mean Sea Level

OS - Operating System

PC-Personal Computer

PDU - Protocol Data Unit

RCS-radar cross section

SAM - surface-to-air missile

SAR - synthetic aperture radar

VESPA - Visual Environment for Scenario Preparation and Analysis

WSF - World Simulation Framework

dB - decibels

dBsm - decibel square meters

deg-degrees

ft-feet

GHz-GigaHertz

kts-knots

m - meters

m^2 - square meters

mw-megawatts

nm - nautical miles

s - seconds

- 本实验重点是扩展 Warlock。  
- 您将编写一个插件，该插件将实现以下功能：

- 从模拟中获取数据。  
- 将数据显示给用户。  
- 允许用户更改所选平台的航向（heading）。

- 此外，您还将连接到首选项系统（Preference system），以实现以下功能：

- 为航向操作提供快捷键。  
- 为您的插件提供显示选项。

![](images/d814fb75cbcf0705ccc77ab513d7c7270392c6fe7c1784b85ae369d2856a4add.jpg)

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQQD.

# UNCLASSIFIED

![](images/9f26fdae677fe03d951b6b0f7cdb06ef1d29e288604da98c4be0899c4bef9454.jpg)

# 问题陈述

![](images/c368405bf8d70f34a3139c7851d415c4dbff2e7fc53c7d8a07f1489993c71836.jpg)

- 扩展 Warlock 应用程序以提供新功能：  
- 向用户显示当前 Warlock 中未显示的数据，并允许用户以当前未实现的方式控制模拟。

![](images/d06f4214851a8192f2f48287581bff6378089b7ab333de79a37692d20754ef0b.jpg)

References:   
- AFSIM Developers Web-based data.   
- AFSIM Source Codes and Visual Studio search functions.   
AFSIM Documentation.

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

- 您将获得以下方面的实践知识：

- 如何创建一个插件来扩展 Warlock。  
- 如何连接到模拟以检索数据。  
- 如何控制模拟。  
- 如何连接到首选项中的设置。

![](images/a59016bd15325ff8e02cf10fabb54fe6458413001e331e6124e15ebe12a58d1b.jpg)

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

UNCLASSIFIED

![](images/45e6b07b11d27a5aa41cd3cec9704d8c539ab8e13e6d97c2529aafbdd025128d.jpg)

# Warlock

![](images/f0ab245512e5b79448e82a6f82f6350527feedf7188d0d4e7b7adfb14dbaf4d9.jpg)

- Warlock 扩展了 WKF，以创建一个“操作员在环”

(Operator-In-The-Loop, OITL) 应用程序。代码位于 Warlock 目录中，包含以下子目录：

- Plugins: 存放 Warlock 特定插件的目录。

- 一些通用插件（例如地图显示插件）位于WKF/plugins目录中。

- Warlock_core: 为 Warlock 构建的库所在的目录。  
- Warlock_exec: 一个小型目录，包含主循环（main loop）。  
- Data: 一个存放非必要内容的目录，主要用于测试。  
- 您可以安全地忽略此目录，因为其中的内容不会用于构建或运行 Warlock。

- Warlock 可以加载多种类型的插件:

- Warlock 会从 wsfPlugins 或 missionPlugins 目录加载 AFSIM 插件。  
- 这使得在 Mission 中运行的场景也可以在 Warlock 中执行。

- Warlock 会从 wkfPlugins 目录加载插件，该目录包含所有三个应用程序（Warlock、Wizard 和 Mystic??）通用的插件。  
- Warlock 会从 warlockPlugins 目录加载插件，该目录仅包含专用于 Warlock 的插件。

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQQD.

UNCLASSIFIED

![](images/72b9807a0f1bb8e92aaa768b670945eeac93015b235f6d16041b12c9466d6026.jpg)

# warlock::Environment

![](images/41702f17dee0f94740adcb8c61ea2dfc530fa2d92724849015f1fd5834ecc58a.jpg)

- Warlock 添加了一个额外的环境类:

warlock::Environment（simEnv），用于访问处理模拟数据的对象。

- 插件可以使用 Warlock Environment 类来访问 PlatformManager 或 ScriptSimInterface。  
- 对 simEnv 的访问仅限于模拟线程（simulation thread）。  
- 在GUI线程上访问simEnv会导致异常。

Warlock中的三个环境类可以通过宏simEnv、wkfEnv和vaEnv访问。

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

- Warlock 有一个 Plugin 类, 它继承自 wkf::Plugin。

模板参数是插件将使用的SimInterface。  
- 添加了虚方法 GetPlotUpdater(), 用于支持在图表上绘制数据。

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQQD.

9

![](images/31629c2e840c3812a002f51b3b0e6014caadee3cc7b499e12b6b0ea73f9d1ca9.jpg)

# UNCLASSIFIED

# 绘图和更新器

![](images/9eab0bcaa575a58d8f007afa5e9c474fe5d1fc5e249136afe10fdbc55c0f2547.jpg)

- wkf::PlottingWidget

- 继承自 wkf::DockWidget，并包含一个 UtQtGL2DPlot。  
- 提供了一个默认的上下文菜单，用于一些常见操作。

- warlock::PlottingWidget

- 继承自 wkf::PlottingWidget，并使用一个 PlotUpdater 列表。  
- PlotUpdater 是一个专门设计用于从 WsfSimulation 对象中获取数据的类。

- 当用户从 Platform Data Display 启动绘图时，提供该 TreeWidgetItem 的插件会调用其 GetPlotUpdater 方法。

- 如果该方法未返回有效的 Updater，绘图将无法更新数据。

![](images/437300ede77f4123ed488c89e20fa9aec298afd9472a4e86053865139959c041.jpg)

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

- warlock::RunManager 负责加载 AFSIM 输入文件、创建 WsfScenario，以及管理用于运行模拟的线程。  
- 它还存储最近场景的列表。  
- 插件很少需要访问 RunManager，但有一些例外：

- DemoMode: 在GuiSimulationComplete()中，它会使用最近的场景调用LoadScenario()。  
- SimController: 根据用户操作调用 LoadScenario()。

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

11

![](images/68d2ff08cace4d25ea9d50b68c3948d5fc4df2a64c859c080ab89168af3d5161.jpg)

# SimInterface

![](images/1cf3dcb98a00cb18bc24e2a155b20e8008b142394b90fb32a0cff87292c8904f.jpg)

- SimInterface 类是访问模拟数据的唯一途径，因此几乎每个 Warlock 插件都会拥有一个。

- 提供使用 SimEvents 和 SimCommands 时的线程安全通信。  
- 已经连接到许多与模拟事件相关的虚方法，例如 PlatformAdded 和 SimulationStarting。  
- 要使用这些方法，只需重写它们即可。

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

- 周期性函数

- WallClockRead 和 SimClockRead

- 单次（非周期性）函数

- 所有其他公共虚方法，例如 PlatformAdded()。

- 将 SetEnabled(false) 设置为禁用时，会停止调用周期性函数，从而减少插件所需的计算时间。

- 单次函数仍然会被调用。  
- 命令在 Enabled 设置为 true 之前不会被处理。

- 在不需要周期性更新时（例如所有显示窗口都已关闭或隐藏），禁用 SimInterface 是一个好主意。

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQQD.

# UNCLASSIFIED

![](images/4bb04454dbfafd224f902c53b060d7f26f36c92b67da6905f23fec746cd905ad.jpg)

# SimEvents

![](images/43dc0ea2e6039b0759803df78b94861a6af28d6b8c9dc22e207f5ca8b7e62855.jpg)

- SimEvents 是通过调用方法 SimInterfaceT::AddSimEvent 从模拟线程发送到 GUI 线程的消息。

- SimInterfaceT 是一个类模板，其模板参数是用户定义的 Event 类型。  
- 每个插件都会定义自己的 SimEvent 接口，并包含其自定义的 Event 类型。

- 每个 SimEvent 都应有一个 Process 函数，用于规定事件在 GUI 线程上的处理方式。

- 从GUI线程中定期调用SimInterfaceT::ProcessEvents()。

- 通常在 Plugin::GuiUpdate() 方法中完成。

- 如果 ProcessEvents 的参数与 SimEvent 的 Process 方法的签名不匹配, 则会发生编译错误。

In file SimControllerSimEvents.hpp   
class SimControllerEvent : public warlock::SimEvent   
{ public: SimControllerEvent(bool aRecurring $=$ false) : warlock::SimEvent(aRecurring) {} virtual void Process(SimControllerDataContainer& aState) $= 0$ .   
}；   
class SimStartingEvent : public SimControllerEvent   
{ public: SimStartingEvent(bool aPaused) : SimControllerEvent(false) , mPaused(aPaused) {} void Process(SimControllerDataContainer& aState) override; private: bool mPaused; const std::string mStateString;   
}；

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

# UNCLASSIFIED

# SimEvent Example

15

![](images/acfac34f14c09348ebde8e3be77afe6d5f5a1dad26461bd4acb0d9326804aabb.jpg)

![](images/6a58879636bdfd4c09c4d7f9cbf6ed57ec4ec126f1c37ffe78ca5f1cf737bf5c.jpg)

In file SimControllerSimInterface.cpp   
```cpp
// Add a SimEvent to a SimInterface example  
void WkSimController::SimInterface::SimulationStarting(const WsfSimulation& aSimulation)  
{  
    AddSimEvent(ut::make_unique<SimStartingEvent>(aSimulation.IsExternallyStarted()));  
} 
```

In file SimControllerSimEvents.cpp   
```txt
// SimEvent::Process example implementation  
void WkSimController::SimStartingEvent::Process(SimControllerDataContainer& aState)  
{  
    aState.setStarting(mPaused);  
} 
```

In file SimControllerPlugin.cpp   
```cpp
// Make sure to call ProcessEvents at a regular interval to read data  
void WkSimController::Plugin::GuiUpdate()  
{  
    mInterfacePtr->ProcessEvents(mSimulationState);  
    mStatusWidgetPtr->Update();  
} 
```

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

- SimEvents 的基类（warlock::SimEvent）在构造函数中有一个名为 aRecurring 的布尔参数。

- 该参数用于指示 SimEvent 是否为循环消息。  
- 如果 SimEvent 被标记为循环消息，Warlock 只会处理给定类型的最新 SimEvent。  
- 这可以减少处理过时数据所花费的时间。  
- 在以多倍于实时的速度运行时非常有用。  
- 如果在适当的情况下不使用循环事件，可能会出现以下情况：模拟线程生成 SimEvents 的速度快于 GUI 线程处理 SimEvents 的速度，从而导致 Warlock 死锁。

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQQD.

17

![](images/83fd94067c01e20fe5362dc3017b37704ea2fd665377d15674402af9ec5671d7.jpg)

# SimCommands

![](images/077397e3adf5e7fd57ae8b7f6db397b48295bdd4587dce7dee0bcee621c23305.jpg)

- SimCommands 类似于 SimEvents，但它们是从 GUI 线程发送到模拟线程的消息。  
- SimCommand 基类定义在 VkSimInterface.hpp 中。

- Process(WsfSimulation&) 是一个纯虚函数，允许SimCommand 访问模拟。

- 调用 AddSimCommand 来发送一个 SimCommand。  
- SimCommand 的 Process() 方法会被自动调用。

- 根据构造函数的参数，Process() 可以基于墙钟时间（Wall Clock）或模拟时间（Simulation Clock）调用。

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQQD.

In file SimControllerSimCommands.hpp   
class SimCommand : public warlock::SimCommand   
{ public: SimCommand(   ) : warlock::SimCommand(true) \{\} //Execute these Commands on WallClock timer protected: static void SendXIO_Man Command(WsfSimulation& aSimulation, WsfXIO_SimTimeCommandPkt::CommandType aType, double aValue $= 0.0$ );   
};   
class PauseCommand : public SimCommand   
{ public: PauseCommand(bool aSendDIS) : SimCommand(   ) , mSendDIS(aSendDIS) \{\} void Process(WsfSimulation& aSimulation) override; private: bool mSendDIS;   
}；

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

# UNCLASSIFIED

# SimCommand 示例

19

![](images/9ce088b205fc1e23d605559418a1739189ce7c00f2d6582b77129798cc13b59c.jpg)

![](images/877ad07efaf0662092f35945dca19615470b8bf944a3b5e9e1e5af2f4011237d.jpg)

In file SimControllerSimCommands.cpp   
In file SimControllerToolBar.cpp   
```cpp
// SimCommand::Process example implementation
void WkSimController::PauseCommand::Process(WsfSimulation& aSimulation)
{
    if (mSendDIS)
    {
        WsfDisInterface* dis = WsfDisInterface::Find(aSimulation);
        if (dis != nullptr)
        {
            auto pdu = ut::make_unique<WsfDisStopFreeze>(dis);
            pdu->SetReason(DisEnum::Control::Reason::RECESS);
            dis->PutPdu(aSimulation.GetSimTime(), std::move(pdu));
        }
    }
    SendXIO_Cmond(aSimulation, WsfXIO_SimTimeCommandPkt::cPAUSE);
    aSimulation.Pause();
} 
```

// Adding a SimCommand to a SimInterface example  
mSimInterfacePtr->AddSimCommand(ut::make_unique<PauseCommand>(mSendDIS_PDUs));

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

- SimCommand 的 Process() 方法会根据传递给

warlock::SimCommand 的布尔值 aUseWallClock 自动调用:

- aUseWallClock == true: 表示该 SimCommand 应在墙钟时间（Wall Clock）推进时处理。  
- aUseWallClock == false：表示该SimCommand应在模拟时间（Sim Clock）推进时处理。

- 大多数 SimCommand 应使用模拟时间（Sim Clock），但任何需要在模拟暂停时处理的 SimCommand 都需要基于墙钟时间（Wall Clock）进行处理。

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

UNCLASSIFIED

![](images/0b26105eb0c07e9470424ba82ca463813daa1d9c14af6d39474baf2bf1d1ff09.jpg)

# 从SimCommand生成的SimEvents

![](images/5a6a495527ff1eb8adf1a1d8dc64afbe0a643a88e0f9bd9e85f0f0747af8c602.jpg)

- 某些 SimCommand 可能会从模拟线程生成需要发送回 GUI 线程的响应。这可以通过以下两种方式实现:

- 连接到在 SimCommand 执行时触发的回调（例如，当移除平台时触发的 WsfPlatformObserver::PlatformDeleted 回调），然后将 SimEvent 发送回 GUI。  
- 如果没有回调存在，可以在SimCommand::Process()方法中创建SimEvent。

In file SimControllerSimEvents.cpp   
void WkPlatformMovement::LocalRouteRequestCommand::Process(WsfSimulation& aSimulation)   
{ wkf::RouteBrowserInterface::RouteInfo info $=$ FindLocalRouteInfo(aSimulation, mPlatformName); if (mResponseEventType $= =$ ROUTE_SELECT) { AddSimEvent(ut::make_unique<RouteSelectEvent>(info)); } else if (mResponseEventType $= =$ ROUTE_DIALOG) { AddSimEvent(ut::make_unique<RouteDialogEvent>(info)); }

```cpp
void WkPlatformMovement::LocalRouteRequestCommand::Process(WsfSimulation& aSimulation)  
{ if (mResponseEventType == ROUTE) { WsfPlatform* platform = aSimulation.GetPlatformByName(mPlatformName); if (platform) { WsfMover* mover = platform->GetMover(); if (mover) { const WsfRoute* route = mover->GetRoute(); if (route != nullptr) { AddSimEvent(ut::make_unique<RouteEvent>(platform->GetIndex(), mPlatformName, route)); } else if (!mPlatformName.empty()) { wkf::RouteBrowserInterface::RouteInfo info = FindLocalRouteInfo(aSimulation, mPlatformName); if (mResponseEventType == ROUTE_SELECT) { AddSimEvent(ut::make_unique<RouteSelectEvent>(info)); } else if (mResponseEventType == ROUTE_DIALOG) { AddSimEvent(ut::make_unique<RouteDialogEvent>(info)); } } DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQDD. 
```

23

![](images/852f08a03bfe59338d291decf9f5a1cde075ce21d9d53aeed560597ac669c84b.jpg)

UNCLASSIFIED

# SimCommands 中的 WsfEvents

![](images/cf0220ac790556b08cdce9f44ee42dd8923095ced34e1eef7a3658198f62fe17.jpg)

- 在处理需要未来进行额外处理的 SimCommand 时，可以创建一个 WsfEvent 并将其添加到 WsfSimulation 的事件队列中。

# In file SimControllerSimCommands.cpp

```cpp
void WkSimController::AdvanceToTimeCommand::Process(WsfSimulation& aSimulation)  
{  
    ...  
    aSimulation.AddEvent(ut::make_unique<WsfOneShotEvent>(mSimTime, [=, &aSimulation](())) {  
        aSimulation.SetRealtime(simTime, true);  
        // Need to call resume due to the real-time clock being deleted and re-created,  
        // and the new clock potentially expecting a Resume() command.  
        pause ? aSimulation.Pause(): aSimulationResume();  
    });  
    aSimulation.SetRealtime(aSimulation.GetSimTime(), false);  
} 
```

不要从一个SimCommand中创建额外的SimCommand，因为这会导致不良的编程习惯。

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19.

Other requests for this document shall be referred to AFRL/RQQD.

• ScriptSimInterface 是一个专门的 SimInterface，用于处理与 AFSIM 脚本的交互：

- 获取全局和平台脚本信息。  
执行全局和平台脚本。

- 可以通过 Warlock Environment 访问：

simEnv.ScriptSimInterface()。

- 不要自行实例化此类，所有需要访问脚本信息的插件都可以通过相同的实例（使用 std::shared_ptr）进行访问。  
- 该接口被DialogBuilder和ScriptBrowser插件使用。

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQQD.

UNCLASSIFIED

![](images/7b6118ce641b2a84e9259479677bdda5d1adf9b1cfc39bbdb71859f071f4653f.jpg)

# 发送DIS和XIO消息

![](images/064408e15ce0f5a4cb401eeeebccf468fa44733ebb629e86c2e65eb9cc9057db.jpg)

• DIS 和 XIO 消息可以从 Warlock 插件（在模拟线程中）发送。

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.   
```cpp
void WkSimController::SimCommand::SendXIO_Management(WsfSimulation& aSimulation, WsfXIO_SimTimeCommandPkt::CommandType aType, double aValue /*= 0.0*/)  
{ WsfXIO_Interface* xio = WsfXIO_Extension::Find(aSimulation); if (xio) { WsfXIO_SimTimeCommandPkt pkt; pkt.mCommandType = aType; pkt.mSimTime = aValue; for (auto connection : xio->GetReliableConnections()) { connection->Send(pk); } }  
}  
void WkSimController::PauseCommand::Process(WsfSimulation& aSimulation) { if (mSimDIS) { WsfDisInterface* dis = WsfDisInterface::Find(aSimulation); if (dis != nullptr) { auto pdu = ut::make_unique<WsfDisStopFreeze>(dis); pkt->SetReason(DISEnum::Control::Reason::RECESS); dis->PutPdu(aSimulation.GetSimTime(), std::move(pdu)); }  
} 
```

27

![](images/bc59e2d895fb598160eb1d9615f1d4fc37be96115d760b94290eb0e626e9a658.jpg)

# UNCLASSIFIED

# 线程安全

![](images/bf323638b79e63dc8cab1f3bc8be4fafc972975710b51499dd8673abbe5d203f.jpg)

- Warlock 通过在单独的线程上启动 AFSIM 来运行。这意味着在与模拟进行通信时，必须考虑线程安全问题。

- 使用 mutex 锁定代码的关键部分。  
- 通常在读取/写入 SimInterface 类的成员数据时使用 mutex，因为这些数据可以被两个线程访问。  
- 仅锁定关键部分。  
- 避免长时间持有锁，因为这会影响性能。  
- SimInterface 提供了一个 QMutex 用于锁定数据。  
- 使用 SimEvents 和 SimCommands 来减少甚至消除在插件中使用 mutex 锁的需求。

- 在 Warlock 中，这两个线程通常被称为 GUI（或主线程）和 Sim 线程。

In file PlatformDataSimInterface.cpp   
```cpp
void WkPlatformData::SimInterface::WallClockRead(const WsfSimulation& aSimulation)  
{  
    std::string platformName;  
    if (mMutex.tryLock()) ← Use tryLock() because it is not critical that we update this frame since this is a periodic call.  
    platformName = mPlatformOfInterest;  
    mMutex.unlock();  
}  
} 
```

In file SensorVolumesSimInterface.cpp   
```cpp
void WkSensorVolumes::SimInterface::RemovePlatformOfInterest(unsigned int aPlatformIndex)  
{  
    QMutexLocker locker(&mMutex);  
    mPlatformsOfInterest[aPlatformIndex] &= (aWeapon ? eSENSOR : eWEAPON); // remove the appropriate bit from the component map  
    if (mPlatformsOfInterest[aPlatformIndex] == 0)  
        lock() or use of QMutexLocker will block until the mutex is available before allowing processing to continue. This should be used on all events that are non-periodic.  
} 
```

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

# UNCLASSIFIED

![](images/3bc24a6f2c5224fb994c24a85a6e23f40e906b12d26b8c07a9f0941d13bd0e91.jpg)

# 死锁

![](images/8b72b23a2ac93ad7b92699d92318cc8a00b7641e04af4ecb8856bae6b2df5d79.jpg)

- 不正确地使用 mutex 可能会导致死锁。

- 这发生在 mutex 未被释放时，而另一部分代码正在等待该 mutex 被释放以便锁定它。  
- 确保每次锁定 mutex 时都释放锁。

- QMutexLocker 是一个辅助类，提供了作用域锁定功能：

- 在其构造函数中锁定 mutex，并在 QMutexLocker 超出作用域（调用其析构函数）时自动解锁。

https://doc qt.io/qt-5/qmutexlocker.html

# 多线程编程问题回顾

- 死锁的四个必要且充分条件：

1. 互斥（Mutual Exclusion）

- 涉及的资源必须是不可共享的。如果资源是可共享的，进程就不会因为无法使用资源而被阻止。

2. 占有并等待（Hold and Wait 或 Partial Allocation）  
- 线程必须在等待其他（请求的）资源时，继续持有它们已经分配到的资源。

3. 不可抢占（No Preemption）

- 线程在使用资源时，资源不能被强制收回。线程只能在完成任务后自愿释放资源。

4. 资源等待或循环等待（Resource Waiting 或 Circular Wait）

- 存在一个线程的循环链，每个线程都持有其他线程正在请求的资源。例如，线程A持有资源1并请求资源2，而线程B持有资源2并请求资源1。

- 所有四个条件必须同时存在，死锁才会真正发生。  
- 在 Warlock 中，由于只有一个线程在执行模拟代码，因此获取锁/互斥锁相对容易，从而降低了死锁发生的可能性。

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQQD.

31

![](images/69ca7c78d9d6a37a570fa31368f34a637bd00de10ae2f79bad73996b9cb7e689.jpg)

# 常见的死锁问题

![](images/b7bfce616ae9ad1fbd2472968f11f635973d8f122445317bd9833c9687a31d71.jpg)

- 在 SimInterface 中，通常会有一个函数连接到

PlatformAdded() 回调。这个函数通常会在其内部锁定一个互斥锁（mutex）。

- 当执行一个脚本（Script）或调用 Platform::Update() 时，可能会创建一个新的平台（Platform），这会触发

PlatformAdded 的回调。

- 这意味着，如果在执行脚本或调用 Platform::Update 时互斥锁已经被锁定，你的代码将会发生死锁。

# In file WkScriptSimInterface.cpp

```txt
void warlock::ScriptSimInterface::PlatformAdded(double aSimTime, WsfPlatform& aPlatform)  
{ QMutexLocker locker(&mMutex); 这可能会导致死锁。如果将平台添加到模拟中的方法/函数已经持有 mMutex 的锁，那么当回调函数 PlatformAdded 被调用时，它在尝试获取锁时将会发生死锁。
```

• 上一张幻灯片描述了一种情况：一个线程已经持有某个资源的锁，然后尝试重新获取它已经持有的同一个资源。此时，该线程与自身形成了循环等待条件。

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

UNCLASSIFIED

![](images/5ad75eefd12c2082fece58467a4b90a003cb77ee67a8742cea16d118c7350a49.jpg)

# 可排队的消息对象

![](images/de378518c217c57cebb396b16b56f324514bae86212208a6704bbb5bd0b70794.jpg)

- wkf::QueueableMessageObject 封装了 QMessageBox,并内置了功能，使其在从模拟线程调用时能够将自身排队到 GUI 的事件循环中。  
- 这允许开发者向用户显示警告和错误信息，而无需担心线程问题。

wkf::QueueableMessageObject::DisplayQueuedMessage(QMessageBox::Warning, "Script Error", "Insert Warning Message Here");

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

接下来的几张幻灯片将介绍配置（Configurations）和偏好设置（Preferences）。

尽管这是Warlock培训幻灯片，但访问和使用配置与偏好设置在Warlock、Wizard和Mystic之间是通用的。

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

UNCLASSIFIED

# 配置

![](images/c88cf20c821ee5be4ce225f29ee5aadc1814a25d4da0480e385cf16802816d6f.jpg)

![](images/3e66d299443c19e2f491723376d8c3d98d3521ede5e39a7cefe409c4bcf712e4.jpg)

35

- 配置（Configuration）是所有偏好设置（Preference）选择的快照，包括加载的插件、可见窗口及其位置和大小。Warlock 允许用户保存、加载和导入配置。窗口几何形状以及在插件中创建的对话框是否显示，都会自动保存。偏好设置通过在 wkf::Plugin 中重写函数实现的 Save/LoadSettings 进行保存和加载。  
- 支持配置不需要额外的工作。

- 在创建、删除或修改平台之前，请检查用户是否具有权限。  
- 调用以下函数（VkPermissions.hpp）：

- warlock::HasPermissionToControlPlatform()   
- warlock::HasPermissionstoCreateOrRemovePlatforms()

![](images/f83f4d470293b31800f4fcaa77250837e3e882380e21bc530d2b9d05f57582ed.jpg)

![](images/debc14543696b759db2cf789b10f5a5fe00230a69e0dfe89c72e6f5b0f0eb60a.jpg)  
DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

# UNCLASSIFIED

![](images/74c63e7866bc5397d4262164191cbb9d2d30a09be43c1fe4918d960ff7198f2e.jpg)

# Preferences（首选项）

![](images/7c38a961a50cbfd59669cec4e83f1d5b815557391c5897349c5a61bd6ed2d0de.jpg)

- 所有WKF应用程序的共同点  
- 首选项对话框提供了一些应用程序标准选项，位于“环境”下：

指定要加载的地图  
定义键盘快捷键  
- 更改默认单位

- 插件可以添加自己的选项

定义一个 PrefObject 来包含数据  
定义一个 PrefWidget 来显示数据  
- 在您的插件类中重写 GetPreferencesWidgets()

![](images/332edb87fa130cf75f40031c8f38696c77d52e09c65f0f35b472872f22c5ea93.jpg)

- PrefObject 负责从文件中读取和写入选项。

- 当选项发生更改时，该类会发出信号以通知订阅者更改（包括相应的 PrefWidget 更新其显示）。

- PrefWidget 负责选项的显示。

- 它是插件在“Preferences”对话框中首选项的接口。  
- 插件的 PrefWidget 将从 PrefWidgetT 类模板派生，并以 PrefObject 作为模板参数。  
- PrefWidget 应仅与其对应的 PrefObject 交互。  
- 任何类都不应直接从 PrefWidget 获取信息，而应从 PrefObject 获取信息。

不要从PrefWidget发送任何信号

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQQD.

UNCLASSIFIED

![](images/7c18c4ad68fde1add86be149ea34c580552af6cca0a710f55d9bbd0d58453680.jpg)

# 快捷键 & wkf::Action

![](images/20524aeae054631886a9581808fb3a419df5abb7e65df67b592c9dfb8c18acd0.jpg)

- 要在“Preferences”对话框的“Keyboard Shortcuts”页面中添加操作，需要在插件类中重写GetActions()方法。

- 该方法应返回一个 wkf::Action 的列表。

- wkf::Action 是从 QAction 派生的类。

- 它具有默认的按键序列。  
- 允许用户重新绑定按键序列。  
- 允许用户恢复到默认按键序列。

![](images/92843ec7992944da19cc6d8b722ca26dcee2e42e48fe8bc3d658c232eb4428a4.jpg)

- 用户对按键序列的修改会被自动保存，无需在插件中进行额外的处理。

- “Units”页面控制 Warlock 应用于显示不同数值类型的单位。  
- 在插件中使用这些单位非常简单。

- WkfUnitTypes.hpp 定义了用于在树和表中显示数值的项目，这些项目已经与单位首选项集成。  
- 这些项目会自动转换单位，并在用户更改默认单位时自动更新。

- 只需声明项目类型即可：

```cpp
mSpeed = new wkf::SpeedTreeMenuItem(aParentItem, "Speed: "); 
```

- 请务必在适用时使用单位项目——显示的单位与应用程序的其余部分不匹配会显得非常糟糕。

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQQD.

UNCLASSIFIED

![](images/2dacd7a108d046409c97d9d38354b6481e7c1f4efad57017fb64ec26bf1e4d4b.jpg)

warlock::net::Network

![](images/816a070765bfab84206cfd0e36017980c2f9542aa6c2702b139f79f380f7c03b.jpg)

- warlock::net::Network 是一个 Warlock-to-Warlock 的多播网络接口，用于模拟分布式信号和槽机制。  
- 可以通过 wkEnv.GetNetwork(); 访问它。

//Defining a packet type. 使用DerivePacket<DemoPacket>会添加调用正确回调所需的机制。  
using namespace warlock::net;  
struct DemoPacket:DerivePacket<DemoPacket>  
{QString PacketType() const override{return"DemoPacket";}Field<PlatformId>mPlatform{this，"platform”};通过添加字段（Fields），数据的序列化Field<Int32>mData{this，"data"};字段类型包括：Boolean、Int32、Float32、  
};  
//Sendinga packet.DemoPacket pkt;pkt.mPlatform->SetPlatform platformPtr);Float64、String、Color、Platfromld、List<T>和自定义对象。  
pkt.mData->Set(value);  
bool success $\equiv$ wkEnv.GetNetwork().Publish(pkt);  
//Definingacancelback.  
void Plugin::OnPacketReceived(const DemoPacket&aPacket)  
{warlock::Platform\* platform $=$ aPacket.mPlatform->GetPlatform();int value $=$ aPacket.mData->Get();if（platform != nullptr）{…}订阅回调必须添加到UtCallbackHolder  
}中。  
//SubscribingtoDemoPacket.  
wkEnv.GetNetwork().RegisterPacket<DemoPacket>();  
mCallbacks $+ =$ wkEnv.GetNetwork().Subscribe<DemoPacket>(&Plugin::OnPacketReceived,this);

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQDD.

# UNCLASSIFIED

![](images/c81e12dca0ddb3f17f4bd8d509cc506c993c9fe810f7e09fb5891c90c692ead3.jpg)

# Warlock插件结构

![](images/7d26adcd49fd2817dfab6ba24c1372d706757a10efd77e023e3c706705f42517.jpg)

- 插件的公共组件如下:

- PrefObject 和 PrefWidget  
- SimInterface   
- SimEvents   
- SimCommands   
- 显示组件（如 DockWidget 或对话框）  
- DataContainer: 用于存储来自仿真的信息  
- PlotUpdaters   
- 类型文件：用于定义自定义数据类型

![](images/230ce68b7b6d5e7bc1876249ac61505fae965b7acf5d858b73500ff058be2371.jpg)

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

# UNCLASSIFIED

![](images/8894d78111b43e50526b4b9ea248761a87e16f5e4e6dc90baff7b8a22049adf4.jpg)

# 插件示例

![](images/d5a5514460301b4c15cab03ef5f0010988f206606cbb77d3554dd702e6fd568f.jpg)

- Warlock 中有许多插件可以作为参考。

- 一些适合作为示例的插件包括:

- DemoMode: 因为它是一个非常简单的插件。  
- SimController: 因为它既与仿真交互以读取数据，又能控制仿真。  
- PlatformData：因为它展示了如何使用 Updaters 并将数据写入上下文对话框中。

- 创建一个 Warlock 插件，功能如下：

- 获取所选平台的位置和航向信息，并在 DockWidget 中显示这些信息。  
- 在 DockWidget 中提供一个按钮，用于控制所选平台的转向，并为这些操作提供快捷键。  
- 创建一个首选项小部件（Preference Widget），允许用户配置在 DockWidget 上显示的信息。

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQQD.

47

![](images/29b8b6cbee20f7a7fa9fbe286ba4993e50a4a702ed6c69209bd5f5da9462cd06.jpg)

# 配置 Warlock 培训

![](images/ca26b10a2e31b58b23fca1a15514d2a9e8f865a329fdd73b10b0fadb98b26f1c.jpg)

在下面文件中：training/developer/wkf/labs/config.cmake

- 确保以下设置的是TRUE

- BUILD_WARLOCK_PLUGIN_WarlockTraining   
- BUILD WITH warlock   
- BUILD_WITH.wsf_mil   
- BUILD_WITH.wsf_p6dof   
- BUILD_WITH_wsf_parser   
- BUILD_WITH_wsf_space   
- BUILD_WARLOCK_PLUGIN_P6dofController   
- BUILD_WARLOCK_PLUGIN_P6dofData   
- BUILD_WARLOCK_PLUGGIN_PlatformBrowser   
- BUILD_WARLOCK_PLUGGIN_PlatformData   
- BUILD WARLOCK Plugin SimController   
- BUILD_WARLOCK_PLUGIN_VisualEffects   
- BUILD_WIZARD_PLUGIN_WizMapAnnotation   
- BUILD_WKF_PLUGIN_MapDisplay   
- BUILD_WKF_PLUGIN_MapHoverInfo   
- BUILD_WKF_PLUGIN_TetherView

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

在CMD中(Windows):

- cd到AFSIM文件夹(包含training的文件夹)  
- 执行以下命令：

> cd training\developer\wkf\Labs   
> scriptpath=%cd%\config.cmake   
> cd inwork   
>extpath=%cd%

如果工作在AFSIM release模式下，执行：

>cd...\...\...\swdev\src

- 其它模式下, 执行:

>cd...\...\...\...\afsim

最终，执行：

> set srcpath=%cd%   
>cd...\build   
>rm CMakeCache.txt   
> cmake -C %scriptpath% -DWSF_ADD Extensions_PATH:PATH=%extpath% -B . -S %srcpath%

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQQD.

49

![](images/a034bc9277005ffa057d66544b65c293d1141aa90ec0ce2af5d046d95c4099fd.jpg)

# UNCLASSIFIED 配置 Warlock 培训 (bash shell)

![](images/d6295b2b802a135df3e79261a623388a9b1bdedc514fb1d441473b6f245b296d.jpg)

在bash shell中 (git bash 在Windows下或 bash 在 Linux下):

- cd到AFSIM文件夹(包含training的文件夹)  
- 执行以下命令；

$ cd training/developer/wkf/labs   
$ scriptpath=$PWD/config.cmake   
$ cd inwork   
$ extpath=$PWD

如果工作在AFSIM release模式下，执行：

$ cd ..//././.swdev/src

- 其它模式下, 执行:

$ cd ../../../..//afsim

最终，执行：

$ srcpath=$PWD   
$ cd ../build   
$ rm CMakeCache.txt   
$ cmake -C $scriptpath -DWSF_ADD Extensions_PATH:PATH=$extpath -B . -S $srcpath

- 检查 Types.hpp 文件。

- 注意，结构体 PlatformData 包含四个成员变量，分别对应平台的纬度、经度、高度和航向。

namespace WarlockTraining   
{ struct PlatformData double mLatitude $= 0$ double mLongitude $= 0$ double mAltitude $= 0$ double mHeading $= 0$ . }；

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQQD.

51

![](images/c348b4e13706b3c72a937b74523915712faecb2be261d3b17966ee982f3e07f0.jpg)

# UNCLASSIFIED

# 练习1 Review 2

# SimInterface.hpp

![](images/b58f48a83f5d782380db7f4c380fe45cb7bfcd188dddeb5a39e0d0cc76cb7450.jpg)

- 检查 SimInterface.hpp 文件。

- 注意，SimInterface 继承自 warlock::SimInterfaceT<EventBase>。

```cpp
namespace WarlockTraining   
{ //! This represents the specific simulation interface we are creating. //! Inheriting from warlock::SimInterfaceT<T> tells the class what type of //! event the interface creates. class SimInterface : public warlock::SimInterfaceT<EventBase> { Q_OBJECT   
public: SimInterface(const QName& aPluginName); //! Creates an UpdateEvent. //! This function will be updated every time the simulation clock updates. //! @param aSimulation This is the simulation whose clock updated. void SimulationClockRead(const WsfSimulation& aSimulation) override; };   
} 
```

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

- 在 Plugin.hpp, 有 3 个方法和 4 个成员变量  
Other requests for this document shall be referred to AFRL/RQQD.   
class Plugin : public warlock::PluginT<WarlockTraining::SimInterface>   
public: Plugin(const QString& aPluginName, const size_t aUniqueId); \~Plugin() override $=$ default; //! Called periodically to update the GUI. void GuiUpdate(） override; //! Returns a list of the preferences widgets that this plugin provides. //! @note Without this function, the PrefWidget for this plugin will not appear in the Preferences menu. QList<wkf::PrefWidget\*> GetPreferencesWidgets(） const override; //! Returns a list of the actions that this plugin provides. //! @note Without this function, the actions for this plugin will do nothing. QList<wkf::Action\*> GetActions(） const override;   
private: //! The container of Data of this plugin DataContainer mDataContainer; //! The preferences widget to display. PluginUiPointer<PrefWidget> mPrefWidget; //! The DockWidget that displays information PluginUiPointer<DockWidget> mDockWidget; //! The actions that this plugin uses. QList<wkf::Action\*> mActions;   
}； DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19.

![](images/7e5ba1b8fc15873e38022efd6d06b2249a0373a834e969371800abf7b2414eb6.jpg)

# UNCLASSIFIED

# 练习1 Review 4

# SimEvents.hpp

![](images/85f000ea9f2606627286c37258d68434e5100d888cca5be0210e768572938191.jpg)

- 在SimEvents.hpp文件中：

- 注意类 EventBase 和类 UpdateEvent。  
- 注意每个类中的 Process 方法。

class EventBase : public warlock::SimEvent   
public: EventBase(bool aRecurring) : warlock::SimEvent(aRecurring) \{\} //! All event types should have a Process function. The arguments can vary depending on need. virtual void Process(DataContainer& aDataContainer) $= 0$ .   
\};   
//! This is an event that represents the clock updating. class UpdateEvent : public EventBase   
public: UpdateEvent(const std::map<std::string, PlatformData>& aData); //! Processes the event by updating the DockWidget's display. void Process(DataContainer& aDataContainer) override;   
private: //! Data about all platforms' position and heading. std::map<std::string, PlatformData> mData;   
\};

- 在 DataContainer.hpp 文件中:

- 注意类中的方法。  
- 注意 Qt 信号 DataChanged。  
- 注意私有成员变量。

```cpp
class DataContainer : public QObject   
{ Q_OBJECT   
public: PlatformData GetPlatformData(const std::string& aPlatformName) const; void SetData(const std::map<std::string, PlatformData>& aData);   
signals: void DataChanged();   
private: std::map<std::string, PlatformData> mData;   
}; 
```

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

# UNCLASSIFIED

# 练习1- 任务1

55

![](images/1adbb77020f9091d9c78d8beddeafbe91242376c56490ffb9264883fb2ba0d69.jpg)

![](images/fd1d6fbcd43382ce289491501f0127e9667ff40a7a0bbad5cc46921d66a4c789.jpg)

- 从仿真中的平台获取位置和航向信息：

- 在 SimInterface.cpp 文件中的

WarlockTraining::SimInterface::SimulationClockRead 方法中创建一个 UpdateEvent。

- 调用 AddSimEvent 方法，传入一个参数，该参数是一个指向 UpdateEvent 的新 unique_ptr，并使用上述的 std::map PlatformData 构造该 UpdateEvent。

- 在SimEvents.cpp文件中：

实现WarlockTraining::UpdateEvent::Process方法。   
- 调用 aDataContainer 的 SetData 方法，并传入 mData。

- 在 DataContainer.cpp 文件中：

- 对WarlockTraining::DataContainer::SetData方法进行实现，将数据存储在DataContainer中，并通知订阅者数据已更改。

- 在 Plugin.cpp 文件中的 WarlockTraining::Plugin::GuiUpdate 方法中：

- 调用 SimInterface 的 ProcessEvents() 方法。  
- ProcessEvents 的参数是插件类的 DataContainer 成员变量。

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19.

Other requests for this document shall be referred to AFRL/RQQD.

void WarlockTraining::SimInterface::SimulationClockRead(const WsfSimulation& aSimulation) { std::map<std::string, PlatformData> platformData;

```cpp
// For each platform, add its information to dataForEvent.   
for(std::size_t i = 0; i < aSimulation.GetPlatformCount(); i++)   
{ WsfPlatform* platform = aSimulation.GetPlatformEntry(i); if (platform) { PlatformData& dataBeingRead = platformData[platform->GetName()); //Get the position information for the platform platform->GetLocationLLA(dataBeingRead.mLatitude, dataBeingRead.mLongitude, dataBeingRead.mAltitude); //Dummy variables for in-out parameters. double pitch, roll; //Get the heading information for the platform platform->GetOrientationNED(dataBeingRead.mHeading, pitch, roll); } } //EXERCISE 1 TASK 1a // Create the UpdateEvent and then add it to the SimInterface note: std::make_unique can't be used until c++14, since AFSIM is c++11 we have to use ut::make_unique instead. AddSimEvent(ut::make_unique<UpdateEvent>(platformData)); 
```

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

# UNCLASSIFIED

# 解决方案- 练习1 任务1.b, 1.c, 1.d

57

![](images/455eb8d2cc4fb94b87d57df71c29f2c470e18536b0f24250e4bc058371a1fe2f.jpg)

# SimEvents.cpp

```cpp
void WarlockTraining::UpdateEvent::Process(DataContainer& aDataContainer)  
{ // EXERCISE 1 TASK 1b // Add mData to the DataContainer  
aDataContainer.setData(mData); 
```

# DataContainer.cpp

```cpp
void WarlockTraining::DataContainer::SetData(const std::map<std::string, PlatformData>& aData)  
{ // EXERCISE 1 TASK 1c // Store aData and emit the DataChanged() signal  
mData = aData;  
emit DataChanged(); 
```

# Plugin.cpp

```cpp
void WarlockTraining::Plugin::GuiUpdate()   
{ //EXERCISE1TASK1d //CallProcessEventson theSimInterface so that we can process the SimEventswe have created //Remember the argument to ProcessEvents is the DataContainer mInterfacePtr->ProcessEvents(mDataContainer);   
} 
```

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19.

Other requests for this document shall be referred to AFRL/RQQD.

- 检查 DockWidget.hpp 文件:  
- 注意以下是信号在 DockWidget.cpp 中建立的槽（目标）：

- TurnToHeading  
- PlatformOfInterestChanged   
- PreferencesChanged   
- UpdateDisplay

- 注意以下成员变量：

- mPlatformOfInterest   
- mSimInterface   
- mDataContainer   
- mUI

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

59

![](images/e187cb9676e9bbd42c6bd3c3e38aa56d6c500c0a0c31c3c137d4112ec83f7116.jpg)

# UNCLASSIFIED

# 练习1 Review 6

# DockWidget.hpp

![](images/0cc919dcb825dd6dbcc0acb80a70137f176e95f52164be9807b7678658a246cb.jpg)

namespace WarlockTraining

```txt
{ //! This represents the specific dockable widget associated with our plugin. class DockWidget : public QDockWidget { // This line is required for Qt signals to be properly emitted from this class. Q_OBJECT 
```

public:

```cpp
DockWidget(SimInterface& aSimInterface, DataContainer& aDataContainer, PrefObject* aPrefObject, Qt::WindowFlags aWindowFlags = Qt::WindowFlags()); 
```

void TurnToHeading(double aHeading);

private:

```cpp
void PlatformOfInterestChanged(wkf::Platform* aPlatform);  
void PreferencesChanged(const PrefData& aPrefData);  
void UpdateDisplay(); 
```

std::string mPlatformOfInterest;

SimInterface& mSimInterface;  
DataContainer& mDataContainer

```rust
/// This contains all of the components that will appear on the screen.
/// The UI::WarlockTraining class is generated from the file "SimListenerDockWidget.ui".
/// Its name comes from the "objectName" field.
Ui::WarlockTraining mUI; 
```

}；

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19.

Other requests for this document shall be referred to AFRL/RQQD.

- 在 DockWidget 上显示“关注平台”（Platform of Interest）的位置信息和航向信息：

1. 在 DockWidget.cpp 文件中:

- 将 DataContainer 的 DataChanged 信号连接到 DockWidget 的 UpdateDisplay 方法。  
- 将wkf::Environment的PlatformOfInterestChanged信号连接到DockWidget的PlatformOfInterestChanged方法。

2. 更新显示内容以展示从 DataContainer 接收到的数据：

- 对mUI的每个LineEdit成员（用于显示纬度、经度、高度和航向）调用SetValue方法。

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

61

![](images/daaa785792620755b6c79c5dc024c1ef52c26131a13d7d5fd0b5f17f133f1802.jpg)

# UNCLASSIFIED 解决方案-练习1 任务2

# DockWidget.cpp

![](images/cbe797b491f397e79abdb1f3936c9ffb2af0601b999bfc06e677586691fae53a.jpg)

```cpp
WarlockTraining::DockWidget::DockWidget(SimInterface& aSimInterface, DataContainer& aDataContainer, PrefObject* aPrefObject, Qt::WindowFlags aWindowFlags) : QDockWidget(nullptr, aWindowFlags) , mSimInterface(aSimInterface) , mDataContainer(aDataContainer)   
{ //! Without this line, nothing will show up in the dock widget. mUI_setupUi(this); // EXERCISE 1 TASK 2a // Connect the DataContainer's DataChanged signal to UpdateDisplay() // Connect the WkfEnvironment's PlatformOfInterestChanged signal to PlatformOfInterestChanged() connect(&mDataContainer, &DataContainer::DataChanged, this, &DockWidget::UpdateDisplay); connect(&wkfEnv, &wkf::Environment::PlatformOfInterestChanged, this, &DockWidget::PlatformOfInterestChanged); void WarlockTraining::DockWidget::UpdateDisplay() { //Get the data for the platform of interest from the DataContainer PlatformData data = mDataContainer.GetPlatformData(mPlatformOfInterest); mUI.nameOutput-> setText(QString::fromStdString(mPlatformOfInterest)); // EXERCISE 1 TASK 2b // Using the PlatformData, set the value to display in the latitude, longitude, altitude, and heading LineEdits mUIlatitudeLineEdit->SetValue(data.mLatitude); mUI.longitudelineEdit->SetValue(data.mLongitude); mUI.altitudeLineEdit->SetValue(data.mAltitude); mUIheadingLineEdit->SetValue(data.mHeading); 
```

}

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19.

Other requests for this document shall be referred to AFRL/RQQD.

- 在 DockWidget.cpp 中，实现逻辑，当点击四个按钮（北、东、南、西）之一时发送一个 TurnCommand。

1. 将四个按钮的 clicked() 信号连接到 TurnToHeading() 方法，并传入正确的航向值作为参数：

- 北（North）：0度  
东（East）：90度  
- 南（South）：180度  
- 西（West）：270度

- 在 TurnToHeading 方法中:

1. 创建一个TurnCommand，并将其添加到SimInterface中。  
2. 调用 AddSimCommand 方法，传入一个参数，该参数是一个指向 TurnCommand 的新 unique_ptr，并使用 mPlatformOfInterest 和 aHeading 变量构造该 TurnCommand。

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQQD.

63

![](images/7773bf38cbee77632b50028921abb96390daf1ac191a9366014a1be27cf14f1b.jpg)

# UNCLASSIFIED 解决方案-练习1 任务3

# DockWidget.cpp

![](images/91967d6b5bb4bf2b36a9584881a004906ed58013223d01ab7b452285e4fb1630.jpg)

```cpp
WarlockTraining::DockWidget::DockWidget(SimInterface& aSimInterface, DataContainer& aDataContainer, PrefObject* aPrefObject, Qt::WindowFlags aWindowFlags) : QDockWidget(nullptr, aWindowFlags) , mSimInterface(aSimInterface) , mDataContainer(aDataContainer)   
{ //! Without this line, nothing will show up in the dock widget. mUI_setupUi(this); . // EXERCISE 1 TASK 3a / connect the clicked signal for northPushButton, eastPushButton, southPushButton, // and westPushButton to TurnHeading with appropriate heading passed in as an argument   
connect(mUI.northPushButton, &QPushButton::clickcd, this, [this]( {TurnToHeading(0); }); connect(mUI.eastPushButton, &QPushButton::clickcd, this, [this]( {TurnToHeading(90); }); connect(mUI.southPushButton, &QPushButton::clickcd, this, [this]( {TurnToHeading(180); }); connect(mUI.westPushButton, &QPushButton::clickcd, this, [this]( {TurnToHeading(270); });   
void WarlockTraining::DockWidget::TurnToHeading(double aHeading)   
{ // EXERCISE 1 TASK 3b // Create the TurnCommand (arguments should the platform of interest and the desired heading) // and then add it to the SimInterface // note: std::make_unique can't be used until c++14, // since AFSIM is c++11 we have to use ut::make_unique instead. mSimInterface.AddSimCommand(ut::make_unique<TurnCommand>(mPlatformOfInterest, aHeading)); 
```

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19.

Other requests for this document shall be referred to AFRL/RQQD.

- 在SimCommands.hpp文件中：

- 注意到TurnCommand类是此文件中唯一的SimCommand。  
- 注意到 Process 方法，以及成员变量 mHeading 和 mPlatformName。

class TurnCommand : public warlock::SimCommand   
{   
public: TurnCommand(const std::string& aPlatformName, double aHeading); \~TurnCommand() override $=$ default; //! Processes the command by changing the heading of the platform in question. //! @param aSimulation This is the simulation to modify. void Process(WsfSimulation& aSimulation) override;   
private: //! This is the direction to turn to. double mHeading; //! This is the name of the platform to be modified. std::string mPlatformName;   
};

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQQD.

65

![](images/c53acfb344a8e7716b986ba0712ae047585a6d1c13a2027ef5fd3ff82ae0f868.jpg)

# 练习1- 任务4

![](images/debeea4106431a394b6eef847ed7dc138fb8209dff3a809a5d89d6e6a7329394.jpg)

- 实现 TurnCommand::Process() 方法，使选定的平台能够转向指定的航向：

- 使用 mover，调用 TurnToHeading 方法，并传入以下参数：

- 当前仿真时间，通过GetSimTime()获取；  
- 将mHeading转换为弧度后的值；  
- 加速度为 0 ;  
- WsfPath::cTURN_DIR_SHORTEST。

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

void WarlockTraining::TurnCommand::Process(WsfSimulation& aSimulation)  
{ WsfPlatform* platform = aSimulation.GetPlatformByName(mPlatformName); if (platform) { WsfMover* mover = platform->GetMover(); if (mover) { // EXERCISE 1 TASK 4 // Command the mover to turn to the specified Heading mover->TurnToHeading(aSimulation.GetSimTime(), //When to turn mHeading * UtMath::cRAD_PER_DEG, //Where to turn to 0, //Acceleration. $0=$ use default WsfPath::cTURN_DIR_shortTEST); //Direction to turn (left/right) } }

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQDD.

67

![](images/a9696578fde2e1b462965dffa2b0add53b130e0fa0c7f4acd81101787aa73d12.jpg)

# UNCLASSIFIED

# 测试

![](images/800c3d74d66851ba6de5726681e3c715d8eefb83ca5b179565c31c5c10b30e25.jpg)

- 此时，您应该能够运行 Warlock，并在 Warlock Training 的 DockWidget 中看到所选平台的信息显示，同时可以通过按钮控制所选平台。

- 在Visual Studio当中：

- 在“Release”模式下进行构建  
- 构建“INSTALL”项目

- 在Linux下，在构建的目录(build directory)下执行如下命令：

$ cmake --build . --target all -- -j12

$ cmake --build . --target install -- -j12

- 在Warlock中运行测试想定Test Scenario

运行warlock.exe   
加载测试想定：training\developer\wkf\labs\data\wkf_trainingscenario.txt

![](images/01d0384f2172c089ed630df81f71397200f6bfdeb6c8f4aa6a63bc34e739e9a1.jpg)

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

69

![](images/a139cc4bcef7a02f75bda64b654c1711e8e6eb20179500fcc8fbccce0f194f2a.jpg)

# UNCLASSIFIED 练习2-任务1

Plugin.cpp

![](images/8e83dffa27d0f2730258707718a700d0f54426d6d228480214e72405b26f8246.jpg)

- 将插件连接到首选项系统：

1. 重写 GetPreferencesWidget() 方法，并返回 PrefWidget 成员的 QList。  
2. 重写 GetActions() 方法，并返回存储在成员变量 mActions 中的 QList<wkf::Actions>。