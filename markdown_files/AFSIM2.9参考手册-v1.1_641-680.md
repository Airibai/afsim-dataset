其中 <阶段编号> 必须是大于或等于 1 且小于或等于当前已定义阶段数加一的值。如果指定的阶段已经存在，则包含的子命令将覆盖该阶段的值。如果值等于当前已定义阶段数加一，则创建一个新阶段并填充包含的子命令。指定一个比当前最高定义阶段编号多一个以上的阶段编号是无效的。

以下是可能出现在阶段块中的子命令：

<table><tr><td>命令</td><td>aero &lt;空气动力学类型名称&gt;</td></tr><tr><td>解释</td><td>指定此阶段的空气动力学类型名称。类型必须在初始化时已知。aero-type-name 为none 意味着不会计算空气动力。这适用于在大气层外运行的阶段。默认值:必须提供。参见:4.12 空气动力学</td></tr><tr><td>命令</td><td>empty_mass &lt;质量值&gt;</td></tr><tr><td>解释</td><td>指定阶段没有燃料时的质量。默认值:0.0kg</td></tr><tr><td>命令</td><td>fuel_mass &lt;质量值&gt;</td></tr><tr><td>解释</td><td>指定阶段上的燃料质量。默认值:0.0kg</td></tr><tr><td>命令</td><td>total_mass &lt;质量值&gt;</td></tr><tr><td>解释</td><td>指定阶段的总质量,即 empty_mass 和 fuel_mass 的总和,但不包括此阶段上方任何上级阶段的质量(视为有效载荷)。默认值:0.0kg注意:为了向后兼容,可以通过关键字 launch_mass、mass、initial_mass 或 weight提供相同的值,但未来不保证支持这些关键字。</td></tr><tr><td>命令</td><td>thrust &lt;力值&gt;sea_level_thrust &lt;力值&gt;vacuum_thrust &lt;力值&gt;</td></tr><tr><td>解释</td><td>指定推进系统的推力。如果未提供此值,将尝试从其他提供或派生的输入值中推导。注意:如果指定了海平面或真空值,则可能还需要提供 nozzle_exit_area。参见上文的阶段输入值推导。</td></tr><tr><td>命令</td><td>thrust_table ... end_thrust_tablesea_level_thrust_table ... end_sea_level_thrust_tablevacuum_thrust_table ... end_vacuum_thrust_table</td></tr><tr><td>解释</td><td>定义推力随时间的函数。thrust_table&lt;时间-1&gt;&lt;推力-1&gt;...&lt;时间-n&gt;&lt;推力-n&gt;end_thrust_table注意:时间值必须单调递增,并且必须至少有两个时间/推力条目。注意:如果单独指定了海平面或真空推力表,则必须提供 nozzle_exit_area。参见上文的阶段输入值推导。</td></tr><tr><td>命令</td><td>reverse_thrust</td></tr><tr><td>解释</td><td>表示推力应施加在相反方向(即,作为制动力而不是推进力)。</td></tr><tr><td>命令</td><td>specific_impulse &lt;时间值&gt;sea_levelSpecific_impulse &lt;时间值&gt;vacuum Specific impulse &lt;时间值&gt;</td></tr><tr><td>解释</td><td>指定推进系统在特定条件下的比冲。如果未提供此值,将尝试从其他提供或派生的输入值中推导。注意:如果指定了海平面或真空值,则可能还需要提供 nozzle_exit_area。参见上文的阶段输入值推导。</td></tr><tr><td></td><td>注意:如果以N-sec/kg为单位给出比冲,则必须除以9.80665m/sec2以获得秒为单位的值。</td></tr><tr><td>命令</td><td>nozzle_exit_area&lt;面积值&gt;</td></tr><tr><td>解释</td><td>指定发动机喷嘴的出口面积。这用于将海平面或真空参考推力或比冲值从参考值调整到当前操作高度的值。默认值:无-当使用真空推力表或海平面推力表时始终需要。当使用海平面或真空参考推力或比冲值时可能需要。参见上文的阶段输入值推导。</td></tr><tr><td>命令</td><td>thrust_duration&lt;时间值&gt;</td></tr><tr><td>解释</td><td>指定发动机将产生指定推力的时间量。如果未提供此值,将尝试从其他提供或派生的输入值中推导。·燃烧率表中的最后一个时间值(如果提供)。·推力表、海平面推力表或真空推力表中的最后一个时间值(如果提供)。·从其他可用值计算。注意:根据提供的输入值,实际推力时间可能与此值不同。发动机将继续燃烧,直到燃料用完或被制导计算机终止。</td></tr><tr><td>命令</td><td>burn_rate&lt;质量流率值&gt;</td></tr><tr><td>解释</td><td>指定推力时的推进剂燃烧率。如果未提供此值,将尝试从其他提供或派生的输入值中推导。</td></tr><tr><td>命令</td><td>burn_rate_table...end_burn_rate_table</td></tr><tr><td>解释</td><td>定义推进剂燃烧率随时间的函数。burn_rate_table&lt;时间-1&gt;&lt;燃烧率-1&gt;··&lt;时间-n&gt;&lt;燃烧率-n&gt;end_burn_rate_table注意:时间值必须单调递增,并且必须至少有两个时间/燃烧率条目。</td></tr><tr><td>命令</td><td>throttle&lt;表值&gt;</td></tr><tr><td>解释</td><td>·这提供了一个函数来调整当前推力和燃烧率(调整仅是乘法)。从属值是非维数节流因子,大于或等于零。值为零对应于无推力,值为一对应于全推力。当基本推力和燃烧率值小于最大值时,允许大于一的值。·允许的自变量(及其单位)包括:·time(&lt;时间单位&gt;):发动机点火后的时间。·altitude(&lt;长度单位&gt;):平台的高度。·speed(&lt;速度单位&gt;):平台的速度。·mach(无单位):以马赫数表示的平台速度。</td></tr><tr><td>命令</td><td>thrust_vectoring_angle_limit&lt;角度值&gt;</td></tr><tr><td>解释</td><td>指定推力矢量可以转向的最大角度。默认值:0度(不允许推力矢量控制)。</td></tr><tr><td>命令</td><td>thrust_vectoring_time Limits&lt;时间值&gt;&lt;时间值&gt;</td></tr><tr><td>解释</td><td>指定推力矢量控制可以使用的最小和最大时间(相对于当前阶段的点火时间)。默认值:无限制。推力矢量控制可以在发动机产生推力时随时使用。</td></tr><tr><td>命令</td><td>lateral_thrust_gain&lt;实数值&gt;</td></tr><tr><td>解释</td><td>通过矢量控制发动机的推力或使用推进器可以施加横向力。这些力通常具有较大的力臂(发动机位于火箭的末端,距离重心有一定距离),因此,引入一个旋转,从而导致速度矢量方向的变化。问题在于该模型将机体视为点质量(参见概述),不考虑角速度-它通过“推”质量来改变方向。改变方向所需的力比旋转所需的力要大。因此,需要更高的矢量角,从而从轴向推力中偷取更多推力。这是一个尝试补偿差异的修正因子。除了在创建在极限性能下运行的轨道发射载具以将大质量物体送入轨道时,通常不重要。如果需要,5或10的值并不不合理。不要害怕设置更高的值。默认值:1</td></tr><tr><td>命令</td><td>divert_thrust&lt;力值&gt;</td></tr><tr><td>解释</td><td>指定从推进器可用的推力量。“divert”能力是实际推进器的简单实现。最初提供是为了使vehicle在高空可用的空气动力小或不存在时仍能机动。</td></tr><tr><td></td><td>在任何给定时间,制导计算机(WSF GUIDANCECOMPUTER)确定实现当前目标(拦截、转向航向、爬升高度等)所需的加速度。WSF GUIDED MOVER将尝试按以下顺序满足所请求的加速度:1)利用推力矢量控制尽可能满足请求。推力矢量控制在定义 thrust_vectoring_angle_limit时可用。2)利用可用的空气动力尽可能满足剩余请求。3)利用偏转推力尽可能满足剩余请求。偏转推力在以下所有条件成立时可用:·divert thrust大于零。·当前偏转燃料质量(初始值为divert_fuel_mass)大于零。·当前高度在divert_altitude_limits指定的范围内。任何前述步骤中未满足的请求部分将不被满足。注意:这是一种简单实现。实际推进器通常在很短的时间内全推力运行。由于WSF GUIDED MOVER的简单性质(3-DOF、点质量、简化空气动力学),真正的推进器模型是不合理的。如果请求的加速度不需要全推力,则使用的推力和燃料流量将减少。实际模型通常在较短时间内启动推进器。默认值:0牛顿(不提供偏转推力)。注意:如果divert thrust大于零,则divert_fuel_mass和divert_fuel_flow_rate必须均大于零。注意:divert thrust不应在WSF GUIDED MOVER中指定,该移动器是由weapon.tools用于生成WSF BALLISTIC_MISSLE_LAUNCH Computer数据的武器场景的一部分,但可以在由任务或Warlock执行的相同武器场景中使用。</td></tr><tr><td>命令</td><td>divert_fuel_mass&lt;质量值&gt;</td></tr><tr><td>解释</td><td>指定初始可用的偏转燃料质量。当使用divert thrust时,它将消耗偏转燃料,直到不再可用为止。注意:divert_fuel_mass不被视为vehicle质量的一部分(即:其质量不影响运动方程)。divert_fuel_mass和divert_fuel_flow_rate仅用于限制偏转可以使用的时间长度。这里的假设是推进器及其质量相对于vehicle的其余部分很小。默认值:0千克(如果divert thrust大于零,则必须指定一个大于零的值)。注意:divert_fuel_mass不应在WSF GUIDED MOVER中指定,该移动器是由weapon.tools用于生成WSF BALLISTIC_MISSLE_LAUNCH Computer数据的武器场景的一部分,但可以在由任务或Warlock执行的相同武器场景中使用。</td></tr><tr><td>命令</td><td>divert_fuel_flow_rate&lt;质量流率值&gt;</td></tr><tr><td>解释</td><td>指定使用全偏转推力时的偏转燃料消耗率。如果仅需要部分偏转推力以满足当前请求,则燃料流速将按比例减少。注意:指定较小的值将使偏转可用的时间更长。默认值:0千克/秒(如果divert thrust大于零,则必须指定一个大于零的值)。注意:divert_fuel_flow_rate不应在WSF GUIDED MOVER中指定,该移动器是由weapon.tools用于生成WSF BALLISTIC_MISSLE_LAUNCH Computer数据的武器场景的一部分,但可以在由任务或Warlock执行的相同武器场景中使用。</td></tr><tr><td>命令</td><td>divert_altitude_limits&lt;长度值&gt;&lt;长度值&gt;</td></tr><tr><td>解释</td><td>指定使用偏转推力的最低和最高高度。默认值:无限制(在所有高度都可用)。注意:divert_altitude_limits不应在WSF GUIDED MOVER中指定,该移动器是由weapon.tools用于生成WSF BALLISTIC_MISSLE_LAUNCH Computer数据的武器场景的一部分,但可以在由任务或Warlock执行的相同武器场景中使用。</td></tr></table>

其他命令

