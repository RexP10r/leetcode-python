class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        new: list[int] = [0] * len(nums)
        i = 0
        j = len(nums) - 1
        for k in range(len(nums) - 1, -1, -1):
            if abs(nums[i]) >= abs(nums[j]):
                new[k] = nums[i] ** 2
                i += 1
            else:
                new[k] = nums[j] ** 2
                j -= 1
        return new
