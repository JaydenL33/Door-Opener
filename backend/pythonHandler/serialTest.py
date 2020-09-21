import serial

ser = serial.serial('/dev/ttyACMO0')
print(ser.name)
ser.write(b'hello')
ser.close()
