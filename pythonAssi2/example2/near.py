a = []

def findNearVal(lst):
    cnt = 0
    distance = (lst[0][0])**2 + (lst[0][1])**2
    for i in range(len(lst)):
        if distance >= (lst[i][0])**2 + (lst[i][1])**2:
            distance = (lst[i][0])**2 + (lst[i][1])**2 
            cnt = 0
        else:
            cnt += 1
    pos = len(lst) - cnt - 1
    return lst[pos][0], lst[pos][1]

while True:
    try:    
        x_value, y_value = input("좌표 입력: ").split(" ")
        x_value, y_value = int(x_value), int(y_value)
        a.append((x_value, y_value))
    except:
        print("최근접 좌표", findNearVal(a))
        break