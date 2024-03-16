import sys

from flask import Flask

app = Flask (__name__)

sys.path.append('c:\\tasksWeb\\ProyectoFinal\\src\\controller')

from PositController import positApp

sys.path.append('c:\\tasksWeb\\ProyectoFinal\\src\\controller')

from ManagementController import managementApp

sys.path.append('c:\\tasksWeb\\ProyectoFinal\\src\\controller')

from TaskController import taskApp

sys.path.append('c:\\tasksWeb\\ProyectoFinal\\src\\controller')

from MainController import mainApp

app.register_blueprint(managementApp)
app.register_blueprint(positApp)
app.register_blueprint(taskApp)
app.register_blueprint(mainApp)

if (__name__=='__main__'):
    app.run(debug=True)
