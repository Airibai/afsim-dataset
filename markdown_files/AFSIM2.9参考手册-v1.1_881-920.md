# 噪声参考值

恒定加速度模型  

<table><tr><td>平台类别</td><td>Sigma X</td><td>Sigma Y</td><td>Sigma Z</td></tr><tr><td>高机动性飞机</td><td>50.0</td><td>10.0</td><td>50.0</td></tr><tr><td>卡车/汽车</td><td>2.0</td><td>2.0</td><td>2.0</td></tr><tr><td>海军舰艇</td><td>1.0</td><td>2.0</td><td>2.0</td></tr></table>

恒定速度模型  

<table><tr><td>平台类别</td><td>Sigma X</td><td>Sigma Y</td><td>Sigma Z</td></tr><tr><td>高机动性飞机</td><td>2.0</td><td>2.0</td><td>2.0</td></tr><tr><td>卡车/汽车</td><td>0.1</td><td>0.2</td><td>0.2</td></tr><tr><td>海军舰艇</td><td>0.4</td><td>0.4</td><td>2.0</td></tr></table>

# 4.5.4.4. 2D 卡尔曼滤波器 WSF_KALMAN_FILTER_2D_RB

```txt
filter <name> WSF_KALMAN_FILTER_2D_RB ... Commands ... end_filter 
```

定义了一种用于滤波轨迹的卡尔曼滤波器。该滤波器将测量的距离和方位数据转换为X-Y 位置。这个卡尔曼滤波器专门用于处理二维空间中的目标跟踪。它通过将测量的距离和方位数据转换为 X-Y 坐标来估计目标的位置。

<table><tr><td>命令</td><td>debug</td></tr><tr><td>解释</td><td>将调试信息写入标准输出。</td></tr><tr><td>命令</td><td>range mesurement_sigma &lt;距离值&gt;</td></tr><tr><td>解释</td><td>定义在滤波前应用于测量范围的标准差。</td></tr><tr><td>命令</td><td>bearing mesurement_sigma &lt;角度值&gt;</td></tr><tr><td>解释</td><td>定义在滤波前应用于测量方位的标准差。</td></tr><tr><td>命令</td><td>process noise sigmas_XY &lt;X值&gt;&lt;Y值&gt;</td></tr><tr><td>解释</td><td>定义滤波器在两个方向上的噪声标准差。值必须以米为单位输入。</td></tr></table>

# 4.5.4.5. 轨迹确认滤波器 WSF_ORBIT_DETERMINATION_FILTER

```txt
filter <name> WSF_ORBIT_DETERMINATION_FILTER ... Commands ... end_filter 
```

WSF_ORBIT_DETERMINATION_FILTER 实现了一个无迹卡尔曼滤波器（UKF）用于轨道确定和跟踪。与卡尔曼滤波器类似，WSF_ORBIT_DETERMINATION_FILTER 接受输入位置（来自距离、方位角、仰角或位置测量），并生成被跟踪目标的位置和速度估计，以及状态和协方差。不同于 WSF_KALMAN_FILTER，WSF_ORBIT_DETERMINATION_FILTER 生成适用于轨道运动的状态和协方差估计。根据滤波器是否稳定（通常在接收到三个测量值后），它以不同的方式提供这些估计。在稳定之前，滤波器依赖于线性外推（在过滤器定义中显式添加时使用）

或过滤状态的显式轨道传播（在轨道确定融合中内部使用）。一旦滤波器稳定，状态和协方差预测通过使用轨道传播器的非线性（无迹）变换计算。

注意：此过滤器由轨道确定跟踪融合方法使用。在 track_manager 定义中不要将此过滤器与轨道确定融合方法结合使用。

<table><tr><td>命令</td><td>process_noise_sigmas_XYZ&lt;X值&gt;&lt;Y值&gt;&lt;Z值&gt;</td></tr><tr><td>解释</td><td>定义过滤器在三个方向上的噪声标准差。这些值对应于被跟踪平台的实体坐标系(ECS)中的加速度。默认值:000</td></tr><tr><td>命令</td><td>propagator&lt;propagator-type&gt;propagator Commands ... end_propagator</td></tr><tr><td>解释</td><td>指定用于跟踪目标的传播器类型。默认值:如果跟踪中有真实目标类型,则使用被跟踪目标的传播器类型;否则,使用WSF_kePLERIAN_propAGATOR。注意:传播器的初始状态将使用提供的跟踪更新;任何提供的传播器初始状态配置(初始轨道元素或轨道状态)将被忽略。</td></tr><tr><td>命令</td><td>range mesure_sigma&lt;长度值&gt;</td></tr><tr><td>解释</td><td>定义在过滤之前应用于测量范围的标准差。注意:通常不需要此输入。仅在相关跟踪中没有范围误差时使用。默认值:0米</td></tr><tr><td>命令</td><td>bearing mesure_sigma&lt;长度值&gt;</td></tr><tr><td>解释</td><td>定义在过滤之前应用于测量方位角的标准差。注意:通常不需要此输入。仅在相关跟踪中没有方位误差时使用。默认值:0度</td></tr><tr><td>命令</td><td>elevation mesure_sigma&lt;长度值&gt;</td></tr><tr><td>解释</td><td>定义在过滤之前应用于测量仰角的标准差。注意:通常不需要此输入。仅在相关跟踪中没有仰角误差时使用。默认值:0度</td></tr><tr><td>命令</td><td>debug</td></tr><tr><td>解释</td><td>当指定时,将过滤后的测量数据和过滤器性能数据写入文件KFILT_DEBUG.out。</td></tr></table>

# 4.5.5. 跟踪器 track

track

```txt
position ...  
mgrs Coordinate ...  
altitude ...  
range ...  
bearing ...  
elevation ...  
speed ...  
heading ...  
type ...  
side ...  
spatial_domain ...  
frequency ...  
platform ...  
aux_data... end(aux_data  
end_track 
```

track 块中定义的目标会一直被跟踪，无论传感器有没有探测到，相当于定义了个初始

跟踪物体，只要没有明确停止跟踪，则会一直跟踪和更新其信息。可以定义多个 track。

track 块是 platform 或 track_manager 的一个子命令，用于定义对另一个对象的初始跟踪（或感知）。在给定的平台中，可以指定多个 track 块。命令应该只针对那些被认为已知的属性进行指定，所有其他属性应省略。

如果没有使用 position、mgrs_coordinate、range 或 bearing 明确指定跟踪位置，则如果提供了目标平台的真实位置，将使用该位置来初始填充跟踪中的位置数据。

注意：position 和 mgrs_coordinate 命令与 range 和 bearing 命令互斥。

<table><tr><td>命令</td><td>position</td></tr><tr><td>解释</td><td>对象的感知位置。</td></tr><tr><td>命令</td><td>mgrs Coordinate</td></tr><tr><td>解释</td><td>对象在军事网格参考系统中的感知坐标。</td></tr><tr><td>命令</td><td>altitude [ agl | msl ]</td></tr><tr><td>解释</td><td>对象的感知高度。agl（地面以上）和 msl（平均海平面以上）指定高度的基准。如果省略基准规格，则假定为 msl。</td></tr><tr><td>命令</td><td>range</td></tr><tr><td>解释</td><td>从跟踪平台的初始位置到对象的感知距离。</td></tr><tr><td>命令</td><td>bearing</td></tr><tr><td>解释</td><td>从跟踪平台的初始位置到对象的感知方位角。</td></tr><tr><td>命令</td><td>elevation</td></tr><tr><td>解释</td><td>从跟踪平台的初始位置到对象的感知仰角。</td></tr><tr><td>命令</td><td>speed</td></tr><tr><td>解释</td><td>对象的感知速度。</td></tr><tr><td>命令</td><td>heading</td></tr><tr><td>解释</td><td>对象的感知航向。</td></tr><tr><td>命令</td><td>type</td></tr><tr><td>解释</td><td>对象的感知类型。</td></tr><tr><td>命令</td><td>side</td></tr><tr><td>解释</td><td>对象的感知方（“团队”或“隶属关系”）。</td></tr><tr><td>命令</td><td>spatial_domain [ land | air | surface | subsurface | space ]</td></tr><tr><td>解释</td><td>定义对象的感知空间域。</td></tr><tr><td>命令</td><td>frequency</td></tr><tr><td>解释</td><td>对象的感知频率。</td></tr><tr><td>命令</td><td>platform</td></tr><tr><td>解释</td><td>如果没有指定位置，用于初始填充跟踪中位置数据的平台。平台必须在 track 之前定义。</td></tr></table>

# 4.6. 辅助数据 aux_data

aux_data 提供了一种机制，可以将特定于应用程序的数据附加到轨迹、平台、通信、传感器、发射器和接收器对象上。这些数据可以通过脚本方法或特定于应用程序的代码进行操作。

简单属性

简单属性类型包括 bool、int、double 和 string，它们与 C语言代码中的等价类型相对应。unitary 类型允许用户使用单位指定一个双精度值。以下是仅包含简单数据类型的 aux_data

定义示例：

```python
aux_data bool IS_DETECTED = false string FAC_RESPONSE = "FLY-route" 
```

```txt
end(aux_data 
```

初始值可以如上例所示提供。如果省略初始值，它们将被分配默认值如下：

```yaml
bool: false  
int: 0  
double: 0.0  
string: "" 
```

单位类型

单位类型表示具有 WSF 标准单位的变量。为了在 aux_data 块中提供单位声明，必须提供单位类型以及初始值。以下是单位声明的示例：

```txt
unitary TIME debunkED = 1.0 seconds 
```

将此声明包含在上面的示例中，结果如下：

aux_data bool IS_DETECTED = false unitary TIME_DETECTED $= 1.0$ seconds string FAC_RESPONSE $\equiv$ "FLY_ROUTER   
end_aux_data

结构

结构用于将相关变量分组在一起，这些变量在 aux_data 中使用 struct 关键字定义；例如：

```txt
struct TARGET_INFO_TYPE
    string NATIONALITY = "USA"
    int TAIL_NUMBER = 4321
    string ENGINE_TYPE = "GE-111"
end_struct 
```

