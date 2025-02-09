import csv
from datetime import datetime
from database import SessionLocal
from models import Vuelo

def importar_csv(archivo_csv):
    session = SessionLocal()

    with open(archivo_csv, newline='', encoding="utf-8") as file:
        reader = csv.reader(file)
        next(reader)

        for row in reader:
            origen, destino, fecha, horario, disponibilidad = row

            nuevo_vuelo = Vuelo(
                origen = origen,
                destino = destino,
                fecha = datetime.strptime(fecha, "%Y-%m-%d").date(),
                horario = datetime.strptime(horario, "%H:%M").time(),
                disponibilidad = disponibilidad
            )

            session.add(nuevo_vuelo)

        session.commit()
        session.close()
        print("Datos importados correctamente.")

importar_csv("vuelos_publicos.csv")