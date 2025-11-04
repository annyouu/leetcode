# 前から後ろから読んでも同じintかどうかを判定する

class Solution:
    def isPalindrome(self, x: int) -> bool:
        # 整数での比較

        # 負の数は回文にはならない
        if x < 0:
            return False
        
        original = x
        reversed_num = 0

        while x > 0:
            digit = x % 10 # 一番下の桁を取り出す
            reversed_num = reversed_num * 10 + digit
            x //= 10 # 下の桁を削除する
        
        # 元の整数と逆順整数を比較する
        return original == reversed_num



        # 文字列での比較
        # s = str(x)

        # return s == s[::-1]
