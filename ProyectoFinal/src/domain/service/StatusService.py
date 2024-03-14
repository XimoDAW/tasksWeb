from abc import ABCMeta, abstractmethod
import sys

class StatusService(metaclass=ABCMeta):

    @abstractmethod
    def getById(self, id):
        pass