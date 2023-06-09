class List(list):
    ...


# MY solution
class Solution:
    def leftRigthDifference(self, nums: List[int]) -> List[int]:
        output = []
        count = 0
        while count != len(nums):
            output.append(
                abs(sum(nums[:count]) - abs((nums[count] - sum(nums[count:]))))
            )
            count += 1

        return output
