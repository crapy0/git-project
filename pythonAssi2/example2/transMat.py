s0, s1, s2 = [], [], []
p = tuple(input("행과 열 개수를 입력하세요: ").split(" "))


for i in range(int(p[0])):
    s0.append(tuple(input(str(i+1) + "행 원소를 입력하세요: ").split(" ")))
print(s0)

for i in range(len(s0[0])):
    for j in range(len(s0)):
        s1.append(s0[j][i])
    s2.append(tuple(s1))
    s1 = []

    