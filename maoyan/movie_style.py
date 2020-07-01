import pandas as pd
from matplotlib import pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']

datas = pd.read_csv('maoyan.csv', encoding='utf-8')

s = ''
for i in range(99):
    s += datas.iloc[i, 4]+','
s += datas.iloc[99, 4]
# print(s)

styles = s.split(',')
style = list(set(styles))
print(style)
count = []
for item in style:
    count.append(styles.count(item))
# print(count)

plt.figure(figsize=(20, 8), dpi=80)

plt.bar(style, count)
plt.title('电影的类型分布情况')
plt.ylabel('电影数量')
plt.xlabel('类型')

# plt.savefig('F:/movie_style.png')

plt.show()
