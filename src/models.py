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
    password = Column(String(25), nullable=False)
    favorite_char_id = Column(Integer, ForeignKey("character.id"))
    favorite_char = relationship("Character")
    favorite_plan_id = Column(Integer, ForeignKey("planet.id"))
    favorite_plan = relationship("Planet")

class Character(Base):
    __tablename__ = 'character'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(150), nullable=False)
    image = Column(String(250))     #?
    age = Column(String(5), nullable=False)
    height = Column(String(5), nullable=False)
    # person_id = Column(Integer, ForeignKey('user.id'))
    # person = relationship(Person)

class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    name = Column(String(150), nullable=False)
    image = Column(String(250))     #?
    rotation_period = Column(String(7), nullable=False)
    orbital_period = Column(String(7), nullable=False)
    gravity = Column(String(5), nullable=False)
    terrain = Column(String(150), nullable=False)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')