注意：这些结构旨在以一种不显眼的方式为场景提供附加数据，可以从代码库中访问/修改，特别是在使用外部插件和扩展时。这些结构与 script_struct 本质上不同，因此 script_struct不能在 aux_data 中使用。

在 aux_data 中声明的结构在脚本中不可访问，但结构成员可能是可访问的，例如：

aux_data struct example int $x = 3$ end_struct   
end(aux_data

```txt
execute at_time 1 sec absolute  
int y = PLATFORM.AuxDataInt("x");  
writeIn(y); // 输出为 "3"  
end_execute 
```

注意：结构可以嵌套在其他结构中，但这些嵌套结构的成员不能在脚本中访问。

这些用户定义的结构与简单属性一起放置在 aux_data 定义中，如下所示：

aux_data bool IS_DETECTED = false unitary TIME_DETECTED $= 1.0$ seconds string FAC_RESPONSE $\equiv$ "FLY_ROUTER TARGET_INFO_TYPE TARGET_INFO end(aux_data

注册类型

注册类型（以前称为复杂类型）是代码中已定义的类和结构。必须在代码中使用 ${ \mathsf { C } } { \mathsf { + } } { \mathsf { + } }$ 语句UtAttributeBase::RegisterPrototype 注册一个注册类型，然后才能在 aux_data 定义中使用。例如，为了在 aux_data 声明中使用 WSF ${ \mathsf { C } } { + } { + }$ 类 WsfCategoryList 作为注册类型，必须首先在代码中注册此类型，如下所示：

```cpp
// 选项1:  
UtAttributeBase::RegisterPrototype("WSF_CATEGORY_LIST", ut::make_unique<UtAttribute<WsfCategoryList>>(); 
```

```cpp
// 选项2:  
UtAttribute<WsfCategoryList>::RegisterPrototype("WSF_CATEGORY_LIST");  
将此类型的属性添加到上述aux_data声明中，结果如下：
```

aux_data bool IS_DETECTED = false unitary TIME_DETECTED $= 1.0$ seconds string FAC_RESPONSE $\equiv$ "FLY_ROUTER TARGET_INFO_TYPE TARGET_INFO WSF_CATEGORY_LIST SENSOR_CATEGORY   
end(aux_data

注意：注册类型没有初始值。对象的构造函数将执行必要的初始化。

# 4.7. 指挥链 Command Chains

指挥链用于决策制定程序，以确定可以向谁发布命令以及报告应发送到哪里。指挥链通过在各个平台上使用 commander 和 command_chain 命令构建。

指挥链由指挥官、下属和同级组成。每个指挥链必须至少有一个指挥官（即使该指挥官是你自己）。通过使用这些输入构建指挥官层次结构，可以创建一个复杂的多层次层级。

通信设备使用指挥链将消息发送给接收者。在指挥官的情况下，这是一个单一的接收者；而在同级和下属的情况下，可能有零个、一个或多个接收者。

注意：一个平台可以是多个指挥链的成员，但在每个指挥链中只能是一次成员。

示例

在此示例中，有两个指挥链：ATC 和 AIRLINERS。在 AIRLINERS 指挥链中，737-1、737-2和 737-3 向 737-cmd-1 报告，737-cmd-1 向 joint-cmdr 报告。此外，737-3 具有双重角色，并在 ATC 指挥链中直接向 joint-cmdr 报告。

```txt
platform joint-cmdr COMMAND_POST command_chain ATC SELF command_chain AIRLINERS SELF 
```

```txt
endplatform   
platform737-cmd-1COMMAND_POST command_chainAIRLINERS joint-cmdr   
endplatform   
platform737-1F-18 command_chainAIRLINERS 737-cmd-1   
endplatform   
platform737-2F-18 command_chainAIRLINERS 737-cmd-1   
endplatform   
platform737-3F-18 command_chainAIRLINERS 737-cmd-1 command_chainATC joint-cmdr   
endplatform 
```

# 默认指挥链

默认指挥链可以通过使用 commander 命令、使用命令链名称为“default”的command_chain 命令或隐式构建来构建。在显式构建默认指挥链的情况下，其行为与其他显式构建的指挥链相同。

隐式构建的默认指挥链发生在指定了显式指挥链但未指定默认指挥链的情况下。如果一个平台恰好是一个命名（非默认）指挥链的成员，则该平台将在默认指挥链上具有相同的指挥官。如果一个平台是多个命名指挥链的成员，则默认指挥链上的指挥官将是其中一个命名指挥链的指挥官。选择哪个指挥官不保证，因此不建议在多个命名指挥链的情况下使用隐式构建的指挥链。

注意：建议在场景中包含多个指挥链时使用命名指挥链，而不是隐式构建的默认指挥链。已弃用：自版本 2.9 起，使用隐式构建的默认指挥链已被弃用，并将在未来版本中不再支持，因为当存在多个命名指挥链时，这种行为会导致歧义。

# 4.8. 交通模型

# 4.8.1. 路由 route

```txt
route  
#Commands  
navigation  
#Navigation Commands  
label...  
position...  
mgrs_coordinates...  
offset...  
turn_left...  
turn_right... 
```

```tcl
turn_to Heading ...   
goto ...   
#Waypoint Commands   
altitude ...   
depth ...   
heading ...   
turn ...   
speed ...   
linear acceleraion ...   
radial acceleraion ...   
bank_angle_limit ...   
turn_g_limit ...   
climb_rate ...   
dive_rate ...   
pause_time ...   
execute ...   
extrapolate ...   
stop ...   
remove ...   
switch_on_passing ...   
switch_onapproach ...   
distance ...   
time ...   
time_to_point...   
node_id...   
aux_data...end(aux_data   
endjahication   
#Auxiliary Data Commands   
aux_data...end(aux_data   
#Route Insertion Commands.   
transform-route...   
transform absolute-route...   
endroute 
```

# Define a route on a platform.

platform ...

route

...

end_route

end_platform

```perl
Define a route type that can be referenced by the use-route command of the platform or route_network   
# commands, or by transformRoute or transform absoluteRoute commands. #   
These occur outside platform definitions.   
route <name> end-route 
```

路线是定义移动器（例如：WSF_AIR_MOVER、WSF_GROUND_MOVER、WSF_ROAD_MOVER和 WSF_SURFACE_MOVER）路径或在路线网络中定义路线部分的航路点集合。

航路点的开始由以下命令之一指示：

□ 特定的纬度和经度（position）  
▫ 相对于当前位置的偏移（offset）  
□ 转向命令（turn_left、turn_right 或 turn_to_heading）  
□ ‘goto’ 命令（goto）到另一个标记的航路点

航路点的定义将持续到下一个开始新航路点的命令。

注意：参数如速度、高度、爬升率、径向加速度、线性加速度等用于所有后续航路点，直到被覆盖。

命令

导航命令

navigation <navigation-commands> … end_navigation

定义用于输入路线航路点和其他导航数据的导航命令块。

辅助数据

aux_data <aux-data> … end_aux_data

定义路线的辅助数据。有关更多命令和信息，请参见 aux_data。

导航命令

label <string>

将字符串标签与紧随其后的航路点定义关联。这可以用作 goto 命令的目标。

注意：此命令应紧随导航命令之后，因为它附加到下一个航路点。

position <latitude-value> <longitude-value>

指定航路点的纬度和经度。

mgrs_coordinate <MGRS-value>

指定航路点在军事网格参考系统中的坐标。

offset <x-offset> <y-offset> <length-units>

转到相对于平台当前位置的点。每个偏移航路点相对于前一个航路点的位置（如果是第一个航路点，则相对于平台的位置），并使用第一个偏移航路点的航向设置方向，并在所有后续偏移航路点中保持不变。 $+ { \sf X }$ 轴在初始航向方向上， $+ \mathsf { Y }$ 轴在初始航向右侧 90 度。

![](images/ea1c974be9caff37ac61c581498464df4db3d739e9b2465ff617a5f371cc897e.jpg)

<table><tr><td>Step</td><td>+X</td><td>+Y</td><td>Cumulative Change (X, Y)</td></tr><tr><td>Starting Location</td><td></td><td></td><td>(0,0)</td></tr><tr><td>1</td><td>2</td><td>0</td><td>(2,0)</td></tr><tr><td>2</td><td>2</td><td>0</td><td>(4,0)</td></tr><tr><td>3</td><td>0</td><td>3</td><td>(4,3)</td></tr><tr><td>4</td><td>-3</td><td>-1</td><td>(1,2)</td></tr><tr><td>5</td><td>-3</td><td>2</td><td>(-2, 4)</td></tr><tr><td>6</td><td>5</td><td>2</td><td>(3,6)</td></tr></table>

turn_left <angle-value> / turn_right <angle-value>

发起转弯以实现指定的航向角度变化。

turn_to_heading <angle-value>

发起转弯到指定的绝对航向角度。转弯方向将是需要最少航向角度变化的方向。

goto <string>

当到达此航路点时，转到当前路线中具有指定标签的航路点。

注意：此命令应跟随导航命令，因为它附加到前一个航路点。

航路点命令用于定义移动器在路径上的行为和状态。以下是可用的命令及其解释：

altitude <length-value> [ agl | msl ]

指定航路点的高度。如果省略 agl 或 msl，则默认高度参考由移动器定义。对于WSF_AIR_MOVER，假定为 MSL（平均海平面高度），对于其他所有移动器，假定为 AGL（地面以上高度）.

depth <length-value>

指定航路点的水下深度。

heading <angle-value>

指定航路点的航向。这在只有一个航路点的路径中才有效。如果给出了多个航路点，则航向将自动确定。

turn [ left | right | shortest ]

指定如果需要转弯时的转向方向。

默认值：shortest

speed <speed-value>

指定航路点的速度。

linear_acceleration <acceleration-value>

指定用于改变从此航路点开始的路径段速度的线性加速度。<acceleration-value> 也可以是默认值，以使用移动器的默认线性加速度。

默认值：移动器的默认线性加速度。

radial_acceleration <acceleration-value>

指定用于在从此航路点开始的路径段上进行航向变化时的转弯径向加速度。<acceleration-value> 也可以是默认值，以使用移动器的默认径向加速度。

默认值：移动器的默认径向加速度。

注意：径向加速度不是飞机的载荷因子。例如，如果希望最大载荷因子为 ${ \mathsf n } = 2$ 的 $2 { \tt g }$ 转

弯，则所需的 2g 转弯限制的径向加速度需要设置为 $\mathrm { g } ^ { \ast } \mathsf { s q r t } ( \mathsf { n } ^ { \wedge } 2 - 1 ) = 1 . 7 3 2 \mathrm { g } ^ { }$

bank_angle_limit <angle-value>

指定用于在从此航路点开始的路径段上进行航向变化时的最大倾斜角。这实际上将径向加速度设置为 ${ \pmb { \xi } } ^ { * }$ tan(bank_angle_limit)。

turn_g_limit <acceleration-value>

指定用于在从此航路点开始的路径段上进行航向变化时的最大转弯 g 载荷。这实际上将径向加速度设置为 sqrt(turn_g_limit^2 - g^2)。

climb_rate <speed-value> / dive_rate <speed-value>

指定用于改变从此航路点开始的路径段高度的爬升或俯冲速度。<speed-value> 也可以是默认值，以使用移动器的默认爬升率。

默认值：移动器的默认爬升/俯冲率。

maximum_flight_path_angle <angle-value>

指定在此航路点之后发生的爬升和俯冲的最大飞行路径角。如果指定为默认值，移动器将使用其默认值。

pause_time <time-value>

当到达航路点时，停止移动指定的时间。

execute <script-name> <callback-name>

指定在到达航路点时要执行的脚本或回调。<script-name>/<callback-name> 必须是为平台或平台类型定义的“脚本”的名称。

extrapolate / stop / remove

指示移动器在遇到此航路点且路线中没有更多航路点时要执行的操作。可能的操作有：

□ extrapolate- 以当前速度、航向和高度继续移动。

▫ stop - 停止移动。  
□ remove- 从模拟中移除平台。

默认值取决于移动器的类型：

□ extrapolate - WSF_AIR_MOVER   
□ stop - WSF_GROUND_MOVER、WSF_ROAD_MOVER、WSF_SURFACE_MOVER

switch_on_passing / switch_on_approach

定义移动器应声明已到达此航路点并应开始向下一个航路点移动的条件。switch_on_passing 有时称为“长转弯”，并导致在平台经过或沿着航路点时发生切换。switch_on_approach 有时称为“短转弯”，并导致在航路点之前发生切换。

默认值：switch_on_passing

注意：这仅适用于位置和偏移航路点。switch_on_approach 仅在下一个点也是位置航路点时适用。用户还需确保目标航路点使得转弯可以正确完成。

distance <length-value> / time <time-value>

如果航路点是 turn_left、turn_right 或 turn_to_heading，并且下一个航路点也是同类，则此命令指定在切换到下一个航路点之前要移动的距离或时间。

注意：将此命令与位置或偏移航路点一起指定是错误的。

time_to_point <time-value>

如果指定，移动器将改变速度以尝试在指定的持续时间后到达此航路点。<time-value>是平台从前一个航路点移动到当前航路点所需的时间。time_to_point 只能为位置航路点指定。

node_id <string>

此命令仅在路线是路线网络的一部分时使用。假定在路线网络中的一组路线内共享相同

node_id 的航路点在这些点处相交或连接。

注意：用户有责任确保具有相同 node_id 的航路点实际上具有相同的空间位置。

aux_data <aux-data> … end_aux_data

定义航路点的辅助数据。请参见 aux_data。

路线插入命令允许在当前路线中的某个点插入另一条路线。这使得可以创建表示模式的路线。

# 命令

insert_route <route-name> [ reference_heading <heading> ]   
insert_route <route-name> <latitude> <longitude> <heading>

转换指定名称的路线并将其航路点插入正在定义的路线中。指定名称的路线应已定义为“路线类型”。在命名路线中使用 offset 命令定义的所有点都将转换为新的坐标系，其原点和方向如下定义，然后在内部转换为位置点。

第一种形式：如果命令出现在包含航路点的路线中，则应使用此形式。它使用前一个航路点的纬度和经度作为转换坐标系的原点。如果指定了 reference_heading，则它定义了转换坐标系的方向。如果省略，它将使用前两个航路点之间的航向，如果只有一个前一个航路点，则为 0。

第二种形式：如果命令作为路线中的第一个项目出现，则应使用此形式。<latitude>、<longitude> 和 <heading> 值指定转换坐标系的原点和方向。

注意：此命令对于在路线中插入模式（例如：轨道等）非常有用。

insert_offset_route <route-name> [ reference_heading <heading> ]   
insert_offset_route <route-name> <latitude> <longitude> <heading>

insert_offset_route 命令类似于 insert_route。insert_offset_route 命令将偏移航路点转换为相对于单个原点。这与在路线中显式定义的偏移航路点不同，后者是相对于前一个航路点处理的。这意味着显式包含偏移航路点的路线将与使用 insert_route 命令隐式包含这些偏移航路点的路线不同。

transform_absolute_route <route-name> <north-length-value> <east-length-value> <down-length-value>

将指定名称的路线按指定的量平移并插入到当前路线中。只有位置点会被平移。

# 已弃用的路线插入命令

transform_route <route-name> [ reference_heading <heading> ]   
transform_route <route-name> <latitude> <longitude> <heading>

转换指定名称的路线并将其航路点插入正在定义的路线中。指定名称的路线应已定义为“路线类型”。在命名路线中使用 offset 命令定义的所有点都将转换为新的坐标系，其原点和方向如下定义，然后在内部转换为位置点。

第一种形式：如果命令出现在包含航路点的路线中，则应使用此形式。它使用前一个航路点的纬度和经度作为转换坐标系的原点。如果指定了 reference_heading，则它定义了转换坐标系的方向。如果省略，它将使用前两个航路点之间的航向，如果只有一个前一个航路点，则为 0。

第二种形式：如果命令作为路线中的第一个项目出现，则应使用此形式。<latitude>、<longitude> 和 <heading> 值指定转换坐标系的原点和方向。

注意：此命令对于在路线中插入模式（例如：轨道等）非常有用。

已弃用自版本 2.9：此命令将被 insert_route 替代。

# 4.8.2. 路网 route_network

```perl
route_network <route-network-name> #Repeat as required to specify routes in network route end-route #Repeat as required to specify routes in network use_route <route-name> #Test to solve the shortest path for routes in network test #Test to solve the shortest path between 2 nodes test_nodes <from-node-id> <to-node-id> #Generate debugging output verbose endROUTE_network 
```

上面命令中的路由模型命令参考：4.8.1 路由 route。

route_network 通常用于表示道路、航线或水路网络。它通常被空中交通、道路交通和海上交通等对象使用，以定义平台导航或移动的路径。

注意：route 必须至少定义两个路径点才能添加到 route_network 中。

<table><tr><td>命令</td><td>use-route&lt;route-name&gt;</td></tr><tr><td>解释</td><td>包含具有指定名称的路线类型作为路线定义的一部分。根据需要重复以指定路线网络。
route的定义参见:4.8.1路由route</td></tr><tr><td>命令</td><td>test</td></tr><tr><td>解释</td><td>在初始化期间,测试所有 route 中每个 node_id 之间的所有可能路径,以解决最短路径问题。测试的 route_network 中节点数量将输出到控制台。
参见本节示例 1 - 带有 test 命令的 route_network。
注意:当无法解决每个起点和终点路径之间的最短路径时,输出中会提供警告。参见本节示例 2 - 带有 test 命令的 route_network - 无法解决最短路径。提示:使用 verbose 命令在使用 test 命令时生成额外的调试数据。</td></tr><tr><td>命令</td><td>test_nodes&lt;from-node-id&gt;&lt;to-node-id&gt;</td></tr><tr><td>解释</td><td>在初始化期间,测试所有路线以解决 &lt;from-node-id&gt; 和 &lt;to-node-id&gt; (指定为整数)之间的最短路径。
以下数据将输出到控制台:
From:&lt;from-node-id&gt;
To:&lt;to-node-id&gt;
Cost:(测试路径的计算成本值)
Path:(测试路径中包含的 node_id 列表)</td></tr><tr><td></td><td>参见本节示例3-带有test_nodes命令的route_network。
注意：当路径无法解决时，Cost:=-1且Path:为空。</td></tr><tr><td>命令</td><td>verbose</td></tr><tr><td rowspan="2">解释</td><td>在使用test命令时生成额外的调试数据。每条测试路径的以下数据将输出到控制台：
From:&lt;from-node-id&gt;
To:&lt;to-node-id&gt;
Cost:(测试路径的计算成本值)
Path:(测试路径中包含的node_id列表)</td></tr><tr><td>参见本节示例4-带有test和verbose命令的route_network。
注意：当在到目标节点的路线中检测到断开连接时，无法解决最短路径。当无法解决最短路径时，将提供警告，Cost:=-1且Path:No path could be found。参见示例5-带有verbose的test命令-无法解决最短路径。</td></tr></table>

示例 1 - 带有 test 命令的 route_network  
```csv
Example Output
#route_network with test command
route_network network_test
route
name North_Stert
navigation
position 39.219389n 86.5141197w
node_id 180609922
position 39.2211938n 86.5141739w
node_id 180609925
endjahication
end route
route
name North_West_Drive
navigation
position 39.2222346n 86.5172063w
node_id 180585436
position 39.2221397n 86.5168094w
node_id 180585443
position 39.2220435n 86.5141509w
node_id 180585448
end_havigaton
end route
route
name North_East_Drive
navigation
position 39.2204988n 86.5114021w
node_id 180618988
position 39.220344n 86.51123w 
```

<table><tr><td>node_id 180646456</td><td></td></tr><tr><td>endjahmentation</td><td></td></tr><tr><td>endRoute</td><td></td></tr><tr><td>route</td><td></td></tr><tr><td>name East_Stert</td><td></td></tr><tr><td>navigation</td><td></td></tr><tr><td>position 39.2193807n 86.5145605w</td><td></td></tr><tr><td>node_id 180609922</td><td></td></tr><tr><td>position 39.2193854n 86.5137976w</td><td></td></tr><tr><td>node_id 180646456</td><td></td></tr><tr><td>position 39.2193414n 86.5099257w</td><td></td></tr><tr><td>endjahmentation</td><td></td></tr><tr><td>endRoute</td><td></td></tr><tr><td>route</td><td></td></tr><tr><td>name West_Drive</td><td></td></tr><tr><td>navigation</td><td></td></tr><tr><td>position 39.2220473n 86.5160534w</td><td></td></tr><tr><td>node_id 180585443</td><td></td></tr><tr><td>position 39.2219058n 86.5160317w</td><td></td></tr><tr><td>node_id 180609925</td><td></td></tr><tr><td>position 39.2211938n 86.5127147w</td><td></td></tr><tr><td>node_id 180585448</td><td></td></tr><tr><td>position 39.2210674n 86.5124463w</td><td></td></tr><tr><td>node_id 180618988</td><td></td></tr><tr><td>end_ha navigation</td><td></td></tr><tr><td>end_ha route</td><td></td></tr><tr><td>test</td><td></td></tr><tr><td>end_ha route_network</td><td></td></tr></table>

示例 2 - 带有 test 命令的 route_network - 无法解决最短路径  

<table><tr><td>Example</td><td>Output</td></tr><tr><td># route_network with test command cannot solve shortest path</td><td>...</td></tr><tr><td>route_network_network_test</td><td>Loading simulation input.</td></tr><tr><td>route</td><td>Begin testing route network.</td></tr><tr><td>route</td><td>Network: osm_roadnetwork</td></tr><tr><td>name North_Ster</td><td>Nodes: 4</td></tr><tr><td>navigation</td><td>* WARNING: Could not solve shortest path.</td></tr><tr><td>position 39.219389n 86.5141197w</td><td>From: 180609922</td></tr><tr><td>node_id 180609922</td><td>To: 180618988</td></tr><tr><td>position 39.2211938n 86.5141739w</td><td>* WARNING: Could not solve shortest path.</td></tr><tr><td>node_id 180609925</td><td>From: 180609922</td></tr></table>

<table><tr><td>endjahment
endjahment
endjahment
endjahment
endjahment
endjahment
endjahment
endjahment
endjahment
endjahment
endjahment
endjahment
endjahment
endjahment
endjahment
endjahment
endjahment
endjahment
endjahment
endjahment
endjahment
endjahment
endjahment
endjahment
endjahment
endjahment</td></tr></table>

示例 3 - 带有 test_nodes 命令的 route_network  

<table><tr><td>Example</td><td>Output</td></tr><tr><td># route_network with test_nodes command route_network network_test_nodes route name North_Ster navigation position 39.219389n 86.5141197w node_id 180609922 position 39.2211938n 86.5141739w node_id 180609925 endjahication endroute route name North_West_Drive navigation position 39.2222346n 86.5172063w node_id 180585436 position 39.2221397n 86.5168094w node_id 180585443 position 39.2220435n 86.5141509w</td><td>...Loading simulation input. Route network &#x27;test_nodes&#x27;: From Node: 180609922 To Node: 180585443 Cost: 215 Path: 180609922 180609925 180585443 ...</td></tr></table>

```txt
node_id 180585448 endjahng   
endjahng   
endroute   
route   
name North_East_Drive   
navigation position 39.2204988n 86.5114021w node_id 180618988 position 39.220344n 86.51123w node_id 180646456 endjahng   
endjahng   
endroute   
route   
name East_Sreet   
navigation position 39.2193807n 86.5145605w node_id 180609922 position 39.2193854n 86.5137976w node_id 180646456 position 39.2193414n 86.5099257w endjahng   
endjahng   
endroute   
route   
name West_Drive   
navigation position 39.2220473n 86.5160534w node_id 180585443 position 39.2219058n 86.5160317w node_id 180609925 position 39.2211938n 86.5127147w node_id 180585448 position 39.2210674n 86.5124463w node_id 180618988 end_hangg   
end_hangg   
endroute   
test_nodes 180609922 180585443   
endRoute network 
```

示例 4 - 带有 test 和 verbose 命令的 route_network  
```txt
Example Output
# route_network with test and verbose ... 
```

<table><tr><td>commands</td><td>Loading simulation input.</td></tr><tr><td>route_network network_test</td><td>Begin testing route network.</td></tr><tr><td>route</td><td>Network: network_test</td></tr><tr><td>name North_Stertn</td><td>Nodes: 8</td></tr><tr><td>navigation</td><td></td></tr><tr><td>position 39.219389n 86.5141197w</td><td>From: 180609922</td></tr><tr><td>node_id 180609922</td><td>To: 180609925</td></tr><tr><td>position 39.2211938n 86.5141739w</td><td>Cost: 200</td></tr><tr><td>node_id 180609925</td><td>Path:</td></tr><tr><td>endjahmentation</td><td>180609922</td></tr><tr><td>endRoute</td><td>180609925</td></tr><tr><td>end_north_West_Drive</td><td>From: 180609922</td></tr><tr><td>navigation</td><td>To: 180585436</td></tr><tr><td>position 39.2222346n 86.5172063w</td><td>Cost: 250</td></tr><tr><td>node_id 180585436</td><td>Path:</td></tr><tr><td>position 39.2221397n 86.5168094w</td><td>180609922</td></tr><tr><td>node_id 180585443</td><td>180609925</td></tr><tr><td>position 39.2220435n 86.5141509w</td><td>180585443</td></tr><tr><td>node_id 180585448</td><td>180585436</td></tr><tr><td>end_nahmentation</td><td></td></tr><tr><td>endRoute</td><td>From: 180609922</td></tr><tr><td>end_north_East_Drive</td><td>To: 180585443</td></tr><tr><td>navigation</td><td>Cost: 215</td></tr><tr><td>position 39.2204988n 86.5114021w</td><td>Path:</td></tr><tr><td>node_id 180618988</td><td>180609922</td></tr><tr><td>position 39.220344n 86.51123w</td><td>180609925</td></tr><tr><td>node_id 180646456</td><td>180585443</td></tr><tr><td>end_nahmentation</td><td>From: 180609922</td></tr><tr><td>endRoute</td><td>To: 180585448</td></tr><tr><td>end_north_East_Drive</td><td>Cost: 114</td></tr><tr><td>navigation</td><td>Path:</td></tr><tr><td>position 39.2193807n 86.5145605w</td><td>180609922</td></tr><tr><td>node_id 180609922</td><td>180646456</td></tr><tr><td>position 39.2193854n 86.5137976w</td><td>180618988</td></tr><tr><td>node_id 180646456</td><td>180585448</td></tr><tr><td>position 39.2193414n 86.5099257w</td><td>From: 180609922</td></tr><tr><td>end_nahmentation</td><td>To: 180618988</td></tr><tr><td>end_north_East_Drive</td><td>Cost: 87</td></tr><tr><td>end_route</td><td>Path:</td></tr><tr><td>name West_Drive</td><td>180609922</td></tr><tr><td>navigation</td><td>180646456</td></tr></table>

示例 5 - 带有 verbose 的 test 命令 - 无法解决最短路径  

<table><tr><td>position 39.2220473n 86.5160534w
node_id 180585443</td><td>180618988</td></tr><tr><td rowspan="2">position 39.2219058n 86.5160317w
node_id 180609925</td><td>From: 180609922</td></tr><tr><td>To: 180646456</td></tr><tr><td rowspan="3">position 39.2211938n 86.5127147w
node_id 180585448</td><td>Cost: 65</td></tr><tr><td>Path:</td></tr><tr><td>180609922</td></tr><tr><td>position 39.2210674n 86.5124463w
node_id 180618988</td><td>180646456</td></tr><tr><td>endjahmentary</td><td>...</td></tr><tr><td>endRoute</td><td></td></tr><tr><td>verbose</td><td></td></tr><tr><td>test</td><td></td></tr><tr><td>endRoute_network</td><td></td></tr></table>

<table><tr><td>Example</td><td>Output</td></tr><tr><td># test command with verbose - cannot solve shortest path route_network_network_test route name North_Ster navigation position 39.219389n 86.5141197w node_id 180609922 position 39.2211938n 86.5141739w node_id 180609925 endjahment navigation endroute route name North_East_Drive navigation position 39.2204988n 86.5114021w node_id 180618988 position 39.220344n 86.51123w node_id 180646456 endjahment navigation endroute verbose test</td><td>... Loading simulation input. Begin testing route network. Network: network_test Nodes: 4 From: 180609922 To: 180609925 Cost: 200 Path: 180609922 180609925 * WARNING: Could not solve shortest path. From: 180609922 To: 180618988 From: 180609922 To: 180618988 Cost: -1 Path: No path could be found. * WARNING: Could not solve shortest path. From: 180609922 To: 180646456</td></tr></table>

end_route_network

From: 180609922

To: 180646456

Cost: -1

Path:

No path could be found.

From: 180609925

To: 180609922

Cost: 200

Path:

180609925

180609922

* WARNING: Could not solve shortest path.

From: 180609925

To: 180618988

From: 180609925

To: 180618988

Cost: -1

Path:

No path could be found.

* WARNING: Could not solve shortest path.

From: 180609925

To: 180646456

From: 180609925

To: 180646456

Cost: -1

Path:

No path could be found.

...

Cost: 87

Path:

180609922

180646456

180618988

From: 180609922

To: 180646456

Cost: 65

Path:

180609922

180646456

...

4.8.3. 空中交通 air_traffic  
```txt
airTraffic aircraft_type ... end_Aircraft_type airbase ... end_airbase everyone_land_time ... end_airTraffic remove_completed_flights   
end_airTraffic 
```

air_traffic 命令在模拟期间生成背景空中交通。生成器以指定的间隔创建往返机场的航班。必须定义以下项目：

□ 要生成的飞机类型  
□ 飞机可以起飞和降落的空军基地  
□ 出发信息（速率、类型和目的地）

命令

aircraft_type <aircraft-type> … end_aircraft_type   
定义可以由空中交通管理器控制的飞机的属性。<aircraft-type> 名称必须是先前定义的platform_type。  
minimum_cruise_altitude <length-value>该飞机类型可以巡航的最低高度。  
maximum_cruise_altitude <length-value>该飞机类型可以巡航的最高高度。  
mean_cruise_speed <speed-value>该飞机类型的平均巡航速度。  
sigma_cruise_speed <speed-value>速度的标准差幅度。  
maximum_operating_range <length-value>该飞机类型可以飞行的最大距离，用于确定它可以飞往哪些空军基地。  
minimum_runway_length <length-value>该飞机类型可以降落的最小跑道长度，用于确定它可以飞往哪些空军基地。  
local表示该飞机可以用于本地航班。  
mean_loiter_time <time-value>该飞机类型在到达 local_destination 后的盘旋时间。  
sigma_loiter_time <time-value>时间的标准差幅度。  
loiter_route <route>该飞机到达 local_destination 后执行的盘旋模式。注意：可以指定多个 loiter_route 命令以使用不同的盘旋模式。

示例：

```txt
aircraft_type Cessna172 minimum_cruise_altitude 10000 ft maximum_cruise_altitude 12000 ft 
```

```txt
mean_cruise_speed 175 kts  
sigma_cruise_speed 20 kts  
minimum_runway_length 3000 ft  
maximum-operating_range 400 nm  
end_Aircraft_type 
```

airbase <airbase-name> <latitude> <longitude> … end_airbase

定义飞机可以起飞或到达的空军基地的属性。可以根据需要多次指定 airbase 块以定义所有空军基地。<airbase-name> 指定空军基地的名称。在空中交通定义中必须是唯一的。

<latitude> <longitude> 指定空军基地的纬度和经度。

runway_length <length-value>

指定跑道的长度。如果指定了 runway 命令，则此命令不是必需的。

runway_heading <heading>

指定跑道的航向。起飞和降落将在此方向进行。如果指定了 runway 命令，则此命令不是必需的。

runway <beg-lat> <beg-lon> <end-lat> <end-lon>

指定跑道的端点。此命令可用于精确指定跑道的位置。此命令将覆盖 runway_length 和runway_heading 命令。

departure_interval <time-value>

指定所有出发的时间间隔。

deactivation_time <time-value>

这是一个可选命令，指定空军基地何时“停用”。这可用于模拟空军基地的情况，防止进一步的到达或出发。目前在途的飞机将被转移到另一个空军基地。

aircraft <aircraft-type> <fraction>

定义从空军基地出发的交通中指定类型的飞机的比例（范围为 (0..1]）。注意：给定空军基地的所有 <fraction> 值之和必须为 1。

destination <airbase-name> <fraction>

定义从此空军基地出发的交通中飞往指定目的地的比例。给定空军基地目的地的所有<fraction> 值之和必须为 1。此外，飞机必须在目的地空军基地定义中列出。

local_destination <latitude> <longitude> <length-value> <fractional-quantity>

指定本地起飞的飞机将飞往并盘旋的本地目的地。第三个参数是以指定纬度和经度为中心的区域直径。可以指定多个 local_destination，但它们的 <fractional-quantity> 之和必须为1.0。

空军基地子命令示例：

```txt
airbase SFO 37:37:08.300N 122:22:29.600W runway_length 12000 ft runway Heading 117 departure_interval 50.0 min aircraft B-707 1.0 destination LAS 1.0   
end_airbase 
```

everyone_land_time <time_value>

指定所有背景空中交通降落的时间。

remove_completed_flights

待定（TBD）

# 4.8.4. 道路交通 road_traffic

```txt
roadTraffic   
network <route-network-name>   
vehicle_count <number>   
vehicle_density <number> per <length-unit>   
maximum_speed <speed-value>   
mean_travel_time <time-value>   
sigma_travel_time <time-value>   
minimum_distance_off_road <length-unit>   
maximum_distance_off_road <length-unit>   
pause_time_off_road <time-value>   
end_of_path_option [respawn | reverseDirection]   
vehicle <platform-type> fraction <fractional-quantity> mean_speed <speed-value> sigma_speed <speed-value>   
end_vehle   
convoy start_position <latitude> <longitude> end_position <latitude> <longitude> spacing <length-unit> speed <speed-value> use_closest_waypoint vehicle <number> <platform-type>   
end_conv   
weighted_region latitude <latitude>   
longitude <longitude> inner_radius <length-unit> outer_radius <length-unit> inner_weight <fractional-quantity> outer_weight <fractional-quantity>   
end_weighted_region   
end_network   
end_roadTraffic 
```

road_traffic 命令在模拟期间通过地面移动平台在预定义的 route_network 上生成背景道路交通。

命令

network <route-network-name> … end_network

定义在指定的 route_network 上生成的属性和车辆。

vehicle_count <number>

生成并放置在道路网络上的飞行器数量。如果未指定 <vehicle_count>，则将使用<vehicle_density> 设置。

vehicle_density <number> per <length-unit>

可以指定每单位长度的车辆密度，而不是指定特定数量的车辆（例如，每 1 公里 5 辆车）。

maximum_speed <speed-value>

网络上任何车辆可以行驶的最高速度，即使在车辆块中指定了更快的速度。这可以模拟限速。

mean_travel_time <time-value>

网络中所有车辆的平均行驶时间。

sigma_travel_time <time-value>

行驶时间的标准差幅度。当车辆到达其路径或行驶时间的终点时，它会离开道路一段距离，然后暂停一段时间后从模拟中移除。以下三个项目（<minimum_distance_off_road>、maximum_distance_off_road 和 pause_time_off_road）定义了此过程的参数。

minimum_distance_off_road <length-unit>

车辆离开道路行驶的最小距离。

maximum_distance_off_road <length-unit>

车辆离开道路行驶的最大距离。

pause_time_off_road <time-value>

车辆在离开道路后在其路线终点暂停的时间。

end_of_path_option [respawn | reverse_direction]

确定车辆在其路线终点时应执行的操作。默认情况下，车辆会以不同的路线重新生成。

vehicle <platform-type> end_vehicle

定义在此网络上下文中特定车辆类型的属性。要定义多种车辆类型，请创建多个车辆块。<platform-type> 必须是先前定义的 platform_type。

fraction <fractional-quantity>

如果定义了多个车辆块，则 fraction 是填充道路网络的特定车辆类型的百分比（以小数值表示）。所有车辆比例之和必须加起来为 1。

mean_speed <speed-value>

此车辆块定义的所有车辆的平均速度。

sigma_speed <speed-value>

速度的标准差幅度。

convoy … end_convoy

定义一个车队（即一系列跟随彼此的车辆），在两个端点之间移动。

start_position <latitude> <longitude>

定义车队的初始位置，使用纬度和经度值。

end_position <latitude> <longitude>

定义车队的最终位置，使用纬度和经度值。

spacing <length-unit>

定义车队中每辆车之间的间距。

speed <speed-value>

定义车队的行驶速度。

use_closest_waypoint

如果存在此选项，车队将从最接近指定起始位置的航路点开始，并在最接近终点位置的航路点结束。

vehicle <number> <platform-type>   
定义车队中特定车辆类型及其数量。可以多次指定此选项以创建多种车辆类型。  
weighted_region … end_weighted_region

定义网络中将创建更高密度车辆的区域。例如，此命令可用于在城市区域生成比乡村更多的车辆。加权区域具有内半径和外半径以及权重。权重在内半径和外半径之间线性插值。这允许模拟在内半径和外半径之间线性变化车辆密度。

latitude <latitude>

指定加权区域的中心纬度。

longitude <longitude>

指定加权区域的中心经度。

inner_radius <length-unit>

指定加权区域的内半径。

outer_radius <length-unit>

指定加权区域的外半径。

inner_weight <fractional-quantity>

指定与内半径对应的权重。权重数值越大，车辆密度越高。

outer_weight <fractional-quantity>

指定与外半径对应的权重。权重数值越大，车辆密度越高。

示例  
```txt
roadTraffic network stl_roadnetwork vehicle_count 500 maximum_speed 75 mi/h minimum_distance_off_road 1 nm maximum_distance_off_road 2 nm pause_time_off_road 240 min mean_travel_time 40.0 min sigma_travel_time 5.0 min vehicle Car fraction 0.80 mean_speed 60 mi/h sigma_speed 5 mi/h end_vehicle vehicle Pickup_Truck fraction 0.15 mean_speed 60 mi/h sigma_speed 10 mi/h end_vehicular vehicle School_Bus 
```

```txt
fraction 0.05  
mean_speed 50 mi/h  
sigma_speed 10 mi/h  
end_vehicle  
end_network  
end_roadTraffic 
```

# 4.8.5. 海上交通 sea_traffic

```txt
seaTraffic   
port <name> position<latitude-value> <longitude-value> <length-value> port-route position<latitude-value> <longitude-value> <length-value> end_port-route localTraffic_region<latitude-value> <longitude-value> <length-value> <fractional> departure_interval <time-value> use_all_lanes lane <name> <weighting-factor>   
end_port   
lane <name> port<port-name> [ignore_port-route] lane-route ... end_lane-route position<latitude-value> <longitude-value> <length-value>   
end_lane   
departureTraffic <fraction> ship<platform-type> ... end_ship fraction <fraction> mean_speed <speed> sigma_speed <speed>   
end_SHiP   
localTraffic <fraction> ship<platform-type> ... end_ship fraction <fraction> mean(loiter_time <time> sigma(loiter_time <time> loiter-route <name> mean_speed <speed> sigma_speed <speed>   
end_localTraffic   
end_seaTraffic 
```

sea_traffic 命令在模拟期间生成背景船舶交通。生成器创建往返港口的船只以及港口周围的本地船舶交通。

# 命令

port <name> … end_port

定义船舶交通起始和终止的港口。

position <latitude-value> <longitude-value> <length-value>

定义港口的位置和大小。第三个参数用作直径，因此进入港口的船只将位于以指定纬度和经度为中心的给定直径的圆内。

port_route … end_port_route

定义船舶进入和离开港口的路线。这使得能够在离开主航道后引导船只绕过障碍物。指定多个位置以构建进入港口的路径。当船只离开港口时，它们使用定义的港口路线的反向。

position <latitude-value> <longitude-value> <length-value>

定义进入港口路线上的航路点。第三个参数用作直径，因此沿港口路线行驶的船只将在以指定纬度和经度为中心的给定直径的圆内随机路径。

注意：指定多个位置命令以放置所需数量的航路点。

local_traffic_region <latitude-value> <longitude-value> <length-value> <fractional>

本地交通从此港口将前往的区域。fraction 指定从此港口前往该区域的交通比例。

departure_interval <time-value>

指定从港口出发的船只的间隔时间。

use_all_lanes

从港口出发和终止的船舶交通将使用所有可用的航道。

lane <name> <weighting-factor>

指定船舶交通可以使用的航道。权重因子用于在各种航道之间分配交通。

示例：

```txt
port seattle  
position 48:15n 123:00w 1 km  
port-route  
    position 48:30n 125:00w 10 km  
    position 48:15n 124:00w 1 km  
end_port-route  
localTraffic_region 48:15n 123:00w 10 km 0.3  
localTraffic_region 48:10n 122:50w 10 km 0.2  
localTraffic_region 48:20n 122:52w 15 km 0.25  
localTraffic_region 48:25n 123:10w 15 km 0.25  
departure_interval 5 min  
lane lane-seattle-to-british-columbia 0.7  
lane lane-seattle-to-baja-mexico 0.3  
end_port 
```

lane <name> … end_lane

定义船舶交通用于从港口到港口旅行的航道。

port <port-name> [ignore_port_route]

指定起始或结束港口。ignore_port_route 是可选的，指定船只在此航道上行驶时将忽略

港口定义的 port_route。

lane_route … end_lane_route

指定船只在使用此航道时将行驶的路线。

注意：不要指定起始或结束港口的位置。

position <latitude-value> <longitude-value> <length-value>

指定航道的一个点。第三个参数用作直径，因此沿航道行驶的船只将在以指定纬度和经度为中心的给定直径的圆内随机路径。

示例：

```shell
lane lane-seattle-to-british-columbia  
port seattle  
port british-columbia  
lane-route  
position 50:00n 129:00w 50 km  
end_lane-route  
end_lane 
```

departure_traffic <fraction> … end_departure_traffic

定义将离开港口并前往 local_traffic_region 的船舶交通。fractional-quantity 是离开港口并前往本地区域的船只的百分比。此比例和 departure_traffic 比例之和必须为 1.0。

ship <platform-type> … end_ship

定义特定船舶类型的属性。

注意：要为出发交通使用多种船舶类型，请创建多个船舶块。

fraction <fraction>

控制使用此船舶类型的船舶交通量。

注意：所有船舶比例之和必须为 1。

mean_speed <speed>

船舶交通行驶的平均速度。

sigma_speed <speed>

船舶速度的标准差。

示例：

```txt
departure蚣 0.5   
ship TANKER_SHIP fraction 0.5 mean_speed 20.0 kts sigma_speed 5.0 kts end_ship ship CONTAINER_SHIP fraction 0.5 mean_speed 20.0 kts sigma_speed 5.0 kts end_ship   
enddeparture蚣 
```

local_traffic <fraction> … end_local_traffic

定义将离开港口并前往 local_traffic_region 的船舶交通。fractional-quantity 是离开港口并前往本地区域的船只的百分比。此比例和 departure_traffic 比例之和必须为 1.0。

ship <platform-type> … end_ship

定义特定船舶类型的属性。

注意：要在本地交通区域中使用多种船舶类型，请创建多个船舶块。

fraction <fraction>

控制使用此船舶类型的船舶交通量。

注意：所有船舶比例之和必须为 1。

mean_loiter_time <time>

指定船舶类型在 local_traffic_region 中盘旋的时间。

sigma_loiter_time <time>

船舶盘旋时间的标准差。

loiter_route <name>

船舶类型将使用指定的路线进行盘旋。可以输入多个 loiter_route。

mean_speed <speed>

船舶交通行驶的平均速度。

sigma_speed <speed>

船舶速度的标准差。

# 4.9. 区域和区域集

# 4.9.1. 区域 zone

```txt
zone <zone-name>
    debug
    position <latitude-value> <longitude-value> | referenceplatform <platform-name>
    heading <angle-value>
    references <zone-name>
    minimum_altitude <length-value>
    maximum_altitude <length-value>
    positive | negative
    aux_data <aux_data> ... end(aux_data
    fill_color <color-value>
    line_color <color-value>
    circular
    minimum_radius <length-value>
    maximum_radius <length-value>
    start_angle <angle-value>
    stop_angle <angle-value> 
```

```txt
spherical minimum_radius <length-value> maximum_radius <length-value> start_angle <angle-value> stop_angle <angle-value>   
elliptical lateral_axis <length-value> longitudinal_axis <length-value> start_angle <angle-value> stop_angle <angle-value>   
polygonal point <x-value> <y-value> <length-units> # if relative (x / y)   
polar # if relative (bearing / range) point <angle-value> <length-value>   
lat_lon # if absolute (lat / lon) point <latitude-value> <longitude-value>   
mgrs # if absolute (mgrs) point <mgrs-value>   
comm_modifier | sensor_modifier | modifier ...   
end-zone 
```

Zone（区域）表示一个地理区域。可以测试地理点是否包含在区域内，从而使实体能够根据给定检查的结果动态地表现。一个区域由以下属性定义：

# 属性

Context（上下文）

上下文决定了哪些实体可以访问给定的区域。

Geometry（几何形状）

区域的形状和大小。

Bounds（边界）

约束给定几何形状的线性和角度边界。

Reference Frame and Pose（参考框架和姿态）

区域相对于定义的参考框架的位置和航向。

# 上下文

Global（全局）

在全局上下文中定义的区域称为全局区域。模拟中的任何实体都可以访问全局区域进行计算。

# Local（本地）

在本地上下文中定义的区域称为本地区域或平台定义区域。本地区域可以在platform_type 定义或 platform 定义中创建。对于在 platform_type 定义中定义的本地区域，该类型的每个平台在其平台定义中隐式定义了该区域的一个实例。对于直接在 platform 定义中定义的本地区域，只有该平台可以访问本地区域进行计算。

# 几何形状

# Planar（平面）

平面几何形状由二维中的一个或多个点定义。在三维空间中定义时，平面几何形状在第三维上自然是无界的。此外，由曲面上的坐标（如地球表面）定义的平面区域在几何上与表面一致。对于绝对区域，这导致截面在地球中心收敛，并在地球表面上发散。对于相对平面几何形状，区域截面与地球表面一致，结合偏移/范围/半径的边界观察高度边界，导致区域在不同高度不收敛/发散。平面几何形状如下：

# Polygonal（多边形）

由构成区域顶点的有序点集定义的几何形状。给定多边形区域的点可以由以下坐标系之一定义：

Relative（相对）

相对坐标系中的点从定义的原点派生意义。由相对点定义的区域是相对区域。

Offset（偏移）

偏移定义的点提供一对距离值，定义从给定原点的横向和纵向距离。

Polar（极坐标）

极坐标定义的点提供一个方位和范围，定义从给定原点的径向距离。

# Absolute（绝对）

在绝对坐标系中的点（在此情况下为 WCS）固有地提供所有位置信息，无需参考原点。由绝对点定义的区域是绝对区域。

Lat/Lon（纬度/经度）

每个点由纬度和经度（lat_lon）对定义。

MGRS

每个点由军事网格参考系统（mgrs）中的字母数字字符序列对定义。

# Circular（圆形）

圆形几何形状由最大半径（可选地，最小半径）定义。圆形区域始终是相对的。

# Elliptical（椭圆形）

椭圆形几何形状由横向和纵向轴（可选地，最小半径）定义。椭圆形区域始终是相对的。

![](images/f742edafeecccdd84eb457112a872192f732c0fac4a571e5b38500aef76a16c9.jpg)

非平面几何是独立定义的，因此不受其定义表面的曲率影响。非平面几何在给定维度中可能有界也可能无界。

# 球形几何

球形几何由 maximum_radius（最大半径）定义（可选地，还可以定义 minimum_radius（最小半径））。球体表面上的所有点到球心的距离相等。球形区域始终是相对的。球形的原点始终是相对于参考框架的零高度。这意味着在世界坐标系（WCS）中的球形区域出现在零高度，而在实体坐标系（ECS）中的球形区域出现在参考实体的高度。minimum_altitude（最小高度）和 maximum_altitude（最大高度）从 WCS 参考框架应用，无论区域的参考框架如何。

# 边界

边界或几何边界限制了给定域中的几何，并分为以下几类：

角度边界：角度边界适用于径向几何。当应用时，角度边界将几何限制在地球表面的平面参考框架中的 start_angle（起始角度）和 stop_angle（终止角度）之间。零角度由区域的参考框架确定。  
线性边界：线性边界适用于所有几何。当应用时，线性边界在给定方向上限制几何。目前，minimum_altitude（最小高度）和 maximum_altitude（最大高度）命令可用于限制给定区域的下限和上限高度，其中高度始终参考地球表面。

# 参考框架和姿态

姿态封装了对象在参考框架内的位置和方向。由于区域不考虑俯仰或滚动，区域的姿态包括位置和航向。

绝对区域：固有地在世界坐标系（WCS）参考框架中定义，并保持静态姿态。相反，相对区域可以在 WCS 或实体坐标系（ECS）参考框架中定义。使用 WCS 参考框架的相对区域定义了一个可以在脚本中更改的静态姿态，而使用 ECS 参考框架的相对区域将观察到与参考实体（通常是平台）对齐的动态姿态。  
因为绝对区域的每个点都在 WCS 参考框架中定义，所以生成区域的姿态是绝对的。这意味着在相关区域定义中使用的位置和航向命令将被忽略。  
与绝对区域不同，相对区域必须定义其姿态及其适用的参考框架。参考框架和姿态由以

下因素定义：

□ 区域定义的上下文。  
□ reference_platform（参考平台）命令。  
□ position（位置）和 heading（航向）命令。

在测试局部相对区域内的包含性时，被测试的点必须与定义区域的平台在同一半球。这可以防止几乎直接在地球另一侧的点被视为在区域内。

# 命令

常用命令

▫ debug：在运行时启用调试消息，特别是在使用 PointIsInside 脚本方法时非常有用。  
□ minimum_altitude <length-value>：最小高度约束（平均海平面）。默认值：无最小高度约束。  
▫ maximum_altitude <length-value>：最大高度约束（平均海平面）。默认值：无最大高度约束。  
▫ position <latitude-value> <longitude-value>：静态定义相对区域的原点。指定此命令时不应使用 reference_platform 命令。如果在平台定义的区域上指定此命令，区域将使用指定的位置作为其原点，并将使用 WCS 作为其参考框架。  
▫ heading <angle-value>：与 position 一起使用以静态指定区域的方向。指定此命令时不应使用 reference_platform 命令。如果在平台定义的区域上指定此命令，区域将使用指定的航向，并且必须指定一个位置才能有效。如果指定了位置，区域将使用WCS 作为其参考框架。  
reference_platform <platform-name>：使用指定平台的姿态定义相对全局区域的姿态，并使用平台的 ECS 参考框架移动。每当执行区域包含性检查时，所指示平台的姿态将用作区域的姿态。如果在进行包含性检查时尚未创建参考平台，则检查将返回 false。如果参考平台已被删除，但在参考平台存在时至少执行过一次包含性检查，则检查将使用参考平台的最后已知位置和航向进行。  
□ references <zone-name>：对另一个区域的引用。指定 references 命令的区域是参考区域。被引用区域的几何被复制，并且可以通过使用其他有效的几何命令覆盖属性。.. 注意：不相关于继承几何的命令不应使用，如果使用可能导致意外行为。

负面/正面

□ negative/positive：指定区域是负面还是正面。负面区域具有与区域命令定义的区域完全相反的区域。例如，如果指定了一个圆形区域，则否定它将表示圆外的区域。默认值：positive（正面）。

辅助数据

□ aux_data <aux-data> … end_aux_data：定义区域的辅助数据。参见 aux_data。  
□ fill_color<color-value>：定义区域的填充颜色。注意：如果颜色通过名称指定，填充 alpha 将在[0, 255]范围内设置为 63。  
□ line_color <color-value>：定义区域的线条颜色。

径向几何

圆形区域

定义一个圆形区域的语法如下：

```txt
zone<zone_name> 
```

```txt
circular minimum_radius <length-value> #最小半径约束 maximum_radius <length-value> #最大半径约束 start_angle <angle-value> #起始角度 stop_angle <angle-value> #终止角度 end-zone 
```

椭圆形区域

定义一个椭圆形区域的语法如下：

```txt
zone <zone_name>  
elliptical  
lateral_axis <length-value> # 横轴约束  
longitudinal_axis <length-value> # 纵轴约束  
minimum_radius <length-value> # 最小半径约束  
start_angle <angle-value> # 起始角度  
stop_angle <angle-value> # 终止角度  
end-zone 
```

球形区域

定义一个球形区域的语法如下：

```c
zone <zone_name>
spherical
    minimum_radius <length-value> # 最小半径约束
    maximum_radius <length-value> # 最大半径约束
    start_angle <angle-value> # 起始角度
    stop_angle <angle-value> # 终止角度
end-zone
```

# 半径和角度约束

minimum_radius <length-value>：最小半径约束。默认值：无最小半径约束。  
maximum_radius <length-value>：最大半径约束。默认值：无最大半径约束。  
start_angle <angle-value> 和 stop_angle <angle-value>：定义角度约束。角度区域从start_angle 开始，顺时针到 stop_angle。零度角指向参考航向的方向（在 WCS 中为北，在 ECS 中为实体航向）。

椭圆形区域的轴约束

lateral_axis <length-value>：椭圆形区域的横轴约束。  
longitudinal_axis <length-value>：椭圆形区域的纵轴约束。

多边形几何

多边形区域

多边形区域由一系列节点点定义，必须遵循以下条件：

从上方看，点必须按顺时针方向排列。  
第一个和最后一个点不应重复（即，假设最后一个点和第一个点之间的连接）。

所有区域点必须是同一类型（全部相对 x,y，全部极坐标，全部 lat_lon，或全部 mgrs）。

定义一个多边形区域的语法如下：  
```txt
zone <zone_name> polygonal  
point <x-value> <y-value> <length-units> # 如果是相对（x/y）  
polar #如果是相对（方位/距离）  
point <angle-value> <length-value> #如果是相对（方位/距离）  
lat_lon #如果是绝对（纬度/经度）  
point <latitude-value> <longitude-value> #如果是绝对（纬度/经度）  
mgrs #如果是绝对（mgrs）  
point <mgrs-value> #如果是绝对（mgrs）  
// 根据需要重复 point...以适应每种格式。  
end-zone
```

# 衰减

comm_modifier <category-name> <real-value>：指定应用于通信设备检测的衰减。  
sensor_modifier <category-name> <real-value>：指定应用于传感器设备检测的衰减。  
modifier <category-name> <real-value>：指定应用于检测线的衰减。<real-value>是一个介于 0.0 和 1.0 之间的数字，表示区域内每米的衰减值百分比损失。例如，修饰符值为 0.1表示 10 米的穿透将导致 100%的衰减。

注意：修饰符关键字仅在绝对区域定义中有效。区域穿透计算不考虑任何区域类型的minimum_radius、start_angle 和 stop_angle 输入，以及多边形区域类型的 heading 输入。

# 4.9.2. 区域集 zone_set

```txt
zone_set<zone_name> zone ... zone definition ... end-zone exclude-zone ... zone definition ... end Exclude-zone attenuation_parameters ... attenuation parameters ... end attenuation_parameters use-zone <shared-zone_name> useExclude-zone <shared-zone_name> fill_color <color-value> 
```

```txt
line_color <color-value> end-zone_set 
```

区域集（zone_set）是由离散区域组件（称为区域集元素）组成的区域。区域集元素可以是包含区域（inclusionzone）或排除区域（exclusionzone）。此外，区域集元素可以是嵌入区域（embeddedzone）或使用区域（use_zone）。嵌入区域直接在包含区域集的定义中定义。使用区域是添加到区域集中的外部定义区域的副本。

一个点被认为包含在区域集中，如果它至少包含在一个包含区域中，并且不包含在任何排除区域中。为了功能正常，区域集必须至少包含一个包含区域。

区域集本身也是一个区域。因此，区域集由区域属性定义，包括：

集合上下文：定义整个区域集的上下文。  
元素几何：定义每个元素的几何形状。  
元素边界：定义每个元素的边界。  
元素参考框架和姿态：定义每个元素的参考框架和姿态。

# 命令

zone…end_zone：创建一个嵌入区域，将作为此区域集的包含区域。注意：此命令可以出现 0 次或多次。  
exclude_zone … end_exclude_zone：创建一个嵌入区域，将作为此区域集的排除区域。注意：此命令可以出现 0 次或多次。  
use_zone <shared_zone_name>：声明指定的共享区域将作为此区域集的包含区域。注意：此命令可以出现 0 次或多次。  
use_exclude_zone <shared_zone_name>：声明指定的共享区域将作为此区域集的排除区域。注意：此命令可以出现 0 次或多次。  
fill_color <color-value>：定义区域的填充颜色。注意：如果颜色通过名称指定，填充 alpha将在[0, 255]范围内设置为 63。  
line_color <color-value>：定义区域的线条颜色。

# 衰减参数

attenuation_parameters … end_attenuation_parameters：定义用于给定区域集的衰减变量。基于区域的衰减提供了一种机制，可以在不使用复杂传播算法的情况下衰减来自通信或传感器设备的 RF 或光学信号。为了使用此功能，用户必须首先创建包含modifier_category 命令的通信和传感器定义。然后，用户必须创建一个或多个定义信号通过区域时应用的衰减的区域集。  
file <file-name>：声明要导入以表示此区域集的形状文件（.shp）。<file-name>是 ESRI形状文件的名称，不包括扩展名。  
use_dted：如果包含，将使用当前加载的 DTED 文件中定义的垂直偏移。  
height_parameter <dbf file-name>：用于定义各个形状高度的.dbf 文件中的参数。""是可接受的输入。  
constant_height <height-value> <unit-type>：用于所有形状的恒定高度。height_parameter会覆盖此值。  
base_altitude_parameter <dbf file-name>：用于定义各个形状基准高度的.dbf 文件中的参数。""是可接受的输入。

constant_base_altitude <base altitude-value> <unit-type>：用于所有形状的恒定基准高度。base_altitude_parameter 会覆盖此值。  
projection <projection-type>：定义要使用的投影类型。目前，地心投影（geocentric）和大地投影（geodetic）是可接受的。默认值：大地投影（geodetic）  
sensor_modifier <modifier-name> <modifier-value> ： 声 明 此 区 域 集 修 改 所 有 带 有modifier_category <modifier-name>的传感器，使用在<modifier-value>中定义的衰减值。  
comm_modifier <modifier-name> <modifier-value>：声明此区域集修改所有通信设备，使用在<modifier-value>中定义的衰减值。

# 4.10. 导航误差 navigation_errors

end_navigation_errors   
```txt
navigation.errors   
gps_status ...   
# GPS Error specifications   
gps_in_track_error ...   
gps CROSS_track_error ...   
gps_vertical_error ...   
gps_degraded-multiplier ...   
# INS Error specifications   
insaccelerometer.bias_error ...   
insgyroscope.bias_error ...   
ins_random_walk_error ...   
ins_vertical_error ...   
ins_xerrors ...   
ins_yerrors ...   
ins_zerrors ...   
ins_xy Errors ...   
# Other parameters   
ins_scaleFactors...   
randomness...   
show.status_changes...   
time_history_path... 
```

Navigation_Errors 块是 platform 命令的一个子命令。其主要功能是定义平台认为其位置与实际位置之间的误差。这种误差以“位置误差向量”表示。这些误差用于影响传感器报告，通过改变报告位置和报告中的任何绝对位置。

该模型提供了根据 GPS 可用性产生不同误差的能力。如果 GPS 被定义为可用，则使用GPS 误差；如果 GPS 不可用，则使用 INS 误差。脚本方法可用于查询和更改 GPS 的可用性状

态。

在每个 update_interval（更新间隔）中，模型计算用于下一个更新间隔的误差或漂移率。如果 GPS 处于活动状态，则使用以下公式计算沿轨误差、横轨误差和垂直误差：

```txt
in_track_error = gaussian(gps_in_track_error)  
cross_track_error = gaussian(gps CROSS_track_error)  
vertical_error = gaussian(gps_vertical_error) 
```

如果 gps_status 设置为 2（降级），则上述每个误差将乘以 gps_degraded_multiplier。

如果 GPS 不处于活动状态，则使用以下公式计算沿轨和横轨漂移率以及垂直误差：

```python
heading_error = gaussian(ins Heading_error)  
perceived_speed = true_speed + gaussian(ins_velocity_error)  
in_track drifting_rate = perceived_speed * abs(cos(heading_error)) - true_speed  
cross Tracks drifting_rate = perceived_speed * sin(heading_error)  
vertical_error = gaussian(ins_vertical_error) 
```

在每次移动更新期间，模型执行以下操作：

如果 GPS 不处于活动状态，更新沿轨和横轨误差：

```txt
dt = time-since-last-mover-update  
in_track_error = in_track_error + dt * in_track_error_drift_rate  
cross Tracks_error = cross Tracks_error + dt * cross Tracks_error_drift_rate 
```

然后，无论 GPS 状态如何，当前的 in_track_error、cross_track_error 和 vertical_error 都会从局部体框架转换为世界框架，用作当前的位置误差向量。

注意：这不是一个完整的导航误差模型（即，它不会直接影响平台的运动。相反，它用于在传感器检测报告过程中引入小误差，因为感知平台可能不知道其确切位置）。

# 命令

gps_cross_track_error <length-reference>：定义高斯分布的标准差，用于在 GPS 可用时创建位置误差向量的横轨分量。默认值： $_ { 0 . 0 \mathsf { m } }$   
gps_in_track_error <length-reference>：定义高斯分布的标准差，用于在 GPS 可用时创建位置误差向量的沿轨分量。默认值： $_ { 0 . 0 \mathsf { m } }$   
gps_vertical_error <length-reference>：定义高斯分布的标准差，用于在 GPS 可用时创建位置误差向量的垂直分量。默认值： $_ { 0 . 0 \mathsf { m } }$   
gps_degraded_multiplier <real-value>：指定当 gps_status 降级（2）时，计算的 GPS 位置误差将被乘以的值。  
gps_status <integer-value>：设置初始操作状态：

□ -1：GPS 不可用。仅计算 INS 误差。  
▫ 0：模型被禁用。既不计算 GPS 误差也不计算 INS 误差。  
□ 1：GPS 可用。仅计算 GPS 误差。  
□ 2 ： GPS 可 用 但 能 力 降 级 。 仅 计 算 GPS 误 差 ， 并 将 这 些 误 差 乘 以gps_degraded_multiplier。  
□ 3 ： GPS 误 差 可 以 从 外 部 源 设 置 （ 例 如 ， 使 用WsfPlatform.SetPerceivedLocationErrorWCS）；否则，模型被禁用。 默认值：1（GPS可用）

ins_accelerometer_bias_error <angle-reference>：定义在 GPS 不可用时使用的加速度计误差的标准差。默认值： $0 . 0 \ : \mathrm { m } / \varsigma ^ { 2 }$   
ins_gyroscope_bias_error <angle-rate-reference>：定义在 GPS 不可用时使用的陀螺仪偏差误差的标准差。默认值：0.0deg/hour  
ins_random_walk_error <real-value>：定义在 GPS 不可用时使用的随机游走误差的标准差。默认值：0.0 deg/sqrt-hr  
ins_scale_factors <real-value> <real-value> <real-value>：定义 INS 比例因子。  
ins_vertical_error <length-reference>：定义高斯分布的标准差，用于在 GPS 不可用时创建位置误差向量的垂直分量。默认值： $0 . 0 1 ~ \mathsf { m }$   
ins_x_errors coefficient <real-value> [ exponent <real-value> ]：为平台实体坐标系（ECS）中的每个轴指定自定义误差模型，当 gps_status 设置为“INS” (-1) 时适用。每个轴的条目表示具有指定系数和指数的多项式项。  
time_history_path <dir-name>：启用写入时间历史文件，显示真实位置和误差分量随时间 的 变 化 。 <dir-name> 是 将 文 件 写 入 的 目 录 名 称 。 文 件 名 将 为<dir-name>/<platform-name>.neh。如果省略此命令，则不会写入时间历史数据。默认值：未指定（不写入时间历史）。  
randomness<boolean-value>：指定是否将位置误差计算为高斯随机数。如果启用，位置误差（gps_in_track_error、gps_cross_track_error 和 gps_vertical_error）将用作随机数生成中的标准差。如果禁用，位置误差将被解释为恒定偏移。默认值：启用  
show_status_changes <boolean-value>：显示状态变化。

# 脚本接口

WsfPlatform 脚本类具有用于查询和更改 GPS 可用性状态以及查询位置误差向量的方法：

GPS_Status   
SetGPS_Status   
SetPerceivedLocationErrorWCS   
PerceivedLocation   
PerceivedLocationErrorNED   
PerceivedLocationErrorWCS

这些脚本方法可用于根据用户希望的任何标准更改 GPS 的可用性。

# 4.11. 环境定义

此处定义了和全局环境、大气、以及在环境中相关传播的部分定义。

# 4.11.1. 全局环境定义 global_environment

```txt
global_environment   
land_coverage...   
landFormation...   
sea_state...   
wind_speed...   
wind_direction...   
wind_table altitude-value> <wind-direction-value> <wind-speed_value> / wind_table data sets in order of increasing altitudes. 
```

```txt
... end Winds_table cloud_altitude_limits ... cloud_water_density ... rain_altitude_limit .. rain_rate ... central_body polar_offsetAngles end_central_body end_global_environment 
```

Global_Environment块定义了全球环境的属性。各种对象利用此块中定义的数据。

# 命令

land_cover <land-cover-type>：指定接收器杂波模型的地表覆盖类型。有效值包括：

```erlang
- :general（一般）
- :urban（城市）
- :agricultural（农业）
- :rangeland_herbaceous（草原）
- :rangeland_shrub（灌木丛）
- :forest deciduous（落叶林）
- :forest_coniferous（针叶林）
- :forest_mixed（混合林）
- :forest_clear-cut（清理林）
- :forest_block-cut（块状砍伐林）
- :wetland_forested（森林湿地）
- :wetland_non_forested（非森林湿地）
- :desert（沙漠）默认值：general
```

land_formation <land-formation-type>：指定接收器杂波模型的地形类型。有效值包括：

```txt
- :level（平坦）
- :inclined（倾斜）
- :undulating（起伏）
- :rolling（滚动）
- :hummocky（丘陵）
- :ridged（脊状）
- :moderately_steen（中等陡峭）
- :steep（陡峭）
- :broken（破碎） 默认值：level
```

sea_state<value>：指定接收器杂波模型的海况。有效值为 0 到 6，描述如下：

□ 0：无浪（平静，光滑）

□ 1：0 - 0.10 米（平静，波纹）  
□ 2：0.10 - 0.50 米（光滑）  
▫ 3：0.50 - 1.25 米（轻微）  
□ 4：1.25 - 2.50 米（中等）  
□ 5：2.50 - 4.00 米（粗糙）  
▫ 6：4.00-6.00 米（非常粗糙） 默认值：0

wind_speed <speed-value>：指定风速。默认值： $0 \ : \mathsf { m } / \mathsf { s }$   
wind_direction <angle-value>：指定风向。默认值：0 度（注意：WSF 风向是风吹向的方向，而不是风来的方向）  
wind_table … end_wind_table：指定风值数据集，每个条目使用 3 个参数（从最低高度到最高高度）：altitude <length-value>（高度）、wind direction <angle-value>（风向）、wind speed <speed-value>（风速）。

```txt
wind_table
0 ft 90 deg 20 kts
5000 ft 95 deg 25 kts
10000 ft 100 deg 30 kts
15000 ft 100 deg 35 kts
20000 ft 120 deg 40 kts
25000 ft 125 deg 45 kts
30000 ft 125 deg 50 kts
35000 ft 130 deg 55 kts
40000 ft 130 deg 60 kts
end Winds_table 
```

Default If no wind_table, then WSF defaults to values assigned to wind_speed_ and wind_direction_.

.. note:: WSF wind direction is the direction to which the wind flows; not from where it comes.

.. note:: Insert altitudes in order from lowest to highest.

cloud_altitude_limits <length-value> <length-value>：指定云层出现的最小和最大高度范围。这用于某些衰减模型。默认值： $0 \textrm { m } 0 \textrm { m }$ （无云）  
cloud_water_density <mass-density-value>：指定云中的水密度。这用于某些衰减模型。默认值： $0 ~ \mathrm { k g } / \mathrm { m } ^ { 3 }$   
rain_altitude_limit <length-value>：指定雨存在的高度以下。这用于某些衰减模型。默认值：0 m  
rain_rate <speed-value>：指定降雨累积率。这用于某些衰减模型。默认值：0 m/s
central_body … end_central_body：指定用于模拟平台的中心体及相关椭球模型。

<central-body-type>的选项包括：

▫ earth_wgs72（地球世界大地测量系统 1972）  
□ earth_wgs84（地球世界大地测量系统 1984）  
□ earth_egm96（地球重力模型 1996）  
□ moon（月球）  
□ sun（太阳）  
□ jupiter（木星）

默认值：earth_wgs84

polar_offset_angles <angle-value> <angle-value>：指定中心体的极偏移角（分别为 x_p 和y_p），相对于 WCS（ITRS）坐标系的天体中间极（CIP）。提供这些值（约为十分之一角秒）可以实现 ECI 和 WCS 坐标之间的非常高精度转换。默认值：0.0rad0.0rad

注意：WCS 到 LLA 的转换受中心体选择的影响，以及在惯性（ECI）坐标转换中计算的恒星运动变换。

