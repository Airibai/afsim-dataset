```cpp
QList<wkf::PrefWidget> WarlockTraining::Plugin::GetPreferencesWidgets() const
{
    // EXERCISE 2 TASK 1a
    // return a QList that contains the PrefWidget.
    // This will add the widget to the Preferences display.
    return { mPrefWidget };
}
QList<wkf::Action> WarlockTraining::Plugin::GetActions() const
{
    // EXERCISE 2 TASK 1b
    // return the QList of Actions. This will add the actions to the Preferences' KeyBinding menu.
    return mActions;
} 
```

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

# UNCLASSIFIED

![](images/92f616129c1b6cbdc3bb9cee49153231e8ebe4f1db6527a74f98c1e50768aa1c.jpg)

# 练习2 - Review 1

71

![](images/8cc8be3c357156b50ce993373755fd81e19610427acab1e47d86bf8616da89e7.jpg)

- 检查 PrefObject 类（位于 PrefObject.hpp 和 PrefObject.cpp 文件中）：

- 该类负责将首选项数据读写到 Settings.ini 文件中。  
- 该类会通知订阅者首选项数据的更改。  
- 该类处理用户通过显示在首选项对话框中的 PrefWidget 更新首选项数据的操作。

namespace WarlockTraining   
```txt
{   
//! This represents the data that the preferences widget modifies.   
//! @note A default constructed PrefData is used for the default preferences.   
//! Use default member initializers (as used here), and/or a default constructor.   
struct PrefData   
{ bool mDisplayAltitude = true; bool mDisplayHeading = true;   
}；   
//! This provides an interface to load, save, and apply changes to the preferences.   
//! Inheriting from wkf::PrefObject<T> tells the class what type of data it is dealing with. class PrefObject : public wkf::PrefObjectT<PrefData>   
{ // This line is required for Qt signals to be properly emitted from this class. Q_OBJECT   
public: static constexpr const char* cNAME = "WarlockTrainingPreferences"; PrefObject(QObject* aParent = nullptr); ~PrefObject() override = default;   
//! Applies changes to the PrefData to the rest of the application. //! Called internally AFTER SetPreferenceDataP(). void Apply() override; 
```

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19.

Other requests for this document shall be referred to AFRL/RQQD.

73

# UNCLASSIFIED

# 练习2 - Review 1

# PrefObject.hpp

![](images/f7a6be4e87f8489e138131fc9d45f949a3bba0af3bdd9dfecbbd36253eecd2f3.jpg)

![](images/4d5f64f1b4d5c27aa21df95e0b352c5ebd5e68f8db2280aaf60e21f02a93977e.jpg)

```txt
// Sets the current preferences.
// If applying changes to every preference would cause a significant delay,
// this function is where flags can be set to indicate which preferences need re-applied.
// @param aPrefData This is the new preferences.
void SetPreferenceDataP(const PrefData& aPrefData) override;
// Reads the current preferences from a file.
// @param aSettings This is the interface to the file where preference data is stored.
// @returns The settings read.
PrefData ReadSettings(QSettings& aSettings) const override;
// Saves the current preferences to a file.
// @param aSettings This is the interface to the file where preference data is stored.
void SaveSettingsP(QSettings& aSettings) const override;
signals:
// Used by Apply() to only update the display when the preferences have actually changed.
// @param aPreferences This is the current preferences.
// @note In practice, one could have multiple such functions to update each non-trivial setting.
void Changed(const PrefData& aPreferences);
private:
// Represents whether the preferences have changed.
bool mPreferencesChanged = false;
}; 
```

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19.

Other requests for this document shall be referred to AFRL/RQQD.

WarlockTraining::PrefObject::PrefObject(QObject* aParent /\*=0\*/) :wkf::PrefObjectT<PrefData>(aParent, "WarlockTraining")   
}   
void WarlockTraining::PrefObject::Apply()   
{ //If Preferences have changed, we need to notify subscribers if (mPreferencesChanged) { emit Changed(mCurrentPrefs); mPreferencesChanged $=$ false; }   
}   
void WarlockTraining::PrefObject::SetPreferenceDataP(const PrefData& aPrefData)   
{ // Check to see if the new value for the preferences are different than the current values // If so, updated the mPreferencesChanged flag if (mCurrentPrefs.mDisplayAltitude != aPrefData.mDisplayAltitude || mCurrentPrefs.mDisplayHeading != aPrefData.mDisplayHeading) { mPreferencesChanged $=$ true; mCurrentPrefs = aPrefData; }   
}

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

