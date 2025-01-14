from machine import Pin, SoftSPI
from mfrc522 import MFRC522

sck=18
mosi=23
miso=19
rst=4
cs=5

spi = SoftSPI(baudrate=100000, polarity=0, phase=0, sck=sck, mosi=mosi, miso=miso)
spi.init()

rdr = MFRC522(spi=spi, gpioRst=4, gpioCs=5)
sda = Pin(5, Pin.OUT)

def do_write():
    print("")
    print("Place card before reader to write address 0x08")
    print("")

    try:
        while True:

			(stat, tag_type) = rdr.request(rdr.REQIDL)

			if stat == rdr.OK:

				(stat, raw_uid) = rdr.anticoll()

				if stat == rdr.OK:
					print("New card detected")
					print("  - tag type: 0x%02x" % tag_type)
					print("  - uid	 : 0x%02x%02x%02x%02x" % (raw_uid[0], raw_uid[1], raw_uid[2], raw_uid[3]))
					print("")

					if rdr.select_tag(raw_uid) == rdr.OK:

						key = bytearray([0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF])

						if rdr.auth(rdr.AUTHENT1A, 8, key, raw_uid) == rdr.OK:
							stat = rdr.write(8, b"\x4B\x4B\x4B\x4B\x4B\x4B\x4B\x4B\x4B\x4B\x4B\x4B\x4B\x4B\x4B\x4B")
							rdr.stop_crypto1()
							if stat == rdr.OK:
								print("Data written to card")
							else:
								print("Failed to write data to card")
						else:
							print("Authentication error")
					else:
						print("Failed to select tag")

    except KeyboardInterrupt:
        print("Bye")

do_write()