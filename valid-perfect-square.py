class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num == 1:
            return True
        left, right = 1, num // 2
        while left <= right:
            mid = (left + right) // 2
            sq = mid * mid
            if sq == num:
                return True
            if sq < num:
                left = mid + 1
            else:
                right = mid - 1
        return False


def main() -> int:
    num = 9
    print(Solution().isPerfectSquare(num))
    return 0


if __name__ == '__main__':
    main()
