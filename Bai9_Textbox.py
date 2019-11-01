"""
Chương trình sử dụng textbox để nhập thông tin và hiển trị trên label sau khi click chuột.
Khi khởi động chương trình, con trỏ chuột nhấp nháy tại ô textbox để nhập dữ liệu.
Coding here,
--------------------------------------------------------------------------------
"""

#Khai bao thu vien
from tkinter import *

#Khai bao bien


#Chuong trinh con
def nhannut():
  thongbao="Hello anh, "+txt_name.get()
  lbl_name.config(text=thongbao)
  #an khung textbox
  txt_name.config(state=DISABLED)

#Chuong trinh chinh
window = Tk()

#Thiet lap window
window.title("Thao tac voi Textbox")
window.geometry('600x400')
window.resizable(width=False, height=False)

#Thao tac voi label
lbl_name = Label(window)
lbl_name.config(text="Hello, what's your name? ")
lbl_name.config(fg="Blue")
lbl_name.config(font="Arial,20")
#lbl_name.config(bg="grey")
#lbl_name.config(height=30,width=200)

lbl_name.grid(column=0,row=0)

#Thao tac voi Button
but_OK=Button(window)
but_OK.config(text = "Display")
but_OK.config(fg="Green")
but_OK.config(bd=1)

but_OK.grid(column = 200, row = 200)

#Tao su kien clicked
but_OK.config(command=nhannut)


#Thao tac voi Textbox
txt_name = Entry(window,width=10)
txt_name.grid(column=200, row=0)
#dat con tro chuot vo o Text
txt_name.focus()

window.mainloop()

"""
Ending code,
--------------------------------------------------------------------------------
#Thao tac voi Textbox
txt_name = Entry(window,width=10)
txt_name.grid(column=200, row=0)
#dat con tro chuot vo o Text
txt_name.focus()
