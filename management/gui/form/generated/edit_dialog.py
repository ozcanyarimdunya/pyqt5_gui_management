# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/edit_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_DialogEdit(object):
    def setupUi(self, DialogEdit):
        DialogEdit.setObjectName("DialogEdit")
        DialogEdit.resize(480, 160)
        self.gridLayout = QtWidgets.QGridLayout(DialogEdit)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_Delete = QtWidgets.QPushButton(DialogEdit)
        self.pushButton_Delete.setStyleSheet("background-color:red")
        self.pushButton_Delete.setObjectName("pushButton_Delete")
        self.gridLayout.addWidget(self.pushButton_Delete, 1, 0, 1, 1)
        self.pushButton_OK = QtWidgets.QPushButton(DialogEdit)
        self.pushButton_OK.setObjectName("pushButton_OK")
        self.gridLayout.addWidget(self.pushButton_OK, 1, 3, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(DialogEdit)
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
        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 4)
        self.pushButton_Cancel = QtWidgets.QPushButton(DialogEdit)
        self.pushButton_Cancel.setObjectName("pushButton_Cancel")
        self.gridLayout.addWidget(self.pushButton_Cancel, 1, 2, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 1, 1, 1)

        self.retranslateUi(DialogEdit)
        QtCore.QMetaObject.connectSlotsByName(DialogEdit)
        DialogEdit.setTabOrder(self.lineEdit_ProjectName, self.lineEdit_CompanyName)
        DialogEdit.setTabOrder(self.lineEdit_CompanyName, self.pushButton_Cancel)
        DialogEdit.setTabOrder(self.pushButton_Cancel, self.pushButton_OK)
        DialogEdit.setTabOrder(self.pushButton_OK, self.pushButton_Delete)

    def retranslateUi(self, DialogEdit):
        _translate = QtCore.QCoreApplication.translate
        DialogEdit.setWindowTitle(_translate("DialogEdit", "Edit Project"))
        self.pushButton_Delete.setText(_translate("DialogEdit", "Delete"))
        self.pushButton_OK.setText(_translate("DialogEdit", "Save"))
        self.groupBox.setTitle(_translate("DialogEdit", "Project Information"))
        self.label_e.setText(_translate("DialogEdit", "Project Name:"))
        self.lineEdit_ProjectName.setPlaceholderText(_translate("DialogEdit", "Type your project name .."))
        self.label_e_2.setText(_translate("DialogEdit", "Company Name:"))
        self.lineEdit_CompanyName.setPlaceholderText(_translate("DialogEdit", "Type your company name .."))
        self.pushButton_Cancel.setText(_translate("DialogEdit", "Cancel"))

