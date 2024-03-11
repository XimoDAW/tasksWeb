import sys

sys.path.append('c:\\tasksWeb\\ProyectoFinal\\src\\bd') 
import DButil

sys.path.append('c:\\tasksWeb\\ProyectoFinal\\src\\persistance\\model') 
import PositEntity


class PositDAO:
    connection = ''
    cursor = ''

    def __init__(self):
        self.connection = DButil.connect('localhost', 'root', 'root', 'tasks')
        self.cursor = DButil.open(self.connection)
    
    def getAll(self):
        positEntityList = []
        self.cursor.execute('select * from posit')
        for id, name in self.cursor.fetchall():
            positEntity = PositEntity.PositEntity(id, name)
            positEntityList.append(positEntity)
        return positEntityList
    
    def getById(self, id):
        self.cursor.execute('select * from posit where id=%s', (id))
        id, name = self.cursor.fetchone()
        positEntity = PositEntity.PositEntity(id, name)
        return positEntity