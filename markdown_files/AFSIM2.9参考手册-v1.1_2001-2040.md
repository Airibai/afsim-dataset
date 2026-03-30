# UNCLASSIFIED

![](images/1ca4c2fb3fed32a22d21dc91af68c541fd9eaade69e51f285bf986277e6cc0df.jpg)

# 变量

![](images/846ef7d128c40f6361a651e1cfbf364b02c8378f8d0399c4ccbe1f60e5518c19.jpg)

17

# - 以下变量的重要性及用途

- BUILD_WITH_...

- 每个可选项目都可以通过切换相关复选框来启用或禁用。默认值由 swdev 目录中该模块的可用性决定。

- BUILD...PLGIN...

- 用于启用/禁用插件。这对于最小化构建大小和调试非常有用。

- WSF_PLUGIN Builds

- 构建共享对象（Shared Object）或 DLL 库，而不是静态库，并启用加载 WSF 插件的功能。

- WSFINSTALL_SOURCE

- 在安装文件夹中创建一个名为 swdev 的目录，其中包含源代码。

- CMAKE-built_TYPE（仅限Linux）

- 设置为 Release 或 Debug。在 Linux 上构建时需要设置此变量。如果需要同时构建调试和发布版本，则需要两个单独的构建目录。

- WSF_ADDExtension_PATH

- 告诉 CMake 在哪里查找插件。在培训中会使用此变量。

- 以下高级变量的重要性及用途  
（需要在cmake-gui中勾选Advanced选项才能查看）

SWDEV_THIRD_PARTY.Package SOURCES

- 告诉 CMake 在哪里可以找到第三方源代码，例如 gtest（mission 需要）、osg、osg-earth、qt 等。

- VTK.RESOURCES_ARCHIVE_FILENAME

- 告诉 CMake 在哪里可以找到 VTK 资源（如果需要构建任何可视化应用程序，如 wizard、warlock、mystic，则需要此资源）。

注意：只有当您将第三方资源和/或VTK资源放在.../swdev/dependencies以外的文件夹时，才需要更改这两个变量。

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

# UNCLASSIFIED

# 目标

![](images/1ea59e384ff025ecbffebe1fd228ce02558c21d58739fb54da025306808ba246.jpg)

![](images/3f8d81bf836493636ce7741301d852911f0c99074b11224b79e9f0b875d42702.jpg)

- CMake会生成多个可以构建的目标（targets），包括每个可执行文件、库以及测试集的目标。此外，以下目标非常重要：

- Windows 平台：

RUN TESTS   
运行单元测试。  
- INSTALL

- 生成安装目录（BUILD/wsf_install）。

- ALL Builds, ZERO_CHECK

由CMake自动为VisualStudio集成生成，可忽略。

Linux平台：

- tests   
运行单元测试。  
install

生成安装目录（BUILD/wsf_install）。

两种平台通用：

- <xxxx>_AUTO_TEST   
- 运行 <xxxx> 的系统集成测试（<xxxx> 可以是“engage”、“mission”、“sensor_plot”、“weapon.tools”之一）。  
- <xxxx> REGRESSION_TEST   
- 运行<xxxx>的回归测试（<xxxx>可以是“engage”、“mission”、“sensor_plot”、“weapon.tools”之一）。  
- DOCUMENTATION

构建Sphinx文档系统（面向用户）。

DOXYGEN

构建 Doxygen 文档（面向开发者）。

- 如果添加了新文件，则需要手动重新执行 CMake：

- 在 cmakeGUI 中按下“Generate”按钮，或者  
• 在构建目录中使用命令行运行: $ cmake ..

- CMake 在 Visual Studio 中的注意事项

- 如果修改了 CMakeLists.txt 文件，Visual Studio 会提示重新加载项目：

- 按下“Yes to All”按钮。  
- 在执行任何Git更新或显式修改CMakeLists.txt文件后，建议手动在cmake-gui中按下“Generate”按钮。

- CMake 在 Linux 中的注意事项

- 通常，只需运行 make 就足以更新 CMake 配置的更改。  
- 只有在添加新文件时，才需要显式调用 CMake。  
- 使用以下命令来解决构建问题：

make VERBOSE=1”

- 使用以下命令进行并行计算以加快构建速度：

make -j

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

# UNCLASSIFIED

# 其他问题 - Linux

21

![](images/3de079a3dcbe68cde169b7f0a2f8e1612a00be19fa5d42d2a22f6ad253793a1c.jpg)

![](images/355522276f5383d091f43782da3a15ac3d38fa8d731baa12a1c063319dc8e016.jpg)

Linux上的CMake使用指南

- 尽管可以在其他平台上使用 CMake，但整个构建过程也可以完全在 Linux 上完成。以下是具体步骤：  
- 在 swdev/build 文件夹中执行以下操作:

- 运行 cmake-api。  
- 确保源代码目录和构建目录设置正确。

- 假设 swdev/build 是构建目录，但您也可以创建其他文件夹用于构建，例如 swdev/DEBUG 或 swdev/SpecialBUILD 等。  
- 按下“Configure”按钮，然后按下“Generate”按钮。

- 进入构建目录，例如 swdev/build（或者如果您从 GitLab 下载了仓库，则进入 afsim_dev/build）  
- 如果您的笔记本/台式机有6个处理器核心（每个核心有2个虚拟处理器），可以在命令行中运行以下命令以进行并行构建：

$ cmake --build . --target all -- -j12

- 在构建目录中运行以下命令以进行安装:

$ cmake --build . --target install -- -j12

- 在构建目录中运行以下命令以执行单元测试:

$ cmake --build . --target test -- -j12

- 我们需要一个基于插件（dll）的 mission 版本用于实验室  
- Mission 是 AFSIM 的基础模拟应用程序

- 读取包含AFSIM命令的文本文件并执行模拟。模拟过程中推进时间、移动平台、做出决策以及执行对象之间的交互。

- 执行模式：

- 事件步进（Event-stepped）或帧步进（Frame-stepped）。  
非实时（Non-realtime）或实时（Realtime）。  
- 纯构造性模拟，包括多次蒙特卡洛迭代。  
- 作为分布式交互式模拟（DIS）演习的一部分。

- 使用 CMake 构建 AFSIM 可执行文件（如 mission）：

- 支持在Linux和Windows上使用相同的配置文件进行构建。  
- 也可以为其他平台构建（但未经过测试）。

- CMake 的优势，提供了简单的配置管理，能够轻松包含或排除功能模块。

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

# UNCLASSIFIED

![](images/e823944709ad0f7ef1d73f2a5976ab75cdab4434f446e558d67dc7d5c5ec6c22.jpg)

# 构建标准的AFSIM应用程序(1/8)

![](images/2f414a1f38b81a768f21ce44765c0c968408ad058f30de4d81ca6068334a9db1.jpg)

23

1. 确保您已从 DI2E 下载了 3rd_party 资源。  
2. 确保您已从 DI2E 下载了 vtk-resources.tar.gz 文件。  
3. 创建目录：.../swdev/dependencies。  
4. 创建目录：.../swdev/resources   
5. 将 3rdParty 目录移动到 ../swdev/dependencies 中。  
6. 将文件 vtk-resources.tar.gz 移动到 ../swdev/resources 中。

# 配置第一次构建

1. 导航到：.../training/developer/core/labs   
2. 编辑文件：config.cmake  
3. 设置 CMAKE_GENERATOR 变量（第 16-18 行）：

可选项包括：

Visual Studio 2017   
Visual Studio 2019   
- Unix Makefiles (Linux)

取消注释您希望使用的构建工具对应的那一行。  
注释掉您不需要使用的构建工具对应的行。

4. 如果选择了 Visual Studio 生成器：

取消注释第22行，设置CMAKEgeneratedATORPLATFORM变量。

5. 如果希望使用 Unity 构建训练项目：

取消注释第27和28行。

6. 设置构建目标（第34-55行）：

- 将您希望构建的目标的值从 FALSE 改为 TRUE。  
- 初始状态下，只有BUILD_WITH_mission被设置为TRUE。

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19.

Other requests for this document shall be referred to AFRL/RQQD.

# UNCLASSIFIED

![](images/67c4a3ccd21ddf354976efb8aefd55a6f3c6bf952c2eba8017c5989cd76485c3.jpg)

# 构建标准的 AFSIM 应用程序 (3a / 8)

![](images/5ac4a3252cf8f669809570d1427b4cd9518e7ffa3f1ee4a551c880b2e16a8be0.jpg)

