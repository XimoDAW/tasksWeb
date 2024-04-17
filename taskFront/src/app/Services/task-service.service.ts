import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { Task } from '../Models/task';
import { TaskCreate } from '../Models/task-create';

@Injectable({
  providedIn: 'root'
})
export class TaskServiceService {

  constructor(private taskServer: HttpClient) { }

  url = "http://127.0.0.1:5000/tasks"

  getAllTasks(positId: number): Observable<Task[]> {
    return this.taskServer.get<Task[]>(this.url + '?positId=' + positId)

  }

  getTaskById(id: number): Observable<Task> {
    return this.taskServer.get<Task>(this.url + "/" + id)
  }

  addTask(task: TaskCreate): Observable<TaskCreate> {
    return this.taskServer.post<TaskCreate>(this.url, task)

  }

  deleteTask(id: number): Observable<Task> {
    return this.taskServer.delete<Task>(this.url + '/' + id)

  }

  putTask(task: TaskCreate, id: number): Observable<TaskCreate> {
    return this.taskServer.put<TaskCreate>(this.url + '/' + id, task)
  }

}
