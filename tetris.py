from tkinter import  *
from PIL import Image, ImageTk


"""
Nombre: largoLista
Entrada: lista
Salida: La cantidad de elementos que contiene la lista
Restricciones:
        El parametro 'lista' debe ser del tipo lista
        El parametro 'lista' no debe estar vacio
"""
def largoLista(lista):
    if not isinstance(lista, list):
        print("Error: Debe ingresar una lista!")
    elif lista == []:
        print("Error: La lista esta vacia!")
    else:
        return largoListaAux(lista)
def largoListaAux(lista):
    contador = 0
    for i in lista:
        contador += 1
    return contador


"""
Nombre: crearArchivoJuegoXX
Entrada: niguna
Salida: Un archivo juegoXX donde 'XX' representa un numero consecutivo
Restricciones: Las necesarias para el correcto funcionamiento
"""
def crearArchivoJuegoXX():
    if leerArchivo("JuegosGuardados.txt") == "":
        return crearArchivoJuegoXXAux(1)
    else:
        return crearArchivoJuegoXXAux(largoLista(archivoALista("JuegosGuardados.txt")))
def crearArchivoJuegoXXAux(identidicador):
    if identidicador <= 9:
        juegoXX = f"juego0{str(identidicador)}.txt"
    else: 
        juegoXX = f"juego{str(identidicador)}.txt"
    
    print(juegoXX)

    archivo = open(juegoXX, "x")
    archivo.close()
    

"""
Nombre: archivoALista
Entrada: nombreArchivo
Salida: El archivo convertido a lista
Restricciones: Las necesarias para el correcto funcionamiento
"""
def archivoALista(nombreArchivo):
    if not isinstance(nombreArchivo, str):
        print("Error: El parametro debe ser tipo string!")
    elif nombreArchivo == "":
        print("Error: La cadena de texto esta vacia!")
    else:
        try:
            archivo = open(nombreArchivo, "r")
            archivo.close()
        except:
            print("Error: El nombre del archivo ingresado no existe!")
        else:
            return archivoAListaAux(nombreArchivo)
def archivoAListaAux(nombreArchivo):
    resultado = []
    archivo = open(nombreArchivo, "r")
    contenidoArchivo = archivo.readlines()
    archivo.close()
    for contenido in contenidoArchivo:
        resultado = resultado + [contenido.split(",")]
    print(resultado)
    return resultado


"""
Nombre: leerArchivo
Entrada: nombreArchivo
Salida: El contenido del archivo
Restricciones: Las necesarias para el correcto funcionamiento
"""
def leerArchivo(nombreArchivo):
    if not isinstance(nombreArchivo, str):
        print("Error: Debe ingresar una cadena de texto!")
    elif nombreArchivo == "":
        print("Error: El nombre del archivo esta vacio!")
    else:
        return leerArchivoAux(nombreArchivo)
def leerArchivoAux(nombreArchivo):
    archivo = open(nombreArchivo, "r")
    contenido = archivo.read()
    archivo.close()

    return contenido

def seleccionarObstaculo(canva, evento, imagen, matrizIds):
    imagenId = canva.find_closest(evento.x, evento.y)
    canva.itemconfig(imagenId[0], image=imagen)

    cordenadas = buscarObstaculo(matrizIds, imagenId[0])
    

def quitarObstaculo(canva, evento, imagen, matrizIds):
    imagenId = canva.find_closest(evento.x, evento.y)
    canva.itemconfig(imagenId[0], image=imagen)

    cordenadas = buscarObstaculo(matrizIds, imagenId[0])

"""
Nombre: buscarObstaculo
Entrada: matrizIds y indice
Salida: Las coordenadas del obstaculo
Restricciones: Las necesarias para el correcto funcionamiento
"""
def buscarObstaculo(matrizIds, indice):
    for i in range(20):
        for j in range(10):
            if matrizIds[i][j] == indice:
                cordenadas = [i,j]
                return cordenadas



