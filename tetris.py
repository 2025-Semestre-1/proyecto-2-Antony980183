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
Nombre: sobreBoton
Entrada: evento
Salida: Cambia la imgaen del 'boton'
Restricciones: Las necesarias para el correcto funcionamiento
"""
def sobreBoton(canvas, identificador, nuevaImagen):
    canvas.itemconfig(identificador, image=nuevaImagen)


"""
Nombre: ventanaInicio
Entraeda: Ninguna
Salida: La ventana inicial, iniciara el juego o finalizara el programa
Restricciones: Las necesarias para el correcto funcionamiento
"""
def ventanaInicio():
    global imagenInicio
    ventanaInicial = Tk()   
    ventanaInicial.geometry("900x700")
    ventanaInicial.resizable(0,0)
    centrarVentana(ventanaInicial)
    
    imagenInicio = Image.open("fondoInicio.png")
    imagenInicio = imagenInicio.resize((900,700))
    imagenInicio = ImageTk.PhotoImage(imagenInicio)

    canvasInicio = Canvas(ventanaInicial, width=900, height=700)
    canvasInicio.pack(fill="both", expand=True)
    canvasInicio.create_image(0, 0, anchor="nw", image=imagenInicio)

    imagenJugar = Image.open("jugar.png")
    imagenJugar = imagenJugar.resize((120,120))
    imagenJugar = ImageTk.PhotoImage(imagenJugar)

    imagenJugarPresionado = Image.open("jugarPresionado.png")
    imagenJugarPresionado = imagenJugarPresionado.resize((120,120))
    imagenJugarPresionado= ImageTk.PhotoImage(imagenJugarPresionado)

    imagenCargar = Image.open("cargar.png")
    imagenCargar = imagenCargar.resize((120,120))
    imagenCargar = ImageTk.PhotoImage(imagenCargar)

    imagenCargarPresionado = Image.open("cargarPresionado.png")
    imagenCargarPresionado = imagenCargarPresionado.resize((120,120))
    imagenCargarPresionado= ImageTk.PhotoImage(imagenCargarPresionado)
    
    imagenEstadisticas = Image.open("estadisticas.png")
    imagenEstadisticas = imagenEstadisticas.resize((120,120))
    imagenEstadisticas = ImageTk.PhotoImage(imagenEstadisticas)

    imagenEstadisticasPresionado = Image.open("estadisticasPresionado.png")
    imagenEstadisticasPresionado = imagenEstadisticasPresionado.resize((120,120))
    imagenEstadisticasPresionado = ImageTk.PhotoImage(imagenEstadisticasPresionado)

    imagenInformacion = Image.open("informacion.png")
    imagenInformacion = imagenInformacion.resize((120,120))
    imagenInformacion = ImageTk.PhotoImage(imagenInformacion)

    imagenInformacionPresionado = Image.open("informacionPresionado.png")
    imagenInformacionPresionado = imagenInformacionPresionado.resize((120,120))
    imagenInformacionPresionado = ImageTk.PhotoImage(imagenInformacionPresionado)

    imagenSalir = Image.open("salir.png")
    imagenSalir = imagenSalir.resize((120,120))
    imagenSalir = ImageTk.PhotoImage(imagenSalir)

    imagenSalirPresionado = Image.open("salirPresionado.png")
    imagenSalirPresionado = imagenSalirPresionado.resize((120,120))
    imagenSalirPresionado = ImageTk.PhotoImage(imagenSalirPresionado)

    botonJugar = canvasInicio.create_image(30, 15, anchor="nw", image=imagenJugar)
    botonCargar =  canvasInicio.create_image(30, 150, anchor="nw", image=imagenCargar)
    botonEstadisticas =  canvasInicio.create_image(30, 285, anchor="nw", image=imagenEstadisticas) 
    botonInformacion =  canvasInicio.create_image(30, 420, anchor="nw", image=imagenInformacion) 
    botonSalir =  canvasInicio.create_image(30, 555, anchor="nw", image=imagenSalir)

    canvasInicio.tag_bind(botonJugar, "<Enter>", lambda evento: sobreBoton(canvasInicio, botonJugar, imagenJugarPresionado))
    canvasInicio.tag_bind(botonJugar, "<Leave>", lambda evento: sobreBoton(canvasInicio, botonJugar, imagenJugar))
    canvasInicio.tag_bind(botonJugar, "<Button-1>", lambda evento: comoSeleccionar(ventanaInicial))

    canvasInicio.tag_bind(botonCargar, "<Enter>", lambda evento: sobreBoton(canvasInicio, botonCargar, imagenCargarPresionado))
    canvasInicio.tag_bind(botonCargar, "<Leave>", lambda evento: sobreBoton(canvasInicio, botonCargar, imagenCargar))
    canvasInicio.tag_bind(botonCargar, "<Button-1>", lambda evento: ventanaJuegosGuardados(ventanaInicial))


    canvasInicio.tag_bind(botonEstadisticas, "<Enter>", lambda evento: sobreBoton(canvasInicio, botonEstadisticas, imagenEstadisticasPresionado))
    canvasInicio.tag_bind(botonEstadisticas, "<Leave>", lambda evento: sobreBoton(canvasInicio, botonEstadisticas, imagenEstadisticas))
    canvasInicio.tag_bind(botonEstadisticas, "<Button-1>", lambda evento: ventanaEstadisticas(ventanaInicial))


    canvasInicio.tag_bind(botonInformacion, "<Enter>", lambda evento: sobreBoton(canvasInicio, botonInformacion, imagenInformacionPresionado))
    canvasInicio.tag_bind(botonInformacion, "<Leave>", lambda evento: sobreBoton(canvasInicio, botonInformacion, imagenInformacion))
    canvasInicio.tag_bind(botonInformacion, "<Button-1>", lambda evento: ventanaInformacion(ventanaInicial))


    canvasInicio.tag_bind(botonSalir, "<Enter>", lambda evento: sobreBoton(canvasInicio, botonSalir, imagenSalirPresionado))
    canvasInicio.tag_bind(botonSalir, "<Leave>", lambda evento: sobreBoton(canvasInicio, botonSalir, imagenSalir))
    canvasInicio.tag_bind(botonSalir, "<Button-1>", lambda evento: salir(ventanaInicial))
    

    ventanaInicial.mainloop() #                                 Agregar funcionalidades de botones restantes


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
Nombre: comoSeleecionar
Entrada: ventana
Salida: Una ventana explicando como seleccionar los obstaculos
Restricciones: Las necesarias para el correcto funcionamiento
"""
def comoSeleccionar(ventana):
    ventana.destroy()

    consola = Tk()
    consola.geometry("600x800")
    consola.resizable(0,0)
    centrarVentana(consola)

    imagenGameboy = Image.open("gameboyBase.png")
    imagenGameboy = ImageTk.PhotoImage(imagenGameboy)

    canvasGameboy = Canvas(consola, width=300, height=300)
    canvasGameboy.pack(fill="both", expand=True)
    canvasGameboy.create_image(0, 0, anchor="nw", image=imagenGameboy)

    canvasPantalla = Canvas(canvasGameboy, width=465, height=366)
    canvasPantalla.place(x=67, y=85)

    imagenSeleccionObstaculo = Image.open("comoSeleccionarObstaculos.png")
    imagenSeleccionObstaculo = ImageTk.PhotoImage(imagenSeleccionObstaculo)
    canvasPantalla.create_image(0, 0, anchor="nw", image=imagenSeleccionObstaculo)

    imagenConfirmar = Image.open("confirmar.png")
    imagenConfirmar = ImageTk.PhotoImage(imagenConfirmar)

    imagenConfirmarPresionado = Image.open("confirmarPresionado.png")
    imagenConfirmarPresionado = ImageTk.PhotoImage(imagenConfirmarPresionado)

    canvasConfirmacion = Canvas(canvasGameboy, width=235, height=178)
    canvasConfirmacion.place(x=305, y=567)

    
    botonConfirmar = canvasConfirmacion.create_image(0, 0, anchor="nw", image=imagenConfirmar)

    canvasConfirmacion.tag_bind(botonConfirmar, "<Enter>", lambda evento: sobreBoton(canvasConfirmacion, botonConfirmar, imagenConfirmarPresionado))
    canvasConfirmacion.tag_bind(botonConfirmar, "<Leave>", lambda evento: sobreBoton(canvasConfirmacion, botonConfirmar, imagenConfirmar))
    canvasConfirmacion.tag_bind(botonConfirmar, "<Button-1>", lambda evento: ventanaSeleccion(consola))

    consola.mainloop()


"""
Nombre: ventanaInformacion
Entrada: ventana
Salida: Muestra distintas imagenes
Restricciones: Las necesarias para el correcto funcionamiento
"""
def ventanaInformacion(ventana):
    ventana.destroy()

    ventanaPrincipal = Tk()
    ventanaPrincipal.geometry("900x800")
    ventanaPrincipal.resizable(0,0)
    centrarVentana(ventanaPrincipal)

    canvasImagenes = Canvas(ventanaPrincipal, width=300, height=300, bg='pink')
    canvasImagenes.pack(fill="both", expand=True)

    imagenComoMoverse = Image.open("comoMoverse.png")
    imagenComoMoverse = ImageTk.PhotoImage(imagenComoMoverse)
    canvasImagenes.create_image(0, 0, anchor="nw", image=imagenComoMoverse)

    imagenComoSelecconarObstaculos = Image.open("comoSeleccionarObstaculos.png")
    imagenComoSelecconarObstaculos = ImageTk.PhotoImage(imagenComoSelecconarObstaculos)
    canvasImagenes.create_image(465, 0, anchor="nw", image=imagenComoSelecconarObstaculos)

    imagenComoGuardar = Image.open("comoGuardar.png")
    imagenComoGuardar = imagenComoGuardar.resize((900,430))
    imagenComoGuardar = ImageTk.PhotoImage(imagenComoGuardar)
    canvasImagenes.create_image(0, 366, anchor="nw", image=imagenComoGuardar)



    imagenVolver = Image.open("volver.png")
    imagenVolver = imagenVolver.resize((120,120))
    imagenVolver = ImageTk.PhotoImage(imagenVolver)

    imagenVolverPresionado = Image.open("volverPresionado.png")
    imagenVolverPresionado = imagenVolverPresionado.resize((120,120))
    imagenVolverPresionado = ImageTk.PhotoImage(imagenVolverPresionado)

    botonVolver = canvasImagenes.create_image(780,680, anchor="nw", image=imagenVolver)

    canvasImagenes.tag_bind(botonVolver, "<Enter>", lambda evento: sobreBoton(canvasImagenes, botonVolver, imagenVolverPresionado))
    canvasImagenes.tag_bind(botonVolver, "<Leave>", lambda evento: sobreBoton(canvasImagenes, botonVolver, imagenVolver))
    canvasImagenes.tag_bind(botonVolver, "<Button-1>", lambda evento: volverInicio(ventanaPrincipal))

    ventanaPrincipal.mainloop()


"""
Nombre: ventanaEstadisticas
Entrada: ventana
Salida: Muestra el top 10 de los mejores puntajes
Restricciones: Las necesatias para el correcto funcionamiento
"""
def ventanaEstadisticas(ventana):
    ventana.destroy()
    
    consola = Tk()
    consola.geometry("600x800")
    consola.resizable(0,0)
    centrarVentana(consola)

    imagenGameboy = Image.open("gameboyBase.png")
    imagenGameboy = ImageTk.PhotoImage(imagenGameboy)

    canvasGameboy = Canvas(consola, width=300, height=300)
    canvasGameboy.pack(fill="both", expand=True)
    canvasGameboy.create_image(0, 0, anchor="nw", image=imagenGameboy)
   
    framePantalla = Frame(canvasGameboy, bg="gray26", bd= 10,relief="ridge",width=470, height=368)
    framePantalla.pack_propagate(False)
    framePantalla.place(x=67, y=80)

    listaMejoresJugadores = []
    for i in range(10):
        contenido = []
        for j in range(3):
            contenido += ["vacio!"]
        listaMejoresJugadores += [contenido]

    Label(framePantalla, text="Puesto", font=("Arial", 15, "bold"),bg="gray42", bd=5 ,relief="ridge").grid(row=0,column=0, padx=24, pady=3)
    Label(framePantalla, text="Jugador", font=("Arial", 15, "bold"),bg="gray42", bd=5 ,relief="ridge").grid(row=0,column=1, padx=24, pady=3)
    Label(framePantalla, text="Puntaje Total", font=("Arial", 15, "bold"),bg="gray42", bd=5 ,relief="ridge").grid(row=0,column=2, padx=24, pady=3)

    for i  in range(largoLista(listaMejoresJugadores)):
        Label(framePantalla, text=listaMejoresJugadores[i][0], font=("Arial",10,"bold"), bg="gray52", relief="ridge").grid(row=i+1, column=0, padx=10, pady=5)
        Label(framePantalla, text=listaMejoresJugadores[i][1], font=("Arial",10,"bold"), bg="gray52", relief="ridge").grid(row=i+1, column=1, padx=10, pady=5)
        Label(framePantalla, text=listaMejoresJugadores[i][2], font=("Arial",10,"bold"), bg="gray52", relief="ridge").grid(row=i+1, column=2, padx=10, pady=5)

    imagenVolver = Image.open("volver.png")
    imagenVolver = ImageTk.PhotoImage(imagenVolver)

    imagenVolverPresionado = Image.open("volverPresionado.png")
    imagenVolverPresionado = ImageTk.PhotoImage(imagenVolverPresionado)

    canvasVolver = Canvas(canvasGameboy, width=235, height=178)
    canvasVolver.place(x=305, y=567)


    botonVolver = canvasVolver.create_image(0, 0, anchor="nw", image=imagenVolver)

    canvasVolver.tag_bind(botonVolver, "<Enter>", lambda evento: sobreBoton(canvasVolver, botonVolver, imagenVolverPresionado))
    canvasVolver.tag_bind(botonVolver, "<Leave>", lambda evento: sobreBoton(canvasVolver, botonVolver, imagenVolver))
    canvasVolver.tag_bind(botonVolver, "<Button-1>", lambda evento: volverInicio(consola))

    consola.mainloop()


