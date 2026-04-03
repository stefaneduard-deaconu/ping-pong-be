# FE-01 — Template Basics

**Goal:** Display data that lives in the component class — no HTTP calls, just learning how Angular connects TypeScript to HTML.

> **Ce vei învăța / What you'll learn**
> - Cum definim date în clasa componentei *(how to define data in the component class)*
> - `{{ expression }}` — interpolation: afișezi o valoare în HTML *(display a value in HTML)*
> - `@if (condition)` — afișezi ceva condiționat *(conditional rendering)*
> - `@for (item of list; track item.id)` — repeți un element HTML *(loop over a list)*

---

## Concept

The component **class** (TypeScript) holds the data. The **template** (HTML) displays it. They are linked automatically.

```typescript
// app.component.ts
export class AppComponent {
  title = 'Ping Pong';
  score = 42;
  players = [
    { id: 1, name: 'Alice' },
    { id: 2, name: 'Bob' },
  ];
}
```

```html
<!-- app.component.html -->
<h1>{{ title }}</h1>           <!-- shows: Ping Pong -->
<p>Score: {{ score }}</p>      <!-- shows: Score: 42 -->

@for (p of players; track p.id) {
  <div>{{ p.name }}</div>      <!-- one div per player -->
}
```

`@if` shows or hides a block:

```html
@if (players.length === 0) {
  <p>No players yet.</p>
}
```

---

## Exercise

In `app.component.ts`, add:
- A `title` property: `'Ping Pong App'`
- A `players` array with 3 hardcoded player objects (each with `id` and `name`)
- A `showPlayers` boolean set to `true`

In `app.component.html`, replace the current content with:
1. An `<h1>` showing the title
2. An `@if (showPlayers)` block containing:
   - An `@for` loop that displays each player's name in a `<div>`

---

## Done when…

- The browser shows the title and the 3 player names — **no server needed**
- Temporarily setting `showPlayers = false` makes the list disappear

---

## Stretch 🏓

Add a `playerCount` property that returns `players.length` and display it below the title:
`"3 players registered"`. *(Hint: you can use a regular getter: `get playerCount() { return this.players.length; }`)*
