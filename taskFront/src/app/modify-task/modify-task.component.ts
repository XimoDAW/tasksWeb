import { Component } from '@angular/core';
import { Router, ActivatedRoute } from '@angular/router';
import { PositCreate } from '../Models/posit-create';
import { TaskServiceService } from '../Services/task-service.service';
import { TaskCreate } from '../Models/task-create';

@Component({
  selector: 'app-modify-task',
  templateUrl: './modify-task.component.html',
  styleUrls: ['./modify-task.component.css']
})
export class ModifyTaskComponent {
  constructor(private taskService: TaskServiceService, private router: Router, private activeRoute: ActivatedRoute) { }

  id!: number
  name!: string;
  description!: string;
  idPosit!: number
  idManagement!: number
  startDate!: string;
  endDate!: string;


  ngOnInit() {
    this.activeRoute.queryParams.subscribe(params => {
      this.idManagement = parseInt(params['idManagement'])
      this.idPosit = parseInt(params['idPosit'])
    })
    this.id = this.activeRoute.snapshot.params['id']
    console.log(this.id)
  }

  modify() {
    let taskCreate: TaskCreate = {
      name: '',
      description: '',
      positId: 0,
      managementId: 0,
      startDate: '',
      endDate: ''
    }

    taskCreate.name = this.name
    taskCreate.description = this.description
    taskCreate.managementId = this.idManagement
    taskCreate.positId = this.idPosit
    let dateOrder = this.startDate.split('-')
    taskCreate.startDate = dateOrder[2] + '-' + dateOrder [1] + '-' + dateOrder[0]
    dateOrder = this.endDate.split('-')
    taskCreate.endDate = dateOrder[2] + '-' + dateOrder [1] + '-' + dateOrder[0]
    console.log(taskCreate)

    this.taskService.putTask(taskCreate, this.id)
      .subscribe({
        next: dato => {
          console.log(`${dato}`)
          this.router.navigate(['/posits'], { queryParams: { idManagement: this.idManagement } })
        },
        error: error => alert("Error al modificar el posit")
      })
  }

  cancel() {
    this.router.navigate(['/posits'], { queryParams: { idManagement: this.idManagement } })
  }
}
