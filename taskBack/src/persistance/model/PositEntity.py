class PositEntity:
    __id = 0
    __name = ''
    __managementId = 0

    def __init__(self, id, name, managementId):
        self.__id = id
        self.__name = name
        self.__managementId = managementId

    def getId(self):
        return self.__id
    
    def setId(self, id):
        self.__id = id

    def getName(self):
        return self.__name
    
    def setName(self, name):
        self.__name = name

    def getManagementId(self):
        return self.__managementId
    
    def setManagementId(self, managementId):
        self.__managementId = managementId