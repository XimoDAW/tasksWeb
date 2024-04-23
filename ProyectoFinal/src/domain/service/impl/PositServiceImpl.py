import sys

sys.path.append('c:\\tasksWeb\\ProyectoFinal\\src\\domain\\service')
import PositService

sys.path.append('c:\\tasksWeb\\ProyectoFinal\\src\\persistance\\repositoryImpl')
import PositRepositoryImpl

sys.path.append('c:\\tasksWeb\\ProyectoFinal\\src\\http_errors')
import ResourceNotFoundException


positRepository = PositRepositoryImpl.PositRepositoryImpl()

class PositServiceImpl(PositService.PositService):
    def getAll(self, managementId):
        return positRepository.getAll(managementId)
    
    def getById(self, id):
        posit = positRepository.getById(id)

        if (posit is None):
            raise ResourceNotFoundException.ResourceNotFoundException('ERROR(404): No se encuentra el posit con ese id')

        return posit
    
    def deletePosit(self, id):
        return positRepository.deletePosit(id)
    
    def insertPosit(self, posit):
        return positRepository.insertPosit(posit)
    
    def updatePosit(self, posit, id):
        return positRepository.updatePosit(posit, id)