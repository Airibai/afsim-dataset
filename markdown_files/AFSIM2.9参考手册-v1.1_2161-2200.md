完成 MATLABBallisticMover 类构造函数的实现（位于

MATLABBallisticMover.cpp 文件中）。

每个 mrow 类在构造时都需要指定大小。

添加一行代码来构造mwInputOrientation成员变量。

mwInputOrientation 构造函数需要四个参数：

1. 行数（number of rows）：  
2. 列数（number of columns），  
3. 矩阵的数据类型（data type of the matrix），以及  
4. 矩阵的复杂性（complexity of the matrix，详见 MATLAB® 文档）。

对于mwInputOrientation成员变量：

- 它将有3行，1列，  
- 数据类型为mxDOUBLE_CLASS,  
复杂性类型为mxREAL。

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19.

Other requests for this document shall be referred to AFRL/RQQD.

49

![](images/0abc1cd5d945620193db123515e8ecd4e62cf135feb7c7262624af69d7cd461b.jpg)

# Mover练习2 — 任务1 解决方案

# MATLABballisticMover.cpp

![](images/189fff98ab1d287dc32e5f3a8595f00db69a1fb84016ec566a3ebaab19579d76.jpg)

MATLABBallisticMover::MATLABBallisticMover(WsfScenario& aScenario)

: WsfMover(aScenario),

mwInputLLA(3,1,mxDOUBLE_CLASS,mxREAL),

// EXERCISE 2 TASK 1

mwInputOrientation(3, 1, mxDOUBLE_CLASS, mxREAL),

mwInputTime(1, 1, mxDOUBLE_CLASS, mxREAL),

mwInputBoosterParams(cBOOSTER_PARMS_SIZE, 1, mxDOUBLE_CLASS, mxREAL),

mInputAlt(0.0),

mInputAltAGL(false),

mStageList(),

mExplicitStageUsed(false),

mImplicitStageUsed(false),

mCd0(0.0),

mReferenceArea(0.0),

mMassPayload(0.0),

mMaxq(0.0),

mPitchInterval(1.0),

mVerticalTime(0.0),

mwHitGroundTime(1, 1, mxDOUBLE_CLASS, mxREAL),

mwState(cSTATE_VECTOR_SIZE, 1, mxDOUBLE_CLASS, mxREAL)

$\left\{  \begin{array}{ll} {10} & \text{ 若 }{a}_{3} = {a}_{4} = {20} \\  {10} & \text{ 若 }{a}_{5} = {a}_{6} = {25} \\  {10} & \text{ 若 }{a}_{7} = {a}_{8} = {28} \end{array}\right.$

…

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19.

Other requests for this document shall be referred to AFRL/RQQD.

- 检查文件 libAFSIM_Mover.h，并查看文件底部声明的 extern 方法。这两个方法将在 MATLABBallisticMover 类的不同阶段被调用。  
- 这些方法分别对应 MATLAB 函数 InitializeMover (InitializeMover.m) 和 UpdateMover (UpdateMover.m)。

```c
extern LIB_libAFSIM_Mover_CPP_API void MW_CALL_CONV InitializeMover(int nargout, mwArray& state, const mwArray& inLLA, const mwArray& inBoosterParams);   
extern LIB_libAFSIM_Mover_CPP_API void MW_CALL_CONV UpdateMover(int nargout, mwArray& state, mwArray& hit-ground_time, const mwArray& t, const mwArray& x, const mwArray& inLLA, const mwArray& inOrientation, const mwArray& inBoosterParams); 
```

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

51

![](images/6df99f265e44e660c026397b69f618b8c8ed4ec4c1496b58a43d68a68c692c6c.jpg)

# Mover 练习2 - 检视3

# MATLAB function InitializeMover - file InitializeMover.m

![](images/8b9fd2f8e08154ae602a4742a0eacdc1a6bde36e953a494b5eb56b6e8e9a7a48.jpg)

```matlab
function [state] = InitializeMover(inLLA, inBoosterParams)  
% Zero the return values  
state = zeros(1,24);  
% Read input  
% LLA  
latitude = inLLA(1); % degrees  
longitude = inLLA(2); % degrees  
altitude = inLLA(3); % km  
% Booster parameters  
mass_1st = inBoosterParams(6);  
mass_2nd = inBoosterParams(7);  
mass_3rd = inBoosterParams(8);  
mass_load = inBoosterParams(12);  
thrust_1st = inBoosterParams(15);  
:  
% Fill in initial state values  
state(1) = x_eci(1);  
state(2) = v_eci(1);  
state(3) = x_eci(2);  
state(4) = v_eci(2);  
state(5) = x_eci(3);  
state(6) = v_eci(3);  
state(7) = total_mass; % kg  
state(8) = latitude; % degrees  
state(9) = longitude; % degrees  
state(10) = altitude; % km 
```

: state(11) $= 0$ % Great circle range 0 km state(12) $=$ Thrust_mag; $\%$ Thrust magnitude state(13) $=$ Gravity_mag; $\%$ Gravity magnitude state(14) $= 0$ % Drag magnitude state(15) $= 90$ .. $\%$ alpha 90 degrees state(16) $= 90$ .. $\%$ aoa 90 degrees state(17) $=$ x_ecef(1); $\%$ positon in ECEF frame state(18) $=$ x_ecef(2); $\%$ state(19) $=$ x_ecef(3); $\%$ state(20) $= 0$ . $\%$ velocity in ECEF frame state(21) $= 0$ . $\%$ state(22) $= 0$ . $\%$ state(23) $= 0$ . $\%$ time 0 sec state(24) $= 0$ . $\%$ stage

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQDD.

function [state, hitGround_time] = UpdateMover(t, x, inLLA, inOrientation, inBoosterParams)

$\%$ Zero the return values state $=$ zeros(1,24); hit-ground_time $= 0.0$

```matlab
%Set state variables  
ECI(1) = x(1);  
ECI(2) = x(2);  
ECI(3) = x(3);  
ECI(4) = x(4);  
ECI(5) = x(5);  
ECI(6) = x(6);  
M = x(7);  
alpha = x(15);  
aoa = x(16);  
dt = t - x(23);  
stage = round(x(24));  
hit-ground_time = 0.0; 
```

latitude = inLLA(1);
longitude = inLLA(2);
altitude = inLLA(3);
% Orientation
azimuth = inOrientation(1);
fpa = inOrientation(2); $\vdots$

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

53

![](images/86d1df70f6ea86ae25c8307dc58359593535336308f26c32292f257e88364fb2.jpg)

# UNCLASSIFIED

# Mover练习2—任务2

![](images/fb958ba9bb279988caf7047407bfa75f07e8f47664097b9b56402695afe1d627.jpg)

- 实现 MATLABBallisticMover::ProcessInput 方法以读取以下内容:

```txt
- massPGA  
- pitch_interval 
```

- 具体要求如下：

1. 属性 mass_payload 的单位是质量，其值必须大于 0.0。  
2. 属性pitch_interval的单位是时间，其值必须大于或等于1.0。

- 每个输入值都应存储在对应的 MATLABBallisticMover 类的成员变量中。

可以通过在源代码中搜索对“ReadValue”和“ReadValueOfType”的引用来找到AFSIM的示例。

```cpp
bool MATLABBallisticMover::ProcessInput(UtInput& aInput)  
{  
    ...  
else if (command == "massPGA")  
{  
// EXERCISE 2 TASK 2a  
aInput.ReadValueOfType(mMassPayload, UtInput::cMASS);  
aInput.ValueGreater(mMassPayload, 0.0);  
}  
else if (command == "pitch_interval")  
{  
// EXERCISE 2 TASK 2b  
aInput.ReadValueOfType(mPitchInterval, UtInput::cTIME);  
aInput.ValueGreaterEqual(mPitchInterval, 1.0);  
} 
```

可以通过在源代码中搜索对“ReadValue”和“ReadValueOfType”的引用来找到AFSIM的示例。

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

55

![](images/b80b2aede7d8de8dd1b451b606008021271fa1226d86aa684aea9694055cfe59.jpg)

# UNCLASSIFIED Mover练习2—检视5

# MATLABballisticMover.cpp

![](images/5e1212bfd0eae3fd462e411f78e6ebd83801c4c533f8bb423e4bf9caeda3a678.jpg)

```cpp
bool MATLABBallisticMover::ProcessInput(UtInput& aInput) 注意：变量 mStageList 是一个类型为  
{ // Set the default value MATLAB BallisticMover::Stage 的数组。  
bool myCommand(true);  
std::string command(aInput.GetCommand());  
if ((! mExplicitStageUsed) && mStageList[0].ProcessInput(aInput))  
{ mImplicitStageUsed = true; } else if (!mImplicitStageUsed) && (command == "stage")) { UtInputBlock inputBlock(aInput); int stageNumber; aInput.ReadValue(stageNumber); aInput.ValueInClosedRange(static_cast<double>(stageNumber), 1.0, static_cast<double>(mStagelist.size() + 1)); if (stageNumber > ut::cast_to_int(mStageList.size())) { mStageList.push_back(Stage()); } while (inputBlock.ReadCommand()) { if (!mStageList[stageNumber - 1].ProcessInput(aInput)) { throw UtInput::UnknownCommand(aInput); } } 
```

} DISTRIBUTION C.D.

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19.

