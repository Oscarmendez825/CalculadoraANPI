from tkinter import *
from tokenize import Number
import div_fact as d
import FuncionesTrigonometricas as f
import trigonometricasHiperbolicas as h

ventana = Tk()
ventana.title("Calculadora ANPI")


# FUNCIONES PARA LOS BOTONES


# Inserta el un numero en la entrada seleccionada
def set_input(value):
    name = str(ventana.focus_get()).split(".")[-1]
    if name == "x_input" or name == "y_input":
        ventana.focus_get().insert(END, value)
    return


# Limpia la entrada seleccionada
def clear_input(name):
    if name == "x":
        x_entry.delete(0, END)
    if name == "y":
        y_entry.delete(0, END)
    return


# Realiza la operacion y muestra el resultado
def operate(func):
    result = ""
    if func == "senh":
        result = str(h.sinh(float(x_entry.get())))
    elif func == "cosh":
        result = str(h.cosh(float(x_entry.get())))
    elif func == "tanh":
        result = str(h.tanh(float(x_entry.get())))
    elif func == "asen":
        result = str(d.asin_t(float(x_entry.get())))
    elif func == "acos":
        result = str(d.acos_t(float(x_entry.get())))
    elif func == "atan":
        result = str(d.atan_t(float(x_entry.get())))
    elif func == "sec":
        result = str(f.sec_t(float(x_entry.get())))
    elif func == "csc":
        result = str(f.csc_t(float(x_entry.get())))
    elif func == "cot":
        result = str(f.cot_t(float(x_entry.get())))
    elif func == "sen":
        result = str(f.sin_t(float(x_entry.get())))
    elif func == "cos":
        result = str(f.cos_t(float(x_entry.get())))
    elif func == "tan":
        result = str(f.tan_t(float(x_entry.get())))
    elif func == "ln":
        result = str(d.ln_t(float(x_entry.get())))
    elif func == "log10":
        result = str(d.log_t(float(x_entry.get()), 10))
    elif func == "logy":
        result = str(d.log_t(float(x_entry.get()), float(y_entry.get())))
    elif func == "1/x":
        result = str(d.div_t(float(x_entry.get())))
    elif func == "sqrt":
        result = str(h.sqrt_t(float(x_entry.get())))
    elif func == "sqrty":
        result = str(h.root_t(float(x_entry.get()), float(y_entry.get())))
    elif func == "exp":
        result = str(d.exp_t(float(x_entry.get())))
    elif func == "x^y":
        result = str(h.power_t(float(x_entry.get()), float(y_entry.get())))
    elif func == "x!":
        result = str(d.fact_t(float(x_entry.get())))

    result_entry.config(state="normal")
    result_entry.delete(0, END)
    result_entry.insert(END, result)
    result_entry.config(state="readonly")


# INPUT/OUTPUT
x_entry = Entry(ventana, name="x_input", font="Arial 12")
y_entry = Entry(ventana, name="y_input", font="Arial 12")
result_entry = Entry(ventana, font="Arial 12", state="readonly")
x_label = Label(ventana, text="X", font="Arial 12")
y_label = Label(ventana, text="Y", font="Arial 12")
result_label = Label(ventana, text="Result", font="Arial 12")

x_entry.grid(row=0, column=1, columnspan=3, padx=10, pady=5)
y_entry.grid(row=1, column=1, columnspan=3, padx=10, pady=5)
result_entry.grid(row=2, column=1, columnspan=3, padx=10, pady=5)
x_label.grid(row=0, column=0, columnspan=1, padx=10, pady=5)
y_label.grid(row=1, column=0, columnspan=1, padx=10, pady=5)
result_label.grid(row=2, column=0, columnspan=1, padx=10, pady=5)


# BOTONES

help_button = Button(ventana, text="Help", width=5, height=2)
clear_x = Button(ventana, text="Clear",
                 command=lambda: clear_input("x"), width=5, height=2)
clear_y = Button(ventana, text="Clear",
                 command=lambda: clear_input("y"), width=5, height=2)

button1 = Button(ventana, text="1",
                 command=lambda: set_input("1"), width=5, height=2)
button2 = Button(ventana, text="2",
                 command=lambda: set_input("2"), width=5, height=2)
button3 = Button(ventana, text="3",
                 command=lambda: set_input("3"), width=5, height=2)
button4 = Button(ventana, text="4",
                 command=lambda: set_input("4"), width=5, height=2)
button5 = Button(ventana, text="5",
                 command=lambda: set_input("5"), width=5, height=2)
button6 = Button(ventana, text="6",
                 command=lambda: set_input("6"), width=5, height=2)
button7 = Button(ventana, text="7",
                 command=lambda: set_input("7"), width=5, height=2)
button8 = Button(ventana, text="8",
                 command=lambda: set_input("8"), width=5, height=2)
button9 = Button(ventana, text="9",
                 command=lambda: set_input("9"), width=5, height=2)

button = Button(ventana, text=".",
                command=lambda: set_input("."), width=5, height=2)
button0 = Button(ventana, text="0",
                 command=lambda: set_input("0"), width=5, height=2)
buttonPi = Button(ventana, text="PI",
                  command=lambda: set_input("3.141592653589793"), width=5, height=2)


