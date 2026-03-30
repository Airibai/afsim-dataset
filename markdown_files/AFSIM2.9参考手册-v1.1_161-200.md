# 组件化架构

AFSIM 的核心架构是一个 Component Based Architecture (CBA)，允许通过组件包含许多功能，并通过组件列表进行管理。这个 CBA 是通过 ${ \mathsf { C } } { + } { + }$ 的面向对象原则实现的，包括封装、继承、模板化和多态性，以及下文将进一步描述的组件列表。

AFSIM 的 CBA 允许在框架的多个层级使用组件和组件列表，包括应用程序、场景、模拟和平台，还可以包含到子系统等其他领域。在模拟和平台层级，组件类型可以通过名称或角色进行访问。这种访问方式使得可以通过组件列表以通用的方式在模拟和平台中添加或移除组件类型。

![](images/fcef6a883780633a7bca82b01c6b6ae6fa974af8b232e3606c81f9524154fdc8.jpg)

组件（即 WsfComponent）是创建新类型或类型模板以进行专门化时从层次结构派生的基本元素。基础的 WsfComponent 不包含任何成员变量，因此任何函数都需要通过派生类中的 Wsf<type-name>Component 实现。

![](images/6767c04c1d3aaec9d8becaad0b9204cf29a574bb2b39ee7e8eaa5b3311d21ec7.jpg)

WsfComponent 定义了以下 主要 框架方法，其中许多是纯虚函数，需要派生类实现：CloneComponent 、 ProcessInput 、 PreInput 、 PreInitialize 、 Initialize 、 Initialize2 、<Get/Set>ComponentName、<Get/Set>ComponentRole、InitializationOrder、QueryInterface 和GetComponentInitializationOrder。

QueryInterfaceMethod 是 一 个 必 需 的 虚 函 数 ， 允 许 查 询 角 色 ， 并 要 求 定 义GetComponentRoles。角色通常定义模拟组件列表上的服务或其他类型。角色通常定义平台组件列表上的类型，例如传感器、通信、移动设备、处理器等。此外，为每个组件和部件类型在全局和有时局部级别定义组件角色枚举，以支持组件列表中的 FindComponentByRole功能。每个需要额外角色的项目都会在其自身项目中添加到全局组件角色枚举中。在全局上下文中添加角色确实需要在多个项目中进行去冲突。

组件列表与类型枚举一起提供维护和管理组件的方法。WsfComponentList 定义了以下框架方法，其中许多是纯虚函数，需要派生类实现。

WsfComponentList

Componentand Part Type Enumerations

Part Type Enumerations

主要方法可用于添加/删除组件、迭代列表中的组件、按名称或角色查找组件以及与添加/删除相关的回调。

# CBA 实现

# 平台 CBA 实现

WsfPlatform（也称为平台）本身是一个组件，并附带组件列表，以便通过附加到平台上来包含传感器、通信、处理器、移动设备等组件。

![](images/a4d7c3c88fe71b0a3f42ad48ace894fdb7654fb489404052b157a1c7540ab47c.jpg)

WsfPlatform 派 生 自 WsfComponent （ 模 板 类 ） 、 WsfComponentList （ 模 板 类 ） 和WsfObject/WsfUniqueId 类。这种派生允许直接访问 WsfComponentList 函数，并使平台能够成为另一个平台的组件，实现了组合设计模式。

# 示例组件实现

WsfSensor 通过 WsfPlatformPart 继承 WsfComponent，提供成员变量并在 WsfSensor中实现与组件相关的虚函数。WsfProcessor、WsfComm、WsfMover 等的实现类似。

![](images/e8b127a9a95b66d9cd62bdaa367d7042a593dde9cf1a8e326e64790a539f7e5c.jpg)

声明：

WSF_DECLARE_COMPONENT_ROLE_TYPE(WsfSensor, cWSF_COMPONENT_SENSOR)

函数：

WsfComponent* CloneComponent()

```txt
WsfStringld ComponentName()  
virtual void* QueryInterface(int aRole);  
virtual const int* GetComponentRoles();  
PreInitialize(...), Initialize(...), Initialize2(...) 和 ProcessInput(...) 
```

示例传感器角色实现：

