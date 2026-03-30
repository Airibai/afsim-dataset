# UNCLASSIFIED

# 行为树-答案1

![](images/f137cb9e97cd68ec2226fb1612b8a61c73a285ce235d90b8d0be7b5dfb53f62a.jpg)

![](images/3b3987658d6ebc9bd42d4964ebd5a77b5fd01a34ac07b9d36c49f52ac1273271.jpg)

DISTRIBUTIostritittUeeedtetractsestftcumtl AFRL/RQQD 15 15

![](images/32fa25262df8cf45b8d61572a4ff1d530a3cebd941865cf1aea123694db96eb4.jpg)

假设性（如果被访问）。

哪些节点会被执行？

DISTRIBUTIOstrtiuttUeetsdetractrstftumtld AFRL/RQQD 16

![](images/0ce7e1743aaa52c89be8ce112c905ca8e163a796f374e362c3c902f612a6f9f1.jpg)

# UNCLASSIFIED

# 行为树-答案2

![](images/3af2d03c10e6b0f3e2b3a566acdbb8903495c67a15a0a20c3a0f88c941804444.jpg)

![](images/a17c065a2deceb576e8b9d570fed21fb2fa2287ef9b4950ed2389026c0bc0478.jpg)

DISTRIBUTIostritittUeeedtetractsestftcumtl AERL/ROOD T17 17

![](images/ebb3e32fbbce9c8cd7b88c2719e40d842df61dbe3cc9119c4bd9fda62e4a3779.jpg)  
DISTRIBUTIOstrtithdtUoeentecisdtetractostereqestftmntal AFRL/RQQD 18

![](images/5acb93d205e1ab67dae766ff1face55a2464392c5d3a30cff2d9bedf7cd740d4.jpg)

# UNCLASSIFIED

# 简单的行为树

![](images/69a64b5d0f223ca9d28ef913b790b657f884134c49238cf326efabfc1863848c.jpg)

# 行为树示例：

![](images/c7cee177ef7513b3ac6fbbfdde905efcec2abcb7fd2776000771b743baf2e3fa.jpg)  
DISTRIBUTIostritittUeeedtetractsestftcumtl AFRL/RQQD 19 19

![](images/a5efdc7c09a155d41fbdf81ba56eba10dcefedcbe3c4143dac38744bf493e6eb.jpg)

DISTRIBUTIOstrtithdtUoeentecisdtetractostereqestftcmntal AFRL/RQQD 20

![](images/d7567fee6f0c319b1a503e9654b3c5faa1317572e4928cad78d3c1ca7fe4b7dc.jpg)

# UNCLASSIFIED

# 行为示例

![](images/b462af6262396f68ffc0f6f232630208963b5a3813b86c811963140b2c027c8a.jpg)

1 behavior default-flight   
2 script_variables bool mPrintRoute $\equiv$ false;   
4 endcript_variables   
5   
6   
7 script void PrintRoute()   
8 PLATFORM-route().Print();   
9 endScript   
10   
11   
12 precondition   
13 return true;   
14 end precondition   
15   
16   
17 execute   
18 PLATFORMReturnToRoute();   
19 if (mPrintRoute) { PrintRoute(); }   
22 end execute   
24   
25 endbehavior

Behaviors可以有局部变量和脚本

叶结点可以在其内部或外部:

simulatior platform processor $\gets$ behavior

行为在执行时应该做一些事情，

DISTRIBUTICstritiuttUetdttractsrstfotcumetld

AFRL/RQQD

# setup.txt

```txt
2 include_once platforms/common.txt   
3 include_once platforms/target.txt   
4 include_once platforms/ucav.txt   
5 //red commander   
6 include_once platforms/ship.txt   
10 // red SOJ   
11 include_once platforms/soj.txt   
12 // blue commander   
13 include_once platforms/flight_lead.txt   
14 //air platform (used by blue and red)   
15 include_once platforms/striker.txt   
16 include_once event_output.txt   
17 include once observers.txt   
18 
```

DISTRIBUIOstrtitdtUoenteidtractostetftmntal AFRL/RQQD 22 22

# UNCLASSIFIED

![](images/f7bacf13264a22b306acbaa3f20bbe4351254fb73deba070c9017ebb1ad43864.jpg)

# 额外的文件

![](images/76ac9589f5a20af0615a5ab568cd7207ea5f66cc6de64aa1c92c6c3d2cfe4f42.jpg)

# platforms/striker.txt

```batch
include_once weapons/aam/medium_range_radar_missile.txt include_once weapons/aam/simple_mrm_with_lc.txt include_once processors/quantum_agentaiai/behavior_agengageweapon_task_target.txt include_once processors/quantum_agentaiai/behavior_planned-route.txt include_once processors/quantum_agentaiai/behavior_pursue Weapon_task_target.txt 
```

DISTRIBUTIostritittUeeedtetractsestftcumtl AERL/ROOD 23 23

# platforms/striker.txt

![](images/88a13a5fa895a645f6e67105fda0bf8a46cb7765244dafcc4522b47976c4d738.jpg)

DISTRIBUTIOstrtithdtUoeentecisdtetractostereqestftcmntal AFRL/RQQD 24

![](images/7d7c25928518b3c749d1bde0186492d2c6621fb48db365dc0467c9767498efa8.jpg)

# UNCLASSIFIED

# 感知处理器

![](images/c45dd12e80b78c015a17fc302c898f6ff6fe38050d9d642d33b5a4eb3c533db9.jpg)

# platforms/striker.txt

![](images/063e573514b280edfcb73a65012fa9966caaad9a2257880d5f22abd4c77ddc5a.jpg)

DISTRIBUTIostritittUeeedtetractsestftcumtl AFRL/RQQD 25 25

# platforms/striker.txt

![](images/ca0b9e3d99f8d0bbd6d737423b8a121e8e0bf4772b2e9446aa556b6fbe6ae556.jpg)

DISTRIBUTIOstrtithdtUoeentecisdtetractostereqestftcmntal AFRL/RQQD 26

![](images/995c52d1f9f13994cae5bba9fb1c5f5302ce377371e1329f855e324d37c83f42.jpg)

# UNCLASSIFIED

# 行为:Planned Route

![](images/c2869b198c87b281cc4ca32d3d8e0d3f338da3758cd32237ae23daae44985ea2.jpg)

