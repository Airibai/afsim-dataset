Cl.9- 不应重新定义继承的非虚函数。

如果在派生类中重新定义非虚函数，可能会导致意外行为。如果将基类指针类型（而不是派生类指针类型）分配给派生类的地址，则调用重新定义的非虚函数实际上会调用基类中的函数！

注意 引用与指针表现出相同的行为。

示例：

class ClassA   
{ public: void DoFunction();   
}；   
class ClassB :public ClassA   
{ public: void DoFunction(); //注意这个继承的 //非虚函数被重新定义！   
}；   
void main()   
{ ClassB objectOfClassB; //创建ClassB的对象 ClassB\* aClassB_TYPEPtr $=$ &objectOfClassB; //创建指向派生类类型的指针 //指向派生类 aClassB_TYPEPtr->DoFunction(); //调用ClassB中重新定义的

```txt
// DoFunction()（不意外）  
ClassA* aClassA_TYPEPtr = &objectOfClassB; // 创建指向基类类型的指针 // 指向派生类  
aClassA_TYPEPtr->DoFunction(); // 调用 ClassA 中定义的 // DoFunction(), 尽管 // 指向 ClassB!
```

例外 在某些无法修改基类的情况下，重新定义非虚函数可能是可以接受的。

Cl.10- 在继承的虚函数中，不应重新定义默认参数。

在继承的虚函数中重新定义默认参数可能会导致意想不到的事情发生。如果将基类指针类型（而不是派生类指针类型）分配给派生类的地址，则调用继承的虚函数而不调用重新定义的默认参数时会出错。不是使用重新定义的默认参数，而是使用基类的默认参数值。

注意 引用与指针表现出相同的行为。

示例：

enum SeinfeldCharacter {cJERRY, cELAINE, cGEORGE, cKRAMER, cNEWMAN};   
class ClassA   
{ public: virtual void DoFunction(SeinfeldCharacter name = cJERRY);   
}；   
class ClassB : public ClassA   
{ public: void DoFunction(SeinfeldCharacter name = cNEWMAN) override;   
}；   
void main()   
{ ClassA objectOfClassA; // 创建 ClassA 的对象 ClassA\* aClassA_Ptr $=$ &objectOfClassA; // 创建指向基类类型的指针 // 指向基类 ClassB objectOfClassB; // 创建 ClassB 的对象 ClassA\* aClassB_Ptr $=$ &objectOfClassB; // 创建指向基类类型的指针 // 指向派生类 aClassA_Ptr->DoFunction(); // 调用 ClassA::DoFunction(cJERRY)

```cpp
//（不意外）  
aClassB_Ptr->DoFunction(); //调用ClassB::DoFunction(cJERRY) //而不是调用 // ClassB::DoFunction(cNEWMAN)
```

Cl.11 - 不修改成员数据的成员函数应声明为 const。

声明为 const 的成员函数不能修改成员数据，并且是唯一可以在 const 对象上调用的函数。const对象声明是确保对象在不应修改（变异）时不会被修改的极好保障。 ${ \mathsf { C } } { \mathsf { + } } { \mathsf { + } }$ 提供的一个很大优势是可以根据它们的 const 性重载函数。（两个成员函数可以有相同的名称，其中一个是 const，另一个不是）。

Cl.12- 如果一个类定义了析构函数、复制构造函数或复制赋值运算符，则应定义全部 三个。

$ { \mathrm { ~ \textrm ~ { ~ ~ } ~ } } 3 / 5 / 0$ 规则 在 ${ \mathsf { C } } { \mathsf { + } } { \mathsf { + } }$ 中是常见实践，旨在防止由于意外使用默认提供的特殊成员函数而导致的错误。通常，当显式定义这些特殊成员函数之一时，类正在管理自己之外的资源。如果需要为类提供移动语义，则还应定义移动构造函数和移动赋值运算符。

Cl.13- 如果给定类中有指向该类分配的内存的指针，则应定义复制构造函数和赋值运算符。

默认的复制构造函数或赋值运算符会复制类中的所有成员数据，从而复制任何指向动态分配内存等实体的指针。这会导致两个对象指向同一个实体。更糟糕的是，当两个对象之一超出作用域时，其析构函数会删除两个对象指向的实体。

定义复制构造函数和赋值运算符可以解决这些问题。

在这些函数内部，要么复制指向的数据结构，以便每个对象都有自己的副本，要么实现某种引用计数方案来跟踪当前有多少对象指向特定数据结构。

例外 如果确实不打算进行复制/赋值，可以使用规则 Cl.17 中的技术来确保不进行复制/赋值。

Cl.14- 赋值运算符应返回对 *this 的引用。

在赋值链连接在一起的情况下，运算符= 的返回类型必须可以作为自身的输入。这是因为赋值运算符是右结合的，这意味着赋值链是从内向外解析的，每个赋值的返回值用作下一个外部赋值的输入。（见示例。）一个常见的错误是让运算符= 返回 void，这不支持赋值链。

示例：

```txt
//内置类型允许赋值链，如下所示：  
int x;  
int y;  
int z;  
x = y = z = 0;  
//要对用户定义类型执行赋值链，赋值  
//运算符必须支持这一点，如下所示：  
class SomeString{
```

public: SomeString(const char\* aValue $= 0$ ); SomeString& operator $\equiv$ (const SomeString& aRhs) { //... return \*this; //返回对左侧对象的引用 } private: char\* mData; }; SomeString x; SomeString y; SomeString z; $\mathrm{x} = \mathrm{y} = \mathrm{z} = \mathrm{"Hello"}$ //由于赋值运算符的返回值，这可以工作 //注意：以下表达式的形式与上面的表达式相同。 //括号展示了表达式是如何从内向外进行求值的。 $\mathrm{x} = (\mathrm{y} = (\mathrm{z} = "Hello"))$

Cl.15- 赋值运算符应为所有数据成员赋值。

特别注意派生类的赋值运算符：它们还需要处理基类成员的赋值。

Cl.16- 如果一个赋值运算符释放分配给接收对象的先前资源，则不应在对象被赋值给自身时这样做。

当对象被赋值给自身时（例如， $\mathtt { a } = \mathtt { a }$ ），可能会出现问题。（这种赋值通常不会显式出现，而是间接发生。）赋值运算符通常在为对象分配与其新值相关的新资源之前释放分配给对象的资源。在将对象赋值给自身时，这将导致问题，因为在分配新资源的过程中通常需要旧资源。

如果赋值运算符检测到对象被分配给自身，则可以避免此问题。赋值运算符可以有效地跳过大部分代码。

示例：

```cpp
class SomeClass   
{ public: const SomeClass& operator=(const SomeClass& aSc); //... private: char\* mSomeData;   
}；   
//赋值运算符   
const SomeClass& SomeClass::operator=(const SomeClass& aSc)   
{ 
```

```javascript
if(this != &aSc) //这是同一个对象吗？{delete mSomeData; //可以删除数据}return \*this;
```

Cl.17- 在仅为禁用自动生成的编译器函数而声明操作的情况下，定义（主体）应使用delete 关键字。

由于不允许使用这些函数，这允许在编译时检测到这些错误以提高可测试性。

示例：

class SomeClass   
{ public: SomeClass(const SomeClass&) $=$ delete;   
}；

Cl.18 - 在子类中重新定义虚函数时使用 override 关键字。

虽然语言没有要求，但添加关键字作为自文档提醒，表明该函数是对超类虚函数的重写。使用此关键字将生成编译时错误，通知任何函数签名的差异。

Cl.19- 每个类属性在其类构造完成时都应有一个值，无论该值是默认值还是实际工作值。

消费者可能会在该函数的类属性在启动后不久接收到值之前调用供应商的公共成员函数。如果类属性在构造完成之前没有接收到值，则该属性将包含 意外 值。如果 意外 值与默认或实际工作值大相径庭，则启动软件性能可能会降低。

Cl.20(G)- 不应在类中指定公共成员数据。

不鼓励使用公共变量，原因如下：

公共变量代表了违反面向对象编程的基本原则之一，即数据的封装。例如，如果有一个类型为 BankAccount 的类，其中 accountBalance是一个公共变量，任何类的用户都可以更改该变量的值。但是，如果该变量被声明为私有，则其值只能由类的成员函数更改。

程序中的任意函数可以更改公共数据，这可能会导致难以定位的错误。

如果避免公共数据，则可以更改其内部表示，而无需类的用户修改他们的代码。类设计的原则是保持类的公共接口的稳定性。类的实现不应成为其用户关心的问题。

Cl.21(G)- 不应在类中指定受保护的成员数据。

不建议在类中使用受保护的变量，因为其变量会对其派生类可见。然后，基类中的类型或变量的名称可能无法更改，因为派生类可能依赖于它们。如果出于某种原因，派生类必须访问基类中的数据，一种解决方案可能是在基类中创建一个特殊的受保护接口，其中包含返回私有数据的函数。如果可以内联定义这些函数，这种解决方案不会导致性能下降。

Cl.22(G)- 尽可能使用标准库容器或智能指针，以避免手动定义特殊成员函数。

使用经过良好测试的资源管理类型可以消除手动定义析构函数、复制/移动构造函数和复制/移动赋值运算符的需要。手动定义这些函数容易出错。

Cl.23(G)- 对于具体（非抽象）类，如果希望仅将对象的创建限制为派生类，则应声明受保护的构造函数。

在某些情况下，不应从基类构造对象，仅应从派生类构造对象。如果有人试图创建这样一个基类的对象，由于受保护声明的构造函数不可用，尝试调用受保护声明的构造函数将导

致编译时错误。然而，关于派生类，基类的受保护声明的构造函数是可用的。

Cl.24 (G) - 应避免使用 friend 机制。

应提供充分的理由来证明需要使用 friend 机制。

Cl.25(G)- 使用默认成员初始化器，而不是仅初始化数据成员的默认构造函数。

使用默认成员初始化器允许生成编译器生成的函数。

示例：  
class SomeClass1{//坏：不使用成员初始化器 public: SomeClass1():s{"default"},i{1}{} //... protected: string s; int i;   
};   
class SomeClass2 { public: //使用编译器生成的默认构造函数 //... private: string s $=$ "default"; int i $= 1$ .   
};

Cl.26 (G) - 当对象关系是动态的时，使用指针成员变量。

当指针成员变量可以随时间指向许多不同的对象或根本不指向任何对象时，应使用指针成员变量。指针成员变量可以随意更改，并且在当前未包含任何内容时可以设置为 nullptr。

Cl.27(G)- 当对象关系是静态的时，使用引用成员变量。

成员函数（构造函数除外）不能更改引用指向的内容。引用成员变量必须由类的构造函数初始化，并且它们永远不能更改为引用其他任何内容。虽然指针可以用于所有关系，但在可能的情况下使用引用更安全。

例外 当 null 是有效值时，使用常量指针（而不是指向常量的指针）。

▪ Cl.28 (G) - 当不希望自动转换时，构造函数和转换运算符应标记为 explicit。  
Cl.29(G)- 在模板类定义中，应避免多个潜在的重载函数定义。

类模板中的重载函数可能会造成问题。如果函数被重载，则可能会在其中之一显式出现元素类型时发生冲突。实例化后，可能会出现两个函数，例如，具有类型 int 作为参数。编译器可能不会对此提出异议，风险是类设计者没有注意到这一点。在存在多个成员函数定义风险的情况下，必须仔细记录。

示例：  
```txt
template<class class ET> class Conflict {
    public:
        void SomeFunction(int aA); 
```

```javascript
void SomeFunction(ET aA); //如果ET最终变为int会怎样？}；
```

首选的方法是使用模板特化、std::enable_if，或（在 ${ \mathsf { C } } { \mathsf { + } } { \mathsf { + } } 1 7$ 中）使用 if constexpr。

Cl.30 (G) - 将异常类基于标准 ${ \mathsf { C } } { + } { + }$ 类之一。

这使得可以以与系统生成的异常一致的方式处理异常。

如果异常处理的效率不能满足性能要求，则应使用某种替代机制来防止可能导致程序异常终止的项目，例如

const cBAD_DIVISOR = 0.0;   
const cGONSET_DEFAULT = 0.0;   
if (mDeltaGonset != cBAD_DIVISOR)   
{ myGonset $=$ (mDownVelGonset - mDownVelPilot) / mDeltaGonset;   
}   
else   
{ myGonset $=$ cGONSET_DEFAULT;

# 函数

Fn.1 - 声明函数时，如果没有形式参数，应指定空括号，而不是(void)。  
Fn.2- 不应使用未指定的函数参数（省略号表示法）。

不建议使用此类未指定的函数参数，因为这会避免类型检查。考虑使用函数重载。

注意：此规则不禁止使用变长模板或 catch(...)。

Fn.3- 函数的形式参数名称应在函数声明和定义中指定，并且应相同。

形式参数的名称应在函数声明和定义中指定。参数的名称可以阐明参数的使用方式，从而减少在类声明等中添加注释的需要。

例外：当派生类中的虚函数的参数未在函数中使用时，可以省略参数名称。这可以防止某些编译器发出警告消息。

示例：（遵循规则）

```txt
//函数声明  
int SetPoint(int, int); //不正确！  
int SetPoint(int aX, int aY); //正确  
//函数定义  
int SetPoint(int aX, int aY)  
{ //...  
}  
示例：（遵循例外）  
cpp
```

```cpp
class BaseClass   
{ public: virtual void PrintSum(int aA,int aB);   
}；   
void BaseClass::PrintSum(int aA,int aB)   
{ cout<<aA+aB<<endl;   
}；   
class DerivedClass :public BaseClass   
{ public: void PrintSum(int aA,int) override; //第二个形式参数名称   
}； //省略，因为未使用。 //注意形式参数类型仍需   
void DerivedClass::PrintSum(int aA,int) //包含以匹配基类中的原型。   
{ cout<<aA<<endl;   
}；
```

Fn.4 - 仅作为输入的传引用函数参数应在参数列表中声明为 const。

此规则确保调用例程不会修改仅输入参数。

例外：如果输入参数是来自非 const 正确的库的对象的指针或引用，可能无法遵循此规则。

Fn.5- 不应在函数中操作全局数据，而应通过形式函数参数传递数据。

此规则旨在减少程序中全局数据的数量。

Fn.6- 函数不应返回对临时变量的引用或指针。

如果函数返回对临时变量的引用或指针，则在使用此引用或指针时，它所引用的内存将已被释放。编译器可能会或可能不会对此发出警告。临时变量的示例包括局部变量，但不包括静态局部变量。静态局部变量具有永久存储。

示例：

```cpp
class String   
{ public: String(int aN); }； String\* NumToString(int aN) //不正确！返回的指针在函数结束后将 //无意义   
1
```

String converted(aN); return &converted;   
} //在此时，“converted"从栈中移除并调用其析构函数！ int main() { int num $= 2$ · string\*s; $\mathbf{s} =$ NumToString(num);//s指向已释放内存！

Fn.7 - 不应使用预处理器指令#define 替换函数。

示例：

```c
// 使用#define“函数”可能出现的问题示例
#define SQUARE(x) ((x)*(x))
int a = 2;
int b = SQUARE(a++) ; // b = (2 * 3) = 6;
// 内联函数比宏更安全且更易于使用，如果您
// 需要一个由于效率原因而不可接受的普通函数。
// 如果以后需要将其转换为普通函数，也更容易。
inline int Square(int aX)
{
return (aX * aX);
};
int c = 2;
int d = Square(c++); // d = (2 * 2) = 4;
```

Fn.8- 仅打算在单个实现文件中使用的非成员函数应声明为 static或位于未命名的命名空间中。

此规则强制函数“本地”于实现文件（即，不包含在实现文件的对应头文件中）。

示例：

```txt
// myfile.cpp   
static int UtilityFunction()   
{ //...   
}   
//或者   
namespace { int UtilityFunction() { //... 
```

}

Fn.9(G)- 为了性能，函数参数在变量大小明显大于指针时不应按值传递。

为函数输入和输出复制值可能会显著消耗吞吐量。传递引用会导致复制固定大小的变量（指针），而不考虑实际的变量大小。通常，指针需要 8 个字节。建议将大于 16 字节的值通过引用传递。如果值是输入且不应由函数修改，则应通过常量引用传递。

例外：在返回值的情况下，如果供应商返回的是自动变量（即在成员函数中定义的变量）或消费者需要获得自己的副本以应对并发访问问题，则应按值传递返回值。

Fn.10(G)- 尽可能促进返回值优化（RVO）。

返回值优化（RVO）是一种编译器优化，当对象按值返回时，可以避免创建和删除临时对象。当函数被编写为返回构造函数参数而不是对象，并且该函数在允许函数的返回位置被函数调用点的对象替换的上下文中被调用时，就会调用此优化。以下示例展示了编译器如何直接在为对象 c分配的内存中构造定义在运算符*的返回表达式中的对象。

示例：

```c
// 正确实现返回对象的函数的方法  
Rational operator* (Rational& aLhs, Rational& aRhs)  
{ return Rational(aLhs.numerator * aRhs.numerator, aLhs-denominator * aRhs-denominator); }  
// 下面的例子展示了如何调用函数以利用 RVO  
Rational a = (3, 4);  
Rational b = (5, 60);  
Rational c = a * b; // 这也说明了声明的局部性
```

# 变量和常量

Va.1 - 常量应使用 const、constexpr 或 enum 定义，绝不使用预处理器指令 #define。

预处理器在源代码中对宏进行文本替换，然后进行编译。这会带来许多负面影响。例如，如果使用 #define 定义常量，许多调试器无法识别常量的名称。如果常量由表达式表示，则根据名称的作用域，不同实例化可能会对该表达式进行不同的求值。

示例：

```c
//使用宏定义常量  
#define BUFSIZE 7 //无类型检查  
//使用const定义常量  
const int cBUFSIZE = 7; //进行类型检查  
//使用枚举定义常量  
enum SIZE {cBUFSIZE = 7}; //进行类型检查
```

示例：

```c
// 在另一个文件中定义的 const 声明 extern const char cCONSTANTCHAR; extern const string cFILENAME;
```

Va.2- 应避免在代码中使用数值。应使用符号值。

代码中的数值应被视为可疑。如果需要更改值，它们可能会导致难以解决的问题。

一旦定义了常量，应尽可能使用该常量以确保代码更易于维护。例如，用于指定数组大小的相同常量也应用作遍历数组的相关循环中的结束比较器。

例外：某些数值在程序中可能具有明确的意义，例如零。此类值可以直接在代码中使用。

Va.3 - 每个指针或引用类型的变量应在单独的声明语句中声明。

这种做法可以消除由语句引起的错误，例如：char*a,b,c; 实际上只声明了一个指针（可能不是预期的）。此外，它提高了可读性。

Va.4 - 每个声明的变量在使用前都应赋值。  
Va.5- 对于可能由程序外部操作更改的任何变量，应使用 volatile 类型关键字。

这些变量通常指向硬件地址或在多个进程之间共享。这可以防止编译器缓存这些变量的最后已知值或优化掉这些变量。

▪ Va.6- 代码不应假设静态数据成员或全局对象以任何特殊顺序初始化或销毁。

示例：

```txt
// 模块A  
int someParam = 3;  
// 模块B  
int someOtherParam;  
extern int someParam;  
...  
someOtherParam = someParam; // 无法保证 someParam 已在模块 A 中初始化
```

Va.7 - 指针在声明时应始终初始化为有效值或 nullptr。

未初始化的指针可能导致难以追踪的错误，并且在每次执行时可能会发生变化。由于它们可能导致非确定性行为，因此指针必须始终初始化。

Va.8 - 应使用关键字 nullptr 代替 0 和 NULL 来表示空指针值。  
Va.9- 应避免使用 C 风格的数组语义。  
Va.10(G)- 变量应在尽可能低的作用域中声明。

在尽可能低的作用域中声明变量可以降低声明未使用变量的风险。由于变量更接近使用它的代码，因此更容易确定变量的使用情况。

Va.11(G)- 对于具有相关构造函数和析构函数的类，应遵循声明的局部性。

声明的局部性意味着在使用变量的地方附近定义变量。这可以避免不必要的对象构造/销毁。

示例：

```txt
// 使用声明的局部性的高效方法  
int Foo()  
{
```

```c
if (!someValidityCheck)  
{  
    return 0;  
}  
Matrix m1;  
Matrix m2;  
// 好的，在这里使用 m1 和 m2 进行一些工作  
}  
// 低效的方法 - 编译器将在条件检查失败时不必要地调用 m1 和 m2 的构造函数和析构函数  
int Foo()  
{  
    Matrix m1;  
    Matrix m2;  
    if (!someConditionCheck)  
{  
        return 0;  
    }  
// 好的，在这里使用 m1 和 m2 进行一些工作
```

Va.12(G)- 如果可能，应使用初始化而不是赋值。

通常，如果变量未初始化，编译器会发出警告。为了保持一致性，应在构造函数中进行初始化。即使在声明中未提供参数，类的实例通常也会被初始化（调用空构造函数）。要声明在另一个文件中初始化的变量，总是使用关键字 extern。

通过初始化变量而不是在首次使用之前为其赋值，代码变得更高效，因为没有为初始化创建临时对象。对于具有大量数据的对象，这可以显著加快代码速度。

对于具有相关构造函数、复制构造函数、赋值运算符和析构函数的类对象，用其类的另一个对象初始化对象总是比等效赋值更高效。

示例：

// 使用声明的局部性的高效方法

Matrix m1;

Matrix m2;

Matrix composite $= { \mathsf { m } } 1 + { \mathsf { m } } 2$

// 低效的方法 - 生成临时矩阵对象

Matrix m1;

Matrix m2;

Matrix composite;

composite $= { \mathsf { m } } 1 + { \mathsf { m } } 2$ ;

Va.13 (G) - 对于非负整数变量，应使用 unsigned。

无符号整数始终为零或正数。在适用的情况下，使用 unsigned int 而不是 int 向代码的读者传达信息。

Va.14- 对于表示大于 10 的基数的数字的字母字符、用于科学计数法的字符 E 以及字面类型后缀，应使用大写。

这种大写约定被广泛采用并受到偏爱。

# 内存

Me.1 - 不应使用 malloc、realloc 和 free。

在 C 语言中，malloc、realloc 和 free 用于在堆上动态分配内存。这可能导致与 ${ \mathsf { C } } { + } { + }$ 中的 new 和 delete 操作符的使用冲突。

Me.2 - 在释放数组时，应使用空括号（[]）进行 delete。

如果分配了类型为 T 的数组，重要的是以正确的方式调用 delete。仅编写 deletea; 将导致仅为第一个类型为 T 的对象调用析构函数。正确的方法是编写 delete[]a;，因为这样会为分配的数组中的所有对象调用析构函数。

示例：

int n $= 7$ T\*myT_Ptr $\equiv$ new T[n];//T是具有定义的构造函数和析构函数的类型  
//不正确！仅为数组中的第一个对象调用析构函数delete myT_Ptr;  
//正确。为整个数组调用析构函数delete[]myT_Ptr;

Me.3- 分配的内存应被释放。

示例：

string MyFunc(const char* myArgument)  
{ string\* temp $\equiv$ new string(myArgument); return \*temp; // temp 从未被释放，myFunc 的用户无法释放 //因为返回的是该实例的临时副本。

Me.4-Lambda 函数不应通过引用捕获可能超出其生命周期的值。

如果变量在 lambda 持有对其的引用时超出作用域，lambda 可以修改它不应访问的内存。这可能导致难以发现的错误。

Me.5 - 当指针现在指向已释放的内存时，应将指针设置为 nullptr。

指向已释放内存的指针应设置为 nullptr 以防止访问已释放的内存。

Me.6(G)- 优先使用自动存储而不是堆分配。

自动存储使用速度更快，并消除了所有内存泄漏的风险。

Me.7(G)- 使用 RAII 范式管理所有资源，包括但不限于内存、互斥锁和文件句柄。  
Me.8 (G) - 应尽量避免使用 new 和 delete。

# 可移植性

Po.1 - 使用 ${ \mathsf { C } } { \mathsf { + } } { \mathsf { + } }$ 标准库中定义的项目应通过并符合 ISO ${ \mathsf { C } } { + } { + }$ 标准定义的 ${ \mathsf { C } } { + } { + }$ 库头文件。  
遵循 ISO ${ \mathsf { C } } { + } { + }$ 标准使源代码更具可移植性并减少维护。  
Po.2- 当大小至关重要时，应使用预定义数据类型的别名。

当声明用于迭代简单循环的整数时，大小并不重要。然而，当值通过接口传递到另一台计算机时，大小至关重要。

不同的机器和编译器可以以不同的方式实现预定义的数据类型。通过包含标准头文件<cstdint> 并使用其定义的别名，整数大小将在不同机器上保持一致。

Po.3- 代码不应依赖于下溢或上溢以任何特殊方式运行。  
Po.4(G)- 代码不应假设 char 变量是有符号或无符号的。

ISO ${ \mathsf { C } } { \mathsf { + } } { \mathsf { + } }$ 标准提供了三种字符数据类型：char、unsigned char 和 signed char。char 类型是有符号还是无符号，取决于编译器的实现，因此代码不应假设 char 变量是有符号或无符号的。

Po.5 (G) - 代码不应假设指针和整数具有相同的大小。  
Po.6 (G) - 代码不应假设数据类型在内存中的某种表示。  
Po.7(G)- 代码不应对数据成员构造的顺序做出任何假设。

数据成员根据类声明的顺序构造，而不依赖于构造函数初始化列表中的顺序。如果是这样，编译器将需要为每个构造函数存储不同的顺序。最好不要对数据成员构造的顺序做出任何假设。特别是，依赖于其他数据成员值的指针数据成员应初始化为零。

示例：展示依赖于数据成员构造顺序的代码。在此示例中，mGeneralAlignStatusPtr 和mCarrierAlignStatusPtr 依赖于其他数据成员首先被初始化。如果这没有发生，这些指针将包含一些随机初始值：

```cpp
AlignmentFactory::AlignmentFactory (ACAlignmentLogicalINS* aAlignmentLogicalDevice, ACNIDC* aCNIDC_Ptr) // 开始成员初始化 :mAlignmentLogicalDevicePtr(aAlignmentLogicalDevice) ,mCNIDC_Ptr(aCNIDC_Ptr) ,mGeneralAlignStatusPtr(std::make_unique<mAlignmentLogicalDevicePtr>) ,mCarrierAlignStatusPtr(std::make_unique<mCarrierAlignStatus>(mGeneralAlignStatusPtr)) // 结束成员初始化 { } 
```

示例：展示不对数据成员构造顺序做出假设的代码。在这种情况下，依赖于数据成员构造顺序的指针在成员初始化列表中初始化为零，并在构造函数中分配其实际值。这确保指针被分配有效值或零值：

```cpp
AlignmentFactory::AlignmentFactory (ACAlignmentLogicalINS\* aAlignmentLogicalDevice, ACNIDC\* aCNIDC_Ptr)   
//开始成员初始化 :mAlignmentLogicalDevicePtr(aAlignmentLogicalDevice) ,mCNIDC_Ptr(aCNIDC_Ptr)   
//结束成员初始化   
{ 
```

mGeneralAlignStatusPtr   
std::make_unique<GeneralAlignmentStatus>(mAlignmentLogicalDevicePtr); mCarrierAlignStatusPtr $=$ std::make_unique<CarrierAlignStatus>(mGeneralAlignStatusPtr);   
}

Po.8(G)- 指针值不应进行比较，除了测试相等或不等。

应避免对内存分配顺序的假设。

# 类型安全

Ts.1 - 应使用 ${ \mathsf { C } } { + } { + }$ 风格的数据类型转换，而不是“C”风格。

虽然应尽可能避免类型转换，但推荐和不推荐的非指针数据类型转换形式如下所示。推荐的形式利用了语言内置的转换模板函数。 ${ \mathsf { C } } { \mathsf { + } } { \mathsf { + } }$ 标准对这些转换模板有特定规则。对于static_cast、const_cast 和 reinterpret_cast，转换可以在编译时解决，但 dynamic_cast 需要运行时类型识别。因此，违反转换规则可以在编译时标记，或者在运行时通过显式异常处理程序处理 dynamic_cast。不使用内置转换模板可能会或可能不会调用转换模板提供的相同错误检查和异常处理支持。

示例：

```txt
z = static_cast <double>(k); // 推荐的转换形式  
z = double(k); // 不推荐的转换形式  
z = (double)k; // 不推荐的转换形式
```

应注意，类型转换，特别是在整数和浮点类型之间，可能导致运行时系统的函数调用。

Ts.2 - 在类转换时，应使用隐式转换或 static_cast 转换为基类，使用 dynamic_cast 转换为派生类。

例外：当转换为虚基类时，使用 dynamic_cast。

Ts.3 - 模板参数的要求应使用 static_assert 语句检查。

例 如 ， 如 果 T 需 要 有 一 个 默 认 构 造 函 数 ， 指 定static_assert(std::is_default_constructible<T>::value, "Error text.");

注意：SFINAE 模式还可以用于指定专门行为，而不是在某些条件不满足时无法编译。

Ts.4 (G) - 应使用显式数据类型转换而不是隐式转换。

此规则确保代码的读者明确希望进行转换，消除任何可能无意进行转换的疑虑。

例外：派生类到基类的转换可以隐式进行。

示例：

```cpp
double b = 4.51;  
int j = 4;  
double a = 0.0;  
a = b / static_cast<double>(j); // 显式将 int 转换为 double 
```

示例：

int someFunc(int someParam); //... int $\mathrm{a} = 0$ double $b = 0.0$ . $\mathbf{b} = 5.6$

```txt
a = someFunc(static_cast<int>(b)); // 在函数调用中也使用显式转换 // （注意：将浮点数转换为整数 // 隐式调用截断函数；在这种情况下， // 传递给函数的值将等于5）
```

示例：

//另一个应避免的隐式转换示例：  
classA{public:classA(int al);classA operator+(const classA& aRhs);  
}；  
//...  
classA objectA = 10; //一次转换int tempObject $= 3$ classA objectB $=$ objectA + tempObject; //小心：隐式//类型转换//通过ClassA的构造函数//将整数3转换。

Ts.5 (G) - 不应将 const 转换为非 const。

为了返回非 const 临时对象，有时会使用显式类型转换通过 const_cast 将 const 数据转换为非 const。

Ts.6(G)- 不应从“较长”类型转换为“较短”类型。

在缩短浮点类型时，由于丢弃低有效位，可能导致精度不足。

在缩短整数类型时，可能会丢弃高有效位，导致值与原始值相差甚远。一些编译器在缩短整数类型时会发出警告，但其他编译器不会。

如果需要，请使用 ut::safe_cast 对整数类型进行缩小转换。

Ts.7- 在赋值/初始化多态类型时，应谨慎避免对象切片。

因为…

1) 复制构造函数通过引用传递其参数，并且…  
2) 派生类的引用可以隐式转换为基类的引用

