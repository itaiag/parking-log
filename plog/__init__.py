import logging
from os import path

from flask import Flask
import logging as log

from flask_restful import Api

from plog.db.database_initializer import init_database
from definitions import root_dir, database_name
from plog.resource.resources import Park, Car, ParkSpotList, CarList

log.basicConfig(filename=path.join(root_dir, 'plog.log'), encoding='utf-8', level=logging.DEBUG)

app = Flask(__name__)
api = Api(app)
api.add_resource(Park, '/api/v1/park')
api.add_resource(CarList, '/api/v1/car')
api.add_resource(Car, '/api/v1/car/<car_id>')
api.add_resource(ParkSpotList, '/api/v1/spot')

if not path.exists(path.join(root_dir, database_name)):
    log.info("Database is not exist. Creating new database")
    init_database()

import plog.views