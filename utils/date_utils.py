import datetime


def diff_sec(date1,date2):
    '计算两个时间之间的差值'
    return (date2-date1).total_seconds()

def time_gap(arg_time):
    ''
    morning_sec=diff_sec(arg_time[0],arg_time[1])
    afternoon_sec=diff_sec(arg_time[2],arg_time[3])
    return [morning_sec,afternoon_sec]

def is_off(date,flag):
    '市场关门了吗'
    return True

def init_time(now):
    '初始化市场开关门时间'
    return [datetime.datetime(now.year,now.month,now.day,9,30,00),datetime.datetime(now.year,now.month,now.day,11,30,00),datetime.datetime(now.year,now.month,now.day,13,00,00),datetime.datetime(now.year,now.month,now.day,15,00,00)]

def is_weekend():
    '''0#正常交易时间 1#工作日休市 2#周末休市'''
    now = datetime.datetime.now()
    m_time = init_time(now)
    gap = time_gap(m_time)
    #星期几
    int_weekday = datetime.date.today().weekday()
    if (int_weekday == 6 or int_weekday == 5):
        return 2
    elif((diff_sec(m_time[0], now) > 0 and 0 < diff_sec(now, m_time[1]) < gap[0]) or (diff_sec(m_time[2], now) > 0 and 0 < diff_sec(now, m_time[3]) < gap[1])):
        return 0
    else:
        return 1