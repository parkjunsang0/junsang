speed = 1700
stroll = 1600
def thruster(speed,stroll):
    global thruster_left, thruster_right
    if 1100 <= stroll < 1500:
        if 1900 >= speed >= 1500:
            thruster_left = (1900 - speed) / 400 * (1500 - stroll) + speed
            thruster_right = speed - (1500 - stroll)
        elif 1500 > speed >= 1100:
            thruster_left = (speed - 1100) / 400 * (1500 - stroll) + speed
            thruster_right = (1300 - stroll) * 2 / 400 * (1300 - speed) + 1300
    elif 1500 < stroll <= 1900:
        if 1900 >= speed >= 1500:
            thruster_left = speed - (stroll - 1500)
            thruster_right = (1900 - speed) / 400 * (stroll - 1500) + speed
        elif 1500 > speed >= 1100:
            thruster_left = (stroll - 1700) * 2 / 400 * (1300 - speed) + 1300
            thruster_right = (speed - 1100) / 400 * (stroll - 1500) + speed
    elif stroll == 1500:
        thruster_left = speed
        thruster_right = speed

    return thruster_left,thruster_right
thruster_value_tup = thruster(speed, stroll)
thruster_value_lis = list(thruster_value_tup)
thruster_left = float(thruster_value_lis[0])
thruster_right = float(thruster_value_lis[1])

print(thruster_left,thruster_right)