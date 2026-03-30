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
◦ f是真近点角（trueanomaly），如下图所示。  
M 是平均近点角（meananomaly），从近地点测量，表示卫星以恒定角速度遍历的角度。

通过这些公式，可以更好地理解和计算轨道参数，从而进行轨道仿真和分析。

![](images/88293137f335790fc45602a9dd6b6878cc57fd4f7e26e5078e224ed092d22e86.jpg)

此 图 来 自 ： Eccentric and true anomaly.PNG ， CC BY-SA 4.0https://commons.wikimedia.org/w/index.php?curid=48384905

<table><tr><td>命令</td><td>orbit_color &lt;color-value&gt;</td></tr><tr><td>解释</td><td>指定轨道的颜色。
注意：即使指定了颜色的 alpha 分量，也不会使用。</td></tr></table>

# 两行根数（TLE）轨道

指定一个两行元素（TLE），用于定义平均轨道元素和其他用于传播卫星的数据。两行元素通常从现有资源中获取，例如 Spacetrak 数据库（http://www.space-track.org）或 Celestrak（http://www.celestrak.com/NORAD/elements）。与普通的 AFSIM 输入不同，列格式、字段长度和字符格式必须完全按照以下规定进行。

# 示例

orbit

*<(optional) satellite descriptor>*   
*<first line of TLE>*   
*<second line of TLE>*

end_orbit

# TITLE INFORMATION:

Line 1

Column Characters Description

----- |--- |----

1 1 Line No. Identification   
3 5 Catalog No.   
8 1 Security Classification   
10 8 International Identification   
19 14 YRDOY.FODddddd   
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

Line 2

Column Characters Description

----- |--- |----

1 1 Line No. Identification   
3 5 Catalog No.   
9 8 Inclination  
18 8 Right Ascension of Ascending Node   
27 7 Eccentricity with assumed leading decimal   
35 8 Argument of the Perigee   
44 8 Mean Anomaly  
53 11 Revolutions per Day (Mean Motion)

```txt
64 5 Revolution Number at Epoch  
69 1 Check Sum Modulo 10 
```

Vanguard-1 卫星的 TLE 示例

```verilog
orbit  
1 00005U 58002B 09105.24506411 .00000084 00000-0 11810-3 0 4337  
2 00005 034.2551 191.5961 1850437 000.0334 000.0199 10.83999999762276  
end_orbit 
```

注意：WSF_SPACE_MOVER 目前仅使用 TLE 中包含的经典轨道元素，并将其解释为瞬时元素，而不是平均元素。

注意：使用 Modify_tle_list Perl 脚本将 TLE 列表转换为 AFSIM 平台列表。

Common Orbital Propagator Commands 中文翻译与解释

通用轨道传播器命令用于定义轨道传播中使用的坐标系的中心天体及相关椭球模型。根据传播器类型，传播会受到中心天体相关引力参数的影响。

命令

central_body … end_central_body

指定定义用于轨道传播的坐标系原点的中心天体及相关椭球模型。

可选的中心天体类型：

□ earth_wgs72：根据 WGS-72 标准定义的地球椭球。  
□ earth_wgs84：根据 WGS-84 标准定义的地球椭球。  
□ earth_egm96：根据 EGM-96 标准定义的地球椭球。  
□ moon：根据已发布的月球参数定义的月球椭球。   
□ sun：根据已发布的太阳参数定义的太阳椭球。  
□ jupiter：根据已发布的木星参数定义的木星椭球。

默认值：在 global_environment 中指定的中心天体选择（默认值为 earth_wgs84）。

注意：如果指定的中心天体类型与 global_environment 中定义的不同，则父平台的报告位置将相对于全局环境的中心天体。

polar_offset_angles <angle-value> <angle-value>

指定中心天体的极偏移角（分别为 x_p 和 y_p），相对于 WCS（ITRS）坐标系的天体中间极（CIP）。提供这些值（约为十分之一角秒）可以实现 ECI 和 WCS 坐标之间的非常精确的转换。

默认值：在 global_environment 中指定的极偏移角（0.0 弧度 0.0 弧度）。

注意事项

适 用 范 围 ： 此 命 令 目 前 仅 用 于 WSF_KEPLERIAN_PROPAGATOR 和WSF_J2_PERTURBATION_PROPAGATOR 的轨道传播，限于地球中心天体。

# 3.6.5.4.1.3. J2 轨道传播 WSF_J2_PERTURBATION_PROPAGATOR

```txt
propagator <name> WSF_J2_PERTURBATION_propAGATOR ... Orbital Element Commands ... 
```

```txt
... Common Orbital Propagator Commands ... end_propagator 
```

WSF_J2_PERTURBATION_PROPAGATOR 模拟卫星围绕椭球形地球的轨道传播。该模型不仅考虑了地球点质量引力的主要效应，还考虑了由于地球扁平化引起的（平均一阶）引力扰动效应。结果轨道在惯性空间中是一个椭圆，由于轨道元素的变化而缓慢旋转。WSF_J2_PERTURBATION_PROPAGATOR 对于建模特殊地球轨道的卫星非常有用，例如太阳同步轨道和莫尔尼亚轨道。

命令

轨道状态命令

orbital_state … end_orbital_state

指定轨道状态，可以通过以下方式之一：

▫ 足够的轨道元素命令   
□ 位置和速度向量  
□ 包 含 两 行 元 素 （ TLE ） 的 orbit … end_orbit 命 令 块 （ 当 使 用WSF_NORAD_SPACE_MOVER 时）

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
raan 120 deg  
argument_of_periapsis 80 deg  
end_orbital_state  
end_mover  
endPLATFORM 
```

位置/速度声明示例

```txt
platform test-rv WSFPLATFORM add mover WSF_SPACE_MOVER 
```

```txt
orbital_state  
epoch 2021245.18563  
position 800 0 0 km  
velocity 100 3000 -50 m/s  
end_orbital_state  
end_mover  
endplatform  
TLE 声明示例  
platform test-tle WSFPLATFORM  
add mover WSF_NORAD_SPACE_MOVER  
orbital_state  
orbit  
0 HST  
1 20580U 90037B 20216.30423610 .00000333 00000-0 92680-5 0 9996  
2 20580 28.4681 168.2117 0002666 190.3324 294.3699 15.09238375401891  
end_orbit  
end_orbital_state  
end_mover  
endplatform 
```

时间纪元

epoch [<epoch-value> | platform_creation_epoch]

指定与轨道元素有效的参考纪元对应的纪元。

示例：使用 platform_creation_epoch

```txt
platform test-oe WSFPLATFORM
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
    end_orbital_state
    end_mover
endPLATFORM 
```

epoch_date_time <month> <day-of-month> <year> <hh:mm:ss>

指定与轨道元素有效的参考纪元对应的日期和时间。

注意：月份以三字符格式表示，如：jan,feb,mar 等。时间以 UT 午夜为参考，使用 24小时制。

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

注意：对于偏心率为零，远地点半径等于近地点半径和半长轴。此输入与apoapsis_altitude 等效，因为两者通过中心天体的平均半径相关。如果同时指定，以最后一个为准。

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

$d$ 是一天中的秒数（86400）  
$\mu$ 是中心体的引力常数

![](images/aa0d8a3eb7b2ff4b8c68550a94cb1a2d58342d0849b6b87feea4ba9af5940f13.jpg)

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
\begin{array}{l} M = E - e \sin E \\ \cos E = \frac {e + c o s f}{1 + e c o s f} \\ \end{array}
$$

其中：

◦ E 是偏近点角（eccentric anomaly），如下图所示。  
f 是真近点角（true anomaly），如下图所示。  
M 是平均近点角（meananomaly），从近地点测量，表示卫星以恒定角速度遍历的角度。

通过这些公式，可以更好地理解和计算轨道参数，从而进行轨道仿真和分析。

![](images/4649508621d3537a061382319bc3c20aed3092c79080e99f4c03e93873355c50.jpg)

此 图 来 自 ： Eccentric and true anomaly.PNG ， CC BY-SA 4.0https://commons.wikimedia.org/w/index.php?curid=48384905

<table><tr><td>命令</td><td>orbit_color &lt;color-value&gt;</td></tr><tr><td>解释</td><td>指定轨道的颜色。
注意：即使指定了颜色的 alpha 分量，也不会使用。</td></tr></table>

# 两行根数（TLE）轨道

指定一个两行元素（TLE），用于定义平均轨道元素和其他用于传播卫星的数据。两行元素通常从现有资源中获取，例如 Spacetrak 数据库（http://www.space-track.org）或 Celestrak（http://www.celestrak.com/NORAD/elements）。与普通的 AFSIM 输入不同，列格式、字段长度和字符格式必须完全按照以下规定进行。

# 示例

orbit \*<(optional) satellite descriptor> \* <first line of TLE $^ { \text{青} }$ \* <second line of TLE $^ { \text{青} }$ end_orbit

```txt
TITLE INFORMATION: Line 1 Column Characters Description 
```

```txt
---- |--- |---   
1 1 Line No. Identification   
3 5 Catalog No.   
8 1 Security Classification   
10 8 International Identification   
19 14 YRDOY.FODdddd   
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
Line 2 Column Characters Description   
---- |--- |---   
1 1 Line No. Identification   
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

