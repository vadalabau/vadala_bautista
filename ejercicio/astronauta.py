# astronauta.py
from persona import Persona
from expeciones import DuracionNegativaError

class Astronauta(Persona):
    def __init__(self, nombre, dni, nacionalidad):
        super().__init__(nombre, dni, nacionalidad)
        self.__misiones = []

    def agregar_mision(self, nombre, destino, duracion, resultado):
        if duracion < 0:
            raise DuracionNegativaError("La duración no puede ser negativa")
        mision = {
            "nombre": nombre,
            "destino": destino,
            "duracion": duracion,
            "resultado": resultado,
            "evaluacion": None
        }