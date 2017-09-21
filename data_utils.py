import requests
import user_obj
from print_msg import pprint
import re
from user_obj import obj_volume
def read_stocks():
    '从文件中读取关注的股票列表'
    file=open('codelist.txt','r')
    l=file.readlines()[1:]
    for i,li in enumerate(l):
        l[i]=li.replace('\n', '')
    return ','.join(l)[:]
def get_volumes(args):
    rex_pattern=re.compile(r'\["[a-z]+[0-9]+","[*]?[A-Z]{0,2}[\u4e00-\u9fa5]{0,}[Ｂ]?[Ａ]?[Ａ]?[A-Z]?[股]?",(-)?[0-9]+.[0-9]+,[0-9]+.[0-9]+\]')
    # print(args[args.find('[')+1:args.rfind(']')])
    matchs=rex_pattern.finditer(string=args[args.find('[')+1:args.rfind(']')])
    list_volume=[]
    for match in matchs:
        args=match.group().replace('\"', '').replace('[', '').replace(']', '').split(',')
        list_volume.append(obj_volume(args))
    return list_volume
def get_stocks():
    '获取股票的实时数据'
    list_values = requests.get('http://hq.sinajs.cn/list='+read_stocks()).text.split('\n')
    obj_list=[]
    list_values=list_values[1:-4]#暂时不关注指数
    pprint(list_values)
    for s in list_values:
        if (len(s) < 3):
            continue
        obj=user_obj.obj_stock(s.split('\"')[1].split(","))
        obj_list.append(obj)
    return obj_list
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

# get_volume()
# li=get_volumes('sstock_b_down_d_10=[["sh900906","中毅达B",-1.78,0.442],["sz200017","深中华B",-1.59,3.100],["sh900928","临港B股",-0.91,1.748],["sz200037","深南电B",-0.88,4.490],["sz200530","大冷Ｂ",-0.83,4.780],["sz200581","苏威孚Ｂ",-0.67,17.690],["sz200011","深物业B",-0.64,9.300],["sz200761","本钢板Ｂ",-0.59,3.380],["sh900952","锦港Ｂ股",-0.57,0.524],["sz200539","粤电力Ｂ",-0.56,3.570]]')
# for l in li:
#     print(str(l))

