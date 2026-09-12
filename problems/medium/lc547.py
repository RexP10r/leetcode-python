class Solution:
    def findCircleNum(self, isConnected: list[list[int]]) -> int:
        seen = [False] * len(isConnected)
        provinces = 0

        def dfs(u: int):
            nonlocal seen
            seen[u] = True
            for v in range(len(isConnected)):
                if isConnected[u][v] and not seen[v]:
                    dfs(v)

        for v in range(len(isConnected)):
            if not seen[v]:
                provinces += 1
                dfs(v)
        return provinces
