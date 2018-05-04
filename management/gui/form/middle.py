# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/middle.ui'
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
        self.tableWidgetData = QtWidgets.QTableWidget(FormMiddle)
        self.tableWidgetData.setObjectName("tableWidgetData")
        self.tableWidgetData.setColumnCount(0)
        self.tableWidgetData.setRowCount(0)
        self.gridLayout.addWidget(self.tableWidgetData, 0, 0, 1, 1)

        self.retranslateUi(FormMiddle)
        QtCore.QMetaObject.connectSlotsByName(FormMiddle)

    def retranslateUi(self, FormMiddle):
        _translate = QtCore.QCoreApplication.translate
        FormMiddle.setWindowTitle(_translate("FormMiddle", "Form"))

