import { Component } from '@angular/core';
import { Router } from '@angular/router';

@Component({
  selector: 'app-error-usuario',
  templateUrl: './error-usuario.component.html',
  styleUrls: ['./error-usuario.component.css']
})
export class ErrorUsuarioComponent {
  constructor(private router:Router){}

  inicio() {
    this.router.navigate(['/'])
  }
}