"""
Nombre: ventanaJuegosGuardados
Entrada: ventana
Salida: Carga un archivo guardado
Rsetricciones: Las necesarias para el correcto funcionamiento
"""
def ventanaJuegosGuardados(ventana):
    ventana.destroy()
    
    consola = Tk()
    consola.geometry("600x800")
    consola.resizable(0,0)
    centrarVentana(consola)

    imagenGameboy = Image.open("gameboyBase.png")
    imagenGameboy = ImageTk.PhotoImage(imagenGameboy)

    canvasGameboy = Canvas(consola, width=300, height=300)
    canvasGameboy.pack(fill="both", expand=True)
    canvasGameboy.create_image(0, 0, anchor="nw", image=imagenGameboy)
   
    framePantalla = Frame(canvasGameboy, bg="gray26", bd= 10,relief="ridge",width=470, height=368)
    framePantalla.pack_propagate(False)
    framePantalla.place(x=67, y=80)

    listaMejoresJugadores = []
    for i in range(7):
        contenido = []
        for j in range(3):
            contenido += ["vacio!"]
        listaMejoresJugadores += [contenido]

    Label(framePantalla, text="Juegos Guardados", font=("Arial", 17, "bold"),bg="gray42", bd=5 ,relief="ridge").grid(row=0,column=0, padx=111, pady=3,columnspan=3)

    for i  in range(largoLista(listaMejoresJugadores)):
        for j in range(largoLista(listaMejoresJugadores[0])):
            Button(framePantalla, text=listaMejoresJugadores[i][j], font=("Arial",13,"bold"), bg="gray52", relief="ridge").grid(row=i+1, column=j, padx=10, pady=6)

    imagenVolver = Image.open("volver.png")
    imagenVolver = ImageTk.PhotoImage(imagenVolver)

    imagenVolverPresionado = Image.open("volverPresionado.png")
    imagenVolverPresionado = ImageTk.PhotoImage(imagenVolverPresionado)

    canvasVolver = Canvas(canvasGameboy, width=235, height=178)
    canvasVolver.place(x=305, y=567)

    botonVolver = canvasVolver.create_image(0, 0, anchor="nw", image=imagenVolver)

    canvasVolver.tag_bind(botonVolver, "<Enter>", lambda evento: sobreBoton(canvasVolver, botonVolver, imagenVolverPresionado))
    canvasVolver.tag_bind(botonVolver, "<Leave>", lambda evento: sobreBoton(canvasVolver, botonVolver, imagenVolver))
    canvasVolver.tag_bind(botonVolver, "<Button-1>", lambda evento: volverInicio(consola))

    consola.mainloop()

"""
Nombre: volverInicio
Entrada: ventana
Salida: Retorna la ventana principal
Restricciones: Las necesarias para el correcto funcionamiento
"""
def volverInicio(ventana):
    ventana.destroy()
    return ventanaInicio()

#logiva # game
"""
Nombre: seleccionDeObstaculos
Entrada: canvasPantalla,imagenPared, imagenFondo, imagenFondoSeleccionado, nombreArchivo
Salida: Crea una 'matriz' donde el ususario seleccionara los osbtaculos del tetriz
Restricciones: Las necesarias paraa el correcto funcionamiento
"""
def seleccionDeObstaculos(canvasPantalla,imagenPared,imagenFondo, imagenFondoSeleccionado, nombreArchivo):
    coordenadas = posicionImagenes()
    matrizIdentificadores = []
    for fila in range (22):
        vectorIdentificadores = []
        for columna in range(12):
            if fila == 0 or fila == 21:
                area_fondo = canvasPantalla.create_image(coordenadas[fila][columna][0], coordenadas[fila][columna][1], anchor="center", image=imagenPared)
            else:
                if columna == 0 or columna == 11:
                    area_fondo = canvasPantalla.create_image(coordenadas[fila][columna][0], coordenadas[fila][columna][1] , anchor="center", image=imagenPared)
                else:
                    area_fondo = canvasPantalla.create_image(coordenadas[fila][columna][0], coordenadas[fila][columna][1], anchor="center", image=imagenFondo)
            
                    canvasPantalla.tag_bind(area_fondo, "<Button-1>", lambda evento:seleccionarObstaculo(canvasPantalla, evento, imagenFondoSeleccionado, matrizIdentificadores, nombreArchivo))
                    canvasPantalla.tag_bind(area_fondo, "<Button-3>", lambda evento:quitarObstaculo(canvasPantalla, evento, imagenFondo, matrizIdentificadores, nombreArchivo))
        
            vectorIdentificadores += [area_fondo]
                

        matrizIdentificadores += [vectorIdentificadores]


"""
Nombre: posicionImagenes
Entrada: ninguna
Salida: Una matriz con las coordenadas donde se ubicaran las imagenes
Restricciones: Las necesarias para el correcto funcionamiento
"""
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
            posiciones += [[(x1 + x2) / 2, (y1 + y2) / 2]]
        coordenadas += [posiciones]
    return coordenadas


"""
Nombre: seleccionarObstaculo
Entrada: canva, evento, imagen, matrizIdentificadores, nombreArchivo
Salida: Cambia el contenido del archivo por un caracter de '+' segun la posicion indicada
Restriccioene: Las necesarias para el correceto funcionamiento
"""
def seleccionarObstaculo(canva, evento, imagen, matrizIdentificadores, nombreArchivo):
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
    if not isinstance(nombreArchivo, str):
        print("Error: Debe ingresar una cadena de texto!")
    elif not isinstance(contenido, list):
        print("Error: El contenido debe ser del tipo lista!")
    elif nombreArchivo == "":
        print("Error: El nombre del archivo esta vacio!")
    elif contenido == []:
        print("Error: El contenido de la lista esta vacio!")
    else:
        return modificarArchivoJuegoXXAux(nombreArchivo, contenido)
def modificarArchivoJuegoXXAux(nombreArchivo, contenido):
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
    for i in range(largoLista(matrizIdentificadores)):
        for j in range(largoLista(matrizIdentificadores[0])):
            if matrizIdentificadores[i][j] == elemento:
                coordenadas = [i,j]
                return coordenadas


"""
Nombre: ventanaSeleccion 
Entrada: ventana
Salida: La creacion de nuevas ventanas(una matriz interactiva y una ventana de demostracion) junto con sus respectivos widgets
Restricciones: Las necesarias para el correcto funcionamiento
"""
def ventanaSeleccion(ventana):
    nombreArchivo = crearArchivoJuegoXX()
    crearMatrizArchivoJuegoXX(nombreArchivo)
    ventana.destroy()
    
    consola = Tk()
    consola.geometry("600x800")
    consola.resizable(0,0)
    centrarVentana(consola)

    imagenGameboy = Image.open("gameboyBase.png")
    imagenGameboy = ImageTk.PhotoImage(imagenGameboy)

    canvasGameboy = Canvas(consola, width=300, height=300)
    canvasGameboy.pack(fill="both", expand=True)
    canvasGameboy.create_image(0, 0, anchor="nw", image=imagenGameboy)
   
    canvasPantalla = Canvas(canvasGameboy, width=465, height=366)
    canvasPantalla.place(x=67, y=85)

    imagenPared = Image.open("bloqueGris.png")
    imagenPared = imagenPared.resize((39, 17))
    imagenPared = ImageTk.PhotoImage(imagenPared)

    imagenFondo= Image.open("fondo.png")
    imagenFondo = imagenFondo.resize((39, 17))
    imagenFondo = ImageTk.PhotoImage(imagenFondo)

    imagenFondoSeleccionado = Image.open("fondoSeleccionado.png")
    imagenFondoSeleccionado = imagenFondoSeleccionado.resize((39, 17))
    imagenFondoSeleccionado = ImageTk.PhotoImage(imagenFondoSeleccionado)

    imagenConfirmar = Image.open("confirmar.png")
    imagenConfirmar = ImageTk.PhotoImage(imagenConfirmar)

    imagenConfirmarPresionado = Image.open("confirmarPresionado.png")
    imagenConfirmarPresionado = ImageTk.PhotoImage(imagenConfirmarPresionado)

    seleccionDeObstaculos(canvasPantalla,imagenPared,imagenFondo, imagenFondoSeleccionado, nombreArchivo)

    canvasConfirmacion = Canvas(canvasGameboy, width=235, height=178)
    canvasConfirmacion.place(x=305, y=567)

    botonConfirmar = canvasConfirmacion.create_image(0, 0, anchor="nw", image=imagenConfirmar)

    canvasConfirmacion.tag_bind(botonConfirmar, "<Enter>", lambda evento: sobreBoton(canvasConfirmacion, botonConfirmar, imagenConfirmarPresionado))
    canvasConfirmacion.tag_bind(botonConfirmar, "<Leave>", lambda evento: sobreBoton(canvasConfirmacion, botonConfirmar, imagenConfirmar))
    canvasConfirmacion.tag_bind(botonConfirmar, "<Button-1>", lambda evento: ventanaTetris(consola,nombreArchivo))

    consola.protocol("WM_DELETE_WINDOW", lambda : borrarArchivo(nombreArchivo, consola))
    consola.mainloop()

