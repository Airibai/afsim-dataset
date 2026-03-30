例如：

```matlab
Object obj = 'my string';  
string str = (string)obj;  
int i = 99;  
double d = (double)i;  
WsfMessage msg = GetControlMessage();  
((WsfControlMessage)msg).SetResource('my_resource'); 
```

# <statement> 语句

语句定义为以下之一：

# <variable-declaration> 变量声明

每个变量必须在使用前声明。变量可以简单地声明，也可以声明并赋值。变量声明如下：

```latex
[ \text{[storage_type]} ] <type> <identifier> ';'  
[ \text{[storage_type]} ] <type> <identifier> = <expression> ';' 
```

前者的示例：

```c
int i;  
static j;  
WsfSensor thisSensor; 
```

后者的示例：

```txt
int i = 0;  
global double x = 10.0 * i;  
string s = 'Hello, world';  
WsfSensor thisSensor = PLATFORM.Sensor('this_sensor'); 
```

# <variable-assignment> 变量赋值

简单值、复杂表达式和脚本/函数返回值可以使用赋值运算符赋值给变量。

```txt
<variable> = <expression>; 
```

例如：

```matlab
int x;  
x = 10; 
```

# <if-else> 条件语句

if-else 语句允许用户根据一个或多个计算为布尔值的表达式选择要执行的语句。第一个解析为 true 的条件执行其<block>中包含的语句。

```typescript
if '(' <expression>'') <block> { else if '(' <expression>'') <block> } [else <block>] 
```

例如：

string name $=$ 'platform-1';   
if (name $\equiv$ 'platform-2')   
{ print('Found platform-2');   
}   
else if (name $\equiv$ 'platform-1') { print('Found platform-1');   
}   
else { print('Couldn\'t find platform 1 or 2');   
}

# <while-loop> 循环语句

while 语句允许用户基于计算为布尔值的表达式进行迭代。迭代继续，直到表达式解析为 false。

```txt
while '('<expression>'')<block> 
```

例如：

