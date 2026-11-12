class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if (len(nums)) == 0:
            return False
        if (len(nums)) < 2:
            return False
        lenOfMap = len(set(nums))
        return lenOfMap != len(nums)        