Vanguard-1 卫星的 TLE 示例  
```txt
orbit  
100005U 58002B 09105.24506411 .00000084 00000-0 11810-3 0 4337  
200005 034.2551 191.5961 1850437 000.0334 000.0199 10.83999999762276  
end_orbit 
```

注意：WSF_SPACE_MOVER 目前仅使用 TLE 中包含的经典轨道元素，并将其解释为瞬时元素，而不是平均元素。

注意：使用 Modify_tle_list Perl 脚本将 TLE 列表转换为 AFSIM 平台列表。

Common Orbital Propagator Commands 中文翻译与解释

通用轨道传播器命令用于定义轨道传播中使用的坐标系的中心天体及相关椭球模型。根据传播器类型，传播会受到中心天体相关引力参数的影响。

命令

central_body … end_central_body

指定定义用于轨道传播的坐标系原点的中心天体及相关椭球模型。

可选的中心天体类型：

□ earth_wgs72：根据 WGS-72 标准定义的地球椭球。  
▫ earth_wgs84：根据 WGS-84 标准定义的地球椭球。  
□ earth_egm96：根据 EGM-96 标准定义的地球椭球。  
□ moon：根据已发布的月球参数定义的月球椭球。   
□ sun：根据已发布的太阳参数定义的太阳椭球。  
□ jupiter：根据已发布的木星参数定义的木星椭球。

默认值：在 global_environment 中指定的中心天体选择（默认值为 earth_wgs84）。

注意：如果指定的中心天体类型与 global_environment 中定义的不同，则父平台的报告位置将相对于全局环境的中心天体。

polar_offset_angles <angle-value> <angle-value>

指定中心天体的极偏移角（分别为 x_p 和 y_p），相对于 WCS（ITRS）坐标系的天体中间极（CIP）。提供这些值（约为十分之一角秒）可以实现 ECI 和 WCS 坐标之间的非常精确的转换。

默认值：在 global_environment 中指定的极偏移角（0.0 弧度 0.0 弧度）。

注意事项

适 用 范 围 ： 此 命 令 目 前 仅 用 于 WSF_KEPLERIAN_PROPAGATOR 和WSF_J2_PERTURBATION_PROPAGATOR 的轨道传播，限于地球中心天体。

# 3.6.5.4.1.4. NORAD 传播模型 WSF_NORAD_PROPAGATOR

```txt
propagator <name> WSF_NORAD_propAGATOR ... Orbital Element Commands ... ... Orbit Command for Two-Line Elements (TLEs) ... ... Common Orbital Propagator Commands... end_propagator 
```

WSF_NORAD_PROPAGATOR 实现了一个用于地球轨道平台的传播器。它适用于建模那些有两行元素（TLE）集可用的卫星，包括大多数在轨运行的地球卫星、非运行卫星和主动跟踪的轨道碎片。

该传播器实现了在 SpaceTrack 报告第 3 号中定义的传播算法（SpaceTrack Report No. 3）。该报告提供了定义多个模型的算法；传播器根据两行元素中提供的数据选择适当的模型（NORADSGP、SGP4、SGP8、SDP4 或 SDP8）进行传播。这些模型考虑了地球的扁平化、大气阻力以及太阳和月球的第三体扰动效应。

命令

# 轨道状态命令

orbital_state … end_orbital_state

指定轨道状态，可以通过以下方式之一：

□ 足够的轨道元素命令   
□ 位置和速度向量  
包 含 两 行 元 素 （ TLE ） 的 orbit … end_orbit 命 令 块 （ 当 使 用WSF_NORAD_SPACE_MOVER 时）

# 位置和速度

position <real> <real> <real> <length-units>设置空间移动器的初始位置。此命令必须与速度命令一起使用。  
velocity <real> <real> <real> <speed-units>设置空间移动器的初始速度。此命令必须与位置命令一起使用。注意：位置和速度输入必须按顺序提供，速度输入紧随位置之后。

# 示例

轨道元素声明示例  
```txt
platform test-oe WSF_PLATFORM  
add mover WSF_SPACE_MOVER  
orbital_state  
epoch 2021245.18563  
semimajor_axis 10000 km  
eccentricity 0.2  
mean_anomaly 255 deg  
inclination 30 deg  
raan 120 deg  
argument_of_periapsis 80 deg  
end_orbital_state  
end_mover  
endPLATFORM 
```

位置/速度声明示例  
```txt
platform test-rv WSFPLATFORM  
add mover WSF_SPACE_MOVER  
orbital_state  
epoch 2021245.18563  
position 800 0 0 km  
velocity 100 3000 -50 m/s  
end_ orbital_state  
end_mover  
endPLATFORM 
```

TLE 声明示例  
```txt
platform test-tle WSFPLATFORM 
```

```txt
add mover WSF_NORAD_SPACE_MOVER  
orbital_state  
orbit  
0 HST  
1 20580U 90037B 20216.30423610 .00000333 00000-0 92680-5 0 9996  
2 20580 28.4681 168.2117 0002666 190.3324 294.3699 15.09238375401891  
end_orbit  
end_orbital_state  
end.movere  
endPLATFORM 
```

时间纪元

epoch [<epoch-value> | platform_creation_epoch]

指定与轨道元素有效的参考纪元对应的纪元。

示例：使用 platform_creation_epoch

```txt
platform test-oe WSFPLATFORM creation_time 1 hour add mover WSF_SPACE_MOVER orbital_state epoch platformCreation_epoch semi major_axis 10000 km eccentricity 0.2 mean_anomaly 255 deg inclination 30 deg raan 120 deg argument_of_periapsis 80 deg end_orbital_state end_mover   
end-platform 
```

epoch_date_time <month> <day-of-month> <year> <hh:mm:ss>

指定与轨道元素有效的参考纪元对应的日期和时间。

注意：月份以三字符格式表示，如：jan,feb,mar 等。时间以 UT 午夜为参考，使用 24小时制。

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

◦ ?是一天中的秒数（86400）  
$\mu$ 是中心体的引力常数

![](images/17d8a73c849df1576a05583f0f14df196822b20a60a97c6292b44b2372f0fc0d.jpg)

命令 periapsis_radius（近地点半径）和 periapsis_altitude（近地点高度）是等效的输入，因为它们通过中心天体的半径相关联。同样，apoapsis_radius（远地点半径）和apoapsis_altitude（远地点高度）也是如此。请参见上图和以下公式：

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
◦ M 是平均近点角（mean anomaly），从近地点测量，表示卫星以恒定角速度遍历的角度。

通过这些公式，可以更好地理解和计算轨道参数，从而进行轨道仿真和分析。

![](images/f8c105d1bc187d00e5ab8b3cc81bcea8814eadf71b35ad50af8a623864aaefed.jpg)

此 图 来 自 ： Eccentric and true anomaly.PNG ， CC BY-SA 4.0https://commons.wikimedia.org/w/index.php?curid=48384905

<table><tr><td>命令</td><td>orbit_color &lt;color-value&gt;</td></tr><tr><td>解释</td><td>指定轨道的颜色。
注意：即使指定了颜色的 alpha 分量，也不会使用。</td></tr></table>

# 两行根数（TLE）轨道

指定一个两行元素（TLE），用于定义平均轨道元素和其他用于传播卫星的数据。两行元素通常从现有资源中获取，例如 Spacetrak 数据库（http://www.space-track.org）或 Celestrak（http://www.celestrak.com/NORAD/elements）。与普通的 AFSIM 输入不同，列格式、字段长度和字符格式必须完全按照以下规定进行。

# 示例

orbit

\*<(optional) satellite descriptor $\rightharpoondown$ \* <first line of TLE $^ { \text{青} }$

```txt
*<second line of TLE>* end_orbit 
```

# TITLE INFORMATION:

```txt
Line 1 Column Characters Description 
```

```txt
---- |--- |---  
1 1 Line No. Identification  
3 5 Catalog No.  
8 1 Security Classification  
10 8 International Identification  
19 14 YRDOY.FODdddd  
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
```

