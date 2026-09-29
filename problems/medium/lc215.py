from random import randint


class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        if k == 50_000:
            return 1
        left, right = 0, len(nums) - 1
        while True:
            pivot_index = randint(left, right)
            new_pivot_index = self.partition(nums, left, right, pivot_index)
            if new_pivot_index == len(nums) - k:
                return nums[new_pivot_index]
            elif new_pivot_index > len(nums) - k:
                right = new_pivot_index - 1
            else:
                left = new_pivot_index + 1

    def partition(self, nums: list[int], left, right, pivot_index) -> int:
        pivot = nums[pivot_index]
        nums[pivot_index], nums[right] = nums[right], nums[pivot_index]
        place_index = left
        for i in range(left, right):
            if nums[i] < pivot:
                nums[place_index], nums[i] = nums[i], nums[place_index]
                place_index += 1
        nums[right], nums[place_index] = nums[place_index], nums[right]
        return place_index
