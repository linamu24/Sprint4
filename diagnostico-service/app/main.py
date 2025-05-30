from fastapi import FastAPI
from .database import diagnosticos
from .models import Diagnostico
from .report import generar_reporte

app = FastAPI()

@app.post("/diagnosticos")
def crear_diag(diag: Diagnostico):
    diagnosticos.insert_one(diag.dict())
    return {"mensaje": "Diagnóstico guardado"}

@app.get("/reporte")
async def reporte():
    return await generar_reporte()