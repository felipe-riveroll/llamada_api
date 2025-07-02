import requests
import json

# Reemplaza con tus credenciales
api_key = '869a64c220260c1'
api_secret = '9ea092b7c05e142'

url = "https://erp.asiatech.com.mx/api/resource/Employee Checkin"

headers = {
    'Authorization': f'token {api_key}:{api_secret}'
}

# Define los filtros y los campos que necesitas
params = {
    'fields': '["name", "employee", "employee_name", "time", "log_type"]',
    'filters': '[["Employee Checkin", "time", "Between", ["2025-06-01", "2025-06-30"]],["Employee Checkin", "device_id", "like", "%31"]]'
}

try:
    all_records = []
    page_length = 100  # Cantidad de registros por página
    limit_start = 0
    
    while True:
        # Agregar parámetros de paginación
        params['limit_start'] = limit_start
        params['limit_page_length'] = page_length
        
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        
        data = response.json()
        current_records = data.get('data', [])
        
        # Si no hay registros, salimos del bucle
        if not current_records:
            break
            
        # Agregar registros a nuestra lista
        all_records.extend(current_records)
        print(f"Obtenidos {len(current_records)} registros (total hasta ahora: {len(all_records)})")
        
        # Si recibimos menos registros que page_length, significa que ya no hay más
        if len(current_records) < page_length:
            break
            
        # Avanzar al siguiente conjunto de registros
        limit_start += page_length
    
    # Construir resultado final con el mismo formato que la respuesta original
    filtered_records = {'data': all_records}
    
    # Imprimir el resultado de forma legible
    print(f"\nTotal de registros obtenidos: {len(all_records)}")
    print(json.dumps(filtered_records, indent=4))

except requests.exceptions.HTTPError as err:
    print(f"Error HTTP: {err}")
    print(f"Respuesta del servidor: {response.text}")
except Exception as e:
    print(f"Ocurrió un error: {e}")