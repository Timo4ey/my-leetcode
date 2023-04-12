class List(list):
    pass




class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # 10-->15-->20
        acc = 0
        for i in range(1, len(cost) - 1):
            if cost[i-1] <= cost[i] < cost[i + 1]:
                acc += cost[i]
            elif cost[i-1] < cost[i] > cost[i + 1]:
                acc += cost[i-1]
            elif cost[i-1] >= cost[i] >= cost[i + 1]:
                acc += cost[i]
        return acc


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # 10-->15-->20
        acc = 0
        for i in range(len(cost) - 2):
            if cost[i] <= cost[i + 1] < cost[i + 2]:
                acc += cost[i + 1]
            elif cost[i] >= cost[i + 1]:
                acc += cost[i + 1]
            elif cost[i] < cost[i + 1]:
                acc += cost[i]
        return acc


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        length = len(cost)
        if length <= 3:
            return cost[1]
        acc = 0
        index = 0
        while index <= length - 1:

            if cost[index] < cost[index + 1]:
                acc += cost[index]
                index += 1
            
            elif  cost[index] >= cost[index + 1]:
                acc += cost[index + 1]
                index += 2

            if index > length:
                break
        return acc



class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        length = len(cost)
        midl = length // 2
        acc = 0
        index = 0
        while index < length - 1:

            if cost[index] < cost[index + 1]:
                if index + 2 < length and  cost[index + 1] >=  cost[index + 2]:
                    acc += cost[index + 1]
                    index += 2
                else:
                    acc += cost[index]
                    index += 1
            
            elif  cost[index] >= cost[index + 1]:
                acc += cost[index + 1]
                index += 2

            if index >= length:
                break
        return acc




class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        length = len(cost)
        acc = 0
        index = 0
        while index < length - 1:
            if cost[index] != 0 and index + 2 < length and cost[index + 1] <=  cost[index + 2]:
                acc += cost[index + 1]
                index += 2

            elif cost[index] < cost[index + 1] and index + 2 < length and cost[index + 1] <=  cost[index + 2]:
                acc += cost[index + 1]
                index += 2

            elif cost[index] < cost[index + 1]:
                acc += cost[index]
                index += 1
            
            elif  cost[index] >= cost[index + 1]:
                acc += cost[index + 1]
                index += 2

            if index >= length:
                break
        return acc

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        length = len(cost)
        if length == 2:
            return min(cost)
        acc = 0
        index = 0
        # 1      1   1     1 1  
        # [1,100,1,1,1,100,1,1,100,1]
        #  0  1  2
        #          3 4
        while index < length - 2:
            cur_sum = cost[index] + cost[index + 1] 
            if index + 2 <= length:
                
                if cur_sum >= cost[index + 2]:
                    acc += min(cost[index: index+1])
                    index += 2
                elif cur_sum <= cost[index + 2]:
                    acc += max(cost[index: index+1])
                    index += 1
            elif index + 1 == length:
                acc += min(cost[index: index+1])
                break
        # acc += min(cost[index: index+1])
        return acc

# class Solution:
#     def minCostClimbingStairs(self, cost: List[int]) -> int:
#         length = len(cost)
#         if length == 2:
#             return min(cost)
        

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        length = len(cost)
        if length == 2:
            return min(cost)
        
        # if length == 3:
        #     if cost[1] < cost[2]:
        #         return cost[1]
        #     return cost[0]

        acc = 0
        index = 0
        last_index = 0
        # 1      1   1     1 1  
        # [1,100,1,1,1,100,1,1,100,1]
        #  0  1  2
        #          3 4
        while index < length - 2:
            # if index + 1 < length - 1:
            if cost[index + 1] >= cost[index + 2]:
                acc += cost[index]
                last_index = index
                index += 2
            elif cost[index + 1] <= cost[index + 2]:
                last_index = index
                acc += cost[index + 1]
                index += 2
        print(last_index)
        while last_index < length - 2:
            if cost[last_index] <= cost[last_index + 1]:
                acc += cost[last_index]
                last_index += 1
            elif cost[last_index] > cost[last_index + 1]:
                last_index += 1
                acc += cost[last_index + 1]
        # acc += min(cost[index: index+1])
        return acc


# class Solution:
#     def minCostClimbingStairs(self, cost: List[int]) -> int:
#         length = len(cost)
#         if length == 2:
#             return min(cost)
#         acc = 0
#         index = 0
#         # 1      1   1     1 1  
#         # [1,100,1,1,1,100,1,1,100,1]
#         #  0  1  2
#         #          3 4
#         while index < length - 2:
#             if index + 2 <= length:
                
#                 if cost[index + 1] >= cost[index + 2]:
#                     acc += cost[index]
#                     index += 2
#                 elif cost[index + 1] < cost[index + 2]:
#                     acc += cost[index]
#                     index += 2

#         # acc += min(cost[index: index+1])
#         return acc




s = Solution()
print(s.minCostClimbingStairs([10,15,20]))
print(s.minCostClimbingStairs([1,100,1,1,1,100,1,1,100,1]))
print(s.minCostClimbingStairs([0,2,3,2]))



[10,15,20]
[1,100,1,1,1,100,1,1,100,1]
[10, 15]
[15, 10]
[1,100,1]
[100, 1, 100, 1 ,10, 1]
[0,1,2,2]
[0,1, 0,1,2,2]
[0,2,3,2]