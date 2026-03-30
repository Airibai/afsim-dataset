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

# UNCLASSIFIED

# AFSIM插件&扩展

# AFSIM mission启动流程

![](images/a432882950fbd2df63d0ce4990eca5c081ffedb05ce459c1717a84ec427ac1e7.jpg)

![](images/51dc01ae97e75bf3b692a73537864b0f4afa0cc8dc89021d6f6ed6da3adbef59.jpg)

Mission 通过执行以下代码初始化模拟:

app.InitializeSimulation(simPtr.get())

• InitializeSimulation 调用: aSimPtr->Initialize()

中

- 下一步, Initialize 调用: Initialize() 在所有的仿真扩展中

- 这没有任何效果，因为没有用于相位器的模拟扩展。

![](images/1b9cfc3aef15aa15f2bd8c7584bc2919dc70f6cd8d1840357c0e897c69879a80.jpg)

Mission 通过执行以下代码初始化模拟:

app.InitializeSimulation(simPtr.get())

- InitializeSimulation 调用: aSimPtr->Initialize()

：

- 接下来，WsfSimulation::Initialize 将所有可用的平台添加到模拟的平台列表中。  
- 最后，WsftSimulation::Initialize将模拟状态设置为cPENDING_START。

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQQD.

58

![](images/7fa02bc01b7f2a32e8879fff5f7dda440293924382d6ad8cd788f3917c8acf90.jpg)

# UNCLASSIFIED

# 练习2

![](images/3344464ec1e3f972d3f48a6d54907d26a837bc63e548be621ed4204c1fd9aa06.jpg)

- 理解并完成相位器ProcessInput方法的实现（PhaserWeapon::ProcessInput和PhaserLethality::ProcessInput）。  
- 理解武器如何开火，以及其效果如何应用于目标。  
- 完成与发射相位器相关的方法的实现。

- 检查文件 WsfWeapon.hpp 和 WsfWeapon.cpp。

- 注意其继承自 WsfArticulatedPart。  
- 武器可以被瞄准。

- 特别是，检查 Fire 方法。

- 注意该方法是通用的，并接受三个参数。

- 检查定义在 WsfWeapon.hpp 中的通用参数 FireTarget 和 FireOptions。

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQQD.

60

![](images/5e2c3f32c8ef4f3d03e47522e04d3aa55c61227ddb9d20025c3709b162661c59.jpg)

# UNCLASSIFIED 武器练习2—检视1

WsfWeapon.hpp

![](images/a7256c92c3d94bc35f0cc05fb8ba2b847927037141dcec269b1c6726c601d94a.jpg)

```txt
class WsfWeapon : public WsfArticulatedPart   
public: WsfWeapon(const WsfScenario& aScenario); ~WsfWeapon() override; virtual FireResult Fire(double aSimTime, const FireTarget& aTarget, const FireOptions& aSettings); virtual bool FireSalvo(double aSimTime, const FireTarget& aTarget, const SalvoOptions& aSettings); virtual void CeaseFire(double& aSimTime) override; WsfTrack* CreateTargetTrack(double aSimTime, const WsfTrack* aTrackPtr); bool GetTargetLocationWCS(double aSimTime, const WsfTrack* aTrackPtr, double aTargetLocWCS[3]); 
```

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQDD.

```cpp
class FireTarget   
{ public: FireTarget() : mTrackPtr(nullptr) { } FireTarget(const WsfTrack* aTrackPtr) : mTrackPtr(aTrackPtr) { if (mTrackPtr != nullptr) { mTrackId = mTrackPtr->GetTrackId(); } } //! A pointer to the track that represents the target. //! If mTrackPtr is null, will attempt to use //! WsfPlatform::GetCurrentTarget(). const WsfTrack* mTrackPtr; //! The target name against which to fire the weapon. std::string mTargetName; WsfTrackId mTrackId; // For convenience only... //! An string indicating a targeted sub-region of the target //! (e.g., "canopy", "irst", "stabilizer"). This offset must //! be recognized by and used by the weapon effects type //! associated with the weapon. std::string mTargetOffset; 
```

```cpp
class FireOptions   
{ public: FireOptions() : mWeaponId(0) {FireOptions(int aWeaponId) : mWeaponId(aWeaponId) {} //! The weapon id assigned to an allocated //! weapon platform. int mWeaponId; //! Name of the explicit weapon platform. If //! empty, the weapon will create a new unique //! name. std::string mWeaponPlatformName; //! Name of the weapon component that will be //! used to fire. WsfStringId mWeaponComponentName; }; 
```

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQDD.

62

![](images/52274f5c2f6453756c4d4d03bb8948063a060b5d5572434cbc93389684235099.jpg)

UNCLASSIFIED

# 武器练习 2- 检视2

![](images/706cf9e28e3f8e983f8fc4e290f1538a19586e29d2346be3ad8a235fe22e2d3b.jpg)

- 检查文件 PhaserWeapon.hpp。

- 注意其继承自 WsfImplicitWeapon。  
- 检查为我们的解决方案假定的类属性和函数。

- 特别是，检查 Fire 方法。

- 注意该方法是通用的，并接受三个参数。

- 在本练习中，您将修改PhaserWeapon.hpp和PhaserWeapon.cpp。

```txt
class PhaserWeapon : public WsfImplicitWeapon { 
```

```txt
public: //! Constructor explicit PhaserWeapon(WsfScenario& aScenario); 
```

```rust
//! Virtual destructor  
~PhaserWeapon() noexcept override = default; 
```

```txt
WsfWeapon* Clone() const override;  
bool ProcessInput(UtInput& aInput) override; 
```

```txt
FireResult Fire(double 
```

```txt
const FireTarget& 
```

```txt
const FireOptions& 
```

```txt
aSimTime, 
```

```txt
aTarget, 
```

```txt
aSetting 
```

```javascript
protected: //! Copy Constructor; used by clone PhaserWeapon(const PhaserWeapon& aSrc); PhaserWeapon& operator=(const PhaserWeapon& aSrc); 
```

private: boolFireUpdate(double aSimTime, WsfStringId aTargetName); void FireComplete(double aSimTime, WsfStringId aTargetName); void DisplayEngagement(WsfStringId aTargetName, bool aErase $=$ false);

```txt
：
```

//! FireUpdateEvent is executed at a regular   
//! Interval to apply damage from the phaser to   
//! the target   
class FireUpdateEvent : public WsfEvent   
{ public: FireUpdateEvent(); ~FireUpdateEvent() noexcept override $\equiv$ default EventDisposition Execute() override; // EXERCISE 1 TRAINING TASK 2 // PLACE YOUR CODE HERE bool mComplete;   
}；

```rust
//! Phaser effects are applied at this discrete
//! time interval; units are in seconds
double mFireIntegrationInterval;
//! Each time the phaser fires, it keeps the beam
//! on the target for this much time in seconds
double mFireDuration;
//! Display firing and lethality data using WsfDraw
bool mDisplayEngagements; 
```

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQQD.

64

![](images/69fa3350a9b75c23dd56a7dd70256e52e359b804babd4adc8cffb2f835661973.jpg)

# UNCLASSIFIED

# 武器练习2-检视3

![](images/77011d4ecb640c76f0f39a6ffe89cc881ae170d5892e054026cfd0a8dc44e25d.jpg)

- 检查文件 PhaserLethality.hpp。

- 注意其继承自 WsfWeaponEffects。  
- 检查为我们的解决方案假定的类属性和函数。

- 特别是，检查 ApplyEffectTo 方法。

