import json

class ManagementDetailWeb:
    __id = 0

    def __init__(self, id):
        self.__id = id

    def getId(self):
        return self.__id
    
    def setId(self, id):
        self.__id = id

    def getJson(self):
        return json.dumps(self.__dict__)