"""
Viết chương trình tạo ra một danh sách các tốc độ truyền tin cho combo box, mỗi lần nhấn nút OK sẽ lấy giá trị của combo box
và hiển thị trong label có tên là lbl_baud.
Coding here,
-----------------------------------------------------------------
"""

#Khai bao thu vien
from tkinter import *
from tkinter.ttk import *

#Su dung cho combo box

#Chuong trinh con
def nhannut():
  lbl_baud.config(text=cmb_baud.get() + " bit/s")

#Chuong trinh chinh
window = Tk()

#Thiet lap title window
window.title("Su dung Combo box")
window.geometry('600x400')
window.resizable(height=False, width=False)

#Thiet lap label_name
lbl_name = Label(window,text="Toc do truyen du lieu: ")
#lbl_name.config(fg="Blue") #Khong hieu sao ko co dong bay thi no khong bao loi khi su dung combo box
lbl_name.grid(column=0, row=0)

#Thiet lap label_baud
lbl_baud = Label(window,text="")
#lbl_name.config(fg="Blue") #Khong hieu sao ko co dong bay thi no khong bao loi khi su dung combo box
lbl_baud.grid(column=100, row=0)

#Thiet lap button
but_OK = Button(window)
but_OK.config(text="OK")
but_OK.config(command=nhannut)
but_OK.grid(column=100,row=200)


#Thiet lap text box
#txt_name=Entry(window,width=20)
#txt_name.grid(column=100,row=20)

#Thiet lap combo box
cmb_baud = Combobox(window)
cmb_baud['values']= (512,1024,2048,9600,11200, "speed transfer")
cmb_baud.current(5) #Chon toc do truyen mac dinh
cmb_baud.grid(column=0, row=100)


window.mainloop()

"""
-----------------------------------------------------------------
Ending code,
#Thiet lap combo box
cmb_baud = Combobox(window)
cmb_baud['values']= (512,1024,2048,9600,11200, "speed transfer")
cmb_baud.current(5) #Chon toc do truyen mac dinh
cmb_baud.grid(column=0, row=100)

#Chuong trinh con
def nhannut():
  lbl_baud.config(text=cmb_baud.get() + " bit/s")