<table><tr><td>命令</td><td>pre_ignition_coast_time &lt;时间值&gt;</td></tr><tr><td>解释</td><td>指定从阶段开始到发动机点火之间经过的时间量。默认值:0.0秒注意:如果为第一阶段指定此值,则表示平台仍处于“发射台”或“导轨”上的时 间。武器平台将保持连接到发射平台,直到此时间过期。</td></tr><tr><td>命令</td><td>pre_separation_coast_time &lt;时间值&gt;</td></tr><tr><td>解释</td><td>指定从该阶段燃烧结束到与载具分离之间经过的时间量。此命令对单级载具或多级 载具的最后一级无效。默认值:0.0秒</td></tr><tr><td>命令</td><td>integration timestep &lt;时间值&gt;</td></tr><tr><td>解释</td><td>指定此阶段的积分时间步长。默认值:全局 integration timestep 的值(在阶段定义之外)。</td></tr><tr><td>命令</td><td>ignition_failure(probability &lt;实数值&gt;</td></tr><tr><td>解释</td><td>指定此阶段发动机点火失败的概率,范围为[0..1]。如果点火失败,结果如下: 将移动器标记为“损坏”。这将触发 MOVER BROKEN 模拟事件。 位置将继续更新,但仅受重力和空气动力的影响(即:没有推进力)。 默认值:0.0</td></tr><tr><td>命令</td><td>separation_failure(probability &lt;实数值&gt;</td></tr><tr><td>解释</td><td>指定此阶段无法与后续阶段分离的概率,范围为[0..1]。如果分离失败,结果如下: 将移动器标记为“损坏”。这将触发 MOVER BROKEN 模拟事件。 位置将继续更新,但仅受重力和空气动力的影响(即:没有推进力)。 默认值:0.0</td></tr><tr><td>命令</td><td>angle_of_attack &lt;表值&gt;</td></tr><tr><td>解释</td><td>默认情况下,模型简单地将平台与速度矢量对齐,没有迎角。此表提供了指定迎角 的函数。依赖值是迎角,单位为&lt;角度单位&gt;。允许的自变量(及其单位)包括: time(&lt;时间单位&gt;):发动机点火后的时间。 altitude(&lt;长度单位&gt;):平台的高度。 speed(&lt;速度单位&gt;):平台的速度。 mach(无单位):以马赫数表示的平台速度。 默认值:无迎角注意:这不会影响 vehicle 的性能。它只是更新姿态,以便其他平台上的传感器获得 更准确的方面进行签名查找,并使视觉表现更逼真。注意:此值优先于由制导程序 ATTITUDE PROGRAM 引起的任何非零俯仰角。(如果命令的角度为零,则使用此值)。</td></tr><tr><td>命令</td><td>bank_to_turn skid_to_turn</td></tr><tr><td>解释</td><td>默认情况下,模型简单地将 vehicle 与速度矢量对齐,没有滚转。“bank_to_turn” 表 示应施加滚转角。此角度与施加的侧向空气动力成正比。 默认值:skid_to_turn注意:这不会影响 vehicle 的性能。它只是更新姿态,以便其他平台上的传感器获得 更准确的方面进行签名查找,并使视觉表现更逼真。注意:此值优先于由制导程序 ATTITUDE PROGRAM 引起的任何非零滚转角。如果命令的角度为零,则使用此值。</td></tr></table>

# 脚本接口

WSF_GUIDED_MOVER 移动器将在阶段生命周期的某些关键事件期间调用平台（而不是移动器）上定义的以下脚本方法。这些脚本可用于显示信息数据、更改签名等。

<table><tr><td>脚本</td><td>script void on stage ignition(int aStage) ... end script</td></tr><tr><td>功能</td><td>处理阶段 aStage 的点火事件。</td></tr><tr><td>脚本</td><td>script void on stage burnout(int aStage) ... end script</td></tr><tr><td>功能</td><td>处理阶段 aStage 的燃烧结束事件。</td></tr><tr><td>脚本</td><td>script void on stage separation(int aStage) ... end script</td></tr><tr><td>功能</td><td>处理阶段 aStage 的分离事件。</td></tr></table>

```txt
mover <name> WSF_OLD.GuidED_MOVER  
mover Commands ...  
show_status  
show_trjectory  
disable-guidance  
integration_method ...  
integration timestep ...  
stage 1  
    aero ...  
    empty_mass ...  
    fuel_mass ...  
    total_mass ...  
    pre_ignition_coast_time ...  
    pre_separation_coast_time ...  
    thrust ...  
    thrust_duration ...  
    burn_rate ...  
    specific_impulse ...  
    thrust_vectoring_angle_limit ...  
    thrust_vectoring_time_limit ...  
end_stage  
stage <n>  
    ... stage commands ...  
end_stage  
end_mover 
```

注：过时的运动模型，避免使用在新的工作中。

概述

WSF_OLD_GUIDED_MOVER 实现了一个能够代表制导滑翔炸弹或单级或多级制导导弹的移动器。该模型具有以下特征：

推进: 对于滑翔炸弹类型的武器，推进不是必需的，但如果需要推进，则每个阶段的推力、燃烧速率和比冲（Isp）在燃烧时间内假定为恒定。

质量属性和推进输入: 这些都是灵活的，任何遗漏的值将在可能的情况下计算。在多级载具中，较低的阶段将携带每个上阶段的总质量作为有效载荷。相互关联的值包括推力、燃烧速率、推力持续时间、比冲、燃料质量、空重和总质量。如果所有值都已指定，但它们的总和不一致，则在初始化期间会生成错误消息。

空气动力学: 模型化了空气动力学阻力和升力。导弹将在指定的空气动力学约束内进行空气动力学转向以拦截目标轨迹。如果由于最大升力系数不足或动态压力不足（在极端高度或低速飞行）而导致空气动力学不足，模型将无法正确引导拦截。

导 引 计 算 机 : 飞 行 的 导 引 轨 迹 将 由 必 须 存 在 于 同 一 平 台 上 的

WSF_OLD_GUIDANCE_COMPUTER 处理器确定。导引计算机将提供所需的横向和垂直力来引导移动器。

典型配置: WSF_OLD_GUIDED_MOVER 通常是由 WSF_EXPLICIT_WEAPON 实例发射的平台类型的一部分。平台类型通常还包括一个 WSF_WEAPON_FUSE 来指示何时终止。

# 详细过程描述

WSF_OLD_GUIDANCE_COMPUTER 提供所需的俯仰和偏航力，以实现与目标轨迹的拦截引导。所需的力提供给空气动力学对象，该对象可能会根据当前的动态压力和指定的最大升力系数进行干预以减少横向力。此外，计算阻力值以阻碍前进运动。横向和纵向力的矢量和以牛顿方式作用于平台，导致加速度矢量，该矢量被积分一次以获得速度，再次积分以进行位置更新。

# 命令

show_status: 启用调试打印输出，指示何时发生分级操作。如果调试也启用，则自动启用。  
show_trajectory: 启用有关质量变化和轨迹数据点的调试打印输出。此选项提供下游距离、速度、马赫数和施加的空气动力学力。  
disable_guidance: 禁用任何空气动力学升力（横向或垂直力）的生成。将制导武器变成“哑弹”弹道武器。此选项是 WSF_UNGUIDED_MOVER 的默认设置。  
integration_method [ rk2 | rk4 | trapezoidal ]: 指定用于积分运动方程的方法。

默认值: rk2

integration_timestep <time-value>: 指定用于积分运动方程的全局时间步长。此值用于未指定局部积分时间步长的任何阶段。

默认值: 必须指定。

stage <stage-number>: 定义单级载具的唯一阶段或多级载具中的一个阶段的属性。<stagenumber> 必须是大于或等于 1 且小于或等于当前定义阶段数加一的值。如果该值指定了一个已经存在的阶段，则封闭的子命令将覆盖该阶段中的值。如果该值等于当前定义阶段数加一，则创建一个新阶段并用封闭的子命令填充。指定比当前最高定义阶段数多一个以上的阶段号是无效的。

▫ aero<aero-type-name>: 指定此阶段的空气动力学类型名称。类型必须在初始化时已知。  
□ empty_mass <mass-value>: 指定没有燃料的阶段质量。  
□ fuel_mass <mass-value>: 指定阶段上的燃料质量。  
□ total_mass<mass-value>: 指定阶段的总质量，即空重和燃料质量的总和，但不包括此阶段上方任何上阶段的质量（视为有效载荷）。注意：为了向后兼容，可以通过关键字“launch_mass”、“mass”、“initial_mass”或“weight”提供相同的值，但不保证将来支持这些关键字。

默认值: 如果未提供此值，将从提供的燃料质量和空重中计算。如果未提供燃料质量或空重，则必须提供此值。

□ pre_ignition_coast_time <time-value>: 指定从阶段开始到发动机点火之间将经过的时间。

默认值: 0.0 秒

pre_separation_coast_time <time-value>: 指定从此阶段燃烧结束到其与载具分离之

间将经过的时间。此命令对单级载具或多级载具的最后一个阶段没有影响。

默认值: 0.0 秒

▫ thrust <force-value>: 指定推进系统的推力。  
□ thrust_duration <time-value>: 指定发动机将产生指定推力的时间。  
□ burn_rate <mass-flow-value>: 指定推力时的推进剂燃烧速率。  
▫ specific_impulse <time-value>: 推进系统的比冲。  
□ thrust_vectoring_angle_limit <angle-value>: 指定推力在推力矢量时间限制期间偏离纵轴的角度，以引入俯仰机动。

默认值:0- 无推力矢量。

▫ thrust_vectoring_time_limits <time-value min-time-value> <time-valuemax-time-value>: 指定阶段点火后可以使用推力矢量的时间窗口。仅当推力矢量角度限制大于零时适用。

默认值: 0 秒 <inf> 秒

end_stage

# 脚本接口

以下脚本方法可以在平台上定义（而不是在移动器块中）：

▫ void on_stage_ignition(int aStage): 在阶段点火期间调用。  
□ void on_stage_burnout(int aStage): 在阶段燃烧结束期间调用。  
□ void on_stage_separation(int aStage): 在阶段分离期间调用。

这些脚本在阶段的点火、燃烧结束和分离期间分别被调用。‘aStage’ 的值将是阶段号，从 1 开始。

这些方法的一个用途是改变签名状态以反映载具签名的变化，或使用其他脚本方法更改平台的视觉效果。

# 3.6.4.7. 简单抛物线弹道运动模型 WSF_PARABOLIC_MOVER

```txt
mover WSF_PARABOLIC_MOVER Platform Part Commands .. //Mover Commands update_interval ... update_time_tolerance .. //Parabolic Mover Commandstof_and_impact_lat_lon_alt... tof_and_impact_lat_lon...   
end_mover 
```

WSF_PARABOLIC_MOVER 类近似模拟弹道轨迹。它可以通过三种不同的方式使用：

从指定的初始条件飞行简单的抛物线轨迹（垂直路径仅受恒定向下的重力加速度影响）。  
指定最终条件以及到达那里的时间，并将以恒定加速度运动到达最终的预期撞击点。  
如果没有以其他方式设置，它将查询其平台的当前目标（如果存在），并尝试根据其初始条件飞行到那里。

注意：此移动器不会自行终止运动；地形撞击必须单独确定，因此计算的最终条件（纬度、经度、高度）仅为预期值。实际轨迹可能会提前终止，或飞过预期点并继续前进。

# 移动器公共命令

<table><tr><td>命令</td><td>update_interval &lt;time-reference&gt;</td></tr><tr><td>解释</td><td>如果非零，指定模拟将调用Mover的周期时间间隔。如果为零，则仅在需要确定包含平台的位置时调用Mover。默认值：0秒，除非特定Mover实现覆盖。</td></tr><tr><td>命令</td><td>update_time_tolerance &lt;time-reference&gt;</td></tr><tr><td>解释</td><td>当模拟请求位置更新时，如果自上次更新以来的时间小于或等于此值，则Mover将忽略更新。默认值：大多数Mover实现将其定义为以某个适当的名义速度行驶1米所需的时间。注意：Mover实现可能会选择忽略此命令。</td></tr></table>

# 抛物线移动器命令

<table><tr><td>命令</td><td>tof_and_impact_lat_lon_alt&lt;时间值&gt;&lt;纬度值&gt;&lt;经度值&gt;&lt;高度值&gt;</td></tr><tr><td>解释</td><td>指定预期的最终条件:飞行时间和撞击的纬度、经度和高度。</td></tr><tr><td>命令</td><td>tof_and_impact_lat_lon&lt;时间值&gt;&lt;纬度值&gt;&lt;经度值&gt;</td></tr><tr><td>解释</td><td>指定预期的最终条件:飞行时间和撞击的纬度、经度。高度通过查找给定纬度和经度的地形高度来确定。</td></tr></table>

# 3.6.4.8. 简单直线运动模型 WSF_STRAIGHT_LINE_MOVER

```batch
mover WSF_STRAIGHT_LINE_MOVER Platform Part Commands .. //Mover Commands update_interval ... update_time_tolerance .. // Straight Line Mover Commands average_speed ... tof_and_speed ... maximum_lateral acceleraion ... guidance_mode ... guide_totruth ...   
end_mover 
```

WSF_STRAIGHT_LINE_MOVER 实现了一个用于 WSF_EXPLICIT_WEAPON 的移动器，该移动器从发射点沿（或多或少）直线飞行以拦截目标轨迹。用户无需指定武器的质量属性、推进或空气动力学表，但会因此损失一定的保真度。目标轨迹必须由某种 WsfSensor 或WsfProcessor 类型提供，这些类型通过其 WsfTrackManager 填充 WsfPlatform 上的当前目标。该移动器将实现恒定的平均速度，或根据飞行时间线性插值的速度表。用户还可以选择指定最大横向过载限制，以限制任何初始或最终机动加速度的大小。

注意：如果目标命中或未命中，或进行致命性判定时，不会终止飞行。发射的WSF_EXPLICIT_WEAPON 通常会提供要使用的武器效果，并且类型为 WSF_WEAPON_FUSE（或从其派生）的处理器通常会终止飞行并调用武器效果。

# 移动器公共命令

<table><tr><td>命令</td><td>update_interval &lt;time-reference&gt;</td></tr><tr><td>解释</td><td>如果非零，指定模拟将调用Mover的周期时间间隔。如果为零，则仅在需要确定包含平台的位置时调用Mover。默认值：0秒，除非特定Mover实现覆盖。</td></tr><tr><td>命令</td><td>update_time_tolerance &lt;time-reference&gt;</td></tr><tr><td>解释</td><td>当模拟请求位置更新时，如果自上次更新以来的时间小于或等于此值，则Mover将忽略更新。默认值：大多数Mover实现将其定义为以某个适当的名义速度行驶1米所需的时间。注意：Mover实现可能会选择忽略此命令。</td></tr></table>

# 直线移动器命令

<table><tr><td>命令</td><td>average_speed &lt;速度值&gt;</td></tr><tr><td>解释</td><td>指定武器在飞行期间使用的平均速度。</td></tr><tr><td>命令</td><td>tof_and_speed ... end_to_and_speed</td></tr><tr><td rowspan="2">解释</td><td>指定武器的速度与时间的关系。时间值必须按数值递增顺序排列。</td></tr><tr><td>tof_and_speed
0.0 sec 1500 kts
10.0 sec 1200 kts
20.0 sec 1000 kts
end_to_and_speed</td></tr><tr><td>命令</td><td>maximum_lateral acceleration &lt;加速度值&gt;</td></tr><tr><td>解释</td><td>指定武器机动时使用的最大横向加速度。</td></tr><tr><td>命令</td><td>guidance_mode [ lead_pursuit | pure_pursuit ]</td></tr><tr><td>解释</td><td>指定武器的制导模式。使用 lead_pursuit 时,速度矢量将始终指向当前目标轨迹(如果静止),如果轨迹在移动,将根据需要进行外推以预测拦截时间,模拟比例导航制导。使用 pure_pursuit 时,速度矢量将始终指向当前目标轨迹。默认值: pure_pursuit</td></tr><tr><td>命令</td><td>guide_totruth &lt;布尔值&gt;</td></tr><tr><td>解释</td><td>指定在制导计算中是否使用感知的目标位置(由当前目标轨迹定义)或真实目标位置。默认值: false</td></tr></table>

# 3.6.4.9. 多级弹道导弹运动模型 WSF_TBM_MOVER

```tcl
mover <name> WSF_TBM_MOVER
... base mover commands ...
trajectory_type [lofted | depressed]
target_position <latitude-value><longitude-value>
ignore_target
show_status 
```

```txt
stage <stage-number>
    ballistic_coefficient <force/area value>
end stage
empty_mass <mass-value>
fuel_mass <mass-value>
fuel_mass_fraction <fraction>
pre_ignition_coast_time <time-value>
pre_separation_coast_time <time-value>
specific_impulse <time-value>
total_mass <mass-value>
 thrust <force-value>
 thrust_duration <time-value>
 cep <distance value>
 cep_table
    range <distance value> cep <distance value>
    range <distance value> range_error <distance value> azimuth_error <angle value>
 end_cep_table
 end mover 
```

WSF_TBM_MOVER 实现了一个能够以简化格式表示单级或多级战术弹道导弹的移动实体。使用 WSF_TBM_MOVER 时，弹道轨迹往往会达到极高的高度，因为燃料会完全燃烧。注意 如果需要更高精度的弹道导弹（例如在弹道导弹拦截的情况下），强烈推荐使用WSF_GUIDED_MOVER。 TBM 移动实体具有以下特征：

标准的“火箭方程”使用四阶龙格-库塔方法积分。  
推力在燃烧时间内假设为恒定。  
燃料消耗在燃烧时间内假设为恒定。  
大气阻力在高度低于200,000米时使用指数模型进行建模。更高高度则不考虑阻力。  
除推力和重力外，没有其他力的考虑。因此，轨迹完全由初始条件和阶段定义决定。

在计算轨迹时，移动实体会计算与目标关联的期望地面距离。然后，它会生成一个发射角度，使计算的地面距离在目标的 10 米以内。在少数情况下，内部算法可能缺乏满足这一条件的精度，因此轨迹将表示为“最佳尝试”。

导弹会立即调整到所需的轨迹。

TBM 移动实体通常是由 WSF_EXPLICIT_WEAPON 实例发射的平台类型的一部分。平台类型通常还包括一个 WSF_WEAPON_FUSE，以指示何时终止。移动实体将通过以下两种方法之一建立附加平台的初始状态：

1) 您可以使用 target_position 命令或由 WSF_EXPLICIT_WEAPON 定义的“当前目标轨迹”来指定目标位置。移动实体将确定一个初始状态，以使其撞击目标位置，除非提供了固定的圆概率误差（CEP）或 CEP 表。如果使用 CEP 选项，指定的目标位置将偏移到一个新的终端撞击位置，以引入偏差距离。  
2) 您可以设置 WSF_EXPLICIT_WEAPON 的方位（偏航和俯仰）。移动实体将不进行任何轨迹的预计算。如果您处理的是固定的发射和目标位置，您可以在启用

