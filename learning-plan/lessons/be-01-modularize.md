# BE-01 — Modularise the Backend

**Goal:** Make the server run without a database by using a simple in-memory list, and move the players routes into their own file.

> **Ce vei învăța / What you'll learn**
> - Ce este un `APIRouter` și de ce îl folosim *(what a Router is and why we use it)*
> - Cum separăm rutele pe fișiere *(how to split routes into separate files)*
> - Cum înlocuim baza de date cu o listă Python *(how to replace the DB with a Python list)*

---

## Concept

Right now `main.py` does everything: CORS setup, database startup, and all the routes.
As the app grows, this becomes hard to read and maintain.

**`APIRouter`** lets you define routes in a separate file and then "plug them in" to the main app:

```python
# api/players.py
from fastapi import APIRouter

router = APIRouter()

@router.get("/players")
def get_players():
    ...
```

```python
# main.py
from api.players import router as players_router

app.include_router(players_router)
```

Instead of a real database, we'll use a **module-level list** — a variable that lives as long as the server is running:

```python
players_list = [
    {"id": 1, "name": "Alice"},
    {"id": 2, "name": "Bob"},
]
```

---

## Exercise

1. Create the file `api/players.py`
2. At the top of that file define `players_list` with 2–3 hardcoded players
3. Add one route: `GET /players` — returns the list
4. In `main.py`:
   - Remove (or comment out) all DB imports, the `startup` event, and any `Depends(get_db)`
   - Import the new router and register it: `app.include_router(players_router)`
5. Start the server: `uvicorn main:app --reload`

---

## Done when…

- `GET http://localhost:8000/players` returns the hardcoded players
- No database is running and the server starts without errors
- `main.py` no longer contains any DB code

---

## Stretch 🏓

Add a second router `api/locations.py` with its own hardcoded `locations_list` and a `GET /locations` route. Include it in `main.py`.
