from fastapi import FastAPI, HTTPException
from .models import Paciente
from .database import conn
from sqlalchemy import text

app = FastAPI()

@app.post("/pacientes")
def crear_paciente(p: Paciente):
    query = text("""
        INSERT INTO pacientes (id, nombre, apellido, fecha_nacimiento, edad, estado_civil, tipo_documento)
        VALUES (:id, :nombre, :apellido, :fecha_nacimiento, :edad, :estado_civil, :tipo_documento)
    """)
    conn.execute(query, p.dict())
    return {"mensaje": "Paciente creado"}

@app.get("/pacientes/{id}")
def obtener_paciente(id: int):
    result = conn.execute(text("SELECT edad FROM pacientes WHERE id = :id"), {"id": id}).fetchone()
    if result:
        return {"edad": result[0]}
    else:
        raise HTTPException(status_code=404, detail="Paciente no encontrado")