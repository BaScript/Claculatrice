from tkinter import *
import math
from tkinter import messagebox

calcul = Tk()
calcul.title("Calculatrice")
calcul.configure(background="beige")
calcul.resizable(width=False, height=False)
calcul.geometry("400x410") 
icon = PhotoImage(file = "icc.jpg")
calcul.iconphoto(False,icon) 

calculatrice = Frame(calcul)
calculatrice.pack()

format_txt = Entry(calculatrice, font=("arial",20),width=20, bg="beige", bd=10, justify="right")
format_txt.grid(row=0, column=0, columnspan=4, sticky="we", pady=(5,0),ipadx=10,ipady=10)
format_txt.insert(0, "0")


class Calculatrice:
    def __init__(self):
        self.total = 0
        self.current = ""
        self.input_value = True
        self.check_sum = False
        self.operator = ""
        self.result = False
    
    def numberEnter(self, num):
        self.result = False
        firstnum = format_txt.get()
        secondnum = str(num)
        if self.input_value:
            self.current = secondnum
            self.input_value = False
        else:
            if secondnum == ".":
                if secondnum in firstnum:
                    return
            self.current = firstnum + secondnum
        self.display(self.current)

    def sum_of_total(self):
        self.result = True
        self.current = float(self.current)
        if self.check_sum == True:
            self.fonction()
        else:
            self.total = float(format_txt.get())

    def fonction(self):
        if self.operator == "add":
            self.total += self.current
        if self.operator == "sub":
            self.total -= self.current
        if self.operator == "mul":
            self.total *= self.current
        if self.operator == "div":
            self.total /= self.current
        if self.operator == "mod":
            self.total %= self.current
        self.input_value = True
        self.check_sum = False
        self.display(self.total)

    def operateur(self, operator):
        self.current = float(self.current)
        if self.check_sum:
            self.fonction()
        elif not self.result:
            self.total = self.current
            self.input_value = True
        self.check_sum = True
        self.operator = operator
        self.result = False

    def display(self, value):
        format_txt.delete(0, END)
        format_txt.insert(0, value)         

    def clear(self):
        self.result = False
        if len(self.current) > 0:
            if len(self.current) == 1:
                self.display(0)
                self.input_value == True
            else:
                self.current = self.current[0:len(self.current)-1]
                self.display(self.current)
        else:
            self.display(0)
            self.input_value = True

    def clearAll(self):
        self.display(0)
        self.input_value = True

    def pi(self):
        self.result = False
        self.current = math.pi
        self.display(self.current)
    def two_pi(self):
        self.result = False
        self.current = math.tau
        self.display(self.current)

    def e(self):
        self.result = False
        self.current = math.e
        self.display(self.current)
    def exp(self):
        self.result = False
        self.current = math.exp
        self.display(self.current)
    
    def log(self):
        self.result = False
        self.current = math.log(float(format_txt.get()))
        self.display(self.current)

    def log2(self):
        self.result = False
        self.current = math.log2(float(format_txt.get()))
        self.display(self.current)

    def log10(self):
        self.result = False
        self.current = math.log10(float(format_txt.get()))
        self.display(self.current)
    
    def log1p(self):
        self.result = False
        self.current = math.log1p(float(format_txt.get()))
        self.display(self.current)
    
    def lgamma(self):
        self.result = False
        self.current = math.lgamma(float(format_txt.get()))
        self.display(self.current)

    def cos(self):
        self.result = False
        self.current = math.cos(float(format_txt.get()))
        self.display(self.current)
    def sin(self):
        self.result = False
        self.current = math.sin(float(format_txt.get()))
        self.display(self.current)
    def tan(self):
        self.result = False
        self.current = math.tan(float(format_txt.get()))
        self.display(self.current)
    def cosh(self):
        self.result = False
        self.current = math.cosh(float(format_txt.get()))
        self.display(self.current)
    def acosh(self):
        self.result = False
        self.current = math.acosh(float(format_txt.get()))
        self.display(self.current)
    def sinh(self):
        self.result = False
        self.current = math.sinh(float(format_txt.get()))
        self.display(self.current)
    def asinh(self):
        self.result = False
        self.current = math.asinh(float(format_txt.get()))
        self.display(self.current)
    def tanh(self):
        self.result = False
        self.current = math.tanh(float(format_txt.get()))
        self.display(self.current)
    def atanh(self):
        self.result = False
        self.current = math.atanh(float(format_txt.get()))
        self.display(self.current)
    def log10(self):
        self.result = False
        self.current = math.log10(float(format_txt.get()))
        self.display(self.current)
    
    def deg(self):
        self.result = False
        self.current = math.degrees(float(format_txt.get()))
        self.display(self.current)
    def exmp1(self):
        self.result = False
        self.current = math.expm1(float(format_txt.get()))
        self.display(self.current)
    def sqrt(self):
        self.result = False
        self.current = math.sqrt(float(format_txt.get()))
        self.display(self.current)
    
