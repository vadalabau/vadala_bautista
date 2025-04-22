from expeciones import DatosIncompletosError

class Persona:
    def __init__(self, nombre, dni, nacionalidad):
        if not nombre or not dni or not nacionalidad:
            raise DatosIncompletosError("Faltan datos obligatorios")
        self.__nombre = nombre
        self.__dni = dni
        self.__nacionalidad = nacionalidad

    def get_nombre(self):
        return self.__nombre