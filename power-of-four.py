# class Solution:
#     def isPowerOfFour(self, n: int) -> bool:
#         if n == 1:
#             return True
#         if n < 4:
#             return False
#         x = 1
#         while 4**x <= n:
#             if 4**x == n:
#                 return True
#             x += 1
#         return False


class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n < 1:
            return False
        if n == 1:
            return True
        return self.isPowerOfFour(n / 4)


def main() -> int:
    print(Solution().isPowerOfFour(64))
    return 0


if __name__ == '__main__':
    main()
