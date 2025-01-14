from machine import Pin
import time

# Pin definitions
pins = {
    26: Pin(26, Pin.OUT),  # top
    32: Pin(32, Pin.OUT),  # right up
    33: Pin(33, Pin.OUT),  # right down
    14: Pin(14, Pin.OUT),  # middle
    12: Pin(12, Pin.OUT),  # bottom
    27: Pin(27, Pin.OUT),  # left down
    25: Pin(25, Pin.OUT),  # left up
}

# Mapping for segments to each number (0-9)
digit_segments = {
    0: [26, 32, 33, 25, 27, 12],       # 0
    1: [32, 33],                        # 1
    2: [26, 32, 14, 27, 12],            # 2
    3: [26, 32, 14, 33, 12],            # 3
    4: [25, 32, 14, 33],                # 4
    5: [26, 25, 14, 33, 12],            # 5
    6: [26, 25, 27, 14, 33, 12],        # 6
    7: [26, 32, 33],                    # 7
    8: [26, 32, 33, 25, 27, 14, 12],    # 8
    9: [26, 32, 33, 25, 14, 12],        # 9
}

# Function to turn off all pins
def turn_off_all():
    for pin in pins.values():
        pin.value(1)

# Function to display a number
def display_number(number):
    # Turn off all pins before displaying the new number
    turn_off_all()
    
    # Turn on the necessary pins for the number
    if number in digit_segments:
        for pin_num in digit_segments[number]:
            pins[pin_num].value(0)

# Example of displaying numbers from 0-9
try:
    while True:
        for num in range(10):
            display_number(num)
            time.sleep(0.1)  # Wait for 1 second to display each number
except KeyboardInterrupt:
    turn_off_all()  # Turn off all pins when exiting
