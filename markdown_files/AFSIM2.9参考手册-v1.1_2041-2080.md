# UNCLASSIFIED

# 扩展

![](images/ec4fbee6e68925c0b078cbf0c81f35029c8937bf50342d8fb766a56ced0a0904.jpg)

![](images/8ab2deb842229f7fb3c11134167edbf5741afa011505a4cfccce51c4fe27664f.jpg)

- 应用程序、场景和仿真都可以被“扩展”

- 应用扩展由应用程序拥有。  
- 表示可以添加到应用程序的可选功能。

- 当您需要新的脚本类型（如传感器、武器、组件、移动器）时会用到。

- 这是在AFSIM中注册所有扩展的入口点。  
- 如果要创建场景扩展或仿真扩展（将在后续练习中介绍），则需要一个应用扩展。

- 要扩展一个应用程序，您必须创建一个继承自 WsfApplicationExtension 类的类：

class myAppExtension: public WsfApplicationExtension { ... }

- 如果需要在扩展中使用，可以重写以下成员函数：

- AddedToApplication：用于接收扩展被添加到应用程序的通知。通常用于注册额外的脚本类和方法等。  
- ScenarioCreated：在场景构造函数结束时调用，用于接收应用程序通知场景已被创建——如果需要，可以在此处注册场景扩展。  
- SimulationCreated: 从仿真的 Initialize 方法中调用，用于接收应用程序通知仿真已被创建——如果需要，可以在此处注册仿真扩展。  
- ProcessCommandLine: 从 WsfApplication::ProcessCommandLine 方法中调用，用于检查当前的命令行参数，并在必要时对其进行处理  
- PrintGrammar: 打印出扩展所识别的扩展语法。  
- ProcessCommandLineCommands: called by WsfApplication::由WsfApplication::ProcessCommandLineCommands 调用，以允许扩展处理/识别其需要处理的任何命令。

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQDD.

35

![](images/35351f5a46848cd904a5f39f7a474ffd48b88a048e6c4ebc70342931a6735df0.jpg)

UNCLASSIFIED

# 应用扩展

![](images/c7258cdeec2cb0fee511e3b817157c7dd232ad3c25b6f1efa5fa59e02ba6b073.jpg)

- 我们将创建一个名为TricorderSensorRegistration的应用程序扩展，该扩展将注册一些新的脚本。

class TricorderSensorRegistration: public WsfApplicationExtension { ... }

此类将重写以下成员函数：

- AddedToApplication: 用于接收扩展被添加到应用程序的通知——将用于注册类 ScriptTricorderSensorClass 以及多个脚本方法。  
- ScenarioCreated: 在 Scenario 构造函数结束时调用，以接收来自应用程序的场景创建通知——这对于在需要时注册场景扩展非常有用。此函数将用于将 TricorderSensor 类注册为场景中的一种新型传感器。

- 检查文件 TricorderSensor.hpp，以熟悉文件底部定义的类 ScriptTricorderSensorClass 的方法和属性（我们将在练习 3 中向该类添加“内容”）。  
- 请注意，新的脚本传感器类 ScriptTricorderSensorClass 是从 WsfScriptSensorClass 派生的，而 WsfScriptSensorClass 又继承自 UtScriptTypes。

![](images/28c503ff9ab6335b70c8eb37592e8fc09c68edd812189418e79c1e2039c717af.jpg)

- 请注意，构造函数接受两个参数：类名（一个字符串）和一个指向UtScriptTypes的指针（UtScriptTypes维护了所有脚本类型类的列表）。

```cpp
//! The script interface 'class'
class ScriptTricorderSensorClass: public WsfScriptSensorClass {
public:
    ScriptTricorderSensorClass(const std::string& aClassName, UtScriptTypes* aTypesPtr);
    ~ScriptTricorderSensorClass() noexcept override = default;
}; 
```

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQDD.

37

![](images/39b03d2e9e49569fb50fff8b16cc06ff2af3c6312dacb7dc998fc2207432aceb.jpg)

# UNCLASSIFIED

# 传感器练习 1—任务 1

![](images/d9021cbd303e9240cc908630fb4ade353fe0867487b3a0475ea630afbe5de513.jpg)

在文件 SensorPluginRegistration.cpp 中：

完成TricorderSensorRegistration::AddedToApplication()方法  
- 任务1：将新的脚本类ScriptTricorderSensorClass注册到UtScriptTypes类中，后者维护了从UtScriptTypes派生的脚本类列表。  
- 使用 WsfApplication 参数对象 aApplication 将类 ScriptTricorderSensorClass 添加/注册到 UtScriptTypes 维护的脚本类列表中。

- 第1部分：调用aApplication.getScriptTypes()获取一个指向UtScriptTypes列表的指针，该列表由WsfApplication类维护。  
- 第2部分: 使用这个UtScriptTypes指针，调用其Register()方法：

- UtScriptTypes::Register() takes a single input argument:

- UtScriptTypes::Register() 方法接受一个输入参数：一个指向从 UtScriptTypes 派生的类的 unique_ptr（具体来说是我们的 ScriptTricorderSensorClass 类）。  
- 注意：在创建 unique_ptr<ScriptTricorderSensorClass>对象时，将调用 *ScriptTricorderSensorClass(string, UtScriptTypes) 构造函数。

你需要做的：

- 在调用构造函数时，需要传递以下两个参数：

1. 类的名称（字符串）：“TricorderSensor”。  
2. 一个UtScriptTypes指针，可以通过调用GetApplication()->GetScriptTypes()获取。

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19.

Other requests for this document shall be referred to AFRL/RQQD.

