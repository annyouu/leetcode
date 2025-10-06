from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)

        for s in strs:
            key = ''.join(sorted(s))  # ソートしてアナグラム共通のキーを作る
            anagrams[key].append(s)

        return list(anagrams.values())
