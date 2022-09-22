# Chương trình tính thuế thu nhập cá nhân
[Tiếng Anh](https://github.com/kr4zym3nvn/tinh-thue-thu-nhap-ca-nhan/tree/master) | **Tiếng Việt**
```
[]: # © 2022 Nguyễn Hữu Khoa x Lê Thảo Quyên
[]: # Version: 1.0.0
[]: # Date: 21 - 09 - 2022
[]: # Description: Một bài tập nhỏ của môn học Hệ thống thông tin ở trường
```
Nếu chương trình chạy không thành công, hãy xem lần lượt thử các bước sau:
1. Kiểm tra xem Python 3.x đã được cài đặt hay chưa và PATH đã được chỉnh đúng địa chỉ chưa 
2. Kiểm tra xem các packages phụ thuộc đã được cài đặt chưa
3. Kiểm tra xem các thông số đầu vào có sai không.
4. Nếu vẫn không được, hãy liên hệ với tác giả qua email: **nguyenkhoa376@duck.com**

## Giới thiệu
Chương trình tính thuế thu nhập cá nhân với 2 cách nhập dữ liệu đầu vào (hoặc từ file txt hoặc nhập từng tháng từ bàn phím). Chương trình sẽ tính toán và xuất ra màn hình kết quả thuế thu nhập cá nhân của người dùng.

Chương trình được viết căn cứ vào
- Luật _Thuế TNCN_ năm 2007
- Luật sửa đổi, bổ sung _Luật thuế thu nhập cá nhân_ năm 2012
- Thông tư _111/2013/TT-BTC_
- Nghị quyết _954/2020/UBTVQH14_

## Môi trường hoạt động

```
Windows
python 3.x
```

## Hướng dẫn sử dụng

1. Mở terminal
2. Chạy lệnh `python main.py` hoặc chạy file `run.bat` với quyền admin
3. Chọn cách nhập dữ liệu
4. Nhập dữ liệu
5. Chờ chương trình tính toán và xuất kết quả

Màn hình yêu cầu lựa chọn cách nhập dữ liệu
![](https://raw.githubusercontent.com/kr4zym3nvn/tinh-thue-thu-nhap-ca-nhan/master/img/menu_choice.png)

### Cách nhập dữ liệu từ file
Để nhập dữ liệu, hãy cập nhật file `input.txt` trong thư mục **input**

Bạn có thể xem ví dụ trong file `input_test.txt`
![](https://raw.githubusercontent.com/kr4zym3nvn/tinh-thue-thu-nhap-ca-nhan/master/img/input_test.png)

Với mỗi dòng là dữ liệu của 1 tháng với 3 thông số liên quan được phân tách bởi _khoảng trắng_: **Thu nhập**, **Số người phụ thuộc và số tiền bảo hiểm đã đóng**

### Hướng dẫn nhập dữ liệu từ bàn phím
Chương trình sẽ yêu cầu nhập từng tháng, mỗi tháng sẽ có 3 thông số liên quan: **Thu nhập**, **Số người phụ thuộc và số tiền bảo hiểm đã đóng**
![img](https://raw.githubusercontent.com/kr4zym3nvn/tinh-thue-thu-nhap-ca-nhan/master/img/input_keyboard.png)

## Kết quả
Chương trình sẽ xuất ra màn hình kết quả thuế thu nhập cá nhân của người dùng cùng với file txt trong thư mục `output/{your_name}`

![Display U can see](https://img.upanh.tv/2022/09/21/image44af2b60639a8118.png "Display you can see after all")
## Bổ sung
Tặng tôi ⭐️ nếu bạn thấy chương trình hữu ích nhé :D

