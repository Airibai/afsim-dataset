- Fire是处理里的一个方法

- 如果开火任务分配成功则返回真

processors/single_large_sam Tactics.txt

![](images/b87e7915793ff9c5b6e374fb578cfab30edf4e41f49f0a6ecb193da2651a5619.jpg)

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQQD.

29

![](images/70a77d6dcfe3e9cdaa4a6d064368b23bc8d3429f0e83e9be7917a19a36564177.jpg)

UNCLASSIFIED

# 第三阶段-侦察阶段（WAIT）

![](images/357b94440d5af339f4b1560f4a6dc2629052691d3d36f90e8a6f7a725eb032e9.jpg)

- next_state 块与我们在 DETECTED 状态中编写的完全相同。

![](images/02d98f3fdeecc68abe7bb008f5df30f6d9bbdd06c5a0ef5d439665a651d11f60.jpg)

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

- 任务处理器使用SINGLE_largeSAM_TACTICS类型  
- Run!!!

platforms/single_largeSAM.txt

```txt
50 weapon sam LARGE_SAM   
52 quantity 16   
53 endweapon   
54   
55 processor data_mgr WSFTRACKPROCESSOR   
56 purge_interval 60 seconds   
57 end Processor   
58   
59 processor task_mgr SINGLE LARGE_SAM_TACTICS # WSF_TASKPROCESSOR   
60 end处理器   
61   
62 endPLATFORM_type
```

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQQD.

31

![](images/f6a65ba5a87293fdee74eb921155b0b55d70309f15b257cc0a314a730964f768.jpg)

# UNCLASSIFIED

# 程序执行

![](images/20dcdaeb8d5e33bdd9a6e33bfe8d569664ce25863581e2f133e419ca7d4d192f.jpg)

![](images/72ac17dbd5a0bc0a29303b3d9f977bdebbc2c53e6204c4dfb37737eae117d6cc.jpg)

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQQD.

- 您将获得以下方面的实操知识：

一 构建状态机  
- 将状态机附加到平台

- 提醒：关于任务处理器……

- 状态机在轨迹（tracks）上运行。  
- 每条轨迹都会“启动”状态机。  
- 轨迹会从文件中列出的第一个状态开始。  
- 每条轨迹会被独立处理。  
- 定时基于轨迹的到达时间和评估间隔。  
- 当轨迹被清除时，处理会简单地停止。

![](images/763d31bf6ee9a2b96766bfc3a5890192d9c69c75be46736d0545bb2e8af3216f.jpg)

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQQD.

UNCLASSIFIED

![](images/0d0407daaa9d208c02def9b10f7d477cc0c91127b2ca970f59cad859b8ad5ea7.jpg)

33

![](images/64ff33bf74c5d5480273486d97ac6e099e4071f1043dafb10fef06b8670c3e88.jpg)

![](images/7ed6a8caeb76f1af08a2c2a7971310fd5ad4c88d8bd074e67ecff73e937937be.jpg)

# 备用PPT

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQQD.

35

![](images/cef060737c93ac6b67fcdbab7c4a2b74bf2ebf8c96086ebb1ca0339bb0fbfa44.jpg)

# 状态机示例 - 固定电话

![](images/75f27c84ce841d11d1ac3455f3811074fd880ce696ad5099d39f76e44cf1f52f.jpg)

![](images/cfab4aec0db10c4ba3b3f0b7a5bfbf3353abaf251efabd0d71fde30f51707430.jpg)

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQDD.

![](images/1e8d3ce3635c3f714dd2ecf7742dbb682a5bb5cf8cdd7c6c81203563f2b4c2fe.jpg)  
“交易”以硬币进入和离开机器开始和结束

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQQD.

# UNCLASSIFIED

# 交易视图代码

37

![](images/59019386aba8b00b352980c687a305f3c500b55062b02d4f054084826a7f251a.jpg)

![](images/ae065522a37671502076b75b2d74d4a32442de704e945e768fad42efb3e98499.jpg)

```txt
1 # New file created by AFNES IDE   
2 processor VENDINGMACHINE WSF_TASKPROCESSOR   
3 # these are dummy scripts to make the state machine compile   
4 # to actually work, real code would have to be put in here   
5 script bool enoughCoins() return true; end script   
6 script bool rejectCoins() return true; end script   
8 script bool cancelOrder() return true; end script   
9 script bool selectionMade() return true; end script   
10 script void returnChange() end script   
11   
12 evaluation_interval COUNTCoins 1 sec   
13 evaluation_interval SELECT_SODA 1 sec   
14 evaluation_interval DISPENSE 10 days   
15 evaluation_interval GIVE_CHANGES 10 days   
16   
17 state COUNTCoins   
18 on entry   
19 writeln("have received some coins");   
20 end on entry   
21   
22 next state GIVE_CHANGES   
23 return (rejectCoins()) | | cancelOrder());   
24 end next state   
25   
26 next state SELECT_SODA   
27 return enoughCoins();   
28 end next state   
29 end state   
30 
```

```txt
30 state SELECT_SODA on entry writeIn("Please make a selection"); end on entry   
35 next state GIVE_CHANGES return cancelOrder();   
38 end next state   
39   
40 next state DISPENSE return selectionMade();   
42 end next state   
43 end state   
44   
45 state DISPENSE   
46 next state GIVE_CHANGES return true;   
48 end next state   
49 end state   
50   
51 state GIVE_CHANGES on entry returnChange(); end on entry   
53 end state   
54   
55 end processor   
56 
```

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQDD.

- 被“追踪”的“对象”是一个交易。

- 该处理器假设交易在完成后会很快被“丢弃”，即饮料被分发后。

- 实际的状态机只有 37 行代码

- 处理逻辑已经被移至脚本中。

- 不同的状态有不同的评估间隔。

- 终止节点不需要重新评估。

- 每个状态必须有一个评估间隔。

- 评估间隔通常被放置在状态附近。

- 这个处理器假设的机器是什么类型？

- 单一产品类型，且所有产品价格相同。

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQQD.

# UNCLASSIFIED

![](images/d7f625e0b6d4636daea98776ac7f99842fc7dd9282c9fd62f2d3f6cd0f1b03b7.jpg)

# 任务处理器状态机基础

![](images/21023b3bd20e86284456401f4ae9bdc5978a7147913959a8f94933f4e7466af0.jpg)

状态机在轨迹（tracks）上运行。

- 每条轨迹都会“启动”状态机。  
- 轨迹从文件中列出的第一个状态开始！  
- 每条轨迹独立处理。  
- 计时基于轨迹的到达时间和评估间隔。  
- 当轨迹被丢弃时，处理会简单地停止。

![](images/59064230911437ec1bb1ffe6ac1778fa73cacc40e43fd92810345560c71c9ff6.jpg)

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQQD.

# UNCLASSIFIED

# 客户视图代码

41

![](images/928658270f9c1f307341f9764efc1ffb54ced269f0afc2dc6f4b87afb5f49d6f.jpg)

![](images/658c86dfc3aa098d4e71a0e2da4b8315d4213d82a5db406cf778d5197e21a450.jpg)

