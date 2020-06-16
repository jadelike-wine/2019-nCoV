# coding: utf-8
import requests 
import json
import pandas as pd
from matplotlib import pyplot as plt
from datetime import datetime

url='https://api.inews.qq.com/newsqa/v1/automation/foreign/daily/list'
country=["美国","巴西","俄罗斯","西班牙","英国","意大利","法国","德国","土耳其","印度","伊朗","秘鲁","加拿大","智利","沙特阿拉伯","墨西哥","巴基斯坦","比利时","卡塔尔","荷兰","白俄罗斯","孟加拉","厄瓜多尔","瑞典","新加坡","阿联酋","葡萄牙","瑞士","南非","爱尔兰","哥伦比亚","印度尼西亚","科威特","波兰","乌克兰","埃及","罗马尼亚","以色列","日本本土","奥地利","多米尼加","菲律宾","阿根廷","阿富汗","巴拿马","丹麦","韩国","塞尔维亚","巴林","哈萨克斯坦","捷克","阿尔及利亚","尼日利亚","挪威","阿曼","亚美尼亚","玻利维亚","马来西亚","摩洛哥","摩尔多瓦","加纳","澳大利亚","芬兰","喀麦隆","伊拉克","洪都拉斯","阿塞拜疆","苏丹","危地马拉","卢森堡","匈牙利","塔吉克斯坦","乌兹别克斯坦","几内亚","塞内加尔","泰国","希腊","吉布提","科特迪瓦","刚果（金）","保加利亚","波黑","加蓬","克罗地亚","萨尔瓦多","北马其顿","古巴","爱沙尼亚","冰岛","索马里","立陶宛","吉尔吉斯斯坦","斯洛伐克","新西兰","肯尼亚","斯洛文尼亚","斯里兰卡","马尔代夫","海地","委内瑞拉","几内亚比绍","黎巴嫩","马里","赞比亚","拉脱维亚","突尼斯","阿尔巴尼亚","赤道几内亚","哥斯达黎加","尼日尔","塞浦路斯","尼泊尔","巴拉圭","布基纳法索","乌拉圭","塞拉利昂","安道尔","尼加拉瓜","格鲁吉亚","埃塞俄比亚","约旦","乍得","钻石号邮轮","中非共和国","圣马力诺","马达加斯加","马耳他","刚果（布）","牙买加","坦桑尼亚","巴勒斯坦","多哥","佛得角","卢旺达","毛里求斯","越南","黑山","毛里塔尼亚","乌干达","斯威士兰","利比里亚","也门","莫桑比克","贝宁","缅甸","蒙古","文莱","圭亚那","津巴布韦","柬埔寨","叙利亚","特立尼达和多巴哥","马拉维","巴哈马","利比亚","摩纳哥","巴巴多斯","科摩罗","列支敦士登公国","安哥拉","布隆迪","厄立特里亚","马提尼克岛","博茨瓦纳","不丹","冈比亚","安提瓜和巴布达","东帝汶","格林纳达","纳米比亚","老挝","斐济","伯利兹","圣文森特和格林纳丁斯","圣卢西亚","多米尼克","圣基茨和尼维斯","梵蒂冈","苏里南","塞舌尔","巴布亚新几内亚","莱索托"]
print("请选择所想展示的国家（输入数字即可）：")
for i in range(len(country)):
    print(str(i)+"."+country[i])
n=int(input())
res = requests.post(url, {"country": country[n]})
data=pd.DataFrame(json.loads(res.content.decode())['data'])
xs=pd.DataFrame(json.loads(res.content.decode())['data']).date
for i in range(len(xs)):
    xs[i]="2020/"+xs[i][0]+xs[i][1]+'/'+xs[i][3]+xs[i][4]
xs = [datetime.strptime(d, '%Y/%m/%d').date() for d in xs]
startDate=xs[0]
endDate=xs[len(xs)-1]
index = pd.date_range(startDate, endDate) 
#confirm_add,confirm,heal,dead四选一
ys=data.confirm_add
y=list()
for i in range(0,len(xs)):
    y.append(ys[i])
cols = ['value'] 
df = pd.DataFrame(y, index=index, columns=cols) 
fig, axs = plt.subplots(1,1, figsize=(18,5)) 
index_hourly = pd.date_range(startDate, endDate, freq='1H') 
df_smooth = df.reindex(index=index_hourly).interpolate('cubic') 
df_smooth = df_smooth.rename(columns={'value':'smooth'}) 
df_smooth.plot(ax=axs, alpha=100) 
df.plot(ax=axs, alpha=100)
plt.xlabel('date')#x轴
plt.ylabel('number')#y轴
plt.title("Added trend graph after smoothing the infected person data")#标题
plt.show()