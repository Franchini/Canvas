import ConfigParser,  os,  sys
from PyQt4 import QtGui, QtCore
from ui.Ui_properties import Ui_Properties as propWindow

class Properties(QtGui.QDialog,  propWindow):
    def __init__(self):
        # this will initialize the Window and reference all needed properties
        QtGui.QDialog.__init__(self)
        self.setupUi(self)
        #setup properties
        self.__properties = {}
        self.__readAllProperties()
        self.__fillAllFields()
        
        #set slots
        self.connect(self.buttonOk, QtCore.SIGNAL("clicked()"), self.onOk)
        self.connect(self.buttonCancel, QtCore.SIGNAL("clicked()"), self.onCancel)
        #development issues
#        print self.getValue('mysqlpw')
        
    def __readAllProperties(self):
        # will read all properties from confg.ini
        try:
            self.__config = ConfigParser.ConfigParser()
            self.__config.read("confg.ini")
            self.sections = self.__config.sections()
        except:
            print "the confg.ini file cannot be found"
            self.close()
        
        try:
            for section in self.sections:
                # get all option in actual section
                options = self.__config.options(section)
        
                for option in options:
                        self.__properties[option] = self.__config.get(section, option)
                 
            #self.__config.close()
        except:
            print "The confg.ini has an invalid format"
            self.close()
        
    def getValue(self,  option):
        # will return the value of key 'option' in self.__properties
        try:
            value = self.__properties[option]
            return value
        except:
            print "The option " + option + " does not exist"
            return None
        
    def __fillAllFields(self):
        # will fill all option fields with their values
        self.separationChar.setText(self.getValue('separationchar'))
        self.dateFormat.setText(self.getValue('dateformat'))
        self.mysqlServer.setText(self.getValue('mysqlserver'))
        self.mysqlName.setText(self.getValue('mysqluser'))
        self.mysqlPw.setText(self.getValue('mysqlpw'))
        self.mysqlBase.setText(self.getValue('mysqlbase'))
        self.mysqlDatatable.setText(self.getValue('mysqltable'))
        
    def onOk(self):
        # All properties have to be written into confg.ini
        self.__writeAllProperties()
        
    def __writeAllProperties(self):
        # will write all properties from ConfigParser to the confg.ini file
        
        #create section
        sections = {'csv':{}, 'mysql':{}}
        # fill options
        sections['csv'] = {'separationchar':self.separationChar.text(), 'dateformat':self.dateFormat.text()}
        sections['mysql'] = {'mysqlserver': self.mysqlServer.text(), 'mysqluser':self.mysqlName.text(), 'mysqlpw':self.mysqlPw.text(), 
            'mysqlbase':self.mysqlBase.text(), 'mysqltable':self.mysqlDatatable.text()}
        for section in sections:
            for option in sections[section]:
                #print sections[section][option]
                self.__config.set(section, option, sections[section][option])
        self.__config.write(open("confg.ini", "w"))
        self.close()
        
    def onCancel(self):
        # close the PropertiesWindow
        self.close()
        
#app = QtGui.QApplication(sys.argv)
#dialog = Properties()
#dialog.show()
#sys.exit(app.exec_())
