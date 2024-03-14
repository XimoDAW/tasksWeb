import sys

sys.path.append('c:\\tasksWeb\\ProyectoFinal\\src\\domain\\service')
import StatusService

sys.path.append('c:\\tasksWeb\\ProyectoFinal\\src\\persistance\\repositoryImpl')
import StatusRepositoryImpl

sys.path.append('c:\\tasksWeb\\ProyectoFinal\\src\\http_errors')
import ResourceNotFoundException

statusRepository = StatusRepositoryImpl.StatusRepositoryImpl()

class StatusServiceImpl(StatusService.StatusService):
    
    def getById(self, id):
        status = statusRepository.getById(id)

        if (status is None):
            raise ResourceNotFoundException.ResourceNotFoundException('ERROR(404): No se encuentra el estado de la tarea')

        return status