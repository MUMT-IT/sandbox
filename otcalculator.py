from datetime import datetime, timedelta
import time
import pandas as pd
import numpy as np
start_time = time.time() # measure execution time
F = '%H:%M:%S'
D = '%y-%m-%d'

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

def readdata():
    log = pd.read_excel('work_time.xlsx')
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
    #return equaldate

def caltime(checkin,checkout,equaldate):
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


if __name__ == '__main__':
    #caldate()
    #readdata()
    checkin,checkout = readdata()
    checkd(checkin,checkout)
    #equaldate = checkd(checkin,checkout)
    #caltime(checkin,checkout,equaldate)
    #allinone(checkin,checkout)
    print("--- %s seconds ---" % (time.time() - start_time))
