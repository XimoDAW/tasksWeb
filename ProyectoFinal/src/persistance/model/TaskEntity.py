from PositEntity import PositEntity
from ManagementEntity import ManagementEntity

class TaskEntity:
    __id = 0
    __name = ''
    __description = ''
    __positEntity = PositEntity(0, '', 0)
    __managementEntity = ManagementEntity(0, '', '')
    __startDate = ''
    __endDate = ''
    __status = True
    
    def __init__(self, id, name, description, positEntity, managementEntity, startDate, endDate, status):
        self.__id = id
        self.__name = name
        self.__description = description
        self.__positEntity = positEntity
        self.__managementEntity = managementEntity
        self.__startDate = startDate
        self.__endDate = endDate
        self.__status = status

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

    def getPositEntity(self):
        return self.__positEntity
    
    def setPositEntity(self, positEntity):
        self.__positEntity = positEntity

    def getManagementEntity(self):
        return self.__managementEntity
    
    def setManagementEntity(self, managementEntity):
        self.__managementEntity = managementEntity

    def getStartDate(self):
        return self.__startDate
    
    def setStartDate(self, startDate):
        self.__startDate = startDate

    def getEndDate(self):
        return self.__endDate
    
    def setEndDate(self, endDate):
        self.__endDate = endDate

    def getStatus(self):
        return self.__status
    
    def setStatus(self, status):
        self.__status = status