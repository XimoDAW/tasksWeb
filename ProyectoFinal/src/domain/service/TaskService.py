from abc import ABCMeta, abstractmethod

class TaskService(metaclass=ABCMeta):
    @abstractmethod
    def getAll():
        pass

    @abstractmethod
    def getById(self, id):
        pass

    #@abstractmethod
    #def deletePosit(self, id):
        #pass

    #@abstractmethod
    #def insertPosit(self, posit):
        #pass