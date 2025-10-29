from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = []
        a = 0
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                a = nums[i] + nums[j]
                if a == target:
                    return [i, j]
        