75

![](images/5995f84852e64ecc2da01a6c782497fb363477999ba4841070be87932bcb4260.jpg)

UNCLASSIFIED

# 练习2 - Review 1

PrefObject.cpp

![](images/bdbcc82f202f52e0ae8fe1b5294f80a8654843c509b2977f82709f21e6122a47.jpg)

```javascript
WarlockTraining::PrefData WarlockTraining::PrefObject::ReadSettings(QSettings& aSettings) const { PrefData pData; //Read the settings from the QSettings file pData.mDisplayAltitude = aSettings.value("showAltitude", mDefaultPrefs.mDisplayAltitude).toBool(); pData.mDisplayHeading = aSettings.value("showHeading", mDefaultPrefs.mDisplayHeading).toBool(); return pData; } void WarlockTraining::PrefObject::SaveSettingsP(QSettings& aSettings) const { //Write the settings to the QSettings file aSettingsSetValue("showAltitude", mCurrentPrefs.mDisplayAltitude); aSettingsSetValue("showHeading", mCurrentPrefs.mDisplayHeading); } 
```

```cpp
namespace WarlockTraining   
{ //! This represents the specific preferences widget associated with our plugin. //! Inheriting from wkf::PrefWidgetT<T> tells the class what type of PrefObject it is dealing with. class PrefWidget : public wkf::PrefWidgetT<PrefObject> { public: explicit PrefWidget(QWidget* aParent = nullptr); private: Ui::WarlockTrainingPrefs mUI; //! Updates the widget with the current preferences. //! @param aPrefData This is the current preferences. void ReadPreferenceData(const PrefData& aPrefData) override; //! Writes the preferences shown in the widget to the current preferences. //! @param aPrefData This is the current preferences. void WritePreferenceData(PrefData& aPrefData) override; }; } 
```

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

77

![](images/1d1091c721b323329e3b0c261965d6ba5debc4761efb243c4fd56330f4a9f13c.jpg)

# UNCLASSIFIED

# 练习2- 任务2

# PrefWidget.cpp

![](images/89a5360bcd35938ffe0c91665bd7e0561a721a4dcbdbe1ad0f6eea8d4a6d8f04.jpg)

- 显示当前的首选项数据，并允许用户更改这些数据：

a) 在 PrefWidget.cpp 中，将复选框的状态更新为与 PrefData 的状态一致：

- mUI 成员变量是一个类，其中包含成员 altitudeCheckBox 和 headingCheckBox。  
- 调用这两个成员的 setChecked 方法，分别传入 aPrefData.mDisplayAltitude 和 aPrefData.mDisplayHeading。

b) 读取复选框的状态并更新发送到 PrefObject 的 PrefData:

- 调用这两个成员的 isChecked 方法，并使用结果来设置 PrefData 的两个成员变量。

```cpp
void WarlockTraining::PrefWidget::ReadPreferenceData(const PrefData& aPrefData)  
{ // EXERCISE 2 TASK 2a // Call setChecked() on altitudeCheckBox & headingCheckBox using the data in aPrefData mUI.altitudeCheckBox->setChecked(aPrefData.mDisplayAltitude); mUIheadingCheckBox->setChecked(aPrefData.mDisplayHeading);  
}  
void WarlockTraining::PrefWidget::WritePreferenceData(PrefData& aPrefData)  
{ // EXERCISE 2 TASK 2b // Set aPrefData based on the altitude and heading checkboxes aPrefData.mDisplayAltitude = mUI.altitudeCheckBox->isChecked(); aPrefData.mDisplayHeading = mUIheadingCheckBox->isChecked();  
} 
```

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQQD.

# UNCLASSIFIED

# 练习2-任务3

79

![](images/1b5d9afbb1e5327b111efc716e56a5404ac064e0b2bd1c2e019439eb2f7ede31.jpg)

![](images/f513e7c1690e4240af734e3538a89c64c41ec073cbbf9a0c26227695800624ea.jpg)

- 在 DockWidget.cpp 中，根据用户的首选项更新显示内容：

1. 将 PrefObject 参数的 Changed 信号连接到 DockWidget 的 PreferencesChanged 函数。  
2. 更新高度和航向的标签及行编辑框的可见性，使其与 PrefData 参数的 mDisplayAltitude 和 mDisplayHeading 成员相匹配。

