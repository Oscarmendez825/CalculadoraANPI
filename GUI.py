from tkinter import *
from tokenize import Number
import div_fact as d
import FuncionesTrigonometricas as f
import trigonometricasHiperbolicas as h
import re

ventana = Tk()
ventana.title("Calculadora ANPI")
ventana['bg'] = "#3f3f3f"


# FUNCIONES PARA LOS BOTONES


# Inserta el un numero en la entrada seleccionada
def set_input(value):
    name = str(ventana.focus_get()).split(".")[-1]
    if name == "x_input" or name == "y_input":
        ventana.focus_get().insert(END, value)
    else:
        x_entry.focus_set()
        ventana.focus_get().insert(END, value)
    return


# Limpia la entrada seleccionada
def clear_input(name):
    if name == "x":
        x_entry.delete(0, END)
    if name == "y":
        y_entry.delete(0, END)
    return


# Valida los valores de las entradas
def is_valid(entry):
    pattern = re.compile("^[+-]?([0-9]+([.][0-9]*)?|[.][0-9]+)?\s*(PI)*$")
    if pattern.match(entry) is not None and entry != "":
        return True
    return False


# Realiza la operacion y muestra el resultado
def operate(func):
    result_str = ""
    number_x = x_entry.get()
    number_y = y_entry.get()
    if not is_valid(number_x):
        result_str = "Error: Debe ingresar numeros o PI"
    if func == "logy" or func == "sqrty" or func == "x^y":
        if not is_valid(number_y):
            result_str = "Error: Debe ingresar numeros o PI"
    if result_str != "":
        result_entry.config(state="normal", fg="#ff8888")
        result_entry.delete(0, END)
        result_entry.insert(END, result_str)
        result_entry.config(state="readonly")
        return

    float_x = 0
    nx = re.findall("PI", number_x)
    if len(nx) > 0:
        number_x = number_x.replace("PI", "")
        number_x = number_x.replace(" ", "")
        if number_x == "-":
            float_x = -3.141592653589793**len(nx)
        elif number_x != "":
            float_x = float(number_x) * 3.141592653589793**len(nx)
        else:
            float_x = 3.141592653589793**len(nx)
    else:
        float_x = float(number_x)

    float_y = 0
    if func == "logy" or func == "sqrty" or func == "x^y":
        ny = re.findall("PI", number_y)
        if len(ny) > 0:
            number_y = number_y.replace("PI", "")
            number_y = number_y.replace(" ", "")
            if number_y == "-":
                float_y = -3.141592653589793**len(ny)
            elif number_y != "":
                float_y = float(number_y) * 3.141592653589793**len(ny)
            else:
                float_y = 3.141592653589793**len(ny)
        else:
            float_y = float(number_y)

    if func == "senh":
        result_str = str(h.sinh(float_x))
    elif func == "cosh":
        result_str = str(h.cosh(float_x))
    elif func == "tanh":
        result_str = str(h.tanh(float_x))
    elif func == "asen":
        result_str = str(d.asin_t(float_x))
    elif func == "acos":
        result_str = str(d.acos_t(float_x))
    elif func == "atan":
        result_str = str(d.atan_t(float_x))
    elif func == "sec":
        result_str = str(f.sec_t(float_x))
    elif func == "csc":
        result_str = str(f.csc_t(float_x))
    elif func == "cot":
        result_str = str(f.cot_t(float_x))
    elif func == "sen":
        result_str = str(f.sin_t(float_x))
    elif func == "cos":
        result_str = str(f.cos_t(float_x))
    elif func == "tan":
        result_str = str(f.tan_t(float_x))
    elif func == "ln":
        result_str = str(d.ln_t(float_x))
    elif func == "log10":
        result_str = str(d.log_t(float_x, 10))
    elif func == "logy":
        result_str = str(d.log_t(float_x, float_y))
    elif func == "1/x":
        result_str = str(d.div_t(float_x))
    elif func == "sqrt":
        result_str = str(h.sqrt_t(float_x))
    elif func == "sqrty":
        result_str = str(h.root_t(float_x, float_y))
    elif func == "exp":
        result_str = str(d.exp_t(float_x))
    elif func == "x^y":
        result_str = str(h.power_t(float_x, float_y))
    elif func == "x!":
        result_str = str(d.fact_t(float_x))

    result_entry.config(state="normal", fg="#efefef")
    if len(re.findall("Error", result_str)) > 0:
        result_entry.config(fg="#ff8888")
    result_entry.delete(0, END)
    result_entry.insert(END, result_str)
    result_entry.config(state="readonly")


