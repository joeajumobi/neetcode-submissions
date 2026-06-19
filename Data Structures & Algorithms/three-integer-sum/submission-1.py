class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #return a list of triplets that equal 0 when summed together
        #input is a random list of numbers not in any particular order
         
        
        #establish a list variable of dynamic size
        #make 2 pointers that will go through the list
        #establish some sort of loop going through the list
        nums.sort()
        numList = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            left = i +1 
            right = len(nums) - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total < 0:
                    left +=1
                elif total > 0:
                    right -=1
                else:
                    numList.append([nums[i],nums[left],nums[right]])

                    while left < right and nums[left] == nums[left+1]:
                        left+=1
                    while left < right and nums[right] == nums[right-1]:
                        right -=1
                    
                    left+=1
                    right-=1
                    
        return numList
            
            