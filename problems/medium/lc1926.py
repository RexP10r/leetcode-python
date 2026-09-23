class Solution:
    def nearestExit(self, maze: list[list[str]], entrance: list[int]) -> int:
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        queue = []
        queue.append(entrance)
        maze[entrance[0]][entrance[1]] = "+"
        n, m = len(maze), len(maze[0])
        max_path = 0
        while queue:
            temp = []
            for _ in range(len(queue)):
                i, j = queue.pop()
                for di, dj in directions:
                    new_i = di + i
                    new_j = dj + j
                    if 0 <= new_i < n and 0 <= new_j < m and maze[new_i][new_j] == ".":
                        if new_i == 0 or new_i == n - 1 or new_j == 0 or new_j == m - 1:
                            return max_path + 1

                        temp.append([new_i, new_j])
                        maze[new_i][new_j] = "+"
            queue = temp
            max_path += 1

        return -1
