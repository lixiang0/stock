import requests
import re
from obj import Volume
from obj import Stock
import os
def read_stocks():
    '从文件中读取关注的股票列表'
    if not os.path.exists('data/hold_stock_codes.txt'):
        raise Exception('请新建data/hold_stock_codes.txt文件，并添加股票代码')
    codes=[code.replace('\n','') for code in open('data/hold_stock_codes.txt','r').readlines()]
    # print(f'read codes:{codes}')
    return codes

def get_volumes(args):
    '获取成交量'
    rex_pattern=re.compile(r'\["[a-z]+[0-9]+","[*]?[A-Z]{0,2}[\u4e00-\u9fa5]{0,}[Ｂ]?[Ａ]?[Ａ]?[A-Z]?[股]?",(-)?[0-9]+.[0-9]+,[0-9]+.[0-9]+\]')
    matchs=rex_pattern.finditer(string=args[args.find('[')+1:args.rfind(']')])
    list_volume=[]
    for match in matchs:
        args=match.group().replace('\"', '').replace('[', '').replace(']', '').split(',')
        list_volume.append(obj_volume(args))
    return list_volume

def get_stocks(loader):
    '获取股票的实时数据'
    # print('http://hq.sinajs.cn/list='+read_stocks())
    list_codes=read_stocks()
    string_codes=','.join(list_codes)[:]
    list_values = loader.download('http://hq.sinajs.cn/list='+string_codes).split('\n')
    value_list=[]
    for i,value in enumerate(list_values):
        if (len(value) < 3):
            continue
        value=(value.split('\"')[1]+','+list_codes[i]).split(",")
        value_list.append(Stock(value))
    return value_list

def get_volume():
    url='http://hq.sinajs.cn/format=text & rn =@ & list = stock_sh_up_d_10, stock_sh_down_d_10, stock_sz_up_d_10, stock_sz_down_d_10, stock_sh_volume_d_10, stock_sh_amount_d_10, stock_sz_volume_d_10, stock_sz_amount_d_10, stock_b_up_d_10, stock_b_down_d_10'.replace(' ','')
    answer_str=requests.get(url).text.split('\n')
    for li in answer_str:
        result=get_volumes(li.replace(' ', '').replace('\n', ''))
        if(li.__contains__('stock_sh_volume_d_10')):
            print('沪市成交量排行前10：')
        elif (li.__contains__('stock_sz_volume_d_10')):
            print('深市成交量排行前10：')
        else:
            continue
        for r in result:
            print(str(r))
if __name__ == '__main__':
    from net_utils import HtmlDownloader
    # loader=HtmlDownloader()
    get_stocks(HtmlDownloader())
# get_volume()
# li=get_volumes('sstock_b_down_d_10=[["sh900906","中毅达B",-1.78,0.442],["sz200017","深中华B",-1.59,3.100],["sh900928","临港B股",-0.91,1.748],["sz200037","深南电B",-0.88,4.490],["sz200530","大冷Ｂ",-0.83,4.780],["sz200581","苏威孚Ｂ",-0.67,17.690],["sz200011","深物业B",-0.64,9.300],["sz200761","本钢板Ｂ",-0.59,3.380],["sh900952","锦港Ｂ股",-0.57,0.524],["sz200539","粤电力Ｂ",-0.56,3.570]]')
# for l in li:
#     print(str(l))

