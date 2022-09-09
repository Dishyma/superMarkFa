from tkinter import *
from tkinter import ttk


ventana = Tk()
ventana.geometry("1280x720")

ventana.title("SuperMarkFa")
label = Label(ventana, text = "SuperMarkFa", font="chaparral 36 italic", height=2).pack()

separator = ttk.Separator(ventana, orient='horizontal')
separator.pack(fill='x')

icon1 = PhotoImage(file = "img/checkout.png").subsample(4)
icon2 = PhotoImage(file = "img/password.png").subsample(4)
icon3 = PhotoImage(file = "img/coupons.png").subsample(4)
icon4 = PhotoImage(file = "img/personal.png").subsample(4)

btn1 = Button(ventana, text = 'Comprar', 
                    font="times 24 bold", 
                    width=300, 
                    height=200, 
                    borderwidth=1, 
                    relief="raised", 
                    image=icon1, 
                    compound="top").place(x=200 , y=150 )

btn2 = Button(ventana, text = 'Iniciar Sesion', 
                    font="times 24 bold", 
                    width=300, 
                    height=200,  
                    borderwidth=1, 
                    relief="raised",
                    image=icon2, 
                    compound="top").place(x=800 , y=150 )

btn3 = Button(ventana, text = 'Cupones', 
                    font="times 13 bold", 
                    width=300, 
                    height=200,
                    borderwidth=1, 
                    relief="raised",
                    image=icon3, 
                    compound="top").place(x=200 , y=450 )

btn4 = Button(ventana, text = 'Registrar', 
                    font="times 13 bold", 
                    width=300, 
                    height=200,
                    borderwidth=1, 
                    relief="raised", 
                    image=icon4, 
                    compound="top").place(x=800 , y=450 )

ventana.mainloop()