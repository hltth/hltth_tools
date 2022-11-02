from cssselect import GenericTranslator, SelectorError, HTMLTranslator
from lxml.html import fromstring
import lxml
import requests

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