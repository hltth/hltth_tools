from cssselect import GenericTranslator, SelectorError, HTMLTranslator
from lxml.html import fromstring
import lxml
import requests

class CchnCrawler:
    def __init__(self) -> None:
        pass

    def crawl_thanh_hoa(self):
        result = open("/Users/hung/Downloads/z_hung_content.html", "w")

        for i in range(1,7):
            r = requests.get('https://syt.thanhhoa.gov.vn/web/chung-chi-hanh-nghe.htm?id_dm=1&cbCosoyte=5cae09ea-c404-8682-8460-48b936a8cc91&page=' + str(i))
            content = r.content
            expression = HTMLTranslator().css_to_xpath('table')
            document = fromstring(content)
            z = [lxml.html.tostring(e, encoding='unicode') for e in document.xpath(expression)]
            
            result.write(z[1])
            result.write('\n')
            print('Done ' + str(i))

    def crawl_hoa_binh(self):
        result = open("/Users/hung/Downloads/z_hung_content.html", "w")

        for i in range(1,3):
            r = requests.get('http://soytehoabinh.ddns.net/QLNV/laws/search/?is_advance=1&q=&sfrom=&sto=&area=8&cat=6&status=0&signer=0&subject=0&page=' + str(i))
            content = r.content
            expression = HTMLTranslator().css_to_xpath('table')
            document = fromstring(content)
            z = [lxml.html.tostring(e, encoding='unicode') for e in document.xpath(expression)]

            result.write(z[0])
            result.write('\n')
            print('Done ' + str(i))
            
            