<table><tr><td>1</td><td># New file created by AFNES IDE</td></tr><tr><td>2</td><td>processor VENDINGIMACHINE2 WSF_TASKPROCESSOR</td></tr><tr><td>3</td><td></td></tr><tr><td>4</td><td># these are dummy scripts to make the state machine compile</td></tr><tr><td>5</td><td># to actually work, real code would have to be put in here</td></tr><tr><td>6</td><td>script bool receivedCoins() return true; end script</td></tr><tr><td>7</td><td>script bool enoughCoins() return true; end script</td></tr><tr><td>8</td><td>script bool rejectCoins() return true; end script</td></tr><tr><td>9</td><td>script bool cancelOrder() return true; end script</td></tr><tr><td>10</td><td>script bool selectionMade() return true; end script</td></tr><tr><td>11</td><td>script void returnChange() end script</td></tr><tr><td>12</td><td></td></tr><tr><td>13</td><td>evaluation_interval IDLE 1 sec</td></tr><tr><td>14</td><td>evaluation_interval COUNTCoins 1 sec</td></tr><tr><td>15</td><td>evaluation_interval SELECT_SODA 1 sec</td></tr><tr><td>16</td><td>evaluation_interval DispENSE 10 days</td></tr><tr><td>17</td><td>evaluation_interval GIVE_CHANGES 10 days</td></tr><tr><td>18</td><td></td></tr><tr><td>19</td><td>state IDLE</td></tr><tr><td>20</td><td>on entry</td></tr><tr><td>21</td><td>writeln(&quot; have received some coins&quot;);</td></tr><tr><td>22</td><td>end on entry</td></tr><tr><td>23</td><td></td></tr><tr><td>24</td><td>next state COUNTCoins</td></tr><tr><td>25</td><td>return receivedCoins();</td></tr><tr><td>26</td><td>end next state</td></tr><tr><td>27</td><td>end state</td></tr><tr><td>28</td><td></td></tr><tr><td>29</td><td>state COUNTCoins</td></tr><tr><td>30</td><td>next state GIVE_CHANGES</td></tr><tr><td>31</td><td>return (rejectCoins() || cancelOrder());</td></tr><tr><td>32</td><td>end next state</td></tr><tr><td>33</td><td></td></tr><tr><td>34</td><td>next state SELECT_SODA</td></tr><tr><td>35</td><td>return enoughCoins();</td></tr><tr><td>36</td><td>end next state</td></tr><tr><td>37</td><td>end state</td></tr><tr><td>38</td><td></td></tr></table>

<table><tr><td>38</td><td>state SELECT_SODA</td></tr><tr><td>39</td><td>on entry</td></tr><tr><td>40</td><td>writeIn(&quot;Please make a selection&quot;);</td></tr><tr><td>41</td><td>end on entry</td></tr><tr><td>42</td><td>next state GIVE_CHANGES</td></tr><tr><td>43</td><td>return cancelOrder();</td></tr><tr><td>44</td><td>end next state</td></tr><tr><td>45</td><td>next state DISPENSE</td></tr><tr><td>46</td><td>return selectionMade();</td></tr><tr><td>47</td><td>end next state</td></tr><tr><td>48</td><td>end state DISPENSE</td></tr><tr><td>49</td><td>next state GIVE_CHANGES</td></tr><tr><td>50</td><td>return true;</td></tr><tr><td>51</td><td>end next state</td></tr><tr><td>52</td><td>end state</td></tr><tr><td>53</td><td>state DISPENSE</td></tr><tr><td>54</td><td>next state GIVE_CHANGES</td></tr><tr><td>55</td><td>return true;</td></tr><tr><td>56</td><td>end next state</td></tr><tr><td>57</td><td>end state</td></tr><tr><td>58</td><td>end processor</td></tr><tr><td>59</td><td>state GIVE_CHANGES</td></tr><tr><td>60</td><td>on entry returnChange(); end on entry</td></tr><tr><td>61</td><td>next state TDLE</td></tr><tr><td>62</td><td>return true;</td></tr><tr><td>63</td><td>end next state</td></tr><tr><td>64</td><td>end state</td></tr><tr><td>65</td><td>end processor</td></tr><tr><td>66</td><td>end processor</td></tr><tr><td>67</td><td>end processor</td></tr><tr><td>68</td><td>end processor</td></tr></table>

- 被“追踪”的“对象”是一个客户。

- 允许客户继续向机器中投币。  
- 当客户离开时，客户将被“丢弃”。

- 状态机代码只有 47 行。  
- 在这两种模型中需要考虑哪些问题？

- 当第二个“轨迹”出现时会发生什么？  
- 当客户走开时会发生什么？

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQQD.

43

![](images/a92f7f3717abb15976859163056af41cb3d3c2e341d36643ee50424f3eac6231.jpg)

# UNCLASSIFIED

# 另一个状态机示例

![](images/1a8660a5c7e97908b12f7c515ef16a00b5f8dafb514b4caf5dd1e897ebcf947d.jpg)

![](images/6170c2e12c41600fc9013c2d229291a89e752c1dc910f187697da3ab63abeb16.jpg)

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

![](images/d9d20c3ab3599e8cfa7b79869e4f9d59f578a6fc83d0d4816b3d92257de501d3.jpg)  
DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQQD.

45

![](images/b3815f7460cf3f066990b1e8ee67519542c721d4929b1ba608ac44204dd927cb.jpg)

# UNCLASSIFIED

# BITES状态机示例

![](images/b07477dc5b0ec82b62cbc8f524bb025720d9c6e0872a6cb7a4efd6dd35575928.jpg)

![](images/8f95ee1dd8ac1941b31cdf6702b5992d66ea790ff421bc5ebebaf0a65caeb561.jpg)  
DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQDD.

![](images/eee151a13ac9506447246271714a192c8d5d9d3986a5dd2a5a819862be689d61.jpg)

![](images/05341e6eb7417a6a7fba55552e0402a2ebf5d41ec0f13ed18e49e9e307f7f0df.jpg)

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQDD.

# UNCLASSIFIED

# BITES代码细节

47

![](images/c57fe68abbb3c95f414ecdefafc82166f5104e78ba6a5a6d606a1fab40c9b159.jpg)

![](images/558243fb63c824452ee3bb894b4947c5ba75d833a462dfe9ff5435c4bef46618.jpg)

- “被追踪”的“对象”是受害者。  
- 状态机代码为65行。  
- 具体示例：

- 一个男孩在某天晚上10:00出生。他的父母让他一生都待在家里。到了他21岁生日那天，他决定走到街角的酒吧喝一杯啤酒。酒吧距离他家只有8分钟的路程。  
- 他在晚上10:01离开家。他的路途非常糟糕，他被三种不同的生物咬了三次。然而，这些咬伤并没有耽误他的行程。  
他在10:09进入酒吧，感觉很好。  
- 在 10:11, 当他走到酒保面前时, 他会点什么?  
啤酒、TruBlood™、脑浆奶昔，还是皮纳科拉达（Pina Colada）？

# 6.1.6.2. 指挥链与通信 11_AFSIM_User_Training_CommandChains_Comms

# 6.1.6.2.1. 本节想定解析

本节想定为：

afsim2.9_src\training\user\6_Task_Processors_and_Comms\scenes\scenarios\solutions\11_Comm and_Chains_And_Comms\floridistan\floridistan.txt

![](images/798117abeb46094a54e5e4f91121816affe7f859e22780023d7357ad089a600e.jpg)

# 红方兵力

一艘航母 ship_1

定义了一个循环的路线

