# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Dokumente\Studium\Projects\KSS Projekt\Canvas\ui\table.ui'
#
# Created: Mon Dec 17 18:48:48 2012
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
        self.tableWidget.setGeometry(QtCore.QRect(0, 0, 641, 371))
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
        self.buttonApply = QtGui.QPushButton(self.tabFilter)
        self.buttonApply.setGeometry(QtCore.QRect(540, 180, 75, 23))
        self.buttonApply.setObjectName(_fromUtf8("buttonApply"))
        self.line = QtGui.QFrame(self.tabFilter)
        self.line.setGeometry(QtCore.QRect(173, 10, 20, 191))
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.formLayoutWidget = QtGui.QWidget(self.tabFilter)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 40, 160, 171))
        self.formLayoutWidget.setObjectName(_fromUtf8("formLayoutWidget"))
        self.columnSelect = QtGui.QFormLayout(self.formLayoutWidget)
        self.columnSelect.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.columnSelect.setMargin(0)
        self.columnSelect.setObjectName(_fromUtf8("columnSelect"))
        self.line_2 = QtGui.QFrame(self.tabFilter)
        self.line_2.setGeometry(QtCore.QRect(350, 10, 20, 191))
        self.line_2.setFrameShape(QtGui.QFrame.VLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.checkNewWindow = QtGui.QCheckBox(self.tabFilter)
        self.checkNewWindow.setGeometry(QtCore.QRect(370, 40, 201, 21))
        self.checkNewWindow.setChecked(True)
        self.checkNewWindow.setObjectName(_fromUtf8("checkNewWindow"))
        self.widget = QtGui.QWidget(self.tabFilter)
        self.widget.setGeometry(QtCore.QRect(190, 40, 164, 81))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.gridLayout = QtGui.QGridLayout(self.widget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_3 = QtGui.QLabel(self.widget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)
        self.filterStart = QtGui.QDateTimeEdit(self.widget)
        self.filterStart.setCalendarPopup(True)
        self.filterStart.setObjectName(_fromUtf8("filterStart"))
        self.gridLayout.addWidget(self.filterStart, 0, 1, 1, 1)
        self.label_4 = QtGui.QLabel(self.widget)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 1, 0, 1, 1)
        self.filterEnd = QtGui.QDateTimeEdit(self.widget)
        self.filterEnd.setCalendarPopup(True)
        self.filterEnd.setObjectName(_fromUtf8("filterEnd"))
        self.gridLayout.addWidget(self.filterEnd, 1, 1, 1, 1)
        self.widget1 = QtGui.QWidget(self.tabFilter)
        self.widget1.setGeometry(QtCore.QRect(10, 10, 541, 16))
        self.widget1.setObjectName(_fromUtf8("widget1"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.widget1)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(self.widget1)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.label_2 = QtGui.QLabel(self.widget1)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout.addWidget(self.label_2)
        self.label_5 = QtGui.QLabel(self.widget1)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.horizontalLayout.addWidget(self.label_5)
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
        self.commandExport = QtGui.QCommandLinkButton(TableWindow)
        self.commandExport.setGeometry(QtCore.QRect(470, 370, 171, 41))
        self.commandExport.setIconSize(QtCore.QSize(20, 20))
        self.commandExport.setCheckable(False)
        self.commandExport.setObjectName(_fromUtf8("commandExport"))

        self.retranslateUi(TableWindow)
        self.tabTools.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(TableWindow)

    def retranslateUi(self, TableWindow):
        TableWindow.setWindowTitle(QtGui.QApplication.translate("TableWindow", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget.setSortingEnabled(True)
        self.buttonApply.setText(QtGui.QApplication.translate("TableWindow", "Apply", None, QtGui.QApplication.UnicodeUTF8))
        self.checkNewWindow.setText(QtGui.QApplication.translate("TableWindow", "open filtered data in a new window", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("TableWindow", "from:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("TableWindow", "to:", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("TableWindow", "Select Columns:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("TableWindow", "Select by Date", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("TableWindow", "Options", None, QtGui.QApplication.UnicodeUTF8))
        self.tabTools.setTabText(self.tabTools.indexOf(self.tabFilter), QtGui.QApplication.translate("TableWindow", "Filter", None, QtGui.QApplication.UnicodeUTF8))
        self.statisticOutput.setText(QtGui.QApplication.translate("TableWindow", "This is the statistical output area.\n"
"Select data to list its statistical properties", None, QtGui.QApplication.UnicodeUTF8))
        self.tabTools.setTabText(self.tabTools.indexOf(self.tabStatistic), QtGui.QApplication.translate("TableWindow", "Statistics", None, QtGui.QApplication.UnicodeUTF8))
        self.checkTool.setText(QtGui.QApplication.translate("TableWindow", "enable Statistic Tools", None, QtGui.QApplication.UnicodeUTF8))
        self.commandExport.setText(QtGui.QApplication.translate("TableWindow", "set as new Dataset", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    TableWindow = QtGui.QDialog()
    ui = Ui_TableWindow()
    ui.setupUi(TableWindow)
    TableWindow.show()
    sys.exit(app.exec_())

