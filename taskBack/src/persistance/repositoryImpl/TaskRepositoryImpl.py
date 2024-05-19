import sys

sys.path.append('c:\\tasksWeb\\taskBack\\src\\domain\\repository')
import TaskRepository

sys.path.append('c:\\tasksWeb\\taskBack\\src\\persistance\\dao') 
import TaskDAO

sys.path.append('c:\\tasksWeb\\taskBack\\src\\mapper') 
import TaskMapper

sys.path.append('c:\\tasksWeb\\taskBack\\src\\http_errors')
import SQLException

sys.path.append('c:\\tasksWeb\\taskBack\\src\\http_errors')
import ResourceNotFoundException


taskDAO = TaskDAO.TaskDAO()

class TaskRepositoryImpl (TaskRepository.TaskRepository):
    def getAll(self, positId):
        tasksList = list()
        taskEntityList = taskDAO.getAll(positId)

        for taskEntity in taskEntityList:
            tasksList.append(TaskMapper.toTask(taskEntity))
        return tasksList

    def getById(self, id):
        taskEntity = taskDAO.getById(id)
        if (taskEntity is None):
            return None
            
        task = TaskMapper.toTask(taskEntity)
        return task 
            
    def deleteTask(self, id):
        return taskDAO.deleteTask(id)
    
    def insertTask(self, task):
        taskEntity = TaskMapper.toTaskEntity(task)
        return taskDAO.insertTask(taskEntity)
    
    def updateTask(self, task):
        taskEntity = TaskMapper.toTaskEntity(task)
        return taskDAO.updateTask(taskEntity, task.getId())
    
    def updateStatusByTaskId(self, taskId, status):
        return taskDAO.updateStatusByTaskId(taskId, status)