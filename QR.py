import qrcode
from PIL import Image
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import ImageTk, Image

# Función para generar el código QR y mostrarlo en la GUI
def generar_qr():
    texto = entrada_texto.get()
    if not texto:
        messagebox.showerror("Error", "Por favor, ingrese texto o enlace.")
        return
    
    # Crear el objeto QRCode
    qcode = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
    )

    qcode.add_data(texto)
    qcode.make(fit=True)

    # Crear la imagen del código QR con colores personalizados
    global img_qr
    img_qr = qcode.make_image(fill_color="black", back_color="white")
    img_qr = img_qr.resize((250, 200))  # Cambiar tamaño para mostrar en la GUI
    img_qr_tk = ImageTk.PhotoImage(img_qr)

    # Mostrar la imagen en la etiqueta de la GUI
    etiqueta_imagen.config(image=img_qr_tk)
    etiqueta_imagen.image = img_qr_tk

# Función para guardar la imagen del código QR generado
def guardar_qr():
    if img_qr:
        archivo = filedialog.asksaveasfilename(defaultextension=".png",
                                               filetypes=[("PNG files", "*.png")])
        if archivo:
            img_qr.save(archivo)
            messagebox.showinfo("Guardado", "El código QR se ha guardado correctamente.")
    else:
        messagebox.showerror("Error", "Primero genere un código QR.")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Código QR")
ventana.geometry("410x430")

# Crear los elementos de la GUI
etiqueta_texto = tk.Label(ventana, text="Ingrese el texto o enlace:", font ='arial 13')
etiqueta_texto.pack(pady=10)

entrada_texto = tk.Entry(ventana, width=40, font ='arial 13') 
entrada_texto.pack(pady=5)

boton_generar = tk.Button(ventana, text="Generar Código QR", command=generar_qr, font ='arial 13')
boton_generar.pack(pady=10)

etiqueta_imagen = tk.Label(ventana)
etiqueta_imagen.pack(pady=10)

boton_guardar = tk.Button(ventana, text="Guardar Código QR", command=guardar_qr, font ='arial 13')
boton_guardar.pack(pady=10)

# Inicializar la variable global para la imagen QR
img_qr = None

# Ejecutar la aplicación
ventana.mainloop()
