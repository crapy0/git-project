totalGrade, totalSum1, sTotalSum1 = 0, 0, 0
key = 0 # initalizing
class CourseHistory: # 모든 수강내역을 관리하는 Class입니다.
    subject = {key: ""} # 수강과목 수가 자연히 늘어남
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
        case _: # 예외가 발생하는지 알기 위해 default값을 정합니다
            return -1
def chkDup(lst): # 중복된 수강내역 중 낮은 학점을 받은 이력을 제거하는 함수입니다
    for i in range(len(lst)-1):
        if CourseHistory.subject[lst[i][0]] == CourseHistory.subject[lst[len(lst)-1][0]]:
            if gradeCompute(lst[i][2]) >= gradeCompute(lst[len(lst)-1][2]):
                lst.pop(len(lst)-1)
                break
            else:
                tup1 = lst.pop(i)
                tup2 = lst.pop(len(lst)-1)
                lst.insert(i, (tup1[0], tup2[1], tup2[2]))
                break
        else:
            continue
    return lst

key = len(CourseHistory.subject) - 1
while True:
    print()
    print("작업을 선택하세요")
    print("1. 입력")
    print("2. 출력")
    print("3. 조회")
    print("4. 계산")
    print("5. 저장")
    print("6. 불러오기")
    print("7. 종료")
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
            for i in CourseHistory.item:
                print(f"[{CourseHistory.subject[i[0]]}] {i[1]}학점: {i[2]}")
            continue
        elif p==3: # 조회
            name = input("과목명을 입력하세요: ")
            for i in CourseHistory.item:
                if CourseHistory.subject[i[0]] == name:
                    print(f"[{CourseHistory.subject[i[0]]}] {i[1]}학점: {i[2]}")
                    break
                if i[0] == len(CourseHistory.subject) - 1:
                    print("해당 과목이 없습니다")
            continue
        elif p==4: # 계산
            for i in CourseHistory.item:
                totalGrade += i[1] * gradeCompute(i[2]) 
                if i[2] != "F":
                    totalSum1 += i[1]
                else:
                    sTotalSum1 += i[1]
            gpa = totalGrade / (totalSum1 + sTotalSum1)
            gpa = "{:.2f}".format(gpa)
            sGpa = totalGrade / totalSum1
            sGpa = "{:.2f}".format(sGpa)
            
            print(f"제출용: {totalSum1} (GPA: {sGpa})")
            print(f"열람용: {totalSum1+sTotalSum1} (GPA: {gpa})")
            totalGrade, totalSum1, sTotalSum1 = 0, 0, 0
            continue
        elif p==5: # 파일 저장 
            with open("score.csv", "w", encoding="utf   8") as scoreFile:
                for i in CourseHistory.item:
                    scoreFile.write(f"{CourseHistory.subject[i[0]]}, {i[1]}, {i[2]}\n")
            print("파일로 저장합니다.") # 삭제기능이 없어서 수정하려면 새로 저장해야 합니다.
            continue
        elif p==6: # 파일 불러오기
            if len(CourseHistory.subject) != 1: # 충돌 회피, 이어쓰기가 가능하도록 요구하시면 수정하겠습니다
                print("파일을 불러올 수 없습니다.")
                continue
            with open("score.csv", "r", encoding="utf8") as scoreFile:
                info = scoreFile.readlines() # 과제에서 다루는 파일은 용량이 작으므로 readlines를 사용했습니다.
                # print(info)
                for line in info:
                    line_data = line.strip().split(', ')
                    CourseHistory.subject[key] = line_data[0]
                    CourseHistory.item.append((key, int(line_data[1]), line_data[2]))
                    key += 1
            print("파일을 불러왔습니다.")
        elif p==7: # 종료
            break
    except: # 예외 처리
        print("잘못된 입력입니다.")
        continue

