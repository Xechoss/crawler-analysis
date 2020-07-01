import pandas as pd
from matplotlib import pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']

datas = pd.read_csv('maoyan.csv', encoding='utf-8')

long_time = list(datas['long_time'])
# print(long_time)

d = 10
num_bins = int((max(long_time) - min(long_time)) / d)

plt.hist(long_time, range(min(long_time), max(long_time) + d, d), density=True)

plt.xticks(range(min(long_time), max(long_time) + d, d))
plt.grid(alpha=0.4)

plt.title('电影的时长分布情况')
plt.xlabel('电影时长')
plt.ylabel('比例')

# plt.savefig('F:/movie_long_time.png')

plt.show()
