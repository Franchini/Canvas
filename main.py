import sys, os, datetime, sqlite3
from PyQt4 import QtGui, QtCore
from ui.Ui_main import Ui_MainWindow as Dlg
import MySQLdb
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from mpl_toolkits.mplot3d import Axes3D
import table, filestream,  importdata, properties
import data as dataObject

from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import matplotlib.pyplot as plt
import numpy as np



class MainWindow (QtGui.QMainWindow, Dlg):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.setupUi(self)
        self.main_widget = QtGui.QWidget(self)
        
        
        self.layout = QtGui.QVBoxLayout(self.main_widget)

        
        self.main_widget.setFocus()
        self.setCentralWidget(self.main_widget)
        
        #set starttime of Application
        self.starttime = datetime.datetime.today()
        #open a file upstream for an ErrorLog
        self.errorlog = filestream.ErrorLog(self.starttime)
        #open a file upstream for an LogFile
        self.logfile = filestream.LogFile(self.starttime)
        
        #set data attribute to zero
        self.data = 0
        self.Data = dataObject.Data()
        #check default sqlite db and load the content
        self.__defaultdb = MyConnection(self, "sqlite", database="db/default.db", table="data")
        self.Data = self.__defaultdb.getData()
        
        #setup array for TableWindows
        self.table = []
        
        #again development only
        print (str(self.Data.getMeasuringPoints()) + " Datapoints loaded")
        
        # load all properties
        self.properties = properties.Properties()
        
        #set slots
        self.connect(self.actionExit, QtCore.SIGNAL("triggered()"), QtCore.SLOT("close()"))
        self.connect(self.actionTable_2, QtCore.SIGNAL("triggered()"), self.onTableShow)
        self.connect(self.actionSave, QtCore.SIGNAL("triggered()"), self.onSave)
        self.connect(self.actionImportFile, QtCore.SIGNAL("triggered()"), self.onImport)
        self.connect(self.actionImportConnection, QtCore.SIGNAL("triggered()"),  self.onConnect)
        self.connect(self.actionDatabaseManager, QtCore.SIGNAL("triggered()"), self.onDatabaseManager)
        self.connect(self.buttonMysql, QtCore.SIGNAL("clicked()"), self.onConnect)
        self.connect(self.buttonImport, QtCore.SIGNAL("clicked()"), self.onImport)
        self.connect(self.buttonProperties, QtCore.SIGNAL("clicked()"), self.onProperties)
        self.connect(self.buttonTable, QtCore.SIGNAL("clicked()"), self.onTableShow)
        self.connect(self.buttonExport, QtCore.SIGNAL("clicked()"), self.onExport)
        self.connect(self.buttonDatabaseManager, QtCore.SIGNAL("clicked()"),  self.onDatabaseManager)
        
        self.myplot = MyCanvas(self, self.main_widget)
        self.layout.addWidget(self.myplot)
        #self.setLayout(self.layout)


        # last command of __init__ method:
        self.logfile.writeLog("Application initialized")
        
    def closeEvent(self, event):
        # reimplementation of closeEvent to close all open filestreams properly
        # The MessageBox is commented during development
        reply = QtGui.QMessageBox.question(self,"Message","Do you want to save the current Dataset?",
            QtGui.QMessageBox.No, QtGui.QMessageBox.Yes, QtGui.QMessageBox.Cancel)
        if reply == QtGui.QMessageBox.Cancel:
            
            event.ignore()
        else:
            if reply == QtGui.QMessageBox.Yes:
                self.__defaultdb.write("data", self.Data)     
            # close all filestreams and then accept closeEvent
            err = self.errorlog.checkNoError()
            self.logfile.writeLog("\nEnding this Session;\n" +
                "Errors during this Session: "+ str(err) + "\nApplication closed")            
            self.logfile.closeLogFile()
            # check if the data should be saved
            event.accept()
        
    def onSave(self):
        # ask user if the default database should be overwritten
        reply = QtGui.QMessageBox.question(self,"Message","Do you want to save the current Dataset?",
            QtGui.QMessageBox.Yes, QtGui.QMessageBox.Cancel)
        if reply == QtGui.QMessageBox.Yes:
            self.__defaultdb.write("data", self.Data)
            self.logfile.writeLog("Dataset %s saved as default database" % self.Data.getNameStation())
        
    def onTableShow(self):
        # pops up a table form for dataview
        self.table.append(table.TableWindow(self, self.Data))
        self.table[len(self.table) - 1].show()
    
    def onConnect(self):
        # connects to a MySQL db and imports the data into self.data object
        try:
            self.Connection = MyConnection(self, "mysql", self.properties.getValue('mysqlserver'), self.properties.getValue('mysqluser'),  
                self.properties.getValue('mysqlpw'), self.properties.getValue('mysqlbase'), self.properties.getValue('mysqltable'))
        except:
            # no properties loaded
            self.Connection = MyConnection(self, "mysql")
        self.Data = self.Connection.getData()
        # only during development
        print (str(self.Data.getMeasuringPoints()) + " Datapoints loaded")
        
    def onImport(self):
        #open a ImportWindow and give self.Data as a export Object
        self.importWindow = importdata.ImportWindow(self)
        self.importWindow.exec_()
        # only during development:
        print (str(self.Data.getMeasuringPoints()) + " Datapoints loaded")
        
    def onProperties(self):
        # show the Properties Window by only using its show() method, since it's initialized yet
        self.properties.show()
        
    def onExport(self):
        # The actual DataObject is exported to the given MySQL connection
        # first ask if everything should be overrided
        reply = QtGui.QMessageBox.question(self, "Override Data", "Do you really want to override database %s"%self.properties.getValue('mysqlbase'), 
            QtGui.QMessageBox.No, QtGui.QMessageBox.Yes)
        if reply == QtGui.QMessageBox.Yes:
            try:
                self.Connection.write(self.properties.getValue('mysqltable'), self.Data)
            except AttributeError:
                # there is no Connection, so connect to MySQL database, but do not recieve data
                self.Connection = MyConnection(self, "mysql", self.properties.getValue('mysqlserver'), self.properties.getValue('mysqluser'),  
                    self.properties.getValue('mysqlpw'), self.properties.getValue('mysqlbase'), self.properties.getValue('mysqltable'))
                try:
                    self.Connection.write(self.properties.getValue('mysqltable'), self.Data)
                except AttributeError:
                    # The connection Data maybe wrong
                    pass
                    
    def onDatabaseManager(self):
        # open Database Manager to import and export to different database conenctions
       pass 
 
