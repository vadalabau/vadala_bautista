from persona import Persona

class Astronauta(Persona):
    def __init__(self, nombre, dni, nacionalidad):
        super().__init__(nombre, dni, nacionalidad)
        self.__misiones = []  # Lista de tuplas (nombre, destino, duración, resultado)

    def agregar_mision(self, nombre, destino, duracion, resultado):
        if duracion <= 0:
            raise ValueError("La duración de la misión no puede ser negativa o cero")
        self.__misiones.append((nombre, destino, duracion, resultado))

    def informe_personal(self):
        informe = f"Informe de misiones de {self.get_nombre()}:\n"
        for mision in self.__misiones:
            informe += f"- Misión: {mision[0]}, Destino: {mision[1]}, Duración: {mision[2]} días, Resultado: {mision[3]}\n"
        return informe