int $\mathrm{i} = 0$ while $(\mathrm{i} <   10)$ { print('is'，i); $\mathrm{i} = \mathrm{i} + 1;$

# <do-while-loop> do-while 循环

do-while 语句允许用户基于计算为布尔值的表达式进行迭代。迭代继续，直到表达式解析为 false。do-while 和 while 循环之间的区别在于条件在 do-while 循环的底部检查，这保证至少进行一次迭代。

```txt
do <block> while '('<expression>'') 
```

例如：

```txt
int i = -1;  
do  
{  
    i = i + 1;  
    print('i is', i);  
}  
while (i < 10) 
```

# <for-loop> for 循环

for语句允许用户基于计算为布尔值的表达式进行迭代。迭代继续，直到表达式解析为

false。此外，它提供了声明循环计数器和增量操作的空间。

```javascript
for '(' [variable-declaration>] ';' [expression-list] ';' [expression-list] ')' <block>例如： 
```

```lisp
for (int i = 0; i < 10; i = i + 1)  
{  
    print('i is', i);  
} 
```

# <foreach-loop> foreach 循环

foreach循环允许用户迭代容器中的元素，同时提供对键和值的访问。

```txt
foreach '(' [variable-declaration>':] <variable-declaration> in <expression>'') <block>例如： 
```

```txt
Map<string, double> myMap = Map<string, double>();  
myMap['a'] = 1.1;  
myMap['b'] = 2.2;  
// 如果声明了两个循环变量（用冒号分隔），第一个必须是键，第二个必须是数据。  
foreach (string aKey : double aData in myMap)  
{  
    print('key, data', aKey, ', ', aData);  
}  
// 如果声明了一个循环变量，它必须是数据。  
foreach (double aData in myMap)  
{  
    Print('data', aData);  
}
```

# <break> 跳出循环

break语句允许用户跳出当前块。

```gemfile
break ';'
```

例如：

```txt
while(true) { if(true) { break; }   
} 
```

# <continue> 继续循环

continue语句允许用户忽略循环中的其余语句并跳到循环的顶部。

```txt
continue ';'
```

例如：

```lisp
for (int i = 0; i < 10; i = i + 1)  
{ if (i == 5) { continue; } } 
```

# <return> 返回值

return 语句允许用户从脚本/函数调用中返回一个值。

```txt
return <expression>' 
```

例如：

```txt
double Multiply(double aA, double aB)  
{  
    return aA * aB;  
} 
```

# <block> 代码块

代码块是：

□ 零个或多个语句被 script 和 end_script 包围  
▫ 零个或多个语句被花括号包围

前者的示例：

```matlab
script void my_script()
int i = 1;
print('i = ', i);
end.Script 
```

后者的示例：

if(true) { int $\mathrm{i} = 1$ . print('i $= ^{\prime}$ ,i); }

# <function-declaration> 函数声明

函数可以在脚本中使用以下语法声明。函数只能在脚本中声明。如果需要一个对所有脚本都可用的函数，将其定义为脚本。

```html
<type> <identifier> '(' [<variable-declaration-list>] ')' <block> 
```

例如：

```txt
double Magnitude(double aDx, double aDy)  
{  
return MATH.Sqrt(aDx*aDx + aDy*aDy);  
} 
```

注意：MATH是一个系统变量，所有脚本都可以使用它，提供对各种基于数学的实用程

序的访问。

# 1.2.14. 六自由度模型理论 P6DOF Theory

# 介绍

本文档旨在解释 P6DOF Mover 的物理原理（参见 WSF_P6DOF_MOVER 输入类型和WsfP6DOF_Mover 脚本类）。定义了运动学和动力学方程，并在适用的情况下，将本文档中的数学符号与现有的 P6DOF 命令进行比较。

WSF_P6DOF_MOVER 提供了一个基于物理的 6 自由度（6DOF）运动器，支持广泛的飞机和武器建模。6 个自由度包括平移位置（?）以及姿态 $( \Psi , \Theta , \Phi )$ ）。车辆的姿态由基于动量的计算确定，提供了真实的车辆指向以及正确的迎角（α）和侧滑角（β）建模。旋转运动学受空气动力和推进力及力矩以及旋转惯性的影响。尽管 P6DOF 运动器包括完整的 6DOF建模，但它们利用了一些角度/姿态简化来减少所需数据并简化控制——因此称为“伪”6DOF。在特别情况下，它们仅使用惯性张量的对角线来减少惯性交叉耦合 $( I _ { x x } , I _ { y y } , I _ { z z }$ ）。然而，P6DOF 运动器支持完整的 6 个自由度，并包括详细的稳定性导数累积方法来进行空气动力学建模，如本文档所述。这允许基于马赫数的详细空气动力学建模，以提供对跨音速、超音速和高超音速状态的准确建模。

P6DOF 运动器包括涡轮喷气发动机、涡轮风扇发动机、冲压/超燃冲压发动机、液体推进剂火箭和固体推进剂火箭的特定类型建模，提供了广泛的推进类型。这意味着每个发动机模型都包括对推力性能影响最大的参数，如马赫数和高度。

符号定义  

<table><tr><td>符号</td><td>定义</td><td>P6DOF 命令</td><td>P6DOF 脚本方法</td></tr><tr><td>α</td><td>迎角</td><td>-</td><td>GetAlpha</td></tr><tr><td>β</td><td>侧滑角</td><td>-</td><td>GetBeta</td></tr><tr><td>M</td><td>马赫数</td><td>-</td><td>GetMach</td></tr><tr><td>ψ</td><td>偏航角</td><td>-</td><td>GetHeading</td></tr><tr><td>θ</td><td>俯仰角</td><td>-</td><td>GetPitch</td></tr><tr><td>φ</td><td>滚转角</td><td>-</td><td>GetRoll</td></tr><tr><td>r</td><td>机体偏航速率</td><td>-</td><td>GetYawRate</td></tr><tr><td>q</td><td>机体俯仰速率</td><td>-</td><td>GetPitchRate</td></tr><tr><td>p</td><td>机体滚转速率</td><td>-</td><td>GetRollRate</td></tr><tr><td>c</td><td>翼弦</td><td>wing_chord_ft</td><td>-</td></tr><tr><td>s</td><td>翼展</td><td>wing spans_ft</td><td>-</td></tr><tr><td>t</td><td>时间</td><td>-</td><td>-</td></tr><tr><td>x̅</td><td>惯性位置</td><td>-</td><td>-</td></tr><tr><td>v̅</td><td>惯性速度</td><td>-</td><td>-</td></tr><tr><td>a</td><td>惯性加速度</td><td>-</td><td>-</td></tr><tr><td>ω</td><td>旋转速度</td><td>-</td><td>-</td></tr><tr><td>a̅</td><td>旋转加速度</td><td>-</td><td>-</td></tr><tr><td>v̅</td><td>惯性坐标系中的速度单位向量</td><td>-</td><td>-</td></tr><tr><td>R</td><td>将惯性框架中的向量转换为机体框架的方向余弦矩阵</td><td>-</td><td>-</td></tr><tr><td>m</td><td>质量</td><td>mass</td><td>GetEmptyWeight</td></tr><tr><td>I</td><td>惯性矩阵</td><td>moment_of_inertia_ixx, moment_of_inertia_iyy, moment_of_inertia_izz</td><td>-</td></tr><tr><td>FT,i</td><td>惯性框架中的总力</td><td>-</td><td>-</td></tr><tr><td>MT</td><td>总力矩</td><td>-</td><td>-</td></tr><tr><td>FT,b</td><td>机体框架中的总力</td><td>-</td><td>-</td></tr><tr><td>Fa</td><td>机体框架中的空气动力</td><td>-</td><td>-</td></tr><tr><td>Fg</td><td>机体框架中的重力</td><td>-</td><td>-</td></tr><tr><td>Fp</td><td>机体框架中的推进力</td><td>-</td><td>-</td></tr><tr><td>Fl</td><td>机体框架中的起落架力</td><td>-</td><td>-</td></tr><tr><td>Ma</td><td>空气动力产生的力矩</td><td>-</td><td>-</td></tr><tr><td>rcm/a</td><td>相对于空气动力学参考点的质心</td><td>center_of_mass_x1, center_of_mass_y1, center_of_mass_z1</td><td>GetCgX, GetCgY, GetCgZ</td></tr><tr><td>gi</td><td>惯性框架中的重力向量</td><td>-</td><td>-</td></tr><tr><td>q</td><td>动压</td><td>-</td><td>-</td></tr><tr><td>Ar</td><td>参考面积</td><td>reference_area</td><td>-</td></tr><tr><td>Y</td><td>面积乘数</td><td>-</td><td>-</td></tr><tr><td>CL</td><td>升力系数</td><td>cl_alpha_beta_mach_table</td><td>-</td></tr><tr><td>CLq</td><td>由于俯仰速率引起的升力系数贡献, dCL/dq</td><td>clq_alpha_mach_table</td><td>-</td></tr><tr><td>CLà</td><td>由于迎角变化率引起的升力系数贡献, dCL/dα</td><td>cl_alpha_mach_table</td><td>-</td></tr><tr><td>Cd</td><td>阻力系数</td><td>cd_alpha_beta_mach_table</td><td>-</td></tr><tr><td>Cy</td><td>侧向力系数</td><td>cy_alpha_beta_mach_table</td><td>-</td></tr><tr><td>CYr</td><td>由于偏航速率引起的侧向力系数贡献, dCy/dr</td><td>cyr_beta_mach_table</td><td>-</td></tr><tr><td>CYβ</td><td>由于侧滑变化率引起的侧向力系数贡献, dCy/dβ</td><td>cy_betadot_beta_mach_table</td><td>-</td></tr><tr><td>Cn</td><td>偏航力矩系数</td><td>cn_alpha_beta_mach_table</td><td>-</td></tr><tr><td>Cnr</td><td>由于偏航速率引起的偏航力矩系数贡献, dCn/dr</td><td>cnr_mach_table</td><td>-</td></tr><tr><td>Cnp</td><td>由于滚转速率引起的偏航力矩系数贡献, dCn/dp</td><td>cnp_mach_table</td><td>-</td></tr><tr><td>Cnβ</td><td>由于侧滑变化率引起的偏航</td><td>cn_betadot_mach_table</td><td>-</td></tr><tr><td></td><td>力矩系数贡献, \(\frac{dC_n}{d\beta}\)</td><td></td><td></td></tr><tr><td>\(C_m\)</td><td>俯仰力矩系数</td><td>cm_alpha_beta_mach_table</td><td>-</td></tr><tr><td>\(C_{mq}\)</td><td>由于俯仰速率引起的俯仰力矩系数贡献,\(\frac{dC_m}{dq}\)</td><td>cmq_mach_table</td><td>-</td></tr><tr><td>\(C_{mp}\)</td><td>由于滚转速率引起的俯仰力矩系数贡献,\(\frac{dC_m}{dp}\)</td><td>cmp_mach_table</td><td>-</td></tr><tr><td>\(C_{mA}\)</td><td>由于迎角变化率引起的俯仰力矩系数贡献,\(\frac{dC_m}{da}\)</td><td>cm_alphadot_mach_table</td><td>-</td></tr><tr><td>\(C_l\)</td><td>滚转力矩系数</td><td>cl_alpha_beta_mach_table</td><td>-</td></tr><tr><td>\(C_{lp}\)</td><td>由于滚转速率引起的滚转力矩系数贡献,\(\frac{dC_l}{dp}\)</td><td>clp_mach_table</td><td>-</td></tr><tr><td>\(C_{lr}\)</td><td>由于偏航速率引起的滚转力矩系数贡献,\(\frac{dC_l}{dr}\)</td><td>clr_mach_table</td><td>-</td></tr><tr><td>\(C_{lq}\)</td><td>由于俯仰速率引起的滚转力矩系数贡献,\(\frac{dC_l}{dq}\)</td><td>clq_mach_table</td><td>-</td></tr><tr><td>\(C_{l\dot{a}}\)</td><td>由于迎角变化率引起的滚转力矩系数贡献,\(\frac{dC_l}{da}\)</td><td>cl_alphadot_mach_table</td><td>-</td></tr><tr><td>\(C_{l\dot{\beta}}\)</td><td>由于侧滑变化率引起的滚转力矩系数贡献,\(\frac{dC_l}{d\dot{\beta}}\)</td><td>cl_betadot_mach_table</td><td>-</td></tr><tr><td>\(\hat{l}\)</td><td>机体坐标中的升力单位向量</td><td>-</td><td>-</td></tr><tr><td>\(\widehat{d}\)</td><td>机体坐标中的阻力单位向量</td><td>-</td><td>-</td></tr><tr><td>\(\hat{s}\)</td><td>机体坐标中的侧向力单位向量</td><td>-</td><td>-</td></tr><tr><td>\(T\)</td><td>发动机推力,取决于发动机类型</td><td>-</td><td>-</td></tr><tr><td>\(\hat{t}\)</td><td>机体框架中的推力单位向量</td><td>-</td><td>-</td></tr></table>

# 运动方程

惯性加速度通过将总惯性力除以总质量来获得。类似地，旋转加速度通过将总力矩除以总转动惯量来获得。这些加速度，如公式(1)所示，是通过两个时间步之间的平均力和力矩

计算的，如公式(2)所示。

公式(1)

$$
\overrightarrow {a} = \frac {\overrightarrow {\vec {F}} _ {T , i}}{m}
$$

$$
\vec {\alpha} = \mathrm {I} ^ {- 1} \overline {{\vec {M}}} _ {T}
$$

公式(2)

$$
\overline {{\vec {F}}} _ {T, i} = \frac {1}{2} [ \overrightarrow {F} _ {T, i} ] _ {t} + \frac {1}{2} [ \overrightarrow {F} _ {T, i} ] _ {t + \Delta t}
$$

需要注意的是，P6DOF 的简化之一是公式(1)中的转动惯量是一个对角矩阵，如公式(3)所示。

公式(3)

$$
I = \left[ \begin{array}{c c c} I _ {x x} & 0 & 0 \\ 0 & I _ {y y} & 0 \\ 0 & 0 & I _ {z z} \end{array} \right]
$$

首先力 $[ \vec { F } _ { T , i } ] _ { t }$ 和力矩 $[ \overrightarrow { M } _ { T } ] _ { t }$ ，在当前时间步计算，用于计算线性和角加速度。接着，使用公式(4)将状态向前推进。然后在新状态下计算力和力矩，生成 $[ \overrightarrow { F } _ { T , i } ] _ { t + \varDelta t }$ 和 $[ \overrightarrow { M } _ { T } ] _ { t + \varDelta t }$ 。使用公式(2)计算平均力和平均力矩，然后用这些值在公式(1)中计算线性和角加速度。最后，状态通过公式(4)更新。

公式(4)

$$
\overrightarrow {x} _ {t + \Delta t} = \overrightarrow {x} _ {t} + \overrightarrow {v} _ {t} \Delta t + \frac {1}{2} \overrightarrow {a} _ {t} \Delta t ^ {2}
$$

$$
\vec {v} _ {t + \Delta t} = \vec {v} _ {t} + \vec {\alpha} _ {t} \Delta t
$$

$$
\overrightarrow {Q} _ {t + \Delta t} = \overrightarrow {Q} _ {t} + \overrightarrow {Q} _ {t} \Delta t
$$

$$
\vec {\omega} _ {t + \Delta t} = \vec {\omega} _ {t} + \vec {\alpha} _ {t} \Delta t
$$

机体角速率?   、四元数 $\overrightarrow { Q }$ 和速率四元数 $\overrightarrow { { \dot { Q } } }$ 定义如下公式(5)。

公式(5)

$$
\overrightarrow {\omega} = \left[ \begin{array}{c c c} r & q & p \end{array} \right] ^ {T}
$$

$$
\overrightarrow {Q} = \left[ \begin{array}{l} c o s \frac {\psi}{2} c o s \frac {\theta}{2} c o s \frac {\phi}{2} + s i n \frac {\psi}{2} s i n \frac {\theta}{2} s i n \frac {\phi}{2} \\ c o s \frac {\psi}{2} c o s \frac {\theta}{2} s i n \frac {\phi}{2} - s i n \frac {\psi}{2} s i n \frac {\theta}{2} c o s \frac {\phi}{2} \\ c o s \frac {\psi}{2} s i n \frac {\theta}{2} c o s \frac {\phi}{2} + s i n \frac {\psi}{2} c o s \frac {\theta}{2} c o s \frac {\phi}{2} \\ s i n \frac {\psi}{2} c o s \frac {\theta}{2} c o s \frac {\phi}{2} - c o s \frac {\psi}{2} s i n \frac {\theta}{2} s i n \frac {\phi}{2} \end{array} \right]
$$

$$
\vec {Q} _ {t} = \frac {1}{2} \left[ \begin{array}{c c c c} 0 & - r & - q & - p \\ r & 0 & p & - q \\ q & - p & 0 & r \\ p & q & - r & 0 \end{array} \right] \vec {Q} _ {t}
$$

如果四元数Q  定义为[a b c d]T，那么相应的方向余弦矩阵计算如下公式(6)。

公式(6)

$$
R = \left[ \begin{array}{c c c} a ^ {2} + b ^ {2} - c ^ {2} - d ^ {2} & 2 (b c + a d) & 2 (b d - a c) \\ 2 (b c - a d) & a ^ {2} - b ^ {2} + c ^ {2} - d ^ {2} & 2 (c d + a b) \\ 2 (b d + a c) & 2 (c d - a b) & a ^ {2} - b ^ {2} - c ^ {2} + d ^ {2} \end{array} \right]
$$

# 力和力矩

力是在机体坐标系中计算的，然后转换到惯性坐标系中以用于公式(1)。这种转换通过公式(7)实现。

公式(7)

$$
\overrightarrow {F} _ {T, i} = R ^ {- 1} \overrightarrow {F} _ {T, b}
$$

其中，R 定义为 3-2-1 旋转矩阵（偏航-俯仰-滚转），如公式(8)所示。

公式(8)

$$
R = \left[ \begin{array}{c c c} {c o s (\theta) c o s (\psi)} & {c o s (\theta) s i n (\psi)} & {- s i n (\theta)} \\ {s i n (\phi) s i n (\theta) c o s (\psi) - c o s (\phi) s i n (\psi)} & {s i n (\phi) s i n (\theta) s i n (\psi) + c o s (\phi) c o s (\psi)} & {s i n (\phi) c o s (\theta)} \\ {c o s (\phi) s i n (\theta) c o s (\psi) + s i n (\phi) s i n (\psi)} & {c o s (\phi) s i n (\theta) s i n (\psi) - s i n (\phi) c o s (\psi)} & {c o s (\phi) c o s (\theta)} \end{array} \right]
$$

总机体力 $\vec { F } _ { T , b }$ 由公式(7)计算，是机体坐标系中空气动力、重力和推进力的总和。如果适用，还包括起落架的力。

公式(7)

$$
\overrightarrow {F} _ {T, b} = \overrightarrow {F} _ {a} + \overrightarrow {F} _ {g} + \overrightarrow {F} _ {p} + \overrightarrow {F} _ {l}
$$

总力矩由公式(9)给出。

公式(9)

$$
\overrightarrow {M} _ {T} = \overrightarrow {M} _ {a} + \overrightarrow {r} _ {c m / a} \times (\overrightarrow {F} _ {a} + \overrightarrow {F} _ {p} + \overrightarrow {F} _ {l})
$$

机体坐标系中的重力由公式(10)计算。

公式(10)

$$
\overrightarrow {F} _ {g} = m R \overrightarrow {g} _ {i}
$$

机体坐标系中的推进力由公式(11)给出。

公式(11)

$$
\overrightarrow {F} _ {p} = T \hat {t} _ {b}
$$

空气动力产生的力和力矩分别由公式(12)和(13)给出。

公式(12)

$$
\begin{array}{l} \overrightarrow {F} _ {a} = \tilde {q} A _ {r} \gamma [ (C _ {L} (\alpha , \beta , M) + k _ {L q} C _ {L q} (\alpha , M) + k _ {L \dot {\alpha}} C _ {L \dot {\alpha}} (\alpha , M)) \hat {l} + (C _ {Y} (\alpha , \beta , M) + k _ {Y r} C _ {Y r} (\beta , M)) \hat {m} ] \\ + k _ {Y \widehat {\beta}} C _ {Y \widehat {\beta}} (\beta , M)) \widehat {s} + C _ {d} (\alpha , \beta , M) \widehat {d} ] \\ \end{array}
$$

公式(13)

$$
\begin{array}{l} \vec {F} _ {a} = \tilde {q} A _ {r} [ (C _ {l} (\alpha , \beta , M) + k _ {l p} C _ {l p} (M) + k _ {l r} C _ {l r} (M) + k _ {l q} C _ {l q} (M) + k _ {l \dot {a}} C _ {l \dot {a}} (M) + k _ {l \dot {\beta}} C _ {l \dot {\beta}} (M)) \hat {i} \\ + (C _ {m} (\alpha , \beta , M) + k _ {m q} C _ {m q} (M) + k _ {m p} C _ {m p} (M) + k _ {m \dot {\alpha}} C _ {m \dot {\alpha}} (M)) \hat {j} + (C _ {n} (\alpha , \beta , M) + k _ {n \dot {\alpha}} C _ {n \dot {\alpha}} (M) + k _ {n \dot {\beta}} C _ {n \dot {\beta}} (M)) \hat {k} \\ + k _ {n r} C _ {n r} (M) + k _ {n p} C _ {n p} (M) + k _ {n \beta} C _ {m \beta} (M)) \hat {k} ] \\ \end{array}
$$

在公式(13)中，向量 $\hat { i } , \hat { j } , \hat { k }$ 是机体坐标系中的标准正交基单位向量。

在公式(12)中，向量   , 分别是机体坐标系中的升力、阻力和侧向力单位向量，计算方法如公式(14)。

公式(14)

$$
\hat {l} = \hat {j} \times R \hat {v}
$$

$$
\widehat {d} = - R \hat {v}
$$

$$
\hat {s} = \hat {l} \times \hat {d}
$$

# 简化频率

在 公 式 (12) 和 (13) 中 ， 简 化 频 率 $k _ { \{ x \} }$ 的 计 算 方 法 如 公 式 (15) 所 示 。 如 果use_reduced_frequency 被设置为 false，那么将使用相应的角速度代替无量纲的简化频率，并应根据情况相应调整稳定性导数表。

公式(15)

$$
k _ {L q} = \frac {\overline {{c}} q}{2 \| \overrightarrow {v} \|}
$$

$$
k _ {L \dot {a}} = \frac {\overline {{c}} \dot {a}}{2 \| \overrightarrow {v} \|}
$$

$$
k _ {Y r} = \frac {\overline {{s}} r}{2 \| \overrightarrow {v} \|}
$$

$$
k _ {Y \dot {\beta}} = \frac {\overline {{s}} \dot {\beta}}{2 \| \overrightarrow {v} \|}
$$

$$
k _ {l p} = \frac {\overline {{s}} p}{2 | | \overrightarrow {v} | |}
$$

$$
k _ {l r} = \frac {\overline {{s}} r}{2 \| \overrightarrow {v} \|}
$$

$$
k _ {l q} = \frac {\overline {{s}} q}{2 \| \overrightarrow {v} \|}
$$

$$
k _ {m q} = \frac {\overline {{c}} q}{2 \| \overrightarrow {v} \|}
$$

$$
k _ {m p} = \frac {\overline {{c}} p}{2 \| \overrightarrow {v} \|}
$$

$$
k _ {m \dot {a}} = \frac {\overline {{c}} \dot {a}}{2 \| \overrightarrow {v} \|}
$$

$$
k _ {n r} = \frac {\overline {{c}} r}{2 | | \overrightarrow {v} | |}
$$

$$
k _ {n p} = \frac {\overline {{c}} p}{2 \| \overrightarrow {v} \|}
$$

$$
k _ {n \dot {\beta}} = \frac {\overline {{c}} \dot {\beta}}{2 \| \overrightarrow {v} \|}
$$

和 分别指机翼的弦长和翼展。弦长是指机翼前缘到后缘的距离，而翼展是指从一个翼尖到另一个翼尖的距离。平均弦长（StandardMean Chord,SMC）是用于计算俯仰力矩的一个特征值，通常定义为机翼面积除以翼展。

参考：

Jenkins, J. “Dynamic Stability Derivatives”, Air Force Research Laboratory - Aerodynamic Technology Branch Aerospace Vehicles Division, June 2015. AFRL-RQ-WP-TR-2015-0141.

# 1.2.15. 新六自由度模型理论 SixDOF Theory

介绍

刚 体 六 自 由 度 （ 6DOF ） 模 型 （ WSF_RIGID_BODY_SIX_DOF_MOVER,WsfRigidBodySixDOF_Mover）的理论与其前身 P6DOF 相同，可以通过 P6DOF 理论文章进行研究。当 WSF_P6DOF_MOVER 被移除时，该文档将被合并到当前文档中。

WSF_POINT_MASS_SIX_DOF_MOVER 旨 在 弥 合 诸 如 WSF_GUIDED_MOVER 和WSF_AIR_MOVER 等 三 自 由 度 （ 3DOF ） 模 型 与 诸 如 WSF_P6DOF_MOVER 和WSF_RIGID_BODY_SIX_DOF_MOVER 等完整六自由度（6DOF）模型之间的差距。

在三自由度模型中，需要假设其方向的某些元素，而完整的六自由度模型将根据角动量守恒（ $\boldsymbol { \Sigma } \boldsymbol { M } = I \boldsymbol { \dot { \omega } }$ ）传播方向。这种方法在运动学上是正确的，但对数据的要求可能不切实际。具体来说，净力矩需要准确及时地了解机体周围的力分布，而惯性矩张量需要了解机体内的质量分布。

PointMass 六自由度运动模型使用基于效果的系统来估计 ，尽可能由可以直接测量或假设的旋转数据组成。与类似模型一样，PM6DOF 模型的空气动力系数应表示在给定空速和迎角下的配平（零净力矩）状态。旋转速率要么由主动飞行员（无论是否有人在环中）指令，要么生成以模拟空气动力稳定性或不稳定性的效果。

推力大小的计算与刚体模型使用的相同，但运动学模型的性质要求推力矢量化也必须基于效果。此外，目前不考虑 PointMass 车辆的推力反转。

这种六自由度模型广泛应用于航空航天、机器人、3D 建模等领域，能够精确描述物体在三维空间中的运动，包括前后、上下、左右的平移以及绕三个轴的旋转。

<table><tr><td>符号</td><td>定义</td><td>SixDOF命令</td><td>SixDOF脚本方法</td></tr><tr><td>α</td><td>攻角(angle of attack)</td><td></td><td>GetAlpha</td></tr><tr><td>β</td><td>侧滑角( angle of side slip)</td><td></td><td>GetBeta</td></tr><tr><td>αT</td><td>总攻角(total angle of attack)</td><td></td><td>GetAlpha</td></tr><tr><td>M</td><td>马赫数(Mach number)</td><td></td><td>GetMach</td></tr><tr><td>t</td><td>时间(time)</td><td></td><td></td></tr><tr><td>p</td><td>机体滚转速率(body roll rate)</td><td></td><td>GetRollRate</td></tr><tr><td>q</td><td>机体俯仰速率(body pitch rate)</td><td></td><td>GetPitchRate</td></tr><tr><td>r</td><td>机体偏航速率(body yaw rate)</td><td></td><td>GetYawRate</td></tr><tr><td>p</td><td>机体滚转加速度(body roll acceleration)</td><td></td><td></td></tr><tr><td>q</td><td>机体俯仰加速度(body pitch acceleration)</td><td></td><td></td></tr><tr><td>r</td><td>机体偏航加速度(body yaw acceleration)</td><td></td><td></td></tr><tr><td>ω</td><td>旋转速度向量(rotational velocity vector)</td><td></td><td></td></tr><tr><td>ω</td><td>旋转加速度向量(rotational acceleration vector)</td><td></td><td></td></tr><tr><td>ωmax</td><td>控制的总角加速度限制(total limit of angular acceleration from controls)</td><td></td><td></td></tr><tr><td>ωmax,aero</td><td>空气动力控制的角加速度限制(limit of angular acceleration from aerodynamic controls)</td><td></td><td></td></tr><tr><td>ωmax,aero0</td><td>在标准海平面条件下干重下的ωmax,aero值</td><td></td><td></td></tr><tr><td>ωmax,prop</td><td>推进控制的角加速度限制(limit of angular acceleration from propulsive controls)</td><td></td><td></td></tr><tr><td>ωmax,prop0</td><td>在干重下的ωmax,prop值</td><td></td><td></td></tr><tr><td>ωn</td><td>稳定空气动力响应的自然频率(natural frequency of the stabilizing aerodynamic response)</td><td></td><td></td></tr><tr><td>ωn0</td><td>在标准海平面条件下干重下的ωn值</td><td></td><td></td></tr><tr><td>m</td><td>当前质量(current mass)</td><td></td><td>GetCurrentWeight</td></tr><tr><td>m0</td><td>空重(empty mass)</td><td>mass</td><td>GetEmptyWeight</td></tr><tr><td>I</td><td>惯性矩阵(moment of inertia matrix)</td><td>moment_of_inertia_ixx, moment_of_inertia_iyy,</td><td></td></tr><tr><td></td><td></td><td>moment_of_inertia_izz</td><td></td></tr><tr><td>M_T</td><td>总力矩 (total moment)</td><td></td><td></td></tr><tr><td>T</td><td>发动机推力 (engine thrust), 依赖于发动机类型</td><td></td><td></td></tr><tr><td>rho</td><td>当前高度下的大气密度 (density of the atmosphere at the vehicle's current altitude)</td><td></td><td></td></tr><tr><td>rho0</td><td>椭球面上的标准大气密度 (standard density of the atmosphere at the ellipsoid surface)</td><td></td><td></td></tr></table>

# 运动方程

与刚体模型一样，线性运动是加速度的二阶积分，根据动量守恒计算（公式(1)）。方向同样是角加速度的二阶积分，但与刚体模型不同，PointMass 运动模型中没有真正考虑角动量——角加速度?   仅由控制能力和（去）稳定化效果构建。

P6DOF 理论文档详细讨论了如何积分这些微分方程（参见运动方程），这里不再重复。

# 控制力和旋转

在 PM6DOF 中，力的求和方式与 RB6DOF 相同，但角加速度的构建方式抽象化了对车辆实际力矩的考虑。

对于非制导弹药（如炸弹、火箭、诱饵），不需要提供控制响应数据，但对于需要制导或驾驶的车辆则是必需的。基线角加速度限制在用户定义的表中提供，基于马赫数，然后根据空气密度和攻角效应进行修正。角加速度表应根据车辆或车辆类别的参考数据提供，但也可以通过运动学估计。

例如，考虑一个合理的战斗机描述，其在马赫 0.8 时能够在一秒内从水平飞行加速到滚转速率 180 度/秒。在这种情况下，峰值加速度应至少在马赫 0.8 时指定为 180 度/秒²——可能更高，以考虑高度和任何稳定化效果（参见下文的稳定旋转效果）。

注意：这种变化与马赫数的关系因车辆类型而异，但合理的初步策略是将加速度限制按马赫数的平方进行缩放，记住空气动力矩随速度的平方缩放。在跨音速和超音速范围内，压力中心的变化或控制器降低控制权的情况可以通过在这些马赫数下从初始估计中减少最大加速度来近似。

公式(1)

$$
\vec {\dot {\omega}} _ {m a x, a e r o} = \left(\frac {\rho}{\rho 0}\right) \left(\frac {m _ {0}}{m}\right) \vec {\dot {\omega}} _ {m a x, a e r o _ {0}} c o s \alpha T
$$

这些修正考虑了在更高高度和更大侧滑角下控制效率的降低，以及随着质量增加或减少而发生的惯性变化。

一个单独的第二项被添加以考虑在给定推力下推力矢量化的效果。

公式(2)

$$
\overrightarrow {\dot {\omega}} _ {m a x, p r o p} = \left(\frac {m 0}{m}\right) \left(\frac {\Delta \overrightarrow {\dot {\omega}} _ {p r o p}}{\Delta T}\right) T
$$

推力本身被建模为高度的函数，因此不考虑额外的高度效应。为了考虑随着燃料消耗而增加的敏捷性，引入了质量因子。

公式(3)

$$
\overrightarrow {\dot {\omega}} _ {m a x} = \overrightarrow {\dot {\omega}} _ {m a x, a e r o} + \overrightarrow {\dot {\omega}} _ {m a x, p r o p}
$$

PM6DOF 上的操纵杆和方向舵飞行控制直接映射到旋转速率命令。这个映射是用户在脚本中定义的 1D 表，允许线性或非线性映射。旋转速率命令通过线性斜坡实现，其斜率受角加速度限制。

公式(4)

$$
\vec {\omega} _ {d e s i r e d} = \frac {\vec {\omega} _ {c m d} - \vec {\omega}}{\Delta t}
$$

# 稳定旋转效果

稳定化效果的影响在非制导弹药上最为明显。默认情况下，PM6DOF 车辆在没有飞行员操作的情况下没有改变其旋转速率的倾向。这包括指向风向，或称为“风标效应”。

可以通过添加表格来引入这种效果，这些表格指定了作为马赫数函数的基线稳定频率。这些频率指定了非控制车辆返回平衡时的临界阻尼系统响应。目前，平衡状态为俯仰轴的 0度攻角，偏航轴的 0 度侧滑角，以及滚转轴的 0 度/秒滚转速率。未来版本可能会引入设置，以允许修改平衡状态，例如飞机的非零攻角或弹药的指定旋转速率。

与控制加速度数据一样，输入参数会根据载荷和操作空气密度的变化进行调整。

公式(5)

$$
\omega_ {n} = \frac {m _ {0}}{m} \frac {\rho}{\rho_ {0}} \omega_ {n 0}
$$

响应频率然后被转换为俯仰和偏航轴的旋转加速度：

公式(6)

$$
\dot {q} = (0 - \alpha) \omega_ {n _ {p i t c h}} ^ {2} - 2 \omega_ {p i t c h} \dot {\alpha}
$$

$$
\dot {r} = (0 - \beta) \omega_ {n _ {y a w}} ^ {2} - 2 \omega_ {n _ {y a w}} \dot {\beta}
$$

对于滚转轴，我们影响的是旋转速率而不是旋转，因此采用一阶滞后系统：

公式(7)

$$
f = \frac {\omega_ {r o l l} \Delta t}{1 + \omega_ {n _ {r o l l}} \Delta t}
$$

$$
p t + \Delta t = (1 + f) p t
$$

$$
\dot {p} = \frac {p t + \Delta t - p t}{\Delta t}
$$

为了避免超调和数值不稳定，这些加速度基于运动学外推进行限制：

公式(8)

$$
\dot {p} _ {m a x} = \left| \frac {- p}{\Delta t} \right|
$$

$$
\dot {q} _ {m a x} = \left| \frac {2}{\varDelta t ^ {2}} (- \alpha - \dot {a} \varDelta t) \right|
$$

$$
\dot {r} _ {m a x} = \left| \frac {2}{\varDelta t ^ {2}} (- \beta - \dot {\beta} \varDelta t) \right|
$$

PM6DOF 的最终旋转加速度是控制加速度和稳定加速度的总和。

# 1.3. 开发 Development

# 1.3.1. 构建指南 Build Instructions

# 概述

本文档描述了如何构建 AFSIM（高级仿真、集成和建模框架）的基础应用程序，目录结构的可能安排，以及如何在构建中包含扩展和插件。它适用于需要编译 AFSIM 的软件开发人员和终端用户。

# 先决条件

支持以下操作系统和编译器：

# 操作系统和编译器

操作系统：Windows 10

□ 编译器：Microsoft Visual Studio 2015, 2017, 或 2019  
架构：64 位

操作系统：Linux

□ 编译器：GCC 4.8.5   
▫ 架构：64 位

注意：支持的配置意味着 AFSIM 已在这些配置上进行了测试。虽然 AFSIM 可以在许多配置中成功编译和运行，但只有列出的配置经过开发团队的全面测试。

# 其他工具

<table><tr><td>工具</td><td>版本</td><td>用途</td><td>备注</td></tr><tr><td>CMake</td><td>3.7或更高</td><td>生成构建系统</td><td>Visual Studio 2019 需要 CMake 3.14 或更高版本</td></tr><tr><td>Python</td><td>3.x.x</td><td>运行自动化测试和构建Sphinx文档</td><td></td></tr><tr><td>Sphinx</td><td>2.1.x或更高</td><td>构建Sphinx文档</td><td>Windows 需要MikTex, Linux需要额外的latex和图像包</td></tr><tr><td>myst-parser</td><td>0.14.x或更高</td><td>Sphinx 文档 的Markdown支持</td><td></td></tr><tr><td>MikTex</td><td>2.9或更高</td><td>构建Sphinx文档</td><td>仅限 Windows</td></tr><tr><td>Perl</td><td>5.16.3</td><td>构建Sphinx文档(LaTex/PDF)</td><td></td></tr><tr><td>Doxygen</td><td>1.8.5或更高</td><td>构建 Doxygen 文档</td><td>需要安装 Graphviz</td></tr><tr><td>Graphviz</td><td>2.38或更高</td><td>构建 Doxygen 文档</td><td>需要安装 Doxygen</td></tr><tr><td>Gtest</td><td>1.10.0</td><td>运行单元测试</td><td></td></tr><tr><td>GFortran</td><td>Windows: 8.1.0, Linux: 4.8.5</td><td>构建机密发布</td><td></td></tr><tr><td>MESA 图形库</td><td>最新版本</td><td>构建图形应用程序</td><td>Debian: libglu1-mesa-dev 和 libgl1-mesa-dev, RHEL: mesa-libGLU-devel 和 mesa-libGL-devel</td></tr><tr><td>Linux JPEG 库</td><td>最新版本</td><td>构建图形应用程序</td><td>Debian: libjpeg62 和 libjpeg62-dev</td></tr></table>

提示：验证用户和系统环境变量是否正确，包括 PATH 设置，以避免工具执行问题。

# 获取软件

AFSIM源代码和应用程序文件可以通过以下方法获取：

从官方发行版安装 AFSIM源代码和应用程序文件。  
从官方 AFSIM存储库下载 AFSIM源文件。  
从官方 AFSIM存储库克隆 AFSIM源代码。

注意：从发行文件获得的 AFSIM 软件将包括已编译的 AFSIM 应用程序可执行文件，如Mission、Warlock 等。克隆的存储库需要后续构建以生成目标 AFSIM 应用程序。

# 从发行版安装 AFSIM 和 AFSIM 源代码

AFSIM发布软件可以通过 Confluence 上的 AFSIM门户获取，导航到所需的版本并下载发布包（zip, msi, tar.gz, deb, rpm）。

提示：当提取发行包时，会在指定的提取路径中创建一个文件夹（例如 afsim-x.y.z-win64）。在执行构建之前，可以将此文件夹重命名为用户特定的约定并移动到所需位置。

以下是从发行文件安装 AFSIM时的目录结构示例：

path/to/afsim/distribution   
```txt
|__bin
|__demoos
|__documentation
|__resources
|__swdev
|__src
|____.
|____.
|____CMakeLists.txt
|____.
|____.
|____tools
|____training 
```

注意：从发行文件安装时，swdev 目录包含 AFSIM 源代码。bin 目录包含 AFSIM 应用程序可执行文件和库。

# 从远程存储库下载 AFSIM 源代码

AFSIM源代码可以从 Bitbucket 上的 afsim存储库下载。通过选择省略号图标，然后从下拉菜单中选择下载选项，如下图所示：

![](images/a027fde5db1b8977b180b75e04187b6a3009160ea09086a36a810250ee9f6bce.jpg)

下载完成后，可以通过右键单击.zip 文件并选择根目录作为目标，将其解压到根目录中。解压后的目录结构示例如下：

path/to/afsim

```txt
|__.gitlab  
|__ cmake  
|__ core  
|__ doc  
|__ mission  
|_.  
|_.  
CMakeLists.txt  
LICENSE.md  
README.md  
. 
```

注意：Linux 和 Windows 的目录结构相同。

# 从远程存储库克隆 AFSIM 源代码

可以在 Windows 和 Linux 中使用“git clone”命令克隆 AFSIM 远程存储库，传递远程存储库的 URL，并可选地指定本地存储库的名称。

AFSIM 项目的克隆地址可以在 Bitbucket 上的 afsim 存储库中找到，通过从 ACTIONS 菜单中选择 Clone 并复制弹出窗口中的高亮文本，如下图所示：

![](images/58fcdeed4f5409e6cb040c6e16dbf88eff36eaab735dc3f7ab07f7a783e2b115.jpg)

以下是一个 git clone 命令示例（Windows），将创建 afsim 子目录，并在其中克隆 afsim远程存储库：

```txt
git clone https://bitbucket.di2e.net/scm/afsim/afsim.git afsim 
```

克隆后的目录结构示例如下：

```batch
path/to/afsim |_.gitlab |_ cmake |_ core |_ doc |_ mission |. CMakeLists.txt LICENSE.md README.md 
```

提示：其他 AFSIM 存储库，如 demos、tools 和 training，可以以类似方式从 Bitbucket克隆。这些存储库可以在这里找到：AFSIM项目。

# 构建环境

目录结构

为了保持干净的源代码树，建议使用源代码外构建。源代码外构建通过在源目录之外提供一个单独的、专用的 BUILD 目录来实现。这使用户能够删除构建树而不删除源文件，将CMake生成的构建工件保持在源目录之外，并保护源文件不受版本控制工具的影响。

在此示例中，BUILD 目录已在 path/to/afsim下的源目录之外创建：

从 AFSIM发行文件的目录结构

```txt
path/to/afsim  
\|\_bin  
\|\_demo  
\|\_documentation  
\|\_resources  
\|\_swdev  
\|\_**BUILD**  
\|\_src  
\|.  
\|.  
\MakeLists.txt  
\|.  
\|.  
\|\_tools  
\|\_training 
```

从 AFSIM下载或克隆的目录结构

```txt
path/to/afsim  
\|\_.gitlab  
\|\_**BUILD**  
\|\_ cmake  
\|\_ core  
\|\_ doc  
\|\_ mission  
\|\_ mystic  
\|\_ sensor_plot  
\|\_ tools  
\|\_ warlock 
```

```batch
\I CMakeLists.txt CMakeSettings.json LICENSE.md README.md 
```

顶级源目录包含主要的 CMakeLists.txt 文件。core 目录包含仿真框架（WSF）及其扩展的源代码。应用程序目录（如 mission、mystic、warlock、wizard 等）包含托管应用程序的源代码和测试代码。

注意：从发行文件安装 AFSIM时，swdev目录包含源代码文件系统。bin 目录包含 AFSIM应用程序可执行文件和库。demos 文件夹包含所有 AFSIM 应用程序的演示和场景。demos下的 regression_tests 子目录包含指定回归测试文件的<application-name>_list.txt 文件。

```txt
demos   
|acoustic   
1.   
1.   
regressionTests mission_list.txt sensor_plot_list.txt .   
1.   
routefinderdemoos satellite_demos 
```

注意：回归测试套件不随 AFSIM发布一起分发，仅在克隆或下载 demos 存储库时可用。单元测试源文件（ $\mathsf { C } { + + }$ ）位于具有单元测试套件的模块或库下的 test子目录中。

```txt
.   
.   
|core   
doc   
mission   
tools   
geodata test   
.   
.   
|util   
test 
```

```txt
1 .   
1_wizard   
1_wsfPlugins   
. 
```

包含第三方库和资源

可以通过导航到 Confluence 上的开发者资源表来下载 3rd_party 和 vtk_resources 工件。可以通过在 AFSIM 根目录（或其他目录）中提取文件并在 CMake 构建选项中设置SWDEV_THIRD_PARTY_PACKAGE_SOURCES 和 VTK_RESOURCES_SOURCEDIR 为文件下载目录来将第三方库和资源包含在 AFSIM构建中。有关更多信息，请参见配置第三方库和资源。

包含扩展和插件

可以通过将扩展（也称为可选项目）和插件放置在 AFSIM 根目录（或其他目录）中，并在 CMake 构建选项中设置 WSF_ADD_EXTENSION_PATH 来将其包含在 AFSIM 构建中。将WSF_PLUGIN_BUILD CMake 选项设置为 TRUE 可以在构建可执行文件中启用插件。有关更多信息，请参见 CMake选项。

扩展有一个目录，收集组成扩展的所有文件和目录。该主目录必须包含一个 wsf_module文件，CMake将使用该文件将扩展包含在 AFSIM 构建中。wsf_module 文件名没有扩展名，文件本身没有内容。此文件与插件一起存在，作为 CMake的指示，表明该目录包含一个扩展。

它还包括 test_<application-name>目录，其中包含将与应用程序的自动测试一起运行的test_*.txt 文件。有关更多信息，请参见运行系统测试。

# 生成构建系统

CMake用于生成 AFSIM 的构建系统，并提供命令行和 GUI 界面来生成构建系统。有关CMake的更多文档可以在 CMake官方网站 找到。

CMake 命令行

可以使用以下 CMake 命令格式之一来指定源和构建树并生成构建系统：

使用当前工作目录作为构建树

```txt
cmake [<options>] <path-to-source> 
```

使用当前工作目录作为构建树，并将<path-to-source>作为包含顶级 AFSIM CMakeLists.txt文件的源树。指定的路径可以是绝对路径或相对于当前工作目录的相对路径。示例如下：

AFSIM 发行文件

```txt
path/to/afsim> cd BUILD  
path/to/afsim/swdev/BUILD> cmake ../src 
```

AFSIM 下载或克隆

```txt
path/to/afsim> cd BUILD  
path/to/afsim/BUILD> cmake ... 
```

使用现有构建路径

```txt
cmake [<options>] <path-to-existing-build> 
```

使用<path-to-existing-build>作为构建树，并从其 CMakeCache.txt 文件中加载源树路径（该文件必须由之前的 CMake运行生成）。示例如下：

AFSIM 发行文件

```txt
path/to/afsim/swdev> cd BUILD path/to/afsim/swdev/BUILD> cmake . 
```

AFSIM 下载或克隆

```txt
path/to/afsim> cd BUILD path/to/afsim/BUILD> cmake . 
```

指定源和构建路径

```html
cmake [<options>] -S <path-to-source> -B <path-to-build> 
```

使 用 <path-to-source> 作 为 源 树 和 <path-to-build> 作 为 构 建 树 ， 包 含 顶 级 AFSIMCMakeLists.txt 文件。构建树将自动创建（如果尚不存在）。示例如下：

AFSIM 发行文件

```batch
path/to/afsim/swdev> cmake -S ./src -B ./BUILD 
```

AFSIM 下载或克隆

```batch
path/to/afsim> cmake -S . -B ./BUILD 
```

注意：请参阅 CMake选项以获取常用选项列表。

# CMake GUI

启动 cmake-gui 应用程序（或在 Linux 上使用 cmake3-gui，它支持与 cmake 相同的命令行接口）以指定源和构建目录的路径。如果没有给出参数，可以使用以下步骤指定这些路径：在“Where is the source code:”字段中，输入包含顶级 AFSIM CMakeLists.txt 文件的源树路径，例如<path/to/afsim>/swdev/src。在支持的窗口系统中，您还可以将 CMakeLists.txt 文件拖放到 CMake GUI 中。

在 “Where to build the binaries:” 字 段 中 ， 输 入 构 建 目 录 的 路 径 ， 例 如<path/to/afsim>/swdev/BUILD。如果该目录尚不存在，系统会提示您创建。在支持的窗口系统中，您还可以将先前生成的 CMakeCache.txt 文件从现有构建中拖放到 CMakeGUI 中。

根据需要更改配置选项，然后选择 Configure 按钮。

注意：如果这是一个新构建（即没有 CMake缓存），您需要为项目指定生成器（例如VisualStudio），以及生成器的可选平台（例如 x64）。

配置步骤完成后，选择 Generate 按钮以生成构建系统。

如果使用 IDE 生成器（如 Visual Studio），可以选择“Open Project”按钮打开项目文件。

# CMake 选项

选项可以在 CMake GUI 中设置或通过命令行参数传递，使用-D<var>[:<type>]=<value>格式。以下变量是修改配置时最常用的：

BUILD_WITH_<module>: 启用或禁用每个可选模块（库扩展或应用程序）。  
BUILD_MYSTIC_PLUGIN_<PluginName>: 启用或禁用每个 Mystic 插件。  
BUILD_WARLOCK_PLUGIN_<PluginName>: 启用或禁用每个 Warlock 插件。   
BUILD_WIZARD_PLUGIN_<PluginName>: 启用或禁用每个 Wizard 插件。  
BUILD_WKF_PLUGIN_<PluginName>: 启用或禁用每个 WKF 插件，该插件由多个 GUI 应用 程序加载。   
CMAKE_BUILD_TYPE: 指定单配置生成器（如 Makefile Generators 和 Ninja）的构建类型，与多配置生成器（如 Microsoft Visual Studio）相对。可能的值包括 Debug 和 Release（默认）。  
CMAKE_INSTALL_PREFIX: 指定调用 make install 或构建 INSTALL 目标时的安装目录。默认是${CMAKE_BINARY_DIR}/wsf_install。  
CMAKE_UNITY_BUILD: 启用或禁用 CMake unity 构建支持（在 CMake 3.16 及更高版本中可用）。此功能 启用每个目标内多个源的批量编译 ，显著提高构建时间。具体结果将根据 CPU、I/O 子系统、操作系统和编译器而有所不同。观察到的 AFSIM 结果通常显示干净构建的时钟时间至少提高 3 倍。  
PROMOTE_HARDWARE_EXCEPTIONS: 当设置时，ut::PromoteHardwareExceptions(true)允许硬件异常（如除以零和访问违规）提升为 ut::HardwareException。在 Windows 上，必须在每个线程上单独调用该函数。当未设置 CMake标志时，该函数仍然可调用但不执行任何操作。  
WSF_ADD_EXTENSION_PATH: 定义扩展和插件的附加搜索路径。可以使用分号分隔的列表指定多个路径。  
WSF_PLUGIN_BUILD: 构建共享对象或 DLL 库而不是静态库，并在生成的可执行文件中启用插件。默认是 TRUE。  
WSF_INSTALL_SOURCE: 启用或禁用源文件的安装。默认是 FALSE。  
WSF_INSTALL_DOXYGEN: 启用或禁用 Doxygen 目录及子目录的安装（如果构建了DOXYGEN 目标）。默认是 FALSE。  
WSF_INSTALL_DOCUMENTATION: 启用或禁用文档目录及子目录的安装（如果构建了DOCUMENTATION 目标）。默认是 FALSE。  
WSF_INSTALL_DEMOS: 启用或禁用演示目录及子目录的安装。默认是 FALSE。  
WSF_INSTALL_SCENARIOS: 启用或禁用场景目录及子目录的安装。默认是 FALSE。  
WSF_INSTALL_TOOLS: 启用或禁用工具目录及子目录的安装。默认是 FALSE。  
WSF_INSTALL_TRAINING: 启用或禁用培训目录及子目录的安装。默认是 FALSE。  
WSF_INSTALL_DEPENDENCIES: 启用或禁用依赖项的安装，例如 MSVC 运行时、MESA GL库等。默认是 FALSE。

# 配置第三方库和资源

有多种选项可用于配置第三方和资源依赖项。这些依赖项是使用 GTest 创建单元测试目

标 和 构 建 GUI 应 用 程 序 所 必 需 的 。 在 默 认 配 置 中 ， CMake 将 在${CMAKE_SOURCE_DIR}/../dependencies/3rd_party 中 查 找 第 三 方 包 ， 并 在${CMAKE_SOURCE_DIR}/../dependencies/resources 中查找资源存档。

SWDEV_THIRD_PARTY_ROOT: 第三方包将被提取到的目录，或包含已解压库的现有目录。如果未指定，CMake 将尝试检测由环境变量 SWDEV_THIRD_PARTY_PATH 定义的现有3rd_party 目录，或包含在源树中或与源树平行的目录。如果在这些位置中未检测到3rd_party 目录，将在默认位置${CMAKE_BINARY_DIR}/3rd_party 中创建一个。  
SWDEV_THIRD_PARTY_PACKAGE_SOURCES: 包含 tar.gz、tar 或 zip 格式的第三方包的源目录。可以在分号分隔的列表中指定多个搜索路径。如果未指定，默认位置是${CMAKE_SOURCE_DIR}/../dependencies/3rd_party。  
VTK_DEV_RESOURCES_PATH: 资源存档将被提取到的目录，或包含已解压资源内容的现有目录。默认位置是${CMAKE_SOURCE_DIR}/../resources。  
VTK_RESOURCES_SOURCEDIR: 包含资源存档或外部管理的已解压资源的源目录。如果未指 定 ， 默 认 位 置 是 ${CMAKE_SOURCE_DIR}/../dependencies/resources ， 除 非 定 义 了VTK_RESOURCES_SEARCH_PATH。

注意：以下变量标记为高级选项，仅在 CMake GUI 中选中“Advanced”框时可见：

VTK_RESOURCES_SEARCH_PATH: 作为 VTK_RESOURCES_SOURCEDIR 的替代方案，定义资源的初始搜索路径，使用分号分隔的列表。为开发人员或构建系统提供一个钩子，以指定 替 代 布 局 而 无 需 修 改 源 代 码 。 发 现 的 第 一 个 有 效 目 录 将 被 设 置 为VTK_RESOURCES_SOURCEDIR（并缓存以供后续执行）。  
VTK_RESOURCES_ARCHIVE_FILENAME: 要 提 取 的 资 源 存 档 的 文 件 名 。 默 认 是vtk_resources-<version>-noarch.tar.gz。  
VTK_RESOURCES_CONTINUEIFMISSING: 指定如果未找到所需资源，CMake 是否应警告并继续生成。如果为 false（默认），则会产生错误，继续处理但跳过生成。

# 构建标准 AFSIM 应用程序

要构建一个或多个标准应用程序（如 mission 等），可以根据操作系统选择不同的方法。Windows

# CMake 目标

CMake生成多个目标，包括每个可执行文件和库的目标。以下是可用的 CMake预定义目标：

ALL_BUILD: 构建所有应用程序和库。  
INSTALL: 生成一个安装目录，安装 CMakelists.txt 文件中定义的所有项目。有关详细信息，请参阅构建安装目标。  
INSTALL_RUNTIME_ONLY: 仅生成包含运行时组件（如库、插件、可执行文件、语法）的安装目录。这可以用于生成运行 AFSIM 所需的最小组件集，从而通过不安装文档、演示等来减少安装时间。  
PACKAGE: 使用 CMake 选项中指定的 CPack 生成器创建用于分发的包文件：CPACK_BINARY_ZIP 用于 zip 文件或 CPACK_BINARY_WIX 用于 msi 安装程序（需要 WiX）。  
RUN_TESTS: 运行项目中定义的所有单元测试。需要安装 gtest。

ZERO_CHECK: 由 CMake 为 Visual Studio 集成自动生成，忽略。

# 自定义目标

<application-name>_AUTO_TEST: 针对<application-name>应用程序运行所有测试。  
<application-name>_REGRESSION_TEST: 针对<application-name>应用程序运行演示和场景的回归输出。  
DOCUMENTATION: 在 BUILD 目录中生成名为 documentation 的文件夹中的文档以供安装。有关详细信息，请参阅构建文档目标。  
DOXYGEN: 在 BUILD 目录中生成名为 doxygen 的文件夹中的 Doxygen（代码）文档以供安装。打开 BUILD 目录中的 afsim.sln 文件，使用 Visual Studio 进行构建。

1) 打开“配置管理器”（Build $^ { - > }$ Configuration Manager）或使用标准工具栏（View $- >$ Toolbars->Standard）并选择所需的活动解决方案配置。  
2) 在解决方案资源管理器中选择 INSTALL。  
3) 为解决方案配置选择 Release（除非构建调试版本）。  
4) 开始构建。

