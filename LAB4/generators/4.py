def squares(a,b):
    for i in range(a, b+1):
        yield i * i

for x in squares(int(input()), int(input())):
    print(x, end = " ")