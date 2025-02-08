from sqlalchemy import Column, Integer, String, Date, Time, ForeignKey
from database import Base

class Usuario(Base):
    __tablename__ = "usuarios"
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(255), nullable=False)
    correo = Column(String(255), unique=True, nullable=False)
    contraseña = Column(String(255), nullable=False)

class Vuelo(Base):
    __tablename__ = "vuelos"
    id = Column(Integer, primary_key=True, index=True)
    origen = Column(String(100), nullable=False)
    destino = Column(String(100), nullable=False)
    fecha = Column(Date, nullable=False)
    horario = Column(Time, nullable=False)
    disponibilidad = Column(Integer, nullable=False)

class Reserva(Base):
    __tablename__ = "reservas"
    id = Column(Integer, primary_key=True, index=True)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"))
    vuelo_id = Column(Integer, ForeignKey("vuelos.id"))
    estado = Column(String(50), default="confirmada")
