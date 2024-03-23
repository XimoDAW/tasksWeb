import sys

sys.path.append('c:\\tasksWeb\\ProyectoFinal\\src\\persistance\\dao') 
import ManagementDAO

sys.path.append('c:\\tasksWeb\\ProyectoFinal\\src\\domain\\repository')
import ManagementRepository

sys.path.append('c:\\tasksWeb\\ProyectoFinal\\src\\mapper') 
import ManagementMapper

managementDAO = ManagementDAO.ManagementDAO()

class ManagementRepositoryImpl (ManagementRepository.ManagementRepository):

    def getById(self, id):
        managementEntity = managementDAO.getById(id)
        if (managementEntity is None):
            return None
            
        management = ManagementMapper.toManagement(managementEntity)
        return management 