```txt
Line 2 Column Characters Description 
```

```txt
---- |--- |----  
1 1 Line No. Identification  
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

Vanguard-1 卫星的 TLE 示例

```txt
orbit 
```

```verilog
1 00005U 58002B 09105.24506411 .00000084 00000-0 11810-3 0 4337  
2 00005 034.2551 191.5961 1850437 000.0334 000.0199 10.83999999762276  
end_orbit
```

注意：WSF_SPACE_MOVER 目前仅使用 TLE 中包含的经典轨道元素，并将其解释为瞬时元素，而不是平均元素。

注意：使用 Modify_tle_list Perl 脚本将 TLE 列表转换为 AFSIM 平台列表。

Common Orbital Propagator Commands 中文翻译与解释

通用轨道传播器命令用于定义轨道传播中使用的坐标系的中心天体及相关椭球模型。根据传播器类型，传播会受到中心天体相关引力参数的影响。

命令

central_body … end_central_body

指定定义用于轨道传播的坐标系原点的中心天体及相关椭球模型。

可选的中心天体类型：

□ earth_wgs72：根据 WGS-72 标准定义的地球椭球。  
▫ earth_wgs84：根据 WGS-84 标准定义的地球椭球。  
□ earth_egm96：根据 EGM-96 标准定义的地球椭球。  
□ moon：根据已发布的月球参数定义的月球椭球。   
□ sun：根据已发布的太阳参数定义的太阳椭球。  
□ jupiter：根据已发布的木星参数定义的木星椭球。

默认值：在 global_environment 中指定的中心天体选择（默认值为 earth_wgs84）。

注意：如果指定的中心天体类型与 global_environment 中定义的不同，则父平台的报告位置将相对于全局环境的中心天体。

polar_offset_angles <angle-value> <angle-value>

指定中心天体的极偏移角（分别为 x_p 和 y_p），相对于 WCS（ITRS）坐标系的天体中间极（CIP）。提供这些值（约为十分之一角秒）可以实现 ECI 和 WCS 坐标之间的非常精确的转换。

默认值：在 global_environment 中指定的极偏移角（0.0 弧度 0.0 弧度）。

注意事项

适 用 范 围 ： 此 命 令 目 前 仅 用 于 WSF_KEPLERIAN_PROPAGATOR 和WSF_J2_PERTURBATION_PROPAGATOR 的轨道传播，限于地球中心天体。

# 3.6.5.4.1.5. 积分传播器 WSF_INTEGRATING_PROPAGATOR

```txt
propagator <name> WSF_INTEGRATING_propAGATOR  
integrator  
...  
end_integrator  
dynamics  
term  
...  
end_term 
```

```rst
... end_dynamics end_propagator 
```

WSF_INTEGRATING_PROPAGATOR 实现 了一 个用于 空间 域平 台的轨 道传 播器。 与WSF_KEPLERIAN_PROPAGATOR 或 WSF_NORAD_PROPAGATOR 使用解析模型来预测平台的未来状态不同，WSF_INTEGRATING_PROPAGATOR 使用数值积分。通过使用可指定的动力学模型，该传播器不限于地球在动力学中占主导地位的传播情况。

使用 WSF_INTEGRATING_PROPAGATOR 的用户需要选择一个积分器和一个动力学模型，以完全指定该传播器的行为。积分器具体说明了平台状态如何在时间上进行数值传播。动力学模型指定平台将经历的力。

注意：如果动力学模型需要依赖于平台质量的项，则需要为平台指定质量。这可以通过显式设置平台的质量来实现，或者通过在相关的 WSF_INTEGRATING_SPACE_MOVER 中使用火箭机动模型来实现。

命令

轨道积分器

integrator <orbital-integrator-name> … end_integrator

指定用于传播平台状态的积分器。每个积分器都有自己的一组输入来控制其行为。

可用的积分器：

□ Prince-Dormand 45  
□ Prince-Dormand 78

Prince-Dormand 45   
```txt
integrator prince_dormand_45 ...Embedded Runge-Kutta commands... end_integrator 
```

是一种嵌入式 Runge-Kutta 积分方案，具体为 RK5(4)7S。这种方法由 J.R. Dormand 和 P.J.Prince 在 1980 年提出，发表在《计算与应用数学杂志》上。

特性与功能

阶数与误差估计：该积分器提供了一个 5 阶的解，并使用 4 阶的误差估计器。这意味着它在计算过程中能够提供高精度的解，同时通过误差估计器来控制计算误差。

自适应步长：Prince-Dormand45 使用自适应步长来控制计算解中的误差。这种自适应性使得积分器在处理不同复杂度的问题时能够动态调整步长，从而提高计算效率和精度。

FSAL 特性：该方法具有“First Same As Last”（FSAL）的特性，这意味着在每一步的最后一个阶段的计算点与下一步的第一个阶段相同。这一特性减少了每步所需的函数评估次数，从而提高了计算效率。

应用场景

Prince-Dormand45 积分器适用于需要高精度和效率的数值计算场景，特别是在解决常

微分方程（ODEs）时。由于其自适应步长和高阶误差控制能力，它在科学计算、工程模拟和轨道计算等领域中被广泛应用。

通过选择合适的积分器，用户可以在 AFSIM中实现更精确和高效的模拟。

# Prince-Dormand 78

```txt
integrator prince_dormand_78 ...Embedded Runge-Kutta commands ... end_integrator 
```

Prince-Dormand 78 是一种嵌入式 Runge-Kutta 积分方案，具体为 RK8(7)13M。这种方法由 P.J. Prince 和 J.R. Dormand 在 1981 年提出，发表在《计算与应用数学杂志》上。

特性与功能

阶数与误差估计：该积分器提供了一个 8 阶的解，并使用 7 阶的误差估计器。这意味着它能够提供非常高精度的解，同时通过误差估计器来控制计算误差。

自适应步长：Prince-Dormand78 使用自适应步长来控制计算解中的误差。这种自适应性使得积分器在处理不同复杂度的问题时能够动态调整步长，从而提高计算效率和精度。

函数评估：该方法需要 13 次函数评估来完成每一步的积分计算，这使得它在处理复杂的常微分方程时非常有效。

应用场景

Prince-Dormand78 积分器适用于需要极高精度的数值计算场景，特别是在解决复杂的常微分方程（ODEs）时。由于其高阶误差控制能力和自适应步长特性，它在科学计算、工程模拟和天体力学等领域中被广泛应用。

通过选择合适的积分器，用户可以在 AFSIM 中实现更精确和高效的模拟，特别是在需要长时间模拟和高精度要求的情况下。

Prince-Dormand 45 和 78 都用到了下列的嵌入式命令

Embedded Runge-Kutta commands   

<table><tr><td>命令</td><td>tolerance &lt;real-value&gt;</td></tr><tr><td>解释</td><td>设定积分器单步的误差容限。默认值为1.0e-10。这是控制计算精度的重要参数,确保每一步的误差不超过指定的容限。</td></tr><tr><td>命令</td><td>max_adjustment Attempts &lt;integer-value&gt;</td></tr><tr><td>解释</td><td>设定最大步长调整尝试次数。如果无法找到合适的步长,将打印警告并继续模拟,但不再保证满足用户请求的误差容限。默认值为50。</td></tr><tr><td>命令</td><td>max_step_size &lt;real-value&gt;</td></tr><tr><td>解释</td><td>设定最大步长(以秒为单位)。如果积分器调整的步长超过此值,将使用此值作为步长。默认值实际上是无限大。</td></tr><tr><td>命令</td><td>min_step_size &lt;real-value&gt;</td></tr><tr><td>解释</td><td>设定最小允许步长(以秒为单位)。如果积分器调整的步长小于此值,将使用此值作为步长。默认值为0。注意,设置非零值可能导致计算解不再满足指定的误差容限。</td></tr><tr><td>命令</td><td>initial_step_size &lt;real-value&gt;</td></tr><tr><td>解释</td><td>设定首次积分尝试的初始步长(以秒为单位)。默认步长为0.1。</td></tr><tr><td>命令</td><td>errorCriterion &lt;error-criterion-type&gt;</td></tr><tr><td>解释</td><td>设定评估步长误差的标准。可能的值为L_infinity和L_2。选择L_infinity要求解中任</td></tr></table>

何误差分量的最大值小于指定的容限。选择 L_2 要求误差平方和的平方根小于容限。默认选项为 L_2。

# 动力学模型 Dynamical Model

```txt
dynamics <orbital-dynamics-term> end_dynamics 
```

# 动力学模型的作用

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

# 可用的动力学项

以下是一些可以用于轨道动力学模型的动力学项：

EarthMonopole: 地球的单极引力场，即地球的主要引力影响，通常是最基本的引力模型。  
EarthJ2Perturbation: 地球的 J2 摄动，考虑地球赤道隆起对航天器轨道的影响。这是地球非球对称性的一个重要修正，影响近地轨道的长时间演变。  
MoonMonopole: 月球的单极引力场，考虑月球对航天器的引力影响，特别是在地月系统中的任务。  
SunMonopole: 太阳的单极引力场，用于模拟太阳对航天器的引力作用，尤其在深空任务中非常重要。  
JupiterMonopole: 木星的单极引力场，适用于需要考虑木星引力影响的任务，如木星探测任务。  
AtmosphericDrag: 大气阻力，主要用于近地轨道的航天器，考虑大气层对航天器的阻力影响。  
Scripted: 脚本化的动力学项，允许用户通过脚本自定义特定的动力学效应或力的影响。

以下对上述项进行一一列举：

EarthMonopole：代表地球的标准开普勒两体引力场。

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
term moon_monopole gravitational_parameter <real-value> interpolation_interval <time-value> end_term 
```

