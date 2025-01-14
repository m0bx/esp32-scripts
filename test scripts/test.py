def count_bits(pulses, threshold=1000):
    pulses = pulses[1:]  # Skip the initial long start pulse
    bits = 0

    for i in range(1, len(pulses), 2):  # Only check gaps (every second value)
        if i + 1 < len(pulses):
            gap = pulses[i]
            if gap < threshold:
                bits += 1  # Short gap -> one bit (either 0 or 1)

    return bits

# Example pulses
pulses = [16320, 2366, 585, 1173, 587, 532, 587, 576, 597, 1166, 587, 1185, 588, 576, 587, 576, 598, 1160, 587, 577, 587, 585, 587, 1177, 587, 1196, 565, 1176, 585, 578, 582, 1188, 19739, 2397, 555, 1210, 554, 607, 566, 598, 566, 1198, 560, 1177, 587, 577, 585, 609, 565, 1166, 596, 577, 587, 576, 588, 1177, 582, 1176, 588, 1174, 598, 576, 587, 1174, 19741]

# Count the number of bits
bits = count_bits(pulses)
print(f"Number of bits: {bits}")