- 开始第一次构建Mission!

- 打开一个 Windows 命令提示符窗口

- 适用于 AFSIM Release 的 Windows 命令（适用于 AFSIM 2.2202 或更高版本）：

导航到目录：...\AFSIM-2.x.x-zzz\training\developer\core\Labs

- 其中，2.x.x 是发布版本号，zzz 是文件夹名称中的其他部分。

- 执行以下命令:

> set scriptpath=%cd%\config.cmake   
> cd inwork   
> set expath=%cd%   
> cd ../\..\..\swdev/src   
> set srcpath=%cd%   
>cd..   
> mkdir build $\leftarrow$ 如果build目录已经存在则这一步不用  
>cd build   
> cmake -C %scriptpath% -DWSF_ADD Extensions_PATH:PATH=%extpath% -B . -S %srcpath%

- 开始第一次构建Mission!

- 打开一个 git-bash（Windows）、终端（Linux）或 xterm 窗口

- 适用于AFSIM Release的Bash命令（适用于AFSIM2.2202或更高版本）：

导航到目录：../AFSIM-2.x.x-zzz/training/developer/core/labs

- 其中，2.x.x 是发布版本号，zzz 是文件夹名称中的其他部分

- 执行以下命令:

```shell
$ scriptpath=$PWD/config.cmake
$ cd inwork
$ expath=$PWD
$ cd ../../../swdev/src
$ srcpath=$PWD
$ cd ..
$ mkdir build 但是如果build目录已经存在则不用该命令
$ cd build
$ cmake -C $scriptpath -DWSF_ADD_EXTENSION_PATH:PATH=$extpath -B . -S $srcpath 
```

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

27

![](images/4224e1d7f86e0c094eb599348473bb3f760f1317ce4144fc03ad7577e7a5cd4b.jpg)

# UNCLASSIFIED

# 构建标准的 AFSIM 应用程序 (4a / 8)

![](images/95538b3dde7d2cd75ad1df6a50e00717d5577221ac05c7e5d390f08821d45f9a.jpg)

- 开始第一次构建 Mission!

- 打开一个 Windows 命令提示符窗口

- 适用于AFSIM开发者的Bash命令:

- 导航到目录: ../afsim_dev/training/developer/core/labs   
- 执行以下命令:

```txt
$ set scriptpath=%cd%\config.cmake
$ cd inwork
$ set expath=%cd%
$ cd ../\..\\..\\.\.afsim
$ set srcpath=%cd%
$ cd ../training\developer
$ mkdir build ←———如果构建目录已存在,则此步骤不必要
$ cd build
$ cmake -C %scriptpath% -DWSF_ADD Extensions_PATH:PATH=%extpath% -B . -S %srcpath% 
```

- 开始第一次构建 Mission!

- 打开一个 git-bash（Windows）、终端或 xterm（Linux）窗口

- 适用于AFSIM开发者的Bash命令:

- 导航到目录: ../afsim_dev/training/developer/core/labs   
- 执行以下命令:

$ scriptpath=$PWD/config.cmake   
$ cd inwork   
$ extpath=$PWD   
$ cd ../../../..//afsim   
$ srcpath=$PWD   
$ cd ../training/developer   
$ mkdir build ←——— 如果构建目录已存在, 则此步骤不必要  
$ cd build   
$ cmake -C $scriptpath -DWSF_ADD Extensions_PATH:PATH=$extpath -B . -S $srcpath

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19.

Other requests for this document shall be referred to AFRL/RQQD.

# UNCLASSIFIED

![](images/a953c3cec674880ef74573a2fdd000a397b50adccaf30509220dc3b1c6a6d93c.jpg)

# 构建标准的AFSIM应用程序(5/8)

![](images/c8ec4e54ececc661fc1ee354e55e30bfafce9fcde90dd08cbb206933210cbfc1.jpg)

- 之前的 CMake 命令将会执行以下操作:

修改构建目标，仅构建Mission可执行文件。  
- 运行 CMake 以生成一个 CMakeCache 文件。  
- 启动 CMake GUI: .../swdev/build/ (或 .../afsim_dev/training/developer/build)   
- 验证“Where is the source code”（源代码位置）是否已从缓存更新为：.../swdev/src/

(或.../afsim_dev/training/developer/build)

- 检查 CMake 选项：

确保选中

WSF_PLUGIN Builds

- WSF_ADD ExtensionsPATH 应指向：

# .../core/labs/inwork

此时，唯一应选中的构建选项是

BUILD_WITH_mission。

特别地，所有训练练习应保持未选中状态。

如果您进行了任何更改，请点击“Configure”（配置），然后点击“Generate”（生成）。

![](images/49b5e5a35687bed8fb38332f9bd996889c5bf26d37e5c7dad4592cb11a2edb69.jpg)

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

UNCLASSIFIED

# 构建标准的AFSIM应用程序(7/8)

![](images/734146029de9ad84db029b88cd43328a52f97f5ef64367491ba168089e407b7d.jpg)

![](images/89f2ea2e84c2fc43f1f791f57b8f75979f22c27a838e99cc00ffcf4b4a9a9c3d.jpg)

# Windows:

- 从 Windows 资源管理器中，双击“afsim.sln”解决方案文件，路径为：

"...swdev/build/"

或者，在 CMake-GUI 中按“Open Project”（打开项目）按钮

- 在 Visual Studio 中，从 GUI 顶部的下拉菜单中选择“Release”构建

- 如果不这样做，默认将以调试模式构建，这会显著延长构建时间，并且执行时间也会显著增加

- 在 Visual Studio 中构建解决方案（这将花费大约 20-30 分钟）

- 选择菜单项 Build -> Build Solution（或使用快捷键 F7）

- 构建 INSTALL 项目

- 这将把标准的WSF应用程序安装到.../build/wsf_install/bin目录中的“bin”文件夹内（CMAKE Installation_PREFIX）

# Linux:

- 使用 CMake GUI 确保 CMAKE.Build_TYPE 设置正确:

确保变量 CMAKE-built_TYPE 设置为 Release（仅适用于 Linux）。  
- 如果该变量设置为 debug，CMake 将以调试模式构建，这会显著延长构建时间，并且执行时间也会显著增加。

·构建解决方案（这将花费大约20-30分钟）：

- 在Linux终端（或xterm）中，在构建目录（“../swdev/build”或“../afsim_dev/training/developer/build”）中执行以下命令$ cmake -build . -target all -- -j12  
- 注意：-j12 选项使 CMake 以最多 12 个并行线程进行多线程构建（使用的数字应与系统中的处理器/核心数量相同）

- 构建install目标：

- 在 Linux 终端 (或 xterm) 中, 在构建目录中执行以下命令$ cmake -build . -target install -- -j12  
- 这将把标准的WSF应用程序安装到.../build/wsf_install/bin目录中的“bin”文件夹内

within ../build/wsf_install/bin (CMAKEInstall Prefix) DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQQD.

UNCLASSIFIED

![](images/b72d5ce5f0d2454ed49a4c289138aeea1ac499afcb72302a35abb9b100f34c8b.jpg)

# 关于构建AFSIM 培训练习的注意事项

![](images/deca8f0a1701496ed3885052f968427a0dd97d5661601a7515e56e53db028f3e.jpg)

- 如果您想构建练习，有两种选择：

- 运行 cmakeGUI

- 手动开启您想要构建的目标。  
- 然后点击“Configure”（配置）和“Generate”（生成）。

修改 config.cmake 文件

- 编辑core/labs或wkf/labs目录中的config.cmake文件。  
- 将您想要构建的目标设置为 TRUE。  
- 删除构建目录中的 CMakeCache.txt 文件。  
- 按照构建幻灯片中的命令执行（第1-8步，幻灯片24-31）。

- 但请注意，不要执行创建构建目录的 mkdir 命令

![](images/065fa50e5cb61c347b7beea5eaa109ea4e2e92319bc867a5da8ed77e6b927ffd.jpg)

![](images/5adfb5ec6c8a017edc87140cd9eae6db69b4868550de77babc63cb870b9bf7f8.jpg)

UNCLASSIFIED

35

![](images/6e1ce30414368ffc3bc88dac4a2322ba44ba6a3523a82ceb940bc37d99ac000b.jpg)

![](images/b617a02ff19603ae85f0bd9c1ba35568f944c6badd4084bbf25b5f1cddd7a44b.jpg)

