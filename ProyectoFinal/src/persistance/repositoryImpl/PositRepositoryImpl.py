import sys

sys.path.append('c:\\tasksWeb\\ProyectoFinal\\src\\domain\\repository')
import PositRepository

sys.path.append('c:\\tasksWeb\\ProyectoFinal\\src\\persistance\\dao') 
import PositDAO

sys.path.append('c:\\tasksWeb\\ProyectoFinal\\src\\persistance\\model') 
import PositEntity

sys.path.append('c:\\tasksWeb\\ProyectoFinal\\src\\mapper') 
import PositMapper

sys.path.append('c:\\tasksWeb\\ProyectoFinal\\src\\http_errors')
import SQLException

sys.path.append('c:\\tasksWeb\\ProyectoFinal\\src\\http_errors')
import ResourceNotFoundException


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
        if (positEntity is None):
            return None
            
        posit = PositMapper.toPosit(positEntity)
        return posit 
            
    def deletePosit(self, id):
        return positDAO.deletePosit(id)
    
    def insertPosit(self, posit):
        positEntity = PositMapper.toPositEntity(posit)
        return positDAO.insertPosit(positEntity)