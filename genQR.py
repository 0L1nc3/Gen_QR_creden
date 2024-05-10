import qrcode


class GeneradorCodigoQR:
    def __init__(self, contenido, nombre_archivo):
        self.contenido = contenido
        self.nombre_archivo = nombre_archivo

    def generar_codigo_qr(self):
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(self.contenido)
        qr.make(fit=True)

        imagen_qr = qr.make_image(fill_color="black", back_color="white")
        imagen_qr.save(self.nombre_archivo)

        print(f"El código QR se ha generado y guardado en {self.nombre_archivo}.")


if __name__ == "__main__":
    contenido = "¡Hola, este es un código QR en Python!"
    nombre_archivo = "codigo_qr.png"

    generador = GeneradorCodigoQR(contenido, nombre_archivo)
    generador.generar_codigo_qr()
