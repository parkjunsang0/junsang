# FileOpen = open('./palindrome.inp', 'r')
# data = FileOpen.readlines()
# for i in range(1,len(data)):
#     data[i]=data[i].lower().strip("\n")
#     data[i]=list(data[i])
#     #print(data[i])
#     data[i].reverse()
# FileOpen.close()
#
# FileOpen = open('./palindrome.inp', 'r')
# data1 = FileOpen.readlines()
# for i in range(1,len(data1)):
#     data1[i]=data1[i].lower().strip("\n")
#     data1[i]=list(data1[i])
#     if data1[i] == data[i]:
#         print("1")
#     else:print("0")
# FileOpen.close()

FileOpen = open('./palindrome.inp', 'r')
data = FileOpen.readlines()

for i in range(1,len(data)):
    data[i]=data[i].lower().strip("\n")
    data[i]=list(data[i])
    data[i].reverse()
FileOpen.close()
FileOpen = open('./palindrome.inp', 'r')
data1 = FileOpen.readlines()
for i in range(1,len(data1)):
    data1[i]=data1[i].lower().strip("\n")
    data1[i]=list(data1[i])
FileOpen.close()

with open('./palindrome.out', 'w') as FileOpen:
    for i in range(1, len(data1)):
        if data1[i] == data[i]:
            FileOpen.write("1\n")
        else:FileOpen.write("0\n")