Linux

从 BUILD 目录运行：

```txt
make <make-options> <make-targets> 
```

# Make 目标

以下是可用的 CMake预定义目标：

all: 构建所有应用程序和库。如果未指定，这是默认目标。  
install: 构建并安装工件到 CMAKE_INSTALL_PREFIX（默认是 BUILD/wsf_install）。  
clean: 删除所有创建的构建产品（对象文件、库和可执行文件的调试和优化版本）。  
package: 使用适当的 CPack 生成器（deb、rpm 或 tar.gz）创建用于分发的包文件。  
test: 运行项目中定义的所有单元测试。需要安装 gtest。

# 自定义目标

<application-name>_AUTO_TEST: 针对<application-name>应用程序运行所有测试。  
<application-name>_AUTO_TEST_VALGRIND: 使用 valgrind 输出 xml 文件进行解析，针对<application-name>应用程序运行所有测试。  
<application-name>_REGRESSION_TEST: 针对<application-name>应用程序运行演示和场景的回归输出。  
DOCUMENTATION: 在 BUILD 目录中生成名为 documentation 的文件夹中的文档以供安装。  
DOXYGEN: 在 BUILD 目录中生成名为 doxygen 的文件夹中的 Doxygen（代码）文档以供安装。

# Make 选项

-j[jobs]: 指定同时运行的作业（命令）数量。如果给出 -j 选项而没有参数，make将不限制可以同时运行的作业数量。 -j8 是一个不错的折衷选择，如果不希望垄断系统。  
VERBOSE $^ { = 1 }$ :CMake在调用编译器和链接器时隐藏了许多细节，使得调试构建问题变得困难。此命令强制所有由 make运行的命令输出到 STDOUT。