# Abre la ventana de ayuda
def openHelp():
    ayuda = Toplevel(ventana)
    ayuda.title("Ayuda - Calculadora ANPI")
    ayuda["bg"] = "#3f3f3f"

    Label(ayuda, text="Calculadora ANPI", font="Arial 16 bold",
          bg="#3f3f3f", fg="#efefef").pack()
    Label(ayuda, text="Desarrollado por: ", font="Arial 10 italic",
          bg="#3f3f3f", fg="#efefef").pack()
    Label(ayuda, text="Brandon Gómez, Oscar Méndez & Simón Fallas", font="Arial 10 italic",
          bg="#3f3f3f", fg="#efefef").pack()

    Label(ayuda, text="""
Esta aplicación consiste en una calculadora de funciones 
trascendentes para un valor único. Se implementó utilizando
sucesiones que aproximan los valores de las funciones
que aparecen disponibles en la interfaz, por tanto, se debe tener
en cuenta que los resultados presentan un cierto grado de error.
""", font="Arial 11",
          bg="#3f3f3f", fg="#efefef", justify=LEFT, anchor="w").pack()
    Label(ayuda, text="Modo de Uso", font="Arial 12 bold",
          bg="#3f3f3f", fg="#efefef", justify=LEFT, anchor="w").pack()
    Label(ayuda, text="""Si se desea saber el valor de, por ejemplo, el factorial de 5,
se debe ingresar primero el valor al que se le desea aplicar la
función, en este caso sería 5. Se puede ingresar un valor con
los botones que se muestran en la interfaz, o utilizando el
teclado. Se debe tener en cuenta que solo se aceptan numeros
reales, o la constante PI. Los siguientes ejemplos muestran
el formato de algunas de las posibles entradas aceptadas:
4, -4, 4.1, -4.1, PI, 3PI, 3.2PI, -3.2PI, PIPI (pi cuadrado)

Continuando con el ejemplo, luego de ingresar el 5 en la
entrada X, se procede a presionar el boton x! para operar el
valor. El resultado de dicha operación se muestra en la sección
Resultado.
En el caso de que se quisiera aplicar una función que necesite
dos parámetros, como el logy(x), entonces se debe seleccionar
e ingresar un valor para la entrada Y, además del X.

En caso de que se ingrese algún valor que se encuentre fuera
del domino de la función, entonces se mostrará un mensaje de
error indicando cuales son los valores aceptados en la misma
sección donde se muestra el resultado.

Para borrar los valores de las entradas puede utilizar el
teclado o los botones "Limpiar" correspondientes. El resultado
se actualizará cada vez que se realice una operación nueva.
""", font="Arial 11",
          bg="#3f3f3f", fg="#efefef", anchor="w", justify=LEFT).pack()


# INPUT/OUTPUT
x_entry = Entry(ventana, name="x_input", font="Arial 12",
                bg="#3f3f3f", fg="#efefef", insertbackground="#efefef")
y_entry = Entry(ventana, name="y_input", font="Arial 12",
                bg="#3f3f3f", fg="#efefef", insertbackground="#efefef")
result_entry = Entry(ventana, text="", state="readonly",
                     font="Arial 12", readonlybackground="#3f3f3f", fg="#efefef")
x_label = Label(ventana, text="Valor X", font="Arial 12",
                bg="#3f3f3f", fg="#efefef")
y_label = Label(ventana, text="Valor Y", font="Arial 12",
                bg="#3f3f3f", fg="#efefef")
result_label = Label(ventana, text="Resultado",
                     font="Arial 12", bg="#3f3f3f", fg="#efefef")

x_entry.grid(row=0, column=1, columnspan=3, pady=5)
y_entry.grid(row=1, column=1, columnspan=3, pady=5)
result_entry.grid(row=2, column=1, columnspan=6, sticky="EW", pady=20)
x_label.grid(row=0, column=0, columnspan=1, pady=5)
y_label.grid(row=1, column=0, columnspan=1, pady=5)
result_label.grid(row=2, column=0, columnspan=1, pady=20)


# BOTONES

help_button = Button(ventana, text="Ayuda", bg="#4f4f4f", fg="#00bbff", relief=FLAT,
                     command=lambda: openHelp(), width=8, font="Arial 12 italic")
clear_x = Button(ventana, text="LImpiar", bg="#4f4f4f", fg="#efefef", relief=FLAT,
                 command=lambda: clear_input("x"), width=8, font="Arial 12")
clear_y = Button(ventana, text="Limpiar", bg="#4f4f4f", fg="#efefef", relief=FLAT,
                 command=lambda: clear_input("y"), width=8, font="Arial 12")

button1 = Button(ventana, text="1", bg="#4f4f4f", fg="#00ffff", relief=FLAT,
                 command=lambda: set_input("1"), width=8, height=2, font="Arial 12 bold")
