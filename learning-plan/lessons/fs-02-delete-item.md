# FS-02 — Delete a Player: End-to-End

**Goal:** Add a delete button to each player card. Clicking it removes the player from the backend and updates the list.

> **Ce vei învăța / What you'll learn**
> - `@Output()` și `EventEmitter` — cum trimite o componentă-copil un eveniment spre părinte *(child-to-parent communication)*
> - DELETE request cu parametru de cale *(DELETE with a path parameter)*
> - Actualizarea listei după ștergere *(refresh after delete)*

---

## Concept

The **delete button lives inside `PlayerCardComponent`**, but the actual API call must be handled by `AppComponent` (which owns the list and the service).

We use `@Output()` to send an event from child to parent.

**In the child (`PlayerCardComponent`):**

```typescript
import { Output, EventEmitter } from '@angular/core';

@Output() deleteRequested = new EventEmitter<number>();

onDelete() {
  this.deleteRequested.emit(this.player.id);
}
```

```html
<!-- player-card.component.html -->
<button (click)="onDelete()">Delete</button>
```

**In the parent (`AppComponent`):**

```html
<!-- app.component.html -->
<app-player-card [player]="p" (deleteRequested)="deletePlayer($event)" />
```

```typescript
// app.component.ts
deletePlayer(id: number) {
  this.playerService.deletePlayer(id).subscribe(() => this.loadPlayers());
}
```

**In the service:**

```typescript
deletePlayer(id: number) {
  return this.http.delete(`http://localhost:8000/players/${id}`);
}
```

---

## Exercise

1. In `PlayerService`, add `deletePlayer(id: number)` — sends `DELETE /players/{id}`
2. In `PlayerCardComponent`:
   - Add `@Output() deleteRequested = new EventEmitter<number>()`
   - Add an `onDelete()` method that emits the player's id
   - Add a Delete button in the template that calls `onDelete()`
3. In `AppComponent`:
   - Handle the `(deleteRequested)` event
   - Call `playerService.deletePlayer(id)` and reload the list on success

---

## Done when…

- Each card shows a Delete button
- Clicking it removes the player from the backend and the card disappears
- Loading the players again confirms the player is gone (until the server restarts)

---

## Stretch 🏓

Ask for confirmation before deleting:

```typescript
onDelete() {
  if (confirm(`Delete ${this.player.name}?`)) {
    this.deleteRequested.emit(this.player.id);
  }
}
```