构建安装目标

用户可以使用 INSTALL 目标进行构建，该目标在 CMAKE_INSTALL_PREFIX 创建一个新的安装目录，并将所有先前构建的应用程序、库和插件拉入新目录。

注意：需要成为安装一部分的任何文档工件必须在运行安装目标之前生成。

对于 Windows，在运行 INSTALL目标之前，必须在配置管理器中选择 Release 配置。  
对于 Linux，在运行安装目标之前，必须将 CMAKE_BUILD_TYPE 选项设置为 Release。

安装目录示例如下：

```txt
path/to/afsim/install  
|__bin  
|__grammar  
|__lib  
|__missionPlugins  
|.  
|.  
|dis.dll  
|.  
|.  
|resources  
|__data  
|__maps  
|__models  
|__shaders 
```

构建文档目标

有关构建文档的详细信息，请参阅文档生成。

提示：构建文档不需要完整构建。构建 DOCUMENTATION 目标足以生成文档。

运行系统测试

系统测试确保 AFSIM（特别是核心应用程序 mission）正常工作。AFSIM扩展和插件也可以通过在以下路径上拥有 test_*.txt 文件来测试其功能：

```txt
path/to/afsim/extension_name/wsf_<extension_name>/test_mission 
```

成功测试的输出将是：

