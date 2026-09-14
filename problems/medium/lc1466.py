class Solution:
    def minReorder(self, n: int, connections: list[list[list]]) -> int:
        all = [[] for _ in range(n)]
        for u, v in connections:
            all[u].append(v)
            all[v].append(-u)

        visited = [False] * n

        def dfs(src: int) -> int:
            visited[src] = True
            count = 0
            for dest in all[src]:
                next_node = abs(dest)
                if not visited[next_node]:
                    if dest > 0:
                        count += 1
                    count += dfs(next_node)
            return count

        return dfs(0)
