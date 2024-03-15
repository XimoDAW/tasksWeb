import json
from PositDetailWeb import PositDetailWeb

from ManagementDetailWeb import ManagementDetailWeb

class TaskDetailWeb:
    __id = 0
    __name = ''
    __description = ''
    __positDetailWeb = PositDetailWeb(0, '')
    __managementDetailWeb = ManagementDetailWeb(0)
    __statusDetailWeb = ''
    __startDate = ''
    __endDate = ''
    
    def __init__(self, id, name, description, positDetailWeb, managementDetailWeb, startDate, endDate, statusDetailWeb):
        self.__id = id
        self.__name = name
        self.__description = description
        self.__positDetailWeb = positDetailWeb
        self.__managementDetailWeb = managementDetailWeb
        self.__startDate = startDate
        self.__endDate = endDate
        self.__statusDetailWeb = statusDetailWeb

    def getId(self):
        return self.__id
    
    def setId(self, id):
        self.__id = id

    def getName(self):
        return self.__name
    
    def setName(self, name):
        self.__name = name

    def getDescription(self):
        return self.__description
    
    def setDescription(self, description):
        self.__description = description

    def getPositDetailWeb(self):
        return self.__positDetailWeb
    
    def setPositDetailWeb(self, positDetailWeb):
        self.__positDetailWeb = positDetailWeb

    def getManagementDetailWeb(self):
        return self.__managementDetailWeb
    
    def setManagementDetailWeb(self, managementDetailWeb):
        self.__managementDetailWeb = managementDetailWeb

    def getStartDate(self):
        return self.__startDate
    
    def setStartDate(self, startDate):
        self.__startDate = startDate

    def getEndDate(self):
        return self.__endDate
    
    def setEndDate(self, endDate):
        self.__endDate = endDate

    def getStatusDetailWeb(self):
        return self.__statusDetailWeb
    
    def setStatusDetailWeb(self, statusDetailWeb):
        self.__statusDetailWeb = statusDetailWeb

    def getJson(self):
        #Para pasar a JSON, tengo que pasar sus atributos, ya que no puede convertirlos a JSON todo junto
        
        self.__positDetailWeb = json.dumps(self.__positDetailWeb.__dict__)
        self.__managementDetailWeb = json.dumps(self.__managementDetailWeb.__dict__)
        self.__startDate = json.dumps(str(self.__startDate))
        self.__endDate = json.dumps(str(self.__endDate))

        return json.dumps(self.__dict__)