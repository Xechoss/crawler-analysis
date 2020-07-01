import pandas as pd
from matplotlib import pyplot as plt
from collections import Counter

plt.rcParams['font.sans-serif'] = ['SimHei']

datas = pd.read_csv('maoyan.csv', encoding='utf-8')

s = ''
for i in range(99):
    s += datas.iloc[i, 1]+','
s += datas.iloc[99, 1]
# print(s)
authors = s.split(',')
# print(authors)
c = Counter(authors)
# print(c)
items = c.most_common(6)
print(items)

author = []
count = []
for item in items:
    author.append(item[0])
    count.append(item[1])

# print(author)
# print(count)
plt.bar(author, count, color='orange')
plt.title('出演次数最多的六位演员情况')
plt.xlabel('演员')
plt.ylabel('出演次数')

# plt.savefig('F:/movie_author.png')

plt.show()
