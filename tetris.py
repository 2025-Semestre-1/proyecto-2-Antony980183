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
    print(f'{ancho}x{alto}+{x}+{y}')


"""
Nombre: ventana_inicio
Entraeda: Ninguna
Salida: La ventana inicial, iniciara el juego o finalizara el programa
Restricciones: Las necesarias para el correcto funcionamiento
"""
def ventada_inicio():
    ventana_inicial = Tk()
    ventana_inicial.geometry("500x300")
    ventana_inicial.resizable(0,0)
    centrar_ventana(ventana_inicial)
    
    boton_jugar = Button(ventana_inicial, text="Jugar", 
                         font=("Arial", 25, "bold")).pack()
    
    boton_salir = Button(ventana_inicial, 
                         text="Salir", 
                         font=("Arial", 25, "bold"), 
                         command= lambda arg = ventana_inicial: salir(ventana_inicial)).pack()
    
    ventana_inicial.mainloop()


"""
Nombre: salir
Entrada: ventana
Salida: Cierra (destruye) la ventana
Restricciones: Las necesarias para el correcto funcionamiento
"""
def salir(ventana):
    ventana.destroy()


ventada_inicio()