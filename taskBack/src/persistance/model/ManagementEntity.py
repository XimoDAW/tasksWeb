class ManagementEntity:
    __id = 0
    __user = ''
    __password = ''

    def __init__(self, id, user, password):
        self.__id = id
        self.__user = user
        self.__password = password

    def getId(self):
        return self.__id
    
    def setId(self, id):
        self.__id = id

    def getUser(self):
        return self.__user
    
    def setUser(self, user):
        self.__user = user

    def getPassword(self):
        return self.__password
    
    def setPassword(self, password):
        self.__password = password