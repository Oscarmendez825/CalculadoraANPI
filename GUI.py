from tkinter import *

ventana = Tk()
ventana.title("Calculadora ANPI")

x_entry = Entry(ventana, font="Arial 12")
y_entry = Entry(ventana, font="Arial 12")
x_entry.grid(row=0, column=0, columnspan=4, padx=10, pady=5)
y_entry.grid(row=1, column=0, columnspan=4, padx=10, pady=5)

#BOTONES

button1 = Button(ventana, text="1", width=5, height=2)
button2 = Button(ventana, text="2", width=5, height=2)
button3 = Button(ventana, text="3", width=5, height=2)
button4 = Button(ventana, text="4", width=5, height=2)
button5 = Button(ventana, text="5", width=5, height=2)
button6 = Button(ventana, text="6", width=5, height=2)
button7 = Button(ventana, text="7", width=5, height=2)
button8 = Button(ventana, text="8", width=5, height=2)
button9 = Button(ventana, text="9", width=5, height=2)

button = Button(ventana, text=".", width=5, height=2)
button0 = Button(ventana, text="0", width=5, height=2)
buttonPi = Button(ventana, text="pi", width=5, height=2)

senh = Button(ventana, text="senh(x)", width=5, height=2)
cosh = Button(ventana, text="cosh(x)", width=5, height=2)
tanh = Button(ventana, text="tanh(x)", width=5, height=2)
asen = Button(ventana, text="asen(x)", width=5, height=2)
acos = Button(ventana, text="acos(x)", width=5, height=2)
atan = Button(ventana, text="atan(x)", width=5, height=2)
sec = Button(ventana, text="sec(x)", width=5, height=2)
csc = Button(ventana, text="csc(x)", width=5, height=2)
cot = Button(ventana, text="cot(x)", width=5, height=2)
sen = Button(ventana, text="sen(x)", width=5, height=2)
cos = Button(ventana, text="cos(x)", width=5, height=2)
tan = Button(ventana, text="tan(x)", width=5, height=2)
ln = Button(ventana, text="ln(x)", width=5, height=2)
log10 = Button(ventana, text="log10(x)", width=5, height=2)
logy = Button(ventana, text="logy(x)", width=5, height=2)
div = Button(ventana, text="1/x", width=5, height=2)
sqrt = Button(ventana, text="sqrt(x)", width=5, height=2)
sqrty = Button(ventana, text="sqrty(x)", width=5, height=2)
exp = Button(ventana, text="exp(x)", width=5, height=2)
pot = Button(ventana, text="x^y", width=5, height=2)
fact = Button(ventana, text="x!", width=5, height=2)

senh.grid(row=2, column=0, columnspan=1, padx=10, pady=5)
cosh.grid(row=2, column=1, columnspan=1, padx=10, pady=5)
tanh.grid(row=2, column=2, columnspan=1, padx=10, pady=5)

asen.grid(row=3, column=0, columnspan=1, padx=10, pady=5)
acos.grid(row=3, column=1, columnspan=1, padx=10, pady=5)
atan.grid(row=3, column=2, columnspan=1, padx=10, pady=5)

sec.grid(row=4, column=0, columnspan=1, padx=10, pady=5)
csc.grid(row=4, column=1, columnspan=1, padx=10, pady=5)
cot.grid(row=4, column=2, columnspan=1, padx=10, pady=5)

sen.grid(row=5, column=0, columnspan=1, padx=10, pady=5)
cos.grid(row=5, column=1, columnspan=1, padx=10, pady=5)
tan.grid(row=5, column=2, columnspan=1, padx=10, pady=5)

ln.grid(row=6, column=0, columnspan=1, padx=10, pady=5)
log10.grid(row=6, column=1, columnspan=1, padx=10, pady=5)
logy.grid(row=6, column=2, columnspan=1, padx=10, pady=5)

div.grid(row=7, column=0, columnspan=1, padx=10, pady=5)
sqrt.grid(row=7, column=1, columnspan=1, padx=10, pady=5)
sqrty.grid(row=7, column=2, columnspan=1, padx=10, pady=5)

exp.grid(row=8, column=0, columnspan=1, padx=10, pady=5)
pot.grid(row=8, column=1, columnspan=1, padx=10, pady=5)
fact.grid(row=8, column=2, columnspan=1, padx=10, pady=5)

button7.grid(row=9, column=0, columnspan=1, padx=10, pady=5)
button8.grid(row=9, column=1, columnspan=1, padx=10, pady=5)
button9.grid(row=9, column=2, columnspan=1, padx=10, pady=5)

button4.grid(row=10, column=0, columnspan=1, padx=10, pady=5)
button5.grid(row=10, column=1, columnspan=1, padx=10, pady=5)
button6.grid(row=10, column=2, columnspan=1, padx=10, pady=5)

button1.grid(row=11, column=0, columnspan=1, padx=10, pady=5)
button2.grid(row=11, column=1, columnspan=1, padx=10, pady=5)
button3.grid(row=11, column=2, columnspan=1, padx=10, pady=5)

buttonPi.grid(row=12, column=0, columnspan=1, padx=10, pady=5)
button0.grid(row=12, column=1, columnspan=1, padx=10, pady=5)
button.grid(row=12, column=2, columnspan=1, padx=10, pady=5)


ventana.mainloop()