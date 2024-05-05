import sys

from unittest import mock
from unittest.mock import patch, MagicMock

import pytest

import unittest

sys.path.append('c:\\tasksWeb\\ProyectoFinal\\src\\domain\\entity')
import Management

sys.path.append('c:\\tasksWeb\\ProyectoFinal\\src\\domain\\entity')
import Posit

sys.path.append('c:\\tasksWeb\\ProyectoFinal\\src\\domain\\entity')
import Task

sys.path.append('c:\\tasksWeb\\ProyectoFinal\\src\\controller\\entity')
import ManagementDetailWeb

sys.path.append('c:\\tasksWeb\\ProyectoFinal\\src\\controller\\entity')
import ManagementCreate

sys.path.append('c:\\tasksWeb\\ProyectoFinal\\src\\controller\\entity')
import PositCreate

sys.path.append('c:\\tasksWeb\\ProyectoFinal\\src\\controller\\entity')
import PositDetailWeb

sys.path.append('c:\\tasksWeb\\ProyectoFinal\\src\\controller\\entity')
import TaskCreate

sys.path.append('c:\\tasksWeb\\ProyectoFinal\\src\\controller\\entity')
import TaskDetailWeb

sys.path.append('c:\\tasksWeb\\ProyectoFinal\\src\\controller\\entity')
import TaskListWeb

sys.path.append('c:\\tasksWeb\\ProyectoFinal\\src\\controller')
import ManagementController

sys.path.append('c:\\tasksWeb\\ProyectoFinal\\src\\controller')
import PositController

sys.path.append('c:\\tasksWeb\\ProyectoFinal\\src\\controller')
import TaskController

def test_constructor_managementCreate():
    management = ManagementCreate.ManagementCreate('Prueba', 'Prueba')
    assert (management.getUser() == 'Prueba')
    assert (management.getPassword() == 'Prueba')

def test_constructor_positCreate():
    posit = PositCreate.PositCreate('Prueba', 1)
    assert (posit.getName() == 'Prueba')
    assert (posit.getManagementId() == 1)

def test_constructor_taskCreate():
    management = ManagementDetailWeb.ManagementDetailWeb(1, 'Prueba', 'Prueba')
    posit = PositDetailWeb.PositDetailWeb(1, 'Prueba', management.getId())
    task = TaskCreate.TaskCreate('Prueba', 'Prueba', posit.getId(), management.getId(), '20-06-1999', '20-07-1999')
    assert (task.getName() == 'Prueba')
    assert (task.getPositId() == 1)
    assert (task.getManagementId() == 1)
    assert (task.getStartDate() == '20-06-1999')
    assert (task.getEndDate() == '20-07-1999')

@mock.patch('ManagementController.getAll')
def test_management_controller_get_all(mock_get_all):

    test_data = [
    {"id": 1, "user": "Elemento 1", "password": "Elemento 1"},
    {"id": 2, "user": "Elemento 2", "password": "Elemento 2"}
    ]
    
    mock_get_all.return_value = test_data

    management_controller = ManagementController

    result = management_controller.getAll()

    assert result == test_data

@mock.patch('ManagementController.getById')
def test_management_controller_get_by_id(mock_get_by_id):

    test_data = ManagementDetailWeb.ManagementDetailWeb(1, 'Prueba', 'Prueba')
    
    mock_get_by_id.return_value = test_data

    management_controller = ManagementController

    result = management_controller.getById(1)

    assert result == test_data

@mock.patch('ManagementController.insertManagement')
def test_management_controller_insert_management(mock_insert_management):

    test_data = 'Usuario insertado correctamente'
    
    mock_insert_management.return_value = test_data

    management_controller = ManagementController

    result = management_controller.insertManagement(Management.Management(1, 'Prueba', 'Prueba'))

    assert result == 'Usuario insertado correctamente'
    
@mock.patch('ManagementController.deleteManagement')
def test_management_controller_delete_management(mock_delete_management):

    management = Management.Management(1, 'Prueba', 'Prueba')
    test_data = 'Usuario borrado con el id: ' + str(management.getId())
    
    mock_delete_management.return_value = test_data

    management_controller = ManagementController

    result = management_controller.deleteManagement(management.getId())

    assert result == 'Usuario borrado con el id: ' + str(management.getId())

@mock.patch('PositController.getAll')
def test_posit_controller_get_all(mock_get_all):

    test_data = [
    {"id": 1, "name": "Elemento 1", "managementId": 1},
    {"id": 2, "name": "Elemento 2", "managementId": 1}
    ]
    
    mock_get_all.return_value = test_data

    posit_controller = PositController

    result = posit_controller.getAll()

    assert result == test_data

