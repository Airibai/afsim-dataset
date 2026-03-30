# 按照平台在场景中出现的顺序逐个处理

·从输入文件中获取初始位置（地理坐标LLA与地形，高度方向NED）  
ECI坐标系的参考地球角度  
组织所有存在的组（可选）  
·on_initialize   
·特征、高度、长度、宽度、质量（空载、燃料、载荷）（可选）  
·指令链   
·目标管理器（所有平台都有一个目标列表）  
·动力装置（如果没有附加动力装置，则默认为地面域！）  
·燃料（可选）  
导航误差（可选）  
·平台部件初始化  
on_initialize2

DISTRIBUTioNC.Distributionauthorized toU.S.GovernmentAgenciesandtheircontractors,9-Aug-19. Otherrequestsforthisdocument shall bereferredtoAFRL/RQQD.

UNCLASSIFIED

# 当在射程范围内则发射武器

18

![](images/6b16d80ffd66f79e03499e0aa6bf40e1595db62a96c40fafd0bc4ea2455ea835.jpg)

![](images/33cd83a6582feaf4d2d563966fc975d82832d370beaa540fb8ca929e735c6567.jpg)

·当轰炸机在tank武器的打击范围内则进行打击   
·使用脚本处理器来处理

－检查到目标范围  
－发射武器  
－记录交战成果

DISTRIBUTioNC.Distributionauthorized toU.S.GovernmentAgenciesandtheircontractors,9-Aug-19 Otherrequestsforthisdocument shallbereferredtoAFRL/RQQD.

# ·创建新的脚本处理器步骤

在“bomber.txt"包含“include_onceprocessors/bomber_weapon_release.txt"  
创建bomber_weapon_release.txt platforms/bomber.txt

![](images/754c8a52b91a3231eb1f9f94dd8dc0b7720f81a378b0662154c966a3db18b8a9.jpg)

# ·类型:WSF_SCRIPT_PROCESSOR

# ·名称:BOMBER_WEAPON_RELEASE

# ·内含四个块

Variables   
Initialize2   
一 Script  
Onupdate

![](images/82d719c555f8bae633d4f452d4d9dde3377121b20e0a22388de374f9c5e18a8f.jpg)

DISTRIBUTioNC.Distributionauthorized toU.S.GovernmentAgenciesandtheircontractors,9-Aug-19. Otherrequestsforthisdocument shall bereferredtoAFRL/RQQD.

UNCLASSIFIED

# 练习：脚本变量

20

![](images/2ecf7732f0d7c10d202dd3a4f2952d749ef0b48da4941df5e89e4209973c9693.jpg)

processors/bomber_weapon_release.txt

# ·给script_variables块中定义以下变量:

-string 名为weaponName

·值为："red_gps_bomb_1"

-string 名为LARmeters

·值为:"lar_meters”

-array里面装的是bool，名为tgt_engaged

·使用默认初始化(必须要显式调用!)

# ·相当于在该processor中定义全局变量

processors/bomber_weapon_release.txt   
2 processor BOMBERWEAPONRELEASE WSFScriptPTPROCESSOR   
4 script_variables string weaponName $=$ "red_gps_bomb_1"; string LARmeters $=$ "lar_meters"; Array<bool> tgt_engaged $=$ Array<bool>(); endcript_variables   
10   
11 end Processor   
12

DISTRIBUTioNC.Distributionauthorized toU.S.GovernmentAgenciesandtheircontractors,9-Aug-19. Otherrequestsforthisdocument shall bereferredtoAFRL/RQQD.

22

![](images/2cce65055cf890062cd1a0788f8b02f501bdfaf3d4203643509c3ef8eebb99fb.jpg)

UNCLASSIFIED

on_initialize2

![](images/364fedee58dd983d2598d560a755ef1859c49573a137ae646295315e67a0c2be.jpg)

# ·初始化"target engagement”数组

－默认全false  
－使用"initialize2”确保跟踪已经建立

processors/bomber_weapon_release.txt   
8 Array bool> tgt_engaged $=$ Array bool>();   
9 endScript_variables   
10   
11 on_initlize2 for (int i $= 0$ ;i < PLATFORM.MasterTrackList().Count();i $= \mathrm{i} + 1$ ） { tgt_engaged[i] $=$ false; } // for loop   
15 end_on_initlize2   
16   
17   
18   
19 end Processor

DISTRIBUTioNC.Distributionauthorizedto U.S.Government Agenciesand theircontractors,9-Aug-19.

Otherrequests forthisdocument shallbereferred toAFRL/RQQD.

# ·发射一个武器weapon

－确定武器可用，以及相对目标的打击范围  
－返回打击状态

DISTRIBUTioNC.Distributionauthorized toU.S.GovernmentAgenciesandtheircontractors,9-Aug-19. Otherrequestsforthisdocument shall bereferredtoAFRL/RQQD.

![](images/91a212433a5cba12db2c78af9c496e62e3914b1de9ce9308520f369836a98867.jpg)

# fireWeapon脚本

![](images/5934ea4e0f4b5bc35209f10a2b017643faee3a9b16dc707706ee02ed6ed7656d.jpg)

processors/bomber_weapon_release.txt   
```txt
script bool fireWeapon (WsfTrack tTrack, string tWpn)
bool shot = false;
WsfWeapon tempWeapon = PLATFORM.Weapon(tWpn);
if (tempWeapon.IsValid() && tempWeapon.AuxDataExists(LARmeters))
{
    double tempRange = tempWeapon.AuxDataDouble(LARmeters);
    if (PLATFORM.GroundRangeTo(tTrack) < tempRange // Within range
        && tempWeaponQuantityRemaining() > 0 // Weapons remaining
        && PLATFORM.altitude() >= 7620) // Above 25,000 ft
    {
        shot = tempWeapon.FireSalvo(tTrack, 2);
    } // Firing Parameters
} // Validity Checks
return shot;
end_script 
```

processors/bomber_weapon_release.txt

# ·添加if

-条件:shot (true/false)   
-打印output:

·当前打击平台名称  
·当前发射武器名称  
·打击目标名称  
·当前时间

shot $=$ tempWeapon.FireSalvo(tTrack,2);   
30 } // Firing Parameters   
31 } // Validity Checks   
33 return shot;   
34 endScript

DISTRIBUTioNC.DistributionauthorizedtoU.S.GovernmentAgenciesandtheircontractors,9-Aug-19. Otherrequestsfor thisdocument shall bereferred toAFRL/RQQD.

UNCLASSIFIED

# 解决方案:fireWeapon输出

26

![](images/79ddb978484a7e83619306c454d7478ffb5197c16674af802938fcd6ae7f990a.jpg)

![](images/321e4a53b3cc784169091dca1052c1c60439ba7cc078893204cf747f8ef89cd3.jpg)

processors/bomber_weapon_release.txt

shot $=$ tempWeapon.FireSalvo(tTrack,2);   
} // Firing Parameters   
} // Validity Checks   
if (shot) { titeln(PLATFORM.Name(), "fired ", tWpn, "at ", tTrack.TargetName(), "at time ", TIME NOW);   
}   
return shot;   
end_script

DISTRIBUTioNC.Distributionauthorized toU.S.GovernmentAgenciesandtheircontractors,9-Aug-19. Otherrequestsforthisdocument shallbereferredtoAFRL/RQQD.

·每3秒处理一次  
·循环遍历所有当前的目标轨迹。  
·确认目标尚未被交战。  
·尝试发射武器。  
·记录目标已被交战。

