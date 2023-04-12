# sum1 = 0
# sum2 = 0
# gpa = 0
# sGpa = 0, 초기화가 필요 없는 줄을 몰랐습니다...
totalGrade, totalSum1, sTotalSum1 = 0, 0, 0

subject = {key: "" for key in range(100, 500)}
key = 100 # initalizing
item = []

def gradeCompute(sum2):
    match sum2:
        case 'A+':
            return 4.5
        case 'A':
            return 4.0
        case 'B+':
            return 3.5
        case 'B':
            return 3.0
        case 'C+':
            return 2.5
        case 'D':
            return 2.0
        case 'F':
            return 0

def chkDup(lst):
    for i in range(len(lst)-1):
        if subject[lst[i][0]] == subject[lst[len(lst)-1][0]]:
            if gradeCompute(lst[i][2]) >= gradeCompute(lst[len(lst)-1][2]):
                lst.pop(len(lst)-1)
                break
            else:
                lst.pop(i)
                break
        else:
            continue
    return lst
        
while totalSum1 + sTotalSum1 < 132:
    print("작업을 선택하세요")
    print("1. 입력")
    print("2. 출력")
    print("3. 계산")

    p = int(input())

    if p == 1:
        subject[key] = input("과목명을 입력하세요: ")
        sum1 = int(input("학점을 입력하세요: "))
        sum2 = input("평점을 입력하세요: ")
        item.append((key, sum1, sum2))        
        if sum2 != "F":
            totalSum1 += sum1
        else:
            sTotalSum1 += sum1
        totalGrade += sum1 * gradeCompute(sum2)
        key += 1
        item = chkDup(item)
        print()
            
    elif p==2:
        for i in range(0, len(item)):
            print("["+ subject[item[i][0]] +"]", str(item[i][1]) +"학점: "+ item[i][2])
        continue

    elif p==3:
        gpa = totalGrade / (totalSum1 + sTotalSum1)
        gpa = "{:.2f}".format(gpa)
        sGpa = totalGrade / totalSum1
        sGpa = "{:.2f}".format(sGpa)
        
        print("제출용: "+ str(totalSum1) +"(GPA: "+ str(sGpa) +")")
        print("열람용: "+ str(totalSum1+sTotalSum1) +"(GPA: "+ str(gpa) +")")
        break
    else:
        print("잘못된 값을 입력하셨습니다")
        continue
