"""
from random import *
i=(randint(4,28))
print("오프라인 수업 날짜는" , str(i) +"일입니다")
"""

"""
import math
length=float(input("r:"))
square=length**2*math.pi
print(square)
"""

"""
sum=0
for i in range(101):
    if i%2==1:
        sum=sum+i
print(sum)
"""

"""
Box=[]
for i in range(101):
    if i%2==0:
        Box.append(i)
print(Box)
"""

"""
Number=float(input("x:"))
if Number%2==0 and Number>0 or Number<0:
    print(Number,"는 짝수입니다.")
elif Number%2==1:
    print(Number,"는 홀수입니다.")
else:print(Number,"는 실수입니다")
if Number>0:
    print(Number,"는 양수입니다.")
elif Number<0:
    print(Number,"는 음수입니다")
"""

"""
for i in  range(100):
    i=i+1
    print(i)
    if i==20:
        break
"""

"""
Remainder=0
while Remainder<=100000:
    Number=float(input("x:"))
    Remainder=Number%3
    print(Remainder)
    if Remainder<1:
        break
"""

"""
List2=[]
List1=[1,2,3,4,5]
for i in List1:
    Number=i**2
    List2.append(Number)
FileOpen=open('/Users/parkjunsang/PycharmProjects/pythonProject/혼자 연습/List2.dat','w')
FileOpen.write((str(List2)))
FileOpen.close()
print(List2)
"""

"""
Number=0
def Calc_score(Number):
    Number=float(input('input score:'))
    if Number>=90:
        print(str(Number)+'점 A입니다.')
    elif Number>=80 and Number<90:
        print(str(Number)+'점 B입니다.')
    elif Number>=70 and Number<80:
        print(str(Number)+'점 C입니다.')
    else:print(str(Number)+'점 F입니다.')
Calc_score(Number)
"""

"""
Number=0
def Calc_KM():
    Number=float(input('input hour:'))
    KM=Number*4
    print(KM,'km')
Calc_KM()
"""

"""
Numbers=[]
FileOpen=open('./Number.dat','r')
Numbers=FileOpen.read().split(" ")
#print(Numbers)
def Calc_MAX(Numbers):
    for i in range(len(Numbers)):
        Numbers[i]=int(Numbers[i])
        if Numbers[i]%2==0 and Numbers[i]!=0:
            print(Numbers[i],'짝수입니다.')
        elif Numbers[i]%2==1:
            print(Numbers[i],'홀수입니다.')
        else:print(Numbers[i],'실수입니다.')
print('가장 큰 원소는', max(Numbers),'입니다')
Calc_MAX(Numbers)
"""

