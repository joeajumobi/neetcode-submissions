class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        fList = [[] for i in range(len(nums)+1)]

        for n in nums:
            count[n] = 1 + count.get(n, 0)

        for i, n in count.items():
            fList[n].append(i)
        
        output = []
        for i in range(len(fList) -1, 0 , -1):
            for n in fList[i]:
                output.append(n)
                if len(output) == k:
                    return output