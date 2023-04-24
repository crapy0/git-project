def hanoi(num, source, destination, pos):
    if num == 1:
        print(source, "->", destination)
        return
    hanoi(num-1, source, pos, destination)
    print(source, "->", destination)
    hanoi(num-1, pos, destination, source)


hanoi(4, 1, 3, 2)