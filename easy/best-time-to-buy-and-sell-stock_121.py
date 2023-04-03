class List(list):
    pass


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minimum = float('inf')
        maximum = 0
        for i in range(len(prices)):
            result = prices[i] - minimum
            if prices[i] < minimum:
                minimum = prices[i]
            
            elif result > maximum:
                maximum = result
        return maximum


def counter():
    count = 1
    while True:
        yield count
        count += 1

a = counter()
if __name__ == "__main__":
    ts1 = [7,1,5,3,6,4]
    ts2 = [7,6,4,3,1]
    ts3 = [2,4,1]
    ts4 = [7,1,5,3,6,4]
    ts5 = [7,6,4,3,1]
    ts6 = [1,2,3,4,5]
    ts7 = [3,3]
    ts8 = [2,3,1,5,6,7,1]
    ts9 = [2,1]
    ts10 = [3,2,6,5,0,3]
    ts11 = [2,1,2,0,1]
    ts12 = [2,1,2,1,0,0,1]
    ts13 = [2,1,2,1,0,1,2]
    ts14 = [4,2,1,7]
    ts15 = [3,3,5,0,0,3,1,4]
    ts16 = [2,11,1,4,7]
    ts17 = [2,1,4]
    ts18 = [11,7,4,1,2]
    sol = Solution()
    # print(sol.maxProfit(ts1))
    print(f'ts-{next(a)}:',sol.maxProfit(ts1) , sol.maxProfit(ts1) == 5, 'Except:', 5)
    print(f'ts-{next(a)}:',sol.maxProfit(ts2) , sol.maxProfit(ts2) == 0, 'Except:', 0)
    print(f'ts-{next(a)}:',sol.maxProfit(ts3) , sol.maxProfit(ts3) == 2, 'Except:', 2)
    print(f'ts-{next(a)}:',sol.maxProfit(ts4) , sol.maxProfit(ts4) == 5, 'Except:', 5)
    print(f'ts-{next(a)}:',sol.maxProfit(ts5) , sol.maxProfit(ts5) == 0, 'Except:', 0)
    print(f'ts-{next(a)}:',sol.maxProfit(ts6) , sol.maxProfit(ts6) == 4, 'Except:', 4)
    print(f'ts-{next(a)}:',sol.maxProfit(ts7) , sol.maxProfit(ts7) == 0, 'Except:', 0)
    print(f'ts-{next(a)}:',sol.maxProfit(ts8) , sol.maxProfit(ts8) == 6, 'Except:', 6)
    print(f'ts-{next(a)}:',sol.maxProfit(ts9) , sol.maxProfit(ts9) == 0, 'Except:', 0)
    print(f'ts-{next(a)}:',sol.maxProfit(ts10) , sol.maxProfit(ts10) == 4, 'Except:', 4)
    print(f'ts-{next(a)}:',sol.maxProfit(ts11) , sol.maxProfit(ts11) == 1, 'Except:', 1)
    print(f'ts-{next(a)}:',sol.maxProfit(ts12) , sol.maxProfit(ts12) == 1, 'Except:', 1)
    print(f'ts-{next(a)}:',sol.maxProfit(ts13) , sol.maxProfit(ts13) == 2, 'Except:', 2)
    print(f'ts-{next(a)}:',sol.maxProfit(ts13) , sol.maxProfit(ts13) == 2, 'Except:', 2)
    print(f'ts-{next(a)}:',sol.maxProfit(ts14) , sol.maxProfit(ts14) == 6, 'Except:', 6)
    print(f'ts-{next(a)}:',sol.maxProfit(ts15) , sol.maxProfit(ts15) == 4, 'Except:', 4)
    print(f'ts-{next(a)}:',sol.maxProfit(ts16) , sol.maxProfit(ts16) == 9, 'Except:', 9)
    print(f'ts-{next(a)}:',sol.maxProfit(ts17) , sol.maxProfit(ts17) == 3, 'Except:', 3)
    print(f'ts-{next(a)}:',sol.maxProfit(ts18) , sol.maxProfit(ts18) == 1, 'Except:', 1)









# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         buy = min_num= 0
#         sell = max_num = len(prices) - 1
#         while sell >= 0:
#             point_1 = prices[buy]
#             point_2 = prices[sell]
#             max_point = prices[max_num]
#             min_point = prices[min_num]

#             if max_point < point_2 and sell > min_num:
#                 max_num = sell
#             if min_point > point_1 and sell != buy < max_num:
#                 min_num = buy
#             elif sell == buy:
#                 buy -= 1
#             sell-= 1
#             buy += 1
#         return prices[max_num] - prices[min_num] if prices[max_num] - prices[min_num] > 0 else 0


# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         buy = min_num= 0
#         sell = max_num = len(prices) - 1
#         while sell >= 0:
#             point_1 = prices[buy]
#             point_2 = prices[sell]
#             max_point = prices[max_num]
#             min_point = prices[min_num]

#             if max_point < point_2 and sell > min_num:
#                 max_num = sell
#             if min_point > point_1 and sell != buy < max_num:
#                 min_num = buy
#             elif sell == buy:
#                 buy -= 1
#             sell-= 1
#             buy += 1
#         return prices[max_num] - prices[min_num] if prices[max_num] - prices[min_num] > 0 else 0


    # class Solution:
    # def maxProfit(self, prices: List[int]) -> int:
    #     buy = 0
    #     sell = max_num = len(prices) - 1
    #     while buy < sell:
    #         point_1 = prices[buy]
    #         point_2 = prices[sell]
    #         point_3 = prices[max_num]
    #         if point_1 > point_2 and sell == len(prices) - 1 or point_2 == 0:
    #             sell -= 1

    #         elif point_1 > point_2:
    #             if point_3 < point_2:
    #                 max_num -=1
    #             buy += 1
                
    #         elif point_1 <= point_2:
    #             if point_3 <point_2:
    #                 max_num -=1
    #             sell -= 1
        
    #     if buy >= max_num or (prices[max_num] - prices[buy] <= 0):
    #         return 0
    #     return prices[max_num] - prices[buy]

    # class Solution:
    # def maxProfit(self, prices: List[int]) -> int:
    #     buy = max_num = min_num= 0
    #     sell = len(prices) - 1
    #     while buy <= sell:
    #         point_1 = prices[buy]
    #         point_2 = prices[sell]
    #         if max_num == 0 or max_num < point_2:
    #             max_num = point_2
    #         if min_num == 0 or min_num > point_1:
    #             min_num = point_1
    #         buy+=1
    #         sell -=2
        
    #     return max_num - min_num if max_num - min_num > 0 else 0
