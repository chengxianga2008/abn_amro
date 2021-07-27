# -*- coding: utf-8 -*-
import pandas as pd
from collections import OrderedDict

cols = {"RECORD CODE": 3, "CLIENT TYPE": 4, "CLIENT NUMBER": 4, "ACCOUNT NUMBER": 4, "SUBACCOUNT NUMBER": 4,
        "OPPOSITE PARTY CODE": 6, "PRODUCT GROUP CODE": 2, "EXCHANGE CODE": 4, "SYMBOL": 6, "EXPIRATION DATE": 8, "CURRENCY CODE": 3,
        "MOVEMENT CODE": 2, "BUY SELL CODE": 1, "QUANTTTY LONG SIGN": 1, "QUANTITY LONG": 10, "QUANTITY SHORT SIGN": 1,
        "QUANTITY SHORT": 10, "EXCH/BROKER FEE / DEC": 12, "EXCH/BROKER FEE D C": 1, "EXCH/BROKER FEE CUR CODE": 3, "CLEARING FEE / DEC": 12,
        "CLEARING FEE D C": 1, "CLEARING FEE CUR CODE": 3, "COMMISSION": 12, "COMMISSION D C": 1, "COMMISSION CUR CODE": 3, "TRANSACTION DATE": 8,
        "FUTURE REFERENCE": 6, "TICKET NUMBER": 6, "EXTERNAL NUMBER": 6, "TRANSACTION PRICE / DEC": 15, "TRADER INITIALS": 6, "OPPOSITE TRADER ID": 7, "OPEN CLOSE CODE": 1}


def daily_summary(input_path, output_path):
    df = import_data(input_path)
    df = process_data(df)
    export_data(df, output_path)


def import_data(input_path):
    odic = OrderedDict(cols)
    df = pd.read_fwf(input_path, widths=odic.values(),
                     header=None, names=odic.keys(), dtype=str)
    return df


def export_data(df, output_path):
    df.to_csv(output_path, index=False, )


def process_data(df):
    # add Client_Information, Product_Information Column and Transaction_Amount
    df = df.assign(Client_Information=lambda x: x['CLIENT TYPE'] + x['CLIENT NUMBER'] + x['ACCOUNT NUMBER'] + x['SUBACCOUNT NUMBER'],
                   Product_Information=lambda x: x['EXCHANGE CODE'] + x['PRODUCT GROUP CODE'] + x['SYMBOL'] + x['EXPIRATION DATE'],
                   Transaction_Amount=lambda x: x['QUANTITY LONG'].astype(int) - x['QUANTITY SHORT'].astype(int),)
    # group by each client and product
    grouped = df.groupby(['Client_Information','Product_Information']) 
    
    # sum up transaction amount
    df = grouped['Transaction_Amount'].sum().reset_index()
    df = df.rename(columns={'Transaction_Amount':'Total_Transaction_Amount'})
    return df
