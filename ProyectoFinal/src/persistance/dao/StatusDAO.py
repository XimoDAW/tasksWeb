import sys

sys.path.append('c:\\tasksWeb\\ProyectoFinal\\src\\bd') 
import DButil

sys.path.append('c:\\tasksWeb\\ProyectoFinal\\src\\persistance\\model') 
import StatusEntity

class StatusDAO:
    connection = ''
    cursor = ''

    def __init__(self):
        self.connection = DButil.connect('localhost', 'root', 'root', 'tasks')

    def getById(self, id):
        cursor = DButil.open(self.connection)
        cursor.execute('select * from status where id=%s', (id))
        result = cursor.fetchone()
        
        if not result:
            return None
        
        id, name = result
        statusEntity = StatusEntity.StatusEntity(id, name)
        return statusEntity
    
    def getStatusByTaskId(self, id):
        cursor = DButil.open(self.connection)
        cursor.execute('select id_status from task_status where id_task=%s', (id))
        result = cursor.fetchone()
        
        if not result:
            return None
        
        id = result
        statusEntity = StatusDAO().getById(id)
        return statusEntity