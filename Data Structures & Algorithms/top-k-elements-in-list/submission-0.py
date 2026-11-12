class Solution:
    def topKFrequent(self, arr: List[int], k: int) -> List[int]:
        heap = []
        d = {}
        for i in range(len(arr)):
            d[arr[i]] = 1 + d.get(arr[i],0)
        for key,val in d.items():
            heapq.heappush(heap,(-val,key))
        res = []
        for i in range(k):
            top = heapq.heappop(heap)
            res.append(top[1])
        return res
        
        