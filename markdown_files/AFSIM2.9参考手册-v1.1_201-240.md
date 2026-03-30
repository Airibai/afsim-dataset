```txt
command_chain<string> <string>[new(commandChains,$1);this=$2] 
```

```txt
apply($$) 
```

将先前的 (new …) 或 (load …) 规则应用于代理数据结构。

通常 (new …) 和 (load …) 仅对符号表操作，对结构属性没有影响。此命令对代理结构执行与符号表相同的操作。

```txt
skip() 
```

进入没有当前代理对象的模式。这允许执行规则而不应用任何代理更改。例如，当使用<Platform> 规则时，当前代理对象必须是 Platform 类型，否则会报告错误。使用

```txt
[skip()]<Platform> 
```

或缩写形式（规则名称前缀为冒号）

```txt
:Platform> 
```

# 2. 平台 WSF_PLATFORM

AFSIM中所有能够布署的装备都是基于一个平台，比如一艘舰，一个飞机。而平台是由组件构成，比如舰上的弹就是一个组件。组件无法独立成为一个可布置的单位，只有形成平台才是可布置的。AFSIM 中有大量的关于平台的使用示例，此处对其相关命令做全面的介绍。以全面为主。

```txt
platform <platform-name> <platform-type>
    acoustic_signature ...
    altitude ...
    aux_data ...
    category ...
    clear_categories
    commander ...
    command_chain ...
    concealment_factor ...
    creation_time ...
    empty_mass ...
    fuel ... end_fuel
    fuel_mass ...
    geo_point ...
    group_join ...
    group Leave ...
    heading ...
    height ...
    icon ...
    indestructible ...
    infrared_signature ...
    inherent Contrast ...
    initial DAMAGE_factor ...
    length ...
    marking ...
    mgrs_coordinates ...
    add_mover ... end_mover
    mover ... end_mover
    navigation Errors ... endjahging Errors
    nutation_update_interval ...
    on_broken ...
    optical_reflectivity ...
    optical_signature ...
    payload_mass ...
    position ...
    precession_nutation_update_interval ...
    radar_signature ...
    route ... end routc 
```

```txt
side ...  
spatial_domain ...  
<component> ... end_<component>  
add <component> ... end_<component>  
edit <component> ... end_<component>  
delete <component> ...  
track ... end_track  
trackmanager...end_trackmanager  
use-zone...  
width ...  
zone...end-zone  
zone_set...end-zone_set  
#Script Interface  
on_initiage...end_on_initiage  
on_initiage2...end_on_initiage2  
on_update...end_on_update  
script_variables...end.script_variables  
script...endcript  
...Other Script_Commands...  
script void on DAMAGE_received() ... endScript  
script void onPLATFORM_deleted() ... endScript  
script void on-commander_deleted(WsfPlatform aCommander) ... endScript  
script void on-peer_deleted(WsfPlatform aPeer) ... endScript  
script void on_subordinate_deleted(WsfPlatform aSubordinate) ... endScript  
callback...end_callback  
endplatform 
```

作者注：官方帮助文档给的是上面的，感觉少了 sensor... end_sensor 和 processor...end_processor

WSF_PLATFORM属于顶级模型，没有需要继承的其它父类模型命令。平台中包含一系列的组件，通过以下表格中平台中包含的命令便可以了解组件在平台中定义的方式。平台中的所有组件细节均在 3 组件 PlatformPart 中一节中进行定义。

<table><tr><td>命令</td><td>side &lt;side-name&gt;</td></tr><tr><td>解释</td><td>定义平台所属的“方”（可以是“团队”或“归属”）。side 子命令可以是蓝方（blue）、红方（red）、国家名称或团队名称。具体支持哪些方，请参考所使用的可视化应用或工具。
默认值：无。</td></tr><tr><td>命令</td><td>icon &lt;icon-name&gt;</td></tr><tr><td>解释</td><td>指定在显示此类平台时所用的图标名称。如果平台类型在 dis_INTERFACE(4.2 分布式接</td></tr><tr><td></td><td>口dis-interface) 模块中没有相关的 entity_type 子命令,则使用此图标。默认值:或&lt;new-type-name&gt;的值。</td></tr><tr><td>命令</td><td>marking&lt;marking-name&gt;</td></tr><tr><td>解释</td><td>指定要应用于平台的标记名称。此文本字段在dis/interface(4.2分布式接口dis/interface)中与该平台关联。默认值:无标记。</td></tr><tr><td>命令</td><td>indestructible (or destructible)</td></tr><tr><td>解释</td><td>指示平台类型是否不可摧毁。每次命中将根据以下公式更新生存概率:Ps(new) = Ps(old) × (1 - Pk)默认值:可摧毁(destructible)。</td></tr><tr><td>命令</td><td>on_broken [ remove | disable | disabled但不限 movable]</td></tr><tr><td>解释</td><td>指示当平台被破坏时应执行的操作。指定 remove 时,平台被破坏后将从仿真中移除。指定 disable 时,平台被破坏后将留在仿真中,平台的运动将停止,所有子系统将被设置为“非操作状态”且无法重新开启。脚本方法 WsfPlatform DamageFactor 将返回 1.0。指定 disabled但不限 movable 时,平台被破坏后将留在仿真中,平台的运动将继续。一些移动器可能会因破坏状态而影响运动,如减速和失控。所有子系统将被设置为“非操作状态”且无法重新开启。脚本方法 WsfPlatform DamageFactor 将返回 1.0。默认值:remove。</td></tr><tr><td>命令</td><td>spatial_domain [ land | air | subsurface | surface | space ]</td></tr><tr><td>解释</td><td>指示平台主要操作的空间域。这有时用于分类对象是“陆地”对象、“空间”对象等。默认值:如果平台有移动器,则默认值由移动器的类型推断(例如,对于WSF_AIR_MOVER,默认值为“air”)。如果平台没有移动器,则默认值为“land”。</td></tr><tr><td>命令</td><td>acoustic_signature&lt;string-reference&gt;</td></tr><tr><td>解释</td><td>指定此平台类型的声学特征定义。特征类型必须已通过 acoustic_signature 定义。默认值:无。参考:4.4.1 声学特性 acoustic_signature</td></tr><tr><td>命令</td><td>infrared_signature&lt;string-reference&gt;</td></tr><tr><td>解释</td><td>指定此平台类型的红外特征定义。特征类型必须已通过 infrared_signature 定义。默认值:无。参考:4.4.2 红外特性 infrared_signature</td></tr><tr><td>命令</td><td>optical_reflectivity&lt;string-reference&gt;</td></tr><tr><td>解释</td><td>指定此平台类型的光学反射率定义。特征类型必须已通过 optical_reflectivity 定义。默认值:无。参考:4.4.3 光学反射率 optical_reflectivity</td></tr><tr><td>命令</td><td>optical_signature&lt;string-reference&gt;</td></tr><tr><td>解释</td><td>指定此平台类型的光学特征定义。特征类型必须已通过 optical_signature 定义。默认值:无。参考:4.4.4 光学特性 optical_signature</td></tr><tr><td>命令</td><td>radar_signature&lt;string-reference&gt;</td></tr><tr><td>解释</td><td>指定此平台类型的雷达特征定义。特征类型必须已通过 radar_signature 定义。默认值:无。</td></tr><tr><td>命令</td><td>geo_point&lt;geo-point-name&gt;&lt;latitude-value&gt;&lt;longitude-value&gt;&lt;length-value&gt;</td></tr><tr><td>解释</td><td>用纬度、经度、高度元组定义一个命名位置。该位置可以通过 WsfPlatform.GeoPoint脚本方法访问。</td></tr><tr><td>命令</td><td>position&lt;latitude-value&gt;&lt;longitude-value&gt;</td></tr><tr><td>解释</td><td>指定平台的纬度和经度。此命令仅适用于没有移动器的静态平台。默认值:On 0e。</td></tr><tr><td>命令</td><td>mutation_update_interval&lt;time-value&gt;</td></tr><tr><td>解释</td><td>指定用于 WCS-ECI 坐标转换的章动计算更间隔时间。默认值:1000 秒。</td></tr><tr><td>命令</td><td>precession_nutation_update_interval&lt;time-value&gt;</td></tr><tr><td>解释</td><td>指定用于 WCS-ECI 坐标转换的章动计算更间隔时间。</td></tr><tr><td></td><td>默认值:1000秒。2.9以后该命令被nutation_update_interval代替。</td></tr><tr><td>命令</td><td>mgrs Coordinate&lt;MGRS-value&gt;</td></tr><tr><td>解释</td><td>指定平台在军事网格参考系统中的坐标。此命令仅适用于没有移动器的静态平台。</td></tr><tr><td>命令</td><td>altitude &lt;length-value&gt;[agl | msl]</td></tr><tr><td>解释</td><td>指定平台的高度。此命令仅适用于没有移动器的静态平台。如果在平台中定义了移动器,则忽略此命令。默认值:0米msl。</td></tr><tr><td>命令</td><td>creation_time &lt;random-time-reference&gt;</td></tr><tr><td>解释</td><td>指定平台在仿真中添加的时间。平台存在于内存中但尚未成为仿真中的参与者。默认值:0秒(在仿真开始时创建)。</td></tr><tr><td>命令</td><td>heading &lt;angle-value&gt;</td></tr><tr><td>解释</td><td>指定平台的朝向。此命令仅适用于没有移动器的静态平台。如果在平台中定义了移动器,则忽略此命令。默认值:0度。</td></tr><tr><td>命令</td><td>empty_mass &lt;mass-reference&gt;</td></tr><tr><td>解释</td><td>指定平台的空重,通常是一个固定值。默认值:0公斤。</td></tr><tr><td>命令</td><td>fuel_mass &lt;mass-reference&gt;</td></tr><tr><td>解释</td><td>指定平台的燃料质量。当用户在输入文件中指定时,该值假定为固定值。然而,如果平台包含燃料对象,则在运行时允许且预期会修改燃料质量,覆盖用此关键字指定的值。默认值:0公斤。</td></tr><tr><td>命令</td><td>payload_mass &lt;mass-reference&gt;</td></tr><tr><td>解释</td><td>指定平台的载荷质量。当用户在输入文件中指定时,该值假定为固定值。然而,某些运行时事件(例如投放浮标)可能会改变载荷质量。默认值:0公斤。</td></tr><tr><td>命令</td><td>concealment_factor &lt;concealment-factor&gt;</td></tr><tr><td>解释</td><td>用于表示平台的视觉隐蔽程度。值为0.0表示没有隐蔽。值为1.0表示完全隐藏(例如在建筑物内或地下掩体中)。介于这两个端点之间的值表示增加的伪装程度。大多数传感器不会检测到隐蔽因子为1.0的平台,但任何较小的值都没有效果。默认值:0.0。</td></tr><tr><td>命令</td><td>initial DAMAGE_factor &lt;initial DAMAGE_factor&gt;</td></tr><tr><td>解释</td><td>损伤因子是[0..1]范围内的值,用于表示平台的损伤程度。值为0表示没有损伤,而值为1表示平台“破损”。默认值:0.0。</td></tr><tr><td>命令</td><td>track_management trackmanager #Commands track-manager-commands...end trackmanager</td></tr><tr><td>解释</td><td>此块中的命令由平台的主跟踪管理器处理。请参阅trackmanager。参考:4.5跟踪管理器trackmanager</td></tr><tr><td>命令</td><td>aux_data &lt;aux-data&gt; ... end aux_data</td></tr><tr><td>解释</td><td>定义平台的辅助数据。请参阅aux_data。参考:4.6辅助数据aux_data</td></tr><tr><td>命令</td><td>height &lt;length-reference&gt; length &lt;length-reference&gt; width &lt;length-reference&gt;</td></tr><tr><td>解释</td><td>指定平台的尺寸。默认值:所有值均为0。</td></tr><tr><td>命令</td><td>category &lt;category-name&gt;</td></tr><tr><td>解释</td><td>指定平台属于指定类别。类别可用于强制传感器忽略平台。类别也可以通过WsfPlatform CategoryMemberOf 脚本方法访问。默认值:平台不属于任何类别。</td></tr><tr><td>命令</td><td>clear Categories</td></tr><tr><td>解释</td><td>取消任何先前的 category 命令。</td></tr><tr><td>命令</td><td>group_join &lt;group-name&gt;</td></tr><tr><td>解释</td><td>group Leave &lt;group-name&gt;将平台加入或移出指定组。</td></tr><tr><td>命令</td><td>commander &lt;commander-name&gt; command chain &lt;command-chain-name&gt; &lt;commander-name&gt;</td></tr><tr><td>解释</td><td>commander指定平台在默认指挥链中的直接上级(指挥官)。默认指挥官是自己。</td></tr><tr><td></td><td>command_chain 指定平台在给定指挥链中的直接上级(指挥官)。指挥链由决策程序使用,以确定命令和/或报告的接收者。参考:4.7 指挥链 Command Chains</td></tr><tr><td>命令</td><td>route route-commandst...end-route</td></tr><tr><td>解释</td><td>route 子命令提供一组定义路径或路线的航点,用于平台移动器。参考:4.8.1 路由 route</td></tr><tr><td>命令</td><td>add mover&lt;mover-type&gt; mover-commandst...end movermover&lt;mover-type&gt; mover-commandst...end_mover</td></tr><tr><td>解释</td><td>移动器定义平台可以移动的域及其在域内的移动方式。参考:3.6 运动组件 Mover</td></tr><tr><td>命令</td><td>fuel &lt;fuel-type&gt; fuel-commandst...end_fuel</td></tr><tr><td>解释</td><td>燃料对象可以附加到平台上以模拟燃料消耗的影响。默认值:未定义燃料对象(不模拟燃料消耗)。参考:3.7 燃料组件 fuel</td></tr><tr><td>命令</td><td>&lt;component&gt;&lt;component-name&gt;[&lt;component-type&gt;] component-commandst...end_&lt;component&gt;add &lt;component&gt;&lt;component-name&gt;&lt;component-type&gt;component-commandst...end_&lt;component&gt;edit &lt;component&gt;&lt;component-name&gt;component-commandst...end_&lt;component&gt;delete &lt;component&gt;&lt;component-name&gt;</td></tr><tr><td>解释</td><td>向平台添加组件,修改或移除现有组件。参考:3 组件 Platform Part。</td></tr><tr><td>命令</td><td>track ...end track</td></tr><tr><td>解释</td><td>track 块中定义的目标会一直被跟踪,无论传感器有没有探测到,相当于定义了个初始跟踪物体,只要没有明确停止跟踪,则会一直跟踪和更新其信息。可以定义多个track。参见:4.5.5 跟踪器 track</td></tr><tr><td>命令</td><td>use-zone&lt;shared-zone-type&gt;as &lt;zone-name&gt;</td></tr><tr><td>解释</td><td>将指定区域的副本附加到平台上,并命名为 &lt;zone-name&gt;。如果指定的区域没有定义姿态,则复制的区域使用平台的当前姿态。此命令可以根据需要重复使用。use-zone:这个命令用于将一个预定义的区域(zone)的副本附加到平台上,并为这个副本指定一个新的名称。如果预定义的区域没有指定姿态(pose),那么这个副本将使用平台当前的姿态。这对于在仿真中管理和复用区域非常有用。</td></tr><tr><td>命令</td><td>zone ...end-zone zone_set...end-zone_set</td></tr><tr><td>解释</td><td>zone 和 zone_set 子命令定义了:与平台姿态对齐的相对区域。保持静态姿态的相对区域。保持静态姿态的绝对区域。请参阅 zone 和 zone_set 以了解影响仿真行为的子命令。zone 和 zone_set:这些命令用于定义区域。区域可以是相对的(与平台姿态对齐或保持静态姿态)或绝对的(保持静态姿态)。这些区域可以用于模拟不同的行为和环境条件。参考:4.9 区域和区域集</td></tr><tr><td>命令</td><td>navigation.errors ...endjahcision errors</td></tr><tr><td>解释</td><td>navigation.errors 块提供了一种方法,用于定义平台认为其位置与实际位置之间的误差。请参阅 navigation.errors 以了解输入的描述。navigation.errors:这个块允许定义平台的导航误差,即平台认为自己所在的位置与实际位置之间的差异。这对于模拟导航系统的精度和误差非常重要。默认值:无导航误差。参考:4.10 导航误差 navigation Errors</td></tr><tr><td>命令</td><td>weapon_effects&lt;string-reference&gt;weapon_effects_type&lt;string-reference&gt;</td></tr><tr><td>解释</td><td>这些命令用于指定平台的武器效果。武器效果定义了武器在使用时的各种效果,如</td></tr><tr><td></td><td>爆炸、火焰等。这些效果通常在平台是WSF_EXPLICIT_WEapon类型时使用，这意味着平台本身就是一个明确的武器系统。
参考：3.8.6武器效能模型weapon effects</td></tr><tr><td>命令</td><td>sensor &lt;sensor-type&gt; sensor Commands … end_sensor</td></tr><tr><td>解释</td><td>指定平台传感器效果。可以添加多个传感器。
参考：-3.53.5传感器组件 sensor</td></tr><tr><td>命令</td><td>processor &lt;name&gt;&lt;base-type&gt; processor Commands … end Processor</td></tr><tr><td>解释</td><td>指定平台处理器效果。可以添加多个处理器。</td></tr></table>

