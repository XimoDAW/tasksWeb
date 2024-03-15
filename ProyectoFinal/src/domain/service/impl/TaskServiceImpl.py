import sys

sys.path.append('c:\\tasksWeb\\ProyectoFinal\\src\\domain\\service')
import TaskService

sys.path.append('c:\\tasksWeb\\ProyectoFinal\\src\\persistance\\repositoryImpl')
import TaskRepositoryImpl

sys.path.append('c:\\tasksWeb\\ProyectoFinal\\src\\persistance\\repositoryImpl')
import StatusRepositoryImpl

sys.path.append('c:\\tasksWeb\\ProyectoFinal\\src\\persistance\\repositoryImpl')
import ManagementRepositoryImpl

sys.path.append('c:\\tasksWeb\\ProyectoFinal\\src\\persistance\\repositoryImpl')
import PositRepositoryImpl

sys.path.append('c:\\tasksWeb\\ProyectoFinal\\src\\http_errors')
import ResourceNotFoundException

taskRepository = TaskRepositoryImpl.TaskRepositoryImpl()

positRepository = PositRepositoryImpl.PositRepositoryImpl()

managementRepository = ManagementRepositoryImpl.ManagementRepositoryImpl()

statusRepository = StatusRepositoryImpl.StatusRepositoryImpl()

class TaskServiceImpl(TaskService.TaskService):
    def getAll(self):
        return taskRepository.getAll()
    

    def getById(self, id):
        task = taskRepository.getById(id)

        if (task is None):
            raise ResourceNotFoundException.ResourceNotFoundException('ERROR(404): No se encuentra la tarea')
        
        status = statusRepository.getStatusByTaskId(id)
        task.setStatus(status)
        return task
    
    def insertTask(self, task, positId, managementId, statusId):
        task.setPosit(positRepository.getById(positId))
        task.setManagement(managementRepository.getById(managementId))
        task.setStatus(statusRepository.getById(statusId))
        return taskRepository.insertTask(task)
    
    def deleteTask(self, id):
        return taskRepository.deleteTask(id)