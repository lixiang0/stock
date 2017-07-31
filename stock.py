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
        #关注上下波动超过2个点的股票
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

def stock():
    '''还得加上大盘的情况，资金量，流入流出'''
    url = 'http://hq.sinajs.cn/list=sh600538,sz000002,sz000656,sz002133,sz002613,sh601099,sh601872,sh601668,sh603133,sh603603,sz000655,sz002413,sz002413,sh000001,sz399006'
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
def init_time():
    return datetime.datetime(2017,1,1,9,25,00),datetime.datetime(2017,1,1,11,30,00),datetime.datetime(2017,1,1,13,00,00),datetime.datetime(2017,1,1,15,00,00)
stock_strategy(stock())
init_time=init_time()
gap=time_gap(init_time)
while True:
    now=datetime.datetime.now()  
    weekday=datetime.date.today().weekday()
    if(weekday==6 or weekday==5):
        print("周末休市")
        time.sleep(60*60*6)#遇到周末 间断的休眠6个小时
        continue   
    if(diff_sec(init_time[0],now)>0 and 0<diff_sec(now,init_time[1])<gap[0] or diff_sec(init_time[2],now)>0 and 0<diff_sec(now,init_time[3])<gap[1]):
        stock_strategy(stock())
    else:
        print("休市")
        time.sleep(30*60)
        continue
    time.sleep(30)

