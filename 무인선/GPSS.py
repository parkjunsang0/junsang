x0=float(input("x0: "))
y0=float(input("y0: "))
x1=float(input("x1: "))
y1=float(input("y1: "))
x2=float(input("x2: "))
y2=float(input("y2: "))
X1=float(input("X1: "))
Y1=float(input("Y1: "))
X2=float(input("X2: "))
Y2=float(input("Y2: "))
dU1=(x1-x0)
dU2=(x2-x0)
dV1=(y1-y0)
dV2=(y2-y0)

SHARE=(dV2*dU1-dV1*dU2)
SHARE2=(dU2*dV1-dU1*dV2)

A=(dV2*X1-dV1*X2)/(dV2*dU1-dV1*dU2)
B=(dU2*X1-dU1*X2)/(dU2*dV1-dU1*dV2)
C=(dV2*Y1-dV1*Y2)/(dV2*dU1-dV1*dU2)
D=(dU2*Y1-dU1*Y2)/(dU2*dV1-dU1*dV2)

print(SHARE)
print(SHARE2)

print(A)
print(B)
print(C)
print(D)

geo_lon=128.967057
geo_lat=35.1147487

X=A*(geo_lon-x0)+B*(geo_lat-y0)
Y=C*(geo_lon-x0)+D*(geo_lat-y0)

print(X)
print(Y)