class Solution:
    def largestAltitude(self, gain: list[int]) -> int:
        prefix_sum = 0
        max_sum = 0
        for height in gain:
            prefix_sum += height
            max_sum = max(max_sum, prefix_sum)
        return max_sum
