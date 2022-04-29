# x=3
# y=4
# print(type(x!=y))#같지 않다, #bool연산자 타입
# print(x<=y)

# x=float(input("input x:"))
# y=float(input("input y:"))
# if x>y:
#     print("x가 y보다 큽니다")
# elif x<y:
#     print("y가 x보다 큽니다")
# else:
#     print("x는 y와 같습니다")

# x=float(input("input number"))
# if x%2==0:
#     print("x는 짝수입니다")
# else:
#     print("x는 홀수입니다")
# elif x%2==1:
#     print("x는 홀수입니다")

# List1=[68,71,59,88,100,93,47]
# People=1
# for i in List1:
#     if i>=75:
#         print(People,"번째 학생은 합격입니다")
#     else:
#         print(People,"번째 학생은 불합격입니다")
#     People=People+1

# for i in range(0,40):
#     if i==20:
#         print(i,"프로그램이 종료됩니다")
#         break
#     print(i, "프로그램이 실행 중입니다")

#Length=1
#while Length<11:
#    area=Length**2
#    print(area)
#    Length=Length+1
#print("end")

#x=0
#while x<7642:
#    x=float(input("input x"))
#    print(x)
#print("end")

# Running=True
# number=0
# while Running==True:
#     if number==30:
#         Running=False
#     number+=1
#     print(number)


# x=0
# while x<99999:
#     number=float(input("input number"))
#     number=x**2+2*x+1
#     print(number)


# Result=0
# while Result<=1000:
#     x=int(input("input x : "))
#     Result=x**2+2*x+1
#     print(Result)


# a=['1','2','3','4','5']
#
# FileOpen=open('./01.dat','w')
# FileOpen.write(a[0]+a[1]+a[2]+a[3]+a[4])
# =
# FileOpen.write(a[0])
# FileOpen.write(a[1])
# FileOpen.write(a[2])
# FileOpen.write(a[3])
# FileOpen.write(a[4])
# +" "
# FileOpen.write(a[0]+" "+a[1]+" "+a[2]+" "+a[3]+" "+a[4])
# FileOpen.close()


# a=['1','2','3','4','5']
# b=['6','7','8','9','10']

# FileOpen=open('./220124/01.dat','w')
# FileOpen.write(a[0]+a[1]+a[2]+a[3]+a[4]+"\n")
# FileOpen.write(b[0]+b[1]+b[2]+b[3]+b[4])
# FileOpen.close()

# a=['1','2','3','4','5']
# b=['6','7','8','9','11']
# with open('./220124/01.dat','w') as FileOpen:
#     FileOpen.write(a[0]+a[1]+a[2]+a[3]+a[4]+"\n")
#     FileOpen.write(b[0]+b[1]+b[2]+b[3]+b[4])
#     FileOpen.close() (with open as FileOpen 쓰면 안 써도 상관 없)