# FE-03 — Fetching Data from the Backend

**Goal:** Replace the hardcoded players array with live data loaded from the FastAPI backend.

> **Ce vei învăța / What you'll learn**
> - Ce este un Service în Angular și de ce îl folosim *(what a Service is and why)*
> - `HttpClient` — cum facem un request HTTP GET *(how to make an HTTP GET request)*
> - `signal()` — stare reactivă: template-ul se actualizează automat *(reactive state)*
> - `Observable` și `.subscribe()` *(how to consume an RxJS observable)*

> **Prerequisite:** Backend from BE-01/BE-02 must be running (`uvicorn main:app --reload`)

---

## Concept

**Service** — a class dedicated to fetching data. Keeps HTTP calls out of the component.

```typescript
// player.service.ts
@Injectable({ providedIn: 'root' })
export class PlayerService {
  constructor(private http: HttpClient) {}

  getPlayers() {
    return this.http.get<{ players: Player[] }>('http://localhost:8000/players');
  }
}
```

**Signal** — a reactive variable. When it changes, the template re-renders automatically.

```typescript
players = signal<Player[]>([]);

// update it:
this.players.set(data);

// read it in the template:
// {{ players().length }}
// @for (p of players(); ...)
```

**Subscribe** — triggers the HTTP request and gives you the result:

```typescript
this.playerService.getPlayers().subscribe({
  next: (res) => this.players.set(res.players),
  error: (err) => console.error(err),
});
```

---

## Exercise

The app already has `PingService` — you can rename/edit it or create a new `PlayerService`.

1. Make sure the service has a `getPlayers()` method that calls `GET /players`
2. In `AppComponent`, inject the service in the constructor
3. Call `getPlayers()` when the "Load Players" button is clicked (the button already exists)
4. Store the result in a `players` signal
5. Update the template to loop over `players()` and render `<app-player-card>` for each one

---

## Done when…

- Clicking the button loads real players from the backend and displays them using `PlayerCardComponent`
- If you add a player directly to the backend's `players_list` and restart the server, it shows up in the browser after clicking the button

---

## Stretch 🏓

Add a `loading` signal (`boolean`) that is `true` while the request is in flight.
Show "Loading…" text in the template while it's `true` and hide the button.
