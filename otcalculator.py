import sys
import math
import numpy as np
from datetime import datetime, timedelta, time
import time
import pandas as pd
import numpy as np
start_time = time.time() # measure execution time
F = '%H:%M:%S'
D = '%y-%m-%d'

'''
def readdate(): #read only same date for case of multi-datetime from excel
    log = pd.read_excel('work_time.xlsx')
    firstrow = str(log['checkin'][0])[:10]
    for i in log.index:
        getdate = str(log['checkin'][i])[:10]
        #print (str(getdate)[:10])
        if getdate == firstrow:
            print ('Same day')
        else:
            print ('Different date time')
'''


def read_data(exel_file):
    """Read data from a given excel file.

    excel_file: a filename
    """

    log = pd.read_excel(exel_file)
    log.dropna(inplace = True)
    checkin = log['checkin']
    checkout = log['checkout']
    log2 = pd.DataFrame(log)
    log2['Result Date'] = np.where(log2['checkin'].dt.date ==log2['checkout'].dt.date, 'same day', 'different day')
    #print datetime.strptime(log2.checkin.apply(str), '%y-%m-%d %H:%M:%S')
    print timedelta(hours=8, minutes=30)
    #log2['Ealier OT'] = np.where(log2['checkin'].dt.time < log2['checkin'].dt.date.time.replace(hour=8, minute=30).strftime(D) , 'have OT' , 'not have OT')
    print log2
    return checkin, checkout
    #setin = '08:30:00'
    #dtype_setin = datetime.strptime(setin, F)
    #t = checkin.dt.time
    #tt = checkout.dt.time
    #a = datetime.strptime('08:30:00',F).time()

def checkd(checkin,checkout):
    din = checkin.dt.date
    dout = checkout.dt.date
    #d = din.equals(dout)
    #d = dout.isin(din)
    equaldate = din.eq(dout)
    #for i in din:
    return equaldate


def caltime(checkin_date,checkout_date):
    print  equaldate


def checkdate():
    log = pd.read_excel('work_time.xlsx')
    for i in log.index:
        d_in = log['checkin'][i].strftime(D)
        d_out = log['checkout'][i].strftime(D)
        datein = datetime.strptime(d_in,D)
        dateout = datetime.strptime(d_out,D)
        if datein == dateout :
            calculate()
        elif dateout > datein:
            print ('Check out date more than check in date')
        else:
            print ('Check out date less than check in date')

def calculate(setin='08:30:00', setout='16:30:00'):
    log = pd.read_excel('work_time.xlsx')
    for i in log.index:
        print ('ID : %i' %log['id'][i])
        #print ((log['checkin']))
        checkin = log['checkin'][i] #get checkin data
        s1 = checkin.strftime(F) #datetime to string type, get onlytime (F declare as global var)
        t_checkin = datetime.strptime(s1, F) #string to datetime type because can't let datetime minus datetime
        dtype_set_in = datetime.strptime(setin,F)
        if t_checkin >= dtype_set_in :
            print ('Work on time/late')
        else:
            ot = dtype_set_in - t_checkin
            print ('Work early (overtime): %s' %ot)
        checkout = log['checkout'][i]  # get checkout data
        s2 = checkout.strftime(F)  # datetime to string type, get only time
        t_checkout = datetime.strptime(s2, F)  # string to datetime type because can't let datetime minus datetime
        dtype_set_out = datetime.strptime(setout, F)
        if t_checkout <= dtype_set_out:
            print ('Get off early/on time')
        else:
            ot = t_checkout - dtype_set_out
            print ('Night work overtime: %s' %ot)

def allinone(checkin,checkout,setin='08:30:00', setout='16:30:00'):
    d_in = checkin.strftime(D)
    d_out = checkout.strftime(D)
    datein = datetime.strptime(d_in,D)
    dateout = datetime.strptime(d_out,D)
    if datein == dateout:
        # print ((log['checkin']))
        s1 = checkin.strftime(F)  # datetime to string type, get onlytime (F declare as global var)
        t_checkin = datetime.strptime(s1, F)  # string to datetime type because can't let datetime minus datetime
        dtype_set_in = datetime.strptime(setin, F)
        if t_checkin >= dtype_set_in:
            return 'Work on time/late'
        else:
            ot = dtype_set_in - t_checkin
            return 'Work early (overtime): {}'.format(ot)
        s2 = checkout.strftime(F)  # datetime to string type, get only time
        t_checkout = datetime.strptime(s2, F)  # string to datetime type because can't let datetime minus datetime
        dtype_set_out = datetime.strptime(setout, F)
        if t_checkout <= dtype_set_out:
            return 'Get off early/on time'
        else:
            ot = t_checkout - dtype_set_out
            return 'Night work overtime: {}'.format(ot)
    elif dateout > datein:
        return ('Check out date more than check in date')
    else:
        return ('Check out date less than check in date')


def caldate(checkin, checkout, setin='08:30:00', setout='16:30:00'):
    if not checkout:
        raise ValueError

    if checkin.date() == checkout.date():
        s1 = checkin.strftime(F)  # datetime to string type, get onlytime (F declare as global var)
        t_checkin = datetime.strptime(s1, F)  # string to datetime type because can't let datetime minus datetime
        dtype_set_in = datetime.strptime(setin, F)
        if t_checkin >= dtype_set_in:
            return 'Work on time/late'
        else:
            ot = dtype_set_in - t_checkin
            return 'Work early'
    # return value if late show - value
        checkout = log['checkout'][i]  # get checkout data
        s2 = checkout.strftime(F)  # datetime to string type, get only time
        t_checkout = datetime.strptime(s2, F)  # string to datetime type because can't let datetime minus datetime
        dtype_set_out = datetime.strptime(setout, F)

        if t_checkout <= dtype_set_out:
            return 'Get off early/on time'
        else:
            ot = t_checkout - dtype_set_out
            return 'Night work overtime: {}'.format(ot)

    elif checkin.date() < checkout.date():
        return ('Check out date more than check in date')
    else:
        return ('Check out date less than check in date')


def calculate_work_hours(checkin_times, checkout_times):
    return calculate_ot_hours(checkin_times, checkout_times)


def create_datetime(row, hour, minute, second=0):
    return datetime(row.year, row.month, row.day,
                    hour, minute, second)


def round_hours(deltahour):
    if deltahour >= 0:
        return math.floor(deltahour)
    else:
        return math.floor(abs(deltahour)) * -1


def calculate_ot_hours(scantimes,
                       check_hour,
                       check_minute,
                       check_second=0):
    """Calculate OT hours for same date.

    scantimes: Series of check-in times
    check_hour: hour
    check_minute: minute
    check_second: second
    return: Data frame of OT hours
    """
    checktimes = scantimes.apply(create_datetime, args=[
        check_hour, check_minute, check_second
    ])
    ot_time = scantimes - checktimes
    ot_hours = ot_time/pd.Timedelta(hours=1)
    return ot_hours.apply(round_hours)



if __name__ == '__main__':
    #caldate()
    #readdata()
    excel_file = sys.args[1]
    checkin,checkout = read_data(excel_file)
    checkd(checkin,checkout)
    #equaldate = checkd(checkin,checkout)
    #caltime(checkin,checkout,equaldate)
    #allinone(checkin,checkout)
    print("--- %s seconds ---" % (time.time() - start_time))
