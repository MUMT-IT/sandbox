from datetime import datetime
import time
import pandas as pd
start_time = time.time() # measure execution time
F = '%H:%M:%S'
D = '%y-%m-%d'

log = pd.read_excel('work_time.xlsx')

def readdate(): #read only same date for case of multi-datetime from excel
    firstrow = str(log['checkin'][0])[:10]
    for i in log.index:
        getdate = str(log['checkin'][i])[:10]
        #print (str(getdate)[:10])
        if getdate == firstrow:
            print ('Same day')
        else:
            print ('Different date time')

def checkdate():
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

def calculate():
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


def test():
    for i in log.index:
        a = log['checkin'][i]
        b = a.strftime(F)
        ti = datetime.strptime(setin, F) - datetime.strptime(b, F)
        print ti


def allinone():
    for i in log.index:
        d_in = log['checkin'][i].strftime(D)
        d_out = log['checkout'][i].strftime(D)
        datein = datetime.strptime(d_in,D)
        dateout = datetime.strptime(d_out,D)
        if datein == dateout :
            print ('ID : %i' % log['id'][i])
            # print ((log['checkin']))
            checkin = log['checkin'][i]  # get checkin data
            s1 = checkin.strftime(F)  # datetime to string type, get onlytime (F declare as global var)
            t_checkin = datetime.strptime(s1, F)  # string to datetime type because can't let datetime minus datetime
            dtype_set_in = datetime.strptime(setin, F)
            if t_checkin >= dtype_set_in:
                return 'Work on time/late'
            else:
                ot = dtype_set_in - t_checkin
                return 'Work early (overtime): {}'.format(ot)

            checkout = log['checkout'][i]  # get checkout data
            s2 = checkout.strftime(F)  # datetime to string type, get only time
            t_checkout = datetime.strptime(s2, F)  # string to datetime type because can't let datetime minus datetime
            dtype_set_out = datetime.strptime(setout, F)

            if t_checkout <= dtype_set_out:
                return 'Get off early/on time'
            else:
                ot = t_checkout - dtype_set_out
                return 'Night work overtime: {}'.format(ot)

        elif dateout > datein:
            print ('ID : %i' % log['id'][i])
            return ('Check out date more than check in date')
        else:
            print ('ID : %i' % log['id'][i])
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
    #calculate()
    #readdate()
    #checkdate()
    #test()
    allinone()
    print("--- %s seconds ---" % (time.time() - start_time))
