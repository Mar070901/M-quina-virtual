import tkinter as tk
from tkinter import messagebox, scrolledtext
from PIL import Image, ImageTk  # Asegúrate de tener Pillow instalado
from maquina_virtual import MaquinaVirtual
from traductor import generar_programa_mar

MAX_LETRAS = 10  # Límite máximo de letras

def actualizar_recuento(event=None):
    texto = texto_input.get("1.0", tk.END).strip()
    letras = [c for c in texto if c.isalpha()]  # Solo contar letras
    recuento = len(letras)
    recuento_label.config(text=f"Letras: {recuento}/{MAX_LETRAS}")

    # Si el recuento supera el máximo, truncamos el texto
    if recuento > MAX_LETRAS:
        messagebox.showwarning("Advertencia", f"Máximo de {MAX_LETRAS} letras alcanzado.")
        texto_input.delete("1.0", tk.END)
        texto_input.insert(tk.END, ''.join(letras[:MAX_LETRAS]))
        recuento_label.config(text=f"Letras: {MAX_LETRAS}/{MAX_LETRAS}")
        return

def ejecutar_traductor():
    texto = texto_input.get("1.0", tk.END).strip()  # Obtiene el texto del área de texto
    if not texto:
        messagebox.showwarning("Advertencia", "Por favor, ingrese algún texto.")
        return

    # Generar y guardar el programa .mar solo cuando se presiona el botón de traducir
    nombre_archivo_mar = 'C:/Users/mar_a/OneDrive/Escritorio/3º/LYP/MV/programa.mar'  # Ruta del archivo .mar
    generar_programa_mar(texto, nombre_archivo_mar)

    # Leer el programa generado y convertir a lista de instrucciones
    with open(nombre_archivo_mar, 'r') as archivo:
        programa = []
        for line in archivo:
            parts = line.strip().split()
            if len(parts) == 2 and parts[0] == 'push':
                programa.append((parts[0], int(parts[1])))
            else:
                programa.append((parts[0],))

    # Crear e iniciar la máquina virtual
    mv = MaquinaVirtual()
    mv.cargar_programa(programa)
    mv.ejecutar()

def salir():
    ventana.quit()  # Cierra la aplicación

# Configuración de la ventana principal
ventana = tk.Tk()
ventana.title("Transcriptor")
ventana.geometry("500x400")
ventana.config(bg="#f0f0f0")  # Color de fondo suave

# Cargar la imagen de fondo y ajustarla al tamaño de la ventana
try:
    fondo_image = Image.open("C:/Users/mar_a/OneDrive/Escritorio/3º/LYP/MV/fondo.png")  # Asegúrate de que la ruta sea correcta
    fondo_image = fondo_image.resize((500, 400))  # Redimensionar imagen de fondo
    fondo_photo = ImageTk.PhotoImage(fondo_image)
    fondo_label = tk.Label(ventana, image=fondo_photo)
    fondo_label.place(relwidth=1, relheight=1)  # Establece la imagen como fondo
except Exception as e:
    print(f"Error al cargar la imagen de fondo: {e}")

# Crear un área de texto para ingresar el texto
texto_input = scrolledtext.ScrolledText(ventana, height=10, width=60, font=("Arial", 12), wrap=tk.WORD)
texto_input.pack(pady=20, padx=20)
texto_input.bind("<KeyRelease>", actualizar_recuento)  # Actualizar recuento al escribir

# Etiqueta para mostrar el recuento de letras
recuento_label = tk.Label(ventana, text=f"Letras: 0/{MAX_LETRAS}", bg="#f0f0f0", font=("Arial", 10))
recuento_label.pack()

# Cargar la imagen del botón de traducir y ajustarla
traducir_photo = None  # Inicializamos la variable antes del bloque try
try:
    traducir_image = Image.open("C:/Users/mar_a/OneDrive/Escritorio/3º/LYP/MV/traducir.png")  # Asegúrate de que la ruta sea correcta
    traducir_image = traducir_image.resize((150, 50))  # Ajustar tamaño del botón de traducir
    traducir_photo = ImageTk.PhotoImage(traducir_image)
except Exception as e:
    print(f"Error al cargar la imagen del botón de traducir: {e}")

# Crear un botón para ejecutar el traductor
boton_ejecutar = tk.Button(ventana, image=traducir_photo, command=ejecutar_traductor, 
                            bg="#4CAF50", relief=tk.RAISED, bd=3)
boton_ejecutar.pack(pady=10)

# Cargar la imagen del botón de salir y ajustarla
salir_photo = None  # Inicializamos la variable antes del bloque try
try:
    salir_image = Image.open("C:/Users/mar_a/OneDrive/Escritorio/3º/LYP/MV/salir.png")  # Asegúrate de que la ruta sea correcta
    salir_image = salir_image.resize((150, 50))  # Ajustar tamaño del botón de salir
    salir_photo = ImageTk.PhotoImage(salir_image)
except Exception as e:
    print(f"Error al cargar la imagen del botón de salir: {e}")

# Crear un botón para salir
boton_salir = tk.Button(ventana, image=salir_photo, command=salir, 
                        bg="#f44336", relief=tk.RAISED, bd=3)
boton_salir.pack(pady=10)

# Iniciar el bucle principal de la interfaz
ventana.mainloop()
