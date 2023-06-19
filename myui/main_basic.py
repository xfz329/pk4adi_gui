# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_basic.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1600, 900)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1600, 22))
        self.menubar.setObjectName("menubar")
        self.menu_file = QtWidgets.QMenu(self.menubar)
        self.menu_file.setObjectName("menu_file")
        self.menu_window = QtWidgets.QMenu(self.menubar)
        self.menu_window.setObjectName("menu_window")
        self.menu_new_win = QtWidgets.QMenu(self.menu_window)
        self.menu_new_win.setObjectName("menu_new_win")
        self.menu_config = QtWidgets.QMenu(self.menubar)
        self.menu_config.setObjectName("menu_config")
        self.menu_language = QtWidgets.QMenu(self.menu_config)
        self.menu_language.setObjectName("menu_language")
        self.menu_about = QtWidgets.QMenu(self.menubar)
        self.menu_about.setObjectName("menu_about")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action_open = QtWidgets.QAction(MainWindow)
        self.action_open.setObjectName("action_open")
        self.action_new_win_data = QtWidgets.QAction(MainWindow)
        self.action_new_win_data.setObjectName("action_new_win_data")
        self.action_new_win_analysis = QtWidgets.QAction(MainWindow)
        self.action_new_win_analysis.setObjectName("action_new_win_analysis")
        self.action_tile_subwin = QtWidgets.QAction(MainWindow)
        self.action_tile_subwin.setObjectName("action_tile_subwin")
        self.action_ch = QtWidgets.QAction(MainWindow)
        self.action_ch.setObjectName("action_ch")
        self.action_en = QtWidgets.QAction(MainWindow)
        self.action_en.setObjectName("action_en")
        self.action_outdir = QtWidgets.QAction(MainWindow)
        self.action_outdir.setObjectName("action_outdir")
        self.action_kernel = QtWidgets.QAction(MainWindow)
        self.action_kernel.setObjectName("action_kernel")
        self.action_author = QtWidgets.QAction(MainWindow)
        self.action_author.setObjectName("action_author")
        self.action_logs = QtWidgets.QAction(MainWindow)
        self.action_logs.setObjectName("action_logs")
        self.action_lisence = QtWidgets.QAction(MainWindow)
        self.action_lisence.setObjectName("action_lisence")
        self.menu_file.addAction(self.action_open)
        self.menu_new_win.addAction(self.action_new_win_data)
        self.menu_new_win.addAction(self.action_new_win_analysis)
        self.menu_window.addAction(self.menu_new_win.menuAction())
        self.menu_window.addAction(self.action_tile_subwin)
        self.menu_language.addAction(self.action_ch)
        self.menu_language.addAction(self.action_en)
        self.menu_config.addAction(self.menu_language.menuAction())
        self.menu_config.addAction(self.action_outdir)
        self.menu_about.addAction(self.action_kernel)
        self.menu_about.addAction(self.action_author)
        self.menu_about.addAction(self.action_logs)
        self.menu_about.addAction(self.action_lisence)
        self.menubar.addAction(self.menu_file.menuAction())
        self.menubar.addAction(self.menu_window.menuAction())
        self.menubar.addAction(self.menu_config.menuAction())
        self.menubar.addAction(self.menu_about.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "PK4ADI"))
        self.menu_file.setTitle(_translate("MainWindow", "文件"))
        self.menu_window.setTitle(_translate("MainWindow", "窗口"))
        self.menu_new_win.setTitle(_translate("MainWindow", "新建"))
        self.menu_config.setTitle(_translate("MainWindow", "配置"))
        self.menu_language.setTitle(_translate("MainWindow", "语言"))
        self.menu_about.setTitle(_translate("MainWindow", "关于"))
        self.action_open.setText(_translate("MainWindow", "打开"))
        self.action_open.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.action_new_win_data.setText(_translate("MainWindow", "数据窗口"))
        self.action_new_win_data.setShortcut(_translate("MainWindow", "Ctrl+D"))
        self.action_new_win_analysis.setText(_translate("MainWindow", "分析窗口"))
        self.action_new_win_analysis.setShortcut(_translate("MainWindow", "Ctrl+A"))
        self.action_tile_subwin.setText(_translate("MainWindow", "平铺"))
        self.action_tile_subwin.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.action_ch.setText(_translate("MainWindow", "中文"))
        self.action_en.setText(_translate("MainWindow", "English"))
        self.action_outdir.setText(_translate("MainWindow", "默认输出文件夹"))
        self.action_kernel.setText(_translate("MainWindow", "分析内核"))
        self.action_author.setText(_translate("MainWindow", "作者"))
        self.action_logs.setText(_translate("MainWindow", "更新日志"))
        self.action_lisence.setText(_translate("MainWindow", "协议"))