- 一架轰炸机bomber_1（另一架bomber_2与bomber_1配置相同）

定义了一个路线，先到陆地，再回到海上  
。 设置了固定跟踪 tank_1, tank_2，只有跟踪了才能投弹  
挂了4枚GPS制导炸弹，最大允许同时齐射2枚

- 设置当在gps制导炸弹的打击范围内时才开火(double lar_meters = 18520)   
- 打击 tank_1, tank_2 的炸弹同时开火，针对每个目标又齐射 2 枚，相当于四枚一次打完

当有打击目标时，实时的绘制当前飞机弹的攻击范围

GPS制导炸弹

本例中被挂在了bomber_1上  
。弹的雷达特征 RCS 被设置为了常数 $1 \mathrm{~m}^{2}$ , 换算为 dbsm 则是 0

# 蓝方兵力

- 一个在天上的卫星 satellite_1

定义了一个 $700 \mathrm{~km}$ 的轨道

- 两辆坦克 tank_1, tank_2  
一个车辆

定义了一个向北行进的路线

两部远程预警雷达200_ew_radar和300_ew_radar

探测距离为 370.4 公里  
其发现目标会向100_radar_company汇报

一个雷达连100_radar_company

其收到200_ew_radar和300_ew_radar报上来的目标后会上报给10_iads_cmdr

一个联合防空指挥部10_iads_cmdr

其收到目标后，会下达给下级3500_large_sam_battalion去执行打击

一个地空导弹营3500_large_sam_battalion

。 收到目标后会分配给目标捕获雷达 3510_acq_radar 来锁定目标轨迹  
接着分配大型地空导弹跟踪雷达3520_large_sam_ttr  
当明确目标并进入射程，会命令一台地空导弹发射车来进行攻击比如3530_large_sam launcher

一部目标捕获雷达3510_acq_radar

探测范围277.8公里  
将捕获信息上报给3500_large_sam_battalion

一部地空导弹跟踪雷达3520_large_sam_ttr

探测范围 185.2 公里  
将捕获信息上报给3500_large_sam_battalion

· 三部地空导弹车 3530_large_sam launcher ， 3540_large_sam launcher ,  
3550_large_sam launcher   
带弹4发

# 公共

- 建了一个统计场景中打击次数的脚本（统计 WEAPON_HIT 事件），并输出发生该事件的平台。  
建立了蒙特卡洛多次仿真的方法，并将多次仿真的结果分开输出。

# 6.1.6.2.2. 本节PPT资料

本文为afsim2.9_src\training\user\6_Task_Proceors_and_Comms\slides\

11_AFSIM_User_Training_CommandChains_Comms.pptx 的翻译。

![](images/af495774f8916a0e0074ff087417f92c6780da09a86c79bccff7a61602f97f85.jpg)

Integrity $\star$ Service $\star$ Excellence

# AFSIM用户培训

# 11-指挥链、报告、通信

本文档由杨石兴翻译，该资料做为《AFSIM2.9参考手册》的一部分。没有《AFSIM2.9参考手册》的加杨石兴微信领取：13324598743

# AFRL/RQQD

# 美国空军研究实验室

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQDD.

1

![](images/e8074b393768ba3ab43c882f5d01a45242de60e316e96ce071dff77917a1fb84.jpg)

UNCLASSIFIED

# 学习目标

![](images/8498b3341e7d2815cb09ba3ca8fb1bbec40756d0a00d034c99ffdd8e670e405c.jpg)

- 包含以下内容：

定义指挥链  
定义通信和链路

![](images/d18a31880f3d9cfcbd972b91f0c9abaa7d02835b39ac6418b81c3b6b66106e41.jpg)

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

- 指挥链（Command Chains）

- 分级图  
- 可以用来寻址: 指挥端, 对端, 等等.

![](images/e57fb7d6253cba4b75bdde59366e60bb3a2bd8659b0cecfa4365cd037be61da5.jpg)

- 通信设备（Comm Devices）

- 允许外部平台之间通信

![](images/d05897d21c92148c6d6d1f2fa5466fc4b5bdb6e963e5e02a8cbe6c560a880d88.jpg)

汇报（Reporting）

- 指定消息发往哪儿  
- 使用外部链接，可以利用指挥链，但不是必须的。

![](images/528da4f587cab3dadda6f300d116056917a548aed8a598dfb3905fd23f2bcd81.jpg)

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

3

![](images/58ff4044dc23876409731033ea32141fab930e55a136a8dbc138889c16df8a55.jpg)

# UNCLASSIFIED

# 指挥链（Command Chains）

![](images/86b2fee56d307695c6ba67ca2e8718e609c319003397f22f9a4442e3cb9bdf3a.jpg)

commander<commander-name>

command_chain <command-chain-name> <commander-name>

- 平台的子命令，用来指定平台的直接上级，建立指挥和汇报关系
- 指挥链由指挥官、下属和同级组成  
- 每条指挥链必须有一个指挥官（可以是自身）。  
- 一个平台可以属于多个指挥链。  
- 一个平台可以有多个指挥官（位于不同的指挥链中）。  
- 如果指挥官不存在，不会产生编译错误
- 向导会标记平台名称，但程序依然会执行。

![](images/cc2f95c9bb0cc08a1c5a983ec05984acfb9be7fa002f41f261343c6e4e8608d0.jpg)  
- 定义平台的指挥官

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

5

![](images/e8f19696808ba9085d97500bf655d0d0155db7743a1f586cee6064fe2f81697f.jpg)

UNCLASSIFIED

# 指挥链示例 (来自文档)

![](images/e16b20035cf8657bceaacebe18c1ed2f98ab90f840a7f8cce673686e22b97cfb.jpg)

![](images/82fd0c383edf5301230c60211cbe8f1f7099c4e46b47d046862d1852d5b493da.jpg)

![](images/1e2b60a2325177f1f882b34a5c9cdfc9412d035bc2480de0313b0f0cf3632521.jpg)

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

- 三个平台都用了同一个指挥链  
- 飞机的指挥官是自己(SELF)
- 顶级指挥官  
- 两艘船的指挥官是飞机，向飞机汇报

![](images/cb7275e0b15223163924952cce88f1240064bff328efee856b99d01fa44bcc7d.jpg)

![](images/f32e605c01921e5595bd217ed7d8aa31b9a30e36adab74dad73753a7a45844f3.jpg)

![](images/e60b61342d5d75114bf4b5b680f54dca3c7baf69f8b344ac58dd18a34680f1d9.jpg)

![](images/7976ca1f545f1305bd9a55dce8c89365188ccf1dec11ed2d9a7a5ddeb511f3a1.jpg)

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQQD.

7

![](images/28d9d02b064e1dd2201a0ac1080987517e48dbaf2d860077262357d6053d6d37.jpg)

UNCLASSIFIED

# 平台（Platform）默认

![](images/111a759e22591773715a18e525eb2caa32f348419ec32699d767decb8081660f.jpg)

- 每个平台都有以下默认值：

- 指挥链

- 指挥官名称（Commander name）SELF  
- 指挥链名称（Command Chain name） “default”

- 当分析一个命链时的使用注意

- 测试是不是顶端指挥官：

- if(PLATFORM.Commander().Name() == PLATFORM.Name())

- 指挥链（Command Chains）

-分级图  
- 可以用来寻址: 指挥端, 对端, 等等.

