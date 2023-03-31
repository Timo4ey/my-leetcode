# https://leetcode.com/problems/running-sum-of-1d-array/
# My solution

# Time complexity O(N)

List = list

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        output = []
        for i in range(len(nums)):
            output.append(sum(nums[:i+1]))
        return output


if __name__ == '__main__':
    s = Solution()
    print(s.runningSum([1,2,3,4]))
    print(s.runningSum([1,1,1,1,1]))
    print(s.runningSum([3,1,2,10,1]))
