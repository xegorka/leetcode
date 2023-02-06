from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def helper(root):
            if not root:
                return True, 0
            lb, lh = helper(root.left)
            rb, rh = helper(root.right)
            if not lb or not rb:
                return False, -1
            return abs(lh - rh) < 2, 1 + max(lh, rh)

        return helper(root)[0]


def main() -> int:
    print(Solution().isBalanced(root))
    return 0


if __name__ == '__main__':
    main()
