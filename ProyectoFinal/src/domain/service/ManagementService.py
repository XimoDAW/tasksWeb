from abc import ABCMeta, abstractmethod

class ManagementService(metaclass=ABCMeta):

    @abstractmethod
    def getAll(self):
        pass

    @abstractmethod
    def getByUser(self, user):
        pass

    @abstractmethod
    def getById(self, id):
        pass

    @abstractmethod
    def deleteManagement(self, id):
        pass

    @abstractmethod
    def insertManagement(self, management):
        pass