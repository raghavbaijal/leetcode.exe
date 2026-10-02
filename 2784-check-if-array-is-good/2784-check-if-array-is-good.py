class Solution:
    def isGood(self, nums: list[int]) -> bool:
        n = len(nums) - 1

        count = {}

        for num in nums:
            count[num] = count.get(num, 0) + 1

        for i in range(1, n):
            if count.get(i, 0) != 1:
                return False

        return count.get(n, 0) == 2