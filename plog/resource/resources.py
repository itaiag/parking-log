from datetime import datetime

from flask import request
from flask_restful import Resource, reqparse

from definitions import date_time_format
from plog.db.database_operations import *


class Park(Resource):

    def get(self):
        return get_parking()

    def post(self):
        car_id = request.form['car_id']
        park_spot_id = request.form['park_spot_id']
        driver = request.form['driver']
        now = datetime.now()
        dt = now.strftime(date_time_format)
        add_park(dt, car_id, park_spot_id, driver)
        return get_parking()


class CarList(Resource):

    def post(self):
        car_name = request.form['car_name']
        add_car(car_name)
        return get_cars()

    def get(self):
        return get_cars()


class Car(Resource):

    def get(self, car_id):
        return get_car(car_id)

    def delete(self, car_id):
        return delete_car(car_id)


class ParkSpotList(Resource):

    def get(self):
        return get_parking_spots()

