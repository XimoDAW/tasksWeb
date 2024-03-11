import sys

sys.path.append('c:\\tasksWeb\\ProyectoFinal\\src\\domain\\repository')
import PositRepository

sys.path.append('c:\\tasksWeb\\ProyectoFinal\\src\\persistance\\dao') 
import PositDAO

sys.path.append('c:\\tasksWeb\\ProyectoFinal\\src\\persistance\\model') 
import PositEntity

sys.path.append('c:\\tasksWeb\\ProyectoFinal\\src\\mapper') 
import PositMapper

positDAO = PositDAO.PositDAO()

class PositRepositoryImpl (PositRepository.PositRepository):
    def getAll(self):
        positsList = list()
        positEntityList = positDAO.getAll()

        for positEntity in positEntityList:
            positsList.append(PositMapper.toPosit(positEntity))
        return positsList

    def getById(self, id):
        positEntity = positDAO.getById(id)
        posit = PositMapper.toPosit(positEntity)
        return posit

a = PositRepositoryImpl()