DISTRIBUTioNC.Distributionauthorized toU.S.GovernmentAgenciesandtheircontractors,9-Aug-19. Otherrequestsforthisdocument shall bereferredtoAFRL/RQQD.

28

![](images/d16225f0b0a3773810134976abecf8882b431a37377067d316a6e2e9516b3ee5.jpg)

UNCLASSIFIED

# Update块代码

![](images/d05727607be4b7833c4ac2c7592769fe052ca1ea9006c0a2f0c62427ec78b127.jpg)

processors/bomber_weapon_release.txt

```txt
41 update_interval 3.0 s on_update for (int i = 0; i < PLATFORM MasterTrackList().Count(); i += 1) { if (!tgt_engaged[i]) { WsfTrack tempTrack = PLATFORM MasterTrackList().TrackEntry(i); if (fireWeapon(tempTrack,weaponName)) { tgt_engaged[i] = true; } // fired weapon } // not engaged } // for loop end_on_update   
57 end Processor 
```

DISTRIBUTioNC.Distributionauthorized toU.S.GovernmentAgenciesandtheircontractors,9-Aug-19. Otherrequestsforthisdocument shallbereferredtoAFRL/RQQD.

·Processor名称:fire-em   
·ProCeSSOr类型:BOMBER_WEAPON_RELEASE  
·将以前的发射代码注释   
·Run!!!

platforms/bomber.txt   
UNCLASSIFIED   
```txt
20 weapon red_gps_bomb_1 RED_GPS_BOMB_1 maximum_request_count 2 quantity 4 endweapon   
26 processor fire-em BOMBER WEAPON RELEASE end Processor   
27 # execute at_time 510 sec absolute # Weapon("red_gps_bomb_1").FireSalvo(MasterTrackList().TrackEntry(0),2); # Weapon("red_gps_bomb_1").FireSalvo(MasterTrackList().TrackEntry(1),2); # end_execute   
33 endplatform_type   
35 
```

30

![](images/0e4c5f7f4e1b2118343563974a5daec0c3a29353ea04f8a6b07b29f6fc041b32.jpg)

# 执行想定

![](images/aa94d250dd993fa5ee64758bff14a5f719e7a898d549057be53c4fc2b3a49dd4.jpg)

Output   
Scenario:floridistan sensor_plot_lib,wsf_cyber,wsfGRAMmer_check,ws   
Loading simulation input.   
Loading simulation input complete. Elapsed Wall Clock Time:0.0110941 Elapsed Processor Time:0.015625   
Initializing simulation.   
Initializing simulation complete. Elapsed Wall Clock Time:0.0112862 Elapsed Processor Time:0   
Starting simulation.   
bomber_1 fired redgps_bomb_1 at tank_1 at time 462   
bomber_1 fired redgps_bomb_1 at tank_2 at time 462 $T = 1000.000$ $T = 2000.000$ $T = 3000.000$ Simulation complete Elapsed WallClock Time:0.0567362 Elapsed Processor Time:0.0625

![](images/b95d122ad6d8819fbdd6bc09e4060c57b6c082826228a33e744744b19ad0a576.jpg)

·在地图中添加‘bomber_2'   
·打开scenarios/red_laydown.txt   
·阵营改为red'   
·高度30,000 ft   
·朝向270deg   
·给一个和bomber_1相似的路线

![](images/40f5d703fc52ebd36f7f424b89238e2ae51da97ccc89912aa72a8a113a9578da.jpg)

DISTRIBUTioNC.Distributionauthorized toU.S.GovernmentAgenciesandtheircontractors,9-Aug-19. Otherrequestsforthisdocument shall bereferredtoAFRL/RQQD.

32

![](images/fd078d32da26de209069a3bb9a5c2e24851d101efabcdee9a2180ffa878c912e.jpg)

# UNCLASSIFIED

# 添加跟踪

![](images/30acd8d8fe5cece6f0d6d4bb6eaf2be49161830458a84169ce107eb1f2b7af90.jpg)

·再次将两个坦克先就跟上  
·Run!!!

# scenarios/red_laydown.txt

```txt
53 platformbomber_2BOMBER   
55 position 30:20:26.608n 80:01:12.413w   
56 side red   
57 altitude 30000 ft   
58 heading 270 deg   
59   
60 track platform tank_1 end_track   
61 track platform tank_2 end_track   
62   
63 route   
64 position 30:20:26.608n 80:01:12.413w altitude 30000.00 ft   
65 speed 500 mph   
66 position 30:20:14.170n 81:30:06.210w   
67 position 30:24:31.183n 81:40:12.528w   
68 position 30:31:53n 81:34:47w   
69 position 30:34:42.210n 81:23:35.072w   
70 position 30:34:23.820n 80:44:17.139w   
71 end-route   
72   
73 endplatform 
```

DISTRIBUTioNC.Distributionauthorizedto U.S.Government Agenciesand theircontractors,9-Aug-19.

Otherrequests forthisdocument shallbereferred toAFRL/RQQD.

Output

Scenario foridistan

Loading simulation input.

Loading simulation input complete.

Elapsed Wall Clock Time:0.0125511

Elapsed Processor Time：0

Initializing simulation.

Initializing simulation complete.

Elapsed Wall Clock Time:0.0l26809

Elapsed Processor Time ：O.015625

Starting simulation.

bomber1 fired red gps bomb 1 at tank 1 at time 462

bomber1 fired red gps bomb1 at tank 2 at time 462

bomber2 fired red gps bomb1 at tank 2 at time 468

bomber2 fired red gps bomb1at tank 1at time 498

T=1000.000

=2000.000

Simulation complete

Elapsed Wall Clock Time:0.084439

Elapsed Processor Time ：O.09375

![](images/ddcbebf4fd7813b6676d81869b1ffc2afb96b91afd2421ff689309ecba44281f.jpg)

DISTRIBUTioNC.Distributionauthorizedto U.S.Government Agenciesand theircontractors,9-Aug-19.

Otherrequests forthisdocument shallbereferredtoAFRL/RQQD.

# UNCLASSIFIED

# 学习目标

34

![](images/a83625d1d988515bf15ee470bc3535577a8bd758bf995284975b4166024ff51b.jpg)

![](images/98446849d8998461d70519bab8634cd85f41525bfe45555f5dee416c7463b076.jpg)

·将学习到以下内容：

-AFSIM脚本语言  
-使用脚本处理器processor

![](images/3fb51be9d28e6ac67158039402fc645847e405f9717a538ccc7048fbb5d788dd.jpg)

DISTRIBUTioNC.Distributionauthorizedto U.S.GovernmentAgenciesand theircontractors,9-Aug-19.

Otherrequests forthisdocument shallbereferred toAFRL/RQQD.

# 6.1.5.2. WsfDraw 和脚本观察者 9_AFSIM_User_Training_WsfDraw_ScriptObserver

# 6.1.5.2.1. 本节想定解析

本节想定为：

afsim2.9_src\training\user\5_Scripting\scenarios\solutions\9_WsfDraw_And_Script_Observ ers\floridistan\floridistan.txt

![](images/610110c821b6f2d504e7f00c3e348271af8d65063c5f3f8452df9e1ba09db976.jpg)

# 红方兵力

一艘航母 ship_1

□ 定义了一个循环的路线

一架轰炸机 bomber_1（另一架 bomber_2 与 bomber_1 配置相同）

□ 定义了一个路线，先到陆地，再回到海上  
□ 设置了固定跟踪 tank_1,tank_2，只有跟踪了才能投弹  
□ 挂了 4 枚 GPS 制导炸弹，最大允许同时齐射 2 枚

