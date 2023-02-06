from typing import List


class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        seen = set()
        for num in arr:
            if num*2 in seen or num/2 in seen:
                return True
            seen.add(num)
        return False


def main() -> int:
    arr = [10, 2, 5, 3]
    print(Solution().checkIfExist(arr))
    return 0


if __name__ == '__main__':
    main()
