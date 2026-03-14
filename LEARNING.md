# Ping-Pong Project — Learning Guide

This is a full-stack project for learning. Use it alongside the exercises below.

| Layer | Tech | Key Files |
|-------|------|-----------|
| **Backend** | Python, FastAPI | `main.py`, `models/__init__.py`, `db/__init__.py` |
| **Frontend** | TypeScript, Angular 21 | `frontend/src/app/app.component.ts`, `ping.service.ts` |
| **Database** | MySQL, SQLAlchemy | Configured in `db/__init__.py` |

**Backend endpoints:**

| Method | Path | What it does |
|--------|------|-------------|
| `GET` | `/` | Health check |
| `GET` | `/players` | List all players |
| `GET` | `/players/{id}` | Get one player |
| `POST` | `/players` | Create a player (body: `{ "name": "..." }`) |
| `PUT` | `/players/{id}` | Update a player's name |
| `DELETE` | `/players/{id}` | Delete a player |

---

## Part 1: Git Exercises on This Project

### Exercise G1: Explore the repo history

```bash
cd C:\Users\stefa\Desktop\Projects\ping-pong-be
git log --oneline
```

- How many commits are there?
- Who made them?
- Read a few commit messages — can you understand what changed?

### Exercise G2: Check the .gitignore

Open `.gitignore` in the project root. Answer these questions:

