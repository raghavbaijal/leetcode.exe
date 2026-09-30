class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        ans = []

        for word in words:
            total = 0

            for ch in word:
                index = ord(ch) - ord('a')
                total += weights[index]

            remainder = total % 26
            ans.append(chr(ord('z') - remainder))

        return ''.join(ans)