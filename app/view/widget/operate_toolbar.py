#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   operate_toolbar.py    
@Contact :   Jiang Feng(silencejiang@zju.edu.cn)
@License :   (C)Copyright 2004-2020, Zhejiang University
"""
from PyQt5.QtCore import Qt, pyqtSignal, QUrl, QEvent
from PyQt5.QtGui import QDesktopServices, QPainter, QPen, QColor
from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QHBoxLayout, QFrame

from qfluentwidgets import (ScrollArea, PushButton, ToolButton, FluentIcon, PrimaryPushButton, SplitPushButton, SwitchButton,
                            isDarkTheme, IconWidget, Theme, ToolTipFilter, TitleLabel, CaptionLabel,
                            StrongBodyLabel, BodyLabel)

from .toolbar import ToolBar
from .separator_widget import SeparatorWidget

class OperateToolBar(ToolBar):
    """ Operate Tool bar """

    def __init__(self, title, subtitle, parent=None):
        super().__init__(title = title, subtitle = subtitle, parent=parent)

        self.calcaulateButton = PrimaryPushButton("计算PK", self)
        self.compareButton = PrimaryPushButton("比较PK", self)
        self.separator1 = SeparatorWidget(self)
        self.openDirButton = PrimaryPushButton("打开输出文件夹", self)
        self.separator2 = SeparatorWidget(self)
        self.commentSwitchButton = SwitchButton("记录关")
        self.themeButton = ToolButton(FluentIcon.CONSTRACT, self)

        self.__initButtonLayout()


    def __initButtonLayout(self):
        self.buttonLayout.setSpacing(4)
        self.buttonLayout.setContentsMargins(0, 0, 0, 0)
        self.buttonLayout.addWidget(self.calcaulateButton, 0, Qt.AlignLeft)
        self.buttonLayout.addWidget(self.compareButton, 0, Qt.AlignLeft)
        self.buttonLayout.addWidget(self.separator1, 0, Qt.AlignLeft)
        self.buttonLayout.addWidget(self.openDirButton, 0, Qt.AlignLeft)
        self.buttonLayout.addWidget(self.separator2, 0, Qt.AlignLeft)
        self.buttonLayout.addWidget(self.commentSwitchButton, 0, Qt.AlignLeft)
        self.buttonLayout.addStretch(1)
        self.buttonLayout.addWidget(self.themeButton, 0, Qt.AlignRight)
        self.buttonLayout.setAlignment(Qt.AlignVCenter | Qt.AlignLeft)

        self.commentSwitchButton.checkedChanged.connect(self.onSwitchCheckedChanged)
        self.themeButton.installEventFilter(ToolTipFilter(self.themeButton))
        self.themeButton.clicked.connect(self.toggleTheme)


    def onSwitchCheckedChanged(self, isChecked):
        if isChecked:
            self.commentSwitchButton.setText("记录开")
        else:
            self.commentSwitchButton.setText("记录关")