将派生类的实例赋值给基类的实例将导致仅复制派生类实例的一部分。这被称为对象切片，应避免。

# 杂项

Mi.1- 在引用全局函数或变量时，应使用作用域运算符 (::)。

使用作用域运算符将立即向读者表明正在引用全局函数或变量。

Mi.2- 在 case 标签下故意省略 break 语句的代码应提供注释说明省略是故意的。

如果 case 标签不包含 break 语句，执行将跨越 case 边界继续。因此，在大多数情况下，case 标签的最后一条语句是 break 语句。然而，在某些情况下，例如一组值都由相同的操作序列处理时，可能会故意省略 break 语句。

示例：

```txt
switch (tag)  
{  
    case A:  
        SomeFunction();  
        // 故意省略 break 语句  
    case B:  
        AnotherFunction();  
        break; // 现在我们离开 switch 语句  
    default:  
        // ...  
    break;  
} // 结束 switch (tag)
```

Mi.3 - switch 语句应始终包含处理意外情况的 default 分支。  
Mi.4 - 不应使用 goto 语句。

goto 打破了控制流，可能导致难以理解的代码。此外，goto 的使用有限制。例如，不允许跳过初始化具有析构函数的局部对象的语句。

例外：对于从其他语言（例如 FORTRAN）转换的代码，可能无法避免使用 goto。

