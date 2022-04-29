import math
import requests

global list_x
global list_y
global list_server_err
global target_x
global target_y
global ERR_server_str
global gps_err


def PostFileToServer(FileName):
    URL = 'http://192.168.0.12:9054/ThrusterTransferTest'
    UNAME = 'Thruster'
    NewFile_req = open(FileName, 'rb')
    NewFile = {'NewFile': NewFile_req}
    reqdata = {'uname': UNAME, 'fileName': FileName}
    try:
        res = requests.post(URL, files=NewFile, data=reqdata, timeout=1)
    except requests.exceptions.Timeout:
        PostFileToServer(FileName)


err = 0
list_x = [0, 0]
list_y = [0, 0]
gps_err = 0
while True:
    try:
        while True:
            try:
                FileOpen = open('/home/openesb/EsbServer/DataFiles/Gps/gps.dat', 'r')
                data = FileOpen.readline().strip("\n").split(" ")
                data_x = data[0]
                data_y = data[1]

                X = float(data_x)
                Y = float(data_y)

                list_x.append(X)
                list_y.append(Y)

                list_x.pop(0)
                list_y.pop(0)

                target_x = 7
                target_y = 10

                list_x_0 = float(list_x[0])
                list_x_1 = float(list_x[1])
                list_y_0 = float(list_y[0])
                list_y_1 = float(list_y[1])

                GPS_distance = math.sqrt((list_x_1 - target_x) ** 2 + (list_y_1 - target_y) ** 2)

                if list_x_1 == list_x_0 and list_y_1 == list_y_0:
                    gps_err = 1
                print(X, Y, gps_err)

                with open('/home/openesb/EsbServer/DataFiles/Gps/gps_backup.dat', 'w') as FileOpen:
                    FileOpen.write(str(list_x_1) + " " + str(list_y_1) + " " + str(gps_err))

            except KeyboardInterrupt:
                break
        while True:
            try:
                err += 1
                if err == 10:
                    err = 0
                ERR_server_str = str(err)
                FileOpen = open('/home/openesb/EsbServer/DataFiles/Gps/gps.dat', 'r')
                data = FileOpen.readline().strip("\n").split(" ")
                data_x = data[0]
                data_y = data[1]

                X = float(data_x)
                Y = float(data_y)

                list_x.append(X)
                list_y.append(Y)

                list_x.pop(0)
                list_y.pop(0)

                list_x_0 = float(list_x[0])
                list_x_1 = float(list_x[1])
                list_y_0 = float(list_y[0])
                list_y_1 = float(list_y[1])

                with open('/home/openesb/EsbServer/DataFiles/Gps/gps_backup.dat', 'w') as FileOpen:
                    FileOpen.write(str(list_x_1) + " " + str(list_y_1) + " " + str(gps_err))

                GPS_distance = math.sqrt((list_x_1 - target_x) ** 2 + (list_y_1 - target_y) ** 2)
                if list_x_1 == list_x_0 and list_y_1 == list_y_0:
                    left_str = str(1500)
                    right_str = str(1500)
                    GPS_distance_str = str(GPS_distance)
                    gps_err = 1

                if list_y_1 >= target_y:
                    left_str = str(1550)
                    right_str = str(1450)
                    GPS_distance_str = str(GPS_distance)
                  #  with open('/home/openesb/ThrusterFile/Thruster.dat', 'w') as FileOpen:
                     #   FileOpen.write(left_str + " " + right_str + " " + GPS_distance_str + " " + str(gps_err) + " " + ERR_server_str)
                     #   print("CheckPoint1")

                elif list_y_1 < target_y:
                    left_str = str(1500)
                    right_str = str(1500)
                    GPS_distance_str = str(GPS_distance)
                  #  with open('/home/openesb/ThrusterFile/Thruster.dat', 'w') as FileOpen:
                    #    FileOpen.write(left_str + " " + right_str + " " + GPS_distance_str + " " + str(gps_err) + " " + ERR_server_str)
                    #    print("CheckPoint2")
                print(X, Y, gps_err, err)
                with open('/home/openesb/ThrusterFile/Thruster.dat', 'w') as FileOpen:
                    FileOpen.write(left_str + " " + right_str + " " + GPS_distance_str + " " + str(gps_err) + " " + ERR_server_str)
                FileName = '/home/openesb/ThrusterFile/Thruster.dat'
                PostFileToServer(FileName)
            except KeyboardInterrupt:
                quit()
            except IndexError:
                print("***************************************")
                FileOpen = open('/home/openesb/EsbServer/DataFiles/Gps/gps_backup.dat', 'r')
                data = FileOpen.readline().strip("\n").split(" ")
                print(str(data) + "\n" + "************************************")

                data_x = data[0]
                data_y = data[1]
                gps_err = data[2]

                X = float(data_x)
                Y = float(data_y)
                GPS_err = float(gps_err)

                list_x.append(X)
                list_y.append(Y)

                list_x.pop(0)
                list_y.pop(0)

                list_x_0 = float(list_x[0])
                list_x_1 = float(list_x[1])
                list_y_0 = float(list_y[0])
                list_y_1 = float(list_y[1])

                GPS_distance = math.sqrt((list_x_1 - target_x) ** 2 + (list_y_1 - target_y) ** 2)
                if list_x_1 == list_x_0 and list_y_1 == list_y_0:
                    gps_err = 1

                elif list_y_1 >= target_y:
                    left_str = str(1550)
                    right_str = str(1450)
                    GPS_distance_str = str(GPS_distance)
                    with open('/home/openesb/ThrusterFile/Thruster.dat', 'w') as FileOpen:
                        FileOpen.write(
                            left_str + " " + right_str + " " + GPS_distance_str + " " + str(gps_err) + " " + ERR_server_str)

                elif list_y_1 < target_y:
                    left_str = str(1500)
                    right_str = str(1500)
                    GPS_distance_str = str(GPS_distance)
                    with open('/home/openesb/ThrusterFile/Thruster.dat', 'w') as FileOpen:
                        FileOpen.write(
                            left_str + " " + right_str + " " + GPS_distance_str + " " + str(gps_err) + " " + ERR_server_str)
                print(X, Y, gps_err, err)
                FileName = '/home/openesb/ThrusterFile/Thruster.dat'
                PostFileToServer(FileName)
    except KeyboardInterrupt:
        quit()
    except IndexError:
        continue
