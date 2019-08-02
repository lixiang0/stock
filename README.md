# 交易助手
设置需关注的股票代码，自动更新股票最新价格
![](data/main.png)

退出在界面按```q```。


#### 用法

0.安装依赖的包

windows:

```
pip install windows-curses
```

ubuntu:
```
sudo apt-get install libncurses5-dev
```

1.在```/data/hold_stock_codes.txt```文件加入股票代码，比如：
```
sh000001
sh000016
```
2.在项目根目录执行：
```python
python main.py
```
即可。

# todo

- 添加持仓盈亏
- 添加5日均线
- 添加板块涨跌
