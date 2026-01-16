class Solution:
    def isValid(self, s: str) -> bool:
        # スタック構造の使用
        stack = []

        # ハッシュテーブルを使う
        hash_table = {
            ')': "(",
            "}": "{",
            "]": "[",
        }

        for char in s:
            # charが空きかっこなら
            if char in hash_table.values():
                stack.append(char)

            # charが閉じかっこなら
            if char in hash_table.keys():
                if not stack or hash_table[char] != stack.pop():
                    return False

        return not stack
