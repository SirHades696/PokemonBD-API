# -*- coding: utf-8 -*-
__author__ = 'SirHades696'
__email__ = 'djnonasrm@gmail.com'

from . import pokemons
pks = pokemons.values
import click 
from flask.cli import with_appcontext
from app import database

class PokemonsDB(database.Model):
    __tablename__ = 'Pokemons'
    id = database.Column(database.Integer, primary_key=True)
    name = database.Column(database.String(100))
    type = database.Column(database.String(100))
    total = database.Column(database.Integer)
    hp = database.Column(database.Integer)
    attack = database.Column(database.Integer)
    defense = database.Column(database.Integer)
    sp_atk = database.Column(database.Integer)
    sp_def = database.Column(database.Integer)
    speed = database.Column(database.Integer)
    src = database.Column(database.String(300))
    
    def data(self):
        return {
            "id": self.id,
            "name": self.name,
            "type": self.type,
            "total": self.total,
            "hp": self.hp,
            "attack" : self.attack,
            "defense" : self.defense,
            "sp_atk" : self.sp_atk,
            "sp_def" : self.sp_def,
            "speed" : self.speed,
            "img": self.src
        }

def load_data():
    for i, pk in enumerate(pks):
        new_pk = PokemonsDB(
            id=i,
            name=pk[1],
            type=pk[2],
            total=pk[3],
            hp=pk[4],
            attack=pk[5],
            defense=pk[6],
            sp_atk=pk[7],
            sp_def=pk[8],
            speed=pk[9],
            src=pk[10]
        )
        database.session.add(new_pk)
        
    database.session.commit()

@click.command('load-data')
@with_appcontext
def load_data_command():
    load_data()
    click.echo("Todos los pokemons fueron agregados a la BD...")