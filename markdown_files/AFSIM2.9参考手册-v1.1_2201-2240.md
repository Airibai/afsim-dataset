- 要扩展一个场景，您必须创建一个继承自 WsfScenarioExtension 类的类

# class ComponentTypesRegistration: public WsfScenarioExtension

- 您必须重写以下方法:

- AddedToScenario：接收扩展被添加到场景的通知，通常用于注册额外的组件类型对象和工厂

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

49

![](images/b3b6c4e0be118aebd58ff2e13c29fe37308dacde9e1586cae97ce9d0199e5127.jpg)

# 组件练习1-检视4

# ComponentTypesRegistration.hpp

![](images/ae04d1063bb1ab0b5088855f1a3171d5288b5786b8580745e9c3ed3940dd1a79.jpg)

- 在文件 ComponentTypesRegistration.hpp 中，检查新组件类型与场景的注册情况。

- AddedToScenario 方法负责将新的 ShieldTypes 组件类型和新的 LatinumComponent 组件类型添加到场景中。

class ComponentTypesRegistration : public WsfScenarioExtension   
public: ComponentTypesRegistration() $=$ default;   
void AddedToScenario() override { // Register our custom type lists with the scenario. // Shields mShieldTypesIndex $\equiv$ GetScenario().GetTypeLists().size auto mShieldTypesPtr $\equiv$ ut::make_unique<ShieldTypes>(Get Scenario().Addelist(std::move(mShieldTypesPtr)). // Latinum // Note we do not need to access the type list for later // using it to process input and add instances to the GetScenario().Addelist(ut::make_unique<LatinumTypes> } ShieldTypes& GetShieldTypes() const {return \*static cast<ShieldTypes\*>(GetScenario().GetTypeList); private: size_t mShieldTypesIndex;   
}； DISTRIBUTION C. Distribution authorized to U.S.Government Agency Other requests for this document shall be referred

AddedToScenario 方法是由场景的 RegisterExtension 方法调用的，而 RegisterExtension 方法又是由应用扩展的 ScenarioCreated 方法调用的。

- 检查ShieldTypes类的构造函数。

- 注意它将ShieldComponentFactory（在ShieldTypes.cpp中定义）注册到场景中。  
- 注意它将WSF_SHIELDS添加为可以在场景中创建的命令，并为该类型注册ShieldComponent类。

```cpp
class ShieldTypes : public WsfObjectTypeList<ShieldComponent>   
{ public: static ShieldTypes& Get(WsfScenario& aScenario); static const ShieldTypes& Get(const WsfScenario& aScenario); explicit ShieldTypes(WsfScenario& aScenario);   
}； 
```

```cpp
ShieldTypes::ShieldTypes(WsfScenario& aScenario) : WsfObjectTypeList<ShieldComponent>(aScenario, cREDEFINITION_OPENED, "shields") { aScenario.RegisterComponentFactory(ut::make_unique<ShieldComponentFactory>(); // Allows for definition // inside platform, platform_type blocks. Add("WSF_SHIELDS", ut::make_unique<ShieldComponent>(aScenario)); // Dummy type "WSF_SHIELDS" // explicitly referenced in the input. } 
```

```txt
DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD. 
```

51

![](images/baee78576e4e564e7e90eb18c13578e4fbd54f03eefc6cd143e89f66f9aebb1c.jpg)

# UNCLASSIFIED

# 组件练习 1 - 检视 6

# LatinumTypes.hpp

![](images/37e161da1e1943a8a696e8c435fa061268207950d617e192f6d95c08ebe1ca26.jpg)

- 检查 LatinumTypes 类的构造函数。

- 注意它将LatinumComponentFactory（在LatinumComponent.cpp中定义）注册到场景中。

```typescript
class LatinumTypes : public WsfObjectTypeList<LatinumComponent> {
    public:
        explicit LatinumTypes(WsfScenario& aScenario);
} 
```

```cpp
LatinumTypes::LatinumTypes(WsfScenario& aScenario) : WsfObjectTypeList<LatinumComponent>(aScenario, cREDEFINITION_OPENED, "latinum") { SetSingularBaseType(); aScenario.RegisterFactory(ut::make_unique<LatinumComponentFactory>(); // Allows for definition // inside platform, platform_type blocks. } 
```

![](images/385d7a4bf571cec1d80dad9ecdf9289939c7d27d15e373fe81155a1a77f2034b.jpg)

WsfStandardApplication 构造函数利用插件管理器查找并加载所有插件（包括训练文件夹中的插件——因为使用了 cmake 选项

WSF_ADD_EXTENDED_PATH)。

- 对于找到的每个插件，执行 WsfPluginSetup（注意：这会导致我们的组件练习插件的 WsfPluginSetup 函数被执行）

- 这导致我们的组件练习的 RegisterShieldComponent 应用扩展被创建并注册到 app 中  
- RegisterExtension 然后调用 WsfApplicationExtension::AddedToApplication(), 该方法被 RegisterShieldComponent::AddedToApplication() 重写。  
- AddedToApplication 注册了 ShieldComponent 和 LatinumComponent 的脚本类型和方法。

53

![](images/c4e6500923416af4b1892e24cd2874ab58a0db1d96f0697bf4a5700ef6061b28.jpg)

# UNCLASSIFIED

# AFSIM插件&扩展

# AFSIM mission 启动顺序

![](images/e0481e24cb5c22b0e4930503dd3869bec998e2ab8cec07ef695e1d45358543de.jpg)

![](images/3acef3d3a3366dc58398ed93232cac89f8dddc3b17b2a7922f98bd963e0ebbc9.jpg)

任务随后将所有必要的预定义扩展注册到 app 中

![](images/1a93bc310d8545b0aa6b80b3eb3f74203b7ca28247e51fc8564abb9e78ce256b.jpg)

任务随后创建场景并调用 WsfScenario 构造函数：WsfScenario scenario(app);

- 该构造函数调用 WsfApplication::ScenarioCreated 方法。  
- 这又依次调用所有注册的应用扩展的 ScenarioCreated 方法（包括 RegisterShieldComponent::ScenarioCreated）。

- 这进一步创建了 ComponentTypesRegistration 并将其注册到场景中

- RegisterExtension 然后调用 ComponentTypesRegistration::AddedToScenario。  
- ComponentTypesRegistration::AddedToScenario 将 ShieldTypes 和 LatinumTypes 添加为新的场景类型。

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQQD.

55

![](images/b8e361fe2a0b55c4074b8056a0af6c6ddc9a9632b5e7a1a0b5c72aa96334d622.jpg)

# AFSIM插件&扩展

# AFSIM mission 启动顺序

![](images/d524099a30fa01d470d0e25113348a9063a3d46965bf7eb5d4722b2fef93ab89.jpg)

![](images/7a2688a68bd3a6175b80bd878f07090a1b6a1295712766928c01e64422868a6a.jpg)

- 当 ComponentTypesRegistration::AddedToScenario 执行时：

- 它创建一个ShieldTypes对象，

- ShieldTypes 构造函数调用 ShieldTypes::RegisterComponentFactory 方法，将 ShieldComponentFactory 注册到场景中。  
- 这使得场景在处理场景的输入文件时能够创建ShieldComponent对象。

然后它创建LatinumTypes对象

- LatiniumTypes 构造函数调用 LatiniumTypes::RegisterComponentFactory 方法，将 LatiniumComponentFactory 注册到场景中。  
- 这使得场景在处理场景的输入文件时能够创建 LatinumComponent 对象。

![](images/0fb95f50b8a772df5eadee58890a65463c15d5037a7ee41ff712993507009174.jpg)

Mission调用app.WsfStandardApplication::ProcessInputFiles()，该方法又调用WsfScenario::LoadFromFile()

- 对于输入中的每个命令，调用每个核心类的ProcessInput()方法（包括注册组件和类型的处理）。  
- 在处理 cyber Effect 传感器命令时，核心找到 CyberSensorComponentFactory 用于创建 CyberSensorEffect 对象。

调用CyberSensorComponentFactory::ProcessInput(),

