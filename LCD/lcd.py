import machine
from machine import Pin, SoftI2C
from lcd_api import LcdApi
from i2c_lcd import I2cLcd
from time import sleep
import json
"""
def load_wordcounts(filename="word_frequencies.json"):
    try:
        with open(filename, 'r') as f:
            word_counts = json.load(f)
        print("Word counts loaded successfully!")
    except Exception as e:
        print(f"Failed to load word counts: {e}")
        word_counts = {}
    return word_counts
    
words = load_wordcounts()
"""
I2C_ADDR = 0x27
totalRows = 4
totalColumns = 20

i2c = SoftI2C(scl=Pin(22), sda=Pin(21), freq=10000)
lcd = I2cLcd(i2c, I2C_ADDR, totalRows, totalColumns)

pt = bytearray([0x00,0x00,0x00,0x0E,0x0E,0x0E,0x00,0x00])
lcd.custom_char(0, pt)
lcd.putstr("Top 3 words:")