设置当在 gps 制导炸弹的打击范围内时才开火(double lar_meters $=$ 18520)  
打击 tank_1,tank_2 的炸弹同时开火，针对每个目标又齐射 2 枚，相当于四枚一次打完

□ 当有打击目标时，实时的绘制当前飞机弹的攻击范围

GPS 制导炸弹

□ 本例中被挂在了 bomber_1 上  
▫ 弹的雷达特征 RCS 被设置为了常数 1 $m ^ { 2 }$ ，换算为 dbsm则是 0

# 蓝方兵力

一个在天上的卫星 satellite_1  
□ 定义了一个 700km 的轨道  
两辆坦克 tank_1, tank_2  
一个车辆

□ 定义了一个向北行进的路线

一个地空导弹阵地 sam_1

□ 下挂 16 枚地空导弹（但未设置发射条件）  
□ 下挂 2 部雷达，一部 150 海里（acq，开启），一部是 100 海里（ttr，默认关），在想定开始后，acq 雷达陆续会探测到红方的战斗机以及其发射的 4 枚 GPS 制导炸弹  
□ 其它定义包括通信、区域等在推演时均未有动作

# 公共

1 建了一个统计场景中打击次数的脚本（统计 WEAPON_HIT 事件），并输出发生该事件的平台。  
▪ 建立了蒙特卡洛多次仿真的方法，并将多次仿真的结果分开输出。

# 6.1.5.2.2. 本节 PPT 资料

本文为 afsim2.9_src\training\user\5_Scripting\slide\

9_AFSIM_User_Training_WsfDraw_ScriptObserver.pptx 的翻译。

![](images/ba3f4a65e9f3a7fc8e0037406a577772c9ac6a5ea1484b8b0272ebb7ade67bf2.jpg)

UNCLASSIFIED

![](images/6dee313738013a57984d6ced4bae24eb247f47cd9a01019c437176d57c9de485.jpg)

![](images/30df35fbd4b3a34faa8c4da15910f5f47f039babfb3b69a6ea2b2e876f60aaf8.jpg)  
Integrity★Service★ Excellence

# AFSIM用户培训

# 9-WsfDraw和脚本观

# 察者

13324598743

# AFRL/RQQD

# 美国空军研究实验室

·本节包含以下内容：

-使用WsfDraw脚本  
-创建一个脚本观察者(script observer)

![](images/aa9bb66520f1ef13d92728800b17b33e0f170a88b626b6fede505434374d3991.jpg)

DISTRIBUTioNC.Distributionauthorizedto U.S.GovernmentAgenciesandtheircontractors,9-Aug-19. Otherrequestsforthisdocument shallbereferredtoAFRL/RQQD.

UNCLASSIFIED

![](images/f2163436e064e2f9caa91861e5474b6e454e377b8f4d83653dfffe7d0b34ed5b.jpg)

WsfDraw

![](images/b8e3433892fe28ae0a04a04ba33d493d841afb99107c8f89bb43f3d449315a5e.jpg)

·Mystic和Warlock可以被用来通过.aer文件来可视化WsfDraw这些命令，或者实时的想应分布式消息  
·三个基本方法

-State:改变WsfDraw对象的状态   
·颜色、线型、持续时间等等

-Begin:指定绘制的几何体类型  
·线、圆、椭圆、图标等等

－Vertex:绘制元素的位置

·平台位置，LLA等等

·打开"processors/bomber_weapon_release.txt"   
·从在脚本的variables块后面添加这行开始  
·创建和打开draw.txt

processors/bomber_weapon_release.txt   
DISTRIBUTioNC.Distributionauthorized toU.S.GovernmentAgenciesandtheircontractors,9-Aug-19. Otherrequestsforthisdocument shall bereferredtoAFRL/RQQD.   
UNCLASSIFIED   
3 processor BOMBERWEaponRELEASE WSFScriptPTPROCESSOR   
4 script_variables   
6 string weaponName $=$ "red_gps_bomb_1";   
7 string LARmeters $=$ "lar_meters";   
8 Array bool> tgt_engaged $\equiv$ Array<bool>();   
9 end_script_variables   
10 include scripts/draw.txt   
11   
12   
13 oninitialize2

4

![](images/7c8634ff55dd78e184fa568685444bba8bda0a8bf311c33e49883cff1de0996e.jpg)

# Draw脚本

![](images/610d5007fff9b53eac978f53abc8bbc18cd066b6b8d181704de7c3a21c9b071b.jpg)

scripts/draw.txt   
```javascript
3 script void Draw()
4 WsfWeapon tempWeapon = PLATFORM.Weapon(name);
5 if (tempWeapon.IsValid() && tempWeapon.AuxDataExists(LARmeters))
6 {
7 WsfDraw draw = WsfDraw();
8 double range = tempWeapon.AuxDataDouble(LARmeters);
9 draw.Duration(3.0);
10 draw.setColor(0,1,0);
11 draw.Colorline;
12 draw.line;
13 draw.Line;
14 end;
15 } // Validity Checks
16 end_script 
```

·在跟踪队列中仍有目标，我们就进行绘制  
·Run!!!

```txt
44 update_interval 3.0 s  
45 on_update  
46 for (int i = 0; i < PLATFORM MasterTrackList().Count(); i += 1)  
47 {  
48 if (!tgt_engaged[i])  
49 {  
50 Draw();  
51  
52 WsfTrack tempTrack = PLATFORM MasterTrackList().TrackEntry(i);  
53 if (fireWeapon(tempTrack, weaponName))  
54 {  
55 tgt_engaged[i] = true;  
56 } // fired weapon  
57 } // not engaged  
58 } // for loop  
59 end_on_update 
```

DISTRIBUTioNC.Distributionauthorized toU.S.GovernmentAgenciesandtheircontractors,9-Aug-19. Otherrequestsforthisdocument shall bereferredtoAFRL/RQQD.

6

![](images/75a27fcdd43b6f510bd30631f7e77abbbb70e9a7b36fe18ba1ffc3972f6145fe.jpg)

# UNCLASSIFIED

# Results

![](images/b7dec298972826844852f297a0aca07f75c5612756a053e6dc1dffac57781fb3.jpg)

![](images/81babab1e16bd4bcfb517b12ec1a473d95ed22a096e94120dcb46d82e265884f.jpg)

DISTRIBUTioNC.Distributionauthorized toU.S.GovernmentAgenciesandtheircontractors,9-Aug-19. Otherrequestsforthisdocument shallbereferredtoAFRL/RQQD.

·自定义用户定义的事件输出数据，位于仿真级别。  
·可作为event_output 的替代方案使用。  
·用户必须创建必要的脚本来捕获事件。

DISTRIBUTioNC.Distributionauthorized toU.S.GovernmentAgenciesandtheircontractors,9-Aug-19. Otherrequestsforthisdocument shall bereferredtoAFRL/RQQD.

# UNCLASSIFIED

![](images/f0ecc5378021cc653f21f598c544e6d355727e8264ba31e4707704957eda272d.jpg)

# 脚本观察者

![](images/223a6e486769842ff0cfa6ed83af03f302a5e0a72df3a755293214ef36b1fbdb.jpg)

·当前可用的事件可用于触发脚本观察器，详见观察器文档页面。

observer

observer...end observe

enable<EVENT TYPe>[<user defined script name>1

disable<EVENYE>uerdinedste>]

