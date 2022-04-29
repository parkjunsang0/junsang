#!/usr/bin/env python3
#-----------------------------------------------------------------------------
# geo_coords_ex1.py
#
# Simple Example for SparkFun ublox GPS products
#------------------------------------------------------------------------
#
# Written by  SparkFun Electronics, July 2020
#
# Do you like this library? Help support SparkFun. Buy a board!
# https://sparkfun.com
#==================================================================================
# GNU GPL License 3.0
# Copyright (c) 2020 SparkFun Electronics
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
#==================================================================================
# Example 1
# This example sets up the serial port and then passes it to the UbloxGPs
# library. From here we call geo_coords() and to get longitude and latitude. I've
# also included heading of motion here as well.

import serial

from ublox_gps import UbloxGps

port = serial.Serial('/dev/serial0', baudrate=38400, timeout=1)
gps = UbloxGps(port)

def run():

    try:
        print("Listening for UBX Messages")
        while True:

            try:
                x0 = float(input("x0: "))
                y0 = float(input("y0: "))
                x1 = float(input("x1: "))
                y1 = float(input("y1: "))
                x2 = float(input("x2: "))
                y2 = float(input("y2: "))
                X1 = float(input("X1: "))
                Y1 = float(input("Y1: "))
                X2 = float(input("X2: "))
                Y2 = float(input("Y2: "))
                #geo = gps.geo_coords()
                #print("Longitude: ", geo.lon)
                #print("Latitude: ", geo.lat)
                #print("Heading of Motion: ", geo.headMot)

                a=((y2-y0)*X1-(y1-y0)*X2)/((y2-y0)*(x1-x0)-(y1-y0)*(x2-x0))
                b=((x2-x0)*X1-(x1-x0)*X2)/((x2-x0)*(y1-y0)-(x1-x0)*(y2-y0))
                c=((y2-y0)*Y1-(y1-y0)*Y2)/((y2-y0)*(x1-x0)-(y1-y0)*(x2-x0))
                d=((x2-x0)*Y1-(x1-x0)*Y2)/((x2-x0)*(y1-y0)-(x1-x0)*(y2-y0))

                geo_lon=128.9665276
                geo_lat=35.1160166
                X=a*(geo_lon-x0)+b*(geo_lat-y0)
                Y=c*(geo_lon-x0)+d*(geo_lat-y0)
                print(x)
                print(y)
            except (ValueError, IOError) as err:
                print(err)

    finally:
        port.close()


if __name__ == '__main__':
    run()