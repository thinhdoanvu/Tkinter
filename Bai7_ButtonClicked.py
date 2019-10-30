"""
Trong bài tập này hướng dẫn cách dùng nút nhấn để tạo sự kiện nhấp chuột lên nút
Sau khi nhấp chuột:
1. Hiển thị dòng text ở mục label
2. Khóa chức năng click chuột vô nút

Coding here
------------------------------------------------------------------------
"""
#Khai bao thu vien
from tkinter import *

#Khai bao bien


#Chuong trinh chinh
window = Tk()

#Tieu de cho window
window.title("Button Event")

#Thiet lap cho window
window.geometry('600x400')
window.resizable(width=False, height=False)

#Su dung label
lbl_name = Label(window, text = "My name is ...", font = "Arial,20", bg="grey")
#lbl_name.config(height=100, width = 100)

#Hien thi lable
lbl_name.grid(column=100, row=10)

#Su kien gi neu nut duoc nhan?
def nhannut():
  lbl_name.config(text="My name is dthinh")
  #Sau khi nhan nut xong thi Khoa nut nhan 
  but_ok.config(state=DISABLED) 

#Su dung button
but_ok = Button(window, text = "Click here",command=nhannut)

#hien thi nut nhan
but_ok.grid(column = 200, row = 200)

window.mainloop()

"""
--------------------------------------------------------------------------
Ending Code
Hàm nhannut được định nghĩa bởi: 
def nhannut():
  bl_name.config(text="My name is dthinh")
  #Sau khi nhan nut xong thi Khoa nut nhan 
  but_ok.config(state=DISABLED) 

Chú ý khoảng trắng bên phải chính là {} trong C hay begin end; trong Pascal
Để thực hiện thao tác click có gọi hàm nhannut được định nghĩa trước sử dụng từ khóa command.


Một sô thao tác của button như sau: config(option)
activebackground=
What background color to use when the button is active. The default is system specific. (the option database name is activeBackground, the class is Foreground)
activeforeground=
What foreground color to use when the button is active. The default is system specific. (activeForeground/Background)
anchor=
Controls where in the button the text (or image) should be located. Use one of N, NE, E, SE, S, SW, W, NW, or CENTER. Default is CENTER. (anchor/Anchor)
background=
The background color. The default is system specific. (background/Background)
bg=
Same as background.
bitmap=
The bitmap to display in the widget. If the image option is given, this option is ignored. (bitmap/Bitmap)
borderwidth=
The width of the button border. The default is platform specific, but is usually 1 or 2 pixels. (borderWidth/BorderWidth)
bd=
Same as borderwidth.
command=
A function or method that is called when the button is pressed. The callback can be a function, bound method, or any other callable Python object. If this option is not used, nothing will happen when the user presses the button. (command/Command)
compound=
Controls how to combine text and image in the button. By default, if an image or bitmap is given, it is drawn instead of the text. If this option is set to CENTER, the text is drawn on top of the image. If this option is set to one of BOTTOM, LEFT, RIGHT, or TOP, the image is drawn besides the text (use BOTTOM to draw the image under the text, etc.). Default is NONE. (compound/Compound)
cursor=
The cursor to show when the mouse is moved over the button. (cursor/Cursor)
default=
If set, the button is a default button. Tkinter will indicate this by drawing a platform specific indicator (usually an extra border). The default is DISABLED (no default behavior). (default/Default)
disabledforeground=
The color to use when the button is disabled. The background is shown in the background color. The default is system specific. (disabledForeground/DisabledForeground)
font=
The font to use in the button. The button can only contain text in a single font. The default is system specific. (font/Font)
foreground=
The color to use for text and bitmap content. The default is system specific. (foreground/Foreground)
fg=
Same as foreground.
height=
The height of the button. If the button displays text, the size is given in text units. If the button displays an image, the size is given in pixels (or screen units). If the size is omitted, it is calculated based on the button contents. (height/Height)
highlightbackground=
The color to use for the highlight border when the button does not have focus. The default is system specific. (highlightBackground/HighlightBackground)
highlightcolor=
The color to use for the highlight border when the button has focus. The default is system speciific. (highlightColor/HighlightColor)
highlightthickness=
The width of the highlight border. The default is system specific (usually one or two pixels). (highlightThickness/HighlightThickness)
image=
The image to display in the widget. If specified, this takes precedence over the text and bitmap options. (image/Image)
justify=
Defines how to align multiple lines of text. Use LEFT, RIGHT, or CENTER. Default is CENTER. (justify/Justify)
overrelief=
Alternative relief to use when the mouse is moved over the widget. If empty, always use the relief value. (overRelief/OverRelief)
padx=
Extra horizontal padding between the text or image and the border. (padX/Pad)
pady=
Extra vertical padding between the text or image and the border. (padY/Pad)
relief=
Border decoration. Usually, the button is SUNKEN when pressed, and RAISED otherwise. Other possible values are GROOVE, RIDGE, and FLAT. Default is RAISED. (relief/Relief)
repeatdelay=
(repeatDelay/RepeatDelay)
repeatinterval=
(repeatInterval/RepeatInterval)
state=
The button state: NORMAL, ACTIVE or DISABLED. Default is NORMAL. (state/State)
takefocus=
Indicates that the user can use the Tab key to move to this button. Default is an empty string, which means that the button accepts focus only if it has any keyboard bindings (default is on, in other words). (takeFocus/TakeFocus)
text=
The text to display in the button. The text can contain newlines. If the bitmap or image options are used, this option is ignored (unless the compound option is used). (text/Text)
textvariable=
Associates a Tkinter variable (usually a StringVar) to the button. If the variable is changed, the button text is updated. (textVariable/Variable)
underline=
Which character to underline, in a text label. Default is -1, which means that no character is underlined. (underline/Underline)
width=
The width of the button. If the button displays text, the size is given in text units. If the button displays an image, the size is given in pixels (or screen units). If the size is omitted, or zero, it is calculated based on the button contents. (width/Width)
wraplength=
Determines when a button’s text should be wrapped into multiple lines. This is given in screen units. Default is 0 (no wrapping). (wrapLength/WrapLength)
