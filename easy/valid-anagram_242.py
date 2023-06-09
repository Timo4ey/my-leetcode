# My solution
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        def get_dict(array):
            temp_dict = {}
            for i in array:
                if not temp_dict.get(i):
                    temp_dict[i] = 1
                else:
                    temp_dict[i] += 1
            return temp_dict

        s1 = get_dict(s)
        t1 = get_dict(t)
        return s1 == t1


# My solution 2


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        def get_dict(array):
            temp_dict = {}
            for i in array:
                temp_dict[i] = temp_dict.get(i, 0) + 1
            return temp_dict

        s1 = get_dict(s)
        t1 = get_dict(t)
        return s1 == t1
