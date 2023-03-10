from flask_sqlalchemy import SQLAlchemy

db=SQLAlchemy()

class Fact(db.Model):
    __tablename__="facts"

    id = db.Column(db.Integer, primary_key=True)
    submitter = db.Column(db.String(250))
    fact = db.Column(db.Text)

class Pet(db.Model):
    __tablename__="pets"

    pet_id = db.Column(db.Integer, primary_key=True)
    pet_name = db.Column(db.String(250))
    pet_photo = db.Column(db.String(500))
    pet_fact = db.Column(db.Text)