Note:Muitipie scripts can beenabled forthe same <EyeNT TYPE>

STAEteattrocoacratet   
STATEEXI#teEiarocssrocsocrinaeet   
TANKINE#nteiinEtouoatoatotret   
TASK_AssGNED#ContextscriptvoidTaskAssigned(WsfTaskaTask,WsfTrackaTrack)end_script   
TASK_CANCELED#Context scriptvoidTaskCanceled(WsfTaskaTask)end_script   
·TASK_COMPLETED #Context scriptvoidTaskCompleted(WsfTaskaTask,intaStatus)end_script   
TEAM_NAME_DEFINITION #Context:scriptvoid TeamNameDefinition(WsfPlatformaPlatform)end_script   
WEAPON_FAoD#ContextsriptdeapoirebortedWeapoeaponWacrackoubleQuantitdit   
WEAPONFIEEQUD#ontetsritidWeaporeRequestedseapoWeaponWsackackubeuantdt   
WEAPON_FIED#ContextsriptvoidWeaponFiredWsfWeaponEngagementaWeaponEngagementWsfTrackaTargetTrack)endscript   
WEAPON_H#ContextscriptidWeapoHitWsfWeaponEngagementaWeaponEngagementWfPlatfoargetPlatforedscript   
WEAPONsSED#ontextscriptideapoiedWseapongagementWeapoEngagementWsfPlatorgetplatfoedct   
WEAPONODE_ACVAED#ContextsriptvdWeaponModeActivatedWsfatfoaPlatformWsfWeaponaWeaponendscrit   
WEAPONEEACVontextiptapodeDeactivatedatoatoeaoeapodit   
WEAPON_RELOAD_STARTED#Context:scriptvoidWeaponReloadStarted(WsfWeaponaWeapon)end script   
WEAPON_RELOAD_ENDED#ContextscriptvoidWeaponReloadEnded(WsfWeaponaWeapon)end_script   
WEAPON_TERMINATED#ContextscriptvoidWeaponTerminated(WsfWeaponEngagementaWeaponEngagement)end_script   
WEAPON_URNEDOFF#ContextscriptvoidWeaponTurnedOf(WsfPatformaPlatformWsfWeaponaWeapon）endscript   
WEAPON_TURNEDON#Context:scriptvoidWeaponTurnedOn(WsfPlatformaPlatformWsfWeaponaWeaponend_script

DISTRIBUTioNC.Distributionauthorized toU.S.GovernmentAgenciesandtheircontractors,9-Aug-19. Otherrequestsforthisdocument shall bereferredtoAFRL/RQQD.

# UNCLASSIFIED

# 汇报打击次数

10

# 需要两个观察者：

·第一个观察者数每个平台的打击次数-WEAPON_HIT事件  
·第二个观察者在仿真过程中汇报结果-SIMULATION_COMPLETE事件  
·使用一个全局的MAP将平台和其打击次数映射起来MAP的索引可以是平台的名称  
·FilelO对象可以用来对文件进行操作，可以写入内容

·在"setup.txt"文件中添加"include_once observers.txt"   
·创建并打开文件

# setup.txt

```txt
8 include_once platforms/bomber.txt   
9 include_once platforms/satellite.txt   
10 include_once platforms/single_large_sam.txt   
11 include once event output.txt   
13 include once observers.txt   
14 
```

DISTRIBUTioNC.Distributionauthorized toU.S.GovernmentAgenciesandtheircontractors,9-Aug-19. Otherrequestsforthisdocument shall bereferredtoAFRL/RQQD.

![](images/08beb89ea6a88f81a1f357ef20b6cbf67c2567d72d91ecb89fcdc3ed1192cc67.jpg)

# UNCLASSIFIED

# 实践：脚本观察者

![](images/e9ef25b3120c83d0182c9acac19807a41f8242b086865ceea531a4c90d39c100.jpg)

# observers.txt

·在script_variables块中定义以下变量： -MAP名为samHits

·键类型：string   
·值类型：int   
·使用默认初始化

·在脚本块中添加WEAPON_HIT观察者  
·为SIMULATION_COMPLETE事件添加观察者  
·添加observer块以及打开事件输出

observers.txt   
UNCLASSIFIED   
```txt
2 script variables Map<string, int> samHits = Map<string, int>();   
4 end script variables   
5 script void WeaponHit(WsfWeaponEngagement aWeaponEngagement, WsfPlatform aTargetPlatform)   
6 end script   
7 script void SimulationComplete()   
8 end script   
9 observer enable WEAPON_HIT enable SIMULATION_COMPLETE   
10 end observer 
```

DISTRIBUTioNC.Distributionauthorized toU.S.GovernmentAgenciesandtheircontractors,9-Aug-19. Otherrequestsforthisdocument shall bereferredtoAFRL/RQQD.

![](images/6ebacbbc0121ff088361e9d8c092c507c03cf3c5b86f425c418bb5d06e58c086.jpg)

# 创建脚本观察者

![](images/4bf91da9c2a53aa84b28c8a069bcb4013ae5a3e437b13e17d5eb0dd60eb10de5.jpg)

·针对每个WEAPON_HIT事件，创建并更新MAP中的值－使用目标平台名称做为“key”

observers.txt   
```txt
script void WeaponHit(WsfWeaponEngagement aWeaponEngagement, WsfPlatform aTargetPlatform)  
string name = aTargetPlatform.Name();  
if(samHits.Exists(name))  
{ samHits[name] = samHits[name] + 1; } else { samHits[name] = 1; } end script 
```

DISTRIBUTioNC.Distributionauthorized to U.S.Government Agenciesand their contractors,9-Aug-19. Otherrequestsforthisdocument shallbereferredtoAFRL/RQQD.

# ·使用FilelO来将结果写入到文件当中

observers.txt   
19   
20 script void SimulationComplete() FileIO output $=$ FileIO(); output.Open("output/hits.txt","out"); foreach(string name : int hits in samHits) { output.WriteLn(write_str(name, " was hit ", hits, " times")); } output.Close();   
28   
29   
27

# ·Run!!!

DISTRIBUTioNC.Distributionauthorized toU.S.GovernmentAgenciesandtheircontractors,9-Aug-19. Otherrequestsforthisdocument shall bereferredtoAFRL/RQQD.

# UNCLASSIFIED

![](images/26b2c257add98026c7e6da0a9b615a0548716ece2faadeccfd3377018b90472c.jpg)

# 将观察到的信息输出到文件

![](images/5d467167d27828bedb0ed8855f7452a0d8291dd3791a8b37404028bf56004af0.jpg)

# ·打开hits.txt

output/hits.txt   
```txt
1 bomber_1_red_gps_bomb_1_3 was hit 1 times   
2 bomber_1_red_gps_bomb_1_4 was hit 1 times   
3 bomber_2_red_gps_bomb_1_2 was hit 1 times   
4 bomber_2_red_gps_bomb_1_4 was hit 1 times   
5 tank_1 was hit 1 times   
6 tank_2 was hit 1 times 
```

DISTRIBUTioNC.Distributionauthorized to U.S.Government Agenciesand their contractors,9-Aug-19. Otherrequestsforthisdocument shallbereferredtoAFRL/RQQD.

![](images/f8fd61054902767cf02aeeffdb913f59617dff5435a6e73a8a76a17ac3bba096.jpg)

DISTRIBUTioNC.Distributionauthorized to U.S.Government Agenciesand their contractors,9-Aug-19. Otherrequestsforthisdocument shall bereferredtoAFRL/RQQD.