Other requests for this document shall be referred to AFRL/RQQD.

:   
else if ((command $= =$ "zero Lift cd") || (command $= =$ "drag_coeff"))   
{   
}   
:   
else if (command $= =$ "vertical_time") {   
:   
}   
else   
{ myCommand $\equiv$ WsfMover::ProcessInput(aInput);   
}   
return myCommand;

mover MATLAB BALLISTIC MOVER

update interval 1 sec

stage 1

fuel

27941 kg

total

31343 kg

thru

1230600 Nt

burn time

76 sec

end stage

stage 2

fuel mass

8872.3 kg

total

10233 kg

thrust

529290 Nt

burn time

59 sec

end stage

stage 3

fuel mass

3265.9 kg

total

4209.3 kg

thrust

200140 Nt

burn time

49 sec

end stage

drag coef

0.4

effective area

2.986 meters^2

mass payload

900 kg

maxq

650 // lb/ft^2

pitch interval

35 sec

vertical time

10 sec

end mover

57

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19.

Other requests for this document shall be referred to AFRL/RQQD.

# UNCLASSIFIED

# Mover练习 2 — 检视6

# MATLABBallisticMover.cpp

![](images/e392b8ad32bdc4fc5110f31623134cca257488f98e92a47b3136cfc28f93787c.jpg)

![](images/be961690a3323eee2339f989c0479760b3f65d0ece082e9582c49ed3c3503772.jpg)

bool MATLABBallisticMover::Stage::ProcessInput(UtInput& aInput)

