class List(list):
    pass


class Solution:
    def floodFill(
        self, image: List[List[int]], sr: int, sc: int, color: int
    ) -> List[List[int]]:
        output = image[:]
        pivot = image[sr][sc]
        for i in range(0, len(image)):
            for j in range(0, len(image)):
                if output[i][j] == output[sr][sc]:
                    # if output[i][j] == pivot:
                    output[i][j] = color
                # if output[i][sc] != pivot:

        return output


if __name__ == "__main__":
    s1 = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
    s = Solution()
    print(s.floodFill(s1, 1, 1, 2))


1
1
2
[[0, 0, 0], [0, 0, 0]]
0
0
0
