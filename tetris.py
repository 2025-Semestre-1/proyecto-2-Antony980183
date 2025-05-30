from tkinter import  *
from PIL import Image, ImageTk
import random
import os

rotaciones = 1
x1 = 0
x2 = 0
x3 = 0
x4 = 0
x5 = 0
y1 = 0
y2 = 0
y3 = 0
y4 = 0
y5 = 0
moviendo = True

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

    return juegoXX


"""
Nombre: crearMatrizArchivoJuegoXX
Entrada: nombreArchivo
Salida: La matriz agregada en el archivo
Restricciones: Las necesarias para el correcto funcionamiento
"""
def crearMatrizArchivoJuegoXX(nombreArchivo):
    contenido = crearMatriz()
    contenido = listaATexto(contenido)

    archivo = open(nombreArchivo, "w")
    archivo.write(contenido)
    archivo.close()


"""
Nombre: listaATexto
Entrada: lista
Salida: La lista con formato archivo de texto
Restricciones: Las necesarias para el correcto funcionamiento
"""
def listaATexto(lista):
    if not isinstance(lista, list):
        print("Error: Debe ingresar una lista!")
    elif lista == []:
        print("Error: La lista esta vacia!")
    else:
        return listaATextoAux(lista)
def listaATextoAux(lista):
    texto = ""
    for i in range(largoLista(lista)):
        for j in range(largoLista(lista[0])):
            if j == largoLista(lista[0]) - 1:
                texto += lista[i][j] + "\n"
            else:
                texto += lista[i][j] + ","
    return texto

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
    return matriz




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
def sobreBoton(canvas, identificador, nuevaImagen):
    canvas.itemconfig(identificador, image=nuevaImagen)


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


    canvasInicio.tag_bind(botonJugar, "<Enter>", lambda evento: sobreBoton(canvasInicio, botonJugar, imagenJugarSeleccionada))
    canvasInicio.tag_bind(botonJugar, "<Leave>", lambda evento: sobreBoton(canvasInicio, botonJugar, imagenJugar))
    canvasInicio.tag_bind(botonJugar, "<Button-1>", lambda evento: interfaz(ventanaInicial))



    canvasInicio.tag_bind(botonSalir, "<Enter>", lambda evento: sobreBoton(canvasInicio, botonSalir, imagenSalirSeleccionada))
    canvasInicio.tag_bind(botonSalir, "<Leave>", lambda evento: sobreBoton(canvasInicio, botonSalir, imagenSalir))
    canvasInicio.tag_bind(botonSalir, "<Button-1>", lambda evento: salir(ventanaInicial))
    
    
    #90x70

    ventanaInicial.mainloop()


"""
Nombre: borrarArchivo
Entrada: nombreArchivo
Salida: Elimina un archivo de texto
Restricciones: Las necesarias para el correcto funcionamiento
"""
def borrarArchivo(nombreArchivo, ventana):
    os.remove(nombreArchivo)
    ventana.destroy()


"""
Nombre: seleccionDeObstaculos
Entrada: canvasPantalla,imagenParedTk,imagenFondoTk, imagenFondoSeleccionadoTk, nombreArchivo
Salida: Crea una 'matriz' donde el ususario seleccionara los osbtaculos del tetriz
Restricciones: Las necesarias paraa el correcto funcionamiento
"""
def seleccionDeObstaculos(canvasPantalla,imagenParedTk,imagenFondoTk, imagenFondoSeleccionadoTk, nombreArchivo):
    coordenadas = posicionImagenes()
    matrizIdentificadores = []
    for fila in range (22):
        vectorIdentificadores = []
        for columna in range(12):
            if fila == 0 or fila == 21:
                area_fondo = canvasPantalla.create_image(coordenadas[fila][columna][0] / 2, coordenadas[fila][columna][1] / 2, anchor="center", image=imagenParedTk)
            else:
                if columna == 0 or columna == 11:
                    area_fondo = canvasPantalla.create_image(coordenadas[fila][columna][0] / 2, coordenadas[fila][columna][1] / 2, anchor="center", image=imagenParedTk)
                else:
                    area_fondo = canvasPantalla.create_image(coordenadas[fila][columna][0] / 2, coordenadas[fila][columna][1] / 2, anchor="center", image=imagenFondoTk)
            
                    canvasPantalla.tag_bind(area_fondo, "<Button-1>", lambda evento:seleccionarObstaculo(canvasPantalla, evento, imagenFondoSeleccionadoTk, matrizIdentificadores, nombreArchivo))
                    canvasPantalla.tag_bind(area_fondo, "<Button-3>", lambda evento:quitarObstaculo(canvasPantalla, evento, imagenFondoTk, matrizIdentificadores, nombreArchivo))
        
            vectorIdentificadores += [area_fondo]
                

        matrizIdentificadores += [vectorIdentificadores]


def posicionImagenes():
    contante_x = 39
    contante_y = 16.68

    coordenadas = []
    for fila in range(22):
        posiciones = [] 
        for columna in range(12):
            x1 = columna * contante_x
            y1 = fila * contante_y
            x2 = x1 + contante_x
            y2 = y1 + contante_y
            posiciones += [[x1 + x2, y1 + y2]]
            prueba = posiciones
        #print(posiciones)
        coordenadas += [posiciones]
    return coordenadas

"""
Nombre: seleccionarObstaculo
Entrada: canva, evento, imagen, matrizIdentificadores, nombreArchivo
Salida: Cambia el contenido del archivo por un caracter de '+' segun la posicion indicada
Restriccioene: Las necesarias para el correceto funcionamiento
"""
def seleccionarObstaculo(canva, evento, imagen, matrizIdentificadores, nombreArchivo):
    print(evento.x, evento.y)
    imagenId = canva.find_closest(evento.x, evento.y)
    canva.itemconfig(imagenId[0], image=imagen)
    coordenadas = buscarObstaculo(matrizIdentificadores, imagenId[0])

    listaArchivo = archivoALista(nombreArchivo)
    listaArchivo = eliminarSaltosDeLinea(listaArchivo)
    resultado = []

    for i in range(largoLista(listaArchivo)):
        vector = []
        for j in range(largoLista(listaArchivo[0])):
            if i == coordenadas[0] and j == coordenadas[1]:
                vector += ["+"]
            else:
                vector += [listaArchivo[i][j]]
        resultado += [vector]
    
    modificarArchivoJuegoXX(nombreArchivo, resultado)


"""
Nombre: quitarObstaculo
Entrada: canva, evento, imagen, matrizIdentificadores, nombreArchivo
Salida: Cambia el contenido del archivo por un caracter de '0' segun la posicion indicada
Restriccioene: Las necesarias para el correceto funcionamiento
"""                      
def quitarObstaculo(canva, evento, imagen, matrizIdentificadores, nombreArchivo):
    print(evento.x, evento.y)
    imagenId = canva.find_closest(evento.x, evento.y)
    canva.itemconfig(imagenId[0], image=imagen)
    coordenadas = buscarObstaculo(matrizIdentificadores, imagenId[0])

    listaArchivo = archivoALista(nombreArchivo)
    listaArchivo = eliminarSaltosDeLinea(listaArchivo)
    resultado = []

    for i in range(largoLista(listaArchivo)):
        vector = []
        for j in range(largoLista(listaArchivo[0])):
            if i == coordenadas[0] and j == coordenadas[1]:
                vector += ["0"]
            else:
                vector += [listaArchivo[i][j]]
        resultado += [vector]
    
    modificarArchivoJuegoXX(nombreArchivo, resultado)


"""
Nombre: modificarArchivoJuegoXX
Entrada: nombreArchivo y contenido
Salida: Sobre escribe el contenido del archivo indicado
Restricciones: Las necesarias para el correcto funcionamiento
""" 
def modificarArchivoJuegoXX(nombreArchivo, contenido):
    contenido = listaATexto(contenido)

    archivo = open(nombreArchivo, "w")
    archivo.write(contenido)
    archivo.close()


"""
Nombre: eliminarSaltosDeLinea
Entrada: matriz
Salida: Una matriz sin los caracteres de salto de linea
Restricciones: Las necesarias para el correcto funcionamiento
"""
def eliminarSaltosDeLinea(matriz):
    resultado = []
    for i in range(largoLista(matriz)):
        contenido = []
        for j in range(largoLista(matriz[0])):
            if j == largoLista(matriz[0]) - 1:
                contenido += [matriz[i][j][:-1]]
            else:
                contenido += [matriz[i][j]]
        resultado += [contenido]
    return resultado


"""
Nombre: buscarObstaculo
Entrada: matrizIds y indice
Salida: Las coordenadas del obstaculo
Restricciones: Las necesarias para el correcto funcionamiento
"""
def buscarObstaculo(matrizIdentificadores, elemento):
    print(elemento)
    for i in range(largoLista(matrizIdentificadores)):
        for j in range(largoLista(matrizIdentificadores[0])):
            if matrizIdentificadores[i][j] == elemento:
                coordenadas = [i,j]
                print(coordenadas)
                return coordenadas


