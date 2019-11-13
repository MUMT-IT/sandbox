import sys
import math
import numpy as np
from datetime import datetime, timedelta, time
import time
import pandas as pd
F = '%H:%M:%S'

"""Read data from a given excel file.
    excel_file: a filename
    """
def read_data(exel_file):
    df = pd.read_excel(exel_file)
    return df


def splittime(x):
        if pd.isnull(x):
            return np.nan
        times = x.split()
        if len(times) > 1:
            chkin = times[0]
            chkout = times[-1]
            if chkin != chkout:
                return '{},{}'.format(chkin,chkout)
            else:
                return '{},{}'.format(chkin,'')
        elif len(times) == 1:
            return '{},{}'.format(x,'')


def calculate_work_hours(df):
    cleaned_df = df
    cleaned_df[['chkin', 'chkout']] = df.Time.apply(splittime).dropna().str.split(',', expand=True)
    cleaned_df['chkin'] = pd.to_datetime(cleaned_df['chkin'])
    cleaned_df['chkout'] = pd.to_datetime(cleaned_df['chkout'])
    cleaned_df['diff_time'] = cleaned_df['chkout'] - cleaned_df['chkin']
    cleaned_df['diff_mins'] = cleaned_df['diff_time'] / np.timedelta64(1, 'm')
    cleaned_df['diff_hours'] = cleaned_df['diff_time'] / np.timedelta64(1, 'h')
    return cleaned_df


def workhourstatus (setin, setout,work_hours):
    setin = pd.to_datetime(setin)
    setout = pd.to_datetime(setout)
    work_hours['chkin_status'] = work_hours.chkin.apply(lambda x: 'late' if x>setin else 'ontime')
    work_hours['chkout_status'] = work_hours.chkout.apply(lambda x: 'on time' if x > setout else 'Early')
    return work_hours


def write_to_excel(df):
    export_excel =df.to_excel(r'/Users/nut/Desktop/ot_result.xls',header=True)
    return export_excel


def read_schedule(excel_work_file):
    df = pd.read_excel(excel_work_file)
    return df


def calculate_ot (work_hours, ot_schedule):
    work_hours = read_data()
    ot_schedule = read_schedule()
    df1 = DataFrame(work_hours, columns=['ID'])
    df2 = DataFrame(ot_schedule, columns=['ID'])
    df1['ID'] = df2['ID']
    df1.Product.apply(lambda x: df2.AttrName[df2.ProdDetail.str.contains(x)], 1)


def calculate_ot_time(chkin, chkout, shiftstart, shiftend):
    chkin = datetime.strptime(chkin,F)
    shiftstart = datetime.strptime(shiftstart, F)
    chkout = datetime.strptime(chkout, F)
    shiftend = datetime.strptime(shiftend, F)
    if shiftstart >= chkin:
        if chkout >= shiftend: #checkin before and checkout after OT set time
            ot = shiftend - shiftstart
            ot_minute = ot.seconds / 60
            print ot_minute
        else: #checkin before shiftstart but checkout before shiftend
            ot = chkout - shiftstart
            ot_minute = ot.seconds / 60
            print ot_minute
    else: #checkin after shiftstart
        if chkout >= shiftend:  #checkin after shiftstart but checkout after shiftend
            ot = shiftend - chkin
            ot_minute = ot.seconds / 60
            print ot_minute
        else: #checkin after shiftstart and checkout before shiftend
            ot = chkout - chkin
            ot_minute = ot.seconds / 60
            print ot_minute
    #return 180

if __name__ == '__main__':
    #excel_file = read_data('/Users/nut/Desktop/reportworktime.xls')
    #work_hours = calculate_work_hours(excel_file)
    #workhourstatus('09:00:00', '16:00:00',work_hours)
    #excel_file = read_schedule('/Users/nut/Desktop/workschedule.xls')
    calculate_ot_time(chkin='05:30:00', chkout='9:59:00', shiftstart='06:00:00', shiftend='09:00:00')