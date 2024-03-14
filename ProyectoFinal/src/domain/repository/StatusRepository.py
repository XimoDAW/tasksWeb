from abc import ABCMeta, abstractmethod

class StatusRepository(metaclass=ABCMeta):
    @abstractmethod
    def getById(self, id):
        pass