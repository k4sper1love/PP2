import math
n = int(input("Input number of sides: "))
l = int(input("Input the length of a side: "))
perimetr = n * l
apofema = l / (2 * math.tan(math.pi/n))
area = round((perimetr * apofema) / 2)
print(area)