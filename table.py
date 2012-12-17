import sys, os,  math, datetime
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
            
        # set slots
        self.connect(self.checkTool, QtCore.SIGNAL("stateChanged(int)"),  self.__oncheckTool)
        self.connect(self.tableWidget, QtCore.SIGNAL("itemSelectionChanged()"), self.__onSelectionChanged)
        
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
        
        # set the column header names
        for i, depth in enumerate(depths):
            item = QtGui.QTableWidgetItem()
            item.setText(str(depth))
            self.tableWidget.setHorizontalHeaderItem(i,  item)
            
        # set the row column header names
        start = self.Data.getStartTime()
        timestep = self.Data.getLengthTimestep("s")
        format = "%d.%m.%y"
        if (timestep < (60*60*24)):
            format = format + " %H:%M"
            if (timestep < 60):
                format = format + ":%S"
        
        for i in range(self.tableWidget.rowCount()):
            item = QtGui.QTableWidgetItem()
            # get time
            time = start + datetime.timedelta(seconds=(timestep*(i+1)))
            item.setText(str(time.strftime(format)))
            self.tableWidget.setVerticalHeaderItem(i, item)
            
    def __oncheckTool(self):
        # check status of checkBox and show or hide tabwidget by setting window size
        if self.checkTool.checkState() == 2:
            #show tabwidget by resizing TableWindow
            self.setMinimumSize(QtCore.QSize(641, 665))
            self.setMaximumSize(QtCore.QSize(641, 665))
            self.resize(641, 665)
        elif self.checkTool.checkState() == 0:
            #hide tabwidget by resizing TableWindow
            self.setMinimumSize(QtCore.QSize(641, 416))
            self.setMaximumSize(QtCore.QSize(641, 416))
            self.resize(641, 416)
        
    def __onSelectionChanged(self):
        # calculate new statistical output for selected data
        #print "got Selection %s"%str(self.tableWidget.selectedItems())
        self.selection = Statistic(self.tableWidget.selectedItems())
        
        if len(self.tableWidget.selectedItems()) == 0:
            # nothing selected
            self.statisticOutput.setText("This is the statistical output area.\nSelect data to list its statistical properties")
        else:
            # print the output
            self.statisticOutput.setText("Statistic Output\n\n")
            self.statisticOutput.setText(self.statisticOutput.text() + "Mean Value:\t\t" + str(self.selection.getMean()) +"\n")
            self.statisticOutput.setText(self.statisticOutput.text() + "Maximum Value:\t\t" + str(self.selection.getMax()) +"\n")
            self.statisticOutput.setText(self.statisticOutput.text() + "Minimum Value:\t\t" + str(self.selection.getMin()) +"\n")
            self.statisticOutput.setText(self.statisticOutput.text() + "Sample Variance:\t\t" + str(self.selection.getVar()) +"\n")
        

class Statistic (object):
    def __init__(self, QTableWidgetItems):
        # create a list of all QTableWidgetItem values
        self.__data = []
        for item in QTableWidgetItems:
            self.__data.append(float(item.text()))
        
    def getMean(self):
        # returns the mean value of of given data list
        mean = 0;
        for i, value in enumerate(self.__data):
            mean += value
        mean /= (i+1)                                   # as i starts with 0
        return mean
        
    def getMin(self):
        # returns the minimum value of given data list
        minimum = float('inf')
        
        for value in self.__data:
            if value < minimum:
                minimum = value
        return minimum
        
    def getMax(self):
        # returns the maximum value of given data list
        maximum = -float('inf')
        
        for value in self.__data:
            if value > maximum:
                maximum = value
        return maximum
        
    def length(self):
        #returns the number n of elements
        return len(self.__data)
        
    def getSum(self):
        # returns the sum of all values in data
        sum = 0
        for value in self.__data:
            sum += value
        return sum
        
    def getVar(self):
        # returns the variance of given values in data, using sample variance
        mean = self.getMean()
        sq = 0
        for value in self.__data:
            sq += math.pow((value - mean), 2)
        try:
            res = float(sq) * float(1.0/(float(self.length()) - 1.0))
        except ZeroDivisionError:
            res = 0             # as n = 1
        return res
