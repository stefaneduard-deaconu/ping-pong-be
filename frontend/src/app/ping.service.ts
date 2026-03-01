import { Injectable } from "@angular/core";
import { HttpClient } from "@angular/common/http";
import { Observable } from "rxjs";
import { environment } from "../environments/environment";

@Injectable({ providedIn: "root" })
export class PingService {
  private base = environment.apiBase;
  constructor(private http: HttpClient) {}

  getPing(): Observable<object> {
    return this.http.get<object>(`${this.base}/players`);
  }
}
