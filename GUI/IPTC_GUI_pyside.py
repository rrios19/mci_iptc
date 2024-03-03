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

class Ui_IPTC(object):
    def setupUi(self, IPTC):
        if not IPTC.objectName():
            IPTC.setObjectName(u"IPTC")
        IPTC.resize(689, 551)
        icon = QIcon()
        icon.addFile(u":/icons/icons/IPTC_logo.svg", QSize(), QIcon.Normal, QIcon.Off)
        IPTC.setWindowIcon(icon)
        IPTC.setStyleSheet(u"*{\n"
"	border: none;\n"
"}")
        self.centralwidget = QWidget(IPTC)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.mainwindow = QFrame(self.centralwidget)
        self.mainwindow.setObjectName(u"mainwindow")
        self.mainwindow.setMaximumSize(QSize(16777215, 16777215))
        self.mainwindow.setFrameShape(QFrame.StyledPanel)
        self.mainwindow.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.mainwindow)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.project_info = QFrame(self.mainwindow)
        self.project_info.setObjectName(u"project_info")
        self.project_info.setMaximumSize(QSize(16777215, 50))
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
        self.minimize_btn.setMaximumSize(QSize(20, 20))
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/minus.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.minimize_btn.setIcon(icon1)

        self.horizontalLayout_7.addWidget(self.minimize_btn)

        self.maximize_btn = QPushButton(self.frame_20)
        self.maximize_btn.setObjectName(u"maximize_btn")
        self.maximize_btn.setEnabled(True)
        self.maximize_btn.setMaximumSize(QSize(20, 20))
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/maximize-2.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.maximize_btn.setIcon(icon2)

        self.horizontalLayout_7.addWidget(self.maximize_btn)

        self.close_btn = QPushButton(self.frame_20)
        self.close_btn.setObjectName(u"close_btn")
        self.close_btn.setMaximumSize(QSize(20, 20))
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

        self.label_2 = QLabel(self.project_info)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(250, 16777215))
        self.label_2.setPixmap(QPixmap(u":/icons/icons/IPTC_logo.svg"))
        self.label_2.setScaledContents(True)
        self.label_2.setMargin(1)

        self.horizontalLayout.addWidget(self.label_2, 0, Qt.AlignHCenter)

        self.size_grip = QFrame(self.project_info)
        self.size_grip.setObjectName(u"size_grip")
        self.size_grip.setFrameShape(QFrame.StyledPanel)
        self.size_grip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout.addWidget(self.size_grip)


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
        self.confWorkspaceBtn = QPushButton(self.func_select)
        self.confWorkspaceBtn.setObjectName(u"confWorkspaceBtn")
        self.confWorkspaceBtn.setStyleSheet(u"*{border:none;}")
        icon4 = QIcon()
        icon4.addFile(u":/icons/icons/settings.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.confWorkspaceBtn.setIcon(icon4)
        self.confWorkspaceBtn.setIconSize(QSize(20, 20))

        self.gridLayout_5.addWidget(self.confWorkspaceBtn, 0, 0, 1, 1)

        self.devBtnTest = QPushButton(self.func_select)
        self.devBtnTest.setObjectName(u"devBtnTest")
        self.devBtnTest.setStyleSheet(u"*{border:none;}")
        icon5 = QIcon()
        icon5.addFile(u":/icons/icons/battery-charging.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.devBtnTest.setIcon(icon5)
        self.devBtnTest.setIconSize(QSize(20, 20))

        self.gridLayout_5.addWidget(self.devBtnTest, 0, 1, 1, 1)

        self.dataResultBtn = QPushButton(self.func_select)
        self.dataResultBtn.setObjectName(u"dataResultBtn")
        self.dataResultBtn.setMaximumSize(QSize(150, 50))
        self.dataResultBtn.setStyleSheet(u"*{border:none;}")
        icon6 = QIcon()
        icon6.addFile(u":/icons/icons/bar-chart-2.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.dataResultBtn.setIcon(icon6)
        self.dataResultBtn.setIconSize(QSize(20, 20))

        self.gridLayout_5.addWidget(self.dataResultBtn, 0, 2, 1, 1)

        self.helpBtn = QPushButton(self.func_select)
        self.helpBtn.setObjectName(u"helpBtn")
        self.helpBtn.setMaximumSize(QSize(100, 16777215))
        self.helpBtn.setStyleSheet(u"*{border:none;}")
        icon7 = QIcon()
        icon7.addFile(u":/icons/icons/help-circle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.helpBtn.setIcon(icon7)
        self.helpBtn.setIconSize(QSize(20, 20))

        self.gridLayout_5.addWidget(self.helpBtn, 0, 3, 1, 1)


        self.verticalLayout.addWidget(self.func_select)

        self.slide_devtstmenu = QFrame(self.body_window)
        self.slide_devtstmenu.setObjectName(u"slide_devtstmenu")
        self.slide_devtstmenu.setMaximumSize(QSize(16777215, 0))
        self.slide_devtstmenu.setFrameShape(QFrame.StyledPanel)
        self.slide_devtstmenu.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.slide_devtstmenu)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
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
        icon8 = QIcon()
        icon8.addFile(u":/icons/icons/chevron-left.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.side_btn_tests.setIcon(icon8)
        self.side_btn_tests.setIconSize(QSize(25, 25))

        self.horizontalLayout_8.addWidget(self.side_btn_tests, 0, Qt.AlignTop)


        self.gridLayout_4.addWidget(self.slideBtnFrame, 1, 0, 1, 1)

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


        self.gridLayout_7.addWidget(self.opt_menu, 0, 0, 1, 1)

        self.newSeq_slidemenu = QFrame(self.testsopt_slide)
        self.newSeq_slidemenu.setObjectName(u"newSeq_slidemenu")
        self.newSeq_slidemenu.setMaximumSize(QSize(0, 16777215))
        self.newSeq_slidemenu.setFrameShape(QFrame.StyledPanel)
        self.newSeq_slidemenu.setFrameShadow(QFrame.Raised)
        self.gridLayout_6 = QGridLayout(self.newSeq_slidemenu)
        self.gridLayout_6.setSpacing(0)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.uploadFile = QPushButton(self.newSeq_slidemenu)
        self.uploadFile.setObjectName(u"uploadFile")

        self.gridLayout_6.addWidget(self.uploadFile, 0, 0, 1, 1)

        self.template_2 = QPushButton(self.newSeq_slidemenu)
        self.template_2.setObjectName(u"template_2")

        self.gridLayout_6.addWidget(self.template_2, 1, 0, 1, 1)


        self.gridLayout_7.addWidget(self.newSeq_slidemenu, 0, 1, 1, 1)


        self.gridLayout_4.addWidget(self.testsopt_slide, 1, 1, 1, 1)


        self.verticalLayout.addWidget(self.slide_devtstmenu)

        self.dataResults_menu = QFrame(self.body_window)
        self.dataResults_menu.setObjectName(u"dataResults_menu")
        self.dataResults_menu.setMaximumSize(QSize(16777215, 0))
        self.dataResults_menu.setFrameShape(QFrame.StyledPanel)
        self.dataResults_menu.setFrameShadow(QFrame.Raised)
        self.formLayout_2 = QFormLayout(self.dataResults_menu)
        self.formLayout_2.setObjectName(u"formLayout_2")
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
        self.sideResultsBtn.setIcon(icon8)
        self.sideResultsBtn.setIconSize(QSize(25, 25))

        self.verticalLayout_15.addWidget(self.sideResultsBtn)


        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.frame_17)

        self.dataresult_sidemenu = QFrame(self.dataResults_menu)
        self.dataresult_sidemenu.setObjectName(u"dataresult_sidemenu")
        self.dataresult_sidemenu.setMaximumSize(QSize(600, 300))
        self.dataresult_sidemenu.setFrameShape(QFrame.StyledPanel)
        self.dataresult_sidemenu.setFrameShadow(QFrame.Raised)
        self.formLayout = QFormLayout(self.dataresult_sidemenu)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setHorizontalSpacing(0)
        self.formLayout.setVerticalSpacing(0)
        self.formLayout.setContentsMargins(0, 0, 350, 0)
        self.intAnalysisBtn = QPushButton(self.dataresult_sidemenu)
        self.intAnalysisBtn.setObjectName(u"intAnalysisBtn")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.intAnalysisBtn)

        self.filTagsGrBtn = QPushButton(self.dataresult_sidemenu)
        self.filTagsGrBtn.setObjectName(u"filTagsGrBtn")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.filTagsGrBtn)

        self.interacGraphBtn = QPushButton(self.dataresult_sidemenu)
        self.interacGraphBtn.setObjectName(u"interacGraphBtn")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.interacGraphBtn)

        self.patAnoDetBtn = QPushButton(self.dataresult_sidemenu)
        self.patAnoDetBtn.setObjectName(u"patAnoDetBtn")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.patAnoDetBtn)

        self.resultCompBtn = QPushButton(self.dataresult_sidemenu)
        self.resultCompBtn.setObjectName(u"resultCompBtn")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.resultCompBtn)

        self.customReportBtn = QPushButton(self.dataresult_sidemenu)
        self.customReportBtn.setObjectName(u"customReportBtn")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.customReportBtn)


        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.dataresult_sidemenu)


        self.verticalLayout.addWidget(self.dataResults_menu)

        self.confWokspace_menu = QFrame(self.body_window)
        self.confWokspace_menu.setObjectName(u"confWokspace_menu")
        self.confWokspace_menu.setMaximumSize(QSize(16777215, 0))
        self.confWokspace_menu.setFrameShape(QFrame.StyledPanel)
        self.confWokspace_menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.confWokspace_menu)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.workspaceActions = QFrame(self.confWokspace_menu)
        self.workspaceActions.setObjectName(u"workspaceActions")
        self.workspaceActions.setFrameShape(QFrame.StyledPanel)
        self.workspaceActions.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.workspaceActions)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.frame_10 = QFrame(self.workspaceActions)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_10)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.selectWorkspaceBtn = QPushButton(self.frame_10)
        self.selectWorkspaceBtn.setObjectName(u"selectWorkspaceBtn")

        self.verticalLayout_8.addWidget(self.selectWorkspaceBtn)

        self.newWorkspaceBtn = QPushButton(self.frame_10)
        self.newWorkspaceBtn.setObjectName(u"newWorkspaceBtn")

        self.verticalLayout_8.addWidget(self.newWorkspaceBtn)


        self.horizontalLayout_2.addWidget(self.frame_10)

        self.frame_11 = QFrame(self.workspaceActions)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_11)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.manageNotifBtn = QPushButton(self.frame_11)
        self.manageNotifBtn.setObjectName(u"manageNotifBtn")

        self.verticalLayout_10.addWidget(self.manageNotifBtn)

        self.logEventsBtn = QPushButton(self.frame_11)
        self.logEventsBtn.setObjectName(u"logEventsBtn")

        self.verticalLayout_10.addWidget(self.logEventsBtn)

        self.preloadTestsBtn = QPushButton(self.frame_11)
        self.preloadTestsBtn.setObjectName(u"preloadTestsBtn")

        self.verticalLayout_10.addWidget(self.preloadTestsBtn)

        self.exportSettingsBtn = QPushButton(self.frame_11)
        self.exportSettingsBtn.setObjectName(u"exportSettingsBtn")

        self.verticalLayout_10.addWidget(self.exportSettingsBtn)

        self.viewSavedBtn = QPushButton(self.frame_11)
        self.viewSavedBtn.setObjectName(u"viewSavedBtn")

        self.verticalLayout_10.addWidget(self.viewSavedBtn)


        self.horizontalLayout_2.addWidget(self.frame_11)


        self.verticalLayout_3.addWidget(self.workspaceActions)

        self.frame_9 = QFrame(self.confWokspace_menu)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_9)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.frame_14 = QFrame(self.frame_9)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_14)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.LabelName = QLabel(self.frame_14)
        self.LabelName.setObjectName(u"LabelName")

        self.gridLayout_3.addWidget(self.LabelName, 0, 0, 1, 1)

        self.line_name = QLineEdit(self.frame_14)
        self.line_name.setObjectName(u"line_name")

        self.gridLayout_3.addWidget(self.line_name, 0, 1, 1, 1)

        self.LabelOrg = QLabel(self.frame_14)
        self.LabelOrg.setObjectName(u"LabelOrg")

        self.gridLayout_3.addWidget(self.LabelOrg, 1, 0, 1, 1)

        self.line_org = QLineEdit(self.frame_14)
        self.line_org.setObjectName(u"line_org")

        self.gridLayout_3.addWidget(self.line_org, 1, 1, 1, 1)

        self.label_6 = QLabel(self.frame_14)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_3.addWidget(self.label_6, 2, 0, 1, 1)

        self.line_team = QLineEdit(self.frame_14)
        self.line_team.setObjectName(u"line_team")

        self.gridLayout_3.addWidget(self.line_team, 2, 1, 1, 1)

        self.moduleConfBtn = QPushButton(self.frame_14)
        self.moduleConfBtn.setObjectName(u"moduleConfBtn")

        self.gridLayout_3.addWidget(self.moduleConfBtn, 3, 1, 1, 1)


        self.gridLayout_2.addWidget(self.frame_14, 0, 0, 1, 1)


        self.verticalLayout_3.addWidget(self.frame_9)


        self.verticalLayout.addWidget(self.confWokspace_menu)

        self.help_menu = QFrame(self.body_window)
        self.help_menu.setObjectName(u"help_menu")
        self.help_menu.setMaximumSize(QSize(16777215, 0))
        self.help_menu.setFrameShape(QFrame.StyledPanel)
        self.help_menu.setFrameShadow(QFrame.Raised)

        self.verticalLayout.addWidget(self.help_menu)


        self.verticalLayout_2.addWidget(self.body_window)


        self.gridLayout.addWidget(self.mainwindow, 0, 0, 1, 1)

        IPTC.setCentralWidget(self.centralwidget)

        self.retranslateUi(IPTC)

        QMetaObject.connectSlotsByName(IPTC)
    # setupUi

    def retranslateUi(self, IPTC):
        IPTC.setWindowTitle(QCoreApplication.translate("IPTC", u"IPTC", None))
        self.minimize_btn.setText("")
        self.maximize_btn.setText("")
        self.close_btn.setText("")
        self.SETECLabel.setText("")
        self.label_2.setText("")
        self.confWorkspaceBtn.setText(QCoreApplication.translate("IPTC", u"Configure Workspace", None))
        self.devBtnTest.setText(QCoreApplication.translate("IPTC", u"Develop and run tests", None))
        self.dataResultBtn.setText(QCoreApplication.translate("IPTC", u"Data results", None))
        self.helpBtn.setText(QCoreApplication.translate("IPTC", u"Help", None))
        self.side_btn_tests.setText("")
        self.tests_recent_btn.setText(QCoreApplication.translate("IPTC", u"Recents", None))
        self.newSeqBtn.setText(QCoreApplication.translate("IPTC", u"New sequence", None))
        self.uploadFile.setText(QCoreApplication.translate("IPTC", u"Upload file", None))
        self.template_2.setText(QCoreApplication.translate("IPTC", u"Template", None))
        self.sideResultsBtn.setText("")
        self.intAnalysisBtn.setText(QCoreApplication.translate("IPTC", u"Integrated analysis", None))
        self.filTagsGrBtn.setText(QCoreApplication.translate("IPTC", u"Filters, Tags & Groups", None))
        self.interacGraphBtn.setText(QCoreApplication.translate("IPTC", u"Interactive graphics", None))
        self.patAnoDetBtn.setText(QCoreApplication.translate("IPTC", u"Pattern and Anomaly detection", None))
        self.resultCompBtn.setText(QCoreApplication.translate("IPTC", u"Results Comparison ", None))
        self.customReportBtn.setText(QCoreApplication.translate("IPTC", u"Customize reports", None))
        self.selectWorkspaceBtn.setText(QCoreApplication.translate("IPTC", u"Choose a saved Workspace", None))
        self.newWorkspaceBtn.setText(QCoreApplication.translate("IPTC", u"Create a new workspace", None))
        self.manageNotifBtn.setText(QCoreApplication.translate("IPTC", u"Manage Notifications", None))
        self.logEventsBtn.setText(QCoreApplication.translate("IPTC", u"Log events", None))
        self.preloadTestsBtn.setText(QCoreApplication.translate("IPTC", u"Pre-load tests", None))
        self.exportSettingsBtn.setText(QCoreApplication.translate("IPTC", u"Export settings", None))
        self.viewSavedBtn.setText(QCoreApplication.translate("IPTC", u"View saved tests", None))
        self.LabelName.setText(QCoreApplication.translate("IPTC", u"Name", None))
        self.LabelOrg.setText(QCoreApplication.translate("IPTC", u"Org", None))
        self.label_6.setText(QCoreApplication.translate("IPTC", u"Team", None))
        self.moduleConfBtn.setText(QCoreApplication.translate("IPTC", u"Modules settings", None))
    # retranslateUi

