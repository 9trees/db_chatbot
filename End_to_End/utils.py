import configparser
from functools import wraps
from time import time
import pandas as pd
from connect_to_db import connectToSqliteDB

bullet_set = {'*', '-', '\u2022', '\u2023', '\u25e6', '\u2043', '\u204c', '\u204d', '\u2219'}

sqlColumns = ['Time_Stamp', 'V_R', 'V_Y', 'V_B', 'VRB', 'VRY', 'VYB', 'I_R', 'I_Y',
              'I_B', 'kW', 'kVA', 'PF_R', 'PF_Y', 'PF_B', 'THD_V_R', 'THD_V_Y',
              'THD_V_B', 'THD_I_R', 'THD_I_Y', 'THD_I_B', 'FREQUENCY', 'Frwd_kWh',
              'REV_ACTENERGY', 'FRWD_APPENERGY', 'FRWD_REACTENERGY', 'kVA_R', 'kVA_Y',
              'kVA_B', 'KVAH_FWD', 'KVAH_REV', 'kVAr_R', 'KVARH_LAG_FWD',
              'KVARH_LAG_REV', 'KVARH_LEAD_FWD', 'KVARH_LEAD_REV', 'kVAr_Y', 'kVAr_B',
              'kWH_Fwd', 'KWH_REV', 'kW_R', 'kW_Y', 'kW_B', 'kVA_1', 'REV_APPENERGY',
              'REV_REACTENERGY', 'TOT_kVAh', 'TOT_KVARH_LEG',
              'TOT_kWh_Fwd_kWh_Active_Energy_Sent_Out', 'Unnamed_column1', 'TEMP4',
              'TOT_KVAH_1', 'TOT_KVARH_LEG_1', 'TOT_KWH', 'mainId_id']

logicalReplacements = {
    'DT': 'DT_ID', 'DISTRIBUTION TRANSFORMER': 'DT_ID', 'MANUFACTURER': 'MAKE', 'TRANSFORMERS': 'DT_ID',
    'Location': 'AREA', 'TRANSFORMER': 'DT_ID', 'CAPACITY': 'RATED_CAPACITY', 'kW': 'RATED_CAPACITY',
    'TIME STAMP': 'Time_Stamp', 'VR': 'V_R'

}

tables = ['polls_events', 'polls_transformer']


def getConfig():
    """
    Returns config parameters using the configFile.ini file.

            Parameters:
                    None

            Returns:
                    config parameters (dict): A python dictionary
    """
    config_obj = configparser.ConfigParser()
    config_obj.read("configFile.ini")
    APIEndPoint = config_obj["APIEndPoint"]
    host = APIEndPoint['host']
    port = APIEndPoint['port']

    dbCreds = config_obj["dbCreds"]
    dbName = dbCreds['Name']
    TableName = dbCreds['TableName']

    return {
        "host": host,
        "port": port,
        'DBName': dbName,
        "TableName": TableName
    }


configs = getConfig()


def measure(func):
    @wraps(func)
    def _time_it(*args, **kwargs):
        start = int(round(time() * 1000))
        try:
            return func(*args, **kwargs)
        finally:
            end_ = int(round(time() * 1000)) - start
            # print(func.__name__)
            print(f"Total execution time: {end_ if end_ > 0 else 0} ms")

    return _time_it


def getTheColumns():
    columnsDict = {}
    for i in tables:
        columnsDict[i] = list(pd.read_sql("select * from " + i, con=connectToSqliteDB()))
    return columnsDict