"""
Nombre: ventanaTetris
Entrada: ventana, nomberArchivo
Salida: El juego tetris de forma 'funcional'
Restricciones: Las necesarias para el correcto funcionamiento
"""
def ventanaTetris(ventana, nombreArchivo):
    #global listaTetrominos, tetromino, matrizIdentificadores
    ventana.destroy()
    consola = Tk()
    consola.geometry("600x800")
    consola.resizable(0,0)
    centrarVentana(consola)

    imagenGameboy = Image.open("gameboyBase.png")
    imagenGameboy = ImageTk.PhotoImage(imagenGameboy)

    canvasGameboy = Canvas(consola, width=300, height=300)
    canvasGameboy.pack(fill="both", expand=True)
    canvasGameboy.create_image(0, 0, anchor="nw", image=imagenGameboy)


    imagenPared = Image.open("bloqueGris.png")
    imagenPared = imagenPared.resize((39, 17))
    imagenPared = ImageTk.PhotoImage(imagenPared)

    imagenFondo= Image.open("fondo.png")
    imagenFondo = imagenFondo.resize((39, 17))
    imagenFondo = ImageTk.PhotoImage(imagenFondo)

    imagenFondoTetris = Image.open("fondoTetris.png")
    imagenFondoTetris = imagenFondoTetris.resize((446, 358))
    imagenFondoTetris = ImageTk.PhotoImage(imagenFondoTetris)

    canvasPantalla = Canvas(canvasGameboy, width=465, height=366, bg="pink")
    canvasPantalla.place(x=67, y=85)

    canvasDemostrativo = Canvas(canvasGameboy, width=235, height=178, bg="pink")
    canvasDemostrativo.place(x=305, y=567)

    #globales
    coordenadas = posicionImagenes()
    listaTetrominos = crearListaTetrominos()

    """
    Nombre: crearListaImagenesBloque
    Entrada: ninguna
    Salida: Una lista con los identificadores de las imagenes de bloques
    Restricciones: Las necesarias para el correcto funcionamiento
    """
    def crearListaImagenesBloques():
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
            imagen = ImageTk.PhotoImage(imagen)
            listaImagenesBloques += [imagen]
        return listaImagenesBloques
    listaImagenesBloques = crearListaImagenesBloques()
        
    
    """
    Nombre: imprimirArchivoTetris
    Entrada: ninguna
    Salida: El contenido del archivo imprimido en la ventana
    Restricciones: Las necesarias para el correcto funcionamiento
    """
    def imprimirArchivoTetris():
        coordenadas = posicionImagenes()
        listaArchivo = archivoALista(nombreArchivo)
        listaArchivo = eliminarSaltosDeLinea(listaArchivo)
        canvasPantalla.create_image(19, 8, anchor="nw", image=imagenFondoTetris)
        print(coordenadas[0][0])
        for i in range(largoLista(listaArchivo)):
            for j in range(largoLista(listaArchivo[0])):
                if listaArchivo[i][j] == "+": 
                    canvasPantalla.create_image(coordenadas[i][j][0], coordenadas[i][j][1], anchor="center", image=imagenPared)
                elif listaArchivo[i][j] == "1": 
                     canvasPantalla.create_image(coordenadas[i][j][0], coordenadas[i][j][1], anchor="center", image=listaImagenesBloques[0])
                elif listaArchivo[i][j] == "2": 
                     canvasPantalla.create_image(coordenadas[i][j][0], coordenadas[i][j][1], anchor="center", image=listaImagenesBloques[1])
                elif listaArchivo[i][j] == "3": 
                     canvasPantalla.create_image(coordenadas[i][j][0], coordenadas[i][j][1], anchor="center", image=listaImagenesBloques[2])
                elif listaArchivo[i][j] == "4": 
                     canvasPantalla.create_image(coordenadas[i][j][0], coordenadas[i][j][1], anchor="center", image=listaImagenesBloques[3])
                elif listaArchivo[i][j] == "5": 
                     canvasPantalla.create_image(coordenadas[i][j][0], coordenadas[i][j][1], anchor="center", image=listaImagenesBloques[4])
                elif listaArchivo[i][j] == "6": 
                     canvasPantalla.create_image(coordenadas[i][j][0], coordenadas[i][j][1], anchor="center", image=listaImagenesBloques[5])
                elif listaArchivo[i][j] == "7": 
                     canvasPantalla.create_image(coordenadas[i][j][0], coordenadas[i][j][1], anchor="center", image=listaImagenesBloques[6])
                elif listaArchivo[i][j] == "8": 
                     canvasPantalla.create_image(coordenadas[i][j][0], coordenadas[i][j][1], anchor="center", image=listaImagenesBloques[7])
    imprimirArchivoTetris()
    # matrizIdentificadores = crearMatriz()


    """
    Nombre: crearListaTetrominos
    Entrada: ninguna
    Salida: Una lista con las primeras 30 piezas del tetris
    Restricciones: Las necesarias para el correcto funcionamiento
    """
    def crearListaTetrominos():
        listatetrominos = []
        for i in range(30):
            listatetrominos += [random.randint(1,8)]
        return listatetrominos
    

    """
    Nombre: crearTetromino
    Entrada: ninguna
    Salida: Una lista tetromino
    Restricciones: LAs necesarias para el correcto funcionamiento
    """
    def crearTetromino():
        if listaTetrominos[0] == 1:
            return crearTetrominoO()
        elif listaTetrominos[0] == 2:
            return crearTetrominoI()
        elif listaTetrominos[0] == 3:
            return crearTetrominoL()
        elif listaTetrominos[0] == 4:
            return crearTetrominoJ()
        elif listaTetrominos[0] == 5:
            return crearTetrominoT()
        elif listaTetrominos[0] == 6:
            return crearTetrominoZ()
        elif listaTetrominos[0] == 7:
            return crearTetrominoU()
        else:
            return crearTetrominoCruz()
        

    """
    Nombre: crearTetrominoO
    Entrada: ninguna
    Salida: El tetromino 'O' mostrado en pantalla
    Restricciones: Las necesarias para el correcto funcionamiento
    """    
    def crearTetrominoO():
        bloque1 = canvasPantalla.create_image(coordenadas[1][5][0], coordenadas[1][5][1], anchor="center", image=listaImagenesBloques[0])
        bloque2 = canvasPantalla.create_image(coordenadas[1][6][0], coordenadas[1][6][1], anchor="center", image=listaImagenesBloques[0])
        bloque3 = canvasPantalla.create_image(coordenadas[2][5][0], coordenadas[2][5][1], anchor="center", image=listaImagenesBloques[0])
        bloque4 = canvasPantalla.create_image(coordenadas[2][6][0], coordenadas[2][6][1], anchor="center", image=listaImagenesBloques[0])
        
        posicionesX = [1, 1, 2, 2, 0]
        posicionesY = [5, 6, 5, 6, 0]
        tetromino = [posicionesX, posicionesY, bloque1, bloque2, bloque3, bloque4]
        return tetromino
    
    
    """
    Nombre: crearTetrominoI
    Entrada: ninguna
    Salida: El tetromino 'I' mostrado en pantalla
    Restricciones: Las necesarias para el correcto funcionamiento
    """      
    def crearTetrominoI():
        bloque1 = canvasPantalla.create_image(coordenadas[1][4][0], coordenadas[1][4][1], anchor="center", image=listaImagenesBloques[1])
        bloque2 = canvasPantalla.create_image(coordenadas[1][5][0], coordenadas[1][5][1], anchor="center", image=listaImagenesBloques[1])
        bloque3 = canvasPantalla.create_image(coordenadas[1][6][0], coordenadas[1][6][1], anchor="center", image=listaImagenesBloques[1])
        bloque4 = canvasPantalla.create_image(coordenadas[1][7][0], coordenadas[1][7][1], anchor="center", image=listaImagenesBloques[1])
        
        posicionesX = [1, 1, 1, 1, 0]
        posicionesY = [4, 5, 6, 7, 0]
        tetromino = [posicionesX, posicionesY, bloque1, bloque2, bloque3, bloque4]
        return tetromino
    

    """
    Nombre: crearTetrominoL
    Entrada: ninguna
    Salida: El tetromino 'L' mostrado en pantalla
    Restricciones: Las necesarias para el correcto funcionamiento
    """     
    def crearTetrominoL():
        bloque1 = canvasPantalla.create_image(coordenadas[2][4][0], coordenadas[2][4][1], anchor="center", image=listaImagenesBloques[2])
        bloque2 = canvasPantalla.create_image(coordenadas[2][5][0], coordenadas[2][5][1], anchor="center", image=listaImagenesBloques[2])
        bloque3 = canvasPantalla.create_image(coordenadas[2][6][0], coordenadas[2][6][1], anchor="center", image=listaImagenesBloques[2])
        bloque4 = canvasPantalla.create_image(coordenadas[1][6][0], coordenadas[1][6][1], anchor="center", image=listaImagenesBloques[2])
        
        posicionesX = [2, 2, 2, 1, 0]
        posicionesY = [4, 5, 6, 6, 0]
        tetromino = [posicionesX, posicionesY, bloque1, bloque2, bloque3, bloque4]
        return tetromino
    

    """
    Nombre: crearTetrominoJ
    Entrada: ninguna
    Salida: El tetromino 'J' mostrado en pantalla
    Restricciones: Las necesarias para el correcto funcionamiento
    """      
    def crearTetrominoJ():
        bloque1 = canvasPantalla.create_image(coordenadas[1][4][0], coordenadas[1][4][1], anchor="center", image=listaImagenesBloques[3])
        bloque2 = canvasPantalla.create_image(coordenadas[2][4][0], coordenadas[2][4][1], anchor="center", image=listaImagenesBloques[3])
        bloque3 = canvasPantalla.create_image(coordenadas[2][5][0], coordenadas[2][5][1], anchor="center", image=listaImagenesBloques[3])
        bloque4 = canvasPantalla.create_image(coordenadas[2][6][0], coordenadas[2][6][1], anchor="center", image=listaImagenesBloques[3])
        
        posicionesX = [1, 2, 2, 2, 0]
        posicionesY = [4, 4, 5, 6, 0]
        tetromino = [posicionesX, posicionesY, bloque1, bloque2, bloque3, bloque4]
        return tetromino       
    

    """
    Nombre: crearTetrominoT
    Entrada: ninguna
    Salida: El tetromino 'T' mostrado en pantalla
    Restricciones: Las necesarias para el correcto funcionamiento
    """  
    def crearTetrominoT():
        bloque1 = canvasPantalla.create_image(coordenadas[2][4][0], coordenadas[2][4][1], anchor="center", image=listaImagenesBloques[4])
        bloque2 = canvasPantalla.create_image(coordenadas[2][5][0], coordenadas[2][5][1], anchor="center", image=listaImagenesBloques[4])
        bloque3 = canvasPantalla.create_image(coordenadas[2][6][0], coordenadas[2][6][1], anchor="center", image=listaImagenesBloques[4])
        bloque4 = canvasPantalla.create_image(coordenadas[1][5][0], coordenadas[1][5][1], anchor="center", image=listaImagenesBloques[4])

        posicionesX = [2, 2, 2, 1, 0]
        posicionesY = [4, 5, 6, 5, 0]
        tetromino = [posicionesX, posicionesY, bloque1, bloque2, bloque3, bloque4]
        return tetromino
    

    """
    Nombre: crearTetrominoZ
    Entrada: ninguna
    Salida: El tetromino 'Z' mostrado en pantalla
    Restricciones: Las necesarias para el correcto funcionamiento
    """  
    def crearTetrominoZ():
        bloque1 = canvasPantalla.create_image(coordenadas[1][5][0], coordenadas[1][5][1], anchor="center", image=listaImagenesBloques[5])
        bloque2 = canvasPantalla.create_image(coordenadas[1][6][0], coordenadas[1][6][1], anchor="center", image=listaImagenesBloques[5])
        bloque3 = canvasPantalla.create_image(coordenadas[2][6][0], coordenadas[2][6][1], anchor="center", image=listaImagenesBloques[5])
        bloque4 = canvasPantalla.create_image(coordenadas[2][7][0], coordenadas[2][7][1], anchor="center", image=listaImagenesBloques[5])

        posicionesX = [1, 1, 2, 2, 0]
        posicionesY = [5, 6, 6, 7, 0]
        tetromino = [posicionesX, posicionesY, bloque1, bloque2, bloque3, bloque4]
        return tetromino
    

    """
    Nombre: crearTetrominoU
    Entrada: ninguna
    Salida: El tetromino 'U' mostrado en pantalla
    Restricciones: Las necesarias para el correcto funcionamiento
    """  
    def crearTetrominoU():
        bloque1 = canvasPantalla.create_image(coordenadas[1][4][0], coordenadas[1][4][1], anchor="center", image=listaImagenesBloques[6])
        bloque2 = canvasPantalla.create_image(coordenadas[2][4][0], coordenadas[2][4][1], anchor="center", image=listaImagenesBloques[6])
        bloque3 = canvasPantalla.create_image(coordenadas[2][5][0], coordenadas[2][5][1], anchor="center", image=listaImagenesBloques[6])
        bloque4 = canvasPantalla.create_image(coordenadas[2][6][0], coordenadas[2][6][1], anchor="center", image=listaImagenesBloques[6])
        bloque5 = canvasPantalla.create_image(coordenadas[1][6][0], coordenadas[1][6][1], anchor="center", image=listaImagenesBloques[6])

        posicionesX = [1, 2, 2, 2, 1]
        posicionesY = [4, 4, 5, 6, 6]
        tetromino = [posicionesX, posicionesY, bloque1, bloque2, bloque3, bloque4, bloque5]
        return tetromino
    

    """
    Nombre: crearTetrominoCruz
    Entrada: ninguna
    Salida: El tetromino '+' mostrado en pantalla
    Restricciones: Las necesarias para el correcto funcionamiento
    """  
    def crearTetrominoCruz():
        bloque1 = canvasPantalla.create_image(coordenadas[2][4][0]/ 2, coordenadas[2][4][1] / 2, anchor="center", image=listaImagenesBloques[7])
        bloque2 = canvasPantalla.create_image(coordenadas[1][5][0]/ 2, coordenadas[1][5][1] / 2, anchor="center", image=listaImagenesBloques[7])
        bloque3 = canvasPantalla.create_image(coordenadas[2][5][0]/ 2, coordenadas[2][5][1] / 2, anchor="center", image=listaImagenesBloques[7])
        bloque4 = canvasPantalla.create_image(coordenadas[3][5][0]/ 2, coordenadas[3][5][1] / 2, anchor="center", image=listaImagenesBloques[7])
        bloque5 = canvasPantalla.create_image(coordenadas[2][6][0]/ 2, coordenadas[2][6][1] / 2, anchor="center", image=listaImagenesBloques[7])

        posicionesX = [2, 1, 2, 3, 2]
        posicionesY = [4, 5, 5, 5, 6]
        tetromino = [posicionesX, posicionesY, bloque1, bloque2, bloque3, bloque4, bloque5]
        return tetromino


    consola.bind("<KeyPress-w>", lambda evento: rotar())
    consola.bind("<KeyPress-s>", lambda evento: moverAbajo())
    consola.bind("<KeyPress-d>", lambda evento: moverDerecha()) 
    consola.bind("<KeyPress-a>", lambda evento: moverIzquierda())
 #escribirNuevaPosicionArchivo("juego01.txt", tetromino, x1,x2,x3,x4,x5,y1,y2,y3,y4,y5)
    tetrmino = crearTetromino()
    print(tetrmino)
    consola.protocol("WM_DELETE_WINDOW", lambda : borrarArchivo(nombreArchivo, consola))
    consola.mainloop()

    # def moverAbajo(canvasPantalla, listaImagenesBloques, nombreArchivo, consola):
    #     global x1, x2,  x3, x4, x5, listaTetrominos, tetromino, rotaciones
    #     eliminarAntiguaPosicionArchivo(nombreArchivo, tetromino, x1,x2,x3,x4,x5,y1,y2,y3,y4,y5)
    #     x1 +=1
    #     x2 +=1
    #     x3 +=1
    #     x4 +=1
    #     x5 +=1
    #     coordenadas = posicionImagenes()
    #     if validarMovimiento(nombreArchivo, tetromino) == False:
    #         x1 -=1
    #         x2 -=1
    #         x3 -=1
    #         x4 -=1
    #         x5 -=1
    #         escribirNuevaPosicionArchivo(nombreArchivo, tetromino, x1,x2,x3,x4,x5,y1,y2,y3,y4,y5)
    #         modificarMatrizIdentificadores(tetromino,x1,x2,x3,x4,x5,y1,y2,y3,y4,y5)
            
    #         eliminarFilaTetris(canvasPantalla, nombreArchivo)
    #         eliminar = eliminarFilaMatrizIdentificadores(nombreArchivo)
    #         if eliminar == True:
    #             consola.after(500, refrescarPantallaTetris(canvasPantalla))

    #         eliminarFilaArchivo(nombreArchivo)
            
    #         listaTetrominos = listaTetrominos[1:]
    #         tetromino = crearTetromino(canvasPantalla, listaImagenesBloques, listaTetrominos[0])
    #         rotaciones = 1
    #     else:
    #         if tetromino[0] == 1:
    #             canvasPantalla.coords(tetromino[1],(coordenadas[x1][y1][0]/ 2, coordenadas[x1][y1][1] / 2))
    #             canvasPantalla.coords(tetromino[2],(coordenadas[x2][y2][0]/ 2, coordenadas[x2][y2][1] / 2))
    #             canvasPantalla.coords(tetromino[3],(coordenadas[x3][y3][0]/ 2, coordenadas[x3][y3][1] / 2))
    #             canvasPantalla.coords(tetromino[4],(coordenadas[x4][y4][0]/ 2, coordenadas[x4][y4][1] / 2))
    #         elif tetromino[0] == 2:
    #             canvasPantalla.coords(tetromino[1],(coordenadas[x1][y1][0]/ 2, coordenadas[x1][y1][1] / 2))
    #             canvasPantalla.coords(tetromino[2],(coordenadas[x2][y2][0]/ 2, coordenadas[x2][y2][1] / 2))
    #             canvasPantalla.coords(tetromino[3],(coordenadas[x3][y3][0]/ 2, coordenadas[x3][y3][1] / 2))
    #             canvasPantalla.coords(tetromino[4],(coordenadas[x4][y4][0]/ 2, coordenadas[x4][y4][1] / 2))
    #         elif tetromino[0] == 3:
    #             canvasPantalla.coords(tetromino[1],(coordenadas[x1][y1][0]/ 2, coordenadas[x1][y1][1] / 2))
    #             canvasPantalla.coords(tetromino[2],(coordenadas[x2][y2][0]/ 2, coordenadas[x2][y2][1] / 2))
    #             canvasPantalla.coords(tetromino[3],(coordenadas[x3][y3][0]/ 2, coordenadas[x3][y3][1] / 2))
    #             canvasPantalla.coords(tetromino[4],(coordenadas[x4][y4][0]/ 2, coordenadas[x4][y4][1] / 2))
    #         elif tetromino[0] == 4:
    #             canvasPantalla.coords(tetromino[1],(coordenadas[x1][y1][0]/ 2, coordenadas[x1][y1][1] / 2))
    #             canvasPantalla.coords(tetromino[2],(coordenadas[x2][y2][0]/ 2, coordenadas[x2][y2][1] / 2))
    #             canvasPantalla.coords(tetromino[3],(coordenadas[x3][y3][0]/ 2, coordenadas[x3][y3][1] / 2))
    #             canvasPantalla.coords(tetromino[4],(coordenadas[x4][y4][0]/ 2, coordenadas[x4][y4][1] / 2))
    #         elif tetromino[0] == 5:
    #             canvasPantalla.coords(tetromino[1],(coordenadas[x1][y1][0]/ 2, coordenadas[x1][y1][1] / 2))
    #             canvasPantalla.coords(tetromino[2],(coordenadas[x2][y2][0]/ 2, coordenadas[x2][y2][1] / 2))
    #             canvasPantalla.coords(tetromino[3],(coordenadas[x3][y3][0]/ 2, coordenadas[x3][y3][1] / 2))
    #             canvasPantalla.coords(tetromino[4],(coordenadas[x4][y4][0]/ 2, coordenadas[x4][y4][1] / 2))
    #         elif tetromino[0] == 6:
    #             canvasPantalla.coords(tetromino[1],(coordenadas[x1][y1][0]/ 2, coordenadas[x1][y1][1] / 2))
    #             canvasPantalla.coords(tetromino[2],(coordenadas[x2][y2][0]/ 2, coordenadas[x2][y2][1] / 2))
    #             canvasPantalla.coords(tetromino[3],(coordenadas[x3][y3][0]/ 2, coordenadas[x3][y3][1] / 2))
    #             canvasPantalla.coords(tetromino[4],(coordenadas[x4][y4][0]/ 2, coordenadas[x4][y4][1] / 2))
    #         elif tetromino[0] == 7:
    #             canvasPantalla.coords(tetromino[1],(coordenadas[x1][y1][0]/ 2, coordenadas[x1][y1][1] / 2))
    #             canvasPantalla.coords(tetromino[2],(coordenadas[x2][y2][0]/ 2, coordenadas[x2][y2][1] / 2))
    #             canvasPantalla.coords(tetromino[3],(coordenadas[x3][y3][0]/ 2, coordenadas[x3][y4][1] / 2))
    #             canvasPantalla.coords(tetromino[4],(coordenadas[x4][y4][0]/ 2, coordenadas[x4][y4][1] / 2))
    #             canvasPantalla.coords(tetromino[5],(coordenadas[x5][y5][0]/ 2, coordenadas[x5][y5][1] / 2))        
    #         else:
    #             canvasPantalla.coords(tetromino[1],(coordenadas[x1][y1][0]/ 2, coordenadas[x1][y1][1] / 2))
    #             canvasPantalla.coords(tetromino[2],(coordenadas[x2][y2][0]/ 2, coordenadas[x2][y2][1] / 2))
    #             canvasPantalla.coords(tetromino[3],(coordenadas[x3][y3][0]/ 2, coordenadas[x3][y4][1] / 2))
    #             canvasPantalla.coords(tetromino[4],(coordenadas[x4][y4][0]/ 2, coordenadas[x4][y4][1] / 2))
    #             canvasPantalla.coords(tetromino[5],(coordenadas[x5][y5][0]/ 2, coordenadas[x5][y5][1] / 2))
    #         escribirNuevaPosicionArchivo(nombreArchivo, tetromino, x1,x2,x3,x4,x5,y1,y2,y3,y4,y5)

    # def moverDerecha(canvasPantalla, nombreArchivo): 
    #     global y1, y2, y3, y4, y5, tetromino
    #     eliminarAntiguaPosicionArchivo(nombreArchivo, tetromino, x1,x2,x3,x4,x5,y1,y2,y3,y4,y5)
    #     y1 +=1
    #     y2 +=1
    #     y3 +=1
    #     y4 +=1
    #     y5 +=1
    #     coordenadas = posicionImagenes()
    #     if validarMovimiento(nombreArchivo, tetromino) == False:
    #         y1 -=1
    #         y2 -=1
    #         y3 -=1
    #         y4 -=1
    #         y5 -=1
    #     else:
    #         if tetromino[0] == 1:
    #             canvasPantalla.coords(tetromino[1],(coordenadas[x1][y1][0]/ 2, coordenadas[x1][y1][1] / 2))
    #             canvasPantalla.coords(tetromino[2],(coordenadas[x2][y2][0]/ 2, coordenadas[x2][y2][1] / 2))
    #             canvasPantalla.coords(tetromino[3],(coordenadas[x3][y3][0]/ 2, coordenadas[x3][y3][1] / 2))
    #             canvasPantalla.coords(tetromino[4],(coordenadas[x4][y4][0]/ 2, coordenadas[x4][y4][1] / 2))
    #         elif tetromino[0] == 2:
    #             canvasPantalla.coords(tetromino[1],(coordenadas[x1][y1][0]/ 2, coordenadas[x1][y1][1] / 2))
    #             canvasPantalla.coords(tetromino[2],(coordenadas[x2][y2][0]/ 2, coordenadas[x2][y2][1] / 2))
    #             canvasPantalla.coords(tetromino[3],(coordenadas[x3][y3][0]/ 2, coordenadas[x3][y3][1] / 2))
    #             canvasPantalla.coords(tetromino[4],(coordenadas[x4][y4][0]/ 2, coordenadas[x4][y4][1] / 2))
    #         elif tetromino[0] == 3:
    #             canvasPantalla.coords(tetromino[1],(coordenadas[x1][y1][0]/ 2, coordenadas[x1][y1][1] / 2))
    #             canvasPantalla.coords(tetromino[2],(coordenadas[x2][y2][0]/ 2, coordenadas[x2][y2][1] / 2))
    #             canvasPantalla.coords(tetromino[3],(coordenadas[x3][y3][0]/ 2, coordenadas[x3][y3][1] / 2))
    #             canvasPantalla.coords(tetromino[4],(coordenadas[x4][y4][0]/ 2, coordenadas[x4][y4][1] / 2))
    #         elif tetromino[0] == 4:
    #             canvasPantalla.coords(tetromino[1],(coordenadas[x1][y1][0]/ 2, coordenadas[x1][y1][1] / 2))
    #             canvasPantalla.coords(tetromino[2],(coordenadas[x2][y2][0]/ 2, coordenadas[x2][y2][1] / 2))
    #             canvasPantalla.coords(tetromino[3],(coordenadas[x3][y3][0]/ 2, coordenadas[x3][y3][1] / 2))
    #             canvasPantalla.coords(tetromino[4],(coordenadas[x4][y4][0]/ 2, coordenadas[x4][y4][1] / 2))
    #         elif tetromino[0] == 5:
    #             canvasPantalla.coords(tetromino[1],(coordenadas[x1][y1][0]/ 2, coordenadas[x1][y1][1] / 2))
    #             canvasPantalla.coords(tetromino[2],(coordenadas[x2][y2][0]/ 2, coordenadas[x2][y2][1] / 2))
    #             canvasPantalla.coords(tetromino[3],(coordenadas[x3][y3][0]/ 2, coordenadas[x3][y3][1] / 2))
    #             canvasPantalla.coords(tetromino[4],(coordenadas[x4][y4][0]/ 2, coordenadas[x4][y4][1] / 2))
    #         elif tetromino[0] == 6:
    #             canvasPantalla.coords(tetromino[1],(coordenadas[x1][y1][0]/ 2, coordenadas[x1][y1][1] / 2))
    #             canvasPantalla.coords(tetromino[2],(coordenadas[x2][y2][0]/ 2, coordenadas[x2][y2][1] / 2))
    #             canvasPantalla.coords(tetromino[3],(coordenadas[x3][y3][0]/ 2, coordenadas[x3][y3][1] / 2))
    #             canvasPantalla.coords(tetromino[4],(coordenadas[x4][y4][0]/ 2, coordenadas[x4][y4][1] / 2))
    #         elif tetromino[0] == 7:
    #             canvasPantalla.coords(tetromino[1],(coordenadas[x1][y1][0]/ 2, coordenadas[x1][y1][1] / 2))
    #             canvasPantalla.coords(tetromino[2],(coordenadas[x2][y2][0]/ 2, coordenadas[x2][y2][1] / 2))
    #             canvasPantalla.coords(tetromino[3],(coordenadas[x3][y3][0]/ 2, coordenadas[x3][y4][1] / 2))
    #             canvasPantalla.coords(tetromino[4],(coordenadas[x4][y4][0]/ 2, coordenadas[x4][y4][1] / 2))
    #             canvasPantalla.coords(tetromino[5],(coordenadas[x5][y5][0]/ 2, coordenadas[x5][y5][1] / 2))        
    #         else:
    #             canvasPantalla.coords(tetromino[1],(coordenadas[x1][y1][0]/ 2, coordenadas[x1][y1][1] / 2))
    #             canvasPantalla.coords(tetromino[2],(coordenadas[x2][y2][0]/ 2, coordenadas[x2][y2][1] / 2))
    #             canvasPantalla.coords(tetromino[3],(coordenadas[x3][y3][0]/ 2, coordenadas[x3][y4][1] / 2))
    #             canvasPantalla.coords(tetromino[4],(coordenadas[x4][y4][0]/ 2, coordenadas[x4][y4][1] / 2))
    #             canvasPantalla.coords(tetromino[5],(coordenadas[x5][y5][0]/ 2, coordenadas[x5][y5][1] / 2))
    #         escribirNuevaPosicionArchivo(nombreArchivo, tetromino, x1,x2,x3,x4,x5,y1,y2,y3,y4,y5)


    # def moverIzquierda(canvasPantalla, nombreArchivo): 
    #     global y1, y2, y3, y4, y5, tetromino
    #     eliminarAntiguaPosicionArchivo(nombreArchivo, tetromino, x1,x2,x3,x4,x5,y1,y2,y3,y4,y5)
    #     y1 -=1
    #     y2 -=1
    #     y3 -=1
    #     y4 -=1
    #     y5 -=1
    #     coordenadas = posicionImagenes()
    #     if validarMovimiento(nombreArchivo, tetromino) == False:
    #         y1 +=1
    #         y2 +=1
    #         y3 +=1
    #         y4 +=1
    #         y5 +=1
    #     else:
    #         if tetromino[0] == 1:
    #             canvasPantalla.coords(tetromino[1],(coordenadas[x1][y1][0]/ 2, coordenadas[x1][y1][1] / 2))
    #             canvasPantalla.coords(tetromino[2],(coordenadas[x2][y2][0]/ 2, coordenadas[x2][y2][1] / 2))
    #             canvasPantalla.coords(tetromino[3],(coordenadas[x3][y3][0]/ 2, coordenadas[x3][y3][1] / 2))
    #             canvasPantalla.coords(tetromino[4],(coordenadas[x4][y4][0]/ 2, coordenadas[x4][y4][1] / 2))
    #         elif tetromino[0] == 2:
    #             canvasPantalla.coords(tetromino[1],(coordenadas[x1][y1][0]/ 2, coordenadas[x1][y1][1] / 2))
    #             canvasPantalla.coords(tetromino[2],(coordenadas[x2][y2][0]/ 2, coordenadas[x2][y2][1] / 2))
    #             canvasPantalla.coords(tetromino[3],(coordenadas[x3][y3][0]/ 2, coordenadas[x3][y3][1] / 2))
    #             canvasPantalla.coords(tetromino[4],(coordenadas[x4][y4][0]/ 2, coordenadas[x4][y4][1] / 2))
    #         elif tetromino[0] == 3:
    #             canvasPantalla.coords(tetromino[1],(coordenadas[x1][y1][0]/ 2, coordenadas[x1][y1][1] / 2))
    #             canvasPantalla.coords(tetromino[2],(coordenadas[x2][y2][0]/ 2, coordenadas[x2][y2][1] / 2))
    #             canvasPantalla.coords(tetromino[3],(coordenadas[x3][y3][0]/ 2, coordenadas[x3][y3][1] / 2))
    #             canvasPantalla.coords(tetromino[4],(coordenadas[x4][y4][0]/ 2, coordenadas[x4][y4][1] / 2))
    #         elif tetromino[0] == 4:
    #             canvasPantalla.coords(tetromino[1],(coordenadas[x1][y1][0]/ 2, coordenadas[x1][y1][1] / 2))
    #             canvasPantalla.coords(tetromino[2],(coordenadas[x2][y2][0]/ 2, coordenadas[x2][y2][1] / 2))
    #             canvasPantalla.coords(tetromino[3],(coordenadas[x3][y3][0]/ 2, coordenadas[x3][y3][1] / 2))
    #             canvasPantalla.coords(tetromino[4],(coordenadas[x4][y4][0]/ 2, coordenadas[x4][y4][1] / 2))
    #         elif tetromino[0] == 5:
    #             canvasPantalla.coords(tetromino[1],(coordenadas[x1][y1][0]/ 2, coordenadas[x1][y1][1] / 2))
    #             canvasPantalla.coords(tetromino[2],(coordenadas[x2][y2][0]/ 2, coordenadas[x2][y2][1] / 2))
    #             canvasPantalla.coords(tetromino[3],(coordenadas[x3][y3][0]/ 2, coordenadas[x3][y3][1] / 2))
    #             canvasPantalla.coords(tetromino[4],(coordenadas[x4][y4][0]/ 2, coordenadas[x4][y4][1] / 2))
    #         elif tetromino[0] == 6:
    #             canvasPantalla.coords(tetromino[1],(coordenadas[x1][y1][0]/ 2, coordenadas[x1][y1][1] / 2))
    #             canvasPantalla.coords(tetromino[2],(coordenadas[x2][y2][0]/ 2, coordenadas[x2][y2][1] / 2))
    #             canvasPantalla.coords(tetromino[3],(coordenadas[x3][y3][0]/ 2, coordenadas[x3][y3][1] / 2))
    #             canvasPantalla.coords(tetromino[4],(coordenadas[x4][y4][0]/ 2, coordenadas[x4][y4][1] / 2))
    #         elif tetromino[0] == 7:
    #             canvasPantalla.coords(tetromino[1],(coordenadas[x1][y1][0]/ 2, coordenadas[x1][y1][1] / 2))
    #             canvasPantalla.coords(tetromino[2],(coordenadas[x2][y2][0]/ 2, coordenadas[x2][y2][1] / 2))
    #             canvasPantalla.coords(tetromino[3],(coordenadas[x3][y3][0]/ 2, coordenadas[x3][y4][1] / 2))
    #             canvasPantalla.coords(tetromino[4],(coordenadas[x4][y4][0]/ 2, coordenadas[x4][y4][1] / 2))
    #             canvasPantalla.coords(tetromino[5],(coordenadas[x5][y5][0]/ 2, coordenadas[x5][y5][1] / 2))        
    #         else:
    #             canvasPantalla.coords(tetromino[1],(coordenadas[x1][y1][0]/ 2, coordenadas[x1][y1][1] / 2))
    #             canvasPantalla.coords(tetromino[2],(coordenadas[x2][y2][0]/ 2, coordenadas[x2][y2][1] / 2))
    #             canvasPantalla.coords(tetromino[3],(coordenadas[x3][y3][0]/ 2, coordenadas[x3][y4][1] / 2))
    #             canvasPantalla.coords(tetromino[4],(coordenadas[x4][y4][0]/ 2, coordenadas[x4][y4][1] / 2))
    #             canvasPantalla.coords(tetromino[5],(coordenadas[x5][y5][0]/ 2, coordenadas[x5][y5][1] / 2))
    #         escribirNuevaPosicionArchivo(nombreArchivo, tetromino, x1,x2,x3,x4,x5,y1,y2,y3,y4,y5)


    # def rotar(canvasPantalla, tetromino, nombreArchivo): # mejorar
    #     global rotaciones, x1, x2, x3, x4, x5, y1, y2, y3, y4, y5
    #     eliminarAntiguaPosicionArchivo(nombreArchivo, tetromino, x1,x2,x3,x4,x5,y1,y2,y3,y4,y5)
        
    #     posicionesX = [x1,x2,x3,x4,x5]
    #     posicionesY = [y1,y2,y3,y4,y5]
    #     if y1 >= 10 or y2 >= 10 or y3 >= 10 or y4 >= 10 or y5 >= 10:
    #         return False
    #     coordenadas = posicionImagenes()
    #     if tetromino[0] == 2:
    #         if rotaciones == 1:
    #             x2 = x1 + 1
    #             x3 = x2  + 1
    #             x4 = x3 + 1

    #             y1 += 2
    #             y2 = y1
    #             y3 = y1
    #             y4 = y1
    #             if validarMovimiento(nombreArchivo,tetromino):
    #                 canvasPantalla.coords(tetromino[1], coordenadas[x1][y1][0] / 2, coordenadas[x1][y1][1] / 2)
    #                 canvasPantalla.coords(tetromino[2], coordenadas[x2][y2][0] / 2, coordenadas[x2][y2][1] / 2)
    #                 canvasPantalla.coords(tetromino[3], coordenadas[x3][y3][0] / 2, coordenadas[x3][y3][1] / 2)
    #                 canvasPantalla.coords(tetromino[4], coordenadas[x4][y4][0] / 2, coordenadas[x4][y4][1] / 2)
    #             else:
    #                 x1 = posicionesX[0]
    #                 x2 = posicionesX[1]
    #                 x3 = posicionesX[2]
    #                 x4 = posicionesX[3]

    #                 y1 = posicionesY[0]
    #                 y2 = posicionesY[1]
    #                 y3 = posicionesY[2]
    #                 y4 = posicionesY[3]
    #                 rotaciones = 0

    #         elif rotaciones == 2:
    #             x2 = x1
    #             x3 = x1
    #             x4 = x1

    #             y1 -= 2
    #             y2 = y1 + 1
    #             y3 = y2 + 1
    #             y4 = y3 + 1
    #             if validarMovimiento(nombreArchivo,tetromino):
    #                 canvasPantalla.coords(tetromino[1], coordenadas[x1][y1][0] / 2, coordenadas[x1][y1][1] / 2)
    #                 canvasPantalla.coords(tetromino[2], coordenadas[x2][y2][0] / 2, coordenadas[x2][y2][1] / 2)
    #                 canvasPantalla.coords(tetromino[3], coordenadas[x3][y3][0] / 2, coordenadas[x3][y3][1] / 2)
    #                 canvasPantalla.coords(tetromino[4], coordenadas[x4][y4][0] / 2, coordenadas[x4][y4][1] / 2)
    #             else:
    #                 x1 = posicionesX[0]
    #                 x2 = posicionesX[1]
    #                 x3 = posicionesX[2]
    #                 x4 = posicionesX[3]

    #                 y1 = posicionesY[0]
    #                 y2 = posicionesY[1]
    #                 y3 = posicionesY[2]
    #                 y4 = posicionesY[3]
    #                 rotaciones = 0


    #         elif rotaciones == 3:
    #             x2 = x1 + 1
    #             x3 = x2 + 1
    #             x4 = x3 + 1

    #             y1 += 1
    #             y2 = y1
    #             y3 = y1
    #             y4 = y1
    #             if validarMovimiento(nombreArchivo,tetromino):
    #                 canvasPantalla.coords(tetromino[1], coordenadas[x1][y1][0] / 2, coordenadas[x1][y1][1] / 2)
    #                 canvasPantalla.coords(tetromino[2], coordenadas[x2][y2][0] / 2, coordenadas[x2][y2][1] / 2)
    #                 canvasPantalla.coords(tetromino[3], coordenadas[x3][y3][0] / 2, coordenadas[x3][y3][1] / 2)
    #                 canvasPantalla.coords(tetromino[4], coordenadas[x4][y4][0] / 2, coordenadas[x4][y4][1] / 2)
    #             else:
    #                 x1 = posicionesX[0]
    #                 x2 = posicionesX[1]
    #                 x3 = posicionesX[2]
    #                 x4 = posicionesX[3]

    #                 y1 = posicionesY[0]
    #                 y2 = posicionesY[1]
    #                 y3 = posicionesY[2]
    #                 y4 = posicionesY[3]
    #                 rotaciones = 0


    #         else:
    #             x2 = x1
    #             x3 = x1 
    #             x4 = x1

    #             y1 -= 1
    #             y2 = y1 + 1
    #             y3 = y2 + 1
    #             y4 = y3 + 1
    #             if validarMovimiento(nombreArchivo,tetromino):
    #                 canvasPantalla.coords(tetromino[1], coordenadas[x1][y1][0] / 2, coordenadas[x1][y1][1] / 2)
    #                 canvasPantalla.coords(tetromino[2], coordenadas[x2][y2][0] / 2, coordenadas[x2][y2][1] / 2)
    #                 canvasPantalla.coords(tetromino[3], coordenadas[x3][y3][0] / 2, coordenadas[x3][y3][1] / 2)
    #                 canvasPantalla.coords(tetromino[4], coordenadas[x4][y4][0] / 2, coordenadas[x4][y4][1] / 2)
    #             else:
    #                 x1 = posicionesX[0]
    #                 x2 = posicionesX[1]
    #                 x3 = posicionesX[2]
    #                 x4 = posicionesX[3]

    #                 y1 = posicionesY[0]
    #                 y2 = posicionesY[1]
    #                 y3 = posicionesY[2]
    #                 y4 = posicionesY[3]


    #             rotaciones = 0
    #     elif tetromino[0] == 3: 
    #         if rotaciones == 1:
    #             x1 = x2 - 1
    #             x3 = x2 + 1
    #             x4 = x3

    #             y1 = y2
    #             y3 = y2
    #             y4 = y2 + 1

    #             if validarMovimiento(nombreArchivo,tetromino):
    #                 canvasPantalla.coords(tetromino[1], coordenadas[x1][y1][0] / 2, coordenadas[x1][y1][1] / 2)
    #                 canvasPantalla.coords(tetromino[2], coordenadas[x2][y2][0] / 2, coordenadas[x2][y2][1] / 2)
    #                 canvasPantalla.coords(tetromino[3], coordenadas[x3][y3][0] / 2, coordenadas[x3][y3][1] / 2)
    #                 canvasPantalla.coords(tetromino[4], coordenadas[x4][y4][0] / 2, coordenadas[x4][y4][1] / 2)
    #             else:
    #                 x1 = posicionesX[0]
    #                 x2 = posicionesX[1]
    #                 x3 = posicionesX[2]
    #                 x4 = posicionesX[3]

    #                 y1 = posicionesY[0]
    #                 y2 = posicionesY[1]
    #                 y3 = posicionesY[2]
    #                 y4 = posicionesY[3]
    #                 rotaciones = 0

    #         elif rotaciones == 2:
    #             x2 -=1
    #             x3 = x2
    #             x4 = x3 + 1

    #             y1 -=1
    #             y3 = y2 + 1
    #             y4 = y1
    #             if validarMovimiento(nombreArchivo,tetromino):
    #                 canvasPantalla.coords(tetromino[1], coordenadas[x1][y1][0] / 2, coordenadas[x1][y1][1] / 2)
    #                 canvasPantalla.coords(tetromino[2], coordenadas[x2][y2][0] / 2, coordenadas[x2][y2][1] / 2)
    #                 canvasPantalla.coords(tetromino[3], coordenadas[x3][y3][0] / 2, coordenadas[x3][y3][1] / 2)
    #                 canvasPantalla.coords(tetromino[4], coordenadas[x4][y4][0] / 2, coordenadas[x4][y4][1] / 2)
    #             else:
    #                 x1 = posicionesX[0]
    #                 x2 = posicionesX[1]
    #                 x3 = posicionesX[2]
    #                 x4 = posicionesX[3]

    #                 y1 = posicionesY[0]
    #                 y2 = posicionesY[1]
    #                 y3 = posicionesY[2]
    #                 y4 = posicionesY[3]
    #                 rotaciones = 0

    #         elif rotaciones == 3:
    #             x3 = x2 + 1
    #             x4 = x3 + 1

    #             y3 = y2 
    #             y4 = y2
    #             if validarMovimiento(nombreArchivo,tetromino):
    #                 canvasPantalla.coords(tetromino[1], coordenadas[x1][y1][0] / 2, coordenadas[x1][y1][1] / 2)
    #                 canvasPantalla.coords(tetromino[2], coordenadas[x2][y2][0] / 2, coordenadas[x2][y2][1] / 2)
    #                 canvasPantalla.coords(tetromino[3], coordenadas[x3][y3][0] / 2, coordenadas[x3][y3][1] / 2)
    #                 canvasPantalla.coords(tetromino[4], coordenadas[x4][y4][0] / 2, coordenadas[x4][y4][1] / 2)
    #             else:
    #                 x1 = posicionesX[0]
    #                 x2 = posicionesX[1]
    #                 x3 = posicionesX[2]
    #                 x4 = posicionesX[3]

    #                 y1 = posicionesY[0]
    #                 y2 = posicionesY[1]
    #                 y3 = posicionesY[2]
    #                 y4 = posicionesY[3]
    #                 rotaciones = 0

    #         else:
    #             x1 += 1
    #             x2 += 1
    #             x4 = x1 - 1

    #             y3 += 1
    #             y4 = y2 + 1
                            
    #             if validarMovimiento(nombreArchivo,tetromino):
    #                 canvasPantalla.coords(tetromino[1], coordenadas[x1][y1][0] / 2, coordenadas[x1][y1][1] / 2)
    #                 canvasPantalla.coords(tetromino[2], coordenadas[x2][y2][0] / 2, coordenadas[x2][y2][1] / 2)
    #                 canvasPantalla.coords(tetromino[3], coordenadas[x3][y3][0] / 2, coordenadas[x3][y3][1] / 2)
    #                 canvasPantalla.coords(tetromino[4], coordenadas[x4][y4][0] / 2, coordenadas[x4][y4][1] / 2)
    #             else:
    #                 x1 = posicionesX[0]
    #                 x2 = posicionesX[1]
    #                 x3 = posicionesX[2]
    #                 x4 = posicionesX[3]

    #                 y1 = posicionesY[0]
    #                 y2 = posicionesY[1]
    #                 y3 = posicionesY[2]
    #                 y4 = posicionesY[3]


    #             rotaciones = 0         
    #     elif tetromino[0] == 4:
    #         if rotaciones == 1:
    #             x2 += 1
    #             x4 += 1

    #             y1 += 1
    #             y2 += 1
    #             y4 = y2 - 1

    #             if validarMovimiento(nombreArchivo,tetromino):
    #                 canvasPantalla.coords(tetromino[1], coordenadas[x1][y1][0] / 2, coordenadas[x1][y1][1] / 2)
    #                 canvasPantalla.coords(tetromino[2], coordenadas[x2][y2][0] / 2, coordenadas[x2][y2][1] / 2)
    #                 canvasPantalla.coords(tetromino[3], coordenadas[x3][y3][0] / 2, coordenadas[x3][y3][1] / 2)
    #                 canvasPantalla.coords(tetromino[4], coordenadas[x4][y4][0] / 2, coordenadas[x4][y4][1] / 2)
    #             else:
    #                 x1 = posicionesX[0]
    #                 x2 = posicionesX[1]
    #                 x3 = posicionesX[2]
    #                 x4 = posicionesX[3]

    #                 y1 = posicionesY[0]
    #                 y2 = posicionesY[1]
    #                 y3 = posicionesY[2]
    #                 y4 = posicionesY[3]
    #                 rotaciones = 0

    #         elif rotaciones == 2:
    #             x2 -= 2
    #             x3 -= 1
    #             x4 -= 1

    #             y1 -= 1
    #             y3 += 1
    #             y4 = y3
            
    #             if validarMovimiento(nombreArchivo,tetromino):
    #                 canvasPantalla.coords(tetromino[1], coordenadas[x1][y1][0] / 2, coordenadas[x1][y1][1] / 2)
    #                 canvasPantalla.coords(tetromino[2], coordenadas[x2][y2][0] / 2, coordenadas[x2][y2][1] / 2)
    #                 canvasPantalla.coords(tetromino[3], coordenadas[x3][y3][0] / 2, coordenadas[x3][y3][1] / 2)
    #                 canvasPantalla.coords(tetromino[4], coordenadas[x4][y4][0] / 2, coordenadas[x4][y4][1] / 2)
    #             else:
    #                 x1 = posicionesX[0]
    #                 x2 = posicionesX[1]
    #                 x3 = posicionesX[2]
    #                 x4 = posicionesX[3]

    #                 y1 = posicionesY[0]
    #                 y2 = posicionesY[1]
    #                 y3 = posicionesY[2]
    #                 y4 = posicionesY[3]
    #                 rotaciones = 0

    #         elif rotaciones == 3:
    #             x1 += 1
    #             x4 = x1 + 1

    #             y1 += 1
    #             y4 = y1
            
    #             if validarMovimiento(nombreArchivo,tetromino):
    #                 canvasPantalla.coords(tetromino[1], coordenadas[x1][y1][0] / 2, coordenadas[x1][y1][1] / 2)
    #                 canvasPantalla.coords(tetromino[2], coordenadas[x2][y2][0] / 2, coordenadas[x2][y2][1] / 2)
    #                 canvasPantalla.coords(tetromino[3], coordenadas[x3][y3][0] / 2, coordenadas[x3][y3][1] / 2)
    #                 canvasPantalla.coords(tetromino[4], coordenadas[x4][y4][0] / 2, coordenadas[x4][y4][1] / 2)
    #             else:
    #                 x1 = posicionesX[0]
    #                 x2 = posicionesX[1]
    #                 x3 = posicionesX[2]
    #                 x4 = posicionesX[3]

    #                 y1 = posicionesY[0]
    #                 y2 = posicionesY[1]
    #                 y3 = posicionesY[2]
    #                 y4 = posicionesY[3]
    #                 rotaciones = 0

    #         elif rotaciones == 4:
    #             x1 -= 1
    #             x2 += 1
    #             x3 += 1
    #             x4 -= 1

    #             y1 -= 1
    #             y2 = y1
    #             y3 = y2 + 1
    #             y4 = y3 + 1 
    #             if validarMovimiento(nombreArchivo,tetromino):
    #                 canvasPantalla.coords(tetromino[1], coordenadas[x1][y1][0] / 2, coordenadas[x1][y1][1] / 2)
    #                 canvasPantalla.coords(tetromino[2], coordenadas[x2][y2][0] / 2, coordenadas[x2][y2][1] / 2)
    #                 canvasPantalla.coords(tetromino[3], coordenadas[x3][y3][0] / 2, coordenadas[x3][y3][1] / 2)
    #                 canvasPantalla.coords(tetromino[4], coordenadas[x4][y4][0] / 2, coordenadas[x4][y4][1] / 2)
    #             else:
    #                 x1 = posicionesX[0]
    #                 x2 = posicionesX[1]
    #                 x3 = posicionesX[2]
    #                 x4 = posicionesX[3]

    #                 y1 = posicionesY[0]
    #                 y2 = posicionesY[1]
    #                 y3 = posicionesY[2]
    #                 y4 = posicionesY[3]


    #             rotaciones = 0
    #     elif tetromino[0] == 5:
    #         if rotaciones == 1:
    #             x3 = x2 + 1
    #             y3 = y2

    #             if validarMovimiento(nombreArchivo,tetromino):
    #                 canvasPantalla.coords(tetromino[1], coordenadas[x1][y1][0] / 2, coordenadas[x1][y1][1] / 2)
    #                 canvasPantalla.coords(tetromino[2], coordenadas[x2][y2][0] / 2, coordenadas[x2][y2][1] / 2)
    #                 canvasPantalla.coords(tetromino[3], coordenadas[x3][y3][0] / 2, coordenadas[x3][y3][1] / 2)
    #                 canvasPantalla.coords(tetromino[4], coordenadas[x4][y4][0] / 2, coordenadas[x4][y4][1] / 2)
    #             else:
    #                 x1 = posicionesX[0]
    #                 x2 = posicionesX[1]
    #                 x3 = posicionesX[2]
    #                 x4 = posicionesX[3]

    #                 y1 = posicionesY[0]
    #                 y2 = posicionesY[1]
    #                 y3 = posicionesY[2]
    #                 y4 = posicionesY[3]
    #                 rotaciones = 0

    #         elif rotaciones == 2:
    #             x4 = x2
    #             y4 = y2 + 1

    #             if validarMovimiento(nombreArchivo,tetromino):
    #                 canvasPantalla.coords(tetromino[1], coordenadas[x1][y1][0] / 2, coordenadas[x1][y1][1] / 2)
    #                 canvasPantalla.coords(tetromino[2], coordenadas[x2][y2][0] / 2, coordenadas[x2][y2][1] / 2)
    #                 canvasPantalla.coords(tetromino[3], coordenadas[x3][y3][0] / 2, coordenadas[x3][y3][1] / 2)
    #                 canvasPantalla.coords(tetromino[4], coordenadas[x4][y4][0] / 2, coordenadas[x4][y4][1] / 2)
    #             else:
    #                 x1 = posicionesX[0]
    #                 x2 = posicionesX[1]
    #                 x3 = posicionesX[2]
    #                 x4 = posicionesX[3]

    #                 y1 = posicionesY[0]
    #                 y2 = posicionesY[1]
    #                 y3 = posicionesY[2]
    #                 y4 = posicionesY[3]
    #                 rotaciones = 0

    #         elif rotaciones == 3:
    #             x1 = x2 - 1
                
    #             y1 = y2

    #             if validarMovimiento(nombreArchivo,tetromino):
    #                 canvasPantalla.coords(tetromino[1], coordenadas[x1][y1][0] / 2, coordenadas[x1][y1][1] / 2)
    #                 canvasPantalla.coords(tetromino[2], coordenadas[x2][y2][0] / 2, coordenadas[x2][y2][1] / 2)
    #                 canvasPantalla.coords(tetromino[3], coordenadas[x3][y3][0] / 2, coordenadas[x3][y3][1] / 2)
    #                 canvasPantalla.coords(tetromino[4], coordenadas[x4][y4][0] / 2, coordenadas[x4][y4][1] / 2)
    #             else:
    #                 x1 = posicionesX[0]
    #                 x2 = posicionesX[1]
    #                 x3 = posicionesX[2]
    #                 x4 = posicionesX[3]

    #                 y1 = posicionesY[0]
    #                 y2 = posicionesY[1]
    #                 y3 = posicionesY[2]
    #                 y4 = posicionesY[3]
    #                 rotaciones = 0

    #         else:
    #             x1 = x2
    #             x3 = x2
    #             x4 = x1 - 1

    #             y1 = y2 - 1
    #             y3 = y2 + 1
    #             y4 = y2

    #             if validarMovimiento(nombreArchivo,tetromino):
    #                 canvasPantalla.coords(tetromino[1], coordenadas[x1][y1][0] / 2, coordenadas[x1][y1][1] / 2)
    #                 canvasPantalla.coords(tetromino[2], coordenadas[x2][y2][0] / 2, coordenadas[x2][y2][1] / 2)
    #                 canvasPantalla.coords(tetromino[3], coordenadas[x3][y3][0] / 2, coordenadas[x3][y3][1] / 2)
    #                 canvasPantalla.coords(tetromino[4], coordenadas[x4][y4][0] / 2, coordenadas[x4][y4][1] / 2)
    #             else:
    #                 x1 = posicionesX[0]
    #                 x2 = posicionesX[1]
    #                 x3 = posicionesX[2]
    #                 x4 = posicionesX[3]

    #                 y1 = posicionesY[0]
    #                 y2 = posicionesY[1]
    #                 y3 = posicionesY[2]
    #                 y4 = posicionesY[3]


    #             rotaciones = 0
    #     elif tetromino[0] == 6:
    #         if rotaciones == 1:
    #             x2 = x1 + 1
    #             x3 = x2
    #             x4 = x3 + 1

    #             y2 = y1
    #             y3 = y2 - 1
    #             y4 = y3
    #             if validarMovimiento(nombreArchivo,tetromino):
    #                 canvasPantalla.coords(tetromino[1], coordenadas[x1][y1][0] / 2, coordenadas[x1][y1][1] / 2)
    #                 canvasPantalla.coords(tetromino[2], coordenadas[x2][y2][0] / 2, coordenadas[x2][y2][1] / 2)
    #                 canvasPantalla.coords(tetromino[3], coordenadas[x3][y3][0] / 2, coordenadas[x3][y3][1] / 2)
    #                 canvasPantalla.coords(tetromino[4], coordenadas[x4][y4][0] / 2, coordenadas[x4][y4][1] / 2)
    #             else:
    #                 x1 = posicionesX[0]
    #                 x2 = posicionesX[1]
    #                 x3 = posicionesX[2]
    #                 x4 = posicionesX[3]

    #                 y1 = posicionesY[0]
    #                 y2 = posicionesY[1]
    #                 y3 = posicionesY[2]
    #                 y4 = posicionesY[3]
    #                 rotaciones = 0

    #         elif rotaciones == 2:
    #             x2 = x1
    #             x3 = x2 + 1
    #             x4 = x3

    #             y2 = y1 + 1
    #             y3 = y2
    #             y4 = y3 + 1
    #             if validarMovimiento(nombreArchivo,tetromino):
    #                 canvasPantalla.coords(tetromino[1], coordenadas[x1][y1][0] / 2, coordenadas[x1][y1][1] / 2)
    #                 canvasPantalla.coords(tetromino[2], coordenadas[x2][y2][0] / 2, coordenadas[x2][y2][1] / 2)
    #                 canvasPantalla.coords(tetromino[3], coordenadas[x3][y3][0] / 2, coordenadas[x3][y3][1] / 2)
    #                 canvasPantalla.coords(tetromino[4], coordenadas[x4][y4][0] / 2, coordenadas[x4][y4][1] / 2)
    #             else:
    #                 x1 = posicionesX[0]
    #                 x2 = posicionesX[1]
    #                 x3 = posicionesX[2]
    #                 x4 = posicionesX[3]

    #                 y1 = posicionesY[0]
    #                 y2 = posicionesY[1]
    #                 y3 = posicionesY[2]
    #                 y4 = posicionesY[3]
    #                 rotaciones = 0

        
    #         elif rotaciones == 3:
    #             x1 += 1
    #             x4 = x3 + 1

    #             y2 += 1
    #             y1 = y2
    #             y4 = y3 

    #             if validarMovimiento(nombreArchivo,tetromino):
    #                 canvasPantalla.coords(tetromino[1], coordenadas[x1][y1][0] / 2, coordenadas[x1][y1][1] / 2)
    #                 canvasPantalla.coords(tetromino[2], coordenadas[x2][y2][0] / 2, coordenadas[x2][y2][1] / 2)
    #                 canvasPantalla.coords(tetromino[3], coordenadas[x3][y3][0] / 2, coordenadas[x3][y3][1] / 2)
    #                 canvasPantalla.coords(tetromino[4], coordenadas[x4][y4][0] / 2, coordenadas[x4][y4][1] / 2)
    #             else:
    #                 x1 = posicionesX[0]
    #                 x2 = posicionesX[1]
    #                 x3 = posicionesX[2]
    #                 x4 = posicionesX[3]

    #                 y1 = posicionesY[0]
    #                 y2 = posicionesY[1]
    #                 y3 = posicionesY[2]
    #                 y4 = posicionesY[3]
    #                 rotaciones = 0

    #         else:
    #             x1 = x2
    #             x4 = x3

    #             y2 -= 1
    #             y1 = y2 - 1
    #             y4 = y3 + 1

    #             if validarMovimiento(nombreArchivo,tetromino):
    #                 canvasPantalla.coords(tetromino[1], coordenadas[x1][y1][0] / 2, coordenadas[x1][y1][1] / 2)
    #                 canvasPantalla.coords(tetromino[2], coordenadas[x2][y2][0] / 2, coordenadas[x2][y2][1] / 2)
    #                 canvasPantalla.coords(tetromino[3], coordenadas[x3][y3][0] / 2, coordenadas[x3][y3][1] / 2)
    #                 canvasPantalla.coords(tetromino[4], coordenadas[x4][y4][0] / 2, coordenadas[x4][y4][1] / 2)
    #             else:
    #                 x1 = posicionesX[0]
    #                 x2 = posicionesX[1]
    #                 x3 = posicionesX[2]
    #                 x4 = posicionesX[3]

    #                 y1 = posicionesY[0]
    #                 y2 = posicionesY[1]
    #                 y3 = posicionesY[2]
    #                 y4 = posicionesY[3]


    #             rotaciones = 0
    #     elif tetromino[0] == 7:
    #         if rotaciones == 1:
    #             x2 += 1
    #             x4 = x2

    #             y1 = y3
    #             y2 = y3
                
    #             if validarMovimiento(nombreArchivo,tetromino):
    #                 canvasPantalla.coords(tetromino[1], coordenadas[x1][y1][0] / 2, coordenadas[x1][y1][1] / 2)
    #                 canvasPantalla.coords(tetromino[2], coordenadas[x2][y2][0] / 2, coordenadas[x2][y2][1] / 2)
    #                 canvasPantalla.coords(tetromino[3], coordenadas[x3][y3][0] / 2, coordenadas[x3][y3][1] / 2)
    #                 canvasPantalla.coords(tetromino[4], coordenadas[x4][y4][0] / 2, coordenadas[x4][y4][1] / 2)
    #                 canvasPantalla.coords(tetromino[5], coordenadas[x5][y5][0] / 2, coordenadas[x5][y5][1] / 2)
    #             else:
    #                 x1 = posicionesX[0]
    #                 x2 = posicionesX[1]
    #                 x3 = posicionesX[2]
    #                 x4 = posicionesX[3]
    #                 x5 = posicionesX[4]

    #                 y1 = posicionesY[0]
    #                 y2 = posicionesY[1]
    #                 y3 = posicionesY[2]
    #                 y4 = posicionesY[3]
    #                 y5 = posicionesY[4]
    #                 rotaciones = 0

    #         elif rotaciones == 2:
    #             x3 = x1
    #             x2 = x3 + 1
    #             x4 = x2

    #             y1 -= 1
    #             y2 = y1


    #             if validarMovimiento(nombreArchivo,tetromino):
    #                 canvasPantalla.coords(tetromino[1], coordenadas[x1][y1][0] / 2, coordenadas[x1][y1][1] / 2)
    #                 canvasPantalla.coords(tetromino[2], coordenadas[x2][y2][0] / 2, coordenadas[x2][y2][1] / 2)
    #                 canvasPantalla.coords(tetromino[3], coordenadas[x3][y3][0] / 2, coordenadas[x3][y3][1] / 2)
    #                 canvasPantalla.coords(tetromino[4], coordenadas[x4][y4][0] / 2, coordenadas[x4][y4][1] / 2)
    #                 canvasPantalla.coords(tetromino[5], coordenadas[x5][y5][0] / 2, coordenadas[x5][y5][1] / 2)
    #             else:
    #                 x1 = posicionesX[0]
    #                 x2 = posicionesX[1]
    #                 x3 = posicionesX[2]
    #                 x4 = posicionesX[3]
    #                 x5 = posicionesX[4]

    #                 y1 = posicionesY[0]
    #                 y2 = posicionesY[1]
    #                 y3 = posicionesY[2]
    #                 y4 = posicionesY[3]
    #                 y5 = posicionesY[4]
    #                 rotaciones = 0
    #         elif rotaciones == 3:
    #             x5 = x2 + 1
    #             x4 = x5

    #             y2 = y3
    #             y5 = y3
    #             y4 = y5 - 1
    #             if validarMovimiento(nombreArchivo,tetromino):
    #                 canvasPantalla.coords(tetromino[1], coordenadas[x1][y1][0] / 2, coordenadas[x1][y1][1] / 2)
    #                 canvasPantalla.coords(tetromino[2], coordenadas[x2][y2][0] / 2, coordenadas[x2][y2][1] / 2)
    #                 canvasPantalla.coords(tetromino[3], coordenadas[x3][y3][0] / 2, coordenadas[x3][y3][1] / 2)
    #                 canvasPantalla.coords(tetromino[4], coordenadas[x4][y4][0] / 2, coordenadas[x4][y4][1] / 2)
    #                 canvasPantalla.coords(tetromino[5], coordenadas[x5][y5][0] / 2, coordenadas[x5][y5][1] / 2)
    #             else:
    #                 x1 = posicionesX[0]
    #                 x2 = posicionesX[1]
    #                 x3 = posicionesX[2]
    #                 x4 = posicionesX[3]
    #                 x5 = posicionesX[4]

    #                 y1 = posicionesY[0]
    #                 y2 = posicionesY[1]
    #                 y3 = posicionesY[2]
    #                 y4 = posicionesY[3]
    #                 y5 = posicionesY[4]
    #                 rotaciones = 0
    #         else:
    #             x3 = x2
    #             x4 = x2
    #             x5 = x1

    #             y2 = y1
    #             y3 = y2 + 1
    #             y4 = y3 + 1
    #             y5 = y4
                
    #             if validarMovimiento(nombreArchivo,tetromino):
    #                 canvasPantalla.coords(tetromino[1], coordenadas[x1][y1][0] / 2, coordenadas[x1][y1][1] / 2)
    #                 canvasPantalla.coords(tetromino[2], coordenadas[x2][y2][0] / 2, coordenadas[x2][y2][1] / 2)
    #                 canvasPantalla.coords(tetromino[3], coordenadas[x3][y3][0] / 2, coordenadas[x3][y3][1] / 2)
    #                 canvasPantalla.coords(tetromino[4], coordenadas[x4][y4][0] / 2, coordenadas[x4][y4][1] / 2)
    #                 canvasPantalla.coords(tetromino[5], coordenadas[x5][y5][0] / 2, coordenadas[x5][y5][1] / 2)
    #             else:
    #                 x1 = posicionesX[0]
    #                 x2 = posicionesX[1]
    #                 x3 = posicionesX[2]
    #                 x4 = posicionesX[3]
    #                 x5 = posicionesX[4]

    #                 y1 = posicionesY[0]
    #                 y2 = posicionesY[1]
    #                 y3 = posicionesY[2]
    #                 y4 = posicionesY[3]
    #                 y5 = posicionesY[4]

    #             rotaciones = 0
    #     rotaciones += 1


    # def  validarMovimiento(nombreArchivo, tetromino):# mejorar
    #     global x1, x2,  x3, x4, x5, y1, y2, y3, y4, y5
    #     listaArchivo = archivoALista(nombreArchivo)
    #     listaArchivo = eliminarSaltosDeLinea(listaArchivo)
    #     if tetromino[0] >= 1 and tetromino[0] <= 6:
    #         for i in range(largoLista(listaArchivo)):
    #             for j in range(largoLista(listaArchivo[0])):
    #                 if i != 0:
    #                     if i == x1 and j == y1:
    #                         if verificarElementos(listaArchivo[i][j]):
    #                             return False
    #                     elif i == x2 and j == y2:
    #                         if verificarElementos(listaArchivo[i][j]):
    #                             return False
    #                     elif i == x3 and j == y3:
    #                         if verificarElementos(listaArchivo[i][j]):
    #                             return False
    #                     else:
    #                         if i == x4 and j == y4:
    #                             if verificarElementos(listaArchivo[i][j]):
    #                                 return False
    #         return True
    #     else:
    #         for i in range(largoLista(listaArchivo)):
    #             for j in range(largoLista(listaArchivo[0])):
    #                 if i != 0:
    #                     if i == x1 and j == y1:
    #                         if verificarElementos(listaArchivo[i][j]):
    #                             return False
    #                     elif i == x2 and j == y2:
    #                         if verificarElementos(listaArchivo[i][j]):
    #                             return False
    #                     elif i == x3 and j == y3:
    #                         if verificarElementos(listaArchivo[i][j]):
    #                             return False
    #                     elif i == x4 and j == y4:
    #                         if verificarElementos(listaArchivo[i][j]):
    #                             return False
    #                     else:
    #                         if i == x5 and j == y5:
    #                             if verificarElementos(listaArchivo[i][j]):
    #                                 return False
    #         return True

    # def verificarElementos(elemento):
    #     listaElementos = ["+","1","2","3","4","5","6","7","8"]
    #     for i in listaElementos:
    #         if i == elemento:
    #             return True
    #     return False


    # def escribirNuevaPosicionArchivo(nombreArchivo, tetrimino, x1, x2,  x3, x4, x5, y1, y2, y3, y4, y5):
    #     listaArchivo = archivoALista(nombreArchivo)
    #     listaArchivo = eliminarSaltosDeLinea(listaArchivo)
    #     nuevoContenido = []
        
    #     if tetrimino[0] == 1:
    #         imagen = "1"
    #     elif tetrimino[0] == 2:
    #         imagen = "2"
    #     elif tetrimino[0] == 3:
    #         imagen = "3"
    #     elif tetrimino[0] == 4:
    #         imagen = "4"
    #     elif tetrimino[0] == 5:
    #         imagen = "5"
    #     elif tetrimino[0] == 6:
    #         imagen = "6"
    #     elif tetrimino[0] == 7:
    #         imagen = "7"
    #     else:
    #         imagen = "8"


    #     if tetrimino[0] >= 1 and tetrimino[0] <= 6:
    #         for i in range(largoLista(listaArchivo)):
    #             contenido = []
    #             for j in range(largoLista(listaArchivo[0])):
    #                 if i == x1 and j == y1:
    #                     contenido += [imagen]
    #                 elif i == x2 and j == y2:
    #                     contenido += [imagen]
    #                 elif i == x3 and j == y3:
    #                     contenido += [imagen]
    #                 elif i == x4 and j == y4:
    #                     contenido += [imagen]
    #                 else:
    #                     contenido += [listaArchivo[i][j]]
    #             nuevoContenido += [contenido]
    #     else:
    #         for i in range(largoLista(listaArchivo)):
    #             contenido = []
    #             for j in range(largoLista(listaArchivo[0])):
    #                 if i == x1 and j == y1:
    #                     contenido += [imagen]
    #                 elif i == x2 and j == y2:
    #                     contenido += [imagen]
    #                 elif i == x3 and j == y3:
    #                     contenido += [imagen]
    #                 elif i == x4 and j == y4:
    #                     contenido += [imagen]
    #                 elif i == x5 and j == y5:
    #                     contenido += [imagen]
    #                 else:
    #                     contenido += [listaArchivo[i][j]]
    #             nuevoContenido += [contenido]
        
        
    #     modificarArchivoJuegoXX(nombreArchivo, nuevoContenido)



    # def eliminarAntiguaPosicionArchivo(nombreArchivo, tetrimino, x1, x2,  x3, x4, x5, y1, y2, y3, y4, y5):
    #     listaArchivo = archivoALista(nombreArchivo)
    #     listaArchivo = eliminarSaltosDeLinea(listaArchivo)
    #     nuevoContenido = []
        
    #     if tetrimino[0] >= 1 and tetrimino[0] <= 6:
    #         for i in range(largoLista(listaArchivo)):
    #             contenido = []
    #             for j in range(largoLista(listaArchivo[0])):
    #                 if i == x1 and j == y1:
    #                     contenido += ["0"]
    #                 elif i == x2 and j == y2:
    #                     contenido += ["0"]
    #                 elif i == x3 and j == y3:
    #                     contenido += ["0"]
    #                 elif i == x4 and j == y4:
    #                     contenido += ["0"]
    #                 else:
    #                     contenido += [listaArchivo[i][j]]
    #             nuevoContenido += [contenido]
    #     else:
    #         for i in range(largoLista(listaArchivo)):
    #             contenido = []
    #             for j in range(largoLista(listaArchivo[0])):
    #                 if i == x1 and j == y1:
    #                     contenido += ["0"]
    #                 elif i == x2 and j == y2:
    #                     contenido += ["0"]
    #                 elif i == x3 and j == y3:
    #                     contenido += ["0"]
    #                 elif i == x4 and j == y4:
    #                     contenido += ["0"]
    #                 elif i == x5 and j == y5:
    #                     contenido += ["0"]
    #                 else:
    #                     contenido += [listaArchivo[i][j]]
    #             nuevoContenido += [contenido]
        
    #     modificarArchivoJuegoXX(nombreArchivo, nuevoContenido)


    # def eliminarFilaArchivo(nombreArchivo):
    #     fila = retornarFilaArchivoDescendente(nombreArchivo)
    #     if fila != False: # para la fubncion de validacion
    #         listaArchivo = archivoALista(nombreArchivo)
    #         listaArchivo = eliminarSaltosDeLinea(listaArchivo)
    #         nuevoContenido = []
    #         for i in range(largoLista(listaArchivo)):
    #             contenido = []
    #             for j in range(largoLista(listaArchivo[0])):
    #                 if i != fila:
    #                     contenido += [listaArchivo[i][j]]
    #             if contenido != []:
    #                 nuevoContenido += [contenido]
    #         modificarArchivoJuegoXX(nombreArchivo,nuevoContenido)
    #         fila = reubicarFila(nombreArchivo)
    #         nuevoContenido = acomodarFilasArchivo(nombreArchivo, fila)
    #         modificarArchivoJuegoXX(nombreArchivo, nuevoContenido)

    # def retornarFilaArchivoDescendente(nombreArchivo):
    #     listaArchivo = archivoALista(nombreArchivo)
    #     listaArchivo = eliminarSaltosDeLinea(listaArchivo)
    #     i = largoLista(listaArchivo) - 2

    #     while i != 0:
    #         contenido = []
    #         j = largoLista(listaArchivo[0]) - 1
    #         while j != 0:
    #             if listaArchivo[i][j] != "0":
    #                 verificarElementos
    #                 contenido += [listaArchivo[i][j]]
    #             if contenido != []:
    #                 if largoLista(contenido) == 11:
    #                     return i
    #             j -= 1
    #         i -= 1
    #     return False


    # def reubicarFila(nombreArchivo):
    #     listaArchivo = archivoALista(nombreArchivo)
    #     listaArchivo = eliminarSaltosDeLinea(listaArchivo)
    #     i = largoLista(listaArchivo) -1

    #     while i != 0:
    #         contenido = []
    #         j = largoLista(listaArchivo[0]) - 1
    #         while j != 0:
    #             if verificarElementos(listaArchivo[i][j]) == False:
    #                 contenido += [listaArchivo[i][j]]
    #             if contenido != []:
    #                 if largoLista(contenido) == 10:
    #                     return i
    #             j -= 1
    #         i -= 1
    #     return False

    # def acomodarFilasArchivo(nombreArchivo, fila):
    #     listaArchivo = archivoALista(nombreArchivo)
    #     listaArchivo = eliminarSaltosDeLinea(listaArchivo)
    #     nuevoContenido = []
    #     for i in range(largoLista(listaArchivo)):
    #         if i == fila:
    #             nuevoContenido += [listaArchivo[i],listaArchivo[i]]
    #         else:
    #             nuevoContenido += [listaArchivo[i]]
    #     return nuevoContenido


    # def modificarMatrizIdentificadores(tetromino, x1,x2,x3,x4,x5,y1,y2,y3,y4,y5):
    #     global matrizIdentificadores
    #     nuevaMatriz = []
    #     for i in range(largoLista(matrizIdentificadores)):
    #         vector = []
    #         for j in range(largoLista(matrizIdentificadores[0])):
    #             if tetromino[0] >= 1 and tetromino[0] <= 6:
    #                 if i == x1 and j == y1:
    #                     vector += [tetromino[1]]
    #                 elif i == x2 and j == y2:
    #                     vector += [tetromino[2]]
    #                 elif i == x3 and j == y3:
    #                     vector += [tetromino[3]]
    #                 elif i == x4 and j == y4:
    #                     vector += [tetromino[4]]
    #                 else:
    #                     vector += [matrizIdentificadores[i][j]]
                
    #             else:
    #                 if i == x1 and j == y1:    
    #                     vector += [tetromino[1]]
    #                 elif i == x2 and j == y2:
    #                     vector += [tetromino[2]]
    #                 elif i == x3 and j == y3:
    #                     vector += [tetromino[3]]
    #                 elif i == x4 and j == y4:
    #                     vector += [tetromino[4]]
    #                 elif i == x5 and j == y5:
    #                     vector += [tetromino[5]]
    #                 else:
    #                     vector += [matrizIdentificadores[i][j]]
                
    #         nuevaMatriz += [vector]
    #     matrizIdentificadores = nuevaMatriz

    # def eliminarFilaMatrizIdentificadores(nombreArchivo):
    #     global matrizIdentificadores

    #     fila = retornarFilaArchivoDescendente(nombreArchivo)
    #     if fila != False: # para la fubncion de validacion
    #         nuevoContenido = []
    #         for i in range(largoLista(matrizIdentificadores)):
    #             contenido = []
    #             for j in range(largoLista(matrizIdentificadores[0])):
    #                 if i != fila:
    #                     contenido += [matrizIdentificadores[i][j]]
    #             if contenido != []:
    #                 nuevoContenido += [contenido]
    #         matrizIdentificadores = nuevoContenido
    #         fila = reubicarFilaMatrizIdentificadores()
    #         acomodarFilasMatrizIdentificadores(fila)
    #         reubicarFilaMatrizIdentificadores()
    #         return True    

    # def reubicarFilaMatrizIdentificadores():
    #     global matrizIdentificadores
    #     i = largoLista(matrizIdentificadores) -1

    #     while i != 0:
    #         contenido = []
    #         j = largoLista(matrizIdentificadores[0]) - 1
    #         while j != 0:
    #             if verificarElementos(matrizIdentificadores[i][j]) == False and not isinstance(matrizIdentificadores[i][j], int):
    #                 contenido += [matrizIdentificadores[i][j]]
    #             if contenido != []:
    #                 if largoLista(contenido) == 10:
    #                     return i
    #             j -= 1
    #         i -= 1
    #     return False



    # def acomodarFilasMatrizIdentificadores(fila):
    #     global matrizIdentificadores
    #     filaCeros = matrizIdentificadores[fila]
    #     nuevoContenido = []
    #     for i in range(largoLista(matrizIdentificadores)):
    #         if i == fila:
    #             nuevoContenido += [matrizIdentificadores[i],matrizIdentificadores[i]]
    #         else:
    #             nuevoContenido += [matrizIdentificadores[i]]

    #     matrizIdentificadores = nuevoContenido




    # def eliminarFilaTetris(canvasPantalla, nombreArchivo):
    #     global matrizIdentificadores
    #     fila = retornarFilaArchivoDescendente(nombreArchivo)
    #     for i in range(largoLista(matrizIdentificadores)):
    #         for j in range(largoLista(matrizIdentificadores[0])):
    #             if i == fila and j != 0 and j != 11:
    #                 canvasPantalla.delete(matrizIdentificadores[i][j])
        
    # def refrescarPantallaTetris(canvasPantalla):
    #     global matrizIdentificadores
    #     coordenadas = posicionImagenes()
    #     for i in range(largoLista(matrizIdentificadores)):
    #         for j in range(largoLista(matrizIdentificadores[0])):
    #             if matrizIdentificadores[i][j] != "0" or matrizIdentificadores[i][j] != "+":
    #                 canvasPantalla.coords(matrizIdentificadores[i][j], coordenadas[i][j][0] / 2, coordenadas[i][j][1] / 2)
    
    # consola.protocol("WM_DELETE_WINDOW", lambda : borrarArchivo(nombreArchivo, consola))
    # consola.mainloop()




"""
Nombre: salir
Entrada: ventana
Salida: Cierra (destruye) la ventana
Restricciones: Las necesarias para el correcto funcionamiento
"""
def salir(ventana):
    ventana.destroy()

ventanaInicio()