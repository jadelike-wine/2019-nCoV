import requests
import json
import pandas as pd
import plotly.offline as py
import plotly.graph_objs as go
import matplotlib.pyplot as plt
import scipy as sp
import numpy as np
from datetime import datetime


plt.rcParams['font.sans-serif']=['SimHei'] 
plt.rcParams['axes.unicode_minus']=False

country=input("请输入你想查询的国家（中文即可，回车结束）：")
url_api = "https://api.inews.qq.com/newsqa/v1/automation/foreign/daily/list?"
param={"country" : country}
res = requests.post(url_api,param)
d = json.loads(res.content.decode())
data = pd.DataFrame(d['data'])
for i in range(len(data.date)):
    data.date[i] = '2020.'+data.date[i]
data.date = [datetime.strptime(d, '%Y.%m.%d').date() for d in data.date]
x=[]
for i in range(len(data.date)):
    x.append(i)



#平滑处理
p = sp.polyfit(x,data.confirm_add, deg=45)#旋转45°
y2 = sp.polyval(p, x)
plt.plot(x,y2, color='r', linewidth=2)
#设置x,y轴代表意思
plt.xlabel("日期")
plt.ylabel("人数")
plt.gcf().autofmt_xdate()
#设置标题
plt.title("所选国家的每日新增感染人数")
x2=list()#因为插值法只适合于x轴为int类型的，所以先平滑处理，在更换x轴坐标的名称
y2=list()
for i in range(0,len(data.date),10):
    x2.append(i)
    y2.append(data.date[i])
x2.append(len(data.date))
y2.append(data.date[len(data.date)-1])
plt.xticks(x2,y2)#对x轴设置副刻度
plt.show()