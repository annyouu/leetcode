from typing import List

class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        # res_even = []
        # res_odd = []

        # for num in nums:
        #     if num % 2 == 0:
        #         res_even.append(num)
        #         res_even.sort()
        #     else:
        #         res_odd.append(num)
        #         res_odd.sort()
        
        # for num in res_odd:
        #     res_even.append(num)
        
        # return res_even

        res_even = [x for x in nums if x % 2 == 0]
        res_odd =  [x for x in nums if x % 2 != 0]
        
        res_even.sort()
        res_odd.sort()

        return res_even + res_odd
