# DB-01 — SQLite + SQLAlchemy

**Goal:** Reintroduce a real database, but using SQLite — a file-based database that needs zero installation or Docker.

> **Ce vei învăța / What you'll learn**
> - Ce este un ORM și cum mapează clase Python la tabele *(what an ORM is)*
> - Ce este SQLite și de ce e util în development *(SQLite as a zero-config DB)*
> - `Session` și dependency injection în FastAPI *(DB sessions as a FastAPI dependency)*
> - Cum migrezi de la lista in-memory la un model SQLAlchemy *(migrating from list to ORM)*

---

## Concept

**ORM (Object-Relational Mapper)** — SQLAlchemy lets you work with the database using Python classes instead of raw SQL.

```python
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Player(Base):
    __tablename__ = "players"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
```

**SQLite** — the entire database is a single `.db` file. No server, no password:

```python
engine = create_engine("sqlite:///./pingpong.db")
```

**Session** — each request gets its own database connection, closed when done:

```python
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
```

**Using it in a route:**

```python
@router.get("/players")
def get_players(db=Depends(get_db)):
    return db.query(Player).all()
```

---

## Exercise

1. In `db/__init__.py`, replace the MySQL URL with:
   ```python
   DATABASE_URL = "sqlite:///./pingpong.db"
   ```
   *(no `.env` file needed for this)*
2. Keep the `Player` SQLAlchemy model in `models/__init__.py` as-is
3. Remove the in-memory `players_list` from `api/players.py`
4. Update each route to accept `db=Depends(get_db)` and query via SQLAlchemy
5. Start the server — it should create `pingpong.db` automatically

---

## Done when…

- The server starts with no MySQL connection running
- `pingpong.db` appears in the project folder after first startup
- Adding a player via POST persists after restarting the server

---

## Stretch 🏓

Delete `pingpong.db`, restart the server, and confirm the table is recreated empty. This shows you that `create_tables()` handles the schema automatically.
