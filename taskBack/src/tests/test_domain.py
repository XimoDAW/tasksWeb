import sys

from unittest import mock
from unittest.mock import patch, MagicMock

import pytest

import unittest

sys.path.append('c:\\tasksWeb\\taskBack\\src\\domain\\entity')
import Management

sys.path.append('c:\\tasksWeb\\taskBack\\src\\domain\\entity')
import Task

sys.path.append('c:\\tasksWeb\\taskBack\\src\\domain\\entity')
import Posit

sys.path.append('c:\\tasksWeb\\taskBack\\src\\domain\\service')
import ManagementService

sys.path.append('c:\\tasksWeb\\taskBack\\src\\domain\\service')
import PositService

sys.path.append('c:\\tasksWeb\\taskBack\\src\\domain\\service')
import TaskService

sys.path.append('c:\\tasksWeb\\taskBack\\src\\domain\\service\\impl')
import ManagementServiceImpl

sys.path.append('c:\\tasksWeb\\taskBack\\src\\domain\\service\\impl')
import PositServiceImpl

sys.path.append('c:\\tasksWeb\\taskBack\\src\\domain\\service\\impl')
import TaskServiceImpl

sys.path.append('c:\\tasksWeb\\taskBack\\src\\http_errors')
import ResourceNotFoundException

sys.path.append('c:\\tasksWeb\\taskBack\\src\\http_errors')
import DateException

def test_constructor_management():
    management = Management.Management(1, 'Prueba', 'Prueba')
    assert (management.getId() == 1)
    assert (management.getUser() == 'Prueba')
    assert (management.getPassword() == 'Prueba')

def test_constructor_posit():
    management = Management.Management(1, 'Prueba', 'Prueba')
    posit = Posit.Posit(1, 'Prueba', management.getId())
    assert (posit.getId() == 1)
    assert (posit.getName() == 'Prueba')
    assert (posit.getManagementId() == management.getId())

def test_constructor_task():
    management = Management.Management(1, 'Prueba', 'Prueba')
    posit = Posit.Posit(1, 'Prueba', management.getId())
    task = Task.Task(1, 'Prueba', 'Prueba', posit, management, '20-06-1999', '20-07-1999', 'Pendiente')
    assert (task.getId() == 1)
    assert (task.getName() == 'Prueba')
    assert (task.getPosit() == posit)
    assert (task.getManagement() == management)
    assert (task.getStartDate() == '20-06-1999')
    assert (task.getEndDate() == '20-07-1999')
    assert (task.getStatus() == 'Pendiente')

@mock.patch('ManagementServiceImpl.ManagementServiceImpl.getAll')
def test_management_service_get_all(mock_get_all):

    test_data = [
    {"id": 1, "user": "Elemento 1", "password": "Elemento 1"},
    {"id": 2, "user": "Elemento 2", "password": "Elemento 2"}
    ]
    
    mock_get_all.return_value = test_data

    management_service = ManagementServiceImpl.ManagementServiceImpl()

    result = management_service.getAll()

    assert result == test_data

@mock.patch('ManagementServiceImpl.ManagementServiceImpl.getById')
def test_management_service_get_by_id(mock_get_by_id):

    test_data = Management.Management(1, 'Prueba', 'Prueba')
    
    mock_get_by_id.return_value = test_data

    management_service = ManagementServiceImpl.ManagementServiceImpl()

    result = management_service.getById(1)

    assert result == test_data

@mock.patch('ManagementServiceImpl.ManagementServiceImpl.insertManagement')
def test_management_service_insert_management(mock_insert_management):

    test_data = 'Usuario insertado correctamente'
    
    mock_insert_management.return_value = test_data

    management_service = ManagementServiceImpl.ManagementServiceImpl()

    result = management_service.insertManagement(Management.Management(1, 'Prueba', 'Prueba'))

    assert result == 'Usuario insertado correctamente'
    
