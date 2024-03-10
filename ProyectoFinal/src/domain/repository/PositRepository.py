from abc import ABCMeta, abstractmethod

class PositRepository(metaclass=ABCMeta):
    @abstractmethod
    def getAll():
        pass

    @abstractmethod
    def getById(self, id):
        pass