valeur_ajoutee = Calculatrice()

buttons = [
    ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), 
    ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), 
    ('1', 4, 0), ('2', 4, 1), ('3', 4, 2), 
]
i=0
for (text, row, column) in buttons:
    button = Button(calculatrice, text=text, font=('Arial', 14), bd=4,width=6)
    button.grid(row=row, column=column, sticky="nsew",ipadx=10,ipady=10)
    button.config(command=lambda x=buttons[i][0]: valeur_ajoutee.numberEnter(x))
    i+=1

b_effacer_tous = Button(calculatrice, text="CE", font=("arial",14), bg="#8A9797", foreground="blue", bd=4, width=6,command=valeur_ajoutee.clearAll).grid(row=1, column=0, pady=1, sticky="nsew", ipadx=10,ipady=10)
b_effacer = Button(calculatrice, text="C", font=("arial",14), bg="#8A9797", foreground="blue", bd=4, width=6, command=valeur_ajoutee.clear).grid(row=1, column=1, pady=1, sticky="nsew", ipadx=10,ipady=10)
b_sqrt = Button(calculatrice, text=chr(8730),font=("arial",14), bg="#8A9797", foreground="blue", bd=4, width=6, command= valeur_ajoutee.sqrt).grid(row=1, column=2, pady=1, sticky="nsew", ipadx=10,ipady=10)
b_plus = Button(calculatrice, text="+",font=("arial",14), bg="#8A9797", foreground="blue", bd=4, width=6, command=lambda: valeur_ajoutee.operateur("add")).grid(row=1, column=3, pady=1, sticky="nsew", ipadx=10,ipady=10)
b_sub = Button(calculatrice, text="-", font=("arial",14), bg="#8A9797", foreground="blue", bd=4, width=6, command=lambda: valeur_ajoutee.operateur("sub")).grid(row=2, column=3, pady=1, sticky="nsew", ipadx=10,ipady=10)
b_mul = Button(calculatrice, text="x", font=("arial",14), bg="#8A9797", foreground="blue", bd=4, width=6, command=lambda: valeur_ajoutee.operateur("mul")).grid(row=3, column=3, pady=1, sticky="nsew", ipadx=10,ipady=10)
b_div = Button(calculatrice, text="/", font=("arial",14), bg="#8A9797", foreground="blue", bd=4, width=6, command=lambda: valeur_ajoutee.operateur("div")).grid(row=4, column=3, pady=1, sticky="nsew", ipadx=10,ipady=10)
b_zero = Button(calculatrice, text="0", font=("arial",14), bg="#8A9797", bd=4, width=6, command= lambda: valeur_ajoutee.numberEnter(0)).grid(row=5, column=0, pady=1, sticky="nsew", ipadx=10,ipady=10)
b_point = Button(calculatrice, text=".", font=("arial",14), bg="#8A9797", bd=4, width=6, command= lambda: valeur_ajoutee.numberEnter(".")).grid(row=5, column=1, pady=1, sticky="nsew", ipadx=10,ipady=10)
b_eq = Button(calculatrice, text="=", font=("arial",14), bg="#8A9797", foreground="blue", bd=4, command=lambda: valeur_ajoutee.sum_of_total()).grid(row=5, column=2, columnspan=2, pady=1, sticky="nsew", ipadx=10,ipady=10)


b_pi = Button(calculatrice, text="π",font=("arial",14), bg="#8A9797", foreground="blue", width=6, bd=4, command= lambda: valeur_ajoutee.pi()).grid(row=1, column=4, pady=1, sticky="nsew", ipadx=10,ipady=10)
b_cos = Button(calculatrice, text="cos",font=("arial",14), bg="#8A9797", foreground="blue", width=6, bd=4, command=valeur_ajoutee.cos).grid(row=1, column=5, pady=1, sticky="nsew", ipadx=10,ipady=10)
b_sin = Button(calculatrice, text="sin",font=("arial",14), bg="#8A9797", foreground="blue", width=6, bd=4, command=valeur_ajoutee.sin).grid(row=1, column=6, pady=1, sticky="nsew", ipadx=10,ipady=10)
b_tan = Button(calculatrice, text="tan",font=("arial",14), bg="#8A9797", foreground="blue", width=6, bd=4, command=valeur_ajoutee.tan).grid(row=1, column=7, pady=1, sticky="nsew", ipadx=10,ipady=10)

