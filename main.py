from tkinter import *
from tkinter import ttk


class calculate:
    def start(self):
        self.root = Tk()
        self.root.geometry("450x130")
        self.root.configure(bg="#B3E5FC")
        self.btn1 = Button(self.root, text="Калькулятор", width=25, bg="Azure", command=self.calculate)
        self.btn2 = Button(self.root, text="Перевод из целых чисел в римскую систему исчислений и обратно", width=55,
                           bg="Azure")
        self.btn3 = Button(self.root, text="Перевод из любой системы исчислений в любую систему исчислений", width=55,
                           bg="Azure")

        self.btn1.pack(ipadx=10, ipady=10)
        self.btn2.pack(ipadx=10, ipady=10)
        self.btn3.pack(ipadx=10, ipady=10)
        self.root.mainloop()

    def calculate(self):
      return