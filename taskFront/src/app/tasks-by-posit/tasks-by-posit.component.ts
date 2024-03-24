import { Component } from '@angular/core';
import { PositServiceService } from '../Services/posit-service.service';
import { TaskServiceService } from '../Services/task-service.service';

@Component({
  selector: 'app-tasks-by-posit',
  templateUrl: './tasks-by-posit.component.html',
  styleUrls: ['./tasks-by-posit.component.css']
})
export class TasksByPositComponent {
  constructor(private positService: PositServiceService, private taskService: TaskServiceService){}

  
}
