#http://hq.sinajs.cn/list=sh600538,sz000002,sz000656,sz002133,sz002613,sh601099,sh601872,sh601668,sh603133,sh603603,sz000655

import time
import requests
import string
import datetime
class obj_stock:
    def __init__(self,args):
        self.name=args[0]
        self.today=args[1]
        self.yesterday=args[2]
        self.now=args[3]
        self.top=args[4]
        self.low=args[5]
    def __str__(self):
        return ' '.join([self.name,"今开：",self.today,"昨收：",self.yesterday,"现价：",self.now,"最高：",self.top,"最低：",self.low])

def stock_strategy(args):
    for sto in args:
        #关注上下波动超过5个点的股票
#        print(sto)
#        print(float(sto.now)-float(sto.today))
#        print(sto.today if bool(float(sto.today)) else 10000)
        gap=(float(sto.now)-float(sto.today))/float(sto.today if bool(float(sto.today)) else 10000)
        if(gap<-0.05):
            print('gap=',str(gap)[:5],'______',sto.name)
        elif(gap>0.05):
            print('gap=',str(gap)[:5],'______',sto.name)
        else:
            pass

def diff_sec(date1,date2):
    return (date2-date1).total_seconds()

def time_gap(arg_time):
    morning_sec=diff_sec(arg_time[0],arg_time[1])
    afternoon_sec=diff_sec(arg_time[2],arg_time[3])
    return [morning_sec,afternoon_sec]

def is_off(date,flag):
    return True
def get_stocks():
    file=open('config','r')
    list=file.readlines()
    return ','.join(list)[1:]
def stock():
    '''还得加上大盘的情况，资金量，流入流出'''
    url = 'http://hq.sinajs.cn/list='+get_stocks()
    r = requests.get(url)
    str = r.text.split("\n")[0]
    obj_list=[]
    for str in r.text.split("\n"):
        if (len(str) < 3):
            continue
        s = ""
        flag = False
        for c in range(len(str)):
            if (str[c - 1].__eq__("\"") & c > 0):
                flag = True
            if (flag):
                s += str[c];
        stocks = s.split(",")
        obj=obj_stock(stocks)
        print(obj)
        obj_list.append(obj)
    return obj_list
def init_time(now):
    return [datetime.datetime(now.year,now.month,now.day,9,30,00),datetime.datetime(now.year,now.month,now.day,11,30,00),datetime.datetime(now.year,now.month,now.day,13,00,00),datetime.datetime(now.year,now.month,now.day,15,00,00)]
# stock_strategy(stock())
while True:
    now=datetime.datetime.now()
    weekday=datetime.date.today().weekday()
    gap = time_gap(init_time(now))
    if(weekday==6 or weekday==5):
        print("周末休市")
        time.sleep(60*60*6)#遇到周末 间断的休眠6个小时
        continue
    m_time=init_time(now)
    print(diff_sec(m_time[0],now),diff_sec(now,m_time[1]),diff_sec(m_time[2],now),diff_sec(now,m_time[3]))
    if((diff_sec(m_time[0],now)>0 and 0<diff_sec(now,m_time[1])<gap[0]) or (diff_sec(m_time[2],now)>0 and 0<diff_sec(now,m_time[3])<gap[1])):
        stock_strategy(stock())
    else:
        print("休市")
        time.sleep(30*60)
        continue
    time.sleep(30)
                             #今开  昨收   现价   最高  最低               成交量   成交额        买1    价格  买2   价格   买3   价格   买4    价格  买5    价格  卖1         卖2          卖3          卖4         卖5         时间
#var hq_str_sh600538="国发股份,5.940,5.950,6.010,6.020,5.930,6.000,6.010,5211267,31156630.000,11200,6.000,84833,5.990,54000,5.980,41900,5.970,77500,5.960,5000,6.010,134100,6.020,77300,6.030,38900,6.040,84800,6.050,2017-08-25,15:00:00,00";

