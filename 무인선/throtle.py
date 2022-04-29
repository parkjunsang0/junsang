import serial
import time
import pigpio

pi2=pigpio.pi()

port = "/dev/ttyACM0"
serialFromArduino = serial.Serial(port,9600)

while True:
    input_s=serialFromArduino.readline()
    input_s =input_s.decode('utf-8')
    input=input_s.replace("\r\n","")
    CH_2=int(input[4:8])
    CH_1=int(input[0:4])
    print(CH_1)
    print(CH_2)
    throtle=1500-CH_2
    if throtle==0:
    pi2.set_servo_pulsewidth(19,CH_1)
    pi2.set_servo_pulsewidth(9,CH_1)

    elif throtle<0:
        pi2.set_servo_pulsewidth(19,input+abs(throtle))
        pi2.set_servo_pulsewidth(9, input-abs(throtle))

    elif throtle>0:
        pi2.set_servo_pulsewidth(19, input-throtle)
        pi2.set_servo_pulsewidth(9, input-throtle)