//   
const int\* WsfSensor::GetComponentRoles() const   
{ static const int roles[] $\equiv$ { cWSF_COMPONENT_SENSOR, cWSF ComponentsARTICULATED_PART, cWSF ComponentsPLATFORM_PART, cWSF ComponentNULL }; return roles;   
}   
//   
void\* WsfSensor::QueryInterface(int aRole)   
{ if (aRole $= =$ cWSF Componentsensation){return this;} if(aRole $= =$ cWSF ComponentsARTICULATED_PART){return (WsfArticulatedPart\*)this;} if(aRole $= =$ cWSF ComponentsPLATFORM_PART){return (WsfPlatformPart\*)this;} return nullptr;

# 插件管理

AFSIM 的插件系统通过动态加载的插件允许进行定制，这提供了与源代码修改类似的灵活性。使用插件消除了分发框架源代码和更新核心可执行文件或库的需要。此外，终端用户可以轻松分享、加载和卸载插件。

AFSIM 插件管理提供了通过主版本和次版本描述符进行版本控制的能力，搜索由WSF_PLUGIN_PATH 环境变量定义的路径，或使用 ../<application>_plugin 或 ../wsf_plugins目录。插件管理还在注册插件之前执行操作系统、编译器检查以及构建类型检查，以确保兼容性。

# 扩展和扩展类型

应用程序、场景和模拟的扩展提供了在每个层级扩展功能的灵活性。

应用程序扩展

是应用程序单例或实例的扩展，由应用程序拥有。  
修改或表示应用程序的可选功能。

维护脚本类型和插件管理。  
可用于为场景或模拟添加功能。

# 场景扩展

是场景的扩展，由场景拥有。  
拥有类型工厂和列表、用户输入和脚本。  
允许读取输入，例如 ProcessInput(...) 实现。

# 模拟扩展

是模拟的扩展，由模拟拥有。  
提供特定功能，例如接口、输出、观察者和其他服务。

# AFSIM 构建系统

有关使用 CMake 的 AFSIM 构建系统的更多信息，请参阅构建 WSF 应用程序。

可选项目

构建 WSF 应用程序概述了创建可选 AFSIM 项目的设置和必要文件，并使顶级CMakeLists.txt 文件包含该项目。另外，集成方法部分概述了在这些文件中包含项目所需的不同文件和设置，以便通过开发人员选择的正确集成方法将其纳入 AFSIM 构建系统。

# 集成方法

AFSIM 为任何扩展或模型提供了三种集成方法：直接、项目和插件。每种方法允许：

一个或多个扩展类型进行集成。  
不同的集成方法和包含方式。  
扩展的不同交付方法。

这些方法在下面进一步定义，涉及其方法、实现、交付和任何其他独特方面。

# 直接集成

直接集成使用现有项目或插件通过新的类型定义或附加扩展类型添加来扩展功能。通常，扩展已存在于项目中，并且此方法用于添加额外的模型类型定义或进一步扩展现有扩展。

作为主要示例是在现有框架项目中添加新类型或附加基类型。在这种情况下，新类型将通过项目接口添加到新的或现有的类型列表中，类似于：

# 项目

项目方法是扩展 AFSIM 功能的最常用方法之一。此方法也可以用于通过插件方法进行集成，如下一节所述。此方法涉及创建一个额外的项目，可以集成到任何扩展类型中以扩展AFSIM 的功能。

# 目录结构

AFSIM 中的项目目录结构由多个目录和文件组成，以支持将项目作为 AFSIM 构建系统中的可选项目添加。此外，还必须包含项目纳入 AFSIM 构建系统所需的 CMake 配置文件。

```txt
my_project |-doc 
```

```txt
| - grammar |
| --- |
| - source |
| --- CMakeLists.txt |
| --- <header-files> |
| --- <source-files> |
| - test |
| - test_<application>
| - CMakeLists.txt |
| - wsf_cmake_extension.cmake |
| - wsf_module | 
```

# CMake 配置设置

从目录结构中，新增项目要通过 CMake 纳入 AFSIM 构建系统，需要四个必需文件：

wsf_module   
wsf_cmake_extension.cmake   
CMakeLists.txt   
source/CMakeLists.txt

wsf_module

此文件由 AFSIM swdev 中的主 CMakeLists.txt 使用。

wsf_cmake_extension.cmake

此文件用于告知 AFSIM 主 CMakeLists.txt 该项目是一个可选项目，并设置扩展名、源路径、构建类型和默认包含标志。

```cmake
# configuration for automatic inclusion as a WSF extension  
set(WSF_EXTERNAL_NAME my_project) # Required; Project name, match project name in main CMakeLists.txt  
set(WSF_EXTERNAL_SOURCE_PATH.) # Required; Path to the project main CMakeLists.txt  
set(WSF_EXTERNAL_TYPE lib) # Optional; default value: lib; available options: lib, plugin, exe  
set(WSF_EXTERNAL Builds TRUE) # Optional; default value: TRUE; available options: TRUE, FALSE 
```

# CMakeLists.txt

此文件是项目中包含并在 wsf_cmake_extension.cmake 文件中设置的主 CMakeLists.txt文件。它用于设置项目名称、添加项目中的子目录、包含其他所需目录、添加必要的文档和doxygen 目录，并安装项目中其他 CMake 配置文件未包含的必要项目文件。

```cmake
# Project Configuration
project(wsf_my_project)
cmake_minimum_required (VERSION 3.2.3)
include(swdev_project)
include_directories(include ${CMAKE_BINARY_DIR} ${CMAKE_BINARY_DIR}/include)
add_subdirectorysource)
add_subdirectory(test) 
```

```cmake
# Add source directories to doxygen input
add_wsf_doxygen_input(\$\{CMAKE_CURRENT_SOURCE_DIR\}/source)
# Add project to Sphinx for documentation
add_wsf_doc_input(\$\{CMAKE_CURRENT_SOURCE_DIR\})
install_sources.source wsfPlugins/\$\{PROJECT_NAME\})
install_sources_all_files(grammar wsfPlugins/\$\{PROJECT_NAME\})
install_sources_all_files(doc wsfPlugins/\$\{PROJECT_NAME\})
install_sources_all_files(data wsfPlugins/\$\{PROJECT_NAME\})
install_sources_all_files(conversion wsf plugins/\$\{PROJECT_NAME\})
installTests(test_mission DESTINATION wsfPlugins/\$\{PROJECT_NAME\})
install_source_files(CMakeLists.txt
		ωsf_module
		ωsf_cmake_extension.cmake
		ωsfPlugins/\$\{PROJECT_NAME\})
install_source_files(FILES wsfModule DESTINATION \$\{INSTALL_SOURCE_ROOT\}/wsfPlugins)
if(WSF INSTALL DEMOS)
# Demo directories included with this projects build
set(EXAMPLE_DEMO_DIRS
		Example_demo
		)
install_wsfdemo("\$\{EXAMPLE_DEMO_DIRS\}" \{\{WSF_DEMOS_ROOT\} demos)
endif() 
```

# source/CMakeLists.txt

这是从项目的主 CMakeLists.txt 文件中通过 add_subdirectory 命令调用的次级 CMake配置文件。其目的是对所有源文件进行全局搜索，指定语法文件，设置项目的包含路径、库和链接内容，最后安装源代码、演示和场景。

```cmake
cmake_minimum_required (VERSION 3.2.3)   
include (GenerateExportHeader)   
include(swdev_project)   
FILE(GLOB SRCS\*.cpp\*.hpp)   
wsf Grammar_file(SRCS"\$\{CMAKE_CURRENT_SOURCE_DIR\}/../grammar/wsf_my_project.ag")   
add_library(\$\{PROJECT_NAME\}\$\{SRCS\})   
generate_export_header(\$\{PROJECT_NAME\})   
target includeldirections(\$\{PROJECT_NAME\}PUBLIC "$\{CMAK_CURRENTSOURCE_DIR\}" 
```

```cmake
"\$\{PROJECT_BINARY_DIR\}/source") target_linklibraries(\$\{PROJECT_NAME\}wsfutil) swdevwarning_level(\$\{PROJECT_NAME\}) swdev_lib_install(\$\{PROJECT_NAME\}) 
```

# 源配置设置

```txt
WsfExampleExtension 应用程序扩展的注册函数定义：WsfExampleExtension.hpp 
```

```cpp
ifndef WSFEXAMPLEEXTENSION_HPP   
#define WSFEXAMPLEEXTENSION_HPP   
#include"wsf_example_export.hpp"   
#include"WsfScenarioExtension.hpp"   
//! An implementation of WSf Scenario Extension that   
//! adds replicated project capability to an application.   
//! @see WsfScenarioExtension   
class WSF_EXAMPLE exports WsfExampleExtension : public WsfScenarioExtension   
{ public: //! Called when the extension has been added to the scenario //! to add script types and wsf_my_project specific types virtual void AddedToScenario();   
};   
endif 
```

WsfExampleExtension.cpp   
```cpp
include "WsfExampleExtension.hpp"   
#include "UtMemory.hpp"   
#include "WsfApplication.hpp"   
#include "WsfApplicationExtension.hpp"   
#include "WsfExampleProcessor.hpp"   
#include "WsfProcessorTypes.hpp"   
#include "WsfScenario.hpp"   
#include "WsfScriptExampleProcessorClass.hpp"   
#include "script/WsfScriptManager.hpp"   
using namespace std; 
```

```cpp
namespace
{
    class ApplicationExtension : public WsfApplicationExtension
    {
        public:
            void AddedToApplication(WsfApplication& aApplication) override
            {
                // Register script classes associated with this extension
                UtScriptTypes* scriptTypesPtr = aApplication.ScriptTypes();
                scriptTypesPtr->Register(new WsfScriptExampleProcessorClass("WsfExampleProcessor", scriptTypesPtr));
            }
            void ScenarioCreated(WsfScenario& aScenario) override
            {
                aScenario.RegisterExtension(GetExtensionName(), ut::make_unique<WsfExampleExtension>(); }
            };
        }
    }
void WsfExampleExtension::AddedToScenario()
{
    WsfScenario& scenario = GetScenario();
    WsfProcessorTypes::Get(scenario).AddCoreType("WSF_EXAMPLE_PROCESSOR", ut::make_unique<WsfExampleProcessor>(scenario));
}  
//! Registers the wsf_example extension with the application
//! so it is available for use.
void WSF_EXAMPLE-export Register_wsf_example(WsfApplication& aApplication)
{
    if (!aApplicationExtensionsRegistered("wsf_example"))
    {
        aApplication.RegisterFeature("example", "wsf_example"); // Indicate the feature is present
        aApplication.RegisterExtension("wsf_example",
        ut::make_unique<WsfExampleExtension>();
    }
} 
```

WsfExampleExtension 场景扩展的注册函数定义

WsfExampleExtension.hpp

```txt
ifndef WSFEXAMPLEEXTENSION_HPP #define WSFEXAMPLEEXTENSION_HPP #endif 
```

WsfExampleExtension.cpp

include "WsfExampleExtension.hpp"   
#include "UtMemory.hpp"   
#include "WsfApplication.hpp"   
#include "WsfApplicationExtension.hpp"   
#include "WsfExampleProcessor.hpp"   
#include "WsfProcessorTypes.hpp"   
#include "WsfScenario.hpp"   
#include "WsfScenarioExtension.hpp"   
using namespace std;   
namespace   
{ class ScenarioExtension:public WsfScenarioExtension { public: void AddedToScenario() override { WsfScenario& scenario $=$ GetScenario(); WsfProcessorTypes::Get(scenario).AddCoreType("WSF_EXAMPLE_PROCESSOR", ut::make_unique<WsfExampleProcessor>(scenario)); } 1;   
}   
//! Registers the wsf_example extension with the application   
//! so it is available for use.   
void WSF_EXAMPLE exporting Register_wsf_example(WsfApplication& aApplication) { if(!aApplication.ExtensionIsRegistered("wsf_example")) { aApplication.RegisterFeature("example","wsf_example"); // Indicate the feature is present aApplication.RegisterExtension("wsf_example",   
ut::make_unique<WsfDefaultApplicationExtension<ScenarioExtension>(); }

}

# 插件

作为插件，与项目类似，并可能具有双重用途。本节概述了对项目集成方法的修改。

注意：通过 CMake 构建配置和项目接口设置，可以将一个项目集成为项目并作为插件集成。

CMake 配置设置

需要修改以下文件以创建或将项目转换为插件项目：

```txt
wsf_cmake_extension.cakesource/CMakeLists.txtwsf_cmake_extension.cake 
```

在 CMake 构建配置中，如果选择了 WSF_PLUGIN_BUILD，需要添加逻辑检查并将扩展类型设置为插件。

注意：如果 WSF_PLUGIN_BUILD 设置为 FALSE，则项目集成方法将使用该配置进行构建，因为默认的 WSF_EXT_TYPE 是 lib。

```cmake
# configuration for automatic inclusion as a WSF extension   
set(WSF_EXT_NAME my_project) # Required; Project name, match project name in main CMakeLists.txt   
set(WSF_EXT_SOURCE_PATH.) # Required; Path to the project main CMakeLists.txt if(WSF Plugin_BUILD) set(WSF_EXT_TYPE plugin) # Optional; default value: lib; available options: lib, plugin, exeendif()   
set(WSF_EXT Builds TRUE) # Optional; default value: TRUE; available options: TRUE, FALSE 
```

source/CMakeLists.txt

这是从项目的主 CMakeLists.txt 文件中通过 add_subdirectory 命令调用的次级 CMake配置文件。其目的是对所有源文件进行全局搜索，指定语法文件，设置项目的包含路径、库和链接内容，最后安装源代码和演示。

```cmake
cmake_minimum_required (VERSION 3.2.3)  
include (GenerateExportHeader)  
include(swdev_project)  
FILE(GLOB SRCS *.cpp *.hpp)  
wsfGRAMMAR_file(SRCS "${CMAKE_CURRENT_SOURCE_DIR}/../grammar/wsf_my_project.ag")  
add_library{$PROJECT_NAME} ${SRCS})  
generate_export_header{$PROJECT_NAME})  
target includeldirections{$PROJECT_NAME}PUBLIC "${CMAKE_CURRENT_SOURCE_DIR}" "${PROJECT_BINARY_DIR}/source")  
target_linklibraries{$PROJECT_NAME} wsfutil) 
```

```cmake
swdevwarning_level(\$\{PROJECT_NAME\})   
if(WSF Plugin_BUILD) swdevPlugin_install(\$\{PROJECT_NAME\} wsfPlugins) else() swdev_lib_install(\$\{PROJECT_NAME\})endif() 
```

# 源配置设置

与项目源配置设置部分类似，但在全局 Register_wsf_example 定义下面增加了一个extern "C" 部分。以下是插件项目的注册函数示例定义：

```cpp
//! Registers the wsf_example extension with the application
//! so it is available for use.
void WSFexample_Wsrf_Wsrf_Example(WsfApplication& aApplication)
{
    if (!aApplication.ExtensionIsRegistered("wsf_example"))
    {
        aApplication.RegisterFeature("example", "wsf_example"); // Indicate the feature is present
        aApplication.RegisterExtension("wsf_example",
ut::make_unique<ApplicationExtension>());
    }
}
extern "C"
{
    //! This method is called when the plug-in is loaded to ensure that the plug-in and the executable loading it were built with
    //! the same version of the plug-in API.
UT PluginEXPORT void WsfPluginVersion(UtPluginVersion& aVersion)
{
    aVersion = UtsPluginVersion(WSF Plugin_APIMajor_VERSION,
WSF Plugin_APIMinor_VERSION,
WSF Plugin_API_COMPILER_STRING);
    }
    //! This method is called when the plug-in is loaded. It must have exactly this signature (name and parameter) to succeed.
    //! As we only have an application reference at load time, one usually registers an application extension, within which the
        ScenarioCreated method can be overridden to gain access to a scenario. If one also needs
        //! access to the simulation, one should also instantiate and register a simulation extension 
```

```txt
by overriding //! the SimulationCreated method in the scenario extension. UT_PLUGIN exporting void WsfPluginSetup(WsfApplication& aApplication) { Register_wsf_example(aApplication, wsf_example); } 
```

# 额外的集成项目和要求

# 编码标准

所有集成都应遵循编码标准，如编码标准中所述。第三方库和源代码不直接与 AFSIM社区相关，可能不总是遵循标准，但这并不排除 AFSIM 接口与第三方源/库遵循标准的可能性。

# CMake

任何 CMake 文件都应遵循本文档或构建 WSF 应用程序中概述的目录结构。许多示例存在，格式应紧密遵循已发布的项目。

有关使用 CMake 的 AFSIM 构建系统的更多信息，请参阅构建 WSF 应用程序。

# 语法

集成所需的任何用户输入应包含在为项目添加功能的语法文件夹和文件中，并在测试时无错误和警告地执行。语法在 WSF 语法指南和 WSF 语法格式中进行了概述。

# 文档

AFSIM 文档通过 Sphinx 和 Doxygen 工具分别在用户和开发人员级别提供。两者都应无错误和警告地构建。

# Sphinx

集成所需的任何用户输入或参考材料的文档应包含在为项目添加功能的 doc 文件夹中。此包含确保功能被定义供终端用户使用。Sphinx 用作工具来创建 restrctureText 格式的HTML 输出。CMake 提供了一个用于构建和安装文档的 DOCUMENTATION 目标。

要正确地将 doc 文件夹包含在构建目标中，请将以下内容添加到项目的 CMakeLists.txt文件中：

```htaccess
Add project to Sphinx for documentation  
add_wsf_doc_input(\$\{CMAKE_CURRENT_SOURCE_DIR\}/...) 
```

有关文档的更多信息，请参阅 AFSIM 文档指南。

# Doxygen

支持 Doxygen 代码文档，并应由开发人员提供。要将项目的源代码添加到 Doxygen 目标以进行解析，请将以下 CMake 宏添加到项目的 CMakeLists.txt 文件中：

```txt
Add source directories to doxygen input 
```

```cmake
add_wsf_doxygen_input(\$\{CMAKE_CURRENT_SOURCE_DIR\}/source) 
```

# 构建

应消除 AFSIM 在生产中使用的每个构建配置和平台的所有警告或错误。AFSIM 社区或集成商不维护的第三方源和库可能无法满足此准则。

有关文档的更多信息，请参阅构建 WSF 应用程序。

# 测试

# 单元测试

AFSIM 中的单元测试如构建 AFSIM 应用程序中所述提供。

要向项目添加单元测试，您需要提供以下内容：

```batch
test/CMakeLists.txt test/test_example.cpp test/CMakeLists.txt 
```

这是从项目的主 CMakeLists.txt 文件中通过 add_subdirectory 命令调用的测试 CMake配置文件。其目的是对所有测试源文件进行全局搜索，链接测试可执行文件，并注册测试以作为 CMake 目标的一部分运行。

```cmake
cmake_minimum_required(VERSION 3.2.3)  
file(GLOB SRCS *.cpp *.hpp)  
if(GTestFOUND)  
add_executable(example_test ${SRCS})  
target includeldirections(example_test PUBLIC ${EXAMPLE PROJECT INCLUDES})  
target_linklibrariesexample_test  
${WSF_LIBS}  
${PROJECT_NAME}  
${SWDEV_THREAD_LIB}  
${SWDEV_DL_LIB}  
${GTEST_BOTH_LIBRARIES}  
）  
add_test(NAME "example" COMMAND example_test)  
set_property(TARGET example_test PROPERTY FOLDER UnitTests)  
endif() 
```

# test/test_example.cpp

这是一个源文件，包含针对特定函数或类的测试。可以在测试目录中创建多个源文件，并将自动包含在编译中。最佳实践是为每个被测试的类创建一个新的源文件。

```cpp
include <gtest/gtest.h>   
// Assume Example.hpp declares a factorial function #include "Example.hpp"   
TEST(Factorial, HandlesZeroInput) 
```

```c
{ ASSERT_EQ(1. factorial(0));   
}   
TEST(Factorial, HandlesPositiveInput)   
{ ASSERT_EQ(1, factorial(1)); ASSERT_EQ(2, factorial(2)); ASSERT_EQ(6, factorial(3)); ASSERT_EQ(362880, factorial(9));   
}   
TEST(Factorial, ThrowsOnNegativeInput)   
{ ASSERT_THROWS(factorial(-12),InvalidValueException);   
} 
```

# 系统集成

AFSIM 中的系统或集成测试如构建 AFSIM 应用程序中所述提供。

要向项目添加系统或集成测试，您需要提供以下文件：

```txt
test_<application>/test_<capability>.txt 
```

此文件包含用于测试 AFSIM 和 WSF 应用程序的 AFSIM 测试命令和脚本，由<application> 定义。文件中至少应包含通过/失败标准，并输出 -FAIL-，如下所示，此外还可以选择输出 -PASS-，以便在测试中解析运行脚本和输出失败的情况时正确解析 -FAIL-。

Example file: test_mission/test_maketrack.txt   
platform testplatform WSF_PLATFORM execute at_time 1 s absolute WsfTrack track $=$ PLATFORM.MakeTrack(); if (track.LocationValid()) { writeln(-PASS-); } else { writeln(-FAIL-); } end_execute   
endplatform

# 1.3.6. 性能监测工具 Performance Tools

# 什么是 WPR/WPA？

Windows 性能记录器 (WPR) 和 Windows 性能分析器 (WPA) 是 Windows 性能工具包中的性能监控工具。它们是免费的工具，可以通过下载和安装 Windows 评估和部署工具

包 (ADK) 获得。

WPR 是一个工具，允许用户动态部署 Windows 事件跟踪 (ETW) 基础设施，从而捕获内核和应用程序事件。WPR 充当会话控制器，允许用户启动和停止所有正在运行的应用程序的事件跟踪，并收集指标以诊断性能问题。

![](images/9d6e88b43cc7a432f9aeba5bcc5a83d49d14a7da700e07c27d773207283ea8f0.jpg)

WPA 是一个工具，允许用户可视化由 WPR 生成的事件跟踪日志 (ETL) 文件，并对记录的应用程序进行分析。

![](images/4f765f574291a5da637e4357b65a1df7e493a8af14f3830236b0b6403a6568b6.jpg)

重要提示：用户需要访问正在分析的应用程序的相应符号 (PDB)，因为它们对于 WPA识别进程所在的函数是必要的。PDB 文件不随 AFSIM 版本一起提供，但如果可以访问源代码，则可以生成。

如何安装 WPR/WPA

# Select the features you want to change

Clicka feature namefor moreinformation.

Application Compatibility Tools   
Deployment Tools   
Imaging AndConfiguration Designer(ICD)   
Configuration Designer   
User State Migration ToolUSMT   
□Volume Activation ManagementTool(VAMT)   
Windows Performance Tookit   
Windows Assessment Toolkit   
Microsoft User Experience Virtualization (U   
Microsoft Application Virtualization(App-V) Sequencer   
MicrosoftApplication Virtualization(App-V)AutoSeque   
□Media eXperience Analyzer

# Windows Performance Toolkit

Toolstorecord systemeventsbyusing Event Tracing for Windows,and a tool toanalyze performance data ina graphical user interface.

Includes:

·WindowsPerformance Recorder   
Windows Performance Analyzer   
·Xperf

Estimated disk space required: Disk space available:

0 bytes

413.1GB

Back

![](images/791553a1d27d528dd9f8b38b77f648edcdb8d776d447f1cc96e4a57524245404.jpg)

Cancel

如果测试机器上未安装 Windows ADK，可以通过访问下载页面并选择适用于所用Windows 版本的正确安装程序来获取。

运行 Windows 性能工具包的系统要求如下：

WPR：Windows 8 或更高版本。  
WPA：Windows 8 或更高版本，并安装 Microsoft .NET Framework 4.5 或更高版本。

运行安装可执行文件时，用户应禁用发送匿名消息，并选择包含 WPR 和 WPA 的Windows 性能工具包。

注意：Windows 性能工具包提供对以前命令行工具 Xperf 的支持。然而，Xperfview 不再受支持，所有使用 Xperf 的记录必须使用 WPA 打开和分析。

安装完成后，性能工具将准备好开始性能测试。

# 如何使用 WPR

可以通过在任务栏搜索字段中输入“Windows Performance Recorder”或在单击“开始”按钮时在 WindowsKits 下找到它来启动 WPRUI。在开始录制会话之前，用户必须配置 WPR。以下是推荐的设置：

1) 将性能场景设置为通用：这将 WPR 设置为在计算机运行时进行通用录制。  
2) 将详细级别设置为详细：轻量级负担较小，对系统干扰较少，但详细记录对于彻底分析更有用。  
3) 设置日志记录：

