"""
Viết chương trình bao gồm 2 nút bấm (Manual và Automatic), 1 label thực hiện công việc sau:
Khi nhấn nút: Manual, mỗi lần click là mỗi lần hiển thị số lần nhấp chuột lên nút
Khi nhân nút: Automatic, sau mỗi giây giá trị của lable tự động tăng lên 1

Coding here
------------------------------------------------------------------------------
#Khai bao thu vien
from tkinter import *

#Khai bao bien

#Chuong trinh con

#Tao su kien click
def nhannut_Manual():
  global dem

  lbl_name.config(text=str(dem))
  dem=dem+1

def nhannut_Auto():

  def count():
    global dem2
    lbl_name.config(text=str(dem2))
    dem2=dem2+1
    lbl_name.after(1000,count)
  count()

#Chuong trinh chinh
window = Tk()

dem=0
dem2=0

#Thiet lap window
window.title("Button More Configuration")
window.geometry('600x400')
window.resizable(width=False, height=False)

#Thiet lap label
lbl_name = Label(window,text = "....")
lbl_name.config(font="Arial,20")
lbl_name.config(fg="Green")
#Hien thi label
lbl_name.grid(column=200,row=50)


#Thiet lap Button Manual
but_manual = Button(window)
but_manual.config(text="Manual")
but_manual.config(fg="Blue")
but_manual.config(bd=5)

#Tao su kien nhan nut
but_manual.config(command=nhannut_Manual)


#Thiet lap Button Auto
but_auto = Button(window)
but_auto.config(text="Automatic")
but_manual.config(fg="Green")
but_manual.config(bd=1)

#Tao su kien nhan nut
but_manual.config(command=nhannut_Manual)

#Tao su kien nhan nut
but_auto.config(command=nhannut_Auto)


#Hien thi button
but_manual.grid(column = 200, row = 100)

#Hien thi button
but_auto.grid(column = 400, row = 100)

window.mainloop()

"""
------------------------------------------------------------------------
Ending Code

Hàm lbl_name.after(1000,count) được dùng để tự động lặp lại sau mỗi giây.
