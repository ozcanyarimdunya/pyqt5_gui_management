# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'middle.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_FormMiddle(object):
    def setupUi(self, FormMiddle):
        FormMiddle.setObjectName("FormMiddle")
        FormMiddle.resize(500, 300)
        self.gridLayout = QtWidgets.QGridLayout(FormMiddle)
        self.gridLayout.setObjectName("gridLayout")
        self.tableViewData = QtWidgets.QTableView(FormMiddle)
        self.tableViewData.setObjectName("tableViewData")
        self.gridLayout.addWidget(self.tableViewData, 1, 0, 1, 3)
        self.pushButton_Configure = QtWidgets.QPushButton(FormMiddle)
        self.pushButton_Configure.setObjectName("pushButton_Configure")
        self.gridLayout.addWidget(self.pushButton_Configure, 0, 0, 1, 1)
        self.pushButton_Edit_Delete = QtWidgets.QPushButton(FormMiddle)
        self.pushButton_Edit_Delete.setObjectName("pushButton_Edit")
        self.gridLayout.addWidget(self.pushButton_Edit_Delete, 0, 2, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 1, 1, 1)

        self.retranslateUi(FormMiddle)
        QtCore.QMetaObject.connectSlotsByName(FormMiddle)

    def retranslateUi(self, FormMiddle):
        _translate = QtCore.QCoreApplication.translate
        FormMiddle.setWindowTitle(_translate("FormMiddle", "Form"))
        self.pushButton_Configure.setText(_translate("FormMiddle", "Configure"))
        self.pushButton_Edit_Delete.setText(_translate("FormMiddle", "Edit / Delete"))

