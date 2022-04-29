import serial
import pigpio
import time

pi2=pigpio.pi()
port="/dev/ttyACM0"
serialfromArduino=serial.Serial(port,9600)
try:
    pi2.set_servo_pulsewidth(19,1550)
    pi2.set_servo_pulsewidth(9,1450)
    time.sleep(2)
    while True:
        try:
            input_s = serialfromArduino.readline()
            input_s = input_s.decode("utf-8")
            input = input_s.replace("\r\n", "")
            CH_1 = int(input[0:4])
            CH_2 = int(input[5:9])
            CH_3 = int(input[9:])
            stroll = CH_1
            speed = CH_2

            FileOpen = open('/home/pi/EsbServer/DataFiles/Thruster/Thruster.dat', 'r')
            data = FileOpen.readlines()
            data_left = data[-3:]
            data_right = data[-2:]
            data_distance = data[-1:]
            GPS_left = float(data_left[0])
            GPS_right = float(data_right[0])
            GPS_distance = float(data_distance[0])

            GPS_left_str=str(GPS_left)
            GPS_right_str = str(GPS_right)
            GPS_distance_str = str(GPS_distance)
            
            pi2.set_servo_pulsewidth(19, GPS_left)
            pi2.set_servo_pulsewidth(9, GPS_right)
            print("left:" + GPS_left_str + "right:" + GPS_right_str + "distance:" + GPS_distance_str)

            if speed != 1500:
                while True:
                    try:
                        input_s = serialfromArduino.readline()
                        input_s = input_s.decode("utf-8")
                        input = input_s.replace("\r\n", "")
                        CH_1 = int(input[0:4])
                        CH_2 = int(input[5:9])
                        CH_3 = int(input[10:])
                        stroll = CH_1
                        speed = CH_2
                        if 1100 <= stroll < 1500:
                            if 1900 >= speed >= 1500:
                                thruster_left = (1900 - speed) / 400 * (1500 - stroll) + speed
                                thruster_right = speed - (1500 - stroll)
                                pi2.set_servo_pulsewidth(19, thruster_left)
                                pi2.set_servo_pulsewidth(9, 3000 - thruster_right)
                                print('left:', thruster_left, 'right:', thruster_right, 'CH:', CH_3,'If you want to stop, press RC "CH_3" butten')
                            elif 1500 > speed >= 1100:
                                thruster_left = (speed - 1100) / 400 * (1500 - stroll) + speed
                                thruster_right = (1300 - stroll) * 2 / 400 * (1300 - speed) + 1300
                                pi2.set_servo_pulsewidth(19, thruster_left)
                                pi2.set_servo_pulsewidth(9, 3000 - thruster_right)
                                print('left:', thruster_left, 'right:', thruster_right, 'CH:', CH_3,'If you want to stop, press RC "CH_3" butten')
                        elif 1500 < stroll <= 1900:
                            if 1900 >= speed >= 1500:
                                thruster_left = speed - (stroll - 1500)
                                thruster_right = (1900 - speed) / 400 * (stroll - 1500) + speed
                                pi2.set_servo_pulsewidth(19, thruster_left)
                                pi2.set_servo_pulsewidth(9, 3000 - thruster_right)
                                print('left:', thruster_left, 'right:', thruster_right, 'CH:', CH_3,'If you want to stop, press RC "CH_3" butten')
                            elif 1500 > speed >= 1100:
                                thruster_left = (stroll - 1700) * 2 / 400 * (1300 - speed) + 1300
                                thruster_right = (speed - 1100) / 400 * (stroll - 1500) + speed
                                pi2.set_servo_pulsewidth(19, thruster_left)
                                pi2.set_servo_pulsewidth(9, 3000 - thruster_right)
                                print('left:', thruster_left, 'right:', thruster_right, 'CH:', CH_3,'If you want to stop, press RC "CH_3" butten')
                        elif stroll == 1500:
                            thruster_left = speed
                            thruster_right = speed
                            pi2.set_servo_pulsewidth(19, thruster_left)
                            pi2.set_servo_pulsewidth(9, 3000 - thruster_right)
                            print('left:', thruster_left, 'right:', thruster_right, 'CH:', CH_3,'If you want to stop, press RC "CH_3" butten')
                        elif CH_3 == 1:
                            pi2.set_servo_pulsewidth(19, 1500)
                            pi2.set_servo_pulsewidth(9, 1500)
                            pi2.stop()
                    except KeyboardInterrupt:
                        pi2.set_servo_pulsewidth(19, 1500)
                        pi2.set_servo_pulsewidth(9, 1500)
                        pi2.stop()
                    except:
                        continue
        except KeyboardInterrupt:
            pi2.set_servo_pulsewidth(19, 1500)
            pi2.set_servo_pulsewidth(9, 1500)
            pi2.stop()
        except:
            continue
except:
    pi2.set_servo_pulsewidth(19,1500)
    pi2.set_servo_pulsewidth(9,1500)
    pi2.stop()
