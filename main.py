import qrcode

# Contenido que deseas codificar en el código QR
contenido = f"LECHERIA DEL ALTIPLANO LEDAL S.A.\nNombre: Javier Aduviri Mamani\nCarnet: 2520985-1E\nProvincia: Ingavi\nSerie: 'C'"

# Genera el código QR
qr = qrcode.QRCode(
    version=1,  # Versión del código QR
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # Nivel de corrección de errores
    box_size=10,  # Tamaño de cada "caja" del código QR
    border=4,  # Margen alrededor del código QR
)
qr.add_data(contenido)
qr.make(fit=True)

# Crea una imagen del código QR
imagen_qr = qr.make_image(fill_color="black", back_color="white")

# Guarda la imagen en un archivo
nombre_archivo = "qr_48.png"
imagen_qr.save(nombre_archivo)

print(f"El código QR se ha generado y guardado en {nombre_archivo}.")
