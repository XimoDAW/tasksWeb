import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { Management } from '../Models/management';

@Injectable({
  providedIn: 'root'
})
export class ManagementServiceService {
    constructor(private managementServer: HttpClient) { }

    url = "http://127.0.0.1:5000/management"
  
    getManagementByUserAndPassword(user:string, password:string): Observable<Management[]> {
      return this.managementServer.get<Management[]>(this.url + '?user=' + user + '&password=' + password)
      
    }

    createManagement(management: Management): Observable<Management> {
      return this.managementServer.post<Management>(this.url, management)
  
    }
  
    deleteManagement(id: number): Observable<Management> {
      return this.managementServer.delete<Management>(this.url + '/' + id)
  
    }
  }