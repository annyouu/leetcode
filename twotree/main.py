def solution(root: TreeNode) -> int:
    # ノードが空の場合は深さ0を返す
    if root is None:
        return 0
    
    # 再帰ステップ: 左の子ノードの深さを求める
    left_depth = solution(root.left)

    # 再帰ステップ： 右の子ノードの深さを求める
    right_depth = solution(root.right)

    # 左右の深さのうち、大きい方に1を足して返す
    return 1 + max(left_depth, right_depth)