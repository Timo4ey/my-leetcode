# You have a browser of one tab where you start on the homepage and you can visit another url, get back in the history number of steps or move forward in the history number of steps.

# Implement the BrowserHistory class:

# BrowserHistory(string homepage) Initializes the object with the homepage of the browser.
# void visit(string url) Visits url from the current page. It clears up all the forward history.
# string back(int steps) Move steps back in history. If you can only return x steps in the history and steps > x, you will return only x steps. Return the current url after moving back in history at most steps.
# string forward(int steps) Move steps forward in history. If you can only forward x steps in the history and steps > x, you will forward only x steps. Return the current url after forwarding in history at most steps.

# Example:

# Input:
# ["BrowserHistory","visit","visit","visit","back","back","forward","visit","forward","back","back"]
# [["leetcode.com"],["google.com"],["facebook.com"],["youtube.com"],[1],[1],[1],["linkedin.com"],[2],[2],[7]]
# Output:
# [null,null,null,null,"facebook.com","google.com","facebook.com",null,"linkedin.com","google.com","leetcode.com"]

# Explanation:
# BrowserHistory browserHistory = new BrowserHistory("leetcode.com");
# browserHistory.visit("google.com");       // You are in "leetcode.com". Visit "google.com"
# browserHistory.visit("facebook.com");     // You are in "google.com". Visit "facebook.com"
# browserHistory.visit("youtube.com");      // You are in "facebook.com". Visit "youtube.com"
# browserHistory.back(1);                   // You are in "youtube.com", move back to "facebook.com" return "facebook.com"
# browserHistory.back(1);                   // You are in "facebook.com", move back to "google.com" return "google.com"
# browserHistory.forward(1);                // You are in "google.com", move forward to "facebook.com" return "facebook.com"
# browserHistory.visit("linkedin.com");     // You are in "facebook.com". Visit "linkedin.com"
# browserHistory.forward(2);                // You are in "linkedin.com", you cannot move forward any steps.
# browserHistory.back(2);                   // You are in "linkedin.com", move back two steps to "facebook.com" then to "google.com". return "google.com"
# browserHistory.back(7);                   // You are in "google.com", you can move back only one step to "leetcode.com". return "leetcode.com"

# Constraints:

# 1 <= homepage.length <= 20
# 1 <= url.length <= 20
# 1 <= steps <= 100
# homepage and url consist of  '.' or lower case English letters.
# At most 5000 calls will be made to visit, back, and forward.

# ---------------------------------------Runtime 290 ms Beats 9.90% Memory 19.10 MB Beats 78.70%---------------------------------------

from __future__ import annotations


class Node:
    def __init__(
        self, val: str = "", prev: Node = None, next: Node = None
    ) -> None:
        self.val = val
        self.prev = prev
        self.next = next


class LinkedList:
    Node: Node = Node

    def __init__(self) -> None:
        self.head = self.tail = self.current_node = None

    def append(self, value: str):
        if not self.head:
            self.head = self.Node(value)
            self.tail = self.head
            self.current_node = self.tail
            return
        if not self._is_equal():
            self._set_next_node(value)
            return
        node = self.head
        while node.next:
            node = node.next
        node.next = self.Node(value, node)
        self.tail = node.next
        self.current_node = self.tail

    def _set_next_node(self, site: str) -> None:
        self.current_node.next = Node(site, self.current_node)
        self.current_node = self.current_node.next
        self.tail = self.current_node

    def _is_equal(self) -> bool:
        """
        Compare values of cuttent_node and tail
        """
        return self.current_node == self.tail

    def go_next(self):
        if self.current_node.next:
            self.current_node = self.current_node.next

    def go_prev(self):
        if self.current_node.prev:
            self.current_node = self.current_node.prev

    def get_curr_value(self):
        return self.current_node.val


class BrowserHistory:

    def __init__(self, homepage: str):
        self.stack = LinkedList()
        self.stack.append(homepage)

    def visit(self, url: str) -> None:
        self.stack.append(url)

    def back(self, steps: int) -> str:
        while steps:
            steps -= 1
            self.stack.go_prev()
        return self.stack.get_curr_value()

    def forward(self, steps: int) -> str:
        while steps:
            steps -= 1
            self.stack.go_next()
        return self.stack.get_curr_value()
