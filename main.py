from prettytable import PrettyTable
from tinhthue import TinhThue
from remove_accent_vietnamese import convert
from cal_from_file import cal_from_file
from add_dot_int import reformat_text
from read_file_output import read_file_output
import datetime
import time
import os


def set_up_terminal():
    os.system("mode con: cols=120 lines=30")
    os.system("title Chương trình tự động tính thuế TNCN")
    os.system("cls")


def main():
    set_up_terminal()
    print()
    print("Chương trình tính thuế thu nhập cá nhân")
    print()
    print("Chọn cách nhập dữ liệu: ")
    print("1. Nhập dữ liệu từ file")
    print("2. Nhập dữ liệu từ bàn phím")
    print("3. Đọc kết quả đã tính thuế")
    print("4. Thoát")

    print()
    choice = input("Nhập lựa chọn của bạn: ")

    while True:
        if choice == "1":
            os.system("cls")
            print("Chương trình tính thuế thu nhập cá nhân - Đọc dữ liệu từ file")
            print()
            ten_nguoi_tinh_thue = input("Nhập tên của bạn: ")

            cal_from_file(ten_nguoi_tinh_thue)
            # trở lại menu chọn chức năng
            main()

        elif choice == "2":
            os.system("cls")
            print("Chương trình tính thuế thu nhập cá nhân nhập dữ liệu từ bàn phím")
            print()
            ten_nguoi_tinh_thue = input("Nhập tên của bạn: ")
            while True:
                try:
                    so_thue_tam_nop = int(input("Nhập số tiền thuế bạn đã nộp tạm (triệu VNĐ): "))
                    break
                except ValueError:
                    print("Bạn phải nhập số nguyên dương. Vui lòng nhập lại!")
                    continue
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
                while True:
                    try:
                        phu_thuoc = int(input(f"Nhập số người phụ thuộc năm {nam}: "))
                        break
                    except ValueError:
                        print("Bạn phải nhập số nguyên dương. Vui lòng nhập lại!")
                        continue
                while True:
                    try:
                        bao_hiem_xa_hoi = int(input(f"Nhập số tiền bảo hiểm xã hội năm {nam} (triệu VNĐ): "))
                        break
                    except ValueError:
                        print("Bạn phải nhập số nguyên dương. Vui lòng nhập lại!")
                        continue
                print("\nBạn đang nhập thu nhập năm", nam)
                print("Đơn vị tính: triệu VND")
                print()
                for thang in tinh_thue.thang:
                    tinh_thue.nhap_thong_tin(thang, phu_thuoc, bao_hiem_xa_hoi)
                    tinh_thue.tinh_thue()
                    tien_thue_hang_thang = {"Thang": thang, "Tien thue": tinh_thue.tien_thue_thang}
                    tinh_thue.thong_ke_tien_thue_cac_nam.append(tien_thue_hang_thang)
                    print()
                    print(f"Tiền thuế tháng {thang}: {tinh_thue.tien_thue_thang} VND")
                    print()

                    table.add_row(
                        [thang, reformat_text(str(tinh_thue.thu_nhap)),
                         reformat_text(str(tinh_thue.thu_nhap_chiu_thue)),
                         reformat_text(str(tinh_thue.tien_thue_thang))])
                    tien_thue_ca_nam += tinh_thue.tien_thue_thang
                    if thang == 12:
                        now = datetime.datetime.now()
                        table.add_row(["", "", f"Tổng thuế TNCN cả năm {nam}", reformat_text(str(tien_thue_ca_nam))])
                        # cột Tháng căn giữa
                        table.align["Tháng"] = "c"
                        with open(f"output/{ten_nguoi_tinh_thue_folder}/{ten_nguoi_tinh_thue_folder}_tienThueNam{nam}.txt",
                                  "w") as f:
                            f.write(str(table))
                            f.write("\n")
                            f.write(f"Thuế tạm nộp: {so_thue_tam_nop} triệu VND\n")
                            if (tien_thue_ca_nam - so_thue_tam_nop * 1000000) > 0:
                                f.write(
                                    f"Thuế TNCN còn phải nộp: {reformat_text(str(tien_thue_ca_nam - int(so_thue_tam_nop) * 1000000))} VND\n")
                            else:
                                f.write(
                                    f"Tiền được nhận lại: {reformat_text(str(int(so_thue_tam_nop) * 1000000 - tien_thue_ca_nam))} VND\n")
                            f.write("\n")
                            f.write(f"Ngày tạo file: {now.strftime('%d/%m/%Y %H:%M:%S')}")
                            f.close()
                        # Lưu bảng vào file có sẵn tienThueCacNam.txt
                        with open(
                                f"output/{ten_nguoi_tinh_thue_folder}/{ten_nguoi_tinh_thue_folder}_tienThueCacNam.txt",
                                "a") as f:
                            f.write(str(table))
                            f.write("\n")
                            f.write(f"Thuế tạm nộp: {so_thue_tam_nop} triệu VND\n")
                            if (tien_thue_ca_nam - so_thue_tam_nop * 1000000) > 0:
                                f.write(
                                    f"Thuế TNCN còn phải nộp: {reformat_text(str(tien_thue_ca_nam - int(so_thue_tam_nop) * 1000000))} VND\n")
                            else:
                                f.write(
                                    f"Tiền được nhận lại: {reformat_text(str(int(so_thue_tam_nop) * 1000000 - tien_thue_ca_nam))} VND\n")
                            f.write("\n")
                            f.write(f"Ngày tạo file: {now.strftime('%d/%m/%Y %H:%M:%S')}")
                            f.write("\n\n")
                            f.close()
                        print(f"{table}\n")
                        print(
                            f"{ten_nguoi_tinh_thue} đã nộp tạm {reformat_text(so_thue_tam_nop * 1000000)}  VND thuế TNCN năm {nam}" + "\n")
                        if (tien_thue_ca_nam - int(so_thue_tam_nop) * 1000000) > 0:
                            print(
                                f"Thuế TNCN còn phải nộp: {reformat_text(str(tien_thue_ca_nam - int(so_thue_tam_nop) * 1000000))} VND" + "\n")
                        else:
                            print(
                                f"Tiền được nhận lại: {reformat_text(str(int(so_thue_tam_nop) * 1000000 - tien_thue_ca_nam))} VND" + "\n")
                        print(f"Ngày tạo file: {now.strftime('%d/%m/%Y %H:%M:%S')}")
                        print(f"Đã lưu file output vào thư mục output/{ten_nguoi_tinh_thue_folder}\n")
            continue_cal = input("Bạn có muốn tiếp tục tính thuế không? (Y/N): ").lower()
            if continue_cal == "y":
                continue
            else:
                main()

        elif choice == "3":
            # Đọc file output
            os.system("cls")
            print("Đọc file output")
            name_input = convert(input("Nhập tên người bạn muốn xem: ").lower().replace(" ", "_"))
            read_file_output(name_input)
            main()
        elif choice == "4":
            print("Cảm ơn bạn đã sử dụng chương trình!")
            # delay 3s rồi thoát
            time.sleep(3)
            return False


main()
