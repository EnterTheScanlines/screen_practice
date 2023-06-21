from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
import framebuf
import utime

WIDTH = 128
HEIGHT = 64

i2c = I2C(0, scl=Pin(9), sda=Pin(8), freq=200000)
oled = SSD1306_I2C(WIDTH, HEIGHT, i2c)

# Raspberry Pi logo as 32x32 bytearray
logo_data = bytearray(b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00|?\x00\x01\x86@\x80\x01\x01\x80\x80\x01\x11\x88\x80\x01\x05\xa0\x80\x00\x83\xc1\x00\x00C\xe3\x00\x00~\xfc\x00\x00L'\x00\x00\x9c\x11\x00\x00\xbf\xfd\x00\x00\xe1\x87\x00\x01\xc1\x83\x80\x02A\x82@\x02A\x82@\x02\xc1\xc2@\x02\xf6>\xc0\x01\xfc=\x80\x01\x18\x18\x80\x01\x88\x10\x80\x00\x8c!\x00\x00\x87\xf1\x00\x00\x7f\xf6\x00\x008\x1c\x00\x00\x0c \x00\x00\x03\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")

logo_fb = framebuf.FrameBuffer(logo_data, 32, 32, framebuf.MONO_HLSB)

def draw_frame():
    # Dibujar el marco alrededor de todo el display
    oled.rect(0, 0, WIDTH-1, HEIGHT-1, 1)
    oled.show()

# Mostrar textos estáticos, el logo de Raspberry Pi y dibujar el marco inicial
oled.text("Suscríbete", 10, 20)
oled.text("2021", 45, 30)
oled.blit(logo_fb, 96, 0)
draw_frame()

while True:
    oled.fill(0)  # Limpiar la pantalla
    oled.text("2023", 45, 40)  # Mostrar el texto parpadeante
    oled.text("Mecatronica", 10, 20)  # Mostrar el texto estático
    oled.text("curso", 40, 30)  # Mostrar el texto estático
    oled.blit(logo_fb, 96, 5)  # Mostrar el logo de Raspberry Pi
    draw_frame()  # Dibujar el marco
    utime.sleep(0.5)  # Esperar 0.5 segundos
    
    oled.fill(0)  # Limpiar la pantalla
    oled.text("Mecatronica", 10, 20)  # Mostrar el texto estático
    oled.text("curso", 40, 30)  # Mostrar el texto estático
    oled.blit(logo_fb, 96, 5)  # Mostrar el logo de Raspberry Pi
    draw_frame()  # Dibujar el marco
    utime.sleep(0.5)  # Esperar 0.5 segundos

    



