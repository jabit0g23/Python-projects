import qrcode
from flet import app, Page, TextField, ElevatedButton, Column, Image, ImageFit

def main(page: Page):
    def btn_click(e):
        codigo_qr = qrcode.QRCode(
            version=1,
            box_size=10,
            border=4,
        )
        codigo_qr.add_data(texto.value)
        imagen_qr = codigo_qr.make_image(fill_color='black', back_color='white')
        imagen_qr.save('codigo_qr.png')

        imagen_col.controls.append(Image(src='codigo_qr.png', width=400, height=400, fit=ImageFit.CONTAIN))
        page.update()

    texto = TextField(label='Introduce aquí tu texto')
    boton = ElevatedButton('Generar')
    imagen_col = Column(expand=1, wrap=False, scroll='AUTO')

    boton.on_click = btn_click

    page.add(texto, boton, imagen_col)

app(target=main)