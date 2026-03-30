对于地对空计算，计算机将始终使用目标轨迹中的“真实平台”。

此发射计算机的表格应使用 weapon_tools 实用程序生成。（参见：3.8.8.4 制导弹道导弹发射计算模型产生工具 BALLISTIC_MISSILE_LAUNCH_COMPUTER_GENERATOR ）。

# 命令

surface_to_surface_table <table_file_name>

指定用于计算与此导弹相关的发射解决方案的文件名。发射计算机假设导弹正在计算地面拦截。

注意：如果不存在预先存在的表格，则应使用 weapon_tools 实用程序生成。

surface_to_air_table <table_file_name>

指定用于计算与此导弹相关的发射解决方案的文件名。发射计算机假设导弹正在计算空中拦截。

注意：如果不存在预先存在的表格，则应使用 weapon_tools 实用程序生成。

maximum_launch_slant_range <length-value>

指定定义为可接受发射的目标最大斜距。这通常用于在发射时强制目标在跟踪传感器（假定与发射器同位）的范围内。

注意：可以使用零值来禁用此约束。

默认值：0 米（发射斜距不是约束）。

maximum_intercept_slant_range <length-value>

指定拦截点的最大允许斜距。这通常用于在拦截时强制目标在跟踪传感器（与发射器同位）的范围内。

注意：零值表示这不是约束。

默认值：0 米（拦截斜距不是约束）。

minimum_intercept_altitude <length-value>

指定定义为可接受的地对空拦截的最小高度。

默认值：0 米

maximum_intercept_altitude <length-value>

指定定义为可接受的地对空拦截的最大高度。

默认值：无限制

maximum_intercept_angle <angle-value>

指定定义为可接受的地对空拦截的最大拦截角。0 度表示正面撞击，而 180 度表示从后方撞击。

默认值：拦截角不是约束。

minimum_intercept_velocity <speed-value>

指定定义为可接受的地对空拦截的最小相对拦截速度。

默认值：拦截速度不是约束。

integration_timestep <time-value>

对于地对空发射解决方案，指定弹道目标表示向前传播的积分步长。时间间隔越小，向前弹道表示越准确，发射解决方案也越准确。通常，此值应与发射计算机表中的条目时间步长相同。例如，如果表中的时间步长间隔为 0.1 秒，则一个好的值也是 0.1 秒。

默认值：0.05 秒

ground_range_sample_interval <length-value>

指定创建内部地对空拦截表的采样间隔。

默认值：500 米

allow_boost_phase_intercept <boolean-value>

指定是否允许在助推阶段进行拦截。默认情况下，当目标仍处于“助推阶段”时，不执行拦截计算，因为轨迹预测非常不准确。将此设置为“true”允许尝试拦截。

默认值：false

compute_end_point <boolean-value>

指定发射计算机是否应计算地对空拦截计算的武器“终点和时间”。“终点和时间”是对武器（拦截器）沿弹道轨迹飞行并未击中预定目标时将撞击地球表面的估计。可以使用WsfLaunchComputer 中描述的方法提取结果。

注意：在使用此命令之前，必须为拦截器提供一个 target_data 块，定义武器最终阶段的质量和空气动力学特性。这由弹道轨迹计算使用。

默认值：false

predicted_trajectory_error_limit <length-value>

指定预测目标轨迹与实际目标轨迹之间的最大允许误差，超过此误差将强制重新计算预测目标轨迹。

默认值：250 米

show_graphics

对于地对空交战，显示最大运动学包线、投影弹道轨迹、拦截计算和拦截点的图形（这些图形显示在许多可视化工具中）。运动学包线显示从父平台发射器可以进行拦截的最大范围，以青色显示。投影弹道轨迹在计算初始拦截时间时以绿色绘制，并在第一个可能的拦截点绘制一个绿色点。否则，对于详细的拦截解决方案，轨迹以红色绘制，红点表示发射计算机尝试计算解决方案的测试点（这些可能无效）。有效的拦截点沿这些红色轨迹以紫色绘制。

show_results

显示地对空或地对地拦截计算的结果。如果成功，拦截点和抛物角/燃烧时间将显示在标准输出上，并在 DIS 流中作为注释传输/保存。

debug

除了 show_results，还显示与发射解决方案确定相关的详细信息。

目标数据命令

目标数据命令指定弹道目标表示的阻力和消耗质量的空气动力学数据。它们用于更好地计算这些目标的轨迹以获得地对空解决方案。目标数据定义不需要提供，但通常对于计算低层大气拦截至关重要。以下示例说明了 WSF 平台 DF-21B 目标的 target_data 块：

```txt
target_data DF-21B  
aero DF_21B_RV_AERO  
mass 500 kg  
end_target_data 
```

aero <aero-type-name>

指定用于计算阻力数据的空气动力学类型名称。

mass <mass-value>

指定与此目标类型相关的消耗质量。

注意：target_data 定义只需在一个 WSF_BALLISTIC_MISSILE_LAUNCH_COMPUTER 定义中指定一次。然后，发射计算机的所有实例都可以访问它。

# 3.8.7.7. 轨道运载火箭发射计算模型 WSF_ORBITAL_LAUNCH_COMPUTER

```txt
launch_computer <name> WSF_ORBITAL-LaUNCH_COMPUTER ... launch_computer Commands ... 
```

```txt
... WSF-LaUNCH COMPUTER Commands ...
... WSF_ORBITAL-LaUNCH COMPUTER Commands ...
end-Launch_computer 
```

WSF_ORBITAL_LAUNCH_COMPUTER 实现了一种用于轨道运载火箭的发射计算机。此发射计算机的表格应使用 weapon_tools 实用程序生成。请参见：3.8.8.5 轨道运载火箭发射计算模型产生工具 ORBITAL_LAUNCH_COMPUTER_GENERATOR 。

命令

leo_data <leo_data_file_name>

指定用于计算低地球轨道（LEO）发射解决方案的文件名。此文件是使用 weapon_tools实 用 程 序 的 3.8.8.5 轨 道 运 载 火 箭 发 射 计 算 模 型 产 生 工 具ORBITAL_LAUNCH_COMPUTER_GENERATOR 命令创建的。

默认值：无，必须指定。

# 3.8.7.8. 炮弹发射计算模型 WSF_FIRES_LAUNCH_COMPUTER

```txt
launch_computer <name> WSF_FIRESLAUNCH_COMPUTER ... launch_computer Commands ... ... WSF_LAUNCH_COMPUTER Commands ... fires_table ... end_fires_table end_launch_computer 
```

WSF_FIRES_LAUNCH_COMPUTER 实现了一种用于短程间接火力弹药的发射计算机。此发射计算机由 WSF_FIRES_MOVER 使用，以获取最大高度和飞行时间（给定范围）的特征轨迹值，从而计算完整的轨迹。这些离散值存储在 fires_table 中。如果可以访问美国陆军的 FireSim 表格以获取所需的系统和弹药，则可以直接使用这些表格（参见下文中的fires_table）。否则，可以从现有定义生成表格。

注意：可以在同一发射计算机定义中使用多个表格，对应于同一弹药的多个系统。

命令

fires_table SystemMunition … end_fires_table

定义一个火力表，其中包含多个条目，分别表示范围、最大高度和飞行时间。范围和最大高度以米为单位测量；飞行时间以秒为单位测量。每个条目（1,2,…n）表示一个可能的离散轨迹。

SystemMunition <string-value>提供此表格所指的系统 $\mid +$ 弹药类型。此名称应与发射武器的发射平台类型相同。

range_values <range-value-1> <range-value- $\cdot 2 >$ … <range-value-n> end_range_values定义一组特征轨迹值以表示范围。

maximum_ordinate_values <maximum-ordinate-1> <maximum-ordinate-2> …<maximum-ordinate-n> end_maximum_ordinate_values定义一组特征轨迹值以表示最大高度。

注意：必须定义 elevation_angle_values 或 maximum_ordinate_values 之一。

elevation_angle_values <elevation-angle-1> <elevation-angle-2> … <elevation-angle-n> end_elevation-angle_values

定义一组特征轨迹值以表示初始仰角。

注意：必须定义 elevation_angle_values 或 maximum_ordinate_values 之一。

time_of_flight_values <time-of-flight-value-1> <time-of-flight-value-2> … <time-of-flight-value-n> end_time_of_flight_values

定义一组特征轨迹值以表示飞行时间。

示例  
```txt
fires_table FIRES_60MM_MORTAR  
maximum_ordinate_values 2581.65 2581.3 2548.23 2510.96 2468.58 2419.26 2364.94  
2300.47 2226.98 2129.38 2038.33  
end_maximun_ordinate_values  
range_values 1596.07 1868.87 2063.09 2272.4 2458.37 2675.11 2850.41  
3075.58 3277.17 3359.59 3680.16  
end_range_values  
time_of_airport_values 46.21 46.21 45.56 45.56 44.66 44.66 43.51  
43.51 42.76 40.81 40.81  
end_time_of_Airport_values  
end_fires_table 
```

# 3.8.7.9. 地空导弹发射计算模型 WSF_SAM_LAUNCH_COMPUTER

```txt
launch_computer <name> WSF_SAM-LaUNCH COMPUTER  
... launch_computer Commands ...  
... WSF-LaUNCH_COMPUTER Commands ...  
... WSF_SAM-LaUNCH_COMPUTER Commands ..  
end-Launch_computer 
```

WSF_SAM_LAUNCH_COMPUTER 实现了一种用于地对空导弹系统的发射计算机，并列出了导弹在某个下游和高度距离发射时的预期拦截时间，假设目标在导弹飞行期间不进行机动。预期的飞行时间通过插值四维表查找获得。独立值数组（横向偏移、高度、范围、速度）在拦截结果之前提供（在 intercept_envelope 块内），这些结果是在定义的一组独立条件下获得的。

weapon_tools 应用程序协助创建此类发射计算机。（参见 ：3.8.8.6 地空导弹发射计算模型产生工具 SAM_LAUNCH_COMPUTER_GENERATOR）。

# 命令

lateral_offsets <distance-values> end_lateral_offsets

提供用于 intercept_envelope 中的第一个独立变量（变化最慢的索引）的横向偏移列表。横向偏移是目标在当前轨迹保持不变的情况下飞越发射器的水平距离。值应按升序提供，并假设效果关于发射器的视线轴对称。

altitudes <altitude-values> end_altitudes

指定用于 intercept_envelope 中的第二个独立变量的目标高度。可以不均匀，但必须按升序排列。

ranges <range-values> end_ranges

指定用于 intercept_envelope 中的第三个独立变量的地面范围。可以不均匀，但必须按升序排列。

speeds <speed-values> end_speeds

指定用于 intercept_envelope 中的第四个独立变量的目标速度。可以不均匀，但必须按升序排列。

intercept_envelope … end_intercept_envelope

此块包含定义拦截包线的数据。按照惯例，可以从表格中省略任何不成功的拦截点，并假设飞行时间为-1.0 秒（未命中）。示例中给出的五个索引值由类 weapon_tools 生成器打印出，并用于确保在流解析器读取数据时正确索引。

intercept_envelope   
```txt
"intercept" intercept_index lateral_offset_index  
lateral_offset_value altitude_index altitude_value  
ground_range_index ground_range_value speed_index  
speed_value time_of_flight_value  
intercept 0 0 0 m 0 300 m 0 0 m 1 50 m/s 31.3536 sec  
intercept 1 0 0 m 0 300 m 0 0 m 4 200 m/s 19.9911 sec  
intercept 2 0 0 m 0 300 m 0 0 m 5 250 m/s 20.5551 sec  
intercept 3 0 0 m 0 300 m 0 0 m 6 300 m/s 21.9581 sec  
intercept 4 0 0 m 0 300 m 0 0 m 7 350 m/s 23.5001 sec  
end_intercept_envelope 
```

