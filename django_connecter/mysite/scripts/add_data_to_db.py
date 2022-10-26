from polls.models import Transformer, Events
import pandas as pd


def run():
    addDataToTransformer()
    addEvents()


def addDataToTransformer():
    df = pd.read_csv(r"C:\Tamil\temp\db_chatbot\django_connecter\mysite\csv\DT_details.csv")
    df.Year_of_manufacturer = df.Year_of_manufacturer.astype('datetime64[ns]')

    for row in df.itertuples():
        transformer = Transformer()
        transformer.Manufacturer_name = row.Manufacturer_name
        transformer.Transformer_location_name = row.Transformer_location_name
        transformer.Transformer_number = row.Transformer_number
        transformer.Meter_number = row.Meter_number
        transformer.Manufacturer_Serial_number = row.Manufacturer_Serial_number
        transformer.Section = row.Section
        transformer.Sub_Division = row.Sub_Division
        transformer.Division = row.Division
        transformer.Circle = row.Circle
        transformer.Region = row.Region
        transformer.Latitude = row.Latitude
        transformer.Longitude = row.Longitude
        transformer.Status = row.Status
        transformer.Transformers_Name_plate = row.Transformers_Name_plate
        transformer.KVA = row.KVA
        transformer.Volts_H_V = row.Volts_H_V
        transformer.Volts_L_V = row.Volts_L_V
        transformer.Amperes_H_V = row.Amperes_H_V
        transformer.Amperes_L_V = row.Amperes_L_V
        transformer.Phases_HV = row.Phases_HV
        transformer.Phases_LV = row.Phases_LV
        transformer.Type_of_Cooling = row.Type_of_Cooling
        transformer.Impedance_volts = row.Impedance_volts
        transformer.Connection_symbols = row.Connection_symbols
        transformer.Core_and_winding = row.Core_and_winding
        transformer.Total_weight = row.Total_weight
        transformer.Oil = row.Oil
        transformer.Year_of_manufacturer = row.Year_of_manufacturer
        transformer.save()


