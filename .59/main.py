from typing import List

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        # n * nの0行列を作成する
        matrix = [[0] * n for _ in range(n)]

        # 上下左右の境界を設定する
        left, right, top, bottom = 0, n - 1, 0, n - 1
        num = 1

        while left <= right and top <= bottom:
            # 左 → 右
            for i in range(left, right + 1):
                matrix[top][i] = num
                num += 1
            top += 1

            # 上 → 下
            for i in range(top, bottom + 1):
                matrix[i][right] = num
                num += 1
            right -= 1

            # 右 → 左
            if top <= bottom:
                for i in range(right, left - 1, -1):
                    matrix[bottom][i] = num
                    num += 1
                bottom -= 1

            # 下 → 上
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    matrix[i][left] = num
                    num += 1
                left += 1
        
        return matrix