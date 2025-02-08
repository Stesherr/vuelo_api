from pydantic import BaseModel, EmailStr
from datetime import date, time
from typing import Optional

class UsuarioCreate(BaseModel):
    nombre: str
    correo: EmailStr
    contraseña: str

class UsuarioResponse(BaseModel):
    id: int
    nombre: str
    correo: EmailStr

    class config:
        orm_mode = True

class UsuarioLogin(BaseModel):
    correo: EmailStr
    contraseña: str

class VueloResponse(BaseModel):
    id: int
    origen: str
    destino: str
    fecha: date
    horario: time
    disponibilidad: int

    class Config:
        orm_mode = True

class ReservaCreate(BaseModel):
    usuario_id: int
    vuelo_id: int

class ReservaResponse(BaseModel):
    id: int
    usuario_id: int
    vuelo_id: int
    estado: str

    class Config:
        orm_mode = True