button2 = Button(ventana, text="2", bg="#4f4f4f", fg="#00ffff", relief=FLAT,
                 command=lambda: set_input("2"), width=8, height=2, font="Arial 12 bold")
button3 = Button(ventana, text="3", bg="#4f4f4f", fg="#00ffff", relief=FLAT,
                 command=lambda: set_input("3"), width=8, height=2, font="Arial 12 bold")
button4 = Button(ventana, text="4", bg="#4f4f4f", fg="#00ffff", relief=FLAT,
                 command=lambda: set_input("4"), width=8, height=2, font="Arial 12 bold")
button5 = Button(ventana, text="5", bg="#4f4f4f", fg="#00ffff", relief=FLAT,
                 command=lambda: set_input("5"), width=8, height=2, font="Arial 12 bold")
button6 = Button(ventana, text="6", bg="#4f4f4f", fg="#00ffff", relief=FLAT,
                 command=lambda: set_input("6"), width=8, height=2, font="Arial 12 bold")
button7 = Button(ventana, text="7", bg="#4f4f4f", fg="#00ffff", relief=FLAT,
                 command=lambda: set_input("7"), width=8, height=2, font="Arial 12 bold")
button8 = Button(ventana, text="8", bg="#4f4f4f", fg="#00ffff", relief=FLAT,
                 command=lambda: set_input("8"), width=8, height=2, font="Arial 12 bold")
button9 = Button(ventana, text="9", bg="#4f4f4f", fg="#00ffff", relief=FLAT,
                 command=lambda: set_input("9"), width=8, height=2, font="Arial 12 bold")

button = Button(ventana, text=".", bg="#4f4f4f", fg="#00ffff", relief=FLAT,
                command=lambda: set_input("."), width=8, height=2, font="Arial 12 bold")
button0 = Button(ventana, text="0", bg="#4f4f4f", fg="#00ffff", relief=FLAT,
                 command=lambda: set_input("0"), width=8, height=2, font="Arial 12 bold")
buttonPi = Button(ventana, text="PI", bg="#4f4f4f", fg="#00ffff", relief=FLAT,
                  command=lambda: set_input("PI"), width=8, height=2, font="Arial 12 bold")


senh = Button(ventana, text="senh(x)", bg="#4f4f4f", fg="#00ff99", relief=FLAT,
              command=lambda: operate("senh"), width=8, height=2, font="Arial 12 italic")
cosh = Button(ventana, text="cosh(x)", bg="#4f4f4f", fg="#00ff99", relief=FLAT,
              command=lambda: operate("cosh"), width=8, height=2, font="Arial 12 italic")
tanh = Button(ventana, text="tanh(x)", bg="#4f4f4f", fg="#00ff99", relief=FLAT,
              command=lambda: operate("tanh"), width=8, height=2, font="Arial 12 italic")
asen = Button(ventana, text="asen(x)", bg="#4f4f4f", fg="#00ff99", relief=FLAT,
              command=lambda: operate("asen"), width=8, height=2, font="Arial 12 italic")
acos = Button(ventana, text="acos(x)", bg="#4f4f4f", fg="#00ff99", relief=FLAT,
              command=lambda: operate("acos"), width=8, height=2, font="Arial 12 italic")
atan = Button(ventana, text="atan(x)", bg="#4f4f4f", fg="#00ff99", relief=FLAT,
              command=lambda: operate("atan"), width=8, height=2, font="Arial 12 italic")
sec = Button(ventana, text="sec(x)", bg="#4f4f4f", fg="#00ff99", relief=FLAT,
             command=lambda: operate("sec"), width=8, height=2, font="Arial 12 italic")
csc = Button(ventana, text="csc(x)", bg="#4f4f4f", fg="#00ff99", relief=FLAT,
             command=lambda: operate("csc"), width=8, height=2, font="Arial 12 italic")
cot = Button(ventana, text="cot(x)", bg="#4f4f4f", fg="#00ff99", relief=FLAT,
             command=lambda: operate("cot"), width=8, height=2, font="Arial 12 italic")
sen = Button(ventana, text="sen(x)", bg="#4f4f4f", fg="#00ff99", relief=FLAT,
             command=lambda: operate("sen"), width=8, height=2, font="Arial 12 italic")
cos = Button(ventana, text="cos(x)", bg="#4f4f4f", fg="#00ff99", relief=FLAT,
             command=lambda: operate("cos"), width=8, height=2, font="Arial 12 italic")
tan = Button(ventana, text="tan(x)", bg="#4f4f4f", fg="#00ff99", relief=FLAT,
             command=lambda: operate("tan"), width=8, height=2, font="Arial 12 italic")
