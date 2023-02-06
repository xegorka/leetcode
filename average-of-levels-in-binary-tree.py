from typing import List, Optional
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        ans = []
        q = deque([root])
        while q:
            cnt = 0
            summ = 0

            for _ in range(len(q)):
                cur = q.popleft()
                summ += cur.val
                cnt += 1
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
            ans.append(summ/cnt)
        return ans


def main() -> int:
    root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    print(Solution().averageOfLevels(root))
    return 0


if __name__ == '__main__':
    main()
