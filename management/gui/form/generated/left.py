# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'left.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_FormLeft(object):
    def setupUi(self, FormLeft):
        FormLeft.setObjectName("FormLeft")
        FormLeft.resize(200, 450)
        self.gridLayout = QtWidgets.QGridLayout(FormLeft)
        self.gridLayout.setObjectName("gridLayout")
        self.listView = QtWidgets.QListView(FormLeft)
        self.listView.setObjectName("listView")
        self.gridLayout.addWidget(self.listView, 1, 0, 1, 1)
        self.pushButton_CreateNewProject = QtWidgets.QPushButton(FormLeft)
        self.pushButton_CreateNewProject.setObjectName("pushButton_CreateNewProject")
        self.gridLayout.addWidget(self.pushButton_CreateNewProject, 0, 0, 1, 1)

        self.retranslateUi(FormLeft)
        QtCore.QMetaObject.connectSlotsByName(FormLeft)

    def retranslateUi(self, FormLeft):
        _translate = QtCore.QCoreApplication.translate
        FormLeft.setWindowTitle(_translate("FormLeft", "Form"))
        self.pushButton_CreateNewProject.setText(_translate("FormLeft", "Create New Project"))

