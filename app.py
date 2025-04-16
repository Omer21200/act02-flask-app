from flask import Flask
from datetime import datetime
import requests

app = Flask(__name__)

@app.route('/')
def home():
    # Leer archivo desde la URL
    url = 'https://gist.githubusercontent.com/reroes/502d11c95f1f8a17d300ece914464c57/raw/872172ebb60e22e95baf8f50e2472551f49311ff/gistfile1.txt'
    response = requests.get(url)
    datos = response.text.splitlines()

    # Filtrar líneas que inicien con 3, 4, 5 o 7
    personas_filtradas = []
    for linea in datos:
        partes = linea.split(";")
        if partes and partes[0][0] in ['3', '4', '5', '7']:
            personas_filtradas.append(partes)

    # Crear la tabla HTML
    tabla_html = """
    <table border="1">
        <tr>
            <th>ID</th>
            <th>Nombre</th>
            <th>Apellido</th>
            <th>Email</th>
        </tr>
    """

    for persona in personas_filtradas:
        tabla_html += f"""
        <tr>
            <td>{persona[0]}</td>
            <td>{persona[1]}</td>
            <td>{persona[2]}</td>
            <td>{persona[3]}</td>
        </tr>
        """
    tabla_html += "</table>"

    # Fecha y hora actual
    actual = datetime.now()
    fecha_formateada = actual.strftime("%d, %B, %Y, %H:%M:%S")

    # Retornar la respuesta completa
    return f'¡Hola, Loja! <br><b>{fecha_formateada}</b><br><br>{tabla_html}'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
