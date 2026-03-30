- 应用程序、场景和仿真都可以被“扩展”

- 应用扩展由应用程序拥有  
- 代表可以添加到应用程序的可选功能  
- 如果需要新的脚本类型（传感器、武器、组件、移动器），则使用应用扩展  
- 这是在AFSIM中注册所有扩展的入口点  
- 如果要创建场景扩展或仿真扩展，则需要应用扩展  
- 如果我们正在创建新的脚本，或者需要注册新的插件，我们也需要应用扩展  
- 我们将使用默认的应用扩展，因为我们只需要注册场景和仿真扩展  
- 请参见文件XIO PluginRegistration.cpp

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQQD.

28

![](images/1aa3fea882688b2ee8abd56b10ca8ecbd2d7fa518c5854b207cc5d634ca59829.jpg)

# XIO 练习1 - 检视1

# XIO_RegISTRATION.cpp

![](images/e29964a9b49d6f19ebb1f3b7ec4af2c0ea9eb0e4fb87101d54bf6cd6b774e219.jpg)

- 熟悉 WsfPluginVersion 和 WsfPluginSetup

- WsfPluginSetup 注册一个 WsfDefaultApplicationExtension   
- WsfDefaultApplicationExtension::ScenarioCreated 在执行时注册一个 RegisterPlatformController 场景扩展  
- 这个对象加载方案应该开始变得熟悉！

extern "C"

```cpp
/// This method is called to check the plugin version and compiler type.  
/// If values do not match the plugin will not load.  
XIO_EXERCISE exports void WsfPluginVersion(UtPluginVersion& aVersion)  
{  
    aVersion = UtPluginVersion(WSF Plugin_APIMajor_VERSION,  
                      WSF Plugin_APIMinor_VERSION,  
                      WSF Plugin_API_COMPILER_STRING);  
}  
注意，WsfDefaultApplicationExtension是基于  
/// This method is called RegisterPlatformController（一个场景扩展）进行模板化的。  
XIO_EXERCISE exports void WsfPluginSetup(WsfApplication& aApplication)  
{  
    // Make an application extension that creates a scenario extension for every scenario.  
    aApplication.RegisterExtension("platform_controller-registration",  
                      ut::make_unique<WsfDefaultApplicationExtension<RegisterPlatformController>>(););  
    aApplication.ExtensionDepends("platform_controller-registration", "wsf_p6dof", true);  
} 
```

}

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

# - 要扩展应用程序，您必须创建一个继承自 WsfApplicationExtension 的类

# class myAppExtension: public WsfApplicationExtension { ... }

- 您应该重写以下成员：

- AddedToApplication: 接收扩展被添加到应用程序的通知，通常用于注册额外的脚本类和方法等.  
- ScenarioCreated: 在场景构造函数结束时调用，以接收来自应用程序的场景创建通知，如果需要，可以用于注册场景扩展  
- SimulationCreated: 在仿真的初始化方法中调用，以接收来自应用程序的仿真创建通知，如果需要，可以用于注册仿真扩展  
- ProcessCommandLine: 从 WsfApplication::ProcessCommandLine 方法调用，以检查当前参数并在必要时处理它  
- PrintGrammar: 打印扩展识别的扩展语法  
- ProcessCommandLineCommands: 由 WsfApplication 的 ProcessCommandLineCommands 调用，以允许扩展处理/处理其需要识别的任何命令

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQQD.

30

![](images/6ee79398bd99afdc91ab85462e86d11935d12ddf58ca526687d59870d032b874.jpg)

# XIO 练习应用扩展

![](images/518d256e43101e076001b04a7efe47af0e4238d4c76d1a06049a52f4e037a81b.jpg)

# - 要扩展一个应用程序，您必须创建一个继承自 WsfApplicationExtension 的类

- 我们将使用 WsfDefaultApplicationExtension，它将注册场景扩展

# class WsfDefaultApplicationExtension: public WsfApplicationExtension { ... }

- 该类重写了应用扩展的以下成员:

- ScenarioCreated：在场景构造函数结束时调用，以接收来自应用程序的场景创建通知——如果需要，便于注册场景扩展

- 该类是基于 WsfScenarioExtension 进行模板化的（RegisterPlatformController 是从此类派生的）

- 当 ScenarioCreated 方法由 WsfScenario 构造函数执行时，我们的 RegisterPlatformController 类作为场景扩展与场景注册

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

- 场景也可以被“扩展”

场景扩展由场景拥有

代表可以添加到场景的可选类型  
如果需要新的类型（组件、观察者、通信），则使用场景扩展  
如果要创建场景扩展（或仿真扩展——稍后讨论），则需要应用扩展

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQQD.

32

![](images/3b8965f38347032d914344c906c2154b2cb5320b1b8ba956ef0a50aab1efe390.jpg)

# UNCLASSIFIED

# 想定扩展

![](images/52a715f49c737f7e97cb213a124d4d25501f41fc44ba9c192c26f2f8772d6f1e.jpg)

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

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

- 要扩展一个场景，您必须创建一个继承自 WsfScenarioExtension 的类

class RegisterPlatformController: public WsfScenarioExtension

- 我们将重写:

- SimulationCreated: 从 WsfSimulation::Initialize 调用——如果场景扩展需要一个关联的仿真扩展，这个方法可以注册仿真扩展

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

34

![](images/274368d4e96db90a3daa28881b2b71e183b482793cc682bd6cbda50eb0e9efb5.jpg)

# UNCLASSIFIED

# 仿真扩展

![](images/037e2e001e32134ed5d0a315a1b5c29767560ff22f9a87d2d4367267f2ddd53d.jpg)

- 仿真也可以被“扩展”

仿真扩展由仿真拥有  
- 允许访问仿真功能  
- 如果需要访问仿真本身（观察者、通信、XIO），则使用仿真扩展  
- 如果要创建仿真扩展，则需要应用扩展（并且您可能还需要场景扩展）

- 我们需要仿真扩展的情况：

- 我们需要知道何时添加或删除平台  
- 我们需要访问仿真的某些部分以控制平台

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

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQQD.

36

![](images/2ea176e611b3c733b25228f96ca9983b63a842ce30077d9b9f3846084b9765e0.jpg)

# XIO 练习仿真扩展

![](images/1befd9ee883b8f1da52f05ef49d9c40b500b0391c0bf2a793f8db4f15a6c4309.jpg)

- 要扩展一个模拟（Simulation），您必须创建一个继承自 WsfSimulationExtension 类的类

class PlatformControlService: public WsfSimulationExtension

- 我们将重写以下方法:

- Start: 该方法在 WsfSimulation::Initialize 中被调用，适用于通知扩展程序模拟即将开始

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

- 完成 RegisterPlatformController::SimulationCreated 方法。使用模拟对象参数来注册一个扩展，命名为 platform_controller。  
- 提供 PlatformControlService 的新实例作为参数（使用 unique_ptr 来创建它）。  
- 请记住，SimulationCreated 方法是在模拟对象的构造函数中执行的，紧接着它被实例化之后。

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQQD.

38

![](images/9e1f5cd8cfb28ad3e491a6134c4c76d713a98f193babb63c26848d1cff49fe44.jpg)

# XIO练习1-任务1解决方案

# XIO_RegISTRATION.cpp

![](images/8cafd004f27734bff772f148ebe15a16232d5024127f633bc029d08835417002.jpg)

```cpp
class RegisterPlatformController : public WsfScenarioExtension   
{ public: ~RegisterPlatformController(   ) noexcept override = default; void SimulationCreated(WsfSimulation& aSimulation) override { // EXERCISE 1 TASK 1 // Use the simulation object to register an extension // Name this extension "platform_controller" // Provide a new instance of PlatformControlService as a parameter aSimulation.RegisterExtension("platform_controller", ut::make_unique<PlatformControlService>(); } }; 
```

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQDD.

- 检查 PlatformControlService.hpp 文件:

- 注意到 start 方法重写了 WsfSimulationExtension 的一个方法。  
- 注意到 ControlPlatform 方法接受一个包含控制信息的数据包。

- 注意到私有辅助方法：

- SelectPlatform: 用于更改正在控制的平台。  
- DeselectPlatform: 用于更改正在控制的平台。

