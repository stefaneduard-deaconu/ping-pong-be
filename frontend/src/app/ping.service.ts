import { Injectable } from "@angular/core";
import { HttpClient } from "@angular/common/http";
import { Observable, map } from "rxjs";
import { environment } from "../environments/environment";

@Injectable({ providedIn: "root" })
export class PingService {
  private base = environment.apiBase;
  constructor(private http: HttpClient) {}

  getPing(): Observable<string> {
    return this.http.get(`${this.base}/players`, {
      responseType: "application/json",
    });
  }
}
