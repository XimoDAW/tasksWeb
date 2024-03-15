import sys

sys.path.append('c:\\tasksWeb\\ProyectoFinal\\src\\controller\\entity')
import TaskListWeb

sys.path.append('c:\\tasksWeb\\ProyectoFinal\\src\\controller\\entity')
import TaskDetailWeb

sys.path.append('c:\\tasksWeb\\ProyectoFinal\\src\\domain\\entity')
import Task

sys.path.append('c:\\tasksWeb\\ProyectoFinal\\src\\persistance\\model')
import TaskEntity

sys.path.append('c:\\tasksWeb\\ProyectoFinal\\src\\mapper')
import PositMapper

sys.path.append('c:\\tasksWeb\\ProyectoFinal\\src\\mapper')
import ManagementMapper


def toTask(taskEntity):
    task = Task.Task(0, '', '', None, None, '', '', None)
    task.setId(taskEntity.getId())
    task.setName(taskEntity.getName())
    task.setDescription(taskEntity.getDescription())
    task.setPosit(PositMapper.toPosit(taskEntity.getPositEntity()))
    task.setManagement(ManagementMapper.toManagement(taskEntity.getManagementEntity()))
    task.setStartDate(taskEntity.getStartDate())
    task.setEndDate(taskEntity.getEndDate())
    return task

def toTaskListWeb(task):
    taskListWeb = TaskListWeb.TaskListWeb(0, '')
    taskListWeb.setId(task.getId())
    taskListWeb.setName(task.getName())
    return taskListWeb

def toTaskDetailWeb(task):
    taskDetailWeb = TaskDetailWeb.TaskDetailWeb(0, '', '', None, None, '', '', '')
    taskDetailWeb.setId(task.getId())
    taskDetailWeb.setName(task.getName())
    taskDetailWeb.setDescription(task.getDescription())
    taskDetailWeb.setPositDetailWeb(PositMapper.toPosit(task.getPosit()))
    taskDetailWeb.setManagementDetailWeb(ManagementMapper.toManagement(task.getManagement()))
    taskDetailWeb.setStartDate(task.getStartDate())
    taskDetailWeb.setEndDate(task.getEndDate())
    taskDetailWeb.setStatusDetailWeb(task.getStatus().getStatus())
    return taskDetailWeb

def toTaskForInsert(taskCreate):
    task = Task.Task(0, '', '', None, None, '', '', None)
    task.setName(taskCreate.getName())
    task.setDescription(taskCreate.getDescription())
    task.setPosit(None)
    task.setStatus(None)
    task.setManagement(None)
    task.setStartDate(taskCreate.getStartDate())
    task.setEndDate(taskCreate.getEndDate())
    return task

def toTaskEntity(task):
    taskEntity = TaskEntity.TaskEntity(0, '', '', None, None, '', '', None)
    taskEntity.setName(task.getName())
    taskEntity.setDescription(task.getDescription())
    taskEntity.setPositEntity(task.getPosit())
    taskEntity.setManagementEntity(task.getManagement())
    taskEntity.setStartDate(task.getStartDate())
    taskEntity.setEndDate(task.getEndDate())
    return taskEntity