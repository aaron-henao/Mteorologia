from typing import Tuple

class DatosMeteorologicos:

    def __init__(self, nombre_archivo: str):
        self.nombre_archivo: str = nombre_archivo
        nombre_archivo = "datos_meteorologicos.txt"

    def procesar_datos(self) -> Tuple[float, float, float, float, str]:
        temperatura_total = 0
        humedad_total = 0
        presion_total = 0
        velocidad_viento_total = 0
        viento_grados = []

        with open(self.nombre_archivo) as archivo:
            for linea in archivo:
                if linea.startswith("Temperatura"):
                    temperatura_total += float(linea.split(": ")[1])
                    temperatura_total += temperatura
                elif linea.startswith("Humedad"):
                    humedad_total += float(linea.split(": ")[1])
                    humedad_total += humedad
                elif linea.startswith("Presión"):
                    presion_total += float(linea.split(": ")[1])
                    presion_total += presion
                elif linea.startswith("Viento"):
                    velocidad_viento, direccion_viento = linea.split(": ")[1].split(",")
                    velocidad_viento_total += float(velocidad_viento)



