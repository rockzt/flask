from dogtor.db import db
# Used to generated specific columns used by the model
from sqlalchemy.orm import mapped_column
# Importing datatypes for creating Model
from sqlalchemy import Integer, String, DateTime, ForeignKey
from enum import Enum
import datetime




# Inheriting from db model created by SQLAlchemy
class User(db.Model):
    """User Object"""
    id = mapped_column(Integer, primary_key=True)
    username = mapped_column(String(255), unique=True, nullable=False)
    email = mapped_column(String(100), unique=True)



class Owner(db.Model):
    """Pet Owner Object"""
    id = mapped_column(Integer, primary_key=True)
    first_name = mapped_column(String(length=50))
    last_name = mapped_column(String(length=50))
    phone = mapped_column(String(length=15))
    mobile = mapped_column(String(length=15))
    email = mapped_column(String(), unique=True)
    # Foreign Key to connect with Specie Model  'modelname_id' ,  column that is related to the main Model
    pets = db.relationship("Pet", backref="owner")


class Specie(db.Model):
    id = mapped_column(Integer, primary_key=True)
    name = mapped_column(String(255))
    pet = db.relationship("Pet", backref="specie")


class Pet(db.Model):
    id = mapped_column(Integer, primary_key=True)
    name = mapped_column(String(255))
    # Take two parameters (model, reference name model where we are calling the model linked)
    owner_id = mapped_column(Integer, ForeignKey("owner.id"))
    age = mapped_column(Integer)
    specie_id = mapped_column(Integer, ForeignKey("specie.id"))
    record_id = mapped_column(Integer, ForeignKey("record.id"))



class Category(Enum):
    OTHER = 0
    BLOOD_PRESSURE = 1
    BLOOD_SUGAR = 2
    BLOOD_GLUCOSE = 3
    BLOOD_OXYGEN = 4
    VACCINATION = 5
class Record(db.Model):
    id = mapped_column(Integer, primary_key=True)
    category = mapped_column(db.Enum(Category))
    procedure = mapped_column(String(255))
    date = mapped_column(DateTime)
    pet = db.relationship("Pet", backref="records")
    created_at = mapped_column(DateTime, default=db.func.datetime)
