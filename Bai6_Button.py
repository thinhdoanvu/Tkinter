"""
Bài tập này hướng dẫn sử dụng tạo ra một đối tượng có tên là button, cũng có các thuộc tính giống label.
Tuy nhiên,bài tập này có 2 sự bổ sung so với các bài trước:
1. Khóa tinh năng cho phép thay đổi kích cỡ của Window
2. Thêm thuộc tính cho BUTTON, tuy nhiên chưa thể tạo ra sự kiện click chuột như thực tế. Xem bài 7

Coding here
-------------------------------------------------------------------------------------------
"""

#Khai bao thu vien
from tkinter import *

#Khai bao bien

#Chuong trinh chinh
window = Tk()

#Title window form
window.title("Button Example")

#Window Size
window.geometry('600x400')
#Lock window resizeable
window.resizable(height=False, width=False)

#Su dung label
lbl_name=Label(window, text="My name is dthinh",font="Arial,20",fg="Blue",bg="white")

#Hien thi label name
lbl_name.grid(column=20, row = 200)

#Su dung Button (nut nhan)
but_ok=Button(window,text="Click here")
but_ok.config(fg="red",bg="grey")

#Hien thi button
but_ok.grid(column=200, row = 300)

window.mainloop()

"""
--------------------------------------------------------------------------------------------------
