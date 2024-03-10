import sys
from flask import Flask, jsonify

app = Flask (__name__)

sys.path.append('c:\\tasksWeb\\ProyectoFinal\\src\\domain\\service\\impl')
import PositServiceImpl

sys.path.append('c:\\tasksWeb\\ProyectoFinal\\src\\mapper') 
import PositMapper

@app.route('/posits', methods=['GET'])
def getAll():
    positList = PositServiceImpl.PositServiceImpl().getAll()
    positsDetailWeb = []

    for posit in positList:
        positsDetailWeb.append(PositMapper.toPositDetailWeb(posit).getJson())
    return jsonify(positsDetailWeb)


app.run(debug=True)