# UNCLASSIFIED

# 蒙特卡洛运行

18

# floridistan.txt

```txt
floridistan.txt\*   
1 # File generated by Wizard 2.6.0 on Apr 10, 2020. file_path . file_path ./models   
3   
4 log_file output/jacksonabad.log   
5 include_once setup.txt   
7 include_once scenarios/blue_laydown.txt   
8 include_once scenarios/red_laydown.txt   
10 include_once scenarios/blue_sams.txt   
11   
12 event_output   
event_pipe file output/jacksonabad.evt   
end_event_output   
16   
17 event_pipe file output/jacksonabad.aer   
end_event_pipe   
20 end_time 1 hr   
21   
22 final_run_number 3 
```

DISTRIBUTioNC.Distributionauthorized toU.S.GovernmentAgenciesandtheircontractors,9-Aug-19. Otherrequestsforthisdocument shallbereferredtoAFRL/RQQD.

·What problems did this create?   
·Overwrites the files!

-Only one event and .aer files   
-Also,observer over-wrote its file

·How to address this?

-.aerand .evt files easy

·Using“_%d"makes copy for each replication

DISTRIBUTioNC.Distributionauthorized toU.S.GovernmentAgenciesandtheircontractors,9-Aug-19. Otherrequestsforthisdocument shall bereferredtoAFRL/RQQD.

# UNCLASSIFIED

![](images/d65d01b5bd22bbecf4300bd59df310da6bd58fc11c5b417d87af89e5b0c8520e.jpg)

# Multiple.aer&.evt Files

20

![](images/5083e462a9e1e01443d8830f1c69ecc14c039d83ea07499a7e8068b6b2827466.jpg)

# floridistan.txt

```txt
floridistan.txt*  
1 # File generated by Wizard 2.6.0 on Apr 10, 2020.  
2 file_path .  
3 file_path ../models  
4  
5 log_file output/jacksonabad.log  
6 include_ once setup.txt  
7 include_ once scenarios/blue_laydown.txt  
8 include_ once scenarios/red_laydown.txt  
9 include_ once scenarios/blue_sams.txt  
10 include_ once scenarios/red_sams.txt  
11 include_ once scenarios/blue_sams.txt  
12  
13 event_output file output/jacksonabad_%d.evt end_event_output  
14 event_pipe file output/jacksonabad_%d.aer end_event_pipe  
15 end_time 1 hr  
16 end_time 1 hr  
17  
18 final_run_number 3  
19 
```

DISTRIBUTioNC.Distributionauthorized toU.S.GovernmentAgenciesandtheircontractors,9-Aug-19

Otherrequests forthisdocument shallbereferredtoAFRL/RQQD.

![](images/4b78d6e29bf35768417d2c7a24522123afe7c64d23a611b86243feda30d89ad4.jpg)

DISTRIBUTioNC.Distributionauthorized toU.S.GovernmentAgenciesandtheircontractors,9-Aug-19. Otherrequestsforthisdocument shall bereferredtoAFRL/RQQD.

# UNCLASSIFIED

![](images/124828766a9ffe57b9710d8cd0b589714bfb655a4829484e3c2e3b98cbde3e79.jpg)

# 观察者

22

![](images/194413c2af59a7cdc635f99a966028ba95d473146f7262c4d79d269cf29fc810.jpg)

·如何阻卡多次运行观察者覆盖文件？  
·线索：

－帮助文档查看FilelO 的Open方法  
－帮助文档查看WsfSimulation方法

observers.txt   
19   
20 script void SimulationComplete()   
21 FileTO output $=$ FileTO();   
22 int runNum $\equiv$ WsfSimulationRUNumber();   
23 if(runNum $\equiv = 1$ ) output.Open("output/hits.txt","out"); else output.Open("output/hits.txt","append");   
28   
29   
30 foreach(string name:int hits in samHits) { output.WriteLn(write_str"in run"，runNum，"，"，name，"was hit"，hits，"times")； } output.Close();   
35 endScript

·RUN!!!

DISTRIBUTioNC.Distributionauthorized toU.S.GovernmentAgenciesandtheircontractors,9-Aug-19. Otherrequestsforthisdocument shall bereferredtoAFRL/RQQD.

![](images/7173b6cd8538fe64df8c719574323350f516da27be5fd739dc09aa71521285a9.jpg)

# 观察者输出到文件

![](images/b2c2af9c272c1caa9d5516b354e6e9febea005ecd021129887f3cd7a2329c92f.jpg)

UNCLASSIFIED   
Hits.txt   
```csv
output/hits.txt   
1 in run 1,bomber_1_red_gps_bomb_1_3 was hit 1 times   
2 in run 1,bomber_1_red_gps_bomb_1_4 was hit 1 times   
3 in run 1,bomber_2_red_gps_bomb_1_2 was hit 1 times   
4 in run 1,bomber_2_red_gps_bomb_1_4 was hit 1 times   
5 in run 1,tank_1 was hit 1 times   
6 in run 1,tank_2 was hit 1 times   
7 in run 2,bomber_1_red_gps_bomb_1_3 was hit 1 times   
8 in run 2,bomber_1_red_gps_bomb_1_4 was hit 1 times   
9 in run 2,bomber_2_red_gps_bomb_1_2 was hit 1 times   
10 in run 2,bomber_2_red_gps_bomb_1_4 was hit 1 times   
11 in run 2,tank_1 was hit 1 times   
12 in run 2,tank_2 was hit 1 times   
13 in run 3,bomber_1_red_gps_bomb_1_3 was hit 1 times   
14 in run 3,bomber_1_red_gps_bomb_1_4 was hit 1 times   
15 in run 3,bomber_2_red_gps_bomb_1_2 was hit 1 times   
16 in run 3,bomber_2_red_gps_bomb_1_4 was hit 1 times   
17 in run 3,tank_1 was hit 1 times   
18 in run 3,tank_2 was hit 1 times   
19 
```

DISTRIBUTioNC.Distributionauthorizedto U.S.GovernmentAgenciesand theircontractors,9-Aug-19. Otherrequestsforthisdocument shallbereferredtoAFRL/RQQD.

