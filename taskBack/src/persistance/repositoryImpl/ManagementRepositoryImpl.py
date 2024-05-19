import sys

sys.path.append('c:\\tasksWeb\\taskBack\\src\\persistance\\dao') 
import ManagementDAO

sys.path.append('c:\\tasksWeb\\taskBack\\src\\domain\\repository')
import ManagementRepository

sys.path.append('c:\\tasksWeb\\taskBack\\src\\mapper') 
import ManagementMapper

managementDAO = ManagementDAO.ManagementDAO()

class ManagementRepositoryImpl (ManagementRepository.ManagementRepository):

    def getAll(self):
        managementList = list()
        managementEntityList = managementDAO.getAll()

        for managementEntity in managementEntityList:
            managementList.append(ManagementMapper.toManagement(managementEntity))
        return managementList

    def getByUser(self, user):
        managementEntity = managementDAO.getByUser(user)
        if (managementEntity is None):
            return None
            
        management = ManagementMapper.toManagement(managementEntity)
        return management

    def getById(self, id):
        managementEntity = managementDAO.getById(id)
        if (managementEntity is None):
            return None
            
        management = ManagementMapper.toManagement(managementEntity)
        return management 
    
    def deleteManagement(self, id):
        return managementDAO.deleteManagement(id)
    
    def insertManagement(self, management):
        managementEntity = ManagementMapper.toManagementEntity(management)
        return managementDAO.insertManagement(managementEntity)