<table><tr><td>命令</td><td>gravitational_parameter &lt;real-value&gt;</td></tr><tr><td>解释</td><td>指定引力参数（SI单位），默认值为4.9028e12。</td></tr><tr><td>命令</td><td>interpolation_interval &lt;time-value&gt;</td></tr><tr><td>解释</td><td>指定月球位置的插值间隔。设置为0.0可关闭插值，默认值为600秒。</td></tr></table>

term sun_monopole: 代表太阳的单极引力场。

```txt
term sun_monopole 
```

```txt
gravitational_parameter <real-value> end_term 
```

<table><tr><td>命令</td><td>gravitational_parameter &lt;real-value&gt;</td></tr><tr><td>解释</td><td>指定引力参数（SI单位），默认值为1.32712440018e20。</td></tr></table>

term jupiter_monopole: 代表木星的单极引力场。

```txt
term jupiter_monopole  
gravitational_parameter <real-value>  
end_term 
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

示例：the following script would reproduce the effect of the Earth Monopole term:

```txt
script Vec3 ScriptedEarthMonopole(WsfIntegratingSpaceMover aMover, double aMass, Calendar aTime, Vec3 aPosition, Vec3 aVelocity) Vec3 acc = aPosition.Normal(); acc.Scale(-Earth.GRAVITATIONAL_PARAMETER() / aPosition MagnitudeSquared()); return acc;   
end_script 
```

# 3.6.6. 多动运模型 WSF_MULTIRESOLUTION_MOVER

```batch
multiresolution mover WSF MultiresOLUTION_MOVER ... multiresolution mover ...   
end multiresolution mover 
```

概述

multiresolution_mover 定义了一个容器，用于在平台上保存一个或多个移动器（mover）对象，并将选择使用哪个 mover 推迟到运行时。选择 mover 是通过与组件关联的 fidelity 参数来完成的。容器中定义的每个 mover 模型都分配了一个 fidelity_range，在初始化期间根据匹配的 fidelity 设置平台上的 mover。

使用方法

定义新类型: 可以在 platform 或 platform_type 命令之外使用 multiresolution_mover 来定义新类型。

```txt
multiresolution mover<derived> WSF Multiresolution_MOVER  
fidelity <real-value>  
[add | edit] model <string-value>  
fidelity_range <real-value> <real-value>  
[default]  
mover [<mover-type>]  
... mover-specific commands ...  
end_mover  
end_model  
[add | edit] model <string-value>  
... Any number of models may be specified ...  
end_model  
common  
... mover-specific commands ...  
end_common  
endMULTIRESOLUTION_MOVER 
```

实例化对象: 可以在 platform_type 或 platform 实例上实例化一个 multiresolution_mover 对象。

```txt
platform_type ...
multiresolution_mover <type>
    ... multiresolution_mover commands ...
endMULTIRESOLUTION_MOVER
endPLATFORM_TYPE 
```

```txt
platform ...
    add multiresolution_mover <type>
        ... multiresolution_mover commands ...
    endMULTIRESOLUTION_mover
endplatform 
```

修改现有对象: 可以在 platform 实例上修改现有的 multiresolution_mover 对象。

```matlab
platform ...
    edit multiresolution mover <type>
        ... multiresolution mover commands ...
    endMULTIRESOLUTION_MOVER
endplatform 
```

命令

fidelity <real-value>: 定义组件的 fidelity 值，决定在运行时使用哪个 mover。必须在 0到 1 之间（包括 0 和 1）。此值直接映射到模型命令中定义的 fidelity_range。

默认值: 1.0

model <string-value> ... end_model: 定义或编辑包含的 mover 模型，名称由字符串给出。支持隐式添加（或编辑如果命名模型存在）以及使用 add 和 edit 命令的显式添加和编辑。

注意: 必须至少指定一个模型块。

fidelity_range <real-value> <real-value>: 定义此模型应使用的 fidelity 值范围。必须在 0到 1 之间（包括 0 和 1），按递增顺序排列，并且不得与此组件上的另一个模型的fidelity_range 重叠。

默认值: 0.0 1.0

default: 如果没有匹配的 fidelity，则使用此模型作为默认选择。  
mover <mover-type> ... end_mover: 定义 mover 模型的类型和特定于此模型实例化的参数。在首次定义新模型时需要 mover，在编辑现有模型时不得指定。  
common ... end_common: 定义要转发到所有当前指定的 mover 模型的通用参数。这些参数必须对所有当前定义的 mover 模型有效。

说明

多分辨率分析: 这种方法允许在不同的分辨率下分析和选择合适的 mover模型，以便在不同的场景中优化移动性能。  
未来改进: 计划在场景文件的其他位置提供 fidelity 选择，以提高此组件的实用性。

# 3.7. 燃料组件 fuel

在 AFSIM 中，燃料对象用于定义平台上燃料的消耗速率。对于每个平台，总质量被假定为空质量、燃料质量和有效载荷质量的总和。空质量通常是固定的，有效载荷可能只在离散事件中变化，但燃料量是连续消耗的。每当平台移动时，燃料对象会被调用并更新消耗的燃料量。计算出的燃料量会反馈给平台，以便于牛顿动力学和其他计算。

燃料类型定义语法

1、定义燃料类型（在 platform 或 platform_type 命令之外定义）：

```txt
fuel <new-type> <base-type>
... Platform Part Commands ...
maximum�数量 ...
initial�数量 ...
reserve数量 ...
mode ...
```

```txt
on_bingo ... end_on_bingo  
on_empty ... end_on_empty  
on_refuel ... end_on_refuel  
on_reserved ... end_on_reserved  
... type-specific fuel commands ...  
end_fuel 
```

2、在新平台类型上实例化燃料对象：

```matlab
platform_type ...
    fuel <type>
        ... desired attributes and commands ...
    end_fuel
endPLATFORM 
```

3、在平台实例上实例化（之前不存在的）燃料对象：

```matlab
platform ...
    add fuel <type>
        ... desired attributes and commands ...
    end_fuel
