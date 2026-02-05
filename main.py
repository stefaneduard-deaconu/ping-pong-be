from fastapi import FastAPI

app = FastAPI()

# Routers will be included here later

@app.get("/")
def read_root():
    return {"message": "Ping Pong API is running 2024-06"}  

