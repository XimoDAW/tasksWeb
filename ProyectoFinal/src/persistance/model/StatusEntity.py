class StatusEntity:
    __id = 0
    __status = ''

    def __init__(self, id, status):
        self.__id = id
        self.__status = status

    def getId(self):
        return self.__id
    
    def setId(self, id):
        self.__id = id

    def getStatus(self):
        return self.__status
    
    def setStatus(self, status):
        self.__status = status