![](images/f784ddaeec6c23c37aa8c52c69ce2b27f8e790c1efe478fce70b757cada0acac.jpg)

- 通信设备（Comm Devices）

- 允许外部平台之间通信

![](images/275517cfb2b83c42f7019833af6a1e8ef260e253fca22ff1b5bb11b693c9f19f.jpg)

汇报（Reporting）

- 指定消息发往哪儿  
- 使用外部链接，可以利用指挥链，但不是必须的。

![](images/5a2a7d9091ae4ae4932f531320b6ae527fc08501aa79afa103669b528e1740ba.jpg)

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQQD.

9

![](images/22b7e1b1da03df623548e3449639038003ecf962ce07e9eb278d5ad8709909ef.jpg)

# UNCLASSIFIED

# 预定义的通信设备

![](images/b53db695873052034ba7084e22743f426f0e82a92a2d306af01461f174723ddf.jpg)

- COMM 代表一个完美的（有线）通信设备。  
- JTIDS TERMINAL 是一个内置的 Link-16 设备。  
- RADIO 是一个无线电设备，通信仅限于视距范围内。  
- SUBSURFACE 能够与水下平台通信（详见文档）。  
- TRANSCEIVER是双向通信设备。  
- RCVR仅接收信号。  
- XMTR仅发送信号。

# Predefined Comm Types

- WSFCOMMRCVR   
- WSFCOMM_XMTR   
- WSF COMM TRANSCEIVER   
- WSF_RADIO_RCVR   
- WSF_RADIO XMTR   
- WSF_RADIO_TRANSEIVER   
- WSE JTIDS TERMINAL   
- WSE SUBSURFACE RADIO RCVR   
- WSE SUBSURFACE RADIO XMTR   
- WSF_SUBSURFACE RADIO_TRANSEIVER   
- WSF_LASER_RCVR   
- WSF LASER XMTR   
- WSF_LASER_TRANSEIVER

- 通信设备属于平台的一个组件  
- 使用同一名称（network_name）的设备之间可以进行通信  
- 链接到平台上的其他部分，否则消息不会传送到任何地方。

![](images/dcdcc18c6a29e8c4c13d7c209bc639c738e61911088c40b872f13c396d637ad9.jpg)

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

11

![](images/ee0b42bd988d378e302fba6b294a04e2cc3b18f2911d0c4f197243d1dd68a745.jpg)

# UNCLASSIFIED

# 简单的指挥官-下属网络

![](images/1d00b8289d4ef767a7c1d6499e00b4c983e3d9af14927ce15f522279fa9c1b8c.jpg)

network_name [<network-name] | <local:master> | <local:slave>]

Define the subnetwork name (address) that this device belongs to. All devices that are defined to be on a given subnetwork can communicate with each other. To communicate across subnetworks, a default gateway with a router must be created. If no network_name is specified, then a subnetwork with the name 'default' is created.

The <local:master> and <local:slave> are special case network names used to create simple networks based on the explicit commander-subordinate relationships as defined by the commander keyword in platform definition. This, in effect, creates a network between a commander and its subordinates. Example:

不要在同台内部即使用默认网络也使用命名的网络，就是要么用默认的要么自己创

- 使用<local:master>和<local:slave>作为network_name会创建一个依附于已定义指挥链的网络。  
- 当通信设备在多个场景的文件中被引用时，这种方式非常强大。  
<local:master> = “我是此数据链上的指挥官。”  
<local:slave $> =$ “我是此数据链上的下属。”  
- 使用<local:master>和<local:slave>创建的网络最多支持255个通信设备。

![](images/bc598e2fcc258da65dc982a6a5b6c3b3cb9057e5531949899fd13a84c4f3fef5.jpg)

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

13

![](images/c842a4183f1b759e92da20f6f49eaea3aae9866172dc9f6c08e8fd66044532dc.jpg)

# UNCLASSIFIED

# 另一定义方法使用“Include”

![](images/0edbbbeb17d53cf40aa1892ceee5a203223475847df93d527a768c822d43105f.jpg)

- include包含的文件会将代码直接插到当前位置:

platform_type IADS_CMDR WSF_PLATFORM icon C4I

infrared signature VEHICLE_INFRARED_SIGNATURE optical_signature VEHICLE_OPTICAL_SIGNATURE radar_signature VEHICLE_RARAD_SIGNATURE

include comms/team_datalink.txt

processor data_mgr WSFTRACKPROCESSOR end Processor

comm cmdr_net TEAM_DATALINK network_name <local:slave> internal_link data_mgr internal_link task_mgr  
end_comm

comm sub_net TEAM_DATALINK network_name <local:master> internal_link data_mgr internal_link task_mgr   
end_comm

- 指挥链（Command Chains）

- 分级图  
- 可以用来寻址: 指挥端, 对端, 等等.

![](images/55d1a23cc50257ae5decee3adddc6df3383acb6d50f73c8e6185c342497d6e68.jpg)

- 通信设备（Comm Devices）

- 允许外部平台之间通信

![](images/6168f5662e90463f4e636de03413e44e424a36d201159d4675606dbbb0fc846d.jpg)

汇报（Reporting）

- 指定消息发往哪儿  
- 使用外部链接，可以利用指挥链，但不是必须的。

![](images/00f7a5e46a7343978056e2e873edba27d2596044b09f09386dfdf1587e4a9aff.jpg)

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

15

![](images/87ec4174109512c779f39a9ec81d7dc1675ba41dbf01b7cf3c19e9b1cb9979e2.jpg)

UNCLASSIFIED

汇报链：

external_link & report_to

![](images/28607bbc7093cc1c45524113982458beb58f01a3ed2f1450f56df3683e1f74c1.jpg)

- 通过通信（comm）将消息路由到指定的接收者。

```txt
processor data_mgr WSFTRACKPROCESSOR report_to commander via blue_comm end Processor 
```

![](images/696c8383bd83a9a6c3eccb2a2d29298285340b467cd6a4e882b552794cd71d48.jpg)

- 识别：

- 指挥链（如果未指定，将使用“默认”）  
- 接收者（指挥官、同级或下属）  
- 发送通信通道（期望接收通信通道名称与发送通信通道名称匹配）  
- 接收通信通道（可选）

```txt
processor data_mgr WSFTRACKPROCESSOR report_to command_chain STRIKERS commander via cmdr_net to sub_net report_to command_chain INTEL subordinates via sub_net to cmdr_net end Processor 
```

- 在脚本（Script）和轨迹（Track）处理器上是必需的，但在任务（Task）处理器上不是必需的。

- 不要求使用指挥链。

- 通过平台名称和通信名称进行显式关联。

```txt
processor data_mgr WSFTRACKPROCESSOR report_to platform 10_iads_cmdr comm blue_comm via blue_comm end Processor 
```

![](images/8f0d64aec00a637ae4ecf9c019d2d62c5a52f7d6cc0efb7764f7f122419593a5.jpg)

- 地址（更高级的通信用法）

```txt
report_to address 192.168.1.32/24 via blue_comm 
```

群组（培训中未涉及，请参阅文档）

```txt
group blue WsF_GROUP end_group 
```

```txt
comm blue_comm WSFCOMM_TRANSEIVER group_join blue end_comm 
```

```txt
report_to_group blue via blue_comm 
```

```txt
Agencies and their contractors, 9-Aug-19. Ferred to AFRL/RQDD. 
```

