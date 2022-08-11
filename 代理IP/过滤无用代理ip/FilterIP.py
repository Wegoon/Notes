from email import header
import requests


url_list = []


ip_set = set()


path = r'D:\aDesktop\Code\Repositories\Notes\代理IP\过滤无用代理ip\\'

file_r = open(path + 'config', 'r', encoding = 'utf-8')

flag = 0
for line in file_r.readlines():
    line = line.strip()
    if line == '#ip':
        flag = 1
        continue
    if line == '#url':
        flag = 2
        continue
    if not flag or not line:
        continue
    if flag == 1:
        tmp = line.split()
        address, port = tmp[0], tmp[1]
        address_port = str(address) + ':' + str(port)
        ip_set.add(address_port)
    else:
        url_list.append(line)
file_r.close()


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
    'Host': 'www.baidu.com',
}

for ip in ip_set:
    proxies = {
        'HTTP' : 'HTTP://' + ip,
        'HTTPS' : 'HTTPS://' + ip
    }
    # print(proxies)
    num = 0
    for url in url_list:
        headers['Host'] = url
        status = requests.get(url, headers = headers, proxies = proxies).status_code
        print(url, proxies)
        if status == '200':
            num += 1
            print('ok', status)
        else:
            print('no', status)
    file_w = open(path + str(num) + '.out', 'a', encoding = 'utf-8')
    file_w.write(ip + '\n')