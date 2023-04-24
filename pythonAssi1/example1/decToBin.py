n = int(input("(1~10000사이의) 정수: "))
sum = 0
i = 15
sumb = 0 


def decToBin(i):
    return 10**i

while n < sum + 2**i and i>0:
    i -= 1
    if sum + 2**i > n:
        continue
    else:
        sum += 2**i
        # print(i, sum)
        sumb += decToBin(i)
print(sumb)

    
    
# n 을 입력 받으면 (14인 경우) 2^3이 구해지고 sum + 2**(i-1) < n 인 경우에는 더해지고, 아닌 경우 contuinue(i-=1)
# 같은 원리로 2^2 이 구해지고 2^1이 구해짐 
# i값을 함수에 연속적으로 넘겨줌  


#--- decToBin ---
# 함수를 하나 만들어서 i값을 받으면 해당 자리에 1로 채워 넣는다.
# i에 해당하지 않는 숫자는 0으로 채워 넣는다.
