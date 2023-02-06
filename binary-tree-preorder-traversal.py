from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        return (
            [root.val]
            + self.preorderTraversal(root.left)
            + self.preorderTraversal(root.right)
            if root
            else []
        )


def main() -> int:
    root = TreeNode(4, TreeNode(6, TreeNode(2)), TreeNode(8))
    print(Solution().preorderTraversal(root))
    return 0


if __name__ == '__main__':
    main()
