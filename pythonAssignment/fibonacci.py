n = int(input("값 입력."))



def fibonacci(a, b, cnt):
    if cnt > 0:
        print(a, end = " ")
        fibonacci(b, a+b, cnt - 1)
    
        
        

fibonacci(0, 1, n)