- 创建一个CyberSensorEffect对象作为传感器组件（用于相关的传感器），  
- 并读取 track_drop、track_pulloff 和 exploit_delay 命令。

![](images/9f960bb37c180161df6a64a7f74989939b7daa61b90c337b653d383829bdd546.jpg)

# UNCLASSIFIED

# AFSIM插件&扩展

# AFSIM mission 启动顺序

![](images/c3c1d992ab122ad53a4592317ff759e4b6e17f4c380ba646225747d44fade686.jpg)

![](images/28d8597f5a9c99fa40dc9cdd70d2520249ed34186c6205fc77f94dc1b709618e.jpg)

Mission调用app.WsfStandardApplication::ProcessInputFiles()，该方法又调用WsfScenario::LoadFromFile()。

- 对于输入中的每个命令，调用每个核心类的ProcessInput()方法（包括注册组件和类型的处理）。  
：  
- 在处理 WSF_SHIELDS 类型时，核心找到 ShieldTypes 的 ShieldComponentFactory，用于创建 ShieldComponent 对象，该对象是一个平台组件（因为它是一个注册组件），并创建一个 ShieldComponent。  
- 调用ShieldComponentFactory::ProcessAddOrEditCommand(),   
- 这导致调用ShieldComponent::ProcessInput()来处理shields命令。

![](images/c7d32bad2fda0d3577946897193cccde60c7ff7ab9f72fc3ab0b471e4b71c2a6.jpg)

Mission调用app.WsfStandardApplication::ProcessInputFiles()，该方法又调用WsfScenario::LoadFromFile()。

- 对于输入中的每个命令，调用每个核心类的ProcessInput()方法（包括注册组件和类型的处理）。  
：  
- 在处理latinum命令时，核心找到LatinumComponentFactory，用于创建LatinumComponent对象。  
- 调用 LatinumComponentFactory::ProcessInput(),   
- 创建LatinumComponent对象作为平台组件，并  
- 调用LatinumComponent::ProcessInput(),该方法读取quantity命令。

59

![](images/9ad3acb44b444330d049c1b0206d5ccf04c52577e91096da98e4ffe85613a932.jpg)

# UNCLASSIFIED

# AFSIM插件&扩展

# AFSIM mission 启动顺序

![](images/199f5385a0f549e9b171631320c9fba07f6d795b0bcc3277d8e6725b23819273.jpg)

![](images/10a526af662363b6a4e37134b9dee562953405b61e28a18a94f73c84fd6822df.jpg)

Mission调用app.WsfStandardApplication::ProcessInputFiles()，该方法又调用WsfScenario::LoadFromFile()。

- 对于输入中的每个命令，调用每个核心类的 ProcessInput() 方法，  
- 调用每个注册场景扩展的ProcessInput()方法。  
- 调用 WsfScenarioExtension::ProcessInput() 处理 ComponentTypesRegistration。  
- ComponentTypesRegistration 并没有重写此方法，因此这没有任何效果。

![](images/df4f5c2b563925d437d84d6212830cf775659e12f694910bf988a3e282ef3ea6.jpg)

任务调用app.WsfStandardApplication::ProcessInputFiles()，该方法接着调用WsfScenario::LoadFromFile()，然后调用WsfScenario::CompleteLoad()。

- 调用每个场景扩展的 Complete() 方法。  
- 然后调用每个场景扩展的 Complete2() 方法。

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

61

![](images/81dc8f6e52c7780d2d600806ca4106decf3c45dbfcf537e71bf6cf80a0b94425.jpg)

# UNCLASSIFIED AFSIM插件&扩展 AFSIM mission启动顺序

![](images/8dca329b78f9af7d3fbacb5d0985ac0ba94c2c2932e4b997a830ab4b453991b2.jpg)

![](images/58659dfedf9988da71f46a984f57484398edc7eea2505ee8a78c5781cd3ce5f1.jpg)

Mission通过执行以下代码创建 Simulation:

std::unique_ptr<WsfSimulation> simPtr =

app.CreateSimulation(scenario, ...);

- CreateSimulation 调用 WsfSimulation 对象的构造函数（以 scenario 作为参数）

![](images/5d8ac40839d19fb3fa9a1bbfbe9408abb15dcfcb528f430b3989a19864d6dd4f.jpg)

Mission通过执行以下代码初始化 Simulation:

app.InitializeSimulation(simPtr.get())

- InitializeSimulation 调用: aSimPtr->Initialize()

(where aSimPtr $\equiv$ simPtr.get())

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

63

![](images/d466580e2244feb5dff9248ecabea55cdadeb84ac47fa661084e43e315e7b8f9.jpg)

# AFSIM插件&扩展

# AFSIM mission 启动顺序

![](images/41639fd4f267e0339512ec334a7cc4d77353b20f5b86b481d3d1551edb832f97.jpg)

![](images/0f98cdff144c086bdc81731e34fd93248938761484054063e9ea10698b3cc0fa.jpg)

Mission通过执行以下代码初始化 Simulation:

app.InitializeSimulation(simPtr.get())

- InitializeSimulation 调用: aSimPtr->Initialize()   
- WsfSimulation::Initialize 调用: mScenario.SimulationCreated(*this)

