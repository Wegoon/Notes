from email import header
from urllib import response
import requests, re, threading
from lxml import etree
import concurrent.futures

url = 'http://henmi42.cocolog-nifty.com/yijianyeye/archives.html'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
}

response = requests.get(url, headers=headers)
# print(response.text)
tree = etree.HTML(response.text)
# print(tree)
url_list = tree.xpath('//p//a/@href')

# for url in url_list:
#     print(url)
# print(len(url_list))





def mainprocess(url):
    response = requests.get(url, headers=headers)
    # print(response.text)
    tree = etree.HTML(response.text)
    tmp_content = tree.xpath('//div[@class="entry-body-text"]//div')
    # print(tmp_content)
    content = list()
    for tmp in tmp_content:
        this = tmp.xpath('.//text()')
        # print(this)
        yuan = ''
        for line in this:
            line = line.strip()
            yuan += line
        content.append(yuan)

    zh = ''
    ja = ''
    for line in content:
        line = line.strip()
        if not line or (not re.search('[\u3040-\u309F\u30A0-\u30FF]', line) and not re.search(r'[\u4e00-\u9fa5]', line)):
            continue
        if re.search('[\u3040-\u309F\u30A0-\u30FF]', line):
            ja += line + '\n'
        elif re.search('[\u4e00-\u9fa5]', line):
            zh += line + '\n'
    print(zh, ja)
    if ja and zh:
        ja += '==========\n'
        zh += '==========\n'
        lock = threading.Lock()
        with lock:
            with open(r'C:\Users\my\Desktop\my\depository\Notes\pctest\pctest\no.zh', 'a', encoding='utf-8') as fw:
                fw.write(zh)
            with open(r'C:\Users\my\Desktop\my\depository\Notes\pctest\pctest\no.ja', 'a', encoding='utf-8') as fw:
                fw.write(ja)

with concurrent.futures.ThreadPoolExecutor() as pool:
    # print('ok')
    future_list = [pool.submit(mainprocess, url) for url in url_list]
    # print(len(self.future_list))
    id = 0
    for future in concurrent.futures.as_completed(future_list):
        id += 1
        print('完成', id, '个任务')