class TinhThue:

    mien_tru = 11000000
    so_nguoi_phu_thuoc = 0
    tien_bao_hiem = 0
    thong_ke_tien_thue_cac_nam = []
    thu_nhap = 0
    thu_nhap_chiu_thue = 0
    tien_thue_thang = 0
    thang = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    nam = []

    def __init__(self):
        pass

    def nhap_thong_tin(self, month, phu_thuoc, bao_hiem):
        while True:
            try:
                self.thu_nhap = int(input("Nhập thu nhập tháng " + str(month) + ": ")) * 1000000
                break
            except ValueError:
                print("Vui lòng nhập số!")
        self.so_nguoi_phu_thuoc = int(phu_thuoc)
        self.tien_bao_hiem = int(bao_hiem) * 1000000

    def nhap_thong_tin_file(self, thu_nhap):
        self.thu_nhap = int(thu_nhap) * 1000000
        self.thu_nhap_chiu_thue = self.thu_nhap - self.tien_bao_hiem - self.mien_tru - self.so_nguoi_phu_thuoc * 4400000

    def nhap_nam(self):
        print("Nhập những năm bạn muốn tính thuế ")
        self.nam = [int(x) for x in input().split()]
        print()

    def tinh_thue(self):
        self.thu_nhap_chiu_thue = int(self.thu_nhap) - int(self.tien_bao_hiem) - int(self.mien_tru) - int(self.so_nguoi_phu_thuoc) * 4400000
        if self.thu_nhap_chiu_thue < 0:
            self.tien_thue_thang = 0
            self.thu_nhap_chiu_thue = 0
        elif 0 < self.thu_nhap_chiu_thue <= 5000000:
            self.tien_thue_thang = int(self.thu_nhap_chiu_thue * 0.05)
        elif 5000000 < self.thu_nhap_chiu_thue <= 10000000:
            self.tien_thue_thang = int(0.05 * 5000000 + (self.thu_nhap_chiu_thue - 5000000) * 0.1)
        elif 10000000 < self.thu_nhap_chiu_thue <= 18000000:
            self.tien_thue_thang = int(0.05 * 5000000 + 0.1 * 5000000 + (self.thu_nhap_chiu_thue - 10000000) * 0.15)
        elif 18000000 < self.thu_nhap_chiu_thue <= 32000000:
            self.tien_thue_thang = int(0.05 * 5000000 + 0.1 * 5000000 + 0.15 * 8000000 + (self.thu_nhap_chiu_thue - 18000000) * 0.2)
        elif 32000000 < self.thu_nhap_chiu_thue <= 52000000:
            self.tien_thue_thang = int(0.05 * 5000000 + 0.1 * 5000000 + 0.15 * 8000000 + 0.2 * 14000000 + (
                    self.thu_nhap_chiu_thue - 32000000) * 0.25)
        elif 52000000 < self.thu_nhap_chiu_thue <= 80000000:
            self.tien_thue_thang = int(0.05 * 5000000 + 0.1 * 5000000 + 0.15 * 8000000 + 0.2 * 14000000 + 0.25 * 20000000 + (
                    self.thu_nhap_chiu_thue - 52000000) * 0.3)
        elif self.thu_nhap_chiu_thue > 80000000:
            self.tien_thue_thang = int(0.05 * 5000000 + 0.1 * 5000000 + 0.15 * 8000000 + 0.2 * 14000000 + 0.25 * 20000000 + 0.3 * 28000000 + (
                    self.thu_nhap_chiu_thue - 80000000) * 0.35)

