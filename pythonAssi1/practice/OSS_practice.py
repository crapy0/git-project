sum1 = 0
sum2 = 0
totalGrade = 0
totalSum1 = 0
sTotalSum1 = 0
gpa = 0
sGpa = 0

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
        
while True:
    print("작업을 선택하세요")
    print("1. 입력")
    print("2. 출력")
    print("3. 계산")
    p = int(input())

    if (p == 1):
        grade_file = open("grade_file.txt", "w", encoding="utf8")
        while((totalSum1 + sTotalSum1) < 132):
            sum1 = int(input("학점을 입력하세요: "))
            sum2 = input("평점을 입력하세요: ")
            if sum2 != "F":
                totalSum1 += sum1
            else:
                sTotalSum1 += sum1
            totalGrade += sum1 * gradeCompute(sum2)
        gpa = totalGrade / (totalSum1 + sTotalSum1)
        gpa = "{:.2f}".format(gpa)
        sGpa = totalGrade / totalSum1
        sGpa = "{:.2f}".format(sGpa)
        print("gpa:", gpa, "sGpa: ", sGpa, "totalSum1:", totalSum1, "sTotalSum1", sTotalSum1) # 값이 잘 들어갔는지 확인용 출력
        
        print("제출용 학점: "+ str(totalSum1) +" (GPA: "+ sGpa + ")", file = grade_file) 
        print("열람용 학점: "+ str(totalSum1 + sTotalSum1) +" (GPA: " + gpa + ")", file = grade_file)

        grade_file.close()
        

            
    elif (p==2):
        grade_file = open("grade_file.txt", "r", encoding="utf8")
        print(grade_file.read())
        grade_file.close()
