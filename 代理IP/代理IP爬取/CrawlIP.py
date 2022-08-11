import time
import requests
import lxml

url_module_list = [
    'https://free.kuaidaili.com/free/inha/',
    'https://free.kuaidaili.com/free/intr/',
]

headers = {
    # 'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
    'User-Agent' : 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Mobile Safari/537.36',
    'Host' : 'https://free.kuaidaili.com/',
    'Upgrade-Insecure-Requests' : '1',
    'Connection' : 'keep-alive',
}

def get_content(url):
    headers['Host'] = url
    time.sleep(5)
    response = requests.get(url, headers = headers)
    print(response.status_code)
    pass

for url_module in url_module_list:
    for id in range(1, 4719):
        # print(id)
        url = url_module + str(id) + '/'
        # print(url)
        get_content(url)