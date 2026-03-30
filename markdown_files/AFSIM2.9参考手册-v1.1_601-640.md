```txt
// SixDOF Subobjects   
subobject ... end_subobject   
// SixDOF Sequencers   
sequencer ... end_sequencer   
remove_sequencer ...   
// Parent-Relative Positioning and Separation   
parent.rel_x ...   
parent.rel_y ...   
parent.rel_z ...   
parent.rel_yaw ...   
parent.rel_pitch ...   
parent reli_roll ...   
separation_vx ...   
separation_vy ...   
separation_vz ...   
separation_omega_x ...   
separation_omega_y ...   
separation_omega_z ...   
// Size Factor Parameters   
size_factor_radius ...   
size_factor_min ...   
size_factor_max ...   
size_factor_volume_rate_m3_per_sec ...   
size_factor_area_rate_m2_per(sec ...   
size_factor_radius_rate_m_per(sec ...   
// Special Properties   
use_spherical-earth ...   
use_rotating-earth ...   
ignore_jettisoned Objects ...   
fixed_object ...   
// Object Creation Support   
nominal_max_mach ...   
nominal_max_alpha ...   
nominal_min_alpha ...   
nominal_max_beta ...   
end_point_massvehicle_type 
```

Point Mass Vehicle Type 是 WSF_POINT_MASS_SIX_DOF_MOVER 的一个关键组件。它定义了各种组件的特性（如质量属性、空气动力学、推进系统等），这些特性决定了WSF_POINT_MASS_SIX_DOF_MOVER 的性能。必须在 WSF_POINT_MASS_SIX_DOF_MOVER中引用之前定义一个 point_mass_vehicle_type。一个 point_mass_vehicle_type 可以从另一个 point_mass_vehicle_type 或 BASE_TYPE（PM6 对象类型的基类）派生。

# 定义 Point Mass Vehicle Type

```txt
point_massvehicle_type <type_name> <derived_from_object_name> end_point_mass_vehic1e_type 
```

在 point_mass_vehicle_type 块 中 定 义 point_mass_vehicle_type 。 每 个point_mass_vehicle_type 定义了一种飞行器类型，从简单的手动发射无人机到复杂的航天器。一个 point_mass_vehicle_type 可以包括质量属性、主要空气动力学、推进系统组件（包括发动机和燃料系统）、子对象（如武器、油箱等）、序列器（可以基于“事件”产生“动作”）、控制提供者（包括手动飞行员、合成飞行员、自动驾驶仪和制导系统）、飞行控制系统（决定如何路由/混合控制输入以移动控制面）、次级空气动力学（包括控制面空气动力学）、尺寸因子参数（允许对象的尺寸变化，如降落伞或气球）、相对定位（定义子对象相对于其父对象的定位方式）、分离效应（在子对象从其父对象抛弃时赋予其一个 delta-V 或角速度）以及其他特殊属性。

# 相关概念

PointMass Model: 在动力学中，点质量模型是一种简化的模型，通常用于描述物体的运动而不考虑其旋转惯性属性。它仅考虑物体的质量和位置，而忽略其形状和旋转特性。

应用场景: 点质量模型常用于飞行器的轨迹规划和动力学模拟中，因为它能够简化计算并专注于关键的运动学和动力学特性。

# 质量属性定义 Mass Properties

<table><tr><td>命令</td><td>mass</td></tr><tr><td>解释</td><td>物体的（空载）质量，不包括燃料。</td></tr><tr><td colspan="2">以下数据对于点质量飞行器未使用，但仍可以输入和存储：</td></tr><tr><td>命令</td><td>moment_of_inertia_ixx</td></tr><tr><td>解释</td><td>物体绕x轴的（空载）惯性矩，不包括燃料。</td></tr><tr><td>命令</td><td>moment_of_inertia_iyy</td></tr><tr><td>解释</td><td>物体绕y轴的（空载）惯性矩，不包括燃料。</td></tr><tr><td>命令</td><td>moment_of_inertia_izz</td></tr><tr><td>解释</td><td>物体绕z轴的（空载）惯性矩，不包括燃料。</td></tr><tr><td>命令</td><td>center_of_mass_x</td></tr><tr><td>解释</td><td>相对于参考点的物体x方向上的空载质心。</td></tr><tr><td>命令</td><td>center_of_mass_y</td></tr><tr><td>解释</td><td>相对于参考点的物体y方向上的空载质心。</td></tr><tr><td>命令</td><td>center_of_mass_z</td></tr><tr><td>解释</td><td>相对于参考点的物体z方向上的空载质心。</td></tr></table>

相关概念

惯性矩（MomentofInertia）: 惯性矩是一个物理属性，结合了质量和粒子围绕旋转轴的分布。它是物体对旋转运动变化的抵抗测量，与质量在线性运动中的作用相同。

质量（Mass）: 质量决定了物体在施加力时的加速度。质量越大，物体的惯性越大，越不容易加速。

这些属性在模拟和分析飞行器的动力学行为时非常重要，尽管对于点质量模型，惯性矩和质心位置可能不直接影响计算，但它们仍然可以用于更复杂的模型或分析中。

# SixDOF 积分器 SixDOF Integrator

在六自由度（Six Degrees of Freedom, SixDOF）模拟中，积分器用于计算物体在三维空间中的运动，包括平移和旋转。设置积分器类型是 SixDOF 对象正常运行的关键步骤。如果指定的积分器不存在，将会抛出异常，因为 SixDOF 对象无法在没有积分器的情况下工作。

积分器的选择

integrator<string>: 通过指定名称来设置对象的积分器类型。如果没有指定积分器，系统将使用默认积分器。

积分器的重要性

积分器在 SixDOF 模拟中至关重要，因为它们负责解决物体的运动方程，确保模拟的准确性和稳定性。SixDOF 模型通常用于航空航天、机器人和虚拟现实等领域，以模拟物体在空间中的复杂运动。

# 燃料传输 Fuel Transfers

燃料传输的组成

fuel_transfer <string>: 每个燃料传输都有一个名称，使用 fuel_transfer 后的第一个参数指定。  
source_tank <string>: 源油箱，通过其字符串名称定义。  
target_tank <string>: 目标油箱，通过其字符串名称定义。

运行时行为

在运行时，源油箱会尝试将燃料传输到目标油箱。传输过程受限于两个油箱的传输速率。这种机制允许在模拟中动态管理燃料的分配和使用，特别是在复杂的航天器或飞行器系统中。

应用场景

燃料传输系统在航空航天和汽车工业中非常重要。例如，在飞机中，燃料传输系统可以帮助平衡燃料负载，以减少滚转力矩，并在需要时将燃料从一个油箱转移到另一个油箱，以优化飞行性能和安全性。在复杂的航天器中，燃料传输系统可以确保推进剂在不同的推进系

统之间有效分配，以支持长时间的任务执行。

# 燃料系统修改 Fuel System Modification

在 AFSIM 中，燃料系统可以通过以下命令进行修改，通常是对从父对象继承的燃料系统进行调整：

remove_fuel_tank<string>: 移除指定名称的燃料箱。如果没有找到具有该名称的油箱，则该命令将被忽略。  
modify_fuel_quantity … end_modify_fuel_quantity: 修改指定燃料箱中的燃料数量。

```html
modify_fuelquantity<string> fuelquantity <mass-value> end_modify_fuelquantity 
```

fuel_quantity<mass-value>: 指定燃料箱中的燃料质量。如果没有找到具有该名称的油箱，则该命令将被忽略。

# 应用场景

这些命令允许用户灵活地管理和调整模拟中的燃料系统。例如，在模拟复杂的航天器或飞行器时，可能需要根据任务需求调整燃料分配，或者在设计阶段测试不同的燃料配置。通过移除不必要的油箱或调整燃料量，用户可以优化模拟的性能和准确性。这对于需要精确燃料管理的任务（如长时间飞行或复杂的轨道机动）尤为重要。

# 父对象相对定位与分离 Parent-Relative Positioning and Separation

在 AFSIM 中，可以通过以下命令指定子对象相对于父对象的定位方式，以及其在分离时的扰动。

# 相对定位

这些命令用于定义子对象在被父对象捕获时的相对位置和姿态：

parent_rel_x <length-value>: 指定子对象参考点相对于父对象参考点的 x 位置，使用父对象的机体坐标系。默认值： 0.0  
parent_rel_y <length-value>: 指定子对象参考点相对于父对象参考点的 y 位置。默认值：0.0  
parent_rel_z <length-value>: 指定子对象参考点相对于父对象参考点的 z 位置。默认值：0.0  
parent_rel_yaw <angle-value>: 指定子对象相对于父对象机体坐标系的偏航角。默认值：0.0  
parent_rel_pitch <angle-value>: 指定子对象相对于父对象机体坐标系的俯仰角。  
parent_rel_roll <angle-value>: 指定子对象相对于父对象机体坐标系的滚转角。默认值：0.0

# 分离扰动

这些命令用于定义子对象从父对象分离时的速度和角速度分量：

separation_vx <length-value>: 指定子对象分离时赋予的 $\pmb { \times }$ 方向速度分量（在父对象坐标系中）。默认值： 0.0  
separation_vy <length-value>: 指定子对象分离时赋予的 y 方向速度分量。默认值： 0.0  
separation_vz <length-value>: 指定子对象分离时赋予的 z 方向速度分量。默认值： 0.0  
separation_omega_x <length-value>: 指定子对象分离时赋予的绕 x 轴的角速度分量（在子对象坐标系中）。默认值： 0.0  
separation_omega_y <length-value>: 指定子对象分离时赋予的绕 y 轴的角速度分量。默认值： 0.0  
separation_omega_z <length-value>: 指定子对象分离时赋予的绕 z 轴的角速度分量。默认值： 0.0

# 应用场景

这些设置对于模拟多级火箭、航天器释放卫星或其他复杂的航天器分离过程非常重要。通过精确控制子对象的相对位置和分离扰动，用户可以更好地模拟分离后的动态行为，以满足特定的任务需求。

# 尺寸因子参数 Size Factor Parameters

尺寸因子参数用于调整对象的大小，这在需要改变大小的物体（如降落伞或气球）中非常有用，因为它们的大小部分决定了其空气动力学阻力。尺寸因子支持基于半径、面积或体积的变化率。当通过序列器动作（action_enable_size_factor）启用时，尺寸因子将根据选择的变化率类型进行“增长”或“缩小”，直到达到最小或最大尺寸因子限制。

# 参数说明

size_factor_radius <length-value>: 这是对象的“参考”半径，即对象的起始半径。此半径也用于计算参考面积和参考体积。默认值： 1.0 米  
size_factor_min <real-value>: 这是参考半径允许达到的最小因子（乘数）。默认值： 1.0  
size_factor_max <real-value>: 这是参考半径允许达到的最大因子（乘数）。默认值： 1.0  
size_factor_volume_rate_m3_per_sec <real-value>: 提供基于体积的变化率，以立方米每秒为单位。当使用体积模式时，不应使用面积和半径模式。默认值： 0.0  
size_factor_area_rate_m2_per_sec <real-value>: 提供基于面积的变化率，以平方米每秒为单位。当使用面积模式时，不应使用体积和半径模式。默认值： 0.0  
size_factor_radius_rate_m_per_sec <real-value>: 提供基于半径的变化率，以米每秒为单位。当使用半径模式时，不应使用体积和面积模式。默认值： 0.0

# 应用场景

这些参数在模拟中非常重要，尤其是在涉及空气动力学的场景中。例如，降落伞的大小直接影响其阻力和下降速度，通过调整尺寸因子，可以模拟不同大小的降落伞对飞行性能的

影响。此外，在气球膨胀或收缩的模拟中，尺寸因子也能提供精确的控制。

# 特殊属性 Special Properties

在 AFSIM中，特殊属性用于修改六自由度（SixDOF）对象的行为。这些属性可以帮助简化模型或提高模拟效率，具体如下：

