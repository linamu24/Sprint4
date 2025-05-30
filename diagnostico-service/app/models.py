from pydantic import BaseModel
from datetime import datetime

class Diagnostico(BaseModel):
    id: str
    paciente_id: str
    diagnostico: str
    fecha: datetime