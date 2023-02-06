from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        cur_min, cur_max = strs[0], strs[0]
        for i in range(len(strs)):
            cur_min = min(cur_min, strs[i])
            cur_max = max(cur_max, strs[i])
        prefix = ''
        for i in range(len(cur_min)):
            if cur_min[i] != cur_max[i]:
                break
            prefix += cur_min[i]
        return prefix


def main() -> int:
    strs = ["flower", "flow", "flight"]
    print(Solution().longestCommonPrefix(strs))
    return 0


if __name__ == '__main__':
    main()
