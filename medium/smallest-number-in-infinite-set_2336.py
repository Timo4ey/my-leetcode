# Implement the SmallestInfiniteSet class:

# SmallestInfiniteSet() Initializes the SmallestInfiniteSet object to contain all positive integers.
# int popSmallest() Removes and returns the smallest integer contained in the infinite set.
# void addBack(int num) Adds a positive integer num back into the infinite set, if it is not already in the infinite set.


# Example 1:

# Input
# ["SmallestInfiniteSet", "addBack", "popSmallest", "popSmallest", "popSmallest", "addBack", "popSmallest", "popSmallest", "popSmallest"]
# [[], [2], [], [], [], [1], [], [], []]
# Output
# [null, null, 1, 2, 3, null, 1, 4, 5]

# Explanation
# SmallestInfiniteSet smallestInfiniteSet = new SmallestInfiniteSet();
# smallestInfiniteSet.addBack(2);    // 2 is already in the set, so no change is made.
# smallestInfiniteSet.popSmallest(); // return 1, since 1 is the smallest number, and remove it from the set.
# smallestInfiniteSet.popSmallest(); // return 2, and remove it from the set.
# smallestInfiniteSet.popSmallest(); // return 3, and remove it from the set.
# smallestInfiniteSet.addBack(1);    // 1 is added back to the set.
# smallestInfiniteSet.popSmallest(); // return 1, since 1 was added back to the set and
#                                    // is the smallest number, and remove it from the set.
# smallestInfiniteSet.popSmallest(); // return 4, and remove it from the set.
# smallestInfiniteSet.popSmallest(); // return 5, and remove it from the set.

# ---------------------------------------Runtime 130 mss Beats 33.62% Memory 17.1 MB Beats 10.48%---------------------------------------
from sortedcontainers import SortedSet


class SmallestInfiniteSet:
    def __init__(self):
        self.smallSet = SortedSet()
        self.curr_int = 1

    def popSmallest(self) -> int:
        if len(self.smallSet):
            smallest = self.smallSet[0]
            self.smallSet.discard(smallest)
        else:
            smallest = self.curr_int
            self.curr_int += 1
        return smallest

    def addBack(self, num: int) -> None:
        if self.curr_int <= num or num in self.smallSet:
            return
        self.smallSet.add(num)