use_spherical_earth <boolean-value>: 如果设置为 true，SixDOF 对象将使用球形地球模型，而不是 WGS84（扁球体）地球模型。这种简化在使用弹道导弹和航天发射器时非常有用，因为它消除了与扁球体地球相关的纬度问题。默认值： false  
use_rotating_earth <boolean-value>: 如果设置为 true，SixDOF 对象将使用旋转地球模型，而不是非旋转地球模型。默认值： false  
ignore_jettisoned_objects <boolean-value>: 如果设置为 true，任何从 SixDOF 对象抛弃的子对象将立即被移除，并且不会在 AFSIM 平台上存在。这通常用于加速运行时间，当不需要弹道导弹或航天发射器的废弃阶段时。默认值： false  
fixed_object <boolean-value>: 如果设置为 true，SixDOF 对象将不会执行运动学计算，而是保持静止。默认值： false

# 应用场景

这些特殊属性在模拟中提供了灵活性。例如，使用球形地球模型可以简化计算，特别是在不需要高精度地球模型的情况下，如某些弹道导弹轨迹模拟中。此外，忽略抛弃的子对象可以显著减少计算负担，提高模拟效率。固定对象属性则适用于需要保持对象静止的场景，如地面站或固定设备的模拟。

# 对象创建支持 Object Creation Support

在创建六自由度（SixDOF）模型时，可以使用以下命令来定义性能包络的限制。这些参数并不直接限制对象的性能，而是为计算性能和分析的函数提供提示。

# 参数说明

nominal_max_mach <real-value>: 定义对象预期的最大马赫数。这是一个提示值，用于帮助计算性能和分析。  
nominal_max_alpha <angle-value>: 定义对象预期的最大迎角（alpha）。这也是一个提示值，用于性能计算和分析。  
nominal_min_alpha <angle-value>: 定义对象预期的最小迎角（alpha）。同样是一个提示值。  
nominal_max_beta <angle-value>: 定义对象预期的最大侧滑角（beta）。这也是一个提示值，用于性能计算和分析。

# 应用场景

这些参数在设计和分析飞行器的飞行包络时非常有用。飞行包络通常包括速度、迎角和

侧滑角等参数的变化范围，这些参数帮助确定飞行器在不同飞行条件下的性能极限。例如，在设计阶段，工程师可以使用这些提示值来确保飞行器在预期的操作条件下能够安全运行，并在模拟中验证其性能。

通过合理设置这些参数，用户可以更好地理解和优化飞行器的性能，确保其在各种飞行条件下的安全性和效率。

# 3.6.3.1.3. 刚体载具类型 rigid_body_vehicle_type

rigid_body_vehicle_type F-86_Saber BASE_TYPE   
```txt
// Mass Properties  
mass ...  
moment_of_inertia_ixx ...  
moment_of_inertia_iyy ...  
moment_of_inertia_izz ...  
center_of_mass_x ...  
center_of_mass_y ...  
center_of_mass_z ...  
// SixDOF Mass Properties Data  
massProperties...end_mass_propertyies  
// SixDOF Aerodynamics Data  
aero_data...end_aero_data  
aero_component...end_aero_component  
// SixDOF Pilot Manager and Control Inputs  
pilotmanager...end_pilotmanager  
// SixDOF Flight Control System Definition  
flight Controls...end_aircraft_control  
// SixDOF Propulsion System Definition  
propulsion_data...end_propulsion_data  
// SixDOF Integrator  
integrator...  
// SixDOF Landing Gear  
landing_gear...end landing_gear  
// Fuel Transfers  
fuel_transfer...end_fuel_transfer  
remove_fuel_transfer...  
// Fuel System Modification 
```

```matlab
remove_fuel-tank...   
modify_fuelquantity...end_modify_fuelquantity 
```

```txt
// SixDOF Subobjects  
subobject ... end_subobject 
```

```txt
// SixDOF Sequencers  
sequencer ... end_sequence  
remove_sequence ... 
```

```txt
// Parent-Relative Positioning and Separation 
```

```txt
parent.rel_x ...  
parent.rel_y ...  
parent.rel_z ...  
parent.rel_yaw ...  
parent.rel_pitch ...  
parent.rel_roll ...  
separation_vx ...  
separation_vy ...  
separation_vz ...  
separation_omega_x ...  
separation_omega_y ...  
separation_omega_z ... 
```

```c
// Size Factor Parameters  
size_factor_radius ...  
size_factor_min ...  
size_factor_max ...  
size_factor_volume_rate_m3_per_sec ...  
size_factor_area_rate_m2_per(sec ...  
size_factor_radius_rate_m_per(sec ... 
```

```shell
// Special Properties  
use_spherical-earth ...  
use_rotating-earth ...  
ignore_jettisoned Objects ...  
fixed_object ... 
```

```txt
// Object Creation Support  
nominal_max_mach ...  
nominal_max_alpha ...  
nominal_min_alpha ...  
nominal_max_beta ... 
```

rigid_body_vehicle_type 是 AFSIM 中的一个关键组件，用于定义刚体六自由度运动器（WSF_RIGID_BODY_SIX_DOF_MOVER）的特性。它通过定义各种组件（如质量属性、空气动力学、推进等）的特性来决定刚体六自由度运动器的表现。在被引用到刚体六自由度运动器中之前，必须定义一个 rigid_body_vehicle_type。一个 rigid_body_vehicle_type 可以从另一个 rigid_body_vehicle_type 或 从 BASE_TYPE （ RB6 对 象 类 型 的 基 类 ） 派 生 。 一 个rigid_body_vehicle_type 的 定 义 是 在 一 个 rigid_body_vehicle_type 块 中 进 行 的 。 每 个rigid_body_vehicle_type 定义了一种类型的载具，从简单的手掷无人机到复杂的航天器不等。

# Mass Properties 质量属性

在 AFSIM 中，质量属性包括对象在空载（无燃料或有效载荷）时的质量和惯性矩。燃料和有效载荷对质量属性的额外贡献是单独考虑的。

# 参数和字段

mass <mass-value>：对象的空载质量，不包括燃料。  
moment_of_inertia_ixx <angular-inertia-value>：对象绕 $\pmb { \times }$ 轴的空载惯性矩，不包括燃料。  
moment_of_inertia_iyy <angular-inertia-value>：对象绕 y 轴的空载惯性矩，不包括燃料。  
moment_of_inertia_izz <angular-inertia-value>：对象绕 z 轴的空载惯性矩，不包括燃料。  
center_of_mass_x <length-value>：相对于参考点的空载质心在对象 $\pmb { \times }$ 方向上的位置。  
center_of_mass_y <length-value>：相对于参考点的空载质心在对象 y 方向上的位置。  
center_of_mass_z <length-value>：相对于参考点的空载质心在对象 z 方向上的位置。

# 解释

惯性矩（MomentofInertia）是描述物体抵抗角加速度的量度，类似于质量在直线运动中抵抗加速度的作用。惯性矩取决于物体的质量分布和选择的旋转轴，惯性矩越大，需要的扭矩就越大。

质量（Mass）是物体的基本属性，决定了物体在施加力时的加速度。质量越大，物体的惯性越大，抵抗加速度的能力也越强。

这些参数帮助定义对象在模拟环境中的物理特性，确保在模拟中能够准确地表现其运动行为。希望这些信息对你的学习有所帮助！如果有其他问题，随时问我哦！

# SixDOF Integrator 六自由度积分器

在 AFSIM 中，integrator<string> 用于设置对象的积分器类型为指定的名称。如果没有与指定名称匹配的积分器存在，将抛出异常，因为六自由度对象无法在没有积分器的情况下运行。如果未指定积分器，对象将使用默认积分器。

# Fuel Transfers 燃料转移

通常，燃料转移是在 propulsion_data 块中定义的。然而，当存在外部油箱（作为子对

象）时，燃料转移可以在 rigid_body_vehicle_type 块中定义，但仍然在推进系统块之外。

```txt
fuel_transfer <string> source-tank <string> target-tank <string> end_fuel_transfer 
```

每个燃料转移都有一个名称，使用 fuel_transfer 后的第一个参数。

source_tank <string>：定义源油箱的名称。  
target_tank <string>：定义目标油箱的名称。

在运行时，源油箱将尝试向目标油箱转移燃料，受限于两个油箱的转移速率。

remove_fuel_transfer <string>：移除具有指定名称的燃料转移。如果不存在具有该名称的转移，则忽略该命令。

# Fuel System Modification 燃料系统修改

燃料系统可以通过以下命令进行修改（通常是修改从父对象继承的燃料系统）：

remove_fuel_tank<string>：移除具有指定名称的燃料箱。如果不存在具有该名称的油箱，则忽略该命令。

```html
modify_fuelquantity<string> fuelquantity <mass-value> end_modify_fuelquantity 
```

modify_fuel_quantity <string>：修改指定名称的燃料箱中的燃料数量。如果不存在具有该名称的油箱，则忽略该命令。

这些功能允许用户在模拟中灵活地管理和调整燃料系统，以适应不同的模拟需求和场景。

# Parent-Relative Positioning and Separation 父相对定位与分离

在 AFSIM 中，以下命令用于指定子对象在被俘获时相对于其父对象的位置：

父相对定位

parent_rel_x <length-value>：指定对象参考点相对于父对象参考点在父对象坐标系中的x 位置。默认值为 0.0。  
parent_rel_y <length-value>：指定对象参考点相对于父对象参考点在父对象坐标系中的y 位置。默认值为 0.0。  
parent_rel_z <length-value>：指定对象参考点相对于父对象参考点在父对象坐标系中的z 位置。默认值为 0.0。  
parent_rel_yaw <angle-value>：指定对象相对于父对象坐标系的偏航角。默认值为 0.0。  
parent_rel_pitch <angle-value>：指定对象相对于父对象坐标系的俯仰角。  
parent_rel_roll <angle-value>：指定对象相对于父对象坐标系的滚转角。默认值为 0.0。

# 分离效应

以下命令用于指定子对象从父对象分离时施加的扰动：

separation_vx <length-value>：指定分离时施加给子对象的 x 方向速度分量（在父对象坐标系中）。默认值为 0.0。  
separation_vy <length-value>：指定分离时施加给子对象的 y 方向速度分量（在父对象

坐标系中）。默认值为 0.0。

separation_vz <length-value>：指定分离时施加给子对象的 z 方向速度分量（在父对象坐标系中）。默认值为 0.0。  
separation_omega_x <length-value>：指定分离时施加给子对象的 x 方向角速度分量（在子对象坐标系中）。默认值为 0.0。  
separation_omega_y <length-value>：指定分离时施加给子对象的 y 方向角速度分量（在子对象坐标系中）。默认值为 0.0。  
separation_omega_z <length-value>：指定分离时施加给子对象的 z 方向角速度分量（在子对象坐标系中）。默认值为 0.0。

# Size Factor Parameters 尺寸因子参数

尺寸因子参数提供了一种调整对象尺寸的方法。这对于降落伞或气球等可以改变尺寸的物体非常有用，因为它们的尺寸部分决定了它们的空气阻力。尺寸因子支持基于半径、面积或体积的变化率。当启用时（使用 action_enable_size_factor 序列器动作），尺寸因子将根据选择的变化率类型进行变化，直到达到最小或最大尺寸因子限制。

size_factor_radius <length-value>：这是对象的“参考”半径，即起始半径。此半径也用于计算参考面积和参考体积。默认值为 1.0 米。  
size_factor_min <real-value>：参考半径允许达到的最小因子（乘数）。默认值为 1.0。  
size_factor_max <real-value>：参考半径允许达到的最大因子（乘数）。默认值为 1.0。  
size_factor_volume_rate_m3_per_sec <real-value>：提供基于体积的变化率（立方米每秒）。使用体积模式时，不应使用面积和半径模式。默认值为 0.0。  
size_factor_area_rate_m2_per_sec <real-value>：提供基于面积的变化率（平方米每秒）。使用面积模式时，不应使用体积和半径模式。默认值为 0.0。  
size_factor_radius_rate_m_per_sec <real-value>：提供基于半径的变化率（米每秒）。使用半径模式时，不应使用体积和面积模式。默认值为 0.0。

# Special Properties 特殊属性

一些“特殊属性”可用于修改六自由度对象的行为：

