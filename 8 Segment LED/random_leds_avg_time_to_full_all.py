from machine import Pin
import random
from time import sleep, ticks_ms

def toggle_random_pin():
    index = random.randint(0, len(pins) - 1)
    pin_states[index] = 0 if pin_states[index] == 1 else 1
    pins[index].value(pin_states[index])

def update_avg(current_avg, count, new_value):
    return (current_avg * count + new_value) / (count + 1)

pins = [Pin(27, Pin.OUT), Pin(26, Pin.OUT), Pin(25, Pin.OUT),
        Pin(33, Pin.OUT), Pin(32, Pin.OUT), Pin(14, Pin.OUT), Pin(12, Pin.OUT)]

pin_states = [1] * len(pins)

# Initialize pins to their starting states
for pin, state in zip(pins, pin_states):
    pin.value(state)

average_time = 0  # Running average
count = 0  # Count of times all pins are turned off
current_time = ticks_ms()

while True:
    toggle_random_pin()
    if all(state == 0 for state in pin_states):
        ctt = ticks_ms() - current_time  # Time taken for this iteration
        current_time = ticks_ms()  # Reset the start time for the next iteration
        count += 1
        average_time = update_avg(average_time, count - 1, ctt)
        print("All pins are 0, it took ", ctt / 1000, " seconds")
        print("The average time is ", average_time / 1000, " seconds")
        
    sleep(0.01)
