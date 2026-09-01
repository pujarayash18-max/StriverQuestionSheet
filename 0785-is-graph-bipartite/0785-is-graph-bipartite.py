class Solution:
    def isBipartite(self, graph):
        color = [0] * len(graph)

        def dfs(node, c):
            color[node] = c

            for nei in graph[node]:
                if color[nei] == 0:
                    if not dfs(nei, -c):
                        return False
                elif color[nei] == color[node]:
                    return False

            return True

        for i in range(len(graph)):
            if color[i] == 0:
                if not dfs(i, 1):
                    return False

        return True
        