from .database import diagnosticos
import httpx
from collections import defaultdict

async def generar_reporte():
    resultados = defaultdict(lambda: defaultdict(int))
    async with httpx.AsyncClient() as client:
        for d in diagnosticos.find({"diagnostico": "epilepsia"}):
            año = d["fecha"].year
            paciente_id = d["paciente_id"]
            resp = await client.get(f"http://paciente-service:8000/pacientes/{paciente_id}")
            edad = resp.json().get("edad", "desconocido")
            resultados[año][edad] += 1
    return resultados