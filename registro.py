

import tkinter 
from tkinter import *
from tkinter import messagebox
import sqlite3




def menu_pantalla():
    
    global pantalla
    pantalla = Tk()
    pantalla.geometry("300x500")
    pantalla.title("Bienvenido")
    pantalla.iconbitmap("tornillo.ico")

    image=PhotoImage(file='tornillo.gif')
    image=image.subsample(2,2)
    label=Label(image=image)
    label.pack()

    Label(text="Acceso al Sistema",bg="navy", fg="white",width="300",height="3",font=("calibri",15)).pack()
    Label(text="").pack()

    Button(text="Iniciar Sesion" , height="3" , width="30",command=inicio_sesion).pack()
    Label(text="").pack()
    Button(text="Registrar",height="3",width="30",command=registrar).pack()

    pantalla.mainloop()

def inicio_sesion():
    global pantalla1
    pantalla1= Toplevel(pantalla)
    pantalla1.geometry("400x250")
    pantalla1.title("Inicio de Sesion")
    pantalla1.iconbitmap("tornillo.ico")
    
    Label(pantalla1,text="Por favor ingrese su usuario y contraseña",bg="navy", fg="white",width="300",height="3",font=("calibri",15)).pack()
    Label(pantalla1,text="").pack
    
    global nombreusuario_verify
    global contraseñausuario_verify
    
    nombreusuario_verify=StringVar()
    contraseñausuario_verify=StringVar()
    
    global nombre_usuario_entry
    global contraseña_usuario_entry
    
    Label(pantalla1,text="Usuario").pack()
    nombre_usuario_entry=Entry(pantalla1,textvariable=nombreusuario_verify)
    nombre_usuario_entry.pack()
    Label(pantalla1).pack()
    
    Label(pantalla1,text="Contraseña").pack()
    contraseña_usuario_entry=Entry(pantalla1,textvariable=contraseñausuario_verify,show="*")
    contraseña_usuario_entry.pack()
    Label(pantalla1).pack()
    
    Button(pantalla1,text="Iniciar sesion",command=validar_datos).pack()
    
def registrar():
    global pantalla2
    pantalla2= Toplevel(pantalla)  
    pantalla2.geometry("450x500")
    pantalla2.title("Registro")
    pantalla2.iconbitmap("tornillo.ico")
    
    global nombreusuario_entry
    global contraseña_entry
    global recom_entry

    
    nombreusuario_entry=StringVar()
    contraseña_entry=StringVar()
    recom_entry=IntVar()

    
    Label(pantalla2, text="Por favor ingrese un usuario y contraseña",bg="navy", fg="white",width="300",height="3",font=("calibri",15)).pack()
    Label(pantalla2,text="").pack
    
    Label(pantalla2,text="Usuario").pack()
    nombreusuario_entry=Entry(pantalla2)
    nombreusuario_entry.pack()
    Label(pantalla2).pack()
    
    Label(pantalla2,text="Contraseña").pack()
    contraseña_entry=Entry(pantalla2,show="*")
    contraseña_entry.pack()
    Label(pantalla2).pack()
    
    Label(pantalla2, text="Por favor selecione una categorias de su interes",bg="navy", fg="white",width="300",height="3",font=("calibri",15)).pack()
    Label(pantalla2,text="").pack
    
    Radiobutton(pantalla2,variable=recom_entry,text="Herramientas",value=1).pack()
    Radiobutton(pantalla2,variable=recom_entry,text="Pintura",value=2).pack()
    Radiobutton(pantalla2,variable=recom_entry,text="Construccion",value=3).pack()
    Radiobutton(pantalla2,variable=recom_entry,text="Todo",value=4).pack()
    
    
    Button(pantalla2,text="Registrar",command=inserta_datos).pack()

def inserta_datos():
    print(recom_entry.get())
    conexion=sqlite3.connect("rufo_db.db")
    if (recom_entry.get()==1):
        conexion.execute("INSERT INTO User(user,password,recommended) values(?,?,?)",(nombreusuario_entry.get(),contraseña_entry.get(),"herramientas"))
        conexion.commit()
        conexion.close 
    elif (recom_entry.get()==2):
        conexion.execute("INSERT INTO User(user,password,recommended) values(?,?,?)",(nombreusuario_entry.get(),contraseña_entry.get(),"pintura"))
        conexion.commit()
        conexion.close 
    elif (recom_entry.get()==3):
        conexion.execute("INSERT INTO User(user,password,recommended) values(?,?,?)",(nombreusuario_entry.get(),contraseña_entry.get(),"construccion"))
        conexion.commit()
        conexion.close 
    elif (recom_entry.get()==4):
        conexion.execute("INSERT INTO User(user,password,recommended) values(?,?,?)",(nombreusuario_entry.get(),contraseña_entry.get(),"todo"))
        conexion.commit()
        conexion.close    
    messagebox.showinfo(message="Registro exitoso",title="Aviso")
        
