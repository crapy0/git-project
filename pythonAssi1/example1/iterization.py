import random

anw = random.randrange(1, 101)
count = 0
p = int(input("(1~100)사이의 정수: "))

while count < 10:
    if p > anw:
        print("up")
        p = int(input("(1~100)사이의 정수: "))
    elif p < anw:
        print("down")
        p = int(input("(1~100)사이의 정수: "))
    else:
        print("정답")
        break

