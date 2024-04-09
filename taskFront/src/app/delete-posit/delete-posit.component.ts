import { Component } from '@angular/core';
import { PositServiceService } from '../Services/posit-service.service';
import { ActivatedRoute, Router } from '@angular/router';

@Component({
  selector: 'app-delete-posit',
  templateUrl: './delete-posit.component.html',
  styleUrls: ['./delete-posit.component.css']
})
export class DeletePositComponent {
  constructor(private positService: PositServiceService, private activeRoute: ActivatedRoute, private router: Router) { }
  idManagement!: number
  idPosit!: number

  ngOnInit() {
    this.activeRoute.queryParams.subscribe(params => {
      this.idManagement = params['idManagement']
      this.idPosit = params['idPosit']
    })
  }

  deletePosit() {
    this.positService.deletePosit(this.idPosit).subscribe(response => {
      this.router.navigate(['/posits'], { queryParams: { idManagement: this.idManagement } })
    })
  }

  cancelDelete() {
    this.router.navigate(['/posits'], { queryParams: { idManagement: this.idManagement } })

  }

}
