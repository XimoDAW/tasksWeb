import { Component } from '@angular/core';
import { Posit } from '../Models/posit';
import { PositServiceService } from '../Services/posit-service.service';

@Component({
  selector: 'app-posits',
  templateUrl: './posits.component.html',
  styleUrls: ['./posits.component.css']
})
export class PositsComponent {

  constructor(private positService: PositServiceService) { }
  posits!: Posit[]

  ngOnInit() {
    //Dentro del getAllPosits iria el usuario
    this.positService.getAllPosits(1).subscribe(posits => {
      this.posits = []
      const positsLength = posits.length

      for (let i = 0; i < positsLength; i++) {
        let dato = JSON.stringify(posits[i]).slice(1, -1)
        let indexPoint1 = dato.indexOf(',')
        let indexId = dato.indexOf(':')
        let indexName = dato.indexOf(':', indexId + 1)
        let indexManagementId = dato.indexOf(':', indexName + 1)
        let indexPoint2 = dato.indexOf(',', indexPoint1 + 1)

        let id = parseInt(dato.slice(indexId + 2, indexPoint1))
        let name = dato.slice(indexName + 4, indexPoint2 -2)
        let managementId = parseInt(dato.slice(indexManagementId +2, -1))

        let posit:Posit = {
          "id":id,
          "name":name,
          "managementId":managementId
        }

        this.posits.push(posit)
      }
    })
  }
}
