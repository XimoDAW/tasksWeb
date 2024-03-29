import { Component } from '@angular/core';
import { ManagementServiceService } from '../Services/management-service.service';
import { Management } from '../Models/management';

@Component({
  selector: 'app-management',
  templateUrl: './management.component.html',
  styleUrls: ['./management.component.css']
})
export class ManagementComponent {
  constructor(private managementService: ManagementServiceService) { }
  management: Management = {
    id: 0,
    user: '',
    password: ''
  }

  ngOnInit() {
    //Dentro del getAllPosits iria el usuario
    this.managementService.getManagementById(1).subscribe(management => {
        let dato = JSON.stringify(management).slice(1, -1)
        let indexPoint1 = dato.indexOf(',')
        let indexId = dato.indexOf(':')
        let indexUser = dato.indexOf(':', indexId + 1)
        let indexPassword = dato.indexOf(':', indexUser + 1)
        let indexPoint2 = dato.indexOf(',', indexPoint1 + 1)

        let id = parseInt(dato.slice(indexId + 2, indexPoint1))
        console.log(id)
        let user = dato.slice(indexUser + 4, indexPoint2 -2)
        console.log(user)
        let password = dato.slice(indexPassword +4, -3)
        console.log(password)

           
    })
  }
}
