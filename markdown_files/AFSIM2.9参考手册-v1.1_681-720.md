<table><tr><td></td><td>eccentricity 0.2
mean_anomaly 255 deg
inclination 30 deg
raan 120 deg
argument_of_periapsis 80 deg
end_orbital_state
end_mover
endPLATFORM
//Example: Position/velocity declaration
platform test-rv WSF PLATFORM
add mover WSF_SPACE_MOVER
orbital_state
    epoch 2021245.18563
    position 800 0 0 km
    velocity 100 3000 -50 m/s
    end_orbital_state
    end_mover
    endPLATFORM
//Example: TLE declaration
//Note: TLE declaration is only allowed within a WSF_NORAD_SPACE_MOVER
platform test-tle WSF PLATFORM
add mover WSF_NORAD_SPACE_MOVER
orbital_state
    orbit
    0 HST
    1 20580U 90037B 20216.30423610 .00000333 00000-0 92680-5 0
9996
    2 20580 28.4681 168.2117 0002666 190.3324 294.3699 15.09238375401891
    end_orbit
    end_orbital_state
    end_mover
    endPLATFORM</td></tr><tr><td>命令</td><td>epoch [&lt;epoch-value&gt; | platform creation_epoch]</td></tr><tr><td>解释</td><td>指定与轨道元素有效的参考历元相对应的历元。
如果指定了 platform creation_epoch, 初始历元将设置为平台的创建时间。
示例</td></tr><tr><td></td><td>//Example: platform creation_epoch usage
//In this case, initial epoch will be set to 1 hour after simulation start</td></tr><tr><td></td><td>platform test-oe WSF PLATFORM
creation_time 1 hour
add mover WSF_SPACE_MOVER
orbital_state
    epoch platform creation_epoch
semimajor_axis 10000 km
eccentricity 0.2
mean_anomaly 255 deg
inclination 30 deg
raan 120 deg
argument_of_periapsis 80 deg</td></tr><tr><td></td><td>end_orbital_state
end_mover
endPLATFORM</td></tr><tr><td>命令</td><td>epoch_date_time &lt;month&gt;&lt;day-of-month&gt;&lt;year&gt;&lt;hh:mm:ss&gt;</td></tr><tr><td>解释</td><td>指定与轨道元素有效的参考历元相对应的日期和时间。
注意 月份使用如下三字符格式表示：jan | feb | mar | apr | may | jun | jul | aug | sep | oct | nov | dec
一天中的时间参考 UT 午夜，并使用 24 小时制。</td></tr></table>

轨道元素命令   

<table><tr><td>命令</td><td>designator &lt;string-value&gt;</td></tr><tr><td>解释</td><td>指定空间移动器的标识符。默认值:“00001A”注意 如果使用 TLE,标识符由 TLE 卫星国际标识符在第一行提供。</td></tr><tr><td>命令</td><td>eccentricity &lt;real-value&gt;</td></tr><tr><td>解释</td><td>指定轨道的偏心率。指定的值必须大于或等于零(圆形轨道)。默认值:0注意 对于 WSF_SPACE_MOV 和 WSF_NORAD_SPACE_MOV,偏心率还必须小于 1.0(抛物线轨道)。</td></tr><tr><td>命令</td><td>semimajor_axis &lt;length-value&gt;</td></tr><tr><td>解释</td><td>指定定义轨道的椭圆的半长轴。默认值:无。必须提供此值或从其他命令派生。参见轨道元素输入值的派生。注意 对于偏心率为零,半长轴成为圆的半径。注意 此输入等同于 revolutions_per_day,因为两者通过开普勒第三定律相关。如果两者都指定,则使用最后一个指定的。</td></tr><tr><td>命令</td><td>revolutions_per_day &lt;real-value&gt;</td></tr><tr><td>解释</td><td>指定卫星每天绕地球的圈数。默认值:无。必须提供此值或从其他命令派生。参见轨道元素输入值的派生。注意 此输入等同于 semiajor_axis,因为两者通过开普勒第三定律相关。如果两者都指定,则使用最后一个指定的。</td></tr><tr><td>命令</td><td>periapsis_radius &lt;length-value&gt;</td></tr><tr><td>解释</td><td>指定定义轨道的椭圆的近地点半径。这是卫星与中心体中心之间的最小距离。默认值:无。必须提供此值或从其他命令派生。参见轨道元素输入值的派生。注意 对于偏心率为零,近地点半径等于远地点半径和半长轴。注意 此输入等同于 periapsis_altitude,因为两者通过中心体的平均半径相关。如果两者都指定,则使用最后一个指定的。</td></tr><tr><td>命令</td><td>apoapsis_radius &lt;length-value&gt;</td></tr><tr><td>解释</td><td>指定定义轨道的椭圆的远地点半径。这是卫星与中心体中心之间的最大距离。默认值:无。必须提供此值或从其他命令派生。参见轨道元素输入值的派生。注意 对于偏心率为零,远地点半径等于近地点半径和半长轴。注意 此输入等同于 apoapsis_altitude,因为两者通过中心体的平均半径相关。如果两者都指定,则使用最后一个指定的。</td></tr><tr><td>命令</td><td>periapsis_altitude &lt;length-value&gt;</td></tr><tr><td>解释</td><td>指定定义轨道的椭圆的近地点高度。这是卫星与中心体表面之间的最小距离。默认值:无。必须提供此值或从其他命令派生。参见轨道元素输入值的派生。注意 对于偏心率为零,近地点高度等于远地点高度。注意 此输入等同于 periapsis_altitude,因为两者通过中心体的平均半径相关。如果两者都指定,则使用最后一个指定的。</td></tr><tr><td>命令</td><td>apoapsis_altitude &lt;length-value&gt;</td></tr><tr><td>解释</td><td>指定定义轨道的椭圆的远地点高度。这是卫星与中心体表面之间的最大距离。默认值:无。必须提供此值或从其他命令派生。参见轨道元素输入值的派生。注意 对于偏心率为零,远地点高度等于近地点高度。注意 此输入等同于 apoapsis_altitude,因为两者通过中心体的平均半径相关。如果两者都指定,则使用最后一个指定的。</td></tr><tr><td>命令</td><td>raan | right ascension_ofascending_node &lt;angle-value&gt;</td></tr><tr><td>解释</td><td>指定升交点的赤经(“raan”)。这是沿天赤道从春分点(赤经角)逆时针测量的卫星从南向北穿过赤道(升交点)的角度。
默认值:0度
注意raan值必须大于或等于零且小于360度(2π弧度)。注意raan参考于真日期坐标系。</td></tr><tr><td>命令</td><td>inclination&lt;angle-value&gt;</td></tr><tr><td>解释</td><td>指定轨道平面切线与地球自转轴的分离角。
默认值:0度
注意倾角值必须大于或等于零(赤道轨道)且小于或等于180度(π弧度;逆行赤道轨道)。注意倾角参考于真日期坐标系。</td></tr><tr><td>命令</td><td>mean_anomaly&lt;angle-value&gt;</td></tr><tr><td>解释</td><td>指定卫星在历元时间的轨道中的角位置。此角度从近地点测量,表示卫星以恒定角速度遍历的角度。
默认值:0度
注意平近点角值必须大于或等于零且小于360度(2π弧度)。注意此输入等同于真近点角。参见轨道元素输入值的派生。</td></tr><tr><td>命令</td><td>true_anomaly&lt;angle-value&gt;</td></tr><tr><td>解释</td><td>指定卫星在历元时间的轨道中的角位置。此角度从近地点测量,表示卫星的真实角位置。
默认值:0度
注意真近点角值必须大于或等于零且小于360度(2π弧度)。注意此输入等同于平近点角。参见轨道元素输入值的派生。</td></tr><tr><td>命令</td><td>argument_of_periapsis&lt;angle-value&gt;</td></tr><tr><td>解释</td><td>指定近地点相对于地球表面的角度。此角度从升交点测量。
默认值:0度
注意近地点角值必须大于或等于零且小于360度(2π弧度)。</td></tr><tr><td>命令</td><td>descriptor&lt;string-value&gt;</td></tr><tr><td>解释</td><td>指定空间飞行器的任意描述符(标签)。
注意如果使用TLE,描述符在第0行提供。</td></tr></table>

# 轨道元素输入值的解析

对于某些轨道元素，有多种方式可以指定轨道的特定特征。

符号与命令对照表

<table><tr><td>Symbol</td><td>Command</td></tr><tr><td>N</td><td>revolutions_per_day</td></tr><tr><td>a</td><td>semimajor_axis</td></tr><tr><td>e</td><td>eccentricity</td></tr><tr><td>rp</td><td>periapsis_radius</td></tr><tr><td>ra</td><td>apoapsis_radius</td></tr><tr><td>zp</td><td>periapsis_altitude</td></tr><tr><td>za</td><td>apoapsis_altitude</td></tr><tr><td>M</td><td>mean_anomaly</td></tr><tr><td>f</td><td>true_anomaly</td></tr></table>

# 轨道大小/形状

命令 semi_major_axis 和 revolutions_per_day 是等效输入，因为它们通过开普勒第三定律相关：

$$
N = \frac {d}{2 \pi} \sqrt {\frac {\mu}{a ^ {3}}}
$$

其中：

?是一天中的秒数（86400）  
$\mu$ 是中心体的引力常数

![](images/04808f3d13ce374dee1e142a5f21170e69206f99caa6f7199ae100f5bc0f0b6a.jpg)

命令 periapsis_radius（近地点半径）和 periapsis_altitude（近地点高度）是等效的输入，因 为 它 们 通 过 中 心 天 体 的 半 径 相 关 联 。 同 样 ， apoapsis_radius （ 远 地 点 半 径 ） 和apoapsis_altitude（远地点高度）也是如此。请参见上图和以下公式：

$$
r _ {p} = R + z _ {p}
$$

$$
r _ {a} = R + z _ {a}
$$

其中，R 是 central_body(中心天体)的平均半径。

# 轨道参数之间的关系

近地点半径（periapsis_radius）、远地点半径（apoapsis_radius）、偏心率（eccentricity）和半长轴（semi_major_axis）之间的关系如下：

$$
r _ {p} = a (1 - e)
$$

$$
r _ {a} = a (1 + e)
$$

这两个方程中有四个未知数；如果指定其中的两个，另外两个也可以确定。如果只指定一个参数，则假设偏心率（e）为零，仍然可以确定所有四个参数。

# 平均近点角和真近点角

命令 mean_anomaly（平均近点角）和 true_anomaly（真近点角）是等效的输入，它们通过以下方程相关联：

$$
M = E - e \sin E
$$

$$
\cos E = \frac {e + c o s f}{1 + e c o s f}
$$

其中：

。 E 是偏近点角（eccentric anomaly），如下图所示。  
f是真近点角（trueanomaly），如下图所示。  
M 是平均近点角（meananomaly），从近地点测量，表示卫星以恒定角速度遍历

的角度。

通过这些公式，可以更好地理解和计算轨道参数，从而进行轨道仿真和分析。

![](images/a51964224f62ffe0c30b314a7cf68ebfa2f0b5c30daccb7b996f71d9ef0c1e16.jpg)  
此 图 来 自 ： Eccentric and true anomaly.PNG ， CC BY-SA 4.0https://commons.wikimedia.org/w/index.php?curid=48384905