"""
Nombre: interfaz 
Entrada: ventana
Salida: La creacion de nuevas ventanas(una matriz interactiva y una ventana de demostracion) junto con sus respectivos widgets
Restricciones: Las necesarias para el correcto funcionamiento
"""
def interfaz(ventana):
    nombreArchivo = crearArchivoJuegoXX()
    crearMatrizArchivoJuegoXX(nombreArchivo)
    
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

    seleccionDeObstaculos(canvasPantalla,imagenParedTk,imagenFondoTk, imagenFondoSeleccionadoTk, nombreArchivo)

    canvasConfirmacion = Canvas(canvasGameboy, width=235, height=178, bg="pink")
    canvasConfirmacion.place(x=305, y=567)

    
    consola.protocol("WM_DELETE_WINDOW", lambda : borrarArchivo(nombreArchivo, consola))
    consola.mainloop()







def imprimirArchivoTetris(canvasPantalla, nombreArchivo, imagenParedTk, imagenFondoTk):
    coordenadas = posicionImagenes()
    listaArchivo = archivoALista(nombreArchivo)
    listaArchivo = eliminarSaltosDeLinea(listaArchivo)

    for i in range(largoLista(listaArchivo)):
        for j in range(largoLista(listaArchivo[0])):
            if listaArchivo[i][j] == "+":
                canvasPantalla.create_image(coordenadas[i][j][0] / 2, coordenadas[i][j][1] / 2, anchor="center", image=imagenParedTk)
            else:
                canvasPantalla.create_image(coordenadas[i][j][0] / 2, coordenadas[i][j][1] / 2, anchor="center", image=imagenFondoTk)


def crearListatetrominos():
    listatetrominos = []
    for i in range(30):
        listatetrominos += [random.randint(1,8)]
    return listatetrominos

def crearTetromino(canvasPantalla, imagenes, tetromino):
    global x1, x2, x3, x4, x5, y1, y2, y3, y4, y5

    coordenadas = posicionImagenes()
    if tetromino == 1:
        bloque1 = canvasPantalla.create_image(coordenadas[1][5][0]/ 2, coordenadas[1][5][1] / 2, anchor="center", image=imagenes[0])
        bloque2 = canvasPantalla.create_image(coordenadas[1][6][0]/ 2, coordenadas[1][6][1] / 2, anchor="center", image=imagenes[0])
        bloque3 = canvasPantalla.create_image(coordenadas[2][5][0]/ 2, coordenadas[2][5][1] / 2, anchor="center", image=imagenes[0])
        bloque4 = canvasPantalla.create_image(coordenadas[2][6][0]/ 2, coordenadas[2][6][1] / 2, anchor="center", image=imagenes[0])
        
        x1 = 1
        x2 = 1
        x3 = 2
        x4 = 2
    
    
        y1 = 5
        y2 = 6
        y3 = 5
        y4 = 6
    elif tetromino == 2:
        bloque1 = canvasPantalla.create_image(coordenadas[1][4][0]/ 2, coordenadas[1][4][1] / 2, anchor="center", image=imagenes[1])
        bloque2 = canvasPantalla.create_image(coordenadas[1][5][0]/ 2, coordenadas[1][5][1] / 2, anchor="center", image=imagenes[1])
        bloque3 = canvasPantalla.create_image(coordenadas[1][6][0]/ 2, coordenadas[1][6][1] / 2, anchor="center", image=imagenes[1])
        bloque4 = canvasPantalla.create_image(coordenadas[1][7][0]/ 2, coordenadas[1][7][1] / 2, anchor="center", image=imagenes[1])
    
        x1 = 1
        x2 = 1
        x3 = 1
        x4 = 1
    
    
        y1 = 4
        y2 = 5
        y3 = 6
        y4 = 7
    elif tetromino == 3:
        bloque1 = canvasPantalla.create_image(coordenadas[2][4][0]/ 2, coordenadas[2][4][1] / 2, anchor="center", image=imagenes[2])
        bloque2 = canvasPantalla.create_image(coordenadas[2][5][0]/ 2, coordenadas[2][5][1] / 2, anchor="center", image=imagenes[2])
        bloque3 = canvasPantalla.create_image(coordenadas[2][6][0]/ 2, coordenadas[2][6][1] / 2, anchor="center", image=imagenes[2])
        bloque4 = canvasPantalla.create_image(coordenadas[1][6][0]/ 2, coordenadas[1][6][1] / 2, anchor="center", image=imagenes[2])
        
        x1 = 2
        x2 = 2
        x3 = 2
        x4 = 1
    
    
        y1 = 4
        y2 = 5
        y3 = 6
        y4 = 6
    elif tetromino == 4:
        bloque1 = canvasPantalla.create_image(coordenadas[1][4][0]/ 2, coordenadas[1][4][1] / 2, anchor="center", image=imagenes[3])
        bloque2 = canvasPantalla.create_image(coordenadas[2][4][0]/ 2, coordenadas[2][4][1] / 2, anchor="center", image=imagenes[3])
        bloque3 = canvasPantalla.create_image(coordenadas[2][5][0]/ 2, coordenadas[2][5][1] / 2, anchor="center", image=imagenes[3])
        bloque4 = canvasPantalla.create_image(coordenadas[2][6][0]/ 2, coordenadas[2][6][1] / 2, anchor="center", image=imagenes[3])
        
        x1 = 1
        x2 = 2
        x3 = 2
        x4 = 2
    
    
        y1 = 4
        y2 = 4
        y3 = 5
        y4 = 6        
    elif tetromino == 5:
        bloque1 = canvasPantalla.create_image(coordenadas[2][4][0]/ 2, coordenadas[2][4][1]/ 2, anchor="center", image=imagenes[4])
        bloque2 = canvasPantalla.create_image(coordenadas[2][5][0]/ 2, coordenadas[2][5][1]/ 2, anchor="center", image=imagenes[4])
        bloque3 = canvasPantalla.create_image(coordenadas[2][6][0]/ 2, coordenadas[2][6][1]/ 2, anchor="center", image=imagenes[4])
        bloque4 = canvasPantalla.create_image(coordenadas[1][5][0]/ 2, coordenadas[1][5][1]/ 2, anchor="center", image=imagenes[4])

        x1 = 2
        x2 = 2
        x3 = 2
        x4 = 1
    
    
        y1 = 4
        y2 = 5
        y3 = 6
        y4 = 5
    elif tetromino == 6:
        bloque1 = canvasPantalla.create_image(coordenadas[1][5][0]/ 2, coordenadas[1][5][1] / 2, anchor="center", image=imagenes[5])
        bloque2 = canvasPantalla.create_image(coordenadas[1][6][0]/ 2, coordenadas[1][6][1] / 2, anchor="center", image=imagenes[5])
        bloque3 = canvasPantalla.create_image(coordenadas[2][6][0]/ 2, coordenadas[2][6][1] / 2, anchor="center", image=imagenes[5])
        bloque4 = canvasPantalla.create_image(coordenadas[2][7][0]/ 2, coordenadas[2][7][1] / 2, anchor="center", image=imagenes[5])

        x1 = 1
        x2 = 1
        x3 = 2
        x4 = 2
    
    
        y1 = 5
        y2 = 6
        y3 = 6
        y4 = 7
    elif tetromino == 7:
        bloque1 = canvasPantalla.create_image(coordenadas[1][4][0]/ 2, coordenadas[1][4][1] / 2, anchor="center", image=imagenes[6])
        bloque2 = canvasPantalla.create_image(coordenadas[2][4][0]/ 2, coordenadas[2][4][1] / 2, anchor="center", image=imagenes[6])
        bloque3 = canvasPantalla.create_image(coordenadas[2][5][0]/ 2, coordenadas[2][5][1] / 2, anchor="center", image=imagenes[6])
        bloque4 = canvasPantalla.create_image(coordenadas[2][6][0]/ 2, coordenadas[2][6][1] / 2, anchor="center", image=imagenes[6])
        bloque5 = canvasPantalla.create_image(coordenadas[1][6][0]/ 2, coordenadas[1][6][1] / 2, anchor="center", image=imagenes[6])

        x1 = 1
        x2 = 2
        x3 = 2
        x4 = 2
        x5 = 1
    
    
        y1 = 4
        y2 = 4
        y3 = 5
        y4 = 6
        y5 = 6
    else:
        bloque1 = canvasPantalla.create_image(coordenadas[2][4][0]/ 2, coordenadas[2][4][1] / 2, anchor="center", image=imagenes[7])
        bloque2 = canvasPantalla.create_image(coordenadas[1][5][0]/ 2, coordenadas[1][5][1] / 2, anchor="center", image=imagenes[7])
        bloque3 = canvasPantalla.create_image(coordenadas[2][5][0]/ 2, coordenadas[2][5][1] / 2, anchor="center", image=imagenes[7])
        bloque4 = canvasPantalla.create_image(coordenadas[3][5][0]/ 2, coordenadas[3][5][1] / 2, anchor="center", image=imagenes[7])
        bloque5 = canvasPantalla.create_image(coordenadas[2][6][0]/ 2, coordenadas[2][6][1] / 2, anchor="center", image=imagenes[7])

        x1 = 2
        x2 = 1
        x3 = 2
        x4 = 3
        x5 = 2
    
    
        y1 = 4
        y2 = 5
        y3 = 5
        y4 = 5
        y5 = 6
    if tetromino == 7 or tetromino == 8:
        return  [tetromino, bloque1, bloque2, bloque3, bloque4, bloque5]
    else:
        return  [tetromino, bloque1, bloque2, bloque3, bloque4]



