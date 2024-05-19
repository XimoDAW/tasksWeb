from abc import ABCMeta, abstractmethod

class PositRepository(metaclass=ABCMeta):
    @abstractmethod
    def getAll(self, managementId):
        pass

    @abstractmethod
    def getById(self, id):
        pass

    @abstractmethod
    def deletePosit(self, id):
        pass

    @abstractmethod
    def insertPosit(self, posit):
        pass

    @abstractmethod
    def updatePosit(self, posit, id):
        pass