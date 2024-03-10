import sys

sys.path.append('c:\\tasksWeb\\ProyectoFinal\\src\\domain\\repository')
import PositRepository

sys.path.append('c:\\tasksWeb\\ProyectoFinal\\src\\bd') 
import DButil

sys.path.append('c:\\tasksWeb\\ProyectoFinal\\src\\persistance\\model') 
import PositEntity

sys.path.append('c:\\tasksWeb\\ProyectoFinal\\src\\mapper') 
import PositMapper

connection = DButil.connect('localhost', 'root', 'root', 'tasks')
cursor = DButil.open(connection)

class PositRepositoryImpl (PositRepository.PositRepository):
    def getAll(self):
        positsList = list()
        cursor.execute('select * from posit')

        for id, name in cursor.fetchall():
            positsList.append(PositMapper.toPosit(PositEntity.PositEntity(id, name)))
        return positsList

    def getById(self, id):
        pass
