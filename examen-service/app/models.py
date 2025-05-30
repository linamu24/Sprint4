from pydantic import BaseModel
from datetime import datetime

class Examen(BaseModel):
    id: str
    paciente_id: str
    examen: str
    fecha: datetime