interpolation_test … end_interpolation_test

仅用于调试目的，是可选的。在此块中可以放置一个或多个 lateral_offset<distance-value>、 altitude <distance-value>、target_speed <speed_value> 和 ground_range<distance_value> 规格。每次出现关键字 test 时，最近的（偏移、高度、速度、范围）值将保存为测试点，并存储到测试点数组中。发射计算机初始化后，将评估每个测试点，并将相应的插值飞行时间值打印到屏幕上。

interpolation_test   
```txt
lateral_offset 4000 m altitude 2000 m ground_range 10000 m target_speed 120 m/s test ground_range 20000 m test lateral_offset 2000 m 
```

```txt
test end_interpolation_test 
```

这些命令和结构帮助定义和评估地对空导弹系统的拦截能力，确保在不同条件下的有效性和准确性。

# 3.8.7.10.脚本发射计算模型 WSF_SCRIPT_LAUNCH_COMPUTER

```c
launch_computer <name> WSFScriptLAUNCH_COMPUTER ... launch_computer Commands ... script void compute_intercept(WsfTrack aTrack, double aLaunchDelay) end_script end_launch_computer 
```

WSF_SCRIPT_LAUNCH_COMPUTER 实现了一种使用脚本语言来确定是否可以进行拦截的发射计算机。这种计算机允许用户通过脚本来定义拦截逻辑。

# 示例实现

以下示例展示了如何实现基于脚本的发射计算机。这个示例非常简单，假设目标以恒定速度直线飞行，并且武器以定义的平均速度飞行。示例展示了：

□ 所需的方法名称和签名。  
□ 预定义的脚本变量。  
▫ 如何报告拦截结果。

请注意，必须调用 WsfLaunchComputer.SetInterceptTime 来报告成功的拦截。如果不调用此方法，将表示无法进行拦截。

# 示例脚本

launch_computer_ MyScriptLaunchComputer WSF-scriptLAUNCHCOMPUTER script void compute_intercept(WsfTrack aTrack, double aLaunchDelay) // Assume target is flying straight and level at a constant speed double targetSpeed $=$ aTrack.GetSpeed(); double weaponSpeed $= 300.0$ ; // Example weapon speed in m/s double distanceToTarget $=$ aTrack.GetDistance(); // Calculate time to intercept double timeToIntercept $=$ distanceToTarget / (weaponSpeed - targetSpeed); // Check if intercept is possible if (timeToIntercept $>0$ ) { WsfLaunchComputer.SetInterceptTime(timeToIntercept); } end_script   
end_launch_computer

说明

□ 方法名称和签名：compute_intercept(WsfTrack aTrack, double aLaunchDelay) 是所需的方法签名。  
□ 预定义的脚本变量：aTrack 提供目标的轨迹信息。  
□ 拦截结果报告：使用 WsfLaunchComputer.SetInterceptTime(timeToIntercept) 来报告成功的拦截时间。

这个脚本假设目标和武器的速度是已知的，并且目标在飞行过程中不进行机动。通过计算目标和武器之间的相对速度，可以确定拦截所需的时间。

示例

launch_computer EX-LaUNCH COMPUTER WSFScriptLAUNCHCOMPUTER # This is the required script method name and signature.   
script void compute_intercept(WsfTrack aTrack, double aLaunchDelay) # If needed the following additional script variables are pre-defined: # WEAPON references the WsfWeapon to which the launch computer is attached. # PLATFORM references the WsfPlatform to which the weapon is attached. double weaponSpeed $= 500.0$ ; #Assumed weapon speed WsfWaypoint intercept $=$ WsfWaypoint(); double tti $\equiv$ PLATFORM.InterceptLocation2D(aTrack, intercept, weaponSpeed, aLaunchDelay); if (tti > 0.0) { WsfGeoPoint interceptPoint = WsfGeoPoint.Construct(interceptLatitude(), intercept.Longitude(), aTrack.Altitude()); SetInterceptPoint(interceptPoint); # The next call is the minimum requirement for reporting an intercept. SetInterceptTime(TIME NOW +tti); SetLaunchTime(TIME NOW + aLaunchDelay); SetTimeOfFlight(tti - aLaunchDelay); } end_script   
end_launch_computer

# 3.8.8. 发射计算工具 weapon_tools

weapon_tools 是一个可选的 WSF 模块，可以集成到 WSF 应用程序中，也可以作为独

立 可 执 行 文 件 分 发 。 weapon_tools 在 各 种 交 战 条 件 下 反 复 发 射 预 定 义 的WSF_EXPLICIT_WEAPON，捕获命中/未命中结果以量化该武器类型的交战能力，从而允许成功地对目标轨迹进行武器部署。该工具生成一个或多个文件，这些文件定义了未来模拟或场景中将使用的运行时软件对象。weapon_tools 是可扩展的，目前允许创建/生成以下武器部署对象：

空对空发射计算机，通过 AIR_TO_AIR_LAUNCH_COMPUTER_GENERATOR。  
空对地（ATG）发射可接受区域（LARs）和发射计算机，通过 ATG_LAR_AND_LC_GENERATOR。  
弹道发射计算机，通过 BALLISTIC_LAUNCH_COMPUTER_GENERATOR。  
弹道导弹发射计算机，通过 BALLISTIC_MISSILE_LAUNCH_COMPUTER_GENERATOR。  
轨道发射计算机，通过 ORBITAL_LAUNCH_COMPUTER_GENERATOR。  
地对空导弹（SAM）发射计算机，通过 SAM_LAUNCH_COMPUTER_GENERATOR。

命令行使用

使用独立的 weapon_tools.exe：

```xml
weapon.tools.exe <input-files> 
```

对于支持 weapon_tools 的其他 WSF 应用程序：

```xml
wsf.application.exe --weapon-tools <input-files> 
```

命令

tool <tool-type-name> … end_tool：定义工具类型，其中 <tool-type-name> 是概述中给出的选项之一。

# 工具命令

tool_debug：启用运行时调试输出。默认值：关闭。  
terminate_on_launch_failure <boolean-value>：如果为 true，当武器未能发射时工具将终 止 。 此 命 令 仅 适 用 于 AIR_TO_AIR_LAUNCH_COMPUTER_GENERATOR 、ATG_LAR_AND_LC_GENERATOR 和 BALLISTIC_LAUNCH_COMPUTER_GENERATOR。默认值：true。  
position <latitude> <longitude>：指定发射平台的地理位置。默认值： $0 . 0 \mathsf { n } , 0 . 0 \mathsf { e }$   
altitude <length-value>：指定武器发射的高度。默认值： $_ { 0 . 0 \mathsf { m } }$   
heading <angle-value>：指定发射平台的罗盘方向。默认值： $0 . 0 { \mathsf { d e g } }$   
frame_step <time-value>：工具更新之间的时间间隔。默认值：0.5 sec。  
launch_platform_type <platform-type> ： 指 定 将 发 射 武 器 的 平 台 类 型 。 默 认 值 ：LAUNCH_PLATFORM_TYPE。  
target_platform_type <platform-type> ： 指 定 将 被 攻 击 的 平 台 类 型 。 默 认 值 ：TARGET_PLATFORM_TYPE。  
weapon_name <weapon-name>：指定发射平台上使用的武器名称。默认值：发射平台类型上遇到的第一个武器。

weapon_effects <effect-name> ： 指 定 发 射 武 器 平 台 将 用 于 确 定 目 标 效 果 的weapon_effects（致命性）模型。默认值：WEAPON_TOOL_LETHALITY。  
tool_produces <product-name>：指定武器工具的输出产品。此值用于自动命名输出文件。典型值包括 _LAUNCH_COMPUTER 或 _LAUNCH_ACCEPTABLE_REGION 等。默认值：UNKNOWN_PRODUCT。  
output_object_name <output-name>：指定武器工具的输出产品。此值用于自动命名输出文件。默认值：_UNKNOWN_PRODUCT。  
output_file_extension <extension-name>：指定武器工具输出产品的文件扩展名。默认值：.txt。  
output_file_name <file-name>：指定工具生成的文件的名称。默认值：output_object_name$^ +$ output_file_extension 的连接。

这些命令和参数帮助定义了武器在不同交战条件下的有效性和性能，确保在复杂的战斗环境中能够做出最佳决策。

# 3.8.8.1. 空 空 发 射 计 算 模 型 产 生 工 具AIR_TO_AIR_LAUNCH_COMPUTER_GENERATOR

```batch
tool AIR_TO_AIR-LaUNCH COMPUTER_GENITOR ... weapon.tools Commands ... ..COMMANDSCommands... .WSF_AIR_TO_AIR-LaUNCH_COMPUTERCommands ... end_tool 
```

AIR_TO_AIR_LAUNCH_COMPUTER_GENERATOR 是 weapon_tools 的一个专业化工具，用于 生 成 WSF_AIR_TO_AIR_LAUNCH_COMPUTER 。 该 生 成 器 内 部 包 含 一 个WSF_AIR_TO_AIR_LAUNCH_COMPUTER 实例，该实例被修改为最终的输出产品，因此许多命令在两者之间是通用的。发射计算机是通过一个大型的空对空交战条件矩阵创建的。工具会遍历这一交战条件矩阵，在选定条件下放置一个空中射手和目标。交战会在不同的距离上重复进行，以得出三个值：最小值、最大值和无逃逸距离，以及每次的武器飞行时间。迭代过程是一个二分搜索，目的是找到使交战从成功转变为失败或反之的临界条件（距离）。目标被放置后，立刻向其发射武器，并提供一个完美的跟踪。导弹飞出，如果在运动学上有可能，目标会被拦截并摧毁。注意，在足够小的未命中距离下，击杀概率应为 1.0。如果交战结果是目标被击杀，距离和飞行时间会被保存到结果数组中。如果目标未被击杀（在任何距离上），则记录为-1。该过程会在每个交战条件下重复。当所有交战结果被记录后，结果会被写入一个 WSF 输入格式的文本文件，定义适用于该武器发射的条件。

影响空对空战斗中致命范围的交战自变量

这些变量包括射手高度和马赫数、目标高度和马赫数、目标的方位角和目标的引导角。目标的方位和引导都是从速度矢量到交战中另一个参与者的视线测量的。值得注意的是，用于考虑交战的条件矩阵保存在 WSF_AIR_TO_AIR_LAUNCH_COMPUTER 中，并且输入命令定义了该生成器将考虑的测试条件矩阵。此发射计算机对象聚合在此生成器对象中，因此它将接受相同的命令作为有效输入。

警告

AIR_TO_AIR_LAUNCH_COMPUTER_GENERATOR 不支持任何具有延迟发射时间的发射平台。

# 命令

minimum_range <distance-value>

要测试的最短交战距离。默认值 $= 1 0 0 0$ 米。

maximum_range <distance-value>

要测试的最长交战距离。默认值 $= 1 2 0 { , } 0 0 0$ 米。

range_tolerance <distance-value>

这是一个收敛测试值；如果找到两个交战距离，它们包围[成功，失败]并且它们的差异小于公差值，则认为找到了过渡边界。

maximum_iterations <positive-integer>

这是一个终止搜索约束；如果在每次交战的迭代次数内未达到收敛，则停止该交战的迭代。

# 示例

```txt
********** WEAPON TOOL INPUT FILE - Air-to-Air Launch Computer Generator 
```

