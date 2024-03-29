import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { MainComponent } from './main/main.component';
import { PositsComponent } from './posits/posits.component';
import { Guard1Guard } from './Guards/guard1.guard';
import { ErrorUsuarioComponent } from './error-usuario/error-usuario.component';

const routes: Routes = [
  { path: '', component: MainComponent },
  { path: 'posits', canActivate:[Guard1Guard], component: PositsComponent },
  { path: '**', component: ErrorUsuarioComponent }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
