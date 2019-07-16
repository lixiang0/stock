#http://hq.sinajs.cn/list=sh600538,sz000002,sz000656,sz002133,sz002613,sh601099,sh601872,sh601668,sh603133,sh603603,sz000655
#http://live.sina.com.cn/zt/f/v/finance/globalnews1?tag=10  a股新闻
import time
import datetime
from utils import date_utils,data_utils
import argparse
import numpy as np
import os
from utils.net_utils import HtmlDownloader
def run(args):
    '''
    args:
        0:run once
        1:run every 30 seconds
    '''
    writer=open('data/prices.txt','a')
    if args.t==0:
        stock_strategy(0,data_utils.get_stocks(HtmlDownloader()),writer)  # 输出策略
    elif args.t==1:
        while True:
            stock_strategy(date_utils.is_weekend(),data_utils.get_stocks(HtmlDownloader()),writer)
    elif args.t==2:
        data_utils.get_volume()
    else:
        print('''type error!!\nplease input:\n
                     0:run once \n\
                     1:run every 30 seconds
                     2:get volume
                     ''')

def stock_strategy(args,values,writer):
    '''

    '''
    if(args==0):#
        print('\n'.join([str(value) for value in values]))
        gettime=str(time.time())
        for value in values:
            #关注上下波动超过5个点的股票
            writer.write('|||'.join([gettime,value.code,value.now])+'\n')
            gap=(float(value.now)-float(value.today))/float(value.today if bool(float(value.today)) else 10000)
            if(np.abs(gap)>0.05):
                print('gap=',str(gap)[:5],'______',value.name)
        print('-'*100)
        time.sleep(30)
    elif(args==1):#
        print("交易日休市"), time.sleep(30 * 60)
    else:
        print("周末休市"), time.sleep(60 * 60 * 6)  # 遇到周末 间断的休眠6个小时

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", help="spider one time or cycle",type=int,default=0)
    args = parser.parse_args()
    print('开始...')
    run(args)

if __name__=='__main__':
    main()



