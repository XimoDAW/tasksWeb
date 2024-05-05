import sys

from unittest import mock
from unittest.mock import patch, MagicMock

import pytest

import unittest

sys.path.append('c:\\tasksWeb\\ProyectoFinal\\src\\persistance\\model')
import ManagementEntity


sys.path.append('c:\\tasksWeb\\ProyectoFinal\\src\\domain\\repository')
import ManagementRepository

sys.path.append('c:\\tasksWeb\\ProyectoFinal\\src\\domain\\repository')
import PositRepository

sys.path.append('c:\\tasksWeb\\ProyectoFinal\\src\\domain\\repository')
import TaskRepository

sys.path.append('c:\\tasksWeb\\ProyectoFinal\\src\\persistance\\repositoryImpl')
import ManagementRepositoryImpl

sys.path.append('c:\\tasksWeb\\ProyectoFinal\\src\\persistance\\repositoryImpl')
import PositRepositoryImpl

sys.path.append('c:\\tasksWeb\\ProyectoFinal\\src\\persistance\\repositoryImpl')
import TaskRepositoryImpl

sys.path.append('c:\\tasksWeb\\ProyectoFinal\\src\\persistance\\model')
import TaskEntity

sys.path.append('c:\\tasksWeb\\ProyectoFinal\\src\\persistance\\model')
import PositEntity

def test_constructor_managementEntity():
    management = ManagementEntity.ManagementEntity(1, 'Prueba', 'Prueba')
    assert (management.getId() == 1)
    assert (management.getUser() == 'Prueba')
    assert (management.getPassword() == 'Prueba')

def test_constructor_positEntity():
    management = ManagementEntity.ManagementEntity(1, 'Prueba', 'Prueba')
    posit = PositEntity.PositEntity(1, 'Prueba', management.getId())
    assert (posit.getId() == 1)
    assert (posit.getName() == 'Prueba')
    assert (posit.getManagementId() == management.getId())

def test_constructor_taskEntity():
    management = ManagementEntity.ManagementEntity(1, 'Prueba', 'Prueba')
    posit = PositEntity.PositEntity(1, 'Prueba', management.getId())
    task = TaskEntity.TaskEntity(1, 'Prueba', 'Prueba', posit, management, '20-06-1999', '20-07-1999', 'Pendiente')
    assert (task.getId() == 1)
    assert (task.getName() == 'Prueba')
    assert (task.getPositEntity() == posit)
    assert (task.getManagementEntity() == management)
    assert (task.getStartDate() == '20-06-1999')
    assert (task.getEndDate() == '20-07-1999')
    assert (task.getStatus() == 'Pendiente')

@mock.patch('ManagementRepositoryImpl.ManagementRepositoryImpl.getAll')
def test_management_repository_get_all(mock_get_all):

    test_data = [
    {"id": 1, "user": "Elemento 1", "password": "Elemento 1"},
    {"id": 2, "user": "Elemento 2", "password": "Elemento 2"}
    ]
    
    mock_get_all.return_value = test_data

    management_repository = ManagementRepositoryImpl.ManagementRepositoryImpl()

    result = management_repository.getAll()

    assert result == test_data

@mock.patch('ManagementRepositoryImpl.ManagementRepositoryImpl.getById')
def test_management_repository_get_by_id(mock_get_by_id):

    test_data = ManagementEntity.ManagementEntity(1, 'Prueba', 'Prueba')
    
    mock_get_by_id.return_value = test_data

    management_repository = ManagementRepositoryImpl.ManagementRepositoryImpl()

    result = management_repository.getById(1)

    assert result == test_data

@mock.patch('ManagementRepositoryImpl.ManagementRepositoryImpl.insertManagement')
def test_management_repository_insert_management(mock_insert_management):

    test_data = 'Usuario insertado correctamente'
    
    mock_insert_management.return_value = test_data

    management_repository = ManagementRepositoryImpl.ManagementRepositoryImpl()

    result = management_repository.insertManagement(ManagementEntity.ManagementEntity(1, 'Prueba', 'Prueba'))

    assert result == 'Usuario insertado correctamente'
    
@mock.patch('ManagementRepositoryImpl.ManagementRepositoryImpl.deleteManagement')
def test_management_repository_delete_management(mock_delete_management):

    management = ManagementEntity.ManagementEntity(1, 'Prueba', 'Prueba')
    test_data = 'Usuario borrado con el id: ' + str(management.getId())
    
    mock_delete_management.return_value = test_data

    management_repository = ManagementRepositoryImpl.ManagementRepositoryImpl()

    result = management_repository.deleteManagement(management.getId())

    assert result == 'Usuario borrado con el id: ' + str(management.getId())

@mock.patch('PositRepositoryImpl.PositRepositoryImpl.getAll')
def test_posit_repository_get_all(mock_get_all):

    test_data = [
    {"id": 1, "name": "Elemento 1", "managementId": 1},
    {"id": 2, "name": "Elemento 2", "managementId": 1}
    ]
    
    mock_get_all.return_value = test_data

    posit_repository = PositRepositoryImpl.PositRepositoryImpl()

    result = posit_repository.getAll()

    assert result == test_data

@mock.patch('PositRepositoryImpl.PositRepositoryImpl.getById')
def test_posit_repository_get_by_id(mock_get_by_id):

    test_data = PositEntity.PositEntity(1, 'Prueba', 'Prueba')
    
    mock_get_by_id.return_value = test_data

    posit_repository = PositRepositoryImpl.PositRepositoryImpl()

    result = posit_repository.getById(1)

    assert result == test_data

