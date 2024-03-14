import sys

sys.path.append('c:\\tasksWeb\\ProyectoFinal\\src\\persistance\\dao') 
import StatusDAO

sys.path.append('c:\\tasksWeb\\ProyectoFinal\\src\\domain\\repository') 
import StatusRepository

sys.path.append('c:\\tasksWeb\\ProyectoFinal\\src\\mapper') 
import StatusMapper

statusDAO = StatusDAO.StatusDAO()

class StatusRepositoryImpl(StatusRepository.StatusRepository):
    def getById(self, id):
        statusEntity = statusDAO.getById(id)

        if (statusEntity is None):
            return None
        
        status = StatusMapper.toStatus(statusEntity)
        return status
    
    def getStatusByTaskId(self, id):

        statusEntity = statusDAO.getStatusByTaskId(id)

        if (statusEntity is None):
            return None
        
        status = StatusMapper.toStatus(statusEntity)
        return status