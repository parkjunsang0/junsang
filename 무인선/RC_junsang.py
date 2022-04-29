import serial
import pigpio

pi2=pigpio.pi()
port="/dev/ttyACM0"
serialfromArduino=serial.Serial(port,9600)
stop=string(input('If you want to stop, press "s".: ')
char=screen.getch()
try:
    while True:
        try:
            input_s=serialfromArduino.readline()
            input_s=input_s.decode("utf-8")
            input=input_s.replace("\r\n","")
            CH_1=int(input[0:4])
            CH_2=int(input[5:9])
            CH_3=int(input[10:11])
            print((1500-CH_1),(1500-CH_2),CH_3)
            stroll=abs(1500-CH_1)
            reverse=(3000-CH_2)
            if CH_2>1500:
                if CH_1>1500:
                    pi2.set_servo_pulsewidth(19,CH_2-stroll)
                    pi2.set_servo_pulsewidth(9,reverse)
                elif CH_1<1500:
                    pi2.set_servo_pulsewidth(19,CH_2)
                    pi2.set_servo_pulsewidth(9,reverse-stroll)
                else:
                    pi2.set_servo_pulsewidth(19,CH_2)
                    pi2.set_servo_pulsewidth(9,reverse)
            elif CH_2<1500:
                if CH_1>1500:
                    pi2.set_servo_pulsewidth(19,CH_2+stroll)
                    pi2.set_servo_pulsewidth(9,reverse)
                elif CH_1<1500:
                    pi2.set_servo_pulsewidth(19,CH_2)
                    pi2.set_servo_pulsewidth(9,reverse+stroll)
                else:
                    pi2.set_servo_pulsewidth(19,CH_2)
                    pi2.set_servo_pulsewidth(9,reverse)
            else:
                if CH_1>1500:
                    pi2.set_servo_pulsewidth(19,1500-stroll)
                    pi2.set_servo_pulsewidth(9,3000-(1500+stroll))
                elif CH_1<1500:
                    pi2.set_servo_pulsewidth(19,1500+stroll)
                    pi2.set_servo_pulsewidth(9,3000-(1500-stroll))
                else:
                    pi2.set_servo_pulsewidth(19,CH_2)
                    pi2.set_servo_pulsewidth(9,reverse)
        except (ValueError, IOError) as err:

            print(err)
        if char == str("s"):
            pi2.set_servo_pulsesidth(19,1500)
            pi2.set_servo_pulsewidth(9,1500)
            pi2.close()

finally:
    pi2.close()