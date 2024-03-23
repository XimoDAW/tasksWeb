class Posit:
    __id = 0
    __name = ''

    def __init__(self, id, name):
        self.__id = id
        self.__name = name

    def getId(self):
        return self.__id
    
    def setId(self, id):
        self.__id = id

    def getName(self):
        return self.__name
    
    def setName(self, name):
        self.__name = name