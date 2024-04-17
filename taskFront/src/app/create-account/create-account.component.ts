import { Component } from '@angular/core';
import { ManagementServiceService } from '../Services/management-service.service';
import { ActivatedRoute, Router } from '@angular/router';
import { Management } from '../Models/management';

@Component({
  selector: 'app-create-account',
  templateUrl: './create-account.component.html',
  styleUrls: ['./create-account.component.css']
})
export class CreateAccountComponent {
  constructor(private managementService: ManagementServiceService, private router: Router, private activeRoute: ActivatedRoute) { }

  name!:string
  password!:string

  create() {
    let management:Management = {
      id: 0,
      user: '',
      password: ''
    }

    management.user = this.name
    management.password = this.password
    
    this.managementService.createManagement(management)
      .subscribe({
        next: dato => {
          console.log(`${dato}`)
          this.router.navigate(['/'])
        },
        error: error => alert("Error al crear el usuario")
      })
  }

  cancel() {
    this.router.navigate(['/'])
  }
}
