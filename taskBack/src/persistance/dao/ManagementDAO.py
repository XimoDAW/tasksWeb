import sys

sys.path.append('c:\\tasksWeb\\taskBack\\src\\bd') 
import DButil

sys.path.append('c:\\tasksWeb\\taskBack\\src\\persistance\\model') 
import ManagementEntity


class ManagementDAO:
    connection = ''
    cursor = ''

    def __init__(self):
        self.connection = DButil.connect('localhost', 'root', 'root', 'tasks')

    def getAll(self):
        cursor = DButil.open(self.connection)
        managementEntityList = []
        cursor.execute('select * from management')
        for id, user, password in cursor.fetchall():
            managementEntity = ManagementEntity.ManagementEntity(id, user, password)
            managementEntityList.append(managementEntity)
        return managementEntityList

    def getByUser(self, user):
        cursor = DButil.open(self.connection)
        cursor.execute('select * from management where usr = %s', (user))
        result = cursor.fetchone()
        if not result:
            return None
        id, user, password = result
        managementEntity = ManagementEntity.ManagementEntity(id, user, password)
        return managementEntity

    def getById(self, id):
        cursor = DButil.open(self.connection)
        cursor.execute('select * from management where id=%s', (id))
        result = cursor.fetchone()

        if not result:
            return None
        id, user, password = result
        managementEntity = ManagementEntity.ManagementEntity(id, user, password)
        return managementEntity
    
    def deleteManagement(self, id):
        cursor = DButil.open(self.connection)
        cursor.execute('delete from task where id_management=%s', (id))
        cursor.execute('delete from posit where id_management=%s', (id))
        cursor.execute('delete from management where id=%s', (id))
        deleting = 'Usuario borrado con el id: ' + str(id)
        self.connection.commit()
        return deleting
    
    def insertManagement(self, managementEntity):
        cursor = DButil.open(self.connection)
        cursor.execute('insert into management (id, usr, pass) values (%s, %s, %s)', (managementEntity.getId(),managementEntity.getUser(), managementEntity.getPassword()))
        inserting = 'Usuario insertado correctamente'
        self.connection.commit()
        return inserting
        