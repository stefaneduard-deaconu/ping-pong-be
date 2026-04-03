# FE-02 — Creating a New Component

**Goal:** Extract the player display into its own reusable component and use it from `AppComponent`.

> **Ce vei învăța / What you'll learn**
> - Cum generezi o componentă nouă cu Angular CLI *(how to generate a new component)*
> - `@Input()` — cum trimiți date unei componente-copil *(how a parent passes data to a child)*
> - Cum folosești o componentă în template cu property binding `[prop]="value"` *(how to use a component)*

---

## Concept

Right now the player display is written directly inside `AppComponent`.
As the app grows, we extract pieces into their own components.

**1. Generate** a new component (run this inside the `frontend/` folder):

```bash
ng generate component player-card
# shorthand:
ng g c player-card
```

This creates `src/app/player-card/player-card.component.ts` and `.html`.

**2. Declare an `@Input()`** — a property the parent can set from outside:

```typescript
import { Component, Input } from '@angular/core';

@Component({ selector: 'app-player-card', standalone: true, templateUrl: '...' })
export class PlayerCardComponent {
  @Input() player!: { id: number; name: string };
}
```

**3. Use it in the parent template:**

```html
@for (p of players; track p.id) {
  <app-player-card [player]="p" />
}
```

`[player]="p"` — square brackets mean "bind this property to a value from the parent".

**4. Import it** in `AppComponent`:

```typescript
@Component({
  imports: [PlayerCardComponent],   // ← add this
  ...
})
```

---

## Exercise

1. Run `ng generate component player-card` inside `frontend/`
2. In `PlayerCardComponent`, declare `@Input() player!: { id: number; name: string }`
3. In `player-card.component.html`, display `player.id` and `player.name` — style it however you like
4. Add `PlayerCardComponent` to the `imports` array of `AppComponent`
5. In `app.component.html`, replace the inline `@for` content with `<app-player-card [player]="p" />`

---

## Done when…

- Each player is rendered by `PlayerCardComponent` (verify by inspecting the DOM in DevTools)
- Adding a 4th player to `AppComponent`'s array automatically shows a 4th card
- You can update the card's HTML without touching `AppComponent`

---

## Stretch 🏓

Make the card look different for the first player using a conditional CSS class:
`[class.first-player]="player.id === 1"` and define `.first-player` in `player-card.component.css`.
