# BE-02 — CRUD on an In-Memory List

**Goal:** Implement all four operations (read, add, delete, update) on the in-memory players list, using Pydantic to validate incoming data.

> **Ce vei învăța / What you'll learn**
> - `GET /players/{id}` — parametru de cale *(path parameter)*
> - `POST /players` cu `BaseModel` Pydantic *(validating a request body)*
> - `DELETE /players/{id}` *(removing an item by id)*
> - Ce înseamnă să "validezi" datele primite *(what input validation means)*

---

## Concept

**Pydantic** checks that the data the client sends matches what you expect — before your code even runs:

```python
from pydantic import BaseModel

class PlayerCreate(BaseModel):
    name: str   # FastAPI rejects requests where name is missing or not a string
```

**Path parameter** — the value comes directly from the URL:

```python
@router.get("/players/{player_id}")
def get_player(player_id: int):
    ...
```

**Finding an item in a list:**

```python
player = next((p for p in players_list if p["id"] == player_id), None)
if player is None:
    raise HTTPException(status_code=404, detail="Player not found")
```

**Auto-generating an id for a new item:**

```python
new_id = max((p["id"] for p in players_list), default=0) + 1
```

---

## Exercise

Inside `api/players.py`, implement these four routes:

| Method   | URL                    | What it does                             |
|----------|------------------------|------------------------------------------|
| `GET`    | `/players`             | Return all players                       |
| `GET`    | `/players/{player_id}` | Return one player (404 if not found)     |
| `POST`   | `/players`             | Add a new player (body: `{"name": "…"}`) |
| `DELETE` | `/players/{player_id}` | Remove a player by id                    |

Use `PlayerCreate(name: str)` as the Pydantic model for the POST body.

---

## Done when…

- You can test all four routes in the interactive docs at `http://localhost:8000/docs`
- Adding a player via POST makes them appear in subsequent GET calls
- Deleting a player removes them from the list (until the server restarts)

---

## Stretch 🏓

Add `PUT /players/{player_id}` that updates the name of an existing player.
Use the same `PlayerCreate` model as the request body.
