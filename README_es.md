# Llamada API (documentación en español)

Este repositorio contiene un pequeño script (`registros.py`) utilizado para obtener los registros de entrada de empleados desde la API de ERP de Asiatech.

## Variables de entorno

El script espera que se definan las siguientes variables en el entorno:

- `ASIATECH_API_KEY` – clave de API proporcionada por Asiatech.
- `ASIATECH_API_SECRET` – secreto de API asociado a la clave.

Antes de ejecutar el script o utilizar la función de forma programática, establece estas variables, por ejemplo:

```bash
export ASIATECH_API_KEY="tu_api_key"
export ASIATECH_API_SECRET="tu_api_secret"
python registros.py
```

## Función `fetch_checkins`

La función `fetch_checkins(start_date, end_date, device_filter)` permite recuperar los registros de check-in de los empleados entre dos fechas y filtrados por un identificador de dispositivo.

Parámetros:

- `start_date`: fecha inicial en formato `AAAA-MM-DD`.
- `end_date`: fecha final en formato `AAAA-MM-DD`.
- `device_filter`: filtro aplicado al campo `device_id` (por ejemplo `%31%`, `%villas%` o `%nave%`).

La función realiza solicitudes paginadas a la API, acumulando los registros obtenidos hasta que no haya más datos. Devuelve una lista de diccionarios con la información de cada check-in.

Un ejemplo de uso sería:

```python
from registros import fetch_checkins
resultados = fetch_checkins("2025-06-01", "2025-06-30", "%31%")
print(resultados)
```
