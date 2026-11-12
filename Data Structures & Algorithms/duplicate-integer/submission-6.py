class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if (len(nums)) == 0:
            return False
        if (len(nums)) < 2:
            return False
        # lenOfMap = len(set(nums))
        # return lenOfMap != len(nums)        

        nums_sorted = sorted(nums)
        print(nums_sorted)
        for i in range(0, len(nums_sorted)-1):
            if (nums_sorted[i] == nums_sorted[i+1]):
                return True
        return False