ln = Button(ventana, text="ln(x)", bg="#4f4f4f", fg="#00ff99", relief=FLAT,
            command=lambda: operate("ln"), width=8, height=2, font="Arial 12 italic")
log10 = Button(ventana, text="log10(x)", bg="#4f4f4f", fg="#00ff99", relief=FLAT,
               command=lambda: operate("log10"), width=8, height=2, font="Arial 12 italic")
logy = Button(ventana, text="logy(x)", bg="#4f4f4f", fg="#00ff99", relief=FLAT,
              command=lambda: operate("logy"), width=8, height=2, font="Arial 12 italic")
div = Button(ventana, text="1/x", bg="#4f4f4f", fg="#00ff99", relief=FLAT,
             command=lambda: operate("1/x"), width=8, height=2, font="Arial 12 italic")
sqrt = Button(ventana, text="sqrt(x)", bg="#4f4f4f", fg="#00ff99", relief=FLAT,
              command=lambda: operate("sqrt"), width=8, height=2, font="Arial 12 italic")
sqrty = Button(ventana, text="sqrty(x)", bg="#4f4f4f", fg="#00ff99", relief=FLAT,
               command=lambda: operate("sqrty"), width=8, height=2, font="Arial 12 italic")
exp = Button(ventana, text="exp(x)", bg="#4f4f4f", fg="#00ff99", relief=FLAT,
             command=lambda: operate("exp"), width=8, height=2, font="Arial 12 italic")
pot = Button(ventana, text="x^y", bg="#4f4f4f", fg="#00ff99", relief=FLAT,
             command=lambda: operate("x^y"), width=8, height=2, font="Arial 12 italic")
fact = Button(ventana, text="x!", bg="#4f4f4f", fg="#00ff99", relief=FLAT,
              command=lambda: operate("x!"), width=8, height=2, font="Arial 12 italic")

help_button.grid(row=0, column=6, columnspan=1, padx=5, pady=5)
clear_x.grid(row=0, column=4, columnspan=1, padx=5, pady=5)
clear_y.grid(row=1, column=4, columnspan=1, padx=5, pady=5)

senh.grid(row=3, column=0, columnspan=1, padx=5, pady=5)
cosh.grid(row=3, column=1, columnspan=1, padx=5, pady=5)
tanh.grid(row=3, column=2, columnspan=1, padx=5, pady=5)

asen.grid(row=4, column=0, columnspan=1, padx=5, pady=5)
acos.grid(row=4, column=1, columnspan=1, padx=5, pady=5)
atan.grid(row=4, column=2, columnspan=1, padx=5, pady=5)

sec.grid(row=5, column=0, columnspan=1, padx=5, pady=5)
csc.grid(row=5, column=1, columnspan=1, padx=5, pady=5)
cot.grid(row=5, column=2, columnspan=1, padx=5, pady=5)

sen.grid(row=6, column=0, columnspan=1, padx=5, pady=5)
cos.grid(row=6, column=1, columnspan=1, padx=5, pady=5)
tan.grid(row=6, column=2, columnspan=1, padx=5, pady=5)

ln.grid(row=7, column=0, columnspan=1, padx=5, pady=5)
log10.grid(row=7, column=1, columnspan=1, padx=5, pady=5)
logy.grid(row=7, column=2, columnspan=1, padx=5, pady=5)

div.grid(row=8, column=0, columnspan=1, padx=5, pady=5)
sqrt.grid(row=8, column=1, columnspan=1, padx=5, pady=5)
sqrty.grid(row=8, column=2, columnspan=1, padx=5, pady=5)

exp.grid(row=3, column=4, columnspan=1, padx=5, pady=5)
pot.grid(row=3, column=5, columnspan=1, padx=5, pady=5)
fact.grid(row=3, column=6, columnspan=1, padx=5, pady=5)

button7.grid(row=5, column=4, columnspan=1, padx=5, pady=5)
button8.grid(row=5, column=5, columnspan=1, padx=5, pady=5)
button9.grid(row=5, column=6, columnspan=1, padx=5, pady=5)

button4.grid(row=6, column=4, columnspan=1, padx=5, pady=5)
button5.grid(row=6, column=5, columnspan=1, padx=5, pady=5)
button6.grid(row=6, column=6, columnspan=1, padx=5, pady=5)

button1.grid(row=7, column=4, columnspan=1, padx=5, pady=5)
button2.grid(row=7, column=5, columnspan=1, padx=5, pady=5)
button3.grid(row=7, column=6, columnspan=1, padx=5, pady=5)

buttonPi.grid(row=8, column=4, columnspan=1, padx=5, pady=5)
button0.grid(row=8, column=5, columnspan=1, padx=5, pady=5)
button.grid(row=8, column=6, columnspan=1, padx=5, pady=5)


ventana.mainloop()
