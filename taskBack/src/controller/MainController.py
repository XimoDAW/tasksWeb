import sys
from flask import Blueprint

mainApp = Blueprint('mainApp', __name__)

sys.path.append('c:\\tasksWeb\\taskBack\\src\\http_response')
import ResponseTask

@mainApp.route('/', methods=['GET'])
def getMain():
        response = ResponseTask.getPage('Bienvendio a TaskAPI')
        return response