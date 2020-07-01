import pandas as pd
from matplotlib import pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']

datas = pd.read_csv('maoyan.csv', encoding='utf-8')

titles = list(datas.iloc[:20, 0])
# print(titles)

stars = list(datas.iloc[:20, 3])
# print(stars)

plt.figure(figsize=(20, 10), dpi=80)
_x = range(len(titles))

#  color设置颜色，height设置条线高度,bar绘制
plt.barh(range(len(titles)), stars, height=0.5)

plt.yticks(_x, titles)

plt.grid(alpha=0.3, linestyle='--')

plt.xlabel('得分')
plt.ylabel('电影')
plt.title('前20的电影和电影评分得分数据')

# plt.savefig('F:/movie_star.png')

plt.show()
