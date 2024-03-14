import sys

sys.path.append('c:\\tasksWeb\\ProyectoFinal\\src\\persistance\\model')
import StatusEntity

sys.path.append('c:\\tasksWeb\\ProyectoFinal\\src\\domain\\entity')
import Status

def toStatus(statusEntity):
    status = Status.Status(0, '')
    status.setId(statusEntity.getId())
    status.setStatus(statusEntity.getStatus())
    return status