def moverAbajo(canvasPantalla, listaImagenesBloques, nombreArchivo, consola):
    global x1, x2,  x3, x4, x5, listaTetrominos, tetromino, rotaciones
    eliminarAntiguaPosicionArchivo(nombreArchivo, tetromino, x1,x2,x3,x4,x5,y1,y2,y3,y4,y5)
    x1 +=1
    x2 +=1
    x3 +=1
    x4 +=1
    x5 +=1
    coordenadas = posicionImagenes()
    if validarMovimiento(nombreArchivo, tetromino) == False:
        x1 -=1
        x2 -=1
        x3 -=1
        x4 -=1
        x5 -=1
        escribirNuevaPosicionArchivo(nombreArchivo, tetromino, x1,x2,x3,x4,x5,y1,y2,y3,y4,y5)
        modificarMatrizIdentificadores(tetromino,x1,x2,x3,x4,x5,y1,y2,y3,y4,y5)
        
        
        consola.after(500, eliminarFilaTetris(canvasPantalla, nombreArchivo))
        eliminar = eliminarFilaMatrizIdentificadores(nombreArchivo)
        if eliminar == True:
            consola.after(500, refrescarPantallaTetris(canvasPantalla))

        eliminarFilaArchivo(nombreArchivo)
        
        listaTetrominos = listaTetrominos[1:]
        tetromino = crearTetromino(canvasPantalla, listaImagenesBloques, listaTetrominos[0])
        rotaciones = 1
    else:
        if tetromino[0] == 1:
            canvasPantalla.coords(tetromino[1],(coordenadas[x1][y1][0]/ 2, coordenadas[x1][y1][1] / 2))
            canvasPantalla.coords(tetromino[2],(coordenadas[x2][y2][0]/ 2, coordenadas[x2][y2][1] / 2))
            canvasPantalla.coords(tetromino[3],(coordenadas[x3][y3][0]/ 2, coordenadas[x3][y3][1] / 2))
            canvasPantalla.coords(tetromino[4],(coordenadas[x4][y4][0]/ 2, coordenadas[x4][y4][1] / 2))
        elif tetromino[0] == 2:
            canvasPantalla.coords(tetromino[1],(coordenadas[x1][y1][0]/ 2, coordenadas[x1][y1][1] / 2))
            canvasPantalla.coords(tetromino[2],(coordenadas[x2][y2][0]/ 2, coordenadas[x2][y2][1] / 2))
            canvasPantalla.coords(tetromino[3],(coordenadas[x3][y3][0]/ 2, coordenadas[x3][y3][1] / 2))
            canvasPantalla.coords(tetromino[4],(coordenadas[x4][y4][0]/ 2, coordenadas[x4][y4][1] / 2))
        elif tetromino[0] == 3:
            canvasPantalla.coords(tetromino[1],(coordenadas[x1][y1][0]/ 2, coordenadas[x1][y1][1] / 2))
            canvasPantalla.coords(tetromino[2],(coordenadas[x2][y2][0]/ 2, coordenadas[x2][y2][1] / 2))
            canvasPantalla.coords(tetromino[3],(coordenadas[x3][y3][0]/ 2, coordenadas[x3][y3][1] / 2))
            canvasPantalla.coords(tetromino[4],(coordenadas[x4][y4][0]/ 2, coordenadas[x4][y4][1] / 2))
        elif tetromino[0] == 4:
            canvasPantalla.coords(tetromino[1],(coordenadas[x1][y1][0]/ 2, coordenadas[x1][y1][1] / 2))
            canvasPantalla.coords(tetromino[2],(coordenadas[x2][y2][0]/ 2, coordenadas[x2][y2][1] / 2))
            canvasPantalla.coords(tetromino[3],(coordenadas[x3][y3][0]/ 2, coordenadas[x3][y3][1] / 2))
            canvasPantalla.coords(tetromino[4],(coordenadas[x4][y4][0]/ 2, coordenadas[x4][y4][1] / 2))
        elif tetromino[0] == 5:
            canvasPantalla.coords(tetromino[1],(coordenadas[x1][y1][0]/ 2, coordenadas[x1][y1][1] / 2))
            canvasPantalla.coords(tetromino[2],(coordenadas[x2][y2][0]/ 2, coordenadas[x2][y2][1] / 2))
            canvasPantalla.coords(tetromino[3],(coordenadas[x3][y3][0]/ 2, coordenadas[x3][y3][1] / 2))
            canvasPantalla.coords(tetromino[4],(coordenadas[x4][y4][0]/ 2, coordenadas[x4][y4][1] / 2))
        elif tetromino[0] == 6:
            canvasPantalla.coords(tetromino[1],(coordenadas[x1][y1][0]/ 2, coordenadas[x1][y1][1] / 2))
            canvasPantalla.coords(tetromino[2],(coordenadas[x2][y2][0]/ 2, coordenadas[x2][y2][1] / 2))
            canvasPantalla.coords(tetromino[3],(coordenadas[x3][y3][0]/ 2, coordenadas[x3][y3][1] / 2))
            canvasPantalla.coords(tetromino[4],(coordenadas[x4][y4][0]/ 2, coordenadas[x4][y4][1] / 2))
        elif tetromino[0] == 7:
            canvasPantalla.coords(tetromino[1],(coordenadas[x1][y1][0]/ 2, coordenadas[x1][y1][1] / 2))
            canvasPantalla.coords(tetromino[2],(coordenadas[x2][y2][0]/ 2, coordenadas[x2][y2][1] / 2))
            canvasPantalla.coords(tetromino[3],(coordenadas[x3][y3][0]/ 2, coordenadas[x3][y4][1] / 2))
            canvasPantalla.coords(tetromino[4],(coordenadas[x4][y4][0]/ 2, coordenadas[x4][y4][1] / 2))
            canvasPantalla.coords(tetromino[5],(coordenadas[x5][y5][0]/ 2, coordenadas[x5][y5][1] / 2))        
        else:
            canvasPantalla.coords(tetromino[1],(coordenadas[x1][y1][0]/ 2, coordenadas[x1][y1][1] / 2))
            canvasPantalla.coords(tetromino[2],(coordenadas[x2][y2][0]/ 2, coordenadas[x2][y2][1] / 2))
            canvasPantalla.coords(tetromino[3],(coordenadas[x3][y3][0]/ 2, coordenadas[x3][y4][1] / 2))
            canvasPantalla.coords(tetromino[4],(coordenadas[x4][y4][0]/ 2, coordenadas[x4][y4][1] / 2))
            canvasPantalla.coords(tetromino[5],(coordenadas[x5][y5][0]/ 2, coordenadas[x5][y5][1] / 2))
        escribirNuevaPosicionArchivo(nombreArchivo, tetromino, x1,x2,x3,x4,x5,y1,y2,y3,y4,y5)