{ bool myCommand(true); std::string command(aInput.GetCommand()); if((command $= =$ "total_mass") || (command $= =$ "launch mass"）） { aInput.ReadValueOfType(mTotalMass，UtInput::cMASS); aInput.ValueGreater(mTotalMass,0.0); } else if (command $= =$ "fuel_mass") { aInput.ReadValueOfType(mFuelMass，UtInput::cMASS); aInput.ValueGreater(mFuelMass,0.0); } else if (command $= =$ "thrust") { aInput.ReadValueOfType(mThrust，UtInput::cFORCE); aInput.ValueGreater(mThrust,0.0); } else if((command $= =$ "thrust_duration") (command $= =$ "burn_time")) { aInput.ReadValueOfType(mThrustDuration，UtInput::cTIME); aInput.ValueGreaterEqual(mThrustDuration，0.0); } else { myCommand $=$ false; } return myCommand;

```txt
mover MATLAB BALLISTIC_MOVER  
update interval 1 sec  
stage 1  
fuel_mass 27941 kg  
total_mass 31343 kg  
thrust 1230600 Nt  
burn_time 76 sec  
end stage  
stage 2  
fuel_mass 8872.3 kg  
total_mass 10233 kg  
thrust 529290 Nt  
burn_time 59 sec  
end stage  
stage 3  
fuel_mass 3265.9 kg  
total_mass 4209.3 kg  
thrust 200140 Nt  
burn_time 49 sec  
end stage  
:  
end mover 
```

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19.

Other requests for this document shall be referred to AFRL/RQQD.

58

- 实现 MATLABBallisticMover::Stage::ProcessInput

函数以读取以下内容：

- total_mass（总质量），以及

这些是彼此的同义词，应该导

- launch_mass（发射质量）。

- 属性 total_mass / launch_mass 的单位为质量，并且其值必须大于 0.0。  
- 该输入应存储在 MATLABBallisticMover 类的成员变量 mTotalMass 中。

AFSIM 示例可以通过搜索源代码中引用“ReadValue”和“ReadValueOfType”来找到。

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19.

Other requests for this document shall be referred to AFRL/RQQD.

59

![](images/621971909f6399f588614f87860f08381488bd97032fc88653713f6cd0021988.jpg)

# Mover练习2—任务3解决方案

# MATLABBallisticMover.cpp

![](images/68657eb91892b99ced0e8519e0cae7c6ac1e9c2fe0eb4c0fabf79a546c78103e.jpg)

bool MATLABBallisticMover::Stage::ProcessInput(UtInput& aInput)

bool myCommand(true); std::string command(aInput.GetCommand()); if((command $= =$ "total_mass") || (command $= =$ "launch_mass")) { //EXERCISE2TASK3 aInput.ReadValueOFType(mTotalMass，UtIn aInput.ValueGreater(mTotalMass，0.0); }

}

- 检视和理解  
```cpp
void MATLABBallisticMover::GetBoosterParams()  
{ // Initialize the booster parameters to zero double dBooster[cBOOSTER Params_SIZE] = {0.0}; // Get the stage data; stop at 3 stages int nStages(mStageList.size()); if (nStages > 3) { nStages = 3; } for(int i = 0; i < nStages; ++i) { // burn_time dBooster[nBurnTimeIndex + i] = mStageList[i].mThrustDuration; // total_mass dBooster[nTotalMass + i] = mStageList[i].mTotalMass; // fuel_mass dBooster[nFuelMass + i] = mStageList[i].mFuelMass; // thrust dBooster[nThrust + i] = mStageList[i].mThrust; } } DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQDD. 
```

![](images/932e8083305c1072bfc38e105e4c8a987c3b8d98ad436980427e7324e48929bc.jpg)

# UNCLASSIFIED

# Mover练习2—检视8

# MATLABballisticMover.cpp

61

![](images/911b543e3d7999ad0171b711ddb43c3c727b5e9e6fe62f616938cc3afb743bce.jpg)

- 理解MATLABBallisticMover::Initialize中包含的代码:

- 将数组 mwInputLLA 和 mwInputBoosterParams 分别通过调用 GetInitialAltitude 和 GetBoosterParams 方法填充。

```cpp
bool MATLABBallisticMover::Initialize(double aSimTime)  
{ // Get the altitude GetInitialAltitude(); // Get the booster parameters GetBoosterParams(); // EXERCISE 2 TASK 4 // Call the MATLAB to initialize // PLACE YOUR CODE HERE // EXERCISE 2 TASK 5 // Set orientation // Initialize the base class return WsfMover::Initialize(aSimTime); } 
```

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

63

![](images/f30d9eedf7a6ebb2c761511609cfc2091541fecff628a82c0007c9b3dd15f57a.jpg)

UNCLASSIFIED

# Mover练习2—任务4

![](images/dbcdfc67459d4db909aa0c581c22efb2edbf8d2d74f8986849ac6816c82d7988.jpg)

# 在MATLABBallisticMover.cpp中

- 任务4: 初始化MATLAB® mover

- 调用libAFSIM_Mover接口中的InitializeMover方法.

- 此方法需要四个参数：

1. 输出参数的数量，  
2. 用于保存状态的输出 mwwarray,  
3. 包含初始纬度、经度和高度的输入mwarray，  
4. 包含助推器参数的输入 mwwarray。

```cpp
bool MATLABBallisticMover::Initialize(double aSimTime)  
{ // Get the altitude  
GetInitialAltitude();  
// Get the booster parameters  
GetBoosterParams(); 
```

```txt
// EXERCISE 2 TASK 4
// Call the MATLAB to initialize
InitializeMover(1, mwState, // output
mwInputLLA, // input
mwInputBoosterParams); 
```

```objectivec
// EXERCISE 2 TASK 5 // Set orientation 
```

```cpp
// Initialize the base class return WsfMover::Initialize(aSimTime); } 
```

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

# UNCLASSIFIED

# Mover练习2—任务5

65

![](images/e93a45f1e396aff9a24d5276949f626b3a5848d3ea89ad3b9079e3d6b82d4534.jpg)

![](images/74d3b40ac81fe74d0d6d0790d9e982a088d7206575117b4a93624a30ee4ec9ef.jpg)

在文件 MATLABBallisticMover.cpp 中：

任务5：完成MATLABBallisticMover::Initialize方法：

从MATLAB库中获取输入方向，并使用它设置航向。

将平台的初始方向设置为输入航向（以弧度为单位）和90度俯仰角（以弧度为单位）。

步骤：

1. 创建一个大小为3的double类型数组，命名为dInputOrientation，并将其元素初始化为0.0。  
2. 调用mwInputOrientation GetData()方法，并传入以下两个参数：

1. 参数 1: 数组 dInputOrientation  
2. 参数 2: 数组的大小

3. 定义并设置航向（heading），将dInputOrientation数组的第0个元素转换为弧度（乘以UtMath::cRAD_PER_DEG）。  
4. 定义并设置俯仰角（pitch），将其设置为UtMath::cRAD_PER_DEG（90度的弧度值）。  
5. 调用GetPlatform()方法，并对返回的平台调用SetOrientationNED()方法，传入以下参数：

1. 航向（heading）  
2.俯仰角（pitch）   
3.0.0（平台的滚转角 roll）。

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQQD.

```cpp
bool MATLABBallisticMover::Initialize(double aSimTime)  
{ // Get the altitude GetInitialAltitude(); // Get the booster parameters GetBoosterParams(); // EXERCISE 2 TASK 4 // Call the MATLAB to initialize InitializeMover(1, mwState, // output mwInputLLA, // input mwInputBoosterParams); 
```

```cpp
// EXERCISE 2 TASK 5
// Set orientation
double dInputOrientation[3] = {0.0};
mwInputOrientation GetData(dInputOrientation, 3);
double heading = dInputOrientation[0] * UtMath::cRAD_PER_DEG;
double pitch = UtMath::cPI_OVER_2;
GetPlatform()->SetOrientationNED(heading, pitch, 0.0); 
```

```cpp
// Initialize the base class return WsfMover::Initialize(aSimTime); } 
```

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

# UNCLASSIFIED

# Mover练习2—任务6

67

![](images/2cc67c266f59c802e757fe4e96a4ebd7bcab687c12d5587fe7cf815ba6291a87.jpg)

![](images/f20b6813bc65ef7cd7efa22c88015d0ff7f6a99bd80c74e88cf3d4b68747c6ba.jpg)

在文件 MATLABBallisticMover.cpp 中：

实现 MATLABBallisticMover::Update 方法

调用libAFSIM_Mover接口中的UpdateMover方法。

UpdateMover 方法需要以下八个参数：

输出参数的数量，

1. 用于保存状态的输出 mwwarray,  
2. 用于保存移动器触地时间的输出mwarray，  
3. 包含当前仿真时间的输入mwarray，  
4. 包含当前状态的输入 mwwarray,  
5. 包含初始纬度、经度和高度的mwarray，  
6. 包含初始方向的 mwarray,  
7. 包含助推器参数的输入mwarray。

执行更新后，使用数据更新平台的位置、速度、方向等信息。

如果移动器已经触地，则删除平台。

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQQD.

```cpp
void MATLABBallisticMover::Update(double aSimTime)  
{ if((aSimTime - mLastUpdateTime) > mUpdateTimeTolerance) { // Set the input parameter - time mwInputTime.SetData(&aSimTime, 1); 
```

```cpp
// EXERCISE 2 TASK 6
// -- call MATLAB update function
UpdateMover(2, mwState, mWHitGroundTime, // output
		mwInputTime, // input
		mwState,
		mwInputLLA,
		mwInputOrientation,
		mwInputBoosterParams);
}
// Update the platform location, velocity, orientation, etc.
UpdatePlatform(aSimTime);
...
// Call base class implementation last
WsfMover::Update(aSimTime); 
```

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

69

![](images/e1f07792f01b9e06f94a812399a9d571f4ed26943f8ebc136b0e8f77b6eeb141.jpg)

# UNCLASSIFIED

# Mover练习2—任务7

![](images/786a8febedbb41dd91aa321eee49916285e6d8575d052309fabff1ebbcf87099.jpg)

在文件 MATLABBallisticMover.cpp 中：

实现 MATLABBallisticMover::UpdatePlatform 方法

此方法从 MATLAB® 移动器返回的数据（存储在名为 mwState 的 mwaray 中）中提取数据，并将相应的数据设置到 AFSIM 平台中。

关于mwState成员变量的描述可以在MATLABBallisticMover.hpp文件的注释中找到。

mwState GetData 方法会提取数据并将其存储到一个数组中（我们称之为 dState）。

- dState 的元素 0、2 和 4 包含 ECI 位置的三个分量。  
- dState 的元素 1、3 和 5 包含 ECI 速度的三个分量。

任务7：

1. 创建一个大小为3的double类型数组，用于存储ECI速度的分量。  
2. 从mwState中提取ECI速度值（存储在dState[1]、dState[3]和dState[5]中），并将这些值分别填充到ECI速度数组中。  
3. 调用GetPlatform()->SetVelocityECI()方法，并传入包含ECI速度的数组，以设置平台的ECI速度。

```cpp
//  
void MATLABBallisticMover::UpdatePlatform(double aSimTime)  
{ // Get the MATLAB result  
double dState[cSTATE_VECTOR_SIZE] = {0.0};  
mwState GetData(dState, cSTATE_VECTOR_SIZE);  
;  
// Update platform with new ECI location  
double newLocECI[3] = {0.0};  
UtVec3d::Set(newLocECI, dState[0], dState[2], dState[4]);  
GetPlatform()->SetLocationECI(newLocECI); 
```

```cpp
// EXERCISE 2 TASK 7
// Update platform with new ECI velocity
double newVelECI[3] = {0.0};
UtVec3d::Set(newVelECI, dState[1], dState[3], dState[5]);
GetPlatform()->SetVelocityECI(newVelECI); 
```

```txt
… 
```

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

# UNCLASSIFIED

# 练习3

71

![](images/40c8fc8803c781e1c2d6579ecd352428d2d2a7a1d54c5af5e2e282440352ae68.jpg)

![](images/98633535ea107bfb542dcd6910f45f352ac143cd6410887e4eedccad583975c9.jpg)

在 MATLAB 中打开 MATLAB 文件  
- 理解 makelib.m 文件  
- 创建 MATLAB 库文件  
- 部署 MATLAB 库文件

- 您将创建一个 MATLAB® 编译的 C++ 共享库，以集成到移动器项目中（有关更多信息，请参考 MATLAB®）。

![](images/d2a749a93fd1a9a0f18603594a5469bfe357a7f85783c9a5c0d0165beef5f3b7.jpg)

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

UNCLASSIFIED

![](images/2eb1455dae00ba69b656de94462fa43ad805d506b6da8d17ce64fbd865a24365.jpg)

# [可选]Mover练习3\* - 任务1

要求安装 MATLAB®

![](images/888e3aca7bf179f98508bf8d69ff1ca330d9ef940fac48f4e4c715f320742e1b.jpg)

73

编译 MATLAB® M 文件 - 任务 1

1. 打开 MATLAB® 应用程序。  
2. 通过浏览到 inwork\hover\MATLAB_mover 目录来更改“当前目录”。现在，该目录中的所有 M 文件都应该在 MATLAB 应用程序中可见。

编译 MATLAB® M 文件 - 任务 2

1. 双击 makelib.m 文件。这将会在 MATLAB® 编辑器中打开该文件。  
2. 查看并理解文件的内容（MATLAB 命令）。

cmdFlags $= \{\dots$ %'-v';% verbose  
'-N';% clear MATLAB path  
'-W';'cpplib:libAFSIM_Mover';% create C++ library wrapper named libAFSIM_Mover  
'-T';'link:lib';% link library  
'-d';'./lib';% output directory}；  
mFiles $= \{\ldots$ 'InitializeMover.m'; 'UpdateMover.m';   
};  
gcc(cmdFlags{：},mFiles{：});

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

75

![](images/ae8297bd7422cb95dd9e1504c625fdd4634baf882f87884001b7affe90fb3db5.jpg)

UNCLASSIFIED

# [可选]Mover练习3\* - 任务3

要求安装 MATLAB®

![](images/46de92177c149f7e98c1e15c5326126bad3f79f558981161be09848778648d95.jpg)

编译 MATLAB® M 文件 - 任务 3

1. 在 MATLAB® 命令窗口中输入 makelib，以创建 C++ 共享库。这将需要几分钟时间完成。  
2. 使用Windows资源管理器定位到inwork\mover\MATLAB_mover目录，查看编译步骤生成的文件。  
3. 将libAFSIM_Mover.dll文件移动到inwork\mover\datab目录中。

# 部署共享库

要分发使用 MATLAB® 编译器创建的共享库，请创建一个包含以下文件的安装包：

1. MCRInstaller.exe（位于 <MCR install folder>\toolbox\compiler\deploy)  
2. libAFSIM_Mover.h   
3. libAFSIM_Mover.lib   
4. libAFSIM_Mover.dll

请注意，在编译步骤中生成的README.txt文件位于inwork\hover\MATLAB_mover目录中，其中包含有关部署的有用信息。

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQQD.

# UNCLASSIFIED

![](images/a42dce89dfb79f9c665650ef37ced96893111ec4ac2f131bd6a2056b697e0345.jpg)

# 测试

![](images/d70cac4a4c427c492e161524b1527ef868dcf570a32ea9872ee81d925e91bd3e.jpg)

- 从 Visual Studio 开始:

1. 在 Release 模式下构建解决方案。  
2. 构建 INSTALL 项目。

Linux: 在构建目录,运行:
$ cmake --build . --target all -- -j11
$ cmake --build . --target install -- -j11

3. 将测试场景加载到 WIZARD 中:

打开 WIZARD。  
- 找到位于...mover\data文件夹中的顶级场景文件moverscenario.txt。这是我们用来测试程序的输入文件。  
- 将 moverscenario.txt拖放到WIZARD中。

4. 从 WIZARD 中运行选定的应用程序。  
5. 在Mystic中运行生成的moverscenario.aer文件。

![](images/e05c58ad2cfe6750a318b2771005b5e2fe4dd6aa277df74a4e5554059a012f10.jpg)  
DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQDD.

![](images/15d926dec71ab056989ea83678b684d993c1a6e7389baecc70533a4a51efe74e.jpg)

![](images/cf269cacaf06e34283933c06be890eb0cb6d5335d781bfe77fe1d9467a2e3a0b.jpg)  
UNCLASSIFIED

![](images/77725105a1db19a5f0ea7d22a7098c82d031bc5b1391d9ccb30b5cedc46ff4b8.jpg)

# 6.2.1.8. 组件 7_AFSIMDev_Trng_Components

本文为afsim2.9_src\training\developer\core\slides\

7_AFSIM_Dev_Trng_Components.pptx 的翻译，主要是介绍如何扩展自定义组件，并做了许多

![](images/8fd3bdffc78107ecda547c48947e9cc7d423a208b238920b257a3dc94847eee0.jpg)

Integrity $\star$ Service $\star$ Excellence

# AFSIM开发培训

# 7-组件

本文档由杨石兴翻译，该资料做为《AFSIM2.9参考手册》的一部分。没有《AFSIM2.9参考手册》的加杨石兴微信领取：13324598743

# AFRL/RQQD美国空军研究实验室

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQQD.

# UNCLASSIFIED

![](images/c737580e1d69820e54297c81051885f0cd1bb5e008eb810a4ade19820dcc9956.jpg)

# 缩写和术语

![](images/978ecf8f6a24b8452fc3ac5da134e51d1e0cf59c9a234fb50d0890fd5ae5d025.jpg)

AFSIM - Advanced Framework for Simulation, Integration, and Modeling

AGL - Above Ground Level

DIS-Distributed Interactive Simulation

DTED-Digital Terrain Elevation Data

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

本实验重点在于理解AFSIM组件及其扩展：

- 您将构建一个新的AFSIM组件类，该类不是“标准”组件之一，学习如何使用组件工厂配置组件实例、处理自定义输入，并在平台上访问它们。  
- 您将构建一个新的AFSIM组件扩展，为现有组件提供额外功能，而无需扩展现有的组件类。  
- 您将了解如何扩展现有的 AFSIM 脚本类，以添加额外功能，而无需修改核心代码。

以下练习将提供操作AFSIM组件的实践：

练习1：注册一个新的应用程序扩展、新的场景扩展和一个组件工厂。

练习2：创建一个自定义的AFSIM组件。

练习3：创建一个组件工厂。

练习4：创建一个自定义的AFSIM组件脚本接口。

![](images/ddd5f55630c7901da596d5f26396751f2ddc9131105b54362aa6a518ebcb7c2d.jpg)

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

# UNCLASSIFIED

# 问题陈述

3

![](images/bc360a54059d3b2569fb0bf6d8865acbb26d5268e136dccbb6caad3c9affb2b7.jpg)

![](images/d412727e22cb022eea813d81e22c47116cfc298f6003f6e2b8bb3e4abc75e053.jpg)

- 在网络攻击中影响传感器检测以删除传感器轨迹：  
- 创建一个名为 Shields 的新组件，该组件被插入到平台上，并且不需要使用辅助数据（Aux Data）。  
- 创建一个简单的新组件，名为 Latinum，它代表一种可以在平台之间传输的商品。  
- 将Shield组件暴露到脚本接口中，作为一个可以查询的脚本Shields对象。  
- 扩展现有的 WsfPlatform 脚本类, 使其返回一个 Shields 脚本对象。

![](images/e93b0be38a83b5c5f73219f6f291694cdf79edb4dfef297bec8d2379bfaf1361.jpg)

- 理解如何创建新的组件和组件扩展。  
- 理解创建组件工厂并通过组件的输入处理对其进行注入的选项。  
- 理解如何在不使用输入的情况下注入组件。  
- 理解如何扩展现有的脚本类以包含新方法，而无需修改核心代码。  
- 巩固创建应用程序扩展和插件的技能。  
- 理解如何创建新的场景扩展。

![](images/7ce89ebd0d503e8a5428352b8487bdfb7ad5be141e5961c06d5c5023566740a3.jpg)

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

# UNCLASSIFIED

![](images/a655a6a41e1fb8f319dc666207ff8090514d2911238770ffce3ce86d041e680d.jpg)

# 提前掌握

![](images/2717cdfb64a78454383d599c275bf4530a4705e5a186ea4e34f8d62120efac00.jpg)

- 在开始本实验之前，您应该：  
- 熟悉 WIZARD 和 AFSIM 脚本语言。  
- 建议参加过AFSIM分析师课程或具有同等经验。

- 熟悉并能够使用 Microsoft® Visual Studio 2017® 或更新版本来编译应用程序。  
- 熟悉使用 Microsoft Windows® Explorer。

- 已完成模块“使用 CMAKE 构建 AFSIM”。

- 熟悉使用 cmake-api。  
- 如果在 Linux 上开发，熟悉执行 cmake。

![](images/7b2373a63a73ae902f1d1cbc4685b177836a0283380a84d5e1106bb8b2928d1e.jpg)  
基于组件的方法允许添加和移除整个类型。

- 平台/仿真组件类型可以通过名称或角色进行访问。  
- 支持从仿真和平台中添加或移除组件类型

例如：在EAR版本中移除武器和电子战（EW）功能，并仅在ITAR版本中添加这些功能

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

UNCLASSIFIED

![](images/c9fed2fd044d7bb154aba5da7c4252a686297d20213940bb7f48b2cbb9ea10ad.jpg)

# AFSIM框架中的组件

![](images/0566be8e25eb619e12d83659ec86f313dcf97a744ce776e7e154748a04ecc649.jpg)

- AFSIM 允许将任意组件放置在平台和平台组件（如传感器）上。

- “基于组件的架构”（Component-Based Architecture, CBA）。

![](images/b42e2b4452ae1ea5128ba9a58b34546a40db229c27b9aab10ad1a23d973e46b6.jpg)

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19.

Other requests for this document shall be referred to AFRL/RQQD.

- AFSIM 允许将任意组件放置在平台上。  
- “基于组件的架构”（Component-Based Architecture, CBA）。  
- 依赖于组件（对象）工厂来创建并加载平台上的组件。  
- “PreInitialize”方法会自动加载组件。

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

9

![](images/150900710f6f631e9de1ecbb2ff3633652ff379ee4250d9d506183795fc09b71.jpg)

# UNCLASSIFIED

# 类型工厂

![](images/780e97138acba745d77ddabdeb1b81b2e8c344725a7788d4005a6e0b90cd1091.jpg)

- 大多数新组件类型将实现一个关联的组件工厂。
- 组件工厂将根据组件的类型创建新组件。  
- 四种主要的组件工厂类型：

1. 有名称/可编辑

示例：Processor（处理器）、Sensor（传感器）、Comm（通信）。

2. 无名称/可编辑

示例：Mover（移动器）。

3. 有名称 / 不可编辑  
- 允许使用，但可能不需要。  
4. 无名称/不可编辑

- 示例：Signature（特征）、Intersection Mesh（交叉网格）。

ComponentFactory 和 aScenario.RegisterComponentFactory 的实现用于上述某些类型的组件工厂。

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19.

Other requests for this document shall be referred to AFRL/RQQD.

- PreInitialize 方法由 WsfPlatform::Initialize 调用，在实际初始化平台上的组件之前执行。例如：为每个组件调用 Initialize 和 Initialize2 方法之前。

- PreInitialize 允许组件添加其他组件。  
- 如果某个组件需要被添加，但在输入流的任何地方都没有声明，则应通过 PreInitialize 插入该组件。  
- 一个组件可以检查组件列表并添加组件，但它不能假设组件的实际状态，因为：

- 组件尚未被初始化！

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQQD.

11

![](images/2641bf253ccdc38beb8d241e92f5d3da5611c833a9e9b7383b8122a65db7669a.jpg)

# UNCLASSIFIED

# 组件想定

![](images/f293be27761192ef6506a56c5ef8e9701f613cfb2e7b444deb0bbfef5e30ae33.jpg)

- 该场景由两个围绕地球运行的平台组成：

- 星舰企业号，携带“金压拉丁”（24世纪唯一剩下的货币）。  
- 费伦吉飞船（“费伦吉”是一个虚构的、道德存疑的商人种族）。

- 费伦吉飞船接近企业号并试图偷取拉丁。  
- 费伦吉执行了一个计划，其中包括：

1. 通过通信设备发起网络攻击：  
- 结果，企业号丢失了对费伦吉飞船的跟踪（无法再锁定目标）。  
2. 发起第二次网络攻击，迫使企业号“关闭”其护盾（屏障）。  
3. 一旦这些网络攻击成功完成，费伦吉便可以偷取拉丁。

- 企业号有一个新组件：护盾（Shields）

- 初始能量和功率恢复是输入参数。  
- 在本场景中，我们并未直接使用该功能来“削弱”护盾。  
- 将其定义为平台的一部分，可以关闭或关闭护盾。  
- 还有其他功能可用。  
- 请注意，护盾的定义是在平台定义之外完成的，并且在平台中仅通过类型定义（而不是在块中定义）。

- 这是因为我们将护盾组件工厂设置为“不可编辑”（Un-Editable）。  
- 企业号的定义中还包含对拉丁数量（latinum quantity）的定义。  
- 企业号和费伦吉飞船被放置在“标准轨道”上：  
- WSF_SPACE_MOVER 的功能可轻松将卫星放置在轨道上。  
- 指定纬度、经度、高度和航向即可将其放入圆形轨道。  
- 开始日期设置为 2369 年 7 月 27 日。

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQQD.

13

![](images/4a6ac7b94dbf493650aa4a42fd32e2fb9274039b22e5d4fb846c27166c44d0ef.jpg)

# 组件想定(继续)

![](images/a541ada1e2376443dec62a2129279678a2749a71948fb41d957e1e4367c77f8b.jpg)

- 企业号的传感器还具有一个输入，用于创建 track_drop 的网络效果（cyber Effect）。  
- 该输入会导致创建一个CyberSensorEffect实例，并将其添加到传感器中。  
- 企业号上的一个“不安全通信设备”（unsecure comm）接收来自费伦吉的指令以开始网络攻击：

1. 首先，发送指令激活传感器的网络效果以丢失跟踪（SimTime = 30秒）：

- 触发 CyberSensorEffect 中的效果。  
- 使目标锁定变得不可能。  
- 在Mystic中，红色的跟踪图标会消失以可视化此效果。

2. 然后，发送指令关闭护盾（SimTime = 40秒）：

- 该指令针对新的护盾组件（Shields component）。  
- 允许费伦吉“占有”拉丁。  
- 在Mystic中，会有一条绿色线条的可视化，表示拉丁的运输/转移过程。

强制传感器丢失跟踪的结果。

![](images/83e3fae42a80d249d2bb8f34c89eb275fab0a9bc8544a1330776539b5f438d90.jpg)

强制护盾关闭的结果。

![](images/d38c496039b83978da152372185338f3c9d9482efe7fe6e845cbc0813936ddcc.jpg)

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQQD.

# UNCLASSIFIED

![](images/84a0074abe405d03bcd0dcbc33281306f515c44f9a2565cdbe49c520634aee30.jpg)

# 组件办理入处理

![](images/53e32d3beb0ca874585011eedff0cd379ad90831f19dd912ff98f6a90c3584ac.jpg)

- 请注意，ProcessInput 方法会被调用于所有插入到平台上的组件，以及插入到传感器、通信设备和处理器上的组件扩展。

例如，拉丁组件（latinum component）的定义和插入方式如下：

```shell
platform_type Enterprise WSFPLATFORM
  icon space_shuttle
  side white
mover WSF_SPACE_MOVER
  position On 90w altitude 500 km heading 90 deg // "standard orbit"
  suppressWarnings enabled
end_mover 
```

latinumquantity500 //Definelatinumhere //onlyasingleinput,so not inablock

- 在此示例中，只有一个可能的输入：quantity（数量）。

- 它并未在一个 (latinum ... end_latinum) 块中定义。

然而，如果有多个输入，则应在一个块中定义。

这样可以使输入更容易解析。

![](images/14e9281d59f96432d40dba28f6a271d08dea29f0f79b5927e24313ff305bac24.jpg)

```txt
platform_type FERENGI_SHIP WSFPLATFORM
  icon ucraft_navy
  side green
  mover WSF_SPACE_MOVER
  end_mover
  endplatform_type
```c
platform Ferengi_Ship FERENGI_SHIP
edit mover
  position On 91w altitude 500 km heading 90 deg // "standard orbit"
  end_mover
add comm unsecured_comm WSFCOMM_TRANSEIVER
  end_comm
execute at_time 30 seconds absolute
  WsfComm c = PLATFORM.Comm("unsecured_comm");
  WsfMessage msg = {};
  msg.SetSubType("DROPTRACK");
  c.SendMessage(msg, "enterprise", "unsecured_comm");
end_execute
execute at_time 40 seconds absolute
  WsfComm c = PLATFORM.Comm("unsecured_comm");
  WsfMessage msg = {};
  msg.SetSubType("DROP_SHIELDS");
  c.SendMessage(msg, "enterprise", "unsecured_comm");
end_execute 
```

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

# UNCLASSIFIED

# 想定文件

add processor transport_latinum WsF-scriptPROCESSOR 创建处理器用来偷取latinumupdate_interval 0.1 son_update//check to see if the shields are downWsfPlatform enterprise $=$ WsFSimulation.FindPlatform("enterprise");Shields shields $=$ enterprise.Shields();检查企业号（Enterprise）的护盾是否已关闭。if(!shields.IsTurnedOn())//We can do this because of inheritance of shields from WsFPlatformPart{enterprise COMMENT("Shields Down");static bool beamLatinumNow $=$ true;WsfDraw draw $\equiv$ {；static double downTime $=$ TIME NOW;if(beamlatinumNow){writeIn("Enterprise shields down.);PLATFORM COMMENT(TIME NOW,Stealing Latinum);Latinum latinum $=$ enterprise.Latinum();latinum.TransformTo(PLATFORM);if(PLATFORM.Latinum().IsValid()）{writeIn("Latinum now on Ferengi Ship:"，PLATFORM.Latinum().Quantity());}beamLatinumNow $=$ false;if (TIME NOW < (downTime +10)){draw.Erase(1);：draw.End();如果护盾未关闭，则在两艘飞船之间绘制一条线。

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19.

Other requests for this document shall be referred to AFRL/RQQD.

![](images/c3f5f0904bc652618e38f9c67d6be564c89075be0bd81956912f8bece0765166.jpg)

以下代码片段定义了一些有用的标识符

$\dagger$ using WsfPlatformComponent = WsfComponentT<WsfPlatform>   
\* using WsfPlatformComponentList $\equiv$ WsfComponentListTWsfPlatormComponent>   
class WsfProcessorComponent : public WsfComponentT<WsfProcessor> ...   
$\ddagger$ using ComponentList = WsfComponentListT<WsfProcessorComponent>

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

21

![](images/ec923034ec060dd6371341695560d3449d9583d14cdb202f738ab7f8e6e73654.jpg)

# 通用组件层次结构

注意：这只是 AFSIM 组件的部分层次结构。

![](images/cb212a8b040a0ce7462c4354c724dbec0706707b9d3a82c0a33915f7b5a6994c.jpg)

![](images/9418460943d8f716e718d8329edfeebaf38f7c8157cf77b21e7ad018956630b9.jpg)  
以下代码片段定义了一些有用的标识符  
+ using WsfPlatformComponent = WsfComponent<T<WsfPlatform>   
* using WsfPlatformComponentList = WsfComponentListT<WsfPlatormComponent>   
class WsfProcessorComponent : public WsfComponentT<WsfProcessor> ...   
$\ddagger$ using ComponentList = WsfComponentListT<WsfProcessorComponent>   
$\spadesuit$ class WsfSensorComponent : public WsfComponentT<WsfSensor>   
$\mathbb{P}$ using ComponentList $\equiv$ WsfComponentListTWsfSensorComponent>

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19.

Other requests for this document shall be referred to AFRL/RQQD.

1. 打开 CMake GUI。  
2. 勾选BUILD_WITH_component exercis   
3. 勾选BUILD_WITH_wsf_space。  
4. 勾选BUILD_WITH.wsf_mil。  
5. 点击“Configure”（配置）。

- （如果出现提示要求选择编译器，请根据提示进行操作。）

6. 点击“Generate”（生成）。

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

UNCLASSIFIED

![](images/a7fee15b67b9bdbca828a66cf6f8ea40ba2f96ce40a83d8480ad7d1140faafc1.jpg)

# 开始 (2/3)

![](images/bb4a398ac6b1614a513013b241e03ca1ac6937ea12a073677fd4666bb810d5d9.jpg)

- 如果 Visual Studio 已经打开：

- 导航到 Visual Studio，并在提示时选择“Reload All”（重新加载所有）。

![](images/e1dd326186a52e362d681d76bd9eac27eac128c3aa12a7888fecf9a08adf3727.jpg)

- 或者，通过以下方式打开解决方案文件“afsim.sln”：

- 从“swdev\build”打开。  
- 从 CMake 中点击“Open Project”（打开项目）。

- 工程包含以下源文件:

- ComponentPluginRegistration.cpp   
- ComponentTypesRegistration.hpp   
- CyberSensorEffect.hpp   
- CyberSensorEffect.cpp   
- ShieldComponent.hpp   
- ShieldComponent.cpp   
ShieldTypes.hpp   
- ShieldTypes.cpp   
- LatinumComponent.hpp   
- LatinumComponent.cpp   
- ComponentRoles.hpp

![](images/4bd1bf778d18cb07b0056e13f13ac00b8071af9962de73f23ce2c0d8ba2ab42c.jpg)

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

UNCLASSIFIED

# 本练习所使用的类

25

![](images/3773d3ae897a0b06709d0cddf3f5fd93f4c7c55596ce874c32b65df25f532d5f.jpg)

![](images/d9129403b495dba110d5a81f53b13d7dd3d4365caf1ed569da9849f78db97162.jpg)

在文件ShieldComponent.hpp和ShieldComponent.cpp中：

- class ShieldComponent : public WsfPlatformPart

- 创建并注册一种新的平台部件类型，角色为cWSF_COMPONENT_SHIELDS。  
- 维护Strength（强度）、RechargeRate（充电速率）、UpdateInterval（更新间隔）等属性。

- class WsfScriptShieldComponentClass : public WsfScriptPlatformPartClass

定义一个名为Strength（强度）的脚本，用于场景输入文件脚本中。

在文件ShieldTypes.hpp和ShieldTypes.cpp中：

- class ShieldTypes : public WsfObjectTypeList<ShieldComponent>

- 将ShieldTypes的ShieldComponentFactory注册到场景中，以便平台可以拥有由shields...end_shields命令块创建的ShieldComponent类型的组件。

- class ShieldComponentFactory : public WsfComponentFactory<WsPlatform>

- 为ShieldTypes扩展WsfComponentFactory<WsPlatform>，并重写

ProcessAddorEditCommand 和 ProcessDeleteCommand 方法，以加载/删除作为平台组件的 ShieldComponent。

在文件 LatinumComponent.hpp 和 LatinumComponent.cpp 中：

- class LatinumComponent : public WsfPlatformComponent, ...

- 创建并注册一种新的平台组件，角色为cWSF_COMPONENT_LATINUM。

- class WsfScriptLatinumComponentClass : public UtScriptClass

定义一个名为Quantity（数量）的脚本（返回LatinumComponent的条数），用于场景输入文件。  
定义一个名为TransferTo（转移到）的脚本（将LatinumComponent转移给接收者，即Ferengi船），用于场景输入文件脚本。

- class LatinumComponentFactory : public WsfComponentFactory<WsPlatform>   
- 创建一个 LatinumComponent 对象，并实现 ProcessInput 方法以读取该对象的 latinum 命令。  
- class LatinumTypes : public WsfObjectTypeList<LatinumComponent>   
- 定义 LatinumComponents 的类型列表，并为 LatinumComponent 注册 LatinumComponentFactory 以处理 latinum 命令。

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

27

![](images/9c24caf46b44091eaf786991b68cd911c77ac1f58cc76e41a1d258aecdafd159.jpg)

# 本练习所使用的类

![](images/2ef66b7d873fe9abc9e42bbe9ff6addb5f99250d96db6a9eea7dfa03dc80f047.jpg)

在文件CyberSensorEffect.hpp和CyberSensorEffect.cpp中：

- class CyberSensorEffect : public WsfSensorComponent

- 创建一种新的传感器组件，角色为cWSF_COMPONENT_CYBER_SENSOR_EFFECT。  
- 实现了电子战（EW）组件，该组件附加到所有传感器系统上（将允许Ferenci干扰/击败企业号的传感器）。

- class CyberSensorComponentFactory : public WsfComponentFactory<WsfSensor>

- 创建一个CyberSensorEffectObject，并实现ProcessInput方法以读取该对象的cyber Effect...end_cyber-effect命令。

在文件 ComponentTypesRegistration.hpp 中:

- class ComponentTypesRegistration : public WsfScenarioExtension

- 该类作为场景扩展注册到场景中。  
- 重写 AddedToScenario 方法，注册新的 ShieldComponent 类型到场景中，并将 LatinumTypes 类型添加到场景中。

在文件 ComponentPluginRegistration.cpp 中:

- class RegisterShieldComponent : public WsfApplicationExtension

- 重写 AddedToApplication 方法，注册新的 ShieldComponent 脚本类型，注册 ShieldComponent 脚本方法，并注册 LatinumComponent 脚本方法。  
- 重写 ScenarioCreated 方法，注册新的 ShieldComponent 类型到场景中，并在任务/法术创建场景后将 LatiniumTypes 类型添加到场景中。  
- 通过 WsfPluginSetup 注册到 StandardApplication。

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

29

![](images/fde72f9b9ad8349d60e613b394c20ce97eb22d4255e0a8960514cd9368889a79.jpg)

# UNCLASSIFIED

# 组件练习

![](images/e3624d6f7743ca68a9084f1db084cb07c6e98e1e53acf65ea39895d3bd0a88cd.jpg)

·练习1

- 完成应用扩展、场景扩展和组件工厂的注册。  
- 了解其他组件工厂。

·练习2

- 理解并完成新的平台和传感器组件的实现。

·练习3

- 理解组件工厂类的 ProcessInput 方法。  
完成CyberSensorEffect的ProcessInput和TrackerAllowTracking方法。

·练习4

- 理解并完成脚本类的实现。

完成应用扩展的注册。  
- 完成场景扩展的注册。  
- 完成脚本方法的注册。  
- 完成 CyberSensorEffect 组件工厂的注册。  
- 了解其他组件工厂（如ShieldTypes和LatinumComponent）。

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

31

![](images/c543221b69d55aae12361837386adc9acb14db635fb5c08d9420fbab326c0849.jpg)

# AFSIM插件&扩展

![](images/177cfe6a6c4d828c76a24172e1d396c1ae6567f8db11825f5237e7cb4f51e0a1.jpg)

![](images/e7ce1731635baf45d3af1cacd63b646c1cd0314f545a01a3f1a3d9829ad213aa.jpg)

在mission/warlock中调用的主程序类

所有AFSIM扩展必须继承自WsfExtension:

- 已经存在三个预定义的扩展类（可以继承）：

- WsfScenarioExtension - 提供新场景命令的扩展（需要为这些命令实现新的ProcessInput）需要继承此类。  
- WsfSimulationExtension - 访问仿真的扩展需要继承此类。  
- WsfApplicationExtension - 创建新脚本类型或利用仿真扩展或场景扩展的扩展需要继承此类。

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19.

Other requests for this document shall be referred to AFRL/RQQD.

![](images/1062c43b886596c9a08266d09576e44658b3c18cd7f64f3c2d391c8058ea72f4.jpg)

所有AFSIM扩展必须继承自WsfExtension:

- 已经存在三个预定义的扩展类（可以继承）：

- WsfScenarioExtension - 提供新场景命令的扩展（需要为这些命令实现新的ProcessInput）需要继承此类。  
- WsfSimulationExtension - 访问仿真的扩展需要继承此类。  
- WsfApplicationExtension - 创建新脚本类型或利用仿真扩展或场景扩展的扩展需要继承此类。

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

33

![](images/9a0a934f24473abddf4a3775c2a83670fea3cec66d68637095cf611c5607429c.jpg)

UNCLASSIFIED

# 扩展

![](images/b6d568bb8fabb7f219b7d61f73990a45df68242bb1e47eb956ea6bc13f20c6ae.jpg)

应用程序、场景和仿真都可以被“扩展”。

- 应用扩展由应用程序拥有，代表可以添加到应用程序的可选功能。

- 当需要新的脚本类型（传感器、武器、组件、移动器）时使用。  
- 这是在AFSIM中注册所有扩展的入口点。  
- 如果要创建场景扩展或仿真扩展，则需要应用扩展。

- 如果我们正在创建新脚本、需要注册新插件，或者因为创建新类型而需要新插件，我们也需要应用扩展。

- 在这里，我们需要通过应用扩展注册插件（请参见文件 RegisterShieldComponent 在 ComponentPluginRegistration.cpp 中）。

在文件 ComponentPluginRegistration.cpp 中:

- 审查并理解插件是如何设置的。

- 查看 WsfPluginSetup，注意调用 RegisterExtension 来注册 WsfApplicationExtension（我们的 RegisterShieldComponent 类）。  
- 查看 WsfPluginVersion，注意调用 UtPluginVersion。

- 这与武器和移动器练习中的代码相同。

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQQD.

35

![](images/ada52faf24225558f47d4706887673ecbe7aebc86b07eb9dcadf5d42a5a6840a.jpg)

# 组件练习 1 — 检视 1

# ComponentPluginRegistration.cpp

![](images/93f0bca865384faa530898f122bc7902a7859d0bc87248426f3d6af428c4695e.jpg)

```cpp
extern "C"
{
COMPONENT_EXERCISE exports void WsfPluginVersion(UtPluginVersion& aVersion)
{
aVersion = UtsPluginVersion(WSF Plugin_APIMajor_VERSION,
WSF Plugin_APIMinor_VERSION,
WSF Plugin_API_COMPILER_STRING);
}
COMPONENT_EXERCISE exports void WsfPluginSetup(WsfApplication& aApplication)
{
aApplication.RegisterExtension("register_shield_component",
ut::make_unique<RegisterShieldComponent>());
}
} 
```

# - 要扩展应用程序，您必须创建一个继承自 WsfApplicationExtension 的类

# class myAppExtension: public WsfApplicationExtension { ... }

- 您应该重写以下成员：

- AddedToApplication: 接收扩展被添加到应用程序的通知，通常用于注册额外的脚本类和方法等.  
- ScenarioCreated: 在场景构造函数结束时调用，以接收来自应用程序的场景创建通知，如果需要，可以用于注册场景扩展  
- SimulationCreated: 在仿真的初始化方法中调用，以接收来自应用程序的仿真创建通知，如果需要，可以用于注册仿真扩展  
- ProcessCommandLine: 从 WsfApplication::ProcessCommandLine 方法调用，以检查当前参数并在必要时处理它  
- PrintGrammar: 打印扩展识别的扩展语法  
- ProcessCommandLineCommands: 由 WsfApplication 的 ProcessCommandLineCommands 调用，以允许扩展处理/处理其需要识别的任何命令

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

37

![](images/f5d261125fddef6cb23bdb4474f1b0df91333a16d6f84f4ea7f8ef6ab83cac8d.jpg)

# 应用扩展

![](images/07cce233b045dd3847eca325ad9e0956646c1694def94ad5f1440ef854e39b88.jpg)

- 我们将创建一个名为 RegisterShieldComponent 的应用扩展，该扩展将注册一些新的脚本

# class RegisterShieldComponent: public WsfApplicationExtension { ... }

- 该类将重写以下成员:

- AddedToApplication: 接收扩展被添加到应用程序的通知，通常用于注册额外的脚本类和方法等.  
- ScenarioCreated: 在场景构造函数结束时调用，以接收来自应用程序的场景创建通知，如果需要，可以用于注册场景扩展。

注意：这次，您需要完成 AddedToApplication 方法和 ScenarioCreated 方法

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

- 应用程序的 RegisterExtension 方法调用

WsfApplicationExtension::AddedToApplication 方法，该方法会调用应用扩展的 AddedToApplication 方法。

- 在文件 ComponentPluginRegistration.cpp 中，完成方法

RegisterShieldComponent::AddedToApplication。

- 任务1a：调用ShieldComponent::RegisterScriptTypes方法以注册盾组件的脚本类型

- RegisterScriptTypes 的格式为:

```txt
static void RegisterScriptTypes(UtScriptTypes&); 
```

- 输入参数应为通过调用 aApplication.getScriptTypes() 方法返回的指针的解引用

- 任务1b：调用ShieldComponent::RegisterScriptMethods方法以注册盾组件的脚本方法

- RegisterScriptMethods 的格式为:

```txt
static void RegisterScriptMethods(UtScriptTypes&); 
```

- 输入参数应为通过调用 aApplication.getScriptTypes() 方法返回的指针的解引用

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19.

Other requests for this document shall be referred to AFRL/RQQD.

39

![](images/50ed8d90403bace40c42a5a3160c6144c5f90c3755689eef5324567b56a2a7c3.jpg)

# 组件练习1—任务1解决方案

# ComponentPluginRegistration.cpp

![](images/11e17a63a7a15731e2120427fb5519d25313cbbf2dc5d076ca29dc950b4aa323.jpg)

class RegisterShieldComponent : public WsfApplicationExtension

public: RegisterShieldComponent() $=$ default; void AddedToApplication(WsfApplication& aApplication) override { //EXERCISE1TASK1a //Use the application object to register the shield component's script type(s) ShieldComponent::RegisterScriptTypes(\*aApplication.GetScriptTypes()); //EXERCISE1TASK1b //Use the application object to register the "Shields"accessor that extends the WsfPlatform script type. ShieldComponent::RegisterScriptMethods(\*aApplication.GetScriptTypes()); //Use the application object to register the latinum component's script type(s) LatinumComponent::RegisterScriptTypes(\*aApplication.GetScriptTypes()); //Use the application object to register the "Latinum"accessor that extends WsfPlatform LatinumComponent::RegisterScriptMethods(\*aApplication.GetScriptTypes()); } 1

请注意，AddedToApplication还会调用RegisterScriptTypes和RegisterScriptMethods来处理LatinumComponent。

在文件 ComponentPluginRegistration.cpp 中，为应用扩展实现 RegisterShieldComponent::ScenarioCreated 方法。

- 使用场景对象的 RegisterExtension 方法来注册我们的新场景扩展（ComponentTypesRegistration）。  
- RegisterExtension 的格式为:  
    void RegisterExtension(const std::string&, std::unique_ptr<WsfScenarioExtension>();   
- 第一个参数是扩展的名称，即“shield_types”。  
- 第二个参数是扩展的类型，即场景扩展。  
- 第二个参数应为使用 ut::make_unique<ComponentTypesRegistration>() 创建的 unique_ptr。

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

41

![](images/14bbf93343ba44a4e1adbd283e0badd341a042f98b648a4c2ca5e57bd97c1831.jpg)

# 组件练习1—任务2解决方案

# ComponentPluginRegistration.cpp

![](images/98dd193e957cb84a989e18d48a2ce2c3f6050fe713b95d8a992f82eb96af1449.jpg)

```cpp
class RegisterShieldComponent : public WsfApplicationExtension   
{ public: void ScenarioCreated(WsfScenario& aScenario) override { // EXERCISE 1 TASK 2 // Register the scenario extension that allows us to reference the new type lists. // Use the scenario object to register an extension called "shield_types", // of type ComponentTypesRegistration(). aScenario.RegisterExtension("shield_types", ut::make_unique<ComponentTypesRegistration>(); // EXERCISE 1 TASK 3 // Call the CyberSensorEffect's static method RegisterComponentFactory. } }; 
```

在文件 ComponentPluginRegistration.cpp 中，完成应用扩展的 RegisterShieldComponent::ScenarioCreated 方法。

- 调用 CyberSensorEffect 的方法 RegisterComponentFactory。  
- RegisterComponentFactory 的格式为: static void RegisterComponentFactory(WsfScenario&);  
- 将 aScenario 对象作为参数传入。这将把 CyberSensorEffect 的 CyberSensorComponentFactory 类注册到场景中。

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

43

![](images/859478db1c8ae1b84d9f73303779437674a21e1c5df816be4204043859ef6197.jpg)

# UNCLASSIFIED 组件练习1—任务3解决方案

# ComponentPluginRegistration.cpp

![](images/b2dcc19a300d2bdb093387ee01396d13ea01fc3db6bf6553c76db25b3b9a7d11.jpg)

```cpp
class RegisterShieldComponent : public WsfApplicationExtension   
{ public: void ScenarioCreated(WsfScenario& aScenario) override { // EXERCISE 1 TASK 2 // Register the scenario extension that allows us to reference the new type lists. // Use the scenario object to register an extension called "shield_types", // of type ComponentTypesRegistration(). aScenario.RegisterExtension("shield_types", ut::make_unique<ComponentTypesRegistration>(); // EXERCISE 1 TASK 3 // Call the CyberSensorEffect's static method RegisterComponentFactory. CyberSensorEffect::RegisterComponentFactory(aScenario); } }; 
```

# - 检查 CyberSensorEffect 类。

# - 注意 RegisterComponentFactory 的实现。

```cpp
//! The Ew component that will be attached to all sensor systems.   
class CyberSensorEffect : public WsfSensorComponent   
public:   
enum Type   
{ cUNDEFINED, cTRACK_PULLOFF, cTRACK DROP };   
static void RegisterComponentFactory(WsfScenario& aScenario); static CyberSensorEffect* Find(const WsfSensor& aSensor); static CyberSensorEffect* FindOrCreate(WsfSensor& aSensor); CyberSensorEffect(); CyberSensorEffect(const CyberSensorEffect& aSrc); CyberSensorEffect& operator=(const CyberSensorEffect& aSrc); ~CyberSensorEffect() noexcept override = default;   
}； 
```

```txt
//! Register the component factory that handles input for this component.  
void CyberSensorEffect::RegisterComponentFactory( WsfScenario& aScenario)  
{  
    aScenario.RegisterComponentFactory(ut::make_unique<CyberSensorComponentFactory>();  
}  
DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19.  
Other requests for this document shall be referred to AFRL/RQQD. 
```

45

![](images/e8b50ed7c60ce51b45b6ff604a1247172dc960ef75b109526a5cf28694c9b626.jpg)

# UNCLASSIFIED

# 组件练习1-检视3

# CyberSensorEffect.cpp

![](images/8c0460724aac3f50d821dd22a02e24469fa07e7891fe37370cd96947b47923b2.jpg)

# 检查CyberSensorEffect.cpp中的CyberSensorComponentFactory。

- 注意 ProcessInput 的实现。

- 该方法处理 cyber Effect 传感器命令，并查找现有的 Cyber SensorEffect 对象；如果必要，它会创建一个新的对象，以实现该组件并处理其命令。

classCyberSensorComponentFactory:public WsfComponentFactory<WsfSensor>   
public: boolProcessAddOrEditCommand(UtInput&aInput,WsfSensor&aParent，boolaIsAdding)override { //Noaddoredit commands to process return false;   
}   
boolProcessInput(UtInput&aInput，WsfSensor&aParent）override std::stringcommand; aInput.GetCommand command); boolmyCommand $=$ false; if command $\equiv$ "cyber-effect") { CyberSensorEffect\*cbePtr $\equiv$ CyberSensorEffect::FindOrCreate(aParent); 1 } return myCommand;

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19.

Other requests for this document shall be referred to AFRL/RQQD.

- 场景也可以被“扩展”。

- 场景扩展由场景拥有，代表可以添加到场景中的可选类型。  
- 如果您需要新的类型（组件、观察者、通信），则会使用场景扩展。  
- 如果您要创建场景扩展（或稍后讨论的仿真扩展），则需要应用扩展。  
- 如果我们正在创建全局级别的 ProcessInput 方法（针对我们的类型），我们也需要场景扩展。

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

47

![](images/ce3ffa7388354eb9ba8a0f85ed35a1d87f2e91a2a5ec4e9c9044ba9dd2f625e6.jpg)

UNCLASSIFIED

# 想定扩展

![](images/03b54dfee12eadc08b9a281828c5424fb6e21ae4e52a3c5bc98cf5189fb72e6c.jpg)

- 要扩展一个场景，您必须创建一个继承自 WsfScenarioExtension 类的类

class myScenarioExtension: public WsfScenarioExtension

- 您必须重写以下方法:

- AddedToScenario：接收扩展被添加到场景的通知，通常用于注册额外的组件类型对象和工厂  
- ProcessInput: 处理必须被扩展识别的任何场景输入命令  
- FileLoaded: 通知扩展文件已被加载到场景中  
- Complete: 从 WsfScenario::LoadComplete 调用，通知扩展所有场景输入已被处理  
- Complete2: 在所有扩展的 Complete 方法被调用后调用  
- SimulationCreated: 从 WsfSimulation::Initialize 调用，如果场景扩展需要一个关联的仿真扩展，这个方法可以注册仿真扩展  
AlwaysCreate: 确定扩展是可选的还是必需的