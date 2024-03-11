import sys
from flask import Flask, jsonify, request

app = Flask (__name__)

sys.path.append('c:\\tasksWeb\\ProyectoFinal\\src\\domain\\service\\impl')
import PositServiceImpl

sys.path.append('c:\\tasksWeb\\ProyectoFinal\\src\\http_response')
import ResponseTask

sys.path.append('c:\\tasksWeb\\ProyectoFinal\\src\\mapper') 
import PositMapper

positService = PositServiceImpl.PositServiceImpl()

@app.route('/posits', methods=['GET'])
def getAll():
    #Posible paginacion en futuro: page = request.args.get('page', type=int)
    positList = positService.getAll()
    positsDetailWeb = []
    for posit in positList:
        positsDetailWeb.append(PositMapper.toPositDetailWeb(posit).getJson())

    response = ResponseTask.getPage(positsDetailWeb)
    return response

@app.route('/posits/<int:id>', methods=['GET'])
def getById(id, name=None):
    #Posible paginacion en futuro: page = request.args.get('page', type=int)
    posit = positService.getById(id)
    positDetailWeb = PositMapper.toPositDetailWeb(posit).getJson()

    response = ResponseTask.getPage(positDetailWeb)
    return response


app.run(debug=True)