```cpp
WarlockTraining::DockWidget::DockWidget(SimInterface& aSimInterface, DataContainer& aDataContainer, PrefObject* aPrefObject, Qt::WindowFlags aWindowFlags) : QDockWidget(nullptr, aWindowFlags) , mSimInterface(aSimInterface) , mDataContainer(aDataContainer)   
{ //! Without this line, nothing will show up in the dock widget. mUI_setupUi(this); // EXERCISE 1 TASK 2a // Connect the DataContainer's DataChanged signal to UpdateDisplay() // Connect the WkfEnvironment's PlatformOfInterestChanged signal to PlatformOfInterestChanged() connect(&mDataContainer, &DataContainer::DataChanged, this, &DockWidget::UpdateDisplay); connect(&wkfEnv, &wkf::Environment::PlatformOfInterestChanged, this, &DockWidget::PlatformOfInterestChanged); // EXERCISE 2 TASK 3a // Connect the PrefObject's Changed() signal to PreferencesChanged() connect(aPrefObject, &WarlockTraining::PrefObject::Changed, this, &DockWidget::PreferencesChanged); // EXERCISE 1 TASK 3a // connect the clicked signal for northPushButton, eastPushButton, southPushButton, and westPushButton // to TurnHeading with appropriate heading passed in as an argument connect(mUI.northPushButton, &QPushButton:::clickcd, this, [this]( ) { TurnToHeading(0); }); connect(mUI.eastPushButton, &QPushButton:::clickcd, this, [this]( ) { TurnToHeading(90); }); connect(mUI.southPushButton, &QPushButton:::clickcd, this, [this]( ) { TurnToHeading(180); }); connect(mUI.westPushButton, &QPushButton:::clickcd, this, [this]( ) { TurnToHeading(270); }); } 
```

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

81

![](images/82ef44005ac7469ba9eb729696d5c6a91bd742ecfb475d600f73377c5639ad1e.jpg)

# UNCLASSIFIED

# 解决方案- 练习2 任务3b

# DockWidget.cpp

![](images/60ff0d36a687ded0c186c25f1c17fb4df6ee78425e742fa5b23d1ff53b199857.jpg)

```cpp
void WarlockTraining::DockWidget::PreferencesChanged(const PrefData& aPrefData)  
{ // EXERCISE 2 TASK 3b // Hide/Show the altitude/heading labels & lineEdits based on the user selection in Preferences. mUI.altitudeLabel->setVisible(aPrefData.mDisplayAltitude); mUI.altitudeLineEdit->setVisible(aPrefData.mDisplayAltitude); mUIheadingLabel->setVisible(aPrefData.mDisplayHeading); mUIheadingLineEdit->setVisible(aPrefData.mDisplayHeading); } 
```

- 您应该能够在“首选项”中的“键盘快捷键”菜单中重新绑定控制飞机移动的操作。  
- 您还应该能够通过“首选项”中的“Warlock Training”菜单切换高度和航向的显示。  
- 从 Windows Visual Studio 执行以下操作：

1. 在“Release”模式下构建解决方案。  
2. 构建"INSTALL"项目。

- 从Linux执行以下命令（在构建目录中）：：

$ cmake --build . --target all -- -j12

$ cmake --build . --target install -- -j12

- 运行 Warlock 的测试场景：

1. 运行warlock.exe。  
2. 加载测试场景，路径为：training\developer\wkflabs\data\wkf_trainingscenario.txt。

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQQD.

83

![](images/3d257d9db0b7a398347992341137e8ab39526cff8a10c0f01123a2f7c15055f2.jpg)

# UNCLASSIFIED

# 测试

![](images/d71695652d196e59c93c06a7dc95e1ce3b3c067ae3a2444bae7bc64978058d54.jpg)

![](images/1a0b06512e0d1a61c881dd5d83fe03d8e65fa1a463a82c2a1fa7d9d9b2b6096c.jpg)

![](images/1613f9e8e5a11892371a9edca9c5ed3089fc652b930441d418489277da2b579f.jpg)

DISTRIBUTION C. Distribution authorized to U.S. Government Agencies and their contractors, 9-Aug-19. Other requests for this document shall be referred to AFRL/RQD.

# 7. 官方附带Demo功能说明

待更新

# 8. 源代码结构分析

待更新