<table><tr><td>命令</td><td>position &lt; waypoint&gt;</td></tr><tr><td>解释</td><td>指定一个航点作为定义轨道路径的替代方法（即，代替轨道...结束轨道块）。如果没有指定速度，平台将被放置在一个圆形轨道上；否则，将使用航点中指定的速度来生成轨道。使用此方法时，请记住以下几点：·低地球轨道（LEO）通常在400公里以上的高度。·地球同步轨道（GEO）位于22,240英里（或35786公里）的高度，倾角为零（航向=90度）。·轨道通常具有发射纬度的倾角（航向=90-发射纬度）。·轨道通常是顺行的（航向在0到180度之间）。//Example: Geostationary satellite platform test-geo WSF PLATFORM add mover WSF_SPACE_MOVER position On 90w altitude 22240 mi heading 90 degrees end mover endplatform //Example: LEO satellite platform test-leo WSFPLATFORM add mover WSF_SPACE_MOVER position On 90w altitude 450 km heading 60 degrees end mover endplatform</td></tr><tr><td>命令</td><td>initial_state_Ila &lt;lat&gt;&lt;lon&gt;&lt;alt&gt;&lt;velN&gt;&lt;velE&gt;&lt;velD&gt;</td></tr><tr><td>解释</td><td>以位置和速度指定平台的初始状态。位置以纬度、经度、高度格式表示；速度在本地的北、东、下框架中表示。此输入类似于上面的position输入，但在这种情况下，它完全指定了物体的物理状态。</td></tr><tr><td>命令</td><td>initial_state_eci &lt;locX&gt;&lt;locY&gt;&lt;locZ&gt;&lt;velX&gt;&lt;velY&gt;&lt;velZ&gt;</td></tr><tr><td>解释</td><td>以位置和速度指定平台的初始状态。位置和速度在地心惯性（ECI）框架中表示。此输入类似于上面的position输入，但在这种情况下，它完全指定了物体的物理状态。</td></tr><tr><td>命令</td><td>oblate-earth &lt;boolean-value&gt;</td></tr><tr><td>解释</td><td>启用或禁用一阶扁球地球扰动。当启用时，模拟效果是两个天体和一个扁球地球的效果。当禁用时，效果是两个天体和一个球形地球的效果。
默认值：‘禁用’。</td></tr><tr><td>命令</td><td>orbit_color &lt;color-value&gt;</td></tr><tr><td>解释</td><td>指定轨道的颜色。
注意：即使指定了颜色的 alpha 分量，也不会使用。</td></tr></table>

# 两行根数（TLE）轨道

指定一个两行元素（TLE），用于定义平均轨道元素和其他用于传播卫星的数据。两行元素通常从现有资源中获取，例如 Spacetrak 数据库（http://www.space-track.org）或 Celestrak（http://www.celestrak.com/NORAD/elements）。与普通的 AFSIM 输入不同，列格式、字段长度和字符格式必须完全按照以下规定进行。

示例

TITLE INFORMATION:   
orbit \*<(optional) satellite descriptor> \* <first line of TLE $^ { \text{青} }$ \* <second line of TLE $^ { \text{青} }$ end_orbit

```txt
Line 1 Column Characters Description   
---- |--- |--- Line No. Identification   
1 1   
3 5   
8 1   
10 8   
19 14   
34 1   
35 9   
45 1   
46 5   
51 1   
52 1   
54 1   
55 5   
60 1   
61 1   
63 1   
65 4   
69 1 Check Sum, Modulo 10 
```

![](images/9bb9bcaa1575c4b601a89cf75224d2e4888ce4bbf1bdf97139a7171040319e9b.jpg)  
Vanguard-1 卫星的 TLE 示例

```txt
orbit  
100005U 58002B 09105.24506411 .00000084 00000-0 11810-3 0 4337  
200005 034.2551 191.5961 1850437 000.0334 000.0199 10.8399999762276  
end_orbit 
```

注意：WSF_SPACE_MOVER 目前仅使用 TLE 中包含的经典轨道元素，并将其解释为瞬时元素，而不是平均元素。

注意：使用 Modify_tle_list Perl 脚本将 TLE 列表转换为 AFSIM 平台列表。

轨道传播器命令  

<table><tr><td>命令</td><td>central_body &lt;central-body-type&gt;
    polar_offsetAngles
end_central_body</td></tr><tr><td>解释</td><td>指定模拟平台使用的中心天体及相关椭球模型。&lt;central_body_type&gt;的选项如下:
earth_wgs72（地球世界大地测量系统1972）：中心天体椭球根据WGS-72标准定义。
earth_wgs84（地球世界大地测量系统1984）：中心天体椭球根据WGS-84标准定义。
earth_egm96（地球重力模型1996）：中心天体椭球根据EGM-96标准定义。
moon（月球）：中心天体椭球根据已发布的月球参数定义。
sun（太阳）：中心天体椭球根据已发布的太阳参数定义。
jupiter（木星）：中心天体椭球根据已发布的木星参数定义。
默认值：earth_wgs84
polar_offsetAngles &lt;角度值&gt;&lt;角度值&gt;
指定中心天体的极偏移角（分别为x_p和y_p），相对于WCS（ITRS）坐标系统的天体中间极（CIP）。提供这些值（约为十分之一角秒）可以实现ECI和WCS坐标之间的高精度转换。
默认值：0.0弧度0.0弧度
注意：WCS-&gt;LLA转换受中心天体选择的影响，以及在惯性（ECI）坐标转换中计算的恒星运动变换。</td></tr></table>

# 已弃用的轨道传播器命令

egm_96

wgs_84

heliocentric

指定使用 wgs_84 重力参数、egm_96 重力参数或日心重力参数进行传播。日心选项用于模拟围绕太阳运行的天体。

注意：此设置仅对 WSF_SPACE_MOVER 有效。

默认值：wgs_84

自版本 2.9 起已弃用：以下调试输出命令将在未来版本中删除。

debug_output_wsf <布尔值> 将附加信息写入标准输出，可由 CME 工具“sedit”处理。

debug_output_oe <布尔值> 将有关轨道元素的附加信息写入标准输出。

debug_output_stk <布尔值> 将附加信息写入标准输出，可用于与 Analytical Graphics, Inc.的系统工具包（STK）进行轨道比较。

debug_output_xyz <布尔值> 将附加信息写入标准输出，可用于与 Analytical Graphics, Inc.的系统工具包（STK）进行轨道比较。

# 合相设置命令

<table><tr><td>命令</td><td>conjunction_setup&lt;initial-position-specification&gt;with_target&lt;target-platform&gt;at_time&lt;time&gt;end_conjunction_setup</td></tr><tr><td>解释</td><td>设置该航天器的初始条件,以便在指定时间与给定目标航天器发生合相。在初始化期间,将尝试找到符合给定边界条件的解决方案。如果成功,将设置该平台的状态以使指定的合相发生。如果没有解决方案(例如,轨道会使卫星穿过地球),则将航天器的速度设置为默认值(见下文)。初始位置规范如下之一:from_lla&lt;纬度值&gt;&lt;经度值&gt;&lt;高度值&gt;将该航天器的初始位置设置为给定的纬度、经度和高度。如果没有合相解决方案,将航天器的速度设置为航向为90度的圆形轨道的速度。from_eci&lt;长度值&gt;&lt;长度值&gt;&lt;长度值&gt;将该航天器的初始位置设置为ECI框架中的给定位置。如果没有合相解决方案,将航天器的速度设置为航向为90度的圆形轨道的速度。from.initial 使用其他方法设置该航天器的初始位置,以指定航天器的初始轨道。如果没有合相解决方案,将航天器的速度设置为其他初始化方法提供的速度。with_target&lt;字符串值&gt;指定合相目标平台的名称。该航天器将在at_time命令指定的时间移动到目标平台的位置。指定的目标必须是一个在空间域中移动的平台的名称。at_time&lt;时间值&gt;指定该航天器应在指定时间与指定目标发生合相。tolerance&lt;实数值&gt;指定合相解决方案的容差。默认容差值为1.0e-9。注意:WCS-&gt;LLA转换受中心天体选择的影响,以及在惯性(ECI)坐标转换中计算的恒星运动变换。</td></tr></table>

# 姿态控制命令

姿态控制命令参见 3.6.5.1.1 姿态控制模型 Attitude Controller Models：

姿态控制器用于指定平台的姿态控制器。所有具有 WSF_SPACE_MOVER 或WSF_NORAD_SPACE_MOVER 的平台都会有某种姿态控制器。如果没有指定姿态控制器块，移动器将以选择即时姿态控制器的方式运行。

姿态控制器将尝试改变平台的方向以匹配给定的目标方向。在创建时，姿态控制器将通过 姿 态 控 制 器 块 中 的 方 向 命 令 指 定 目 标 方 向 。 创 建 后 ， 可 以 通 过WsfSpaceMover.SetOrientation 更改姿态控制器的方向目标。

目标方向可以是一次性选择的目标方向，或者将姿态控制器连接到预设的方向类型之一。在后一种情况下，随着航天器沿其轨道移动，姿态控制器将具有不断更新的目标方向。

可用的模型包括：

3.6.5.1.1.2 即时姿态控制器

3.6.5.1.1.3 速率限制姿态控制器

在执行机动时，需要检查以确保有足够的燃料供应。当机动执行时，推进剂被消耗，火箭阶段的质量属性会更新。

# 轨道机动命令

轨道机动命令参见：3.6.5.1.2 轨道机动模型 Orbital Maneuvering Models。

轨道机动模型 用于在太空中执行轨道机动。这些模型用于改变航天器的轨道。根据提供的信息，简单机动模型和火箭机动模型是可用的选项。火箭机动模型通常涉及使用火箭发动机来执行轨道插入、轨道圆化、轨道转移、交会、脱轨等操作。

可用的模型包括：

3.6.5.1.2.2 简单机动模型

3.6.5.1.2.3 火箭机动模型

# 轨道任务序列

```txt
mission_sequence <constraint> event Common Mission Event Commands mission event-specific commands ... end_event ... additional mission event definitions end_mission_sequence 
```

指定任务序列，参考：3.6.5.1.3 轨道任务序列 Orbital Mission Sequence。

示例

```txt
// Example: Two mission events to raise a satellite  
// from an initial injection point  
// into a geosynchronous transfer orbit (GTO)  
mission_sequence  
// Constraint: delay two full orbits before executing 
```

