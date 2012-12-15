# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Dokumente\Studium\Projects\KSS Projekt\Canvas\ui\table.ui'
#
# Created: Sat Dec 15 12:24:24 2012
#      by: PyQt4 UI code generator 4.9.4
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
        TableWindow.resize(641, 416)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(TableWindow.sizePolicy().hasHeightForWidth())
        TableWindow.setSizePolicy(sizePolicy)
        TableWindow.setMinimumSize(QtCore.QSize(641, 416))
        TableWindow.setMaximumSize(QtCore.QSize(641, 416))
        self.tableWidget = QtGui.QTableWidget(TableWindow)
        self.tableWidget.setGeometry(QtCore.QRect(0, 0, 641, 381))
        self.tableWidget.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.tableWidget.setSelectionBehavior(QtGui.QAbstractItemView.SelectItems)
        self.tableWidget.setRowCount(13)
        self.tableWidget.setColumnCount(9)
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tabTools = QtGui.QTabWidget(TableWindow)
        self.tabTools.setGeometry(QtCore.QRect(0, 420, 641, 241))
        self.tabTools.setFocusPolicy(QtCore.Qt.TabFocus)
        self.tabTools.setObjectName(_fromUtf8("tabTools"))
        self.tabFilter = QtGui.QWidget()
        self.tabFilter.setObjectName(_fromUtf8("tabFilter"))
        self.tabTools.addTab(self.tabFilter, _fromUtf8(""))
        self.tabStatistic = QtGui.QWidget()
        self.tabStatistic.setFocusPolicy(QtCore.Qt.TabFocus)
        self.tabStatistic.setObjectName(_fromUtf8("tabStatistic"))
        self.statisticOutput = QtGui.QLabel(self.tabStatistic)
        self.statisticOutput.setGeometry(QtCore.QRect(10, 20, 601, 111))
        self.statisticOutput.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.statisticOutput.setObjectName(_fromUtf8("statisticOutput"))
        self.tabTools.addTab(self.tabStatistic, _fromUtf8(""))
        self.checkTool = QtGui.QCheckBox(TableWindow)
        self.checkTool.setGeometry(QtCore.QRect(10, 390, 131, 17))
        self.checkTool.setObjectName(_fromUtf8("checkTool"))

        self.retranslateUi(TableWindow)
        self.tabTools.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(TableWindow)

    def retranslateUi(self, TableWindow):
        TableWindow.setWindowTitle(QtGui.QApplication.translate("TableWindow", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget.setSortingEnabled(True)
        self.tabTools.setTabText(self.tabTools.indexOf(self.tabFilter), QtGui.QApplication.translate("TableWindow", "Filter", None, QtGui.QApplication.UnicodeUTF8))
        self.statisticOutput.setText(QtGui.QApplication.translate("TableWindow", "This is the statistical output area.\n"
"Select data to list its statistical properties", None, QtGui.QApplication.UnicodeUTF8))
        self.tabTools.setTabText(self.tabTools.indexOf(self.tabStatistic), QtGui.QApplication.translate("TableWindow", "Statistics", None, QtGui.QApplication.UnicodeUTF8))
        self.checkTool.setText(QtGui.QApplication.translate("TableWindow", "enable Statistic Tools", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    TableWindow = QtGui.QDialog()
    ui = Ui_TableWindow()
    ui.setupUi(TableWindow)
    TableWindow.show()
    sys.exit(app.exec_())

