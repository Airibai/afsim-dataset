# UNCLASSIFIED AFSIM插件与扩展

# AFSIM 任务启动序列

![](images/db3fc692ff568c12a8dcf9f37e3c71f45e1e38aab7a83ad3e4d27c656ac7165e.jpg)

![](images/d3d44246dceb3564fd1e3afc929ea77357ca04cd7069225e02ecec72c45f90d2.jpg)

Mission通过执行以下代码创建仿真：

app.InitializeSimulation(simPtr.get())

- InitializeSimulation 调用: aSimPtr->Initialize()

：

- 下一步, WsfSimulation::Initialize 调用: Initialize()在所有的仿真扩展当中

- 接着调用 CommLab::Interface::Initialize()

![](images/7c83b6c7ef1675b6dc793b472c0813016fcbb2dce449d53f572097d5199c9c8e.jpg)

Mission通过执行以下代码创建仿真:

app.InitializeSimulation(simPtr.get())

- InitializeSimulation 调用: aSimPtr->Initialize()

：

- 下一步, WsfSimulation::Initialize将所有可用平台添加到平台列表当中  
- 最终, WsfSimulation::Initialize 将仿真状态置为 cPENDING_START

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQQD.

63

![](images/cc3bdc00d480f86469c0e0c6677de607e797a04aaa69c2abe262836c248e3bc7.jpg)

# AFSIM插件与扩展

# AFSIM 任务启动序列

![](images/3577150bb4305a739dd46ea91908560142099840408ed4cebad210059dadad41.jpg)

![](images/7f2e18c968d2367d933ac79e2cd9ecd1e87d9e13b7cf15d6a22c9799aac77447.jpg)

Mission使用以下代码运行仿真：

appRUNEventLoop(simPtr.get(),options)

- RunEventLoop 调用: aSimPtr->Start()

- WsfSimulation::Start

- 对于每个仿真扩展调用 Start()

- 调用CommLab::Interface::Start()

- 设置低级DIS接口以进行通信

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19.

Other requests for this document shall be referred to AFRL/RQQD.

![](images/88753abd49d9fbe7ab5dd597a81934bcf18b72217049f0baa28879a693ef132e.jpg)

Mission使用以下代码运行仿真:

appRUNEventLoop(simPtr.get(), options)

- RunEventLoop 调用: aSimPtr->Start()

：

- 循环直到仿真完成

- 执行：aSimPtr->AdvanceTime()

- 将时间推进到下一个事件时间，  
- 触发为下一个事件时间安排的仿真事件。

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19.

Other requests for this document shall be referred to AFRL/RQQD.

65

![](images/7dd64d672f87eba87fa439eb206c7ab9b78c418da5bb05784b8b02572a5a5bea.jpg)

# UNCLASSIFIED

# 练习2

![](images/f66cef9bbebc7b1a532fc1a28ccb7c5c8c50847ccc978c8d57f50adaede50d01.jpg)

- 完成场景扩展 SignalCommRegistration::ProcessInput,  
- 完成 Interface::ProcessInput,   
- 审查 Interface 仿真扩展的 Initialize 和 Start 方法。

- 通过调用原型 CommLab::Interface 的 ProcessInput 方法来完成 SignalCommRegistration::ProcessInput 方法:

- 使用成员变量 mPrototypicalInterface 来调用 ProcessInput。  
- 确保将对 mPrototypical Interface 的 ProcessInput 调用的结果返回给 SignalCommRegistration::ProcessInput 的调用者。

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

67

![](images/b27d5f259d4bf76ae8fe7e639cf8cd7dc9af3b0ba2d7fac0e8bbe368e2f8adc6.jpg)

# Comm Exercise 2 — Task 1 Solution

# SignalCommRegistration.hpp

![](images/a5234da6191529ba02e97471b7c4c72676672e6e6d85c58e548fb6f7638870d3.jpg)

