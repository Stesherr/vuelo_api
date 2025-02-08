from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal, engine
import models, schemas, crud

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/api/vuelos")
def buscar_vuelos(origen: str, destino: str, fecha: str, db: Session = Depends(get_db)):
    return crud.buscar_vuelos(db, origen, destino, fecha)

@app.post("/api/reservas")
def reservar_vuelo(reserva: schemas.ReservaCreate, db: Session = Depends(get_db)):
    return crud.reservar_vuelo(db, reserva)