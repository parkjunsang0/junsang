import serial
import time
import pigpio

pi2=pigpio.pi()

port = "/dev/ttyACM0"
serialFromArduino = serial.Serial(port,9600)

while True:
    input_s=serialFromArduino.readline()
    input_s=input_s.decode('utf-8')
    input=input_s.replace("\r\n","")
    CH_1=int(input[0:4])
    CH_2=int(input[5:9])
    print(CH_1)
    print(CH_2)
    throtle = abs(1500 - CH_1)
    #19핀이 오른쪽 추진기 9핀이 왼쪽 추진기
    if CH_2 > 1500:
        if 1500 - CH_1 < 0:
            pi2.set_servo_pulsewidth(19, CH_2 - throtle)
            pi2.set_servo_pulsewidth(9, CH_2)
        elif 1500 - CH_1 > 0:
            pi2.set_servo_pulsewidth(19, CH_2)
            pi2.set_servo_pulsewidth(9, CH_2 - throtle)
        else:
            pi2.set_servo_pulsewidth(19, CH_2)
            pi2.set_servo_pulsewidth(9, CH_2)


    elif CH_2 < 1500:
        if 1500 - CH_1 < 0:
            pi2.set_servo_pulsewidth(19, CH_2 + throtle)
            pi2.set_servo_pulsewidth(9, CH_2)
        elif 1500 - CH_1 > 0:
            pi2.set_servo_pulsewidth(19, CH_2)
            pi2.set_servo_pulsewidth(9, CH_2 + throtle)
        else:
            pi2.set_servo_pulsewidth(19, CH_2)
            pi2.set_servo_pulsewidth(9, CH_2)



    else:
        if 1500 - CH_1 < 0:
            pi2.set_servo_pulsewidth(19, 1500 - throtle)
            pi2.set_servo_pulsewidth(9, 1500 + throtle)
        elif 1500 - CH_1 > 0:
            pi2.set_servo_pulsewidth(19, 1500 + throtle)
            pi2.set_servo_pulsewidth(9, 1500 - throtle)
        else:
            pi2.set_servo_pulsewidth(19, 1500)
            pi2.set_servo_pulsewidth(9, 1500)



