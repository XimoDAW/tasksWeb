import json

class TaskListWeb:
    __id = 0
    __name = ''
    __idManagement = 0

    def __init__(self, id, name, idManagement):
        self.__id = id
        self.__name = name
        self.__idManagement = idManagement

    def getId(self):
        return self.__id
    
    def setId(self, id):
        self.__id = id

    def getName(self):
        return self.__name
    
    def setName(self, name):
        self.__name = name

    def getManagementId(self):
        return self.__idManagement
    
    def setManagementId(self, idManagement):
        self.__idManagement = idManagement

    def getJson(self):
        
        return json.dumps(self.__dict__)