UNCLASSIFIED

17

![](images/f26aa77c68dd8b602a1d9745dd1f076b39be4123c87e635d35918b023dc9fc31.jpg)

# AFSIM通信：3个点

![](images/c4adba79a7a2d8893bc7a21221da30540624301b1b4cf4e154df235ab9620f03.jpg)

- 指挥链（Command Chains）

- 分级图  
- 可以用来寻址: 指挥端, 对端, 等等.

![](images/3921435536c070acb757cd7bd9bf83ae27cd1018b8ccd5b4118692b1b6babcb9.jpg)

- 通信设备（Comm Devices）

- 允许外部平台之间通信

![](images/a794c35a1c8e4f2482193c5c2dc639c70a74fecc3ac0f330f4f69c1efb7a96c5.jpg)

汇报（Reporting）

- 指定消息发往哪儿  
- 使用外部链接，可以利用指挥链，但不是必须的。

![](images/c06b410690367b99b22a683ec244540d117715ee7b13e97883ab8957d3a7ff18.jpg)

- small_blue_iads.txt 可以在模型库中找到  
·进行包含

floridistan.txt   
UNCLASSIFIED   
```txt
1 # New file created by AFSIM Wizard  
2 log_file output/jacksonabad.log  
3 include_ once setup.txt  
4 include_ once scenarios/blue_laydown.txt  
5 include_ once scenarios/red_laydown.txt  
6 include_ once scenarios/blue_sams.txt  
7 include_ once scenarios/small_red_iads.txt  
8 #include_ once scenarios/blue_sams.txt  
9 include_ once scenarios/small_red_iads.txt  
10 event_output file output/jacksonabad.evt end_event_output  
11 event_pipe file output/jacksonabad_%d.aer end_event_pipe  
12 end_time 1 hour  
13 end_time 1 hour  
14 final_run_number 5 
```

19

![](images/8e551668d850f86e2fa9feca1ade388cbf2d00bbd62c7685f3f2ae62a13ff050.jpg)

# Blue IADS流程图

![](images/7463e6b315d32540b47b8de434a30c75d4f62012a19cfd013ae7c0718f66b4e2.jpg)

![](images/7370f9b5265ccd9e3a65d9d897c684bc2376127cc330bc8b79ac704966196d97.jpg)  
DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

- 打开命令链浏览器（Command Chain browser）  
- 只需在 blue_chain 上点击并拖动平台即可。

![](images/b806c7d60e298fadb9dc678b82a0ae5a93feb8a84ac529b972cc8f28475fdb0b.jpg)

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

# UNCLASSIFIED

# 实践：Blue IADS命令链关系图

21

![](images/e6bd5e0d05ce41addb6ac5550f9e0575669d1d67997ee29a110ace3c036e32aa.jpg)

![](images/43df1b6c1e9be4ef9b8e10b6c29187c12620d6c162eb41db495f3556c7dff632.jpg)

![](images/67bdf10dc83c865a7ec25afeccc818943dfc792a277605f2bd748b7dda909985.jpg)

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

- 也可以使用此面板通过名称定义指挥链。

![](images/ef048703dcaac556ddb045aa8c473487aa88ae170f3980e2f9dcaea436a6a1aa.jpg)

![](images/d7aaa4fda0f4cbe2d0ca0a996533fb9d3bab3de4385b54d28771a01bd6a5f72c.jpg)

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

23

![](images/f0717094eb3fc2952def6551c345d98af3e9d2c9248b2386da621f8255314c4b.jpg)

# UNCLASSIFIED

# 练习：通信设备

# scenarios/small_blue_iads.txt

![](images/675ca538957e41a0975614a57f268145358c14ee5671be348dc33a40672f83c4.jpg)

- 对于每个通信（comm）：

- 给“commanders”添加通信设备  
- 名称叫做blue_comm

- 继承 TEAM_DATALINK   
- 添加网络名称 blue_net  
- 将内部链接添加到轨迹（track）和任务（task）处理器

10_iads_cmdr

100_radar_company

200_ew_radar

300 ew radar

3500_large_sam_battalion

3510_acq_radar

3520_largeSAM_TTR

3530_large_sam-Launcher

3540_large_sam launcher

3550_large_sam launcher

- 给“commanders”添加通信设备

![](images/fdeb715a25bcae528cf2ebda2a0ad0414500c10007016599d0b2f482f2956116.jpg)

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

25

![](images/3b126a6d72d540cd8152c76fea4323e86dd6c2b3148d4f762d3b40c6bb3e3b6f.jpg)

# UNCLASSIFIED

# 两个内部链路

# platforms/large_sam_battalion.txt

![](images/20b499c2f7cfbc96216c7a6649784a26fcb8421ff4895b498c44f495214c58f4.jpg)

- 通信设备有两个内部链路（internal links）

- 他们将消息发向哪里？  
- Track Processor (data_mgr)   
- Task Processor (task_mgr)   
- 为什么需要两个？  
- SAM系统是怎样工作的？

![](images/31621af89ce1366869fe729e34b87be7e33022dafc231b67bb98c1df1fc1c565.jpg)

![](images/f7b4dd69e95dcdddcf766c8068979060269ff2c6f1d70ef87e45c2774eedd7cd.jpg)

add comm blue_comm TEAM_DATALINK network_name blue_net internal_link data_mgr internal_link task_mgr   
end_comm

预警（EW）雷达：

- 对象类 EW_RADAR，派生自 BLUE_RADAR 对象类  
- EW_RADAR 对象具有一个名为 ew_radar 的 EW_RADAR 传感器

- 该传感器处于开启状态

链接到data_mgr

- WSFLINKEDPROCESSOR的datamgr会自动向指挥官报告   
- 所有传感器轨迹都会发送给指挥官

![](images/92e610e63244d8c1a2570a2ad2bfc093d72f20082bd64f7346aa9aced295feda.jpg)

DISTRIBUTION C

Distribution auth 540, large_sam_buncher

Government Agencies and their contractors, 9-Aug-19.

Other requests for this document shall be referred to AFRL/RQQD.

# UNCLASSIFIED

# EW雷达连队指挥官

# platforms/blue_radar_company.txt

27

![](images/bd3590307fd358717e55feb48ef536233bb205e431a9f0fbe60927d93864ba59.jpg)

![](images/03f579383ec97567b6bfeeaa6bee63bd5fc65de28ea1d7bfda2470463d7c6be6.jpg)

雷达指挥官：

- 对象类：

BLUE_RADAR_company

- WSFTRACKPROCESSOR的datamgr从通信设备接收轨迹数据

- WSFTRACK_PROCESSOR派生自WSFLINKEDPROCESSOR

```csv
5
6 platfom_type BLUE_RADARCOMPANY WSF_PLATFOM
7 icon TWIN_BOX
8
9 infrared signature VEHICLE_INFRARED_SIGNATURE
10 optical signature VEHICLE_OPTICAL_SIGNATURE
11 radar signature VEHICLE_RADAR_SIGNATURE
12
13 processor data_mgr WSF TrackPROCESSOR
14 purge_interval 60 sec
15 report_interval 20 sec
16 fused_reportreporting on
17 raw_reportreporting off
18 end Processor
19
20 processor task_mgr WSF_TASK_PROCESSOR
21 end Processor
22 end platform_type 
```

- data_mgr 处理器执行两项任务：

