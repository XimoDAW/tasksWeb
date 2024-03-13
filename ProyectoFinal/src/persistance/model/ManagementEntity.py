class ManagementEntity:
    __id = 0
    def __init__(self, id):
        self.__id = id

    def getId(self):
        return self.__id
    
    def setId(self, id):
        self.__id = id