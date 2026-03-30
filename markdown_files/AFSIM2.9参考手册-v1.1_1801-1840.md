# UNCLASSIFIED

# 实践：下行消息

![](images/20cfcfb053cdbcf4270c03ecccdee4c9c48ed52bd1de69141971500bd0fcb509.jpg)

修改test_network.txt以确认临时网络（adhocnetwork）正在动态更新jacksonabad和NEARIDIUM卫星之间的链路。

在comm_sats.txt中包含test_network.txt。  
从NEARIDIUM的星间通信设备（消息发送端）发送消息。  
将消息发送到jacksonabad的上行通信设备（消息接收端）。  
运行您的解决方案。  
使用.evt输出文件或.aer输出文件检查您的结果。

<table><tr><td>10</td><td>// load the scenario</td></tr><tr><td>11</td><td>include_once nearidium_autogen.txt</td></tr><tr><td>12</td><td>include_once scenarios/floridistan.txt</td></tr><tr><td>13</td><td>include_once scripts/test_network.txt</td></tr><tr><td>14</td><td>include_once observers/draw/messages.txt</td></tr><tr><td>15</td><td></td></tr></table>

12 execute at_interval_of 1 min   
13 string source $=$ PickASatellite();   
14 string target $=$ "jacksonabad";#PickASatellite();   
15 # while (target $\equiv$ source)   
16 {   
17 # target $=$ PickASatellite();   
18 # }   
19   
20 writeln(TIME NOW,": send msg from ",source,"to",target);   
21   
22 WsfPlatform sender $=$ WsfSimulation.FindPlatform.source);   
23 WsfComm comm $=$ sender.Comm("crosslink");   
24 WsfControlMessage msg $=$ WsfControlMessage();   
25 #comm.SendMessage(msg,target,"crosslink");   
26 comm.SendMessage(msg,target,"uplink");   
27 end_execute

![](images/fc5b4214a7d67e251e3674571c727004aec40dc4798c080731853fdd45dcc3a0.jpg)

DISTRIBUTioNC.DistributionauthorizedtoU.S.GovernmentAgenciesandtheircontractors，11-Feb-2020.

Copyright  2020 Infoscitex, a DCS company Allrights reserved

Otherreguests forthisdocument shall bereferredtoAFRL/RQQD.

37

![](images/84068e4340360202d971251dad1bb32f57c0ee0bc2b6a7c24b3c2efe97524a96.jpg)

UNCLASSIFIED

# 图像卫星

![](images/45bc04bd6f146d64faefffa2fef15f46e74f30a46019fe97bcd21e83c92c9927.jpg)

·接下来，我们将添加一个Floridistani空间资产。  
·它需要以下内容：

一一个WSF_SPACE_MOVER，其轨道将该资产带到感兴趣的区域上空。  
－一个通信设备（NEARIDIUM_HANDHELD），用于通过临时网络（adhocnetwork）连接到卫星星座。  
一模拟消息发送的行为。

·这将作为一个多部分的练习完成。  
·在开始之前，请修改comm_sats.txt:

-不再包含 test_network.txt。  
－更新开始日期和时间。

<table><tr><td>9</td></tr><tr><td>10</td></tr><tr><td>11</td></tr><tr><td>12</td></tr><tr><td>13</td></tr><tr><td>14</td></tr><tr><td>15</td></tr></table>

<table><tr><td>32</td><td>start_date mar 23 2018</td></tr><tr><td>33</td><td>start_time 12:00:00.000</td></tr></table>

Step1（步骤1）：定义空间平台的轨道数据，使用tle/launch.txt文件来指定轨道参数。  
Step2（步骤2）：配置通信设备，使其能够连接到Nearidium网络；同时添加传感器，辅助可视化通信窗口，例如通信覆盖范围和时间。  
Step3（步骤3）：设置一个机制，使该平台能够定期向地面目标（jacksonabad）发送消息，模拟通信行为。

DISTRIBUTioNC.DistributionauthorizedtoU.S.GovernmentAgenciesandtheircontractors,11-Feb-2020.

Copyright  2o20 Infoscitex.a DCS company. Allrights reserved

Otherreguestsforthisdocument shallbereferredtoAFRL/RQQD

![](images/fb300e43464a37cd04b5d23d148c62d14bf539693420419a6a3c3c53e8316548.jpg)

# UNCLASSIFIED

# 图像卫星:实践

39

![](images/43e9589adb7179eec55dca66ad771c8bf9409959530d0364c309d785adf433c1.jpg)

Step1（步骤1）：定义空间平台的轨道数据，使用tle/launch.txt文件来指定轨道参数。

![](images/31294e90cae3e17c70dd2771462b15c8c08ceae1a5e1f6a57221c9a09edbc4d9.jpg)

Step2（步骤2）：配置通信设备，使其能够连接到Nearidium网络；同时添加传感器，辅助可视化通信窗口，例如通信覆盖范围和时间。

![](images/3429199c535ae2e8b5e9886b8005600f394a98a5c1a66dea772da9cef2a93ec7.jpg)

DISTRIBUTioNC.DistributionauthorizedtoU.S.GovernmentAgenciesandtheircontractors,11-Feb-2020.

Copyright  2020 Infoscitex, a DCS company Allrights reserved

Otherreguestsforthisdocument shallbereferredtoAFRL/RQQD

![](images/ba806eb1ae047453b6b26f35c3901d6ba8ce501a06ac68f77fa5f4fa85e6c67c.jpg)

# UNCLASSIFIED

# 图像卫星:实践

41

![](images/8446fe68e58348c7ec736fa933a8374fd93d5873a8bf8b66e8a2c1f297d0a1a9.jpg)

Step3（步骤3）：设置一个机制，使该平台能够定期向地面目标（jacksonabad）发送消息，模拟通信行为。

![](images/5667da41b2f3dab38039d1b80c312d9bdeeabce011c9b7c7bffa0cdf789fd6bc.jpg)

DISTRIBUTioNC.DistributionauthorizedtoU.S.GovernmentAgenciesandtheircontractors,11-Feb-2020.

Copyright  2020 Infoscitex, a DCS company. Allrights reserved

Otherreguestsforthisdocument shallbereferredtoAFRL/RQQD

![](images/ab920e5631e171fb76451215522c81b3514c4a9833a064d970634c4f1031cfed.jpg)

DISTRIBUTioNC.DistributionauthorizedtoU.S.GovernmentAgenciesandtheircontractors,11-Feb-2020.

Copyright  2o20 Infoscitex.a DCS company. Allrights reserved

Otherreguests forthisdocument shall bereferredtoAFRL/RQQD.

![](images/58f1f22ca11d676ef3a522be1541ed437dea5319b8259755d926419f6f1eef12.jpg)

# UNCLASSIFIED

# 问题

![](images/2b1536df6f41fd3ca9a481d6e75365003a9d47069415da43111d24232221f463.jpg)

![](images/12d7653ac5667f8a292e4f522c0cdb9cd2cf6477d1840994a3d779c607adad17.jpg)

# 6.1.9.3. 太空态势感知 3_Space_Situational_Awareness

# 6.1.9.3.1. 本节想定解析

本节想定资源在以下目录下：

afsim2.9_src\training\user\9_Space\scenarios\solution\3_space_situational_awareness\spa ce_situational_awareness.txt

![](images/2c2ee36b85f357eacce314f88656d3be87b2499b8ffd527bbdaf6bbb28c08002.jpg)

# 红方兵力

一个指挥所 red_command

▫ 其共有 4 个下属，两部太空围栏探测雷达 tripwire_1 和 2，两部跟踪雷达tracking_sensor_1 和 2  
▫ 当其收到太空围栏雷达传来的轨迹时，会将任务分配给跟踪雷达进行进一步跟踪

1 两部太空围栏探测雷达 tripwire_1 和 2  
▫ 每部太空围栏拥有两个传感器，探测后将目标上报给指挥所，仅上报一次

▪ 两部跟踪雷达 tripwire_1 和 2

▫ 每部雷达有一部传感器，正常时候关机，在收到指挥所的跟踪命令后开机跟踪

# 蓝方兵力

两个在轨目标

一个是编号为#133 的卫星  
□ 一个是其废弃的火箭助推器，他们都在太空中运动

# 6.1.9.3.2. 本节 PPT 资料

本文为 afsim2.9_src\training\user\9_Space\slides\3_Space_Situational_Awareness.pptx 的翻译。

![](images/e462a1d0c1439c26792d4caff99b35c6b5448207352f0c23edfa0ac8f55cd0b1.jpg)

Integrity ★Service★ Excellence

# AFSIM空间培训

# 3－太空态势感知(SSA)

13324598743

![](images/bbc4476562af254a57dfe039e3ff4888c0f16428ce6827f10a97d74b329f7bfa.jpg)

# AFRL/RQQD

# 美国空军研究实验室

DISTRIBUTioNC.Distributionauthorized to U.S.Government Agenciesand theircontractors,11-Feb-2020. OtherrequestsforthisdocumentshallbereferredtoAFRL/RQQD

1

![](images/e20d73e5d7fd4873a4bbbb314fa5e15e7f341c2ce04d9c935724a4074c943da4.jpg)

# UNCLASSIFIED