class SignalCommRegistration : public WsfScenarioExtension   
{ public: SignalCommRegistration() $=$ default; bool ProcessInput(UtInput& aInput) override { //EXERCISE2TASK1 //!Call the CommLab::Interface prototype's ProcessInput method. return mPrototypeInterface.ProcessInput(aInput); } private: CommLab::Interface mPrototypeInterface; };

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQQD.

- 检查 CommLab::Interface 类以熟悉该类的方法和属性。

- CommLab::Interface 将作为 WsfSimulationExtension 实现。  
- Initialize 方法由仿真自动调用。  
- ProcessInput 通过 SignalCommRegistration 对象由场景调用。  
- HandleSignalPDU 方法是一个回调方法。  
- SendMessage 方法在 SignalComm 通信设备发送消息时被调用。

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

69

![](images/47744681c463c46d74c7f560a00e514b98ffcb2d49e27ecb19114a226528288e.jpg)

# UNCLASSIFIED Comm 练习2—检视1 Interface.hpp

![](images/88b431375d257c94304b9f171b5b2717add7d36b06c481e821aadfb960f8b3e7.jpg)

class Interface : public WsfSimulationExtension   
{ public: //! Constructor Interface(); //! Virtual destructor ~Interface() noexcept override $=$ default; bool Initialize() override; bool ProcessInput(UtInput& aInput); void Start() override; void SendMessage(double aSimTime, WsfPlatform\* aSenderPlatformPtr, int aSourceTrackNumberOffset, const WsfMessage\* aMessagePtr); //! Determine if debugging is enabled. bool DebugEnabled() const { return mDebugEnabled; } using LocationMessageReceivedCallback $=$ UtCallbackListNvoid(double, DataLink::LocationMessage\*)> static LocationMessageReceivedCallback LocationMessageReceived; private: void HandleSignalPDU(WsfDisInterface\* aInterfacePtr, const WsfDisSignal& aPdu); UtCallbackHolder mCallbacks; WsfDisInterface\* mDisPtr; bool mDebugEnabled; bool mPrintMessages;

70

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9 Aug 19.

Other requests for this document shall be referred to AFRL/RQQD.

- 在 Interface.cpp 中，完成

CommLab::Interface::ProcessInput 方法。

- 任务 2a: 编写一个 if 语句, 检查变量 cmd 是否包含字符串 “print_messages”, 如果为真, 则将成员 mPrintMessages 设置为 true。  
- 任务 2b: 编写一个 elseif 语句, 检查变量 cmd 是否包含字符串 debug, 如果为真, 则将成员 mDebugEnabled 设置为 true。

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

71

![](images/a022b62ad427cd79848a900430500b81dd2894806c84e2afae0a7eb36a1a7215.jpg)

# Comm 练习2—任务2 解决方案

# Interface.cpp

![](images/f59d21101b972b0edf36e6ec18cde66d08339ad6b3c41134e4157f685fcab26c.jpg)

bool Interface::ProcessInput(UtInput& aInput)   
{ bool myCommand $=$ false; std::string cmd; if("comm_lab-interface" $\equiv$ aInput.GetCommand()) { myCommand $=$ true; UtInputBlock block(aInput); while (block.ReadCommand(cmd)) { //EXERCISE 2 TASK 2a //Write if statement to check if cmd contains "print/messages" and if true, //sets mPrintMessages to true if (cmd $= =$ "print/messages") { mPrintMessages $=$ true; } //EXERCISE 2 TASK 2b //Write else if statement to check if cmd contains "debug" and if true, // sets mDebug to true else if (cmd $= =$ "debug") { mDebugEnabled $=$ true; } else { throw UtInput::BadValue(aInput); } } return myCommand; } DISTRIBUTION C. Distribution authorized to U.S.Government Agencies and their contractor Other requests for this document shall be referred to AFRL/RQDD.

- 在 Interface.cpp 中，检查

CommLab::Interface::Initialize 方法和

CommLab::Interface::Start 方法。

- 注意, Initialize 方法将回调 HandleSignalPDU 添加到存储在 mCallbacks 中的回调列表。  
- 注意，Start 方法将成员 mDisPtr 设置为指向 WsfDisInterface 仿真扩展。

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

73

![](images/371b7db94a95a4af2d634209370d84a5975a97f3ed73247a63d00aa73004fd25.jpg)

# Comm 练习2—检视2

# Interface.cpp

![](images/7fe2713aa4e412f6f39d612daa26158726237d3495489c8f5d48117b9713603f.jpg)

- 检视和理解

void Interface::Start()   
{ //Get the DIS interface mDisPtr $=$ dynamic cast<WsfDisInterface\*>(&GetSimulation().GetExtension("dis-interface"));   
}

```cpp
bool Interface::Initialize()   
{ mCallbacks += WsfObserver::DisSignalReceived(&GetSimulation().Connect(&Interface::HandleSignalPDU, this); return true;   
} 
```

- 添加成员变量到 LocationMessage 类

- 根据提示，需要为 LocationMessage 类添加成员变量，并为这些变量添加访问器（Accessor）和修改器（Mutator）方法。

- 完成 LocationMessage 构造函数

- 根据提示，需要完成 LocationMessage 类的构造函数的实现。

- 完成 SignalComm::Receive

- 根据提示，需要完成SignalComm::Receive方法的实现。

- 完成 SignalComm::Send

- 根据提示，需要完成 SignalComm::Send 方法的实现。

- 完成 Interface::SendMessage

- 根据提示，需要完成 Interface::SendMessage 方法的实现。

- 完成 Interface::HandleSignalPDU

- 根据提示，需要完成 Interface::HandleSignalPDU 方法的实现。

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQQD.

# UNCLASSIFIED

# Comm 练习3 — 检视1

75

![](images/b665ff405b1ac2338a7bc218998504acef66bdbfb93e64b71fa4952e5f359343.jpg)

![](images/45450a9ccf65271d3c2303a92ca80388b94fc67c00a272af00a20e6c4449edf7.jpg)

- 审查并理解 DataLink::Message 类。

- 该类为 LocationMessage 数据创建数据链路层头部。  
- 该类利用 GenIO 来序列化和反序列化我们的数据。

class Message   
{ public: // This method reads enough of the input stream to // determine the type of Message being read. It then creates the proper Message // type from a factory class.Once the Message is generated, // it is populated with the data from the input stream. // // The caller owns the returned Message and is responsible for its destruction. static Message\* Create(GenI& aGenI); Message() $=$ delete; Message(const UtCalendar& aCurrentTime, unsigned short aSourceTrackNumber); explicit Message(GenI& aGenI); virtual \~Message() noexcept $=$ default; enum Type { cUNDEFINED $= 0$ cLOCATION $= 1$ cNUM_MESSAGETYPES $= 2$ }；

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

77

![](images/a4f4a9e8c6351326ce3f6c6396ad85384347039baebdc41fab39dca0d9270925.jpg)

# UNCLASSIFIED

# Comm 练习3 — 检视1

DataLinkMessage.hpp

![](images/80bae6d50c84612878132331c98b737684a638520ecfa40be1ce938560c2269b.jpg)

```cpp
class Message   
{ public: // Input/output virtual void Get(GenI& aGenI); virtual void Put(GenO& aGenO) const; virtual unsigned GetSize() const; virtual int GetType() const { return cUNDEFINED;} virtual const std::string&GetName() const; virtual void TestData() const; // Test Message for bad or questionable data // The following are simply the data and so are public // Message header unsigned short mSourceTrackNumber; // The originator of the message unsigned short mSize; // total number of bytes in the Message unsigned char mType; // Message type enumeration unsigned char mHour; // 0-24 UT unsigned char mMin; // 0-60 unsigned char mSec; // 0-60   
}； 
```

- 审查并理解 DataLink::LocationMessage 类。

- 该类为 LocationMessage 类的数据创建数据链路层消息。  
- 该类同样利用 GenIO 来序列化和反序列化我们的数据。

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

79

![](images/408b546c7c668d74a9f3dffbb51b4af031efb716a441ffc573dcb05b3fbad734.jpg)

# UNCLASSIFIED

# Comm 练习3 — 检视2

# DataLinkLocationMessage.hpp

![](images/46e084059d0b4dd4b5af9d318facde55ef3ef659631580aaca4808e7da13e7a1.jpg)

class LocationMessage : public Message   
{ public: LocationMessage() $=$ delete; LocationMessage(const UtCalendar& aCurrentTime, unsigned short aSourceTrackNumber); LocationMessage(const Message& aMessage, GenI& aGenI); ~LocationMessage() noexcept override $=$ default; double mLatitude; double mLongitude; double mAltitude; double mCourse; double mSpeed; unsigned GetSize() const override; int GetType() const override { return Message::cLOCATION; } const std::string&GetName() const override; void Get(GenI& aGenI) override; void Put(GenO& aGenO) const override; protected: virtual void GetMemberData(GenI& aGenI);

- WsfControlMessage.hpp 和 WsfStatusMessage.hpp 已经声明了本练习中使用的两种消息类型:

- WsfControlMessage: 由指挥平台使用，以发送“I COMMAND YOU”消息。  
- WsfStatusMessage: 由下属（那些有指挥官的平台）使用，以发送“OK”消息作为回应。

• 本练习添加了一种新的消息类型，称为 LocationMessage。  
- 检查 LocationMessage.hpp 文件，以熟悉该类的方法和属性。注意，新的消息类型 LocationMessage 已从 WsfMessage 子类化。

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

81

![](images/852ed4a59ad9eacf129e0ad4bd80ef5966af5dddbd2917f2897a731244cb59af.jpg)

# Comm 练习3 — 检视3

LocationMessage.hpp

![](images/feea9661126407da590909c2ee2e940aaa5a91b8b7c256d25e3af6bb83e587c0.jpg)

```txt
class LocationMessage : public WsfMessage   
{ public: LocationMessage(); int GetSourceTrackNumber() const { return mSourceTrackNumber; } void SetSourceTrackNumber(int aSourceTrackId) { mSourceTrackNumber = aSourceTrackId; } double GetLatitude() const { return mLatitude; } void SetLatitude(double aLatitude) { mLatitude = aLatitude; } double GetAltitude() const { return mAltitude; } void SetAltitude(double aAltitude) { mAltitude = aAltitude; } const char* GetScriptClassName() const override; private: int mSourceTrackNumber; double mLatitude; double mLatitude; double mLongitude; double mAltitude; 
```

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQDD.

• 为 LocationMessage 类添加私有成员变量，以存储以下内容：

- 平台的航向（一个双精度浮点数）  
- 平台的速度（一个双精度浮点数）

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

83

![](images/577be9956e24673447ceaf02fd9d0318198729600417fa43a9a5bf2c9421f034.jpg)

# Comm 练习3—任务1 解决方案

# LocationMessage.hpp

![](images/3b50ecf107de0c6564a8682f436be131445821dcd7bddd4aa7aee9deb5f7a8a9.jpg)

```cpp
class LocationMessage : public WsfMessage
{
public:
    LocationMessage(   );
...
private:
    int mSourceTrackNumber;
    double mLatitude;
    double mLongitude;
    double mAltitude;
    // EXERCISE 3 TASK 1
    double mCourse;
    double mSpeed; 
```

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

- 任务2：提供公共的访问器和修改器函数，语法应类似于其他成员变量的访问器/修改器。这些函数应命名为：

- GetCourse   
- SetCourse   
GetSpeed   
- SetSpeed

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

85

![](images/ab1689ea34b3188501d89558c882592a343a7173676d5f06930909e110d4ecbf.jpg)

# Comm 练习3—任务2 解决方案

# LocationMessage.hpp

![](images/a03bfd74dba4ac832c59f4eaa24543615d4406a7e0fc761283e6be7c5d9e1094.jpg)

class LocationMessage : public WsfMessage   
{ public: LocationMessage(); ... //EXERCISE3TASK2 doubleGetCourse()const{returnmCourse;} void SetCourse(doubleaCourse){mCourse $\equiv$ aCourse;} doubleGetSpeed()const{return mSpeed;} void SetSpeed(doubleaSpeed){mSpeed $=$ aSpeed;} const char\* GetScriptClassName()const override; private: int mSourceTrackNumber; double mLatitude; double mLongitude; double mAltitude; //EXERCISE3TASK1 double mCourse; double mSpeed; }；

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQQD.

- 完成 LocationMessage 类构造函数的实现:  
- 任务3a：将前一步定义的新成员变量添加到构造函数的成员初始化列表中，并提供适当的默认值。  
- 任务3b：在构造函数的主体中，使用消息发起者的信息设置消息数据，包括位置（mLatitude、mLongitude、mAltitude）、航向（可以通过使用atan2从速度中获得）。

- 获取速度。  
- 创建一个大小为3的双精度数组veINED，初始化为全0.0。  
- 调用 aPlatformPtr->GetVelocityNED(veINED)。  
- 调用atan2(veINED, veINED[0])并将航向设置为结果。  
- 调用 aPlatformPtr->GetSpeed() 并将速度设置为结果。

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

87

![](images/df6f902937fa086b35b8d6c8652662aecda210dd94903a6eb43f85460920c063.jpg)

# Comm 练习3—任务3 解决方案

# LocationMessage.cpp

![](images/194c0c5f3d5245533322b41fc66d38db31d95f36f9eb85e5a14b9be49df35cc1.jpg)

LocationMessage::LocationMessage(WsfPlatform* aPlatformPtr)

```cpp
WsfMessage(GetId(), nullptr, aPlatformPtr), mSourceTrackNumber(0), mLatitude(0.0), mLongitude(0.0), mAltitude(0.0), // EXERCISE 3 TASK 3a mCourse(0.0), mSpeed(0.0)   
// Set the source track number mSourceTrackNumber = aPlatformPtr->GetAuxData().GetInt("SOURCETracksNumber");   
// EXERCISE 3 TASK 3b // Get location aPlatformPtr->GetLocationLLA(mLatitude, mLongitude, mAltitude);   
// Get course double velNED[3] = { 0.0 }; aPlatformPtr->GetVelocityNEDVelNED); mCourse = atan2(velNED[1], velNED[0]);   
// Get speed mSpeed = aPlatformPtr->GetSpeed(); 
```

- 检查 SignalComm.hpp 文件，以熟悉该类的方法和属性。注意，新的通信设备类型 SignalComm 已从 wsf::comm::Comm 子类化。

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

89

![](images/4af20ec9361da3a9f72a9d93240ed88b158fcd05efd68a8dfda32a4f803831b7.jpg)

# UNCLASSIFIED Comm 练习3—检视4

# SignalComm.hpp

![](images/7a7a088c17ca7440c945a43e9d92b6d85239fd98bc80a0ccf5e26d6b76908af1.jpg)

class SignalComm : public wsf::comm::Comm   
public: //! Constructor explicit SignalComm(WsfScenario& aScenario); SignalComm& operator $\equiv$ (const SignalComm&) $=$ delete; //! Virtual destructor ~SignalComm() noexcept override $=$ default; //! Get the class ID associated with the object (poor man's RTTI). //! @return Returns the associated class ID. static Wsfstringld GetSignalCommClassId(); //! @name Framework methods //@{ wsf::comm::Comm* Clone() const override; bool ProcessInput(UtInput& aInput) override; bool Initialize(double aSimTime) override; //} unsigned int GetSourceTrackNumber() const { return mSourceTrackNumber; } CommLab::Interface\* GetInterface() const { return mInterfacePtr; } bool Receive(double aSimTime, wsf::comm::Comm\* aCommPtr, wsf::comm::Message& aMessage) override; bool Send(double aSimTime, std::unique_ptrWsfMessage> aMessagePtr, const Address& aAddress) override;

```cpp
void LocationMessageReceived(double aSimTime, DataLink::LocationMessage* aLocMsgPtr); const char* GetScriptClassName() const override; protected: //! Copy Constructor; used by clone SignalComm(const SignalComm& aSrc) = default; private: unsigned int mSourceTrackNumber; //! Like a link-16 source identifier CommLab::Interface* mInterfacePtr; UtCallbackHolder mCallbacks; }; 
```

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

# UNCLASSIFIED

# Comm 练习3—任务4

91

![](images/e59c35d54005ae055ff28e36e889f3881b0045df8e356ae1da4e51f210f0ecef.jpg)

![](images/07a228862816db55cb2dac721a1b7ec4a569c40e0cde9d76d57ea210c8871cc8.jpg)

实现SignalComm::Receive方法   
- 该方法在通信设备接收消息时被调用。  
- 任务4a：将消息传递给协议栈

调用mProtocolStack.receive(aSimTime，aCommPtr，aMessage);   
- Receive返回一个布尔值，将此布尔值存储在变量messageReceived中。

- 任务4b：使用拥有的仿真对象访问器，通知观察者消息已被接收

调用 WsfObserver::MessageReceived 将生成对已注册观察者的回调。  
调用方式为：

WsfObserver::MessageReceived(GetSimulation()))(aSimTime, aCommPtr, this,

*aMessage.SourceMessage(), aMessage.Result());

- 任务4c：将消息发送给任何在船上的接收者

- 调用基类 WsfPlatformPart::Send_Message 方法。  
参数为：

仿真时间  
- aMessage 参数的源消息（通过调用 aMessage.SourceMessage() 获取）

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19.

Other requests for this document shall be referred to AFRL/RQQD.

```cpp
bool SignalComm::Receive(double aSimTime, Comm* aCommPtr, Message& aMessage)  
{  
    ...  
    bool messageReceived = false;  
    // Perform a comm filter check  
    if (Component::Receive(*this, aSimTime, aCommPtr, aMessage))  
    {  
        // EXERCISE 3 TASK 4a  
        // Pass the message to the stack to see if it can be processed  
    }  
    messageReceived = mProtocolStack.receive(aSimTime, aCommPtr, aMessage);  
    if (messageReceived)  
    {  
        // EXERCISE 3 TASK 4b  
        // Using the owning simulation object accessor,  
        // Notify simulation observers that a message has been received  
    }  
    WsfObserver::MessageReceived(GetSimulation())(aSimTime, aCommPtr, this, *aMessage.SourceMessage(), aMessage.Result());  
    // EXERCISE 3 TASK 4c  
    // Forward the message to any on-board recipients (internal links)  
    SendMessage(aSimTime, *aMessage.SourceMessage());  
    }  
    //! Only throw a notification of message discarded if the message was intended for us and failed.  
    if (!messageReceived && aMessage.SourceMessage() ->GetDstAddr() == GetAddress())  
    {  
        // This message is specifically for a protocol stack failure  
        WsfObserver::MessageDiscarded(GetSimulation())(aSimTime, aCommPtr, *aMessage.SourceMessage(), "layer_receive_fail");  
    }  
}  
return messageReceived; 
```

93

![](images/dfa46b6ef7a68b7f6f1205a606fa518d8896a209270974ace72175223e8285cd.jpg)

# UNCLASSIFIED

# Comm 练习3—任务5

![](images/e8d7336a8e8a8e356870771c8297de81533a3279aaa10119cfbd748848bbb9ad.jpg)

# - 实现 SignalComm::Send 方法

- 请注意，此方法是从基类 wsf::comm::Comm 重写的。我们不会对消息进行排队或路由；当消息被发送时，它会立即被接收。  
- 任务5a：使用拥有的仿真访问器，通知观察者消息已被传输  
- 这可以通过以下方式完成：

```cpp
WsfObserver:::MessageTransmitted(GetSimulation())(aSimTime, this, 
```

```txt
\*message.SourceMessage();
```

- 任务 5b: 将消息传递给协议栈, 执行:

```txt
mProtocolStack.Send(aSimTime, message); 
```

- 任务 5c: 使用 CommLab::Interface 属性, 通过执行以下操作在 DIS 上发送消息:

```javascript
mInterfacePtr->SendMessage(aSimTime, GetPlatform(), mSourceTrackNumber, message.SourceMessage()); 
```

bool SignalComm::Send(double aSimTime, std::unique_ptr<WsfMessage> aMessagePtr, const Address& aAddress)

```rust
{ // Perform a comm filter check if (Component::Send(*this, aSimTime, *aMessagePtr, aAddress)) { //! This object is only valid in the scope of this method call, and will //! deallocate upon returning. If any object (layer, event, etc.) in the //! stack call chain requires an extended lifetime of this object, it is //! their responsibility to create such an object and manage it. Message message(std::move(aMessagePtr)); message.SourceMessage()->SetDstAddr(aAddress); message.SourceMessage()->SetSrcAddr(GetAddress()); // Use properties from the message table GetScenario().GetMessageTable()->SetMessageProp(GetId(), *message.SourceMessage()); 
```

```cpp
// EXERCISE 3 TASK 5a
// Using the owning simulation accessor, notify observers that a message has been transmitted
WsfObserver::MessageTransmitted(GetSimulation()(aSimTime, this, *message.SourceMessage));
// EXERCISE 3 TASK 5b
// Using our comm's protocol stack, send the message
messageSent = mProtocolStack.Send(aSimTime, message);
// EXERCISE 3 TASK 5c
// Using the CommLab::Interface attribute, send the message over DIS
mInterfacePtr->SendMessage(aSimTime, GetPlatform(), mSourceTrackNumber, 
```

}

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

95

![](images/8d7f16257c94ff98f2ceb395c6f79dc4728ae232c549066d4b8aa9a08c9cb304.jpg)

# UNCLASSIFIED

# Comm 练习3—任务6

![](images/1194ec94ae5cd9c44f1a9550094a0d7755d6e35a09664492c64e62badb3c9d1f.jpg)

- 实现 CommLab::Interface::SendMessage 方法

- 该方法由我们练习中的几个类调用。

- SignalComm::Send 方法在发送任何类型的消息时会调用此方法。

- 使用 if 语句忽略任何非 LocationMessage 类型的消息。

- 使用 LocationMessage::GetTyped 方法获取 LocationMessage 的类型 ID,  
- 使用 aMessage::GetType 获取存储在消息中的消息类型。  
- 检查并比较类型，如果它们不相同，则直接从此方法返回。

```cpp
void Interface::SendMessage(double aSimTime, WsfPlatform* aSenderPlatformPtr, int aSourceTrackNumberOffset, const WsfMessage* aMessagePtr) { // EXERCISE 3 TASK 6a // Check for quick return if this message type is not a LocationMessage if (aMessagePtr->GetType() != LocationMessage::GetteryId()) { return; } 
```

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

# UNCLASSIFIED

# Comm 练习3—任务7

97

![](images/2b65352f246f1a934ddcc0854b75844467cf99ca720c2a1e2f986b0b6d2a37e9.jpg)

![](images/3ee2e5f98b04f54fb84c35ac1da584c25ebd8456a889ed2779968fdc4922d345.jpg)

- 注意创建了一个类型为 DataLink::LocationMessage 的变量 dIMsg。  
- 任务7a：将头部和数据打包到DIS信号PDU中  
- 创建一个 GenMemIO 对象作为发送缓冲区，  
构造函数接受两个参数：

- 类型为 GenBuf::Native,   
消息的大小（使用dMsg.Size，返回消息中的字节数）。

使用dIMsg消息的Put方法将数据打包到缓冲区中，

Put方法接受一个参数，即GenMemIO缓冲区。

- 任务7b：在信号PDU中设置用户数据

调用 signalPduPtr->SetUserData,  
- 参数化为缓冲区的内容（buffer.GetBuffer）和消息的大小（以位为单位，使用dIMsg.Size并转换为位数）。

- 任务7c：使用DIS接口发送

- 使用指针 mDisPtr，调用接口的 PutPdu 方法，  
- 传入仿真时间（aSimTime）和唯一指针 signalPduPtr，该指针被移动到 PutPdu 方法中。

```cpp
void Interface::SendMessage(double aSimTime, WsfPlatform* aSenderPlatformPtr, int aSourceTrackNumberOffset, const WsfMessage* aMessagePtr) { ... if (mDisPtr != nullptr) { ... const LocationMessage* msgPtr = dynamic_cast(const LocationMessage*)((aMessagePtr); if (msgPtr != nullptr) { ... DataLink::LocationMessage dlMsg(currentTime, sourceTrackOffset); dlMsg.mSourceTrackNumber = msgPtr->GetSourceTrackNumber(); dlMsg.mLatitude = msgPtr->GetLatitude(); dlMsg.mLongitude = msgPtr->GetLongitude(); dlMsg.mAltitude = msgPtr->GetAltitude(); dlMsg.mCourse = msgPtr->GetCourse(); dlMsg.mSpeed = msgPtr->GetSpeed(); ... // EXERCISE 3 TASK 7a GenMemIO buffer(GenBuf::Native, dlMsg.GetSize()); dlMsg.Put(buffer); // EXERCISE 3 TASK 7b signalPduPtr->SetUserData(buffer.GetBuffer(), dlMsg.GetSize() * 8); // EXERCISE 3 TASK 7c mDisPtr->PutPdu(aSimTime, std::move(signalPduPtr)); } 
```

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

99

![](images/8fafd28b048520b6c774eeaf6456a5bf32848ef789341815bd37b9801efbaa90.jpg)

# UNCLASSIFIED

# Comm 练习3—任务8

![](images/7f31bbee2185a0d9c8b76778881cb2b802da4c4fe5f7b693aaf0fce8f75b6325.jpg)

实现 CommLab::Interface::HandleSignalPDU 方法  
- 该方法在 DIS 接口类接收到信号 PDU 时被调用。  
- 任务8a：仅处理来自类型为WsfDisSignal::EtGenericIP的数据链路的信号PDU

- 使用PDU的GetTDLType方法检查该值。  
- 从DIS信号PDU中解包DataLink::LocationMessage对象。

- 任务8b：使用GenMemIO对象访问来自DIS信号PDU的数据缓冲区  
- 参数化为：

- 信号数据（调用 signalData.data 方法），  
缓冲区的大小（dataLength），  
- 类型（使用 GenBuf::Native），  
- 缓冲区中数据的长度（同样是dataLength）。

- 任务8c：利用DataLink::Message::Create工厂方法从缓冲区读取

# DataLink::LocationMessage

- 将缓冲区传递给 Create 方法。  
返回值是 DataLink::Message* 指针，应存储在该类型的变量中（注意：此变量必须命名为 msgPtr，因为后续提供的代码中会使用到该变量）。

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19.

Other requests for this document shall be referred to AFRL/RQQD.

```cpp
void Interface::HandleSignalPDU(WsfDisInterface* aInterfacePtr, const WsfDisSignal& aPdu)  
{ // EXERCISE 3 TASK 8a // Use the PDUs GetTDLType() to check that it is of type // WsfDisSignal::EtGenericIP, and if so return  
if (aPdu.GetTDLType() != WsfDisSignal::EtGenericIP) { return; }  
}  
if (mDisPtr != nullptr) // Must be configured with optional DIS interface  
{ ...  
// EXERCISE 3 TASK 8b // Use a GenMemIO object that accesses the data buffer from the DIS Signal PDU // Parameterize with the signal data, type with type GenBuf::Native and length of the data GenMemIO buffer(signalData.data(), dataLength, GenBuf::Native, dataLength); // EXERCISE 3 TASK 8c // Utilize the DataLink::Message::Create factory method to read the // DataLink::LocationMessage from the buffer DataLink::Message* msgPtr = DataLink::Message::Create(buffer);  
} 
```

```txt
DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD. 
```

101

![](images/7225f38c4f74807a27e61f811da86ddded561de207457337c7eabedf0cd02ca8.jpg)

# UNCLASSIFIED

# 练习4

![](images/f25ace64a3e96b197df6ad188e6d1f2dad692df7d4d23b147e7ff92d23da04a3.jpg)

• 为 ScriptLocationMessageClass 添加 UT_DEclareScriptMethod 宏，以支持新的脚本方法 Course 和 Speed。  
• 在 LocationMessage.cpp 中为新的脚本方法 Course 和 Speed 添加 UT DEFINEScriptMethod 宏。  
• 在 ScriptLocationMessageClass 构造函数中添加 AddMethod 调用，以支持新的脚本方法 Course 和 Speed。

- 检查 LocationMessage.hpp 文件，以熟悉

ScriptLocationMessageClass 类的方法和属性，该类在文件底部定义。

- 注意，新的脚本消息类 ScriptLocationMessageClass 已从

WsfScriptMessageClass子类化。

```cpp
class ScriptLocationMessageClass : public WsfScriptMessageClass { public: ScriptLocationMessageClass(const std::string& aClassName, UtScriptTypes* aScriptTypePtr); void* Create(const UtScriptContext& aContext) override; void* Clone(void* aObjectPtr) override; void Destroy(void* aObjectPtr) override; UT.Declare-scriptMethod(SourceTrackNumber); UT.Declare.scriptMethod(Latitude); UT.Declare.scriptMethod(Longitude); UT.Declare.scriptMethod(Altitude); }; 
```

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

UNCLASSIFIED

![](images/b01b404c0a0235f9ace1e42ae7fb36bfc582cbfc845d21ad5df3569a1e2b2d39.jpg)

# Comm 练习4—任务1

103

![](images/208195d3bb7aaf59e9aedbe0660420356148a1904937010750026705a1a72aea.jpg)

- 脚本方法的声明

- #define UT.DeclareScriptMethod( ... )

- 扩展为方法参数的类声明  
- 继承自类UtScriptClass::InterfaceMethod   
- 声明类方法的构造函数和运算符()

- 任务1：在ScriptLocationMessageClass中添加一个

UT_DECLAREScriptMethod，声明一个名为Course的脚本和另一个名为Speed的脚本。这些方法允许在脚本中访问消息内容。

```cpp
class ScriptLocationMessageClass : public WsfScriptMessageClass
{
public:
    ScriptLocationMessageClass(const std::string& aClassName,
        UtScriptTypes* aScriptTypePtr);
    void* Create(const UtScriptContext& aContext) override;
    void* Clone(void* aObjectPtr) override;
    void Destroy(void* aObjectPtr) override;
    UT.Declare-scriptMethod(SourceTrackNumber);
    UT.Declare.scriptMethod(Latitude);
    UT.Declare.scriptMethod(Longitude);
    UT.Declare.scriptMethod(Altitude);
}
// EXERCISE 4 TASK 1
UT.Declare.scriptMethod(Course);
UT.Declare.scriptMethod(Speed); 
```

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

# UNCLASSIFIED

# Comm 练习4—任务2

105

![](images/c8a9f352e28c990bcf41e137f738c6f1711e7721d0f49158e625037c5f7779d4.jpg)

![](images/8d62c2279765ff1331890e5f4d3ea7b17b531c38b6cb01192f754674fd9ff535.jpg)

- 在 LocationMessage.cpp 中，完成

ScriptLocationMessageClass 构造函数的实现。

- 添加对 AddMethod 的调用，以支持 Course 和 Speed 脚本方法（类似于对 SourceTrackNumber、Latitude、Longitude 和 Altitude 的调用）。

ScriptLocationMessageClass::ScriptLocationMessageClass(const std::string& aClassName, UtScriptTypes* aScriptTypesPtr) : WsfScriptMessageClass(aClassName, aScriptTypesPtr)   
{ SetClassName("LocationMessage"); mConstructible $=$ true; mCloneable $=$ true; AddMethod(ut::make_unique<SourceTrackNumber $\succ$ ()); AddMethod(ut::make_unique<Latitude $\succ$ ()); AddMethod(ut::make_unique<Longitude $\succ$ ()); AddMethod(ut::make_unique<Altitude $\succ$ ()); // EXERCISE 4 TASK 2 // add calls to AddMethod for the script methods Course and Speed AddMethod(ut::make_unique<Course $\succ$ ()); AddMethod(ut::make_unique<Speed $\succ$ ());   
}

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

# UNCLASSIFIED

# Comm 练习4—任务3

107

![](images/2789075c2a185c35e452cf1fbeabd72e6df5e61151386be30e1973aa92fb9102.jpg)

![](images/d9d83d72b93c53dafae8760dce1a1c08587244b87bfd04cf9dac43a748d6647b.jpg)

- 脚本方法的定义

define UT DEFINEScriptPTMETHOD( ..)

- 创建与 UT.Declare-scriptMethod 宏定义的相同“方法”的类定义。  
- 同时扩展为一系列 $\mathsf{C} + +$ 语句，这些语句创建一个函数，其主体是宏定义的代码。  
- 该函数由类中声明的运算符()调用。  
- 一旦定义，该脚本方法可以从场景文件中的脚本接口调用。

- 任务3：完成 LocationMessage.cpp 文件底部的 Course 和 Speed 脚本方法的实现。  
- 请记住，您必须调用宏 UT DEFINEScriptMethod。  
- UT DEFINEScriptMethod( ... ) 接受以下输入参数:

Class：派生自UtScriptClass的类  
- Obj_Type: 应用对象的类型  
Method: 脚本的名称  
Num_Args: 输入参数的数量  
- Ret_Type: 一个字符串，指示返回值的类型  
- Arg_Types: 一个字符串，包含以逗号分隔的类型，指示每个输入参数的类型（如果没有输入参数，则该字符串应为空）。

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQQD.

```txt
UTDEFINESCRPTMETHOD(ScriptLocationMessageClass, LocationMessage, Altitude, 0, "double","") { aReturnVal.setDouble(aObjectPtr->GetAltitude()); } 
```

```cpp
// EXERCISE 4 TASK 3a
UT DEFINEScriptMethod(ScriptLocationMessageClass, LocationMessage, Course, 0, "double", "") {
    aReturnVal.setDouble(aObjectPtr->GetCourse() * UtMath::cDEG_PER_RAD);
}
// EXERCISE 4 TASK 3b
UT DEFINEScriptMethod(ScriptLocationMessageClass, LocationMessage, Speed, 0, "double", "") {
    aReturnVal.setDouble(aObjectPtr->GetSpeed());
} 
```

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

# UNCLASSIFIED

# 测试

109

![](images/f68484cad271c6aa079676b463421941f01dd86bceca15f70ac933520f3d3858.jpg)

![](images/66ce7d960ba086ffcb4d77de53f8b78ccb992e246cbcf4c8b53f8062b0719f21.jpg)

- 在 Visual Studio 中:

- 以发布模式构建解决方案  
- 构建 INSTALL 项目

Linux: from the build directory, run:
$ cmake --build . --target all -- -j11
$ cmake --build . --target install -- -j11

- 在 .comm\data 中检查并运行 run_all.bat 文件

- 程序应使用位于“.comm\data”文件夹中的两个场景文件进行测试，分别命名为 commscenario1.txt 和 commscenario2.txt（我们将不使用向导进行此测试）。

![](images/6b333a1f8b2efbd54120180f9e7569afcbf99a34bd39e8cb5194a30e9f0128c6.jpg)  
DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

![](images/58b577fc942a53e590e4a20bf4dfac1f5d6461d67ce152f2f92ac91dfd5f90ed.jpg)

![](images/f06be85ddf7f9e13c323f3a926b9cdbba943d82a5554cdc3194f6b1e2e530e1a.jpg)

111

![](images/8ae199b2d5a28a42643abd8e497e8049ae2743269994b31901f54ddc5b2d162d.jpg)  
UNCLASSIFIED

# 测试

![](images/3ea620580cc2271def4dc40b949eff7631ef28e3631fc195bfed2560f70c04a4.jpg)

- Mystic 将从 run_all.bat 文件启动。   
- 由于应用程序正在查看实时更新的文件，因此最好为此目的进行配置。  
- 在首选项中，将“At Scenario End”选项设置为“Extrapolate”。  
- 现在，Mystic将在播放超出从仿真接收到的最新数据时进行外推。

![](images/625a7adeacb5f6d714cfe76abafcc5bdfc5911681f6c6556f5f845bbfc99ab64.jpg)  
DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQQD.

![](images/6818973a82fd71e4a8902023774c942631c61287f3148833a35e06cf1ccbe6b0.jpg)

113

# 6.2.1.11.XIO10_AFSIMDev_Trng_XIO

本文为afsim2.9_src\training\developer\core\slides\

10_AFSIM_Dev_Trng_XIO.pptx 的翻译，主要是介绍如何扩展自定义 XIO，并做了许多小练习。

![](images/8e08412fad2e94d4c415ac5b53fc4c3e27bd801309218407e46bac884994f49f.jpg)

![](images/341ccc3965703c2f883f9addda321c46edbd43d50bb32ac1752082bdd008c4de.jpg)

![](images/211da2377944c42df8d767c4cce741c8c04058e8d9790ab77485605bd58738fb.jpg)

AFSIM开发培训

10 - XIO

本文档由杨石兴翻译，该资料做为《AFSIM2.9参考手册》的一部分。没有《AFSIM2.9参考手册》的加杨石兴微信领取：13324598743

Integrity $\star$ Service $\star$ Excellence

AFRL/RQQD 美国空军研究实验室

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

SAM - Surface-to-Air Missile

SAR - Synthetic Aperture Radar

VESPA - Visual Environment for Scenario Preparation and Analysis

WKF - Warlock Framework

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

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19.

Other requests for this document shall be referred to AFRL/RQQD.

2

![](images/9b8a3bac8c7b125d2e5f38f5bf65f27242ebbc45dc0707c2064d3399fdfa0941.jpg)

# UNCLASSIFIED

# 介绍

![](images/f756754d7628cb181c9357ca66703bbdadb2827f21ea1470104d69335262ead7.jpg)

- 本实验重点是使用XIO数据通信接口。  
- 您将构建一个外部飞行控制器应用程序，该应用程序从AFSIM仿真中接收平台列表信息，并向仿真发送控制数据包。  
- 以下练习提供了使用AFSIMXIO的实践机会：

- 练习1：注册一个默认的应用扩展、一个新的场景扩展和一个新的仿真扩展。  
- 练习2：实现一个仿真扩展，用于读取和处理新的XIO消息以控制选定的平台。  
练习3：创建一个与AFSIM仿真通信的外部应用程序。

![](images/aac39ac179e81b004cd3c1cf798b12b2c3cad9bd9b2c147adb61e78004473b7b.jpg)

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19.

Other requests for this document shall be referred to AFRL/RQQD.

- 订阅由XIO平台列表服务发布的信息。  
- 通过XIO向AFSIM仿真发送平台控制信息。  
- 扩展AFSIM以接收并利用数据来控制模拟的飞机。

![](images/61a25f17ddfa8560cf54db23a2c547d936f239a62ab74b5392e2162ab246613f.jpg)

参考资料：

- AFSIM 开发者基于 Web 的数据。  
- AFSIM 源代码和 Visual Studio 搜索功能。  
- AFSIM 文档。

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

4

![](images/a8db62cb397a56897701ebf274fbd44398d4fc134ca381be07cbd9da4012b255.jpg)

# UNCLASSIFIED

# 学习目标

![](images/b892c2b4a4b13f319e1c36b47368d36bcff154890221e5c68c950683cb810a1f.jpg)

- 您将获得以下方面的实践知识:

- 使用新的数据包类型扩展 XIO 接口。  
- 利用XIO接口发送和接收仿真数据。  
- 创建一个用户界面，用于控制仿真中的平台。  
- 理解如何调用不依赖于AFSIM仿真加载器的输入处理。  
- 巩固创建默认应用扩展和插件的技能。  
- 巩固创建仿真扩展和场景扩展的技能。

![](images/8f4cc6c7c7aade558ab25ce7d3f61882cdbb9c7549535664abe57a8556a7cfcb.jpg)

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

- 在开始本实验之前，您应该：

- 熟悉 WIZARD 和 AFSIM 脚本语言。  
- 建议参加过AFSIM分析课程或具备同等经验。  
- 拥有并熟悉使用 Microsoft® Visual Studio 2017® 或更新版本来编译应用程序。  
- 已完成模块“使用 CMAKE 构建 AFSIM”。

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQQD.

6

![](images/1b3cbc31382c5b616b7bdae1eff4c3b402cdc031890bba43755ce80884c930d8.jpg)

# eXternal IO Interface(外部 I/O 接口) (XIO)

![](images/2c7d08a5be4d1353c36eecef580bd94547a04d0a8af642ff51fc8d199d8cc7af.jpg)

- XIO 是一个自定义的，仅限 AFSIM 的网络接口

- 仅连接AFSIM实体与其他AFSIM实体  
- 而Comms可以连接到非AFSIM的网络实体

·用途：

- 在多个进程中模拟平台部件（传感器、通信等）  
AFSIM平台的分布式控制  
查询信息关于：

跟踪   
- 发送/接收的 WsfMessages  
- 任务  
- 平台/平台部件  
- 指挥与控制  
控制平台和平台部件  
发送消息  
控制任务

![](images/b035952654b7ae82c6851d7d30fde3270172c50df67450aa05e29a05ad13c394.jpg)

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

- 在多个机器上分布仿真AFSIM平台的场景  
- 允许连接到外部用户界面

![](images/9c9c9792c83c4cb301b0ea108e2751a761ed4c2ef8ab4f5726050d8499f8eb01.jpg)

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQQD.

8

![](images/c1f4fee09365f3c8fdadde883e1f38df29be9f5a235e18dd351713995a1eb2d1.jpg)

# UNCLASSIFIED

# XIO协议选项

![](images/ad9b46431526cfedfbdcb65e47b418f5066b3a2c01fdd220e17dffecd1e284f6.jpg)

# - TCP

- 保证发送的消息将到达，并且顺序相同。  
- 消息必须单独发送给每个接收者，网络开销较大。

# - UDP

- 不保证消息的到达或到达顺序。  
- 发送消息的开销较低。  
- 单个消息可以发送给多个接收者。

- 命令

- 通常是单向消息，发出命令或请求。  
- 可以可靠地或不可靠地发送。

- 查询

- 由单个查询消息和响应消息组成。  
- 必须可靠地发送。

·订阅

- 通过可靠的TCP消息初始化和维护。  
- 订阅的主题可以使用 UDP 或 TCP 发送。

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

10

![](images/0b4d513027ec71d0db8921eec57aa60f3dfdcecd94a40c785dc5591120d33f16.jpg)

# UNCLASSIFIED

# XIO数据

![](images/05f506f68383a0c8a2d8d87d7e68b4b5cb8508551b70ce442bcde449c37aab36.jpg)

命令

删除仿真中的平台

改变平台的目标航向、速度、高度或整个航线  
- 打开或关闭平台部件（传感器、武器、处理器等）

- 服务

- 平台列表服务

- 提供应用程序拥有的平台列表，以及当平台添加或删除时对该列表的更新。

- 平台信息服务

提供特定平台的信息。  
- 提供附加到该平台的平台部件的信息。  
提供平台部件状态变化的信息。

跟踪服务

- 发送平台跟踪管理器或特定传感器的跟踪更新和跟踪丢失消息。

仿真传感器服务

- 应用程序为外部平台建模传感器。  
可选地将传感器的跟踪发送回请求者。

查询

- 传感器重新托管查询   
查询应用程序是否能够建模特定的传感器类型。

- 基线XIO数据包在WsfXIO_PacketRegistry中定义  
- 每种数据包类型都有一个唯一的数据包 ID  
- 使用宏创建序列化和反序列化的"样板"代码

//！Packet sent from flight controller to the controlling simulation.   
class FlightControlPkt:public WsfXIO_Packet   
{ public: \~FlightControlPkt(）noexcept override $=$ default; //! Use the predefined macros to define constructor, serialization, and //! de-serialization methods. XIO.DefINEPACKET(FlightControlPkt,WsfXIO_Packet,350) { aBuff&mPlatformIndex&mPitchRate&mRollRate&mYawRate&mThrottle; } unsigned mPlatformIndex $= 0$ double mPitchRate $= 0$ / -1to1 double mRollRate $= 0$ / -1to1 double mYawRate $= 0$ / -1to1 double mThrottle $= 0$ /0to2   
}；

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQQD.

12

![](images/6e1be1c30d4ab9f92120526550e0e9ef0f89c7dd77be477dd7d8fcde7830466b.jpg)

# UNCLASSIFIED

# XIO配置

![](images/646f0d0b7b79ad80c8da5c6f5384094dbe8ed72a8263b2a3293bec83e66c401a.jpg)

- XIO 接口与 dis_INTERFACE 共享类似的网络配置参数
  - 有关详细信息，请参阅文档。

xio_INTERFACE ... end_xio_INTERFACE

```txt
xio_INTERFACE   
broadcast...   
[port..|send_port...receive_port...]   
multicast...   
[port..| send_port...receive_port...]   
unicast...   
[port..| send_port...receive_port...]   
mover_update_timer...   
entity_position_threshold...   
entity_orientation_threshold...   
connect_to_simulations   
application...   
debug...   
auto_dismapped...   
auto_map.application...   
no_autemap.application...   
end_xio-interface 
```

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

- 在这个场景中，有四架（非常概念化的）飞机正在飞行

- Blue_Fighter_1   
- Blue_Fighter_2   
- Blue_Fighter_3   
- Blue_Fighter_4

These four aircraft are theoretical. Their flight characteristics are generic in nature and do not share any operational characteristics with any real aircraft.

- 演示了使用 XIO 控制其中一架或多架飞机的能力  
- WsfP6DOF_Mover 被用作这些飞机的移动器  
- 我们将使用 Warlock 作为我们的仿真执行器

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

14

![](images/5f030185999e12e8d87b790b93eff83e5ca114ae4d935a86be22b4cf5814caf4.jpg)

# UNCLASSIFIED

# 测试

![](images/082ba45cf9b630ffc2f86ed8ba7c41a1896571d8deb63a2c8cecd68c027ef008.jpg)

- 我们将测试飞行控制器和XIO连接

- 通过点击飞行控制器应用程序来聚焦它。

- 以下键盘命令控制飞机：

- 数字1-9：选择要控制的平台  
- 退格键：取消选择所有平台  
箭头键或WASD>：平台的俯仰、滚转、速率变化  
Page-Up / Page-Down 或 “[” / “]”: 增加/减少平台速度

![](images/fb82916469e93b2c0ca38f9e1c9971d21b93be34e724ca3140a97051ab78db5c.jpg)

![](images/7b767f2edfe8a4fd143261d2e09fcf262312d9ea06e1e7cefd04983e51090034.jpg)

![](images/01bb880048365b9eba6808b9a6a95b52367ce4a6fb561f5bfd5b2844f6aeae09.jpg)

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

- 以下高级变量很重要（在cmake-gui中勾选高级选项）：

SWDEV_THIRD_PARTY.Package SOURCES

- 告诉 CMake 在哪里找到第三方源代码，例如 gtest（任务所需）、osg、osg-earth、qt 等。  
- 对于AFSIM版本，CMake期望在以下文件夹中找到第三方资源：  
..../swdev/dependencies/3rd_party

- VTK.RESOURCES_ARCHIVE_FILENAME

- 告诉 CMake 在哪里找到 VTK 资源（如果您构建任何可视化应用程序：wizard、warlock、mystic，则需要）。  
- 对于AFSIM版本，CMake期望在以下文件夹中找到VTK资源：  
..../swdev/dependencies/resources

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

16

![](images/28a2cae74fedc7bf4f8b35705dcd685451cd2ffa6cd498acece65da5c421f659.jpg)

# UNCLASSIFIED

# 开始 (2/4)

![](images/796e264a47942ff98223d81241bbe2d827abdcc849e3a2e6f381776d476f8048.jpg)

- 在写字板中打开run_cmake.bat

如果在Linux下打开run_cmake_Inx.sh

- 设置:

BUILD_WITH.wsf_p6dof to ON   
- BUILD_WITH_xio exerciseto ON   
BUILD_WITHWARLOCK TO ON   
- BUILD_WITHWARLOCK Plugin_P6nofData to ON   
- BUILD_WITH_WARLOCK_PLUGINPLATFORMBrowser to ON   
- BUILD_WITH_WARLOCK_PLUGINPLATFORMData to ON   
- BUILD_WITH_WARLOCK Plugin_SimController to ON   
- BUILD_WITHWARLOCK_PLUGIN_VisuaIEffects to ON   
- BUILD_WITH_WKF_PLGINmapDisplay to ON   
- BUILD_WITH_WKF_PLUGIN MapHoverInfo to ON   
- BUILD_WITH_WKF_PLUGIN_TetherView to ON

- 运行run_cmake.bat

如果是Linux运动run_cmake_Inx.sh

- 返回VS

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

- 如果 Visual Studio 已经打开：

- 导航到它并在提示时选择“重新加载所有”。

![](images/fae8ffd99e979abe95d287d008a7d3ecc408b0e661c234f6f4188c2e2afd6fa9.jpg)

- 或者，通过以下方式打开解决方案文件afsim.sln:

- 从 swdev\build 中打开。

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQDD.

18

![](images/37951cd867a06ff8fa5878fe9a4f128b1d985c39aa70cf7379e65be0fd167b52.jpg)

# UNCLASSIFIED

# 开始 (4/4)

![](images/d7249eb35c02ddcaa90afa2b0624e6a11580c3c3487757336f14d4ec3f09103c.jpg)

- 工程包含以下文件:

- Flight Controller App

FlightControllerPlatformListRequest.hpp   
FlightControllerPlatformListRequest.cpp   
FlightControllerInterface.hpp   
FlightControllerInterface.cpp   
FlightControlPkt.hpp   
FlightController.cpp

AFSIM Extensions

- PlatformControlService.hpp   
- PlatformControlService.cpp   
XIO_PluginRegistration.cpp

![](images/ec1baf29ccbc215be9df67e3af58994e448bd37a6e9daa6f0969f4804fa863ed.jpg)

Note that many solutions are possible; we have provided a solution in order to complete our training exercise in a short time period.

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

- 本练习利用以下类进行AFSIM扩展：  
- class FlightControlIPkt : public WsfXIO_Packet

定义了一种新类型的数据包，用于携带平台控制信息，包括当前的俯仰速率、滚转速率、偏航速率和油门值。

- class PlatformControlService : public WsfSimulationExtension

- 接收来自外部应用程序的 FlightControlPkt 数据包，并使用它们控制配备 P6DOF 驱动器的平台。  
- 发送 WsfXIO_PlatformListUpdatePkt 数据包，以通知外部应用程序可供控制的平台。

- class RegisterPlatformController : public WsfScenarioExtension

- 此类等待直到仿真创建完成，然后在接收到 SimulationCreated 方法调用时，将 PlatformControlService 类注册为仿真扩展。

- class WsfDefaultApplicationExtension : public WsfApplicationExtention

- 一个简单的应用程序扩展，具有 ScenarioCreated 方法。  
基于场景扩展进行模板化。  
- 当调用 ScenarioCreated 时，它会将场景扩展注册到场景中。

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQQD.

20

![](images/a5199033f1b03729ad78db20950e863fb338c7775dcece5dd911b059e7b4c568.jpg)

# UNCLASSIFIED

# 这个练习用到类

![](images/9890fd699cb41fe4026ec05352af1c3531b6b8444ecab68b14fc9aaa2fa73a89.jpg)

- 本练习利用以下类用于外部 FlightController 应用程序：  
class FlightControlPkt : public WsfXIO_Packet

定义了一种新类型的数据包，用于携带平台控制信息，包括当前的俯仰速率、滚转速率、偏航速率和油门值。  
- 由于 CMake 在 XIO 练习构建时不知道 flight_controller 文件夹，因此在 XIO 源文件夹中重复定义（它仅在构建外部 FlightController 应用程序时知道 flight_controller 文件夹）。

- class FlightControllerWidget : public QMainWindow

定义了一个主窗口小部件，用于在屏幕上显示飞行控制器的窗口。

class FlightControllerPlatformListRequest : public WsfXIO_PlatfromListRequest

- 维护一个可以被应用程序选择和控制的平台列表。  
- HandlePlatformList 是一个回调函数，每当从 AFSIM 接收到 WsfXIO_PrtformListUpdatePkt 时被调用。

- class FlightControllerInterface : public WsfScenarioExtension

- 维护用户按键时应用于俯仰、滚转和偏航的变化速率。  
- Update 方法执行大部分实际工作，从键盘获取输入并生成带有俯仰、滚转和偏航值的 FlightControlPkt 数据包。

• 与仿真扩展和飞行控制器应用程序共同使用的内容

![](images/29567154b5e6e833cd941fb2966b543c71286c4b93e9582f4d4539c9516b44bf.jpg)

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQQD.

22

![](images/da6286b884c379612ef3a2175001357dfda018add3389f50445ea8588869464c.jpg)

# UNCLASSIFIED

# XIO接口

# 只有FlightController App使用

![](images/f1c5fdaa76ff1a21b2bd3fa3850bcd588b97af0f5bb544b569f6a247327f3fc2.jpg)

- 我们只使用 XIO 接口的一部分

- AFSIM 中的 XIO 利用：

应用扩展  
- 场景扩展   
- 仿真扩展

- FlightController 不注册 XIO

- 不创建任何扩展  
- FlightController 主要使用所示的 XIO 类  
- main 创建一个 FlightControllerInterface   
- main 创建一个 FlightControllerWidget

我们将创建一个新的

FlightControllerWidget

![](images/cb840a53373b128668fa56d4199503853d0750d5a5df77592a3cc9b502d568b3.jpg)

我们将创建一个新的

FlightControllerInterface

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

·练习1

- 插件设置、扩展注册、注册 FlightControlPkt 数据包类型  
注册以在这些数据包到达时执行 ControlPlatform 回调方法

·练习2

- 理解平台的选择和取消选择，并完成 ControlPlatform

·练习3

- 理解 FlightController 应用程序  
实现 HandlePlatformList 数据包  
实现 Initialize   
- 理解在 FlightController 应用程序中使用 ProcessInput  
- 理解按键处理  
注册 FlightControlPkt 并注册平台列表更新

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

24

![](images/7eb4df12047878deed023da13f41864ca74f2a9981b2b69e4ca024eb019fdda1.jpg)

# UNCLASSIFIED

# 练习1

![](images/fdf4570ca5bc7afc18b3befe62fff32c13be34fa34304517fd6e77ab71b9410f.jpg)

完成默认应用扩展的注册，基于场景扩展进行模板化，并注册仿真扩展

- 注意 RegisterPlatformController 是一个场景扩展  
- 注意 PlatformControlService 是一个仿真扩展

- 注册 FlightControlPkt 数据包类型  
- 注册以在 FlightControlPkt 数据包到达时执行 PlatformControlService::ControlPlatform 回调方法

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

![](images/98efc4063b68ae3bea02e56e9f5dccc60e11a8679ce9143d75241250e8ba7050.jpg)

所有AFSIM扩展必须继承自WsfExtension:

- 已经存在三个预定义的扩展类（可以继承）：

- WsfScenarioExtension - 提供新场景命令的扩展（需要为这些命令实现新的ProcessInput）需要继承此类。  
- WsfSimulationExtension - 访问仿真的扩展需要继承此类。  
- WsfApplicationExtension - 创建新脚本类型或利用仿真扩展或场景扩展的扩展需要继承此类。

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQQD.

26

![](images/9e60ceaec9c86a6ba4c23a7e7b251483fdc7a6b6d314adfde5f6486376a54676.jpg)

# AFSIM Plugins & Extensions

![](images/f4b1db4934059f99f1508819131b89c95c01d7cb7e127533a16e7a20acefaccc.jpg)

![](images/d48acd4257205cf573c779a385b2d6936c3e00bf5548511be58deef1795cbcff.jpg)

所有AFSIM扩展必须继承自WsfExtension:

- 已经存在三个预定义的扩展类（可以继承）：

- WsfScenarioExtension - 提供新场景命令的扩展（需要为这些命令实现新的ProcessInput）需要继承此类。  
- WsfSimulationExtension - 访问仿真的扩展需要继承此类。  
- WsfApplicationExtension - 创建新脚本类型或利用仿真扩展或场景扩展的扩展需要继承此类。

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQQD.
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

