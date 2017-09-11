import requests
import user_obj
from print_msg import pprint


def read_stocks():
    '从文件中读取关注的股票列表'
    file=open('codelist.txt','r')
    l=file.readlines()[1:]
    for i,li in enumerate(l):
        l[i]=li.replace('\n', '')
    return ','.join(l)[:]

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
        print(obj)
        obj_list.append(obj)
    return obj_list
