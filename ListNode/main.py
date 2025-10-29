class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val     # ノードの値
        self.next = next   # 次のノード（Noneなら終わり）

# リストの作成
node3 = ListNode(3)
node2 = ListNode(2, node3)
node1 = ListNode(1, node2)
head = node1

# ノードを1つ追加してみる
new_node = ListNode(4)
node3.next = new_node

cur = head
while cur:
    print(cur.val)
    cur = cur.next