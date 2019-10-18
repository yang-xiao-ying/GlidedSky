import requests
import secret

def pach():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/70.0.3538.110 '
                      'Safari/537.36',
        'Cookie': secret.cookie,
    }
    #此处ip用的是setting里处理好的ip地址
    ip = [
'47.106.178.169:8118',
]
    k = 959
    for j in range(len(ip)):
        proxies = {'http': ip[j] }
        print(proxies)
        r = requests.get('http://glidedsky.com/level/web/crawler-ip-block-1?page={}'.format(j + k), headers=headers,proxies=proxies,timeout = 3)
        print(r.content)
        contents = r.content.decode('utf-8')
        with open('cached/{}.html'.format(j + k), 'w', encoding='utf-8')as f:
            f.write(contents)
    print(len(ip))
pach()