Integrity $\star$ Service $\star$ Excellence

AFSIM开发培训

0 - 使用CMAKE构建

附录

AFRL/RQQD

1. 运行 cmake-gui。  
2. 将“Where is the source code”（源代码位置）文本框设置为 swdev/src 目录：

您可以手动输入路径，或者点击“Browse Source...”（浏览源代码）按钮，导航到该目录并点击“Select Folder”（选择文件夹）。

3. 将“Where to build the binaries”（二进制文件的构建位置）文本框设置为swdev/build 目录：

- 您可以手动输入路径，或者点击“Browse Build...”（浏览构建）按钮，导航到该目录并点击“Select Folder”。

4. 点击“Configure”按钮（这将执行初始配置并构建缓存文件）。  
5. 如果系统要求您选择生成器，请选择×64。

![](images/1e66aa94c2323649db09225d7e161641f613c540729fdf697aa6ade68cc71be6.jpg)

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

# UNCLASSIFIED

37

![](images/27380ee248e216f3afba7a683847889fddbc35de425a44b96088a27f2d77179b.jpg)

# 如果我想从头开始构建 … (2/5)

![](images/ce5345892f580b235db8aa40f22566bb8821606a6e67f38c9937367f76208717.jpg)

6. 在搜索栏下方的大白框中，导航到WSF组标签，并点击WSF左侧的箭头“>”。  
7. 第一个条目是WSF_ADD_EXTENDED_PATH。这个变量没有关联的值。点击该行的值列，输入训练文件夹的路径：：.../training/developer/core/labs/inworK  
8. 点击“Configure”按钮（这将执行另一次配置并重建缓存文件——将练习构建变量添加到配置中）

![](images/1d3747ba6f6855272c13e60aa6ff643788a4089b44ac035ac732e5b44583747e.jpg)

9. 点击所有BUILD组标签旁边的箭头“>”。

9. 可能会有多个BUILD组。

10. 手动勾选或取消勾选所有感兴趣的构建目标的框。  
11. 再次点击“Configure”按钮以设置最终配置。  
12. 点击“Generate”按钮以生成构建。

![](images/99c4f08c5a4eaf9ae8283b4a1e17d207117321586508d0884873a237fef96158.jpg)  
DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

# UNCLASSIFIED

39

![](images/423b3df74866ed3e3e73075bec2fd5510b908256ba4d748ee36b2f8b21f02e13.jpg)

# 如果我想从头开始构建 … (4/5)

![](images/2fcba404ce7c1fc9dedc2e559a1547c2a46113f036c3cb32807b9f017a1a0e89.jpg)

# 13. 编译构建：

- 在Windows上：  
1. 运行 Visual Studio。  
2. 点击 File > Open > Project/Solution，在对话框中导航到构建目录，双击文件afsim.sln。  
3. 确保构建设置为 Release。  
4. 点击：

Build $>$ Build Solution.

5. 在解决方案资源管理器中找到INSTALL目标，右键点击INSTALL并在菜单中选择Build。

DISTRIBUTION C. Distribution authorized to U.S. Other requests for this docum

![](images/ad7a04e91aeb09cd82377fbbbf71cb3482ba168e56b3fd8baef8b7ed1c41102f.jpg)

# 13. 编译构建：

b) 在Linux终端窗口中:

i. 切换到swdev/build目录   
ii. 执行以下命令：

```txt
> cmake --build . --target all -- -j<n>, 中 <n> 是您系统中的处理器数量
```

iii. 执行以下命令以构建安装目标:

> cmake --build . --target install -- -j<n>,其中 $<  n>$ 也是您系统中的处理器数量

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

# 6.2.1.4. Mission 概览 3_AFSIM_Trng_MissionOverview

本文为afsim2.9_src\training\developer\core\slides\

3_AFSIM_Dev_Trng_MissionOverview.pptx 的翻译，主要是对 Mission 的代码进行解析，使用户熟悉和掌握 Mission 代码结构。

![](images/17a3cf893bcc1a8cb1e2c58148ec9012836d401b55cb7464a6d9443eaee1ea62.jpg)

Integrity $\star$ Service $\star$ Excellence

# AFSIM开发培训

# 3 - Mission介绍

本文档由杨石兴翻译，该资料做为《AFSIM2.9参考手册》的一部分。没有《AFSIM2.9参考手册》的加杨石兴微信领取：13324598743

# AFRL/RQQD 美国空军研究实验室

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

UNCLASSIFIED

![](images/d5bdc6369265225f90bfc94d774d3a0d0dba115357b421cf3fd4e912374bf4aa.jpg)

# 任务

![](images/9d4689218d2e3648845adf8c9a4527759e3a93b475d0ea3c8d1389c9ba68523d.jpg)

1

- 理解mission.cpp (located in swdev/src/mission/source)   
- WsfStandardApplication 的创建：了解如何实例化和配置 WsfStandardApplication，以便为应用程序提供标准化的功能和接口。  
- 内置和可选扩展的注册：查看如何注册内置的扩展模块以及可选的扩展，以增强应用程序的功能。  
- 场景创建：理解场景的构建过程，包括如何设置和初始化场景中的元素。  
- 命令行选项和输入文件的处理：分析如何解析命令行参数和输入文件，以便根据用户的输入配置应用程序。

- 平台列表的构建：了解如何生成可用平台的列表，以便在模拟过程中进行选择和管理。

- 模拟初始化：查看模拟的初始化过程，包括必要的设置和资源分配。  
- 模拟启动：理解模拟启动的步骤，确保所有组件准备就绪以开始执行。  
- 模拟执行：分析模拟的执行过程，包括主要的逻辑和循环。

- 事件处理：了解如何处理在模拟过程中发生的事件，以确保系统的响应和交互。  
- 可选帧步骤：查看可选的帧步骤功能，允许在模拟中进行逐帧控制。  
- 蒙特卡洛：理解蒙特卡洛方法的实现，通常用于不确定性分析和概率模拟。

- 模拟终止：分析模拟结束时的清理和资源释放过程，以确保系统的稳定性。

- 创建标准应用程序  
注册扩展  
- 处理命令行选项   
- 创建场景  
- 处理所有场景输入文件  
- 处理任何命令行命令  
- 创建模拟  
- 执行模拟

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

3

![](images/6f84c4b54930e42339749c8a0bb599ce5865b1e83ec04d98dabd9b7c3926a467.jpg)

# mission.cpp

![](images/7f761274a00df839ad905703193afb99aab8a8ba73716a62de30d46118547c54.jpg)

