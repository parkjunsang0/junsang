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
                LON=str(geo.lon)
                LAT=str(geo.lat)
                with open('./GPS_LON.txt', 'w') as FileOpen:
                    FileOpen.write(LON + "\n")
                with open('./GPS_LAT.txt', 'w') as FileOpen:
                    FileOpen.write(LAT + "\n")

                except (ValueError, IOError) as err:
                print(err)

    finally:
    port.close()

if __name__ == '__main__':
    run()