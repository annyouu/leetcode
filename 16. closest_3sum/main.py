class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        # 全て0だったら、0を返す
        if all(x == 0 for x in nums):
            return 0

        # ソートしてrightとleftで攻める
        N = len(nums)
        nums.sort()

        # 初期値を設定した
        closest_sum = nums[0] + nums[1] + nums[2]

        for i in range(N - 2):
            left, right = i + 1, N - 1
            while left < right:
                s = nums[i] + nums[left] + nums[right]

                if abs(s - target) < abs(closest_sum - target):
                    closest_sum = s
                
                if s < target:
                    left += 1
                elif s > target:
                    right -= 1
                else:
                    return s
        
        return closest_sum

