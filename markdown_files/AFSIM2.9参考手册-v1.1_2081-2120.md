# 传感器练习3—任务3解决方案

# TricorderSensor.cpp

![](images/44d4ce1a164127f1025f71e528d9e796fc15052fbeebf4c189a7c767ee598a53.jpg)

```cpp
//! Provide the name of the corresponding script class so that the   
//! scripting system can implement type casting properly.   
const char\* TricorderSensor::GetScriptClassName() const   
{ return "TricorderSensor";   
}   
ScriptTricorderSensorClass::ScriptTricorderSensorClass(const std::string& UtScriptTypes\* aClassName, aScriptTypesPtr) : WsfScriptSensorClass(aClassName, aScriptTypesPtr)   
{ SetClassName("TricorderSensor"); AddMethod(ut::make_unique<LifeFormTypeCount_1>("LifeFormTypeCount")); // LifeFormTypeCount() AddMethod(ut::make_unique<LifeFormTypeCount_2>("LifeFormTypeCount")); // LifeFormTypeCount(string) AddMethod(ut::make_unique<LifeFormTypeEntry_1>("LifeFormTypeEntry")); // LifeFormTypeEntry(int) // EXERCISE 3 TASK 3 AddMethod(ut::make_unique<LifeFormTypeEntry_2>("LifeFormTypeEntry")); // LifeFormTypeEntry(string, int)   
} 
```

```cpp
// Scripts used by the script observer   
// These need to be defined before the script observer block   
script void SensorTrackInitiated(WsfPlatform aPlatform, WsfSensor aSensor, WsfTrack aTrack)   
writeln("*** T=", TIME NOW, " ", aPlatform.Name(), " has initiated a track on a ", aTrack.Type(), " with a health of ", (aTrack.TrackQuality() * 100.0), " %");   
writeln(" Mode: ", aSensor.CurrentMode());   
int lifeFormCount = ((TricorderSensor)aSensor).LifeFormTypeCount();   
for (int i = 0; i < lifeFormCount; i = i + 1) { std::string lifeFormTypeStr = ((TricorderSensor)aSensor).lifeFormTypeEntry(i); writeln(" Life Form Type: ", lifeFormTypeStr); }   
end_script 
```

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQDD.

# UNCLASSIFIED

# 测试(1/2)

![](images/f88006019d0e7902ce0b8bcb58ccb6794591d6c9bcc412d934c26ee000e9db95.jpg)

![](images/eea20089ef6d066c50564e3a879e0bf34db6fc4a99907571901e5e26932c91a8.jpg)

- 从 Visual Studio 执行以下步骤：

1. 在 Release 模式下构建解决方案。  
2. 构建 INSTALL 项目。

Linux: from the build directory, run:
$ cmake --build . --target all -- -j11
$ cmake --build . --target install -- -j11

-在WIZARD中加载测试场景：

1. 打开 WIZARD。  
2. 找到位于 $\backslash$ sensor\data 文件夹中的顶级场景文件 sensorscenario.txt。这是我们用来测试程序的输入文件。  
3. 将 sensorscenario.txt 拖放到 WIZARD 中。

- 运行应用程序：

1. 从 WIZARD 中运行所选的应用程序。  
2. 在Mystic中运行生成的.aer文件。

- 在“Platform Options”停靠窗口中启用选项：

- 平台标签（全部）  
- 传出的传感器轨迹（Spock）

![](images/d38186577e620ce1793dce345668ad59041da9ac083bce61883095ed3e9056a9.jpg)  
DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQQD.

![](images/ae7e3f9d07dbecf5b9026353c5e082376ba67cfefbf012928a98586218d36e49.jpg)  
UNCLASSIFIED

# 测试(3/3)

117

![](images/2394d29675e40efcba3bda32743244b47348ec5011230324fe77ccd34eda894d.jpg)

![](images/e605fb58cc0e9afdb212d5c27d9c4f0b3df2758b5c8d53c35e94ab3ec2354894.jpg)

![](images/0eb0c4dc3f331b1221ef4253799246f5037c0388d725d16cac0414c539be5684.jpg)  
DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

：

Starting simulation.

*** T=0 Spock has turned on a tricorder

*** T=0.666667 Spock has initiated a track on a Klingon with a health of 75 %

Mode: KLINGON

Life Form Type: klingon.life_form

*** T=301 Spock has initiated a track on a Romulan with a health of 100 %

Mode:ALL_LIFE_FORMS