- 注意该方法会影响单个目标。  
- 注意 PhaserLethality.cpp 中的调用/交互顺序与 WsfWeaponEffects.cpp 中的调用/交互顺序的区别。

class PhaserLethality : public WsfWeaponEffects   
public: explicit PhaserLethality(WsfScenario& aScenario); PhaserLethality(const PhaserLethality& aLethality); PhaserLethality& operator=(const PhaserLethality&) $=$ delete; \~PhaserLethality() noexcept override $=$ default; WsfWeaponEffects* Clone() const override { return new PhaserLethality(\*this); } bool ProcessInput(UtInput& aInput) override; bool Initialize(double aSimTime, const WsfWeaponEngagement\* aEngagementPtr) override; protected: void ApplyEffectTo(double aSimTime, WsfPlatform\* aTargetPtr) override;

```txt
private: //! For each second of beam on target, the shield //! is reduced by this amount double mShieldDamageRate; //! Once the shield is gone, the armor is reduced //! by this amount. double mArmorDamageRate; //! The last time we applied damage to the target double mLastUpdateTime; 
```

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQQD.

66

![](images/faa9eb28763d2024e9998e360d1b4f3b21d3cfb88991f8f9855bd4c33b89ecda.jpg)

UNCLASSIFIED

# ApplyEffectTo

![](images/19c27c72a6fe715461fe1f5145170adbab1c43568bd86a5fe7bee10ca63317af.jpg)

- 在 WsfWeaponEffects::ApplyEffectTo 中,  
- 对平台的伤害按以下方式应用：

如果平台是不可摧毁的，  
- 基于 PK 约束（Probability of Kill，击杀概率）的持续对数衰减伤害会被施加到平台上，但平台永远不会被摧毁。

如果平台是可摧毁的，

- 会计算一个随机数来决定伤害量。如果随机数小于击杀概率（Probability of Kill），则平台被摧毁；否则，不会造成任何伤害。

- 在PhaserLethality::ApplyEffectTo中，  
- 对带有护盾的平台的伤害按以下方式应用：

- 首先对护盾造成伤害，按一定增量减少护盾值，直到护盾值为0。  
- 一旦护盾值减少到0，伤害会按一定增量作用于平台的装甲，直到装甲值为0。  
一旦装甲值减少到0，平台被摧毁。

- 在文件 PhaserWeapon.hpp 中,  
- 向PhaserWeapon::FireUpdateEvent类添加成员变量，用于存储以下内容：

剩余的开火时间（double类型）  
- 持有目标轨迹的实体的平台索引（int 类型）  
- 武器指针（PhaserWeapon* 类型）  
目标名称（WsfStringld类型）

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQQD.

68

![](images/8e70381b2a3916011c4b5034181d1a2d7a3a1f015c6ff699d2fcec5abf7f1042.jpg)

# UNCLASSIFIED 武器练习2—任务1解决方案

# PhaserWeapon.hpp

![](images/faed1486697f84afb6cb6305be90485edadd4ae303c5cea903db4640e5624440.jpg)

class FireUpdateEvent : public WsfEvent   
{ public: FireUpdateEvent(); ~FireUpdateEvent() noexcept override $=$ default; EventDisposition Execute() override; //EXERCISE 2 TASK1 double mFireTimeLeft; size_t mPlatformIndex; PhaserWeapon\* mWeaponPtr; WsfstringId mTargetName; bool mComplete;   
}；

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQDD.

请记住，ProcessInput 方法是在加载场景时调用的。

- ProcessInput 是一个虚方法，它以多态的方式执行（从最派生对象的 ProcessInput 方法开始）。

![](images/c8da6665567e1943fcba6ee437f2b5e6fda04b1c2b4e15bfc5086a22a703c9cc.jpg)

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQQD.

70

![](images/14dfde1e8b3783155deee7273c27b70c249ca43906117e3502eb25744a4deb4f.jpg)

UNCLASSIFIED

# 武器练习2—任务2

![](images/e5d68d97b7ceca8875a615e9bfb9a470da83f06f4172e566169f218cc530d886.jpg)

在文件 PhaserLethality.cpp 中:

- 实现 PhaserLethality::ProcessInput 方法以读取：  
  - 通过 alInput.ReadValue() 读取 armor DAMAGE_rate。

可以通过在源代码中搜索对“ReadValue”和“ReadValueOfType”的引用来找到AFSIM示例。

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQQD.

```cpp
bool PhaserLethality::ProcessInput(UtInput& aInput)  
{ bool myCommand = true; std::string command = aInput.GetCommand(); if (command == "shield DAMAGE_rate") { aInput.ReadValue(mShieldDamageRate); } else if (command == "armor DAMAGE_rate") { // EXERCISE 2 TASK 2 aInput.ReadValue(mArmorDamageRate); } return myCommand; } 
```

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQQD.

# UNCLASSIFIED

# 武器练习 2 — 任务3

72

![](images/66390d204039114c032de71bbf1eecee479cad47374c863ccdd2079a4555d7a6.jpg)

![](images/97893b5d961255f5fc41aa41388b7ab8db8c3dea3abe8e08fadd8dffa1c1f9ca.jpg)

在文件 PhaserWeapon.cpp 中:

- 实现 PhaserWeapon::ProcessInput 方法以读取：

- 通过 alinput.ReadValueOfType() 读取 fire_integration_interval，其类型为 cTIME。

- 请记住，ProcessInput 方法是在加载场景时调用的。

- ProcessInput 是一个虚方法，它以多态的方式执行（从最派生对象的 ProcessInput 方法开始）。

可以通过在源代码中搜索对“ReadValue"和“ReadValueOfType"的引用来找到AFSIM示例。

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQQD.

```cpp
bool PhaserWeapon::ProcessInput(UtInput& aInput)  
{  
    ...  
    else if (command == "fire_integration_interval")  
{  
        // EXERCISE 2 TASK 3  
        aInput.ReadValueOfType(mFireIntegrationInterval, UtInput::cTIME);  
    }  
    return myCommand; 
```

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQQD.

# UNCLASSIFIED

# 武器练习2—任务4

74

![](images/5f2666c9764965467cd51b51a7a211ae3ec63a650ac8cacd45fb4c51cad0c119.jpg)

![](images/ebb96f24fd49b6876b101204d425d5a3d519c7e0fe426a35ddc316547873d2a2.jpg)

# 在PhaserWeapon.cpp中：

# - 实现PhaserWeapon::Fire

- 按照由 fire_integration_interval 决定的离散时间间隔应用效果。

一种实现方式是通过一个新的 WsfEvent 类型。  
- 我们已经创建了一个新的事件类，名为PhaserWeapon::FireUpdateEvent，它是WsfEvent的子类。

# 任务4a:

- 创建一个新的FireUpdateEvent指针，命名为eventPtr。  
- 适当地填充 eventPtr 的所有属性（mTargetName 除外，它已经在其他地方完成）。

- mPlatformIndex 设置为 GetPlatform()->GetIndex().  
- mWeaponPtr 设置为指向当前对象的指针（即相同的 WsfWeapon 对象）。

# 任务4b：

- 将mFireTimeLeft设置为整个开火持续时间（mFireDuration）。  
- 使用 WsfEvent 基类方法 SetTime，将事件的执行时间设置为 aSimTime + mFireIntegrationInterval。

- 注意 eventPtr 是如何被添加到所属的 WsfSimulation 的事件队列中的。

