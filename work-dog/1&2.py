import requests
import json
import pandas as pd
import plotly.offline as py
import plotly.graph_objs as go
from datetime import datetime

country=input("请输入国家（中文，回车结束）：")
wangzhi = "https://api.inews.qq.com/newsqa/v1/automation/foreign/daily/list?"
res={"country" : country}
res = requests.post(wangzhi,res)
d = json.loads(res.content.decode())
data = pd.DataFrame(d['data'])
print("输入数字以查询：")
print("1：累计的确诊病例")
print("2：每日新增人数")
print("3：累计治愈人数")
print("4：累计死亡人数")
p=int(input())
if p==1:
    data_k=data.confirm
    a1="累计的确诊病例"
elif p==2:
    data_k=data.confirm_add
    a1="每日新增人数"
elif p==3:
    data_k=data.heal
    a1="累计治愈人数"
else:
    data_k=data.dead
    a1="累计死亡人数"

data.date = '2020.'+data.date
print("请输入指定的时间段（输入数字，空格间隔，回车结束）：")
for i in range(len(data.date)):
    print(str(i)+'   .   '+str(data.date[i]))
a,b=map(int,input().split())
data.date = [datetime.strptime(d, '%Y.%m.%d').date() for d in data.date]
xx=list()
for i in range(a,b+1):
    xx.append(data.date[i])
#图表显示
trace_country= go.Bar(x=xx, y=data_k)  #画柱状图
layout=go.Layout(title=country+"的"+a1, xaxis={'title':'日期'}, yaxis={'title':'数量'})
figure=go.Figure(data = [trace_country],layout=layout)
py.plot(figure)#输出图
#峰值
max=data_k.max()#获取所要求的峰值
a=list()#建立一个新的list
for i in range(len(data.date)):
    if data_k[i]==max:
        a.append(data.date[i])#因为可能有多天同时为同一个数值，所以要遍历一次
print("所选数据峰值为"+str(max)+"(单位：人)")
print("出现时间为：")
for i in range(len(a)):
    print(a[i])