选择文件进行短期和有针对性的分析会话。这将数据记录到顺序文件中，这些文件将无限增长，因此建议进行短期会话以避免生成不必要的大文件。  
选择内存进行不确定的分析会话；也就是说，用户可以保持记录器运行，直到他们检测到值得注意的事情或达到他们想要分析的应用程序的确切点（即，通过向导 UI加载脚本后启动任务）。这将数据记录到一个循环缓冲区中，当数据大小超过缓冲区大小时，该缓冲区开始丢弃最旧的事件。

警告：如果会话运行时间过长，文件模式可能会导致记录过大，WPA 无法打开。

4) 选择配置文件：

CPU 使用率  
堆使用率和 VirtualAlloc 使用率用于内存分析

WPR 功能的更详细描述可以在 WPR 文档页面中找到。

一旦 WPR 配置完成，用户可以单击“开始”以开始录制会话，这将捕获 CPU 上运行的所有内容。此时，用户可以运行需要分析的应用程序（向导、任务等）。单击 保存 将停止会话并保存配置文件数据；这将生成事件跟踪日志。

WPR 也可以在命令提示符下运行。性能工具需要提升的权限才能使用，因此用户必须以管理员身份运行命令提示符。以下是开始分析的示例命令：

```batch
wpr -start CPU.verbs -recordtempto C:\<PATH>\wpr_test_temp 
```

