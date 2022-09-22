from prettytable import PrettyTable
from tinhthue import TinhThue
from add_dot_int import reformat_text
from no_accent_vietnamese import convert
import os


def cal_from_file(name_input, thue_ca_nam=0):
    name_folder = convert(name_input.lower().replace(" ", "_"))
    # tạo thư mục output nếu chưa có
    if not os.path.exists("output"):
        os.mkdir("output")
    # tạo thư mục output/ten_nguoi_tinh_thue nếu chưa có
    if not os.path.exists(f"output/{name_folder}"):
        os.mkdir(f"output/{name_folder}")

    # Tạo đối tượng tính thuế
    tinh_thue = TinhThue()

    # Đọc file input
    with open(f"input/input.txt", "r") as fin:
        lines = fin.readlines()
        # remove whitespace characters like `\n` at the end of each line
        lines = [x.strip() for x in lines]
        # dòng 1 là dữ liệu số năm dạng 2022 2021
        data_year = lines[0].split()
        for year_th in range(len(data_year)):
            table = PrettyTable(title=f"Bảng tính thuế thu nhập cá nhân năm {data_year[year_th]} của {name_input}")
            table.field_names = ["Tháng", "Thu nhập cá nhân (VND)", "Thu nhập chịu thuế (VND)", "Tiền Thuế (VND)"]
            for month in range(1, 13):
                data_month = lines[month + year_th * 12].split()
                tinh_thue.nhap_thong_tin_file(data_month[0], data_month[1], data_month[2])
                tinh_thue.tinh_thue()
                table.add_row(
                    [month, reformat_text(str(tinh_thue.thu_nhap)), reformat_text(str(tinh_thue.thu_nhap_chiu_thue)),
                     reformat_text(str(tinh_thue.tien_thue_thang))])
                thue_ca_nam += tinh_thue.tien_thue_thang
                if month == 12:
                    table.add_row(["", "", f"Tổng thuế TNCN cả năm {data_year[year_th]}", reformat_text(str(thue_ca_nam))])
                # cột Tháng căn giữa
                    table.align["Tháng"] = "c"
                # lưu file output vào thư mục output/{name_folder}
                    with open(f"output/{name_folder}/{name_folder}_tienThueNam{data_year[year_th]}.txt", "w") as fout:
                        fout.write(table.get_string())
                        print("\n\n")
                        fout.close()
                    with open(f"output/{name_folder}/{name_folder}_tienThueCacNam.txt", "a") as fin:
                        fin.write(table.get_string())
                        fin.write("\n\n")
                        fin.close()
                    print(table)
                    print("\n\n")
    print(f"Đã lưu file output vào thư mục output/{name_folder}\n")
    print("Cảm ơn bạn đã sử dụng chương trình của chúng tôi!\n")
    print("Chúc bạn có một ngày tốt lành!\n")
    input("Nhấn Enter để thoát chương trình\n")



