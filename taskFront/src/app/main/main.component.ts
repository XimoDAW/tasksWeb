import { Component } from '@angular/core';
import { MainServiceService } from '../Services/main-service.service';
import { ManagementServiceService } from '../Services/management-service.service';
import { Management } from '../Models/management';
import { ActivatedRoute, Router } from '@angular/router';
import { Guard1Guard } from '../Guards/guard1.guard';

@Component({
  selector: 'app-main',
  templateUrl: './main.component.html',
  styleUrls: ['./main.component.css']
})
export class MainComponent {

  constructor(private mainService: MainServiceService, private managementService: ManagementServiceService, private router: Router, private activeRoute: ActivatedRoute, private guard: Guard1Guard) { }
  main!: string
  user!: string
  password!: string
  validate = false
  management: Management = {
    "id": 0,
    "user": "",
    "password": ""
  }

  ngOnInit() {
    this.mainService.getMain().subscribe(response => {
      this.main = response
    })
  }

  checkUser() {
    this.managementService.getManagementByUserAndPassword(this.user, this.password).subscribe({
      next: datos => {
        let managementString = JSON.stringify(datos)
        let index = managementString.indexOf(':')
        let index2 = managementString.indexOf(',')
        let id = parseInt(managementString.slice(index + 2, index2))
        this.validate = true
        this.guard.isConnect(this.validate)
        this.router.navigate(['posits'], { queryParams: { idManagement: id } })
      },
      error: error => alert("Usuario o contraseña incorrectos")
    })

  }
}
