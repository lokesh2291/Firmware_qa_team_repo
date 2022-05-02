import serial
ser = serial.Serial('/dev/ttyUSB0', 230400)

while True:
     data = ser.readline()
     if data:
         print(data)
