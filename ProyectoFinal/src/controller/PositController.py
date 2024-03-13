import sys
from flask import Blueprint, Flask, jsonify, request

positApp = Blueprint('positApp', __name__)


sys.path.append('c:\\tasksWeb\\ProyectoFinal\\src\\domain\\service\\impl')
import PositServiceImpl

sys.path.append('c:\\tasksWeb\\ProyectoFinal\\src\\http_response')
import ResponseTask

sys.path.append('c:\\tasksWeb\\ProyectoFinal\\src\\controller\\entity')
import PositCreate

sys.path.append('c:\\tasksWeb\\ProyectoFinal\\src\\mapper') 
import PositMapper

sys.path.append('c:\\tasksWeb\\ProyectoFinal\\src\\http_errors')
import ResourceNotFoundException

positService = PositServiceImpl.PositServiceImpl()

@positApp.route('/posits', methods=['GET'])
def getAll():
    #Posible paginacion en futuro: page = request.args.get('page', type=int)
    positList = positService.getAll()
    positsDetailWeb = []
    for posit in positList:
        positsDetailWeb.append(PositMapper.toPositDetailWeb(posit).getJson())

    response = ResponseTask.getPage(positsDetailWeb)
    return response

@positApp.route('/posits/<int:id>', methods=['GET'])
def getById(id, name=None):

    try:
        posit = positService.getById(id)
        positDetailWeb = PositMapper.toPositDetailWeb(posit).getJson()
        response = ResponseTask.getPage(positDetailWeb)
        return response
        
    except ResourceNotFoundException.ResourceNotFoundException as exce:
        return exce.getMessage()

@positApp.route('/posits', methods=['POST'])
def insertPosit():
    request_data = request.get_json()
    positCreate = PositCreate.PositCreate('')

    if 'name' in request_data:
        positCreate.setName(request_data['name'])

    posit = PositMapper.toPositForInsert(positCreate)

    response = ResponseTask.getPage(positService.insertPosit(posit))
    return response

@positApp.route('/posits/<int:id>', methods=['DELETE'])
def deletePosit(id, name=None):
    deleting = positService.deletePosit(id)

    response = ResponseTask.getPage(deleting)
    return response
