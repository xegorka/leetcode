from typing import List


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        answer = []
        for i in range(1, n + 1):
            if not i % 5 and not i % 3:
                answer.append('FizzBuzz')
            elif not i % 3:
                answer.append('Fizz')
            elif not i % 5:
                answer.append('Buzz')
            else:
                answer.append(str(i))
        return answer


def main() -> int:
    n = 5
    print(Solution().fizzBuzz(n))
    return 0


if __name__ == '__main__':
    main()
