import { Component } from '@angular/core';
import { Task } from '../Models/task';
import { TaskServiceService } from '../Services/task-service.service';

@Component({
  selector: 'app-tasks',
  templateUrl: './tasks.component.html',
  styleUrls: ['./tasks.component.css']
})
export class TasksComponent {
  constructor(private taskService: TaskServiceService) { }
  tasks!: Task[]

  ngOnInit() {
    this.taskService.getAllTasks(1).subscribe(tasks => {
      this.tasks = tasks
      const tasksLength = tasks.length

      for (let i = 0; i < tasksLength; i++) {
        let dato = JSON.stringify(tasks[i]).slice(1, -1)
        let indexPoint = dato.indexOf(',')
        let indexId = dato.indexOf(':')
        let indexName = dato.indexOf(':', indexId + 1)

        let id = parseInt(dato.slice(indexId + 2, indexPoint))
        let name = dato.slice(indexName + 4, -3)

        let task:Task = {
          "id": id,
          "name": name,
          description: '',
          idPosit: 0,
          idManagement: 0,
          dateStart: '',
          dateEnd: '',
          status: ''
        }

        this.tasks.push(task)
        console.log(task)
      }
    })
  }
}
