import requests
import json
import pandas as pd
import plotly.offline as py
import plotly.graph_objs as go

#以下为获取数据的部分
guojia=input("请输入你想查询的国家（中文即可，回车结束）：")
url = "https://api.inews.qq.com/newsqa/v1/automation/foreign/daily/list?"#腾讯API网址
param={"country" : guojia}
res = requests.post(url,param)#爬虫
d = json.loads(res.content.decode())#获取信息
data = pd.DataFrame(d['data'])#把data值赋值给data变量
#以下为选择查询哪些数据部分
print("输入数字以查询：")
print("1：确诊人数")
print("2：新增确诊数")
print("3：治愈人数")
print("4：死亡人数")
k=int(input())#和输入的数字一一对应关系
if k==1:
    data_k=data.confirm
elif k==2:
    data_k=data.confirm_add
elif k==3:
    data_k=data.heal
else:
    data_k=data.dead
#指定日期

for i in range(len(data.date)):
    data.date[i] = '2020-'+data.date[i][0]+data.date[i][1]+'-'+data.date[i][3]+data.date[i][4]
data.date = pd.to_datetime(data.date)#将网页上的时间转换为python指定的时间格式

print("请输入你想展现的起止时间（输入数字，回车结束即可）：")
for i in range(len(data.date)):
    print(str(i)+" ."+str(data.date[i]))
a=int(input())
day=data.date[a]
data.date = data.date[(data.date >= pd.to_datetime(day,format = '%Y-%m-%d'))]#把用户指定的时间段进行赋值

#图表显示
trace_country= go.Bar(x=data.date, y=data_k)  #画柱状图
layout=go.Layout(title="疫情数据", xaxis={'title':'人数'}, yaxis={'title':'日期'})#标题，x轴和y轴分表表示的意思
figure=go.Figure(data = [trace_country],layout=layout)#分别带入x和y轴的值
py.plot(figure)#输出图
#峰值
max=data_k.max()#获取所要求的峰值
time=list()#建立一个新的list
for i in range(len(data.date)):
    if data_k[i]==max:
        time.append(data.date[i])#因为可能有多天同时为同一个数值，所以要遍历一次
print("所选数据峰值为"+str(max)+"(单位：人)")
print("出现时间为：")#输出
for i in range(len(time)):
    print(time[i])
