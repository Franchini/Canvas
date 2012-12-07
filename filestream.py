import datetime, os, shutil

class ErrorLog(object):
    def __init__(self, starttime):
        self.starttime = starttime
        self.__openErrorStream()
        self.errors = 0
        self.errorMessage = {}
        
    def __openErrorStream(self):
        #open a file upstream for an ErrorLog
        filename = "ErrorLog_%i_%i_%i_%i_%i.txt" % (self.starttime.month,
            self.starttime.day, self.starttime.year, self.starttime.hour,self.starttime.minute)
        self.errorstream = open("errorlog/" + filename, "w+")
        self.errorstream.write("ErrorLog started at " + self.starttime.ctime() + "\n")
        #save filename for removal if no errors occured
        self.filename = filename
        
    def closeErrorStream(self):
        #closes the file upstream of its ErrorLog
        self.errorstream.close()
        
    def checkNoError(self):
        #check the actual ErrorLog for emptyness, if true delete it.
        #funtion returns 0 if no error occured or the amount of errors.
        if self.errors == 0:
            self.closeErrorStream()
            os.remove("errorlog/" + self.filename)
            return 0
        else:
            self.closeErrorStream()
            return self.errors
        
    def writeError(self, message):
        #writes message of ocuring error into errorstream as well as counting errors
        self.errorstream.write("\n" + processTime() + ":\n" + message + 
            "\n--------------------")
        self.errorMessage[self.errors] = message
        self.errors += 1
        
class LogFile(object):
    def __init__(self, starttime, writeModeOn='true'):
        #all methods of LogFile objects will only be run if writeModeOn is true
        self.starttime = starttime
        self.write = writeModeOn
        self.logs = 0
        self.openLogFile()
        
    def openLogFile(self):
        #opens a file upstream for a LogFile
        if self.write == 'true':
            filename = "LogFile_%i_%i_%i.txt" % (self.starttime.month,
                self.starttime.day, self.starttime.year)
            if os.path.isfile("log/" + filename):
                # append logs to existing todays LogFile
                self.logstream = open("log/" + filename, "a")
                self.logstream.write("\n\n\nSession started at " +
                    self.starttime.ctime() + "\n") 
            else:
                #create new LogFile
                self.logstream = open("log/" + filename, "w")
                self.logstream.write("LogFile started at " + self.starttime.ctime() +
                    "\n--------------------\n")
        
    def closeLogFile(self):
        # closes the file upstream of its LogFile
        if self.write == 'true':
            self.logstream.close()
        
    def writeLog(self, message):
        #wirtes message produced by Application into logstream and adds a timestemp
        #logs are also counted (no idea why yet)
        self.logstream.write("\n" + processTime() + ":    " + message)
        self.logs += 1


def processTime(mode=0):
    #returns a timestamp of actual Processtime as String
    #mode can specifiy the formatting of string or force the return of runtime
    #which is not implemented yet
    if mode == 0:
        now = datetime.datetime.today()
        return now.ctime()
