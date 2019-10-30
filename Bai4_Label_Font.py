"""
Trong bài tập này, sẽ giải quyết bài toán fontsize mặc định của Label theo tiêu chuẩn của Window size, tuy nhiên 
chúng ta có thể thay đổi cỡ chữ, máu sắc của label.

Coding here,
---------------------------------------------------------------------
"""
Khai bao thu vien
from tkinter import *

#Khai bao bien

#Chuong trinh chinh
window = Tk()

#Tieu de cua so:
window.title("Setting Font...")

#Set window size
window.geometry('300x200')

#Su dung label
lbl_name = Label(window, text = "My name is dthinh")

#Dat cac thuoc tinh cho label
lbl_name.config(fg="red")
lbl_name.config(bg="black")
lbl_name.config(font="Arial,20")

#Setting vi tri cua lable
lbl_name.grid(column=10, row=10)


window.mainloop()

#---------------------------------------------------------------------
#Ending code!
"""
Chú ý: lbl_name.grid(column=10, row=10) sẽ đặt sau các khối của label
lbl_name.config sẽ chứa tất cả các thiết lập của label.

activebackground= The colors "white", "black", "red", "green", "blue", "cyan", "yellow", and "magenta"
activeforeground= The colors "white", "black", "red", "green", "blue", "cyan", "yellow", and "magenta"
anchor= Use one of N, NE, E, SE, S, SW, W, NW, or CENTER. Default is CENTER. (anchor/Anchor)
background/bg=
bitmap=
borderwidth/bd=
compound=Controls how to combine text and image in the label. BOTTOM, LEFT, RIGHT, or TOP, NONE ís default
cursor=
disabledforeground=
font=
foreground/fg= The colors "white", "black", "red", "green", "blue", "cyan", "yellow", and "magenta"
height=
highlightbackground=
highlightcolor=
highlightthickness=
image=
justify=LEFT, RIGHT, or CENTER (default). 
padx=Extra horizontal padding to add around the text. The default is 1 pixel. (padX/Pad)
pady=
relief=Border decoration. The default is FLAT. Other possible values are SUNKEN, RAISED, GROOVE, and RIDGE. 
state=Label state. This option controls how the label is rendered. The default is NORMAL. Other possible values are ACTIVE and DISABLED. (state/State)
takefocus=
text=The text to display in the label. The text can contain newlines. If the bitmap or image options are used, this option is ignored. (text/Text)
textvariable=Associates a Tkinter variable (usually a StringVar) with the label. If the variable is changed, the label text is updated. (textVariable/Variable)
underline=Default is -1 (no underline).
width=
wraplength=Determines when a label’s text should be wrapped into multiple lines. This is given in screen units. Default is 0 (no wrapping).
