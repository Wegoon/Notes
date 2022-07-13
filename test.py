from email import header
from email.encoders import encode_noop
from logging import root
import time
import requests
from lxml import etree

def get_html(s_url, s_headers):
    response = requests.get(url = s_url, headers = s_headers)
    response.encoding = "utf-8"
    html = response.text
    xpa = etree.HTML(html)
    return xpa

def get_book_url(root_url, module_name, module_url, headers):
    module_content = get_html(s_url = module_url, s_headers = headers)
    relative_address = module_content.xpath('//a[@class="book"]/@href')
    for tmp_address in relative_address:
        tmp_address = tmp_address.strip()
        book_url = root_url + tmp_address.split('/')[-1]
        # print(book_url)
        get_chapter_url(root_url, module_name = module_name, book_url = book_url, headers = headers)

def get_chapter_url(root_url, module_name, book_url, headers):
    book_content = get_html(s_url = book_url, s_headers = headers)
    book_name = str(book_content.xpath('//h3[@class="f16"]/text()')[0]).strip()
    book_author = str(book_content.xpath('//div[@class="cont"]/p/text()')[0]).strip()
    book_synopsis = str(book_content.xpath('//div[@class="cont"]/text()')[0]).strip()
    save_data_book(module_name, book_name)
    save_data_book(module_name, book_author)
    save_data_book(module_name, book_synopsis + '\n')
    # print('book_name', type(book_name), book_name)
    # print('book_author', type(book_author), book_author)
    # print('book_synopsis', type(book_synopsis), book_synopsis)
    relative_address = book_content.xpath('//table//tr//a/@href')
    # print('relative_address', relative_address)
    for tmp_address in relative_address:
        tmp_address = tmp_address.strip()
        chapter_url = root_url + tmp_address.split('/')[-1]
        get_chapter_content(module_name = module_name, chapter_url = chapter_url, headers = headers)

def get_chapter_content(module_name, chapter_url, headers):
    chapter_content = get_html(s_url = chapter_url, s_headers = headers)
    en = chapter_content.xpath('//div[@class="line_en"]//text()')
    cn = chapter_content.xpath('//div[@class="line_cn"]/@title')
    for i in range(len(en)):
        en_paragraph = str(en[i]).strip()
        cn_paragraph = str(cn[i]).strip()
        # print(cn_paragraph + '\t' + en_paragraph)
        save_data_cn_en(module_name, cn_paragraph, en_paragraph)
    save_data_book(module_name, "\n\n\n")

# book_name, book_author, book_synopsis
def save_data_book(module_name, book_date):
    print(module_name)
    print('{0}.txt'.format(module_name))
    file = open('{0}.txt'.format(module_name), 'a', encoding='utf-8')
    # with open('{}.txt'.format(module_name), 'a+', encoding='utf-8')as f:
    #     print(book_date)
    file.write(book_date + "\n")
    file.close()
    # print(book_date)

def save_data_cn_en(module_name, cn_paragraph, en_paragraph):
    print('{0}.txt'.format(module_name))
    file = open('{0}.txt'.format(module_name), 'a', encoding='utf-8')
    # with open('{}.txt'.format(module_name), 'a+', encoding='utf-8')as f:
    #     print(cn_paragraph + '\t' + en_paragraph)
    file.write(cn_paragraph + "\t" + en_paragraph + "\n")
    file.close()
    # print(cn_paragraph + '\t' + en_paragraph)

def run():
    root_url = 'http://www.bczzz.com/book/'
    module_name = ['短篇', '中篇', '长篇']
    headers = {
        'Referer': 'http://www.bczzz.com/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
        # 'Cookie': 'Hm_lvt_308b87570281daa02f0d31c085c39163=1638931313; acw_tc=3b2fe1b816389326707231189e9ecf75af42cbef8e41511f142f8fda0b; Hm_lpvt_308b87570281daa02f0d31c085c39163=1638932671'
    }
    for ml in module_name:
        module_url = root_url + ml + '/'
        # print(module_url)
        get_book_url(root_url, module_name = ml, module_url = module_url, headers = headers)

if __name__ == '__main__':
    run()