def addEvents():
    df = pd.read_csv(r"C:\Tamil\temp\db_chatbot\django_connecter\mysite\csv\5_DT_Data.csv")

    rename_columns = {'transformer': 'mainId',
                      'Date & Time Stamp': 'Time_Stamp',
                      'V(R)': 'V_R',
                      'V(Y)': 'V_Y',
                      'V(B)': 'V_B',
                      'VRB': 'VRB',
                      'VRY': 'VRY',
                      'VYB': 'VYB',
                      'I(R)': 'I_R',
                      'I(Y)': 'I_Y',
                      'I(B)': 'I_B',
                      'kW': 'kW',
                      'kVA': 'kVA',
                      'PF(R)': 'PF_R',
                      'PF(Y)': 'PF_Y',
                      'PF(B)': 'PF_B',
                      'THD(V-R)': 'THD_V_R',
                      'THD(V-Y)': 'THD_V_Y',
                      'THD(V-B)': 'THD_V_B',
                      'THD(I-R)': 'THD_I_R',
                      'THD(I-Y)': 'THD_I_Y',
                      'THD(I-B)': 'THD_I_B',
                      'FREQUENCY': 'FREQUENCY',
                      'Frwd.kWh': 'Frwd_kWh',
                      'REV.ACTENERGY': 'REV_ACTENERGY',
                      'FRWD.APPENERGY': 'FRWD_APPENERGY',
                      'FRWD.REACTENERGY': 'FRWD_REACTENERGY',
                      'kVA-R': 'kVA_R',
                      'kVA-Y': 'kVA_Y',
                      'kVA-B': 'kVA_B',
                      'KVAH.FWD': 'KVAH_FWD',
                      'KVAH.REV': 'KVAH_REV',
                      'kVAr-R': 'kVAr_R',
                      'KVARH.LAG.FWD': 'KVARH_LAG_FWD',
                      'KVARH.LAG.REV': 'KVARH_LAG_REV',
                      'KVARH.LEAD.FWD': 'KVARH_LEAD_FWD',
                      'KVARH.LEAD.REV': 'KVARH_LEAD_REV',
                      'kVAr-Y': 'kVAr_Y',
                      'kVAr-B': 'kVAr_B',
                      'kWH-Fwd': 'kWH_Fwd',
                      'KWH.REV': 'KWH_REV',
                      'kW-R': 'kW_R',
                      'kW-Y': 'kW_Y',
                      'kW-B': 'kW_B',
                      'kVA.1': 'kVA_1',
                      'REV.APPENERGY': 'REV_APPENERGY',
                      'REV.REACTENERGY': 'REV_REACTENERGY',
                      'TOT.kVAh': 'TOT_kVAh',
                      'TOT.KVARH.LEG': 'TOT_KVARH_LEG',
                      'TOT.kWh/Fwd.kWh/Active Energy Sent Out': 'TOT_kWh_Fwd_kWh_Active_Energy_Sent_Out',
                      'Unnamed: 51': 'Unnamed_column1',
                      'TEMP4': 'TEMP4',
                      'TOT.KVAH': 'TOT_KVAH_1',
                      'TOT.KVARH.LEG.1': 'TOT_KVARH_LEG_1',
                      'TOT.KWH': 'TOT_KWH'}

    df = df.rename(columns=rename_columns)
    df.Time_Stamp = df.Time_Stamp.astype('datetime64[ns]')
    df.KVAH_FWD = df.KVAH_FWD.apply(lambda x: x.replace(',', '').replace('-', '0')).astype('float')
    df.KVARH_LEAD_REV = df.KVARH_LEAD_REV.apply(lambda x: x.replace(',', '').replace('-', '0')).astype('float')
    df.kWH_Fwd = df.kWH_Fwd.apply(lambda x: x.replace(',', '').replace('-', '0')).astype('float')
    df.TOT_KVARH_LEG = df.TOT_KVARH_LEG.apply(lambda x: x.replace(',', '').replace('-', '0')).astype('float')
    df.TOT_KVARH_LEG_1 = df.TOT_KVARH_LEG_1.apply(lambda x: x.replace(',', '').replace('-', '0')).astype('float')
    df.FRWD_APPENERGY = df.FRWD_APPENERGY.apply(lambda x: x.replace(',', '')).astype('float')
    df.FRWD_REACTENERGY = df.FRWD_REACTENERGY.apply(lambda x: x.replace(',', '')).astype('float')
    df.kVA_Y = df.kVA_Y.apply(lambda x: x.replace(',', '')).astype('float')
    df.kVAr_R = df.kVAr_R.apply(lambda x: x.replace(',', '')).astype('float')
    df.KVARH_LAG_REV = df.KVARH_LAG_REV.apply(lambda x: x.replace(',', '')).astype('float')
    df.KVARH_LEAD_FWD = df.KVARH_LEAD_FWD.apply(lambda x: x.replace(',', '')).astype('float')
    df.KWH_REV = df.KWH_REV.apply(lambda x: x.replace(',', '').replace('-', '0')).astype('float')
    df.TOT_KVAH_1 = df.TOT_KVAH_1.apply(lambda x: x.replace(',', '')).astype('float')
    df.Frwd_kWh = df.Frwd_kWh.apply(lambda x: x.replace(',', '')).astype('float')
    df.TOT_KWH = df.TOT_KWH.apply(lambda x: x.replace(',', '')).astype('float')
    df.REV_ACTENERGY = df.REV_ACTENERGY.apply(lambda x: x.replace('-', '0')).astype('float')
    df.kW_R = df.kW_R.apply(lambda x: x.replace('-', '0')).astype('float')
    df.TOT_kWh_Fwd_kWh_Active_Energy_Sent_Out = df.TOT_kWh_Fwd_kWh_Active_Energy_Sent_Out. \
        apply(lambda x: x.replace(',', '').replace('-', '0')).astype('float')
    df.Unnamed_column1 = df.Unnamed_column1.apply(lambda x: x.replace(',', '').replace('-', '0')).astype('float')
    df.KVARH_LAG_FWD = df.KVARH_LAG_FWD.apply(lambda x: x.replace(',', '').replace('-', '0')).astype('float')

    # dt = Transformer()

    for row in df.itertuples():
        dtEvents = Events()
        dtEvents.mainId = Transformer.objects.get(Transformer_number=row.mainId)
        dtEvents.Time_Stamp = row.Time_Stamp
        dtEvents.V_R = row.V_R
        dtEvents.V_Y = row.V_Y
        dtEvents.V_B = row.V_B
        dtEvents.VRB = row.VRB
        dtEvents.VRY = row.VRY
        dtEvents.VYB = row.VYB
        dtEvents.I_R = row.I_R
        dtEvents.I_Y = row.I_Y
        dtEvents.I_B = row.I_B
        dtEvents.kW = row.kW
        dtEvents.kVA = row.kVA
        dtEvents.PF_R = row.PF_R
        dtEvents.PF_Y = row.PF_Y
        dtEvents.PF_B = row.PF_B
        dtEvents.THD_V_R = row.THD_V_R
        dtEvents.THD_V_Y = row.THD_V_Y
        dtEvents.THD_V_B = row.THD_V_B
        dtEvents.THD_I_R = row.THD_I_R
        dtEvents.THD_I_Y = row.THD_I_Y
        dtEvents.THD_I_B = row.THD_I_B
        dtEvents.FREQUENCY = row.FREQUENCY
        dtEvents.Frwd_kWh = row.Frwd_kWh
        dtEvents.REV_ACTENERGY = row.REV_ACTENERGY
        dtEvents.FRWD_APPENERGY = row.FRWD_APPENERGY
        dtEvents.FRWD_REACTENERGY = row.FRWD_REACTENERGY
        dtEvents.kVA_R = row.kVA_R
        dtEvents.kVA_Y = row.kVA_Y
        dtEvents.kVA_B = row.kVA_B
        dtEvents.KVAH_FWD = row.KVAH_FWD
        dtEvents.KVAH_REV = row.KVAH_REV
        dtEvents.kVAr_R = row.kVAr_R
        dtEvents.KVARH_LAG_FWD = row.KVARH_LAG_FWD
        dtEvents.KVARH_LAG_REV = row.KVARH_LAG_REV
        dtEvents.KVARH_LEAD_FWD = row.KVARH_LEAD_FWD
        dtEvents.KVARH_LEAD_REV = row.KVARH_LEAD_REV
        dtEvents.kVAr_Y = row.kVAr_Y
        dtEvents.kVAr_B = row.kVAr_B
        dtEvents.kWH_Fwd = row.kWH_Fwd
        dtEvents.KWH_REV = row.KWH_REV
        dtEvents.kW_R = row.kW_R
        dtEvents.kW_Y = row.kW_Y
        dtEvents.kW_B = row.kW_B
        dtEvents.kVA_1 = row.kVA_1
        dtEvents.REV_APPENERGY = row.REV_APPENERGY
        dtEvents.REV_REACTENERGY = row.REV_REACTENERGY
        dtEvents.TOT_kVAh = row.TOT_kVAh
        dtEvents.TOT_kWh_Fwd_kWh_Active_Energy_Sent_Out = row.TOT_kWh_Fwd_kWh_Active_Energy_Sent_Out
        dtEvents.Unnamed_column1 = row.Unnamed_column1
        dtEvents.TEMP4 = row.TEMP4
        dtEvents.TOT_KVAH_1 = row.TOT_KVAH_1
        dtEvents.TOT_KVARH_LEG = row.TOT_KVARH_LEG
        dtEvents.TOT_KVARH_LEG_1 = row.TOT_KVARH_LEG_1
        dtEvents.TOT_KWH = row.TOT_KWH
        dtEvents.save()