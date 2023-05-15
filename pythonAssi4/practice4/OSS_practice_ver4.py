totalGrade, totalSum1, sTotalSum1 = 0, 0, 0
key = 0 # initalizing
class CourseHistory: # 모든 수강내역을 관리하는 Class입니다.
    subject = {key: "" for key in range(0, 60)} # 수강과목수가 60개를 넘지 않는다고 가정
    item = []
    def __init__(self):
        self.name 
        self.credit
        self.grade

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
        case _:
            return -1

def chkDup(lst): # 중복된 수강내역 중 낮은 학점을 받은 이력을 제거하는 함수입니다
    for i in range(len(lst)-1):
        if CourseHistory.subject[lst[i][0]] == CourseHistory.subject[lst[len(lst)-1][0]]:
            if gradeCompute(lst[i][2]) > gradeCompute(lst[len(lst)-1][2]):
                lst.pop(len(lst)-1)
                break
            else:
                tup1 = lst.pop(i)
                tup2 = lst.pop(len(lst)-1)
                lst.append((tup1[0], tup2[1], tup2[2]))
                break
        else:
            continue
    return lst
 
while True:
    print()
    print("작업을 선택하세요")
    print("1. 입력")
    print("2. 출력")
    print("3. 조회")
    print("4. 계산")
    print("5. 종료")
    try:
        p = int(input())
        if p == 1: # 입력
            CourseHistory.subject[key] = input("과목명을 입력하세요: ")
            sum1 = int(input("학점을 입력하세요: "))
            sum2 = input("평점을 입력하세요: ")
            if gradeCompute(sum2) != -1:
                CourseHistory.item.append((key, sum1, sum2))        
                key += 1
                CourseHistory.item = chkDup(CourseHistory.item) # item에 들어있는 수강과목 중에서 중복된 값을 제거합니다 
            else:
                print("잘못된 입력입니다.")
        elif p==2: # 출력
            for i in range(0, len(CourseHistory.item)):
                print("["+ CourseHistory.subject[CourseHistory.item[i][0]] +"]", str(CourseHistory.item[i][1]) +"학점: "+ CourseHistory.item[i][2])
            continue
        elif p==3: # 조회
            name = input("과목명을 입력하세요: ")
            for i in range(len(CourseHistory.item)):
                if CourseHistory.subject[CourseHistory.item[i][0]] == name:
                    print("["+ CourseHistory.subject[CourseHistory.item[i][0]] +"]", str(CourseHistory.item[i][1]) +"학점: "+ CourseHistory.item[i][2])
                    break
                elif i == len(CourseHistory.item)-1:
                    print("해당 과목이 없습니다")
                    break
            continue
        elif p==4: # 계산
            for i in range(len(CourseHistory.item)):
                totalGrade += CourseHistory.item[i][1] * gradeCompute(CourseHistory.item[i][2]) 
                if CourseHistory.item[i][2] != "F":
                    totalSum1 += CourseHistory.item[i][1]
                else:
                    sTotalSum1 += CourseHistory.item[i][1]
            gpa = totalGrade / (totalSum1 + sTotalSum1)
            gpa = "{:.2f}".format(gpa)
            sGpa = totalGrade / totalSum1
            sGpa = "{:.2f}".format(sGpa)
            
            print("제출용: "+ str(totalSum1) +"(GPA: "+ str(sGpa) +")")
            print("열람용: "+ str(totalSum1+sTotalSum1) +"(GPA: "+ str(gpa) +")")
            totalGrade, totalSum1, sTotalSum1 = 0, 0, 0
            continue
        elif p==5: # 종료
            break

    except: # 예외 처리
        print("잘못된 입력입니다.")
        continue
