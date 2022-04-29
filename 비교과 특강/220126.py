
List1=[1,2,3,4,5]
List1.insert(3,9)
print(List1)

List1=[3,4,5,2]
for i in range(2,10):
     List1.insert(i,9)
print(List1)


"""
x=float(input("input x"))
y=float(input("input y"))
if x>y or x==y and x**2>100 not x==0:
    print("good")
"""

#FileOpen=open('./01.dat','r')
#data=FileOpen.read()
#print(data)
#print(type(data))

"""
FileOpen=open('./01.dat','r')
data=FileOpen.readline().strip("\n").split(" ")
print(data)
data=FileOpen.readline().split(" ")
print(data)
"""
"""
FileOpen=open('./01.dat','r')
data=FileOpen.readlines()
#print(data[0].strip("\n").split(" "))

#for i in data:
#    i.strip("\n").split(" ")
#    print(i)

for i in range(len(data)):
data[i]=data[i].strip("\n").split(" ")
print(data)
"""
"""
FileOpen=open('./01.dat','r')
     data=FileOpen.readline().strip("\n").split(" ")
for i in range(len(data)):
    data[i]=int(data[i])
print(type(data[0]))
"""
"""
a=255

def Calc_divisor(Number):
    for i in range(1,Number+1):
        if Number%i==0:
            print(i,"는",Number,"의 약수입니다")

Calc_divisor(a)
"""

"""
def Calu_square(lenth):
    area=lenth**2
    print(area)
Calu_square(float(input("input a")))
"""
"""
a=33
max_divisor=0

def square(number):
    square=number**2
    print(square)

def Calc_divisor_max(number):
    divisor_List=[]
    for i in range(1,number):
        if number%i==0:
            print(i,"는",number,"의 약수입니다")
            divisor_List.append(i)
    return max(divisor_List)

#max_divisor=Calc_divisor_max(a)
#print("약수 중 가장 큰 값은",max_divisor,"입니다")
square(Calc_divisor_max(a))
print("약수 중 가장 큰 값은",Calc_divisor_max(a),"입니다")
"""