from datetime import datetime
import sys

sys.path.append('c:\\tasksWeb\\taskBack\\src\\domain\\service')
import TaskService

sys.path.append('c:\\tasksWeb\\taskBack\\src\\persistance\\repositoryImpl')
import TaskRepositoryImpl

sys.path.append('c:\\tasksWeb\\taskBack\\src\\persistance\\repositoryImpl')
import ManagementRepositoryImpl

sys.path.append('c:\\tasksWeb\\taskBack\\src\\persistance\\repositoryImpl')
import PositRepositoryImpl

sys.path.append('c:\\tasksWeb\\taskBack\\src\\http_errors')
import ResourceNotFoundException

taskRepository = TaskRepositoryImpl.TaskRepositoryImpl()

positRepository = PositRepositoryImpl.PositRepositoryImpl()

managementRepository = ManagementRepositoryImpl.ManagementRepositoryImpl()


class TaskServiceImpl(TaskService.TaskService):
    def getAll(self, positId):
        return taskRepository.getAll(positId)

    def getById(self, id):
        task = taskRepository.getById(id)

        if (task is None):
            raise ResourceNotFoundException.ResourceNotFoundException('ERROR(404): No se encuentra la tarea')
        
        endDate= datetime.strptime(str(task.getEndDate()), "%Y-%m-%d")

        if (endDate < datetime.now()):
            taskRepository.updateStatusByTaskId(task.getId(), 0)
            task = taskRepository.getById(id)
            
        return task
    
    def insertTask(self, task, positId, managementId):
        task.setPosit(positRepository.getById(positId))
        task.setManagement(managementRepository.getById(managementId))
        startDate= datetime.strptime(task.getStartDate(), "%d-%m-%Y")
        endDate= datetime.strptime(task.getEndDate(), "%d-%m-%Y")

        if (endDate > datetime.now()):
            task.setStatus(True)
        else:
            task.setStatus(False)
        return taskRepository.insertTask(task)
    
    def updateTask(self, task, positId, managementId, id):
        task.setId(id)
        task.setPosit(positRepository.getById(positId))
        task.setManagement(managementRepository.getById(managementId))
        startDate= datetime.strptime(task.getStartDate(), "%d-%m-%Y")
        endDate= datetime.strptime(task.getEndDate(), "%d-%m-%Y")

        if (endDate > datetime.now()):
            task.setStatus(True)
        else:
            task.setStatus(False)
        return taskRepository.updateTask(task)
    
    def deleteTask(self, id):
        return taskRepository.deleteTask(id)