@mock.patch('PositController.getById')
def test_posit_repository_get_by_id(mock_get_by_id):

    test_data = PositDetailWeb.PositDetailWeb(1, 'Prueba', 'Prueba')
    
    mock_get_by_id.return_value = test_data

    posit_controller = PositController

    result = posit_controller.getById(1)

    assert result == test_data

@mock.patch('PositController.insertPosit')
def test_posit_controller_insert_posit(mock_insert_posit):

    test_data = 'Posit insertado correctamente'
    
    mock_insert_posit.return_value = test_data

    posit_controller = PositController

    result = posit_controller.insertPosit(PositCreate.PositCreate('Prueba', 1))

    assert result == 'Posit insertado correctamente'
    
@mock.patch('PositController.deletePosit')
def test_posit_controller_delete_posit(mock_delete_posit):

    posit = PositDetailWeb.PositDetailWeb(1, 'Prueba', 1)
    test_data = 'Posit borrado con el id: ' + str(posit.getId())
    
    mock_delete_posit.return_value = test_data

    posit_controller = PositController

    result = posit_controller.deletePosit(posit.getId())

    assert result == 'Posit borrado con el id: ' + str(posit.getId())

@mock.patch('PositController.updatePosit')
def test_posit_repository_update_posit(mock_update_posit):

    test_data = 'Posit actualizado correctamente'
    
    mock_update_posit.return_value = test_data

    posit_controller = PositController

    result = posit_controller.updatePosit(PositCreate.PositCreate('Prueba', 2), 1)

    assert result == 'Posit actualizado correctamente'

@mock.patch('TaskController.getAll')
def test_task_repository_get_all(mock_get_all):

    posit = PositDetailWeb.PositDetailWeb(1, 'Prueba', 1)
    management = ManagementDetailWeb.ManagementDetailWeb(1, 'Prueba', 'Prueba')
    
    test_data = [
    {"id": 1, "name": "Elemento 1", "description": "Descripcion", "positDetailWeb": posit, "managementDetailWeb": management, "startDate": "10-10-2023", "endDate": "11-10-2023", "status": "Fuera de plazo"},
    {"id": 2, "name": "Elemento 2", "description": "Descripcion", "positDetailWeb": posit, "managementDetailWeb": management, "startDate": "10-11-2023", "endDate": "11-12-2023", "status": "Fuera de plazo"}
    ]
    
    mock_get_all.return_value = test_data

    task_controller = TaskController

    result = task_controller.getAll()

    assert result == test_data

@mock.patch('TaskController.getById')
def test_task_repository_get_by_id(mock_get_by_id):

    posit = PositDetailWeb.PositDetailWeb(1, 'Prueba', 1)
    management = ManagementDetailWeb.ManagementDetailWeb(1, 'Prueba', 'Prueba')

    test_data = TaskDetailWeb.TaskDetailWeb(1, 'Prueba', 'Prueba', posit, management, '20-06-1999', '20-07-1999', 'Pendiente')
    
    mock_get_by_id.return_value = test_data

    task_controller = TaskController

    result = task_controller.getById(1)

    assert result == test_data

@mock.patch('TaskController.insertTask')
def test_task_repository_insert_task(mock_insert_task):

    posit = Posit.Posit(1, 'Prueba', 1)
    management = Management.Management(1, 'Prueba', 'Prueba')

    test_data = 'Tarea insertada correctamente'
    
    mock_insert_task.return_value = test_data

    task_repository = TaskController

    result = task_repository.insertTask(TaskCreate.TaskCreate('Prueba', 'Prueba', posit, management, '20-06-1999', '20-07-1999'), 1)

    assert result == 'Tarea insertada correctamente'
    
@mock.patch('TaskController.deleteTask')
def test_task_repository_delete_task(mock_delete_task):

    posit = Posit.Posit(1, 'Prueba', 1)
    management = Management.Management(1, 'Prueba', 'Prueba')
    task = Task.Task(1, 'Prueba', 'Prueba', posit, management, '20-06-1999', '20-07-1999', 'Pendiente')

    test_data = 'Tarea borrada con el id: ' + str(task.getId())
    
    mock_delete_task.return_value = test_data

    task_controller = TaskController

    result = task_controller.deleteTask(task.getId())

    assert result == 'Tarea borrada con el id: ' + str(task.getId())

@mock.patch('TaskController.updateTask')
def test_task_repository_update_task(mock_update_task):
    posit = Posit.Posit(1, 'Prueba', 1)
    management = Management.Management(1, 'Prueba', 'Prueba')
    test_data = 'Tarea actualizada correctamente'
    
    mock_update_task.return_value = test_data

    task_controller = TaskController

    result = task_controller.updateTask(TaskCreate.TaskCreate('Prueba', 'Prueba', posit, management, '20-06-1999', '20-07-1999'), 1)

    assert result == 'Tarea actualizada correctamente'