p = int(input("(1~100)사이의 정수: "))
n = 2
cnt = 0


while n <= p:
    if int(p/n) == p/n and p/n != 1:
        # print(p/n, "소수가 아닙니다")
        cnt += 1
    elif n==p and cnt==0:
        print(str(p) + "는 소수입니다")
    elif cnt > 0:
        print(str(p) + "는 소수가 아닙니다")
        break
    n += 1