observers.txt   
19   
20 script void SimulationComplete()   
21 FileIO output $=$ FileIO();   
22 string runNum $=$ (string)WsfSimulationRUNumber();   
23 output.Open("output/hits"+runNum+.txt","out");   
25   
26 foreach (string name : int hits in samHits)   
27 { output.Writeln(write_str(name, " was hit ", hits, " times"));   
29 }   
30 output.Close();   
31 end_script   
32

DISTRIBUTioNC.Distributionauthorized toU.S.GovernmentAgenciesandtheircontractors,9-Aug-19. Otherrequestsforthisdocument shall bereferredtoAFRL/RQQD.

26

# UNCLASSIFIED

![](images/c6e5a4572c9f284d7cb17f63a332b26303ae5504fcfaab837fff0654336e9e70.jpg)

# 现在我们拥有了多个观察者文件

![](images/28ff32822916f58ccf78b4db8d8375280564fad2ee0af34d6a3ca565ee34710b.jpg)

![](images/3aa7b949f1557ca74d6165d3e88d2c7178b98972f1b292d7227593d52149752f.jpg)

DISTRIBUTioNC.Distributionauthorized toU.S.GovernmentAgenciesandtheircontractors,9-Aug-19. Otherrequestsforthisdocument shallbereferredtoAFRL/RQQD.

·本节包含以下内容：

-使用WsfDraw脚本  
-创建一个脚本观察者(script observer)

![](images/92906a91d4979aaf83f5f582986f39f8ea3d1a7bca3b9d8e294eb98d648c4f06.jpg)

DISTRIBUTioNC.Distribution authorized to U.S.Government Agenciesand their contractors,9-Aug-19. Otherrequestsforthisdocument shallbereferredtoAFRL/RQQD.

# 6.1.6. 任务处理和通信 6_Task_Processors_and_Comms

# 6.1.6.1. 任务处理器状态机 10_AFSIM_User_Training_TaskProcessorStateMachines

# 6.1.6.1.1. 本节想定解析

本节想定为：

afsim2.9_src\training\user\6_Task_Processors_and_Comms\scenarios\solutions\10_Task_Pr ocessors_And_State_Machines\floridistan\floridistan.txt

![](images/5ce77b55fd5f3937d16e0da147cc8d15f8c8fe4a15426926cd6b66f7a94c9cc5.jpg)

# 红方兵力

一艘航母 ship_1

定义了一个循环的路线

一架轰炸机 bomber_1（另一架 bomber_2 与 bomber_1 配置相同）

□ 定义了一个路线，先到陆地，再回到海上  
□ 设置了固定跟踪 tank_1,tank_2，只有跟踪了才能投弹  
□ 挂了 4 枚 GPS 制导炸弹，最大允许同时齐射 2 枚

设置当在 gps 制导炸弹的打击范围内时才开火(double lar_meters $=$ 18520)  
打击 tank_1, tank_2 的炸弹同时开火，针对每个目标又齐射 2 枚，相当于四枚一次打完

□ 当有打击目标时，实时的绘制当前飞机弹的攻击范围

GPS 制导炸弹

□ 本例中被挂在了 bomber_1 上  
□ 弹的雷达特征 RCS 被设置为了常数 1 $m ^ { 2 }$ ，换算为 dbsm 则是 0

# 蓝方兵力

一个在天上的卫星 satellite_1

▫ 定义了一个 700km 的轨道

两辆坦克 tank_1, tank_2

一个车辆

▫ 定义了一个向北行进的路线

一个地空导弹阵地 sam_1

▫ 下挂 16 枚地空导弹，因为 acq 雷达的探测距离是 150 海里，远大于红方轰炸机 gps炸弹的攻击距离 18520 米，所以 sam 的 acq 雷达先发现目标，对两架红方的轰炸机进行打击

□ 下挂 2 部雷达，一部 150 海里（acq，开启），一部是 100 海里（ttr，默认关），  
□ 其它定义包括通信、区域等在推演时均未有动作

# 公共

建了一个统计场景中打击次数的脚本（统计 WEAPON_HIT 事件），并输出发生该事件的平台。  
建立了蒙特卡洛多次仿真的方法，并将多次仿真的结果分开输出。

# 6.1.6.1.2. 本节 PPT 资料

本文为 afsim2.9_src\training\user\6_Task_Processors_and_Comms\slides\10_AFSIM_User_Training_TaskProcessorStateMachines.pptx 的翻译。

![](images/a726853a98438430ede01bedc6ace2e216bc6448422427467fded9bd9017ca78.jpg)

Integrity★Service★ Excellence

# AFSIM用户培训10－任务处理器状态机

13324598743

# AFRL/RQQD美国空军研究实验室

DISTRIBUTioNC.DistributionauthorizedtoU.S.GovernmentAgenciesandtheircontractors,9-Aug-19. Otherrequestsfor thisdocument shall bereferred toAFRL/RQQD.

# UNCLASSIFIED

![](images/6cd0791b8cb5be328a68e46183da4a0fde0f434a8cc21ab1a7c6a14f742e2124.jpg)

# 学习目标

![](images/72f39636565cebe9bff639991215a30d11ede0074d8d225a03c4f1b16109ac04.jpg)

·包含以下内容：

－构建一个任务处理器状态机  
－将一个状态机绑定到一个平台上

![](images/2a7fe0b2aa039736cfe1634445384e832a468d046dc6f578861012658717ef6a.jpg)

DISTRIBUTioNC.Distributionauthorized toU.S.GovernmentAgenciesandtheircontractors,9-Aug-19. Otherrequestsforthisdocument shallbereferredtoAFRL/RQQD.

![](images/b71dd7fb99db2a8516d9d52443fc54c6743855d219e5006d42c34bd688c1a6d5.jpg)

DISTRIBUTioNC.DistributionauthorizedtoU.S.GovernmentAgenciesandtheircontractors,9-Aug-19. Otherrequestsfor thisdocument shall bereferred toAFRL/RQQD.

![](images/38835abccc189e78bfde2bf7e3918ebf872da6b571c2d4638d0eefdc2c2de5d6.jpg)

# UNCLASSIFIED

# 状态格式

![](images/e774b75a18101683673ba8dee3e4bbc14d2f5390ab24fed7c36dfbeef1126dde.jpg)

state<state-name>

Defines a state in a statemachine with the name<state-name>

on_entry..end_on_entry

Whenentering this state,performsthese scriptcommands.Thisisanoptional subcommand

on_exit...end_on_exit

When leaving thisstate.performs these script commands.This isanoptional subcommand

next_state<next-state-name>...end_next_state

i eisi osideatii cycles

The state command definition structure

state <state-name> xt_st<seript-commands>e-1 end next state next.state <next-state-name-2> end next state end _state

#

DISTRIBUTioNC.Distributionauthorized toU.S.GovernmentAgenciesandtheircontractors,9-Aug-19. Otherrequestsforthisdocument shallbereferredtoAFRL/RQQD.

![](images/3ccf3ba2e3cd9b99d29c28d9071efe41df4e0e93657023b848aea77fc707bd85.jpg)

DISTRIBUTioNC.Distributionauthorized toU.S.GovernmentAgenciesandtheircontractors,9-Aug-19. Otherrequestsforthisdocument shall bereferredtoAFRL/RQQD.

5

![](images/6e806fe0124ba2e8e69586eddd3e89fe53111f4e7cb63fea591255ce78aac0c9.jpg)

# UNCLASSIFIED

# 状态内部如何工作

![](images/16f318bbddfd15e4138e5cc548189a2a9a0f6a36ada9cbebd5a7299b2414589f.jpg)

![](images/4eae64adb54ca8708c58317154cb1552990a575da5899a06e82aa28f53807a39.jpg)

DISTRIBUTioNC.Distributionauthorized toU.S.GovernmentAgenciesandtheircontractors,9-Aug-19. Otherrequestsforthisdocument shallbereferredtoAFRL/RQQD.

on_entry block

DISTRIBUTioNC.Distributionauthorized toU.S.GovernmentAgenciesandtheircontractors,9-Aug-19. Otherrequestsforthisdocument shall bereferredtoAFRL/RQQD.

7

# UNCLASSIFIED

![](images/57c0de0251e221de0e064131ad770d1a30f909e288d9d539491229a3726fe018.jpg)

# 任务处理器状态机基本

![](images/96d3429822020ac5a248680b6fb3dad2e05108f00fab88f6f38b4909f0f23e99.jpg)

·状态机以轨迹（track）为基础运行。  
·每条轨迹都会"启动"状态机。

－轨迹从文件中列出的第一个状态开始！

·每条轨迹都是独立处理的。  
·定时是基于轨迹的到达时间和评估间隔。  
·当一条轨迹被清除时，处理会直接停止。

·状态机以轨迹（track）为基础运行。  
·每条轨迹都会"启动"状态机。  
－轨迹从文件中列出的第一个状态开始！  
·每条轨迹都是独立处理的。  
·定时是基于轨迹的到达时间和评估间隔。  
·当一条轨迹被清除时，处理会直接停止。

DISTRIBUTioNC.DistributionauthorizedtoU.S.GovernmentAgenciesandtheircontractors,9-Aug-19. OtherrequestsforthisdocumentshallbereferredtoAFRL/RQQD.

9

![](images/9d854c58242fa848859f9c5e590b54c4b6255fc4f65c980a22ea9a1d429d1c7e.jpg)

# UNCLASSIFIED

# 任务处理器状态机基本

![](images/09c46c556c0dd0b1324bf1b2b492100c2d01059ea8fed79ed9e4ec01d246c0ee.jpg)

·状态机以轨迹（track）为基础运行。  
·每条轨迹都会"启动"状态机。

－轨迹从文件中列出的第一个状态开始！

·每条轨迹都是独立处理的。  
·定时是基于轨迹的到达时间和评估间隔。  
·当一条轨迹被清除时，处理会直接停止。

DISTRIBUTioNC.Distributionauthorizedto U.S.Government Agenciesand theircontractors,9-Aug-19.

Otherrequests forthisdocument shallbereferred toAFRL/RQQD.

·在此示例中，每个新创建的轨迹（track）最初都会进入第一个状态（FIRSTstate）。  
·在此处理器中，FIRST列在SECOND之前，因此它将是第一个被评估的状态。

```txt
evaluation_interval FIRST 10.0 sec  
state FIRST  
next_state SECOND  
if (1 < 2) return true;  
else return false;  
end_next_state  
end_state  
evaluation_interval SECOND 10.0 sec  
state SECOND  
end_state 
```

DISTRIBUTioNC.Distributionauthorized toU.S.GovernmentAgenciesandtheircontractors,9-Aug-19. Otherrequestsforthisdocument shall bereferredtoAFRL/RQQD.

11

![](images/1540f39a6048f2a772d17370a272424845653c18144712240f1a11c10ae49cc3.jpg)

# UNCLASSIFIED

# 任务处理器状态机基本

![](images/18265f12f1870aab977fc0a3d85617005751dcd2b65522bd0afa18a845d99c64.jpg)

·状态机以轨迹（track）为基础运行。  
·每条轨迹都会"启动"状态机。

－轨迹从文件中列出的第一个状态开始！

·每条轨迹都是独立处理的。  
·定时是基于轨迹的到达时间和评估间隔。  
·当一条轨迹被清除时，处理会直接停止。

DISTRIBUTioNC.Distributionauthorized toU.S.GovernmentAgenciesandtheircontractors,9-Aug-19 Otherrequestsforthisdocument shallbereferredtoAFRL/RQQD.

·状态×的评估间隔为10秒。它用于引导平台的运动，具体来说，它会直接转向轨迹（track）当前位置。

·轨迹A在21秒时进入状态X；轨迹B在26秒时进入状态X。两者都会停留在状态X，直到平台到达轨迹的位置。

·那么，平台会移动到哪里？

![](images/1493e5590bc7e8f8bc9d8420da9d76bd3fbcaa503601a684974e069e65ecb938.jpg)

DISTRIBUTioNC.Distributionauthorized toU.S.GovernmentAgenciesandtheircontractors,9-Aug-19. Otherrequestsforthisdocument shall bereferredtoAFRL/RQQD.

13

![](images/919fb1060d743a7fa7b06fc0402e703f4be30bb2468c02021a8c9481363edffc.jpg)

# UNCLASSIFIED

# 任务处理器状态机基本

![](images/2f55efe731e7a64d91c7d8f3103ba54217815df9af046e41b7494c85486d55a4.jpg)

·状态机以轨迹（track）为基础运行。  
·每条轨迹都会"启动"状态机。

－轨迹从文件中列出的第一个状态开始！

·每条轨迹都是独立处理的。  
·定时是基于轨迹的到达时间和评估间隔。  
·当一条轨迹被清除时，处理会直接停止。

DISTRIBUTioNC.Distributionauthorized toU.S.GovernmentAgenciesandtheircontractors,9-Aug-19 Otherrequestsforthisdocument shallbereferredtoAFRL/RQQD.

·状态×的评估间隔为10秒。

·轨迹A在第21秒进入状态X；轨迹B在第26秒进入状态X。两者都未通过"下一状态”（NextState）模块。

·在第50秒时，发生某些事情使"下一状态”（NextState）模块变为有效。

－轨迹A将在第51秒转到"下一状态”；  
－轨迹B将在第56秒转到"下一状态”。

Time

A

21

31

51

![](images/5c7e6ef1992db7ca49d8b58774d32ac644e9b47cab9b4a1abf1a365d2819d370.jpg)

B

26

36

46

56

![](images/132073723b826287283794ceff1eadba7c577ab87617581a2a32121c72b7c07d.jpg)

DISTRIBUTioNC.Distributionauthorized toU.S.GovernmentAgenciesandtheircontractors,9-Aug-19. Otherrequestsforthisdocument shall bereferredtoAFRL/RQQD.

15

# UNCLASSIFIED

![](images/80dcebde7948c14a7b07d3760ef3407e3f59cc1372d40efae740451a325d3fda.jpg)

# 计时示例（第三部分）

![](images/7d9be30c97348eddb4366ddc15d2d838c5722753a30eccb2abbec5631ef542d6.jpg)

·状态X的评估间隔为10秒。  
·轨迹A在第21秒进入状态X；轨迹B在第26秒进入状态X。两者都未通过"下一状态”（NextState）模块。  
·然而，在第45秒时，发生了释放事件（releaseevent），允许轨迹进入“下一状态”。  
·现在，谁会先离开？一轨迹B在第46秒离开，而轨迹A在第51秒离开。

Time

A

31

41

51

![](images/756267b5cc0660146bc1d3d34de550b213e0e915b1c59de134bd9cf756a3a0e6.jpg)

B

26   
36

46 46 46

·状态机以轨迹（track）为基础运行。  
·每条轨迹都会"启动"状态机。

－轨迹从文件中列出的第一个状态开始！

·每条轨迹都是独立处理的。  
·定时是基于轨迹的到达时间和评估间隔。  
·当一条轨迹被清除时，处理会直接停止。

DISTRIBUTioNC.Distributionauthorized to U.S.Government Agenciesand their contractors,9-Aug-19. OtherrequestsforthisdocumentshallbereferredtoAFRL/RQQD.

# UNCLASSIFIED

![](images/16fb6529e2be7c5527829c95585c0c8ab20d167e6597508a9561e37a31a21932.jpg)

# 丢弃的轨迹

![](images/88a1633b862387053d04e94b85f0fc2caeba0fc0b0ce2349d115b397cc9386b1.jpg)

·状态X的评估间隔为10秒，用于引导平台的运动。具体来说，它会直接转向轨迹当前所在的位置。  
·轨迹A在第21秒进入状态X，并在第40秒被丢弃。  
·问题：平台将会去哪里？

![](images/86657f038cc5c7c7b969ba1aac010550b3a38f8295e7c9ca556052c2d293a487.jpg)

DISTRIBUTioNC.Distributionauthorized toU.S.GovernmentAgenciesandtheircontractors,9-Aug-19 Otherrequestsforthisdocument shallbereferredtoAFRL/RQQD.

·状态机以轨迹（track）为基础运行。  
·每条轨迹都会"启动"状态机。

－轨迹从文件中列出的第一个状态开始！

·每条轨迹都是独立处理的。  
·定时是基于轨迹的到达时间和评估间隔。  
·当一条轨迹被清除时，处理会直接停止。

DISTRIBUTioNC.Distributionauthorized toU.S.GovernmentAgenciesandtheircontractors,9-Aug-19. Otherrequestsforthisdocument shall bereferredtoAFRL/RQQD.

# UNCLASSIFIED

![](images/fc4db8f9d45cbd9c05ec1a0b029b57e80ba39af6d204d44aee5a60271e3ae10d.jpg)

# 状态机设计

19

![](images/b9055b4b2b50e05162dc78e1c08678590641872592567fb9e41c666529fc3d13.jpg)

·防空（SAM）逻辑：  
·侦察目标（Detected）

－如果是友军就忽略它  
－满足交战条件就交战（Engage）

·交战（Engage）

－向目标开火

·等待（Wait）看目标是否被击杀－如果交战条件还被满足，就继续交战

![](images/c2d6aec70ee00f243a57399d4ea682a85567bd618a05e40c843b646ca5ab8eb8.jpg)

DISTRIBUTioNC.Distributionauthorized toU.S.GovernmentAgenciesandtheircontractors,9-Aug-19 Otherrequestsforthisdocument shallbereferredtoAFRL/RQQD.

·创建新的任务处理器文件

-在"single_large_sam.txt"中添加"include_once processors/single_large_sam_tactics.txt"

platforms/single largesam.txt   
```txt
7 include_once weapons/sam/large_sam.txt   
8 9 include_once sensors/radar/acq_radar.txt   
10 include_once sensors/radar/ttr_radar.txt   
11 include_once processors/single_large_sam_tactics.txt   
12 
```

－创建并打开新文件

DISTRIBUTioNC.Distributionauthorized toU.S.GovernmentAgenciesandtheircontractors,9-Aug-19. Otherrequestsforthisdocument shall bereferredtoAFRL/RQQD.

# UNCLASSIFIED

![](images/10df6378b254afc0390b0f8f00a6050d45afdf2eaede018bfbd2f772212f059c.jpg)

# 变量块

21

![](images/d3b96580b71a78b86863f26c93796663d567640a7b26fa3032dcbdb7a850e179.jpg)

·防空（SAM）的任务处理器WSF_TASK_PROCESSOR

－我们需要申请几个变量？

·发射范围   
·齐射数量  
·武器名称

processors/single_large_sam_tactics.txt   
2   
3 processor SINGLE LARGE SAM TACTICS WSF_TASKPROCESSOR   
4   
5 script_variables   
6 double launchRange $= 20.0$ \*MATH.M_PER_NM();   
7 double salvoSize $= 2$ 8 string weaponName $= \mathrm{"sam"}$ 9 end.script_variables   
10   
11 end Processor

DISTRIBUTioNC.Distributionauthorized toU.S.GovernmentAgenciesandtheircontractors,9-Aug-19

Otherrequests forthisdocument shallbereferred toAFRL/RQQD.

·需要有一个脚本来测试交战条件是否满足：

－武器是否可用  
－武器数量是否满足一次齐射  
目标是否有效  
－目标是否在打击范围内  
－当前未在正在开火的状态

DISTRIBUTioNC.Distributionauthorized toU.S.GovernmentAgenciesandtheircontractors,9-Aug-19. Otherrequestsforthisdocument shall bereferredtoAFRL/RQQD.

UNCLASSIFIED

# CanEngage()

23

![](images/350573db426736a92c5fa0c81278db4978784f83df638387ec7f1d210bc2c6ca.jpg)

![](images/41c3391166b44ceccce93574d613a3643b604388e17c3e66a8a2680b7286d704.jpg)

processors/single_large_sam_tactics.txt

10 script bool CanEngage() bool canEngage $=$ false; WsfWeapon sam $=$ PLATFORM.Weapon(weaponName); if (sam.IsValid()) && sam.QuantityRemaining() $\rightharpoondown$ salvoSize && TRACK.Target().IsValid() && PLATFORM.GroundRangeTo(TRACK) < launchRange && WeaponsActiveFor(TRACK.TrackId()) < 1) { canEngage $=$ true; } return canEngage; end-script

