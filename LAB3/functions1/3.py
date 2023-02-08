def solve(numheads, numlegs):
    rabbits = numlegs // 4
    chicken = numlegs % 4
    rec(rabbits, chicken, numheads)
   
def rec(rabbits , chicken, numheads):
    if rabbits + chicken == numheads:
        return print(rabbits, chicken)
    else:
        rec(rabbits - 1, chicken + 2, numheads)

solve(35, 94)
        