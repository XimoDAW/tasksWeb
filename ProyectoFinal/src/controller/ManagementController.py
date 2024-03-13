import sys
from flask import Blueprint, Flask, jsonify, request

managementApp = Blueprint('managementApp', __name__)

sys.path.append('c:\\tasksWeb\\ProyectoFinal\\src\\http_response')
import ResponseTask

sys.path.append('c:\\tasksWeb\\ProyectoFinal\\src\\http_errors')
import ResourceNotFoundException

sys.path.append('c:\\tasksWeb\\ProyectoFinal\\src\\mapper') 
import ManagementMapper

sys.path.append('c:\\tasksWeb\\ProyectoFinal\\src\\domain\\service\\impl')
import ManagementServiceImpl

managementService = ManagementServiceImpl.ManagementServiceImpl()

@managementApp.route('/management/<int:id>', methods=['GET'])
def getById(id, name=None):

    try:
        management = managementService.getById(id)
        managementDetailWeb = ManagementMapper.toManagementDetailWeb(management).getJson()
        response = ResponseTask.getPage(managementDetailWeb)
        return response
        
    except ResourceNotFoundException.ResourceNotFoundException as exce:
        return exce.getMessage()
    

