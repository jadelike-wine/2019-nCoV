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

country=input("请输入国家（中文，回车结束）：")
wangzhi = "https://api.inews.qq.com/newsqa/v1/automation/foreign/daily/list?"
res={"country" : country}
res = requests.post(wangzhi,res)
d = json.loads(res.content.decode())
data = pd.DataFrame(d['data'])
data.date = '2020.'+data.date
data.date = [datetime.strptime(d, '%Y.%m.%d').date() for d in data.date]
x=[]
for i in range(len(data.date)):
    x.append(i)
p = np.polyfit(x,data.confirm_add, deg=50)
yy = np.polyval(p, x)
plt.plot(x,yy, color='r', linewidth=2)
plt.xlabel("日期")
plt.ylabel("人数")
plt.gcf().autofmt_xdate()
plt.title("所选国家的每日新增感染人数")
xx=list()#因为插值法只适合于x轴为int类型的，所以先平滑处理，在更换x轴坐标的名称
yy=list()
for i in range(0,len(data.date),5):
    xx.append(i)
    yy.append(data.date[i])
xx.append(len(data.date))
yy.append(data.date[len(data.date)-1])
plt.xticks(xx,yy)#对x轴设置副刻度
plt.show()