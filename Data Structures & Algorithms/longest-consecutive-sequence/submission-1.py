class Solution:
    def check(self,i,nums):
        Tres = 0 
        while True:
            if i + 1 in nums:
                Tres += 1
                i += 1
            else:
                return Tres


    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == None or len(nums) == 0:
            return 0
        nums = set(nums)
        res = 0
        for i in nums:
            tempRes = 0
            print(f'{i=}')
            if i-1 not in nums:
                tempRes = self.check(i,nums)
            print(f'{tempRes=} , {res=}')
            if tempRes > res:
                res = tempRes
        return res + 1



        