此示例命令指定将记录 CPU 使用情况，并将所需的详细级别设置为详细。还必须指定一个临时目录，WPR 将使用该目录在生成结果 ETL 时存储中间文件。要停止 WPR 并保存记录，请使用命令：

```batch
wpr -stop C:\<PATH>\test.etl "Description of problem" -skipPdbGen 
```

必须指定路径和文件名，并为报告提供描述。skipPdbGen 标志告诉 WPR 不生成任何缓存的符号文件。

有关如何通过命令行使用 WPR 的更多信息，用户可以使用命令：

```txt
wpr -help <option> 
```

或查阅 Microsoft Devblog。

# 如何使用 WPA

以下是如何查看特定应用程序（如 mission.exe）并分析其 CPU 使用情况的简要示例。

当 WPA 打开一个 ETL 时，用户将看到一个空白的分析选项卡和左侧窗格中的图形资源管理器。图形资源管理器包含基于所选性能配置文件的所有记录数据。

![](images/52e75aa774c8169dcbca71ec354918bf96a996b066f76230bec0059a4c213390.jpg)

通过双击图形或将其拖入分析选项卡，用户可以查看记录的信息。可以通过单击和拖动灰色分隔线来调整每个信息窗格的大小。此示例显示了 CPU 使用率（采样）图，该图测量每个函数在 CPU 上的聚合停留时间。默认采样率为每秒 1000 次，因此每次计数大约为CPU 上的 1 毫秒。

![](images/39f3059acb73592a4f3fb67f0b2d56c922007102fce79842af27ec23d84b390e.jpg)

要隔离特定应用程序（如 mission.exe）的输出，用户可以通过右键单击目标应用程序并选择 禁用 $>$ 除选择外的所有内容 来过滤掉所有其他捕获的信息。

![](images/4a230b68f92011f9e96d9f9dd97c9c66f8203b99e7a341a303c1f8e107ce8900.jpg)

这将从图形窗口中删除所有其他采样进程。要在底部的详细信息窗口中隔离应用程序，用户可以右键单击它并选择 过滤到选择 。

![](images/1e3071372879e83fa38af3b9be35eac46033442f5d156d91c9f2a8479d3ac1d8.jpg)

这将导致 WPA 看起来有些空。

![](images/d4884c15cdfe35c0d6613056e1b7133917c77d14612a351c36c10a24500c705b.jpg)

用户可以通过单击进程名称旁边的右指向三角形并展开节点来开始浏览进程树。堆栈列将开始显示进程的函数堆栈，可以以相同的方式展开。此时，用户可能会看到 [Root] 下的节点带有标签：

```txt
<lib name>.dll!<Symbols disabled> 
```

如果应用程序的符号未正确加载到 WPA 中，则会发生这种情况。

![](images/46eebb7baa056830842c167c6df748af4105f2d8281050ad3873881652aa9a6f.jpg)

# 加载符号

要加载符号，用户需要单击 WPA 窗口左上角菜单中的 跟踪 并选择 配置符号路径 。这将打开 配置符号 菜单，其中可能包含已启用的预选路径；根据 WPR 的配置方式，它将自动生成并包含其他应用程序的缓存符号。如果用户只关心 AFSIM 应用程序，他们可以删除自动生成的路径并添加 AFSIMPDB 文件所在的路径。

![](images/874400de0381e817817cadd6d5be97afbd0cadf30dfe946942c44cb4585942e9.jpg)

一旦添加了路径，用户应确保启用复选标记字段并单击 确定 。接下来，必须再次单击跟踪 并选择 加载符号 选项。

注意：启用 WPA 符号自动加载会将以前会话的符号路径聚合到 配置符号 菜单中，这可能导致冗余和更长的加载时间。

现在，当用户返回到详细信息窗口时，堆栈列中的节点将正确识别应用程序的函数名称。

![](images/c9a9f4e54f93de1305e7bf95a4cc023f4215c230e487a980f66d0addf9e8a4ca.jpg)

# 分析：入门

WPA 按最大样本计数对堆栈节点进行排序，这有助于识别哪些函数调用花费的时间最长。

![](images/f8300deba7dcd1975ee224c7ec69474b82350a6d433bbc0b31ebd87e05d024b9.jpg)

仅样本计数可能会产生误导，因为性能不佳的函数可能很少发生，并且相对于应用程序的其余部分可能具有较小的样本计数；样本计数是整个应用程序运行时间的聚合值。为了检测性能下降，可以利用图形窗口检查运行时的特定时间间隔。通过单击图形并横向拖动光标，用户可以选择要扩展的时间间隔。

![](images/325a95c2dfdb5e411f44732d754b535b59d5aae32f84a7f42bf2f29f96b92b2e.jpg)

右键单击选定的时间间隔并单击“缩放”将扩展时间间隔以填充图形窗口，并更新堆栈列中的样本计数以反映在选定时间间隔内最活跃的函数。

![](images/997aaab057f81ac3a953f97d732d2246f5356073e5a85a96a3a92627cbc53ada.jpg)

此外，可以选择将单个函数调用绘制到图形中。要启用此功能，用户可以单击 图例

列中的相应方块。下图显示了所选函数调用，尽管相对于其他同级具有较小的样本计数，但它们是图形中突然性能峰值的部分原因。

![](images/3629d6ea513ab99395473122a8ae717b41ec320bc8c18641aa3593ca39a61965.jpg)

WPA 中有许多分析工具和功能，从保存特定配置文件设置到过滤特定信息。有关如何使用 WPA 及其功能的更多详细信息，请参阅 WPA 文档页面。

# 错误

2021 年 6 月，Microsoft 发布了一个修复程序，用于修复阻止 WPR 生成 CPU 使用率（采样）报告的 Windows Defender 错误。如果 WPA 不包含录制会话的采样图，则需要运行 Windows 更新（可能需要多次）以修复此问题。

不幸的是，这仅修复了 WindowsDefender 导致的多个问题之一。如果更新未能解决问题，可以在运行 WPR 时暂时禁用 Windows Defender。

# 1.3.7. AFSIM 代码贡献流程 AFSIM Contribution Process

# 介绍

本文档描述了 AFSIM 的变更贡献流程，无论是由核心维护人员提交，还是由外部贡献者提交。本文档描述了流程流，但除了 Git 本身之外，并不依赖或预设特定工具集或基础设施的可用性。同样，本文档不提供详细的实施程序，因为 AFSIM 开发发生在多个环境中，并由多个托管基础设施促进。尽可能地，各个环境中的工具应配置为支持和鼓励遵循此流程，但最终责任在于进行开发和维护的个人。即使在没有支持基础设施（例如仅文件访问或无访问权限限制）的高度受限环境中，该流程仍然适用。

同样，该流程并未为该流程管理的贡献指定特定的验收标准。有关当前标准，请参阅afsim 源代码库顶层的 CONTRIBUTING.md 文件。

贡献更改的最终入口点是通过拉取请求 (PR)。维护人员应在问题跟踪系统内协调 PR的开发。对于外部贡献者，维护人员将在识别和协调贡献后创建一个跟踪问题。

截至本文撰写时，参考的非机密开发基础设施是 DI2E。有关该环境中的具体机制，请

