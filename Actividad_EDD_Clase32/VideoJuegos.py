from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

Base = declarative_base()

class Consolas(Base):
    __tablename__ = 'tbl_consola'

    id = Column(Integer, primary_key = True)
    nombre = Column(String(100), nullable = False)
    marca = Column(String, nullable = False)
    videojuegos = relationship('Videojuegos', back_populates = 'consola')

class Videojuegos(Base):
    __tablename__ = 'tbl_videojuego'

    id = Column(Integer, primary_key = True)
    nombre = Column(String(100), nullable = False)
    genero = Column(String, nullable = False)
    consola_id = Column(Integer, ForeignKey('tbl_consola.id'))
    consola = relationship('Consolas', back_populates = 'videojuegos')

class Usuarios(Base):
    __tablename__ = 'tbl_usuario'

    id = Column(Integer, primary_key = True)
    nombre = Column(String(100), nullable = False)
    correo = Column(String, unique=True, nullable = False)
    videojuegos = Column(String, nullable = True)

engine = create_engine('sqlite:///videojuegos.db', echo = True)
Base.metadata.create_all(engine)