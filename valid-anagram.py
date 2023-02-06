from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)


def main() -> int:
    s = "anagram"
    t = "nagaram"
    # делаем два словарика и сравниваем их
    print(Solution().isAnagram(s, t))
    return 0


if __name__ == '__main__':
    main()
