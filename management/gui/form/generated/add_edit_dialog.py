# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/add_edit_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(480, 160)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_OK = QtWidgets.QPushButton(Dialog)
        self.pushButton_OK.setObjectName("pushButton_OK")
        self.gridLayout.addWidget(self.pushButton_OK, 1, 2, 1, 1)
        self.pushButton_Cancel = QtWidgets.QPushButton(Dialog)
        self.pushButton_Cancel.setObjectName("pushButton_Cancel")
        self.gridLayout.addWidget(self.pushButton_Cancel, 1, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 0, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setObjectName("groupBox")
        self.formLayout_e = QtWidgets.QFormLayout(self.groupBox)
        self.formLayout_e.setObjectName("formLayout_e")
        self.label_e = QtWidgets.QLabel(self.groupBox)
        self.label_e.setObjectName("label_e")
        self.formLayout_e.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_e)
        self.lineEdit_ProjectName = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_ProjectName.setObjectName("lineEdit_ProjectName")
        self.formLayout_e.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit_ProjectName)
        self.label_e_2 = QtWidgets.QLabel(self.groupBox)
        self.label_e_2.setObjectName("label_e_2")
        self.formLayout_e.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_e_2)
        self.lineEdit_CompanyName = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_CompanyName.setObjectName("lineEdit_CompanyName")
        self.formLayout_e.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_CompanyName)
        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 3)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton_OK.setText(_translate("Dialog", "OK"))
        self.pushButton_Cancel.setText(_translate("Dialog", "Cancel"))
        self.groupBox.setTitle(_translate("Dialog", "Project Information"))
        self.label_e.setText(_translate("Dialog", "Project Name:"))
        self.lineEdit_ProjectName.setPlaceholderText(_translate("Dialog", "Enter your project name .."))
        self.label_e_2.setText(_translate("Dialog", "Company Name:"))
        self.lineEdit_CompanyName.setPlaceholderText(_translate("Dialog", "Enter your company name .."))
