from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # 両方が存在しない場合
        if not p and not q:
            return True
        
        # どちらか一方だけ存在しない場合
        if not p or not q:
            return False

        # 値が異なる場合
        if p.val != q.val:
            return False

        # 左右の部分木も同じかチェックする
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        
        