def validar_datos():
    conexion=sqlite3.connect("rufo_db.db")
    fcursor= conexion.cursor()
    
    usuario= nombreusuario_verify.get()
    passwd= contraseñausuario_verify.get()
    
    fcursor.execute('SELECT * FROM User WHERE user = ? AND password=?',(usuario,passwd))
    
    if(fcursor.fetchall()):
        messagebox.showinfo(title="Login exitoso",message="Sesion iniciada correctamenta")
        
        
    else:
        messagebox.showinfo(title="Ups, algo ha salido mal",message="Usuario o contraseña incorrectos")
    
    fcursor.close(
        
    )
    pantalla_principal()
    

def pantalla_principal():
    
    global pantalla_pr
     
    pantalla_pr= Tk()
    pantalla_pr.geometry("700x500")
    pantalla_pr.title("Tornillo Feliz")
    pantalla_pr.iconbitmap("tornillo.ico")
    
    
    Label(pantalla_pr, text="Ferreteria El Tornillo Feliz",bg="navy", fg="white",width="300",height="3",font=("calibri",15)).pack()
    Label(pantalla_pr,text="").pack()
    
    recomendados()
    
    
def recomendados():
    conexion=sqlite3.connect("rufo_db.db")
    fcursor= conexion.cursor()
    
    usuario= nombreusuario_verify.get()
    passwd= contraseñausuario_verify.get()
    recm=""
   
    
    fcursor.execute('SELECT * FROM User WHERE user = ? AND password=?',(usuario,passwd))
    for fila in fcursor:
        recm=fila[3]
        
    
    if recm=="herramientas":
           
        h1= Label(pantalla_pr,text="Alicate",bg="lightblue")
        h1.place(x=100,y=85) 
        b1=Button(pantalla_pr,text="S/:15",command=vA)    
        b1.place(x=102,y=110)     
        
        h2=Label(pantalla_pr,text="Desarmador",bg="lightblue")
        h2.place(x=300,y=85)
        b2=Button(pantalla_pr,text="S/:10",command=vD)    
        b2.place(x=302,y=110)     
        
        h3=Label(pantalla_pr,text="Llave inglesa",bg="lightblue")
        h3.place(x=500,y=85)
        b3=Button(pantalla_pr,text="S/:17",command=vL)    
        b3.place(x=502,y=110)
        
        bot=Button(pantalla_pr,text="Hablar con el asistente",command=bot_conf)
        bot.place(x=302,y=300)     
        
        
    elif recm=="pintura":
        h1= Label(pantalla_pr,text="Cpp-Rojo",bg="lightblue")
        h1.place(x=100,y=85) 
        b1=Button(pantalla_pr,text="S/:45",command=vpC)    
        b1.place(x=102,y=110)     
        
        h2=Label(pantalla_pr,text="Patito-Rojo",bg="lightblue")
        h2.place(x=300,y=85)
        b2=Button(pantalla_pr,text="S/:30",command=vpP)    
        b2.place(x=302,y=110)     
        
        h3=Label(pantalla_pr,text="Brocha",bg="lightblue")
        h3.place(x=500,y=85)
        b3=Button(pantalla_pr,text="S/:12",command=vB)    
        b3.place(x=502,y=110) 
        
        bot=Button(pantalla_pr,text="Hablar con el asistente",command=bot_conf)
        bot.place(x=302,y=300)       
    elif recm=="construccion":
        h1= Label(pantalla_pr,text="Cemento",bg="lightblue")
        h1.place(x=100,y=85) 
        b1=Button(pantalla_pr,text="S/:25",command=vC)    
        b1.place(x=102,y=110)     
        
        h2=Label(pantalla_pr,text="Fierro",bg="lightblue")
        h2.place(x=300,y=85)
        b2=Button(pantalla_pr,text="S/:10",command=vF)    
        b2.place(x=302,y=110)     
        
        h3=Label(pantalla_pr,text="Carretilla",bg="lightblue")
        h3.place(x=500,y=85)
        b3=Button(pantalla_pr,text="S/:85",command=vCa)    
        b3.place(x=502,y=110)  
        
        bot=Button(pantalla_pr,text="Hablar con el asistente",command=bot_conf)
        bot.place(x=302,y=300)      
        
    elif recm=="todo":
        h1= Label(pantalla_pr,text="Alicate",bg="lightblue")
        h1.place(x=100,y=85)          
        h2=Label(pantalla_pr,text="Desarmador",bg="lightblue")
        h2.place(x=300,y=85)
        h3=Label(pantalla_pr,text="Llave inglesa",bg="lightblue")
        h3.place(x=500,y=85)
    conexion.close()
