"""
main.py

    Demo program that displays temperature, determined by the built-in temperature sensor
    on a GC9A01 display through Plus Jakarta Sans font.

@Author: Mert AKSOY
"""

from machine import Pin, SPI, ADC
import plus_jakarta_sans_32 as font_32
import plus_jakarta_sans_64 as font_64
import utime

import gc9a01
adc = ADC(4)


def main():
    spi = SPI(1, baudrate=60000000, sck=Pin(10), mosi=Pin(11))
    tft = gc9a01.GC9A01(
        spi,
        240,
        240,
        reset=Pin(12, Pin.OUT),
        cs=Pin(9, Pin.OUT),
        dc=Pin(8, Pin.OUT),
        backlight=Pin(25, Pin.OUT),
        rotation=0)

    tft.init()
    bg_color = gc9a01.color565(255, 87, 34)
    tft.fill(bg_color)

    def determineTemperature():
        ADC_voltage = adc.read_u16() * (3.3 / 65535)
        return 27 - (ADC_voltage - 0.706) / 0.001721

    def center(font, s, row, color=gc9a01.WHITE):
        screen = tft.width()
        width = tft.write_len(font, s)
        if width and width < screen:
            col = tft.width() // 2 - width // 2
        else:
            col = 0
        tft.write(font, s, col, row, color, bg_color)

    while True:
        mid_row = int((tft.height() / 2) - (font_64.HEIGHT / 2))

        center(font_32, "Temp.", mid_row - font_32.HEIGHT)

        tft.fill_rect(0, mid_row, tft.width(), font_64.HEIGHT, bg_color)
        center(font_64, "{:.1f}C".format(determineTemperature()), mid_row)

        # Slider Bullets
        center(font_32, ". . : . .", tft.height() - font_32.HEIGHT - 5)

        utime.sleep(1)


main()
