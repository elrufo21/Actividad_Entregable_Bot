
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
    
    Button(pantalla1,text="Iniciar sesion").pack
    
def registrar():
    global pantalla2
    pantalla2= Toplevel(pantalla)  
    pantalla2.geometry("400x250")
    pantalla2.title("Registro")
    pantalla2.iconbitmap("tornillo.ico")
    
    global nombreusuario_entry
    global contraseña_entry
    global recom_entry

    
    nombreusuario_entry=StringVar()
    contraseña_entry=StringVar()
    recom_entry=StringVar()

    
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
    Radiobutton(pantalla2,variable=recom_entry,text="Herramientas",value="h").pack()
    Radiobutton(pantalla2,variable=recom_entry,text="Pintura",value="p").pack()
    Radiobutton(pantalla2,variable=recom_entry,text="Construccion",value="c").pack()
    Radiobutton(pantalla2,variable=recom_entry,text="Todo",value="t").pack()
    
    
    Button(pantalla2,text="Registrar",command=inserta_datos).pack()

def inserta_datos():
    
    conexion=sqlite3("rufo_db.db")
    recomend=""
    if(recom_entry=="h"):
        recomend="herramientas"
        conexion.execute("insert into User(user,password,recommended) values(?,?,?) "),(nombreusuario_entry.get(),contraseña_entry.get(),recomend)
        conexion.commit()
        conexion.close
        
      
menu_pantalla()
