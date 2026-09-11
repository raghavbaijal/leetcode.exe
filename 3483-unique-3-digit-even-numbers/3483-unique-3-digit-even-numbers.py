from itertools import permutations

class Solution:
    def totalNumbers(self, digits):
        ans = set()

        for a, b, c in permutations(digits, 3):
            if a != 0 and c % 2 == 0:
                ans.add(a * 100 + b * 10 + c)

        return len(ans)