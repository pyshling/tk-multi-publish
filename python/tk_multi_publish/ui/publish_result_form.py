# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'publish_result_form.ui'
#
# Created: Tue Apr  2 19:00:24 2013
#      by: pyside-uic 0.2.13 running on PySide 1.1.0
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_PublishResulForm(object):
    def setupUi(self, PublishResulForm):
        PublishResulForm.setObjectName("PublishResulForm")
        PublishResulForm.resize(494, 386)
        self.verticalLayout_4 = QtGui.QVBoxLayout(PublishResulForm)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        spacerItem = QtGui.QSpacerItem(20, 97, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.status_icon = QtGui.QLabel(PublishResulForm)
        self.status_icon.setMinimumSize(QtCore.QSize(80, 80))
        self.status_icon.setMaximumSize(QtCore.QSize(80, 80))
        self.status_icon.setBaseSize(QtCore.QSize(32, 32))
        self.status_icon.setText("")
        self.status_icon.setPixmap(QtGui.QPixmap(":/res/success.png"))
        self.status_icon.setScaledContents(False)
        self.status_icon.setAlignment(QtCore.Qt.AlignCenter)
        self.status_icon.setObjectName("status_icon")
        self.verticalLayout_2.addWidget(self.status_icon)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem2)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.status_title = QtGui.QLabel(PublishResulForm)
        self.status_title.setStyleSheet("#status_title {\n"
"font-size: 24px;\n"
"}")
        self.status_title.setObjectName("status_title")
        self.verticalLayout_3.addWidget(self.status_title)
        self.status_details = QtGui.QLabel(PublishResulForm)
        self.status_details.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.status_details.setWordWrap(False)
        self.status_details.setObjectName("status_details")
        self.verticalLayout_3.addWidget(self.status_details)
        self.verticalLayout_3.setStretch(1, 1)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(2, 1)
        self.horizontalLayout.setStretch(3, 1)
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        spacerItem4 = QtGui.QSpacerItem(20, 97, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem4)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem5)
        self.close_btn = QtGui.QPushButton(PublishResulForm)
        self.close_btn.setObjectName("close_btn")
        self.horizontalLayout_2.addWidget(self.close_btn)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        self.verticalLayout_4.setStretch(0, 1)
        self.verticalLayout_4.setStretch(1, 1)
        self.verticalLayout_4.setStretch(2, 1)

        self.retranslateUi(PublishResulForm)
        QtCore.QMetaObject.connectSlotsByName(PublishResulForm)

    def retranslateUi(self, PublishResulForm):
        PublishResulForm.setWindowTitle(QtGui.QApplication.translate("PublishResulForm", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.status_title.setText(QtGui.QApplication.translate("PublishResulForm", "Success!", None, QtGui.QApplication.UnicodeUTF8))
        self.status_details.setText(QtGui.QApplication.translate("PublishResulForm", "Details...", None, QtGui.QApplication.UnicodeUTF8))
        self.close_btn.setText(QtGui.QApplication.translate("PublishResulForm", "Close", None, QtGui.QApplication.UnicodeUTF8))

from . import resources_rc
from . import resources_rc