endPLATFORM 
```

4、修改平台实例上（之前存在的）燃料对象：

```matlab
platform ...
edit fuel
...
additional/changed/overwritten attributes and commands ...
end_fuel
endPLATFORM 
```

在航空和军事术语中，BINGO 状态指的是一个燃料警告状态。当飞机或平台的剩余燃料量降到一个预先设定的阈值（称为 BINGO 燃料量）以下时，平台被认为处于 BINGO 状态。这通常意味着飞机需要立即返回基地或寻找最近的加油点，以确保安全返回而不耗尽燃料。这个状态是为了提醒飞行员或操作员注意燃料不足的情况，以便采取适当的行动。

# 命令说明

maximum_quantity <mass-value>：定义可携带的最大燃料量。默认值：无限  
initial_quantity <mass-value>：定义初始燃料量。默认值： $0 \kappa \varrho$   
reserve_quantity <mass-value>：定义一个阈值，当剩余燃料量低于此值时，平台被认为在使用储备燃料。如果定义了 on_reserve 块，当达到此状态时将执行。默认值： $0 \kappa \varrho$   
bingo_quantity <mass-value>：定义一个阈值，当剩余燃料量低于此值时，平台被认为处于 BINGO 状态。如果定义了 on_bingo 块，当达到此状态时将执行。默认值：0kg  
mode<mode-name>：指定用于支持模式的燃料类型的模式名称。

# 脚本接口

在以下脚本中，预定义了以下变量：

WsfFuel this; // 当前燃料对象  
WsfPlatform PLATFORM; // 包含此燃料对象的平台  
double TIME_NOW; // 当前模拟时间

# 事件脚本

on_bingo … <script-definition> … end_on_bingo ： 定 义 当 剩 余 燃 料 量 低 于bingo_quantity 定义的阈值时执行的脚本。  
on_empty … <script-definition> … end_on_empty：定义当所有燃料耗尽时执行的脚本。  
on_reserve … <script-definition> … end_on_reserve ： 定 义 当 剩 余 燃 料 量 低 于reserve_quantity 定义的阈值时执行的脚本。  
on_refuel … <script-definition> … end_on_refuel：定义当完成加油操作时执行的脚本。

注意：如果平台没有燃料对象，运行时燃料计算将不会执行，但仍可以作为平台输入提供固定燃料量。

# 3.7.1. 燃料模型 WSF_FUEL

```txt
fuel <name>WSF_FUEL ... Platform Part Commands ... ... common fuel commands ... consumption_rate ... filter Commands ... end_fuel 
```

WSF_FUEL 实现了一个以固定速率消耗燃料的燃料对象。它提供了一些脚本方法来管理燃料消耗。

# 额外命令

除了所有标准的燃料命令外，WSF_FUEL 还增加了以下命令：

consumption_rate <mass-flow-value>：定义燃料将以固定速率消耗的速率。

这个命令允许用户指定燃料消耗的固定速率，从而更精确地模拟平台的燃料使用情况。

# 3.7.2. 坦克燃料 WSF_TANKED_FUEL（暂不可用）

```txt
fuel <new_type><base_type>
    Platform Part Commands ...
    ... :command:'Common fuel Commands <fuel> ...
    ... WSF_TABULAR_RATE_FUEL Commands ...
    // Commands associated with supplying fuel ...
    supply_method Preference ...
</base_type> 
```

```txt
supply_location Preference ... supply_point .. //Commands associated with receiving fuel... maximum_refuelquantity ... desired_top_off quantity ... maximum_received_rate ... receive_method ...   
end_fuel 
```

WSF_TANKED_FUEL 是一个特殊的嵌入在平台内的燃料对象，可以进行加油或为其他平台加油。燃料量从供应者的 WSF_TANKED_FUEL 实例转移到接收者的 WSF_TANKED_FUEL 实例。然而，目前 WSF_TANKED_FUEL 的实现是不完整的，并且已被弃用，直到另行通知。

# 额外命令

desired_top_off_quantity <mass-value>：指定期望操作燃料量的下限值。当燃料量从高于此值变为低于此值时，建议开始从附近的加油机接收燃料。脚本操作可以根据此转换采取相应的行动。默认值：0  
maximum_receive_rate <mass-flow-rate>：指定平台可以被加油的最大速率。默认值：0  
maximum_refuel_quantity <mass-value> ： 指 定 期 望 操 作 燃 料 量 的 上 限 值 。 参 见desired_top_off_quantity 以获取更多详细信息。默认值：0  
receive_method [ hose | boom ]：设置此燃料对象可以使用的接收燃料的方法。在两个油箱之间启动燃料供应操作时，加油机必须有一个与接收者配置匹配的可用燃料供应点，否则无法开始转移。默认值：NO_METHOD- 未启用接收燃料。  
supply_location_preference [ wing | center ]：设置此燃料对象可以使用的供应燃料的首选位置。默认值：NO_PREFERENCE- 没有表达加油位置的偏好。  
supply_method_preference [ hose | boom ]：设置此燃料对象可以使用的供应燃料的首选方法。在两个油箱之间启动燃料供应操作时，加油机必须有一个与接收者配置匹配的可用燃料供应点类型，否则无法开始转移。默认值：NO_METHOD- 没有表达加油方法的偏好。  
supply_point [ left | center | right ] [ boom | hose ] ‘<mass-flow-rate>’：指定燃料供应点站的最大流速。如果接收者的最大接收速率较低，则此值可能会减少。此命令应为每个可用的加油站重复。

这些命令和设置允许在模拟中更精确地控制加油操作，确保平台在需要时能够有效地进行燃料补给。

# 3.7.3. 查表多模式燃料模型 WSF_TABULAR_RATE_FUEL

```txt
fuel <name> WSF_TABULAR_RATE_FUEL
    Platform Part Commands ...
    fuel Commands ...
    fuel_table 
