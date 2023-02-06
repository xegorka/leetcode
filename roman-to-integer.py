class Solution:
    def romanToInt(self, s: str) -> int:
        d = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }
        ans, i = 0, 0
        while i < len(s):
            if i < len(s) - 1 and d[s[i]] < d[s[i + 1]]:
                ans += d[s[i + 1]] - d[s[i]]
                i += 2
            else:
                ans += d[s[i]]
                i += 1
        return ans


def main() -> int:
    s = "III"
    print(Solution().romanToInt(s))
    return 0


if __name__ == '__main__':
    main()