# 学习目标

![](images/eeab3f0e2d1959750e4abbe3a963593fbe2f5bdc71475d7ff54232745be559b2.jpg)

# ·包括以下内容：

一结合传感器测量数据以确定轨道要素（初始轨道确定，IOD）  
－利用传感器测量数据优化初始确定的轨道要素（轨道确定，OD）  
－配置轨迹管理器以启用IOD和OD  
-使用任务处理器和观察者回调来配置一个简单的指挥与控制系统

![](images/7b5805b384c12502ca06eea13aa20fa445b944e927142a60ab5a0617a068906a.jpg)

DISTRIBUTioNC.DistributionauthorizedtoU.S.GovernmentAgenciesandtheircontractors,11-Feb-2020. OtherrequestsforthisdocumentshallbereferredtoAFRL/RQQD

·一颗来自佛罗里达斯坦的卫星触发了奥瓦坎的"太空围栏”  
·太空围栏提供了初始轨道确定（IOD）。  
·奥瓦坎的跟踪传感器进一步提供了轨道确定（OD）。  
·你将需要完成以下任务：

一 配置太空围栏传感器。  
编写脚本以确保太空围栏的正常运行。  
－为初始轨道确定（IOD）和轨道确定（OD）配置轨迹管理器。  
利用ORBIT_DETERMINATION_INITIATED脚本回调，为进一步的轨道确定分配任务。

DISTRIBUTioNC.DistributionauthorizedtoU.S.GovernmentAgenciesandtheircontractors,11-Feb-2020. OtherrequestsforthisdocumentshallbereferredtoAFRL/RQQD.

![](images/4d9ad55a7315e280ade61110105966dcaf9085842a5c794f5d55262f0bdd2b34.jpg)

# UNCLASSIFIED

# 开始

![](images/44d05b782bb773ee0de55e8113b0b2b8019eac3d5d25590107681b44a5a48e66.jpg)

·您需要安装以下应用程序：

-AFSIM版本2.7  
Wizard版本2.7，启用了SpaceTools插件  
Mystic版本2.7

# 操作步骤：打开V

打开Wizard  
创建一个名为space_situational_awareness的新项目

·关闭Wizard的启动窗口。  
依次选择File $_ { - > }$ NewProject。  
导航到scenarios/inwork目录下的3_space_situational_awareness子目录。  
输入新的文件名。

-右键点击space situational awareness.txt   
一选择“Set as Startup File”。  
一打开space_situational_awareness.txt文件

或者，将space_situational_awareness.txt拖放到Wizard图标或快捷方式上（更快的方法）。

DISTRIBUTioNc.Distributionauthorized to U.S.GovernmentAgenciesand theircontractors,11-Feb-2020. Otherreguests forthisdocumentshallbereferred toAFRL/ROQD

·使用Wizard的类型浏览器，或直接在platform_type定义中编辑SPACE_FENCE

1.打开Type Browser $_ { - > }$ WSF_PLATFORM $\scriptstyle - >$ SPACE_FENCE

右键点击并选择“ManagePlatformParts”   
点击“AddPart”以添加新传感器。

2.从Wizard项目浏览器中，双击./platforms/space_fence.txt进行编辑。

输入sen后按Ctr $^ +$ Space键以自动完成sensor..end_sensor块。

·创建两个传感器，命名为space_fence_1和space_fence_2:

继承自SPACE_FENCE基础传感器类型。  
默认开启。  
帧时间为5秒。  
一 为它们设置矩形视场：

俯仰视场（elevationfieldofview）：30至90度。  
方位视场（azimuthfield of view）：

space_fence_1:85至95度。

space_fence_2:-90至-80度。

一创建一个内部链接（internal_link）到处理器（processor）的一次性触发（one-shot）。

DISTRIBUTioNC.Distributionauthorizedto U.S.GovernmentAgenciesandtheircontractors,11-Feb-2020.

Copyright  2020 Infoscitex,a DCS company.Allrights reserved

OtherrequestsforthisdocumentshallbereferredtoAFRL/RQQD.

# UNCLASSIFIED

![](images/db1efe39eb8239b7ae1836343fd28a2f15358566b82c6a305ccdbe69b8f38a62.jpg)

编写脚本以实现太空围栏（SpaceFence）的初始轨道确定（IOD）操作

![](images/28fd33f8112e5ba9582266a7ef5b4585c7aab0656b2e5a49a467106f71589f1c.jpg)

·仅向red_command提供来自SPACE_FENCE传感器的一次轨迹更新  
要求来自两个不同SPACE_FENCE平台的轨迹数据用于提供初始轨道确定（IOD）。  
·通过完成SPACE_FENCE的"一次性触发”（one-shot）处理器中的脚本逻辑实现此效果。  
·在on_message 块中：

处理类型为WSF_TRACK_MESSAGE的消息。  
一 检索消息中轨迹的track ld。  
如果trackId已存在于脚本变量mTrackedTargets中，则说明该轨迹已发送至red_command:  
抑制再次发送该消息。  
－否则，这是第一次也是唯一一次将该消息发送至redcommand：

·将track Id插入到脚本变量mTrackedTargets中。

```txt
sensor space_fence1 SPACE_FENCE on frame_time 5 seconds field_of_view rectangular azimuth_field_of_view 85 deg 95 deg elevation_field_of_view 30 deg 90 deg end_field_of_view internal_link one-shot   
end_sensor sensor space_fence2 SPACE_FENCE on frame_time 5 seconds field_of_view rectangular azimuth_field_of_view -90 deg -80 deg elevation_field_of_view 30 deg 90 deg end_field_of_view internal_link one-shot   
end SENSOR 
```

#Only provide one track message to the commander so that #tracks from two separate space fence components are necess a#perform IOD   
processor one-shot WsF-scriptTONPROCESSOR script_variables Set<WsfTrackId> mTrackedTargets $= \{\}$ endScript_variables   
on_message type WsF TrackMESSAGE script WsftTrackId trackId $=$ ((WsftTrackMessage)MESSAGE).Track().TrackId); if(mTrackedTargets.Exists(trackId)) { SuppressMessage(); } else { mTrackedTargets.Insert(trackId); } endScript   
end_on_message   
internal link relay   
end Processor

DISTRIBUTioNC.Distributionauthorizedto U.S.GovernmentAgenciesandtheircontractors,11-Feb-2020.

Copyright  2020 Infoscitex,a DCS company.Allrights reserved

OtherrequestsforthisdocumentshallbereferredtoAFRL/RQQD.

# UNCLASSIFIED

![](images/b1d80302989364795c809a5ca6557fbbc8ce304440e3de2daa6eabb65c6ceb00.jpg)

# 配置 Red_Command 的轨迹管理器

![](images/e1735c531a7ae455f7e46090008b772b4fa36738cc6760c88d83f227a8ce9cf5.jpg)

·在Wizard的项目浏览器中，导航

到./scenarios/red_command.txt并打开

·在 red_command 的 track_manager块中：

一禁用uncorrelated_track_drops:

·保留那些原本会被丢弃的轨迹在track_manager中。

一指定retain_track_history：

提供执行位置或仅角度初始轨道确定（IOD）所需的数据。

一配置fusion_method为类型orbit_determination。

指定debug关键字以提供诊断输出。

指定process noise sigmas为0.030.030.03：

-单位为ECS坐标系下的xyz，以米/秒为单位。

·指定range_error_factors为0.035。

```txt
./scenarios/red_command.txt 
```

```csv
20 track-manager
21 // Keep tracks, assuming some long periods between updates.
22 uncorrelated_trackdrops disable
23 retain_track_history // Enables IOD
24 fusion_method orbit_determination
25 debug
26 range_error_factor 0.035
27 process_noise_sigmas_XYZ 0.03 0.03 0.03
28 end_fusion_method
29 end_trackmanager 
```

```txt
Distribution C. Distribution authorized to U.S. Government Agencies and their contractors, 11-Feb-2020. Copyright © 2020 InfoSitex, a DCS company. All rights reserved. Other requests for this document shall be referred to AFRL/RQQD. 
```

![](images/d8356867e5dd8bea4a2183a2b60d15a38d953dd7f247ecb55882cc67b6742fee.jpg)

# UNCLASSIFIED

# 编写初始轨道确定（IOD）回调脚本

9

![](images/5d523aabce6861c01ac1aa3801fefb4a48d47bc3a247dfff7b687238ff6fe22c.jpg)

# ·在./scenarios/red_command.txt文件中，编写OrbitDeterminationlnitiated回调脚本

一仅在平台名称为red_command时执行脚本。  
一调用red_command的 OrbitDeterminationlnitiated 脚本。

使用->运算符。

```txt
./scenarios/red_command.txt 
```

```txt
131 script void OrbitDeterminationInitiated(WsfPlatform aPlatform, 132 WsfLocalTrack aTrack)  
133 if (aPlatform.Name() == "red_command")  
134 { aPlatform->OrbitDeterminationInitiated(aTrack);  
135 }  
136 end_script 
```

·检查red_command 和tracking_sensor平台的任务处理器（WSF_TASK_PROCESSOR)

1.red_command平台

-理解DETECTED和ASSIGNED状态：

