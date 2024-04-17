import { Component } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { ManagementServiceService } from '../Services/management-service.service';

@Component({
  selector: 'app-header',
  templateUrl: './header.component.html',
  styleUrls: ['./header.component.css']
})
export class HeaderComponent {
  constructor(private managementService: ManagementServiceService, private activeRoute: ActivatedRoute, private router: Router) { }
  idManagement !: Number

  ngOnInit() {
    this.activeRoute.queryParams.subscribe(params => {
      this.idManagement = params['idManagement']
    })
  }

  deleteAccount() {
    this.router.navigate(['delete/' + this.idManagement])
  }

}
