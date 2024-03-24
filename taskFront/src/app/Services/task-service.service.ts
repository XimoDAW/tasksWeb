import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { Task } from '../Models/task';

@Injectable({
  providedIn: 'root'
})
export class TaskServiceService {

  constructor(private taskServer: HttpClient) { }

  url = "http://127.0.0.1:5000/tasks"

  getAllTasks(): Observable<Task[]> {
    return this.taskServer.get<Task[]>(this.url)

  }
  
}