b_2pi = Button(calculatrice, text="2π",font=("arial",14), bg="#8A9797", foreground="blue", width=6, bd=4, command= lambda: valeur_ajoutee.two_pi()).grid(row=2, column=4, pady=1, sticky="nsew", ipadx=10,ipady=10)
b_cosh = Button(calculatrice, text="cosh",font=("arial",14), bg="#8A9797", foreground="blue", width=6, bd=4, command=valeur_ajoutee.cosh).grid(row=2, column=5, pady=1, sticky="nsew", ipadx=10,ipady=10)
b_sinh = Button(calculatrice, text="sinh",font=("arial",14), bg="#8A9797", foreground="blue", width=6, bd=4, command=valeur_ajoutee.sinh).grid(row=2, column=6, pady=1, sticky="nsew", ipadx=10,ipady=10)
b_tanh = Button(calculatrice, text="tanh",font=("arial",14), bg="#8A9797", foreground="blue", width=6, bd=4, command=valeur_ajoutee.tanh).grid(row=2, column=7, pady=1, sticky="nsew", ipadx=10,ipady=10)

b_log = Button(calculatrice, text="log",font=("arial",14), bg="#8A9797", foreground="blue", width=6, bd=4, command=valeur_ajoutee.log).grid(row=3, column=4, pady=1, sticky="nsew", ipadx=10,ipady=10)
b_exp = Button(calculatrice, text="exp",font=("arial",14), bg="#8A9797", foreground="blue", width=6, bd=4, command=valeur_ajoutee.exp).grid(row=3, column=5, pady=1, sticky="nsew", ipadx=10,ipady=10)
b_modulo = Button(calculatrice, text="%",font=("arial",14), bg="#8A9797", foreground="blue", width=6, bd=4, command= lambda: valeur_ajoutee.operateur("mod")).grid(row=3, column=6, pady=1, sticky="nsew", ipadx=10,ipady=10)
b_e_cte = Button(calculatrice, text="e",font=("arial",14), bg="#8A9797", foreground="blue", width=6, bd=4, command=valeur_ajoutee.e).grid(row=3, column=7, pady=1, sticky="nsew", ipadx=10,ipady=10)

b_log2 = Button(calculatrice, text="log2",font=("arial",14), bg="#8A9797", foreground="blue", width=6, bd=4, command=valeur_ajoutee.log2).grid(row=4, column=4, pady=1, sticky="nsew", ipadx=10,ipady=10)
b_deg = Button(calculatrice, text="deg",font=("arial",14), bg="#8A9797", foreground="blue", width=6, bd=4, command=valeur_ajoutee.deg).grid(row=4, column=5, pady=1, sticky="nsew", ipadx=10,ipady=10)
b_acosh = Button(calculatrice, text="acosh",font=("arial",14), bg="#8A9797", foreground="blue", width=6, bd=4, command=valeur_ajoutee.acosh).grid(row=4, column=6, pady=1, sticky="nsew", ipadx=10,ipady=10)
b_asinh = Button(calculatrice, text="asinh",font=("arial",14), bg="#8A9797", foreground="blue", width=6, bd=4, command=valeur_ajoutee.asinh).grid(row=4, column=7, pady=1, sticky="nsew", ipadx=10,ipady=10)

b_log10 = Button(calculatrice, text="log10",font=("arial",14), bg="#8A9797", foreground="blue", width=6, bd=4, command=valeur_ajoutee.log10).grid(row=5, column=4, pady=1, sticky="nsew", ipadx=10,ipady=10)
b_log1p = Button(calculatrice, text="log1p",font=("arial",14), bg="#8A9797", foreground="blue", width=6, bd=4, command=valeur_ajoutee.log1p).grid(row=5, column=5, pady=1, sticky="nsew", ipadx=10,ipady=10)
b_exmp1 = Button(calculatrice, text="exmp1",font=("arial",14), bg="#8A9797", foreground="blue", width=6, bd=4, command=valeur_ajoutee.exmp1).grid(row=5, column=6, pady=1, sticky="nsew", ipadx=10,ipady=10)
b_lgamma = Button(calculatrice, text="lgamma",font=("arial",14), bg="#8A9797", foreground="blue", width=6, bd=4, command=valeur_ajoutee.lgamma).grid(row=5, column=7, pady=1, sticky="nsew", ipadx=10,ipady=10)


def quitter():
    quitter = messagebox.askyesno("calculatrice", "Etes vous sur de vouloir quitter?")
    if quitter:
        calcul.destroy()

def scientifique():
    calcul.resizable(width=False, height=False)
    calcul.geometry("800x410")
    format_txt.grid(row=0, column=0, columnspan=8, sticky="we", pady=(10,0),ipadx=10,ipady=10)

def standard():
    calcul.resizable(width=False, height=False)
    calcul.geometry("400x410")


menuu = Menu(calculatrice)
fichier_menuu = Menu(menuu, tearoff=0)
menuu.add_cascade(label="Fichier", menu=fichier_menuu)
fichier_menuu.add_command(label="Standard", command=standard) 
fichier_menuu.add_command(label="Scientifique", command=scientifique)
fichier_menuu.add_separator()
fichier_menuu.add_command(label="Quitter", command=quitter)

calcul.config(menu=menuu)  
calcul.mainloop()