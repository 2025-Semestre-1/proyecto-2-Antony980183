from tkinter import  *
from PIL import Image, ImageTk


def hola(evento):
    print(type(evento))
    print(evento)

def imagen1(evento):
    print(type(evento))
    print("imagen1")

def imagen2(evento):
    print(type(evento))
    print("imagen2")


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
            
            if i >= 1 and i <= 20:
                if j == 0 or j == 11:
                    vector += ["+"]
                else:
                    vector += ["0"]
        print(vector)
        matriz += [vector]
    #print(matriz)

crear_matriz()




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
    canvas_pantalla.place(x=67, y=85)


    






    contante_x = 39
    contante_y = 16.68

    matriz_obstaculos = []

    for fila in range(22):
        vector_obstaculos = []
        for columna in range(12):
            x1 = columna * contante_x
            y1 = fila * contante_y
            x2 = x1 + contante_x
            y2 = y1 + contante_y


            area_obstaculo = canvas_pantalla.create_rectangle(x1, y1, x2, y2, outline="red", fill="")
            
            obstaculo = canvas_pantalla.tag_bind(area_obstaculo, "<Enter>", imagen1)       
            obstaculo = canvas_pantalla.tag_bind(area_obstaculo, "<Leave>", imagen2)       
            obstaculo = canvas_pantalla.tag_bind(area_obstaculo, "<Button-1>", hola)       

            vector_obstaculos += [obstaculo]

        matriz_obstaculos += [vector_obstaculos]

    


        
    print(matriz_obstaculos)
    print(len(matriz_obstaculos[0]))
    print(len(matriz_obstaculos))
            
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


#Wventana_inicio()