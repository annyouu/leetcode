class Solution:
    def permute(self, nums):
        res = []

        def backtrack(path, used):
            print("呼び出し:", path)

            # 全て使ったら結果に追加
            if len(path) == len(nums):
                print("完成:", path)
                res.append(path[:])

                print("戻る（完成後）:", path)
                return
            
            for n in nums:
                if n in used:
                    continue

                print(f" → {n}を追加")
                path.append(n)
                used.add(n)

                backtrack(path, used)

                # 戻る
                print(f" ← {n}を削除して戻る")
                path.pop()
                used.remove(n)
        
        backtrack([], set())
        return res


if __name__ == "__main__":
    nums = [1, 2, 3]
    solution = Solution()
    result = solution.permute(nums)
    print("\n--- 最終結果 ---")
    print(result)