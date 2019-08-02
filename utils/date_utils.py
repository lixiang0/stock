import datetime


def diff_sec(date1,date2):
    '计算两个时间之间的差值'
    return (date2-date1).total_seconds()

def time_gap(arg_time):
    '计算与开/闭市的时间差'
    morning_sec=diff_sec(arg_time[0],arg_time[1])
    afternoon_sec=diff_sec(arg_time[2],arg_time[3])
    return morning_sec,afternoon_sec

def is_off():
    '市场关门了吗'
    now = datetime.datetime.now()
    m_start,m_end,a_start,a_end = init_time(now)
    return (diff_sec(now,m_start)>0 and diff_sec(now,m_end)<0) or (diff_sec(now,a_start)>0 and diff_sec(now,a_end)<0)#开市了吗？

def init_time(now):
    '初始化市场开关门时间'
    return datetime.datetime(now.year,now.month,now.day,9,30,00),datetime.datetime(now.year,now.month,now.day,11,30,00),datetime.datetime(now.year,now.month,now.day,13,00,00),datetime.datetime(now.year,now.month,now.day,15,00,00)

def is_weekend():
    '''是否周末'''
    #星期几
    int_weekday = datetime.date.today().weekday()
    if (int_weekday == 6 or int_weekday == 5):
        return True
    return False

if __name__=='__main__':
    print(is_off())