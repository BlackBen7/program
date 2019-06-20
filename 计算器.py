from tkinter import *


class NumberTransfer:
    def __init__(self):

        self.frame = Tk()
        self.frame.title("进制转换器软件")
        self.frame.geometry("550x350+450+200")
        self.frame.resizable(0, 0)
        self.frame["bg"] = "white"
        # 添加图片
        # self.Banner_image = PhotoImage(file="./img/photo1.png")
        # self.Banner_top = Label(self.frame, image=self.Banner_image)
        # self.Banner_top.place(x=27, y=10)
        # 选择进制
        self.Label_select = Label(self.frame, text="请选择要输入的进制：",
                                  bg="white", font=("隶书", 12, "bold"))
        self.Label_select.place(x=30, y=150)
        self.var_number = IntVar()
        self.Radio_bin = Radiobutton(self.frame, text="二进制", variable=self.var_number, value=2,
                                     bg="white", font=("宋体", 12, "bold"))
        self.Radio_bin.place(x=195, y=150)
        self.Radio_oct = Radiobutton(self.frame, text="八进制", variable=self.var_number, value=8,
                                     bg="white", font=("宋体", 12, "bold"))
        self.Radio_oct.place(x=275, y=150)
        self.Radio_dec = Radiobutton(self.frame, text="十进制", variable=self.var_number, value=10,
                                     bg="white", font=("宋体", 12, "bold"))
        self.Radio_dec.place(x=355, y=150)
        self.Radio_hex = Radiobutton(self.frame, text="十六进制", variable=self.var_number, value=16,
                                     bg="white", font=("宋体", 12, "bold"))
        self.Radio_hex.place(x=435, y=150)

        # 输入区
        self.Label_input = Label(self.frame, text="请输入具体数值：", bg="white", font=("隶书", 12, "bold"))

        self.Label_input.place(x=65, y=190)
        self.var_input = StringVar()

        self.Entry_input = Entry(self.frame, textvariable=self.var_input, font=("隶书", 12, "bold"))
        self.Entry_input.place(x=205, y=194)
        self.Button_input = Button(self.frame, command=self.get_number, text="计算", font=("宋体", 14, "bold"))
        self.Button_input.place(x=430, y=190)
        # 显示结果
        self.Label_result = Label(self.frame, text="结果:", bg="white", fg="blue", font=("隶书", 12, "bold"))
        self.Label_result.place(x=135, y=230)
        self.Label_bin = Label(self.frame, text="二进制:", bg="white", fg="blue", font=("隶书", 12, "bold"))
        self.Label_bin.place(x=200, y=230)
        self.Label_bin_result = Label(self.frame, text="二进制输出结果",
                                      bg="white", fg="blue", font=("隶书", 12, "bold"))
        self.Label_bin_result.place(x=280, y=230)
        self.Label_oct = Label(self.frame, text="八进制:", bg="white", fg="blue", font=("隶书", 12, "bold"))
        self.Label_oct.place(x=200, y=250)
        self.Label_oct_result = Label(self.frame, text="八进制输出结果",
                                      bg="white", fg="blue", font=("隶书", 12, "bold"))
        self.Label_oct_result.place(x=280, y=250)
        self.Label_dec = Label(self.frame, text="十进制:", bg="white", fg="blue", font=("隶书", 12, "bold"))
        self.Label_dec.place(x=200, y=270)
        self.Label_dec_result = Label(self.frame, text="十进制输出结果",
                                      bg="white", fg="blue", font=("隶书", 12, "bold"))
        self.Label_dec_result.place(x=280, y=270)
        self.Label_hex = Label(self.frame, text="十六进制:", bg="white", fg="blue", font=("隶书", 12, "bold"))
        self.Label_hex.place(x=183, y=290)
        self.Label_hex_result = Label(self.frame, text="十六进制输出结果",
                                      bg="white", fg="blue", font=("隶书", 12, "bold"))
        self.Label_hex_result.place(x=280, y=290)

    def show(self):
        self.frame.mainloop()

    def transfer_number(self, number: int):
        number_list = []
        number_list.append(bin(number))
        number_list.append(oct(number))
        number_list.append(number)
        number_list.append(hex(number))
        return number_list

    def get_type_ten_number(self, type_number: int, number: str):
        if type_number == 2:
            return int(number, 2)
        if type_number == 8:
            return int(number, 8)
        if type_number == 10:
            return int(number)
        if type_number == 16:
            return int(number, 16)

    def get_number(self):
        input_number = self.var_input.get()  # 输入的数据
        type_number = self.var_number.get()  # 选择的禁止类型
        ten_number = self.get_type_ten_number(type_number, input_number)  # 把输入的任意类型都转换为十进制数
        number_list = self.transfer_number(ten_number)  # 转好的数再转化成其他进制数
        self.Label_bin_result["text"] = number_list[0]
        self.Label_oct_result["text"] = number_list[1]
        self.Label_dec_result["text"] = number_list[2]
        self.Label_hex_result["text"] = number_list[3]


if __name__ == "__main__":
    # 根据实例化一个对象
    this_gui = NumberTransfer()
    # 展示窗体
    this_gui.show()
