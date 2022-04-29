import serial
import pigpio

pi2=pigpio.pi()
port="/dev/ttyACM0"
serialfromArduino=serial.Serial(port,9600)
print('If you want to stop, press RC "CH_3" butten.')
while True:
    try:
        input_s=serialfromArduino.readline()
        input = input_s.decode("utf-8").strip("\n").split(" ")
        CH_1 = float(input[0])
        CH_2 = float(input[1])
        CH_3 = float(input[2])
        stroll=CH_1
        speed=CH_2
        if 1100<=stroll<1500:
            if 1900 >= speed >= 1500:
                thruster_left = (1900 - speed) / 400 * (1500 - stroll) + speed
                thruster_right = speed - (1500 - stroll)
                pi2.set_servo_pulsewidth(19, thruster_left)
                pi2.set_servo_pulsewidth(9, 3000-thruster_right)
                print('left:', thruster_left, 'right:', thruster_right)

            elif 1500 > speed >= 1100:
                thruster_left = (speed - 1100) / 400 * (1500 - stroll) + speed
                thruster_right = (1300 - stroll) * 2 / 400 * (1300 - speed) + 1300
                pi2.set_servo_pulsewidth(19, thruster_left)
                pi2.set_servo_pulsewidth(9, 3000 - thruster_right)
                print('left:', thruster_left, 'right:', thruster_right)
        elif 1500<stroll<=1900:
            if 1900 >= speed >= 1500:
                thruster_left = speed - (stroll - 1500)
                thruster_right = (1900 - speed) / 400 * (stroll - 1500) + speed
                pi2.set_servo_pulsewidth(19, thruster_left)
                pi2.set_servo_pulsewidth(9, 3000 - thruster_right)
                print('left:', thruster_left, 'right:', thruster_right)
            elif 1500 > speed >= 1100:
                thruster_left = (stroll - 1700) * 2 / 400 * (1300 - speed) + 1300
                thruster_right = (speed - 1100) / 400 * (stroll - 1500) + speed
                pi2.set_servo_pulsewidth(19, thruster_left)
                pi2.set_servo_pulsewidth(9, 3000 - thruster_right)
                print('left:', thruster_left, 'right:', thruster_right)
        elif stroll==1500:
            thruster_left = speed
            thruster_right = speed
            pi2.set_servo_pulsewidth(19, thruster_left)
            pi2.set_servo_pulsewidth(9, 3000 - thruster_right)
            print('left:', thruster_left, 'right:', thruster_right)
        elif CH_3 == 1:
            pi2.set_servo_pulsewidth(19, 1500)
            pi2.set_servo_pulsewidth(9, 1500)
            pi2.stop()
    except KeyboardInterrupt:
        pi2.set_servo_pulsewidth(19,1500)
        pi2.set_servo_pulsewidth(9,1500)
        pi2.stop()
    except:
        continue

