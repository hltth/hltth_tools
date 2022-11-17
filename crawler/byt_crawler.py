import csv
import json
import math
import http.client
import urllib.parse

import requests

class BytCrawler:
    def __init__(self, website=None, items_per_page=100):
        self.__website = website
        self.__items_per_page = items_per_page

    def crawl(self):
        if self.__website == 'cong_khai_gia':
            self.__file_name = 'cong_khai_gia.csv'            
            self.crawl_byt_cong_khai_gia()

    def chuan_hoa(self, input_string):
        if input_string is not None and isinstance(input_string, str):
            return input_string.replace('\n', '').replace('\r', '')
        else:
            return input_string       
    
    def crawl_byt_cong_khai_gia(self):
        url = "https://kekhaigiattbyt-api.moh.gov.vn/api/services/app/APICongKhaiGiaPublic/GetListByPaging"
        json_request = {"total":0,"totalpage":1,"skipCount":10,"maxResultCount":10,"filter":"","sorting":'',"isHasCongKhai":True}
        r = requests.post(url, json=json_request)
        data = r.json()

        total_records = data["result"]["totalCount"]

        print(total_records)
        
        items_data = data["result"]["items"]

        if not items_data:
            return

        maxResultCount = self.__items_per_page
        n = math.ceil(total_records / maxResultCount)

        # open file
        file = open(self.__file_name, 'w', encoding='utf-8', newline='')

        # open csv writer
        csv_writer = csv.writer(file, delimiter='|', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        # write header
        header =items_data[0].keys()
        csv_writer.writerow(header)
        
        # loop all pages

        for x in range(1166, n):
            skipCount = x * maxResultCount
            json_request = {"total":0,"totalpage":1,"skipCount":skipCount,"maxResultCount":maxResultCount,"filter":"","sorting":'',"isHasCongKhai":True}
            r = requests.post(url, json=json_request)
            print(json_request)
            data = r.json()
            items_data = data["result"]["items"]

            if not items_data:
                return

            #loop item and write to file
            for item in items_data:                
                # Writing data of CSV file
                vals = item.values() 
                vals = [self.chuan_hoa(val) for val in vals]
                csv_writer.writerow(vals)
        
        file.close()

        