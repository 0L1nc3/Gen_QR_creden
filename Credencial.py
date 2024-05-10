import re

import qrcode


class Credencial:
    def __init__(self, nombreDelArchivo):
        self.archivo_nombre = nombreDelArchivo
        self.datos = []

    def extraer_informacion(self):
        with open(self.archivo_nombre, 'r') as archivo:
            bloque = []
            for linea in archivo:
                if re.search(r'NOMBRE:', linea):
                    bloque.append(linea)
                elif re.search(r'C\.I\.', linea):
                    bloque.append(linea)
                elif re.search(r'PROVINCIA:', linea):
                    bloque.append(linea)
                elif re.search(r'SERIE:', linea):
                    bloque.append(linea)
                    self.procesar_bloque(bloque)
                    bloque = []

    def procesar_bloque(self, bloque):
        info = {
            "nombre": None,
            "carnet": None,
            "provincia": None,
            "serie": None
        }

        for linea in bloque:
            if re.search(r'NOMBRE:', linea):
                info["nombre"] = linea.split('NOMBRE: ')[1].strip().title()
            elif re.search(r'C\.I\.', linea):
                carnet_info = re.search(r'C\.I\. (\d+) ?([LQ-])', linea)
                if carnet_info:
                    carnet_numero = carnet_info.group(1)
                    carnet_letra = carnet_info.group(2)
                    if carnet_letra == 'L':
                        info["carnet"] = carnet_numero + ' LP.'
                    elif carnet_letra == 'Q':
                        info["carnet"] = carnet_numero + ' QR.'
                    elif carnet_letra == '-':
                        print(carnet_letra)
                        info["carnet"] = carnet_numero + carnet_letra
            elif re.search(r'PROVINCIA:', linea):
                info["provincia"] = linea.split('PROVINCIA: ')[1].strip().title()
            elif re.search(r'SERIE:', linea):
                info["serie"] = linea.split('SERIE: ')[1].strip().title()

        self.datos.append(info)

    def generar_qr(self):
        for i, info in enumerate(self.datos, start=1):
            contenido_qr = f"LECHERIA DEL ALTIPLANO LEDAL S.A.\nNombre: {info['nombre']}\nCarnet: {info['carnet']}\nProvincia: {info['provincia']}\nSerie: {info['serie']}"
            qr = qrcode.QRCode(
                version=1,  # Versión del código QR
                error_correction=qrcode.constants.ERROR_CORRECT_L,  # Nivel de corrección de errores
                box_size=10,  # Tamaño de cada "caja" del código QR
                border=4,  # Margen alrededor del código QR
            )
            qr.add_data(contenido_qr)
            qr.make(fit=True)
            imagen_qr = qr.make_image(fill_color="black", back_color="white")
            nombre_archivo_qr = f'qr_{i}.png'
            imagen_qr.save(nombre_archivo_qr)
            print(f'El código QR #{i} se ha generado y guardado en {nombre_archivo_qr}')


# Ejemplo de uso
archivo_nombre = 'CREDENCIALES 5TO LOTE 2024.txt'  # Reemplaza con la ruta de tu archivo
credencial = Credencial(archivo_nombre)

credencial.extraer_informacion()
credencial.generar_qr()
