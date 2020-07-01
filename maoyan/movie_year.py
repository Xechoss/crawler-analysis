import pandas as pd
from matplotlib import pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']

datas = pd.read_csv('maoyan.csv', encoding='utf-8')

datas['year'] = datas['pub_time'].str.split('-').str[0]
datas['month'] = datas['pub_time'].str.split('-').str[1]

year = datas.groupby('year')['year'].count()
month = datas.groupby('month')['month'].count()
# print(list(year.index))
# print(list(year))
# print(month)

plt.figure(figsize=(20, 8), dpi=80)

plt.plot(list(year.index), list(year))
plt.title('电影年份的分布情况')
plt.xlabel('年份')
plt.ylabel('电影数量')
plt.grid(alpha=0.4)

# plt.savefig('F:/movie_year.png')

plt.show()
