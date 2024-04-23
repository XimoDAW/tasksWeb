import sys

sys.path.append('c:\\tasksWeb\\ProyectoFinal\\src\\domain\\entity')
import Management

sys.path.append('c:\\tasksWeb\\ProyectoFinal\\src\\persistance\\model')
import ManagementEntity

sys.path.append('c:\\tasksWeb\\ProyectoFinal\\src\\controller\\entity')
import ManagementDetailWeb

def toManagement(managementEntity):
    management = Management.Management(0, '', '')
    management.setId(managementEntity.getId())
    management.setUser(managementEntity.getUser())
    management.setPassword(managementEntity.getPassword())
    return management

def toManagementDetailWeb(management):
    managementDetailWeb = ManagementDetailWeb.ManagementDetailWeb(0, '', '')
    managementDetailWeb.setId(management.getId())
    managementDetailWeb.setUser(management.getUser())
    managementDetailWeb.setPassword(management.getPassword())
    return managementDetailWeb

def toManagementForInsert(managementCreate):
    management = Management.Management(0, '', '')
    management.setUser(managementCreate.getUser())
    management.setPassword(managementCreate.getPassword())
    return management

def toManagementEntity(management):
    managementEntity = ManagementEntity.ManagementEntity(0, '', '')
    managementEntity.setUser(management.getUser())
    managementEntity.setPassword(management.getPassword())
    return managementEntity