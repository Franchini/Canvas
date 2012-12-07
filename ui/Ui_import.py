# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Dokumente\Studium\Projects\KSS Projekt\Canvas\ui\import.ui'
#
# Created: Sat Nov 17 13:37:39 2012
#      by: PyQt4 UI code generator 4.9.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_ImportDialog(object):
    def setupUi(self, ImportDialog):
        ImportDialog.setObjectName(_fromUtf8("ImportDialog"))
        ImportDialog.setWindowModality(QtCore.Qt.ApplicationModal)
        ImportDialog.resize(443, 408)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ImportDialog.sizePolicy().hasHeightForWidth())
        ImportDialog.setSizePolicy(sizePolicy)
        ImportDialog.setModal(True)
        self.filename = QtGui.QLineEdit(ImportDialog)
        self.filename.setGeometry(QtCore.QRect(120, 10, 211, 20))
        self.filename.setObjectName(_fromUtf8("filename"))
        self.buttonSearch = QtGui.QPushButton(ImportDialog)
        self.buttonSearch.setGeometry(QtCore.QRect(350, 10, 75, 23))
        self.buttonSearch.setObjectName(_fromUtf8("buttonSearch"))
        self.buttonEdit = QtGui.QPushButton(ImportDialog)
        self.buttonEdit.setEnabled(False)
        self.buttonEdit.setGeometry(QtCore.QRect(20, 10, 75, 23))
        self.buttonEdit.setDefault(False)
        self.buttonEdit.setFlat(False)
        self.buttonEdit.setObjectName(_fromUtf8("buttonEdit"))
        self.layoutWidget = QtGui.QWidget(ImportDialog)
        self.layoutWidget.setGeometry(QtCore.QRect(270, 370, 158, 25))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.buttonCancel = QtGui.QPushButton(self.layoutWidget)
        self.buttonCancel.setObjectName(_fromUtf8("buttonCancel"))
        self.horizontalLayout.addWidget(self.buttonCancel)
        self.buttonImport = QtGui.QPushButton(self.layoutWidget)
        self.buttonImport.setObjectName(_fromUtf8("buttonImport"))
        self.horizontalLayout.addWidget(self.buttonImport)
        self.lblColumns = QtGui.QLabel(ImportDialog)
        self.lblColumns.setGeometry(QtCore.QRect(120, 30, 151, 16))
        self.lblColumns.setObjectName(_fromUtf8("lblColumns"))
        self.scrollArea = QtGui.QScrollArea(ImportDialog)
        self.scrollArea.setGeometry(QtCore.QRect(0, 100, 441, 261))
        self.scrollArea.setFrameShadow(QtGui.QFrame.Raised)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 439, 259))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.sensorDepth0 = QtGui.QLineEdit(self.scrollAreaWidgetContents)
        self.sensorDepth0.setEnabled(False)
        self.sensorDepth0.setGeometry(QtCore.QRect(120, 30, 111, 20))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sensorDepth0.sizePolicy().hasHeightForWidth())
        self.sensorDepth0.setSizePolicy(sizePolicy)
        self.sensorDepth0.setObjectName(_fromUtf8("sensorDepth0"))
        self.sensorType0 = QtGui.QComboBox(self.scrollAreaWidgetContents)
        self.sensorType0.setGeometry(QtCore.QRect(280, 30, 141, 22))
        self.sensorType0.setEditable(False)
        self.sensorType0.setObjectName(_fromUtf8("sensorType0"))
        self.sensorType0.addItem(_fromUtf8(""))
        self.sensorType0.addItem(_fromUtf8(""))
        self.sensorType0.addItem(_fromUtf8(""))
        self.label = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label.setGeometry(QtCore.QRect(290, 10, 220, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_2.setGeometry(QtCore.QRect(140, 10, 111, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.sensorName0 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.sensorName0.setGeometry(QtCore.QRect(10, 30, 111, 16))
        self.sensorName0.setObjectName(_fromUtf8("sensorName0"))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.retranslateUi(ImportDialog)
        QtCore.QMetaObject.connectSlotsByName(ImportDialog)

    def retranslateUi(self, ImportDialog):
        ImportDialog.setWindowTitle(QtGui.QApplication.translate("ImportDialog", "Import Data", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonSearch.setText(QtGui.QApplication.translate("ImportDialog", "Search", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonEdit.setText(QtGui.QApplication.translate("ImportDialog", "Edit", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonCancel.setText(QtGui.QApplication.translate("ImportDialog", "Cancel", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonImport.setText(QtGui.QApplication.translate("ImportDialog", "Import", None, QtGui.QApplication.UnicodeUTF8))
        self.lblColumns.setText(QtGui.QApplication.translate("ImportDialog", "0 datasets have been found", None, QtGui.QApplication.UnicodeUTF8))
        self.sensorDepth0.setText(QtGui.QApplication.translate("ImportDialog", "d", None, QtGui.QApplication.UnicodeUTF8))
        self.sensorType0.setItemText(0, QtGui.QApplication.translate("ImportDialog", "Date [XXXX]", None, QtGui.QApplication.UnicodeUTF8))
        self.sensorType0.setItemText(1, QtGui.QApplication.translate("ImportDialog", "Soil Moisture [Vol/Vol]", None, QtGui.QApplication.UnicodeUTF8))
        self.sensorType0.setItemText(2, QtGui.QApplication.translate("ImportDialog", "Matrix Potential [kPa]", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("ImportDialog", "Data type:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("ImportDialog", "Depth [cm]:", None, QtGui.QApplication.UnicodeUTF8))
        self.sensorName0.setText(QtGui.QApplication.translate("ImportDialog", "Default", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    ImportDialog = QtGui.QDialog()
    ui = Ui_ImportDialog()
    ui.setupUi(ImportDialog)
    ImportDialog.show()
    sys.exit(app.exec_())

