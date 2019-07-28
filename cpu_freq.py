# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CPU Freq.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import os

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setMaximumSize(QtCore.QSize(322, 0))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setPalette(palette)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.MainLayout = QtWidgets.QVBoxLayout()
        self.MainLayout.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.MainLayout.setSpacing(5)
        self.MainLayout.setObjectName("MainLayout")
        self.Headline_2 = QtWidgets.QFrame(self.centralwidget)
        self.Headline_2.setMaximumSize(QtCore.QSize(16777215, 167777))
        self.Headline_2.setPalette(palette)
        self.Headline_2.setAutoFillBackground(True)
        self.Headline_2.setFrameShape(QtWidgets.QFrame.Box)
        self.Headline_2.setObjectName("Headline_2")
        self.Headline = QtWidgets.QHBoxLayout(self.Headline_2)
        self.Headline.setSpacing(15)
        self.Headline.setObjectName("Headline")
        spacerItem = QtWidgets.QSpacerItem(130, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.Headline.addItem(spacerItem)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label = QtWidgets.QLabel(self.Headline_2)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.Headline.addWidget(self.label, 0, QtCore.Qt.AlignTop)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.Headline.addItem(spacerItem1)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5 = QtWidgets.QLabel(self.Headline_2)
        self.label_5.setMaximumSize(QtCore.QSize(64, 64))
        self.label_5.setText("")
        path = os.path.abspath(os.path.dirname(os.path.abspath(__file__))+'/res/pic.png')
        self.label_5.setPixmap(QtGui.QPixmap(path))
        self.label_5.setScaledContents(True)
        self.label_5.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.Headline.addWidget(self.label_5)
        self.MainLayout.addWidget(self.Headline_2)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setPalette(palette)
        self.frame.setAutoFillBackground(True)
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout.addWidget(self.label_6)
        self.horizontalSlider = QtWidgets.QSlider(self.frame)
        self.horizontalSlider.setFont(font)
        self.horizontalSlider.setMinimum(10)
        self.horizontalSlider.setMaximum(100)
        self.horizontalSlider.setSliderPosition(30)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setTickPosition(QtWidgets.QSlider.TicksBothSides)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.horizontalLayout.addWidget(self.horizontalSlider)
        self.MainLayout.addWidget(self.frame)
        self.MainLayout.setStretch(0, 10)
        self.MainLayout.setStretch(1, 10)
        self.MainLayout.setStretch(2, 10)
        self.verticalLayout_2.addLayout(self.MainLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 490, 20))
        self.menubar.setObjectName("menubar")
        self.menuOmg = QtWidgets.QMenu(self.menubar)
        self.menuOmg.setObjectName("menuOmg")
        MainWindow.setMenuBar(self.menubar)
        self.actionClose = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon.fromTheme("exit")
        self.actionClose.setIcon(icon)
        self.actionClose.setObjectName("actionClose")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon.fromTheme("about")
        self.actionAbout.setIcon(icon)
        self.actionAbout.setObjectName("actionAbout")
        self.menuOmg.addAction(self.actionClose)
        self.menuOmg.addAction(self.actionAbout)
        self.menubar.addAction(self.menuOmg.menuAction())
        self.retranslateUi(MainWindow)
        self.actionClose.triggered.connect(MainWindow.close)
        self.actionAbout.setEnabled(False)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "CPU Freq"))
        self.label.setText(_translate("MainWindow", "INTEL i7-3610QM "))
        self.label_6.setText(_translate("MainWindow", "Update interval:"))
        self.menuOmg.setTitle(_translate("MainWindow", "App"))
        self.actionClose.setText(_translate("MainWindow", "Close"))
        self.actionAbout.setText(_translate("MainWindow", "by Nikola Stojicic"))


