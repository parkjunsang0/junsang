import serial

from ublox_gps import UbloxGps

port = serial.Serial('/dev/ttyACM0', baudrate=38400, timeout=1)
gps = UbloxGps(port)


def run():
    try:
        while True:
            try:

                print("Listening for UBX Messages")
                geo=gps.geo_coords()
                print("Longitude: ", geo.lon)
                print("Latitude: ", geo.lat)
                LON=str(geo.lon)
                LAT=str(geo.lat)
                with open('./GPS_LON_Y.txt', 'a') as FileOpen:
                    FileOpen.write(LON+"\n")
                with open('./GPS_LAT_Y.txt', 'a') as FileOpen:
                    FileOpen.write(LAT+"\n")
            except (ValueError, IOError) as err:
                print(err)

    finally:
        port.close()

if __name__ == '__main__':
    run()

