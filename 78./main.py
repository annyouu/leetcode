from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        def backtrack(res, cur, start):
            res.append(cur[:])
            for i in range(start, len(nums)):
                cur.append(nums[i])
                backtrack(res, cur, i + 1)
                cur.pop()
        
        res = []
        backtrack(res, [], 0)
        return res