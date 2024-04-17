import { Component } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { TaskServiceService } from '../Services/task-service.service';

@Component({
  selector: 'app-delete-task',
  templateUrl: './delete-task.component.html',
  styleUrls: ['./delete-task.component.css']
})
export class DeleteTaskComponent {
  constructor(private taskService: TaskServiceService, private activeRoute: ActivatedRoute, private router: Router) { }
  idManagement!: number
  idPosit!: number
  id!:number

  ngOnInit() {
    this.activeRoute.queryParams.subscribe(params => {
      this.idManagement = params['idManagement']
      this.idPosit = params['idPosit']
    })
    this.id = this.activeRoute.snapshot.params['id']
    console.log(this.idPosit)
  }

  deleteTask() {
    this.taskService.deleteTask(this.id).subscribe(response => {
      this.router.navigate(['/tasks'], { queryParams: { idPosit: this.idPosit, idManagement: this.idManagement } })
    })
  }

  cancelDelete() {
    this.router.navigate(['/tasks'], { queryParams: { idPosit: this.idPosit, idManagement: this.idManagement } })

  }
}
