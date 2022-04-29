# Number=2
# while Number<=100:
for Number in range(2,1100):
    a=1
    count=0
    while a<=Number:
        if Number%a == 0:
            count+=1
        a+=1
    if count == 2:
        print(Number)
    Number+=1

"""
Number=2
while Number<=10:
#for Number in range(2,11):
    a=1
    count=0
    while a<=Number:
        if Number%a == 0:
            count+=1
        a += 1
    if count == 2:
        print(Number)

    Number+=1
"""



