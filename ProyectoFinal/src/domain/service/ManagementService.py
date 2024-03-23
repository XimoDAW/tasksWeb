from abc import ABCMeta, abstractmethod

class ManagementService(metaclass=ABCMeta):

    @abstractmethod
    def getById(self, id):
        pass