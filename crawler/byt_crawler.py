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
        if self.__website == 'cong_bo_thuoc':
            self.__file_name = 'cong_bo_thuoc.csv'
            self.crawl_byt_cong_bo_thuoc()

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

    def crawl_byt_cong_bo_thuoc(self):
        url = "https://dichvucong.dav.gov.vn/api/services/app/soDangKy/GetAllPublicServerPaging"
        json_request = {"KichHoat":True,"SoDangKyThuoc":{},"skipCount":15,"maxResultCount":15,"sorting":''}
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
        header = ["hoatChatHamLuong","dangBaoChe","dongGoi","tieuChuan","tieuChuanId","tuoiTho","tenCongTyDangKy","nuocDangKyId","nuocDangKy","diaChiDangKy","tenCongTySanXuat","nuocSanXuat","diaChiSanXuat","nuocSanXuatId","dotCap","ngayCapSoDangKy","soQuyetDinh","hoatChatChinh","messageError","isCapNhatNHHSDK","tenHoatChatChinh","hoatChatDangKy","hamLuong","hangSanXuat","donViTinh","giaDangKy","tenKhongDau","coSoSanXuat","ketQua","isLuongCapNhat","listNoiDungThayDoi","isHetHan","maThuoc","tenThuoc","soDangKy","ngayCapSoDangKy","ngayGiaHanSoDangKy","ngayHetHanSoDangKy","soQuyetDinh","urlSoQuyetDinh","dotCap","isCapNhatNHHSDK","urlCongVanRutSoDangKy","hoatChatHamLuongCB","hoatChatChinh","hoatChatChinhId","hamLuong","dangBaoChe","dangBaoCheId","dongGoi","dongGoiJson","maDuongDung","tenDuongDung","tieuChuan","tieuChuanId","tuoiTho","loaiThuoc","loaiThuocId","nhomThuoc","nhomThuocId","urlHuongDanSuDung","urlNhan","urlNhanVaHDSD","ksdbisHoSoACTD","ksdbisHoSoLamSang","ksdbnguoiLap","ksdbchuTichHoiDong","ksdbthuKyHoiDong","ksdbnguoiDuyet","ksdbngayQuyetDinhCongVan","ksdbsoQuyetDinhCongVan","loaiVacXin","phongBenh","congTySanXuatId","tenCongTySanXuat","diaChiSanXuat","nuocSanXuat","nuocSanXuatId","congTyDangKyId","tenCongTyDangKy","diaChiDangKy","nuocDangKy","nuocDangKyId","phanLoaiThuocEnum","ghiChu","isActive","nguonDuLieuEnum","trangThai","lyDoSuaDoi","doanhNghiepId","mstDoanhNghiep","isXacNhanSoHuuDoanhNghiep","isDaRutSoDangKy","isDeleted","deleterUserId","deletionTime","lastModificationTime","lastModifierUserId","creationTime","creatorUserId","id"]
                
        csv_writer.writerow(header)
        
        # loop all pages

        for x in range(1, n):
            skipCount = x * maxResultCount
            json_request = {"KichHoat":True,"SoDangKyThuoc":{},"skipCount":skipCount,"maxResultCount":maxResultCount,"sorting":''}
            r = requests.post(url, json=json_request)
            print(json_request)
            data = r.json()
            items_data = data["result"]["items"]

            if not items_data:
                return

            #loop item and write to file
            for item in items_data:                
                # Writing data of CSV file
                vals = [item["hoatChatHamLuong"],item["dangBaoChe"],item["dongGoi"],item["tieuChuan"],item["tieuChuanId"],item["tuoiTho"],item["tenCongTyDangKy"],item["nuocDangKyId"],item["nuocDangKy"],item["diaChiDangKy"],item["tenCongTySanXuat"],item["nuocSanXuat"],item["diaChiSanXuat"],item["nuocSanXuatId"],item["dotCap"],item["ngayCapSoDangKy"],item["soQuyetDinh"],item["hoatChatChinh"],item["messageError"],item["isCapNhatNHHSDK"],item["tenHoatChatChinh"],item["hoatChatDangKy"],item["hamLuong"],item["hangSanXuat"],item["donViTinh"],item["giaDangKy"],item["tenKhongDau"],item["coSoSanXuat"],item["ketQua"],item["isLuongCapNhat"],item["listNoiDungThayDoi"],item["isHetHan"],item["maThuoc"],item["tenThuoc"],item["soDangKy"],item["thongTinDangKyThuoc"]["ngayCapSoDangKy"],item["thongTinDangKyThuoc"]["ngayGiaHanSoDangKy"],item["thongTinDangKyThuoc"]["ngayHetHanSoDangKy"],item["thongTinDangKyThuoc"]["soQuyetDinh"],item["thongTinDangKyThuoc"]["urlSoQuyetDinh"],item["thongTinDangKyThuoc"]["dotCap"],item["thongTinDangKyThuoc"]["isCapNhatNHHSDK"],		item["thongTinRutSoDangKy"]["urlCongVanRutSoDangKy"],item["thongTinThuocCoBan"]["hoatChatHamLuong"],item["thongTinThuocCoBan"]["hoatChatChinh"],item["thongTinThuocCoBan"]["hoatChatChinhId"],item["thongTinThuocCoBan"]["hamLuong"],item["thongTinThuocCoBan"]["dangBaoChe"],item["thongTinThuocCoBan"]["dangBaoCheId"],item["thongTinThuocCoBan"]["dongGoi"],item["thongTinThuocCoBan"]["dongGoiJson"],item["thongTinThuocCoBan"]["maDuongDung"],item["thongTinThuocCoBan"]["tenDuongDung"],item["thongTinThuocCoBan"]["tieuChuan"],item["thongTinThuocCoBan"]["tieuChuanId"],item["thongTinThuocCoBan"]["tuoiTho"],item["thongTinThuocCoBan"]["loaiThuoc"],item["thongTinThuocCoBan"]["loaiThuocId"],item["thongTinThuocCoBan"]["nhomThuoc"],item["thongTinThuocCoBan"]["nhomThuocId"],		item["thongTinTaiLieu"]["urlHuongDanSuDung"],item["thongTinTaiLieu"]["urlNhan"],item["thongTinTaiLieu"]["urlNhanVaHDSD"],item["thuocKiemSoatDacBiet"]["isHoSoACTD"],item["thuocKiemSoatDacBiet"]["isHoSoLamSang"],item["thuocKiemSoatDacBiet"]["nguoiLap"],item["thuocKiemSoatDacBiet"]["chuTichHoiDong"],item["thuocKiemSoatDacBiet"]["thuKyHoiDong"],item["thuocKiemSoatDacBiet"]["nguoiDuyet"],item["thuocKiemSoatDacBiet"]["ngayQuyetDinhCongVan"],item["thuocKiemSoatDacBiet"]["soQuyetDinhCongVan"],item["vacXinSinhPham"]["loaiVacXin"],item["vacXinSinhPham"]["phongBenh"],		item["congTySanXuatId"],		item["congTySanXuat"]["tenCongTySanXuat"],item["congTySanXuat"]["diaChiSanXuat"],item["congTySanXuat"]["nuocSanXuat"],item["congTySanXuat"]["nuocSanXuatId"],		item["congTyDangKyId"],		item["congTyDangKy"]["tenCongTyDangKy"],item["congTyDangKy"]["diaChiDangKy"],item["congTyDangKy"]["nuocDangKy"],item["congTyDangKy"]["nuocDangKyId"],item["phanLoaiThuocEnum"],item["ghiChu"],item["isActive"],item["nguonDuLieuEnum"],item["trangThai"],item["lyDoSuaDoi"],item["doanhNghiepId"],item["mstDoanhNghiep"],item["isXacNhanSoHuuDoanhNghiep"],item["isDaRutSoDangKy"],item["isDeleted"],item["deleterUserId"],item["deletionTime"],item["lastModificationTime"],item["lastModifierUserId"],item["creationTime"],item["creatorUserId"],item["id"]]
                
                vals = [self.chuan_hoa(val) for val in vals]
                csv_writer.writerow(vals)
                        
        file.close()

        