def moverDerecha(canvasPantalla, nombreArchivo): 
    global y1, y2, y3, y4, y5, tetromino
    eliminarAntiguaPosicionArchivo(nombreArchivo, tetromino, x1,x2,x3,x4,x5,y1,y2,y3,y4,y5)
    y1 +=1
    y2 +=1
    y3 +=1
    y4 +=1
    y5 +=1
    coordenadas = posicionImagenes()
    if validarMovimiento(nombreArchivo, tetromino) == False:
        y1 -=1
        y2 -=1
        y3 -=1
        y4 -=1
        y5 -=1
    else:
        if tetromino[0] == 1:
            canvasPantalla.coords(tetromino[1],(coordenadas[x1][y1][0]/ 2, coordenadas[x1][y1][1] / 2))
            canvasPantalla.coords(tetromino[2],(coordenadas[x2][y2][0]/ 2, coordenadas[x2][y2][1] / 2))
            canvasPantalla.coords(tetromino[3],(coordenadas[x3][y3][0]/ 2, coordenadas[x3][y3][1] / 2))
            canvasPantalla.coords(tetromino[4],(coordenadas[x4][y4][0]/ 2, coordenadas[x4][y4][1] / 2))
        elif tetromino[0] == 2:
            canvasPantalla.coords(tetromino[1],(coordenadas[x1][y1][0]/ 2, coordenadas[x1][y1][1] / 2))
            canvasPantalla.coords(tetromino[2],(coordenadas[x2][y2][0]/ 2, coordenadas[x2][y2][1] / 2))
            canvasPantalla.coords(tetromino[3],(coordenadas[x3][y3][0]/ 2, coordenadas[x3][y3][1] / 2))
            canvasPantalla.coords(tetromino[4],(coordenadas[x4][y4][0]/ 2, coordenadas[x4][y4][1] / 2))
        elif tetromino[0] == 3:
            canvasPantalla.coords(tetromino[1],(coordenadas[x1][y1][0]/ 2, coordenadas[x1][y1][1] / 2))
            canvasPantalla.coords(tetromino[2],(coordenadas[x2][y2][0]/ 2, coordenadas[x2][y2][1] / 2))
            canvasPantalla.coords(tetromino[3],(coordenadas[x3][y3][0]/ 2, coordenadas[x3][y3][1] / 2))
            canvasPantalla.coords(tetromino[4],(coordenadas[x4][y4][0]/ 2, coordenadas[x4][y4][1] / 2))
        elif tetromino[0] == 4:
            canvasPantalla.coords(tetromino[1],(coordenadas[x1][y1][0]/ 2, coordenadas[x1][y1][1] / 2))
            canvasPantalla.coords(tetromino[2],(coordenadas[x2][y2][0]/ 2, coordenadas[x2][y2][1] / 2))
            canvasPantalla.coords(tetromino[3],(coordenadas[x3][y3][0]/ 2, coordenadas[x3][y3][1] / 2))
            canvasPantalla.coords(tetromino[4],(coordenadas[x4][y4][0]/ 2, coordenadas[x4][y4][1] / 2))
        elif tetromino[0] == 5:
            canvasPantalla.coords(tetromino[1],(coordenadas[x1][y1][0]/ 2, coordenadas[x1][y1][1] / 2))
            canvasPantalla.coords(tetromino[2],(coordenadas[x2][y2][0]/ 2, coordenadas[x2][y2][1] / 2))
            canvasPantalla.coords(tetromino[3],(coordenadas[x3][y3][0]/ 2, coordenadas[x3][y3][1] / 2))
            canvasPantalla.coords(tetromino[4],(coordenadas[x4][y4][0]/ 2, coordenadas[x4][y4][1] / 2))
        elif tetromino[0] == 6:
            canvasPantalla.coords(tetromino[1],(coordenadas[x1][y1][0]/ 2, coordenadas[x1][y1][1] / 2))
            canvasPantalla.coords(tetromino[2],(coordenadas[x2][y2][0]/ 2, coordenadas[x2][y2][1] / 2))
            canvasPantalla.coords(tetromino[3],(coordenadas[x3][y3][0]/ 2, coordenadas[x3][y3][1] / 2))
            canvasPantalla.coords(tetromino[4],(coordenadas[x4][y4][0]/ 2, coordenadas[x4][y4][1] / 2))
        elif tetromino[0] == 7:
            canvasPantalla.coords(tetromino[1],(coordenadas[x1][y1][0]/ 2, coordenadas[x1][y1][1] / 2))
            canvasPantalla.coords(tetromino[2],(coordenadas[x2][y2][0]/ 2, coordenadas[x2][y2][1] / 2))
            canvasPantalla.coords(tetromino[3],(coordenadas[x3][y3][0]/ 2, coordenadas[x3][y4][1] / 2))
            canvasPantalla.coords(tetromino[4],(coordenadas[x4][y4][0]/ 2, coordenadas[x4][y4][1] / 2))
            canvasPantalla.coords(tetromino[5],(coordenadas[x5][y5][0]/ 2, coordenadas[x5][y5][1] / 2))        
        else:
            canvasPantalla.coords(tetromino[1],(coordenadas[x1][y1][0]/ 2, coordenadas[x1][y1][1] / 2))
            canvasPantalla.coords(tetromino[2],(coordenadas[x2][y2][0]/ 2, coordenadas[x2][y2][1] / 2))
            canvasPantalla.coords(tetromino[3],(coordenadas[x3][y3][0]/ 2, coordenadas[x3][y4][1] / 2))
            canvasPantalla.coords(tetromino[4],(coordenadas[x4][y4][0]/ 2, coordenadas[x4][y4][1] / 2))
            canvasPantalla.coords(tetromino[5],(coordenadas[x5][y5][0]/ 2, coordenadas[x5][y5][1] / 2))
        escribirNuevaPosicionArchivo(nombreArchivo, tetromino, x1,x2,x3,x4,x5,y1,y2,y3,y4,y5)


def moverIzquierda(canvasPantalla, nombreArchivo): 
    global y1, y2, y3, y4, y5, tetromino
    eliminarAntiguaPosicionArchivo(nombreArchivo, tetromino, x1,x2,x3,x4,x5,y1,y2,y3,y4,y5)
    y1 -=1
    y2 -=1
    y3 -=1
    y4 -=1
    y5 -=1
    coordenadas = posicionImagenes()
    if validarMovimiento(nombreArchivo, tetromino) == False:
        y1 +=1
        y2 +=1
        y3 +=1
        y4 +=1
        y5 +=1
    else:
        if tetromino[0] == 1:
            canvasPantalla.coords(tetromino[1],(coordenadas[x1][y1][0]/ 2, coordenadas[x1][y1][1] / 2))
            canvasPantalla.coords(tetromino[2],(coordenadas[x2][y2][0]/ 2, coordenadas[x2][y2][1] / 2))
            canvasPantalla.coords(tetromino[3],(coordenadas[x3][y3][0]/ 2, coordenadas[x3][y3][1] / 2))
            canvasPantalla.coords(tetromino[4],(coordenadas[x4][y4][0]/ 2, coordenadas[x4][y4][1] / 2))
        elif tetromino[0] == 2:
            canvasPantalla.coords(tetromino[1],(coordenadas[x1][y1][0]/ 2, coordenadas[x1][y1][1] / 2))
            canvasPantalla.coords(tetromino[2],(coordenadas[x2][y2][0]/ 2, coordenadas[x2][y2][1] / 2))
            canvasPantalla.coords(tetromino[3],(coordenadas[x3][y3][0]/ 2, coordenadas[x3][y3][1] / 2))
            canvasPantalla.coords(tetromino[4],(coordenadas[x4][y4][0]/ 2, coordenadas[x4][y4][1] / 2))
        elif tetromino[0] == 3:
            canvasPantalla.coords(tetromino[1],(coordenadas[x1][y1][0]/ 2, coordenadas[x1][y1][1] / 2))
            canvasPantalla.coords(tetromino[2],(coordenadas[x2][y2][0]/ 2, coordenadas[x2][y2][1] / 2))
            canvasPantalla.coords(tetromino[3],(coordenadas[x3][y3][0]/ 2, coordenadas[x3][y3][1] / 2))
            canvasPantalla.coords(tetromino[4],(coordenadas[x4][y4][0]/ 2, coordenadas[x4][y4][1] / 2))
        elif tetromino[0] == 4:
            canvasPantalla.coords(tetromino[1],(coordenadas[x1][y1][0]/ 2, coordenadas[x1][y1][1] / 2))
            canvasPantalla.coords(tetromino[2],(coordenadas[x2][y2][0]/ 2, coordenadas[x2][y2][1] / 2))
            canvasPantalla.coords(tetromino[3],(coordenadas[x3][y3][0]/ 2, coordenadas[x3][y3][1] / 2))
            canvasPantalla.coords(tetromino[4],(coordenadas[x4][y4][0]/ 2, coordenadas[x4][y4][1] / 2))
        elif tetromino[0] == 5:
            canvasPantalla.coords(tetromino[1],(coordenadas[x1][y1][0]/ 2, coordenadas[x1][y1][1] / 2))
            canvasPantalla.coords(tetromino[2],(coordenadas[x2][y2][0]/ 2, coordenadas[x2][y2][1] / 2))
            canvasPantalla.coords(tetromino[3],(coordenadas[x3][y3][0]/ 2, coordenadas[x3][y3][1] / 2))
            canvasPantalla.coords(tetromino[4],(coordenadas[x4][y4][0]/ 2, coordenadas[x4][y4][1] / 2))
        elif tetromino[0] == 6:
            canvasPantalla.coords(tetromino[1],(coordenadas[x1][y1][0]/ 2, coordenadas[x1][y1][1] / 2))
            canvasPantalla.coords(tetromino[2],(coordenadas[x2][y2][0]/ 2, coordenadas[x2][y2][1] / 2))
            canvasPantalla.coords(tetromino[3],(coordenadas[x3][y3][0]/ 2, coordenadas[x3][y3][1] / 2))
            canvasPantalla.coords(tetromino[4],(coordenadas[x4][y4][0]/ 2, coordenadas[x4][y4][1] / 2))
        elif tetromino[0] == 7:
            canvasPantalla.coords(tetromino[1],(coordenadas[x1][y1][0]/ 2, coordenadas[x1][y1][1] / 2))
            canvasPantalla.coords(tetromino[2],(coordenadas[x2][y2][0]/ 2, coordenadas[x2][y2][1] / 2))
            canvasPantalla.coords(tetromino[3],(coordenadas[x3][y3][0]/ 2, coordenadas[x3][y4][1] / 2))
            canvasPantalla.coords(tetromino[4],(coordenadas[x4][y4][0]/ 2, coordenadas[x4][y4][1] / 2))
            canvasPantalla.coords(tetromino[5],(coordenadas[x5][y5][0]/ 2, coordenadas[x5][y5][1] / 2))        
        else:
            canvasPantalla.coords(tetromino[1],(coordenadas[x1][y1][0]/ 2, coordenadas[x1][y1][1] / 2))
            canvasPantalla.coords(tetromino[2],(coordenadas[x2][y2][0]/ 2, coordenadas[x2][y2][1] / 2))
            canvasPantalla.coords(tetromino[3],(coordenadas[x3][y3][0]/ 2, coordenadas[x3][y4][1] / 2))
            canvasPantalla.coords(tetromino[4],(coordenadas[x4][y4][0]/ 2, coordenadas[x4][y4][1] / 2))
            canvasPantalla.coords(tetromino[5],(coordenadas[x5][y5][0]/ 2, coordenadas[x5][y5][1] / 2))
        escribirNuevaPosicionArchivo(nombreArchivo, tetromino, x1,x2,x3,x4,x5,y1,y2,y3,y4,y5)


