from cssselect import GenericTranslator, SelectorError, HTMLTranslator
from lxml.html import fromstring
import lxml
import requests
from cchn_crawler import CchnCrawler
from byt_crawler import BytCrawler

crawler = BytCrawler(website='cong_bo_thuoc')

crawler.crawl()