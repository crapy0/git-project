a = []

def chkDup(lst, limit):
    b = set()
    cnt = 0
    for i in range(len(lst)):
        for j in range(len(lst)):
            if lst[i] == lst[j]:
                if i != j:
                    cnt += 1
                if cnt >= limit:
                    b.add(lst[i])
                    break
        cnt = 0
    return b 

limitDup = int(input("허용 중복수: "))

while True:
    try:
        num = int(input("값 입력: "))
        a.append(num)
    except:
        a = tuple(a)
        print("중복된 수", chkDup(a, limitDup)) 
        break   
