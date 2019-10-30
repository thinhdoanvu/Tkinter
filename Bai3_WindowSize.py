"""
Như đã đề cập ở bài tập 2, khi thực hiện chương trình đó, bạn sẽ thấy cửa sổ hiển thị bị thu gọn đúng bằng label.
Do vậy chúng ta cần thiết lập cửa sổ với chiều cao và chiều rộng ngay từ đâu.
"""

#Coding here,
#-----------------------------------------------------------------------------------------
#Khai báo thư viện
from tkinter import *

#Khai báo biến

#Chương trình chính
window = Tk()

#Hiển thị tiêu đề của Window
window.title("Window Size")

#Sử dụng label để hiện thị tên
lbl_name = Label(window, text = "My name is dthinh")
#Vị trí của label
lbl_name.grid(column = 0, row = 0)

#Set window size
window.geometry('300x200')


window.mainloop()
#-----------------------------------------------------------------------------------------
#Ending code!
"""
window.geometry('300x200') biểu diễn kích thước c
