import configparser

bullet_set = {'*', '-', '\u2022', '\u2023', '\u25e6', '\u2043', '\u204c', '\u204d', '\u2219'}

sqlColumns = ['DT_ID',
              'AREA',
              'ALERT',
              'RATED_CAPACITY',
              'TIME_STAMP',
              'LOAD_DATA',
              'ALERT_STATUS',
              'ENERGY',
              'MAKE',
              'MANUFACTURE_YEAR']

logicalReplacements = {
    'DT': 'DT_ID', 'DISTRIBUTION TRANSFORMER': 'DT_ID', 'MANUFACTURER': 'MAKE' ,'TRANSFORMERS': 'DT_ID',
    'Location': 'AREA', 'TRANSFORMER':  'DT_ID' , 'CAPACITY':'RATED_CAPACITY' , 'kW':'RATED_CAPACITY' ,
                       }

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
