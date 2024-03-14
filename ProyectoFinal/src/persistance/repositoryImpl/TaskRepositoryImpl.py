import sys

sys.path.append('c:\\tasksWeb\\ProyectoFinal\\src\\domain\\repository')
import TaskRepository

sys.path.append('c:\\tasksWeb\\ProyectoFinal\\src\\persistance\\dao') 
import TaskDAO

sys.path.append('c:\\tasksWeb\\ProyectoFinal\\src\\mapper') 
import TaskMapper

sys.path.append('c:\\tasksWeb\\ProyectoFinal\\src\\http_errors')
import SQLException

sys.path.append('c:\\tasksWeb\\ProyectoFinal\\src\\http_errors')
import ResourceNotFoundException


taskDAO = TaskDAO.TaskDAO()

class TaskRepositoryImpl (TaskRepository.TaskRepository):
    def getAll(self):
        tasksList = list()
        taskEntityList = taskDAO.getAll()

        for taskEntity in taskEntityList:
            tasksList.append(TaskMapper.toTask(taskEntity))
        return tasksList

    def getById(self, id):
        taskEntity = taskDAO.getById(id)
        if (taskEntity is None):
            return None
            
        task = TaskMapper.toTask(taskEntity)
        return task 
            
    #def deletePosit(self, id):
        #return positDAO.deletePosit(id)
    
    #def insertPosit(self, posit):
        #positEntity = PositMapper.toPositEntity(posit)
        #return positDAO.insertPosit(positEntity)