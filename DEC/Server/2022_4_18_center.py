import math
import requests

def PostFileToServer(FileName):
    URL = 'http://192.168.0.12:9054/ThrusterTransferTest'
    UNAME = 'Thruster'
    NewFile_req = open(FileName, 'rb')
    NewFile = {'NewFile' : NewFile_req}
    reqdata = {'uname' : UNAME, 'fileName' : FileName}
    try:
        res=requests.post(URL, files=NewFile, data=reqdata, timeout=1)
    except requests.exceptions.Timeout:
        PostFileToServer(FileName)

FileOpen=open('/home/openesb/EsbServer/DataFiles/Gps/gps.dat','r')
data=FileOpen.readline().strip("\n").split(" ")
data_x = data[0]
data_y = data[1]
X = float(data_x)
Y = float(data_y)

list_x = []
list_y = []
list_x.append(X)
list_x.append(X)
list_y.append(Y)
list_y.append(Y)
target_x = 7
target_y = 10

while True:
    try:
        FileOpen = open('/home/openesb/EsbServer/DataFiles/Gps/gps.dat', 'r')
        data = FileOpen.readline().strip("\n").split(" ")
        print(data)
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

        GPS_distance = math.sqrt((list_x_1 - target_x) ** 2 + (list_y_1 - target_y) ** 2)

        with open('/home/openesb/EsbServer/DataFiles/Gps/gps_backup.dat', 'w') as FileOpen:
            FileOpen.write(str(list_x_1)+" "+str(list_y_1))

        if list_y_1 > target_y:
            left_str = str(1650)
            right_str = str(1350)
            GPS_distance_str = str(GPS_distance)
            with open('/home/openesb/ThrusterFile/Thruster.dat', 'w') as FileOpen:
                FileOpen.write(left_str + " " + right_str + " " + GPS_distance_str)

        elif list_y_1 < target_y:
            left_str = str(1500)
            right_str = str(1500)
            GPS_distance_str = str(GPS_distance)
            with open('/home/openesb/ThrusterFile/Thruster.dat', 'w') as FileOpen:
                FileOpen.write(left_str + " " + right_str + " " + GPS_distance_str)

        if list_x_1 == list_x_0:
            print("GPS_err")

        FileName = '/home/openesb/ThrusterFile/Thruster.dat'
        PostFileToServer(FileName)
    except KeyboardInterrupt:
        break
    except IndexError:
        FileOpen = open('/home/openesb/EsbServer/DataFiles/Gps/gps_backup.dat', 'r')
        data = FileOpen.readline().strip("\n").split(" ")
        print(data)
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

        GPS_distance = math.sqrt((list_x_1 - target_x) ** 2 + (list_y_1 - target_y) ** 2)

        if list_y_1 > target_y:
            left_str = str(1650)
            right_str = str(1350)
            GPS_distance_str = str(GPS_distance)
            with open('/home/openesb/ThrusterFile/Thruster.dat', 'w') as FileOpen:
                FileOpen.write(left_str + " " + right_str + " " + GPS_distance_str)
        elif list_y_1 < target_y:
            left_str = str(1500)
            right_str = str(1500)
            GPS_distance_str = str(GPS_distance)
            with open('/home/openesb/ThrusterFile/Thruster.dat', 'w') as FileOpen:
                FileOpen.write(left_str + " " + right_str + " " + GPS_distance_str)
        FileName = '/home/openesb/ThrusterFile/Thruster.dat'
        PostFileToServer(FileName)


