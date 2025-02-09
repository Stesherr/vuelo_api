from fastapi import FastAPI, Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from auth import oauth2_scheme
from database import SessionLocal, engine
import models, schemas, crud, auth

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/token")
def login(usuario: schemas.UsuarioLogin, db: Session = Depends(get_db)):
    return auth.autenticar_usuario(db, usuario.correo, usuario.contraseña)

@app.post("/api/usuarios")
def registrar_usuario(usuario: schemas.UsuarioCreate, db: Session = Depends(get_db)):
    return crud.crear_usuario(db, usuario)

@app.get("/api/vuelos")
def buscar_vuelos(origen: str, destino: str, fecha: str, db: Session = Depends(get_db)):
    return crud.buscar_vuelos(db, origen, destino, fecha)

@app.post("/api/reservas")
def reservar_vuelo(reserva: schemas.ReservaCreate, db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    return crud.reservar_vuelo(db, reserva)

@app.delete("/api/reservas/{id}")
def cancelar_reserva(id: int, db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    return crud.cancelar_reserva(db, id)

@app.get("/api/usuarios/{usuario_id}/reservas")
def listar_reservas_usuario(usuario_id: int, db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    return crud.listar_reservas_usuario(db, usuario_id)

