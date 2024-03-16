from Posit import Posit

from Management import Management

class Task:
    __id = 0
    __name = ''
    __description = ''
    __posit = Posit(0, '')
    __management = Management(0)
    __startDate = ''
    __endDate = ''
    __status = ''
    
    def __init__(self, id, name, description, posit, management, startDate, endDate, status):
        self.__id = id
        self.__name = name
        self.__description = description
        self.__posit = posit
        self.__management = management
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

    def getPosit(self):
        return self.__posit
    
    def setPosit(self, posit):
        self.__posit = posit

    def getManagement(self):
        return self.__management
    
    def setManagement(self, management):
        self.__management = management

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