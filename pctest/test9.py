import requests
from lxml import etree
import json
import time
import random



path = r'D:\aDesktop\pctest\cn-healthcare_9.zh'

file = open(path, 'w', encoding = 'utf-8')

module_list = [
    '1104',
]



headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
    'Host': 'www.cn-healthcare.com',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
}



def get_one_proxies():
    retry = 0
    while retry < 10:
        try:
            # 白名单
            proxy_api = 'http://service.ipzan.com/core-extract?num=1&no=20211206602823745568&minute=1&format=json&repeat=1&protocol=1&pool=ordinary&mode=whitelist&secret=o4g98deho'
            headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.167 Safari/537.36'}
            response = requests.get(url=proxy_api, headers=headers, timeout=5)
            response.encoding = response.apparent_encoding
            dic = json.loads(response.text)
            # print(type(dic),dic)
            if response.status_code != 200:
                print("get proxies, statu_code != 200 ...")
                continue
            proxies = {}
            # print(type(dic["data"]), dic["data"])
            ip = dic["data"]["list"][0]["ip"]

            port = dic["data"]["list"][0]["port"]
            proxies["HTTPS"] = f'HTTPS://{ip}:{port}'
            proxies["HTTP"] = f'HTTP://{ip}:{port}'
            print("获取一次代理为: " + str(proxies))
            return proxies
        except Exception as e:
            retry += 1
            # print("Error: get_one_proxies retry_num=%s, error=%s" % (retry, e))
            time.sleep(1)
    # print('Exception: get_proxies error, raise exception.')
    return None




url_set = set()

now_time = int(time.time())
last_time = int(time.time())

proxies=get_one_proxies()

for module in module_list:
    # print(module)
    id = 0
    for start in range(10000):
        flag = True
        for wmstart in range(0, 3000, 10):
            url = 'https://www.cn-healthcare.com/freezingapi/api/article/articlelist?data={"start":"' + str(start) + '","size":"10","wmstart":"' + str(wmstart) + '","flag":"2","arctype":"' + module + '"}'
            # file.write(url + '\n')

            retry = 0

            while retry < 5:
                try:
                    # print(url)
                    response = requests.get(url, headers=headers, proxies=proxies)
                    response.encoding = 'utf-8'
                    time.sleep(random.random())
                    print(response.status_code)
                    # print(response.text)
                    re_js = json.loads(response.text)

                    len_num = len(re_js['data']['datalist'])

                    if len_num == 0:
                        flag = False
                        break

                    id += 1

                    print(module, id, url)

                    for num in range(len_num):
                        # print(num)
                        body = re_js['data']['datalist'][num]['body']
                        body_url = 'https://www.cn-healthcare.com' + re_js['data']['datalist'][num]['url']

                        if body_url in url_set:
                            continue

                        url_set.add(body_url)

                        body_html = etree.HTML(body)
                        content_list = body_html.xpath('//body//p')
                        for content in content_list:
                            paragraph = ''.join(content.xpath('.//text()')).strip()
                            # print(paragraph)
                            if paragraph:
                                file.write(paragraph + '\t' + body_url + '\n')
                                # pass
                    break
                except Exception as r:
                    retry += 1
                    print('error :', str(r), '\n', module, id, url)
                    now_time = int(time.time())
                    if now_time < last_time + 10:
                        continue
                    proxies=get_one_proxies()
                    last_time = now_time


                    
                    
            if not flag:
                break

file.close()
