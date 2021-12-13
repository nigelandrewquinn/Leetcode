# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        res = 0
        if root:
            res = self.rangeSumBST(root.left, low, high)
            if low <= root.val <= high:
                res += root.val
            res = res + self.rangeSumBST(root.right, low, high)
        return res
