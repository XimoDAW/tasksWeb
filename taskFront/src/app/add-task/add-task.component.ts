import { Component } from '@angular/core';
import { TaskServiceService } from '../Services/task-service.service';
import { ActivatedRoute, Router } from '@angular/router';
import { TaskCreate } from '../Models/task-create';

@Component({
  selector: 'app-add-task',
  templateUrl: './add-task.component.html',
  styleUrls: ['./add-task.component.css']
})
export class AddTaskComponent {
  constructor(private taskService: TaskServiceService, private router: Router, private activeRoute: ActivatedRoute) { }

  task: TaskCreate = {
    name: '',
    description: '',
    idPosit: 0,
    idManagement: 0,
    startDate: '',
    endDate: ''
  }

  name!: string
  description!: string
  idPosit!: number
  idManagement!: number
  dateStart!: string
  dateEnd!: string

  ngOnInit() {
    this.activeRoute.queryParams.subscribe(params => {
      this.idManagement = parseInt(params['idManagement'])
      this.idPosit = parseInt(params['idPosit'])
    })
  }

  add() {
    this.task.name = this.name
    this.task.description = this.description
    this.task.idPosit = this.idPosit
    this.task.idManagement = this.idManagement
    let dateOrder = this.dateStart.split('-')
    this.task.startDate = dateOrder[2] + '-' + dateOrder [1] + '-' + dateOrder[0]
    dateOrder = this.dateEnd.split('-')
    this.task.endDate = dateOrder[2] + '-' + dateOrder [1] + '-' + dateOrder[0]
    console.log(this.task)
    this.taskService.addTask(this.task)
      .subscribe({
        next: dato => {
          console.log(`${dato}`)
          this.router.navigate(['/tasks'], { queryParams: { idPosit: this.idPosit, idManagement: this.idManagement } })
        },
        error: error => alert("Error al añadir la tarea")
      })
  }

  cancel() {
    this.router.navigate(['/tasks'], { queryParams: { idPosit: this.idPosit, idManagement: this.idManagement } })
  }
}
