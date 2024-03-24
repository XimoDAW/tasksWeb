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
    this.positService.getAllPosits().subscribe(posits => {
      this.posits = posits
      const positsLength = posits.length

      for (let i = 0; i < positsLength; i++) {
        let dato = JSON.stringify(posits[i]).slice(1, -1)
        let indexPoint = dato.indexOf(',')
        let indexId = dato.indexOf(':')
        let indexName = dato.indexOf(':', indexId + 1)

        let id = parseInt(dato.slice(indexId + 2, indexPoint))
        let name = dato.slice(indexName + 4, -3)

        let posit:Posit = {
          "id":id,
          "name":name
        }

        this.posits.push(posit)
      }
    })
  }
}
