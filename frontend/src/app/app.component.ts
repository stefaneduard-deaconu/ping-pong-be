import { Component, signal, ChangeDetectionStrategy, ViewEncapsulation } from "@angular/core";
import { PingService } from "./ping.service";

interface Player {
  id: number;
  name: string;
}

interface PlayersResponse {
  players: Player[];
}

@Component({
  selector: "app-root",
  standalone: true,
  imports: [],
  templateUrl: "./app.component.html",
  changeDetection: ChangeDetectionStrategy.OnPush,
  encapsulation: ViewEncapsulation.None,
})
export class AppComponent {
  playersData = signal<PlayersResponse | null>(null);
  loading = signal(false);
  error = signal<string | null>(null);

  constructor(private ping: PingService) {}

  callPing() {
    this.loading.set(true);
    this.error.set(null);
    this.ping.getPing().subscribe({
      next: (res) => {
        this.playersData.set(res as PlayersResponse);
        this.loading.set(false);
      },
      error: (err) => {
        this.error.set(err.message || "Request failed");
        this.loading.set(false);
      },
    });
  }
}
