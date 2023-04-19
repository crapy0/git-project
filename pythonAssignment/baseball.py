import time
item = []

def setBall(num, rand):
    noItem = [i for i in range(10)] # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    lst = []
    a = 1
    for i in range(num):
        if 9 - int(rand[-a]) >= i:
            lst.append(noItem.pop(int(rand[-a])))
        else:
            i -= 1
            continue 
        a += 1
    return lst

def chkScore(record, std):
    strike, ball = 0, 0
    for i in range(len(record)):
        if record[i] == std[i]:
            strike += 1
        if record[i] == std[0] or record[i] == std[1] or record[i] == std[2]:
            ball += 1
    ball -= strike
    return strike, ball


startTime = time.time()
s = input("시작하겠습니까?")
endTime = time.time()
randNum = str(endTime-startTime)

# print(randNum)
# print(endTime-startTime) # 둘 다 테스트 출력 코드입니다
item = setBall(3, randNum)
item = tuple(item)

while True:
    s = tuple(map(int, input("숫자 3개(공백으로 나눠):").split()))
    if len(s) != 3:
        continue
    strike, ball = chkScore(s, item)
    if strike == 3:
        print(strike, "strike!!")
        break
    print(strike, "strike", ball, "ball")

