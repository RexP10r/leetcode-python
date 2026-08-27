class Solution:
    def equalPairs(self, grid: list[list[int]]) -> int:
        row_counts = {}
        for row in grid:
            row = tuple(row)
            row_counts[row] = row_counts.get(row, 0) + 1

        size = len(grid)
        total_count = 0
        for col_idx in range(size):
            col = tuple(grid[row_idx][col_idx] for row_idx in range(size))
            total_count += row_counts.get(col, 0)

        return total_count