@mock.patch('PositRepositoryImpl.PositRepositoryImpl.insertPosit')
def test_posit_repository_insert_posit(mock_insert_posit):

    test_data = 'Posit insertado correctamente'
    
    mock_insert_posit.return_value = test_data

    posit_repository = PositRepositoryImpl.PositRepositoryImpl()

    result = posit_repository.insertPosit(PositEntity.PositEntity(1, 'Prueba', 1))

    assert result == 'Posit insertado correctamente'
    
@mock.patch('PositRepositoryImpl.PositRepositoryImpl.deletePosit')
def test_posit_repository_delete_posit(mock_delete_posit):

    posit = PositEntity.PositEntity(1, 'Prueba', 1)
    test_data = 'Posit borrado con el id: ' + str(posit.getId())
    
    mock_delete_posit.return_value = test_data

    posit_repository = PositRepositoryImpl.PositRepositoryImpl()

    result = posit_repository.deletePosit(posit.getId())

    assert result == 'Posit borrado con el id: ' + str(posit.getId())

@mock.patch('PositRepositoryImpl.PositRepositoryImpl.updatePosit')
def test_posit_repository_update_posit(mock_update_posit):

    test_data = 'Posit actualizado correctamente'
    
    mock_update_posit.return_value = test_data

    posit_repository = PositRepositoryImpl.PositRepositoryImpl()

    result = posit_repository.updatePosit(PositEntity.PositEntity(1, 'Prueba', 2))

    assert result == 'Posit actualizado correctamente'

@mock.patch('TaskRepositoryImpl.TaskRepositoryImpl.getAll')
def test_task_repository_get_all(mock_get_all):

    posit = PositEntity.PositEntity(1, 'Prueba', 1)
    management = ManagementEntity.ManagementEntity(1, 'Prueba', 'Prueba')
    
    test_data = [
    {"id": 1, "name": "Elemento 1", "description": "Descripcion", "positEntity": posit, "managementEntity": management, "startDate": "10-10-2023", "endDate": "11-10-2023", "status": "Fuera de plazo"},
    {"id": 2, "name": "Elemento 2", "description": "Descripcion", "positEntity": posit, "managementEntity": management, "startDate": "10-11-2023", "endDate": "11-12-2023", "status": "Fuera de plazo"}
    ]
    
    mock_get_all.return_value = test_data

    task_repository = TaskRepositoryImpl.TaskRepositoryImpl()

    result = task_repository.getAll()

    assert result == test_data

@mock.patch('TaskRepositoryImpl.TaskRepositoryImpl.getById')
def test_task_repository_get_by_id(mock_get_by_id):

    posit = PositEntity.PositEntity(1, 'Prueba', 1)
    management = ManagementEntity.ManagementEntity(1, 'Prueba', 'Prueba')

    test_data = TaskEntity.TaskEntity(1, 'Prueba', 'Prueba', posit, management, '20-06-1999', '20-07-1999', 'Pendiente')
    
    mock_get_by_id.return_value = test_data

    task_repository = TaskRepositoryImpl.TaskRepositoryImpl()

    result = task_repository.getById(1)

    assert result == test_data

@mock.patch('TaskRepositoryImpl.TaskRepositoryImpl.insertTask')
def test_task_repository_insert_task(mock_insert_task):

    posit = PositEntity.PositEntity(1, 'Prueba', 1)
    management = ManagementEntity.ManagementEntity(1, 'Prueba', 'Prueba')

    test_data = 'Tarea insertada correctamente'
    
    mock_insert_task.return_value = test_data

    task_repository = TaskRepositoryImpl.TaskRepositoryImpl()

    result = task_repository.insertTask(TaskEntity.TaskEntity(1, 'Prueba', 'Prueba', posit, management, '20-06-1999', '20-07-1999', 'Pendiente'))

    assert result == 'Tarea insertada correctamente'
    
@mock.patch('TaskRepositoryImpl.TaskRepositoryImpl.deleteTask')
def test_task_repository_delete_task(mock_delete_task):

    posit = PositEntity.PositEntity(1, 'Prueba', 1)
    management = ManagementEntity.ManagementEntity(1, 'Prueba', 'Prueba')
    task = TaskEntity.TaskEntity(1, 'Prueba', 'Prueba', posit, management, '20-06-1999', '20-07-1999', 'Pendiente')

    test_data = 'Tarea borrada con el id: ' + str(task.getId())
    
    mock_delete_task.return_value = test_data

    task_repository = TaskRepositoryImpl.TaskRepositoryImpl()

    result = task_repository.deleteTask(task.getId())

    assert result == 'Tarea borrada con el id: ' + str(task.getId())

@mock.patch('TaskRepositoryImpl.TaskRepositoryImpl.updateTask')
def test_task_repository_update_task(mock_update_task):
    posit = PositEntity.PositEntity(1, 'Prueba', 1)
    management = ManagementEntity.ManagementEntity(1, 'Prueba', 'Prueba')
    test_data = 'Tarea actualizada correctamente'
    
    mock_update_task.return_value = test_data

    task_repository = TaskRepositoryImpl.TaskRepositoryImpl()

    result = task_repository.updateTask(TaskEntity.TaskEntity(1, 'Prueba', 'Prueba', posit, management, '20-06-1999', '20-07-1999', 'Pendiente'))

    assert result == 'Tarea actualizada correctamente'