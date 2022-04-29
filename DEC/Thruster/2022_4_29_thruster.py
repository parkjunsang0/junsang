import serial
import pigpio
import time

global ERR_server_str
global list_server_err

pi2 = pigpio.pi()
port = "/dev/ttyACM0"
serialfromArduino = serial.Serial(port, 9600)
pi2.set_servo_pulsewidth(19, 1550)
pi2.set_servo_pulsewidth(9, 3000-1550)
time.sleep(2)

with open('/home/pi/EsbServer/DataFiles/Thruster/Thruster_backup.dat', 'w') as FileOpen:
    FileOpen.write(str(1500) + " " + str(1500) + " " + str(1))

list_server_err = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1]

while True:
    try:
        input_s = serialfromArduino.readline()
        input_ch = input_s.decode("ascii").strip("\r\n").split(" ")
        CH_1 = float(input_ch[0])
        CH_2 = float(input_ch[1])
        CH_3 = float(input_ch[2])
        stroll = CH_1
        speed = CH_2
        if speed == 1500:
            try:
                FileOpen = open('/home/pi/EsbServer/DataFiles/Thruster/Thruster.dat', 'r')
                data = FileOpen.readline().strip("\n").split(" ")
                GPS_left = float(data[0])
                GPS_right = float(data[1])
                GPS_distance = float(data[2])
                ERR_gps = float(data[3])
                ERR_server = float(data[4])

                list_server_err.append(ERR_server)
                list_server_err.pop(0)

                list_err_0 = float(list_server_err[0])
                list_err_1 = float(list_server_err[1])
                list_err_2 = float(list_server_err[2])
                list_err_3 = float(list_server_err[3])
                list_err_4 = float(list_server_err[4])
                list_err_5 = float(list_server_err[5])
                list_err_6 = float(list_server_err[6])
                list_err_7 = float(list_server_err[7])
                list_err_8 = float(list_server_err[8])
                list_err_9 = float(list_server_err[9])

                if list_err_0 == list_err_1 == list_err_2 == list_err_3 == list_err_4 == list_err_5 == list_err_6 == list_err_7 == list_err_8 == list_err_9:
                    pi2.set_servo_pulsewidth(19, 1500)
                    pi2.set_servo_pulsewidth(9, 1500)
                    print("SERVER_STOP")
                elif ERR_gps == 1:
                    pi2.set_servo_pulsewidth(19, 1500)
                    pi2.set_servo_pulsewidth(9, 1500)
                    print("GPS_STOP")

                pi2.set_servo_pulsewidth(19, GPS_left)
                pi2.set_servo_pulsewidth(9, GPS_right)

                GPS_left_str = str(GPS_left)
                GPS_right_str = str(GPS_right)
                GPS_distance_str = str(GPS_distance)
                ERR_server_str = str(ERR_server)
                print("left: " + GPS_left_str + " right: " + GPS_right_str + " distance: " + GPS_distance_str + " err: " + ERR_server_str)

                with open('/home/pi/EsbServer/DataFiles/Thruster/Thruster_backup.dat', 'w') as FileOpen:
                    FileOpen.write(GPS_left_str + " " + GPS_right_str + " " + GPS_distance_str + " " + ERR_server_str)
            except ValueError:
                FileOpen = open('/home/pi/EsbServer/DataFiles/Thruster/Thruster_backup.dat', 'r')
                data = FileOpen.readline().strip("\n").split(" ")
                GPS_left = float(data[0])
                GPS_right = float(data[1])
                GPS_distance = float(data[2])
                ERR_gps = float(data[3])
                ERR_server = float(data[4])

                list_server_err.append(ERR_server)
                list_server_err.pop(0)

                list_err_0 = float(list_server_err[0])
                list_err_1 = float(list_server_err[1])
                list_err_2 = float(list_server_err[2])
                list_err_3 = float(list_server_err[3])
                list_err_4 = float(list_server_err[4])
                list_err_5 = float(list_server_err[5])
                list_err_6 = float(list_server_err[6])
                list_err_7 = float(list_server_err[7])
                list_err_8 = float(list_server_err[8])
                list_err_9 = float(list_server_err[9])

                if list_err_0 == list_err_1 == list_err_2 == list_err_3 == list_err_4 == list_err_5 == list_err_6 == list_err_7 == list_err_8 == list_err_9:
                    print("SERVER_STOP")
                    pi2.set_servo_pulsewidth(19, 1500)
                    pi2.set_servo_pulsewidth(9, 1500)
                elif ERR_gps == 1:
                    pi2.set_servo_pulsewidth(19, 1500)
                    pi2.set_servo_pulsewidth(9, 1500)

                pi2.set_servo_pulsewidth(19, GPS_left)
                pi2.set_servo_pulsewidth(9, GPS_right)

                GPS_left_str = str(GPS_left)
                GPS_right_str = str(GPS_right)
                GPS_distance_str = str(GPS_distance)
                print("left: " + GPS_left_str + " right: " + GPS_right_str + " distance: " + GPS_distance_str + " err: " + ERR_server_str)
            except IndexError:
                FileOpen = open('/home/pi/EsbServer/DataFiles/Thruster/Thruster_backup.dat', 'r')
                data = FileOpen.readline().strip("\n").split(" ")
                GPS_left = float(data[0])
                GPS_right = float(data[1])
                GPS_distance = float(data[2])
                ERR_gps = float(data[3])
                ERR_server = float(data[4])

                list_server_err.append(ERR_server)
                list_server_err.pop(0)

                list_err_0 = float(list_server_err[0])
                list_err_1 = float(list_server_err[1])
                list_err_2 = float(list_server_err[2])
                list_err_3 = float(list_server_err[3])
                list_err_4 = float(list_server_err[4])
                list_err_5 = float(list_server_err[5])
                list_err_6 = float(list_server_err[6])
                list_err_7 = float(list_server_err[7])
                list_err_8 = float(list_server_err[8])
                list_err_9 = float(list_server_err[9])

                if list_err_0 == list_err_1 == list_err_2 == list_err_3 == list_err_4 == list_err_5 == list_err_6 == list_err_7 == list_err_8 == list_err_9:
                    print("SERVER_STOP")
                    pi2.set_servo_pulsewidth(19, 1500)
                    pi2.set_servo_pulsewidth(9, 1500)
                elif ERR_gps == 1:
                    pi2.set_servo_pulsewidth(19, 1500)
                    pi2.set_servo_pulsewidth(9, 1500)

                pi2.set_servo_pulsewidth(19, GPS_left)
                pi2.set_servo_pulsewidth(9, GPS_right)

                GPS_left_str = str(GPS_left)
                GPS_right_str = str(GPS_right)
                GPS_distance_str = str(GPS_distance)
                print("left: " + GPS_left_str + " right: " + GPS_right_str + " distance: " + GPS_distance_str + " err: " + ERR_server_str)
        elif speed != 1500:
            while True:
                try:
                    input_s = serialfromArduino.readline()
                    input_ch = input_s.decode("ascii").strip("\r\n").split(" ")
                    CH_1 = float(input_ch[0])
                    CH_2 = float(input_ch[1])
                    stroll = CH_1
                    speed = CH_2
                    if 1100 <= stroll < 1500:
                        if 1900 >= speed >= 1500:
                            thruster_right = (1900 - speed) / 400 * (1500 - stroll) + speed
                            thruster_left = speed - (1500 - stroll)
                            pi2.set_servo_pulsewidth(19, thruster_left)
                            pi2.set_servo_pulsewidth(9, 3000 - thruster_right)
                            print('left:', thruster_left, 'right:', thruster_right)
                        elif 1500 > speed >= 1100:
                            thruster_right = (speed - 1100) / 400 * (1500 - stroll) + speed
                            thruster_left = (1300 - stroll) * 2 / 400 * (1300 - speed) + 1300
                            pi2.set_servo_pulsewidth(19, thruster_left)
                            pi2.set_servo_pulsewidth(9, 3000 - thruster_right)
                            print('left:', thruster_left, 'right:', thruster_right)
                    elif 1500 < stroll <= 1900:
                        if 1900 >= speed >= 1500:
                            thruster_right = speed - (stroll - 1500)
                            thruster_left = (1900 - speed) / 400 * (stroll - 1500) + speed
                            pi2.set_servo_pulsewidth(19, thruster_left)
                            pi2.set_servo_pulsewidth(9, 3000 - thruster_right)
                            print('left:', thruster_left, 'right:', thruster_right)
                        elif 1500 > speed >= 1100:
                            thruster_right = (stroll - 1700) * 2 / 400 * (1300 - speed) + 1300
                            thruster_left = (speed - 1100) / 400 * (stroll - 1500) + speed
                            pi2.set_servo_pulsewidth(19, thruster_left)
                            pi2.set_servo_pulsewidth(9, 3000 - thruster_right)
                            print('left:', thruster_left, 'right:', thruster_right)
                    elif stroll == 1500:
                        thruster_left = speed
                        thruster_right = speed
                        pi2.set_servo_pulsewidth(19, thruster_left)
                        pi2.set_servo_pulsewidth(9, 3000 - thruster_right)
                        print('left:', thruster_left, 'right:', thruster_right)
                except KeyboardInterrupt:
                    pi2.set_servo_pulsewidth(19, 1500)
                    pi2.set_servo_pulsewidth(9, 1500)
                    pi2.stop()
                    break
    except KeyboardInterrupt:
        pi2.set_servo_pulsewidth(19, 1500)
        pi2.set_servo_pulsewidth(9, 1500)
        pi2.stop()
        break
