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
        get_chapter_url(root_url, module_name = module_name, book_url = book_url, headers = headers)

def get_chapter_url(root_url, module_name, book_url, headers):
    book_content = get_html(s_url = book_url, s_headers = headers)
    book_name = str(book_content.xpath('//h3[@class="f16"]/text()')[0]).strip()
    book_author = str(book_content.xpath('//div[@class="cont"]/p/text()')[0]).strip()
    book_synopsis = str(book_content.xpath('//div[@class="cont"]/text()')[0]).strip()
    save_data_book(module_name, book_name)
    save_data_book(module_name, book_author)
    save_data_book(module_name, book_synopsis + '\n')
    relative_address = book_content.xpath('//table//tr//a/@href')
    tmp_chapter_name = book_content.xpath('//table//tr//a/text()')

    for i in range(len(relative_address)):
        tmp_address = relative_address[i].strip()
        chapter_url = root_url + tmp_address.split('/')[-1]
        chapter_name = str(tmp_chapter_name[i]).strip()
        get_chapter_content(module_name = module_name, chapter_url = chapter_url, chapter_name = chapter_name, headers = headers)
    save_data_book(module_name, "\n")

def get_chapter_content(module_name, chapter_url, chapter_name, headers):
    chapter_content = get_html(s_url = chapter_url, s_headers = headers)
    save_data_book(module_name, chapter_name)
    en = chapter_content.xpath('//div[@class="line_en"]//text()')
    cn = chapter_content.xpath('//div[@class="line_cn"]/@title')
    for i in range(len(en)):
        en_paragraph = str(en[i]).strip()
        cn_paragraph = str(cn[i]).strip()
        save_data_cn_en(module_name, cn_paragraph, en_paragraph)
    save_data_book(module_name, "")

# book_name, book_author, book_synopsis
def save_data_book(module_name, book_date):
    file = open('{0}.txt'.format(module_name), 'a', encoding='utf-8')
    file.write(book_date + "\n")
    file.close()

def save_data_cn_en(module_name, cn_paragraph, en_paragraph):
    file = open('{0}.txt'.format(module_name), 'a', encoding='utf-8')
    file.write(cn_paragraph + "\t" + en_paragraph + "\n")
    file.close()

def run():
    root_url = 'http://www.bczzz.com/book/'
    module_name = ['短篇', '中篇', '长篇']
    headers = {
        'Referer': 'http://www.bczzz.com/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
    }
    for ml in module_name:
        module_url = root_url + ml + '/'
        get_book_url(root_url, module_name = ml, module_url = module_url, headers = headers)
        
        print(module_url)
        while True:
            module_content = get_html(s_url = module_url, s_headers = headers)
            next_page_url = module_content.xpath('//a[@class="next"]/@href')
            if not next_page_url:
                break
            next_page_url = 'http://www.bczzz.com/' + next_page_url[0].strip()
            module_url = next_page_url
            get_book_url(root_url, module_name = ml, module_url = module_url, headers = headers)
            print(module_url)

if __name__ == '__main__':
    run()