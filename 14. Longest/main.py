class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        A = strs[0]

        for s in strs[1:]:
            while not s.startwith(A):
                A = A[:-1]
        return A