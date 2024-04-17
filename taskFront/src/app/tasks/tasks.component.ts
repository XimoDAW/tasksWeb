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


  ngOnInit() {
    this.activeRoute.queryParams.subscribe(params => {
      this.idPosit = params['idPosit']
      this.idManagement = params['idManagement']
    })
    this.taskService.getAllTasks(this.idPosit).subscribe(response => {
      this.tasks = []
      const tasksLength = response.length

      for (let i = 0; i < tasksLength; i++) {
        let dato = JSON.stringify(response[i]).slice(1, -1)
        let indexPoint = dato.indexOf(',')
        let indexId = dato.indexOf(':')
        let indexName = dato.indexOf(':', indexId + 1)
        let indexPoint2 = dato.indexOf(',', indexPoint + 1)
        let id = parseInt(dato.slice(indexId + 2, indexPoint))
        let name = dato.slice(indexName + 4, indexPoint2 - 2)

        let task: Task = {
          "id": id,
          "name": name,
          "description": '',
          "positId": 0,
          "managementId": 0,
          "startDate": '',
          "endDate": '',
          "status": ''
        }

        this.tasks.push(task)
      }
    })
  }

  return() {
    this.router.navigate(['posits'], { queryParams: { idManagement: this.idManagement } })
  }

  view(id: number) {
    this.router.navigate(['tasks/view/' + id], { queryParams: { idPosit: this.idPosit, idManagement: this.idManagement } })
  }

  modifyTask(id: number) {
    this.router.navigate(['tasks/modify/' + id], { queryParams: { idPosit: this.idPosit, idManagement: this.idManagement } })
  }

  deleteTask(id: number) {
    this.router.navigate(['tasks/' + id], { queryParams: { idPosit: this.idPosit, idManagement: this.idManagement } })
  }

  addTask() {
    this.router.navigate(['tasks/add'], { queryParams: { idPosit: this.idPosit, idManagement: this.idManagement } })
  }
}
