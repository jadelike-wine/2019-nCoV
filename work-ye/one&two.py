import requests
import json
import pandas as pd
import plotly.offline as py
import plotly.graph_objs as go
from datetime import datetime

country=input("请输入你想查询的国家（中文即可，回车结束）：")
url_api = "https://api.inews.qq.com/newsqa/v1/automation/foreign/daily/list?"
param={"country" : country}
res = requests.post(url_api,param)
d = json.loads(res.content.decode())
data = pd.DataFrame(d['data'])
print("输入数字以查询：\n1：确诊人数\n2：新增确诊数\n3：治愈人数\n4：死亡人数")
k=int(input())
if k==1:
    data_k=data.confirm
    ppp="确诊人数"
elif k==2:
    data_k=data.confirm_add
    ppp="新增确诊数"
elif k==3:
    data_k=data.heal
    ppp="治愈人数"
else:
    data_k=data.dead
    ppp="死亡人数"
#指定日期

for i in range(len(data.date)):
    data.date[i] = '2020.'+data.date[i]
print("请输入你想展现的起止时间（输入数字，回车结束即可）：")
for i in range(len(data.date)):
    print(str(i)+".  "+str(data.date[i]))
a,b=map(int,input().split())
#day1=data.date[a]
#day2=data.date[b]

data.date = [datetime.strptime(d, '%Y.%m.%d').date() for d in data.date]
x1=list()
for i in range(a,b+1):
    x1.append(data.date[i])
#图表显示
trace_country= go.Bar(x=x1, y=data_k)  #画柱状图
layout=go.Layout(title=country+"的"+ppp+"疫情数据", xaxis={'title':'人数'}, yaxis={'title':'日期'})
figure=go.Figure(data = [trace_country],layout=layout)
py.plot(figure)#输出图
#峰值
max=data_k.max()#获取所要求的峰值
t=list()#建立一个新的list
for i in range(len(data.date)):
    if data_k[i]==max:
        t.append(data.date[i])#因为可能有多天同时为同一个数值，所以要遍历一次
print("所选数据峰值为"+str(max)+"(单位：人)")
print("出现时间为：")#输出
for i in range(len(t)):
    print(t[i])
