# You are given an integer array matches where matches[i] = [winneri, loseri] indicates that the player winneri defeated player loseri in a match.

# Return a list answer of size 2 where:

# answer[0] is a list of all players that have not lost any matches.
# answer[1] is a list of all players that have lost exactly one match.
# The values in the two lists should be returned in increasing order.

# Note:

# You should only consider the players that have played at least one match.
# The testcases will be generated such that no two matches will have the same outcome.


# Example 1:

# Input: matches = [[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]]
# Output: [[1,2,10],[4,5,7,8]]
# Explanation:
# Players 1, 2, and 10 have not lost any matches.
# Players 4, 5, 7, and 8 each have lost one match.
# Players 3, 6, and 9 each have lost two matches.
# Thus, answer[0] = [1,2,10] and answer[1] = [4,5,7,8].
# Example 2:

# Input: matches = [[2,3],[1,3],[5,4],[6,4]]
# Output: [[1,2,5,6],[]]
# Explanation:
# Players 1, 2, 5, and 6 have not lost any matches.
# Players 3 and 4 each have lost two matches.
# Thus, answer[0] = [1,2,5,6] and answer[1] = [].


# Constraints:

# 1 <= matches.length <= 105
# matches[i].length == 2
# 1 <= winneri, loseri <= 105
# winneri != loseri
# All matches[i] are unique.


# ---------------------------------------Runtime 1424 ms Beats 83.24% Memory 73.21 MB Beats 7.53%---------------------------------------

from collections import defaultdict
from typing import List


class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        answer = []
        loosers_map = defaultdict(int)
        players = set()

        for match in matches:
            looser = match[1]
            loosers_map[looser] += 1
            players.add(looser)
            players.add(match[0])
        answer.append([p for p in players if p not in loosers_map])
        answer.append(
            [key for key, value in loosers_map.items() if value == 1]
        )
        if answer[0]:
            answer[0].sort()
        if answer[1]:
            answer[1].sort()
        return answer
