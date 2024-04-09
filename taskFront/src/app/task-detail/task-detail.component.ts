import { Component } from '@angular/core';
import { TaskServiceService } from '../Services/task-service.service';
import { ActivatedRoute, Router } from '@angular/router';
import { Task } from '../Models/task';

@Component({
  selector: 'app-task-detail',
  templateUrl: './task-detail.component.html',
  styleUrls: ['./task-detail.component.css']
})
export class TaskDetailComponent {
  constructor(private taskService: TaskServiceService, private activeRoute: ActivatedRoute, private router: Router) { }
  id!:number

  task:Task= {
    id: 0,
    name: '',
    description: '',
    idPosit: 0,
    idManagement: 0,
    startDate: '',
    endDate: '',
    status: ''
  }

  ngOnInit() {
    this.id = this.activeRoute.snapshot.params['id']

    this.taskService.getTaskById(this.id).subscribe(response => {
      let dato = JSON.stringify(response).slice(1, -1)
      let indexPoint = dato.indexOf(',')
      let indexPoint2 = dato.indexOf(',', indexPoint + 1)
      let indexPoint3 = dato.indexOf(',', indexPoint2 + 1)
      let indexPoint4 = dato.indexOf(',', indexPoint3 + 1)
      let indexPoint5 = dato.indexOf(',', indexPoint4 + 1)
      let indexPoint6 = dato.indexOf(',', indexPoint5 + 1)
      let indexPoint7 = dato.indexOf(',', indexPoint6 + 1)
      let indexPoint8 = dato.indexOf(',', indexPoint7 + 1)
      let indexPoint9 = dato.indexOf(',', indexPoint8 + 1)
      let indexPoint10 = dato.indexOf(',', indexPoint9 + 1)
      let indexPoint11 = dato.indexOf(',', indexPoint10 + 1)
      let indexPoint12 = dato.indexOf(',', indexPoint11 + 1)

      let indexId= dato.indexOf(':')
      let indexName = dato.indexOf(':', indexId + 1)
      let indexDescription = dato.indexOf(':', indexName + 1)
      let indexIdPosit1 = dato.indexOf(':', indexDescription + 1)
      let indexIdPosit2 = dato.indexOf(':', indexIdPosit1 + 1)
      let indexIdManagement1 = dato.indexOf(':', indexIdPosit2 + 1)
      let indexIdManagement2 = dato.indexOf(':', indexIdManagement1 + 1)
      let indexStartDate1 = dato.indexOf(':', indexIdManagement2 + 1)
      let indexStartDate2 = dato.indexOf(':', indexStartDate1 + 1)
      let indexStartDate3 = dato.indexOf(':', indexStartDate2 + 1)
      let indexStartDate4 = dato.indexOf(':', indexStartDate3 + 1)
      let indexStartDate5 = dato.indexOf(':', indexStartDate4 + 1)
      let indexEndDate = dato.indexOf(':', indexStartDate5 + 1)
      let indexStatus = dato.indexOf(':', indexEndDate + 1)

      let id = parseInt(dato.slice(indexId + 2, indexPoint))
      let name = dato.slice(indexName + 4, indexPoint2 - 2)
      let description = dato.slice(indexDescription + 4, indexPoint3 - 2)
      let idPosit = parseInt(dato.slice(indexIdPosit2 + 2, indexPoint4))
      let idManagement = parseInt(dato.slice(indexIdManagement2 + 2, indexPoint6-3))
      let startDate = dato.slice(indexStartDate5 + 8, indexPoint10 - 6)
      let endDate = dato.slice(indexEndDate + 8, indexPoint11 - 6)
      let status = dato.slice(indexStatus + 4, indexPoint12 - 2)

      this.task.id = id
      this.task.name = name
      this.task.description = description
      this.task.idPosit = idPosit
      this.task.idManagement = idManagement
      this.task.startDate = startDate
      this.task.endDate = endDate
      this.task.status = status
      console.log(this.task)
    })
  }

  return() {
    this.router.navigate(['/tasks'], { queryParams: { idPosit: this.task.idPosit, idManagement: this.task.idManagement}})
  }
}
