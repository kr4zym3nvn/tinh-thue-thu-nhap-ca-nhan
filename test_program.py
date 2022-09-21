from prettytable import PrettyTable
from tinhthue import TinhThue
from add_dot_int import reformat_text

def test(name_test="test_program"):
    # mở file test.txt trong thư mục input để lấy dữ liệu test
    with open("input/test.txt", "r") as f:
        data = f.read()
    # tách dữ liệu thành từng dòng
    data = data.split("\n")
    # tạo đối tượng tính thuế
    tinh_thue = TinhThue()
    # lấy năm
    nam = data[0]
    ten_nguoi_tinh_thue = name_test
    # lấy dữ liệu test
    data = data[1:]
    # tạo bảng
    table = PrettyTable(title=f"Bảng tính thuế thu nhập cá nhân năm {nam} của {ten_nguoi_tinh_thue}")
    table.field_names = ["Tháng", "Thu nhập cá nhân (VND)", "Thu nhập chịu thuế (VND)", "Tiền Thuế (VND)"]
    tien_thue_ca_nam = 0
    for thang in tinh_thue.thang:
        # lấy dữ liệu test của tháng
        thang_data = data[thang - 1]
        # tách dữ liệu test thành từng phần
        thang_data = thang_data.split(" ")
        # lấy thu nhập
        tinh_thue.thu_nhap = int(thang_data[0]) * 1000000
        # lấy số người phụ thuộc
        tinh_thue.so_nguoi_phu_thuoc = int(thang_data[1])
        # lấy tiền bảo hiểm
        tinh_thue.tien_bao_hiem = int(thang_data[2]) * 1000000
        # tính thu nhập chịu thuế
        tinh_thue.thu_nhap_chiu_thue = tinh_thue.thu_nhap - tinh_thue.tien_bao_hiem - tinh_thue.so_nguoi_phu_thuoc * 4400000 - 11000000
        tinh_thue.tinh_thue()
        # thêm dữ liệu vào bảng
        table.add_row(
            [thang, reformat_text(str(tinh_thue.thu_nhap)), reformat_text(str(tinh_thue.thu_nhap_chiu_thue)),
             reformat_text(str(tinh_thue.tien_thue_thang))])
        tien_thue_ca_nam += tinh_thue.tien_thue_thang
        if thang == 12:
            table.add_row(["", "", f"Tổng thuế TNCN cả năm {nam}", reformat_text(str(tien_thue_ca_nam))])
            # căn giữa cột Tháng
            table.align["Tháng"] = "c"
            # lưu bảng vào file
            with open(f"output/{name_test}/{name_test}_tienThue{nam}.txt", "w") as f:
                f.write(str(table))
                f.write("\n\n")
            with open(f"output/{name_test}/{name_test}_tienThueCacNam.txt", "a") as f:
                f.write(str(table))
                f.write("\n\n")
            print(table)
            # dừng màn hình, bấm phím bất kỳ để tiếp tục
            input("Nhấn phím bất kỳ để tiếp tục...")