参阅 AFSIM 的创建拉取请求页面和该空间中的其他相关文档。DI2E 上的外部贡献者应通过AFSIM 项目讨论 (Discourse)（限于 AFSIM 分发渠道的私人项目讨论）启动贡献讨论。讨论后，外部贡献者应使用 [https://confluence.di2e.net/display/AFSIM/Enhancements](DI2E 上的增强页面) 上的“提议增强”功能。

注意：此流程是分布式代码库中工件和存储库的规范。托管、共享和外部 AFSIM 相关存储库的维护人员被鼓励遵循类似的流程，但可以根据需要选择最佳适应的方法。

# 角色定义

与贡献流程相关的三个主要角色是贡献者、维护者和发布经理。某些个人可能在不同时间以多个角色操作，但在担任特定单一角色时应仅采取任何给定的行动。

# 贡献者

贡献者是 AFSIM 社区中的任何个人，他们提交更改以供整个社区使用。贡献的更改可能包括新功能、错误修复、改进、兼容性更新或其他有价值的更改。成为贡献者的唯一要求是该个人受到有效的 AFSIM 分发协议（例如 MOU 或 ITA）的约束。有时，贡献者可能不是原始作者。但是，通过提交贡献，他们参与了流程，就像他们是作者一样，承担审查行动的责任，无论是直接还是作为原始作者的联络人。

# 维护者

维护者是由 AFSIM PMT 指定的个人，负责持续维护部分或全部 AFSIM 代码库。在PMT 的自由裁量下，维护人员池可能包括来自军队、政府和承包商的代表。维护者的责任超出贡献者，包括监督产品稳定性、推进产品能力、维护支持的版本以及协调开发和支持活动。与贡献流程相关，维护者的主要互动是作为个别贡献的审查者。当个人维护者提交贡献时，他们是作为贡献者而不是维护者。

# 发布经理

发布经理是具有决定权的维护者，负责应用于先前版本的更改。主要发布经理应委派少数个人协助他们的职责。主要发布经理及其代表都可以作为发布经理行事。虽然发布经理有决策权，但贡献流程中的所有参与者都应始终意识到对支持版本的潜在影响。

除了上述三个命名角色之外，还使用了 审阅者 一词。审阅者不是专门的角色，而是描述了在特定贡献范围内执行审阅的维护者。并非所有维护者都必须或预期会审阅所有贡献。

由于 AFSIM 开发以类似开源的方式进行，贡献者有机会查看和评论他人的贡献。这样的贡献者不构成 审阅者 ，而是 评论者 ，其建设性的反馈虽然不具约束力，但受到欢迎和鼓励。

# 动机

为了在 AFSIM 社区中协调和优先发展努力，需要一个协调的贡献流程。任何个人更改的最快接受路径是将更改直接提交到主开发分支。虽然这样的过程无疑会更快，但它带来了跨组织障碍的趋势，这对于 AFSIM 开发来说是不可取的。该贡献流程的建立是为了邀请、

鼓励和管理来自多个群体的并发贡献。作为一个流程，它不可避免地增加了一些开销和随之而来的处理延迟。然而，通过这样做，该流程旨在尽可能轻量化，同时仍合理地实现以下目标：

确保更改的整体正确性  
鼓励对整个社区的净产品改进和一致性  
促进产品设计和演进的一致性  
强制遵守贡献指南  
在发布之间管理软件 API 稳定性  
协调多个更改的相互依赖性  
及早介入以确保分支/提交结构适合回移到发布分支  
协调多个正在进行的开发，管理合并冲突与顺序依赖合并  
提供自动化测试（CI、单元测试、文档）的中间阶段  
提供社区可见的计划和完成工作的跟踪

# 指导原则

以下是激励这一贡献流程的主要指导原则。

欢迎所有人提交贡献，无论组织或资金来源如何。提交方有责任参与审查，可能导致贡献的多次迭代和重做。  
没有贡献太小，尽管当以整体形式贡献时，有些可能太大而无法有效审查和接受。  
所有贡献都必须经过审查过程，无论贡献来源如何。  
审查过程中的贡献节奏和速度应尽可能不受负担和高效，同时仍促进产品改进的趋势。  
所有参与者的时间都是宝贵的；不应对任何一方提出不当的工作要求。高效的流程有助于最大化社区利益。

为了帮助提高流程效率，良好贡献的一些指南包括：

制作较小的 PR  
编写有用的描述和标题  
使用明确的提交消息  
添加注释以帮助指导审阅者

审查应确定事物是否在不回归的情况下逐步得到改进。贡献应符合适用的贡献指南，但由于完美是良好的敌人，讨论转向 如果这样会不会更好？ 时，通常应与 PR 审查分开。换句话说，审阅者应牢记 YAGNI 原则。

主开发分支（例如 master 、 main 、 develop ）并不是神圣的。所有人都应努力保持其在所有支持的配置中可构建和稳定，但如果 CI 识别出问题，则说明 CI 正在发挥作用。特别是对于开发人员可能使用的不同平台或编译器版本，这是尤其如此。在审查过程中未发现但随后识别的问题应由原始 PR 贡献者通过后续 PR 高度优先解决。CI 只是一个工具。CI 作业因明显与 PR 本身无关的原因失败时，可以合理地排除为标准，只要在支持的平台上进行了必要的测试。

由于 AFSIM 是一个 GOTS 产品，因此没有专属代码所有者。为了管理正在进行的产品演进，代码库的维护者由 AFSIMPMT 指定。维护者的集合可能会随着时间的推移而变形和演变。由于维护权可能会随时间演变，拥有当前和明确记录的流程在维护者组之间起着重要的协调作用。维护权并不意味着严格或不可渗透的边界，也不是排他性的权威或所有权。没有一个团队被期望对产品的所有方面都有全面的了解。维护者组之间的频繁协作和磋商是至关重要的。

对于任何给定的贡献，应该可以清楚地识别贡献者从何处开始。

虽然任何维护者都可以审阅任何给定的贡献，但贡献有一个关联的主要审阅者。主要审阅者充当贡献的协调员和联系人，并且是确定何时达到 足够好 的人。贡献的最终合并通常由该贡献的主要审阅者处理。

在维护者之间意见分歧的情况下，首席架构师充当决策仲裁者。

在和跨团队的维护者审阅中，应该鼓励多种审阅，以促进一致的审阅实践并促进对代码库的广泛接触。

# 贡献流程

只是因为 PR 是结构化的，并不意味着它需要缓慢或繁琐。

只是因为 PR 应该快速，并不意味着它应该松散。

在接受之前，所有贡献必须由至少两名合适的维护者（贡献者除外）进行审查和批准。对于 修复 类贡献（如拼写错误修正），也同样要求两次审查批准；这些更改应该是微不足道且快速审查的。

建议为 PR 选择三个初始审阅者。虽然不要求必须有三个审阅者，但这有助于识别合适的审阅者，并为哪一位初始审阅者将进行评审提供灵活性。添加过多的审阅者可能适得其反，因为这通常导致每个审阅者看到很多其他人，假设他们的输入不是关键。这种情况下，常常会出现许多人可以处理任务，但都认为会有人处理，结果没有人去处理的情况。

在某项贡献影响多个团队的情况下，PR 应分配更多的审阅者，以便提供跨团队评论的机会。在这种情况下，并不期望所有审阅者提供全面审查。对总体方法的高层次一致性（或至少不反对）在这种情况下本身可能是有用的。当给予时，一致性不足以算作审查。仍然需要至少两名审阅者的详细审查，并且他们应清楚地标识。

为了帮助贡献者识别初始候选人以担任审阅者，代码库中包含了 REVIEWERS 文件。这些纯粹是方便机制，并不严格规定谁可以成为合适的审阅者（无论是通过包含还是排除）。维护者应根据需要在代码库中适当地添加和删除自己的 REVIEWERS 文件。这有助于REVIEWERS 文件准确反映维护管理的时间点。

当为给定 PR 指定审阅者时，审阅者可以在需要时推迟给其他审阅者。这可能是由于对产品特定方面的专业知识，或者只是某个人在需要时有更多时间可用。维护者还应为假期、会议或其他义务准备替代和备份。

任何给定 PR 的最佳审阅者集是依赖于具体情况的。它可能是软件工具密集型、操作交互密集型、物理学密集型，或任何包括各种主题专业知识的混合体。PR 的主要维护者应努力确保根据 PR 的性质使用适当的审阅者代表。

同时担任贡献者的维护者（这种情况非常常见）不能计入其自己贡献所需的审阅者门槛。这包括个别维护者在其他能力下也担任外部贡献者的情况。

# 拉取请求流程

将包含贡献的分支合并到主开发分支的结构化请求可以互换地称为拉取请求 (PR) 或合并请求 (MR)。一个替代的（通常更广泛的）术语是更改请求 (CR)，或在 Google 的changelist (CL)。AFSIM 文档使用术语 PR，原因如下：

它是 Bitbucket、DI2E 代码托管服务使用的术语

它更常用

# PR 准备

在创建 PR 之前，贡献者可以将 git 仓库中的分支用作暂存区域。通过这样做，开发人员可以启用早期访问 CI 机会，与其他开发人员交流，并提供正在进行的工作的备份。分支可以存在而没有关联的 PR。然而，它们可能会受到偶尔修剪闲置、废弃或其他过时分支的约束。

如果愿意，贡献者可以通过明确标记为此类来创建工作进行中的 (WIP) 或草稿 PR。标记 PR 为工作进行中的常规方法是将标题前缀为 WIP: 或 (WIP)。WIP 状态可用于指示对一般方向的非正式反馈的开放性，同时允许审阅者将其识别为不期望完全准备好。WIP PR 没有流程要求。因此，不应期望审阅者具有相同的及时性和响应性。实际上，除非贡献者特别要求，否则审阅者可能会或可能不会认为更改在 WIP 状态下准备好进行审阅。WIP PR 通常对团队内协作和执行内部团队审查有用，同时随后将团队审查评论提供给最终审阅者，而不必重复讨论。WIPPR 应积极工作，不应长时间闲置或变得过时。

PR 分支应被构建为逻辑上既独立又完整。相互依赖的更改应在单个提交中进行，而逻辑上的顺序更改应用应在单个分支中作为一系列多个提交。应优先选择短期分支和更频繁的[完整] PR，以减少相关的如合并冲突等的波动。

对于自动化或工具驱动的更改（即 sed、clang-tidy 等），应使用专用提交仅用于执行命令，而不涉及其他预编辑或后编辑。对于这种自动化更改，请在提交消息中包含所用的命令和参数，以便在历史中保存，并帮助审阅者。

为了促进高效的贡献和审阅，强烈鼓励单一目的贡献。大型批量贡献通常可以更好地组织为一系列相互构建的单个 PR。

新分支最好基于初始开发时的主开发分支。完全可以预期 PR 分支和主线分支会分叉。在提交 PR 之前，没有一般需要将分支重新基于主开发分支，并且出于习惯或主动这样做是不可取的。当合并冲突出现时，贡献者有责任在需要时将主开发分支合并到 PR 分支中以解决冲突。

仓库的提交历史很重要，应该作为产品的活工程笔记本，包括变更时的理由、约束和考虑。同样，PR 的分支应该包含逻辑上的提交进展。在某些情况下，单个提交就足够了，但通常多个结构良好、顺序良好的提交可以为审阅以及历史信息提供相当大的上下文。提交审查的最终分支不应包含诸如 哦，忘记了另外两个地方 或 哎呀，忘记了另外三个地方 之类的随意提交。可以使用交互式重新基来调整提交消息和/或改进提交的结构或顺序。只有贡献者应执行交互式重新基，但审阅者可以请求这样做。对审阅反馈的更改不应被交互式重新基到原始提交中，尽管可能希望交互式重新基多个审阅地址提交的部分。实际上，保持提交和历史记录的分离通常很有价值。自动工具代表贡献者生成的提交在使用时不需要交互式重新基，但如果需要也可以。

在转变为 PR 之前，分支应在 MSVC 和 GCC（支持的编译器）上进行编译测试。此测试可以在本地开发环境中进行，也可以使用可用的 CI 系统进行。没有必要使用最低编译器版本。针对 PR 分支的 CI 构建应有助于识别此类问题，并且每个开发人员维护多个本地编译器版本往往很麻烦。

贡献者应努力将特定主题的所有相关更改收集到同一 PR 中，以避免相同内容和上下文的多次连续提交。这有助于减少审阅者的心理切换需求 我不是刚看到这个更改吗？ ，以及更容易收集所有更改到单个分支以进行基于分支的 CI 执行。

# PR 创建

创建 PR 是贡献者采取的特定行动，以表明分支开发的结束并开始审查。这是贡献的

最后阶段，其前是创建问题和根据问题进行的后续开发。

当贡献者发起 PR（或更新以移除 WIP 指定）时，它应该反映出某个分支准备好合并到主开发分支的信念。贡献者有责任进行尽职调查，以测试并确保提交的分支根据CONTRIBUTING.md 中规定的贡献指南是完整的。

贡献者应自己审查提交系列和每个的差异，以确保所有更改都是预期的。快速跟进的附加提交通常表明提交仓促。一旦创建，贡献者有责任通知适当的审阅者 PR 已准备好审阅。PR 应有一个描述，涵盖所有组成提交的范围。通常不应花费大量时间去制作理想化的 PR描述，因为它们不包括在永久更改历史中。很多时候，描述可以从第一个提交消息自动生成，和/或提交主题的摘要可能足够清晰地描述目的。如果需要额外时间来制作 PR 消息，贡献者可能考虑改进基础提交消息的机会。

在大多数情况下，PR 应引用由 PR 解决或解决的突出问题。提供琐碎修复的 PR 可以作为“修复”PR 提交，而无需绑定到问题。修复 PR 应在 PR 标题中包括“fixup:”前缀。在此上下文中琐碎的意思是拼写错误、清理或其他易于和清晰的可审查更改。它们必须是不更改原始设计、实现或运行时行为的情况下提高可理解性或可维护性的更改。

可接受的“修复”PR 范围的示例包括但不限于：

面向用户的文档的编辑更改，以 reStructuredText 或 Markdown 形式：

修正语法或拼写错误  
修改句子或段落以提高可读性而不改变原始写作意图  
根据最新的 AFSIM 文档指南提高风格一致性  
根据实施的功能协调文档  
更新（过时的）文档（例如，添加弃用说明）  
更新（错误的）文档（例如，错误的参数名称或类型）  
添加（缺失的）文档（例如，功能的有限文档覆盖）

${ \mathsf { C } } { + } { + }$ 源代码工件的一般清理：

根据最新的 AFSIM 编码标准提高源代码格式和一致性  
修正源代码注释中的拼写或语法错误  
修正交换或错误命名的变量或参数（例如，查找替换或重构错误）

一旦创建了 PR，相关的分支应保持稳定。PR 分支的稳定性意味着不应添加不解决审查评论的新提交。保持 PR 稳定有助于审阅者有一个稳定的审查目标。同样，贡献者应避免重写分支历史，除非与审阅者协调。这有助于审阅者更容易跟踪已审阅的内容，并在后续审查中仅显示自上次审查以来的更改。

贡献者应至少识别一名初始审阅者，如果知道的话还可以多识别一些。如果没有指派审阅者，PR 很可能在一段时间内未被注意到，直到在定期检查未决 PR 时被识别。

# PR 审查

为了最终合并，PR 必须获得两次审查批准。

PR 的审查从最初选择的审阅者开始。在创建和选择初始审阅者后，初始审阅者自我组织，确定 PR 的主要审阅者。首先，选定的审阅者评估自己是否适合审阅特定更改，确定主要审阅者，并根据特定更改的需要添加（或替换自己为）替代审阅者。

即使仅考虑单一目的的 PR，所有 PR 的大小也不相同。有些是修复单个拼写错误的琐碎问题，可以非常快速地进行视觉审查，而其他则跨越多个领域的多个文件。

PR 审查的及时性没有绝对的门槛要求。任意的强制规定会削弱审查的彻底性。话虽如此，审查的预期时间应该相对于更改的大小较小。一次性的大型和/或复杂更改通常需要指数级的时间进行充分审查。一旦收到，来自外部来源的贡献可能会受到维护者资源优先级的

影响。

然而，作为经验法则，贡献者应该合理地期望在提交后的 24-48 小时内获得初步审查反馈，较小的 PR 需要的时间更少，而较大的 PR 可能需要更长时间。初步审查反馈可能不全面，但应为贡献者提供初步确认以及基于更改的大小和复杂性以及审阅者日程安排的预期时间框架。指定这样的平均审查时间有助于让贡献者知道何时跟进或考虑添加替代审阅者。

虽然审查应该是全面的，但没有要求或期望审阅者找到可以评论的内容。如果 PR 被认为准备就绪，那么简单的批准是完全可以接受的履行审阅者职责的方式。仅仅为了找到细枝末节进行评论的搜索是适得其反的，强烈不鼓励这样做。如果审查的唯一行动是批准，审查的价值并不会因此降低。

除了更改本身的最终状态内容外，审阅者还应审查提交消息的上下文和正确性。提交消息将保留在历史中，而 PR 特定的写作和描述通常不会。审阅者在审查时的方法会有所不同，可以分别审查大的结果差异和提交，也可以按顺序逐步审查提交。只要内容和提交消息都经过审查，这两种方法都是同样可接受的。

当审阅者在评论中明确区分讨论和澄清请求与阻碍成功审查的任务时，对贡献者是有帮助的。贡献者应考虑两者，但了解剩余的请求项目有助于任务跟踪。PR 上的任务或行动并不总是意味着建议必须被采纳。如果贡献者认为这不正确或不合适，那么在 PR（和/或代码注释）中解释可能是合适的解决方案。CONTRIBUTING.md 中指定为贡献指南的项目不应轻易忽视。同样，贡献指南的适用性应根据受影响代码的当前状态主观判断。例如，如果对没有现有单元测试的代码进行更改，那么更改代码的单元测试可能仍然是合理的，但为整个受影响模块编写单元测试可能是相对于 PR 范围的过度任务。

PR 审查在社区中是可见的。作为开放的一部分，审查和社区评论的早期曝光应该受到欢迎。非维护者的评论应始终根据其优点进行考虑，但只有审阅者可以指定接受 PR 所需的行动。

作为 PR 一部分生成的任务或行动通常包括代码更改，但也可能包括创建衍生问题或其他副作用。审阅者可以有条件地批准 PR，待解决已识别的行动并有明确的解决结果。审阅者可以选择不使用此选项，直到解决路径对贡献者和审阅者都清晰且可接受。

审查的重点和精力应放在语义、交互和接口上。审阅者应依赖 CI、代码格式化和代码检查工具及其报告（如有）。在可用的情况下，所有 PR 应通过基本的 CI 执行。在审查期间由 PR 中的更改引起的 CI 识别的问题必须在最终 PR 批准之前解决。

审阅者还可以在合理预期 PR 具有更高影响可能性的情况下包括执行辅助 CI 管道。例如，文档生成过程的全面改革可能需要额外执行文档生成管道。审阅者应努力在审查中平衡CI 的使用，考虑 CI 资源容量、给定 PR 的预期影响，并且不应不当阻碍 PR 过程。谨慎运行辅助 CI 管道在审查期间捕捉问题方面可能非常有益，但不应成为对每个 PR 运行所有可用管道的要求或期望，因为这可能会延迟审查。

审阅者应注意冗长的 PR 讨论。特别是应区分它是解决激励问题的核心方面，还是进入未来改进机会的假设或识别。这样的讨论通常应该被捕获但单独记录，以免鼓励长时间审查而没有明确的解决方案。

贡献者可以在审查进行中开始工作并添加提交以解决审查反馈。只有对具有明确解决路径的审查项目的修复应被推送，具有活动讨论或不明确路径的项目应被保留，直到找到明确的解决路径。与原始开发提交一样，审查提交应组织良好且完整； 散弹枪 式的多个审查修复提交可能会分散审查过程的注意力。这对于审查提交更为重要，因为它使审阅者能够仅审查额外的增量提交，从而提高审查时间的效率。

如果对分支的审查识别出涉及重大返工的内容，则应将其转换为 WIP 状态。这有助于审阅者将其保持在他们的视野中，但不必频繁检查是否需要审查行动。一旦返工完成，应将

其转换回活动 PR 状态。

除了贡献者之外，没有人应该重写分支历史。作为例外，在提交者事先同意的情况下，审阅者可以在审查中的分支内执行历史重写。

在审阅者之间协调时，应以合理性为主导，作为更大更改的一部分偶然涉及多个其他领域的简单更改可能不需要每个潜在审阅者的审查。许多开源项目都有处理此类跨领域或大规模更改的指南（例如，Google Chrome 和 LibreOffice）。对于 AFSIM，应为此类大规模更改使用不同的 PR，并应具有集中的目的，例如格式化、标准一致性、API 更新等。为每个目的使用不同的 PR 有助于提高审查效率，并简化将来的更改清晰地回移到发布分支。

# PR 处置

在合并之前，PR 审查中的所有操作都应得到解决。适当解决 PR 任务可能包括为将来的操作打开一个新问题，只要这不会降低 PR 内容的准确性。

如果审查确定 PR 中的要求或方法不再适用，或者贡献者撤回 PR，那么 PR 应该在不合并的情况下关闭。偶尔的 PR 关闭（即拒绝接受）是开放软件开发健康的指标，绝不应被视为失败。

一旦所有操作完成并且足够的审阅者批准，PR 应该被合并。PR 的主要审阅者应在确认满足审查门槛和所有相关贡献标准后执行实际合并。在某些情况下，维护者可能需要协调以优先顺序合并几个单独的 PR。

合并 PR 时，应始终作为非快进合并提交进行。原始 PR 分支不应在合并过程中重写历史，无论是通过分支压缩还是重基。在合并之前，主要审阅者可以在现有分支上附加额外的清理提交，但必须保留贡献的历史。在 PR 合并期间重写分支历史是不可取的，因为它会丢失信息并且有害，包括以下显著方式：

丢失提交的时间线和基础上下文（开发断点）  
略去原作者和提交者的功劳   
减少 gitbisect 和其他工具在隔离/查找开发的自然阶段提交的有效性  
阻止贡献者（以及从远程拉取分支的所有其他人）根据 git 历史跟踪和自动识别并删除合并的本地分支

如果 PR 过于陈旧，应予以拒绝。贡献者始终有机会在将来重新参与并重新开放一个新的 PR。

# 发布分支

发布经理保留选择应用于一个或多个发布分支的提交的自由裁量权。然而，贡献过程中的所有参与者都应考虑对积极支持的发布分支的影响，并努力在初始问题创建期间识别适用于发布的更改。期望某个更改最终应用于一个或多个发布分支可能会影响和指导针对给定更改采取的方法或结构，从而更容易回移。从与给定 PR 相关联的问题开始，贡献者可以推荐 PR 作为一个或多个发布分支的候选。也可以从较大分支中的单个提交中识别为回移候选，但通常更倾向于使用单独的 PR。

除非发布经理确定的特殊情况，否则不应向发布分支提交任何尚未在最新开发分支上（即 PR 已经批准并合并）的提交。将开发分支中的提交应用于发布分支的首选模式是使用 gitcherry-pick-x 以包含对原始提交的可追溯性。这使得在以后的时间点更容易定位任意提交的祖先。

稳定 和 最新 发布分支的标准可能根据生命周期时间和需求而有所不同。例如，准备

首次发布的新发布分支的标准可能比从分支发布的先前版本的更新更宽松。Linux 内核稳定发布规则是考虑发布包含的其他标准的几个公共示例之一。某些典型的包含和排除标准是：

# 包含

安全更新  
修复发布中包含的功能的错误  
修复兼容性，例如非故意的 API 更改

# 排除

新功能  
与比发布中支持的工具链更新的兼容性

当提名 PR 以回移到一个或多个发布分支时，最好使用提交消息本身中的“尾注”来完成，

例如 AFSIM-Backport: release_2p7, release_2p8。在提交消息中标识为回移的分支应由贡献者测试，以识别在 cherry-pick 时它们是否能够干净地应用。如果存在冲突，推荐的冲突解决步骤和理由的摘要通常会大大帮助发布经理。预期应用于发布分支的分支 PR 具有重要性，仅修复一件事。

# Git 程序

本节概述了在 PR 过程中经常使用的 git 命令。它仅包含命令行参考，但大多数图形工具（例如 UI 包装器、IDE 集成）提供了实现相同最终结果的方法。

# 历史重写

在 PR 分支上重写历史通常是有用的。它允许清理提交消息，例如 哎呀，错过了另外三个地方 。知道可以在以后进行这样的清理有助于鼓励在开发过程中频繁提交和推送。

历史重写可以在开发和准备分支提交时频繁使用。然而，一旦分支作为[非 WIP]PR 提交，除非审阅者要求，否则所有人都应避免重写历史。在审查期间进行协调有助于最大限度地减少审阅者在跟踪已审查和未审查内容时的干扰（例如，在初步审查后审查调整时）。

仅仅为了与主线开发分支保持同步而重写历史应该避免。然而，它可以是解决合并冲突的合理和有用的方法，但应仅在需要时使用，而不是预先使用。

由于使用重叠术语，一些 git 术语有时可能会令人困惑。特别是，在交互式重基中 压缩 单个提交不应与合并时整个分支的 压缩 混淆。在交互式重基中压缩或修复单个提交提供了分支压缩所没有的控制和粒度。它仍然是一个单独的分支，最终合并提交到主线开发分支。相比之下，合并时压缩整个分支通常会在主线开发分支上产生一个新的提交，删除了合并甚至发生的元数据历史。

每个贡献者都有他们个人偏好的开发工作流程。关于如何以及何时在 git 中使用各种历史重写技术的教程超出了本文档的范围。一些常用的方法包括 git rebase --interactive--rebase-merges、git rebase --autosquash 和 git reset --soft。

# 提交消息

使用 git 作为版本控制系统意味着提交消息的惯用格式。AFSIM 开发不强制遵循像ConventionalCommits 这样的正式规范，但贡献者应该了解惯用的提交格式。提交消息应遵循以下指南：

# 必需

使用简洁的主题作为第一行（软限制约 50 个字符，硬限制 70 个字符）。Linux 文档：“既简洁又描述性是具有挑战性的，但这正是写得好的摘要应该做到的。”  
在第三行开始正文（第二行留空）。  
将正文换行在 72 个字符（除了连续字符串如 URL 引用和外部引用如编译器错误消息）。

# 推荐

以相关的大写动词开始主题行。  
使用祈使语气和现在时，例如“Fix”、“Improve”、“Update”而不是“Fixed”、“Improves”、“Updating”。  
不要在主题后面加上句号。  
使用提交“尾注”，例如“Fix:AFSIM-1234”在消息末尾将提交与问题关联。

# 考虑

描述 为什么 和 如何 ，而不是 什么 。确切的更改被捕获并且可以在提交差异中轻松查看。进行更改的背景和理由并不总是显而易见的（当它显而易见时，提交正文可能是多余的）。特别是，更改文件的名称经常是多余的。  
努力将提交结构化为逻辑上不同的分组。一些开源项目要求系列中的每个单独提交都能成功构建；这不是要求，但这是一个值得称赞的目标。

# 工具配置

本节提供了跨环境的工具配置建议。它不指定任何工具或产品的具体程序，而是声明性地说明了考虑的结果行为。

如介绍中所述，工具支持是有帮助的，但最终责任在于进行开发和维护的人。

各种环境可能提供不同级别的服务和/或处于不同的技术准备阶段；以下仅供考虑，并不代表最低能力。一些有限的环境可能仅使用文件/SSH 托管的 git 仓库并通过 git-diff 审查 PR，但过程应保持不变。

# 开发者 Git 配置

为了保持与编码标准的一致性，将执行 git 预提交钩子以处理提交时的代码格式化。此钩子将在提交中更改的文件上调用 clang-format。git 环境将在 cmake 配置步骤中配置为使用包含此钩子的 afsim 目录（.githooks）。

# 开发者 IDE 配置

一些 IDE，如 Visual Studio，内置或通过插件启用了 clang-format 支持。希望在提交之前通过其 IDE 本地运行 clang-format 的贡献者应确保其 IDE 正确配置为使用clang-format $9 . 0 +$ 可执行文件。一些 IDE，如 VS2017，默认集成了较早版本。

# 基础设施配置

在任何给定环境中的可用性下，以下是与特定集中基础设施配置相关的建议供考虑。

限制对受保护开发分支（例如 master、main、develop）的维护者的提交和合并访问  
限制对发布分支（例如 release/*）的发布经理的提交和合并访问  
要求对发布分支的所有提交要么是注释的 cherry-picks，要么是已经合并到主开发分支的分支的合并  
要求标签是注释标签，而不是轻量标签  
限制版本标签的推送到发布经理（例如 $\nu ^ { * }$ ，*-release）  
限制其他标签的推送为用户前缀（例如 ${USERNAME}-*）  
使用 REVIEWERS 文件自动分配初始审阅者，考虑 WIP 与最终状态  
在 PR 可合并之前要求必要数量的审查批准  
在 PR 可合并之前要求解决所有任务/操作  
在 PR 可合并之前要求针对分支的成功 CI 执行  
禁止对受保护开发分支的压缩合并和快进合并  
允许匹配用户在用户分支上强制推送（即那些匹配 ${USERNAME}/* 的分支）  
强制服务器端预提交 git 钩子以验证更改部分的 clang-format  
强制服务器端预提交 git 钩子以验证提交消息结构（允许一些松散）  
提供更改通知（例如通过电子邮件），包括在 PR 分支上出现的合并冲突

# 1.3.8. WSF 语法指南 WSF Grammar Guide

WSF 语法格式，如 WSF 语法格式中所述，定义了 WSF 命令的语法。该语法用于许多工具和应用程序中以解析 WSF 文件。许多 WSF 模块的语法文件已经存在，可以在 WSF 安装 bin 目录的 grammar 子目录中的.ag 文件中找到。

当添加新的类型和命令时，开发人员有责任维护语法文件，以便工具和应用程序可以正确处理 WSF 文件。

# 语法文件定义

语法文件有两个主要功能：解析 WSF 输入的规则和创建表示输入文件的数据的操作。

# 规则

序列   
字面量  
规则引用  
循环   
内置规则  
命名规则

# 结构

符号表

代理  
变量

# 操作

# 规则

规则构成了语法的基础。规则共同定义了如何解析输入文件。单个规则可以匹配或不匹配给定的输入。找到匹配的第一个规则被使用并消耗文本。

# 序列

最基本的规则是序列。序列由{ }符号指示。序列定义了必须依次匹配的子规则列表：{ rule0 rule1 ... }

序列中的每个规则都必须匹配才能使序列匹配。在序列中，规则从 0 开始计数。稍后，规则可以使用$0符号引用。

# 字面量

字面量匹配单个特定的字符字符串。字面量可以是带引号的字符串或纯文本。解析器假定以空格分隔的标记。

```txt
end_time
"the end time" 
```

# 规则引用

规则可以在定义后使用‘<rule-name>’格式引用：

```twig
<my-rule> 
```

# 循环

循环是指 0 到多次或 0 到 1 次重复的规则引用。*字符用于表示零到多次循环。+表示1 到多次。?表示 0 到 1 次。

{ string_list $\text{串串} > ^ { \text{串} }$ end_string_list |ABCD{EFG}?   
1

使用 * 或 $^ +$ 时，终止字面量的存在起到关键作用。在 stuff <string>* end_stuff 中，将读取任意数量的字符串，直到找到 end_stuff。但使用 stuff<int>* 将消耗每个匹配整数规则的标记，并仅在非整数标记后停止。尽可能地，应该提供终止字面量。

# 内置规则

```txt
string> 
```

匹配以空格分隔的字符串：

MY_PLATFORM  
banana's/apple  
· <quotable-string>匹配以空格分隔的字符串或带引号的字符串：  
MY_PLATFORM"C:\Program Files\MyPath"  
· <string-except>匹配任何字符串，带有例外列表：  
#匹配任何以空格分隔的字符串，除了invalid_word1和invalid_word2(string-except invalid_word1 invalid_word2)  
· <integer>匹配整数：  
0-123  
· <real>匹配实数：  
-2-2.0-2.0e-7  
· (error {})定义一个序列，当匹配时触发错误：  
#这将匹配任何字符串。如果它是整数，将记录一个错误。{（error {integer}）|<string>}  
· (delimited...)定义非空格分隔的单词。所有规则假定输入以空格分隔。此规则提供了一种绕过此限制的方法。每个参数都不带空格匹配。使用此规则有一些限制，尤其是每个其他参数必须是字面量：  
#这将匹配纬度值如10.5n和60s{（delimited<nI|（delimited<s)}  
· (name name-kind)与 $<  \mathrm{string}>$ 匹配相同，但将单词标识为某物的名称。name-kind标识名称的种类。此规则的目的是允许用户界面自动填充建议以填写此字段。示例用法：icon(name icon)I category(name category)I ignore(name category)

(typeref type-prefix)

与 <string> 匹配相同，但表示匹配的单词应为现有类型。type-prefix 表示符号表中的类型键前缀。示例：

```txt
exclusion-zone (typeref zone) | inclusion-zone (typeref zone) 
```

(nocase { … })

接受任何序列，并使其不区分大小写：

```txt
(nocase { true | false }) 
```

(file-reference file-type)

与 <quotable-string> 相同，但也将文本标记为指定类型的输入文件的位置。

(output-file-reference file-type)

与 <quotable-string> 相同，但也将文本标记为指定类型的输出文件的位置。

<TypeCommand>

使用与当前符号关联的规则。参见符号表。

<ScriptBlock>, <ScriptVariables>, <ScriptFunctionBlock>

与循环（*）一起使用。匹配任何字符串，但将文本块标记为属于脚本。脚本内容在另一个项目中解析，此语法仅注释文本块。

读取一个脚本及其返回类型、名称、参数script $\text{<ScriptFunctionBlock>}$ \*end_script#读取没有返回类型、名称、参数的脚本on_exit $\text{<ScriptBlock>}$ \*end_on_exit#读取脚本变量块script_variables $\text{<ScriptVariables>}$ \*endcript_variables

# 命名规则

使用此语法创建一个新的命名规则：

```txt
rule \*rule-name\*{ *rules\* } 
```

示例：

```txt
定义新规则  
(rule my-rule{end_time<Time> 
```

```txt
使用新规则   
(rule my-rule-2{ <my-rule> | not <my-rule> }
```

规则名称是用户定义的，除了 root-command 规则。必须定义 root-command 规则，并作为语法的入口点。任何被处理的顶级输入都应以某种方式匹配 root-command 规则。

为了支持可扩展性，可以重新打开命名规则。例如，这两个块可以存在于任何语法文件中的任何位置，并且都向 root-command 添加新命令：

```txt
rule root-command { apple{core|peel} }   
rule root-command { banana{seed|peel} } 
```

这等效于：

```txt
rule root-command { apple{core|peel} | banana{seed|peel} } 
```

# 结构

结构是一种特殊类型的命名规则，表示 WSF 理解的对象。Platform、Sensor 和 Processor是结构的示例。结构可以包含规则定义，就像 (rule..) 命令一样，但也可以包含变量。示例：

```txt
(Struct MY_SENSOR :base_type Sensor :symbol (type sensorType MY_SENSOR) (var String my_settings)   
{ my_command <String> [my_settings \(\equiv\) \\(1] |<Sensor>   
}） 
```

结构可以像 (rule ....) 一样稍后使用 <struct-name> 语法引用。

```txt
:base_type BaseTypeName 
```

表示此结构继承另一个结构的所有变量

```txt
symbol ... 
```

指定在解析时应将结构插入符号表中。符号由 new 和 load 规则使用。参见符号表变量在后面描述的代理表示中使用。它们对文件的解析没有影响。

# 符号表

要解析使用类型的文件，我们需要一个符号表。符号允许文件引用先前定义的类型。符号表是从键到结构类型的映射。键是字符串的元组。

给定此示例输入文件：

```txt
platform_type newtype WSFPLATFORM
    processor y WSFScriptPROCESSOR endprocessor
    weapon z WSF_EXPLICIT_WEAPON endweapon
end-platform_type
platform x newtype
    delete weapon z
end-platform 
```

生成的符号表如下所示：

<table><tr><td>符号</td><td>类型</td></tr><tr><td>platformType.newtype</td><td>struct Platform</td></tr><tr><td>platformType.newtype processors.y</td><td>struct WSFScriptPROCESSOR</td></tr><tr><td>platformType.newtype.weapons.z</td><td>struct WSF_EXPLICIT_WEapon</td></tr><tr><td>platform.x</td><td>struct Platform</td></tr><tr><td>platform.xprocessors.y</td><td>struct WSFScriptPROCESSOR</td></tr></table>

符号表包含了解析文件所需的内容。如果接下来发生编辑 platformx 块，我们可以确定 platform.x 存在并且它有一个名为 y 的处理器，其类型为 WSF_SCRIPT_PROCESSOR。符号表的维护通过 new、new_replace、load 和 delete 规则来完成。在符号表中引用位置（键）是通过 type 和 subtype 命令完成的。

(type …)

指定符号表中的位置。允许任意数量的参数。每个参数可以是字符串或序列规则引用。序列规则引用将给定规则匹配的文本插入为类型键的一部分。示例：

```txt
(type platform x) #-> platform.x  
(type platformType新业态 processors y) #-> platformType.newtypeprocessors.y 
```

# 使 用 序 列 规 则 引 用 作 为 序 列 的 一 部 分 （ 未 显 示 ） (type platform $\$ 1$ ) # ->platform.<text-from-parsed-file>

(subtype …)

与 type 相同，但将参数附加到当前类型。当前类型最初是一个空元组，但通过使用 new、new_replace 或 load 规则进行更改。

(new storage-address load-address [:backup load-address])

定义一个尝试创建新符号的规则。load-address 处的符号被复制到 storage-address。地址必须是 type 或 subtype 命令。如果 storage-address 尚未使用，并且 load-address 指向有效符号，则规则成功。storage-address 成为后续命令的当前符号，直到当前序列结束：

```txt
{ sensor<string><string>(new (subtype sensors $1) (type sensorType $2) <TypeCommand> end_sensor | other_command 
```

在上面的示例中，如果 new 规则成功，则当前符号设置为新的符号表条目。TypeCommand 将调用与新符号关联的结构，并在匹配 end_sensor 标记后，当前符号恢复

到其先前状态。

如果 new 命令失败——要么 storage-address 处已经存在符号，要么 load-address 处不存在符号，则规则不匹配。这会导致整个序列匹配失败。

:backup alternate-load-address

此选项添加一个备用位置以加载类型，如果第一个加载位置无效。此外，会记录一个错误。这主要用作用户输入未知类型名称时的回退，备份类型至少提供对用户意图的部分理解。

(new_replace storage-address load-address [:option…])

与 (new …) 相同，但会替换任何现有符号。

(load load-address)

从符号表中加载现有符号并将其设置为当前符号。如果符号不存在，则此规则不匹配。

(delete address)

删除现有符号。如果该地址没有符号，则规则不匹配。

```txt
在当前符号上创建一个名为 'mover' 的新子符号，从 'moverType.WSF_AIR_MOVER' 加载 (new (subtype mover) (type moverType WSF_AIR_MOVER))
```

```txt
尝试加载用户定义的 mover。如果找不到用户定义的类型，则创建一个 WSF_AIR_MOVER。（记录错误）
```

```txt
(new (subtype mover) (type moverType $1):backup (type moverType WSF_AIR_MOVER)) 
```

```txt
将 'mover' 加载为新的当前符号
```

```lisp
- (load (subtype mover)) 
```

# 代理

上述所有构造都需要正确解析输入文件。本节中的构造为语法提供语义，构建输入文件含义的表示，这就是我们所说的代理。

代理的结构与符号表类似。与平台对应的符号表键也会与代理中的平台对应。代理不存储解析对象的关联规则，而是存储有关该对象的信息。对于平台，我们可能会存储侧面、图标、位置、部件列表等。目的是不构建输入文件中对象的全面描述，而是保存构建特定用户界面所需的关键信息。因此，一些结构定义的变量很少或没有，而其他结构定义的变量很多。

# 变量

变量是结构的成员，用于存储有关对象的数据片段。变量由类型和名称组成。变量类型定义了变量包含的数据类型。可用变量类型的完整列表可以在核心语法文件中找到 这些是用 (value…) 命令定义的。此外，还有两种容器类型 List 和 ObjectMap。List 是对象的有序列表，用于路线的航点等。ObjectMap 是一个关联数组，将字符串映射到值类型。对于 List和 ObjectMap，必须使用以下语法指定包含类型：

```txt
List/Platform  
List/Waypoint  
ObjectMap/Platform  
ObjectMap/Sensor 
```

最后，语法中定义的任何结构都可以作为变量类型的双重用途。

在结构中，变量使用以下语法定义：

```txt
(var *type* *name* [default <value>]) 
```

可以提供可选的默认值。

```txt
(var Real earthRadiusMultiplier :default 1.0)  
(var String myName :default "a name") 
```

# 操作

操作可以放在序列规则中的条目之前或之后。操作提供了一种在代理中存储数据的机制。操作放在‘[’‘]’字符之间。可以使用‘;’字符指定多个操作：

```txt
[mySetting1="ok";mySetting2=$1] 
```

有多种类型的操作：

赋值：为属性分配新值。attribute=value

```txt
side=blue  
icon="F-18"  
width="24 inches"  
height=$1 
```

值可以是文字值，也可以是用户输入的值引用。输入$0取自此序列中第一个规则的用户输入结果。$$ 表示前一个规则的结果：

```txt
{ side <string> [side=$1] | set width <Length> [width=$2] | make height equal to <Length> [height=$$] } 
```

作为快捷方式，属性名称可以在规则引用中使用以表示自动赋值。这是等效的：

```twig
{ side<$side>
| set width <$width>
| make height equal to <$height>
} 
```

push(attribute-name)

将当前值更新为指定属性。代理中的操作作用于当前对象，因此这将影响后续操作或子规则的处理方式，直到下一个子规则完成：

这将‘auxData’属性设置为当前对象，以便稍后由‘AuxData.block’规则中的命令修改：

```txt
{ [push(auxData)]<AuxData.block>   
} 
```

new(attribute-name, key-name)向ObjectMap属性添加新条目，并将当前对象设置为新值。

这会向类别添加一个新条目：

```txt
将命令链名称映射到指挥官名称(var ObjectMap/Strinng commandChains)  
{#当此规则匹配时，使用第一个用户输入添加一个新的命令链条目#然后将值分配给第二个用户输入。
```
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