- 融合轨迹数据  
-自动向综合防空系统（IADS）指挥官报告轨迹10.26.13

![](images/38b84c2d774c6de07b71599c2f2916d012d50770fe0552660faf550bb5fc9ea8.jpg)

add comm blue_comm TEAM_DATALINK network_name blue_net internal_link data_mgr internal_link task_mgr end_comm

DISTRIBUTION C. Distribution authorized to U.S. 1050 large, un launched. Agencies and their contractors, 9-Aug-19.

Other requests for this document shall be referred to AFRL/RQQD.

综合防空系统（IADS）指挥官：

- 对象类：IADS_CMDR  
- IADS_CMDR_DATA_MGR 的 data_mgr 从通信设备接收轨迹数据

- WSFTRACK_PROCESSOR

- 处理器 taskmgr 根据主轨迹列表（Master Track List）中的轨迹，将目标分配给下属单位

![](images/b1fbb9790e1f1133aea3a3a2737b1ecdc9ae89b5417ab9ace62db439ea9a1de4.jpg)

![](images/d44d751c51f8b7c8183f5d6fe45241df59f365d3591a3f3d34fb01faf8bc9901.jpg)

UNCLASSIFIED大型地对空(SAM)导弹营platforms/large_sam_battalion.txt

29

![](images/c75836ed112e9a5964d5fdb57be475b3735186ccc1754d22c7a6a86f76b570fd.jpg)

大型地对空导弹营：：

- 对象类：LARGE_SAM_BATTALION  
- 标准数据管理器（data_mgr）从通信设备接收目标轨迹信息

- 来自指挥官和下属  
- 在60秒后清除目标轨迹信息

- WSFTRACKPROCESSOR

LARGE_SAM_BATTALION_TASK_MGR任务管理器(taskMgr)负责开启传感器并下达导弹发射命令

BLUE_SAM_BATTERY_TASK_MGR

- 替换父处理器类中的两个脚本

![](images/fe343a252dbc07205ddc695e6149186d7fdf631d19625586391ba595984a99aa.jpg)

地对空导弹捕获雷达：

- 对象类：ACQ_RADAR（捕获雷达）

- BLUE_RADAR是父类   
通信模块（comm）、数据管理器（data_mgr）和任务管理器（task_mgr）在父类中定义  
数据管理器（data_mgr）向指挥官汇报

- 传感器在 ACQ_RADAR 类中定义  
与数据管理器（data_mgr）相连接  
- 这种设置允许我们做什么？  
可以定义多个平台，这些平台将以相同的方式运行，只是使用不同的传感器

![](images/dbf985bdeafa78d5e123c6ceba6c369e9833eeda49b22a6524652485df0add82.jpg)

![](images/f4c8a1a37b8398202a51fbfdf5f28fe19b8990f57f97834345eb1a506ac59299.jpg)

ABITION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQQD.

# UNCLASSIFIED 地对空导弹目标跟踪雷达 platforms/large_sam_ttr.txt

31

![](images/bfe4d35c026db2d822c9aff792cd5a904b7df3b672d2b4cebb5cc2709792de69.jpg)

目标跟踪雷达（TTR）：

对象类：LARGESAM_TTR（大型地对空导弹目标跟踪雷达）  
- 在此定义了TTR传感器
  - TTR_RADAR对象类  
- 标准数据管理器（data_mgr）从TTR传感器接收目标轨迹信息

通过通信设备（comm）将目标轨迹信息发送给指挥官

![](images/da5d215c28d1491f6a6a3f7848d00509b9f1565e050e1d74b17f4e0b58f19179.jpg)

![](images/92b8e24a8242376896e0518b7ae3facd7e03ab0a04a3b5285dbc39e83a527109.jpg)

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

大型地对空导弹发射器：

对象类：LARGESAMLAUNCHER（大型地对空导弹发射器）  
在此实例化了武器SAM（地对空导弹）

LARGE_SAM对象类

- 武器发射由地对空导弹营（SAM Battalion）中的任务管理器（task manager）执行

- 标准的数据管理器（data_mgr）和任务管理器（task_mgr）  
没有实际发射武器的逻辑！  
- 武器是如何发射的？

![](images/6094822c3ec1f790b3a6ef867fdbf136ae0b14dd1bc55ea8f671c8e15d171f21.jpg)

![](images/87c88be2906845e9cb5546a4d80ac326b0694d3b1cbcf30a5c9f07c8ab4110ec.jpg)

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

# UNCLASSIFIED

# WsfTaskManager

33

![](images/46778ce7ac2dc4c4d73b9a96377f82099a3909c0c630c4eab6703bfa2241ffff.jpg)

![](images/62962d5080b81990c8af8237b58830981fd30c6cc37d035780404974398d4e30.jpg)

Overview

WeTaskManager is a processor that provides functions to manage tasks. Tasks represent a request to a resource (i.e., a processor, sensor or weapon) to perform some 'work.' The resource may exist on the initiating platform or on another platform (resources will be discussed more in the section Resource Types). There are several categories of functions involved in managing tasks:

- Assignment functions - issued by the assigning task manager to start or update a task
- Control functions - issued by the assigning task manager to cancel a task   
- Status reporting functions - issued by the assigned resource indicating it has completed the assignment.   
- Query functions - issued by either the assigning task manager, or by the assignee (if the assigned resource was a processor.)

The functions to perform the above depend on the type of resource involved and are summarized in the following table. Note that some resources have multiple functions that can be used.

<table><tr><td></td><td>Processor</td><td>Sensor</td><td>Weapon</td><td>Jammer</td></tr><tr><td>Assignment</td><td>AssignTaskDelayTask</td><td>StartTracking</td><td>FireFireAt</td><td>StartJamming</td></tr><tr><td>Control(by assignee)</td><td>CancelTask</td><td>StopTrackingCancelTask</td><td>AbortFiringAtCancelTask</td><td>StopJammingCancelTask</td></tr><tr><td>Status(by assignee)</td><td>TaskComplete</td><td>N/A</td><td>N/A</td><td>N/A</td></tr><tr><td>Query(by assignee)</td><td>TasksAssignedTasksAssignedToTasksAssignedForTimeSinceAssignedTimeSinceLastAssignedAssignedTaskListAssigneesForTaskAssigneeForTask</td><td>Same as Processor Methods</td><td>WeaponsActiveForRoundsFiredAtWeaponsFiredAtWeaponsFiredForSalvosFiredAtTimeSinceWeaponLastFiredForTimeSinceWeaponLastTerminatedForAnd Processor Methods</td><td>Same as Processor Methods</td></tr><tr><td>Query(by assignee)</td><td>TasksReceivedTasksReceivedForTimeSinceLastReceivedReceivedTaskList</td><td>N/A</td><td>N/A</td><td>N/A</td></tr></table>

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

