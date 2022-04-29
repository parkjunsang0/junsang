"""
i=float(input("input score:"))
def Calc_glad(score):
    if i>=90:
            print(i," A입니다")
    elif i>=80 and i<90:
            print(i," B입니다")
    elif i>=70 and i<80:
            print(i," C입니다")
    else:print(i," F입니다")
Calc_glad(i)
"""

"""
def Clac_Meter(Hour):
    Meter=Hour*4
    print(Meter,"KM")

Clac_Meter(float(input("input time")))
"""


FileOpen=open('Number.dat', 'r')
data=FileOpen.read().split(" ")
print(data)
for i in range(len(data)):
    data[i]=int(data[i])
    if data[i]%2==0:
        print(data[i],"는 짝수입니다")
    else:print(data[i],"는 홀수입니다")
def Clac_divisor_max(number):
    print(max(data))
#print(data)
print("원소 중 가장 큰 값은",max(data),"입니다")