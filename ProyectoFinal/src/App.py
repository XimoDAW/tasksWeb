import sys

from flask import Flask

app = Flask (__name__)

sys.path.append('c:\\tasksWeb\\ProyectoFinal\\src\\controller')

from PositController import positApp

sys.path.append('c:\\tasksWeb\\ProyectoFinal\\src\\controller')

from ManagementController import managementApp

app.register_blueprint(managementApp)
app.register_blueprint(positApp)


if (__name__=='__main__'):
    app.run(debug=True)
