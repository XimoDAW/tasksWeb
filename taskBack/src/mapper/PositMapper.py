import sys

sys.path.append('c:\\tasksWeb\\taskBack\\src\\persistance\\model')
import PositEntity

sys.path.append('c:\\tasksWeb\\taskBack\\src\\domain\\entity')
import Posit

sys.path.append('c:\\tasksWeb\\taskBack\\src\\controller\\entity')
import PositDetailWeb

sys.path.append('c:\\tasksWeb\\taskBack\\src\\controller\\entity')
import PositCreate

def toPosit(positEntity):
    posit = Posit.Posit(0, '', 0)
    posit.setId(positEntity.getId())
    posit.setName(positEntity.getName())
    posit.setManagementId(positEntity.getManagementId())
    return posit

def toPositDetailWeb(posit):
    positDetailWeb = PositDetailWeb.PositDetailWeb(0, '', 0)
    positDetailWeb.setId(posit.getId())
    positDetailWeb.setName(posit.getName())
    positDetailWeb.setManagementId(posit.getManagementId())
    return positDetailWeb

def toPositForInsert(positCreate):
    posit = Posit.Posit(0, '', 0)
    posit.setName(positCreate.getName())
    posit.setManagementId(positCreate.getManagementId())
    return posit

def toPositForUpdate(positCreate):
    posit = Posit.Posit(0, '', 0)
    posit.setName(positCreate.getName())
    posit.setManagementId(positCreate.getManagementId())
    return posit

def toPositEntity(posit):
    positEntity = PositEntity.PositEntity(0, '', 0)
    positEntity.setName(posit.getName())
    positEntity.setManagementId(posit.getManagementId())
    return positEntity