```txt
# 
```

```txt
Example input data file to configure and exercise the Air-to-Air Launch Computer 
```

```txt
# Generator Weapon Tool. Examples for all possible input keywords and values 
```

```txt
are given below; however, default values are often sufficient, and when so, 
```

```txt
# the input keyword and its corresponding default value is commented out to 
```

```txt
show the input is not mandatory. 
```

```txt
# 
```

```batch
include ../base_types/weapons/aam/aim-9x.txt 
```

```javascript
\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* 
```

```txt
This lethality is "perfect" if within lethal range. Necessary, because 
```

```txt
# for the Tool to work properly we must have a kill if the missile is 
```

```txt
kinematically able to pass within lethal range of its target. 
```

```txt
NOTE: The weapon's fuse should not have 'hit_proximity_range' set 
```

```txt
greater than the radius indicated below. 
```

```txt
weapon_effects WEAPON_TOOL_LETHALITY WSF_GRADUATED_LETHALITY 
```

```python
radius_and_PK 30.0 ft 1.00 # All Platforms 
```

```txt
endweapon_effects 
```

```txt
The following is used as the launch platform type 
```

```txt
platform_type LAUNCH_PLATFORM_TYPE WSF_PLATFORM 
```

```txt
icon F-18E 
```

```tcl
# (The default weapon fired by all Weapon Tools is the first one
# encountered on the launch platform.)
weapon launching weaponry AIM-9X endweapon
endplatform_type
# The following is used as a target
platform_type TARGET_PLATFORM_TYPE WSF_PLATFORM
icon F-18
mover TARGET_MOV end_mover
endplatform_type
tool AIR_TO_AIR_LAUNCH Computer Generator
# === Tool Input Keywords ===
# toolDebug
# The inputs below position the test case somewhere
# on the globe, and indicate the firing conditions
# altitude 10000 ft # ATA Launcher defaults to 10000 ft alt.
# position 00:00n 00:00w
#heading 0 deg
position 34:54n 117:53w # Near Edwards AFB
#frame_step 0.5 sec # Time interval between Tool updates
#target-platform_type TARGET_PLATFORM_TYPE
#launch-platform_type LAUNCH_PLATFORM_TYPE
# The default is to select the first weapon on the launchplatform_type
#weapon_name <firstweapon_on_launchPLATFORM_type> # (No matter what it is named.)
# (The PK should usually boosted to 1.0 for this generator to work properly.)
# weapon_effects WEAPON_TOOL_LETHALITY
# The following two string values are used to assist with naming output
# objects and files, if the names are not explicitly provided by user input.
# tool_produces_ata_launch_computer
#output_file_extension.txt 
```

```txt
The user may have letter case preferences on file names, or a preferred naming # convention, so may choose to explicitly override the two Tool-provided names below: # 1. Output object name # (If not provided, the default name is to aggregate the two items shown below.) #output_object_name <weapon-platform_type><toolProduces> # 2. Output file name # (If not provided, the default name is to aggregate the two items shown below.) #output_file_name <output_object_name><output_file_extension> output_object_name AIM-9X_ATA_LAUNCH COMPUTER_10KFT_0.6MACH # *** TEMPORARY NON_DEFAULT OVERRIDE output_file_name aim-9x_ata_LAunched_computer_alt10kft_0.6mach.txt # *** TEMPORARY NON_DEFAULT OVERRIDE #=== WsfAirToAirLaunchComputer Input Keywords --- #maximum_iterations 20 #range_tolerance 5 m #minimum_range 1000.0 m #maximum_range 12000.0 m #=== The file included and read in below will specify the independent --- #=== variable engagement conditions for which results are generated --- #load_table test_air_to_air_launch_computer_table.txt #=== OR ALTERNATELY, READ IN IV's BELOW --- #=== (NO DV's are given here, as the Tool will Generate them.) --- launch_computer_table noescape_mechanuever 7 g independent_variables shooter_altitudes 10000 ft 20000 ft 30000 ft end_shooter_altitudes shooter_machs 0.8 1.0 1.2 end_shooter_machs target_altitudes 10000 ft 20000 ft 30000 ft end_target_altitudes shooter_machs 0.8 1.0 1.2 end_target_machs target_aspects 0 deg 30 deg 60 deg 90 deg 135 deg 180 deg end_target_aspects target LeadAngles 0 deg 30 deg 60 deg 90 deg 135 deg 180 deg end_target LeadAngles end_independent_variables end_launch_computer_table 
```

```txt
end_tool  
dis_INTERFACE record lc_generation.rep  
end_dis-interface 
```

# 3.8.8.2. 空地发射计算模型产生工具 ATG_LAR_AND_LC_GENERATOR

```txt
tool ATG_LAR_AND_LC Generator
    ... weapon.tools Commands ...
    altitude_and_mach <length-value> <float-value>
    altitude_and_speed <length-value> <speed-value>
    target_lateralOffsets <length-value> <quantity>
    target_offsetsets <length-value> <quantity>
    target_forward_offsetsets <minimum-value> <delta-length-value> <quantity>
    shrink_factor <positive-floating-point-quantity>
    switch_sides
end_tool 
```

ATG_LAR_AND_LC_GENERATOR 是 weapon_tools 的一个专业化工具，用于生成发射可接受区域（LAR）和用于发射空对地制导武器的发射计算机（这些计算机将使用 LAR）以对地面目标进行攻击。为了生成 LAR，将静止的地面目标放置在发射飞机的横向和纵向偏移矩阵上，并进行攻击。当发射的武器能够机动以拦截给定的地面目标时，该目标将被标识为可攻击的。一个多边形形状的 LAR 将从所有可攻击目标位置的极限边缘定义出来。为了在对未知因素使用武器时保持保守，可以应用一个 shrink_factor，如果需要，它将线性缩小 LAR 围绕其自身的质心。

命令

altitude_and_mach <length-value> <float-value>

提供空对地武器发射的高度和马赫数。功能上等同于 altitude_and_speed。接受多个发射条件。

altitude_and_speed <length-value> <speed-value>

提供空对空导弹发射的平台速度。接受多个发射条件。

target_lateral_offsets <length-value> <quantity>

提供横向偏移的长度和数量（从发射平台的中心线），在这些位置上放置地面目标并进行攻击。总是测试从发射飞机的零横向偏移（目标在发射飞机的中心线），并假设 LAR 关于发射飞机的横向平面对称。

默认值：500.0 米，5 个偏移

target_offsets <length-value> <quantity>

与上述“target_lateral_offsets”同义（为了向后兼容）。

target_forward_offsets <minimum-value> <delta-length-value> <quantity>

提供最小前向偏移（最负值；允许负数）、增量长度和目标偏移的数量（从发射平台），在这些位置上放置地面目标并进行攻击。如果预计 LAR 包含当前飞机位置后面的点，则最小值必须小于零。总是测试从发射飞机的横向偏移（目标在发射飞机的中心线），并假设 LAR

关于发射飞机的横向平面对称。

默认值：1000.0 米（最小），500.0 米（增量），10 个偏移

shrink_factor <positive-floating-point-quantity>

提供一个因子（ $0 . 0 <$ 因子 $< 1 . 0$ ）以缩小 LAR 的大小，从而在武器使用中应用保守性。

默认值：1.0

switch_sides

结果重放文件的默认输出显示在发射平台的右侧。此命令将输出切换到左侧。

示例  
```cmake
include the weapon file of choice   
include myweapon.txt # 500lb version   
weapon_effects WEAPON_TOOL_LETHALITY WSF_GRADUATED_LETHALITY radius_and_pk 15.0 ft 1.00 # All Platforms   
endweapon_effects   
platform_type LAUNCH_PLATFORM_TYPE WSF_PLATFORM icon F-18E weapon launchingweapon MYWEAPON endweapon   
end-platform_type   
platform_type TARGET_PLATFORM_TYPE WSF_PLATFORM   
icon Ground_Radar   
end-platform_type   
tool ATG_LAR_AND_LCGenerator position 00:00n 00:00w output_object_name myweapon_ATG_LAUNCHCOMPUTER_20KFT_MACH_0.8 \# \*\*   
TEMPORARY NON_DEFAULT OVERRIDE output_file_name myweapon_atg_launch_computer_20kft_mach_0.8.txt # \*\* TEMPORARY NON_DEFAULT OVERRIDE   
# altitude_and_mach 40000 ft 0.8 targetRanges 40 miles 5.0 miles 26   
# altitude_and_mach 40000 ft 1.2 targetRanges 50 miles 5.0 miles 27   
# altitude_and_mach 40000 ft 1.4 targetRanges 60 miles 5.0 miles 28   
# altitude_and_mach 35000 ft 0.8 targetRanges 40 miles 5.0 miles 23   
# altitude_and_mach 35000 ft 1.2 targetRanges 40 miles 5.0 miles 27   
# altitude_and_mach 35000 ft 1.4 targetRanges 55 miles 5.0 miles 28   
# altitude_and_mach 25000 ft 0.8 targetRanges 40 miles 5.0 miles 20   
# altitude_and_mach 25000 ft 1.2 targetRanges 50 miles 5.0 miles 23   
# altitude_and_mach 25000 ft 1.4 targetRanges 50 miles 5.0 miles 24   
altitude_and_mach 20000 ft 0.8 targetRanges 40 miles 5.0 miles 18   
# altitude_and_mach 20000 ft 1.2 targetRanges 40 miles 5.0 miles 22   
# altitude_and_mach 20000 ft 1.4 targetRanges 45 miles 5.0 miles 23 
```

```julia
# altitude_and_mach 15000 ft 0.8 targetRanges 30 miles 5.0 miles 17
# altitude_and_mach 15000 ft 1.2 targetRanges 35 miles 5.0 miles 19
# altitude_and_mach 15000 ft 1.4 targetRanges 40 miles 5.0 miles 20
# altitude_and_mach 10000 ft 0.8 targetRanges 25 miles 5.0 miles 15
# altitude_and_mach 10000 ft 1.2 targetRanges 35 miles 5.0 miles 16
# altitude_and_mach 10000 ft 1.4 targetRanges 40 miles 5.0 miles 17
# altitude_and_mach 5000 ft 0.8 targetRanges 25 miles 5.0 miles 13
# altitude_and_mach 1000 ft 0.8 targetRanges 25 miles 5.0 miles 10
# targetRanges 40 miles 5.0 miles 21 # min, delta, number of target offsets forward of
the launcher
# targetRanges 40 miles 2.5 miles 50 # min, delta, number of target offsets forward of
the launcher
# targetOffsets 10.0 miles 4 # delta, number of target offsets lateral to the launcher
targetOffsets 15.0 miles 3 # delta, number of target offsets lateral to the launcher
# targetOffsets .1 meter 2 # delta, number of target offsets lateral to the launcher
# shrink_factor 0.8
end_tool
dis_INTERFACE
#record myweapon.rep
end_dis/interface
#event_output
# file myweapon.evt
# enable WEAPON_HIT
# enable WEAPON_MISSED
# enable WEAPON_TERMINATED
#end_event_output
script void WeaponHit(WsfWeaponEngagement aWeaponEngagement, WsfPlatform
aTargetPlatform)
WsfPlatform weapon = aWeaponEngagement.WeamerPlatform();
WsfGeoPoint launchpoint = aWeaponEngagement.WeanLocationAtLaunch();
WsfGeoPoint weaponpoint = aWeaponEngagement.WeanLocation();
double groundrange = launchpoint.GroundRangeTo(weaponpoint);
double timeofflight = aWeaponEngagement.TimeStarted();
writeln(weapon.MachNumber(), "", weapon.Speed(), "", weapon.Pitch(), "", groundrange,
",timeofflight");
end.script
observer
enable WEAPON_HIT
end observer 
```

