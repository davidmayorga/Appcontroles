# Este proyecto me permitirá llevar a una relación de los libros 
# Que tengo que leer y saber en cualquier momento los libros 
# Que tengo pendientes por leer 


from tkinter import *
from tkinter import messagebox
libros = []
#Definimos la funcion añadir()

def añadir():
    t = titulo.get()
    a = autor.get()
    e = editorial.get()
    np = NdePaginas.get()
    fl = fechalimite.get()
    libros.append(t+"$"+a+"$"+e+"$"+str(np)+"$"+fl)
    escribirLibro()
    messagebox.showinfo ("Guardado", "EL libro que tiene que leer ha sido guardado")
    titulo.set("")
    autor.set("")
    editorial.set("")
    NdePaginas.set("")
    fechalimite.set("")
    consultar()

# Definimos la función escribirLibro()

def escribirLibro(): 
    archivo=open ("biblioteca.txt", "w") 
    libros.sort() 
    for elemento in libros: 
        archivo.write (elemento+"\n") 
    archivo.close()

# Definimos  lafunción eliminar libro

def eliminarLibro():
    eliminado=eliminarLibro.get()
    removido=False
    for elemento in libros:
        arreglo = elemento.split("$")
        if eliminarLibro.get() ==arreglo [0]:
            respuesta=messagebox.askyesno("Eliminar libro", "Desea eliminar el libro con el titulori\n"+eliminado)
            if respuesta:
                libros.remove (elemento)
                removido = True
                escribirLibro ()
                consultar()
                respuesta=""

        if removido:
            messagebox.showinfo ("Elimina:", "Se ha eliminado el tituno\n"+eliminado)


# Definimos la función salir():
def salir():
    sa=messagebox.askyesno ("Sali", "¿Deseas finalizar?")
    if sa==True:
        quit()



#Definimos la función iniciarArchivo():

def iniciarArchivo (): 
    archivo = open("biblioteca.txt", "a") 
    archivo.close()


#Definimos la función cargar():

def cargar():
    archivo=open ("biblioteca.txt","r")
    linea = archivo.readline ()
    if linea:
        while linea:
            if linea [-1]=='\n':
                linea=linea [:-1]
            libros.append (linea)
            linea=archivo.readline ()
        archivo.close()


# Definimos la función consultar()
def consultar():
    r=Text (ventana, width=80, height=15)
    libros.sort()
    valores=[]
    r.insert(INSERT, "\tTitulo del libro\n")
    r.insert (INSERT,"------------------------------/------------------------------------/n")
    for elemento in libros:
        arreglo=elemento.split("$")
        valores.append(arreglo [0])
        r.insert(INSERT, "\t"+arreglo[0]+"\n Autor:"+arreglo[1]+ "\tEditorial: "+arreglo[2]+"N de páginas: "+arreglo[3]+"AtFecha limite:"+arreglo [4]+"\n")
        r.insert(INSERT,"------------------------------------------------/------------------------------/n")

    spinTitulo=Spinbox (ventana, value=(valores), textvariable=eliminarLibro,width=70).place(x=110, y=450)
    r.place (x=30,y=195)

    if libros==[]:
        spinTitulo=Spinbox (ventana, value=(valores), width=70).place(x=110, y=450)
    r.config(state=DISABLED)

#La parte principal del programa:

ventana =Tk()
titulo =StringVar ()
autor= StringVar()
editorial =StringVar () 
NdePaginas = IntVar()
fechalimite =StringVar()
eliminarlibro =StringVar ()
colorFondo = "#006"
colorLetra = "#FFF"
iniciarArchivo ()
cargar ()
consultar ()
ventana.title("Relación de libros que tengo que leer")
ventana.geometry("700x500")
ventana.configure(background=colorFondo)
etiquetaTitulo = Label(ventana, text="Relación de libros\ que tengo que leer", bg = colorFondo,fg = colorLetra). place(x=250 , y =10)

eTitulo = Label (ventana, text="Titulo: ", bg = colorFondo,fg = colorLetra).place(x=30,y=40) 

cTitulo = Entry (ventana, textvariable=titulo, width=70). place (x=120,y=40)

eAutor = Label (ventana, text="Autor: ", bg = colorFondo,  fg = colorLetra) .place(x=30, y=70)

cAutor = Entry (ventana, textvariable=autor) .place (x=120,y=70)

eEditorial = Label (ventana, text="Editorial: ",bg = colorFondo, fg = colorLetra) .place (x=30,y=100)

cEditorial = Entry (ventana, textvariable=editorial) .place (x=120,y=100) 

eNpaginas = Label (ventana, text="N° de páginas: ",bg = colorFondo, fg=colorLetra) .place (x=30,y=130)

cNpaginas = Entry (ventana, textvariable=NdePaginas). place (x=120,y=130)
eFechaLimite =Label (ventana, text="Fecha limite: ",\
    bg = colorFondo, fg = colorLetra) .place (x=30,y=160) 

botonAnadir = Button (ventana, text="Añadir libro",\
    command= añadir, bg="#009", fg="white") .place (x=550,y=38)

cFechaLimite = Entry (ventana, textvariable=fechalimite)\
    .place (x=120,y=160)

spinTitulo = Label (ventana, text="Titulo leide:",\
    bg = colorFondo, fg = colorLetra). place (x=30, y=450)

botonLeido = Button (ventana, text="Libro ya leido",\
    command=eliminarLibro, bg="#009", fg="white") .place (x=550,y=448)

imgbtn = PhotoImage(file="salir.png")
sal = Button(ventana, image=imgbtn,command=salir).place(x=300,y=60)
mainloop()
