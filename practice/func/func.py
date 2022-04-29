import sys

X = float(input("value:"))
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


def thruster(X, x0, x1, x2, y0, y1, y2, X1, X2, Y1, Y2):
    A = ((y2 - y0) * X1 - (y1 - y0) * X2) / ((y2 - y0) * (x1 - x0) - (y1 - y0) * (x2 - x0))
    B = ((x2 - x0) * X1 - (x1 - x0) * X2) / ((x2 - x0) * (y1 - y0) - (x1 - x0) * (y2 - y0))
    C = ((y2 - y0) * Y1 - (y1 - y0) * Y2) / ((y2 - y0) * (x1 - x0) - (y1 - y0) * (x2 - x0))
    D = ((x2 - x0) * Y1 - (x1 - x0) * Y2) / ((x2 - x0) * (y1 - y0) - (x1 - x0) * (y2 - y0))
    x = (A * (128.101 - x0)) + (B * (35.114 - y0))
    y = (C * (128.941 - x0)) + (D * (35.1423 - y0))
    X_x = X * x

    return X_x, y


result = thruster(X, x0, x1, x2, y0, y1, y2, X1, X2, Y1, Y2)

result_list = list(result)
result_1 = float(result_list[0])
print(result_1)
result_2 = float(result_list[1])
print(result_2)

result_3 = result_2 + result_1
print(result_3)
