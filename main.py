from tkinter import *
from tkinter import ttk
from turtle import left


ventana = Tk()
ventana.geometry("1280x720")

helv36 = ("Chaparral Pro", 36, "bold")
ventana.title("SuperMarkFa")
label = Label(ventana, text = "SuperMarkFa", font=helv36, height=2).pack()

separator = ttk.Separator(ventana, orient='horizontal')
separator.pack(fill='x')

btn1 = Button(ventana, text = 'boton 1', width=40, height=10).place(x=200 , y=150 )
btn2 = Button(ventana, text = 'boton 2', width=40, height=10).place(x=800 , y=150 )
btn3 = Button(ventana, text = 'boton 3', width=40, height=10).place(x=200 , y=450 )
btn4 = Button(ventana, text = 'boton 4', width=40, height=10).place(x=800 , y=450 )

ventana.mainloop()