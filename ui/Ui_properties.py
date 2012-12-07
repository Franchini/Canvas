# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Dokumente\Studium\Projects\KSS Projekt\Canvas\ui\properties.ui'
#
# Created: Mon Nov 26 18:22:46 2012
#      by: PyQt4 UI code generator 4.9.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Properties(object):
    def setupUi(self, Properties):
        Properties.setObjectName(_fromUtf8("Properties"))
        Properties.resize(298, 345)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Properties.sizePolicy().hasHeightForWidth())
        Properties.setSizePolicy(sizePolicy)
        self.Tab = QtGui.QTabWidget(Properties)
        self.Tab.setGeometry(QtCore.QRect(10, 10, 281, 301))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Tab.sizePolicy().hasHeightForWidth())
        self.Tab.setSizePolicy(sizePolicy)
        self.Tab.setObjectName(_fromUtf8("Tab"))
        self.tab1 = QtGui.QWidget()
        self.tab1.setObjectName(_fromUtf8("tab1"))
        self.label_3 = QtGui.QLabel(self.tab1)
        self.label_3.setGeometry(QtCore.QRect(20, 160, 221, 91))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.layoutWidget = QtGui.QWidget(self.tab1)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 20, 261, 121))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.layoutWidget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(self.layoutWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.separationChar = QtGui.QLineEdit(self.layoutWidget)
        self.separationChar.setObjectName(_fromUtf8("separationChar"))
        self.gridLayout.addWidget(self.separationChar, 0, 1, 1, 1)
        self.label_2 = QtGui.QLabel(self.layoutWidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.dateFormat = QtGui.QLineEdit(self.layoutWidget)
        self.dateFormat.setObjectName(_fromUtf8("dateFormat"))
        self.gridLayout.addWidget(self.dateFormat, 1, 1, 1, 1)
        self.Tab.addTab(self.tab1, _fromUtf8(""))
        self.tab2 = QtGui.QWidget()
        self.tab2.setObjectName(_fromUtf8("tab2"))
        self.layoutWidget1 = QtGui.QWidget(self.tab2)
        self.layoutWidget1.setGeometry(QtCore.QRect(10, 10, 261, 191))
        self.layoutWidget1.setObjectName(_fromUtf8("layoutWidget1"))
        self.gridLayout_2 = QtGui.QGridLayout(self.layoutWidget1)
        self.gridLayout_2.setMargin(0)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.label_4 = QtGui.QLabel(self.layoutWidget1)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout_2.addWidget(self.label_4, 0, 0, 1, 1)
        self.mysqlServer = QtGui.QLineEdit(self.layoutWidget1)
        self.mysqlServer.setObjectName(_fromUtf8("mysqlServer"))
        self.gridLayout_2.addWidget(self.mysqlServer, 0, 1, 1, 1)
        self.label_5 = QtGui.QLabel(self.layoutWidget1)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout_2.addWidget(self.label_5, 1, 0, 1, 1)
        self.mysqlName = QtGui.QLineEdit(self.layoutWidget1)
        self.mysqlName.setObjectName(_fromUtf8("mysqlName"))
        self.gridLayout_2.addWidget(self.mysqlName, 1, 1, 1, 1)
        self.label_6 = QtGui.QLabel(self.layoutWidget1)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout_2.addWidget(self.label_6, 2, 0, 1, 1)
        self.mysqlPw = QtGui.QLineEdit(self.layoutWidget1)
        self.mysqlPw.setObjectName(_fromUtf8("mysqlPw"))
        self.gridLayout_2.addWidget(self.mysqlPw, 2, 1, 1, 1)
        self.label_7 = QtGui.QLabel(self.layoutWidget1)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout_2.addWidget(self.label_7, 3, 0, 1, 1)
        self.mysqlBase = QtGui.QLineEdit(self.layoutWidget1)
        self.mysqlBase.setObjectName(_fromUtf8("mysqlBase"))
        self.gridLayout_2.addWidget(self.mysqlBase, 3, 1, 1, 1)
        self.label_8 = QtGui.QLabel(self.layoutWidget1)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.gridLayout_2.addWidget(self.label_8, 4, 0, 1, 1)
        self.mysqlDatatable = QtGui.QLineEdit(self.layoutWidget1)
        self.mysqlDatatable.setObjectName(_fromUtf8("mysqlDatatable"))
        self.gridLayout_2.addWidget(self.mysqlDatatable, 4, 1, 1, 1)
        self.Tab.addTab(self.tab2, _fromUtf8(""))
        self.widget = QtGui.QWidget(Properties)
        self.widget.setGeometry(QtCore.QRect(130, 310, 158, 25))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.widget)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.buttonOk = QtGui.QPushButton(self.widget)
        self.buttonOk.setObjectName(_fromUtf8("buttonOk"))
        self.horizontalLayout.addWidget(self.buttonOk)
        self.buttonCancel = QtGui.QPushButton(self.widget)
        self.buttonCancel.setObjectName(_fromUtf8("buttonCancel"))
        self.horizontalLayout.addWidget(self.buttonCancel)

        self.retranslateUi(Properties)
        self.Tab.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Properties)

    def retranslateUi(self, Properties):
        Properties.setWindowTitle(QtGui.QApplication.translate("Properties", "Properties", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Properties", "For the proper Date Format use:\n"
"%y   for year\n"
"%m  for month\n"
"%d  for day\n"
"%h  for hour\n"
"%i   for minutes", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Properties", "Separation Char  ", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Properties", "Date Format", None, QtGui.QApplication.UnicodeUTF8))
        self.Tab.setTabText(self.Tab.indexOf(self.tab1), QtGui.QApplication.translate("Properties", "Import", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("Properties", "Server", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("Properties", "Username", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("Properties", "Password", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("Properties", "Database", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("Properties", "Datatable", None, QtGui.QApplication.UnicodeUTF8))
        self.Tab.setTabText(self.Tab.indexOf(self.tab2), QtGui.QApplication.translate("Properties", "MySQL", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonOk.setText(QtGui.QApplication.translate("Properties", "OK", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonCancel.setText(QtGui.QApplication.translate("Properties", "Cancel", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Properties = QtGui.QDialog()
    ui = Ui_Properties()
    ui.setupUi(Properties)
    Properties.show()
    sys.exit(app.exec_())

