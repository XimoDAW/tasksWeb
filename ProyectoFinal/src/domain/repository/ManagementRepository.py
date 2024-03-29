from abc import ABCMeta, abstractmethod

class ManagementRepository(metaclass=ABCMeta):

    @abstractmethod
    def getAll(self, managementId):
        pass
    
    @abstractmethod
    def getByUserAndPassword(self, user, password):
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