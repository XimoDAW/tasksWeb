import sys

sys.path.append('c:\\tasksWeb\\ProyectoFinal\\src\\domain\\entity')
import Management

sys.path.append('c:\\tasksWeb\\ProyectoFinal\\src\\controller\\entity')
import ManagementDetailWeb

def toManagement(managementEntity):
    management = Management.Management(0)
    management.setId(managementEntity.getId())
    return management

def toManagementDetailWeb(management):
    managementDetailWeb = ManagementDetailWeb.ManagementDetailWeb(0)
    managementDetailWeb.setId(management.getId())
    return managementDetailWeb