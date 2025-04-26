from persona import Persona

class DirectorDeMision(Persona):
    def __init__(self, nombre, dni, nacionalidad):
        super().__init__(nombre, dni, nacionalidad)
        self.__misiones = {}  # Diccionario {nombre_astronauta: [(mision, evaluacion)]}

    def asignar_mision(self, astronauta, nombre, destino, duracion, descripcion):
        if duracion <= 0:
            raise ValueError("La duración de la misión no puede ser negativa o cero")
        astronauta.agregar_mision(nombre, destino, duracion, "Pendiente")
        if astronauta.get_nombre() not in self.__misiones:
            self.__misiones[astronauta.get_nombre()] = []
        self.__misiones[astronauta.get_nombre()].append((nombre, None))

    def evaluar_mision(self, astronauta, nombre_mision, evaluacion):
        for mision in self.__misiones[astronauta.get_nombre()]:
            if mision[0] == nombre_mision:
                mision[1] = evaluacion
                return
        raise ValueError(f"No se encontró la misión {nombre_mision} para evaluar")

    def informe_personal(self):
        informe = f"Resumen global de desempeño:\n"
        for astronauta, misiones in self.__misiones.items():
            informe += f"\nAstronauta: {astronauta}\n"
            for mision, evaluacion in misiones:
                informe += f"- Misión: {mision}, Evaluación: {evaluacion}\n"
        return informe

    def generar_informe_global(self, archivo="informe_misiones.txt"):
        with open(archivo, "w") as file:
            file.write(self.informe_personal())