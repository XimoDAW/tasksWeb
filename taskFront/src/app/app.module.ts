import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { HttpClientModule } from '@angular/common/http';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { FormsModule } from '@angular/forms';
import { TasksComponent } from './tasks/tasks.component';
import { PositsComponent } from './posits/posits.component';
import { MainComponent } from './main/main.component';
import { TasksByPositComponent } from './tasks-by-posit/tasks-by-posit.component';
import { ErrorComponent } from './error/error.component';
import { ErrorUsuarioComponent } from './error-usuario/error-usuario.component';

@NgModule({
  declarations: [
    AppComponent,
    TasksComponent,
    PositsComponent,
    MainComponent,
    TasksByPositComponent,
    ErrorComponent,
    ErrorUsuarioComponent
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