def rotar(canvasPantalla, tetromino, nombreArchivo):
    global rotaciones, x1, x2, x3, x4, x5, y1, y2, y3, y4, y5
    eliminarAntiguaPosicionArchivo(nombreArchivo, tetromino, x1,x2,x3,x4,x5,y1,y2,y3,y4,y5)
    x1 +=1
    x2 +=1
    x3 +=1
    x4 +=1
    x5 +=1
   
    y1 +=1
    y2 +=1
    y3 +=1
    y4 +=1
    y5 +=1
    
    if validarMovimiento(nombreArchivo, tetromino) == False:
        x1 -=1
        x2 -=1
        x3 -=1
        x4 -=1
        x5 -=1
    
        y1 -=1
        y2 -=1
        y3 -=1
        y4 -=1
        y5 -=1
    else:
        x1 -=1
        x2 -=1
        x3 -=1
        x4 -=1
        x5 -=1
    
        y1 -=1
        y2 -=1
        y3 -=1
        y4 -=1
        y5 -=1
        coordenadas = posicionImagenes()
        if tetromino[0] == 2:
            if rotaciones == 1:
                x2 = x1 + 1
                x3 = x2  + 1
                x4 = x3 + 1

                y1 += 2
                y2 = y1
                y3 = y1
                y4 = y1
                canvasPantalla.coords(tetromino[1], coordenadas[x1][y1][0] / 2, coordenadas[x1][y1][1] / 2)
                canvasPantalla.coords(tetromino[2], coordenadas[x2][y2][0] / 2, coordenadas[x2][y2][1] / 2)
                canvasPantalla.coords(tetromino[3], coordenadas[x3][y3][0] / 2, coordenadas[x3][y3][1] / 2)
                canvasPantalla.coords(tetromino[4], coordenadas[x4][y4][0] / 2, coordenadas[x4][y4][1] / 2)
            elif rotaciones == 2:
                x2 = x1
                x3 = x1
                x4 = x1

                y1 -= 2
                y2 = y1 + 1
                y3 = y2 + 1
                y4 = y3 + 1

                canvasPantalla.coords(tetromino[1], coordenadas[x1][y1][0] / 2, coordenadas[x1][y1][1] / 2)
                canvasPantalla.coords(tetromino[2], coordenadas[x2][y2][0] / 2, coordenadas[x2][y2][1] / 2)
                canvasPantalla.coords(tetromino[3], coordenadas[x3][y3][0] / 2, coordenadas[x3][y3][1] / 2)
                canvasPantalla.coords(tetromino[4], coordenadas[x4][y4][0] / 2, coordenadas[x4][y4][1] / 2)

            elif rotaciones == 3:
                x2 = x1 + 1
                x3 = x2 + 1
                x4 = x3 + 1

                y1 += 1
                y2 = y1
                y3 = y1
                y4 = y1

                canvasPantalla.coords(tetromino[1], coordenadas[x1][y1][0] / 2, coordenadas[x1][y1][1] / 2)
                canvasPantalla.coords(tetromino[2], coordenadas[x2][y2][0] / 2, coordenadas[x2][y2][1] / 2)
                canvasPantalla.coords(tetromino[3], coordenadas[x3][y3][0] / 2, coordenadas[x3][y3][1] / 2)
                canvasPantalla.coords(tetromino[4], coordenadas[x4][y4][0] / 2, coordenadas[x4][y4][1] / 2)
            else:
                x2 = x1
                x3 = x1 
                x4 = x1

                y1 -= 1
                y2 = y1 + 1
                y3 = y2 + 1
                y4 = y3 + 1
                canvasPantalla.coords(tetromino[1], coordenadas[x1][y1][0] / 2, coordenadas[x1][y1][1] / 2)
                canvasPantalla.coords(tetromino[2], coordenadas[x2][y2][0] / 2, coordenadas[x2][y2][1] / 2)
                canvasPantalla.coords(tetromino[3], coordenadas[x3][y3][0] / 2, coordenadas[x3][y3][1] / 2)
                canvasPantalla.coords(tetromino[4], coordenadas[x4][y4][0] / 2, coordenadas[x4][y4][1] / 2)

                rotaciones = 0
        elif tetromino[0] == 3: 
            if rotaciones == 1:
                x1 = x2 - 1
                x3 = x2 + 1
                x4 = x3

                y1 = y2
                y3 = y2
                y4 = y2 + 1

                canvasPantalla.coords(tetromino[1], coordenadas[x1][y1][0] / 2, coordenadas[x1][y1][1] / 2)
                canvasPantalla.coords(tetromino[2], coordenadas[x2][y2][0] / 2, coordenadas[x2][y2][1] / 2)
                canvasPantalla.coords(tetromino[3], coordenadas[x3][y3][0] / 2, coordenadas[x3][y3][1] / 2)
                canvasPantalla.coords(tetromino[4], coordenadas[x4][y4][0] / 2, coordenadas[x4][y4][1] / 2)
            elif rotaciones == 2:
                x2 -=1
                x3 = x2
                x4 = x3 + 1

                y1 -=1
                y3 = y2 + 1
                y4 = y1

                canvasPantalla.coords(tetromino[1], coordenadas[x1][y1][0] / 2, coordenadas[x1][y1][1] / 2)
                canvasPantalla.coords(tetromino[2], coordenadas[x2][y2][0] / 2, coordenadas[x2][y2][1] / 2)
                canvasPantalla.coords(tetromino[3], coordenadas[x3][y3][0] / 2, coordenadas[x3][y3][1] / 2)
                canvasPantalla.coords(tetromino[4], coordenadas[x4][y4][0] / 2, coordenadas[x4][y4][1] / 2)
            elif rotaciones == 3:
                x3 = x2 + 1
                x4 = x3 + 1

                y3 = y2 
                y4 = y2

                canvasPantalla.coords(tetromino[1], coordenadas[x1][y1][0] / 2, coordenadas[x1][y1][1] / 2)
                canvasPantalla.coords(tetromino[2], coordenadas[x2][y2][0] / 2, coordenadas[x2][y2][1] / 2)
                canvasPantalla.coords(tetromino[3], coordenadas[x3][y3][0] / 2, coordenadas[x3][y3][1] / 2)
                canvasPantalla.coords(tetromino[4], coordenadas[x4][y4][0] / 2, coordenadas[x4][y4][1] / 2) 
            else:
                x1 += 1
                x2 += 1
                x4 = x1 - 1

                y3 += 1
                y4 = y2 + 1
                            
                canvasPantalla.coords(tetromino[1], coordenadas[x1][y1][0] / 2, coordenadas[x1][y1][1] / 2)
                canvasPantalla.coords(tetromino[2], coordenadas[x2][y2][0] / 2, coordenadas[x2][y2][1] / 2)
                canvasPantalla.coords(tetromino[3], coordenadas[x3][y3][0] / 2, coordenadas[x3][y3][1] / 2)
                canvasPantalla.coords(tetromino[4], coordenadas[x4][y4][0] / 2, coordenadas[x4][y4][1] / 2)

                rotaciones = 0         
        elif tetromino[0] == 4:
            if rotaciones == 1:
                x2 += 1
                x4 += 1

                y1 += 1
                y2 += 1
                y4 = y2 - 1

                canvasPantalla.coords(tetromino[1], coordenadas[x1][y1][0] / 2, coordenadas[x1][y1][1] / 2)
                canvasPantalla.coords(tetromino[2], coordenadas[x2][y2][0] / 2, coordenadas[x2][y2][1] / 2)
                canvasPantalla.coords(tetromino[3], coordenadas[x3][y3][0] / 2, coordenadas[x3][y3][1] / 2)
                canvasPantalla.coords(tetromino[4], coordenadas[x4][y4][0] / 2, coordenadas[x4][y4][1] / 2) 
            elif rotaciones == 2:
                x2 -= 2
                x3 -= 1
                x4 -= 1

                y1 -= 1
                y3 += 1
                y4 = y3
            
                canvasPantalla.coords(tetromino[1], coordenadas[x1][y1][0] / 2, coordenadas[x1][y1][1] / 2)
                canvasPantalla.coords(tetromino[2], coordenadas[x2][y2][0] / 2, coordenadas[x2][y2][1] / 2)
                canvasPantalla.coords(tetromino[3], coordenadas[x3][y3][0] / 2, coordenadas[x3][y3][1] / 2)
                canvasPantalla.coords(tetromino[4], coordenadas[x4][y4][0] / 2, coordenadas[x4][y4][1] / 2) 
            elif rotaciones == 3:
                x1 += 1
                x4 = x1 + 1

                y1 += 1
                y4 = y1
            
                canvasPantalla.coords(tetromino[1], coordenadas[x1][y1][0] / 2, coordenadas[x1][y1][1] / 2)
                canvasPantalla.coords(tetromino[2], coordenadas[x2][y2][0] / 2, coordenadas[x2][y2][1] / 2)
                canvasPantalla.coords(tetromino[3], coordenadas[x3][y3][0] / 2, coordenadas[x3][y3][1] / 2)
                canvasPantalla.coords(tetromino[4], coordenadas[x4][y4][0] / 2, coordenadas[x4][y4][1] / 2)
            elif rotaciones == 4:
                x1 -= 1
                x2 += 1
                x3 += 1
                x4 -= 1

                y1 -= 1
                y2 = y1
                y3 = y2 + 1
                y4 = y3 + 1 

                canvasPantalla.coords(tetromino[1], coordenadas[x1][y1][0] / 2, coordenadas[x1][y1][1] / 2)
                canvasPantalla.coords(tetromino[2], coordenadas[x2][y2][0] / 2, coordenadas[x2][y2][1] / 2)
                canvasPantalla.coords(tetromino[3], coordenadas[x3][y3][0] / 2, coordenadas[x3][y3][1] / 2)
                canvasPantalla.coords(tetromino[4], coordenadas[x4][y4][0] / 2, coordenadas[x4][y4][1] / 2)

                rotaciones = 0
        elif tetromino[0] == 5:
            if rotaciones == 1:
                x3 = x2 + 1
                y3 = y2

                canvasPantalla.coords(tetromino[1], coordenadas[x1][y1][0] / 2, coordenadas[x1][y1][1] / 2)
                canvasPantalla.coords(tetromino[2], coordenadas[x2][y2][0] / 2, coordenadas[x2][y2][1] / 2)
                canvasPantalla.coords(tetromino[3], coordenadas[x3][y3][0] / 2, coordenadas[x3][y3][1] / 2)
                canvasPantalla.coords(tetromino[4], coordenadas[x4][y4][0] / 2, coordenadas[x4][y4][1] / 2)
            elif rotaciones == 2:
                x4 = x2
                y4 = y2 + 1

                canvasPantalla.coords(tetromino[1], coordenadas[x1][y1][0] / 2, coordenadas[x1][y1][1] / 2)
                canvasPantalla.coords(tetromino[2], coordenadas[x2][y2][0] / 2, coordenadas[x2][y2][1] / 2)
                canvasPantalla.coords(tetromino[3], coordenadas[x3][y3][0] / 2, coordenadas[x3][y3][1] / 2)
                canvasPantalla.coords(tetromino[4], coordenadas[x4][y4][0] / 2, coordenadas[x4][y4][1] / 2)
            elif rotaciones == 3:
                x1 = x2 - 1
                
                y1 = y2

                canvasPantalla.coords(tetromino[1], coordenadas[x1][y1][0] / 2, coordenadas[x1][y1][1] / 2)
                canvasPantalla.coords(tetromino[2], coordenadas[x2][y2][0] / 2, coordenadas[x2][y2][1] / 2)
                canvasPantalla.coords(tetromino[3], coordenadas[x3][y3][0] / 2, coordenadas[x3][y3][1] / 2)
                canvasPantalla.coords(tetromino[4], coordenadas[x4][y4][0] / 2, coordenadas[x4][y4][1] / 2)
            else:
                x1 = x2
                x3 = x2
                x4 = x1 - 1

                y1 = y2 - 1
                y3 = y2 + 1
                y4 = y2

                canvasPantalla.coords(tetromino[1], coordenadas[x1][y1][0] / 2, coordenadas[x1][y1][1] / 2)
                canvasPantalla.coords(tetromino[2], coordenadas[x2][y2][0] / 2, coordenadas[x2][y2][1] / 2)
                canvasPantalla.coords(tetromino[3], coordenadas[x3][y3][0] / 2, coordenadas[x3][y3][1] / 2)
                canvasPantalla.coords(tetromino[4], coordenadas[x4][y4][0] / 2, coordenadas[x4][y4][1] / 2)

                rotaciones = 0
        elif tetromino[0] == 6:
            if rotaciones == 1:
                x2 = x1 + 1
                x3 = x2
                x4 = x3 + 1

                y2 = y1
                y3 = y2 - 1
                y4 = y3

                canvasPantalla.coords(tetromino[1], coordenadas[x1][y1][0] / 2, coordenadas[x1][y1][1] / 2)
                canvasPantalla.coords(tetromino[2], coordenadas[x2][y2][0] / 2, coordenadas[x2][y2][1] / 2)
                canvasPantalla.coords(tetromino[3], coordenadas[x3][y3][0] / 2, coordenadas[x3][y3][1] / 2)
                canvasPantalla.coords(tetromino[4], coordenadas[x4][y4][0] / 2, coordenadas[x4][y4][1] / 2)
            elif rotaciones == 2:
                x2 = x1
                x3 = x2 + 1
                x4 = x3

                y2 = y1 + 1
                y3 = y2
                y4 = y3 + 1

                canvasPantalla.coords(tetromino[1], coordenadas[x1][y1][0] / 2, coordenadas[x1][y1][1] / 2)
                canvasPantalla.coords(tetromino[2], coordenadas[x2][y2][0] / 2, coordenadas[x2][y2][1] / 2)
                canvasPantalla.coords(tetromino[3], coordenadas[x3][y3][0] / 2, coordenadas[x3][y3][1] / 2)
                canvasPantalla.coords(tetromino[4], coordenadas[x4][y4][0] / 2, coordenadas[x4][y4][1] / 2)
        
            elif rotaciones == 3:
                x1 += 1
                x4 = x3 + 1

                y2 += 1
                y1 = y2
                y4 = y3 

                canvasPantalla.coords(tetromino[1], coordenadas[x1][y1][0] / 2, coordenadas[x1][y1][1] / 2)
                canvasPantalla.coords(tetromino[2], coordenadas[x2][y2][0] / 2, coordenadas[x2][y2][1] / 2)
                canvasPantalla.coords(tetromino[3], coordenadas[x3][y3][0] / 2, coordenadas[x3][y3][1] / 2)
                canvasPantalla.coords(tetromino[4], coordenadas[x4][y4][0] / 2, coordenadas[x4][y4][1] / 2)
            else:
                x1 = x2
                x4 = x3

                y2 -= 1
                y1 = y2 - 1
                y4 = y3 + 1

                canvasPantalla.coords(tetromino[1], coordenadas[x1][y1][0] / 2, coordenadas[x1][y1][1] / 2)
                canvasPantalla.coords(tetromino[2], coordenadas[x2][y2][0] / 2, coordenadas[x2][y2][1] / 2)
                canvasPantalla.coords(tetromino[3], coordenadas[x3][y3][0] / 2, coordenadas[x3][y3][1] / 2)
                canvasPantalla.coords(tetromino[4], coordenadas[x4][y4][0] / 2, coordenadas[x4][y4][1] / 2)

                rotaciones = 0
        elif tetromino[0] == 7:
            if rotaciones == 1:
                x2 += 1
                x4 = x2

                y1 = y3
                y2 = y3
                
                canvasPantalla.coords(tetromino[1], coordenadas[x1][y1][0] / 2, coordenadas[x1][y1][1] / 2)
                canvasPantalla.coords(tetromino[2], coordenadas[x2][y2][0] / 2, coordenadas[x2][y2][1] / 2)
                canvasPantalla.coords(tetromino[3], coordenadas[x3][y3][0] / 2, coordenadas[x3][y3][1] / 2)
                canvasPantalla.coords(tetromino[4], coordenadas[x4][y4][0] / 2, coordenadas[x4][y4][1] / 2)
                canvasPantalla.coords(tetromino[5], coordenadas[x5][y5][0] / 2, coordenadas[x5][y5][1] / 2)
            elif rotaciones == 2:
                x3 = x1
                x2 = x3 + 1
                x4 = x2

                y1 -= 1
                y2 = y1


                canvasPantalla.coords(tetromino[1], coordenadas[x1][y1][0] / 2, coordenadas[x1][y1][1] / 2)
                canvasPantalla.coords(tetromino[2], coordenadas[x2][y2][0] / 2, coordenadas[x2][y2][1] / 2)
                canvasPantalla.coords(tetromino[3], coordenadas[x3][y3][0] / 2, coordenadas[x3][y3][1] / 2)
                canvasPantalla.coords(tetromino[4], coordenadas[x4][y4][0] / 2, coordenadas[x4][y4][1] / 2)
                canvasPantalla.coords(tetromino[5], coordenadas[x5][y5][0] / 2, coordenadas[x5][y5][1] / 2)
            elif rotaciones == 3:
                x5 = x2 + 1
                x4 = x5

                y2 = y3
                y5 = y3
                y4 = y5 - 1

                canvasPantalla.coords(tetromino[1], coordenadas[x1][y1][0] / 2, coordenadas[x1][y1][1] / 2)
                canvasPantalla.coords(tetromino[2], coordenadas[x2][y2][0] / 2, coordenadas[x2][y2][1] / 2)
                canvasPantalla.coords(tetromino[3], coordenadas[x3][y3][0] / 2, coordenadas[x3][y3][1] / 2)
                canvasPantalla.coords(tetromino[4], coordenadas[x4][y4][0] / 2, coordenadas[x4][y4][1] / 2)
                canvasPantalla.coords(tetromino[5], coordenadas[x5][y5][0] / 2, coordenadas[x5][y5][1] / 2)
            else:
                x3 = x2
                x4 = x2
                x5 = x1

                y2 = y1
                y3 = y2 + 1
                y4 = y3 + 1
                y5 = y4
                
                canvasPantalla.coords(tetromino[1], coordenadas[x1][y1][0] / 2, coordenadas[x1][y1][1] / 2)
                canvasPantalla.coords(tetromino[2], coordenadas[x2][y2][0] / 2, coordenadas[x2][y2][1] / 2)
                canvasPantalla.coords(tetromino[3], coordenadas[x3][y3][0] / 2, coordenadas[x3][y3][1] / 2)
                canvasPantalla.coords(tetromino[4], coordenadas[x4][y4][0] / 2, coordenadas[x4][y4][1] / 2)
                canvasPantalla.coords(tetromino[5], coordenadas[x5][y5][0] / 2, coordenadas[x5][y5][1] / 2)

                rotaciones = 0
        rotaciones += 1
        escribirNuevaPosicionArchivo(nombreArchivo, tetromino, x1,x2,x3,x4,x5,y1,y2,y3,y4,y5)

