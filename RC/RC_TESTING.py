import serial
import pigpio
import time

pi2=pigpio.pi()
port="/dev/ttyACM0"
serialfromArduino=serial.Serial(port,9600)
while True:
    try:
        input_s = serialfromArduino.readline()
        input_s = input_s.decode("latin-1")
        input_s = input_s.replace(" ","")
        input = input_s.replace("\r\n", "")
        #print(input_s)
        print(input)
    except (ValueError, IOError) as err:
        print(err)
