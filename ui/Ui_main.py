# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Dokumente\Studium\Projects\KSS Projekt\Canvas\ui\main.ui'
#
# Created: Wed Dec 19 10:14:06 2012
#      by: PyQt4 UI code generator 4.9.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(956, 765)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setMaximumSize(QtCore.QSize(800, 540))
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setEnabled(True)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 956, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuEdit = QtGui.QMenu(self.menubar)
        self.menuEdit.setObjectName(_fromUtf8("menuEdit"))
        self.menuOpen_Connection = QtGui.QMenu(self.menuEdit)
        self.menuOpen_Connection.setObjectName(_fromUtf8("menuOpen_Connection"))
        self.menuTools = QtGui.QMenu(self.menubar)
        self.menuTools.setObjectName(_fromUtf8("menuTools"))
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.Toolbox = QtGui.QDockWidget(MainWindow)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Toolbox.sizePolicy().hasHeightForWidth())
        self.Toolbox.setSizePolicy(sizePolicy)
        self.Toolbox.setMinimumSize(QtCore.QSize(138, 724))
        self.Toolbox.setAutoFillBackground(False)
        self.Toolbox.setStyleSheet(_fromUtf8(""))
        self.Toolbox.setFeatures(QtGui.QDockWidget.DockWidgetFloatable|QtGui.QDockWidget.DockWidgetMovable)
        self.Toolbox.setAllowedAreas(QtCore.Qt.LeftDockWidgetArea|QtCore.Qt.RightDockWidgetArea)
        self.Toolbox.setObjectName(_fromUtf8("Toolbox"))
        self.dockWidgetContents = QtGui.QWidget()
        self.dockWidgetContents.setObjectName(_fromUtf8("dockWidgetContents"))
        self.layoutWidget = QtGui.QWidget(self.dockWidgetContents)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 116, 301))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.buttonDatabaseManager = QtGui.QPushButton(self.layoutWidget)
        self.buttonDatabaseManager.setObjectName(_fromUtf8("buttonDatabaseManager"))
        self.verticalLayout.addWidget(self.buttonDatabaseManager)
        self.buttonImport = QtGui.QPushButton(self.layoutWidget)
        self.buttonImport.setObjectName(_fromUtf8("buttonImport"))
        self.verticalLayout.addWidget(self.buttonImport)
        self.buttonProperties = QtGui.QPushButton(self.layoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonProperties.sizePolicy().hasHeightForWidth())
        self.buttonProperties.setSizePolicy(sizePolicy)
        self.buttonProperties.setObjectName(_fromUtf8("buttonProperties"))
        self.verticalLayout.addWidget(self.buttonProperties)
        self.buttonMysql = QtGui.QPushButton(self.layoutWidget)
        self.buttonMysql.setObjectName(_fromUtf8("buttonMysql"))
        self.verticalLayout.addWidget(self.buttonMysql)
        self.buttonExport = QtGui.QPushButton(self.layoutWidget)
        self.buttonExport.setObjectName(_fromUtf8("buttonExport"))
        self.verticalLayout.addWidget(self.buttonExport)
        self.buttonTable = QtGui.QPushButton(self.layoutWidget)
        self.buttonTable.setObjectName(_fromUtf8("buttonTable"))
        self.verticalLayout.addWidget(self.buttonTable)
        self.Toolbox.setWidget(self.dockWidgetContents)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.Toolbox)
        self.actionExit = QtGui.QAction(MainWindow)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.actionDatabase_datatable = QtGui.QAction(MainWindow)
        self.actionDatabase_datatable.setObjectName(_fromUtf8("actionDatabase_datatable"))
        self.actionDatabase_Connection = QtGui.QAction(MainWindow)
        self.actionDatabase_Connection.setObjectName(_fromUtf8("actionDatabase_Connection"))
        self.actionDatatable = QtGui.QAction(MainWindow)
        self.actionDatatable.setObjectName(_fromUtf8("actionDatatable"))
        self.actionConnection = QtGui.QAction(MainWindow)
        self.actionConnection.setObjectName(_fromUtf8("actionConnection"))
        self.actionDatatable_2 = QtGui.QAction(MainWindow)
        self.actionDatatable_2.setObjectName(_fromUtf8("actionDatatable_2"))
        self.actionAbout = QtGui.QAction(MainWindow)
        self.actionAbout.setObjectName(_fromUtf8("actionAbout"))
        self.actionToolbox = QtGui.QAction(MainWindow)
        self.actionToolbox.setCheckable(True)
        self.actionToolbox.setChecked(True)
        self.actionToolbox.setObjectName(_fromUtf8("actionToolbox"))
        self.actionTable = QtGui.QAction(MainWindow)
        self.actionTable.setObjectName(_fromUtf8("actionTable"))
        self.actionConnect_defaut_Db = QtGui.QAction(MainWindow)
        self.actionConnect_defaut_Db.setObjectName(_fromUtf8("actionConnect_defaut_Db"))
        self.actionDefaultConnection = QtGui.QAction(MainWindow)
        self.actionDefaultConnection.setObjectName(_fromUtf8("actionDefaultConnection"))
        self.actionSave = QtGui.QAction(MainWindow)
        self.actionSave.setObjectName(_fromUtf8("actionSave"))
        self.actionTable_2 = QtGui.QAction(MainWindow)
        self.actionTable_2.setObjectName(_fromUtf8("actionTable_2"))
        self.actionPreferences = QtGui.QAction(MainWindow)
        self.actionPreferences.setObjectName(_fromUtf8("actionPreferences"))
        self.actionImportFile = QtGui.QAction(MainWindow)
        self.actionImportFile.setObjectName(_fromUtf8("actionImportFile"))
        self.actionImportConnection = QtGui.QAction(MainWindow)
        self.actionImportConnection.setObjectName(_fromUtf8("actionImportConnection"))
        self.actionDatabaseManager = QtGui.QAction(MainWindow)
        self.actionDatabaseManager.setObjectName(_fromUtf8("actionDatabaseManager"))
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionExit)
        self.menuOpen_Connection.addAction(self.actionImportFile)
        self.menuOpen_Connection.addAction(self.actionImportConnection)
        self.menuEdit.addAction(self.actionTable_2)
        self.menuEdit.addAction(self.menuOpen_Connection.menuAction())
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionPreferences)
        self.menuTools.addAction(self.actionDatabaseManager)
        self.menuHelp.addAction(self.actionAbout)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuTools.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setTitle(QtGui.QApplication.translate("MainWindow", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.menuEdit.setTitle(QtGui.QApplication.translate("MainWindow", "Edit", None, QtGui.QApplication.UnicodeUTF8))
        self.menuOpen_Connection.setTitle(QtGui.QApplication.translate("MainWindow", "Import Data", None, QtGui.QApplication.UnicodeUTF8))
        self.menuTools.setTitle(QtGui.QApplication.translate("MainWindow", "Tools", None, QtGui.QApplication.UnicodeUTF8))
        self.menuHelp.setTitle(QtGui.QApplication.translate("MainWindow", "Help", None, QtGui.QApplication.UnicodeUTF8))
        self.Toolbox.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Toolbox", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonDatabaseManager.setText(QtGui.QApplication.translate("MainWindow", "Manage Connections", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonImport.setText(QtGui.QApplication.translate("MainWindow", "Import", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonProperties.setText(QtGui.QApplication.translate("MainWindow", "Properties", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonMysql.setText(QtGui.QApplication.translate("MainWindow", "Import from Database", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonExport.setText(QtGui.QApplication.translate("MainWindow", "Export to Database", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonTable.setText(QtGui.QApplication.translate("MainWindow", "View Table", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExit.setText(QtGui.QApplication.translate("MainWindow", "Exit", None, QtGui.QApplication.UnicodeUTF8))
        self.actionDatabase_datatable.setText(QtGui.QApplication.translate("MainWindow", "database datatable", None, QtGui.QApplication.UnicodeUTF8))
        self.actionDatabase_Connection.setText(QtGui.QApplication.translate("MainWindow", "Database Connection...", None, QtGui.QApplication.UnicodeUTF8))
        self.actionDatatable.setText(QtGui.QApplication.translate("MainWindow", "Datatable", None, QtGui.QApplication.UnicodeUTF8))
        self.actionConnection.setText(QtGui.QApplication.translate("MainWindow", "Connection", None, QtGui.QApplication.UnicodeUTF8))
        self.actionDatatable_2.setText(QtGui.QApplication.translate("MainWindow", "Datatable", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAbout.setText(QtGui.QApplication.translate("MainWindow", "About", None, QtGui.QApplication.UnicodeUTF8))
        self.actionToolbox.setText(QtGui.QApplication.translate("MainWindow", "Toolbox", None, QtGui.QApplication.UnicodeUTF8))
        self.actionTable.setText(QtGui.QApplication.translate("MainWindow", "Table", None, QtGui.QApplication.UnicodeUTF8))
        self.actionConnect_defaut_Db.setText(QtGui.QApplication.translate("MainWindow", "Connect defaut Db", None, QtGui.QApplication.UnicodeUTF8))
        self.actionDefaultConnection.setText(QtGui.QApplication.translate("MainWindow", "Import default Db", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave.setText(QtGui.QApplication.translate("MainWindow", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.actionTable_2.setText(QtGui.QApplication.translate("MainWindow", "Open Table", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPreferences.setText(QtGui.QApplication.translate("MainWindow", "Preferences", None, QtGui.QApplication.UnicodeUTF8))
        self.actionImportFile.setText(QtGui.QApplication.translate("MainWindow", "file", None, QtGui.QApplication.UnicodeUTF8))
        self.actionImportConnection.setText(QtGui.QApplication.translate("MainWindow", "default connection", None, QtGui.QApplication.UnicodeUTF8))
        self.actionDatabaseManager.setText(QtGui.QApplication.translate("MainWindow", "Database Manager", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

