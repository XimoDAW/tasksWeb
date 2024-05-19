import sys

sys.path.append('c:\\tasksWeb\\taskBack\\src\\domain\\service')
import ManagementService

sys.path.append('c:\\tasksWeb\\taskBack\\src\\persistance\\repositoryImpl')
import ManagementRepositoryImpl

sys.path.append('c:\\tasksWeb\\taskBack\\src\\http_errors')
import ResourceNotFoundException

from werkzeug.security import generate_password_hash, check_password_hash

managementRepository = ManagementRepositoryImpl.ManagementRepositoryImpl()

class ManagementServiceImpl(ManagementService.ManagementService):
    def getAll(self):
        return managementRepository.getAll()
    
    def getByUser(self, user, password):
        management = managementRepository.getByUser(user)

        if (management is None):
            raise ResourceNotFoundException.ResourceNotFoundException('ERROR(404): El usuario no está disponible')
        
        hashPassword = check_password_hash(management.getPassword() , password)
        hashPassword = not hashPassword
        
        if (hashPassword):
            raise ResourceNotFoundException.ResourceNotFoundException('ERROR: La contraseña está mal')

        return management
    
    def getById(self, id):
        management = managementRepository.getById(id)

        if (management is None):
            raise ResourceNotFoundException.ResourceNotFoundException('ERROR(404): No se encuentra el gestor')

        return management
    
    def deleteManagement(self, id):
        return managementRepository.deleteManagement(id)
    
    def insertManagement(self, management):
        newManagement = managementRepository.getByUser(management.getUser())

        if (newManagement is not None):
            raise ResourceNotFoundException.ResourceNotFoundException('ERROR: El usuario ya existe')

        hashPassowrd = generate_password_hash(management.getPassword())
        management.setPassword(hashPassowrd)
        return managementRepository.insertManagement(management)