@mock.patch('ManagementServiceImpl.ManagementServiceImpl.deleteManagement')
def test_management_service_delete_management(mock_delete_management):

    management = Management.Management(1, 'Prueba', 'Prueba')
    test_data = 'Usuario borrado con el id: ' + str(management.getId())
    
    mock_delete_management.return_value = test_data

    management_service = ManagementServiceImpl.ManagementServiceImpl()

    result = management_service.deleteManagement(management.getId())

    assert result == 'Usuario borrado con el id: ' + str(management.getId())

@mock.patch('ManagementServiceImpl.ManagementServiceImpl.getById')
def test_management_service_get_by_id_exception(mock_get_by_id):
    mock_get_by_id.side_effect = ResourceNotFoundException.ResourceNotFoundException("Error")

    management_service = ManagementServiceImpl.ManagementServiceImpl()

    with pytest.raises(ResourceNotFoundException.ResourceNotFoundException):
        management_service.getById(1)

@mock.patch('PositServiceImpl.PositServiceImpl.getAll')
def test_posit_service_get_all(mock_get_all):

    test_data = [
    {"id": 1, "name": "Elemento 1", "managementId": 1},
    {"id": 2, "name": "Elemento 2", "managementId": 1}
    ]
    
    mock_get_all.return_value = test_data

    posit_service = PositServiceImpl.PositServiceImpl()

    result = posit_service.getAll()

    assert result == test_data

@mock.patch('PositServiceImpl.PositServiceImpl.getById')
def test_posit_service_get_by_id(mock_get_by_id):

    test_data = Posit.Posit(1, 'Prueba', 'Prueba')
    
    mock_get_by_id.return_value = test_data

    posit_service = PositServiceImpl.PositServiceImpl()

    result = posit_service.getById(1)

    assert result == test_data

@mock.patch('PositServiceImpl.PositServiceImpl.insertPosit')
def test_posit_service_insert_posit(mock_insert_posit):

    test_data = 'Posit insertado correctamente'
    
    mock_insert_posit.return_value = test_data

    posit_service = PositServiceImpl.PositServiceImpl()

    result = posit_service.insertPosit(Posit.Posit(1, 'Prueba', 1))

    assert result == 'Posit insertado correctamente'
    
@mock.patch('PositServiceImpl.PositServiceImpl.deletePosit')
def test_posit_service_delete_posit(mock_delete_posit):

    posit = Posit.Posit(1, 'Prueba', 1)
    test_data = 'Posit borrado con el id: ' + str(posit.getId())
    
    mock_delete_posit.return_value = test_data

    posit_service = PositServiceImpl.PositServiceImpl()

    result = posit_service.deletePosit(posit.getId())

    assert result == 'Posit borrado con el id: ' + str(posit.getId())

@mock.patch('PositServiceImpl.PositServiceImpl.updatePosit')
def test_posit_service_update_posit(mock_update_posit):

    test_data = 'Posit actualizado correctamente'
    
    mock_update_posit.return_value = test_data

    posit_service = PositServiceImpl.PositServiceImpl()

    result = posit_service.updatePosit(Posit.Posit(1, 'Prueba', 2))

    assert result == 'Posit actualizado correctamente'

@mock.patch('PositServiceImpl.PositServiceImpl.getById')
def test_posit_service_get_by_id_exception(mock_get_by_id):
    
    mock_get_by_id.side_effect = ResourceNotFoundException.ResourceNotFoundException("Error")

    posit_service = PositServiceImpl.PositServiceImpl()

    with pytest.raises(ResourceNotFoundException.ResourceNotFoundException):
        posit_service.getById(1)

@mock.patch('TaskServiceImpl.TaskServiceImpl.getAll')
def test_task_service_get_all(mock_get_all):

    posit = Posit.Posit(1, 'Prueba', 1)
    management = Management.Management(1, 'Prueba', 'Prueba')
    
    test_data = [
    {"id": 1, "name": "Elemento 1", "description": "Descripcion", "posit": posit, "management": management, "startDate": "10-10-2023", "endDate": "11-10-2023", "status": "Fuera de plazo"},
    {"id": 2, "name": "Elemento 2", "description": "Descripcion", "posit": posit, "management": management, "startDate": "10-11-2023", "endDate": "11-12-2023", "status": "Fuera de plazo"}
    ]
    
    mock_get_all.return_value = test_data

    task_service = TaskServiceImpl.TaskServiceImpl()

    result = task_service.getAll()

    assert result == test_data

