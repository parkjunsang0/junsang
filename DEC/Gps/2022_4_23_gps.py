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
        geo = gps.geo_coords()
        """
        옥상 좌표
        point_zero_x = 128.9664835
        point_zero_y = 35.1160249
        point_x_x = 128.9665769
        point_x_y = 35.11596035
        point_y_x = 128.9665563
        point_y_y = 35.11609505
        x_x = 14
        x_y = 0
        y_x = 0
        y_y = 14
        """
        #연못 좌표
        point_zero_x = 128.96665993991235
        point_zero_y = 35.11505532252948
        point_x_x = 128.96675579646794
        point_x_y = 35.11488316247233
        point_y_x = 128.96684063137369
        point_y_y = 35.11513365186809
        xpoint_x = 20
        ypoint_x = 0
        xpoint_y = 0
        ypoint_y = 20

        a = ((point_y_y - point_zero_y) * xpoint_x - (point_x_y - point_zero_y) * ypoint_x) / ((point_y_y - point_zero_y) * (point_x_x - point_zero_x) - (point_x_y - point_zero_y) * (point_y_x - point_zero_x))
        b = ((point_y_x - point_zero_x) * xpoint_x - (point_x_x - point_zero_x) * ypoint_x) / ((point_y_x - point_zero_x) * (point_x_y - point_zero_y) - (point_x_x - point_zero_x) * (point_y_y - point_zero_y))
        c = ((point_y_y - point_zero_y) * xpoint_y - (point_x_y - point_zero_y) * ypoint_y) / ((point_y_y - point_zero_y) * (point_x_x - point_zero_x) - (point_x_y - point_zero_y) * (point_y_x - point_zero_x))
        d = ((point_y_x - point_zero_x) * xpoint_y - (point_x_x - point_zero_x) * ypoint_y) / ((point_y_x - point_zero_x) * (point_x_y - point_zero_y) - (point_x_x - point_zero_x) * (point_y_y - point_zero_y))

        x = (a * (geo.lon - point_zero_x)) + (b * (geo.lat - point_zero_y))
        y = (c * (geo.lon - point_zero_x)) + (d * (geo.lat - point_zero_y))

        list_x = []
        list_y = []
        list_x.append(x)
        list_x.append(x)
        list_y.append(y)
        list_y.append(y)
        while True:
            try:
                geo = gps.geo_coords()
                """
                옥상 좌표
                point_zero_x = 128.9664835
                point_zero_y = 35.1160249
                point_x_x = 128.9665769
                point_x_y = 35.11596035
                point_y_x = 128.9665563
                point_y_y = 35.11609505
                x_x = 14
                x_y = 0
                y_x = 0
                y_y = 14
                """
                #연못 좌표
                point_zero_x = 128.96665993991235
                point_zero_y = 35.11505532252948
                point_x_x = 128.96675579646794
                point_x_y = 35.11488316247233
                point_y_x = 128.96684063137369
                point_y_y = 35.11513365186809
                xpoint_x = 20
                xpoint_y = 0
                ypoint_x = 0
                ypoint_y = 20

                a = ((point_y_y - point_zero_y) * xpoint_x - (point_x_y - point_zero_y) * ypoint_x) / ((point_y_y - point_zero_y) * (point_x_x - point_zero_x) - (point_x_y - point_zero_y) * (point_y_x - point_zero_x))
                b = ((point_y_x - point_zero_x) * xpoint_x - (point_x_x - point_zero_x) * ypoint_x) / ((point_y_x - point_zero_x) * (point_x_y - point_zero_y) - (point_x_x - point_zero_x) * (point_y_y - point_zero_y))
                c = ((point_y_y - point_zero_y) * xpoint_y - (point_x_y - point_zero_y) * ypoint_y) / ((point_y_y - point_zero_y) * (point_x_x - point_zero_x) - (point_x_y - point_zero_y) * (point_y_x - point_zero_x))
                d = ((point_y_x - point_zero_x) * xpoint_y - (point_x_x - point_zero_x) * ypoint_y) / ((point_y_x - point_zero_x) * (point_x_y - point_zero_y) - (point_x_x - point_zero_x) * (point_y_y - point_zero_y))

                x = (a * (geo.lon - point_zero_x)) + (b * (geo.lat - point_zero_y))
                y = (c * (geo.lon - point_zero_x)) + (d * (geo.lat - point_zero_y))

                list_x.append(x)
                list_y.append(y)
                list_x.pop(0)
                list_y.pop(0)

                f = open('/home/pi/GpsFile/gps.dat', 'w')
                x = (a * (geo.lon - point_zero_x)) + (b * (geo.lat - point_zero_y))
                y = (c * (geo.lon - point_zero_x)) + (d * (geo.lat - point_zero_y))
                f.write(str(x) + " " + str(y))
                print(str(x) + str(y))

                list_x_0 = float(list_x[0])
                list_x_1 = float(list_x[1])

                if list_x_1 == list_x_0:
                    print("GPS_err")

                f.close()

                FileName='/home/pi/GpsFile/gps.dat'
                PostFileToServer(FileName)
            except KeyboardInterrupt:
                break
            except:
                continue
    finally:
        port.close()
if __name__ == '__main__':
    run()
