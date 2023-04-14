from collections import deque
import heapq


class List(list):
    ...



class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = deque(sorted(stones, reverse=True))
        x = 0
        y = 1
        print(heap)
        while len(heap) - 1 >= 1:
            if heap[x] == heap[y]:
                heap.popleft()
                heap.popleft()
            elif heap[x] != heap[y]:
                result = heap[x] - heap[y]
                if result == 1:
                    heap.append(result)
                    heap.popleft()
                    heap.popleft()
                elif result != 1:
                    heap.popleft()
                    heap.popleft()
                    heap.appendleft(result)
        if heap:
            return heap[x]
        return x

# 1 1 2 4 7 8
if __name__ == '__main__':
    sol = Solution()
    stones = [2,7,4,1,8,1]
    print(sol.lastStoneWeight(stones))

    stones = [1]
    print(sol.lastStoneWeight(stones))

    stones = [1,1,1,1,1,1]
    print(sol.lastStoneWeight(stones))
    

    stones = [1,3]
    print(sol.lastStoneWeight(stones))

    stones = [2,7,4,1,8,1, 500, 1000]
    print(sol.lastStoneWeight(stones))


    stones = [7,6,7,6,9]
    print(sol.lastStoneWeight(stones))
# class Solution:
#     def lastStoneWeight(self, stones: List[int]) -> int:
#         heap = deque(sorted(stones))
#         length = len(heap) -1
#         if length == 0:
#              return stones[length]
#         x = 0
#         y = 1
#         while len(heap) > 1:

#             if heap[x] == heap[y]:
#                 heap.popleft()
#                 heap.popleft()
#                 x = 0
#                 y = 1
#             elif x != y:
#                 heap[y] = heap[y] - heap[x]
#                 del  heap[x]
#                 if len(heap) > 1:
#                     x = 1
#                     y = 2
#                 else:
#                     x = 0
#                     y = 1
#         if not heap:
#             return 0
#         return heap[0]


# class Solution:
#     def lastStoneWeight(self, stones: List[int]) -> int:
#         heap = deque(sorted(stones))
#         x = 0
#         y = 1
#         while len(heap) - 1 >= 1:
#             if heap[x] == heap[y]:
#                 heap.popleft()
#                 heap.popleft()
#                 x = 0
#                 y = 1
#             elif heap[x] != heap[y]:
#                 heap[x] = abs(heap[y] - heap[x])
#                 del heap[y]
#                 if len(heap) > 2:
#                     x = 1
#                     y = 2
#                 if len(heap) <= 2:
#                     x = 0
#                     y = 1
#         if heap:
#             return heap[x]
#         return x