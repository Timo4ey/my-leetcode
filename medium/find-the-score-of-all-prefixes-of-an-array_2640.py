

from itertools import accumulate


class List(list):
    ...


    
# My solution
class Solution:
    def findPrefixScore(self, nums: List[int]) -> List[int]:
        # define current maximum
        cur_mx = nums[0]
        # get first element that the func `max` doesn't return 
        # an error 'ValueError: max() arg is an empty sequence' 
        sum_ = nums[0] * 2
        # put our sum into list
        ans = [sum_]
        for i in range(1, len(nums)):
            # get max number for sum the next element num[0...i]
            cur_mx = max(cur_mx, nums[i])
            # sum elements
            sum_ += cur_mx + nums[i]
            ans.append(sum_ )
        return ans

# Solution SunnyvaleCA
def findPrefixScore(self, A):
    return accumulate(n+maxN for n,maxN in zip(A, accumulate(A,max)))




sol = Solution()
nums = [2,3,7,5,10]
print(sol.findPrefixScore(nums))
nums = [1,1,2,4,8,16]
print(sol.findPrefixScore(nums))




# My solution with bad time 


class Solution:
    def findPrefixScore(self, nums: List[int]) -> List[int]:
        output = []
        count = 0
        while count <= len(nums) - 1:
            output.append(nums[count] + max(nums[:count + 1]))
            count += 1
        count = 0
        while count <= len(output) - 1:
            mx = 0
            if output[:count]:
                mx = max(output[:count])
            output[count] = output[count] + mx
            count += 1
        return output