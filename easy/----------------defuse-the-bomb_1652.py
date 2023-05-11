class List(list):
    pass


class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        count = 0
        output = []
        i = 1
        while count < len(code):
            
            if i > len(code):
                i = i - k
                output.append(sum())

            

sol = Solution()
code = [5,7,1,4]
k = 3
print(sol.decrypt(code, k ))

code = [1,2,3,4]
k = 0

print(sol.decrypt(code, k ))

code = [2,4,9,3]
k = -2

print(sol.decrypt(code, k ))

# class Solution:
#     def decrypt(self, code: List[int], k: int) -> List[int]:
#         output = []
#         length = len(code)
#         for num in range(length):
#             output.append(0)
#             for it in range(num + 1, k + 1):
#                 if it > length:
#                     it = -it
#                 output[num] += code[it]
#         return output


# class Solution:
#     def decrypt(self, code: List[int], k: int) -> List[int]:
#         output = []
#         length = len(code)
#         count = 2
#         for num in range(length):
#             f = num + 1
#             new_k = k + 1
#             cur_nums = code[f:new_k]
#             if (length - f) >= k:
#                 output.append(sum(cur_nums))
#             elif (length - f) < new_k:
#                 min_k = -new_k 
#                 min_num = -num + count
#                 min_nums = code[min_k:min_num]

#                 output.append(sum(cur_nums) + sum(min_nums) )
#                 count += 2
#         return output