@mock.patch('TaskServiceImpl.TaskServiceImpl.getById')
def test_task_service_get_by_id(mock_get_by_id):

    posit = Posit.Posit(1, 'Prueba', 1)
    management = Management.Management(1, 'Prueba', 'Prueba')

    test_data = Task.Task(1, 'Prueba', 'Prueba', posit, management, '20-06-1999', '20-07-1999', 'Pendiente')
    
    mock_get_by_id.return_value = test_data

    task_service = TaskServiceImpl.TaskServiceImpl()

    result = task_service.getById(1)

    assert result == test_data

@mock.patch('TaskServiceImpl.TaskServiceImpl.insertTask')
def test_task_service_insert_task(mock_insert_task):

    posit = Posit.Posit(1, 'Prueba', 1)
    management = Management.Management(1, 'Prueba', 'Prueba')

    test_data = 'Tarea insertada correctamente'
    
    mock_insert_task.return_value = test_data

    task_service = TaskServiceImpl.TaskServiceImpl()

    result = task_service.insertTask(Task.Task(1, 'Prueba', 'Prueba', posit, management, '20-06-1999', '20-07-1999', 'Pendiente'))

    assert result == 'Tarea insertada correctamente'
    
@mock.patch('TaskServiceImpl.TaskServiceImpl.deleteTask')
def test_task_service_delete_task(mock_delete_task):

    posit = Posit.Posit(1, 'Prueba', 1)
    management = Management.Management(1, 'Prueba', 'Prueba')
    task = Task.Task(1, 'Prueba', 'Prueba', posit, management, '20-06-1999', '20-07-1999', 'Pendiente')

    test_data = 'Tarea borrada con el id: ' + str(task.getId())
    
    mock_delete_task.return_value = test_data

    task_service = TaskServiceImpl.TaskServiceImpl()

    result = task_service.deleteTask(task.getId())

    assert result == 'Tarea borrada con el id: ' + str(task.getId())

@mock.patch('TaskServiceImpl.TaskServiceImpl.updateTask')
def test_task_service_update_task(mock_update_task):
    posit = Posit.Posit(1, 'Prueba', 1)
    management = Management.Management(1, 'Prueba', 'Prueba')
    test_data = 'Tarea actualizada correctamente'
    
    mock_update_task.return_value = test_data

    task_service = TaskServiceImpl.TaskServiceImpl()

    result = task_service.updateTask(Task.Task(1, 'Prueba', 'Prueba', posit, management, '20-06-1999', '20-07-1999', 'Pendiente'))

    assert result == 'Tarea actualizada correctamente'

@mock.patch('TaskServiceImpl.TaskServiceImpl.getById')
def test_task_service_get_by_id_exception(mock_get_by_id):

    mock_get_by_id.side_effect = ResourceNotFoundException.ResourceNotFoundException("Error")

    task_service = TaskServiceImpl.TaskServiceImpl()

    with pytest.raises(ResourceNotFoundException.ResourceNotFoundException):
        task_service.getById(1)

@mock.patch('TaskServiceImpl.TaskServiceImpl.getById')
def test_task_service_get_by_id_date_exception(mock_get_by_id):

    mock_get_by_id.side_effect = DateException.DateException("Error")

    task_service = TaskServiceImpl.TaskServiceImpl()

    with pytest.raises(DateException.DateException):
        task_service.getById(1)

@mock.patch('TaskServiceImpl.TaskServiceImpl.getById')
def test_task_service_date_exception(mock_get_by_id):
    
    posit = Posit.Posit(1, 'Prueba', 1)
    management = Management.Management(1, 'Prueba', 'Prueba')
    task = Task.Task(1, 'Prueba', 'Prueba', posit, management, '20-06-1999', '20-07-1999', 'Pendiente')

    with pytest.raises(DateException.DateException):
        task.setEndDate("20-02-1999")