```cpp
WsfWeapon::FireResult PhaserWeapon::Fire(double aSimTime, const WsfWeapon::FireTarget& aTarget, const WsfWeapon::FireOptions& aSettings)   
{ // Call base class' Fire method WsfWeapon::FireResult result = WsfImplicitWeapon::Fire(aSimTime, aTarget, aSettings); // EXERCISE 2 TASK 4a // Create a new fire update event (pointer) // Set the attributes of the event for // - firing platform index // - the firing weapon auto eventPtr = ut::make_unique<FireUpdateEvent>(); eventPtr->mPlatformIndex = GetPlatform()->GetIndex(); eventPtr->mWeaponPtr = this; ... if(result.mSuccess) { // EXERCISE 2 TASK 4b // Set the attributes of the event for // - the fire time left (initially, set to the fire duration) // - the time to fire the event (after one fire integration interval) eventPtr->mFireTimeLeft = mFireDuration; eventPtr->SetTime(aSimTime + mFireIntegrationInterval); GetSimulation()->AddEvent(std::move(eventPtr)); return result; } DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-15 Other requests for this document shall be referred to AFRL/RQDD. 
```

# UNCLASSIFIED

![](images/7508519eec42d9225b5f5073d534d71887cfc5278f1f1b5549b958bba195a6a6.jpg)

# 武器练习2—任务5

76

![](images/d8c56db84559c196a29f4101cfb8d12ad85bac03734a906a03b68730116b65be.jpg)

# 在PhaserWeapon.cpp中:

# - 完成FireUpdateEvent的Execute方法。

- 请注意，FireUpdateEvent::Execute会调用PhaserWeapon::FireUpdate方法。

- 任务5a:

- 更新“剩余开火时间”变量，将其减少武器的开火积分间隔（fire integration interval）。

- 如果剩余开火时间为正值，则表示射击尚未完成。因此，我们必须重新安排事件（Reschedule the event）。

- 任务5b:

- 将事件的执行时间设置为下一个开火积分间隔之后，或者剩余开火时间之后，以较小者为准。

- 请注意，对于事件的重新安排（Rescheduling），我们需要返回 WsfEvent::EventDisposition 的值 cRESCHEDULE。

```cpp
WsfEvent::EventDisposition PhaserWeapon::FireUpdateEvent::Execute()
{
    // Ensure the firing platform is still alive during the engagement
    if (GetSimulation()->PlatformExists(mPlatformIndex))
        {
            bool repeat = mWeaponPtr->FireUpdate(GetTime(), mTargetName);
        }
        if (repeat)
            {
                // EXERCISE 2 TASK 5a
                // Compute the remaining fire time
            }
        }
        mFireTimeLeft -= mWeaponPtr->mFireIntegrationInterval;
        if (mFireTimeLeft > 0.0)
            {
                // EXERCISE 2 TASK 5b
                //Set the time the event will next execute to the end of the fire time
                //or the next integration update time, whichever is first.
            }
        SetTime(GetTime() + std::min(mWeaponPtr->mFireIntegrationInterval, mFireTimeLeft));
        mComplete = false;
        }
        if (mComplete)
            {
                // Set the last time the event will execute to a slightly later
                //time. This is a common practice; in this case it allows the
                // WsfDraw erase command to execute properly.
                SetTime(GetTime() + 0.001);
            }
        }
    return disposition;
} DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19.
Other requests for this document shall be referred to AFRL/ROOD. 
```

78

![](images/dafc1bdc741db2c60a2f412bed0cd45087a064050c3bcd82233495690ddb9e62.jpg)

# 武器练习2—检视4

![](images/8124af8c4cc6159fd16f5a25d5b0c38e1600ceb6c1d12f2513530caed37c1be5.jpg)

在文件PhaserWeapon.cpp中：

- 检查PhaserWeapon类的FireUpdate方法。

代码确保平台和目标不会被地球地平线遮挡，使用UtSphericalEarth::MaskedByHorizon方法进行判断。  
- 当前的交战对象（engagement object）会被更新。  
- 交战对象会进一步更新我们当前的武器效果（PhaserLethality）。

