# x=float(input("input x :"))
# if x%2==0:
#     print("x는 짝수입니다")
# else:
#     print('x는 홀수입니다')
# if x>0:
#     print('x는 양수입니다')
# elif x<0:
#     print('x는 음수입니다')

"""
for number in range(0,50):
    number = number + 1
    print(number)
    if number==20:
        break
"""

number=0
while number\<3:
    x=float(input("input x:"))
    number=x%3
    print(number)
    number


"""
number=0
while number<3:
    x=float(input("input x:"))
    NUMBER=x/3
    print(NUMBER)
    if NUMBER<3:
        break
"""

"""
List2=[]
List1=[1,2,3,4,5]
for i in List1:
    if i>0:
        number=i**2
        List2.append(number)
#print(List2)
FileOpen=open('./List2.dat','w')
FileOpen.write(str(List2[0])+str(List2[1])+str(List2[2])+str(List2[3])+str(List2[4]))
FileOpen.close()
"""

"""
List2=[]
List1=['1','2','3','4','5']
i=int(List1[0])
j=int(List1[1])
k=int(List1[2])
l=int(List1[3])
m=int(List1[4])
number=i**2
List2.append(number)
number=j**2
List2.append(number)
number=k**2
List2.append(number)
number=l**2
List2.append(number)
number=m**2
List2.append(number)
I=str(List2[0])
J=str(List2[1])
K=str(List2[2])
L=str(List2[3])
M=str(List2[4])
print(List2)
FileOpen=open('./List2.dat','w')
FileOpen.write(str(List2[0]))
FileOpen.write(str(List2[1]))
FileOpen.write(str(List2[2]))
FileOpen.write(str(List2[3]))
FileOpen.write(str(List2[4]))
FileOpen.close()
"""