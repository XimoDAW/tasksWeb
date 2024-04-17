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
        
    def getAll(self, managementId):
        cursor = DButil.open(self.connection)
        positEntityList = []
        cursor.execute('select * from posit where id_management = %s', (managementId))
        for id, name, managementId in cursor.fetchall():
            positEntity = PositEntity.PositEntity(id, name, managementId)
            positEntityList.append(positEntity)
        return positEntityList
    
    def getById(self, id):
        cursor = DButil.open(self.connection)
        cursor.execute('select * from posit where id=%s', (id))
        result = cursor.fetchone()

        if not result:
            return None
        id, name, managementId = result
        positEntity = PositEntity.PositEntity(id, name, managementId)
        return positEntity
    
    def deletePosit(self, id):
        cursor = DButil.open(self.connection)
        cursor.execute('delete from task where id_posit=%s', (id))
        cursor.execute('delete from posit where id=%s', (id))
        deleting = 'Posit borrado con el id: ' + str(id)
        cursor.execute('alter table posit AUTO_INCREMENT = 1')
        self.connection.commit()
        return deleting
    
    def insertPosit(self, positEntity):
        cursor = DButil.open(self.connection)
        cursor.execute('insert into posit (name, id_management) values (%s, %s)', (positEntity.getName(), positEntity.getManagementId()))
        inserting = 'Posit insertado correctamente'
        self.connection.commit()
        return inserting
    
    def updatePosit(self, positEntity):
        cursor = DButil.open(self.connection)
        cursor.execute('update posit set name = %s where id = %s', (positEntity.getName(), positEntity.getId()))
        updating = 'Posit actualizado correctamente'
        self.connection.commit()
        return updating