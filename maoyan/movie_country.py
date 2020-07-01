import pandas as pd
from matplotlib import pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']

datas = pd.read_csv('maoyan.csv', encoding='utf-8')


def get_country(s):
    country = s.split('(')
    if len(country) == 1:
        return '中国'
    else:
        temp = country[1].strip(')')
        if temp == '中国香港':
            return '中国'
        elif temp == '法国戛纳':
            return '法国'
        else:
            return temp


datas['country'] = datas['pub_time'].map(get_country)
# print(datas['country'])

country = datas.groupby('country')['country'].count()
# print(country)
# print(list(country))
# print(list(country.index))
explods = [0, 0.2, 0, 0, 0, 0, 0, 0, 0]

plt.pie(list(country), labels=list(country.index), autopct='%1.1f%%', explode=explods)
plt.title('电影的国家分布情况')

# plt.savefig('F:/movie_country.png')

plt.show()
