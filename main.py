from fastapi import FastAPI
from fastapi.params import Depends
from db import create_tables, get_db
from models import Player, PlayerCreate

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
def get_player(player_id: int, db=Depends(get_db)):
    player = db.query(Player).filter(Player.id == player_id).first()
    return {"player": player}

# GET - Query parameters  
@app.get("/players")
def get_players(db=Depends(get_db)):
    players = db.query(Player).all()
    return {"players": players}

# POST - Request body
@app.post("/players")
def create_player(player: PlayerCreate, db=Depends(get_db)):
    db_player = Player(name=player.name)
    db.add(db_player)
    db.commit()
    db.refresh(db_player)
    return {"message": "Player created", "name": player.name, "id": db_player.id}

# PUT - Path + Body
@app.put("/players/{player_id}")
def update_player(player_id: int, player: PlayerCreate, db=Depends(get_db)):
    db_player = db.query(Player).filter(Player.id == player_id).first()
    db_player.name = player.name
    db.commit()
    return {"id": player_id, "name": db_player.name}

# DELETE - Path parameters
@app.delete("/players/{player_id}")
def delete_player(player_id: int, db=Depends(get_db)):
    db.query(Player).filter(Player.id == player_id).delete()
    db.commit()
    return {"message": f"Player {player_id} deleted"}


