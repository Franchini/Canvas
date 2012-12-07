# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'table.ui'
#
# Created: Wed Jun 27 17:19:47 2012
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_TableWindow(object):
    def setupUi(self, TableWindow):
        TableWindow.setObjectName(_fromUtf8("TableWindow"))
        TableWindow.resize(612, 437)
        self.tableWidget = QtGui.QTableWidget(TableWindow)
        self.tableWidget.setGeometry(QtCore.QRect(0, 0, 611, 431))
        self.tableWidget.setRowCount(13)
        self.tableWidget.setColumnCount(9)
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)

        self.retranslateUi(TableWindow)
        QtCore.QMetaObject.connectSlotsByName(TableWindow)

    def retranslateUi(self, TableWindow):
        TableWindow.setWindowTitle(QtGui.QApplication.translate("TableWindow", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget.setSortingEnabled(True)
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(QtGui.QApplication.translate("TableWindow", "X", None, QtGui.QApplication.UnicodeUTF8))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(QtGui.QApplication.translate("TableWindow", "Y", None, QtGui.QApplication.UnicodeUTF8))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(QtGui.QApplication.translate("TableWindow", "Z", None, QtGui.QApplication.UnicodeUTF8))

