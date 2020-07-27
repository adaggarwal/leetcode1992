


class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return None
        if root.val == val:
            return root
        return Solution.searchBST(self, root.right, val) if root.val<val else Solution.searchBST(self, root.left, val) 