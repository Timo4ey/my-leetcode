# Design a HashMap without using any built-in hash table libraries.

# Implement the MyHashMap class:

# MyHashMap() initializes the object with an empty map.
# void put(int key, int value) inserts a (key, value) pair into the HashMap. If the key already exists in the map, update the corresponding value.
# int get(int key) returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key.
# void remove(key) removes the key and its corresponding value if the map contains the mapping for the key.


# Example 1:

# Input
# ["MyHashMap", "put", "put", "get", "get", "put", "get", "remove", "get"]
# [[], [1, 1], [2, 2], [1], [3], [2, 1], [2], [2], [2]]
# Output
# [null, null, null, 1, -1, null, 1, null, -1]

# Explanation
# MyHashMap myHashMap = new MyHashMap();
# myHashMap.put(1, 1); // The map is now [[1,1]]
# myHashMap.put(2, 2); // The map is now [[1,1], [2,2]]
# myHashMap.get(1);    // return 1, The map is now [[1,1], [2,2]]
# myHashMap.get(3);    // return -1 (i.e., not found), The map is now [[1,1], [2,2]]
# myHashMap.put(2, 1); // The map is now [[1,1], [2,1]] (i.e., update the existing value)
# myHashMap.get(2);    // return 1, The map is now [[1,1], [2,1]]
# myHashMap.remove(2); // remove the mapping for 2, The map is now [[1,1]]
# myHashMap.get(2);    // return -1 (i.e., not found), The map is now [[1,1]]

# ---------------------------------------Runtime 3736 ms Beats 5.2% Memory 20.2 MB Beats 51.68%---------------------------------------


class Node:
    def __init__(self, key=None, value=None):
        self.key: int = key
        self.value: int = value
        self.next = None


class MyHashMap:
    def __init__(self):
        self.hashmap = Node()

    def put(self, key: int, value: int) -> None:
        node: Node = self.hashmap
        if node is None:
            self.hashmap = Node(key, value)
            return

        if node.key is None:
            node.key = key
            node.value = value
        else:
            while node.next:
                if node.key == key:
                    node.value = value
                    break
                node = node.next
            if node.next is None:
                if node.key == key:
                    node.value = value
                else:
                    node.next = Node(key, value)

    def get(self, key: int) -> int:
        node: Node = self.hashmap
        while node:
            if node.key == key:
                return node.value
            node = node.next
        return -1

    def remove(self, key: int) -> None:
        node: Node = self.hashmap
        prev: Node = None

        if node is not None:
            if node.key == key:
                self.hashmap = node.next
                return

        while node:
            if node.key == key:
                if node and prev:
                    prev.next = node.next
                return
            prev = node
            node = node.next


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
