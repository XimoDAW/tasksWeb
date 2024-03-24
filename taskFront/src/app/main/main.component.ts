import { Component } from '@angular/core';
import { MainServiceService } from '../Services/main-service.service';

@Component({
  selector: 'app-main',
  templateUrl: './main.component.html',
  styleUrls: ['./main.component.css']
})
export class MainComponent {
  
  constructor(private mainService: MainServiceService) { }
  main!:string

  ngOnInit() {
    this.mainService.getMain().subscribe(response => {
      console.log(response)
      this.main = response
      
    })
  }
}
