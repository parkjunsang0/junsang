import serial

from ublox_gps import UbloxGps

port = serial.Serial('/dev/ttyACM0', baudrate=38400, timeout=1)
gps = UbloxGps(port)


def run():
    try:
        while True:
            try:
                x0 = 128.9664835
                y0 = 35.1160249
                x1 = 128.9665769
                y1 = 35.11596035
                x2 = 128.9665563
                y2 = 35.11609505
                X1 = 14
                Y1 = 0
                X2 = 0
                Y2 = 14
                print("Listening for UBX Messages")
                geo=gps.geo_coords()
                a = ((y2 - y0) * X1 - (y1 - y0) * X2) / ((y2 - y0) * (x1 - x0) - (y1 - y0) * (x2 - x0))
                b = ((x2 - x0) * X1 - (x1 - x0) * X2) / ((x2 - x0) * (y1 - y0) - (x1 - x0) * (y2 - y0))
                c = ((y2 - y0) * Y1 - (y1 - y0) * Y2) / ((y2 - y0) * (x1 - x0) - (y1 - y0) * (x2 - x0))
                d = ((x2 - x0) * Y1 - (x1 - x0) * Y2) / ((x2 - x0) * (y1 - y0) - (x1 - x0) * (y2 - y0))

                X = a * (geo.lon - x0) + b * (geo.lat - y0)
                Y = c * (geo.lon - x0) + d * (geo.lat - y0)

                print("X:"+ str(X) + "Y:" + str(Y))

                #with open('./GPS_LON_Y.txt', 'a') as FileOpen:
                #    FileOpen.write(LON+"\n")
                #with open('./GPS_LAT_Y.txt', 'a') as FileOpen:
                #    FileOpen.write(LAT+"\n")
            except (ValueError, IOError) as err:
                print(err)

    finally:
        port.close()

if __name__ == '__main__':
    run()