-TEST- Using <path-to>/mission_<suffix>.exe Running ### tests Tests Complete in $\# .\#$ s   
##### tests passed   
-PASS- No errors detected

Windows

从 Visual Studio 构建<application-name>_AUTO_TEST 项目。

注意：在插件构建中，必须在目标<application-name>_AUTO_TEST 之前运行 ALL_BUILD目标，以便在适当位置正确安装插件以进行自动测试。

# Linux

从 BUILD 目录运行：

```txt
make <application-name>_AUTO_TEST 
```

注意：在插件构建中，必须在目标<application-name>_AUTO_TEST 之前运行 make 命令，以便在适当位置正确安装插件以进行自动测试。

# 运行回归测试

回归测试确保 AFSIM 操作（特别是核心应用程序“mission, sensor_plot 等”）与所有演示和场景正常工作，并与黄金标准输出进行比较。演示和场景目录结构包含一个名为regression_tests 的目录，其中有一个名为<application-name>_list.txt 的文件。此文件包含要针对应用程序运行的演示和场景列表，并收集输出以与该演示或场景的黄金标准输出进行比较。所有测试输出都放置在 BUILD 目录下名为 regression 的文件夹中。此文件夹包含演示和场景输出事件以及应用程序输出列表，以便与存档的黄金标准输出进行比较。

