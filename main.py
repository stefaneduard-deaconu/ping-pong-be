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


