import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class MainServiceService {

  constructor(private mainServer: HttpClient) { }

  url = "http://127.0.0.1:5000/"

  getMain(): Observable<string> {
    return this.mainServer.get<string>(this.url)

  }
}
