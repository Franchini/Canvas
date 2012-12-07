import sys, os
from PyQt4 import QtGui, QtCore
from ui.Ui_table import Ui_TableWindow as table

class TableWindow (QtGui.QDialog, table):
    def __init__(self, parent, Data=None):
        QtGui.QDialog.__init__(self)
        self.setupUi(self)
        self.parent = parent
        
        #check if data was transmitted
        if Data is None:
            #no data was transmitted, a dialog will be included here
            parent.errorlog.writeError("Warning: No data was imported into TableWindow")
        else:
            self.Data = Data
            self.__setup(self.Data)
            self.__showData(self.Data.getAllData())
            
        
    def __showData(self, data):
        #includes given data into the QTableWidget
        for i, row in enumerate(data):
            for j, cell in enumerate(row):
                point = QtGui.QTableWidgetItem()
                point.setText(str(cell))
                self.tableWidget.setItem(i, j, point)
                
    def __setup(self, DataObject):
        # will setup the number of rows and columns and name the Window and Columns
        self.tableWidget.setRowCount(len(DataObject.getAllData()))
        depths = DataObject.getDepthsValues()
        self.tableWidget.setColumnCount(len(depths))
        self.setWindowTitle(DataObject.getNameStation())
        
        # set the header names
        for i, depth in enumerate(depths):
            item = QtGui.QTableWidgetItem()
            item.setText(str(depth))
            self.tableWidget.setHorizontalHeaderItem(i, item)
            
