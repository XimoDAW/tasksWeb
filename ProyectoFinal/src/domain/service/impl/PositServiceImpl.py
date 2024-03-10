import sys

sys.path.append('c:\\tasksWeb\\ProyectoFinal\\src\\domain\\service')
import PositService

sys.path.append('c:\\tasksWeb\\ProyectoFinal\\src\\persistance\\repositoryImpl')
import PositRepositoryImpl

class PositServiceImpl(PositService.PositService):
    def getAll(self):
        positRepository = PositRepositoryImpl.PositRepositoryImpl()
        return positRepository.getAll()
    
    def getById(self, id):
        pass