import sys

sys.path.append('c:\\tasksWeb\\ProyectoFinal\\src\\domain\\service')
import ManagementService

sys.path.append('c:\\tasksWeb\\ProyectoFinal\\src\\persistance\\repositoryImpl')
import ManagementRepositoryImpl

sys.path.append('c:\\tasksWeb\\ProyectoFinal\\src\\http_errors')
import ResourceNotFoundException

managementRepository = ManagementRepositoryImpl.ManagementRepositoryImpl()

class ManagementServiceImpl(ManagementService.ManagementService):
    
    def getById(self, id):
        management = managementRepository.getById(id)

        if (management is None):
            raise ResourceNotFoundException.ResourceNotFoundException('ERROR(404): No se encuentra el gestor')

        return management