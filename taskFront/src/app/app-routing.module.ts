import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { MainComponent } from './main/main.component';
import { PositsComponent } from './posits/posits.component';
import { Guard1Guard } from './Guards/guard1.guard';
import { ErrorUsuarioComponent } from './error-usuario/error-usuario.component';
import { AddPositComponent } from './add-posit/add-posit.component';
import { TasksComponent } from './tasks/tasks.component';
import { TaskDetailComponent } from './task-detail/task-detail.component';
import { DeletePositComponent } from './delete-posit/delete-posit.component';
import { AddTaskComponent } from './add-task/add-task.component';
import { ModifyTaskComponent } from './modify-task/modify-task.component';
import { ModifyPositComponent } from './modify-posit/modify-posit.component';
import { DeleteTaskComponent } from './delete-task/delete-task.component';

const routes: Routes = [
  { path: '', component: MainComponent },
  { path: 'posits', canActivate: [Guard1Guard], component: PositsComponent },
  { path: 'tasks', canActivate: [Guard1Guard], component: TasksComponent },
  { path: 'tasks/view/:id', canActivate: [Guard1Guard], component: TaskDetailComponent },
  { path: 'posits/add', canActivate: [Guard1Guard], component: AddPositComponent },
  { path: 'tasks/add', canActivate: [Guard1Guard], component: AddTaskComponent },
  { path: 'posits/:id', canActivate: [Guard1Guard], component: DeletePositComponent },
  { path: 'tasks/:id', canActivate: [Guard1Guard], component: DeleteTaskComponent },
  { path: 'tasks/modify/:id', canActivate: [Guard1Guard], component: ModifyTaskComponent },
  { path: 'posits/modify/:id', canActivate: [Guard1Guard], component: ModifyPositComponent },
  { path: '**', component: ErrorUsuarioComponent }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
