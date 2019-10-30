"""
Định dạng thêm một số thuộc tính cho label
Coding here
-------------------------------------------------------------------------------
"""

#Khai bao thu vien
from tkinter import *

#Khai bao bien

#Chuong trinh chinh
window = Tk()

#Tittle window
window.title("Label Config")
#Window size
window.geometry('600x400')

#Su dung label
lbl_name = Label(window,text="Hello World")

#Dinh dang font chu cho label
lbl_name.config(font = "Arial,22")

#Chieu cao cua label
#lbl_name.config(heigh = 30, width = 100)

#Mau sac cua label
lbl_name.config(fg="red",bg="grey")

#Canh le cho label
lbl_name.config(justify=LEFT)

#Hien thi label
lbl_name.grid(column=10, row = 50)

window.mainloop()


"""
--------------------------------------------------------------------------------
Ending Code
