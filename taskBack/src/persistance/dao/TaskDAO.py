import os
import sys

from ManagementDAO import ManagementDAO
from PositDAO import PositDAO

from datetime import datetime

sys.path.append('c:\\tasksWeb\\taskBack\\src\\bd') 
import DButil

sys.path.append('c:\\tasksWeb\\taskBack\\src\\persistance\\model') 
import TaskEntity

positDAO = PositDAO()
managementDAO = ManagementDAO()

class TaskDAO:
    connection = ''
    cursor = ''

    def __init__(self):
        self.connection = DButil.connect('localhost', 'root', 'root', 'tasks')
        
    def getAll(self, positId):
        cursor = DButil.open(self.connection)
        taskEntityList = []
        cursor.execute('select * from task where id_posit = %s', (positId))
        for id, name, description, idPosit, idManagement, startDate, endDate, status in cursor.fetchall():
            taskEntity = TaskEntity.TaskEntity(id, name, description, positDAO.getById(idPosit), managementDAO.getById(idManagement), startDate, endDate, status)
            taskEntityList.append(taskEntity)
        return taskEntityList
    
    def getById(self, id):
        cursor = DButil.open(self.connection)
        cursor.execute('select * from task where id=%s', (id))
        result = cursor.fetchone()

        if not result:
            return None
        id, name, description, idPosit, idManagement, startDate, endDate, status = result
        taskEntity = TaskEntity.TaskEntity(id, name, description, positDAO.getById(idPosit), managementDAO.getById(idManagement), startDate, endDate, status)
        return taskEntity

    def insertTask(self, taskEntity):
        cursor = DButil.open(self.connection)
        cursor.execute('insert into task (name, description, id_posit, id_management, init, end, status) values (%s, %s, %s, %s, %s, %s, %s)', (taskEntity.getName(), taskEntity.getDescription(), taskEntity.getPositEntity().getId(), taskEntity.getManagementEntity().getId(), datetime.strptime(taskEntity.getStartDate(), "%d-%m-%Y"), datetime.strptime(taskEntity.getEndDate(), "%d-%m-%Y"), taskEntity.getStatus()))
        inserting = 'Tarea insertada correctamente'
        self.connection.commit()
        pid = os.getpid()
        print(f"Reiniciando servidor Flask. Terminando proceso con PID {pid}.")
    
        python = sys.executable
        os.execv(python, [python] + sys.argv)        
        return inserting
    
    def updateTask(self, taskEntity, taskId):
        cursor = DButil.open(self.connection)
        cursor.execute('update task set name=%s, description=%s, id_posit=%s, id_management=%s, init=%s, end=%s where id = %s',(taskEntity.getName(), taskEntity.getDescription(), taskEntity.getPositEntity().getId(), taskEntity.getManagementEntity().getId(), datetime.strptime(taskEntity.getStartDate(), "%d-%m-%Y"), datetime.strptime(taskEntity.getEndDate(), "%d-%m-%Y"), taskId))
        updating = 'Tarea actualizada correctamente'
        self.connection.commit()
        return updating
    
    def updateStatusByTaskId(self, taskId, status):
        cursor = DButil.open(self.connection)
        cursor.execute('update task set status = %s where id = %s', (status, taskId))
        self.connection.commit()
    
    def deleteTask(self, id):
        cursor = DButil.open(self.connection)
        print('Tarea con id: '+ str(id))
        cursor.execute('delete from task where id=%s', (id))
        cursor.execute('alter table task AUTO_INCREMENT = 1')
        self.connection.commit()
        deleting = 'Tarea borrada con el id: ' + str(id)
        return deleting