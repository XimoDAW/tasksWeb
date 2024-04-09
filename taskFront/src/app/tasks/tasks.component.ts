import { Component } from '@angular/core';
import { Task } from '../Models/task';
import { TaskServiceService } from '../Services/task-service.service';
import { ActivatedRoute, Router } from '@angular/router';

@Component({
  selector: 'app-tasks',
  templateUrl: './tasks.component.html',
  styleUrls: ['./tasks.component.css']
})
export class TasksComponent {
  constructor(private taskService: TaskServiceService, private activeRoute: ActivatedRoute, private router: Router) { }
  tasks!: Task[]
  idPosit!: number
  idManagement!: number
  task: Task = {
    "id": 0,
    "name": '',
    "description": '',
    "positId": 0,
    "managementId": 0,
    "startDate": '',
    "endDate": '',
    "status": ''
  }

  ngOnInit() {
    this.activeRoute.queryParams.subscribe(params => {
      this.idPosit = params['idPosit']
      this.idManagement = params['idManagement']
    })
    this.taskService.getAllTasks(this.idPosit).subscribe(tasks => {
      console.log(tasks)
      this.tasks = []
      const tasksLength = tasks.length

      for (let i = 0; i < tasksLength; i++) {
        let dato = JSON.stringify(tasks[i]).slice(1, -1)
        let indexPoint = dato.indexOf(',')
        let indexId = dato.indexOf(':')
        let indexName = dato.indexOf(':', indexId + 1)
        let indexPoint2 = dato.indexOf(',', indexPoint + 1)
        let id = parseInt(dato.slice(indexId + 2, indexPoint))
        let name = dato.slice(indexName + 4, indexPoint2 - 2)

        this.task.id = id
        this.task.name = name
        this.task.managementId = this.idManagement

        this.tasks.push(this.task)
      }
    })
  }

  return() {
    this.router.navigate(['posits'], { queryParams: { idManagement: this.idManagement } })
  }

  view(id: number) {
    this.router.navigate(['tasks/view/' + id])
  }

  modifyTask(id: number) {
    this.router.navigate(['tasks/modify/' + id])
  }

  deleteTask(id: number) {
    this.router.navigate(['tasks/' + id])
  }

  addTask() {
    this.router.navigate(['tasks/add'], { queryParams: { idPosit: this.idPosit, idManagement: this.idManagement } })
  }
}
