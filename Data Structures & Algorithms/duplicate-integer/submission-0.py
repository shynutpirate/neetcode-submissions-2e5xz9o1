class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        uniqElements = set(nums)
        return not len(uniqElements) == len(nums)