```

```txt
mode <mode-name>   
constant <mass-flow-value>   
speeds units <speed-units> <speed_1> ... <speed_2> end_speeds altitudes units <length-units> <altitude_1> ... <altitude_n> end_altitudes weights units <mass-units> <mass_1> ... <mass_n> endweights masses units <mass-units> <mass_1> ... <mass_n> end_masses rates units <mass-flow-units> <mass_flow_1> ... <mass_flow_n> endRates end_fuel_table   
end_fuel 
```

WSF_TABULAR_RATE_FUEL 定义了一种燃料消耗率模型。它可以在恒定速率（零个自变量）下消耗燃料，或者基于一到三个自变量（平台高度、质量（重量）和速度）以可变速率消耗燃料。默认情况下，燃料模式被忽略，只接受一个表格；但如果需要，可以为不同模式定义多个表格。通过设置燃料模式可以切换活动表格，除非新模式没有定义表格，此时活动表格将保持不变。

这 个 模 型 与 类 似 的 WSF_VARIABLE_RATE_FUEL 有 几 个 不 同 之 处 ； 特 别 是WSF_TABULAR_RATE_FUEL 表格必须是矩形的（依赖变量（速率）的数量必须与每个自变量的数量的乘积相匹配（速度数量 * 重量数量 * 高度数量）），并且 WSF_TABULAR_RATE_FUEL允许创建 1-D、2-D 或 3-D 表格。

在多维表格的 fuel_table块中，用户可以按任意顺序列出速度、高度或重量块。首先列出的自变量（IV）将被视为表格中“外部”最慢变化的索引，而最后列出的自变量将被视为“内部”最快变化的索引。相应的速率块必须具有相同的外部、中间和内部索引变化顺序。

# 命令说明

fuel_table … end_fuel_table：可以提供一个或多个 fuel_table 块。  
mode<mode-name>：指定表格有效的燃料模式。如果只提供一个燃料流量表，并且无论燃料模式如何都要使用，则不需要提供此值。如果提供了多个燃料速率表，则每个表必须提供此区分符，以便在表之间切换。  
constant <mass-flow-value>：指定恒定的燃料消耗率。  
speeds units <speed-units> <speed_1> … <speed_2> end_speeds：指定一个独立变量的任意大小的速度值数组（必须按升序排列），适用于后续的独立燃料流量值。此命令与mach命令互斥。  
mach <mach_1> … <mach_2> end_mach：指定一个独立变量的任意大小的马赫值数组（必须按升序排列），适用于后续的独立燃料流量值。此命令与 speeds 命令互斥。  
altitudes units <length-units> <altitude_1> … <altitude_n> end_altitudes：指定一个独立变量的任意大小的高度值数组（必须按升序排列），适用于后续的独立燃料流量值。  
weights units <mass-units> <mass_1> … <mass_n> end_weights：指定一个独立变量的任意大小的重量值数组（必须按升序排列），适用于后续的独立燃料流量值。（关键词“masses”是等效的。）  
masses units <mass-units> <mass_1> … <mass_n> end_masses：指定一个独立变量的任意大小的质量值数组（必须按升序排列），适用于后续的独立燃料流量值。（关键词“weights”是等效的。）  
rates units <mass-flow-units> <mass_flow_1> … <mass_flow_n> end_rates：指定与之前的

1-D、2-D 或 3-D 独立变量相对应的依赖变量值。提供的值数量必须与每个提供的维度中的独立值数量的乘积相匹配（例如，6 个速度和 4 个高度的表格必须包含 24 个燃料流量值）。

示例  
```txt
fuel FuelExample WSF_TABULAR_RATE_FUEL   
maximumquantity 7000 lb   
initialquantity 6750 lb   
reservequantity 1500 lb   
mode GROUND_IDLE # Sets the mode in the Fuel Object   
fuel_table mode FLIGHT_IDLE # Sets the mode ONLY for this table (optional) constant 800 lb/hr   
end_fuel_table   
fuel_table mode CLIMB # Sets the mode ONLY for this table (optional) altitudes units ft 02000040000   
end_altitudes mach # mutually exclusive with speeds .25.5.75 1.0   
end_mach speeds units fps 200 400 600 800   
end_speeds rates units lb/hr .25 .5 .75 1.0 mach   
3000 4500 5500 7000 # Sea Level   
2000 3500 4500 6000 # 20 kft   
1000 2500 3500 5000 # 40 kft   
endRates   
end_fuel_table   
fuel_table mode CRUISE # Sets the mode ONLY for this table (optional) weights units lb 5000 50000   
endweights   
altitudes units ft 
```

```tcl
0 20000 40000   
end_altitudes   
speeds # mutually exclusive with mach   
units fps   
200 400 600 800   
end_speeds   
rates   
units lb/hr   
# s1, s2, s3, s4   
1 2 3 4 # w1 and a1   
5 6 7 8 # w1 and a2   
9 10 11 12 # w1 and a3 #   
13 14 15 16 # w2 and a1   
17 18 19 20 # w2 and a2   
21 22 23 24 # w2 and a3   
endRates   
end_fuel_table   
end_fuel 
```

# 3.7.4. 变量速率燃料模型 WSF_VARIABLE_RATE_FUEL

```txt
fuel <name> WSF VARIABLE RATE FUEL Platform Part Commands ... Fuel.Commandst... table_for_mode <mode-name> rates altitude <length-value> speed <length-value> rate <mass-flow-value> endRates   
end_fuel 
```

WSF_VARIABLE_RATE_FUEL 是一种燃料消耗率模型。该类定义了燃料消耗行为，可以是恒定速率，也可以基于一到两个自变量（平台高度和速度）以可变速率消耗燃料。默认情况下，接受一个燃料表，与燃料模式无关。然而，如果提供了多个表，则可以为不同的燃料模式 定 义 多 个 表 ， 并 通 过 设 置 燃 料 模 式 来 切 换 活 动 表 。 这 个 模 型 与 类 似 的WSF_TABULAR_RATE_FUEL 不同，WSF_VARIABLE_RATE_FUEL 的输入格式更灵活，不需要是矩形的。WSF_TABULAR_RATE_FUEL 允许最多三个自变量，因此在需要时应优先使用，但WSF_VARIABLE_RATE_FUEL 为了与一些遗留应用程序的向后兼容性而保留。

# 命令说明

table_for_mode <mode-name>：指示以下速率定义适用于指定的模式。模式通常用于指定各种配置的消耗速率（例如，“巡航”）。用户负责通过脚本接口或自定义代码更改模式。如果未提供此命令，则速率定义普遍适用，燃料模式被忽略。  
rates … end_rates：定义燃料消耗速率的块。  
altitude<length-value>：指定后续速度数据有效的高度。高度块必须按升序排列。消耗

速率将通过当前高度的线性插值计算。

speed <length-value> rate <mass-flow-value>：指定列出的消耗速率有效的速度。速度条目必须按升序排列。消耗速率将通过当前高度和速度的线性插值计算。

这种模型允许根据平台的高度和速度动态调整燃料消耗速率，提供了更大的灵活性以适应不同的飞行条件和配置。

# 3.7.5. 旧的六自由度燃料模型 WSF_P6DOF_FUEL

```txt
fuel <name> WSF_P6DOF_FUEL
... Platform Part Commands ...
initial�数量...
reserve�数量...
bingo数量...
on_bingo ... end_on_bingo
on_empty ... end_on_empty
on_refuel ... end_on_refuel
on_reserved ... end_on_reserved
Un-Supported Commands
end_fuel 
```

WSF_P6DOF_FUEL 是 从 WSF_FUEL 派 生 的 燃 料 对 象 ， 它 的 燃 料 消 耗 速 率 由WSF_P6DOF_MOVER 决定。为了使 WSF_P6DOF_FUEL 正常工作，WSF_P6DOF_MOVER 必须存在于 WSF_PLATFORM 上。

注意：仅在包含 WSF_P6DOF_MOVER 的平台上使用 WSF_P6DOF_FUEL。如果在缺少WSF_P6DOF_MOVER 的平台上使用，WSF_P6DOF_FUEL 将抛出异常。

WSF_P6DOF_FUEL提供了一个通用的燃料对象和类似于其他基于WSF_FUEL对象的通用脚本方法。

# 命令说明

initial_quantity <mass-value>：定义要加载到飞行器上的初始燃料量。WSF_P6DOF_FUEL将与 WSF_P6DOF_MOVER 交互以设置初始燃料。燃料将首先添加到内部油箱中，保持每个油箱的填充百分比同步。例如，如果 initial_quantity是总内部燃料容量的 $7 5 \%$ ，则每个内部油箱将填充到 $7 5 \%$ ，而不会填充外部油箱。默认值： $0 \nu \mathrm { g }$   
reserve_quantity <mass-value>：定义一个阈值，当剩余燃料量低于此值时，平台被认为在使用储备燃料。如果定义了 on_reserve 块，当达到此状态时将执行。默认值： $0 \kappa \varrho$   
bingo_quantity <mass-value>：定义一个阈值，当剩余燃料量低于此值时，平台被认为达到了 BINGO 状态。如果定义了 on_bingo 块，当达到此状态时将执行。默认值： $0 \kappa \varrho$

# 不支持的命令

由于 WSF_P6DOF_FUEL 与 WSF_P6DOF_MOVER 接口，它提供了比许多其他 WSF_FUEL派生类更详细和现实的燃料系统。因此，WSF_FUEL（和 WsfFuel）提供的一些命令和方法不被支持，因为这些命令和/或脚本方法不合适。

例如，WSF_FUEL 中的 consumption_rate 命令是不合适的，因为不能指定单一值。在WSF_P6DOF_MOVER 中，燃料消耗通常动态依赖于发动机类型和油门设置以及WSF_PLATFORM的速度/马赫和高度。因此，单一值是不合适的。

WSF_P6DOF_FUEL 不支持以下燃料命令：

maximum_quantity <mass-flow-value>：燃料容量由 WSF_P6DOF_MOVER 中的燃料箱定义。如果指定了 maximum_quantity，它将被忽略，WSF_P6DOF_FUEL 将输出警告。  
mode <mode-name>：WSF_P6DOF_FUEL 和 WSF_P6DOF_MOVER 不使用燃料模式。如果指定了 mode，它将被忽略，WSF_P6DOF_FUEL 将输出警告。  
consumption_rate <mass-flow-value>：对于 WSF_P6DOF_MOVER，燃料消耗率不是单一/恒定值。如果指定了 consumption_rate，它将被忽略，WSF_P6DOF_FUEL 将输出警告。

# 脚本接口

与 WSF_FUEL 类似，WSF_P6DOF_FUEL 支持以下脚本块。每个脚本预定义以下变量：

□ WsfP6DOF_Fuel this; // 当前燃料对象  
▫ WsfPlatform PLATFORM; // 包含此燃料对象的平台  
□ double TIME_NOW; // 当前模拟时间  
□ on_bingo … <script-definition> … end_on_bingo ： 定 义 当 剩 余 燃 料 量 低 于bingo_quantity 定义的阈值时执行的脚本。  
□ on_empty … <script-definition> … end_on_empty：定义当所有燃料耗尽时执行的脚本。  
□ on_reserve … <script-definition> … end_on_reserve ： 定 义 当 剩 余 燃 料 量 低 于reserve_quantity 定义的阈值时执行的脚本。  
on_refuel … <script-definition> … end_on_refuel：定义当完成加油操作时执行的脚本。WSF_P6DOF_FUEL 还支持其他脚本方法。有关更多信息，请参见 WsfP6DOF_Fuel。

# 常见用法

使用 WSF_P6DOF_FUEL 的最常见方法是在平台类型块中定义一个燃料块。以下示例展示了如何设置初始燃料负载为 15,000 磅，并将 BINGO 燃料量设置为 4,000 磅：

```txt
platform_type ...
    fuel WSF_P6DOF_FUEL
        initial_quantity 15000 lbs
        bingo的数量 4000 lbs
    end_fuel