bool PhaserWeapon::FireUpdate(double aSimTime, WsfstringId aTargetName)   
{ bool repeatFireIsNeeded $=$ false; WsfPlatform\*targetPtr $\equiv$ GetSimulation()->GetPlatformByName(aTargetName); if(targetPtr != nullptr) { double wpnLat, wpnLon, wpnAlt; GetLocationLLA(wpnLat, wpnLon, wpnAlt); double tgtLat, tgtLon, tgtAlt; targetPtr->GetLocationLLA(tgtLat, tgtLon, tgtAlt); // Verify the target isn't masked by the earth's horizon if(!UtSphericalEarth::MaskedByHorizon(wpnLat, wpnLon, wpnAlt, tgtLat, tgtLon, tgtAlt, 1.0)) { repeatFireIsNeeded $=$ true; //Update the engagement. It will apply damage and destroy any targets. GetEngagement(-)>Update(aSimTime); if(mDisplayEngagements) { DisplayEngagement(aTargetName); } } return repeatFireIsNeeded; }

```txt
DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQQD. 
```

80

![](images/abb0929dd6c94f2048dd60645f08c3f5a15e78e6be67c8ae0287e10a4a56bb12.jpg)

# UNCLASSIFIED

# 武器练习 2 — 任务 6

![](images/2f319a323cebe54f7f5f30e0810c0101da87009ea28e6aecc618b8b0136f62a2.jpg)

在文件PhaserLethality.cpp中：

- 修改PhaserLethality::ApplyEffectTo方法。

- 对平台的护盾和/或装甲施加伤害。  
- 注意使用 WsfUtil::GetAuxData 方法访问平台的辅助数据（aux data），以获取护盾和装甲信息。

- 任务6：

1. 如果护盾值为正：  
- 根据护盾伤害速率（shield damage rate）和积分时间（integration time）减少护盾值。  
2. 否则：  
- 护盾已耗尽，将护盾值设置为零，并根据装甲伤害速率（armor damage rate）和积分时间减少装甲值。

3. 注意：如果平台的装甲值降到 0 以下，将伤害变量设置为 WsfWeaponEffects::cKILLED。

4. 注意使用 WsfPlatform 的 GetAuxData().Assign() 方法来重置修改后的辅助数据值。

void PhaserLethality::ApplyEffectTo(double aSimTime, WsfPlatform* aTargetPtr)   
{ WsfPlatform* weaponPlatformPtr = GetEngagement()-GetFiringPlatform(); double integrationTime $=$ aSimTime - mLastUpdateTime; double damage $= 1.0\mathrm{e} - 6$ ; // always apply some damage. if ((weaponPlatformPtr != nullptr) && (integrationTime > 0.0)) { double shields(0.0); double armor(100.0); // Get the shield and armor data from the auxiliary data container on the target platform WsfUtil::GetAuxValue(aTargetPtr, "phaser_shields", shields); WsfUtil::GetAuxValue(aTargetPtr, "phaser_armor", armor); // EXERCISE 2 TASK 6 // Reduce shields based on damage rate shields -- mShieldDamageRate * integrationTime; if (shields <= 0.0) { // If shields are down then reduce armor base on damage rate shields $= 0.0$ armor $=$ armor - mArmorDamageRate \* integrationTime; } // If armor is depleted, target is killed and removed if (armor <= 0.0) { armor $= 0.0$ damage $=$ WsfWeaponEffects::ckILLED; } DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19.

![](images/a40995f25622b93122f3e405ae1248e20a0922c46688de4d93513670cd6c9081.jpg)

# UNCLASSIFIED武器练习2—任务6解决方案PhaserLethality.cpp

![](images/fb1bfbf2623b5045285e50e0a47f2029ba4ab625b194c2e372fd7463254a780e.jpg)

```cpp
void PhaserLethality::ApplyEffectTo(double aSimTime, WsfPlatform* aTargetPtr)  
{  
    WsfPlatform* weaponPlatformPtr = GetEngagement()->GetFiringPlatform();  
    double integrationTime = aSimTime - mLLastUpdateTime;  
    double damage = 1.0e-6; // always apply some damage.  
if ((weaponPlatformPtr != nullptr) && (integrationTime > 0.0))  
{  
    // If armor is depleted, target is killed and removed  
    if (armor <= 0.0)  
    {  
        armor = 0.0;  
        damage = WsfWeaponEffects::ckILLED;  
    }  
    // Set the new shield and armor values in the auxiliary data container  
aTargetPtr->GetAuxData().Assign("phaser_shields", shields);  
aTargetPtr->GetAuxData().Assign("phaser_armor", armor);  
}  
//! Reflect the last update time.  
mLastUpdateTime = aSimTime;  
// Call the base class to apply any damage to the target.  
ApplyEffectIncrement(aSimTime, aTargetPtr, damage); 
```

- 对于隐式武器（implicit weapons）要终止一次交战（engagement），必须满足以下条件之一：

- 拥有一个关联的发射计算机（launch computer），用于定义飞行时间（time of flight）；或者  
调用该武器的CeaseFire方法。

请审阅并理解：

```cpp
void PhaserWeapon::FireComplete(double aSimTime, WsfstringId aTargetName) { if (mDisplayEngagements) { DisplayEngagement(aTargetName, true); // Erase any engagement data } // Call base class' method to automatically terminate the engagement. WsfImplicitWeapon::CeaseFire(aSimTime); } 
```

注意：PhaserWeapon 的 FireComplete 方法会显式调用 CeaseFire。

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19.

Other requests for this document shall be referred to AFRL/RQQD.

# UNCLASSIFIED

![](images/c23d665aeab28c10ace7949c0597edf25cf956accbf26a876944c5cb1a8a246a.jpg)

# 测试(1/2)

84

![](images/ca85f576e0a7234150f10d5041208bceb7649daf435c9d32d107abcfb5fa635e.jpg)

- 从 Visual Studio 执行以下步骤：

1. 在“Release”模式下构建解决方案。  
2. 构建“INSTALL”项目。

Linux: 在构建的目录中，运行：

$$
\begin{array}{l} \$ \text {c m a k e} - - \text {b u i l d} . - - \text {t a r g e t a l l} - - j 1 1 \\ \$ \text {c m a k e} - - \text {b u i l d} . - - \text {t a r g e t i n s t a l l} - - j 1 1 \\ \end{array}
$$

- 加载测试场景到 WIZARD:

1. 打开 WIZARD。  
2. 找到位于 $\backslash$ weapon\data 文件夹中的顶级场景文件，名为

weaponscenario.txt。这是我们用来测试程序的输入文件。

3. 将 weaponscenario.txt拖放到 WIZARD 中。

- 从 WIZARD 中运行选定的应用程序。

- 在项目浏览器 (Project Browser) 中双击 weaponscenario.aer 文件，以在Mystic中查看。

![](images/c1e5d83da6990ffc4575febaaef513f364e5390ed8d5a36f24335fbf06a47e49.jpg)

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQQD.

86

![](images/914e9ac0c96161a1b0c125608737ccf1c4bbcbafbc951bad41db8cf260dc198b.jpg)

![](images/b386e39b0a925f9f60d676a2174e7ea9569e6ad8f256b6679ac4fe4d407c067f.jpg)

![](images/791251aed8887e34b46d0b3bbe30e92bb441f6e097aded99c1347726215d872c.jpg)

87

# 6.2.1.7. 运动 6_AFSIMDev_Trng_Movers

本文为afsim2.9_src\training\developer\core\slides\

6_AFSIM_DeTrng_Movers.pptx 的翻译，主要是介绍如何扩展自定义运动，并做了许多小练习。

![](images/197368c770d447eb78e182b3a6853258464f0e1bac40bc6acd71b4ae8d9c5070.jpg)

Integrity $\star$ Service $\star$ Excellence

# AFSIM开发培训

# 6 - 运动

本文档由杨石兴翻译，该资料做为《AFSIM2.9参考手册》的一部分。没有《AFSIM2.9参考手册》的加杨石兴微信领取：13324598743

# AFRL/RQQD 美国空军研究实验室

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

# UNCLASSIFIED

![](images/d3d36b266ffb3091f7f356616c587171a26fab822fcde94dd46881b3ea55027e.jpg)

# 缩写与术语

![](images/efa20b628885f147a118694a95c7383786340d6a0f7fd163d46abe7d0845183c.jpg)

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

- 本实验演示了如何创建一个新的AFSIM mover。  
- Mover 是一个平台组件，负责维护其附加平台的运动学状态（位置、方向、速度、加速度等）。  
- 以下练习提供了操作AFSIM movers的实践机会：

练习1：注册AFSIMMover  
- 练习2：创建一个自定义的AFSIMMover  
- 练习3[可选]：编译一个MATLAB共享库

- 注意：除非您的计算机上安装了 MATLAB，否则此练习只能在运行于 Microsoft Windows 的 Microsoft Visual Studio 中完成。

![](images/ec2b16bd94c354350c46db964e4a57de29e3b43b4acc0df33423effb53e8f12f.jpg)

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

3

![](images/3a89321157154edad0e1f87559327c926c860482b44cb040228548320780ef91.jpg)

# UNCLASSIFIED

# 问题陈述

![](images/3f7d8500574e332b282caf63114a901b826dc363afc9db1ea8ea63e13c5e945e.jpg)

- 您将创建一个新的 mover 类型，名为 MATLAB BALLISTIC_MOVER。

- 该 mover 表示一个简单的多级弹道导弹。  
- 运动学计算将使用 MATLAB® 动态链接库 (DLL) 来执行。

- 为实现这一目标，我们将创建一个新的插件和一个新的应用程序扩展。

参考资料：

- AFSIM 开发者基于 Web 的数据。  
- AFSIM 源代码和 Visual Studio 搜索功能。  
- AFSIM 文档。

![](images/2e707c8709b19b5e93eafd76ad24fa89cdc5a5edaab31b529b7bc7405b876826.jpg)

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19.

Other requests for this document shall be referred to AFRL/RQQD.

- 您将获得以下方面的实践知识:

- 创建新的 mover 类型。  
- 为多级弹道 mover 实现一个 "Update" 方法。  
- 使用 MATLAB® 编译器运行时库工具来初始化、交互以及终止 MATLAB 编译的 DLL。  
- 创建新的脚本类型。

- 强化您在创建应用程序扩展和插件方面的技能。

![](images/1e96a56ef7e9dbebfd15eb972bd73f85c15b500c6115f25525e8963d9721c1b3.jpg)

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQQD.

5

![](images/84724edd9fc3216be735d5ad418948749e4b2168da9e2cd91f9af71c730d5525.jpg)

# UNCLASSIFIED

# 先决条件

![](images/0248b4ab69eeb37e266c182dfe373548266abf06928ce1183a02319fa70b107a.jpg)

- 在开始本实验之前，您应具备以下条件：

- 熟悉 WIZARD 和 AFSIM 脚本语言。  
- 建议参加过AFSIM分析课程或具备同等经验。  
- 能够使用 Microsoft® Visual Studio 2017® 或更新版本来编译应用程序，并熟悉其使用方法。  
- 熟悉使用 Microsoft Windows® Explorer。  
- 已完成模块“使用 CMAKE 构建 AFSIM”。  
- 熟悉使用 cmake-api。  
- 已安装 MATLAB MCR 9.1（可在 MathWorks 网站上免费获取）。

- AFSIM 在其基础框架中包含了一套强大的 mover 选项。  
• 通过使用 $\mathrm{C} + +$ 架构，开发人员可以扩展类以创建新的 movers 或新的 mover 行为。

![](images/e18d1e2051d0607b8bc1f1afb048780bcc8c73a7ff854a2979c83412e0fd0eae.jpg)

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQDD.

# UNCLASSIFIED

![](images/a8af83a60498d7bbdb597e6a47d6ab08e93f052a4d989c9e0d4205e5b71d610c.jpg)

# Movers如何运动

![](images/a567f444fc8da6721a13be3cc70bad8d41d3a0497ab8441604fc7f6b57cf291d.jpg)

• Mover 是一个平台组件，负责维护其附加平台的运动学状态（如位置、方向、速度、加速度等）。  
- 它由模拟调用，用于在模拟中实现平台的运动。  
- 集成一个新的 mover 非常简单，只需在派生类中实现“Update”方法即可：

- 当使用 WsfEventStepSimulation 时，Update 方法由事件调用。  
- 当使用 WsfFrameStepSimulation 时，Update 方法被直接调用。

![](images/3fc3225bae9fb8b2ad5505ec2d255c9034d3172a3ae2aa792642c8f5ddccebf2.jpg)  
DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

9

![](images/30a80bb4becbd6f18597a027142461fab60e256dfb7bd6fcd89d6872f1698a85.jpg)

# Mover 练习扩展了 WsfMover 类

![](images/96e3759b98c32e5315ff6d102495f6d5fc4bbaae6506e8edcd474ee7641e14c4.jpg)

- 您将向 AFSIM 添加一个新的 MATLABBallisticMover 类。

![](images/acf30c4251bce3e2bc66ceefbe022a7f3701908a074ad72d8040ecf0f13fa5c5.jpg)  
DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19.   
Other requests for this document shall be referred to AFRL/RQQD.

# - 一个简单的弹道导弹 mover:

- 多级设计  
垂直发射   
- 使用用户定义的俯仰间隔和动态压力约束，在助推阶段提供平滑的俯仰过渡。  
- 仅在助推阶段建模阻力  
- 假设侧滑角（ $\beta$ ）为常数。  
- 阻力系数不随马赫数变化。  
- 空气密度使用指数近似进行建模。

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQQD.

11

![](images/67ed1d30a46ca100feb6918a764adabfcd1d4760f8e6c4d4a2411d4fcaa710eb.jpg)

# Mover想定

![](images/d6963bf5ffc5879aaad5ffcb0f0c9717f40826a8c86021e91fb7bb0c25a12548.jpg)

- 输入文件声明了一种名为“ICBM”的平台类型，该平台使用MATLABBALLISTIC_MOVER。  
- MATLAB BALLISTIC_MOVER 是一个多级飞行器。  
- 平台“ballistic_missile-1”配备了一个MATLAB BALLISTIC_MOVermover，并具有指定的初始位置、航向和俯仰角。  
- “结束时间”被设置为3000个模拟秒。  
- 请注意，moverscenario.txt文件指定了moverscenario.aer文件，用于保存数据，以便通过Mystic回放场景并验证操作。

![](images/ac7535261cec546c02182b6c2f03f099572f2955623935b2bf27c27c88973afe.jpg)

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19.

Other requests for this document shall be referred to AFRL/RQQD.

# - 输入示例：

以下方法处理：

MATLABBallisticMover::ProcessInput

mover MATLAB BALLISTIC MOVER

update interval 1 sec

stage 1

fuel mass

total mass

thrust

burn time

end stage

stage

fuel mass

total mass

thrust

burn time

end stage

stage 3

fuel_mass

total_mass

thrust

burn time

end stage

drag coeff 0.4

effective area 2.986 meters^2

mass payload 900 kg

maxq 650 // lb/ft^2

pitch_interval 35 sec

vertical_time 10 sec

end mover

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19.

Other requests for this document shall be referred to AFRL/RQQD.

# UNCLASSIFIED

# 新的输入参数

![](images/0eb226667e79598ff139ee2fdf08115a893a04c26e0033d5b5e0c048b3adda23.jpg)

![](images/a69e59a02bf476bfa285d2a44bc0272b9cfda966963fea18abb81747417b87f1.jpg)

# - 输入示例：

以下方法处理

MATLABBallisticMover::Stage::ProcessInput -

mover MATLAB BALLISTIC MOVER

update interval 1 sec

stage 1

fuel mass 27941 kg

total_mass 31343 kg

thrust 1230600 Nt

burn time 76 sec

end stage

stage 2

fuel mass 8872.3 kg

total_mass 10233 kg

thrust 529290 Nt

burn time 59 sec

end stage

stage 3

fuel_mass 3265.9 kg

total_mass 4209.3 kg

thrust

burn time 49 sec

end stage

drag_coeff 0.4

effective area 2.986 meters^2

mass payload 900 kg

maxq 650 // lb/ft^2

pitch interval 35 sec

vertical_time 10 sec

end mover

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19.

Other requests for this document shall be referred to AFRL/RQQD.

- 将MATLAB®编译的 $\mathrm{C}++$ 共享库集成到mover项目中：

- 使用MATLAB® Compiler Runtime (MCR)，这是MATLAB®提供的一组独立共享库，用于在C++ mover项目中执行已编译的M文件。

- 安装 MATLAB® Compiler Runtime (MCR):

- 如果目标机器上没有安装 MATLAB® ，则需要在目标机器上安装 MCR。  
- MCR 只需安装一次即可。  
安装MCR后，必须重新启动计算机。  
- MCR是特定于MATLAB®版本的，因此在提供或接收MATLAB®编译的共享库时，请确保提供正确版本的MCR（MCRInstaller.exe）。  
- 在 Microsoft® Windows 系统下安装 MCR 相对简单。

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

# UNCLASSIFIED

![](images/159b6852a289bcb1c135fdb1f1aaa30e65ae883f4fcf2b9cb151450c7b80981c.jpg)

# 开始(2/4)

![](images/40015f5d6b18d7d4ac7d7daab50f835369b973057163979a842d5006d75f25ad.jpg)

1. 打开 CMake GUI。  
2. 勾选BUILD_WITH_mover exercis   
3. 点击“Configure”。

- （如果出现提示要求选择编译器，请进行相应操作）。

4. 确保 MCR_INCLUDE_LOCATION 和 MCRlibraries_LOCATION 的选项正确指向 <MCR 安装文件夹>。  
5. 点击“Generate”。

- 如果 Visual Studio 已经打开:

- 导航到它，并在提示时选择“Reload All”（全部重新加载）。

![](images/2b1b931653a8da9dff68159ec4074c327b89212486fb4f1f7def898a83533f6f.jpg)

- 或者，通过以下方式打开解决方案文件afsim.sln:

- 从labs\build 打开。  
- 从 CMake 中点击“Open Project”（打开项目）。

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

17

![](images/878bda65784f75167b0ef567ba08a1cac2c6eded59806ff746d9b00c77d8ff94.jpg)

# UNCLASSIFIED

# 开始 (4/4)

![](images/917bbe1793f9e542c986599e7940d1ce0adb4003461934b516870daaa72d7744.jpg)

- 项目中应包含以下文件:

- MoverPluginRegistration.cpp   
MATLABBallisticMover.hpp   
MATLABBallisticMover.cpp

![](images/b862143ecd76dfc58122b8bc7786ca83e7d328f50419ca8f00b0fd1e6c05f554.jpg)

请注意，有许多解决方案是可行的；我们提供了一个解决方案，以便在较短的时间内完成我们的训练练习。

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19.

Other requests for this document shall be referred to AFRL/RQQD.

- 本练习使用了以下类：

1. 类 MATLABBallisticMover : public WsfMover

创建了一种新的 mover 类型。  
- 维护了许多与MATLAB相关的变量。  
维护了许多与 mover 相关的变量。

2. 类 Stage

- 内嵌于MATLABBallisticMover类中。  
- 表示（可能是）多级飞行器中的一个阶段。  
- 维护了该阶段的燃料质量(FuelMass)、总质量(TotalMass)、推力(Thrust)和推力持续时间(ThrustDuration)。

3. 类 RegisterMATLAB_BallisticMover : public WsfApplicationExtension

- 该类作为应用扩展注册到标准应用程序中。  
- 重写了 ScenarioCreated 方法，该方法在场景由 mission/warlock 创建后，将 MATLAB BALLISTIC_MOVER 添加为一种新的 mover 类型。

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

19

![](images/a1adf77aa1fe85c4558a6afdb6fb0450822ad45b6d9b395db870000de3ff298d.jpg)

# Mover练习

![](images/a96341cea22c56641b27432d8262960bf0e966321d1c558ada1c50e39a003e8b.jpg)

·练习1

完成应用扩展的注册。  
- 初始化并终止 MATLAB 库。

·练习2

- 完成MATLABBallisticMover类中以下方法的实现：

- ProcessInput   
- Initialize   
- Update   
- UpdatePlatform

- 练习3（可选）

- 创建并部署 MATLAB 库文件。

注册应用扩展  
- 在场景创建时初始化 MATLAB 共享库。  
- 在AFSIM终止时终止MATLAB共享库。  
- 将一种新的 mover 类型（类型为 MATLABBallisticMover）添加到场景中。

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

21

![](images/7ec3fc36d2759007a6bf5809e45d8a6832c2c6a81170c48dd1727f81b562352d.jpg)

# AFSIM插件&扩展

![](images/3b3c3197b2258e3d87c460b9c0d236fc092beab7dbc094ebe048d582e3b1e0f4.jpg)

![](images/25743e59a657d277edc2572f2af474534c200b69213a22e8a37c7823f8efb22b.jpg)

在mission/warlock中使用的主应用程序

- 所有AFSIM扩展都必须继承自WsfExtension:

- 已经存在三个预定义的扩展类（可以继承自这些类）：

1. WsfScenarioExtension：需要提供新的场景命令的扩展（需要为这些命令实现新的ProcessInput）需要继承此类。  
2. WsfSimulationExtension：需要访问仿真的扩展需要继承此类。  
3. WsfApplicationExtension：需要创建新的脚本类型，或需要利用仿真扩展或场景扩展的扩展需要继承此类。

![](images/bcd858705025cfb4f166d3a352e431df542388510a2fd6d11bfccde456fe14ff.jpg)

- 所有 AFSIM 扩展都必须继承自 WsfExtension:

- 已经存在三个预定义的扩展类（可以继承自这些类）：

1. WsfScenarioExtension：需要提供新的场景命令的扩展（需要为这些命令实现新的ProcessInput）需要继承此类。  
2. WsfSimulationExtension：需要访问仿真的扩展需要继承此类。  
3. WsfApplicationExtension: 需要创建新的脚本类型，或需要利用仿真扩展或场景扩展的扩展需要继承此类。

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQQD.

23

![](images/fb2ba33a76165654fd57d355cf1a963d4eecc8b865e56ded587f9ab8a3d8377d.jpg)

# UNCLASSIFIED

# 扩展

![](images/e6314453cb9bf66773797895c7868bac710637a15681d4c03dd523abe4d49d83.jpg)

应用程序、场景和仿真都可以被“扩展”：

- 应用扩展由应用程序拥有。

- 表示可以添加到应用程序的可选功能。  
- 当需要新的脚本类型（如传感器、武器、组件、movers）时使用。  
- 这是在AFSIM中注册所有扩展的入口点。  
- 如果要创建场景扩展或仿真扩展，则需要一个应用扩展。

- 我们还需要应用扩展的情况包括：

创建新的脚本时。  
需要向场景注册类型时。  
- 需要新的插件，因为我们正在创建一种新类型。

- 在这里，我们需要通过应用扩展注册插件（请参阅文件MoverPluginRegistration.cpp）。

# - 回顾并理解插件的设置方式

- 查看 WsfPluginSetup，并注意调用 RegisterExtension 来注册 WsfApplicationExtension（即我们的 RegisterMATLAB_BallisticMover 类）。  
- 查看 WsfPluginVersion，并注意调用 UtPluginVersion。

- 这与武器练习中的代码相同。

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

25

![](images/a6abb163fc313c1bf4ccdfd5744222da69b9aba1e4bdf6063f64e1f56e79f00a.jpg)

# Mover练习1—检视1

# MoverPluginRegistration.cpp

![](images/2e3bfaf6a05bf7201326f00ae6b7887faccca547c1ec33b6ff4f43055e3cba49.jpg)

```cpp
extern "C"
{
MOVER_EXERCISE exporting void WsfPluginVersion(UtPluginVersion& aVersion)
{
aVersion = UtsPluginVersion(WSF Plugin_APIMajor_VERSION,
WSF Plugin_APIMinor_VERSION,
WSF Plugin_API_COMPILER_STRING);
}
MOVER_EXERCISE exporting void WsfPluginSetup(WsfApplication& aApplication)
{
aApplication.RegisterExtension("register_matlab_ballistic_mover",
ut::make_unique<RegisterMATLAB_BallisticMover>();}
} 
```

- 要扩展一个应用程序，您必须创建一个继承自 WsfApplicationExtension 的类

class myAppExtension: public WsfApplicationExtension { ... }

- 您需要重写以下成员函数:

- AddedToApplication: 用于接收扩展被添加到应用程序的通知。通常用于注册额外的脚本类和方法等。  
- ScenarioCreated：在场景构造函数结束时调用，用于接收来自应用程序的场景创建通知。  
- 如果需要，可以在此处注册场景扩展。  
- SimulationCreated: 从仿真的 Initialize 方法中调用，用于接收来自应用程序的仿真创建通知。如果需要，可以在此处注册仿真扩展。  
- ProcessCommandLine: 从 WsfApplication::ProcessCommandLine 方法中调用，用于检查当前参数并在必要时处理它  
- PrintGrammar: 打印出扩展所识别的扩展语法  
- ProcessCommandLineCommands: 由 WsfApplication 的 ProcessCommandLineCommands 调用，允许扩展处理/处理它需要识别的任何命令。

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQQD.

27

![](images/32b665de3f37f53d6ef66f7f2eb46d7ca5095bfd0ff208d57722b1fd3462da74.jpg)

# 应用程序扩展

![](images/ea0812ceca3eb44033980993c25bd58c71064181a18867ea46fd9d8788036e80.jpg)

- 我们将创建一个名为 RegisterMATLAB_BallisticMover 的应用扩展，它将注册一些新的脚本

class RegisterMATLAB_BallisticMover: public WsfApplicationExtension { ... }

此类将重写以下成员函数：

- ScenarioCreated：在场景构造函数结束时调用，用于接收来自应用程序的场景创建通知。如果需要，可以在此处注册场景扩展。

在文件MaverPluginRegistration.cpp中：

在类 RegisterMATLAB_BallisticMover 中:

1. 查看 ScenarioCreated 方法，并回顾以下内容的初始化和销毁：

MATLAB® Compiler Runtime (MCR) 实例的初始化和销毁。  
- MATLAB 生成的 libAFSIM_Mover 共享库 的初始化和销毁。

2. 查看析构函数，并回顾以下内容的销毁：

- MATLAB 生成的 libAFSIM_Mover 共享库 的销毁。  
MATLAB® Compiler Runtime (MCR) 实例的销毁。

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

29

![](images/cfec5ba57709d191fbce717a37be41f0f7cda600e4d151e066897cd6c1cb838b.jpg)

UNCLASSIFIED Mover练习1—检视2 MoverPluginRegistration.cpp

![](images/74a4c8410cd3103bb1d7eb554a118a25531cc8e26535692a2a0171068295445e.jpg)

```cpp
class RegisterMATLAB_BallisticMover : public WsfApplicationExtension   
{ public: RegisterMATLAB_BallisticMover() { } ~RegisterMATLAB_BallisticMover() noexcept override { // Clean up the Matlab Compiler Runtime. libAFSIM_MoverTerminate(); mclTerminateApplication(); } void ScenarioCreated(WsfScenario& aScenario) override { // To use a MATLAB shared library, you must initialize and terminate // the MATLAB Compiler Runtime instance correctly. if (!mclInitializeApplication(NULL, 0) || !libAFSIM_MoverInitialize()) { ut::log::error << "Could not initialize MATLAB libraries!"; exit(-1); } // Exercise 1 Task 1 } }; 
```

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

在 RegisterMATLAB_BallisticMover::ScenarioCreated 方法中：

1. 将 MATLABBallisticMover 类注册为一个应用扩展，名称为“MATLAB BALLISTIC_MOVER”。  
2. 使用 aScenario 调用 GetMoverTypes 方法。  
3. 使用上一步返回的 WsfMoverTypes 对象，调用 Add 方法，并传入以下内容：

名称（“MATLABBALLISTIC_MOVER”）。  
- 一个新的 unique_ptr，指向从场景变量 aScenario 构造的 MATLAB BallisticMover 对象。

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

31

![](images/5ae3cff29c718bd384edc91e5e2e8d2af85049e7d9d507ee03714e1acf73d54f.jpg)

# Mover练习1—任务1解决方案

# MoverPluginRegistration.cpp

![](images/3020e0a0f8f5c15dc094f62162235f22fe524414caa628e6b68f9da85fae7183.jpg)

```cpp
class RegisterMATLAB_BallisticMover : public WsfApplicationExtension   
{ public: RegisterMATLAB_BallisticMover() { } ~RegisterMATLAB_BallisticMover( ) noexcept override { // Clean up the Matlab Compiler Runtime. libAFSIM_MoverTerminate(); mclTerminateApplication(); } void ScenarioCreated(WsfScenario& aScenario) override { // To use a MATLAB shared library, you must initialize and terminate // the MATLAB Compiler Runtime instance correctly. if (!mclInitializeApplication(NULL, 0) || !libAFSIM_MoverInitialize()) { ut::log::error << "Could not initialize MATLAB libraries!"; exit(-1); } // Exercise 1 Task 1 aScenario.GetMoverTypes().Add("MATLAB_BALLISTIC_MOVER", ut::make_unique<matlabballisticMover>(aScenario)); } }; 
```

![](images/e0b7ba178eaf9ed6c5478a31ddc830bf4d62815a98883ca3d386eb49b3ceb296.jpg)

WsfStandardApplication 构造函数利用插件管理器来查找并加载所有插件（包括训练文件夹中的插件——这是因为 CMake 选项 WSF_ADD Extensions_PATH 的设置）。

1. 对于找到的每个插件，都会执行 WsfPluginSetup（注意：这会导致我们用于 mover 练习的插件的 WsfPluginSetup 函数被执行）。  
2. 这会导致我们用于 mover 练习的 RegisterMATLAB_BallisticMover 类（这是一个应用扩展）被创建并注册到应用程序中。  
3. RegisterExtension 随后调用 WsfApplicationExtension::AddedToApplication()。

注意：RegisterMATLAB_BallisticMover 并未重写 AddedToApplication，因此该通知没有任何效果。

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19.

Other requests for this document shall be referred to AFRL/RQQD.

33

![](images/090948e1f43ec0a55d9fe3aac4532a9631ae520baa3d947500bf4f65f49cd2a1.jpg)

# UNCLASSIFIED AFSIM插件&扩展

# AFSIM mission 启动顺序

![](images/832f8a9c8a949448720f509b15c5f01becd267cfe4ab1615f3f75370d11108a9.jpg)

![](images/6d8a29349ad6f34a14aef975504b0cbc551ed4fd33760a23e22567d50685ba3b.jpg)

任务随后会将所有必要的预定义扩展注册到应用程序中。

![](images/9cd27663a69e5283f30a0f73c101030539462fb357b037eaba9a2dc51803e0b0.jpg)

Mission随后创建场景并调用 WsfScenario 构造函数：WsfScenario scenario(app);

1. 该构造函数会调用 WsfApplication::ScenarioCreated() 方法。  
2. 这又会调用所有已注册的应用扩展的 ScenarioCreated() 方法（包括我们的 RegisterMATLAB_BallisticMover 扩展）。  
3. RegisterMATLAB_BallisticMover::ScenarioCreated()会创建并将MATLABBallisticMover类型添加到mover类型列表中，以便当场景文件中发现MATLAB_BALLISTIC_MOVER命令时，可以调用它们的ProcessInput()方法。

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

35

![](images/c24d5a0cdaa2d4b3f34585dd278ac1f03aa476b3ee89713ac977bcb2810e2554.jpg)

# UNCLASSIFIED AFSIM插件&扩展 AFSIM mission启动顺序

![](images/79b43372a5894b064bd003174c7d476ff92a96eee91e960585ce60307f3d07d5.jpg)

![](images/c3499a8dcf99e1d0a1a0d87450f0ad195978a9582bbbd21fc46b5f13aa958fa2.jpg)

任务调用app.WsfStandardApplication::ProcessInputFiles(),

该方法会调用 WsfScenario::LoadFromFile():

- 对于输入中的每个命令：

- 调用每个核心类的ProcessInput()方法。  
调用MATLABBallisticMover::ProcessInput()来处理MATLABBallisticMover命令。  
- 调用每个已注册的场景扩展的ProcessInput()方法——但由于没有为MATLABBallisticMover定义场景扩展，因此此操作没有效果。

注意：当在场景输入文件中遇到MATLABBallisticMover块命令时，会创建一个MATLABBallisticMover对象。

![](images/acb03f62fb655dc20e3a668a19f8110236c62950e92c245c21c495099d844bae.jpg)

任务调用app.WsfStandardApplication::ProcessInputFiles(),

该方法会调用 WsfScenario::LoadFromFile(),

然后调用 WsfScenario::CompleteLoad():

1. 调用每个场景扩展的 Complete() 方法。  
2. 然后调用每个场景扩展的 Complete2() 方法。

注意：我们的类中没有任何类继承自 WsfScenarioExtension，因此没有定义需要调用的 Complete 或 Complete2 方法

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

37

![](images/b3362ce4e31024821caf58a9ef9b2aa1ae4e6b1513f00b4a5755da5b72e7a27c.jpg)

# AFSIM插件&扩展

# AFSIM mission启动顺序

![](images/57ab919dac44c2e32c61d1ee8cead0886f59eaafa6caf4350075b3671cf67bb6.jpg)

![](images/d0d4b69b2c0e549f9bc59b30e2e3620b460f6ff8a84e7ed048f43d9934514e43.jpg)

Mission通过执行以下代码创建模拟：

```cpp
std::unique_ptr<WsfSimulation> simPtr = app.CreateSimulation(scenario, ...); 
```

- CreateSimulation 调用 WsfSimulation 对象的构造函数（以 scenario 作为参数）。

![](images/6b4ec941281051650d04e68db94d25e81ef30cbf447f1f5996725990408c64a1.jpg)

Mission通过执行以下代码初始化模拟：

app.InitializeSimulation(simPtr.get())

- InitializeSimulation 调用: aSimPtr->Initialize()

(where aSimPtr $\equiv$ simPtr.get())

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

39

![](images/309a85a40ed3b267dc8c26b1501cdd567de1b65cc2381f14418b3501af5e9e76.jpg)

# AFSIM插件&扩展

# AFSIM mission启动顺序

![](images/c68d5e77b3ee3404e55c69785d99c0a69f6c06c962ba76225dc27855908043a7.jpg)

![](images/96769b7aac3f4bce5077c8cbe0f3d017e51cd2655d4d9085bbbdc090765c83e9.jpg)

Mission通过执行以下代码初始化模拟：

app.InitializeSimulation(simPtr.get())

- InitializeSimulation 调用: aSimPtr->Initialize()   
- WsfSimulation::Initialize 调用: mScenario.SimulationCreated(*this)

(where mScenario $\equiv$ scenario and \*this $\equiv$ *simPtr.get()

![](images/f4e510e4c2eb1602d68cf1d552f1dc297d93cfaf6fae1215b1bc5019bf64f68c.jpg)

Mission通过执行以下代码初始化模拟：

app.InitializeSimulation(simPtr.get())

- InitializeSimulation 调用: aSimPtr->Initialize()   
- WsfSimulation::Initialize 调用: mScenario.SimulationCreated(*this)   
- SimulationCreated 调用: GetApplication().SimulationCreated(aSimulation)

(where GetApplication() ≡ app and aSimulation ≡ *simPtr.get())

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19.

Other requests for this document shall be referred to AFRL/RQQD.

41

![](images/dbec1a050777a96ebeabfc62bad4be9c8895a17daec0980675c57aa91254ae63.jpg)

# AFSIM插件&扩展

# AFSIM mission启动顺序

![](images/c086ab24cb2114e853a1022c5423caffab224da7abc140b48162084496d7705b.jpg)

![](images/0f8f8ed811ce6cf310db04c5dce5f3fb0ef01d773bb1a77821e1f053a87dbdab.jpg)

Mission通过执行以下代码初始化模拟：

app.InitializeSimulation(simPtr.get())

- InitializeSimulation 调用: aSimPtr->Initialize()   
- WsfSimulation::Initialize 调用：mScenario.SimulationCreated(*this)   
- SimulationCreated 调用: GetApplication().SimulationCreated(aSimulation)

- 对于每个应用扩展，调用 SimulationCreated(aSimulation)

(where aSimulation $\equiv^{*}\mathrm{simPtr.get()}$

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19.

Other requests for this document shall be referred to AFRL/RQQD.

![](images/d1b88871eb5dae98701bb38eb0a45dec9bebe63ab98b577aff5c77f4255a7460.jpg)

Mission 通过执行以下代码初始化模拟：

app.InitializeSimulation(simPtr.get())

中

- SimulationCreated 调用: GetApplication().SimulationCreated(aSimulation)

- 对于每个应用扩展，调用 SimulationCreated(aSimulation)  
- 它们调用 WsfApplicationExtension::SimulationCreated(aSimulation) (where aSimulation ≡ *simPtr.get())

注意：RegisterMATLAB_BallisticMover没有重写SimulationCreated，因此该调用没有任何效果

Other requests for this document shall be referred to AFRL/RQQD.

43

![](images/6d5caefd5948706b7c6154bcafbe3ee5e3a9057e263e92117f1fa0636a4a52c4.jpg)

# AFSIM插件&扩展

# AFSIM mission启动顺序

![](images/dd2a50e13582c225e30d9ab5d311b962b9db6a9d927b837196a06445cd794e3b.jpg)

![](images/82b5394cd6c55c1fdb795c79460bc02fae0158f728857156e7825209e83ae964.jpg)

Mission 通过执行以下代码初始化模拟：

app.InitializeSimulation(simPtr.get())

- InitializeSimulation 调用: aSimPtr->Initialize()

：

- 下一步, WsfSimulation::Initialize 调用:

WsfObserver::SimulationInitializing(this)

- 这会通知所有已注册的事件观察者，模拟即将被初始化

注意：我们没有创建任何模拟观察者，因此该通知没有任何效果

![](images/f63d7d305d8cbd4e58a53226ba67b89ba3d791672ec99db40c0e52e1c2cdb7ac.jpg)

Mission 通过执行以下代码初始化模拟:

app.InitializeSimulation(simPtr.get())

- InitializeSimulation 调用: aSimPtr->Initialize()

中

- 下一步, Initialize 在所有仿真扩展中调用: Initialize()

- 这没有任何效果，因为移动器练习没有模拟扩展

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19.

Other requests for this document shall be referred to AFRL/RQQD.

45

![](images/0798dde6b73b086a02d531991d5d6dab456fc810103bd566dc03a9fdc66f0c87.jpg)

# AFSIM插件&扩展

# AFSIM mission 启动顺序

![](images/02c0552e39e0dc3e1c5c924a6bf785b98d79f6ae050796f7c521d0b5ea051db3.jpg)

![](images/a96744472bee750c20c563c44bdb0964cf521bfd284bc6baf3f2a26c5b74efbc.jpg)

Mission 通过执行以下代码初始化模拟:

app.InitializeSimulation(simPtr.get())

- InitializeSimulation 调用: aSimPtr->Initialize()

：

- 接下来，WsfSimulation::Initialize 将所有可用的平台添加到模拟的平台列表中。  
- 最后，WsfSimulation::Initialize 将模拟状态设置为 cPENDING_START。

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19.

Other requests for this document shall be referred to AFRL/RQQD.

1. 完成 MATLABBallisticMover::ProcessInput 和  
MATLABBallisticMover::Stage::ProcessInput的实现。   
2. 理解MATLABBallisticMover::GetBoosterParams的实现。  
3. 完成 MATLAB BallisticMover::Initialize 的实现。  
4. 完成 MATLAB BallisticMover::Update 的实现。  
5. 完成 MATLAB BallisticMover::UpdatePlatform 的实现。

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19.

Other requests for this document shall be referred to AFRL/RQQD.

# UNCLASSIFIED

# Mover练习2 — 检视1

![](images/aa1a9fefa230b136421312cb2a360058a49a8583929b4d39ceb433e639832001.jpg)

![](images/43d7ec5a260d002e517202820aa5d430926e6454b001da3b6350842f8a22006b.jpg)

1. 检查文件 MATLABBallisticMover.hpp，并注意其继承自 WsfMover，以及为我们的解决方案假定的类属性和函数。  
2. 查看成员变量。

- mwarray 类是一个 MATLAB® 生成的类，用于将输入/输出参数传递给 MATLAB® 编译器生成的 C++ 接口。

// Input to MATLAB functions
mwArray mwInputLLA;
mwArray mwInputOrientation;
mwArray mwInputTime;
mwArray mwInputBoosterParams; $\vdots$ // Output from MATLAB functions
mwArray mwHitGroundTime;
mwArray mwState;

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19.

Other requests for this document shall be referred to AFRL/RQQD.