def vA():
    conexion=sqlite3.connect("rufo_db.db")
    usuario= nombreusuario_verify.get()
    conexion.execute("INSERT INTO venta(usuario,producto,precio) values(?,?,?)",(usuario,"alicate",15))
    conexion.commit()
    conexion.close 
def vD():
    conexion=sqlite3.connect("rufo_db.db")
    usuario= nombreusuario_verify.get()
    conexion.execute("INSERT INTO venta(usuario,producto,precio) values(?,?,?)",(usuario,"Desarmador",10))
    conexion.commit()
    conexion.close 
def vL():
    conexion=sqlite3.connect("rufo_db.db")
    usuario= nombreusuario_verify.get()
    conexion.execute("INSERT INTO venta(usuario,producto,precio) values(?,?,?)",(usuario,"Llave inglesa",17))
    conexion.commit()
    conexion.close 
def vpC():
    conexion=sqlite3.connect("rufo_db.db")
    usuario= nombreusuario_verify.get()
    conexion.execute("INSERT INTO venta(usuario,producto,precio) values(?,?,?)",(usuario,"PinturaCPP",45))
    conexion.commit()
    conexion.close 
def vpP():
    conexion=sqlite3.connect("rufo_db.db")
    usuario= nombreusuario_verify.get()
    conexion.execute("INSERT INTO venta(usuario,producto,precio) values(?,?,?)",(usuario,"PinturaPatito",30))
    conexion.commit()
    conexion.close 
def vB():
    conexion=sqlite3.connect("rufo_db.db")
    usuario= nombreusuario_verify.get()
    conexion.execute("INSERT INTO venta(usuario,producto,precio) values(?,?,?)",(usuario,"Brocha",12))
    conexion.commit()
    conexion.close 
def vC():
    conexion=sqlite3.connect("rufo_db.db")
    usuario= nombreusuario_verify.get()
    conexion.execute("INSERT INTO venta(usuario,producto,precio) values(?,?,?)",(usuario,"Cemento",25))
    conexion.commit()
    conexion.close 
def vF():
    conexion=sqlite3.connect("rufo_db.db")
    usuario= nombreusuario_verify.get()
    conexion.execute("INSERT INTO venta(usuario,producto,precio) values(?,?,?)",(usuario,"Fierro",10))
    conexion.commit()
    conexion.close 
def vCa():
    conexion=sqlite3.connect("rufo_db.db")
    usuario= nombreusuario_verify.get()
    conexion.execute("INSERT INTO venta(usuario,producto,precio) values(?,?,?)",(usuario,"Carretilla",85))
    conexion.commit()
    conexion.close 
    

def bot_conf():
   
    global bot
    global ctex


    
    bot= Toplevel(pantalla_pr)  
    bot.geometry("500x600")
    bot.title("TornilloBot")
    bot.iconbitmap("tornillo.ico")

    Label(bot, text="Tornillo bot",bg="navy", fg="white",width="300",height="3",font=("calibri",15)).pack()
    Label(bot,text="").pack()
    ctex=Text(bot)
    ctex.pack()
    ctex.insert(END,"\n"+"TornilloBot: Hola "+nombreusuario_verify.get()+" soy tornillo bot. ¿En que le puedo ayudar?")
    
    op1=Button(bot,text="Contacto",command=ayuda1).pack()
    op2=Button(bot,text="Mi compra",command=ayuda2).pack()
    op3=Button(bot,text="Productos",command=ayuda3).pack()
    op4=Button(bot,text="Ubicacion",command=ayuda4).pack()
def ayuda1():
    ctex.insert(END,"\n"+"TornilloBot dice: El numero de um empleado es: 987292296")
def ayuda2():
    
    conexion=sqlite3.connect("rufo_db.db")
    fcursor= conexion.cursor()
    
    user= nombreusuario_verify.get()
    print(user)
    fcursor.execute('SELECT * FROM venta WHERE usuario = ? ',(user,))
    for fila in fcursor:
        prod=fila[2]
        prec=fila[3]
    ctex.insert(END,"\n"+"TornilloBot dice: Usted compro un "+prod+", adeuda "+str(prec)+"/S")
def ayuda3():
    ctex.insert(END,"\n"+"TornilloBot dice: Tenemos varidad\nHerramientas(Destornilladores,Alicates,etc)\nPintura(Pinturas,Herramientas de pintura)\nConstruccion(Variedad en materiales de construccion)")
def ayuda4():
    ctex.insert(END,"\n"+"Estamos ubicados en la calle lima 166 San Jeroniom de Tunan")    
    
    
menu_pantalla()