use_spherical_earth <boolean-value>：如果为 true，六自由度对象将使用球形地球模型而不是 WGS84（扁球）地球模型。这在使用弹道导弹和航天发射器时通常是一个有用的简化，因为它消除了与扁球地球相关的导航纬度问题。默认值为 false。  
use_rotating_earth <boolean-value>：如果为 true，六自由度对象将使用旋转地球模型而不是非旋转地球模型。默认值为 false。  
ignore_jettisoned_objects <boolean-value>：如果为 true，从六自由度对象弹出的任何子对象将立即被移除，并且不会有 AFSIM 平台。这通常用于加快运行时间，当不需要弹道导弹或航天发射器的废弃阶段时。默认值为 false。  
fixed_object <boolean-value>：如果为 true，六自由度对象将不执行运动学计算作为其“更新”的一部分，而是保持静止。默认值为 false。  
Object Creation Support 对象创建支持  
这些命令用于帮助创建六自由度模型的函数。它们用于定义性能包络的限制。  
nominal_max_mach <real-value>：定义对象预期的最大马赫数。这并不限制性能，而是

为计算性能和/或分析的函数提供提示。

nominal_max_alpha <angle-value>：定义对象预期的最大迎角。这并不限制性能，而是为计算性能和/或分析的函数提供提示。  
nominal_min_alpha <angle-value>：定义对象预期的最小迎角。这并不限制性能，而是为计算性能和/或分析的函数提供提示。  
nominal_max_beta <angle-value>：定义对象预期的最大侧滑角。这并不限制性能，而是为计算性能和/或分析的函数提供提示。

# 3.6.3.2. 六自由度推力类型 SixDOF Thrust Producer Types

在 AFSIM 中，推力产生器类型的定义（包括涡轮驱动的喷气发动机如涡轮喷气和涡轮风扇发动机、冲压/超音速冲压发动机、液体推进剂火箭发动机和固体推进剂火箭发动机）是在 six_dof_object_types 块中进行的。这些定义了可以在 rigid_body_vehicle_type 或point_mass_vehicle_type 块内的 propulsion_data 块中引用的发动机“类型”。

由于 RB6 和 PM6 在飞行控制管理上的差异，推力产生器在用于 RB6 或 PM6 载具时也有略微不同的输入。RB6 推力产生器必须在 rigid_body_engine_type 块中定义，而 PM6推力产生器必须在 point_mass_engine_type 块中定义。

# 3.6.3.2.1. 刚体发动机类型 rigid_body_engine_type

```txt
rigid_body.engine_type J79-GE-7 BASE_TYPE ... Jet- or rocket-specific commands ... //Thrust Offset Location thrust_offset ... //Reference Area When Inoperative inop_ref_area ... //Fuel Source for Engine fuel_feed ... //Thrust producer control handles throttle_settings_mil THROTTLE_MIL throttleSetting_ab THROTTLE_AB throttleSetting_reverser THRUST_REVERSER throttleSetting_yaw THRUST_VECTORING_YAW throttleSetting_pitch THRUST_VECTORING_PITCH end_rigid_body.engine_type 
```

每种类型的发动机定义在 rigid_body_engine_type 块中进行。由于定义的是发动机的“类型”而不是“实例”，因此不包括安装位置/姿态数据。通常，燃料供应是在实例级别而不是类型级别指定的。

thrust_offset：推力偏移位置，用于调整推力的施加点。

inop_ref_area：发动机不工作时的参考面积。  
fuel_feed：发动机的燃料来源。

推力控制手柄：

throttle_setting_mil：军用推力设置。  
throttle_setting_ab：加力推力设置。  
throttle_setting_reverser：反推力设置。  
throttle_setting_yaw：偏航推力矢量控制。  
throttle_setting_pitch：俯仰推力矢量控制。

这些定义允许在模拟中精确地控制和管理不同类型的推力产生器，以适应各种飞行器的需求和性能要求。

# 3.6.3.2.2. 点质量发动机类型 point_mass_engine_type

```txt
point_mass.engine_type J79-GE-7 BASE_TYPE ... Jet-or rocket-specific commands ... //Thrust Offset Location thrust_offset ... //Reference Area When Inoperative inop_ref_area ... //Fuel Source for Engine fuel_feed ...   
end_point_mass.engine_type 
```

在 AFSIM 中，point_mass_engine_type 用于定义发动机的类型，而不是发动机的实例，因此不包括安装位置或姿态数据。通常，燃料供应是在实例级别而不是类型级别指定的。

发动机类型包括：

Jet Engines (Turbojets and Turbofans)：喷气发动机（涡轮喷气和涡轮风扇）。  
Ramjet/Scramjet Engines：冲压/超音速冲压发动机。   
Liquid-Propellant Rocket Engines：液体推进剂火箭发动机。  
Solid-Propellant Rocket Motors：固体推进剂火箭发动机。

这些定义允许在模拟中精确地控制和管理不同类型的推力产生器，以适应各种飞行器的需求和性能要求。

下面将对这些发动机类型逐一介绍。

# 3.6.3.2.2.1. 喷气发动机（涡轮喷气和涡轮风扇）Jet Engines (Turbojets and Turbofans)

```txt
jet // Thrust Specific Fuel Consumption (TSFC) 
```

```txt
tsfc_idle_pph ... tsfc_mil_pph ... tsfc_ab_pph ... // Rated Thrust rated_thrust_idle ... rated_thrust_mil ... rated_thrust_ab ... // Idle Thrust Tables thrust_table_idle ... end_thrust_table_idle thrust_idle_mach_alt_table ... end_thrust_idle_mach_alt_table thrust_idle_alt_mach_table ... end_thrust_idle_alt_mach_table // Military (MIL) Thrust Tables thrust_table_mil ... end_thrust_table_mil thrust_mil_mach_alt_table ... end_thrust_mil_mach_alt_table thrust_mil_alt_mach_table ... end_thrust_mil_alt_mach_table // Afterburner (AB) Thrust Tables thrust_table_ab ... end_thrust_table_ab thrust_ab_mach_alt_table ... end_thrust_ab_mach_alt_table thrust_ab_alt_mach_table ... end_thrust_ab_alt_mach_table // Spin-Up Data spin_up_mil_per_sec ... spin_up_table_mil_per_sec ... endspin_up_table_mil_per_sec spin_up_ab_per_sec ... spin_up_table_ab_per_sec ... endSpin_up_table_ab_per_sec // Spin-Down Data spin_down_mil_per_sec ... spin_down_table_mil_per_sec ... endSpin_down_table_mil_per_sec spin_down_ab_per_sec ... spin_down_table_ab_per_sec ... endSpin_down_table_ab_per_sec // Flag for smoking engines engine_smokes_above_power-setting ...   
end Jet 
```

定义了喷气发动机的各种参数和推力表，重点关注不同功率设置和环境条件下的推力比燃油消耗（TSFC）和推力值。以下是关键组件的说明：

tsfc_idle_pph <real-value>: 该字段用于定义怠速状态下的推力比油耗，单位是磅推力/磅燃料/小时。推力比油耗（TSFC）是评价发动机燃油效率的重要指标，表示每单位推力所需的燃料消耗量。  
tsfc_mil_pph<real-value>: 该字段指定在军用功率下（即不使用加力燃烧器的全功率）的推力比油耗，同样以磅推力/磅燃料/小时为单位。军用功率是指发动机在不使用加力燃烧器时达到的最大功率状态。  
tsfc_ab_pph<real-value>: 这个字段描述了在使用全加力燃烧器时的推力比油耗，单位为磅推力/磅燃料/小时。使用加力燃烧器可以显著增加推力，但也会增加燃油消耗。  
rated_thrust_idle <force-value>: 这是怠速时的参考推力值，因为实际推力会因环境条件变化。怠速推力通常用于地面操作或低速飞行。  
rated_thrust_mil <force-value>: 这个字段提供了在军用功率下的参考推力值。军用功率指的是不使用加力燃烧器时发动机的最大推力。  
rated_thrust_ab <force-value>: 这是使用全加力燃烧器时的参考推力值。在这种情况下，发动机能够产生最高的推力。  
thrust_table_idle: 这是一个简单的怠速推力与高度的对照表，不考虑马赫效应。虽然thrust_idle_mach_alt_table 或 thrust_idle_alt_mach_table 更精确，但如果没有马赫数据，可以使用此表。

```txt
thrust_table_idle
# alt_ft thrust_lbs
0.0 10000.0
50000.0 2000.0
59000.0 100.0
60000.0 0.0
end_thrust_table_idle 
```

thrust_idle_mach_alt_table: 这个表格比 thrust_table_idle 更先进，因为它包括了马赫效应。然而，数据格式上大多数用户会偏好 thrust_idle_alt_mach_table。

```txt
thrust_idle_mach_alt_table  
irregular_table  
    independent_variable mach precision float  
    independent_variable alt units ft  
    dependent_variable precision float  
mach 0.0  
    alt 0.00 10000.0 30000.0 59000.0 60000.0  
    values 10000.0 8000.0 4000.0 100.0 0.0  
    ...  
mach 2.0  
    alt 0.00 10000.0 30000.0 59000.0 60000.0  
    values 10000.0 8000.0 4000.0 100.0 0.0  
mach 3.0  
    alt 0.00 10000.0 30000.0 59000.0 60000.0  
    values 0.0 0.0 0.0 0.0 0.0  
end_irregular_table 
```

```txt
end_thrust_idle_mach_alt_table 
```

thrust_idle_alt_mach_table: 这是最理想的推力表格格式，包含马赫效应并以用户偏好的方式组织数据，是 thrust_idle_mach_alt_table 的替代格式。

```txt
thrust_Idle_alt_mach_table  
irregular_table  
independent_variable alt units ft  
independent_variable mach precision float  
dependent_variable precision float  
alt 0.0  
mach 0.00 0.60 1.00 2.00 3.00  
values 10000.0 10000.0 10000.0 10000.0  
alt 59000.0  
mach 0.00 0.60 1.00 2.00 3.00  
values 10000.0 10000.0 10000.0 10000.0  
alt 60000.0  
mach 0.00 0.60 1.00 2.00 3.00  
values 10000.0 10000.0 10000.0 10000.0  
end_irregular_table  
end_thrust_Idle_alt_mach_table 
```

```txt
- thrust_table_mil 
```

这是一个简单的军事推力（MIL）与高度的对照表。需要注意的是，这个表没有考虑马赫数的影响。虽然 thrust_mil_mach_alt_table 或 thrust_mil_alt_mach_table 更为理想，但如果没有马赫数的数据，可以使用这个表。

```tcl
thrust_table_mil
# alt_ft thrust_lbs
0.0 10000.0
50000.0 2000.0
59000.0 100.0
60000.0 0.0
end_thrust_table_mil 
```

```sql
- thrust_mil_mach_alt_table 
```

这个表比 thrust_table_mil 更为先进，因为它包含了马赫数的影响。然而，大多数用户更喜欢 thrust_mil_alt_mach_table 的格式。

```txt
thrust_mil_mach_alt_table  
 irregular_table  
 independent_variable mach precision float  
 independent_variable alt units ft  
 dependent_variable precision float  
 mach 0.0 
```

```txt
alt 0.00 10000.0 30000.0 59000.0 60000.0  
values 10000.0 8000.0 4000.0 100.0 0.0  
...  
mach 2.0  
alt 0.00 10000.0 30000.0 59000.0 60000.0  
values 10000.0 8000.0 4000.0 100.0 0.0  
mach 3.0  
alt 0.00 10000.0 30000.0 59000.0 60000.0  
values 0.0 0.0 0.0 0.0 0.0  
endIrregular_table  
end_thrust_mil_mach_alt_table 
```

thrust_mil_alt_mach_table

这是通常最好的推力表格式——它包括了马赫数的影响，并以一种更为理想的方式组织数据。thrust_mil_mach_alt_table 是一种替代格式。

```txt
thrust_mil_alt_mach_table  
irregular_table  
independent_variable alt units ft  
independent_variable mach precision float  
dependent_variable precision float  
alt 0.0  
mach 0.00 0.60 1.00 2.00 3.00  
values 10000.0 10000.0 10000.0 10000.0 10000.0  
...  
alt 59000.0  
mach 0.00 0.60 1.00 2.00 3.00  
values 10000.0 10000.0 10000.0 10000.0 10000.0  
alt 60000.0  
mach 0.00 0.60 1.00 2.00 3.00  
values 10000.0 10000.0 10000.0 10000.0 10000.0  
end_irregular_table  
end_thrust_mil_alt_mach_table 
```

thrust_table_ab

