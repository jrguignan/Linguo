#Lingo 2.0 ingles para convertir en .exe
import tkinter as tk
from tkinter import messagebox
import csv
import os
import pygame
from PIL import Image, ImageTk

#Funcion para obtener el path absoluto
def resource_path(relative_path):
 try:
# PyInstaller creates a temp folder and stores path in _MEIPASS 
   base_path = sys._MEIPASS
 except Exception:
   base_path = os.path.abspath(".")
 return os.path.join(base_path, relative_path)


def cargar_diccionario(csv_file):
    lista_palabras = []
    with open(csv_file, newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            if len(row) == 2:
                lista_palabras.append((row[0].strip(), row[1].strip()))
    return lista_palabras

diccionario = cargar_diccionario(resource_path("vocabulario.csv"))
indice_actual = 0

def mostrar_info():
    info_ventana = tk.Toplevel(tk_root)
    info_ventana.title("Información del Programa")
    info_ventana.geometry("550x400")
    info_ventana.configure(bg="#444444")
    
    # Cargar y mostrar el logo
    logo_img = Image.open(resource_path("logo/logo.ico"))
    logo_img = logo_img.resize((100, 100), Image.LANCZOS)
    logo_tk = ImageTk.PhotoImage(logo_img)
    label_logo = tk.Label(info_ventana, image=logo_tk, bg="#444444")
    label_logo.image = logo_tk
    label_logo.pack(pady=(10, 5))
    
    label_titulo = tk.Label(info_ventana, text="Linguo 2.0", font=("Arial", 14, "bold"), fg="white", bg="#444444")
    label_titulo.pack()
    
    texto_info = (
        "🌟 Bienvenido a Linguo 2.0 🎉🎧 \n"
        "Este software te ayudará a mejorar tu vocabulario en inglés. 🚀📖\n\n"
        "📌 Características:\n"
        "✔️ Muestra palabras en inglés y sus traducciones.\n"
        "✔️ Reproducción de pronunciación en audio.\n"
        "✔️ Interfaz fácil de usar.\n\n"
        "👨‍💻 Creado por: José R. Guignan. 🚀✨ \n\n "
        "💡 ¡Gracias por usar Linguo 2.0! 💙\n"
        
    )
    label_info = tk.Label(info_ventana, text=texto_info, font=("Arial", 11), fg="white", bg="#444444", justify="left")
    label_info.pack(padx=20, pady=10)

def actualizar_botones():
    btn_anterior.config(state=tk.NORMAL if indice_actual > 0 else tk.DISABLED)
    btn_siguiente.config(state=tk.NORMAL if indice_actual < len(diccionario) - 1 else tk.DISABLED)

def mostrar_palabra():
    global indice_actual
    if diccionario:
        palabra_ingles, _ = diccionario[indice_actual]
        label_palabra.config(text=palabra_ingles)
        label_traduccion.config(text="¿  . . .  ?")
        actualizar_botones()

def mostrar_traduccion():
    global indice_actual
    if diccionario:
        _, traduccion = diccionario[indice_actual]
        label_traduccion.config(text=traduccion)

def pronunciar():
    global indice_actual
    if diccionario:
        palabra_ingles, _ = diccionario[indice_actual]
        palabra_ingles = palabra_ingles.replace(" ", "_").replace("...", "").replace("-", "_").replace("'", "_").replace("?", "")
        audio_file = f"audio/{palabra_ingles}.mp3"
        if os.path.exists(audio_file):
            os.system(f"start {resource_path(audio_file)}" if os.name == "nt" else f"mpg321 {audio_file}")
        else:
            messagebox.showwarning("Audio no encontrado", "No se encontró el archivo de audio para esta palabra.")

def siguiente_palabra():
    global indice_actual
    if indice_actual < len(diccionario) - 1:
        indice_actual += 1
        mostrar_palabra()

def anterior_palabra():
    global indice_actual
    if indice_actual > 0:
        indice_actual -= 1
        mostrar_palabra()

tk_root = tk.Tk()
tk_root.title("Linguo 2.0")
tk_root.geometry("1000x700")
tk_root.configure(bg="#2E2E2E")
tk_root.iconbitmap(resource_path("logo/logo.ico"))

frame_titulo = tk.Frame(tk_root, bg="#444444", height=100)
frame_titulo.pack(fill="x", padx=10, pady=10)
label_titulo = tk.Label(frame_titulo, text="Linguo 2.0 - Software Para Practicar Vocabulario", font=("Arial", 20, "bold"), fg="white", bg="#444444")
label_titulo.pack(side="left", padx=10)

btn_style = {
    "font": ("Arial", 16, "bold"),
    "fg": "#FFFFFF",
    "bg": "#444444",
    "activebackground": "#666666",
    "bd": 3,
    "padx": 20,
    "pady": 12,
}

label_palabra = tk.Label(tk_root, text="", font=("Arial", 44, "bold"), fg="#00FF00", bg="#2E2E2E")
label_palabra.pack(pady=20)

btn_traducir = tk.Button(tk_root, text="Ver Significado", command=mostrar_traduccion, **btn_style)
btn_traducir.pack(pady=10)

label_traduccion = tk.Label(tk_root, text="", font=("Arial", 44), fg="#0000FF", bg="#2E2E2E")
label_traduccion.pack(pady=10)

btn_pronunciar = tk.Button(tk_root, text="Escuchar Pronunciación", command=pronunciar, **btn_style)
btn_pronunciar.pack(pady=10)

frame_navegacion = tk.Frame(tk_root, bg="#2E2E2E")
frame_navegacion.pack(pady=20)

btn_anterior = tk.Button(frame_navegacion, text="⏪ Anterior", command=anterior_palabra, **btn_style)
btn_anterior.grid(row=0, column=0, padx=20)

btn_siguiente = tk.Button(frame_navegacion, text="Siguiente ⏩", command=siguiente_palabra, **btn_style)
btn_siguiente.grid(row=0, column=1, padx=20)

btn_info = tk.Button(tk_root, text="ℹ️ Info", font=("Arial", 12, "bold"), command=mostrar_info, bg="#555555", fg="white", bd=2)
btn_info.place(relx=1.0, rely=1.0, anchor="se", x=-10, y=-10)

mostrar_palabra()
tk_root.mainloop()
