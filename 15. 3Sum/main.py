from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        N = len(nums)
        result = set()

        for i in range(N):
            for j in range(i + 1, N):
                for k in range(j + 1, N):
                    if nums[i] + nums[j] + nums[k] == 0:
                        triple = tuple(sorted([nums[i], nums[j], nums[k]]))
                        result.add(triple)
        
        return [list(t) for t in result]
