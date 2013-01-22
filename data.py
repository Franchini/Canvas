import datetime

class Data(object):
    def __init__(self, datatable=None, depths=None,  timestep=0,  stationName="Default Station", startdate=None):
        #check the parameters for given information
        if datatable is not None:
            self.__datatable = datatable
        else:
            self.__datatable = []
        
        if depths is  not None:
            self.__measuringDepths = depths
        else:
            self.__measuringDepths = []
        
        if startdate is not None:
            #startdate has to be a datetime object
            self.__startdate = startdate
        else:
            self.__startdate = datetime.datetime.today()
        
        self.__timestep = timestep
        self.__name = stationName
        
#development
        print self.__datatable
        print self.__measuringDepths
        print self.__timestep
        print self.__startdate
        print self.getMeta()
        
        
    def getMeasuringPoints(self):
        #retuns the number of measuring points
        points = len(self.__datatable)
        return points
        
    def getAllData(self):
        # returns all dataobjects as an Array
        return self.__datatable
        
    def getNameStation(self):
        # retuns the Name of the Measurement Site
        return self.__name
        
    def getDepthsValues(self, mode='s'):
        # retuns an array of all used depths
        if mode == 's': return self.__measuringDepths
        elif mode == 'i': return [(-1)*int(depth) for depth in self.__measuringDepths]
        elif mode == 'f': return [(-1)*float(depth) for depth in self.__measuringDepths]     
            

    def getLengthTimestep(self,unit="s"):
        #returns the value of self.__timestep using given unit. Accepted values are s (Second), min (Minute), h (Hour), d (day)
        if unit == "s":
            value = self.__timestep
        elif unit == "min":
            value = self.__timestep / 60
        elif unit == "h":
            value = self.__timestep / (60*60)
        elif unit == "d":
            value = self.__timestep / (60*60*24)
        else: 
            value = 0
        return value
     
    def getNumberTimesteps(self):
        #returns the number of measuring intervals
        numberTimesteps= len(self.__datatable)
        return numberTimesteps

    def getDepth(self, depth):
        # returns all data at a certain depth
        depthIndex = 99
        for i in range(0, self.getNumberMeasuringPoints()):
            # This loop finds the index in self.__measuringDepths to a corresponding depth
            if self.__measuringDepths[i] == depth:
                    depthIndex = i
            
        if depthIndex == 99:
            #depth has no valid index
            print "This depth does not exist"
        else:
            data = length(self.__datatable)*[0]
            for i in range(0, self.getNumberTimesteps()):
                #This loop fills the varaible "data" with data of a sensor at a certain depth for all timesteps
                dataAtStep = self.__datatable[i]  #copies array of all measuring values during one timestep
                data[i] = dataAtStep[depthIndex]  #writes value of a certain depth during this timestep
        return data
        
    def getStartTime(self):
        #returns the starttime as datetime Object
        return self.__startdate
        
    def getMeta(self):
        # returns a dictionary of all Metadata, where key is the name of its value; eg: name : default station
        name = self.getNameStation()
        timestep = self.getLengthTimestep("s")
        depths = self.getDepthsValues()
        start =  self.__startdate.strftime("%Y/%m/%d %H:%M:%S")   # this is a fix value for db connection
        
        #merge depths to one string
        temp = ""
        for depth in depths:
            temp += str(depth)+","
        temp = temp.strip(",")
        list = {'name':str(name), 'timestep':str(timestep), 'depths':temp, 'start':start}
        
        return list


