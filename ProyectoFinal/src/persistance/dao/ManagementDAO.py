import sys

sys.path.append('c:\\tasksWeb\\ProyectoFinal\\src\\bd') 
import DButil

sys.path.append('c:\\tasksWeb\\ProyectoFinal\\src\\persistance\\model') 
import ManagementEntity


class ManagementDAO:
    connection = ''
    cursor = ''

    def __init__(self):
        self.connection = DButil.connect('localhost', 'root', 'root', 'tasks')

    def getById(self, id):
        cursor = DButil.open(self.connection)
        cursor.execute('select * from management where id=%s', (id))
        result = cursor.fetchone()

        if not result:
            return None
        id = result
        managementEntity = ManagementEntity.ManagementEntity(id)
        return managementEntity
        