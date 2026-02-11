from fastapi import FastAPI
from db import create_tables

app = FastAPI()

@app.on_event("startup")
def startup():
    """Create database tables on app startup"""
    create_tables()

# Routers will be included here later

@app.get("/")
def read_root():
    return {"message": "Ping Pong API is running 2024-06"}  


# endpoints for player table.

# CRUD?   Create, Read, Update, Delete players

# GET - Path parameters
@app.get("/players/{player_id}")
def get_player(player_id: int):
    return {"id": player_id, "name": "John"}

# GET - Query parameters  
@app.get("/players")
def get_players(skip: int = 0, limit: int = 10):
    return {"players": [], "skip": skip, "limit": limit}

# POST - Request body
@app.post("/players")
def create_player():
    return {"message": "Player created", "name": "John"}

# PUT - Path + Body
@app.put("/players/{player_id}")
def update_player(player_id: int):
    return {"id": player_id, "name": "John Updated"}

# DELETE - Path parameters
@app.delete("/players/{player_id}")
def delete_player(player_id: int):
    return {"message": f"Player {player_id} deleted"}


