# hiển thị danh sách file trong thư mục output
import os
from remove_accent_vietnamese import convert

def read_file_output(name):
    # kiểm tra xem có thư mục name hay không, nếu không thấy yêu cầu nhập lại tên người muốn tính
    while not os.path.isdir("output/" + name):
        name = convert(input("Không tìm thấy người này, vui lòng nhập lại: ").lower().replace(" ", "_"))

    while True:
        print()
        print("Danh sách file đã tính thuế: \n")
        # in ra danh sách file kèm số thứ tự ở đầu
        print("0. Quay lại menu chính")
        for i, file in enumerate(os.listdir(f"output/{name}")):
            print(f"{i + 1}. {file}")
        # for file in os.listdir(f"output/{name}"):
        #     print(file)
        # chọn file muốn đọc bằng cách nhập số thứ tự của file, nếu số thứ tự không hợp lệ yêu cầu nhập lại
        while True:
            try:
                file = int(input("\nChọn file muốn đọc (nhập số): "))
                if 0 < file <= len(os.listdir(f"output/{name}")):
                    break
                elif file == 0:
                    return
                else:
                    print("Số thứ tự không hợp lệ, vui lòng nhập lại")
            except ValueError:
                print("Số thứ tự không hợp lệ, vui lòng nhập lại")
        # đọc file đã chọn
        with open(f"output/{name}/{os.listdir(f'output/{name}')[file - 1]}", "r") as f:
            print(f.read())
        # hiển thị dữ liệu
        print("\nBạn có muốn đọc thêm file khác không?")
        print("1. Có")
        print("2. Không, tôi muốn quay về Menu chính")
        choice = input("Nhập lựa chọn của bạn: ")
        if choice == "2":
            return False
        elif choice == "1":
            continue
