import json
# 在网上提取ip地址，以json格式提取出来，做一下处理后，格式化。
# 以下tt里的数据为我提取的一部分，ip地址

result = []
tt = [{"ip":"58.218.200.220","port":2029,"outip":"61.146.190.169"},{"ip":"58.218.201.74","port":2452,"outip":"112.111.185.157"},{"ip":"58.218.201.74","port":9163,"outip":"157.61.249.20"},{"ip":"58.218.201.114","port":8163,"outip":"223.88.12.239"},{"ip":"58.218.201.122","port":8105,"outip":"125.41.201.236"},{"ip":"58.218.200.220","port":2346,"outip":"223.157.8.146"},{"ip":"58.218.200.220","port":4389,"outip":"114.232.217.186"}]
for i in tt:
    ip = '{}:{}'.format(i['ip'], i['port'])
    result.append(ip)
print(result)
