class Persona:
    def __init__(self, nombre, dni, nacionalidad):
        self.__nombre = nombre
        self.__dni = dni
        self.__nacionalidad = nacionalidad

    def get_nombre(self):
        return self.__nombre

    def get_dni(self):
        return self.__dni

    def get_nacionalidad(self):
        return self.__nacionalidad

    def informe_personal(self):
        raise NotImplementedError("Este método debe ser implementado en las clases hijas")
