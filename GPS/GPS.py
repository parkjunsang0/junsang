from ublox_gps import UbloxGps
import serial
import math as math

port = serial.Serial('/dev/ttyACM0', baudrate=38400, timeout=1)
gps = UbloxGps(port)

def run():
    try:
        geo = gps.geo_coords()

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
        target_x = -4
        target_y = 20

        A = ((y2 - y0) * X1 - (y1 - y0) * X2) / ((y2 - y0) * (x1 - x0) - (y1 - y0) * (x2 - x0))
        B = ((x2 - x0) * X1 - (x1 - x0) * X2) / ((x2 - x0) * (y1 - y0) - (x1 - x0) * (y2 - y0))
        C = ((y2 - y0) * Y1 - (y1 - y0) * Y2) / ((y2 - y0) * (x1 - x0) - (y1 - y0) * (x2 - x0))
        D = ((x2 - x0) * Y1 - (x1 - x0) * Y2) / ((x2 - x0) * (y1 - y0) - (x1 - x0) * (y2 - y0))

        X = (A * (geo.lon - x0)) + (B * (geo.lat - y0))
        Y = (C * (geo.lon - x0)) + (D * (geo.lat - y0))

        list_x = []
        list_y = []
        list_x.append(X)
        list_x.append(X)
        list_y.append(Y)
        list_y.append(Y)
        time = 0
        while True:
            try:
                print("Listening for UBX Messages")
                geo = gps.geo_coords()
                A = ((y2 - y0) * X1 - (y1 - y0) * X2) / ((y2 - y0) * (x1 - x0) - (y1 - y0) * (x2 - x0))
                B = ((x2 - x0) * X1 - (x1 - x0) * X2) / ((x2 - x0) * (y1 - y0) - (x1 - x0) * (y2 - y0))
                C = ((y2 - y0) * Y1 - (y1 - y0) * Y2) / ((y2 - y0) * (x1 - x0) - (y1 - y0) * (x2 - x0))
                D = ((x2 - x0) * Y1 - (x1 - x0) * Y2) / ((x2 - x0) * (y1 - y0) - (x1 - x0) * (y2 - y0))
                X = (A * (geo.lon - x0)) + (B * (geo.lat - y0))
                Y = (C * (geo.lon - x0)) + (D * (geo.lat - y0))

                X_str = str(X)
                Y_str = str(Y)

                list_x.append(X)
                list_y.append(Y)
                list_x.pop(0)
                list_y.pop(0)

                list_x_0 = float(list_x[0])
                list_x_1 = float(list_x[1])
                list_y_0 = float(list_y[0])
                list_y_1 = float(list_y[1])

                speed = math.sqrt((list_x_1 - list_x_0) ** 2 + (list_y_1 - list_y_0) ** 2)
                distance = math.sqrt((list_x_1 - target_x) ** 2 + (list_y_1 - target_y) ** 2)

                tar_x = target_x - list_x_1
                tar_y = target_y - list_y_1

                head_x = -(list_x_0 - list_x_1)
                head_y = -(list_y_0 - list_y_1)

                HEAD = math.atan2(head_y, head_x) * 180 / math.pi
                TARGET = math.atan2(tar_y, tar_x) * 180 / math.pi

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
                    head_degree = 360 - head_angle
                elif head_angle < 180:
                    head_degree = -head_angle
                else:
                    head_degree = 180

                time = time + 1

                head_degree_str = str(head_degree)
                distance_str = str(distance)
                speed_str = str(speed)
                time_str = str(time)


                print(X, Y)
                print(head_degree)
                print(distance)
                print(speed)
                print(time)

                with open('GPS_head_degree.txt', 'a') as FileOpen:
                    FileOpen.write(head_degree_str + "\n")
                with open('GPS_distance.txt', 'a') as FileOpen:
                    FileOpen.write(distance_str + "\n")
                with open('GPS_speed.txt', 'a') as FileOpen:
                    FileOpen.write(speed_str + "\n")
                with open('GPS_spot_x.txt','a') as FileOpen:
                    FileOpen.write(X_str + "\n")
                with open('GPS_spot_y.txt','a') as FileOpen:
                    FileOpen.write(Y_str + "\n")
                with open('GPS_time.txt', 'a') as FileOpen:
                   FileOpen.write(time_str + "\n")
            except (ValueError, IOError) as err:
                print(err)
    finally:
        port.close()
if __name__ == '__main__':
    run()
