# DB-03 — Full CRUD with the Real Database

**Goal:** Restore and verify all five CRUD operations working with MySQL and SQLAlchemy.

> **Ce vei învăța / What you'll learn**
> - Toate operațiile CRUD cu SQLAlchemy ORM *(complete CRUD with the ORM)*
> - `PUT` — actualizarea unei înregistrări existente *(updating a record)*
> - `HTTPException` pentru erori 404 *(raising 404 errors properly)*
> - Cum arată un backend complet și bine structurat *(what a complete backend looks like)*

---

## Concept

By now you know the patterns from the in-memory phase. With SQLAlchemy it's the same logic — just replace the Python list with database queries.

```python
# GET one — or 404
@router.get("/players/{player_id}")
def get_player(player_id: int, db=Depends(get_db)):
    player = db.query(Player).filter(Player.id == player_id).first()
    if not player:
        raise HTTPException(status_code=404, detail="Player not found")
    return player

# POST — create
@router.post("/players")
def create_player(data: PlayerCreate, db=Depends(get_db)):
    player = Player(name=data.name)
    db.add(player)
    db.commit()
    db.refresh(player)
    return player

# PUT — update
@router.put("/players/{player_id}")
def update_player(player_id: int, data: PlayerCreate, db=Depends(get_db)):
    player = db.query(Player).filter(Player.id == player_id).first()
    if not player:
        raise HTTPException(status_code=404, detail="Player not found")
    player.name = data.name
    db.commit()
    return player

# DELETE
@router.delete("/players/{player_id}")
def delete_player(player_id: int, db=Depends(get_db)):
    player = db.query(Player).filter(Player.id == player_id).first()
    if not player:
        raise HTTPException(status_code=404, detail="Player not found")
    db.delete(player)
    db.commit()
    return {"message": f"Player {player_id} deleted"}
```

---

## Exercise

Implement all five routes in `api/players.py`:

| Method   | URL                    | Body              | Returns               |
|----------|------------------------|-------------------|-----------------------|
| `GET`    | `/players`             | —                 | list of all players   |
| `GET`    | `/players/{id}`        | —                 | one player or 404     |
| `POST`   | `/players`             | `{ "name": "…" }` | created player        |
| `PUT`    | `/players/{id}`        | `{ "name": "…" }` | updated player        |
| `DELETE` | `/players/{id}`        | —                 | confirmation message  |

Test each one in `http://localhost:8000/docs`. Check that `GET /players/{id}` returns 404 for a non-existent id.

---

## Done when…

- All five routes work correctly in Swagger UI
- Data persists after restarting both the server and the Docker container (if using volumes)
- The Angular frontend still works unchanged — it calls the same URLs

---

## Stretch 🏓

Add a second entity — `Location` (id, name, city) — with its own:
- SQLAlchemy model in `models/`
- Pydantic schema
- Router in `api/locations.py`
- All included in `main.py`
