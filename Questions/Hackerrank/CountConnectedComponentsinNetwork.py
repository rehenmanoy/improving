"""
Count Connected Components in Network
-------------------------------------

Problem:
    We have n computers labeled from 0 to n-1.
    We are also given a list of bidirectional links where each link [u, v]
    means computer u is directly connected to computer v (and v to u).

    A "connected component" (or communication group) means:
        - A set of computers where each computer can reach the others
          through some chain of links.
        - Groups do not connect to each other.

Goal:
    Return how many separate communication groups exist.

Example:
    n = 4
    links = [[0, 1], [2, 3]]

    Computers 0 and 1 form one group.
    Computers 2 and 3 form another group.
    There are 2 groups → answer = 2.

Approach (DFS):
    1. Build a graph from the links using an adjacency list.
       For each [u, v], we add v to u's neighbor list and u to v's list
       because the graph is undirected.

    2. Use a 'visited' set to track which computers have been explored.

    3. For each computer from 0 to n-1:
         - If it has not been visited yet, this means we found a new
           disconnected group.
         - We run DFS starting from this computer, which visits all
           computers reachable from it.
         - After DFS finishes, we increase our component count by 1.

    4. The total number of times we start DFS is equal to the total number
       of connected components.

Why DFS works:
    DFS (Depth-First Search) explores all nodes connected to a starting node.
    Running DFS from every unvisited node ensures we count each independent
    group exactly once.

Time Complexity:
    O(n + e)
       n = number of computers
       e = number of links

Space Complexity:
    O(n + e) for graph storage and visited set.
"""
from collections import defaultdict
def countIsolatedCommunicationGroups(links, n):
    graph = defaultdict(list)
    for u , v in links:
        graph[u].append(v)
        graph[v].append(u)
    
    visited = set()
    components = 0
    
    def dfs(start):
        stack = [start]
        visited.add(start)
        while stack:
            node = stack.pop()
            for nei in graph[node]:
                if nei not in visited:
                    visited.add(nei)
                    stack.append(nei)
    
    for node in range(n):
        if node not in visited:
            dfs(node)
            components += 1
    return components
    