1. Is `node_modules/` ignored? (It should be — it's the Angular dependency folder)
2. Is `__pycache__/` ignored? (Python bytecode cache)
3. Is `.env` ignored? (Contains database passwords)
4. Is `.venv/` ignored? (Python virtual environment)

If anything is missing, add it, then:

```bash
git add .gitignore
git commit -m "Update .gitignore"
```

### Exercise G3: Create a feature branch

```bash
git checkout -b feature/your-name
```

Make a small change — for example, update the health check message in `main.py`:

```python
# Line 23 in main.py — change the message:
return {"message": "Ping Pong API is running 2026-03"}
# TODO Bonus, even better if you use current time using Python
```

Then commit and push:

```bash
git add main.py
git commit -m "Update health check message"
git push -u origin feature/your-name
```

**Discussion:** How would this become a Pull Request on a team? What's the review process?

---

## Part 2: Angular Signals Exercises

The frontend already uses Angular **signals** — a reactive primitive for managing state without RxJS Subjects or BehaviorSubjects.

### What's already in the project

Open `frontend/src/app/app.component.ts`. You'll find:

```typescript
// Three writable signals:
playersData = signal<PlayersResponse | null>(null);
loading = signal(false);
error = signal<string | null>(null);
```

- **`signal(initialValue)`** — creates a writable signal
- **`.set(newValue)`** — replaces the signal's value (used in `callPing()`)
- **`signalName()`** — call it like a function to read the current value (used in the template)

Open `frontend/src/app/app.component.html`. You'll find:

```html
<!-- Reading signals in templates — call them with () -->
{{ loading() ? 'Loading…' : 'Load Players' }}

<!-- New Angular control flow syntax -->
@if (error()) { ... }
@if (playersData()) { ... }
@for (player of playersData()!.players; track player.id) { ... }
```

- **`@if`** — replaces `*ngIf` (Angular 17+ syntax)
- **`@for`** — replaces `*ngFor` with mandatory `track` expression
- **`ChangeDetectionStrategy.OnPush`** — signals trigger change detection automatically

---

### Exercise S1: Add a `computed()` signal (10 min)

**Goal:** Create a derived signal that automatically recalculates when its dependencies change.

**In `app.component.ts`:**

1. Add `computed` to the import:

```typescript
import { Component, signal, computed, ChangeDetectionStrategy, ViewEncapsulation } from "@angular/core";
```

2. Add this after the existing signals:

```typescript
playerCount = computed(() => this.playersData()?.players.length ?? 0);
```

> `computed()` creates a **read-only** signal that derives its value from other signals.  
> Whenever `playersData` changes, `playerCount` automatically recalculates.  
> The `?? 0` handles the case where `playersData` is `null`.

**In `app.component.html`:**

3. Find the line that shows the player count:

```html
<h2 class="text-xl font-semibold text-gray-700 mb-4">
  Players ({{ playersData()!.players.length }})
</h2>
```

Replace `playersData()!.players.length` with `playerCount()`:

```html
<h2 class="text-xl font-semibold text-gray-700 mb-4">
  Players ({{ playerCount() }})
</h2>
```

### ✅ Verify

- Run the app, click "Load Players" — the count should display as before
- **Why is this better?** The computed signal centralizes the logic. If you need the count in multiple places, you use `playerCount()` instead of repeating `playersData()!.players.length` everywhere.

---

### Exercise S2: Add an `effect()` for logging (10 min)

**Goal:** Run code every time a signal changes — useful for debugging and side effects.

**In `app.component.ts`:**

1. Add `effect` to the import:

```typescript
import { Component, signal, computed, effect, ChangeDetectionStrategy, ViewEncapsulation } from "@angular/core";
```

2. Add this inside the `constructor`:

```typescript
constructor(private ping: PingService) {
  effect(() => {
    const data = this.playersData();
    if (data) {
      console.log('Players loaded:', data.players.length, 'players');
    }
  });
}
```

> `effect()` automatically tracks which signals you read inside it.  
> Every time `playersData` changes, this effect re-runs.  
> Effects run in a **reactive context** — no subscriptions to manage, no cleanup needed.

### ✅ Verify

- Open the browser DevTools (F12) → Console tab
- Click "Load Players"
- You should see: `Players loaded: X players` in the console
- Click "Load Players" again — the message appears again with updated data

---

### Exercise S3: Search filter with signals (20 min)

**Goal:** Add a search input that filters players by name, using only signals (no RxJS).

**In `app.component.ts`:**

1. Add a new signal for the search term:

```typescript
searchTerm = signal('');
```

2. Add a computed signal for filtered players:

```typescript
filteredPlayers = computed(() => {
  const data = this.playersData();
  const term = this.searchTerm().toLowerCase();
  if (!data) return [];
  if (!term) return data.players;
  return data.players.filter(player =>
    player.name.toLowerCase().includes(term)
  );
});
```

3. Add a method to update the search term (called from the template):

```typescript
onSearch(event: Event) {
  const input = event.target as HTMLInputElement;
  this.searchTerm.set(input.value);
}
```

**In `app.component.html`:**

4. Add a search input after the "Load Players" button:

```html
<input
  type="text"
  placeholder="Search players..."
  (input)="onSearch($event)"
  class="mt-4 w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500"
/>
```

5. Update the `@for` loop to use `filteredPlayers()` instead of `playersData()!.players`:

```html
@for (player of filteredPlayers(); track player.id) {
```

6. Update the player count heading to show filtered vs total:

```html
<h2 class="text-xl font-semibold text-gray-700 mb-4">
  Players ({{ filteredPlayers().length }} / {{ playerCount() }})
</h2>
```

### ✅ Verify

- Load players, then type in the search box
- The list should filter in real-time as you type
- The count should update (e.g., "Players (2 / 5)")
- **Notice:** No subscriptions. No `debounceTime`. No `Subject`. Pure signals.

---

### Exercise S4: Add a new player — full-stack (20 min)

**Goal:** Wire up the frontend to the existing `POST /players` backend endpoint.

**In `frontend/src/app/ping.service.ts`:**

1. Add a method to create a player:

```typescript
createPlayer(name: string): Observable<object> {
  return this.http.post<object>(`${this.base}/players`, { name });
}
```

**In `app.component.ts`:**

2. Add a signal for the new player name:

```typescript
newPlayerName = signal('');
```

3. Add the method to handle submission:

```typescript
addPlayer() {
  const name = this.newPlayerName().trim();
  if (!name) return;

  this.ping.createPlayer(name).subscribe({
    next: () => {
      this.newPlayerName.set('');
      this.callPing(); // reload the player list
    },
    error: (err) => {
      this.error.set(err.message || "Failed to add player");
    },
  });
}

onNewPlayerInput(event: Event) {
  const input = event.target as HTMLInputElement;
  this.newPlayerName.set(input.value);
}
```

**In `app.component.html`:**

4. Add an "Add Player" form after the search input:

```html
<div class="mt-4 flex gap-2">
  <input
    type="text"
    placeholder="New player name..."
    [value]="newPlayerName()"
    (input)="onNewPlayerInput($event)"
    class="flex-1 px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500"
  />
  <button
    (click)="addPlayer()"
    [disabled]="!newPlayerName().trim()"
    class="px-5 py-2 rounded-lg bg-green-600 text-white font-semibold hover:bg-green-700 disabled:opacity-50 disabled:cursor-not-allowed transition"
  >
    Add Player
  </button>
</div>
```

### ✅ Verify

- Type a name in the input, click "Add Player"
- The player list should reload and include the new player
- The input should clear after successful addition
- Try adding a player with an empty name — the button should be disabled

---

## Signals Cheat Sheet

| Concept | Code | What it does |
|---------|------|-------------|
| Create writable signal | `mySignal = signal('initial')` | Holds a value you can change |
| Read a signal | `mySignal()` | Returns current value |
| Set a signal | `mySignal.set('new')` | Replaces the value |
| Update a signal | `mySignal.update(v => v + 1)` | Transform based on current value |
| Computed signal | `derived = computed(() => mySignal() * 2)` | Read-only, auto-recalculates |
| Effect | `effect(() => console.log(mySignal()))` | Runs side effects when signals change |

**Key insight:** Signals replace the need for BehaviorSubject / ReplaySubject for local component state. RxJS is still useful for async operations (HTTP calls, WebSockets), but signals handle the UI state.
