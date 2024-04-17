import { Component } from '@angular/core';
import { ManagementServiceService } from '../Services/management-service.service';
import { ActivatedRoute, Router } from '@angular/router';

@Component({
  selector: 'app-delete-account',
  templateUrl: './delete-account.component.html',
  styleUrls: ['./delete-account.component.css']
})
export class DeleteAccountComponent {
  constructor(private managementService: ManagementServiceService, private activeRoute: ActivatedRoute, private router: Router) { }

  idManagement!:number
  ngOnInit() {
    this.idManagement = this.activeRoute.snapshot.params['id']
  }

  deleteAccount() {
    this.managementService.deleteManagement(this.idManagement).subscribe(response => {
      this.router.navigate(['/'])
    })
  }

  cancelDelete() {
    this.router.navigate(['/posits'], { queryParams: { idManagement: this.idManagement } })

  }
}
