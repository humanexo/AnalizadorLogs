from typing import Any, Dict

import self as self


class AnalizadorLogs:
    def __init__(self, nombre_archivo: str):
        self.nombre_archivo = nombre_archivo  # Este sería el archivo que estamos procesando

    # Acá como necesitamos almacenar datos lo que hacemos es crear
    # las variables acumuladoras y los contadores para poder calcular las estadisticas.
    def procesar_logs(self) -> Dict[str, Any]:
        numero_total_solicitudes = 0
        numero_metodo_http_solicitudes = {}
        numero_solicitudes_codigo_respuesta = {}
        tamaño_total_respuesta = 0
        tamaño_promedio_respuesta = 0
        numero_solicitudes_url = 0

    # Utilizamos la función "open" para abrir los datos y hacer
    # la lectura linea por linea con un ciclo "for"

    with open(self.nombre_archivo) as f:
        for linea in f:
            # El metodo Strip sirve para eliminar espacios en blancos
            # se pone al principio para que no queden espacios en blanco
            # a la hora de utilizar el metodo Split
            campos = linea.strip().split()

            # Acá para acceder a los campos utilizamos el indice correspondiente de cada
            # cosa en la lista
            direccion_ip = campos[0]
            fecha_hora = campos[1] + " " + campos[2]
            metodo_http = campos[3]
            url_recurso = campos[4]
            codigo_respuesta_http = campos[5]
            tamaño_respuesta_bytes = int(campos[6])

            # Ahora tenemos que actualizar con cada linea del archivo las variables que habíamos creado.
            # Actualizamos las variables acumuladoras y contadores





