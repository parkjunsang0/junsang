#1500 < stroll <= 1900
#stroll = 1900

for speed in range(1095,1905,5):
    if 1900>=speed>=1500:
        thruster_left = (1900-speed) / 400 * (stroll - 1500) + speed
        thruster_right = speed - (stroll - 1500)
        print(thruster_left,thruster_right)
    elif 1500>speed>=1100:
        thruster_left = (speed-1100) / 400 * (stroll - 1500) + speed
        thruster_right = (stroll - 1700) * 2 / 400 * (1300 - speed) + 1300
        print(thruster_left,thruster_right)


#1100 <= stroll < 1500
#stroll = 1100

for speed in range(1095,1905,5):
    if 1900>=speed>=1500:
        thruster_left = speed - (1500 - stroll)
        thruster_right = (1900-speed) / 400 * (1500 - stroll) + speed
        print(thruster_left,thruster_right)
    elif 1500>speed>=1100:
        thruster_left = (1300 - stroll) * 2 / 400 * (1300 - speed) + 1300
        thruster_right = (speed-1100) / 400 * (1500 - stroll) + speed
        print(thruster_left,thruster_right)

