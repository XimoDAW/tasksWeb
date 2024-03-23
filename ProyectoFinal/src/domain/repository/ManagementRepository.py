from abc import ABCMeta, abstractmethod

class ManagementRepository(metaclass=ABCMeta):

    @abstractmethod
    def getById(self, id):
        pass