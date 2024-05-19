class SQLException (Exception):
    __message = 'Error en la base de datos'
    def __init__(self):
        pass
    
    def getMessage(self):
        return self.__message