class Solution:
    def isGood(self, nums):
        n = max(nums)

        if len(nums) != n + 1:
            return False

        count = [0] * (n + 1)

        for x in nums:
            count[x] += 1

        for x in range(1, n):
            if count[x] != 1:
                return False

        return count[n] == 2
        