from email import header
from urllib import response
import requests, re
from lxml import etree

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

id = 0
for url in url_list:
    id += 1
    print(id, url)
    response = requests.get(url, headers=headers)
    # print(response.text)
    tree = etree.HTML(response.text)
    content = tree.xpath('//div[@class="entry-body-text"]//text()')
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
    if ja and zh:
        ja += '==========\n'
        zh += '==========\n'
        with open(r'D:\aDesktop\pctest\ok.zh', 'a', encoding='utf-8') as fw:
            fw.write(zh)
        with open(r'D:\aDesktop\pctest\ok.ja', 'a', encoding='utf-8') as fw:
            fw.write(ja)