class TricorderSensorRegistration : public WsfApplicationExtension   
{ public: TricorderSensorRegistration() $=$ default; ~TricorderSensorRegistration() noexcept override $=$ default; void AddedToApplication(WsfApplication& aApplication) override { // EXERCISE 1 TASK 1 // Use the application object parameter to add the script tricorder class // to the script types // Call the script class "TricorderSensor" aApplicationscriptTypes()->Register(ut::make_unique<ScriptTricorderSensorClass> ("TricorderSensor", GetApplication().GetScriptTypes())); } void ScenarioCreated(WsfScenario& aScenario) override { // EXERCISE 1 TASK 2 // Use the scenario object parameter to add the TricorderSensor class to the / list of sensor types // Name the new sensor type "TRICORDER_SENSOR" } };

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQDD.

![](images/d6a96216fa0076fafb26ed020d8b8fb0fd2c26464e05ad3d3aadbf7892db8cb4.jpg)

# UNCLASSIFIED

# 传感器练习1—任务2

![](images/29bc723dc185c944cd0d74c8635f51d1fad33c6e9db77ddbe0b616738844c524.jpg)

在文件 SensorPluginRegistration.cpp 中：

- 完成TricorderSensorRegistration::ScenarioCreated()方法。

- 任务2：将类TricorderSensor添加到场景中由WsfSensorTypes维护的传感器类型列表中。

- WsfScenario 类（即对象 aScenario）维护一个实现传感器类型的类列表，这些类是从 WsfSensor 派生的。

- 第1部分：使用WsfScenario对象aScenario，通过调用WsfSensorTypes::Get(aScenario)获取传感器类型列表。

- Get() 是一个静态方法，不需要对象实例即可调用。  
- 它返回存储在 aScenario 对象中的 WsfSensorTypes 列表。

- 第2部分：在返回的WsfSensorTypes对象上调用add()方法。

- add() 方法接受两个参数：

1. 新传感器类型的名称："TRICORDER_SENSOR"。  
2. 一个指向传感器类型类的unique_ptr：unique_ptr<TricorderSensor>。

- 注意：创建unique_ptr<TricorderSensor>时，将调用TricorderSensor类的构造函数。

- 该构造函数需要场景对象 aScenario 作为其参数。

class TricorderSensorRegistration : public WsfApplicationExtension   
{ public: TricorderSensorRegistration() $=$ default; ~TricorderSensorRegistration() noexcept override $=$ default; void AddedToApplication(WsfApplication& aApplication) override { // EXERCISE 1 TASK 1 // Use the application object parameter to add the script tricorder class to the script types // Call the script class "TricorderSensor" aApplicationscriptTypes()->Register(ut::make_unique<ScriptTricorderSensorClass> ("TricorderSensor", GetApplication().GetScriptTypes())); } void ScenarioCreated(WsfScenario& aScenario) override { // EXERCISE 1 TASK 2 // Use the scenario object parameter to add the TricorderSensor class to the / list of sensor types // Name the new sensor type "TRICORDER SENSOR" WsfSensorTypes::Get(aScenario).Add("TRICORDER SENSOR", ut::make_unique<TricorderSensor>(aScenario));   
}

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQDD.

41

![](images/fa9298d46c1d52f91cfc33cfda3427eee769f44f463395d7673c554a7f65b9fa.jpg)

# UNCLASSIFIED AFSIM插件&扩展 AFSIM任务启动顺序

![](images/464587f802298dc7a69e36be334656f425813fb825e8be461851e4862ad05a36.jpg)

- 当我们创建一个应用程序扩展时会发生什么？

- 插件方法何时以及如何被调用？  
- WsfApplicationExtension 方法何时被调用？  
- ProcessInput() 和 Initialize() 方法何时以及如何被调用？

![](images/82cce88166204f3c96923df4ff8777236fb506586c9d359154e1b1aebe6a43c2.jpg)

WsfStandardApplication 构造函数利用插件管理器（Plugin Manager）来查找并加载所有插件（包括训练文件夹中的插件——这是因为使用了 CMake 选项 WSF_ADDExtension_PATH）。

- 对于找到的每个插件，都会执行 WsfPluginSetup（注意：这会导致我们的传感器练习插件的 WsfPluginSetup 函数被执行）。

- 这会导致我们的传感器练习中的 TricorderSensorRegistration 类（一个应用程序扩展）被创建并注册到 app 中。  
- 注册扩展后，会调用 WsfApplicationExtension::AddedToApplication()，而该方法被 TricorderSensorRegistration::AddedToApplication() 重写。

- AddedToApplication()会将“TricorderSensor”注册为一个新的脚本类型类。

Other requests for this document shall be referred to AFRL/RQQD.

43

![](images/93d9009bb5596a20ce47b3f5b1e0eb03cb100875b69a7a8cd773f01c0efb7a90.jpg)

# UNCLASSIFIED AFSIM插件&扩展

# AFSIM任务启动顺序

![](images/6548febc97eb5498f3ec63b7d3d5ebb79ff96adbf1c03246fa8b2d7aaf1728c2.jpg)

![](images/2d715c99257cc3bc3e60dd3140fd0391e689b47aff3a9392e2d25a31614c0a59.jpg)

任务随后将所有必要的预定义扩展注册到 app 中。

![](images/5abec8037b1e67f21a67237bec79596f21d6b97f26b63b399b7d9741c4e86f69.jpg)

任务随后创建场景并调用 WsfScenario 构造函数：WsfScenario scenario(app);

- 该构造函数会调用 WsfApplication::ScenarioCreated() 方法。  
- 而这又会依次调用所有已注册的应用程序扩展的 ScenarioCreated() 方法（包括我们的 TricorderRegistration 扩展）。

- TricorderRegistration::ScenarioCreated() 会创建并将TRICORDER_SENSOR类型添加到传感器类型列表中，以便在场景文件中发现TRICORDER_SENSOR命令时，可以调用它们的ProcessInput()方法。

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQDD.

45

![](images/ccb89c593a6893d9136604c4cfd33ef2bb10c5a6d16daad082db2c4e278f3757.jpg)

# UNCLASSIFIED AFSIM插件&扩展 AFSIM任务启动顺序

![](images/85006e43ae5da0bd0cdd850c2a377e4236217bc189110df7bdc21a1f2c18c8cb.jpg)

![](images/ea0152384e3f534aae221557ea26d30d5c7423a547cdd59aa54e43400c6fba8a.jpg)

任务调用了app.WsfStandardApplication::ProcessInputFiles(),

该方法会调用 WsfScenario::LoadFromFile()。

- 对于输入中的每个命令：

- 调用每个核心类的 ProcessInput() 方法。  
- 调用TricorderSensor::ProcessInput()来处理TricorderSensor命令（但没有相关命令）。  
- 调用TricorderMode::ProcessInput()来处理模式命令。  
- 调用每个已注册场景扩展的ProcessInput()方法——由于TricorderRegistration类中未定义ProcessInput(),因此没有任何效果。

Note: a TricorderSensor object is created when a TricorderSensor block command is encountered in the scenario input files

![](images/277b2bd790ebdbfa87904cd557805d4a7634c163ef1f5e0d4635fa3ed86f89b7.jpg)

任务调用了app.WsfStandardApplication::ProcessInputFiles(),

- 该方法会调用 WsfScenario::LoadFromFile(),  
- 然后调用 WsfScenario::CompleteLoad()。

- 调用每个场景扩展的 Complete() 方法。  
- 然后调用每个场景扩展的 Complete2() 方法。

Note: None of our classes inherit WsfScenarioExtension, so no Complete or Complete2 are defined that need to be called

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQDD.

47

![](images/8d090bcae1401a3de491137b047fa1db7212a90e79a8c813c4e901d3cb326a2e.jpg)

# AFSIM插件&扩展

# AFSIM任务启动顺序

![](images/84db9b8c35cea6ac539027e4c85e73544c9069ba54a805084b3689528f51e5bf.jpg)

![](images/d6b435070f4cf39fc4fab098b6e3ba568f54ae6ba37c229d615e00e0fac49ed8.jpg)

任务通过执行以下代码创建了 Simulation:

```cpp
std::unique_ptr<WsfSimulation> simPtr = app.CreateSimulation(scenario, ...); 
```

- CreateSimulation 调用了 WsfSimulation 对象的构造函数（以 scenario 作为参数）。

![](images/bcbf7e88f062344a94773e49a8ca1fe802c099decb1e526a3d99d8b3c82778bc.jpg)

任务通过执行以下代码初始化 Simulation:

app.InitializeSimulation(simPtr.get())

- InitializeSimulation 调用了: aSimPtr->Initialize()

(where aSimPtr $\equiv$ simPtr.get())

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQDD.

# UNCLASSIFIED

![](images/a36730c9ad3ff2a5a89894de4f1909c03ee1c8f5251579dd57cdc76884125cde.jpg)

# AFSIM插件&扩展

# AFSIM任务启动顺序

![](images/668bb35dabbef968d724d3fb44e9447ac236d6e48f84bf60a45ec2f941db5904.jpg)

![](images/d076295fac3b298e671596c213a7712465c8d2080da759b89d45bc48a4a94bc9.jpg)

Missio使用下面的语句初始化Simulation:

app.InitializeSimulation(simPtr.get())

- InitializeSimulation 调用: aSimPtr->Initialize()   
- WsfSimulation::Initialize 调用: mScenario.SimulationCreated(*this)

(where mScenario $\equiv$ scenario and \*this $\equiv$ *simPtr.get()

![](images/5ce7848955fefed4d7c9c84f367f68926290a4fea35690568a1fb76cfaf4982f.jpg)

Mission通过调用Simulation来初始化:

app.InitializeSimulation(simPtr.get())

- InitializeSimulation调用: aSimPtr->Initialize()   
- WsfSimulation::Initialize调用：mScenario.SimulationCreated(*this)   
- SimulationCreated调用: GetApplication().SimulationCreated(aSimulation)

(where GetApplication() ≡ app and aSimulation ≡ *simPtr.get())

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19.

Other requests for this document shall be referred to AFRL/RQQD.

51

![](images/73226e1f03264e8140241eaa3e078f71c2fd9d6269db53481d86f83586ed5162.jpg)

# AFSIM插件&扩展

# AFSIM任务启动顺序

![](images/4eda3236f40d9bb0cd0b6a5d56d8ad546aaf1bd321d228c90c67f68c95c4870d.jpg)

![](images/817afc2e9640f9dfe67c2c4ffa0d09c556b4aaaa822415bbed5c8d61fe6c128e.jpg)

Mission通过调用Simulation来初始化:

app.InitializeSimulation(simPtr.get())

- InitializeSimulation 调用: aSimPtr->Initialize()   
- WsfSimulation::Initialize 调用: mScenario.SimulationCreated(*this)   
- SimulationCreated 调用: GetApplication().SimulationCreated(aSimulation)

- 在每个应用扩展中调用 SimulationCreated(aSimulation)

(where aSimulation $\equiv^{*}\mathrm{simPtr.get()}$

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19.

Other requests for this document shall be referred to AFRL/RQQD.

![](images/0af5bebb52f351a89f4fd1cde1bbec6138482a62512b42a74420a1c7eeda1ade.jpg)

Mission通过调用Simulation来初始化:

app.InitializeSimulation(simPtr.get())

中

- SimulationCreated 调用: GetApplication().SimulationCreated(aSimulation)

- 每个扩展调用 SimulationCreated(aSimulation)  
- 调用 WsfApplicationExtension::SimulationCreated(aSimulation)

(where aSimulation $\equiv^{*}\mathrm{simPtr.get()}$

Note: TricorderRegistration does not override SimulationCreated, so this call has no effect 53

![](images/d592cb59e7c566e6d3f6fdf50f9375243518877b8b29ba37b4272ab6520ff960.jpg)

# UNCLASSIFIED

# AFSIM插件&扩展

# AFSIM任务启动顺序

![](images/db3af24f9b53c8732edc538a35a93bc954998e8afa7e8f4721cf96096495ee03.jpg)

![](images/463ecb81e7a2612196624fcad970274655115f0006c07de1d3d6c6ba493487f6.jpg)

Mission通过调用Simulation来初始化:

app.InitializeSimulation(simPtr.get())

- InitializeSimulation 调用: aSimPtr->Initialize()

：

- 下一步, WsfSimulation::Initialize 调用:

WsfObserver::SimulationInitializing(this)

- 该举是通知所有已经注册的Observer要进行初始化了

注意: 我们目前没有创造任何观察者, 所以调用也没有什么用

![](images/4c44e66ae43d05b0ba7c309f34c5899e1efc0469e3eeb01a1250bc2fe7eeda31.jpg)

Mission通过调用Simulation来初始化：

app.InitializeSimulation(simPtr.get())

- InitializeSimulation 调用: aSimPtr->Initialize()

：

- 下一步, Initialize 在所有的仿真扩展中调用: Initialize()

然而对于当前传感器没有仿真扩展

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQDD.

55

![](images/562441bb1f1e7f8b1dfb772d786cea0fb3ccaafe7d76d39184e3c900e1c7561a.jpg)  
UNCLASSIFIED AFSIM插件&扩展 AFSIM任务启动顺序

![](images/ea5f0f80053e7c78e7b4407e803390c042f116ab761fc0530e37ee28379f4092.jpg)

![](images/ec5abadbda13306051c8df375ea3513e8cbf8f1174bc50abee9b5a1fb85d7b1b.jpg)

Mission通过调用Simulation来初始化:

app.InitializeSimulation(simPtr.get())

- InitializeSimulation 调用: aSimPtr->Initialize()

：

- 下一步，WsfSimulation::Initialize将所有可用平台添加到模拟的平台列表中  
- 最终, WsfSimulation::Initialize 将仿真状态置为 cPENDING_START

- 之前的动画仅专注于创建一个应用扩展。  
- 在后续的练习中，我们将创建场景扩展，并观看涵盖该过程的动画，了解更多细节。  
- 在后续的练习中，我们还将创建模拟扩展，并观看涵盖该过程的动画，了解更多细节。

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQQD.

57

![](images/566026180c9cd9b55a806b234785595012d59a0ff5ba57fb4e740001279c150c.jpg)

# UNCLASSIFIED

# 传感器练习2

![](images/d3af2e1c63db201e754ca9835765d74286b2be4a020514ba444f680e586b808d.jpg)

- 本练习的重点是创建一个新的传感器（继承自 WsfSensor）和一个新的传感器模式（继承自 WsfSensorMode）。

- 理解TricorderSensor类和TricorderMode类。  
- 实现TricorderSensor类和TricorderMode类的部分功能。  
- 使用ProcessInput来处理TricorderSensor的输入。  
- 使用 Initialize 方法确保在模拟开始时，所有成员变量都被赋予初始值。

- 检查文件 TricorderSensor.hpp 中的 TricorderSensor 类,并注意其继承自 WsfSensor, 以及为我们的解决方案假定的类属性和函数。

//! A standard tricorder sensor for sensing living things.   
class TricorderSensor : public WsfSensor   
public:   
//! Constructor explicit TricorderSensor(WsfScenario& aScenario); TricorderSensor& operator $\equiv$ (const TricorderSensor&) $=$ delete; //! Virtual destructor \~TricorderSensor() noexcept override $=$ default;

```txt
DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQDD. 
```

59

![](images/ecf155961d8a55bc15602aa3a5a1144f14f4f325f6fc2672b8df5b97f116c255.jpg)

# 传感器练习 2 — 检视 1

# TricorderSensor.hpp

![](images/a8bb27a6ae879fa5c5f495acadbf97a11cac4e5e641c5f18b22b87cbf180a8fb.jpg)

```cpp
class TricorderSensor : public WsfSensor   
{ public: WsfSensor\* Clone() const override; bool Initialize(double aSimTime) override; boolProcessInput(UtInput& aInput) override; void Update(double aSimTime) override; bool AttemptToDetect(double aSimTime, WsfPlatform\* aTargetPtr, Settings& aSettings, WsfSensorResult& aResult) override; size_t GetLifeFormTypeCount(WsfStringId aModeNameId); WsfStringId GetLifeFormTypeEntry(WsfStringId aModeNameId, unsigned int aEntry); protected: class TricorderMode : public WsfSensorMode { }； //! The sensor-specific list of modes (not valid until Initialize is called) //! Required by the default sensor scheduler std::vector mTricorderModeList; //! Get the name of the script class associated with this class. //! This is necessary for proper downcasts in the scripting language. const char\* GetScriptClassName() const override; }; 
```

```txt
DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQDD. 
```

- 检查文件 TricorderSensor.hpp 中的

TricorderSensorMode 类，并注意其继承自

WsfSensorMode，以及为我们的解决方案假定的类属性和函数。

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQDD.

61

![](images/ba5342877d9924c359f36bd3d70b0772411f07db84bb2ff85b8547af92a5a553.jpg)

# UNCLASSIFIED 传感器练习2—检视2

# TricorderSensor.hpp

![](images/4e41c0636d61273af8fdf78e8195f6333f1993c8d858bb6a8be20a414383ca00.jpg)

class TricorderMode : public WsfSensorMode 在整个初始化期间，   
public: TricorderMode(); TricorderMode(const TricorderMode& aSrc); TricorderMode& operator $\equiv$ (const TricorderMode& aSrc); WsfMode\* Clone() const override; virtual bool Initialize(double aSimTime, 在加载想定时由ProcessInput统一调用。 WsfSensor\* aSensorPtr); bool ProcessInput(UtInput& aInput) override; bool AttemptToDetect(double aSimTime, WsfPlatform\* aTargetPtr, WsfSensor::Settings& aSettings, WsfSensorResult& aResult) override; void UpdateTrack(double aSimTime, void Deselect(double aSimTime) override {} void Select(double aSimTime) override {} void ApplyMeasurementErrors(WsfSensor::Result& aResult) override; double GetLifeReading(WsfPlatform\* aTargetPtr); bool IsLifeForm(WsfPlatform\* aTargetPtr);

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQDD.

- 完成 TricorderSensor 构造函数的实现，具体步骤如下：

- 任务1a：通过调用SetModeList方法，分配一个新的传感器模式列表，并使用该传感器特定的模式模板（TricorderMode）进行参数化。  
- 注意：SetModeList 的函数签名如下：

- SetModeList(std::unique_ptr<WsfSensorModeList> aModeListPtr);

- 该参数需要是一个指向 WsfSensorModeList 的唯一指针（unique_ptr），而该 WsfSensorModeList 是使用指向 WsfSensorMode（即 TricorderMode，继承自 WsfSensorMode）的指针构造的。

- 任务1b：将传感器调度器分配为默认传感器调度器。

默认传感器调度器负责管理传感器的目标检测尝试。  
- 大多数传感器使用 WsfDefaultSensorScheduler。  
- 它确保我们能够以固定的时间间隔，在每个frame_time中查看每个目标一次。  
需要一个类唯一的模式列表。  
注意：SetScheduler的函数签名如下：

- SetScheduler(std::unique_ptr<WsfDefaultSensorScheduler> aSchedulerPtr);   
- 该参数必须是一个指向 WsfDefaultSensorScheduler 的指针，而该调度器是使用默认构造函数构造的。

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQDD.

63

![](images/07e77f5a07f6700206ce8476f506bd60da0d6a2697fa5dce3b1e85011a5fd90a.jpg)

# 传感器练习 2—任务 1

# TricorderSensor.cpp

![](images/c8e70b1b460955f830192548fdb60d02bbd42458dfa61e16e9d31f78c299ade5.jpg)

- 完成TricorderSensor构造函数的实现，具体步骤如下：

- 任务1c：将传感器跟踪器分配为默认传感器跟踪器。

- 默认传感器跟踪器根据传感器的检测结果维护传感器的跟踪列表。  
- 大多数传感器使用 WsfDefaultSensorTracker，但不报告跟踪信息的传感器（如成像传感器）不会设置跟踪器。  
- 注意：SetTracker 的函数签名如下：

SetTracker(std::unique_ptr<WsfDefaultSensorTracker>(WsfScenario& aScenario));

- 该参数是一个 WsfDefaultSensorTracker，它是通过使用场景（scenario）的引用构造的。

TricorderSensor::TricorderSensor(WsfScenario& aScenario)

: WsfSensor(aScenario), mTricorderModelList()

// Set the class of the sensor. This is a passive multi-spectral sensor Class(cPASSIVE | cRADIO | cINFRARED | cVISUAL | cACOUSTIC);

```cpp
// EXERCISE 2 TASK 1a
// Assign a new mode list, parameterizing it with this
// sensor-specific mode template (constructed with a new TricorderMode)
SetModeList(ut::make_unique<WsfSensorModeList>(new TricorderMode)); 
```

// EXERCISE 2 TASK 1b
// Assign the sensor scheduler to be the default sensor scheduler
SetScheduler(ut::make_uniqueWsfDefaultSensorScheduler());

// EXERCISE 2 TASK 1c
// Assign the sensor tracker to be the default sensor tracker (constructed // with a reference to the scenario)
SetTracker(ut::make_unique<WsfDefaultSensorTracker>(aScenario));

指向new

TricorderMode的指

针由 WsfModeList

删除，而

WsfModeList是由

WsfSensorModeLis

t继承的。

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQDD.

# 传感器练习2—检视3

# TricorderSensor.cpp

# 在 TricorderSensor.cpp文件中:

- 检视和理解：

```cpp
//! Initialized the Tricorder Sensor; called by WsfSimulation. //! @param aSimTime [input] The current simulation time. //! @return 'true' if initialization was successful. bool TricorderSensor::Initialize(double aSimTime) { // Must call base class first! bool ok = WsfSensor::Initialize(aSimTime); // Reduce future dynamic casting by extracting derived class mode pointers. mModelListPtr->GetDerivedModelList(mTricorderModellist); return ok; } 
```

- 检视和理解：WsfModeList.hpp

```cpp
template<class T>  
void GetDerivedModelList(std::vector<T>& aModelList) const  
{  
    aModelListresize(mModelList.size());  
    for (typename std::vector<wsfMode*>::size_type i = 0; i < mModelList.size(); ++i)  
    {  
        T modePtr = dynamic_cast<T>(mModelList[i]);  
        assert(modePtr != nullptr);  
        aModelList[i] = modePtr;  
    }  
} 
```

# 在TricorderSensor.cpp中

# - 检视和理解:

```cpp
// @param aInput [input] The input stream.
// 
// @return 'true' if the command was recognized (and processed) or 'false'
// if the command was not one recognized by this class. 
bool TricorderSensor::ProcessInput(UtInput& aInput) 
{
    // Call the base class implementation
    return WsfSensor::ProcessInput(aInput);
} 
```

![](images/4cc5a2f3b5fc22b086841aba2ee2e5c2926e271df1a65d98226f257758640027.jpg)

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQDD.

67

![](images/01ad2990dd750cb3cccd8db6d054ac44cb232ad340f48a48d800b797f141de29.jpg)

# UNCLASSIFIED

# 传感器练习2—检视5

# TricorderSensor.cpp

![](images/4d7767bab345c273793b4cbc78df174c336b5ae90afd25e43ab1118affb80df9.jpg)

# In TricorderSensor.cpp:

# - 检视和理解：

```cpp
// Called by the simulation object to update the Tricorder Sensor
//! @param aSimTime [input] The current simulation time.
void TricorderSensor::Update(double aSimTime)
{
    // Bypass updates if not time for an update. This avoids unnecessary device updates.
    // (A little slop is allowed to make sure event-driven chances occur as scheduled)
    if (mNextUpdateTime <= (aSimTime + 1.0E-5))
        {
            WsfSensor::Update(aSimTime); // Ensure my position is current
            PerformScheduledDetections(aSimTime); // Perform any required detection attempts
        }
} 
```

![](images/59784a5d9359a146f673e47ea327e42c18674863408fe1c4fd12ac62b4e4bae4.jpg)

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19.

Other requests for this document shall be referred to AFRL/RQQD.

在 TricorderSensor.hpp中

- 在TricorderSensor::TricorderMode类中添加一个类型为WsfCategoryList的成员变量，用于存储该模式可以检测的生命形式类型。

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQDD.

69

![](images/e009ae062d0024065420339fdf98441ec8c8e01f40d725f59cede3b2456bae07.jpg)

# 传感器练习2—任务2解决方案

# TricorderSensor.hpp

![](images/9885d11ef67c77176d821eab6b52c2b356518ec15f01223961a82db3c24fcafb.jpg)

```cpp
class TricorderMode : public WsfSensorMode   
public: TricorderMode(); TricorderMode(const TricorderMode& aSrc); TricorderMode& operator=(const TricorderMode& aSrc); WsfMode\* Clone() const override; virtual bool Initialize(double aSimTime, WsfSensor\* aSensorPtr); bool ProcessInput(UtInput& aInput) override; double GetLifeReading(WsfPlatform\* aTargetPtr); bool IsLifeForm(WsfPlatform\* aTargetPtr); //EXERCISE 2 TASK 2 WsfCategoryList mLifeFormTypes;   
}； 
```

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQDD.

# TricorderSensor.cpp:

- 检视和理解：

```cpp
TricorderSensor::TricorderMode::TricorderMode()
: WsfSensorMode()
, mLIFEFormTypes()
{
    // Derived sensor modes should call SetCapabilities(...) to register what
    // they detect and report out in measurements and tracks.
    SetCapabilities(cRANGE | cTYPE | cOTHER);
} 
```

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQDD.

71

![](images/641ef9c1057b4487a18bdf49e18dbc8a883247879d9acd264af763c8580bad38.jpg)

# UNCLASSIFIED

# 传感器练习2—任务3

TricorderSensor.cpp

示例想定输入:

(see sensorscenario.txt)

# 在TricorderSensor.cpp中

```txt
platform Spock VULCAN
add sensor tricorder TRICORDER_SENSOR
mode KLINGON
    frame_time 2 s
    reports_type
    life_form_type klingon.life_form
    end_mode
    mode ALL-LifeForms
    frame_time 1 s
    reports_type
    life_form_type LIFE(Form
    life_form_type klingon.life_form
    end_mode
    endsensor
endplatform 
```

- 任务3：在TricorderSensor::TricorderMode::ProcessInput中去读取和添加指定的类型到我们的可检测生命形式列表中:

命令形式为：life_form_type <string-value>

command

value

- 该变量必须是一个 WsfStringld 类型，并需要存储通过 ReadValue 方法从输入文件中读取的 <string-value>。

- 基类, WsfSensorMode::ProcessInput, 处理基本的传感器输入像 frame_time 和 reports_type

AFSIM examples can be found by searching source codes using references to "ReadValue".

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19.

Other requests for this document shall be referred to AFRL/RQQD.

```cpp
bool TricorderSensor::TricorderMode::ProcessInput(UtInput& aInput)  
{ bool myCommand = true; std::string command(aInput.GetCommand()); if (command == "life_form_type") { // EXERCISE 2 TASK 3 WsfStringId lifeFormType; aInput.ReadValue(lifeFormType); mLIFEFormTypes.JoinCategory(lifeFormType); } else { myCommand = WsfSensorMode::ProcessInput(aInput); } 如 return myCommand; 
```

```txt
life_form_type 目前是 TricorderSensor中的唯一的新命令
```

```txt
JoinCategory 添加lifeFormType到mLifeFormTypes中 
```

如果当前命令不是life_form_type，那么我们需要将输入传递给基类WsfSensorMode::ProcessInput，以查看是否可以在那里处理。

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQDD.

73

![](images/9ac2fd9024d4de9cab405a23df2eafa3e473ce6d4f617ee4a2bb3a9b7a483e1d.jpg)

# UNCLASSIFIED 传感器练习2—任务4 TricorderSensor.cpp

![](images/e010f08a411e7ade366df344b366915e3e1e68c289e7f00a574ee9a3d3a00fdc.jpg)

- 实现 TricorderSensor::TricorderMode::IsLifeForm 方法

- 该方法用于确定给定目标（WsfPlatform）是否是该模式可以检测到的生命形式。  
- 将目标平台视为生命形式的条件如下：

- 如果它的类型与mLifeFormTypes中的任何生命形式类型相同，或者如果它的类别与mLifeFormTypes中的任何生命形式类别相同。  
- 注意：mLifeFormTypes可用于同时存储类别和平台类型。

- 任务4a:

遍历通过调用mLifeFormTypescatsCategoryList(返回的类别列表。  
- 对于每个类别，调用输入参数 aTargetPtr->IsA类型的方法，并传入当前类别。

- IsA类型的方法在平台与传入的类别共享类型时返回 true。  
- 如果 IsA_typeOf() 返回 true，则 IsLifeForm() 应返回 true。

- 任务4b:

- 调用mLifeFormTypes.Intersects(aTargetPtr->GetCategories())方法。   
- Intersects 方法接受一个输入参数（类别列表），并确定它是否是生命形式类型的类别之一。  
- 如果 Intersects() 返回 true，则 IsLifeForm() 应返回 true。

```cpp
bool TricorderSensor::TricorderMode::IsLifeForm(WsfPlatform* aTargetPtr)   
{ for(const auto& category:mLifeFormTypes-categoryList()) { //EXERCISE2TASK4a //Check platform type if(aTargetPtr->IsA_TYPEOf(category)){ return true; }   
1 //EXERCISE2TASK4b //Check for category on the platform if(mLifeFormTypes.Intersects(aTargetPtr->GetCategories())){ return true; 1   
return false; 
```

category类别被依次设置为类别列表中生命形式类型的每个类别

IsA_TYPEOf 接受一个输入参数（类别），并确定该类别是否是平台的类型。

Intersects 接受一个输入参数（类别列表），并确定它是否是生命形式类型的类别之一。

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQDD.

UNCLASSIFIED

# 传感器练习2—任务5

75

![](images/bf962e2cf8cf840ff48db74a9ada888bbf71bde89c48abdc2fc409bc9867f022.jpg)

![](images/a5984586daafaf6e214810d2c3f65fd7d08dca02c25c93009610ec86b371e522.jpg)

# 在TricorderSensor.cpp:

·完成

TricorderSensor::TricorderMode::AttemptToDetect 方法的实现:

- 你需要创建一个名为 detected 的布尔变量，并将其设置为调用 TricorderSensor::TricorderMode::IsLifeForm() 方法的结果（该方法来自任务 4）。  
- 请记住，IsLifeForm()方法需要一个输入参数aTargetPtr，而aTargetPtr是AttemptToDetect方法的输入参数之一。  
- 注意：这个布尔变量（detected）会在调用之后的第二个 if 语句中使用，用于检查是否检测到了生命形式。

```cpp
bool TricorderSensor::TricorderMode::AttemptToDetect(double aSimTime, WsfPlatform* aTargetPtr, Settings& aSettings, WsfSensorResult& aResult)  
{ //EXERCISE 2 TASK 5 // Check for a life form bool detected = IsLifeForm(aTargetPtr); 我们在这里定义检测 if (detected) 在这里使用检测结果 { // Set probability of detection to 1.0; tricorder will detect all life forms aResult.mPd = 1.0; } // Get the range and unit vector from the receiver to the target. aTargetPtr->Update(aSimTime); // Ensure the target position is current GetSensor()->GetPlatform()->GetLocationWCS(aResult.mRcvrLoc.mLocWCS); aTargetPtr->GetLocationWCS(aResult.mTgtLoc.mLocWCS); UtVec3d::Subtract(aResult.mRcvrToTgt.mTrueUnitVecWCS, aResult.mTgtLoc.mLocWCS, aResult.mRcvrLoc.mLocWCS); aResult.mRcvrToTgt.mRange = UtVec3d::Normalize(aResult.mRcvrToTgt.mTrueUnitVecWCS); //Notify observers about the sensor detection attempt WsfSensorObserver::Get(GetSimulation().SensorDetectionAttempt(aSimTime, GetSensor(), aTargetPtr, aResult); return detected; } 
```

```txt
DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQDD. 
```

77

![](images/4348ebbaad81625ce51ac3de48969224433dfa94ae30e3ae18e0b1eca2cc5e08.jpg)

# 传感器练习2—检视7

![](images/b3c645c17daabba8e7092cc5b3e8e5139d7d62d564b3644435bce6958a4743a6.jpg)

- 熟悉 WsfSensorResult 类（位于文件 WsfSensorResult.hpp [路]

径：./core/wsf/source/sensor]），并查看我们在变量 aResult 中设置的数据。

- 至少必须提供目标的距离（range-to-target），否则在 WsfSensorMode 类的 ApplyMeasurementErrors 方法中会触发断言错误。

```txt
bool TricorderSensor::TricorderMode::AttemptToDetect(double aSimTime, WsfPlatform* aTargetPtr, Settings& aSettings, WsfSensorResult& aResult) 
```

bool detected $=$ IsLifeForm(aTargetPtr); ... if (detected) { // Set probability of detection to 1.0; tricorder will detect all life forms aResult.mPd $= 1.0$ . } //Get the range and unit vector from the receiver to the target. aTargetPtr->Update(aSimTime); //Ensure the target position is current GetSensor( $)\rightarrow$ GetPlatform( $)\rightarrow$ GetLocationWCS(aResult.mRcvrLoc.mLocWCS); aTargetPtr->GetLocationWCS(aResult.mTgtLoc.mLocWCS); UtVec3d::Subtract(aResult.mRcvrToTgt.mTrueUnitVecWCS,aResult.mTgtLoc.mLocWCS,aResult.mRcvrLoc.mLocWCS); aResult.mRcvrToTgt.mRange $=$ UtVec3d::Normalize(aResult.mRcvrToTgt.mTrueUnitVecWCS); //Notify observers about the sensor detection attempt WsfSensorObserver::Get(GetSimulation().SensorDetectionAttempt(aSimTime,GetSensor(),aTargetPtr,aResult) return detected;

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQDD.

79

![](images/f4cc2263cd2136dd1527fbb3c8a404ee63081cf51abc0ac4f2efabb7339f4388.jpg)

# UNCLASSIFIED

# 传感器练习2—检视7

# WsfSensorResult.hpp

![](images/635ba7694f2507b3d3ef27188106f56e28505a4156c3af418a0557f904f0dea3.jpg)

//! Result class is supplied to the AttemptToDetect method.   
//! On output it contains detailed data about the detection attempt.   
//! Not every sensor will update every member. Each member documents under   
//! what conditions it is valid. It is the responsibility of the caller to   
//! ensure that the member they are using contains valid data.   
class WsF exporting WsfSensorResult : public WsfEM_Interaction   
public:   
//! Status flag values used in mCheckedStatus and mFailedStatus   
enum   
{ cCONCEALMENT $= 0\mathrm{x}00010000$ //<! Concealment checked/failed cDOPPLER_LIMITS $= 0\mathrm{x}00020000$ //<! Doppler limits checked/failed cVELOCITY_LIMITS $= 0\mathrm{x}00040000$ //<! Velocity limits checked/failed cTARGET_deleted $= 0\mathrm{x}00080000$ //<! Target deleted cOTH_LIMITS $= 0\mathrm{x}00100000$ //<! OTH Bounce Constraints cEXCLUSION_SALAR $= 0\mathrm{x}00200000$ //<! Solar exclusion is blocking sensor cEXCLUSION_LUNAR $= 0\mathrm{x}00400000$ //<! Lunar exclusion is blocking sensor cMOON_BLOCKED $= 0\mathrm{x}0080000$ //<! Moon is blocking the sensor from target   
}; WsfSensorResult() = default; ~WsfSensorResult() override = default; bool Detected() const;

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQDD.

class WsF exporting WsfEM_Interaction : public UtScriptAccessible   
public: using Component $=$ WsfEM_InteractionComponent; using ComponentList $=$ WsfComponentListTWsfEM_InteractionComponent>;   
1   
//! Represents the location of a platform or device.   
struct LocationData   
{ double mLat{0.0};//< Latitude (decimal degrees) double mLon{0.0};//< Longitude (decimal degrees) double mAlt{0.0};//< Altitude (meters) double mLocWCS[3]{0.0,0.0,0.0}; //< WCS locations (meters) bool mIsValid{ false }; //< Data is valid only if this is true   
}；   
//! Represents the relative location of one object with respect to another. ...   
struct RelativeData   
{ double mRange{-1.0};//< Range to the other object (meters). double mTrueUnitVecWCS[3]{0.0,0.0,0.0};//< True WCS unit vector pointing to the other object. double mTrueAz{0.0};//< The azimuth of the other object (radians) double mTrueE1{0.0};//< The elevation of the other object (radians) double mUnitVecWCS[3]{0.0,0.0,0.0};//< Apparent WCS unit vector pointing to the other object. double mAz{0.0};//< The apparent azimuth of the other object (radians) double mEl{0.0};//< The apparent elevation of the other object (radians)   
}；   
：

```txt
DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQDD. 
```

81

![](images/0e6fe12efae7d7f7f0db3c7e42d010082a51d7782257faa3855ecb9bf97ab367.jpg)

# UNCLASSIFIED

# 传感器练习2—检视7

WsfEM_Interaction.hpp

![](images/84225070943ef3ecfd1538c3171f2d748383cbd64fd7ee3a1e3457df916bba17.jpg)

：

```txt
/// Location of the receiver.  
/// @note This is valid only if the interaction involves a receiver.  
LocationData mRcvrLoc; 
```

```txt
/// Location of the target.  
/// @note This is valid only if the interaction involves a target platform.  
LocationData mTgtLoc; 
```

```txt
//! Receiver-to-target relative data.  
//! @note This is valid only if the interaction involves a target platform.  
RelativeData mRcvrToTgt; 
```

```scss
//! Target-to-receiver relative data.
//! @note This is valid only if the interaction involves a target platform.
RelativeData mTgtToRcvr; 
```

}；

bool TricorderSensor::TricorderMode::AttemptToDetect(double aSimTime, WsfPlatform* aTargetPtr, Settings& aSettings, WsfSensorResult& aResult)   
{ bool detected $=$ IsLifeForm(aTargetPtr); ... if (detected) { // Set probability of detection to 1.0; tricorder will detect all life forms aResult.mPd $= 1.0$ .. } //Get the range and unit vector from the receiver to the target. aTargetPtr->Update(aSimTime); // Ensure the target position is current GetSensor()->GetPlatform()->GetLocationWCS(aResult.mRcvrLoc.mLocWCS); aTargetPtr->GetLocationWCS(aResult.mTgtLoc.mLocWCS); UtVec3d::Subtract(aResult.mRcvrToTgt.mTrueUnitVecWCS,aResult.mTgtLoc.mLocWCS,aResult.mRcvrLoc.mLocWCS); aResult.mRcvrToTgt.mRange $\equiv$ UtVec3d::Normalize(aResult.mRcvrToTgt.mTrueUnitVecWCS); //Notify observers about the sensor detection attempt WsfSensorObserver::Get(GetSimulation().SensorDetectionAttempt(aSimTime，GetSensor()，aTargetPtr，aResult); return detected;

```txt
DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQDD. 
```

83

![](images/3cb9a4601c93625d0a6dacd241234514369836ccf65ac3e215e35f6e0f2dbba5.jpg)

UNCLASSIFIED

# 传感器练习2—任务6

![](images/2357df2c38e0551e118b49e6de5f4c778f05ba2d24b8566e167c7858201450cc.jpg)

# 在TricorderSensor.cpp中

# ·执行

# TricorderSensor::TricorderMode::GetLifeReading

- 确保值在 0.0 到 1.0 之间

# - 使用生命形式的损伤因子（damage factor）来表示健康值（health reading）。

- 可以通过调用平台的 GetDamageFactor 方法获取该值。  
- 高损伤因子表示低健康值。  
- 请参阅AFSIM文档中“platform”部分的initial DAMAGE_factor属性。

```cpp
double TricorderSensor::TricorderMode::GetLifeReading(WsfPlatform* aTargetPtr)  
{ // EXERCISE 2 TASK 6 // Use the damage factor of the life form for the health reading // Use std::min and std::max to ensure value is between 0 and 1. return std::min(1.0, std::max(0.0, 1.0 - aTargetPtr->GetDamageFactor())); } 
```

This is equivalent to:   
```txt
double val = 1.0 - aTargetPtr->GetDamageFactor();  
if (val < 0.0) val = 0.0;  
if (val > 1.0) val = 1.0;  
return val; 
```

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQDD.

UNCLASSIFIED

# 传感器练习2—任务7

85

![](images/e7e763716da12b420ece657337591cdd932fe97fbd3a1b3d4be9dfdbd82dbe9b.jpg)

![](images/22b4d78aae2c51cd2aa560cbdb48a9bad8b1509a98da7d528abcbb22f9732b27.jpg)

# 在TricorderSensor.cpp:

- 完成TricorderSensor::TricorderMode::UpdateTrack方法的实现：

- 如果目标通过 AttemptToDetect 方法的处理被确定为已检测到，则传感器会自动处理 WsfTrack 对象的创建，并调用此方法以填写新的或更新的跟踪信息。  
- 大部分需要填写的跟踪信息由基类实现完成。

- 熟悉附加到平台的辅助数据容器的使用，以报告生命形式的类型。  
- 将 WsfTrack 属性“track quality”设置为 GetLifeReading 方法返回的生命值（life reading）。  
- 高的“track quality”值表示“强”的生命值。

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19.

Other requests for this document shall be referred to AFRL/RQQD.

void TricorderSensor::TricorderMode::UpdateTrack(double aSimTime, WsfTrack* aTrackPtr, WsfPlatform* aTargetPtr, WsfSensorResult& aResult)   
{ // If the sensor is reporting type if (ReportsType()) { // Get the life form type WsfAttributeContainer& auxDataTarget $\equiv$ aTargetPtr->GetAuxData(); if (auxDataTarget AttributeExists("LIFE(Form_REPORTED_TYPE")) { // Set the type data in the track WsfStringId��ID $=$ WsfStringId(auxDataTarget.GetString("LIFE(Form_REPORTED aResult.mMeasurement.TypeId(typeID); aResult.mMeasurement.SetTypeName(true); } 1 // Call base class' method. This will set valid measurement data (typeof) in the WsfSensorMode::UpdateTrack(aSimTime, aTrackPtr, aTargetPtr, aResult); // Set the "track quality" WsfTrack attribute with the life reading // EXERCISE 2 TASK 7 aTrackPtr->SetTrackQuality(GetLifeReading(aTargetPtr));   
}

```txt
DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQDD. 
```

87

![](images/ba955ad3edf447aa37a2bbfd403af97922628add384958ef0108f1997df2008f.jpg)

# 传感器练习3

![](images/180b6782f6d57e24d98220d53241063e34a024f739c1a4e61871f64984e72cf9.jpg)

- 本练习的重点是：

- 实现脚本类 ScriptTricorderSensorClass 的部分内容，该类通过脚本接口提供对 TricorderSensor 类的访问。  
- 理解 C++ 中的 #define、UT_DEclareScriptMethod 和 UT DEFINEScriptMethod 是如何扩展为最终的类声明和定义的。

- 检查文件 TricorderSensor.hpp，熟悉在文件底部定义的

ScriptTricorderSensorClass 类的方法和属性。

- 请记住，该类是从 WsfScriptSensorClass 类派生而来的。  
- 注意，新的脚本传感器类 ScriptTricorderSensorClass 中有多个对 UT_DEclare-scriptMethod 的调用。  
- 每次调用都会在 ScriptTricorderSensorClass 中创建一个新的类声明，其名称为传递给调用的参数的名称。

![](images/4df7123e07fdc6ba08e165ce99a81b9381fc38d9cced793fe3bef7392d67f0d0.jpg)

![](images/615e0f302e763dbea6e0d34ba8d1244ea275e1d6d2162c85ece2c24b80ef40a4.jpg)  
DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQQD.

89

![](images/756ff122c8cf92258a52e7fe072065978b20c4b40df7535ac954e43919276dec.jpg)

# 传感器练习3—检视2

# TricorderSensor.cpp

![](images/fbb146eac886c5b79f548e1cbb084521d15ba1eb9472c91012b85905b6c2d5e2.jpg)

```rust
//! Provide the name of the corresponding script class so that the //! scripting system can implement type casting properly. const char* TricorderSensor::GetClassName() const {
    return "TricorderSensor";
} 
```

这将名称TricorderSensor定义为已定义脚本方法的脚本类名称。

```cpp
ScriptTricorderSensorClass::ScriptTricorderSensorClass(const std::string& aClassName, UtScriptTypes* aScriptTypesPtr) : WsfScriptSensorClass(aClassName, aScriptTypesPtr) SetClassName("TricorderSensor"); 这将脚本类名称设置为 TricorderSensor，与上面 GetScriptClassName 中定义的名称相同。
```

- 在 TricorderSensor.cpp 文件中查看  
ScriptTricorderSensorClass 的实现。  
- 注意构造函数的定义中有对 AddMethod 的调用。  
• 注意文件末尾使用了 UT DEFINEScriptMETHOD, 它定义了脚本的行为。

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQDD.

91

![](images/769a9ce10676015ec2e327c6c46e85adcce392e6e1facf086aa80da5b597d41e.jpg)

# UNCLASSIFIED 传感器练习3—检视3

# TricorderSensor.cpp

![](images/bf51cef77c559025f8d0e6ce0fed0673a3a3dd9a96f28c2478eabfbe9694e995.jpg)

# - 检视和理解:

```cpp
include"script/WsftScriptContext.hpp"   
ScriptTricorderSensorClass::ScriptTricorderSensorClass(const std::string& aClassName,   
UtscriptTypes\* aScriptTypesPtr) :WsftScriptSensorClass(aClassName,aScriptTypesPtr)   
{ SetClassName("TricorderSensor"); AddMethod(ut::make_unique<LifeFormTypeCount_1>"LifeFormTypeCount")）; // LifeFormTypeCount() AddMethod(ut::make_unique<LifeFormTypeCount_2>"LifeFormTypeCount")）; // LifeFormTypeCount(string) AddMethod(ut::make_unique<LifeFormTypeEntry_1>"LifeFormTypeEntry")）; // LifeFormTypeEntry(int)   
} 
```

AddMethod函数将具有指定名称（例如LifeForm.TypeEntry）的脚本方法添加到脚本接口中，并将实现（例如类LifeForm.TypeEntry_1）与该方法关联起来。

注意：这实际上并没有声明/定义脚本方法。

- 检视和理解:   
$\vdots$ // int lifeFormCount $=$ <x>.LifeFormTypeCount();   
UT	defineScriptMethod(ScriptTricorderSensorClass, TricorderSensor, LifeFormTypeCount_1, 0, "int", "")   
{ }   
// int lifeFormCount $=$ <x>.LifeFormTypeCount(string aModeName);   
UT	defineScriptMethod(ScriptTricorderSensorClass, TricorderSensor, LifeFormTypeCount_2, 1, "int", "string")   
{ }   
// int lifeFormEntry $=$ <x>.LifeFormTypeEntry(int aEntryIndex);   
UT	defineScriptMethod(ScriptTricorderSensorClass, TricorderSensor, LifeFormTypeEntry_1, 1, "string", "int")   
{ }   
// int lifeFormEntry $=$ <x>.LifeFormTypeEntry(string aModeName, int aEntryIndex);   
UT	defineScriptMethod(ScriptTricorderSensorClass, TricorderSensor, LifeFormTypeEntry_2, 2, "string", "string, int");   
{ }

UT DEFINEScriptMethod定义了脚本方法的主体/实现，并将其与脚本类的声明和定义函数关联起来。

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQDD.

93

![](images/362551be4c2dcd92d0ffe26c654a57e542bb8adf05030c2e12b563fe190be7d0.jpg)

# AFSIM脚本

![](images/f07e5aa47356711cc53e8d7ede722554d3efb659d6ce00a99c2e9e02a3f4d497.jpg)

- AFSIM 拥有一个相当丰富的脚本接口，该接口定义了用户可以从其基于 WsfPlatform 等实体调用的脚本方法。

- 有关脚本的详细使用案例，请参阅用户培训材料。

- AFSIM 提供了大量预定义的脚本方法。

- 开发人员可以通过声明和定义新的脚本方法并将其添加到管理脚本的UtScriptClass中来扩展此接口。

- 以下是相关的关键功能：

- UT_DECLAREScriptMethod   
- UT DEFINEScriptMethod   
- AddMethod   
- AddStaticMethod

- #define UT.Declare-script 方法 (METHOD_NAME)

- 展开为针对 METHOD_NAME参数的类声明。  
- 这个新类继承自UtScriptClass::InterfaceMethod类。  
- 为该类的方法声明了构造函数和 operator()。  
- 此宏必须在“脚本”类声明内部调用。

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQDD.

95

![](images/37c2ccc1dcb597fd5cd9207cb4bfc6898ffdce8a390ae1e88a8bd572dcca4ba0.jpg)

UNCLASSIFIED

# 声明脚本方法

![](images/5c9f9768738a4fc603f8b2dd9a6e32803f7815c29fb499469154174ef423fb1a.jpg)

- #define UT DEFINEScriptMethod(CLASS,OBJ_TYPE, METHOD, NUM_args, RET_TYPE, ARGTYPES)

- 为使用 UT.Declare-script 方法宏定义的相同“方法”创建类定义。  
- 为该类创建一个 operator() 方法。

- 当用户脚本执行关联的脚本方法时，脚本接口会调用此操作符。

创建一个模板 $\mathsf{C} + +$ 函数（不与任何类关联），其名称为

<CLASS#METHOD>_Execute，函数体是宏定义的代码。

- 符号 <CLASS#METHOD> 是 CLASS 和 METHOD 的拼接，形成一个单一的字符串。

- 该函数的主体是紧跟在 UT DEFINEScriptMethod 宏调用之后的大括号中的代码块。  
- 此函数由为“脚本”类定义的 operator() 调用。

- #define UT DEFINEScriptMethod(CLASS,OBJ_TYPE, METHOD, NUM_args, RET_TYPE, ARGTYPES)

- CLASS: 包装脚本方法的“脚本”类的名称。  
- OBJ_TYPE: 与此脚本方法直接关联的对象的类名。  
-METHOD:实现脚本方法的类的名称（应与UT_DECLAREScriptMethod的METHOD_NAME参数相同）。  
- NUM_args: 实现 METHOD所需的参数数量。  
- RET_TYPE: 一个字符串，指示实现 METHOD的返回类型。  
- ARG_TYPES: 一个字符串，指示实现 METHOD所需参数的类型。

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQDD.

97

![](images/25431117720ae3d3960d6692e32c0f11464d3616c4df0b07bc78b7adac2ff572.jpg)

UNCLASSIFIED

# 脚本方法的注册

![](images/4888adb296b89e6c2e51af2dcacf0bb55946d9655f11ad367192f15eb6114c11.jpg)

- OtScriptClass::AddMethod( ... )   
- 通常以以下形式调用:

AddMethod(ut::make_unique<METHOD>(ScriptFunction));

- 将由 UT Define Script METHOD 宏定义的 METHOD 添加到脚本接口中可调用的方法集合中。  
- ScriptFunction 是一个字符串，用于标识可以从用户脚本中调用的脚本函数的名称。  
- 一旦定义并添加了该脚本方法，用户可以在场景文件中的脚本接口中通过调用 ScriptFunction，并传入正确数量和类型的参数来使用该方法。

- 步骤 1: 创建一个新的“脚本”类, 该类继承自源代码目

录../afsim/core/wsf/source-script中定义的WsfScript<xxx>Class类之一，例如：

- WsfScriptPlatformClass   
- WsfScriptPlatformPartClass   
- WsfScriptSensorClass   
- WsfScriptZoneClass   
等等。

- 确保该类声明了以下内容：

- 一个构造函数，接收两个参数：  
- 一个字符串，表示脚本方法将使用/交互的类的类名。  
- 一个指向UtScriptTypes对象的指针。  
- 一个析构函数，该析构函数需要重写基类的析构函数（可以是默认析构函数）。

- 步骤 2：在新“脚本”类的声明中，在析构函数声明之后，调用 UT.DeclareScriptMethod。

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQQD.

99

![](images/88d902d4b67bb1281801053da84be6f0b76a25042fb7760a36b056339861f074.jpg)

# 创建新脚本方法的标准流程

![](images/16d42c29dd5249d66e119cc52434aca58bc749c7374c229c1738f81687ba7138.jpg)

- 步骤3：在“脚本”类的实现文件中，在定义任何“脚本”类方法之前，以及调用UT DEFINEScriptMethod之前，包含头文件"script/WsfScriptContext.hpp"。  
- 步骤 4：在“脚本”类的实现文件中，在构造函数定义之后调用 UT DEFINEScriptMethod。

- 对于头文件中每次调用 UT.Declare-scriptMETHOD，实现文件中应有一次对应的 UT	definecriptMethod 调用。  
- 这些调用通常应放置在“脚本”类构造函数定义之后。

- 步骤5：在“脚本”类的构造函数定义中，调用AddMethod。

- 对于每次调用 UT.DeclareSCRIPT 方法，都应有一次对应的 AddMethod 调用。  
- 这些 AddMethod 调用将脚本方法名称与由 UT_DECLAREScriptMethod 和 UT DEFINEScriptMethod 定义的实现对象关联起来。

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQDD.

# UNCLASSIFIED

# 传感器练习3—任务1

101

![](images/c02f1cc4ef2b5b9556c990ae728ccc036a9aaafdc7e93e3565ecb2915cd46cd3.jpg)

![](images/89f68e4373150ba7c749a90a085313c0f5a76a5ef977600989174089768dffbf.jpg)

在TricorderSensor.hpp文件中：

- 向 ScriptTricorderSensorClass 添加一个 UT.Declare-scriptMethod，声明 LifeFormTypeEntry_2 为一个脚本的实现。  
• 注意: UT_DECLAREScriptMethod会为正在定义的脚本生成一个类声明。  
- 请注意，脚本方法 LifeFormTypeEntry_1 已经被定义。  
- 通过创建一个名为 LifeFormTypeEntry_2 的方法，我们实际上是在重载脚本方法 LifeFormTypeEntry。  
- 为了使其正确工作，我们需要提供一个唯一的签名（与 LifeFormTypeEntry_1 的签名不同），并实现一个使用我们新的 TricorderSensor 和 TricorderMode 类方法的功能。

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19.

Other requests for this document shall be referred to AFRL/RQQD.

class ScriptTricorderSensorClass : public WsfScriptSensorClass { public:

```cpp
ScriptTricorderSensorClass(const std::string& aClassName, UtScriptTypes* aTypesPtr); 
```

```javascript
~ScriptTricorderSensorClass() noexcept override = default; 
```

```javascript
UT.Declare-scriptMETHOD(LifeFormTypeCount_1); UT.Declare-scriptMETHOD(LifeFormTypeCount_2); 
```

```txt
UT.Declare-scriptMethod(LifeForm.TypeEntry_1); 
```

```txt
// EXERCISE 3 TRAINING TASK 1 
```

```txt
UT_DEclare-scriptMETHOD(LifeFormTypeEntry_2); 
```

}；

这将创建第一个重载方法，名为 LifeFormTypeEntry。

该脚本方法接受一个参数，一个表示 EntryIndex 的整数。

这将创建第二个重载方法，名为 LifeFormTypeEntry。该脚本方法接受两个参数：

- 一个字符串，表示 ModeName。  
- 一个整数，表示 EntryIndex。

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQDD.

UNCLASSIFIED

# LifeFormEntry_2的扩展

103

![](images/77719fd37e543e6786f42d851b28ebe6efabc0c664f8464de126c54643fd036e.jpg)

![](images/43bc65bcbd8449a28c52dae232d446a541168b9a15efba52dc5cefb467fadd19.jpg)

UT.Declare-scriptMETHOD(LifeFormTypeEntry_2);

![](images/9383f6aebb5466f55b19c2a44a5769cf0664b55e90b9ae947457e199c749e0b9.jpg)

Is transformed into

```cpp
class LifeForm.TypeEntry_2 : public UtScriptClass::InterfaceMethod
{
public:
    LifeForm.TypeEntry_2(const std::string& aName = "LifeForm.TypeEntry_2");
virtual void operator() (UtScriptExecutor* utScriptContext& const UtScriptRef& const std::vector<UtScriptData>& aReturnVal); 
```

}；

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQDD.

# - 检视和理解:

定义了类 LifeFormTypeCount_1，该类实现了脚本类方法

LifeFormTypeCount.

此方法返回一个整数（int），且不接受任何参数。

```txt
// int lifeFormCount = <x>.LifeFormTypeCount();  
UT DEFINEScriptMethod(LifeFormTypeCount_1, 0, "int", "")  
{ // Use the current mode WsfstringIdemodeNameId = aObjectPtr->GetCurrentModeName(); // Get the number of life form types for this mode int lifeFormTypeCount = static_cast<int>(aObjectPtr->GetLifeFormTypeCount(modeNameId)); // Return the count aReturnVal.SetInt(lifeFormTypeCount); } 
```

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19.

Other requests for this document shall be referred to AFRL/RQQD.

# UNCLASSIFIED

# 传感器练习3—检视4

# TricorderSensor.cpp

105

![](images/9abde821389feb5e6504e8abf0bec9b88a23a9f07eb3c02a825bbf59170fb467.jpg)

![](images/31367835e21cd73abe7e14fe810d4a3886bc91e022fc319f7072934faa54132e.jpg)

# - 检视和理解：

定义了类 LifeFormTypeCount_1，该类实现了脚本类方法

LifeFormTypeCount

此方法返回一个整数（int），且不接受任何参数。

```cpp
// int lifeFormCount = <x>.LifeFormTypeCount(string aModeName);  
UT DEFINEScriptMethod(ScriptTricorderSensorClass, TricorderSensor, LifeFormTypeCount_2, 1, "int", "string")  
{ // Argument 1: string aModeName // Use the mode name provided and convert to string ID WsfStringIdemodeNameId = WsfStringId(aVarArgs[0].ToString()); // Get the number of life form types for this mode int lifeFormTypeCount = static_cast<int>(aObjectPtr->GetLifeFormTypeCount(modeNameId)); // Return the count aReturnVal.SetInt(lifeFormTypeCount); } 
```

```txt
// int lifeFormEntry = <x>.LifeFormTypeEntry(string aModeName, int aEntryIndex);  
UT DEFINEScriptMethod(LifeFormTypeEntry_2, 2, "string", "string, int")  
{ // Argument 1: string aModeName // Argument 2: int aEntryIndex // Use the mode name provided and convert to string ID WsfStringIdemodeNameID = WsfStringId(aVarArgs[0].GetStr; unsigned index = (unsigned)aVarArgs[1].GetInt(); if(index >= aObjectPtr->GetLifeFormTypeCount(modeNameId)) { // EXERCISE 3 TASK 2 } WsfStringId lifeFormEntry = aObjectPtr->GetLifeFormTypeEntry(modeNameId, index); if (lifeFormEntry == nullptr) { // EXERCISE 3 TASK 2 } else { aReturnVal SETString(lifeFormEntry.GetString()); } } 
```

```txt
DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQDD. 
```

107

![](images/97b0aeb0fc71ef0db29d2709da926a7ba1ec601ebe2e9977152c94c175c2ae5f.jpg)

UNCLASSIFIED

# 传感器练习3 — 任务2

![](images/2db8f881d0deee88d785111b8ee65a79513eb39c845e81aac99c3fa2098f343b.jpg)

- LifeFormTypeEntry_1 是脚本方法 LifeFormTypeEntry 的第一个重载实现。  
- LifeFormTypeEntry_2 是脚本方法 LifeFormTypeEntry 的第二个重载实现。  
- 在文件 TricorderSensor.cpp 中:  
- 完成 LifeFormTypeEntry_2 的实现。  
- 任务2a:

如果以下调用返回的索引值过大：aObjectPtr->GetLifeFormTypeCount(modeNameld)则说明 modeNameld（一个 WsfStringID）未找到。  
- 在这种情况下，调用宏 UTSCRIPT_ABORT，并传入字符串 "Bad mode name"。

- 任务2b:

- 如果以下调用返回的 WsfStringld 是空指针（nullptr）：  
aObjectPtr->GetLifeFormTypeEntry(modeNameld, index)则说明传入的索引值未找到。  
- 在这种情况下，调用宏 UTScriptABLEX，并传入字符串 "Bad index"。

```cpp
// int lifeFormEntry = <x>.LifeFormTypeEntry(string aModeName, int aEntryIndex);  
UT DEFINEScriptMethod(ScriptTricorderSensorClass, TricorderSensor, LifeFormTypeEntry_2, 2, "string", "string, int")  
{ // Argument 1: string aModeName // Argument 2: int aEntryIndex // Use the mode name provided and convert to string ID WsfStringIdemodeNameId = WsfStringId(aVarArgs[0].ToString()); unsigned index = (unsigned)aVarArgs[1].GetInt(); if (index >= aObjectPtr->GetLifeFormTypeCount(modeNameId)) { // EXERCISE 3 TASK 2a UTScript.AbORT("Bad mode name"); } WsfStringIdlifeFormEntry = aObjectPtr->GetLifeFormTypeEntry(modeNameId, index); if (lifeFormEntry == nullptr) { // EXERCISE 3 TASK 2b UTScript.AbORT("Bad index"); } else { aReturnVal SETString(lifeFormEntry.GetString()); } 
```

```txt
DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQDD. 
```

109

![](images/c4d9e585d2209fa580ed3d374246f1e0c80d4143a8cdef5a5ab04023adfd743f.jpg)

UNCLASSIFIED

# 脚本方法定义中可用的隐式参数变量

![](images/ecab799592be40738a7270e25a799945260b505f80b27c6f1dbe511608ea0bcd.jpg)

- 每个定义的脚本方法在其 <xxx>_Execute 函数的定义中（包含在 UT DEFINEScriptMethod 实现块中的代码）隐式访问多个变量和方法。  
- 对于 LifeFormEntry_2 的实现，其 Execute 函数声明如下：

```cpp
template<class T> void ScriptTricorderSensorClassLifeFormEntry_2 Execute(UtScriptExecutor* aExecutorPtr, UtScriptContext& const UtScriptRef& aContext, aReference, T* aObjectPtr, UtScriptClass* aObjectClassPtr, UtScriptData& aReturnVal, UtScriptClass* aReturnClassPtr, const std::vector<UtScriptData>& aVarArgs, UtScriptClass::InterfaceMethod* this); 
```

- 这些参数中的每一个都可以在脚本方法定义的主体中使用。

# 参数 用途

- aExecutorPtr：指向调用/执行此函数的脚本执行器类的指针。  
·aContext：当前脚本上下文（范围、环境、变量、脚本方法等）。  
- aReference：当前脚本引用（包括指向实际应用层对象的指针，以及定义该类的UtScriptClass对象）。  
·aObjectPtr：指向与脚本关联的应用程序对象的指针（例如，在本练习中是一个TricorderSensor对象）。  
·aObjectClassPtr：指向应用程序对象脚本类型的指针。  
-aReturnVal：用于加载返回值的对象。  
- aReturnClassPtr：指向返回对象类类型的指针。  
- aVarArgs: 包含脚本方法输入参数的列表。

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQDD.

111

![](images/e86c0838c1782fae8bb6a47cf6b972cfe421ee0cd210d9dd5c9c637692ff1316.jpg)

# LifeFormEntry_2 脚本

# 隐式参数变量的使用

![](images/0f25421442fe4d4071f63368ea9e98c53888b7ec7ccf2ae863a09e991b4000e6.jpg)

```txt
// int lifeFormEntry = <x>.LifeFormTypeEntry(string aModeName, int aEntryIndex);  
UT DEFINEScriptMethod(LifeFormTypeEntry_2, 2, "string", string, int)  
{  
    // Argument 1: string aModeName  
    // Argument 2: int aEntryIndex  
    // Use the mode name provided and convert to string ID  
    WsfStringIdemodeNameId = WsfStringId(aVarArgs[0].GetString());  
    unsigned index = (unsigned)aVarArgs[1].GetInt();  
    if (index >= aObjectPtr->GetLifeFormTypeCount(modeNameId))  
    {  
        UTScript_ABOBT("Bad mode name");  
    }  
    WsfStringId lifeFormEntry = aObjectPtr->GetLifeFormTypeEntry(modeNameId, index);  
    if (lifeFormEntry == nullptr)  
    {  
        UTScript_ABOBT("Bad index");  
    }  
    else  
    {  
        aReturnVal SETString(lifeFormEntry.GetString());  
    } 
```
在文件TricorderSensor.cpp中：

- 在 ScriptTricorderSensorClass 构造函数中，添加一个 AddMethod 语句，将 LifeForm.TypeEntry_2 关联为重载脚本方法 LifeForm.TypeEntry 的实现类。

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQDD.

113

![](images/5631e896c7958d34bb670fbc6d4eda0762aa0d16809c9f7f16ae73aaac5ef87d.jpg)