# 3.8.8.3. 非 制 导 弹 道 武 器 发 射 计 算 模 型 产 生 工 具BALLISTIC_LAUNCH_COMPUTER_GENERATOR

```txt
tool BALLISTIC-LaUNCH_comPUTER_GENITOR
... weapon.tools Commands ...
launch_altitudes <minimum-altitude> <delta-altitude> <number-of-altitudes>
launch_speeds <minimum-speed> <delta-speed> <number-of-speeds>
target_altitudes <minimum-altitude> <delta-altitude> <number-of-altitudes>
end_tool 
```

BALLISTIC_LAUNCH_COMPUTER_GENERATOR 是 weapon_tools 的一个专业化工具，用于生成发射计算机，以释放无制导的弹道武器，如重力炸弹。该工具将在各种交战高度和速度下释放武器，并捕获由此产生的下游行程和飞行时间，以达到目标。生成的发射计算机定义文件将检查当前飞行速度和目标上方的高度，并预测在足够远的上游释放武器，以便将武器投放到目标轨迹位置。（由于武器没有横向制导，发射飞机必须垂直飞越目标。）

命令

launch_altitudes <minimum-altitude> <delta-altitude> <number-of-altitudes>武器释放所需的发射高度。假设高度是发射器在椭球地球上的高度。默认值：1000.0 米（最小），1000.0 米（增量），10 个高度  
launch_speeds <minimum-speed> <delta-speed> <number-of-speeds>武器释放时发射器的速度。默认值：120.0 米/秒（最小），30.0 米/秒（增量），4 个速度  
target_altitudes <minimum-altitude> <delta-altitude> <number-of-altitudes>放置目标以进行攻击的高度。假设高度是目标在椭球地球上的高度。默认值：0.0 米（最小），50.0 米（增量），10 个高度

# 3.8.8.4. 制 导 弹 道 导 弹 发 射 计 算 模 型 产 生 工 具BALLISTIC_MISSILE_LAUNCH_COMPUTER_GENERATOR

```txt
tool BALLISTIC_MISSILE_LAUNCH Computer Generator ... weapon.tools Commands ... air_target_file surface_target_file gnuplot_file minimum_output_time maximum_output_time minimum_output_range maximum_output_range maximum_output_altitude limited_to_preapogee loft_angle loftangles 
```

```txt
burn_time   
burn(times   
pass_1_loft_angle_start   
pass_1_loft_angle_stop   
pass_1_loft_angle_step   
pass_2_loft_angle_step   
loft_angle_range   
depress_angle_range   
end_tool 
```

BALLISTIC_MISSILE_LAUNCH_COMPUTER_GENERATOR 是 weapon_tools 的一个专业化工具，用于生成发射计算机，以协助制导弹道导弹的目标定位和发射。该工具将以各种抛物角和/或推进剂燃烧时间发射定义的导弹类型，并捕获由此产生的轨迹特征，以便在以后用于空中拦截弹道导弹的撞击或拦截时间和位置的目标定位。任何时候导弹定义被修改以影响其运动学时，都应重新应用此生成器以创建新的发射计算机数据表。为了使相同的发射数据表可以在全球任何地方使用，假设使用一个球形非旋转地球模型。

# 抛物角

大型远程弹道导弹垂直发射，然后迅速转向某个名义上的“抛物角”，从该角度开始，重力引起的转弯将它们保持在弹道轨迹上，朝向所需的（最大范围）目标点。最大可实现的下游轨迹对初始抛物角的微小变化非常敏感（抛物角的两度增量可能很容易导致短程地球撞击或导弹进入轨道）。此武器工具生成器允许用户选择一系列抛物角，并选择所需的角度分辨率以迭代收敛到“最佳”发射解决方案。通常，较小范围的拦截或撞击仍然使用相同的“最佳”抛物角，但提前终止推进以导致较低、较短范围的轨迹撞击或拦截。实现较短范围撞击的替代方法是抛物或压低轨迹，其中选择高于或低于最佳的抛物角以实现所需的目标范围撞击。抛物轨迹牺牲了更长的飞行时间，而压低轨迹可能因高空高速飞行而遭受气动加热问题。

# 使用制导移动器

在 为 WSF_BALLISTIC_MISSILE_LAUNCH_COMPUTER 生 成 数 据 时 ， 不 应 使 用 某 些WSF_GUIDED_MOVER 命令，因为它们可能以意想不到的方式改变导弹的飞行路径，可能导致生成错误的数据。这些命令包括但不限于偏转命令（divert_thrust、divert_fuel_mass、divert_fuel_flow_rate、divert_altitude_limits）。然而，一旦生成了发射计算机数据，这些命令可以在执行任务或 Warlock 时在为武器定义的 WSF_GUIDED_MOVER 中使用。

# 生成过程

生成器首先以低（平）抛物角迭代发射导弹，每次发射时增加抛物角。导弹的终端撞击最初会每次增加。当接近最佳抛物角时，终端范围将达到最大值，然后再次开始减少。如上段所述，这种效应是高度非线性的。因此，使用两步迭代方法，首先使用“粗略”较大的增量抛物角（0.2 度是一个好的起点），当找到近似最佳抛物角时，重新运行“精细”迭代循环以捕获更准确的最佳抛物角值（大约 0.001 度步长）。此过程需要 a）关于抛物角限制和增量

的智能选择，并进行人工调整，或 b）大量迭代和大量计算时间来生成表格。一旦确定了最佳抛物角（及其结果范围），则通过如上所述的抛物或压低轨迹实现次优目标范围。

# 命令

air_target_file <air-target-file-name>

包含生成的地对空轨迹数据的输出文件的名称。

surface_target_file <surface-target-file-name>

包含生成的地对地轨迹数据的输出文件的名称。

gnuplot_file <gnu-plot-file-name>

用于后处理可视化的绘图文件的名称。

minimum_output_time <time-value>

导弹飞行时间的最小值，低于此值的拦截或撞击被视为无效。

maximum_output_time <time-value>

导弹飞行时间的最大值，超过此值的拦截或撞击被视为无效。

minimum_output_range <distance-value>

导弹飞行地面范围的最小值，低于此值的拦截或撞击被视为无效。

maximum_output_range <distance-value>

导弹飞行地面范围的最大值，超过此值的拦截或撞击被视为无效。

maximum_output_altitude <altitude-value>

测试拦截解决方案成功的最大高度。

limited_to_preapogee

如果拦截发生在顶点后，则排除将其视为可行的标志。

loft_angle <angle-value>

用于轨迹传播的单一抛物角值。通常仅用于小型短程弹道导弹。实现各种下游轨迹的自变量是推进剂燃烧时间。

loft_angles from <min-angle-value> to <max-angle-value> by <delta-angle-value>

用于轨迹传播测试的抛物角范围。

burn_time <time-duration-value>

用于轨迹传播的单一燃烧时间值。

burn_times from <min-time-duration-value> to <max-time-duration-value> by <delta-duration-value>

用于生成名义轨迹特征发射表（燃烧时间）作为所需目标范围的函数。确定最小和最大持续时间值时，请确保添加级间延迟时间。不能与 loft_angle_range 或 depress_angle_range关键字一起使用。

pass_1_loft_angle_start <angle-value>

第一次遍历（粗略遍历）以找到最佳抛物角的起始抛物角。此值高度依赖于导弹运动学……对于笨重的导弹更大（更垂直），对于有活力的导弹更小（更水平）。注意：选择过高或过低的值可能导致生成器错误地预测最佳抛物角。

pass_1_loft_angle_stop <angle-value>

第一次遍历（粗略遍历）以找到最佳抛物角的结束抛物角。由于迭代是随着抛物角的增加进行的，因此此值必须大于 pass_1_loft_angle_start。此值高度依赖于导弹运动学……对于笨重的导弹更大（更垂直），对于有活力的导弹更小（更水平）。注意：选择过高或过低的值可能导致生成器错误地预测最佳抛物角。

pass_1_loft_angle_step <angle-value>

第一次遍历抛物角的增量值（粗略遍历）。推荐的起点是 0.2 度。

pass_2_loft_angle_step <angle-value>

第一次遍历抛物角的增量值（精细遍历）。推荐的起点是 0.001 度。

loft_angle_range max_angle <angle-value> max_loft <angle-value> by <angle-value>

仅用于生成抛物轨迹特征发射表。参数 max_angle 和 max_loft 都可以独立终止迭代循环。max_angle 参数是抛物角的绝对值，而 max_loft 参数是相对于预先计算的最佳抛物角的相对值。不能与 burn_times 或 depress_angle_range 关键字一起使用。

depress_angle_range min_angle <angle-value> max_depress <angle-value> by <angle-value>

仅用于生成压低轨迹特征发射表。参数 min_angle 和 max_depress 都可以独立终止迭代循环。min_angle 参数是抛物角的绝对值，而 max_loft 参数是相对于预先计算的最佳抛物角的相对值。不能与 burn_times 或 loft_angle_range 关键字一起使用。

# 3.8.8.5. 轨 道 运 载 火 箭 发 射 计 算 模 型 产 生 工 具ORBITAL_LAUNCH_COMPUTER_GENERATOR

tool ORBITAL_LAUNCH_COMPUTER_GENERATOR

```txt
... weapon.tools Commands ...  
speed ...  
pitch ...  
leo_data_file ...  
launch Heading ...  
launch headings ...  
loft_angle ...  
loftAngles ...  
pitch_rate ...  
pitchRates ... 
```

end_tool

ORBITAL_LAUNCH_COMPUTER_GENERATOR 是 weapon_tools 的一个专业化工具，用于生成发射计算机，以协助发射轨道运载火箭。该工具将以各种发射航向和抛物角发射定义的运载火箭类型，并捕获结果数据，以便在以后用于发射到轨道的计算。

每当发射运载火箭的定义以某种方式修改以影响其运动学时，应重新执行此生成器以创建新的发射计算机数据表。

# 通用命令

speed <speed-value>

指定发射平台的速度。仅当发射平台是飞机时使用。

默认值： $0 \ : \mathsf { m } / \mathsf { s }$

注意：发射平台不得定义为移动器。

pitch <angle-value>

指定发射平台的俯仰角。仅当发射平台是飞机且速度大于零时使用。

默认值：0 度

注意：发射平台不得定义为移动器。

leo_data_file <leo-data-file-name>

为低地球轨道（LEO）计算生成的文件的名称。

默认值：无 - 必须提供。

launch_heading <angle-value>

用于轨迹传播的单一发射航向值。

默认值：如果未指定 launch_heading 或 launch_headings，则使用 weapon_tools 命令heading 中指定的值。

launch_headings from <angle-value> to <angle-value> by <angle-value>

用于轨迹传播测试的发射航向范围。

默认值：如果未指定 launch_heading 或 launch_headings，则使用 weapon_tools 命令heading 中指定的值。

loft_angle <angle-value>

用于轨迹传播的单一抛物角值。

默认值：无。必须指定至少一个 loft_angle 或 loft_angles 命令。

loft_angles from <angle-value> to <angle-value> by <angle-value>

用于轨迹传播测试的抛物角范围。

默认值：无。必须指定至少一个 loft_angle 或 loft_angles 命令。

# 俯仰率调整命令

