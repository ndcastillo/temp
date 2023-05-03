import requests
import json

# Configuración de conexión con Thingsboard
url = "10.0.2.83/api/v1/ZruKMouS1Yli8wFCJRSG/telemetry"
headers = {
            "Content-Type": "application/json",
                "Accept": "application/json",
                    "X-Authorization": "Bearer eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJuZXN0b3IuY2FzdGlsbG9AdWN1ZW5jYS5lZHUuZWMiLCJ1c2VySWQiOiJlN2NhZWU1MC1jZDc0LTExZWQtYTE5Yy04MzNhOTYzM2E2ZmMiLCJzY29wZXMiOlsiVEVOQU5UX0FETUlOIl0sInNlc3Npb25JZCI6Ijc1OGIyOGNiLWNkZDktNDUwOS04ODcwLTQyMGE5YWE4NjM0ZCIsImlzcyI6InRoaW5nc2JvYXJkLmlvIiwiaWF0IjoxNjgzMTMzNDY0LCJleHAiOjE2ODMxNDI0NjQsImZpcnN0TmFtZSI6Ik5lc3RvciIsImxhc3ROYW1lIjoiQ2FzdGlsbG8iLCJlbmFibGVkIjp0cnVlLCJpc1B1YmxpYyI6ZmFsc2UsInRlbmFudElkIjoiZWNkZGM5YjAtY2Q3MS0xMWVkLWExOWMtODMzYTk2MzNhNmZjIiwiY3VzdG9tZXJJZCI6IjEzODE0MDAwLTFkZDItMTFiMi04MDgwLTgwODA4MDgwODA4MCJ9.CnQYQ2X9r9RhGRu1RwHqHPwcYtWF3Xp2Q1o9whmUlXkD-2akWPJigglnaFjkNzSHoO57WAodovjpOS1PI4Mjyg"
                    }

# Crear un diccionario con los valores de los parámetros
data = {
            "temperature": 25.0,
                "humidity": 60.0
                }

# Convertir el diccionario a un formato JSON
payload = json.dumps(data)

# Enviar la solicitud HTTP POST
response = requests.post(url, headers=headers, data=payload)

# Verificar el estado de la respuesta
if response.status_code == 200:
    print("Mensaje enviado con éxito a Thingsboard")
else:
    print("Error al enviar el mensaje a Thingsboard")
