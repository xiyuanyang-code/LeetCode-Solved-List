#
# @lc app=leetcode id=207 lang=python3
#
# [207] Course Schedule
#

from typing import List, Dict
from collections import deque


# @lc code=start
class Solution:
    def topological_sort_bfs(self, graph: Dict):
        in_degree = {}
        result = []
        queue = deque([])

        # counting all the in_degree of the models
        for node, neighbors in graph.items():
            if node not in in_degree:
                in_degree[node] = 0
            for neighbor in neighbors:
                if neighbor not in in_degree:
                    in_degree[neighbor] = 0
                in_degree[neighbor] += 1

        for node, neighbors in graph.items():
            if in_degree[node] == 0:
                queue.append(node)

        while queue:
            current_node = queue.popleft()
            result.append(current_node)
            for neighbor in graph[current_node]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        # cyclic detections
        if len(result) != len(graph):
            return None

        return result

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {}
        for i in range(numCourses):
            graph[i] = []
        for a,b in prerequisites:
            graph[a].append(b)
        result = self.topological_sort_bfs(graph=graph)
        if not result:
            return False
        else:
            return True
        
        pass


# @lc code=end
