from sqlalchemy.orm import Session
from fastapi import HTTPException
import models, schemas
from auth import get_password_hash, verify_password

def buscar_vuelos(db: Session, origen: str, destino: str, fecha: str):
    return db.query(models.Vuelo).filter(
        models.Vuelo.origen == origen, 
        models.Vuelo.destino == destino, 
        models.Vuelo.fecha == fecha
    ).all()

def reservar_vuelo(db: Session, reserva: schemas.ReservaCreate):
    vuelo = db.query(models.Vuelo).filter(
        models.Vuelo.id == reserva.vuelo_id, 
        models.Vuelo.disponibilidad > 0
    ).first()

    if not vuelo:
        raise HTTPException(status_code=400, detail="Vuelo no disponible")
    
    nueva_reserva = models.Reserva(usuario_id=reserva.usuario_id, vuelo_id=reserva.vuelo_id)
    db.add(nueva_reserva)
    vuelo.disponibilidad -= 1
    db.commit()
    return{"mensaje": "Reserva confirmada"}

def cancelar_reserva(db: Session, reserva_id: int):
    reserva = db.query(models.Reserva).filter(models.Reserva.id == reserva_id).first()

    if not reserva:
        raise HTTPException(status_code=404, detail="Reserva no encontrada")
    
    db.delete(reserva)
    db.commit()
    return {"mensaje": "Reserva cancelada"}

def listar_reservas_usuario(db: Session, usuario_id: int):
    reservas = db.query(models.Reserva).filter(models.Reserva.usuario_id == usuario_id).all()
    return reservas

def obtener_usuario_por_correo(db: Session, correo: str):
    return db.query(models.Usuario).filter(models.Usuario.correo == correo).first()

def crear_usuario(db: Session, usuario: schemas.UsuarioCreate):
    hasesh_password = get_password_hash(usuario.contraseña)
    nuevo_usuario = models.Usuario(nombre=usuario.nombre, correo=usuario.correo, contraseña=hasesh_password)
    db.add(nuevo_usuario)
    db.commit()
    db.refresh(nuevo_usuario)
    return{"mensaje": "Usuario registrado con éxito"}

