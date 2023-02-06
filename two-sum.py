from typing import List

# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         arr = []
#         for x in nums:
#             arr.append(x)
#         arr.sort()
#         left, right = 0, len(arr) - 1
#         while left < right:
#             if arr[left] + arr[right] == target:
#                 break
#             if arr[left] + arr[right] > target:
#                 right -= 1
#                 continue
#             if arr[left] + arr[right] < target:
#                 left += 1
#                 continue

#         ans = []
#         for i, x in enumerate(nums):
#             if x == arr[left] or x == arr[right]:
#                 ans.append(i)
#         return ans


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i, num in enumerate(nums):
            comp = target - num
            if comp in seen:
                return list((i, seen[comp]))
            seen[num] = i


def main() -> int:
    nums = [3, 2, 4]
    target = 6
    print(Solution().twoSum(nums, target))
    return 0


if __name__ == '__main__':
    main()
