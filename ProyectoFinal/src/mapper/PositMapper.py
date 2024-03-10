import sys

sys.path.append('c:\\tasksWeb\\ProyectoFinal\\src\\persistance\\model')
import PositEntity

sys.path.append('c:\\tasksWeb\\ProyectoFinal\\src\\domain\\entity')
import Posit

sys.path.append('c:\\tasksWeb\\ProyectoFinal\\src\\controller\\entity')
import PositDetailWeb

def toPosit(positEntity):
    posit = Posit.Posit(0, '')
    posit.setId(positEntity.getId())
    posit.setName(positEntity.getName())
    return posit

def toPositDetailWeb(posit):
    positDetailWeb = PositDetailWeb.PositDetailWeb(0, '')
    positDetailWeb.setId(posit.getId())
    positDetailWeb.setName(posit.getName())
    return positDetailWeb