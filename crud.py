from sqlalchemy.orm import Session
from fastapi import HTTPException
import models, schemas

def buscar_vuelos(db: Session, origen: str, destino: str, fecha: str):
    return db.query(models.Vuelo).filter(models.Vuelo.origen == origen, models.Vuelo.destino == destino, models.Vuelo.fecha == fecha).all()

def reservar_vuelo(db: Session, reserva: schemas.ReservaCreate):
    vuelo = db.query(models.Vuelo).filter(models.Vuelo.id == reserva.vuelo_id, models.Vuelo.disponibilidad > 0).first()
    if not vuelo:
        raise HTTPException(status_code=400, detail="Vuelo no disponible")
    
    nueva_reserva = models.Reserva(usuario_id=reserva.usuario_id, vuelo_id=reserva.vuelo_id)
    db.add(nueva_reserva)
    vuelo.disponibilidad -= 1
    db.commit()
    return{"mensaje": "Reserva confirmada"}