class MyCanvas (FigureCanvas):
    def __init__(self, parent, widget, width=5, height=4, dpi=100):
        self.figure = plt.figure()
        self.axes = self.figure.add_subplot(111, projection='3d')
        FigureCanvas.__init__(self, self.figure)
        #SizePolicy
        FigureCanvas.setSizePolicy(self,QtGui.QSizePolicy.Expanding,
            QtGui.QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)
        self.setParent(widget)
        self.parent = parent
        self.axes.mouse_init()

        
        if parent is not None:
            self.drawData(data = self.parent.Data.getAllData(), depths = self.parent.Data.getDepthsValues(mode='i'), timesteps = self.parent.Data.getNumberTimesteps(), starttime = self.parent.Data.getStartTime())
    
        
        
    
    def drawData(self, data, depths, timesteps, starttime):
        print 'drawData'
        print 'depths = ', depths, ', starttime = ', starttime, 'timesteps = ', timesteps
        timeline =  range(timesteps)
        #produces vector of the length of timesteps that works together with depths as a grid for plotting the data
        timeline, depths = np.meshgrid(timeline, depths)
        #produces the grid
        data = zip(*data)
        #transposes the datamatrix
        dataarray = np.array(data)
        self.axes.plot_surface(timeline,depths, dataarray, rstride=1, cstride=1, cmap=cm.jet, linewidth=0, antialiased=True)
        #plots the data
        self.figure.colorbar( self.axes.plot_surface(timeline,depths, dataarray, rstride=1, cstride=1, cmap=cm.jet, linewidth=1, antialiased=True))
        #adds a color-scale to the plot
        print 'drawData'
        print 'depths = ', depths, ', timeline = ', timeline
        print 'Data: ', dataarray



