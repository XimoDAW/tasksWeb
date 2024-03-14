import sys

sys.path.append('c:\\tasksWeb\\ProyectoFinal\\src\\domain\\service')
import TaskService

sys.path.append('c:\\tasksWeb\\ProyectoFinal\\src\\persistance\\repositoryImpl')
import TaskRepositoryImpl

sys.path.append('c:\\tasksWeb\\ProyectoFinal\\src\\persistance\\repositoryImpl')
import StatusRepositoryImpl

sys.path.append('c:\\tasksWeb\\ProyectoFinal\\src\\http_errors')
import ResourceNotFoundException

taskRepository = TaskRepositoryImpl.TaskRepositoryImpl()

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