int main(int argc, char* argv[])  
{ WsfStandardApplication app("mission", argc, argv);

// Load built-in extensions (defined in wsf_extensi RegisterBuilttinExtensions(app);

// Load optional extensions (defined in wsf_extensi RegisterOptionalExtensions(app);

// Register the XIO simulation interface.  
WSFRegisterExtension(app, xio-interface);

// Process command-line arguments WsfStandardApplication::Options options;

try { app.ProcessCommandLine(options); } catch (WsfApplication::Exception& e) { std::cout << e.what() << std::endl; return e.GetReturnCode(); }

// Create a scenario   
WsfScenario scenario(app);   
try { // Read WSF input files into the scenario app.ProcessInputFiles(scenario, options.mInputFiles); }

1. 创建WsfStandardApplication对象

2. 注册扩展  
3.5处理命令行  
4. 创建WsfScenario对象  
5.读取想定涉及的所有.txt文件  
6. 处理可能的命令行参数  
7. 开始仿真循环

a.(使用循环)对于在需要仿真循环次数的每次仿真：

I. 创建下一个 WsfSimulation 对象以运行下一个模拟  
II. 初始化模拟对象  
III. 运行事件循环（导致模拟执行）  
IV. 增加runNumber

8. 退出

```txt
int main(int argc, char\* argv[]) WsfStandardApplication app("mission", argc, argv); 
```

```txt
// Load built-in extensions (defined in wsf_extens: RegisterBuiltInExtensions(app); // Load optional extensions (defined in wsf_extens: RegisterOptionalExtensions(app); 
```

```txt
// Register the XIO simulation interface.  
WSFRegisterExtension(app, xio-interface); 
```

```cpp
// Process command-line arguments
WsfStandardApplication::Options options; 
```

```cpp
try   
{ app.ProcessCommandLine(options);   
}   
catch (WsfApplication::Exception& e)   
{ std::cout << e.what() << std::endl; return e.GetReturnCode();   
} 
```

```txt
// Create a scenario
WsfScenario scenario(app); 
```

```javascript
try { // Read WSF input files into the scenario app.ProcessInputFiles(scenario, options.mInputFiles); } 
```

![](images/c4b25f63595163ec494d8514b8e4b5749652117cf61865de2afd58859f76aed2.jpg)

# UNCLASSIFIED

# Mission

1. 创建WsfStandardApplication对象  
2. 注册扩展  
3. 处理命令行  
4. 创建WsfScenario对象  
5.读取想定涉及的所有.txt文件  
6. 处理可能的命令行参数  
7. 开始仿真循环

a.(使用循环)对于在需要仿真循环次数的每次仿真：

I. 创建下一个 WsfSimulation 对象以运行下一个模拟  
II. 初始化模拟对象  
III. 运行事件循环（导致模拟执行）

IV. 增加 runNumber

8. 退出

![](images/8133955d3a2083f13b46c5ecb7383975dbb262cda31eef690e5adcb0f90ced6d.jpg)

```txt
int main(int argc, char\* argv[]) 1.包 WsfStandardApplication app("mission", argc, argv); 2.注 //Load built-in extensions (defined in wsf_extensi3.s RegisterBuiltinExtensions(app); 4.包 //Load optional extensions (defined in wsf_extensi5. registerOptionalExtensions(app); 6.处 //Register the XIO simulation interface. WSFREGISTERExtension(app,xio-interface); 7.开 
```

```cpp
// Process command-line arguments
WsfStandardApplication::Options options;
try
{
    app.ProcessCommandLine(options);
}
catch (WsfApplication::Exception& e)
{
    std::cout << e.what() << std::endl;
    return e.GetReturnCode();
} 
```

```txt
// Create a scenario
WsfScenario scenario(app); 
```

1. 创建WsfStandardApplication对象  
2. 注册扩展  
3.处理命令行  
4. 创建WsfScenario对象  
5. 读取想定涉及的所有.tx  
6. 处理可能的命令行参数  
7. 开始仿真循环

a.(使用循环)对于在需要仿真循环次数的每次仿真：

I. 创建下一个 WsfSimulation 对象以运行下一个模拟  
II. 初始化模拟对象  
III. 运行事件循环（导致模拟执行）  
IV.增加runNumber

8.

退出

```javascript
try { // Read WSF input files into the scenario app.ProcessInputFiles(scenario, options.mInputFiles); } 
```

int main(int argc, char\* argv[]) 1.创建WsfStandardApplication对象   
{ WsfStandardApplication app("mission", argc, argv); 2.注册扩展   
//Load built-in extensions (defined in wsf.extensi; 3.处理命令行   
RegisterBuiltinExtensions(app); 4.创建Wsfscenario对象   
//Load optional extensions (defined in wsf.extensi; 5.读取想定涉及的所有.txt文件   
RegisterOptionalExtensions(app); 6.处理可能的命令行参数   
//Register the XIO simulation interface. WSF REGISTER EXTENSION(app, xio_interfca)； 7.开始仿真循环 a.(使用循环)对于在需要仿真循环次数 的每次仿真： I.创建下一个WsfSimulation对象 以运行下一个模拟 II.初始化模拟对象 III.运行事件循环（导致模拟执行） IV.增加runNumber   
//Process command-line arguments WsfStandardApplication::Options options;   
try { app.ProcessCommandLine(options); catch (WsfApplication::Exception& e) std::cout<<e.what()<<std::endl; return e.GetReturnCode(); } UNCLASSIFIED   
//Create a scenario WsfScenario scenario(app);   
try { //ReadWSFinputfilesinto the scenariopapp.ProcessInputFiles(scenario, options.mInputFiles);   
}   
//Create a scenario WsfScenario scenario(app);   
try { //Read WSF input files into the scenariopapp.ProcessInputFiles(scenario, options.mInputFiles); catch (WsfApplication::Exception& e) std::cout<<e.what()<<std::endl; return e.GetReturnCode(); }   
app.ProcessCommandLineCommands(scenario, options);   
int errorCode $= 0$ . 8退出 if(options.mRunMode $\equiv$ WsfStandardApplication::CRU.SCE) //Loop while Monte-Carlo runs remain to be executed or an external controller has not told us to for(unsigned int runNumber $\equiv$ scenario.GetInitialRunNumber(); runNumber $\Leftarrow$ scenario.GetFinalRunNumDISTRIBUTION.C.Distributionauthorized to U.S.GovernmentAgencies and their contractors,9-Aug-19. Other requests for this document shall be referred to AFRL/ROQD.

：

1. 创建WsfStandardApplication对象  
2. 注册扩展  
3. 处理命令行  
4. 创建WsfScenario对象  
5. 读取想定涉及的所有.txt文件  
6. 处理可能的命令行参数  
7. 开始仿真循环

a.(使用循环)对于在需要仿真循环次数的每次仿真：

I. 创建下一个 WsfSimulation 对象以运行下一个模拟  
II. 初始化模拟对象  
III. 运行事件循环（导致模拟执行）  
IV. 增加 runNumber

8.SCE退出

```cpp
// Create a scenario
WsfScenario scenario(app);
try
{
    // Read WSF input files
    app.ProcessInputFiles(s);
}
catch (WsfApplication::Exce
{
    std::cout << e.what() << return e.GetReturnCode(
} 
```

```javascript
app.ProcessCommandLineCommands(scenario, options); 
```

```txt
int errorCode = 0;  
if(options.mRunMode == WsfStandardApplication::cRU8_SCEN)  
{ // Loop while Monte-Carlo runs remain to be executed or an external controller has not told us to for (unsigned int runNumber = scenario.GetInitialRunNumber(); runNumber <= scenario.GetFinalRunNumDISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQQD. 
```

# UNCLASSIFIED

![](images/4af318160d077d40e6d63a91e865f09112f28670f973f97f0a799144b749eae9.jpg)

# Mission

![](images/569828550073325727d95abd159c82598866a2922ee61c8e93a4c6654855b83c.jpg)

中

1. 创建WsfStandardApplication对象  
2. 注册扩展  
3. 处理命令行  
4. 创建WsfScenario对象  
5. 读取想定涉及的所有.txt文件  
6. 处理可能的命令行参数

7. 开始仿真循环

a.(使用循环)对于在需要仿真循环次数的每次仿真：

I. 创建下一个 WsfSimulation 对象以运行下一个模拟  
II. 初始化模拟对象

III. 运行事件循环（导致模拟执行）

INSCENV.增加runNumber

8. 退出

app.ProcessCommandLineCommands(scenario, options);

```txt
int errorCode = 0; 
```

```txt
if(options.mRunMode == WsfStandardApplication::cRUN_SCENARIO) 
```

(1)

```txt
// Loop while Monte-Carlo runs remain to be ex 
```

```txt
for (unsigned int runNumber = scenario.GetInit; 
```

```txt
1. 创建WsfStandardApplication对象
```

```txt
2. 注册扩展
```

```txt
3. 处理命令行
```

```txt
4. 创建WsfScenario对象
```

```txt
5. 读取想定涉及的所有.txt文件
```

```txt
6. 处理可能的命令行参数
```

```txt
7. 开始仿真循环
```

a.(使用循环)对于在需要仿真循环次数的每次仿真：

I. 创建下一个 WsfSimulation 对象以运行下一个模拟

II. 初始化模拟对象

III. 运行事件循环（导致模拟执行）

IV. 增加 runNumber

8.

![](images/7932e77ff6aa3091d1796d02561698e49eddbfc4fd72da2a9f9b003be1952f94.jpg)

# UNCLASSIFIED

# Mission

![](images/5d8c09a569d2ed318c9bd0236278f9c1cb7d43363e86457edbb3efddd5efe7bc.jpg)

```javascript
app.ProcessCommandLineCommands(scenario, options); 
```

```txt
int errorCode = 0; 
```

```txt
if(options.mRunMode == WsfStandardApplication::cRUN_SCENARIO) 
```

```txt
// Loop while Monte-Carlo runs remain to be executed or an external controller has not told us to do so for (unsigned int runNumber = scenario.GetInitialRunNumber(); runNumber <= scenario.GetFinalRunNumber); 
```

```cpp
std::unique ptr<WsfSimulation> simPtr = app.CreateSimulation(scenario, options, runNumber); 
```

```txt
if (!app.InitializeSimulation(simPtr.get())) 
```

errorCode $= 1$

```txt
break; 
```

1

```txt
// If given no inputs, quit now 
```

```txt
if(options.mInputFiles.empty()) 
```

{

```txt
break; 
```

1

```txt
WsfStandardApplication::SimulationResult result 
```

try

result $=$ appRUNEventLoop(simPtr.get(),options)

```txt
} 
```

```batch
catch (UtException& e) 
```

```txt
1 
```

```cpp
std::cout << e.what() << std::endl; 
```

errorCode $= 1$

```txt
break; 
```

```txt
1. 创建WsfStandardApplication对象
```

```txt
2. 注册扩展
```

```txt
3. 处理命令行
```

```txt
4. 创建WsfScenario对象
```

```txt
5. 读取想定涉及的所有.txt文件
```

```txt
6. 处理可能的命令行参数
```

```txt
7. 开始仿真循环
```

a. (使用循环) 对于在需要仿真循环次数的每

次仿真：

I. 创建下一个 WsfSimulation 对象以运行下一个模拟

II. 初始化模拟对象

III. 运行事件循环（导致模拟执行）

IV. 增加 runNumber

··

app.ProcessCommandLineCommands(scenario, options);

int errorCode $= 0$ if(options.mRunMode $\equiv$ WsfStandardApplication::cRUN_SCENARIO)

$\left\{  {1,2,3}\right\}   \Rightarrow  \;\left\{  {1,3,4}\right\}   \Rightarrow  \left\{  {2,3,4}\right\}   \Rightarrow  \left\{  {3,4,5}\right\}   \Rightarrow  \left\{  {4,5,6}\right\}   \Rightarrow  \left\{  {5,6}\right\}   \Rightarrow  \left\{  {6,7}\right\}   \Rightarrow  }$

```cpp
// Loop while Monte-Carlo runs remain to be executed for (unsigned int runNumber = scenario.GetInitialRundersNum <= scenario.GetFinalRunNum) 3. 注册扩展 3. 处理命令行 std::unique_ptr<WsfSimulation> simPtr = app.CreateSimulator(scenario, options, runNumber); if (!app.InitializeSimulation(simPtr.get())) 4. 创建WsfScenario对象 errorCode = 1; 5. 读取想定涉及的所有.txt文件 break; 6. 处理可能的命令行参数 7. 开始仿真循环 if (options.mInputFiles.empty()) a.(使用循环)对于在需要仿真循环次数的每次仿真： break; I. 创建下一个 WsfSimulation 对象以运
```

```txt
WsfStandardApplication::SimulationResult result; 
```

```txt
try 
```

$\left\{  \begin{array}{l} \text{①}\;\text{若}\sin \alpha  = 1 \\  \text{若}\sin \alpha  < 1\;\text{且}\alpha  > 0 \end{array}\right.$

```javascript
result = app.runEventLoop(simPtr.get(), options); 
```

```txt
1 
```

```batch
catch (UtException& e) 
```

$\left\{  \begin{array}{l} \text{①}\;\text{若}\overrightarrow{a} = m\overrightarrow{a},\overrightarrow{b} = n\overrightarrow{a} \\  \text{若}\overrightarrow{a} + \overrightarrow{b} = c\overrightarrow{a} \end{array}\right.$

```cpp
std::cout << e.what() << std::endl; 
```

errorCode $= 1$

```txt
break: 
```

1. 创建WsfStandardApplication对象  
2.注册扩展runNumber $\Leftarrow$ scenario.GetFinalRunNumber   
3. 处理命令行  
4.创建WsfScenario对象  
5. 读取想定涉及的所有.txt文件  
6. 处理可能的命令行参数  
7. 开始仿真循环

a.(使用循环)对于在需要仿真循环次数的每次仿真：

I. 创建下一个 WsfSimulation 对象以运

# 行下一个模拟

II. 初始化模拟对象

III. 运行事件循环（导致模拟执行）

IV. 增加runNumber

8.

![](images/588462138093758b213d0907f92a746ada547a2ac35c2a43734b14903163c253.jpg)

![](images/d9f88411cb43a7de86b72a5a144b88f4264286d8eaf71b134d6347cdb31c7ce0.jpg)

# UNCLASSIFIED

# Mission

![](images/08ecb958283cd793189584ec53ed28cfadc79517758c5dd365ee85210a109992.jpg)

![](images/7d0cdc9ed28b6c31df1acd1bb950a393b4646b661d51532b32e574eb07a6e759.jpg)

```txt
WsfStandardApplication::SimulationResult result 
```

```txt
try 
```

$\left( {x - 1}\right) \left( {x + 3}\right)  = 0$

result $=$ app.runEventLoop(simPtr.get(),opt

```txt
1 
```

```batch
catch (UtException& e) 
```

$\left\{  \begin{array}{l} \text{①}\;\left( {0 < x}\right)  \Rightarrow  x \in  \left( {{2x} - 1,2{x}^{2} + x}\right) \\  \text{②}\left( {0 < x}\right)  \Rightarrow  x \in  \left( {{2x} + 1,{2x} + 3}\right)  \end{array}\right.$

```cpp
std::cout << e.what() << std::endl; 
```

errorCode $= 1$

```txt
break; 
```

```txt
1 
```

1. 创建WsfStandardApplication对象  
2. 注册扩展  
3. 处理命令行  
4. 创建WsfScenario对象  
5. 读取想定涉及的所有.txt文件  
6. 处理可能的命令行参数  
7. 开始仿真循环

a.(使用循环)对于在需要仿真循环次数的每次仿真：

I. 创建下一个 WsfSimulation 对象以运

# 行下一个模拟

II. 初始化模拟对象  
III. 运行事件循环（导致模拟执行）  
IV. 增加runNumber

```javascript
} return errorCode; 
```

8. 退出

![](images/36bde0c72654cc6e572bf11ff64884d596905ab141872c178afd369cd36f3918.jpg)

- 创建场景

加载一个场景。

- 调用所有的ProcessInput方法

- 使用组件工厂（component factories）实例化所有组件、其他对象、平台和平台组件。

- 使用 UtlInputBlock::ProcessInput 方法处理一个块输入

- Utlnput

- 提供实用方法，例如 ReadCommand、ReadValue、ReadString、ReadUnitValue 和 ReadValueOfType。

- UtInputBlock

- 与 Utlnput 一起使用，用于处理块中的所有命令（块以 end_<blockname> 结束）。

- ProcessInput 方法

用于处理输入。

![](images/5d96a5e51a34454a1cb86a11e4ae2563e14cf2ba8f16ebd3aa4203596da1e057.jpg)  
DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQQD.

17

![](images/71b32ac9575f64e747a387fff035170a94396dde7fc058f62855a0fdf1caee60.jpg)

# UNCLASSIFIED

# 读取想定文件

![](images/85e1009d8ee173bce7ac543bdd13b7583c83f2368317736f5d2f551a03e93c73.jpg)

- Utlnput

- 提供实用方法，例如 ReadCommand、ReadValue、ReadString、ReadUnitValue 和 ReadValueOfType。

- UtlnputBlock

- 与 Utlnput 一起使用，用于处理块中的所有命令（块以 end_<blockname> 结束）。

- ProcessInput 方法

- 用于处理输入。

# From UtlnputBlock class

```txt
template<class T> void ProcessInput(T* aObjectPtr) {
    while (ReadCommand())
    {
        if (!aObjectPtr->ProcessInput(mInput))
            {
                ThrowUnknownCommandException();
            }
        }
} 
```

一旦我们确定了输入块的开始位置以及将处理该块的对象，就可以为该输入创建一个UtlInputBlock，并调用其ProcessInput方法。

处理块中的所有命令，并为负责处理该块命令的对象调用其关联的ProcessInput方法。

注意：ProcessInput是特定于任务的——不要将其与由Wizard使用的WsfParser类混淆。

![](images/d0963e39feb10b28ed29e68aa47341c07b9b8ab0dd3dbd0e4b5e978ef14842f6.jpg)  
DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQQD.

19

![](images/4997efa8cd7a8d786215d45581da44bc35a68045c5928a8a98f1801db691875d.jpg)  
UNCLASSIFIED

# Initialize

![](images/1affb2dcfc2ca3dad549a04fb1d5b162e68e9e6e23bf294608b9e7f97a219153.jpg)

![](images/f33a7d77990e37d273120caa0974e0102be9fa83e4486bc295564b89da7cbd29.jpg)  
DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

20

![](images/5a735cb11c98e83c89cb21d832a636124fdd3f60979fe618ad018882edc01511.jpg)

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

21

![](images/aa35486dcff7fe6dbf04098d1bc7f1ec29b0974bb95044ac041002811dd80c95.jpg)

![](images/76bb0f700078f0c2cba05519a1c45b58d1358b51ee16b726ab5892a3c855069e.jpg)

UNCLASSIFIED

![](images/14dc346b6060e1e7835d383708e1a67790354bf02669844e46c3cb6c727f8e32.jpg)

# 6.2.1.5. 传感器4_AFSIMDev_Trng_Sensors

本文为afsim2.9_src\training\developer\core\slides\

4_AFSIMDev_Trng_Sensors.pptx的翻译，主要是介绍如何扩展自定义传感器，并做了许多小练习。

![](images/979c228dd5241208dc677a8fc5a012484ec209e2337e0b83d06e7de004870c49.jpg)  
Integrity ★ Service ★ Excellence

# AFSIM开发培训

# 4-传感器

本文档由杨石兴翻译，该资料做为《AFSIM2.9参考手册》的一部分。没有《AFSIM2.9参考手册》的加杨石兴微信领取：13324598743

# AFRL/RQQD 美国空军研究实验室

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQQD.

1

![](images/025fe5779d1d27a96d0ada6649f54d24f1265245a7b3ce9b77f2d89ba08965b2.jpg)

# UNCLASSIFIED

# 术语和定义

![](images/934bdd3ddf07db226a2415f3c8672423331a3a1e588d7b34e9d45b85b858b458.jpg)

AFSIM - Advanced Framework for Simulation, Integration, and Modeling

AGL - Above Ground Level

DIS - Distributed Interactive Simulation

DTED - Digital Terrain Elevation Data

EO/IR - Electro-Optical/Infra-Red

ESM - Electronic Support Measure

FOV - Field Of View

GUI-Graphical User Interface

HLA-High Level Architecture

IEEE - Institute of Electrical & Electronics Engineers, Inc.

JTIDS - Joint Tactical Information Distribution System

MSL - Mean Sea Level

PDU - Protocol Data Unit

RCS - Radar Cross Section

SAM - Surface-to-Air Missile

SAR - Synthetic Aperture Radar

VESPA - Visual Environment for Scenario Preparation and Analysis

WKF-Warlock Framework

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

- 本实验演示了如何创建一个新的AFSIM传感器。  
- 传感器是一个表示感知系统的可调节平台部件。  
- 您将创建一个需要跟踪器和调度器的传感器，并且该传感器将具有多种模式。  
- 以下练习提供了操作AFSIM传感器的实践机会：

- 练习1：了解AFSIM插件和扩展  
- 练习2：创建一个自定义AFSIM传感器  
- 练习3：创建一个自定义AFSIM传感器脚本接口

![](images/523f97bb678b569b8222c26da6683a88dd0e1c9914af30066c29e2f5244732a0.jpg)

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQDD.

3

![](images/8a2e777e2e7c96f405b7ae986bea958bf1ff8f97c992150707a3e608d12257d5.jpg)

# UNCLASSIFIED

# 问题陈述

![](images/fc5948c90857796ed2f5ae7e8af1719751c3018133f7dfa9efdd918ee3c90325.jpg)

- 三录仪（Tricorders）是《星际迷航》（Star Trek）电视系列中虚构的传感器  
- 创建一个新的AFSIM传感器类型，命名为TRICORDER_SENSOR。  
- TRICORDER_SENSOR 应具备以下功能:

- 检测并跟踪“生命形式”  
- 识别特定类型的生命形式  
评估每种生命形式的健康状况

# 参考：

- AFSIM 开发者基于网络的数据  
- AFSIM源代码和Visual Studio搜索功能  
- AFSIM文档

![](images/54ffc1d7e1878b0967f0da2de5fd16633099a7b2f1bb40bd587adbb2cca34518.jpg)

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19.

Other requests for this document shall be referred to AFRL/RQQD.

- 您将获得以下方面的实践知识:  
- 创建一个应用扩展

- 支持新的脚本类型所需的内容

- 创建一种新类型的传感器  
- 为单模式被动传感器实现 AttemptToDetect 方法  
- 实现 UpdateTrack 方法以设置生命形式的跟踪数据  
- 使用平台类型和类别来识别生命形式  
- 使用平台损伤信息作为健康指标  
- 为新传感器创建并使用脚本类

![](images/8a93a5e912a4dbbf12804e50b5a7efb6f78d314bc6cef63edcf50c64bb80b833.jpg)

5

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQDD.

UNCLASSIFIED

![](images/359387d804016a89582ff063359bd8ab32a18c2b4c039c6a597b8caccd394fa6.jpg)

# 先决条件

![](images/4fb46aac553d3bce0455574b3f0956b1c3fd1f8b870d5fa7f66a1f39f25dde67.jpg)

- 在进行本实验之前，您应该：

- 熟悉 WIZARD 和 AFSIM 脚本语言

- 建议参加过AFSIM分析课程或具有同等经验

- 能够使用并熟悉 Microsoft® Visual Studio 2017® 或更新版本，用于编译应用程序  
- 熟悉使用 Microsoft Windows® Explorer  
- 已完成模块“使用 CMAKE 构建 AFSIM”

- 熟悉使用 cmakeGUI  
- 熟悉执行 cmake（如果在 Linux 上开发）

- AFSIM 在其基本框架中包含了一套强大的传感器选项。  
- 通过使用 $\mathrm{C} + +$ 架构，开发人员可以扩展类以创建新的传感器或新的传感器行为。

![](images/917e2a0c80fd1da78cb5c4c119dccac3a08a6cc4faf0cb0a6aaac39a23b09626.jpg)

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQDD.

7

![](images/f0780a318d270acdcd94e23492ff0e015c1c90cac1bed6edb5dd41ecdf49d008.jpg)

# UNCLASSIFIED

# 传感器

![](images/9058b08f28351b8ba988c5e302f916c94ca5ed53f8b4676ad3254dab86fe10a2.jpg)

- “传感器”是一个可调节的部件，用于检测操作环境中的某些事物。  
- 下面展示了AFSIM中WsfSensor的基本类结构图。

![](images/d75fc1e90908259424ce1ce1d811b4c605828aa3b6448a10c551bb62fc85565b.jpg)

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQDD.

- 传感器调度器对象控制传感器的测量生成

- 标准实现：在传感器的帧时间内，将测量视为感知机会。  
- 另一种实现：通过伪扫描实现预测感知机会。

- 非成像传感器的传感器跟踪器对象

- 标准实现：新测量值完美关联；采用“M-out-of-N”形成方法。  
- 另一种实现：利用现有的轨迹对轨迹算法。

- 成像传感器的图像/视频处理器

- 将AFSIM的伪传感器图像转换为轨迹。

![](images/77779d58f6531272b61616867aced187d59b21da392f94c5d855cfbb3f2444a8.jpg)

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQDD.

# UNCLASSIFIED

# 跟踪管理

9

![](images/ede2a8cdc5babc7e6d1011b60cf41274e1efe59860c897c4fdff9c7f527433ec.jpg)

![](images/33fbff664c45265530638506f8308741de91bb422456b686f9b6fe45649542e1.jpg)

- 轨迹管理器始终可用于平台，并负责以下任务：

- 维护“本地”轨迹（WsfLocalTrack）的轨迹列表  
- 维护贡献的“原始”轨迹（WsfTrack）的轨迹列表  
- 控制轨迹与轨迹之间的关联和融合

- 关联和融合被实现为可互换的“策略”，以便于集成

控制轨迹清除  
提供跟踪事件的通知  
- 充当“过滤中心”

![](images/60b273b4c9d20ba07732a3db387b846d7de5e2dfd7307ec0b5fa7639a00d94ce.jpg)

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19.

Other requests for this document shall be referred to AFRL/RQQD.

# - 轨迹处理器功能

填充轨迹管理器的轨迹列表

从其他平台导入的离板轨迹  
来自本平台传感器的轨迹

清除轨迹

如果在指定的时间间隔内没有更新，轨迹将被“丢弃”。

报告轨迹

使用发布/订阅服务与轨迹管理器进行交互。  
报告选项包括：

- 批量报告  
- 循环报告  
传递所有轨迹或仅传递已更改的轨迹

![](images/fb5e1dd0c5c4080a77abbff44cd2641ad40afb965caa5b246183550c00486495.jpg)

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQDD.

UNCLASSIFIED

# 轨迹管理器跟踪“策略”

![](images/04dc52fac1efe178f7717c6359944e1784383e546dd96eb5596e3ead807d2851.jpg)

![](images/5c60567ebd17729a67ded69bfe898256e4f064905dec683dbf5f8f0126c14b71.jpg)

# - 轨迹关联策略：

完美关联（Perfect）

- 原始轨迹与真实目标直接关联。

- 最近邻（Nearest Neighbor）

如果两个位置之间的距离在协方差矩阵的标准差范围内“合理接近”，则将原始轨迹与另一轨迹关联。

- 聚类（Cluster）

- 真实关联（Truth）

- 使用聚类算法建立轨迹关联，协方差矩阵的标准差作为聚类成员资格的判别条件。  
- 在分布式场景中非常有用，该算法将轨迹位置与最近的真实位置匹配，如果两者“合理接近”。

![](images/36f6701b67914a69ab0d44625981f76ea99609903713318e27d07c390061d7d4.jpg)

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19.

Other requests for this document shall be referred to AFRL/RQQD.

# 轨迹融合策略：

- 本地/“默认”策略（Native / “Default”）

- 替换或基于协方差的加权平均方法。  
- 主要关注运动学融合。

- 多目标跟踪（MTT；来自Suppressor）

- 请参阅 Suppressor 文档以了解具体算法。

- 分类数据融合（Categorical Data Fusion）

- 通常遵循简单规则（但可能很快会发生变化）：

- 侧面（Side）、类型（Type）：直接复制。  
敌我识别（IFF）：根据简单的硬编码规则进行合并。  
- 辅助数据（Aux Data）：进行合并或替换。

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQQD.

# UNCLASSIFIED

![](images/c6056ea1d71108640f518812b9719e12cc86f8eead970b697b03a9bd879e866f.jpg)

# 传感器练习扩展了 WsfSensor 类

![](images/88ef5264fc6a1ba3df598e1149aeafca6c71439856af6be0337cd0889166f7ed.jpg)

![](images/6cb6e99fee35e6a381e5171a3645159c077390a7977b3e447bedb08287e70efc.jpg)

您将向AFSIM添加一个新的TricorderSensor类。

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19.

Other requests for this document shall be referred to AFRL/RQQD.

您将向AFSIM添加一个新的TricorderMode。

![](images/5fd6639348c0254baa98efef80d0fe04623b837fe9b50b7eb894bdc749ca9bbe.jpg)

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQDD.

# UNCLASSIFIED

![](images/702def34e7a4c41332cf172ab1a1434f896b28171fc995d95c738b0b48b225fc.jpg)

# Tricorder Detections

![](images/d81640ebb8edcef8da829ac820683e124d0d4536b660a9adb65eeae88184d678.jpg)

- TRICORDER SENSOR 检测生命形式，并报告所检测到的“生命形式类型”。

- 检测基于用户定义的目标属性检查。  
- 仅限标称效果（Nominal effects）。  
非基于物理学原理。  
- 无签名表或环境过程。

- TRICORDER SENSOR 将使用平台类别和平台类型定义作为检测标准。在本次练习中：

- 如果平台的类型为 LIFE_FORM，则声明检测。  
- 如果平台属于名为 klingon_life_form 的类别，则声明检测。  
- 使用 LIFE(Form_REPORTED_TYPE 作为轨迹中报告的类型

- 输入文件定义了五种不同的平台类型：

- GROUND FORCE VEHICLE、LIFE FORM 和 KLINGON 条目都属于 WSF PLATFORM 类型。  
- GROUND FORCE_VEHICLE 平台类型是场景中唯一的非生命形式玩家。仅设置了“图标（icon）”属性。  
- ROMULAN 和 VULCAN 条目派生自 LIFE(Form 平台类型。  
- KLINGON平台类型使用名为klingon_life_form的平台类别来表示生命形式，而不是从LIFE(Form平台类型派生。  
- ROMULAN、KLINGON和VULCAN平台类型使用辅助数据来标识特定类型的生命形式。

- 所有平台为了简化处理都是静止的；没有定义移动器（mover）。

- 四个玩家被创建在不同的位置，并具有初始的损伤因子（damage factors）。

- 平台的损伤因子范围为 $[0..1]$ 。  
- 值为0表示没有损伤，而值为1表示平台“死亡”。

- 平台 Spock（VULCAN）拥有一种类型为 TRICORDER_SENSOR 的传感器设备。该设备：

- 已开启，并定义了两种模式。  
- 报告其正在跟踪的生命形式类型。  
- 能够检测类型为 LIFE(Form 和类别为 klingon.life_form 的生命形式。

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19.

Other requests for this document shall be referred to AFRL/RQQD.

17

![](images/4f2c534ab573387f1a3b1813dda7f4d040353ea0bc340f994cfcee4ee0ac3b59.jpg)

# UNCLASSIFIED

# 传感器想定 (2/2)

![](images/5aea5e05369144c46355af2247a1b4ed7940e6a817dce3c638995d5b5f5b1195.jpg)

- 两个脚本观察者方法被用来捕获 SENSORTRACK Initialized 和 SENSOR_TURNED_ON 事件。

- 这些信息会被发送到标准输出（STDOUT）。  
- SENSORTRACK INITIATED 和 SENSOR_TURNED_ON 事件的数据也会被记录到 sensorscenario.asp 文件中。

- 模拟的结束时间被设置为10分钟。

- 一个名为 sensorscenario.aer 的输出文件会将Mystic查看。

![](images/4ac0b31264ea3b90ca5f6f90d2910343aec3368df615260829bc9b9f3111906c.jpg)

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19.

Other requests for this document shall be referred to AFRL/RQQD.

- 需要进行代码修改以支持以下功能：

- 接受传感器类型TRICORDER_SENSOR。  
- 接受关键字 life_form_type 及其输入值。

- 现有的AFSIM方法将被用于在平台上设置输入值：

- 平台类型为 LIFE_FORM。  
- 平台类别为 klingon-Life_form。

- 示例场景输入：

```txt
platform Spock VULCAN
add sensor tricorder TRICORDER_SENSOR
mode KLINGON
    frame_time 2 s
    reports_type
    life_form_type klingon.life_form
    end_mode
    mode ALL_LIFE_FORMS
    frame_time 1 s
    reports_type
    life_form_type LIFE(Form
    life_form_type klingon.life_form
    end_mode
    end SENSOR
endPLATFORM 
```

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQDD.

# UNCLASSIFIED

# 平台检测

![](images/55c9744c9f25f25fd0b3c6e2ad1d2805c33c04ee36079317a4b7995618a930a7.jpg)

![](images/32d820bac905962af704cfe272e266236af7b12a280d123e843283b0c4a5d003.jpg)

- TRICORDER_SENSOR 将检测平台是否具有与目标平台匹配的

life_form_type（生命形式类型）：

- 类型（例如：LIFE(Form），用于派生平台。  
- 类别（例如：类别 klingon_life_form），用于定义平台。

- 示例输入：

```txt
platform_type LIFE(Form WSF_PLATFORM
    icon human
end-platform_type
platform_type ROMULAN LIFE(Form // Uses the LIFE(Form type
    side red
end-platform_type
platform_type KLINGON WSF_PLATFORM
    icon human
    side magenta
        category klingonlife_form // Uses a category to denote a life form
    end-platform_type 
```

- 在文件“sensorscenario.txt”中，有一个脚本调用了我们为新的TricorderSensor定义的新脚本方法（这些方法需要我们自行定义）。  
- 请注意，这两个方法使用了一种新的TricorderSensor脚本类型（我们也需要创建这种脚本类型）。

// Scripts used by the script observer   
// These need to be defined before the script observer block   
script void SensorTrackInitiated(WsfPlatform aPlatform, WsfSensor aSensor, WsfTrack aTrack)   
writeln("*** T="，TIME NOW，" "，aPlatform.Name()， " has initiated a track on a "，aTrack.Type()， " with a health of "，(aTrack.TrackQuality() \* 100.0)，" %")； writeln(" Mode: ",aSensor.CurrentMode()); int lifeFormCount $=$ ((TricorderSensor)aSensor).LifeFormTypeCount(); for (int i = 0; i < lifeFormCount; i = i + 1) { std::string lifeFormTypeStr $=$ ((TricorderSensor)aSensor).LifeFormTypeEntry(i); writeln(" Life Form Type: ",lifeFormTypeStr); }   
end_script

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19.

Other requests for this document shall be referred to AFRL/RQQD.

# UNCLASSIFIED

![](images/db596892f8b48ba703ea3975b5974d56fa25e76abb65a4917399b822054e43c8.jpg)

# 开始 (1/3)

![](images/08e4280d7ca86f8f70daa0c5b170962d9564d228255bc9490dbe893b4f6e00e6.jpg)

1. 打开 CMake GUI。  
2. 确保 BUILD_WITH_mission 已被勾选。

如果未勾选，请勾选它。

3. 勾选BUILD_WITH_sensor exercis   
4. 点击“Configure”按钮。

- （如果出现提示要求选择编译器，请根据提示进行操作）。

5. 点击“Generate”按钮。

- 如果 Visual Studio 已经打开：

- 前往 Visual Studio，并在提示时选择“Reload All”（全部重新加载）。

![](images/bfeb55ee2095fdbd9de07a221aba23ff72d1e2fba0017c59b4eda4049a918298.jpg)

- 或者，可以通过以下方式打开解决方案文件“afsim.sln”：

- 从“swdev\build”目录中打开。  
- 从 CMake 中点击“Open Project”（打开项目）。

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQDD.

23

![](images/af49dde461400400b6728e835104e41ccdc91a9f867a94ec5ab68bf80d73b1e1.jpg)

# UNCLASSIFIED

# 开始 (3/3)

![](images/06588093af866894acd5508aa9d258b593370e482ccd1fd9b95d16380e275239.jpg)

- 该项目使用以下源文件:

- SensorPluginRegistration.cpp   
- TricorderSensor.hpp   
TricorderSensor.cpp

![](images/92121eb4a3c533a243e6aaa0e5329ac47ebbe35b183951b9958a0d983da66037.jpg)

请注意，许多解决方案都是可行的；我们提供了一个解决方案，以便在较短的时间内完成我们的训练练习。

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQDD.

- 本练习使用了以下类：

1. class TricorderSensor : public WsfSensor

1. 创建了一种名为TricorderSensor的新传感器类型。  
2. 维护一个TricorderMode的列表（使用vector实现）。

2. class TricorderMode : public WsfSensorMode

1. 创建了一种名为TricorderMode的新传感器模式。  
2. 维护一个已知生命形式类型的列表。

3. class ScriptTricorderSensorClass : public WsfScriptSensorClass

1. 声明并定义了新的脚本方法，这些方法将可用于场景定义。

4. class TricorderSensorRegistration : public WsfApplicationExtension

1. 该类作为应用扩展注册到标准应用程序中。  
2. 重写了 AddedToApplication 方法，用于在扩展注册后，将新的脚本类型类注册到标准应用程序中。  
3. 重写了 ScenarioCreated 方法，用于在场景由 mission/warlock 创建后，将 TricorderSensor 添加为一种新的传感器类型。

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQDD.

25

![](images/76bd4879e149691498c51b04c7d937330dcf762c7ea33261bbd3880c721a2943.jpg)

# 传感器练习

![](images/9fb20cdf727923a27b35e4481e2a3cd09e6005fdb46c9e2defa86272ac36c1eb.jpg)

- 练习1：

- 理解 AFSIM 扩展和插件如何与 AFSIM 集成，以扩展现有行为并创建新的功能。

·练习2：

- 实现主要的三录仪传感器类（TricorderSensor 和 TricorderMode）的部分功能。

- 练习3:

- 实现相关脚本类的部分功能，这些脚本类提供从脚本接口访问三录仪类的能力。

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQDD.

- 理解如何创建 AFSIM 扩展和插件，并将其注册到 AFSIM 中。  
- 内容概述：

- AFSIM扩展和插件的概览   
- 实现 TricorderSensorRegistration 类的部分功能。  
- 理解当将应用扩展添加到AFSIM时会发生什么。

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQDD.

27

![](images/d4b9ca30414a6b2be54ccd3be21ee538e7d71786be9ffb524f85300a3f071485.jpg)

# AFSIM插件&扩展

![](images/e145727383ccbd480c4f151102d829cb909f2c8036566f8645c3cedf73cb8436.jpg)

![](images/9d5126024a6b1541fbc9afebf58d3ecc61d50ab715011ff561f96c760f6bf3fd.jpg)

- 所有AFSIM扩展都必须继承自WsfExtension:  
- 已经存在三个预定义的扩展类（可以继承自这些类）：

- WsfScenarioExtension：需要为新场景命令提供扩展（这些命令需要一个新的ProcessInput）的扩展类需要继承此类。  
- WsfSimulationExtension：需要访问仿真功能的扩展类需要继承此类。  
- WsfApplicationExtension：需要创建新的脚本类型，或利用仿真扩展或场景扩展的扩展类需要继承此类。

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19.

Other requests for this document shall be referred to AFRL/RQQD.

![](images/2fb494bf752dbf52aa34c32b65cf50b321027456bc566047dee69b1ff2f2c2e1.jpg)

- 所有 AFSIM 扩展都必须继承自 WsfExtension:  
- 已经存在三个预定义的扩展类（可以继承自这些类）：

- WsfScenarioExtension：需要为新场景命令提供扩展（这些命令需要一个新的ProcessInput）的扩展类需要继承此类。  
- WsfSimulationExtension: 需要访问仿真功能的扩展类需要继承此类。  
- WsfApplicationExtension：需要创建新的脚本类型，或利用仿真扩展或场景扩展的扩展类需要继承此类。

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQQD.

29

![](images/679a4b1ea37d6267e5af99eadc159ed41c64edc2731e5bde2f821b1014ed4f53.jpg)

# AFSIM插件&扩展

![](images/fa44434dba7239a9a19768c5ae95e7e213f9243eacb1cc5c185fe0fbf1f42fd0.jpg)

- 插件在 AFSIM 中的目的是什么？

- 插件是一个可以在运行时加载到内存中的外部库。  
- 插件的主要目的是支持创建AFSIM扩展，包括：

- 应用扩展（继承自 WsfApplicationExtension）  
- 场景扩展（继承自 WsfScenarioExtension）  
- 仿真扩展（继承自 WsfSimulationExtension）

- 应用扩展的位置在哪里？

- 应用扩展几乎可以位于任何地方。  
- CMake 会在一组预定义的位置中搜索“标准”应用扩展。  
- CMake 也可以配置为在其他位置查找应用扩展。

ex., cmake ... -DWSF_ADD Extensions_PATH=<path to extension> ...

- AFSIM 扩展被编译为外部动态链接库（DLL）或插件。  
- 应用扩展如何注册到标准应用程序中？

- 每个插件都必须包含一个名为 WsfPluginSetup 的函数。  
- 该函数会在插件加载到内存并与AFSIM链接后立即执行。

- WsfPluginSetup 的函数原型如下：：void WsfPluginSetup(WsfApplication& aApplicationPtr);  
- 每个 WsfPluginSetup 的定义应完成以下任务:

1. 为该库插件创建应用扩展对象。  
2. 调用以下方法注册扩展：

- aApplicationPtr->RegisterExtension( ... )

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQDD.

# UNCLASSIFIED

![](images/cbabf5cbb9240ce192527e9aa02ed1c6dacb1869d75bfb7b7e9f08e89526cf4f.jpg)

# AFSIM插件&扩展

![](images/dee5de09357b5b3ea0e3de554c452efbc29f64b88f9823daea7b01c38b2ba42a.jpg)

- AFSIM 如何定位插件并加载扩展？  
- 使用插件管理器（WsfPluginManager 或 UtPluginManager），AFSIM 会：

- 在一组预定义的位置中搜索动态库文件（Windows 中为 .lib 或 .DLL 文件，Linux 中为 .so 文件）。

- 对于每个找到的库文件，AFSIM会执行以下操作：

1. 将库加载到内存中。  
2. 一旦加载完成，AFSIM会调用该库中的WsfPluginSetup函数。
- 检查 SensorPluginRegistration.cpp

- 审查并理解 WsfPluginSetup 函数。

```cpp
SENSOR_EXERCISE exporting void WsfPluginSetup(WsfApplication& aApplicationPtr)  
{  
    aApplicationPtr.RegisterExtension("tricorder_sensorregistration", ut::make_unique<TricorderSensorRegistration>();  
} 
```

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQDD.