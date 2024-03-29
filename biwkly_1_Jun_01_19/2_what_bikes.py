1066. Campus Bikes II
  User Accepted: 115
  User Tried: 280
  Total Accepted: 116
  Total Submissions: 796
  Difficulty: Medium
On a campus represented as a 2D grid, there are N workers and M bikes, with N <= M. Each worker and bike is a 2D coordinate on this grid.

We assign one unique bike to each worker so that the sum of the Manhattan distances between each worker and their assigned bike is minimized.

The Manhattan distance between two points p1 and p2 is Manhattan(p1, p2) = |p1.x - p2.x| + |p1.y - p2.y|.

Return the minimum possible sum of Manhattan distances between each worker and their assigned bike.

 

Example 1:



  Input: workers = [[0,0],[2,1]], bikes = [[1,2],[3,3]]
  Output: 6
  Explanation: 
  We assign bike 0 to worker 0, bike 1 to worker 1. The Manhattan distance of both assignments is 3, so the output is 6.


Example 2:



  Input: workers = [[0,0],[1,1],[2,0]], bikes = [[1,0],[2,2],[2,1]]
  Output: 4
  Explanation: 
  We first assign bike 0 to worker 0, then assign bike 1 to worker 1 or worker 2, bike 2 to worker 2 or worker 1. Both assignments lead to sum of the Manhattan distances as 4.
 

Note:

0 <= workers[i][0], workers[i][1], bikes[i][0], bikes[i][1] < 1000
All worker and bike locations are distinct.
1 <= workers.length <= bikes.length <= 10



from itertools import permutations, repeat
class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> int:
        def dis(i, j):
            return abs(workers[i][0] - bikes[j][0]) + abs(workers[i][1] - bikes[j][1])
        h = [[0, 0, 0]]
        seen = set()
        while True:
            cost, i, taken = heapq.heappop(h)
            if (i, taken) in seen: continue
            seen.add((i, taken))
            if i == len(workers):
                return cost
            for j in range(len(bikes)):
                if taken & (1 << j) == 0:
                    heapq.heappush(h, [cost + dis(i, j), i + 1, taken | (1 << j)])
                    
                    
#                    mine mine

#         distance = float("inf")
        
#         for j in [list(zip(range(10), p)) for p in permutations(range(10))]:
#             temp = 0
#             for i in range(len(j)): 
#                 wk = j[i][0]
#                 bk = j[i][1] 
#                 temp += abs(workers[wk][0] - bikes[bk][0]) + abs(workers[wk][1] - bikes[bk][1])
#                 if temp >= distance:
#                     break
#             if temp < distance:
#                 distance = temp
                
#         return distance


