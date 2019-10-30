#Bài tập này hướng dẫn sử dụng các lable (chỉ hiển thị nội dung chứ không nhập nội dung như Textbox) như Window form của C#

#Coding here,
#-------------------------------------------------------------------------------------------
#Khai báo thư viện
from tkinter import *

#Khai báo biến

#Chương trình chính

window =Tk()

#Hiển thị nội dung lên tiêu đề.
window.title("Bai 2, su dung label");

#Hiển thị nội dung trong label

#Đặt tên biến cho label, trường hợp chúng ta có rất nhiều label sau này.
lbl_1 = Label(window, text="My name is dthinh")

#Vị trí hiển thị của label
lbl_1.grid(column=0, row=0)

window.mainloop()
#-------------------------------------------------------------------------------------------
#Ending code!
"""
Giải thích
lbl_1 là tên gọi của label, ví dụ label dùng để hiển thị tên là: lbl_name, hiển thị lương là: lbl_luong.
Việc đặt tên label sao cho dễ nhớ, để sau này biết gọi đến label nào cho tiện.

Label có cú pháp như sau:
Label(window, text="Text")

Cái này khá quen thuộc nếu ai đó từng lập trình giao diện với VB (VB6, 2010, 2016,...). Chú ý: Label phải viết hoa.

Sau khi đã gán tên là lbl_1, bây giờ sẽ có các thuộc tính cần được sử dụng. Một trong số đó là: lbl_1.grid().
Mỗi thuộc tính được gọi bởi dấu chấm (.). Trong C# hay VB tối đa là 8 thuộc tính.
Cú pháp của .grid như sau: lbl_1.grid(colum = ?, row = ?) - Tọa độ của label trong cửa sổ giao diện.
  
Khi thực hiện bài này, bạn sẽ thấy cửa sổ của bạn bé lại đúng bằng một cô gái, à không đúng bằng label vừa tạo.
Do đó, chúng ra cần điều chỉnh khung cửa sổ cố định kích thước bằng lệnh: window.geometry('300,200')
 
Trong đó, '300,200' lần lượt là chiều rộng và chiều cao.
"""
