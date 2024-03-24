import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { Posit } from '../Models/posit';

@Injectable({
  providedIn: 'root'
})
export class PositServiceService {

  constructor(private positServer: HttpClient) { }

  url = "http://127.0.0.1:5000/posits"

  getAllPosits(): Observable<Posit[]> {
    return this.positServer.get<Posit[]>(this.url)

  }
}
