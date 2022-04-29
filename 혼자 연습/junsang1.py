'''print("hello world")
print(5)
print(3.14)
print(1004)
print(5+10)
print(9*193)
print(3*4*312/3)
print('풍선')
print("나비")
print("ㅎ"*4)
print(5<10)
print(not True)
print(not (5>10))
애완동물을 소개해주세요'''
# animal = "고양이"
# name = "라온이"
# age = 4
# hobby = "잠자기"
# is_adult = age >= 5
#
# print("우리집 " + animal + "의 이름은 " + name + "에요")
# #hobby = "사냥"
# #print(name + "는 " + str(age) + "살이고요")
# print(name, "는 ", age, "살이고요")
# print(name + "는 " + hobby + "을 좋아해요")
# print(name + "는 어른일까요? " + str(is_adult))

# station = "사당"
# print(station + "행 열차가 들어오고 있습니다.")
# print(4**3)
# print(3.14%2)
# print(1313147%13)
# print(21//4)
# print(3 >= 5)
# print(3 == 3)
# print(3 == 2+1)
# print(3*12 == 6*2)
# print(1 != 1)
# print(1 != 3)
# print(not(1 == 1))
# print((3>1) and (7<8))
# print((5>2) & (4<8))
# print((3<5) or (6<4))
# print((3<1) | (5<10))
# print(5>3>1)
# print(5>3>7)
# print(5*4*2)
# number = 2 + 5 * 4
# print(number)
# number = number * 3
# print(number)
# number += 3
# print(number)
# number %= 4
# print(number)
# number /= 3
# print(number)
# number //= 4
# print(number)
# print(abs(-15))
# print(pow(3, 5))
# print(max(2*4, 43/3))
# print(min(4**3, 53//3))

# sentence='http://naver.com'
# my_sentence=sentence.replace("http://","") #A를 B로
# my_sentence=my_sentence[0:my_sentence.index(".")] #0부터.까지
# password=my_sentence[:3]+str(len(my_sentence))+str(my_sentence.count("e"))+"!"
# print("{}의 비밀번호는 {}입니다.".format(sentence,password))

# sentence='http://naver.com'
# my_sentence=sentence[7:sentence.index(".")] #0부터.까지
# password=my_sentence[:3]+str(len(my_sentence))+str(my_sentence.count("e"))+"!"
# print("{}의 비밀번호는 {}입니다.".format(sentence,password))
from random import *
List1=range(1,21)
List1=list(List1)
shuffle(List1)
winner=sample(List1,4)
print("---당첨을 축하합니다---")
print("치킨 당첨자 :{}".format(winner[0]))
print("커피 당첨자 :{}".format(winner[1:]))
print("---축하합니다---")


