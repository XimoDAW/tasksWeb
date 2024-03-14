import sys

sys.path.append('c:\\tasksWeb\\ProyectoFinal\\src\\persistance\\model')
import TaskEntity

sys.path.append('c:\\tasksWeb\\ProyectoFinal\\src\\domain\\entity')
import Task

sys.path.append('c:\\tasksWeb\\ProyectoFinal\\src\\mapper')
import PositMapper

sys.path.append('c:\\tasksWeb\\ProyectoFinal\\src\\mapper')
import ManagementMapper


def toTask(taskEntity):
    task = Task.Task(0, '', '', None, None, '', '', None)
    task.setId(taskEntity.getId())
    task.setDescription(taskEntity.getDescription())
    task.setPosit(PositMapper.toPosit(taskEntity.getPositEntity()))
    task.setManagement(ManagementMapper.toManagement(taskEntity.getManagementEntity()))
    task.setStartDate(taskEntity.getStartDate())
    task.setEndDate(taskEntity.getEndDate())
    return task