Life Form Type: LIFE(Form

Life Form Type: klingon life form

Simulation complete

Elapsed Wall Clock Time: 0.00787

Elapsed Processor Time : 0.01

![](images/11b6eeb0c20095b7f5b972a1093ba717a3dd790999a76ef09152dc2b779a6242.jpg)

119

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19.

Other requests for this document shall be referred to AFRL/RQQD.

# UNCLASSIFIED

# 问题？

![](images/74ce6c717ef661cbf612c7f36ca242f2ce4ae8c64d99cf23efaccdf5c14b8281.jpg)

![](images/b8d6b43c8dc19dc32a0aacffd30deb68bb3921e4048006224ce4d5dfa09b8712.jpg)

![](images/0742aa34db921a367d5ea577adf642fafb8eea48ad67f9520ccee9c36c7df7c6.jpg)

![](images/f61f15b79c0369841b9d6c5653cefc797b09c8566e53f7a287bd32ec73a14cb8.jpg)

Integrity $\star$ Service $\star$ Excellence

# AFSIM开发培训3-传感器附录

AFRL/RQQD

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQDD.

121

![](images/7038288a6b561f1706c06a3a1f3269c4acddb1998dac20b57873ab29c63057cd.jpg)

# UT DEFINEScriptMETHOD宏的完整推导

![](images/f99e1cef2931d57b135acfaa47f84e02bce841f434c76c3de3d3aa2c0f9a7103.jpg)

- 以下附录中的幻灯片展示了调用以下宏的完整推导：

UT DEFINEScriptMETMethod(LifeFormTypeEntry_2)

以及

```txt
UT DEFINEScriptMETMethod(ScriptTricorderSensorClass, TricorderSensor, LifeFormTypeEntry_2, 2, "string", "string, int") 
```

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQDD.

# UT_DECLAREScriptMethod相对容易理解:

define UT.Declare-scriptMETHOD(METHOD_NAME)   
class METHOD_NAME:publicUtScriptClass::InterfaceMethod   
{ public: METHOD_NAME(const std::string& aName $\equiv$ #METHOD_NAME); virtual void operator(）(UtScriptExecutor\* aExecutorPtr, UtScriptContext& aContext, constUtScriptRef& aReference, conststd::vector<UtScriptData>&aVarArgs, UtScriptData& aReturnVal);   
}

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQDD.

UNCLASSIFIED

# LifeFormEntry_2扩展

123

![](images/a9a49592d1236b81051e0dcbba119e067fb8288ac667fb37122d00b9d2194a1b.jpg)

![](images/e760faa0c7eb998ce69f4ac26cba8b18dfe4428284a065098029b5eba030835f.jpg)

UT_DECLARE-scriptMETHOD(LifeFromEntry_2);

![](images/24c12599dfa8b6cdfaf7c873e24055cfd748a2726959cd159a7237a4f884b7d1.jpg)

被转化为

```cpp
class LifeFormEntry_2 : public UtScriptClass::InterfaceMethod
{
public:
    LifeFormEntry_2(const std::string& aName = "LifeFormEntry_2");
virtual void operator() (UtScriptExecutor* utScriptContext& const UtScriptRef& const std::vector<UtScriptData>& utScriptData&) aReturnVal); 
```

UT DEFINEScriptMethod要复杂得多：

```txt
define UTScriptCheck_IMP if(!CheckForCallErrors(aExecutorPtr, aReference, &aVarArgs, aReturnVal)) return; 
```

```cpp
define UT DEFINEScriptMethod(CLASS, OBJ_TYPE, METHOD, NUM_args, RET_TYPE,ARGTYPES)   
UTDEFINESCRIPTMETHOD_IMP(CLASS, CLASS::, OBJ_TYPE, METHOD, NUM_args, RET_TYPE, ARGTYPES, UTScript_CHECK_IMP) 
```

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQDD.

UNCLASSIFIED

![](images/b17efa4c2a2bd58fdb5e44fad2b74934b804c3f81d2d2bc480fe82e91012e470.jpg)

# UT DEFINESCRIPTMETHODO

注意：代码已重新排序并稍作格式调整，以提高可读性

![](images/05e273682725d325bc64945954f201c9b82b80831cbe9da3e84b343926dc9915.jpg)

UT DEFINEScriptMethod相对复杂:

define UT DEFINE-scriptMETHOD_IMP(CLASS, SCOPE_OP, OBJ_TYPE, METHOD, NUM_args, RET_TYPE,ARGTYPES,CHECK_LINE)   
UTScriptMethod.MethodDecl(CLASS,METHOD);   
SCOPE_OP METHOD::METHOD(const std::string& aName) :UtScriptClass::InterfaceMethod(aName,RET_TYPE,ARGTYPES,NUM_args)   
{   
}   
void SCOPE_OP METHOD::operator() (UtScriptExecutor\* aExecutorPtr, UtScriptContext& aContext, const UtScriptRef& aReference, const std::vector<UtScriptData>& aVarArgs, UtScriptData& aReturnVal)   
{ if (NUM_args $\geq 0$ ) assert(aVarArgs.size() $= =$ static castsize_t(NUM_args)); auto objPtr $=$ aReference.GetAppObject<OBJ_TYPE>(); UtScriptClass\* retClassPtr $=$ GetReturnClass(); CHECK_LINE CLASS##METHOoD#####_Execute(aExecutorPtr,aContext,aReference, objPtr, mParentPtr,aReturnVal,retClassPtr,aVarArgs,this);   
}   
UTScriptMethod.MethodDecl(CLASS,METHOD)

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19.

Other requests for this document shall be referred to AFRL/RQQD.

# UT DEFINEScriptMethod相对复杂:

```cpp
define UT-scriptMETHODdecl(CLASS, METHOD) template<class T> voidCLASS##METHOD##Execute(UtScriptExecutor\* aExecutorPtr, UtScriptContext& aContext, const UtScriptRef& aReference, T\* aObjectPtr, UtScriptClass\* aObjectClassPtr, UtScriptData& aReturnVal, UtScriptClass\* aReturnClassPtr, const std::vector<UtScriptData>& aVarArgs, UtScriptClass::InterfaceMethod\* aInterfaceMethodPtr) 
```

```txt
define UTScriptABORT(MEMAGE) aInterfaceMethodPtr->ReportCallErrors(nullptr, nullptr, &aVarArgs, aReturnVal, (MESSAGE)); return 
```

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQDD.

127

![](images/0acd830dcaaca872cd387a3f91176572eb5cf513f2755c14c05193382e33558f.jpg)

# 对 LifeFormEntry_2 的扩展 原始 UT DEFINEScriptMethod 调用

![](images/4fe43eb2c8c2815cd8c02110971a8b7c5b3233f9f62c9dd34d1c9dc422624887.jpg)

```txt
// int lifeFormEntry = <x>.LifeFormTypeEntry(string aModeName, int aEntryIndex);  
UT DEFINEScriptMethod(ScriptTricorderSensorClass, TricorderSensor, LifeFormTypeEntry_2, 2, "string", "string, int") 
```

```objectivec
// Argument 1: string aModeName
// Argument 2: int aEntryIndex
// Use the mode name provided and convert to string ID
WsfstringIdemodeNameId = WsfstringId(aVarArgs[0].ToString());
unsigned index = (unsigned)aVarArgs[1].GetInt();
if(index >= aObjectPtr->GetLifeFormTypeCount(modeNameId))
{
    UTScript_ABORT("Bad mode name");
}
WsfstringId.lifeFormEntry = aObjectPtr->GetLifeFormTypeEntry(modeNameId, index);
if(lifeFormEntry == nullptr)
{
    UTScript_ABORT("Bad index");
}
else
{
aReturnVal SETString(lifeFormEntry.GetString());
} 
```

# 这是在脚本方法被调用时要执行的代码

![](images/631f3d4a856569cb093641d11637ede31d655e4ee67a1f0503af9fbcc8544bf4.jpg)

# s Transformed into:

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQDD.

UT DEFINEScriptMethod_IMP(ScriptTricorderSensorClass,ScriptTricorderSensorClass::,TricorderSensor, LifeFormTypeEntry_2,2,"string","string,int",UTScript_CHECK_IMP)

```objectivec
// Argument 1: string aModeName
// Argument 2: int aEntryIndex
// Use the mode name provided and convert to string ID
WsfStringIdemodeNameId = WsfStringId(aVarArgs[0].ToString());
unsigned index = (unsigned)aVarArgs[1].GetInt();
if (index >= aObjectPtr->GetLifeFormTypeCount(modeNameId))
{
    UTScript_ABOBT("Bad mode name");
}
WsfStringId.lifeFormEntry = aObjectPtr->GetLifeFormTypeEntry(modeNameId, index);
if (lifeFormEntry == nullptr)
{
    UTScript_ABOBT("Bad index");
}
else
{
aReturnVal SETString(lifeFormEntry.GetString());
}
} 
```

这是在脚本方法被调用时要执行的代码

Is Transformed into:

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQDD.

129

![](images/2f357965d272b705273cc29d5795dadeb2501ef87e194043a82f444d5d37bde5.jpg)

# 对 LifeFormEntry_2 的扩展

步骤2：在扩展UTScriptCHECK_IMP之后

![](images/722457ef018b6920d04a0e6212042dd4240d438d48b65c7267fd5809053b0238.jpg)

UT DEFINEScriptMethod_IMP(ScriptTricorderSensorClass, ScriptTricorderSensorClass::, TricorderSensor, LifeFormTypeEntry_2, 2, "string", "string, int", if (!CheckForCallErrors(aExecutorPtr, aReference, &aVarArgs, aReturnVal)) return;

```objectivec
// Argument 1: string aModeName
// Argument 2: int aEntryIndex
// Use the mode name provided and convert to string ID
WsfStringIdemodeNameId = WsfStringId(aVarArgs[0].ToString());
unsigned index = (unsigned)aVarArgs[1].GetInt();
if (index >= aObjectPtr->GetLifeFormTypeCount(modeNameId))
{
    UTScriptABORT("Bad mode name");
}
WsfStringId lifeFormEntry = aObjectPtr->GetLifeFormTypeEntry(modeNameId, index);
if (lifeFormEntry == nullptr)
{
    UTScriptABORT("Bad index");
}
else
{
    aReturnVal SETString(lifeFormEntry.GetString());
} 
```

这是在脚本方法被调用时要执行的代码

Is Transformed into:

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQDD.

UT-scriptMETHOD_DECL(ScriptTricorderSensorClass, LifeForm.TypeEntry_2);   
ScriptTricorderSensorClass::LifeFormTypeEntry_2::LifeFormTypeEntry_2(const std::string& aName) : UtScriptClass::InterfaceMethod(aName, "string", "string, int", 2)   
{   
}   
void ScriptTricorderSensorClass::LifeFormTypeEntry_2::operator() (UtScriptExecutor* aExecutorPtr, UtScriptContext& aContext, const UtScriptRef& aReference, const std::vector<UtScriptData>& aVarArgs, UtScriptData& aReturnVal)   
{ if $(2 >= 0)$ assert(aVarArgs.size() == static_cast(size_t>(2)); auto objPtr = aReference.GetAppObject<TricorderSensor>(); UtScriptClass* retClassPtr = GetReturnClass();

if (!CheckForCallErrors(aExecutorPtr, aReference, &aVarArgs, aReturnVal)) return;   
```javascript
ScriptTricorderSensorClassLifeFormTypeEntry_2 Execute(aExecutorPtr, aContext, aReference, objPtr, mParentPtr, aReturnVal, retClassPtr, aVarArgs, this); 
```

```txt
} UTScriptMethod_DECL(SciptTricorderSensorClass, LifeFormTypeEntry_2) 
```

```typescript
// Argument 1: string aModeName  
// Argument 2: int aEntryInde 
```

![](images/41d3693d24ed933ac896b2a47afbc0e4fb020a13a3bf7936efa44f3c484f1464.jpg)

这是在脚本方法被调用时要执行的代码

```txt
131 
```

# UNCLASSIFIED

![](images/f7e043d20b0ef0ddf624d2b7457facbac02f6684c868719451469116d659d709.jpg)

# 对 LifeFormEntry_2 的扩展

步骤4：在扩展UTSCRIPT_METHOD_DECL之后

```cpp
template<class T> void ScriptTricorderSensorClassLifeFormTypeEntry_2 Execute(UtScriptExecutor* &aExecutorPtr, &documentContext& const UtsScriptRef& aReference, &objectPtr, &documentClass* &objectClassPtr, &objectData& aReturnVal, &returnClassPtr, &const std::vector<UtScriptData>& aVarArgs, &interfaceMethodPtr); 
```

```cpp
ScriptTricorderSensorClass::LifeFormTypeEntry_2::LifeFormTypeEntry_2(const std::string& aName) : UtScriptClass::InterfaceMethod(aName, "string", "string, int", 2)   
{   
}   
void ScriptTricorderSensorClass::LifeFormTypeEntry_2::operator() (UtScriptExecutor* utScriptContext& const UtScriptRef& const std::vector<UtScriptData>& aVarArgs, UtScriptData& aReturnVal) 
```

{ if $(2\Rightarrow 0)$ assert(aVarArgs.size() $= =$ static cast<size_t>(2)); auto objPtr $=$ aReference.GetAppObject<TricorderSensor>(); UtScriptClass* retClassPtr $=$ GetReturnClass(); if(!CheckForCallErrors(aExecutorPtr,aReference,&aVarArgs,aReturnVal))return; ScriptTricorderSensorClassLifeFormTypeEntry_2 Execute(aExecutorPtr,aContext,aReference,objPtr, mParentPtr，aReturnVal, retClassPtr，aVarArgs,this);

```txt
} DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQDD. 
```

```cpp
template<class T> void ScriptTricorderSensorClassLifeFormTypeEntry_2 Execute(UtScriptExecutor* uExecutionPtr, UtsScriptContext& context, const UtsScriptRef& reference, T* aObjectPtr, UtsScriptClass* aObjectClassPtr, UtsData& aReturnVal, UtsScriptClass* aReturnClassPtr, const std::vector<UtScriptData>& aVarArgs, UtsClass::InterfaceMethod* aInterfaceMethodPtr) 
```

```txt
// Argument 1: string aModeName
// Argument 2: int aEntryIndex
// Use the mode name provided and convert to string ID
WsfStringIdemodeNameId = WsfStringId(aVarArgs[0].ToString());
unsigned index = (unsigned)aVarArgs[1].GetInt(); 
```

if(index $\vDash$ aObjectPtr->GetLifeFormTypeCount(modeNameId))   
{ UTScriptABORT("Badmode name"); 1

这是在脚本方法被调用时要执行的代码。

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQDD.

133

![](images/aa999c817ef7e63184c2d92196b99b39e89f7ea0648249121e54d4e7a242953a.jpg)

# UNCLASSIFIED

# 对 LifeFormEntry_2 的扩展

步骤4：在扩展UT-scriptMETHOD_DECL之后

![](images/d0705972c09b8cfb43fe6ea8bf8e0d1f624f1a97d22c94d6560ce4f19e97889d.jpg)

：

WsfStringIdlifeFormEntry $\equiv$ aObjectPtr->GetLifeFormTypeEntry(modeNameId,index); if(lifeFormEntry $= =$ nullptr) 这是在脚本方法 UTSCRIPT_ABORT("Bad index"); 1 else { aReturnVal SETstring(lifeFormEntry.getString()); }

UTScript.AbORT is define as:

define UTScriptABORT(MEMsAGE_）

aInterfaceMethodPtr->ReportCallErrors(nullptr, nullptr, &aVarArgs, aReturnVal, (MESSAGE_)); return

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQDD.

# UNCLASSIFIED

# 在<xxx>_Execute方法中的扩展

步骤5：在扩展UT-scriptABORT之后

135

![](images/413784426c2eac63db7dda66df6ceee4f57993d7fb20c0743ef3e29a7df67678.jpg)

![](images/027e76c544075fd2f25ca657a8c3d1baac600a25216a4f978d40ca31bea97e73.jpg)

```cpp
template<class T>  
void ScriptTricorderSensorClassLifeFormTypeEntry_2 Execute(UtScriptExecutor* executeUtsScriptExecutor*) execute(UtScriptContext& const UtsScriptRef& T* UtScriptClass* UtScriptData& UtScriptClass* const std::vector<UtsScriptData>& aReturnVal, UtScriptClass* returnClassPtr, UtScriptClass::InterfaceMethod* InterfaceMethodPtr) 
```

{

```cpp
// Argument 1: string aModeName
// Argument 2: int aEntryIndex
// Use the mode name provided and convert to string ID
WsfStringId(modeNameId = WsfStringId(aVarArgs[0].ToString());
unsigned index = (unsigned)aVarArgs[1].GetInt());
if(index >= aObjectPtr->GetLifeFormTypeCount(modeNameId))
{
aInterfaceMethodPtr->ReportCallErrors(nullptr, nullptr, &aVarArgs, aReturnVal, ("Bad mode name");
return;
}
; 
```

```txt
WSfStringId lifeFormEntry = aObjectPtr->GetLifeFormTypeEntry(modeNameId, index);
if (lifeFormEntry == nullptr) 
{
    aInterfaceMethodPtr->ReportCallErrors(nullptr, nullptr, &aVarArgs, aReturnVal, ("Bad mode name");
return;
}
else 
{
    aReturnVal SETString(lifeFormEntry.getString());
}
} 这是在脚本被调用时要执行的代码。
```

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQQD.

137

# 6.2.1.6. 武器 5_AFSIMDev_Trng_Weapons

本文为afsim2.9_src\training\developer\core\slides\

5_AFSIM_Dev_Trng_Weapons.pptx 的翻译，主要是介绍如何扩展自定义武器，并做了许多小练习。

![](images/466f96b912f7177ddd36397f0164312b95007680261662daba568be06045dfff.jpg)

UNCLASSIFIED

![](images/5bda17fcde5172b30990a103c262051c7102db71e5f2fa19c4fa1e40c02db56b.jpg)

![](images/17ce845fcf0272a58ea4d63bb531d004e0bfde0d1b0d0a4a2f6778898e43ab70.jpg)

# AFSIM开发培训

# 5-武器

本文档由杨石兴翻译，该资料做为《AFSIM2.9参考手册》的一部分。没有《AFSIM2.9参考手册》的加杨石兴微信领取：13324598743

Integrity $\star$ Service $\star$ Excellence

# AFRL/RQQD美国空军研究实验室

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

# UNCLASSIFIED

# 介绍

![](images/5e0f831a5eef0a82d88912095e092456d4b44be4a826398a4b2f726eb53778c3.jpg)

![](images/5b75d5ab94c4d08adc2ad604908562320eba0d2f28ef7852dd87b061ae1e9078.jpg)

- 本实验演示如何创建一个新的AFSIM武器  
- 在 AFSIM 中，武器可以是多种多样的事物：

- 大多数武器是“显式”武器；这些对象被明确地建模为一个平台（例如：导弹和炸弹）。  
- 隐式武器不被表示为平台（例如：干扰器）。

- 您将实现一个新的隐式武器，称为“相位器”（phaser）。  
- 以下练习提供了处理 AFSIM 武器的实践：

练习1：注册一个新的应用扩展  
- 练习2：创建一个自定义的AFSIM武器

![](images/a4994065c06f871d35809701be3bdfca4ee34bcb8d0e97ae0e085e4239154670.jpg)

- “PHASed Energy Rectification”（相位能量整流）武器是原版《星际迷航》电视剧中使用的虚构武器。  
- 您将创建一个名为PHASER_WEapon的新AFSIM武器类型。  
- “相位器”（phaser）应该向一个平台发射能量光束，其效果是削弱平台的护盾和装甲。  
- 当目标的护盾和装甲全部耗尽时，目标将被摧毁。

参考资料：

- AFSIM 开发人员基于网络的数据。  
- AFSIM源代码和Visual Studio搜索功能。  
- AFSIM文档。

![](images/2e571f7ffd3c8f2d19d0642e4bc7b92e17d2be7cbc00c8dbfc5bbba6e1d22751.jpg)

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQQD.

# UNCLASSIFIED

![](images/cb52c9290baaa0342a6accf0b984abb5ce8665bb8e00304c2e9ec1919ac996bc.jpg)

# 学习目标

![](images/1a58d0cce1deac9197bc0ecf5ce96eee161c29c8d69959e8c1eeed77d2567c62.jpg)

- 您将获得以下实践知识：

- 创建一个应用扩展  
- 创建一个新的插件  
- 创建新类型的武器  
- 实现一个 Fire 方法，用于创建并启动武器的事件时间表  
- 扩展 WsfEvent 类以创建新的事件类型，该事件类型将为我们的新武器安排事件  
- 为特定于我们武器的新事件类型扩展 WsfEvent 的虚拟 Execute 函数  
- 在响应计划的火力更新事件时实施武器动作  
- 为未完成的交战重新安排事件，并删除已完成交战的事件  
- 使用AFSIM的aux_data方法快速开发新功能

- 在进行本实验之前，您应该：

- 熟悉 WIZARD 和 AFSIM 脚本语言  
- 建议完成AFSIM分析师课程或具有同等经验  
- 拥有并熟悉使用 Microsoft® Visual Studio 2017® 或更新版本来编译应用程序  
- 熟悉使用 Microsoft Windows® Explorer  
- 已完成模块“使用 CMAKE 构建 AFSIM”

- 熟悉使用 cmakeGUI  
- 熟悉执行 cmake（如果在 Linux 上开发）

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQQD.

UNCLASSIFIED

# AFSIM 框架中的武器

![](images/62e75627508e2f75fed0e0545619ed6608bdb7c7e68deec3f54280269896fce5.jpg)

6

- AFSIM 在基础框架中包含了一套强大的武器选项。  
- 通过使用 $\mathrm{C} + +$ 架构，开发人员可以扩展类以创建新武器或新的武器行为。

![](images/02770397a53e83b851c7d09bfd9216c7721ccc9199eb3d7250486a86fd677778.jpg)

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19.

Other requests for this document shall be referred to AFRL/RQQD.

- 武器是指旨在阻止某个对象（永久或暂时）运行的事物。  
- AFSIM 中 WsfWeapon 的继承图如下所示。

![](images/24763e74a43b2ae12bc8d5a8fddbd9ed044bca14148c929174952bdb1f5eb2b3.jpg)

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQQD.

8

![](images/471d48c33f9137621016302c6383ea725513ea7b85507f7b8521cf3550e3a576.jpg)

UNCLASSIFIED

# 武器能力

![](images/5a019e697998ba8d69c4e7b51064643e24003d9b97de76c69e80993afe4ed2fb.jpg)

- WsfWeapon 定义了以下方法:

- Fire: 发射武器  
- FireSalvo：多次发射武器  
- CeaseFire: 停止齐射   
-CreateTargetTrack：为目标创建跟踪轨迹以进行攻击

您将向 AFSIM 添加一个新的 PhaserWeapon 类  
![](images/69f90c0bf06ca92d134094adb1cceac4347a33f16f719b3e6c6361096a7fb07b.jpg)  
DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQQD.

# UNCLASSIFIED

# 武器效应

10

![](images/00c4f0eb12188dbc0e04c6b8550ea0e71b971ace5b2f1408695009a32fc8a44f.jpg)

![](images/89b4bdfdfc1f013a5ab35a1d7533a9bfec51b20a0451ce8fedeeb9504efe368c.jpg)

- 对目标的效果通过武器效果实现。  
- 武器效果可以定义在平台上（显式效果）或定义在武器上（隐式效果）。  
- AFSIM 的武器效果继承树如下所示:

![](images/57a8f9bbef3e1e753f94d1380fabe2d08886976c2c207f88b59b188944db889e.jpg)  
DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQDD.

- 武器效果（杀伤力）对象用于确定武器对平台的影响。  
- WsfLethality 是所有杀伤力实现的基类。AFSIM 提供了几种实现，包括：

- WsfCarltonLethality 使用 Carlton 损伤方程  
- WsfSphericalLethality   
- WsfTabulatedLethality

- 我们将在AFSIM武器模块中实现一个简单的武器效果。

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQQD.

UNCLASSIFIED

# 扩展WsfWeaponEffects

![](images/3b57399759b8f32a58bb91a287769fbbc05e73c9fb7e8cf12470fd1e02950013.jpg)

![](images/072d41645a15e01d1790f43f0b7c37f837355dce74cc1394be0863df85287986.jpg)

您将向AFSIM添加一个新的PhaserLethality类。

![](images/c505056933b96a0986ae2b5faf3eaa012fbe6a3d42e401d4f970c07f1df556db.jpg)

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQDD.

- 平台类型 phaser-plat 携带一个 PHASER_WEapon

PHASER_WEPOCH 使用了新的关键字。

- 一个PHASER WEAPON将对平台“开火”。  
- 每次开火时，它会连续发射一个用户定义的时间段，例如 fire_duration（在我们的场景中为 5 秒）。

- phaser-plat 携带一个雷达，用于探测目标并生成跟踪轨迹。

- PhaserLethality 类的功能

- 每秒从目标平台中消耗一定单位的护盾值（units-of-shield）。  
如果没有护盾，则每秒消耗一定单位的装甲值（units-of-armor）。  
- 一个 fire_integration_interval 参数指定了多长时间应用一次效果，即多长时间调整一次护盾值或装甲值的减少。  
我们的相位武器传播时不会损失能量。

- 简化假设

为了简化，我们不考虑瞄准精度（只要有目标或目标轨迹，就足够开火）。  
- 然而，我们假设PHASER_WEPOCH无法穿透地面，因此需要确保目标不会被地平线遮挡。

- 平台类型目标的 aux_data 关键字关联以下值：

- phaser_shields: 初始护盾强度。  
- phaser Armour: 初始装甲强度。

- phaser-1平台上的执行脚本：

- 每10秒从跟踪列表中随机选择一个目标，并执行其phaserweapon的fire方法。

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19.

Other requests for this document shall be referred to AFRL/RQQD.

# UNCLASSIFIED

![](images/c821b16d9057b2ad7cafeeb48c8a48c031dd1bacfc3e3ad8e95fcb03944e54b7.jpg)

# 武器想定 (2/2)

![](images/d19ea5696a53b630448a7921796bb4a2263b6ee44a89ab3a32f5704c079441ad.jpg)

- 注意，一个名为 target_spawn 的目标生成对象会随机生成目标，目标可以被PHASER_WEapon武器摧毁。  
- target_spawn 平台添加了一个“武器”：

- 这个“武器”被命名为target launcher。  
- target launcher 持有用户定义数量的目标平台，每个平台的类型为 target。

- target_spawn 平台有一个执行脚本：

- 这个脚本尝试每秒“发射”一次 target launcher。  
- 当“发射”时，target launcher会释放一个目标。  
- 当 target launcher 释放一个新目标时，会执行一个定义好的脚本：

- 该脚本使用均匀随机分布来设置目标的航向（heading）和位置（position），位置以一个中心纬度和经度为基准。

- 补充说明：

- 也可以通过运行 WsfSimulation 对象的脚本，使用其 AddPlatform 或 CreatePlatform 方法生成新的平台。  
模拟的结束时间设定为20分钟。  
- 场景数据将保存到文件 weapon exercise.aer 中，并可以使用 Mystic 进行回放。

- Phaser 武器将定义以下属性：

- fire_duration - Phaser 在一次交战中持续射击的时间。  
- fire_integration_interval - 在 fire_duration 期间，应用武器效果的时间间隔。

- PhaserLethality 武器效果将定义以下参数:

- shield_damage_rate - 对护盾的每秒伤害值。  
- armor DAMAGE_rate - 对装甲的每秒伤害值。

- 示例输入：

```python
shield DAMAGE_rate 100
armor DAMAGE_rate 20
...
    fire_duration 5.0 sec
    fire_integration_interval 0.1 sec 
```

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQQD.

16

![](images/fd981144763bd4db0774a1283fabc1281272285f706d88d335b052ea3cbe22fd.jpg)

# UNCLASSIFIED

# 场景结果（来自Mystic）

![](images/2ef0b7c25451d23a0d142f5dfa523ff3beaa2e976afde9109365f6d36a252667.jpg)

![](images/a1ab12f060c03ed2cbd148a6afb393c86e1e648295bba64d28af33b0888cd2f6.jpg)

- 红线和文字表示平台的护盾值（当前为0）和装甲值（当前为58）。  
- 在Mystic中，这条线在护盾值减少到0之前是黄色的，然后会变成红色。

- 辅助数据允许在轨迹或其他组件（包括平台）上放置“额外”数据，包括：

- 任何平台部件（通信、传感器、武器、移动器等）  
- 任务  
-组  
一 路线  
- 发射器/接收器

- 基本类型（int、bool、double、string）是预定义的。  
- 也可以注册任意类型或构建结构体。  
- 通过脚本语言也可以使用这些数据。

Signatures

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQQD.

UNCLASSIFIED

![](images/1507504f801f029dcba2575d9d48a294153352a01194acd4cb3f9d29438178c1.jpg)

# 护甲和护盾（Armor and Shields）

![](images/5eaa0c67755a36eb596adab8c2547bfaeaa8ff5defde38eca70c80066ea2e938.jpg)

- Phaser 武器将影响平台的护甲和护盾。

- 注意：AFSIM 平台没有护甲或护盾，因此我们需要为本次练习“发明”它们。  
- 我们将使用AFSIM的aux_data方法来分配护甲和护盾。  
- 我们的PHASER_WEAPON将在交战期间访问并调整目标平台的护甲和护盾值。

- 示例输入：

```matlab
platform ....
aux_data
    double phaser_shields = 600
    double phaser Armour = 100
    end(aux_data
endplatform 
```

![](images/4e1faed67a1b63415af68dc737c0a43429263d0a46fe0c7be9e06a169bd88f86.jpg)

- 一个模拟对象（WsfSimulation）在构造时创建一个事件管理器（WsfEventManager）。事件管理器维护一个按时间顺序排列的事件队列。这个事件队列是一个标准模板库（STL）中的priority_queue，每个元素按递增的时间排序。时间指示事件（WsfEvent）何时被调度。  
- 事件管理器提供了方法来将事件添加到队列中、查看但不移除下一个要调度的事件、从队列中弹出下一个事件，以及将队列重置为空状态。添加事件的接口通过模拟对象的 AddEvent 方法来实现。

- 事件步模拟通过查看事件队列的前端来等待下一个事件。事件步和帧步模拟对象在调用AdvanceTime方法时调度事件。事件从队列中弹出，并调用其Execute方法。

![](images/471ef40f386f693e490288779487e23b9900b63b10e4e3e3db1f348d3fb3bb7d.jpg)

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQQD.

20

![](images/ae3974ca555f4c65822f1b50af72d5438a6bedb4daccec6216147c3f04cf0c1a.jpg)

# UNCLASSIFIED

# 事件管理

![](images/b31dcc1760bd84e821cf8e870ffd8a92cbebeae5fb345ae0506ff79aee83d5e3.jpg)

- 由于Phaser在一段时间间隔内射击（fire_duration），我们需要告诉AFSIM定期重新访问我们的模型（fire_integration_interval）以重新计算伤害。与大多数瞬时生效的武器（如爆炸）不同。  
- 武器的初始发射将由任务处理器或调用 WsfWeapon.Fire 来处理。  
- 在PhaserWeapon内部，确定fire_duration是否已过期。如果没有，则创建一个新事件（PhaserWeapon::FireUpdateEvent），并将其安排在当前模拟时间之后的fire_integration_interval秒进行调度。  
- WsfEvent 及其所有子类都有一个枚举值 EventDisposition，用于标记事件在 WsfEventManager 中的状态：

- cDELETE - 删除此事件。  
- cRESCHEDULE - 重新调度到未来某个时间。

![](images/dc0a95152ae681094d0ee6435e5ba94dbbefc2edce9fe07d66858b6190772c3c.jpg)  
DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQQD.

22

![](images/3ba07d752db8542b83419b563d09ee639b5b6787d71e6b519f049e8ee1cbec26.jpg)

UNCLASSIFIED

# 开始 (1/3)

![](images/9087a6449d9f8a20e6e045a7e8b680adde1ad20591349a2429a18dba9a03fbc1.jpg)

- 打开 CMake GUI  
- 勾选BUILD_WITHweapon exercise   
- 勾选BUILD_WITH_wsf_mil   
- 点击“Configure”（如果出现提示要求选择编译器，请进行响应）  
- 点击“Generate”

- 如果 Visual Studio 已经打开：

- 切换到 Visual Studio，当出现提示时选择 Reload All（全部重新加载）。

![](images/f396c0a4d1808d3f2cac265fd15bafdbd0c08c46f4999e5e051e591d6a5d2e46.jpg)

- 或者，通过以下方式打开解决方案文件afsim.sln:

- 从 swdev\build 打开  
- 或者点击 CMake 中的 “Open Project”（打开项目）

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQQD.

24

![](images/a6fa876e413836ed59beaa85b95ef0ef3076c9fa4653b3bea11460beddd73ed4.jpg)

# UNCLASSIFIED

# 开始 (3/3)

![](images/8b0839fe62c6f8334604b6a8694bac9305644a73abf9e338b3c9f715e06b6ea6.jpg)

- 工程使用如下源文件:

- WeaponPluginRegistration.cpp   
- PhaserWeapon.hpp   
- PhaserWeapon.cpp   
- PhaserLethality.hpp   
- PhaserLethality.cpp

![](images/1769cbe6191144807e519a1022e3e53bdc4576aecf36939f574376eedd80d787.jpg)

请注意，有许多解决方案是可行的；我们提供了一个解决方案，以便在较短的时间内完成我们的训练练习。

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQDD.

- 本练习使用了以下类：  
- 类PhaserWeapon:public WsfWeapon

- 创建了一种名为PhaserWeapon的新武器类型  
- 处理“fire”（开火）事件

- 类PhaserLethality:public WsfWeaponEffects

- 创建了一种名为PhaserLethality的新武器效果  
定义了一个适用于Phaser的杀伤力模型（针对目标）

首先将护盾降为零  
然后将装甲降为零   
最后摧毁目标

- 类 RegisterPhaserWeapon : public WsfApplicationExtension

- 此类作为应用扩展注册到标准应用程序中  
- 重写了 ScenarioCreated 方法，在场景由 mission/warlock 创建后，将 PhaserWeapon 添加为一种新武器类型

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQDD.

# UNCLASSIFIED

![](images/c0650322c1bb4d5033a00452d8ad0c1f33b268ab4b3008ec5fc0efb3b0e44c65.jpg)

# 武器练习

![](images/de12f6835eba3b2abeac43384d20a3fdd4c6a2e50f02f9e791b017bff2dd7d5b.jpg)

·练习1

- 应用扩展的注册   
- 添加/注册新的武器类型和新的武器效果类型

·练习2

- 理解并完成 phaser 的 ProcessInput 方法的实现  
- 理解并完成武器如何开火以及其效果如何应用于目标的实现

- 完成应用扩展的注册并建立对 wsf_mil 的依赖关系  
- 添加/注册一种新的武器类型 PhaserWeapon  
- 添加/注册一种新的武器效果类型 PhaserLethality

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQQD.

28

![](images/6cbb91fbdbe46a4856154dd0367f43a68f429fe8523c8fa0f723786fb45c69bd.jpg)

# AFSIM插件&扩展

![](images/9c313c94cb729c5a869fca1c15660fa5df5d024ecebc2af6b4675af897b39098.jpg)

![](images/566dfbfe5f324e5e290021724d31a2eddd4ca63840dd5813bd3fef438f76d73e.jpg)

- 所有AFSIM扩展都必须继承自WsfExtension:  
- 已经存在三个预定义的扩展类（可以继承）：

- WsfScenarioExtension - 提供新场景命令的扩展（需要为这些命令实现新的ProcessInput）需要继承此类  
- WsfSimulationExtension - 访问仿真的扩展需要继承此类  
- WsfApplicationExtension - 创建新脚本类型，或使用仿真扩展或场景扩展的扩展需要继承此类

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19.

Other requests for this document shall be referred to AFRL/RQQD.

![](images/57db4915c8e0c9e4f2f264ac5f88be61de17cb118d7286aaeba94a2db643b667.jpg)

- 所有AFSIM扩展必须派生自WsfExtension：已经存在三个预定义的扩展类（可以继承）：

- WsfScenarioExtension - 提供新场景命令的扩展（需要为这些命令创建新的ProcessInput）需要继承此类。  
- WsfSimulationExtension - 访问模拟的扩展需要继承此类。  
- WsfApplicationExtension - 创建新脚本类型的扩展，或将利用模拟扩展或场景扩展的扩展，需要继承此类。

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQQD.

30

![](images/894c111e8f4c94b1ebe7d8370e903242664ea892f9fc9fce8fd0c87ab6fa8ca8.jpg)

UNCLASSIFIED

# 扩展

![](images/fa3fe590a1f84ee348b57c70c750dc3cadb31bd4e674b7b820276b7a4b9b4851.jpg)

- 应用程序、场景和模拟都可以被“扩展”。

- 应用扩展由应用程序拥有。

- 代表可以添加到应用程序的可选功能。  
- 如果需要新的脚本类型（传感器、武器、组件、移动器），则使用此功能。  
- 这是在AFSIM中注册所有扩展的入口点。  
- 如果要创建场景扩展或模拟扩展，则需要应用扩展。

- 我们将使用一个新的插件来注册应用扩展。

- 在这个练习中，我们需要新的应用扩展，因为我们正在创建一种新类型。

- 插件代码和应用扩展代码位于文件WeaponPluginRegistration.cpp中。

- 在传感器练习中，WsfPluginSetup和WsfPluginVersion的定义已为您提供。

- WsfPluginVersion创建了一个新的UtPluginVersion对象，该对象使用三个参数构造（主版本号、次版本号和编译器信息字符串），并利用这个对象设置了作为参数传入的UtPluginVersion对象的值。  
- WsfPluginSetup调用了aApplicationPtr.RegisterExtension(), 以将TricorderSensorRegistration应用扩展对象注册到WsfApplication::aApplicationPtr对象参数中。

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQQD.

32

![](images/6f1fc8a573e706529aad91a01ce6f6cd3a47740adf9d4ab2beb9b3a28236e90d.jpg)

# 武器练习1—任务1

![](images/fa429c24a889aedc483404cbcac9273c45457e22ec0ffa640c37e98cff3798fc.jpg)

在本练习中，您需要实现WsfPluginSetup和WsfPluginVersion。

- 在WeaponPluginRegistration.cpp中：

完成WsfPluginVersion方法

- 该方法接收一个引用输入参数UtaPluginVersion&aVersion，并将其赋值为一个新的UtaPluginVersion对象，该对象使用版本信息初始化。  
- 使用WsfPlugin.hpp中提供的宏来获取版本信息。

- 在创建新的UtPluginVersion对象时，调用其构造函数，并传入三个输入参数：

- 主版本号：WSF Plugin_APIMajor_VERSION  
- 次版本号：WSF_PLUGGIN_APIMinor_VERSION  
编译器字符串：WSF_PLUGGIN_API_COMPILER_STRING

WEAPON_EXERCISE exports void WsfPluginVersion(UtPluginVersion& aVersion)   
{ //EXERCISE1TASK1 // Initialize the plugin version object using the provided macros in UtPlugin.hpp // Use the class UtPluginVersion(..) with the version information from the macros aVersion $=$ UtPluginVersion(WSF Plugin_APIMajor_VERSION, WSF Plugin_APIMinor_VERSION, WSF Plugin_API_COMPILER_STRING);   
} WEAPON_EXERCISE exports void WsfPluginSetup(WsfApplication& aApplication) { //EXERCISE1TASK2.a //Use the aApplication object to Register an extension. //Name this extension "register_phaserweapon". //Make it of type RegisterPhaserWeapon //EXERCISE1TASK2.b //Tell the application that this extension, "register_phaser Weapon",depends on"wsf_mil" //Make sure that wsf_mil is loaded before we try to register our new types. // (WsfWeaponTypes and WsfWeaponEffectsTypes need to be valid)

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQQD.

34

![](images/1bbcec624f4cc37030b4a466f185b031e9ce8bc402c6af0cccdbcc9b1cc6d1cc.jpg)

# 武器练习1—任务2

![](images/128e835c9e8837b6a63fe7dc5cd2f51febf51d5d0a92e7af562e16e7f286f9fd.jpg)

# 在 WeaponPluginRegistration.cpp:

任务2：完成 WsfPluginSetup 方法

- a部分：使用aApplication参数注册一个扩展

调用aApplication.RegisterExtension( ... )

- RegisterExtension 的形式如下:  
void RegisterExtension(const std::string&, std::unique_ptr<WsfApplicationExtension>();

- 第一个参数是扩展的名称。  
- 您应该将此扩展命名为“register_phaserweapon”。  
- 将其设置为类型 RegisterPhaserWeapon。

- RegisterExtension 需要一个参数，该参数是一个 WsfApplicationExtension 类型的对象。

- 创建一个类型为 RegisterPhaserWeapon 的 unique_ptr（ut::make_unique<RegisterPhaserWeapon>()）。  
- RegisterPhaserWeapon 是我们的应用扩展类。  
- 注意：RegisterPhaserWeapon 是从 WsfApplicationExtension 派生的类。

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQQD.

WEAPON_EXERCISE exports void WsfPluginVersion(UtPluginVersion& aVersion)   
{ // EXERCISE 1 TASK 1 // Initialize the plugin version object using the provided macros in UtfPlugin.hpp // Use the method UtfPluginVersion(...) aVersion $=$ UtfPluginVersion(WSF PluginATION_APIMajor_VERSION, WSF PluginATION_APIMinor_VERSION, WSF PluginATION_API_COMPILER_STRING); } WEAPON_EXERCISE exports void WsfPluginSetup(WsfApplication& aApplication)   
{ // EXERCISE 1 TASK 2.a // Use the aApplication object to Register an extension. // Name this extension "register_phaserweapon". // Make it of type RegisterPhaserWeapon aApplication.RegisterExtension("register_phaser Weapon", ut::make_unique<RegisterPhaserWeapon>(); // EXERCISE 1 TASK 2.b // Tell the application that this extension, "register_phaser Weapon", depends on "wsf_mil" // Make sure that wsf_mil is loaded before we try to register our new types. // (WsfWeaponTypes and WsfWeaponEffectsTypes need to be valid)

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQQD.

![](images/0437d18625fa66342f581f404cac6b3d6220d10f7851725727507374d68ab92f.jpg)

# 武器练习1—任务2

![](images/3ec11ecb0d512118e4bf6e416b5711208fc105e2ec07421acfa7fa818c8f9fcc.jpg)

在WeaponPluginRegistration.cpp中：

任务2：完成WsfPluginSetup方法

- b部分：

- 为 wsf_mil 创建依赖关系，以便应用程序知道扩展 "register_phaserweapon" 依赖于 "wsf_mil"。  
- 调用 aApplication.ExtensionDepends(...) 方法。

- ExtensionDepends 的函数形式为:  
- void RegisterExtension(const std::string&, std::string&, bool);   
- 第一个参数是依赖扩展的名称。

- 我们的依赖扩展名称为“register_phaser weaponry”。

- 第二个参数是我们扩展所依赖的扩展的名称。

- 这是“wsf_mil”扩展。

- 第三个参数应为 true，以指示 "wsf_mil" 依赖是必需的。

- 这将确保在我们的 RegisterPhaserWeapon 类尝试注册新类型之前，wsf_mil 已加载。  
- 这是必要的，因为所有武器类都属于 wsf_mil。  
DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19.  
Other requests for this document shall be referred to AFRL/RQDD.

WEAPON_EXERCISE exports void WsfPluginVersion(UtPluginVersion& aVersion)   
{ // EXERCISE 1 TASK 1 // Initialize the plugin version object using the provided macros in UtfPlugin.hpp // Use the method UtfPluginVersion(...) aVersion $=$ UtfPluginVersion(WSF PluginATION_APIMajor_VERSION, WSF PluginATION_APIMinor_VERSION, WSF PluginATION_API_COMPILER_STRING); } WEAPON_EXERCISE exports void WsfPluginSetup(WsfApplication& aApplication)   
{ // EXERCISE 1 TASK 2.a // Use the aApplication object to Register an extension. // Name this extension "register_phaserweapon". // Make it of type RegisterPhaserWeapon aApplication.RegisterExtension("register_phaser Weapon", ut::make_unique<RegisterPhaserWeapon>(); // EXERCISE 1 TASK 2.b // Tell the application that this extension, "register_phaser Weapon", depends on "wsf_mil" // Make sure that wsf_mil is loaded before we try to register our new types. // (WsfWeaponTypes and WsfWeaponEffectsTypes need to be valid) aApplication.ExtensionDepends("register_phaser Weapon", "wsf_mil", true); }

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQQD.

38

![](images/c6b36b07e3af32035a5ae688ac2de25cdf744df759cabaa54b8db97212669113.jpg)

UNCLASSIFIED

# 应用扩展

![](images/c0003f77edbc62d24778ad15a9b5db2506702c10feb765149abd53fdb8141861.jpg)

- 要扩展一个应用程序，您必须创建一个继承自 WsfApplicationExtension 类的类：

class myAppExtension: public WsfApplicationExtension { ... }

- 您需要重写以下成员函数:

- AddedToApplication：用于接收扩展被添加到应用程序的通知——通常用于注册额外的脚本类和方法等。  
- ScenarioCreated：在场景构造函数结束时调用，以便从应用程序接收场景已创建的通知——如果需要，可以用来注册场景扩展。  
- SimulationCreated：从模拟的 Initialize 方法中调用，以便从应用程序接收模拟已创建的通知——如果需要，可以用来注册模拟扩展。  
- ProcessCommandLine：从 WsfApplication::ProcessCommandLine 方法中调用，用于检查当前参数并在必要时处理它。  
- PrintGrammar: 打印扩展所识别的扩展语法。  
- ProcessCommandLineCommands：由 WsfApplication 的 ProcessCommandLineCommands 调用，允许扩展处理/处理它需要识别的任何命令。

- 我们将创建一个名为 RegisterPhaserWeapon 的应用扩展，该扩展将向场景注册一个新的 WsfWeapon 类型和一个新的 WsfWeaponEffects 类型：

class RegisterPhaserWeapon: public WsfApplicationExtension { ... }

- 此类将重写以下成员函数:

- ScenarioCreated：在场景构造函数结束时调用，以便从应用程序接收场景已创建的通知——这对于需要注册场景扩展的情况非常有用。

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQQD.

UNCLASSIFIED

# 武器练习1—任务3

40

![](images/d037cdd4fbcd516458ab615df46b7a39b922584fdee03c153527a95ae3bbe48f.jpg)

![](images/7ae30b10e1ff4d5519c8bebd1ae55c5d62529a523ba202ca68478094d87db363.jpg)

在RegisterPhaserWeapon.hpp中完成

RegisterPhaserWeapon::ScenarioCreated的实现。

注意：添加新的武器和武器效果类型需要调用这些类型类中的静态Get方法。

这种实现隐藏了这些类型类与“核心”类型的访问方式的不同。

- 任务3a:

- 使用场景的WeaponTypes，添加一个名为PHASER_WEAPON的原型PhaserWeapon对象。

- 调用 WsfWeaponTypes 中的静态 Get 方法, 参数为 "aScenario"。此方法返回一个 WsfWeaponTypes 对象。

- 对返回的 WsfWeaponTypes 对象调用 Add 方法：  
第一个参数为武器名称"PHASER_WEapon"。  
- 第二个参数为一个PhaserWeapon原型实例的unique_ptr，可以通过ut::make_unique<PhaserWeapon>(aScenario)创建。

class RegisterPhaserWeapon : public WsfApplicationExtension   
{ public: RegisterPhaserWeapon() $=$ default; ~RegisterPhaserWeapon() noexcept override $=$ default; void ScenarioCreated(WsfScenario& aScenario) override { // EXERCISE 1 TASK 3a //! Using the scenario's WeaponTypes, Add a prototype //! Call the static "Get" Method in WsfWeaponTypes. //! Then call "Add", calling the weapon "PHASER_WE//! and provide a prototype instance of PhaserWeapon WsfWeaponTypes::Get(aScenario).Add("PHASER_WEPOIN") //EXERCISE 1 TASK 3b //! Using the scenario's WeaponEffectsTypes, //! Add a prototype PhaserLethality object called //! Call the static "Get" Method in WsfWeaponEffect//! Then call "Add", calling the weapon effect "PHASER//! and provide a prototype instance of PhaserLethal   
}   
}；

```txt
注意：在本练习中，类RegisterPhaserWeapon位于它自己的文件中，而在传感器练习中，类TricorderSensorRegistration与WsfPluginSetup位于同一个文件中。
```

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQQD.

42

![](images/9f9cfcc31325aa75950e60bf82c161b5b38dcf6166a09234304aa6a96631be97.jpg)

# 武器练习1—任务3

![](images/3e37541e8bc2206755167e219a4435be914f0cf2b4fceab77112b52dd1f9fbf4.jpg)

在WeaponPluginRegistration.cpp中：

- 任务3b:

使用场景的WeaponEffects，添加一个名为

PHASER_LETHALITY 的原型 PhaserLethality 对象。

- 调用 WsfWeaponEffectTypes 中的静态 Get 方法，参数为 "aScenario"。此方法返回一个 WsfWeaponEffects 对象。

- 对返回的 WsfWeaponEffects 对象调用 Add 方法：

- 第一个参数为武器效果名称"PHASER_LETHALITY"。  
- 第二个参数为一个PhaserLethality原型实例的unique_ptr，可以通过ut::make_unique<PhaserLethality>(aScenario)创建。

class RegisterPhaserWeapon : public WsfApplicationExtension   
{ public: RegisterPhaserWeapon() $=$ default; \~RegisterPhaserWeapon() noexcept override $=$ default; void ScenarioCreated(WsfScenario& aScenario) override { // EXERCISE 1 TASK 3a // Using the scenario's WeaponTypes, Add a prototype PhaserWeapon object called "PHASER_WEapon" //! Call the static "Get" Method in WsfWeaponTypes with the argument of "aScenario". //! Then call "Add", calling the weapon "PHASER_WEapon", //! and provide a prototype instance of PhaserWeapon. WsfWeaponTypes::Get(aScenario).Add("PHASER_WEapon", ut::make_unique<PhaserWeapon>(aScenario)); // EXERCISE 1 TASK 3b // Using the scenario's WeaponEffectsTypes, //! Add a prototype PhaserLethality object called "PHASER_LETHALITY" //! Call the static "Get" Method in WsfWeaponEffectTypes with the argument of "aScenario" //! Then call "Add", calling the weapon effect "PHASER_LETHALITY", //! and provide a prototype instance of PhaserLethality. WsfWeaponEffectsTypes::Get(aScenario).Add("PHASER_LETHALITY", ut::make_unique<PhaserLethality>(aScenario));   
}   
};

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQQD.

44

![](images/52dbd0334a7b71a402ccd43fe16482dc447f9e3b4f9326ca7f50571ca83ba219.jpg)

# UNCLASSIFIED AFSIM插件&扩展 AFSIM mission启动流程

![](images/3a435bfa3a09bcbac70ef63dbf114d75b506a5ac5ade98c6293698ef845f1f48.jpg)

![](images/263253249c2437311cf638e2bea9471de870193e79af0621556ab2a8e0af3b82.jpg)

WsfStandardApplication构造函数利用插件管理器查找并加载所有插件（包括训练文件夹中的插件——这是因为CMake选项WSF_ADD_EXTENDED_PATH的设置）。

- 对于找到的每个插件，都会执行 WsfPluginSetup（注意：这会导致我们Phaser练习插件的WsfPluginSetup函数被执行）。  
- 这会导致我们Phaser练习的RegisterPhaserWeapon类（这是一个应用扩展）被创建并注册到应用程序中。  
- RegisterExtension 随后调用 WsfApplicationExtension::AddedToApplication()。

注意：RegisterPhaserWeapon 并未重写 AddedToApplication，因此此通知没有任何效果。

![](images/fdfaef6703b6eaaa5225d42704769344335a07731c3951407cdfe5eb3b2913bc.jpg)

Mission 然后向应用程序注册所有必要的预定义扩展。

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQQD.

46

![](images/1cd7301780b9f52a8433c28a82ce47af1f4ae63d4e3c8634896a23a0adbacdb2.jpg)

# UNCLASSIFIED AFSIM插件&扩展

# AFSIM mission启动流程

![](images/1f02e26fbb03d009e62e0a454e1f47d9f2314253d375ee87bb0f9925543a6b8d.jpg)

![](images/79227c8bd4ca50c7728258cf64e9a386b3b13d126ac98fc1f833850d3093d26d.jpg)

Mission 然后创建场景并调用 WsfScenario 构造函数：

WsfScenario scenario(app);

- 此构造函数会调用 WsfApplication::ScenarioCreated() 方法。  
- 接着，这会调用所有已注册的应用扩展的 ScenarioCreated() 方法（包括我们的 RegisterPhaserWeapon 扩展）。  
- RegisterPhaserWeapon::ScenarioCreated() 会创建并将 PHASER_WEAPON 类型添加到武器类型列表中，以便在场景文件中找到 PHASER_WEAPON 命令时，可以调用它们的 ProcessInput() 方法。

![](images/336d538671f94e5fff74067ad1f2ce9029f3d50c52791671a5519fe3140ad795.jpg)

# Mission 调用 app.WsfStandardApplication::ProcessInputFiles()

- 该方法会调用 WsfScenario::LoadFromFile()

这是因为这些类是从核心类派生而来的。

对于输入中的每个命令：，

- 调用每个核心类的 ProcessInput() 方法

调用PhaserWeapon::ProcessInput()来处理PhaserWeapon命令

调用PhaserLethality::ProcessInput()来处理damage_rate命令

- 调用每个已注册场景扩展的ProcessInput()方法——但由于没有为Phaser定义场景扩展，因此此调用没有效果。

注意：在场景输入文件中，当遇到PHASER_WEapon类型的武器块时，会创建一个PhaserWeapon对象；当遇到PHASER_LETHALITY类型的武器效果块时，会创建一个PhaserLethality对象。

48

![](images/3ae938659cdbc16fb0c9615dc90629db77afe6a9d1cda5dbabc34c184e21e1dd.jpg)

# UNCLASSIFIED AFSIM插件&扩展

# AFSIM mission启动流程

![](images/0ff17caa45423a11da2d2218bb6e01c410343139ab24b7e96895676bfca26041.jpg)

![](images/182fb1f47e57dbc327726cc63654d39a14bb4c7e557a4e252216216c38ec4dac.jpg)

Mission 调用 app.WsfStandardApplication::ProcessInputFiles(),

该方法会调用 WsfScenario::LoadFromFile(),

然后调用 WsfScenario::CompleteLoad()。

- 调用每个场景扩展的 Complete() 方法。  
- 然后调用每个场景扩展的 Complete2() 方法。

注意：我们的类中没有继承自 WsfScenarioExtension 的类，因此没有需要调用的 Complete 或 Complete2 方法。

![](images/6d154cb63f7519b4430c3a25f9d3f838a5a267d2cdfa45f295b1834e01d2148a.jpg)

Mission 通过执行以下代码创建模拟：

```cpp
std::unique_ptr<WsfSimulation> simPtr = app.CreateSimulation(scenario, ...); 
```

- CreateSimulation 调用 WsfSimulation 对象的构造函数（以 scenario 作为参数）。

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQQD.

50

![](images/6f617975e320257bf0da977c1b03f5af23f50520d4f8960dd6d90aaef0374d78.jpg)

# UNCLASSIFIED AFSIM插件&扩展 AFSIM mission启动流程

![](images/5e3c025321dfcf35d3920d817268b3ef8fb0fb6b88ee835c5832d4158bb90bf8.jpg)

![](images/9d68d45a8eabb36ff860d4285b17d29dc299514e233b6dcf783e4dc1ffe1ccab.jpg)

Mission 通过执行以下代码初始化模拟：

```kotlin
app.InitializeSimulation(simPtr.get()) 
```

- InitializeSimulation 调用: aSimPtr->Initialize()

（其中aSimPtr $\equiv$ simPtr.get()）

![](images/2d3107c3ba19730dcaa347b982f320393f66e984d0d1a69e15462105f1df16b9.jpg)

Mission 通过执行以下代码初始化模拟：

app.InitializeSimulation(simPtr.get())

- InitializeSimulation 调用: aSimPtr->Initialize()   
- WsfSimulation::Initialize 调用: mScenario.SimulationCreated(*this)

(其中mScenario $\equiv$ scenario，\*this $\equiv$ *simPtr.get()）

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQQD.

52

![](images/7d25e0b9478fad8e8cac3894f4888fba81916fd419863ac94479c1f717673c5c.jpg)

# AFSIM插件&扩展

# AFSIM mission启动流程

![](images/836a120fd0def0a221ce41ddfbd6550073b2dab39a920903e0fb06e528166669.jpg)

![](images/f8c89c7ca978979fc5f2f7c91d468ff290fca7827274cb242136383fd243d90b.jpg)

Mission 通过执行以下代码初始化模拟：

app.InitializeSimulation(simPtr.get())

- InitializeSimulation 调用: aSimPtr->Initialize()   
- WsfSimulation::Initialize 调用: mScenario.SimulationCreated(*this)   
- SimulationCreated 调用: GetApplication().SimulationCreated(aSimulation)

（其中GetApplication() $\equiv$ app，aSimulation $\equiv$ *simPtr.get()）

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19.

Other requests for this document shall be referred to AFRL/RQQD.

![](images/59168ae841b329690394952ea3d1ec9e4c8847a8673ffa4ce0283db7522ea4f4.jpg)

Mission 通过执行以下代码初始化模拟：

app.InitializeSimulation(simPtr.get())

- InitializeSimulation 调用: aSimPtr->Initialize()   
- WsfSimulation::Initialize 调用: mScenario.SimulationCreated(*this)   
- SimulationCreated 调用: GetApplication().SimulationCreated(aSimulation)

- 对每个应用扩展调用 SimulationCreated(aSimulation)

(其中aSimulation $\equiv^{*}\mathrm{simPtr.get()}$

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19.

Other requests for this document shall be referred to AFRL/RQQD.

54

![](images/3bf44c9a3cccef9ef9520c7c5f1fa2821a41694a51f583731b93d3b61fed6691.jpg)

# AFSIM插件&扩展

# AFSIM mission启动流程

![](images/6e107e112e9f9cf5cb1ef128fe80ce322b4d09ca3bbf72aee5224c7e98dfafbc.jpg)

![](images/b612085149d66e3dac44eabd6663c61e59fa08d504c11786b696b7da5533736a.jpg)

Mission 通过执行以下代码初始化模拟：

app.InitializeSimulation(simPtr.get())

：

- SimulationCreated 调用: GetApplication().SimulationCreated(aSimulation)

- 对每个应用扩展调用SimulationCreated(aSimulation)  
- 调用 WsfApplicationExtension::SimulationCreated(aSimulation)

（其中aSimulation $\equiv^{*}\mathrm{simPtr.get()}$ ）

Note: RegisterPhaserWeapon does not override SimulationCreated, so this call has no effect 55
![](images/bc71294f2bb89ffdc18dc7bcb91979616190510aeb9ff757c806538b2814417f.jpg)

Mission 通过执行以下代码初始化模拟：

app.InitializeSimulation(simPtr.get())

- InitializeSimulation 调用: aSimPtr->Initialize()

：

- 接下来, WsfSimulation::Initialize 调用:

WsfObserver::SimulationInitializing(this)

- 这会通知所有已注册的事件观察者，模拟即将被初始化。

注意：我们没有创建任何模拟观察者，因此该通知没有任何效果。

56

![](images/da2c7cf0b20a2ddab388340b1cd790e767f222c7b91c445a0e6fba7adefea730.jpg)