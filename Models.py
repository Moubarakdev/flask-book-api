from tkinter import CASCADE
from flask_sqlalchemy import SQLAlchemy
from flask import jsonify

database_name = "bookap"
# postgresql://postgres:moubarak@localhost:5432/bookap
database_path = "postgresql://{}:{}@{}/{}".format(
    'postgres', 'moubarak', 'localhost:5432', database_name)
db = SQLAlchemy()
'''
setup_db(app)
binds a flask application and a SQLAlchemy service
'''

def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    db.create_all()


# table categorie
class Categorie(db.Model):
    __tablename__ = 'categorie'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.String(), nullable=False)
    livres = db.relationship('Livre', backref='categorie', lazy=True)

    def __init__(self, name, description):
        self.name = name
        self.description = description

    def format(self):
        return {
            "id" : self.id,
            "name" : self.name,
            "description" : self.description
        }

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()



# table Livre
class Livre(db.Model):
    __tablename__ = 'livre'
    id = db.Column(db.Integer, primary_key=True)
    isbn = db.Column(db.Integer, unique=True, nullable=False)
    titre = db.Column(db.String(), nullable=False)
    date_publication = db.Column(db.Date(), nullable=False)
    auteur = db.Column(db.String(), nullable=False)
    editeur = db.Column(db.String(), nullable=False)
    categorie_id = db.Column(db.Integer, db.ForeignKey('categorie.id'), )

    def __init__(self, isbn, titre, categorie_id, date_publication, auteur, editeur):
        self.isbn = isbn
        self.titre = titre
        self.categorie_id = categorie_id
        self.date_publication = date_publication
        self.auteur = auteur
        self.editeur = editeur

    def format(self):
        return {
            "id" : self.id,
            "titre" : self.titre,
            "auteur" : self.auteur,
            "categorie_id" : self.categorie_id,
            "auteur" : self.auteur,
            "editeur" : self.editeur
        }

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
