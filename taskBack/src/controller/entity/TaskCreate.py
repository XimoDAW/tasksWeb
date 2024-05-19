import json
from PositDetailWeb import PositDetailWeb

from ManagementDetailWeb import ManagementDetailWeb

class TaskCreate:
    __name = ''
    __description = ''
    __positId = 0
    __managementId = 0
    __startDate = ''
    __endDate = ''    
    def __init__(self, name, description, positId, managementId, startDate, endDate):
        self.__name = name
        self.__description = description
        self.__positId = positId
        self.__managementId = managementId
        self.__startDate = startDate
        self.__endDate = endDate

    def getName(self):
        return self.__name
    
    def setName(self, name):
        self.__name = name

    def getDescription(self):
        return self.__description
    
    def setDescription(self, description):
        self.__description = description

    def getPositId(self):
        return self.__positId
    
    def setPositId(self, positId):
        self.__positId = positId

    def getManagementId(self):
        return self.__managementId
    
    def setManagementId(self, managementId):
        self.__managementId = managementId

    def getStartDate(self):
        return self.__startDate
    
    def setStartDate(self, startDate):
        self.__startDate = startDate

    def getEndDate(self):
        return self.__endDate
    
    def setEndDate(self, endDate):
        self.__endDate = endDate