import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Planets(Base):
    __tablename__ = 'planets'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    fav_id = Column(Integer, ForeignKey('favorites.id'))
    name = Column(String(250), nullable=False)
    climate = Column(String(250))
    diameter = Column(Integer)
    terrain = Column(String(250))
    population = Column(Integer)
    orbital_period = Column(Integer)
    planets = relationship('Favorites')

    def to_dict(self):
        return {}

class Characters(Base):
    __tablename__ = 'characters'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    fav_id = Column(Integer, ForeignKey('favorites.id'))
    name = Column(String(250), nullable=False)
    bithyear = Column(Integer)
    eye_color = Column(String(250))
    hair_color = Column(String(250))
    skin_color = Column(String(250))
    gender = Column(String(250))
    characters = relationship('Favorites')

    def to_dict(self):
        return {}

class Favorites(Base):
    __tablename__ = 'favorites'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    planets = Column(String(250))
    characters = Column(String(250))
    favorites = relationship('Users')

    def to_dict(self):
        return {}

class Users(Base):
    __tablename__ = 'users'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    user_id = Column(Integer, primary_key=True)
    email = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)
    users = relationship('Favorites')

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
