from persona import Persona

class Ingeniero(Persona):
    def __init__(self, nombre, dni, nacionalidad):
        super().__init__(nombre, dni, nacionalidad)
        self.__sistemas = []  # Lista de tuplas (sistema, estado)

    def agregar_sistema(self, sistema, estado):
        if (sistema, estado) in self.__sistemas:
            raise ValueError("Este sistema ya fue registrado")
        self.__sistemas.append((sistema, estado))

    def informe_personal(self):
        informe = f"Informe técnico de {self.get_nombre()}:\n"
        for sistema, estado in self.__sistemas:
            informe += f"- {sistema}: {estado}\n"
        return informe