这是一个简单的加力推力（AB）与高度的对照表。需要注意的是，这个表没有考虑马赫数的影响。thrust_ab_mach_alt_table 或 thrust_ab_alt_mach_table 更为理想，但如果没有马赫数的数据，可以使用这个表。

```python
thrust_table_ab alt_ft thrust_lbs 0.0 10000.0 
```

```txt
50000.0 2000.0  
59000.0 100.0  
60000.0 0.0  
end_thrust_table_ab 
```

thrust_ab_mach_alt_table

这个表比 thrust_table_ab 更为先进，因为它包含了马赫数的影响。然而，大多数用户更喜欢 thrust_ab_alt_mach_table 的格式。

```txt
thrust_ab_mach_alt_table  
irregular_table  
independent_variable mach precision float  
independent_variable alt units ft  
dependent_variable precision float  
mach 0.0  
alt 0.00 10000.0 30000.0 59000.0 60000.0  
values 10000.0 8000.0 4000.0 100.0 0.0  
...  
mach 2.0  
alt 0.00 10000.0 30000.0 59000.0 60000.0  
values 10000.0 8000.0 4000.0 100.0 0.0  
mach 3.0  
alt 0.00 10000.0 30000.0 59000.0 60000.0  
values 0.0 0.0 0.0 0.0 0.0  
end_irregular_table  
end_thrust_ab_mach_alt_table 
```

thrust_ab_alt_mach_table

这是通常最好的推力表格式——它包括了马赫数的影响，并以一种更为理想的方式组织数据。thrust_ab_mach_alt_table 是一种替代格式。

```txt
thrust_ab_alt_mach_table  
irregular_table  
independent_variable alt units ft  
independent_variable mach precision float  
dependent_variable precision float  
alt 0.0  
mach 0.00 0.60 1.00 2.00 3.00  
values 10000.0 10000.0 10000.0 10000.0  
...  
alt 59000.0  
mach 0.00 0.60 1.00 2.00 3.00 
```

```verilog
values 10000.0 10000.0 10000.0 10000.0 alt 60000.0 mach 0.00 0.60 1.00 2.00 3.00 values 10000.0 10000.0 10000.0 10000.0 end_irregular_table end_thrust_ab_alt_mach_table 
```

# 加速参数

spin_up_mil_per_sec <实数值>

这个参数定义了发动机从怠速加速到军事功率（MIL）的速度。值为 1.0 表示发动机将在 1 秒内从怠速加速到 MIL 功率，而值为 0.1 表示需要 10 秒。

spin_up_table_mil_per_sec

这个表格提供了一个基于油门水平（归一化）的加速速度表，使得加速过程更符合实际情况。值为 1.0 表示 1 秒内从怠速加速到 MIL 功率，而值为 0.1 表示需要 10 秒。

```txt
spin_up_table_mil_per_sec  
# throttle_level spin_up_per(sec  
0.0 0.05  
0.2 0.10  
0.4 0.20  
0.6 0.30  
0.8 0.40  
1.0 0.50  
endspin_up_table_mil_per(sec 
```

spin_up_ab_per_sec <实数值>

这个参数定义了发动机从 MIL 功率加速到全加力（FullAB）功率的速度。值为 1.0 表示1 秒内从 MIL 加速到全加力，而值为 0.1 表示需要 10 秒。

spin_up_table_ab_per_sec

这个表格提供了一个基于油门水平的加速速度表，使得加速过程更符合实际情况。

```txt
spin_up_table_ab_per_sec
# throttle_level spin_up_per(sec
0.0 0.05
0.2 0.10
0.4 0.20
0.6 0.30
0.8 0.40
1.0 0.50
endspin_up_table_ab_per(sec 
```

# 减速参数

spin_down_mil_per_sec <实数值>

这个参数定义了发动机从 MIL 功率减速到怠速的速度。值为 1.0 表示 1 秒内从 MIL 功率减速到怠速，而值为 0.1 表示需要 10 秒。

spin_down_table_mil_per_sec

这个表格提供了一个基于油门水平的减速速度表，使得减速过程更符合实际情况。

```txt
spin_down_table_mil_per_sec
# throttle_level spin_down_per(sec
0.0 0.05
0.2 0.10
0.4 0.20
0.6 0.30
0.8 0.40
1.0 0.50
endspin_down_table_mil_per(sec 
```

spin_down_ab_per_sec <实数值>

这个参数定义了发动机从全加力功率减速到 MIL 功率的速度。值为 1.0 表示 1 秒内从全加力减速到 MIL，而值为 0.1 表示需要 10 秒。

spin_down_table_ab_per_sec

这个表格提供了一个基于油门水平的减速速度表，使得减速过程更符合实际情况。

```txt
spin_down_table_ab_per_sec
# throttle_level spin_down_per_sec
0.0 0.05
0.2 0.10
0.4 0.20
0.6 0.30
0.8 0.40
1.0 0.50
endspin_down_table_ab_per_sec 
```

# 发动机烟雾参数

engine_smokes_above_power_setting <实数值>

这个参数指定了在何种油门水平（MIL 功率）以上发动机会产生烟雾。例如，值为 0.8表示当油门超过 $80 \%$ 功率时会产生烟雾。如果选择了加力，烟雾将停止。默认值为 1.0，不会产生烟雾。这对于模拟产生大量烟雾的发动机（如旧款 F-4Phantom和 MiG-29）非常有用。

# 3.6.3.2.2.2. 冲压/超音速冲压发动机 Ramjet/Scramjet Engines

```txt
ramjet   
//Thrust Specific Fuel Consumption (TSFC) tsfc_alt_mach_table ... end(tsfc_alt_mach_table   
//Thrust Table thrust_alt_mach_table ... end_thrust_alt_mach_table   
//Use afterburner appearance when operating afterburner Appearance_when-operating ..   
//Latch fuel injection control 
```

```txt
latch_fuel_injection ... // Use proportional throttle (rather than on/off throttle) use_proportional_throttle ... // Minimum thrust multiplier for proportional throttle minimum_proportional_thrust ...   
end_ramjet 
```

tsfc_alt_mach_table

这个表格定义了推力比燃料消耗（TSFC），以高度和马赫数为函数，单位为磅推力/磅燃料/小时。高度单位为英尺。

```txt
tsfc_alt_mach_table  
irregular_table  
independent_variable alt units ft  
independent_variable mach precision float  
dependent_variable precision float  
alt 0.0  
mach 1.90 2.00 2.50 2.6  
values 1.96 1.96 1.96 1.96  
...  
alt 90000.0  
mach 1.90 2.00 2.50 2.6  
values 1.96 1.96 1.96 1.96  
end_irregular_table  
end(tsfc_alt_mach_table 
```

thrust_alt_mach_table

这个表格定义了推力，以高度和马赫数为函数，单位为磅。由于表格在极值处会夹住而不是插值，因此确保极值数据为零非常重要，否则可能导致高马赫数下推力增加。

```txt
thrust_alt_mach_table_  
irregular_table  
independent_variable alt units ft  
independent_variable mach precision float  
dependent_variable precision float  
alt 0.0  
mach 1.90 2.00 2.50 2.6  
values 0.0 10000.0 12000.0 0.0 
```

```txt
alt 90000.0 mach 1.90 2.00 2.50 2.6 values 0.0 0.0 0.0 0.0 endIrregular_table end_thrust_alt_mach_table_ 
```

afterburner_appearance_when_operating <boolean-value>

这个参数指定当 ramjet 运行时是否使用加力燃烧器的外观。仅影响外观，没有物理或运动学效果。当为 true 时，ramjet 运行时将具有使用加力燃烧器的喷气发动机的外观。

latch_fuel_injection <boolean-value>

当为 true 时，燃料喷射将锁定在开启状态。这将保持发动机运行，只要有燃料可用，无论油门命令如何。当为 false 时，使用正常的油门控制。默认值为 false。

use_proportional_throttle <boolean-value>

当为 true 时，将使用比例油门控制。当为 false 时，使用正常的开/关油门控制。默认值为 false。

minimum_proportional_thrust <real-value>

这是比例油门控制可使用的最小推力水平。通常为 0.8，但必须始终大于零。默认值为0.0。

# 3.6.3.2.2.3. 液体推进剂发动机 Liquid-Propellant Rocket Engines

```txt
liquid_propellant_rocket   
//Max Thrust max_thrust_sealevel ... max_thrust_vacuum...   
//Altitude Effects normalized_thrust_vs_alt ... end_normalized_thrust_vs_alt   
//Specific Impulse isp_vs_alt ... end isp_vs_alt   
//Spin-up/Spin-Down normalized_spinup ... normalized_spindown ...   
//Smoke Trail Appearance When Burning creates_s smoke_trail ...   
end_liquid_propellant_rocket 
```

液体推进剂火箭发动机在 AFSIM 中通过一系列参数和表格来定义其性能和行为。这些

参数帮助模拟发动机在不同飞行条件下的表现。

液体推进剂火箭发动机的基本概念

液体推进剂火箭发动机使用液体燃料和液体氧化剂，这些推进剂通过泵从各自的储罐中转移到发动机中。泵将压力提高到发动机的工作压力以上，然后推进剂被注入发动机，以确保雾化和快速混合。液体火箭发动机的典型组件包括发动机、燃料箱和用于固定这些部件并连接到有效载荷和发射台（或飞行器）的结构。

液体推进剂火箭发动机的优势

可控推力：液体推进剂火箭发动机的推力可以调节（节流），并且可以在稍后阶段关闭和重新启动。

高能量密度：由于高燃烧温度，液体推进剂的能量密度（每千克推进剂的焦耳数）往往很高，导致比冲（每千克推进剂的冲量）非常大。

高性能：液体推进剂发动机提供更高的性能，即每单位推进剂重量提供更大的推力。

液体推进剂火箭发动机的设计与开发

液体推进剂火箭发动机的设计涉及多个方面，从推力室到涡轮泵、阀门、推进剂箱和控制系统的每个组件。设计过程需要考虑推进剂的流动、燃烧效率、热管理和结构完整性等因素。

液体推进剂火箭发动机的应用

液体火箭发动机被用于多种应用，包括将人类送入轨道的航天飞机、用于发射卫星的无人导弹，以及二战后用于高速度研究飞机的发动机。这些发动机的灵活性和高性能使其成为许多航天任务的首选。

通过这些参数和表格，AFSIM能够模拟液体推进剂火箭发动机在不同飞行条件下的动态响应，提供更真实的飞行模拟体验。

推力参数

max_thrust_sealevel <力值>

这个参数指定了在海平面条件下可以产生的最大推力。应指定 max_thrust_sealevel 或max_thrust_vacuum 之一，而不是同时指定两者。

max_thrust_vacuum <力值>

这个参数指定了在真空条件下可以产生的最大推力。应指定 max_thrust_sealevel 或max_thrust_vacuum 之一，而不是同时指定两者。

推力与高度的关系

normalized_thrust_vs_alt

这是一个“归一化推力”与高度的简单对照表。归一化推力是一个将与名义比冲计算推力相乘的值，通常使用 max_thrust_sealevel 和 isp_vs_alt 计算。这允许考虑高度对推力产生的影响。

```txt
normalized_thrust_vs_alt  
#alt normalized_thrust  
0.0 1.0  
300000.0 1.0  
end_normalizedTHRUST_vs-alt 
```

```txt
isp_vs_alt 
```

这是一个比冲（Isp）与高度的简单对照表，单位为秒。

```txt
isp_vs_alt #alt_feet Isp(sec) 0.0 285.0 100000.0 290.0 300000.0 295.0 end_isp_vs_alt 
```

发动机动态响应

normalized_spinup <实数值>

这个参数指定了归一化位置/秒的加速率。值为 1.0 表示发动机将在 1 秒内从零加速到全推力，而值为 0.1 表示需要 10 秒。

normalized_spindown <实数值>

这个参数指定了归一化位置/秒的减速率。值为 1.0 表示发动机将在 1 秒内从全推力减速到零推力，而值为 0.1 表示需要 10 秒。

视觉效果

creates_smoke_trail <布尔值>

这个参数决定火箭是否会产生烟雾轨迹的外观。默认情况下，液体推进剂火箭不会产生烟雾轨迹，而固体推进剂火箭会产生烟雾轨迹。

# 3.6.3.2.2.4. 固体推进剂火箭发动机 Solid-Propellant Rocket Motors

