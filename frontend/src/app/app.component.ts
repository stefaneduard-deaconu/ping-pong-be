import { Component } from "@angular/core";
import { PingService } from "./ping.service";

@Component({
  selector: "app-root",
  templateUrl: "./app.component.html",
})
export class AppComponent {
  playersData: object | null = null;
  loading = false;
  error: string | null = null;

  constructor(private ping: PingService) {}

  callPing() {
    this.loading = true;
    this.error = null;
    this.ping.getPing().subscribe({
      next: (res) => {
        this.playersData = res;
        this.loading = false;
      },
      error: (err) => {
        this.error = err.message || "Request failed";
        this.loading = false;
      },
    });
  }
}
