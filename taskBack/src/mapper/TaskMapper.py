import sys

sys.path.append('c:\\tasksWeb\\taskBack\\src\\controller\\entity')
import TaskListWeb

sys.path.append('c:\\tasksWeb\\taskBack\\src\\controller\\entity')
import TaskDetailWeb

sys.path.append('c:\\tasksWeb\\taskBack\\src\\domain\\entity')
import Task

sys.path.append('c:\\tasksWeb\\taskBack\\src\\persistance\\model')
import TaskEntity

sys.path.append('c:\\tasksWeb\\taskBack\\src\\mapper')
import PositMapper

sys.path.append('c:\\tasksWeb\\taskBack\\src\\mapper')
import ManagementMapper


def toTask(taskEntity):
    task = Task.Task(0, '', '', None, None, '', '', '')
    task.setId(taskEntity.getId())
    task.setName(taskEntity.getName())
    task.setDescription(taskEntity.getDescription())
    task.setPosit(PositMapper.toPosit(taskEntity.getPositEntity()))
    task.setManagement(ManagementMapper.toManagement(taskEntity.getManagementEntity()))
    task.setStartDate(taskEntity.getStartDate())
    task.setEndDate(taskEntity.getEndDate())
    task.setStatus(mapperStatusToTask(taskEntity.getStatus()))
    return task

def mapperStatusToTask(statusCondition):
    if (statusCondition):
        return 'Pendiente'
    return 'Fuera de plazo'

def toTaskListWeb(task):
    taskListWeb = TaskListWeb.TaskListWeb(0, '', 0)
    taskListWeb.setId(task.getId())
    taskListWeb.setName(task.getName())
    taskListWeb.setManagementId(task.getManagement().getId())
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
    taskDetailWeb.setStatus(task.getStatus())
    return taskDetailWeb

def toTaskForInsert(taskCreate):
    task = Task.Task(0, '', '', None, None, '', '', '')
    task.setName(taskCreate.getName())
    task.setDescription(taskCreate.getDescription())
    task.setPosit(None)
    task.setManagement(None)
    task.setStartDate(taskCreate.getStartDate())
    task.setEndDate(taskCreate.getEndDate())
    task.setStatus('')

    return task

def toTaskForUpdate(taskCreate, id):
    task = Task.Task(id, '', '', None, None, '', '', '')
    task.setName(taskCreate.getName())
    task.setDescription(taskCreate.getDescription())
    task.setPosit(None)
    task.setManagement(None)
    task.setStartDate(taskCreate.getStartDate())
    task.setEndDate(taskCreate.getEndDate())
    task.setStatus('')

    return task

def toTaskEntity(task):
    taskEntity = TaskEntity.TaskEntity(0, '', '', None, None, '', '', True)
    taskEntity.setName(task.getName())
    taskEntity.setDescription(task.getDescription())
    taskEntity.setPositEntity(task.getPosit())
    taskEntity.setManagementEntity(task.getManagement())
    taskEntity.setStartDate(task.getStartDate())
    taskEntity.setEndDate(task.getEndDate())
    taskEntity.setStatus(task.getStatus())
    return taskEntity