轨道运载火箭通常包括一个阶段，使火箭从垂直飞行过渡到其上升轨迹。由于制导方法的普遍性质，上升轨迹和结果轨道高度对“俯仰过渡”阶段结束时的条件极为敏感。为了使这些命令有效，火箭必须在俯仰过渡阶段使用 FLIGHT_PATH_ANGLE_PROGRAM。该程序中的一个命令是 pitch_rate 命令。程序结束时的条件由此速率控制，因此它对结果轨道有巨大影响。

确定此速率的良好值需要一些迭代。这些命令允许您定义一组俯仰率，用于执行launch_heading/loft_angle 矩阵。对于每个俯仰角，执行并总结整个发射航向和抛物角集。通常，您运行一个单一的发射航向（90 度）和一组合理的抛物角。第一次运行通常使用较大的俯仰角范围和增量（0.20 度/秒到 0.50 度/秒，每次增量 0.10 度/秒）。第二次和第三次运行通常通过缩小范围和缩小增量来锁定候选值。一旦找到一个值，“最佳”值就用作FLIGHT_PATH_ANGLE_PROGRAM 中 pitch_rate 的值。然后，您可以继续使用完整的发射航向和抛物角范围生成实际的发射计算机。

pitch_rate <angle-rate-value>

覆盖任何 FLIGHT_PATH_ANGLE_PROGRAM 在火箭上的 pitch_rate 值的单一俯仰率值。默认值：无，不需要。

pitch_rates from <angle-rate-value> to <angle-rate-value> by <angle-rate-value>

覆盖任何 FLIGHT_PATH_ANGLE_PROGRAM 在火箭上的 pitch_rate 值的俯仰率范围。

默认值：无，不需要。

# 3.8.8.6. 地空导弹发射计算模型产生工具 SAM_LAUNCH_COMPUTER_GENERATOR

```batch
tool SAM-LaUNCH COMPUTER_GENITOR 
```

```txt
... weapon.tools Commands ...
... WSF_SAM-LaUNCH COMPUTER Commands ...
...
... test_matrix ... end_test_matrix ...
...
... post_generation_interpolation/tests ... end_post_generation_interpolation/tests ...
re数据分析Produced_input_file
//Tracker Information
tracker_height ...
tracker_name ...
tracker_elevationlimits ...
effective-earth_radius ...
end_tool 
```

SAM_LAUNCH_COMPUTER_GENERATOR 是 weapon_tools 的一个专业化工具，用于生成用于发射地对空导弹的发射计算机。

命令

test_matrix … end_test_matrix

在此块中列出了要评估的目标轨迹测试条件，以成功拦截导弹。需要提供四个不同的数组：lateral_offsets、altitudes、speeds 和 ranges。每个数组可以使用以下语法设置：a) from<start-value> to <end-value> by <delta-value>，或 b) 列表，如 <value-1> <value- $\cdot 2 >$ <value- $\ B >$ …<end-value>。所有值必须按升序排列，但间隔不必均匀，可以结合使用 from-to-by 语法和枚举列表。

altitudes <distance-values> end_altitudes

评估轨迹拦截的高度。格式如上所述。

lateral_offsets <altitude-values> end_lateral_offsets

评估轨迹拦截的横向偏移。格式如上所述。

ranges <range-values> end_ranges

评估轨迹拦截的目标地面范围。格式如上所述。

speeds <speed-values> end_speeds

评估轨迹拦截的速度。格式如上所述。

post_generation_interpolation_tests … end_post_generation_interpolation_tests

仅用于调试目的，是可选的。在此块中可以放置一个或多个 lateral_offset、altitude、ground_range 和 target_speed 规格。每次出现关键字 test 时，最近的（偏移、高度、速度、范围）值将保存为测试点，并存储到测试点数组中。生成发射计算机后，将评估每个测试点，并将相应的飞行时间值打印到屏幕上。

lateral_offset <length-value>

指定插值测试点的轨迹横向偏移。

altitude <length-value>

指定插值测试点的轨迹高度。

ground_range <length-value>指定插值测试点的轨迹地面范围。

target_speed <speed-value>指定插值测试点的轨迹目标速度。

test

保存最近的（偏移、高度、范围和速度）值，并将其存储为要进行插值测试的点。结果将打印到屏幕上。

re_parse_produced_input_file

生成并写入发射计算机后，重新打开文件并尝试通过正常流输入处理读取它。默认情况下不检查文件。

tracker_height <length-value>

设置跟踪雷达的地面高度。这用于地平线遮蔽计算，如果目标交战被地球曲率遮蔽，将禁用武器发射。如果未输入此参数的值，则不考虑地平线遮蔽，仅使用导弹运动学计算发射包线。

tracker_name <sensor-name>

通过指定传感器名称来设置跟踪器高度的替代方法。如果未指定跟踪器高度而指定了跟踪器名称，则从其定义中解析跟踪器高度。指定的传感器必须存在于发射平台上。

tracker_elevation_limits <angle-value> <angle-value>

设置跟踪雷达将运行的最小和最大仰角。超出这些限制的目标仰角将抑制武器发射。

默认值：-180 度， $\yen 180$ 度（无限制）

effective_earth_radius <ratio-value>

设置有效地球半径比。必须大于零。

默认值：4/3

# 3.9. UCI 组件 uci_component

```txt
uci_component <type> <base_type> ... Platform Part Commands ... subsystem_uuid ... subsystem Descriptor ... end_uci_component 
```

# 概述

Universal Command and Control Interface (UCI) 是一个用于在平台组件之间发送和接收消息和命令的接口，基于 Critical Abstraction Layer (CAL) 规范。当前使用的 CAL 版本是 75。此扩展需要 ActiveMQ 作为处理消息的中间件。要将模拟连接到 ActiveMQ，需要一个Reference CAL (RefCAL) 配置文件。通过环境变量 CAL_ACTIVEMQ_CONFIG 设置 RefCAL 配置文件。该文件配置所有平台和组件的通用唯一标识符 (UUID)，以便模拟可以向正确的平台、传感器等发送消息/命令。

# 组件

为了发送 UCI 消息，每个平台组件必须在其所属平台上附加一个相应的 UCI_Component。

要接收 UCI 消息，平台必须有一个 COMPUTER 组件。

▫ <type>: 定义的 UCI 组件类型。  
□ <base_type>: 现有 UCI 组件类型或预定义 UCI 类型的名称。

预定义的 UCI 基础类型包括：

▫ AMTI   
□ COMPUTER   
▫ ESM   
□ IRST   
□ WEAPON

在平台类型上实例化：

```txt
platform_type <type> <base_type>
    uci_component <name> <type>
    ...
    end_uci_component
end-platform_type 
```

向平台添加 uci_component：

```perl
platform <name> <type>
    add uci_component <name> <type>
        ...
    end_uci_component
end-platform 
```

编辑平台上的 uci_component：

```txt
platform <name> <type>
    edit uci_component <name>
    ...
    end_uci_component
end-platform 
```

删除平台上的 uci_component：

```perl
platform <name> <type>
    delete uci_component <name>
    ...
    end_uci_component
end-platform 
```

命令

subsystem_uuid <string-value>: 设置对应子系统的 UUID。

注意: UUID 应该是格式为 ‘########-####-####-####-############’ 的字符串，其

中 # 是大写字母或数字 [A-Z0-9]。

默认值: 由接口自动生成。

subsystem_descriptor <string-value>: 设置子系统的人类可读描述。

说明

ActiveMQ 和 RefCAL 配置: 确保正确配置 ActiveMQ 和 RefCAL，以便平台和组件能够正确通信。

UUID 格式: 确保 UUID 格式正确，以避免识别和通信错误。

组件管理: 使用提供的命令来添加、编辑或删除平台上的 UCI 组件，以确保系统的灵活性和可扩展性。

# 3.9.1. AMTI 组件 AMTI Component

```txt
uci_component <type> AMTI   
sensor <string-value> mode_uuid ... default_mode_uuid ...   
Part Commands ...   
uci_component Commands ...   
end_uci_component 
```

概述

AMTI 是 与 WSF_RADAR_SENSOR 对 应 的 UCI 组 件 。 将 AMTI 组 件 链 接 到WSF_RADAR_SENSOR 允许传感器发送 UCI 消息。

命令

sensor <string-value>: 要链接的传感器名称。  
mode_uuid <mode-name> <uuid-value>: 将能力（模式）UUID 设置为给定值。此命令等同于“capability_uuid”命令。

注意: UUID 应该是格式为 ‘########-####-####-####-############’ 的字符串，其中 # 是大写字母或数字 [A-Z0-9]。

default_mode_uuid <uuid-value>: 将索引 0 的模式设置为给定的 UUID 值。

注意: UUID 应该是格式为 ‘########-####-####-####-############’ 的字符串，其中 # 是大写字母或数字 [A-Z0-9]。

# 部件命令

update_message_interval <time-value>: 组件发送更新消息的间隔。  
capability_uuid <capability-name> <uuid-value>: 将能力 UUID 设置为给定值。

□ 注意: UUID 应该是格式为 ‘########-####-####-####-############’ 的字符串，其中 # 是大写字母或数字 [A-Z0-9]。  
□ 消息类型  
□ 所有消息类型都可以通过脚本方法发送。

Activity: UCI_AMTI_ActivityMessage 在以下事件中发送：

□ 接收到并接受 UCI_AMTI_CommandMessage   
▫ 完成 UCI_AMTI_Command  
□ 传感器开/关   
□ 传感器模式激活/停用  
□ 更新间隔

Capability: UCI_AMTI_CapabilityMessage 在更新间隔时发送。

CapabilityStatus: UCI_AMTI_CapabilityStatusMessage 在以下事件中发送：

□ 接收到并接受 UCI_AMTI_SettingsCommandMessage   
□ 传感器开/关   
▫ 传感器模式激活/停用  
□ 更新间隔

Command: UCI_AMTI_CommandMessage 仅在脚本中发送。

CommandStatus: UCI_AMTI_CommandStatusMessage 在以下事件中发送：

□ 接收到并处理 UCI_AMTI_CommandMessage（每个消息中的命令一个）  
□ 接收到并处理 UCI_AMTI_SettingsCommandMessage  
□ 注意: 尚未在脚本中实现

ControlRequest: UCI_ControlRequestMessage 仅在脚本中发送。  
▪ ControlRequestStatus: UCI_ControlRequestStatusMessage 在以下事件中发送：  
□ 接收到并处理 ControlRequestMessage（每个消息中的控制对象一个）

ControlStatus: UCI_ControlStatusMessage 在以下事件中发送：

□ 接收到并处理 ControlRequestMessage（每个消息中的控制对象一个）  
□ 更新间隔

Entity: UCI_EntityMessage 在以下事件中发送：

□ 传感器轨迹启动  
□ 传感器轨迹更新

SettingsCommand: UCI_AMTI_SettingsCommandMessage 仅在脚本中发送。  
SettingsCommandStatus: UCI_AMTI_SettingsCommandStatusMessage 在以下事件中发送：

□ 接收到并处理 UCI_AMTI_SettingsCommandMessage  
□ 注意: 尚未在脚本中实现

SubsystemStatus: UCI_SubsystemStatusMessage 在以下事件中发送：

□ 传感器开/关   
□ 更新间隔

SystemStatus: UCI_SystemStatusMessage 在以下事件中发送：

□ 传感器开/关   
□ 更新间隔   
□ 注意: 尚未在脚本中实现

说明

UUID 格式: 确保所有 UUID 的格式正确，以避免识别和通信错误。

消息发送: 根据需要配置和发送不同类型的消息，以确保系统的有效通信和状态更新。

# 3.9.2. 计算机组件 UCI_COMPUTER

