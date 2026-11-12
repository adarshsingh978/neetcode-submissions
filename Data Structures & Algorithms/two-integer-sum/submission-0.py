class Solution:
    def twoSum(self, arr: List[int], target: int) -> List[int]:
        d = dict()
        for i in range(len(arr)):
            if target - arr[i] in d:
                t = target - arr[i]
                return [d[t], i]
            elif arr[i] not in d:
                d[arr[i]] = i

    # 3:0
    # 4:1
    # 5:3
    # 6:4

    # 4:0
    # 5:1
    # 6:2
        