show_status 的情况下运行一次，然后使用输出设置偏航和俯仰值，并使用ignore_target 以防止重新计算初始条件。

<table><tr><td>命令</td><td colspan="2">trajectory_type [lofted | depressed]</td></tr><tr><td>解释</td><td colspan="2">指定用于到达目标的轨迹类型。如果未指定目标,则不使用此命令。默认值: lofted</td></tr><tr><td>命令</td><td colspan="2">target_position &lt;纬度值&gt;&lt;经度值&gt;</td></tr><tr><td>解释</td><td colspan="2">指定目标的位置。如果使用了ignore_target,则不使用此命令。如果使用了cep或cep_table,可能会偏离目标。默认值:如果未指定,则目标位置由武器发射过程传递的“当前目标轨迹”定义。</td></tr><tr><td>命令</td><td colspan="2">ignore_target</td></tr><tr><td>解释</td><td colspan="2">表示忽略任何目标位置(无论是由target_position 定义还是由“当前目标轨迹”定义)。平台的方位定义了初始状态。</td></tr><tr><td>命令</td><td colspan="2">show_status</td></tr><tr><td>解释</td><td colspan="2">在发射时显示状态信息。</td></tr><tr><td>命令</td><td colspan="2">stage &lt;阶段编号&gt;... end stage</td></tr><tr><td rowspan="3">解释</td><td colspan="2">定义单级 vehicle 的唯一状态或多级 vehicle 的某个阶段的属性。&lt;阶段编号&gt;必须是大于或等于1且小于或等于当前定义阶段数加一的值。如果该值指定了一个已存在的阶段,则包含的子命令将覆盖该阶段中的值。如果该值等于当前定义阶段数加一,则创建一个新阶段并用包含的子命令填充。指定一个比当前最高定义阶段编号高出一个以上的阶段编号是无效的。</td></tr><tr><td colspan="2">stage &lt;阶段编号&gt; ... 阶段子命令 ... end stage</td></tr><tr><td colspan="2">子命令: ballistic_coefficient &lt;力/面积值&gt;弹道系数。这是一个必需值,没有默认值。</td></tr><tr><td>命令</td><td colspan="2">empty_mass &lt;质量值&gt;</td></tr><tr><td>解释</td><td colspan="2">指定没有燃料时阶段的质量。默认值:如果未提供,则此值将从total_mass 和 fuel_mass 或 fuel_mass_fraction计算得出。</td></tr><tr><td>命令</td><td colspan="2">fuel_mass &lt;质量值&gt;</td></tr><tr><td>解释</td><td colspan="2">指定阶段上的燃料质量。如果指定了非零的 thrust_duration,则必须指定此值或fuel_mass_fraction。</td></tr><tr><td>命令</td><td colspan="2">fuel_mass_fraction &lt;比例&gt;</td></tr><tr><td>解释</td><td colspan="2">指定阶段总质量中燃料的比例(0.0到1.0)。如果指定了非零的 thrust_duration,则必须指定此值或 fuel_mass。</td></tr><tr><td>命令</td><td colspan="2">pre_ignition_coast_time &lt;时间值&gt;</td></tr><tr><td>解释</td><td colspan="2">指定从阶段开始到发动机点火之间的时间。默认值:0.0秒</td></tr><tr><td>命令</td><td colspan="2">pre_separation_coast_time &lt;时间值&gt;</td></tr><tr><td>解释</td><td colspan="2">指定从该阶段燃烧结束到与多级分离之间的时间。对于单级 vehicle 或多级 vehicle的最后一个阶段,此命令无效。默认值:0.0秒</td></tr><tr><td>命令</td><td colspan="2">specific_impulse &lt;时间值&gt;</td></tr><tr><td>解释</td><td colspan="2">指定发动机推力的另一种机制。如果指定了非零的 thrust_duration,则必须指定此值或 thrust。</td></tr><tr><td>命令</td><td colspan="2">total_mass &lt;质量值&gt;</td></tr><tr><td>解释</td><td colspan="2">指定阶段的总质量。</td></tr><tr><td></td><td colspan="2">默认值:如果未提供,则此值将从 fuel_mass 和 empty_mass 计算得出(如果它们已提供)。如果未提供 fuel_mass 或 empty_mass,则必须提供此值。</td></tr><tr><td>命令</td><td colspan="2">thrust&lt;力值&gt;</td></tr><tr><td>解释</td><td colspan="2">指定发动机的推力。如果指定了非零的 thrust_duration,则必须指定此值或 specific_impulse。</td></tr><tr><td>命令</td><td colspan="2">thrust_duration&lt;时间值&gt;</td></tr><tr><td>解释</td><td colspan="2">指定发动机燃烧的时间。</td></tr><tr><td>命令</td><td colspan="2">cep&lt;距离值&gt;</td></tr><tr><td>解释</td><td colspan="2">指定导弹在引导到目标时的误差。这是一个50百分位统计预期的从目标瞄准点的径向水平偏差。如果未指定 cep距离或 cep_table,则导弹将击中上面指定的 target_position。使用cep或cep_table是互斥的。</td></tr><tr><td>命令</td><td colspan="2">cep_table...end_cep_table</td></tr><tr><td>解释</td><td colspan="2">cep_table...cep_table子命令... end_cep_table</td></tr><tr><td></td><td>CEP = Fixed Value (Independent of Range) CEP Target Lat/Long Missile Downrange Direction Option 1: Fixed CEP</td><td>CEP = f (Range) CEP Precision = f (Range) Range &amp; Azimuth Precision = f (Range) Range Error Azimuth Error Range Error Azimuth error is measured from intended target bearing (usually less than 1 deg)</td></tr><tr><td></td><td>Option 1: CEPTable</td><td>Option 2: CEPTable</td></tr><tr><td></td><td colspan="2">NOTES: 1) CEP = Circular Error Probability 2) Shaded Regions are 50% Probability of Impact</td></tr><tr><td colspan="3">定义一个50百分位统计误差表,以量化导弹在击中预定目标时的误差。(此选项与固定的cep关键字互斥。)误差可以通过以下两种方式之一指定:圆概率误差(CEP)或距离和方位误差。在任何一种情况下,这些值都是依赖于表查找中的名义地面目标距离的独立变量。每个导弹只允许一个表,并且定义一个表的派生对象将覆盖其父定义。对于以下两种指定精度的方法,量化的误差是针对给定的名义目标距离。必须至少给出两个这样的距离以启用线性插值。每个名义距离一行输入,并且每个后续的距离值必须大于前一个。</td></tr><tr><td colspan="3">cep_table子命令 range&lt;距离值&gt;cep&lt;距离值&gt; 在给定的名义目标距离处预期的径向水平撞击误差。(与下面的 [range, range_error, azimuth_error]三元组互斥。)必须指定至少两个距离。</td></tr><tr><td colspan="3">range&lt;距离值&gt; range_error&lt;距离值&gt; azimuth_error&lt;角度值&gt; 在给定的名义目标距离处预期的距离和方位撞击误差。(与上面的 [range, cep]对互斥。)必须指定至少两个距离。</td></tr></table>

# 脚本接口

以下脚本方法可以在平台上定义（而不是在移动实体块中）：

```txt
void on stage ignition(int aStage)  
void on stage burnout(int aStage)  
void on stage separation(int aStage) 
```

这些脚本分别在阶段点火、燃烧结束和分离时调用。aStage 的值将是阶段编号，从 1开始。

这些方法的一个用途是改变签名状态，以反映飞行器签名的变化，或者使用其他脚本方法来改变平台的视觉效果。

# 3.6.4.10.牵引运动模型 WSF_TOWED_MOVER

```verilog
mover WSF_TOWED_MOVER Platform Part Commands .. //Mover Commands update_interval ... // Towed Mover Commandstow_length ... reel_out_speed ... reel_in_speed ... reel_in_at absolute_time ... reel_in_time_afterdeployed ... restorequantity... follow_lead_trjectory... azimuth:relative_to_lead... elevationrelative_to_lead...   
end_mover 
```

WSF_TOWED_MOVER 实现了一个由前导平台牵引的移动实体。只要被部署，牵引平台就会跟随前导平台的路径。WsfTowedMover 的脚本示例如下所示。

# 特殊考虑事项

被牵引的资产平台必须定义为 WSF_TOWED_ASSET 类型的移动实体。  
被牵引的资产被视为 WSF_EXPLICIT_WEAPON 类型，必须“发射”才能添加到仿真环境中。  
前导平台必须包含一个包含被牵引资产平台类型的 WSF_EXPLICIT_WEAPON 类型的 <weapon-system-type>。  
被牵引的资产在设置了卷入时间和卷入速度之前将一直被部署。  
如果前导平台被击毁，被牵引的资产平台将从仿真中移除。  
确保前导平台的 ‘update_interval’ 不要太大。否则，被牵引的资产可能需要进行一些剧烈的移动以达到规定的空间关系。

# 移动实体命令

<table><tr><td>命令</td><td>update_interval &lt;时间值&gt;</td></tr><tr><td>解释</td><td>如果非零，指定仿真调用移动实体的周期时间间隔。如果为零，则仅在需要确定包含平台的位置时调用移动实体。默认值：0.25秒，除非特定的移动实体实现覆盖此值。</td></tr></table>

