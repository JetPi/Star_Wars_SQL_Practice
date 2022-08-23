import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(150), nullable=False)
    password = Column(String(100), nullable=False)

    def __init__(self, user_name, user_password):
        self.name = user_name
        self.password = user_password

class Favorites(Base):
    __tablename__ = 'favorites'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    character_id = Column(Integer, ForeignKey("character.id"))
    character = relationship("Character")
    planet_id = Column(Integer, ForeignKey("planet.id"))
    planet = relationship("Planet")
    user_id = Column(Integer, ForeignKey("user.id"))
    user = relationship("User")

    def add_favorite_char(self, char_id):
        self.character_id = char_id 
    
    def add_favorite_plan(self, planet_id):
        self.planet_id = planet_id 

class Character(Base):
    __tablename__ = 'character'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(150), nullable=False)
    image = Column(String(250), nullable=False)     
    age = Column(String(5), nullable=False)
    height = Column(String(5), nullable=False)
    # person_id = Column(Integer, ForeignKey('user.id'))
    # person = relationship(Person)

class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    name = Column(String(150), nullable=False)
    image = Column(String(250), nullable=False)     #?
    rotation_period = Column(String(7), nullable=False)
    orbital_period = Column(String(7), nullable=False)
    gravity = Column(String(5), nullable=False)
    terrain = Column(String(150), nullable=False)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')