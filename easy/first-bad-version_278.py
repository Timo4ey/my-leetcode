class isBadVersion:
    ...

# My solution
class Solution:
    def firstBadVersion(self, n: int) -> int:
        start = 0
        finish = n
        results = []
        while start <= finish:
            midl = (start + finish) // 2
            result = isBadVersion(midl)
            if result:
                results.append(midl)
                finish = midl - 1
            else:
                start = midl + 1
        return min(results)

#  MVP
# class Solution:
#     def firstBadVersion(self, n: int) -> int:
#         start = 0
#         finish = n
#         results = []
#         for x in range(n,0, -1):
#             if isBadVersion(x):
#                 results.append(x)
#         return min(results)


# Solution GANJINAVEEN

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left,right=0,n-1
        while left<=right:
            mid=(left+right)//2
            if isBadVersion(mid)==False:
                left=mid+1
            else:
                right=mid-1
        return left
    
class Solution:
    def firstBadVersion(self, n: int) -> int:
        start = 0
        finish = n
        results = {}
        while start <= finish:
            midl = (start + finish) // 2
            result = isBadVersion(midl)
            if result:
                results[midl] = midl
                finish = midl - 1
            else:
                start = midl + 1
        return min(results, key=results.get)