平台脚本使用 4.1公共脚本接口 CommonScriptInterface的基本功能，而后扩展了自己个性化的脚本如下：

<table><tr><td>脚本</td><td>script void on DAMAGE_received() ... endScript</td></tr><tr><td>功能</td><td>这是一个可选脚本,可以定义在平台受到伤害时接管控制。这个脚本通常与destructible 或 on_broken 命令一起使用。通常,当平台受到伤害时,如果确定该伤害导致平台破损,平台将从仿真中移除。如果指定了destructible、on_broken disable 或 on_broken disabled但她_movable,平台将不会被删除,而是增加损伤因子(DamageFactor),并调用此脚本。脚本可以执行停止移动、关闭传感器、更改外观等操作。注意:如果指定了on_broken disable,平台的运动将停止,所有子系统将被设置为非操作状态,无需额外干预。如果指定了on_broken disabled但她_movable,平台的运动将继续,但所有子系统将被设置为非操作状态,无需额外干预。</td></tr><tr><td>脚本</td><td>script void onPLATFORM_deleted() ... endScript</td></tr><tr><td>功能</td><td>这是一个可选脚本,可以定义在平台从仿真中移除之前接管控制。</td></tr><tr><td>脚本</td><td>script void on-commander_deleted(WsfPlatform aCommander) ... endScript</td></tr><tr><td>功能</td><td>这是一个可选脚本,可以定义在平台的指挥链层级中的其他平台从仿真中移除之前执行。脚本的唯一参数是待移除平台的引用。</td></tr><tr><td>脚本</td><td>script void on_peer_deleted(WsfPlatform aPeer) ... endScript</td></tr><tr><td>功能</td><td>这是一个可选脚本,可以定义在平台的指挥链层级中的其他平台从仿真中移除之前执行。脚本的唯一参数是待移除平台的引用。</td></tr><tr><td>脚本</td><td>script void on_subordinate_deleted(WsfPlatform aSubordinate) ... endScript</td></tr><tr><td>功能</td><td>这是一个可选脚本,可以定义在平台的指挥链层级中的其他平台从仿真中移除之前执行。脚本的唯一参数是待移除平台的引用。</td></tr><tr><td>脚本</td><td>callback&lt;callback-name&gt;&lt;callback-type&gt; callback Commands end_callback</td></tr><tr><td>功能</td><td>回调是一个命名的动作,可以通过路线的 execute 命令在平台到达路线中的特定航点时调用。注意:这是一个已过时的形式,已被脚本取代。</td></tr></table>

# 3. 组件 Platform Part

组件是构成平台的重要组成部分。该部分定义了所有的组件以及其命令细节。除了每个组件特有的命令之外，大多数的组件都有公共的命令，在 3.1 公共命令中进行定义，具体哪个组件中包含了公共命令中的哪些部分，则会在各组件中进行说明。

在官方文档中，以下属于组件：

comm   
processor   
router   
sensor   
mover   
fuel   
weapon   
uci_component

以上组件分别在本章的分小节中进行依次描述。

# 3.1. 公共命令

# 3.1.1. 组件命令 Platform Part Commands

