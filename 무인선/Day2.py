# FileOpen=open('./numbers.inp','r')
# numbers=FileOpen.readlines()
# NUMBERS=[]
# for i in range(len(numbers)):
#     numbers[i]=numbers[i].strip("\n").split(" ")
#     for k in range(len(numbers[i])):
#         numbers[i][k]=int(numbers[i][k])
#     numbers[i].sort()
#     print(numbers[i])



FileOpen=open('./numbers.inp','r')
Filewrite=open('./number.outres','w')

numbers=FileOpen.readlines()
List1=[]
List2=[]
List3=[]
List4=[]

for i in range(2,len(numbers),2):
    numbers[i]=numbers[i].strip("\n").split(" ")
    for k in range(len(numbers[i])):
        numbers[i][k]=int(numbers[i][k])
    numbers[i].sort()
    List1=(numbers[i][:2])
    List2=(numbers[i][-2:])
    List3='Test Case #'+str(int(i/2))+' :'
    List4=str(List3)+str(abs(List1[1]-List2[0]))
    #print(type(List4))
    print((List3),abs(List1[1]-List2[0]))
 #   with open('./numbers.out', 'a') as FileOpen:
    Filewrite.write(List4)
    Filewrite.write("\n")







