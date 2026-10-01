import heapq


class Solution:
    def maxScore(self, nums1: list[int], nums2: list[int], k: int) -> int:
        pairs = sorted(zip(nums2, nums1), reverse=True)
        min_heap = []
        current_sum = 0
        max_sum = 0
        for n2, n1 in pairs:
            heapq.heappush(min_heap, n1)
            current_sum += n1

            if len(min_heap) > k:
                current_sum -= heapq.heappop(min_heap)

            if len(min_heap) == k:
                max_sum = max(max_sum, current_sum * n2)
        return max_sum
