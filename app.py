from flask import Flask
import requests
from datetime import datetime

app = Flask(_name_)

@app.route('/')
def home():
    # Leer archivo desde la URL
    url = 'https://gist.githubusercontent.com/reroes/502d11c95f1f8a17d300ece914464c57/raw/872172ebb60e22e95baf8f50e2472551f49311ff/gistfile1.txt'
    response = requests.get(url)
    
    # Asegurar que la respuesta fue exitosa
    if response.status_code != 200:
        return f'Error al acceder al archivo: {response.status_code}'
    
    # Procesar líneas del archivo
    lineas = response.text.strip().split('\n')
    encabezados = lineas[0].split('|')
    personas = [line.split('|') for line in lineas[1:] if line[0] in {'3', '4', '5', '7'}]

    # Construir tabla HTML
    tabla = "<table border='1'><thead><tr>"
    for h in encabezados:
        tabla += f"<th>{h}</th>"
    tabla += "</tr></thead><tbody>"
    for persona in personas:
        tabla += "<tr>" + ''.join(f"<td>{campo}</td>" for campo in persona) + "</tr>"
    tabla += "</tbody></table>"

    actual = datetime.now()
    fecha_formateada = actual.strftime("%d, %B, %Y, %M, %H, %S")
    
    return f'<h2>Listado de personas (ID inicia con 3, 4, 5 o 7)</h2>{tabla}<p><b>Fecha actual:</b> {fecha_formateada}</p>'

if _name_ == '_main_':
    app.run(host='0.0.0.0', port=5000)