# imports
import os
import pandas as pd
import numpy as np
import sys
from datetime import datetime

cdir = os.path.dirname('')
python_root = os.path.abspath(os.path.join(cdir, 'python'))
sys.path.append(python_root)
print('root: ', python_root)

from utils.Config import DBConfig
from utils.PSQLCommander import PSQLCommander, substitute_sql_placeholders
from sqlalchemy.engine import URL, create_engine

# DB connection
conf_path = os.path.abspath(os.path.join(python_root, "../config/db.conf"))
conf_template_path = os.path.abspath(os.path.join(python_root, "../config/db_template.conf"))
dbconfig = DBConfig(conf_path, conf_template_path)
con_url = URL.create(drivername="postgresql",
                    host=dbconfig.host,
                    port=dbconfig.port,
                    username=dbconfig.user,
                    password=dbconfig.password,
                    database=dbconfig.name)

engine = create_engine(con_url, echo=True)
connection = engine.raw_connection()
cursor= connection.cursor()
psqlcmd = PSQLCommander(cursor)


###############################################################


class MVGBike:
    def __init__(self, date_start_in=datetime.strptime('22/01/01 00:00:00', '%y/%m/%d %H:%M:%S'), date_end_in=datetime.strptime('23/01/01 00:00:00', '%y/%m/%d %H:%M:%S')):
        self.type = 'bicycle'
        self.space = 1.6 
        self.number_vehicles = MVGBike.number_vehicles_db() # 3851 # Überprüfen noch einmal
        self.hours_idling = MVGBike.annual_idling_db()
        # self.data_time = 365 
        self.annual_mileage = MVGBike.annual_mileage_db()
        self.power_consumption_driving = 0 
        self.power_consumption_idling = 0 
        self.avg_power_consumption_per_vkm = 0 
        self.annual_usage_time = MVGBike.annual_usage_time_db()
        self.annual_parking_cost = MVGBike.annual_parking_cost_db()
        self.annual_parking_cost_stations = 53920 # 160 * 337 # MVGBike.annual_parking_cost_stations_db() # TODO: Wieder einfügen
        self.refresh_cache()

    def refresh_cache(self):
        self.hours_idling = MVGBike.annual_idling_db()
        # self.data_time = 365 
        self.annual_mileage = MVGBike.annual_mileage_db()
        self.annual_usage_time = MVGBike.annual_usage_time_db()
        self.annual_parking_cost = MVGBike.annual_parking_cost_db()
        self.annual_parking_cost_stations = 53920 # 160 * 337 # MVGBike.annual_parking_cost_stations_db() # TODO: Wieder einfügen

    def space(self):
        return self.space
    
    def number_vehicles(self):
        return self.number_vehicles
    
    def hours_idling(self):
        return self.hours_idling
    
    def data_time(self):
        return self.data_time    
    
    def annual_mileage(self):
        return self.annual_mileage
    
    def annual_usage_time(self):
        return self.annual_usage_time
    
    def annual_parking_cost(self):
        return self.annual_parking_cost
    
    def annual_parking_cost_stations(self):
        return self.annual_parking_cost_stations


    @staticmethod
    def number_vehicles_db():
        sql_mvg_bicycle_number_vehicles = substitute_sql_placeholders(os.path.join(python_root, "..", "sql", "bicycle", "mvg_rad_number_vehicles.sql"),{})
        mvg_bicycle_number_vehicles =    pd.read_sql(sql_mvg_bicycle_number_vehicles, connection) 
        return mvg_bicycle_number_vehicles.loc[0, 'total_count']
    
    @staticmethod
    def annual_mileage_db():
        sql_mvg_bicycle_annual_mileage = substitute_sql_placeholders(os.path.join(python_root, "..", "sql", "bicycle", "mvgrad_annual_mileage.sql"),{})
        mvg_bicycle_annual_mileage =    pd.read_sql(sql_mvg_bicycle_annual_mileage, connection) 
        return mvg_bicycle_annual_mileage.loc[0, 'annual_mileage_km']
    
    @staticmethod
    def annual_idling_db():
        sql_mvg_bicycle_idling_hours = substitute_sql_placeholders(os.path.join(python_root, "..", "sql", "bicycle", "mvg_rad_annual_idling.sql"),{})
        mvg_bicycle_annual_idling_hours = pd.read_sql(sql_mvg_bicycle_idling_hours, connection) 
        return mvg_bicycle_annual_idling_hours.loc[0, 'annual_idling_hours']
    
    @staticmethod
    def annual_usage_time_db():
        sql_mvg_bicycle_usage_time = substitute_sql_placeholders(os.path.join(python_root, "..", "sql", "bicycle", "mvgrad_annual_usage_time.sql"),{})
        mvg_bicycle_annual_usage_time = pd.read_sql(sql_mvg_bicycle_usage_time, connection) 
        return mvg_bicycle_annual_usage_time.loc[0, 'usage_time_2022_h']
    
    @staticmethod
    def annual_parking_cost_db():
        sql_mvg_bicycle_parking_cost= substitute_sql_placeholders(os.path.join(python_root, "..", "sql", "bicycle", "mvgrad_annual_parking_cost.sql"),{})
        mvg_bicycle_annual_parking_cost = pd.read_sql(sql_mvg_bicycle_parking_cost, connection) 
        return mvg_bicycle_annual_parking_cost.loc[0, 'annual_parking_cost_euro']
    
    @staticmethod
    def annual_parking_cost_stations_db():
        sql_mvg_bicycle_parking_cost_stations = substitute_sql_placeholders(os.path.join(python_root, "..", "sql", "bicycle", "mvg_rad_stations_LU.sql"),{})
        mvg_bicycle_annual_parking_cost_stations = pd.read_sql(sql_mvg_bicycle_parking_cost_stations, connection) 
        return mvg_bicycle_annual_parking_cost_stations.loc[0, 'annual_stations_cost_euro']
    
    