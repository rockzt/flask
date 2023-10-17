from dogtor.db import db
# Used to generated specific columns used by the model
from sqlalchemy.orm import mapped_column
# Importing datatypes for creating Model
from sqlalchemy import Integer, String, DateTime, ForeignKey
import datetime




# Inheriting from db model created by SQLAlchemy
class User(db.Model):
    """User Object"""
    id = mapped_column(Integer, primary_key=True)
    first_name = mapped_column(String(255), nullable=False)
    last_name = mapped_column(String(255), nullable=True)
    email = mapped_column(String(100), unique=True)
    password = mapped_column(String(100), nullable=False)



class Owner(db.Model):
    """Pet Owner Object"""
    id = mapped_column(Integer, primary_key=True)
    first_name = mapped_column(String(length=50))
    last_name = mapped_column(String(length=50))
    phone = mapped_column(String(length=15))
    mobile = mapped_column(String(length=15))
    email = mapped_column(String(), unique=True)
    # Foreign Key to connect with Specie Model  'modelname_id' ,  column that is related to the main Model
    pets = db.relationship("Pet", back_populates="owner")


class Specie(db.Model):
    id = mapped_column(Integer, primary_key=True)
    name = mapped_column(String(25))
    pets = db.relationship("Pet", back_populates="species")


class Pet(db.Model):
    id = mapped_column(Integer, primary_key=True)
    name = mapped_column(String(255))
    # Take two parameters (model, reference name model where we are calling the model linked)
    owner_id = mapped_column(Integer, ForeignKey("owner.id"))
    age = mapped_column(Integer)
    specie_id = mapped_column(Integer, ForeignKey("specie.id"))
    record_id = mapped_column(Integer, ForeignKey("record.id"))
    species = db.relationship("Specie", back_populates="pets")
    owner = db.relationship("Owner", back_populates="pets")
    records = db.relationship("Record", back_populates="pet")

record_category_m2m = db.Table(
    "record_category",
    db.Column("record_id", Integer, db.ForeignKey("record.id")),
    db.Column("category_id", Integer, db.ForeignKey("category.id")),
)



class Record(db.Model):

    id = mapped_column(Integer, primary_key=True)
    procedure = mapped_column(String(255))
    date = mapped_column(DateTime)
    pet = db.relationship("Pet", back_populates="records")
    created_at = mapped_column(DateTime, default=db.func.datetime)
    categories = db.relationship(
        "Category", secondary=record_category_m2m, back_populates="records"
    )



class Category(db.Model):
    """Record category object"""
    id = db.Column(Integer, primary_key=True)
    name = db.Column(String(length=20))
    records = db.relationship(
        "Record", secondary=record_category_m2m, back_populates="categories"
    )
