# -*- coding: utf-8 -*-
__author__ = 'SirHades696'
__email__ = 'djnonasrm@gmail.com'

from flask_restful import Resource
from app import db
db = db.PokemonsDB

class All_pks(Resource):
    def get(self):
        try:
            pks = db.query.all()
            lista = [pk.data() for pk in pks]
            return {
                "Total" : len(lista),
                "Pokemons": lista
                }
        except:
            return {"Panic":"We have a problem... :("}
        
class Type(Resource):
    def get(self, type):
        try:
            pks = db.query.filter(db.type.like('%' + type + '%')).all()
            lista = [pk.data() for pk in pks]
            return {
                "Total" : len(lista),
                "Pokemons": lista
                }
        except:
            return {"Panic":"We have a problem... :("}
        
class Name(Resource):
    def get(self, name):
        try:
            pks = db.query.filter(db.name.like('%' + name + '%')).all()
            lista = [pk.data() for pk in pks]
            return {
                    "Total" : len(lista),
                    "Pokemons": lista
                    }
        except:
            return {"Panic":"We have a problem... :("}

class One_type(Resource):
    def get(self, type):
        try:
            pks = db.query.filter_by(type=type.capitalize()).all()
            lista = [pk.data() for pk in pks]
            return {
                "Total":len(lista),
                "Pokemons": lista
            }
        except:
            return {"Panic":"We have a problem... :("}
        
class Index(Resource):
    def get(self):
        return {
            "Hi": {
            "API" : "Welcome to Pokémon DB API",
            "Version": 1.0,
            "Autor": "SirHades696",
            "Email" : "djnonasrm@gmail.com",
            "Web" : "https://sirhades696.herokuapp.com",
            "GitHub": "https://github.com/SirHades696",
            "GETs": ["/", '/type/<type>', "/name/<name>", "/all", "/only/<type>"]
            }
        }