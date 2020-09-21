import serial

ser = serial.Serial('/dev/ttyACMO0')
print(ser.name)
ser.write(b'hello')
ser.close()
