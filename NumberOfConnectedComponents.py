class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        seen = set()
        graph = {i:[] for i in range(n)}
        res = 0
        
        # Create Graph
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        # Depth-First search through the graph and add all seen nodes to the set
        def DFS(node):
            seen.add(node)
            
            for neighbor in graph[node]:
                if neighbor not in seen:
                    DFS(neighbor)
        
        for i in range(n):
            if i not in seen:
                DFS(i)
                res += 1
        
        return res
