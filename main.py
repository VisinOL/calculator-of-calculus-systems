from tkinter import *
from tkinter import ttk

class calculate_app:
    def two_button(self):
        self.root.destroy()
        self.window_button2 = Tk()
        self.window_button2.geometry("1750x200")
        self.window_button2.configure(bg="#B3E5FC")
        self.text = ttk.Label(text="Римляне, как известно, использовали для записи числа латинские буквы.Считается, что римская система счисления является классическим примером непозиционной системы счисления,",background="Azure")
        self.text1 = ttk.Label(text=" то есть такой системы счисления, в которой величина, которую обозначает цифра, не зависит от положения в числе.Напомним,",background="Azure")
        self.text2 = ttk.Label(text=" что в римской системе счисления I обозначает 1, V обозначает 5, X — 10, L — 50, C — 100, D — 500, M — 1000.",background="Azure")
        self.text3 = ttk.Label(text="Например, число 3 в римской системе счисления будет обозначаться как III.Однако на самом деле не все так просто,",background="Azure")
        self.text4 = ttk.Label(text=" и она не является полностью непозиционной системой счисления, потому что в римской системе счисления есть дополнительное правило,",background="Azure")
        self.text5 = ttk.Label(text=" которое влияет на величину, которую обозначает цифра, в зависимости от ее положения.Правило это запрещает употреблении одной и той же цифры более 3 раз подряд,",background="Azure")
        self.text6 = ttk.Label(text=" поэтому три это III, а четыре это уже IV, и I(1), стоящая перед большей цифрой V(5), обозначает вычитание, то есть фактически равна -1.",background="Azure")
        self.back_button_third = Button(text="Назад", command=self.back_to_start_from_two_button)
        self.text.config(font=("Courier", 13))
        self.text1.config(font=("Courier", 13))
        self.text2.config(font=("Courier", 13))
        self.text3.config(font=("Courier", 13))
        self.text4.config(font=("Courier", 13))
        self.text5.config(font=("Courier", 13))
        self.text6.config(font=("Courier", 13))
        self.text.pack()
        self.text1.pack()
        self.text2.pack()
        self.text3.pack()
        self.text4.pack()
        self.text5.pack()
        self.text6.pack()
        self.back_button_third.pack()
        self.window_button2.mainloop()

    def third_button(self):
        self.root.destroy()
        self.window_button3 = Tk()
        self.window_button3.configure(bg="#B3E5FC")
        text = """Перевод из одной системы исчисления в другую может быть выполнен с помощью различных методов, включая преобразование чисел по основанию, умножение и деление, а также использование таблиц перевода.

Пример 1: Перевод из двоичной системы в десятичную систему.
Для этого необходимо умножить каждую цифру двоичного числа на соответствующую степень 2 и сложить результаты. Например, число 1011 в двоичной системе будет равно 11 в десятичной системе (1*2^3 + 0*2^2 + 1*2^1 + 1*2^0).

Пример 2: Перевод из шестнадцатеричной системы в десятичную систему.
Аналогично можно умножить каждую цифру шестнадцатеричного числа на соответствующую степень 16 и сложить результаты. Например, число 3A в шестнадцатеричной системе будет равно 58 в десятичной системе (3*16^1 + 10*16^0).

Пример 3: Перевод из десятичной системы в двоичную систему.
Для этого можно делить число на 2 и запоминать остатки от деления. Например, число 25 в десятичной системе будет равно 11001 в двоичной системе (25 / 2 = 12 (остаток 1), 12 / 2 = 6 (остаток 0), 6 / 2 = 3 (остаток 0), 3 / 2 = 1 (остаток 1), 1 / 2 = 0 (остаток 1)).

Таким образом, существует несколько способов перевода чисел из одной системы исчисления в другую, и выбор метода зависит от конкретной задачи и удобства для выполнения перевода."""
        txt = ttk.Label(text=text,background="Azure")
        self.back_button_third = Button(text="Назад", command=self.back_to_start_from_third_button)
        txt.config(font=("Courier", 10))
        txt.pack()
        self.back_button_third.pack()
        self.window_button2.mainloop()



    def back_to_start_from_two_button(self):
        self.window_button2.destroy()
        self.start()

    def back_to_start_from_third_button(self):
        self.window_button3.destroy()
        self.start()

    def start(self):
        self.root = Tk()
        self.root.geometry("450x130")
        self.root.configure(bg="#B3E5FC")
        self.btn1 = Button(self.root, text="Калькулятор", width=25, bg="Azure", command=self.first_button)
        self.btn2 = Button(self.root, text="Перевод из целых чисел в римскую систему исчислений и обратно", width=55,
                           bg="Azure", command=self.two_button)
        self.btn3 = Button(self.root, text="Перевод из любой системы исчислений в любую систему исчислений", width=55,
                           bg="Azure", command=self.third_button)

        self.btn1.pack(ipadx=10, ipady=10)
        self.btn2.pack(ipadx=10, ipady=10)
        self.btn3.pack(ipadx=10, ipady=10)
        self.root.mainloop()

    def first_button(self):
        self.root.destroy()
        self.window_button1 = Tk()
        self.window_button1.geometry("400x250")
        self.window_button1.configure(bg="#B3E5FC")
        answer = ttk.Label(text="Введите число").pack()
        self.entry_calculate1 = ttk.Entry(width=300).pack(anchor=NW, padx=8, pady= 8)
        value1 = ttk.Label(text="Введите из какой системы исчислений нужно перевести")
        value1.config(font=("Courier", 10))
        value1.pack(anchor=NW)
        self.entry_calculate2 = ttk.Entry().pack(anchor=NW,pady= 8)
        value2 = ttk.Label(text="Введите в какую систему исчислений нужно перевести")
        value2.config(font=("Courier", 10))
        value2.pack(anchor=NW)
        self.entry_calculate3 = ttk.Entry().pack(anchor=NW,pady= 8)
        self.btn3 = Button(text="Перевести", width=55,bg="Azure", command=self.answer_to_calculus).pack()
        self.window_button1.mainloop()

    def answer_to_calculus(self):
        self.window_button1.destroy()
        self.answer_window = Tk()
        self.answer_window.configure(bg="#B3E5FC")
        self.answer_window.geometry("400x250")

        self.answer_window.mainloop()
if __name__ == "__main__":
    app = calculate_app()
    app.start()
