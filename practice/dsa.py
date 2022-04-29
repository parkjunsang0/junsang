"""thruster=[]
GPS_distance=10.8021311
thruster_list = "16301600"+str(GPS_distance)
thruster.append(thruster_list)
thruster_value = thruster[0]
GPS_left = int(thruster_value[0:4])
GPS_right = int(thruster_value[4:8])
GPS_distance = float(thruster_value[8:])
print(GPS_left)
print(GPS_right)
print(GPS_distance)
"""
'''import time

X = 10.3251
Y = -6.12345
X_str = str(X)
Y_str = str(Y)
with open('./01.dat','a') as FileOpen:
    FileOpen.write(X_str r+ Y_str + "\n")
FileOpen=open('./01.dat')
data = FileOpen.readlines()
data_x = data[-1:]
data_y = data[-2:]
data_z = data[-3:]
data_x_1 = float(data_x[0])
data_y_1 = float(data_y[0])
data_z_1 = float(data_z[0])

print(data)
print(data_x_1)
print(data_y_1)
print(data_z_1)
#print(float(data_x))
#print(float(data_y))
#'''
"""
list=[]
try:
    while True:
        try:
            list.append("1")
            print(list)
            if 2>1:
                while True:
                    try:
                        list.append("2")
                        time.sleep(1)
                        print(list[0])
                    except KeyboardInterrupt:
                        print(list[0])
                        break
                    except:
                        continue
        except KeyboardInterrupt:
            print(list[0])
            break
        except:
            continue
except:
    print(err)""""""
b = '1500 ' + '1600 ' + '1' + '\n'
b1 = b.encode('utf-8')
b2 = b1.decode('utf-8').strip("\n").split(" ")
print(b1)
print(type(b1))
print(b2)
print(type(b2))"""
"""
import csv
import glob
import os

input = '/Users/parkjunsang/PycharmProjects/pythonProject/practice/gps_data/'
filename = 'gps_data'
file_ext = '.dat'

while True:
    output = '/Users/parkjunsang/PycharmProjects/pythonProject/practice/gps_data/%s%s' % (filename, file_ext)
    uniq = 1
    while os.path.exists(output):
        output = '/Users/parkjunsang/PycharmProjects/pythonProject/practice/gps_data/%s(%d)%s' % (filename, uniq, file_ext)
        uniq += 1

    file_list = glob.glob(input + '*.dat')

    with open(output, 'w') as f:
        for i, file in enumerate(file_list):  # 첫 번째 파일은 그대로 불러오기
            if i == 0:  # 첫 번째 파일은 그대로 불러오기
                with open(file, 'r') as f2:
                    while True:
                        line = f2.readline()
                        if not line:
                            break
                        f.write(line)
                print(file.split('\\')[-1])

            else:
                with open(file, 'r') as f2:
                    n = 0
                    while True:
                        line = f2.readline()
                        if n != 0:  # 2번째 파일부터는 (헤더)제외
                            f.write(line)
                        if not line:
                            break
                        n += 1
                print(file.split('\\')[-1])


    file_num = len(next(os.walk('/Users/parkjunsang/PycharmProjects/pythonProject/practice/gps_data/'))[2])
    print(file_num, ' file merge complete...')
    """
a=int(input("숫자 입력"))
b=int(input("숫자 입력"))
list=[]
if a>b:
    for i in range(b+1,a,1):
        list.append(i)
        print(list)
elif a<b:
    for i in range(a+1,b,1):
        list.append(i)
        print(list)