# -*- coding: utf-8 -*-
__author__ = 'SirHades696'
__email__ = 'djnonasrm@gmail.com'

from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os

database = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    path = os.path.abspath(os.path.dirname(__file__))
    app.config.from_mapping(
        SQLALCHEMY_DATABASE_URI='sqlite:///' + os.path.join(path,'pokemons.sqlite'),
        SQLALCHEMY_TRACK_MODIFICATIONS=False
    )
    
    database.init_app(app)
    api = Api(app)
    from . import db
    
    migrate.init_app(app,database)
    
    app.cli.add_command(db.load_data_command)
    
    from . import api_rest
    api.add_resource(api_rest.All_pks,"/all")
    api.add_resource(api_rest.Type,"/type/<string:type>")
    api.add_resource(api_rest.One_type,"/only/<string:type>")
    api.add_resource(api_rest.Name,"/name/<string:name>")
    api.add_resource(api_rest.Index,"/")
    return app
    