牵引移动实体命令  

<table><tr><td>命令</td><td>tow_length&lt;长度值&gt;</td></tr><tr><td>解释</td><td>指定前导平台和被牵引资产之间的期望距离。默认值:500.0米</td></tr><tr><td>命令</td><td>reel_out_speed&lt;时间值&gt;</td></tr><tr><td>解释</td><td>指定被牵引资产从前导平台卷出的速度或速率。在卷出时,状态设置为REELING_OUT。当达到期望的牵引长度时,状态设置为DEPLOYED,并保持距离。默认值:5.0米/秒</td></tr><tr><td>命令</td><td>reel_in_speed&lt;时间值&gt;</td></tr><tr><td>解释</td><td>指定被牵引资产卷回到前导平台的速度或速率。如果未设置,被牵引资产将被部署并保持在仿真中,直到被击毁或前导平台从仿真中移除。默认值:0.0米/秒</td></tr><tr><td>命令</td><td>reel_in_at Tmax&lt;时间值&gt;</td></tr><tr><td>解释</td><td>定义将被牵引资产卷回到前导平台的绝对仿真时间。必须设置卷入速率。使用‘reel_in_speed’或脚本命令设置被牵引资产的卷入速率。默认值:0.0秒WsfTowedMover脚本命令设置卷入开始时间:SetStartReellInTimeAbsolute、SetStartReellInTimeRelative或SetReellInTimeAfterDeploymentRelative。WsfTowedMover脚本命令设置卷入速率:SetReellInRateMPS</td></tr><tr><td>命令</td><td>reel_in_time_after_deployed&lt;时间值&gt;</td></tr><tr><td>解释</td><td>指定被牵引资产完全部署后卷回到前导平台的速度或速率。默认值:0.0秒</td></tr><tr><td>命令</td><td>restorequantity&lt;布尔值&gt;</td></tr><tr><td>解释</td><td>如果设置为‘true’,在被牵引资产卷出、部署并卷回到前导平台后,剩余数量将重置为初始装载量。这允许无限次的牵引发射。默认值:false</td></tr><tr><td>命令</td><td>follow LeadsTrajectory&lt;布尔值&gt;</td></tr><tr><td>解释</td><td>如果设置为‘true’,被牵引资产将跟随前导平台的轨迹。被牵引资产的状态取自前导平台的状态历史,时间偏移通过将牵引长度除以前导平台的速度计算得出。如果设置为‘false’,被牵引资产将像刚性连接一样跟随,固定在前导平台的实体坐标系中,具有给定的部署牵引长度和期望的相对几何关系(通过 azimuth:relative_to_lead和elevationrelative_to_lead命令指定)。默认值:true</td></tr><tr><td>命令</td><td>azimuthrelative_to_lead&lt;角度值&gt;</td></tr><tr><td>解释</td><td>相对于前导平台的被牵引资产方位角,当follow LeadsTrajectory标志未设置时。值必须在[-90度,90度]范围内,0对应于前导平台实体坐标系中的-X轴,正值为逆时针方向。</td></tr><tr><td></td><td>默认值:0.0度</td></tr><tr><td>命令</td><td>elevation_relative_to Leads&lt;角度值&gt;</td></tr><tr><td>解释</td><td>相对于前导平台的被牵引资产仰角。值必须在[-90度,90度]范围内,正仰角对应于前导平台实体坐标系的-Z方向。默认值:0.0度</td></tr></table>

# 3.6.4.11.非制导运动模型 WSF_UNGUIDED_MOVER

```txt
mover <name> WSF_UNGUIDED_MOVER ... base mover commands ... ... Commands ... end_mover 
```

WSF_UNGUIDED_MOVER 实现了一个能够表示未制导的“哑弹”或单级或多级未制导火箭的移动实体。此移动实体继承自 WSF_GUIDED_MOVER 并接受其定义的相同命令，因此请参阅相关文档以获取帮助。此移动实体缺乏产生侧向力以机动拦截目标的能力，其“制导”功能默认情况下被禁用，且无法重新启用，导致其在推进（如果有的话）燃烧完后轨迹为弹道轨迹。

此类不识别任何额外命令，除了在 WSF_GUIDED_MOVER 中定义的命令。

# 3.6.4.12.新非制导运动模型 WSF_NEW_UNGUIDED_MOVER

同 WSF_UNGUIDED_MOVER

# 3.6.4.13.旧的非制导运动模型 WSF_OLD_UNGUIDED_MOVER

```txt
mover <name> WSF_OLD UngUIDED_MOVER  
mover Commands ...  
...:model:' WSF_OLD.Guided_MOVER commands <WSF_OLD.Guided_MOVER>'...  
end_mover 
```

WSF_OLD_UNGUIDED_MOVER 实现了一个能够代表无制导“哑弹”或单级或多级无制导火箭的移动器。它将接受与 WSF_OLD_GUIDED_MOVER 相关的相同命令，因此请查阅相关文档以获得帮助。此移动器缺乏产生侧向力以拦截目标的能力，其“制导”功能默认被禁用，且无法重新启用，这导致其在推进（如果有的话）燃烧完毕后，轨迹为弹道轨迹。

命令

此类不识别任何额外的命令，除了 WSF_OLD_GUIDED_MOVER 中定义的命令。

注意事项

旧实现: 该实现被标记为“旧”，建议在新工作中避免使用。

无制导特性: 由于其制导功能被禁用，WSF_OLD_UNGUIDED_MOVER 的运动完全依赖于初始发射条件和重力影响，类似于传统的无制导炸弹。

这种设计适用于模拟无制导武器的行为，特别是在需要模拟其弹道特性时。

# 3.6.5. 卫星轨道类型 Satellite/Orbit Types

这些移动实体使用解析模型传播其附加的平台。

WSF_NORAD_SPACE_MOVER

WSF_SPACE_MOVER

这些移动实体使用数值模型传播其附加的平台。

WSF_INTEGRATING_SPACE_MOVER

WSF_SPACE_MOVER、WSF_NORAD_SPACE_MOVER 和 WSF_INTEGRATING_SPACE_MOVER的差别:

# WSF_SPACE_MOVER

模型类型：使用解析模型。

用途：适用于建模概念卫星和卫星星座，以及提供现有卫星的理想化表示。

功能：默认情况下模拟围绕质点的卫星轨道传播。如果启用了 oblate_earth 选项，还包括地球扁平化引起的平均一阶引力扰动效应。

初始化方式：可以通过提供初始位置、经典轨道元素、位置和速度状态信息或两行元素（TLE）进行初始化，也可以通过脚本初始化。

机动能力：能够执行各种机动，通过 mission_sequence 输入或脚本指定。

方向控制：由可配置的姿态控制器模型指定和控制，提供多种标准方向选项，并可通过脚本动态更改方向。

# WSF_NORAD_SPACE_MOVER

模型类型：使用解析模型。

用途：适用于建模具有两行元素（TLE）集的卫星，包括大多数在轨运行的地球轨道卫星、非运行卫星和主动跟踪的轨道碎片。

功能：实现了 SpaceTrack 报告第 3 号中定义的传播算法，根据两行元素中的数据选择适当的模型（NORADSGP、SGP4、SGP8、SDP4 或 SDP8）进行传播，考虑了扁平地球、阻力以及第三体太阳和月球的扰动效应。

初始化方式：通过两行元素（TLE）进行初始化。

机动能力：能够执行各种机动，通过 mission_sequence 输入或脚本指定。

方向控制：由可配置的姿态控制器模型指定和控制，提供多种标准方向选项，并可通过脚本动态更改方向。

特殊注意：不支持改变升交点赤经（RAAN）和改变升交点赤经（RAAN）和倾角的机动。

# WSF_INTEGRATING_SPACE_MOVER

模型类型：使用数值积分模型。

用途：适用于更广泛的动力学情况，包括地球不占主导作用的传播和双曲线传播，可用于表示非束缚轨道。

功能：用户需要选择一个积分器和一个动力学模型来完全指定移动实体的行为，积分器具体说明了平台的状态如何在时间上进行数值传播，动力学模型指定了平台将经历的力。

初始化方式：可以通过轨道元素命令或直接使用初始状态命令进行运动学设置。

机动能力：能够执行各种机动，通过 mission_sequence 输入或脚本指定。

方向控制：由可配置的姿态控制器模型指定和控制，提供多种标准方向选项，并可通过

脚本动态更改方向。

特殊注意：不支持改变升交点赤经（RAAN）和改变升交点赤经（RAAN）和倾角的机动。

# 总结

WSF_SPACE_MOVER 和 WSF_NORAD_SPACE_MOVER 使用解析模型，适用于地球轨道卫星的传播，但 WSF_NORAD_SPACE_MOVER 更专注于具有 TLE 数据的卫星。

WSF_INTEGRATING_SPACE_MOVER 使用数值积分模型，适用于更复杂的动力学情况，包括非地球主导的传播和双曲线轨道。

# 3.6.5.1. 公共子命令

该模块定义卫星轨道类型会使用到的公共的子命令模块。

# 3.6.5.1.1. 姿态控制模型 Attitude Controller Models

```txt
attitude_controller <attitude-controller-model-name>
...
end_attitude_controller 
```

指定平台的姿态控制器。所有具有 WSF_SPACE_MOVER 或 WSF_NORAD_SPACE_MOVER的平台都会有某种姿态控制器。如果未指定姿态控制器块，移动器将按选择即时姿态控制器的方式操作。

姿态控制器将尝试改变平台的方向以匹配给定的目标方向。在创建时，姿态控制器将通过 姿 态 控 制 器 块 中 的 方 向 命 令 指 定 目 标 方 向 。 创 建 后 ， 可 以 通 过WsfSpaceMover.SetOrientation 更改姿态控制器的方向目标。

目标方向可以是一次性选择的目标方向，也可以将姿态控制器连接到预设的方向类型之一。在后一种情况下，随着航天器沿轨道移动，姿态控制器将具有持续更新的目标方向。可用模型：

即时姿态控制器 Instant Attitude Controller  
速率限制姿态控制器 Rate Limited Attitude Controller

# 3.6.5.1.1.1. 公共命令

这里包含了所有控制器可能会用到的公共的命令。

