import os
import requests
from pyquery import PyQuery as pq
import secret


def cached_page(url):
    """
    缓存, 避免重复下载网页浪费时间
    """
    folder = 'cached'
    if not os.path.exists(folder):
        os.makedirs(folder)

    filename = '{}.html'.format(url.split('page=', 1)[1])
    # \\
    # //
    path = os.path.join(folder, filename)

    if os.path.exists(path):
        with open(path, 'rb') as f:
            s = f.read()
            return s
    else:
        r = requests.get(url)
        with open(path, 'wb') as f:
            f.write(r.content)
        return r.content


def movie_from_div(page):

    e = pq(page)
    re = []
    re.append((e('.col-md-1').text()))
    print(re)
    return re

def main():
    res = 0
    for i in range(1, 1001, 1):
        print(i)
        url = 'http://glidedsky.com/level/web/crawler-ip-block-1?page={}'.format(i)
        # 利用缓存好的网页处理数据
        page = cached_page(url)
        movies = movie_from_div(page)
        t = 0
        result = 0
        for i in movies:
            t = i.split()
            # print(type(t),t)
        for j in t:
            result = result + int(j)
        res = res + result
    print('res', res)


if __name__ == '__main__':
    main()
