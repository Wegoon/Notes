import requests
from lxml import etree

def get_html(s_url, s_headers):
    response = requests.get(url = s_url, headers = s_headers)
    response.encoding = "utf-8"
    html = response.text
    xpa = etree.HTML(html)
    return xpa

def save_date(module_name, date):
    print('{}.txt'.format(module_name))
    file = open('{}.txt'.format(module_name), 'a', encoding = 'utf-8')
    file.write(date)
    file.close()

def get_article_content(module_name, article_url, headers):
    article_content = get_html(s_url = article_url, s_headers = headers)
    article_title = article_content.xpath('//div[@class="arc-header"]/h1/text()')
    if article_title:
        article_title = str(article_title[0])
    article_main_body = article_content.xpath('//div[@class="content"]//p')
    date = ''
    if article_title:
        date += article_title + '\n'
    for tmp_paragraph in article_main_body:
        paragraph = ''.join(tmp_paragraph.xpath('.//text()')).strip()
        if paragraph:
            date += paragraph + '\n'
    save_date(module_name, date + '\n\n\n')


def get_article_url(home_page_url, module_name, now_page_url, headers):
    while True:
        print('\n' + now_page_url)
        now_page_content = get_html(s_url = now_page_url, s_headers = headers)

        tmp_article_url = now_page_content.xpath('//ul[@class="list-box"]//div[@class="t"]/a/@href')
        for article_url in tmp_article_url:
            article_url = home_page_url[: -1] + article_url
            get_article_content(module_name = module_name, article_url = article_url, headers = headers)

        relative_address = now_page_content.xpath('//a[@id="next_page"]/@href')
        if not relative_address:
            break
        now_page_url = home_page_url[: -1] + relative_address[0]

def get_module(home_page_url, headers):
    home_page_content = get_html(s_url = home_page_url, s_headers = headers)
    tmp_module_name = home_page_content.xpath('//div[@class="center"]/ul/li//a[@title!="微米资讯"][@title!="首页"]/@href')
    module_name = []
    module_url = []
    for tmp_name in tmp_module_name:
        module_name.append(str(tmp_name[1 : -1]))
        module_url.append(home_page_url + tmp_name[1 : ])
    
    for i in range(len(module_name)):
        now_page_url = module_url[i]
        get_article_url(home_page_url = home_page_url, module_name = module_name[i], now_page_url = now_page_url, headers = headers)


def run():
    home_page_url = 'http://wmforum.cn/'
    headers = {
        'Referer': home_page_url,
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
    }

    get_module(home_page_url = home_page_url, headers = headers)

if __name__ == '__main__':
    run()