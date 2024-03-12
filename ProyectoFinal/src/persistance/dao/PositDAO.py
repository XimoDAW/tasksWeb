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
        
    def getAll(self):
        cursor = DButil.open(self.connection)
        positEntityList = []
        cursor.execute('select * from posit')
        for id, name in cursor.fetchall():
            positEntity = PositEntity.PositEntity(id, name)
            positEntityList.append(positEntity)
        return positEntityList
    
    def getById(self, id):
        cursor = DButil.open(self.connection)
        cursor.execute('select * from posit where id=%s', (id))
        id, name = cursor.fetchone()
        positEntity = PositEntity.PositEntity(id, name)
        return positEntity
    
    def deletePosit(self, id):
        cursor = DButil.open(self.connection)
        cursor.execute('delete from posit where id=%s', (id))
        deleting = 'Posit borrado con el id: ' + str(id)
        self.connection.commit()
        return deleting
    
    def insertPosit(self, positEntity):
        cursor = DButil.open(self.connection)
        cursor.execute('insert into posit (name) values (%s)', (positEntity.getName()))
        inserting = 'Posit insertado correctamente'
        self.connection.commit()
        return inserting