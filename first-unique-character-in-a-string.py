from collections import Counter


class Solution:
    def firstUniqChar(self, s: str) -> int:
        counter = Counter(s)
        for i, c in enumerate(s):
            if counter[c] == 1:
                return i
        return -1


def main() -> int:
    s = "loveleetcode"
    print(Solution().firstUniqChar(s))
    return 0


if __name__ == '__main__':
    main()