def  validarMovimiento(nombreArchivo, tetromino):# mejorar
    global x1, x2,  x3, x4, x5, y1, y2, y3, y4, y5
    listaArchivo = archivoALista(nombreArchivo)
    listaArchivo = eliminarSaltosDeLinea(listaArchivo)
    if tetromino[0] >= 1 and tetromino[0] <= 6:
        for i in range(largoLista(listaArchivo)):
            for j in range(largoLista(listaArchivo[0])):
                if i != 0:
                    if i == x1 and j == y1:
                        if verificarElementos(listaArchivo[i][j]):
                            return False
                    elif i == x2 and j == y2:
                        if verificarElementos(listaArchivo[i][j]):
                            return False
                    elif i == x3 and j == y3:
                        if verificarElementos(listaArchivo[i][j]):
                            return False
                    else:
                        if i == x4 and j == y4:
                            if verificarElementos(listaArchivo[i][j]):
                                return False
        return True
    else:
        for i in range(largoLista(listaArchivo)):
            for j in range(largoLista(listaArchivo[0])):
                if i != 0:
                    if i == x1 and j == y1:
                        if verificarElementos(listaArchivo[i][j]):
                            return False
                    elif i == x2 and j == y2:
                        if verificarElementos(listaArchivo[i][j]):
                            return False
                    elif i == x3 and j == y3:
                        if verificarElementos(listaArchivo[i][j]):
                            return False
                    elif i == x4 and j == y4:
                        if verificarElementos(listaArchivo[i][j]):
                            return False
                    else:
                        if i == x5 and j == y5:
                            if verificarElementos(listaArchivo[i][j]):
                                return False
        return True

