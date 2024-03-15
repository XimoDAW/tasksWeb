import sys

from ManagementDAO import ManagementDAO
from PositDAO import PositDAO
from StatusDAO import StatusDAO

from datetime import datetime

sys.path.append('c:\\tasksWeb\\ProyectoFinal\\src\\bd') 
import DButil

sys.path.append('c:\\tasksWeb\\ProyectoFinal\\src\\persistance\\model') 
import TaskEntity

statusDAO = StatusDAO()
positDAO = PositDAO()
managementDAO = ManagementDAO()

class TaskDAO:
    connection = ''
    cursor = ''

    def __init__(self):
        self.connection = DButil.connect('localhost', 'root', 'root', 'tasks')
        
    def getAll(self):
        cursor = DButil.open(self.connection)
        taskEntityList = []
        cursor.execute('select * from task')
        for id, name, description, idPosit, idManagement, startDate, endDate in cursor.fetchall():
            taskEntity = TaskEntity.TaskEntity(id, name, description, positDAO.getById(idPosit), managementDAO.getById(idManagement), startDate, endDate, None)
            taskEntityList.append(taskEntity)
        return taskEntityList
    
    def getById(self, id):
        cursor = DButil.open(self.connection)
        cursor.execute('select * from task where id=%s', (id))
        result = cursor.fetchone()

        if not result:
            return None
        id, name, description, idPosit, idManagement, startDate, endDate = result
        taskEntity = TaskEntity.TaskEntity(id, name, description, positDAO.getById(idPosit), managementDAO.getById(idManagement), startDate, endDate, None)
        return taskEntity

    def insertTask(self, taskEntity, statusId):
        cursor = DButil.open(self.connection)
        cursor.execute('insert into task (name, description, id_posit, id_management, init, end) values (%s, %s, %s, %s, %s, %s)', (taskEntity.getName(), taskEntity.getDescription(), taskEntity.getPositEntity().getId(), taskEntity.getManagementEntity().getId(), datetime.strptime(taskEntity.getStartDate(), "%d-%m-%Y"), datetime.strptime(taskEntity.getEndDate(), "%d-%m-%Y")))
        self.connection.commit()
        cursor.execute('SELECT id FROM task ORDER BY id DESC LIMIT 1')
        taskId = cursor.fetchone()
        cursor.execute('insert into task_status (id_task, id_status) values (%s, %s)', (taskId, statusId))
        inserting = 'Tarea insertada correctamente'
        self.connection.commit()
        return inserting
    
    def deleteTask(self, id):
        cursor = DButil.open(self.connection)
        cursor.execute('delete from task_status where id_task=%s', (id))
        cursor.execute('delete from task where id=%s', (id))
        deleting = 'Tarea borrada con el id: ' + str(id)
        cursor.execute('alter table task AUTO_INCREMENT = 1')
        cursor.execute('alter table task_status AUTO_INCREMENT = 1')
        self.connection.commit()
        return deleting