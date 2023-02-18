gen_3 = (str(x) for x in range(0, int(input())+1) if x % 3 == 0 and x % 4 == 0)
print(','.join(gen_3))