processors/quantum_agents/aiai/behavior_planned_route.txt   
processors/quantum_agentaiai/behavior_planned-route.txt   
28   
29 behavior planned route   
30 scriptDebugWrites off Named for behavior   
31   
32   
33 script_variables   
34 bool mDrawRoute = false;   
35 WsfDraw mDraw = WsfDraw();   
36 double cDEFAULT_SPEED = 450.0 \* MATH.MPS_PER_NMPH();   
37 double cDEFAULT_ACCEL $=$ 7.5 \* Earth.ACCEL_OF_GRAVITY( $)$ ; // 7.5 G (m/s^2)   
38   
39   
40 precondition   
41 writeIn_d("precondition planned-route");   
42 return true;   
43   
44   
45 execute   
46 writeIn_d(PLATFORM.Name()," executing planned-route, $T = "$ ,TIME NOW);   
47 // only command the platform to do something different if its not currently flying a route   
48 WsfMover aMover $=$ PLATFORM.Mover();   
49 if (aMover.IsValid()){   
50 if (aMover.IsExtrapolating()){   
51 WsfGeoPoint pt $=$ PLATFORM.Location();   
52 WsfRoute ro $=$ aMover.DefaultRoute().Copy(); // now we have a modifiable route   
53 if (!ro.IsValid())   
54 return;

DISTRIBUTIostritittUeeedtetractsestftcumtl AFRL/RQQD 27 27

# ：追踪目标行为参数示例

-debugging parameters

```txt
- bool mDrawSteering = false; 
```

-target point

WsfTrackId mTargetId;   
WsfGeoPoint mTargetPoint;   
double mTargetSpeed;

-flying parameters

double mMatchSpeedDistanceMin = 5 * 1852; # 5 miles   
double mMatchSpeedDistanceMax = 30 * 1852; # 30 miles   
double mWaitSpeed = 250 * MATH.MPS_PER_NMPH();   
double mInterceptSpeed $=$ 600.O * MATH.MPS PER NMPH() ;  
double mDefaultAccel   
etc.

-off-limit variables (not for user editing)

WsfDraw mDraw;   
double mLastTime;

DISTRIBUTIOstrtiuthdtoUoventAecisdtetractos,g9thereqstfortoumntald AFRL/RQQD 28 28

![](images/8db3b84e89fc28e023446389d9f6ee4ff0101eb1498de775784926ed4426bb7e.jpg)

# UNCLASSIFIED

# 行为：追踪武器任务目标

![](images/0a13fdb99cc10532ac9e89099d948989b2043c4f3de8f0abfb63355c60d8c072.jpg)

processors/quantum_agents/aiai/behavior_pursue_weapon_task_target.txt

```c
behavior pursueweapon_task_target   
scriptDebugWrites off   
script_variables   
WsfQuantumTaskerProcessor processor;   
//**********   
//** debugging parameters   
//**********   
bool mDrawSteering = false;   
string mZoneName = "";   
WsfZone mFezZone; 
```

DISTRIBUTIOistrtiuthdtUemeencedthotractsugthestfoumetsaet

AERL/ROOD

# ·交战目标行为参数示例

-platform/agent specific

```txt
- bool mCoopEngageOne = false;
- double mMaxFiringRollAngle = 10.0; 
```

-threat specific

```javascript
- ThreatTypeRequiredTrackQuality["bomber"] = 0.49;
- ThreatTypeSalvo["sam"] = 2; 
```

-weapon $^ +$ threat specific (complex types)

```txt
- double DefaultPercentRangeMax = 0.80; 
```

```txt
- double DefaultPercentRangeMin = 1.20; 
```

```javascript
WeaponThreatRmaxMap["baseweapon"].Set("fighter", 0.80); 
```

DISTRIBUTIOstrtiuthdtoUoventAecisdtetractos,g9thereqstfortoumntald AFRL/RQQD 30

![](images/26e28b4bb3243dd871cfe026e68472387a8975e922dc8eef6e139ddf653d8c45.jpg)

# UNCLASSIFIED

# 行为：交战武器任务目标

![](images/17c8d4e699d003c2a2905196e65f58f181e83b36610021ce8e2de92177362833.jpg)

processors/quantum_agents/aiai/behavior_engage_weapon_task_target.txt

include_once ../common/weapon.defs.txt   
behavior engageweapon_task_target   
scriptDebugWrites off   
script_variables   
//**********   
//** platform / agent specific shooting parameters \*\*/   
//**********   
//**   
bool mCoopEngageOne $=$ false;   
#bool mCoopEngageOneFlightOnly $=$ false;   
double mDegradedFiringAngle $= 55.0$ // negative if not valid   
double mDegradedPercentRange $= 0.50$ // range constraint if past degraded firing angle   
// specify orientation limits for shooting   
double mMaxFiringRollAngle $= 10.0$ // dont shoot if rolled more/less than this   
double mMaxFiringPitchAngle $= 15.0$ // dont shoot if pitched more than this   
double mMinFiringPitchAngle $= -10.0$ // dont shoot if pitched less than this

DISTRIBUTIOistrtiutdtUemeencedthotractsugthestfoumetsaet AFRL/RQQD 1 31

·一个武器平台由"launched_platform_type"创建。

·它会在当前状态下被赋予目标轨迹。  
·武器平台被添加到模拟中。  
·它可以通过以下方式更新自己的目标轨迹：

·使用自身的传感器（如果有的话）。  
·接收来自外部供应商的轨迹消息（上行链路）。  
·或者使用WSF_PERFECT_TRACKER。

·如果在武器发射后目标轨迹未更新：

·武器将根据原始轨迹信息，继续向前推断目标的位置。

DISTRIBUTIOstrtiuthdtUontecisdtetractosg9thereqstfortmntal AFRL/RQQD 32

![](images/c48b926125493f02a10723e732bf0ccce0daa13827d69c15ef3e70232c31c3df.jpg)

# UNCLASSIFIED

# 发射计算

![](images/b353884ebeb09160e389d635a309d3609fc283add0138c0243c6a5156c642b10.jpg)

·发射决策的理想使用场景：

·武器已经配备了发射计算机，例如：

·WSF_AIR_TO_AIR_LAUNCH_COMPUTER（空对空发射计算机）  
·WSF_ATG_LAUNCH_COMPUTER（空对地发射计算机）  
·等等.

·发射计算机使用预处理的发射表（LaunchTables）或发射允许区域（LARs）。

·这些表格由已发布的weapon_tools.exe生成。

DISTRIBUTIOstritiuttUetisdtetractsrstftumtld AERL/ROOD 33 33

创建weaponData结构体：

将包含有关武器的信息。

将武器名称映射到weaponData结构体：

通过映射关系快速访问武器数据。

使用用户定义的数据通知行为脚本：

行为脚本可以利用这些用户定义的数据来执行相关逻辑。

低保真度，但用户响应速度快：

这种方法牺牲了一些精确性，但能够快速满足用户需求。

不是必需的，但在AFSIM演示中使用：

这种方法并非强制要求，但在AFSIM的演示中被采用以展示功能。

processors/quantum_agents/common/weapon_defs.txt

1 script struct WeaponData   
2 script variables   
3 string type $= ^{**}$ .   
4 double rangeMin $= 0$ . //1852; //1 nm (meters)   
5 double rangeMax $= 0$ . //18520; //10 nm (meters)   
6 bool onlyUseInRange $= \mathrm{true}$ .   
7 double averageSpeed $= 0$ . //331.46; //-mach 1 (meters/seconds)   
8 double maxTimeFlight $= 0$ . //55.87; //should -equal~rangeMax / averageSpeed   
9 int numActiveMax $= 0$ . //1;   
10 bool domainAir $= \mathrm{false}$ . //true;   
11 bool domainLand $= \mathrm{false}$ .   
12 double maxFiringAngle $= 0$ 13 end script variables   
14 end script structure   
15   
16   
17 script variables   
18 Map<string, struct> gWeaponDefs = Map<string, struct>();   
19   
20 gWeaponDefs["MEDIUM_RANGE_MISSILE"] = struct.New("WeaponData");   
21 gWeaponDefs["MEDIUM_RANGE_MISSILE"]->type = "MEDIUM_RANGE_MISSILE";   
22 gWeaponDefs["MEDIUM_RANGE_MISSILE"]->rangeMin = 50; // (meters)   
23 gWeaponDefs["MEDIUM_RANGE_MISSILE"]->averageSpeed = 111128; // $\sim 60$ nm (meters)   
24 gWeaponDefs["MEDIUM_RANGE_MISSILE"]->maxTimeFlight = 67.05; //for 60 nm range (seconds)   
25 gWeaponDefs["MEDIUM_RANGE_MISSILE"]->numActiveMax = 2;   
26 gWeaponDefs["MEDIUM_RANGE_MISSILE"]->domainAir = true;   
27 gWeaponDefs["MEDIUM_RANGE_MISSILE"]->domainland = false;   
28 gWeaponDefs["MEDIUM_RANGE_MISSILE"]->maxFiringAngle = 45.0;   
29   
31 gWeaponDefs["MEDIUM_RANGE_RADIAR_MISSILE"] = struct.New("WeaponData");   
32 gWeaponDefs["MEDIUM_RANGE_RADIAR_MISSILE"]->type = "MEDIUM_RANGE_RADIAR_MISSILE";   
33 gWeaponDefs["MEDIUM_RANGE_RADIAR_MISSILE"]->rangeMin = 50; // (meters)   
34 gWeaponDefs["MEDIUM_RANGE_RADIAR_MISSILE"]->rangeMax = 111128; // $\sim 60$ nm (meters)   
35 gWeaponDefs["MEDIUM_RANGE_RADIAR_MISSILE"]->averageSpeed = 1657.283; //mach 5 (m/s)   
36 gWeaponDefs["MEDIUM_RANGE_RADIAR_MISSILE"]->maxTimeFlight = 67.05; //for 60 nm range (seconds)   
37 gWeaponDefs["MEDIUM_RANGE_RADIAR_MISSILE"]->numActiveMax = 2;   
38 gWeaponDefs["MEDIUM_RANGE_RADIAR_MISSILE"]->domainAir = true;   
39 gWeaponDefs["MEDIUM_RANGE_RADIAR_MISSILE"]->domainLand = false;   
40 gWeaponDefs["MEDIUM_RANGE_RADIAR_MISSILE"]->maxFiringAngle = 45.0;   
41   
end script variables

DISTRIBUTIOstrtithdtUoeentecisdtetractostereqestftcmntal AFRL/RQQD 34

![](images/c82c63a408414070464a3574cf7a75e74f435c7fe37c0c8ff73b416590ada9a1.jpg)

# UNCLASSIFIED

# 同样包含脚本

![](images/4a09b003dd268a3d89f8bb2444a14fb70f67cbb212650cb1b9faf73c359a236c.jpg)

```txt
// returns a 'WeaponData' struct  
45 script struct GetWeaponData(string aType)  
46 if (gWeaponDefs.Exists(aType))  
47 {  
48 return gWeaponDefs.Get(aType);  
49 }  
50 else  
51 {  
52 return struct.New("WeaponData");  
53 }  
54 end_script  
55 include_once processors/quantum企业提供/common/commonplatformScript.txt  
56 script_new();  
57 script_new();  
58 script_new();  
59 end.script  
60 script bool WeaponCapableAvailableAgainstThreat(WsfWeapon weapon, WsfTrack track)  
61 writeIn_d(" checking weapon", weapon.Name(), "valid=", weapon.IsValid());  
62 if (weapon.IsNull() || !weapon.IsValid() || track.IsNull() || !track.IsValid())  
63 {  
64 writeIn_d("weapon or track is not valid!");  
65 return false; 
```

DISTRIBUTIOstrittdvetAgecdtheotractsgOthreqstsfortumtal AERL/ROOD 35 35

·weapon_def.txt文件被包含两次：

![](images/a3ce170c0ef037c008112b47971d4954802b66a8300f911417b009133d2eda84.jpg)

![](images/2515233f25d286f52e66b18e4618882d0a6e739415d16109baa3ae0cc3325ce6.jpg)

·为什么？

－行为和处理器都需要数据和脚本。

·include_once 会确保它只被引用一次。

DISTRIBUIOstrtitdtUenteidtractostetftmntal AFRL/RQQD 36

![](images/05f8a49422767a8cac57b215198671bf54d0c7fb104140e5b1845101d11917af.jpg)

# UNCLASSIFIED

# 飞行队长的处理器

![](images/af41291b71070b0b6718ff633db55fcc6afb076b21ceeed48be614494df59e2e.jpg)

platforms/flight_lead.txt   
```txt
include_once processors/quantum_agenta/aif1/f1_quantum_tasker_verysimple.txt platform_typeFLIGHT_LEADWSFPLATFORM #sideblue/red 
```

```txt
max-threat_load 10   
end Processor   
processor task_mgr FL_QUANTUM_TASKER #scriptDebugWrites on #show_task/messages end处理器   
end platform_type 
```

DISTRIBUTIOistrtiutdtUemeencedthotractsugthestfoumetsaet AFRL/RQQD 37

processors/quantum_agents/aifl/fl_quantum_tasker_very_simple.txt

```txt
3 processor FL_QUANTUM_TASKER WSF_QUANTUM_TASKERPROCESSOR 
```

```txt
5 script_variables 
```

```txt
59 end.script   
60   
61 #show_task/messages   
62 #script debugWrites off   
63 update_interval 10.0 sec   
64 asset Representation platform   
65 reallocation_strategy dynamic   
66 generator custom FlightLeadTaskGeneration   
67 evaluator custom FlightLeadEvaluation   
68 allocator optimal_profit type WEAPON   
69 #Allocatorextra_tasks optimal_profit   
70 #Allocatorextra_assets optimal_profit   
71   
72 end Processor 
```

DISTRIBUIOstrtitdtUenteidtractostetftmntal AFRL/RQQD 38 38

# UNCLASSIFIED

# 飞行队长的任务产生器

![](images/792517a3f9d829eaa9cd2d5e832da434d5adaa018329d22fa3e82066b790aad3.jpg)

processors/quantum_agents/aifl/fl_quantum_tasker_very_simple.txt   
```txt
script Array<WsfQuantumTask> FlightLeadTaskGeneration (Array<WsfLocalTrack> TRACKS, Array<WsfAssetPerception> ASSETS)  
Array<WsfQuantumTask> tasks = Array<WsfQuantumTask>();  
//check if we are creating tasks or if we have a commander for that  
if (mSelfCreateTasks == true)  
{  
//if its us, then create weapon tasks for enemy tracks  
for (int i=0; i<TRACKS.Size(); i=i+1)  
{  
WsfLocalTrack lt = TRACKS.Get(i);  
if (lt.IsValid() && (!lt.SideValid() || lt.Side != PLATFORM.Side()))  
{  
if (mKnownTargetTypes.Size() <= 0 || mKnownTargetTypes.Exists(lt.TargetType()))  
{  
WsfQuantumTask task = WsfQuantumTask.Construct(1.0, "WEAPON", lt);  
task.SetTaskType("WEAPON");  
tasks.PushBack(task);  
writeIn_d("weapon task generated for: ", lt.TargetName(), "", updated time: ", lt.UpdateTime());  
}  
}  
}  
return tasks;  
end_script 
```

DISTRIBUTIostritittUeeedtetractsestftcumtl AERL/ROOD 39 39

processors/quantum_agents/aifl/fl_quantum_tasker_very_simple.txt   
DISTRIBUTIOstrtithdtUoeentecisdtetractostereqestftcmntal AFRL/RQQD 40   
```txt
script double FlightLeadEvaluation ( WsfQuantumTask TASK, WsfAssetPerception ASSET)  
#TODO - include missile capability in evaluation  
# for now: just base value on range & whether or not asset as domain capable weapon  
WsfTrack track = PLATFORM MasterTrackList().FindTrack(TASK TrackId());  
writeln_d(PLATFORM.Name(), "evaluating task type", TASK.TaskType());  
if (TASK.TaskType() == "WEapon" && track.IsValid())  
{  
    writeln_d("evaluating weapon task: ", track.TargetName(), "", updated time: ", track.UpdateTime()));  
#TODO - select one of the systems?  
for (int i=0; i<ASSET_SystemCount(); i+=1)  
{  
    if (ASSET_SystemKind(i) == "weapon" && ASSET_SystemQuantityRemaining(i) >= 1)  
{  
        double value = 1.0 / track.SlantRangeTo(ASSET.Location());  
    }  
    struct weaponData = GetWeaponData(ASSET_SystemType(i));  
    if (weaponData->type == ASSET_SystemType(i))  
{  
        if ((weaponData->domainAir && track.AirDomain())) || (weaponData->domainLand && track.LandDomain()))  
{  
            return value;  
        }  
    }  
else  
{ 
```

![](images/bcf62b0f4b6e4e1b0d20b504e944cc3e6fc79b740a8881efebb7699c40104cdb.jpg)

# UNCLASSIFIED

# 新的想定文件

![](images/0c2ea6f6d4a934ca5e996b8642e8576227b087c2c1e309d71078480d32d72067.jpg)

run_course.txt   
```txt
4 // setup file containing type definitions  
5 include_once setup.txt  
6  
7 // include the scenario files  
8 include_once scenarios/targets.txt  
9 include_once scenarios/red_air_strike.txt  
10 include_once scenarios/small-blue_iads.txt  
11 include_once scenarios/blue_air_cap.txt  
12 include_once scenarios/red_air_support.txt  
13 
```

DISTRIBUTIostrittdveetecedthtractsgtheqstfotumntal AFRL/RQQD 41 41

RUN IT!!!

现在我们可以开火了

DISTRIBUTIOstrtiuttUeetsdetractrstftumtld AFRL/RQQD 42

![](images/237d0254d70fb8456924a6fec89342bcfc9c88acb1b1445154804090f3da42b7.jpg)

# UNCLASSIFIED

开火！

![](images/ce5a93b81fdcdb9754be5f8145cb039cd246fea87f3e5e06157f88d535f0cb16.jpg)

![](images/f443b285ed4ff32a7f9904584ba0d8ff2752c3c94ebef48af5201454d3c1ce7a.jpg)

DISTRIBUIOstrtitdtUteisdtetractsteesftmntal AFRL/RQQD 43 43

创建两个新的行为节点：

“fail"：始终失败的节点。   
“pass"：始终成功的节点。  
在precondition（前置条件）和execute（执行）块中添加writeln或注释，以显示哪些内容会执行，哪些不会执行。

在攻击者行为树中添加额外的节点：

使用一个sequence（顺序）节点，包含几个pass 和 fail子节点，顺序随意。  
使用一个selector（选择器）节点，包含几个pass 和fail子节点，顺序随意。  
使用一个parallel（并行）节点，包含几个pass 和fail子节点，顺序随意。  
将其中一个中间节点嵌套为另一个节点的第一个子节点。

提示：

顶层节点是一个隐式的并行节点。

DISTRIBUTIOstrtithodtoU.oventAcdotrsugOtrststisumetsld AFRL/RQQD 44

![](images/3912e18768ec2ddc33eeb3720c92d6a403413c47157ee23da208448a02db0c5b.jpg)

# UNCLASSIFIED

# 学习目标

![](images/3990a0f2f5642bcf2bb5211479ca8a36b3dccac6e3a2c31f12727465e56a2441.jpg)

·包括：

－描述AFSIM中的行为树  
－构建行为节点  
－修改行为树

![](images/c53967332525be5fc23b7467f5a3f87f3f2df964fb2df526ab699fcc9837a209.jpg)

DISTRIBUTIOstrittdvetAgecdtheotractsgOthreqstsfortumtal AFRL/ROOD 45 45

![](images/3daabc5d4972511bb3265b2596e35c2c87afeae36e2df61f6a85473984d8faed.jpg)

DISTRIBUIOstrtitdtUenteidtractostetftmntal AFRL/RQQD

# 6.1.10.4.寻路 24_AFSIM_BAM_Trng_RouteFinder

# 6.1.10.4.1. 本节想定解析

本节想定资源在以下目录下：

afsim2.9_src\training\user\10_Other_Topics\bam\scenarios\floridistan\24_floridistan_route_finder\run_course.txt，在 10_Other_Topics\bam\scenarios\other_examples\route_finder_examples 下也有一些。

行为与智能体建模培训的每一节都是在上一节的基础上的，而且想定较为复杂，因此要先了解上一节的内容。本节是在上一节的基础上让蓝方的战斗机避开了蓝方的地空导弹的区域。其结果如下：

![](images/0ce4cd46eb595a1bebb323ebae768d76be0e00de3c4ce855e568961d16e5065e.jpg)

其中灰色的部分是画划的要避开的区截至。可以看到蓝方的战机 cap_south_2 避开了该区域。

# 6.1.10.4.2. 本节 PPT 资料

本文为 afsim2.9_src\training\user\10_Other_Topics\bam\slides\24_AFSIM_BAM_Trng_RouteFinder.pptx 的翻译。

![](images/987f3295e59aad1a405a2656944adb7f06ea870c1f39170953b8e3dfdb63f97a.jpg)

Integrity ★Service ★ Excellence

# AFSIM用户培训

# 24-寻路

AFRL/RQQD美国空军研究实验室

DISTRIBUTIostrtittUeeeedtractstftcumtld AFRL/RQQD 1

![](images/c06a529c3d70c2796cc25b62a89a8fe225103b3f4a6be7a7ffb45e51ecc518ec.jpg)

# UNCLASSIFIED

# 寻路

![](images/80d55c4c6910e209ab119a450ef5732b915637b6b5013dab397b287616e31d97.jpg)

规划静态路由  
动态使用以应对移动目标/避让障碍

![](images/00bbf9e92d3531c7b9b7fc6983e33dd00be9b47efec3cb218ac3b8ee56656d1e.jpg)

DISTRIBUTIostritittUeeedtetractsestftcumtl AFRL/RQQD 2 °2

·理论

－快速且简单的路径查找器

·应用

－全局定义一个避让区域

·任何需要的对象都可以避开该区域

－在攻击者（striker）上切换追击行为

·使用一个利用WsfRouteFinder的行为

![](images/391051d06b05da8aa31c2bc8e48cef836f207a75c574efaa6f0cc969d21dd648.jpg)

DISTRIBUTIOstrtiuttUeetesdtetractosrstfotcumtsld AFRL/RQQD 3

![](images/c7d29d6f0f4e3cbd30132471df8c9e898725dfb538ac96d1418bc152aad6edad.jpg)

# UNCLASSIFIED

# 应用

![](images/e9b7dd53a2a3b2a2e29e6e20ac90faa12cd01fc87566760271a911b9602f75fb.jpg)

·用例

－在任何需要避开某个区域时使用，例如：

·地对空导弹（SAM）阵地  
·敌方战斗空中巡逻（CAP)  
·敌方领土

－ (可以用一个大圆或多个重叠的圆来抽象表示这些区域)  
－支持绕过复杂的避让区域组合进行路径规划

·底层实现

－轻量级、快速计算  
－利用所有避让区域都是圆形这一特点  
－在所有避让区域、代理（agent）和目标位置之间生成图  
-使用深度优先搜索（Depth-First-Search,DFS）算法从图中选择最佳路径

# ·WsfRouteFinder

－避开静态区域和动态区域(附加到平台上的区域)  
－简单的接口  
－可以用于一次性操作的简单平台 (演示1)

·例如：一次性规划路径

－可以与代理和任务一起使用（演示2）

·动态地，根据需要重新规划路

－文档：WsfRouteFinder

![](images/e9434bfa2840e8fbe8aadaa6bbc34e9beea2ea7db0aa04e48ac4c5ef87d2cba3.jpg)

DISTRIBUIONCistititodtUvetAencdthotractorsg9tereqstsfotscumtld AFRL/RQQD 5

![](images/83e1fca24a2102e83dfb0158db685be7506b0e8949dfabce261e68959a173b01.jpg)

# UNCLASSIFIED

# 不可到达的路径处理选项

![](images/8dfed70cd4e58617308717ce72a850c71f847f4517ad6c7de19db55aa0f4f5a2.jpg)

![](images/154d96e9540822e1a135ae1996d8aefe2ce46135db2fececee0bdaebecae2865.jpg)  
SHIFT

![](images/999f4a042689524575b391e2ef3721b81cd3cc9fe5d9251d12d6f524da9e610b.jpg)  
SHRINK

![](images/d5796aa3e8424d0a90c5f931645e1bb61e76f5a1821d9e9a6f15c332dc1a0e6a.jpg)  
IGNORE

DISTRIBUTIOstrittdvetAgecdtheotractsgOthreqstsfortumtal AFRL/ROOD 6 6

![](images/5875c756b4b2553ad07cb367ea8191d5c6b3991c01ec7a8bf5fb8145d3df4c57.jpg)  
SHIFT多次尝试后停止

![](images/d403eb1921ca62a8904c89796d80f1ca5d14cbc4b7601f338afd4510300bf6f8.jpg)  
经常情况下没撤

DISTRIBUIONCistititodtUvetAencdthotractorsg9tereqstsfotscumtld AFRL/RQQD 7 7

# UNCLASSIFIED

![](images/ae5e21253d68e69907bf82bc02c53ede3677160da3a6cf596f274a1a37121344.jpg)

# 路径查找器生成一个移动者路径

![](images/58581ec6e599e390f1f49043390b078450de04bd1e3d5bfae0ef001c34786845.jpg)

·WsfRoute 是在径向加速度限制下构建的（用于长转弯）。  
WsfRoute RouteAvoidances( $) = = \{ \textsf { G } , \textsf { H } , \textsf { F } \}$

－这不是用于飞行的路径，仅用于避让点的计算。  
－最终的"避让点"是目标  
－避让点的数量等于路

· WsfRoute Route() ={ A,B

－这是一个真实的 AFS  
－路径点的数量是偶数

![](images/9f938c5ca8795217b678c1926d6e6b395925f6bed78ca48b8f70a5a8cd58440a.jpg)

DISTRIBUTIOstrtiuthdtoU.oventAdteotratsugOtrestftsumetsld AFRL/ROOD 8 8

·如果我的移动者不擅长径向加速度怎么办？  
·用户可以使用WsfRouteFinder.SetMaxArcLength(米)设置最大弧长。  
·WsfRoute 的 RouteAvoidances() $= = \{$ 现在更难使用了，所以不要用它}  
.WsfRoute Route()={A,B,C,D,E,F,G,H,I,J,K,L}

－在长转弯处根据指定的最大弧长插入航路点。  
－路径的大小现在也取决于长弧的数量。

![](images/a83b37c23466288bb78f6d8ce19e71a55600348f40ffac747a4a224abeea1e61.jpg)  
DISTRIBUTIostrtittUeeeedtractstftcumtld AFRL/RQQD 9

![](images/a3768b0e6e93ccbdd68cb315e2e698f7d31ac8d0d047c7b89fc05f5f01a450ae.jpg)

# UNCLASSIFIED

# 寻路示例#1-静态

![](images/9afd64f0f8a2d8799e1bd38ae2f5d367ddf542b3273212ce5d5ff518d65ad09f.jpg)

![](images/232503b27499d96f923b77dbcbc687e99e062d3b6a95ad9f971a7d66f3fbe286.jpg)  
DISTRIBUTIOstrittdvetAgecdtheotractsgOthreqstsfortumtal AERL/ROOD 10

scenario-route_finder_1.txt\*   
1 define_path_variable CASE scenario-route_finder_1   
2 log_file output/\\((CASE).log   
3   
4   
5   
6 file_path .   
7 file_path ./config   
8   
9 include_once dis_record.txt   
10 include_once event_output.txt   
11   
12 event_pipe   
13 file output/\\)(CASE).aer   
14 end_event_pipe   
15

DISTRIBUTIOstrtithedtUoventdotracuOtesttcumetsld AFRL/RQQD 11 11

![](images/e502380415672f77c8a5ed0ae9a726071bf61153c41301c9ec12f238160910d7.jpg)

# UNCLASSIFIED

# 定义避让区域

![](images/6c6ec76ca9cc4a4c47f8166b8f32c79cc6f98fe97941679d35da60c3f87e4c9f.jpg)

scenario_route_finder_1.txt   
49 script_variables WsfRouteFinder finder $=$ WsfRouteFinder();   
51   
52   
53   
54 on initialize2 finder.Set ImpossibleRouteResponse("SHRINK"); #finder.Set ImpossibleRouteResponse("SHIFT"); #finder.Set ImpossibleRouteResponse("IGNORE");   
56   
57   
58   
59 finder.MaxArcLength(4000); // a little over 2 nm (in meters) WsfGeoPoint src $=$ PLATFORM.Location(); WsfGeoPoint tgt $=$ WsfSimulation.FindPlatform("target").Location();   
60   
61   
62   
63 // three eastern avoidances finder.Avoid(WsfGeoPoint.Construct(0.91667,3.16667,0),1852\*20);#1 finder.Avoid(WsfGeoPoint.Construct(0.46222,2.87111,0),1852\*20);#2 finder.Avoid(WsfGeoPoint.Construct(-0.06667,2.88222,0),1852\*20);#3   
64   
65   
66   
67   
68 // two western avoidances finder.Avoid(WsfGeoPoint.Construct(0.77000,1.95833,0),1852\*10);#4   
70 finder.Avoid(WsfGeoPoint.Construct(-0.13500,1.91500,0),1852\*10);#5   
72   
73 WsfRoute path $=$ finder-route(TIME NOW,src,tgt,250);//250 met/sec $\sim 500$ knots

DISTRIBUIOstrtitdtUteisdtetractsteesftmntal AFRL/RQQD 12 12

![](images/7608843f65bea4025d6ed5c794da7417903fb30ebf8abbf202e72792f9a55e1c.jpg)

DISTRIBUTIOstrtiuttUeetsdetractrstftumtld AFRL/RQQD 13

![](images/9a8ac149bf7806ac0e134c4f46cf8250d8e2c71c45d0a16064433bf1d76a5c64.jpg)

# UNCLASSIFIED

# 选择路径

![](images/a518f4717814ec5f5c34a5dc6a91ba12198124d52fb6ffdcf70df9512bda01e3.jpg)

![](images/00d2de7045b7516a5dd446521f137fa3afc059f98f90081359984ea252f8c1ee.jpg)

DISTRIBUTIostritittUeeedtetractsestftcumtl AFRL/RQQD 14 14

·更改避让区域

－强制飞机向北飞行

·创建一条"无法完成"的路径，观察系统如何解决它

－尝试不同的解决方案

DISTRIBUTIOstrtiuthdtUontecisdtetractosg9thereqstfortmntal AFRL/RQQD 15

![](images/ed03953155a02215d5b2acf4c9cccba8b65d0ca164e66d95ce15eaa61b8310d4.jpg)

# UNCLASSIFIED

# 路径查找器示例#2-轨道

![](images/0d007204f9ccd2ecf1da43d637ca2a9a78b1fd288393ec547da0a45337b5fc08.jpg)

![](images/11f35119cb5a8827ed90fc9304e65903d2dac0a659a3ebe767dc888713a53f33.jpg)

DISTRIBUTIostritittUeeedtetractsestftcumtl AFRL/RQQD 16 16

![](images/ce8942e1243faeedaf2ca8ea9b9b0562cfd0a461ac2ab126a2df68932e489807.jpg)

DISTRIBUTIOstrtithdtUoeentecisdtetractostereqestftcmntal AFRL/RQQD 17

![](images/ac965a06f5d1792819eed4cf91d926b528e291057a7a018a6ed325e0ea80dc96.jpg)

# UNCLASSIFIED

# 动态更新避让路径

![](images/0e33975b6c07263870b2242db42164c419b1bfcabfb8612be2fd137afe5a077c.jpg)

scenario_route_finder_orbit.txt   
```txt
update_interval 1 sec   
execute at_interval_of 10 sec   
finder.MaxArcLength(4000); // a little over 2 nm (in meters)   
WsfGeoPoint src = PLATFORM.Location();   
WsfPlatform tgt = WsfSimulation.FindPlatform("target");   
WsfGeoPoint tempLoc = tgt.Location();   
double locDir = PLATFORM,TrueBearingTo(tgt)-1.0;   
tempLoc.Extrapolate(locDir, 20*MATH.M_PER_NM());   
finder.ClearAvoidances();   
finder.Avoid(tgt.Location(), 1852*20);   
WsfRoute path = finder-route(TIME NOW, src, tempLoc, 250); // 250 met/sec ~500 knots   
writeln("path: ");   
for(int i=0; i<path.Size(); i=i+1) { WsfWaypoint pt = pathWAYpoint(i); writeln(pt.Location().ToString()); }   
writeln_d(PLATFORM.Name(), "given path, size:", path.Size());   
PLATFORM.SetRoute(path);   
finder.DrawAvoidances(1, Vec3.Construct(0.4, 0.4, 0.4));   
DrawRoute(path);   
end_execute   
endplatform 
```

DISTRIBUTIostritittUeeedtetractsestftcumtl AERL/ROOD 18 18

·理论

－快速且简单的路径查找器

·应用

－全局定义一个避让区域

·任何需要的人都可以避开它

－在攻击者上切换追踪行为

·使用利用WsfRouteFinder 的行为

![](images/21a112827b76774a053dea6c62ed1ea69d586cff518465f83b33bacc722f93ba.jpg)

DISTRIBUTIOstrtiuttUeetsdetractrstftumtld AFRL/RQQD 19 19

![](images/9ccb9f2b3638debf69ba5076d97377b75e464c91315b5422cd93a2e5acfd7955.jpg)

# UNCLASSIFIED

# 全局避让点已定义

![](images/fc3c41cf705a6e2f3500ead9b3a2696560046fe3d054dee5565e2b5a5ab0b08b.jpg)

setup.txt   
```c
7 // red commander  
9 include_once platforms/ship.txt  
10 // red SOJ  
11 include_once platforms/soj.txt  
12 // blue commander  
13 include_once platforms/flight_lead.txt  
14 // air platform (used by blue and red)  
15 include_once platforms/striker.txt  
16  
17 script_variables  
18 Array<WsfGeoPoint> gAvoidPoints = Array<WsfGeoPoint>();  
19 Array<double> gAvoidRadii = Array<double>();  
20 // avoid the zone: 100 brigade sector  
21 gAvoidPoints[0] = WsfGeoPoint.Construct("30:22n 81:45w"); // lat lon string  
22 gAvoidRadii[0] = 1852*30.0; // 30.0 nm  
23 end_script_variables  
24  
25  
26 include_once event_output.txt  
27 
```

DISTRIBUTIostritittUeeedtetractsestftcumtl AERL/ROOD 20 20

platforms/striker.txt   
```txt
include_once weapons/aam/medium_range_radar Missile.txt include_once weapons/aam/simple_mrm_with_lc.txt include_once processors/quantum_agentaiai/behavior_agengage weaponry_task_target.txt include_once processors/quantum agents/aiai/behavior_planned route.txt include_once processors/quantum Agents/aiai/behavior_pursue-target-route_find.txt include_once processors/quantum agents/aiai/behavior_pursue weaponry_task_target.txt 
```

DISTRIBUTIOstrtithedtUoventdotracuOtesttcumetsld AFRL/RQQD 21

![](images/0eed62a29eaf33d3f872fdb638063da3f04ac3bcf2c65bedfe2859132da7e6a9.jpg)

# UNCLASSIFIED

# 行为代替

![](images/f4efdefb9c7fdf2ef2f4ee6137e8ade9dc3d2544b4452c959c4dd51265ca7c7d.jpg)

# platforms/striker.txt

```txt
61. weapon mrm MEDIUM_RANGE_RADAR_MISSILE  
62 quantity 6  
63 endweapon  
64 processor taskmgr WSF_QUANTUM_TASKER_PROCESSOR  
65 scriptDebugWrites off  
66 update_interval 5 sec  
67 behavior_tree  
68 selector  
70 #behavior node pursueweapon task target  
71 behavior_node pursue-target-route_finder  
72 behavior_node planned-route  
73 end_selector  
74 behavior_node engageweapon_task_target  
75 end_behavior_tree  
76 end Processor 
```

DISTRIBUTIostritittUeeedtetractsestftcumtl AFRL/RQQD 22 22

processors/quantum_agents/aiai/behavior_pursue-target_route_finder.txt   
DISTRIBUTIostrtittUeesdetracttftumtl AFRL/RQQD 23   
1 behavior pursue-target-route_find   
3 script debugWrites off   
4   
5   
6 script_variables   
7 //expected global externs   
8 #extern ArrayWsfGeoPoint> gAvoidPoints;   
9 #extern Array<double> gAvoidRadii;   
10 double cDEFAULT_ALTITUDE $= 9144$ ;// \~30,000 feet   
11 WsfRouteFinder mRouteFinder $=$ WsfRouteFinder();   
12 bool mDebugDraw $=$ true;   
13 WsfGeoPoint mTargetPoint;   
14 double mTargetSpeed $= 300$ .//300 ms (~600 knots)   
15 bool mForceRePath $=$ false;   
16 WsfDraw mDraw $=$ WsfDraw();   
17   
18 WsfGeoPoint mCurrentAvoidancePt $=$ WsfGeoPoint();   
19 WsfRoute mCurrentRoute $=$ WsfRoute();   
20   
21 end-script_variables

![](images/9416c9d43f6a653d9e1acc84d57ccc4c3a0ca0ab81399061726270cc66c59a48.jpg)

# UNCLASSIFIED

# 定义避让区域

![](images/aa0546668bec23be0ffe8da90e5e86a69df982ff853a394f9b507e1dd96d58ec.jpg)

processors/quantum_agents/aiai/behavior_pursue-target_route_finder.txt   
```txt
26 on_init   
28 mDraw层数Layer("pursue-target-route_find");   
29 mDraw.setDuration(PROCESSOR.UpdateInterval());   
30 mDraw.lineSize(1);   
31 //shift starting or ending points outside of any avoidances (dont shrink or ignore the   
32 mRouteFinder.SetImpossibleRouteResponse("SHIFT");   
33 mRouteFinder.setMaxArcLength(1852*5)； //max of 5 mile long arcs   
34 extern Array<WsfGeoPoint> gAvoidPoints;   
35 extern Array<double> gAvoidRadii;   
36 for (int i=0; i < gAvoidPoints.Size() && i < gAvoidRadii.Size(); i=i+1)   
37 { WsfGeoPoint pt = gAvoidPoints[i]; double radius = gAvoidRadii[i]; write_n_d(PLTFORM.Name(), "avoiding: ", pt.ToString(), "", at radius: ", radius); mRouteFinder.Avoid(pt, radius); }   
42 end_on_init   
44 
```

processors/quantum_agents/aiai/behavior_pursue-target_route_finder.txt   
DISTRIBUTIOstrtithdtUoeentecisdtetractostereqestftcmntal AFRL/RQQD 25   
74 mTargetPoint $=$ aTrack.CurrentLocation(); //set altitude double desiredAlt $=$ MATH.Max(PLATFORM.Altitude(),MATH.Max(cDEFAULT_ALTITUDE,mTat $\rightarrow$ mTargetPoint.Set(mTargetPoint Latitude(),mTargetPoint.Longitude()，desiredAlt); return true; } 1 return Failure("no valid target track was found!");   
83 end precondition   
87 execute #writeln_d("executing pursue-target-route_finder."); if (mForceRePath || PLATFORM.SlantRangeTo(mTargetPoint) > (3*mTargetSpeed)) //if we { WsfRoute path $=$ mRouteFinderRoute(TIME NOW,PLATFORM.Location(),mTargetPoint,mTarg if(!path.IsValid() || path.Size() <=0) { writeln_d("******ERROR:INVALID OR EMPTY PATH!!!!"); return; } WsfRoute avoidances $=$ mRouteFinderRouteAvoidances(); if(!avoidances.IsValid()) {

![](images/01ea92728b01a7baf934a7918e966aba205075506097a8c2a0e99f1a07389ed6.jpg)

# UNCLASSIFIED

# 执行

![](images/3de23341fa2f1fcf5e872bc2768ffc57723f627890ee13e7fc2b8db96c8b6697.jpg)

RUN IT!!!

现在会避开SAM

DISTRIBUTIOstritiuttUetisdtetractsrstftumtld AERL/ROOD 26 26

![](images/105f86c0c613bd29fd029f3759dff33831e011e8b90079a5a034c1fcc72212ac.jpg)

DISTRIBUIOstrtitdtUoenteidtractostetftmntal AFRL/RQQD 27

![](images/633253daa859a15a81a43da5f1d147713f99bf76d8fcaa6749afbfc4ce653ab7.jpg)

DISTRIBUTIostrittdveetecedthtractsgtheqstfoumntal AFRL/ROOD

# 6.1.10.5.返航与护航行为 25_AFSIM_BAM_Trng_GoHomeEscort

# 6.1.10.5.1. 本节想定解析

本节想定资源在以下目录下：

afsim2.9_src\training\user\10_Other_Topics\bam\scenarios\floridistan\25_floridistan_escort\run_co urse.txt，

行为与智能体建模培训的每一节都是在上一节的基础上的，而且想定较为复杂，因此要先了解上一节的内容。本节是在上一节的基础上给两部红方干扰机各生成了一个护航的飞机，但是没有给战斗能力，跑一会儿就被打掉了。如下图：

![](images/89cddeed31b599225d20632e49484c414086b08a866c226ab956e66c125e63c8.jpg)

可以看到蓝方 cap_south_1 发射的导弹马上就要将它击落了。

# 6.1.10.5.2. 本节 PPT 资料

本文为 afsim2.9_src\training\user\10_Other_Topics\bam\slides\25_AFSIM_BAM_Trng_GoHomeEscort.pptx 的翻译。

![](images/ff9140088c284ea195c683eebd0704e46e1749e6442eac4374a4a494ac420122.jpg)

Integrity★Service★ Excellence

# AFSIM用户培训

# 25-返航与护航行为

AFRL/RQQD

美国空军研究实验室

DISTRIBUIostrtittUeecdtetractsesftocta AFRL/RQQD 1 1

![](images/bdc0b21f2dd12746b990eb2cfb909ffc501e9080d78b44558f1ec5d29ac35387.jpg)

UNCLASSIFIED

# 燃料对象

![](images/060dbda5cfa6b543b685d326668d1de1c895f268e40b7b7fc24407b4ad5e1021.jpg)

# WsfFuel

WSF_FUEL,WSF_TABULAR_RATE_FUEL, WSF_VARIABLE_RATE_FUEL   
Existing Methods:

Mode, Refuel, QuantityRemaining, ConsumptionRate, XXXQuantity, TimeToXXX

DISTRIBUTIOstrtiuthodtoUovetAecisadtetractos,g9tereqstfrtmntald

AFRL/RQQD

# platforms/striker.txt

![](images/5cc73ce73f58d4df07b9fc8820367ccd3edd3681bd840f67a7c885e150a09b42.jpg)

DISTRIBUTIOstrtithdtUoeentecisdtetractostereqestftcmntal AFRL/RQQD ed3 3

# UNCLASSIFIED

![](images/588aa7beaf463c829abfa9dd2e24792a9e13c1b3a113d607da092c3e8f6e84ae.jpg)

# Escort Node in Behavior Tree

![](images/0431424a17556474ebb0e42151ceab91cb7ed18a848403abd4669defa04f0035.jpg)

# platforms/striker.txt

![](images/fd795cf46a8de566d40b2b482f013a381be035098c6ec2aa47dea4521141df3f.jpg)

![](images/b1e1e10d0041d00de9f373d12a38279a1100b3e25d4a1f452faf2ba04f8ce03e.jpg)

DISTRIBUTIostritittUeeedtetractseestftcumtld AFRL/RQQD 4 4

processors/quantum_agents/aiai/behavior_go_home.txt   
DISTRIBUTIOstrtithedtUoventdotrcuOtesttcumetld AFRL/RQQD d5 5   
precondition   
84 write_n_d("precondition go_home");   
85   
86 # if(!PROCESSOR.IsA_TYPEOf("WSF_RIPRPROCESSOR"))   
87 # { return Failure("behavior not attached to a RIPR processor!");   
88 # }   
90 string msg $= \mathrm{''}$ .   
91 bool result $=$ false;   
92   
93   
94 //go home if bingo on fuel   
95 if(mCheckFuel $= =$ true &&   
96 PLATFORM.FuelRemaining() < PLATFORM.FuelBingoQuantity())   
97 { msg $= \mathrm{"GO}$ HOME:bingo fuel";   
98 result $= \mathrm{true}$ ..   
100 }   
101 //go home if all my escorts are dead or gone   
102 else if(mCheckEscorts $= =$ true &&   
103 !HasEscorts()   
104 { msg $= \mathrm{"GO}$ HOME:all escorts are dead or gone";   
106 result $= \mathrm{true}$ ..   
107 }   
108 //DO NOT go home if I have any active weapons still under my control   
109 else if(mWaitOnActiveWeapons $= =$ true &&   
110 PLATFORM.WeaponsActiveFor(WsfTrackId()) <= 0)   
111 { msg $= \mathrm{"GO}$ HOME:no active weapons";   
113 result $= \mathrm{true}$ .   
114 }

![](images/7ec0d98218b68acdb12eb8030f4bf2415fe6d5027034b66fb362805c4cec68d3.jpg)

# UNCLASSIFIED

# 行为执行

![](images/ce549e2a86de063ad92d03c6e9b69a3b8eac44bb0980f30c399f8eb62483f785.jpg)

processors/quantum_agents/aiai/behavior_go_home.txt   
DISTRIBUIOstrtthodtUoventdotruOtsttumetsld AFRL/RQQD 6 6   
```txt
182 e execute
183 write_d(PLATFORM.Name(), " executing go_home, T=", TIME NOW);
184 // platFORM. Comment ("go_home");
185 string msg = "";
186 # WsfRIPRProcessor commander = ((WsfRIPRProcessor)PROCESSOR).CommanderProcessor();
187 if (commander.IsValid())
190 { for (int i = 0; i < ((WsfRIPRProcessor) PROCESSOR).NumJobChannels(); i = i + 1)
191 { commander.ClearBidsFor((WsfRIPRProcessor)PROCESSOR), i);
192 }
193 # } // TODO - reject or cancel any received tasks, we are going home
194 # }
195 # }
196 }
197 // TODO - reject or cancel any received tasks, we are going home
198 // make sure we are at the right speed so we don't burn the fuel we have left too fast
199 platFORM. GoToSpeed(cBINGO_SPEED);
200 }
201 }
202 // make sure we are at the right speed so we don't burn the fuel we have left too fast
203 platFORM. GoToSpeed(" , cBINGO_speed, ") );
204 write_d(" GoToSpeed( ", cBINGO_speed, ") ");
205 bool onHomeRoute = false;
206 }
207 // if an egress route is defined, and that is the current route,
208 // find the closest waypoint and fly the route from there.
209 // this is mainly used to correct some bugs in the 6dof mover
210 if (mRouteName != "") {
211 { WsfRoute myRoute = PlatFORM. Route();
212 }
213 { if (myRoute.Name() == "home-route")
214 { int routeIndex = PlatFORM. RoutePointIndex();
215 { if (routeIndex < 0 || routeIndex >= myRoute.Size())
216 { routeIndex = 0;
217 double distThreshold = 4.0*185.2; # # 4/10th nm
218 if (myRouteWAYpoint路线Index).Location().GroundRangeTo(PLATFORM.Location()) < d
220 } 
```

如果指定了护航目标，则执行。  
以编队偏移的方式飞行。  
忽略那些不构成威胁的任务。  
在以下任一情况下可能失败并脱离编队：

护航单位对威胁目标有武器任务。  
护航单位自身受到威胁目标的威胁。  
护航单位能够将威胁目标驱逐出受保护区域。

1 总结：当存在威胁时，护航单位会停止护航任务。

DISTRIBUIONCistititodtUvetAencdthotractorsg9tereqstsfotscumtld AFRL/RQQD 7

![](images/07bc17b2cb6c232d8d10875cfee4230f0e04677a4bf103ea47e4f3748ef935e0.jpg)

# UNCLASSIFIED

# 护航参数

![](images/f3a29bbbecea10077db4fbcec5d98f4859a862f1b63226d054229791b55eb804.jpg)

# ·护航行为举例

－所有参数都与护航对象、保护范围以及编队飞行相关。

-debugging parameters

```txt
- bool mDrawEscortData = false; 
```

-mode/control parameters

```txt
- bool mCheckOnlyTasks = true; 
```

```javascript
- bool mCheckMasterTracks = false; 
```

-escort parameters

```txt
- Array<string> mEscortNames;
- double mEscortProtectDistance = 100.0 * MATH.M_PER_NM(); 
```

-flying parameters

```txt
- double mFormationPositionX = 0; #meters in front of package
- double mFormationPositionY = 0; #meters off right wing of package 
```

-off-limit variables (not for user editing)

```txt
- WsfDraw mDraw;
- bool mLastInPosition; 
```

processors/quantum_agents/aiai/behavior_escort.txt

```c
behavior escort   
scriptDebugWrites off   
script_variables   
//**********   
//** debugging parameters   
//**********   
//**********   
bool mDrawEscortData = false;   
//**********   
//** control / mode of operation parameters   
//**********   
bool mCheckOnlyTasks = true;   
bool mCheckMasterTracks = false;   
//**********   
//** escort parameters (who to escort, and what ranges)   
//**********   
Array<string> mEscortNames = Array<string>();   
double mEscortProtectDistance = 100.0 * MATH.M_PER_NM(); #engage thre   
double mEscortChaseDistance = 15.0 * MATH.M_PER_NM(); #allowed to   
double mWeaponRangeToInclude = 50.0 * MATH.M_PER_NM();   
//**********   
//** flying parameters, for offset and tightness   
//**********   
double mFormationPositionX = 0; #meters in front of of package   
double mFormationPositionY = 0; #meters off right wing of package   
double mGoodformationRatio = 0.15; #percentage of total offset   
double mFormationLookAhead = 30.0; #seconds   
double mFormationAltitude = -1.0; #used if positive 
```

DISTRIBUTIostrtittUeeeedtractstftcumtld AFRL/RQQD edg 9

![](images/42e61a37ec15f996d7c8e766cb5d58f31c65f4b452f019dc9075d862ae65159e.jpg)

# UNCLASSIFIED

# 定义护航参数

![](images/f6874aea5db5187d47757a4eed8f4fb7a9715af526787390b4082ffae3a22c22.jpg)

# scenario_escort.txt

```c
27 platform Blue_2 STRIKER  
29 indestructible  
30 icon F-22  
31 side blue  
32 commander blue-FL  
33  
34 route  
35 position 0.3n 05:45:36.00e altitude 30000 ft msl speed 450 kts  
36 position 00:18:12.66n 02:34:24.22e altitude 30000.00 ft  
37 end-route  
38  
39 heading 270 deg  
40  
41 edit processor task_mgr  
42 edit behavior escort  
43 script_variables  
44 mDrawEscortData = true;  
45 mFormationPositionX = 3*1852;  
46 mFormationPositionY = -10*1852;  
47 mEscortNames[0] = "Blue_1";  
48 mEscortProtectDistance = 92600; // 50 nm  
49 end scripted_variables  
50 end_behaviour  
51 end Processor  
52 endplatform 
```

DISTRIBUTIostritittUeeedtetractsestftcumtl AERL/ROOD 10 10

![](images/c87b2417abe97636f486ecb570ddb7d75cb6584e4863944cd40b7df31c7d0ce2.jpg)  
DISTRIBUTIOstrtithedtUoventdotracuOtesttcumetsld AFRL/RQQD 11

![](images/f263dc19d7257ea2a894c29058448f3db5e5c1ed98ceb487b4de1d9a78955502.jpg)

# UNCLASSIFIED护航响应

![](images/4cc6bea47d89f6d9be724537f83cf6a42c3b097935d7523b7fce073c72234bf0.jpg)

![](images/3b8d476d34191d222abcb0f8975596d392228cb2a4ac78dc2c40bff65f1a6000.jpg)

![](images/ddf595105085377761a9acd7a3d20a56ad616d61fb0252a5ac5ca09922e8b1c5.jpg)  
DISTRIBUIOstrtitdtUteisdtetractsteesftmntal AFRL/RQQD 12 12

添加两个新的蓝色平台：

“一个护航当前的护航单位。  
为其设置一个更小的保护半径。  
·另一个护航原始的目标物。  
为其设置一个不同的编队偏移。

提示：

护航单位会尝试移动到指定位置一一可以考虑从不同的初始位置开始。

DISTRIBUTIOstrtithodtoU.oventAcdotrsugOtrststisumetsld AFRL/RQQD 13

![](images/d7042b0025ebcceb4511f41568b43c584681f303e1930701dc7b90922752984f.jpg)

# UNCLASSIFIED

# 护航一个绕圈飞行的目标物

![](images/0c33be47ae3a719da8f761b6f03887418e09a3eea52733e94278500ca79c304e.jpg)

![](images/e1547c87497062ebdab6a67aadbd75aea0f06f61eb003e1ecf18c9a36bef2c32.jpg)

DISTRIBUTIOstrittdvetAgecdtheotractsgOthreqstsfortumtal AFRL/ROOD 14 14
scenarios/red_air_support.txt   
DISTRIBUON C. Distribution authorized to U.S. Government Agencies and their contractors, 9 Aug 19. Other requests for this document shall be referred to AFRL/RQQD 15   
```txt
74 platform escort_south RED_STRIKER   
76 side red   
77 icon weasel   
78 command_chain red_chain ship_lead   
79 route   
81 position 29:33:57.54n 80:08:06.19w altitude 35000 ft msl   
82 speed 450 kts   
83 position 29:46:00.17n 80:36:37.58w altitude 35000 ft msl   
84 end-route   
85 NOTE: added north AND south escorts!!!   
86 heading 250 deg   
87 edit processor task_mgr   
89 edit behavior escort   
90 script_variables   
91 mDrawEscortData = true;   
92 mEscortNames[0] = "soj_south";   
93 mFormationPositionX = 0; // meters in front of of package   
94 mFormationPositionY = -5*1852; // meters off right wing of package   
95 mEscortProtectDistance = 60 * MATH.M_PER_NM();   
96 mWeaponRangeToInclude = 0;   
97 mEscortChaseDistance = 5 * MATH.M_PER_NM();   
98 end scripted_variables   
99 end_behavior   
100 end Processor   
101 endplatform 
```

![](images/aead2459af7e8f03b85d5b5753c62ba16a9bd2d62abc86286a02fc5c2d8f2bac.jpg)