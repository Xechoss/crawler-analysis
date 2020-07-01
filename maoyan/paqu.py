import requests
from lxml import etree
import csv

headers = {  # 设置header
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36'
}


def get_url(url):  # top100电影获取
    res = requests.get(url, headers=headers)  # 请求
    # print(res.text)
    html = etree.HTML(res.text)  # 获取网页源码
    infos = html.xpath('//dl[@class="board-wrapper"]/dd')  # 获取top100的全部电影，xpath
    for info in infos:
        title = info.xpath('div/div/div[1]/p[1]/a/text()')[0]  # 电影名称
        author = info.xpath('div/div/div[1]/p[2]/text()')[0].strip().strip('主演：')  # 电影主演，strip()去掉空格
        pub_time = info.xpath('div/div/div[1]/p[3]/text()')[0].strip('上映时间：')  # 上映时间
        star_1 = info.xpath('div/div/div[2]/p/i[1]/text()')[0]  # 得分1(整数部分)
        star_2 = info.xpath('div/div/div[2]/p/i[2]/text()')[0]  # 得分2（小数部分）
        star = star_1 + star_2  # 电影得分
        movie_url = 'https://maoyan.com' + info.xpath('div/div/div[1]/p[1]/a/@href')[0]  # 电影的详细页
        # print(title,author,pub_time,star,movie_url)
        get_info(movie_url, title, author, pub_time, star)  # 进入电影的详细页爬取


def get_info(url, title, author, pub_time, star):  # 电影详细获取
    res = requests.get(url, headers=headers)
    html = etree.HTML(res.text)
    style = html.xpath('/html/body/div[3]/div/div[2]/div[1]/ul/li[1]/text()')[0]  # 电影类型
    long_time = html.xpath('/html/body/div[3]/div/div[2]/div[1]/ul/li[2]/text()')[0].split('/')[1].strip().strip(
        '分钟')  # 电影时长
    print(title, author, pub_time, star, style, long_time)
    writer.writerow([title, author, pub_time, star, style, long_time])  # 写入数据


if __name__ == '__main__':
    fp = open('F://maoyan.csv', 'w', newline='', encoding='utf-8')  # 存储文件
    writer = csv.writer(fp)
    writer.writerow(['title', 'author', 'pub_time', 'star', 'style', 'long_time'])  # 写入表头
    urls = ['https://maoyan.com/board/4?offset={}'.format(str(i)) for i in range(0, 100, 10)]  # url构造
    for url in urls:
        get_url(url)
