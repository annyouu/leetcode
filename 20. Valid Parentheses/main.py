class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {
            "(": ")",
            "{": "}",
            "[": "]",
        }

        for value in s:
            # 開きカッコ
            if value in pairs:
                stack.append(value)
            # 閉じカッコ
            elif value in pairs.values():
                # スタックが空ならFalse
                if not stack:
                    return False
                
                top = stack.pop()
                if pairs[top] != value:
                    return False
        
        return not stack