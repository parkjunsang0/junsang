import math
import requests


global list_x
global list_y
global list_server_err
global target_x
global target_y
global ERR_server_str


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

list_x.append(0)
list_x.append(0)
list_y.append(0)
list_y.append(0)
list_server_err.append(0)
list_server_err.append(0)
list_server_err.append(0)
list_server_err.append(0)
list_server_err.append(0)
while True:
    try:
        FileOpen = open('/home/openesb/EsbServer/DataFiles/Gps/gps.dat', 'r')
        data = FileOpen.readline().strip("\n").split(" ")
        #print(data)
        data_x = data[0]
        data_y = data[1]
        data_err = data[2]

        X = float(data_x)
        Y = float(data_y)
        ERR_gps = float(data_err)

        list_x = []
        list_y = []
        list_server_err = []

        list_x.append(X)
        list_y.append(Y)
        list_server_err.append(ERR_gps)

        list_x.pop(0)
        list_y.pop(0)
        list_server_err.pop(0)
        print(list_x, list_y, ERR_gps)

        target_x = 7
        target_y = 10

        list_x_1 = float(list_x[1])
        list_y_1 = float(list_y[1])
        list_err_1 = float(list_server_err[1])

        GPS_distance = math.sqrt((list_x_1 - target_x) ** 2 + (list_y_1 - target_y) ** 2)

        with open('/home/openesb/EsbServer/DataFiles/Gps/gps_backup.dat', 'w') as FileOpen:
            FileOpen.write(str(list_x_1) + " " + str(list_y_1) + " " + str(list_err_1))

        start = int(input("press '1':"))
        if start == 1:
            while True:
                try:
                    err += 1
                    if err == 2:
                        err = 0
                    ERR_server_str = str(err)
                    FileOpen = open('/home/openesb/EsbServer/DataFiles/Gps/gps.dat', 'r')
                    data = FileOpen.readline().strip("\n").split(" ")
                    print(data)
                    print(len(data))
                    data_x = data[0]
                    data_y = data[1]
                    data_err = data[2]

                    X = float(data_x)
                    Y = float(data_y)
                    ERR_gps = float(data_err)

                    list_x.append(X)
                    list_y.append(Y)
                    list_server_err.append(ERR_gps)

                    list_x.pop(0)
                    list_y.pop(0)
                    list_server_err.pop(0)

                    list_x_0 = float(list_x[0])
                    list_x_1 = float(list_x[1])
                    list_y_0 = float(list_y[0])
                    list_y_1 = float(list_y[1])
                    list_err_0 = float(list_server_err[0])
                    list_err_1 = float(list_server_err[1])
                    list_err_2 = float(list_server_err[2])
                    list_err_3 = float(list_server_err[3])
                    list_err_4 = float(list_server_err[4])

                    with open('/home/openesb/EsbServer/DataFiles/Gps/gps_backup.dat', 'w') as FileOpen:
                        FileOpen.write(str(list_x_1) + " " + str(list_y_1) + str(list_err_1))

                    GPS_distance = math.sqrt((list_x_1 - target_x) ** 2 + (list_y_1 - target_y) ** 2)

                    if list_err_0 == list_err_1 == list_err_2 == list_err_3 == list_err_4:
                        print("GPS_ERR")
                        left_str = str(1500)
                        right_str = str(1500)
                        GPS_distance_str = str(GPS_distance)
                        with open('/home/openesb/ThrusterFile/Thruster.dat', 'w') as FileOpen:
                            FileOpen.write(left_str + " " + right_str + " " + GPS_distance_str + " " + ERR_server_str)
                        break

                    elif list_y_1 >= target_y:
                        left_str = str(1550)
                        right_str = str(1450)
                        GPS_distance_str = str(GPS_distance)
                        with open('/home/openesb/ThrusterFile/Thruster.dat', 'w') as FileOpen:
                            FileOpen.write(left_str + " " + right_str + " " + GPS_distance_str + " " + ERR_server_str)

                    elif list_y_1 < target_y:
                        left_str = str(1500)
                        right_str = str(1500)
                        GPS_distance_str = str(GPS_distance)
                        with open('/home/openesb/ThrusterFile/Thruster.dat', 'w') as FileOpen:
                            FileOpen.write(left_str + " " + right_str + " " + GPS_distance_str + " " + ERR_server_str)

                    FileName = '/home/openesb/ThrusterFile/Thruster.dat'
                    PostFileToServer(FileName)
                except KeyboardInterrupt:
                    break
                except IndexError:
                    print("***************************************")
                    FileOpen = open('/home/openesb/EsbServer/DataFiles/Gps/gps_backup.dat', 'r')
                    data = FileOpen.readline().strip("\n").split(" ")
                    print(str(data)+"\n"+"************************************")

                    data_x = data[0]
                    data_y = data[1]
                    data_err = data[2]

                    X = float(data_x)
                    Y = float(data_y)
                    ERR_gps = float(data_err)

                    list_x.append(X)
                    list_y.append(Y)
                    list_server_err.append(ERR_gps)

                    list_x.pop(0)
                    list_y.pop(0)
                    list_server_err.pop(0)

                    list_x_0 = float(list_x[0])
                    list_x_1 = float(list_x[1])
                    list_y_0 = float(list_y[0])
                    list_y_1 = float(list_y[1])
                    list_err_0 = float(list_server_err[0])
                    list_err_1 = float(list_server_err[1])
                    list_err_2 = float(list_server_err[2])
                    list_err_3 = float(list_server_err[3])
                    list_err_4 = float(list_server_err[4])

                    GPS_distance = math.sqrt((list_x_1 - target_x) ** 2 + (list_y_1 - target_y) ** 2)

                    if list_err_0 == list_err_1 == list_err_2 == list_err_3 == list_err_4:
                        print("GPS_ERR")
                        left_str = str(1500)
                        right_str = str(1500)
                        GPS_distance_str = str(GPS_distance)
                        with open('/home/openesb/ThrusterFile/Thruster.dat', 'w') as FileOpen:
                            FileOpen.write(left_str + " " + right_str + " " + GPS_distance_str + " " + ERR_server_str)
                        break

                    elif list_y_1 > target_y:
                        left_str = str(1550)
                        right_str = str(1450)
                        GPS_distance_str = str(GPS_distance)
                        with open('/home/openesb/ThrusterFile/Thruster.dat', 'w') as FileOpen:
                            FileOpen.write(left_str + " " + right_str + " " + GPS_distance_str + " " + ERR_server_str)
                    elif list_y_1 < target_y:
                        left_str = str(1500)
                        right_str = str(1500)
                        GPS_distance_str = str(GPS_distance)
                        with open('/home/openesb/ThrusterFile/Thruster.dat', 'w') as FileOpen:
                            FileOpen.write(left_str + " " + right_str + " " + GPS_distance_str + " " + ERR_server_str)
                    FileName = '/home/openesb/ThrusterFile/Thruster.dat'
                    PostFileToServer(FileName)
    except KeyboardInterrupt:
        break
    except:
        continue
