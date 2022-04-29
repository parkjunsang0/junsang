#!/usr/bin/env python3

from ublox_gps import UbloxGps
import serial
import requests

port = serial.Serial('/dev/ttyACM0', baudrate=38400, timeout=1)
gps = UbloxGps(port)

def PostFileToServer(FileName):
    URL = 'http://192.168.0.8:9053/GpsTransferTest'
    UNAME = 'Gps'
    NewFile_req = open(FileName, 'rb')
    NewFile = {'NewFile' : NewFile_req}
    reqdata = {'uname' : UNAME, 'fileName' : FileName}
    try:
        res=requests.post(URL, files=NewFile, data=reqdata, timeout=1)
    except requests.exceptions.Timeout:
        PostFileToServer(FileName)

def run():
    global numbering
    try:
        print('Listening for GPS')
        while True:
            """
            point_zero_x = 128.9664835
            point_zero_y = 35.1160249
            point_x_x = 128.9665769
            point_x_y = 35.11596035
            point_y_x = 128.9665563
            point_y_y = 35.11609505
            X_x = 14
            X_y = 0
            Y_x = 0
            Y_y = 14
            """
            point_zero_x = 128.96665993991235
            point_zero_y = 35.11505532252948
            point_x_x = 128.96675579646794
            point_x_y = 35.11488316247233
            point_y_x = 128.96684063137369
            point_y_y = 35.11513365186809
            X_x = 20
            X_y = 0
            Y_x = 0
            Y_y = 20

            geo = gps.geo_coords()

            A = ((point_y_y - point_zero_y) * X_x - (point_x_y - point_zero_y) * Y_x) / ((point_y_y - point_zero_y) * (point_x_x - point_zero_x) - (point_x_y - point_zero_y) * (point_y_x - point_zero_x))
            B = ((point_y_x - point_zero_x) * X_x - (point_x_x - point_zero_x) * Y_x) / ((point_y_x - point_zero_x) * (point_x_y - point_zero_y) - (point_x_x - point_zero_x) * (point_y_y - point_zero_y))
            C = ((point_y_y - point_zero_y) * X_y - (point_x_y - point_zero_y) * Y_y) / ((point_y_y - point_zero_y) * (point_x_x - point_zero_x) - (point_x_y - point_zero_y) * (point_y_x - point_zero_x))
            D = ((point_y_x - point_zero_x) * X_y - (point_x_x - point_zero_x) * Y_y) / ((point_y_x - point_zero_x) * (point_x_y - point_zero_y) - (point_x_x - point_zero_x) * (point_y_y - point_zero_y))
            f=open('/home/pi/GpsFile/gps.dat','w')
            X = (A * (geo.lon - point_zero_x)) + (B * (geo.lat - point_zero_y))
            Y = (C * (geo.lon - point_zero_x)) + (D * (geo.lat - point_zero_y))
            f.write(str(X) + '\n' + str(Y))
            print(X,Y)
            f.close()

            FileName='/home/pi/GpsFile/gps.dat'
            PostFileToServer(FileName)
    finally:
        port.close()

if __name__ == '__main__':
    run()


tar_x = target_x - list_x_1
tar_y = target_y - list_y_1

head_x = -(list_x_0 - list_x_1)
head_y = -(list_y_0 - list_y_1)

HEAD = math.atan2(head_y, head_x) * 180 / math.pi
TARGET = math.atan2(tar_y, tar_x) * 180 / math.pi

GPS_speed = math.sqrt((list_x_1 - list_x_0) ** 2 + (list_y_1 - list_y_0) ** 2)
GPS_distance = math.sqrt((list_x_1 - target_x) ** 2 + (list_y_1 - target_y) ** 2)

if head_y > 0:
    if tar_y > 0:
        if HEAD > TARGET:
            head_angle = (TARGET + 360 - HEAD)
        elif HEAD < TARGET:
            head_angle = TARGET - HEAD
        else:
            head_angle = 0
    elif tar_y < 0:
        head_angle = 360 - abs(TARGET) - HEAD
elif head_y < 0:
    if tar_y > 0:
        head_angle = abs(HEAD) + TARGET
    elif tar_y < 0:
        if HEAD > TARGET:
            head_angle = 360 - abs(TARGET) + abs(HEAD)
        elif HEAD < TARGET:
            head_angle = abs(HEAD) - abs(TARGET)
        else:
            head_angle = 0
    else:
        if head_x > 0:
            if tar_x > 0:
                head_angle = abs(HEAD)
            elif tar_x < 0:
                head_angle = abs(HEAD) + 180
            else:
                head_angle = 0
        elif head_x < 0:
            if tar_x > 0:
                head_angle = abs(HEAD) - abs(TARGET)
            elif tar_x < 0:
                head_angle = abs(HEAD) + 180
            else:
                head_angle = 0
        else:
            head_angle = 0
else:
    if head_x > 0:
        if tar_y > 0:
            head_angle = HEAD
        elif tar_y < 0:
            head_angle = 360 - abs(HEAD)
        else:
            if tar_x > 0:
                head_angle = 0
            elif tar_x < 0:
                head_angle = 180
    elif head_x < 0:
        if tar_y > 0:
            head_angle = 180 - abs(HEAD)
        elif tar_y < 0:
            head_angle = 180 - abs(HEAD)
        else:
            if tar_x > 0:
                head_angle = 180
            elif tar_x < 0:
                head_angle = 0
    else:
        head_angle = 0

if head_angle > 180:
    GPS_degree = 360 - head_angle
elif head_angle < 180:
    GPS_degree = -head_angle
else:
    GPS_degree = 180
