# FE-04 — Sending Data to the Backend

**Goal:** Add a text input so the user can type a name and add a new player via POST.

> **Ce vei învăța / What you'll learn**
> - Cum legi un câmp `<input>` la o proprietate din componentă *(binding an input to component state)*
> - Cum trimiți un POST request cu un body JSON *(POST with a JSON body)*
> - Cum reîmprospătezi lista după adăugare *(refresh the list after a successful POST)*

---

## Concept

**Reading what the user typed** — store it in a signal and update it on each keystroke:

```typescript
newName = signal('');
```

```html
<input [value]="newName()" (input)="newName.set($any($event.target).value)" />
```

Or, if you add `FormsModule` to imports, use the simpler `ngModel`:

```html
<input [(ngModel)]="newNameStr" />
```

**Sending a POST with a body:**

```typescript
addPlayer(name: string) {
  return this.http.post('http://localhost:8000/players', { name });
}
```

**Pattern — add then refresh:**

```typescript
onAdd() {
  this.playerService.addPlayer(this.newName()).subscribe({
    next: () => {
      this.loadPlayers();      // reload the list
      this.newName.set('');    // clear the input
    },
    error: (err) => console.error(err),
  });
}
```

---

## Exercise

1. In `PlayerService`, add an `addPlayer(name: string)` method that sends `POST /players`
2. In `AppComponent`, add:
   - A `newName` signal (string, starts as `''`)
   - An `onAdd()` method that calls the service, then reloads the list
3. In the template, add:
   - A text `<input>` bound to `newName`
   - An "Add" button that calls `onAdd()`
4. After a successful POST the list should update automatically and the input should clear

---

## Done when…

- Typing a name and clicking "Add" sends the POST (visible in the browser Network tab — F12)
- The new player appears in the list without a page refresh
- The input field is empty after adding

---

## Stretch 🏓

Disable the "Add" button when the input is blank:
`[disabled]="newName().trim() === ''"`.