```txt
solid_propellant_rocket   
// Thrust Parameters rated_thrust... thrust_vs_time_sealevel ... end_thrust_vs_time_sealevel thrust_vs_time_vacuum ... end_thrust_vs_time_vacuum   
// Specific Impulse isp_vs_alt ... end isp_vs_alt   
// Smoke Trail Appearance When Burning creates_s smoke_trail ...   
end_solid_propellant_rocket 
```

在 AFSIM 中，固体推进剂火箭发动机通过一系列参数和表格来定义其性能和行为。与液体推进剂火箭不同，固体推进剂火箭不需要指定燃料供给，因为它们包含自己的推进剂特性。

rated_thrust <力值>

这个参数指定了固体推进剂火箭发动机的“额定推力”。由于推力依赖于多种条件，这是一个参考值，通常用于计算推力百分比。

thrust_vs_time_sealevel

这是一个简单的推力与时间的对照表，单位为磅，适用于海平面压力条件。应指定thrust_vs_time_sealevel 或 thrust_vs_time_vacuum 之一，而不是同时指定两者。

```txt
thrust_vs_time_sealevel
#time thrust_lbs
0.0 0.0
0.1 2000.0
6.0 2000.0
6.5 200.0
end_thrust_vs_time_sealevel 
```

thrust_vs_time_vacuum

这是一个简单的推力与时间的对照表，单位为磅，适用于真空压力条件。应指定thrust_vs_time_sealevel 或 thrust_vs_time_vacuum 之一，而不是同时指定两者。

```csv
thrust_vs_time_vacuum
#time thrust_lbs
0.0 0.0
0.1 2000.0
6.0 2000.0
6.5 200.0
end_thrust_vs_time_vacuum 
```

isp_vs_alt

这是一个比冲（Isp）与高度的简单对照表，单位为秒。

```txt
isp_vs_alt #alt_feet lsp(sec) 0.0 200.0 100000.0 200.0 300000.0 200.0 end isp_vs_alt 
```

creates_smoke_trail <布尔值>

这个参数决定火箭是否会产生烟雾轨迹的外观。默认情况下，固体推进剂火箭会产生烟雾轨迹，而液体推进剂火箭不会。

# 3.6.3.3. 六自由度基础模型 WSF_SIX_DOF_MOVER

```txt
mover<name>WSF SIX DOF MOVER 
```

```c
// SixDOF Vehicle Type Commands  
autopilot_no_control ...  
enable Controls ...  
enable thrust_vectoring ...  
engines_on ...  
follow_vertical_track ...  
ignore_all_crashes ...  
six_dof_alt ...  
six_dof_ned Heading ...  
six_dof_ned_pitch ...  
six_dof_ned-roll ...  
six_dof_position ...  
six_dof_set Velocity_ned_fps ...  
produces_launch_s smoke ...  
throttle_afterburner ...  
throttle_full ...  
throttle_idle ...  
wash_in_conditions ...  
// Route Commands  
route ... end-route  
use_route ...  
// Script Methods -- see WsfSixDOF_Mover 
```

WSF_SIX_DOF_MOVER 是一个基于时间步长的基础类，用于在三个平移和三个旋转自由度上操作的物理学驱动的移动器。这些移动器提供了比其他移动器更高阶的动态能力。有两种 类 型 的 SixDOF 移 动 器 可 供 选 择 ： WSF_RIGID_BODY_SIX_DOF_MOVER 和WSF_POINT_MASS_SIX_DOF_MOVER。

WSF_RIGID_BODY_SIX_DOF_MOVER 直接继承自 WSF_P6DOF_MOVER，并保留了其几乎所 有 的 功 能 。 它 是 真 正 的 6DOF 移 动 器 ， 具 备 三 个 轴 的 旋 转 惯 性 。WSF_POINT_MASS_SIX_DOF_MOVER 旨在提供一个更简单的模型，同时保留了诸如子对象和序列器等有用的特性。它需要的调校远少于刚体移动器，但仍可以进行精细调整以匹配所需特性。

注意 由于其较高的精度，WSF_RIGID_BODY_SIX_DOF_MOVER 涉及的计算量显著高于大多 数 3DOF 模 型 。 它 还 以 相 对 较 高 的 更 新 率 （ $1 0 0 ~ \mathsf { H z }$ ） 进 行 内 部 更 新 。WSF_POINT_MASS_SIX_DOF_MOVER 对数值的敏感度较低，因此以 $2 0 ~ \mathsf { H z }$ 进行更新。单个点质量模拟帧并不比刚体模拟帧快多少，但由于需要的帧数较少，它的计算成本要低得多。分析师可能会采取的一种策略是，为一个 vehicle 生成刚体和点质量版本，在必要时使用刚体表示，并在较不关键的移动器和飞行的较不重要阶段使用点质量模型。

使用 WSF_RIGID_BODY_SIX_DOF_MOVER 的场景必须设置 minimum_mover_timestep，并将其设置为不大于 0.01 秒——比实时默认最小时间步长 0.05 秒要小。这是必要的，以

便在使用显式实时模式或诸如 Warlock 之类的实时应用程序时，允许制导计算机和序列器与 SixDOF vehicle 同步更新。

六自由度类型命令  

<table><tr><td>命令</td><td>vehicle_type&lt;string&gt;</td></tr><tr><td>解释</td><td>定义移动器使用的对象类型。</td></tr><tr><td>命令</td><td>autopilot_no_control&lt;boolean-value&gt;</td></tr><tr><td>解释</td><td>这将命令自动驾驶仪“归零”所有控制,将操纵杆和方向舵居中,并将油门拉回到零(空闲)。类似于 enable Controls,但命令的是自动驾驶仪,而不是控制本身。对应的脚本方法: WsfSixDOF_Mover.SetAutopilotNoControl</td></tr><tr><td>命令</td><td>enable Controls&lt;boolean-value&gt;</td></tr><tr><td>解释</td><td>启用/禁用来自任何来源的控制输入(自动驾驶,外部手动驾驶等)。控制默认启用,因此该命令通常用于在开始时禁用控制。这通常用于允许武器在从载机释放后以弹道方式下降而不进行控制输入,然后调用脚本方法 WsfSixDOF_Mover EnableControls 以在武器安全脱离飞机后建立控制输入。对应的脚本方法: WsfSixDOF_Mover EnableControls</td></tr><tr><td>命令</td><td>enable thrust_vectoring&lt;boolean-value&gt;</td></tr><tr><td>解释</td><td>指示是否启用推力矢量控制。对应的脚本方法: WsfSixDOF_Mover EnableThrustVectoring</td></tr><tr><td>命令</td><td>engines_on&lt;boolean-value&gt;</td></tr><tr><td>解释</td><td>指示在场景开始时发动机应开启或关闭。对应的方法: WsfSixDOF_Mover.StartupEngines 或 WsfSixDOF_Mover.ShutdownEngines</td></tr><tr><td>命令</td><td>follow_vertical_track</td></tr><tr><td>解释</td><td>通常情况下,自动驾驶仪在改变高度时会尽可能快地爬升/下降(在当前限制范围内),但当设置 follow_vertical_track 时,自动驾驶仪将使用允许对象沿直线垂直轨迹在航路点之间平稳/缓慢改变高度的垂直速度。尽管这是一个选项,且默认不使用 follow_vertical_track,但它常常被使用,因为许多用户更喜欢这种“渐进”的垂直飞行路径,而不是默认的航路点之间的“快速”高度变化。</td></tr><tr><td>命令</td><td>ignore_all_crashes&lt;boolean-value&gt;</td></tr><tr><td>解释</td><td>指示移动器是否忽略所有形式的碰撞。这通常用于测试。</td></tr><tr><td>命令</td><td>six_dof_alt&lt;length-value&gt;</td></tr><tr><td>解释</td><td>设置移动器的初始高度。</td></tr><tr><td>命令</td><td>six_dof_ned Heading&lt;angle-value&gt;</td></tr><tr><td>解释</td><td>设置移动器的初始航向角。</td></tr><tr><td>命令</td><td>six_dof_ned_Pitch&lt;angle-value&gt;</td></tr><tr><td>解释</td><td>设置移动器的初始俯仰角。</td></tr><tr><td>命令</td><td>six_dof_ned-roll&lt;angle-value&gt;</td></tr><tr><td>解释</td><td>设置移动器的初始滚转角。</td></tr><tr><td>命令</td><td>six_dof_position&lt;real-value&gt;</td></tr><tr><td>解释</td><td>设置移动器的初始位置(使用小数纬度和经度)。</td></tr><tr><td>命令</td><td>six_dof_set Velocity_ned_fps&lt;real-value&gt;</td></tr><tr><td>解释</td><td>设置移动器在 NED 坐标系中的初始速度,单位为英尺/秒。</td></tr><tr><td>命令</td><td>produces_launch_s smoke&lt;time-value&gt;</td></tr><tr><td>解释</td><td>设置 vehicle 在发射时产生发射烟雾/闪光效果(仅外观)的时间。如果不需要发射效果,则不应定义此命令。</td></tr><tr><td>命令</td><td>throttle_afterburner&lt;boolean-value&gt;</td></tr><tr><td>解释</td><td>在场景开始时将油门设置为加力燃烧器。对应的脚本方法: WsfSixDOF_MoverMOVThrottleToAfterburner</td></tr><tr><td>命令</td><td>throttle_full&lt;boolean-value&gt;</td></tr><tr><td>解释</td><td>在场景开始时将油门设置为最大功率。对应的脚本方法: WsfSixDOF_MoverMOVThrottleToFull</td></tr><tr><td>命令</td><td>throttle_idle&lt;boolean-value&gt;</td></tr><tr><td>解释</td><td>在场景开始时将油门设置为空闲。
对应的脚本方法: WsfSixDOF_Mover.MoveThrottleToldle</td></tr><tr><td>命令</td><td>wash_in_conditions &lt;boolean-value&gt;</td></tr><tr><td>解释</td><td>包含此标志表示在初始化时应对该移动器进行“洗入”条件。这意味着对象将在初始化时运行特殊模式，以帮助“渐进”和“稳定”对象，通过允许其有一些时间来稳定在所需的攻角（alpha）以及正确的油门设置。这对于确保 vehicle 在开始模拟时稳定是有用的——例如，它们可能在模拟开始时缺乏正确的攻角。
  由于“洗入”操作实际上执行了大量的“更新”功能以达到稳定状态，因此计算量很大，应仅在需要时使用。此外，不应对子对象使用。
  在稳定的“洗入”操作期间，参数必须满足各种容差才能被认为是稳定的。参数包括高度、垂直速度、攻角、速度、俯仰控制输入和油门控制输入。</td></tr></table>

# 路线命令

<table><tr><td>命令</td><td>route ... end-route</td></tr><tr><td>解释</td><td>route
position ... 指定航路点的纬度和经度。
altitude ... 指定航路点的高度（MSL）。
speed ... 指定航路点的速度。
label ... 将标签与紧随其后的航路点定义关联。这可以用作 goto 命令的目标。
goto ... 转到当前路线中具有指定标签的航路点。
bank_angle_limit ... 指定用作转弯时的最大滚转角。这有效地将 radialacceleration 设置为 g * tan(bank_angle_limit)。
radialacceleration ... 指定用作转弯时的径向加速度。
turn_g_limit ... 指定用作转弯时的最大转弯过载。这有效地将 radialacceleration 设置为√turn_g_limit2 - g2
switch_on_passing ...
switch_onapproach ... 定义当移动器应声明已到达该航路点并应开始向下一个航路点移动的条件。switch_on_passing 有时被称为“长转弯”，在平台经过或旁边经过航路点时触发切换。switch_onapproach 有时被称为“短转弯”，在到达航路点之前触发切换。
注意，WSF SIX DOF MOVER 默认为 switch_onapproach，这与大多数其他移动器不同。
end-route</td></tr><tr><td>命令</td><td>use-route &lt;route-name&gt;</td></tr><tr><td>解释</td><td>提供要遵循的路线名称。假定该路线是预定义的绝对路线。
route 的定义参见：4.8.1 路由 route</td></tr></table>

# 示例

以下是一个示例路线定义。最简单的路线包括多行使用 position、altitude 和 speed 命令，如下所示：

