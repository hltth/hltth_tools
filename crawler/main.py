from cssselect import GenericTranslator, SelectorError, HTMLTranslator
from lxml.html import fromstring
import lxml
import requests
from cchn_crawler import CchnCrawler

crawler = CchnCrawler()

crawler.crawl_hoa_binh()