class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        longest, length = 0, 0

        for n in nums:
            if n == 0:
                longest = max(longest, length)
                length = 0
                continue
            length += 1
        return max(longest, length)