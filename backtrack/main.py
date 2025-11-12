from pyparsing import nums

def backtrack(i, current):
    if i == len(nums):
        print(current)
        return
    
    backtrack(i + 1, current)
    backtrack(i + 1, current + [nums[i]])

nums = [1, 2, 3]
backtrack(0, [])
