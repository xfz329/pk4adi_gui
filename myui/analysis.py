# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'analysis.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import pandas as pd
import time
import os
import traceback

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QStringListModel
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QFileDialog

from pk4adi.pk import calculate_pk
from pk4adi.pkc import compare_pks

from utils.logger import Logger

class Ui_MainWindow(QtWidgets.QMainWindow):

    def __init__(self, data =None):
        super(QtWidgets.QMainWindow, self).__init__()
        self.setupUi(self)
        self.data = data
        self.log = Logger().get_logger()

        self.add2x = False
        self.add2y = False


        self.list_model_all = QStringListModel()
        self.listView_all.setModel(self.list_model_all)

        self.list_model_x = QStringListModel()
        self.listView_x.setModel(self.list_model_x)

        self.list_model_y = QStringListModel()
        self.listView_y.setModel(self.list_model_y)
        self.init_view()
        self.load_data(data)

        self.pk_columns = ["ID", "Independent variables", "Test variables", "PK", "SE0", "SE1", "Jackknife", "PKj", "SEj"]
        self.pks_columns = ["ID", "Independent variables", "Test variables A", "Test variables B",
                                           "PKD", "SED", "ZD", "P value of norm", "Comment 1",
                                           "PKDJ", "SEDJ", "DF", "TD", "P value of t", "Comment 2"]
        self.out_dir_set = False
        self.out_dir = None


    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.ApplicationModal)
        MainWindow.setEnabled(True)
        MainWindow.resize(1600, 900)
        MainWindow.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_all = QtWidgets.QLabel(self.centralwidget)
        self.label_all.setObjectName("label_all")
        self.gridLayout_2.addWidget(self.label_all, 0, 0, 1, 1)
        self.label_y = QtWidgets.QLabel(self.centralwidget)
        self.label_y.setObjectName("label_y")
        self.gridLayout_2.addWidget(self.label_y, 0, 2, 1, 1)
        self.pushButton_y = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_y.sizePolicy().hasHeightForWidth())
        self.pushButton_y.setSizePolicy(sizePolicy)
        self.pushButton_y.setObjectName("pushButton_y")
        self.gridLayout_2.addWidget(self.pushButton_y, 1, 1, 1, 1)
        self.listView_y = QtWidgets.QListView(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listView_y.sizePolicy().hasHeightForWidth())
        self.listView_y.setSizePolicy(sizePolicy)
        self.listView_y.setMinimumSize(QtCore.QSize(400, 300))
        self.listView_y.setObjectName("listView_y")
        self.gridLayout_2.addWidget(self.listView_y, 1, 2, 1, 1)
        self.label_x = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_x.sizePolicy().hasHeightForWidth())
        self.label_x.setSizePolicy(sizePolicy)
        self.label_x.setObjectName("label_x")
        self.gridLayout_2.addWidget(self.label_x, 2, 2, 1, 1)
        self.pushButton_x = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_x.sizePolicy().hasHeightForWidth())
        self.pushButton_x.setSizePolicy(sizePolicy)
        self.pushButton_x.setObjectName("pushButton_x")
        self.gridLayout_2.addWidget(self.pushButton_x, 3, 1, 1, 1)
        self.listView_x = QtWidgets.QListView(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listView_x.sizePolicy().hasHeightForWidth())
        self.listView_x.setSizePolicy(sizePolicy)
        self.listView_x.setMaximumSize(QtCore.QSize(400, 16777215))
        self.listView_x.setObjectName("listView_x")
        self.gridLayout_2.addWidget(self.listView_x, 3, 2, 1, 1)
        self.listView_all = QtWidgets.QListView(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listView_all.sizePolicy().hasHeightForWidth())
        self.listView_all.setSizePolicy(sizePolicy)
        self.listView_all.setMinimumSize(QtCore.QSize(400, 0))
        self.listView_all.setMaximumSize(QtCore.QSize(400, 16777215))
        self.listView_all.setObjectName("listView_all")
        self.gridLayout_2.addWidget(self.listView_all, 1, 0, 3, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_pk = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_pk.setMinimumSize(QtCore.QSize(100, 0))
        self.pushButton_pk.setObjectName("pushButton_pk")
        self.gridLayout.addWidget(self.pushButton_pk, 0, 0, 1, 1)
        self.pushButton_pks = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_pks.setMinimumSize(QtCore.QSize(100, 0))
        self.pushButton_pks.setObjectName("pushButton_pks")
        self.gridLayout.addWidget(self.pushButton_pks, 0, 1, 1, 1)
        self.pushButton_export = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_export.setMinimumSize(QtCore.QSize(100, 0))
        self.pushButton_export.setObjectName("pushButton_export")
        self.gridLayout.addWidget(self.pushButton_export, 0, 2, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 3, 1, 1)
        self.label_result_title = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_result_title.sizePolicy().hasHeightForWidth())
        self.label_result_title.setSizePolicy(sizePolicy)
        self.label_result_title.setObjectName("label_result_title")
        self.gridLayout.addWidget(self.label_result_title, 1, 0, 1, 1)
        self.label_result = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.label_result.sizePolicy().hasHeightForWidth())
        self.label_result.setSizePolicy(sizePolicy)
        self.label_result.setMinimumSize(QtCore.QSize(250, 0))
        self.label_result.setText("")
        self.label_result.setAlignment(QtCore.Qt.AlignCenter)
        self.label_result.setObjectName("label_result")
        self.gridLayout.addWidget(self.label_result, 2, 0, 1, 4)
        spacerItem1 = QtWidgets.QSpacerItem(188, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 1, 1, 1, 3)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 3, 4, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "计算PK"))
        self.label_all.setText(_translate("MainWindow", "所有变量"))
        self.label_y.setText(_translate("MainWindow", "独立变量"))
        self.pushButton_y.setText(_translate("MainWindow", "添加"))
        self.label_x.setText(_translate("MainWindow", "检验变量"))
        self.pushButton_x.setText(_translate("MainWindow", "添加"))
        self.pushButton_pk.setText(_translate("MainWindow", "计算PK值"))
        self.pushButton_pks.setText(_translate("MainWindow", "比较PK值"))
        self.pushButton_export.setText(_translate("MainWindow", "导出结果"))
        self.label_result_title.setText(_translate("MainWindow", "结果显示"))

    def init_outdir(self):
        QMessageBox.information(None, "设置输出目录", "请设置本次分析的输出目录", QMessageBox.Ok)
        result = QFileDialog.getExistingDirectory(self, "选择一个文件夹", "./")
        while not os.path.exists(result):
            QMessageBox.critical(None, "输出目录设置失败", "请重新选择输出目录！", QMessageBox.Ok)
            result = QFileDialog.getExistingDirectory(self, "选择一个文件夹", "./")

        full_path = result + "/Analysis_" +time.strftime("%Y-%m-%d", time.localtime())
        if not os.path.exists(full_path):
            os.mkdir(full_path)
        QMessageBox.information(None, "输出目录设置成功", "本次分析的输出目录已设置为 " + full_path, QMessageBox.Ok)
        self.out_dir_set = True
        self.out_dir = full_path
        self.log.info(full_path)
        os.startfile(full_path)


    def load_data(self,df):
        if isinstance(df,pd.DataFrame):
            self.list_model_all.setStringList(df.columns)


    def init_view(self):
        self.pushButton_x.setEnabled(False)
        self.pushButton_y.setEnabled(False)

        self.listView_all.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)
        self.listView_all.clicked.connect(self.enable_all_buttons)

        self.listView_x.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)
        self.listView_x.clicked.connect(self.disable_button_x)

        self.listView_y.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)
        self.listView_y.clicked.connect(self.disable_button_y)

        self.pushButton_x.clicked.connect(self.clicked_button_x)
        self.pushButton_y.clicked.connect(self.clicked_button_y)
        self.pushButton_pk.clicked.connect(self.clicked_button_pk)
        self.pushButton_pks.clicked.connect(self.clicked_button_pks)

    def enable_all_buttons(self):
        self.add2x = True
        self.add2y = True
        self.pushButton_x.setEnabled(True)
        self.pushButton_y.setEnabled(True)
        self.pushButton_x.setText("添加")
        self.pushButton_y.setText("添加")
        if not self.out_dir_set:
            self.init_outdir()

    def disable_button_x(self):
        self.add2x = False
        self.pushButton_x.setText("移除")

    def disable_button_y(self):
        self.add2y = False
        self.pushButton_y.setText("移除")

    def exchange_selected_list(self, start, end):
        selected = start.selectedIndexes()
        for i in selected:
            num = i.row()
            temp = start.model().stringList()
            line = temp[num]
            del (temp[num])
            start.model().setStringList(temp)
            temp = end.model().stringList()
            temp.append(line)
            end.model().setStringList(temp)

    def clicked_button_x(self):
        if self.add2x:
            self.exchange_selected_list(self.listView_all, self.listView_x)
        else:
            self.exchange_selected_list(self.listView_x, self.listView_all)

    def clicked_button_y(self):
        if self.add2y:
            if len(self.listView_y.model().stringList()) == 0 :
                self.exchange_selected_list(self.listView_all, self.listView_y)
            else:
                QMessageBox.warning(None, "参数错误", "一次分析只能设置一个独立变量！", QMessageBox.Ok)
        else:
            self.exchange_selected_list(self.listView_y, self.listView_all)

    def clicked_button_pk(self):
        pk_ready = len(self.listView_x.model().stringList()) > 0 and len(self.listView_y.model().stringList()) > 0
        if not pk_ready:
            QMessageBox.warning(None, "参数错误", "一次分析需要设置一个独立变量和至少一个检验变量！", QMessageBox.Ok)
            return
        y_name = self.listView_y.model().stringList()[0]
        x_names = self.listView_x.model().stringList()

        df = pd.DataFrame(columns = self.pk_columns)
        index = 0

        for x_name in x_names:
            ans = self.pk(x_name,y_name)
            if None != ans:
                new_row = [index + 1, y_name, x_name, ans.get("PK"), ans.get("SE0"), ans.get("SE1"),
                           ans.get("jack_ok"), ans.get("PKj"), ans.get("SEj")]
                df.loc[index] = new_row
                index = index + 1

        self.log.info(df)

        pre = time.strftime("%H-%M-%S", time.localtime()) + "_PK"
        csv_name = self.out_dir + "/" +pre + "_.csv"
        xlsx_name = self.out_dir + "/" +pre + "_.xlsx"
        self.log.info(csv_name)
        self.log.info(xlsx_name)

        try:
            df.to_csv(csv_name)
            df.to_excel(xlsx_name)
        except Exception as e:
            self.log.error(e)
            info = traceback.format_exc()
            self.log.error(info)
            self.log.error("Error")





    def clicked_button_pks(self):
        pks_ready = len(self.listView_x.model().stringList()) > 1 and len(self.listView_y.model().stringList()) > 0
        if not pks_ready:
            QMessageBox.warning(None, "参数错误", "一次分析需要设置一个独立变量和至少两个检验变量！", QMessageBox.Ok)
            return
        y_name = self.listView_y.model().stringList()[0]
        x_names = self.listView_x.model().stringList()

        df = pd.DataFrame(columns = self.pks_columns)
        index = 0

        for i in x_names:
            for j in x_names:
                if i != j :
                    pk1 = self.pk(i, y_name)
                    pk2 = self.pk(j, y_name)
                    if None != pk1 and None != pk2:
                        ans = self.pks(pk1, pk2)
                        new_row = [index + 1, y_name, i, j,
                                   ans.get("PKD"), ans.get("SED"), ans.get("ZD"), ans.get("ZP"), ans.get("ZJ"),
                                   ans.get("PKDJ"), ans.get("SEDJ"), ans.get("DF"), ans.get("TD"), ans.get("TP"),ans.get("TJ")]
                        df.loc[index] = new_row
                        index = index + 1

        self.log.info(df)

        pre = time.strftime("%H-%M-%S", time.localtime()) + "_PKC"
        csv_name = self.out_dir + "/" + pre + "_.csv"
        xlsx_name = self.out_dir + "/" + pre + "_.xlsx"
        self.log.info(csv_name)
        self.log.info(xlsx_name)

        try:
            df.to_csv(csv_name)
            df.to_excel(xlsx_name)
        except Exception as e:
            self.log.error(e)
            info = traceback.format_exc()
            self.log.error(info)
            self.log.error("Error")


    def pk(self, xn, yn):
        x = self.data.loc[:,xn]
        y = self.data.loc[:,yn]

        if x.apply(lambda n: not isinstance(n, (int, float))).any():
            QMessageBox.warning(None, "值错误", "检验变量 "+ xn + " 数据类型错误，需要为整型或浮点型！", QMessageBox.Ok)
            return None
        if x.isna().any():
            QMessageBox.warning(None, "值错误", "检验变量 " + xn + " 包含非数值字符！", QMessageBox.Ok)
            return None
        if y.apply(lambda n: not isinstance(n, (int, float))).any():
            QMessageBox.warning(None, "值错误", "独立变量 "+ yn + " 数据类型错误，需要为整型或浮点型！", QMessageBox.Ok)
            return None
        if y.isna().any():
            QMessageBox.warning(None, "值错误", "独立变量 " + yn + " 包含非数值字符！", QMessageBox.Ok)
            return None
        lx = len(x)
        ly = len(y)
        if lx != ly or lx < 2:
            QMessageBox.warning(None, "数据长度错误", "独立变量" + yn + " 与观测变量 " + xn + "长度不等或长度小于2。", QMessageBox.Ok)
            return None
        sy = y.tolist()
        if len(set(sy)) < 2:
            QMessageBox.warning(None, "值错误", "独立变量" + yn + "需要包含至少2个区分数值。", QMessageBox.Ok)
            return None

        ans = calculate_pk(x, y, False)
        self.log.info(ans)

        return ans


    def pks(self, pk1, pk2):
        ans = compare_pks(pk1, pk2, False)
        self.log.info(ans)
        return ans