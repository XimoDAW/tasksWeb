from abc import ABCMeta, abstractmethod
import sys

class PositService(metaclass=ABCMeta):
    @abstractmethod
    def getAll():
        pass

    @abstractmethod
    def getById(self, id):
        pass

print(sys.path)