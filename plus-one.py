from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        for i in range(len(digits) - 1, -1, -1):
            carry, digits[i] = divmod(digits[i] + carry, 10)
        return digits if not carry else [carry] + digits


def main() -> int:
    digits = [1, 2, 3]
    print(Solution().plusOne(digits))
    return 0


if __name__ == '__main__':
    main()
