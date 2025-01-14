from machine import Pin
from time import sleep

def playsound(state=int):
    """
        Sound 1 = Pin 19
        Sound 2 = Pin 18
        Sound 3 = Pin 5
        Sound 4 = Pin 17
        Sound 5 = Pin 16
        Sound 6 = Pin 4
        Sound 7 = Pin 0
        Sound 8 = Pin 2
    """
    pins = [19,18,5,17,16,4,0,2]
    play_from_this_pin = machine.Pin(pins[state], machine.Pin.OUT)
    play_from_this_pin.value(1)
    sleep(0.05)
    play_from_this_pin.value(0)
    
    
pin1 = machine.Pin(27, machine.Pin.OUT) # Button 1 OUT
pin2 = machine.Pin(26, machine.Pin.IN) # Button 1 IN
pin3 = machine.Pin(27, machine.Pin.OUT) # Button 2 OUT
pin4 = machine.Pin(14, machine.Pin.IN) # Button 2 IN

value1, value2 = 0,0
notice1, notice2 = False
state = 0

while True:
    value1_temp = pin2.value()
    value2_temp = pin4.value()
    if value1_temp != value1:
        state  = state + 1
        if state > 7:
            state = state - 8
    if value2_temp != value2:
        playsound(state)
    
