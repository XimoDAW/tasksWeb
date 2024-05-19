class PositCreate:
    __name = ''
    __managementId = 0

    def __init__(self, name, managementId):
        self.__name = name
        self.__managementId = managementId

    def getName(self):
        return self.__name
    
    def setName(self, name):
        self.__name = name

    def getManagementId(self):
        return self.__managementId
    
    def setManagementId(self, managementId):
        self.__managementId = managementId