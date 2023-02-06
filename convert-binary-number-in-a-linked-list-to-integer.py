# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        ans = 0
        while head:
            ans = head.val + ans * 2
            head = head.next
        return ans


def main() -> int:
    print(Solution().getDecimalValue(head))
    return 0


if __name__ == '__main__':
    main()
