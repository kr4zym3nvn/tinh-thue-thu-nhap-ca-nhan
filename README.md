# A script for Calulating "Personal income". Driven by python
**English** | [Vietnamese](https://github.com/kr4zym3nvn/tinh-thue-thu-nhap-ca-nhan/tree/vietnamese)
```
[]: # © 2022 Nguyễn Hữu Khoa x Lê Thảo Quyên
[]: # Version: 1.0.0
[]: # Date: 21 - 09 - 2022
[]: # Description: A small exercise of the Information Systems subject at school
```
If the program crashes, please go through these steps:
1. Check if python 3.x is installed and path is set correctly  
2. Check if the dependency packages are installed.  
3. Check if the input parameters are wrong.  


## The operating environment

```
Windows
python 3.x
```

## Introduction

Includes 2 calculation features by importing data from month to month from keyboard or importing data from along with that is the feature of printing a beautiful, easy-to-see, intuitive, easy-to-follow board.

The program is written based on the Vietnamese tax law.
- Luật _Thuế TNCN_ năm 2007
- Luật sửa đổi, bổ sung _Luật thuế thu nhập cá nhân_ năm 2012
- Thông tư _111/2013/TT-BTC_
- Nghị quyết _954/2020/UBTVQH14_


## How to use

Open Terminal or Command Prompt and type the following command:
`pip install -r requirements.txt`

Then run the program by typing the following command `python main.py` or double-clicking the file `run.bat` with administrator privileges.

Double-click run.bat or run `python main.py` with administrator privileges

The program will ask you to choose how to calculate
![](https://raw.githubusercontent.com/kr4zym3nvn/tinh-thue-thu-nhap-ca-nhan/master/img/menu_choice.png)

### How input data from file
To import data, update the `input.txt` file in the **input** directory

You can see the example in the `input_test.txt` file.

With the first line being the years you want to calculate.
Each of the following 12 lines is the data of 12 months with 3 related parameters separated by `spaces`: **Income**, **number of dependents and amount of insurance paid**

![](https://raw.githubusercontent.com/kr4zym3nvn/tinh-thue-thu-nhap-ca-nhan/master/img/input_test.png)

`input_test.txt`

### How input data from keyboard
The program will ask you to enter the data for each month.![img](https://raw.githubusercontent.com/kr4zym3nvn/tinh-thue-thu-nhap-ca-nhan/master/img/input_keyboard.png)

After doing what the program asks you will get a statistics table like below along with the txt file in the ```output/{your_name}``` folder

![Display U can see](https://img.upanh.tv/2022/09/21/image44af2b60639a8118.png "Display you can see after all")

## Extra
Give a ⭐️ if this project helped you!

