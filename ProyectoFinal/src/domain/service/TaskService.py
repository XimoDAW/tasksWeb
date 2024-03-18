from abc import ABCMeta, abstractmethod

class TaskService(metaclass=ABCMeta):
    @abstractmethod
    def getAll():
        pass

    @abstractmethod
    def getById(self, id):
        pass

    @abstractmethod
    def deleteTask(self, id):
        pass

    @abstractmethod
    def insertTask(self, task, positId, managementId):
        pass

    @abstractmethod
    def updateTask(self, task, positId, managementId, id):
        pass