from fastapi import FastAPI
from .models import Examen
from .database import examenes

app = FastAPI()

@app.post("/examenes")
def crear_examen(e: Examen):
    examenes.insert_one(e.dict())
    return {"mensaje": "Examen guardado"}