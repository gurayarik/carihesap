import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { CariKart } from '../models/cari-kart';

@Injectable({
  providedIn: 'root',
})
export class CariKartService {
  private apiUrl = 'http://localhost:8000/cari-kartlar';

  constructor(private http: HttpClient) {}

  list(): Observable<CariKart[]> {
    return this.http.get<CariKart[]>(this.apiUrl);
  }

  create(kart: Omit<CariKart, 'id'>): Observable<CariKart> {
    return this.http.post<CariKart>(this.apiUrl, kart);
  }

  delete(id: number): Observable<CariKart> {
    return this.http.delete<CariKart>(`${this.apiUrl}/${id}`);
  }
}
