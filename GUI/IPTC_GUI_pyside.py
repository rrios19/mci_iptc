# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'IPTC_GUI.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import icons_rc
import icons_rc
import icons_rc

class Ui_IPTC(object):
    def setupUi(self, IPTC):
        if not IPTC.objectName():
            IPTC.setObjectName(u"IPTC")
        IPTC.resize(776, 532)
        IPTC.setMaximumSize(QSize(16777215, 800))
        icon = QIcon()
        icon.addFile(u":/icons/icons/IPTC_logo.svg", QSize(), QIcon.Normal, QIcon.Off)
        IPTC.setWindowIcon(icon)
        IPTC.setStyleSheet(u"*{\n"
"	border:none;\n"
"}\n"
"")
        self.centralwidget = QWidget(IPTC)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_5 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.mainwindow = QFrame(self.centralwidget)
        self.mainwindow.setObjectName(u"mainwindow")
        self.mainwindow.setMaximumSize(QSize(16777215, 16777215))
        self.mainwindow.setFrameShape(QFrame.StyledPanel)
        self.mainwindow.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.mainwindow)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.project_info = QFrame(self.mainwindow)
        self.project_info.setObjectName(u"project_info")
        self.project_info.setMaximumSize(QSize(16777215, 100))
        self.project_info.setFrameShape(QFrame.StyledPanel)
        self.project_info.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.project_info)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SetNoConstraint)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_20 = QFrame(self.project_info)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setMaximumSize(QSize(80, 30))
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_20)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.minimize_btn = QPushButton(self.frame_20)
        self.minimize_btn.setObjectName(u"minimize_btn")
        self.minimize_btn.setMinimumSize(QSize(20, 20))
        self.minimize_btn.setMaximumSize(QSize(20, 20))
        self.minimize_btn.setStyleSheet(u"QPushButton:hover{\n"
"background-color:#ffff00;\n"
"}\n"
"QPushButton{\n"
"border-top-left-radius:10px;\n"
"border-top-right-radius:10px;\n"
"border-bottom-left-radius:10px;\n"
"border-bottom-right-radius:10px;\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/minus.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.minimize_btn.setIcon(icon1)

        self.horizontalLayout_7.addWidget(self.minimize_btn)

        self.maximize_btn = QPushButton(self.frame_20)
        self.maximize_btn.setObjectName(u"maximize_btn")
        self.maximize_btn.setEnabled(True)
        self.maximize_btn.setMinimumSize(QSize(20, 20))
        self.maximize_btn.setMaximumSize(QSize(20, 20))
        self.maximize_btn.setStyleSheet(u"QPushButton:hover{\n"
"background-color:#00ff00;\n"
"}\n"
"QPushButton{\n"
"border-top-left-radius:10px;\n"
"border-top-right-radius:10px;\n"
"border-bottom-left-radius:10px;\n"
"border-bottom-right-radius:10px;\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/maximize-2.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.maximize_btn.setIcon(icon2)

        self.horizontalLayout_7.addWidget(self.maximize_btn)

        self.close_btn = QPushButton(self.frame_20)
        self.close_btn.setObjectName(u"close_btn")
        self.close_btn.setMinimumSize(QSize(20, 20))
        self.close_btn.setMaximumSize(QSize(20, 20))
        self.close_btn.setStyleSheet(u"QPushButton{\n"
"border-top-left-radius:10px;\n"
"border-top-right-radius:10px;\n"
"border-bottom-left-radius:10px;\n"
"border-bottom-right-radius:10px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:#ff0000;\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/x.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.close_btn.setIcon(icon3)

        self.horizontalLayout_7.addWidget(self.close_btn)


        self.horizontalLayout.addWidget(self.frame_20, 0, Qt.AlignTop)

        self.SETECLabel = QLabel(self.project_info)
        self.SETECLabel.setObjectName(u"SETECLabel")
        self.SETECLabel.setMaximumSize(QSize(300, 16777215))
        self.SETECLabel.setPixmap(QPixmap(u":/icons/icons/SETECLab_logo.svg"))
        self.SETECLabel.setScaledContents(True)
        self.SETECLabel.setMargin(0)

        self.horizontalLayout.addWidget(self.SETECLabel, 0, Qt.AlignHCenter)

        self.IPTC_label = QLabel(self.project_info)
        self.IPTC_label.setObjectName(u"IPTC_label")
        self.IPTC_label.setMaximumSize(QSize(250, 16777215))
        self.IPTC_label.setPixmap(QPixmap(u":/icons/icons/IPTC_logo.svg"))
        self.IPTC_label.setScaledContents(True)
        self.IPTC_label.setMargin(1)

        self.horizontalLayout.addWidget(self.IPTC_label, 0, Qt.AlignHCenter)

        self.ConnectControlFrame = QFrame(self.project_info)
        self.ConnectControlFrame.setObjectName(u"ConnectControlFrame")
        self.ConnectControlFrame.setFrameShape(QFrame.StyledPanel)
        self.ConnectControlFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.ConnectControlFrame)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.ssh_connect_btn = QPushButton(self.ConnectControlFrame)
        self.ssh_connect_btn.setObjectName(u"ssh_connect_btn")
        self.ssh_connect_btn.setStyleSheet(u"QPushButton:hover{\n"
"background-color:#99ffee;\n"
"}\n"
"QPushButton{\n"
"font:bold;\n"
"color:black;\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u":/icons/icons/zap-off.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.ssh_connect_btn.setIcon(icon4)
        self.ssh_connect_btn.setIconSize(QSize(30, 30))

        self.verticalLayout_7.addWidget(self.ssh_connect_btn)

        self.connectionStatus = QFrame(self.ConnectControlFrame)
        self.connectionStatus.setObjectName(u"connectionStatus")
        self.connectionStatus.setMaximumSize(QSize(16777215, 0))
        self.connectionStatus.setFrameShape(QFrame.StyledPanel)
        self.connectionStatus.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.connectionStatus)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.connectLabel = QLabel(self.connectionStatus)
        self.connectLabel.setObjectName(u"connectLabel")

        self.horizontalLayout_5.addWidget(self.connectLabel)


        self.verticalLayout_7.addWidget(self.connectionStatus, 0, Qt.AlignHCenter)


        self.horizontalLayout.addWidget(self.ConnectControlFrame)

        self.label_working_path = QLabel(self.project_info)
        self.label_working_path.setObjectName(u"label_working_path")

        self.horizontalLayout.addWidget(self.label_working_path)


        self.verticalLayout_2.addWidget(self.project_info)

        self.body_window = QFrame(self.mainwindow)
        self.body_window.setObjectName(u"body_window")
        self.body_window.setMaximumSize(QSize(16777215, 600))
        palette = QPalette()
        self.body_window.setPalette(palette)
        self.body_window.setFrameShape(QFrame.StyledPanel)
        self.body_window.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.body_window)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.func_select = QFrame(self.body_window)
        self.func_select.setObjectName(u"func_select")
        self.func_select.setMaximumSize(QSize(16777215, 50))
        self.func_select.setStyleSheet(u"border-bottom:3px solid rgb(0,0,0);")
        self.func_select.setFrameShape(QFrame.StyledPanel)
        self.func_select.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.func_select)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.devBtnTest = QPushButton(self.func_select)
        self.devBtnTest.setObjectName(u"devBtnTest")
        self.devBtnTest.setStyleSheet(u"*{border:none;}\n"
"QPushButton:hover{\n"
"background-color:#99ffee;\n"
"}")
        icon5 = QIcon()
        icon5.addFile(u":/icons/icons/battery-charging.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.devBtnTest.setIcon(icon5)
        self.devBtnTest.setIconSize(QSize(20, 20))

        self.gridLayout_5.addWidget(self.devBtnTest, 0, 1, 1, 1)

        self.confWorkspaceBtn = QPushButton(self.func_select)
        self.confWorkspaceBtn.setObjectName(u"confWorkspaceBtn")
        self.confWorkspaceBtn.setStyleSheet(u"*{border:none;}\n"
"QPushButton:hover{\n"
"background-color:#99ffee;\n"
"}")
        icon6 = QIcon()
        icon6.addFile(u":/icons/icons/settings.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.confWorkspaceBtn.setIcon(icon6)
        self.confWorkspaceBtn.setIconSize(QSize(20, 20))

        self.gridLayout_5.addWidget(self.confWorkspaceBtn, 0, 0, 1, 1)

        self.helpBtn = QPushButton(self.func_select)
        self.helpBtn.setObjectName(u"helpBtn")
        self.helpBtn.setMaximumSize(QSize(16777215, 16777215))
        self.helpBtn.setStyleSheet(u"*{border:none;}\n"
"QPushButton:hover{\n"
"background-color:#99ffee;\n"
"}")
        icon7 = QIcon()
        icon7.addFile(u":/icons/icons/help-circle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.helpBtn.setIcon(icon7)
        self.helpBtn.setIconSize(QSize(20, 20))

        self.gridLayout_5.addWidget(self.helpBtn, 0, 3, 1, 1)

        self.dataResultBtn = QPushButton(self.func_select)
        self.dataResultBtn.setObjectName(u"dataResultBtn")
        self.dataResultBtn.setMaximumSize(QSize(16777215, 50))
        self.dataResultBtn.setStyleSheet(u"*{border:none;}\n"
"QPushButton:hover{\n"
"background-color:#99ffee;\n"
"}")
        icon8 = QIcon()
        icon8.addFile(u":/icons/icons/bar-chart-2.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.dataResultBtn.setIcon(icon8)
        self.dataResultBtn.setIconSize(QSize(20, 20))

        self.gridLayout_5.addWidget(self.dataResultBtn, 0, 2, 1, 1)


        self.verticalLayout.addWidget(self.func_select)

        self.slide_devtstmenu = QFrame(self.body_window)
        self.slide_devtstmenu.setObjectName(u"slide_devtstmenu")
        self.slide_devtstmenu.setMaximumSize(QSize(16777215, 0))
        self.slide_devtstmenu.setFrameShape(QFrame.StyledPanel)
        self.slide_devtstmenu.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.slide_devtstmenu)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.slideBtnFrame = QFrame(self.slide_devtstmenu)
        self.slideBtnFrame.setObjectName(u"slideBtnFrame")
        self.slideBtnFrame.setEnabled(True)
        self.slideBtnFrame.setMaximumSize(QSize(35, 35))
        self.slideBtnFrame.setAutoFillBackground(False)
        self.slideBtnFrame.setFrameShape(QFrame.StyledPanel)
        self.slideBtnFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.slideBtnFrame)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.side_btn_tests = QPushButton(self.slideBtnFrame)
        self.side_btn_tests.setObjectName(u"side_btn_tests")
        self.side_btn_tests.setMaximumSize(QSize(30, 30))
        icon9 = QIcon()
        icon9.addFile(u":/icons/icons/chevron-left.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.side_btn_tests.setIcon(icon9)
        self.side_btn_tests.setIconSize(QSize(25, 25))

        self.horizontalLayout_8.addWidget(self.side_btn_tests, 0, Qt.AlignTop)


        self.horizontalLayout_6.addWidget(self.slideBtnFrame)

        self.testsopt_slide = QFrame(self.slide_devtstmenu)
        self.testsopt_slide.setObjectName(u"testsopt_slide")
        self.testsopt_slide.setFrameShape(QFrame.StyledPanel)
        self.testsopt_slide.setFrameShadow(QFrame.Raised)
        self.gridLayout_7 = QGridLayout(self.testsopt_slide)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.opt_menu = QFrame(self.testsopt_slide)
        self.opt_menu.setObjectName(u"opt_menu")
        self.opt_menu.setMaximumSize(QSize(600, 16777215))
        self.opt_menu.setFrameShape(QFrame.StyledPanel)
        self.opt_menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.opt_menu)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.tests_recent_btn = QPushButton(self.opt_menu)
        self.tests_recent_btn.setObjectName(u"tests_recent_btn")

        self.verticalLayout_4.addWidget(self.tests_recent_btn)

        self.newSeqBtn = QPushButton(self.opt_menu)
        self.newSeqBtn.setObjectName(u"newSeqBtn")

        self.verticalLayout_4.addWidget(self.newSeqBtn)

        self.newSeq_slidemenu = QFrame(self.opt_menu)
        self.newSeq_slidemenu.setObjectName(u"newSeq_slidemenu")
        self.newSeq_slidemenu.setMaximumSize(QSize(150, 0))
        self.newSeq_slidemenu.setFrameShape(QFrame.StyledPanel)
        self.newSeq_slidemenu.setFrameShadow(QFrame.Raised)
        self.gridLayout_6 = QGridLayout(self.newSeq_slidemenu)
        self.gridLayout_6.setSpacing(0)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.uploadFile = QPushButton(self.newSeq_slidemenu)
        self.uploadFile.setObjectName(u"uploadFile")
        self.uploadFile.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_6.addWidget(self.uploadFile, 0, 0, 1, 1)

        self.template_2 = QPushButton(self.newSeq_slidemenu)
        self.template_2.setObjectName(u"template_2")
        self.template_2.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_6.addWidget(self.template_2, 1, 0, 1, 1)


        self.verticalLayout_4.addWidget(self.newSeq_slidemenu, 0, Qt.AlignHCenter)


        self.gridLayout_7.addWidget(self.opt_menu, 0, 0, 1, 1)


        self.horizontalLayout_6.addWidget(self.testsopt_slide)

        self.frame_2 = QFrame(self.slide_devtstmenu)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_2)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.TestNameFrame = QFrame(self.frame_2)
        self.TestNameFrame.setObjectName(u"TestNameFrame")
        self.TestNameFrame.setMaximumSize(QSize(16777215, 0))
        self.TestNameFrame.setFrameShape(QFrame.StyledPanel)
        self.TestNameFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.TestNameFrame)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.filenameLabel = QLabel(self.TestNameFrame)
        self.filenameLabel.setObjectName(u"filenameLabel")

        self.horizontalLayout_9.addWidget(self.filenameLabel, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.editNameBtn = QPushButton(self.TestNameFrame)
        self.editNameBtn.setObjectName(u"editNameBtn")

        self.horizontalLayout_9.addWidget(self.editNameBtn, 0, Qt.AlignHCenter)


        self.verticalLayout_8.addWidget(self.TestNameFrame)

        self.treeWidget = QTreeWidget(self.frame_2)
        self.treeWidget.headerItem().setText(0, "")
        self.treeWidget.setObjectName(u"treeWidget")
        self.treeWidget.setMaximumSize(QSize(0, 16777215))

        self.verticalLayout_8.addWidget(self.treeWidget)

        self.TestActionsFrame = QFrame(self.frame_2)
        self.TestActionsFrame.setObjectName(u"TestActionsFrame")
        self.TestActionsFrame.setMaximumSize(QSize(500, 0))
        self.TestActionsFrame.setFrameShape(QFrame.StyledPanel)
        self.TestActionsFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.TestActionsFrame)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.ExcTestBtn = QPushButton(self.TestActionsFrame)
        self.ExcTestBtn.setObjectName(u"ExcTestBtn")

        self.horizontalLayout_3.addWidget(self.ExcTestBtn)

        self.add2QueueBtn = QPushButton(self.TestActionsFrame)
        self.add2QueueBtn.setObjectName(u"add2QueueBtn")
        self.add2QueueBtn.setStyleSheet(u"")
        self.add2QueueBtn.setAutoDefault(False)

        self.horizontalLayout_3.addWidget(self.add2QueueBtn)


        self.verticalLayout_8.addWidget(self.TestActionsFrame)


        self.horizontalLayout_6.addWidget(self.frame_2)


        self.verticalLayout.addWidget(self.slide_devtstmenu)

        self.dataResults_menu = QFrame(self.body_window)
        self.dataResults_menu.setObjectName(u"dataResults_menu")
        self.dataResults_menu.setMaximumSize(QSize(16777215, 800))
        self.dataResults_menu.setFrameShape(QFrame.StyledPanel)
        self.dataResults_menu.setFrameShadow(QFrame.Raised)
        self.gridLayout_9 = QGridLayout(self.dataResults_menu)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.frame_17 = QFrame(self.dataResults_menu)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setMinimumSize(QSize(0, 0))
        self.frame_17.setMaximumSize(QSize(35, 35))
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.frame_17)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.sideResultsBtn = QPushButton(self.frame_17)
        self.sideResultsBtn.setObjectName(u"sideResultsBtn")
        self.sideResultsBtn.setIcon(icon9)
        self.sideResultsBtn.setIconSize(QSize(25, 25))

        self.verticalLayout_15.addWidget(self.sideResultsBtn)


        self.gridLayout_9.addWidget(self.frame_17, 0, 0, 1, 1)

        self.dataresult_sidemenu = QFrame(self.dataResults_menu)
        self.dataresult_sidemenu.setObjectName(u"dataresult_sidemenu")
        self.dataresult_sidemenu.setMaximumSize(QSize(400, 300))
        self.dataresult_sidemenu.setFrameShape(QFrame.StyledPanel)
        self.dataresult_sidemenu.setFrameShadow(QFrame.Raised)
        self.formLayout = QFormLayout(self.dataresult_sidemenu)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setHorizontalSpacing(0)
        self.formLayout.setVerticalSpacing(0)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.interacGraphBtn = QPushButton(self.dataresult_sidemenu)
        self.interacGraphBtn.setObjectName(u"interacGraphBtn")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.interacGraphBtn)

        self.resultCompBtn = QPushButton(self.dataresult_sidemenu)
        self.resultCompBtn.setObjectName(u"resultCompBtn")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.resultCompBtn)

        self.customReportBtn = QPushButton(self.dataresult_sidemenu)
        self.customReportBtn.setObjectName(u"customReportBtn")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.customReportBtn)


        self.gridLayout_9.addWidget(self.dataresult_sidemenu, 0, 1, 1, 1, Qt.AlignHCenter)

        self.stackedDataResults = QStackedWidget(self.dataResults_menu)
        self.stackedDataResults.setObjectName(u"stackedDataResults")
        self.homeDataResOpt = QWidget()
        self.homeDataResOpt.setObjectName(u"homeDataResOpt")
        self.label = QLabel(self.homeDataResOpt)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(140, 160, 67, 17))
        self.stackedDataResults.addWidget(self.homeDataResOpt)
        self.interactiveGrphOpt = QWidget()
        self.interactiveGrphOpt.setObjectName(u"interactiveGrphOpt")
        self.gridLayout_4 = QGridLayout(self.interactiveGrphOpt)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.stackedWidgetResGraphs = QStackedWidget(self.interactiveGrphOpt)
        self.stackedWidgetResGraphs.setObjectName(u"stackedWidgetResGraphs")
        self.BTMres = QWidget()
        self.BTMres.setObjectName(u"BTMres")
        self.horizontalLayout_10 = QHBoxLayout(self.BTMres)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.Graph1 = QFrame(self.BTMres)
        self.Graph1.setObjectName(u"Graph1")
        self.Graph1.setFrameShape(QFrame.StyledPanel)
        self.Graph1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.Graph1)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_5 = QLabel(self.Graph1)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout_9.addWidget(self.label_5)

        self.VlayGraph1 = QVBoxLayout()
        self.VlayGraph1.setObjectName(u"VlayGraph1")

        self.verticalLayout_9.addLayout(self.VlayGraph1)

        self.verticalLayout_9.setStretch(0, 1)
        self.verticalLayout_9.setStretch(1, 5)

        self.horizontalLayout_10.addWidget(self.Graph1)

        self.stackedWidgetResGraphs.addWidget(self.BTMres)
        self.SAMres = QWidget()
        self.SAMres.setObjectName(u"SAMres")
        self.horizontalLayout_11 = QHBoxLayout(self.SAMres)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.Graph2 = QFrame(self.SAMres)
        self.Graph2.setObjectName(u"Graph2")
        self.Graph2.setFrameShape(QFrame.StyledPanel)
        self.Graph2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.Graph2)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_3 = QLabel(self.Graph2)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_10.addWidget(self.label_3)

        self.VlayGraph2 = QVBoxLayout()
        self.VlayGraph2.setObjectName(u"VlayGraph2")

        self.verticalLayout_10.addLayout(self.VlayGraph2)

        self.verticalLayout_10.setStretch(0, 1)
        self.verticalLayout_10.setStretch(1, 5)

        self.horizontalLayout_11.addWidget(self.Graph2)

        self.stackedWidgetResGraphs.addWidget(self.SAMres)
        self.VELMres = QWidget()
        self.VELMres.setObjectName(u"VELMres")
        self.horizontalLayout_12 = QHBoxLayout(self.VELMres)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.Graph3 = QFrame(self.VELMres)
        self.Graph3.setObjectName(u"Graph3")
        self.Graph3.setFrameShape(QFrame.StyledPanel)
        self.Graph3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.Graph3)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.label_4 = QLabel(self.Graph3)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_11.addWidget(self.label_4)

        self.VlayGraph3 = QVBoxLayout()
        self.VlayGraph3.setObjectName(u"VlayGraph3")

        self.verticalLayout_11.addLayout(self.VlayGraph3)

        self.verticalLayout_11.setStretch(0, 1)
        self.verticalLayout_11.setStretch(1, 5)

        self.horizontalLayout_12.addWidget(self.Graph3)

        self.stackedWidgetResGraphs.addWidget(self.VELMres)

        self.gridLayout_4.addWidget(self.stackedWidgetResGraphs, 0, 0, 1, 1)

        self.frame_3 = QFrame(self.interactiveGrphOpt)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.BTMresBtn = QPushButton(self.frame_3)
        self.BTMresBtn.setObjectName(u"BTMresBtn")

        self.horizontalLayout_13.addWidget(self.BTMresBtn)

        self.SAMresBtn = QPushButton(self.frame_3)
        self.SAMresBtn.setObjectName(u"SAMresBtn")

        self.horizontalLayout_13.addWidget(self.SAMresBtn)

        self.VELMresBtn = QPushButton(self.frame_3)
        self.VELMresBtn.setObjectName(u"VELMresBtn")

        self.horizontalLayout_13.addWidget(self.VELMresBtn)


        self.gridLayout_4.addWidget(self.frame_3, 1, 0, 1, 1)

        self.stackedDataResults.addWidget(self.interactiveGrphOpt)
        self.resCompOpt = QWidget()
        self.resCompOpt.setObjectName(u"resCompOpt")
        self.label_8 = QLabel(self.resCompOpt)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(110, 160, 131, 17))
        self.stackedDataResults.addWidget(self.resCompOpt)
        self.customRepOpt = QWidget()
        self.customRepOpt.setObjectName(u"customRepOpt")
        self.label_9 = QLabel(self.customRepOpt)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(110, 160, 131, 17))
        self.stackedDataResults.addWidget(self.customRepOpt)

        self.gridLayout_9.addWidget(self.stackedDataResults, 0, 3, 1, 1)


        self.verticalLayout.addWidget(self.dataResults_menu)

        self.home_frame = QFrame(self.body_window)
        self.home_frame.setObjectName(u"home_frame")
        self.home_frame.setMaximumSize(QSize(16777215, 0))
        self.home_frame.setFrameShape(QFrame.StyledPanel)
        self.home_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.home_frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_2 = QLabel(self.home_frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(400, 400))
        self.label_2.setPixmap(QPixmap(u":/icons/icons/satellite.svg"))
        self.label_2.setScaledContents(True)

        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)


        self.verticalLayout.addWidget(self.home_frame)

        self.confWokspace_menu = QFrame(self.body_window)
        self.confWokspace_menu.setObjectName(u"confWokspace_menu")
        self.confWokspace_menu.setMaximumSize(QSize(16777215, 0))
        self.confWokspace_menu.setFrameShape(QFrame.StyledPanel)
        self.confWokspace_menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.confWokspace_menu)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.workConfMenu = QFrame(self.confWokspace_menu)
        self.workConfMenu.setObjectName(u"workConfMenu")
        self.workConfMenu.setMaximumSize(QSize(16777215, 800))
        self.workConfMenu.setFrameShape(QFrame.StyledPanel)
        self.workConfMenu.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.workConfMenu)
        self.gridLayout_2.setSpacing(6)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(9, 9, 9, 9)
        self.stackedWidgetWorkspace = QStackedWidget(self.workConfMenu)
        self.stackedWidgetWorkspace.setObjectName(u"stackedWidgetWorkspace")
        self.home = QWidget()
        self.home.setObjectName(u"home")
        self.stackedWidgetWorkspace.addWidget(self.home)
        self.saveWorksMenu = QWidget()
        self.saveWorksMenu.setObjectName(u"saveWorksMenu")
        self.verticalLayout_6 = QVBoxLayout(self.saveWorksMenu)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.manageNotifBtn = QPushButton(self.saveWorksMenu)
        self.manageNotifBtn.setObjectName(u"manageNotifBtn")

        self.verticalLayout_6.addWidget(self.manageNotifBtn)

        self.logEventsBtn = QPushButton(self.saveWorksMenu)
        self.logEventsBtn.setObjectName(u"logEventsBtn")

        self.verticalLayout_6.addWidget(self.logEventsBtn)

        self.preloadTestsBtn = QPushButton(self.saveWorksMenu)
        self.preloadTestsBtn.setObjectName(u"preloadTestsBtn")

        self.verticalLayout_6.addWidget(self.preloadTestsBtn)

        self.exportSettingsBtn = QPushButton(self.saveWorksMenu)
        self.exportSettingsBtn.setObjectName(u"exportSettingsBtn")

        self.verticalLayout_6.addWidget(self.exportSettingsBtn)

        self.viewSavedBtn = QPushButton(self.saveWorksMenu)
        self.viewSavedBtn.setObjectName(u"viewSavedBtn")

        self.verticalLayout_6.addWidget(self.viewSavedBtn)

        self.stackedWidgetWorkspace.addWidget(self.saveWorksMenu)
        self.newWorkMenu = QWidget()
        self.newWorkMenu.setObjectName(u"newWorkMenu")
        self.gridLayout_10 = QGridLayout(self.newWorkMenu)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.gridLayout_10.setContentsMargins(0, 0, 0, 0)
        self.frameNew = QFrame(self.newWorkMenu)
        self.frameNew.setObjectName(u"frameNew")
        self.frameNew.setMaximumSize(QSize(16777215, 500))
        self.frameNew.setFrameShape(QFrame.StyledPanel)
        self.frameNew.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frameNew)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.line_org = QLineEdit(self.frameNew)
        self.line_org.setObjectName(u"line_org")

        self.gridLayout_3.addWidget(self.line_org, 1, 1, 1, 1)

        self.label_6 = QLabel(self.frameNew)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_3.addWidget(self.label_6, 2, 0, 1, 1)

        self.frame = QFrame(self.frameNew)
        self.frame.setObjectName(u"frame")
        self.frame.setMaximumSize(QSize(16777215, 40))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.addMembersBtn = QPushButton(self.frame)
        self.addMembersBtn.setObjectName(u"addMembersBtn")
        self.addMembersBtn.setMaximumSize(QSize(200, 16777215))

        self.horizontalLayout_2.addWidget(self.addMembersBtn)

        self.moduleConfBtn = QPushButton(self.frame)
        self.moduleConfBtn.setObjectName(u"moduleConfBtn")

        self.horizontalLayout_2.addWidget(self.moduleConfBtn)

        self.saveWorkspaceBtn = QPushButton(self.frame)
        self.saveWorkspaceBtn.setObjectName(u"saveWorkspaceBtn")
        self.saveWorkspaceBtn.setMaximumSize(QSize(200, 16777215))

        self.horizontalLayout_2.addWidget(self.saveWorkspaceBtn)


        self.gridLayout_3.addWidget(self.frame, 3, 0, 1, 2)

        self.line_name = QLineEdit(self.frameNew)
        self.line_name.setObjectName(u"line_name")

        self.gridLayout_3.addWidget(self.line_name, 0, 1, 1, 1)

        self.LabelOrg = QLabel(self.frameNew)
        self.LabelOrg.setObjectName(u"LabelOrg")

        self.gridLayout_3.addWidget(self.LabelOrg, 1, 0, 1, 1)

        self.LabelName = QLabel(self.frameNew)
        self.LabelName.setObjectName(u"LabelName")

        self.gridLayout_3.addWidget(self.LabelName, 0, 0, 1, 1)

        self.line_team = QLineEdit(self.frameNew)
        self.line_team.setObjectName(u"line_team")

        self.gridLayout_3.addWidget(self.line_team, 2, 1, 1, 1)

        self.addMembersLine = QFrame(self.frameNew)
        self.addMembersLine.setObjectName(u"addMembersLine")
        self.addMembersLine.setMinimumSize(QSize(0, 50))
        self.addMembersLine.setMaximumSize(QSize(16777215, 0))
        self.addMembersLine.setFrameShape(QFrame.StyledPanel)
        self.addMembersLine.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.addMembersLine)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_10 = QLabel(self.addMembersLine)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout_4.addWidget(self.label_10)

        self.line_newMember = QLineEdit(self.addMembersLine)
        self.line_newMember.setObjectName(u"line_newMember")

        self.horizontalLayout_4.addWidget(self.line_newMember)

        self.addBtn = QPushButton(self.addMembersLine)
        self.addBtn.setObjectName(u"addBtn")

        self.horizontalLayout_4.addWidget(self.addBtn)


        self.gridLayout_3.addWidget(self.addMembersLine, 4, 0, 1, 2)


        self.gridLayout_10.addWidget(self.frameNew, 0, 0, 1, 1)

        self.stackedWidgetWorkspace.addWidget(self.newWorkMenu)

        self.gridLayout_2.addWidget(self.stackedWidgetWorkspace, 1, 1, 1, 1)

        self.workOptions = QFrame(self.workConfMenu)
        self.workOptions.setObjectName(u"workOptions")
        self.workOptions.setFrameShape(QFrame.StyledPanel)
        self.workOptions.setFrameShadow(QFrame.Raised)
        self.gridLayout_8 = QGridLayout(self.workOptions)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.selectWorkspaceBtn = QPushButton(self.workOptions)
        self.selectWorkspaceBtn.setObjectName(u"selectWorkspaceBtn")

        self.gridLayout_8.addWidget(self.selectWorkspaceBtn, 0, 0, 1, 1)

        self.newWorkspaceBtn = QPushButton(self.workOptions)
        self.newWorkspaceBtn.setObjectName(u"newWorkspaceBtn")

        self.gridLayout_8.addWidget(self.newWorkspaceBtn, 0, 1, 1, 1)

        self.workOptBtn = QPushButton(self.workOptions)
        self.workOptBtn.setObjectName(u"workOptBtn")

        self.gridLayout_8.addWidget(self.workOptBtn, 0, 2, 1, 1)


        self.gridLayout_2.addWidget(self.workOptions, 0, 1, 1, 2)


        self.verticalLayout_3.addWidget(self.workConfMenu)


        self.verticalLayout.addWidget(self.confWokspace_menu)

        self.help_menu = QFrame(self.body_window)
        self.help_menu.setObjectName(u"help_menu")
        self.help_menu.setMaximumSize(QSize(16777215, 0))
        self.help_menu.setFrameShape(QFrame.StyledPanel)
        self.help_menu.setFrameShadow(QFrame.Raised)
        self.hel_label_on_menu = QLabel(self.help_menu)
        self.hel_label_on_menu.setObjectName(u"hel_label_on_menu")
        self.hel_label_on_menu.setGeometry(QRect(20, 20, 288, 17))

        self.verticalLayout.addWidget(self.help_menu)


        self.verticalLayout_2.addWidget(self.body_window)


        self.verticalLayout_5.addWidget(self.mainwindow)

        self.size_grip = QFrame(self.centralwidget)
        self.size_grip.setObjectName(u"size_grip")
        self.size_grip.setMinimumSize(QSize(10, 10))
        self.size_grip.setMaximumSize(QSize(10, 10))
        self.size_grip.setFrameShape(QFrame.StyledPanel)
        self.size_grip.setFrameShadow(QFrame.Raised)

        self.verticalLayout_5.addWidget(self.size_grip, 0, Qt.AlignRight)

        IPTC.setCentralWidget(self.centralwidget)
        self.size_grip.raise_()
        self.mainwindow.raise_()

        self.retranslateUi(IPTC)

        self.add2QueueBtn.setDefault(False)
        self.stackedDataResults.setCurrentIndex(1)
        self.stackedWidgetResGraphs.setCurrentIndex(0)
        self.stackedWidgetWorkspace.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(IPTC)
    # setupUi

    def retranslateUi(self, IPTC):
        IPTC.setWindowTitle(QCoreApplication.translate("IPTC", u"IPTC", None))
        self.minimize_btn.setText("")
        self.maximize_btn.setText("")
        self.close_btn.setText("")
        self.SETECLabel.setText("")
        self.IPTC_label.setText("")
        self.ssh_connect_btn.setText(QCoreApplication.translate("IPTC", u"SSH", None))
        self.connectLabel.setText("")
        self.label_working_path.setText("")
        self.devBtnTest.setText(QCoreApplication.translate("IPTC", u"Develop and run tests", None))
        self.confWorkspaceBtn.setText(QCoreApplication.translate("IPTC", u"Configure Workspace", None))
        self.helpBtn.setText(QCoreApplication.translate("IPTC", u"Help", None))
        self.dataResultBtn.setText(QCoreApplication.translate("IPTC", u"Data results", None))
        self.side_btn_tests.setText("")
        self.tests_recent_btn.setText(QCoreApplication.translate("IPTC", u"Recents", None))
        self.newSeqBtn.setText(QCoreApplication.translate("IPTC", u"New sequence", None))
        self.uploadFile.setText(QCoreApplication.translate("IPTC", u"Upload file", None))
        self.template_2.setText(QCoreApplication.translate("IPTC", u"Template", None))
        self.filenameLabel.setText("")
        self.editNameBtn.setText(QCoreApplication.translate("IPTC", u"Change file name", None))
        self.ExcTestBtn.setText(QCoreApplication.translate("IPTC", u"Excute test", None))
        self.add2QueueBtn.setText(QCoreApplication.translate("IPTC", u"Add test to queue", None))
        self.sideResultsBtn.setText("")
        self.interacGraphBtn.setText(QCoreApplication.translate("IPTC", u"Interactive graphics", None))
        self.resultCompBtn.setText(QCoreApplication.translate("IPTC", u"Results Comparison ", None))
        self.customReportBtn.setText(QCoreApplication.translate("IPTC", u"Customize reports", None))
        self.label.setText(QCoreApplication.translate("IPTC", u"Home", None))
        self.label_5.setText(QCoreApplication.translate("IPTC", u"Graph1", None))
        self.label_3.setText(QCoreApplication.translate("IPTC", u"Graph2", None))
        self.label_4.setText(QCoreApplication.translate("IPTC", u"Graph3", None))
        self.BTMresBtn.setText(QCoreApplication.translate("IPTC", u"BTM results", None))
        self.SAMresBtn.setText(QCoreApplication.translate("IPTC", u"SAM results", None))
        self.VELMresBtn.setText(QCoreApplication.translate("IPTC", u"VELM results", None))
        self.label_8.setText(QCoreApplication.translate("IPTC", u"Results comparison", None))
        self.label_9.setText(QCoreApplication.translate("IPTC", u"Customize reports", None))
        self.label_2.setText("")
        self.manageNotifBtn.setText(QCoreApplication.translate("IPTC", u"Manage Notifications", None))
        self.logEventsBtn.setText(QCoreApplication.translate("IPTC", u"Log events", None))
        self.preloadTestsBtn.setText(QCoreApplication.translate("IPTC", u"Pre-load tests", None))
        self.exportSettingsBtn.setText(QCoreApplication.translate("IPTC", u"Export settings", None))
        self.viewSavedBtn.setText(QCoreApplication.translate("IPTC", u"View saved tests", None))
        self.label_6.setText(QCoreApplication.translate("IPTC", u"Team", None))
        self.addMembersBtn.setText(QCoreApplication.translate("IPTC", u"Add members", None))
        self.moduleConfBtn.setText(QCoreApplication.translate("IPTC", u"Modules settings", None))
        self.saveWorkspaceBtn.setText(QCoreApplication.translate("IPTC", u"Save workspace", None))
        self.LabelOrg.setText(QCoreApplication.translate("IPTC", u"Org", None))
        self.LabelName.setText(QCoreApplication.translate("IPTC", u"Name", None))
        self.label_10.setText(QCoreApplication.translate("IPTC", u"Name", None))
        self.addBtn.setText(QCoreApplication.translate("IPTC", u"Add", None))
        self.selectWorkspaceBtn.setText(QCoreApplication.translate("IPTC", u"Choose a saved Workspace", None))
        self.newWorkspaceBtn.setText(QCoreApplication.translate("IPTC", u"Create a new workspace", None))
        self.workOptBtn.setText(QCoreApplication.translate("IPTC", u"Workspace  options", None))
        self.hel_label_on_menu.setText(QCoreApplication.translate("IPTC", u"IPTC GUI is an application for writing tests.", None))
    # retranslateUi

