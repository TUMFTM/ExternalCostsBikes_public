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


class TierEbike:
    def __init__(self, date_start_in=datetime.strptime('22/01/01 00:00:00', '%y/%m/%d %H:%M:%S'), date_end_in=datetime.strptime('23/01/01 00:00:00', '%y/%m/%d %H:%M:%S')):
        self.type = 'pedelec'
        self.space = 1.6
        self.bat_capa = 0.518 # 518 Wh # Laut www.notebookcheck.com = 518 Wh für OKAI EB10
        self.hours_idling = TierEbike.annual_idling_db()
        # self.data_time = TierEbike.data_timerange(date_start_in, date_end_in)
        self.annual_mileage = TierEbike.annual_mileage_db()
        self.power_consumption_driving = TierEbike.power_consumption_driving()
        self.power_consumption_idling = TierEbike.power_consumption_idling()
        self.avg_power_consumption_per_vkm = TierEbike.power_consumption_driving() / TierEbike.annual_mileage_db()
        self.annual_usage_time = TierEbike.annual_usage_time()
        self.annual_parking_cost = TierEbike.annual_parking_cost_db()
        self.refresh_cache()

    def refresh_cache(self):
        self.hours_idling = TierEbike.annual_idling_db()
        # self.data_time = TierScooter.data_timerange(date_start_in, date_end_in)
        self.annual_mileage = TierEbike.annual_mileage_db()
        self.power_consumption_driving = TierEbike.power_consumption_driving()
        self.power_consumption_idling = TierEbike.power_consumption_idling()
        self.avg_power_consumption_per_vkm = TierEbike.power_consumption_driving() / TierEbike.annual_mileage_db()
        self.annual_usage_time = TierEbike.annual_usage_time()
        self.annual_parking_cost = TierEbike.annual_parking_cost_db()

    def space(self):
        return self.space
    
    def hours_idling(self):
        return self.hours_idling
    
    # def data_time(self):
    #     return self.data_time    
    
    def annual_mileage(self):
        return self.annual_mileage
    
    def annual_usage_time(self):
        return self.annual_usage_time
    
    def avg_power_consumption_per_vkm(self):
        return self.avg_power_consumption_per_vkm
    
    def annual_parking_cost(self):
        return self.annual_parking_cost
    
    # def retrieve_trips_db(self):
    #    sql_tier_ebike = substitute_sql_placeholders(os.path.join(python_root, "..", "sql", "tier_ebike_trips.sql"),{"limit":limit})
    #    tier_ebike_trips = pd.read_sql(sql_tier_ebike, connection)

    def retrieve_trips_db(self):
        date_start_in = datetime.strptime('22/01/01 00:00:00', '%y/%m/%d %H:%M:%S')
        date_end_in = datetime.strptime('23/01/01 00:00:00', '%y/%m/%d %H:%M:%S')
        sql_tier_ebike = substitute_sql_placeholders(os.path.join(python_root, "..", "sql", "tier_ebike_trips.sql"), {})
        tier_ebike_trips = pd.read_sql(sql_tier_ebike, connection)
        tier_ebike_trips = pd.read_sql(sql_tier_ebike, connection)
        return tier_ebike_trips

    @staticmethod
    def annual_mileage_db():
        sql_tier_ebike_mileage = substitute_sql_placeholders(os.path.join(python_root, "..", "sql", "ebike", "tier_ebike_annual_mileage.sql"),{})
        tier_ebike_annual_mileage = pd.read_sql(sql_tier_ebike_mileage, connection) 
        return tier_ebike_annual_mileage.loc[0, 'annual_mileage_km']
    
    @staticmethod
    def annual_idling_db():
        sql_tier_ebike_idling_hours = substitute_sql_placeholders(os.path.join(python_root, "..", "sql", "ebike", "tier_ebike_annual_idling.sql"),{})
        tier_ebike_annual_idling_hours = pd.read_sql(sql_tier_ebike_idling_hours, connection) 
        #return tier_ebike_annual_idling_hours.loc[0, 'annual_idling_time']
        return tier_ebike_annual_idling_hours.loc[0, 'duration_h_2022']
    
    # @staticmethod
    # def data_timerange(date_start_in, date_end_in):
    #     date_delta = 0
    #     sql_tier_ebike_date_minmax = substitute_sql_placeholders(os.path.join(python_root, "..", "sql", "ebike", "tier_ebike_date_min_max.sql"),{})
    #     tier_ebike_date_minmax_df = pd.read_sql(sql_tier_ebike_date_minmax, connection) 
    #     date_min_db = tier_ebike_date_minmax_df.loc[0, 'date_min_db']
    #     date_max_db = tier_ebike_date_minmax_df.loc[0, 'date_max_db']
    #     earliest = np.max([date_start_in, date_min_db])
    #     latest = np.min([date_end_in, date_max_db])
    #     date_delta = (latest - earliest)
    #     return date_delta
    
    @staticmethod
    def power_consumption_driving():
        sql_tier_ebike_power_consumption_driving = substitute_sql_placeholders(os.path.join(python_root, "..", "sql", "ebike", "tier_ebike_power_consumption_driving.sql"),{})
        tier_ebike_power_cons_driving = pd.read_sql(sql_tier_ebike_power_consumption_driving, connection) 
        tier_ebike_power_consumption_driving_kWh = tier_ebike_power_cons_driving.loc[0, 'consumption_soc'] * 0.518
        return tier_ebike_power_consumption_driving_kWh
    
    @staticmethod
    def power_consumption_idling():
        sql_tier_ebike_power_consumption_idling = substitute_sql_placeholders(os.path.join(python_root, "..", "sql", "ebike", "tier_ebike_power_consumption_idling.sql"),{})
        tier_ebike_power_cons_idling = pd.read_sql(sql_tier_ebike_power_consumption_idling, connection) 
        tier_ebike_power_consumption_idling_kWh = tier_ebike_power_cons_idling.loc[0, 'consumption_soc'] * 0.518
        return tier_ebike_power_consumption_idling_kWh
    
    @staticmethod
    def annual_usage_time():
        sql_tier_ebike_usage_time = substitute_sql_placeholders(os.path.join(python_root, "..", "sql", "ebike", "tier_ebike_annual_usage_time.sql"),{})
        tier_ebike_annual_usage_time =    pd.read_sql(sql_tier_ebike_usage_time, connection) 
        return tier_ebike_annual_usage_time.loc[0, 'annual_usage_time']
    
    @staticmethod
    def annual_parking_cost_db():
        sql_tier_ebike_parking_cost= substitute_sql_placeholders(os.path.join(python_root, "..", "sql", "ebike", "tier_ebike_annual_parking_cost.sql"),{})
        tier_ebike_annual_parking_cost = pd.read_sql(sql_tier_ebike_parking_cost, connection) 
        return tier_ebike_annual_parking_cost.loc[0, 'annual_parking_cost_euro']
    
    