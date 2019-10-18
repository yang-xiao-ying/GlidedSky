import re
from operator import itemgetter
import requests
from lxml import etree
import secret

def css():
    resu = 0
    for i in range(1, 1001, 1):
        items = []
        url = 'http://glidedsky.com/level/web/crawler-css-puzzle-1?page={}'.format(i)
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                          'AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/70.0.3538.110 '
                          'Safari/537.36',
            'Cookie': secret.cookie,

        }
        response = requests.get(url, headers=headers, timeout=20)
        html = etree.HTML(response.content.decode())
        divs = html.xpath('//div[@class="row"]/div[@class="col-md-1"]')

        print(len(divs))
        for div in divs:
            clas = div.xpath('./div')
            a_items = []
            # 获取每个数字所在位置
            left = 1  # 数字第几位
            for cla in clas:
                class_name = cla.xpath('./@class')
                res = class_name[0] + '.*{( .* )?}'
                div_num = cla.xpath('./text()')  # 获取每一个的值
                class_value = re.findall(res, response.content.decode())
                item = {}
                for value in class_value:
                    vals = value.split(':')

                    item[vals[0].strip()] = vals[1].strip().strip('em')
                valu = False
                if 'opacity' in item:
                    if item['opacity'] == 0:
                        # 隐藏元素
                        pass

                elif 'content' in item:
                    result = item['content']
                    # print(type(result), int(result.strip('"')))
                    items.append(int(result.strip('"')))
                elif 'left' in item:
                    valu = left + int(item['left'])  # 元素移动之后所在位置
                else:
                    valu = left  # 元素保持原来的位置

                if valu:
                    left += 1
                    item_num = {}
                    item_num['num'] = ''.join(div_num)
                    item_num['valu'] = valu
                    a_items.append(item_num)


            if a_items:
                a_items.sort(key=itemgetter('valu'), reverse=False)
                nums = ''
                for item in a_items:
                    num = item['num']
                    nums += num
                items.append(int(nums))
        # 这一页所有的数据列表
        temp = 0
        for j in items:
            temp = temp + j
            # print(temp)
        resu = resu + temp
    print(resu)
css()