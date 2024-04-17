import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { HttpClientModule } from '@angular/common/http';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { FormsModule } from '@angular/forms';
import { TasksComponent } from './tasks/tasks.component';
import { PositsComponent } from './posits/posits.component';
import { MainComponent } from './main/main.component';
import { ErrorComponent } from './error/error.component';
import { ErrorUsuarioComponent } from './error-usuario/error-usuario.component';
import { AddPositComponent } from './add-posit/add-posit.component';
import { TaskDetailComponent } from './task-detail/task-detail.component';
import { DeletePositComponent } from './delete-posit/delete-posit.component';
import { ModifyPositComponent } from './modify-posit/modify-posit.component';
import { ModifyTaskComponent } from './modify-task/modify-task.component';
import { AddTaskComponent } from './add-task/add-task.component';
import { DeleteTaskComponent } from './delete-task/delete-task.component';
import { HeaderComponent } from './header/header.component';
import { FooterComponent } from './footer/footer.component';
import { DeleteAccountComponent } from './delete-account/delete-account.component';
import { CreateAccountComponent } from './create-account/create-account.component';

@NgModule({
  declarations: [
    AppComponent,
    TasksComponent,
    PositsComponent,
    MainComponent,
    ErrorComponent,
    ErrorUsuarioComponent,
    AddPositComponent,
    TaskDetailComponent,
    DeletePositComponent,
    ModifyPositComponent,
    ModifyTaskComponent,
    AddTaskComponent,
    DeleteTaskComponent,
    HeaderComponent,
    FooterComponent,
    DeleteAccountComponent,
    CreateAccountComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    FormsModule,
    HttpClientModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
