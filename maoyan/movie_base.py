import pandas as pd
from matplotlib import pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']

datas = pd.read_csv('maoyan.csv', encoding='utf-8')
print(datas.head(5))
print(datas.info())
print(datas.describe())
print('电影平均得分：', datas['star'].mean())
print('电影平均时长：', datas['long_time'].mean())
