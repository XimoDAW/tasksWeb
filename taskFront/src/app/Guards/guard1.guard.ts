import { Injectable } from '@angular/core';
import { ActivatedRoute, ActivatedRouteSnapshot, CanActivate, Router, RouterStateSnapshot, UrlTree } from '@angular/router';
import { Observable } from 'rxjs';
import { ManagementServiceService } from '../Services/management-service.service';

@Injectable({
  providedIn: 'root'
})
export class Guard1Guard implements CanActivate {
  constructor(private router: Router,
    private activeRoute: ActivatedRoute) { }
  validate = false
  canActivate(
    route: ActivatedRouteSnapshot,
    state: RouterStateSnapshot): Observable<boolean | UrlTree> | Promise<boolean | UrlTree> | boolean | UrlTree {
    let idManagement


    this.activeRoute.queryParams.subscribe(params => {
      idManagement = params['idManagement']
    })

    if (this.validate) {
      return true
    }else {
      this.router.navigate(['error'])
      return false
    }
  }

  isConnect(validate: boolean) {
    if (validate)
      this.validate = true
  }
}
