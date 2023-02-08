def has_33(nums):
    for i in range(len(nums)):
        if i+1 == len(nums):
            return False
        if nums[i] == nums[i+1] == 3:
            return True
    
print(has_33([1, 3, 3]))
print(has_33([1, 3, 1, 3]))
print(has_33([3, 1, 3]))
