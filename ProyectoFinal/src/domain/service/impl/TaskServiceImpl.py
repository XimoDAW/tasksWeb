from datetime import datetime
import sys

sys.path.append('c:\\tasksWeb\\ProyectoFinal\\src\\domain\\service')
import TaskService

sys.path.append('c:\\tasksWeb\\ProyectoFinal\\src\\persistance\\repositoryImpl')
import TaskRepositoryImpl

sys.path.append('c:\\tasksWeb\\ProyectoFinal\\src\\persistance\\repositoryImpl')
import ManagementRepositoryImpl

sys.path.append('c:\\tasksWeb\\ProyectoFinal\\src\\persistance\\repositoryImpl')
import PositRepositoryImpl

sys.path.append('c:\\tasksWeb\\ProyectoFinal\\src\\http_errors')
import ResourceNotFoundException

taskRepository = TaskRepositoryImpl.TaskRepositoryImpl()

positRepository = PositRepositoryImpl.PositRepositoryImpl()

managementRepository = ManagementRepositoryImpl.ManagementRepositoryImpl()


class TaskServiceImpl(TaskService.TaskService):
    def getAll(self):
        return taskRepository.getAll()
    

    def getById(self, id):
        task = taskRepository.getById(id)

        if (task is None):
            raise ResourceNotFoundException.ResourceNotFoundException('ERROR(404): No se encuentra la tarea')
        
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
    
    def deleteTask(self, id):
        return taskRepository.deleteTask(id)