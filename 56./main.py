from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        n = len(intervals)
        used = [False] * n
        result = []

        for i in range(n):
            if used[i]:
                continue
            start, end = intervals[i]
            for j in range(i + 1, n):
                if used[j]:
                    continue
                start2, end2 = intervals[j]

                # 重なる判定
                if start2 <= end:
                    end = max(end, end2)
                    used[j] = True
                else:
                    break
        
            result.append([start, end])
        return result
        