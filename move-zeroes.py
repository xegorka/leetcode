from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        right = 0
        for left in range(len(nums)):
            if nums[left]:
                nums[right], nums[left] = nums[left], nums[right]
                right += 1
        return


def main() -> int:
    nums = [0, 1, 0, 3, 12]
    print(Solution().moveZeroes(nums))
    print(nums)
    return 0


if __name__ == '__main__':
    main()
