from astronauta import Astronauta
from ingeniero import Ingeniero
from directorDeMision import DirectorDeMision

def main():
    try:
        # Crear objetos de cada tipo de persona
        astronauta = Astronauta("Juan Pérez", "12345678", "Argentina")
        ingeniero = Ingeniero("Maria López", "87654321", "España")
        director = DirectorDeMision("Carlos García", "11223344", "México")

        # Registrar sistemas supervisados por el ingeniero
        print("Agregando sistemas supervisados por el ingeniero...")
        ingeniero.agregar_sistema("Propulsión", "Óptimo")
        ingeniero.agregar_sistema("Vida", "Riesgo bajo")
        print(ingeniero.informe_personal())

        # Registrar misiones del astronauta
        print("\nAgregando misiones del astronauta...")
        astronauta.agregar_mision("Apollo 11", "Luna", 7, "Éxito")
        print(astronauta.informe_personal())

        # Director asigna una nueva misión al astronauta
        print("\nAsignando nueva misión al astronauta...")
        director.asignar_mision(astronauta, "Marte 1", "Marte", 100, "Exploración avanzada")
        print(astronauta.informe_personal())

        # Director evalúa el rendimiento de una misión
        print("\nEvaluando misión...")
        director.evaluar_mision(astronauta, "Marte 1", "Excelente")

        # Generar informe global por el director
        print("\nGenerando informe global...")
        director.generar_informe_global()
        print("Informe global generado: informe_misiones.txt")

    except ValueError as e:
        print(f"Error: {str(e)}")
        with open("log_errores.txt", "a") as log:
            log.write(f"Error: {str(e)}\n") #preguntarle a sesto tmb no te olvides 

if __name__ == "__main__":
    main()