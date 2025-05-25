from tkinter import  *
from PIL import Image, ImageTk


def seleccionar_obstaculo(canva, evento, imagen, paredes):
    imagenId = canva.find_closest(evento.x, evento.y)
    for pared in paredes:
        if imagenId[0] != pared:
            canva.itemconfig(imagenId[0], image=imagen)
    

def quitar_obstaculo(canva, evento, imagen, paredes):
    imagenId = canva.find_closest(evento.x, evento.y)
    for pared in paredes:
        if imagenId[0] != pared:
            canva.itemconfig(imagenId[0], image=imagen)


"""
Nombre: crear_matriz
Entrada: ninguna
Salida: Una matriz
Restricciones: Las necesarias para el correcto funcionamiento
"""
def crear_matriz():
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
Nombre: centrar_ventana
Entrada: ventana
Salida: La ventana reposicionada en el 'centro' de la pantalla
Restricciones: Las necesarias para el correcto funcionamiento
"""
def centrar_ventana(ventana):
    ventana.update_idletasks()
    ancho = ventana.winfo_width()
    alto = ventana.winfo_height()
    x = (ventana.winfo_screenwidth() // 2) - (ancho // 2)
    y = (ventana.winfo_screenheight() // 2) - (alto // 2)
    ventana.geometry(f'{ancho}x{alto}+{x}+{y}') 


"""
Nombre: ventana_inicio
Entraeda: Ninguna
Salida: La ventana inicial, iniciara el juego o finalizara el programa
Restricciones: Las necesarias para el correcto funcionamiento
"""
def ventana_inicio(): # Tal vez cambien los nombres de las variables
    ventana_inicial = Tk()   
    ventana_inicial.geometry("500x300")
    ventana_inicial.resizable(0,0)
    centrar_ventana(ventana_inicial)
    
    boton_jugar = Button(ventana_inicial, 
                         text="Jugar", 
                         font=("Arial", 25, "bold"), 
                         command= lambda arg =ventana_inicial: interfaz(ventana_inicial)).pack()
    
    boton_salir = Button(ventana_inicial, 
                         text="Salir", 
                         font=("Arial", 25, "bold"), 
                         command= lambda arg = ventana_inicial: salir(ventana_inicial)).pack()
    
    ventana_inicial.mainloop()


"""
Nombre: interfaz 
Entrada: ventana
Salida: La creacion de nuevas ventanas(una matriz interactiva y una ventana de demostracion) junto con sus respectivos widgets
Restricciones: Las necesarias para el correcto funcionamiento
"""
def interfaz(ventana):
    #                        Creacion de ventana principal 
    ventana.destroy()
    consola = Tk()
    consola.geometry("600x800")
    consola.resizable(0,0)
    consola.config(bg="#A9A9A9")
    centrar_ventana(consola)

    imagen = Image.open("gameboyBase.png")
    imagen_tk = ImageTk.PhotoImage(imagen)

    canvas_gameboy = Canvas(consola, width=300, height=300, bg="pink")
    canvas_gameboy.pack(fill="both", expand=True)
    canvas_gameboy.create_image(0, 0, anchor="nw", image=imagen_tk)
    ###########################################################################


    canvas_pantalla = Canvas(canvas_gameboy, width=465, height=366, bg="pink")
    canvas_pantalla.place(x=67, y=85)

    
    contante_x = 39
    contante_y = 16.68

    
    matriz_obstaculos = []

    
    imagen_pared = Image.open("bloqueGris.png")
    imagen_pared = imagen_pared.resize((39, 17))
    imagen_paredTk = ImageTk.PhotoImage(imagen_pared)


    imagen_fondo = Image.open("fondo.png")
    imagen_fondo = imagen_fondo.resize((39, 17))
    imagen_fondoTk = ImageTk.PhotoImage(imagen_fondo)


    imagen_fondo_seleccioando = Image.open("fondoSeleccionado.png")
    imagen_fondo_seleccioando = imagen_fondo_seleccioando.resize((39, 17))
    fondo_seleccionadoTk = ImageTk.PhotoImage(imagen_fondo_seleccioando)


    listaParedesIds = []
    for fila in range(22):  
        for columna in range(12):
            x1 = columna * contante_x
            y1 = fila * contante_y
            x2 = x1 + contante_x
            y2 = y1 + contante_y

            
            if fila == 0 or fila == 21:
                paredId = canvas_pantalla.create_image((x1 + x2) / 2, (y1 + y2) / 2, anchor="center", image=imagen_paredTk)
                listaParedesIds += [paredId]
            else:
                if columna == 0 or columna == 11:
                    paredId = canvas_pantalla.create_image((x1 + x2) / 2, (y1 + y2) / 2, anchor="center", image=imagen_paredTk)
                    listaParedesIds += [paredId]
                else:
                    area_fondo = canvas_pantalla.create_image((x1 + x2) / 2, (y1 + y2) / 2, anchor="center", image=imagen_fondoTk)
                    
                    canvas_pantalla.tag_bind(area_fondo, "<Button-1>", lambda evento:seleccionar_obstaculo(canvas_pantalla, evento, fondo_seleccionadoTk, listaParedesIds))
                    canvas_pantalla.tag_bind(area_fondo, "<Button-3>", lambda evento:quitar_obstaculo(canvas_pantalla, evento, imagen_fondoTk, listaParedesIds))

            
    canva_demostrativo = Canvas(canvas_gameboy, width=235, height=178, bg="pink")
    canva_demostrativo.place(x=305, y=567)

    
    consola.mainloop() # bucle


"""
Nombre: salir
Entrada: ventana
Salida: Cierra (destruye) la ventana
Restricciones: Las necesarias para el correcto funcionamiento
"""
def salir(ventana):
    ventana.destroy()


ventana_inicio()