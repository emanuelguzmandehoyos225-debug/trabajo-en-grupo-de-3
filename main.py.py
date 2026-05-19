from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Recolector(BaseModel):
    nombre: str
    kilos_diarios: List[float]

@app.post("/liquidar-pago")
def liquidar_pago(datos: Recolector):
    total_kilos = 0
    for kilos in datos.kilos_diarios:
        total_kilos += kilos

    pago_base = total_kilos * 600

    bono = 0
    if total_kilos > 150:
        bono = 50000
    elif total_kilos > 100:
        bono = 20000

    pago_neto = pago_base + bono

    return {
        "nombre": datos.nombre,
        "total_kilos": total_kilos,
        "pago_base": pago_base,
        "valor_bono": bono,
        "pago_neto": pago_neto
    }