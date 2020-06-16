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

country="美国"#input("请输入你想查询的国家（中文即可，回车结束）：")
url_api = "https://api.inews.qq.com/newsqa/v1/automation/foreign/daily/list?"
param={"country" : country}
res = requests.post(url_api,param)
d = json.loads(res.content.decode())
data = pd.DataFrame(d['data'])


# 数据（画折线至少需要两个点）
xs = [0, 0]
ys = [1, 1]

for i in range(len(data.date)-1):
    # 不断更新这个两个点
    y = np.random.random()
    xs[0] = data.date[i]
    ys[0] = data.confirm_add[i]
    xs[1] = data.date[i+1]
    ys[1] = data.confirm_add[i+1]
    plt.plot(xs, ys, "b")
    #plt.xlim(xs[1], xs[1])
    #plt.xlim()
    plt.pause(0.1)

# 显示（暂停）
plt.show()