```txt
route position 21.325n 158.000w altitude 9000.0 ft speed 600.0 kts position 21.325n 157.941w altitude 9000.0 ft speed 600.0 kts position 21.250n 157.800w altitude 9000.0 ft speed 600.0 kts position 21.260n 157.700w altitude 9000.0 ft speed 600.0 kts position 21.400n 157.700w altitude 9000.0 ft speed 600.0 kts position 21.700n 157.900w altitude 13000.0 ft speed 600.0 kts 
```

```txt
position 21.900n 158.300w altitude 9000.0 ft speed 600.0 kts position 21.600n 158.200w altitude 9000.0 ft speed 600.0 kts position 21.550n 158.120w altitude 9000.0 ft speed 600.0 kts position 21.325n 157.941w altitude 9000.0 ft speed 600.0 kts position 21.325n 157.900w altitude 9000.0 ft speed 600.0 kts end-route 
```

Script Methods

要了解 WSF_SIX_DOF_MOVER 支持的各种脚本方法，请参见 WsfSixDOF_Mover。

# 3.6.3.4. 刚体六自由度运动模型 WSF_RIGID_BODY_SIX_DOF_MOVER

```txt
mover <name> WsF_RIGID_BODY SIX_DOF_MOVER // RB6 Vehicle Type Commands vehicle_type ... landing_gear_down ... nws_enabled ... parking_brake_on ... taxi_mode_enabled ... ... WsF_SIX_DOF_MOVER Commands ... // Script Methods -- see WsfRigidBodySixDOF_Mover end_mover 
```

WSF_RIGID_BODY_SIX_DOF_MOVER 是 WSF_SIX_DOF_MOVER 的一种特定类型，使用一阶和二阶力和力矩系数来实现旋转和平移。它直接继承自 WSF_P6DOF_MOVER，并采用了几乎所有的功能。

构建一个成功的 WSF_RIGID_BODY_SIX_DOF_MOVER 所需的细节和数据是非平凡的，但结果是一个能够自然捕捉其他移动器（包括 WSF_POINT_MASS_SIX_DOF_MOVER）无法捕捉的现象和动态的移动器。

WSF_RIGID_BODY_SIX_DOF_MOVER 仅使用惯性张量的主（对角）元素。这种简化有助于加快执行速度并减少一些复杂性，但可能会导致交叉耦合效应的阻尼不足。净力和力矩从空气动力、推进和重力源中汇总，并直接用于运动方程。

空气动力系数可用于所有自由度，包括阻尼导数系数。并非所有系数都是必需的，但每个使用的表格都可以增加模型的精度。

# RB6 vehicle 类型命令

对于 WSF_RIGID_BODY_SIX_DOF_MOVER，最重要的命令是 vehicle_type，它定义了对象 的 性 能 特 征 。 刚 体 vehicle_type 在 six_dof_object_types 块 中 定 义 为command:rigid_body_vehicle_type。必须在引用之前定义 six_dof_vehicle_type。

有关如何 创建 rigid_body_vehicle_type 的信息， 请参见:3.6.3.1.3 刚体载具 类型rigid_body_vehicle_type。

