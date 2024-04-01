import { Component } from '@angular/core';
import { PositServiceService } from '../Services/posit-service.service';
import { ActivatedRoute, Router } from '@angular/router';
import { Posit } from '../Models/posit';
import { ErrorComponent } from '../error/error.component';

@Component({
  selector: 'app-add-posit',
  templateUrl: './add-posit.component.html',
  styleUrls: ['./add-posit.component.css']
})
export class AddPositComponent {
  constructor(private positService: PositServiceService, private router: Router, private activeRoute: ActivatedRoute) { }


  posit: Posit = {
    "id": 0,
    "name": "",
    "managementId": 0
  }

  name!: string
  idManagement!: number

  ngOnInit() {
    this.activeRoute.queryParams.subscribe(params => {
      this.idManagement = params['idManagement']
    })
  }

  add() {
    this.posit.name = this.name
    this.posit.managementId = this.idManagement
    this.positService.addPosit(this.posit)
      .subscribe({
        next: dato => {
          console.log(`${dato}`)
          this.router.navigate(['/posits'], { queryParams: { idManagement: this.idManagement } })
        },
        error: error => alert("Usuario o contraseña incorrectos")
      })
  }

  cancel() {
    this.router.navigate(['/posits'], { queryParams: { idManagement: this.idManagement } })
  }
}