```txt
path/to/demos/scenarios/regressionTests/<application-name>_list.txt 
```

成功测试的输出将是：

-REGRESSION TEST-Using <path/to>/mission_<suffix>.exe Running ### tests Tests Complete in $\# .\# s$ ## tests passed -PASS-No errors detected

回归输出将放置在以下目录中：

```txt
<build-directory>/regression/<demo/scenario/dirty-name> 
```

# Windows

从 Visual Studio 构建<application-name>_REGRESSION_TEST 项目。

注意：在插件构建中，必须在目标<application-name>_REGRESSION_TEST 之前构建ALL_BUILD 目标，以便在适当位置正确安装插件以进行回归测试。

# Linux

从 BUILD 目录运行：

```txt
make <application-name>_REGRESSION_TEST 
```

注意：在插件构建中，必须在目标<application-name>_REGRESSION_TEST 之前运行 make命令，以便在适当位置正确安装插件以进行回归测试。

故障排除

遇到构建问题时，可以使用以下故障排除提示：

验证构建工具是否符合先决条件中的正确版本。  
删除现有的 BUILD 目录并重新构建 AFSIM目标。  
确保构建环境具有正确的路径或远程地址以获取第三方库和资源。  
当由于缺少库而导致已构建的应用程序无法运行时，请使用 Install目标进行构建。通常发生在应用程序已编译但未安装时。

# 1.3.2. 文档指南 Documentation Guide

文档是所有与 AFSIM软件交互者的基本组成部分。

首先，它是用户发现和参考 AFSIM 功能的主要媒介，并在引入新功能时保持对软件变化的最新了解。

除此之外，由于 AFSIM 是许多开发者多年来贡献的成果，良好维护的文档对于开发者来说是维护和扩展软件的重要工具。

理解文档对使用和/或支持 AFSIM 的各方的核心功能，需要建立、理解并实践一个标准，以确保 AFSIM文档的可维护性、一致性和通用导航性。

本指南用于描述支持所有 AFSIM 文档（即文档）的系统。熟悉本指南及其组件将使开发者能够更有效地编写和导航 AFSIM文档。

# 介绍

文档以多种格式提供给用户。虽然文档在每种格式中以统一状态提供，但以这种方式维护文档并不实用。相反，文档分布在许多相对较小的 ReStructuredText 文件中，并使用 Sphinx和其他工具生成。（参见文档生成）

为了定义 AFSIM 文档标准，需要详细介绍 ReStructuredText、Sphinx 以及 AFSIM SphinxExtensions 引入的各种功能。

注意：有关构建文档所需的软件和版本要求的详细说明，请参阅构建说明。

# ReStructuredText

ReStructuredText（RST）被描述为 一种易于阅读、所见即所得的纯文本标记语法和解析系统 。RST 是 docutils 的一个组件，docutils 是一个开源 Python 项目，被描述为 一个将文档处理成有用格式的模块化系统 。

详尽的 RST 标记规范在 docutils 中描述。

# Sphinx

尽管文档生成因最终格式而异，但所有 AFSIM 文档的生成都始于 Sphinx。Sphinx是一个根据 BSD-3-Clause 许可的开源 Python 项目。它使用 RST 作为其标记语言，并包括内置支持以增强 RST 标记，原生扩展了 docutils 提供的功能。它能够生成多种格式的文档，包括 HTML和 LaTeX 等。

重要的是，Sphinx 设计用于扩展性，并提供文档间的交叉引用支持。

为了支持 AFSIM 文档，AFSIM 源代码包括 AFSIM Sphinx Extensions，这些扩展定义了除Sphinx和 docutils 提供的标记之外的自定义标记。

# 1.3.3. 编程规范 Coding Standards

# 引言

本文档包含了高级仿真、集成和建模框架 (AFSIM) 的 ${ \mathsf { C } } { + } { + }$ 编码标准和指南。本标准适用于 AFSIM开发工作和使用该框架开发的应用程序。

# 本文档的主要目标：

为 AFSIM相关的软件项目提供一致性。  
提高 ${ \mathsf { C } } { \mathsf { + } } { \mathsf { + } }$ 软件的理解性、可靠性和可维护性。  
为项目提供制定项目特定编码标准的能力。  
对于本文档未解决的问题，请参考 ${ \mathsf { C } } { \mathsf { + } } { \mathsf { + } }$ 核心指南。

注意 如果规则编号后有(G)，则该项为指导原则，不需要像未标记项那样严格遵循。如果规则编号后有(F)，则该项由 clang-format 自动处理（F*表示部分支持）。

# 文件

$\mathsf { F i } . 1 \textrm { - C + + }$ 中的包含文件应具有文件名扩展名“.hpp”。  
$\mathsf { F i . } 2 \textrm { - C + + }$ 中的实现文件应具有文件名扩展名“.cpp”。

这些约定的目的是提供文件名的统一解释。这些规则将使基于文件名扩展名创建工具更容易。

Fi.3- 只有类、结构体、联合体和非成员操作符函数应在 .hpp 文件的文件范围内声明。  
Fi.4- 只有类、结构体、联合体和内联（成员或非成员操作符）函数应在 .hpp 文件的文件范围内定义。