senh = Button(ventana, text="senh(x)",
              command=lambda: operate("senh"), width=5, height=2)
cosh = Button(ventana, text="cosh(x)",
              command=lambda: operate("cosh"), width=5, height=2)
tanh = Button(ventana, text="tanh(x)",
              command=lambda: operate("tanh"), width=5, height=2)
asen = Button(ventana, text="asen(x)",
              command=lambda: operate("asen"), width=5, height=2)
acos = Button(ventana, text="acos(x)",
              command=lambda: operate("acos"), width=5, height=2)
atan = Button(ventana, text="atan(x)",
              command=lambda: operate("atan"), width=5, height=2)
sec = Button(ventana, text="sec(x)",
             command=lambda: operate("sec"), width=5, height=2)
csc = Button(ventana, text="csc(x)",
             command=lambda: operate("csc"), width=5, height=2)
cot = Button(ventana, text="cot(x)",
             command=lambda: operate("cot"), width=5, height=2)
sen = Button(ventana, text="sen(x)",
             command=lambda: operate("sen"), width=5, height=2)
cos = Button(ventana, text="cos(x)",
             command=lambda: operate("cos"), width=5, height=2)
tan = Button(ventana, text="tan(x)",
             command=lambda: operate("tan"), width=5, height=2)
ln = Button(ventana, text="ln(x)",
            command=lambda: operate("ln"), width=5, height=2)
log10 = Button(ventana, text="log10(x)",
               command=lambda: operate("log10"), width=5, height=2)
logy = Button(ventana, text="logy(x)",
              command=lambda: operate("logy"), width=5, height=2)
div = Button(ventana, text="1/x",
             command=lambda: operate("1/x"), width=5, height=2)
sqrt = Button(ventana, text="sqrt(x)",
              command=lambda: operate("sqrt"), width=5, height=2)
sqrty = Button(ventana, text="sqrty(x)",
               command=lambda: operate("sqrty"), width=5, height=2)
exp = Button(ventana, text="exp(x)",
             command=lambda: operate("exp"), width=5, height=2)
pot = Button(ventana, text="x^y",
             command=lambda: operate("x^y"), width=5, height=2)
fact = Button(ventana, text="x!",
              command=lambda: operate("x!"), width=5, height=2)

help_button.grid(row=0, column=6, columnspan=1, padx=10, pady=5)
clear_x.grid(row=0, column=4, columnspan=1, padx=10, pady=5)
clear_y.grid(row=1, column=4, columnspan=1, padx=10, pady=5)

senh.grid(row=3, column=0, columnspan=1, padx=10, pady=5)
cosh.grid(row=3, column=1, columnspan=1, padx=10, pady=5)
tanh.grid(row=3, column=2, columnspan=1, padx=10, pady=5)

asen.grid(row=4, column=0, columnspan=1, padx=10, pady=5)
acos.grid(row=4, column=1, columnspan=1, padx=10, pady=5)
atan.grid(row=4, column=2, columnspan=1, padx=10, pady=5)

sec.grid(row=5, column=0, columnspan=1, padx=10, pady=5)
csc.grid(row=5, column=1, columnspan=1, padx=10, pady=5)
cot.grid(row=5, column=2, columnspan=1, padx=10, pady=5)

sen.grid(row=6, column=0, columnspan=1, padx=10, pady=5)
cos.grid(row=6, column=1, columnspan=1, padx=10, pady=5)
tan.grid(row=6, column=2, columnspan=1, padx=10, pady=5)

ln.grid(row=7, column=0, columnspan=1, padx=10, pady=5)
log10.grid(row=7, column=1, columnspan=1, padx=10, pady=5)
logy.grid(row=7, column=2, columnspan=1, padx=10, pady=5)

div.grid(row=2, column=4, columnspan=1, padx=10, pady=5)
sqrt.grid(row=2, column=5, columnspan=1, padx=10, pady=5)
sqrty.grid(row=2, column=6, columnspan=1, padx=10, pady=5)

exp.grid(row=3, column=4, columnspan=1, padx=10, pady=5)
pot.grid(row=3, column=5, columnspan=1, padx=10, pady=5)
fact.grid(row=3, column=6, columnspan=1, padx=10, pady=5)

button7.grid(row=4, column=4, columnspan=1, padx=10, pady=5)
button8.grid(row=4, column=5, columnspan=1, padx=10, pady=5)
button9.grid(row=4, column=6, columnspan=1, padx=10, pady=5)

button4.grid(row=5, column=4, columnspan=1, padx=10, pady=5)
button5.grid(row=5, column=5, columnspan=1, padx=10, pady=5)
button6.grid(row=5, column=6, columnspan=1, padx=10, pady=5)

button1.grid(row=6, column=4, columnspan=1, padx=10, pady=5)
button2.grid(row=6, column=5, columnspan=1, padx=10, pady=5)
button3.grid(row=6, column=6, columnspan=1, padx=10, pady=5)

buttonPi.grid(row=7, column=4, columnspan=1, padx=10, pady=5)
button0.grid(row=7, column=5, columnspan=1, padx=10, pady=5)
button.grid(row=7, column=6, columnspan=1, padx=10, pady=5)


ventana.mainloop()