class MyConnection(object):
    def __init__(self, parent,  type, server='localhost', user='root', pw='root', database='python', table='datatable'):
        self.parent = parent
        self.type = type
        self.server = server
        self.user = user
        self.pw = pw
        self.database = database
        self.table = table
        # connect to db and import the data into own data attribute
        self.data = self.__read(self.table)
        # read information table   
        self.info = self.__info(self.table + "info")
     
    def __read(self, table):
        # db connector (MySQLdb, sqlite3) is used to connect and the table is read
        try:
            if self.type == "mysql":
                self.__conn = MySQLdb.connect(self.server, self.user, self.pw, self.database)
                self.parent.logfile.writeLog("MySQL Connection established at:\nServer:  " +
                    "%s\nUser:  %s\nPassword:  %s\nDatabase:  %s\nTable:  %s" % (self.server, self.user, self.pw, self.database, table))
            elif self.type == "sqlite":
                self.__conn = sqlite3.connect(self.database)
                self.parent.logfile.writeLog("SQLite Connection established at %s\n Table %s was read" % (self.database, table))
            self.__reader = self.__conn.cursor()
            self.__reader.execute("Select * from " + table)
            content = self.__reader.fetchall()
            self.__conn.close()
            return content
        except MySQLdb.Error, e:
            self.parent.errorlog.writeError("MySQL Error occured:\n%s" %e.message)
        except  sqlite3.Error, e:
            self.parent.errorlog.writeError("SQLite Error occured: \n%s" % e.message)
     
    def write(self, table, DataObject):
        # will use the db connectors (MySQLdb, sqlite3) to write new values into existing tables
        # connection has to be established again, because it was closed after reading it.
        
        try:
            if self.type == "mysql":
                self.__conn = MySQLdb.connect(self.server, self.user, self.pw, self.database)
            elif self.type == "sqlite":
                self.__conn = sqlite3.connect(self.database)
            self.__reader = self.__conn.cursor()
            # create content
            values = self.__queryData(self.__reader, table, DataObject)
            self.__conn.commit()
            self.__queryInfo(self.__reader, table+"info", DataObject)
            self.__conn.commit()
            self.__conn.close()
            self.parent.logfile.writeLog("%s Datapoints have been saed to %s" %(values, self.database))
            return 1
        except MySQLdb.Error, e:
            self.parent.errorlog.writeError("MySQL Error occured:\n%s" %e.message)
        except sqlite3.Error, e:
            self.parent.errorlog.writeError("SQLite Error occured: \n%s" % e.message)
        
    def __queryData(self,  cursor, table, DataObject):
        # will use the db connection cursor to write all Data in DataObject to given database
        # the number of written datasets is returned
        data = DataObject.getAllData()
        # delete whole table
        cursor.execute("DELETE FROM %s" % table)
        for i, point in enumerate(data):
            command = ("INSERT INTO %s VALUES(%s" % (table, str(i)))
            for value in point:
                command += (",%s" % str(value))
            command += ")"
            cursor.execute(command)
            value = i
        return value
        
    def __queryInfo(self, cursor, table, DataObject):
        # will use the db conncetion cursor to write all info metadata of Dataobject to table
        
        #delete whole table
        cursor.execute("DELETE FROM %s" % table)
        list = DataObject.getMeta()
        
        for i, key in enumerate(list):
            command = ("INSERT INTO %s ('id','information','value') VALUES('%s'" % (table,  str(i)))
            command += (",'%s','%s'" % (str(key), str(list[key])))
            command += ")"
            cursor.execute(command)
     
    def __info(self, table):
        # The Info table is read
        info = self.setTable(table)
        return info
        
    def getData(self):
        # returns data of self.data object as a Data Object
        # define export object
        expdata = []
        expdepths = []
        expname = ""
        exptimestep = 0
        expstartdate = None
        try:
            for point in self.data:
                # get all values from this datapoint
                expdata.append(point[1:len(point)])
        except TypeError:
            # self.data was not iterable
            self.parent.errorlog.writeError("No data was uploaded from database %s" % self.database)
        
        # Read information from information Table
        try:
            for point in self.info:
                if point[1] == "name":
                    expname = point[2]
                elif point[1] == "depths":
                    expdepths = point[2].split(",")
                elif point[1] == "timestep":
                    exptimestep = int(point[2])
                elif point[1] == "start":
                    expstartdate = datetime.datetime.strptime(point[2], "%Y/%m/%d %H:%M:%S")    # this is a fix value for db connection
        except TypeError:
            # self.info was not iterable
            self.parent.errorlog.writeError("Informationtable of %s cannot be read" % self.database)
        export = dataObject.Data(expdata, expdepths, exptimestep, expname,  expstartdate)
        return export
    
        
    def setTable(self, newtable):
        # set a new table for connection and returns the read data
        content = self.__read(newtable)
        return content
        



app = QtGui.QApplication(sys.argv)
dialog = MainWindow()
dialog.show()
sys.exit(app.exec_())
