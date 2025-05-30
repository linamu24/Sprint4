from pydantic import BaseModel

class Paciente(BaseModel):
    id: int
    nombre: str
    apellido: str
    fecha_nacimiento: str
    edad: int
    estado_civil: str
    tipo_documento: str