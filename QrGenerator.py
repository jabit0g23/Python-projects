import flet as ft
import qrcode

def main(page: ft.Page):
  def btn_click(e):
    codigo_qr = qrcode.QRCode(
      version = 1,
      box_size = 10,
      border = 4,
      )
    codigo_qr = codigo_qr.make_image(fill_color='black', back_color='white')

  texto = ft.TextField(label='Introduce aqui tu texto')
  boton = ft.ElevatedButton('Generar')
  imagen_col = ft.Column(expand=1, wrap=False,scroll='AUTO')