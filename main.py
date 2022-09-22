from prettytable import PrettyTable
from tinhthue import TinhThue
from no_accent_vietnamese import convert
from cal_from_file import cal_from_file
from add_dot_int import reformat_text
import os


def main():
    print()
    print("Chương trình tính thuế thu nhập cá nhân")
    print()
    print("Chọn cách nhập dữ liệu: ")
    print("1. Nhập dữ liệu từ file")
    print("2. Nhập dữ liệu từ bàn phím")
    print("3. Thoát")
    print()
    choice = input("Nhập lựa chọn của bạn: ")

    while True:
        if choice == "1":
            os.system("cls")
            print("Chương trình tính thuế thu nhập cá nhân")
            print()
            ten_nguoi_tinh_thue = input("Nhập tên của bạn: ")
            cal_from_file(ten_nguoi_tinh_thue)
            break

        elif choice == "2":
            os.system("cls")
            print("Chương trình tính thuế thu nhập cá nhân")
            print()
            ten_nguoi_tinh_thue = input("Nhập tên của bạn: ")
            ten_nguoi_tinh_thue_folder = convert(ten_nguoi_tinh_thue.lower().replace(" ", "_"))
            # tạo thư mục output nếu chưa có
            if not os.path.exists("output"):
                os.mkdir("output")
            # tạo thư mục output/ten_nguoi_tinh_thue nếu chưa có
            if not os.path.exists(f"output/{ten_nguoi_tinh_thue_folder}"):
                os.mkdir(f"output/{ten_nguoi_tinh_thue_folder}")

            # Tạo đối tượng tính thuế
            tinh_thue = TinhThue()
            tinh_thue.nhap_nam()
            tien_thue_ca_nam = 0
            for nam in tinh_thue.nam:
                table = PrettyTable(title=f"Bảng tính thuế thu nhập cá nhân năm {nam} của {ten_nguoi_tinh_thue}")
                table.field_names = ["Tháng", "Thu nhập cá nhân (VND)", "Thu nhập chịu thuế (VND)", "Tiền Thuế (VND)"]
                print("Bạn đang nhập thu nhập năm", nam)
                print("Đơn vị tính: triệu VND")
                print()
                for thang in tinh_thue.thang:
                    tinh_thue.nhap_thong_tin(thang)
                    tinh_thue.tinh_thue()
                    tien_thue_hang_thang = {"Thang": thang, "Tien thue": tinh_thue.tien_thue_thang}
                    tinh_thue.thong_ke_tien_thue_cac_nam.append(tien_thue_hang_thang)
                    print()
                    print(f"Tiền thuế tháng {thang}: {tinh_thue.tien_thue_thang} VND")
                    print()

                    table.add_row(
                        [thang, reformat_text(str(tinh_thue.thu_nhap)), reformat_text(str(tinh_thue.thu_nhap_chiu_thue)),
                         reformat_text(str(tinh_thue.tien_thue_thang))])
                    tien_thue_ca_nam += tinh_thue.tien_thue_thang
                    if thang == 12:
                        table.add_row(["", "", f"Tổng thuế TNCN cả năm {nam}", reformat_text(str(tien_thue_ca_nam))])
                        # cột Tháng căn giữa
                        table.align["Tháng"] = "c"
                        with open(f"output/{ten_nguoi_tinh_thue_folder}/{ten_nguoi_tinh_thue_folder}_tienThue{nam}.txt", "w") as f:
                            f.write(str(table))
                        # Lưu bảng vào file có sẵn tienThueCacNam.txt
                        with open(f"output/{ten_nguoi_tinh_thue_folder}/{ten_nguoi_tinh_thue_folder}_tienThueCacNam.txt", "a") as f:
                            f.write(str(table))
                            f.write("\n\n")
                        print(table)
                        # dừng màn hình, bấm phím bất kỳ để tiếp tục
                        input("Nhấn phím bất kỳ để tiếp tục...")
                        os.system("cls")
            continue_cal = input("Bạn có muốn tiếp tục tính thuế không? (Y/N): ").lower()
            if continue_cal == "y":
                continue
            else:
                print("Cảm ơn bạn đã sử dụng chương trình!")
                break

        elif choice == "3":
            print("Cảm ơn bạn đã sử dụng chương trình!")
main()
