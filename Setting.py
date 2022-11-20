# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Setting.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Setting_main(object):
    def setupUi(self, Setting_main):
        Setting_main.setObjectName("Setting_main")
        Setting_main.resize(800, 600)
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei UI")
        font.setPointSize(11)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        Setting_main.setFont(font)
        self.centralwidget = QtWidgets.QWidget(Setting_main)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 0, 191, 601))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.Bar = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.Bar.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.Bar.setContentsMargins(30, 0, 30, 0)
        self.Bar.setObjectName("Bar")
        self.pushButton_2 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_2.setEnabled(False)
        self.pushButton_2.setObjectName("pushButton_2")
        self.Bar.addWidget(self.pushButton_2, 1, 1, 1, 1)
        self.Normal_Setting_Button = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.Normal_Setting_Button.setObjectName("Normal_Setting_Button")
        self.Bar.addWidget(self.Normal_Setting_Button, 0, 1, 1, 1)
        self.Normal_Setting = QtWidgets.QFrame(self.centralwidget)
        self.Normal_Setting.setGeometry(QtCore.QRect(190, 0, 611, 601))
        self.Normal_Setting.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Normal_Setting.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Normal_Setting.setObjectName("Normal_Setting")
        self.Common_Text = QtWidgets.QLabel(self.Normal_Setting)
        self.Common_Text.setGeometry(QtCore.QRect(20, 10, 271, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.Common_Text.setFont(font)
        self.Common_Text.setObjectName("Common_Text")
        self.Language_Text = QtWidgets.QLabel(self.Normal_Setting)
        self.Language_Text.setGeometry(QtCore.QRect(20, 270, 271, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.Language_Text.setFont(font)
        self.Language_Text.setObjectName("Language_Text")
        self.Language = QtWidgets.QFrame(self.Normal_Setting)
        self.Language.setGeometry(QtCore.QRect(20, 300, 301, 51))
        self.Language.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Language.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Language.setObjectName("Language")
        self.English_Radio = QtWidgets.QRadioButton(self.Language)
        self.English_Radio.setGeometry(QtCore.QRect(10, 5, 81, 41))
        self.English_Radio.setObjectName("English_Radio")
        self.Traditional_Chinese_Radio = QtWidgets.QRadioButton(self.Language)
        self.Traditional_Chinese_Radio.setGeometry(QtCore.QRect(110, 0, 91, 51))
        self.Traditional_Chinese_Radio.setObjectName("Traditional_Chinese_Radio")
        self.Simplified_Chinese_Radio = QtWidgets.QRadioButton(self.Language)
        self.Simplified_Chinese_Radio.setGeometry(QtCore.QRect(210, 0, 101, 51))
        self.Simplified_Chinese_Radio.setObjectName("Simplified_Chinese_Radio")
        self.Common_Options = QtWidgets.QFrame(self.Normal_Setting)
        self.Common_Options.setGeometry(QtCore.QRect(19, 49, 341, 211))
        self.Common_Options.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Common_Options.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Common_Options.setObjectName("Common_Options")
        self.Minimize_Check = QtWidgets.QCheckBox(self.Common_Options)
        self.Minimize_Check.setGeometry(QtCore.QRect(10, 10, 311, 21))
        self.Minimize_Check.setObjectName("Minimize_Check")
        self.Main_Top_Check = QtWidgets.QCheckBox(self.Common_Options)
        self.Main_Top_Check.setGeometry(QtCore.QRect(10, 40, 311, 21))
        self.Main_Top_Check.setObjectName("Main_Top_Check")
        Setting_main.setCentralWidget(self.centralwidget)

        self.retranslateUi(Setting_main)
        QtCore.QMetaObject.connectSlotsByName(Setting_main)

    def retranslateUi(self, Setting_main):
        _translate = QtCore.QCoreApplication.translate
        Setting_main.setWindowTitle(_translate("Setting_main", "MainWindow"))
        self.pushButton_2.setText(_translate("Setting_main", "PushButton"))
        self.Normal_Setting_Button.setText(_translate("Setting_main", "一般設定"))
        self.Common_Text.setText(_translate("Setting_main", "常用選項"))
        self.Language_Text.setText(_translate("Setting_main", "語言選項"))
        self.English_Radio.setText(_translate("Setting_main", "English"))
        self.Traditional_Chinese_Radio.setText(_translate("Setting_main", "繁體中文"))
        self.Simplified_Chinese_Radio.setText(_translate("Setting_main", "简体中文"))
        self.Minimize_Check.setText(_translate("Setting_main", "最小化到托盤"))
        self.Main_Top_Check.setText(_translate("Setting_main", "主窗口置頂"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Setting_main = QtWidgets.QMainWindow()
    ui = Ui_Setting_main()
    ui.setupUi(Setting_main)
    Setting_main.show()
    sys.exit(app.exec_())
