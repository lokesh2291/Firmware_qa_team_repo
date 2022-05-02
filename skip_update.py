import serial
import time
from keyboard import press
COM_PORT='/dev/ttyUSB0'
COM_BAUD=230400
STR_TO_LOOK_FOR=[b'Press any key to skip update']
def init_serial():
        ser = serial.Serial(COM_PORT, timeout=30)
        ser.baudrate = COM_BAUD
        ser.bytesize = 8
        ser.parity   = 'N'
        ser.stopbits = 1
        return ser

if __name__ == "__main__":
        ser = init_serial()
        # readline until we get one of string we are
        # looking for or readline timeout
        while True:
            line = ser.readline()
            print(line)
            if line == '':


            # got timeout
                break
            line = line.rstrip()

            if STR_TO_LOOK_FOR[0] in line:
                    print ("Skipping update ****")
                    press('enter')
                    break