def verificarElementos(elemento):
    listaElementos = ["+","1","2","3","4","5","6","7","8"]
    for i in listaElementos:
        if i == elemento:
            return True
    return False


def escribirNuevaPosicionArchivo(nombreArchivo, tetrimino, x1, x2,  x3, x4, x5, y1, y2, y3, y4, y5):
    listaArchivo = archivoALista(nombreArchivo)
    listaArchivo = eliminarSaltosDeLinea(listaArchivo)
    nuevoContenido = []
    
    if tetrimino[0] == 1:
        imagen = "1"
    elif tetrimino[0] == 2:
        imagen = "2"
    elif tetrimino[0] == 3:
        imagen = "3"
    elif tetrimino[0] == 4:
        imagen = "4"
    elif tetrimino[0] == 5:
        imagen = "5"
    elif tetrimino[0] == 6:
        imagen = "6"
    elif tetrimino[0] == 7:
        imagen = "7"
    else:
        imagen = "8"


    if tetrimino[0] >= 1 and tetrimino[0] <= 6:
        for i in range(largoLista(listaArchivo)):
            contenido = []
            for j in range(largoLista(listaArchivo[0])):
                if i == x1 and j == y1:
                    contenido += [imagen]
                elif i == x2 and j == y2:
                    contenido += [imagen]
                elif i == x3 and j == y3:
                    contenido += [imagen]
                elif i == x4 and j == y4:
                    contenido += [imagen]
                else:
                    contenido += [listaArchivo[i][j]]
            nuevoContenido += [contenido]
    else:
        for i in range(largoLista(listaArchivo)):
            contenido = []
            for j in range(largoLista(listaArchivo[0])):
                if i == x1 and j == y1:
                    contenido += [imagen]
                elif i == x2 and j == y2:
                    contenido += [imagen]
                elif i == x3 and j == y3:
                    contenido += [imagen]
                elif i == x4 and j == y4:
                    contenido += [imagen]
                elif i == x5 and j == y5:
                    contenido += [imagen]
                else:
                    contenido += [listaArchivo[i][j]]
            nuevoContenido += [contenido]
    
    
    modificarArchivoJuegoXX(nombreArchivo, nuevoContenido)



def eliminarAntiguaPosicionArchivo(nombreArchivo, tetrimino, x1, x2,  x3, x4, x5, y1, y2, y3, y4, y5):
    listaArchivo = archivoALista(nombreArchivo)
    listaArchivo = eliminarSaltosDeLinea(listaArchivo)
    nuevoContenido = []
    
    if tetrimino[0] >= 1 and tetrimino[0] <= 6:
        for i in range(largoLista(listaArchivo)):
            contenido = []
            for j in range(largoLista(listaArchivo[0])):
                if i == x1 and j == y1:
                    contenido += ["0"]
                elif i == x2 and j == y2:
                    contenido += ["0"]
                elif i == x3 and j == y3:
                    contenido += ["0"]
                elif i == x4 and j == y4:
                    contenido += ["0"]
                else:
                    contenido += [listaArchivo[i][j]]
            nuevoContenido += [contenido]
    else:
        for i in range(largoLista(listaArchivo)):
            contenido = []
            for j in range(largoLista(listaArchivo[0])):
                if i == x1 and j == y1:
                    contenido += ["0"]
                elif i == x2 and j == y2:
                    contenido += ["0"]
                elif i == x3 and j == y3:
                    contenido += ["0"]
                elif i == x4 and j == y4:
                    contenido += ["0"]
                elif i == x5 and j == y5:
                    contenido += ["0"]
                else:
                    contenido += [listaArchivo[i][j]]
            nuevoContenido += [contenido]
    
    modificarArchivoJuegoXX(nombreArchivo, nuevoContenido)


def eliminarFilaArchivo(nombreArchivo):
    fila = retornarFilaArchivoDescendente(nombreArchivo)
    if fila != False: # para la fubncion de validacion
        listaArchivo = archivoALista(nombreArchivo)
        listaArchivo = eliminarSaltosDeLinea(listaArchivo)
        nuevoContenido = []
        for i in range(largoLista(listaArchivo)):
            contenido = []
            for j in range(largoLista(listaArchivo[0])):
                if i == fila:
                    if j != 0 and j != 11:
                        contenido += ["0"]
                    else:
                       contenido += [listaArchivo[i][j]]
                else:
                    contenido += [listaArchivo[i][j]]
            nuevoContenido += [contenido]

        modificarArchivoJuegoXX(nombreArchivo,nuevoContenido)
        nuevoContenido = acomodarFilasArchivo(nombreArchivo, fila)
        modificarArchivoJuegoXX(nombreArchivo, nuevoContenido)

def retornarFilaArchivoDescendente(nombreArchivo):
    listaArchivo = archivoALista(nombreArchivo)
    listaArchivo = eliminarSaltosDeLinea(listaArchivo)
    i = largoLista(listaArchivo) - 2

    while i != 0:
        contenido = []
        j = largoLista(listaArchivo[0]) - 2
        while j != 0:
            if listaArchivo[i][j] != "0":
                contenido += [listaArchivo[i][j]]
            if contenido != []:
                if largoLista(contenido) == 10:
                    return i
            j -= 1
        i -= 1
    return False


def retornarFilaArchivoAscendente(nombreArchivo):
    listaArchivo = archivoALista(nombreArchivo)
    listaArchivo = eliminarSaltosDeLinea(listaArchivo)
    i = 1
    while i !=  largoLista(listaArchivo) - 2:
        contenido = []
        j = 0
        while j !=  largoLista(listaArchivo[0]) - 2:
            if listaArchivo[i][j] != "0":
                contenido += [listaArchivo[i][j]]
            if contenido != []:
                if largoLista(contenido) == 10:
                    return i
            j += 1
        i += 1
    return False

