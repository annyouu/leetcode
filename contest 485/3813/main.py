# class Solution:
#     def vowelConsonantScore(self, s: str) -> int:
#         score = 0
#         things = list(s)
#         # 母音のカウント
#         v= 0
#         # 子音のカウント
#         c = 0

#         for val in things:
#             # まず空白だったら次へ
#             if val == "":
#                 continue
#             else:
#                 # もし母音だったら
#                 if val in ('a','i','u','e','o'):
#                     v += 1
#                 else:
#                     # 数字か
#                     if val in ('1','2','3','4','5','6','7','8','9'):
#                         continue
#                     else:
#                         c += 1
        
#         if c == 0:
#             return 0
#         else:
#             score = floor(v / c)
#             return score
        
# 正答例
        
class Solution:
    def vowelConsonantScore(self, s: str) -> int:
        v = 0
        c = 0

        for ch in s:
            if ch.isalpha():
                if ch in ('a','i','u','e','o'):
                    v += 1
                else:
                    c += 1
        
        if c == 0:
            return 0
        else:
            return v // c