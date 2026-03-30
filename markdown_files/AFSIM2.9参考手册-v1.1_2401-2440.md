# 命名规则

![](images/52ff8e03cb1b557aa8954b7b5919c5a4b066b25d776fc8e2db97e10b647238f2.jpg)

- 可以在其他地方引用的语法语法

```typescript
rule time-unit {
    seconds | second | secs | sec | s | minutes | minute | mins | min | m | hours | hour
    | hrs | hr | h | milliseconds | millisecond | msec | msec | ms | microseconds | microsecond
    | usesc | usec | us | nanoseconds | nanosecond | nsecs | nsec | ns
    | days | day 
```

这样使用:

(value Time { <real> <time-unit> }

- 代表可选项
- 结合语法和数据结构的定义。

```txt
(Struct Processor
    :base_type PlatformPart
        (var Time updateInterval)
{
    update_interval <Time> [updateInterval=$$
    | <PlatformPart>
} 
```

- 继承自 PlatformPart   
- 定义变量 updaterInterval。

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

6

![](images/f750d8c41085ebbef8828f61bc62c03a62235aeb503c152d87caf46553ca6e80.jpg)

UNCLASSIFIED

Actions

![](images/0a5d5f8b23e6fd2f11e0128164587e96fa37ed5399ddae8ce1248bc5fa4b4fff.jpg)

- 变量可以在匹配规则时赋值

```ocaml
(Struct Processor
    :base_type PlatformPart
        (var Time updateInterval)
{
    update_interval <Time> [updateInterval=$$
    | <PlatformPart>
}) 
```

- [...] 表示要执行的操作动作。这些动作不会影响语法本身

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

- 结构规则通常调用基本规则。

```txt
struct Processor
    :base_type PlatformPart
        (var Time updateInterval)
{
    update_interval <Time> [updateInterval=$$
    | <PlatformPart>
} 
```

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

8

![](images/5c955e13541ef1663fae3c771603e6dbe0f73766cf72e9beaf3560c08c6bcce5.jpg)

UNCLASSIFIED

Structs…

![](images/2c3c3eda74d36afc5a227c1b8f8a5c2a68c7590efb76bbcfabc95250e2c05138.jpg)

- 可以指定默认值。  
• < $\mathbf{\Phi}$ yaw> 将被读取为角度并存储在变量yaw中。

```txt
(var Length3 location :default "0 0 0 m")  
(var Angle yaw :default "0.0 deg")  
(var Angle pitch :default "0.0 deg")  
(var Angle roll :default "0.0 deg")  
{  
    location <$location>  
    | yaw <$yaw>  
    | pitch <$pitch>  
    | roll <$roll> 
```

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

- 存在一些特殊规则，以便为 Wizard 提供更多信息。  
• (name ...) 将读取一个单词并将其与某个内容关联。

```txt
| ignore (name category)
| ignore_side (name side) 
```

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

10

![](images/c3445f5e9e3f4d863e08616051d1b6ee1cf054f0bae9b8fe4ed6270b8d525871.jpg)

UNCLASSIFIED

# 特殊规则

![](images/4691c476db4ffaac46eaf3cdb05f7194407b22b3425b791ce3d5dbfc61b98916.jpg)

• (typeref ...) 读取一个单词，并提示它应该是对其他地方定义的某个内容的引用。.

```txt
rule platform-availability-command {
    name (typeref platform) availability <real>
    | type (typeref platformType) availability <real>
    | category (name category) availability <real>
    | default availability <real>
    | exclusion-zone (typeref zone)
    | inclusion-zone (typeref zone)
} 
```

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

- (nocase ...) 使内容不区分大小写。

```txt
(value Bool # <Bool.yes_no> is matched with this: (rule yes_no { yes | no }) # <Bool.on_off> is matched with this: (rule on_off { on | off }) # <Bool> is matched with this: { (nocase { true | yes | on | enable | enabled | false | no | off } ) } 
```

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

12

![](images/8d26df2696ce03c63e9b9799e43f00aafabbe1a75ad9ff63fec14090fc046fdc.jpg)

UNCLASSIFIED

# 嵌套规则…

![](images/740d8b0790dd0a39a7a3f751c60d2a73c6bad80accbb4ba417c88c09e94c2658.jpg)

# - 规则可以嵌套

```txt
(value Bool
# <Bool.yes_no> is matched with this:
rule yes_no { yes | no }
# <Bool.on_off> is matched with this:
(rule on_off { on | off } )
# <Bool> is matched with this:
{ nocase {
true | yes | on | enable | enabled | false | no | off
} } 
```

# 像这样使用:

name <string> afterburner | <Bool.on_off> <signature-type> <string>

Zero to Many \*   
- One to Many $^{\prime} + ^{\prime \prime}$   
Zero or One ?

```c
rule dis-interface-block {
dis_INTERFACE <dis-interface-command> * end_dis-interface } 
```

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

14

![](images/c293ecb6b99a99a48d072de5881c3ed71ceb7fc7ebe243e4dc5ae5a96d77a87f.jpg)

# 更多特殊规则

![](images/f917dcb45847b850d81537ba381c3b6841cb33e512103ad0da8d87a3c87e3ce8.jpg)

- 要理解 AFSIM 文件, 需要一个符号表:

sensor MY_TYPE1 MY_TYPE2

one_m2detect_range ...

end SENSOR

- (load ...) - 查找一个符号  
- (new ...) - 创建一个新符号  
- (new_replace ...) - 覆盖一个符号  
- (delete ...) - 删除一个符号

- (file-reference ...)   
- (output-file-reference ...)   
- (error ...)   
- <ScriptBlock>   
- <ScriptVariables>   
- <ScriptFunctionBlock>   
• <TypeCommand>

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

16

# 6.2.1.13.CMAKE 结合 12_CMake_Integration

本文为afsim2.9_src\training\developer\core\slides\

12_CMake_Integration.pptx 的翻译，主要是介绍 AFSIM 和 CMAKE 的相关结合。

UNCLASSIFIED

![](images/5e332ebc684fa91647b595d9bb878e9723cfe83c04fce4b4d17f095fc1448005.jpg)

![](images/24e79647d3f39b051e678c439a6e5238fd326d2d6ddcd262056b4e59f2546241.jpg)

![](images/a2b8f9c3a9ccf153b5d35d85e20d65a2b09aa324fb831690c41c2e763a79048a.jpg)

AFSIM开发培训

12 - 使用CMAKE构建

AFSIM

本文档由杨石兴翻译，该资料做为《AFSIM2.9参考手册》的一部分。没有《AFSIM2.9参考手册》的加杨石兴微信领取：13324598743

integrity $\star$ Service $\star$ Excellence

AFRL/RQQD

美国空军研究实验室

- AFSIM 现在使用 CMake 进行构建配置。本演示文稿描述了在 AFSIM 中使用 CMake 的最佳实践。  
- 可以从
http://www.cmake.org在线获取 CMake。  
- CMake 提供了一个名为 cmake-gui 的工具，如右图所示。该工具使自定义 AFSIM 构建变得更加容易。

(Note: This presentation is largely adapted from the AFSIM documentation page entitled "Building_WSF_with_Cmake")

![](images/6b3eabe786b47f6fb065fdef8e5a779ec55cebf89d648e9747e7916e55e51b3e.jpg)

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQQD.

2

![](images/995bfd91f9ef73216050718fb59d4a5736bed65f01c932cdc54a527d0ddc2fac.jpg)

# UNCLASSIFIED

# 代码外构建

![](images/5d645c8483aff1fcee1a8af06439a20c7e1fb3705727c37f375b3ffce9ba3b43.jpg)

![](images/be99843a241bc28a014fa3713050a949599bcb56da7120cc77016ced45b8b0bc.jpg)

- 有时在构建过程中会出现问题。  
- 这种布局允许我们安全地销毁构建目录，而不会丢失数据。

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQDD.

- 以下变量非常重要：

BUILD_WITH...

- 每个可选项目都可以通过切换相关复选框来启用或禁用。默认值由 swdev 目录中该模块的可用性决定。

- WSF_PLUGIN Builds

- 构建共享对象或 DLL 库，而不是静态库，并启用加载 WSF 插件的功能。

- WsF_BUILD_TYPE_secret

- 此构建面向DOD（国防部）目标。如果未选中此框，DOD的可选项目将不会包含在构建中。

- WSFINSTALL_DATA

与应用程序一起安装WSF数据文件。这些数据文件必须被检出。

- WSFINSTALL_SOURCE

- 在安装文件夹中创建一个包含源代码的 swdev 目录。

- CMAKE-built_TYPE（仅适用于Linux）

- 设置为 Release 或 Debug。在 Linux 上构建时应设置此变量。如果需要同时构建调试版和发布版，则需要两个构建目录。

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

# UNCLASSIFIED

# 目标

4

![](images/12f6cd0d432ef63219bd66b8618230cfbac33901a8ea17ecff553be88e09142b.jpg)

![](images/376793e223e69b4b4b9eb19ddbe3c732b4f03341696cfeea01a066e905e851f2.jpg)

- CMake 会生成多个目标，包括每个可执行文件和库的目标。

- 此外，这些目标也很重要：

- INSTALL - 生成一个安装目录。  
- ALL Builds, ZERO_CHECK - 由 CMake 自动为 Visual Studio 集成生成，可忽略。

- WSF 还包含许多额外的构建目标。这些目标都不会作为默认解决方案的一部分运行:

- *_AUTO_TEST - 调用脚本快速测试 WSF 可执行文件。  
- DOCUMENTATION - 构建Sphinx（wiki）文档。  
- 在 CMake-GUI 中通过设置 WSFINSTALL_DOCENTATION 进行安装。  
- DOXYGEN - 构建 Doxygen 源代码文档。   
- 在 CMake-GUI 中通过设置 WSFINSTALL_DOXYGEN 进行安装。

- 课程示例是一个很好的起点，但有时也需要对 CMake 进行一些修改。  
- 课程示例会在一个单独的解决方案文件和构建目录中构建插件。

- 这样可以简化展示：  
（可能）只需要编译一次WSF核心。  
然而，这会使得导航和调试框架的其余部分变得困难。

- 另一种方法是将插件的源代码目录直接放置在“swdev”中。

- 通过对 CMake 进行一些小的修改，您的插件可以与框架的其余部分一起被捕获。  
- 这提供了一个更统一的开发环境。  
- 对于向AFSIM CCB提交功能非常理想！！！

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

6

![](images/47aab543ca474d9be17122a08b0afdeb7c3bc54a85cf5bd8a803007253ce9113.jpg)

# 集成－使用课程示例

![](images/1c04fa9e5aaf9ce317c093edc47189e8031c1ecd029e0544ea62b9f013c22066.jpg)

- 用户经常会根据课程示例来调整代码以满足自己的需求。   
- 优点：

- 是一个很好的起点，大部分代码已经完善。  
- 从已知的、可运行的源码开始。  
- 解决方案文件简化（适用于插件）。

- 缺点:

- 无法轻松导航WSF框架的其余部分。  
- CMake 对相对文件夹非常敏感。  
- 需要事先准备一个单独的WSF构建目录以进行链接。  
- 此构建目录还必须与您的配置匹配！

- 如果调整课程示例，关键点是确保 CMake 中的相对路径保持一致。

```cmake
9 # Set options to find the plugin (standard WSF) build location, and the WSF source location
10 set(WSF Plugin_BUILD_LOCATION "$({CMAKE_CURRENT_SOURCE DIR})/..//./././././build_directories/wsf_build"
11 set(WSF SOURCE_LOCATION "$({CMAKE_CURRENT_SOURCE DIR})/..//./././././swdev" Cache STRING "Path to 'swdev"
12
13 # Specify a user-defined option to create a plugin version.
14 option(PLUGIN "Make a plugin version" ON)
15
16 # Specify the name of this project.
17 projet(sensor exercise) Don't forget a name.
18
19 # Add all files into the project to be compiled.
20 FILE(GLOB SRCS *.cpp *.hpp)
21
22 # Locate 'misc' and 'tools' directories and set variables that
23 # will be used in this and other CMake files
24 find_path"MISC_DIRECTORY swdev_project.cmake NO_SYSTEM_ENvironment_PATH HINTS
25 $({CMAKE_CURRENT_SOURCE DIR})/..//./././././swdev/misc)
26
27 # The following section provides the necessary definitions for compatibility
28 # with the WSF cmake build directives.
29
30 # Locate the directory that contains the core wsf directories
31 # (wsf, wsf-package, wsfutil) and store the full path in the
32 # WSF_ROOT variable that will be used in this and other CMake files
33 get Filename_component(WSF ROOT "$({CMAKE_CURRENT_SOURCE DIR})/..//./././././swdev ABSOLUTE") 
```

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

8

![](images/202f7f07486944d8b53feafbf1c85824e8dfcd758a1e156f02a39352e63ce681.jpg)

# UNCLASSIFIED

# 集成-使用课程示例

![](images/4dba11305a18927f531d6d56a9558a0e5d8eb97cb3b14fed2c09da87973327ba.jpg)

检查includeDirectories()和target_linklibraries()中的路径。参考您的include语句。

```perl
63 # Specify include directories for the c++ code.   
64 includeDirectories(\(wsf_SOURCE_LOCATION)/wsf/include   
65 \)\\( (WSF_SOURCE_LOCATION)/wsf/include/sensor   
66 \)\S (\) wsf_SOURCE_LOCATION)/wsf/include/observer   
67 \)\S (\) wsf_SOURCE_LOCATION)/wsf_mil/include   
68 \)\S (\) wsf_SOURCE_LOCATION)/wsf_mil/include/sensor   
69 \)\S (\) wsf_SOURCE_LOCATION)/util/source   
70 \)\S (\) wsf_SOURCE_LOCATION)/util_script/source)   
71   
72 # Our target is a shared library (.dll or .so)   
73 add_library(\$PROJECT_NAME) SHARED \$(SRCS))   
74   
75 # Link with the wsf,util,and util.script libraries   
76 target_linklibraries(\$PROJECT_NAME)   
77 debug wsf_d   
78 debug wsf_mil_d   
79 debugutil_d   
80 debugutil_script_d   
81 optimized wsf   
82 optimized wsf_mil   
83 optimizedutil   
84 optimizedutil-script)   
85 
```

Any custom grammar to include?

install(FILES ${CHAKE_CURRENT_SOURCE_DIR}//.grammar/sensor exercis.eag DESTINATION ${CHAKE-instALL_prefix}//.wsf_exec_grammer)

- 集成 - 直接放入 “swdev”  
- 另一种方法是将您的插件文件夹放入“swdev”文件夹，与WSF源代码的其余部分一起存放。

- 优点：

- 在构建时，插件和框架的配置保持同步。  
- 使用单一的构建目录。  
- 如果您希望将其作为功能提交以供AFSIM的通用分发，CCB接受的可能性会大大增加。  
- 您的插件和WSF框架可以一起进行版本管理！

- 缺点：

- 需要在 CMake 上投入更多工作。

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

# UNCLASSIFIED

# 集成 - 直接进入 “swdev”

10

![](images/81d57ec5e15b284343ea7e084fb5f92249049ecf6c32a05ba0b9e638771b585c.jpg)

![](images/a675dba18d4b2b096a0a8b145db5b1d2f9dfc4109ee957ad1039f4444e724431.jpg)

- 现有的示例包括“wsf_p6dof”和“wsf_iads_c2”文件夹，它们位于“swdev/ssfPlugins”下。  
除了主 CMakeLists.txt 文件外，您的文件夹还需要包含以下内容：

- wsf_module: 通过存在此文件, AFSIM 的 CMake 系统会知道该文件夹包含一个需要构建的模块。此文件可以是空的。  
- wsf_cmake_extension.cmake: 设置两个变量：

- WSF_EXT_NAME: 模块的名称。这将在 CMake-GUI 中显示为一个 BUILD_WITH_* 标志。  
- WSF_EXT_SOURCE_PATH：指向插件 CMakeLists.txt 的相对路径。

- 任何可选的免责声明文件：WSF模块具有不同的发布级别。

- 插件的示例目录 ->  
- 这些只是一些约定。  
- “doc”: 包含文档。

- 使用 reStructuredText (.rst) 格式的文档将会被 Sphinx* 处理。

- “grammar”: 包含任何示例语法文件。

- 需要在 CMakeLists.txt 中包含这些文件以进行安装。

- “source”: 包含源文件和 CMakeLists.txt 文件。

- 由WSF_EXT_SOURCE_PATH指向。

*请参见下一页幻灯片，了解将项目添加到Sphinx的宏。

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

# UNCLASSIFIED

![](images/72db7a600537f77aee240c321b43f39021a2e604361069b4835424ca9d314a14.jpg)

# 集成 - 直接进入 “swdev”

![](images/af836deccec73dd8c02e92a8b5553e0f54a1df7840fcf2793c02518dbd8d38ca.jpg)

- 无需查找其余的WSF。  
- 您需要调用以下命令：

- add_subdirectory() - 用于添加您的源文件目录。  
- includeDirectories() - 用于包含您的源目录以及WSF未包含的任何其他文件夹。  
-target_linklibraries() - 用于链接到任何其他WSF库。  
- (插件) add_library() - 用于指示需要构建一个库。  
- (应用程序) add_executable() - 用于指示需要构建一个可执行文件。  
- install() - 用于安装任何构建目标和可选文件。  
- 不要忘记语法文件！

- WSF 内的模块应包含 “swdev_project.cmake” 文件。  
- 此文件包含许多有用的宏，并设置了一些标志。  
- AFSIM 的 CMake 环境中还提供了其他有用的宏:

- add_wsf_doxygen_input() - 作用于源目录。会将该目录添加到 Doxygen 的处理文件夹中。  
- add.wsf_sphinx_input() - 作用于项目目录。会对目录中的 *.rst 文件进行全局搜索，以供Sphinx处理。  
- install.wsf_data() - 如果包含演示场景文件夹，当 WSF_install_DATA 被设置时，此宏会将该文件夹添加到 INSTALL 步骤中。  
- swdevwarning_level() - 将编译器警告设置为与WSF构建的其他部分一致的设置。

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

14

![](images/5749147843476d022c28e7fc16e25e94af6b14547d23744a369d6d6eb5a519e8.jpg)

# UNCLASSIFIED

# 其它问题

![](images/760ecb63599302de6126c7d46307cd74ab89c1a85d9d7e16eaaaf92609ef4a45.jpg)

ieysx@163.com

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQDD.

![](images/69375fff25de38c5c2308ffa346f34ee02feafc98f52da8f8b104e055586642c.jpg)

# 6.2.2. 框架wkf

# 6.2.2.1. Qt 介绍 1_AFSIM_Dev_Trng_Qt

本文为afsim2.9_src\training\developer\wkf\slides\1_AFSIMDev_Trng_Qt.pptx的翻译，主要是介绍了一下QT。

![](images/650b9f7fb37f450db14bdf28d8937f27c2e03cd377f6df0f48dc6479553b78ff.jpg)

Integrity $\star$ Service $\star$ Excellence

# AFSIM开发培训 Qt介绍

本文档由杨石兴翻译，该资料做为《AFSIM2.9参考手册》的一部分。没有《AFSIM2.9参考手册》的加杨石兴微信领取：13324598743

# AFRL/RQQD 美国空军研究实验室

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

UNCLASSIFIED

![](images/0fe29473c03f15f540c3e25a4492574e9eb23f26886596908a813f53d20b71c8.jpg)

介绍

![](images/25c8c22e7e59a9cc7cc496adc202831685673e7e2d67c4968afdafecf870553f.jpg)

1

- 该演示旨在简要概述第三方库 Qt，它在 Wizard、Warlock 和 Mystic 的开发中被广泛使用。  
- Qt 是一个文档齐全的框架，在线上有许多教程可供学习。

![](images/400f80c4ba413582a012cceed1e74cb58a52ee8186f4fb4ee3fdc744dc38c1ec.jpg)

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

- Qt 是一个免费的开源 C++ 应用框架，用于跨平台开发（桌面、嵌入式和移动平台）。

- 支持的平台包括：Windows、Linux/X11、Android、iOS、macOS等。  
- Qt不仅仅用于用户界面开发。

- 它是 AFSIM 可视化软件（如 Warlock、Wizard 和 Mystic）所依赖的多个第三方库之一。

- 我们目前使用的是 Qt 5.12。

- 支持通过“Config-file Packages”使用 CMake（参考：http://doc qt.io/qt-5/cmake-manual.html）。  
- Qt Creator IDE

- Qt Creator 是一个跨平台的集成开发环境，是 Visual Studio 的替代方案。

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQQD.

# UNCLASSIFIED

# Qt模块

3

![](images/0b77bf3309258b527210a7282d339f22f51c190cec0a5c186f02f953ee1b0497.jpg)

![](images/42d932101d9e583c136b9decc58b3d1d67999486f8f2ffb1c7a8736f3ed29561.jpg)

# - 重要模块

<table><tr><td>模块</td><td>描述</td></tr><tr><td>Qt Core</td><td>被其他模块使用的核心非图形类</td></tr><tr><td>Qt GUI</td><td>GUI组件的基础类，包括OpenGL</td></tr><tr><td>Qt Widgets</td><td>用于通过C++扩展Qt GUI的类</td></tr><tr><td>Qt Network</td><td>用于便携且简单的网络编程的类</td></tr></table>

# - 附加模块

- 用于特定目的，许多模块仅适用于某些平台。  
示例:

- Qt WebEngine   
- Qt Windows Extras，提供针对 Windows 的平台特定 API  
- Qt Charts（GPL授权）

http://doc qt.io/qt-5/qtmodules.html

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19.

Other requests for this document shall be referred to AFRL/RQQD.

QObject

- 所有 Qt 对象的基类。  
- 提供信号/槽机制，实现无缝的对象间通信。

- QWidget 继承自 QObject

- 是所有 UI 对象的基类

- 窗口类

- QDialog   
QMainWindow

- 常用的控件（widgets）...

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQQD.

UNCLASSIFIED

5

![](images/e2e4dd751e469563626534f66bf0929e1531e63872e0bfd8ff2f83b7316cb898.jpg)

# 常见QT窗口

![](images/e5ad23f53c662ee6f1d222c220a32aafc7fc3f189e3fc2760e63af6e5bc0784b.jpg)

- 按钮

- QPushButton, QToolButton, QRadioButton, QCheckBox

- 列表

- QListWidget/View, QTreeWidget/View, QTableWidget/View

- 容器

QGroupBox, QTabWidget, QStackedWidget, QDockWidget

- 输入框

- QComboBox, QLineEdit, QSpinBox, QSlider

- 显示框

- QLabel, QProgressBar, QOpenGLWidget

- 主窗口元素

- QToolBar, QStatusBar, QToolBar

- 菜单

- 可以是“弹出式”（例如上下文菜单）或附加到菜单栏上。  
由QActions组成。

- QObjects 会组织成对象树

当你创建一个带有父对象的 QObject 时，它会被添加到父对象的 children() 列表中，并在父对象销毁时一同被删除。  
- 这种方法非常适合GUI对象的需求

例如，一个QShortcut（键盘快捷键）是相关窗口的子对象，因此当用户关闭该窗口时，快捷键也会被删除。

- QObject 可以访问其 parent() 和子对象的 children() 列表。  
- QWidget扩展了父子关系

子对象会显示在父对象的坐标系统中，并且会被父对象的边界裁剪。  
- 你可以手动删除子对象（不通过父对象的析构函数）  
子对象会自动从其父对象中移除。

- 调试功能

- 提供了 QObject::dumpObjectTree() 和 QObject::dumpObjectInfo(), 用于调试对象树和对象信息。

http://doc qt.io/qt-5/objecttrees.html

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQQD.

UNCLASSIFIED

# 信号槽

7

![](images/c510099a0d0e79b441a2f86fa9a4ab27fd0e9d15f72aefe88bba67618e5fd5f2.jpg)

![](images/b5cf8b0731c811e3776cfd5d758f54697055958cefa70ce0926a99eefb3a47c9.jpg)

- 用于对象之间的通信

- 通过 Qt 的元对象系统（meta-object system）实现。

- 类似于回调或发布/订阅设计模式

- 信号（signal）在特定事件发生时发出，而槽（slot）是响应特定信号时调用的函数。

- 信号/槽机制的特点

- Qt 的控件（widgets）有许多预定义的信号和槽，但我们可以通过继承控件类来添加自定义的信号和槽。  
- 信号/槽机制是类型安全的：信号的签名必须与接收槽的签名匹配。  
- 槽的签名可以更短（即可以忽略多余的参数）。  
- Qt5 的语法允许编译器检测信号和槽之间的签名不匹配。

- 信号与槽的连接

- 使用 Qt 的 connect 方法将信号连接到槽，这样当信号发出时，相应的槽（函数）会被执行。  
- 支持跨线程通信，通过队列连接（queued connections）实现。

http://doc qt.io/qt-5/signalsandslots.html

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19.

Other requests for this document shall be referred to AFRL/RQQD.

- VS菜单：Tools > Extensions and Updates...   
- 搜 Qt 下载 “Qt Visual Studio Tools”   
- Version 2.5.2 - support for VS 2013, 2015, 2017   
- 功能

- 在调试时为 Qt 类型提供原生可视化工具。  
- 打开 .ui 文件时会自动启动 Designer。  
集成文档！！！（F1帮助）

![](images/9dd27817b2b63cb80b63f4a55e0728725acd5e0a857a2c6d5a6d3ad9d92358e2.jpg)

http://doc qt.io/qtvstools/index.html

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

# UNCLASSIFIED

![](images/47590d5b31d8fc6334fe3fbe173b77d530f7012ab3c0115ea800f1f5ee6aea45.jpg)

# 参考

![](images/472f1b1a417a51a8e6f9d9b61b8c4c10b70648cb21560ec67af506b82312c6f2.jpg)

- Qt Wiki

http://wiki.qt.io/

- Qt Documentation

http://doc qt.io/qt-5/

- CMake Manual

http://doc qt.io/qt-5/cmake-manual.html

- Qt Style Sheets

http://doc.qt.io/qt-5/stylesheet.html

![](images/dcbb6edf5295375fcff70334ffed284ae5313aac9fc259bf27a4ea7380c5261b.jpg)

11

# 6.2.2.2. WKF 介绍 2_AFSIMDev_Trng_WKF

本文为afsim2.9_src\training\developer\wkf\slides\2_AFSIMDev_Trng_WKF.pptx的翻译，主要是介绍AFSIM开发框架WKF的使用，并做了些小例子。

![](images/03cbd5dbb6a61185ea80fc922a87c738e83e6ab73d5359cced4f076d9e2c83fe.jpg)

UNCLASSIFIED

![](images/8c4cb63527a331c6ccccf89b73e22cf2881d325d81cb3144b1f3ca492fb07af2.jpg)

![](images/03e4b24b52e6840328e00b4b7a5599888d1481a167b4e9fa7e7b2a92a8feac9a.jpg)

# AFSIM开发培训

# 2-WKF介绍

本文档由杨石兴翻译，该资料做为《AFSIM2.9参考手册》的一部分。没有《AFSIM2.9参考手册》的加杨石兴微信领取：13324598743

Integrity $\star$ Service $\star$ Excellence

AFRL/RQQD 美国空军研究实验室

AFSIM - Advanced Framework for Simulation, Integration, and Modeling

AGL – Above Ground Level

DIS - Distributed Interactive Simulation

DTED-Digital Terrain Elevation Data

EO/IR - electro-optical/infra-red

ESM - electronic support measure

FOV - field of view

GUI - graphical user interface

HLA-High Level Architecture

ID - identification

IEEE - Institute of Electrical & Electronics Engineers, Inc.

JTIDS - Joint Tactical Information Distribution System

MSL - Mean Sea Level

OS - Operating System

PC-Personal Computer

PDU - Protocol Data Unit

RCS-radar cross section

SAM - surface-to-air missile

SAR - synthetic aperture radar

VESPA - Visual Environment for Scenario Preparation and Analysis

WSF - World Simulation Framework

dB - decibels

dBsm - decibel square meters

deg-degrees

ft-feet

GHz-GigaHertz

kts-knots

m - meters

m^2 - square meters

mw-megawatts

nm - nautical miles

s - seconds

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19.

Other requests for this document shall be referred to AFRL/RQQD.

# UNCLASSIFIED

![](images/226f440df43af6e9a2b5e64eabb8f96a066ba59879e88aefaa48c86b765f7eff.jpg)

# 介绍

![](images/1a518926f35d01109bcff79c859d080b82cf30f5fd2c65aac1e9f34eaaa7b72e.jpg)

- 本实验的重点是使用通用框架（WKF）扩展AFSIM-Wizard，该框架旨在支持所有AFSIM可视化应用程序（Wizard、Warlock和Mystic）。  
- 您将构建一个基于 $\mathrm{C} + + \mathrm{W} / \mathrm{K} \mathrm{F}$ 的新插件, 该插件将创建一个停靠窗口小部件以显示数据, 并创建一个附件以显示在中央地图显示上。

![](images/1cd8db9690d81fc803ac1da6f5cfc8c406e34f00d2f72aa0524a418d12aa3bae.jpg)

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19.

Other requests for this document shall be referred to AFRL/RQQD.

- 扩展 Wizard 应用程序以提供新功能  
- 创建新的可视化内容以显示在地图上

![](images/e7b9689ffa6c494bdc67d0a32931c627d85da7b34badb88dc81f13c724b8f3cb.jpg)

# 参考资料：

- AFSIM 开发者的基于网络的数据。  
- AFSIM 源代码和 Visual Studio 搜索功能。  
- AFSIM 文档。

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQQD.

# UNCLASSIFIED

![](images/6b1418e0daf2a3315acb502fb05b36d507f6cdce21f38d6248ce61cc374a5b61.jpg)

# 学习目标

![](images/6e750c7e34dd721726e7eecab6697a52aad96f44234e2e12b8669fd156e90e30.jpg)

- 您将获得以下方面的实践知识：

- 什么是WKF和VTK，以及如何使用它们  
- 如何创建插件以扩展 Wizard  
- 如何创建附件并将其添加到平台中

![](images/19e56dbe9b6ddbcd3d434806c27a4cd560e7b583b7f73391031bc3e6bdc41749.jpg)

![](images/4be377f9f5b2684fa76869e33815f425288e524b8b1200f5ecdfc8b8e669426c.jpg)

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19.

Other requests for this document shall be referred to AFRL/RQQD.

- Vespa 工具包

- 它是 VESPA（遗留工具）构建所基于的框架。  
- 用于创建和管理地图显示以及显示在其中的对象。  
- 位于工具目录下名为“vespatk”的目录中。

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQQD.

6

![](images/5f113a7b005f59f53777515d2efd9a7b4ebd4aae23a31623eb316e70b7f1bc25.jpg)

UNCLASSIFIED

# VTK 的概念

![](images/ada7f69b931039212694ced3035bfde4c8d1fc4ec6cfe6020fccd5e35a3d6cab.jpg)

- Attachment（附件）：

- 场景中的一个视觉元素，与实体（Entity）和查看器（Viewer）相关联。

- Entity（实体）：

- 场景中平台的表示形式，包含一组称为附件（Attachments）的元素。

- Environment（环境）：

- 包含查看器（Viewers）和场景（Scenarios），管理场景时间，并提供对应用程序工厂的访问。

- Overlay（叠加层）：

- 用于在查看器（Viewer）中显示与实体（Entity）无关的视觉元素。

- Scenario（场景）：

- 应用程序中加载的一组实体的容器。

- Viewer（查看器）：

- 控制可见场景，是附件（Attachments）和叠加层（Overlays）的容器。

- Warlock 框架 (WKF)

- 通用应用程序代码，利用 Qt 和 VTK 提供核心应用程序功能，并支持地图显示功能。  
- 该框架最初是为支持 Warlock 的开发而创建的，后来被用于创建结果可视化工具（现称为 Mystic）。  
- 在AFSIM2.4中，Wizard被转换为使用WKF。  
- WKF 通过其插件接口支持扩展。

- 这些插件可以是所有三个应用程序通用的，也可以仅限于某个单一应用程序使用。

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

8

![](images/b7f0903da022dbbe7d552a77ff7cded0942a95e987b8085f09ce2ae82e8425e4.jpg)

# UNCLASSIFIED

# WKF是什么？

![](images/2f58b25692c68ec77f6e05bac5b01d326de6723d20c8e0faf3170c1289987dee.jpg)

- 用于创建 GUI 和支持功能的核心代码

- 该代码被所有WKF应用程序使用。  
位于 tools/wkf/core 目录中。

- WKF 应用程序可能使用的通用代码

- 包含一些类，这些类不会直接从 WKF 内部实例化，但通常被不同应用程序的插件使用。  
- 有助于插件的代码复用。  
位于tools/wkf/common目录中。

- 适用于所有WKF应用程序的通用插件

- 位于 tools/wkf/plugins 目录中。

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19.

Other requests for this document shall be referred to AFRL/RQQD.

- 在WKF中有两个Environment（环境）类：  
- wkf::Environment (wkfEnv):

- 提供对主窗口（MainWindow）、首选项（Preferences）、目录路径（Directory paths）、用户选择等的访问。  
- 这是最常用的 Environment 类。

- wkf::VtkEnvironment (vaEnv):

- 扩展自vespa::VaEnvironment。  
- 插件使用此类来访问标准查看器（Standard Viewer）和标准场景想定（Standard Scenario）。

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQQD.

10

![](images/f152959f3ba236de10caac51fb82aeb097ca10be3c5059394fe1395cc35aea87.jpg)

UNCLASSIFIED

# 标准想定场景

![](images/6e43c58951a5e5f1f1f45fa6a025940811c4527c97c8e34ba2e87d8eacbf640a.jpg)

- 标准场景（Standard Scenario）是已注册到 VtkEnvironment 类的场景对象。

- 标准场景的类型为 wkf::Scenario，它继承自vespa::VaScenario。  
- 场景（Scenario）允许访问平台（Platforms），附件（Attachments）随后可以被添加到这些平台中。

wkf::Scenario\* scenario $=$ vaEnv.GetStandardScenario(); if(scenario $! =$ nullptr) { //Do Stuff }

标准场景（Standard Scenario）可能为nullptr，因此在使用标准场景之前需要检查是否为nullptr。

- 标准查看器（Standard Viewer）是已注册到

VtkEnvironment 类的查看器对象。

- 标准查看器的类型为vespa::VaViewer。  
- 目前由MapDisplay插件注册该查看器。  
- 其他插件如果需要，可以更改标准查看器，但一次只能有一个查看器被指定为标准查看器。  
- 插件可以向查看器添加叠加层（Overlays）或控制摄像机（Camera）。

```txt
if (vaEnv.GetStandardViewer() != nullptr) { vaEnv.GetStandardViewer()->AddOverlay(layer); }
```

```txt
标准查看器（StandardViewer）可能为nullptr，因此在使用标准查看器之前需要检查是否为nullptr。
```

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQQD.

# UNCLASSIFIED

![](images/d5ae9780d20c11727d78076110989e959b99d9ff979c05cabb75e8e753da8789.jpg)

# WKF插件接口

![](images/3caa07d6d57e1f89fc6c9877211d42fffedd51e1c8f24329c9e8545ace145c09.jpg)

- wkf::Plugin 是一个抽象基类，视觉应用程序通过继承该类来实现其插件类。

- 提供插件管理器的注册接口。  
- 提供与GUI交互的方法。

- 一些插件在所有 WKF 应用程序中是通用的：

- 例如MapDisplay、MapHoverInfo、TetherView等。

- 所有插件必须导出必要的符号，以便注册到WKF插件管理器中。  
- 在 WkfPlugin.hpp 中提供了一个方便的宏：

WKF_PLUGINDEFINE_SYMBOLS(PLUGIN_CLASS, PLUGIN_NAME, DESCRIPTION, TAGS, ...)

- 通常放置在插件类的cpp文件顶部。  
- PLUGINS_CLASS: 插件的类名。  
- PLGINNAME: 插件在GUI中显示的名称。   
- DESCRIPTION: 插件功能的描述。  
- TAGS：用于确定哪些WKF应用程序可以加载该插件的标签列表，标签之间用竖线（|）分隔。

- 例如：Warlock会加载带有标签“all”或“warlock”的插件。

- OPTIONAL...：可选的布尔标志，指示插件是否默认加载（如果未指定值，则插件会被加载）。

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

# UNCLASSIFIED

# 选择wkf::Plugin的虚方法

![](images/ee3f69cf8556c7995c66ef5b9d8856ee1554c5f295020f83c43fd97726acb38e.jpg)

- GetPreferencesWidgets() - 返回将在“首选项”对话框中显示的 PrefWidget 列表。  
- GetActions() - 返回用户可以在“首选项”对话框中绑定到键盘快捷键的 Action 列表。  
- BuildPlatformContextMenu() - 允许插件向平台的上下文菜单（右键菜单）中添加项目。  
- GetPlatformData() - 当平台选择发生变化时，允许插件提供有关所选平台的数据，这些数据将显示在“平台数据”对话框中。  
- RegisterOption()和RegisterOptionGroup() - 定义将在“平台选项”对话框中显示的选项。通常在插件的构造函数中调用。  
- LoadSettings() 和 SaveSettings() - 这些函数在用户请求时被调用，以允许插件保存/加载首选项数据。SaveSettings 也会在应用程序退出时调用。  
- GuiUpdate() - 以固定的频率调用，允许插件更新其显示内容。

![](images/024df9d63fec955abdb1938d86720d96be8eb7670d89139914d0a4ad38b4205e.jpg)

- 创建一个 WKF 插件的 CMakeLists.txt 文件非常简单。WKF 将所需的 CMake 配置抽象为一个可以调用的宏。  
- 大多数 WKF 插件的 CMakeLists.txt 文件如下所示:

- plugin_cmakelists_template(MapHoverInfo tools/wkf LIBRARIES wkf wkf_common)   
- 一些插件会包含额外的第三方依赖：
    - plugin_cmakelists_template(MapDisplay tools/wkf
        THIRD_PARTY_INCLUDE_DIRS osg
        LIBRARIES wkf wkf_common)

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQQD.

# UNCLASSIFIED

![](images/acaa5c1f4a69f07799d66c02a3432cb57edc008fd0e1be470eefc679b5967d8d.jpg)

# Plugin Manager对话框

![](images/f9147f7cfd5bf794bdedfb57b50f67ca8726cf09e6a8a77b75deb4d6dd92faa9.jpg)

- 在创建插件时，不需要与WKF插件管理器直接交互。所有与插件管理器的交互都由基类完成。  
- 插件管理器对话框可以通过菜单 Options->Plugin Manager... 访问：  
- 显示加载插件时遇到的错误。  
- 可以禁用插件的自动启动功能。这在调试插件问题时非常有用。  
- 显示每个插件的描述信息。

![](images/808ccaaed3c8d430d6ec3984937ce9e7f551055539d4b62b96ff34af297d5f42.jpg)

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQQD.

- 平台选择由wkf::Environment处理。

修改选择的方法：

- PlatformSelectionChanged() 信号：当选择发生变化时发送。  
- PlatformOfInterestChanged() 信号：当关注的平台发生变化时发送。

- 关注的平台（Platform of Interest）：

- 这是最近选择的平台。  
- 对于不支持多选的显示器，这非常有用。如果您的插件不支持多选，则应使用关注的平台。  
- 这可以更好地优化GUI的更新。

- 当前仅有以下插件修改平台选择：

- 平台浏览器（Platform Browser）  
- 地图显示（Map Display）插件

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQQD.

# UNCLASSIFIED

# 平台上下文对话框

![](images/bc52682a54f0c37a7a4d46577c4640f2471ce0e9aea0171f2c2413143d4ab6e2.jpg)

![](images/6a5a353b9b28916c6771f5166c58ddd960a220876b550a4e7e31e8e942d23911.jpg)

- WKF 提供了两个基于平台选择的标准对话框，所有插件都可以向其中添加内容：

- 平台选项（Platform Options）：

- 显示所选平台的布尔选项，例如隐藏/显示轨迹线的能力。  
- 在插件的构造函数中，使用 RegisterOption() 或 RegisterOptionGroup() 方法注册选项。

- 平台数据（Platform Data）：

- 显示关于关注平台（Platform of Interest）的数据。  
- 重写 GetPlatformData() 方法，并返回 QTreeNode 的列表。  
- 对于带有单位的值，使用wkf::UnitTreeMenuItem，稍后将在讨论“首选项（Preferences）”时详细介绍。

- 配置是所有首选项选择的快照，包括加载了哪些插件、哪些窗口可见以及它们的位置和大小。

- WKF 允许用户保存、加载和导入配置:

- 窗口的几何形状和可见性会自动保存。  
- 首选项通过在wkf::Plugin中重写的SaveSettings和LoadSettings方法进行保存和加载。  
- 不需要额外的工作即可支持配置功能。

- 配置的保存和加载：

- 可以通过“文件”菜单保存/加载配置。  
- 可以通过命令行使用 -cf 或 -icf 选项指定配置文件。

- 更多关于配置的内容：

- 在Warlock培训演示中讨论首选项时会进一步介绍配置。

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQQD.

20

![](images/e82a3c1d98e5728f8a882423d3d7d4113be848ed7f314f20a89cafc3b5ac1b0a.jpg)

# wkf::MainWindow

![](images/1c614f7229dd2fed3f24e04e96fb50a1fe25bd4ba8dbe7724be5ae261f133308.jpg)

- WKF 应用程序的主窗口可以通过 wkf::Environment::GetMainWindow() 访问。  
·方法：

- 添加菜单并通过名称获取菜单 (Add menus and GetMenuByName)   
- 将对话框添加到工具菜单 (Add a dialog to the Tools menu)   
- 添加停靠窗口 (Add DockWidgets)

- 一个用于切换可见性的操作会自动添加到“视图”菜单中 (An action to toggle visibility will automatically be added to the View menu)

- 在状态栏上显示消息，或访问状态栏 (Show a message on the status bar, or access the status bar)  
- 获取中央窗口部件(Get the central widget)（详见下一页幻灯片）

- CentralDisplayWidget 位于 MainWindow 的中心。

- 允许以多种配置显示多个窗口部件（widgets）。  
- wkf::DockWidget 的上下文菜单允许用户在中央窗口部件中移动窗口部件，并将其移除。

![](images/0cfbe3baf0ba59fc0ff1df119d596e91c935e04abd989fb8872a3d853f7cefb1.jpg)

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

UNCLASSIFIED

![](images/87f5132e416c568fbe631e95af1f611cb68bdf7703e2d61045ed288f6678afd6.jpg)

# wkf::DockWidget vs QDockWidget

![](images/f03d09582a813ee2f9b02e7704a9dd248f5197cfccf717248ca8767eeef75bfe.jpg)

- wkf::DockWidget 继承自 QDockWidget，并增加了与 CentralDisplayWidget 交互的功能。

- 提供支持在中央窗口部件（central widget）中移动或移出的功能。  
- 提供构建上下文菜单的功能。

- 将额外的状态信息保存到设置文件中。  
- 只有 wkf::DockWidget 可以添加到 CentralDisplayWidget，而不能使用 QDockWidget。  
- 建议：除非您特别希望您的 DockWidget 能够停靠在中央窗口部件中，否则推荐使用 QDockWidget。

Hint: Hold ctrl when moving Dock Widgets to prevent them from docking.

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

- 在可视化应用程序的源代码中，您可能会看到使用PluginUiPointer<T>代替QPointer<T>。  
- QPointer 是一个受保护的指针（guaranteed pointer）：

- 它的行为类似于普通的 C++ 指针 T*, 但当所指向的对象被销毁时, 它会自动设置为 nullptr, 从而避免悬空指针的问题。

- PluginUiPointer 包装了 QPointer，并提供了额外的内存管理功能：

- 在其析构函数中会删除 T，从而自动管理内存。

·注意：

- 使用 PluginUiPointer 并不是强制要求的，您也可以直接使用 QPointer。  
- 但如果使用 QPointer，需要记得手动删除其 data() 指向的对象。

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

UNCLASSIFIED

![](images/e15fbe5124179e0f7a48fdec7dc493c4bd9dc04a867dc026f3bf5c7f7177296a.jpg)

# WkfPlatform警告

![](images/f9ccb4e62c2c0db9cf2195cfd9f9c9855ccdc2712f05d5830bc6e7e54d1591a9.jpg)

- 地图显示（Map Display）使用的是 WkfPlatform（不要与 WsfPlatform 混淆），它继承自 VaEntity，而 VaEntity 是 VTK 的一部分。

- 附件（Attachments）可以从任何插件添加到 WkfPlatform。

- 使用从VaAttachment派生的类。  
- WkfPlatform 将接管任何添加到它的附件的所有权，并在 WkfPlatform 被删除时自动删除这些附件。

示例：路线（Routes）、翼带（Wing Ribbons）和平台模型（Platform Model）。

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

- 创建附件:

```cpp
vespa::make_attachment<wkf::AttachmentRangeRing>(\*platform, vaEnv.GetStandardViewer(), "range_ring"); 
```

- 访问一个附件:

auto ring $=$ platform->FindAttachment("range_ring"); if (ring != nullptr) { //do stuff }

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQQD.

# UNCLASSIFIED

![](images/3650f15950379ea8387a1577ed36852aabce6f304f842b1c7b79412c76af1c0f.jpg)

# 菜单&状态栏

![](images/3751886ababaf487f81eb60ac47f1258c8adcdd88be2b4befb69cc9d3674107c.jpg)

- 应用程序的菜单栏和状态栏可以通过wkf::MainWindow类访问。  
- 虽然可以调用从 QMainWindow 继承的任何方法，但最好使用 wkf::MainWindow 类中提供的方法：

- AddMenu()   
GetMenuByName()   
- AddDialogToToolBar()   
- addToolBar()   
addDockWidget()   
ShowStatusMessage()

- 这些函数处理插件与菜单栏和状态栏的常见交互。

- 例外情况：

如果您想向状态栏添加一个窗口部件（widget），可以参考SimController插件中的示例来处理这种情况。

- 创建一个简单的插件用于 Wizard

- 这是一个通用插件，因此 Warlock 和 Mystic 也可以加载此插件。  
- 创建一个 QDockWidget，显示“Hello World”。  
- 在“视图”菜单中添加一个操作，用于显示 QDockWidget。  
- 当所选平台发生变化时：

- 为每个选定的平台添加一个附件（Attachment）。  
- 从不再选定的平台中移除附件。

- 学习使用插件管理器（Plugin Manager）来验证插件是否正确加载，并查看如果未加载成功时的错误消息。

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

# UNCLASSIFIED

# 配置WKF培训

28

![](images/7a1512adf90968dcd2e8c2d2e494b28d8f6f8173f1c402389e3862ff4e6b8fb6.jpg)

![](images/a4b37e78d39ff5dded623fcd67b4f0d70d54a9bd917ec5885a346fd2478b027a.jpg)

- 编辑文件：training/developer/wkf/labs/config.cmake

- 确保正确的生成器（Generator）已取消注释。  
如果您使用的是 Visual Studio，请确保 CMAKE_GENERATORPLATFORM 已取消注释。  
如果您希望使用 Unity 构建, 请取消注释与 Unity 构建相关的两行代码。

在：training/developer/wkf/labs/config.cmake文件中

- 确保以下的项都设置为TRUE

- BUILD_WKF_PLUGIN_WKF_Training   
BUILD WITH mission   
- BUILD WITH wizard   
BUILD WITH wsf mil   
BUILD WITH wsf p6dof   
- BUILD WITH wsf parser   
BUILD WITH wsf space   
- BUILD_WIZARD_PLUGIN_WizMapAnnotation   
- BUILD_WIZARD_PLUGIN_WizMysticLauncher   
- BUILD WIZARD PLGIN WizPlatformBrowser   
- BUILD WIZARD PLUGIN WizPlatformData   
- BUILD_WIZARD_PLUGIN_WizSimulationManager   
- BUILD WIZARD Plugin WizSpaceTools   
- BUILD_WIZARD_PLUGIN_WizTypeBrowser   
- BUILD_WIZARD_PLUGIN_WizUnitConversion   
- BUILD WIZARD PLGIN WizZoneEditor   
- BUILD_WKF_PLGINmapDisplay   
- BUILD_WKF_PLUGIN_MapHoven   
- BUILD_WKF_PLUGIN_TetherView

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQQD.

# UNCLASSIFIED

# 配置WKF培训 (cmd shell)

![](images/8937bb470abf5df93db2a50648dca52c1adf35307876db72f85e6fcf6587b026.jpg)

![](images/e7e5c6a8081d2a525f22e67cea749146cea700a7fcf8e4d0fbd2429d76d35d24.jpg)

30

在CMD中.windows):

- cd到AFSIM主文件夹中(包含training文件夹)  
- 执行如下：

>cd training\developer\wkf\Labs   
> scriptpath=%cd%\config.cmake   
> cd inwork   
>extpath=%cd%

如果在AFSIM release模式下工作使用则执行：

> cd ../\..\..\swdev\src

否则执行：

>cd...\...\...\...\afsim

- 最终执行：

> set srcpath=%cd%   
>cd...\build   
> rm CMakeCache.txt   
> cmake -C %scriptpath% -DWSF_ADD Extensions_PATH:PATH=%extpath% -B . -S %srcpath%

在a bash shell中 (git bash in Windows or bash in Linux):

- cd到AFSIM主文件夹中(包含training文件夹)  
- 执行以下命令；

```txt
$ cd training/developer/wkf/labs
$ scriptpath=$PWD/config.cmake
$ cd inwork
$ extpath=$PWD 
```

如果在AFSIM release模式下工作使用则执行：

```txt
$ cd ..//././.swdev/src 
```

- 否则执行:

```txt
$ cd ..//././.afsim 
```

- 最终执行：

```shell
$ srcpath=$PWD
$ cd ../build
$ rm CMakeCache.txt
$ cmake -C $scriptpath -DWSF_ADD Extensions_PATH:PATH=$extpath -B . -S $srcpath 
```

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQQD.

32

![](images/908cf81a6b4dbea517005e76fd10b4f2f2c142086a4178c6ada2b28975190939.jpg)

# 练习1-任务1

# TrainingPlugin.hpp and TrainingPlugin.cpp

![](images/386cf92a1d9d4ee35dd673bf2219616bd0614490d0b3b889c5c23610ed685a11.jpg)

- 在文件 TrainingPlugin.hpp 中，创建一个名为“Plugin”的类，该类继承自 wkf::Plugin。  
- 在文件 TrainingPlugin.cpp 中，在 Plugin 类的实现文件中调用宏函数 WKF PluginrogenDEFINE_SYMBOLS。

- 这是一个导出插件管理器（PluginManager）所需符号的宏。  
- WKF_PLUGIN {?}DEFINE_SYMBOLS 的格式如下：：

define WKF Plugin	define_SYMBOLS(Plugin_CLASS, Plugin_NAME, Plugin_description, TAGS, ...)

- 该宏接受以下参数：

- PLGIN CLASS: C++ 类的名称  
- PLGIN_NAME:插件的名称，用于向用户显示  
- PLGIN DESCRIPTION: 插件的描述  
- PLGINTAGS: 定义哪些应用程序将使用/加载该插件  
- ...：一个可选的布尔值，指定是否默认加载插件

TrainingPlugin.hpp   
```cpp
// EXERCISE 1 TASK 1a
// Derive a new class Plugin from wkf::Plugin
class Plugin : public wkf::Plugin
{
public:
    Plugin(const QString& aPluginName,
        const size_t aUniqueId);
    ~Plugin() override = default;
private:
    //! Adds range rings to all newly selected platforms.
    //! Removes range rings from all unselected platforms.
    //! @param aSelected This is a list of newly selected platforms.
    //! @param aUnselected This is a list of newly unselected platforms.
    void SelectionChanged(const wkf::PlatformList& aSelected,
                      const wkf::PlatformList& aUnselected);
};
TrainingPlugin.cpp
// EXERCISE 1 TASK 1b
// Add the macro WKF_PLUGIN DEFINE_SYMBOLS
// The PLUGINTags should either "wizard | warlock" or "all",
// so that the plugin will be loaded by both Wizard and Warlock
WKF_PLUGINDEFINESYMBOLS(Training::Plugin, "WKF Training", "Plugin created for AFSIM Developer Course.", "all") 
```

中

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

34

![](images/ddd7282e0c3020d8e44368f10f508411a4d921cf7f08a7287940b66b62af7299.jpg)

# UNCLASSIFIED

# 练习1- 任务2

# TrainingPlugin.cpp

![](images/bddef359fcac43d9ee47d2c0c7a3ccf7e96e5a6d7aff192f0e2c0c80f53f03c0.jpg)

- 在 Plugin 类的构造函数中：  
- 任务2a:

- 从 Environment 类访问主窗口（Main Window）。  
- 创建一个指向主窗口的 wkf::MainWindow 指针，该主窗口通过调用 wkfEnv::GetMainWindow() 返回。

- 任务2b:

- 构造一个 DockWidget 并将其添加到主窗口中。   
- 使用任务 2a 中的指针调用 AddDockWidget 方法。

- 第一个参数应为：Qt::RightDockWidgetArea。  
- 第二个参数应为指向新建 DockWidget 的指针。  
- https://doc qt.io/qt-5/qmainwindow.html#addDockWidget

WKF Plugin	define_SYMBOLs(Training::Plugin, "WKF Training", "Plugin created for AFSIM Developer Course.", "all")

Training::Plugin::Plugin(const QName& aPluginName, const size_t aUniqueId)

: wkf::Plugin(aPluginName, aUniqueId)

```cpp
// EXERCISE 1 TASK 2a  
// Get wkf::MainWindow pointer from WkfEnvironment  
wkf::MainWindow* mainWindowPtr = wkfEnv.GetMainWindow();  
// EXERCISE 1 TASK 2b  
// Add mDockWidget to the Main Window,  
// this will also add the action to toggle the visibility of the DockWidget to the View menu  
mainWindowPtr->addDockWidget(Qt::RightDockWidgetArea, new DockWidget()); 
```

：

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQQD.

36

![](images/9832ab9c23fe5d2f94af6cedd5facd2684e1ad5542a303b0364eddba4aa53ed6.jpg)

# 练习1- 任务3

# TrainingDockWidget.ui

![](images/63af59a8da18385e7104e666e1a84a05acaa5c3436824745df471a1d8da85b45.jpg)

- 使用 QtDesigner 向 DockWidget 添加一个 QLabel:

1. 打开 TrainingDockWidget.ai 文件：

路径为：developer\wkflabs\inwork\1_WKF_Training\ui。

2. 启动 QtDesigner:

- Designer.exe 位于 Qt 的第三方包中，路径为：  
- afsim\tools\3rd_party\qt-5.9.7-x86-vs2017\bin。  
- 如果 Designer 无法打开，可能需要在 bin 目录中添加一个 qt.conf 文件。

3. 在Designer中编辑DockWidget:

- 在 DockWidget 中添加一个 QLabel。  
- 将QLabel的文本更改为“Hello World”。

- 完成后保存文件，确保更改已正确应用到 DockWidget 的 UI 文件中

Qt's User Interface Compiler (uic) will convert the UI file into source code https://doc.qt.io/qt-5/uic.html

![](images/b86d47cd94ff1f12ce3c96c2ef7bb3345cd5302fd52fccc2434bfdce83294251.jpg)

qt.conf

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

![](images/2ad9e271ce102a091852d6968fd32325b6e765b5c23ee56c722567aa32a9beca.jpg)

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

# UNCLASSIFIED

# 练习1- 任务4

38

![](images/e5661c2f000c480daa94f79cdf7766d4034a27a9418c84f49a668f077c4235f5.jpg)

![](images/a5bb8df8e7d8ed643ba01ba26b4afbe5a1473c4e1d82f1b5b530f42a2e3d256f.jpg)

- 添加UI到DockWidget当中：

- 任务4a:

- 在文件 TrainingDockWidget.hpp 中，包含由 Qt 的 UIC 从 UI 文件生成的头文件。

- 任务4b:

- 在文件 TrainingDockWidget.hpp 中，为 UI 添加一个类成员变量。  
- 该变量的类型应为 Ui::WKF_Training。

- 任务4c:

- 在文件 TrainingDockWidget.cpp 中，确保在 DockWidget 的构造函数中调用 setupUi() 方法，使用任务 4b 中的变量来完成 UI 的初始化。

TrainingDockWidget.hpp   
```cpp
// EXERCISE 1 TASK 4a
// Add an include for code generated from the .ui file
#include "ui_TrainingDockWidget.h"
namespace Training
{
    //! This represents the specific dockable widget associated with our plugin.
    class DockWidget : public QDockWidget
    {
        ;
        private:
            // EXERCISE 1 TASK 4b
            // Declare a member variable for the UI element defined in "ui_TrainingDockWidget.h"
        Ui::WKF_Training mUI;
    };
}
TrainingDockWidget.cpp
Training::DockWidget::DockWidget(QWidget* aParent,
Qt::WindowFlags aWindowFlags)
: QDockWidget(aParent, aWindowFlags)
{
    // EXERCISE 1 TASK 4c
    // Call setupUI(this) on the UI member variable.
    // If setupUI is not called, the UI will be blank
    mUI_setupUi(this);
} 
```

40

![](images/379d2b00324f9ec8b753d852fe0f439d5edbd17f7879572d11be91969b5fc4b0.jpg)

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

# UNCLASSIFIED

# 测试

![](images/aa567dc9cb015e2f65ad572c157c7592d6db9f98f842f97e9c6f22d0807bc97a.jpg)

- 从 Windows 的 Visual Studio:

- 在“Release”模式下构建解决方案。  
- 构建“INSTALL”项目。

- 从Linux:

- 执行以下命令（在构建目录中）：：

$ cmake --build . --target all -- -j12

$ cmake --build . --target install -- -j12

- 加载 WIZARD 中的测试场景

- 在: training\developer\wkf\Labs\data\wkf_trainingscenario.txt

- 验证：

- 确认“Hello World!!”操作出现在“View”菜单中。  
- 确认“Hello World!!!”停靠窗口（Dock Widget）中显示的文本字符串为“Hello World”。
![](images/4d0ede67a5229c0cde79779d3079e40ac2ab149759edf5c92e196353453963e8.jpg)  
DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

![](images/9fe426f981355f8293b2da948f175c0b02c49e1bc8f6485ba66314ca6635dc31.jpg)