uci_component <type> COMPUTER

uci_component Commands ...

```txt
end_uci_component 
```

概述

UCI_COMPUTER 是一个 UCI 组件，使平台能够通过 internal_links 和抽象服务总线（ASB）发送、接收和处理 UCI 消息。每个具有 uci_component 的平台必须有一个计算机，并且每个 uci_component 必须与该计算机连接才能发送消息。

在下面的示例中，平台 EXAMPLE 拥有一个 IRST 和一个 ESM 传感器，它们可以通过各自的 uci_components 发送和接收 UCI 消息。每个组件都有一个到计算机的 internal_link，计算机将其接收到的消息发送到 ASB。计算机到传感器 uci_component 的 internal_link 将其从 ASB 接收到的消息发送以进行处理。

示例

platform EXAMPLE WSF_PLATFORM   
```txt
uci_component computer COMPUTER internal_link esm_uci_component internal_link irst_uci_component end_uci_component   
add sensor irst WSFIRST_SENSOR sensor irst internal_link computer   
end_sensor   
add sensor esm WSF ESM SENSOR sensor esm internal_link computer   
end_sensor   
endPLATFORM 
```

说明

计算机组件: 每个平台必须包含一个 COMPUTER 组件，以便通过 UCI 进行消息传递和处理。

内部链接:internal_link 用于连接传感器组件和计算机组件，以确保消息能够在平台内正确传递和处理。

抽象服务总线 (ASB): 计算机组件通过 ASB 发送和接收消息，确保平台内外的通信。

通过这种设置，平台上的传感器可以有效地与其他系统组件进行通信，支持复杂的指挥和控制操作。

# 3.9.3. ESM 组件 ESM Component

```txt
uci_component <type> ESM 
```

```txt
sensor <string-value> mode_uuid ... default_mode_uuid ... Part Commands ... uci_component Commands ... end_uci_component 
```

# 概述

ESM 是 与 WSF_ESM_SENSOR 对 应 的 UCI 组 件 。 将 ESM 组 件 链 接 到WSF_ESM_SENSOR 允许传感器发送 UCI 消息。

# 命令

sensor <string-value>: 要链接的传感器名称。

mode_uuid <mode-name> <uuid-value>: 将能力（模式）UUID 设置为给定值。此命令等同于“capability_uuid”命令。

□ 注意: UUID 应该是格式为 ‘########-####-####-####-############’ 的字符串，其中 # 是大写字母或数字 [A-Z0-9]。

default_mode_uuid <uuid-value>: 将索引 0 的模式设置为给定的 UUID 值。

□ 注意: UUID 应该是格式为 ‘########-####-####-####-############’ 的字符串，其中 # 是大写字母或数字 [A-Z0-9]。

# 部件命令

update_message_interval <time-value>: 组件发送更新消息的间隔。

capability_uuid <capability-name> <uuid-value>: 将能力 UUID 设置为给定值。

注意: UUID 应该是格式为 ‘########-####-####-####-############’ 的字符串，其中 # 是大写字母或数字 [A-Z0-9]。

# 消息类型

所有消息类型都可以通过脚本方法发送。

Activity: UCI_ESM_ActivityMessage 在以下事件中发送：

□ 接收到并接受 UCI_ESM_CommandMessage   
□ 完成 UCI_ESM_Command  
□ 传感器开/关   
□ 传感器模式激活/停用  
▫ 更新间隔

Capability: UCI_ESM_CapabilityMessage 在更新间隔时发送。

CapabilityStatus: UCI_ESM_CapabilityStatusMessage 在以下事件中发送：

接收到并接受 UCI_ESM_SettingsCommandMessage   
□ 传感器开/关   
传感器模式激活/停用  
□ 更新间隔

Command: UCI_ESM_CommandMessage 仅在脚本中发送。  
CommandStatus: UCI_ESM_CommandStatusMessage 在以下事件中发送：

□ 接收到并处理 UCI_ESM_CommandMessage（每个消息中的命令一个）  
□ 接收到并处理 UCI_ESM_SettingsCommandMessage  
□ 注意: 尚未在脚本中实现

ControlRequest: UCI_ControlRequestMessage 仅在脚本中发送。

▪ ControlRequestStatus: UCI_ControlRequestStatusMessage 在以下事件中发送：

□ 接收到并处理 ControlRequestMessage（每个消息中的控制对象一个）

ControlStatus: UCI_ControlStatusMessage 在以下事件中发送：

□ 接收到并处理 ControlRequestMessage（每个消息中的控制对象一个）  
▫ 更新间隔

Entity: UCI_EntityMessage 在以下事件中发送：

▫ 传感器轨迹启动  
▫ 传感器轨迹更新

SettingsCommand: UCI_ESM_SettingsCommandMessage 仅在脚本中发送。  
SettingsCommandStatus: UCI_ESM_SettingsCommandStatusMessage 在以下事件中发送：

▫ 接收到并处理 UCI_ESM_SettingsCommandMessage  
▫ 注意: 尚未在脚本中实现

SubsystemStatus: UCI_SubsystemStatusMessage 在以下事件中发送：

□ 传感器开/关   
□ 更新间隔

SystemStatus: UCI_SystemStatusMessage 在以下事件中发送：

▫ 传感器开/关   
□ 更新间隔   
□ 注意: 尚未在脚本中实现

说明

UUID 格式: 确保所有 UUID 的格式正确，以避免识别和通信错误。

消息发送: 根据需要配置和发送不同类型的消息，以确保系统的有效通信和状态更新。

# 3.9.4. IRST 组件 IRST Component

```txt
uci_component <type> IRST sensor <string-value> mode_uuid ... default_mode_uuid ... Part Commands ... uci_component Commands ... end_uci_component 
```

概述

IRST 是 与 WSF_IRST_SENSOR 对 应 的 UCI 组 件 。 将 IRST 组 件 链 接 到

WSF_IRST_SENSOR 允许传感器发送 UCI 消息。

# 命令

sensor <string-value>: 要链接的传感器名称。  
mode_uuid <mode-name> <uuid-value>: 将能力（模式）UUID 设置为给定值。此命令等同于“capability_uuid”命令。

注意: UUID 应该是格式为 ‘########-####-####-####-############’ 的字符串，其中 # 是大写字母或数字 [A-Z0-9]。

default_mode_uuid <uuid-value>: 将索引 0 的模式设置为给定的 UUID 值。

注意: UUID 应该是格式为 ‘########-####-####-####-############’ 的字符串，其中 # 是大写字母或数字 [A-Z0-9]。

# 部件命令

update_message_interval <time-value>: 组件发送更新消息的间隔。  
capability_uuid <capability-name> <uuid-value>: 将能力 UUID 设置为给定值。

注意: UUID 应该是格式为 ‘########-####-####-####-############’ 的字符串，其中 # 是大写字母或数字 [A-Z0-9]。

# 消息类型

所有消息类型都可以通过脚本方法发送。

Activity: UCI_POST_ActivityMessage 在以下事件中发送：

□ 接收到并接受 UCI_POST_CommandMessage   
▫ 完成 UCI_POST_Command  
□ 传感器开/关   
□ 传感器模式激活/停用  
更新间隔

Capability: UCI_POST_CapabilityMessage 在更新间隔时发送。  
CapabilityStatus: UCI_POST_CapabilityStatusMessage 在以下事件中发送：

□ 接收到并接受 UCI_POST_SettingsCommandMessage   
□ 传感器开/关   
▫ 传感器模式激活/停用  
□ 更新间隔

Command: UCI_POST_CommandMessage 仅在脚本中发送。  
CommandStatus: UCI_POST_CommandStatusMessage 在以下事件中发送：

□ 接收到并处理 UCI_POST_CommandMessage（每个消息中的命令一个）  
□ 接收到并处理 UCI_POST_SettingsCommandMessage  
□ 注意: 尚未在脚本中实现

ControlRequest: UCI_ControlRequestMessage 仅在脚本中发送。  
ControlRequestStatus: UCI_ControlRequestStatusMessage 在以下事件中发送：

□ 接收到并处理 ControlRequestMessage（每个消息中的控制对象一个）

ControlStatus: UCI_ControlStatusMessage 在以下事件中发送：

□ 接收到并处理 ControlRequestMessage（每个消息中的控制对象一个）  
更新间隔

Entity: UCI_EntityMessage 在以下事件中发送：

□ 传感器轨迹启动  
▫ 传感器轨迹更新

SettingsCommand: UCI_POST_SettingsCommandMessage 仅在脚本中发送。  
SettingsCommandStatus: UCI_POST_SettingsCommandStatusMessage 在以下事件中发送：

接收到并处理 UCI_POST_SettingsCommandMessage  
□ 注意: 尚未在脚本中实现

SubsystemStatus: UCI_SubsystemStatusMessage 在以下事件中发送：

□ 传感器开/关   
□ 更新间隔

SystemStatus: UCI_SystemStatusMessage 在以下事件中发送：

▫ 传感器开/关   
□ 更新间隔   
▫ 注意: 尚未在脚本中实现

说明

UUID 格式: 确保所有 UUID 的格式正确，以避免识别和通信错误。

消息发送: 根据需要配置和发送不同类型的消息，以确保系统的有效通信和状态更新。

# 3.9.5. 武器组件 Weapon Component

```txt
uci_component <type> WEAPON  
Part Commands ...  
uci_component Commands ...  
end_uci_component 
```

概述

WEAPON 组件负责处理平台上所有武器的 StrikeUCI 消息。

命令

此组件的命令部分未详细列出，但通常涉及与武器系统相关的操作和配置。

消息类型

所有消息类型都可以通过脚本方法发送，除非另有说明。

Activity: UCI_StrikeActivityMessage 将在以下事件中发送：

□ 注意: 尚未实现

Capability: UCI_StrikeCapabilityMessage 将在更新间隔时发送。   
CapabilityStatus: UCI_StrikeCapabilityStatusMessage 将在更新间隔时发送。   
Command: UCI_StrikeActivityMessage 将在以下事件中发送：

□ 注意: 尚未实现

CommandStatus: UCI_StrikeActivityMessage 将在以下事件中发送：

注意: 尚未实现

ControlRequest: UCI_ControlRequestMessage 仅在脚本中发送。

ControlRequestStatus: UCI_ControlRequestStatusMessage 将在以下事件中发送：▫ 当接收到并处理 ControlRequestMessage 时（每个消息中的控制对象一个）  
ControlStatus: UCI_ControlStatusMessage 将在以下事件中发送：▫ 当接收到并处理 ControlRequestMessage 时（每个消息中的控制对象一个）▫ 更新间隔  
SettingsCommand: UCI_StrikeSettingsCommandMessage 将在以下事件中发送：□ 注意: 尚未实现  
SettingsCommandStatus: UCI_StrikeActivityMessage 将在以下事件中发送：□ 注意: 尚未实现  
SubsystemStatus: UCI_SubsystemStatusMessage 将在更新间隔时发送。  
SystemStatus: UCI_SystemStatusMessage 将在更新间隔时发送。□ 注意: 尚未在脚本中实现

说明

消息发送: 根据需要配置和发送不同类型的消息，以确保武器系统的有效通信和状态更新。

未实现功能: 某些消息类型和命令尚未实现，可能需要在未来的系统更新中添加。

# 4. 全局定义与其它

该部分定义了一些相对全局的定义，他可能被一部分使用，但是也可能被其它的部分使用，并不能很好的归类为平台或组件，均放在此章节中。

# 4.1. 公共脚本接口 Common Script Interface

公共脚本接口定义了所有使用接口的公共机制。对脚本的使用做框架做的说明。

