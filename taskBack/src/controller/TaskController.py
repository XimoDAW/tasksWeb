import sys
from flask import Blueprint, Flask, jsonify, request

taskApp = Blueprint('taskApp', __name__)

sys.path.append('c:\\tasksWeb\\taskBack\\src\\http_response')
import ResponseTask

sys.path.append('c:\\tasksWeb\\taskBack\\src\\http_errors')
import DateException

sys.path.append('c:\\tasksWeb\\taskBack\\src\\controller\\entity')
import TaskCreate

sys.path.append('c:\\tasksWeb\\taskBack\\src\\http_errors')
import ResourceNotFoundException

sys.path.append('c:\\tasksWeb\\taskBack\\src\\mapper') 
import TaskMapper

sys.path.append('c:\\tasksWeb\\taskBack\\src\\domain\\service\\impl')
import TaskServiceImpl


taskService = TaskServiceImpl.TaskServiceImpl()

@taskApp.route('/tasks', methods=['GET'])
def getAll():

    #Posible paginacion en futuro: page = request.args.get('page', type=int)
    posit = request.args.get('positId', type=int)
    taskList = taskService.getAll(posit)
    tasksListWeb = []
    for task in taskList:
        tasksListWeb.append(TaskMapper.toTaskListWeb(task).getJson())

    response = ResponseTask.getPage(tasksListWeb)
    return response

@taskApp.route('/tasks/<int:id>', methods=['GET'])
def getById(id, name=None):
    try:
        task = taskService.getById(id)
        taskDetailWeb = TaskMapper.toTaskDetailWeb(task).getJson()
        response = ResponseTask.getPage(taskDetailWeb)
        return response
        
    except ResourceNotFoundException.ResourceNotFoundException as exce:
        return exce.getMessage()
    
@taskApp.route('/tasks', methods=['POST'])
def insertTask():
    request_data = request.get_json()
    taskCreate = TaskCreate.TaskCreate('', '', 0, 0, '', '')
    try:

        if ('name' in request_data) & ('description' in request_data) & ('positId' in request_data) & ('managementId' in request_data) & ('startDate' in request_data) & ('endDate' in request_data):
            taskCreate.setName(request_data['name'])
            taskCreate.setDescription(request_data['description'])
            taskCreate.setPositId(request_data['positId'])
            taskCreate.setManagementId(request_data['managementId'])
            taskCreate.setStartDate(request_data['startDate'])
            taskCreate.setEndDate(request_data['endDate'])
        task = TaskMapper.toTaskForInsert(taskCreate)
        response = ResponseTask.getPage(taskService.insertTask(task, taskCreate.getPositId(), taskCreate.getManagementId()))
        return response
    except DateException.DateException as exce:
        return exce.getMessage()
    
@taskApp.route('/tasks/<int:id>', methods=['PUT'])
def updateTask(id, name=None):
    request_data = request.get_json()
    taskCreate = TaskCreate.TaskCreate('', '', 0, 0, '', '')
    try:

        if ('name' in request_data) & ('description' in request_data) & ('positId' in request_data) & ('managementId' in request_data) & ('startDate' in request_data) & ('endDate' in request_data):
            taskCreate.setName(request_data['name'])
            taskCreate.setDescription(request_data['description'])
            taskCreate.setPositId(request_data['positId'])
            taskCreate.setManagementId(request_data['managementId'])
            taskCreate.setStartDate(request_data['startDate'])
            taskCreate.setEndDate(request_data['endDate'])

        task = TaskMapper.toTaskForUpdate(taskCreate, id)
        response = ResponseTask.getPage(taskService.updateTask(task, taskCreate.getPositId(), taskCreate.getManagementId(), id))
        return response
    except DateException.DateException as exce:
        return exce.getMessage()

@taskApp.route('/tasks/<int:id>', methods=['DELETE'])
def deleteTask(id, name=None):
    deleting = taskService.deleteTask(id)

    response = ResponseTask.getPage(deleting)
    return response