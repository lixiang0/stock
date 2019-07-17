#http://hq.sinajs.cn/list=sh600538,sz000002,sz000656,sz002133,sz002613,sh601099,sh601872,sh601668,sh603133,sh603603,sz000655
#http://live.sina.com.cn/zt/f/v/finance/globalnews1?tag=10  a股新闻
import time
import datetime
from utils import date_utils,data_utils
import argparse
import numpy as np
import os
from utils.net_utils import HtmlDownloader
import curses

if __name__=='__main__':
    '''
    如果是交易时间则30s更新一次，
    否则30分钟更新一次
    '''
    scr = curses.initscr()
    curses.echo()
    scr.nodelay(True)
    FIRST=True
    while True:
        if scr.getch()==ord('q'):
            break
        if (date_utils.is_off() or date_utils.is_weekend()) and not FIRST:
            curses.napms(3*1000)
            continue
        out='\n'.join([str(value) for value in data_utils.get_stocks(HtmlDownloader())])+'\n'+'-'*100
        if (date_utils.is_off() or date_utils.is_weekend()):
            out+='\n市场闭市......\n停止更新......'
        scr.addstr(0,0,out)
        scr.refresh()
        curses.napms(3000)
        FIRST=False

    curses.endwin()



