class Solution:
    def addDigits(self, num: int) -> int:
        while num >= 10:
            new_num = 0
            cur = num
            while cur:
                cur, d = divmod(cur, 10)
                new_num += d
            num = new_num
        return num


def main() -> int:
    num = 38
    print(Solution().addDigits(num))
    return 0


if __name__ == '__main__':
    main()