(where mScenario $\equiv$ scenario and \*this $\equiv$ *simPtr.get()

![](images/741e4475a0a667d0645c16243a3c639d6801502cee8183a0d4e95d296cc0401e.jpg)

Mission通过执行以下代码初始化 Simulation:

app.InitializeSimulation(simPtr.get())

- InitializeSimulation 调用: aSimPtr->Initialize()   
- WsfSimulation::Initialize 调用: mScenario.SimulationCreated(*this)   
- SimulationCreated 调用: GetApplication().SimulationCreated(aSimulation)

(where GetApplication() ≡ app and aSimulation ≡ *simPtr.get())

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19.

Other requests for this document shall be referred to AFRL/RQQD.

65

![](images/f3e2722345f57d4ac2ee1a0ed64e2d3fa52bdcf1968aff095ed227f89c187f2b.jpg)

# AFSIM插件&扩展

# AFSIM mission 启动顺序

![](images/86371da41e7dbb55ddea5b0ed05fdcb9c91e550997510cbec519734df1a7f41d.jpg)

![](images/779c6f83d8c5ca157f6b3221ac91d166616b87fc6f0e36bf3ab3a1cfafb2ec74.jpg)

Mission通过执行以下代码初始化 Simulation:

app.InitializeSimulation(simPtr.get())

- InitializeSimulation 调用: aSimPtr->Initialize()   
- WsfSimulation::Initialize 调用: mScenario.SimulationCreated(*this)   
- SimulationCreated 调用: GetApplication().SimulationCreated(aSimulation)

- 对于每个应用扩展调用 SimulationCreated(aSimulation)

(where aSimulation $\equiv^{*}\mathrm{simPtr.get()}$

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19.

Other requests for this document shall be referred to AFRL/RQQD.

![](images/37fe71ab15eee87c943e36260f55999aed45c17f7814dac2362454bb09b2680e.jpg)

Mission通过执行以下代码初始化 Simulation:

app.InitializeSimulation(simPtr.get())

：

- SimulationCreated 调用: GetApplication().SimulationCreated(aSimulation)

- 对于每个应用扩展调用 SimulationCreated(aSimulation)  
- 会调用 WsfScenarioExtension::SimulationCreated(aSimulation) on ComponentTypesRegistration

(where aSimulation $\equiv^{*}\mathrm{simPtr.get()}$

Note: ComponentTypesRegistration does not override SimulationCreated, so this call has no effect

67

![](images/6e66f22bf1b5e3bac36b5779f46c5b1dcbca25f12ad369b7e31324d08d61717d.jpg)

# UNCLASSIFIED AFSIM插件&扩展

# AFSIM mission 启动顺序

![](images/5e6613f645baa1ae13ef3de1ad32d0e3c9c7202e8085ef3826bcebaad9fab712.jpg)

![](images/7161fde6f3262f980872a301e404d02a7a46502b5f3da3569bc0da1fb032eba3.jpg)

Mission通过执行以下代码初始化 Simulation:

app.InitializeSimulation(simPtr.get())

- InitializeSimulation 调用: aSimPtr->Initialize()

：

- 下一步, WsfSimulation::Initialize 调用:

WsfObserver::SimulationInitializing(this)

- 这会通知所有注册的事件观察者，模拟即将被初始化

注意：Interfaced 类没有重写此方法，因此我们对通知不做任何处理。

![](images/ff64968434e59505dd12365fa26b06c99701efc364e94dc503aecdc622389847.jpg)

Mission通过执行以下代码初始化 Simulation:

app.InitializeSimulation(simPtr.get())

- InitializeSimulation 调用: aSimPtr->Initialize()

中

- 下一步, WsfSimulation::Initialize 调用: Initialize() 在所有的仿真扩展上

- 此练习没有定义模拟扩展，因此这没有任何效果

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19.

Other requests for this document shall be referred to AFRL/RQQD.

69

![](images/14e05c1cca9d335938d55c796feb36c5e407d36d8c4d91669a32c5e3d6dc5034.jpg)

# AFSIM插件&扩展

# AFSIM mission 启动顺序

![](images/0480d5ce912aa765cf08d793764877cda4d746f5353d659e26f024a1dea28452.jpg)

![](images/21315989bab37b66689ffabe9fd6fb87001ba8cbe684043c2a199cfb9c662635.jpg)

Mission通过执行以下代码初始化 Simulation:

app.InitializeSimulation(simPtr.get())

- InitializeSimulation 调用: aSimPtr->Initialize()

：

- 下一步, WsfSimulation::Initialize添加所有可用的平台到平台列表中

![](images/5201b73cd755a0cd05ee64f6361e7c3f3a0a2b03bb111af4f3b160f43b11788b.jpg)

Mission通过执行以下代码初始化 Simulation:

app.InitializeSimulation(simPtr.get())

- InitializeSimulation 调用: aSimPtr->Initialize()

：

- 然后, WsfSimulation::Initialize在每个平台（和其组件）上调用Initialize

- WsfPlatform::Initialize 对每个平台的组件调用PreInitialize 当前还没有被ShieldComponent重写

71

![](images/bb09f58d56e32f06f3ceef403cc389775f39df5b016149b13547ad836c146d13.jpg)

# UNCLASSIFIED

# AFSIM插件&扩展

# AFSIM mission 启动顺序

![](images/f1623f65c599f8bfc4930cd0b1f2d696b4db0ccac3f1dc94c1eccdde58ecf283.jpg)

![](images/d2ab1ef234be0b2da9a8d46ff30a7ce6ba0eb6f38c17aa6c577ecaf6a26e38b1.jpg)

Mission通过执行以下代码初始化 Simulation:

app.InitializeSimulation(simPtr.get())

- InitializeSimulation 调用: aSimPtr->Initialize()

：

- 然后, WsfSimulation::Initialize对每个平台（和其组件）调用Initialize

- 然后, WsfPlatform::Initialize() 调用ShieldComponent::Initialize()

- 将 MessageReceived 确定为在通过通信链接接收到消息时要调用的方法

![](images/f4dbc7025fb9f2e328272561873e23932a50337bdcb7e5175490b39196726c9b.jpg)

Mission通过执行以下代码初始化 Simulation:

app.InitializeSimulation(simPtr.get())

- InitializeSimulation 调用: aSimPtr->Initialize()   
：  
- 最后, WsfSimulation::Initialize 设置仿真状态为 cPENDING_START

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQQD.

73

![](images/09a135abc46694569683b9db5b4697019ff4203c146bc86ab3b1676c444db0ab.jpg)

# UNCLASSIFIED AFSIM插件&扩展

# AFSIM mission 启动顺序

![](images/d73a0d79f32e72fa2e7384d0afabb4b93cf0be9bbfe75657e494d73b55f13761.jpg)

![](images/6da639e9b8435e945b7d40cd76c82960b72a00fd92ce904781c190b3fb5d1888.jpg)

Mission调用如下语句开始仿真循环：

app.runEventLoop(simPtr.get(), options)

- RunEventLoop 调用: aSimPtr->Start()

- WsfSimulation::Start

- 调用每个仿真扩展的Start()

- 此练习没有模拟扩展，因此这没有任何效果。

![](images/fc3c6e1138b768fd40d897381300fca50c2a73892b1e284bffcce966efdf2a1c.jpg)

Mission调用如下语句开始仿真循环:

appRUNEventLoop(simPtr.get(), options)

- RunEventLoop 调用: aSimPtr->Start()

：

- 循环直到仿真完成

- 执行：aSimPtr->AdvanceTime()

- 将时间推进到下一个事件时间，  
- 触发计划中的模拟事件或下一个时间。

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19.

Other requests for this document shall be referred to AFRL/RQQD.

75

![](images/f27e37a6e6b17176a7f365de9ef00bc701e1abacd1a2969da1d69ca4a9f5c298.jpg)

# UNCLASSIFIED

# 练习2

![](images/7731c5e8255b224abc2751a134494866163472d6686f4d27f140c3e573b8f43c.jpg)

- 理解组件角色  
- 理解 WsfSensorComponent、WsfPlatformPart 和 WsfArticulatedPart  
- 理解 GetComponentRoles 和 QueryInterface 的目的

- 角色通常定义模拟组件列表中的服务或其他类型。  
- 角色通常定义平台组件列表中的类型，例如传感器、通信、移动器、处理器等。  
- 此外，为每个组件和部分类型在全局和有时在本地级别定义了组件角色枚举，以支持组件列表中的 FindComponentByRole 功能。  
- 每个需要额外角色的项目都会在其自己的项目中添加到全局组件角色枚举中。  
- 在全局上下文中添加角色确实需要在多个项目之间进行冲突解决，以避免角色的重复定义。

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

77

![](images/6fd6ca6165df38399d433f7241b9ec30c4a2e3d7c2720faf924252bdc98ea000.jpg)

# 组件练习2—检视1

![](images/f2c17f91a9ba0adb0578532bde052bd8a634f3890d73f3def8768f424dc45b82.jpg)

检查ComponentRoles.hpp

```txt
enum  
{cWSF_COMPONENT_SHIELDS = 1234567, cWSF COMPONENT_LATINUM = 1234568, cWSF Component_CYBER_SENSORYEFFECT = 654321}； 
```

这些组件角色被添加到  
WsfComponentRoles.hpp中定义的组件角色列表中。

- 组件角色必须具有唯一编号，以便将其与其他组件角色区分开。  
- 请参阅 WsfComponentRoles.hpp 以获取预定义的角色

enum   
{ cWSF_COMPONENTPLATFORM $= 1$ , cWSF_COMPONENTPLATFORM_PART $= 2$ , cWSF Components ARTICULATED_PART $= 3$ , cWSF Component MOVER $= 4$ $\vdots$ cWSF Component Sensor $= 9$ $\vdots$ }

在 WsfComponentRoles.hpp中预定义了许多组件角色。

- 角色由 WsfComponentList 使用。

- 请参阅 WsfComponent::QueryInterfaceT 以了解如何查询组件角色的有效性。

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQQD.

- 在文件 CyberSensorEffect.hpp 中，注意到类 CyberSensorEffect 继承自

WsfSensorComponent，它是传感器的一个组件，而传感器又是平台的一个组件。

```txt
class CyberSensorEffect : public WsfSensorComponent
{
    ...
} 
```

- 在文件ShieldComponent.hpp中，注意到类ShieldComponent继承自WsfPlatformPart，而WsfPlatformPart又继承自WsfPlatformComponent，它是平台的一个组件。

```txt
class ShieldComponent : public WsfPlatformPart { ... } 
```

- 在文件 LatinumComponent.hpp 中，注意到类 LatinumComponent 继承自 WsfPlatformComponent，它是平台的一个组件。

```txt
class LatinumComponent : public WsfPlatformComponent, public WsfObject   
{ DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQQD. 
```

79

![](images/c9950ffd3f99604d698edf321f196be03a4965ef222bc5bd1d64966c0af75c99.jpg)

# UNCLASSIFIED

# 组件练习2—检视3

![](images/70443f392f17ddb586aa224b25c7aa8fca288366da9b3daef10b7ca56b3aee64.jpg)

- ShieldTypes 和 LatiniumTypes 是完整的类型，因此可以用来创建 ShieldComponent 和 LatinumComponent。  
- 在文件ShieldTypes.hpp中，注意到类ShieldTypes继承自WsfObjectTypeList<ShieldComponent>，因此它是ShieldTypes的完整类型列表，并被添加到场景的类型列表中。

```typescript
class ShieldTypes : public WsfObjectTypeList<ShieldComponent> { } 
```

- 在文件 LatinumComponent.hpp 中，注意到类 LatinumTypes 继承自 WsfObjectTypeList<LatinumComponent>，因此它是 LatinumTypes 的完整类型列表，并被添加到场景的类型列表中。

```txt
class LatinumTypes : public WsfObjectTypeList<LatinumComponent> {
    ...
} 
```

![](images/0f3a9f8b4c4d703c5fc1e9a9e9ef60ea2e128730a03681bdf9c671e0292d092b.jpg)  
类型和组件

![](images/aa51073937e45c3b0fa763d4635feff4457d9b65fd04e5a7128cf6b644de402e.jpg)  
类型和组件

"enterprise"平台包含一个组件列表

CyberSensorEffect是由“全视”WsfSensor创建的，在它被添加到平台并调用

CyberSensorComponentFactory::ProcessInput后。

ProcessInput 然后创建一个新的 CyberSensorEffect 对象，将其插入传感器的组件列表中，并处理其场景命令。

CyberSensorEffect 是一个传感器组件（而不是类型），并且 CyberSensorComponentFactory 已在场景中注册。

![](images/faee92bdfd21c3a875ed5c973612dd1e34ee701595aef4b5e82ee3a44e1cac7c.jpg)

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19.

Other requests for this document shall be referred to AFRL/RQQD.

由于这三个类 CyberSensorEffect、ShieldComponent 和

LatinumComponent 都是组件，我们必须将它们声明为组件。

任务 1a: 使用 WSF_DECLAREComponent ROLE_TYPE 宏来注册在 ComponentRoles.hpp 中定义的盾牌组件。

- WSF_DEDECLARE_COMPONENT ROLE_TYPE 宏的输入包括：类的名称 (ShieldComponent)，以及组件角色编号(cWSF Component SHIELDS)，将宏调用放在 ShieldComponent 类声明之后。

任务1b：同样，注册LatinumComponent的类型。

任务 1c: 同样,注册 CyberSensorEffect 的类型。

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

# UNCLASSIFIED

# 组件练习2—任务1解决方案

83

![](images/2c0ca8d6d0f05929179edc20aa0dafbe62fd1f2c23ac8ffbc83c726c39d91e8c.jpg)

![](images/88bda053150eb75a9eead9e31f619d8306fc7d8790d42104913249bd08425e98.jpg)

File:ShieldComponent.hpp

class ShieldComponent : public WsfPlatformPart

$\left\{  \begin{array}{ll} {10} & 2 \times  {25} \\  {10} & 3 \times  {25} \end{array}\right.$

中

}；

class WsfScriptShieldComponentClass : public WsfScriptPlatformPartClass { ... };

// EXERCISE 2 TASK 1a

// Register the shield component type using macro defined in WsfComponentRoles.hpp

WSF.Declare_component_TYPE(ShieldComponent, cWSF Component SHIELDS)

File: LatinumComponent.hpp

class LatinumComponent : public WsfPlatformComponent,

public WsfObject

$\left\{  \begin{array}{ll} {10} & 2 \times  {25} \\  {10} & 3 \times  {25} \end{array}\right.$

中

[\} ;]

class WsfScriptLatinumComponentClass : public UtScriptClass { ... };

class LatinumTypes : public WsfObjectTypeList<LatinumComponent> { ... };

// EXERCISE 2 TASK 1b

// Register the latinum component type using macro defined in WsfComponentRoles.hpp

WSF.Declare_component ROLE_TYPE(LatinumComponent, cWSF Component_LATINUM)

File: CyberSensorEffect.hpp

class CyberSensorEffect : public WsfSensorComponent

f

1

：

// EXERCISE 2 TASK 1c

// Register the sensor cyber effect component type using macro defined in WsfComponentRoles.hpp

WSF.Declare_component ROLE_TYPE(CyberSensorEffect, cWSF Component CyBER SENSOR_EFFECT)

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19.

Other requests for this document shall be referred to AFRL/RQQD.

- 检查并理解来自 WsfComponentRoles.hpp 的这些方法

```cpp
template<class T> struct WsfComponentRole {
    template<class U> struct always_true::std::false_type {};
    static_assert(always_true<T>::value, "Type has no component role registered. Use the WSF_DECLARE Component_TYPE macro to register the type.");
};
#define WSF_DECLARE Component_TYPE_TYPE(TYPE, ROLE) template<class> std::integral_constant<int,ROLE>
{
    static_assert(std::is_base_of<WsfComponent, TYPE>::value, "Cannot register component role for type that does not derive from WsfComponent");
    static_assert(value > 0, "Component role must be > 0");
};
template<class T> struct cCOMPONENT ROLE {
    constexpr operator int() const noexcept{return WsfComponentRole<T>::value; }
}; 
```

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

85

![](images/30957f2caba00e98a13dfd7fb21108a85bdf11d4a32f8c262fb42595fcc4cd5d.jpg)

UNCLASSIFIED

# 组件练习2—检视5

![](images/e4d634d296407fa51ae9e8ad60371ff76e38309ff840ee8dccba40ccd47e3f79.jpg)

- 检视和理解WsfComponent.hpp中的接口

```cpp
class WsF exports WsfComponent
{
public:
    virtual ~WsfComponent() = default;
    ;
    virtual WsfComponent* CloneComponent() const = 0;
    ;
    virtual WsfstringId GetComponentName() const = 0;
    ;
    virtual const int* GetComponentRoles() const = 0;
    ;
    virtual void* QueryInterface(int aRole) = 0;
    ;
    virtual int GetComponentInitializationOrder() const { return 0; }
    template<typename T> bool QueryInterfaceT(T& aRolePtr) {
        aRolePtr = static_cast<T>(QueryInterface(cCOMPONENT ROLE<T>));
        return aRolePtr != nullptr;
    }
    bool ComponentHasRole(int aRole) { return QueryInterface(aRole) != nullptr; }
    virtual bool PreInitialize(double aSimTime);
    virtual bool Initialize(double aSimTime);
    virtual bool Initialize2(double aSimTime);
    virtual void PreInput();
    virtual bool ProcessInput(UtInput& aInput); 
```

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19.

Other requests for this document shall be referred to AFRL/RQQD.

• QueryInterface 方法是一个必需的虚拟函数，允许查询角色。

- 它要求同时定义 GetComponentRoles 方法，以便可以查找角色以验证其是否对给定组件有效。

- 在这个练习中，QueryInterface 被组件的组件工厂的 ProcessInput 方法利用，用于在平台上查找现有的该类型组件，或者在该类型组件尚不存在时创建一个新的该类型组件。

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQQD.

# UNCLASSIFIED

# 组件练习2—检视6

87

![](images/9ef799f759a64c462e5c43ddad8ad3e2885b9766ea465b34038ff9223c16bcb8.jpg)

![](images/ea297f5d80b5432b0f283b314ed07f04239c1aad8826b32749467d67ea70280c.jpg)

- 检视和理解WsfComponent.hpp中的如下方法

```cpp
template <typename PARENT_TYPE>
class WsfComponentT : public WsfComponent
{
public:
    typedef PARENT_TYPE ParentType;
WsfComponentT()
    : mParentPtr(nullptr)
} WsfComponentT(const WsfComponentT& /* aSrc */)
    : mParentPtr(nullptr)
} WsfComponentT& operator=(const WsfComponentT& /* aSrc */)
{ mParentPtr = nullptr; return *this;
} ~WsfComponentT() override = default;
virtual void ComponentParentChanged(ParentType* aParentPtr) { }
ParentType* GetComponentParent() const { return mParentPtr; } 
```

这个类的工作是跟踪组件的父对象。

- 检视和理解WsfComponent.hpp中的方法

```txt
void SetComponentParent(ParentType* aParentPtr)  
{  
    mParentPtr = aParentPtr;  
    ComponentParentChanged(aParentPtr); // Inform of change of parent  
}  
private:  
    ParentType* mParentPtr;  
};  
//! A convenient typedef for a platform component.  
using WsfPlatformComponent = WsfComponent<T<WsfPlatform>;  
这个声明创建了一个定义，使得平台本身可以成为一个平台组件。
```

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

89

![](images/951974b17eaf331a20bfb0c35c6e76792c1970279e1d56d7603692cf7c7732b6.jpg)

UNCLASSIFIED

# 组件练习2—检视7

![](images/db983abf7f7ff16827d53f5720a4636da7afc518e20330968e4539e8c21e3f4f.jpg)

- 检视和理解其它核心类

```txt
class WsfSensorComponent : public WsfComponentTWsfSensor> { ... };   
class WsfPlatformPart : public WsfPlatformComponent .. { ... }; 定义 WsfSensorComponent为 WsfSensor的一个组件。   
定义 WsfPlatformPart 为 WsfPlatformComponent （即，平台的一个组件）。   
class WsfArticulatedPart : public WsfPlatformPart ... { ... }; 定义 WsfArticulatedPart 为 WsfPlatformPart 的扩展。
```

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

- 检查并理解来自CyberSensorEffect.cpp的这些方法。

```cpp
WsfComponent* CyberSensorEffect::CloneComponent() const { return new CyberSensorEffect(*this); } WsfstringId CyberSensorEffect::GetComponentName() const { static WsfstringId id = "WSF_CYBER_SENSOR_EFFECT"; return id; } 
```

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

91

![](images/38b9bf1399ca844a29fde7551fd2f04e2eafb418257f7425615a80e7adec3444.jpg)

# UNCLASSIFIED 组件练习2—任务2

# CyberSensorEffect.cpp

![](images/e36f6cb6f29533bae9aa182b6a6850b0f1a21448b3bb2ee42afd00015550bfd1.jpg)

- 完成 CyberSensorEffect::GetComponentRoles 方法。

- 将角色集定义为一个静态整数数组。  
初始化该数组，使其包含：

- 'this' 组件角色  
(cWSF_COMPONENT_CYBER_SENSOR_EFFECT)、  
- 传感器 (cWSF_COMPONENT_SENSOR) 和  
- 空组件 (cWSF_COMPONENT_NULL)。

```cpp
const int* CyberSensorEffect::GetComponentRoles() const  
{ // EXERCISE 2 TASK 2 // Define the set of roles as a static array of ints. // Initialize this array to consist of 'this' component role // (cWSF ComponentcyBER_SENSORY_EFFECT), sensor (cWSF ComponentSENATOR), // and the null component (cWSF Component NULL).  
static int roles[] = { cWSF ComponentCYBER_SENSORY_EFFECT, cWSF Component SENSOR, cWSF Component NULL };  
return roles; 
```

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

93

![](images/27329915e2f21433c7ab1129d3dfec72e1a32cd759f1cf138ac391e579e52b1b.jpg)

# QueryInterface 使用

![](images/af0f201eb95eb88936fda4fd338864956294606b9aeca5d4f5ac5a35dea0373d.jpg)

- QueryInterface 是 WsfComponent 中的一个纯虚拟方法。

- 它必须在任何直接继承 WsfComponent 的类中被重写（否则会出现编译错误）。  
- 然而，在任何派生类中重写它实际上是一个要求。  
- 因此，由于CyberSensorEffect继承自 WsfComponent，而WsfComponent又继承自WsfComponent，所以它应该重写QueryInterface。

- QueryInterface 应返回一个指向其所属对象的指针。

- 这个指针应该被强制转换为由传入的 aRole 整数参数所指示的对象类型。

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

- 任务3：完成CyberSensorEffect::QueryInterface方法。

- QueryInterface 应返回指向当前对象（即 this）的指针，该指针的类型由参数 aRole 指定。  
- 根据给定的角色 aRole 返回正确类型的指针。

- 角色 cWSF_COMPONENT_CYBER_SENSOR_EFFECT 意味着你应该返回 this。  
- 角色 cWSF Component Sentence 意味着你应该返回 this，并将其静态转换为 WsfSensorComponent*。

- 如果 aRole 中给定的角色不被 GetComponentRoles 支持，或者是 cWSF_COMPONENT_NULL，则返回零（nullptr）。

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

95

![](images/659d516c51abfad258b5a7e9caefe6307776ad0f1bb3070bfc20d8b7ebd2618f.jpg)

# UNCLASSIFIED 组件练习2—任务3解决方案

# CyberSensorEffect.cpp

![](images/6295366e05ba35503b1e785e6c9df6abcbcb02bb8b78225d1abf797ca088acac.jpg)

void\* CyberSensorEffect::QueryInterface(int aRole)   
{ //EXERCISE 2 TASK3 //Return a properly cast pointer according to the given role. //If the given role is not one supported by GetComponnntRoles // (or if it is cWSF Component NULL), return zero. if(aRole $= =$ cwSF ComponentcyBER_SENSOR_EFFECT) { return this; } if(aRole $= =$ cwSF Component SENSOR) { return(static_cast<WsfSensorComponent $\text{串}$ >(this)); } return nullptr;

- 检视和理解CyberSensorEffect.cpp中的方法

```cpp
//   
/// Find the instance of this component attached to the specified sensor. CyberSensorEffect* CyberSensorEffect::Find(const WsfSensor& aParent)   
{ CyberSensorEffect* componentPtr(nullptr); aParent.Components().FindByRole<CyberSensorEffect>(componentPtr); return componentPtr;   
}   
//   
/// Find the instance of this component attached to the specified processor,   
/// and create it if it doesn't exist. CyberSensorEffect* CyberSensorEffect::FindOrCreate(WsfSensor& aParent)   
{ CyberSensorEffect* componentPtr = Find(aParent); if (componentPtr == nullptr) { componentPtr = new CyberSensorEffect; aParent.Components().AddComponent(componentPtr); } return componentPtr; 
```

注意：如果一个组件在传感器的组件列表中，则 FindByRole 将导致对该组件的 QueryInterface 方法的调用。

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

97

![](images/80c8c0b4610dbfa64e83de3b747bd8160d055f9143a814f7f77868207ffb9dba.jpg)

# UNCLASSIFIED

# 想定文件

![](images/959fb889f9fb3edee388d3267fb1f84d738063112088ab5fdad2554788b8a28f.jpg)

processor unsecured_computer WsF-scriptPROCESSOR on_message default script string command $=$ MESSAGE.SubType(); if (command $\equiv$ "DROPTRACK") { WsfSensor s $=$ PLATFORM.Sensor("all Seeing"); s.SetAuxData("BEGIN_EXPLOIT",true); //show } end_script end_on_message end Processor 1 脚本平台form enterprise Enterprise end platform

脚本方法 Sensor 必须找到“all Seeing”传感器（该传感器会搜索平台的组件列表，对每个组件调用 QueryInterface，直到找到一个名称为“all seeing”的 WsfSensor）。

// should be able to communicate directly with component

脚本方法 Sensor 仅扫描平台的组件列表，而不扫描 WsfSensor 组件列表。因此，它不会调用 CyberSensorEffect::QueryInterface 方法。  
然而，我们仍然应该定义 CyberSensorEffect::QueryInterface 方法，因为可能会有其他函数或脚本方法最终扫描传感器的组件列表。

- 检查并理解 LatinumComponent 类中的这些方法。  
```cpp
class LatinumComponent : public WsfPaltformComponent, public WsfObject   
{ WsfstringId GetComponentName() const override { returnGetNameId(); } };   
// virtual WsfComponent\* LatinumComponent::CloneComponent() const   
{ return new LatinumComponent(\*this);   
} 
```

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

99

![](images/7f87fac1eea3c5a356653708b055dbfcc711ea45770fd81f5e6bd7317274af18.jpg)

# UNCLASSIFIED 组件练习2—任务4

# LatinumComponent.cpp

![](images/d874e71d40afe9e6a0d6c874cc8aa3cdd7c37d00b991183afb571b2b2af42c12.jpg)

- 完成 LatinumComponent::GetComponentRoles 方法。

- 将角色集定义为一个静态整数数组。  
初始化该数组，使其包含：

- 'this' 组件角色 (cWSFCOMPONENT_LATINUM),  
- 空组件(cWSFCOMPONENT_NULL)。

const int \* LatinumComponent::GetComponentRoles() const   
{ //EXERCISE 2 TASK4 //Define the set of roles as a static array of ints. //Initialize this array to consist of 'this' component role // (cWSF ComponentLATINUM), and the null component (cWSF ComponentNULL). static const int roles[] $=$ { cWSF ComponentLATINUM, cWSF ComponentNULL }; return roles;

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

![](images/d5a968cb51a37a02c8f7afffb6d051eafae589c7dca6f0d311b405c8835f4452.jpg)

# UNCLASSIFIED 组件练习2—任务5 LatinumComponent.cpp

101

![](images/25ade4036d2cba24aad98361924c8457922f8ac513aacb79636a177a4a3c45f7.jpg)

• QueryInterface 应返回指向当前对象（即 this）的指针，该指针的类型由参数 aRole 指定（在返回之前可能需要将其强制转换为正确的类型），如果对象不是

GetComponentRoles 支持的任何类型，则返回空指针（nullptr）。

- 任务 5: 完成 LatinumComponent::QueryInterface 方法

根据给定的角色返回正确类型的指针：

- 如果角色是 cWSFComponent_LATINUM, 则返回 this。  
- 如果给定的角色不是 GetComponentRoles 支持的角色（即，不是 cWSF ComponentALATINUM），则返回零（nullptr）。

```cpp
// virtual
void* LatinumComponent::QueryInterface(int aRole)
{
    // EXERCISE 2 TASK 5
    // Return a properly cast pointer according to the given role.
    // If the given role is not one supported by GetComponentRoles
    // (or if it is cWSF Component NULL), return zero.
    if (aRole == cWSF Component_LATINUM)
        {
            return this;
        }
    return nullptr;
} 
```

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

103

![](images/6107069dfa961e716e6ca2cf8a79efbada0ed3fbfdb468fac5116feef8c419bd.jpg)

# QueryInterface 使用

![](images/77a33cf2bc85d823b59c6e8d7881c88d86a037b2190273911e6788563019741d.jpg)

- LatinumComponent::QueryInterface 在模拟执行过程中被多次调用。

- 一旦 LatinumComponent 被创建并添加到“enterprise”平台，任何尝试查找平台组件的操作都会扫描平台的组件列表，这会对列表中的每个组件（包括 LatinumComponent）调用 QueryInterface，以查看它是否是正在搜索的组件。

- 当ProcessInput添加新组件到列表时，也会发生这种情况，因为它必须首先扫描列表以查看是否已经存在该类型的组件。  
- 此外，当执行 LatinumComponent 的脚本方法“Latinum”时，也会发生这种情况，因为它必须找到该组件并返回指向它的指针。

- 深入并理解 LatinumComponent.cpp中的这些方法

//   
/// Find the instance of this component attached to the specified sensor. LatinumComponent\* LatinumComponent ::Find(const WsfPlatform& aParent)   
{ // Exercise 2 Review 4 (understand) LatinumComponent\* componentPtr $\equiv$ nullptr; aParent.GetComponents().FindByRole<LatinumComponent>(componentPtr); return componentPtr;   
}   
//   
/// Find the instance of this component attached to the specified processor,   
/// and create it if it doesn't exist. LatinumComponent\* LatinumComponent::FindOrCreate(WsfPlatform& aParent)   
{ // Exercise 2 Review 4 understand LatinumComponent\* componentPtr $\equiv$ Find(aParent); if (componentPtr $= =$ nullptr) { componentPtr $\equiv$ new LatinumComponent(); aParent.AddComponent(componentPtr); } return componentPtr;

}注意：如果一个组件在平台的组件列表中，则FindByRole将导致对该组件的QueryInterface方法的调用。

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQQD.

105

![](images/d4a3bcbb69bc39399bb3a5602c09a8a1a7249343492c14ab3fb7c189eea5601e.jpg)

# UNCLASSIFIED 创建 LatinumComponent 使用 FindOrCreate

![](images/ddae3aa9690661a85a36ef2ea7ae2a90a4acafcb09cb7715432b65aeb1318d8b.jpg)

![](images/1d1b55c0aed96c6996e0bdddbc85f6ff1ad0e4232f03595afaab1ae60be3ef84.jpg)

add processor transport_latinum WsF-scripttPROCESSOR 脚本方法 Latinum 必须找到"latinum"组件 update_interval 0.1 s （该方法会搜索平台的组件列表，对每个 on_update // check to see if the shields are down WsfPlatform enterprise $=$ WsfSimulation.FindPlatform("ent) Shields shields $=$ enterprise/Shields(); if(! shields.IsTurnedOn())// We can do this because of inheritance of shields from WsfPlatformPart { enterpriseCOMMENT("Shields Down"); static bool beamLatinumNow $=$ true; WsfDraw draw $= \{\}$ . static double downTime $=$ TIME NOW; if (beamLatinumNow) { writeIn("Enterprise shields down"); PLATFORM COMMENT(TIME NOW, "Steing Latinum"); Latinum latinum $=$ enterprise.Latinum(); latinum.TransformTo(PLATFORM); if (PLATFORM.Latinum().IsValid()) { writeIn("Latinum now on Ferengi Ship: ", PLATFORM.Latinum().Quantity()); } beamlatinumNow $=$ false; } if (TIME NOW < (downTime + 10)) { draw.Erase(1); $\vdots$ draw.End(); }

```txt
DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD. 
```

107

![](images/b461121fd9c508a57ac550f929196aa0838f95a107ccc1d77e7bf9df830f5bec.jpg)

# 当脚本接口调用 Latinum 脚本方法时。

![](images/1da2308680246de797142b461e38c045e5b3688a7108c0553bdc9df1e3d15d63.jpg)

![](images/a2c8c3ef85ab6b3ffe496baa734f3afe6ed22020ee6f4d24dcaadba7f9d060fc.jpg)

Latinum 脚本方法被添加到 WsfPlatform 对象中，因此 aObjectPtr 指向“enterprise” WsfPlatform 对象。

GetComponent 调用 FindComponentByRoleP，该方法在组件列表中的每个组件上调用 QueryInterface，以查看它是否是正确的类型。当 FindComponentByRoleP 在平台上找到 LatinumComponent 时，它返回指向该组件的指针，随后 GetComponent 将该指针返回给 Latinum 脚本方法。然后，Latinum 脚本方法将此指针返回给脚本方法的调用者。

- 检查ShieldComponent.hpp文件。

- 注意ShieldComponent继承自WsfPlatformPart，这是一个平台组件类型。  
- ShieldComponent 已经是一个组件，继承了 WsfPlatformPart 的功能，如 TurnOn、TurnOff、Degradation 等。  
- 注意 GetComponentName 的实现。

class ShieldComponent : public WsfPlatformPart   
public: explicit ShieldComponent(WsfScenario& aScenario); ShieldComponent(const ShieldComponent& aSrc); ShieldComponent& operator $\equiv$ (const ShieldComponent& aSrc); ~ShieldComponent() noexcept override $=$ default; bool Initialize(double aSimTime) override; //! @name Component infrastructure methods. //@{ Wsfstringld GetComponentName(） const override {returnGetNameId(); }

```txt
DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD. 
```

109

![](images/d2fc7427ad243bc311b9a9362a99ce573cdf706925d3e213e3fbaf2e8c3fcad3.jpg)

# UNCLASSIFIED

# 组件练习2—检视13

# ShieldComponent.cpp

![](images/61ee2975d21c53dc0f8d0fc98996f6b37201b34c61b4b1b17136d23c7e5d61cc.jpg)

# - 检查ShieldComponent.cpp

- 注意 WsfPlatformPart 构造函数将组件角色作为参数传递。

```cpp
ShieldComponent::ShieldComponent(WsfScenario& aScenario) : WsfPlatformPart(aScenario, cCOMPONENT ROLE<ShieldComponent>(); mUpdateInterval(-1.0), mInitialStrength(0.0), mRechargeRate(0.0), mStrength(0.0), mLastUpdateTime(0.0) { SetName("shields"); } // virtual WsfComponent* ShieldComponent::CloneComponent() const { return new ShieldComponent(*this); } 
```

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19.

Other requests for this document shall be referred to AFRL/RQQD.

# - 完成ShieldComponent::GetComponentRoles

- 定义角色集合为一个静态整型数组。  
- 将该数组初始化为包含以下内容：

- 'this' 组件角色 (cWSF Component SHIELDS),  
- 平台部分 (cWSFPLATFORM_PART),  
- 空组件 (cWSF_COMPONENT_NULL)。

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQQD.

111

![](images/72289922da0c7e93682590a574aaa619347a566a3f8207ac8b87049c0ae585af.jpg)

# UNCLASSIFIED 组件练习2—任务6解决方案

# ShieldComponent.cpp

![](images/5978b21403ec505ab8bdb86678c1e7a3470703039b85339e1ee1814850bc1317.jpg)

const int* ShieldComponent::GetComponentRoles() const { //EXERCISE2TASK6 //Define the set of roles as a static array of ints. //Initialize this array to consist of 'this' component role // (cWSF_COMPONENT_SHEIELDS), platform part (cWSF ComponentsPLATFORM_PART), // and the null component (cWSF Component NULL). static const int roles[] $=$ { cWSF Component_SHEIELDS, cWSF Component_PLATFORM_PART, cWSF Component_NULL }; return roles;   
}

- 任务3：完成ShieldComponent::QueryInterface方法

- QueryInterface 方法应返回一个指向当前对象（即 this）的指针，该对象的类型由参数 aRole 指定。

- 根据给定的角色返回正确类型的指针：

- 如果角色是cWSF_COMPONENT_SHIELDS，则返回this。  
- 如果角色是 cWSFPLATFORM_PART，则返回通过 static_cast 转换为 WsfPlatformPart* 类型的 this。  
- 如果给定的角色不是 GetComponentRoles 支持的角色，或者是 cWSF ComponentNULL，则返回零（nullptr）。

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

113

![](images/3ec42cbdb66a15de7566905cf20c285c6b479eb9ed98b70cba253e32d3284462.jpg)

# UNCLASSIFIED 组件练习2—任务7解决方案

# ShieldComponent.cpp

![](images/9e4d5accf758401682dbe6b994bf05d161261c72e104534b6803875de228a51b.jpg)

```cpp
void* ShieldComponent::QueryInterface(int aRole)  
{ // EXERCISE 2 TASK 7 // Return a properly cast pointer according to the given role. // If the given role is not one supported by GetComponentRoles // (or if it is cWSF Component NULL), return zero.  
if (aRole == cWSF Component_SHIELDS) { return this; } else if (aRole == cWSF ComponentPLATFORM_PART) { return (static_cast<WsfPlatformPart>(this)); } return nullptr; } 
```

• ShieldComponent::QueryInterface 在模拟执行过程中会被多次调用。

- 一旦ShieldComponent被创建并添加到“enterprise”平台后，任何尝试查找平台组件的操作都会扫描平台的组件列表。

- 这会对列表中的每个组件（包括ShieldComponent）调用QueryInterface，以检查它是否是正在搜索的组件。  
- 当执行ShieldComponent的脚本方法“Shields”时，也会发生这种情况，因为它必须找到该组件并返回指向它的指针。

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQQD.

115

![](images/3668fe095d215d19766b01aa2a48109d1fb4adf5ca21f08b766f20042c239d07.jpg)

# UNCLASSIFIED

# 想定文件

![](images/02b2e2b432f8714022562a5d16cdca5f63512eafe75118170b966dd35cb5e621.jpg)

add processor transport_latinum WSFScriptPTPROCESSOR

```txt
update_interval 0.1 s
on_update
// check to see if the shields are down
WsfPlatform enterprise = WsfSimulation.FindPlatform("enterprise");
Shields shields = enterprise/Shields();
if (!shields.IsTurnedOn()) // We can do this because of
{
enterpriseCOMMENT("Shields Down");
static bool beamLatinumNow = true;
WsfDraw draw = {};
static double downtime = TIME NOW;
if (beamLatinumNow)
{
writeln("Enterprise shields down.");
PLATFORM COMMENT(TIME NOW, "Stealing Latinum");
Latinum latinum = enterprise.Latinum();
latinum.TransformTo(PLATFORM);
if (PLATFORM.Latinum().IsValid())
{
writeln("Latinum now on Ferengi Ship: ", PLATFORM);
}
beamLatinumNow = false;
}
if (TIME NOW < (downTime + 10))
{
draw.Erase(1);
};
draw.End();
} 
```

脚本方法Shields必须找到"shields"组件（该方法会搜索平台的组件列表，对每个组件调用QueryInterface，直到找到一个ShieldComponent）。

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19.

Other requests for this document shall be referred to AFRL/RQQD.

![](images/264aec96cd9fd0f960f74e89c8654fe0e93effd3194f857dfdcd858ef165f466.jpg)

Shields 脚本方法被添加到

WsfPlatform对象中，因此aObjectPtr

指向“enterprise” WsfPlatform 对象。

GetComponent调用FindComponentByRoleP，该方法会对组件列表中的每个组件调用QueryInterface，以检查它是否是正确的类型。

当 FindComponentByRoleP 在平台上找到

ShieldComponent时，它会返回指向该组件的指针，随

后 GetComponent 将该指针返回给 Shields 脚本方法。

Shields 脚本方法随后将这个指针返回给调用该脚本方法的对象。

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19.

Other requests for this document shall be referred to AFRL/RQQD.

UNCLASSIFIED

![](images/b4f1de847eae06b6e1c27a047b73d1ad6e74f337713e3397b612a789aef8afa2.jpg)

# 练习3

117

![](images/d199c8f4add25d798b3eb512de47131b05ab24b581ef4bb58a1e9fd1467e1897.jpg)

- 理解组件工厂类的 ProcessInput 方法。  
- 完成CyberSensorEffect的ProcessInput和TrackerAllowTracking方法。

- 在CyberSensorEffect.cpp中，检查

CyberSensorComponentFactory 类。

- 这个工厂允许我们直接在传感器类型输入定义上创建和配置 CyberSensorEffect 实例。

- 检查 ProcessInput 方法，理解 Review 6 中的

FindOrCreate 方法是如何用来填充 CyberSensorEffect 指针的。

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

119

![](images/d9cb8a8f6a9ad966faafe5592adbc67fc1cec794e1d42dcb2b5a3b4612afa708.jpg)

# UNCLASSIFIED 组件练习3—检视1

# CyberSensorEffect.cpp

![](images/89ae76cebcb90607e2ff07aeb8671297e8e53adff37790e2f1d351a068bfaab5.jpg)

```cpp
class CyberSensorComponentFactory : public WsfComponentFactory<WsfSensor>   
{ public: bool ProcessInput(UtInput& aInput, WsfSensor& aParent) override { std::string command; aInput.GetCommand(command); bool myCommand = false; if (command == "cyber Effect") { CyberSensorEffect* cbePtr = CyberSensorEffect::FindOrCreate(aParent); aInput.ReadCommand commanded); if (command == "track_pulloff") { cbePtr->setType(CyberSensorEffect::cTRACK_PULLOFF); myCommand = true; } else if (command == "track_drop") { cbePtr->setType(CyberSensorEffect::cTRACK.Drop); myCommand = true; } return myCommand;   
} 
```

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19.

Other requests for this document shall be referred to AFRL/RQQD.

- 完成 CyberSensorComponentFactory::ProcessInput 方法（位于 CyberSensorEffect.cpp 文件中）：

- 对于 exploit_delay 命令，创建一个变量（类型为 double）来存储延迟时间。  
- 调用alInput.ReadValueOfType方法读取延迟值。

- ReadValueOfType 方法的格式如下：：

```txt
template<typename T> void ReadValueOfType(T& aValue, ValueType aValueType) 
```

- 第一个参数应是你创建的变量。  
- 第二个参数应是UtInput::cTIME，以指示读取的值是一个时间值。

- 使用CyberSensorEffect指针cbePtr，调用

CyberSensorEffect::SetExploitDelay 方法，并传入存储延迟时间的变量。

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

121

![](images/b38bbf4747b0e9322ab706aca839c34aa573b52e99594917c2b6db1ab043e480.jpg)

# UNCLASSIFIED

# 组件练习3—任务1解决方案

# CyberSensorEffect.cpp

![](images/3fce7e389561643b2406dbeeafe379c1f9567eec10109f9ab0dccf02b7c67a54.jpg)

```cpp
class CyberSensorComponentFactory : public WsfComponentFactory<WsfSensor>   
public: bool ProcessInput(UtInput& aInput, WsfSensor& aParent) override std::string command; aInput.GetCommand(command); bool myCommand = false; if (command == "cyber_EFFECT") { CyberSensorEffect* cbePtr = CyberSensorEffect::FindOrCreate(aParent); aInput.ReadCommand commanded); if (command == "track_pulloff") else if (command == "track_drop") else if (command == "exploit_delay") { // EXERCISE 3 TASK 1 // Create a variable which is a double, // use that variable to read in the time value (cTIME) from input, and // use that variable to set the CyberSensorEffect's exploit delay double delay; aInput.ReadValueOfType(delay, U_tInput::cTIME); cbePtr->SetExploitDelay(delay); } 
```

- 完成 CyberSensorEffect::TrackerAllowTracking 方法的实现。  
- 该方法由传感器跟踪器调用，以确定是否应停止跟踪。  
- 如果传感器已收到开始利用的命令，则信号表明跟踪器不应允许跟踪。

- 任务2：检查复合条件的值：

-A) 检查利用是否尚未发生，即检查 mExploitTime 是否小于零。  
-B) 并且检查传感器的辅助数据属性是否存在（称为BEGIN_EXPLOIT）。

- 调用 GetSensor()->GetAuxData().AttributeExists("BEGIN_EXPLOIT"), 该方法返回一个布尔值。

- 如果复合条件为真，则将利用时间 (mExploitTime) 设置为当前仿真时间 (mSimTime) 加上利用延迟时间 (mExploitDelayTime)。  
- 否则，不执行任何操作。

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

123

![](images/2d86397f1bf54d3220794ff121179ac91a69c1fd9fe7c7423fb3d1a8b2c40c27.jpg)

# 组件练习3—任务2解决方案

# CyberSensorEffect.cpp

![](images/bb3a69ab9237ed29ba9539ae7f18cabe44f2d6d2f1f66229a91d7aa3f8ed89fe.jpg)

```cpp
bool CyberSensorEffect::TrackerAllowTracking(double aSimTime, const TrackerSettings& aSettings, const WsfTrackId& aRequestId, size_t aObjectId, WsfTrack* aTrackPtr, WsfSensorResult& aResult)  
{ // If we've received a message // EXERCISE 3 TASK 2 // Signal that the tracker should not allow tracking if the sensor has received the command to begin the exploit // Check to see that the exploit is not already occurring (mExploitTime less than zero) // And check to see that the sensor's aux data attribute exists, called "BEGIN_EXPLOIT" // If so, set the exploit time to be the current sim time plus the exploit delay time (mExploitDelayTime). if ((mExploitTime < 0.0) && GetSensor()->GetAuxData().AttributeExists("BEGIN_EXPLOIT")) { mExploitTime = aSimTime + mExploitDelay; } return (aSimTime >= mExploitTime); } 
```

- 理解 LatinumComponent 组件工厂（位于

LatinumComponent.cpp 文件中）。

- ProcessAddOrEditCommand 方法负责在平台上创建或（可选）编辑组件。

- 在这种情况下，如果添加/编辑组件失败，该方法会返回 false。

```txt
class LatinumComponentFactory : public WsfComponentFactory<WsflPlatform> {
    public:
        bool ProcessAddOrEditCommand(UtInput& aInput, WsfPlatform& aPlatform, aIsAdding) override
        return false;
    }
}; 
```

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

125

![](images/2a712ce0eed2cdb14eddc9830f5d8fd4d4a4122061592132be069b69e4d3dd43.jpg)

# UNCLASSIFIED

# 组件练习3-检视2

# LatinumComponent.cpp

![](images/5b63049f00fcb0f3dd2d9d8904c23409efb0a317153e0bd88a9b68785b79b926.jpg)

- 理解 LatinumComponent 组件工厂（位于 LatinumComponent.cpp 文件中）。

- ProcessInput 方法负责处理输入中的 latinum 命令。

class LatinumComponentFactory : public WsfComponentFactory<WsflPlatform>   
public: 注意：组件工厂的 ProcessInput bool ProcessInput(UtInput& aInput, 方法会调用 WsfPlatform& aParent) override LatinumComponent::ProcessInput std::string command; 方法，以处理场景文件中的 aInput.GetCommand(command); bool myCommand $=$ false; if (command $= =$ "latinum") { LatinumComponent\* lPtr $=$ LatinumComponent::FindOrCreate(aParent); aInput.ReadCommand commanded); myCommand $=$ lPtr->ProcessInput(aInput); if (!myCommand) { throw Utlput::BadValue(aInput); } } return myCommand;   
}

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19.

Other requests for this document shall be referred to AFRL/RQQD.

- 理解ShieldComponent组件工厂（位于ShieldTypes.cpp文件中）。  
- ProcessAddOrEditCommand 方法负责在平台上创建或（可选）编辑组件。在这种情况下，它是一个未命名的组件，我们无法进行编辑。  
- ProcessDeleteCommand 方法处理相应的组件删除指令。

```cpp
class ShieldComponentFactory : public WsfComponentFactory<Wsflpform>   
public: bool ProcessAddOrEditCommand(UtInput& aInput, WsfPlatfom& aPlatfom, bool aIsAdding) override { ShieldTypes& types(ShieldTypes::Get(GetScenario()))); return types.LoadUnnamedComponentWithoutEdit(aInput, aPlatform, aIsAdding, cWSF_COMPONENT_SHIELDS); } bool ProcessDeleteCommand(UtInput& aInput, WsfPlatfom& aPlatfom) override { ShieldTypes& types(ShieldTypes::Get(GetScenario()))); return typesDeleteUnnamedComponent(aInput, aPlatform, cWSF_COMPONENT_SHIELDS); }; 
```

```txt
DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQQD. 
```

127

![](images/8d7970c973d177a07b6307438b16a6eb93733ddb8c698626c6d0becdf22baa46.jpg)

# UNCLASSIFIED

# 组件练习3-检视4

# ShieldComponent.cpp

![](images/f09c3e03a02e7e624adefd9fce1b624a7e9f2f63d74199053a1a7f46c11c9898.jpg)

- 检查ShieldComponent::MessageReceived方法。

- 注意，如果消息子类型是DROP_SHIELDS，该方法会关闭Shields平台部分。

void ShieldComponent::MessageReceived(double wsf::comm::Comm* aXmtrPtr, wsf::comm::Comm* aRcvrPtr, const WsfMessage& aMessage, wsf::comm::Result& aResult)   
{ std::string type $=$ aMessage.GetSubType(); if (type $= =$ "DROP_SHIELDS") { // RAI block auto out $=$ ut::log::info() $\ll$ "Turning off shield component."; out.AddNote() $\ll$ "T $=$ " $\ll$ aSimTime; out.AddNote() $\ll$ "Platform:" $\ll$ GetPlatform()->GetName(); out.AddNote() $\ll$ "Shield:" $\ll$ 名GetName(); } GetPlatform()->GetSimulation()->TurnPartOff(aSimTime, this); }