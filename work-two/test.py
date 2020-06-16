import requests 
import json
import pandas as pd
from datetime import datetime
import plotly.graph_objects as go

query_url='https://api.inews.qq.com/newsqa/v1/automation/foreign/daily/list'
param = {"country": "意大利"}#可以更换国家
res = requests.post(query_url, param)
d=json.loads(res.content.decode())
data_italy=pd.DataFrame(d['data'])
param = { "country" :"美国"}
res = requests.post(query_url, param)
d=json.loads(res.content.decode())
data_usa=pd.DataFrame(d['data'])

data_usa.date='2020.'+data_usa.date
data_usa.date=pd.to_datetime(data_usa.date)
data_italy.date='2020.'+data_italy.date
data_italy.date=pd.to_datetime(data_italy.date)

data_usa.confirm_add = data_usa.confirm_add/330
data_italy.confirm_add = data_italy.confirm_add/60


usa_max_day = data_usa.date.iloc [data_usa.confirm_add.idxmax()]
italy_max_day = data_italy.date.iloc [data_italy.confirm_add.idxmax()]
days = usa_max_day-italy_max_day
data_usa_new = data_usa.copy()
data_usa_new.date = data_usa.date-days


trace=go.Scatter(x=data_usa_new.date,y=data_usa_new.confirm_add,name='usa')
trace_italy=go.Scatter(x=data_italy.date,y=data_italy.confirm_add,name='italy')

mylay=go.Layout(title='图片标题')

fig = go.Figure(data=[trace,trace_italy],layout=mylay)
fig.show()
