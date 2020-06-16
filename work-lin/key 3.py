import requests
import json
import pandas as pd
import plotly.offline as py
import plotly.graph_objs as go
import matplotlib.pyplot as plt
import scipy as sp
import numpy as np
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号

#以下为获取数据的部分
guojia=input("请输入你想查询的国家（中文即可，回车结束）：")
#guojia="美国"#测试数据
url = "https://api.inews.qq.com/newsqa/v1/automation/foreign/daily/list?"#腾讯API网址
param={"country" : guojia}
res = requests.post(url,param)#爬虫
d = json.loads(res.content.decode())#获取信息
data = pd.DataFrame(d['data']).confirm_add#把每日新增赋值给data变量
riqi=pd.DataFrame(d['data']).date#把日期赋值给riqi变量
for i in range(len(riqi)):
    riqi[i] = '2020-'+riqi[i][0]+riqi[i][1]+'-'+riqi[i][3]+riqi[i][4]
riqi = pd.to_datetime(riqi)#将网页上的时间转换为python指定的时间格式
x=list()
for i in range(len(riqi)):
    x.append(i)
#平滑处理
p = sp.polyfit(x,data, deg=50)#旋转45°免得重叠了
y_ = sp.polyval(p, x)

plt.plot(x,y_, color='r', linewidth=2)
#设置x,y轴代表意思
plt.xlabel("日期")
plt.ylabel("人数")

plt.gcf().autofmt_xdate()
#设置标题
plt.title("所选国家的每日新增感染人数")
one=list()#因为插值法只适合于x轴为int类型的，所以先平滑处理，在更换x轴坐标的名称
two=list()
for i in range(0,len(riqi),20):
    one.append(i)
    two.append(riqi[i])
one.append(len(riqi))
two.append(riqi[len(riqi)-1])
plt.xticks(one,two)#对x轴设置副刻度
plt.show()