#http://hq.sinajs.cn/list=sh600538,sz000002,sz000656,sz002133,sz002613,sh601099,sh601872,sh601668,sh603133,sh603603,sz000655
#http://live.sina.com.cn/zt/f/v/finance/globalnews1?tag=10  a股新闻
import time
import datetime
import date_utils
import data_utils
from print_msg import pprint
import sys

def stock_strategy(args):
    if(args==0):
        values=data_utils.get_stocks()
        for value in values:
            #关注上下波动超过5个点的股票
            gap=(float(value.now)-float(value.today))/float(value.today if bool(float(value.today)) else 10000)
            if(gap<-0.05):
                print('gap=',str(gap)[:5],'______',value.name)
            elif(gap>0.05):
                print('gap=',str(gap)[:5],'______',value.name)
            else:
                pass
        time.sleep(30)
    elif(args==1):
        print("交易日休市"), time.sleep(30 * 60)
    else:
        print("周末休市"), time.sleep(60 * 60 * 6)  # 遇到周末 间断的休眠6个小时

def main(args=None):
    print('开始...')
    if(args==None):
        args=sys.argv
    args=args[1]
    if args=='singal':
        print('当前模式为：','test...')
        while True:
            stock_strategy(0)  # 输出策略
    elif args=='cycle':
        while True:
                stock_strategy(date_utils.is_weekend())
    elif args=='volume':
        data_utils.get_volume()
    else:
        print('error')



if __name__=='__main__':
    main()