DISTRIBUTioNC.Distributionauthorized toU.S.GovernmentAgenciesandtheircontractors,9-Aug-19. Otherrequestsforthisdocument shallbereferredtoAFRL/RQQD.

processors/single_large_sam_tactics.txt

·创建所有必要的next_state块的状态模型

－无需逻辑—仅为空块！

·DETECTED是入口点（第一个状态）  
·为除IGNORE状态外的所有 状态定义10秒的评估间隔 （IGNORE的评估间隔为24 小时)

![](images/0a6ff6e7135c3f97b99e0b54ba42f4189aff2ab4fd356e7ce034393d31aa6d64.jpg)

DISTRIBUTioNC.Distributionauthorized toU.S.GovernmentAgenciesandtheircontractors,9-Aug-19. Otherrequestsforthisdocument shall bereferredtoAFRL/RQQD.

# UNCLASSIFIED

# 解决方案：状态布置

25

![](images/e94446eb23634dffb41b7c9f53f61908fe07f701c3af50b133bd24d77ed79407.jpg)

![](images/67509ac96fa723433121f842a7c1bb1edd09ebe45a7f5a7abdf99cda66950501.jpg)

processors/single_large_sam_tactics.txt

```txt
24   
25 evaluation_interval DETECTED 10 sec   
26 evaluation_interval ENGAGE 10 sec   
27 evaluation_interval WAIT 10 sec   
28 evaluation_interval IgNORE 24 hr   
29   
30 state DETECTED next_state IGNORE end_next_state   
31   
32   
33 next_state ENGAGE   
34 end_next_state   
35   
36   
37   
38 state ENGAGE next_state WAIT   
39   
40 end_next_state   
41   
42   
43 state WAIT next_state ENGAGE   
44 end_next_state   
45   
46 end_state   
47   
48   
49   
50   
51   
52 end Processor 
```