end-platform_type 
```

在这个例子中，initial_quantity 命令用于定义平台的初始燃料量，而 bingo_quantity 命令用于设置 BINGO 状态的燃料阈值。当燃料量降到 BINGO 阈值以下时，平台需要采取行动

以确保安全返回或寻找加油点。

# 3.7.6. 六自由度燃料模型 WSF_SIX_DOF_FUEL

```txt
fuel <name> WSF SIX DOF FUEL ... Platform Part Commands ... initialquantity ... reservequantity ... bingoquantity ... on_bingo ... end_on_bingo on_empty ... end_on_empty on_refuel ... end_on_refuel on_reserved ... end_on_reserved Un-Supported Commands end_fuel 
```

WSF_SIX_DOF_FUEL 是 从 WSF_FUEL 派 生 的 燃 料 对 象 ， 其 燃 料 消 耗 速 率 由WSF_SIX_DOF_MOVER 决定。为了使 WSF_SIX_DOF_FUEL 正常工作，WSF_SIX_DOF_MOVER必须存在于 WSF_PLATFORM 上。

注意：仅在包含 WSF_SIX_DOF_MOVER 的平台上使用 WSF_SIX_DOF_FUEL。如果在缺少WSF_SIX_DOF_MOVER 的平台上使用，WSF_SIX_DOF_FUEL 将抛出异常。

WSF_SIX_DOF_FUEL 提供了一个通用的燃料对象和类似于其他基于 WSF_FUEL 对象的通用脚本方法。

# 命令说明

initial_quantity <mass-value>：定义要加载到飞行器上的初始燃料量。WSF_SIX_DOF_FUEL将与 WSF_SIX_DOF_MOVER 交互以设置初始燃料。燃料将首先添加到内部油箱中，保持每个油箱的填充百分比同步。例如，如果 initial_quantity是总内部燃料容量的 $7 5 \%$ ，则每个内部油箱将填充到 $7 5 \%$ ，而不会填充外部油箱。默认值： $0 \nu \mathrm { g }$   
reserve_quantity <mass-value>：定义一个阈值，当剩余燃料量低于此值时，平台被认为在使用储备燃料。如果定义了 on_reserve 块，当达到此状态时将执行。默认值： $0 \kappa \varrho$   
bingo_quantity <mass-value>：定义一个阈值，当剩余燃料量低于此值时，平台被认为达到了 BINGO 状态。如果定义了 on_bingo 块，当达到此状态时将执行。默认值： $0 \kappa \varrho$

# 不支持的命令

由于 WSF_SIX_DOF_FUEL 与 WSF_SIX_DOF_MOVER 接口，它提供了比许多其他 WSF_FUEL派生类更详细和现实的燃料系统。因此，WSF_FUEL（和 WsfFuel）提供的一些命令和方法不被支持，因为这些命令和/或脚本方法不合适。

例如，WSF_FUEL 中的 consumption_rate 命令是不合适的，因为不能指定单一值。在

WSF_SIX_DOF_MOVER 中，燃料消耗通常动态依赖于发动机类型和油门设置以及WSF_PLATFORM的速度/马赫和高度。因此，单一值是不合适的。

WSF_SIX_DOF_FUEL 不支持以下燃料命令：

maximum_quantity <mass-flow-value>：燃料容量由 WSF_SIX_DOF_MOVER 中的燃料箱定义。如果指定了 maximum_quantity，它将被忽略，WSF_SIX_DOF_FUEL 将输出警告。  
mode <mode-name>：WSF_SIX_DOF_FUEL 和 WSF_SIX_DOF_MOVER 不使用燃料模式。如果指定了 mode，它将被忽略，WSF_SIX_DOF_FUEL 将输出警告。  
consumption_rate <mass-flow-value>：对于 WSF_SIX_DOF_MOVER，燃料消耗率不是单一/恒定值。如果指定了 consumption_rate，它将被忽略，WSF_SIX_DOF_FUEL 将输出警告。

# 脚本接口

与 WSF_FUEL 类似，WSF_SIX_DOF_FUEL 支持以下脚本块。每个脚本预定义以下变量：

▫ WsfSixDOF_Fuel this; // 当前燃料对象  
▫ WsfPlatform PLATFORM; // 包含此燃料对象的平台  
□ double TIME_NOW; // 当前模拟时间  
□ on_bingo … <script-definition> … end_on_bingo ： 定 义 当 剩 余 燃 料 量 低 于bingo_quantity 定义的阈值时执行的脚本。  
□ on_empty … <script-definition> … end_on_empty：定义当所有燃料耗尽时执行的脚本。  
□ on_reserve … <script-definition> … end_on_reserve：定 义当剩余 燃料量低 于reserve_quantity 定义的阈值时执行的脚本。  
□ on_refuel … <script-definition> … end_on_refuel：定义当完成加油操作时执行的脚本。  
▫ WSF_SIX_DOF_FUEL 还支持其他脚本方法。有关更多信息，请参见 WsfSixDOF_Fuel。

# 3.7.7. BRAWLER 油料模型 WSF_BRAWLER_FUEL

```txt
fuel <name> WSF_BRAWLER_FUEL ... Platform Part Commands ... ... common fuel commands ... aero_file ... initialquantity_ratio ... end_fuel 
```

WSF_BRAWLER_FUEL 实现了一种燃料对象，其燃料消耗速率由 brawler aero_file 中的参数决定。请注意，必须为此燃料类型定义 aero 文件才能正常工作。WSF_BRAWLER_FUEL 需要速度、高度和油门位置来计算燃料消耗率。它会查询平台的速度和高度，并查询平台上的移动器以获取油门位置。默认情况下，WsfMover 的 GetThrottlePosition()函数将返回 1.0，表示军用功率。移动器负责实现虚函数 GetThrottlePosition()以返回更准确的油门值。目前，进一步指定此功能的移动器包括 WsfAirMover 和 WsfBrawlerMover。

# 额外命令

除了所有标准的燃料命令外，WSF_BRAWLER_FUEL 还增加了以下命令：

aero_file <file-absolute-path>：定义用于确定燃料流量率的 brawler aero 文件的绝对路径。燃料流量率是根据平台在不同马赫数和高度值下的定义性能计算的。  
initial_quantity_ratio <real>：指定初始燃料量作为 aero_file 配置中定义的最大燃料容量的比例。

这些命令允许用户根据特定的飞行性能参数来精确控制燃料消耗，从而实现更真实的模拟。

# 3.7.8. 多燃料模型 WSF_MULTIRESOLUTION_FUEL

```txt
multiresolution_fuel WSF MultiresOLUTION_FUEL ... multiresolution_fuel ... end multiresolution_fuel 
```

multiresolution_fuel 定义了一个容器，用于在平台上保存一个或多个燃料（fuel）对象，并将选择使用哪个 fuel 推迟到运行时。选择 fuel 是通过与组件关联的 fidelity 参数来完成的。容器中定义的每个 fuel 模型都分配了一个 fidelity_range，在初始化期间根据匹配的 fidelity设置平台上的 fuel。

使用方法

定义新类型: 可以在 platform 或 platform_type 命令之外使用 multiresolution_fuel 来定义新类型。

```txt
multiresolution_fuel<derived> WSF Multiresolution_FUEL   
fidelity <real-value>   
[add | edit] model string-value> fidelity_range <real-value> <real-value> [default] fuel [<fuel-type>] ... fuel-specific commands ... end_fuel   
end_model   
[add | edit] model string-value> ... Any number of models may be specified ...   
end_model   
common ... fuel-specific commands ...   
end_common   
endMULTIRESOLUTION_FUEL 
```

实例化对象: 可以在 platform_type 或 platform 实例上实例化一个 multiresolution_fuel 对象。

platform_type ...

multiresolution_fuel <type>

```txt
... multiresolution_fuel commands ... endMULTIRESOLUTON_fuel endplatform_type 
```

```txt
platform ...
    add multiresolution_fuel <type>
        ... multiresolution_fuel commands ...
    endMULTIRESOLUTION_FUEL
