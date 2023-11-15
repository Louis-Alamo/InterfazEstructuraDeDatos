from tkinter import Tk
import customtkinter
from interfaz_grafica.componentes_personalizados.componentes_multiples.MenuConBoton import MenuConBoton

def funcion_menu():
    print("menu")

def obtener_seleccion():
    print(menu.variable.get())




app = Tk()
lista = ["opcion 1" , "opcion 2", "opcion 3"]
variable = lista[0]
menu = MenuConBoton(app, lista_opciones=lista, nombre_funcion_boton=obtener_seleccion, variable=variable)
menu.pack()
# optionmenu_var = customtkinter.StringVar(value="option 2")
# optionmenu = customtkinter.CTkOptionMenu(app,values=["Eliminar nodo x", "option 2"],
#                                          command=optionmenu_callback,width=602, height=44,font=("Arial",15, "bold"),text_color="#4E458E",fg_color="#FFFFFF",button_color="#FFFFFF",
#                                          dropdown_fg_color="#FFFFFF",dropdown_text_color="#4E458E",dropdown_font=("Arial",15, "bold"), variable=optionmenu_var)
# optionmenu.pack()

app.mainloop()