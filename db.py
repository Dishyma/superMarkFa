import mysql.connector

base = mysql.connector.connect(
    host="170.187.207.138",
    user ="dishyma",
    passwd = "Ca426391*",
    db='superMarkFa'
)
cursor = base.cursor()

def registrar(datosList):
    try:
        formula = "INSERT INTO users (name, lastName, email, birth, state) VALUES (%s, %s, %s, %s, %s)"
        datos = datosList
        cursor.execute(formula, datos)
        base.commit()
        base.close()
    except:
        print("Ese correo ya esta en uso")

def usuariosRepetidos(usuario):
        formula2 = "SELECT userName FROM usernames"
        cursor.execute(formula2)
        for i in cursor:
            print(type(i))
            if usuario == i:
                
    

usuariosRepetidos()