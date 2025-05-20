from tkinter import  *
from PIL import Image, ImageTk

"""
Nombre: centrar_ventana
Entrada: ventana
Salida: La ventana reposicionada en el 'centro' de la pantalla
Restricciones: Las necesarias para el correcto funcionamiento
"""
def centrar_ventana(ventana):
    ventana.update_idletasks()# realiza todos los ewventos pendientes
    ancho = ventana.winfo_width()# saca el ancho  (x)
    alto = ventana.winfo_height()# saca el alto (y)
    x = (ventana.winfo_screenwidth() // 2) - (ancho // 2) # winfo_screenwidth() obtiene el ancho de la pantalla
    y = (ventana.winfo_screenheight() // 2) - (alto // 2)  # winfo_screenheight() obtiene el alto de la pantalla
    ventana.geometry(f'{ancho}x{alto}+{x}+{y}') # resposiciona la venrana


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
    canvas_pantalla.place(x=67, y=47)


    x1 = 0
    x2 = 38.75

    y1 = 0
    y2 = 16.6363

    cordenada_x = 0,0
    cordenada_y = 0,0


    for fila in range(13):
        for columna in range(23): 
            cordenada_x = (fila * x1, columna * y1)
            cordenada_y = (fila * x2, columna * y2)

            canvas_pantalla.create_rectangle(cordenada_x, cordenada_y, outline="blue", fill="")
    
    canva_demostrativo = Canvas(canvas_gameboy, width=225, height=178, bg="pink")
    canva_demostrativo.place(x=318, y=545)

    
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