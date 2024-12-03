import os
from sqlalchemy import (
    Column,
    ForeignKey,
    Integer,
    String,
    Text,
    TIMESTAMP,
    PrimaryKeyConstraint,
    create_engine,
)
from sqlalchemy.orm import relationship, declarative_base
from eralchemy2 import render_er

# Base para las clases de SQLAlchemy
DeclarativeBase = declarative_base()

# Modelo de usuario
class Usuario(DeclarativeBase):
    __tablename__ = 'usuarios'
    id_usuario = Column(Integer, primary_key=True)
    nombre_usuario = Column(String(30), nullable=False)
    correo = Column(String(100), nullable=False)
    contrasena = Column(String(20), nullable=False)
    foto_perfil = Column(String(255))
    fecha_creacion = Column(TIMESTAMP)

# Modelo de publicación
class Publicacion(DeclarativeBase):
    __tablename__ = 'publicaciones'
    id_publicacion = Column(Integer, primary_key=True)
    id_usuario = Column(Integer, ForeignKey('usuarios.id_usuario'), nullable=False)
    url_contenido = Column(String(255))
    descripcion = Column(String(150))
    fecha_creacion = Column(TIMESTAMP)
    usuario = relationship("Usuario")

# Modelo de comentario
class Comentario(DeclarativeBase):
    __tablename__ = 'comentarios'
    id_comentario = Column(Integer, primary_key=True)
    id_publicacion = Column(Integer, ForeignKey('publicaciones.id_publicacion'), nullable=False)
    id_usuario = Column(Integer, ForeignKey('usuarios.id_usuario'), nullable=False)
    contenido = Column(Text, nullable=False)
    fecha_creacion = Column(TIMESTAMP)
    publicacion = relationship("Publicacion")
    usuario = relationship("Usuario")

# Modelo de 'Me gusta'
class MeGusta(DeclarativeBase):
    __tablename__ = 'me_gustas'
    id_me_gusta = Column(Integer, primary_key=True)
    id_publicacion = Column(Integer, ForeignKey('publicaciones.id_publicacion'), nullable=False)
    id_usuario = Column(Integer, ForeignKey('usuarios.id_usuario'), nullable=False)
    fecha_creacion = Column(TIMESTAMP)
    publicacion = relationship("Publicacion")
    usuario = relationship("Usuario")

# Modelo de seguimiento
class Seguimiento(DeclarativeBase):
    __tablename__ = 'seguimientos'
    id_seguidor = Column(Integer, ForeignKey('usuarios.id_usuario'), nullable=False)
    id_seguido = Column(Integer, ForeignKey('usuarios.id_usuario'), nullable=False)
    fecha_creacion = Column(TIMESTAMP)
    __table_args__ = (
        PrimaryKeyConstraint('id_seguidor', 'id_seguido'),
    )
    seguidor = relationship("Usuario", foreign_keys=[id_seguidor])
    seguido = relationship("Usuario", foreign_keys=[id_seguido])

# Generación del diagrama a partir del modelo
try:
    render_er(DeclarativeBase, 'diagrama.png')
    print("¡Éxito! Revisa el archivo diagrama.png")
except Exception as error:
    print("Hubo un problema generando el diagrama.")
    raise error