![](images/82749e2ae575370d05650e39e8c8bf1e2a21d318b7f1e198c3725afe398ddb40.jpg)

DISTRIBUTioNC.Distributionauthorized toU.S.GovernmentAgenciesandtheircontractors,9-Aug-19. Otherrequestsforthisdocument shallbereferredtoAFRL/RQQD.

·evaluation_interval决定了next_state 块的评估频率。  
·第一个next_state 块用于判断是否为友方状态。

－如果是友方状态，则进入终止状态“IGNORE”。

·第二个next_state 块调用我们的 CanEngage()脚本。

－如果可以交战，则进入ENGAGE状态。

DISTRIBUTioNC.Distributionauthorized toU.S.GovernmentAgenciesandtheircontractors,9-Aug-19. Otherrequestsforthisdocument shall bereferredtoAFRL/RQQD.

# UNCLASSIFIED

![](images/23e3935398539241ba8a28a5b7e8a1592ad4ac4d9deb48c6fcd22b8d1938c3be.jpg)

# 第一阶段-侦察阶段（DETECTED）

![](images/4b8489a9a7b902c470d581e15d922c3f8182de01ee2f478bccb530b0601281a2.jpg)

processors/single_large_sam_tactics.txt

·next_state IGNORE

-返回true/false:

·友方

·next_state ENGAGE

-返回 true/false:

·如果我们可交战

![](images/57560283982a15d9dedc22853125635eb999542256bbc078312542e9c09b0835.jpg)