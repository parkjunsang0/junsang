def Fileread():
    FileOpen = open('/practice/data.dat', 'r')
    data = FileOpen.readline().strip("\n").split(" ")
    data_x = data[0]
    data_y = data[1]
    X = float(data_x)
    Y = float(data_y)

    list_x = []
    list_y = []
    list_x.append(X)
    list_x.append(X)
    list_x.append(X)
    list_y.append(Y)
    list_y.append(Y)
    list_y.append(Y)
    while True:
        try:
            FileOpen = open('/practice/data.dat', 'r')
            data = FileOpen.readline().strip("\n").split(" ")
            data_x = data[0]
            data_y = data[1]
            X = float(data_x)
            Y = float(data_y)
            list_x.append(X)
            list_y.append(Y)
            list_x.pop(0)
            list_y.pop(0)

            list_x_0 = float(list_x[0])
            list_x_1 = float(list_x[1])
            list_y_0 = float(list_y[0])
            list_y_1 = float(list_y[1])

            backup_x = str(list_x[1])
            backup_y = str(list_y[1])

            with open('/Users/parkjunsang/PycharmProjects/pythonProject/practice/DATA.dat', 'w') as FileOpen:
                FileOpen.write(backup_x + " " + backup_y)
            return list_x_0,list_x_1,list_y_0,list_y_1
        except:
            FileOpen = open('/Users/parkjunsang/PycharmProjects/pythonProject/practice/DATA.dat', 'r')
            data = FileOpen.readline().strip("\n").split(" ")
            list_x_1 = data[0]
            list_y_1 = data[1]
            return list_x_1,list_y_1
value_xy = Fileread()
print(value_xy)