class List(list):
    ...


# My solution 

class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        d1 = dict(nums1)
        d2 = dict(nums2)
        for i in d2:
            d1[i] = d1.get(i, 0) + d2.get(i)
        return sorted(list(map(list, zip(d1.keys(), d1.values()))))
                