DETECTED：目标已被检测到。  
ASSIGNED：目标已被分配给一个跟踪传感器。

-审查MakeAssignment脚本：

根据与目标的最近距离，分配一个跟踪传感器，该目标已经完成初始轨道确定（IOD）。

2.tracking_sensor平台

理解以下状态：

WAITING：等待任务分配。  
OBSERVING:正在观察目标。  
TRACKING：正在跟踪目标。  
COMPLETE：跟踪任务已完成。

DISTRIBUTioNC.Distributionauthorizedto U.S.GovernmentAgenciesandtheircontractors,11-Feb-2020.

Copyright  2020 Infoscitex,a DCS company.Allrights reserved

OtherrequestsforthisdocumentshallbereferredtoAFRL/RQQD.

11

![](images/7a58181d88e205f6ff94e3a4cab3504a8c4a5c56db813a267a850dfcaa8325ad.jpg)

# UNCLASSIFIED

# 事件输出中的空间跟踪选项

![](images/f6656c3375991bd164532ef7bda0f6d0f038c77dbf4a6185487061f742ab4cb9.jpg)

·记录事件输出中与空间跟踪相关的有用事件和选项

1.ORBIT_DETERMINATION_INITIATED事件

表示初始轨道确定（IOD）已启动。

2.ORBIT_DETERMINATION_UPDATED事件

表示轨道确定已更新。

3.print_eci_locations选项

输出目标在地心惯性坐标系（ECI）中的位置

4.print_track_covariance选项

输出轨迹的协方差矩阵信息。

```txt
event_output
file ./output/$(CASE).evt
print_eci Locations enable
print_track_covariance enable
time_format h:m:s
enable SENSORTracks INITIATED
enable SENSORTracks_DROPPED
enable LOCALTracks INITIATED
enable LOCALTracks UPDATED
enable LOCALTracks_DROPPED
enable ORBITDETERMINATIONINITIATED
enable ORBITDETERMINATIONUPDATED
enable TASK_ASSIGNED
enable TASK_CANCELED
end_event_output 
```