70 # select a weapon and launch it   
71 # the selected weapon must be available, have sufficient rounds and not busy   
72 script bool LaunchWeapon()   
73 WsftWeapon weapon;   
74 WsftPlatform platform;   
75 foreach (WsftPlatform sub in PLATFORM.Subordinates())   
76 { weapon $=$ sub.Weapon(WEAPON_NAME); if (weapon.IsTurnedOn()) && (weapon.QuantityRemaining $\mathbf{\rho}^{*}) =$ SALVO_SIZE && (TasksAssignedTo(sub，""，weapon.Name $)\left\langle  <   1\right\rangle$ ）   
81 } bool canInterceptNow $=$ InInterceptEnvelopeOf(ENVELOPE); if (canInterceptNow) { platform $=$ sub; break; }   
88 }   
90 bool launched; else;   
91 if ((weapon.IS)) && (platform != NULL)   
92 }   
93 Iunched $=$ Fire(TRACK,mShootTaskStr,weapon.Name(),SALVO_SIZE,platform); if (launched) { writeln_d("*** T="，TIME NOW，""，platform.Name(),"" TRACK.TargetName(),"R="，platform.SlantRangeTo(TRACK), " FIIRE!!!");   
96 }   
100 }   
101 return lauuched;   
102 end script   
103

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

35

![](images/9f9ac0626ddb61fed0aeeb5b7b7c8509068317c5691006f1d9792e41d61f8257.jpg)

# UNCLASSIFIED

# 怎么发生的？

![](images/8d32b4ff66ceda5a2a00a49fd0e29f15f75b2b8bed35b9e6450710319891f273.jpg)

- Fire 方法会创建一个任务分配

- 该任务分配会被发送到发射器  
- 任务分配中包含目标轨迹信息

- 发射器接收到任务分配后会尝试执行任务

- 发射器上的任务处理器会指示武器发射  
- 当武器发射后，任务即完成

- 任务完成后，任务处理器会发送一条 WsfTaskComplete 消息  
·注意：任务处理器没有脚本！  
- 任务完成消息会自动发送

# A Primer on Task Processors

# Task Processor

A Task Processor (WSF_TASKPROCESSOR) is an AFNES processor that provides the ability to examine data (tracks) in the track manager and act upon them. The actions include

- Assignment of tasks to subordinates   
- Activation or deactivation of sensors or jammers   
Firing of weapons   
- Maneuvering the platform

Every platform that can assign tasks or receive task assignments MUST have an instance of a WSF_TASKPROCESSOR. The task processor uses the concept of a 'finite state machine' to control the actions to be performed.

The task processor "listens" to the track manager to determine when a new track appears. The track may be from

A track produced by a local sensor.   
A track received from an off-board source   
- A track embedded within a task assignment   
A prebriefed track

When a new track appears, an evaluation event will be scheduled for the "start" state (i.e., the first "state" in the processor). Subsequent evaluation events will be scheduled as dictated by the state machine. Evaluation events for a given track will cease when BOTH of the following are true:

No tasks have been received for the track.   
- No tasks have been originated for the track.

Each track executes in its own state machine.

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

# UNCLASSIFIED实践: external_link scenarios/small_blue_iads.txt

37

![](images/3fc161a49193131ebc4f4ee2a2d6061c6b0522ecfa903096a9e154c6334073e7.jpg)

- 在轨迹处理器上添加 report_to

![](images/fde868acd6f4185515fe925bc70faa3617fb34138b28b863f520c8d25bb6ee7a.jpg)

edit编辑轨迹处理器

- 使用命令链(command_chain) blue_chain  
- 报告给 commander   
- via 通过合适的通信设施

- 将电子战（EW）报告的所有目标轨迹转发给10_iads_cmdr

```txt
55   
56 platfom 100_radar_company BLUE_Radar_company   
57 side blue   
58 position 30:30n 81:48w   
59 altitude 0.00 ft agl   
60 command_chain blue_chain 10_iads_cmdr   
61 add comm blue_comm TEAM_DATALINK   
63 network_name blue_net   
64 internal_link data_mgr   
65 internal_link task_mgr   
66 end_comm   
67   
68 edit processor data_mgr   
69 report_to command_chain blue_chain commander via blue_comm   
70 endprocessor   
71 endPLATFORM 
```

RUN !!!

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

# UNCLASSIFIED

# 小型蓝色综合防空系统（IADS）部署

39

![](images/c072c219752d30f2b2692639353656884ea385fd262c8684b402e164255c2069.jpg)

![](images/d01c831ca965d8ff17824a123e1625a319eeab79f448f1ef359fb366a2ea6cb6.jpg)

- 您可能需要将新平台移动到坦克周围

![](images/99d72501b6efbf15d6a8de5351053b6b75deca88aa4d3a5c029102c8688a467a.jpg)

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

![](images/44ac9599fc65c9c7983223ff96d768e55dc5d4c3fbf0455fbecf0162e71f9348.jpg)

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

UNCLASSIFIED

# 学习目标

41

![](images/d8a078152be9e29425857c9e8e6a0039be55a3642391da948ff2d28dc56ac9b6.jpg)

![](images/c4bed5b01ba79dc4c771397f369f2241499fe62e4b2a4d9fd6d1c70f644479ef.jpg)

- 包含以下内容：

- 定义指挥链  
定义通信和链路

![](images/cd3b6a85d9346d008d21dc1cbbd7e9385348a341da03a09f12b1b0f6613d6d06.jpg)

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

![](images/d4c0ce7e43317cef6e10153563c82dc8a7b9ff7e3852382d37a1b51369443a1e.jpg)

43

![](images/f31405f7608fc4d7627d2317f621b3ecc54aa3a580f6333f196d19ac5c8b6dec.jpg)

UNCLASSIFIED

# 最终笔记：AFSIM Comms

![](images/de3319d4f5586d40073cd23512f8e120d26db866305370e15118d27093f6c95d.jpg)

<table><tr><td>Command Chain</td><td>Named network</td><td>DEFAULT network</td></tr><tr><td rowspan="2">command_chain iads_chain cmdr commander cmdr
1 2 3
5 4
Links: none</td><td>network_name my_network</td><td>network_name &lt;local:master&gt; 
network_name &lt;local:slave&gt;</td></tr><tr><td>Links: network_name</td><td>Links: none w/o commander</td></tr><tr><td>Hierarchy: command_chain or commander</td><td>Hierarchy: none</td><td>Hierarchy: none</td></tr><tr><td>Routing: none w/o links</td><td>Routing: none w/o hierarchy</td><td>Routing: none w/o links &amp; hierarchy</td></tr></table>

# Named chain + Named network

network_name my_network command_chain iads_chain cmdr

![](images/42208639c231c16911f4204bc1411574527e03a366f0a6145c2e84a9084076ff.jpg)

Links: network_name

Hierarchy: command_chain

Routing: external_link

# DEFAULT chain + DEFAULT network

network_name<local:master> network_name<local:slave>

![](images/858aa6b5e610b42188692a7ec730707f0632d15c94496351c8b7f5c19d366b8a.jpg)

Links: <local:...> + commander

Hierarchy: commander

Routing: external_link and/or <local:....>

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19.

Other requests for this document shall be referred to AFRL/RQQD.

# 6.1.7. 推演工具 Warlock 特性 7_Warlock_Features

# 6.1.7.1. Warlock 概览 13-Warlock_Overview

本节不涉及想定，只有PPT资料，下面为afsim2.9_src\training\user\7_Warlock_Features\slides\13-Warlock_Overview.pptx的翻译。

![](images/cc6b1ef28bb75960aa6596b54a3dc02f683eedf49de41d102ac41141ef278b2f.jpg)

UNCLASSIFIED

![](images/1b5335f4f6f8f8aba66d790326b4a59fbb96d10b2ccc272df35c1967ce29547d.jpg)

