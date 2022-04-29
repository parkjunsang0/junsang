from ublox_gps import UbloxGps
import serial

port = serial.Serial('/dev/ttyACM0', baudrate=38400, timeout=1)
gps = UbloxGps(port)
"""
x0 = float(input("x0:"))
y0 = float(input("y0:"))
x1 = float(input("x1:"))
y1 = float(input("y1:"))
x2 = float(input("x2:"))
y2 = float(input("y2:"))
X1 = float(input("X1:"))
Y1 = float(input("Y1:"))
X2 = float(input("X2:"))
Y2 = float(input("Y2:"))
"""
x0 = 128.9670318
y0 = 35.11462338
x1 = 128.9670894
y1 = 35.11454583
x2 = 128.9673548
y2 = 35.11475767
X1 = 10
Y1 = 0
X2 = 0
Y2 = 33.7

def GPS(x0,x1,x2,y0,y1,y2,X1,X2,Y1,Y2):
    try:
        while True:
            try:
                geo = gps.geo_coords()

                A = ((y2 - y0) * X1 - (y1 - y0) * X2) / ((y2 - y0) * (x1 - x0) - (y1 - y0) * (x2 - x0))
                B = ((x2 - x0) * X1 - (x1 - x0) * X2) / ((x2 - x0) * (y1 - y0) - (x1 - x0) * (y2 - y0))
                C = ((y2 - y0) * Y1 - (y1 - y0) * Y2) / ((y2 - y0) * (x1 - x0) - (y1 - y0) * (x2 - x0))
                D = ((x2 - x0) * Y1 - (x1 - x0) * Y2) / ((x2 - x0) * (y1 - y0) - (x1 - x0) * (y2 - y0))

                X = (A * (geo.lon - x0)) + (B * (geo.lat - y0))
                Y = (C * (geo.lon - x0)) + (D * (geo.lat - y0))
                return X,Y
            except (ValueError, IOError) as err:
                print(err)
    finally:
        port.close()
gps_value = GPS(x0, x1, x2, y0, y1, y2, X1, X2, Y1, Y2)
print(gps_value)