"""
Nombre: crearMatriz
Entrada: ninguna
Salida: Una matriz
Restricciones: Las necesarias para el correcto funcionamiento
"""
def crearMatriz():
    matriz = []
    for i in range(22):
        vector = []
        for j in range(12):
            if i == 0 or i == 21:
                vector += ["+"]
            else:
                if j == 0 or j == 11:
                    vector += ["+"]
                else:
                    vector += ["0"]
        matriz += [vector]


"""
Nombre: crearMatrizSeleccionObstaculos
Entrada: ninguna
Salida: Una matriz donde se seleccionaran los obstaculos
Restricciones: Las necesarias para el correcto funcionamiento
"""
def crearMatrizSeleccionObstaculos():
    matrizObstaculos = []
    for i in range(20):
        vectorObstaculos = []
        for j in range(10):
            vector_obstaculos += ["0"]
        matrizObstaculos += [vectorObstaculos]
        print(vectorObstaculos)


"""
Nombre: centrar_ventana
Entrada: ventana
Salida: La ventana reposicionada en el 'centro' de la pantalla
Restricciones: Las necesarias para el correcto funcionamiento
"""
def centrarVentana(ventana):
    ventana.update_idletasks()
    ancho = ventana.winfo_width()
    alto = ventana.winfo_height()
    x = (ventana.winfo_screenwidth() // 2) - (ancho // 2)
    y = (ventana.winfo_screenheight() // 2) - (alto // 2)
    ventana.geometry(f'{ancho}x{alto}+{x}+{y}') 


"""
Nombre: sobreBotonJugar
Entrada: evento
Salida: Cambia la imgen del 'boton jugar'
Restricciones: Las necesarias para el correcto funcionamiento
"""
def sobreBotonJugar(canvasInicio, identificador, nuevaImagen):
    canvasInicio.itemconfig(identificador, image=nuevaImagen)
    #ventanaInicial.update_idletasks()





"""
Nombre: ventana_inicio
Entraeda: Ninguna
Salida: La ventana inicial, iniciara el juego o finalizara el programa
Restricciones: Las necesarias para el correcto funcionamiento
"""
def ventanaInicio(): # Tal vez cambien los nombres de las variables
    ventanaInicial = Tk()   
    ventanaInicial.geometry("500x300")
    ventanaInicial.resizable(0,0)
    centrarVentana(ventanaInicial)

    canvasInicio = Canvas(ventanaInicial, width=500, height=300, bg="pink")
    canvasInicio.pack()

    imagenJugar = Image.open("jugar.png")
    imagenJugar = ImageTk.PhotoImage(imagenJugar)

    imagenJugarSeleccionada = Image.open("jugarSeleccionado.png")
    imagenJugarSeleccionada = ImageTk.PhotoImage(imagenJugarSeleccionada)
    
    imagenSalir = Image.open("salir.png")
    imagenSalir = ImageTk.PhotoImage(imagenSalir)

    imagenSalirSeleccionada = Image.open("salirSeleccionado.png")
    imagenSalirSeleccionada = ImageTk.PhotoImage(imagenSalirSeleccionada)
     
    botonJugar = canvasInicio.create_image(40, 30, anchor="nw", image=imagenJugar)
    botonSalir = canvasInicio.create_image(40, 90, anchor="nw", image=imagenSalir)


    canvasInicio.tag_bind(botonJugar, "<Enter>", lambda evento: sobreBotonJugar(canvasInicio, botonJugar, imagenJugarSeleccionada))
    canvasInicio.tag_bind(botonJugar, "<Leave>", lambda evento: sobreBotonJugar(canvasInicio, botonJugar, imagenJugar))
    canvasInicio.tag_bind(botonJugar, "<Button-1>", lambda evento: interfaz(ventanaInicial))



    canvasInicio.tag_bind(botonSalir, "<Enter>", lambda evento: sobreBotonJugar(canvasInicio, botonSalir, imagenSalirSeleccionada))
    canvasInicio.tag_bind(botonSalir, "<Leave>", lambda evento: sobreBotonJugar(canvasInicio, botonSalir, imagenSalir))
    canvasInicio.tag_bind(botonSalir, "<Button-1>", lambda evento: salir(ventanaInicial))
    
    
    #90x70

    ventanaInicial.mainloop()


"""
Nombre:
Entrada:
Salida: Crea una 'matriz' donde el ususario seleccionara los osbtaculos del tetriz
Restricciones: Las necesarias paraa el correcto funcionamiento
"""
def seleccionDeObstaculos(canvasPantalla,imagenParedTk,imagenFondoTk, imagenFondoSeleccionadoTk):
    contante_x = 39
    contante_y = 16.68

    matrizIdentificadores =  []
    
    for fila in range(22):
        vectorIdentificadores = []  
        for columna in range(12):
            x1 = columna * contante_x
            y1 = fila * contante_y
            x2 = x1 + contante_x
            y2 = y1 + contante_y

            if fila == 0 or fila == 21:
                canvasPantalla.create_image((x1 + x2) / 2, (y1 + y2) / 2, anchor="center", image=imagenParedTk)
            else:
                if columna == 0 or columna == 11:
                    canvasPantalla.create_image((x1 + x2) / 2, (y1 + y2) / 2, anchor="center", image=imagenParedTk)
                else:
                    area_fondo = canvasPantalla.create_image((x1 + x2) / 2, (y1 + y2) / 2, anchor="center", image=imagenFondoTk)
            
                    canvasPantalla.tag_bind(area_fondo, "<Button-1>", lambda evento:seleccionarObstaculo(canvasPantalla, evento, imagenFondoSeleccionadoTk, matrizIdentificadores))
                    canvasPantalla.tag_bind(area_fondo, "<Button-3>", lambda evento:quitarObstaculo(canvasPantalla, evento, imagenFondoTk, matrizIdentificadores))
        
                    vectorIdentificadores += [area_fondo]

        if vectorIdentificadores != []:
            matrizIdentificadores += [vectorIdentificadores]


"""
Nombre: interfaz 
Entrada: ventana
Salida: La creacion de nuevas ventanas(una matriz interactiva y una ventana de demostracion) junto con sus respectivos widgets
Restricciones: Las necesarias para el correcto funcionamiento
"""
def interfaz(ventana):
    crearArchivoJuegoXX()
    
    ventana.destroy()
    consola = Tk()
    consola.geometry("600x800")
    consola.resizable(0,0)
    consola.config(bg="#A9A9A9")
    centrarVentana(consola)

    imagenGameboy = Image.open("gameboyBase.png")
    imagenGameboy = ImageTk.PhotoImage(imagenGameboy)

    canvasGameboy = Canvas(consola, width=300, height=300)
    canvasGameboy.pack(fill="both", expand=True)
    canvasGameboy.create_image(0, 0, anchor="nw", image=imagenGameboy)
   
    canvasPantalla = Canvas(canvasGameboy, width=465, height=366, bg="pink")
    canvasPantalla.place(x=67, y=85)

    
    imagenPared = Image.open("bloqueGris.png")
    imagenPared = imagenPared.resize((39, 17))
    imagenParedTk = ImageTk.PhotoImage(imagenPared)

    imagenFondo= Image.open("fondo.png")
    imagenFondo = imagenFondo.resize((39, 17))
    imagenFondoTk = ImageTk.PhotoImage(imagenFondo)

    imagenFondoSeleccionado = Image.open("fondoSeleccionado.png")
    imagenFondoSeleccionado = imagenFondoSeleccionado.resize((39, 17))
    imagenFondoSeleccionadoTk = ImageTk.PhotoImage(imagenFondoSeleccionado)

    seleccionDeObstaculos(canvasPantalla,imagenParedTk,imagenFondoTk, imagenFondoSeleccionadoTk)

    canva_demostrativo = Canvas(canvasGameboy, width=235, height=178, bg="pink")
    canva_demostrativo.place(x=305, y=567)
    
    consola.mainloop()


"""
Nombre: salir
Entrada: ventana
Salida: Cierra (destruye) la ventana
Restricciones: Las necesarias para el correcto funcionamiento
"""
def salir(ventana):
    ventana.destroy()


ventanaInicio()