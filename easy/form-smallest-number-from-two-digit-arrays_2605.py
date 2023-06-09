class List(list):
    ...


# my Solution
class Solution:
    def minNumber(self, nums1: List[int], nums2: List[int]) -> int:
        l1, l2 = set(nums1), set(nums2)
        l1_min = min(l1)
        l2_min = min(l2)
        if l1 & l2:
            return min(l1 & l2)
        if l1_min > l2_min:
            l1_min, l2_min = l2_min, l1_min
        return int(f"{l1_min}{l2_min}")


# Solution rock
def minNumber(self, nums1: List[int], nums2: List[int]) -> int:
    s1, s2 = set(nums1), set(nums2)
    if s1 & s2:
        return min(s1 & s2)
    a, b = min(nums1), min(nums2)
    return min(a, b) * 10 + max(a, b)


sol = Solution()
nums1 = [4, 1, 3]
nums2 = [5, 7]
print(sol.minNumber(nums1, nums2))