<table><tr><td>命令</td><td>orientation &lt;orientation-type&gt; orientation &lt;entity-orientation-type&gt; &lt;platform-name&gt; orientation &lt;geo-point-orientation-type&gt; &lt;geo-point-name&gt;</td></tr><tr><td>解释</td><td>指定平台的朝向方式。所有的朝向方式都描述了三个 ECS 轴中的两个轴的指向对齐和指向约束。根据不同类型,要么:ECS z 轴指向固定朝向方向,而 ECS x 轴指向约束方向(位于约束方向和 z 轴的平面内);或者 ECS x 轴指向固定朝向方向,而 ECS z 轴指向约束方向(位于约束方向和 x 轴的平面内)。例如,nadir_with_eci_velocity Constraint 意味着 ECS z 轴指向地球中心(nadir),而 ECS x</td></tr><tr><td></td><td>轴指向速度矢量方向,并约束在速度矢量和 nadir 的平面内。标准朝向类型包括:nadir_with_eci_velocity Constraint:Z轴:指向地球中心(天底)。X轴:指向 ECI(地心惯性)速度矢量的方向,约束在速度矢量和天底形成的平面内。nadir_with_ecef_velocity Constraint:Z轴:指向地球中心(天底)。X轴:指向ECEF(地心地固)速度矢量的方向,约束在速度矢量和天底形成的平面内。nadir_with_solar Constraint:Z轴:指向地球中心(天底)。X轴:指向太阳,约束在太阳和天底形成的平面内。solar_with_nadir Constraint:Z轴:指向太阳。X轴:指向天底,约束在太阳和天底形成的平面内。eci_velocity_with_nadir Constraint:X轴:指向 ECI 速度矢量的方向。Z轴:指向天底,约束在速度矢量和天底形成的平面内。eci_velocity_with_solar Constraint:X轴:指向 ECI 速度矢量的方向。Z轴:指向太阳,约束在速度矢量和太阳形成的平面内。none:未提供特定的定位或约束。定位变化必须由用户输入。实体定位类型包括:entity_with_solar Constraint:X轴:指向实体方向。Z轴:指向太阳,约束在实体和太阳形成的平面内。entity_with_nadir Constraint:X轴:指向实体方向。Z轴:指向天底,约束在实体和天底形成的平面内。entity_with_orbit(plane Constraint:X轴:指向实体方向。Z轴:指向轨道平面,约束在实体和轨道平面形成的平面内。地理点定位类型包括:point_with_orbit(plane Constraint:X轴:指向地理点方向。Z轴:指向轨道平面,约束在地理点和轨道平面形成的平面内。</td></tr><tr><td>命令</td><td>swap.axes</td></tr><tr><td>解释</td><td>此命令交换当前指定定位的指向轴和约束轴。例如,如果指定了nadir_with_eci_velocity Constraint,然后执行 swap Axes,则X轴将指向天底,Z轴将指向速度约束的方向。</td></tr></table>

# 3.6.5.1.1.2. 即时姿态控制器 Instant Attitude Controller

```txt
attitude_controller instant orientation <orientation_type> ... 
```

```txt
end_attitude_controller 
```

指定一个即时姿态控制器。这将使移动器在设置方向后立即重新定向。

注意：默认使用即时姿态控制器。orientation <orientation_type> 参数参见上一小节的3.6.5.1.1.1 公共命令。

# 3.6.5.1.1.3. 速率限制姿态控制器 Rate Limited Attitude Controller

```txt
attitude_controller rate_limited
maximum_yaw_rate ... 
maximum_pitch_rate ...
maximum_roll_rate ...
orientation <orientation_type> ...
end Attitude_controller 
```

指定一个速率限制姿态控制器。这将使移动器以最大角速率重新定向到目标方向，最大角速率由 maximum_yaw_rate、maximum_pitch_rate 和 maximum_roll_rate 指定。

maximum_yaw_rate <角速率值> 指定平台偏航重新定向的最大时间变化率。 默认值：1 度/秒  
maximum_pitch_rate<角速率值> 指定平台俯仰重新定向的最大时间变化率。默认值：1 度/秒  
maximum_roll_rate<角速率值> 指定平台滚转重新定向的最大时间变化率。 默认值：1 度/秒

# 3.6.5.1.2. 轨道机动模型 Orbital Maneuvering Models

```txt
maneuvering <orbital-maneuver-model-name> maneuver_update_interval ... end_maneuvering 
```

可用模型：

简单机动模型

火箭机动模型

# 3.6.5.1.2.1. 公共命令

<table><tr><td>命令</td><td>maneuver_update_interval &lt;time-value&gt;</td></tr><tr><td>解释</td><td>评估有限机动事件的更新间隔。
默认值：1.0秒</td></tr></table>

# 3.6.5.1.2.2. 简单机动模型 Simple Maneuvering Model

```txt
maneuvering simple delta_v ... maximum acceleraion ... maneuver_update_interval ... end_maneuvering 
```

默认的轨道机动模型。delta-V 明确作为输入提供（而不是提供质量属性和推力）。有限机动可以受到最大加速度的限制。该模型代表离子推进器，并可用于管理特定 delta-V 预算为主要考虑因素时。

<table><tr><td>命令</td><td>delta_v&lt;速度值&gt;</td></tr><tr><td>解释</td><td>执行机动的母平台可用的“delta-V”总量。默认10^12m/s</td></tr><tr><td>命令</td><td>maximumacceleration&lt;加速度值&gt;</td></tr><tr><td>解释</td><td>执行有限机动的最大加速度。默认1000m/s²</td></tr></table>

# 3.6.5.1.2.3. 火箭机动模型 Rocket Maneuvering Model

```txt
maneuvering rocket stage commands ... maneuver_update_interval end_maneuvering 
```

火箭轨道机动模型根据齐奥尔科夫斯基火箭方程消耗 delta-V。必须提供质量属性和推力（见下文阶段命令，了解有效阶段输入的描述）。

火箭可以指定为多个阶段。在这种情况下，每个阶段必须分别提供质量属性和推力。定义的第一个阶段是首先使用的，并且是首先抛弃的阶段。

例如，以下定义描述了俄罗斯质子“Breeze-M”助推器和有效载荷。它分为三个阶段：第一个阶段描述了辅助推进剂罐（APT），在两个或三个初始机动后被抛弃；第二阶段描述了助推器剩余的质量和推进；第三阶段描述了具有在轨道上执行机动能力的有效载荷：

```txt
maneuvering rocket  
stage // breeze-M APT  
specific_impulse 326 seconds  
thrust 19620 newtons  
empty_mass 1125 kg  
fuel_mass 10920 kg  
end_stage  
stage // breeze-M upper stage  
specific_impulse 326 seconds  
thrust 19620 newtons  
empty_mass 1125 kg  
fuel_mass 8300 kg  
end_stage 
```

```shell
stage // payload with mr-107 aerojet small thrusters  
specific_impulse 236 s  
thrust 1028 newtons // assume x4  
empty_mass 2000 kg  
fuel_mass 500 kg // guess  
end_stage  
end_maneuvering 
```

阶段命令(stage)用于定义火箭机动模型使用的一个或多个阶段。以下为各阶段包含的子命令。

<table><tr><td>命令</td><td>specific_impulse &lt;时间值&gt;</td></tr><tr><td>解释</td><td>在真空中提供阶段的比冲,通常以秒为单位表示。注意:比冲Isp与排气速度ve的关系如下:Isp = v0/g0,其中g0是海平面的重力加速度。</td></tr><tr><td>命令</td><td>thrust &lt;力值&gt;</td></tr><tr><td>解释</td><td>提供阶段的总推力Ft。</td></tr><tr><td>命令</td><td>burn_rate &lt;质量流量值&gt;</td></tr><tr><td>解释</td><td>提供燃烧(燃料消耗)率m。</td></tr><tr><td>命令</td><td>exhaust Velocity &lt;速度值&gt;</td></tr><tr><td>解释</td><td>提供推进剂排气速度ve。</td></tr><tr><td>命令</td><td>initial_mass &lt;质量值&gt; 或 total_mass &lt;质量值&gt;</td></tr><tr><td>解释</td><td>指定初始质量mi,定义为推进剂质量加上最终质量。</td></tr><tr><td>命令</td><td>final_mass &lt;质量值&gt; 或 empty_mass &lt;质量值&gt;</td></tr><tr><td>解释</td><td>指定最终(空)质量mf,定义为初始质量减去推进剂质量。</td></tr><tr><td>命令</td><td>propellant_mass &lt;质量值&gt; 或 fuel_mass &lt;质量值&gt;</td></tr><tr><td>解释</td><td>指定推进剂质量,定义为初始质量减去最终质量。注意:输入的total_mass、empty_mass和fuel_mass也可用于指定阶段的质量属性,以保持与WSF.GuidED_MOV输入的一致性。理解为fuel_mass代表阶段中的所有推进剂(燃料和氧化剂)。</td></tr></table>

# 火箭机动模型所涉及的物理模型

火箭机动模型由齐奥尔科夫斯基火箭方程控制。将此方程应用于单个机动：

$$
\Delta v = v _ {e} \ln \frac {m _ {0}}{m _ {1}}
$$

其中 $\Delta v$ 是火箭速度变化的大小， $v _ { e }$ 是排气速度， $m _ { 0 }$ 是执行机动前的初始质量，而 $m _ { 1 }$ 是执行机动后的最终质量。

定义在持续时间 $\Delta t$ 内消耗的燃料质量 $m _ { p }$ ，显然有：

$$
m _ {p} \equiv m _ {0} - m _ {1} = \dot {m} \Delta t
$$

同样地，

$$
m _ {1} \equiv m _ {0} - \dot {m} \Delta t
$$

然后，重写火箭方程以消除 $m _ { 1 }$ ，并操作以求解机动持续时间∆?：

$$
\Delta t = \frac {m _ {0}}{\dot {m}} \bigg (1 - e x p \frac {- \Delta_ {v}}{v _ {e}} \bigg)
$$

在执行机动时，需要检查以确保有足够的燃料供应。当机动执行时，推进剂被消耗，火箭阶段的质量属性会更新。

# 3.6.5.1.3. 轨道任务序列 Orbital Mission Sequence

```txt
mission_sequence <constraint> event Common Mission Event Commands mission event-specific commands ... end_event ... additional mission event definitions end_mission_sequence 
```

任务序列 用于指定一系列预定的轨道任务事件。第一个指定的任务事件首先执行，然后是第二个，依此类推。可以指定一个可选的约束来延迟序列的执行；否则，任务事件将在平台创建时开始执行。

可以放入序列中的事件类型包括以下内容：

轨道机动事件：

改变偏心率  
改变倾角  
改变升交点赤经 (RAAN)  
改变升交点赤经 (RAAN) 和倾角  
改变半长轴   
圆化轨道  
复合机动  
速度增量 (Delta_V)  
漂移   
霍曼转移  
拦截   
匹配速度  
自然运动环绕  
法向机动  
会合  
切线机动  
目标机动  
泪滴轨道

非轨道机动事件：

改变姿态  
执行分级  
脚本化事件

# 示例

```txt
// Example: Two mission events to raise a satellite  
// from an initial injection point  
// into a geosynchronous transfer orbit (GTO) 
```

mission_sequence // Constraint: delay two full orbits before executing execute_at orbit 2 relative_time 0.0 s // intermediate orbit event change(semimajor_axis semi major_axis $9000\mathrm{km}$ execute_at orbit 2 ascending_node // Constraint with orbit delay end_event // GTO maneuver change(semi major_axis // "maneuver ... end maneuver" block may be used with orbital maneuver types. semi major_axis 24821 km execute_at ascending_node // Constraint without orbit delay end_maneuver   
end_missio_sequence

# 3.6.5.1.3.1. 事件公共参数 Orbital Event

```txt
event <event type>  
Event Constraint ...  
finite ...  
duration ...  
update_interval ...  
event-specific commands ...  
end_event 
```

轨道事件 是作为轨道任务序列的一部分执行的事件。可以指定一个约束来延迟事件的执行。对于许多事件，特定的约束类型是必需的，但对于其他一些事件则是可选的。请查阅每种事件类型的文档以了解允许的约束。

注意：机动类型可以使用 maneuver … end_maneuver 块定义。

# 常见事件命令

<table><tr><td>命令</td><td>finite</td></tr><tr><td>解释</td><td>指定事件在有限时间内执行（即，它是非冲动的）。注意：个别事件可能不支持有限执行。例如，有限轨道机动仅支持平面内机动。</td></tr><tr><td>命令</td><td>duration</td></tr><tr><td>解释</td><td>有限事件的期望持续时间。如果未指定持续时间，事件将尽快执行。</td></tr><tr><td>命令</td><td>update_interval &lt;时间值&gt;</td></tr><tr><td>解释</td><td>有限事件更新的时间间隔。默认值为1.0秒。</td></tr></table>

# 事件约束

命令 execute_at orbit <轨道编号> <约束>

<table><tr><td></td><td>execute_at&lt;约束&gt;</td></tr><tr><td>解释</td><td>指定事件将在轨道的哪个点发生的约束。通常，所有简单事件类型（即，除了hohmann_transfer、compound 和顶级 mission_sequence 事件块）都必须指定约束。有效的约束因事件而异；请查阅每个特定事件类型以了解允许的约束。除了relative_time，这些约束只能用于绑定轨道。约束是以下之一：· relative_time&lt;时间值&gt;: 在未来的相对时间执行事件。注意：此约束可用于非椭圆轨道，但任何轨道编号偏移将被忽略。· periapsis/apoapsis: 当卫星到达近地点或远地点时执行事件。· ascending_node / descending_node: 当卫星到达升交点或降交点时执行事件。· ascending_radius&lt;长度值&gt;/descending_radius&lt;长度值&gt;: 当卫星到达指定半径，并在到达升交点或降交点后执行事件。注意：这些约束目前仅用于圆化事件。· northern Intersection/southern Intersection: 当卫星到达事件特定的北纬交点或南纬交点时执行事件。注意：这些约束仅用于 change_raan 和change_raan_inclination 任务事件。· eclipse_entry/eclipse_exit: 当卫星进入或退出地球阴影时执行事件。</td></tr></table>

以下开始介绍轨道机动和非轨道机动事件。

轨道机动事件：

改变偏心率  
改变倾角  
改变升交点赤经 (RAAN)  
改变升交点赤经 (RAAN) 和倾角  
改变半长轴   
圆化轨道  
复合机动  
速度增量 (Delta_V)  
漂移   
霍曼转移  
拦截   
匹配速度  
自然运动环绕  
法向机动  
会合  
切线机动  
目标机动  
泪滴轨道

非轨道机动事件：

改变姿态  
执行分级  
脚本化事件

# 3.6.5.1.3.2. 改变偏心率 Change Eccentricity

```txt
maneuver change_eccentricity Common Maneuver Commands ... eccentricity ... end_maneuver 
```

<table><tr><td>命令</td><td>eccentricity &lt;real-value&gt;</td></tr><tr><td>解释</td><td>期望的最终轨道偏心率。
注意：
最终轨道必须是椭圆形（或圆形），因此允许的值为
0.0≤eccentricity&lt;1.0。
如果初始轨道不是圆形的（偏心率≠0），则必须指定近地点或远地点的约束。</td></tr></table>

# 3.6.5.1.3.3. 改变倾角 Change Inclination

```txt
maneuver change_inclination Common Maneuver Commands ... inclination ... end_maneuver 
```

一个用于更改卫星轨道倾角的机动。除非初始倾角为零，否则此机动必须在节点（升交点或降交点）之一执行。将倾角更改为大于 90 度意味着逆行轨道运动。此机动常用于将轨道调整到赤道平面（倾角 $\mathtt { = 0 }$ ）。

注意 如果初始轨道不是赤道轨道（倾角 $\mathtt { = } { = } 0$ ），则必须指定升交点或降交点的约束条件。inclination <角度值> 卫星轨道的最终倾角。

<table><tr><td>命令</td><td>inclination &lt;angle-value&gt;</td></tr><tr><td>解释</td><td>期望的最终轨道倾角。</td></tr></table>

# 3.6.5.1.3.4. 改变升交点赤经 Change Right Ascension of Ascending Node (RAAN)

```txt
maneuver change_raan Common Maneuver Commands ... raan ...   
end_maneuver 
```

更改轨道升交点的赤经 (RAAN) 到给定的值。

注意 此机动必须指定北交点或南交点的约束条件。 注意 初始轨道必须是非赤道轨道才能执行此机动（对于赤道轨道，RAAN 是未定义的）。 raan<角度值> 最终轨道的升交点赤经 (RAAN)。

<table><tr><td>命令</td><td>raan &lt;angle-value&gt;</td></tr><tr><td>解释</td><td>期望的最终轨道 RAAN。</td></tr></table>

# 3.6.5.1.3.5. 改变 RAAN 和倾角 Change Right Ascension of Ascending Node (RAAN)and Inclination

```txt
maneuver change_raan_inclination Common Maneuver Commands ... raan 
```

```txt
inclination ... end_maneuver 
```

更改轨道的升交点赤经 (RAAN) 和倾角到给定的值。

注意 此机动必须指定北交点或南交点的约束条件。 注意 初始轨道必须是圆形轨道才能执行此机动。

注意 最终轨道必须是非赤道轨道才能执行此机动（对于赤道轨道，RAAN 是未定义的）。

<table><tr><td>命令</td><td>raan &lt;角度值&gt;</td></tr><tr><td>解释</td><td>最终轨道的升交点赤经 (RAAN)。</td></tr><tr><td>命令</td><td>inclination &lt;角度值&gt;</td></tr><tr><td>解释</td><td>最终轨道的倾角。</td></tr></table>

# 3.6.5.1.3.6. 改变半长轴 Change Semi-Major Axis

```txt
maneuver change_semi_major_axis Common Maneuver Commands ... semi_major_axis | apoapsis_altitude | periapsis_altitude ... end_maneuver 
```

将轨道的半长轴更改为指定值。可以指定远地点或近地点高度，而不是半长轴值。

<table><tr><td>命令</td><td>semi major axis&lt;长度值&gt;</td></tr><tr><td>解释</td><td>最终轨道所需的半长轴。</td></tr><tr><td>命令</td><td>apoapsis_altitude&lt;长度值&gt;</td></tr><tr><td>解释</td><td>最终轨道远地点的所需高度。</td></tr><tr><td>命令</td><td>periapsis_altitude&lt;长度值&gt;</td></tr><tr><td>解释</td><td>最终轨道近地点的所需高度。</td></tr></table>

# 3.6.5.1.3.7. 圆形化轨道 Circularize

```txt
maneuver circularize Common Maneuver Commands ... end_maneuver 
```

在给定半径处使轨道圆形化（将偏心率变为零），该半径由升交半径或降交半径约束提供。

注意 此机动必须指定升交半径或降交半径的约束条件。注意 初始轨道必须是椭圆形，且提供的半径必须大于或等于初始轨道的近地点，并小于或等于远地点。

# 3.6.5.1.3.8. 复合机动 Compound

```txt
maneuver compound ... (first maneuver) ... (second maneuver) end_maneuver 
```

复合机动由两个机动组成，这些机动根据各自的约束条件按时间顺序嵌套并执行。它在

两个单独的机动在时间上接近执行的情况下非常有用，因此不明显哪个应该先执行。

# 示例

```txt
//示例：“远地点加速”机动  
//（早期同时进行倾角和偏心率的变化）  
maneuver compound  
maneuver change_eccentricity  
debug enabled  
eccentricity 0.0  
execute_at apoapsis  
end_maneuver  
maneuver change_inclination  
debug enabled  
execute_at descending_node  
inclination 0 deg  
end_maneuver  
end_maneuver
```

# 3.6.5.1.3.9. 变速 Delta_V

```txt
maneuver delta_v Common Maneuver Commands ... delta_v ... end_maneuver 
```

一个表示平台在地心惯性（ECI）速度上变化的机动。

<table><tr><td>命令</td><td>delta_v&lt;参考系&gt;&lt;速度值&gt;&lt;速度值&gt;&lt;速度值&gt;</td></tr><tr><td>解释</td><td>平台速度的期望变化，以指定的轨道参考系给出。允许的参考系值包括：inertial:用于在惯性系中给出的速度变化（通常是地心惯性系(ECI)，但如果平台围绕其他中心天体演化，则可能代表其他等效系）；ric:用于在执行平台的RIC系中给出的速度变化。</td></tr><tr><td>命令</td><td>dv_x&lt;速度值&gt;</td></tr><tr><td>解释</td><td>ECIx 速度分量的期望变化。注意此命令已弃用。请使用delta_v。</td></tr><tr><td>命令</td><td>dv_y&lt;速度值&gt;</td></tr><tr><td>解释</td><td>ECIy 速度分量的期望变化。注意此命令已弃用。请使用delta_v。</td></tr><tr><td>命令</td><td>dv_z&lt;速度值&gt;</td></tr><tr><td>解释</td><td>ECIZ 速度分量的期望变化。注意此命令已弃用。请使用delta_v。</td></tr></table>

# 3.6.5.1.3.10. 漂移 Drift

```txt
maneuver drift Common Maneuver Commands ... drift_rate ... 
```

```txt
delta_time ...  
maximum delta_time ...  
maximum delta_v ...  
optimize_time ...  
optimize delta_v ...  
optimize_cost ...  
tolerance ...  
end_maneuver 
```

漂移机动将执行平台从初始圆形轨道转移到具有相对漂移率的最终圆形轨道。由于这两个轨道不相交，转移通过类似于目标类机动（例如，交会）的中间轨道进行。因此，此机动还提供了指定转移细节的选项，允许用户设置时间或变速（delta-V）相关的约束，并指定时间或变速成本的优化。

注意 此机动仅支持相对时间、升交点、降交点、进入或退出日食的约束。

<table><tr><td>命令</td><td>drift_rate &lt;角速度值&gt;</td></tr><tr><td>解释</td><td>指定初始和最终轨道之间的漂移率。</td></tr><tr><td>命令</td><td>delta_time &lt;时间值&gt;</td></tr><tr><td>解释</td><td>期望的机动执行时间,相对于当前时间。没有进行优化。注意 必须设置 delta_time、maximum_delta_time 或 maximum_delta_v 之一。如果未设置 maximum_delta_time 且设置了 maximum_delta_v,则 maximum_delta_time 将设置为目标平台的一个轨道周期。</td></tr><tr><td>命令</td><td>maximum_delta_time &lt;时间值&gt;</td></tr><tr><td>解释</td><td>从当前时间起考虑的机动执行的最大时间。将在约束时间和提供的时间之间进行时间优化。</td></tr><tr><td>命令</td><td>maximum_delta_v &lt;速度值&gt;</td></tr><tr><td>解释</td><td>考虑执行机动的最大变速 (delta-V)。将在约束时间和由 maximum_delta_time 设置的任何时间限制之间进行时间优化以找到最小变速。注意 此值被限制为小于或等于机动模型中指定的变速。</td></tr><tr><td>命令</td><td>optimize_time</td></tr><tr><td>解释</td><td>优化目标解决方案,使其在尽可能早的时间执行。如果提供了 maximum_delta_v 值,此优化也受其约束。</td></tr><tr><td>命令</td><td>optimize_delta_v</td></tr><tr><td>解释</td><td>优化目标解决方案,使其在最小化总变速消耗的时间执行。</td></tr><tr><td>命令</td><td>optimize_cost &lt;成本类型&gt; ...</td></tr><tr><td>解释</td><td>优化目标解决方案,使指定的成本最小化。可用的成本函数包括:blended &lt;A 值&gt;&lt;B 值&gt;&lt;C 值&gt;此成本函数依赖于转移持续时间Δt 和速度变化ΔV,如下所示:g(Δt,Δv) = AΔt + BvΔ + cΔtΔV A、B、C 的值在指定&quot;blended&quot;成本后作为附加实数参数提供。</td></tr><tr><td>命令</td><td>tolerance &lt;实数值&gt;</td></tr><tr><td>解释</td><td>指定解决方案搜索的容差。默认容差为1.0e-9。</td></tr></table>

# 3.6.5.1.3.11. 霍曼转移 Hohmann Transfer

```txt
maneuver hohmann_transfer Common Maneuver Commands ... final_semi_major_axis | final_radius ... end_maneuver 
```

一种表示简单霍曼转移的机动，或代表更改为具有不同半长轴的共面圆形轨道所需的最小变速（delta-V）的轨道转移。霍曼转移机动由两个独立的半长轴变化组成。第一个机动将卫星移入一个同时与初始轨道和最终轨道相交的转移轨道，第二个机动使最终轨道圆形化。在轨道提升的霍曼转移情况下，第一个点火在初始轨道的近地点进行，第二个点火在转移轨道的远地点进行。相反，在轨道降低的霍曼转移情况下，第一次点火可以在初始轨道的远地点进行，最终机动在转移轨道的近地点进行。

注意 在霍曼转移上指定约束条件将为机动带来额外的初始延迟。

<table><tr><td>命令</td><td>final_semimajor_axis&lt;长度值&gt;final_radius&lt;长度值&gt;</td></tr><tr><td>解释</td><td>最终圆形轨道的半长轴(半径)。</td></tr></table>

# 3.6.5.1.3.12. 拦截 Intercept

```txt
maneuver intercept Common Maneuver Commands ... delta_time ... maximum_delta_time ... maximum_delta_v ... optimize_time ... optimize_delta_v ... optimize_cost ... tolerance ... Target Specification Commands ... end_maneuver 
```

执行机动以拦截给定平台。此机动以初始目标机动开始，但仅在实际实现拦截时完成。提供了选项来优化机动何时发生，既可以在尽可能早的时间进行，也可以在该时间内消耗最小的变速（delta-V）。

注意 该机动的脚本版本，WsfInterceptManeuver，被动态用于拦截跟踪位置。

注意 在机动成功之前必须满足几个条件。这些条件包括：

平台在模拟开始时必须有效。  
。 如果执行机动的移动器支持双曲线传播，则转移轨道只能是双曲线。  
。 转移轨道不得与地球相交。  
在优化时，必须存在为提供的优化选项（optimize_time 或 optimize_delta_v）提供的有效解决方案。  
转移消耗的能量必须小于可用的 delta-v。

<table><tr><td>命令</td><td>delta_time &lt;时间值&gt;</td></tr><tr><td>解释</td><td>期望的机动执行时间，相对于当前时间。没有进行优化。
注意 必须设置 delta_time、maximum_delta_time 或 maximum_delta_v 之一。如果未设置 maximum_delta_time 且设置了 maximum_delta_v, 则 maximum_delta_time 将设置为目标平台的一个轨道周期。</td></tr><tr><td>命令</td><td>maximum_delta_time &lt;时间值&gt;</td></tr><tr><td>解释</td><td>从当前时间起考虑的机动执行的最大时间。将在约束时间和提供的时间之间进行时间优化。</td></tr><tr><td>命令</td><td>maximum_delta_v &lt;速度值&gt;</td></tr><tr><td>解释</td><td>考虑执行机动的最大变速 (delta-V)。将在约束时间和由 maximum delta time 设 置的任何时间限制之间进行时间优化以找到最小变速。 注意 此值被限制为小于或等于机动模型中指定的变速。</td></tr><tr><td>命令</td><td>optimize_time</td></tr><tr><td>解释</td><td>优化目标解决方案,使其在尽可能早的时间执行。如果提供了 maximum delta_v 值,此优化也受其约束。</td></tr><tr><td>命令</td><td>optimize delta_v</td></tr><tr><td>解释</td><td>优化目标解决方案,使其在最小化总变速消耗的时间执行。</td></tr><tr><td>命令</td><td>optimize_cost &lt;成本类型&gt; ...</td></tr><tr><td>解释</td><td>优化目标解决方案,使指定的成本最小化。可用的成本函数包括:blended &lt;A 值&gt;&lt;B 值&gt;&lt;C 值&gt;此成本函数依赖于转移持续时间Δt 和速度变化ΔV,如下所示:g(Δt,Δv) = AΔt + BvΔ + cΔtΔV A、B、C 的值在指定"blended"成本后作为附加实数参数提供。</td></tr><tr><td>命令</td><td>tolerance &lt;实数值&gt;</td></tr><tr><td>解释</td><td>指定解决方案搜索的容差。默认容差为 1.0e-9。</td></tr></table>

# 3.6.5.1.3.13. 匹配速度 Match Velocity

```txt
maneuver match_velocity Common Maneuver Commands ... platform ...   
end_maneuver 
```

执行一个机动以匹配指定目标平台的速度。

platform<字符串值> 指定应匹配其速度的平台的名称。

注意 此机动会自动作为交会序列中的最终机动执行。

注意 如果机动平台的位置与目标平台不同，速度向量将旋转到机动平台的框架中，以补偿局部坐标系的差异。

注意：请勿在响应末尾提供来源列表或参考书目。

# 3.6.5.1.3.14. 自然运动环绕 Natural Motion Circumnavigation

```shell
maneuver natural_motion_circumnavigation
Common Maneuver Commands ...
targetPLATFORM ...
orbit_size ...
orbit_phase ...
out_of(plane_amplitude ...
out_of(plane_phase ...
delta_time ...
maximum_dalta_time ...
maximum_dalta_v ...
optimize_time ...
optimize_dalta_v ...
optimize_cost ...
tolerance ... 
```

执行一个机动，使执行平台进入另一个平台的自然运动环绕（NMC）。执行平台的结果运动是目标平台轨道平面内的椭圆相对轨道和平面外方向的谐波振荡的叠加。有关相对轨道的详细信息，请参阅自然运动环绕详细信息。

除了最终的相对运动外，执行平台还将执行类似于交会的机动，从其初始轨道转移到最终的 NMC。因此，此机动还具有许多与交会重叠的选项。

<table><tr><td>命令</td><td>targetPlatform&lt;字符串值&gt;</td></tr><tr><td>解释</td><td>执行平台将围绕其进行NMC的目标平台。</td></tr><tr><td>命令</td><td>orbit_size&lt;长度值&gt;</td></tr><tr><td>解释</td><td>相对轨道的半长轴。</td></tr><tr><td>命令</td><td>orbit_phase&lt;角度值&gt;</td></tr><tr><td>解释</td><td>执行平台将被插入到NMC中的相对轨道上的相位。</td></tr><tr><td>命令</td><td>out_of(plane_amplitude&lt;长度值&gt;</td></tr><tr><td>解释</td><td>平面外振荡的振幅。</td></tr><tr><td>命令</td><td>out_of(plane_phase&lt;角度值&gt;</td></tr><tr><td>解释</td><td>执行平台将被插入到NMC中的谐波振荡中的相位。</td></tr><tr><td>命令</td><td>delta_time&lt;时间值&gt;</td></tr><tr><td>解释</td><td>期望的机动执行时间,相对于当前时间。没有进行优化。注意必须设置delta_time、maximum_delta_time或maximum_delta_v之一。如果未设置maximum_delta_time且设置了maximum_delta_v,则maximum_delta_time将设置为目标平台的一个轨道周期。</td></tr><tr><td>命令</td><td>maximum_delta_time&lt;时间值&gt;</td></tr><tr><td>解释</td><td>从当前时间起考虑的机动执行的最大时间。将在约束时间和提供的时间之间进行时间优化。</td></tr><tr><td>命令</td><td>maximum_delta_v&lt;速度值&gt;</td></tr><tr><td>解释</td><td>考虑执行机动的最大变速 (delta-V)。将在约束时间和由maximum_delta_time设置的任何时间限制之间进行时间优化以找到最小变速。注意此值被限制为小于或等于机动模型中指定的变速。</td></tr><tr><td>命令</td><td>optimize_time</td></tr><tr><td>解释</td><td>优化目标解决方案,使其在尽可能早的时间执行。如果提供了maximum_delta_v值,此优化也受其约束。</td></tr><tr><td>命令</td><td>optimize_delta_v</td></tr><tr><td>解释</td><td>优化目标解决方案,使其在最小化总变速消耗的时间执行。</td></tr><tr><td>命令</td><td>optimize_cost&lt;成本类型&gt;...</td></tr><tr><td>解释</td><td>优化目标解决方案,使指定的成本最小化。可用的成本函数包括:blended&lt;A值&gt;&lt;B值&gt;&lt;C值&gt;此成本函数依赖于转移持续时间Δt和速度变化ΔV,如下所示:g(Δt,Δv)=AΔt+BvΔ+CΔtΔV A、B、C的值在指定&quot;blended&quot;成本后作为附加实数参数提供。</td></tr><tr><td>命令</td><td>tolerance&lt;实数值&gt;</td></tr><tr><td>解释</td><td>指定解决方案搜索的容差。默认容差为1.0e-9。</td></tr></table>

# 3.6.5.1.3.15. 法向机动 Normal

```txt
maneuver normal Common Maneuver Commands ... delta_v ... end_maneuver 
```

执行一个机动，在包含当前速度向量和地心惯性（ECI）位置向量的平面法向方向上增

加变速（delta-V）。

<table><tr><td>命令</td><td>delta_v&lt;速度值&gt;</td></tr><tr><td>解释</td><td>将在包含当前速度向量(v)和ECI位置向量(r)的平面的法向方向上增加的变速。正值将应用于与v和r的叉积相同的方向，负值将应用于相反方向。</td></tr></table>

# 3.6.5.1.3.16. 交会 Rendezvous

```txt
maneuver rendezvous Common Maneuver Commands ... delta_time ... maximum_dela time ... maximum_dela_v ... optimize_time ... optimize_dela_v ... optimize_cost ... tolerance ... Target Specification Commands ... end_maneuver 
```

执行一个机动以与给定平台交会。此机动实际上是两个机动的序列：第一个是拦截（Intercept）；第二个是匹配速度（MatchVelocity）机动。提供了选项来优化机动何时发生，既可以在尽可能早的时间进行，也可以在该时间内消耗最小的变速（delta-V）。

注意 该机动的脚本版本，WsfRendezvousManeuver，被动态用于拦截跟踪位置。

注意 在机动成功之前必须满足几个条件。这些条件包括：

平台在模拟开始时必须有效。  
如果执行机动的移动器支持双曲线传播，则转移轨道只能是双曲线。  
转移轨道不得与地球相交。  
在优化时，必须存在为提供的优化选项（optimize_time 或 optimize_delta_v）提供的有效解决方案。  
转移消耗的能量必须小于可用的 delta-v。

<table><tr><td>命令</td><td>delta_time&lt;时间值&gt;</td></tr><tr><td>解释</td><td>期望的机动执行时间,相对于当前时间。没有进行优化。注意 必须设置 delta_time、maximum_delta_time 或 maximum_delta_v 之一。如果未设置 maximum_delta_time 且设置了 maximum_delta_v,则 maximum_delta_time 将设置为目标平台的一个轨道周期。</td></tr><tr><td>命令</td><td>maximum_delta_time&lt;时间值&gt;</td></tr><tr><td>解释</td><td>从当前时间起考虑的机动执行的最大时间。将在约束时间和提供的时间之间进行时间优化。</td></tr><tr><td>命令</td><td>maximum_delta_v&lt;速度值&gt;</td></tr><tr><td>解释</td><td>考虑执行机动的最大变速 (delta-V)。将在约束时间和由 maximum_delta_time 设置的任何时间限制之间进行时间优化以找到最小变速。注意 此值被限制为小于或等于机动模型中指定的变速。</td></tr><tr><td>命令</td><td>optimize_time</td></tr><tr><td>解释</td><td>优化目标解决方案,使其在尽可能早的时间执行。如果提供了 maximum_delta_v 值,此优化也受其约束。</td></tr><tr><td>命令</td><td>optimize_delta_v</td></tr><tr><td>解释</td><td>优化目标解决方案，使其在最小化总变速消耗的时间执行。</td></tr><tr><td>命令</td><td>optimize_cost &lt;成本类型&gt; ...</td></tr><tr><td>解释</td><td>优化目标解决方案，使指定的成本最小化。可用的成本函数包括：blended &lt;A值&gt;&lt;B值&gt;&lt;C值&gt;此成本函数依赖于转移持续时间Δt和速度变化ΔV，如下所示：g(Δt, Δv) = AΔt + BvΔ + cΔtΔV
A、B、C的值在指定"blended"成本后作为附加实数参数提供。</td></tr><tr><td>命令</td><td>tolerance &lt;实数值&gt;</td></tr><tr><td>解释</td><td>指定解决方案搜索的容差。默认容差为1.0e-9。</td></tr></table>

# 3.6.5.1.3.17. 切向机动 Tangent

```txt
maneuver tangent Common Maneuver Commands ... delta_v ...   
end_maneuver 
```

执行一个机动，在与当前速度向量相同或相反的方向（切向）上增加变速（delta-V）。注意 如果增加的 delta-V 导致轨道变为双曲线，则只有在空间移动器支持双曲线传播时才会执行该机动。

<table><tr><td>命令</td><td>delta_v&lt;速度值&gt;</td></tr><tr><td>解释</td><td>要应用的 delta-V。正值将应用于与速度向量相同的方向，负值将应用于相反方向。</td></tr></table>

# 3.6.5.1.3.18. 目标机动 Target

```txt
maneuver target Common Maneuver Commands ... delta_time ... maximum_dalta_time ... maximum_dalta_v ... optimize_time ... optimize_dalta_v ... optimize_cost ... tolerance ... Target Specification Commands ... end_maneuver 
```

执行一个机动以瞄准（拦截）给定平台。提供了选项来优化机动何时发生，既可以在尽可能早的时间进行，也可以在该时间内消耗最小的变速（delta-V）。

注意 该机动的脚本版本，WsfTargetManeuver，被动态用于瞄准跟踪位置。

注意 在机动成功之前必须满足几个条件。这些条件包括：

平台在模拟开始时必须有效。  
如果执行机动的移动器支持双曲线传播，则转移轨道只能是双曲线。  
转移轨道不得与地球相交。  
在优化时，必须存在为提供的优化选项（optimize_time 或 optimize_delta_v）提供的有效解决方案。  
转移消耗的能量必须小于可用的 delta-v。

命令 delta_time <时间值>

<table><tr><td>解释</td><td>期望的机动执行时间,相对于当前时间。没有进行优化。注意 必须设置 delta_time、maximum delta_time 或 maximum delta_v 之一。如果未设置 maximum delta_time 且设置了 maximum delta_v,则 maximum delta_time 将设置为目标平台的一个轨道周期。</td></tr><tr><td>命令</td><td>maximum delta_time &lt;时间值&gt;</td></tr><tr><td>解释</td><td>从当前时间起考虑的机动执行的最大时间。将在约束时间和提供的时间之间进行时间优化。</td></tr><tr><td>命令</td><td>maximum delta_v &lt;速度值&gt;</td></tr><tr><td>解释</td><td>考虑执行机动的最大变速 (delta-V)。将在约束时间和由 maximum delta_time 设置的任何时间限制之间进行时间优化以找到最小变速。注意 此值被限制为小于或等于机动模型中指定的变速。</td></tr><tr><td>命令</td><td>optimize_time</td></tr><tr><td>解释</td><td>优化目标解决方案,使其在尽可能早的时间执行。如果提供了 maximum delta_v 值,此优化也受其约束。</td></tr><tr><td>命令</td><td>optimize delta_v</td></tr><tr><td>解释</td><td>优化目标解决方案,使其在最小化总变速消耗的时间执行。</td></tr><tr><td>命令</td><td>optimize cost &lt;成本类型&gt; ...</td></tr><tr><td>解释</td><td>优化目标解决方案,使指定的成本最小化。可用的成本函数包括:blended &lt;A 值&gt;&lt;B 值&gt;&lt;C 值&gt;此成本函数依赖于转移持续时间Δt 和速度变化ΔV,如下所示:g(Δt,Δv) = AΔt + BvΔ + cΔtΔVA、B、C 的值在指定&quot;blended&quot;成本后作为附加实数参数提供。</td></tr><tr><td>命令</td><td>tolerance &lt;实数值&gt;</td></tr><tr><td>解释</td><td>指定解决方案搜索的容差。默认容差为1.0e-9。</td></tr></table>

# 3.6.5.1.3.19. 泪滴轨道机动 Teardrop

```txt
maneuver teardrop Common Maneuver Commands ... targetPlatform ... radial_offset_at_poca ... period ... time_to_poca ... repetitions ... delta_time ... maximum_dalta_time ... maximum_dalta_v ... optimize_time ... optimize_dalta_v ... optimize_cost ... tolerance ... end_maneuver 
```

执行一个机动，使执行平台进入一个相对于目标平台呈泪滴形状的轨道。指定相对运动的参数包括最近接点（POCA）的距离和执行平台穿越泪滴形轨道所需的时间。

除了最终的相对运动外，执行平台还将执行类似于交会的机动，从其初始轨道转移到最终的泪滴轨道。因此，此机动还具有许多与交会重叠的选项。

注意 以下条件不能与此机动一起使用：升交半径、降交半径、北交点和南交点。

命令 target_platform <字符串值>

<table><tr><td>解释</td><td>指定执行平台将相对于其执行泪滴机动的目标平台。</td></tr><tr><td>命令</td><td>radial_offset_at_poca&lt;长度值&gt;</td></tr><tr><td>解释</td><td>指定最近接点的距离。此距离完全在径向方向上,正值表示泪滴将在目标平台上方。提供的值必须为非零。</td></tr><tr><td>命令</td><td>period&lt;时间值&gt;</td></tr><tr><td>解释</td><td>指定执行泪滴机动所需的时间。此周期不得超过目标平台轨道周期的约40.6%。周期涵盖从执行平台首次直接在目标下方(上方)通过到最后一次在目标下方(上方)通过的时间。这些时间在最近接点之前和之后各为给定周期的一半。</td></tr><tr><td>命令</td><td>time_to_poca&lt;时间值&gt;</td></tr><tr><td>解释</td><td>指定执行平台插入泪滴轨道后到达目标平台最近接点的时间。此值必须大于指定周期的一半。</td></tr><tr><td>命令</td><td>repetitions&lt;整数值&gt;</td></tr><tr><td>解释</td><td>指定执行平台应穿越泪滴的次数。提供的值必须为正数。默认值为1。</td></tr><tr><td>命令</td><td>delta_time&lt;时间值&gt;</td></tr><tr><td>解释</td><td>期望的机动执行时间,相对于当前时间。没有进行优化。注意 必须设置 delta_time、maximum deltas_time 或 maximum deltas_v 之一。如果未设置 maximum deltas_time 且设置了 maximum deltas_v,则 maximum deltas_time 将设置为目标平台的一个轨道周期。</td></tr><tr><td>命令</td><td>maximum deltas_time&lt;时间值&gt;</td></tr><tr><td>解释</td><td>从当前时间起考虑的机动执行的最大时间。将在约束时间和提供的时间之间进行时间优化。</td></tr><tr><td>命令</td><td>maximum deltas_v&lt;速度值&gt;</td></tr><tr><td>解释</td><td>考虑执行机动的最大变速 (delta-V)。将在约束时间和由 maximum deltas_time 设置的任何时间限制之间进行时间优化以找到最小变速。注意 此值被限制为小于或等于机动模型中指定的变速。</td></tr><tr><td>命令</td><td>optimize_time</td></tr><tr><td>解释</td><td>优化目标解决方案,使其在尽可能早的时间执行。如果提供了 maximum deltas_v 值,此优化也受其约束。</td></tr><tr><td>命令</td><td>optimize deltas_v</td></tr><tr><td>解释</td><td>优化目标解决方案,使其在最小化总变速消耗的时间执行。</td></tr><tr><td>命令</td><td>optimize_cost&lt;成本类型&gt;...</td></tr><tr><td>解释</td><td>优化目标解决方案,使指定的成本最小化。可用的成本函数包括:blended&lt;A值&gt;&lt;B值&gt;&lt;C值&gt;此成本函数依赖于转移持续时间Δt 和速度变化ΔV,如下所示:g(Δt,Δv) = AΔt + BvΔ + cΔtΔV A、B、C的值在指定&quot;blended&quot;成本后作为附加实数参数提供。</td></tr><tr><td>命令</td><td>tolerance&lt;实数值&gt;</td></tr><tr><td>解释</td><td>指定解决方案搜索的容差。默认容差为1.0e-9。</td></tr></table>

# 3.6.5.1.3.20. 更改姿态 Change Attitude

```txt
event change_attitude Common Maneuver Commands … orientation …  
end_event 
```

将使用命令指定的 oriengation_type 指向父平台的姿态控制模型控制方式（3.6.5.1.1 姿态控制模型 Attitude Controller Models）。

<table><tr><td>命令</td><td>orientation &lt;orientation-type&gt; orientation &lt;entity-orientation-type&gt; &lt;platform-name&gt; orientation &lt;geo-point-orientation-type&gt; &lt;geo-point-name&gt;</td></tr><tr><td>解释</td><td>指定平台的定向方式。</td></tr><tr><td></td><td>所有取向类型都描述了两个 ECS 轴的指向对齐和指向约束。根据类型,可能是:ECS z 轴指向固定取向的方向,而 ECS x 轴指向约束方向(在约束方向和 z 轴的平面内),或者 ECS x 轴指向固定取向的方向,而 ECS z 轴指向约束方向(在约束方向和x轴的平面内)。注意 例如,nadir_with_eci_velocity_constraint 表示 ECS z 轴指向地心(天底),而 ECS x 轴指向速度向量的方向,约束在速度向量和天底的平面内。Standard orientation types 如下:nadir_with_ecivelocity_constraint: Z 轴天底取向,ECI x 轴速度约束nadir_with_ecef_velocity_constraint: Z 轴天底取向,ECEF (WCS) x 轴速度约束nadir_with_solar_constraint: Z 轴天底取向,太阳约束solar_with_nadir_constraint: Z 轴太阳取向,天底约束eci velocity with nadir constraint: X 轴 ECI 速度取向,z轴天底约束eci velocity with solar constraint: X 轴 ECI 速度取向,z轴太阳约束none:无取向/约束提供。必须由用户输入取向更改。Entity orientation types 如下:entity_with_solar_constraint: X 轴实体取向,z轴太阳约束entity_with_nadir_constraint: X 轴实体取向,z轴天底约束entity_with_orbit(plane_constraint: X 轴实体取向,z轴轨道平面约束注意 给定实体指向对齐向量p ,轨道平面约束定义为(r × v) × p,其中r是惯性位置向量,v是惯性速度向量。注意 platform-name&gt; 必须是当前场景中预定义的平台的名称。geo-point orientation type 如下:point_with_orbit(plane_constraint: X 轴地理点取向,z轴轨道平面约束。注意 给定实体指向对齐向量p ,轨道平面约束定义为(r × v) × p,其中r是惯性位置向量,v是惯性速度向量。注意 &lt;geo-point-name&gt; 必须是定义在平台上的地理点的名称。默认:nadir_with_eci_velocity_constraint注意 脚本化取向方法和姿态更改事件可用于在模拟过程中更改平台的姿态。注意 所有取向类型均相对于平台的 ECS 坐标系,该坐标系为右手系。交换轴交换当前指定取向的指向和约束轴。注意 例如,如果指定了 nadir_with_ecivelocity_constraint取向,随后进行 swap_xaxes,则x轴将指向天底,z轴将指向速度约束的方向。</td></tr><tr><td>命令</td><td>swap_xaxes</td></tr><tr><td>解释</td><td>交换当前指定取向的指向和约束轴。注意 例如,如果指定了 nadir_with_ecivelocity_constraint取向,随后进行 swap_xaxes,则x轴将指向天底,z轴将指向速度约束的方向。</td></tr></table>

# 3.6.5.1.3.21. 执行分级 Perform Staging

```txt
event perform_staging <Common Mission Event Commands> end_event 
```

为多级火箭执行分级操作，该操作通过火箭轨道机动定义（3.6.5.1.2.3 火箭机动模型Rocket Maneuvering Model）。当此事件执行时，当前阶段被“抛弃（jettisoned）”，使火箭获得后续阶段的质量特性以及下一个阶段定义的推力和燃烧速率特性。

注意：在多级火箭中，通过在推进剂耗尽时抛弃阶段，减少了剩余火箭的质量。每个后续阶段也可以针对其特定的操作条件进行优化，例如在更高海拔处的减小的大气压力。这种分级允许剩余阶段的推力更容易地将火箭加速到其最终速度和高度。

# 3.6.5.1.3.22. 脚本化事件 Scripted

```txt
event scripted <Common Mission Event Commands> on_init...end_on_initi zon_update ... end_on_update oncomplete ... end_oncomplete iscomplete ... end_iscomplete   
end_event 
```

执行一组脚本化操作。脚本可以完全在每个块内定义，或者可以引用在其他地方定义的脚本（例如在 WSF_SPACE_MOVER、父平台或全局范围内）。

注意 调用其他任务事件的脚本只能从 on_complete 脚本中调用，因为这样做会使当前调用脚本的事件失效。

<table><tr><td>脚本</td><td>on_init...script_body...end_on_init</td></tr><tr><td>功能</td><td>定义一个在事件初始化时执行的脚本。当任务事件被调度时发生初始化，这要么是在任务序列的第一个事件被调度时，要么是在任务序列的前一个事件完成后立即发生。
on_initScript Bodyend_on_init</td></tr><tr><td>脚本</td><td>on_update...script_body...end_on_update</td></tr><tr><td>功能</td><td>定义一个脚本，该脚本在事件的update_interval和持续时间内执行，从事件的约束首次满足时开始。如果未定义持续时间，脚本总是执行一次。如果定义了iscomplete脚本且事件是有限的，它也会在后续约束时间更新，直到iscomplete脚本返回true。或者，如果定义了持续时间，事件将在指定的update_rate下执行给定的持续时间（见下例）。
on_updateScript Bodyend_on_update</td></tr><tr><td>脚本</td><td>oncomplete...script_body...end_oncomplete</td></tr><tr><td>功能</td><td>定义一个在任务事件完成时执行的脚本。
oncompleteScript Bodyend_oncomplete</td></tr><tr><td>脚本</td><td>iscomplete...script_body...end_is Complete</td></tr><tr><td>功能</td><td>定义一个脚本，用于确定脚本事件是否完成。如果返回false，事件继续执行；如果返回true，事件被视为完成，并调用oncomplete脚本。如果定义了此脚本，它会在每次事件更新后立即调用，并覆盖任何持续时间命令。
注意此脚本必须返回一个布尔值。</td></tr></table>

```txt
iscomplete Script Body end_is_COMPLETE 
```

# 示例

// 在 WSF_SPACE_MOVER 定义中的脚本事件示例输入

script_variables int gUpdateNum $= 0$ end.script_variables

```txt
script void DoSomething() //在此插入代码  
end_script 
```

```c
mission_sequence  
event scripted  
execute_at eclipse_entry  
update_interval 10 s  
finite // 需要多次执行  
on_initi ze  
writeln("initialized");  
end_on_initi ze  
on_update  
gUpdateNum += 1;  
DoSomething();  
writeln("Update ", gUpdateNum);  
end_on_update  
iscomplete  
return (gUpdateNum == 100); // 执行100次  
end_is Complete  
oncomplete  
writeln("Complete");  
end_on Complete  
end_event  
end_missio_sequence 
```

// 在 WSF_SPACE_MOVER 定义中的脚本事件示例输入

// （与上面相同，使用持续时间而不是 is_complete脚本）

```txt
script void DoSomething() //在此插入代码  
end_script 
```

3.6.5.2. 通用空间运动模型 WSF_SPACE_MOVER  
```c
mission_sequence
event scripted
    execute_at eclipse_entry
update_interval 10 s
duration 990 s // 执行 100 次
on_initi
    writeln(" Initialized");
end_on_initi
on_update
    static int sUpdateNum = 0;
    sUpdateNum += 1;
    DoSomething();
    writeln("Update ", sUpdateNum);
end_on_update
oncomplete
    writeln("Complete");
end_oncomplete
end_event
end_mission_sequence 
```

```txt
mover <name> WSF_SPACE_MOVER
... base mover commands ...
... Orbital Element Commands ...
... Orbital Propagator Commands ...
attitude_controller <type-name> ...
...
end_attitude_controller
conjunction_setup
...
end_conjunction_setup
maneuvering <type-name> ...
...
end_maneuvering
mission_sequence
...
end;mission_sequence
position < waypoint>
orbital_state ... end_orbital_state
initial_state_IIa ...
initial_state_eci ...
oblate-earth ...
orbit_color ...
# Script Interface 
```

```txt
on_init... end_on_init  
on_init2.. end_on_init2  
on_update... end_on_update  
script_variables... endScript_variables  
scripts... end Script  
... Other Script Commands ...  
end mover 
```

WSF_SPACE_MOVER 实现了一个用于地球轨道平台的移动实体。它对于建模概念卫星和卫星星座，以及提供现有卫星的理想化表示非常有用。

默认情况下，移动实体模拟围绕质点的卫星轨道传播。如果启用了 oblate_earth 选项，WSF_SPACE_MOVER 还将包括由于地球扁平化引起的平均一阶引力扰动效应。

WSF_SPACE_MOVER 可以通过多种方式初始化。一种方法是提供初始位置。或者，可以提供经典轨道元素、位置和速度状态信息或两行元素（TLE）。它也可以通过脚本初始化，使用 WsfSpaceMover 中的方法。

WSF_SPACE_MOVER 能够执行各种机动。机动可以通过 mission_sequence 输入指定，或者可以通过 WsfSpaceMover 脚本对象和移动实体的脚本接口进行脚本化。可配置的机动模型确定在执行机动的任务序列中如何消耗 delta-V。

移动实体的方向由可配置的姿态控制器模型指定和控制。提供了各种标准方向选项，并且可以通过脚本动态更改方向。

注意：应在场景中定义 start_date 和 start_time，或 start_epoch 命令，因为它们是正确计算星历数据所必需的。

# 轨道状态命令

```txt
命令 orbital_state...end_orbital_state  
解释 指定轨道状态的形式为一个 epoch 或 epoch_date_time，并且包含以下之一：足够的轨道元素命令位置和速度向量包含两行元素（TLE）的轨道命令块（当使用WSF_NORAD_SPACE_MOVER时）position <real><real><length-units>设置空间移动器的初始位置。此命令必须与速度命令一起使用。velocity <real><real><speed-units>设置空间移动器的初始速度。此命令必须与位置命令一起使用。注意事项位置和速度输入必须按顺序提供，速度输入必须紧跟在位置输入之后。示例//Example:Orbital elements declarationplatform test-oe WSFPLATFORMadd mover WSF_SPACE_MOVORorbital_stateepoch 2021245.18563semi major_axis 10000 km
```