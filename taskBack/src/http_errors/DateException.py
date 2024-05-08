class DateException (Exception):
    __message = ''
    def __init__(self, message):
        self.__message = message
    
    def getMessage(self):
        return self.__message