from persona import Persona

class Director(Persona):
    def __init__(self, nombre, dni, nacionalidad):
        super().__init__(nombre, dni, nacionalidad)
        self.__astronautas = []

    def asignar_mision(self, astronauta, nombre, destino, duracion, resultado="Pendiente"):
        astronauta.agregar_mision(nombre, destino, duracion, resultado)
        if astronauta not in self.__astronautas:
            self.__astronautas.append(astronauta)

    def registrar_evaluacion(self, astronauta, nombre_mision, evaluacion):
        astronauta.evaluar_mision(nombre_mision, evaluacion)

    def generar_reporte_global(self):
        reporte = "REPORTE GLOBAL DE MISIONES:\n\n"
        for a in self.__astronautas:
            reporte += a.informe_personal() + "\n"
        with open("informe_misiones.txt", "w") as archivo: #preguntarle a sesto xd
            archivo.write(reporte)
        return reporte