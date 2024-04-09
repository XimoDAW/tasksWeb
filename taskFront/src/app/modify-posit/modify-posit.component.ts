import { Component } from '@angular/core';
import { Router, ActivatedRoute } from '@angular/router';
import { PositServiceService } from '../Services/posit-service.service';
import { PositCreate } from '../Models/posit-create';

@Component({
  selector: 'app-modify-posit',
  templateUrl: './modify-posit.component.html',
  styleUrls: ['./modify-posit.component.css']
})
export class ModifyPositComponent {
  constructor(private positService: PositServiceService, private router: Router, private activeRoute: ActivatedRoute) { }

  positCreate: PositCreate = {
    name: ''
  }

  id!: number
  name!: string;
  idManagement!: number

  ngOnInit() {
    this.activeRoute.queryParams.subscribe(params => {
      this.idManagement = parseInt(params['idManagement'])
      this.id = parseInt(params['idPosit'])
    })
  }

  modify() {
    this.positCreate.name = this.name
    console.log(this.positCreate)

    this.positService.putPosit(this.positCreate, this.id)
      .subscribe({
        next: dato => {
          console.log(`${dato}`)
          this.router.navigate(['/posits'], { queryParams: { idManagement: this.idManagement } })
        },
        error: error => alert("Error al modificar el posit")
      })
  }

  cancel() {
    this.router.navigate(['/posits'], { queryParams: { idManagement: this.idManagement } })
  }
}
