from machine import Pin
from time import ticks_us, ticks_diff

ir_pin = Pin(34, Pin.IN)

def read_pulses(pin, timeout=100000):
    pulses = []
    start_time = ticks_us()

    while ticks_diff(ticks_us(), start_time) < timeout:
        value = pin.value()
        pulse_start = ticks_us()
        while pin.value() == value:  # Wait for the value to change
            if ticks_diff(ticks_us(), pulse_start) > timeout:
                return pulses  # Timeout
        pulse_duration = ticks_diff(ticks_us(), pulse_start)
        pulses.append(pulse_duration)
    return pulses

# Function to filter out noise
def filter_pulses(pulses, max_pulse_length=25000):
    return [pulse for pulse in pulses if pulse < max_pulse_length]

# Function to decode pulses into bits
def decode_pulses(pulses, short_threshold=800, long_threshold=1500):
    if len(pulses) < 3:
        return None
    pulses = pulses[2:]  # Discard first few pulses (start bits)
    bits = []
    for i in range(0, len(pulses) - 1, 2):
        if pulses[i] <= short_threshold:
            bits.append(0)
        elif pulses[i] <= long_threshold:
            bits.append(1)
        else:
            break
    return bits

# Function to analyze the pulse array
def analyze_pulse_array(pulse_array):
    print("Analyzing:", pulse_array)  # You can replace this with actual analysis logic
    # Here you would do your analysis on the pulse_array, such as decoding it
    filtered_pulses = filter_pulses(pulse_array)
    bits = decode_pulses(filtered_pulses)
    if bits is not None and len(bits) >= 7:
        print("Decoded bits:", bits)
    else:
        print("Invalid pulse array, discarding.")

# Main loop to continuously capture and process IR pulses
pulse_buffer = []  # Array to store ongoing pulses
current_array = []  # Array to store pulses after a 10k+ pulse is found

while True:
    print("Waiting for signal...")
    pulses = read_pulses(ir_pin)

    if pulses:
        pulse_buffer.extend(pulses)  # Add the newly read pulses to the buffer
        print("Raw pulses:", pulses)  # Log raw pulses for debugging

        # Check if a 10k+ pulse is found
        for pulse in pulse_buffer:
            if pulse > 10000:  # Start a new array once a pulse > 10k is found
                if current_array:  # If current_array has data, analyze the previous array
                    analyze_pulse_array(current_array)
                current_array = []  # Reset current array to start new data collection
            current_array.append(pulse)

        # If we have a valid array (at least 7 bits and starts with a pulse > 10k), we proceed
        if current_array and current_array[0] > 10000 and len(current_array) > 7:
            analyze_pulse_array(current_array)  # Analyze the current pulse array
            current_array = []  # Reset after analysis
        else:
            # If the array doesn't meet the criteria, clear it
            if current_array and (current_array[0] <= 10000 or len(current_array) < 7):
                current_array = []  # Discard array if invalid

        print("---")