- 注意到私有成员变量：

- mCallbacks: 该类注册的回调函数列表。  
- mXIO_Ptr: 指向 XIO 接口的简单指针。  
- mControlledPlatformIndex: 当前由接收到的数据包控制的平台的索引。

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQQD.

40

![](images/c89deb977b5adb18b59f313f2275e6174541fe6a694e76169e5314ba3d1ca01d.jpg)

# XIO 练习1 - 检视2

# PlatformControlService.hpp

![](images/464e844aa1a49a1594e2c990becccd9133945ba795325e6ae372cd5d6a3a128e.jpg)

class PlatformControlService : public WsfSimulationExtension {

public: //! Constructor PlatformControlService(); //! Virtual destructor \~PlatformControlService() noexcept override $=$ default; //! Callback Function void ControlPlatform(PakPacket& aPacket); void Start(）override;   
private: void SelectPlatform(const WsfPlatform\* aPlatformPtr); void DeselectPlatform(const WsfPlatform\* aPlatformPtr); //! The callback holder to maintain list of subscriptions made by this class UtCallbackHolder mCallbacks; //! Maintain a pointer to the xio interface. //! This is guaranteed to be valid throughout the simulation. WsfXIO_Interface\* mxIO_Ptr; //! The platform we are currently controlling unsigned int mControlledPlatformIndex;   
};

- 在 PlatformControlService::Start 方法中：

- 任务 $2 \mathrm{a}$ : 使用 XIO 接口（即 mXIO_Ptr）注册新的数据包类型（FlightControlPkt），以便它被识别。调用 RegisterPacket 方法，参数如下:

- 第一个参数是字符串 "FlightControlPkt"。  
- 第二个参数是指向新的 FlightControlPkt 的指针。

- 任务2b: 订阅以便在接收到新的飞行控制数据包时获得通知。使用mXIO_Ptr->Connect，语法与WsfObserver订阅类似。需要的参数包括：

- 要订阅的数据包ID（FlightControlPkt::cPACKET_ID）。  
- 一个函数指针，用于处理该数据包（ControlPlatform）。  
this.

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQQD.

42

![](images/b3076fe762572151bfa945d649a0c0dca9547c132b4714d5445caac29c5f000f.jpg)

# XIO 练习1- 任务2 解决方案

# PlatformControlService.cpp

![](images/9fbed58f505e509680c275646e1acac17bebfd56c3a19b15dc30a3b50302aac6.jpg)

void PlatformControlService::Start()

{

mXIO_Ptr = WsfXIO_Extension::Find(GetSimulation());

// If the xio interface was not configured the pointer will be zero.  
if (mXIO_Ptr != nullptr)

}

```cpp
// EXERCISE 1 TASK 2a
// Register our new packet type
mXIO_Ptr->RegisterPacket("FlightControlPkt", new FlightControlPkt());
// EXERCISE 1 TASK 2b
// Subscribe to be notified when a new Flight Control packet is receive
mCallbacks += mXIO_Ptr->Connect(FlightControlPkt::cPACKET_ID,
&PlatformControlService::ControlPlatf
this); 
```

感兴趣的数据包的ID

用于处理该数据包的函数

将操作该数据包的实例

![](images/6c61a34e281d42539d233560a815f0eb723b97e5ecf6a207cfe4fd3e15f396b0.jpg)

- WsfStandardApplication 构造函数利用插件管理器查找并加载所有插件（包括训练文件夹中的插件，因为 CMake 选项 WSF_ADD Extensions_PATH 的原因）。对于找到的每个插件，执行 WsfPluginSetup（注意：这会导致我们的 XIO 练习插件的 WsfPluginSetup 函数被执行）。这会导致我们的 XIO 练习的 WsfDefaultApplicationExtension 被创建并注册到 app 中。

RegisterExtension 然后调用 WsfApplicationExtension::AddedToApplication()。

- 注意：WsfDefaultApplicationExtension并没有重写 AddedToApplication，因此这个通知实际上被忽略了。

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQQD.

44

![](images/e24163a56682b0b4ff9e397ea91ee5fdf8262f724f51ecbf88b0eadfb12cdf4f.jpg)

# UNCLASSIFIED AFSIM插件&扩展

# AFSIM mission 启动顺序

![](images/1d0802e61654a9659e50ddfd83e97f92234ac3ae87dc49d3b3b1adffa439037f.jpg)

![](images/d84e64f458faedd1b317d4ebd6bc5b1ada5b7ee7e2098ccd2532339d179645ca.jpg)

任务随后将所有必要的预定义扩展注册到 app 中。

![](images/113bd798acfda05ceb68eb82ac8270368088a702e6aacbb3898bc629decdc6ac.jpg)

Mission 随后创建了场景并调用 WsfScenario 构造函数: WsfScenario

scenario(app);

- 该构造函数调用 WsfApplication::ScenarioCreated 方法。接着，这会调用所有注册的应用程序扩展的 ScenarioCreated 方法（包括 WsfDefaultApplicationExtension::ScenarioCreated）。这进一步创建了 RegisterPlatformController 并将其注册到场景中。RegisterExtension 然后调用 RegisterPlatformController::AddedToScenario。  
- 注意：RegisterPlatformController 并没有重写 AddedToApplication，因此这个通知实际上被忽略了。

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

46

![](images/f7c79fedd1fe9c7c0b30a34334ab0ffabc3d6cc96c310c81abfcdf74b8cf201c.jpg)

# AFSIM插件&扩展

![](images/11d6fa8681c521c970b445eff5dd600378a769a98dd6e1e5fb3069bbb600d3e9.jpg)

![](images/b04580e4320c3065cd0cf581ec0a7bb3ec11fff179b41be1ff9786cf15fb6459.jpg)

任务调用app.WsfStandardApplication::ProcessInputFiles()，这会调用

WsfScenario::LoadFromFile()。对于输入中的每个命令：

- 调用每个核心类的ProcessInput()方法。  
- 调用每个注册的场景扩展的ProcessInput()方法。

RegisterPlatformController并没有重写ProcessInput，因此这个扩展不会处理任何新的命令。

![](images/aa5bc5dcc916bd747d5f0e6461a14ca65071daf6eb1f14ccf029f3cc981339b2.jpg)

任务调用 app.WsfStandardApplication::ProcessInputFiles(), 这会调用 WsfScenario::LoadFromFile(), 然后调用

WsfScenario::CompleteLoad()。接着，调用每个场景扩展的

Complete() 方法。最后，调用每个场景扩展的 Complete2() 方法。

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQQD.

48

![](images/bf97d62e542793af70fa1cefd98c834da357acf265b17f3ea7eba50379da0ea5.jpg)

# AFSIM插件&扩展

![](images/049e8def3797902f02390f06bad69529386b8c68398361d0f63da01bf173bbf6.jpg)

![](images/07dfbc2a8819871735820d14a56a4500739dc96fdecc6edda8b86289ca921507.jpg)

Mission 使用以下语句创建仿真:

std::unique_ptr<WsfSimulation> simPtr =

app.CreateSimulation(scenario, ...);

• CreateSimulation 调用 WsfSimulation 对象的构造函数（以场景作为参数）。

![](images/c7fb59e63087d284029d924b9656d666482460adeea9a845fdc5749b701b2618.jpg)

Mission使用以下语句创建仿真::

app.InitializeSimulation(simPtr.get())

- InitializeSimulation 调用: aSimPtr->Initialize()

(where aSimPtr $\equiv$ simPtr.get())

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQQD.

50

![](images/7fe7c3a2c1fc6743aefee25c99da780062ae9ff73fc5ecfad180ad3c3242fd0d.jpg)

# AFSIM插件&扩展

![](images/8fbe49a62446187bae8c0e658c2688e4b31fe3c2560519578ccb2581291de14f.jpg)

![](images/54dbea359423fb5ccc0e401f293d9984162dcf119dc45defe103a0b30f2c68a5.jpg)

Mission使用以下语句创建仿真:

app.InitializeSimulation(simPtr.get())

- InitializeSimulation 调用: aSimPtr->Initialize()   
- WsfSimulation::Initialize 调用: mScenario.SimulationCreated(*this)

