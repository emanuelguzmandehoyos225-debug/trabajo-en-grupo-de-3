# ☕ API Liquidación de Pagos - Caficultores

Este proyecto consiste en una API REST desarrollada con FastAPI para automatizar el pago semanal de recolectores de café.

El sistema recibe un registro de los kilos recolectados diariamente por un trabajador, suma el total semanal, y calcula su pago base más las bonificaciones correspondientes según su rendimiento.

## 🛠️ Tecnologías Utilizadas
* **Lenguaje:** Python
* **Framework:** FastAPI
* **Servidor:** Uvicorn
* **Contenedores:** Docker

## ⚙️ Lógica de Negocio
El microservicio expone un endpoint (`POST /liquidar-pago`) que aplica las siguientes reglas:
1. **Pago base:** Total de kilos recolectados en la semana multiplicados por $600 COP.
2. **Bonificaciones:**
    * Si el trabajador recolecta **más de 150 kilos** en la semana, recibe un bono de **$50.000 COP**.
    * Si el trabajador recolecta **más de 100 kilos** (pero no supera los 150), recibe un bono de **$20.000 COP**.

## 🚀 Instrucciones de Ejecución (Docker)

Para garantizar que la API funcione en cualquier entorno de forma aislada, el proyecto está contenerizado. Sigue estos pasos para ejecutarlo:

1. **Construir la imagen de Docker:**
   ```bash
   docker build -t api-caficultores .