class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo = 0
        hi = len(nums) -  1

        while lo <= hi:
            m = (lo + hi) // 2
            if nums[m] == target:
                return m
            elif target < nums[m]:
                hi = m - 1
            else:
                lo = m + 1
        return -1 
            
        