def acomodarFilasArchivo(nombreArchivo, fila):
    listaArchivo = archivoALista(nombreArchivo)
    listaArchivo = eliminarSaltosDeLinea(listaArchivo)
    reubicar = retornarFilaArchivoAscendente(nombreArchivo)
    filaCeros = listaArchivo[fila]
    contenido = listaArchivo[reubicar]
    ultimaFila = listaArchivo[fila-1]
    nuevoContenido = []
    for i in range(largoLista(listaArchivo)):
        if i == reubicar + 1:
            nuevoContenido += [contenido]
        elif i == fila:
            nuevoContenido += [ultimaFila]
        elif i == reubicar or i == fila - 1:
            nuevoContenido += [filaCeros]
        else:
            nuevoContenido += [listaArchivo[i]]
    return nuevoContenido

eliminarFilaArchivo("juego01.txt")
def modificarMatrizIdentificadores(tetromino, x1,x2,x3,x4,x5,y1,y2,y3,y4,y5):
    global matrizIdentificadores
    nuevaMatriz = []
    for i in range(largoLista(matrizIdentificadores)):
        vector = []
        for j in range(largoLista(matrizIdentificadores[0])):
            if tetromino[0] >= 1 and tetromino[0] <= 6:
                if i == x1 and j == y1:
                    vector += [tetromino[1]]
                elif i == x2 and j == y2:
                    vector += [tetromino[2]]
                elif i == x3 and j == y3:
                    vector += [tetromino[3]]
                elif i == x4 and j == y4:
                    vector += [tetromino[4]]
                else:
                    vector += [matrizIdentificadores[i][j]]
            
            else:
                if i == x1 and j == y1:    
                    vector += [tetromino[1]]
                elif i == x2 and j == y2:
                    vector += [tetromino[2]]
                elif i == x3 and j == y3:
                    vector += [tetromino[3]]
                elif i == x4 and j == y4:
                    vector += [tetromino[4]]
                elif i == x5 and j == y5:
                    vector += [tetromino[5]]
                else:
                    vector += [matrizIdentificadores[i][j]]
            
        print(vector)
        nuevaMatriz += [vector]
    print('')
    
    matrizIdentificadores = nuevaMatriz

def eliminarFilaMatrizIdentificadores(nombreArchivo, x):
    global matrizIdentificadores
    matrizIdentificadores = x
    fila = retornarFilaArchivoDescendente(nombreArchivo)
    if fila != False: # para la fubncion de validacion
        nuevoContenido = []
        for i in range(largoLista(matrizIdentificadores)):
            contenido = []
            for j in range(largoLista(matrizIdentificadores[0])):
                if i == fila:
                    if j != 0 and j != 11:
                        contenido += ["0"]
                    else:
                       contenido += [matrizIdentificadores[i][j]]
                else:
                    contenido += [matrizIdentificadores[i][j]]
            nuevoContenido += [contenido]

        matrizIdentificadores = nuevoContenido
        acomodarFilasMatrizIdentificadores(nombreArchivo,fila)
        return True    


def acomodarFilasMatrizIdentificadores(nombreArchivo,fila):
    global matrizIdentificadores
    reubicar = retornarFilaArchivoAscendente(nombreArchivo)
    filaCeros = matrizIdentificadores[fila]
    contenido = matrizIdentificadores[reubicar]
    ultimaFila = matrizIdentificadores[fila-1]
    nuevoContenido = []
    for i in range(largoLista(matrizIdentificadores)):
        if i == reubicar + 1:
            nuevoContenido += [contenido]
        elif i == fila:
            nuevoContenido += [ultimaFila]
        elif i == reubicar or i == fila - 1:
            nuevoContenido += [filaCeros]
        else:
            nuevoContenido += [matrizIdentificadores[i]]

        print(matrizIdentificadores[i])
    matrizIdentificadores = nuevoContenido




def eliminarFilaTetris(canvasPantalla, nombreArchivo):
    global matrizIdentificadores
    fila = retornarFilaArchivoDescendente(nombreArchivo)
    for i in range(largoLista(matrizIdentificadores)):
        for j in range(largoLista(matrizIdentificadores[0])):
            if i == fila and j != 0 and j != 11:
                canvasPantalla.delete(matrizIdentificadores[i][j])
    
def refrescarPantallaTetris(canvasPantalla):
    global matrizIdentificadores
    coordenadas = posicionImagenes()
    for i in range(largoLista(matrizIdentificadores)):
        for j in range(largoLista(matrizIdentificadores[0])):
            if matrizIdentificadores[i][j] != "0" or matrizIdentificadores[i][j] != "+":
                print(matrizIdentificadores[i][j])
                canvasPantalla.coords(matrizIdentificadores[i][j], coordenadas[i][j][0] / 2, coordenadas[i][j][1] / 2)

eliminarFilaMatrizIdentificadores("juego01.txt",[
['+', '+', '+', '+', '+', '+', '+', '+', '+', '+', '+', '+'],
['+', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '+'],
['+', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '+'],
['+', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '+'],
['+', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '+'],
['+', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '+'],
['+', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '+'],
['+', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '+'],
['+', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '+'],
['+', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '+'],
['+', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '+'],
['+', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '+'],
['+', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '+'],
['+', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '+'],
['+', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '+'],
['+', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '+'],
['+', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '+'],
['+', '0', '0', '0', '0', '0', '0', '0', '0', 273, 277, '+'],
['+', '0', '0', '0', '0', '0', '0', '0', '0', 274, 278, '+'],
['+', '0', '0', '0', '0', '0', '0', '0', '0', 275, 279, '+'],
['+', 265, 266, 267, 268, 269, 270, 271, 272, 276, 280, '+'],
['+', '+', '+', '+', '+', '+', '+', '+', '+', '+', '+', '+']])

def ventanaTetris(ventana, nombreArchivo):
    global listaTetrominos, tetromino, matrizIdentificadores
    #ventana.destroy()
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


    imagenPared = Image.open("bloqueGris.png")
    imagenPared = imagenPared.resize((39, 17))
    imagenParedTk = ImageTk.PhotoImage(imagenPared)

    imagenFondo= Image.open("fondo.png")
    imagenFondo = imagenFondo.resize((39, 17))
    imagenFondoTk = ImageTk.PhotoImage(imagenFondo)

   
    canvasPantalla = Canvas(canvasGameboy, width=465, height=366, bg="pink")
    canvasPantalla.place(x=67, y=85)

    listaNombreBloques = ["bloqueAmarillo.png", 
                          "bloqueAzul.png", 
                          "bloqueNaranja.png", 
                          "bloqueRosa.png", 
                          "bloqueMorado.png", 
                          "bloqueVerde.png", 
                          "bloqueCafe.png", 
                          "bloqueRojo.png"]
    
    listaImagenesBloques = []
    for i in range(largoLista(listaNombreBloques)):
        imagen = Image.open(listaNombreBloques[i])
        imagen = imagen.resize((39, 17))
        imagenTk = ImageTk.PhotoImage(imagen)
        listaImagenesBloques += [imagenTk]

    
    imprimirArchivoTetris(canvasPantalla, nombreArchivo, imagenParedTk, imagenFondoTk)

    matrizIdentificadores = crearMatriz()
    listaTetrominos = [2,2,2,2,2,2,2,2,2,2]#crearListatetrominos()
    listaImagenes = []
    tetromino = crearTetromino(canvasPantalla, listaImagenesBloques,listaTetrominos[0])
    listaImagenes += [tetromino[1:]]
    escribirNuevaPosicionArchivo("juego01.txt", tetromino, x1,x2,x3,x4,x5,y1,y2,y3,y4,y5)

    consola.bind("<KeyPress-w>", lambda evento: rotar(canvasPantalla, tetromino, nombreArchivo))
    consola.bind("<KeyPress-s>", lambda evento: moverAbajo(canvasPantalla, listaImagenesBloques, nombreArchivo, consola))
    consola.bind("<KeyPress-d>", lambda evento: moverDerecha(canvasPantalla, nombreArchivo)) 
    consola.bind("<KeyPress-a>", lambda evento: moverIzquierda(canvasPantalla, nombreArchivo))


    canvasDemostrativo = Canvas(canvasGameboy, width=235, height=178, bg="pink")
    canvasDemostrativo.place(x=305, y=567)






    consola.protocol("WM_DELETE_WINDOW", lambda : borrarArchivo(nombreArchivo, consola))
    consola.mainloop()


"""
Nombre: salir
Entrada: ventana
Salida: Cierra (destruye) la ventana
Restricciones: Las necesarias para el correcto funcionamiento
"""
def salir(ventana):
    ventana.destroy()

#ventanaTetris(1, "juego01.txt")
# pasar nombre aerhccovp como parametro
# def invetirMatrizArchivo(nombreArchivo):
#     listaArchivo = archivoALista(nombreArchivo)
#     listaArchivo = eliminarSaltosDeLinea(listaArchivo)

#     matriz = []
#     for i in range(largoLista(listaArchivo)):
#         vector = []
#         for j in range(largoLista(listaArchivo[0])):
#             vector += [listaArchivo[i * -1][j * -1]]
#         matriz += [vector]
#     return matriz