execute_at orbit 2 relative_time 0.0 s  
// intermediate orbit  
event change(semimajor_axis semi major axis $9000\mathrm{km}$ execute_at orbit 2 ascending_node // Constraint with orbit delay end_event  
// GTO  
maneuver change(semi major_axis // "maneuver ... end maneuver" block may be used with orbital maneuver types. semi major axis 24821 km execute_at ascending_node // Constraint without orbit delay end_maneuver  
end_missio_sequence

轨 道 任 务 事 件 和 任 务 事 件 序 列 可 以 使 用 脚 本 方 法 WsfSpaceMover.ExecuteEvent（WsfSpaceMover.ExecuteManeuver）和 WsfSpaceMover.ExecuteMissionSequence 进行脚本化。

# 脚本接口

WSF_SPACE_MOVER 使用通用脚本接口（4.1 公共脚本接口 Common Script Interface），并提供隐式定义的引用 SPACE_MOVER，这允许在不进行类型转换的情况下调用WsfSpaceMover 方法。

# 3.6.5.3. NORAD 空间运动模型 WSF_NORAD_SPACE_MOVER

```txt
mover <name> WSF_NORAD_SPACE_MOVER  
... base mover commands...  
... Orbital Element Commands...  
... Orbital Propagator Commands...  
orbit_color ...  
conjunction_setup  
...  
end_conjunction_setup  
attitude_controller <type-name> ...  
...  
end Attitude_controller  
maneuvering <type-name> ...  
...  
end_maneuvering  
mission_sequence  
...  
end_mission_sequence 
```

```txt
orbital_state ... end_ orbital_state end_mover 
```

WSF_NORAD_SPACE_MOVER 实现了一个用于地球轨道平台的移动器。它对于建模那些有两行元素（TLE）集可用的卫星非常有用，包括大多数在轨运行的地球卫星、非运行卫星和被积极跟踪的轨道碎片。

该 移 动 器 实 现 了 在 《 SpaceTrack Report No. 3 》 中 定 义 的 传 播 算 法（https://www.celestrak.com/NORAD/documentation/spacetrk.pdf）。该报告提供了定义几种模型的算法；移动器根据两行元素中提供的数据选择适当的模型（NORADSGP、SGP4、SGP8、SDP4 或 SDP8）进行传播。这些模型考虑了地球的扁平化、阻力以及太阳和月球的第三体扰动效应。

WSF_NORAD_SPACE_MOVER 能够执行各种机动。机动可以通过 mission_sequence 输入指定，或者可以通过 WsfSpaceMover 脚本对象和移动器的脚本接口进行脚本化。可配置的机动模型决定了在执行机动的任务序列中如何消耗速度增量（delta-V）。

移动器的取向由可配置的姿态控制器模型指定和控制。提供了多种标准取向选项，并且取向也可以通过脚本动态更改。

注意：应在场景中定义 start_date 和 start_time 或 start_epoch 命令，因为它们是正确计算星历数据所必需的。

注意：尽管 WSF_NORAD_SPACE_MOVER 支持大多数机动类型，但目前不支持更改升交点赤经（RAAN）和更改升交点赤经（RAAN）和倾角的机动。

# 轨道状态命令

<table><tr><td>命令</td><td>orbital_state...end_orbital_state</td></tr><tr><td>解释</td><td>指定轨道状态的形式为一个 epoch 或 epoch_date_time,并且包含以下之一:足够的轨道元素命令位置和速度向量包含两行元素(TLE)的轨道命令块(当使用WSF_NORAD_SPACE_MOVER时)position &lt;real&gt;&lt;real&gt;&lt;length-units&gt;设置空间移动器的初始位置。此命令必须与速度命令一起使用。velocity &lt;real&gt;&lt;real&gt;&lt;speed-units&gt;设置空间移动器的初始速度。此命令必须与位置命令一起使用。注意事项位置和速度输入必须按顺序提供,速度输入必须紧跟在位置输入之后。示例//Example: Orbital elements declarationplatform test-oe WSFPLATFORMadd mover WSF_SPACE_MOVORb orbital_stateepoch 2021245.18563semi major axis 10000 kmeccentricity 0.2mean_anomaly 255 deginclination 30 degraan 120 deg</td></tr><tr><td></td><td>argument_of_periapsis 80 deg
end_orbital_state
end_mover
endPLATFORM
//Example: Position/velocity declaration
platform test-rv WSF PLATFORM
add mover WSF_SPACE_MOVEROBital_state
    epoch 2021245.18563
    position 800 0 0 km
    velocity 100 3000 -50 m/s
    end_orbital_state
    end_mover
    endPLATFORM
//Example: TLE declaration
//Note: TLE declaration is only allowed within a WSF_NORAD_SPACE_MOVERO
platform test-tle WSF PLATFORM
    add mover WSF_NORAD_SPACE_MOVEROBital_state
    orbit
        0 HST
        1 20580U 90037B 20216.30423610 .00000333 00000-0 92680-5 0
9996
        2 20580 28.4681 168.2117 0002666 190.3324 294.3699 15.09238375401891
        end_orbit
        end_orbital_state
        end_mover
        endPLATFORM</td></tr><tr><td>命令</td><td>epoch [&lt;epoch-value&gt; | platform creation_epoch]</td></tr><tr><td>解释</td><td>指定与轨道元素有效的参考历元相对应的历元。
如果指定了 platform creation_epoch, 初始历元将设置为平台的创建时间。
示例</td></tr><tr><td></td><td>//Example: platform creation_epoch usage
//In this case, initial epoch will be set to 1 hour after simulation start</td></tr><tr><td></td><td>platform test-oe WSF PLATFORM
creation_time 1 hour
add mover WSF_SPACE_MOVEROBital_state
    epoch platform creation_epoch
semimajor_axis 10000 km
eccentricity 0.2
mean_anomaly 255 deg
inclination 30 deg
raan 120 deg
argument_of_periapsis 80 deg
end_orbital_state
end_mover
endPLATFORM</td></tr><tr><td>命令</td><td>epoch_date_time &lt;month&gt;&lt;day-of-month&gt;&lt;year&gt;&lt;hh:mm:ss&gt;</td></tr><tr><td>解释</td><td>指定与轨道元素有效的参考历元相对应的日期和时间。
注意 月份使用如下三字符格式表示：jan | feb | mar | apr | may | jun | jul | aug | sep | oct | nov | dec
一天中的时间参考 UT 午夜，并使用 24 小时制。</td></tr></table>

轨道元素命令   

<table><tr><td>命令</td><td>designator &lt;string-value&gt;</td></tr><tr><td>解释</td><td>指定空间移动器的标识符。默认值:“00001A”注意 如果使用 TLE,标识符由 TLE 卫星国际标识符在第一行提供。</td></tr><tr><td>命令</td><td>eccentricity &lt;real-value&gt;</td></tr><tr><td>解释</td><td>指定轨道的偏心率。指定的值必须大于或等于零(圆形轨道)。默认值:0注意 对于 WSF_SPACE_MOV 和 WSF_NORAD_SPACE_MOV,偏心率还必须小于1.0(抛物线轨道)。</td></tr><tr><td>命令</td><td>semi major_axis &lt;length-value&gt;</td></tr><tr><td>解释</td><td>指定定义轨道的椭圆的半长轴。默认值:无。必须提供此值或从其他命令派生。参见轨道元素输入值的派生。注意 对于偏心率为零,半长轴成为圆的半径。 注意 此输入等同于 revolutions_per_day,因为两者通过开普勒第三定律相关。如果两者都指定,则使用最后一个指定的。</td></tr><tr><td>命令</td><td>revolutions_per_day &lt;real-value&gt;</td></tr><tr><td>解释</td><td>指定卫星每天绕地球的圈数。默认值:无。必须提供此值或从其他命令派生。参见轨道元素输入值的派生。注意 此输入等同于 semi major_axis,因为两者通过开普勒第三定律相关。如果两者都指定,则使用最后一个指定的。</td></tr><tr><td>命令</td><td>periapsis_radius &lt;length-value&gt;</td></tr><tr><td>解释</td><td>指定定义轨道的椭圆的近地点半径。这是卫星与中心体中心之间的最小距离。默认值:无。必须提供此值或从其他命令派生。参见轨道元素输入值的派生。注意 对于偏心率为零,近地点半径等于远地点半径和半长轴。 注意 此输入等同于periapsis_altitude,因为两者通过中心体的平均半径相关。如果两者都指定,则使用最后一个指定的。</td></tr><tr><td>命令</td><td>apoapsis_radius &lt;length-value&gt;</td></tr><tr><td>解释</td><td>指定定义轨道的椭圆的远地点半径。这是卫星与中心体中心之间的最大距离。默认值:无。必须提供此值或从其他命令派生。参见轨道元素输入值的派生。注意 对于偏心率为零,远地点半径等于近地点半径和半长轴。 注意 此输入等同于apoapsis_altitude,因为两者通过中心体的平均半径相关。如果两者都指定,则使用最后一个指定的。</td></tr><tr><td>命令</td><td>periapsis_altitude &lt;length-value&gt;</td></tr><tr><td>解释</td><td>指定定义轨道的椭圆的近地点高度。这是卫星与中心体表面之间的最小距离。默认值:无。必须提供此值或从其他命令派生。参见轨道元素输入值的派生。注意 对于偏心率为零,近地点高度等于远地点高度。 注意 此输入等同于periapsis_altitude,因为两者通过中心体的平均半径相关。如果两者都指定,则使用最后一个指定的。</td></tr><tr><td>命令</td><td>apoapsis_altitude &lt;length-value&gt;</td></tr><tr><td>解释</td><td>指定定义轨道的椭圆的远地点高度。这是卫星与中心体表面之间的最大距离。默认值:无。必须提供此值或从其他命令派生。参见轨道元素输入值的派生。注意 对于偏心率为零,远地点高度等于近地点高度。 注意 此输入等同于apoapsis_altitude,因为两者通过中心体的平均半径相关。如果两者都指定,则使用最后一个指定的。</td></tr><tr><td>命令</td><td>raan | right ascension_ofascending_node &lt;angle-value&gt;</td></tr><tr><td>解释</td><td>指定升交点的赤经(“raan”)。这是沿天赤道从春分点(赤经角)逆时针测量的卫星从南向北穿过赤道(升交点)的角度。默认值:0度注意 raan 值必须大于或等于零且小于360度(2π弧度)。注意 raan 参考于真日</td></tr><tr><td></td><td>期坐标系。</td></tr><tr><td>命令</td><td>inclination &lt;angle-value&gt;</td></tr><tr><td>解释</td><td>指定轨道平面切线与地球自转轴的分离角。默认值:0度注意倾角值必须大于或等于零(赤道轨道)且小于或等于180度(π弧度;逆行赤道轨道)。注意倾角参考于真日期坐标系。</td></tr><tr><td>命令</td><td>mean_anomaly &lt;angle-value&gt;</td></tr><tr><td>解释</td><td>指定卫星在历元时间的轨道中的角位置。此角度从近地点测量,表示卫星以恒定角速度遍历的角度。默认值:0度注意平近点角值必须大于或等于零且小于360度(2π弧度)。注意此输入等同于真近点角。参见轨道元素输入值的派生。</td></tr><tr><td>命令</td><td>true_anomaly &lt;angle-value&gt;</td></tr><tr><td>解释</td><td>指定卫星在历元时间的轨道中的角位置。此角度从近地点测量,表示卫星的真实角位置。默认值:0度注意真近点角值必须大于或等于零且小于360度(2π弧度)。注意此输入等同于平近点角。参见轨道元素输入值的派生。</td></tr><tr><td>命令</td><td>argument_of_periapsis &lt;angle-value&gt;</td></tr><tr><td>解释</td><td>指定近地点相对于地球表面的角度。此角度从升交点测量。默认值:0度注意近地点角值必须大于或等于零且小于360度(2π弧度)。</td></tr><tr><td>命令</td><td>descriptor &lt;string-value&gt;</td></tr><tr><td>解释</td><td>指定空间飞行器的任意描述符(标签)。注意如果使用TLE,描述符在第0行提供。</td></tr></table>

# 轨道元素输入值的解析

对于某些轨道元素，有多种方式可以指定轨道的特定特征。

符号与命令对照表  

<table><tr><td>Symbol</td><td>Command</td></tr><tr><td>N</td><td>revolutions_per_day</td></tr><tr><td>a</td><td>semimajor_axis</td></tr><tr><td>e</td><td>eccentricity</td></tr><tr><td>rp</td><td>periapsis_radius</td></tr><tr><td>ra</td><td>apoapsis_radius</td></tr><tr><td>zp</td><td>periapsis_altitude</td></tr><tr><td>za</td><td>apoapsis_altitude</td></tr><tr><td>M</td><td>mean_anomaly</td></tr><tr><td>f</td><td>true_anomaly</td></tr></table>

# 轨道大小/形状

命令 semi_major_axis 和 revolutions_per_day 是等效输入，因为它们通过开普勒第三定律相关：

$$
N = \frac {d}{2 \pi} \sqrt {\frac {\mu}{a ^ {3}}}
$$

其中：

?是一天中的秒数（86400）  
$\mu$ 是中心体的引力常数

![](images/fd1894c85e548baeecb44c234bb17e153281484a4339d56e62810a7f03593b88.jpg)

命令 periapsis_radius（近地点半径）和 periapsis_altitude（近地点高度）是等效的输入，因 为 它 们 通 过 中 心 天 体 的 半 径 相 关 联 。 同 样 ， apoapsis_radius （ 远 地 点 半 径 ） 和apoapsis_altitude（远地点高度）也是如此。请参见上图和以下公式：

$$
r _ {p} = R + z _ {p}
$$

$$
r _ {a} = R + z _ {a}
$$

其中，R 是 central_body(中心天体)的平均半径。

# 轨道参数之间的关系

近地点半径（periapsis_radius）、远地点半径（apoapsis_radius）、偏心率（eccentricity）和半长轴（semi_major_axis）之间的关系如下：

$$
r _ {p} = a (1 - e)
$$

$$
r _ {a} = a (1 + e)
$$

这两个方程中有四个未知数；如果指定其中的两个，另外两个也可以确定。如果只指定一个参数，则假设偏心率（e）为零，仍然可以确定所有四个参数。

# 平均近点角和真近点角

命令 mean_anomaly（平均近点角）和 true_anomaly（真近点角）是等效的输入，它们通过以下方程相关联：

$$
M = E - e \sin E
$$

$$
\cos E = \frac {e + c o s f}{1 + e c o s f}
$$

其中：

E 是偏近点角（eccentric anomaly），如下图所示。  
f是真近点角（trueanomaly），如下图所示。  
M 是平均近点角（meananomaly），从近地点测量，表示卫星以恒定角速度遍历的角度。

通过这些公式，可以更好地理解和计算轨道参数，从而进行轨道仿真和分析。

![](images/98aadf7ce0f12213a90318eaab2fdcbeeaf3fc3957f04d61bfd0aa4870659d12.jpg)

此 图 来 自 ： Eccentric and true anomaly.PNG ， CC BY-SA 4.0https://commons.wikimedia.org/w/index.php?curid=48384905

<table><tr><td>命令</td><td>orbit_color &lt;color-value&gt;</td></tr><tr><td>解释</td><td>指定轨道的颜色。
注意：即使指定了颜色的 alpha 分量，也不会使用。</td></tr></table>

# 两行根数（TLE）轨道

指定一个两行元素（TLE），用于定义平均轨道元素和其他用于传播卫星的数据。两行元素通常从现有资源中获取，例如 Spacetrak 数据库（http://www.space-track.org）或 Celestrak（http://www.celestrak.com/NORAD/elements）。与普通的 AFSIM 输入不同，列格式、字段长度和字符格式必须完全按照以下规定进行。

示例

orbit \*<(optional) satellite descriptor $>$ \* <first line of TLE $>$ \* <second line of TLE $>$ end_orbit

# TITLE INFORMATION:

```txt
Line 1 Column Characters Description ----|---|--- 1 1 Line No. Identification 3 5 Catalog No. 8 1 Security Classification 10 8 International Identification 19 14 YRDOY.FODdddd 
```

Vanguard-1 卫星的 TLE 示例  
```txt
34 1 Sign of first time derivative   
35 9 1st Time Derivative   
45 1 Sign of 2nd Time Derivative   
46 5 2nd Time Derivative   
51 1 Sign of 2nd Time Derivative Exponent   
52 1 Exponent of 2nd Time Derivative   
54 1 Sign of Bstar/Drag Term   
55 5 Bstar/Drag Term   
60 1 Sign of Exponent of Bstar/Drag Term   
61 1 Exponent of Bstar/Drag Term   
63 1 Ephemeris Type   
65 4 Element Number   
69 1 Check Sum, Modulo 10   
Line 2 Column Characters Description.   
--- |--- |---- Line No. Identification   
1 1   
3 5 Catalog No.   
9 8 Inclination   
18 8 Right Ascension of Ascending Node   
27 7 Eccentricity with assumed leading decimal   
35 8 Argument of the Perigee   
44 8 Mean Anomaly   
53 11 Revolutions per Day (Mean Motion)   
64 5 Revolution Number at Epoch   
69 1 Check Sum Modulo 10 
```

```txt
orbit  
100005U 58002B 09105.24506411 .00000084 00000-0 11810-3 0 4337  
200005 034.2551 191.5961 1850437 000.0334 000.0199 10.83999999762276  
end_orbit 
```

注意：WSF_SPACE_MOVER 目前仅使用 TLE 中包含的经典轨道元素，并将其解释为瞬时元素，而不是平均元素。

注意：使用 Modify_tle_list Perl 脚本将 TLE 列表转换为 AFSIM 平台列表。

轨道传播器命令  
```txt
命令 central_body <central-body-type> polar_offsetAngles end_central_body  
解释 指定模拟平台使用的中心天体及相关椭球模型。<central body type>的选项如下：
```

<table><tr><td></td><td>earth_wgs72（地球世界大地测量系统1972）：中心天体椭球根据WGS-72标准定义。earth_wgs84（地球世界大地测量系统1984）：中心天体椭球根据WGS-84标准定义。earth_egm96（地球重力模型1996）：中心天体椭球根据EGM-96标准定义。moon（月球）：中心天体椭球根据已发布的月球参数定义。sun（太阳）：中心天体椭球根据已发布的太阳参数定义。jupiter（木星）：中心天体椭球根据已发布的木星参数定义。默认值：earth_wgs84polar_offsetAngles&lt;角度值&gt;&lt;角度值&gt;指定中心天体的极偏移角（分别为x_p和y_p），相对于WCS（ITRS）坐标系统的天体中间极（CIP）。提供这些值（约为十分之一角秒）可以实现ECI和WCS坐标之间的高精度转换。默认值：0.0弧度0.0弧度注意：WCS-&gt;LLA转换受中心天体选择的影响，以及在惯性（ECI）坐标转换中计算的恒星运动变换。</td></tr></table>

# 已弃用的轨道传播器命令

egm_96

wgs_84

heliocentric

指定使用 wgs_84 重力参数、egm_96 重力参数或日心重力参数进行传播。日心选项用于模拟围绕太阳运行的天体。

注意：此设置仅对 WSF_SPACE_MOVER 有效。

默认值：wgs_84

自版本 2.9 起已弃用：以下调试输出命令将在未来版本中删除。

debug_output_wsf <布尔值> 将附加信息写入标准输出，可由 CME 工具“sedit”处理。

debug_output_oe<布尔值> 将有关轨道元素的附加信息写入标准输出。

debug_output_stk <布尔值> 将附加信息写入标准输出，可用于与 Analytical Graphics, Inc.的系统工具包（STK）进行轨道比较。

debug_output_xyz <布尔值> 将附加信息写入标准输出，可用于与 Analytical Graphics, Inc.的系统工具包（STK）进行轨道比较。

# 合相设置命令

<table><tr><td>命令</td><td>conjunction_setup
&lt;initial-position-specification&gt;
with_target &lt;target-platform&gt;
at_time &lt;time&gt;
end_conjunction_setup</td></tr><tr><td>解释</td><td>设置该航天器的初始条件，以便在指定时间与给定目标航天器发生合相。在初始化期间，将尝试找到符合给定边界条件的解决方案。如果成功，将设置该平台的状态以使指定的合相发生。如果没有解决方案（例如，轨道会使卫星穿过地球），则将航天器的速度设置为默认值（见下文）。
初始位置规范如下之一：
from_IIa &lt;纬度值&gt;&lt;经度值&gt;&lt;高度值&gt;将该航天器的初始位置设置为给定的纬度、经度和高度。如果没有合相解决方案，将航天器的速度设置为航向为90度的圆形轨道的速度。
from_eci &lt;长度值&gt;&lt;长度值&gt;&lt;长度值&gt;将该航天器的初始位置设置为ECI框架中的给定位置。如果没有合相解决方案，将航天器的速度设置为航向为90度的圆形轨道的速度。
from_init 使用其他方法设置该航天器的初始位置，以指定航天器的初始轨道。如</td></tr></table>

果没有合相解决方案，将航天器的速度设置为其他初始化方法提供的速度。

with_target <字符串值> 指定合相目标平台的名称。该航天器将在 at_time命令指定的时间移动到目标平台的位置。指定的目标必须是一个在空间域中移动的平台的名称。

at_time <时间值> 指定该航天器应在指定时间与指定目标发生合相。

tolerance <实数值> 指定合相解决方案的容差。默认容差值为 1.0e-9。

注意：WCS->LLA 转换受中心天体选择的影响，以及在惯性（ECI）坐标转换中计算的恒星运动变换。

# 姿态控制命令

姿态控制命令参见 3.6.5.1.1 姿态控制模型 Attitude Controller Models：

姿态控制器用于指定平台的姿态控制器。所有具有 WSF_SPACE_MOVER 或WSF_NORAD_SPACE_MOVER 的平台都会有某种姿态控制器。如果没有指定姿态控制器块，移动器将以选择即时姿态控制器的方式运行。

姿态控制器将尝试改变平台的方向以匹配给定的目标方向。在创建时，姿态控制器将通过 姿 态 控 制 器 块 中 的 方 向 命 令 指 定 目 标 方 向 。 创 建 后 ， 可 以 通 过WsfSpaceMover.SetOrientation 更改姿态控制器的方向目标。

目标方向可以是一次性选择的目标方向，或者将姿态控制器连接到预设的方向类型之一。在后一种情况下，随着航天器沿其轨道移动，姿态控制器将具有不断更新的目标方向。

可用的模型包括：

3.6.5.1.1.2 即时姿态控制器

3.6.5.1.1.3 速率限制姿态控制器

在执行机动时，需要检查以确保有足够的燃料供应。当机动执行时，推进剂被消耗，火箭阶段的质量属性会更新。

# 轨道机动命令

轨道机动命令参见：3.6.5.1.2 轨道机动模型 Orbital Maneuvering Models。

轨道机动模型 用于在太空中执行轨道机动。这些模型用于改变航天器的轨道。根据提供的信息，简单机动模型和火箭机动模型是可用的选项。火箭机动模型通常涉及使用火箭发动机来执行轨道插入、轨道圆化、轨道转移、交会、脱轨等操作。

可用的模型包括：

3.6.5.1.2.2 简单机动模型

3.6.5.1.2.3 火箭机动模型

# 轨道任务序列

```txt
mission_sequence <constraint> event Common Mission Event Commands mission event-specific commands ... end_event 
```

```txt
... additional mission event definitions end_mission_sequence 
```

指定任务序列，参考：3.6.5.1.3 轨道任务序列 Orbital Mission Sequence。

示例

```c
// Example: Two mission events to raise a satellite  
// from an initial injection point  
// into a geosynchronous transfer orbit (GTO)  
mission_sequence  
// Constraint: delay two full orbits before executing  
execute_at orbit 2 relative_time 0.0 s  
// intermediate orbit  
event change(semimajor_axis  
semi major axis 9000 km  
execute_at orbit 2 ascending_node // Constraint with orbit delay  
end_event  
// GTO  
maneuver change_semiMajor_axis // "maneuver ... end maneuver" block may be used  
with orbital maneuver types.  
semi major axis 24821 km  
execute_at ascending_node // Constraint without orbit delay  
end_maneuver  
end_missio_sequence 
```

轨 道 任 务 事 件 和 任 务 事 件 序 列 可 以 使 用 脚 本 方 法 WsfSpaceMover.ExecuteEvent（WsfSpaceMover.ExecuteManeuver）和 WsfSpaceMover.ExecuteMissionSequence 进行脚本化。

# 脚本接口

WSF_SPACE_MOVER 使用通用脚本接口（4.1 公共脚本接口 Common Script Interface），并提供隐式定义的引用 SPACE_MOVER，这允许在不进行类型转换的情况下调用WsfSpaceMover 方法。

# 3.6.5.4. 数值积分空间运动模型 WSF_INTEGRATING_SPACE_MOVER

```txt
mover <name> WSF_INTEGRATING_SPACE_MOVER  
... base mover commands ...  
... Orbital Element Commands ...  
attitude_controller <type-name> ...  
...  
end_attitude_controller 
```

```txt
conjunction_setup
...
end_conjunction_setup
maneuvering <type-name> ...
...
end_mechanuering
mission_sequence
...
end_mission_sequence
initial_state
...
end_initiallstate
integrator
...
end Integrator
dynamics
...
end_dynamics
orbital_state
...
end_orbital_state
# Script Interface
on_initiall... end_on_initiize
on_initiize2 ... end_on_initiize2
on_update ... end_on_update
script_variables ... endScript_variables
scripts ... end-script
... Other Script Commands ...
end mover 
```

WSF_INTEGRATING_SPACE_MOVER 概述

WSF_INTEGRATING_SPACE_MOVER 实现了一个用于空间域平台的移动器。不同于WSF_SPACE_MOVER 或 WSF_NORAD_SPACE_MOVER 使用解析模型来提供平台的未来状态，WSF_INTEGRATING_SPACE_MOVER 使用数值积分。通过使用用户指定的动态模型，该移动器不仅限于那两个移动器感兴趣的情况，即地球在动力学中起主导作用的传播。此外，WSF_INTEGRATING_SPACE_MOVER 支持双曲线传播，因此也可以用于表示非束缚轨道。

用户配置

使用 WSF_INTEGRATING_SPACE_MOVER 的用户需要选择一个积分器和一个动态模型，以完全指定此移动器的行为。积分器具体说明了平台状态如何在时间上进行数值传播。动态模型则指定平台将经历的力。

用户可以通过两种方式指定平台的初始状态：使用轨道元素命令，或通过 initial_state命令直接使用运动学。

动态模型允许包含依赖于平台质量的项，因此需要为平台指定质量。这可以通过显式设置平台质量，或使用火箭机动模型来实现。

机动能力

WSF_INTEGRATING_SPACE_MOVER 能够执行多种机动。机动可以通过 mission_sequence输入指定，或通过 WsfIntegratingSpaceMover 脚本对象和移动器的脚本接口进行编写。可配置的机动模型决定了在执行机动的任务序列中如何消耗 ΔV。

移动器的方向由可配置的姿态控制器模型指定和控制。提供了多种标准定向选项，并且可以通过脚本动态更改方向。

注意事项

场景中还应定义 start_date 和 start_time，或 start_epoch 命令，因为它们是正确计算星历数据所必需的。

尽管 WSF_INTEGRATING_SPACE_MOVER 支持大多数机动类型，但目前不支持更改升交点赤经（RAAN）和更改升交点赤经（RAAN）及倾角。

# 轨道状态命令

```txt
命令 orbital_state...end_orbital_state  
解释 指定轨道状态的形式为一个 epoch 或 epoch_date_time，并且包含以下之一：足够的轨道元素命令位置和速度向量包含两行元素（TLE）的轨道命令块（当使用WSF_NORAD_SPACE_MOVER时）position <real><real><length-units>设置空间移动器的初始位置。此命令必须与速度命令一起使用。velocity <real><real><speed-units>设置空间移动器的初始速度。此命令必须与位置命令一起使用。注意事项位置和速度输入必须按顺序提供，速度输入必须紧跟在位置输入之后。示例//Example:Orbital elements declarationplatform test-oe WSF_PLATFORMadd mover WSF_SPACE_MOVORorbital_stateepoch 2021245.18563semimajor_axis 10000 kmeccentricity 0.2
```

<table><tr><td></td><td>mean_anomaly 255 deg
inclination 30 deg
raan 120 deg
argument_of_periapsis 80 deg
end_orbital_state
end_mover
endPLATFORM
//Example: Position/velocity declaration
platform test-rv WSF PLATFORM
add mover WSF_SPACE_MOVER
orbital_state
    epoch 2021245.18563
    position 800 0 0 km
    velocity 100 3000 -50 m/s
    end_orbital_state
    end_mover
    endPLATFORM
//Example: TLE declaration
//Note: TLE declaration is only allowed within a WSF_NORAD_SPACE_MOVER
platform test-tle WSF PLATFORM
add mover WSF_NORAD_SPACE_MOVER
orbital_state
    orbit
    0 HST
    1 20580U 90037B 20216.30423610 .00000333 00000-0 92680-5 0
9996
    2 20580 28.4681 168.2117 0002666 190.3324 294.3699 15.09238375401891
    end_orbit
    end_orbital_state
    end_mover
    endPLATFORM</td></tr><tr><td>命令</td><td>epoch [&lt;epoch-value&gt; | platform creation_epoch]</td></tr><tr><td>解释</td><td>指定与轨道元素有效的参考历元相对应的历元。
如果指定了 platform creation_epoch, 初始历元将设置为平台的创建时间。
示例
//Example: platform creation_epoch usage
//In this case, initial epoch will be set to 1 hour after simulation start
platform test-oe WSF PLATFORM
creation_time 1 hour
add mover WSF_SPACE_MOVER
orbital_state
    epoch platform creation_epoch
    semimajor_axis 10000 km
    eccentricity 0.2
    mean_anomaly 255 deg
    inclination 30 deg
    raan 120 deg
    argument_of_periapsis 80 deg
    end_orbital_state</td></tr><tr><td></td><td>end_mover
endplatform</td></tr><tr><td>命令</td><td>epoch_date_time &lt;month&gt;&lt;day-of-month&gt;&lt;year&gt;&lt;hh:mm:ss&gt;</td></tr><tr><td>解释</td><td>指定与轨道元素有效的参考历元相对应的日期和时间。
注意 月份使用如下三字符格式表示：jan | feb | mar | apr | may | jun | jul | aug | sep | oct | nov | dec
一天中的时间参考 UT午夜，并使用24小时制。</td></tr></table>

轨道元素命令   

<table><tr><td>命令</td><td>designator &lt;string-value&gt;</td></tr><tr><td>解释</td><td>指定空间移动器的标识符。默认值:“00001A”注意 如果使用 TLE,标识符由 TLE 卫星国际标识符在第一行提供。</td></tr><tr><td>命令</td><td>eccentricity &lt;real-value&gt;</td></tr><tr><td>解释</td><td>指定轨道的偏心率。指定的值必须大于或等于零(圆形轨道)。默认值:0注意 对于 WSF_SPACE_MOV 和 WSF_NORAD_SPACE_MOV,偏心率还必须小于 1.0(抛物线轨道)。</td></tr><tr><td>命令</td><td>semi major axis &lt;length-value&gt;</td></tr><tr><td>解释</td><td>指定定义轨道的椭圆的半长轴。默认值:无。必须提供此值或从其他命令派生。参见轨道元素输入值的派生。注意 对于偏心率为零,半长轴成为圆的半径。注意 此输入等同于 revolutions_per_day,因为两者通过开普勒第三定律相关。如果两者都指定,则使用最后一个指定的。</td></tr><tr><td>命令</td><td>revolutions_per_day &lt;real-value&gt;</td></tr><tr><td>解释</td><td>指定卫星每天绕地球的圈数。默认值:无。必须提供此值或从其他命令派生。参见轨道元素输入值的派生。注意 此输入等同于 semi major axis,因为两者通过开普勒第三定律相关。如果两者都指定,则使用最后一个指定的。</td></tr><tr><td>命令</td><td>periapsis_radius &lt;length-value&gt;</td></tr><tr><td>解释</td><td>指定定义轨道的椭圆的近地点半径。这是卫星与中心体中心之间的最小距离。默认值:无。必须提供此值或从其他命令派生。参见轨道元素输入值的派生。注意 对于偏心率为零,近地点半径等于远地点半径和半长轴。注意 此输入等同于 periapsis_altitude,因为两者通过中心体的平均半径相关。如果两者都指定,则使用最后一个指定的。</td></tr><tr><td>命令</td><td>apoapsis_radius &lt;length-value&gt;</td></tr><tr><td>解释</td><td>指定定义轨道的椭圆的近地点半径。这是卫星与中心体中心之间的最大距离。默认值:无。必须提供此值或从其他命令派生。参见轨道元素输入值的派生。注意 对于偏心率为零,近地点半径等于近地点半径和半长轴。注意 此输入等同于 apoapsis_altitude,因为两者通过中心体的平均半径相关。如果两者都指定,则使用最后一个指定的。</td></tr><tr><td>命令</td><td>periapsis_altitude &lt;length-value&gt;</td></tr><tr><td>解释</td><td>指定定义轨道的椭圆的近地点高度。这是卫星与中心体表面之间的最小距离。默认值:无。必须提供此值或从其他命令派生。参见轨道元素输入值的派生。注意 对于偏心率为零,近地点高度等于远地点高度。注意 此输入等同于 periapsis_altitude,因为两者通过中心体的平均半径相关。如果两者都指定,则使用最后一个指定的。</td></tr><tr><td>命令</td><td>apoapsis_altitude &lt;length-value&gt;</td></tr><tr><td>解释</td><td>指定定义轨道的椭圆的远地点高度。这是卫星与中心体表面之间的最大距离。默认值:无。必须提供此值或从其他命令派生。参见轨道元素输入值的派生。注意 对于偏心率为零,远地点高度等于近地点高度。注意 此输入等同于 apoapsis_altitude,因为两者通过中心体的平均半径相关。如果两者都指定,则使用最后一个指定的。</td></tr><tr><td>命令</td><td>raan | right ascension_ofascending_node &lt;angle-value&gt;</td></tr><tr><td>解释</td><td>指定升交点的赤经(“raan”)。这是沿天赤道从春分点(赤经角)逆时针测量的卫</td></tr><tr><td></td><td>星从南向北穿过赤道(升交点)的角度。默认值:0度注意raan值必须大于或等于零且小于360度(2π弧度)。注意raan参考于真日期坐标系。</td></tr><tr><td>命令</td><td>inclination &lt;angle-value&gt;</td></tr><tr><td>解释</td><td>指定轨道平面切线与地球自转轴的分离角。默认值:0度注意倾角值必须大于或等于零(赤道轨道)且小于或等于180度(π弧度;逆行赤道轨道)。注意倾角参考于真日期坐标系。</td></tr><tr><td>命令</td><td>mean_anomaly &lt;angle-value&gt;</td></tr><tr><td>解释</td><td>指定卫星在历元时间的轨道中的角位置。此角度从近地点测量,表示卫星以恒定角速度遍历的角度。默认值:0度注意平近点角值必须大于或等于零且小于360度(2π弧度)。注意此输入等同于真近点角。参见轨道元素输入值的派生。</td></tr><tr><td>命令</td><td>true_anomaly &lt;angle-value&gt;</td></tr><tr><td>解释</td><td>指定卫星在历元时间的轨道中的角位置。此角度从近地点测量,表示卫星的真实角位置。默认值:0度注意真近点角值必须大于或等于零且小于360度(2π弧度)。注意此输入等同于平近点角。参见轨道元素输入值的派生。</td></tr><tr><td>命令</td><td>argument_of_periapsis &lt;angle-value&gt;</td></tr><tr><td>解释</td><td>指定近地点相对于地球表面的角度。此角度从升交点测量。默认值:0度注意近地点角值必须大于或等于零且小于360度(2π弧度)。</td></tr><tr><td>命令</td><td>descriptor &lt;string-value&gt;</td></tr><tr><td>解释</td><td>指定空间飞行器的任意描述符(标签)。注意如果使用TLE,描述符在第0行提供。</td></tr></table>

# 轨道大小/形状

命令 semi_major_axis 和 revolutions_per_day 是等效输入，因为它们通过开普勒第三定律相关：

$$
N = \frac {d}{2 \pi} \sqrt {\frac {\mu}{a ^ {3}}}
$$

其中：

?是一天中的秒数（86400）  
$\mu$ 是中心体的引力常数

![](images/64aa327772a210dff656348141d02f8fe0131292c5027f184e22cc49b12686c8.jpg)

命令 periapsis_radius（近地点半径）和 periapsis_altitude（近地点高度）是等效的输入，因 为 它 们 通 过 中 心 天 体 的 半 径 相 关 联 。 同 样 ， apoapsis_radius （ 远 地 点 半 径 ） 和apoapsis_altitude（远地点高度）也是如此。请参见上图和以下公式：

$$
r _ {p} = R + z _ {p}
$$

$$
r _ {a} = R + z _ {a}
$$

其中，R 是 central_body(中心天体)的平均半径。

# 轨道参数之间的关系

近地点半径（periapsis_radius）、远地点半径（apoapsis_radius）、偏心率（eccentricity）和半长轴（semi_major_axis）之间的关系如下：

$$
r _ {p} = a (1 - e)
$$

$$
r _ {a} = a (1 + e)
$$

这两个方程中有四个未知数；如果指定其中的两个，另外两个也可以确定。如果只指定一个参数，则假设偏心率（e）为零，仍然可以确定所有四个参数。

# 平均近点角和真近点角

命令 mean_anomaly（平均近点角）和 true_anomaly（真近点角）是等效的输入，它们通过以下方程相关联：

$$
M = E - e \sin E
$$

$$
\cos E = \frac {e + c o s f}{1 + e c o s f}
$$

其中：

。 E 是偏近点角（eccentric anomaly），如下图所示。  
。 f 是真近点角（true anomaly），如下图所示。  
M 是平均近点角（meananomaly），从近地点测量，表示卫星以恒定角速度遍历的角度。

通过这些公式，可以更好地理解和计算轨道参数，从而进行轨道仿真和分析。

![](images/9b57153ed71c6fcdc8dce30d92c7760cd721f12e51b8a66f8e887f5adec454c2.jpg)

此 图 来 自 ： Eccentric and true anomaly.PNG ， CC BY-SA 4.0https://commons.wikimedia.org/w/index.php?curid=48384905

```txt
initial_state position <length-value> <length-value> <length-value> velocity <speed-value> <speed-value> <speed-value> epoch <epoch-value> epoch_date_time <month> <day-of-month> <year> <hh:mm:ss> j2000   
end_initial_state 
```

<table><tr><td>命令</td><td>initial_state...end_initial_state</td></tr><tr><td>解释</td><td>使用地心惯性（ECI）运动学设置平台的初始状态。</td></tr><tr><td>命令</td><td>position &lt;length-value&gt; &lt;length-value&gt; &lt;length-value&gt;</td></tr><tr><td>解释</td><td>在指定的历元中，设置平台在 ECI 框架中的位置。</td></tr><tr><td>命令</td><td>velocity &lt;speed-value&gt; &lt;speed-value&gt; &lt;speed-value&gt;</td></tr><tr><td>解释</td><td>在指定的历元中，设置平台在 ECI 框架中的速度。</td></tr><tr><td>命令</td><td>epoch &lt;epoch-value&gt;
epoch_date_time &lt;month&gt; &lt;day-of-month&gt; &lt;year&gt; hh:mm:ss</td></tr><tr><td>解释</td><td>设置初始状态的历元。只需指定 epoch 或 epoch_date_time 其中之一。</td></tr><tr><td>命令</td><td>j2000</td></tr><tr><td>解释</td><td>指定初始运动学是在 J2000 框架中给出的。如果没有此命令，则默认认为指定的运动学是在 ECI 框架中。</td></tr></table>

轨道积分器(Orbital Integrator)，参见：3.6.5.4.1 积分器 propagator

```txt
integrator<orbital-integrator-name> end_integrator 
```

这个代码块用于指定用于推进平台状态的积分器。每个积分器都有自己的一组输入参数来控制其行为。

可用的积分器

Prince-Dormand 45   
Prince-Dormand 78

这些是可用的积分器类型，分别代表不同的数值积分方法，用于解决微分方程。Prince-Dormand 方法是一种 Runge-Kutta 方法，常用于精确计算轨道和其他动态系统的状态。

# Prince-Dormand 45

```txt
integrator prince_dormand_45 ... Embedded Runge-Kutta commands ... end_integrator 
```

是一种嵌入式 Runge-Kutta 积分方案，具体为 RK5(4)7S。这种方法由 J.R. Dormand 和 P.J.Prince 在 1980 年提出，发表在《计算与应用数学杂志》上。

特性与功能

阶数与误差估计：该积分器提供了一个 5 阶的解，并使用 4 阶的误差估计器。这意味着它在计算过程中能够提供高精度的解，同时通过误差估计器来控制计算误差。

自适应步长：Prince-Dormand 45 使用自适应步长来控制计算解中的误差。这种自适应性使得积分器在处理不同复杂度的问题时能够动态调整步长，从而提高计算效率和精度。

FSAL 特性：该方法具有“First Same As Last”（FSAL）的特性，这意味着在每一步的最后一个阶段的计算点与下一步的第一个阶段相同。这一特性减少了每步所需的函数评估次数，从而提高了计算效率。

# 应用场景

Prince-Dormand45 积分器适用于需要高精度和效率的数值计算场景，特别是在解决常微分方程（ODEs）时。由于其自适应步长和高阶误差控制能力，它在科学计算、工程模拟和轨道计算等领域中被广泛应用。

通过选择合适的积分器，用户可以在 AFSIM中实现更精确和高效的模拟。

# Prince-Dormand 78

```txt
integrator prince_dormand_78 ...Embedded Runge-Kutta commands... end_integrator 
```

Prince-Dormand 78 是一种嵌入式 Runge-Kutta 积分方案，具体为 RK8(7)13M。这种方法由 P.J. Prince 和 J.R. Dormand 在 1981 年提出，发表在《计算与应用数学杂志》上。

# 特性与功能

阶数与误差估计：该积分器提供了一个 8 阶的解，并使用 7 阶的误差估计器。这意味着它能够提供非常高精度的解，同时通过误差估计器来控制计算误差。

自适应步长：Prince-Dormand78 使用自适应步长来控制计算解中的误差。这种自适应性使得积分器在处理不同复杂度的问题时能够动态调整步长，从而提高计算效率和精度。

函数评估：该方法需要 13 次函数评估来完成每一步的积分计算，这使得它在处理复杂的常微分方程时非常有效。

# 应用场景

Prince-Dormand78 积分器适用于需要极高精度的数值计算场景，特别是在解决复杂的常微分方程（ODEs）时。由于其高阶误差控制能力和自适应步长特性，它在科学计算、工程模拟和天体力学等领域中被广泛应用。

通过选择合适的积分器，用户可以在 AFSIM 中实现更精确和高效的模拟，特别是在需要长时间模拟和高精度要求的情况下。

Prince-Dormand 45 和 78 都用到了下列的嵌入式命令

# Embedded Runge-Kutta commands

<table><tr><td>命令</td><td>tolerance &lt;real-value&gt;</td></tr><tr><td>解释</td><td>设定积分器单步的误差容限。默认值为1.0e-10。这是控制计算精度的重要参数，确保每一步的误差不超过指定的容限。</td></tr><tr><td>命令</td><td>max Adjustment Attempts &lt;integer-value&gt;</td></tr><tr><td>解释</td><td>设定最大步长调整尝试次数。如果无法找到合适的步长,将打印警告并继续模拟,但不再保证满足用户请求的误差容限。默认值为50。</td></tr><tr><td>命令</td><td>max_step_size &lt;real-value&gt;</td></tr><tr><td>解释</td><td>设定最大步长(以秒为单位)。如果积分器调整的步长超过此值,将使用此值作为步长。默认值实际上是无限大。</td></tr><tr><td>命令</td><td>min_step_size &lt;real-value&gt;</td></tr><tr><td>解释</td><td>设定最小允许步长(以秒为单位)。如果积分器调整的步长小于此值,将使用此值作为步长。默认值为0。注意,设置非零值可能导致计算解不再满足指定的误差容限。</td></tr><tr><td>命令</td><td>initial_step_size &lt;real-value&gt;</td></tr><tr><td>解释</td><td>设定首次积分尝试的初始步长(以秒为单位)。默认步长为0.1。</td></tr><tr><td>命令</td><td>errorCriterion &lt;error-criterion-type&gt;</td></tr><tr><td>解释</td><td>设定评估步长误差的标准。可能的值为L_infinity和L_2。选择L_infinity要求解中任何误差分量的最大值小于指定的容限。选择L_2要求误差平方和的平方根小于容限。默认选项为L_2。</td></tr></table>

# 动力学模型 Dynamical Model

```txt
dynamics <orbital-dynamics-term> end_dynamics 
```

动力学模型的作用

动力学模型在模拟中起着关键作用，因为它们描述了航天器在轨道上的运动和受力情况。模型通常包括以下几个方面：

重力影响：主要由地球或其他天体的引力场决定。

其他力的影响：如第三方天体的引力、空气阻力、太阳辐射压力或推进系统的推力等。

轨道动力学：涉及解决轨道力学问题，如开普勒问题，确定物体在给定时间的轨道位置。应用场景

动力学模型广泛应用于航天器的轨道设计和分析中。通过精确的动力学建模，可以预测航天器的轨道变化，优化轨道转移（如霍曼转移）等。此外，动力学模型也用于模拟航天器的旋转和轨道耦合效应，如 Deimos 的旋转动力学模型。

通过在 AFSIM 中指定合适的动力学模型，用户可以实现对航天器运动的精确模拟，从而支持任务规划和执行。

# <orbital-dynamics-term>的配置如下

```txt
term <orbital-dynamics-term-name>  
...  
end_term 
```

可用的动力学项

以下是一些可以用于轨道动力学模型的动力学项：

EarthMonopole: 地球的单极引力场，即地球的主要引力影响，通常是最基本的引力模型。  
EarthJ2Perturbation: 地球的 J2 摄动，考虑地球赤道隆起对航天器轨道的影响。这是地球非球对称性的一个重要修正，影响近地轨道的长时间演变。

MoonMonopole: 月球的单极引力场，考虑月球对航天器的引力影响，特别是在地月系统中的任务。  
SunMonopole: 太阳的单极引力场，用于模拟太阳对航天器的引力作用，尤其在深空任务中非常重要。  
JupiterMonopole: 木星的单极引力场，适用于需要考虑木星引力影响的任务，如木星探测任务。  
AtmosphericDrag: 大气阻力，主要用于近地轨道的航天器，考虑大气层对航天器的阻力影响。  
Scripted: 脚本化的动力学项，允许用户通过脚本自定义特定的动力学效应或力的影响。

以下对上述项进行一一列举：

Earth Monopole：代表地球的标准开普勒两体引力场。

```txt
term earth_monopole  
wgs84  
egm96  
gravitational_parameter <real-value>  
end_term 
```

<table><tr><td>命令</td><td>wgs84</td></tr><tr><td>解释</td><td>使用WGS84引力参数。</td></tr><tr><td>命令</td><td>egm96</td></tr><tr><td>解释</td><td>使用EGM96引力参数，默认选择。</td></tr><tr><td>命令</td><td>gravitational_parameter &lt;real-value&gt;</td></tr><tr><td>解释</td><td>指定引力参数（SI单位）。如果没有选择，将使用EGM96的值。</td></tr></table>

term earth_j2: 代表由于地球扁率引起的 J2 摄动。

```txt
term earth_j2  
wgs84  
egm96  
gravitational_parameter <real-value>  
j2 <real-value>  
mean_radius <length-value>  
end_term 
```

<table><tr><td>命令</td><td>wgs84</td></tr><tr><td>解释</td><td>使用WGS84引力参数。</td></tr><tr><td>命令</td><td>egm96</td></tr><tr><td>解释</td><td>使用EGM96引力参数，默认选择。</td></tr><tr><td>命令</td><td>gravitational_parameter &lt;real-value&gt;</td></tr><tr><td>解释</td><td>指定引力参数（SI单位）。如果没有选择，将使用EGM96的值。</td></tr><tr><td>命令</td><td>j2 &lt;real-value&gt;</td></tr><tr><td>解释</td><td>指定J2摄动的强度，默认值为0.0010826267。</td></tr><tr><td>命令</td><td>mean_radius &lt;length-value&gt;</td></tr><tr><td>解释</td><td>指定地球的平均半径（米），默认值为6371公里。</td></tr></table>

term moon_monopole: 代表月球的单极引力场。

```txt
term moon_monopole gravitational_parameter <real-value> interpolation_interval <time-value> end term 
```

<table><tr><td>命令</td><td>gravitational_parameter &lt;real-value&gt;</td></tr><tr><td>解释</td><td>指定引力参数（SI单位），默认值为4.9028e12。</td></tr><tr><td>命令</td><td>interpolation_interval &lt;time-value&gt;</td></tr><tr><td>解释</td><td>指定月球位置的插值间隔。设置为0.0可关闭插值，默认值为600秒。</td></tr></table>

term sun_monopole: 代表太阳的单极引力场。

```txt
term sun_monopole gravitational_parameter <real-value> end_term 
```

<table><tr><td>命令</td><td>gravitational_parameter &lt;real-value&gt;</td></tr><tr><td>解释</td><td>指定引力参数（SI单位），默认值为1.32712440018e20。</td></tr></table>

term jupiter_monopole: 代表木星的单极引力场。

```txt
term jupiter_monopole gravitational_parameter <real-value> end term 
```

<table><tr><td>命令</td><td>gravitational_parameter &lt;real-value&gt;</td></tr><tr><td>解释</td><td>指定引力参数（SI单位），默认值为1.267127678e17。</td></tr></table>

term atmospheric_drag: 代表由于地球大气引起的阻力。

```txt
term atmosphericdrag cross_sectional_area area-value> drag_coefficient real-value> atmosphere_modelatmosphere-model-name>   
end term 
```

<table><tr><td>命令</td><td>cross_sectional_area</td></tr><tr><td>解释</td><td>指定计算阻力时使用的横截面积。</td></tr><tr><td>命令</td><td>drag_coefficient</td></tr><tr><td>解释</td><td>指定计算阻力时使用的阻力系数。</td></tr><tr><td>命令</td><td>atmosphere_model</td></tr><tr><td>解释</td><td>指定将用于此阻力项的大气模型。</td></tr></table>

termscripted: 允许用户通过脚本指定对平台的动力学影响。

```txt
term scripted script <script-name> end_term 
```

<table><tr><td>命令</td><td>script &lt;script-name&gt;</td></tr><tr><td>解释</td><td>指定在全局上下文中定义的脚本函数，该函数计算加速度并返回一个 Vec3。脚本方法将提供以下参数：体验此动力学项的 Wsfl IntegratingSpaceMover、平台的当前质量、调用脚本的时间（Calendar）、平台的 Vec3 ECI 位置和 Vec3 ECI 速度。</td></tr></table>

示例：the following script would reproduce the effect of the Earth Monopole term: script Vec3 ScriptedEarthMonopole(WsfIntegratingSpaceMover aMover, double aMass, Calendar

```txt
aTime, Vec3 aPosition, Vec3 aVelocity)  
Vec3 acc = aPosition.Normal();  
acc.Scale(-Earth.GRAVITATIONAL_PARAMETER() / aPosition MagnitudeSquared());  
return acc;  
end_script 
```

# 合相设置命令

<table><tr><td>命令</td><td>conjunction_setup&lt;initial-position-specification&gt;with_target&lt;target-platform&gt;at_time&lt;time&gt;end_conjunction_setup</td></tr><tr><td>解释</td><td>设置该航天器的初始条件,以便在指定时间与给定目标航天器发生合相。在初始化期间,将尝试找到符合给定边界条件的解决方案。如果成功,将设置该平台的状态以使指定的合相发生。如果没有解决方案(例如,轨道会使卫星穿过地球),则将航天器的速度设置为默认值(见下文)。初始位置规范如下之一:from_lla&lt;纬度值&gt;&lt;经度值&gt;&lt;高度值&gt;将该航天器的初始位置设置为给定的纬度、经度和高度。如果没有合相解决方案,将航天器的速度设置为航向为90度的圆形轨道的速度。from_eci&lt;长度值&gt;&lt;长度值&gt;&lt;长度值&gt;将该航天器的初始位置设置为ECI框架中的给定位置。如果没有合相解决方案,将航天器的速度设置为航向为90度的圆形轨道的速度。from_initial使用其他方法设置该航天器的初始位置,以指定航天器的初始轨道。如果没有合相解决方案,将航天器的速度设置为其他初始化方法提供的速度。with_target&lt;字符串值&gt;指定合相目标平台的名称。该航天器将在at_time命令指定的时间移动到目标平台的位置。指定的目标必须是一个在空间域中移动的平台的名称。at_time&lt;时间值&gt;指定该航天器应在指定时间与指定目标发生合相。tolerance&lt;实数值&gt;指定合相解决方案的容差。默认容差值为1.0e-9。注意:WCS-&gt;LLA转换受中心天体选择的影响,以及在惯性(ECI)坐标转换中计算的恒星运动变换。</td></tr></table>

# 姿态控制命令

姿态控制命令参见 3.6.5.1.1 姿态控制模型 Attitude Controller Models：

姿态控制器用于指定平台的姿态控制器。所有具有 WSF_SPACE_MOVER 或WSF_NORAD_SPACE_MOVER 的平台都会有某种姿态控制器。如果没有指定姿态控制器块，移动器将以选择即时姿态控制器的方式运行。

姿态控制器将尝试改变平台的方向以匹配给定的目标方向。在创建时，姿态控制器将通过 姿 态 控 制 器 块 中 的 方 向 命 令 指 定 目 标 方 向 。 创 建 后 ， 可 以 通 过WsfSpaceMover.SetOrientation 更改姿态控制器的方向目标。

目标方向可以是一次性选择的目标方向，或者将姿态控制器连接到预设的方向类型之一。在后一种情况下，随着航天器沿其轨道移动，姿态控制器将具有不断更新的目标方向。

可用的模型包括：

3.6.5.1.1.2 即时姿态控制器

3.6.5.1.1.3 速率限制姿态控制器

在执行机动时，需要检查以确保有足够的燃料供应。当机动执行时，推进剂被消耗，火箭阶段的质量属性会更新。

# 轨道机动命令

轨道机动命令参见：3.6.5.1.2 轨道机动模型 Orbital Maneuvering Models。

轨道机动模型 用于在太空中执行轨道机动。这些模型用于改变航天器的轨道。根据提供的信息，简单机动模型和火箭机动模型是可用的选项。火箭机动模型通常涉及使用火箭发动机来执行轨道插入、轨道圆化、轨道转移、交会、脱轨等操作。

可用的模型包括：

3.6.5.1.2.2 简单机动模型  
3.6.5.1.2.3 火箭机动模型

# 轨道任务序列

```txt
mission_sequence <constraint> event Common Mission Event Commands mission event-specific commands ... end_event ... additional mission event definitions end_mission_sequence 
```

指定任务序列，参考：3.6.5.1.3 轨道任务序列 Orbital Mission Sequence。

示例

```txt
// Example: Two mission events to raise a satellite  
// from an initial injection point  
// into a geosynchronous transfer orbit (GTO)  
mission_sequence  
// Constraint: delay two full orbits before executing  
execute_at orbit 2 relative_time 0.0 s  
// intermediate orbit  
event change(semimajor_axis  
    semi major axis 9000 km  
    execute_at orbit 2 ascending_node // Constraint with orbit delay  
end_event  
// GTO  
maneuver change(semi major axis // "maneuver ... end maneuver" block may be used with orbital maneuver types. 
```

```txt
semi major axis 24821 km execute_at ascending_node // Constraint without orbit delay end_maneuver   
end_missio_sequence 
```

轨 道 任 务 事 件 和 任 务 事 件 序 列 可 以 使 用 脚 本 方 法 WsfSpaceMover.ExecuteEvent（WsfSpaceMover.ExecuteManeuver）和 WsfSpaceMover.ExecuteMissionSequence 进行脚本化。

# 脚本接口

WSF_SPACE_MOVER 使用通用脚本接口（4.1 公共脚本接口 Common Script Interface），并提供隐式定义的引用 SPACE_MOVER，这允许在不进行类型转换的情况下调用WsfSpaceMover 方法。

# 3.6.5.4.1. 积分器 propagator

```txt
propagator <propagator-type>  
...  
end_propagator 
```

轨道传播器（OrbitalPropagator）用于根据给定的初始状态确定空间平台的未来运动状态（位置和速度）。在 AFSIM 中，传播器用于模拟带有空间移动器的卫星的轨道运动（例如，参见 WSF_SPACE_MOVER），以及跟踪估计的卫星位置（例如，参见：3.6.5.4.1.1 轨道确定融合 Orbit Determination Fusion）。

传播器类型

请参阅预定义的传播器类型以获取可用传播器类型的列表。

概述

WSF_INTEGRATING_PROPAGATOR 实现了一种轨道传播器，适用于空间域中的平台。与使 用 解 析 模 型 的 WSF_KEPLERIAN_PROPAGATOR 或 WSF_NORAD_PROPAGATOR 不 同 ，WSF_INTEGRATING_PROPAGATOR 使用数值积分。这种方法允许用户指定动力学模型，使传播器不局限于地球在动力学中起主导作用的情况。

用户需要选择一个积分器和一个动力学模型来完全指定传播器的行为。积分器决定了平台状态如何在时间上进行数值传播，而动力学模型则指定平台将经历的力。

注意：如果动力学模型需要依赖于平台质量的项，则需要为平台指定质量。这可以通过在平台上显式设置质量，或使用相关的 WSF_INTEGRATING_SPACE_MOVER 中的火箭机动模型来实现。

# 3.6.5.4.1.1. 轨道确定融合 Orbit Determination Fusion

```txt
fusion_method orbit_determination  
number_of_anglemeasurements <int>  
angles_only_linear_tolerance <length-value>  
angles_only_maximumpatterns <int>  
lambert_convergence_tolerance <real>  
process_noise_sigmas_XYZ... 
```

```txt
propagator ... end_propagator  
debug  
debug_filter  
end_corrption_method 
```

轨道确定融合（Orbit DeterminationFusion）结合了多种传感器测量的算法，以提供卫星轨道的初始估计，然后继续融合后续测量以更新和完善初始估计。目标测量可以来自仅提供方位-仰角轨迹的角度传感器，或也提供距离的测量。一旦轨道初步确定，将触发一个ORBIT_DETERMINATION_INITIATED 事 件 。 在 后 续 的 轨 道 确 定 更 新 中 ， 将 触 发ORBIT_DETERMINATION_UPDATED 事件。

注意：强烈建议在轨道管理器中设置保留轨迹历史为真，以积累足够的测量来启动轨道确定。此外，为了管理要保留的测量总数，请在使用此融合策略的任何轨迹处理器中设置轨迹历史保留间隔时间。

初始轨道确定算法记录在“使用多次观测的初始轨道确定”中（Karimi 和 Mortari，Celest.Mech. Dyn. Astr. (2011) 109:167-180 ） 。 持 续 的 轨 道 确 定 使 用WSF_ORBIT_DETERMINATION_FILTER 实现。

命令

process_noise_sigmas_XYZ <X-value> <Y-value> <Z-value>

定义嵌入式滤波器使用的噪声标准差。值对应于被跟踪平台的实体坐标系（ECS）中的加速度。

默认值：000

propagator <propagator-type> … end_propagator

指定将在 WSF_ORBIT_DETERMINATION_FILTER 中用于跟踪目标的传播器类型。

默认值：如果从轨迹中可获得真实目标类型，则为被跟踪目标的传播器类型；否则为WSF_KEPLERIAN_PROPAGATOR。

注意：传播器的初始状态将使用初始轨道确定和后续轨迹更新的结果提供；任何提供的传播器初始状态配置（初始轨道元素或轨道状态）将被忽略。

number_of_angle_measurements <integer>

指定在进行仅角度初始轨道确定尝试之前要收集的仅角度测量的数量。

注意：此值必须至少为 3。

默认值：5

angles_only_linear_tolerance <length-value>

指定仅角度初始轨道确定算法收敛到解所需的线性公差。指定较高的值更可能找到有效解。

默认值：10 米

angles_only_maximum_iterations <integer>

指定仅角度初始轨道确定算法找到解的最大迭代次数。

注意：通常不需要设置此值。

默认值：200

lambert_convergence_tolerance <real>

指定 Lambert 通用变量算法的两个位置和时间的收敛无单位公差。

默认值：1.0e-12

debug

将调试信息打印到标准输出。

debug_filter

指定保存过滤历史信息（参见过滤调试）。

range_error_factor

指定在将仅角度轨迹与现有轨迹融合时用于计算距离误差的因子（从中可以估计距离）。此因子乘以估计距离以获得估计距离误差。

默认值：0.05

# 3.6.5.4.1.2. KEPLERIAN 传播 WSF_KEPLERIAN_PROPAGATOR

```txt
propagator <name> WSF_kePLERIAN_propAGATOR ... Orbital Element Commands ... ... Common Orbital Propagator Commands... end_propagator 
```

WSF_KEPLERIAN_PROPAGATOR 模拟卫星围绕点质量的轨道传播。结果轨道在惯性空间中是一个完美的椭圆。WSF_KEPLERIAN_PROPAGATOR 对于建模概念卫星和卫星星座，以及为现有卫星提供理想化的轨道表示非常有用。

命令

轨道状态命令

orbital_state … end_orbital_state

指定轨道状态，可以通过以下方式之一：

□ 足够的轨道元素命令   
□ 位置和速度向量  
包 含 两 行 元 素 （ TLE ） 的 orbit … end_orbit 命 令 块 （ 当 使 用WSF_NORAD_SPACE_MOVER 时）

# 位置和速度

position <real> <real> <real> <length-units>

设置空间移动器的初始位置。此命令必须与速度命令一起使用。

velocity <real> <real> <real> <speed-units>

设置空间移动器的初始速度。此命令必须与位置命令一起使用。

注意：位置和速度输入必须按顺序提供，速度输入紧随位置之后。

示例

轨道元素声明示例

```txt
platform test-oe WSFPLATFORM  
add mover WSF_SPACE_MOVER  
orbital_state  
epoch 2021245.18563  
semi major axis 10000 km  
eccentricity 0.2  
mean_anomaly 255 deg  
inclination 30 deg 
```

```txt
raan 120 deg argument_of_periapsis 80 deg end_orbital_state end mover endPLATFORM 
```

位置/速度声明示例  
plaintext   
platform test-rv WSFPLATFORM add mover WSF_SPACE_MOVER orbital_state epoch 2021245.18563 position $80000km$ velocity 100 3000 -50 m/s end_orbital_state end_mover   
end-platform

TLE 声明示例  
```txt
platform test-tle WSFPLATFORM
add mover WSF_NORAD_SPACE_MOVER
orbital_state
    orbit
    0 HST
    1 20580U 90037B 20216.30423610 .00000333 00000-0 92680-5 0 9996
    2 20580 28.4681 168.2117 0002666 190.3324 294.3699 15.09238375401891
    end_orbit
    end_orbital_state
    end_MOVerr
end-platform 
```

时间纪元

epoch [<epoch-value> | platform_creation_epoch]

指定与轨道元素有效的参考纪元对应的纪元。

示例：使用 platform_creation_epoch

```txt
platform test-oe WSFPLATFORM creation_time 1 hour add mover WSF_SPACE_MOVER orbital_state epoch platform creation_epoch 
```

```txt
semi_major_axis 10000 km  
eccentricity 0.2  
mean_anomaly 255 deg  
inclination 30 deg  
raan 120 deg  
argument_of_periapsis 80 deg  
end_orbital_state  
end mover  
endplatform 
```

epoch_date_time <month> <day-of-month> <year> <hh:mm:ss>

指定与轨道元素有效的参考纪元对应的日期和时间。

注意：月份以三字符格式表示，如：jan, feb, mar 等。时间以 UT 午夜为参考，使用 24小时制。

轨道元素命令用于定义卫星的初始轨道状态。以下是可用的命令及其解释：

designator <string-value>

指定空间移动器的标识符。

默认值：00001A

注意：如果使用 TLE，标识符由 TLE 卫星国际标识符提供。

eccentricity <real-value>

指定轨道的偏心率。指定值必须大于或等于零（圆形轨道）。

默认值：0

注意：对于 WSF_SPACE_MOVER 和 WSF_NORAD_SPACE_MOVER，偏心率也必须小于1.0（抛物线轨道）。

semi_major_axis <length-value>

指定定义轨道的椭圆的半长轴。

默认值：无。必须提供或从其他命令中推导。

注意：对于偏心率为零，半长轴即为圆的半径。此输入与 revolutions_per_day 等效，因为两者通过开普勒第三定律相关。如果同时指定，以最后一个为准。

revolutions_per_day <real-value>

指定卫星每天绕地球的圈数。

默认值：无。必须提供或从其他命令中推导。

注意：此输入与 semi_major_axis 等效，因为两者通过开普勒第三定律相关。如果同时指定，以最后一个为准。

periapsis_radius <length-value>

指定定义轨道的椭圆的近地点半径。这是卫星与中心天体中心之间的最小距离。

默认值：无。必须提供或从其他命令中推导。

注意：对于偏心率为零，近地点半径等于远地点半径和半长轴。此输入与periapsis_altitude 等效，因为两者通过中心天体的平均半径相关。如果同时指定，以最后一个为准。

apoapsis_radius <length-value>

指定定义轨道的椭圆的远地点半径。这是卫星与中心天体中心之间的最大距离。

默认值：无。必须提供或从其他命令中推导。

注意：对于偏心率为零，远地点半径等于近地点半径和半长轴。此输入与

apoapsis_altitude 等效，因为两者通过中心天体的平均半径相关。如果同时指定，以最后一个为准。

periapsis_altitude <length-value>

指定定义轨道的椭圆的近地点高度。这是卫星与中心天体表面之间的最小距离。

默认值：无。必须提供或从其他命令中推导。

注意：对于偏心率为零，近地点高度等于远地点高度。此输入与 periapsis_radius 等效，因为两者通过中心天体的平均半径相关。如果同时指定，以最后一个为准。

apoapsis_altitude <length-value>

指定定义轨道的椭圆的远地点高度。这是卫星与中心天体表面之间的最大距离。

默认值：无。必须提供或从其他命令中推导。

注意：对于偏心率为零，远地点高度等于近地点高度。此输入与 apoapsis_radius 等效，因为两者通过中心天体的平均半径相关。如果同时指定，以最后一个为准。

raan | right_ascension_of_ascending_node <angle-value>

指定升交点赤经（“raan”）。这是从春分点沿天赤道逆时针测量的角度，卫星从南向北穿过赤道（升交点）。

默认值：0 度

注意：raan 值必须大于或等于零且小于 360 度（2π弧度）。raan参考于日期真坐标系。

inclination <angle-value>

指定轨道平面切线与地球自转轴的分离角。

默认值：0 度

注意：倾角值必须大于或等于零（赤道轨道）且小于或等于 180 度（π弧度；逆行赤道轨道）。倾角参考于日期真坐标系。

mean_anomaly <angle-value>

指定卫星在纪元时间的轨道角位置。此角度从近地点测量，表示卫星以恒定角速度遍历的角度。

默认值：0 度

注意：平均近点角值必须大于或等于零且小于 360 度（2π弧度）。此输入与真近点角等效。

true_anomaly <angle-value>

指定卫星在纪元时间的轨道角位置。此角度从近地点测量，表示卫星的真实角位置。

默认值：0 度

注意：真近点角值必须大于或等于零且小于 360 度（2π弧度）。此输入与平均近点角等效。

argument_of_periapsis <angle-value>

指定近地点相对于地球表面的角度。此角度从升交点测量。

默认值：0 度

注意：近地点幅角值必须大于或等于零且小于 360 度（2π弧度）。

descriptor <string-value>

为空间飞行器指定任意描述符（标签）。

注意：如果使用 TLE，描述符在第 0 行提供。

# 轨道元素输入值的解析

对于某些轨道元素，有多种方式可以指定轨道的特定特征。

符号与命令对照表  

<table><tr><td>Symbol</td><td>Command</td></tr><tr><td>N</td><td>revolutions_per_day</td></tr><tr><td>a</td><td>semimajor_axis</td></tr><tr><td>e</td><td>eccentricity</td></tr><tr><td>rp</td><td>periapsis_radius</td></tr><tr><td>ra</td><td>apoapsis_radius</td></tr><tr><td>zp</td><td>periapsis_altitude</td></tr><tr><td>za</td><td>apoapsis_altitude</td></tr><tr><td>M</td><td>mean_anomaly</td></tr><tr><td>f</td><td>true_anomaly</td></tr></table>

# 轨道大小/形状

命令 semi_major_axis 和 revolutions_per_day 是等效输入，因为它们通过开普勒第三定律相关：

$$
N = \frac {d}{2 \pi} \sqrt {\frac {\mu}{a ^ {3}}}
$$

其中：

?是一天中的秒数（86400）  
◦ $\mu$ 是中心体的引力常数

![](images/4a4bc9bc8a9fb0a48ff8c5d63a1f03bb4859fca336cdf627401eaaa485165cf3.jpg)

命令 periapsis_radius（近地点半径）和 periapsis_altitude（近地点高度）是等效的输入，因为它们通过中心天体的半径相关联。同样，apoapsis_radius（远地点半径）和apoapsis_altitude（远地点高度）也是如此。请参见上图和以下公式：

$$
r _ {p} = R + z _ {p}
$$

$$
r _ {a} = R + z _ {a}
$$

其中，R 是 central_body(中心天体)的平均半径。

# 轨道参数之间的关系

近地点半径（periapsis_radius）、远地点半径（apoapsis_radius）、偏心率（eccentricity）