![](images/bd42110b646a9dee09269edbb48ea538f0e02dc0692b6ea77b78ba35b8730fb1.jpg)

# AFSIM用户培训

# 13-Warlock概览

本文档由杨石兴翻译，该资料做为《AFSIM2.9参考手册》的一部分。没有《AFSIM2.9参考手册》的加杨石兴微信领取：13324598743

Integrity $\star$ Service $\star$ Excellence

AFRL/RQQD美国空军研究实验室

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

- 包含以下内容:

- Warlock是什么  
- Warlock与Mission的对比  
- Warlock的基本特性

![](images/0cbb4afa4ad2826e57fa1e20f8c6b681ae1d0265a3e4614629fc4162f11a0836.jpg)

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

2

![](images/b6fdd304fcb800b8e969efa7ac2ed3e288cab71cbe1d156683058e6a3530b694.jpg)

UNCLASSIFIED

# Warlock是什么？

![](images/949e778df48b118e2a6d2b90f9dfd0f1d22187bc716f26feafe2014ea30f4365.jpg)

- 一个与AFSIM集成为单一可执行文件的Operator-in-the-Loop(OITL)工具  
提供数据可视化功能，以深入了解AFSIM的决策过程和执行情况。  
- 具备控制AFSIM实体的能力，可用于战争推演和分析。

![](images/da8073fa6b140edfce85e407ded110ada33489f995fee541ae805b921d25174a.jpg)

![](images/dbbf16e82e6dd626166b21ce8133af4962309401b4d336a7298528a5127b154c.jpg)

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

支持多种模拟和分析领域：

交战  
任务  
作战

- 支持白方/红方/蓝方的单元分析。  
提供受限和非受限的视图/控制功能。  
- 分布式操作：  
允许多个视图/阵营同时运行并进行交互。

![](images/92ed5543019a085c45403132dc3dca4e87a5cb3978bf5e2924b85a730c9b8522.jpg)

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

UNCLASSIFIED

![](images/5ff3ef4a7c1f4647676f40edf57da2a5c51045873237c8c4df59bb3c16e32e96.jpg)

# Warlock 和 Mission

4

![](images/4a6d1b032ac0de99a348746711552eddff2844e1674022a415579ffab7d8eb64.jpg)

![](images/4ea79d88d147710c92e599d83fab3ac0434afe248d734c1715110444f226e724.jpg)

![](images/01ef810c57c382222294d77c43b18dabee185034d77cbf5d7a5a3db161b9f6c5.jpg)

用户交互&数据展示

![](images/58c37dbeb3fe21efa22e2586907a019b2ba52b24dd0b5968825462374eada45a.jpg)

Warlock

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

<table><tr><td>Warlock</td><td>Mission</td></tr><tr><td>只能实时推演或多倍速实时推演
·不支持蒙特卡洛模式</td><td>以构建方式运行
·支持蒙特卡洛模式</td></tr><tr><td>可以作为独立应用程序运行，也可以通过 Wizard或命令行执行。</td><td>可以通过 Wizard 或命令行执行。</td></tr><tr><td>支持加载 Warlock 插件以及 AFSIM/Mission 插件。</td><td>仅支持加载 AFSIM/Mission 插件。</td></tr></table>

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

UNCLASSIFIED

# 如何打开Warlock

6

![](images/d2e43577e83214863bd042d76eabf299a8529c1bef5ccd151b950ccfa7d8a5ad.jpg)

# 从Wizard

通过工具栏的这个地方选择

![](images/96d729ce37b3e762f59d19189550486528cdd718882113ddf8c94eca395cd73d.jpg)

选择Warlock

![](images/8c5c162e8920d75c974f94fde1760da9dffe1eec0f764c62878937cd571f230f.jpg)

点击play

![](images/2c75446f7d3298f84e1fe68d0144dc000b190d736914ed54940a13a691e6f6b0.jpg)

# 从AFSIM的bin目录

![](images/f617795bf74e7b0bb6b4ece5e2eca868c39f64d5b8e9c20013e046e66d08682f.jpg)

![](images/6d1c2f0fda099abb1dc664fc8e85f21e644f0fb8345806b195fae74f8fbefb79.jpg)

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

# 从Startup Dialog

浏览选择一个想定文件或选择最近打开的

![](images/1e452483816800db367971671fff0f0ef25a27e3c581870731476a107d7c4a17.jpg)

# 从Warlock的菜单

打开File菜单

选择“Load Scenario”浏览一个想定

![](images/4d23711feeffab0f7b1b73a6e89951f5d65dfc0897d45a51cb3be4a74ed55ae6.jpg)

选择“RecentScenarios”选择最近打开的想定

![](images/77a0af323f69f5c2b784d22d4997ef0a51d3574bb41c86a35fc9639dd59aee98.jpg)

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

# UNCLASSIFIED

# 从命令行打开Warlock

8

![](images/8a95fb755eb76e61cd0b096046ba35b12bf48748bc3c0b0cc2d35f8f5feff4e6.jpg)

- 与 Mission 一样，您可以通过命令提示符桌面应用程序在 Warlock 中打开一个场景。

- 需要包含warlock.exe的地址、场景输入文件以及要打开的配置文件的地址。

- 您可以在命令行中添加一个或多个命令行选项：

<table><tr><td colspan="2">Command Line Options</td></tr><tr><td>-?,-h,-help</td><td>Display command line options and quit</td></tr><tr><td>-cf&lt;filename&gt;</td><td>Use the specified configuration file, modifications will be saved to specified file</td></tr><tr><td>-icf&lt;filename&gt;</td><td>Imports the specified configuration file, modifications will be not be saved to specified file</td></tr><tr><td>--console</td><td>Enables the console window</td></tr><tr><td>-lock_side</td><td>Prevent the user from being able to change the visible sides or teams</td></tr><tr><td>-lock_fileload</td><td>Prevent the user from using file browsing or file loading capabilities</td></tr><tr><td>-ups</td><td>Uses the previous scenario, if no scenario was specified</td></tr></table>

举例：

![](images/dc8194879fd0274e5ca55e48508f021d9b36706b2229c18c70e6b70d76437ac8.jpg)

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

- 方式1: 正常点“X”关闭窗口

- 彻底关闭Warlock

- 方式2: 点击该图标结束推演

- 结束当前推演

- Startup dialog会弹出

- 方式3：点击所示图标重启推演  
- 方式4: 重新加载想定

- 重新读取输入文件

![](images/381a11aa209e15bf44b1967c708e399bc35278eb460c52400fe179204451c87c.jpg)

![](images/2dbdb7b73b537399352a2bb5debd365dee6ec7ea019b49efba23c671e0c7bf1e.jpg)

![](images/a0b03f1c84c6f25fa07e9eef0adc49639a8909566dea262ccdcb68231f29adc8.jpg)

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19.

Other requests for this document shall be referred to AFRL/RQQD.

# UNCLASSIFIED

![](images/a078a6f4a2d8e6c4d859ef744998f8ea6b5e6d2d63c220070132f9b7e4ae66ee.jpg)

# 基本布局

10

![](images/4727a7722318a49020c2efe2db0f41772b47d0bb6719414ac6239029329054a3.jpg)

![](images/e004c102d6e00f98dec131cde1599564dc252271ff935b481318f0d85afa5b05.jpg)

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19.

Other requests for this document shall be referred to AFRL/RQQD.