88 script void DrawCovariance(Wsftrack aTrack) WsftDraw draw $=$ {;   
90 if (aTrack.StateCovarianceValid() && aTrack.LocationValid())   
92 { WsftCovariance stateCovariance $=$ aTrack.StateCovariance(); WsftGeoPoint trackLocation $=$ aTrack.CurrentLocation(); draw.SetId(aTrack.TrackId().Number()); draw.setColor(1.0,0.1,0.1); draw.Duration(10000.0);   
93 // The ellipsoid NED is used by WsftDraw. Ellipsoid ellipsoid $=$ aTrack.StateCovariance().EllipsoidNED();   
100 / scenarios/red-command.txt   
101 // Amplify the size to make it easier to find. double S $= 1000$ ;// Scale by 1000x draw.BeginEllipsoid( ellipsoid.OrientationHeadingDeg(), ellipsoid.OrientationPitchDeg(), ellipsoid.OrientationRollDeg(), ellipsoid.SemiAxisForward() \*S, ellipsoid.SemiAxisSide() \*s, ellipsoid.SemiAxisUp() \*s); draw.Vertex(trackLocation); draw.End();   
114 // Now draw a line to the ellipsoid to make it easier to find. draw.BeginLines(); WsftGeoPoint origin $=$ aTrack.OriigeratorLocation(); draw.Vertex.origin); draw.Vertex(trackLocation); draw.End();   
120 }   
121 end.script

DISTRIBUTioNC.Distributionauthorizedto U.S.GovernmentAgenciesandtheircontractors,11-Feb-2020.

OtherreguestsforthisdocumentshallbereferredtoAFRL/RQQD.

13

![](images/1563ca472984e42577bdf5cadb1418e1359989e750b5a1006694cb20b02a0cab.jpg)

# UNCLASSIFIED

# 想定

![](images/965c9f41ab78a929a7159dd76692238d4c935fa2178a26189f2b9e13fbf9a1ae.jpg)

# ·两个轨道运行的物体

-fls_133  
Flordistani卫星编号#133。  
-fls_133_r_b  
fls133的废弃火箭助推器。

# ·空间围栏（Space Fence）检测到两个物体

一来自空间围栏的轨迹数据由red_command收集。  
-red_command执行初始轨道确定（IOD），但初始误差较大。  
-red_command指派与“已完成初始轨道确定（IODed）"轨迹最近的同位置TRACKING SENSOR执行轨道确定。  
-显著减少了方位角（az）和仰角（el）中的大初始误差。

![](images/cd2b2a97f5406dee2be85191684df39fbf3a6f9bc336ffb542676e7b4dd7cb4c.jpg)  
DISTRIBUTioNc.DistributionauthorizedtoU.S.GovernmentAgenciesandtheircontractors,11-Feb-2020.   
OtherrequestsforthisdocumentshallbereferredtoAFRL/RQQD.

Copyright  2020 Infoscitex,a DCS company.Allrights reserved

![](images/379d59551300448b92fa75a9c5c875db63bb69c68d5d340f1799005dee615f85.jpg)

# UNCLASSIFIED

# 执行

![](images/51cd35d19cc71a8e3f32363c346895c9e9c218f64b18ffe078a8c9abeeeef34d.jpg)

RUN IT NOW!

DISTRIBUTioNC.Distributionauthorizedto U.S.GovernmentAgenciesandtheircontractors,11-Feb-2020.

OtherrequestsforthisdocumentshallbereferredtoAFRL/RQQD.

![](images/63d3d5119922aeffc9e9e0a320c2e0919de8bdb7b5edcbf6391c05755a6b13e4.jpg)

# 6.1.9.4. 交会与近距离操作 4_RPO

# 6.1.9.4.1. 本节想定解析

本节想定资源在以下目录下：

afsim2.9_src\training\user\9_Space\scenarios\solution\4_rpo\rpo_tag.txt

![](images/fad208159cfac54b675ecd0a705350bbbcdcd2947f68685610206a4734a68a41.jpg)

# 红方兵力

■ 一个卫星名叫 Chaser

▫ 与蓝方的卫星 Chief 处于同一轨道上，相距约 70 米  
□ 目标是要避免被蓝方的 Chief 捕获，又必须保持在距离 Chief1 公里以内

. 针对蓝方的机动侦察，Chaser 采用了法向机动来躲避侦察（在 Warlock 中实施）

# 蓝方兵力

■ 一个卫星名叫 Chief

▫ 包含两个传感器，一个指向地球，一个指向轨道前方  
□ Chief 的目标是至少一个传感器要侦察到 Chief

通过两次改变半长轴(第 2 次改变在 1 个轨道周期后）实现机动以试图侦察Chaser

# 6.1.9.4.2. 本节 PPT 资料

本文为 afsim2.9_src\training\user\9_Space\slides\4_RPO.pptx 的翻译。

![](images/a8fa2e01bd0af73d3fd479746b5f1a3ce09ffcba05493657503e7fcd93cdb354.jpg)

![](images/a5b5be5400bb0a8c6cd1569e8d3aaf6fddc043432314dc8752fa7b94de3be976.jpg)  
UNCLASSIFIED

![](images/fa3dcfbdc433224722c6193bd1476c4213d4e4d4542c5f7492a78534ce5c2cd0.jpg)  
Integrity★Service★ Excellence

# AFSIM空间培训

# 4－交会与近距离操作

![](images/038ca40ae8c5685739ccd9c82db53abee3c4d8ad87a6d77c731421de249a3eea.jpg)

# AFRL/RQQD

# 美国空军研究实验室

DISTRIBUTloNC.DistributionauthorizedtoU.S.GovernmentAgenciesand theircontractors,11-Feb-2020.

Otherrequestsforthisdocument shallbereferredtoAFRL/RQQD.

# ·包括：

一创建、验证和可视化用于交会与近距离操作（RPO）场景的轨道任务序列  
－在RPO场景中使用卫星系绳视图  
－在OITL（Operator-in-the-Loop）演练中创建任务序列  
-Astrolabe工具

![](images/27432a2c3b6dfc9e0fc4dc5fd35e9e88d6384b4a31171d1ff8e8fb53d222bdeb.jpg)

DISTRIBUTioNC.DistributionauthorizedtoU.S.Government Agenciesand theircontractors,11-Feb-2020.

Copyright  2020 Infoscitex,a DCS compan. Allrights reserved

Otherrequestsforthisdocumentshall bereferredtoAFRL/RQQD

2

![](images/1213e69148a8c01337a402900d48629517ad2cd7a7d21e274377712c84d69795.jpg)

# UNCLASSIFIED

# 介绍

![](images/01a89e39610b59faf2cdff0305f3f1b676abdba0d71becab5c96b31c970d1bb5.jpg)

# ·两颗卫星玩太空"捉迷藏”游戏

-Chief将尝试对Chaser获取传感器跟踪。   
-Chaser则试图避免被“抓到”，同时保持靠近Chief。

![](images/68427141046d021e2ad7f18821b55af1638e8ed9f3e8f886fed1a5fdd2574ec1.jpg)

DISTRIBUTloNC.DistributionauthorizedtoU.S.GovernmentAgenciesandtheircontractors,11-Feb-2020.

OtherrequestsforthisdocumentshallbereferredtoAFRL/RQQD.

·您需要安装以下应用程序：

AFSIM版本2.7  
-Wizard版本2.7，并启用SpaceTools插件  
Mystic版本2.7  
-Warlock版本2.7

![](images/499f825dbb9a31e7f6c0589852f722ce836768447e6c7de1d19be444d55451b1.jpg)

# ·操作步骤：

# 1.打开Wizard

2.创建一个名为rpo_tag的新项目

·关闭Wizard启动窗口。  
点击菜单栏中的File $\mathbf { \varepsilon } _ { - > }$ New Project。  
导航到路径scenarios/inwork/4_rpo。  
·输入新项目名称rpo_tag。

# 3.设置启动文件

右键单击rpo_tag.txt文件。  
选择“Set asStartup File”

# 4.打开rpo_tag.txt文件

您可以直接打开文件，也可以使用更快捷的方法：将rpo_tag.txt文件拖放到Wizard图标或快捷方式上。

DISTRIBUTioNC.DistributionauthorizedtoU.S.Government Agenciesand theircontractors,11-Feb-2020.

Copyright  2020 Infoscitex,a DCS compan. Allrights reserved

Otherrequestsforthisdocumentshall bereferredtoAFRL/RQQD

4

![](images/f65df89e5162d44015ef78bf5bce48498e1644c1a2652f3a9777aec705f3b061.jpg)

# UNCLASSIFIED

# 大纲

![](images/a775e64937d8e86aa457e33f79f4ceea4b73085dbd16aee4b4f22a98bc15662c.jpg)

# ·我们将分两个阶段开发场景：

# ·第一阶段

－为Chief设计一个计划任务序列

·在Wizard中使用Astrolabe创建输入任务序列。  
在Mystic中查看结果。

# ·第二阶段

－为Chaser设计一个响应方案

·在Warlock中使用Astrolabe将任务序列注入到正在运行的仿真中。  
在Warlock中查看结果。

# ·Chief卫星有两个传感器：

-Down：指向地球。  
－Ahead：指向轨道前方。

# ·目标：

Chief的目标是让Chaser进入至少一个传感器的捕获范围。  
Chaser的目标是避免被任何一个传感器捕获，但必须保持在距离Chief1公里以内。

# ·当前情况：

Chaser与Chief处于相同的轨道上，相距约70米。

![](images/bae265590eff5f72cf728ca6b58f63e3adf3a76c1071f2ca68024907a1ce1d2c.jpg)

![](images/73243fbc065e45f065cfc88ee892fef07e02449b00d92962d4e17239abe657d8.jpg)

DISTRIBUTioNC.Distributionauthorized to U.S.GovernmentAgenciesandtheircontractors,11-Feb-2020.

Copyright  2020 Infoscitex,a DCS compan. Allrights reserved

Otherrequestsforthisdocumentshall bereferredtoAFRL/RQQD

6

![](images/20293b9ba6523d928f3f522eae656bdeb2f4ed93e9ce7d287c4a0157668b6fdb.jpg)

# UNCLASSIFIED

# Chief的任务计划

![](images/3ccb6f735b04f1c5625278150a4b34bc4c24cb7fdf9bec0be2c50f57f6c27d66.jpg)

# Chief的任务计划细节：

1.仿真开始时，Chief位于Chaser前方。  
2.相位机动（PhasingManeuver）提供了两个传感器检测Chaser的机会。

# ·相位机动步骤：

通过两次改变轨道半长轴（SMA）实现机动：

1.第一次机动：提升到更高的SMA，使Chief沿轨道逐渐向后移动。  
2.第二次机动：返回到原始的SMA，以恢复到初始轨道高度。

# 机动时间安排：

－第一次机动可以在任意时间执行。  
第二次机动应在1个轨道周期后执行。

#

我们将使用Astrolabe添加此机动序列，以完成任务计划的设计。

![](images/c7741421d29ace6a6b2f62b5bc3a19ea6391c73e79c01bd821c6f6d0e403fabd.jpg)

夸张的相位机动：

Chief首先移动到更高的半长轴

（SMA）轨道，然后在一个轨道周期后返回到原始的SMA。

# ·Astrolabe是一个用于创建任务序列的工具

# －功能特点：

提供图形用户界面（GUI），用于为带有空间机动能力的平台创建任务序列。  
可以添加、移除、转换或重新组织任务事件。  
·验证任务序列，以检查输入是否完整以及任务的可行性。  
在地图窗口中显示任务预览。

# ·Astrolabe的应用：

一在Wizard中的应用：  
·将任务序列添加到输入文件中。  
一在Warlock中的应用：  
将任务序列注入到仿真中。

![](images/53708e3f9bf0b07c67b2b77bdaa79c4eef646497001a2399177722dbfe72cada.jpg)

DISTRIBUTioNC.DistributionauthorizedtoU.S.Government Agenciesand theircontractors,11-Feb-2020.

Copyright  2020 Infoscitex,a DCS compan. Allrights reserved

Otherrequestsforthisdocumentshall bereferredtoAFRL/RQQD

8

![](images/bd27a528a0503aef95fb3666124e582cdd12618e6cf68fdd2791680935f8d398.jpg)

# UNCLASSIFIED

# Astrolabe

![](images/30f1415864b3792091028dcace51b829d973e98f337884cf1a3654e3b0fe1a3e.jpg)

# ·Astrolabe可以通过以下方式启动：

一从View菜单启动。  
－或从特定平台的上下文菜单启动。

![](images/ead0b41399f70e67fa711bbecf76fed642da6d2544ea2873ef8ea7af7d84f9f4.jpg)

![](images/c2d15ff00bc3f3d90bd2545849bb56566100289c1aa8bf5fe10cbb46fcbd03a3.jpg)

DISTRIBUTloNC.DistributionauthorizedtoU.S.GovernmentAgenciesandtheircontractors,11-Feb-2020.

OtherrequestsforthisdocumentshallbereferredtoAFRL/RQQD.

# ·为Chief的任务序列添加两个机动步骤：

1.点击“Add Event”（添加事件）。  
2.选择“Change Semi-Major-Axis”（改变半长轴）。  
3.添加机动的详细信息：

·使用 $8 0 5 0 . 1 ~ \mathsf { k m }$ 的半长轴值。  
设置相对时间为10分钟。

![](images/4e9eddc2644654397569394526f65e396609c3ab2b812587eb4ffdda68df8442.jpg)

![](images/55cfb7141748acf94d6ee32294fc5a247a32736d1b1b81bb9ae6b6f2bbb75fe1.jpg)

DISTRIBUTioNC.DistributionauthorizedtoU.S.GovernmentAgenciesandtheircontractors,11-Feb-2020.

Copyright  2020 Infoscitex,a DCS compan. Allrights reserved

Otherrequestsforthisdocumentshall bereferredtoAFRL/RQQD

10

![](images/44999dbbe5136ad43be0902cd60e37e831bdce3aa8a742a03049aeeae83f3391.jpg)

# UNCLASSIFIED

# chief的任务

![](images/bd66e0e97e162c52a767e8445bfda05e91bfc42896145de58c1421b6448cbb90.jpg)

# ·为Chief的任务序列添加第二次机

# 动：

1.点击“Add Event”（添加事件）。  
2.选择“Semi-Major-Axis”（半长轴）。  
3.添加机动的详细信息：

使用 $8 0 5 0 \ k m$ 的半长轴值。  
设置事件发生在一个轨道周期之后。

![](images/3164078f4f4261d71c85eec7ddede0178e83a26a5dd370fc248e308955ffc5ce.jpg)

![](images/3416d8642759a67f669c1f063edc9d8ca28c76c93bd90076c2b903100aca5df0.jpg)

# ·任务验证

1.点击“Verify”（验证）。

2.系统将检查以下内容：

输入是否有效且完整。  
平台是否有足够的△v（delta-v）来完成提议的任务序列。

3.系统会显示与任务事件相关的信息，包括：

Av（速度增量）。  
仿真时间（simtime）。  
事件发生的日期（dateofevent）。

![](images/929b6b46ba5567a791898729b21a83bd8deedc7b723f6d9bd3557cf13494f45f.jpg)

4.在地图显示（Map Display）中预览任务。

一注意：对于那些只进行小幅度变化的机动操作，任务预览可能不容易观察到。

![](images/c715ff57cfba0abb02b59744a5ace75c5c2ed7f62cff04840522628199d87bda.jpg)

Copyright  2020 Infoscitex,a DCS company.Allrights reserved

Otherrequestsforthisdocument shallbereferredtoAFRL/RQQD.

![](images/cf891b4206d8db045f7e049723e27568422dfb72fe67125f50d56a9e3edfae02.jpg)

# UNCLASSIFIED

# 任务验证

![](images/943de4c58a9db393b677ac12daf29f74450a07c1109f73232697498405757a0e.jpg)

# 1．接受输入

－这将把输入写入输入文件中。

# 2．检查输入

一仔细检查输入内容。

![](images/8968d42333fe4f6c4b14c0854c9569e5ee56334ad43cc7e8d843801088846f01.jpg)

# 3．运行仿真

一当确认输入无误后，运行仿真。

# 4.查看结果

一在Mystic中查看生成的rpotag.aer文件。

<table><tr><td>17</td><td>mission_sequence</td></tr><tr><td>18</td><td></td></tr><tr><td>19</td><td>maneuver change_semimajor_axis</td></tr><tr><td>20</td><td>execute_at relative_time 10 minutes</td></tr><tr><td>21</td><td>semiMajor_axis 8050.1 kilometers</td></tr><tr><td>22</td><td>end_m学家</td></tr><tr><td>23</td><td></td></tr><tr><td>24</td><td>maneuver change_semiajor_axis</td></tr><tr><td>25</td><td>execute_at orbit 1 relative_time 0 seconds</td></tr><tr><td>26</td><td>semiMajor_axis 8050 kilometers</td></tr><tr><td>27</td><td>end_m学家</td></tr><tr><td>28</td><td></td></tr><tr><td>29</td><td>end_mission_sequence</td></tr></table>

# ·卫星系绳视图（Satellite TetherView）

# 1.设计用途：

－专为RPO（交会与近距离操作）设计。  
提供按比例缩放的视图。  
可显示附近平台的相对运动。

# 2.功能特点：

-提供特定的RIC（径向-沿轨-横轨）坐标系视图。  
显示矢量及其之间的角度。  
每个平台可以打开多个视图。

![](images/ecdbabc0ef2a1e30d8bc9911e02b0bee0aa8362292d446f0eddff4c124a6b129.jpg)

# 3.操作步骤：

打开rpo_tag.aer文件后，右键点击Chaser，选择Satellite-Tetherto Chaser。  
-建议将弹出的窗口停靠（dock）到界面中。  
花点时间与视图进行交互，探索其功能。

DISTRIBUTloNC.DistributionauthorizedtoU.S.GovernmentAgenciesand theircontractors,11-Feb-2020.

Copyright  2020 Infoscitex,a DCS compan. Allrights reserved

OtherrequestsforthisdocumentshallbereferredtoAFRL/RQQD.

# UNCLASSIFIED

![](images/cd4168502066ddf7fee759564ce4fe2f0046bf78e3a29ba6fd86b5fa0545ec32.jpg)

# 卫星系绳视图(Satellite Tether View)

![](images/57a3f464740ab550940e7a472f943e7712c7ebdaaee80431e249d8a8cc464cce.jpg)

# ·卫星系绳视图（Satellite Tether View）

# 1.操作步骤：

在卫星系绳视图中右键点击，选择AddTrack $>$ Chief。  
滚动仿真时间轴，观察视图的更新。  
建议在主地图窗口（MainMapWindow）中选择FollowChaser（跟随追踪者）。

# 2.卫星系绳视图中的轨迹功能：

显示另一个平台的相对位置随时间的变化。  
随着仿真进展，轨道会以不同亮度显示：

平台已经经过的轨道部分会以明亮的颜色显示。  
平台即将经过的轨道部分会以较暗的颜色显示。

![](images/5e71afaed67b5365b0b3453bfe302808130abf6c25c7aa2084c9b171bc396f66.jpg)

![](images/06bba4830722967aab7029a9d6dfb47f858c6bb43f9486e9c9fcbbcce7a80d3a.jpg)

DISTRIBUTloNC.DistributionauthorizedtoU.S.GovernmentAgenciesandtheircontractors,11-Feb-2020.

OtherrequestsforthisdocumentshallbereferredtoAFRL/RQQD.

# ·矢量操作步骤：

一在卫星系绳视图（SatellteTetherView）中右键点击，选择Vectors $>$ Velocity（矢量 $>$ 速度）。  
－接着选择Vectors $>$ New Vector...（矢量 $>$ 新建矢量...）。  
一 在弹出的窗口中，在Pointvectorto（指向矢量）下拉菜单中选择Chief。

一点击OK（确定）。

![](images/f370dfa8e6a6ed34ccba947dcd705512199274e66a11704ac4a66d05e25e86e7.jpg)

![](images/f7a1a12ede6506032defd6db44f6a2dfe885598e02216dd4865ee01549eb79ef.jpg)

![](images/0b8b8708be62773f3b5126bef243d117edfa4e942383aea741c6460fbd04097a.jpg)

![](images/74e9f780a2ea4f00b06a10e7cbe76dbe04e5b006994465e9f0a2407f528aa884.jpg)

DISTRIBUTioNC.DistributionauthorizedtoU.S.Government Agenciesand theircontractors,11-Feb-2020.

Copyright  2020 Infoscitex,a DCS compan. Allrights reserved

OtherrequestsforthisdocumentshallbereferredtoAFRL/RQQD.

16

![](images/8e984736ae3a7daffcc19caa5847ff72d68be28ba28c06ac4b80332dd84c926f.jpg)

# UNCLASSIFIED

# 卫星系绳视图(Satellite Tether View)

![](images/7226c0c0db3996e22a21287c0bf12e9b63814272bb19e2914728b8a21b8c9c6e.jpg)

# ·角度操作步骤：

1.在卫星系绳视图（SatelliteTetherView）中右键点击，选择Vectors $>$ VisualizeAngles（矢量>可视化角度）。  
2.在弹出的窗口中：

在Vector1（矢量1）下选择‘Velocity'（速度）。  
在Vector2（矢量2）下选择‘Chief。

3.点击OK（确定）

![](images/3e1c6e49a1e64c48492d4d0ecd9ed8940cb7424a72a2ffb5267f174cf6d0bb99.jpg)

当角度超过70度时，Chief将能够观察到Chaser。  
一旦被观察到，主地图窗口（MapWindow）中会弹出一条消息提示。

![](images/5baa84887a546c58df2972f9a719396131fe2a26ed3e3516f26a68242e88e3dc.jpg)

DISTRIBUTloNC.DistributionauthorizedtoU.S.GovernmentAgenciesandtheircontractors,11-Feb-2020.

OtherrequestsforthisdocumentshallbereferredtoAFRL/RQQD.

# ·相对几何工具（Relative Geometry Tool）

# 1.功能说明：

提供一个平台相对于另一个平台的位置数据。

# 2.操作步骤：

右键点击Chaser，选择RelativeGeometry $>$ FromChaser（相对几何>从Chaser）  
－一个面板会打开，并停靠在界面侧边。  
-在To:下添加Chief：

可以直接输入Chief，或者点击目标图标后选择Chief。

面板会自动填充RIC数据，包括：

Radial（径向）  
·Intrack（沿轨）  
Cross track（横轨）

![](images/d78c687c92dcbfff6d00e175425a4b45e4f51480545da54a1364d67bec049939.jpg)

![](images/fb610fcf05e82ef55d4e1ab23f978948e5920cdd38dfac9ad49e66d87ee97da9.jpg)

DISTRIBUTioNC.DistributionauthorizedtoU.S.Government Agenciesand theircontractors,11-Feb-2020.

Copyright  2020 Infoscitex,a DCS compan. Allrights reserved

Otherrequestsforthisdocumentshall bereferredtoAFRL/RQQD

18

![](images/ad1b331bc87c7dc7535e8073c77a23e80a8deb79c3507a84f5c88a85f7b02072.jpg)

# UNCLASSIFIED

# RPO可视化

![](images/77327c9012c846452024d3550045c1dcc1cd9b5e1d68c8592e9f7adc3c3ffc6d.jpg)

# ·拖放数据到沉浸式视图（如卫星系绳视图）

1.在RelativeGeometry（相对几何）面板中，点击‘Radial’（径向）数据行并拖动到SatelliteTetherView（卫星系绳视图）。  
2.对In-track（沿轨）和Cross-track（横轨）数据执行相同操作。  
3．拖放时，将数据放到已经显示‘Radial'（径向）数据的新框中。

![](images/4ce4bc200a3577d0982a122e7a1089104e0cc7804e36eb517040cbbfd93ec7ca.jpg)

DISTRIBUTioNC.DistributionauthorizedtoU.S.GovernmentAgenciesandtheircontractors,11-Feb-2020.

OtherrequestsforthisdocumentshallbereferredtoAFRL/RQQD.

# ·首次探测机会

-当Chief在其相位机动（phasingmaneuver）期间经过Chaser上空时，将出现首次探测机会。

# ·避免被探测

-现在我们将尝试使用Warlock中的Astrolabe来响应，以避免被Chief探测到。

![](images/c87db8b7e480fdc75b011c76f6d4a5ca0ff5e652f27de832048dfbc63aa79151.jpg)

1.使用Simulation Manager（仿真管理器）选择Warlock。

2.运行仿真：

·如果在打开Warlock时仿真已经在运行，请暂停仿真。

![](images/9848634fe04ef6dec676147d1efcca0bccc5a0402cd492efbbccc05077e4bb53.jpg)

DISTRIBUTioNC.DistributionauthorizedtoU.S.Government Agenciesand theircontractors,11-Feb-2020.

Copyright  2020 Infoscitex,a DCS compan. Allrights reserved

Otherrequestsforthisdocument shallbereferredtoAFRL/RQQD.

20

![](images/a4f70a5b533acd37e9e30635175d27c329360e9c52e4e1276d10044a5725e435.jpg)

# UNCLASSIFIED

# 建立系绳视图

![](images/c7c39f8bc7dff26461485b3b20c7b1d53c2a8589d3573424b15861f7530e7e5c.jpg)

·打开卫星系绳视图（SatelliteTetherView）

1.为Chaser打开一个卫星系绳视图。  
2.如果需要多个视图，可以打开更多窗口。

·打开相对几何面板（RelativeGeometryPanel）

-从Chaser到Chief打开一个相对几何面板。

·拖放RIC数据

将RIC数据从相对几何面板拖动到卫星系绳视图的面板中。

![](images/9364b2e4650fdd382ecf4401d7150bab8fd180fcfdceafd4472cf802e9fa8cf3.jpg)

![](images/3de7c4f25cd392afc81d7c3b114a7d789365f63025f376e3cbe6422143a785a0.jpg)

DISTRIBUTioNC.DistributionauthorizedtoU.S.GovernmentAgenciesandtheircontractors,11-Feb-2020.

OtherrequestsforthisdocumentshallbereferredtoAFRL/RQQD.

# ·打开Astrolabe

1．在平台选择器中选择Chaser。  
2.在仿真中按下播放（Play）按钮。  
3．观察RIC值，注意Chief开始相对运动的时刻。  
4.如果需要，可以将仿真速度调到快于实时（fasterthanrealtime）。

#

－创建一个任务序列，以避免在Chief 进行相位机动（phasingmaneuver）并飞越Chaser上空时被探测到。  
如果需要，可以重新启动仿真以重新尝试。

DISTRIBUTloNC.DistributionauthorizedtoU.S.GovernmentAgenciesand theircontractors,11-Feb-2020.

Copyright  2020 Infoscitex,a DCS compan. Allrights reserved

Otherrequestsforthisdocumentshall bereferredtoAFRL/RQQD

22

![](images/0c25fec256998172702fbcc8f060da15017f538db77bd0a5cca3991f438fcc7d.jpg)

# UNCLASSIFIED

# 避免第一次被探测

![](images/5f7f795e0a931cbf70c3f24bf30b84764c6a5daeb45e8001ac10e847696cbf36.jpg)

# ·避免首次探测窗口的一种可能性：

一执行一次法向机动（Normalmaneuver）（约20cm/s的△V就足够）。  
这一操作的效果是，在横轨方向（Cross-track）引入一个振荡，其周期等于轨道周期（对于Chief和Chaser来说接近2小时）。  
如果时机掌握得当，当Chief本应在Chaser上空时，它实际上会在横轨方向上显著偏移，从而使向下的传感器无法探测到Chaser。

![](images/4ad63abd3e3d7149dd7d7e407dc5081d3fab085ef498368b3ec5f77c737d74f8.jpg)

DISTRIBUTioNC.DistributionauthorizedtoU.S.GovernmentAgenciesandtheircontractors,11-Feb-2020.

OtherrequestsforthisdocumentshallbereferredtoAFRL/RQQD

·但是，当相位机动完成后，Chaser将会穿过Chief的前方传感器范围。

![](images/02a9bbb9c75afcf1751d2c94875080eaedb15599216b4b31ed7d0d8d83a5c62e.jpg)

![](images/672d29fd02a0dc8f12c4ca360b896b049f5887d71f83e8793095c9e0e5b4be59.jpg)

DISTRIBUTioNC.DistributionauthorizedtoU.S.Government Agenciesand theircontractors,11-Feb-2020.

Copyright  2020 Infoscitex,a DCS compan. Allrights reserved

Otherrequestsforthisdocument shallbereferredtoAFRL/RQQD.

![](images/5a5b6245b32e581e60370010ef2293cb9c1450f4ed4dd5feb09d3052ee0c1562.jpg)

# UNCLASSIFIED

# 避免第二次被探测

![](images/a8a40051e7ea1f9c43e69ee8a1e83c19076838cac84dff49e39135929651ba81.jpg)

# ·实践:

尝试设计一些机动方案，使Chaser能够保持靠近Chief，但不会被第二个传感器（前方传感器）探测到。

# ·实践：

尝试设计一些机动方案，使Chaser能够保持靠近Chief，但不会被第二个传感器（前方传感器）探测到。

# ·一种可能性：

－相位机动（两次半长轴变化）

：可以通过观察RIC数据来选择半长轴（SMA）变化的大小。  
最大的径向距离（R）将是半长轴变化的两倍。

例如，如果观察到最大径向距离R为100米，则表示Chief的相位机动使用了50米的半长轴变化。

请记住，初始轨道的半长轴为8050公里。

DISTRIBUTioNC.DistributionauthorizedtoU.S.Government Agenciesand theircontractors,11-Feb-2020.

Copyright  2020 Infoscitex,a DCS compan. Allrights reserved

Otherrequestsforthisdocumentshall bereferredtoAFRL/RQQD

26

![](images/56207e8241f6fba006ea4cf84e6a37e04a7e10011aafd6b423d2f2bce56f131a.jpg)  
UNCLASSIFIED

# RPO

![](images/ca453d1e9ca86aeb456d86ca7a0c12926b2a7992a09f3375a02bdb2c986f06d9.jpg)

![](images/a8a00bf7c2ddd54b356658399219949a07c26d0478b80abb84b422c8c8211c4a.jpg)  
DISTRIBUTioNC.DistributionauthorizedtoU.S.GovernmentAgenciesandtheircontractors,11-Feb-2020.

OtherrequestsforthisdocumentshallbereferredtoAFRL/RQQD

![](images/ccc85d732ec7c9386e672716fdc46feb3ba117b49a37f5761040b9e2c6ca50c9.jpg)

# 6.1.10. 行为与智能体建模培训 10_Other_Topics_bam

行为与智能体方面是大家都非常关心的课题。本小节会比之前小节更加详细的来对培训教材和培训示例进行解读和分析，以使得大家都能够对该部分内容有较好的掌握。本节共分为 8 次课，第 1 次课就是下面的，讲的会比较仔细，后面的课都是在上一节课的基础上完成的，因此要按顺序来看，最终完成了一个综合空地防空系统。

# 6.1.10.1.行为与智能体建模培训概览 21_AFSIM_BAM_Trng_Review

# 6.1.10.1.1. 本节想定解析

本节想定资源在以下目录下：

```batch
afsim2.9_src\training\user\10_Other_Topics\bam\scenes\floridistan\21_floridistan_review\run_course.txt 
```

# 6.1.10.1.1.1. 模型库

模型库可以看做是可用兵力型号。

# 1) 无人机(UCAV)

□ 目标特性

红外特性：10 watts/steradian  
光学特性： $1 0 \ m ^ { 2 }$   
雷达特性：定义了在各角度下独立的 db值，都在[0,40]db 范围内

□ 运动(WSF_AIR_MOVER)

径向加速度 1.5g  
飞行路径结束后：从模拟中移除平台

# □ 武器

# GPS 制导炸弹(RED_GPS_BOMB_1)

# ▫ 目标特性

雷达特性： $\mathsf { R C S } { = } \mathsf { 1 } m ^ { 2 }$

□ 数量：2

□ 射程： $1 8 . 5 2 \mathrm { k m }$ (double lar_meters = 18520)

□ 杀伤模型(WSF_SPHERICAL_LETHALITY)：

范围 $[ 2 5 \mathsf { m } , 3 0 \mathsf { m } ]$ , 阀值 0.2，威力[0.0, 1.0]  
可以理解为在 $2 5 \mathsf { m }$ 以内杀伤力是 1.0，在 30m 以外杀伤力是 0，在这之间杀伤力是线性从 0.0,1.0，只有杀伤力达到 0.2 时，才会对目标造成杀伤

# □ 制导参数(WSF_GUIDED_MOVER)

重量：500 磅  
空气动力学相关参数(WSF_AERO)

□ 最大升力系数：10.4  
□ 次音速零升力阻力系数：0.100  
□ 超音速零升力阻力系数：0.4  
□ 跨音速阻力上升开始时的马赫数：0.8  
□ 跨音速租力上升结束时的马赫数：1.2  
□ 零升力阻力系数最大时的马赫数：2.0  
□ 面积：0.059 $m ^ { 2 }$   
□ 展弦比：4.0

# □ 制导计算(WSF_GUIDANCE_COMPUTER)

比例导航增益：10.0  
速度追踪导航增益：10.0  
克服重力偏置因子：1.0  
最大加速度大小： $2 5 . 0 { \mathrm { g } }$   
进入制导阶段的时间：0s（一开始就进入）

# 引信采用对地目标引信(WSF_GROUND_TARGET_FUSE)

# 滑翔弹(RED_GLIDE_BOMB_1)

# ▫ 目标特性

雷达特性： ${ \mathsf { R C S } } { = } 1 m ^ { 2 }$

▫ 数量：6  
□ 射程：74.08km(double lar_meters $=$ 74080)

# 杀伤模型(WSF_SPHERICAL_LETHALITY)

范围[30ft, 100ft], 阀值 0.2，威力[0.05, 1.0]  
可以理解为在 30ft 以内杀伤力是 1.0，在 30m 以外杀伤力是 0，在这之间杀伤力是线性从 0.05,1.0，只有杀伤力达到 0.2 时，才会对目标造成杀伤

# 制导参数(WSF_GUIDED_MOVER)

重量：250 磅  
空气动力学(WSF_AERO)

□ 最大升力系数：7.0  
□ 次音速零升力阻力系数：0.150

▫ 超音速零升力阻力系数：0.22  
□ 跨音速阻力上升开始时的马赫数：0.85  
□ 跨音速租力上升结束时的马赫数：1.15  
□ 零升力阻力系数最大时的马赫数：2.0  
□ 面积：0.028 $m ^ { 2 }$   
□ 展弦比：14.0  
□ 奥斯瓦尔德效率因子：0.95

▫ 制导计算(WSF_GUIDANCE_COMPUTER)

比例导航增益：10.0  
速度追踪导航增益：10.0  
克服重力偏置因子：1.0  
最大加速度大小： $2 5 . 0 { \mathrm { g } }$   
进入制导阶段的时间：0s（一开始就进入）

▫ 引信采用对地目标引信(WSF_GROUND_TARGET_FUSE)

最大飞行时间：900s

武器释放逻辑(UCAV_WEAPON_RELEASE)

▫ 在传感器的主跟踪列表中的目标，只要在武器的打击范围内，就开启打击，齐射 2 发

# 2) 远距离干扰机(SOJ)

□ 目标特性

红外特性：1000 watts/steradian  
光学特性：30 $m ^ { 2 }$   
雷达特性： $\mathsf { R C S } = \mathsf { 1 0 } m ^ { 2 }$

□ 运动(WSF_AIR_MOVER)

径向加速度 $2 . 0 { \tt g }$   
飞行路径结束后：从模拟中移除平台

□ 通信(TEAM_DATALINK)

速率：100 mbits/sec  
网络：blue_net (WSF_COMM_NETWORK_MESH_LEGACY)  
内部处理器(internal_link)：WSF_TRACK_PROCESSOR

□ 轨迹不更新丢弃时间：60sec  
□ 轨迹报告时间间隔：10sec  
□ 向外汇报融合轨迹：开启   
□ 向外汇报非本地原始轨道：关闭   
□ 通过 blue_chain 命令链使用本地的 TEAM_DATALINK 来向上级汇报信息  
□ 拒绝循环报告：开启

# 3) 船舶(SHIP)

目标特性

雷达特性： $\mathsf { R C S } = 1 0 0 m ^ { 2 }$

□ 运动(WSF_SURFACE_MOVER)  
□ 通信(TEAM_DATALINK)

速率：100 mbits/sec  
网络：blue_net (WSF_COMM_NETWORK_MESH_LEGACY)

内部处理器(internal_link)：WSF_TRACK_PROCESSOR

▫ 轨迹不更新丢弃时间：60sec  
□ 轨迹报告时间间隔：4sec  
□ 向外汇报融合轨迹：关闭   
□ 向外汇报非本地原始轨道：开启   
□ 通过 blue_chain 命令链使用本地的 TEAM_DATALINK 来向上级/下属汇报信息  
□ 拒绝循环报告：开启

# 4) 目标(TARGET)

# □ 目标特性

红外特性：10 watts/steradian  
光学特性：10 ?2  
雷达特性： ${ \mathsf { R C S } } { = } 1 m ^ { 2 }$

# 5) 大型地空导弹发射器(LARGE_SAM_LAUNCHER)

# □ 通信(TEAM_DATALINK)

速率：100 mbits/sec  
网络：blue_net (WSF_COMM_NETWORK_MESH_LEGACY)  
内部处理器(internal_link)：WSF_TRACK_PROCESSOR

□ 轨迹不更新丢弃时间：60sec

内部处理器(internal_link)：WSF_TASK_PROCESSOR

# □ 武器(LARGE_SAM)

数量：4  
目标特性

▫ 红外特性：1 watts/steradian  
□ 光学特性：1 $m ^ { 2 }$   
▫ 雷达特性： $\mathsf { R C S } { = } \mathsf { 1 } m ^ { 2 }$

# 运动(WSF_STRAIGHT_LINE_MOVER)

▫ 平均速度：2643 kts  
□ 最大横向加速度： $2 0 . 0 { \ \mathsf { g } }$   
□ 制导模式：lead_pursuit 也即速度矢量始终朝向当前轨迹

# 引信采用对空目标引信(WSF_AIR_TARGET_FUSE)

□ 最大飞行时间：27s

跟踪(WSF_PERFECT_TRACKER)   
杀伤模型(WSF_GRADUATED_LETHALITY)

□ 100m 时杀伤是 0.7

射击传达：从命令开始射击，到子弹发出时间为 0.5s  
射击间隔：5.0s  
转动角度：水平 360 度，垂直[10,70]度

# 6) 大型地空导弹营(LARGE_SAM_BATTALION)

# 目标特性

红外特性：10 watts/steradian  
光学特性：10 $m ^ { 2 }$

雷达特性： $\mathsf { R C S } { = } \mathsf { 1 } m ^ { 2 }$

# ▫ 轨迹过滤(WSF_KALMAN_FILTER)

测量范围的标准差 ${ 5 0 } \mathsf { m }$   
测量方位的标准差 0.1deg  
测量仰角的标准差 0.1deg  
滤波器在三个方向上的噪声标准差 505030

# □ 通信(TEAM_DATALINK)

速率：100 mbits/sec  
网络：blue_net (WSF_COMM_NETWORK_MESH_LEGACY)  
内部处理器(internal_link)：WSF_TRACK_PROCESSOR

▫ 轨迹不更新丢弃时间：60sec

内部处理器(internal_link)：LARGE_SAM_BATTALION_TASK_MGR

▫ 并行处理数量：2  
▫ 当接到上级分配的任务后，会遍历其下级单位，找到下级单位中的目标捕获雷达（按类型为”ACQ_RADAR”来判断），将其置为交战状态（将其置为”ENGAGE”）  
▫ 判断目标捕获雷达捕获到目标后，交由目标跟踪雷达跟踪，跟踪到达地空导弹打击区域后(由 full_kinematic 定义，30km 高，25 海里半径)，调用地空导弹进行打击(RED_SAM_BATTERY_TASK_MGR 逻辑)

# 7) 目标捕获雷达(ACQ_RADAR)

# □ 目标特性：

红外特性：10 watts/steradian  
光学特性： $1 0 \ m ^ { 2 }$   
雷达特性： $\mathsf { R C S } { = } \mathsf { 1 } m ^ { 2 }$

# □ 通信(TEAM_DATALINK)

速率：100 mbits/sec  
网络：blue_net (WSF_COMM_NETWORK_MESH_LEGACY)  
内部处理器(internal_link)：RED_RADAR_TACTICS

□ 判断当前状态被置为了”ENGAGE”，则将其下所有传感器开机

# □ 传感器一(acq_radar)

默认关闭   
最小探测概率（高于此值才认为被探测）：0.5  
忽略同一阵营目标  
$\scriptstyle { \mathsf { R C S } } = \mathbf { 1 } m ^ { 2 }$ 的物体的探测范围：50nm  
最大探测距离：150nm  
天线高度： $5 . 0 \mathsf { m }$   
转动角度：水平 360 度，垂直[0,50]度  
虚警概率：1.0e-6  
使用 1 型 Marcum-Swerling 检测模型  
建立跟踪条件：5 击 3 中  
维持跟踪条件：5 击 1 中  
生成跟踪的质量：0.8  
发射机参数

□ 功率：1000.0kw

□ 载频：3000mhz  
□ 内部损耗：2db  
▫ 天线(ACQ_RADAR_ANTENNA)

接收机参数

□ 带宽：2.0 mhz  
▫ 噪声功率：-160dbw   
□ 内部损耗 7db

天线(ACQ_RADAR_ANTENNA)发射机与接收机共用天线

□ 矩形模式

理想峰值增益：35db  
最小增益：-10 db  
水平方向半功率波束宽度：10deg  
垂直方向上的半功率波束宽度：10deg

报告目标的截距、方位角、仰角、敌我识别状态

# 8) 目标跟踪雷达(LARGE_SAM_TTR)

通信(TEAM_DATALINK)

速率：100 mbits/sec  
网络：blue_net (WSF_COMM_NETWORK_MESH_LEGACY)  
内部处理器(internal_link)：WSF_TASK_PROCESSOR

□ 最大探测范围：64.8km  
□ 探测概率：0.7  
□ 传感器一(ttr TTR_RADAR)

默认关闭   
忽略同一阵营目标  
转动角度：水平 360 度，垂直[0,80]度

模式默认参数（其它模式不指定则使用此参数）

□ $\mathsf { R C S } { = } \mathsf { 1 } m ^ { 2 }$ 的物体的探测距离：35 海里  
□ 天线高度： $4 . 0 \mathsf { m }$   
□ 最小探测概率（高于此值才认为被探测）：0.5

□ 发射机参数

功率 1000.0 千瓦  
载频：9500mhz  
内部损耗：2db  
天线模式(TTR_RADAR_ANTENNA)

□ 接收机参数

带宽：500.0 khz   
噪声功率：-160 dBw   
内部损耗：7db

□ 天线模式(TTR_RADAR_ANTENNA)

正弦模式

□ 峰值增益：35db  
□ 最小增益：-10.0 db   
水平方向半功率波束宽度：1deg  
□ 垂直方向半功率波束宽度：1deg

□ 虚警概率：1.0e-6  
[ 使用 1 型 Marcum-Swerling 检测模型  
□ 报告目标的斜距、方位角、仰角、速度

# 识别模式参数(ACQUIRE)

□ 最多同时跟踪目标数量：1  
□ 扫描方式：方位和俯仰方向均扫描  
□ 方位扫描范围[-5,5]deg   
□ 俯仰扫描范围[-5,5]deg   
□ 采样间隔：2s  
□ 建立跟踪条件：5 击 3 中  
▫ 维持跟踪条件：3 击 1 中  
□ 跟踪质量：0.9  
▫ 成功后转入跟踪模式

# 跟踪模式参数(TRACK)

□ 最多同时跟踪目标数量：6  
□ 扫描方式：方位和俯仰方向均扫描  
□ 方位扫描范围[-1,1]deg   
□ 俯仰扫描范围[-1,1]deg   
□ 采样间隔：1.0s  
□ 建立跟踪条件：5 击 3 中  
▫ 维持跟踪条件：3 击 1 中  
□ 跟踪质量：1.0

▫ 上报：通过 blue_comm 向命令链 blue_chain 中的上级上报

# 9) 早期预警雷达(EW_RADAR)

□ 目标特性：

红外特性：10 watts/steradian  
光学特性：10 2  
雷达特性： ${ \mathsf { R C S } } { = } 1 m ^ { 2 }$

□ 通信(TEAM_DATALINK)

速率：100 mbits/sec  
网络：blue_net (WSF_COMM_NETWORK_MESH_LEGACY)  
内部处理器(internal_link)：RED_RADAR_TACTICS

上报：通过 blue_comm 向命令链 blue_chain 中的上级上报

传感器一(EW_RADAR)

默认开机  
忽略同一阵营目标  
${ \mathsf { R C S } } = m ^ { 2 }$ 的目标探测范围：100 海里(185.2 公里)  
天线高度： $_ { 6 . 0 \mathsf { m } }$   
采样间隔：20s  
最小探测概率（高于此值才认为被探测）：0.5  
扫描方式：水平扫描[-180, 180]deg

发射机参数

▫ 天线(EW_RADAR_ANTENNA)   
□ 波束中心在水平方向上的仰角：10.0deg

□ 功率：1000.0kw  
▫ 载频：200mhz  
▫ 内部损耗：2db

# 接收机参数

□ 天线(EW_RADAR_ANTENNA)   
□ 波束中心在水平方向上的仰角：10.0deg  
□ 带宽：2.0mhz  
▫ 噪声功率：-160 dbw   
□ 内部损耗：7db

# 天线(EW_RADAR_ANTENNA)发射机接收机共用天线参数

# ▫ 矩形模式

峰值增益：20.0db  
最小增益：-10.0db  
水平方向半功率波束宽度：10deg  
垂直方向半功率波束宽度：20deg

虚警概率：1.0e-6  
使用 1 型 Marcum-Swerling 检测模型  
建立跟踪条件：5 击 3 中  
维持跟踪条件：3 击 1 中  
跟踪质量：0.5  
报告：斜距、方位角、敌我识别状态

# 10) 联合防空指挥所(IADS_CMDR)

# □ 目标特性：

红外特性：10 watts/steradian  
光学特性：10 2  
雷达特性： ${ \mathsf { R C S } } { = } 1 m ^ { 2 }$

# □ 通信(TEAM_DATALINK)

速率：100 mbits/sec  
网络：blue_net (WSF_COMM_NETWORK_MESH_LEGACY)  
内部处理器(internal_link)：IADS_CMDR_DATA_MGR  
内部处理器(internal_link)：IADS_CMDR_TASK_MGR

□ 5 个线程同时处理

□ 接收下级雷达的侦察轨迹，并向下级发送轨迹更新间隔：10.0s  
□ 遍历所有的下属 LARGE_SAM_BATTALION 大型地空导弹营，看轨迹是否在其打击范围内，若在则对其分配任务进行交战

# 11) 雷达连队(RED_RADAR_COMPANY)

# □ 目标特性：

红外特性：10 watts/steradian  
光学特性：10 $m ^ { 2 }$   
雷达特性： ${ \mathsf { R C S } } { = } 1 m ^ { 2 }$

# □ 通信(TEAM_DATALINK)

速率：100 mbits/sec  
网络：blue_net (WSF_COMM_NETWORK_MESH_LEGACY)

内部处理器(internal_link)：WSF_TRACK_PROCESSOR

□ 上报：通过 blue_comm 向命令链 blue_chain 中的上级上报  
▫ 上报间隔：20s  
□ 开启轨迹融合后跟踪报告  
□ 关闭原始跟踪报告  
内部处理器(internal_link)：WSF_TASK_PROCESSOR

# 6.1.10.1.1.2. 红方兵力

![](images/ce9327b056e8f697ff5b8ab984b0842d8ad51da630e59f7da592e41e9359e809.jpg)

如上图所示，建立如下红方兵力的指挥关系，其各兵力轨迹如上图所示：

![](images/640805471062f3b94b6369b73526da19330c4cff76ed03401981deb980cd34d6.jpg)

红方兵力详细信息如下：

# 1) 一艘指挥船(SHIP) ship_lead

□ 给定了一个位置在海上，速度 30 节  
□ 给定一个巡逻的路线 ship_patrol  
□ 其包含两个下属 soj_north, soj_south

2) 两架远距离干扰机(soj) soj_north, soj_south

▫ 其长级是船舶 ship_lead   
▫ 两架干扰机只有路径不相同，其它的均相同，路径如图所示，飞行到一定位置后会盘旋在 soj_orbit 路径上

3) 四架无人机(UAV)uav-1, uav-2, uav-3, uav-4

□ uav-1

默认建立名为 target_1 和 target_2 的跟踪  
默认挂弹，也即 UAV 模型库里的 2 枚 GPS 炸弹 RED_GPS_BOMB_1，6 枚滑翔弹 RED_GLIDE_BOMB_1  
默认武器释放逻辑：也即目标 target_1 和 target_2 到了弹可以打击的范围就发弹打击

□ uav-2

默认建立名为 target_3 和 target_4 的跟踪  
挂弹为全部挂 10 枚 RED_GLIDE_BOMB_1 滑翔弹  
默认武器释放逻辑：也即目标 target_1 和 target_2 到了弹可以打击的范围就发弹打击

□ uav-3

默认建立名为 target_1 和 target_3 的跟踪  
默认挂弹，也即 UAV 模型库里的 2 枚 GPS 炸弹 RED_GPS_BOMB_1，6 枚滑翔弹 RED_GLIDE_BOMB_1  
默认武器释放逻辑：也即目标 target_1 和 target_3 到了弹可以打击的范围就发弹打击

□ uav-4

默认建立名为 target_2 和 target_4 的跟踪  
默认挂弹，也即 UAV 模型库里的 2 枚 GPS 炸弹 RED_GPS_BOMB_1，6 枚滑翔弹 RED_GLIDE_BOMB_1  
默认武器释放逻辑：也即目标 target_2 和 target_4 到了弹可以打击的范围就发弹打击

# 6.1.10.1.1.3. 蓝方兵力

![](images/81e72251ab0e969b3abc414ea8ea22c6ebf2b5eee954d688c489abfaecc5d14e.jpg)

如上图所示，建立蓝方的指挥关系如下：

![](images/d9292b4f40e66c8ca78cf7d32de7fee3acc5dade30cf4a61478beacb6f602f81.jpg)

蓝方兵力详细信息如下：

# 1) 一个联合防空指挥所(IADS_CMDR)10_iads_cmdr

▫ 主要指挥逻辑是其收到早期预警雷达连队探测的轨迹信息后，将任务发送给大型地空导弹营

# 2) 一个早期预警雷达连队(RED_RADAR_COMPANY)100_radar_company

□ 主要指挥逻辑是收到其下属的两部早期预警雷达的轨迹数据上报给联合防空指挥所

# 3) 两部早期预警雷达(EW_RADAR)200_ew_radar, 300_ew_radar

□ 其具有 180 多公里的探测范围，能够在早期发现来袭目标，然后向上报给早期预警雷达连队

# 4) 一个大型地空导弹营(LARGE_SAM_BATTALION)3500_large_sam_battalion

▫ 其主要的指挥逻辑是收到联合防空指挥所下达的轨迹任务后，先开启目标捕获雷达，在捕获目标后再开启目标跟踪雷达  
□ 当目标在地空导弹的射程范围内后，进行打击
# 5) 一部目标捕获雷达(ACQ_RADAR)3510_acq_radar

▫ 其探测距离为 92 公里，雷达建立的跟踪质量要高于早期预警雷达，捕获目标后上报给大型地空导弹营

# 6) 一部目标跟踪雷达(LARGE_SAM_TTR)3520_large_sam_ttr

▫ 其探测距离为 64.8 公里，其跟踪质量要高于目标捕获雷达，捕获目标后上报给大型地空导弹营

# 7) 三部大型地空导弹发射器(LARGE_SAM_LAUNCHER)

▫ 听大型地空导弹营指挥，打击对应轨迹目标

