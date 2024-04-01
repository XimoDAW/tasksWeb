import { Component } from '@angular/core';
import { TaskServiceService } from '../Services/task-service.service';
import { ActivatedRoute, Router } from '@angular/router';

@Component({
  selector: 'app-task-detail',
  templateUrl: './task-detail.component.html',
  styleUrls: ['./task-detail.component.css']
})
export class TaskDetailComponent {
  constructor(private taskService: TaskServiceService, private activeRoute: ActivatedRoute, private router: Router) { }
  id!:number

  ngOnInit() {
    this.id = this.activeRoute.snapshot.params['id']

    this.taskService.getTaskById(this.id).subscribe(task => {
      console.log(task)
    })
  }
}
