import sys

sys.path.append('c:\\tasksWeb\\ProyectoFinal\\src\\domain\\service')
import PositService

sys.path.append('c:\\tasksWeb\\ProyectoFinal\\src\\persistance\\repositoryImpl')
import PositRepositoryImpl

positRepository = PositRepositoryImpl.PositRepositoryImpl()

class PositServiceImpl(PositService.PositService):
    def getAll(self):
        return positRepository.getAll()
    
    def getById(self, id):
        return positRepository.getById(id)