许多 WSF 组件使用 WSF 的“通用脚本接口”。使用该接口的 WSF 组件将接受以下内容：

• 脚本变量的定义：script_variables … end_script_variables  
• 脚本的定义：script … end_script  
• 脚本系统控制命令（例如，script_call_trace）  
• 通用脚本（如下所述）

当前实现通用脚本接口的 WSF 组件包括：

• 仿真系统  
• 平台  
• 一些处理器，如 WSF_SCRIPT_PROCESSOR 等  
• 一些其他平台部件，如传感器

示例  
```txt
processor my-script-proc WSFScript PROCESSOR update_interval 10 sec on_update writeln("T=",TIME NOW, "",PLATFORM.Name(),"is updating"); end_on_update   
end Processor 
```

# 预定义变量

所有使用通用脚本接口的组件将具有以下适用于该组件的预定义变量：

doubleTIME_NOW：当前仿真时间（秒）。适用于所有脚本。

WsfPlatformPLATFORM：平台的引用。仅在实现通用脚本接口的平台、传感器和处理器中有效。

WsfProcessorPROCESSOR：处理器的引用。仅在使用通用脚本接口的处理器中有效（例如，WSF_SCRIPT_PROCESSOR）。

WsfSensorSENSOR：传感器的引用。仅在 AFSIM 的预定义传感器以及使用通用脚本接口的其他传感器中有效。

WsfRandomRANDOM：仿真使用的随机数生成器的引用。使用此对象将影响仿真的随机抽取，因此会影响仿真结果的可重复性。

# 通用脚本

每个使用通用脚本接口的 WSF 组件将接受以下通用脚本：

• execute at_time <time-value> [ absolute | relative ] …script body… end_execute   
• execute at_interval_of <time-value> …script body… end_execute

这些命令允许你定义一个脚本，该脚本将在特定时间执行一次或在指定时间间隔内重复执行。

在特定时间执行脚本：

```txt
execute at_time <time-value> [absolute | relative ]  
Script Body  
end_execute 
```

如果指定了 absolute，则脚本将在指定的仿真时间执行。如果指定了 relative，则脚本将在相对于平台创建时间的指定时间执行。

在指定间隔内重复执行脚本：

```txt
execute at_interval_of <time-value>  
Script Body  
end_execute 
```

注意：如果在处理器的上下文中定义，这些脚本即使在系统关闭时也会执行，因为脚本的目的是可能打开系统：

on_initialize …script_body… end_on_initialize 这个命令允许你定义一个脚本，该脚本将在平台初始化的第一阶段执行（如果在平台上下文中定义），或在仿真初始化期间执行（如果在全局脚本上下文中定义）。  
• on_initialize2 …script_body… end_on_initialize2 这个命令允许你定义一个脚本，该脚本将在平台初始化的第二阶段执行。第二阶段初始化发生在所有平台及其组件（包括同一平台上下文中的组件）完成第一阶段初始化之后。此外，平台上下文中的第二阶段初始化仅在全局上下文中的第一阶段初始化之后发生。  
• on_update …script_body… end_on_update 这个命令允许你定义一个脚本，该脚本将在平台或处理器更新时执行。当在处理器上下文中指定时，update_interval 命令定义仿真调用 Update 方法的间隔。

# 军事特定

使用该接口的 WSF 组件将接受：

• 一些武器，如 WSF_EXPLICIT_WEAPON。  
• 一些预定义变量，如 WsfWeaponWEAPON：武器的引用。仅在使用通用脚本接口的武器中有效（例如，WSF_EXPLICIT_WEAPON）。

# 4.2. 分布式接口 dis_interface

```txt
dis-interface   
#Connection Commands   
connections...end(connections edit Connections... end_edit connections record <filename> playback<filename> broadcast<broadcast-IP-address> multicast<multicast-IP-address><interface-address> unicast<unicast-address> 
```

```tcl
port <IP-port-number>   
send_port <IP-port-number>   
receive_port <IP-port-number>   
time_to_live <ttl-value>   
#Filtered Output Connection Commands   
filtered_connection ... end-filtered_connection allow entity_type [all / tracked <by force>] allow force [all / tracked <by force>]   
# Simulation Control Commands   
protocol_version <protocol-version-id>   
exercise <dis-exercise-id>   
site <dis-site-id>   
application <dis-application-id>   
join exercise   
no_join_exercise   
autostart   
no_autostart   
deferred_connection_time <time-value>   
absolute_timestamp   
ignore_pdu_time   
use_pdu_time   
mover_update_timer <time-value>   
heartbeat_timer <time-value>   
heartbeat-multiplier <real-value>   
initial_distribution_interval <time-value>   
entity_position_threshold <length-value>   
entity_orientation_threshold <angle-value>   
maximum_beam_entries <positive-integer>   
maximum_track_jam_entries <positive-integer>   
sensor_update_interval <time-value>   
#Mapping Commands   
force <side> <dis-force-id>   
entity_type <platform_type> <dis-entity-type>   
unknownplatform_type <platform-type>   
entity Appearance ... end-entity Appearance   
articulated_part <platform-type> <part-name> <part-id> ... end-articulated_part emitter_type <sensor/jammer-type> <dis-emitter-name-enum> emitter_function <sensor/jammer-type> <dis-emitter-function-enum> 
```

```txt
beam_type <sensor/jammer-type>
<sensor/jammer-mode-name>
<sensor/jammer-beam-number>
<dis-beam-parameter-index-value>
beam_function <sensor/jammer-type>
<sensor/jammer-mode-name>
<sensor/jammer-beam-number>
<dis-beam-function-enum-value>
entity_id <platform_name>
<entity-number>
start_entity <dis-entity>
private [name | type | category | all ]
# Filtering Commands
filter_out_by_site_and_app
ignorekind_and_domain <kind>
ignore_type <dis-entity_type>
ignore_pdu_type <string>
filter_out_by_range <platform-name>
<length-value>
# Other Commands
debug_emission_pdu <level>
enterprise entity_types to <target-name>
enterprise emitter_types to <target-name>
log_created Entities
no_periodic_palus_while_PAused
multi_thread
multi_thread.Sleep_time <time-value>
max Allowed bad entity_states <integer-value>
send_periodic_palus_while_PAused
suppress_non_STANDARD_data <boolean-value>
suppress_comm_data <boolean-value>
suppress_emissions_data <boolean-value>
usesimpleAccelerations
usesimpleOrientationRates
usebody-angular_ Velocities
zero_body-angular_ Velocities
# External DIS Mover Commands
map_externalEntity <dis-entity-id>
map_external_type <dis-entity-type>
end_dis-interface 
```

dis_interface 块用于指定分布式交互仿真（DIS）接口的属性。DIS 接口提供了参与 DIS演习或创建可以通过可视化工具显示的重放文件的能力。使用 broadcast 或 multicast 命令参与 DIS 演习。使用 record 命令生成重放文件。

可以提供多个 dis_interface 块。如果在多个块中指定了相同的子命令，则将使用最后给出的值。

警告

命令 mover_update_timer 和 heartbeat_timer 可能会在仿真中强制更新移动器。将mover_update_timer 设置为 0.0 秒，并将心跳计时器设置为非常大的值（例如大于仿真结束时间），将防止在仿真中移动平台，直到事件需要它们为止。

# 连接命令

这些命令定义了仿真如何与其他仿真参与者连接。

<table><tr><td>命令</td><td>connections ... end Connectionsedit Connections ... end edit connections</td></tr><tr><td>解释</td><td>默认情况下，disInterface 支持单个输入/输出（重放文件、播放文件或网络地址）。连接块中的连接信息允许多种输出类型。可用的子命令包括 record、playback、broadcast、multicast、unicast、port、send_port 和 receive_port。使用 connections ... end Connections 时，所有先前的 DIS 输出命令将被新用户输入替换。使用 edit Connections ... end edit connections 时，现有的 DIS 输出命令将被保留。注意：端口命令应紧跟在连接块内的 broadcast、multicast 或 unicast 命令之后。示例# 设置多个网络连接# 所有先前的连接命令将被丢弃！connectionsunicast_192.168.1.1port_9392unicast_192.168.1.2port_9393broadcast_192.168.255.255port_5828end Connections...# 添加新的重放文件输出，保留现有输出。edit Connectionsrecord_my_replay.repend_edit(connections</td></tr><tr><td>命令</td><td>record &lt;filename&gt;</td></tr><tr><td>解释</td><td>将仿真记录到指定文件。注意：当在连接块之外使用时，record、playback、broadcast、multicast 和 unicast 命令是互斥的。仅使用最后一次出现的命令。注意：要在文件名中插入运行编号，请使用“%d”。示例file replay_%d.rep</td></tr><tr><td>命令</td><td>Playback &lt;filename&gt;</td></tr><tr><td>解释</td><td>将指定文件中的实体状态数据读取并注入仿真中。仅使用实体状态数据-所有其他PDU(Protocol Data Unit)都将被忽略。entity_type命令用于定义DIS实体类型到WSF平台的映射,就像在标准DIS仿真中一样。如果定义了记录文件,实体状态PDU也会被写入记录文件中。所有平台的子系统在被添加到仿真之前都会被移除,移动器将被替换为使用实体状态的特殊移动器。签名数据将从entity_type映射定义的平台类型中获取。此功能的一个优势是它可以在构造性仿真(例如,非实时仿真)中使用。注意:实体的DIS“site”将被更改以消除与其他输入流的潜在冲突。注意:当在连接块之外使用时,record、playback、broadcast、multicast和unicast命令是互斥的。仅使用最后一次出现的命令。</td></tr><tr><td>命令</td><td>broadcast&lt;broadcast-IP-address&gt;</td></tr><tr><td>解释</td><td>在指定的广播网络上参与DIS演习。例如,如果您的以太网端口地址是192.168.1.14并且网络掩码设置为255.255.0.0,命令将是broadcast192.168.255.255。注意:必须同时指定port命令。注意:当在连接块之外使用时,record、playback、broadcast、multicast和unicast命令是互斥的。仅使用最后一次出现的命令。</td></tr><tr><td>命令</td><td>multicast&lt;multicast-IP-address&gt;&lt;interface-address&gt;</td></tr><tr><td>解释</td><td>在指定的多播网络上参与DIS演习。必须同时指定port命令。&lt;multicast-IP-address&gt;:范围在224.0.0.0到239.255.255之间的地址。&lt;interface-address&gt;:所需接口的机器IP地址。IP可以缩写。例如,multicast 225.1.2.3192.168。注意:当在连接块之外使用时,record、playback、broadcast、multicast和unicast命令是互斥的。仅使用最后一次出现的命令。</td></tr><tr><td>命令</td><td>unicast&lt;unicast-address&gt;</td></tr><tr><td>解释</td><td>与单个端点通信DIS流量。unicast-address可以是IP地址或主机名。必须同时指定port命令。注意:当在连接块之外使用时,record、playback、broadcast、multicast和unicast命令是互斥的。仅使用最后一次出现的命令。</td></tr><tr><td>命令</td><td>port&lt;IP-port-number&gt;</td></tr><tr><td>解释</td><td>指定广播、多播和单播模式的端口号。</td></tr><tr><td>命令</td><td>send_port&lt;IP-port-number&gt;receive_port&lt;IP-port-number&gt;</td></tr><tr><td>解释</td><td>指定广播、多播和单播模式的发送和接收端口号。send_port和receive_port必须一起指定,并作为port命令的替代。此命令主要用于单播模式。</td></tr><tr><td>命令</td><td>time_to_live&lt;ttl-value&gt;</td></tr><tr><td>解释</td><td>指定多播通信的“生存时间”值,范围为[0,255]。随着TTL字段值的增加,路由器将扩大它们在多播包中的转发跳数。为了提供有意义的范围控制,多播路由器根据TTL字段强制执行以下“阈值”:“0”限制传出数据包到同一主机“1”限制传出数据包到同一子网“32”限制传出数据包到同一站点“64”限制传出数据包到同一地区“128”限制传出数据包到同一大陆“255”无限制默认值由操作系统设置,通常设置为较低值。每跳一次,TTL值减1,以防止无限制的在网络中传输,造成拥塞。</td></tr></table>

