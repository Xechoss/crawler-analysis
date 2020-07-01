import pandas as pd
from matplotlib import pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']

datas = pd.read_csv('maoyan.csv', encoding='utf-8')

datas['month'] = datas['pub_time'].str.split('-').str[1]

# year = datas.groupby('year')['year'].count()
month = datas.groupby('month')['month'].count()
# print(list(month.index))
# print(list(month))

# plt.figure(figsize=(20, 8), dpi=80)

x_ticks = ['{}月'.format(i) for i in range(1, 13)]

plt.bar(list(month.index), list(month), color='orange')

plt.title('电影月份的分布情况')
plt.xlabel('月份')
plt.ylabel('电影数量')
plt.xticks(range(0, 12), x_ticks)

# plt.savefig('F:/movie_month.png')

plt.show()
