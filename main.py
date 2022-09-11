from tkinter import *
from tkinter import ttk
from tkinter import messagebox


def atras(ventanaCerrar):
    ventanaCerrar.destroy()
    ventana.deiconify()

def salir(ventanaSalir):
    ventanaSalir.destroy()

def validarDatos(txtUsuario, txtConstrasena):
    usuario = txtUsuario
    contrasena = txtConstrasena
    if usuario == "":
        messagebox. showerror(title="Campos Obligatorios", message="Ingrese el usuario")
    elif contrasena == "":
        messagebox. showerror(title="Campos Obligatorios", message="Ingrese la contraseña")
    else:
        messagebox.showinfo(title="Excelente", message="Validando datos")

def comprar():
    ventanaCompra = Toplevel()
    ventanaCompra.geometry("1280x720")
    ventanaCompra.title("Comprando")

    lblCompra = Label(ventanaCompra, text="Añade los productos", font="times 36 bold", height=2).pack()

    separator2 = ttk.Separator(ventanaCompra, orient='horizontal')
    separator2.pack(fill='x')

def login():
    ventanaLogin = Toplevel()
    ventanaLogin.geometry("800x600")
    ventanaLogin.title("Iniciar Sesion")
    
    ventana.withdraw()
    
    logo = PhotoImage(file = "img/supermarket.png").subsample(6)
    lblLogo = Label(ventanaLogin, image=logo)
    lblLogo.image = logo
    lblLogo.pack()

    lblLogin = Label(ventanaLogin, text="Iniciar Sesion", font="times 36 bold", height=2)
    lblLogin.pack()
    
    separator2 = ttk.Separator(ventanaLogin, orient='horizontal')
    separator2.pack(fill=X)

    lblUsuario = ttk.Label(ventanaLogin, text="Nombre de Usuario")
    lblUsuario.pack()

    usuario = StringVar()
    usuario.set("Mateo")
    txtUsuario = ttk.Entry(ventanaLogin, textvariable=usuario, width=30)
    txtUsuario.pack()

    lblcontrasena = ttk.Label(ventanaLogin, text="Contraseña")
    lblcontrasena.pack()
    contrasena = StringVar()
    txtcontrasena = ttk.Entry(ventanaLogin, textvariable=contrasena, show="*", width=30)
    txtcontrasena.pack()
    
    logoEnter = PhotoImage(file= "img/enter.png").subsample(7,7)
    btn1 = Button(ventanaLogin, 
                        text = ' Iniciar Sesion',
                        font="times 11",  
                        borderwidth=1, 
                        relief="raised",
                        image=logoEnter, 
                        compound="left",
                        command= lambda: validarDatos(txtUsuario.get(), txtcontrasena.get())
                        )
    btn1.image_names= logoEnter
    btn1.pack(pady=20)

    btn2 = Button(ventanaLogin, 
                        text = 'Registrarme',
                        font = "times 11",  
                        borderwidth = 1, 
                        relief ="raised",
                        command = lambda : [salir(ventanaLogin), registrar()]
                        )
    btn2.pack(pady=20)

    btn3 = Button(ventanaLogin, 
                        text = 'Atras',
                        font="times 11",
                        borderwidth=1, 
                        relief="raised",
                        command=lambda: atras(ventanaLogin)
                        )
    btn3.pack(pady=20)

def cupones():
    ventanaCupones = Toplevel()
    ventanaCupones.geometry("1280x720")
    ventanaCupones.title("Iniciar Sesion")

    lblCupones = Label(ventanaCupones, text="Cupones", font="times 36 bold", height=2).pack()

    separator2 = ttk.Separator(ventanaCupones, orient='horizontal')
    separator2.pack(fill='x')

def registrar():
    ventanaRegistrar = Toplevel()
    ventanaRegistrar.geometry("1280x720")
    ventanaRegistrar.title("Iniciar Sesion")

    lblRegistrar = Label(ventanaRegistrar, text="Registrar", font="times 36 bold", height=2).pack()

    separator2 = ttk.Separator(ventanaRegistrar, orient='horizontal')
    separator2.pack(fill='x')

    btn3 = Button(ventanaRegistrar, 
                        text = 'Atras',
                        font="times 11",
                        borderwidth=1, 
                        relief="raised",
                        command=lambda: atras(ventanaRegistrar)
                        )
    btn3.pack(pady=20)

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
                    compound="top",
                    command=comprar).place(x=200 , y=150 )

btn2 = Button(ventana, text = 'Iniciar Sesion', 
                    font="times 24 bold", 
                    width=300, 
                    height=200,  
                    borderwidth=1, 
                    relief="raised",
                    image=icon2, 
                    compound="top",
                    command=login).place(x=800 , y=150 )

btn3 = Button(ventana, text = 'Cupones', 
                    font="times 13 bold", 
                    width=300, 
                    height=200,
                    borderwidth=1, 
                    relief="raised",
                    image=icon3, 
                    compound="top",
                    command=cupones).place(x=200 , y=450 )

btn4 = Button(ventana, text = 'Registrar', 
                    font="times 13 bold", 
                    width=300, 
                    height=200,
                    borderwidth=1, 
                    relief="raised", 
                    image=icon4, 
                    compound="top",
                    command=registrar).place(x=800 , y=450 )

btn5 = Button(ventana, text = 'Salir', 
                    font="times 13 bold",
                    borderwidth=1, 
                    relief="raised", 
                    command=lambda: salir(ventana))
btn5.pack(side="bottom")

ventana.mainloop()