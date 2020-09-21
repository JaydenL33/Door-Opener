import serial

ser = serial.Serial('/dev/ttyACM0')
print(ser.name)
ser.write(b'hello')
ser.close()
