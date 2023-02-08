def spy_game(nums):
    firstZero = False
    secondZero = False
    for x in nums:
        if x == 0:
            if secondZero == 0 and firstZero == 1:
                secondZero = True
            else:
                firstZero = True
        elif x == 7:
            if firstZero == secondZero == True:
                return True
            else:
                firstZero = secondZero = False
    return False
 
            
        

print(spy_game([1,2,4,0,0,7,5])) 
print(spy_game([1,0,2,4,0,5,7]))
print(spy_game([1,7,2,0,4,5,0]))