endplatform 
```

修改现有对象: 可以在 platform 实例上修改现有的 multiresolution_fuel 对象。

```txt
platform ...
edit multiresolution_fuel <type>
... multiresolution_fuel commands ...
endMULTIRESOLUTION_FUEL
endPlatform 
```

# 命令

fidelity <real-value>: 定义组件的 fidelity 值，决定在运行时使用哪个 fuel。必须在 0 到 1之间（包括 0 和 1）。此值直接映射到模型命令中定义的 fidelity_range。

默认值: 1.0

model <string-value> ... end_model: 定义或编辑包含的 fuel 模型，名称由字符串给出。支持隐式添加（或编辑如果命名模型存在）以及使用 add 和 edit 命令的显式添加和编辑。

注意: 必须至少指定一个模型块。

fidelity_range <real-value> <real-value>: 定义此模型应使用的 fidelity 值范围。必须在 0到 1 之间（包括 0 和 1），按递增顺序排列，并且不得与此组件上的另一个模型的fidelity_range 重叠。

默认值: 0.0 1.0

default: 如果没有匹配的 fidelity，则使用此模型作为默认选择。

fuel <fuel-type> ... end_fuel: 定义 fuel 模型的类型和特定于此模型实例化的参数。在首次定义新模型时需要 fuel，在编辑现有模型时不得指定。

common ... end_common: 定义要转发到所有当前指定的 fuel 模型的通用参数。这些参数必须对所有当前定义的 fuel 模型有效。

# 说明

多分辨率分析: 这种方法允许在不同的分辨率下分析和选择合适的 fuel 模型，以便在不同的场景中优化燃料使用。  
未来改进: 计划在场景文件的其他位置提供 fidelity 选择，以提高此组件的实用性。

# 3.8. 武器组件 weapon

```txt
weapon <name> <type>
... Platform Part Commands ...
... Articulated Part Commands ... 
```

```txt
on | off   
update_interval   
launch_computer ...   
quantity ...   
maximum�数量...   
firing_delay ...   
firing_interval ...   
salvo_interval ...   
maximum_request_count ...   
automatic_target_cueing ...   
cue_to_predicted_intercept ...   
unknown_target_range ...   
unknown_target_altitude ...   
reload_increment ...   
reload_inventory ...   
reload_threshold ...   
reload_time ...   
inhibit_while_reloading ...   
weapon_effects ...   
end weaponry 
```

注意：某些武器命令与特定的武器模型不兼容。文档中针对受影响的模型提供了指定不兼容命令的警告。避免使用脚本方法来访问不兼容命令的参数。

# 概述

武器是一种旨在摧毁或干扰敌方平台和系统的对象。炸弹是一个旨在摧毁的武器示例，而雷达干扰器是一个旨在干扰的武器示例。

[ on | off ]

定义武器在模拟中引入时的初始状态。

默认值：WSF_EXPLICIT_WEAPON 为 on，WSF_RF_JAMMER 为 off。

update_interval <time-reference>

指定需要更新间隔的武器类型的更新间隔。

默认值：0sec。

launch_computer <type> … end_launch_computer

指定需要发射计算机的武器类型。

第一个形式用于尚未在武器上定义发射计算机时，<type> 必须是用户定义或预定义的发射计算机类型名称，参见：3.8.7 发射计算模型 launch_computer。

第二个形式用于武器上已经实例化了发射计算机时。

quantity <real-reference>

指定初始可用的弹药数量。

默认值：0.0。

maximum_quantity <real-reference>

指定武器上可能存在的最大弹药数量。这用于限制武器的重新装填。

默认值：Infinite。

firing_delay <random-time-reference>

仅适用于由 WsfWeapon.FireSalvo 或 WsfTaskManager.FireAt 发起的射击请求。指定从请求发出到请求的第一（或唯一）次射击之间将经过的时间。

默认值：0.0 sec。

firing_interval <random-time-reference>

指定武器在上次完成射击请求后到下一次射击之间必须经过的时间。

默认值：0.0 sec。

salvo_interval <random-time-reference>

仅适用于由 WsfWeapon.FireSalvo 或 WsfTaskManager.FireAt 发起的射击请求。指定多次射击请求中每轮之间的时间量。

默认值：0.0 sec。

maximum_request_count <integer-value>

指 定 可 以 同 时 激 活 的 最 大 齐 射 射 击 请 求 数 量 （ WsfWeapon.FireSalvo 或WsfTaskManager.FireAt）。

默认值：1。

automatic_target_cueing <boolean-value>

仅适用于由 WsfWeapon.FireSalvo 或 WsfTaskManager.FireAt 发起的射击请求。如果为true 并且武器支持提示，则武器将提示到请求中指定的目标。

默认值：true。

cue_to_predicted_intercept <boolean-value>

如果 automatic_target_cueing 为 true，则指定武器是否应提示到目标位置（false）或预测的拦截位置（true）。

默认值：false。

unknown_target_range <length-reference>

指定用于在射击请求中未指定目标或目标轨迹信息不足时推导目标位置的范围。

默认值：none。

unknown_target_altitude <length-reference> [ agl | msl | relative ]

指定在推导目标位置时要使用的高度。此命令仅在同时指定 unknown_target_range 时有效。

默认值：1 m agl。

reload_increment <real-reference>

指定在重新装填事件发生时从外部补给弹药库（ERM）中添加到武器中的武器库存量。

默认值：0。

reload_inventory <real-reference>

指定来自外部补给弹药库（ERM）的武器库存量，这是武器重新装填的有限来源。

默认值：0 并禁用任何重新装填能力。

reload_threshold <real-reference>

指定在启动重新装填事件时的武器库存量。重新装填潜力仅在成功武器 Fire()后评估。

默认值：0。

reload_time <random-time-reference>

指定从武器重新装填开始到完成所经过的时间。

默认值：0s。

inhibit_while_reloading <boolean-value>

指示在重新装填过程中是否禁止射击。如果为 false，射击将继续进行，直到可用数量为 0。如果为 true，任何请求将被忽略。

默认值：false。

weapon_effects <string-reference>

指定用于确定武器效能的 weapon_effects 类型。有关详细信息，请参考：3.8.6 武器效能模型 weapon effects。

注意：对于 WSF_EXPLICIT_WEAPON，通常在表示发射武器的平台定义中放置weapon_effects 命令。

# 3.8.1. 显式平台发射武器 WSF_EXPLICIT_WEAPON

```txt
weapon <name> WSF_EXPLICIT_WEAPON
... Platform Part Commands ...
... Articulated Part Commands ...
... weapon Commands ...
launchedplatform_type ...
launch_dalta_v ...
ignore_launchPLATFORM_velocity ...
require_loft_angle ...
require_intercept_point ...
commander ...
command_chain ...
dis-entity_id_offset ...
# Script Interface
on_initlize ... end_on_initlize
on_initlize2 .. end_on_initlize2
on_update ... end_on_update
script_variables ... endScript_variables
scripts ... end-script
... Other Script Commands ...
script void on_create(WsfPlatform aWeapon, WsfTrack aTarget) ... end_script
end weaponry 
```

WSF_EXPLICIT_WEAPON 表示一种在发射时被建模为独立平台的武器。

launched_platform_type <string-reference>

指定发射此类武器时要创建的平台类型。指定的值必须代表一个有效的平台类型，并且在此对象在模拟中初始化时必须定义。

默认值：无默认值，必须指定。

launch_delta_v <x-velocity> <y-velocity> <z-velocity> <speed-units>

指定由发射机制提供的相对于发射平台的附加速度向量。此值在发射部件的实体坐标系中指定（ $+ { \sf X }$ 为前方， $+ \mathsf { Y }$ 为右侧， $^ { + 7 }$ 为下方）。

注意：如果净速度小于 $1 \ : \mathsf { m } / \mathsf { s }$ ，则如果 launch_delta_v 小于或等于 $1 \ : \mathsf { m } / \mathsf { s }$ ，将使用 10$\mathsf { m } / \mathsf { s }$ 的前进速度。

默认值： $0 . 0 0 . 0 0 . 0 \mathrm { m } / s$ （即相对于发射平台速度的初始速度）。

ignore_launch_platform_velocity <boolean-value>

指定发射的显式武器的初始速度是否忽略发射平台速度的向量分量。通常，初始武器速度是 launch_delta_v 加上发射平台速度的向量和。

注意：对于船上发射的武器，最好将其设置为 true，因为典型的制导运动器的积分时间增量较大（通常设置在 0.1 到 0.5 秒之间）。

注意：如果从移动平台发射，最好将其设置为 true 以避免可能的误发。

默认值：false。

require_loft_angle   
require_intercept_point

指示 launch_computer 必须提供命令指定的属性。

commander <commander> [ command_chain <command-chain> ]

指定发射平台的指挥官。如果未提供 command_chain，则假定为默认指挥链。<commander> 可以是以下值之一：

□ 平台名称，表示指定的平台是指挥官。  
SELF，表示发射平台是其自身的指挥官。  
LAUNCHER，表示发射平台是指挥官。  
□ LAUNCHER_COMMANDER，表示发射平台的指挥官是指挥官。

此命令可以多次重复以在不同的指挥链上分配多个命令。

默认值：发射平台被指定为发射平台在其中是成员的每个指挥链的指挥官。

dis_entity_id_offset <integer-value>

将此值加到平台索引上并设置武器的 disentityid。此值用于与此武器相关的所有 DISPDU 的实体 ID 字段。这是用户在发射前和/或在 DIS 环境中对武器 ID 进行一些控制的方法。平台索引和该值的总和不得超过 65535。

默认值：0。

# 脚本接口

WSF_EXPLICIT_WEAPON 使用通用脚本接口，并提供以下功能：

script void on_create(WsfPlatform aWeapon, WsfTrack aTarget) ... end_script

定义一个在武器平台创建后但在实际插入模拟之前立即调用的脚本。此脚本通常用于修改武器平台的属性，这些属性在武器添加到模拟之前必须更改。aWeapon 是对新创建的武器平台的引用，aTarget 是对目标轨迹对象的引用。

注意：武器平台尚未初始化。它有一个名称、阵营、指挥官的名称、发射状态和目标轨迹。平台上的所有其他数据都是未定义的。

