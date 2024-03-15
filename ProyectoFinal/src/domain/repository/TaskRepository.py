from abc import ABCMeta, abstractmethod

class TaskRepository(metaclass=ABCMeta):
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
    def insertTask(self, task):
        pass