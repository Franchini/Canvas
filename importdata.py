import sys,  os, re
from PyQt4 import QtGui, QtCore
from datetime import datetime,  timedelta
from ui.Ui_import import Ui_ImportDialog as ImDlg
import data as dataObject

class ImportWindow(QtGui.QDialog, ImDlg):
    def __init__(self, parent=0):
        
        QtGui.QDialog.__init__(self)
        self.setupUi(self)
        #number of the opened columns is set to 1 as a default
        self.columns = 1
        #the existing fileds are ordered in an array
        self.sensorType = {}
        self.sensorName = {}
        self.sensorDepth = {}
        self.sensorType[0] = self.sensorType0
        self.sensorDepth[0] = self.sensorDepth0
        self.sensorName[0] = self.sensorName0
        self.depths =[]
        self.parent = parent
        
        #some default option values:
        self.__loadProperties()
       
        #set slots
        self.connect(self.buttonCancel, QtCore.SIGNAL("clicked()"), self.onCancel)
        self.connect(self.buttonSearch,  QtCore.SIGNAL("clicked()"), self.__onSearch)
        self.connect(self.buttonImport, QtCore.SIGNAL("clicked()"),  self.__onImport)
        self.connect(self.sensorType0,  QtCore.SIGNAL("currentIndexChanged(QString)"), self.__onTypeChanged)
       
    def __checkField(self, textbox):
        # will check the given textbox for a valid value (integer) and return TRUE in case QLineEdit
        # text was a integer and FALSE in case the text was not a Number, 0, or negative
        check = textbox.text()
        if (check == "d"):
            return 2
        try:
            #field could be a date field
            value = int(check)            
            if (value > 0):
                return 1
            else:
                return 0
        except ValueError:
            return 0
       
    def __onImport(self):
        #the specified datafields have to be loaded, but only if the depth field is valid
        
        #create an array of the fileds to be loaded
        loadType = []
        self.importdata = []
        self.dateArray = []
        for i in range(self.columns):
            loadType.append(self.__checkField(self.sensorDepth[i]))
            
        #open file again
        try:
            file = open(self.openfilename,  "r")
            select = 1
        except:
            #no file was selected
            select = 0
        if select == 1:
            for line in file:
                # check if line is a dataline
                if line.find(self.separationChar) == -1:
                    pass
                else:
                    line = line.strip()
                    # if separation char is not "," it can be replaced by "."
                    if self.separationChar != ",":
                        line = line.replace(",", ".")
                    cells = line.split(self.separationChar)
                    data = []
                    #order the read data according to its type
                    for i,  type in enumerate(loadType):
                        if type == 1:
                            # cast cell into float
                            try:
                                cells[i] = float(cells[i])
                                #cell at this index contains needed data, so append to temporary data-list
                                data.append(cells[i])
                            except:
                                pass
                        elif type == 2:
                            #cell at this index is the date itself
                            date = cells[i]
                    
                    #the cells are read, so append to self.importdata
                    if len(data) > 0:
                        self.importdata.append(data)
                    try:
                        self.dateArray.append(date)
                        
                    except:
                        #in this case no date data was loaded and exception is ignored
                        pass
            file.close()
            self.depths = self.__createDepths(loadType, self.sensorDepth)
            self.timestep = self.__createTimestep(self.dateArray)
            try:
                self.startdate = datetime.strptime(self.dateArray[0], self.dateFormat)
            except:
                try:
                    self.startdate = datetime.strptime(self.dateArray[1], self.dateFormat)
                except:
                    self.parent.errorlog.writeError("Could not create Startdate, becahuse dateFormat was invalid")
                    self.startdate = None
            if self.parent != 0:
                self.parent.Data = self.exportDataObject()
                self.parent.logfile.writeLog("ImportWindow created DataObject from file "+self.openfilename+"\n" +
                    "containing: "+str(self.parent.Data.getMeasuringPoints())+" Datapoints")
            else:
                print "Import Window has no callable parent object"
            # close the import Window
            self.close()
        else:
            # sa no file was selected, or the filename was not valid, start openfiledialog
            self.__onSearch()
        
    def onCancel(self):
        self.close()
        
    def __onSearch(self):
        #This function will open a OpenFiledialog and give the filename to textbox 'filename'.
        #The number of columns is read and given to lblColumns
        #As the number of opened columns is bigger than 1 new QWidgets to label the data is 
        #added to the ImportWindow
        try:
            self.openfilename = QtGui.QFileDialog.getOpenFileName(self, 'Open file', os.getcwd())
            self.filename.setText(self.openfilename)
        except:
            #no file was selected
            pass

        #open the file and read the first line
        try:
            file = open(self.openfilename,  "r")
            line = file.readline()
            
            #strip and split line to recieve number of columns
            while line.find(self.separationChar) == -1:
                #this is no dataline
                line = file.readline()
            line.strip()
            cells = line.split(self.separationChar)
            file.close()
            
            if len(cells) > 1:
                self.columns = len(cells)
            self.lblColumns.setText(str(self.columns)+" datasets have been found")
        except:
            if self.parent != 0:
                self.parent.errorlog.writeError("The file " + self.openfilename + "doesn't exist or is not readable.")
            else:
                print "The selected file doesn't exist or is not readable."
        
        
        #to specify the datasets the input fields must be ceated
        try:
            if self.columns > 1:
                self.__createFields(self.columns,  cells)
            self.sensorName0.setText(cells[0])
        except:
            #no file was selected
            pass
     
    def __createFields(self,  columns, names={}):
        #as there is more than 1 dataset in the loaded file, the input fields for the
        #other datasets are created. The number of datasets is given as 'columns'.
        for i in range(1, self.columns ):
            # set the seonsor
            self.sensorType[i] = QtGui.QComboBox(self.scrollAreaWidgetContents)
            self.sensorType[i].setGeometry(QtCore.QRect(280,  30+(40*i),  141,  22))
            self.sensorType[i].setEditable(False)
            self.sensorType[i].setObjectName("sensorType"+str(i))
            self.sensorType[i].addItem("Soil Moisture [Vol/Vol]")
            self.sensorType[i].addItem( "Matrix Potential [kPa]")
            self.sensorType[i].addItem("Date [XXXX]")
            self.connect(self.sensorType[i], QtCore.SIGNAL("currentIndexChanged(QString)"),  self.__onTypeChanged)
            self.sensorType[i].show()
            
            #set the sensorDepth
            self.sensorDepth[i] = QtGui.QLineEdit(self.scrollAreaWidgetContents)
            self.sensorDepth[i].setGeometry(QtCore.QRect(120, 30+(40*i), 111, 20))
            self.sensorDepth[i].setObjectName("sensorDepth"+str(i))
            self.sensorDepth[i].show()
            
            #set the sensorName
            self.sensorName[i] = QtGui.QLabel(self.scrollAreaWidgetContents)
            self.sensorName[i].setGeometry(QtCore.QRect(20, 30+(40*i), 111, 12))
            self.sensorName[i].setObjectName("sensorName"+str(i))
            self.sensorName[i].setText(names[i])
            self.sensorName[i].show()
     
    def __onTypeChanged(self):
        # any of the sensorType Comboboxes was changed. The selected value has to be checked for
        # date values

        #get index of object using regular expressions
        for type in self.sensorType:
            name = self.sensorType[type].objectName()
            c = re.search(r"[0-9]+",  name)
            i = int(c.group(0))
            if self.sensorType[type].currentText() == "Date [XXXX]":
                self.sensorDepth[i].setText("d")
                self.sensorDepth[i].setEnabled(False)
            else:
                #no date was selected
                self.sensorDepth[i].setEnabled(True)
                self.sensorDepth[i].setText("")
            
    def exportDataObject(self):
        #this function will export the imported data as a Data object.
        exportObject = dataObject.Data(self.importdata, self.depths, self.timestep, "imported station", self.startdate)
        return exportObject
        
    def __createDepths(self, loadType,  sensorDepth):
        # an Array including the Depths is created
        depth = []
        for i,  type in enumerate(loadType):
            if type == 1:
                if self.negativeDepths == 0:
                    depth.append(0 - int(sensorDepth[i].text()))
                else:
                    depth.append(int(sensorDepth[i].text()))
        return depth
        
    def __createTimestep(self,  date):
        #will create the timedelta in Seconds from the date array
        start = date[1]
        starttime = datetime.strptime(start,  self.dateFormat)
        second = date[2]
        secondtime = datetime.strptime(second,  self.dateFormat)
        #compute delta of first and second timeobject and save the absolute second value
        delta = abs(starttime-secondtime).total_seconds()
        return delta
        
    def __loadProperties(self):
        # will load properties from parent object, if not possible
        # load some default values
        try:
            self.separationChar = self.parent.properties.getValue('separationchar')
        except:
            self.separationChar = ";"
        try:
            self.dateFormat = self.parent.properties.getValue('dateformat')
        except:
            self.dateFormat = "%y/%m/%d"
        try:
            self.negativeDepths = self.parent.properties.getValue('negativedepths')
        except:
            self.negativeDepths = "0"
        
        
#for development reasons
#app = QtGui.QApplication(sys.argv)
#dialog = ImportWindow()
#dialog.show()
#sys.exit(app.exec_())
