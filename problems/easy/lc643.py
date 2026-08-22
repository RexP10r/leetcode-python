class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        sum = 0
        for i in range(k):
            sum += nums[i]
        max_sum = sum
        for i in range(k, len(nums)):
            sum = sum - nums[i - k] + nums[i]
            max_sum = max(max_sum, sum)
        return max_sum / k