[来源：Lakos, John, Large-Scale ${ \mathsf { C } } { + } { + }$ Software Design. p. 77]

Fi.5- 应避免在文件范围内使用具有外部链接的数据。

在文件范围内声明具有外部链接的变量会使它们成为全局变量并污染全局命名空间。通常，应避免全局可访问的数据。如果确实有必要，它们应包含在类、结构或命名空间中。

示例：

```txt
namespace Data { int i; }; 
```

[来源：Lakos, John, Large-Scale ${ \mathsf { C } } { + } { + }$ Software Design. p. 70]

Fi.6- 每个包含文件应包含防止文件多次包含的机制。

避免文件多次包含的最简单方法是使用#ifndef#define 块在文件的开头，并在文件末尾使用#endif。

#ifndef 块应使用全文件名的全大写字母，后跟_HPP。

包含的文件数量将被最小化，从而减少编译时间。此外，一些链接器会因多次声明而感到困惑。

注意：预处理器指令#pragma once 是非标准的，不应使用。

示例：

```txt
ifndef XYZ_HPP #defineXYZ_HPP 
```

// 文件的其余部分

#endif // XYZ_HPP great for nested if's

Fi.7- 应最小化包含子句的范围。

在最低可能的级别使用包含，以最小化对单元的更改。例如，头文件不应指定仅在实现文件中需要的包含。

Fi.8(F)- 实现文件的相应头文件应是第一个包含的文件。

此外，声明或实现文件应至少在两个块中列出包含文件。第一个块应包含系统包含文件。第二个块应包含本地包含文件。每个这些块应按字母顺序列出。

示例：

```cpp
//**********  
// UtEntity.cpp  
//**********  
# include "UtEntity.hpp"  
# include <algorithm>  
# include <cassert>  
# include <cmath>  
# include <iostream>  
# include "UtDCM.hpp"  
# include "UtEarth.hpp"  
# include "UtEllipsoidalEarth.hpp"  
# include "UtEntityPart.hpp"  
# include "UtMath.hpp"  
# include "UtMat3.hpp"  
# include "UtVec3.hpp" 
```

Fi.9 - 用户准备的包含文件应使用指令#include "filename"。  
Fi.10 - 来自外部库的包含文件应使用指令#include <filename>。

ISO ${ \mathsf { C } } { + } { + }$ 标准指定文件搜索是以实现定义的方式执行的。标准中定义的唯一搜索标准是如果#include " "搜索失败，则应重新处理该指令，使其读取#include < >。

经验表明，大多数编译器实现了一种搜索机制，其中#include $< >$ 符号使编译器搜索其${ \mathsf { C } } { \mathsf { + } } { \mathsf { + } }$ 库目录，而#include""符号使编译器首先搜索用户定义的目录。

Fi.11- 所有必要的包含文件都应在给定的头文件中显式定义。

如果需要包含一个文件以供头文件使用，则必须使用#include 符号显式定义，不应假定它会被其他包含文件之一间接包含。这消除了头文件的依赖性，使代码更具可移植性。

Fi.12- 不应在#include 指令中指定绝对文件路径名。

避免使用绝对路径可以更灵活地重新组织目录结构而无需更改源文件。它还使编译过程更具可移植性；适应于在不同操作系统环境中编译相同源代码等。

Fi.13- 在#include 指令中指定路径名时应使用正斜杠。

虽然一些编译器将支持正斜杠和反斜杠，但 ISO ${ \mathsf { C } } { \mathsf { + } } { \mathsf { + } }$ 标准规定应使用正斜杠。因此，使用正斜杠使代码更具可移植性。

Fi.14(G)- 仅通过指针（*）或引用（&）引用的类的定义不应作为包含文件包含，而应

进行前向声明。

在头文件中，如果您只有一个类的指针或引用，则不需要包含该类的头文件。相反，使用前向声明告知编译器该类存在。这减少了重新编译的依赖性。

示例：  
```cpp
// file: PackableString.hpp
#ifndef PACKABLESTRING_HPP
#define PACKABLESTRING_HPP
#include "String.h"
class Buffer;
class PackableString : public String
{
public:
    PackableString(const String& aS);
    Buffer* Put(Buffer* aOutbufferPtr);
    // ...
};
#endif
// file: PackableString.cpp
#include "PackableString.hpp"
// To be able to use Buffer-instances, Buffer.hpp MUST be included.
#include "Buffer.hpp"
Buffer* PackableString::Put(Buffer* aOutbufferPtr)
{
    // ...
} 
```

Fi.15(G)- 包含类声明或定义的文件名应与其包含的类和命名空间相同。

注意：通过遵循此指南以及规则 Id.7（要求类名以该库唯一的前缀和/或命名空间开头），文件名也将以此前缀和/或命名空间开头。

Fi.16(G)- 一个包含文件不应包含多个（非嵌套）类声明。  
Fi.17(G)- 实现文件应只包含一个（非嵌套）类的函数定义。

在每个实现文件中一次放置一个类的实现会创建更模块化的代码，并且更易于维护。如果类的实现太复杂，可能需要重新考虑该类的设计。此外，对于那些使用和维护类的人来说，如果每个文件中只有一个类定义并且不同类的成员函数实现不在同一文件中，这会更容易。嵌套类是一个例外，其定义或实现可以包含在另一个类的定义或实现中。

Fi.18(G)- 如果一个函数是一个类的朋友，则函数声明（原型）应包含在与类声明相同的头文件中。

相应的函数定义应包含在类定义文件中。参见 Cl.24 关于使用朋友的限制。

Fi.19(G)- 逻辑上相关的全局实体应封装到一个唯一的类或命名空间中。

将逻辑上相关的实体放入一个唯一的类或命名空间中，利用了 ${ \mathsf { C } } { + } { + }$ 封装，以向代码的阅读者展示实体之间的关系。

Fi.20 - using 指令不应位于文件范围内

注意：这以前只适用于被包含的文件。它现在指的是所有文件，包括实现文件。

在头文件中使用 using 指令，实际上将关联命名空间的内容放在文件范围内，这违背了命名空间的目的。

此外，一些项目可能会通过包含实现文件来构建他们的产品。如果特定的实现文件中有一个全局的 using 指令，那么在其之后包含的所有文件都会使用该 using 指令进行构建。由于 using 指令的存在，之后构建的文件可能会表现出不同的行为，这可能对最终产品产生负面影响。

相反，应该在局部声明 using 指令，或者在需要的地方使用命名空间限定符。

一个首选的替代方法是仅导入所需的项目。

using std::cout;   
using std::endl;   
int main()   
{ cout $<  <   \text{"Hello world!"} <  <   \text{endl};$ return 0;   
1

在头文件或“包含的”实现文件中的好例子：

```cpp
XTypes::Float64Min EContributors::GetLastUpdateTime (BObjectIdentifier& aContributor)  
{ double lastUpdateTime = 0.0; std::vector< EContributor* >::iterator i = FindContributor(aContributor); if (i != mCcontainer.end()) { lastUpdateTime = (*i)->GetTimeLastContributed(); } return lastUpdateTime; } 
```

在头文件或 包含的 实现文件中的好例子：

```cpp
XTypes::Float64Min EContributors::GetLastUpdateTime (BObjectIdentifier& aContributor)  
{  
    using namespace std;  
    double lastUpdateTime = 0.0;  
    vector< EContributor* >::iterator i = FindContributor(aContributor);  
    if (i != mContainer.end())  
    { 
```

lastUpdateTime $\equiv$ (\*i)-->GetTimeLastContributed(); } return lastUpdateTime;

在头文件或 包含的 实现文件中的坏例子：

using namespace std;   
XTypes::Float64Min EContributors::GetLastUpdateTime (BObjectIdentifier& aContributor)   
{ double lastUpdateTime $\equiv$ 0.0; vector< EContributor\* $>$ :iterator i $=$ FindContributor(aContributor); if (i != mContainer.end()) { lastUpdateTime $\equiv$ (\*i)->GetTimeLastContributed(); } return lastUpdateTime;   
}

# 标识符

Id.1- 常量和枚举值应以小写字母 c 开头，后接全大写字母，每个单词之间用下划线分隔。

例外：需要作用域的值（例如使用 enumclass）可以以大写字母开头，并使用驼峰式命名法。

示例：

//运行时初始化  
//file.cpp  
const int cSOMECONST $= 5$ //对象数据成员常量  
class A{private:const int cMYCONST;};

Id.2- 类型和函数的名称应以大写字母开头。  
Id.3- 局部变量的名称应以小写字母开头。

变量以小写字母开头是因为这在 ${ \mathsf { C } } { \mathsf { + } } { \mathsf { + } }$ 工业界中很常见。

Lambda函数是局部变量，应遵循此约定。

例外：变量以首字母缩略词开头（如 BOTSize，其中 BOT是公认的缩略词）时，预计以大写字母开头。

Id.4- 名称由多个单词组成时，单词应连接在一起，第一个单词之后的每个单词应以大写字母开头。

这种方法通常称为驼峰式命名法，是 ${ \mathsf { C } } { + } { + }$ 开发中的常见做法。

例外：如果单词/缩略词的最后一个字母是大写，则应使用下划线作为单词/缩略词分隔符。

示例：

```c
int currentStream = 1;  
int currentIO_STREAM = 1; // currentIO 的最后一个字符是大写  
void SomeMemberFunction();
```

Id.5- 两个标识符（如类名和对象名）不应仅通过使用大写和小写字母来区分。

一些开发环境（包括编译器、调试器和链接器）不能很好地处理大小写差异。避免这种情况也能为开发者省去一些麻烦。

Id.6 - 不应使用以一个或两个下划线（'_' 或 '__'）开头的标识符。

根据 ISO ${ \mathsf { C } } { + } { + }$ 标准，使用两个下划线（'__'）在标识符中是为编译器的内部使用保留的。同样，以单个下划线加大写字母开头的标识符，以及在全局范围内以下划线开头的所有名称都是保留的。

下划线（'_'）通常用于库函数的名称（如“_main”和“_exit”）。为了避免冲突，不应以下划线开头标识符。

Id.7- 在集合中，每个全局可见项的标识符应以该集合唯一的前缀或命名空间开头（例如 wsf、ut、wkf 等）。

为全局可见符号使用集合前缀或命名空间将减少链接多个库时名称冲突的可能性。新代码优选使用命名空间，旧代码和一些命名空间通常使用前缀。

注：术语 集合 （在此规则中使用）旨在表示项目的逻辑分组。它不是 ${ \mathsf { C } } { + } { + }$ 语言术语。有许多可供购买的类库，在大型项目中可能有数万个类。因此，重要的是要小心不要发生名称冲突。防止冲突的一种方法是为全局可见对象（例如前缀或命名空间）指定严格的命名规则。这样，来自几个不同类库的类可以同时使用。

以下类型的项目的名称应在集合中加上前缀和/或命名空间：类型名称（类、typedefs、枚举、结构、联合等）、全局变量和常量、函数名称（不是成员函数名称）和预处理器宏（#define）。

注：遵循此规则以及规则 Fi.15（要求文件名与类和/或命名空间名称相同），文件名也将以库前缀或命名空间开头。

示例：

```txt
namespace wsf   
{ class ClassName { //... } 
```

Id.8- 在词法嵌套的范围内，标识符应该是不同的：没有标识符应该与外部封闭范围中的名称相同。