(where mScenario $\equiv$ scenario and \*this $\equiv$ *simPtr.get()

![](images/8245d9b6c97a3ba9a8d151ad7c3eb37e36427cc11ba90fa12c6ec5e9838976e8.jpg)

Mission使用以下语句创建仿真:

app.InitializeSimulation(simPtr.get())

- InitializeSimulation 调用: aSimPtr->Initialize()   
- WsfSimulation::Initialize 调用: mScenario.SimulationCreated(*this)   
- SimulationCreated 调用: GetApplication().SimulationCreated(aSimulation)

(where GetApplication() ≡ app and aSimulation ≡ *simPtr.get())

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19.

Other requests for this document shall be referred to AFRL/RQQD.

52

![](images/bc83ab84d77f383a3d8d59906374effd07fefce8018eab7b54091dffd90b1156.jpg)

# UNCLASSIFIED

# AFSIM插件&扩展

![](images/40e1a98afa1f15aad35c8c0982627a483648c90615377234921e7ff6de06f365.jpg)

![](images/28413711ddfb7f26013b9a6789d4027a590284a3c78c77a8e34ed7b0f664ed10.jpg)

Mission使用以下语句创建仿真:

app.InitializeSimulation(simPtr.get())

- InitializeSimulation 调用: aSimPtr->Initialize()   
- WsfSimulation::Initialize 调用: mScenario.SimulationCreated(*this)   
- SimulationCreated 调用: GetApplication().SimulationCreated(aSimulation)

- 每个应用扩展调用 SimulationCreated(aSimulation)

(where aSimulation $\equiv^{*}\mathrm{simPtr.get()}$

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19.

Other requests for this document shall be referred to AFRL/RQQD.

![](images/ccd88da5f6cdc9e43de22e70545fb60481a6381c10d542df64bf2517df7c1b39.jpg)

Mission使用以下语句创建仿真:

app.InitializeSimulation(simPtr.get())

：

- SimulationCreated 调用: GetApplication().SimulationCreated(aSimulation)

- 每个应用扩展调用 SimulationCreated(aSimulation)  
- 这里调用 RegisterPlatformController::SimulationCreated(aSimulation)

(where aSimulation $\equiv^{*}\mathrm{simPtr.get()}$

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQQD.

54

![](images/e42c4277b463749a0be4e03218bf3b524e8895d8a80a9cea5ee4dcdcd0ffea05.jpg)

# UNCLASSIFIED

# AFSIM插件&扩展

![](images/d08dcdc731b1ed06d5bc9fccaa2d435704a624933005b4510264cd76069393ac.jpg)

![](images/ce438ceda6e122fffa802ef7e86466f998564f286838fa121ec410b0a4836bb0.jpg)

Mission使用以下语句创建仿真：

app.InitializeSimulation(simPtr.get())

：

- SimulationCreated 调用: GetApplication().SimulationCreated(aSimulation)

- 每个应用扩展调用 SimulationCreated(aSimulation)  
- 这里调用 RegisterPlatformController::SimulationCreated(aSimulation)  
- 这里调用 aSimulation.RegisterExtension(ut::make_unique<PlatformControlService>))  
- 最后，RegisterExtension调用PlatformControlService::AddedToApplication，该方法没有被重写，因此没有任何效果。

![](images/d582299793031db89a1fff08971b3a6692494c1a781bafbaf72251ac6332e251.jpg)

Mission使用以下语句创建仿真：

app.InitializeSimulation(simPtr.get())

- InitializeSimulation 调用: aSimPtr->Initialize()

中

- 下一步, WsfSimulation::Initialize 调用:

WsfObserver::SimulationInitializing(this)

- 这会通知所有注册的事件观察者，模拟即将被初始化。注意：PlatformControlService 类没有重写此方法，因此我们对该通知不做任何处理。

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19.

Other requests for this document shall be referred to AFRL/RQQD.

56

![](images/58094844030de3cc04c1025b6aafd075caed6e16d57ed0438abd7022ff03159d.jpg)  
UNCLASSIFIED

# AFSIM插件&扩展

![](images/3d965224bbf1079a604d2ab1830c044e24674f7c92926f6c7661d767365fbcdd.jpg)

![](images/ce19b66257516542544fe4ee9dd52a0a23b0e3496d6d88dc422e5a563417d3d3.jpg)

Mission 使用以下语句创建仿真:

app.InitializeSimulation(simPtr.get())

- InitializeSimulation 调用: aSimPtr->Initialize()

：

- 下一步, WsfSimulation::Initialize 调用: Initialize() 针对所有的扩展

- PlatformControlService并没有重写 Initialize，因此这对XIO没有任何影响。

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19.

Other requests for this document shall be referred to AFRL/RQQD.

![](images/829e4194aa500feba2d89dadec0e287412ed77c328a87df05a11a6174b6a55bc.jpg)

Mission使用以下语句创建仿真:

app.InitializeSimulation(simPtr.get())

- InitializeSimulation 调用: aSimPtr->Initialize()

：

- 下一步, WsfSimulation::Initialize 将所有可用平台添加到平台列表当中  
- 最终, WsfSimulation::Initialize 将仿真状态置为 cPENDING_START

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQQD.

58

![](images/46f33c0c5fbc5b91af22b7ed850b2ceacd67fb3368575a2c7a116d18c4fbffc3.jpg)

# UNCLASSIFIED

# AFSIM插件&扩展

![](images/331e49bfc09b697b2c5370bc7d1073d1d1d542a702854965e0826597f2682d5e.jpg)

![](images/e47059618b75c28d6f21ed9e84c2810c70d4c3f9fd7310256238db25988f3694.jpg)

Mission运行仿真使用以下语句:

app.runEventLoop(simPtr.get(), options)

- RunEventLoop 调用: aSimPtr->Start()

- WsfSimulation::Start

- 对于每个仿真扩展调用 Start()

调用PlatformControlService::Start()

- 设置XIO连接回调以处理传入的数据包

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

![](images/9231e7f09968e820b5ec989d613379bc749ef9ed908d00d1251b1ac5e8d05f53.jpg)

# Mission运行仿真使用以下语句:

appRUNEventLoop(simPtr.get(), options)

# - RunEventLoop 调用: aSimPtr->Start()

：

# - 循环直到仿真结束

- 执行：aSimPtr->AdvanceTime()

- 将时间推进到下一个事件时间，触发计划的模拟事件或下一个时间。

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19.

Other requests for this document shall be referred to AFRL/RQQD.

60

![](images/eab6bf7a8b4a8104a6143cc558dad1c980e334b415c425d31a7bf4337ebb07e3.jpg)

# UNCLASSIFIED

# 练习2

![](images/2cb7c39a1286f3046277f08f9e1d28ee52a738de0bafad0182329afd0b89ab8f.jpg)

# - 处理 FlightControlPkt 数据包:

- 理解平台的选择和取消选择，以及完成  
PlatformControlService::ControlPlatform。  
- 理解 PlatformControlService::Start 如何在模拟开始时为所有平台启用自动驾驶仪。  
- 理解 PlatformControlService::SelectPlatform。  
- 理解 PlatformControlService::DeselectPlatform。  
- 理解 PlatformControlService::ControlPlatform 以及它如何处理在 FlightControlPkt 中编码的按键。  
- 完成 PlatformControlService::ControlPlatform 的逻辑，以直接控制所选平台。

检查 PlatformControlService::Start 方法：

- 注意最后的 for 循环。

- 确保为所有平台的六自由度（6-dof）移动器启用自动驾驶仪。

```cpp
void PlatformControlService::Start()
{
    // Make sure the autopilot is initially turned on for all 6-dof movers
    for (unsigned i = 0; i < GetSimulation().GetPlatformCount(); ++i)
        {
            WsfPlatform* platformPtr = GetSimulation().GetPlatformEntry(i);
            WsfP6DOF_Mover* p6DofMoverPtr = dynamic_cast<Wsfp6DOF_Mover>(platformPtr->GetMover());
            if (p6DofMoverPtr != nullptr)
                {
                    p6DofMoverPtr->ReleaseDirectControlInput();
                    p6DofMoverPtr->EnableAutopilot(true);
            }
        }
} 
```

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQQD.

62

![](images/57312d06d3acd74fab9fb9d44dca18a665f33521ad83572d598c368c525f25bc.jpg)

UNCLASSIFIED XIO练习2-任务1

PlatformControlService.cpp

![](images/3eafd324d7c68997c2267e28cb4ab97bb24287e99828549993b4084c30ab9708.jpg)

- 在 PlatformControlService::ControlPlatform 方法中：

- 执行 ID 检查以验证数据包的 ID 是否与 PlatformControlPkt 数据包的 ID 相对应（即 FlightControlPkt::cPACKET_ID）。

```rust
//! Method called by XIO to control the platform based on received packet values
//! @param aPacket The packet received by XIO and passed to this method.  
void PlatformControlService::ControlPlatform(PakPacket& aPacket)  
{ // EXERCISE 2 TASK 1 // Perform a check to verify that the aPacket's ID corresponds to that of the FlightControlPkt::cPACKET_ID  
if (aPacket.ID() == FlightControlPkt::cPACKET_ID) { ... } } 
```

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQQD.

64

![](images/b6cef397c8a8041fd84f019a5ce316e1133aa0b4adc23786a925f1e3fa4cb998.jpg)

# UNCLASSIFIED XIO 练习2-检视2

# PlatformControlService.cpp

![](images/425447574c54e74c90a6407486a3c2c34b8249d6355191cb4c62808d62027bf6.jpg)

- 在 PlatformControlService::ControlPlatform 方法中：

理解平台取消选择逻辑：

- 当 flightControlPacket 中的平台索引为 10（无效的平台索引）时，将执行此逻辑。

/// Method called by XIO to control the platform based on received packet values

//! @param aPacket The packet received by XIO and passed to this method.

void PlatformControlService::ControlPlatform(PakPacket& aPacket)

1

// EXERCISE 2 TASK 1

// Perform a check to verify that the aPacket's ID corresponds to that of the

FlightControlPkt::cPACKET_ID

if (aPacket.ID() == FlightControlPkt::cPACKET_ID)

FlightControlPkt flightControlPacket $=$ static cast<FlightControlPkt&>(aPacket); if (flightControlPacket.mPlatformIndex $\equiv$ cINVALIDPLATFORM_INDEX) { WsfPlatform\* currentPlatformPtr $=$ GetSimulation().GetPlatformByIndex(mControlledPlatformIndex); if(currentPlatformPtr != nullptr) { DeselectPlatform(currentPlatformPtr); } mControlledPlatformIndex $= 0$ ·

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19.

Other requests for this document shall be referred to AFRL/RQQD.

- 在 PlatformControlService::ControlPlatform 方法中：

理解平台取消选择/选择逻辑。：

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.   
$\vdots$ else if (flightControlPacket.mPlatformIndex != mControlledPlatformIndex) { WsfPlatform* currentPlatformPtr = GetSimulation().GetPlatformByIndex(mControlledPlatformIndex); if (currentPlatformPtr != nullptr) { DeselectPlatform(currentPlatformPtr); } mControlledPlatformIndex = flightControlPacket.mPlatformIndex; currentPlatformPtr = GetSimulation().GetPlatformByIndex( mControlledPlatformIndex); if (currentPlatformPtr != nullptr) { SelectPlatform(currentPlatformPtr); } else { auto out $=$ ut::log::warning() $\ll$ "Could not find platform."; out.AddNote() $\ll$ "Index:" $\ll$ flightControlPacket.mPlatformIndex; } }

66

![](images/8a7dd77f268d5037633d245b3e101536d820843f503bae469c51cd1e374e753f.jpg)

# UNCLASSIFIED

# XIO 练习2- 任务2

![](images/9d145d9c0ddd9948d2c0771cb9584610b47b996a738b1ccda058bd9535842d97.jpg)

- 在 PlatformControlService::ControlPlatform 方法中：

- 使用 Simulation 对象获取当前选定的平台。  
- 调用GetSimulation().GetPlatformByIndex()并传入平台索引（存储在mControlledPlatformIndex中）。  
- 将返回的 WsfPlatform 指针存储在一个变量中。  
- 检查包含 WsfPlatform 指针的变量是否不是 nullptr（即 GetPlatformByIndex 找到了平台）。  
- 如果是 nullptr，则表示未找到平台（即它不存在），因此不执行后续任务的任何部分。  
- 获取当前选定平台的移动器并将其转换为 WsfP6DOF_Mover 类型。  
- 使用 WsfPlatform 指针调用 GetMover。  
- 将返回的移动器动态转换为 WsfP6DOF_Mover。  
- 将转换后的指针存储在类型为 WsfP6DOF_Mover * 的变量中。  
- 调用P6dof移动器的SetDirectControlInputs方法，并使用来自飞行控制数据包的值进行参数化：

翻滚速率 (FlightControlPacket.mRollRate),

俯仰速率 (FlightControlPacket.mPitchRate),   
- 偏航速率 (FlightControlPacket.mYawRate)，以及  
油门（FlightControlPacket.mThrottle）。

- 注意：此方法提供控制 P6dof 移动器的归一化输入。

生成ut::log::info()输出，指示接收到飞行控制数据包。  
- 输出数据包中编码的偏航、俯仰、翻滚和油门值。

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQQD.   
```cpp
if (mControlledPlatformIndex != cNOPLATFORM_SELECTED)  
{ // EXERCISE 2 TASK 2 // Use the simulation object to get the currently selected platform // Get the platform's mover and cast it to a WsfP6DOF_Mover // Set the control inputs using values from the flight control packet // Generate ut::log::info() output indicating a packet was received, and its yaw, // pitch, roll, and throttle values  
WsfPlatform* currentPlatformPtr = GetSimulation().GetPlatformByIndex(mControlledPlatformIndex); if (currentPlatformPtr != nullptr) { WsfP6DOF_Mover* p6DofMoverPtr = dynamic_cast<WsfP6DOF_Mover>(currentPlatformPtr->GetMover()); if (p6DofMoverPtr != nullptr) { p6DofMoverPtr->SetDirectControlInputs(flightControlPacket.mRollRate, flightControlPacket.mPitchRate, flightControlPacket.mYawRate, flightControlPacket.mThrottle); auto out = ut::log::info() << "Received flight control packet."; out.AddNote() << "Yaw: " << flightControlPacket.mYawRate; out.AddNote() << "Pitch: " << flightControlPacket.mPitchRate; out.AddNote() << "Roll: " << flightControlPacket.mRollRate; out.AddNote() << "Throttle: " << flightControlPacket.mThrottle; } } 
```

68

![](images/39ba22a5b98ba0c5f673ec2c3d128e57193e3b57e4c5aa0706af915f41231713.jpg)

# UNCLASSIFIED

# XIO 练习2-检视3

# PlatformControlService.cpp

![](images/74be8b3fe42754ba49253883541323eeea389fad39c0f48777eb9c9874e544d3.jpg)

- 检查 PlatformControlService::SelectPlatform:

- 注意选择一个平台进行控制的逻辑。  
- 注意在此平台上自动驾驶仪被关闭。

```cpp
// private
void PlatformControlService::SelectPlatform(const WsfPlatform * aPlatformPtr)
{
    WsfP6DOF_Mover* p6DofMoverPtr = dynamic_cast<WsfP6DOF_Mover>(aPlatformPtr->GetMover());
    if (p6DofMoverPtr != nullptr)
    {
        // RAIII block
        auto out = ut::log::info() << "Selecting platform."; 
        out.AddNote() << "Platform: " << aPlatformPtr->GetName();
    }
    p6DofMoverPtr->EnableControls(true);
    p6DofMoverPtr->EnableAutopilot(false);
    p6DofMoverPtr->TakeDirectControlInput();
} else
{
    mControlledPlatformIndex = cNOPLATFORMSELECTED;
} 
```

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19.

Other requests for this document shall be referred to AFRL/RQQD.

# - 检查 PlatformControlService::DeselectPlatform:

- 注意取消选择一个平台进行控制的逻辑。  
- 注意在此平台上自动驾驶仪被启用。

```cpp
// private
void PlatformControlService::DeselectPlatform(const WsfPlatform * aPlatformPtr) {
    // RAII block
        auto out = ut::log::info() << "Deselecting platform."; 
        out.AddNote() << "Platform: " << aPlatformPtr->GetName();
    }
    WsfP6DOF_Mover* p6DofMoverPtr = dynamic_cast<WsfP6DOF_Mover>(aPlatformPtr->GetMover());
    if (p6DofMoverPtr != nullptr)
        {
            p6DofMoverPtr->EnableControls(false);
            p6DofMoverPtr->EnableAutopilot(true);
        }
} 
```

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQQD.

70

![](images/6866e5a50190ca87170ae66ff63cf2496384ec50c3470ace5b9ebad3888e49ae.jpg)

# UNCLASSIFIED

# 练习3

![](images/112122f669fcfd6da591c84127350919c9072606711c3335138178d0021bcf67.jpg)

- 理解 FlightController 应用程序：

- 审查FlightController.cpp中的主函数。  
理解FlightControllerWidget类。  
- 理解 FlightControllerPlatformListRequest 类和 WsfXIO_PacketRegistry 类。  
- 理解在 FlightControllerPlatformListRequest 类中添加和移除平台的逻辑。  
- 实现 FlightControllerPlatformListRequest::HandlePlatformList 以处理新平台。

- 处理按键并生成 FlightControlPkt 数据包以发送到 AFSIM。

- 理解按键如何通过FlightControllerInterface::Update和FlightControllerInterface::UpdateInput进行处理。  
实现FlightControllerInterface::Initialize。  
- 理解FlightControllerInterface::ProcessInput在FlightController应用程序中的使用。  
注册FlightControlPkt并注册平台列表更新。

- 检查文件 FlightController.cpp:

- 注意这并不是一个真正的AFSIM应用程序；它只是使用XIO来发送和接收与FlightControllerInterface的数据。

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQQD.

72

![](images/a1a2db86e3c66b13e5bfcb0c7bf133c7e097f8fd3dd7d27d3d7f4acab7609ddb.jpg)

UNCLASSIFIED XIO练习3-检视1 FlightController.cpp 飞行控制器应用程序的主函数

![](images/5ca7dccda1dfb4dc5c289fb4ef21c4587bc2d3e557d65d2d05a1b2c743487567.jpg)

int main(int argc, char* argv[]) QApplication app argc, argv); auto fci $=$ ut::make_unique<FlightControllerInterface $\rangle$ auto mainWindow $=$ ut::make_unique<FlightControllerWidget>(fci.get()); mainWindow->show(); if (argc != 2) { // RAI block auto out $=$ ut::log::fatal()<< "Invalid arguments."; out.AddNote()<< "Usage: flight_controller <config-file>"; } exit(0); } std::string inputFile $=$ argv[1]; if (fci->Initialize(inputFile)) { UtWallClock clock; clock ResetClock(); // The following in the main loop could also be threaded. while (true) { QCoreApplication::processEvents(); fci->Update(clock.GetClock()); UtSleep::Sleep(0.01); // execute approximately 100 times a second } return app.exec();

检查 FlightController.cpp:

注意主函数。

将应用程序与AFSIM分开。

注意创建

FlightControllerInterface。

该接口完成大部分工作。

注意创建

FlightControllerWidget.

显示主窗口。

注意调用 Initialize。

调用ProcessInput以读取飞行控制器的数据文件。

注意while循环：

processEvents。

Update更新模拟时间并处理按键。

contractors, 9-Aug-19.  
编.1/100秒执行一次循环体。73

class FlightControllerWidget : public QMainWindow   
{ Q_OBJECT   
public: FlightControllerWidget(FlightControllerInterface* aInterface); ~FlightControllerWidget() override $=$ default; void keyPressEvent(QKeyEvent\* aEvent) override; void keyReleaseEvent(QKeyEvent\* aEvent) override; void showPopup();   
private: FlightControllerInterface\* mInterface; Ui::FlightControllerMainWindow mUI;   
}；

- 检查 FlightControllerWidget.hpp:

- 注意该类继承自 QMainWindow。  
- 这是一个与AFSIM分开的独立应用程序。  
- 注意成员 mInterface 是一个 FlightControllerInterface。  
- 注意成员 mUI 是用户界面的主窗口。

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQQD.

74

![](images/4d117df60ef416265e151d8d9c61709dfb6b2a3970342102983b76279d9e920d.jpg)

# UNCLASSIFIED

# XIO 练习3-检视2

# FlightControllerWidget.cpp

![](images/572f9aebecf4bb90a364dfac0a134580203520e3d72cad0367680618dc0fb135.jpg)

```cpp
FlightControllerWidget::FlightControllerWidget(FlightControllerInterface* aInterface)  
{  
    mUI_setupUi(this);  
    mInterface = aInterface;  
}  
void FlightControllerWidget::keyPressEvent(QKeyEvent* aEvent)  
{  
    int key = 0;  
    if (aEvent->type() == QKeyEvent::KeyPress)  
    {  
        key = aEvent->key();  
        mInterface->HandleKeyPress(true, key);  
    }  
}  
void FlightControllerWidget::keyReleaseEvent(QKeyEvent* aEvent)  
{  
    if (aEvent->type() == QKeyEvent::KeyRelease)  
    {  
        }  
} 
```

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

- 检查 FlightControllerPlatformListRequest:

- 注意它继承自 WsfXIO_PlatformListRequest。  
- XIO 实现调用虚拟方法 HandlePlatformList（在此处被重写）来处理 WsfXIO_PrtformListUpdatePkt 数据包，以提供：

- 平台列表信息  
- 平台的添加和删除

- 我们在这个派生类中实现 HandlePlatformList 方法。  
- 在我们的情况下，将存储数据以供控制器使用。

//! Requests for an application to send its platform list information.   
class FlightControllerPlatformListRequest : public WsfXIO_PplatfromListRequest   
public: explicit FlightControllerPlatformListRequest(WsfXIO_Connection\* aConnectionPtr); \~FlightControllerPlatformListRequest(） noexcept override $=$ default; void HandlePlatformList(WsfXIO_PplatfromListUpdatePkt& aPkt) override;   
private: static Platforms sPlatforms;

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

76

![](images/0c59c38ce56dc63ad246f7605461723da13905f8f6e8500093746d38e40d1dbb.jpg)

# UNCLASSIFIED

# XIO练习3-检视4

# WsfXIO_PacketRegistry.hpp

![](images/d8716e74d17a568c489daea280efd902b595e6309879017046144f45b5f4f2ef.jpg)

- 在 WsfXIO_PacketRegistry.hpp（WSF 框架）中，检查

WsfXIO_PlatformListUpdatePkt::PlatformData 数据结构：

- 该数据包将平台列表数据存储为 PlatformData 结构的向量。

```typescript
class WsFExport WsfXIO_PlatformListUpdatePkt : public WsfXIO_Packet { 
```

```cpp
public: XIO DEFINE_PACKET(WsfXIOPLATFORMListUpdatePkt, WsfXIO_Packet, 6) { aBuff& mPlatformsAdded& mPlatformsDeleted; } 
```

```c
struct WSFExport PlatformData
{
    template <typename T>
    void SZerize(T& aBuff)
    {
        aBuff& mName& mSide& mIndex& mIcon& mEntityId& mIsExternallyControlled;
    }
} WsfstringId mName;
int mIndex;
WsfstringId mSide;
WsfstringId mIcon;
WsfXIO_EntityId mEntityId;
bool mIsExternallyControlled;
}; 
```

注意：此处使用的&运算符调用了重载的operator&，该运算符将数据序列化为可以放入数据包中的格式。

```cpp
std::vector<PlatformData> mPlatformsAdded; std::vector<int32_t> mPlatformsDeleted; 
```

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

- 在 FlightControllerPlatformListRequest::HandlePlatformList 中：

- 每当添加一个平台时，打印一条包含平台名称和索引的消息。

- 参数 aPkt 有一个名为 mPlatformAdded 的成员，它是一个待添加到可选择/可控制平台列表中的平台列表。  
- 参数 aPkt 还有一个名为 mPlatformDeleted 的成员，它是一个待从可选择/可控制平台列表中移除的平台列表（请参见您正在编写的代码段下方）。  
- 您应该遍历 mPlatformAdded 中的平台列表，并打印到 ut::log::info() 流中：平台名称（平台的 Name 成员）和其索引（平台的 mlndex 成员）。

- FlightControllerPlatformListRequest 类有一个静态成员变量，名为 sPlatforms，它是一个当前被跟踪且可能可控的所有平台的列表。

- 实现代码，将数据从数据包的 mPlatformsAdded 复制到静态类变量 sPlatforms。  
- 您可以使用与打印消息相同的平台迭代器来将该平台添加到 sPlatforms。

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQQD.

![](images/1b02012d9d91dcd0d57690b841075b5adfa0735f91a7c1756769486099b9d8e7.jpg)

# XIO练习3-任务1解决方案

# FlightControllerPlatformListRequest.cpp

![](images/2dc9ef324280ea7fbe182fdcf55df17fb28be8a9f610ca5e941276242a9f4df3.jpg)

void FlightControllerPlatformListRequest::HandlePlatformList(WsfXIOPLATFORMListUpdatePkt& aPkt)

```txt
{ //EXERCISE3TASK1 //Addnewplatforminformation //IterateoveraPkt.mPlatformsAddedusingaPlatforms::iterator //Copy Platform structures from mPlatformsAdded to the Static Class Variable,sPlatforms 
```

```txt
for (const auto& added : aPkt.mPlatformsAdded) { auto out = ut::log::info() << "Platform Added. "; out.AddNote() << "Index: " << added.mIndex; out.AddNote() << "Name: " << added.mName; sPlatforms.push_back(added); } 
```

```txt
：
```

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

void FlightControllerPlatformListRequest::HandlePlatformList(WsfXIOPLATFORMListUpdatePkt& aPkt)

{

// Remove information if a platform is removed   
for (auto deleted : aPkt.mPlatformsDeleted)   
{ { // RAII block auto out $=$ ut::log::info() $\ll$ "Platform deleted."; out.AddNote() $\ll$ "Index:" $\ll$ deleted; } Platforms::iterator platformsIter $=$ sPlatforms.begin(); while (platformsIter != sPlatforms.end()) { if (platformsIter->mIndex $= =$ deleted) { platformsIter $=$ sPlatforms. erase平台上; break; 1 else { ++platformsIter; } }

在 HandlePlatformList 中

- 注意代码，它从 platforms 中移除 platformsDeleted 中的那些平台

}

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQQD.

80

![](images/dab69ac9949bb8cd7f63565c740c6ace86e713662df12ac9fba84fc9360b8d0d.jpg)

# UNCLASSIFIED

# XIO 练习3-检视6

FlightControllerInterface.cpp

![](images/fcba384e5dc0dd88a71794ef61eb1f19824e4ff4d351b7b2e490fe21d9555cf6.jpg)

```cpp
AdvanceTime 定期接受新的 XIO 连接，并处理任何待处理的 XIO 数据包  
//! Read input from the keyboard and send a packet if needed.  
void FlightControllerInterface::Update(double aSimTime) 每秒打印一次消息...  
{ mXIO_InterfacePtr->AdvanceTime(aSimTime); // Issue a message once per second. if (((int)(aSimTime * 100.0) % 100 == 0) { auto out = ut::log::info() << "Update:"; out.AddNote() << "T=" << aSimTime; out.AddNote() << " XIO: " << mXIO_InterfacePtr->GetSimTime(); } HandleKeyPress(false, 0); }  
}  
void FlightControllerInterface::HandleKeyPress(bool aKeyPress, int aKey) { bool hasNewInput = UpdateInput(aKeyPress, aKey); if (hasNewInput && (mSelectedPlatformIndex != 0)) { : // Send a packet FlightControlPkt pkt; // Construct pkt based on keyboard input : // mXIO_InterfacePtr->SendToAll(pk); } DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQDD. 
```

```rust
//! Reads input from the keyboard and updates class attributes. bool FlightControllerInterface::UpdateInput(bool aKeyPress, int aKeyStroke) { if(aKeyPress) { mIgnoreNumber = 0; if((aKeyStroke != 0) && (aKeyStroke != -32)) { if((aKeyStroke == Qt::Key_Up) || (aKeyStroke == Qt::Key_W)) { mDirection = cUP; } else if((aKeyStroke == Qt::Key_Down) || (aKeyStroke == Qt::Key_S)) { mDirection = cDOWN; } else if((aKeyStroke == Qt::Key_Left) || (aKeyStroke == Qt::Key_A)) { mDirection = cLEFT; } else if((aKeyStroke == Qt::Key_Right) || (aKeyStroke == Qt::Key_D)) { mDirection = cRIGHT; } 
```

根据方向键被按下的情况设置mDirection

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQQD.

82

![](images/7c1fbaef25156ab96e89c3d45248183705027e31eda06f245c2280e86ad619b2.jpg)

# UNCLASSIFIED XIO练习3-检视7

# FlightControllerInterface.cpp

![](images/eab8c29c42e4a72b5ef73a386424abf5d05fb11310fcabd8f32067301251e62a.jpg)

$\vdots$ else if((aKeyStroke $= =$ Qt::Key_PageUp) || (aKeyStroke $= =$ Qt::Key BracketRight)) { mThrottle $+ =$ mThrottleIncrement; const static double cMAX_THROTTLE $= 2.0$ // including afterburner effect if(mThrottle $\rightharpoondown$ cMAX_THROTTLE) { mThrottle $=$ cMAX_THROTTLE; } ut::log::info() $\ll$ "Throttle increased to" $\ll$ mThrottle; } else if((aKeyStroke $= =$ Qt::Key_PageDown)||(aKeyStroke $= =$ Qt::Key BracketLeft)) { mThrottle $\rightharpoonup$ mThrottleIncrement; if(mThrottle<0.0) { mThrottle $= 0.0$ 1 } ut::log::info() $\ll$ "Throttle reduced to" $\ll$ mThrottle; }

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

```txt
else if ((aKeyStroke >= Qt::Key_1) && (aKeyStroke <= Qt::Key_9)) { mSelectedPlatformIndex = aKeyStroke - Qt::Key_1 + 1; const FlightControllerPlatformListRequest::Platforms& platforms = FlightControllerPlatformListRequest::GetPlatforms(); bool found = false; for (unsigned i = 0; i < platforms.size(); ++i) { if (platforms[i].mIndex == mSelectedPlatformIndex) { mSelectedPlatform = i; found = true; auto out = ut::log::info() << "Selected platform."; out.AddNote() << "Index: " << platforms[mSelectedPlatform].mIndex; out.AddNote() << "Name: " << platforms[mSelectedPlatform].mName.GetString(); break; } } if (!found) { auto out = ut::log::warning() << "Selected platform does not exist."; out.AddNote() << "Platform Index: " << mSelectedPlatformIndex; mSelectedPlatformIndex = cNOPLATFORM_SELECTED; } } 
```

```txt
DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQQD. 
```

84

![](images/5b2d066f0d4da4712ab3a6a31c5deac383449e5077329b31cfe522daae18e3f4.jpg)

# UNCLASSIFIED XIO练习3-检视7

# FlightControllerInterface.cpp

![](images/cda77c9fb482d6989dd82d1cabc2b7e011caaefb2b56ce48036c100a3a2461a6.jpg)

```cpp
{
    else if (aKeyStroke == Qt::Key_Backspace)
        {
            mSelectedPlatformIndex = cINVALIDPLATFORM_INDEX;
            mSelectedPlatform = cNOPLATFORM Selected;
            auto out = ut::log::info() << "All Platforms Deselected."; 
        }
    else
        {
            ut::log::info() << "Key pressed: " << aKeyStroke; 
        }
    }
} else
{
    ++mIgnoreNumber;
    if (mIgnoreNumber == mDebounce)
        {
            mDirection = cCENTER;
        }
    else
        {
            mDirection = cNONE;
        }
} bool haveNew = (mLastDirection != mDirection);
    mLastDirection = mDirection;
    return haveNew;
} 
```

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

- 在 FlightControllerInterface 的 Initialize 方法中, 通过将 mXIO_InterfacePtr 设置为指向 WsfXIO_Interface 新实例的 unique_ptr 来创建 WsfXIO_Interface 对象。  
- 使用mXIO_InterfacePtr，调用SetApplicationName方法将应用程序的名称设置为“flight_controller”。  
• 注意：我们是在一个独立的应用程序中创建 XIO 接口，而不是在 AFSIM 模拟中。

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQQD.

86

![](images/93c53e55fa9018b57601e92a025c99d43fcfa652ee481cae903294e7f4fba12d.jpg)

UNCLASSIFIED练习3-任务2解决方案FlightControllerInterface.cpp

![](images/72ec4133852c0042c7b2e5fc2725a3ed0d488c6b0f07d31faa08287dae3faf67.jpg)

bool FlightControllerInterface::Initialize(const std::string& aFileName)  
{ bool ok = true;

// EXERCISE 3 TASK 2  
// Create the XIO Interface and set its application name.  
mXIO_InterfacePtr = ut::make_unique<WsfXIO_Interface>();  
mXIO_InterfacePtr->SetApplicationName("flight_controller");

··

- 查看 FlightControllerInterface::ProcessInput 方法。

- 注意该方法处理的输入命令。

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQQD.

![](images/1e0747c221f9d8d01df8050bdf0eb878968ee3662aae531b30781fda5d14b001.jpg)

# UNCLASSIFIED XIO 练习3-检视8

# FlightControllerInterface.cpp

![](images/491fcdc5fe5a1a579e6de824e2835952fac56d68d6bffc28ff00f82db0c201e0.jpg)

bool FlightControllerInterface::ProcessInput(UtInput& aInput)   
{ bool myCommand $\equiv$ true; std::string command; aInput.GetCommand(command); if (command $= =$ "pitch_rate_increment") { aInput.ReadValue(mPitchRateIncrement); aInput.ValueInClosedRange(mPitchRateIncrement,0.0,1.0); } else if (command $= =$ "yaw_rate_increment") { aInput.ReadValue(mYawRateIncrement); aInput.ValueInClosedRange(mYawRateIncrement,0.0,1.0); } else if (command $= =$ "roll_rate_increment") { aInput.ReadValue(mRollRateIncrement); aInput.ValueInClosedRange(mRollRateIncrement,0.0,1.0); } else if (command $= =$ "throttle_increment") { aInput.ReadValue(mThrottleIncrement); aInput.ValueInClosedRange(mThrottleIncrement,0.0,1.0); }

这个ProcessInput方法与我们见过的大多数方法不同。由于FlightController是一个独立的应用程序，ProcessInput并不是在加载场景时从AFSIM的ProcessInput调用链中调用的。相反，这个ProcessInput方法是在FlightControllerInterface::Initialize中被调用的，当应用程序正在设置以处理按键输入时。

```cpp
bool FlightControllerInterface::ProcessInput(UtInput& aInput)  
{ bool myCommand = true; std::string command; aInput.GetCommand commanded); 
```

```txt
else if (command == "debounce")  
{  
    aInput.ReadValue(mIgnoreNumber);  
}  
else if (command == "debug")  
{  
    mDebug = true;  
}  
else  
{  
    myCommand = false;  
}  
return myCommand; 
```

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQQD.

90

![](images/9072883e0a3062c59a10f1bc346aeb34fcc47245f572b04de2ea809491533e08.jpg)

UNCLASSIFIED XIO 练习3- 任务3

FlightControllerInterface.cpp

![](images/43fd5547a1addf97318bfd6e566914254d639afee13a860dca6d08c5002eb609.jpg)

- 了解在 FlightControllerInterface::Initialize 中使用 UtlInputFile 和 UtlInput 对象。

```txt
try { UtInput input; input.PushInput(new UtInputFile(aFileName)); std::string command; 
```

- 实现读取 FlightController 输入：

- 调用 FlightControllerInterface::ProcessInput。  
如果 FlightControllerInterface::ProcessInput 返回 false，则调用 mXIO_InterfacePtr->ProcessInput。  
- 如果前两个ProcessInput调用都返回false，则FlightControllerInterface::Initialize无法处理输入，因此抛出UtInput::UnknownCommand异常。

```cpp
try { UtInput input; input.PushInput(new UtInputFile(aFileName)); std::string command; while (input.TryReadCommand commanded) { // EXERCISE 3 TASK 3 // Call ProcessInput and throw Ut::UnknownCommand exception if neither // FlightControllerInterface::ProcessInput nor WsfXIO_Interface::Process // can process it if (ProcessInput(input)) { } else if (mXIO_InterfacePtr->ProcessInput(input)) { } else { throw UtInput::UnknownCommand(input); } } 
```

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQQD.

92

![](images/78771a908358d3da5e16535a98758b94a08dd7aea94a852751a5072d086d7e46.jpg)

# UNCLASSIFIED XIO练习3-任务4 FlightControllerInterface.cpp

![](images/ee20cb93d55effcd059918aeeae5c2c4c8ad0798cd4c22c1cbc6682a7ba5eb08.jpg)

- 任务4a：在FlightControllerInterface::Initialize中使用XIO接口注册这个新数据包类型，以便它被识别。

- 调用mXIO_InterfacePtr->RegisterPacket。  
- 数据包应命名为 FlightControlPkt，因此第一个参数应为字符串"FlightControlPkt"。  
- 第二个参数应为指向新 FlightControlPkt 的指针。

- 任务4b：使用XIO接口的请求管理器注册平台列表更新。

- 调用GetRequestManager从mXIO_InterfacePtr指针获取请求管理器。  
- 在从上一个调用返回的请求管理器上调用 AddRequest，参数为指向新 FlightControllerPlatformListRequest 的指针，其中构造函数的参数为 mXIO_InterfacePtr->GetConnections().[0]。

```txt
if (ok) { 
```

```cpp
// EXERCISE 3 TASK 4a
// Use the XIO Interface to Register this New Packet Type
// The packet should be called "FlightControlPkt"
mXIO_InterfacePtr->RegisterPacket("FlightControlPkt", new FlightControlPkt());
// EXERCISE 3 TASK 4b
// Use the XIO Interface's RequestManager to Register for Platform List Updates
// Get the RequestManager from the XIO_Interface
// Call AddRequest with an argument of a FlightControllerPlatformListRequest*
mXIO_InterfacePtr->GetRequestManager().AddRequest(
    new FlightControllerPlatformListRequest(mXIO_InterfacePtr->GetConnections()[0]); 
```

#

return ok;

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQQD.

94

![](images/706f5fe50a822124d7d0d6e564e57a8a03fd626ce8bad5fdb03eacbe49e45588.jpg)

# UNCLASSIFIED

# XIO 想定

![](images/fd78418d9dc7b570280b902c5447b6f10aadc4a374aba5ce1fd96f1f3f0ad99e.jpg)

- 从 Visual Studio 中：

- 在“Release”模式下构建整个解决方案。  
- 构建“INSTALL”项目。  
- 找到名为\inwork\xio\data的文件夹。

Linux: 在构建目录, 运行:

$ cmake --build . --target all -- -j11
$ cmake --build . --target install -- -j11

- 在这个场景中，有四架（非常概念化的）飞机正在飞行：.

```diff
- 1 Blue_Fighter_1  
- 1 Blue_Fighter_2  
- 1 Blue_Fighter_3  
- 1 Blue_Fighter_4 
```

- 演示使用XIO控制其中一架或多架飞机的能力。  
- WsfP6DOF_Mover 被用作这些飞机的移动器，直到我们接管控制。  
- 我们将使用 Warlock 作为我们的模拟执行器。

- 运行 run_all.bat 文件。这将启动控制器，加载 flight_controller_config.txt 输入文件，同时也会运行 Warlock，加载 xioscenario.txt 文件。控制器插件应被自动识别并加载。确保在 Warlock 打开时启动模拟。  
- 在Warlock中连接到Blue_Fighter_1:

- 点击Blue_Fighter_1图标进行选择。  
- 按 $\mathrm{ctrl + shift + T}$ 进行连接。  
- 使用鼠标和滚轮以最佳视角查看飞机。

- 也可以在 Warlock 中连接到其他飞机，并使用飞行选择它们。

![](images/16539957dd31d61365bb35ccf9d7bc4b9875c8a2a1320031cc660e4e4701d9ef.jpg)

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

96

![](images/ad9be3ddf567b1c8985f75b5d22ea69801abb67f614802e65e0e3e6551be5850.jpg)

# UNCLASSIFIED

# 测试

![](images/79786325e20f46a687094f958655675983d3ebf01131d8f3ad346aab364c7853.jpg)

- 我们将测试飞行控制器和XIO连接。通过点击飞行控制器应用程序来使其获得焦点。  
- 以下键盘命令控制飞机：

- 数字1-9：选择要控制的平台  
- 退格键：取消选择所有平台  
箭头键或<WASD>：平台的俯仰、滚转和速率变化  
Page-Up/Page-Down或“[”/“]”：增加/减少平台速度

![](images/3b4e62db3d1afbcbb9f3f5a631fddadba8b4793a301d910f0e2ebc14acc59d74.jpg)

![](images/bd3819fbfc7e2d0f7e453dc9f93e0d4491ad9bccd4e5a2b7f17b91e5460f14fa.jpg)

![](images/9922c75c4b307cb20b10e25b74ca96f53dd9e5f3832329ffa9fbbf04c1b9fb95.jpg)

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

![](images/0b30c10af242a1f6b8d4421fe13c0a0377d4ad4f52e9d0de278183cb0130762b.jpg)

在Warlock和飞行控制器启动后，Warlock必须通知飞行控制器四个平台的存在。

![](images/01e261b0dd5f7722e1cde5253a0897818d8605c6cc4c18a4ec7473509330e0bf.jpg)

![](images/873b39ccaba93a43a327e4550b90538234d4046ea1563a18c1f3fcb2e40190d9.jpg)

![](images/be468855e089cf58ec885f9beadbf47895379aa44813461354ed7f40672fb0bd.jpg)

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

98

![](images/c935b74c2bdb23a52ca1fa71873d1abfa21e1ab354216063ef15e2e2c1a6f1fa.jpg)

# 控制Blue_Fighter_1的示例

![](images/ff8fea1c2d72c28123d4850c19f931c83d631a798c258e53e0f2087767ddd7d4.jpg)

现在，飞行控制器应用程序知道这四个平台的存在。

![](images/7d21b5a77e45d1f51308b5882e4aeb99fe374bd9d28c5a36ab73691f9d3232c3.jpg)

![](images/0c5ab754492a173c075e044839ffb3265ebd49997094abedefedd1c25a0a1164.jpg)

![](images/7e5d2684a084457c03510f410031424ef12de3cf8352efe34d33be469bd3baec.jpg)

![](images/8870a2702ced56d9ff1f3ce399f8617a6544ef62a0b0c1ac972449d147575c03.jpg)

![](images/64862566b15350430aa266aa7ed65f92086534911741272484e57de4ada4b696.jpg)

![](images/8a95f0a031c6aa63f3c6dfbc51a689424c9b8cc22b154f32701447abf65aacde.jpg)

![](images/ddadd79e7d41609969cd58e384bbb15a91f7b9ab77baafaf8e1665762fe019d7.jpg)

XIO Connection

# AFSIM Warlock with XIO exercise extensions

Blue_Fighter_1 Platform p6DofMover

Blue_Fighter_2 Platform p6DofMover

Blue_Fighter_3 Platform p6DofMover

Blue_Fighter_4 Platform p6DofMover

PlatformControlService

PlatformListUpdatePkt

![](images/34f0e2d9094175859cc1e98e549cc873b666603d25f046072e19f86ae9a1eae4.jpg)

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

![](images/1b974aa3efa2f2ad7149b100797f47f9f82e31f7c28805af16c7bca2a05bfc8f.jpg)  
DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQQD.

100

![](images/7969f3dd649cd05cf4598f899896cce7fbe8bbbe92c60436e72a5edeeccaeb1c.jpg)  
UNCLASSIFIED

# Blue_Fighter_1 控制

![](images/5469b1f23fc19ae784f7758c1bc9d2ae1a93914dcc54f69f0843d8df1f68eb75.jpg)

![](images/d1a80c3fbaf431759a1b29c03cc29921e29aadb3db5d96f184412edcff014314.jpg)  
Level flight

![](images/f83809b71045c5544d29b129da60c2db392ac822b25379234283233f7276bdfa.jpg)  
Page-Up (increase thrust)

![](images/30f0cb545fdd5f04db583aa74c809db62fe9e992e7bc7489dab1b9936db49e88.jpg)  
Up-Arrow (joystick forward)

![](images/d83bb0526ca759b94fef678314b0c945b3ec00998902d1410121356c9800ab7e.jpg)  
Down-Arrow (joystick backward)

![](images/940d97b743a964193e4ac6af9c461b6a012d48344bd5863793bb85559917ca35.jpg)  
Left-Arrow & Up-Arrow

Right-Arrow & Down-Arrow   
![](images/237042e1554edfa4f2f68674765ca7f8f11e4b1e239e8a8e262c1e598cd5d27b.jpg)  
注意：如果你将推力持续推到最大，燃料会很快耗尽，然后坠毁。  
DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

![](images/a106ad966fd18d1c993442a57db190c701ac3fc24116fe1f67dfe040de0972d6.jpg)

102

# 6.2.1.12.语法11_AFSIMDev_Trng_Grammar

本文为afsim2.9_src\training\developer\core\slides\

11_AFSIMDev_Trng_Grammar.pptx的翻译，主要是介绍AFSIM脚本语法文件规则。

![](images/c834356391b35ea6405ba01ec4fe976269062d438cb25dbe78d5ec030245d829.jpg)

![](images/02cf821f92d749ef3f97f28e9bbb1b795246e4cdb9ffc1e5fc5ca7af3454c77b.jpg)

![](images/6ee3ee83f61a1b18dc43737f20cf676bf94cfe9268836523d63c5ccda606a76c.jpg)  
Integrity $\star$ Service $\star$ Excellence

# AFSIM开发培训

# 11 - 语法

本文档由杨石兴翻译，该资料做为《AFSIM2.9参考手册》的一部分。没有《AFSIM2.9参考手册》的加杨石兴微信领取：13324598743

# AFRL/RQQD

# 美国空军研究实验室

- 在每个项目的“grammar”子目录中找到它们：

- swdev/src/core/wsf/grammar  
- swdev/src/core/wsf_mil/grammar   
- swdev/src/engage/grammar   
- swdev/src/wsfPlugins/wsf_p6dof/grammar

- 这些目录定义了 AFSIM 场景文件的允许语法，供 Wizard 解析使用。脚本方法会自动捕获，应该包含在发布版本中。

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

# UNCLASSIFIED

![](images/8f961fcac8a215340023bc7f371cc923aa578097df3bcbedb131e779450c3b7a.jpg)

# 内置规则

![](images/b5ac9bdd7949dafe731023cfa0313d9a40071e14b0bb235336fadc65059a405d.jpg)

• <string> - 包含非空白字符的单词  
- <real> - 例如 6.214521e22  
- <integer> - 例如 42  
- <line-string> - 直到换行符的所有文本  
• </quotable-string> - 接受带引号的字符串，例如 "quote with spaces", 或者 <string>

- 我们定义了一组固定的数据类型列表：例如 Time（时间）、Speed（速度）、Power（功率）等。  
- 使用 value 命令。  
- 所有在 $\{...\}$ 中的内容定义了语法。

(value Time { <real> <time-unit> }

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

4

![](images/184cf917d3be3cfb5f75c87a067808a9eedff7bd1c7c93c11cecac3431dacb8f.jpg)

UNCLASSIFIED

# 命名规则

![](images/52ff8e03cb1b557aa8954b7b5919c5a4b066b25d776fc8e2db97e10b647238f2.jpg)

- 可以在其他地方引用的语法语法

```typescript
rule time-unit {
    seconds | second | secs | sec | s | minutes | minute | mins | min | m | hours | hour
    | hrs | hr | h | milliseconds | millisecond | msec | msec | ms | microseconds | microsecond
    | usesc | usec | us | nanoseconds | nanosecond | nsecs | nsec | ns
    | days | day 
```

这样使用:

(value Time { <real> <time-unit> }

- 代表可选项