<table><tr><td>命令</td><td>vehicle_type&lt;string&gt;</td></tr><tr><td>解释</td><td>定义移动器使用的对象类型。vehicle_type在six_dof_object_types块中定义，必须在引用之前定义。最简单的WSF_RIGID_BODY SIX_DOF_MOV定义如下：mover WSF_RIGIDBODY SIX_DOF_MOVvehicle_type F-15Cend_mover这表示将使用F-15C vehicle 类型。F-15C 必须是 rigid_body(vehicle_type，不接受point_mass_vehicle_type 对象。</td></tr><tr><td>命令</td><td>landing_gear_downboolean-value&gt;</td></tr><tr><td>解释</td><td>指示在场景开始时起落架是否应放下。对应的脚本方法：WsfRigidBodySixDOF_Mover.LowerLandingGear 或 WsfRigidBodySixDOF_Mover.RetractLandingGear</td></tr><tr><td>命令</td><td>nws_enableboolean-value&gt;</td></tr><tr><td>解释</td><td>指示是否应启用前轮转向。前轮转向通常在滑行时使用，但在起飞滑跑前应移除。对应的脚本方法：WsfRigidBodySixDOF_Mover.SetEnableNWS</td></tr><tr><td>命令</td><td>parking_brake_onboolean-value&gt;</td></tr><tr><td>解释</td><td>设置在场景开始时驻车制动是否应开启。对应的脚本方法：WsfRigidBodySixDOF_Mover.SetParkingBrake 或 WsfRigidBodySixDOF_MoverReleaseWheelBrakes</td></tr><tr><td>命令</td><td>taxi_modeenabledboolean-value&gt;</td></tr><tr><td>解释</td><td>设置在场景开始时自动驾驶仪是否应处于滑行模式。仅在平台在地面时使用。对应的脚本方法：WsfRigidBodySixDOF_Mover.SetTaxiMode</td></tr></table>

# 脚本方法

要 了 解 WSF_RIGID_BODY_SIX_DOF_MOVER 支 持 的 各 种 脚 本 方 法 ， 请 参 见WsfRigidBodySixDOF_Mover。

# 3.6.3.5. 点质量六自由度模型 WSF_POINT_MASS_SIX_DOF_MOVER

```txt
mover <name> WSF_POINT_MASS_SIX_DOF_MOVER // PM6 Vehicle Type Commands vehicle_type ... .. WSF_SIX_DOF_MOVER Commands ... // Script Methods -- see WsfPointMassSixDOF_Mover end_mover 
```

WSF_POINT_MASS_SIX_DOF_MOVER 是 WSF_SIX_DOF_MOVER 的一种特定类型，使用简单的一阶力系数进行平移，并使用基于效果的控制来执行旋转。

与 WSF_RIGID_BODY_SIX_DOF_MOVER 相比，WSF_POINT_MASS_SIX_DOF_MOVER 设置更简单，所需数据更少，数值更稳定，但无法再现构建良好的 WSF_RIGID_BODY_SIX_DOF_MOVER的高阶动态。

与“完整”的 6DOF 模型不同，点质量模型仅使用标量质量属性，并且不知道质量分布和由此产生的惯性张量。旋转能力在表数据中定义，并在执行期间根据 vehicle 质量和飞行条件（如攻角和空气密度）进行修改。推力矢量的旋转也根据表数据施加，推力矢量保持静态。

注意 这种限制影响了垂直起降 vehicle 的构建。可以通过在起飞和着陆配置中包括多个发动机实例来近似 VTOL 行为，并使用脚本命令适当地点燃和关闭这些实例。

WSF_POINT_MASS_SIX_DOF_MOVER 不支持力或旋转的空气动力阻尼效应。可以使用参数来近似静态稳定性，但不是必需的。

# PM6 vehicle 类型命令

对于 WSF_POINT_MASS_SIX_DOF_MOVER，最重要的命令是 vehicle_type，它定义了对象的性能特征。点质量 vehicle_type 在 six_dof_object_types 块中定义，必须在引用之前定义。

```erb
vehicle_type <string> 
```

定义移动器使用的对象类型。点质量 vehicle_type 在 six_dof_object_types 块中定义，必须在引用之前定义。

最简单的 WSF_POINT_MASS_SIX_DOF_MOVER 定义如下：

```txt
mover WSF_POINT_MASS_SIX_DOF_MOVER  
vehicle_type F-15C  
end_mover 
```

这表示将使用 F-15C vehicle 类型。F-15C 必须是 point_mass_vehicle_type（参见：3.6.3.1.2 点质量载具类型 point_mass_vehicle_type），不接受 rigid_body_vehicle_type 对象。

# 脚本方法

要 了 解 WSF_POINT_MASS_SIX_DOF_MOVER 支 持 的 各 种 脚 本 方 法 ， 请 参 见WsfPointMassSixDOF_Mover。

# 3.6.3.6. 旧的六自由度运动模型 WSF_P6DOF_MOVER（弃用）

随着 WSF_RIGID_BODY_SIX_DOF_MOVER 的引入，WSF_P6DOF_MOVER 现已弃用。强烈建 议 用 户 避 免 在 任 何 新 工 作 中 使 用 WSF_P6DOF_MOVER ， 并 应 改 用WSF_RIGID_BODY_SIX_DOF_MOVER。此外，用户还应修改现有的场景和数据文件，将WSF_P6DOF_MOVER 替换为 WSF_RIGID_BODY_SIX_DOF_MOVER。WSF_P6DOF_MOVER 仍将在未来的 AFSIM版本中包含一段时间（大约十二个月），但随后将从 AFSIM 代码库中删除。

以下是对 WSF_P6DOF_MOVER 的描述，以增进对整个六自由度模型的理解。

概述 WSF_P6DOF_MOVER 是一个高保真、伪 6DOF（六自由度）移动器。P6DOF 提供六个自由度（允许姿态/角运动学和平移运动学），能够比基于 3DOF 的模型提供更高保真的模拟，其物理模型（使用力和力矩累积）包括马赫数和高度效应。P6DOF 从一开始就设计成可以与 AFSIM集成，简化了其在框架内的使用。

WSF_P6DOF_MOVER 是一个伪 6DOF 模型，这意味着它在姿态计算上包含了一些简化，与“硬核”6DOF 模型相比。这些简化涉及一些角加速度和惯性张量的简化，但模型在运动计算中保留了完整的六个自由度——因此，P6DOF 是一个真正的 6DOF（不像其他被称为伪6DOF 的模型，但实际上只有 5DOF）。P6DOF 中使用的姿态简化实际上对姿态运动学的影响很小。然而，这些“伪”设计特性的结果是，P6DOF 需要的数据更少，需要的计算更少，并且比完整的 6DOF 模拟更容易使用，同时它仍然提供了现实的建模，包括偏航、俯仰和滚转以及攻角（α）和侧滑角（β）效应。

WSF_P6DOF_MOVER 设计成支持多种移动器 vehicle，包括固定翼飞机、旋翼机、导弹（包括空对空（AAM）、地对空（SAM）、空对地（AGM）和反弹道导弹（ABM））、弹道导弹（包括短程弹道导弹（SRBM）、中程弹道导弹（MRBM）、中远程弹道导弹（IRBM）和洲际弹道导弹（ICBM））、空间发射 vehicle（包括典型的多级线性级联助推器以及并联

级联配置和带翼再入飞行器）和航天器/卫星。初步支持集中在固定翼飞机，但将在未来版本中支持/扩展其他类型。

WSF_P6DOF_MOVER 使用“框架无关”的 P6DOF 核心软件，允许其在 AFSIM 之外的其他模拟框架中使用（如果需要）。

使 用 WSF_P6DOF_MOVER 比 使 用 WSF_AIR_MOVER 、 WSF_GUIDED_MOVER 、WSF_HYBRID_MOVER、WSF_TBM_MOVER 或 WSF_KINEMATIC_MOVER 的优势在于平台的姿态建模更准确，具有真实的偏航、俯仰和滚转以及通过现实的基于力和力矩的物理/空气动力学模型计算的攻角（α）。使用 WSF_P6DOF_MOVER 的缺点是其增加的现实性需要更多的计算和计算机处理时间。

注意 由于其增加的保真度，WSF_P6DOF_MOVER 涉及的计算比大多数 3DOF 模型要多得多。它还必须以相对较高的更新率（通常为 $1 0 0 ~ \mathsf { H z }$ ）进行迭代，以获得高精度。因此，它将消耗更多的计算能力，导致比简单模型如 WSF_AIR_MOVER 更长的运行时间。因此，WSF_P6DOF_MOVER 最好用于小型场景或在较大场景中关注特定“感兴趣的平台”，其中特定平台的保真度增加很重要。使用 WSF_P6DOF_MOVER 的场景必须设置最小移动器时间步长，并将其设置为不大于 0.01 秒--比默认最小时间步长 0.05 秒小。这对于允许制导计算机和序列器与 P6DOFvehicle 同步更新是必要的，特别是在使用显式实时模式或使用实时应用程序如 Warlock 时。为了安全，建议使用 0.001 秒（1 毫秒）。注意，这并不强制每毫秒更新一次，但提供了一个缓冲区，以防止浮点错误可能导致的更新遗漏。

警告 随着 WSF_RIGID_BODY_SIX_DOF_MOVER 的引入，WSF_P6DOF_MOVER 现已弃用。强 烈 建 议 用 户 避 免 在 任 何 新 工 作 中 使 用 WSF_P6DOF_MOVER ， 并 应 改 用WSF_RIGID_BODY_SIX_DOF_MOVER。此外，用户还应修改现有的场景和数据文件，将WSF_P6DOF_MOVER 替换为 WSF_RIGID_BODY_SIX_DOF_MOVER。WSF_P6DOF_MOVER 仍将在未来的 AFSIM版本中包含一段时间（大约十二个月），但随后将从 AFSIM 代码库中删除。

# 3.6.4. 军事类型 Military Types

# 3.6.4.1. 空空导弹运动模型 WSF_ARGO8_MOVER

```txt
mover WSF.ArgO8_MOVER
...
... base mover commands ...
library_name <string-value>
missile_name <string-value>
missile_type <string-value>
argo_log_file_path <path-name>
guidance_update_interval <real-value>
guidance_method ...
seeker_method ...
output_fuze_data ...
endgame/gees <real-value>
end_mover 
```

WSF_ARGO8_MOVER 提供了用于 TMAP ARGO 导弹模型对象的移动器。该移动器使用Brawler 的 ARGO 接口作为其基础。

命令 library_name <类型名称>

<table><tr><td>解释</td><td>指定导弹的ARGO库。不要包含文件扩展名(.so或.dll)。这些库位于构建中的库目录中。</td></tr><tr><td>命令</td><td>missile_name&lt;类型名称&gt;</td></tr><tr><td>解释</td><td>指定导弹的名称。虽然必要,但实际上不会影响飞行路径,因此可以命名为任何名称。</td></tr><tr><td>命令</td><td>missile_type&lt;类型名称&gt;</td></tr><tr><td>解释</td><td>指定要使用的ARGO导弹模型类型。目前,标准类型涵盖了大多数Brawler导弹模型。默认值:standard</td></tr><tr><td>命令</td><td>argo_log_file_path&lt;路径名称&gt;</td></tr><tr><td>解释</td><td>指定用于记录ARGO输出的日志文件路径以进行调试。当指定时会自动开启日志记录。注意:生成的文件与ARGO接口输出匹配,端口号与列号相关联。默认值:无日志记录</td></tr><tr><td>命令</td><td>guidance_update_interval&lt;实数值&gt;</td></tr><tr><td>解释</td><td>指定制导轨迹数据的更新速率。影响真实数据和轨迹数据的速率。如果传感器帧速率较慢,导弹将不会以此命令指定的速率更新。</td></tr><tr><td>命令</td><td>guidance_method[truth | track]</td></tr><tr><td>解释</td><td>指定导弹在被射手引导时使用真实数据还是轨迹数据。对于真实数据,不需要上行链路。默认值:track</td></tr><tr><td>命令</td><td>seeker_method[truth | track]</td></tr><tr><td>解释</td><td>指定一旦导引头开启后是引导真实数据还是轨迹数据。导引头将从ARGO输出或导弹上定义的导引头开启,脚本用户可以控制导引头何时开启。一旦传感器在脚本中开启,模型将识别其为开启状态,并不再遵守制导更新间隔。默认值:track</td></tr><tr><td>命令</td><td>output_fuze_data</td></tr><tr><td>解释</td><td>如果作为命令包含,将输出所有发射导弹的引信状态。如果导弹通过其他方式结束交战,则不会显示输出。</td></tr><tr><td>命令</td><td>endgame/gees&lt;实数值&gt;</td></tr><tr><td>解释</td><td>指定导弹引信所需的最小末端过载。注意:不应用于常规交战,适用于使用诸如weapon.tools等工具进行导弹飞行路径分析。默认值:0</td></tr></table>

# 3.6.4.2. Brawler 空战运动模型 WSF_BRAWLER_MOVER

```txt
mover WSF_BRAWLER_MOV  
aero_file  
draw_projection  
end_MOV 
```

WSF_BRAWLER_MOVER 是 BRAWLER 中 AROTYP1 移动器模型的精确复制。BRAWLER像是一个专业的飞行空战战术仿真工具。它设计用于加载 BRAWLER 飞机定义文件（仅关注空气动力学和物理块），以指定其飞行能力。WSF_BRAWLER_MOVER 还配备了执行大多数常规移动器命令的能力，例如 GoToLocation()、TurnToHeading()、GoToAltitude()、GoToSpeed()、FollowRoute()、ReturnToRoute()。WSF_BRAWLER_MOVER 也可以飞行路线，但它会忽略路线中定义的任何加速或转向要求，以便在飞行时使用其自身的逻辑。实际上，WSF_BRAWLER_MOVER 保证遵守的唯一路线命令是“位置”、“高度”、“速度”和“爬升率”（如果提供）。当 WSF_BRAWLER_MOVER 到达路线的终点时，其默认行为是返回起点并再次飞行该路线。

WSF_BRAWLER_MOVER 的典型用法是在目标的目视范围内使用 WsfBrawlerProcessor

移动器方法进行战术飞行，而在目视范围外（例如飞行路线、前往位置或转向航向）时使用常规的 WsfPlatform 位置和导航方法。

<table><tr><td>命令</td><td>aero_file &lt;文件名&gt;</td></tr><tr><td>解释</td><td>指定 BRAWLER 飞机定义文件的文件名。文件的内容将完全定义此移动器的飞行能力。</td></tr><tr><td>命令</td><td>draw_projection</td></tr><tr><td>解释</td><td>如果指定，将在 DIS 回放文件中渲染黄色点，表示给定当前机动命令的 BRAWLER 移动器的前向投影。</td></tr></table>

# 3.6.4.3. 炮弹运动模型 WSF_FIRES_MOVER

```batch
mover WSF_FIRESMOVER ... Platform Part Commands ... //Mover Commands ... WSF_FIRESMOVERCommands... ...WSF_FIRESMOVERTrajectoryCommands...   
end_mover 
```

WSF_FIRES_MOVER 提供沿弹道轨迹的运动，假设一阶阻力（阻力与速度的一次方成正比）。由此产生的轨迹是确定性的，并以单一参数为特征。这种简单性使得可以轻松地以现实的撞击时间击中某个位置或目标。然而，这些轨迹不如使用完整空气动力学、发射表和数值积分计算的轨迹那么现实。该移动器最常用于火箭、火炮或迫击炮平台定义，从配置了WSF_FIRES_LAUNCH_COMPUTER 和相关 fires_tables 的发射器发射。

<table><tr><td>命令</td><td>remove_on_impact &lt;布尔值&gt;</td></tr><tr><td>解释</td><td>定义是否在撞击时移除发射平台并终止任何活动的武器交战。默认值: true</td></tr><tr><td>命令</td><td>usesimple_propagation &lt;布尔值&gt;</td></tr><tr><td>解释</td><td>定义是否使用简单的抛物线轨迹,仅使用最大高度和飞行时间的值。默认值: false</td></tr><tr><td>命令</td><td>constrain_to.simple_propagation &lt;布尔值&gt;</td></tr><tr><td>解释</td><td>如果无法为给定的射程、最大高度和飞行时间计算出解决方案,则使用use-simple_propagation 选项给出的解决方案。默认值: false;移动器将放宽最大高度的条件,以计算解决方案。</td></tr></table>

# 轨迹命令

注意：通常，使用 fires_table 以及在模拟期间动态发射武器来指定特定轨迹。然而，也可以使用这些命令手动配置移动器。

<table><tr><td>命令</td><td>impact_range &lt;长度值&gt;</td></tr><tr><td>解释</td><td>定义弹药将在发射平台的射程内爆炸的范围。</td></tr><tr><td>命令</td><td>initial_bearing &lt;角度值&gt;</td></tr><tr><td>解释</td><td>定义弹药在其轨迹中从发射平台出发的方位角。</td></tr><tr><td>命令</td><td>impact_location &lt;字符串值&gt;&lt;纬度值&gt;&lt;经度值&gt;&lt;长度值&gt;</td></tr><tr><td>解释</td><td>使用地理点参考指定撞击位置。例如:impact_location geo-point-tag 38n 90w 100 ft // 高度</td></tr><tr><td>命令</td><td>time_of_flight &lt;时间值&gt;</td></tr><tr><td>解释</td><td>指定弹药的飞行时间。</td></tr><tr><td>命令</td><td>maximum_height &lt;长度值&gt;</td></tr><tr><td></td><td>maximum_ordiante&lt;长度值&gt;</td></tr><tr><td>解释</td><td>指定弹药在其轨迹中将达到的最大高度。</td></tr></table>

# 3.6.4.4. 编队飞行模型 WSF_FORMATION_FLYER

```tcl
mover WSFFormation_FLYER   
... Platform Part Commands ...   
// Mover Commands   
update_interval ...   
update_time_tolerance ...   
// Follower Commands   
position ...   
altitude ...   
speed ...   
heading ...   
body_g_limit ...   
maximum_bank_angle ...   
maximum_axialacceleration ...   
maximum_radialacceleration ...   
maximum_climb_rate ...   
maximum_roll_rate ...   
maximum_turn_rate ...   
maximum_speed ...   
minimum_speed ...   
velocity_pursuit_gain ...   
// Formation Flyer Commands   
lead_aircraft ...   
formation Rolls_with_lead   
offset_forward_from_lead ...   
offset_right_from_lead ...   
offset_down_from_lead ...   
initialize_at_offset 
```

WSF_FORMATION_FLYER 是一个用于模拟编队飞行的移动器。它允许多个飞行器以编队形式飞行，并且可以根据领队飞行器的位置和运动进行调整。该移动器支持多种命令来控制编队飞行的行为和参数。

# 跟随者命令

<table><tr><td>命令</td><td>position&lt;纬度值&gt;&lt;经度值&gt;</td></tr><tr><td>解释</td><td>初始纬度和经度位置。默认值:0n 0e</td></tr><tr><td>命令</td><td>altitude&lt;长度值&gt;</td></tr><tr><td>解释</td><td>初始高度(相对于椭球体)。默认值:0米</td></tr><tr><td>命令</td><td>speed&lt;速度值&gt;</td></tr><tr><td>解释</td><td>初始速度。默认值:10米/秒</td></tr><tr><td>命令</td><td>heading&lt;角度值&gt;</td></tr><tr><td>解释</td><td>初始航向。默认值:0度</td></tr><tr><td>命令</td><td>body_g_limit&lt;加速度值&gt;</td></tr><tr><td>解释</td><td>机体过载限制。值必须大于地球重力加速度。</td></tr><tr><td>命令</td><td>maximum_bank_angle&lt;角度值&gt;</td></tr><tr><td>解释</td><td>最大允许的倾斜角。值必须在5度到85度之间。</td></tr><tr><td>命令</td><td>maximum_axialacceleration&lt;加速度值&gt;</td></tr><tr><td>解释</td><td>当需要加速时使用的最大轴向加速度。默认值:0g</td></tr><tr><td>命令</td><td>maximum_radialacceleration&lt;加速度值&gt;</td></tr><tr><td>解释</td><td>转弯时使用的最大径向加速度。默认值:2g</td></tr><tr><td>命令</td><td>maximum_climb_rate&lt;速度值&gt;</td></tr><tr><td>解释</td><td>当需要改变高度时使用的爬升率。如果航点不包括爬升率规范,则使用此值。默认值:5米/秒</td></tr><tr><td>命令</td><td>maximum_roll_rate&lt;角速度值&gt;</td></tr><tr><td>解释</td><td>最大滚转率。值必须大于0。</td></tr><tr><td>命令</td><td>maximum_turn_rate&lt;角速度值&gt;</td></tr><tr><td>解释</td><td>最大转弯率。值必须大于0。</td></tr><tr><td>命令</td><td>maximum_speed&lt;速度值&gt;</td></tr><tr><td>解释</td><td>最大速度限制。值必须大于0。</td></tr><tr><td>命令</td><td>minimum_speed&lt;速度值&gt;</td></tr><tr><td>解释</td><td>最小速度限制。值必须大于0。</td></tr><tr><td>命令</td><td>velocity_pursuit_gain&lt;实数值&gt;</td></tr><tr><td>解释</td><td>应用于航向变化的比例因子,以使速度矢量指向领队的偏移点。当施加滚转率限制时,这是期望的横向加速度。值必须大于0。</td></tr></table>

# 编队飞行命令

<table><tr><td>命令</td><td>lead_aircraft&lt;名称值&gt;</td></tr><tr><td>解释</td><td>领队平台的名称。</td></tr><tr><td>命令</td><td>formation_rolls_with_lead</td></tr><tr><td>解释</td><td>编队与领队平台一起滚转。
默认值：编队在NED框架中保持平坦。</td></tr><tr><td>命令</td><td>offset_forward_from_lead&lt;长度值&gt;</td></tr><tr><td>解释</td><td>相对于领队平台的前向偏移。</td></tr><tr><td>命令</td><td>offset_right_from_lead&lt;长度值&gt;</td></tr><tr><td>解释</td><td>相对于领队平台的右侧偏移。</td></tr><tr><td>命令</td><td>offset_down_from_lead&lt;长度值&gt;</td></tr><tr><td>解释</td><td>相对于领队平台的下方偏移。</td></tr><tr><td>命令</td><td>initialize_at_offset</td></tr><tr><td>解释</td><td>跟随平台最初放置在相对于领队平台的提供偏移处，而不是初始位置（纬度、经度、</td></tr></table>

高度）。

# 3.6.4.5. 制导运动模型 WSF_GUIDED_MOVER

```txt
mover <name> WSF-guided mover
... base mover commands ...
integration timestep ...
integration_method ...
compute_all_forces_each_substep ...
coordinate_frame ...
maintain_inclination ...
show_status ...
show_trjectory ...
align Heading_with Velocity ...
check_forGround_impact ...
time_history_path ...
Stage Definition 1
    aero ...
    empty_mass ...
    fuel_mass ...
    total_mass ...
    thrust | sea_level_thrust | vacuum_thrust ...
    thrust_table | sea_level_thrust_table | vacuum_thrust_table ...
    reverse_thrust
    specific impulses | sea_levelspecific impulses | vacuumSpecific impulses ...
    nozzle_exit_area ...
    thrust_duration ...
    burn_rate ...
    burn_rate_table ...
    throttle ...
    thrust_vectoring_angle_limit ...
    thrust_vectoring_time_limit ...
    lateral_thrust_gain ...
    divert_thrust ...
    divert_fuel_mass ...
    divert_fuel_flow_rate ...
    divert_altitude_limits ...
    pre_ignition_coast_time ...
    pre_separation_coast_time ...
    integration_timestep ...
    ignition_failure(probability ...
    separation_failure(probability ...
    angle_of_attack ...
    bank_to_turn ... 
```

```txt
skid_to_turn ... end stage Stage Definition <n> ... end stage script void on_stage_ignition(int aStage) ... end_script script void on_stage_burnout(int aStage) ... end.script script void on_stage_separation(int aStage) ... end.script end mover 
```

WSF_GUIDED_MOVER 实现了一个能够代表制导滑翔炸弹或单级或多级制导导弹或火箭的移动器，具有中等程度的保真度。该模型具有以下特征：

使用三自由度（3-DOF）运动方程，将机体视为点质量。角速度和姿态不建模。平台的方向与速度矢量对齐，没有迎角或滚转。可以通过 angle_of_attack、bank_to_turn 和制导程序 ATTITUDE_PROGRAM 施加偏离，但它们不会影响性能。如果需要更高的保真度，则应考虑使用 WSF_P6DOF_MOVER，但它需要更多的数据和运行时间。  
不需要推进即可模拟滑翔炸弹类型的武器，但如果需要推进，可以为每个阶段提供推力、燃料质量和燃料消耗率。  
质量属性和推进输入都很灵活，任何省略的值如果可能将被计算。在多级 vehicle 上，下级将携带上级的总质量作为有效载荷。相互关联的值包括 thrust、burn_rate、thrust_duration、specific_impulse、fuel_mass、empty_mass、total_mass。如果所有值都已指定，但它们不一致，则在初始化期间会生成错误消息。  
使用空气动力学阻力和升力响应制导命令（参见 aero 类）。平台将在指定的空气动力学约束内转向拦截目标轨迹。如果由于最大升力系数不足或动态压力不足（在极端高度或低速飞行）导致空气动力学不足，模型将无法正确引导拦截。  
飞行轨迹将由必须存在于同一平台上的 WSF_GUIDANCE_COMPUTER 处理器确定。制导计算机将提供所需的横向和垂直力来引导移动器。  
WSF_GUIDED_MOVER 通常是由 WSF_EXPLICIT_WEAPON 实例发射的平台类型的一部分。平台类型通常还包括提供制导的 WSF_GUIDANCE_COMPUTER 和指示何时终止的WSF_WEAPON_FUSE。

# 阶段输入值的推导

可以指定哪些输入值以生成必要的内部值具有很大的灵活性。正确操作所需的内部值包括：

结构和燃料的初始质量。  
发动机启动和停止的时间以及发动机启动前或停止后和阶段分离前的任何滑行期。  
在每个时间步长中必须能够确定当前的推力和燃料消耗率。

移动器将尝试使用提供的任何输入值并推导出任何必要的内部值。例如，要推导出必要的质量值：

如果提供了 total_mass 和 fuel_mass，则可以推导出 empty_mass。  
如果提供了 total_mass、burn_rate 和 thrust_duration：

可以计算 fuel_mass 为 burn_rate * thrust_duration  
然后可以计算 empty_mass 为 total_mass - fuel_mass

如果提供了 total_mass、specific_impulse、thrust 和 thrust_duration：

可以使用比冲的定义计算 burn_rate（见下文）。  
然后可以计算 fuel_mass 为 burn_rate * thrust_duration  
然后可以计算 empty_mass 为 total_mass - fuel_mass

比冲的定义非常有用，因为它将推力、燃烧率和比冲联系起来：

$$
F _ {t h r u s t} = g _ {0} \cdot I _ {s p} \cdot \dot {m}
$$

其中：

$\mathrm { F _ { t h r u s t } }$ 是发动机的推力（牛顿）  
$g _ { 0 }$ 是地球表面的标准重力加速度（ $9 . 8 0 6 6 5 ~ \mathrm { m } / s ^ { 2 }$ ）  
$I _ { s p }$ 是比冲（秒）  
?  是质量流率（kg/s）

给定三个变量中的两个，可以确定第三个。

当 提 供 “ 参 考 ” 推 力 或 比 冲 值 时 （ 例 如 ： vacuum_thrust 、 sea_level_thrust 、vacuum_specific_impulse、sea_level_specific_impulse），情况会变得有些复杂。如果提供了任何参考值，则必须提供或可推导出所有值。以下推导规则按顺序应用：

如果提供了四个值中的三个，则可以轻松确定第四个。  
• 如果提供了 vacuum_thrust 和 sea_level_thrust 并且提供或可推导出 burn_rate且未提供 nozzle_exit_area，则可以使用比冲的定义确定 vacuum_specific_impulse 和sea_level_specific_impulse，并且可以推导出 nozzle_exit_area。  
• 如果提供了 vacuum_specific_impulse 和 sea_level_specific_impulse 并且提供或可推 导 出 burn_rate 且 未 提 供 nozzle_exit_area ， 则 可 以 使 用 比 冲 的 定 义 确 定vacuum_thrust 和 sea_level_thrust。  
• 如果仅提供了 vacuum_thrust 或 sea_level_thrust 并且提供了 nozzle_exit_area，则可以推导出另一个值。  
如果仅提供了 vacuum_specific_impulse 或 sea_level_specific_impulse 并且提供了nozzle_exit_area 并且提供或可推导出配对的推力值，则可以确定另一个值。

请注意，推导是递归应用的，直到无法进行进一步推导为止。建议使用 show_status 以确保推导值是适当的。

# 全局命令

<table><tr><td>命令</td><td>integration timestep &lt;时间值&gt;</td></tr><tr><td>解释</td><td>指定要使用的积分时间步长。如果指定值为零,则移动器不会将更新请求分解为更小的间隔。
此命令可以在阶段块内外指定。如果在块外指定,则它成为任何未指定值的阶段的默认值。
默认值:0.0秒</td></tr><tr><td>命令</td><td>integration_method [ rk2 | rk4 | trapezoidal ]</td></tr><tr><td>解释</td><td>选择用于积分运动方程的方法之一:
• rk2-二阶龙格-库塔法
• rk4-四阶龙格-库塔法
• trapezoidal-梯形法</td></tr><tr><td></td><td>警告:在AFSIM2.9之前的版本中,尚未完全实现此移动器的龙格-库塔方法。在每个积分子步长中,只有重力被重新计算。这意味着积分没有达到实际的龙格-库塔积分质量。在选择龙格-库塔方法时,请务必考虑选项compute_all_forces_each_substep。默认值:rk2</td></tr><tr><td>命令</td><td>compute_all_forces_each_substep&lt;布尔值&gt;</td></tr><tr><td>解释</td><td>指定龙格-库塔方法是否应在每个积分子步长中计算所有力。如果为false,则每个子步长中只计算重力,而空气动力和推力将从积分步长开始时的状态计算一次。当积分方法为梯形法时,此选项被忽略。此选项的默认值为false,这与AFSIM2.9之前版本中WSF.GuidED_MOVER的实现方式一致。注意:此选项的默认值为false,以避免扰动现有的模拟结果。任何新开发的场景应将此选项设置为true。未来,消除遗留的、不正确的龙格-库塔实现的路径将是将默认值更改为true。因此,在需要遗留行为的情况下,建议明确指示将此标志设置为false。默认值:false</td></tr><tr><td>命令</td><td>coordinate_frame[wcs|eci]</td></tr><tr><td>解释</td><td>指定积分运动方程的坐标系:wcs-世界坐标系eci-地心惯性坐标系注意:eci目前仅在建模轨道发射载具时使用,不应用于其他目的。使用ECI坐标创建的发射计算机特定于发射位置。默认值:wcs</td></tr><tr><td>命令</td><td>maintain_inclination&lt;布尔值&gt;</td></tr><tr><td>解释</td><td>当使用coordinate_frameeci建模轨道发射载具时,停车轨道的倾角是发射纬度和发射方位(或航向)的函数。对于非旋转球形地球,轨道的倾角由以下公式定义:cos(inclination)=cos(launch Latitude)·sim(launch Heading)但地球在旋转,这会给载具引入一个东向的ECI速度分量(在赤道发射时超过460m/s)。如果使用纯东向或西向以外的任何发射航向,则额外的东向速度将有一部分是横向于预定飞行路径的,并导致轨迹略微向赤道弯曲。在现实生活中,任务规划人员将调整初始条件和/或制导,以确保载具达到所需的轨道高度和倾角。如果此命令的值为true,则将忽略由于地球旋转引起的横向速度分量,轨迹不会向赤道弯曲。这使得创建需要特定轨道倾角的场景变得更容易,因为可以简单地使用上述公式根据发射纬度和所需倾角确定发射航向。默认值:false</td></tr><tr><td>命令</td><td>show_status</td></tr><tr><td>解释</td><td>在发生阶段操作时,将消息写入标准输出。如果启用了调试,则自动启用此选项。</td></tr><tr><td>命令</td><td>show_trjectory</td></tr><tr><td>解释</td><td>启用下行距离、速度、马赫数和施加的空气动力的打印输出到标准输出。</td></tr><tr><td>命令</td><td>align Heading_with Velocity&lt;布尔值&gt;</td></tr><tr><td>解释</td><td>如果为true,则使用所属平台的速度(如果非零)确定投影航向。否则,使用方向。默认值:false</td></tr><tr><td>命令</td><td>check_for-ground_impact</td></tr><tr><td>解释</td><td>启用内部地面撞击检查。这可以用于仅用于建模轨道发射载具或火箭的废弃阶段的移动器。以前必须在此类平台上定义WSFGROUND_TARGET Fuse实例,以检测它们是否撞击地面。如果未执行此操作,平台将继续运行并且永远不会被删除。</td></tr><tr><td>命令</td><td>time_history_path&lt;路径名&gt;</td></tr><tr><td>解释</td><td>如果指定,指示路径。</td></tr></table>

# 阶段定义

一个基于 WSF_GUIDED_MOVER 的移动器必须包含一个或多个阶段块。

```txt
stage <阶段编号>
    ... 阶段子命令 ...
end_stage
```