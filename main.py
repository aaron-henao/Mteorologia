class DatosMeteorologicos:

    def __init__(self, nombre_archivo: str):
        self.nombre_archivo: str = nombre_archivo

    def procesar_datos(self) -> tuple[float, float, float, float, str]:

        temperatura_total = 0
        humedad_total = 0
        presion_total = 0
        velocidad_viento_total = 0
        viento_grados = []
        total = len(viento_grados)

        with open(self.nombre_archivo) as archivo:
            for linea in archivo:
                # La funcion startswith manipula los tipos de datos y devuelve un booleano para indicar
                # si una serie de caracteres empieza por otra
                if linea.startswith("Temperatura"):
                    # Con split separamos cadenas en lugares concretos.
                    temperatura = float(linea.split(": ")[1])
                    temperatura_total += temperatura
                elif linea.startswith("Humedad"):
                    humedad = float(linea.split(": ")[1])
                    humedad_total += humedad
                elif linea.startswith("Presión"):
                    presion = float(linea.split(": ")[1])
                    presion_total += presion
                elif linea.startswith("Viento"):
                    velocidad_viento, direccion_viento = linea.split(": ")[1].split(",")
                    velocidad_viento_total += float(velocidad_viento)

                    direccion_viento = direccion_viento.strip()
                    # La función strip retorna una copia de la cadena con ciertos caracteres eliminados.
                    if direccion_viento == "N":
                        viento_grados.append(0)
                    elif direccion_viento == "NNE":
                        viento_grados.append(22.5)
                    elif direccion_viento == "NE":
                        viento_grados.append(45)
                    elif direccion_viento == "ENE":
                        viento_grados.append(67.5)
                    elif direccion_viento == "E":
                        viento_grados.append(90)
                    elif direccion_viento == "ESE":
                        viento_grados.append(122.5)
                    elif direccion_viento == "SE":
                        viento_grados.append(135)
                    elif direccion_viento == "SSE":
                        viento_grados.append(157.5)
                    elif direccion_viento == "S":
                        viento_grados.append(180)
                    elif direccion_viento == "SSW":
                        viento_grados.append(202.5)
                    elif direccion_viento == 'SW':
                        viento_grados.append(225)
                    elif direccion_viento == 'WSW':
                        viento_grados.append(247.5)
                    elif direccion_viento == 'W':
                        viento_grados.append(270)
                    elif direccion_viento == 'WNW':
                        viento_grados.append(292.5)
                    elif direccion_viento == 'NW':
                        viento_grados.append(315)
                    elif direccion_viento == 'NNW':
                        viento_grados.append(337.5)

                    #Calcular promedio en grados y mostrar como cadena
                    viento = sum(viento_grados) / total




        # Cálculos de promedios:
        temperatura_prom = temperatura_total / total
        humedad_prom = humedad_total / total
        presion_prom = presion_total / total
        velocidad_viento_prom = velocidad_viento_total / total


        return temperatura_prom,humedad_prom,presion_prom,velocidad_viento_prom, viento