Mi.5- 不应使用逗号运算符。  
Mi.6(G)- 当概念上执行的是算术运算时，不应使用移位操作。

编写预期的内容并允许优化器完成其工作会产生更正确和更易读的代码。

Mi.7(G)- 尽可能使用基于范围的 for 循环。  
Mi.8(G)- 应使用括号来明确表达式中运算符的求值顺序。

示例：

```txt
int i = a >= b && c < d && e + f <= g + h; // 不好!  
int j = (a >= b) && (c < d) && ((e + f) <= (g + h)); // 更好 
```

Mi.9(G)- 在处理浮点或双精度值的有理表达式中，应使用 $< =$ 和 $> =$ 而不是 $= =$ 。在测试值是否相等时应遵循此指南。例外是与 0.0 的比较。  
Mi.10(G)- 在性能重要的情况下，表达式应预先计算。预先计算表达式可以避免冗余计算值，从而减少吞吐量要求。

示例：

void bad()   
{ int $\mathrm{i} = 0$ double $x = 73.0$ for $(\mathrm{i} = 0;\mathrm{i} <   10; + + \mathrm{i})$ { cout $<  <$ sqrt(3.1415\*i)+sqrt(x) $<  <$ endl; }

void good()   
{ int $\mathrm{i} = 0$ double $x = 73.0$ double sqrtOf $=$ sqrt(x); for $(\mathrm{i} = 0;\mathrm{i} <   10; + + \mathrm{i})$ { cout $<  <$ sqrt(3.1415\*i) $^+$ sqrtOf $<  <$ endl; }

Mi.11(G)- 应优先使用标准库函数和类型，而不是内部实现的类似功能。

通过使用标准库中的组件，通常可以避免从头开始设计自己的流 I/O、字符串、容器（包括迭代和常见操作）、国际化、数值数据结构和诊断机制。这些函数已经被大量重用，并且经过了效率设计。

Mi.12(G) - 在有选择的情况下，应该优先使用 switch 语句而不是 if-else 链。

# 1.3.4. 授权、传递与标记指南 Marking Guide

# 目的

本指南描述了如何根据 AFSIM 信息转移协议 (ITA) 或谅解备忘录 (MOU) 的条款和条件，将受控未分类信息 (CUI) 标记为涵盖信息。

与其他受控或机密信息一样，访问 AFSIM 需要授权和合法的政府目的。此外，每个AFSIM 用户都是美国认为有价值或敏感的信息的管理者。

AFSIM 的持续可访问性和安全性取决于社区每个成员了解如何接收、处理、创建和传播 CUI。所有 AFSIM 用户都应熟悉本标记指南以及国防部 CUI 计划发布的官方指导和培训。

# 背景

根据 AFSIMITA 或 MOU 的适用，定义了适当控制和使用 AFSIM 及相关信息的条款和条件。根据这些协议分发、生成或使用的此类信息（源代码、文档或数据产品）需要适当的标记。

适当的标记有助于社区的所有成员在他们自己的系统上保护 CUI，同时积极参与 AFSIM在共享平台上的持续开发和演变。适当的标记还有助于防止有关 AFSIM 适用和不适用用途的混淆。

适用的 AFSIM 用途包括但不限于以下内容：

DoD 组织在支持 DoD 努力中的使用  
DoD 组织在支持适当协议的国际伙伴关系中的使用  
DoD 承包商在 DoD 合同努力中的使用  
DoD 承包商用于内部研究与开发 (IR&D) 的使用  
DoD 承包商在出口许可证涵盖 AFSIM 生成的输出的努力中的使用

不适用的 AFSIM 用途包括但不限于以下内容：

DoD 组织或 DoD 承包商意图将生成数据的重要部分发布给公众  
DoD 组织或 DoD 承包商与无法处理 ITAR 材料的非 DoD 实体（如大学）合作

# 受控未分类信息

受控未分类信息 (CUI) 需要保护，直到根据适用法律、联邦法规和部门政策授权公开发布。CUI 政策（EO 13556、32 CFR 第 2002 部分、DoDI 5200.48、DFARS 252.204-7008 和 DFARS252.204-7012）在整个国防部建立了一个统一的标记系统，取代了各种机构特定或遗留标记，如 FOUO。有关更多信息，请参阅国防部 CUI 计划发布的官方指导和培训。

# CUI 分类

国防部 CUI 计划定义了多个 CUI 分类。其中两个分类适用于 AFSIM。

受控技术信息 (CTI)：受控技术信息 (CTI) 是指具有军事或空间应用的技术信息，其访问、使用、复制、修改、性能、显示、发布、披露或传播受控。受控技术信息应根据国防部指令 $5 2 3 0 . 2 4 ^ { \prime \prime }$ 技术文件的分发声明 标记为分发声明 B 至 F 之一。  
出口控制信息：国防部物品、服务和技术数据的出口控制受国际武器贸易条例 (ITAR)（22 CFR 第 120-130 部分）管辖。特别是 ITAR 的第 121 部分，称为美国军火清单(USML)，列举了需要出口控制的国防部物品、服务和技术数据的特定类别和子类别。

# 政策

以下政策适用于根据 AFSIMITA 或 MOU 的条款分发、生成或使用的所有 CUI。

AFSIM 是受控技术信息：除非国防部控制办公室 (AFRL/RQ) 另有确定，否则 AFSIM 及其输出受控技术信息。

AFSIM 受出口控制：根据 DTSA 审查（2018 年 3 月），AFSIM 是受 USML 第 IX(b)(4)和 IX(b)(5) 类别控制的出口产品。除非 DTSA 另有确定，否则所有 AFSIM 模块和组件也是受出口控制的产品。  
AFSIM 输出也是受出口控制的：根据 DTSA 指导（2018 年 11 月），AFSIM 的所有输出无论输入如何，均受出口控制。通过 AFSIMITA，行业合作伙伴承认他们在美国出口管制法律法规下的责任（包括在某些情况下在发布使用 AFSIM 生成的数据之前获得出口许可证的义务），并同意不以违反适用出口管制法律法规的方式传播任何受出口控制的数据。违反这些出口法律将受到严厉的刑事处罚。

# 公开发布协调

国防部控制办公室 (AFRL/RQ) 和 AFSIM 产品管理团队 (PMT) 均无权批准社区生成的内容公开发布。只有经过授权的国防部 OPSEC 协调流程和官员才能批准与 AFSIM 相关的CUI 公开发布。

国防部组织应通过其本地 OPSEC 协调员启动此活动，并遵守所有组织特定的政策和指南。国防部承包商应通过相关政府项目经理或合同官员启动此活动。

国防部组织和行业合作伙伴可以选择将材料提交给 AFSIM PMT 进行非正式审查（从AFSIM 内容角度）后再通过授权发布流程提交。许多国防部组织要求进行这种非正式审查，以作为公开发布前联合/项目级协调的证据。

注意：除非或直到被授权公开发布，CUI 需要适当的保护。这需要使用批准的传输 CUI材料的方法，如加密邮件或安全文件交换。

afrl.rq.afsim@us.af.mil 支持加密。在发送 CUI 之前交换证书。

使用 DoD SAFE 传输大文件。首先联系接收方以安排递送。

# 强制性 LDCs

AFSIMITA 或 MOU 中的条款和条件禁止 AFSIM 二进制文件和源代码的二次分发（即重新分发）。这些制品应一致使用 LDC/分发声明 F。

AFSIM 二进制文件：通过包和安装程序分发给社区的编译执行文件、库或插件

AFSIM 源代码：包含软件源制品（例如 ${ \mathsf { C } } { + } { + }$ 和 Python）、文档源制品（例如 reStructuredText和 Markdown）以及辅助构建系统制品（例如 CMake 脚本）的分发代码库

<table><tr><td>制品</td><td>强制性 LDCs</td></tr><tr><td>AFSIM 二进制文件</td><td>DIST-F</td></tr><tr><td>AFSIM 源代码</td><td>DIST-F</td></tr></table>

# 推荐 LDCs

虽然 AFSIMITA 或 MOU 禁止 AFSIM 二进制文件和源代码的二次分发，但这些协议应支持通过 AFSIM 生成或使用的制品的协作和交换。此类制品应根据需要一致使用 LDC/分发声明 C 或 D。DoDI 3200.12 (STINFO) 管理此数据，以：

促进企业范围内对 MS&A 问题的协作  
随 DTIC 中保存的官方报告一起提供  
随分析结果和发现一起提供  
加速其他政府资助的工作作为 GFI

<table><tr><td>制品</td><td>推荐 LDCs</td><td>原因</td></tr><tr><td>社区扩展</td><td>DIST-C 或 DIST-D</td><td>关键技术，出口控制</td></tr><tr><td>输入数据</td><td>DIST-C 或 DIST-D</td><td>关键技术，出口控制</td></tr><tr><td>输出数据</td><td>DIST-C 或 DIST-D</td><td>关键技术，出口控制</td></tr><tr><td>生成的用户文档</td><td>DIST-C 或 DIST-D</td><td>关键技术，出口控制</td></tr><tr><td>生成的源文档</td><td>DIST-C 或 DIST-D</td><td>关键技术，出口控制</td></tr></table>

注意：可能会适用其他传播控制；在所有情况下，用户应咨询适用的组织或程序指导。

# 特殊 LDCs

在国防部控制办公室 (AFRL/RQ) 授权 AFSIM 的变体通过适当的国家间协议进行出口的情况下，可能会对单个源或数据模块适用其他传播控制。

<table><tr><td>源/数据模块</td><td>特殊 LDCs</td><td>原因</td></tr><tr><td>不受限制的模块</td><td>仅限 DL</td><td>传播列表控制</td></tr><tr><td>受限制的模块</td><td>仅限美国</td><td>FDO 排除</td></tr></table>

注意：国防部控制办公室 (AFRL/RQ) 与 AFRL 外国披露办公室 (FDO) 协调建立出口变体。受限制的模块不包括在未来的 FDO 考虑中。

# 常见问题

# 在报告中包含 AFSIM 输出

如果我的简报（或报告）包含 AFSIM 输出或结果，我应该使用什么分发声明？

选择最少限制的控制，可促进国防部内部信息的自由流动，同时根据程序指导使用酌情权。请参阅推荐的 LDCs 获取建议。

请记住，AFSIM 的所有输出都受到出口控制，直到通过适当的国防部审查流程降级。还要记住标识所有适用的 CUI 类别和警告。有关更多信息，请参阅 CUI 类别。

# 在报告中包含视频或截图

如果我的报告（或简报）包含来自 AFSIM 应用程序的视频或截图，我应该使用什么分发声明？

视频和截图也被视为 AFSIM 输出。请参阅在报告中包含 AFSIM 输出。

# 在报告中包含源代码片段

如果我的报告（或简报）包含 AFSIM 源代码片段，我应该使用什么分发声明？

包含 AFSIM 代码片段的内容（广义上解释为包括应用程序源代码和输入/脚本文件）应保留代码来源中最严格的传播控制。作为参考，核心框架源代码通常使用最严格的控制（即DIST-F 或仅限 DL），而模型和场景输入/脚本/数据文件使用较少限制的控制（即 DIST-C 或DIST-D）。

请记住，AFSIM 是出口控制的。还要记住保留这些代码来源中所有适用的 CUI 类别和警告。有关更多信息，请参阅 CUI 类别。

# 在报告中包含用户文档的信息

如果我的报告（或简报）包含来自 AFSIM 用户文档的信息，我应该使用什么分发声明？

包含（通过引用或以附录形式复制）来自 AFSIM 用户文档的信息的内容应保留文档来源中最严格的传播控制。作为参考，生成的（例如 HTML 或 PDF）AFSIM 用户文档使用 LDC/分发声明 DIST-C。这允许 AFSIM 文档随 DTIC 中保存的官方报告一起提供。

请记住，AFSIM 是出口控制的。还要记住保留这些代码来源中所有适用的 CUI 类别和警告。有关更多信息，请参阅 CUI 类别。

# 在报告中包含源文档的信息

如果我的报告（或简报）包含来自 AFSIM 源文档的信息，我应该使用什么分发声明？

将包含在生成的源文档（例如带有 UML 图的 Doxygen 输出）中的信息与生成的用户文档以相同方式处理。请记住，源代码和从源代码生成的文档之间的分发声明不同。作为参考，生成的（例如 HTML）源文档使用 LDC/分发声明 DIST-C。这允许架构和设计文档随 DTIC中保存的官方报告一起提供。

请记住，AFSIM 是出口控制的。还要记住保留这些代码来源中所有适用的 CUI 类别和警告。有关更多信息，请参阅 CUI 类别。

# 模板

以下模板遵循本文档中描述的政策。使用这些模板标记适用的工件。

# 文件头模板

# 未分类文件头

每个未分类的源或数据文件都应包含一个 CUI 横幅，参考随附的 README 和 LICENSE 文件以获取详细信息。作者：

应选择格式特定的注释控制字符（例如，#、//、“””）。  
应为限制模块使用扩展的 RELTO横幅。  
应提供版权声明。  
可以在第一块之后添加其他文件特定的元数据。

注意：并非所有数据格式都支持注释，因此作者应使用 README 文件来解决任何歧义。

```txt
//**********  
// CUI[/REL TO USA ONLY]  
//  
// The Advanced Framework for Simulation, Integration, and Modeling (AFSIM)  
//  
// <COPYRIGHT>  
//  
// 文件中的数据的使用、传播或披露受限或限制。有关详细信息，请参阅随附的README和LICENSE。  
//**********  
// [METADATA]  
//**********  
#**********  
# CUI[/REL TO USA ONLY]  
#  
# The Advanced Framework for Simulation, Integration, and Modeling (AFSIM)  
#  
# <COPYRIGHT>  
#  
# 文件中的数据的使用、传播或披露受限或限制。有关详细信息，请参阅随附的README和LICENSE。  
#**********  
# [METADATA]
```

# 分类文件头

为了进行比较，分类的源或数据文件应包括一个分类横幅和一个分类授权块。否则，标题在目的上是一致的。

```txt
//**********  
//**********  
//**********  
//**********  
//**********  
//**********  
//**********  
//**********  
//********** 
```

```txt
//文件中的数据的使用、传播或披露受限或限制。有关详细信息，请参阅随附的README和LICENSE。  
//**********  
// Classified by:  
//First LAST (CTR), ORGANIZATION>  
//Derived from:  
//Source | Multiple Sources>  
//Declassify on:  
//**********  
//[METADATA]  
//**********  
#**********  
#<CLASSIFICATION//REL//TRIGRAPHS>  
#  
# The Advanced Framework for Simulation, Integration, and Modeling (AFSIM)  
#  
#<COPYRIGHT>  
#  
# 文件中的数据的使用、传播或披露受限或限制。有关详细信息，请参阅随附的README和LICENSE。  
#**********  
# Classified by:  
//First LAST (CTR), ORGANIZATION>  
#Derived from:  
//Source | Multiple Sources>  
#Declassify on:  
//YYYYMMDD>  
#*[METADATA] 
```

# README 模板

作者应将源文件和数据文件组织到不同的模块或包中。每个模块或包应在其根目录中包含一个 README 文件。README 执行类似于 CUI 封面页的功能，并传达适用于该模块中所有文件的 CUI 指定标志。以下模板包含许多可能的通知和警告。作者应相应地调整他们的选择。

<table><tr><td>条件</td><td>适用通知或警告</td></tr><tr><td>CUI</td><td>保留处理和销毁通知</td></tr><tr><td>CTI 类别</td><td>选择分发声明 F、D 或 C</td></tr><tr><td>EXPT 类别</td><td>保留警告 - 出口控制</td></tr><tr><td>混合分类</td><td>保留警告 - 受控未分类信息</td></tr><tr><td>受限模块</td><td>移除随附外国披露的通知</td></tr><tr><td>受限模块</td><td>保留扩展的 REL TO 横幅</td></tr></table>

```txt
**CUI[/REL TO USA ONLY]**  
# <MODULE_OR.Package_NAME> 
```

# [ABOUT]

## CUI Designation Indicator

* Controlled by: <DOD_COMPONENT>   
* Controlled by: <CONTROLLING_OFFICE>   
* CUI Categories: <CATEGORIES>   
* LDC/Distribution Statement: <LDC>   
* POC: <CONTACT>

## Notices and Warnings

### DISTRIBUTION STATEMENT F

Further dissemination only as directed by <CONTROLLING_OFFICE> (<YYYYMMDD>) or higher DoD authority.

### DISTRIBUTION STATEMENT D

Distribution authorized to Department of Defense and U.S. DoD contractors only <REASON>; <YYYYMMDD>. Other requests for this information shall be referred to <CONTROLLING_OFFICE>.

### DISTRIBUTION STATEMENT C

Distribution authorized to U.S. Government agencies and their contractors <REASON>; <YYYYMMDD>. Other requests for this information shall be referred to <CONTROLLING_OFFICE>.

### NOTICE TO ACCOMPANY FOREIGN DISCLOSURE

This content is furnished on the condition that it will not be released to another nation without specific authority of the Department of the Air Force of the United States, that it will be used for military purposes only, that individual or corporate rights originating in the information, whether patented or not, will be respected, that the recipient will report promptly to the United States any known or suspected compromise, and that the information will be provided substantially the same degree of security afforded it by the Department of Defense of the United States. Also, regardless of any other markings on the document, it will not be downgraded or declassified without written approval from the originating U.S. agency.

### WARNING - EXPORT CONTROLLED

This content contains technical data whose export is restricted by the Arms Export Control Act (Title 22, U.S.C. Sec 2751 et seq.) or the Export Administration Act of 1979, as amended, Title 50 U.S.C., App. 2401 et seq. Violations of these export laws are subject to severe criminal penalties. Disseminate in accordance with provisions of DoD Directive 5230.25.

```txt
WARNING - CONTROLLED UNCLASSIFIED INFORMATION  
This content is classified at the <CLASSIFICATION> level and may contain elements of controlled unclassified information (CUI), unclassified, or information classified at a lower level than the overall classification displayed. This content shall not be used as a source of derivative classification; refer instead to <SOURCE>. It must be reviewed for both Classified National Security Information (CNSI) and CUI in accordance with DoDI 5230.09 prior to public release.  
HANDLING AND DESTRUCTION NOTICE  
Handle this information in accordance with DoDI 5200.48. Destroy by any approved method that will prevent unauthorized disclosure or reconstruction of this information in accordance with NIST SP 800-88 and 32 C.F.R 2002.14 (Safeguarding Controlled Unclassified Information).  
**CUI/[REL TO USA ONLY]** 
```

# LICENSE 模板

每个模块或包应在其根目录中包含一个 LICENSE 文件。请注意，LICENSE 文件引用了AFSIMMOU 或 ITA 中列举的条款和条件。作者应在 LICENSE 文件中按名称标识模块。

```txt
**CUI**
## License to Accompany <MODULE_OR-PackAGE_NAME>
You may not use this product except in compliance with the terms and conditions of 48 C.F.R. 252.204-7000 (Disclosure of Information), 48 C.F.R. 252.227-7025 (Limitations on the Use or Disclosure of Government-Furnished Information Marked with Restrictive Legends), and the AFSIM Memorandum of Understanding or Information Transfer Agreement as applicable.
This product is provided "as is" without warranties of any kind.
**CUI** 
```

# NO_EXPORT 模板

对于排除在出口变体之外的受限模块，作者应包含一个 NO_EXPORT 保护文件。在与当地外国披露办公室协商后，作者可能出于各种原因决定某个模块或包不适合出口。NO_EXPORT 保护文件不记录该原因；它只是简单地将模块排除在外。

```txt
**CUI//REL TO USA ONLY**  
Exclude this module or package from all export variants.  
**CUI//REL TO USA ONLY** 
```

# 关于版权声明

对于通过 AFSIM ITA 进行的合同活动或行业贡献，作者应使用标准的版权声明。

```txt
// Copyright YYYY-[YYYY] [公司名称]. All rights reserved. 
```

对于通过 AFSIMMOU 进行的政府内部活动或政府（政府文职或军职人员）贡献，作者应使用版权免责声明。

```txt
// This is a US Government Work not subject to copyright protection in the US. 
```

# 关于元数据字段

# 修改者字段

在一个公司或组织制作原始作品而另一个公司或组织修改该作品（用于维护或增强）的情况下，作者应使用可选的“Modifiedby”元数据字段来跟踪此历史。版本控制系统维护技术变更日志，而 Modifiedby 字段则为次要贡献者提供归属并跟踪原始版权作品的历史。

```txt
**********  
#  
# CUI  
#  
# The Advanced Framework for Simulation, Integration, and Modeling (AFSIM)  
#  
# Copyright YYYYY The First Company. All rights reserved.  
#  
# The use, dissemination or disclosure of data in this file is subject to  
# limitation or restriction. See accompanying README and LICENSE for details.  
#**********  
# Modified by:  
# YYMM A Second Company: Fix bugs in track processor  
# YYMM Some Organization: Add output reporting features 
```

# 实例

以下实例说明了如何将 CUI 标记指南应用于特定信息类型。

# 一个不受限制的源模块

以下示例是大多数框架级源模块的典型示例。受控技术信息 (CTI) 和出口控制 (EXPT)类别均适用。该模块未被排除在出口变体之外，但仍受 AFSIMMOU 或 ITA 管辖，因此适用严格的传播控制。

# 模块组织

```txt
wsf_core_module/  
├doc/  
├core_module.rst  
├grammar/  
├source/  
├core_module.hpp  
├core_module.cpp 
```

├── test/   
├── wsf_module   
├── README.md   
└── LICENSE.md

core_module.cpp   
```txt
//   
// CUI   
//   
// The Advanced Framework for Simulation, Integration, and Modeling (AFSIM)   
//   
// Copyright 2021 Eregion Forge. All rights reserved.   
//   
// The use, dissemination or disclosure of data in this file is subject to   
// limitation or restriction. See accompanying README and LICENSE for details. 
```

core_module.rst   
README   
```txt
**********  
CUI  
The Advanced Framework for Simulation, Integration, and Modeling (AFSIM)  
Copyright 2021 Eregion Forge. All rights reserved.  
The use, dissemination or disclosure of data in this file is subject to limitation or restriction. See accompanying README and LICENSE for details. 
```

```txt
\*\*CUI\*\*   
# wsf_core_module   
\* This module is part of the World Simulation Framework (WSF).   
\* Export variants of AFSIM may include it.   
## CUI Designation Indicator   
\* Controlled by: Air Force Research Laboratory   
\* Controlled by: Aerospace Systems Directorate   
\* CUI Categories: CTI, EXPT   
\* LDC/Distribution Statement: DIST-F   
\* POC: afrl.rq.afsim@us.af.mil   
## Notices andWarnings 
```

### DISTRIBUTION STATEMENT F

Further dissemination only as directed by AFRL Aerospace Systems Directorate (20211209) or higher DoD authority.

### NOTICE TO ACCOMPANY FOREIGN DISCLOSURE

This content is furnished on the condition that it will not be released to another nation without specific authority of the Department of the Air Force of the United States, that it will be used for military purposes only, that individual or corporate rights originating in the information, whether patented or not, will be respected, that the recipient will report promptly to the United States any known or suspected compromise, and that the information will be provided substantially the same degree of security afforded it by the Department of Defense of the United States. Also, regardless of any other markings on the document, it will not be downgraded or declassified without written approval from the originating U.S. agency.

### WARNING - EXPORT CONTROLLED

This content contains technical data whose export is restricted by the Arms Export Control Act (Title 22, U.S.C. Sec 2751 et seq.) or the Export Administration Act of 1979, as amended, Title 50 U.S.C., App. 2401 et seq. Violations of these export laws are subject to severe criminal penalties. Disseminate in accordance with provisions of DoD Directive 5230.25.

### HANDLING AND DESTRUCTION NOTICE

Handle this information in accordance with DoDI 5200.48. Destroy by any approved method that will prevent unauthorized disclosure or reconstruction of this information in accordance with NIST SP 800-88 and 32 C.F.R 2002.14 (Safeguarding Controlled Unclassified Information).

**CUI**

LICENSE

**CUI**

## License to Accompany wsf_core_module

You may not use this product except in compliance with the terms and conditions of 48 C.F.R. 252.204-7000 (Disclosure of Information), 48 C.F.R. 252.227-7025 (Limitations on the Use or Disclosure of Government-Furnished Information Marked with Restrictive Legends), and the AFSIM Memorandum of Understanding or Information Transfer Agreement as applicable.

This product is provided "as is" without warranties of any kind.

**CUI**

# 一个受限的源模块

以下示例适用于几个框架级源模块。受控技术信息 (CTI) 和出口控制 (EXPT) 类别均适用。与前一个示例不同，此模块被排除在出口变体之外。因此，保留了 RELTO 横幅，删除了随附外国披露的通知，并在根文件夹中添加了 NO_EXPORT 保护文件。

模块组织  
```txt
wsf_mil_module/  
doc/  
| mil_module.rst  
| grammar/  
| source/  
| mil_module.hpp  
| mil_module.cpp  
| test/  
| wsf_module  
| NOExport  
| README.md  
| LICENSE.md 
```

mil_module.cpp   
```txt
//**********  
// CUI//REL TO USA ONLY  
//  
// The Advanced Framework for Simulation, Integration, and Modeling (AFSIM)  
//  
// Copyright 2021 Eregion Forge. All rights reserved.  
//  
// The use, dissemination or disclosure of data in this file is subject to  
// limitation or restriction. See accompanying README and LICENSE for details.  
//**********  
mil_module rst  
...  
CUI//REL TO USA ONLY  
..  
The Advanced Framework for Simulation, Integration, and Modeling (AFSIM)  
..  
Copyright 2021 Eregion Forge. All rights reserved.  
..  
The use, dissemination or disclosure of data in this file is subject to  
.. limitation or restriction. See accompanying README and LICENSE for details. 
```

README   
```txt
**CUI//REL TO USA ONLY** 
```

# wsf_mil_module

* This module is part of the World Simulation Framework (WSF).   
* Export variants of AFSIM must exclude it.

## CUI Designation Indicator

* Controlled by: Air Force Research Laboratory   
* Controlled by: Aerospace Systems Directorate   
* CUI Categories: CTI, EXPT   
* LDC/Distribution Statement: DIST-F, REL TO USA ONLY   
* POC: afrl.rq.afsim@us.af.mil

## Notices and Warnings

### DISTRIBUTION STATEMENT F

Further dissemination only as directed by AFRL Aerospace Systems Directorate (20211209) or higher DoD authority.

### WARNING - EXPORT CONTROLLED

This content contains technical data whose export is restricted by the Arms Export Control Act (Title 22, U.S.C. Sec 2751 et seq.) or the Export Administration Act of 1979, as amended, Title 50 U.S.C., App. 2401 et seq. Violations of these export laws are subject to severe criminal penalties. Disseminate in accordance with provisions of DoD Directive 5230.25.

### HANDLING AND DESTRUCTION NOTICE

Handle this information in accordance with DoDI 5200.48. Destroy by any approved method that will prevent unauthorized disclosure or reconstruction of this information in accordance with NIST SP 800-88 and 32 C.F.R 2002.14 (Safeguarding Controlled Unclassified Information).

**CUI//REL TO USA ONLY**

LICENSE

**CUI**

## License to Accompany wsf_mil_module

You may not use this product except in compliance with the terms and conditions of 48 C.F.R. 252.204-7000 (Disclosure of Information), 48 C.F.R. 252.227-7025 (Limitations on the Use or Disclosure of Government-Furnished Information Marked with Restrictive Legends), and the AFSIM Memorandum of Understanding Information Transfer Agreement as applicable.

This product is provided "as is" without warranties of any kind.

# 一个不受限制的社区源模块

以下示例是社区开发的源模块（例如，共享插件或扩展）的典型示例。受控技术信息 (CTI)和出口控制 (EXPT) 类别均适用。该模块未被排除在出口变体之外，并且分发不受 AFSIMMOU 或 ITA 条款和条件的限制。

模块组织  
```txt
wsf_shared_module/  
doc/  
shared_module.rst  
grammar/  
source/  
sharedModule.hpp  
sharedModule.cpp  
test/  
wsf_module  
README.md  
LICENSE.md 
```

shared_module.cpp   
README   
```txt
//**********  
// CUI  
//  
// The Advanced Framework for Simulation, Integration, and Modeling (AFSIM)  
//  
// Copyright 2021 Shire Works. All rights reserved.  
//  
// The use, dissemination or disclosure of data in this file is subject to  
// limitation or restriction. See accompanying README and LICENSE for details.  
//**********  
shared_module rst  
...  
... CUI  
...  
... The Advanced Framework for Simulation, Integration, and Modeling (AFSIM)  
...  
... Copyright 2021 Shire Works. All rights reserved.  
...  
... The use, dissemination or disclosure of data in this file is subject to  
... limitation or restriction. See accompanying README and LICENSE for details. 
```

**CUI**

# wsf_shared_module

* This module is shared with others in the AFSIM community.   
* Some Other Government Agency manages or maintains it.   
* Export variants of AFSIM may include it.

## CUI Designation Indicator

* Controlled by: Some Other Government Agency   
* Controlled by: Some Other Directorate   
* CUI Categories: CTI, EXPT   
* LDC/Distribution Statement: DIST-C   
* POC: some.organization@mail.mil

## Notices and Warnings

### DISTRIBUTION STATEMENT C

Distribution authorized to US Government agencies and their contractors; Critical Technology, Export Controlled; 20211209. Other requests for this information shall be referred to Some Other Government Agency, 123 A Street, Somewhere, USA 12345.

### NOTICE TO ACCOMPANY FOREIGN DISCLOSURE

This content is furnished on the condition that it will not be released to another nation without specific authority of the Department of the Air Force of the United States, that it will be used for military purposes only, that individual or corporate rights originating in the information, whether patented or not, will be respected, that the recipient will report promptly to the United States any known or suspected compromise, and that the information will be provided substantially the same degree of security afforded it by the Department of Defense of the United States. Also, regardless of any other markings on the document, it will not be downgraded or declassified without written approval from the originating U.S. agency.

### WARNING - EXPORT CONTROLLED

This content contains technical data whose export is restricted by the Arms Export Control Act (Title 22, U.S.C. Sec 2751 et seq.) or the Export Administration Act of 1979, as amended, Title 50 U.S.C., App. 2401 et seq. Violations of these export laws are subject to severe criminal penalties. Disseminate in accordance with provisions of DoD Directive 5230.25.

### HANDLING AND DESTRUCTION NOTICE

Handle this information in accordance with DoDI 5200.48. Destroy by any

```txt
approved method that will prevent unauthorized disclosure or reconstruction of   
this information in accordance with NIST SP 800-88 and 32 C.F.R 2002.14   
(Safeguarding Controlled Unclassified Information).   
\*\*CUI\*\*   
LICENSE   
\*\*CUI\*\*   
## License to Accompany wsf_shared_module   
You may not use this product except in compliance with the terms and conditions   
of 48 C.F.R. 252.204-7000 (Disclosure of Information), 48 C.F.R. 252.227-7025   
(Limitations on the Use or Disclosure of Government-Furnished Information   
Marked with Restrictive Legends), and the AFSIM Memorandum of Understanding or   
Information Transfer Agreement as applicable..   
This product is provided "as is" without warranties of any kind.   
\*\*CUI\*\* 
```

# 一个不受限制的数据包

以下示例是 AFSIM 分发中包含的数据包（例如，盒装场景、模型和演示）的典型示例。受控技术信息 (CTI) 和出口控制 (EXPT) 类别均适用。该包未被排除在出口变体之外，并且分发不受 AFSIMMOU 或 ITA 条款和条件的限制。此包使用可选的元数据块来传达模型特定的谱系和验证与确认 (V&V) 信息。

包组织

```txt
afsimscenario/   
doc/ scenario.rst   
platforms/   
processors/ weapon Processor.txt trackprocessor.txt   
sensors/   
output/   
scenario.txt   
README.md   
LICENSE.md 
```

```txt
weapon Processor.txt   
#   
# CUI   
#   
# The Advanced Framework for Simulation, Integration, and Modeling (AFSIM) 
```

```txt
#   
# Copyright 2021 Eregion Forge. All rights reserved.   
#   
# The use, dissemination or disclosure of data in this file is subject to   
# limitation or restriction. See accompanying README and LICENSE for details.   
#   
# Description:   
# [DESCRIPTION]   
# Sources:   
# [SOURCES]   
# Limitations:   
# [LIMITATIONS]   
# Keywords:   
# [COMMA_SEPARATED_LIST_OF_KEYWORDS]   
# Pedigree:   
# AFSIM Versions: [AFSIM Versions]   
# File Version: [FILE_VERSION]   
# Change Log:   
[FILE_VERSION] [CHANGE_DESWPTION]   
# Dependencies:   
[DEPENDENCIES]   
# V&V:   
[VERIFICATION_ANDValidation] 
```

```txt
scenario.rst   
Cui   
The Advanced Framework for Simulation, Integration, and Modeling (AFSIM)   
Copyright 2021 Shire Works. All rights reserved..   
The use, dissemination or disclosure of data in this file is subject to   
limitation or restriction. See accompanying README and LICENSE for details. 
```

```txt
README  
**CUI**  
# afsimscenario  
* This scenario demonstrates the use of AFSIM processors.  
* Export variants of AFSIM may include it.  
## CUI Designation Indicator 
```

* Controlled by: Air Force Research Laboratory   
* Controlled by: Aerospace Systems Directorate   
* CUI Categories: CTI, EXPT   
* LDC/Distribution Statement: DIST-C   
* POC: afrl.rq.afsim@us.af.mil

## Notices and Warnings

# ### DISTRIBUTION STATEMENT C

Distribution authorized to US Government agencies and their contractors; Critical Technology, Export Controlled; 20211209. Other requests for this information shall be referred to AFRL Aerospace Systems Directorate, afrl.rq.afsim@us.af.mil.

# ### NOTICE TO ACCOMPANY FOREIGN DISCLOSURE

This content is furnished on the condition that it will not be released to another nation without specific authority of the Department of the Air Force of the United States, that it will be used for military purposes only, that individual or corporate rights originating in the information, whether patented or not, will be respected, that the recipient will report promptly to the United States any known or suspected compromise, and that the information will be provided substantially the same degree of security afforded it by the Department of Defense of the United States. Also, regardless of any other markings on the document, it will not be downgraded or declassified without written approval from the originating U.S. agency.

# ### WARNING - EXPORT CONTROLLED

This content contains technical data whose export is restricted by the Arms Export Control Act (Title 22, U.S.C. Sec 2751 et seq.) or the Export Administration Act of 1979, as amended, Title 50 U.S.C., App. 2401 et seq. Violations of these export laws are subject to severe criminal penalties. Disseminate in accordance with provisions of DoD Directive 5230.25.

# ### HANDLING AND DESTRUCTION NOTICE

Handle this information in accordance with DoDI 5200.48. Destroy by any approved method that will prevent unauthorized disclosure or reconstruction of this information in accordance with NIST SP 800-88 and 32 C.F.R 2002.14 (Safeguarding Controlled Unclassified Information).

**CUI**

LICENSE

**CUI**

## License to Accompany afsim_scenario

```txt
You may not use this product except in compliance with the terms and conditions of 48 C.F.R. 252.204-7000 (Disclosure of Information), 48 C.F.R. 252.227-7025 (Limitations on the Use or Disclosure of Government-Furnished Information Marked with Restrictive Legends), and the AFSIM Memorandum of Understanding or Information Transfer Agreement as applicable. This product is provided "as is" without warranties of any kind. **CUI** 
```

# 一个受限的混合数据包

当数据包混合了机密信息和受控未分类信息 (CUI) 时，必须保留 CUI 标记。以下示例适用于包含在机密 AFSIM 分发中的一些数据包（例如，盒装场景、模型和演示）。受控技术信息 (CTI) 和出口控制 (EXPT) 类别均适用。与前一个示例不同，此模块被排除在出口变体之外。因此，保留了 RELTO 横幅，删除了随附外国披露的通知，并在根文件夹中添加了NO_EXPORT 保护文件。

# 包组织

```txt
afsimscenario_snf/   
doc/   
| scenario_u.rst   
| platforms/   
| processors/   
| weapon Processor_u.txt   
| track Processor_u.txt   
| track Processor_snf.txt   
sensors/   
output/   
| scenario_snf.txt   
NOExport   
README.md   
LICENSE.md 
```

```txt
track Processor u.txt   
#**********   
# CUI//REL TO USA ONLY   
#   
# The Advanced Framework for Simulation, Integration, and Modeling (AFSIM)   
#   
# Copyright 2021 Eregion Forge. All rights reserved.   
#   
# The use, dissemination or disclosure of data in this file is subject to   
# limitation or restriction. See accompanying README and LICENSE for details. 
```

```txt
Description:   
# [DESCRIPTION]   
# Sources:   
# [SOURCES]   
# Limitations:   
# [LIMITATIONS]   
# Keywords:   
# [COMMA_SEPARATED_LIST_OF_KEYWORDS]   
# Pedigree:   
# AFSIM Versions: [AFSIM Versions]   
# File Version: [FILE_VERSION]   
# Change Log:   
# [[FILE_VERSION] [CHANGE_DESCRIPTION]]   
# Dependencies:   
# [DEPENDENCIES]   
# V&V:   
# [VERIFICATION_ANDValidation]   
#**********   
track Processor_snf.txt   
NOTE: This example is contrived and the following markings are for instructional purposes only. 
```

```python
**********  
# SECRET//NOFORN  
#  
# The Advanced Framework for Simulation, Integration, and Modeling (AFSIM)  
#  
# Copyright 2021 Eregion Forge. All rights reserved.  
#  
# The use, dissemination or disclosure of data in this file is subject to  
# limitation or restriction. See accompanying README and LICENSE for details.  
#**********  
# Classified by: An. Analyst (Ctr)  
# Derived from: Multiple Sources  
# Declassify on: 20461209  
#**********  
# Description:  
# [DESCRIPTION]  
# Sources:  
# [SOURCES]  
# Limitations:  
# [LIMITATIONS]  
# Keywords:  
# [COMMA_SEPARATED_LIST_OF_KEYWORDS]  
# Pedigree: 
```

```txt
AFSIM Versions: [AFSIM Versions]  
# File Version: [FILE_VERSION]  
# Change Log:  
# [[FILE_VERSION] [CHANGE_DESCRIPTION]]  
# Dependencies:  
# [DEPENDENCIES]  
# V&V:  
# [VERIFICATION_ANDValidation] 
```

README

NOTE: This example is contrived and the following markings are for instructional purposes only.

**SECRET//NOFORN**

# (U) afsim_scenario_snf

* (U) This scenario demonstrates the use of AFSIM processors.   
* (U) This scenario includes both classified and unclassified input files.   
* (SNF) The README file itself may include classified content.

## CUI Designation Indicator

* Controlled by: Air Force Research Laboratory   
* Controlled by: Aerospace Systems Directorate   
* CUI Categories: CTI, EXPT   
* LDC/Distribution Statement: DIST-D, REL TO USA ONLY   
* POC: afrl.rq.afsim@us.af.mil

## Notices and Warnings

## DISTRIBUTION STATEMENT D

Distribution authorized to Department of Defense and U.S. DoD contractors only Critical Technology, Export Controlled; 20211209. Other requests for this document shall be referred to AFRL Aerospace Systems Directorate, afrl.rq.afsim@us.af.mil.

### WARNING - EXPORT CONTROLLED

This content contains technical data whose export is restricted by the Arms Export Control Act (Title 22, U.S.C. Sec 2751 et seq.) or the Export Administration Act of 1979, as amended, Title 50 U.S.C., App. 2401 et seq. Violations of these export laws are subject to severe criminal penalties. Disseminate in accordance with provisions of DoD Directive 5230.25.

### WARNING - CONTROLLED UNCLASSIFIED INFORMATION This content is classified at the SECRET//NOFORN level and may contain elements

```txt
of controlled unclassified information (CUI), unclassified, or information classified at a lower level than the overall classification displayed. This content shall not be used as a source of derivative classification; refer instead to <SOURCE>. It must be reviewed for both Classified National Security Information (CNSI) and CUI in accordance with DoDI 5230.09 prior to public release. 
```

```txt
HANDLING AND DESTRUCTION NOTICE 
```

```txt
Handle this information in accordance with DoDI 5200.48. Destroy by any approved method that will prevent unauthorized disclosure or reconstruction of this information in accordance with NIST SP 800-88 and 32 C.F.R 2002.14 (Safeguarding Controlled Unclassified Information). 
```

```txt
**SECRET//NOFORN** 
```

```txt
LICENSE 
```

```txt
**CUI** 
```

```markdown
## License to Accompany afsimscenario_snf 
```

```txt
You may not use this product except in compliance with the terms and conditions of 48 C.F.R. 252.204-7000 (Disclosure of Information), 48 C.F.R. 252.227-7025 
```

```txt
(Limitations on the Use or Disclosure of Government-Furnished Information 
```

```txt
Marked with Restrictive Legends), and the AFSIM Memorandum of Understanding or Information Transfer Agreement as applicable. 
```

```txt
This product is provided "as is" without warranties of any kind. 
```

```txt
**CUI** 
```

# 1.3.5. 集成指南 Integration Guide

# 介绍

本文档描述了将新功能扩展和集成到 AFSIM 中的有限方法。允许并描述了多种方法，以及允许将集成引入到符合 AFSIM 社区标准和指南的可共享资源中的要求。

# 概述

# 核心可执行文件

基于 AFSIM 的可执行文件通常由单个 AFSIM 应用程序 组成。此应用程序维护脚本类型、扩展和插件管理器以及应用程序配置数据。应用程序由一个或多个场景组成，这些场景拥有类型工厂和列表、用户输入和脚本。根据应用程序的不同，场景由一个或多个模拟组成。模拟包含类型实例、接口（例如，DIS、XIO、观察者、地形）和运行时数据，包括事件管理和线程处理。

![](images/62ca655934469194f15a52dd84003a912ea8df3ec0a4a561857d6d5f5599472e.jpg)

# 核心架构

AFSIM 的面向对象的 ${ \mathsf { C } } { \mathsf { + } } { \mathsf { + } }$ 架构提供了一个可扩展和模块化的架构，允许轻松集成许多附加功能。AFSIM 允许插入和使用新的组件模型（例如，传感器、通信、移动设备等），以及全新的组件类型。扩展和插件是扩展框架以集成新平台组件模型、新增和扩展平台功能以及新增和扩展模拟服务的主要机制。插件功能是一种扩展形式，允许在不重新编译核心AFSIM 代码的情况下添加功能。使用插件可以更轻松地分发扩展功能，并提供选择在特定分析中使用哪些扩展功能的能力。下图显示了 AFSIM 提供的主要框架组件和服务，并且可以进行扩展。

![](images/cd054c1153cba645cdeb499f8205ce5a23700b31f46d50de4775017fdc399bc6.jpg)

注意：AFSIM 发布中提供了 Doxygen 软件文档，开发人员可以通过 Doxygen 指令进行构建。