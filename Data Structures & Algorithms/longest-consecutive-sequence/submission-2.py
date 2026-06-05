class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #a set for all the numbers for quick access
        new_set = set(nums)
        # a loop that goes through each number and increments a counter by one if 
        #the the current +1 exists in the set
        #this loop will also 
        longest = 0

        for num in new_set:
            if num-1 not in new_set:
                length = 1
                current = num

                while current + 1 in new_set:
                    length += 1
                    current +=1

                longest = max(longest,length)

        return longest
            