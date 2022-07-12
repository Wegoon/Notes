import time
import requests
from lxml import etree

def get_html(s_url, s_headers):
    response = requests.get(url = s_url, headers = s_headers)
    # print(response)
    response.encoding = "utf-8"
    html = response.text
    xpa = etree.HTML(html)
    # print(xpa)
    return xpa

def get_bk(url, headers):
    data_bk = []
    xpa = get_html(s_url = url, s_headers = headers)
    pro = xpa.xpath('//div[@class="center"]/ul/li//a[@title!="微米资讯"][@title!="首页"]')
    # print(pro)
    for i in pro:
        url_tmp = url + i.xpath('@href')[0][1:]
        data_bk.append(url_tmp)
    return data_bk

def get_waiurl(url, headers, bk):
    # print(bk)
    # print(url)
    xpa = get_html(s_url=url, s_headers = headers)
    pro = xpa.xpath('//ul[@class="list-box"]//div[@class="t"]/a/@href')
    # print('pro', pro)
    for url in pro:
        url = 'http://wmforum.cn' + url
        # print(url)
        # print(bk)
        parse_data(url=url, headers=headers, bk=bk)
    fanye = xpa.xpath('//a[@id="next_page"]/@href')
    # print('fanye', fanye)
    if fanye:
        next_url = fanye[0]
        next_url = 'http://wmforum.cn' + next_url
        get_waiurl(url=next_url, headers=headers, bk=bk)
        # print('next_url', next_url)

def parse_data(url, headers, bk):
    # print(url)
    xpa = get_html(s_url=url,s_headers = headers)
    title = xpa.xpath('//h1/text()')
    # print(title)
    # print(type(title))
    txt = xpa.xpath('//div[@class="content"]//p/text()')
    # print(txt)
    # title = str(title[0])
    tit = ""
    for line in title:
        tit += str(line.strip()) + "\n"
    article = ""
    for line in txt:
        article += "  " + str(line.strip()) + "\n"
    # print(bk)
    bk = bk.split('/')[-2]
    # print(bk)
    save_data(tit, article, bk)

def save_data(title, txt, bk):
    # pass
    # print(bk)
    print('{0}.txt'.format(bk))
    with open('{}.txt'.format(bk),'a+',encoding='utf-8')as f:
        f.write(title + "\n" + txt + "\n\n\n\n")

def run():
    s_url = 'http://wmforum.cn/'
    headers = {
        'Referer': 'http://wmforum.cn/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
        # 'Cookie': 'Hm_lvt_308b87570281daa02f0d31c085c39163=1638931313; acw_tc=3b2fe1b816389326707231189e9ecf75af42cbef8e41511f142f8fda0b; Hm_lpvt_308b87570281daa02f0d31c085c39163=1638932671'
    }
    a = get_bk(url = s_url, headers = headers)
    for bk in a:
        # print(bk)
        # time.sleep(111111)
        # print(bk)
        get_waiurl(url = bk, headers = headers, bk = bk)
    # url = 'http://wmforum.cn/5g/11-12.html'
    # bk = 'http://wmforum.cn/5g'
    # get_waiurl(url=url, headers=headers, bk = bk)




if __name__ == '__main__':
    run()