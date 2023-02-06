from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        j = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[j] = nums[i]
                j += 1
        return j


def main() -> int:
    nums = [3, 2, 2, 3]
    val = 3
    print(Solution().removeElement(nums, val))
    return 0


if __name__ == '__main__':
    main()