<table><tr><td>命令</td><td>automatic_recovery_time &lt;时间值&gt;</td></tr><tr><td>解释</td><td>定义从损坏状态1.0(完全损坏)到排队恢复之间的时间。只有在时间设定为正值并且部件被声明为可恢复时才有效。时间经过后,会调用部件的Resurrect()虚方法。默认值:0(不使用)</td></tr><tr><td>命令</td><td>aux_data ... aux_data Commands ... end(aux_data</td></tr><tr><td>解释</td><td>定义对象的辅助数据。有关定义辅助数据的语法,请参阅aux_data命令。参考:4.6辅助数据aux_data</td></tr><tr><td>命令</td><td>category &lt;name&gt;</td></tr><tr><td>解释</td><td>声明对象属于指定类别。此命令可以多次指定,以表示对象属于多个类别。脚本语言方法 CategoryMemberOf(“*name*”)可以查询类别。</td></tr><tr><td>命令</td><td>clear_categories</td></tr><tr><td>解释</td><td>取消之前的所有类别命令。</td></tr><tr><td>命令</td><td>critical/nonCritical</td></tr><tr><td>解释</td><td>如果为关键组件且损坏程度达到1.0(损坏),平台将从模拟中移除。默认值:non-critical(非关键)</td></tr><tr><td>命令</td><td>damage_factor &lt;unit-value&gt;</td></tr><tr><td>解释</td><td>组件的初始损坏系数。0表示无损坏,1.0表示完全损坏(功能性损坏)。如果损坏系数为1.0,必须将其降低到0之前,组件才能恢复运行,但non_resurrectible状态会阻止这一点。外部实体或效应可能影响损坏水平。组件的实现方式决定其操作如何响应非零损坏系数。默认值:0.0</td></tr><tr><td>命令</td><td>clear_internallinks</td></tr><tr><td>解释</td><td>移除所有当前定义的由internal_link或processor命令定义的内部链接。这在想要对现有平台定义进行一些修改时非常有用。</td></tr><tr><td>命令</td><td>internal_link&lt;platform-part-name&gt;processor&lt;platform-part-name&gt;</td></tr><tr><td>解释</td><td>指定来自此对象的消息应路由到同一平台上的指定平台组件对象。此命令可以多次指定,以将消息路由到多个接收者。&lt;platform-part-name&gt;可以是以下之一:平台上的处理器名称。平台上的通信设备名称。平台上的传感器设备名称。字符串 mover表示接收者是平台上的移动装置对象。字符串fuel表示接收者是平台上的燃料对象。</td></tr><tr><td></td><td>目前,只有第一种形式(接收者为处理器)正在使用。目前,由未分类WSF核心实现的平台组件不支持接收消息,因此链接到它们不会执行任何有用的功能。</td></tr><tr><td>命令</td><td>debug / no debug</td></tr><tr><td>解释</td><td>启用或禁用对象的调试。启用对象调试的实际效果是实现特定的。通常,会有大量信息写入标准输出,为了控制显示的信息,可以使用debug_level。默认值: noDebug (不启用调试)</td></tr><tr><td>命令</td><td>debug_level &lt;level&gt;</td></tr><tr><td>解释</td><td>指定调试级别,范围为[1,3]。每个级别通常提供不同类型或数量的调试信息显示到标准输出。还需要设置debug。启用对象调试级别的实际效果是实现特定的。默认值:3</td></tr><tr><td>命令</td><td>group_join &lt;group-name&gt;/&lt;group Leave &lt;group-name&gt;</td></tr><tr><td>解释</td><td>将平台添加到指定组或从指定组移除。</td></tr><tr><td>命令</td><td>is_type_of &lt;type-name&gt;</td></tr><tr><td>解释</td><td>对象的类型层次结构通常由对象继承的对象定义。此命令允许定义对象也属于指定类型。</td></tr><tr><td>命令</td><td>broken</td></tr><tr><td>解释</td><td>声明组件不可操作,完全损坏,不可恢复。功能上等同于同时将损坏系数设置为1.0、不可恢复和不可操作。该组件不能修复。默认值:functional (可操作)</td></tr><tr><td>命令</td><td>off / on</td></tr><tr><td>解释</td><td>定义对象的初始状态为关闭或开启。默认值:取决于对象类型。通常为“开启”,但传感器为“关闭”。</td></tr><tr><td>命令</td><td>operational/non-operational</td></tr><tr><td>解释</td><td>定义对象的操作状态。可操作的对象可以关闭和开启,并用于操作。不可操作的对象在变为可操作之前不能使用。默认值:operational (可操作)</td></tr><tr><td>命令</td><td>restorable/non Restorable</td></tr><tr><td>解释</td><td>定义组件从损坏系数=1.0中恢复的能力。如果不可恢复,组件损坏状态将固定为1.0。默认值:restorable (可恢复)</td></tr></table>

# 3.1.2. 可动部件命令 Articulated Part Commands

注意：本节仅作为各种命令的参考。这些命令指定了通信和传感子系统相对于其所在平台的位置和方向。它们还指定了部件在响应指向请求（cue）时可以旋转的自由度和限制。如果请求指向设备超出旋转限制，结果将尽可能接近限制而不超出。

<table><tr><td>命令</td><td>location &lt;x 长度值&gt;&lt;y 长度值&gt;&lt;z 长度值&gt;&lt;长度单位&gt;</td></tr><tr><td>解释</td><td>指定关节部件相对于实体坐标系原点的位置。默认值: 000 米</td></tr><tr><td>命令</td><td>yaw &lt;角度值&gt;</td></tr><tr><td>解释</td><td>指定关节部件相对于其附着实体的偏航角。默认值: 0.0 度</td></tr><tr><td>命令</td><td>pitch &lt;角度值&gt;</td></tr><tr><td>解释</td><td>指定关节部件相对于其附着实体的俯仰角。默认值: 0.0 度注意: 此命令不得用于指定绕垂直轴旋转系统(如预警雷达或固定仰角炮塔发射器)的倾斜角。对于传感器,请使用 antenna_tilt 命令或 beam_tilt 命令块中的 beam_tilt 命令;对于发射器,请使用下面的 tilt 命令。</td></tr><tr><td>命令</td><td>roll &lt;角度值&gt;</td></tr><tr><td>解释</td><td>指定关节部件相对于其附着实体的滚转角。默认值: 0.0 度</td></tr><tr><td>命令</td><td>tilt &lt;角度值&gt;</td></tr><tr><td>解释</td><td>用于指定可以在方位角上指向的发射器的固定仰角。详见 pitch 命令中的说明。</td></tr><tr><td>命令</td><td>slew_mode [fixed | azimuth | elevation | both | azimuth_and_elevation]</td></tr><tr><td>解释</td><td>旋转模式(及相应的限制)定义了子系统响应指向请求的能力。如果系统未被指向,则其方向由 yaw、pitch 和 roll 指定。</td></tr><tr><td></td><td>fixed - 系统不能被指向。 azimuth - 系统只能在方位角上被指向。角度限制由 azimuth_slew_limits 定义。 elevation - 系统只能在仰角上被指向。角度限制由 elevation_slew_limits 定义。 both 或 azimuth_and_elevation - 系统可以在方位角和仰角上被指向。角度限制由 azimuth_slew_limits 和 elevation_slew_limits 定义。 默认值: fixed</td></tr><tr><td>命令</td><td>azimuth_slew_limits &lt;最小角度值&gt;&lt;最大角度值&gt;</td></tr><tr><td>解释</td><td>指定子系统在方位角上可以旋转的绝对最小和最大角度,用于指向和扫描。限制在部件坐标系(PCS)中指定。如果旋转模式为 azimuth 或 both,则这些表示明确指向请求的方位角限制。默认值:-180 度到 180 度</td></tr><tr><td>命令</td><td>elevation_slew_limits &lt;最小角度值&gt;&lt;最大角度值&gt;</td></tr><tr><td>解释</td><td>指定子系统在仰角上可以旋转的最小和最大角度,用于指向和扫描。限制在部件坐标系(PCS)中指定。如果旋转模式为 elevation 或 both,则这些表示明确指向请求的仰角限制。默认值:-90 度到 90 度</td></tr><tr><td>命令</td><td>azimuth_slew_rate &lt;角速度值&gt;elevation_slew_rate &lt;角速度值&gt;</td></tr><tr><td>解释</td><td>指定满足指向请求时旋转部件的角速度。这主要用于模拟跟踪或指向单个目标的系统,如机械跟踪器或炮系统。不用于扫描系统,也不应用于多目标跟踪系统。值必须大于零,且大于或等于1.0E+12度/秒的值将被视为“无限”。默认值:无限(瞬时旋转)</td></tr><tr><td>命令</td><td>slew_method [ independent | coordinated ]</td></tr><tr><td>解释</td><td>如果使用非无限旋转速率,此命令指定旋转操作的中间步骤如何进行。如果指定为independent,则每个方向在时间间隔内的移动量将独立确定,这意味着一个方向可能会比另一个方向先达到其目标值。如果指定为coordinated,则速率将调整,使方位角和仰角值同时达到目标值。默认值: independent</td></tr><tr><td>命令</td><td>masking_pattern &lt;masking-pattern-name&gt;</td></tr><tr><td>解释</td><td>指定由全局masking_pattern 命令定义的遮蔽模式名称。遮蔽模式是用于模拟平台结构元素遮挡的机制。详见全局masking_pattern 命令。默认值:无遮蔽模式</td></tr></table>

# 3.2. 通信组件 comm

# 3.2.1. 公共命令 comm commands

```txt
comm <name-or-type> <base-type-name>
... Platform Part Commands ...
... Articulated Part Commands ...
... protocol Commands ...
... medium Commands ...
# Common Device Characteristic Commands
transmit_mode [ intermittent | continuous ]
modifier_category <category-name>
# Common Datalink Commands
channels <integer-value>
queue_type [fifo |IFO |priority ] 
```

```txt
queue_limit <queue-limit>   
purge_interval <time-value>   
retransmit Attempts <integer-value>   
retransmit_delay <time-value>   
# Common Router Association Commands   
router_name <router-name>   
gateway <platform-name> <comm-name>   
# Common Network Addressing Commands   
network_name [ <network-name> | <local:master> | <local:slave>]   
network_address <address>   
address <address>   
link <platform-name> <comm-name>   
local_link <comm-name>   
link_address <address>   
# Common Physical Layer Commands   
propagation_speed <random-speed-reference>   
transfer_rate <random-data-rate-reference>   
packet_loss_time <random-time-reference>   
# Frequency Selection Commands   
frequency_select_delay <time-value>   
end_comm 
```

通信设备对象代表在平台之间发送消息的设备。以下命令适用于所有通信设备，但不是所有通信模型都使用这些命令，路由器特定命令也不一定在所有协议实现中使用。

上述中的：

Platform Part Commands 是在：3.1.1 组件命令 Platform Part Commands 中定义。

Articulated Part Commands 是在：3.1.2 可动部件命令 Articulated Part Commands 中定义。

剩余的命令在剩下的小节中分别介绍。

# 3.2.1.1. 协议命令 protocol Commands

全局上下文命令

```txt
protocol <name-or-type> <base-type-name>  
...  
end_protocol 
```

通信和通信类型范围命令

```txt
add protocol <name-or-type><base-type-name>  
...  
end_protocol  
edit protocol <name>  
...  
end_protocol  
delete protocol <name> end_protocol 
```

概述

协议（commprotocol） 是对特定通信能力的抽象表示。它可以提供或限制常规的功能，并可能改变与之相关的通信层进程。在通信模型 OSI7 层实现的逻辑中定义的任何活动，都可以在协议 API 的范围内进行修改。

在 AFSIM 的通信模型中，每一层在正常通信操作期间，会查询接收/发送协议栈中所有附加的协议，给予每个协议修改消息处理执行的机会。

更一般地说，这允许将能力定义在通信对象之外，并由用户根据需要添加或删除。可以定义任意数量的协议类型，但每种类型只能使用一个。假设每个协议彼此兼容（取决于实现），它们可以在一定程度上协作工作（即，多种传输层协议不能同时控制消息如何拆分成数据包；其中一个必须是主要的）。

需要注意的是，每个通信对象应该只有一个同类型的协议。在当前版本的 AFSIM 中，默认情况下不使用任何协议。

关键点总结

协议是通信能力的抽象表示。  
可以在通信模型的每一层修改消息处理。  
用户可以根据需要添加或删除协议。  
每种类型的协议只能使用一个，且默认情况下不使用任何协议。

# 3.2.1.1.1.1.1. 组播协议模型 WSF_COMM_PROTOCOL_IGMP

```txt
protocol <name> WSFCOMM.PROTOCOL_IGMP  
joinMULTicast_group <address>  
leaveMULTicast_group <address>  
level_0MULTicast  
level_1MULTicast  
level_2MULTicast  
join_delay <random-time-reference>  
leave_delay <random-time-reference>  
end_protocol 
```

WSF_COMM_PROTOCOL_IGMP 是一个组播协议，用于在网络中进行组播通信。它允许设备加入和离开组播组，并定义了不同的组播能力级别（从没有组播支持到完全组播支持）。此协议需要与其他路由协议一起使用，因为它本身不提供路由功能。使用时需注意延迟设置（join_delay 和 leave_delay），这些设置会影响网络中组播通信的效率和准确性。

WSF_COMM_PROTOCOL_IGMP 是在 AFSIM 中提供的基本组播功能的模拟。此协议不是

路由协议，不能确定传送到任何给定目的地或组的正确路径或能力，因此必须与其他启用的路由协议（例如传统协议）一起使用才能成功使用。

组播协议允许通信加入由适当范围内的地址（224.0.0.0 到 239.255.255.255）指定的组播组。然后，任何对该地址的后续传输将由任何其他启用组播的路由器适当地传递到适当的目的地，从而限制生成的消息数量。

请注意，发送组播不仅需要发送者提供此协议，还需要接收者以及任何可能路由组播消息的其他通信设备。其他未启用组播的通信设备将简单地“丢弃”消息，因为它们无法将地址解析为适当的目的地。

<table><tr><td>命令</td><td>joinMULTicast_group&lt;address&gt;</td></tr><tr><td>解释</td><td>将此通信设备添加到指定的组播组。任何发送到此地址的消息将尝试传递消息给此通信设备,假设没有路由失败。</td></tr><tr><td>命令</td><td>leaveMULTicast_group&lt;address&gt;</td></tr><tr><td>解释</td><td>将此通信设备从指定的组播组中移除。专门用于允许从派生通信设备中移除指定的组播组。</td></tr><tr><td>命令</td><td>level_0MULTicast</td></tr><tr><td>解释</td><td>表示此组播协议实例为类型 0 ,表示没有实际的组播支持。</td></tr><tr><td>命令</td><td>level_1MULTicast</td></tr><tr><td>解释</td><td>表示此组播协议实例为类型 1 ,表示此通信设备能够发送组播消息,但不能接收它们。</td></tr><tr><td>命令</td><td>level_2MULTicast</td></tr><tr><td>解释</td><td>表示此组播协议实例为类型 2 ,表示此通信设备具有完全的组播功能,既可以发送也可以接收组播消息。这是此协议的默认设置。</td></tr><tr><td>命令</td><td>join_delay&lt;random-time-reference&gt;</td></tr><tr><td>解释</td><td>指定加入组播组所需的时间,用于更高级的网络特性建模。这也可能影响使用组播的其他协议(如OSPF)的功能,因为组播组数据在路由器之间的传播会延迟。未来加入和离开组播组的脚本功能计划将受到此值的影响。默认值为常量 0 脚本。</td></tr><tr><td>命令</td><td>leave_delay&lt;random-time-reference&gt;</td></tr><tr><td>解释</td><td>指定离开组播组所需的时间,用于更高级的网络特性建模。这也可能影响使用组播的其他协议(如OSPF)的功能,因为组播组数据在路由器之间的传播会延迟。未来加入和离开组播组的脚本功能计划将受到此值的影响。</td></tr></table>

# 3.2.1.2. 媒介命令 medium Commands

```txt
medium <name-or-type><base-type-name> channels <integer-value> default_mode_name <mode-name> use_sharing <boolean-value> mode <mode-name> ... end_mode script string ModeOnTransmit ...   
end_medium 
```

添加一个 medium 到有效的通信框架对象

```txt
comm <name> <type> # or edit comm <name>  
add medium <type>  
...  
end_medium  
end_comm 
```

在有效的通信框架对象上编辑一个 medium 对象

```txt
router <name> <type> # or edit router <name>edit medium <type>  
...  
end_medium  
end_ROUTer 
```

在有效的通信框架对象上删除一个 medium 对象：

```txt
comm <name> <type> # or edit comm <name> delete medium <type> end_comm 
```

注意：删除 medium 会用该对象的默认 medium 类型及默认设置替换现有定义。

概述

在 AFSIM中，medium 是一种对象，代表通信设备将数据传播到另一通信设备的方式。Medium 提供了一种可定义的用户类型，可被 AFSIM通信框架中的各种对象利用。Medium定义了其实现对通信施加的限制，这些限制与使用该 medium 的通信模型所定义的限制相协同。例如，即使通信设备可以利用最大传输速率，该速率也可能会被所使用的 medium 或medium 的其他动态特性（如复用中使用的信道数量）进一步限制。

Medium 在 AFSIM 中是独特的，因为它们可以在多个通信对象之间共享。因此，使用共享 medium 的每个通信设备都受到该 medium 限制的约束。例如，四个通信设备共享一个medium，该 medium 有四个可用传输信道。如果一个通信设备使用了所有四个信道，其他通信设备在一个或多个信道可用之前无法进行传输。特定的模型可能会根据干扰、拥塞等概念实施其自身的限制。

由于 medium 是共享对象，只能在全局上下文中定义。任何特定于通信对象（如路由器或通信设备）的 medium 使用必须引用在全局上下文中定义的 medium，并且只通过其类型名称引用此 medium。

Medium 还可以包含多种模式，表示与该 medium 相关的不同状态。使用 AFSIM脚本语言，可以在运行时修改任何传输的状态，以提供动态方法更改传输特性。虽然 AFSIM 中的任何对象都仅限于一个 medium 对象，但该 medium 可以有任意数量的可用模式。

<table><tr><td>命令</td><td>channels &lt;integer-value&gt;</td></tr><tr><td>解释</td><td>定义 medium 可用的信道数量,也就是说,是否支持复用。信道数量决定了该 medium 可以处理的并发传输的数量,以及随后利用该 medium 的所有通信对象的并发传输数量。默认值:最大整数值(没有并发传输数量的限制)</td></tr><tr><td>命令</td><td>default_mode_name &lt;mode-name&gt;</td></tr><tr><td>解释</td><td>指定该 medium 上传输的默认模式。每个 medium 都有一个名为“default”的默认模式,使用默认值。除非使用此命令,否则在典型的 medium 处理期间将使用“default”模式。需要注意的是,可以通过使用 mode 命令显式定义“default”模式来修改默</td></tr><tr><td></td><td>认模式。
默认值：使用“default”模式</td></tr><tr><td>命令</td><td>use_sharingboolean-value&gt;</td></tr><tr><td>解释</td><td>默认情况下，medium 在每个引用特定全局定义 medium 类型的对象之间共享。如果指示 use_sharing 为 false，那么每次使用此 medium 类型定义将实例化其自身实例。这允许类型定义作为每个实例的简单模板，而避免共享实际 medium 本身。
默认值：true（medium 是共享的）</td></tr><tr><td>命令</td><td>mode end mode</td></tr><tr><td>解释</td><td>mode 命令用于定义该 medium 的单个模式。可以重复多次，但每个模式必须具有唯一的字符串名称。任何给定模式的实际命令由所使用的 medium 类型确定。
注意：每个 medium 都有一个“default”模式。任何在 mode 块之外使用的典型模式命令都引用“default”模式。</td></tr><tr><td>脚本</td><td>script string ModeOnTransmit(WsfCommMessage aMessage, WsfComm aTransmitter, WsfComm aReceiver) ... end script</td></tr><tr><td>功能</td><td>定义一个可选的脚本方法，每次尝试通过该 medium 传输消息时都会调用。用户可以通过返回模式的字符串标识符来指定该 medium 上的传输模式。
返回空字符串或不存在的模式名称时，该 medium 将使用当前指定的默认模式进行消息传输。</td></tr></table>

# 3.2.1.2.1.通用引导型媒介模型 WSF_COMM_MEDIUM_GUIDED

```ruby
medium <name> WSFCOMM_MEDIUM GUIDED ... medium Commands ... propagation_speed <random-speed-reference> transfer_rate <random-data-rate-reference> packet_loss_time <random-time-reference> mode <mode-name> propagation_speed <random-speed-reference> transfer_rate <random-data-rate-reference> packet_loss_time <random-time-reference> end_mode   
end_medium 
```

WSF_COMM_MEDIUM_GUIDED 是一种通用的引导型 medium 类型。引导型 medium 有时也称为有界或有线 medium。这种 medium 提供了通常与以前版本的 AFSIM 中引导通信框架对象相关的基本 medium 功能。

这种 medium 类型适用于 AFSIM 核心中的以下通信对象模型：

WSF_COMM_RCVR   
WSF_COMM_XMTR   
WSF_COMM_TRANSCEIVER   
WSF_COMM_ROUTER

# 军事特定

这种 medium 类型适用于 wsf_mil 中的以下通信模型：

WSF_JTIDS_TERMINAL

注意：删除 medium 会用该对象的默认 medium 类型及默认设置替换现有定义。

<table><tr><td>命令</td><td>propagation_speed &lt;random-speed-reference&gt;</td></tr><tr><td>解释</td><td>设置消息传播速度。当此命令在 mode 块之外定义时,指定与该 medium 关联的 “default” 模式的传播速度。默认值: c(光速常数)</td></tr><tr><td>命令</td><td>transfer_rate &lt;random-data-rate-reference&gt;</td></tr><tr><td>解释</td><td>设置该 medium 在设定时间内可以传输的数据量。当此命令在 mode 块之外定义时,指定与该 medium 关联的 “default” 模式的传输速率。默认值: -1 (瞬时传输)</td></tr><tr><td>命令</td><td>packet_loss_time &lt;random-time-reference&gt;</td></tr><tr><td>解释</td><td>设置每次通过该 medium 传输时增加的延迟时间。虽然表示为由于数据包丢失导致的延迟,但此值可用于引入任何原因的正常传输时间延迟,或作为模拟多种传输延迟源的总延迟。当此命令在 mode 块之外定义时,指定与该 medium 关联的 “default” 模式的数据包丢失时间。默认值: 0 (无延迟)</td></tr><tr><td>命令</td><td>mode &lt;mode-name&gt;..end_mode</td></tr><tr><td>解释</td><td>mode 命令用于定义该 medium 的单个模式。可以重复多次,但每个模式必须具有唯一的字符串名称。任何给定模式的实际命令由所使用的 medium 类型确定。注意:每个 medium 都有一个 “default” 模式。任何在 mode 块之外使用的典型模式命令都引用 “default” 模式。</td></tr></table>

# 3.2.1.2.2.通用非引导型媒介模型 WSF_COMM_MEDIUM_UNGUIDED

```txt
medium <name> WSFCOMM_MEDIUM_UNGUIDED ... medium Commands ... ... WSFCOMM_MEDIUM.GuidED Commands snr_transfer_rate_table ... bit_error(probability ... error Correction ... bit_error_rate ebno_table ... mode <mode-name> ... WSFCOMM_MEDIUM.GuidED Commands snr_transfer_rate_table ... bit_error(probability ... errorCorrection ... bit_error_rate ebno_table ... end_mode   
end_medium 
```

WSF_COMM_MEDIUM_UNGUIDED 是一种通用的非引导型 medium 类型。非引导型medium 是一种不受物理介质限制的 medium，通常与使用电磁辐射传输信号相关。这种medium 类型提供了在以前版本的 AFSIM 中常见的非引导 medium 的通用规范。

这种 medium 类型适用于 AFSIM 核心中的以下通信对象模型：

WSF_RADIO_RCVR   
WSF_RADIO_XMTR   
WSF_RADIO_TRANSCEIVER   
WSF_COMM_ROUTER

注意：目前，路由器不允许基于硬件定义发射器或接收器。对于路由器使用非引导medium，将使用发起消息的通信设备的发射器/接收器功能。

# 军事特定

这种 medium 类型适用于 wsf_mil 中的以下通信模型：

WSF_SUBSURFACE_RADIO_RCVR   
WSF_SUBSURFACE_RADIO_XMTR   
WSF_SUBSURFACE_RADIO_TRANSCEIVER   
WSF_LASER_RCVR   
WSF_LASER_XMTR   
WSF_LASER_TRANSCEIVER

注意：删除 medium 会用该对象的默认 medium 类型及默认设置替换现有定义。

<table><tr><td>命令</td><td>snr_transfer_rate_table &lt;absolute-units&gt;&lt;data-rate-units&gt;&lt;SNR-value 1&gt; &lt;transfer-rate-value 1&gt; ... end snr_transfer_rate_table</td></tr><tr><td>解释</td><td>指定一个将信噪比(SNR)值映射到消息传输速率的表格。SNR-Transfer-Rate表将进行插值。如果指定了表格,表格中的传输速率值将覆盖使用 transfer_rate 命令指定的值。注意:SNR传输速率表与Eb/No vs BER 表互斥。最后指定的将被使用。默认值:无示例snr_transfer_rate_tabledB bit/s0 1001 1002 903 804 405 2055 1070 1end snr_transfer_rate_table</td></tr><tr><td>命令</td><td>bit_error(probability &lt;real-value&gt;</td></tr><tr><td>解释</td><td>可选参数,定义系统设计的比特错误率概率。用于从Eb/No vs BER 表中选择Eb/No值。必须大于或等于零。默认值:0.0</td></tr><tr><td>命令</td><td>error Correction &lt;real-value&gt;</td></tr><tr><td>解释</td><td>可选参数,确定在使用Eb/No计算数据速率时应用的错误校正量。必须在0.0和1.0之间。单位假定为dB。默认值:0 dB</td></tr><tr><td>命令</td><td>bit_error_rate ebno table &lt;absolute-units&gt;&lt;ratio-units&gt;&lt;BER-value 1&gt; &lt;Eb/No-value 1&gt; ... end bit error rate ebno table</td></tr><tr><td>解释</td><td>可选表格,定义比特能量与谐噪声密度(Eb/No)与比特错误率(BER)之间的关系。与bit_error(probability 和 errorCorrection 结合使用,以计算medium上的数据传输速率。使用此表时,数据速率 = SNR * 错误校正 *(带宽 / Eb/No)。比特错误率-EbNo</td></tr><tr><td></td><td>表将进行插值。如果指定了表格,表格中的传输速率值将覆盖使用 transfer_rate 命令指定的值。注意:表格中的值的单位是可选的,如果未输入,假定 BER 为无单位,Eb/No 为 dB。注意:Eb/No vs BER 表与 SNR 传输速率表互斥。最后指定的将被使用。默认值:无示例bit_error_rate ebno_table0.00000001 120.0000001 11.30.000001 10.30.00001 9.50.0001 8.30.001 6.50.01 4.30.1 0end_bit_error_rate ebno_table</td></tr><tr><td>命令</td><td>mode &lt;mode-name&gt;..end_mode</td></tr><tr><td>解释</td><td>mode 命令用于定义该 medium 的单个模式。可以重复多次,但每个模式必须具有唯一的字符串名称。任何给定模式的实际命令由所使用的 medium 类型确定。注意:每个 medium 都有一个“default”模式。任何在 mode 块之外使用的典型模式命令都引用“default”模式。</td></tr></table>

# 3.2.1.3. 网络命令 network

```txt
network <name> <base-type> network_address ... end_network 
```

在 AFSIM （ Advanced Framework for Simulation, Integration, and Modeling ） 中 ， 使 用network 命令来定义用户指定的网络。除非在场景输入中使用此命令显式实例化，否则网络会由 AFSIM 中的通信定义自动生成。所有由 network 命令定义的网络都会被实例化，并通过网络名称或提供的网络地址来分配通信设备。如果未为网络提供特定地址，则将动态分配一个地址，CIDR 值为 24，可以分配给 254 个通信对象。

脚本类 WsfNetwork

```vue
network network <name> <base-type> 
```

定义一个网络，其名称为 <name>，基础类型为 <base-type>。

```txt
network_address network_address <address> 
```

如果指定了此命令，就会将网络分配到所提供的地址。可分配的对象数量也将由地址的 CIDR值定义。为此网络提供的地址不得与其他网络或保留地址冲突。

概述

network 命令 在 AFSIM 通信环境中定义一个用户指定的网络。网络会自动由 AFSIM中

的通信定义生成，除非通过使用此命令显式实例化。在使用网络名称或一个地址（如果为网络提供了一个地址）来分配通信设备时，所有由 network 命令定义的网络都会被实例化并可用。如果未为网络提供特定地址，则将被分配一个动态地址，其 CIDR 值为 24，可分配给254 个通信对象。

命令

network_address <address>

如果指定了此命令，将网络分配到提供的地址。可分配到此地址的对象数量也将由地址的 CIDR 值定义。为此网络提供的地址不得与任何其他网络或保留地址冲突。

# 3.2.1.3.1. AD_HOC 网络模型 WSF_COMM_NETWORK_AD_HOC

```txt
network <name> WSFCOMM_NETWORK_AD_HOC  
... network Commands ...  
... WSFCOMM_NETWORKGENERIC commands ...  
update_rate <random-time-reference>  
comm_updateRates  
    member <platform-name> <comm-name> update_rate <random-time-reference>  
end_comm_updateRates  
remove_comm_update_rate <platform-name> <comm-name>  
address_updateRates  
    member <address> update_rate <random-time-reference>  
end_address_updateRates  
remove_address_update_rate <address>  
end_network 
```

在 AFSIM 中，WSF_COMM_NETWORK_AD_HOC 是一种动态网络类型。

这种网络类型与 WSF_COMM_NETWORK_GENERIC 类似，不指定拓扑结构。然而，与用户定义链路状态的静态网络不同，这种网络类型会在运行时根据其成员的潜在通信能力自动修改其拓扑结构。这完全由通信模型的实现驱动，决定了任何个体通信设备是否可以与其他通信设备进行通信。

在运行时，按照用户指定的时间间隔，网络中的每个通信设备会创建与网络中其他可通信设备的链接，并主动移除与不可用通信设备的链接。因此，网络状态可能会根据每个通信模型的实现不断修改。

这种网络类型主要用于通信模型实现中具有更严格控制或限制通信能力的情况，而不是假设总是能够与类似模型通信的完美或有线通信模型（例如，WSF_COMM_TRANSCEIVER），这些模型在同质模型网络中会有效地形成一个网状网络。

在此网络中，每个通信设备的更新期间，仅检查和可能修改传出的状态。

此网络类型中仅修改网络内部的链接。外部网络链接不予考虑。

警告：由于每个接口在每个时间间隔检查网络中的每个其他接口，这种网络类型可能会成为性能问题。建议用户尽可能限制此网络中的通信设备数量，并使用允许的最大更新速率以适应其使用情况。

命令

update_rate <random-time-reference>

指定此网络将通过创建和移除链接来更新网络状态的速率。网络中没有特定更新速率的通信设备将使用此速率。

建议如果在单个模拟中使用多个此类型的网络，应使用适当的分布而不是恒定值，以避免所有网络同时更新。

如果用户未指定此值，则使用此更新速率的任何通信设备在模拟期间将不会自动更新。这在希望在网络中混合动态和静态链路规范时很有用。

默认值：最大浮点值（在模拟期间不会发生更新）

comm_update_rates … end_comm_update_rates

此块允许用户为特定通信接口指定唯一的更新速率，由平台名称和通信名称指定。以这种方式指定更新速率的任何通信接口将使用此更新速率来修改该接口的传出链接，而不是通过 update_rate 指定的一般更新速率。

此命令对于在适用的情况下增加或减少特定成员的更新速率很有用，这样任何单个通信接口不必决定整个网络的一般更新速率，从而可能导致性能问题。

remove_comm_update_rate <platform-name> <comm-name>

移除由平台和通信名称指定的通信设备的唯一更新速率条目。将指定的通信设备设置为使用通过 update_rate 命令分配的一般更新速率。

此命令可用于移除特定通信更新速率，特别是对于派生网络类型。

address_update_rates … end_address_update_rates

此块允许用户为特定通信接口指定唯一的更新速率，由通信接口地址指定。以这种方式指定更新速率的任何通信接口将使用此更新速率来修改该接口的传出链接，而不是通过update_rate 指定的一般更新速率。

此命令对于在适用的情况下增加或减少特定成员的更新速率很有用，这样任何单个通信接口不必决定整个网络的一般更新速率，从而可能导致性能问题。

remove_address_update_rate <address>

移除由通信地址指定的通信设备的唯一更新速率条目。将指定的通信设备设置为使用通过 update_rate 命令分配的一般更新速率。

此命令可用于移除特定通信更新速率，特别是对于派生网络类型。

# 3.2.1.3.2. 环形拓扑网络模型 WSF_COMM_NETWORK_DIRECTED_RING

```txt
network <name> WSFCOMM_NETWORK_DIRECTED_RING ... network Commands ... comm_list member <string-value><string-value> end_comm_list 
```

```ruby
address_list member <address-value> end_address_list end_network 
```

WSF_COMM_NETWORK_DIRECTED_RING 提供了一种强制环形拓扑的通用网络。在这个网络中，所有成员都是有序的，每个成员都有一个来自更高序通信对象的传入链接，以及一个指向更低序通信对象的传出链接。因此，这个网络只允许消息沿环的一个方向传递。

此网络要求至少提供三个成员才能创建链接。排序通过 comm_list 和 address_list 中定义的成员隐含实现，其中通过地址指定的通信设备（如果适用）按输入顺序排列，接着是通过平台/通信名称指定的通信设备。最后一个有序成员链接到第一个成员以完成环。

命令

comm_list … end_comm_list

可以通过识别通信对象的所属平台名称和通信名称来指定此网络的成员。此列表中的每个条目都以“member”命令为前缀。

address_list … end_address_list

可以通过识别通信对象的地址来指定此网络的成员。此列表中的每个条目都以“member”命令为前缀。此列表仅适用于在输入中指定了地址的通信对象，因为未指定地址的通信设备将在运行时动态分配。

# 3.2.1.3.3. 通用网络模型 WSF_COMM_NETWORK_GENERIC

```txt
network <name> WSFCOMM_NETWORKGENERIC  
... network Commands ...  
comm_list  
    member <string-value> <string-value>  
    ...  
end_comm_list  
address_list  
    member <address-value>  
    ...  
end_address_list  
comm_link_list  
    link <string-value> <string-value> <string-value> <string-value>  
    ...  
end_comm_link_list  
address_link_list  
    link <address-value> <address-value> 
```

```txt
end_address_link_list end_network 
```

WSF_COMM_NETWORK_GENERIC 提供了一种通用网络，除了必须在现有网络成员之间建立链接外，没有特定的网络实现规则。此网络中的链接完全由指定的连接定义，允许自定义网络拓扑。需要注意的是，即使在此网络中指定了通信设备之间的链接，也不保证这些通信对象由于类型差异或不兼容性而能够相互通信。

命令

comm_list … end_comm_list

可以通过识别通信对象的所属平台名称和通信名称来指定此网络的成员。此列表中的每个条目都以“member”命令为前缀。

address_list … end_address_list

可以通过识别通信对象的地址来指定此网络的成员。此列表中的每个条目都以“member”命令为前缀。此列表仅适用于在输入中指定了地址的通信对象，因为未指定地址的通信设备将在运行时动态分配。

comm_link_list … end_comm_link_list

指定由其所属平台名称和通信名称表示的通信对象之间的链接，作为方向对。指定的顺序很重要，因为链接仅从第一个指定的通信设备创建到第二个指定的通信设备。此列表中的每个条目都以“link”命令为前缀。

address_link_list … end_address_link_list

指定由其地址定义的通信对象之间的链接。指定的顺序很重要，因为链接仅从第一个指定的地址创建到第二个。此列表中的每个条目都以“link”命令为前缀。

# 3.2.1.3.4. 全双向通信网格模型 WSF_COMM_NETWORK_MESH

```txt
network <name> WSFCOMM_NETWORK_MESH  
... network Commands ...  
comm_list  
member <string-value> <string-value>  
...  
end_comm_list  
address_list  
member <address-value>  
...  
end_address_list  
end_network 
```

WSF_COMM_NETWORK_MESH 提供了一种强制网状拓扑的通用网络。在这个网络中，只需指定成员，所有成员之间都有双向通信链接。这意味着每个成员都可以与其他所有成员进行通信。

命令

comm_list … end_comm_list

可以通过识别通信对象的所属平台名称和通信名称来指定此网络的成员。此列表中的每个条目都以“member”命令为前缀。

address_list … end_address_list

可以通过识别通信对象的地址来指定此网络的成员。此列表中的每个条目都以“member”命令为前缀。此列表仅适用于在输入中指定了地址的通信对象，因为未指定地址的通信设备将在运行时动态分配。

概述

网状网络（MeshNetwork）是一种局域网拓扑结构，其中基础设施节点（如桥接器、交换机和其他基础设施设备）直接、动态且非层次化地连接到尽可能多的其他节点，并相互协作以有效地路由数据。在 WSF_COMM_NETWORK_MESH 中，这种拓扑结构确保所有成员之间的通信是双向的，形成一个完全互联的网络。

这种网络类型适用于需要高冗余和可靠性的场景，因为每个节点都与多个其他节点连接，从而提高了网络的弹性和数据传输的可靠性。

# 3.2.1.3.5. 严格通信网络模型 WSF_COMM_NETWORK_MESH_LEGACY

```txt
network <name> WSFCOMM_NETWORK_MESH_LEGACY ... network Commands ... comm_list member <string-value> <string-value> end_comm_list address_list member <address-value> ... end_address_list end_network 
```

WSF_COMM_NETWORK_MESH_LEGACY 提供了一种通用网络，强制采用网状拓扑。在这个网络中，只需指定成员。与标准网状网络不同，此网络仅在网络创建时在能够相互通信的对象之间创建链接。例如，两个基于无线电的通信设备如果不在通信距离内，将不会在网络中创建初始链接。

此网络对象是 AFSIM早期版本中的默认网络实现。当未指定其他网络对象时，AFSIM中默认创建的网络继续使用此网络对象。

命令

comm_list … end_comm_list

可以通过识别通信对象的所属平台名称和通信名称来指定此网络的成员。此列表中的每个条目都以“member”命令为前缀。

address_list … end_address_list

可以通过识别通信对象的地址来指定此网络的成员。此列表中的每个条目都以“member”命令为前缀。此列表仅适用于在输入中指定了地址的通信对象，因为未指定地址的通信设备将在运行时动态分配。

概述

WSF_COMM_NETWORK_MESH_LEGACY 是一种网状网络类型，强调在网络创建时的通信能力。它确保只有在创建时能够相互通信的成员之间才会建立链接。这种方法适用于需要考虑通信范围和能力的场景，确保网络的实际通信能力与其拓扑结构一致。

这种网络类型在 AFSIM 的早期版本中作为默认实现，继续在未指定其他网络类型时使用。

# 3.2.1.3.6. P2P 网络拓扑网格模型 WSF_COMM_NETWORK_P2P

```txt
network <name> WSFCOMM_NETWORK_P2P ... network Commands ... comm_list member <string-value><string-value> end_comm_list address_list member <address-value> end_address_list end_network 
```

WSF_COMM_NETWORK_P2P 提供了一种通用网络，强制采用点对点（Point-to-Point）拓扑。在这个网络中，只能存在两个通信设备，并且它们之间具有双向通信能力。

命令

comm_list … end_comm_list

可以通过识别通信对象的所属平台名称和通信名称来指定此网络的成员。此列表中的每个条目都以“member”命令为前缀。

address_list … end_address_list

可以通过识别通信对象的地址来指定此网络的成员。此列表中的每个条目都以“member”命令为前缀。此列表仅适用于在输入中指定了地址的通信对象，因为未指定地址的通信设备将在运行时动态分配。

概述

点对点网络（P2P）是一种网络拓扑结构，其中两个设备直接连接并进行通信。在WSF_COMM_NETWORK_P2P 中，这种拓扑结构确保只有两个成员，并且它们之间的通信是双向的。这种网络类型适用于需要简单、直接连接的场景，例如两个设备之间的专用通信通道。

这种网络类型在需要严格控制通信路径和参与设备数量的情况下非常有用，确保通信的安全性和可靠性。

# 3.2.1.3.7. 环形网络模型 WSF_COMM_NETWORK_RING

```txt
network <name> WSFCOMM_NETWORK_RING ... network Commands ... comm_list member <string-value> <string-value> end_comm_list address_list member <address-value> end_address_list end_network 
```

WSF_COMM_NETWORK_RING 提供了一种通用网络，强制采用环形拓扑。在这个网络中，所有成员都是有序的，每个成员与其邻居有双向链接。因此，此网络要求至少提供三个成员才能创建链接。排序通过 comm_list 和 address_list 中定义的成员隐含实现，其中通过地址指定的通信设备（如果适用）按输入顺序排列，接着是通过平台/通信名称指定的通信设备。第一个和最后一个有序成员相互链接以完成环形拓扑。

命令

comm_list … end_comm_list

可以通过识别通信对象的所属平台名称和通信名称来指定此网络的成员。此列表中的每个条目都以“member”命令为前缀。

address_list … end_address_list

可以通过识别通信对象的地址来指定此网络的成员。此列表中的每个条目都以“member”命令为前缀。此列表仅适用于在输入中指定了地址的通信对象，因为未指定地址的通信设备将在运行时动态分配。

概述

环形网络（RingNetwork）是一种网络拓扑结构，其中每个节点连接到正好两个其他节点，形成一个单一的连续信号路径——一个环。数据从节点传递到节点，每个节点沿途处理每个数据包。在 WSF_COMM_NETWORK_RING 中，这种拓扑结构确保所有成员之间的通信是双向的，形成一个完整的环形连接。

这种网络类型适用于需要确保所有节点之间有直接路径的场景，提供了一种简单而有效的方式来管理网络通信。

# 3.2.1.3.8. 星形拓扑网络模型 WSF_COMM_NETWORK_STAR

```txt
network <name> WSFCOMM_NETWORK_STAR ... network Commands ... 
```

```txt
comm_list member string-value>string-value> end_comm_list address_list member <address-value> end_address_list hubnamed string-value> string-value> hub_address <address-value>   
end_network 
```

WSF_COMM_NETWORK_STAR 提供了一种通用网络，强制采用星形拓扑。在这个网络中，一个通信对象被指定为“中心”（hub），网络中的所有其他成员仅与“中心”通信对象有双向链接。这保证了网络中任何成员之间最多只有两跳。需要注意的是，如果在此网络中未指定中心，则不会创建任何链接。

命令

comm_list … end_comm_list

可以通过识别通信对象的所属平台名称和通信名称来指定此网络的成员。此列表中的每个条目都以“member”命令为前缀。

address_list … end_address_list

可以通过识别通信对象的地址来指定此网络的成员。此列表中的每个条目都以“member”命令为前缀。此列表仅适用于在输入中指定了地址的通信对象，因为未指定地址的通信设备将在运行时动态分配。

hub_named <string-value> <string-value>

通过其所属平台名称和通信名称指定星形网络的中心通信对象。此中心必须是网络的成员。

hub_address <address-value>

通过其地址指定星形网络的中心通信对象。此中心必须是网络的成员。

概述

星形网络（StarNetwork）是一种网络拓扑结构，其中所有节点都连接到一个中央节点（中心）。在 WSF_COMM_NETWORK_STAR 中，这种拓扑结构确保所有成员与中心节点之间的通信是双向的，形成一个以中心为核心的连接结构。这种网络类型适用于需要集中管理和控制的场景，提供了一种简单而有效的方式来管理网络通信。

# 3.2.1.4. 其它公共命令

# 通用设备特征命令

<table><tr><td>命令</td><td>transmit_mode[间歇性|连续性]</td></tr><tr><td>解释</td><td>定义设备是间歇性发送还是连续性发送。目前仅适用于通过无线电波发送的设备(例如,WSF无线电收发器)。间歇性表示设备仅在实际传输消息时才辐射。连续性表示设备只要“开启”就一直辐射。连续性模式用于模拟电视或广播电台等系统。默认:间歇性</td></tr><tr><td>命令</td><td>modifier_category&lt;类别名称&gt;</td></tr><tr><td>解释</td><td>映射到zone_set中定义的衰减值的类别。设置此值告诉通信设备评估区域的衰减情况。</td></tr></table>

# 通用数据链路命令

<table><tr><td>命令</td><td>channels &lt;整数值&gt;</td></tr><tr><td>解释</td><td>指定此通信设备可用的频道数。该值表示通信设备根据其硬件定义支持的同时传输数量（多路复用）。数据链路层使用该值确定要转发到物理层进行传输的并发消息数量。默认：1个频道</td></tr><tr><td>命令</td><td>queue_type [fifo |IFO |priority]</td></tr><tr><td>解释</td><td>指定设备传输队列的排队方法。fifo（先进先出）lifo（后进先出）priority（最高优先级优先）默认：fifo</td></tr><tr><td>命令</td><td>queue_limit &lt;队列限制&gt;</td></tr><tr><td>解释</td><td>指定传输队列的最大大小。如果队列增长到最大大小，后续消息将被丢弃。默认：-1（无限）</td></tr><tr><td>命令</td><td>purge_interval &lt;时间值&gt;</td></tr><tr><td>解释</td><td>表示消息将从队列中移除（丢弃）的时间段。当队列开始充满待传输消息时，这个值将用于确定消息保留多久后被移除。默认：0（不清除消息）</td></tr><tr><td>命令</td><td>retransmit Attempts &lt;整数值&gt;</td></tr><tr><td>解释</td><td>表示消息在从队列中被清除（丢弃）之前尝试传输的次数。默认：0（不重试传输）</td></tr><tr><td>命令</td><td>retransmit_delay &lt;时间值&gt;</td></tr><tr><td>解释</td><td>表示在前一次传输失败后等待的时间量。使用此值时要注意 purge_interval，如果purge_interval比retransmit_delay短，消息可能在重试之前被清除。默认：0（无重试延迟）</td></tr></table>

# 通用网络地址命令

这些命令用于定义通信设备的地址。地址还定义了通信对象的网络成员资格。这些命令还可以定义通信对象与其他通信对象之间的连接，以便消息路由。是否支持显式和静态链接命令取决于协议实现。

<table><tr><td>命令</td><td>network_name [&lt;网络名称&gt; | local-master | local:slave]</td></tr><tr><td>解释</td><td>定义该设备所属的网络名称。网络名称是直接映射到一个用于生成32位IPv4地址的字符串。使用IPv4并不意味着AFSIM仅支持基于IP的通信,它只是一个内部一致的方法来标识仿真中的所有通信对象。</td></tr><tr><td>命令</td><td>network_address &lt;地址&gt;</td></tr><tr><td>解释</td><td>定义设备的网络地址。如果提供的地址属于现有网络,此通信设备将加入该网络,并被提供当前网络中未分配的最低地址。如果地址未被网络管理,将根据父平台和通信名称创建一个网络,并添加此通信设备到第一个可用地址。</td></tr><tr><td>命令</td><td>address &lt;地址&gt;</td></tr><tr><td>解释</td><td>address命令为该通信设备指定一个特定的用户提供的地址。如果地址由网络管理,该通信设备将加入该网络,否则将基于拥有该通信设备的平台名称和通信设备名称创建一个新网络。</td></tr><tr><td>命令</td><td>link&lt;平台名称&gt;&lt;通信名称&gt;</td></tr><tr><td>解释</td><td>此命令在该通信设备与指定设备之间提供通信链接。任何给定通信对象上可以定义任意数量的链接。</td></tr><tr><td>命令</td><td>local_link&lt;通信名称&gt;</td></tr><tr><td>解释</td><td>此命令等同于同一平台上的 link 命令。因此，仅需通信名称即可建立该链接。</td></tr><tr><td>命令</td><td>link_address&lt;地址&gt;</td></tr><tr><td>解释</td><td>此命令执行与 link 命令相同的操作，但使用特定地址创建链接。</td></tr></table>

# 通用路由器关联命令

<table><tr><td>命令</td><td>router_name&lt;路由器名称&gt;</td></tr><tr><td>解释</td><td>指定此通信接口分配给的路由器名称。路由器必须位于与通信设备相同的平台实例上。
默认：使用AFSIM中每个平台实例上可用的默认路由器</td></tr><tr><td>命令</td><td>gateway&lt;平台名称&gt;&lt;通信名称&gt;</td></tr><tr><td>解释</td><td>指定用于此通信实例的网关的远程接口。</td></tr></table>

# 通用物理层命令

<table><tr><td>命令</td><td>propagation_speed &lt;随机速度参考&gt;</td></tr><tr><td>解释</td><td>设置消息传播速度。此命令定义与该通信设备关联的介质的传播速度。
默认: c(光速常数)</td></tr><tr><td>命令</td><td>transfer_rate &lt;随机数据速率参考&gt;</td></tr><tr><td>解释</td><td>设置通信设备在设定时间内可以传输的数据量。任何未初始化的 transfer_rate 值在大多数通信实现中被解释为即时传输。
默认: -1 (即时传输)</td></tr><tr><td>命令</td><td>packet_loss_time &lt;随机时间参考&gt;</td></tr><tr><td>解释</td><td>设置每次传输的延迟时间。尽管表示由于数据包丢失的延迟,此值可以用于引入任何原因的传输延迟。</td></tr></table>

# 频率选择命令

<table><tr><td>命令</td><td>frequency_select_delay &lt;时间值&gt;</td></tr><tr><td>解释</td><td>指定在选择发射器上定义的备用频率时的延迟。
默认：0.0秒</td></tr></table>

# 干扰检测命令

```txt
comm <name-or-type> <base-type-name> # Jamming Detection Commands jamming_perception_timeout <time-value> jamming_perception_threshold <ratio> continuous_jamming_perception_threshold <ratio> pulsed_jamming_perception_threshold <ratio> coherent_jamming_perception_threshold <ratio> end_comm 
```

<table><tr><td>命令</td><td>jamming_perception_timeout &lt;时间值&gt;</td></tr><tr><td>解释</td><td>指定感知到的干扰不再感知后经过的时间。</td></tr><tr><td>命令</td><td>jamming_perception_threshold &lt;比率&gt; continuous_jamming_perception_threshold &lt;比率 &gt; pulsed_jamming_perception_threshold &lt;比率 &gt; coherent_jamming_perception_threshold &lt;比率&gt;</td></tr><tr><td>解释</td><td>指定操作员感知干扰的最小阈值。默认: 380 dB</td></tr></table>

# 3.2.2. 有线收发模型

# 3.2.2.1. 有线仅发送模型 WSF_COMM_XMTR

# 3.2.2.2. 有线仅接收模型 WSF_COMM_RCVR

# 3.2.2.3. 有线收发模型 WSF_COMM_TRANSCEIVER

```txt
comm <name-or-type> WSFCOMM_TRANSEIVER | WSFCOMM XMTR | WSFCOMM_RCVR ... Platform Part Commands ... ... Articulated Part Commands ... ... comm Commands ... end_comm 
```

WSF_COMM_TRANSCEIVER 提供了一个基础的完美/有线实现，能够进行发送和接收。如果通信设备只需要发送或接收，可以使用 WSF_COMM_XMTR（仅发送）和WSF_COMM_RCVR（仅接收）类型。这两种类型是 WSF_COMM_TRANSCEIVER 类型的特例，因此共享相同的命令。

这是 AFSIM 中通信的基础能力模型，除了 comm 命令中提供的典型功能外，没有额外的能力。可以看到其也没有特有命令，其命令使用的都是通信组件或组件的公有命令。

# 3.2.3. 无线电收发模型

# 3.2.3.1. 无线电仅发送模型 WSF_RADIO_XMTR

# 3.2.3.2. 无线电仅接收模型 WSF_RADIO_RCVR

# 3.2.3.3. 无线电收发模型 WSF_RADIO_TRANSCEIVER

```txt
comm <name-or-type> WSF_RADIO_TRANSEIVER | WSF_RADIO_XMTR | WSF_RADIO_RCVR ... Platform Part Commands ... ... Articulated Part Commands ... ... Antenna Commands ... ... comm Commands ... ... transmitter ... end_transmitter ... receiver ... end Receiver snr_transfer_rate_table ... bit_error(probability ... error Correction ... bit_error_rate ebno_table ... end_comm 
```

WSF_RADIO_TRANSCEIVER 提供了一个基本的无线电实现，能够使用发射器和接收器进行发送和接收。如果通信设备只需要发送或接收，可以使用 WSF_RADIO_XMTR 和WSF_RADIO_RCVR 类型。这两种类型是 WSF_RADIO_TRANSCEIVER 类型的特例，因此共享

以下命令部分中列出的相同命令。

<table><tr><td>命令</td><td>snr_transfer_rate_table &lt;绝对单位&gt;&lt;数据速率单位&gt;&lt;SNR值 1&gt;&lt;传输速率值 1&gt;...end_snr_transfer_rate_table</td></tr><tr><td>解释</td><td>指定一个将信噪比值映射到消息传输速率的表。SNR-Transfer-Rate 表将进行插值。如果指定了表格,表格传输速率值将覆盖使用 transfer_rate 命令指定的值。注意:SNR 传输速率表与 Eb/No 对 BER 表互斥。最后指定的将被使用。默认值:无示例snr_transfer_rate_tabledB bit/s0 1001 1002 903 804 405 2055 1070 1end_snr_transfer_rate_table</td></tr><tr><td>命令</td><td>bit_error(probability &lt;实数值&gt;</td></tr><tr><td>解释</td><td>可选参数,定义系统设计的比特错误率概率。用于从 Eb/No 对 BER 表中选择Eb/No 值。必须大于或等于零。默认值:0.0</td></tr><tr><td>命令</td><td>error Correction &lt;dbratio 值&gt;</td></tr><tr><td>解释</td><td>可选参数,确定在使用 Eb/No 计算数据速率时将应用多少错误校正。必须在 0.0 和1.0 之间。默认值:0 dB</td></tr><tr><td>命令</td><td>bit_error_rate ebno_table &lt;绝对单位&gt;&lt;比率单位&gt;&lt;BER 值 1&gt;&lt;Eb/No 值 1&gt; ...end_bit_error_rate ebno_table</td></tr><tr><td>解释</td><td>可选表,定义比特能量与谱噪声密度(Eb/No)对比特错误率(BER)。与bit_error(probability 和 errorCorrection 一起使用,以计算无线电的数据传输速率。使用此表时,数据速率 = SNR * 错误校正 *(带宽 / Eb/No)。Bit-Error-Rate-EbNo-Table 将进行插值。如果指定了表格,表格传输速率值将覆盖使用 transfer_rate 命令指定的值。注意:表中值的单位是可选的,如果未输入,则假定 BER 为无单位,Eb/No 为 dB。注意:Eb/No 对 BER 表与 SNR 传输速率表互斥。最后指定的将被使用。默认值:无示例bit_error_rate ebno_table0.00000001 120.00000001 11.30.0000001 10.30.000001 9.50.0001 8.30.001 6.50.01 4.30.1 0end_bit_error_rate ebno_table</td></tr></table>

# 3.2.4. 联合战术信息分发模型 WSF_JTIDS_TERMINAL

JTIDS 的全称是 Joint Tactical Information Distribution System，即联合战术信息分发系统

```txt
comm <name-or-type> WSF_JTIDS_TERMAL
... Platform Part Commands ...
... Articulated Part Commands ...
... Antenna Commands ...
... comm Commands ...
... transmitter ... end_transmitter
... receiver ... end_receiver
... WSF_JTIDS_TERMAL Commands ...
slot_group <group-name>
... WSF_JTIDS_TERMAL Slot Group Commands ...
end_slot_group
relay_slot_group
... WSF_JTIDS_TERMAL Slot Group Commands ...
endrelay_slot_group
end_comm 
```

WSF_JTIDS_TERMINAL 是一种模拟在 JTIDS 网络上传输数据的实现。它不模拟消息内容或脉冲级特性。当前的 JTIDS 终端实现主要来源于阅读《Understanding Link-16; a Guidebookfor New Users (Logicon, Inc.)》和 NATO STANAG 5516。它通过仅需要时隙组每帧所需的时隙数量来模拟网络容量。它不需要（也不允许）通过实际时隙块定义来定义网络（当前结构将允许在未来实现）。该模型还允许更改基本的网络时隙参数（每时隙比特数、每时隙秒数、每帧时隙数），以便模拟可能使用 JTIDSTDMA 架构但进行了一些修改的未来概念。

当前模型实现了：

多个网络  
每时隙组打包限制   
配对时隙中继  
专用访问   
中继中的时隙重用（洪水中继）  
模型尚未实现：  
争用访问   
时隙重新分配访问  
重新发布的中继

注意：这不是一个 Link-16 模型——它没有明确模拟 J 系列消息。这留给更高层次的东西来处理。它实际上只是模拟消息的物理传输。

<table><tr><td>命令</td><td>error Correction &lt;bratio 值&gt;</td></tr><tr><td>解释</td><td>可选参数,确定在使用 Eb/No 计算数据速率时将应用多少错误校正。必须在 0.0 和 1.0 之间。 默认值: 0 dB</td></tr><tr><td>命令</td><td>command chain &lt;命令链名称&gt;&lt;时隙组名称&gt;</td></tr><tr><td>解释</td><td>将命令链名称映射到时隙组名称,允许平台根据其命令链形成时隙组。</td></tr><tr><td>命令</td><td>maximum_range&lt;长度值&gt;</td></tr><tr><td>解释</td><td>定义接收器和发射器之间的最大范围。此值将覆盖在天线块中明确定义的任何最大范围。对于JTIDS终端，正常范围为300海里，扩展范围为500海里。所有在同一网络中的JTIDS单元应具有相同的范围设置；然而，该模型不强制执行此限制。默认值：300海里</td></tr></table>

以下值纯粹是可选的，提供了一种模拟未来系统的方法。这些命令必须在创建时隙组的命令之前指定：

<table><tr><td>命令</td><td>time_per_slot &lt;时间值&gt;</td></tr><tr><td>解释</td><td>覆盖每个时隙的时间量。
默认值：7.8125毫秒</td></tr><tr><td>命令</td><td>slot_size &lt;数据大小值&gt;</td></tr><tr><td>解释</td><td>覆盖在一个时隙中可以包含的数据量（在“正常”打包密度下）。
默认值：210比特</td></tr><tr><td>命令</td><td>sets_per_frame &lt;整数值&gt;</td></tr><tr><td>解释</td><td>覆盖每帧的交错集数。必须大于零。
默认值：3</td></tr><tr><td>命令</td><td>slots_per_set &lt;整数值&gt;</td></tr><tr><td>解释</td><td>覆盖每帧内每集的时隙数。必须大于一。
默认值：512</td></tr></table>

# 时隙组命令

<table><tr><td>命令</td><td>network&lt;整数值&gt;</td></tr><tr><td>解释</td><td>JTIDS网络编号,范围为[0,127]。默认值:0</td></tr><tr><td>命令</td><td>tsec&lt;整数值&gt;</td></tr><tr><td>解释</td><td>JTIDS加密变量,指定传输安全性(TSEC),范围为[0,127]。此模型不执行数据的加密/解密。此值用于Link-16消息头。默认值:0</td></tr><tr><td>命令</td><td>msec&lt;整数值&gt;</td></tr><tr><td>解释</td><td>JTIDS加密变量,指定消息安全性(MSEC),范围为[0,127]。此模型不执行数据的加密/解密。此值用于Link-16消息头。默认值:0</td></tr><tr><td>命令</td><td>queue_limit&lt;整数值&gt;</td></tr><tr><td>解释</td><td>最大传输队列大小,范围为[0,无限]。默认值:99999</td></tr><tr><td>命令</td><td>packing_limit[standard | p2sp | p2dp | p4sp]</td></tr><tr><td>解释</td><td>消息的打包格式,影响传输消息所需的时隙数量。在扩展范围模式(ERM)(即最大范围设置为500海里)中,JTIDS终端不支持p2dp和p4sp打包结构。此模型不强制执行此限制。standard:标准双脉冲(每时隙3x70比特)p2sp:打包-2单脉冲(每时隙6x70比特)p2dp:打包-2双脉冲(每时隙6x70比特)p4sp:打包-4单脉冲(每时隙12x70比特)默认值:standard</td></tr><tr><td>命令</td><td>relay_slot_offset&lt;整数值&gt;</td></tr><tr><td>解释</td><td>配对中继时隙组与源时隙组的偏移量。偏移量应在[1,无限]范围内。注意:JTIDS协议要求偏移量在[5,32]范围内。默认值:6</td></tr><tr><td>命令</td><td>npg&lt;整数值&gt;</td></tr><tr><td>解释</td><td>网络参与组。NPG可以是:1到511之间的整数以下之一:initial_entry,rtt_a,rtt_b,network_management,ppli_a,ppli_b,surveillance,</td></tr><tr><td></td><td>weapons_coordinates, air_control, electronic Warfare, unassigned, voice_a, voice_b, indirect_ppli, wc, fighter_to_fighter_dedicated, fighter_to_fighter_contention, engagement_coordinates, joint_ppli, distributed_network_management, residual_message, ijms_position, ijms_message 默认值: 0</td></tr></table>

使用以下三个命令来简化分配时隙块的方法：

<table><tr><td>命令</td><td>slots_per_frame&lt;整数值&gt;</td></tr><tr><td>解释</td><td>每帧时隙数提供了一种简化的分配TSBs的方法。每帧时隙数必须在[1,终端的每帧时隙数]范围内。
默认值:1</td></tr><tr><td>命令</td><td>per_unit Slots_per_frame&lt;整数值&gt;</td></tr><tr><td>解释</td><td>此时隙组每帧将使用的分数时隙数。
默认值:-1(默认情况下无影响)</td></tr><tr><td>命令</td><td>receive_only</td></tr><tr><td>解释</td><td>表示此时隙组只能接收。</td></tr></table>

使用以下两个命令来明确分配时隙块：

<table><tr><td>命令</td><td>receive_slot_block &lt;集&gt;&lt;索引&gt;&lt;/rrn&gt;</td></tr><tr><td>解释</td><td>使用指定的集（例如，A、B、C）、时隙索引和重复率编号（RRN）创建接收时隙块。重复率编号必须在[1,15]范围内。</td></tr><tr><td>命令</td><td>transmit_slot_block &lt;集&gt;&lt;索引&gt;&lt;/rrn&gt;</td></tr><tr><td>解释</td><td>使用指定的集（例如，A、B、C）、时隙索引和重复率编号（RRN）创建传输时隙块。重复率编号必须在[1,15]范围内。</td></tr></table>

# 3.2.5. 水下无线电收发模型

# 3.2.5.1. 水下无线电仅发送模型 WSF_SUBSURFACE_RADIO_XMTR

# 3.2.5.2. 水下无线电仅接收模型 WSF_SUBSURFACE_RADIO_RCVR

# 3.2.5.3. 水下无线电收发模型 WSF_SUBSURFACE_RADIO_TRANSCEIVER

```txt
comm <name-or-type> WSF_SUBSURFACE_RADIO_TRANSEIVER | WSF_SUBSURFACE_RADIO_XMTR | WSF_SUBSURFACE_RADIO_RCVR ... Platform Part Commands ... ... Articulated Part Commands ... ... Antenna Commands ... ... comm Commands ... ... WSFCOMM_TRANSEIVER Commands ... ... WSF_RADIO_TRANSEIVER Commands ... ... transmitter ... end_transmitter ... receiver ... endreceiver max_underwater_range_filter ... max_communication_depth ... minimum_horizon_angle ... set_VLF_comm ... unset_VLF_comm ... water_attenuation_factor... 
```

```txt
... WSF_SUBSURFACE_RADIO_TRANSEIVER Commands ... end_comm 
```

WSF_SUBSURFACE_RADIO_TRANSCEIVER 提供了一个基本的无线电实现，能够使用发射器 和 接收 器 进 行 发 送和 接 收 。 如果 通 信 设 备 只需 要 发 送 或接 收 ， 可 以 使用WSF_SUBSURFACE_RADIO_XMTR 和 WSF_SUBSURFACE_RADIO_RCVR 类型。这两种类型是WSF_SUBSURFACE_RADIO_TRANSCEIVER 类型的特例，因此共享以下命令部分中列出的相同命令。

WSF_SUBSURFACE_RADIO_TRANSCEIVER 从 WSF_RADAR_SENSOR 和WSF_COMM_TRANSCEIVER 继承，并接受父类的关键词。测试仅限于在空中平台和可以处于任何高度的第二个平台之间传递消息。使用更复杂的路由功能的行为尚未验证。

WSF_SUBSURFACE_RADIO_TRANSCEIVER 提供了一种通信选项，可以覆盖传统的地平线限制，以便与潜水艇进行模拟通信。大多数 WSF 传感器和通信系统设计用于地球表面以上的操作。因此，当发射器或接收器的高度值为零或更小时，通常会施加约束以停止传感或通信事件的进一步处理。当两个通信系统是 WSF_SUBSURFACE_RADIO_TRANSCEIVER 类型时，消息可以传递到地球表面以下的平台。

在这种单一通信类型中考虑了两种基本的通信方法——甚低频（VLF）和光学激光。这两种方法都旨在允许用户在模拟中实现通信“效果”。两者都没有高保真度来模拟波传播所涉及的物理现象。

VLF 通信模式导致几乎完美的通信，不受地平线或地形的限制。使用关键词set_VLF_comm 激活该模式。在 VLF 操作模式下，不会施加吸收、衰减或地平线角度限制的约束。

WSF_SUBSURFACE_RADIO_TRANSCEIVER 的 默 认 状 态 导 致 VLF 通 信 行 为 未 设 置（unset_VLF_comm），因此将施加一组路径约束。这些路径约束旨在提供激光通信系统效果的一致性。激光光能被水迅速吸收。水下路径长度（通常只有几百英尺）通常非常短。不幸的是，短的水下传输路径距离通常在许多用于任务级模拟的范围和地平线计算误差范围内。为了允许和限制通信事件，在非 VLF 操作时做了简化假设：

使用与球形地球表面相交的直线路径计算通过水的路径距离。此路径用于水下范围限制和水路径吸收效应。其余的斜距用于大气吸收效应。

该方法忽略了详细的折射效应，也忽略了能量穿透空气-水边界时的特定吸收和反射的相互作用。这些值目前在其他误差源的噪声范围内。因此，详细的激光工程级模型更适合研究这些特征。

假设传输距离由平台之间的球形一个地球半径地平线距离近似。如果包含地形模型，则允许地形阻挡路径中的空中部分。

用户可以使用关键词 minimum_horizon_angle 限制由入水角度限制引起的通信能力。此角度从地平线向上测量。低于此限制的角度的通信将被停止。其效果是要求平台减少其斜距以进行通信。

可以使用关键词 max_underwater_range_filter 限制不现实的长水下距离。默认情况下，此范围限制为 1000 米，用户可以根据需要增加或减少该值。此关键词还具有允许短距离通信而不考虑地平线或地形的附加效果。

<table><tr><td>命令</td><td>max_underwater_range_filter&lt;长度值&gt;</td></tr><tr><td>解释</td><td>通过为传输路径的水下部分指定范围约束来防止不现实的长水下距离。此关键词还具有允许短距离通信而不考虑地平线或地形的附加效果。</td></tr><tr><td></td><td>注意:除了基于水下路径长度限制范围外,用户还可以使用发射器或接收器块中的maximum_range关键词限制总范围。默认值:1000米</td></tr><tr><td>命令</td><td>max_communication_depth&lt;长度值&gt;</td></tr><tr><td>解释</td><td>指定潜水平台允许交换通信事件的最大深度。为了减少用户输入问题,使用数值输入的绝对值,并将该值转换为负高度以表示潜水平台的水下深度。默认值:负无穷大</td></tr><tr><td>命令</td><td>minimum_horizon_angle&lt;角度值&gt;</td></tr><tr><td>解释</td><td>指定通过水面传输的最小可接受角度。此角度从地平线向上测量。低于此限制的角度的通信将被停止。其效果是要求平台减少其斜距以进行通信。默认值:-90度</td></tr><tr><td>命令</td><td>set_VLF_comm
unset_VLF_comm</td></tr><tr><td>解释</td><td>当命令为 set_VLF_comm 时,所有地平线检查将被忽略,并且消息将被传递。默认值:unset_VLF_comm</td></tr><tr><td>命令</td><td>water_attenuation_factor&lt;dbratio 值&gt;/&lt;长度值&gt;</td></tr><tr><td>解释</td><td>指定信号在传输路径的水部分通过时衰减的因子。数据格式为数字后跟dB比率值,再跟一个反斜杠,然后跟一个&lt;长度值&gt;。默认:0.0 dB/m示例water_attenuation_factor 0.5 dB/m</td></tr></table>

# 示例

激活 VLF 通信选项：

```txt
comm VLFCOMM WSF_SUBSURFACE_RADIO_TRANSEIVER debug set_VLF_comm //禁用长距离通信的地平线检查 transmitter frequency 30.0 khz //power 10.0 kw //当前未对VLF模型进行S/N和干扰建模 end_transmitter receiver frequency 30.0 khz //maximum_range 500 km //可以限制VLF范围 end Receiver //max_communication_depth -400 ft //可以强制执行深度限制 end_comm 
```

使用默认的光学视距通信选项：

```txt
antenna_pattern UWCOM_ANENNA uniform_pattern minimum_gain 70.0 db end.uniform_pattern   
end_antenna_pattern   
commUWCOMMWSF_SUBSURFACE_RADIO_TRANSEIVER debug 
```

```txt
transmitter frequency 600000.0 ghz //注意：需要 'power' 值以启用衰减和干扰检查以计算 S/I power 1.0 kw antenna_pattern UWCOM_ANTENNA end_transmitter receiver frequency 600000.0 ghz antenna_pattern UWCOM_ANTENNA end Receiver water_attenuation_factor 0.3 dB/m //默认 = 0.0 dB/m minimum_horizon_angle 3.0 deg //默认 = -90 度 max_underwater_range_filter 400.0 m //默认 = 1000 米 max_communication_depth -200.0 m //默认 = 负无穷大  
end_comm 
```

# 3.2.6. 激光收发模型

# 3.2.6.1. 激光发送模型 WSF_LASER_XMTR

# 3.2.6.2. 激光接收模型 WSF_LASER_RCVR

# 3.2.6.3. 激光收发模型 WSF_LASER_TRANSCEIVER

```txt
comm <name-or-type> WSF_LASER_TRANSEIVER | WSF_LASER_XMTR | WSF_LASER_RCVR ... Platform Part Commands ... ... Articulated Part Commands ... ... Antenna Commands ... ... comm Commands ... ... transmitter ... standard transmitter commands ... laser transmitter commands ... end_transmitter ... receiver ... standard receiver commands ... laser receiver commands ... end_receiver ... atmospheric_structure ... attenuation ... attenuation_loss | attenuation_transmission_factor ... aero_optic_loss | aero_optic_transmission_factor ... turbulence_loss | turbulence_transmission_factor ... show_link-budget end_comm 
```

注意：WSF_LASER_XMTR 和 WSF_LASER_RCVR 是 WSF_LASER_TRANSCEIVER 的仅发射

和仅接收版本。

WSF_LASER_TRANSCEIVER 是一个激光通信模型，用于模拟采集时间、能量传播、数据传输速率和维持链路的能力。该模型接受激光通信系统设计方法中使用的典型输入，以便在任务级别测试特定的顶级系统设计。WSF_LASER_TRANSCEIVER 能够使用发射机和接收机进行发射和接收。如果通信设备仅需要发射或接收，可以使用 WSF_LASER_XMTR 和WSF_LASER_RCVR 类型。这两种类型是 WSF_LASER_TRANSCEIVER 类型的特例，因此共享命令部分中列出的相同命令。

如需更详细地了解 AFSIM 中的通信工作方式，请参阅《通信入门》。

注意：以下许多命令指定分数传输功率，或“损耗”（db）。这些值可以指定为分数或db 比率。对于分数输入，值应大于 0.0 且小于或等于 1.0；对于 db 比率输入，值应小于或等于零。

<table><tr><td>命令</td><td>aerooptic_loss &lt;db-ratio-value&gt;aerooptic_transmission_factor &lt;real-value&gt;</td></tr><tr><td>解释</td><td>指定通过湍流空气传输的激光能量的分数。默认值:1.0(0 db)</td></tr><tr><td>命令</td><td>atmospheric_structure &lt;hv57&gt;</td></tr><tr><td>解释</td><td>指定用于计算大气湍流(参考:4.11.2大气湍流模型 Turbulence model)的模型或Cn2函数,单位为m-2/3。默认值:&quot;hv57&quot;注意:当前仅有HV 5/7模型可用。</td></tr><tr><td>命令</td><td>attenuation &lt; attenuation_model name &gt;</td></tr><tr><td>解释</td><td>参考用于计算大气衰减的模型(通常是WSF_OPTICAL AttENUATION)。参考:3.5.5.7衰减模型 attenuation_model</td></tr><tr><td>命令</td><td>attenuation_loss &lt;db-ratio-value&gt;attenuation_transmission_factor &lt;real-value&gt;</td></tr><tr><td>解释</td><td>指定从发射机到接收机通过大气传输的激光能量损失的分数比例。默认值:1.0(0 db)</td></tr><tr><td>命令</td><td>background_radiance &lt;spectral-radiance-value&gt;</td></tr><tr><td>解释</td><td>在接收器孔径处指定背景光谱辐射。默认值:0.0瓦/平方米/立体弧度/米注意:WSF_LASER_XMTR会忽略该值。</td></tr><tr><td>命令</td><td>background_irradiance &lt;spectral-irradiance-value&gt;</td></tr><tr><td>解释</td><td>在接收器孔径处指定背景光谱辐照度。默认值:0.0瓦/平方米/米注意:WSF_LASER_XMTR会忽略该值。</td></tr><tr><td>命令</td><td>turbulence_loss &lt;db-ratio-value&gt;turbulence_transmission_factor &lt;real-value&gt;</td></tr><tr><td>解释</td><td>指定由于湍流损失的激光能量的分数。默认值:1.0(0 db)注意:注意:如果没有指定这两个命令中的任何一个,那么turbulence_loss将被计算为仅由衍射造成的光斑尺寸与由衍射和湍流造成的光斑尺寸之比。湍流引起的光束扩散采用AFSIM湍流模型计算(参考:4.11.2大气湍流模型Turbulence model),该模型使用提供的atmospheric_structure参数进行配置。</td></tr><tr><td>命令</td><td>show_link-budget &lt;boolean-value&gt;</td></tr><tr><td>解释</td><td>如果启用,则在消息传输时打印摘要链路预算。默认值:禁用</td></tr></table>

# 发射机参数

发射机模块包括标准发射机命令（3.5.5.8 发射机 transmitter）以及特定于该通信设备的

命令。WSF_LASER_TRANSCEIVER 使用的标准发射机命令如下：

波长(wavelength)：无默认值；必须指定。  
脉冲宽度(pulse_width)：无默认值；必须指定脉冲宽度、时隙宽度或时隙速率之一。   
衰减模型(attenuation_model)：指定用于计算大气衰减的模型（通常是WSF_OPTICAL_ATTENUATION）参考：3.5.5.7 衰减模型 attenuation_model。

特定于 WSF_LASER_TRANSCEIVER 的命令如下：

<table><tr><td>命令</td><td>show_link-budget</td></tr><tr><td>解释</td><td>如果启用,则在消息传输时打印摘要链路预算。默认值:禁用</td></tr><tr><td>命令</td><td>average_power</td></tr><tr><td>解释</td><td>描述:指定发射机的平均输出功率。发射机的峰值功率将根据调制类型的占空比计算。</td></tr><tr><td>命令</td><td>aperture_diameter</td></tr><tr><td>解释</td><td>描述:定义发射机的孔径直径。更改此参数会影响衍射引起的光束扩展,进而影响光束大小和能量密度。默认值:无默认值。必须指定 aperture_diameter或beamwidth之一。注意:当从beamwidth计算时,aperture_diameter定义为:aperture_diameter=4.0λ/πθd其中:λ为激光波长,θd为波束宽度。</td></tr><tr><td>命令</td><td>beamwidth</td></tr><tr><td>解释</td><td>描述:指定发射光束的波束宽度。默认值:无默认值。必须指定 aperture_diameter或beamwidth之一。注意:当从aperture_diameter计算时,beamwidth定义为:beamwidth=4.0λ/πD其中:λ为激光波长,D为波束宽度。</td></tr><tr><td>命令</td><td>modulation_type</td></tr><tr><td>解释</td><td>指定用于计算发射机数据传输速率和占空比的调制类型。默认值:ppm</td></tr><tr><td>命令</td><td>ppm_order</td></tr><tr><td>解释</td><td>描述:当使用ppm调制类型时,指定ppm顺序。此值必须大于或等于2,通常为2的幂(例如2、4、8、16)。默认值:16</td></tr><tr><td>命令</td><td>slot_rate</td></tr><tr><td>解释</td><td>指定每秒的通信时隙数量。注意:slot_width与pulse_width同义;但是,slot_rate不同于比特率或脉冲重复频率,因为这两者都依赖于调制类型。</td></tr><tr><td>命令</td><td>optics_transmission_factor</td></tr><tr><td>解释</td><td>定义通过发射机光学元件传输的激光光的分数,通常考虑光学元件的传输和反射损失。默认值:1.0(0 dB;无传输损失)</td></tr><tr><td>命令</td><td>wavefront_transmission_factor</td></tr><tr><td>解释</td><td>指定通过发射机光学路径的激光光的分数,作为波前误差的函数。默认值:1.0(0 dB;完美衍射极限光学)</td></tr><tr><td>命令</td><td>wavefront_error</td></tr><tr><td>解释</td><td>指定光学路径的波前误差,以波的分数表示。wavefront_transmission_factor根据以下公式计算:</td></tr><tr><td>命令</td><td>pointing_transmission_factor &lt;real-value&gt;pointing_loss &lt;db-ratio-value&gt;</td></tr><tr><td>解释</td><td>指定在考虑指向误差后传输的激光光量的分数。默认值:1.0(0分贝;无指向误差)</td></tr></table>

# 接收机命令

接收器可以建模为 PIN 光电二极管（默认检测增益为 1.0）或雪崩光电二极管（检测增益 $> 1 . 0$ ）。

接收器模块包括标准接收器命令（3.5.5.9 接收机 receiver），以及以下特定于该通信设备的命令：

<table><tr><td>命令</td><td>aperture_diameter &lt;长度值&gt;</td></tr><tr><td>解释</td><td>定义接收器(探测器)孔径的直径。默认值:无默认值。孔径直径是必需的。</td></tr><tr><td>命令</td><td>bandpass &lt;长度值&gt;</td></tr><tr><td>解释</td><td>指定传输到接收器的光学带通。通常是围绕发射器激光波长的一个非常窄的值。默认值:1纳米</td></tr><tr><td>命令</td><td>optics_transmission_factor &lt;实数值&gt;optics_loss &lt;分贝比值&gt;</td></tr><tr><td>解释</td><td>定义通过接收器光学系统传输的激光光量的分数。该因子通常考虑光学路径中的障碍物(例如,次镜)以及光学元件的传输和反射损失。默认值:1.0(0分贝;无传输损失)</td></tr><tr><td>命令</td><td>quantum_efficiency &lt;实数值&gt;</td></tr><tr><td>解释</td><td>入射信号光子转换为光电子的分数。默认值:1.0(100%效率)</td></tr><tr><td>命令</td><td>responsivity &lt;响应值&gt;</td></tr><tr><td>解释</td><td>作为原子效率的替代,响应度是每瓦入射功率产生的光电流安培数。它与原子效率的关系如下:η=Eλ/qR其中η是原子效率,Eλ=hc/λ是激光波长λ处的特征光子能量,q是电子电荷,R是响应度。默认值:从原子效率计算得出。</td></tr><tr><td>命令</td><td>detector_gain &lt;实数值&gt;</td></tr><tr><td>解释</td><td>探测器的增益。默认值:1.0</td></tr><tr><td>命令</td><td>circuit_temperature &lt;温度值&gt;circuit_capacitance &lt;电容值&gt;circuit_resistance &lt;电阻值&gt;</td></tr><tr><td>解释</td><td>这些是可选命令,用于计算热噪声成分,如下文的噪声计算部分所述。必须指定电路温度,以及电路电容或电路电阻之一。默认值:无</td></tr><tr><td>命令</td><td>dark_count_rate &lt;频率值&gt;dark_current &lt;电流值&gt;</td></tr><tr><td>解释</td><td>这些是可选命令,用于指定背景噪声成分中的放大“体”暗计数项,如下文的噪声计算部分所述。可以根据偏好指定其中之一。默认值:无</td></tr><tr><td>命令</td><td>excess_noise_factor &lt;实数值&gt;</td></tr><tr><td>解释</td><td>对于雪崩光电二极管(APD)接收器,指定由于非理想放大引起的过量噪声因子(增益值),用于计算放大噪声中的光电子。默认值:1.0(无额外影响)</td></tr><tr><td>命令</td><td>surface DARK_count_rate &lt;频率值&gt;surface DARK_current &lt;电流值&gt;</td></tr><tr><td>解释</td><td>这些是可选命令，用于指定背景噪声成分中的非放大或“表面”暗计数项，如下文的噪声计算部分所述。可以根据偏好指定其中之一。
默认值：无
注意：由于表面暗电流未被放大，因此在具有大增益的 APD 接收器中通常可以忽略。</td></tr></table>

# 调制类型

调制类型决定了发射器的占空比和数据传输速率。目前可用的调制类型如下：

开关键控 (On-Off Keying, OOK)：当发送 1 位时，在一个比特间隔内传输信号光子；当发送 0 位时，在一个比特间隔内不传输信号光子。  
脉冲位置调制 (Pulse Position Modulation, PPM)：对于给定的槽数 M，信号光子在 M个槽中的一个槽内传输。在每个符号周期内，传输 $\log _ { 2 }$ (?)位。因此 M 通常是 2的幂。注意:PPM 通常称为 M 元 PPM 或 M-PPM。当 $\mathsf { M } = 2$ 时，有时称为二进制PPM 或 B-PPM。  
二进制差分相移键控 (Binary Differential Phase Shift Keying, DPSK)：如果传输 1 位，则发射器载波相位在比特间隔之间偏移 180 度；如果传输 0 位，则没有相位偏移。

# 占空比和数据速率

给定定义的槽宽度 $t _ { s l o t }$ ，不同调制类型提供以下占空比和数据速率：

<table><tr><td>调制类型</td><td>占空比</td><td>数据速率（bps）</td></tr><tr><td>OOK</td><td>0.5</td><td>1/tslot</td></tr><tr><td>PPM</td><td>1/M</td><td>log2(M)/(Mtslot)</td></tr><tr><td>DPSK</td><td>0.5</td><td>1/tslot</td></tr></table>

这些调制类型在不同的应用场景中有不同的优缺点。例如，OOK 简单且易于实现，但在噪声环境中性能较差；PPM 在低信噪比条件下性能较好，但需要更复杂的接收器设计；DPSK 则在相位噪声较低的环境中表现优异。

# 激光脉冲接收功率的计算

接收激光功率的计算遵循光学链路方程：

$$
P _ {r} = P _ {t} G _ {t} L _ {t} L _ {R} L _ {a t m} G _ {r} L _ {r}
$$

请注意，“损耗”和“传输因子”这两个术语可以互换使用。通常，当这些因子以分贝形式相加时（它们是负值），使用“损耗”一词。上述方程没有使用分贝形式，而是将所有项相乘，在这种情况下，它们更适合被描述为“传输因子”。

其中：

$P _ { r }$ :接收信号功率。  
$P _ { t }$ :发射信号功率。  
$G _ { t }$ :有效发射天线增益。  
$L _ { t }$ :与发射器相关的效率损耗。   
$L _ { R }$ :自由空间范围损耗。   
$L _ { a t m }$ :与大气相关的损耗。   
$G _ { r }$ :接收天线增益。  
$L _ { r }$ :与接收器相关的效率损耗。