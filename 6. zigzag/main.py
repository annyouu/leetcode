class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # 行数が1or 文字列の長さ以下ならそのまま返す
        if numRows == 1 or numRows >= len(s):
            return s
        
        rows = [""] * numRows
        cur_row = 0
        going_down = False

        for c in s:
            rows[cur_row] += c
            if cur_row == 0 or cur_row == numRows - 1:
                going_down = not going_down
            if going_down:
                cur_row += 1
            else:
                cur_row -= 1
        
        return "".join(rows)
            