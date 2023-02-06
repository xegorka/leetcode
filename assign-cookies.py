from typing import List


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        i = 0
        for c in s:
            if c >= g[i]:
                i += 1
            if i == len(g):
                break
        return i


def main() -> int:
    g = [1, 2, 3]
    s = [1, 1]
    print(Solution().findContentChildren(g, s))
    return 0


if __name__ == '__main__':
    main()