虽然 ${ \mathsf { C } } { \mathsf { + } } { \mathsf { + } }$ 的可见性规则允许这样做，但不建议这样做。读者必须了解标识符的来源才能理解软件逻辑。如果标识符在嵌套范围内重复，可能无法立即显现正在使用的是哪个。

示例：

```txt
int someVar = 0;  
for (int someVar = 3; someVar < count; ++someVar)  
{  
    temp = temp + anArray[someVar]; // 内部"someVar"遮蔽了  
    // 外部"someVar"的范围  
} 
```

Id.9- 类数据成员应以“m”作为前缀。

示例：

```txt
class Person   
{ private: int mAge; int\* mSizePtr;   
} 
```

Id.10 - 函数的形式参数名称应以“a”作为前缀。

示例：

```c
int SetPoint(int x, int y); //不好！  
int SetPoint(int aX, int aY); //好
```

Id.11- 首次使用缩略词时应进行定义。  
定义缩略词使代码对可能不熟悉该领域的其他开发人员更清晰。  
Id.12- 访问函数（访问器和变异器）应分别以“Get”和“Set”开头。

返回（访问器）或更改（变异器）成员数据的访问函数应具有一致的名称，以便函数的意图易于识别。使用 Get 表示访问器函数，使用 Set 表示变异器函数是相当标准的。

对于返回布尔值的访问器，可以接受使用前缀“Is”和“Has”。

Id.13(G)- 成员函数应使用动词-名词的命名约定。

使用动词-名词约定，如函数 DrawContent()。

Id.14 (G) - 布尔标识符应反映条件的“真”意义。

为了避免双重否定带来的混淆并促进一致性，布尔标识符本身应反映条件的 真 意义。

示例：

```txt
bool partOn = true; // 表达布尔值更清晰的方式  
bool partOnFalse = false; // 不如上面清晰
```

#

Ws.1(F)- 缩进应使用三个空格。不得使用制表符。

使用 3 个空格的倍数进行缩进是许多项目采用的良好实践。应使用空格而不是制表符，因为某些编辑器会保存 制表符字符 而不是 空格字符 ，这可能导致另一个编辑器将 制表符字符 扩展为不同于 3 个空格的数量。

Ws.2(F)- 续行应至少比语句开头的缩进级别向右缩进三个空格。

为了美观的垂直对齐，可能需要缩进超过三个空格。

Ws.3- 每行不应有超过一个 ${ \mathsf { C } } { + } { + }$ 语句。

如果在一行的前后放置多个 ${ \mathsf { C } } { + } { + }$ 语句，人眼可能会遗漏其中一个。

示例：

// 以下行包含多个 ${ \mathsf { C } } { + } { + }$ 语句 - 不好

$$
a = 3; b = 4;
$$

Ws.4 (F) - 二元运算符（+，=，&&等），除了成员访问运算符（a.x，b->y，c::z），前后应有空格。  
Ws.5 (F) - 一元运算符（someVar++，!someVar 等）与其操作的变量之间不应有空格。  
Ws.6(F)- 逗号和分号后应有空格。  
Ws.7 (F) - 冒号后应始终跟随空格。遵循以下示例来放置冒号前的空格

class Derived : public Base // 继承：空格  
{public: // 访问说明符：无空格enum Colors : short // 枚举基类型：空格{cRED,cGREEN,cBLUE,cBLACK}；explicit Derived(const std::vector<Colors>& aList):Base(aList) // 类初始化器：空格{label: // 标签：无空格（注意：不推荐使用标签（参见Mi.4），但为了完整性在此列出。）Colors appearance $=$ (aList.empty()？cBLACK :alist[0]);// 三元运算符：空格for (auto color : aList) // 范围 for：空格switch (aColor){case cRED:// case 标签：无空格// ...break;default: // 默认标签：无空格//...1}1

Ws.8(F)- 函数名之后及左圆括号之前不应有空格。

Ws.9(F)- 除非在计算数组索引的某种运算中，或括号对[]是 delete[]语句的一部分，否则在方括号前后不应留空格。  
Ws.10(F)- 声明指针和引用时，*和&运算符应紧挨类型名称，并后跟空格。

这些字符应与变量的类型一起书写，而不是与变量名一起，以强调它们是类型定义的一部分。与其说\*i 是一个 int，不如说 i 是一个 int\*。

规则 Va.3 与此规则密切相关。如果允许在同一行声明多个变量，则修饰符\*放在类型名后，只适用于第一个变量而不适用于后续变量。这可能会被轻易误解！

示例：  
unsigned char\* Object::AsString()   
{ //...   
}；   
unsigned char\* userName $\equiv$ 0; int sfBook $= 42$ int& anIntRef $\equiv$ sfBook;

示例：  
```txt
// 不允许 - 容易被误解  
unsigned char* i, j; // i 被声明为指向无符号字符的指针  
// 而 j 被声明为无符号字符
```

Ws.11(F)- 括号{}应放在同一列上，并在块之前和之后分别单独占据一行。例外：在由 0 或 1 个语句组成的短块中，两个括号可以放在同一行上。

Ws.12- 流控制原语 if、else、while、for 和 do 应该跟随一个块，即使它是一个空块。块的括号 {} 不应缩进，但块的内容应缩进。

有时，循环中要完成的所有操作都可以很容易地在循环语句本身的一行中编写。这时可能会倾向于在行末用分号结束语句。这可能导致误解，因为在阅读代码时，很容易忽略这样的分号。最好在语句后放置一个空块，以完全清楚地表明代码在做什么。

示例：  
```txt
//没有块-不好！  
while(/*Something\*/);  
//空块-更好！  
while(/*Something\/)  
{ //空  
}
```

此外，尽管 ${ \mathsf { C } } { \mathsf { + } } { \mathsf { + } }$ 不要求单语句结构使用作用域括号，但一致地使用它们（对于单语句或多语句结构）是一个好习惯。它可以防止在单语句结构中添加语句时程序员忘记添加作用域

括号的可能性。

示例：

```txt
// 不要这样做：  
if (flightStatus == PARKED)  
    engineStatus = OFF;  
// 应该这样做：  
if (flightStatus == PARKED)  
{  
    engineStatus = OFF;  
}
```

Ws.13(F)-template关键字和后续的形式参数列表应与函数或类声明分开行放置。函数声明行应紧跟在泛型参数列表行之后。

示例：

```txt
template<class ElementType, class ComparatorType> ElementAverageType(ElementType alInputElement, ComparatorType alInputComparator) {
    // ...
} 
```

Ws.14(F)- 控制流原语（if、while、for等）和左括号之间应有一个空格。  
Ws.15(G)(F)- 空格不应跟在左括号之后或出现在右括号之前。

括号内的空格通常是不必要的。有时它可以用于对齐和区分嵌套的括号分组。

Ws.16 (G) (F) - 应尽量减少两个或多个连续空行的出现。

多个连续空行很少是必要的，通常看起来很凌乱。要分隔代码的“块”，请使用战略性注释块而不是多个空行。

Ws.17(G)(F*)- 应使用垂直对齐来增强声明、语句、表达式、括号、函数参数以及战术和战略注释的可读性。

示例：

```c
//易于阅读  
int column = FIRST_COLUMN;  
int row = FIRST_ROW;  
char columnRowValue = 'A';  
//不太易于阅读  
int column = FIRST_COLUMN;  
int row = FIRST_ROW;  
char columnRowValue = 'A'; 
```

示例：

// 易于阅读：

```txt
int MyComplicatedFunction(unsigned unsignedValue, int aIntValue, char aCharPointerValue, int* aIntPointerValuePtr, myClass* aMyClassPointerValuePtr, unsigned int* aUnsignedPointerValuePtr); 
```

```c
// 不太易于阅读：  
int MyComplicatedFunction(unsigned aUnsignedValue, int aIntValue, char aCharPointerValue, int* aIntPointerValuePtr, myClass* aMyClassPointerValuePtr, unsigned int* aUnsignedPointerValuePtr);
```

Ws.19 (G) - 为了可读性，在编写注释时，//之后应有一个空格。

例外：为自动文档编写的注释（例如使用 Doxygen）不需要遵循此指南。

# 注释

注释通常被称为 战略性 或 战术性 。战略性注释描述了一个函数或代码段的意图，并放置在函数或代码之前。战术性注释描述了一行代码的意图，通常放在行尾。

Co.1 - 注释标记应使用字符“//”，除非自动文档需要其他标记（例如使用 Doxygen）。

如果始终使用 // 来编写注释，则可以使用组合 $" / \ast * / \prime \prime$ 在开发和调试阶段将整个代码段注释掉。

示例：

//! 描述一个人的类。

```txt
class Person   
{ private: int mAge; int\* mSizePtr; //指针   
}；
```

Co.2- 除构造函数、析构函数和私有函数外，每个类、函数和成员函数都应在声明处用战略性注释块进行文档化。

使用 Doxygen 自动生成文档。战略性注释块应详细到足以让另一位开发者合理地使用所描述的组件而无需参考实现。

Co.3- 在头文件中，定义在该文件中的每个函数或成员函数（除构造函数、析构函数和私有函数外）都应有战略性注释块。  
Co.4 (G)- 注释，尤其是战略性注释，应遵循标准的语法规则，例如完整的句子和正确的标点。

由于战略性注释通常由几句话或更多组成，应遵循语法规则以促进可读性和一致性。

# 类

Cl.1 - 当所有成员数据可以独立变化时，应使用结构体。 (CppCoreGuidelines C.2)

为了保持一致性，如果您有逻辑分组的成员函数，请不要使用结构来代替类。结构体应仅包含数据成员。

Cl.2 - 类的 public、protected 和 private 部分应按此顺序声明。  
Cl.3 - 类的 public、protected 和 private 关键字应缩进，且每个部分下的实体应进一步缩进。

将 public 部分放在最前面，可以让用户感兴趣的所有内容都集中在类声明的开头。protected 部分在考虑从类继承时可能会引起设计者的兴趣。private 部分包含的细节应该是最不受关注的。一致的缩进可以提高可读性。

示例：

```javascript
class SomeClass   
{ public: //whatever protected: //whatever private: //whatever }; 
```

Cl.4- 在类的 public 部分之前，可以声明以下实体：Q_OBJECT 及其相关、私有范围的类型和朋友。  
Cl.5 - 在类的 public 部分，实体应按以下顺序声明：枚举类型、构造函数、类析构函数、成员函数（非运算符）、运算符成员函数，然后是其他公共对象。  
Cl.6- 在类的 protected 部分，实体应按以下顺序声明：成员函数（非运算符）、运算符成员函数，然后是枚举类型。  
Cl.7- 在类的 private部分，实体应按以下顺序声明：成员函数（非运算符）、运算符成员函数，然后是类成员数据（包括类型、结构和枚举类型）。

每个部分内实体的排序可以促进一致性。

例外 在某些情况下，为了编译原因，可能需要将某些实体（例如枚举类型）上移到某个部分内。

Cl.8- 多态类应具有虚析构函数。

如果一个类有虚函数但没有将其析构函数定义为虚函数，则可能会在不适当地析构派生对象时冒风险。如果在派生对象上调用 delete（如附带示例所示），则只调用基对象的析构函数。将基对象的析构函数声明为虚函数可以解决此问题。

例外 在运行时和内存有限的情况下，并且可以确定类继承不会发生或即使发生也会正确销毁应用程序时。

示例：

```txt
class Base{ 
```