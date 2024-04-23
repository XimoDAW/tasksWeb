import sys
from flask import Blueprint, Flask, jsonify, request

managementApp = Blueprint('managementApp', __name__)

sys.path.append('c:\\tasksWeb\\ProyectoFinal\\src\\http_response')
import ResponseTask

sys.path.append('c:\\tasksWeb\\ProyectoFinal\\src\\http_errors')
import ResourceNotFoundException

sys.path.append('c:\\tasksWeb\\ProyectoFinal\\src\\mapper') 
import ManagementMapper

sys.path.append('c:\\tasksWeb\\ProyectoFinal\\src\\controller\\entity') 
import ManagementCreate

sys.path.append('c:\\tasksWeb\\ProyectoFinal\\src\\domain\\service\\impl')
import ManagementServiceImpl

managementService = ManagementServiceImpl.ManagementServiceImpl()

@managementApp.route('/management', methods=['GET'])
def getAll():
    try:
        user = request.args.get('user', type=str)
        password = request.args.get('password', type=str)
        #Posible paginacion en futuro: page = request.args.get('page', type=int)
        management = managementService.getByUser(user, password)
        managementDetailWeb = ManagementMapper.toManagementDetailWeb(management).getJson()
        response = ResponseTask.getPage(managementDetailWeb)
        return response
    except ResourceNotFoundException.ResourceNotFoundException as exce:
        return exce.getMessage()

@managementApp.route('/management/<int:id>', methods=['GET'])
def getById(id, name=None):

    try:
        management = managementService.getById(id)
        managementDetailWeb = ManagementMapper.toManagementDetailWeb(management).getJson()
        response = ResponseTask.getPage(managementDetailWeb)
        return response
        
    except ResourceNotFoundException.ResourceNotFoundException as exce:
        return exce.getMessage()
    

@managementApp.route('/management', methods=['POST'])
def insertManagement():
    try:
        request_data = request.get_json()
        managementCreate = ManagementCreate.ManagementCreate('', '')

        if ('user' in request_data) & ('password' in request_data):
            managementCreate.setUser(request_data['user'])
            managementCreate.setPassword(request_data['password'])

        management = ManagementMapper.toManagementForInsert(managementCreate)
        response = ResponseTask.getPage(managementService.insertManagement(management))
        return response
    except Exception as exce:
        return exce
    
@managementApp.route('/management/<int:id>', methods=['DELETE'])
def deleteManagement(id, name=None):
    deleting = managementService.deleteManagement(id)

    response = ResponseTask.getPage(deleting)
    return response
