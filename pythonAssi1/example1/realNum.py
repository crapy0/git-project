n = 0.1
sum = 0
i = -1

while i>-56:
    i -= 1
    if sum + 2**i > n:
        continue
    else:
        sum += 2**i
    print(sum, " ", -i)