这些输入块允许向其他仿真参与者输出筛选后的连接。

<table><tr><td>命令</td><td>filtered_connection...end_Filtered_connection</td></tr><tr><td>解释</td><td>每个 filtered_connection 块中的连接信息允许将 DIS PDU 的子集输出到指定设备。如果尚不存在设备（输出类型、地址、端口），则会将其附加到连接列表中（如在edit(connections 中）。可用的子命令包括 record、broadcast、multicast、unicast、port 和 allow。唯一的子命令 allow 提供了一种方法，指定哪些类型的 DIS PDU 将被允许输出到给定设备。使用 filtered_connection...end filtrated_connection 时，将保留现有的 DIS 输出连接。如果之前定义了相同的连接，则它将被覆盖为筛选连接，并应用筛选器。如果之前未定义此类连接，则会创建并添加连接，并应用筛选器。注意：端口命令应紧跟在连接块内的 broadcast、multicast 或 unicast 命令之后。示例# 设置多个输出筛选网络连接# 发送到 192.168.10.46:3225，仅包括蓝方实体状态 PDU 和被蓝方跟踪的红方实体状态 PDU</td></tr><tr><td></td><td>filtered_connectionunicast 192.168.10.46port 3225allow force blue allallow force red tracked blueend filtrated_connection</td></tr><tr><td></td><td># 广播到 130.38.255.255:3227，仅包括类型为 BLUE_AIRLINER 的实体状态 PDU。# 同时发送类型为 DRONE 的实体状态 PDU，蓝方跟踪的实体</td></tr><tr><td></td><td>filtered_connectionbroadcast 130.38.255.255port 3227allow entity_type BLUE_AIRLINER allallow entity_type DRONE tracked blueend filtrated_connection</td></tr><tr><td>命令</td><td>allow entity_type [all / tracked &lt;by force&gt;]</td></tr><tr><td>解释</td><td>指定允许从筛选连接输出的 WSF 实体类型。</td></tr><tr><td>命令</td><td>allow force [all / tracked &lt;by force&gt;]</td></tr><tr><td>解释</td><td>指定强制允许从筛选连接输出的 WSF 实体类型。</td></tr></table>

仿真控制命令  

<table><tr><td>命令</td><td>protocol_version &lt;protocol-version-id&gt;</td></tr><tr><td>解释</td><td>指定 DIS 协议版本，范围为 [0, 6]。
默认值：5</td></tr><tr><td>命令</td><td>exercise &lt;dis-exercise-id&gt;</td></tr><tr><td>解释</td><td>指定 DIS 演习 ID，范围为 [1, 255]。
默认值：1</td></tr><tr><td>命令</td><td>site &lt;dis-site-id&gt;</td></tr><tr><td>解释</td><td>指定 DIS 站点 ID，范围为 [1, 65534]。
默认值：1</td></tr><tr><td>命令</td><td>application &lt;dis-application-id&gt;</td></tr><tr><td>解释</td><td>指定 DIS 应用 ID，范围为 [1, 65534]。</td></tr><tr><td></td><td>默认值:1</td></tr><tr><td>命令</td><td>join exerciseno join exercise</td></tr><tr><td>解释</td><td>指定应用程序是否应作为 DIS 非实时缩放和步进仿真的参与者加入演习(由exercise 命令指定)。默认值: no join exercise</td></tr><tr><td>命令</td><td>autostart</td></tr><tr><td>解释</td><td>不等待 Start/Resume PDU 来启动仿真。默认值: no_autostart</td></tr><tr><td>命令</td><td>no_autostart</td></tr><tr><td>解释</td><td>等待 Start/Resume PDU 来启动仿真。这是默认设置。</td></tr><tr><td>命令</td><td>deferred_connection_time &lt;time-value&gt;</td></tr><tr><td>解释</td><td>应用程序将在指定的仿真时间到达之前推迟加入演习。在此之前,它将尽可能快地运行,并且不会向 DIS 演习发送或接收数据。当达到所需时间时,应用程序将连接到网络或开始写入重放文件。仿真时钟将按照 autostart 或 no_autostart 命令的定义运行。此命令的最小有效时间值为一秒。</td></tr><tr><td>命令</td><td>absolute_timestamp</td></tr><tr><td>解释</td><td>指定由此应用程序生成的 PDU 使用绝对时间戳。默认值:使用相对时间戳。</td></tr><tr><td>命令</td><td>ignore_pdu_time</td></tr><tr><td>解释</td><td>忽略 PDU 中的时间,使用当前的仿真时间。</td></tr><tr><td>命令</td><td>use_pdu_time</td></tr><tr><td>解释</td><td>使用 PDU 中的时间作为有效事件时间。不建议在大型仿真中使用此命令。默认值: ignore_pdu_time</td></tr><tr><td>命令</td><td>mover_update_timer &lt;time-value&gt;</td></tr><tr><td>解释</td><td>如果大于0,接口将生成事件以在指定间隔强制平台更新其位置。这对于由于对象之间缺乏交互而位置更新可能不频繁的事件驱动仿真非常有用。注意:时间步进仿真(例如,使用 WsFrameStepSimulation 和 -rt 标志的仿真)应将此值设置为0,以防止额外的更新,因为此类仿真已经以高频率导致移动器更新。默认值:1.0秒</td></tr><tr><td>命令</td><td>heartbeat_timer &lt;time-value&gt;</td></tr><tr><td>解释</td><td>指定 DIS 心跳计时器。对于内部控制的实体,这定义了传输实体状态 PDU 之间可以经过的最大时间。如果需要,仿真将强制发送实体状态 PDU。要显著减少大型仿真的重放文件大小,请将 heartbeat_timer 设置为20或更大。默认值:5.0秒</td></tr><tr><td>命令</td><td>heartbeat-multiplier &lt;real-value&gt;</td></tr><tr><td>解释</td><td>指定 DIS 心跳乘数。对于外部控制的实体,heartbeat_timer 值; heartbeat-multiplier定义了在接收实体状态 PDU 之前可以经过的最大时间,然后实体被声明为“非活动”并从仿真中移除。默认值:2.4</td></tr><tr><td>命令</td><td>initial_distribution_interval &lt;time-value&gt;</td></tr><tr><td>解释</td><td>在参与分布式演习(使用广播或多播)时,接口将分散初始状态数据的传输,以避免网络过载。此命令提供了一种机制来显式指定初始分布间隔。默认值:heartbeat_timer 的值</td></tr><tr><td>命令</td><td>entity_position_threshold &lt;length-value&gt;</td></tr><tr><td>解释</td><td>指定 DIS 实体位置阈值。默认值:1.0米</td></tr><tr><td>命令</td><td>entity_ORIENTATION_threshold &lt;angle-value&gt;</td></tr><tr><td>解释</td><td>指定 DIS 实体方向阈值。默认值:3.0度</td></tr><tr><td>命令</td><td>maximum_beam_entries &lt;positive-integer&gt;</td></tr><tr><td>解释</td><td>指定将在电磁发射 PDU 的“系统”部分中传输的最大波束条目数。默认值:无限制(最多可以存储的最大数量,不超过包含 DIS “系统”的大小限制)。</td></tr><tr><td>命令</td><td>maximum_track_jam_entries &lt;positive-integer&gt;</td></tr><tr><td>解释</td><td>指定在电磁发射 PDU 的“波束”部分中传输的最大跟踪干扰条目数,然后将选择高密</td></tr><tr><td></td><td>度跟踪干扰模式。默认值:无限制(最多可以存储的最大数量,不超过包含DIS“系统”的大小限制)。注意:IEEE DIS标准规定了10的限制。如果希望符合标准,则必须指定值为10的命令。</td></tr><tr><td>命令</td><td>sensor_update_interval&lt;time-value&gt;</td></tr><tr><td>解释</td><td>用于强制电磁发射PDU以大约指定的更新间隔发送,除了标准规则之外。这主要用于强制PDU更频繁地发送,并在DIS波束记录中更新“波束扫描同步”。这允许接收器更准确地了解扫描传感器在其扫描模式中的位置。如果指定的值为0秒,则不会发送额外的更新。默认值:0秒(不发送额外的周期性更新)</td></tr></table>

# 映射关系命令

<table><tr><td>命令</td><td>force &lt;side&gt; &lt;dis-force-id&gt;</td></tr><tr><td>解释</td><td>指定与WSF平台方对应的DIS力量标识符。此命令应为场景中存在的每一方指定。如果没有提供任何force命令,则将定义以下默认值:force blue 1forcedred 2force green 3注意:如果存在任何force命令,则不会使用上述默认值。</td></tr><tr><td>命令</td><td>entity_type &lt;platform_type&gt; &lt;dis-entity-type&gt;</td></tr><tr><td>解释</td><td>指定在为具有指定WSF平台类型的平台或弹药发送PDU时使用的DIS实体类型。此命令应为场景中存在的每个WSF平台类型指定。如果平台的类型没有对应的DIS实体类型,则将使用0:0:0:0:0:0。为了正确地与其他网络仿真接收到的DIS实体进行交互,必须创建一个具有定义签名的对应简单平台类型。示例entity_type JUMBO_JET 1:2:225:1:5:5:0entity_type REGIONAL_JET 1:2:225:1:9:10:0</td></tr><tr><td>命令</td><td>unknownplatform_type &lt;platform-type&gt;</td></tr><tr><td>解释</td><td>指定外部实体的WSF平台类型,如果不存在适用的entity_type条目。</td></tr><tr><td>命令</td><td>entity_appearance...end-entity_appearance</td></tr><tr><td>解释</td><td>指定与指定签名状态关联的DIS实体外观类型和状态或ID。要标识外观映射:entity_appearancename &lt;platform-name&gt; [afterburner | configuration] &lt;appearance-state&gt;&lt;signature-type&gt;&lt;signature-state&gt;Type &lt;platform-type&gt; [afterburner | configuration]&lt;signature-type&gt;&lt;signature-state 名 name &lt;platform-name&gt; articulation &lt;parameter-type&gt;&lt;variable-name&gt;&lt;script-name&gt;Type &lt;platform-type&gt; articulation &lt;parameter-type&gt;&lt;script-name&gt; end-entity_appearance&lt;platform-name&gt;:平台名称的字符串输入。&lt;platform-type&gt;:平台类型的字符串输入。&lt;appearance-state&gt;:afterburner:整数值[0,1],其中0表示“关闭”,1表示“打开”。configuration:范围为[0,15]的整数值。&lt;signature-type&gt;:状态有效的签名类型。有效值为[acoustic,contrast,infrared,optical,radar,rcs]。&lt;signature-state&gt;:签名文件中输入的签名状态名称的字符串。&lt;parameter-type&gt;:在Enumerations文档ISO-REF-010-2006的第4.7.3节中定义的关节部件参数类型的编号。&lt;variable-name&gt;:平台上的脚本变量名称。&lt;script-name&gt;:平台上的脚本名称。</td></tr></table>