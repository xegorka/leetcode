from collections import Counter


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        return list((Counter(t) - Counter(s)).elements())[0]


def main() -> int:
    s = "abcd"
    t = "abcde"
    print(Solution().findTheDifference(s, t))
    return 0


if __name__ == '__main__':
    main()
